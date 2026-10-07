"""Read-only RKSI adapter. Export presentation meshes and seekable replay data."""
from pathlib import Path
import argparse, collections, hashlib, json, math, re, shutil, struct, sys
import numpy as np
from shapely.geometry import Polygon, LineString, Point, box
from shapely.geometry.polygon import orient
from shapely.ops import unary_union, transform
from shapely import constrained_delaunay_triangles, concave_hull
from airport_mockup_lights import build_lights
from airport_mockup_buildings import building_height, building_kind, build_general_volume, T2_COURTYARD_BUILDINGS
from airport_mockup_ground import restore_taxiway_islands
from airport_mockup_centerlines import build_taxiway_centerlines, collect_lead_in_lines
from airport_mockup_roads import build_access_roads
from airport_mockup_replay import export_replay, camera_metadata
from airport_mockup_terminals import terminal_vertex_lists

parser=argparse.ArgumentParser()
parser.add_argument('--source',type=Path,required=True)
parser.add_argument('--layout',type=Path)
parser.add_argument('--map',dest='map_path',type=Path)
parser.add_argument('--result',type=Path)
parser.add_argument('--out',type=Path)
parser.add_argument('--build',type=Path)
parser.add_argument('--icao',default='RKSI')
parser.add_argument('--airport',default='Incheon International Airport')
parser.add_argument('--city',default='Incheon, South Korea')
parser.add_argument('--center',nargs=2,type=float)
args=parser.parse_args()
args.source=args.source.resolve()
ROOT=Path(__file__).resolve().parents[1]
OUT=(args.out or ROOT/'web'/'airport-mockup').resolve(); OUT.mkdir(parents=True,exist_ok=True)
BUILD=(args.build or ROOT/'output'/'airport-mockup').resolve(); BUILD.mkdir(parents=True,exist_ok=True)
ASSETS=BUILD/'assets'; ASSETS.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(args.source))
from blueprint.layout.schema import flatten_grouped_layout_schema
from blueprint.map.geometry import _geom_to_xy_shape
from blueprint.map.rules import OSM_TO_LAYOUT_RULES
from blueprint.map.context_convert import _road_lane_counts

default_rksi=args.layout is None
layout_path=(args.layout or args.source/'data/layouts/RKSI_INITIAL_R1_NORMAL.json').resolve()
result_path=(args.result or args.source/'data/runs/RKSI_INITIAL_R1_NORMAL_sim_result.json') if default_rksi else args.result
raw=json.loads(layout_path.read_text(encoding='utf-8'))
layout=flatten_grouped_layout_schema(raw)
result=json.loads(result_path.read_text(encoding='utf-8')) if result_path else {}
mapdoc=json.loads((args.map_path or args.source/'data/maps/RKSI_map.json').read_text(encoding='utf-8'))
# Canonical Z-up scene, translated near the airport for float precision.
layout_points=[p for key in ['runwayPaths','taxiways'] for row in layout.get(key,[]) for p in (row.get('vertices') or row.get('CW_vertices',[]))]
layout_points.extend(p for row in layout.get('terminals',[]) for vertices in terminal_vertex_lists(row) for p in vertices)
if args.center:CX,CY=args.center
elif default_rksi:CX,CY=14500.0,15000.0
elif layout_points:CX,CY=[(min(float(p[k]) for p in layout_points)+max(float(p[k]) for p in layout_points))/2 for k in ['x','y']]
else:raise ValueError('The selected airport has no usable saved runway or building geometry.')
def xy(p):return (float(p['x'])-CX,CY-float(p['y']))
def polygon(vs):
    if len(vs)<3:return Polygon()
    return Polygon([xy(p) for p in vs]).buffer(0)

def terminal_polygon(row):
    # vertices is the primary piece; footprints retains other saved wings.
    return unary_union([polygon(vertices) for vertices in terminal_vertex_lists(row)])
imp=raw.get('_osmImport')
if not imp:
    # ARP-authored layouts (including REAL_MODEL_COPY) use the source viewer's
    # same east/north projection, with an explicit saved layout anchor.
    geo=raw.get('_liveGeoRef',{})
    if geo.get('mode')=='osm':
        imp={'lonLatOrigin':{'lon':geo['lon0'],'lat':geo['lat0']},'gridOriginShiftM':{'x':geo['xOff']-geo.get('offsetEastM',0),'y':geo['yOff']-geo.get('offsetNorthM',0)},'gridYSpanM':geo['ySpanM']}
    elif geo.get('mode'):
        imp={'lonLatOrigin':{'lon':geo['lon0'],'lat':geo['lat0']},'gridOriginShiftM':{'x':-geo['anchorX']-geo.get('offsetEastM',0),'y':geo['anchorY']-geo.get('offsetNorthM',0)},'gridYSpanM':0}
    else:raise ValueError('The selected layout has no saved map georeference.')
origin=imp['lonLatOrigin']; shift=imp['gridOriginShiftM']
def map_shape(f):
    s=_geom_to_xy_shape(f['geometry'],origin['lon'],origin['lat'],OSM_TO_LAYOUT_RULES['projection']['earth_radius_m'],shift['x'],shift['y'],imp['gridYSpanM'])
    return transform(lambda x,y,z=None:(np.asarray(x)-CX,CY-np.asarray(y)),s) if s is not None else None
core=mapdoc['geojson']['features']
ground_candidates=[map_shape(f) for f in core if f['properties'].get('tags',{}).get('aeroway')=='aerodrome']
ground=unary_union([p for p in ground_candidates if p is not None and p.geom_type in ['Polygon','MultiPolygon']]).buffer(0)
if ground.is_empty:ground=unary_union([Point(*xy(p)) for p in layout_points]).convex_hull.buffer(180)
site=ground.buffer(120,join_style=2).simplify(2,preserve_topology=True)
bounds=site.bounds
batches={}
ground_surfaces=[]
PAVING_MATERIALS={'apron','shoulder','taxiway','runway','road','parking'}
marking_surfaces=collections.defaultdict(list)
GROUND_MARKINGS={'road-marking','yellow-marking','white-marking'}
def bucket(name):return batches.setdefault(name,{'v':[],'f':[]})
def face(name,pts):
    b=bucket(name);i=len(b['v']);b['v'].extend([[round(float(c),4) for c in p] for p in pts]);b['f'].append(list(range(i,i+len(pts))))
def polys(s):
    if s.is_empty:return []
    if s.geom_type=='Polygon':return [s]
    return [p for p in getattr(s,'geoms',[]) if p.geom_type=='Polygon']
def surface(name,s,z,collect_ground=True):
    if name in PAVING_MATERIALS and collect_ground:
        if not s.is_empty:ground_surfaces.append((name,s,z))
        return
    for p in polys(s):
        for tri in constrained_delaunay_triangles(p).geoms:
            pts=list(tri.exterior.coords)[:3]
            if (pts[1][0]-pts[0][0])*(pts[2][1]-pts[0][1])-(pts[1][1]-pts[0][1])*(pts[2][0]-pts[0][0])<0:pts.reverse()
            face(name,[(x,y,z(x,y) if callable(z) else z) for x,y in pts])
def walls(name,s,lo,hi):
    for p in polys(s):
        p=orient(p,sign=1)
        for ring in [p.exterior,*p.interiors]:
            pts=list(ring.coords)
            for a,b in zip(pts,pts[1:]):face(name,[(a[0],a[1],lo),(b[0],b[1],lo),(b[0],b[1],hi),(a[0],a[1],hi)])
def extrude(name,s,lo,hi):surface(name,s,hi);walls(name,s,lo,hi)
def beam(name,a,b,width,height):
    a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float);d=b-a;length=np.linalg.norm(d)
    if length<.02:return
    u=d/length;n=np.cross(u,[0,0,1])
    if np.linalg.norm(n)<.01:n=np.array([1.,0,0])
    n=n/np.linalg.norm(n)*width/2;v=np.cross(u,n);v=v/np.linalg.norm(v)*height/2
    pts=[a-n-v,a+n-v,a+n+v,a-n+v,b-n-v,b+n-v,b+n+v,b-n+v]
    for q in [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]:face(name,[pts[i] for i in q])
def cylinder(name,x,y,r,lo,hi,n=12):extrude(name,Point(x,y).buffer(r,quad_segs=n//4),lo,hi)
def paint_line(name,points,width,z):
    if len(points)<2:return
    shape=LineString(points).buffer(width/2,cap_style=2,join_style=2)
    if name in GROUND_MARKINGS:marking_surfaces[name].append(shape)
    else:surface(name,shape,z)

walls('site-edge',site,-12,0)
# Genuine OSM apron polygons supplement the authored taxiway network.
apron_shapes=[map_shape(f).buffer(0) for f in core if f['properties'].get('tags',{}).get('aeroway')=='apron']
# Saved contact/remote stands extend beyond several OSM apron polygons. Fill
# their service envelope so the authored stand and access routes remain paved.
stand_index={s['id']:s for s in layout.get('pbbStands',[])+layout.get('remoteStands',[])}
stand_operating_cores=[]
for stand in stand_index.values():
    if 'apronSiteX' in stand:
        a=xy({'x':stand['x1'],'y':stand['y1']});b=xy({'x':stand['apronSiteX'],'y':stand['apronSiteY']})
        apron_shapes.append(LineString([a,b]).buffer(38,cap_style=2,join_style=2))
        stand_operating_cores.append(Point(*b).buffer(12))
    else:
        x,y=xy(stand);apron_shapes.append(box(x-40,y-40,x+40,y+40))
        stand_operating_cores.append(Point(x,y).buffer(12))
for link in layout.get('apronLinks',[]):
    stand=stand_index.get(link.get('pbbId') or link.get('standId') or link.get('remoteId'))
    if not stand:continue
    a=xy({'x':stand.get('apronSiteX',stand.get('x',0)),'y':stand.get('apronSiteY',stand.get('y',0))})
    pts=[a]+[xy(p) for p in link.get('midVertices',[])]
    if link.get('tx') is not None:pts.append(xy({'x':link['tx'],'y':link['ty']}))
    if len(pts)>1:
        apron_shapes.append(LineString(pts).buffer(21,quad_segs=3))
        stand_operating_cores.append(LineString(pts).buffer(1))
raw_aprons=unary_union(apron_shapes)
# Join adjacent stand envelopes into continuous ramp pavement. Remove small
# leftover turf pockets, while retaining the large landscaped/taxiway islands.
closed_aprons=raw_aprons.buffer(32,quad_segs=4).buffer(-32,quad_segs=4)
aprons=unary_union([Polygon(p.exterior,[ring for ring in p.interiors if Polygon(ring).area>=5000]) for p in polys(closed_aprons)]).simplify(.3,preserve_topology=True)
# Separate remote ramp strips inherit a sawtooth edge from individual stand
# envelopes. Bridge those short notches within each connected ramp only; keep
# terminal courtyards and every retained large turf island unchanged.
terminal_footprints=unary_union([terminal_polygon(row) for row in layout['terminals'] if row.get('buildingType')=='passenger_terminal'])
ramp_before=aprons;ramp_edges_smoothed=0;ramp_parts=[]
for part in polys(aprons):
    if part.area>10000 and part.distance(terminal_footprints)>80:
        candidate=part.union(concave_hull(part,ratio=.15,allow_holes=True))
        if part.interiors:candidate=candidate.difference(unary_union([Polygon(ring) for ring in part.interiors]))
        # Never let a contour refinement turn an L-shaped ramp into a filled
        # rectangle or join two physically separate ramp areas.
        if candidate.area<=part.area*1.16:
            part=candidate;ramp_edges_smoothed+=1
    ramp_parts.append(part)
aprons=unary_union(ramp_parts).intersection(site).simplify(.3,preserve_topology=True)
ramp_contour_added_area=aprons.difference(ramp_before).area
lines=[];runways=[]
for key in ['runwayPaths','runwayTaxiways','taxiways']:
    for row in layout.get(key,[]):
        vs=row.get('vertices') or row.get('CW_vertices',[])
        if len(vs)<2:continue
        pts=[xy(p) for p in vs];ln=LineString(pts);w=float(row.get('width',23) or 23)
        if key=='runwayPaths':runways.append((row,ln,w))
        else:lines.append((ln,w))
taxi=unary_union([ln.buffer(w/2,quad_segs=4) for ln,w in lines])
# Honour complete taxiway-defined islands before collecting apron and shoulder
# surfaces. The same mask supplies the grass boundary later, so the perimeter
# remains continuous on both sides of a long island without coplanar overlap.
occupied_ramp=unary_union(stand_operating_cores+[terminal_polygon(row).buffer(4) for row in layout['terminals']])
aprons,contact_island_report=restore_taxiway_islands(aprons,taxi,occupied_ramp)
surface('apron',aprons,.12)
surface('shoulder',taxi.buffer(4,quad_segs=3).difference(aprons),.08)
surface('taxiway',taxi,.19)
for ln,w in lines:paint_line('yellow-marking',list(ln.coords),.5,.245)
for row,ln,w in runways:
    surface('shoulder',ln.buffer(w/2+8,cap_style=2),.21)
    surface('runway',ln.buffer(w/2,cap_style=2),.25)
    a=np.array(ln.coords[0]);b=np.array(ln.coords[-1]);u=(b-a)/ln.length;n=np.array([-u[1],u[0]])
    for sign in [-1,1]:paint_line('white-marking',[a+n*(w/2-1.5)*sign,b+n*(w/2-1.5)*sign],.75,.3)
    for dist in np.arange(110,ln.length-110,60):
        p=a+u*dist;paint_line('white-marking',[p,p+u*30],.9,.31)
    for base,direction in [(a,u),(b,-u)]:
        for i in [-5,-4,-3,-2,-1,1,2,3,4,5]:
            p=base+direction*14+n*i*3.4;paint_line('white-marking',[p,p+direction*32],1.6,.31)
        for dist in [150,300,450]:
            for sign in [-1,1]:
                p=base+direction*dist+n*sign*15;paint_line('white-marking',[p,p+direction*35],5,.31)

context=mapdoc['context']['editableGeojson']['features']
road_exclusion=unary_union([aprons,taxi.buffer(4,quad_segs=3),*[ln.buffer(w/2+8,cap_style=2) for _,ln,w in runways],*[polygon(p.get('vertices',[])) for p in layout.get('landsideParkings',[])]])
road_shape,road_report=build_access_roads(context,map_shape,site,road_exclusion,_road_lane_counts,surface,walls)
road_count=road_report['segments']
(BUILD/'road-report.json').write_text(json.dumps(road_report,indent=2),encoding='utf-8')
for p in layout.get('landsideParkings',[]):
    s=polygon(p.get('vertices',[])).intersection(site)
    if s.is_empty:continue
    surface('parking',s,.1)
    if s.area<1000:continue
    minx,miny,maxx,maxy=s.bounds
    # Fine parking lines, clipped to each actual footprint.
    for y in np.arange(miny+6,maxy,17):
        ln=LineString([(minx,y),(maxx,y)]).intersection(s)
        for part in ([ln] if ln.geom_type=='LineString' else getattr(ln,'geoms',[])):
            if part.geom_type!='LineString':continue
            for d in np.arange(0,part.length-5,3):
                p0=part.interpolate(d);seg=LineString([(p0.x,p0.y),(p0.x,p0.y+5)]).intersection(s)
                if seg.geom_type=='LineString':paint_line('road-marking',list(seg.coords),.11,.15)

building_meta=[];building_footprints=[];building_source_keys=set();building_skipped=[]
building_map_features={str(f['properties'].get('type','way'))+'/'+str(f['properties'].get('id')):f for f in [*core,*context]}

def add_building(row,shape,kind,tags=None,source_key=None):
    # The airport boundary cuts through landside buildings, so retain nearby
    # airport support facilities instead of dropping them by centroid alone.
    if shape.is_empty or shape.area<8 or shape.distance(site)>500:return
    if source_key and source_key in building_source_keys:return
    # Context polygons can repeat a saved authored building under another id.
    if any(shape.intersection(existing).area/min(shape.area,existing.area)>.8 for existing in building_footprints):return
    height,height_source=building_height(row,tags or {},kind)
    details=build_general_volume(shape,height,kind,walls=walls,surface=surface,extrude=extrude,beam=beam,face=face)
    center=shape.centroid
    building_meta.append({'id':row.get('id',source_key),'kind':kind,'heightM':height,'heightSource':height_source,'savedHeightM':row.get('totalHeightM',row.get('heightM',row.get('floorHeight'))),'footprintSource':row.get('_presentationFootprintSource','saved layout polygon'),'presentationOverride':row.get('_presentationOverride'),'center':[round(center.x,2),round(center.y,2),height/2],'footprintM2':round(shape.area,2),'details':details})
    building_footprints.append(shape)
    if source_key:building_source_keys.add(source_key)

term_meta=[]
for row in layout['terminals']:
    shape=terminal_polygon(row);height=float(row.get('floorHeight') or 25)
    if shape.is_empty:continue
    center=shape.centroid;kind=row.get('buildingType')
    term_meta.append({'id':row['id'],'name':row.get('name'),'kind':kind,'center':[center.x,center.y,height/2],'bounds':list(shape.bounds),'footprintCount':len(terminal_vertex_lists(row)),'footprintM2':shape.area})
    if kind=='control_tower':
        height=float(row.get('totalHeightM') or height);radius=float(row.get('towerRadiusM') or 12)
        cylinder('tower',center.x,center.y,radius*.55,0,height-14,12)
        cylinder('roof',center.x,center.y,radius*1.25,height-16,height-14,12)
        cylinder('glass',center.x,center.y,radius*1.1,height-14,height-3,12)
        cylinder('roof',center.x,center.y,radius*1.3,height-3,height,12)
        cylinder('mullion',center.x,center.y,.7,height,height+12,8)
        for angle in np.arange(0,math.tau,math.tau/12):
            p=[center.x+radius*1.1*math.cos(angle),center.y+radius*1.1*math.sin(angle)]
            beam('mullion',[*p,height-14],[*p,height-3],.35,.35)
        continue
    if kind!='passenger_terminal':
        source_osm=row.get('sourceOsm',{})
        add_building(row,shape,kind,source_osm.get('tags',{}),source_osm.get('key'));continue
    extrude('plinth',shape.buffer(.7),.2,1.5)
    walls('glass',shape,1.5,height-1)
    roof_shape=shape.buffer(1.4,join_style=2)
    walls('roof',roof_shape,height-1,height+.2)
    # A shallow standing-seam roof keeps the saved footprint while giving the
    # presentation model a softly crowned section. No simulation data changes.
    edge=roof_shape.boundary
    def roof_z(x,y):return height+.2+4.5*math.sin(min(1,Point(x,y).distance(edge)/42)*math.pi/2)
    rx0,ry0,rx1,ry1=roof_shape.bounds
    for rx in np.arange(rx0,rx1,24):
        for ry in np.arange(ry0,ry1,24):surface('roof',roof_shape.intersection(box(rx,ry,rx+24,ry+24)),roof_z)
    # Mullions and horizontal transoms follow the actual perimeter, not a box proxy.
    for poly in polys(shape):
        vs=list(poly.exterior.coords)
        for a,b in zip(vs,vs[1:]):
            a=np.array(a);b=np.array(b);length=np.linalg.norm(b-a)
            if length<.1:continue
            for s in np.arange(0,length,5):
                p=a+(b-a)*s/length;beam('mullion',[*p,1.5],[*p,height-.8],.24,.24)
            for z in [6,12,18,height-1]:beam('mullion',[*a,z],[*b,z],.23,.3)
    # Roof seams and skylight strips use the saved terminal footprint as a mask.
    x0,y0,x1,y1=shape.bounds;inset=shape.buffer(-5)
    for x in np.arange(x0,x1,8):
        line=LineString([(x,y0-3),(x,y1+3)]).intersection(inset)
        for part in ([line] if line.geom_type=='LineString' else getattr(line,'geoms',[])):
            if part.geom_type=='LineString' and part.length>3:
                pts=[part.interpolate(d).coords[0] for d in np.arange(0,part.length,12)]+[part.coords[-1]]
                for a,b in zip(pts,pts[1:]):paint_line('roof-seam',[a,b],.18,lambda x,y:roof_z(x,y)+.11)
    for x in np.arange(x0+20,x1,60):
        strip=box(x,y0-1,x+4,y1+1).intersection(shape.buffer(-14))
        # Short panes follow the roof profile without cutting across its crown.
        for sy in np.arange(y0,y1,16):surface('skylight',strip.intersection(box(x,sy,x+4,sy+16)),lambda x,y:roof_z(x,y)+.18)

for row in layout.get('landsideTrafficCenters',[])+layout.get('utilityFacilities',[])+layout.get('arffStations',[]):
    shape=polygon(row.get('vertices',[]))
    if shape.is_empty:continue
    source_osm=row.get('sourceOsm',{});tags=source_osm.get('tags',{})
    if source_osm and row.get('facilityType') and not tags.get('building'):
        # Power-plant land parcels, solar fields and weather observation plots
        # are not building footprints and must not become giant solid blocks.
        building_skipped.append({'id':row['id'],'reason':'non-building facility area'});continue
    # ARFF import creates a standard 18 x 22 m response footprint even when
    # the source way has a genuine building polygon. Use that retained polygon
    # in the presentation rather than hiding it behind the small proxy.
    feature=building_map_features.get(source_osm.get('key'))
    if row.get('buildingType')=='arff' and feature and tags.get('building') not in [None,'no']:
        source_shape=map_shape(feature)
        if source_shape is not None and polys(source_shape):
            shape=source_shape.buffer(0);row={**row,'_presentationFootprintSource':'saved OSM building polygon'}
    kind=building_kind(row,tags,row.get('facilityType') or 'building')
    add_building(row,shape,kind,tags,source_osm.get('key'))

for row in layout.get('landsideParkings',[]):
    tags=row.get('sourceOsm',{}).get('tags',{})
    selected_height=T2_COURTYARD_BUILDINGS.get(row.get('id'))
    if selected_height:
        row={**row,'_presentationHeightM':selected_height,'_presentationOverride':{'basis':'user identified these four T2 courtyard polygons as buildings on 2026-09-08','savedClassification':row.get('parkingStructureType'),'savedOsmTags':tags,'heightIsEstimated':True}}
        add_building(row,polygon(row.get('vertices',[])),'office',tags,row.get('sourceOsm',{}).get('key'))
        continue
    if row.get('parkingStructureType')!='multi-storey' and tags.get('parking')!='multi-storey':continue
    add_building(row,polygon(row.get('vertices',[])),'parking',tags,row.get('sourceOsm',{}).get('key'))

# Scan both retained map layers for genuine building polygons without a planning
# object. Point-only records and industrial/solar land parcels stay unextruded.
authored_terminal_mask=unary_union([terminal_polygon(row) for row in layout['terminals']])
for feature in [*core,*context]:
    props=feature['properties'];tags=props.get('tags',{})
    if (not tags.get('building') and tags.get('aeroway')!='hangar') or tags.get('building')=='no' or tags.get('aeroway')=='terminal':continue
    shape=map_shape(feature)
    if shape is None or not polys(shape):continue
    shape=shape.buffer(0)
    if shape.intersection(authored_terminal_mask).area>shape.area*.5:continue
    key=str(props.get('type','way'))+'/'+str(props.get('id'))
    kind=building_kind({},tags)
    add_building({'id':'context-'+key,'_presentationFootprintSource':'saved OSM building polygon'},shape,kind,tags,key)

(BUILD/'buildings-report.json').write_text(json.dumps({'buildings':building_meta,'skipped':building_skipped,'heightPolicy':'nondefault saved height, OSM height/levels, nondefault saved floors, then explicit presentation estimate; the generic 1 x 4 m schema profile is not measured height. Defaults: cargo 16 m, industrial 12 m, ARFF 8 m, multistorey parking 12.8 m, ordinary tower 18 m, other buildings 10.5 m. Source layout stays unchanged.','footprintPolicy':'saved layout polygons; original OSM building polygon replaces an ARFF import box when available. Core and context building polygons are both scanned. No new point-only footprint proxies or extruded outdoor/solar parcels.','materialGroups':['building','building-roof','glass']},indent=2),encoding='utf-8')

stands={s['id']:s for s in layout.get('pbbStands',[])+layout.get('remoteStands',[])}
for row in layout.get('apronLinks',[]):
    stand=stands.get(row.get('pbbId') or row.get('standId') or row.get('remoteId'))
    pts=[]
    if stand:
        sx=stand.get('apronSiteX',stand.get('x',stand.get('x2')));sy=stand.get('apronSiteY',stand.get('y',stand.get('y2')))
        if sx is not None and sy is not None:pts.append((sx-CX,CY-sy))
    pts.extend(xy(p) for p in row.get('midVertices',[]))
    if row.get('tx') is not None:pts.append((row['tx']-CX,CY-row['ty']))
    paint_line('yellow-marking',pts,.25,.26)
for stand in layout.get('pbbStands',[]):
    for bridge in stand.get('pbbBridges',[]):
        pts=[xy(p) for p in bridge.get('points',[])]
        for a,b in zip(pts,pts[1:]):
            beam('bridge',[*a,4.9],[*b,4.9],3,2.6)
            beam('bridge-glass',[*a,5.1],[*b,5.1],3.06,1.4)
            beam('roof',[*a,6.3],[*b,6.3],3.2,.2)
        if pts:
            x,y=pts[-1];cylinder('mullion',x,y,.35,.3,4.3,8)
    # Apron edge line to visually anchor each saved contact stand.
    if all(k in stand for k in ['x1','y1','apronSiteX','apronSiteY']):
        a=xy({'x':stand['x1'],'y':stand['y1']});b=xy({'x':stand['apronSiteX'],'y':stand['apronSiteY']})
        paint_line('yellow-marking',[a,b],.35,.29)

# A small number of physically scaled apron lamps, placed from saved lighting fixtures.
for fixture in raw.get('lightingSettings',{}).get('fixtures',[]):
    x=fixture.get('x');y=fixture.get('y')
    if x is None or y is None:continue
    x-=CX;y=CY-y;h=float(fixture.get('heightM',25) or 25)
    cylinder('mullion',x,y,.3,0,h,8)
    beam('roof',[x-3,y,h],[x+3,y,h],1.8,.7)

# Give every ground area a single owner; remove buried pavement as well as
# buried grass. Then clip/deduplicate paint to its actual receiving surface.
ground_groups=collections.defaultdict(list)
for name,shape,z in ground_surfaces:ground_groups[(name,z)].append(shape)
paving_mask=Polygon();resolved_ground=[];pavement_overlap=0.
for (name,z),shapes in sorted(ground_groups.items(),key=lambda item:item[0][1],reverse=True):
    shape=unary_union(shapes).difference(paving_mask).buffer(0)
    pavement_overlap+=shape.intersection(paving_mask).area
    surface(name,shape,z,collect_ground=False)
    resolved_ground.append((name,shape,z));paving_mask=paving_mask.union(shape)
marking_report={}
for marking,shapes in marking_surfaces.items():
    paint=unary_union(shapes)
    allowed={'road','parking'} if marking=='road-marking' else {'runway'} if marking=='white-marking' else {'apron','taxiway','runway'}
    painted_area=0.;min_clearance=.04
    for material,footprint,z in resolved_ground:
        if material not in allowed:continue
        clipped=paint.intersection(footprint)
        surface(marking,clipped,z+min_clearance);painted_area+=clipped.area
    marking_report[marking]={'inputAreaM2':paint.area,'paintedAreaM2':painted_area,'surfaceClearanceM':min_clearance}
grass_mask=site.difference(paving_mask)
assert grass_mask.is_valid, 'Invalid turf boundary after pavement subtraction'
grass_overlap=grass_mask.intersection(paving_mask).area
assert grass_overlap<.001, f'Turf overlaps pavement by {grass_overlap} square metres'
surface('grass',grass_mask,0)
(BUILD/'ground-separation.json').write_text(json.dumps({
    'method':'site minus union of apron, shoulder, taxiway, runway, road and parking footprints',
    'siteAreaM2':site.area,'pavedWithinSiteAreaM2':site.intersection(paving_mask).area,
    'grassAreaM2':grass_mask.area,'grassPavementOverlapM2':grass_overlap,
    'grassPolygons':len(polys(grass_mask)),'pavementOverlapM2':pavement_overlap,
    'rampGapClosingRadiusM':32,'rampSmallHoleLimitM2':5000,
    'remoteRampContoursSmoothed':ramp_edges_smoothed,'remoteRampAddedAreaM2':ramp_contour_added_area,
    'remoteRampMaxAreaIncreaseRatio':.16,'remoteRampConcaveHullRatio':.15,
    'contactApronIslands':contact_island_report,
    'markings':marking_report,
},indent=2),encoding='utf-8')
replay=export_replay(args.source,ASSETS,OUT,layout,result,(CX,CY),default_rksi)
metadata={'scenario':layout_path.stem,'airport':args.airport,'icao':args.icao,'city':args.city,'baseDate':result.get('baseDate'),'speed':30,'stride':5,**replay,'center':[CX,CY],'siteBounds':list(bounds),'terminals':term_meta,'sourceRunTerminatedEarly':bool(result.get('simulation_truncated_deadlock')),'attribution':'Airport map data © OpenStreetMap contributors · ODbL 1.0','counts':{'flights':len(replay['tracks']),'terminals':len(term_meta),'runways':len(runways),'roads':road_count,'drawBatches':len(batches)}}
metadata['lighting']=build_lights(layout,raw)
metadata['taxiwayCenterlines']=build_taxiway_centerlines(lines,resolved_ground,collect_lead_in_lines(layout,xy))
if not default_rksi:
    metadata['camera']=camera_metadata(bounds,term_meta)
    for values in metadata['lighting'].values():
        for i in range(0,len(values),3):values[i]+=14500-CX;values[i+1]+=CY-15000
metadata['counts']['generalBuildings']=len(building_meta)
(OUT/'scene.json').write_text(json.dumps(metadata,separators=(',',':')),encoding='utf-8')
(BUILD/'geometry.json').write_text(json.dumps(batches,separators=(',',':')),encoding='utf-8')
transform_note={'source':'layout metres, +X east, +Y south; scene +Z up','sceneMapping':[f'X=layoutX-{CX}',f'Y={CY}-layoutY','Z=elevation'],'aircraft':'P2 pivot, +X nose, +Y left; heading=-layout headingRad; binary tracks retain all moving samples','samples':[[p,[p[0]-CX,CY-p[1],0]] for p in [[CX,CY],[CX+100,CY],[CX,CY+100]]],'sourceHashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [layout_path,result_path] if p},'sceneCounts':metadata['counts'],'vertices':sum(len(v['v']) for v in batches.values()),'polygons':sum(len(v['f']) for v in batches.values()),'replayBytes':(OUT/'replay.bin').stat().st_size}
(BUILD/'export-report.json').write_text(json.dumps(transform_note,indent=2),encoding='utf-8')
print(json.dumps(transform_note,indent=2))

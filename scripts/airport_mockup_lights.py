"""Small night-light placement adapter; source airport geometry stays read-only."""
import json, math, sys
from pathlib import Path
from shapely.geometry import LineString
from shapely.ops import unary_union

def build_lights(layout,raw):
    def xy(p):return (p['x']-14500,15000-p['y'])
    paths=[];runways=[]
    for key in ['taxiways','runwayTaxiways','runwayPaths']:
        for row in layout.get(key,[]):
            pts=[xy(p) for p in row.get('vertices',row.get('CW_vertices',[]))]
            if len(pts)<2:continue
            entry=(LineString(pts),float(row.get('width') or 23))
            (runways if key=='runwayPaths' else paths).append(entry)
    groups={name:[] for name in ['blue','green','white','red','warm','pools','pbb','pbbPools']}
    seen={name:set() for name in groups}
    def add(name,x,y,z=.5,grid=8):
        key=(round(x/grid),round(y/grid))
        if key in seen[name]:return
        seen[name].add(key);groups[name].extend([round(x,1),round(y,1),z])
    pavement=unary_union([line.buffer(w/2,quad_segs=3) for line,w in paths])
    boundary=pavement.buffer(.8,quad_segs=2).boundary
    for ring in getattr(boundary,'geoms',[boundary]):
        for n in range(math.ceil(ring.length/45)):
            p=ring.interpolate(n*45);add('blue',p.x,p.y)
    for line,w in paths:
        for n in range(math.ceil(line.length/60)):
            p=line.interpolate(n*60);add('green',p.x,p.y,.36,12)
    for line,w in runways:
        a,b=line.coords[0],line.coords[-1];dx=(b[0]-a[0])/line.length;dy=(b[1]-a[1])/line.length
        for n in range(math.ceil(line.length/45)):
            p=line.interpolate(n*45)
            for side in [-1,1]:add('white',p.x-dy*(w/2+1)*side,p.y+dx*(w/2+1)*side)
        for end,sign in [(a,1),(b,-1)]:
            for k in range(-5,6):add('green',end[0]-dy*k*w/12,end[1]+dx*k*w/12,.5,2)
    stands=[]
    for stand in layout.get('pbbStands',[])+layout.get('remoteStands',[]):
        sx=stand.get('apronSiteX',stand.get('x',stand.get('x2')))
        sy=stand.get('apronSiteY',stand.get('y',stand.get('y2')))
        if sx is not None and sy is not None:stands.append((sx-14500,15000-sy))
    for stand in layout.get('pbbStands',[]):
        for bridge in stand.get('pbbBridges',[]):
            points=bridge.get('points',[])
            if len(points)<2:continue
            a,b=xy(points[-2]),xy(points[-1])
            dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy)
            if length<.1:continue
            # A warm canopy lamp at the saved bridge head and a compact pool
            # beyond it illuminate the aircraft docking area, not the turf.
            add('pbb',b[0],b[1],5.9,3)
            add('pbbPools',b[0]+dx/length*6,b[1]+dy/length*6,.33,6)
    for fixture in raw.get('lightingSettings',{}).get('fixtures',[]):
        if fixture.get('x') is None or fixture.get('y') is None:continue
        if fixture.get('type')!='areaLamp':continue
        x,y=fixture['x']-14500,15000-fixture['y']
        add('warm',x,y,float(fixture.get('heightM') or 25),30)
        # Aim the presentation glow from each source mast toward its closest stand.
        # The real mast stays on its recorded island; the apron receives the light.
        target=min(stands,key=lambda p:math.hypot(p[0]-x,p[1]-y)) if stands else (x,y)
        distance=math.hypot(target[0]-x,target[1]-y)
        if 0<distance<500:
            scale=min(.72,90/distance)
            add('pools',x+(target[0]-x)*scale,y+(target[1]-y)*scale,.33,30)
    if not groups['warm']:
        for stand in layout.get('pbbStands',[])[::4]:
            if 'apronSiteX' in stand:add('warm',stand['apronSiteX']-14500,15000-stand['apronSiteY'],22,65)
    return groups

if __name__=='__main__':
    source=Path(sys.argv[1]);sys.path.insert(0,str(source))
    from blueprint.layout.schema import flatten_grouped_layout_schema
    raw=json.loads((source/'data/layouts/RKSI_INITIAL_R1_NORMAL.json').read_text(encoding='utf-8'))
    target=Path(__file__).resolve().parents[1]/'web/airport-mockup/scene.json'
    meta=json.loads(target.read_text(encoding='utf-8'));meta['lighting']=build_lights(flatten_grouped_layout_schema(raw),raw)
    target.write_text(json.dumps(meta,separators=(',',':')),encoding='utf-8')
    print({k:len(v)//3 for k,v in meta['lighting'].items()})

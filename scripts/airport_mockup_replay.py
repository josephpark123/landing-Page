"""Saved replay and framing adapter shared by on-demand airport exports."""
import hashlib
import math
import shutil
import numpy as np

VARIANTS = {
    'A320':'airbus-a320-200','B738':'boeing-737-800-winglet',
    'DHC6':'de-havilland-dhc-6-400','E145':'embraer-erj-145',
    'A20N':'airbus-a320neo-baseline','A21N':'airbus-a321neo-baseline',
    'A321':'airbus-a321-200','A332':'airbus-a330-200','A333':'airbus-a330-300',
    'A339':'airbus-a330-900','A359':'airbus-a350-900','AT76':'atr-72-600',
    'B38M':'boeing-737-max-8','B734':'boeing-737-400','B744':'boeing-747-400',
    'B752':'boeing-757-200','B772':'boeing-777-200','B773':'boeing-777-300',
    'B77W':'boeing-777-300er','B788':'boeing-787-8','B789':'boeing-787-9',
    'B78X':'boeing-787-10',
}


def export_replay(source, assets, out, layout, result, center, default_rksi=False):
    flights={str(f['id']):f for f in layout.get('flights',[])}
    positions={str(k):v for k,v in result.get('positions',{}).items()
               if isinstance(v,dict) and v.get('t') and str(k) in flights}
    types=sorted({str(flights[fid].get('aircraftType','A320')).upper() for fid in positions})
    if default_rksi:types=['A320','B738','DHC6','E145']
    models={};missing=[]
    for typ in types:
        variant=VARIANTS.get(typ,'catalog-'+typ.lower())
        candidates=sorted((source/'data/aircraft_geometry'/variant).glob('**/runtime.glb'))
        if not candidates:
            missing.append(typ);continue
        path=candidates[-1];dest=assets/(typ+'.glb');shutil.copy2(path,dest)
        models[typ]={'template':'AircraftTemplate_'+typ,'source':str(path.relative_to(source)),
                     'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
    tracks=[];chunks=[];offset=0;cx,cy=center
    start=min((float(tr['t'][0]) for tr in positions.values()),default=0.)
    latest=max((float(tr['t'][-1]) for tr in positions.values()),default=1.)
    end=max(start+1,float(result.get('simulation_playback_end_abs_sec') or latest))
    for fid,tr in positions.items():
        typ=str(flights[fid].get('aircraftType','A320')).upper()
        if typ not in models:continue
        t=np.asarray(tr['t'],dtype=float);x=np.asarray(tr['x'],dtype=float);y=np.asarray(tr['y'],dtype=float)
        valid=np.asarray(tr.get('groundPoseValid',np.zeros(len(t))),dtype=bool)
        px=np.asarray(tr.get('p2X',x),dtype=float);py=np.asarray(tr.get('p2Y',y),dtype=float)
        raw_heading=tr.get('headingRad')
        if raw_heading is None:raw_heading=np.arctan2(np.gradient(y),np.gradient(x)) if len(t)>1 else np.zeros(len(t))
        heading=np.unwrap(-np.asarray(raw_heading,dtype=float))
        x=np.where(valid,px,x);y=np.where(valid,py,y);z=np.zeros(len(t));indices=np.flatnonzero(valid)
        if len(indices):
            first,last=indices[0],indices[-1]
            z[:first]=np.hypot(x[:first]-x[first],y[:first]-y[first])*math.tan(math.radians(3))
            z[last+1:]=np.hypot(x[last+1:]-x[last],y[last+1:]-y[last])*math.tan(math.radians(3))
        rows=np.column_stack([t-start,x-cx,cy-y,z,heading])
        keep=np.ones(len(rows),dtype=bool)
        # Keep every moving sample while collapsing only interior dwell points.
        if len(rows)>2:
            same=np.max(np.abs(np.diff(rows[:,1:],axis=0)),axis=1)<.0001
            keep[1:-1]=~(same[:-1]&same[1:])
        rows=rows[keep].astype('<f4');chunks.append(rows)
        tracks.append({'id':fid,'type':typ,'offset':offset,'count':len(rows),
                       'start':float(rows[0,0]),'end':float(rows[-1,0])})
        offset+=rows.size
    (out/'replay.bin').write_bytes(b''.join(rows.tobytes() for rows in chunks))
    if default_rksi:initial=max(0,min(end-start,43260-start))
    elif tracks:
        # Open at a busy moment from the saved run, not at an empty first frame.
        samples=np.linspace(0,end-start,80)
        active=[sum(tr['start']<=t<=tr['end'] for tr in tracks) for t in samples]
        initial=float(samples[int(np.argmax(active))])
    else:initial=0.
    return {'models':models,'tracks':tracks,'start':start,'end':end,'duration':end-start,
            'initialTime':initial,'hasReplay':bool(tracks),'missingAircraftModels':missing}


def camera_metadata(bounds,terminals):
    x0,y0,x1,y1=bounds;span=max(x1-x0,y1-y0,800);cx=(x0+x1)/2;cy=(y0+y1)/2
    choices=[t for t in terminals if t.get('kind')=='passenger_terminal'] or terminals
    main=max(choices,key=lambda t:(t['bounds'][2]-t['bounds'][0])*(t['bounds'][3]-t['bounds'][1])) if choices else None
    tx,ty=(main['center'][:2] if main else [cx,cy])
    terminal_size=max(main['bounds'][2]-main['bounds'][0],main['bounds'][3]-main['bounds'][1],180) if main else 450
    distance=min(span*.4,max(terminal_size*1.3,450));height=max(180,distance*.48)
    target=[tx,ty,8]
    return {'poses':{
        'overview':{'position':[cx-span*.65,cy-span*.75,span*.8],'target':[cx,cy,0]},
        'terminal':{'position':[tx+distance*.5,ty-distance,height],'target':target},
        'airside':{'position':[tx-distance*.6,ty-distance*.72,max(55,distance*.12)],'target':target}},
        'tourTarget':target,'tourPositions':[[tx-distance,ty-distance*1.25,height*2],
            [tx+distance*.5,ty-distance,height],[tx+distance,ty+distance*.6,height*.9],
            [tx-distance,ty+distance*.5,height*1.2],[tx-distance,ty-distance*1.25,height*2]]}

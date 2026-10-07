"""Preserve the source Grid3D terminalFootprintVertexLists3d contract."""
import math


def terminal_vertex_lists(terminal):
    def vertices(raw):
        result=[]
        for point in raw or []:
            if isinstance(point,dict):x,y=point.get('x'),point.get('y')
            elif isinstance(point,(list,tuple)) and len(point)>=2:x,y=point[:2]
            else:continue
            try:x,y=float(x),float(y)
            except (TypeError,ValueError):continue
            if math.isfinite(x) and math.isfinite(y):result.append({'x':x,'y':y})
        return result
    primary=vertices(terminal.get('vertices'))
    polygons=[]
    for footprint in terminal.get('footprints') or []:
        points=vertices(footprint if isinstance(footprint,list) else footprint.get('vertices') if isinstance(footprint,dict) else [])
        if len(points)>=3:polygons.append(points)
    if len(primary)<3:return polygons
    if not polygons:return [primary]
    first=polygons[0]
    same=len(first)==len(primary) and all(abs(a['x']-b['x'])<1e-6 and abs(a['y']-b['y'])<1e-6 for a,b in zip(first,primary))
    return [primary]+(polygons[1:] if same else polygons)

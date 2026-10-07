"""Batched source-width access roads, lane paint and low continuous kerbs."""
import math
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union, substring


def lines(shape):
    if shape.is_empty:
        return []
    if shape.geom_type == 'LineString':
        return [shape]
    return [line for part in getattr(shape, 'geoms', []) for line in lines(part)]


def build_access_roads(features, map_shape, site, exclusion, lane_counts, surface, walls):
    records = []
    footprints = []
    classes = {'motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link',
               'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'service',
               'residential', 'unclassified', 'living_street', 'road'}
    for feature in features:
        tags = feature['properties'].get('tags', {})
        if tags.get('highway') not in classes or str(tags.get('tunnel', '')).lower() in {'yes', 'true', '1'}:
            continue
        shape = map_shape(feature)
        if shape is None or not shape.intersects(site):
            continue
        for line in lines(shape):
            up, down, line = lane_counts(tags, line)
            up, down = min(12, up), min(12, down)
            count = max(1, up + down)
            # Same 3.5 m lane width and OSM directional counts as 260903.
            width = count * 3.5
            footprint = line.buffer(width / 2, quad_segs=3, join_style=2).intersection(site).difference(exclusion)
            if footprint.is_empty:
                continue
            footprints.append(footprint)
            records.append((line, up, down, width, footprint))
    road = unary_union(footprints).buffer(0)
    surface('road', road, .06)
    white, yellow = [], []
    for line, up, down, width, footprint in records:
        for offset in [-width / 2 + .3, width / 2 - .3]:
            for edge in lines(line.offset_curve(offset, quad_segs=3, join_style=2)):
                white.append(edge.buffer(.06, cap_style=2).intersection(footprint))
        for lane in range(1, up + down):
            offset = -width / 2 + lane * 3.5
            if down and lane == up:
                for delta in [-.11, .11]:
                    for divider in lines(line.offset_curve(offset + delta, quad_segs=3, join_style=2)):
                        yellow.append(divider.buffer(.05, cap_style=2).intersection(footprint))
            else:
                for divider in lines(line.offset_curve(offset, quad_segs=3, join_style=2)):
                    for i in range(math.ceil(divider.length / 6)):
                        dash = substring(divider, i * 6, min(divider.length, i * 6 + 3))
                        if dash.geom_type == 'LineString':
                            white.append(dash.buffer(.055, cap_style=2).intersection(footprint))
    # Paint sits 4 cm above its own road slab. One union per material prevents
    # duplicate line surfaces at source OSM segment joins.
    yellow_mask = unary_union(yellow).intersection(road)
    white_mask = unary_union(white).intersection(road).difference(yellow_mask)
    surface('road-marking', white_mask, .10)
    surface('yellow-marking', yellow_mask, .10)
    # Form a continuous outer edge after merging junctions; no curbs cross lanes.
    curb = road.buffer(.23, quad_segs=2, join_style=2).difference(road).difference(exclusion).intersection(site)
    surface('road-curb', curb, .22)
    walls('road-curb', curb, .015, .22)
    return road, {
        'segments': len(records), 'laneWidthM': 3.5, 'roadAreaM2': round(road.area, 2),
        'oneWaySegments': sum(down == 0 for _, up, down, _, _ in records),
        'widthsM': sorted(set(width for _, _, _, width, _ in records)),
        'paintClearanceM': .04, 'curbHeightM': .22,
        'roadAirsideOverlapM2': round(road.intersection(exclusion).area, 6),
        'whiteYellowPaintOverlapM2': round(white_mask.intersection(yellow_mask).area, 6),
        'heightBasis': 'Ground-level presentation; tunnels omitted; no inferred bridge elevations',
    }

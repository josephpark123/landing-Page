"""Compact canonical taxiway segments for one screen-width-preserving batch."""
from shapely.geometry import LineString
from shapely.ops import unary_union


def _line_parts(shape):
    if shape.is_empty:
        return
    if shape.geom_type == 'LineString':
        yield shape
    else:
        for part in getattr(shape, 'geoms', []):
            yield from _line_parts(part)


def collect_lead_in_lines(layout, xy):
    """Match the exporter's existing yellow apron-link and contact-stand paint."""
    stands = {s['id']: s for s in layout.get('pbbStands', []) + layout.get('remoteStands', [])}
    lines = []
    for row in layout.get('apronLinks', []):
        stand = stands.get(row.get('pbbId') or row.get('standId') or row.get('remoteId'))
        points = []
        if stand:
            sx = stand.get('apronSiteX', stand.get('x', stand.get('x2')))
            sy = stand.get('apronSiteY', stand.get('y', stand.get('y2')))
            if sx is not None and sy is not None:
                points.append(xy({'x': sx, 'y': sy}))
        points.extend(xy(point) for point in row.get('midVertices', []))
        if row.get('tx') is not None:
            points.append(xy({'x': row['tx'], 'y': row['ty']}))
        if len(points) > 1:
            lines.append((LineString(points), .25))
    for stand in layout.get('pbbStands', []):
        if all(key in stand for key in ['x1', 'y1', 'apronSiteX', 'apronSiteY']):
            a = xy({'x': stand['x1'], 'y': stand['y1']})
            b = xy({'x': stand['apronSiteX'], 'y': stand['apronSiteY']})
            lines.append((LineString([a, b]), .35))
    return lines


def _pack_segments(network, resolved_ground, seen):
    segments = []
    for material, footprint, elevation in resolved_ground:
        if material not in {'apron', 'taxiway', 'runway'}:
            continue
        for line in _line_parts(network.intersection(footprint)):
            for a, b in zip(line.coords, list(line.coords)[1:]):
                if (a[0]-b[0])**2+(a[1]-b[1])**2 < .0025:
                    continue
                start = (round(a[0], 3), round(a[1], 3), round(elevation+.06, 3))
                end = (round(b[0], 3), round(b[1], 3), round(elevation+.06, 3))
                key = tuple(sorted((start, end)))
                if key in seen:
                    continue
                seen.add(key); segments.extend((*start, *end))
    return segments


def build_taxiway_centerlines(taxi_lines, resolved_ground, lead_in_lines=None):
    # Union removes repeated source edges. Resolve the final receiving surface
    # before splitting, so runway crossings receive runway elevation as well.
    network = unary_union([line for line, _ in taxi_lines])
    seen = set(); segments = _pack_segments(network, resolved_ground, seen)
    lead_segments = []; lead_widths = []; covered = network
    # Preserve the two existing paint widths. Shared portions belong to the
    # taxiway, then to the wider stand line, so the GPU never double draws them.
    for width in sorted({width for _, width in lead_in_lines or []}, reverse=True):
        source = unary_union([line for line, value in lead_in_lines if value == width])
        unique = source.difference(covered)
        packed = _pack_segments(unique, resolved_ground, seen)
        lead_segments.extend(packed); lead_widths.extend([width] * (len(packed)//6))
        covered = unary_union([covered, source])
    return {
        'widthM': .5, 'minimumCssPixels': 1.1, 'surfaceClearanceM': .06,
        'segmentCount': len(segments)//6, 'segments': segments,
        'leadInSegmentCount': len(lead_segments)//6, 'leadInSegments': lead_segments,
        'leadInWidthsM': lead_widths, 'leadInMinimumScale': .8,
        'source': 'saved taxiway centerlines and existing apron-link/contact-stand paint, clipped to final receiving pavement; scene metres, Z up',
    }

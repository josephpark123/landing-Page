"""Small, batched presentation buildings on retained airport footprints.

Heights without source evidence are visual estimates, never measured airport
data. All geometry is already in the exporter's metre-based, Z-up scene frame.
"""
import math
import re

import numpy as np
from shapely.geometry import LineString, Point, Polygon
from shapely.geometry.polygon import orient


# These exact four RKSI T2 courtyard polygons were identified as buildings by
# the user in the 2026-09-08 screenshot. Their saved OSM parking tags remain
# untouched. This narrow presentation override does not promote other lots.
T2_COURTYARD_BUILDINGS = {
    'osm-parking-way-1211657657': 14,
    'osm-parking-way-841554294': 12,
    'osm-parking-way-841554295': 12,
    'osm-parking-way-1168329107': 14,
}


def positive_number(value):
    match = re.match(r'^\s*(\d+(?:\.\d+)?)', str(value))
    if not match:
        return None
    number = float(match.group(1))
    if 'ft' in str(value).lower() or "'" in str(value):
        number *= .3048
    return number if number > 0 and math.isfinite(number) else None


def building_kind(row, tags, fallback='building'):
    if tags.get('parking') == 'multi-storey' or row.get('parkingStructureType') == 'multi-storey':
        return 'parking'
    if tags.get('amenity') == 'fire_station':
        return 'arff'
    if tags.get('aeroway') == 'hangar':
        return 'hangar'
    if tags.get('man_made') == 'tower':
        return 'tower'
    if tags.get('power') == 'substation':
        return 'industrial'
    return row.get('buildingType') or tags.get('building') or row.get('trafficCenterType') or fallback


def building_height(row, tags, kind):
    """Separate the importer/schema's generic four-metre profile from evidence.

    context_convert.py defaults utility heightM to 4 and ARFF to one 4 m
    floor; parking imports default to one floor. The layout schema also uses
    4 m floor-to-floor for newly authored support buildings. Keep nondefault
    layout heights and explicit OSM heights/levels; only replace those generic
    profiles for this presentation export.
    """
    selected_height = positive_number(row.get('_presentationHeightM'))
    if selected_height:
        return selected_height, 'presentation estimate (user-selected T2 courtyard building)'
    total = positive_number(row.get('totalHeightM'))
    if total:
        return min(total, 160), 'layout.totalHeightM'
    for key in ['heightM', 'floorHeight']:
        height = positive_number(row.get(key))
        # An actual four-metre OSM height is retained below. Four metres in an
        # imported/default building profile alone is not source height evidence.
        if height and abs(height - 4) > .001:
            return min(height, 160), 'layout.' + key
    height = positive_number(tags.get('height'))
    if height:
        return min(height, 160), 'osm.height'
    levels = positive_number(tags.get('building:levels'))
    if levels:
        return min(levels * (3.2 if kind == 'parking' else 4), 160), 'osm.building:levels'
    floors = positive_number(row.get('floors'))
    floor_height = positive_number(row.get('floorToFloor'))
    if floors and floor_height and not (floors == 1 and floor_height == 4):
        return min(floors * floor_height, 160), 'layout.floors*floorToFloor'
    default = {
        'parking': 12.8, 'industrial': 12, 'train_station': 12, 'rail_station': 12,
        'arff': 8, 'cargo_terminal': 16, 'hangar': 20, 'warehouse': 14,
        'tower': 18,
    }.get(kind, 10.5)
    generic_profile = any(positive_number(row.get(key)) == 4 for key in ['heightM', 'floorHeight']) or (floors == 1 and floor_height == 4)
    return default, 'presentation estimate (generic 4 m profile)' if generic_profile else 'presentation estimate (height unavailable)'


def build_general_volume(shape, height, kind, *, walls, surface, extrude, beam, face):
    """Gray wall/roof shells, sparse glazing, parapets and a few roof units.

    Existing material batches are reused. Static detail has no runtime objects,
    no per-building lights, and no new materials or texture downloads.
    """
    walls('building', shape, .2, height)
    surface('building-roof', shape, height)
    parts = [shape] if shape.geom_type == 'Polygon' else [p for p in getattr(shape, 'geoms', []) if p.geom_type == 'Polygon']
    panel_count = roof_unit_count = 0
    for part in parts:
        part = orient(part, sign=1)
        # Low perimeter upstand catches sunlight and gives the roof thickness.
        parapet = part.difference(part.buffer(-.3, join_style=2))
        extrude('building-roof', parapet, height, height + .5)
        coords = list(part.exterior.coords)
        if kind in ['cargo_terminal', 'hangar', 'warehouse', 'industrial', 'arff']:
            bands = [(height * .65, min(height * .65 + 1.4, height - 1.2))]
        elif kind == 'parking':
            bands = [(z + 1.0, min(z + 2.25, height - .8)) for z in np.arange(0, height - 2, 3.2)]
        else:
            bands = [(z, min(z + 1.4, height - 1)) for z in np.arange(2, height - 2, 4)]
        # Keep detail bounded even for the large cargo footprint.
        step = max(7.5, part.length * max(len(bands), 1) / 128)
        for a0, b0 in zip(coords, coords[1:]):
            a = np.asarray(a0); b = np.asarray(b0)
            length = float(np.linalg.norm(b - a))
            if length < 4:
                continue
            u = (b - a) / length
            outward = np.array([u[1], -u[0]]) * .035
            for distance in np.arange(1.2, length - 2, step):
                p = a + u * distance + outward
                q = a + u * min(distance + step * .67, length - 1.2) + outward
                for lo, hi in bands:
                    if hi <= lo:
                        continue
                    face('glass', [(*p, lo), (*q, lo), (*q, hi), (*p, hi)])
                    panel_count += 1
            # A light concrete sill, below the roof, reads as a horizontal ledge.
            if length > 10:
                beam('building-roof', [*a, height - .6], [*b, height - .6], .32, .35)
        # Roof fixtures sit on the actual polygon; never bridge a courtyard.
        inset = part.buffer(-3)
        if part.area < 700 or inset.is_empty:
            continue
        rectangle = list(part.minimum_rotated_rectangle.exterior.coords)
        axis = max((np.asarray(b) - np.asarray(a) for a, b in zip(rectangle, rectangle[1:])), key=lambda v: np.linalg.norm(v))
        axis = axis / np.linalg.norm(axis)
        cross = np.array([-axis[1], axis[0]])
        center = np.array(part.representative_point().coords[0])
        unit_width = 2.4 if kind == 'parking' else 3.4
        unit_length = 5.4
        for offset in [-8, 8] if part.area > 2500 else [0]:
            c = center + axis * offset
            corners = [c - axis * unit_length / 2 - cross * unit_width / 2,
                       c + axis * unit_length / 2 - cross * unit_width / 2,
                       c + axis * unit_length / 2 + cross * unit_width / 2,
                       c - axis * unit_length / 2 + cross * unit_width / 2]
            unit = Polygon(corners)
            if not inset.covers(unit):
                continue
            extrude('building', unit, height + .05, height + 1.3)
            surface('building-roof', unit, height + 1.34)
            roof_unit_count += 1
    return {'facadePanels': panel_count, 'roofUnits': roof_unit_count, 'parapetHeightM': .5}

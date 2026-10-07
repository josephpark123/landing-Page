"""Offline presentation masks; unify taxiway enclosures by dominant surface."""
from shapely.geometry import Polygon
from shapely.ops import unary_union


def _polygons(shape):
    if shape.is_empty:
        return []
    if shape.geom_type == 'Polygon':
        return [shape]
    return [part for part in getattr(shape, 'geoms', []) if part.geom_type == 'Polygon']


def restore_taxiway_islands(aprons, taxiways, occupied, shoulder_width=4):
    """Use one continuous surface inside each taxiway/shoulder enclosure.

    At least 50% existing apron means all pavement; otherwise use turf. A
    turf-majority enclosure containing a saved terminal, stand or apron-link
    operating core is deferred rather than removing occupied pavement. The
    shoulders and taxiways define the boundary and are never altered here.
    """
    shoulders = taxiways.buffer(shoulder_width, quad_segs=3)
    turf_islands = []
    paved_islands = []
    report = []; skipped_occupied = []; examined = 0
    for patch in _polygons(shoulders):
        for ring in patch.interiors:
            # Subtract all shoulders so a disconnected taxiway patch nested
            # inside an enclosure cannot be mistaken for its turf interior.
            for island in _polygons(Polygon(ring).difference(shoulders)):
                if island.area < 200:
                    continue
                examined += 1
                overlap = island.intersection(aprons)
                fraction = overlap.area / island.area
                point = island.centroid
                entry = {
                    'center': [round(point.x, 2), round(point.y, 2)],
                    'bounds': [round(v, 2) for v in island.bounds],
                    'islandAreaM2': round(island.area, 3),
                    'apronCoverageBefore': round(fraction, 6),
                }
                if fraction >= .5 - 1e-12:
                    added_area = island.area - overlap.area
                    if added_area < .001:
                        continue
                    paved_islands.append(island)
                    report.append({**entry, 'decision': 'pavement', 'restoredTurfAreaM2': 0, 'addedPavementAreaM2': round(added_area, 3)})
                else:
                    if overlap.area < .001:
                        continue
                    if island.intersects(occupied):
                        skipped_occupied.append({**entry, 'reason': 'turf majority intersects saved operating core'})
                        continue
                    turf_islands.append(island)
                    report.append({**entry, 'decision': 'turf', 'restoredTurfAreaM2': round(overlap.area, 3), 'addedPavementAreaM2': 0})
    protected_turf = unary_union(turf_islands)
    filled_pavement = unary_union(paved_islands)
    updated = aprons.difference(protected_turf).union(filled_pavement).buffer(0)
    removed = aprons.difference(updated); added = updated.difference(aprons)
    changed = removed.union(added)
    assert updated.is_valid
    assert removed.intersection(occupied).area < .001, 'Island repair removed occupied pavement'
    assert updated.intersection(protected_turf).area < .001, 'Apron still crosses a selected turf island'
    assert filled_pavement.difference(updated).area < .001, 'Pavement-majority enclosure is not fully paved'
    assert changed.intersection(taxiways).area < .001, 'Island repair changed taxiway pavement'
    assert changed.difference(protected_turf.union(filled_pavement)).area < .001, 'Surface change escaped its enclosure'
    return updated, {
        'method': 'unify taxiway-shoulder enclosures by existing dominant surface; pavement wins ties',
        'islandsExamined': examined,
        'islandsRestored': len(turf_islands),
        'islandsPaved': len(paved_islands),
        'restoredTurfAreaM2': round(removed.area, 3),
        'addedPavementAreaM2': round(added.area, 3),
        'netPavementChangeM2': round(added.area - removed.area, 3),
        'pavementMajorityThreshold': .5,
        'maxExistingApronFraction': .5,
        'minimumEnclosureAreaM2': 200,
        'taxiwayShoulderWidthM': shoulder_width,
        'occupiedOverlapM2': round(protected_turf.intersection(occupied).area, 6),
        'occupiedPavementRemovedM2': round(removed.intersection(occupied).area, 6),
        'taxiwayOverlapM2': round(changed.intersection(taxiways).area, 6),
        'occupiedEnclosuresDeferred': len(skipped_occupied),
        'deferred': skipped_occupied,
        'islands': report,
    }

"""Remove unneeded aircraft templates without decoding or re-encoding any mesh.

The retained Draco streams, images, transforms, materials and metadata are
byte/semantically identical. This deliberately supports the exporter's static
GLB schema; unknown reference-bearing extensions are rejected, not guessed.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import struct
from urllib.parse import unquote, urlsplit

ALLOWED_EXTENSIONS = {
    'KHR_draco_mesh_compression', 'KHR_materials_clearcoat',
    'KHR_materials_ior', 'KHR_materials_specular', 'KHR_materials_unlit',
}
ARRAYS = ('nodes', 'meshes', 'materials', 'accessors', 'textures', 'images', 'samplers', 'bufferViews')
RUNTIME_EXTRAS = {'aircraftType', 'sourcePavementTone', 'targetNames'}
ROOT = Path(__file__).resolve().parents[1]


def image_payload(doc, blob, image, asset_base):
    if 'bufferView' in image:
        view = doc['bufferViews'][image['bufferView']]
        start = view.get('byteOffset', 0)
        return blob[start:start + view['byteLength']]
    reference = urlsplit(image['uri'])
    assert not reference.scheme and not reference.netloc, 'Only published local image URIs are supported'
    relative = unquote(reference.path)
    target = ROOT / relative.lstrip('/') if relative.startswith('/') else asset_base / relative
    return target.resolve().read_bytes()


def strip_authoring_extras(value):
    """Retain runtime flags and glTF morph-target names, remove production notes.

    The viewer reads aircraftType and sourcePavementTone. The GLTFLoader may
    consume targetNames. Component ledgers, pane indices and source paths are
    authoring diagnostics and are not read by this landing page.
    """
    if isinstance(value, dict):
        if 'extras' in value:
            retained = {k: v for k, v in value['extras'].items() if k in RUNTIME_EXTRAS}
            if retained:
                value['extras'] = retained
            else:
                del value['extras']
        for child in value.values():
            strip_authoring_extras(child)
    elif isinstance(value, list):
        for child in value:
            strip_authoring_extras(child)


def read_glb(path):
    raw = path.read_bytes()
    magic, version, length = struct.unpack_from('<4sII', raw)
    assert magic == b'glTF' and version == 2 and length == len(raw)
    chunks = {}
    pos = 12
    while pos < len(raw):
        size, kind = struct.unpack_from('<II', raw, pos)
        chunks[kind] = raw[pos + 8:pos + 8 + size]
        pos += 8 + size
    assert set(chunks) == {0x4e4f534a, 0x004e4942}
    return json.loads(chunks[0x4e4f534a]), chunks[0x004e4942], raw


def walk_texture_infos(value):
    if not isinstance(value, dict):
        return
    for key, child in value.items():
        if key.endswith('Texture') and isinstance(child, dict) and 'index' in child:
            yield child
        elif isinstance(child, dict):
            yield from walk_texture_infos(child)


def dependencies(doc, roots):
    used = {key: set() for key in ARRAYS}

    def node(index):
        if index in used['nodes']:
            return
        used['nodes'].add(index)
        item = doc['nodes'][index]
        assert 'skin' not in item and 'camera' not in item and not item.get('extensions')
        if 'mesh' in item:
            used['meshes'].add(item['mesh'])
        for child in item.get('children', []):
            node(child)

    for index in roots:
        node(index)
    for index in used['meshes']:
        for primitive in doc['meshes'][index]['primitives']:
            used['accessors'].update(primitive['attributes'].values())
            if 'indices' in primitive:
                used['accessors'].add(primitive['indices'])
            for target in primitive.get('targets', []):
                used['accessors'].update(target.values())
            if 'material' in primitive:
                used['materials'].add(primitive['material'])
            assert set(primitive.get('extensions', {})) <= {'KHR_draco_mesh_compression'}
            draco = primitive.get('extensions', {}).get('KHR_draco_mesh_compression')
            if draco:
                used['bufferViews'].add(draco['bufferView'])
    for index in used['accessors']:
        accessor = doc['accessors'][index]
        if 'bufferView' in accessor:
            used['bufferViews'].add(accessor['bufferView'])
        for sparse in accessor.get('sparse', {}).values():
            if isinstance(sparse, dict) and 'bufferView' in sparse:
                used['bufferViews'].add(sparse['bufferView'])
    for index in used['materials']:
        used['textures'].update(info['index'] for info in walk_texture_infos(doc['materials'][index]))
    for index in used['textures']:
        texture = doc['textures'][index]
        assert not texture.get('extensions')
        used['images'].add(texture['source'])
        if 'sampler' in texture:
            used['samplers'].add(texture['sampler'])
    for index in used['images']:
        image = doc['images'][index]
        if 'bufferView' in image:
            used['bufferViews'].add(image['bufferView'])
        else:
            assert 'uri' in image, 'Image has neither an embedded buffer view nor a URI'
    return used


def canonical_root(doc, blob, root, strip_extras=False, asset_base=None):
    """Resolve indices and offsets into referenced values and exact-byte hashes."""
    def resolve(kind, index):
        value = copy.deepcopy(doc[kind][index])
        if kind == 'bufferViews':
            start = value.pop('byteOffset', 0)
            value.pop('buffer')
            value['sha256'] = hashlib.sha256(blob[start:start + value['byteLength']]).hexdigest()
        elif kind == 'nodes':
            if 'mesh' in value:
                value['mesh'] = resolve('meshes', value['mesh'])
            if 'children' in value:
                value['children'] = [resolve('nodes', child) for child in value['children']]
        elif kind == 'meshes':
            for primitive in value['primitives']:
                primitive['attributes'] = {k: resolve('accessors', v) for k, v in primitive['attributes'].items()}
                if 'indices' in primitive:
                    primitive['indices'] = resolve('accessors', primitive['indices'])
                if 'material' in primitive:
                    primitive['material'] = resolve('materials', primitive['material'])
                if 'targets' in primitive:
                    primitive['targets'] = [{k: resolve('accessors', v) for k, v in target.items()} for target in primitive['targets']]
                draco = primitive.get('extensions', {}).get('KHR_draco_mesh_compression')
                if draco:
                    draco['bufferView'] = resolve('bufferViews', draco['bufferView'])
        elif kind == 'materials':
            for info in walk_texture_infos(value):
                info['index'] = resolve('textures', info['index'])
        elif kind == 'textures':
            value['source'] = resolve('images', value['source'])
            if 'sampler' in value:
                value['sampler'] = resolve('samplers', value['sampler'])
        elif kind in ('accessors', 'images'):
            if kind == 'images' and 'uri' in value:
                assert asset_base is not None, 'External image verification needs its published asset base'
                value['imageSha256'] = hashlib.sha256(image_payload(doc, blob, value, asset_base)).hexdigest()
            if 'bufferView' in value:
                value['bufferView'] = resolve('bufferViews', value['bufferView'])
            for sparse in value.get('sparse', {}).values():
                if isinstance(sparse, dict) and 'bufferView' in sparse:
                    sparse['bufferView'] = resolve('bufferViews', sparse['bufferView'])
        return value
    normalized = resolve('nodes', root)
    if strip_extras:
        strip_authoring_extras(normalized)
    return hashlib.sha256(json.dumps(normalized, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def prune(path, destination, required=None, strip_extras=False):
    assert path.resolve() != destination.resolve(), 'Always create a candidate first.'
    before, blob, raw = read_glb(path)
    assert not before.get('skins') and not before.get('animations')
    assert len(before['buffers']) == 1 and 'uri' not in before['buffers'][0]
    assert set(before.get('extensionsUsed', [])) <= ALLOWED_EXTENSIONS
    assert len(before['scenes']) == 1
    roots = before['scenes'][before.get('scene', 0)]['nodes']
    templates = {before['nodes'][i].get('extras', {}).get('aircraftType'): i for i in roots if before['nodes'][i].get('extras', {}).get('aircraftType')}
    required = set(templates) if required is None else required
    assert required <= set(templates), required - set(templates)
    static = [i for i in roots if i not in templates.values()]
    selected_roots = [i for i in roots if i in static or before['nodes'][i]['extras']['aircraftType'] in required]
    used = dependencies(before, selected_roots)
    maps = {kind: {old: new for new, old in enumerate(sorted(indices))} for kind, indices in used.items()}
    after = copy.deepcopy(before)
    for kind in ARRAYS:
        after[kind] = [copy.deepcopy(before[kind][index]) for index in sorted(used[kind])]
    after['scenes'][after.get('scene', 0)]['nodes'] = [maps['nodes'][i] for i in selected_roots]
    for node in after['nodes']:
        if 'mesh' in node:
            node['mesh'] = maps['meshes'][node['mesh']]
        if 'children' in node:
            node['children'] = [maps['nodes'][i] for i in node['children']]
    for mesh in after['meshes']:
        for primitive in mesh['primitives']:
            primitive['attributes'] = {k: maps['accessors'][v] for k, v in primitive['attributes'].items()}
            if 'indices' in primitive:
                primitive['indices'] = maps['accessors'][primitive['indices']]
            if 'material' in primitive:
                primitive['material'] = maps['materials'][primitive['material']]
            for target in primitive.get('targets', []):
                for key in target:
                    target[key] = maps['accessors'][target[key]]
            draco = primitive.get('extensions', {}).get('KHR_draco_mesh_compression')
            if draco:
                draco['bufferView'] = maps['bufferViews'][draco['bufferView']]
    for accessor in after['accessors']:
        if 'bufferView' in accessor:
            accessor['bufferView'] = maps['bufferViews'][accessor['bufferView']]
        for sparse in accessor.get('sparse', {}).values():
            if isinstance(sparse, dict) and 'bufferView' in sparse:
                sparse['bufferView'] = maps['bufferViews'][sparse['bufferView']]
    for material in after['materials']:
        for info in walk_texture_infos(material):
            info['index'] = maps['textures'][info['index']]
    for texture in after['textures']:
        texture['source'] = maps['images'][texture['source']]
        if 'sampler' in texture:
            texture['sampler'] = maps['samplers'][texture['sampler']]
    for image in after['images']:
        if 'bufferView' in image:
            image['bufferView'] = maps['bufferViews'][image['bufferView']]
    packed = bytearray()
    for view in after['bufferViews']:
        packed.extend(b'\0' * (-len(packed) % 4))
        old = view.get('byteOffset', 0)
        view['byteOffset'] = len(packed)
        packed.extend(blob[old:old + view['byteLength']])
    after['buffers'] = [{'byteLength': len(packed)}]
    json_size_before_strip = len(json.dumps(after, separators=(',', ':')).encode())
    if strip_extras:
        strip_authoring_extras(after)
    asset_base = path.parent.resolve()
    signatures = {before['nodes'][i]['name']: canonical_root(before, blob, i, strip_extras, asset_base) for i in selected_roots}
    assert signatures == {after['nodes'][maps['nodes'][i]]['name']: canonical_root(after, packed, maps['nodes'][i], strip_extras, asset_base) for i in selected_roots}, 'Retained semantic or bytes changed'
    encoded = json.dumps(after, separators=(',', ':')).encode()
    metadata_saved = json_size_before_strip - len(encoded)
    encoded += b' ' * (-len(encoded) % 4)
    packed.extend(b'\0' * (-len(packed) % 4))
    result = struct.pack('<4sII', b'glTF', 2, 28 + len(encoded) + len(packed)) + struct.pack('<II', len(encoded), 0x4e4f534a) + encoded + struct.pack('<II', len(packed), 0x004e4942) + packed
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(result)
    reopened, reopened_blob, _ = read_glb(destination)
    # A candidate keeps the original public-relative image URIs. It is verified
    # against the input's published base, then replaces that input atomically.
    assert signatures == {reopened['nodes'][i]['name']: canonical_root(reopened, reopened_blob, i, strip_extras, asset_base) for i in reopened['scenes'][0]['nodes']}
    static_deps = dependencies(before, static)
    plane_deps = dependencies(before, list(templates.values()))
    image_bytes = sum(before['bufferViews'][image['bufferView']]['byteLength'] for image in before['images'] if 'bufferView' in image)
    external_images = {image['uri']: hashlib.sha256(image_payload(before, blob, image, asset_base)).hexdigest() for image in before['images'] if 'uri' in image}
    bytes_of = lambda indices: sum(before['bufferViews'][i]['byteLength'] for i in indices)
    return {
        'input': str(path), 'candidate': str(destination), 'beforeBytes': len(raw), 'afterBytes': len(result),
        'savedBytes': len(raw) - len(result), 'savedPercent': round((1 - len(result) / len(raw)) * 100, 2),
        'unusedAuthoringExtrasStripped': strip_extras, 'metadataBytesSaved': metadata_saved,
        'jsonBytesBefore': len(json.dumps(before, separators=(',', ':')).encode()), 'jsonBytesAfter': len(encoded),
        'sha256Before': hashlib.sha256(raw).hexdigest(), 'sha256After': hashlib.sha256(result).hexdigest(),
        'keptTypes': sorted(required), 'removedTypes': sorted(set(templates) - required),
        'countsBefore': {kind: len(before[kind]) for kind in ARRAYS}, 'countsAfter': {kind: len(after[kind]) for kind in ARRAYS},
        'baselineBinaryBytes': {'staticIncludingTextures': bytes_of(static_deps['bufferViews']), 'aircraft': bytes_of(plane_deps['bufferViews']), 'embeddedImages': image_bytes},
        'externalImagesVerified': external_images, 'logicalAssetBase': str(asset_base),
        'staticRootCount': len(static), 'retainedRootSignatures': signatures,
        'verification': 'Every retained root has identical transforms, runtime extras, accessor descriptors, material/texture settings, Draco bytes and image bytes. No decode, quantization, simplification or image re-encoding.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--types', help='Comma-separated exact aircraft types; omitted keeps all templates')
    parser.add_argument('--strip-authoring-extras', action='store_true', help='Remove metadata unused by the landing viewer; keep runtime flags and morph target names')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    report = prune(args.input, args.output, set(args.types.split(',')) if args.types else None, args.strip_authoring_extras)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'retainedRootSignatures'}))

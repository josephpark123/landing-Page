"""Pack the Blender airport and original aircraft batches into one GLB."""
from pathlib import Path
import copy,json,struct,argparse
parser=argparse.ArgumentParser();parser.add_argument('--build',type=Path);parser.add_argument('--out',type=Path)
options=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1];OUT=(options.out or ROOT/'web/airport-mockup').resolve();BUILD=(options.build or ROOT/'output/airport-mockup').resolve()
ASSETS=BUILD/'assets'
MODEL_TYPES=list(json.loads((OUT/'scene.json').read_text(encoding='utf-8')).get('models',{}))
def read(path):
    raw=path.read_bytes();size=struct.unpack_from('<I',raw,12)[0]
    return json.loads(raw[20:20+size]),raw[28+size:]
doc,data=read(ASSETS/'airport.glb');data=bytearray(data)
keys=['bufferViews','accessors','materials','meshes','nodes','textures','images','samplers']
for typ in MODEL_TYPES:
    src,blob=read(ASSETS/(typ+'.glb'));offsets={k:len(doc.get(k,[])) for k in keys}
    assert not src.get('skins') and not src.get('animations')
    while len(data)%4:data.append(0)
    byte_offset=len(data);data.extend(blob)
    for v in src.get('bufferViews',[]):v['buffer']=0;v['byteOffset']=v.get('byteOffset',0)+byte_offset
    for a in src.get('accessors',[]):
        if 'bufferView'in a:a['bufferView']+=offsets['bufferViews']
    for m in src.get('meshes',[]):
        for p in m['primitives']:
            p['attributes']={k:v+offsets['accessors'] for k,v in p['attributes'].items()}
            if 'indices'in p:p['indices']+=offsets['accessors']
            if 'material'in p:p['material']+=offsets['materials']
    for n in src.get('nodes',[]):
        if 'mesh'in n:n['mesh']+=offsets['meshes']
        if 'children'in n:n['children']=[i+offsets['nodes'] for i in n['children']]
    for im in src.get('images',[]):
        if 'bufferView'in im:im['bufferView']+=offsets['bufferViews']
    for tex in src.get('textures',[]):
        if 'source'in tex:tex['source']+=offsets['images']
        if 'sampler'in tex:tex['sampler']+=offsets['samplers']
    def adjust_textures(value):
        if not isinstance(value,dict):return
        for k,v in value.items():
            if 'Texture' in k and isinstance(v,dict) and 'index'in v:v['index']+=offsets['textures']
            elif isinstance(v,dict):adjust_textures(v)
    for mat in src.get('materials',[]):adjust_textures(mat)
    for k in keys:
        if src.get(k):doc.setdefault(k,[]).extend(src[k])
    template=len(doc['nodes']);doc['nodes'].append({'name':'AircraftTemplate_'+typ,'children':[i+offsets['nodes'] for i in src['scenes'][src.get('scene',0)]['nodes']],'extras':{'aircraftType':typ}})
    doc['scenes'][doc.get('scene',0)]['nodes'].append(template)
    for extkey in ['extensionsUsed','extensionsRequired']:
        if src.get(extkey):doc[extkey]=sorted(set(doc.get(extkey,[])+src[extkey]))
def embed_texture(path):
    while len(data)%4:data.append(0)
    payload=path.read_bytes();index=len(doc.setdefault('bufferViews',[]));doc['bufferViews'].append({'buffer':0,'byteOffset':len(data),'byteLength':len(payload)});data.extend(payload)
    im=len(doc.setdefault('images',[]));doc['images'].append({'bufferView':index,'mimeType':'image/jpeg'})
    repeat={'magFilter':9729,'minFilter':9987,'wrapS':10497,'wrapT':10497}
    samplers=doc.setdefault('samplers',[])
    if repeat not in samplers:samplers.append(repeat)
    ti=len(doc.setdefault('textures',[]));doc['textures'].append({'source':im,'sampler':samplers.index(repeat)});return ti
texture_sets={kind:{suffix:embed_texture(ASSETS/(kind+'-'+suffix+'.jpg')) for suffix in ['diff','nor_gl','rough']} for kind in ['grass','apron','asphalt']}
def linear_byte(value):
    value=value/255
    return value/12.92 if value<=.04045 else ((value+.055)/1.055)**2.4
for mat in doc['materials']:
    name=mat.get('name','')
    typ='grass' if name=='grass' else 'apron' if name in ['apron','parking'] else 'asphalt' if name in ['runway','taxiway','road','road-deck'] else None
    if typ:
        # Source diffuse/normal/roughness set, shared and embedded once per kind.
        # The green roughness channel works with zero dielectric metal factor.
        textures=texture_sets[typ];pbr=mat['pbrMetallicRoughness']
        tint=linear_byte(189 if typ=='grass' else 245 if name in ['road','road-deck'] else 178 if name=='runway' else 190 if name=='taxiway' else 196)
        pbr.update(baseColorTexture={'index':textures['diff']},baseColorFactor=[tint,tint,tint,1],metallicRoughnessTexture={'index':textures['rough']},metallicFactor=0,roughnessFactor=1)
        mat['normalTexture']={'index':textures['nor_gl'],'scale':.55 if typ=='grass' else .7}
        mat.setdefault('extras',{})['sourcePavementTone']=True
doc['buffers']=[{'byteLength':len(data)}]
header=json.dumps(doc,separators=(',',':')).encode();header+=b' '*((-len(header))%4);data.extend(b'\0'*((-len(data))%4))
combined=struct.pack('<4sII',b'glTF',2,12+8+len(header)+8+len(data))+struct.pack('<II',len(header),0x4e4f534a)+header+struct.pack('<II',len(data),0x004e4942)+data
(BUILD/'airport-combined.glb').write_bytes(combined)
print(json.dumps({'combinedBytes':len(combined),'meshes':len(doc['meshes']),'materials':len(doc['materials'])}))

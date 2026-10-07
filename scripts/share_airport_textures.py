"""Externalize identical GLB textures without decoding/recompressing any asset.

Run after airport model export/pruning. Hash-named JPEG files are shared by all
six airports; each original buffer view and encoded image is verified bytewise.
"""
from pathlib import Path
import argparse, copy, hashlib, json, os, struct
ROOT=Path(__file__).resolve().parents[1]

def unpack(path):
    raw=path.read_bytes()
    magic,version,total=struct.unpack_from('<4sII',raw)
    if magic!=b'glTF' or version!=2 or total!=len(raw):raise ValueError('Invalid GLB')
    size,kind=struct.unpack_from('<II',raw,12)
    if kind!=0x4e4f534a:raise ValueError('Expected JSON chunk')
    doc=json.loads(raw[20:20+size]);offset=20+size
    length,kind=struct.unpack_from('<II',raw,offset)
    if kind!=0x004e4942:raise ValueError('Expected BIN chunk')
    return raw,doc,raw[offset+8:offset+8+length]

def view_bytes(doc,blob,index):
    view=doc['bufferViews'][index]
    if view.get('buffer',0)!=0:raise ValueError('Multiple buffers are not supported')
    start=view.get('byteOffset',0)
    return blob[start:start+view['byteLength']]

def pack(doc,blob):
    doc['buffers']=[{'byteLength':len(blob)}]
    header=json.dumps(doc,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    header+=b' '*((-len(header))%4);blob+=b'\0'*((-len(blob))%4)
    return struct.pack('<4sII',b'glTF',2,28+len(header)+len(blob))+struct.pack('<II',len(header),0x4e4f534a)+header+struct.pack('<II',len(blob),0x004e4942)+blob

def prepare(path,shared,backups):
    raw,original,blob=unpack(path);doc=copy.deepcopy(original)
    discarded=set();image_hashes=[]
    for image in doc.get('images',[]):
        if 'bufferView' not in image:
            target=(path.parent/image['uri']).resolve()
            payload=target.read_bytes();image_hashes.append(hashlib.sha256(payload).hexdigest());continue
        index=image.pop('bufferView');payload=view_bytes(original,blob,index)
        digest=hashlib.sha256(payload).hexdigest();image_hashes.append(digest)
        suffix={'image/jpeg':'.jpg','image/png':'.png','image/webp':'.webp'}.get(image.get('mimeType'))
        if not suffix:raise ValueError('Unsupported texture MIME type')
        target=shared/(digest+suffix)
        if target.exists() and target.read_bytes()!=payload:raise ValueError('Texture hash collision')
        target.write_bytes(payload)
        image['uri']=os.path.relpath(target,path.parent).replace('\\','/')
        discarded.add(index)
    if not discarded:return {'path':str(path.relative_to(ROOT)),'changed':False,'bytes':len(raw),'images':image_hashes}
    new_blob=bytearray();mapping={};views=[]
    for i,view in enumerate(doc.get('bufferViews',[])):
        if i in discarded:continue
        while len(new_blob)%4:new_blob.append(0)
        mapping[i]=len(views);updated=copy.deepcopy(view);updated['byteOffset']=len(new_blob)
        new_blob.extend(view_bytes(original,blob,i));views.append(updated)
    doc['bufferViews']=views
    def remap(value):
        if isinstance(value,dict):
            for key,item in list(value.items()):
                if key=='bufferView':
                    if item not in mapping:raise ValueError('An image buffer view is also used as geometry')
                    value[key]=mapping[item]
                else:remap(item)
        elif isinstance(value,list):
            for item in value:remap(item)
    remap(doc)
    # Encoded geometry/Draco streams are copied exactly, never re-encoded.
    for old,new in mapping.items():
        if view_bytes(original,blob,old)!=view_bytes(doc,new_blob,new):raise ValueError('Buffer content changed')
    for image,expected in zip(doc['images'],image_hashes):
        if hashlib.sha256((path.parent/image['uri']).read_bytes()).hexdigest()!=expected:raise ValueError('Image changed')
    result=pack(doc,bytes(new_blob))
    backup=backups/(path.parent.name+'-'+hashlib.sha256(raw).hexdigest()[:12]+'.glb')
    if not backup.exists():backup.write_bytes(raw)
    pending=path.with_suffix('.glb.pending');pending.write_bytes(result);pending.replace(path)
    return {'path':str(path.relative_to(ROOT)),'changed':True,'beforeBytes':len(raw),'afterBytes':len(result),'bufferViewsVerified':len(mapping),'images':image_hashes}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=ROOT/'web/airport-mockup');args=parser.parse_args()
    shared=args.root/'textures';shared.mkdir(parents=True,exist_ok=True)
    backups=ROOT/'output/airport-mockup/texture-backups';backups.mkdir(parents=True,exist_ok=True)
    paths=[args.root/'airport-scene.glb',*sorted((args.root/'airports').glob('*/airport-scene.glb'))]
    report=[prepare(p,shared,backups) for p in paths]
    output=ROOT/'output/airport-mockup/shared-textures-verification.json';output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps([{k:v for k,v in row.items() if k!='images'} for row in report]))
if __name__=='__main__':main()

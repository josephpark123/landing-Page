from pathlib import Path
import json,hashlib,re,time
root=Path(__file__).resolve().parents[1]
p=root/'web/airport-mockup/airports/catalog.json'
catalog=json.loads(p.read_text(encoding='utf-8'))
for entry in catalog['airports']:
    directory=root/entry['assetBase'].strip('/')
    scene=json.loads((directory/'scene.json').read_text(encoding='utf-8'))
    entry['counts']=scene['counts']
    entry['assets']={name:{'bytes':(directory/name).stat().st_size,'sha256':hashlib.sha256((directory/name).read_bytes()).hexdigest()} for name in ['airport-scene.glb','scene.json','replay.bin']}
    if 'playbackWindow' in scene:entry['playbackWindow']=scene['playbackWindow']
shared=root/'web/airport-mockup/textures'
catalog['sharedTextures']=[{'url':'/web/airport-mockup/textures/'+p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(shared.glob('*')) if p.is_file()]
catalog['generatedAt']=time.time();p.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
versions={entry['icao']:{name:asset['sha256'][:16] for name,asset in entry['assets'].items()} for entry in catalog['airports']}
picker=root/'web/airport-mockup/airports.js'
source=picker.read_text(encoding='utf-8')
source,count=re.subn(r'(// BEGIN GENERATED ASSET VERSIONS[^\n]*\n)\s*const assetVersions = .*?;\n(\s*// END GENERATED ASSET VERSIONS)',lambda m:m[1]+'  const assetVersions = '+json.dumps(versions,separators=(',',':'))+';\n'+m[2],source,flags=re.S)
if count!=1:raise RuntimeError('Airport asset version block is missing or ambiguous')
picker.write_text(source,encoding='utf-8')
print(json.dumps({'airports':len(catalog['airports']),'sharedTextures':len(catalog['sharedTextures'])}))

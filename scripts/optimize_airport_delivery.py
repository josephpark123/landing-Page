"""Finalize static airport delivery without changing rendered geometry or textures.

Call after exporting/rebuilding models. Re-running is safe; original scenario
exports remain in their cache and published inputs are backed up under output.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]

def optimize():
    assets=ROOT/'web/airport-mockup';reports=ROOT/'output/airport-mockup/delivery-optimization';reports.mkdir(parents=True,exist_ok=True)
    node=shutil.which('node')
    if not node:raise RuntimeError('Node.js is required for the lossless replay crop')
    subprocess.run([node,str(ROOT/'scripts/trim_airport_replay.cjs'),'--airport','RPLL','--start','07:00','--end','08:00','--apply'],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
    for directory in [assets,*sorted((assets/'airports').glob('*/'))]:
        path=directory/'airport-scene.glb'
        if not path.exists():continue
        original=path.read_bytes();backup=reports/(directory.name+'-'+hashlib.sha256(original).hexdigest()[:12]+'.original.glb')
        if not backup.exists():backup.write_bytes(original)
        candidate=reports/(directory.name+'.optimized.glb')
        command=[sys.executable,'-B',str(ROOT/'scripts/prune_airport_aircraft_glb.py'),'--input',str(path),'--output',str(candidate),'--strip-authoring-extras','--report',str(reports/(directory.name+'.json'))]
        if directory.name=='RPLL':
            meta=json.loads((directory/'scene.json').read_text(encoding='utf-8'))
            command+=['--types',','.join(sorted(meta['models']))]
        subprocess.run(command,cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
        pending=directory/'airport-scene.glb.pending';pending.write_bytes(candidate.read_bytes());pending.replace(path)
    subprocess.run([sys.executable,'-B',str(ROOT/'scripts/share_airport_textures.py')],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
    subprocess.run([sys.executable,'-B',str(ROOT/'scripts/refresh_airport_catalog.py')],cwd=ROOT,check=True)
    print('Prepared lossless geometry, shared textures and the Manila 07:00-08:00 replay.')

if __name__=='__main__':optimize()

"""Local-only static site for six prebuilt airports.

HTTP requests only serve published files. They never inspect simulator source,
expire models, or start geometry conversion. AirportService is retained as an
offline build utility; it is not instantiated by the server.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
PRESETS=[
    {'icao':'RKSI','iata':'ICN','name':'Incheon','city':'Incheon, South Korea','scenario':'RKSI_INITIAL_R1_NORMAL'},
    {'icao':'RPLL','iata':'MNL','name':'Manila','city':'Manila, Philippines','scenario':'REAL_MODEL_COPY'},
    {'icao':'RJAA','iata':'NRT','name':'Narita','city':'Narita, Japan','scenario':'RJAA_INITIAL'},
    {'icao':'VTBS','iata':'BKK','name':'Suvarnabhumi','city':'Bangkok, Thailand','scenario':'VTBS_INITIAL'},
    {'icao':'VVTS','iata':'SGN','name':'Tan Son Nhat','city':'Ho Chi Minh City, Vietnam','scenario':'VVTS_INITIAL'},
    {'icao':'LOWW','iata':'VIE','name':'Vienna','city':'Vienna, Austria','scenario':'LOWW_INITIAL'},
]
PRESET_CODES=frozenset(p['icao'] for p in PRESETS)
ASSET_NAMES={'scene.json','replay.bin','airport-scene.glb'}


class PublishedAirports:
    """Read-only compatibility API over the same static assets as the frontend."""
    def __init__(self,root=ROOT):
        self.root=Path(root)/'web/airport-mockup'

    def resolve(self,reference):
        code=str(reference or '').strip().upper()
        preset=next((p for p in PRESETS if code in [p['icao'],p['iata']]),None)
        if preset is None:raise ValueError('Select one of the six available airports: ICN, MNL, BKK, NRT, SGN or VIE.')
        return {k:v for k,v in preset.items() if k!='scenario'}

    def asset_path(self,code,name):
        if code not in PRESET_CODES or name not in ASSET_NAMES:raise ValueError('Unknown airport asset')
        return (self.root if code=='RKSI' else self.root/'airports'/code)/name

    def status(self,reference):
        airport=self.resolve(reference);code=airport['icao']
        ready=all(self.asset_path(code,name).is_file() for name in ASSET_NAMES)
        return {'state':'ready' if ready else 'missing','icao':code,'airport':airport,
                'assetBase':'/web/airport-mockup/' if code=='RKSI' else f'/web/airport-mockup/airports/{code}/',
                'prebuilt':True,'cached':True}


class AirportService:
    def __init__(self,source,cache,blender=None,node=None,gltf_cli=None):
        self.source=Path(source).resolve();self.cache=Path(cache).resolve()
        self.python=self.source/'.venv/Scripts/python.exe'
        if not self.python.exists():self.python=Path(sys.executable)
        self.blender=Path(blender or os.environ.get('AIRPORT_MOCKUP_BLENDER') or 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe')
        self.node=Path(node or os.environ.get('AIRPORT_MOCKUP_NODE') or Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe')
        if not self.node.exists():self.node=Path(shutil.which('node') or 'node')
        self.gltf_cli=Path(gltf_cli) if gltf_cli else None
        self.jobs={};self.lock=threading.RLock();self.pool=ThreadPoolExecutor(max_workers=1,thread_name_prefix='airport-build')
        self.cache.mkdir(parents=True,exist_ok=True)

    def resolve(self,reference):
        code=str(reference or '').strip().upper()
        preset=next((p for p in PRESETS if code in [p['icao'],p['iata']]),None)
        if preset is None:raise ValueError('Select one of the six available airports: ICN, MNL, BKK, NRT, SGN or VIE.')
        return {**{k:v for k,v in preset.items() if k!='scenario'},'country':''}

    def _paths(self,code):
        preset=next((p for p in PRESETS if p['icao']==code),None)
        if preset is None:raise ValueError('This airport is not available in the local preset list.')
        scenario=preset['scenario']
        return (self.source/'data/layouts'/(scenario+'.json'),self.source/'data/maps'/(code+'_map.json'),
                self.source/'data/runs'/(scenario+'_sim_result.json'))

    def _fingerprint(self,code):
        digest=hashlib.sha256(b'airport-cache-v3')
        for name in ['export_airport_mockup.py','airport_mockup_replay.py','airport_mockup_ground.py',
                     'airport_mockup_buildings.py','airport_mockup_terminals.py','airport_mockup_roads.py','airport_mockup_centerlines.py','airport_mockup_lights.py','build_airport_mockup_blender.py','package_airport_mockup.py']:
            path=ROOT/'scripts'/name
            if path.is_file():digest.update(path.read_bytes())
        for path in self._paths(code):
            if path.exists():digest.update(f'{path.name}:{path.stat().st_size}:{path.stat().st_mtime_ns}'.encode())
        return digest.hexdigest()

    def ready(self,code):
        if code=='RKSI':return {'state':'ready','icao':'RKSI','assetBase':'/web/airport-mockup/','cached':True}
        current=self.cache/code/'current';manifest=current/'cache.json'
        if not manifest.is_file() or not all((current/name).is_file() for name in ASSET_NAMES):return None
        try:
            data=json.loads(manifest.read_text(encoding='utf-8'))
            if data.get('fingerprint')!=self._fingerprint(code) or time.time()-data.get('createdAt',0)>7*86400:return None
        except (OSError,ValueError):return None
        return {'state':'ready','icao':code,'assetBase':f'/api/airport-assets/{code}/','cached':True,'airport':data.get('airport')}

    def select(self,reference):
        airport=self.resolve(reference);code=airport['icao']
        layout_path,map_path,_=self._paths(code)
        if not layout_path.is_file() or not map_path.is_file():
            raise ValueError(f'Saved layout or map files are missing for {code}. This local preview uses saved airport data only.')
        with self.lock:
            ready=self.ready(code)
            if ready:return {**ready,'airport':airport}
            existing=self.jobs.get(code)
            if existing and existing['state'] in ['queued','building']:return dict(existing)
            self.jobs[code]={'state':'queued','icao':code,'airport':airport,'progress':0,'label':'Waiting to prepare this airport'}
            self.pool.submit(self._build,airport)
            return dict(self.jobs[code])

    def status(self,code):
        with self.lock:return dict(self.jobs.get(code) or self.ready(code) or {'state':'missing','icao':code})

    def _update(self,code,**values):
        with self.lock:self.jobs[code].update(values)

    def _run(self,args,cwd,log,timeout=1200):
        completed=subprocess.run([str(a) for a in args],cwd=str(cwd),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                                 text=True,encoding='utf-8',errors='replace',timeout=timeout,
                                 creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        with log.open('a',encoding='utf-8') as handle:handle.write(completed.stdout+'\n')
        if completed.returncode:
            lines=[line for line in completed.stdout.splitlines() if line.strip()]
            raise RuntimeError('Airport conversion failed: '+(' '.join(lines[-3:])[-500:] or 'export process exited unexpectedly'))

    def _cli(self):
        if self.gltf_cli and self.gltf_cli.is_file():return self.gltf_cli
        root=Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'AppData/Local')))/'npm-cache/_npx'
        found=list(root.glob('*/node_modules/@gltf-transform/cli/bin/cli.js'))
        if not found:raise RuntimeError('The local glTF compression runtime is unavailable.')
        self.gltf_cli=found[0];return self.gltf_cli

    def _build(self,airport):
        code=airport['icao'];entry=self.cache/code;entry.mkdir(parents=True,exist_ok=True)
        fingerprint=self._fingerprint(code)
        self._update(code,state='building',label='Preparing saved airport geometry',progress=4)
        try:
            with tempfile.TemporaryDirectory(prefix='build-',dir=entry) as work_text:
                work=Path(work_text);out=work/'public';build=work/'intermediate';out.mkdir();build.mkdir()
                log=entry/'last-build.log';log.write_text('',encoding='utf-8')
                layout_path,map_path,result_path=self._paths(code)
                if not layout_path.is_file() or not map_path.is_file():
                    raise RuntimeError(f'Saved layout or map files are missing for {code}. This local preview uses saved airport data only.')
                self._update(code,label='Preparing airport surfaces and saved aircraft movements',progress=45)
                command=[self.python,'-X','utf8','-B',ROOT/'scripts/export_airport_mockup.py','--source',self.source,
                         '--layout',layout_path,'--map',map_path,'--out',out,'--build',build,'--icao',code,
                         '--airport',airport['name'],'--city',', '.join(x for x in [airport['city'],airport['country']] if x)]
                if result_path and result_path.is_file():command+=['--result',result_path]
                self._run(command,ROOT,log)
                self._update(code,label='Applying materials and combining the airport model',progress=72)
                self._run([self.blender,'--background','--python-exit-code','1','--python',ROOT/'scripts/build_airport_mockup_blender.py','--',self.source,'--build',build],ROOT,log)
                self._run([self.python,'-B',ROOT/'scripts/package_airport_mockup.py','--out',out,'--build',build],ROOT,log)
                self._update(code,label='Compressing the model for smooth browser playback',progress=90)
                self._run([self.node,self._cli(),'draco',build/'airport-combined.glb',out/'airport-scene.glb',
                           '--quantize-position','18','--quantize-normal','10','--quantize-texcoord','14',
                           '--decode-speed','10','--encode-speed','5'],ROOT,log)
                scene=json.loads((out/'scene.json').read_text(encoding='utf-8'))
                (out/'cache.json').write_text(json.dumps({'airport':airport,'createdAt':time.time(),
                    'fingerprint':fingerprint,'hasReplay':scene.get('hasReplay',False)}),encoding='utf-8')
                # Only remove our own previous cache entry; original files and
                # the shipping RKSI assets never participate in cache cleanup.
                current=entry/'current'
                if current.exists():
                    resolved=current.resolve()
                    if not resolved.is_relative_to(self.cache) or resolved.name!='current':raise RuntimeError('Invalid cache target')
                    shutil.rmtree(resolved)
                out.replace(current)
            self._update(code,state='ready',progress=100,label='Ready',assetBase=f'/api/airport-assets/{code}/',cached=False)
        except Exception as exc:
            self._update(code,state='error',label=str(exc)[:700],progress=0)


def make_handler(service=None):
    # Even an older caller passing AirportService cannot trigger builds through
    # HTTP. Keep the legacy API URLs read-only while old browser tabs reload.
    published=service if isinstance(service,PublishedAirports) else PublishedAirports()
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT),**kwargs)

        def _json(self,value,status=200):
            raw=json.dumps(value,separators=(',',':')).encode();self.send_response(status)
            self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Cache-Control','no-store')
            self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)

        def do_POST(self):
            if urlsplit(self.path).path!='/api/airports/select':return self._json({'error':'Not found'},404)
            origin=self.headers.get('Origin')
            if origin and urlsplit(origin).netloc!=self.headers.get('Host'):return self._json({'error':'Cross-origin request blocked'},403)
            try:
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=1024:raise ValueError('Invalid request size')
                body=json.loads(self.rfile.read(length))
                if not isinstance(body,dict):raise ValueError('Invalid selection')
                state=published.status(body.get('code'))
                if state['state']!='ready':return self._json({'error':'This prebuilt airport model is unavailable.'},404)
                self._json(state)
            except (ValueError,TypeError,json.JSONDecodeError) as exc:self._json({'error':str(exc)},400)

        def do_GET(self):
            parsed=urlsplit(self.path);path=unquote(parsed.path)
            if path=='/api/airports':return self._json({'presets':[{k:v for k,v in p.items() if k!='scenario'} for p in PRESETS]})
            if path.startswith('/api/airports/status/'):
                code=path.rsplit('/',1)[-1]
                if code not in PRESET_CODES:return self._json({'error':'This airport is not available in the local preset list.'},400)
                return self._json(published.status(code))
            if path.startswith('/api/airport-assets/'):
                parts=path.strip('/').split('/')
                if len(parts)!=4 or parts[2] not in PRESET_CODES or parts[3] not in ASSET_NAMES:return self._json({'error':'Not found'},404)
                target=published.asset_path(parts[2],parts[3])
                if not target.is_file():return self._json({'error':'This prebuilt airport model is unavailable.'},404)
                etag=f'"{target.stat().st_mtime_ns}-{target.stat().st_size}"'
                if self.headers.get('If-None-Match')==etag:
                    self.send_response(304);self.send_header('ETag',etag);self.end_headers();return
                self.send_response(200);self.send_header('Content-Type',self.guess_type(str(target)))
                self.send_header('Content-Length',str(target.stat().st_size));self.send_header('Cache-Control','private, no-cache');self.send_header('ETag',etag)
                self.end_headers()
                with target.open('rb') as handle:shutil.copyfileobj(handle,self.wfile)
                return
            if path.startswith('/api/'):return self._json({'error':'Not found'},404)
            segments=Path(path).parts
            if any(part.startswith('.') for part in segments) or (len(segments)>1 and segments[1] in ['scripts','output']):
                return self._json({'error':'Not found'},404)
            return super().do_GET()

        def list_directory(self,path):return self.send_error(404,'Not found')
    return Handler


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8765)
    parser.add_argument('--source',type=Path,default=ROOT.parent/'airside_simulation/airside_simulation_260903')
    parser.add_argument('--cache',type=Path,default=ROOT/'output/airport-mockup-cache')
    parser.add_argument('--blender');parser.add_argument('--node');parser.add_argument('--gltf-cli')
    args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),make_handler(PublishedAirports()))
    print(f'Airport Mockup: http://127.0.0.1:{args.port}/ (prebuilt airports; selected files only)',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()


if __name__=='__main__':main()

"""Explicit offline build: materialize the six selectable airports as static files.

The viewer never invokes this script. Existing current exports are reused when
their source/pipeline fingerprint matches; updates require rerunning this command.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import struct
import time
from airport_mockup_server import AirportService, PRESETS, ASSET_NAMES, ROOT


def validate(directory, code):
    for name in ASSET_NAMES:
        if not (directory/name).is_file():
            raise RuntimeError(f'{code}: missing {name}')
    scene=json.loads((directory/'scene.json').read_text(encoding='utf-8'))
    if scene.get('icao') != code:
        raise RuntimeError(f'{code}: exported airport identifier differs')
    with (directory/'airport-scene.glb').open('rb') as handle:
        magic, version, length=struct.unpack('<4sII',handle.read(12))
    if magic != b'glTF' or version != 2 or length != (directory/'airport-scene.glb').stat().st_size:
        raise RuntimeError(f'{code}: invalid GLB header or length')
    replay_bytes=(directory/'replay.bin').stat().st_size
    if replay_bytes%20 or any((track['offset']+track['count']*5)*4>replay_bytes for track in scene.get('tracks',[])):
        raise RuntimeError(f'{code}: replay sample range exceeds its binary data')
    return scene


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=ROOT.parent/'airside_simulation/airside_simulation_260903')
    parser.add_argument('--cache',type=Path,default=ROOT/'output/airport-prebuild-cache')
    parser.add_argument('--existing-cache',type=Path,default=ROOT/'output/airport-mockup-cache')
    parser.add_argument('--out',type=Path,default=ROOT/'web/airport-mockup/airports')
    parser.add_argument('--gltf-cli',type=Path)
    args=parser.parse_args()
    service=AirportService(args.source,args.cache,gltf_cli=args.gltf_cli)
    args.out.mkdir(parents=True,exist_ok=True)
    entries=[]
    try:
        for preset in PRESETS:
            code=preset['icao'];print(f'{code}: checking prepared model',flush=True)
            if code=='RKSI':
                prepared=ROOT/'web/airport-mockup';method='existing landing model'
            else:
                fingerprint=service._fingerprint(code);prepared=None
                for cache in [args.existing_cache,args.cache]:
                    candidate=cache/code/'current'
                    try:
                        manifest=json.loads((candidate/'cache.json').read_text(encoding='utf-8'))
                        if manifest.get('fingerprint')==fingerprint:
                            validate(candidate,code);prepared=candidate;break
                    except (OSError,ValueError,RuntimeError,KeyError,struct.error):
                        continue
                method='reused matching export'
                if prepared is None:
                    print(f'{code}: building saved airport model offline',flush=True)
                    airport=service.resolve(code)
                    service.jobs[code]={'state':'queued','icao':code,'airport':airport}
                    service._build(airport)
                    if service.jobs[code]['state']!='ready':
                        raise RuntimeError(f"{code}: {service.jobs[code].get('label','export failed')}")
                    prepared=args.cache/code/'current';method='built offline'
            scene=validate(prepared,code)
            destination=prepared if code=='RKSI' else args.out/code
            if destination!=prepared:
                destination.mkdir(parents=True,exist_ok=True)
                # Each completed file replaces its predecessor atomically;
                # original layouts and cached exports are never moved/deleted.
                for name in sorted(ASSET_NAMES):
                    pending=destination/(name+'.pending')
                    shutil.copyfile(prepared/name,pending);pending.replace(destination/name)
            assets={name:{'bytes':(destination/name).stat().st_size,
                          'sha256':hashlib.sha256((destination/name).read_bytes()).hexdigest()}
                    for name in sorted(ASSET_NAMES)}
            entry={k:v for k,v in preset.items() if k!='scenario'}
            entry.update(assetBase='/web/airport-mockup/' if code=='RKSI' else f'/web/airport-mockup/airports/{code}/',
                         sourceScenario=scene['scenario'],counts=scene['counts'],assets=assets,method=method)
            entries.append(entry)
            print(f"{code}: ready, GLB {assets['airport-scene.glb']['bytes']/1e6:.2f} MB ({method})",flush=True)
        catalog={'format':1,'generatedAt':time.time(),'loadMode':'prebuilt-static','airports':entries}
        pending=args.out/'catalog.json.pending';pending.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
        pending.replace(args.out/'catalog.json')
        # Keep the published peak-hour window, unused-aircraft pruning and
        # shared immutable textures when rebuilding from full source exports.
        if args.out.resolve()==(ROOT/'web/airport-mockup/airports').resolve():
            from optimize_airport_delivery import optimize
            optimize()
        print(f'All {len(entries)} airports prepared. Selection only loads static assets.',flush=True)
    finally:
        service.pool.shutdown(wait=True)


if __name__=='__main__':
    main()

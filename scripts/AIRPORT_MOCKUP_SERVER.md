# Prebuilt airport selection

Run from the landing-page repository in PowerShell:

```powershell
python -X utf8 -B scripts/airport_mockup_server.py --port 8765
```

This serves the existing website and the airport API at `http://127.0.0.1:8765/`.
The process binds only to localhost. Serving the published files needs only
Python 3; Blender, Node.js, and the source simulator checkout are not required.
A plain static file server works too.

The initial ICN view uses the bundled RKSI assets. The selector offers ICN,
MNL, BKK, NRT, SGN, and VIE. Opening the selector does not load airport layouts
or start conversions. Only these six saved airport presets are supported.
Selecting an airport immediately navigates to its prebuilt files. The browser
downloads only that airport's GLB, scene JSON, replay binary, and any uncached
shared texture images. No API request,
conversion job, status polling, or other-airport prefetch occurs.

Saved presets reuse the source layouts/maps and recorded runs. MNL uses
`REAL_MODEL_COPY`; the other presets use their corresponding `*_INITIAL`
scenario. Selection never reads source layout or map files. Airports without saved movement
data have an interactive static view; replay controls are hidden.

The curated ICN files remain in `web/airport-mockup/`. The other five airports
are published in `web/airport-mockup/airports/{ICAO}/`, each with
`airport-scene.glb`, `scene.json`, and `replay.bin`. The adjacent `catalog.json`
records sizes and SHA256 hashes. Published files do not expire.

To explicitly refresh the published models after source changes:

```powershell
& '../airside_simulation/airside_simulation_260903/.venv/Scripts/python.exe' -X utf8 -B scripts/prebuild_airport_models.py
```

This offline command needs the saved source files, Blender 5.2, and Node.js with
the glTF Transform CLI. It reuses matching exports or creates updated ones,
then publishes only final web assets. ICN is retained from the existing landing
export; rebuild it with the RKSI steps in `airport-mockup.md` when needed.
Overrides are `--source`, `--cache`, `--existing-cache`, `--out`, and `--gltf-cli`.
Original files are read-only. Build intermediates remain in ignored
`output/airport-prebuild-cache/` and are never served.

API summary:

- `GET /api/airports`: preset metadata only.
- `POST /api/airports/select` with JSON `{"code":"RPLL"}`: read-only compatibility
  endpoint returning the published asset base. It cannot start a build.
- `GET /api/airports/status/RPLL`: published file availability.
- `/api/airport-assets/RPLL/`: compatibility URLs for the static published files.

The exporter and renderer preserve source metres, mirrored layout Y, Z-up,
saved aircraft P2 anchors, and heading conventions. Other airports derive camera
views from their own site/terminal bounds. RKSI's displayed replay window is
12:00–12:20 and loops. RPLL loops 07:00–08:00 using the next-day portion of its
saved run across midnight; other saved runs retain their full recorded range.

The static site and all six prebuilt airports are deployed to
`https://teamflexa.vercel.app/`; no conversion backend is needed.

Mobile navigation (2026-09-08):

- The custom airport picker uses a desktop popover or a mobile bottom sheet.
  Airport changes use normal navigation with no cross-document slide.
- Before airport or mobile Solutions navigation, the old runtime cancels RAF,
  fetches and Draco work, disposes mesh/texture/shadow resources, closes decoded
  ImageBitmaps, loses its WebGL context and removes its canvas.
- Coarse-pointer/mobile and KakaoTalk browser profiles cap rendering DPR at 1.1,
  shadow maps at 1024, and Draco decoding at one worker. Desktop keeps DPR 1.4.
- Mobile Solutions/Mock up navigation slides one live page at a time; it does
  not retain a cross-document WebGL snapshot. History return restores the same
  airport, camera and replay state; a disposed BFCache page reloads safely.
- Solutions controls initialize before the async translation bundle. Font
  styles load without blocking rendering. Videos begin after the first paint
  and release their buffers before returning to the airport.

Validation includes real Chromium interactions with mobile viewport, touch and
DPR 3 emulation, plus a KakaoTalk user-agent profile and throttled network. It
is not a physical-device test of the KakaoTalk application. Reports are in
`output/playwright/mobile-production-*.json` and `.txt`.


Delivery optimization (2026-09-08):

- Run `python -B scripts/optimize_airport_delivery.py` after a fresh export.
  Default `prebuild_airport_models.py` output invokes it automatically. It crops
  RPLL to the 07:00–08:00 peak, retains the exact boundary interpolation samples
  and original time anchor, removes unused aircraft and authoring metadata, and
  shares the nine original JPEGs across all six airports. It does not recompress
  textures, change retained Draco geometry, or reduce visible rendering quality.
- RPLL retains 78 aircraft records and 15 types; replay.bin is 424,600 bytes.
  The full original recording remains in ignored source/export caches and the
  replay backup. Use that original with `trim_airport_replay.cjs --source-dir`
  if a future requested time range is wider.
- `refresh_airport_catalog.py` records actual asset hashes and updates the
  generated version map in airports.js. Run it after any manual published asset
  change. The runtime fetches each GLB/JSON/binary with its content version.
- Vercel gives these versioned requests a one-year immutable browser cache.
  Unversioned data and the HTML/JS bootstrap continue to revalidate, allowing
  newly deployed versions to be discovered. Hashed shared JPEGs and the selected
  language JSON use the same immutable policy. Cache eviction by the browser
  still requires a later download. HTTP caching does not keep old GPU scenes alive.
- Solutions embeds only English and loads another language when selected or
  restored from the visitor's preference. See I18N_BUNDLES.md for the exact-value
  canonical locale generator. Visible preview/current explanation videos load
  on demand; at most one next video is prepared ahead of the current slide.

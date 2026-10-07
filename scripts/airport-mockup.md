# Airport Mockup — local presentation export

The homepage `/` is the Airport Mockup. Its **Solutions** link opens the previous
homepage, preserved at `/solutions.html`. That page's **Mock up** link returns
to `/`; it never loads the 3D model until navigation. The pale blue arrow on
the left shows **Mock up** on hover or keyboard focus. Both pages use native
cross-document view transitions (1050 ms) to slide in opposite directions.
The return restores camera, replay position, speed, and weather from this tab.
If the browser cannot restore the page from its back/forward cache, the slide
waits for the first airport frame, bounded at 2.5 seconds. Direct visits and
browsers without view transitions use ordinary navigation. Reduced-motion
preferences disable the slide. The earlier
`/web/airport-mockup/` URL remains available. Serve the repository with Python's
HTTP server on port 8765. No deployment is part of this change.

## Prebuilt airport selection

All six airport models are generated before the site is served. RKSI assets are
under `web/airport-mockup/`; RPLL, RJAA, VTBS, VVTS and LOWW each have the three
published files (`scene.json`, `replay.bin`, `airport-scene.glb`) under
`web/airport-mockup/airports/<ICAO>/`. `airports/catalog.json` records the published
model versions. Run `scripts/prebuild_airport_models.py` offline when source
layouts, exports or materials change; original simulator data stays read-only.

The selector navigates directly to the selected preset. There is no selection
API call, build queue, polling, or download of the other five airport models.
ICAO and IATA URL aliases are limited to these six presets. All model data loads
from static paths, so the viewer also works with an ordinary static HTTP server.
`airport_mockup_server.py` serves the same published files; its legacy API routes
only report file availability and never inspect source hashes, expire files or
start conversion. `AirportService` remains an offline build utility only.

## Rebuild

1. Run `export_airport_mockup.py --source <absolute BluPrint repository>` with
   that repository's virtual-environment Python (`-X utf8 -B`). It reads the
   saved RKSI layout/result/map through the existing schema adapter.
2. Run Blender 5.2 in background with `--python-exit-code 1 --python
   scripts/build_airport_mockup_blender.py -- <absolute BluPrint repository>`.
3. Run `python -B scripts/package_airport_mockup.py`.
4. With Node 22+ and `@gltf-transform/cli` 4.3.0, run `gltf-transform draco
   output/airport-mockup/airport-combined.glb
   web/airport-mockup/airport-scene.glb --quantize-position 18
   --quantize-normal 10 --quantize-texcoord 14 --decode-speed 10 --encode-speed 5`.

The shipping GLB contains the static airport, four original aircraft templates,
and references to shared, content-hashed original JPEGs. Intermediate geometry, individual GLBs, source texture
copies, Blender file, and verification artifacts stay in the ignored
`output/airport-mockup/` directory. `scene.json` and `replay.bin` are the small,
separately seekable movement dataset; seeking requires no new network requests.

## Spatial and presentation contract

- Metres, Z-up; X = layout X − 14500, Y = 15000 − layout Y.
- Aircraft use the original P2 anchor, +X nose, +Y left, and negated layout
  heading. Heading is unwrapped before interpolation, including pushback.
- Ground positions retain every moving sample from the saved result; duplicate
  stationary samples are omitted. Ground clearance is 0.32 m in the viewer.
- Airborne height is an illustrative 3° profile derived from distance to the
  first/last saved ground position. It is not a recorded flight altitude.
- Terminal footprints and stand positions are original. Materials, shallow
  crowned roofs, stand paving extensions, and lighting are presentation work,
  not a survey-accurate architectural model.
- Grass is the site footprint minus all paved footprints, so it has no area
  underneath apron/ramp, taxiway, runway, road, shoulder or parking surfaces.
  `ground-separation.json` verifies zero turf/pavement overlap. Position
  compression uses 18 bits to retain these boundaries at airport scale. The
  renderer uses conventional depth with MSAA, distance-aware near/far clipping,
  and polygon offset for markings. Paint is deduplicated, clipped to its receiving
  pavement, placed 4 cm above it, and faded with distance to avoid subpixel shimmer.
- The saved run reports `simulation_truncated_deadlock`; playback displays only
  its available timeline. This viewer does not rerun or alter the simulator.
- `export-report.json` records input hashes, coordinate checks, and counts.
- Existing aircraft GLBs are reused; this is not a new certified aircraft asset.
- General buildings use neutral gray walls and roofs, separately merged from the
  terminal's pale blue roof. Saved total heights take priority; OSM height or
  floor counts fill missing values. Defaults are marked in `buildings-report.json`.
  Solar farms and weather-observation grounds are not extruded as solid buildings.
  The presentation cleanup joins short sawtooth recesses around nine separate
  remote ramps, preserving large grass islands and limiting area growth per ramp.

## Rendering and verification

Three.js r128 and its matching loaders are self-hosted. Static meshes are merged
by material; visible aircraft share instanced geometry. The scene is rendered
only when playing or when interaction changes it. Hidden tabs do not render.
Shadows refresh on camera relocation, not on every simulation frame. DPR is
capped at 1.4. No post-processing render chain or live simulation engine loads.

Night is the sole lighting toggle, with an accessible name and pressed state.
Night batches source-inspired blue taxiway edges,
green centre lines, runway lights, and the source area's mast lights into one
point cloud. A single instanced plane batch approximates apron light pools.
These are visual presets, not meteorological or photometric simulations. No
new GLB, HDR download, per-lamp shadow map, or live reflection pass is needed.
Weather freezes with pause, and repeated toggles reuse the same GPU resources.

Use `window.airportMockup.getSnapshot()` for load timing, renderer counts,
frame intervals, active/drawn aircraft, and render-frame count. The RAF intervals
are presentation measurements, not GPU timings. `sampleAircraft(id)` allows
deterministic seek checks. Verify pause, repeat seek, end/restart, orbit/pan/zoom,
mobile layout, reduced motion, no Solutions model request, one viewer model
request, and console errors in a real browser. Capture the initial, terminal,
airside, overview, and opposite-side views, plus day/night and both
directions of the page slide. Check return-state restoration and toolbar focus.

OSM map data attribution remains visible in the viewer. Original aircraft and
texture assets stay under the source project's existing licensing terms.

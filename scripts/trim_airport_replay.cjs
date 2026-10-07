#!/usr/bin/env node
/* Losslessly retain one absolute playback window in a prebuilt Float32 replay.
 * Time values retain meta.start as their original anchor: rebasing float32 times
 * would change interpolation. Boundary samples bracket both ends of the window.
 * Example:
 * node scripts/trim_airport_replay.cjs --airport RPLL --start 07:00 --end 08:00 --apply
 * Rebuild from the preserved input with --source-dir <backup> --output-dir <site>.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const args = process.argv.slice(2), options = {};
for (let i = 0; i < args.length; i++) {
  const key = args[i];
  assert(key.startsWith('--'), `Unexpected argument ${key}`);
  options[key.slice(2)] = key === '--apply' ? true : args[++i];
}
const icao = options.airport || 'RPLL';
assert(/^[A-Z]{4}$/.test(icao), 'Expected a four-letter ICAO');
const outputDir = path.resolve(options['output-dir'] || path.join(root, 'web/airport-mockup/airports', icao));
const sourceDir = path.resolve(options['source-dir'] || outputDir);
const sourceJson = fs.readFileSync(path.join(sourceDir, 'scene.json'));
const sourceBin = fs.readFileSync(path.join(sourceDir, 'replay.bin'));
const source = JSON.parse(sourceJson);
assert.equal(source.icao, icao);
assert.equal(source.stride, 5, 'Expected time/x/y/z/heading float32 records');
assert.equal(sourceBin.byteLength % 20, 0);
const values = new Float32Array(sourceBin.buffer, sourceBin.byteOffset, sourceBin.byteLength / 4);
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
function seconds(clock) {
  assert(/^\d\d:\d\d(?::\d\d)?$/.test(clock), `Invalid clock ${clock}`);
  const [h, m, s = 0] = clock.split(':').map(Number);
  assert(h < 24 && m < 60 && s < 60, `Invalid clock ${clock}`);
  return h * 3600 + m * 60 + s;
}
const startClock = seconds(options.start || '07:00'), endClock = seconds(options.end || '08:00');
assert(endClock > startClock, 'This tool expects a same-day playback window');
let day = options.day === undefined ? Math.floor(source.start / 86400) : Number(options.day);
if (options.day === undefined && day * 86400 + endClock < source.start) day++;
const start = day * 86400 + startClock, end = day * 86400 + endClock;
assert(start >= source.start && end <= source.end, 'Playback window is outside the recorded source interval');
const relativeStart = start - source.start, relativeEnd = end - source.start;
if (source.playbackWindow) {
  assert(start >= source.playbackWindow.start && end <= source.playbackWindow.end,
    'Use an original backup when widening an already-trimmed replay window');
}
function indexAt(track, t, data) {
  let lo = 0, hi = track.count - 1;
  while (lo + 1 < hi) {
    const mid = (lo + hi) >>> 1;
    if (data[track.offset + mid * 5] <= t) lo = mid; else hi = mid;
  }
  return lo;
}
function poseAt(track, t, data) {
  const offset = track.offset + indexAt(track, t, data) * 5;
  const next = Math.min(offset + 5, track.offset + (track.count - 1) * 5);
  const dt = data[next] - data[offset];
  const a = dt > 0 ? Math.max(0, Math.min(1, (t - data[offset]) / dt)) : 0;
  return [1, 2, 3, 4].map(k => data[offset + k] + (data[next + k] - data[offset + k]) * a);
}
function active(track, t, pose) {
  const b = source.siteBounds;
  return t >= track.start && t <= track.end && pose[0] > b[0] - 2000 && pose[0] < b[2] + 2000 && pose[1] > b[1] - 2000 && pose[1] < b[3] + 2000;
}
let offset = 0;
const blocks = [], tracks = [], ranges = [];
for (const track of source.tracks) {
  assert(Number.isInteger(track.count) && track.count > 0);
  assert(track.offset >= 0 && track.offset + track.count * 5 <= values.length);
  if (track.end < relativeStart || track.start > relativeEnd) continue;
  const first = indexAt(track, Math.max(relativeStart, track.start), values);
  const last = Math.min(track.count - 1, indexAt(track, Math.min(relativeEnd, track.end), values) + 1);
  const count = last - first + 1;
  const block = sourceBin.subarray((track.offset + first * 5) * 4, (track.offset + (last + 1) * 5) * 4);
  blocks.push(block); tracks.push({...track, offset, count});
  ranges.push({id: track.id, type: track.type, originalCount: track.count, first, last, count});
  offset += count * 5;
}
const trimmedBin = Buffer.concat(blocks);
const trimmedData = new Float32Array(trimmedBin.buffer, trimmedBin.byteOffset, trimmedBin.byteLength / 4);
const neededTypes = [...new Set(tracks.map(track => track.type))].sort();
assert(neededTypes.every(type => source.models[type]), 'A retained track has no aircraft template');
const meta = {...source, tracks, models: Object.fromEntries(neededTypes.map(type => [type, source.models[type]])),
  initialTime: relativeStart, playbackWindow: {start, end, loop: true},
  hasReplay: tracks.length > 0, counts: {...source.counts, flights: tracks.length}};
// Deliberately preserve source.start/end/duration and every retained binary value;
// playbackWindow alone defines the public timeline, without shifting Float32 time.
const trimmedJson = Buffer.from(JSON.stringify(meta));
const byId = new Map(tracks.map(track => [track.id, track]));
const times = new Set([relativeStart, relativeEnd]);
for (let t = relativeStart; t < relativeEnd; t += 1) times.add(t);
for (const track of tracks) {
  for (const boundary of [track.start, track.end]) for (const delta of [-1e-6, 0, 1e-6]) {
    const t = boundary + delta; if (t >= relativeStart && t <= relativeEnd) times.add(t);
  }
  for (let i = 0; i < track.count; i++) {
    const t = trimmedData[track.offset + i * 5];
    if (t >= relativeStart && t <= relativeEnd) times.add(t);
    if (i > 0) {
      const midpoint = (t + trimmedData[track.offset + (i - 1) * 5]) / 2;
      if (midpoint >= relativeStart && midpoint <= relativeEnd) times.add(midpoint);
    }
  }
}
let posesCompared = 0, visibilityCompared = 0, minVisible = Infinity, maxVisible = 0;
const snapshots = [];
for (const t of [...times].sort((a, b) => a - b)) {
  let beforeVisible = 0, afterVisible = 0;
  for (const original of source.tracks) {
    const before = poseAt(original, t, values), wasActive = active(original, t, before);
    beforeVisible += Number(wasActive);
    const retained = byId.get(original.id);
    if (!retained) { assert(!wasActive, `Removed visible aircraft ${original.id} at ${t}`); continue; }
    // Outside each track's active lifetime its interpolated position is immaterial.
    if (t >= original.start && t <= original.end) {
      const after = poseAt(retained, t, trimmedData);
      assert(before.every((value, i) => value === after[i]), `Interpolation changed for ${original.id} at ${t}`);
      posesCompared++;
      afterVisible += Number(active(retained, t, after));
    }
  }
  assert.equal(afterVisible, beforeVisible, `Visibility changed at ${t}`);
  visibilityCompared++;
  minVisible = Math.min(minVisible, beforeVisible); maxVisible = Math.max(maxVisible, beforeVisible);
  if (t === relativeStart || t === relativeEnd || Math.abs((t - relativeStart) % 600) < 1e-6) snapshots.push({absoluteTime: source.start + t, visible: beforeVisible});
}
const backupDir = path.resolve(options['backup-dir'] || path.join(root, 'output/airport-mockup/replay-backups', `${icao}-${hash(sourceBin).slice(0, 12)}`));
const reportFile = path.resolve(options.report || path.join(root, 'output/airport-mockup', `${icao.toLowerCase()}-replay-window-verification.json`));
const fingerprint = (json, bin, data) => ({sceneBytes: json.length, replayBytes: bin.length, sceneSha256: hash(json), replaySha256: hash(bin), tracks: data.tracks.length, samples: bin.length / 20, models: Object.keys(data.models).length});
const report = {icao, window: meta.playbackWindow, relativeStart, relativeEnd, timeAnchor: source.start,
  method: 'Original Float32 samples, boundary interpolation brackets, original absolute-time anchor',
  sourceDir, outputDir, backupDir, before: fingerprint(sourceJson, sourceBin, source), after: fingerprint(trimmedJson, trimmedBin, meta),
  aircraftTypes: neededTypes, templates: neededTypes.map(type => source.models[type].template), removedTrackCount: source.tracks.length - tracks.length,
  verification: {pass: true, timestampCount: times.size, exactPosesCompared: posesCompared, visibilityCompared, minVisible, maxVisible, snapshots}, ranges, applied: Boolean(options.apply)};
fs.mkdirSync(path.dirname(reportFile), {recursive: true});
if (options.apply) {
  fs.mkdirSync(backupDir, {recursive: true});
  for (const [name, bytes] of [['scene.json', sourceJson], ['replay.bin', sourceBin]]) {
    const target = path.join(backupDir, name);
    if (fs.existsSync(target)) assert.equal(hash(fs.readFileSync(target)), hash(bytes), `Backup mismatch: ${target}`);
    else fs.writeFileSync(target, bytes, {flag: 'wx'});
  }
  fs.mkdirSync(outputDir, {recursive: true});
  fs.writeFileSync(path.join(outputDir, 'replay.bin'), trimmedBin);
  fs.writeFileSync(path.join(outputDir, 'scene.json'), trimmedJson);
}
fs.writeFileSync(reportFile, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({applied: report.applied, aircraftTypes: neededTypes, before: report.before, after: report.after,
  reductionPercent: Math.round((1 - trimmedBin.length / sourceBin.length) * 10000) / 100,
  verification: report.verification, report: reportFile, backup: backupDir}));

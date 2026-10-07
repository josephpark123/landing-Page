#!/usr/bin/env node
'use strict';

// Canonical translations live in locales/*.json (excluded from deployment).
// Run: node scripts/build_i18n_bundles.cjs
// --import-legacy is only for migrating the original all-language i18n.js.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const zlib = require('node:zlib');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const sourceDir = path.join(root, 'locales');
const outputDir = path.join(root, 'web', 'i18n');
const bootstrapPath = path.join(root, 'i18n.js');
const languages = ['en','ko','zh','ja','es','th','vi','id','ru','uz','kk','de','fr','ar','km','am','ur','pt','it','nl','he'];
const compact = value => JSON.stringify(value);
const sizes = bytes => ({raw: bytes.length, gzip: zlib.gzipSync(bytes, {level: 9}).length,
  brotli: zlib.brotliCompressSync(bytes, {params: {[zlib.constants.BROTLI_PARAM_QUALITY]: 11}}).length});
let legacyPacks, legacyBytes;
if (process.argv.includes('--import-legacy')) {
  legacyBytes = fs.readFileSync(bootstrapPath);
  const sandbox = {window: {}};
  vm.runInNewContext(legacyBytes.toString('utf8'), sandbox, {timeout: 1000});
  legacyPacks = JSON.parse(JSON.stringify(sandbox.window.FLEXA_I18N));
  assert.equal(Object.keys(legacyPacks).length, languages.length, 'Expected the original 21-language bundle');
  fs.mkdirSync(sourceDir, {recursive: true});
  for (const lang of languages) {
    assert.ok(legacyPacks[lang], 'Missing original language: ' + lang);
    fs.writeFileSync(path.join(sourceDir, lang + '.json'), JSON.stringify(legacyPacks[lang], null, 2) + '\n');
  }
}
const packs = Object.fromEntries(languages.map(lang => [lang, JSON.parse(fs.readFileSync(path.join(sourceDir, lang + '.json'), 'utf8'))]));
for (const [lang, pack] of Object.entries(packs)) {
  assert.ok(Object.keys(pack).length && Object.values(pack).every(value => typeof value === 'string'), 'Invalid locale: ' + lang);
  if (legacyPacks) assert.deepEqual(pack, legacyPacks[lang], 'Translation changed: ' + lang);
}
fs.mkdirSync(outputDir, {recursive: true});
const files = {}, metrics = {};
for (const lang of languages.filter(lang => lang !== 'en')) {
  const bytes = Buffer.from(compact(packs[lang]) + '\n');
  const hash = crypto.createHash('sha256').update(bytes).digest('hex').slice(0, 12);
  const name = `${lang}.${hash}.json`;
  fs.writeFileSync(path.join(outputDir, name), bytes);
  files[lang] = 'web/i18n/' + name;
  metrics[lang] = sizes(bytes);
  assert.deepEqual(JSON.parse(fs.readFileSync(path.join(outputDir, name), 'utf8')), packs[lang]);
}
const bootstrap = fs.readFileSync(path.join(__dirname, 'i18n-bootstrap.template.js'), 'utf8')
  .replace('__LOCALE_FILES__', compact(files)).replace('__ENGLISH_PACK__', compact(packs.en));
fs.writeFileSync(bootstrapPath, bootstrap);
// Remove only obsolete generated JSON files in this exact output directory.
const retained = new Set(Object.values(files).map(file => path.basename(file)));
for (const name of fs.readdirSync(outputDir)) {
  if (/^[a-z]{2}\.[a-f0-9]{12}\.json$/.test(name) && !retained.has(name)) fs.unlinkSync(path.join(outputDir, name));
}
const sandbox = {window: {}, document: {currentScript: {src: 'https://example.test/i18n.js'}}, URL, Map, Object};
vm.runInNewContext(bootstrap, sandbox, {timeout: 1000});
assert.deepEqual(JSON.parse(JSON.stringify(sandbox.window.FLEXA_I18N.en)), packs.en);
const report = {languages: languages.length, keys: Object.fromEntries(languages.map(lang => [lang, Object.keys(packs[lang]).length])),
  original: legacyBytes ? sizes(legacyBytes) : undefined, englishBootstrap: sizes(Buffer.from(bootstrap)), locales: metrics,
  verified: 'All 21 canonical locale packs equal generated values, including HTML strings.'};
process.stdout.write(JSON.stringify(report, null, 2) + '\n');

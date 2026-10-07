# Translation bundles

`locales/*.json` contains all 21 complete, canonical translation packs. Each pack
preserves the original 267 values, including HTML. These source files stay outside
the deployment allowlist.

After editing a translation, run from the project root:

```sh
node scripts/build_i18n_bundles.cjs
```

The generator embeds English in `i18n.js` and writes the other 20 packs to
`web/i18n/<language>.<content hash>.json`. It validates generated values against
the source files and prints raw, gzip and Brotli sizes. Content hashes keep cached
translations valid across deployments. The loader template is
`scripts/i18n-bootstrap.template.js`.

Solutions loads only the English bootstrap initially, plus a saved language if
one is selected. Other packs load on selection. Successful loads remain in memory
for repeat selection, concurrent requests for a pack are shared, and stale
responses cannot change the currently selected language. A failed request keeps
English usable and can be retried from the same language menu.

`--import-legacy` is a one-time migration option for the original all-language
`i18n.js`; it is not needed for normal translation updates.

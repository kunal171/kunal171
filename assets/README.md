# Profile artwork

The header and systems-alchemy illustration are original SVGs stored in this
repository. The illustration is decorative; it does not represent contribution
counts, live transactions or measured throughput.

Regenerate all light/dark and mobile/desktop variants with:

```bash
python3 scripts/render-artwork.py
```

The script uses only Python's standard library and writes deterministic output.
SVG CSS handles the orbit, pulse and path motion. Reduced-motion preferences
turn these effects off. Names, labels and paths remain visible without animation.
There are no scripts, external fonts, API requests or scheduled generation jobs.

The README selects variants with `<picture>` so the images work as GitHub-hosted
assets. The old contribution animation workflow is removed; its output branch
is no longer used by the profile. Editing this artwork needs no workflow token.

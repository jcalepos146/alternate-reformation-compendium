# Alternate Reformation Compendium

An encyclopedia and atlas for an alternate history in which Zwingli dies at Marignano in 1515 and the Reformation runs a different course, 1500–1789.

- **Compendium** (`index.html`): pages for every faith, person, monarch, faction, battle and document, with beliefs, structure, cross-links and status badges (canon, historical, proposed).
- **Library**: in-world primary sources and chronicles, and reference handouts generated from the data.
- **Atlas** (`atlas.html`): the interactive map, with snapshots from 1500 to 1635.

Everyone in it is a real person, sometimes in a role history did not give them. Nothing is made up.

## Layout

- `index.html`, `atlas.html` and the map files are the site itself, served by GitHub Pages.
- `source/` is the content (Python modules) and the build: `python3 source/build.py` regenerates `index.html`. Add `--portraits DIR` to include portraits from `tools/portraits`.
- `tools/portraits/` is the portrait downloader. See its README.

## Known gaps

The atlas images and notes were made before the Schmalkaldic rout, the Lambeth formula and the later decisions, and do not yet show them.

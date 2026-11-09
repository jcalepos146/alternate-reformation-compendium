# Alternate Reformation Compendium

An encyclopedia and atlas for an alternate history in which Zwingli dies at Marignano in 1515 and the Reformation runs a different course, 1500–1789.

**[Open the Compendium →](https://jcalepos146.github.io/alternate-reformation-compendium/)** · **[Open the Atlas →](https://jcalepos146.github.io/alternate-reformation-compendium/atlas.html)**

- **[Compendium](https://jcalepos146.github.io/alternate-reformation-compendium/)** (`index.html`): pages for every faith, person, monarch, faction, battle and document, with beliefs, structure, cross-links and status badges (canon, historical, proposed). Jump to [faiths](https://jcalepos146.github.io/alternate-reformation-compendium/#faiths), [leaders](https://jcalepos146.github.io/alternate-reformation-compendium/#leaders), [monarchs](https://jcalepos146.github.io/alternate-reformation-compendium/#monarchs), [battles](https://jcalepos146.github.io/alternate-reformation-compendium/#battles), the [timeline](https://jcalepos146.github.io/alternate-reformation-compendium/#timeline) or [about](https://jcalepos146.github.io/alternate-reformation-compendium/#about).
- **[Library](https://jcalepos146.github.io/alternate-reformation-compendium/#library)**: in-world primary sources and chronicles, and reference handouts generated from the data.
- **[Atlas](https://jcalepos146.github.io/alternate-reformation-compendium/atlas.html)** (`atlas.html`): the interactive map, with snapshots from 1500 to 1635. Link a year directly, e.g. [1550](https://jcalepos146.github.io/alternate-reformation-compendium/atlas.html#1550).

Everyone in it is a real person, sometimes in a role history did not give them. Nothing is made up.

## Layout

- `index.html`, `atlas.html` and the map files are the site itself, served by GitHub Pages.
- `source/` is the content (Python modules) and the build: `python3 source/build.py` regenerates `index.html`. Add `--portraits DIR` to include portraits from `tools/portraits`.
- `tools/portraits/` is the portrait downloader. See its README.

## Known gaps

The atlas images, boundaries and snapshot JSON predate the revised first-century lore. In particular, they do not yet show the prolonged Schmalkaldic War (1546–49), the failed Princes’ Revolt (1552), Augustus’s Gnesio turn in Saxony, or the French foothold at Turin confirmed in 1559. Consult the compendium entries for the revised chronology; the atlas is not evidence for the older outcomes.

The first-century revisions are collected in `source/c_first_century.py`, loaded after the earlier decisions. Exact Piedmontese boundaries, the first joint ordaining ministers at Lambeth, and Saxony’s transition to its later recorded Cranmerian alignment remain open questions.


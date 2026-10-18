# Portrait downloader

Fetches a portrait for every person and head of state in the Alternate Reformation Compendium (279 people), from English Wikipedia and Wikimedia Commons. It uses only the free-licensed images by default and records the artist and licence of each, so the site can credit them.

## Run it

Python 3.8 or later, no packages to install. On your own computer (the sandbox I work in cannot reach Wikimedia):

    python3 fetch_portraits.py --contact you@example.com

`--contact` goes in the User-Agent, as Wikimedia asks of scripts. It takes a few minutes. You get:

- `portraits/` with one image per person, named by site id, plus `credits.json`
- `portraits/report.txt` listing who has no image, whose image is non-free, and any failures
- `portraits.zip` of all of that

Re-running skips people already done. Useful options: `--only calvin,knox`, `--size 600`, `--force`, `--delay 1` if you are rate-limited.

## Fixing the misses

Some people will have no free lead image. Put an override in `overrides.json` next to the script, naming a Commons file, and re-run:

    { "john-cosin": "File:John Cosin.jpg", "menno-simons": "File:Menno Simons.jpg" }

`--allow-nonfree` also fetches non-free images, which is not suitable for publishing.

## Putting them on the site

Send me `portraits.zip`. I will rebuild the site with the images in the facts panel and on each card, and add a credits table to the About page.

`people.json` is generated from the site's data (id, name, Wikipedia title, role). A wrong Wikipedia title shows up in the report, not as a wrong picture.

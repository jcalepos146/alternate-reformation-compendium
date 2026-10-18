#!/usr/bin/env python3
"""Download a portrait for every person in people.json from Wikipedia / Wikimedia Commons.

Standard library only (Python 3.8+). Run it on your own computer: it needs open access to
en.wikipedia.org, commons.wikimedia.org and upload.wikimedia.org.

    python3 fetch_portraits.py --contact you@example.com

Outputs, in ./portraits:
    <id>.jpg (or .png/.webp)   the image
    credits.json               id -> artist, license, source URL (required for attribution)
    report.txt                 people with no image, non-free images skipped, failures
and a portraits.zip next to it that you can upload back to the site project.
"""
import argparse, html, json, os, re, sys, time, urllib.parse, urllib.request, urllib.error, zipfile

EN = "https://en.wikipedia.org/w/api.php"
COMMONS = "https://commons.wikimedia.org/w/api.php"
FREE_PREFIX = ("public domain", "pd", "cc0", "cc by", "cc-by", "cc-zero", "gfdl", "attribution", "free", "no restrictions")
UA = None
DELAY = 0.4


def _request(url, binary=False, tries=6):
    wait = 2.0
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            time.sleep(DELAY)
            return data if binary else json.loads(data.decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                ra = e.headers.get("Retry-After")
                time.sleep(float(ra) if ra and ra.replace(".", "").isdigit() else wait)
                wait *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < tries - 1:
                time.sleep(wait); wait *= 2; continue
            raise


def api_get(endpoint, params):
    p = dict(params, format="json", formatversion="2")
    return _request(endpoint + "?" + urllib.parse.urlencode(p))


def download(url):
    return _request(url, binary=True)


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def lead_images(titles, size):
    """Wikipedia title -> {'file': 'Name.jpg', 'page': canonical title} (or {} if none)."""
    out = {}
    for batch in chunks(titles, 40):
        d = api_get(EN, dict(action="query", prop="pageimages|pageprops", piprop="name", ppprop="disambiguation",
                             redirects="1", titles="|".join(batch)))
        q = d.get("query", {})
        back = {}
        for n in q.get("normalized", []): back[n["to"]] = n["from"]
        for r in q.get("redirects", []): back[r["to"]] = back.get(r["from"], r["from"])
        for pg in q.get("pages", []):
            req = back.get(pg["title"], pg["title"])
            if "missing" in pg:
                out[req] = {"error": "page not found"}
            elif "pageprops" in pg and "disambiguation" in pg["pageprops"]:
                out[req] = {"error": "disambiguation page", "page": pg["title"]}
            elif pg.get("pageimage"):
                out[req] = {"file": pg["pageimage"], "page": pg["title"]}
            else:
                out[req] = {"error": "page has no lead image", "page": pg["title"]}
    return out


def clean(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def image_info(files, size):
    """File name -> info from Commons. Missing files (e.g. local non-free uploads) are absent."""
    out = {}
    for batch in chunks(files, 40):
        titles = "|".join("File:" + f.replace("_", " ") for f in batch)
        d = api_get(COMMONS, dict(action="query", prop="imageinfo", iiprop="url|mime|extmetadata", iiurlwidth=str(size),
                                  titles=titles))
        q = d.get("query", {})
        back = {}
        for n in q.get("normalized", []): back[n["to"]] = n["from"]
        for pg in q.get("pages", []):
            ii = pg.get("imageinfo")
            if not ii or pg.get("missing"):
                continue
            ii = ii[0]; em = ii.get("extmetadata", {})
            val = lambda k: clean(em.get(k, {}).get("value", ""))
            name = back.get(pg["title"], pg["title"])[5:].replace(" ", "_")
            out[name] = dict(
                url=ii.get("thumburl") or ii["url"], mime=ii.get("mime", ""), title=pg["title"],
                artist=val("Artist"), license=val("LicenseShortName"), license_url=val("LicenseUrl"),
                copyrighted=val("Copyrighted"), source_url=ii.get("descriptionurl", ""),
            )
    return out


def is_free(info):
    if info["copyrighted"].lower() == "false":
        return True
    lic = info["license"].lower()
    return lic.startswith(FREE_PREFIX)


def ext_for(mime, url):
    m = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp", "image/gif": "gif"}.get(mime)
    return m or os.path.splitext(urllib.parse.urlparse(url).path)[1].lstrip(".").lower() or "jpg"


def run(args):
    global UA, DELAY
    UA = "AlternateReformationPortraits/1.0 (%s; personal research project)" % args.contact
    DELAY = args.delay
    people = json.load(open(args.manifest, encoding="utf-8"))
    if args.only:
        want = set(args.only.split(","))
        people = [p for p in people if p["id"] in want]
    over = json.load(open(args.overrides, encoding="utf-8")) if args.overrides and os.path.exists(args.overrides) else {}
    os.makedirs(args.out, exist_ok=True)
    cpath = os.path.join(args.out, "credits.json")
    credits = json.load(open(cpath, encoding="utf-8")) if os.path.exists(cpath) else {}

    todo = []
    for p in people:
        c = credits.get(p["id"])
        if c and os.path.exists(os.path.join(args.out, c["file"])) and not args.force:
            continue
        todo.append(p)
    print("%d people, %d already done, %d to fetch" % (len(people), len(people) - len(todo), len(todo)))

    report = {"no_page": [], "no_image": [], "nonfree": [], "not_on_commons": [], "failed": []}
    lead = lead_images(sorted({p["wiki"] for p in todo}), args.size)
    chosen = {}  # id -> file name on Commons
    for p in todo:
        if p["id"] in over:
            chosen[p["id"]] = over[p["id"]].replace("File:", "").replace(" ", "_"); continue
        r = lead.get(p["wiki"], {"error": "page not found"})
        if "file" in r:
            chosen[p["id"]] = r["file"].replace(" ", "_")
        elif r["error"] == "page not found" or r["error"] == "disambiguation page":
            report["no_page"].append("%s (%s): %s" % (p["id"], p["wiki"], r["error"]))
        else:
            report["no_image"].append("%s (%s)" % (p["id"], p["wiki"]))
    infos = image_info(sorted(set(chosen.values())), args.size)

    for p in todo:
        f = chosen.get(p["id"])
        if not f: continue
        info = infos.get(f)
        if not info:
            if args.allow_nonfree:
                report["failed"].append("%s: %s is not on Commons; fetch it by hand" % (p["id"], f))
            else:
                report["not_on_commons"].append("%s: %s (a local, probably non-free, Wikipedia upload)" % (p["id"], f))
            continue
        if not is_free(info) and not args.allow_nonfree:
            report["nonfree"].append("%s: %s [%s]" % (p["id"], f, info["license"] or "unknown license"))
            continue
        try:
            data = download(info["url"])
            fn = "%s.%s" % (p["id"], ext_for(info["mime"], info["url"]))
            with open(os.path.join(args.out, fn), "wb") as fh: fh.write(data)
            credits[p["id"]] = dict(file=fn, title=info["title"], artist=info["artist"], license=info["license"],
                                    license_url=info["license_url"], source_url=info["source_url"])
            json.dump(credits, open(cpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("ok   %-28s %s" % (p["id"], f))
        except Exception as e:  # keep going; the report lists it
            report["failed"].append("%s: %s (%s)" % (p["id"], f, e))
            print("FAIL %-28s %s" % (p["id"], e))

    with open(os.path.join(args.out, "report.txt"), "w", encoding="utf-8") as fh:
        for k, v in report.items():
            fh.write("== %s (%d)\n" % (k, len(v)) + "".join("  %s\n" % x for x in v))
    zpath = args.zip
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_STORED) as z:
        for n in sorted(os.listdir(args.out)):
            z.write(os.path.join(args.out, n), "portraits/" + n)
    total = sum(1 for p in people if p["id"] in credits)
    print("\n%d of %d have portraits. Wrote %s and %s." % (total, len(people), os.path.join(args.out, "report.txt"), zpath))
    for k, v in report.items():
        if v: print("  %-15s %d" % (k, len(v)))
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--contact", required=True, help="your email or URL; Wikimedia asks scripts to identify themselves")
    ap.add_argument("--manifest", default="people.json")
    ap.add_argument("--out", default="portraits")
    ap.add_argument("--zip", default="portraits.zip")
    ap.add_argument("--size", type=int, default=480, help="image width in pixels (default 480)")
    ap.add_argument("--overrides", default="overrides.json", help='optional JSON {"id": "File:Name.jpg"} to force an image')
    ap.add_argument("--only", help="comma-separated ids to fetch")
    ap.add_argument("--allow-nonfree", action="store_true", help="also fetch images under non-free licenses (not recommended for publishing)")
    ap.add_argument("--force", action="store_true", help="re-download even if already present")
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    return run(ap.parse_args(argv))


if __name__ == "__main__":
    main()

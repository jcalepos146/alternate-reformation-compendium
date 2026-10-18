import json, os, shutil, tempfile, zipfile
import fetch_portraits as fp

def fake_api(ep, params):
    if ep == fp.EN:
        titles = params["titles"].split("|")
        pages, redirects = [], []
        for t in titles:
            if t == "Nobody Here": pages.append({"title": t, "missing": True})
            elif t == "Pope Julius II": pages.append({"title": t, "pageimage": "Julius_II.jpg"})
            elif t == "Old Name": redirects.append({"from": t, "to": "New Name"}); pages.append({"title": "New Name", "pageimage": "Newbie.png"})
            elif t == "Mid Man": pages.append({"title": t, "pageimage": "Local_nonfree.jpg"})
            elif t == "Imageless": pages.append({"title": t})
            else: pages.append({"title": t, "pageimage": "Free_%s.jpg" % t.replace(" ", "_")})
        return {"query": {"pages": pages, "redirects": redirects}}
    titles = params["titles"].split("|")
    pages = []
    for t in titles:
        n = t[5:].replace(" ", "_")
        if n == "Local_nonfree.jpg": pages.append({"title": t, "missing": True}); continue
        lic = "CC BY-SA 4.0" if n == "Newbie.png" else ("All rights reserved" if n == "Restricted.jpg" else "Public domain")
        pages.append({"title": t, "imageinfo": [{"url": "http://x/" + n, "thumburl": "http://x/t/" + n,
            "mime": "image/png" if n.endswith("png") else "image/jpeg", "descriptionurl": "http://c/" + n,
            "extmetadata": {"Artist": {"value": "<a href='#'>Some &amp; Painter</a>"}, "LicenseShortName": {"value": lic},
                            "LicenseUrl": {"value": ""}, "Copyrighted": {"value": "False" if lic == "Public domain" else "True"}}}]})
    return {"query": {"pages": pages}}

fp.api_get = fake_api
fp.download = lambda url: b"IMG:" + url.encode()
d = tempfile.mkdtemp()
manifest = [dict(id=i, name=i, wiki=w, role="leader", kind="person", when="") for i, w in
            [("julius", "Pope Julius II"), ("old", "Old Name"), ("ghost", "Nobody Here"), ("mid", "Mid Man"), ("blank", "Imageless"), ("plain", "Plain Joe")]]
json.dump(manifest, open(d + "/people.json", "w"))
rep = fp.main(["--contact", "t@example.com", "--manifest", d + "/people.json", "--out", d + "/p", "--zip", d + "/p.zip", "--delay", "0"])
cr = json.load(open(d + "/p/credits.json"))
assert set(cr) == {"julius", "old", "plain"}, cr
assert cr["old"]["file"] == "old.png" and cr["old"]["license"] == "CC BY-SA 4.0"
assert cr["julius"]["artist"] == "Some & Painter"
assert len(rep["no_page"]) == 1 and len(rep["no_image"]) == 1 and len(rep["not_on_commons"]) == 1
assert "portraits/credits.json" in zipfile.ZipFile(d + "/p.zip").namelist()
rep2 = fp.main(["--contact", "t@example.com", "--manifest", d + "/people.json", "--out", d + "/p", "--zip", d + "/p.zip", "--delay", "0"])
print("resume ok; offline tests pass")

import json, re, sys, importlib, os
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from common import ENT

for m in ("c_faiths", "c_people", "c_monarchs", "c_factions", "c_battles", "c_docs", "c_people_a", "c_people_b", "c_people_c", "c_monarchs_b", "c_battles_b", "c_docs_b", "c_people_d", "c_decisions", "c_first_century", "c_library"):
    importlib.import_module(m)

FAMILIES = [
    ["Roman communion and its unions", ["roman-catholic", "gallican-church", "utraquist-rite", "ruthenian-uniate"]],
    ["Gnesio-Catholic", ["gnesio-catholic"]],
    ["Cranmerian and Reformed", ["cranmerian", "byzantinists", "unity-brethren", "hardline-reformed", "evangelical-unaligned"]],
    ["Radical and antitrinitarian", ["anabaptist", "unitarian", "polish-brethren"]],
    ["Orthodox and Eastern Christians", ["eastern-orthodox", "russian-orthodox", "western-rite-orthodox", "miaphysite", "church-east", "maronite"]],
    ["Islam, Judaism and other traditions", ["sunni", "shia", "ibadi", "judaism", "traditional-religions"]],
]
# For the leaders page the Gnesio branches group under their own headings
LEADER_FAMILIES = [[n, ids] for n, ids in FAMILIES]
LEADER_FAMILIES[1] = ["Gnesio-Catholic", ["gnesio-catholic", "gnesio-independent", "gnesio-lyon", "gnesio-orthodox"]]

import meta
for e in ENT:
    if e["id"] in meta.WIKI and not e.get("wiki"): e["wiki"] = meta.WIKI[e["id"]]
    if e["t"] == "person" and not e.get("role"): e["role"] = meta.ROLE.get(e["id"], "leader")
import c_faith_detail
for fid, d in c_faith_detail.DETAIL.items():
    for e in ENT:
        if e["id"] == fid:
            e["beliefs"], e["structure"], e["theologians"] = d.get("beliefs", []), d.get("structure", []), d.get("theologians", [])
    else:
        pass
importlib.import_module("c_handouts")
RESERVED = {"library", "faiths", "leaders", "factions", "battles", "monarchs", "documents", "timeline", "about"}
ids = [e["id"] for e in ENT]
errors = []
dupes = {i for i in ids if ids.count(i) > 1}
if dupes: errors.append("duplicate ids: %s" % dupes)
byid = {e["id"]: e for e in ENT}
for e in ENT:
    if e["id"] in RESERVED: errors.append("reserved id " + e["id"])
    if not re.fullmatch(r"[a-z0-9-]+", e["id"]): errors.append("bad id " + e["id"])
    if e["st"] not in ("canon", "hist", "prop"): errors.append("bad status " + e["id"])
    for f in e["faith"]:
        if f not in byid or byid[f]["t"] != "faith": errors.append("%s: bad faith %s" % (e["id"], f))
    if e["branch_of"] and e["branch_of"] not in byid: errors.append("%s: bad branch_of" % e["id"])
    for r in e["rel"]:
        if r[0] not in byid: errors.append("%s: bad rel target %s" % (e["id"], r[0]))
    blob = " ".join([e["sum"]] + e["body"] + [r[1] for r in e["rel"]] + e["open_q"])
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", blob):
        if m.group(1) not in byid: errors.append("%s: dead link [[%s]]" % (e["id"], m.group(1)))
placed = {i for _, g in FAMILIES for i in g}
for e in ENT:
    if e["t"] == "faith" and not e["branch_of"] and e["id"] not in placed: errors.append("faith not in a family: " + e["id"])
for e in ENT:
    if e["t"] in ("person", "monarch") and not e.get("wiki"): errors.append("no wiki title: " + e["id"])
for fid, d in c_faith_detail.DETAIL.items():
    if fid not in byid or byid[fid]["t"] != "faith": errors.append("detail for non-faith " + fid)
    for t in d.get("theologians", []):
        if t not in byid or byid[t]["t"] not in ("person", "monarch"): errors.append("%s: bad theologian %s" % (fid, t))
    for _, txt in d.get("beliefs", []) + [(0, x) for x in d.get("structure", [])]:
        for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", txt):
            if m.group(1) not in byid: errors.append("%s detail: dead link %s" % (fid, m.group(1)))
for e in ENT:
    if e["t"] == "faith" and e["id"] not in c_faith_detail.DETAIL and not e["branch_of"]: errors.append("no detail for faith " + e["id"])
if errors:
    print("\n".join(errors)); sys.exit(1)

# portraits (optional) and the manifest for the downloader app
import os, argparse
ap = argparse.ArgumentParser(); ap.add_argument("--portraits"); ap.add_argument("--out", default=os.path.join(BASE, "..", "index.html"))
args = ap.parse_args()
credits = []
if args.portraits:
    cj = os.path.join(args.portraits, "credits.json")
    cr = json.load(open(cj, encoding="utf-8")) if os.path.exists(cj) else {}
    for e in ENT:
        c = cr.get(e["id"])
        if e["t"] in ("person", "monarch") and c and os.path.exists(os.path.join(args.portraits, c["file"])):
            e["img"] = "portraits/" + c["file"]
            credits.append(dict(c, name=e["name"]))
manifest = [dict(id=e["id"], name=e["name"], wiki=e["wiki"], role=e.get("role") or "monarch", kind=e["t"], when=e["when"])
            for e in ENT if e["t"] in ("person", "monarch")]
json.dump(manifest, open(os.path.join(BASE, "people.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# the leaders page needs branch grouping; ship both lists
meta = {"families": FAMILIES, "leader_families": LEADER_FAMILIES, "credits": credits}
payload = json.dumps({"meta": meta, "entities": ENT}, ensure_ascii=False).replace("</", "<\\/")
tpl = open(os.path.join(BASE, "template.html"), encoding="utf-8").read()
out = tpl.replace("/*DATA*/", payload)
open(args.out, "w", encoding="utf-8").write(out)
from collections import Counter
print("ok", len(ENT), dict(Counter(e["t"] for e in ENT)), dict(Counter(e["st"] for e in ENT)), len(out) // 1024, "KB")


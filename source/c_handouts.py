"""Reference handouts, generated from the entity data so they never drift from it."""
import re
from common import ENT, E

_by = {e["id"]: e for e in ENT}
NOTE = "Generated from the compendium's entries, so it matches them. Statuses: canon, historical, proposed."
ST = {"canon": "Canon", "hist": "Historical", "prop": "Proposed"}
TY = {"battle": "Battle", "doc": "Council or document", "monarch": "Ruler", "faction": "Faction", "person": "Person", "faith": "Faith", "text": "Library"}


def link(e): return "[[%s|%s]]" % (e["id"], e["name"])


def H(id, name, when, sum, head, rows, body=None):
    E(id, "text", name, "canon", when, 1500, sum, [NOTE] + (body or []),
      facts=[["Kind", "Reference handout"], ["Rows", str(len(rows))]], table=[head, rows], basis="Generated from the data.")


# timeline of events
ev = sorted([e for e in ENT if e["t"] in ("battle", "doc") and e["y"] <= 1700], key=lambda e: (e["y"], e["name"]))
H("hand-timeline", "Timeline of battles, councils and documents, 1500–1700", "1500–1700",
  "Every battle, council, treaty and document in the compendium, in order.",
  ["Year", "Event", "Kind", "Status"], [[str(e["y"]), link(e), TY[e["t"]], ST[e["st"]]] for e in ev])

# battles register
bt = sorted([e for e in ENT if e["t"] == "battle"], key=lambda e: (e["y"], e["name"]))
def fv(e, k):
    for r in e["facts"]:
        if r[0] == k: return r[1]
    return ""
H("hand-battles", "Register of battles and wars", "1500–1700",
  "Date, place, sides and result for every battle and war.",
  ["Battle", "Date", "Place", "Sides", "Result", "Status"],
  [[link(e), fv(e, "Date"), fv(e, "Place"), fv(e, "Sides"), fv(e, "Result"), ST[e["st"]]] for e in bt])

# rulers
mo = sorted([e for e in ENT if e["t"] == "monarch"], key=lambda e: (e["y"], e["name"]))
H("hand-rulers", "Rulers and their faiths", "1500–1700", "Every head of state in the compendium with their office and community.",
  ["Ruler", "Office", "Reign", "Community", "Status"],
  [[link(e), e.get("office") or "", e["when"], ", ".join(_by[f]["name"] for f in e["faith"] if f in _by), ST[e["st"]]] for e in mo])

# who's who by faith
rows = []
for f in sorted([e for e in ENT if e["t"] == "faith" and not e["branch_of"]], key=lambda e: e["name"]):
    ids = [f["id"]] + [x["id"] for x in ENT if x.get("branch_of") == f["id"]]
    ppl = sorted([e for e in ENT if e["t"] == "person" and e["faith"] and e["faith"][0] in ids], key=lambda e: e["y"])
    if ppl: rows.append([link(f), ", ".join(link(p) for p in ppl)])
H("hand-who", "Who's who by community", "1500–1700", "Every person in the compendium under the community they belong to.",
  ["Community", "People"], rows)

# faith comparison
def first_sentence(t):
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return m.group(1) if m else t
fr = []
for f in ENT:
    if f["t"] == "faith" and f["beliefs"]:
        fr.append([link(f), "%s: %s" % (f["beliefs"][0][0], first_sentence(f["beliefs"][0][1])),
                   first_sentence(f["structure"][0]) if f["structure"] else ""])
H("hand-faiths", "Comparison of the faiths", "1500–1700",
  "Each community's leading belief and its form of governance, side by side.",
  ["Community", "Leading belief", "Governance"], fr)

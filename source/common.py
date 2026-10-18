"""Shared entity constructor for the Alternate Reformation encyclopedia.

Types: faith, person, monarch, faction, battle, doc
Person roles: leader, theologian, general, statesman, artist, scholar
Status: canon (settled in the map project), hist (real history carried over), prop (proposed here, needs approval)
Every person and monarch is a real historical figure, used in a possibly different context. Nobody is invented.
Text fields may contain [[id]] or [[id|label]] cross-links; the build checks that each id exists.
"""

ENT = []

R = "Real person, in the role history gave them."
RH = "Real person in a hypothetical role."


def E(id, t, name, st, when, y, sum, body, facts=None, faith=None, office=None, rel=None,
      y2=None, color=None, basis=None, open_q=None, branch_of=None, role=None, wiki=None):
    ENT.append(dict(
        id=id, t=t, name=name, st=st, when=when, y=y, y2=y2, sum=sum,
        body=body if isinstance(body, list) else [body],
        facts=facts or [], faith=faith or [], office=office, rel=rel or [],
        color=color, basis=basis, open_q=open_q or [], branch_of=branch_of,
        role=role, wiki=wiki,
        beliefs=[], structure=[], theologians=[],
    ))


def P(id, name, role, st, when, y, sum, body, faith, office, wiki, basis=None, open_q=None, y2=None, rel=None):
    """A real person. st=hist keeps history's role; st=prop puts them in a hypothetical one."""
    E(id, "person", name, st, when, y, sum, body, faith=faith, office=office, role=role, wiki=wiki,
      basis=basis or (RH if st == "prop" else R), open_q=open_q, y2=y2, rel=rel)


def M(id, name, st, when, y, sum, body, faith, office, wiki, basis=None, open_q=None, y2=None):
    """A real head of state."""
    E(id, "monarch", name, st, when, y, sum, body, faith=faith, office=office, wiki=wiki,
      basis=basis or (RH if st == "prop" else R), open_q=open_q, y2=y2)

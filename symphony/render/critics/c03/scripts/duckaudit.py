#!/usr/bin/env python3
"""Critic 3: audit of r03's mix-stage balance (lib/balance.py gain curves *_gain.npy in the render's stems folder).
Usage: duckaudit.py WORK label
Per stem: bars cut >= 3 / >= 6 dB, bars lifted; max gain slope (dB per second, from the smoothed curve);
printed-dynamic conflicts: a stem cut >= 3 dB in a bar where its own printed dynamic is >= the melody's printed
dynamic (the score asks it to be at least as loud), with the step difference; marked melodies that are CUT."""
import sys, os, csv, json, re, glob, numpy as np
from collections import defaultdict
sys.path.insert(0, "/mnt/project-files/symphony/render/tools"); import rtk
W, lab = sys.argv[1:3]
DY = ['ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff']
def key(n):
    k = re.sub(r"[^A-Za-z0-9 ]", "", n.split(":")[0]).strip(); return k or "drums"
mi = rtk.midi_info(os.path.join(W, "score.midi"))
bars = [(b["bar"], b["t_start"], b["t_end"]) for b in mi["per_bar"]]
rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
pd = defaultdict(dict)
for r in rows:
    if r["dyn"] in DY:
        st = key(r["midi_track"]) if r.get("midi_track") else key(r["staff"]); b = int(r["bar"])
        pd[st][b] = max(pd[st].get(b, 0), DY.index(r["dyn"]))
rep = json.load(open(os.path.join(W, "balance_report.json")))
mel_at = defaultdict(set)
for st, b0, b1, txt in rep["derived_melodies"]:
    for b in range(b0, b1 + 1): mel_at[b].add(st)
G = {}
for p in glob.glob(os.path.join(W, "stems", "*_gain.npy")):
    st = os.path.basename(p)[:-9].replace("_", " ")
    t, g = np.load(p); G[st] = (t, g)
print(f"{lab}: stems with a gain curve: {len(G)}")
print("stem | bars cut>=3 | cut>=6 | lifted>=1 | min/max dB | max slope dB/s | cut>=3 where own printed dyn >= melody's (n; max steps above)")
tot3 = tot6 = conf = 0; confl = []
for st, (t, g) in sorted(G.items()):
    slope = np.max(np.abs(np.diff(g))) / (t[1] - t[0])
    bg = {}
    for b, a, e in bars:
        m = (t >= a) & (t < e)
        if m.any(): bg[b] = float(np.median(g[m]))
    c3 = [b for b, v in bg.items() if v <= -3]; c6 = [b for b, v in bg.items() if v <= -6]; l1 = [b for b, v in bg.items() if v >= 1]
    cf = []
    for b in c3:
        if st in mel_at[b] or st not in pd or b not in pd[st]: continue
        md = [pd[m].get(b) for m in mel_at[b] if pd[m].get(b) is not None]
        if md and pd[st][b] >= max(md):
            cf.append((b, pd[st][b] - max(md), DY[pd[st][b]], DY[max(md)], round(bg[b], 1)))
    tot3 += len(c3); tot6 += len(c6); conf += len(cf); confl += [(st,) + c for c in cf]
    print(f"{st} | {len(c3)} | {len(c6)} | {len(l1)} | {g.min():+.1f}/{g.max():+.1f} | {slope:.1f} | {len(cf)}; {max([c[1] for c in cf], default='-')}")
print(f"{lab}: stem-bars cut >= 3 dB: {tot3}, >= 6 dB: {tot6}; cut >= 3 dB although printed >= the melody: {conf}")
for c in sorted(confl, key=lambda z: -z[2])[:25]:
    print("  ", c)
mc = [(m["staff"], m["bars"], m["lift_dB"]) for m in rep["melodies"] if m["lift_dB"] < -0.4]
print(f"{lab}: marked melodies whose median gain is a CUT: {mc}")

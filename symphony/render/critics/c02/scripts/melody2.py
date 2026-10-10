#!/usr/bin/env python3
"""Critic 2 (series 2): marked melodies derived from the score's own text marks (no hand-made bar list).
Usage: melody2.py events.tsv notes.csv stem_bars.csv midi config.json  -> markdown table on stdout
Marks: text scripts containing espr / dolce / cantabile / solo (LilyPond event log). Phrase = from the bar of the
first note at/after the mark while the staff has notes in consecutive bars, at most 8 bars (critic 1's rule).
For each phrase: melody stem level minus loudest other stem and minus power sum of the others (harp, drums out),
median over bars; plus whether config.melodies lifts that staff in those bars (as the r02 list is bar-number based)."""
import csv, re, sys, json
from collections import defaultdict
import numpy as np, mido
ev, notes, sb, midi, cfgp = sys.argv[1:6]
def key(n):
    k = re.sub(r"[^A-Za-z0-9 ]", "", n.split(":")[0]).strip(); return k or "drums"
tpb = mido.MidiFile(midi).ticks_per_beat; whole = 4 * tpb
rows = list(csv.DictReader(open(notes)))
by_staff = defaultdict(list); bars_with = defaultdict(set)
for r in rows:
    st = key(r["staff"]); by_staff[st].append((int(r["tick_on"]), int(r["bar"]))); bars_with[st].add(int(r["bar"]))
for st in by_staff: by_staff[st].sort()
marks = []
for line in open(ev, encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if len(f) < 8 or not f[7].startswith("text:"): continue
    txt = f[7][5:]
    if not re.search(r"espr|dolce|cantabile|solo", txt, re.I): continue
    st = key(f[1]); mom = float(f[3]); tk = mom * whole
    nb = [b for t, b in by_staff.get(st, []) if t >= tk - 1]
    if not nb: continue
    marks.append((st, nb[0], txt))
md = {}
for st, b, txt in marks:
    md.setdefault((st, b), []).append(txt)
marks = sorted(((st, b, " / ".join(dict.fromkeys(t))) for (st, b), t in md.items()), key=lambda z: (z[1], z[0]))
B = defaultdict(dict)
for r in csv.DictReader(open(sb)):
    if r["loud_LUFS"] in ("", "nan"): continue
    B[int(r["bar"])][r["stem"]] = (float(r["loud_LUFS"]), r["dyn"])
cfg = json.load(open(cfgp)); lifted = defaultdict(dict)
M = cfg.get("melodies", {})
for it in M.get("list", []):
    st, b0 = it[0], it[1]; db = it[3] if len(it) > 3 else M.get("lift_dB", 3)
    b = b0; n = 0
    while b in bars_with[st] and n < M.get("max_bars", 8):
        lifted[st][b] = db; b += 1; n += 1
print("| melody (mark) | bars | dyn | vs loudest other (median dB) | vs sum of others | loudest other | r02 lift in these bars |")
print("|---|---|---|---|---|---|---|")
res = []
for st, b0, txt in marks:
    bs = []; b = b0
    while b in bars_with[st] and len(bs) < 8: bs.append(b); b += 1
    dm, ds, who = [], [], []
    for b in bs:
        if st not in B[b]: continue
        m = B[b][st][0]
        oth = {k: v for k, v in B[b].items() if k != st and not k.startswith("Harp") and k != "drums"}
        if not oth: continue
        k2 = max(oth, key=lambda k: oth[k][0]); dm.append(m - oth[k2][0]); who.append(f"{k2} ({oth[k2][1]})")
        ds.append(m - 10 * np.log10(sum(10 ** (v[0] / 10) for v in oth.values())))
    lift = [lifted[st].get(b) for b in bs]
    nl = sum(1 for x in lift if x)
    lifttxt = "none" if nl == 0 else f"{nl}/{len(bs)} bars, {max(x for x in lift if x):.1f} dB"
    # lifts in bars where this staff is NOT under a mark
    if dm:
        res.append((st, b0, np.median(dm), np.median(ds)))
        print(f"| {st} ({txt}) | {bs[0]}-{bs[-1]} | {B[bs[0]].get(st,(0,''))[1]} | {np.median(dm):+.1f} | {np.median(ds):+.1f} | {max(set(who), key=who.count)} | {lifttxt} |")
marked = defaultdict(set)
for st, b0, txt in marks:
    b = b0; n = 0
    while b in bars_with[st] and n < 8: marked[st].add(b); b += 1; n += 1
stray = {st: sorted(b for b in d if b not in marked[st]) for st, d in lifted.items()}
stray = {k: v for k, v in stray.items() if v}
print()
n0 = sum(1 for r in res if r[2] >= 0); n6 = sum(1 for r in res if r[3] >= -6)
print(f"marked melodies: {len(res)}; >= 0 dB vs loudest other: {n0}; >= -6 dB vs sum: {n6}; median vs loudest {np.median([r[2] for r in res]):+.1f} dB")
print("config lifts in bars with no printed melody mark for that staff:", json.dumps(stray))

#!/usr/bin/env python3
"""critic 4: marked melodies against the other stems, counted (a) over the whole marked phrase (as melody2.py) and
(b) only over the bars the balance stage treats as the phrase (bars before the phrase meets a printed f/ff tutti,
balance_report.json 'balanced_phrases'); harp and percussion left out, stem levels while sounding (stem_bars.csv).
Usage: melody_nt.py WORK stem_bars.csv label"""
import sys, os, json, csv, numpy as np
from collections import defaultdict
W, sb, lab = sys.argv[1:4]
rep = json.load(open(os.path.join(W, "balance_report.json")))
L = defaultdict(dict)
for r in csv.DictReader(open(sb)):
    try: L[int(r["bar"])][r["stem"]] = float(r["loud_LUFS"])
    except ValueError: pass
bp = {(s, a): (a, b) for s, a, b in rep["balanced_phrases"]}
mel_at = defaultdict(set)
for s, a, b, _ in rep["derived_melodies"]:
    for x in range(a, b + 1): mel_at[x].add(s)
def stat(s, bars):
    lo, sm = [], []
    for x in bars:
        if s not in L[x]: continue
        o = {k: v for k, v in L[x].items() if k != s and not k.startswith(("Harp", "drums"))}
        if not o: continue
        lo.append(L[x][s] - max(o.values()))
        sm.append(L[x][s] - 10 * np.log10(sum(10 ** (v / 10) for v in o.values())))
    return (np.median(lo), np.median(sm)) if lo else (np.nan, np.nan)
n1 = n2 = m1 = m2 = k = 0
print(f"{lab}: melody | marked bars | whole phrase: vs loudest / vs sum | balanced bars | balanced: vs loudest / vs sum")
for s, a, b, txt in rep["derived_melodies"]:
    w = stat(s, range(a, b + 1)); pb = bp.get((s, a))
    q = stat(s, range(pb[0], pb[1] + 1)) if pb else (np.nan, np.nan)
    print(f"{s} ({txt}) | {a}-{b} | {w[0]:+.1f} / {w[1]:+.1f} | {pb[0] if pb else '-'}-{pb[1] if pb else '-'} | {q[0]:+.1f} / {q[1]:+.1f}")
    n1 += w[0] >= 0; m1 += w[1] >= -6
    if pb: k += 1; n2 += q[0] >= 0; m2 += q[1] >= -6
print(f"{lab}: whole phrase: >= 0 dB vs loudest {n1}/{len(rep['derived_melodies'])}, >= -6 vs sum {m1}; balanced bars only ({k} phrases): {n2}/{k}, {m2}/{k}")

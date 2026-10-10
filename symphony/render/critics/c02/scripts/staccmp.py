#!/usr/bin/env python3
"""Staccato against unmarked detached notes of the same notated length (+-25 %) in the same stem: peak (first 120 ms,
K-free RMS in 10 ms frames, dB re stem) and level 250 ms after the onset relative to the note's own peak. Only notes with
no other onset of the stem in the 300 ms after the onset (so the decay is the note's own). Usage: staccmp.py notes.csv stems_dir label"""
import csv, sys, os, re, numpy as np, soundfile as sf
from collections import defaultdict
nf, d, lab = sys.argv[1:4]
def key(n): return re.sub(r"[^A-Za-z0-9 ]", "", n.split(":")[0]).strip()
rows = list(csv.DictReader(open(nf, encoding="utf-8")))
ons = defaultdict(list)
for r in rows: ons[key(r["staff"])].append(float(r["t_on_s"]))
for k in ons: ons[k] = np.array(sorted(set(ons[k])))
by = defaultdict(lambda: {"st": [], "det": []})
for r in rows:
    st = key(r["staff"]); arts = r["arts"].split("|") if r["arts"] else []
    t = float(r["t_on_s"]); o = ons[st]
    if ((o > t + 1e-3) & (o < t + 0.3)).any(): continue
    if "staccato" in arts: by[st]["st"].append((t, float(r["notated_s"])))
    elif not arts and r["slur"] == "" and r["tech"] == "": by[st]["det"].append((t, float(r["notated_s"])))
print(f"{lab}: stem | n stacc / n detached same length | peak stacc minus detached dB | level at +250 ms re own peak: stacc / detached dB")
for st, v in sorted(by.items()):
    if len(v["st"]) < 3: continue
    p = os.path.join(d, st.replace(" ", "_") + ".wav")
    if not os.path.exists(p): continue
    x, sr = sf.read(p, dtype="float64", always_2d=True); x = x.mean(1); h = int(0.01 * sr)
    def m(t):
        a = int(t * sr); seg = x[a:a + int(0.4 * sr)]; n = len(seg) // h
        e = 10 * np.log10((seg[:n * h].reshape(n, h) ** 2).mean(1) + 1e-20)
        return e[:12].max(), e[25] - e[:12].max()
    Ls = np.median([L for t, L in v["st"]])
    det = [(t, L) for t, L in v["det"] if 0.75 * Ls <= L <= 1.25 * Ls]
    if len(det) < 3: continue
    S = np.array([m(t) for t, L in v["st"]]); D = np.array([m(t) for t, L in det])
    print(f"  {st} | {len(S)} / {len(D)} (notated {Ls:.2f} s) | {np.median(S[:,0]) - np.median(D[:,0]):+.1f} | {np.median(S[:,1]):+.1f} / {np.median(D[:,1]):+.1f}")

#!/usr/bin/env python3
"""r07: every timpani roll longer than a bar, written as one note or as a chain of untied notes (lib/marks.roll_chains):
per bar, the timpani's whole-bar loudness minus the loudest other stem (while sounding, else whole bar), on the placed
stems of a render work folder (critic 6's 'timp minus loudest other' table), plus the roll's printed dynamics.
Usage: rollcheck.py WORK [LIB_DIR]"""
import sys, os, csv, glob
import numpy as np, soundfile as sf
W = sys.argv[1]
LIB = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "lib")
sys.path.insert(0, LIB)
import marks, balance, rtk
rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
mi = rtk.midi_info(os.path.join(W, "score.midi"))
bars = [(b["bar"], b["t_start"], b["t_end"]) for b in mi["per_bar"]]
by = {}
for r in rows:
    by.setdefault(balance.key(r["midi_track"]) if r["midi_track"] else balance.key(r["staff"]), []).append(r)
lv, wh = {}, {}
for p in sorted(glob.glob(os.path.join(W, "stems", "*.wav"))):
    if p.endswith("_syn.wav"):
        continue
    nm = os.path.basename(p)[:-4]
    st = [k for k in by if k.replace(" ", "_") == nm]
    if not st:
        continue
    x, sr = sf.read(p, dtype="float64", always_2d=True)
    lv[st[0]], wh[st[0]] = balance.bar_levels(x, sr, by[st[0]], bars)
timp = [k for k in lv if k.startswith("Timp")][0]
pdyn = balance.printed_dyn(rows)
allv = []
for t0, t1, bs, dyn, hp in marks.rolls(rows, mi["bar_s"], tpb=mi["tpb"]):
    out = []
    for b in bs:
        m = wh[timp].get(b)
        o = [(lv[s].get(b) if lv[s].get(b) is not None else wh[s].get(b), s) for s in lv if s not in (timp, "drums")]
        o = [z for z in o if z[0] is not None and np.isfinite(z[0]) and z[0] > -90]
        if m is None or not o:
            continue
        mo, so = max(o)
        tp = pdyn.get(timp, {}).get(b); op = pdyn.get(so, {}).get(b)
        out.append(f"{b}:{m - mo:+.1f}({so[:6]} {balance.DY[op] if op is not None else '-'}/{balance.DY[tp] if tp is not None else '-'})")
        allv.append(m - mo)
    print(f"roll {bs[0]}-{bs[-1]} {dyn}{'/'+hp if hp else ''} {t1 - t0:.1f}s: " + " ".join(out))
print(f"bars: {len(allv)}, timpani loudest (>0 dB): {sum(v > 0 for v in allv)}, within 1 dB (>-1): {sum(v > -1 for v in allv)}, max {max(allv):+.1f}")

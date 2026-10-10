#!/usr/bin/env python3
"""r05 (critic 4, plan 8): list the MIDI notes that articulate.py cannot match to a printed note (notes.csv), and the
printed notes without a MIDI note. Usage: unmatched.py WORK"""
import sys, os, csv
from collections import defaultdict, Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "lib"))
import rtk
W = sys.argv[1]
mi = rtk.midi_info(os.path.join(W, "score.midi"))
rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
used = set((r["midi_track"], int(r["midi_on"]), int(r["pitch"]) % 12) for r in rows if r["midi_on"] != "")
import bisect
grid = list(mi["bar_ticks"])
out = []
for on, off, ti, ch, p, v, name in mi["notes"]:
    if (name, int(round(on)), p % 12) not in used:
        b = bisect.bisect_right(grid, on)
        out.append((name, b, int(on), p, v, round(float(mi["t2s"](off) - mi["t2s"](on)), 3)))
print(f"MIDI notes without a printed match: {len(out)}")
for o in out: print("  track %s bar %d tick %d pitch %d vel %d len %.3fs" % o)
pr = [r for r in rows if r["midi_on"] == ""]
print(f"printed notes without a MIDI note: {len(pr)}")
for r in pr[:40]: print("  %s bar %s beat %s pitch %s arts %s" % (r["staff"], r["bar"], r["beat"], r["pitch"], r["arts"]))

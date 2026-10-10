#!/usr/bin/env python3
"""r05: level calibration of a stem between two engines (e.g. FluidR3 against Iowa sfz), per PRINTED dynamic.
Usage: [WORK_B=dir] engcal.py WORK STEM_FILE_BASENAME STAFF_KEY CONFIG_A CONFIG_B
Renders stage 1 (stem.py synth: synthesis, gains, tone, brightness; no room) of the stem MIDI in WORK/stems with
both configs, then the K-weighted level per bar while the staff's notes sound (balance.bar_levels), grouped by the
loudest printed dynamic of the bar; prints median B - A per dynamic and B's dB per printed step."""
import sys, os, csv, json, numpy as np, mido
from collections import defaultdict
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, R); sys.path.insert(0, os.path.join(R, "lib"))
import stem, balance, rtk
W, base, st, ca, cb = sys.argv[1:6]
mid = mido.MidiFile(os.path.join(W, "stems", base + ".mid"))
mi = rtk.midi_info(os.path.join(W, "score.midi"))
bars = [(b["bar"], b["t_start"], b["t_end"]) for b in mi["per_bar"]]
rows = [r for r in csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")) if balance.key(r["midi_track"] or r["staff"]) == st]
pd = balance.printed_dyn(rows).get(st, {})
out = {}
for lab, cp in (("A", ca), ("B", cb)):
    cfg = json.load(open(cp)); sc = cfg["stems"][st]
    if lab == "B" and os.environ.get("WORK_B"):
        # B's own rendering MIDI (articulate.py with config B: CC11 trims are written into the MIDI)
        mid = mido.MidiFile(os.path.join(os.environ["WORK_B"], "stems", base + ".mid"))
    x = stem.synth(mid, sc, cfg, st, sc.get("engine", "fluidsynth"))
    lv, _ = balance.bar_levels(x.astype(np.float64), cfg["sample_rate"], rows, bars)
    out[lab] = lv
    if len(sys.argv) > 6:
        import soundfile as sf; sf.write(os.path.join(sys.argv[6], f"{base}_{lab}.wav"), x, cfg["sample_rate"])
D = balance.DY
by = defaultdict(list); lb = defaultdict(list)
for b, v in out["B"].items():
    if b in out["A"] and b in pd and np.isfinite(v) and np.isfinite(out["A"][b]):
        by[D[pd[b]]].append(v - out["A"][b]); lb[pd[b]].append(v)
print(base, "B - A by printed dynamic (median dB, n):", {d: (round(float(np.median(v)), 1), len(v)) for d, v in sorted(by.items(), key=lambda z: D.index(z[0]))})
xs = [k for k, v in lb.items() for _ in v]; ys = [y for k, v in lb.items() for y in v]
la = defaultdict(list)
for b, v in out["A"].items():
    if b in pd and np.isfinite(v): la[pd[b]].append(v)
xa = [k for k, v in la.items() for _ in v]; ya = [y for k, v in la.items() for y in v]
if len(set(xs)) > 1:
    print(base, "dB per printed step: A %.2f  B %.2f" % (np.polyfit(xa, ya, 1)[0], np.polyfit(xs, ys, 1)[0]))

#!/usr/bin/env python3
"""r06 (critic 5, plan 3): recalibrate stems.<staff>.printed_trim_dB of the Iowa woodwinds from IN-MUSIC stem levels
(stemcmp.md 'vs string median by dyn pp..ff' of one or more renders, not a one-note test).
new trim[d] = old trim[d] + k[d] * (target[d] - mean measured offset[d]); target 0 dB at pp-mp (within +-2 accepted),
-2 dB at mf-ff (winds under the strings unless solo); only the excess beyond a dead band (+-2 dB at pp-mp, +-1 at mf-ff) is corrected; k 0.5 at pp-mp (the two movements disagree there), 0.8 at mf-ff;
fff moves with ff. Usage: windcal.py CONFIG_IN CONFIG_OUT stemcmp.md [stemcmp.md ...]"""
import json, re, sys
import numpy as np
DY = ["pp", "p", "mp", "mf", "f", "ff"]
TGT = {"pp": 0, "p": 0, "mp": 0, "mf": -2, "f": -2, "ff": -2}
K = {"pp": 0.5, "p": 0.5, "mp": 0.5, "mf": 0.8, "f": 0.8, "ff": 0.8}
STEMS = ["Flutes 12", "Oboes 12", "Clarinets 12", "Bass clarinet", "Bassoons 12"]
# r06 pass 2 / brass: WINDCAL_TARGET="pp:0,p:0,mp:0,mf:-1,f:-1,ff:-1" WINDCAL_STEMS="Horns 12,..." override the defaults
import os
if os.environ.get("WINDCAL_TARGET"):
    TGT = {k: float(v) for k, v in (x.split(":") for x in os.environ["WINDCAL_TARGET"].split(","))}
if os.environ.get("WINDCAL_STEMS"):
    STEMS = os.environ["WINDCAL_STEMS"].split(",")
cfg = json.load(open(sys.argv[1]))
meas = {s: {d: [] for d in DY} for s in STEMS}
for p in sys.argv[3:]:
    for line in open(p):
        c = [x.strip() for x in line.split("|")]
        if len(c) > 6 and c[1] in STEMS:
            vals = c[5].split()
            for d, v in zip(DY, vals):
                if v != ".":
                    meas[c[1]][d].append(float(v))
for s in STEMS:
    old = cfg["stems"][s].get("printed_trim_dB", {})
    new = dict(old)
    for d in DY:
        if meas[s][d]:
            m = float(np.mean(meas[s][d]))
            # dead band: pp-mp accepted within +-2 dB of the target, mf-ff within +-1 dB (the critic's -1..-3)
            band = 2.0 if d in ("pp", "p", "mp") else 1.0
            err = TGT[d] - m
            err = np.sign(err) * max(0.0, abs(err) - band)
            new[d] = round(old.get(d, 0.0) + K[d] * err, 1)
    for d in ("pp", "p"):
        # positive soft trims at most +2 dB (critic 5: they undo the samples' own soft layer; bass clarinet pp bar 3)
        if d in new and new[d] > 2.0 and old.get(d, 0.0) <= 2.0:
            new[d] = 2.0
    new = {d: round(float(v), 1) for d, v in new.items()}
    if "ff" in meas[s] and meas[s]["ff"]:
        new["fff"] = round(old.get("fff", 0.0) + (new["ff"] - old.get("ff", 0.0)), 1)
    print(s, {d: (round(float(np.mean(meas[s][d])), 1) if meas[s][d] else None) for d in DY}, "\n   old", old, "\n   new", new)
    cfg["stems"][s]["printed_trim_dB"] = new
json.dump(cfg, open(sys.argv[2], "w"), indent=1)

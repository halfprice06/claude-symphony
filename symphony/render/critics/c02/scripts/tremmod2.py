#!/usr/bin/env python3
"""String tremolo (:32) audibility: envelope modulation energy 8-24 Hz minus 1-6 Hz (dB) of each tremolo note >= 0.6 s,
median per stem, against unmarked held notes >= 0.6 s of the same stem (critic 1's measure, own implementation).
Usage: tremmod2.py notes.csv stems_dir label"""
import csv, sys, os, numpy as np, soundfile as sf, re
from collections import defaultdict
from scipy.signal import welch
nf, d, lab = sys.argv[1:4]
def key(n): return re.sub(r"[^A-Za-z0-9 ]", "", n.split(":")[0]).strip()
rows = list(csv.DictReader(open(nf, encoding="utf-8")))
by = defaultdict(lambda: {"trem": [], "sus": []})
for r in rows:
    st = key(r["staff"])
    if st not in ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses"): continue
    L = float(r["notated_s"]);
    if L < 0.6: continue
    arts = r["arts"].split("|") if r["arts"] else []
    if "tremolo32" in arts: by[st]["trem"].append((float(r["t_on_s"]), L))
    elif not arts and r["tech"] == "": by[st]["sus"].append((float(r["t_on_s"]), L))
def mod(x, sr, t0, L):
    a, b = int((t0 + 0.15) * sr), int((t0 + L - 0.05) * sr); seg = x[a:b]
    h = int(0.005 * sr); n = len(seg) // h
    if n < 60: return None
    env = np.sqrt((seg[:n * h].reshape(n, h) ** 2).mean(1) + 1e-20); env = env / env.mean()
    f, P = welch(env - 1, fs=200, nperseg=min(n, 128))
    hi = P[(f >= 8) & (f <= 24)].mean(); lo = P[(f >= 1) & (f <= 6)].mean()
    return 10 * np.log10(hi / lo)
print(f"{lab}: stem | tremolo 8-24 vs 1-6 Hz dB (n) | held unmarked notes (n) | difference")
for st, v in by.items():
    p = os.path.join(d, st.replace(" ", "_") + ".wav")
    if not os.path.exists(p) or not v["trem"]: continue
    x, sr = sf.read(p, dtype="float64", always_2d=True); x = x.mean(1)
    t = [m for m in (mod(x, sr, *z) for z in v["trem"]) if m is not None]
    s = [m for m in (mod(x, sr, *z) for z in v["sus"][:200]) if m is not None]
    if t:
        mt = np.median(t); ms = np.median(s) if s else np.nan
        print(f"  {st} | {mt:+.1f} ({len(t)}) | {ms:+.1f} ({len(s)}) | {mt-ms:+.1f}")

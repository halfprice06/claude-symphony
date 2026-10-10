#!/usr/bin/env python3
"""Timpani rolls longer than one bar: level against the other stems, decay inside the roll, stroke periodicity.
Usage: rolls2.py notes.csv bars.csv stem_bars.csv timpani_stem.wav [label]
 - per bar of each roll: timpani loudness while sounding minus the loudest other stem (stem_bars.csv, tools/stems.py);
 - decay: timpani K-weighted 400 ms level at 0.4-0.8 s after the roll start and in the last 0.8 s of the roll (dB);
   Dan's rule asks for a fall (settle) unless a crescendo is printed;
 - periodicity: modulation spectrum of the 5 ms RMS envelope (dB re median, 3-40 Hz) and the largest normalised
   autocorrelation of the dB envelope at lags 0.05-0.5 s (machine-gun repetition shows as a sharp peak)."""
import csv, sys, numpy as np, soundfile as sf
from collections import defaultdict
from scipy.signal import welch
sys.path.insert(0, "/mnt/project-files/symphony/render/tools"); import rtk
nf, bf, sbf, wav = sys.argv[1:5]; lab = sys.argv[5] if len(sys.argv) > 5 else ""
bars = [(int(b["bar"]), float(b["t_start"]), float(b["t_end"])) for b in csv.DictReader(open(bf))]
bt = {b: (a, e) for b, a, e in bars}
SB = defaultdict(dict)
for r in csv.DictReader(open(sbf)):
    v = r.get("loud_LUFS", r.get("LUFS"))   # stems.py stem_bars.csv (while sounding) or barlev.py (whole bar)
    if v not in ("", "nan", None): SB[int(r["bar"])][r["stem"]] = float(v)
x, sr = sf.read(wav, dtype="float64", always_2d=True)
k = rtk.k_weight(x, sr); e = (k ** 2).sum(1)
def lev(a, b):
    i, j = int(a * sr), int(b * sr); return 10 * np.log10(e[i:j].mean() + 1e-20) - 0.691
m = x.mean(1)
rows = [r for r in csv.DictReader(open(nf, encoding="utf-8")) if r["staff"].startswith("Timp") and "tremolo" in r["arts"]]
tot = loud = 0
print(f"{lab}: roll bars | dyn | hairpin | len s | timpani minus loudest other per bar (dB) | start / end level, change dB | mod peak Hz (prominence dB) | env autocorr max 0.05-0.5 s (lag) | 1.5-6 s (lag)")
for r in rows:
    t0 = float(r["t_on_s"]); L = float(r["notated_s"]); t1 = t0 + L; b0 = int(r["bar"])
    blen = bt[b0][1] - bt[b0][0]
    if L <= blen * 1.01: continue
    bs = [b for b, a, e2 in bars if a < t1 - 0.05 and e2 > t0 + 0.05]
    per = []
    for b in bs:
        o = {s: v for s, v in SB[b].items() if s not in ("Timpani", "drums")}
        if "Timpani" in SB[b] and o:
            s2 = max(o, key=o.get); d = SB[b]["Timpani"] - o[s2]; per.append(f"{b}:{d:+.1f}"); tot += 1; loud += d > 0
    st = lev(t0 + 0.4, t0 + 0.8); en = lev(t1 - 0.8, t1)
    h = int(0.005 * sr); seg = m[int((t0 + 0.4) * sr):int(t1 * sr)]; n = len(seg) // h
    env = np.sqrt((seg[:n * h].reshape(n, h) ** 2).mean(1) + 1e-20)
    lin = env / env.mean() - 1
    f, P = welch(lin, fs=200, nperseg=min(len(lin), 256)); s = (f >= 3) & (f <= 40)
    pk = f[s][np.argmax(P[s])]; prom = 10 * np.log10(P[s].max() / np.median(P[s]))
    d = 20 * np.log10(env); d = d - np.convolve(d, np.ones(41) / 41, "same"); d = d[20:-20] - d[20:-20].mean()
    ac = np.correlate(d, d, "full")[len(d) - 1:]; ac /= ac[0]; lo, hi = 10, min(100, len(ac) - 1)
    am = ac[lo:hi].max(); al = (lo + np.argmax(ac[lo:hi])) * 0.005
    lo2, hi2 = 300, min(1200, len(ac) - 100)   # 1.5-6 s: repetition of a sample loop
    lm, ll = (ac[lo2:hi2].max(), (lo2 + np.argmax(ac[lo2:hi2])) * 0.005) if hi2 > lo2 + 20 else (np.nan, np.nan)
    print(f"{b0}-{bs[-1]} | {r['dyn']} | {r['hairpin'] or '-'} | {L:.1f} | {' '.join(per)} | {st:.1f} / {en:.1f}, {en-st:+.1f} | {pk:.1f} ({prom:.1f}) | {am:.2f} ({al:.2f}) | loop {lm:.2f} ({ll:.2f})")
print(f"{lab}: bars where timpani is the loudest stem: {loud} of {tot}")

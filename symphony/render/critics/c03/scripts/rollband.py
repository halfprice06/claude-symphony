#!/usr/bin/env python3
"""Timpani roll audibility in its own band: for each roll longer than a bar, the timpani stem's energy in a band around
its pitch (fundamental/1.2 .. fundamental x 3) against the sum of all other stems in the same band, over the first 1 s of
the roll and over the rest (dB). Rough masking proxy: a band ratio below about -10 dB suggests the roll is masked.
Usage: rollband.py WORK label"""
import sys, os, csv, glob, numpy as np, soundfile as sf
from scipy.signal import butter, sosfiltfilt
W, lab = sys.argv[1:3]
sys.path.insert(0, "/mnt/project-files/symphony/render/r03/lib"); import marks, rtk
mi = rtk.midi_info(os.path.join(W, "score.midi")); rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
R = [r for r in rows if r["staff"].startswith("Timp") and "tremolo" in (r["arts"] or "")]
rl = marks.rolls(rows, mi["bar_s"])
stems = {os.path.basename(p)[:-4]: p for p in glob.glob(os.path.join(W, "stems", "*.wav")) if not p.endswith("_syn.wav")}
X = {}
def seg(name, a, b):
    info = sf.info(stems[name]); sr = info.samplerate
    x, _ = sf.read(stems[name], start=int(a * sr), stop=int(b * sr), dtype="float64", always_2d=True)
    return x.mean(1), sr
print(f"{lab}: roll | dyn | pitch | band Hz | timpani minus others in band: first 1 s / rest (dB)")
for t0, t1, bs, dyn, hp in rl:
    r = min(R, key=lambda r: abs(float(r["t_on_s"]) - t0))
    p = int(r["pitch"])
    f0 = 440 * 2 ** ((p - 69) / 12); lo, hi = f0 / 1.2, min(f0 * 3, 1000)
    def band(name, a, b):
        x, sr = seg(name, a, b)
        sos = butter(4, [lo, hi], "bandpass", fs=sr, output="sos"); y = sosfiltfilt(sos, x)
        return (y ** 2).mean()
    out = []
    for a, b in [(t0, t0 + 1.0), (t0 + 1.0, t1)]:
        if b <= a + 0.2: out.append(float("nan")); continue
        tp = band("Timpani", a, b); ot = sum(band(n, a, b) for n in stems if n != "Timpani")
        out.append(10 * np.log10(tp / (ot + 1e-20) + 1e-20))
    print(f"{bs[0]}-{bs[-1]} | {dyn} | {p} ({f0:.0f} Hz) | {lo:.0f}-{hi:.0f} | {out[0]:+.1f} / {out[1]:+.1f}")

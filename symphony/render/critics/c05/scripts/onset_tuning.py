#!/usr/bin/env python3
"""critic 5: in a rendered dry stem (<stem>_syn.wav), how long each isolated note (>= 0.6 s, no other note sounding
in the stem) takes to come within 30 cents of its MIDI pitch, and how much of that time sits a semitone low.
Usage: onset_tuning.py WORK stem [stem ...]"""
import sys, os, numpy as np, soundfile as sf, mido
src = open(os.path.join(os.path.dirname(__file__), 'pitchcheck.py')).read().split('W = sys.argv')[0]
exec(src)
W = sys.argv[1]
for s in sys.argv[2:]:
    ns = notes_of(f'{W}/stems/{s}.mid')
    x, sr = sf.read(f'{W}/stems/{s}_syn.wav', dtype='float32', always_2d=True); x = x.mean(1).astype(float)
    T = []; low = []; n = 0
    for i, (a, b, p) in enumerate(ns):
        if b - a < 0.6: continue
        if any(c < b and d > a for j, (c, d, q) in enumerate(ns) if j != i): continue
        ft = 440 * 2 ** ((p - 69) / 12); n += 1
        ws = []
        for t in np.arange(0.0, 0.6, 0.02):
            seg = x[int((a + t) * sr):int((a + t + 0.06) * sr)]
            r = f0(seg[::2], sr / 2, ft / 1.6, ft * 1.6) if np.sqrt((seg ** 2).mean()) > 1e-5 else None
            ws.append(None if not r else 1200 * np.log2(r / ft))
        ok = next((k for k, v in enumerate(ws) if v is not None and abs(v) <= 30 and all(w is None or abs(w) <= 30 for w in ws[k:k + 3])), None)
        T.append(0.6 if ok is None else ok * 0.02)
        low.append(sum(1 for v in ws[:ok or 30] if v is not None and -140 <= v <= -60) * 0.02)
    if n:
        T = np.array(T); low = np.array(low)
        print(f'{s}: {n} isolated notes; time to pitch (+-30 c) median {np.median(T):.2f} s, p90 {np.percentile(T,90):.2f} s; '
              f'notes with >= 0.1 s a semitone low: {np.mean(low>=0.1)*100:.0f} %, median low time {np.median(low):.2f} s')

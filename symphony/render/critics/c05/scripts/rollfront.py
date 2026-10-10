#!/usr/bin/env python3
"""critic 5: front edge of each timpani roll (tremolo notes) in the dry timpani stem: level of the first 1 ms after the
first audible sample relative to the peak of the first 150 ms (a value near 0 dB with no build-up = a step, click-like),
and the step from the 1 ms before. Usage: rollfront.py WORK"""
import sys, csv, numpy as np, soundfile as sf
W = sys.argv[1]; p = f'{W}/stems/Timpani_syn.wav'; sr = sf.info(p).samplerate
seen = set()
for r in csv.DictReader(open(f'{W}/notes.csv')):
    if not r['staff'].startswith('Timp') or 'tremolo' not in r['arts'] or not r['t_on_s']: continue
    t = float(r['t_on_s'])
    if round(t, 2) in seen: continue
    seen.add(round(t, 2))
    x, _ = sf.read(p, start=max(0, int((t - 0.05) * sr)), stop=int((t + 0.2) * sr), always_2d=True); x = x.mean(1)
    a = np.abs(x); thr = a.max() * 1e-3
    i = int(np.argmax(a > thr)); ms = sr // 1000
    first = 20 * np.log10(np.sqrt(np.mean(x[i:i + ms] ** 2)) + 1e-12)
    pk = 20 * np.log10(np.sqrt(np.mean(x[i:i + 150 * ms] ** 2)) + 1e-12)
    steady = 20 * np.log10(max(np.sqrt(np.mean(x[i + k * ms:i + (k + 5) * ms] ** 2)) for k in range(0, 145, 5)) + 1e-12)
    print(f"bar {r['bar']:>3} pitch {r['pitch']} {r['dyn']:>4} {float(r['notated_s']):5.1f} s: first 1 ms {first - steady:+6.1f} dB re loudest 5 ms of the first 150 ms; first sample {x[i]:+.4f} vs peak {a.max():.4f}")

#!/usr/bin/env python3
"""critic 5: tuning of each stem's isolated notes. For notes >= 0.35 s that do not overlap another note of the same
stem, estimate f0 on the dry stage-1 signal (<stem>_syn.wav) 0.12-0.32 s after onset (YIN-like difference function)
and report the deviation from the MIDI pitch in cents. Usage: pitchcheck.py WORK [stem ...]"""
import sys, os, glob, numpy as np, soundfile as sf, mido

def notes_of(mid):
    m = mido.MidiFile(mid); out = []; on = {}; t = 0.0
    for msg in m:  # merged, in seconds
        t += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            on.setdefault((msg.channel, msg.note), []).append(t)
        elif msg.type in ('note_off', 'note_on'):
            k = (msg.channel, msg.note)
            if on.get(k):
                out.append((on[k].pop(0), t, msg.note))
    return sorted(out)

def f0(x, sr, fmin, fmax):
    x = x - x.mean(); n = len(x)
    lo, hi = int(sr / fmax), int(sr / fmin)
    W = n - hi
    if W < 256: return None
    d = np.array([np.sum((x[:W] - x[tau:tau + W]) ** 2) for tau in range(lo, hi)])
    cm = d * np.arange(1, len(d) + 1) / np.maximum(np.cumsum(d), 1e-12)
    i = int(np.argmin(cm))
    if cm[i] > 0.3: return None
    if 0 < i < len(d) - 1:
        a, b, c = d[i - 1], d[i], d[i + 1]; den = a - 2 * b + c
        sh = 0.5 * (a - c) / den if den else 0
    else: sh = 0
    return sr / (lo + i + sh)

W = sys.argv[1]; stems = sys.argv[2:] or [os.path.basename(p)[:-4] for p in sorted(glob.glob(W + '/stems/*.mid'))]
for s in stems:
    wav = f'{W}/stems/{s}_syn.wav'
    if not os.path.exists(wav): continue
    x, sr = sf.read(wav, dtype='float32', always_2d=True); x = x.mean(1)
    ns = notes_of(f'{W}/stems/{s}.mid'); dev = []
    for i, (a, b, p) in enumerate(ns):
        if b - a < 0.35 or p < 36 or p > 100: continue
        if any((c < b and d > a) for j, (c, d, q) in enumerate(ns) if j != i and abs(c - a) < 5 and q != p): continue
        if any((c < b and d > a) and q != p for (c, d, q) in ns[max(0, i - 30):i + 30] if (c, d, q) != (a, b, p)): continue
        seg = x[int((a + 0.12) * sr):int((a + 0.32) * sr)]
        if len(seg) < 2000 or np.sqrt((seg ** 2).mean()) < 1e-4: continue
        ft = 440 * 2 ** ((p - 69) / 12)
        f = f0(seg.astype(np.float64)[::2], sr / 2, ft / 1.5, ft * 1.5)
        if f: dev.append(1200 * np.log2(f / ft))
    if not dev: print(f'{s}: no usable notes'); continue
    d = np.array(dev)
    print(f'{s}: n {len(d)} median {np.median(d):+.1f} c, |dev| p50 {np.median(abs(d)):.1f} p90 {np.percentile(abs(d),90):.1f} c, >15 c: {np.mean(abs(d)>15)*100:.0f} %, >25 c: {np.mean(abs(d)>25)*100:.0f} %')

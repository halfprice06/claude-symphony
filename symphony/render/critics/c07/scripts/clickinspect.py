#!/usr/bin/env python3
"""critic 7: inspect every premaster 'isolated HF spike' (critics/c02/scripts/clicks2.py detector) without listening.
For each detection: which wet stem carries the >6 kHz burst (stem HF energy in the 1 ms frame over its own 41 ms median),
the spacing of neighbouring detections (a periodic train at f0 = buzz/reed pulse, a lone one = click candidate), and on
the dry stage-1 signal of that stem (<stem>_syn.wav) whether there is a sample discontinuity: the largest
second-difference sample within +-2 ms over the median |second difference| of the surrounding 40 ms (a splice or
loop-seam click is one outlier sample, > 30x; a pulse waveform is smooth, < 15x), and whether the same burst repeats
at the note's fundamental period (autocorrelation of the HF envelope).
Usage: clickinspect.py WORK_DIR [max_events]"""
import sys, os, glob
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
from scipy.ndimage import median_filter

W = sys.argv[1]
MAXE = int(sys.argv[2]) if len(sys.argv) > 2 else 999


def hf_frames(m, sr):
    sos = butter(4, 6000, 'highpass', fs=sr, output='sos'); h = sosfilt(sos, m)
    w = int(0.001 * sr); n = len(h) // w
    e = (h[:n * w].reshape(n, w) ** 2).mean(1) + 1e-16
    return e, median_filter(e, 41), w, n, m


def detect(p):
    x, sr = sf.read(p, dtype='float32', always_2d=True); m = x.mean(1).astype(np.float64)
    e, ref, w, n, m = hf_frames(m, sr)
    full = (m[:n * w].reshape(n, w) ** 2).mean(1)
    fullref = np.convolve(full, np.ones(41) / 41, 'same') + 1e-16
    jump = 10 * np.log10(e / ref)
    cand = np.nonzero((jump > 15) & (10 * np.log10(e) > -95) & (10 * np.log10(fullref) > -80))[0]
    iso = [c for c in cand if c + 4 < n and jump[c + 4] < 6]
    ev = []
    for c in iso:
        if not ev or c - ev[-1] > 20:
            ev.append(c)
    return ev, sr


ev, sr = detect(os.path.join(W, 'mix_prem.wav'))
print(f'premaster detections: {len(ev)}')
stems = {}
for p in sorted(glob.glob(os.path.join(W, 'stems', '*.wav'))):
    b = os.path.basename(p)[:-4]
    if b.endswith('_syn'):
        continue
    x, s2 = sf.read(p, dtype='float32', always_2d=True)
    m = x.mean(1).astype(np.float64)
    e, ref, w, n, _ = hf_frames(m, s2)
    stems[b] = (e, ref, m)
syn_cache = {}
rows = []
for c in ev[:MAXE]:
    best = []
    for b, (e, ref, m) in stems.items():
        if c < len(e):
            best.append((10 * np.log10(e[c] + 1e-16), 10 * np.log10(e[c] / ref[c]), b))
    best.sort(reverse=True)
    lvl, jmp, st = best[0]
    # dry signal discontinuity test
    sp = os.path.join(W, 'stems', st + '_syn.wav')
    disc = float('nan'); per = float('nan')
    if os.path.exists(sp):
        if st not in syn_cache:
            y, s3 = sf.read(sp, dtype='float32', always_2d=True); syn_cache[st] = (y.mean(1).astype(np.float64), s3)
        y, s3 = syn_cache[st]
        i = int(c * 0.001 * s3)
        a, z = max(0, i - int(0.02 * s3)), min(len(y), i + int(0.02 * s3))
        d2 = np.abs(np.diff(y[a:z], 2))
        if len(d2) > 10:
            k0, k1 = max(0, i - a - int(0.003 * s3)), i - a + int(0.004 * s3)
            disc = d2[k0:k1].max() / (np.median(d2) + 1e-12)
            hp = sosfilt(butter(4, 6000, 'highpass', fs=s3, output='sos'), y[a:z]) ** 2
            env = np.convolve(hp, np.ones(int(0.0005 * s3)), 'same'); env -= env.mean()
            ac = np.correlate(env, env, 'full')[len(env) - 1:]; ac /= ac[0] + 1e-30
            lo, hi = int(0.002 * s3), int(0.03 * s3)
            k = lo + int(np.argmax(ac[lo:hi])); per = (k / s3 * 1000, ac[k])
    rows.append((c * 0.001, st, lvl, jmp, best[1][2] if len(best) > 1 else '-', best[1][0] - lvl if len(best) > 1 else 0, disc, per))
for t, st, lvl, jmp, st2, d2nd, disc, per in rows:
    ps = f'{per[0]:.1f} ms r={per[1]:.2f}' if isinstance(per, tuple) else '-'
    print(f'{t:8.3f}s  {st:16s} HF {lvl:6.1f} dB (+{jmp:4.1f} over own median)  next {st2:14s} {d2nd:+5.1f} dB  '
          f'dry 2nd-diff outlier {disc:5.1f}x  HF-envelope period {ps}')
from collections import Counter
print('by stem:', dict(Counter(r[1] for r in rows)))
d = np.diff([r[0] for r in rows]) * 1000
print('spacing between consecutive detections (ms), median %.1f; share 20-30 ms: %.2f' % (np.median(d) if len(d) else 0, np.mean((d > 20) & (d < 30)) if len(d) else 0))
print('dry discontinuity outliers > 30x: %d of %d' % (sum(1 for r in rows if r[6] == r[6] and r[6] > 30), len(rows)))

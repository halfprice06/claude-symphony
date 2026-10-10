#!/usr/bin/env python3
"""critic 5: pitch of the first 0.4 s of every Iowa per-note sample (assets/iowa/<inst>/KKK_dyn.wav) against its
steady part (0.6-0.8 s). Finds samples that begin with the previous note of the chromatic run (segmentation error).
Usage: iowa_onset_pitch.py ASSETS_IOWA_DIR [inst ...]"""
import sys, glob, os, numpy as np, soundfile as sf
src = open(os.path.join(os.path.dirname(__file__), 'pitchcheck.py')).read().split('W = sys.argv')[0]
exec(src)
D = sys.argv[1]; insts = sys.argv[2:] or sorted(os.listdir(D))
for inst in insts:
    fs = sorted(glob.glob(f'{D}/{inst}/*_*.wav'))
    if not fs: continue
    bad = []; tot = 0; wins = [(0.02, 0.10), (0.10, 0.18), (0.18, 0.26), (0.26, 0.34)]
    for f in fs:
        k = int(os.path.basename(f)[:3]); x, sr = sf.read(f, always_2d=True); x = x.mean(1)
        ft = 440 * 2 ** ((k - 69) / 12)
        def c(a, b):
            seg = x[int(a * sr):int(b * sr)]
            if len(seg) < int(0.06 * sr): return None
            r = f0(seg, sr, ft / 1.6, ft * 1.6)
            return None if not r else 1200 * np.log2(r / ft)
        ref = c(0.6, 0.8)
        if ref is None: continue
        tot += 1
        d = [c(a, b) for a, b in wins]
        dd = [None if v is None else round(v - ref) for v in d]
        # the first window that is within 30 c of the steady pitch
        ok = next((i for i, v in enumerate(dd) if v is not None and abs(v) <= 30), None)
        if ok is None or ok > 0:
            bad.append((os.path.basename(f), dd, ok))
    late = [b for b in bad if b[2] is None or b[2] >= 2]
    print(f'{inst}: {tot} samples; first 80 ms off pitch (>30 c or unvoiced) {len(bad)}; still off after 180 ms {len(late)}')
    for b in late[:6]: print('   ', b[0], 'cents re steady per 80 ms window from 20 ms:', b[1])

print('previous-note lead-in (any 80 ms window in the first 0.26 s at -60..-140 c re steady), and its length:')
for inst in insts:
    fs = sorted(glob.glob(f'{D}/{inst}/*_*.wav')); n = 0; L = []; tot = 0
    for f in fs:
        k = int(os.path.basename(f)[:3]); x, sr = sf.read(f, always_2d=True); x = x.mean(1)
        ft = 440 * 2 ** ((k - 69) / 12)
        def c(a, b):
            seg = x[int(a * sr):int(b * sr)]
            r = f0(seg, sr, ft / 1.6, ft * 1.6) if len(seg) > 0.05 * sr else None
            return None if not r else 1200 * np.log2(r / ft)
        ref = c(0.6, 0.8)
        if ref is None: continue
        tot += 1
        ws = [c(a, a + 0.06) for a in np.arange(0.0, 0.5, 0.02)]
        prev = [i for i, v in enumerate(ws) if v is not None and -140 <= v - ref <= -60]
        if prev and prev[0] * 0.02 < 0.26:
            n += 1; L.append(0.02 * prev[-1] + 0.06)
    if tot:
        print(f'  {inst}: {n} of {tot} samples; lead-in ends at median {np.median(L) if L else 0:.2f} s, max {max(L) if L else 0:.2f} s')

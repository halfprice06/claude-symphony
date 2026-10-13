#!/usr/bin/env python3
"""critic 7: every timpani roll longer than one bar, as r07 sees it (lib/marks.roll_chains: chains of untied tremolo
notes are one roll), on the placed Timpani stem of a render work folder:
 - printed dynamics/hairpins along the chain (from the members);
 - settle: K-weighted level 0.4-0.8 s after the start vs the last 0.8 s, and the slope (dB/s) over stretches with no
   printed hairpin and no new dynamic (Dan: settle softer unless a crescendo is printed);
 - junctions: level change across each member boundary (+-0.3 s), i.e. a bump or a hole where a new note/drum begins;
 - stroke periodicity: modulation-spectrum peak 3-40 Hz (prominence) and envelope autocorrelation 0.05-0.5 s (r02-c06
   method; < 0.25 = no machine-gun), loop repetition 1.5-6 s.
Usage: rollchk7.py WORK [LIB_DIR]  (LIB_DIR default r07/lib)"""
import sys, os, csv
import numpy as np, soundfile as sf
from scipy.signal import welch
W = sys.argv[1]
LIB = sys.argv[2] if len(sys.argv) > 2 else '/mnt/project-files/symphony/render/r07/lib'
sys.path.insert(0, LIB)
import marks, rtk
rows = list(csv.DictReader(open(os.path.join(W, 'notes.csv'), encoding='utf-8')))
mi = rtk.midi_info(os.path.join(W, 'score.midi'))
bars = [(b['bar'], b['t_start'], b['t_end']) for b in mi['per_bar']]
x, sr = sf.read(os.path.join(W, 'stems', 'Timpani.wav'), dtype='float64', always_2d=True)
k = rtk.k_weight(x, sr); e = (k ** 2).sum(1); m = x.mean(1)


def lev(a, b):
    i, j = int(max(0, a) * sr), int(b * sr)
    return 10 * np.log10(e[i:j].mean() + 1e-20) - 0.691


print('roll | printed along the roll | len s | members/drums | start->end dB | flat-stretch slope dB/s | junction jumps dB | mod peak Hz (prom dB) | ac 0.05-0.5 s | loop ac 1.5-6 s')
for c in marks.roll_chains(rows, mi['tpb']):
    mem = c['members']; r0 = mem[0]
    t0 = float(r0['t_on_s']); t1 = float(mem[-1]['t_on_s']) + float(mem[-1]['notated_s'])
    b0 = int(r0['bar']); bl = [b for b, a, z in bars if b == b0][0]
    blen = [z - a for b, a, z in bars if b == b0][0]
    if t1 - t0 <= blen * 1.01:
        continue
    bend = max(b for b, a, z in bars if a < t1 - 0.05)
    pr = []
    for r in mem:
        s = f"{r['bar']}:{r['dyn']}{(r['hairpin'] or '')[:3]}"
        if r.get('inner'):
            s += '[' + r['inner'].replace('dyn:', '') + ']'
        pr.append(s)
    drums = len(set(r['pitch'] for r in mem))
    st, en = lev(t0 + 0.4, t0 + 0.8), lev(t1 - 0.8, t1)
    # flat stretches: members with no hairpin and no inner event; slope over each (after 1 s from its start)
    slopes = []
    for r in mem:
        if (r['hairpin'] or '') or (r.get('inner') or ''):
            continue
        a = float(r['t_on_s']) + (1.0 if r is r0 else 0.3); z = float(r['t_on_s']) + float(r['notated_s']) - 0.2
        if z - a > 1.5:
            ts = np.arange(a, z - 0.5, 0.5); ls = [lev(t, t + 0.5) for t in ts]
            slopes.append(np.polyfit(ts, ls, 1)[0])
    jj = []
    for r in mem[1:]:
        t = float(r['t_on_s']); jj.append(lev(t, t + 0.3) - lev(t - 0.3, t))
    h = int(0.005 * sr); seg = m[int((t0 + 0.4) * sr):int(t1 * sr)]; n = len(seg) // h
    env = np.sqrt((seg[:n * h].reshape(n, h) ** 2).mean(1) + 1e-20)
    lin = env / env.mean() - 1
    f, P = welch(lin, fs=200, nperseg=min(len(lin), 256)); s = (f >= 3) & (f <= 40)
    pk = f[s][np.argmax(P[s])]; prom = 10 * np.log10(P[s].max() / np.median(P[s]))
    d = 20 * np.log10(env); d = d - np.convolve(d, np.ones(41) / 41, 'same'); d = d[20:-20] - d[20:-20].mean()
    ac = np.correlate(d, d, 'full')[len(d) - 1:]; ac /= ac[0]; lo, hi = 10, min(100, len(ac) - 1)
    am = ac[lo:hi].max()
    lo2, hi2 = 300, min(1200, len(ac) - 100)
    lm = ac[lo2:hi2].max() if hi2 > lo2 + 20 else np.nan
    print(f"{b0}-{bend} | {' '.join(pr)} | {t1 - t0:.1f} | {len(mem)}/{drums} | {st:.1f}->{en:.1f} ({en - st:+.1f}) | "
          f"{' '.join(f'{v:+.2f}' for v in slopes) or '-'} | {' '.join(f'{v:+.1f}' for v in jj) or '-'} | "
          f"{pk:.1f} ({prom:.1f}) | {am:.2f} | {lm:.2f}")

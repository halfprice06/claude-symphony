#!/usr/bin/env python3
"""r06 copy of critic 5 accents.py that leaves out notes under a printed hairpin (a crescendo raises them on purpose; v156 Horns 1-2 mp accents sit in crescendos). Original doc: critic 5 (Dan 2026-10-10: "accented notes have too much attack"). Per stem, accented (accent, marcato, sf) vs
unaccented notes of the same stem at the same printed dynamic, on the renderer's wet stems (WORK/stems/<stem>.wav):
  boost     peak of the 1 ms-hop 5 ms RMS envelope in the first 150 ms, re the median unaccented peak (dB)
  rise      10 %-90 % rise time of that envelope (amplitude) from the note's onset (ms)
  crest     onset crest: peak in the first 60 ms minus the mean level 150-400 ms after the onset (dB; how much
            the attack sticks out of its own sustain; large = spiky front, small = weight)
  edge      steepest 1 ms rise of the 5 ms RMS envelope in dB (front-edge sharpness; a click-like edge is > 6 dB/ms)
Only clean onsets: the stem is >= 8 dB quieter 30-10 ms before the note. Usage: accents.py WORK LABEL"""
import sys, csv, os, numpy as np, soundfile as sf
from collections import defaultdict
W, LAB = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(f'{W}/notes.csv')))
by = defaultdict(list)
for r in rows:
    by[r['staff']].append(r)
def env(x, sr):
    h = sr // 1000; w = 5 * h
    p = np.convolve(x ** 2, np.ones(w) / w, mode='same')[::h]
    return 10 * np.log10(p + 1e-14)  # dB, 1 ms hop
out = []
print(f'{LAB}: stem | n acc / n plain (clean onsets) | boost dB | rise ms acc / plain | onset crest dB acc / plain | edge dB/ms acc / plain')
for staff, rs in sorted(by.items()):
    fn = f"{W}/stems/{staff.replace(' ', '_').replace('·', '')}.wav"
    if not os.path.exists(fn):
        import glob
        c = [p for p in glob.glob(f'{W}/stems/*.wav') if not p.endswith('_syn.wav') and os.path.basename(p)[:-4].replace('_', ' ').replace('  ', ' ') .startswith(staff.split()[0])]
        fn = c[0] if len(c) == 1 else None
    if not fn: continue
    x, sr = sf.read(fn, dtype='float32', always_2d=True); x = x.mean(1).astype(np.float64)
    e = env(x, sr); n = len(e)
    stats = {'acc': defaultdict(list), 'pl': defaultdict(list)}
    onsets = sorted(set(round(float(r['t_on_s']), 3) for r in rs if r['t_on_s']))
    for r in rs:
        if not r['t_on_s'] or r['hairpin'] or 'tremolo' in r['arts'] or 'staccato' in r['arts'] or r['tech'] == 'pizz': continue
        t = float(r['t_on_s']); i = int(t * 1000)
        if i < 40 or i + 400 >= n: continue
        if float(r['t_off_s']) - t < 0.2: continue
        # another onset of this stem within 300 ms after spoils the window
        if any(t < o < t + 0.3 for o in onsets): continue
        pre = e[i - 30:i - 10].max(); seg = e[i:i + 150]; pk = seg.max()
        if pk - pre < 8: continue
        kind = 'acc' if (any(a in r['arts'] for a in ('accent', 'marcato')) or r['dyn'] in ('sf', 'sfz', 'fz')) else 'pl'
        dyn = r['dyn'] if r['dyn'] not in ('sf', 'sfz', 'fz') else 'f'
        a = 10 ** (e[i - 10:i + 150] / 20); a0 = a[:10].mean(); A = a.max()
        lo = a0 + 0.1 * (A - a0); hi = a0 + 0.9 * (A - a0)
        k10 = np.argmax(a >= lo); k90 = np.argmax(a >= hi)
        crest = e[i:i + 60].max() - 10 * np.log10(np.mean(10 ** (e[i + 150:i + 400] / 10)))
        edge = np.diff(e[i - 5:i + 60]).max()
        stats[kind][dyn].append((pk, k90 - k10, crest, edge))
    acc, pl = stats['acc'], stats['pl']
    B = []; RA = []; RP = []; CA = []; CP = []; EA = []; EP = []
    for d in acc:
        if d not in pl or len(pl[d]) < 2: continue
        med = np.median([v[0] for v in pl[d]])
        B += [v[0] - med for v in acc[d]]; RA += [v[1] for v in acc[d]]; CA += [v[2] for v in acc[d]]; EA += [v[3] for v in acc[d]]
        RP += [v[1] for v in pl[d]]; CP += [v[2] for v in pl[d]]; EP += [v[3] for v in pl[d]]
    if len(B) < 2: continue
    md = lambda z: f'{np.median(z):.1f}' if z else '-'
    print(f'{staff} | {len(B)} / {len(RP)} | {md(B)} | {md(RA)} / {md(RP)} | {md(CA)} / {md(CP)} | {md(EA)} / {md(EP)}')

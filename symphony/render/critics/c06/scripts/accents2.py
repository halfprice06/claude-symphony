#!/usr/bin/env python3
"""critic 6: accents against their NEIGHBOURS (Dan 2026-10-10 "accented notes have too much attack").
critic 5's accents.py uses only clean onsets (5 % of the accents). Here every accented note (accent/marcato, not sf,
not staccato/tremolo/pizz, sounding >= 0.15 s) is compared with the plain notes of the same staff and printed dynamic
whose onsets lie within +-4 s (outside hairpins for both), on the dry stage-1 stem (<stem>_syn.wav) or the wet stem.
Per note (10 ms RMS envelope, 1 ms hop, dB):
  peak    max over onset .. +150 ms
  rise    peak minus the level 30-5 ms before the onset (how far the note jumps out of what was sounding)
  crest   max over 0-60 ms minus the mean over 150-400 ms (front over its own sustain; only notes >= 0.45 s)
  edge    steepest 1 ms rise in -5 .. +60 ms (dB/ms)
Per stem: medians of (accent - local plain median) for peak, rise, crest, edge, and n.
Usage: accents2.py WORK LABEL [syn|wet]"""
import sys, csv, os, glob, numpy as np, soundfile as sf
from collections import defaultdict
W, LAB = sys.argv[1], sys.argv[2]; MODE = sys.argv[3] if len(sys.argv) > 3 else 'syn'
rows = list(csv.DictReader(open(f'{W}/notes.csv')))
by = defaultdict(list)
for r in rows:
    if r['t_on_s']:
        by[r['staff']].append(r)
def env(x, sr):
    h = sr // 1000; w = 10 * h
    p = np.convolve(x ** 2, np.ones(w) / w, mode='same')[::h]
    return 10 * np.log10(p + 1e-14)
def stemfile(staff):
    base = staff.replace(' ', '_').replace('·', '')
    suf = '_syn.wav' if MODE == 'syn' else '.wav'
    fn = f'{W}/stems/{base}{suf}'
    return fn if os.path.exists(fn) else None
print(f'{LAB} ({MODE} stems): stem | n acc (n with crest) | peak dB | rise dB | crest dB | edge dB/ms   (accent minus local plain median; medians)')
allv = defaultdict(list)
for staff, rs in sorted(by.items()):
    fn = stemfile(staff)
    if not fn: continue
    x, sr = sf.read(fn, dtype='float32', always_2d=True); x = x.mean(1).astype(np.float64)
    e = env(x, sr); n = len(e)
    feats = []
    for r in rs:
        a = r['arts'] or ''
        if any(k in a for k in ('tremolo', 'staccato')) or r['tech'] == 'pizz' or r['dyn'] in ('sf', 'sfz', 'fz', 'fp', ''):
            continue
        t = float(r['t_on_s']); dur = float(r['t_off_s']) - t; i = int(round(t * 1000))
        if dur < 0.15 or i < 40 or i + 400 >= n: continue
        acc = ('accent' in a) or ('marcato' in a)
        pk = e[i:i + 150].max(); pre = e[i - 30:i - 5].mean()
        crest = e[i:i + 60].max() - 10 * np.log10(np.mean(10 ** (e[i + 150:i + 400] / 10))) if dur >= 0.45 else np.nan
        edge = np.diff(e[i - 5:i + 60]).max()
        feats.append((t, acc, bool(r['hairpin']), r['dyn'], pk, pk - pre, crest, edge))
    D = defaultdict(list)
    for f in feats:
        if not f[1] or f[2]: continue
        nb = [g for g in feats if not g[1] and not g[2] and g[3] == f[3] and abs(g[0] - f[0]) <= 4.0]
        if len(nb) < 2: continue
        for k, j in (('peak', 4), ('rise', 5), ('crest', 6), ('edge', 7)):
            vals = [g[j] for g in nb if not np.isnan(g[j])]
            if not np.isnan(f[j]) and vals:
                D[k].append(f[j] - np.median(vals))
    if len(D['peak']) < 3: continue
    md = lambda z: f'{np.median(z):+.1f}' if len(z) else '-'
    print(f"{staff} | {len(D['peak'])} ({len(D['crest'])}) | {md(D['peak'])} | {md(D['rise'])} | {md(D['crest'])} | {md(D['edge'])}")
    for k in D: allv[k] += D[k]
md = lambda z: f'{np.median(z):+.1f}' if len(z) else '-'
print(f"ALL | {len(allv['peak'])} ({len(allv['crest'])}) | {md(allv['peak'])} | {md(allv['rise'])} | {md(allv['crest'])} | {md(allv['edge'])}")

#!/usr/bin/env python3
"""Marked melodies (lib/marks.py, derived from the score) against the loudest stem that does NOT carry a marked melody
in the same bar (harp, percussion out): median over the phrase bars. Companion to critic 2's melody2.py, whose
'loudest other' includes concurrent marked melodies (e.g. Violins I + II molto cantabile unis.), where at most one of
two equal lines can be >= 0 dB. Usage: melody_nonmel.py events.tsv notes.csv stem_bars.csv midi"""
import sys, csv
from collections import defaultdict
import numpy as np
sys.path.insert(0, '/mnt/project-files/symphony/render/r03/lib')
import marks, rtk
ev, nf, sb, midi = sys.argv[1:5]
mi = rtk.midi_info(midi); rows = list(csv.DictReader(open(nf, encoding='utf-8')))
mel = marks.melodies(ev, rows, mi['bar_s'], tpb=mi['tpb'])
mel_at = defaultdict(set)
for s, bs, *_ in mel:
    for b in bs: mel_at[b].add(s)
B = defaultdict(dict)
for r in csv.DictReader(open(sb)):
    if r['loud_LUFS'] not in ('', 'nan'): B[int(r['bar'])][r['stem']] = float(r['loud_LUFS'])
res = []
for s, bs, _, _, txt in mel:
    d = []
    for b in bs:
        if s not in B[b]: continue
        o = [v for k, v in B[b].items() if k != s and k not in mel_at[b] and not k.startswith('Harp') and k != 'drums']
        if o: d.append(B[b][s] - max(o))
    if d: res.append((s, bs[0], float(np.median(d))))
for s, b, d in res: print(f'{s} {b}: {d:+.1f}')
print(f'melodies vs loudest non-melody stem: >= 0 dB in {sum(d >= 0 for _, _, d in res)} of {len(res)}; median {np.median([d for *_, d in res]):+.1f} dB')

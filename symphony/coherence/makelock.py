#!/usr/bin/env python3
"""Write a theme-record .ly from excerpts of a version (used to create themes-scherzo.ly from scherzo/v04).

makelock.py VERSION_DIR OUT.ly NAME:SUFFIX:FIRSTBAR:LASTBAR ... [--beats 4]
Each excerpt becomes a variable, re-barred from bar 1 in 3/4, notes split at barlines with ties,
spelled with sharps (E major / E minor). Occurrence lines (%@) are added by hand afterwards.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lyparse

# quarter beats per bar: 3 for the scherzo; pass --beats 4 for a 2/2 or 4/4 movement
BEATS = int(sys.argv[sys.argv.index('--beats') + 1]) if '--beats' in sys.argv else 3

NAMES = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
DUR = {F(3): '2.', F(2): '2', F(3, 2): '4.', F(1): '4', F(3, 4): '8.', F(1, 2): '8', F(1, 4): '16'}

def lily(p):
    o = p // 12 - 4
    return NAMES[p % 12] + ("'" * o if o > 0 else ',' * -o)

def pieces(length):
    out = []
    while length > 0:
        for d in sorted(DUR, reverse=True):
            if d <= length:
                out.append(DUR[d]); length -= d; break
    return out

def excerpt(vdir, suf, a, b):
    ev = [(bar, beat, p, l) for bar, beat, p, l in lyparse.part_events(vdir, suf) if a <= bar <= b]
    toks, pos = [], F(0)
    def rest_to(target):
        nonlocal pos
        while pos < target:
            bar_end = (pos // BEATS + 1) * BEATS
            seg = min(target, bar_end) - pos
            toks.extend('r' + d for d in pieces(seg)); pos += seg
            if pos % BEATS == 0: toks.append('|')
    for bar, beat, p, l in ev:
        start = (bar - a) * BEATS + beat
        rest_to(start)
        while l > 0:
            bar_end = (pos // BEATS + 1) * BEATS
            seg = min(l, bar_end - pos)
            ds = pieces(seg)
            for i, d in enumerate(ds):
                last = (i == len(ds) - 1) and seg == l
                toks.append(lily(p) + d + ('' if last else '~'))
            pos += seg; l -= seg
            if pos % BEATS == 0: toks.append('|')
    if pos % BEATS: rest_to((pos // BEATS + 1) * BEATS)
    return ' '.join(toks).rstrip(' |')

def main():
    vdir, out = sys.argv[1], sys.argv[2]
    lines = []
    args = [a for i, a in enumerate(sys.argv) if a != '--beats' and (i == 0 or sys.argv[i - 1] != '--beats')]
    for spec in args[3:]:
        name, suf, a, b = spec.split(':')
        lines.append(f"% {name}: {os.path.basename(os.path.normpath(vdir))} {suf} bars {a}-{b}")
        lines.append(f"{name} = {{ {excerpt(vdir, suf, int(a), int(b))} }}\n")
    open(out, 'w').write('\n'.join(lines))

main()

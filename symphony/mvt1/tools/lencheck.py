#!/usr/bin/env python3
"""c420: check that every section variable lasts exactly its sections.txt bar count, in both the score and the part tag sets.
Usage: python3 -I lencheck.py <version-dir>   (prints MISMATCH lines; exit 1 if any)"""
import sys, os, subprocess, tempfile
v = os.path.abspath(sys.argv[1])
secs = [l.split() for l in open(os.path.join(v, 'sections.txt')) if l.strip()]
INSTR = ['FluteOne','FluteTwo','OboeOne','OboeTwo','CorAnglais','ClOne','ClTwo','BassCl','BsnOne','BsnTwo','Cbsn','HnOne','HnTwo',
         'HnThree','HnFour','TptOne','TptTwo','TptThree','TbnOne','TbnTwo','BassTbn','Tuba','Timp','Perc','HarpR','HarpL','VlnOne','VlnTwo','Vla','Vc','Cb']
out = ['\\version "2.24.0"', '\\language "nederlands"', '\\include "global.ily"'] + ['\\include "sections/%s.ily"' % s for s, n in secs]
out.append('#(begin')
for s, n in secs:
    for i in INSTR:
        for keep, drop in (('score', 'part'), ('part', 'score')):
            out.append(f' (let ((v (ly:parser-lookup (quote {s}{i})))) (if (ly:music? v) (let ((l (ly:music-length (removeWithTag (quote {drop}) (ly:music-deep-copy v))))) '
                       f'(if (not (equal? l (ly:make-moment {n} 1))) (ly:message "MISMATCH {keep} {s}{i} ~a whole notes, sections.txt {n}" l)))))')
out.append(' (ly:message "lencheck done"))')
with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, 'lencheck.ly'); open(f, 'w').write('\n'.join(out) + '\n')
    r = subprocess.run(['lilypond', '-dno-point-and-click', '-I', v, '-o', os.path.join(d, 'x'), f], capture_output=True, text=True, cwd=v)
bad = [l for l in r.stderr.splitlines() if 'MISMATCH' in l or 'error' in l.lower()]
print('\n'.join(bad) if bad else 'section lengths: every section variable matches sections.txt (score and part tags)')
sys.exit(1 if bad or 'lencheck done' not in r.stderr else 0)

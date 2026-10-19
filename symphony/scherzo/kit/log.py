#!/usr/bin/env python3
# log.py N "critique entry body" "history entry body"  (third series, 2026-10-19)
# Prepends "# vNEW (cycle N, lens, reading)" to vNEW/critique.md and inserts "## Cycle N" above "## Cycle N-1" in critics/HISTORY.md.
import sys,re
M='/home/user/claude_composes/symphony/scherzo'
n=int(sys.argv[1]); crit=sys.argv[2]; hist=sys.argv[3]
L=['melody','harmony','form','orchestration','engraving','playability','texture','expression','holistic','cyclic'][(n-1)%10]
k=(n-1)%10+1
rd=[l for l in open(M+'/critics/READING.md') if l.startswith(f'| {n} |')][0].split(' | ')[2].rstrip(' |\n')
new=f'v{n+1:02d}'; prev=f'v{n:02d}'
p=f'{M}/{new}/critique.md'; old=open(p).read()
if not old.startswith(f'# {new} '):
    open(p,'w').write(f'# {new} (cycle {n}, lens {k} {L}, {rd})\nCritic report: critics/reports/c{n:03d}.md. {crit}\n\n'+old)
h=open(M+'/critics/HISTORY.md').read()
if f'## Cycle {n} (' not in h:
    i=h.index(f'## Cycle {n-1} (')
    h=h[:i]+f'## Cycle {n} (lens {k} {L}, {rd}) {prev} → {new}\n{hist}\n\n'+h[i:]
    open(M+'/critics/HISTORY.md','w').write(h)
print('logged',n)

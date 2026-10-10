#!/usr/bin/env python3
"""xform.py FILE START END 'VARREGEX' 'python-expr-on-s'  -> splices transformed bars.
expr gets s (bar-range text, bars joined with ' | ') and returns new text."""
import sys, subprocess, re, os
f, a, b, vr, expr = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
d = os.path.dirname(os.path.abspath(__file__))
out = subprocess.run(['python3', f'{d}/showbars.py', f, str(a), str(b)], capture_output=True, text=True).stdout
lines = []
for ln in out.splitlines():
    m = re.match(r'^(\S+) \[\d+\]: (.*)$', ln)
    if not m or not re.fullmatch(vr, m.group(1)): continue
    s = m.group(2); ns = eval(expr, {'re': re, 's': s, 'v': m.group(1)})
    if ns != s: lines.append(f'{m.group(1)} {a} {b} {ns}')
if lines:
    r = subprocess.run(['python3', f'{d}/barsplice.py', f], input='\n'.join(lines)+'\n', text=True, capture_output=True)
    print(r.stdout, r.stderr)
else: print('no change')

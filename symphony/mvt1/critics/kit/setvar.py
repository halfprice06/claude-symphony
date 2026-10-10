"""Replace whole variable definitions in a LilyPond section file.
Usage: setvar.py FILE < defs   (defs: one or more 'name = {...}' blocks; a block ends at a line that is '}' or a one-line def)"""
import sys, re
path = sys.argv[1]
src = open(path).read().split('\n')
defs = sys.stdin.read().strip('\n').split('\n')
# parse new defs into {name: [lines]}
new, cur = {}, None
for ln in defs:
    m = re.match(r'^(\w+) = ', ln)
    if m:
        cur = m.group(1); new[cur] = [ln]
    elif cur:
        new[cur].append(ln)
def span(lines, i):
    if lines[i].rstrip().endswith('}'):
        return i, i
    j = i + 1
    while lines[j].rstrip() != '}':
        j += 1
    return i, j
for name, body in new.items():
    idx = next((i for i, l in enumerate(src) if l.startswith(name + ' = ')), None)
    if idx is None:
        src += body
        print('added', name)
    else:
        a, b = span(src, idx)
        src[a:b + 1] = body
        print('replaced', name)
open(path, 'w').write('\n'.join(src))

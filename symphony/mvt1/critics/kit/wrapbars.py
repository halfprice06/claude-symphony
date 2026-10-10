"""wrapbars.py FILE A B PREFIX SUFFIX VAR [VAR...] : put PREFIX before bar A and SUFFIX after bar B."""
import sys, re
path, a, b, pre, suf = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
names = sys.argv[6:]
s = open(path).read()
def bars_of(body):
    out = []
    for c in body.split('|'):
        c = ' '.join(c.split())
        if not c: continue
        m = re.fullmatch(r'R1\*(\d+)(.*)', c)
        if m: out += ['R1' + m.group(2)] + ['R1'] * (int(m.group(1)) - 1)
        else: out.append(c)
    return out
for n in names:
    m = re.search(r'^(' + n + r' = \{)(.*?)(^\}|\}[ \t]*$)', s, re.S | re.M)
    assert m, n
    bars = bars_of(m.group(2))
    bars[a-1] = pre + ' ' + bars[a-1]
    bars[b-1] = bars[b-1] + ' ' + suf
    body = '\n  '.join(' | '.join(bars[k:k+4]) + ' |' for k in range(0, len(bars), 4))
    s = s[:m.start()] + m.group(1) + '\n  ' + body + '\n}' + s[m.end():]
    print(n, len(bars))
open(path, 'w').write(s)

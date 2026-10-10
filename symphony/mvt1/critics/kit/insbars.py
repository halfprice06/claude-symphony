"""insbars.py FILE AFTER N < spec : insert N bars after bar AFTER in every multi-bar variable
of FILE (R1 in those not given). spec lines: VAR new-bars (separated by |)."""
import sys, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
path, after, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
s = open(path).read()
spec = {}
for line in sys.stdin.read().strip().split('\n'):
    if line.strip():
        v, rest = line.split(None, 1); spec[v] = rest
def bars_of(body):
    out = []
    for c in body.split('|'):
        c = c.strip()
        if not c: continue
        m = re.fullmatch(r'R1\*(\d+)(.*)', c, re.S)
        if m:
            k = int(m.group(1)); out.append('R1' + m.group(2)); out += ['R1'] * (k - 1)
        else: out.append(' '.join(c.split()))
    return out
def join(bars):
    res, i = [], 0
    while i < len(bars):
        if bars[i] == 'R1':
            j = i
            while j < len(bars) and bars[j] == 'R1': j += 1
            res.append('R1' if j - i == 1 else f'R1*{j-i}'); i = j
        else: res.append(bars[i]); i += 1
    return '\n  '.join(' | '.join(res[k:k+4]) + ' |' for k in range(0, len(res), 4))
used = set()
def rep(m):
    name, head, body = m.group(1), m.group(2), m.group(3)
    bars = bars_of(body)
    if len(bars) <= after:
        return m.group(0)
    new = bars_of(spec[name]) if name in spec else ['R1'] * n
    assert len(new) == n, (name, len(new))
    used.add(name)
    bars = bars[:after] + new + bars[after:]
    print(f'{name}: {len(bars)} bars', file=sys.stderr)
    return f'{head}\n  {join(bars)}\n}}'
s = re.sub(r'^((\w+) = (?:\\drummode )?\{)(.*?)(?:^\}|\}[ \t]*$)', lambda m: rep(type('M', (), {'group': lambda self, i: [m.group(0), m.group(2), m.group(1), m.group(3)][i]})()), s, flags=re.S | re.M)
missing = set(spec) - used
assert not missing, missing
open(path, 'w').write(s)

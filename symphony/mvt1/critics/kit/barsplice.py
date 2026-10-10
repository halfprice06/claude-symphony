"""Replace bars START..END (1-based, inclusive) of a LilyPond variable.
Usage: barsplice.py FILE  < spec ; spec lines: VAR START END new-bars-text (bars separated by |)"""
import sys, re
path = sys.argv[1]
s = open(path).read()
def bars_of(body):
    out = []
    for chunk in body.split('|'):
        c = chunk.strip()
        if not c:
            continue
        m = re.fullmatch(r'R1\*(\d+)(.*)', c)
        if m:
            n = int(m.group(1)); out.append('R1' + m.group(2)); out += ['R1'] * (n - 1)
        else:
            out.append(c)
    return out
def join(bars):
    res, i = [], 0
    while i < len(bars):
        if bars[i] == 'R1':
            j = i
            while j < len(bars) and bars[j] == 'R1':
                j += 1
            res.append('R1' if j - i == 1 else f'R1*{j-i}'); i = j
        else:
            res.append(bars[i]); i += 1
    lines = [' | '.join(res[k:k+4]) + ' |' for k in range(0, len(res), 4)]
    return '\n  '.join(lines)
for line in sys.stdin.read().strip().split('\n'):
    if not line.strip():
        continue
    var, a, b, new = line.split(None, 3)
    a, b = int(a), int(b)
    m = re.search(r'^' + var + r' = (\\drummode )?\{(.*?)\n?\}\s*$', s, re.S | re.M)
    m = re.search(r'^(' + var + r' = (?:\\drummode )?\{)(.*?)(^\}|\}\s*$)', s, re.S | re.M)
    assert m, var
    bars = bars_of(m.group(2))
    nb = bars_of(new)
    assert len(nb) == b - a + 1, (var, len(nb), b - a + 1)
    total = len(bars)
    bars[a-1:b] = nb
    body = '\n  ' + join(bars) + '\n'
    s = s[:m.start()] + m.group(1) + body + '}' + s[m.end():]
    if m.group(3).strip() == '}' and not m.group(3).startswith('}'):
        pass
    print(var, 'bars', total, '->', len(bars))
open(path, 'w').write(s)

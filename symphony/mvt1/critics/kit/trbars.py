"""trbars.py FILE START END FROMPITCH TOPITCH : wrap bars START..END of every variable in \\transpose."""
import sys, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
path, a, b, fp, tp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
s = open(path).read()
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
def rep(m):
    head, body = m.group(1), m.group(3)
    if 'drummode' in head: return m.group(0)
    bars = bars_of(body)
    if len(bars) < b: return m.group(0)
    seg = bars[a-1:b]
    if all(x == 'R1' for x in seg): return m.group(0)
    new = bars[:a-1] + [f'\\transpose {fp} {tp} {{ ' + ' | '.join(seg) + ' }'] + bars[b:]
    # the wrapped group counts as several bars; join() treats it as one item
    print(m.group(2), file=sys.stderr)
    return f'{head}\n  {join(new)}\n}}'
s = re.sub(r'^((\w+) = (?:\\drummode )?\{)(.*?)(?:^\}|\}[ \t]*$)', rep, s, flags=re.S | re.M)
open(path, 'w').write(s)

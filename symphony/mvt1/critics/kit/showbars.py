"""showbars.py FILE START END : print bars START..END (1-based) of every variable."""
import sys, re
path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
s = open(path).read()
for m in re.finditer(r'^(\w+) = (?:\\drummode )?\{(.*?)(?:^\}|\}\s*$)', s, re.S | re.M):
    name, body = m.group(1), m.group(2)
    bars = []
    for c in body.split('|'):
        c = ' '.join(c.split())
        if not c: continue
        r = re.fullmatch(r'R1\*(\d+)(.*)', c)
        if r: bars += ['R1'] * int(r.group(1))
        else: bars.append(c)
    sel = bars[a-1:b]
    if all(x == 'R1' for x in sel): continue
    print(f'{name} [{len(bars)}]: ' + ' | '.join(sel))

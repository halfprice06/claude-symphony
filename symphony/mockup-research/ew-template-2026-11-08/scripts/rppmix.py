"""Mix routing for an RPP: for each track from index START print vol/pan, main send, receives (with source names), FX list.
Usage: python3 -I rppmix.py file.rpp START"""
import sys, re, math
lines = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\n'); START = int(sys.argv[2])
tracks = []; stack = []
for i, l in enumerate(lines):
    s = l.strip()
    if s.startswith('<'): stack.append((s.split()[0], i))
    elif s == '>':
        tag, st = stack.pop()
        if tag == '<TRACK': tracks.append((st, i))
tracks.sort()
db = lambda v: -150 if v <= 0 else 20 * math.log10(v)
info = []
for idx, (st, en) in enumerate(tracks):
    d = dict(name=None, vol=1, pan=0, main=None, aux=[], fx=[], offs=None, items=0)
    depth = 0
    for l in lines[st+1:en]:
        s = l.strip()
        if s.startswith('<'): depth += 1
        if depth == 0:
            if s.startswith('NAME ') and d['name'] is None: d['name'] = s[5:].strip('"')
            elif s.startswith('VOLPAN '): p = s.split(); d['vol'] = float(p[1]); d['pan'] = float(p[2])
            elif s.startswith('MAINSEND '): d['main'] = s.split()[1]
            elif s.startswith('PLAYOFFS '): d['offs'] = s
            elif s.startswith('AUXRECV '): p = s.split(); d['aux'].append((int(p[1]), int(p[2]), float(p[3]), float(p[4]), p[8]))
        if depth == 1 and re.match(r'<(VST|AU|JS)\b', s):
            m = re.match(r'<\w+ "([^"]*)"', s) or re.match(r'<JS (\S+)', s); d['fx'].append(m.group(1) if m else s[:50])
        if depth == 1 and s.startswith('<ITEM'): d['items'] += 1
        if s == '>': depth -= 1
    info.append(d)
for i, t in enumerate(info):
    if i < START: continue
    print(f"[{i}] {t['name']}: {db(t['vol']):+.1f} dB pan {t['pan']:+.2f} main={t['main']} items={t['items']} {t['offs'] or ''} fx: {', '.join(f.replace('AU: ', '') for f in t['fx'])}")
    for a in t['aux']:
        print(f"     <- [{a[0]}] {info[a[0]]['name']} {db(a[2]):+.1f} dB pan {a[3]:+.2f} mode {a[1]} chan {a[4]}")

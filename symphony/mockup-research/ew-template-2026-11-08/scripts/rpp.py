import sys, re, math, base64
lines = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\n')
# build tracks: (start,end,name,depth)
tracks=[]; stack=[]
for i,l in enumerate(lines):
    s=l.strip()
    if s.startswith('<'):
        stack.append((s.split()[0], i))
    elif s=='>':
        tag,st=stack.pop()
        if tag=='<TRACK': tracks.append((st,i))
tracks.sort()
def db(v): return -150 if v<=0 else 20*math.log10(v)
info=[]
for idx,(st,en) in enumerate(tracks):
    seg=lines[st:en]
    # only top-level props of this track (indent 4)
    name=vol=pan=None; isbus=None; aux=[]; fx=[]
    for l in seg:
        if l.startswith('    NAME ') and name is None: name=l[9:].strip('"')
        elif l.startswith('    VOLPAN '): p=l.split(); vol=float(p[1]); pan=float(p[2])
        elif l.startswith('    ISBUS '): isbus=l.split()[1:]
        elif l.startswith('    AUXRECV '): p=l.split(); aux.append((int(p[1]),int(p[2]),float(p[3]),float(p[4])))
        elif l.startswith('      <VST ') or l.startswith('      <JS ') or l.startswith('      <AU '):
            m=re.match(r'\s*<\w+ "([^"]*)"',l) or re.match(r'\s*<JS (\S+)',l); fx.append(m.group(1) if m else l.strip()[:60])
    info.append(dict(i=idx,name=name,vol=vol,pan=pan,isbus=isbus,aux=aux,fx=fx,st=st,en=en))
for t in info:
    print(f"[{t['i']:2}] {t['name'][:38]:38} vol {db(t['vol']):+6.1f} dB pan {t['pan']:+.2f} bus {' '.join(t['isbus'] or [])} fx: {', '.join(f.replace('VST3i: ','').replace('VST3: ','').replace('VST: ','') for f in t['fx'])}")
    for a in t['aux']:
        print(f"      <- recv from [{a[0]}] {info[a[0]]['name'][:30]} at {db(a[2]):+.1f} dB mode {a[1]}")

import sys, re, base64, binascii
lines = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\n')
want = sys.argv[2]  # substring of FX name
maxn = int(sys.argv[3]) if len(sys.argv)>3 else 3
trackname=None; n=0; i=0
while i < len(lines):
    l=lines[i]
    if l.startswith('    NAME '): trackname=l[9:]
    if re.match(r'\s*<VST ',l) and want in l:
        j=i+1; b=[]
        while lines[j].strip()!='>':
            b.append(lines[j].strip()); j+=1
        raw=b''
        for s in b:
            try: raw+=base64.b64decode(s+'='*(-len(s)%4))
            except binascii.Error: pass
        strs=re.findall(rb'[\x20-\x7e]{5,}', raw)
        print(f'=== {trackname} :: {l.strip()[:50]} bytes={len(raw)}')
        for s in strs[:int(sys.argv[4]) if len(sys.argv)>4 else 60]: print('   ', s.decode()[:200])
        n+=1
        if n>=maxn: break
        i=j
    i+=1

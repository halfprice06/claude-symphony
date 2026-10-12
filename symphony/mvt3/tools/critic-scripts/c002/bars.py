import re,sys
f=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3])  # local bar indices 1-based
src=open(f).read()
src=re.sub(r'%[^\n]*','',src)
for m in re.finditer(r'(\w+)\s*=\s*(?:\\drummode\s*)?\{(.*?)\}\s*(?=\n\w|\Z)',src,re.S):
    body=' '.join(m.group(2).split())
    bars=[x.strip() for x in body.split('|')]
    # expand R1*n
    ex=[]
    for x in bars:
        mm=re.fullmatch(r'R1\*(\d+)(\\!)?',x)
        if mm: ex+=['R1']*int(mm.group(1))
        else: ex.append(x)
    print(f"{m.group(1):22s}", ' | '.join(ex[a-1:b]))

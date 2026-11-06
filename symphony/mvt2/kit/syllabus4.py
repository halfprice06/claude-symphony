# Fourth series (cycles 401-599), 2026-10-31: for each lens, every reading used in cycles 1-399, least recently used first.
# Cycle 400 (already listed) and cycle 599 are release checks. Appends rows to critics/READING.md.
import re
P='/home/user/claude_composes/symphony/mvt2/critics/READING.md'
s=open(P).read(); last={}; 
for m in re.finditer(r'^\| (\d+) \| (\d+) \| (.*) \|$', s, re.M):
    c,k,r=int(m[1]),int(m[2]),m[3]
    if c>=400 or 'Release check' in r: continue
    r=re.sub(r' \((second|third) series\)$','',r)
    last.setdefault(k,{})[r]=c
order={k:[r for r,_ in sorted(d.items(), key=lambda x:x[1])] for k,d in last.items()}
rows=[]; idx={k:0 for k in order}
for c in range(401,600):
    k=(c-1)%10+1
    if c==599: r='Release check: every do-not-touch item in HISTORY.md, every change in cycles 400-598, and every book rule cited in them'
    else: r=order[k][idx[k]%len(order[k])]; idx[k]+=1
    rows.append(f'| {c} | {k} | {r} (fourth series) |')
s=s.replace('cycles 1-400','cycles 1-600',1).rstrip('\n')+'\n'+'\n'.join(rows)+'\n'
open(P,'w').write(s)
print({k:len(v) for k,v in order.items()})

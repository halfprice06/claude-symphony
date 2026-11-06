# Fourth series fix (2026-10-31, after cycle 417): syllabus4.py treated "X (second pass)" and "X" as different readings, so some
# readings came back within a few cycles. Rows 418-598 are rebuilt: per lens, one entry per book page range, least recently used
# (anywhere, any lens) first, never two lenses on the same pages in the same pass. Rows 400-417 and 599 are kept.
import re
P='/home/user/claude_composes/symphony/mvt2/critics/READING.md'
s=open(P).read()
rows=[(int(m[1]),int(m[2]),m[3]) for m in re.finditer(r'^\| (\d+) \| (\d+) \| (.*) \|$', s, re.M)]
def key(r): return tuple(re.findall(r'([\w-]+\d?) PDF ([\d-]+)', r)) or (r[:40],)
def clean(r): return re.sub(r'( \((second|third|fourth) series\)| \(second pass\))+$','',r)
last={}; cand={}
for c,k,r in rows:
    if c>417: continue
    if 'Release check' in r: continue
    kk=key(r); last[kk]=c
    cand.setdefault(k,{})[kk]=clean(r)
order={k:sorted(d, key=lambda kk:last[kk]) for k,d in cand.items()}
used=set(); new={}
for c in range(418,599):
    k=(c-1)%10+1
    for kk in order[k]:
        if kk not in used: break
    else:
        used-= set(order[k]); kk=order[k][0]
    used.add(kk); order[k].remove(kk); order[k].append(kk)
    new[c]=f'| {c} | {k} | {cand[k][kk]} (fourth series) |'
out=[]
for line in s.split('\n'):
    m=re.match(r'^\| (\d+) \|',line)
    out.append(new.get(int(m[1]),line) if m else line)
open(P,'w').write('\n'.join(out))

import csv, sys, numpy as np, re
from collections import defaultdict
bars_csv=sys.argv[1]; notes=sys.argv[2]
def key(n):
    k=re.sub(r"[^A-Za-z0-9 ]","",n.split(":")[0]).strip(); return k or "drums"
B=defaultdict(dict)
for r in csv.DictReader(open(bars_csv)): B[int(r['bar'])][r['stem']]=(float(r['loud_LUFS']),r['dyn'])
N=defaultdict(set)
for r in csv.DictReader(open(notes)): N[key(r['staff'])].add(int(r['bar']))
P=[("Cor anglais",5,"espr."),("Violas",19,"espr."),("Bassoons 12",33,"espr."),("Horns 12",47,"1. dolce"),("Violoncellos",47,"dolce"),
 ("Violins I",55,"molto cantabile"),("Violins II",55,"molto cantabile"),("Clarinets 12",56,"espr."),("Horns 12",56,"espr."),("Flutes 12",73,"espr."),
 ("Bassoons 12",77,"espr."),("Flutes 12",107,"espr."),("Violas",107,"espr."),("Bass clarinet",107,"espr."),("Oboes 12",145,"dolce"),("Horns 12",146,"dolce"),
 ("Violas",146,"dolce"),("Violoncellos",146,"dolce"),("Violoncellos",171,"espr."),("Cor anglais",171,"espr.")]
out=[]
for st,b0,txt in P:
    bs=[]; b=b0
    while b in N[st] and len(bs)<8: bs.append(b); b+=1
    d_max=[];d_sum=[];who=[]
    for b in bs:
        if st not in B[b]: continue
        m=B[b][st][0]; oth={k:v for k,v in B[b].items() if k!=st and not k.startswith('Harp')|(k=='drums')}
        if not oth: continue
        k2=max(oth,key=lambda k:oth[k][0]); d_max.append(m-oth[k2][0]); who.append(f"{k2}({oth[k2][1]})")
        d_sum.append(m-10*np.log10(sum(10**(v[0]/10) for v in oth.values())))
    if d_max:
        mdyn=B[bs[0]].get(st,(0,''))[1]
        out.append((st,txt,f"{bs[0]}-{bs[-1]}",mdyn,np.median(d_max),np.median(d_sum),max(set(who),key=who.count)))
print("| melody (mark) | bars | printed dyn of melody | melody minus loudest other stem, median dB | melody minus sum of all other stems, dB | loudest other stem (its dyn) |")
print("|---|---|---|---|---|---|")
for o in out: print(f"| {o[0]} ({o[1]}) | {o[2]} | {o[3]} | {o[4]:+.1f} | {o[5]:+.1f} | {o[6]} |")

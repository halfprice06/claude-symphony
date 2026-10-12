from g import *
import re
exec(open('pOne.py').read().split("mA=")[0])   # mel, H, bars, vc, cb
mA=" | ".join(mel.split(" | ")[:8])+" |"
mB=mel.split(" | ",8)[8]
def dyn(x,d="\\ff"):
    return re.sub(r"(->\()",lambda m:m.group(1)+d,x,count=1)
def pat(ch,lo,hi):
    ps=place(ch,lo,hi)[:3]
    return f"{ps[0]}8( {ps[1]} {ps[2]} {ps[1]})"
def pats(lo,hi):
    r=[]
    for b in bars:
        r.append(" ".join("r2" if h[1] is None else pat(h[1],lo,hi) for h in b))
    return r
def offb(lo,hi,pick):
    r=[]
    for b in bars:
        seg=[]
        for h in b:
            if h[1] is None: seg.append("r2"); continue
            ps=place(h[1],lo,hi); seg.append(f"r4 {ps[min(pick,len(ps)-1)]}4-.")
        r.append(" ".join(seg))
    return r
def held(lo,hi,pick):
    r=[]
    for b in bars:
        n=[]
        for h in b:
            if h[1] is None: n.append(None); continue
            ps=place(h[1],lo,hi); n.append(ps[min(pick,len(ps)-1)])
        if n[1] is None: r.append(f"{n[0]}2 r2")
        elif n[0]==n[1]: r.append(f"{n[0]}1")
        else: r.append(f"{n[0]}2 {n[1]}2")
    return r
def first(L,d):
    L=list(L); L[0]=re.sub(r"(\d)",lambda m:m.group(1)+d,L[0],count=1); return L
link={}
link['VlnOne']="r4 es'''8(\\f d''' c''' bes'' aes'' g'' | f''8 g'' aes'' f'' d''4) r4 | r4 d''8(\\> c'' b' aes' g' f' | d'1)\\p |"
link['VlnTwo']="r4 es''8(\\f d'' c'' bes' aes' g' | f'8 g' aes' f' d'4) r4 | r4 f'8(\\> es' d' c' b aes | g1)\\p |"
link['Vla']="c'1\\f | c'1\\> | d'1 | d'1\\p |"
link['Vc']="aes,1\\f | d1\\> | b,1~ | b,1\\p |"
link['Cb']="aes,,1\\f | d,1\\> | b,,1~ | b,,1\\p |"
link['BsnTwo']="aes,1\\f | d1\\> | b,1~ | b,1\\p |"
link['BsnOne']="es1\\f | f1\\> | f1~ | f1\\p |"
link['ClOne']="c''1\\f | aes'1\\> | aes'1~ | aes'1\\p |"
link['ClTwo']="es'1\\f | f'1\\> | f'1~ | f'1\\p |"
link['HnOne']="c''1\\f | aes'1\\> | g'1~ | g'2. r4\\p |"
link['HnTwo']="es'1\\f | f'1\\> | d'1~ | d'2. r4\\p |"
O={}
O['VlnOne']=dyn(mA)+" "+mB
O['VlnTwo']=dyn(mA)+" "+shift(mB,-1)
O['FluteOne']=dyn(shift(mA,1))+" "+mB
O['FluteTwo']=dyn(mA)+" "+mB
O['OboeOne']=dyn(mA)+" "+mB
O['OboeTwo']=dyn(mA)+" "+shift(mB,-1)
O['ClOne']=dyn(mA)+" "+shift(mB,-1)
O['ClTwo']=dyn(mA)+" "+shift(mB,-1)
low=shift(mA,-1)+" "+shift(mB,-2)
O['Vla']=dyn(low).replace("es4( d8 c8 b,4 d4) | c2-> r2","es'4( d'8 c'8 b4 d'4) | c'2-> r2")
O['HnOne']=dyn(low); O['HnTwo']=dyn(low)
O['HnThree']=" | ".join(first(offb(60,70,0),"\\f"))+" |"
O['HnFour']=" | ".join(first(offb(53,64,0),"\\f"))+" |"
O['TptOne']=" | ".join(first(offb(67,76,0),"\\f"))+" |"
O['TptTwo']=" | ".join(first(offb(62,71,0),"\\f"))+" |"
O['TptThree']=" | ".join(first(offb(58,67,0),"\\f"))+" |"
O['TbnOne']=" | ".join(first(held(55,64,1),"\\f"))+" |"
O['TbnTwo']=" | ".join(first(held(50,60,0),"\\f"))+" |"
vcf=vc.replace("\\f","\\ff"); cbf=cb.replace("\\f","\\ff")
O['Vc']=vcf; O['Cb']=cbf; O['BsnTwo']=vcf; O['BsnOne']=vcf
O['BassTbn']=vcf.replace("\\ff","\\f"); O['Cbsn']=cbf
O['Tuba']=" | ".join(cbf.split(" | ")[8:16]); O['Tuba']="R1*8 | "+O['Tuba']
O['Timp']="c4->\\ff r4 r2 | R1*3 | c4-> r4 r2 | R1*2 | g,4-> g,4 g,4 r4 | c4-> r4 r2 | R1*3 | c4-> r4 r2 | R1 | g,4 r4 g,4 r4 | aes,4-> r4 r2 |"
O['Timp']+=" aes,4\\f r4 r2 | R1*3 |"
insts=['FluteOne','FluteTwo','OboeOne','OboeTwo','ClOne','ClTwo','BsnOne','BsnTwo','Cbsn','HnOne','HnTwo','HnThree','HnFour','TptOne','TptTwo','TptThree','TbnOne','TbnTwo','BassTbn','Tuba','Timp','VlnOne','VlnTwo','Vla','Vc','Cb']
out=["% RECAPITULATION, bars 151-170: theme F1 ff, fuller than at 11 (flutes and oboes on the tune from the start, trumpets and horns 3-4",
"% off the beat, trombones holding the harmony, tuba on the bass of the consequent). Deceptive cadence at 166 as at 26.",
"% 167-170: link, VI - iiø6/5 - V6/5, diminuendo to p: the second theme in C minor follows from the inverted V (no root V-i in C).",""]
for i in insts:
    b=O.get(i,"R1*16 |")
    if i=='Timp': out.append(f"recP{i} = {{ {b} }}"); continue
    out.append(f"recP{i} = {{ {b} {link.get(i,'R1*4 |')} }}")
txt="\\version \"2.24.0\"\n"+"\n".join(out)+"\n"
txt=re.sub(r'r4\\f (\S+?)4-\.',lambda m:'r4 '+m.group(1)+'4-.\\f',txt)
open('/tmp/m3/v01/sections/recP.ily','w').write(txt)

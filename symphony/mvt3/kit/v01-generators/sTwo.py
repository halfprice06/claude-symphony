from g import *
import re
melA="bes''2.( g''4 | f''4 es''4 g''4 bes''4 | es'''2. d'''4 | c'''2 bes''2) | aes''2.( c'''4 | bes''4 aes''4 g''4 f''4 | g''2 es''2 | f''1) |"
melB="bes''2.( g''4 | f''4 es''4 g''4 bes''4\\< | es'''2. f'''4 | g'''2\\f f'''2) | es'''2.( d'''4 | c'''4 bes''4 aes''4 g''4\\> | f''2 d''2 | es''1)\\mf |"
ctr=("g2(\\mf^\\markup \\italic \"espress.\" aes4 bes4 | aes2 g2) | c'2( es'4 d'4 | c'2 bes2) | aes2( c'4 es'4 | d'2 aes2) | g2( bes4 aes4 | aes2 f2) | "
     "g2( aes4 bes4 | aes2 g2) | bes2( c'4 f'4 | es'2 d'2) | c'2( aes4 c'4 | es'2 d'2) | aes2( f2 | g1) |")
bass="es1 | d2 es2 | c1 | aes,2 g,2 | f,1 | bes,1 | es2 c2 | bes,1 | g,2 es2 | d2 es2 | g,2 aes,2 | c2 d2 | aes,1 | aes,2 bes,2 | bes,1 | es1 |"
H=[['es','g','bes'],['es','g','bes'], ['bes','d','f','aes'],['es','g','bes'], ['aes','c','es'],['aes','c','es'], ['aes','c','es'],['es','g','bes'],
   ['f','aes','c','es'],['f','aes','c','es'], ['bes','d','f'],['bes','d','f','aes'], ['es','g','bes'],['c','es','g'], ['bes','d','f'],['bes','d','f','aes'],
   ['es','g','bes'],['es','g','bes'], ['bes','d','f','aes'],['es','g','bes'], ['es','g','bes'],['aes','c','es','f'], ['c','es','g'],['bes','d','f'],
   ['aes','c','es'],['aes','c','es'], ['aes','c','es'],['bes','d','f'], ['bes','d','f','aes'],['bes','d','f','aes'], ['es','g','bes'],['es','g','bes']]
bars=[H[i:i+2] for i in range(0,32,2)]
bl=[b.strip() for b in bass.split("|") if b.strip()]
def harp():
    R=[];L=[]
    for i,b in enumerate(bars):
        rs=[]
        for ch in b:
            ps=place(ch,63,82)[:4]
            rs.append(" ".join(f"{p}8" for p in ps))
        R.append(" ".join(rs))
        # LH: bass notes from bass line, an octave lower, as halves/whole
        L.append(shift(bl[i],-1))
    return R,L
R,L=harp()
R[0]=R[0].replace("8","8\\mf",1) if False else R[0]
L[0]=re.sub(r"(\d)",lambda m:m.group(1)+"\\mf",L[0],count=1)
def offb(lo,hi,idx):
    r=[]
    for b in bars:
        seg=[]
        for ch in b:
            ps=place(ch,lo,hi); seg.append(f"r4 {chord(ps[idx:idx+2])}4")
        r.append(" ".join(seg))
    return r
va=offb(55,67,0); va[0]=va[0].replace("4 ","4\\p^\\markup \\italic \"arco\" ",1).replace("r4\\p^\\markup \\italic \"arco\" ","r4 ",1)
va[0]=va[0].replace("4 r4","4\\p^\\markup \\italic \"arco\" r4",1)
def held(lo,hi,pick):
    r=[]
    for b in bars:
        n=[]
        for ch in b:
            ps=place(ch,lo,hi); n.append(ps[min(pick,len(ps)-1)])
        r.append(f"{n[0]}1" if n[0]==n[1] else f"{n[0]}2 {n[1]}2")
    return r
c1=held(62,72,0); c2=held(56,67,0); b1=held(48,58,0); h1=held(60,70,0); h2=held(55,65,0)
for L_ in (c1,c2,b1): L_[0]=re.sub(r"(\d)",lambda m:m.group(1)+"\\pp",L_[0],count=1)
for L_ in (h1,h2): L_[8]=re.sub(r"(\d)",lambda m:m.group(1)+"\\p",L_[8],count=1)
out=["% SECOND THEME IN MAJOR, bars 67-82, E flat major: theme F2 in the violins in octaves (Vln I at G6 at most, 78; movement III's",
"% C7 is kept for the C-major arrival at 219), the cellos' counter-melody (the bass counterline movement I lacked), harp broken chords,",
"% violas off the beat. Flute 1 and oboe 1 join the tune from 77 for its climax. 81-82 animando into the closing group.",""]
out.append("sTwoVlnOne = { "+melA.replace("2.(","2.(\\mf^\\markup \\italic \"arco, cantabile\"",1)+" "+melB+" }")
out.append("sTwoVlnTwo = { "+shift(melA,-1).replace("2.(","2.(\\mf^\\markup \\italic \"arco\"",1)+" "+shift(melB,-1)+" }")
out.append("sTwoFluteOne = { R1*10 | "+" | ".join(melB.split(" | ")[2:]).replace("2.","2.(\\mp",1)+" }")
out.append("sTwoOboeOne = { R1*10 | "+" | ".join(shift(melB,-1).split(" | ")[2:]).replace("2.","2.(\\mp",1)+" }")
out.append("sTwoVc = { "+ctr+" }")
out.append("sTwoVla = { "+" | ".join(va)+" | }")
out.append("sTwoCb = { "+re.sub(r"(\d)",lambda m:m.group(1)+"\\mf^\\markup \\italic \"arco\"",shift(bass,-1),count=1)+" }")
out.append("sTwoBsnTwo = { "+re.sub(r"(\d)",lambda m:m.group(1)+"\\pp",bass,count=1)+" }")
out.append("sTwoHarpR = { "+" | ".join(R)+" | }")
out.append("sTwoHarpL = { "+" | ".join(L)+" | }")
out.append("sTwoClOne = { "+" | ".join(c1)+" | }")
out.append("sTwoClTwo = { "+" | ".join(c2)+" | }")
out.append("sTwoBsnOne = { "+" | ".join(b1)+" | }")
out.append("sTwoHnOne = { R1*8 | "+" | ".join(h1[8:])+" | }")
out.append("sTwoHnTwo = { R1*8 | "+" | ".join(h2[8:])+" | }")
open('/tmp/m3/v01/sections/sTwo.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")

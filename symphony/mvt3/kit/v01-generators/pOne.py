from g import *
# FIRST THEME (theme F1), bars 11-26
mel = ("c''2->( g'4. aes'8 | bes'4-.) aes'8( g'8 f'4-.) es'4-. | d'4( g'8 aes'8 b'4 d''4) | f''2-> es''4( d''4) | "
       "es''2->( bes'4. c''8 | des''4-.) c''8( bes'8 aes'4-.) g'4-. | f'4( aes'8 c''8 f''4 aes''4) | g''2.-> r4 | "
       "c'''2->( g''4. aes''8 | bes''4-.) aes''8( g''8 f''4-.) es''4-. | d''4( f''8 aes''8 b''4 d'''4) | f'''2-> es'''4( d'''4) | "
       "es'''2->( d'''4. c'''8 | b''4-.) c'''8( d'''8 g''4-.) f''4-. | es''4( d''8 c''8 b'4 d''4) | c''2-> r2 |")
# harmony per half bar: (bass, chord pcs)
H=[('c',['c','es','g']),('es',['c','es','g']),
   ('d',['bes','d','f']),('aes,',['f','aes','c']),
   ('g,',['g','b','d','f']),('g,',['g','b','d','f']),
   ('b,',['g','b','d','f']),('g,',['g','b','d']),
   ('c',['c','es','g']),('g,',['es','g','bes']),
   ('f',['f','aes','des']),('aes,',['f','aes','c']),
   ('f,',['f','aes','c']),('d',['d','f','aes','c']),
   ('g,',['g','b','d']),(None,None),
   ('c',['c','es','g']),('es',['c','es','g']),
   ('d',['bes','d','f']),('aes,',['f','aes','c']),
   ('g,',['g','b','d','f']),('g,',['g','b','d','f']),
   ('b,',['g','b','d','f']),('g,',['g','b','d']),
   ('c',['c','es','g']),('f',['f','aes','c','d']),
   ('g',['g','b','d']),('g,',['g','b','d','f']),
   ('g,',['g','b','d','f']),('g,',['g','b','d','f']),
   ('aes,',['aes','c','es']),(None,None)]
bars=[H[i:i+2] for i in range(0,32,2)]
# viola: broken chords in eighths, x y z y per half bar, register G3-D5
def vla_half(ch):
    ps=place(ch,55,70)[:3]
    if len(ps)<3: ps=place(ch,55,74)[:3]
    return f"{ps[0]}8 {ps[1]} {ps[2]} {ps[1]}"
vla=[]
for b in bars:
    if b[1][1] is None:
        vla.append(f"{vla_half(b[0][1]).replace('8','8',1)} r2" if b[0][1] else "R1")
    else:
        vla.append(vla_half(b[0][1])+" "+vla_half(b[1][1]))
vla[0]=vla[0].replace("8","8\\f",1)
# woodwind off-beat chords (beats 2 and 4): Cl 1 (top), Cl 2, Bsn 1 (bottom) from chord pcs within registers
def offb(ch,lo,hi,idx):
    ps=place(ch,lo,hi)
    return ps[min(idx,len(ps)-1)]
cl1=[];cl2=[];bs1=[]
for b in bars:
    seg1=[];seg2=[];seg3=[]
    for half in b:
        if half[1] is None:
            seg1.append("r2");seg2.append("r2");seg3.append("r2");continue
        ch=half[1]
        a=place(ch,65,76); bb=place(ch,58,67); cc=place(ch,48,58)
        seg1.append(f"r4 {a[0]}4-.");seg2.append(f"r4 {bb[0]}4-.");seg3.append(f"r4 {cc[-1]}4-.")
    cl1.append(" ".join(seg1));cl2.append(" ".join(seg2));bs1.append(" ".join(seg3))
cl1[0]=cl1[0].replace("4-.","4-.\\mf",1);cl2[0]=cl2[0].replace("4-.","4-.\\mf",1);bs1[0]=bs1[0].replace("4-.","4-.\\mf",1)
# bass line (Vc): half notes with quarter motion at cadences
vc=("es2\\f c2 | d2 f,2 | g,4 g4 f4 d4 | b,2 g,2 | c2 g,2 | f2 d2 | f,2 d2 | g,2 g,4 r4 | "
    "es2 c2 | d2 f,2 | g,4 g4 f4 d4 | b,2 g,2 | c2 f2 | g4 f4 es4 d4 | g,2 g,2 | aes,2-> r2 |")
cb=("es,2\\f c,2 | d,2 f,,2 | g,,2 r4 g,,4 | b,,2 g,,2 | c,2 g,,2 | f,2 d,2 | f,,2 d,2 | g,,2 g,,4 r4 | "
    "es,2 c,2 | d,2 f,,2 | g,,2 r4 g,,4 | b,,2 g,,2 | c,2 f,2 | g,2 g,,2 | g,,2 g,,2 | aes,,2-> r2 |")

mA=" | ".join(mel.split(" | ")[:8])+" |"
mB=mel.split(" | ",8)[8]
def dyn(x,d="\\f"):
    return re.sub(r"(->\()",r"\1"+d.replace("\\","\\\\"),x,count=1)
import re
def pat(ch,lo,hi):
    ps=place(ch,lo,hi)[:3]
    return f"{ps[0]}8( {ps[1]} {ps[2]} {ps[1]})"
def pats(lo,hi):
    r=[]
    for b in bars:
        segs=[]
        for half in b:
            segs.append("r2" if half[1] is None else pat(half[1],lo,hi))
        r.append(" ".join(segs))
    return r
c1=pats(62,77); c2=pats(55,70)
c1[0]=c1[0].replace("8(","8(\\mf",1); c2[0]=c2[0].replace("8(","8(\\mf",1)
out=["% FIRST THEME (theme F1), bars 11-26, C minor, f. Strings with brass on the tune (cyclic-notes: the first theme does not start",
"% in the clarinet or a solo violin, and does not open with a rising sixth): 11-18 violins in unison, violas and horns 1-2 an octave lower;",
"% 19-26 Vln I an octave higher (with Fl 1), Vln II (with Ob 1) at the first octave, violas and horns 1-2 below.",
"% Antecedent 11-18 ends on V (half cadence); consequent 19-26 ends with a deceptive cadence V-VI at 26: no root-position V-i in C",
"% before the last cadence of the symphony (cyclic-notes: movement I has none after its bar 135).",
"% Clarinets: broken chords in eighths; horns 3-4 and bassoon 1: off-beat chords; cellos, basses and bassoon 2: the bass line.",""]
out.append("pOneVlnOne = { "+dyn(mA)+" "+mB+" }")
out.append("pOneVlnTwo = { "+dyn(mA)+" "+shift(mB,-1)+" }")
low=shift(mA,-1)+" "+shift(mB,-2)
vl=dyn(low).replace("es4( d8 c8 b,4 d4) | c2-> r2","es'4( d'8 c'8 b4 d'4) | c'2-> r2"); out.append("pOneVla = { "+vl+" }")
out.append("pOneHnOne = { "+dyn(low)+" }")
out.append("pOneHnTwo = { "+dyn(low)+" }")
out.append("pOneFluteOne = { R1*8 | "+dyn(mB)+" }")
out.append("pOneOboeOne = { R1*8 | "+dyn(shift(mB,-1))+" }")
out.append("pOneClOne = { "+" | ".join(c1)+" | }")
out.append("pOneClTwo = { "+" | ".join(c2)+" | }")
hn3=[];hn4=[];b1=[]
for b in bars:
    s3=[];s4=[];s5=[]
    for half in b:
        if half[1] is None: s3.append("r2");s4.append("r2");s5.append("r2");continue
        a=place(half[1],60,70); bb=place(half[1],53,64); cc=place(half[1],48,58)
        s3.append(f"r4 {a[0]}4-."); s4.append(f"r4 {bb[0]}4-."); s5.append(f"r4 {cc[-1]}4-.")
    hn3.append(" ".join(s3));hn4.append(" ".join(s4));b1.append(" ".join(s5))
for L in (hn3,hn4,b1): L[0]=L[0].replace("4-.","4-.\\mf",1)
out.append("pOneHnThree = { "+" | ".join(hn3)+" | }")
out.append("pOneHnFour = { "+" | ".join(hn4)+" | }")
out.append("pOneBsnOne = { "+" | ".join(b1)+" | }")
out.append("pOneVc = { "+vc+" }")
out.append("pOneCb = { "+cb+" }")
out.append("pOneBsnTwo = { "+vc+" }")
out.append("pOneCbsn = { R1*8 | "+" | ".join(cb.split(" | ")[8:16])+" }")
out.append("pOneTimp = { c4->\\f r4 r2 | R1*3 | c4-> r4 r2 | R1*2 | g,4-> g,4 g,4 r4 | c4-> r4 r2 | R1*3 | c4-> r4 r2 | R1 | g,4 r4 g,4 r4 | aes,4-> r4 r2 | }")
open('/tmp/m3/v01/sections/pOne.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")

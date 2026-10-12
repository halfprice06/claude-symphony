from g import *
import re
# COUNTERSTATEMENT, bars 27-42: F1 in the bass (Vc, Vla, Bsn, Hn 3-4), violins' running countersubject; to A flat (35), B flat minor (37), V of E flat (39-42)
theme=("c'2->( g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | "
       "es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 |")
# halves: chord pcs, scale for runs
Cm=['c','d','es','f','g','aes','bes']; CmV=['c','d','es','f','g','aes','b']
Ab=['aes','bes','c','des','es','f','g']; Bbm=['bes','c','des','es','f','ges','aes']; BbM=['bes','c','d','es','f','g','aes']
H=[(['c','es','g'],Cm),(['g','b','d'],CmV),(['bes','d','f'],Cm),(['f','aes','c'],Cm),
   (['g','b','d','f'],CmV),(['g','b','d','f'],CmV),(['g','b','d','f'],CmV),(['c','es','g'],Cm),
   (['c','es','g'],Cm),(['es','g','bes'],Cm),(['des','f','aes'],Cm),(['f','aes','c'],Cm),
   (['f','aes','c'],Cm),(['d','f','aes','c'],Cm),(['g','b','d'],CmV),(['g','b','d'],CmV),
   (['aes','c','es'],Ab),(['aes','c','es'],Ab),(['es','g','bes','des'],Ab),(['aes','c','es'],Ab),
   (['bes','des','f'],Bbm),(['bes','des','f'],Bbm),(['f','a','c','es'],['f','g','a','bes','c','d','es']),(['bes','d','f'],BbM),
   (['bes','d','f'],BbM),(['bes','d','f'],BbM),(['bes','d','f','aes'],BbM),(['bes','d','f','aes'],BbM),
   (['bes','d','f','aes'],BbM),(['bes','d','f','aes'],BbM),(['bes','d','f','aes'],BbM),(['bes','d','f','aes'],BbM)]
vln1=open('pTwo_vln1.txt').read().strip()
# 35-42 violins: head in A flat (35-36), B flat minor (37-38), then descending, dim. over V of E flat (39-42)
vln1b=("aes''2->( es''4. f''8 | g''4-.) f''8( es''8 des''4-.) c''4-. | bes''2->( f''4. ges''8 | aes''4-.) ges''8( f''8 es''4-.) d''4-. | "
       "f''2->(\\> bes'4. c''8 | d''4-.) c''8( bes'8 aes'4-.) g'4-. | f'2( d'4. es'8 | f'2.)\\mf r4 |")
out=["% COUNTERSTATEMENT, bars 27-42, ff. Theme F1 in the bass (cellos, violas, bassoons, horns 3-4; basses an octave lower);",
"% the violins play a running countersubject in eighths (Adler part 2 PDF 172-186: polyphonic texture, foreground and counterline).",
"% 35-38: the head in the violins in A flat, then B flat minor; 39-42: V of E flat, diminuendo into the transition.",
"% Woodwinds and horns 1-2 hold the harmony; trombones join at 35. No repeated-eighth hammering in the basses: that layout is",
"% movement I's first-theme tutti and is kept for the coda (cyclic-notes 'Owed' item 7).",""]
out.append("pTwoVlnOne = { "+vln1+" "+vln1b+" }")
v2b=shift(vln1b,-1).split(" | "); v1b=vln1b.split(" | "); v2b[6]=v1b[6]; v2b[7]=v1b[7]
out.append("pTwoVlnTwo = { "+shift(vln1,-1)+" "+" | ".join(v2b)+" }")
th=theme.replace("c'2->(","c'2->(\\ff",1)
tail2=("aes,1 | es2 aes,2 | bes,1 | f,2 bes,2 | bes,1\\> | bes,1 | bes,1 | bes,2. r4\\mf |")
out.append("pTwoVc = { "+th+" "+tail2.replace("aes,1","aes,1",1)+" }")
out.append("pTwoVla = { "+th+" aes2 c'2 | es'2 c'2 | bes2 des'2 | c'2 d'2 | d'1\\> | d'1 | aes1 | f2. r4\\mf | }")
out.append("pTwoBsnOne = { "+th+" aes1 | g2 aes2 | des'1 | c'2 d'2 | d'1\\> | d'1 | d'1 | d'2. r4\\mf | }")
out.append("pTwoBsnTwo = { "+th+" "+tail2+" }")
out.append("pTwoHnThree = { "+th+" c'1 | bes2 c'2 | des'1 | c'2 d'2 | f'1\\> | f'1 | f'1 | f'2. r4\\mf | }")
out.append("pTwoHnFour = { "+th+" aes1 | g2 aes2 | bes1 | a2 bes2 | bes1\\> | bes1 | bes1 | bes2. r4\\mf | }")
cb=shift(theme,-1).replace("c2->(","c2->(\\ff",1)
out.append("pTwoCb = { "+cb+" aes,,1 | es,2 aes,,2 | bes,,1 | f,2 bes,,2 | bes,,1\\> | bes,,1 | bes,,1 | bes,,2. r4\\mf | }")
cbs=shift(theme,-2).replace("c,2->(","c,2->(\\ff",1).split(" | "); cbs=" | ".join(cbs[:6])+" | R1*2 |"
out.append("pTwoCbsn = { "+cbs+" aes,,1 | es,2 aes,,2 | bes,,1 | f,2 bes,,2 | bes,,1\\> | bes,,1 | R1*2\\! | }")
# held winds: chord per bar from first half chord
def held(lo,hi,idx,n=16):
    r=[]
    for b in range(n//2):
        ch=H[b*2][0]; ch2=H[b*2+1][0]
        p1=place(ch,lo,hi); p2=place(ch2,lo,hi)
        a=p1[min(idx,len(p1)-1)]; c=p2[min(idx,len(p2)-1)]
        r.append(f"{a}1" if a==c else f"{a}2 {c}2")
    return r
def w(lo,hi,idx,dyn="\\f"):
    r=held(lo,hi,idx,32); r[0]=re.sub(r"(\d)",r"\1"+dyn.replace("\\","\\\\"),r[0],count=1)
    r[12]=re.sub(r"(\d)(\s|$)",r"\1\\\\>\2",r[12],count=1) if False else r[12]
    return " | ".join(r)+" |"
fl=w(79,91,0).split(" | "); fl[10]="des'''1"; fl[11]="c'''2 d'''2"; out.append("pTwoFluteOne = { "+" | ".join(fl)+" }")
out.append("pTwoFluteTwo = { "+w(74,86,0)+" }")
out.append("pTwoOboeOne = { "+w(70,82,1)+" }")
out.append("pTwoOboeTwo = { "+w(67,79,0)+" }")
out.append("pTwoClOne = { "+w(62,74,1)+" }")
out.append("pTwoClTwo = { "+w(58,70,0)+" }")
out.append("pTwoHnOne = { "+w(64,74,0)+" }")
out.append("pTwoHnTwo = { "+w(57,69,0)+" }")
out.append("pTwoTbnOne = { R1*8 | es1\\f | es2 es2 | f1 | f2 f2 | f1\\> | f1 | R1*2\\! | }")
out.append("pTwoTbnTwo = { R1*8 | c1\\f | bes,2 c2 | des1 | c2 d2 | d1\\> | d1 | R1*2\\! | }")
out.append("pTwoBassTbn = { R1*8 | aes,1\\f | es2 aes,2 | bes,1 | f,2 bes,2 | bes,1\\> | bes,1 | R1*2\\! | }")
out.append("pTwoTimp = { c4->\\ff r4 r2 | R1*3 | c4-> r4 r2 | R1 | R1 | g,4-> g,4 g,4 r4 | aes,4->\\f r4 r2 | es4 r4 aes,4 r4 | R1*6 | }")
open('/tmp/m3/v01/sections/pTwo.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")

from g import *
import re
# CLOSING GROUP, bars 83-98, E flat major, Tempo I
head="es'''2->( bes''4. c'''8 | d'''4-.) c'''8( bes''8 aes''4-.) g''4-. | f''4( bes''8 c'''8 d'''4 f'''4) | es'''2-> r2 |"
lowhead="es2->( bes,4. c8 | d4-.) c8( bes,8 aes,4-.) g,4-. | f,4( bes,8 c8 d4 f4) | es2-> r2 |"
xfig="r4 bes''8( aes'' g'' f'' es'' d'' | es''8 f'' g'' aes'' bes''4->) bes'4-> | r4 f''8( es'' d'' c'' bes' a' | bes'8 c'' d'' es'' f''4->) f'4-> |"
cod_v1="<es'' bes'' g'''>4->\\ff r8 <es'' bes'' g'''>8 <f'' bes'' aes'''>4-> r4 | <es'' bes'' g'''>4-> r8 <es'' bes'' g'''>8 <f'' bes'' aes'''>4-> r4 | <g'' bes'' es'''>4-> r4 <f'' bes'' d'''>4-> r4 | <g'' bes'' es'''>2-> r2 |"
out=["% CLOSING GROUP, bars 83-98, E flat major, Tempo I, f to ff. 83-86: theme F1's head in major in the high winds and violins;",
"% 87-90: the head in the low strings and bassoons under the violins' turn figure (motive x), cadence in E flat at 90 (root V-I is",
"% allowed in E flat; the rule against it applies to C); 91-94: codetta chords, the brass's off-beat rhythm; 95-98: the E flat chord",
"% gains its seventh (V7 of A flat), then the bass falls E flat - D flat - C to V of F minor, diminuendo to p: the development starts in F minor.",""]
out.append("closVlnOne = { "+head.replace("->(","->(\\f",1)+" "+xfig+" "+cod_v1.replace("<es'' bes'' g'''>","<bes' g''>").replace("<f'' bes'' aes'''>","<bes' aes''>").replace("<g'' bes'' es'''>","<g' es''>").replace("<f'' bes'' d'''>","<bes' d''>")
          +" es''1\\>( | des''1) | c''1\\p~ | c''2. r4 | }")
out.append("closVlnTwo = { "+shift(head,-1).replace("->(","->(\\f",1)+" "+shift(xfig,-1).replace("f4-> |","f'4-> |")+" <es' bes'>4->\\ff r8 <es' bes'>8 <d' bes'>4-> r4 | <es' bes'>4-> r8 <es' bes'>8 <d' bes'>4-> r4 | <es' bes'>4-> r4 <d' bes'>4-> r4 | <es' bes'>2-> r2 | g'1\\>( | g'1) | g'1\\p~ | g'2. r4 | }")
out.append("closFluteOne = { "+head.replace("->(","->(\\f",1)+" R1*4 | g'''4->\\ff r8 g'''8 aes'''4-> r4 | g'''4-> r8 g'''8 aes'''4-> r4 | es'''4-> r4 d'''4-> r4 | es'''2-> r2 | R1*4 | }")
out.append("closFluteTwo = { "+shift(head,-1).replace("->(","->(\\f",1)+" R1*4 | es'''4->\\ff r8 es'''8 f'''4-> r4 | es'''4-> r8 es'''8 f'''4-> r4 | bes''4-> r4 bes''4-> r4 | bes''2-> r2 | R1*4 | }")
out.append("closOboeOne = { "+shift(head,-1).replace("->(","->(\\f",1)+" R1*4 | bes''4->\\ff r8 bes''8 bes''4-> r4 | bes''4-> r8 bes''8 bes''4-> r4 | g''4-> r4 f''4-> r4 | g''2-> r2 | es''1\\p( | des''1) | c''1~ | c''2. r4 | }")
out.append("closOboeTwo = { R1*4 | R1*4 | g'4->\\ff r8 g'8 aes'4-> r4 | g'4-> r8 g'8 aes'4-> r4 | es''4-> r4 d''4-> r4 | es''2-> r2 | R1*4 | }")
out.append("closClOne = { "+shift(head,-2).replace("->(","->(\\f",1)+" R1*4 | es''4->\\ff r8 es''8 d''4-> r4 | es''4-> r8 es''8 d''4-> r4 | bes'4-> r4 bes'4-> r4 | bes'2-> r2 | bes'1\\p~ | bes'1 | bes'1~ | bes'2. r4 | }")
out.append("closClTwo = { "+shift(head,-2).replace("->(","->(\\f",1)+" R1*4 | bes'4->\\ff r8 bes'8 bes'4-> r4 | bes'4-> r8 bes'8 bes'4-> r4 | g'4-> r4 f'4-> r4 | g'2-> r2 | g'1\\p~ | g'1 | e'1~ | e'2. r4 | }")
out.append("closBsnOne = { es'1\\f | f'2 bes2 | bes2 aes2 | g2 r2 | "+lowhead.replace("->(","->(\\f",1)+" g4->\\ff r8 g8 aes4-> r4 | g4-> r8 g8 aes4-> r4 | es'4-> r4 d'4-> r4 | es'2-> r2 | R1*4 | }")
out.append("closBsnTwo = { es1\\f | aes,2 bes,2 | d2 bes,2 | es2 r2 | "+lowhead.replace("->(","->(\\f",1)+" es4->\\ff r8 es8 d4-> r4 | es4-> r8 es8 d4-> r4 | g4-> r4 f4-> r4 | es2-> r2 | es1\\p | des1 | c1~ | c2. r4 | }")
out.append("closCbsn = { R1*4 | "+shift(lowhead,-1).replace("->(","->(\\f",1)+" es,4->\\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }")
hn=lambda a,b,c,d: f"R1*4 | R1*2 | r4 {a}4->\\f r4 {a}4-> | r4 {b}4-> r4 {b}4-> | {c}4->\\ff r8 {c}8 {d}4-> r4 | {c}4-> r8 {c}8 {d}4-> r4 | {c}4-> r4 {d}4-> r4 | {c}2-> r2 | R1*4 |"
out.append("closHnOne = { "+hn("bes'","bes'","g'","aes'")+" }")
out.append("closHnTwo = { "+hn("g'","f'","es'","f'")+" }")
out.append("closHnThree = { "+hn("es'","d'","bes","bes")+" }")
out.append("closHnFour = { "+hn("bes","bes","g","f")+" }")
out.append("closTptOne = { R1*8 | bes'4->\\ff r8 bes'8 bes'4-> r4 | bes'4-> r8 bes'8 bes'4-> r4 | bes'4-> r4 bes'4-> r4 | bes'2-> r2 | R1*4 | }")
out.append("closTptTwo = { R1*8 | g'4->\\ff r8 g'8 f'4-> r4 | g'4-> r8 g'8 f'4-> r4 | g'4-> r4 f'4-> r4 | g'2-> r2 | R1*4 | }")
out.append("closTptThree = { R1*8 | es'4->\\ff r8 es'8 d'4-> r4 | es'4-> r8 es'8 d'4-> r4 | es'4-> r4 d'4-> r4 | es'2-> r2 | R1*4 | }")
out.append("closTbnOne = { R1*4 | bes1\\f | bes2 c'2 | bes1 | bes2 r2 | g4->\\ff r8 g8 aes4-> r4 | g4-> r8 g8 aes4-> r4 | g4-> r4 aes4-> r4 | g2-> r2 | R1*4 | }")
out.append("closTbnTwo = { R1*4 | g1\\f | f2 es2 | d1 | es2 r2 | es4->\\ff r8 es8 f4-> r4 | es4-> r8 es8 f4-> r4 | es4-> r4 f4-> r4 | es2-> r2 | R1*4 | }")
out.append("closBassTbn = { R1*8 | es,4->\\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }")
out.append("closTuba = { R1*8 | es,4->\\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }")
out.append("closTimp = { R1*7 | es4\\f r4 r2 | es4->\\ff r8 es8 r2 | es4-> r8 es8 r2 | es4-> r4 r2 | es2-> r2 | R1*4 | }")
out.append("closVla = { es'8(\\f g' bes' g') es'8( g' bes' g') | f'8( aes' bes' aes') es'8( g' bes' g') | d'8( f' bes' f') d'8( f' aes' f') | es'8( g' bes' g') es'4 r4 | "
           +shift(lowhead,1).replace("->(","->(\\f",1)+" <es' bes'>4->\\ff r8 <es' bes'>8 <f' bes'>4-> r4 | <es' bes'>4-> r8 <es' bes'>8 <f' bes'>4-> r4 | <es' bes'>4-> r4 <d' bes'>4-> r4 | <es' bes'>2-> r2 | bes1\\>( | bes1) | bes1\\p~ | bes2. r4 | }")
out.append("closVc = { es4\\f g4 bes4 g4 | aes4 f4 g4 es4 | bes,4 d4 f4 aes4 | es2 r2 | "+lowhead.replace("->(","->(\\f",1)+" es4->\\ff r8 es8 d4-> r4 | es4-> r8 es8 d4-> r4 | es4-> r4 bes,4-> r4 | es2-> r2 | es1\\>( | des1) | c1\\p~ | c2. r4 | }")
out.append("closCb = { es,4\\f g,4 bes,4 g,4 | aes,4 f,4 g,4 es,4 | bes,,4 d,4 f,4 aes,4 | es,2 r2 | "+shift(lowhead,-1).replace("->(","->(\\f",1)+" es,4->\\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | es,1\\> | des,1 | c,1\\p~ | c,2. r4 | }")
open('/tmp/m3/v01/sections/clos.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")

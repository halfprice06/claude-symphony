from g import *
import re
def W(name,d,comment,drum=()):
    lines=["\\version \"2.24.0\""]+comment+[""]
    for k,v in d.items():
        lines.append(f"{name}{k} = "+("\\drummode " if k=='Perc' else "")+f"{{ {v} }}")
    open(f'/tmp/m3/v01/sections/{name}.ily','w').write("\n".join(lines)+"\n")
rep=lambda p,n=8: " ".join([f"{p}8"]*n)
# ---------- codaTwo 211-218: D flat episode, trumpets ----------
D={}
D['TptOne']="aes'4->(\\ff des''4 f''4. ges''8 | aes''4 bes''8 aes''8 ges''4. f''8 | es''4. f''8 des''2~ | des''1) | c''1 | c''1 | b'1\\< | b'1\\! |"
D['TptTwo']="f'4->(\\ff aes'4 des''4. es''8 | f''4 ges''8 f''8 es''4. des''8 | c''4. des''8 aes'2~ | aes'1) | fis'1 | g'1 | f'1\\< | aes'1\\! |"
D['TptThree']="des'1\\ff | ges'2 es'2 | aes'2 f'2 | f'1 | c'1 | e'1 | d'1\\< | d'1\\! |"
D['HnOne']="f'1\\ff | ges'2 ges'2 | aes'2 aes'2 | aes'1 | aes'1 | g'1 | g'1\\< | f'1\\! |"
D['HnTwo']="des'1\\ff | des'2 c'2 | c'2 des'2 | des'1 | c'1 | c'1 | d'1\\< | d'1\\! |"
D['HnThree']="aes1\\ff | bes2 aes2 | f2 f2 | f1 | es'1 | e'1 | f'1\\< | b1\\! |"
D['HnFour']="f1\\ff | ges2 ges2 | aes2 aes2 | aes1 | c'1 | c'1 | b1\\< | g1\\! |"
D['TbnOne']="f1\\ff | ges2 es2 | f2 f2 | f1 | fis1 | g1 | g1\\< | aes1\\! |"
D['TbnTwo']="des1\\ff | des2 c2 | aes,2 aes,2 | aes,1 | c1 | c1 | b,1\\< | b,1\\! |"
D['BassTbn']="des1\\ff | ges,2 aes,2 | f,1 | f,1 | aes,1 | g,1 | g,1\\< | g,1\\! |"
D['Tuba']="des,1\\ff | ges,,2 aes,,2 | f,,1 | f,,1 | aes,,1 | g,,1 | g,,1\\< | g,,1\\! |"
D['Timp']="aes,4->\\ff r4 r2 | aes,4 r4 aes,4 r4 | R1*2 | aes,1:32\\f | g,1:32 | g,1:32\\< | g,1:32\\! |"
D['FluteOne']="f''1\\ff | ges''2 es''2 | f''2 aes''2 | f''1 | fis''1 | g''1 | f''1\\< | f''1\\! |"
D['FluteTwo']="des''1\\ff | des''2 c''2 | c''2 des''2 | des''1 | c''1 | e''1 | d''1\\< | d''1\\! |"
D['OboeOne']="aes''1\\ff | bes''2 aes''2 | aes''2 f''2 | aes''1 | c'''1 | c'''1 | b''1\\< | b''1\\! |"
D['OboeTwo']="f''1\\ff | ges''2 ges''2 | es''2 des''2 | des''1 | es''1 | e''1 | d''1\\< | d''1\\! |"
D['ClOne']="des''1\\ff | des''2 c''2 | c''2 aes'2 | aes'1 | aes'1 | g'1 | g'1\\< | aes'1\\! |"
D['ClTwo']="aes'1\\ff | bes'2 aes'2 | f'2 f'2 | f'1 | fis'1 | e'1 | f'1\\< | f'1\\! |"
D['BsnOne']="f1\\ff | bes2 c'2 | aes2 aes2 | aes1 | c'1 | c'1 | b1\\< | b1\\! |"
D['BsnTwo']="des1\\ff | ges,2 aes,2 | f,1 | f,1 | aes,1 | g,1 | g,1\\< | g,1\\! |"
D['Cbsn']="des,1\\ff | ges,,2 aes,,2 | f,,1 | f,,1 | aes,,1 | g,,1 | g,,1\\< | g,,1\\! |"
D['VlnOne']="des'''4\\ff des'''8 c''' bes''4 aes''4 | ges''4 bes''8 aes'' ges''4 f''4 | es''8( f'' ges'' aes'' bes'' c''' des''' es''') | f'''1 | <fis'' c'''>1 | <e'' c'''>1 | <f'' b''>1\\< | b''2\\! r8 g'''8( a''' b''') |"
D['VlnTwo']="aes''4\\ff aes''8 ges'' f''4 des''4 | des''4 ges''8 f'' es''4 des''4 | c''8( des'' es'' f'' ges'' aes'' bes'' c''') | des'''1 | <c'' fis''>1 | <c'' g''>1 | <d'' g''>1\\< | <d'' aes''>1\\! |"
D['Vla']="<des' f'>1\\ff | <ges' bes'>2 <aes' c''>2 | <aes' c''>1 | <aes' des''>1 | <c' dis'>1 | <c' e'>1 | <d' f'>1\\< | <d' f'>1\\! |"
D['Vc']="des2\\ff des'2 | ges2 aes2 | f2 f,2 | f1 | aes,1 | g,1 | g,1\\< | g,1\\! |"
D['Cb']="des,2\\ff des2 | ges,2 aes,2 | f,2 f,,2 | f,1 | aes,,1 | g,,1 | g,,1\\< | g,,1\\! |"
W('codaTwo',D,["% CODA, bars 211-218. 211-214: the D flat episode, ff, in the trumpets: theme B's single recall from movement II, its second half,",
"% ending on D flat (mvt2 c100 sketch; cyclic-notes: give the forte D flat to the trumpets, not movement II's bar 61 tutti). D flat over F",
"% at 213-214 is the Neapolitan sixth of C. 215: German sixth of C spelled with D sharp in the violas; 216: cadential 6/4, the violas' D sharp",
"% rises to E natural (cyclic-notes 'Owed' item 9: the E flat/E natural thread closed in the violas with an augmented sixth); 217: V7;",
"% 218: V7 with the minor ninth, i.e. movement I's stop chord B-D-F-A flat over G, trumpet 1 on B. Top voice D flat - C - B (- C at 219)."])
# ---------- arrival 219-230 ----------
A={}
A['TptOne']="c''1\\ff | g'1 | e''1 | d''1 | c''2 des''2 | c''1 | R1 | c''1\\f | a'1 | g'1 | aes'1\\> | g'2. r4\\mf |"
A['TptTwo']="g'1\\ff | e'1 | c''1 | g'1 | e'2 f'2 | a'1 | R1 | g'1\\f | f'1 | e'1 | f'1\\> | e'2. r4\\mf |"
A['TptThree']="e'1\\ff | R1*11 |"
A['HnOne']="c''1\\ff | c''1 | g'1 | g'1 | e'2 f'2 | f'1 | R1 | e'1\\f | f'1 | e'1 | f'1\\> | e'2. r4\\mf |"
A['HnTwo']="g'1\\ff | e'1 | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\\f | c'1 | c'1 | c'1\\> | c'2. r4\\mf |"
A['HnThree']="e'1\\ff | g1 | c'1 | b1 | a2 bes2 | a1 | R1 | g1\\f | a1 | g1 | aes1\\> | g2. r4\\mf |"
A['HnFour']="c'1\\ff | e1 | g1 | g1 | e2 f2 | f1 | R1 | e1\\f | f1 | e1 | f1\\> | e2. r4\\mf |"
A['TbnOne']="g1\\ff | g1 | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\\f | c'1 | c'1 | c'1\\> | c'2. r4\\mf |"
A['TbnTwo']="e1\\ff | e1 | c'1 | g1 | e2 f2 | f1 | R1 | g1\\f | f1 | g1 | f1\\> | e2. r4\\mf |"
A['BassTbn']="c1\\ff | c1 | c1 | b,1 | a,2 bes,2 | f,1 | R1 | c1\\f | c1 | c1 | c1\\> | c2. r4\\mf |"
A['Tuba']="c,1\\ff | c,1 | c,1 | b,,1 | a,,2 bes,,2 | f,,1 | R1 | c,1\\f | c,1 | c,1 | c,1\\> | c,2. r4\\mf |"
A['Timp']="c1:32\\ff | c4 r4 r2 | R1*4 | c4\\f r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\\f | c1:32 | c1:32\\> | c2.:32 r4\\mf |"
A['Perc']="cymc1\\ff | R1*11 |"
A['FluteOne']="c''''1\\ff | R1*2 | g''1\\f | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1 | g''1 | aes''1\\> | g''2. r4\\mf |"
A['FluteTwo']="g'''1\\ff | R1*2 | e''1\\f | c'''1 | b''1 | a''2 bes''2 | a''1 | f''1 | e''1 | f''1\\> | e''2. r4\\mf |"
A['OboeOne']="c'''1\\ff | R1*2 | g'1\\f | e''1 | d''1 | c''2 des''2 | c''1 | c''1 | c''1 | c''1\\> | c''2. r4\\mf |"
A['OboeTwo']="g''1\\ff | R1*2 | e'1\\f | c''1 | b'1 | a'2 bes'2 | a'1 | a'1 | g'1 | aes'1\\> | g'2. r4\\mf |"
A['ClOne']="e'''1\\ff | R1*2 | g'1\\f | e''1 | d''1 | c''2 des''2 | c''1 | f''1 | e''1 | f''1\\> | e''2. r4\\mf |"
A['ClTwo']="c'''1\\ff | R1*2 | d'1\\f | e'1 | a'1 | g'2 f'2 | e'1 | c''1 | c''1 | c''1\\> | c''2. r4\\mf |"
A['BassCl']="c,1\\ff | R1*11 |"
A['BsnOne']="c1\\ff | c1 | c1 | b,1 | a,2 bes,2 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\\> | c2. r4\\mf |"
A['BsnTwo']="c,1\\ff | c,1 | c,1 | b,,1 | a,2 bes,2 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\\> | c,2. r4\\mf |"
A['Cbsn']="c,,1\\ff | c,,1 | c,,1 | b,,,1 | a,,2 bes,,2 | f,,1 | e,,2 bes,,2 | c,,1 | c,,1 | c,,1 | c,,1\\> | c,,2. r4\\mf |"
A['VlnOne']="c''''1:32\\ff | R1*2 | g''1\\f | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1 | g''1 | aes''1\\> | g''2.\\mf g'4( |"
A['VlnTwo']="<e'' c'''>1:32\\ff | R1*2 | g'1\\f | e''1 | d''1 | c''2 des''2 | c''1 | f''1 | e''1 | f''1\\> | e''2.\\mf g4( |"
A['Vla']="<g' e''>1:32\\ff | e'1 | c'1 | g1 | e2 f2 | a1 | g2 f2 | g1 | a1 | g1 | aes1\\> | g2. r4\\mf |"
A['Vc']="<c g>1:32\\ff | c1 | c1 | b,1 | a,2 bes,2 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\\> | c2. r4\\mf |"
A['Cb']="c,1:32\\ff | c,1 | c,1 | b,,1 | a,,2 bes,,2 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\\> | c,2. r4\\mf |"
W('arrival',A,["% THE C-MAJOR ARRIVAL AND CHORALE, bars 219-230, Maestoso (cyclic-notes 'Owed' items 2-4). 219: trumpet 1's B rises to C, coupled with",
"% the timpani; the stop chord of 218 resolves; the first sustained forte major chord in full brass; string tremolo and the violins' C7 here",
"% and only here; crash cymbals, no tam-tam. 220-224: the brass chorale, the motto in major G-E-D-C-D flat-C, trombone colour with horns",
"% and trumpets, independent bass C-C-B-A-B flat (cyclic-notes, mvt I critic 160). 222-226: the violins (with flutes, oboes, clarinets)",
"% in canon two bars after the brass. 225-226: movement I's timpani pulse c4 r8 g,8 c4 r4 between the phrases. 227-230: plagal close over",
"% the C pedal with mixture (IV - I - iv - I); no root-position V-I in C before the last cadence (255)."])
# ---------- sHead 231-242 ----------
S={}
S['VlnOne']="e''2.~ e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2) | e'''2.~(\\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | b''2 c'''2) | <g' e''>1\\< | <g' e''>1 | <d' b'>2 r8 g''8( a'' b'' | c'''8 d''' e''' f''' g'''4 a'''8 b''')\\! |"
S['VlnTwo']="e'2.~ e'8 d'8 | c'4 a'2-- g'4 | f'4. e'8 d'4 f'8 a'8 | c''2 b'2) | e''2.~(\\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | b'2 c''2) | <c' g'>1\\< | <c' g'>1 | <b f'>2 r8 g'8( a' b' | c''8 d'' e'' f'' g''4 a''8 b'')\\! |"
S['ClOne']="r4 c''4(\\mf b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 a'4( gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2 | e'2 e'2) | g'1\\< | g'1 | f'1 | f'1\\! |"
S['Vla']="r4 c''4(\\mf b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 a'4( gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2 | e'2 e'2) | g1\\< | g1 | f2 r8 g'8( a' b' | c''8 d'' e'' f'' g''4 a''8 b'')\\! |"
S['FluteOne']="R1*4 | e'''2.~(\\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | b''2 c'''2) | R1*2 | r2 r8 g''8(\\f a'' b'' | c'''8 d''' e''' f''' g'''4 a'''8 b''') |"
S['OboeOne']="R1*4 | e''2.~(\\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | b'2 c''2) | R1*4 |"
S['Vc']="c1\\mf | c1 | d2 f,2 | g,1 | a,1\\f | f,1 | d2 g,2 | e1 | g,1\\< | g,1 | d1 | d1\\! |"
S['Cb']="c,1\\mf~ | c,1~ | c,1~ | c,1 | a,,1\\f | f,,1 | d,2 g,,2 | e,1 | g,,1\\< | g,,1 | d,1 | d,1\\! |"
S['BsnTwo']="c1\\mf | c1 | d2 f,2 | g,1 | a,1\\f | f,1 | d2 g,2 | e1 | g,1\\< | g,1 | d1 | d1\\! |"
S['BsnOne']="g1\\mf | f1 | f2 a2 | g2 f2 | c'1\\f | c'1 | a2 g2 | g1 | b1\\< | b1 | b1 | b1\\! |"
S['HnThree']="g1\\p | a1 | a1 | g1 | e'1\\mf | c'1 | a2 b2 | g1 | R1*4 |"
S['HnFour']="e1\\p | f1 | f1 | f1 | c'1\\mf | a1 | f2 f2 | e1 | R1*4 |"
S['TptOne']="R1*8 | e''2->(\\f c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1) |"
S['TptTwo']="R1*8 | e''2->(\\f c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1) |"
S['HnOne']="R1*8 | e2->(\\f c'2~ | c'4 b2.~ | b2 c'2~ | c'1) |"
S['HnTwo']="R1*8 | e2->(\\f c'2~ | c'4 b2.~ | b2 c'2~ | c'1) |"
S['Timp']="c1:32\\pp | c1:32 | c1:32 | c1:32 | R1*4 | g,1:32\\p\\< | g,1:32 | g,1:32 | g,1:32\\f |"
hr=[]; hl=[]
for ch,b in [(['c','e','g'],'c,'),(['c','f','a'],'c,'),(['d','f','a'],'d,'),(['g','b','d'],'g,,'),(['a','c','e'],'a,,'),(['f','a','c'],'f,,'),(['d','f','a'],'d,'),(['e','g','c'],'e,')]:
    ps=place(ch,55,76)[:4]; hr.append(" ".join(f"{p}8" for p in ps)*1+" "+" ".join(f"{p}8" for p in reversed(ps))); hl.append(b+"1")
hr[0]=hr[0].replace("8","8\\mf",1) if False else hr[0]; hl[0]=hl[0]+"\\mf"
S['HarpR']=" | ".join(hr)+" | R1*4 |"; S['HarpL']=" | ".join(hl)+" | R1*4 |"
W('sHead',S,["% MOVEMENT I'S SECOND THEME IN C MAJOR, bars 231-242 (cyclic-notes 'Owed' item 5): the violins' singing statement of the falling",
"% major head with its pickup (230) and the chromatic counter (clarinet 1 and violas), molto cantabile, over the C pedal (basses, timpani);",
"% movement I withheld it (its §2 item 1). 235-238: a continuation to A6, flutes and oboe with the violins.",
"% 239-242: movement I's horn call in major, E-C-B-C, in trumpets 1-2 with horns 1-2 two octaves below (cyclic-notes 'Owed' item 8);",
"% G pedal, then V4/3 (D bass), stringendo into the Allegro molto."])

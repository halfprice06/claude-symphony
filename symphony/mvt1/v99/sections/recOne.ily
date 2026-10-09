% RECAPITULATION, first group, bars 131–146.

recOneFluteOne = {
  \partCombineApart r4\ff es'''2-> des'''4~ | des'''4 c'''2-> b''4 | r4 aes''2-> f''4~ | f''4 d''2-> r4 |
  % 135–137: Fl1 at the violin octave (A♭6 first at 140)
  \partCombineUnisono es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | \partCombineAutomatic b''2.-> r4 |
  r8\f aes''8\<( f'''4.->) es'''8( d'''8 c'''8) | des'''8\ff es'''8 f'''8 g'''8 aes'''2->~ | aes'''4. g'''8 f'''4 d'''4 | c'''2-> b''2-> | c'''8->\ff r8 r4 r2 | R1*3 |
}
recOneFluteTwo = {
  es''1\ff | c''2 d''2 | f''1 | g''1 |
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | aes''2.-> r4 |
  aes''2\f c'''2 | aes''1\ff | aes''2 aes''2 | g''1 | g''8->\ff r8 r4 r2 | R1*3 |
}
recOneOboeOne = {
  \partCombineApart r4\ff es''2-> des''4~ | des''4 c''2-> b'4 | r4 aes'2-> f'4~ | f'4 d''2-> r4 |
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | f''2.-> r4 \partCombineAutomatic |
  r8\f aes'8\<( f''4.->) es''8( d''8 c''8) | des''8\ff es''8 f''8 g''8 aes''2->~ | aes''4. g''8 f''4 d''4 | c''2-> b'2-> | R1*2 | \partCombineSoloI r2 g'4(\p^\markup \italic "dolce" e''4~ | e''2\> d''2)\! \partCombineAutomatic |
}
recOneOboeTwo = {
  g'1\ff | g'2 f'2 | f'1 | g'1 |
  g'4->\mf\< g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | d''2.-> r4 |
  c''1\f | des''1\ff | des''2 b'2 | d''1 | c''8->\ff r8 r4 r2 | R1 | r1 | R1 |
}
recOneClOne = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  \partCombineApart g'4->\mf\< g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | b'2.-> r4 \partCombineAutomatic |
  r8\f aes'8\<( f''4.->) es''8( d''8 c''8) | des''8\ff es''8 f''8 g''8 aes''2->~ | aes''4. g''8 f''4 d''4 | c''2-> b'2-> | es''8->\ff r8 r4 r2 | R1 | g'1\pp~ | g'2 r2 |
}
recOneClTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  es'4->\mf\< es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | aes'2.-> r4 |
  aes'1\f | aes'1\ff | aes'2 aes'2 | g'1 | c''8->\ff r8 r4 r2 | R1 | d'1\pp~ | d'2 r2 |
}
recOneBsnOne = {
  \partCombineUnisono r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  \partCombineAutomatic c4\mf\<-> c4 c4 b,4-> | b,4 b,4 c4-> c4 | c4 f4-> f4 f4 | f2.-> r4 |
  f2\f\< aes2 | des1\ff | f2 d2 | g1 |
  % cycle 77: Bsn 1 answers the Vln I head one bar later (as Bsn/Vla/Vln I at 33-35); tail D-C-B, no D-flat (avoids the head's own fifths)
  c2\f d2 | r8 g8\mf\>( es'4.->) d'4( c'8 | b1\pp) | R1 |
}
recOneBsnTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  c4\mf\<-> c4 c4 b,4-> | b,4 b,4 c4-> c4 | c4 f,4-> f,4 aes,4 | d2.-> r4 |
  f,2\f\< aes,2 | des,1\ff | f,2 d,2 | g,1 |
  R1*4 |
}
recOneCbsn = {
  c,4\ff c,4 c,4 c,4 | c,4 c,4 g,,4 g,,4 | aes,,4 aes,,4 aes,,4 aes,,4 | g,,4 g,,4 g,,4 g,,4 |
  c,4\mf\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.-> r4 |
  f,,2\f\< aes,,2 | des,,1\ff | f,,2 d,,2 | g,,1 | c,8->\ff r8 r4 r2 | R1*3 |
}
recOneHnOne = {
  g'1\ff | g'2 f'2 | f'1 | g'1 |
  g'4->\mp\< g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | aes'2.-> r4 |
  aes'1\f\< | aes'1\ff | aes'2 aes'2 | g'1 | g'8->\ff r8 r4 r2 | R1*2 | r2. g4(\mp^\markup \italic "dolce" |
}
recOneHnTwo = {
  es'1\ff | es'2 d'2 | f'1 | f'1 |
  es'4->\mp\< es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | f'2.-> r4 |
  f'1\f\< | f'1\ff | f'2 f'2 | d'1 | es'8->\ff r8 r4 r2 | R1*3 |
}
recOneHnThree = {
  c'1\ff | c'2. b4 | d'1 | d'1 |
  \partCombineSoloI c'4->\mp\< c'4 c'4 b4-> | b4 b4 c'4-> c'4 | c'4 aes4-> aes4 aes4 | \partCombineAutomatic d'2.->\mf r4 |
  c'1\f | des'1 | des'2 b2 | b1 |
  R1*2 | b1\pp | R1 |
}
recOneHnFour = {
  g1\ff | g1 | f1 | g1 |
  R1*3 | f2.->\mf r4 |
  f1\f | f1 | f2 d2 | g1 |
  R1*2 | g1\pp | R1 |
}
recOneTptOne = {
  g'1\ff | g'2. b'4 | aes'1 | b'1 |
  R1*3 | b'2.->\mf r4 | c''2\f\< c''2 | aes'1\ff |
  aes'2 aes'2 | g'1 | c''8->\ff r8 r4 r2 | R1*3 |
}
recOneTptTwo = {
  g'1\ff | g'2 f'2 | f'1 | g'1 |
  R1*3 | f'2.->\mf r4 | aes'2\f\< aes'2 | f'1\ff |
  f'2 f'2 | d'1 | es'8->\ff r8 r4 r2 | R1*3 |
}
recOneTptThree = {
  es'1\ff | es'2 d'2 | d'1 | d'1 |
  R1*3 | d'2.->\mf r4 | f'2\f\< f'2 | f'1\ff |
  des'2 b2 | b1 | R1*4 |
}
recOneTbnOne = {
  r8 g8\ff es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | r8 g8 f'4.-> es'8 d'8 c'8 | b4 d'8( c'8) g2 |
  c'4->\mp\< c'4 c'4 b4-> | b4 b4 c'4-> c'4 | c'4 aes4-> aes4 aes4 | aes2.-> r4 |
  c'1\f | des'1 | des'2 b2 | b1 | c'8->\ff r8 r4 r2 | R1*3 |
}
recOneTbnTwo = {
  r8 g8\ff es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | r8 g8 f'4.-> es'8 d'8 c'8 | b4 d'8( c'8) g2 |
  g4->\mp\< g4 g4 g4-> | g4 g4 g4-> g4 | g4 f4-> f4 f4 | f2.-> r4 |
  aes1\f | aes1 | aes2 aes2 | g1 | g8->\ff r8 r4 r2 | R1*3 |
}
recOneBassTbn = {
  c1\ff | c2 g,2 | aes,1 | g,1 |
  c4->\mp\< c4 c4 b,4-> | b,4 b,4 c4-> c4 | c4 f,4-> f,4 aes,4 | d2.-> r4 |
  f,2\f aes,2 | des1 | f2 d2 | g,1 | c8->\ff r8 r4 r2 | R1*3 |
}
recOneTuba = {
  c,1\ff | c,2 g,,2 | aes,,1 | g,,1 |
  c,4->\mp\< c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.-> r4 |
  f,,2\f aes,,2 | des,1 | f,2 d,2 | g,,1 | c,8->\ff r8 r4 r2 | R1*3 |
}
recOneTimp = {
  c4\ff r8 c8 c4 r8 c8 | c4 r4 g,4 r4 | aes,4 r8 aes,8 aes,4 r8 aes,8 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |
  c4->\mf r4 r2 | r2 c4-> r4 | r4 c4-> r2 | g,2.->\mf r4 |
  R1 | aes,1:32\f\< | aes,2:32\ff r2 | g,4-> r4 g,4-> r4 | c8->\ff r8 r4 r2 | g,1:32\mp\>~ | g,1:32\pp~ | g,2:32 r2 |
}
recOnePerc = \drummode {
  R1*16 |
}
recOneVlnOne = {
  r4\ff es'''2->\downbow des'''4~ | des'''4 c'''2-> b''4 | r4 aes''2-> f''4~ | f''4 d''2-> r4 |
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.-> r4 |
  r8 aes''8\f\<( \ottava #1 f'''4.->) es'''8( d'''8 c'''8) | des'''8\ff es'''8 f'''8 g'''8 aes'''2->~ | aes'''4. g'''8 f'''4 d'''4 \ottava #0 | c'''2-> b''2-> |
  r8 g'8\f( es''4.->) d''8( des''8 c''8 | c''4)\> b'8( c''8) aes'4. g'8 | g'1\pp~ | g'2 r2 |
}
recOneVlnTwo = {
  r4\ff es''2->\downbow des''4~ | des''4 c''2-> b'4 | r4 aes'2-> f'4~ | f'4 d'2-> r4 |
  g'4->\mf\< g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | <d'' aes''>2.-> r4 |
  r8 aes'8\f\<( f''4.->) es''8( d''8 c''8) | des''8\ff es''8 f''8 g''8 aes''2->~ | aes''4. g''8 f''4 d''4 | c''2-> b'2-> |
  r8\f g'8 r8 g'8 r8 g'8 r8 g'8 | g'2\> f'2 | f'1\pp | f'2 r2 |
}
recOneVla = {
  r8\ff <es' g'>8 \repeat unfold 3 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } | \repeat unfold 4 { r8 <d' f'>8 } | \repeat unfold 4 { r8 <d' f'>8 } |
  es'4->\mf\< es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | <f' b'>2.-> r4 |
  c'8\f\< c'8 b8 c'8 f'8 f'8 e'8 f'8 | f'8\ff f'8 es'8 f'8 aes'8 aes'8 g'8 aes'8 | aes'8 aes'8 g'8 aes'8 f'8 f'8 e'8 f'8 | g'8 g'8 fis'8 g'8 d'8 d'8 cis'8 d'8 |
  r8\f es'8 r8 es'8 r8 es'8 r8 es'8 | es'2\> d'2 | d'1\pp | d'2 r4 g4(\mf^\markup \italic "espr." |
}
recOneVc = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  c4\mf\<-> c4 c4 b,4-> | b,4 b,4 c4-> c4 | c4 f4-> f4 f4 | <d aes>2.-> r4 |
  f2\f\< aes2 | des1\ff | f2 d2 | g,1 |
  c2\f d2 | es2\> d2 | b,1\pp | r2. g,4(\mf^\markup \italic "espr." |
}
recOneCb = {
  c,8\ff \repeat unfold 7 c,8 | \repeat unfold 4 c,8 \repeat unfold 4 g,,8 | \repeat unfold 8 aes,,8 | \repeat unfold 8 g,,8 |
  c,4\mf\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.-> r4 |
  f,4\f\< r8 f,8 aes,4 r8 aes,8 | des,8\ff \repeat unfold 7 { des,8 } | \repeat unfold 4 { f,8 } \repeat unfold 4 { d,8 } | \repeat unfold 8 { g,,8 } |
  c,4\f r8 c,8 c,4 r8 c,8 | g,,1\> | g,,1\pp~ | g,,2 r2 |
}
recOneBassCl = {
  R1*8 | f,2\f\< aes,2 | des1\ff | f2 d2 |
  g,1 | R1*4 |
}
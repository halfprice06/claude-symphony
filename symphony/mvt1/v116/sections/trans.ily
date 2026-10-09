% TRANSITION, bars 33–46.

transFluteOne = {
  c'''8->\ff r8 r4 r2 | R1*5 | \partCombineSoloI r2^\markup \bold "1." d''8\mf\<( es''8 f''8 bes''8) | d'''2-> bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  \partCombineAutomatic g'''1\ff~ | g'''2 f'''2\> | es'''4\p r4 r2 | R1*3 |
}
transFluteTwo = {
  g''8->\ff r8 r4 r2 | R1*7 | g''1\ff~ | g''2 f''2\> |
  es''4\p r4 r2 | R1*3 |
}
transOboeOne = {
  c''8->\ff r8 r4 r2 | R1*3 | \partCombineSoloI r2 r8 bes'8\mf( ges''4->~ | ges''8) f''8( fes''8 es''8) r2 |
  r2 d''8\mf\<( es''8 f''8 bes''8) | d'''2-> r16 c''16( d'' es'' f'' es'' f'' fis'') |
  \partCombineAutomatic g''1\ff~ | g''2 f''2\> | es''4\p r4 r2 | R1 |
  bes'2(\p aes'4 g'4 | f'2 es'4) r4 |
}
transOboeTwo = {
  g'8->\ff r8 r4 r2 | R1*7 | des''1\ff | des''2 bes'2\> |
  bes'4\p r4 r2 | R1*3 |
}
transClOne = {
  es''8->\ff r8 r4 r2 | R1 | bes'1\p( | g'1) | R1 |
  % cycle 77: winds take the half-bar answers to Vln I at 37-40 (Ob 1, Cl 1 double the viola answer at the violin octave; Fl 1/Ob 1 answer at 39)
  \partCombineSoloI r2 r8 c''8\mf( aes''4->~ | aes''8) g''16( ges''16 f''4) r2 | \partCombineAutomatic R1 |
  g'1\ff~ | g'2 f'2\> | es'4\p r4 r2 | R1*3 |
}
transClTwo = {
  c''8->\ff r8 r4 r2 | R1 | f'1\p( | es'1) | R1*4 |
  bes1\ff | \after 2 \> bes1 | g4\p r4 r2 | R1*3 |
}
transBsnOne = {
  \set Staff.soloText = "1. Solo" r8 g8\f_\markup \italic "espr."( es'4.->) d'8(\> des'8 c'8 | \set Staff.soloText = "1." c'4)\mf bes8( aes8) g4 f4 | f2 aes2 | g2 es2 \breathe |
  ges1\mf\< | aes1 | aes1 | aes1\f |
  R1*6 |
}
transBsnTwo = {
  R1*4 | es1\mf\< | f1 | bes,1 |
  bes,1\f | es1\ff | es1\> | es4\p r4 r2 |
  R1*3 |
}
transCbsn = {
  R1*8 | es,1\ff~ | es,1\> | es,4\p r4 r2 |
  R1*3 |
}
transHnOne = {
  g'8->\ff r8 r4 r2 | R1*7 | \partCombineUnisono r2. es4(\ff | c'4 bes2.)\> |
  \partCombineAutomatic r2 es'4(\p c''4~ | c''2 bes'2) | R1 | r2. es4(\mp |
}
transHnTwo = {
  es'8->\ff r8 r4 r2 | R1*7 | r2. es4(\ff | c'4 bes2.)\> |
  g'1\p~ | g'1 | R1*2 |
}
transHnThree = {
  R1*4 | des'1\p\< | c'1 | d'1 |
  d'1\f | des'2.\ff es4( | c'4 bes2.)\> | des'4\p r4 r2 |
  R1*3 |
}
transHnFour = {
  R1*4 | ges1\p\< | aes1 | aes1 |
  aes1\f | g2.\ff es4( | c'4 bes2.)\> | g4\p r4 r2 |
  R1*3 |
}
transTptOne = {
  c''8->\ff r8 r4 r2 | R1*7 | bes'1\ff | bes'2 aes'2\> |
  g'4\p r4 r2 | R1*3 |
}
transTptTwo = {
  g'8->\ff r8 r4 r2 | R1*7 | g'1\ff | g'2 f'2\> |
  es'4\p r4 r2 | R1*3 |
}
transTptThree = {
  R1*8 | des'1\ff | des'1\> | des'4\p r4 r2 |
  R1*3 |
}
transTbnOne = {
  c'8->\ff r8 r4 r2 | R1*6 | bes1\f | bes1\ff |
  bes1\> | bes4\p r4 r2 | R1*3 |
}
transTbnTwo = {
  g8->\ff r8 r4 r2 | R1*6 | f1\f | g1\ff |
  g1\> | g4\p r4 r2 | R1*3 |
}
transBassTbn = {
  c8->\ff r8 r4 r2 | R1*6 | bes,1\f | es1\ff~ |
  es1\> | es4\p r4 r2 | R1*3 |
}
transTuba = {
  c,8->\ff r8 r4 r2 | R1*7 | es,1\ff~ | es,1\> |
  es,4\p r4 r2 | R1*3 |
}
transTimp = {
  c8->\ff r8 r4 r2 | R1^\markup \small "muta C in B♭" | R1*5 | bes,1:32\pp\< |
  es1:32\ff~ | es1:32\>~ | es1:32\pp | R1^\markup \small "muta B♭ in C" |
  R1*2 |
}
transVlnOne = {
  c'''8->\downbow\ff r8 r4 r2 | R1 | r8 f'8\mf( des''4.->) c''8( ces''8 bes'8 | bes'4) a'8( bes'8) g'4.-> f'8 |
  r8 bes'8\<( ges''4.->) f''8( fes''8 es''8) | r8 c''8( aes''4.->) g''8( ges''8 f''8) | d''8( es''8 f''8 bes''8) d'''2-> | f''8( g''8 aes''8 c'''8) \ottava #1 bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  g'''1\ff~ | g'''2 f'''2\> | es'''4\p \ottava #0 r4 r2 | R1*3 |
}
transVlnTwo = {
  c''8->\downbow\ff r8 r4 r2 | R1*3 | bes'1:32\p\< | aes'1:32 |
  aes'1:32 | aes'1:32\f | g''1\ff~ | g''2 f''2\> |
  des'1\pp | es'1 | es'1 | des'2 des'2 |
}
transVla = {
  R1 | r8 c'8\mf( aes'4.->) g'8( ges'8 f'8 | f'4) e'8( f'8) d'2 | es'1 |
  ges'2:32\p\< r8 bes8( ges'4->~ | ges'8) f'8( fes'8 es'8) r8 c'8( aes'4->~ | aes'8) g'16( ges'16 f'4) f'2:32 | <d' f'>1:32\f |
  <es' g'>1:32\ff | <es' g'>1:32\> | bes1\pp | bes1 |
  c'1 | bes2 bes2 |
}
transVc = {
  R1*2 | f2\mf aes2 | g2 es2 |
  ges1\< | aes1 | aes1 | aes1\f |
  g1\ff | g1\> | g1\pp | g1 |
  aes1 | f2 g4 es4(\mf |
}
transCb = {
  c,1\fp | f,1 | bes,,1 | es,1 |
  es,1\< | f,1 | bes,,1 | bes,,1\f |
  es,1\ff~ | es,1\>~ | es,1\pp | des,1 |
  c,1 | des,2 es,2 |
}

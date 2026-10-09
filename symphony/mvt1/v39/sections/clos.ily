% CLOSING, bars 69–76. Forte codetta in A♭ (Tempo I), then the flute's darkened motto over an A♭ pedal.

closFluteOne = {
  c'''2.~\f c'''8 bes''8 | aes''4 f'''2 es'''4 | des'''4. c'''8 bes''4 des'''8 f'''8 | aes'''4-> es'''4-> c'''2-> |
  r2. c''4(\p^\markup \italic "espr." | aes''2.~\> aes''8 g''8 | ges''2 f''4 es''8 f''8)\pp | R1 |
}
closFluteTwo = { es''2\f es''2 | f''2 f''2 | g''1 | aes''4-> aes''4-> aes''2-> | R1*4 | }
closOboeOne = {
  c''2.~\f c''8 bes'8 | aes'4 f''2 es''4 | des''4. c''8 bes'4 des''8 f''8 | aes''4-> es''4-> c''2-> |
  R1*4 |
}
closOboeTwo = { c''2\f c''2 | des''2 des''2 | bes'1 | c''4-> c''4-> c''2-> | R1*4 | }
closClOne = { \partCombineApart r8 es'8 c''4.-> bes'8 aes'8 g'8 | aes'8 bes'8 c''8 des''8 f''4.-> es''8 | des''8 c''8 bes'8 aes'8 g'4.-> bes'8 | aes'4-> c''4-> aes'2-> \partCombineAutomatic | R1*4 | }
closClTwo = { aes'2\f aes'2 | aes'2 aes'2 | g'1 | aes'4-> aes'4-> aes'2-> | R1*4 | }
closBassCl = {
  aes,2\f f,2 | des2 bes,2 | es1 | aes,4-> es4-> aes,2-> |
  R1*4 |
}
closBsnOne = { c'2\f es'2 | f'2 f'2 | des'1 | c'4-> es'4-> c'2-> | R1*4 | }
closBsnTwo = {
  aes,2\f f,2 | des2 bes,2 | es1 | aes,4-> es4-> aes,2-> |
  R1*4 |
}
closCbsn = {
  aes,,2\f f,,2 | des,2 bes,,2 | es,1 | aes,,4-> es,4-> aes,,2-> |
  R1*4 |
}
closHnOne = {
  r8 es8\f c'4.-> bes8 aes8 g8 | aes8 bes8 c'8 des'8 f'4.-> es'8 | des'8 c'8 bes8 aes8 g4.-> bes8 | aes4-> c'4-> aes2-> |
  R1*4 |
}
closHnTwo = {
  r8 es8\f c'4.-> bes8 aes8 g8 | aes8 bes8 c'8 des'8 f'4.-> es'8 | des'8 c'8 bes8 aes8 g4.-> bes8 | aes4-> c'4-> aes2-> |
  R1*4 |
}
closHnThree = { aes2\f aes2 | aes2 aes2 | g1 | aes4-> aes4-> aes2-> | R1*4 | }
closHnFour = { es2\f es2 | f2 f2 | es1 | es4-> es4-> es2-> | aes1\pp~ | aes1~ | aes1~ | aes1 | }
closTptOne = {
  c''2.~\f c''8 bes'8 | aes'4 f''2 es''4 | des''4. c''8 bes'4 des''8 f''8 | aes''4-> es''4-> c''2-> |
  R1*4 |
}
closTptTwo = { aes'2\f aes'2 | aes'1 | g'1 | aes'4-> aes'4-> aes'2-> | R1*4 | }
closTbnOne = {
  es'2\mf es'2 | des'2 des'2 | des'1 | c'4->\f c'4-> c'2-> |
  R1*4 |
}
closTbnTwo = {
  c'2\mf c'2 | aes2 aes2 | bes1 | aes4->\f aes4-> aes2-> |
  R1*4 |
}
closBassTbn = {
  aes,2\mf f,2 | des2 bes,2 | es1 | aes,4->\f es4-> aes,2-> |
  R1*4 |
}
closTuba = {
  aes,,2\mf f,,2 | des,2 bes,,2 | es,1 | aes,,4->\f es,4-> aes,,2-> |
  R1*4 |
}
closTimp = { aes,4\f r8 aes,8 aes,4 r4 | R1 | es1:32\< | aes,4->\ff es4-> aes,2-> | R1*3 | aes,1:32\ppp | }
closVlnOne = {
  c'''2.~\f c'''8 bes''8 | aes''4 f'''2 es'''4 | \ottava #1 des'''4. c'''8 bes''4 des'''8 f'''8 | aes'''4-> es'''4-> c'''2-> \ottava #0 |
  R1*4 |
}
closVlnTwo = { r8 es'8\f c''4.-> bes'8 aes'8 g'8 | aes'8 bes'8 c''8 des''8 f''4.-> es''8 | des''8 c''8 bes'8 aes'8 g'4.-> bes'8 | aes'4-> c''4-> aes'2-> | es'1\pp | es'1 | ges'1 | fes'1 | }
closVla = { <c' es'>8\f \repeat unfold 7 { <c' es'>8 } | \repeat unfold 4 { <des' f'>8 } \repeat unfold 4 { <des' f'>8 } | \repeat unfold 8 { <des' g'>8 } | <c' es'>4-> <c' es'>4-> <c' es'>2-> | c'1\pp | c'1 | c'1 | des'1 | }
closVc = {
  aes2\f f2 | des'2 bes2 | es1 | aes4-> es4-> aes,2-> |
  aes1\pp~ | aes1~ | aes1~ | aes1 |
}
closCb = {
  aes,,2\f f,,2 | des,2 bes,,2 | es,1 | aes,,4-> es,4-> aes,,2-> |
  aes,,1\pp~ | aes,,1~ | aes,,1~ | aes,,1 |
}
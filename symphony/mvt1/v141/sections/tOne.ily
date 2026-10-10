% FIRST THEME, bars 15–32 (Allegro appassionato).
% c102: Hn 4 24–25 holds G (was G–C under the melody D–G: parallel fifths).

tOneFluteOne = {
  R1 | R1 | R1 | R1 |
  R1 | R1 | R1 | R1 |
  % 23–25: Fl1 at the violin octave (top line rises into 26/27; A♭6 first at 31)
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.->\ff r4 |
  \partCombineApart r8 g''8( es'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8( c'''8) aes''4.-> g''8 | r8 g''8( f'''4.->) es'''8( d'''8 c'''8) | bes''8-. c'''-. des'''-. bes''-. g'''4.-> f'''8 |
  aes'''4.-> g'''8 f'''4 d'''4 | c'''4-> b''4-> r2 \partCombineAutomatic |
}
tOneFluteTwo = {
  R1*8 |
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | aes''2.->\ff r4 |
  % c104: C6 at 31 beats 1–2 (fifth of iv) fills the octave under the A♭6 peak
  g''1\ff | aes''1 | aes''1 | bes''1 | c'''2 aes''2 | g''4-> g''4-> r2 |
}
tOneOboeOne = {
  R1*8 | \partCombineSoloI es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) |
  \partCombineAutomatic f''2.->\ff r4 | \partCombineApart r8 g'8( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) |
  bes'8-. c''-. des''-. bes'-. g''4.-> f''8 | aes''4.-> g''8 f''4 d''4 | c''4-> b'4-> r2 \partCombineAutomatic |
}
tOneOboeTwo = {
  R1*8 |
  % c119: Ob 2 rests 23-25 (it held the syncopated G-F line against Ob 1's melody: sevenths/ninths at 24.1, 24.4, 25.3; Rimsky-Korsakov PDF 90 rule 4: no discords between two oboes). The line stays in Cl 1, Hn 1, Vln II.
  R1*3 | d''2.->\ff r4 |
  g'1\ff | f'1 | aes'1 | g'1 | aes'2 f'2 | f'4-> f'4-> r2 |
}
tOneClOne = {
  R1 | R1 | R1 | R1 |
  R1 | R1 | R1 | R1 |
  g'2.\mf\<-> f'4->~ | f'2 g'2->~ | g'4 f'2.-> | b'2.->\ff r4 |
  \partCombineApart r8 g'8( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | bes'8-. c''-. des''-. bes'-. g''4.-> f''8 |
  aes''4.-> g''8 f''4 d''4 | c''4-> b'4-> r2 \partCombineAutomatic |
}
tOneClTwo = {
  R1*8 |
  es'2.\mf\<-> d'4->~ | d'2 es'2->~ | es'4 c'2.-> | aes'2.->\ff r4 |
  es'1\ff | d'1 | c'1 | bes1 | c'2 d'2 | d'4-> d'4-> r2 |
}
tOneBsnOne = {
  R1*4 | f2\mf aes,2 | des1 | f2 g2 |
  g2 c2 | c2.\<-> b,4->~ | b,2 c2->~ | c4 f2.-> |
  f2.->\ff r4 | c'2\ff es'2 | d'2 f'2 | es'2 c'2 |
  e'2 bes2 | aes2 f2 | g4-> g,4-> r2 |
}
tOneBsnTwo = {
  R1*8 |
  c2.\mf\<-> b,4->~ | b,2 c2->~ | c4 f,2-> aes,4 | d2.->\ff r4 |
  c1\ff | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 |
}
tOneCbsn = {
  R1*11 | d,2.->\ff r4 |
  c,4\ff c,4 c,4 c,4 | d,4 d,4 d,4 d,4 | es,4 es,4 es,4 es,4 | e,4 e,4 e,4 e,4 |
  f,4 f,4 d,4 d,4 | g,,4-> g,,4-> r2 |
}
tOneHnOne = {
  R1*8 | g'2.\mp\<-> f'4->~ | f'2 g'2->~ | g'4 f'2.-> |
  aes'2.->\ff r4 | g'1\ff | f'1 | aes'1 |
  g'1 | aes'2 aes'2 | g'4-> g'4-> r2 |
}
tOneHnTwo = {
  R1*8 |
  es'2.\mp\<-> d'4->~ | d'2 es'2->~ | es'4 c'2.-> | f'2.->\ff r4 |
  es'1\ff | f'1 | f'1 | e'1 | f'2 f'2 | f'4-> f'4-> r2 |
}
tOneHnThree = {
  R1*4 | c'1\p | des'1 | des'2 b2 |
  b4 d'4 c'2 | \clef bass c'2.\mp\<-> b4->~ | b2 c'2->~ | c'4 aes2.-> |
  d'2.->\ff r4 | \clef treble c'1\f | b1 | c'1 |
  des'1 | c'2 c'2 | b4-> b4-> r2 |
}
tOneHnFour = {
  R1*4 | f1\p | f1 | f2 g2 |
  g2 g2 | c2.\mp\<-> g,4->~ | g,2 g,2->~ | g,4 f,2.-> |
  f2.->\ff r4 | g1\f | g1 | aes1 |
  bes1 | aes2 aes2 | g4-> g4-> r2 |
}
tOneTptOne = {
  R1*11 | b'2.->\ff r4 | c''4\f r8 c''8 c''4 r8 c''8 | g'4 r4 b'4 r4 |
  c''1 | bes'4 r8 bes'8 bes'4 r8 bes'8 | c''2 aes'2 | g'4->\ff g'4-> r2 |
}
tOneTptTwo = {
  R1*11 | f'2.->\ff r4 | g'4\f r8 g'8 g'4 r8 g'8 | f'4 r4 f'4 r4 |
  aes'1 | g'4 r8 g'8 g'4 r8 g'8 | aes'2 f'2 | f'4->\ff f'4-> r2 |
}
tOneTptThree = { R1*11 | d'2.->\ff r4 | es'4\f r8 es'8 es'4 r8 es'8 | d'4 r4 d'4 r4 | es'1 | e'4 r8 e'8 e'4 r8 e'8 | f'2 d'2 | d'4-> d'4-> r2 | }
tOneTbnOne = { R1*11 | aes2.->\ff r4 | c'1\f | b1 | c'1 | bes1 | c'2 c'2 | b4-> b4-> r2 | }
tOneTbnTwo = { R1*11 | f2.->\ff r4 | g1\f | f1 | aes1 | g1 | aes2 aes2 | g4-> g4-> r2 | }
tOneBassTbn = { R1*11 | d2.->\ff r4 | c1\f | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 | }
tOneTuba = { R1*11 | d,2.->\ff r4 | c,1\f | d,1 | es,1 | e,1 | f,2 d,2 | g,,4-> g,,4-> r2 | }
tOneTimp = {
  R1*12 | c4\ff r8 c8 c4 r8 c8 | g,4 r4 g,4 r4 | R1 |
  c4 r8 c8 c4 r8 c8 | R1 | g,4-> g,4-> r2 |
}
tOneVlnOne = {
  r8 g'8\downbow\f( es''4.->) d''8( des''8 c''8 | c''4) b'8\upbow( c''8) aes'4.-> g'8 | r8 g'8\downbow( f''4.->) es''8( d''8 c''8 | b'4) d''8( c''8) g'2 |
  r8 aes'8\downbow\<( aes''4.->) g''8( f''8 es''8 | des''8 es''8 f''8 aes''8) des'''2~\sf | des'''8\>( c'''8 bes''8 aes''8) g''4.-> f''8 | es''8( d''8 c''8 b'8) c''4\mf r4 |
  es''4(\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.->\ff r4 |
  r8 g''8\downbow\ff( es'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8\upbow( c'''8) aes''4.-> g''8 | r8 g''8\downbow( f'''4.->) es'''8( d'''8 c'''8) | bes''8-. c'''-. des'''-. bes''-. g'''4.-> f'''8 |
  \ottava #1 aes'''4.-> g'''8 f'''4 d'''4 \ottava #0 | c'''4->\downbow b''4->\downbow r4 f''16(\< g'' aes'' b'') |
}
tOneVlnTwo = {
  r8 g'8~\mf g'4 r8 g'8~ g'4 | r8 g'8~ g'4 r8 f'8~ f'4 | r8 aes'8~ aes'4 r8 aes'8~ aes'4 | r8 f'8~ f'4 r8 d'8~ d'4 |
  r8 c'8~\mp c'4 r8 c'8~ c'4 |
  % c121: 20.3-21.2 Vln II doubles the D♭6 peak and its descent an octave below, then resumes the syncopation (Rimsky-Korsakov PDF 58-59, 62 Note I:
  % a violin melody in the very high register is isolated from the ensemble unless doubled in octaves; as at 60-63 and 139-142). Hn 3 holds the D♭ the syncopation left.
  r8 des'8~ des'4 des''2~\sf | des''8\>( c''8 bes'8 aes'8) r8 d'8~\mp d'4 | r8 d'8~ d'4 r8 g'8~ g'4 |
  g'4\mf\<-> g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | <d'' aes''>2.->\ff r4 |
  r8 g'8\downbow\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8\upbow( c''8) aes'4.-> g'8 | r8 g'8\downbow( f''4.->) es''8( d''8 c''8) | bes'8-. c''-. des''-. bes'-. g''4.-> f''8 |
  aes''4.-> g''8 f''4 d''4 | c''4->\downbow b'4->\downbow r4 f'16(\< g' aes' b') |
}
tOneVla = {
  r8 es'8~\mf es'4 r8 es'8~ es'4 | r8 es'8~ es'4 r8 d'8~ d'4 | r8 <d' f'>8~ <d' f'>4 r8 <d' f'>8~ <d' f'>4 | r8 d'8~ d'4 r8 b8~ b4 |
  aes'2.~\mf\<(^\markup \italic "espr." aes'8 g'8 | f'2\f aes'2) | aes'4\>( g'4 f'2~ | f'2\mf es'2) |
  es'4\<-> es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | <f' b'>2.->\ff r4 |
  r8 g8\downbow\ff( es'4.->) d'8( des'8 c'8 | c'4) b8\upbow( c'8) aes4.-> g8 | r8 g8\downbow( f'4.->) es'8( d'8 c'8) | bes8-. c'8-. des'8-. bes8-. g'4.-> f'8 |
  aes'4.-> g'8 f'4 d'4 | <d' f'>4->\downbow <d' f'>4->\downbow r2 |
}
tOneVc = {
  c2\f d2 | es2 d2 | f2 aes2 | g2 g,2 |
  f2\mf aes,2 | des1 | f2 g2 | g2 c2 |
  c2.\<-> b,4->~ | b,2 c2->~ | c4 f2.-> | <d aes>2.->\ff r4 |
  c'2\ff es'2 | d'2 f'2 | es'2 c'2 | e'2 bes2 |
  aes2 f2 | g4->\downbow g,4->\downbow r2 |
}
tOneCb = {
  c,4\f r8 c,8 c,4 r8 c,8 | c,4 r8 c,8 g,,4 r8 g,,8 | aes,,4 r8 aes,,8 aes,,4 r8 aes,,8 | g,,4 r8 g,,8 g,,4 r8 g,,8 |
  f,,4\mf r8 f,,8 f,,4 r8 f,,8 | des,4 r8 des,8 des,4 r8 des,8 | f,,4 r8 f,,8 g,,4 r8 g,,8 | g,,4 r8 g,,8 c,4 r8 c,8 |
  c,4\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.->\ff r4 |
  c,8\ff \repeat unfold 7 c,8 | \repeat unfold 8 d,8 | \repeat unfold 8 es,8 | \repeat unfold 8 e,8 |
  \repeat unfold 4 f,8 \repeat unfold 4 d,8 | g,,4->\downbow g,,4->\downbow r2 |
}

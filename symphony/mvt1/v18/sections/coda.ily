% CODA, bars 159–172. The second theme's head returns in C minor in the cellos against the horn's motto;
% the low strings state the motto in augmentation; the violins' last motto sinks through the Neapolitan
% to C, and the violas alone turn the minor third to major at the very end.

codaClOne = {
  r8 g'8\ff es''4.-> d''8 des''8 c''8 | c''4 b'8( c''8) aes'4.-> g'8 | r8 aes'8 f''4.-> es''8 d''8 c''8 | b'2.->\fff r4 |
  R1*5 | r2. es'4(\pp | c''1~ | c''1 |
  des''1 | c''1) | R1*4 |
}
codaBassCl = {
  c1\ff | c1 | c1 | c2.->\fff r4 |
  R1*4 | g,1\pp( | es1 | d1 |
  des1 | c1) | R1*5 |
}
codaBsnTwo = {
  c1\ff | c1 | c1 | c2.->\fff r4 |
  c1\p | f1 | f1 | g,1 |
  R1*10 |
}
codaHnOne = {
  g'1\ff | g'2 aes'2 | aes'1 | aes'2.->\fff r4 |
  r2. g4(\p | es'2. d'4 | des'2. c'4~ | c'2 b2) |
  R1*10 |
}
codaHnThree = {
  c'1\ff | c'1 | c'1 | d'2.->\fff r4 |
  R1*12 | g'1\ppp~ | g'1\fermata |
}
codaHnFour = {
  g1\ff | g2 aes2 | f1 | b2.->\fff r4 |
  R1*12 | c'1\ppp~ | c'1\fermata |
}
codaTimp = {
  c1:32\ff~ | c1:32~ | c1:32\< | c4->\fff r2. |
  R1*3 | g,1:32\pp | R1*6 | c1:32\ppp~ |
  c1:32~ | c1:32~ | c1:32\fermata |
}
codaHarpL = {
  R1*17 | <c, g, c>1\pp\laissezVibrer |
}
codaVlnOne = {
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | c'''4 b''8( c'''8) aes''4.-> g''8 | r8 aes''8 f'''4.-> es'''8 d'''8 c'''8 | b''2.->\fff r4 |
  R1*8 | r2. g'4(\pp | es''1~ | es''2. d''4 |
  des''1 | c''1~ | c''1\fermata) |
}
codaVlnTwo = {
  r8 g'8\ff es''4.-> d''8 des''8 c''8 | c''4 b'8( c''8) aes'4.-> g'8 | r8 aes'8 f''4.-> es''8 d''8 c''8 | b'2.->\fff r4 |
  g'1\pp | aes'1 | aes'1 | g'1 |
  es'1 | g'1 | f'1 | f'1 |
  g'1 | g'1 | g'1 | f'1 |
  g'1~ | g'1\fermata |
}
codaVla = {
  \repeat unfold 8 { <es' g'>8\ff } | \repeat unfold 4 { <es' g'>8 } \repeat unfold 4 { <es' aes'>8 } | \repeat unfold 8 { <f' aes'>8 } | <d' f'>2.->\fff r4 |
  c'1\pp | c'1 | des'1 | b1 |
  c'1 | c'1 | aes1 | aes1 |
  es'1 | es'1 | es'1 | aes1 |
  es'1( | e'1\ppp\fermata) |
}
codaVc = {
  \repeat unfold 8 { c8\ff } | \repeat unfold 8 { c8 } | \repeat unfold 8 { c8 } | c2.->\fff r4 |
  es'2.~\p es'8 d'8 | c'4( aes'2) g'4 | f'4.( es'8 des'4 es'8 f'8) | g'1 |
  g,1\pp( | es1 | d1 | des1 |
  c1) | c1 | c1 | des1 |
  c1~ | c1\fermata |
}
codaCb = {
  \repeat unfold 8 { c,8\ff } | \repeat unfold 8 { c,8 } | \repeat unfold 8 { c,8 } | c,2.->\fff r4 |
  c,1\p | f,1 | f,1 | g,,1 |
  g,,1\pp | es,1 | d,1 | des,1 |
  c,1~ | c,1~ | c,1~ | c,1~ |
  c,1~ | c,1\fermata |
}
codaFluteOne = { r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | c'''4 b''8( c'''8) aes''4.-> g''8 | r8 aes''8 f'''4.-> es'''8 d'''8 c'''8 | b''2.->\fff r4 | R1*14 | }
codaFluteTwo = { g''1\ff | g''2 aes''2 | aes''1 | aes''2.->\fff r4 | R1*14 | }
codaOboeOne = { r8 g'8\ff es''4.-> d''8 des''8 c''8 | c''4 b'8( c''8) aes'4.-> g'8 | r8 aes'8 f''4.-> es''8 d''8 c''8 | b'2.->\fff r4 | R1*14 | }
codaOboeTwo = { es''1\ff | es''1 | c''1 | d''2.->\fff r4 | R1*14 | }
codaClTwo = { es'1\ff | es'2 es'2 | c'1 | d'2.->\fff r4 | R1*14 | }
codaBsnOne = { g1\ff | g2 aes2 | aes1 | aes2.->\fff r4 | R1*14 | }
codaCbsn = { c,1\ff | c,1 | c,1 | c,2.->\fff r4 | R1*14 | }
codaHnTwo = { es'1\ff | es'1 | f'1 | f'2.->\fff r4 | R1*14 | }
codaTptOne = { c''1\ff | c''1 | c''1 | b'2.->\fff r4 | R1*14 | }
codaTptTwo = { g'1\ff | g'2 aes'2 | aes'1 | aes'2.->\fff r4 | R1*14 | }
codaTptThree = { es'1\ff | es'1 | f'1 | f'2.->\fff r4 | R1*14 | }
codaTbnOne = { es'1\ff | es'1 | c'1 | d'2.->\fff r4 | R1*14 | }
codaTbnTwo = { g1\ff | g2 aes2 | aes1 | b2.->\fff r4 | R1*14 | }
codaBassTbn = { c1\ff | c1 | c1 | c2.->\fff r4 | R1*14 | }
codaTuba = { c,1\ff | c,1 | c,1 | c,2.->\fff r4 | R1*14 | }

% CODA, bars 163–178. Forte C minor (163–166), then the second theme's head returns in C minor in the cellos against the horn's motto;
% the low strings state the motto in augmentation; the violins' last motto sinks through the Neapolitan
% to C, and the violas alone turn the minor third to major at the very end.

codaClOne = {
  \partCombineApart r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 aes'8( f''4.->) es''8( d''8 c''8 | b'2.->\ff) r4 \partCombineAutomatic |
  R1*4 | r2. es'4(\pp | c''1~ | c''2 b'2) |
  R1*5 |
}
codaBassCl = {
  c1\ff | c1 | c1 | c2.->\ff r4 | R1 | R1 | R1 | R1 |
  g,1\pp( | es1 | d1 | c2 des2 | c1) | R1*3 |
}
codaBsnTwo = {
  c1\ff | c1 | c1 | c2.->\ff r4 | c1\p | f1 | f1 | g,1 |
  R1*8 |
}
codaHnOne = {
  g'1\ff | g'2 aes'2 | aes'1 | aes'2.->\ff r4 | r2. g4(\p | es'2.~ es'8 d'8 | c'2 des'4 c'4~ | c'2 b2) |
  R1*8 |
}
codaHnThree = {
  c'1\f | c'1 | c'1 | d'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*6 | g'1\ppp~ | g'1\fermata |
}
codaHnFour = {
  g1\f | g2 aes2 | aes1 | b2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*6 | c'1\ppp~ | c'1\fermata |
}
codaTimp = {
  c1:32\ff~ | c1:32~ | c1:32\< | c4->\ff r2. | R1 | R1 | R1 | g,1:32\pp |
  R1*4 | c4\pp r4 c4 r4 | c4 r4 c4 r4 | c1:32\ppp~ | c1:32\fermata |
}
codaHarpL = {
  R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 |
  R1*7 | <c, g, c>1\pp\laissezVibrer |
}
codaVlnOne = {
  r8 g''8\ff( es'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8( c'''8) aes''4.-> g''8 | r8 aes''8( f'''4.->) es'''8( d'''8 c'''8 | b''2.->\ff) r4 |
  R1*6 | r2. g'4(\pp | es''1~ | es''2.) d''4( |
  c''2 des''2) | c''1~\> | c''1\ppp\fermata |
}
codaVlnTwo = {
  r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 aes'8( f''4.->) es''8( d''8 c''8 | b'2.->\ff) r4 |
  g'1\pp | aes'1 | aes'1 | g'1 |
  es'1 | g'1 | f'1 | g'2 f'2 |
  g'1 | g'2 f'2 | g'1~ | g'1\fermata |
}
codaVla = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 aes8( f'4.->) es'8( d'8 c'8 | <d' f'>2.->\ff) r4 |
  c'1\pp | c'1 | des'1 | es'2 d'2 |
  c'1 | c'1 | aes1 | es'2 aes2 |
  es'1 | es'2 aes2 | es'1(\>^"morendo" | e'1\ppp\fermata) |
}
codaVc = {
  c8\ff \repeat unfold 7 { c8 } | \repeat unfold 8 { c8 } | \repeat unfold 8 { c8 } | c2.->\ff r4 | es'2.~\p es'8 d'8 | c'4( aes'2) g'4 | f'4.( es'8 des'4 f'8 aes'8 | c''2 b'2) |
  g,1\pp( | es1 | d1 | c2 des2 | c1) | c1 | c1~ | c1\fermata |
}
codaCb = {
  c,8\ff \repeat unfold 7 { c,8 } | \repeat unfold 8 { c,8 } | \repeat unfold 8 { c,8 } | c,2.->\ff r4 | c,1\p | f,1 | f,1 | g,,1 |
  g,,1\pp | es,1 | d,1 | c,2 des,2 | c,1~ | c,1~ | c,1~ | c,1\fermata |
}
codaFluteOne = {
  \partCombineApart r8 g''8\ff( es'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8( c'''8) aes''4.-> g''8 | r8 aes''8( f'''4.->) es'''8( d'''8 c'''8 | b''2.->\ff) r4 \partCombineAutomatic |
  R1*12 |
}
codaFluteTwo = {
  g''1\ff | g''2 aes''2 | aes''1 | aes''2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaOboeOne = {
  \partCombineApart r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 aes'8( f''4.->) es''8( d''8 c''8 | b'2.->\ff) r4 \partCombineAutomatic |
  R1*12 |
}
codaOboeTwo = {
  es''1\ff | es''1 | c''1 | d''2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaClTwo = {
  es'1\ff | es'2 es'2 | c'1 | d'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaBsnOne = {
  g1\ff | g2 aes2 | aes1 | aes2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaCbsn = {
  c,1\ff | c,1 | c,1 | c,2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaHnTwo = {
  es'1\ff | es'1 | f'1 | f'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTptOne = {
  c''1\ff | c''1 | c''1 | b'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTptTwo = {
  g'1\ff | g'2 aes'2 | aes'1 | aes'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTptThree = {
  es'1\f | es'1 | f'1 | f'2.->\ff r4 | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTbnOne = {
  es'1\f | es'1 | c'1 | d'2.->\ff r4 |
  R1*4 | g1(\pp | es'1) | d'1( |
  c'2 des'2 | c'1) | R1*3 |
}
codaTbnTwo = {
  g1\f | g2 aes2 | aes1 | b2.->\ff r4 |
  R1*12 |
}
codaBassTbn = {
  c1\f | c1 | c1 | c2.->\ff r4 |
  R1*4 | g,1(\pp | es1) | d1( |
  c2 des2 | c1) | R1*3 |
}
codaTuba = {
  c,1\f | c,1 | c,1 | c,2.->\ff r4 |
  R1*12 |
}

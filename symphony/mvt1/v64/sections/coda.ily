% CODA, bars 163–178. Forte C minor (163–166: brass take the first-theme head; fermata on the denied tutti), then the second theme's head returns in C minor in the cellos against the cor anglais's motto (167–170);
% bass clarinet, low strings and three trombones (pp chorale, tam-tam) state the motto in augmentation (171–175); Cl1 recalls the intro horn call E♭–C–B (171–173); the violins' last motto sinks through the Neapolitan
% to C, and the violas alone turn the minor third to major at the very end.

codaClOne = {
  g''1\f | g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata |
  R1*4 | r2. es'4(\pp | c''1~ | c''2 b'2) |
  R1*5 |
}
codaBassCl = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  g,1\pp( | es1) | d1( | c2 des2 | c1) | R1*3 |
}
codaBsnTwo = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | c1\pp | f1 | f1 | g,1 |
  R1*8 |
}
codaHnOne = {
  \partCombineUnisono r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 aes8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata \partCombineAutomatic |
  R1*12 |
}
codaHnThree = {
  c'1\f | c'1 | c'1\< | d'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*6 | g'1\ppp~ | g'1\fermata |
}
codaHnFour = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*6 | c'1\ppp~ | c'1\fermata |
}
codaTimp = {
  c1:32\f~ | c1:32~ | c1:32\< | c4->\ff r2 r4\fermata | R1 | R1 | R1 | g,1:32\pp |
  R1*4 | c4\pp r4 c4 r4 | c4 r4 c4 r4 | c1:32\ppp~ | c1:32\fermata |
}
codaHarpL = {
  R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 |
  R1*7 | <c, g, c>1\ppp\laissezVibrer\fermata |
}
codaVlnOne = {
  <g'' es'''>1:32\f^"div." | <g'' es'''>2:32 <aes'' es'''>2:32 | <aes'' f'''>1:32\< | <aes'' f'''>2.:32->\ff r4\fermata |
  R1*6 | r2. g'4(\pp^"unis." | es''1~ | es''2.) d''4( |
  c''2 des''2) | c''1~\> | c''1\ppp\fermata |
}
codaVlnTwo = {
  <c'' g''>1:32\f^"div." | <c'' g''>2:32 <c'' aes''>2:32 | <c'' aes''>1:32\< | <d'' aes''>2.:32->\ff r4\fermata |
  g'1\pp^"unis." | aes'1 | aes'1 | g'1 |
  es'1 | g'1 | f'1 | g'2 f'2 |
  g'1 | g'2 f'2 | g'1~\> | g'1\ppp\fermata |
}
codaVla = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 aes8( f'4.->) es'8( d'8 c'8 | <d' f'>2.->) r4\fermata |
  c'1\pp | c'1 | c'2 des'2 | es'2 d'2 |
  c'1 | c'1 | aes1 | es'2 aes2 |
  es'1 | es'2 aes2 | es'1(\>^\markup \italic "morendo" | e'1\ppp\fermata) |
}
codaVc = {
  c'2\f es'2 | es'2 f'2 | es'2\< c'2 | d'2.->\ff r4\fermata | \clef tenor es'2.~(\mp\<^\markup \italic "espr." es'8 d'8\> | c'4\! aes'2--\< g'4\!) | f'4.( es'8 des'4 f'8\< aes'8 | c''2\> b'2\!) |
  \clef bass g,1\pp( | es1) | d1( | c2 des2 | c1) | c1 | c1~\> | c1\ppp\fermata |
}
codaCb = {
  c,8\ff \repeat unfold 7 { c,8 } | \repeat unfold 8 { c,8 } | \repeat unfold 8 { c,8 } | c,2.->\ff r4\fermata | R1*4 |
  g,,1\pp | es,1 | d,1 | c,2 des,2 | c,1~ | c,1~ | c,1~\> | c,1\ppp\fermata |
}
codaFluteOne = {
  es'''1\f | es'''2 es'''2 | f'''1\< | f'''2.->\ff r4\fermata |
  R1*12 |
}
codaFluteTwo = {
  g''1\f | g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaOboeOne = {
  g''1\f | g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata |
  R1*12 |
}
codaOboeTwo = {
  es''1\f | es''1 | c''1\< | d''2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaClTwo = {
  es'1\f | es'2 es'2 | c'1\< | d'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaBsnOne = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaCbsn = {
  c,,1\f | c,,1 | c,,1\< | c,,2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaHnTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 aes8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTptOne = {
  \partCombineUnisono r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 aes'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata \partCombineAutomatic |
  R1*12 |
}
codaTptTwo = {
  r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 aes'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata |
  R1*12 |
}
codaTptThree = {
  es'1\f | es'1 | f'1\< | f'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*8 |
}
codaTbnOne = {
  es'1\f | es'1 | c'1\< | d'2.->\ff r4\fermata |
  R1*4 | g1(\pp | es'1) | d'1( |
  c'2 des'2 | c'1) | R1*3 |
}
codaTbnTwo = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata |
  R1*4 | es1\pp | g1 | f1 |
  g2 f2 | es1 | R1*3 |
}
codaBassTbn = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata |
  R1*4 | g,1(\pp | es1) | d1( |
  c2 des2 | c1) | R1*3 |
}
codaTuba = {
  c,1\f | c,1 | c,1\< | c,2.->\ff r4\fermata |
  R1*12 |
}
codaCorAnglais = { R1*4 | r2. g'4(\p^\markup \italic "espr." | es''2.~ es''8 d''8~ | d''4 c''4 des''4 c''4~ | c''2) r2 | R1*8 | }

codaPerc = \drummode { R1*8 | tt1\pp\laissezVibrer^\markup { "1: Tam-tam" \italic "soft stick, l.v." } | R1*7 | }

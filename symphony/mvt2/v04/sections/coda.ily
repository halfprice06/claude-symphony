% CODA, bars 91-104 (3/4). Over a tonic pedal (violas, cellos, basses ppp) the harp plays the theme's rising head
% and the timpani answer with the motto's tail on their four drums (E flat-D flat-C, A flat): melodic moments for
% instruments movement I kept from melody. Close: plagal iv-I with D flat-C in the top voice (Vln I),
% ending on C5 on top, the pitch movement I ended on and this movement began with.

codaHarpR = {
  r2 es'8(\p f'8 | aes'4. c''8 es''4) | R2.*2 |
  es'8( f'8 aes'8 c''8 es''8 aes''8) | c'''2.^\markup \italic "l.v." | R2.*2 |
  R2.*4 |
  <c' es' aes' c''>2.\arpeggio | R2. |
}
codaHarpL = {
  aes,,2.\p | R2.*3 |
  aes,,2.\pp | R2.*3 |
  R2.*4 |
  <aes,, es, aes,>2.\ppp\arpeggio | R2. |
}
codaTimp = {
  R2.*2 | es4\p des4 c4 | aes,2. |
  R2.*2 | es4\pp des4 c4 | aes,2. |
  R2.*2 | aes,2.:32\ppp~ | aes,2.:32~ | aes,2.:32~ | aes,2.:32\fermata |
}
codaVla = {
  <c' es'>2.~\ppp | <c' es'>2.~ | <c' es'>2.~ | <c' es'>2.~ | <c' es'>2.~ | <c' es'>2.~ | <c' es'>2.~ | <c' es'>2. |
  f'2.\pp | fes'2. | es'2.~ | es'2.~ | es'2.~\> | es'2.\ppp\fermata |
}
codaVc = {
  aes,2.~\ppp | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2. |
  des2.\pp | des2. | aes,2.~ | aes,2.~ | aes,2.~\> | aes,2.\ppp\fermata |
}
codaCb = {
  aes,,2.~\ppp | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2. |
  des,2.\pp | des,2. | aes,,2.~ | aes,,2.~ | aes,,2.~\> | aes,,2.\ppp\fermata |
}
codaVlnOne = {
  R2.*8 |
  des''2.(\pp | des''2. | c''2.~ | c''2.~ | c''2.~\> | c''2.)\ppp\fermata |
}
codaVlnTwo = {
  R2.*8 |
  aes'2.\pp | aes'2. | aes'2.~ | aes'2.~ | aes'2.~\> | aes'2.\ppp\fermata |
}
codaHnThree = { R2.*8 | aes2.\pp | aes2. | aes2.~ | aes2.~ | aes2.~\> | aes2.\ppp\fermata | }
codaHnFour = { R2.*8 | f2.\pp | fes2. | es2.~ | es2.~ | es2.~\> | es2.\ppp\fermata | }

% CODA, bars 83-92 (3/4). c013: one harp/timpani exchange instead of two (85-88 of v13 cut; A&S PDF 448, 455: proportion of coda to reprise).
% (old header) CODA, bars 91-104 (3/4). Over a tonic pedal (violas, cellos, basses ppp) the harp plays the theme's rising head
% and the timpani answer with the motto's tail on their four drums (E flat-D flat-C, A flat): melodic moments for
% instruments movement I kept from melody. Close: plagal iv-I with D flat-C in the top voice (Vln I),
% ending on C5 on top, the pitch movement I ended on and this movement began with.

codaHarpR = {
  aes'4. c''8 es''4) | R2.*3 |
  R2.*4 |
  <c' es' aes' c''>2.\arpeggio | R2. |
}
codaHarpL = {
  aes,,2. | R2.*3 |
  R2.*4 |
  <aes,, es, aes,>2.\ppp\arpeggio | R2. |
}
codaTimp = {
  R2. | es4\pp des4 c4 | aes,2. | R2. |  % c019: answer at 84-85, heard alone; Vln I's tail E flat-D-D flat-C follows at 85 (no two statements of the tail at once)
  R2.*2 | aes,2.:32\ppp~ | aes,2.:32~ | aes,2.:32~ | aes,2.:32\fermata |
}
codaVla = {
  <c' es'>2.~\ppp^\markup \italic "(div.) change bow at will" | <c' es'>2.~ | <c' es'>2. | <c' f'>2. |
  f'2.\pp^\markup \italic "unis." | fes'2. | es'2.~ | es'2.~ | es'2.~\> | es'2.\ppp\fermata |
}
codaVc = {
  aes,2.~\ppp^\markup \italic "change bow at will" | aes,2.~ | aes,2.~ | aes,2. |
  des2.\pp | des2. | aes,2.~ | aes,2.~ | aes,2.~\> | aes,2.\ppp\fermata |
}
codaCb = {
  aes,,2.~\ppp^\markup \italic "change bow at will" | aes,,2.~ | aes,,2.~ | aes,,2. |
  des,2.\pp | des,2. | aes,,2.~ | aes,,2.~ | aes,,2.~\> | aes,,2.\ppp\fermata |
}
% c010: Vln I enters at 89: E flat5-D5 (89-90), then D flat5-C5 (91-93), so the last top line is the motto's tail E flat-D-D flat-C
% at movement I's pitch, one note per bar; it supplies the D natural the timpani (A flat, C, D flat, E flat) cannot play (A&S PDF 600-603).
codaVlnOne = {
  R2.*2 | es''2.\pp\upbow | d''2.\downbow |
  des''2.\upbow | des''2.\downbow | c''2.~\upbow | c''2.~\downbow | c''2.~\upbow\> | c''2.\downbow\ppp\fermata |
}
codaVlnTwo = {
  R2.*4 |
  aes'2.\pp | aes'2. | aes'2.~^\markup \italic "change bow at will" | aes'2.~ | aes'2.~\> | aes'2.\ppp\fermata |
}
codaHnThree = { R2.*4 | aes2.\pp | aes2. | aes2.~ | aes2\> r4\! | R2. | R2.\fermata | }
codaHnFour = { R2.*4 | f2.\pp | fes2. | es2.~ | es2\> r4\! | R2. | R2.\fermata | }
% c008: clarinets take the held A flat / E flat from the horns and die away (Rimsky-Korsakov PDF 130: clarinets for morendo; brass leave first).
codaClOne = { R2.*6 | aes2.~\pp | aes2.~ | aes2.~\>^\markup \italic "morendo" | aes2.\ppp\fermata | }
codaClTwo = { R2.*6 | es2.~\pp | es2.~ | es2.~\> | es2.\ppp\fermata | }

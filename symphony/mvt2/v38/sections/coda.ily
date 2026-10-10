% CODA, bars 83-92 (3/4). c013: one harp/timpani exchange instead of two (85-88 of v13 cut; A&S PDF 448, 455: proportion of coda to reprise).
% (old header) CODA, bars 91-104 (3/4). Over a tonic pedal (violas, cellos, basses ppp) the harp plays the theme's rising head
% and the timpani answer with the motto's tail on their four drums (E flat-D flat-C, A flat): melodic moments for
% instruments movement I kept from melody. Close: plagal iv-I with D flat-C in the top voice (Vln I),
% ending on C5 on top, the pitch movement I ended on and this movement began with.

codaHarpR = {
  << \new Voice \with { \remove "Note_performer" } { \voiceOne aes4.(-\flageolet c'8-\flageolet es'4-\flageolet) } \new Voice { \voiceTwo \hideNotes aes'4. c''8 es''4 \unHideNotes } >> | R2.*3 |  % c026: harmonics (Adler part 1 PDF 116: practical range C3-A5 written; accompany very lightly - strings ppp)
  R2.*4 |
  <c' es' aes' c''>2.\arpeggio | R2. |
}
codaHarpL = {
  aes,,2. \ottava #0 | R2.*3 |  % c026: closes the 8 bassa line from 71
  R2.*4 |
  <aes,, es, aes,>2.\ppp\arpeggio | R2. |
}
codaTimp = {
  R2. | es4\pp des4 c4 | aes,2. | R2. |  % c019: answer at 84-85, heard alone; Vln I's tail E flat-D-D flat-C follows at 85 (no two statements of the tail at once)
  R2.*2 | aes,2.:32\ppp~ | aes,2.:32~ | aes,2.:32~ | aes,2.:32\fermata |
}
codaVla = {
  <c' es'>2.~\ppp^\markup \italic "(div.) change bow at will" | <c' es'>2.~ | <c' es'>2. | <c' f'>2. |
  % c020: unis. sul C an octave lower (F3-F flat3-E flat3 with horn 4, then alone): the E/F flat-E flat thread on the viola's C string
  % (cyclic-notes, critic 126; Adler part 1 PDF 86); clarinet 1 keeps the upper octave.
  f2.\pp^\markup \italic "unis., sul C" | fes2. | es2.~ | es2.~ | es2.~\> | es2.\ppp\fermata |
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
% c030: the tail E flat-D-D flat-C (85-90) goes to clarinet 1; Vln I takes the C5 over from it at 89 and holds it to the end,
% so the movement still ends on Vln I's C5 (its first sound in bar 1), but its last tail is not the sound movement I ended with
% (Vln I alone, E flat5-D5-(C5)-D flat5-C5, ppp). Bowing keeps an up-bow entry and a down-bow ending (c016).
codaVlnOne = {
  R2.*6 | c''2.~\pp\upbow | c''2.~\downbow | c''2.~\upbow\> | c''2.\downbow\ppp\fermata |
}
codaVlnTwo = {
  R2.*4 |
  aes'2.\pp | aes'2. | aes'2.~^\markup \italic "change bow at will" | aes'2.~ | aes'2.~\> | aes'2.\ppp\fermata |
}
% c030: horns 3-4 con sordino for their last two bars (the only muted brass in the symphony so far; Rimsky-Korsakov PDF 44:
% muted brass give an effect of distance, tender in piano; mute in during 82-86).
codaHnThree = { R2.*4 | aes2.\pp^\markup \italic "con sord." | aes2. | aes2.~ | aes2\> r4\! | R2. | R2.\fermata | }
codaHnFour = { R2.*4 | f2.\pp | fes2. | es2.~ | es2\> r4\! | R2. | R2.\fermata | }
% c008: clarinets take the held A flat / E flat from the horns and die away (Rimsky-Korsakov PDF 130: clarinets for morendo; brass leave first).
% c020: clarinet 1 enters at 87 with the F4-F flat4-E flat4 line the violas leave; clarinet 2 takes A flat3.
% c030: clarinet 1 plays the last tail E flat5-D5-D flat5-C5 (85-90) and hands the C5 to Vln I at 89 (Rimsky-Korsakov PDF 130:
% clarinets decrease their tone to a breath); clarinet 2 takes the F4-F flat4-E flat4 line over the violas' sul C octave.
codaClOne = { R2.*2 | es''2.(\pp^\markup \italic "dolce" | d''2.) \breathe | des''2.(\pp | des''2. | c''2.~ | c''2) r4 | R2. | R2.\fermata | }
codaClTwo = { R2.*4 | f'2.\pp | fes'2. \breathe | es'2.~ | es'2.~ | es'2.~\>^\markup \italic "morendo" | es'2.\ppp\fermata | }

% CLOSING, bars 69–76.
% c103 (scratch): 69–71 bass A♭–C | B♭–D♮ | E♭: I–I6 | ii7–vii°7/V | V7 (no third arrival on F minor after 63–64 and the deceptive cadence at 68; Tchaikovsky 6/i closing pattern).
% c102: 69–71 bass A♭–E♮ | F–D♭ | E♭: I–V6/5 of vi | vi–ii6/5 | V7 (was root-position I–vi–IV–ii–V7); viola fifths with the bass at 69, 70, 71→72 removed. Forte codetta in A♭ (Tempo I), then the flute's darkened motto over an A♭ pedal.

closFluteOne = {
  c'''2.~(\f c'''8 bes''8 | aes''4 f'''2-- es'''4) | des'''4.( c'''8 bes''4 des'''8 f'''8) | aes'''4-> es'''4-> c'''2-> |
  r2. c''4(\p_\markup \italic "espr." | aes''2.~\> aes''8 g''8 | ges''2 f''4 es''8 f''8)\pp | R1 |
}
% c131: Fl 2 joins Fl 1 on the tune 69-72 (a2): Rimsky-Korsakov PDF 75, a trumpet melody (Tpt 1 + Ob 1 at C5) needs two flutes in the octave above in the top register;
% Fl 2 no longer doubles Tbn 1's E-flat/F an octave above (same page: woodwinds should not double a trombone in the octave above)
closFluteTwo = { c'''2.~(\f c'''8 bes''8 | aes''4 f'''2-- es'''4) | des'''4.( c'''8 bes''4 des'''8 f'''8) | aes'''4-> es'''4-> c'''2-> | R1*4 | }
closOboeOne = {
  c''2.~(\f c''8 bes'8 | \once \override NoteColumn.force-hshift = #0.9 aes'4 f''2-- es''4) | des''4.( c''8 bes'4 des''8 f''8) | aes''4-> es''4-> c''2-> |
  R1*4 |
}
closOboeTwo = { c''2\f aes'2 | des''2 ces''2 | bes'1 | c''4-> c''4-> c''2-> | R1*4 | }
% c131: Cl 1·2 a2 on the counter (first-theme head) an octave above Hn 1·2 in unison; Rimsky-Korsakov PDF 75: two horns in unison need three or four winds in the
% octave above in forte (with Vln II); Cl 2's A-flat/G stay in Tpt 2
closClOne = { r8 es'8(\f c''4.->) bes'8( aes'8 g'8 | aes'8 bes'8 c''8 des''8) f''4.-> es''8 | des''8( c''8 bes'8 aes'8) g'4.-> bes'8 | aes'4-> c''4-> aes'2-> | R1*4 | }
closClTwo = { r8 es'8(\f c''4.->) bes'8( aes'8 g'8 | aes'8 bes'8 c''8 des''8) f''4.-> es''8 | des''8( c''8 bes'8 aes'8) g'4.-> bes'8 | aes'4-> c''4-> aes'2-> | R1*4 | }
closBassCl = {
  aes,2\f c2 | bes,2 d2 | es1 | aes,4-> es4-> aes,2-> |
  R1*4 |
}
closBsnOne = { c'2\f es'2 | f'2 f'2 | des'1 | c'4-> es'4-> c'2-> | R1*4 | }
closBsnTwo = {
  aes,2\f c2 | bes,2 d2 | es1 | aes,4-> es4-> aes,2-> |
  R1*4 |
}
closCbsn = {
  aes,,2\f c,2 | bes,,2 d,2 | es,1 | aes,,4-> es,4-> aes,,2-> |
  R1*4 |
}
closHnOne = {
  \partCombineUnisono r8 es8\f( c'4.->) bes8( aes8 g8 | aes8 bes8 c'8 des'8) f'4.-> es'8 | des'8( c'8 bes8 aes8) g4.-> bes8 | aes4-> c'4-> aes2-> \partCombineAutomatic |
  R1*4 |
}
closHnTwo = {
  r8 es8\f( c'4.->) bes8( aes8 g8 | aes8 bes8 c'8 des'8) f'4.-> es'8 | des'8( c'8 bes8 aes8) g4.-> bes8 | aes4-> c'4-> aes2-> |
  R1*4 |
}
closHnThree = { aes2\f aes2 | aes2 aes2 | g1 | aes4-> aes4-> aes2-> | R1*4 | }
closHnFour = { es2\f es2 | f2 f2 | es1 | es4-> es4-> es2-> | r4 aes2.\pp~ | aes1~ | aes1~ | aes1 | } % c156: Hn 4 joins the pp pedal on beat 2 of 73 (cellos and basses take the downbeat), so it has a breath between the f codetta and the soft entry (Adler PDF 284, 292)
closTptOne = {
  c''2.~(\f c''8 bes'8 | aes'4 f''2-- es''4) | des''4.( c''8 bes'4 des''8 f''8) | aes''4-> es''4-> c''2-> |
  R1*4 |
}
closTptTwo = { aes'2\f aes'2 | \once \override NoteColumn.force-hshift = #1.7 aes'1 | g'1 | aes'4-> aes'4-> aes'2-> | R1*4 | }
% c149: Tbn 1·2, B.tbn and tuba rest 69-71 and enter f on the 72 cadence chord: after 27 bars' rest an mf re-entry is colourless (Rimsky-Korsakov PDF 136);
% they enter on the stop chord as at 26 and 138, and the trumpet's codetta tune (Tpt 1 + Ob 1 + Fl a2) is no longer padded by four low-brass parts at its own pitch (PDF 138-139)
closTbnOne = {
  R1*3 | c'4->\f c'4-> c'2-> |
  R1*4 |
}
closTbnTwo = {
  R1*3 | aes4->\f aes4-> aes2-> |
  R1*4 |
}
closBassTbn = {
  R1*3 | aes,4->\f es4-> aes,2-> |
  R1*4 |
}
closTuba = {
  R1*3 | aes,,4->\f es,4-> aes,,2-> |
  R1*4 |
}
% c098: 71–72 timpani roll mf< f, so the cadence chord is f in every part (was a lone ff)
closTimp = { aes,4\f r8 aes,8 r2 | R1 | es1:32\mf\< | aes,4->\f es4-> aes,2-> | R1*3 | aes,1:32\ppp | }
closVlnOne = {
  c'''2.~(\f c'''8 bes''8 | aes''4) f'''2--( es'''4) | \ottava #1 des'''4.( c'''8 bes''4 des'''8 f'''8) | aes'''4->\downbow es'''4->\downbow c'''2->\downbow \ottava #0 |
  R1*4 |
}
closVlnTwo = { r8 es'8\f( c''4.->) bes'8( aes'8 g'8 | aes'8 bes'8 c''8 des''8) f''4.-> es''8 | des''8( c''8 bes'8 aes'8) g'4.-> bes'8 | aes'4->\downbow c''4->\downbow aes'2->\downbow | es'1\pp | es'1 | ges'1 | fes'1 | }
% c090: 69–71 broken-chord eighths from the second group's accompaniment (Vc 56–68, harp 47–55) instead of repeated
% chords (each half-bar starts on the third or fifth, not doubling the bass root), so the hammered-eighth tutti stays the first theme's sound (27, 131, 167) and the A♭-major combination keeps its own figure.
closVla = { c'8\f(^"unis." aes8 c'8 es'8) es'8( c'8 aes8 c'8) | f'8( des'8 bes8 des'8) f'8( aes'8 ces''8 aes'8) | g8( bes8 des'8 es'8) g'8( es'8 bes8 des'8) | <c' es'>4->\downbow <c' es'>4->\downbow <c' es'>2->\downbow | c'1\pp | c'1 | c'1 | des'1 | }
closVc = {
  aes2\f c2 | bes,2 d2 | es1 | aes4->\downbow es4->\downbow aes,2->\downbow |
  aes1\pp~ | aes1~ | aes1~ | aes1 |
}
closCb = {
  aes,,2\f c,2 | bes,,2 d,2 | es,1 | aes,,4->\downbow es,4->\downbow aes,,2->\downbow |
  aes,,1\pp~ | aes,,1~ | aes,,1~ | aes,,1 |
}
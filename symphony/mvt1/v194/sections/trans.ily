% TRANSITION, bars 33–46.
% c108: 41 strings and woodwinds sf > mf, so the four horns' call (41 beat 4 - 42) speaks over the held chord (Rimsky-Korsakov PDF 129, sf-dim.; Ex. 253 PDF 418)
% c102: Cb 34 A♭ (i–iv6–VII, Handel Op. 6/6 Musette via Aldwell & Schachter Ex. 17-4); Vla 45–46 c'2 es'2 | bes2 des'2 (no fifths with Ob 1 at 46 or with the bass at 47; the 7th D♭ resolves to C at 47).

transFluteOne = {
  c'''8->\ff r8 r4 r2 | R1*5 | \partCombineSoloI \soloStemsOn r2^\markup \bold "1." d''8\mf\<( es''8 f''8 bes''8) | d'''2-> bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  \partCombineAutomatic \soloStemsOff g'''1\sf\>~ | g'''2\mf f'''2\> | es'''4\p r4 r2 | R1*3 |
}
transFluteTwo = {
  g''8->\ff r8 r4 r2 | R1*7 | g''1\sf\>~ | g''2\mf f''2\> |
  es''4\p r4 r2 | R1*3 |
}
transOboeOne = {
  c''8->\ff r8 r4 r2 | R1*3 | \partCombineSoloI \soloStemsOn r2 r8 bes'8\mf( ges''4->~ | ges''8) f''8( fes''8 es''8) r2 |
  r2 d''8\mf\<( es''8 f''8 bes''8) | d''2-> r16 c''16( d'' es'' f'' es'' f'' fis'') |
  \partCombineAutomatic \soloStemsOff g''1\sf\>~ | g''2\mf f''2\> | es''4\p r4 r2 | R1 |
  % c161: 45 dotted cell aes'4. g'8 anticipates the second theme's own cadence figure (bar 52 aes'4. g'8 f'2; Sebesky PDF 206-207, Tchaikovsky 6/i bars 86-88)
  bes'2(\p aes'4. g'8 | f'2 es'4) r4 |
}
transOboeTwo = {
  g'8->\ff r8 r4 r2 | R1*7 | g'1\sf\>~ | g'2\mf f'2\> |
  es'4\p r4 r2 | R1*3 |
}
transClOne = {
  es''8->\ff r8 r4 r2 | R1 | bes'1\p( | g'1) | R1 |
  % cycle 77: winds take the half-bar answers to Vln I at 37-40 (Ob 1, Cl 1 double the viola answer at the violin octave; Fl 1/Ob 1 answer at 39)
  \partCombineSoloI \soloStemsOn r2 r8 c''8\mf( aes''4->~ | aes''8) g''16( ges''16 f''4) r2 | \partCombineAutomatic \soloStemsOff R1 |
  des''1\sf\> | des''2\mf bes'2\> | bes'4\p r4 r2 | R1*3 |
}
transClTwo = {
  c''8->\ff r8 r4 r2 | R1 | f'1\p( | es'1) | R1*4 |
  % c164: B-flat4 at 41-42 (was B-flat3, in unison with the horns' call note and inside the horns; c124 F5 open item): the call lands on its B-flat3 alone
  % (Adler adler1 PDF 245: Strauss lifts the held winds so the entering line is heard clearly; PDF 257: a unison doubling robs both timbres); Cl 2 joins Cl 1's B-flat4 at 42.3 and takes G4 in the p chord at 43 (Hn 4 keeps G3)
  bes'1\sf\> | \after 2 \> bes'1\mf | g'4\p r4 r2 | R1*3 |
}
% c138: 34-36 tail slurred in two breath arcs (bes-f, f-es), like Cl 1 at 129-130; the espressivo solo was tongued note by note after beat 2 of 34
% (Casanelles, Hyperorchestra PDF 151: legato turns successive pitches into a line, the arc as breath; PDF 152: notation must state the connection, it cannot be left to the notes)
transBsnOne = {
  \soloStemsOn \set Staff.soloText = "1. Solo" r8 g8\f_\markup \italic "espr."( es'4.->) d'8(\> des'8 c'8 | \set Staff.soloText = "1." c'4)\mf bes8( aes8 g4 f4) | f2( aes2 | g2 es2) \breathe |
  \soloStemsOff ges1\mf\< | aes1 | aes1 | aes1\f |
  R1*6 |
}
transBsnTwo = {
  R1*4 | es1\mf\< | f1 | bes,1 |
  bes,1\f | es1\sf\> | es1\mf\> | es4\p r4 r2 |
  R1*3 |
}
transCbsn = {
  R1*8 | es,1\sf\>~ | es,1\mf\> | es,4\p r4 r2 |
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
  % c124: Hn 4 F3 at 39-40 (was A-flat3 with Bsn 1): horns take the concords, the bassoon the seventh (crossing, Rimsky-Korsakov PDF 108); the fifth F is no longer missing at 39
  R1*4 | ges1\p\< | aes1 | f1 |
  f1\f | g2.\ff es4( | c'4 bes2.)\> | g4\p r4 r2 |
  R1*3 |
}
% c108: 43 trumpets, trombones, tuba drop out before the wind/string p chord: diminuendo by eliminating brass first (Rimsky-Korsakov PDF 130)
% c128: 41 trumpets, trombones, tuba give a short sf eighth and stop; strings, woodwinds and timpani hold the chord sf > mf, so the horns' call (G3-C4, the trombones' own pitches) is heard alone (Adler, sforzando scoring, adler2 PDF 189-190, Ex. XV-35)
% c114 (superseded at 41 by c128): 41 brass sf > mf like the strings and woodwinds, so the four horns' call (one line = two trumpets' weight in forte, Rimsky-Korsakov PDF 51) is not covered by seven brass parts at f
% c114: 41-43 Ob 2 and Cl 1 exchange lines: the oboes hold G5/G4 (octave), the D♭ goes to Cl 1 (Rimsky-Korsakov PDF 90 rule 4: no discords between the two oboes)
% c098 (superseded at 41 by c114): 41–42 trumpets, trombones, tuba f under the horns' ff call (Rimsky-Korsakov: horns one degree stronger than the other brass; same grading as 27–32)
transTptOne = {
  c''8->\ff r8 r4 r2 | R1*7 | bes'8->\sf r8 r4 r2 | R1 |
  R1 | R1*3 |
}
transTptTwo = {
  g'8->\ff r8 r4 r2 | R1*7 | g'8->\sf r8 r4 r2 | R1 |
  R1 | R1*3 |
}
transTptThree = {
  R1*8 | des'8->\sf r8 r4 r2 | R1 | R1 |
  R1*3 |
}
transTbnOne = {
  c'8->\ff r8 r4 r2 | R1*6 | bes1\f | bes8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transTbnTwo = {
  g8->\ff r8 r4 r2 | R1*6 | f1\f | g8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transBassTbn = {
  c8->\ff r8 r4 r2 | R1*6 | bes,1\f | es8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transTuba = {
  c,8->\ff r8 r4 r2 | R1*7 | es,8->\sf r8 r4 r2 | R1 |
  R1 | R1*3 |
}
transTimp = {
  c8->\ff r8 r4 r2 | R1^\markup \small "muta C in B♭" | R1*5 | bes,1:32\pp\< |
  es1:32\ff\>~ | es1:32\mf\>~ | es1:32\pp | R1^\markup \small "muta B♭ in C" |
  R1*2 |
}
% c135: no 8va at 40-43 (top note G6, four ledger lines; Gould PDF 47: strings up to five ledger lines; keep the run's contour visible)
transVlnOne = {
  c'''8->\downbow\ff r8 r4 r2 | R1 | r8 f'8\mf( des''4.->) c''8( ces''8 bes'8 | bes'4) a'8( bes'8) g'4.-> f'8 |
  r8 bes'8\<( ges''4.->) f''8( fes''8 es''8) | r8 g''8( aes''4.->) g''8( ges''8 f''8) | d''8( es''8 f''8 bes''8) d'''2-> | f''8( g''8 aes''8 c'''8) bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  g'''1\sf\>~ | g'''2\mf f'''2\> | es'''4\p r4 r2 | R1*3 |
}
% c139: double stop, not triple, after the slurred sixteenth run at the end of 32 (Rimsky-Korsakov PDF 130: string anacrusis runs should not lead up to chords of three or four notes); G3 stays in Vla and Vc
transVlnTwo = {
  <es' c''>8->\downbow\ff r8 r4 r2 | R1*3 | bes'1:32\p\< | aes'1:32 |
  aes'1:32 | aes'1:32\f | g''1\sf\>~ | g''2\mf f''2\> |
  des'1\pp | es'1 | es'1 | des'2 des'2 |
}
% c142: 35 Vla tail D-flat4 on beat 3, D4 on beat 4 (was D4 half note from beat 3): the Vln I head F-D-flat is a real transposition of the Vla's C-A-flat at 34, so its
% D-flat5 sounded against the Vla's D-natural4; now B-flat minor holds under the D-flat and B-flat7 (C-flat passing ninth) follows on beat 4 (Aldwell & Schachter PDF 265)
transVla = {
  % c151: entry at 34 mp (was mf): it starts on the C4 the bassoon solo is holding and rises through its register; Adler adler1 PDF 226: an accompanied bassoon is swallowed, so mark the others softer
  <c g es'>8->\downbow\ff r8 r4 r2 | r8 c'8\mp( aes'4.->) g'8( ges'8 f'8 | f'4) e'8( f'8) des'4 d'4 | es'1 |
  ges'2:32\p\< r8 bes8( ges'4->~ | ges'8) f'8( fes'8 es'8) r8 c'8( aes'4->~ | aes'8) g'16( ges'16 f'4) f'2:32 | <d' f'>1:32\f |
  <es' g'>1:32\sf\> | <es' g'>1:32\mf\> | bes1\pp | bes1 |
  c'2 es'2 | bes2 des'2 |
}
transVc = {
  <c, g, es>8->\downbow\ff r8 r4 r2 | R1 |
  % c137: 35-36 Vc doubles the bass B-flat/E-flat an octave above the Cb instead of the bassoon solo's last two bars at unison: the solo ends in its own colour
  % (Adler PDF 228: Stravinsky changes colour without breaking up a phrase; PDF 229: at-pitch doubling in one register swallows the line)
  bes,1\p | es1 |
  ges1\< | aes1 | aes1 | aes1\f |
  g1\sf\> | g1\mf\> | g1\pp | g1 |
  % c132: 46 Vc holds A♭3 from 45 (was F3): ii6 becomes ii6/5, its seventh prepared and resolving A♭–G into V7 (Aldwell & Schachter PDF 177-178, 183)
  aes1 | aes2 g4 \clef tenor es4(\mf | % c115: clef before the pickup, between phrases (Gould PDF 22)
}
transCb = {
  c,1\fp | aes,,1 | bes,,1 | es,1 |
  es,1\< | f,1 | bes,,1 | bes,,1\f |
  es,1\sf\>~ | es,1\mf\>~ | es,1\pp | des,1 |
  c,1 | des,2 es,2\upbow |
}

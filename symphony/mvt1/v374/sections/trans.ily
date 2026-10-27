% TRANSITION, bars 33–46.
% c108: 41 strings and woodwinds sf > mf, so the four horns' call (41 beat 4 - 42) speaks over the held chord (Rimsky-Korsakov PDF 129, sf-dim.; Ex. 253 PDF 418)
% c102: Cb 34 A♭ (i–iv6–VII, Handel Op. 6/6 Musette via Aldwell & Schachter Ex. 17-4); Vla 45–46 c'2 es'2 | bes2 des'2 (no fifths with Ob 1 at 46 or with the bass at 47; the 7th D♭ resolves to C at 47).

transFluteOne = {
  c'''8->\ff r8 r4 r2 | R1*5 | \partCombineSoloI \soloStemsOn r2^\markup \bold "1." d''8\mf\<( es''8 f''8 bes''8) | d'''2-> bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  % c179: Fl 1 takes only the sf attack of G6 and leaves on beat 3; Fl 2 (G5), Ob and Vln I make the diminuendo. G6 is in the flute's shrill register, where the player
  % can only play loud (Adler adler1 PDF 185); Dvorak, Slavonic Dance 8 m. 33, moves the piccolo down so that every instrument in the ff-p diminuendo is in a
  % controllable range (Adler adler2 PDF 213), and the diminuendo is orchestrated by drop-out (PDF 202, 215). The horns' call at 41.4 enters under a cleared top.
  \partCombineApart \soloStemsOff g'''2\sf r2 | R1 | R1 | \partCombineAutomatic R1*3 |
}
transFluteTwo = {
  g''8->\ff r8 r4 r2 | R1*7 | g''1\sf\>~ | g''2\mf f''2\> |
  es''4\p r4 r2 | R1*3 |
}
transOboeOne = {
  c''8->\ff r8 r4 r2 | R1*3 | \partCombineSoloI \soloStemsOn r2 r8 bes'8\mf( ges''4->~ | ges''8) f''8( fes''8 es''8) r2 |
  r2 d''8\mf\<( es''8 f''8 bes''8) | d''2-> r16 c''16( d'' es'' f'' es'' f'' fis'') |
  \partCombineApart \soloStemsOff g''1\sf\>~ | g''2\mf f''2\> | \partCombineAutomatic es''4\p r4 r2 | R1 | % c255: 41-42 apart from the tie's start, so both halves of 42 take two stems (was two stems, then one; Gould PDF 61)
  % c274: the 45-46 link moves to Cl 1 (Adler adler1 PDF 270: Copland drops the oboe in its low register in a quiet passage "for it honks too much";
  % PDF 238: the woodwinds that introduce Schubert's second theme are the clarinets). The oboes rest from 44 to 68.
  R1*2 |
}
transOboeTwo = {
  % c306: Ob 2 stops on beat 3 of 42 (was f'2\> | es'4\p): F4-E-flat4 is the oboe's lowest fifth, "the most difficult to control"
  % (Sebesky PDF 71), and the p E-flat4 was the only oboe note left there after c274 moved the 45-46 link to Cl 1. Ob 1, Fl 2 and Vln II keep F5-E-flat5;
  % E-flat stays in Bsn 2, Cbsn and Cb. Diminuendo by elimination, as at 116 (c179).
  g'8->\ff r8 r4 r2 | R1*7 | g'1\sf\>~ | g'2\mf r2\! |
  R1*4 |
}
transClOne = {
  es''8->\ff r8 r4 r2 | R1 | r4 bes'2.\p( | g'1) | R1 | % c357: 35 pad from beat 2 (was beat 1, Cl 2 on F4 = Vln I's pickup at 35.1.5), as Vln II at 37 (c294); Adler adler2 PDF 205 (harmony after the first offbeat), 213
  % cycle 77: winds take the half-bar answers to Vln I at 37-40 (Ob 1, Cl 1 double the viola answer at the violin octave; Fl 1/Ob 1 answer at 39)
  \partCombineSoloI \soloStemsOn r2 r8 c''8\mf( aes''4->~ | aes''8) g''16( ges''16 f''4) r2 | \partCombineAutomatic \soloStemsOff R1 |
  % c183: 41-42 E-flat5 (was D-flat5): the medial caesura is a V triad; the 7th D-flat enters with the p chord at 43 and passes to the bass at 44 (V8-7, then V4/2-I6; Aldwell & Schachter PDF 99, 101, 117)
  es''1\sf\> | es''2\mf bes'2\> | \partCombineChords bes'4\p r4 r2 | \partCombineAutomatic R1 | % c255: 43 one stem (Gould PDF 60)
  % c274: Cl 1 takes the link into the second theme (was Ob 1): c161's notes, B-flat4 down to E-flat4 in the chalumeau-throat register at p, poco rit.; E-flat4 on beat 3 of 46 still hands to Hn 1's E-flat3 pickup
  % c298: dolce and a diminuendo into the hand-off to Hn 1 (Adler adler1 PDF 210: throat tones are pale; PDF 212 Ex. VII-63: soft clarinet lines marked dolce with hairpins)
  \partCombineSoloI \soloStemsOn bes'2--(\p_\markup \italic "dolce" aes'4. g'8 | f'2\> es'4)\! r4 \soloStemsOff \partCombineAutomatic |
}
transClTwo = {
  c''8->\ff r8 r4 r2 | R1 | r4 f'2.\p( | es'1) | R1*4 | % c357: as Cl 1
  % c164: B-flat4 at 41-42 (was B-flat3, in unison with the horns' call note and inside the horns; c124 F5 open item): the call lands on its B-flat3 alone
  % (Adler adler1 PDF 245: Strauss lifts the held winds so the entering line is heard clearly; PDF 257: a unison doubling robs both timbres); Cl 2 joins Cl 1's B-flat4 at 42.3 and takes G4 in the p chord at 43 (Hn 4 keeps G3)
  bes'1\sf\> | \after 2 \> bes'1\mf | g'4\p r4 r2 | R1*3 |
}
% c138: 34-36 tail slurred in two breath arcs (bes-f, f-es), like Cl 1 at 129-130; the espressivo solo was tongued note by note after beat 2 of 34
% (Casanelles, Hyperorchestra PDF 151: legato turns successive pitches into a line, the arc as breath; PDF 152: notation must state the connection, it cannot be left to the notes)
transBsnOne = {
  \soloStemsOn \set Staff.soloText = "1. Solo" r8 g8\f-\tag #'part ^\markup \bold "Solo"_\markup \italic "espr."( es'4.->) d'8(\> des'8 c'8 | \set Staff.soloText = "1." c'4--)\mf bes8( aes8 g4 f4) | f2( aes2 | g2 es2) \breathe |
  % c267: 37 B-flat3 (was G-flat3, a unison with Hn 4): the soft E-flat-minor-seventh in two bassoons and two horns now has four real parts, crossed Bsn 2 E-flat3 / Hn 4 G-flat3 / Bsn 1 B-flat3 / Hn 3 D-flat4 (Rimsky-Korsakov PDF 108: crossing for blend in soft four-part bassoon-horn harmony); B-flat3 falls to A-flat3 at 38
  \soloStemsOff bes1\mf\< | aes1 | aes1 | aes1\f |
  R1*6 |
}
transBsnTwo = {
  R1*4 | es1\mf\< | f1 | bes,1 |
  % c357: 41-43 B-flat2 held from 40 (was E-flat3, the pitch of the four-horn call's pickup at 41.4): the call starts on its own E-flat3, not inside a held unison
  % (Adler adler2 PDF 213: Dvorak delays the oboe entrance so the tune is clearer; PDF 229: like pitches at unison swallow a line; as c164 for Cl 2). The E-flat stays in Cb, Cbsn, Vla, Cl 1.
  bes,1\f | bes,1\sf\> | bes,1\mf\> | bes,4\p r4 r2 |
  R1*3 |
}
transCbsn = {
  R1*8 | es,1\sf\>~ | es,1\mf\> | es,4\p r4 r2 |
  R1*3 |
}
transHnOne = {
  g'8->\ff r8 r4 r2 | R1*7 | \partCombineUnisono r2. es4(\ff | c'4 bes2.)\> |
  % c198: 44 diminuendo on the suspended C (7-6 over the D-flat bass of V4/2), Hn 2 with it (shared staff): A&S PDF 348, the suspension is weighted, its resolution softer
  \partCombineAutomatic r2 es'4(\p c''4~ | c''2\> bes'2) | R1\! | r2. es4(\mp |
}
transHnTwo = {
  es'8->\ff r8 r4 r2 | R1*7 | r2. es4(\ff | c'4 bes2.)\> |
  % c189: 44 E-flat4 (was G4 held from 43): G is the leading tone of V4/2 of A-flat and the cellos already carry it (G3 -> A-flat3 at 45); the horn's G4 stopped
  % unresolved at 45 (Aldwell & Schachter PDF 419: the leading tone of V is not doubled; E-flat is common to V and to the A-flat chord at 45)
  g'1\p( | es'1\>) | R1\! | R1 |
}
transHnThree = {
  R1*4 | des'1\p\< | c'1 | d'1 \breathe | % c356: Hn 3-4 breathe at the end of 39 (were unbroken 37-42, about 11 s p to ff into the four-horn call; Adler adler1 PDF 292, Ex. IX-9 PDF 290)
  d'1\f\< | bes2.\ff es4( | c'4 bes2.)\> | des'4\p r4 r2 |
  R1*3 |
}
transHnFour = {
  % c124: Hn 4 F3 at 39-40 (was A-flat3 with Bsn 1): horns take the concords, the bassoon the seventh (crossing, Rimsky-Korsakov PDF 108); the fifth F is no longer missing at 39
  R1*4 | ges1\p\< | aes1 | f1 \breathe |
  d'1\f\< | % c234: 40 D4 with Hn 3 (was F3, at pitch with Tbn 2): in mixed brass the horns go in pairs, so the leading tone is not one horn against three trombones (Rimsky-Korsakov PDF 102)
  g2.\ff es4( | c'4 bes2.)\> | g4\p r4 r2 |
  R1*3 |
}
% c253: 40 Tbn 1·2 and B.tbn enter p< (was f<) under the strings' f and swell into the sf at 41: a second group added to a crescendo enters p and crescendos faster (Rimsky-Korsakov PDF 127, 130); brass re-entering after rests at p/f is weaker than a marked change (PDF 136)
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
  % c284: 33 E-flat4 (was G4): the seventh F4 of 32 falls to E-flat4 as in Hn 2, and the brass chord has its third outside one horn; the same layout as 143 (Adler adler2 PDF 15, Ex. XI-1)
  es'8->\ff r8 r4 r2 | R1*7 | g'8->\sf r8 r4 r2 | R1 |
  R1 | R1*3 |
}
transTptThree = {
  R1*8 | es'8->\sf r8 r4 r2 | R1 | R1 |
  R1*3 |
}
transTbnOne = {
  c'8->\ff r8 r4 r2 | R1*6 | bes1\p\< | bes8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transTbnTwo = {
  g8->\ff r8 r4 r2 | R1*6 | f1\p\< | g8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transBassTbn = {
  c8->\ff r8 r4 r2 | R1*6 | bes,1\p\< | es8->\sf r8 r4 r2 |
  R1 | R1 | R1*3 |
}
transTuba = {
  c,8->\ff r8 r4 r2 | R1*7 | es,8->\sf r8 r4 r2 | R1 |
  R1 | R1*3 |
}
% c176: the B-flat2 at 40 is taken on the A-flat drum (28"/29", F2-C3), not on the C drum lowered to the bottom of its range (25"/26", B-flat2-F3);
% the A-flat drum is free 34-68 (Adler App. A, adler2 PDF 307; ch. 12, PDF 79, 81). The C drum now stays at C all movement.
transTimp = {
  c8->\ff r8 r4 r2 | R1^\markup \small "muta A♭ in B♭" | R1*5 | bes,1:32\pp\< |
  es1:32\ff\>~ | es1:32\mf\>~ | es1:32\pp | R1^\markup \small "muta B♭ in A♭" |
  R1*2 |
}
% c135: no 8va at 40-43 (top note G6, four ledger lines; Gould PDF 47: strings up to five ledger lines; keep the run's contour visible)
transVlnOne = {
  c'''8->\downbow\ff r8 r4 r2 | R1 | r8 f'8\downbow\mf( des''4.->) c''8( ces''8 bes'8 | bes'4--) a'8\upbow( bes'8) g'4.-> f'8 |
  r8 bes'8\downbow\<( ges''4.->) f''8( fes''8 es''8) | r8 g''8( aes''4.->) g''8( ges''8 f''8) | d''8( es''8 f''8 bes''8) d'''2-> | f''8( g''8 aes''8 c'''8) bes''16( c''' d''' es''' f''' es''' f''' fis''') |
  g'''1\sf\downbow\>~ | g'''2\mf f'''2\> | es'''4\p r4 r2 | R1*3 |
}
% c139: double stop, not triple, after the slurred sixteenth run at the end of 32 (Rimsky-Korsakov PDF 130: string anacrusis runs should not lead up to chords of three or four notes); G3 stays in Vla and Vc
transVlnTwo = {
  <es' c''>8->\downbow\ff r8 r4 r2 | R1*3 | r4 bes'2.:32\p\< | aes'1:32 | % c294: 37 tremolo from beat 2 (was B-flat4 from beat 1, the pitch of Vln I's pickup B-flat4 on 1-and; Adler adler1 PDF 135)
 
  aes'1:32 | aes'1:32\f | g''1\sf\downbow\>~ | g''2\mf f''2\> |
  % c222: 46 beat 4 G4 (was D-flat4, in unison with the viola's seventh, then a leap D-flat4-A-flat4 into an octave with the bass E-flat-A-flat at 47):
  % beat 4 regains its third, only the viola's seventh goes on to C, and the top voice steps G-A-flat into the second theme (Aldwell & Schachter PDF 76;
  % PDF 87-88, Ex. 5-29a/b; PDF 82: a leap within the dominant seventh, D-flat-G, is acceptable)
  des'1\pp | es'1 | es'1 | des'2. g'4 |
}
% c142: 35 Vla tail D-flat4 on beat 3, D4 on beat 4 (was D4 half note from beat 3): the Vln I head F-D-flat is a real transposition of the Vla's C-A-flat at 34, so its
% D-flat5 sounded against the Vla's D-natural4; now B-flat minor holds under the D-flat and B-flat7 (C-flat passing ninth) follows on beat 4 (Aldwell & Schachter PDF 265)
transVla = {
  % c151: entry at 34 mp (was mf): it starts on the C4 the bassoon solo is holding and rises through its register; Adler adler1 PDF 226: an accompanied bassoon is swallowed, so mark the others softer
  <c g es'>8->\downbow\ff r8 r4 r2 | r8 c'8\downbow\mp( aes'4.->) g'8( ges'8 f'8 | f'4--) e'8( f'8) des'4 d'4 | es'1 |
  ges'2:32\p\< r8 bes8( ges'4->~ | ges'8) f'8( fes'8 es'8) r8 c'8( aes'4->~ | aes'8) g'16( ges'16 f'4) f'2:32 | <d' f'>1:32\f |
  % c371: 44 rest on beats 1-2, B-flat3 again on beat 3 (was restruck on the downbeat): Hn 1's held C5 over the D-flat bass is a 7-6 suspension
  % resolving to B-flat4 on beat 3; the violas sounded that tone of resolution from the downbeat, a ninth below (Aldwell & Schachter PDF 352, Ex. 21-12c "poor").
  % Now the B-flat arrives in both parts together, and 44-45 is a clean 7-6 series over D-flat-C (PDF 356, Ex. 21-16; c281 fixed the second link at 45)
  <es' g'>1:32\sf\> | <es' g'>1:32\mf\> | bes1\pp | r2 bes2 |
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
  % c281: 45 G3 held to beat 3 (was A-flat3 from the downbeat): Cl 1's B-flat4 at 45.1 is a 7-6 suspension over the C bass (prepared by Hn 1's B-flat4 at 44.3);
  % with the cellos already on A-flat3 its tone of resolution sounded before the resolution, A&S Ex. 21-12c "poor" (PDF 352). The cello now moves 5-6 (G-A-flat)
  % as the clarinet resolves 7-6 (B-flat-A-flat), A&S PDF 351-352 Ex. 21-9c/21-16a, so the I6 of A-flat arrives on beat 3 with the resolution.
  % c338: 45 G3-A-flat3 under one bow, so the pickup E-flat3 at 46.4 is again an up-bow (A-flat3 46.1 up, G3 46.3 down): c281's split of 45 into two bows
  % had turned the S pickup and every bow of 46.4-55 round (pickup down, crescendo 47 down, diminuendo 52 up), unlike the recapitulation at 146.4 (Adler adler1 PDF 38: anacrusis up-bow, crescendo up-bow)
  g2( aes2) | aes2 g4 \clef tenor es4(\mf | % c115: clef before the pickup, between phrases (Gould PDF 22)
}
transCb = {
  c,1\fp | aes,,1 | bes,,1 | es,1 |
  es,1\< | f,1 | bes,,1 | bes,,1\f |
  es,1\sf\>~^\markup \small \italic "change bow at will" | es,1\mf\>~ | es,1\pp | des,1 |
  c,1 | des,2 es,2\upbow |
}

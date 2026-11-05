% c250 (manager): "arco" at bar 1 in cellos and basses, since the scherzo ends pizzicato (scherzo v261 request; Adler part 1 PDF 54).
% INTRODUCTION, bars 1-10 (Allegro con fuoco). After movement III (the scherzo, E major at its end) and a pause.
% c026 (rework for four movements): the scherzo ends ppp on G sharp alone (Hn 1 G#4, Vln I G#5) after a harp E-major chord and a pizzicato E.
% The finale takes that G sharp as A flat, in the same players at the same pitch (Hn 1 A flat 4, Vln I A flat 5), now ff, as the root of the
% German sixth A flat - C - E flat - F sharp; the scherzo's other chord tones move by step: E -> E flat (the scherzo's cellos end on pizz. E2 at its bar 375; finale Vc E flat 3) and B -> C.
% Direct ff start, no quiet held A flat first: the scherzo has already held the G sharp pp for 17 bars (360-376); after a pause a second quiet
% A flat would repeat that ending, and Beethoven 5's quiet pedal works only because its scherzo runs attacca into the finale (cyclic rule: no soft opening).
% 1-2 and 5-6: German sixth -> V, tutti without trumpets (their first melody is the second theme at 51).
% 3-4: the strings' answer, a turn figure on V (the finale's own motive, reused in the transition and development).
% 7-10: dominant preparation; the low strings anticipate the first theme's rhythm on V; crescendo into A.
% c053 (form): 7-10 start mf, not p. After the ff of 1-6 a p bar left only two bassoons, cellos and a timpani G sounding, so the movement started a second
% time, softly, four bars before the theme (the cyclic rule is 'no soft opening'); Dvorak 9/iv 1-10 never drops below f before its theme (ff, ffz, f, cresc. to ff at 10).
% mf keeps the level of the direct start and still leaves the crescendo of 9-10 room to reach the theme's f at 11.

% c058 (expression; Sebesky ch. 1, PDF 18 Ex. 2A, and ch. 6, PDF 205 Ex. 269: each hairpin ends on a printed level): 10 the crescendo of 9-10 lands on f on the accented quarter in every part (only the timpani had it).
% c058 (Sebesky PDF 214-215, Ex. 281: one figure, one articulation; Adler PDF 39, c018): 3-4 the strings' scale figure four notes per bow and the accented G separate, as at 87-90.
% c075 (MOLA Example 3, PDF 10: every entry after rests carries its dynamic; Example 6, PDF 11: every staff of a tutti marks it): bar 5 restates ff in the winds, brass, timpani and basses, as the violins, violas and cellos already do (the strings drop to f at 3-4)
% c188 (Adler ch. 10, PDF 309, 321): 9-10 the held dominant in Fl 2, Ob 2, clarinets, horns and violas is tied into 10 (as Bn 2, Cbsn and basses already were), so the crescendo is not broken by an attack on 10.1.
% c315 (MOLA PDF 8 and Example 7, PDF 12: extracted parts must be proofread; marks placed in the score do not survive extraction): in the Flute 1, Flute 2 and Oboe 2 parts
% the crescendo of bar 10 (mf < f inside the bar, after the rest 7-9) was too short to draw ("crescendo too small"), so the part printed "mf f" with no hairpin.
% Parts only (tag 'part): that hairpin gets a minimum length and widens its bar, as global.ily does for the score at 219-222.
introFluteOne = { c'''1->\ff | b''4-> r4 r2 | R1*2 | c'''1->\ff | b''4-> r4 r2 | R1*3 | \tag #'part { \once \override Staff.Hairpin.minimum-length = #6 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods } f'''2\mf\< d'''4->\f r4 | }
introFluteTwo = { fis''1->\ff | g''4-> r4 r2 | R1*2 | fis''1->\ff | g''4-> r4 r2 | R1*3 | \tag #'part { \once \override Staff.Hairpin.minimum-length = #6 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods } b''2\mf\< b''4->\f r4 | }
introOboeOne = { es''1->\ff | d''4-> r4 r2 | R1*2 | es''1->\ff | d''4-> r4 r2 | R1*3 | \tag #'part { \once \override Staff.Hairpin.minimum-length = #6 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods } aes''2\mf\< f''4->\f r4 | }
introOboeTwo = { c''1->\ff | b'4-> r4 r2 | R1*2 | c''1->\ff | b'4-> r4 r2 | R1*3 | \tag #'part { \once \override Staff.Hairpin.minimum-length = #6 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods } d''2\mf\< d''4->\f r4 | }
introCorAnglais = { fis'1->\ff | g'4-> r4 r2 | R1*2 | fis'1->\ff | g'4-> r4 r2 | R1*4 | }
introClOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1->\ff | g'4-> r4 r2 | R1*2 | r2 b'2~\mf\< | b'2 b'4->\f r4 | }
introClTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1->\ff | d'4-> r4 r2 | R1*2 | r2 g'2~\mf\< | g'2 g'4->\f r4 | }
introBassCl = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 | R1*4 | }
introBsnOne = { c1->\ff | b,4-> r4 r2 | R1*2 | c1->\ff | b,4-> r4 r2 |
  d2\mf( g,4. aes,8 | b,4 c8 d8 es4 f4) | g4\<( aes4 b4 c'4 | d'4 es'4 f'4->\f d'4->) | }
% c054 (orchestration; Adler ch. 8, PDF 224-225, 229, 249-250): 7-8 Bn 2 holds the dominant pedal G2 into 9-10 instead of doubling Bn 1 and the cellos at the unison.
introBsnTwo = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 |
  g,1\mf~ | g,1~ | g,1\<~ | g,2 g,4->\f r4 | }
introCbsn = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1->\ff | g,,4-> r4 r2 | R1*2 | g,,1\p\<~ | g,,2 g,,4->\f r4 | }
% c439 (Rimsky-Korsakov ch. IV, PDF 127 'Amplification': while the first group makes the crescendo gradually, the second group enters piano or pianissimo and reaches its crescendo more rapidly; Ex. 245, 248, PDF 411, 413): at 9 the horns, contrabassoon and basses enter p < (were mf <) under the bassoons, violas and cellos, which are at mf and begin their crescendo there; all still reach f at 10.3. The clarinets (9.3) and flutes and oboes (10.1) keep mf, which by then is already below the level of the crescendo. Notes unchanged.
introHnOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1->\ff | g'4-> r4 r2 | R1*2 | g'1~\p\< | g'2 g'4->\f r4 | }
introHnTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1->\ff | d'4-> r4 r2 | R1*2 | d'1~\p\< | d'2 d'4->\f r4 | }
introHnThree = { c'1->\ff | b4-> r4 r2 | R1*2 | c'1->\ff | b4-> r4 r2 | R1*2 | b1~\p\< | b2 b4->\f r4 | }
introHnFour = { fis1->\ff | g4-> r4 r2 | R1*2 | fis1->\ff | g4-> r4 r2 | R1*2 | g1~\p\< | g2 g4->\f r4 | }
% c424 (orchestration; Adler ch. 11, adler2 PDF 15: above mf two horns equal one trumpet or trombone, so a single horn at ff is half weight; PDF 14: the brass easily overshadow the rest;
%   PDF 17: the trombones are more versatile than horns and trumpets): bars 1 and 5, the German sixth's F sharp, the one tone that turns the A flat triad into the augmented sixth,
%   was in the brass only Hn 4's F sharp3 (half a unit against about seven units of A flat, C and E flat); Tbn 1 now plays F sharp3 with Hn 4 and rises a step to G3 (it had E flat3 and leapt to G3).
%   E flat stays in Hn 2, Ob 1, Cl 2, Vln II, Vla, Vc. Link pitches (Hn 1 A flat4, Hn 2 E flat4, Vc E flat3), bar 2 and the chord's spelling unchanged.
introTbnOne = { fis1->\ff | g4-> r4 r2 | R1*2 | fis1->\ff | g4-> r4 r2 | R1*4 | }
introTbnTwo = { c1->\ff | b,4-> r4 r2 | R1*2 | c1->\ff | b,4-> r4 r2 | R1*4 | }
introBassTbn = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 | R1*4 | }
introTuba = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1->\ff | g,,4-> r4 r2 | R1*4 | }
% Timpani: the scherzo ends tuned E, G, B, E (E2, G2, B2, E3). In the pause each drum moves within its range: 32" E2 -> G2, 29" G2 -> A flat 2,
% 26" B2 -> C3, 23" E3 -> E flat 3 (no drum moves more than a minor third). Adler PDF 112: give the setting at the start.
% c146 (Adler ch. 12, PDF 80: timpani mallets come hard, medium and soft and the composer names them; PDF 61 note: give time to change): "hard sticks" at 1 (the scherzo ends with "soft sticks", its last instruction to the player; its own bar-1 label also names the sticks), "medium sticks" in the rest at 215 for the soft rolls 219-246, "hard sticks" in the rest at 255 for the last cadence. Movement I names its sticks the same way.
% c230 (cyclic; Casanelles ch. 5, PDF 200, 211-212, 227-228, 239, 243): 9 the timpani play the scherzo's motive x on the dominant G (crotchet, two quavers, crotchet), the figure the
% scherzo's timpani end with (pp, pp, then ppp near the rim: B-B-B-E at its 363, 367, 371), now under the crescendo into F1; strokes per bar 1, 1, 4, 5 at 7-10, so the build tightens in its last bars.
% Same form and pitch as the retransition's quotation at 143-145, which this bar now prepares (both dominant preparations lead to F1).
% c235 (Adler part 2 PDF 292: "Timpani - the number of drums should be given at the beginning of the score"; Example XVIII-1, PDF 293, "6 Timpani"): the label names four drums.
% c307 (texture; Adler ch. 5, PDF 139-140 Ex. V-17, Hindemith: a powerful string unison builds tension and prepares the tutti chords that follow; PDF 141 Ex. V-19, Shostakovich 6:
%   when the line reaches the violins' low register the cellos double it an octave below, which gives the passage its resolution): 3-4 the cellos join the strings'
%   answer an octave below the violas (G3 down to B2, ending G2), so the scale figure is a three-octave string unison over a real bass instead of a
%   bass-less two-octave line between the ff tuttis; f as the upper strings; basses still enter at 9 (c279), 7-8 keep the cellos' line with Bn 1.
% c294 (orchestration; Rimsky-Korsakov, appendix of single tutti chords, PDF 505-507: every held f/ff tutti chord there has a timpani roll on a chord tone (chords 1-4, 6, 9-12, 16-20);
%   ch. IV, PDF 118, and Ex. 205/206, PDF 368-369: a tutti that returns is varied by "alteration of details"): 5 the restated German sixth has an A flat roll ff through the bar
%   (was one quarter stroke, as at 1). Bar 1 keeps its single A flat stroke, the scherzo's G sharp taken up as A flat and its single closing strokes; the repeat at 5 now differs from 1
%   only in the drum, so the held chord sounds as a held tutti, not as an attack that decays. No pitch, voicing, link or dynamic of any other part changed.
introTimp = { aes,4->\ff^\markup \column { \italic "4 timpani: G, A♭, C, E♭" \italic "(retune in the pause: low E → G, G → A♭, B → C, high E → E♭)" \italic "hard sticks" } r4 r2 | g,4-> r4 r2 | R1*2 |
  aes,1:32->\ff | g,4-> r4 r2 | g,4\mf r4 r2 | g,4 r4 r2 | g,4\< g,8 g,8 g,4 r4 | g,8 g,8 g,8 g,8 g,4->\f r4 | }
% c218 (expression; Adler ch. 2, PDF 38: a crescendo is natural on an up-bow, toward the frog, and a diminuendo on a down-bow; the composer marks bow direction only to counteract the players' habit, here the down-bow on a downbeat after rests): 9 violas and basses start the held D4/G1 crescendo (mf to the f accent on 10.3) up-bow, so the accent on 10.3 is a down-bow, as at 135 (c018 \upbow under the pp crescendo).
% c366 (playability; Adler ch. 2, adler1 PDF 30: double notes "are usually divided between the two players on the same stand"; unmarked, a player may divide or not;
%   "Some composers wish to have each player perform double-stops. In that case, it is safer to write non div."): 1 Vln I, Vln II and cellos "non div.", so every first violin
%   holds the scherzo's G sharp5 as A flat5 (the link is in the same players at the same pitch) and the cellos' A flat2-E flat3 fifth is not halved; the violas keep "div.". It holds for 5. Text only.
introVlnOne = { <c'' aes''>1->\ff\dnup^\markup \italic "non div." | <b' g''>4->\downbow r4 r2 |
  r4 g''8(\f f''8 es''8 d''8) c''8( b'8 | c''8 d''8 es''8 f''8) g''4-> g'4-> |
  <c'' aes''>1->\ff\dnup | <b' g''>4->\downbow r4 r2 | R1*2 | r4 g'8(\mf\< aes'8 b'8 c''8 d''8 es''8) | f''8( g''8 aes''8 b''8) d'''4->\f\downbow r4 | }
introVlnTwo = { <es' c''>1->\ff\dnup^\markup \italic "non div." | <g d' b'>4->\downbow r4 r2 |
  r4 g'8(\f f'8 es'8 d'8) c'8( b8 | c'8 d'8 es'8 f'8) g'4-> g4-> |
  <es' c''>1->\ff\dnup | <g d' b'>4->\downbow r4 r2 | R1*2 | r4 g8(\mf\< aes8 b8 c'8 d'8 es'8) | f'8( g'8 aes'8 b'8) d''4->\f\downbow r4 | }
% c437 (texture; Adler ch. 16, adler2 PDF 213 and Ex. XVI-10 mm. 25-32 (PDF 211): Dvorak's late oboe entry 'makes the last four measures sound truly polyphonic'; PDF 230-231: a counter-voice built from the bar's own pitches): 8 the violas answer the cellos' F1-rhythm on V one bar later, a fourth higher and two octaves up (G4-D4-E flat4, as D3-G2-A flat2 at 7), the E flat4 a 6-5 into their held D4 at 9; they entered at 9 before.
% c466 (playability; Adler ch. 3, adler1 PDF 73-74: an open string is not under the oscillating finger's control and stands out in a held expressive note; PDF 87: the viola's G and D strings 'can also be exploited for their dark quality'; PDF 76: mark sul G for one string):
%   8-10.3 the violas' answer G4-D4-E flat4 and the held D4 crescendo are 'sul G' (4th position), so the D4 grows with vibrato on a stopped string instead of the open D, in the cellos' dark colour. Notes and MIDI unchanged.
introVla = { <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 |
  r4 g'8(\f^\markup \italic "unis." f'8 es'8 d'8) c'8( b8 | c'8 d'8 es'8 f'8) g'4-> g4-> |
  <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 | R1 | \once \override TextSpanner.bound-details.left.text = \markup \italic "sul G" g'2(\mf\downbow^\markup \italic "unis."\startTextSpan d'4. es'8) | d'1~\<\upbow | d'2 d'4->\f\stopTextSpan r4 | }
introVc = { <aes, es>1->\ff\dnup^\markup \italic "arco, non div." | g,4->\downbow r4 r2 |
  r4 g8(\f f8 \stemDown es8 d8) c8( b,8 \stemNeutral | c8 d8 es8 f8) g4-> g,4-> | <aes, es>1->\ff\dnup | g,4->\downbow r4 r2 |
  d2\mf( g,4. aes,8) | b,4( c8 d8 es4 f4) | g4\<( aes4 b4 c'4) | d'4( es'4) f'4->\f\downbow d'4->\upbow | }
introCb = { aes,,1->\ff\dnup^\markup \italic "arco" | g,,4->\downbow r4 r2 | R1*2 | aes,,1->\ff\dnup | g,,4->\downbow r4 r2 | R1*2 | g,,1\p\<\upbow~ | g,,2 g,,4->\f r4 | }
% c279 (holistic, Eroica; Adler ch. 16, adler2 PDF 205: Brahms "the entire harmony is not sounded until the first offbeat ... so as not to thicken the downbeat suddenly";
%   PDF 213 and 215 (Bizet, Jeux d'enfants 13-18): the crescendo is orchestrated by successive entries "instead of being left to the players or conductor"; PDF 224 (Ravel)):
%   9-10 the winds no longer enter all together mf on 9.1. Horns, violas, contrabassoon and basses (the held V chord) enter on 9.1 as before; clarinets join on 9.3;
%   oboes and flutes join on 10.1 with the V7(b9) top (Ob 1 A flat5, Fl 1 F6), so the chord grows from V to V7(b9) as the dominant preparation swells. The held parts keep
%   c189's ties (no re-attack on 10.1); the new attacks are new instruments. Timpani motive x at 9 and the f accents on 10.3 unchanged.

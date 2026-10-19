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
introFluteOne = { c'''1->\ff | b''4-> r4 r2 | R1*2 | c'''1->\ff | b''4-> r4 r2 | R1*2 | d'''1\mf\< | f'''2 d'''4->\f r4 | }
introFluteTwo = { fis''1->\ff | g''4-> r4 r2 | R1*2 | fis''1->\ff | g''4-> r4 r2 | R1*2 | b''1~\mf\< | b''2 b''4->\f r4 | }
introOboeOne = { es''1->\ff | d''4-> r4 r2 | R1*2 | es''1->\ff | d''4-> r4 r2 | R1*2 | f''1\mf\< | aes''2 f''4->\f r4 | }
introOboeTwo = { c''1->\ff | b'4-> r4 r2 | R1*2 | c''1->\ff | b'4-> r4 r2 | R1*2 | d''1~\mf\< | d''2 d''4->\f r4 | }
introCorAnglais = { fis'1->\ff | g'4-> r4 r2 | R1*2 | fis'1->\ff | g'4-> r4 r2 | R1*4 | }
introClOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1->\ff | g'4-> r4 r2 | R1*2 | b'1~\mf\< | b'2 b'4->\f r4 | }
introClTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1->\ff | d'4-> r4 r2 | R1*2 | g'1~\mf\< | g'2 g'4->\f r4 | }
introBassCl = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 | R1*4 | }
introBsnOne = { c1->\ff | b,4-> r4 r2 | R1*2 | c1->\ff | b,4-> r4 r2 |
  d2\mf( g,4. aes,8 | b,4 c8 d8 es4 f4) | g4\<( aes4 b4 c'4 | d'4 es'4 f'4->\f d'4->) | }
% c054 (orchestration; Adler ch. 8, PDF 224-225, 229, 249-250): 7-8 Bn 2 holds the dominant pedal G2 into 9-10 instead of doubling Bn 1 and the cellos at the unison.
introBsnTwo = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 |
  g,1\mf~ | g,1~ | g,1\<~ | g,2 g,4->\f r4 | }
introCbsn = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1->\ff | g,,4-> r4 r2 | R1*2 | g,,1\mf\<~ | g,,2 g,,4->\f r4 | }
introHnOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1->\ff | g'4-> r4 r2 | R1*2 | g'1~\mf\< | g'2 g'4->\f r4 | }
introHnTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1->\ff | d'4-> r4 r2 | R1*2 | d'1~\mf\< | d'2 d'4->\f r4 | }
introHnThree = { c'1->\ff | b4-> r4 r2 | R1*2 | c'1->\ff | b4-> r4 r2 | R1*2 | b1~\mf\< | b2 b4->\f r4 | }
introHnFour = { fis1->\ff | g4-> r4 r2 | R1*2 | fis1->\ff | g4-> r4 r2 | R1*2 | g1~\mf\< | g2 g4->\f r4 | }
introTbnOne = { es1->\ff | g4-> r4 r2 | R1*2 | es1->\ff | g4-> r4 r2 | R1*4 | }
introTbnTwo = { c1->\ff | b,4-> r4 r2 | R1*2 | c1->\ff | b,4-> r4 r2 | R1*4 | }
introBassTbn = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1->\ff | g,4-> r4 r2 | R1*4 | }
introTuba = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1->\ff | g,,4-> r4 r2 | R1*4 | }
% Timpani: the scherzo ends tuned E, G, B, E (E2, G2, B2, E3). In the pause each drum moves within its range: 32" E2 -> G2, 29" G2 -> A flat 2,
% 26" B2 -> C3, 23" E3 -> E flat 3 (no drum moves more than a minor third). Adler PDF 112: give the setting at the start.
% c146 (Adler ch. 12, PDF 80: timpani mallets come hard, medium and soft and the composer names them; PDF 61 note: give time to change): "hard sticks" at 1 (the scherzo ends with "soft sticks", its last instruction to the player; its own bar-1 label also names the sticks), "medium sticks" in the rest at 215 for the soft rolls 219-246, "hard sticks" in the rest at 255 for the last cadence. Movement I names its sticks the same way.
introTimp = { aes,4->\ff^\markup \column { \italic "Timpani: G, A♭, C, E♭" \italic "(retune in the pause: low E → G, G → A♭, B → C, high E → E♭)" \italic "hard sticks" } r4 r2 | g,4-> r4 r2 | R1*2 |
  aes,4->\ff r4 r2 | g,4-> r4 r2 | g,4\mf r4 r2 | g,4 r4 r2 | g,4\< r4 g,4 r4 | g,8 g,8 g,8 g,8 g,4->\f r4 | }
% c218 (expression; Adler ch. 2, PDF 38: a crescendo is natural on an up-bow, toward the frog, and a diminuendo on a down-bow; the composer marks bow direction only to counteract the players' habit, here the down-bow on a downbeat after rests): 9 violas and basses start the held D4/G1 crescendo (mf to the f accent on 10.3) up-bow, so the accent on 10.3 is a down-bow, as at 135 (c018 \upbow under the pp crescendo).
introVlnOne = { <c'' aes''>1->\ff\dnup | <b' g''>4->\downbow r4 r2 |
  r4 g''8(\f f''8 es''8 d''8) c''8( b'8 | c''8 d''8 es''8 f''8) g''4-> g'4-> |
  <c'' aes''>1->\ff\dnup | <b' g''>4->\downbow r4 r2 | R1*2 | r4 g'8(\mf\< aes'8 b'8 c''8 d''8 es''8) | f''8( g''8 aes''8 b''8) d'''4->\f\downbow r4 | }
introVlnTwo = { <es' c''>1->\ff\dnup | <g d' b'>4->\downbow r4 r2 |
  r4 g'8(\f f'8 es'8 d'8) c'8( b8 | c'8 d'8 es'8 f'8) g'4-> g4-> |
  <es' c''>1->\ff\dnup | <g d' b'>4->\downbow r4 r2 | R1*2 | r4 g8(\mf\< aes8 b8 c'8 d'8 es'8) | f'8( g'8 aes'8 b'8) d''4->\f\downbow r4 | }
introVla = { <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 |
  r4 g'8(\f^\markup \italic "unis." f'8 es'8 d'8) c'8( b8 | c'8 d'8 es'8 f'8) g'4-> g4-> |
  <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 | R1*2 | d'1~\mf\<\upbow^\markup \italic "unis." | d'2 d'4->\f r4 | }
introVc = { <aes, es>1->\ff\dnup | g,4->\downbow r4 r2 | R1*2 | <aes, es>1->\ff\dnup | g,4->\downbow r4 r2 |
  d2\mf( g,4. aes,8) | b,4( c8 d8 es4 f4) | g4\<( aes4 b4 c'4) | d'4( es'4) f'4->\f\downbow d'4->\upbow | }
introCb = { aes,,1->\ff\dnup | g,,4->\downbow r4 r2 | R1*2 | aes,,1->\ff\dnup | g,,4->\downbow r4 r2 | R1*2 | g,,1\mf\<\upbow~ | g,,2 g,,4->\f r4 | }

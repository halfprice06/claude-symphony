\version "2.24.0"
% CODA, bars 211-222 (c013: 211-214 augmented to 211-218; old 215-218 are now 219-222, every later bar +4). 211-218: the D flat episode, ff, in the trumpets: theme B's single recall from movement II, its second half,
% ending on D flat (mvt2 c100 sketch; cyclic-notes: give the forte D flat to the trumpets, not movement II's bar 61 tutti). D flat over F
% at 213-214 is the Neapolitan sixth of C. 215: German sixth of C spelled with D sharp in the violas; 216: cadential 6/4, the violas' D sharp
% rises to E natural (cyclic-notes 'Owed' item 9: the E flat/E natural thread closed in the violas with an augmented sixth); 217: V7;
% c013: theme B augmented (note values doubled, 8 bars, about 13 s at 2 = 72 against movement II's 16 s; was 6.7 s), so it is heard as the theme
% and not as a fast figure. Harmony per old half bar now per bar: D flat (211-212, re-struck f at 212), G flat maj7 (213: the F of trumpet 2 is the
% chord's 7th and falls to E flat in 214; no G flat above it), A flat 7 (214), F minor 7 (215), D flat over F (216-218, the scale in 215-216).
% 218 (c002): movement I's stop chord B-D-F-A flat itself, D in the bass (vii°6/5 over the timpani's G), so the arrival is not a root-position V-I (cadence plan: the first is 262-263 since v14; c070: these are v01 numbers, 218 = now 222, 219 = now 223). Top voice D flat - C - B (- C at 219).

% c028: 211-218 theme B phrased in two halves with a breath after 214, as movement II phrases it (mvt II bSec, breath between the halves);
% the upper woodwinds that double the trumpets (Fl 1-2, Ob 1, Cl 1, and Ob 2/Cl 2 on their shared staves) stay ff with them instead of dropping to f (Adler II PDF 188-189: doubling at pitch strengthens the tune)
% c042 (harmony; A&S PDF 380, 393, 388): 222 the Fl 1/Vln I run into C7 is G-A flat-B (was G-A natural-B against the held A flat of the stop chord: an augmented octave, and flat 6 replaced by natural 6 before it reaches 5).
% The augmented second A flat-B is an arpeggiation inside the diminished seventh (A&S PDF 380).
% c105 (MOLA PDF 5: parts are read by one player; Gould PDF 66-67 is the score-only reason): the tied minims of c035 (211 Ob 2, Cl 2; 215 Hn 3, Hn 4) show a
% crossing or unison on the shared staves only; in the single-player parts they were printed as minim~minim where a semibreve fills the bar. Parts now read a semibreve (tag 'part).
% c108 (expression; Rimsky-Korsakov PDF 129: an echo is weaker than the first statement but akin to it; PDF 133: between brass and brass the harmonic basis must be of inferior dynamic power): 217-218 Hn 1-2 a2 on the echo (Hn 2 left its held D flat 4, which Hn 1 met at the unison), and the held F/A flat chord in Tpt 3, Hn 3-4, Tbn 1-2, B.tbn, tuba, bassoons and contrabassoon diminishes f > mp, so the echo is heard; these parts enter 219 at p (not sub. p).
% c108 (Rimsky-Korsakov PDF 130: a prolonged crescendo adds strings, then wood-wind, then brass; the brass make the final crescendo into the climax): 220-222 the brass hold p through 220, crescendo from 221 and reach mf at 222 (strings, wood-wind and timpani keep p < mp < f < fff); sub. p 219 and fff 223 unchanged.
codaTwoTptOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~\> | des''1~\f | des''1) \breathe | c''1\subP | c''1 | b'1\< | b'1\mf\< | }
codaTwoTptTwo = { f'2->(\ff aes'2 | des''2. es''4 | f''2 ges''4 f''4 | es''2. des''4) \breathe | c''2.( des''4 | aes'1~\> | aes'1~\f | aes'1) \breathe | fis'1\subP | g'1 | f'1\< | aes'1\mf\< | }
% c090 (cyclic lens; Adler ch. 17, PDF 264 and 267 point 4: no instrument of a competing colour on the solo's pitch): 220 Tpt 3 holds C4 (was a leap C4-E4 onto the thread pitch E4
%   at sub. p, at the unison with the violas' and Hn 3's D sharp4-E4); E4 at 220 now comes only from D sharp.
% c104 (REJECTED by the composer: Tpt 3 stays B3 at 221 so the 6/4 fourth resolves down, cycle 102) (Rimsky-Korsakov PDF 100: close order without gaps; PDF 114: balance matters most in sustained chords): 221 Tpt 3 D4 (was B3, a third B3 with Hn 2 and Hn 4), so V7 has its fifth in the brass; D4 is held into the stop chord at 222.
codaTwoTptThree = { des'1\ff\> | des'1\f | ges'1 | es'1 \breathe | aes'1 | f'1 | f'1~\> | f'1\mp \breathe | c'1~\p | c'1 | b1\< | d'1\mf\< | }
% c046 (Adler PDF 292, 303: periodic rests, after high playing): Hn 1-2 rest 211-214 (they played every bar 199-228, about 50 s, with written B flat 5 / G5 held at 207-210)
% c107 (texture; Adler ch. 5, PDF 135: the background moves under the melody's long notes; PDF 142-143: middleground in its own rhythm): 217-218 Hn 1 answers the trumpets' theme-B head (A flat-D flat-F-G flat, as at 211-212, one octave lower: movement II's own pitch, cor anglais 41) under the held D flat, and reaches its A flat4 of 219; the held D flat/F chord no longer stands still for two bars.
codaTwoHnOne = { R1*4 | aes'1\f | aes'1 | aes2(^\markup \italic "espress." des'2 | f'2. ges'4) \breathe | aes'1\subP | g'1 | g'1\< | f'1\mf\< | }
% c110 (cyclic lens; A&S Unit 32, PDF 589 and 591, Ex. 32-10a: a V7 reinterpreted as a German sixth moves the music down a half step, the held tone respelled; PDF 588: a true enharmonic is heard
%   whatever the notation; PDF 597-598 and 600-602: an enharmonic pitch link carried in one voice integrates a remote area and enlarges a motive): 219-221 Hn 2 holds the echo's G flat 4
%   as F sharp 4 (the German sixth's sharp 4) and rises to G4 (was a leap G flat 4 -> C4). Hn 2 held the same G flat 4 as the 7th of A flat 7 (V7 of D flat) at 209-210; the D flat episode is
%   now framed by that chord and its German-sixth respelling in the same player. Hn 1 still continues the theme to A flat 4; both horns close on G4 at 220. 221 Hn 2 D4, the V7's fifth (no D in the brass before).
% c110 (A&S PDF 585: rhythm, texture and dynamics shape how a change of key is heard; Rimsky-Korsakov PDF 129: an echo is softer than the statement): 216-217 the tune's held D flat (Tpt 1-2, Fl 1-2, Ob 1-2, Cl 1-2)
%   goes ff > f, so the horns' f echo of theme B at 217-218 is not under a ff unison; ff at 211 and sub. p at 219 unchanged.
% c138: 'espress.' also on Hn 2 at 217, because the part-combined a2 staff printed neither horn's 'espress.' (only Hn 1 carried it).
codaTwoHnTwo = { R1*4 | c'1\f | des'1 | aes2(^\markup \italic "espress." des'2 | f'2. ges'4) \breathe | fis'1\subP | g'1 | d'1\< | d'1\mf\< | }
% c035 (Gould PDF 65, 67): 215-218 Hn 3 (F3) lies below Hn 4 (A flat 3); 215 is written as tied minims so the stems show the crossing that a semibreve chord hid. Sound unchanged.
% c136 (playability; Adler ch. 9, PDF 292: frequent rests so the brass lips recover): Hn 3-4 rest 215-218 (Hn 3 was in unison with Tbn 1, Hn 4 with Bn 1); Hn 4 otherwise played 199-264 with one bar's rest (229), about 110 s. They re-enter p at 219, the German sixth.
codaTwoHnThree = { aes1\ff\> | aes1\f | des'1 | c'1 \breathe | R1*4 | dis'1\p | e'1 | f'1\< | d'1\mf\< | }
% c104 (Rimsky-Korsakov PDF 102-103: horns in pairs against single trombones and trumpets): 211-212 Hn 4 A flat 3 with Hn 3 (was F3, unison with Tbn 1); the fifth no longer rests on one horn.
codaTwoHnFour = { aes1\ff\> | aes1\f | ges1 | ges1 \breathe | R1*4 | c'1\p | c'1 | b1\< | b1\mf\< | }
codaTwoTbnOne = { f1\ff\> | f1\f | ges1 | es1 \breathe | f1 | f1 | f1~\> | f1\mp \breathe | fis1\p | g1 | g1\< | aes1\mf\< | }
codaTwoTbnTwo = { des1\ff\> | des1\f | des1 | c1 \breathe | aes,1 | aes,1 | aes,1~\> | aes,1\mp \breathe | c1\p | c1 | b,1\< | b,1\mf\< | }
codaTwoBassTbn = { des1\ff\> | des1\f | ges,1 | aes,1 \breathe | f,1 | f,1 | f,1~\> | f,1\mp \breathe | aes,1\p | g,1 | g,1\< | d1\mf\< | }
codaTwoTuba = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 \breathe | f,,1 | f,,1 | f,,1~\> | f,,1\mp \breathe | aes,,1\p | g,,1 | g,,1\< | d,1\mf\< | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
codaTwoTimp = { aes,4->\ff r4 r2 | aes,4\f r4 r2 | R1 | aes,4 r4 aes,4 r4 | R1^\markup \small \italic "medium sticks" | R1*3 | aes,1:32\subP | g,1:32\<~ | g,1:32\mp\<~ | g,1:32\f\< | }
% c036 (Adler PDF 186: above A6 the flute's notes are approached best by scale): 222 Fl 1 joins Vln I's run G6-A6-B6 into the C7 at 223 (was a leap B5-C7 at fff).
codaTwoFluteOne = { aes''2->(\ff des'''2 | f'''2. ges'''4 | aes'''2 bes'''4 aes'''4 | ges'''2. f'''4) \breathe | es'''2.( f'''4 | des'''1~\> | des'''1~\f | des'''1) \breathe | c'''1\subP | c'''1\< | b''1\mp\< | b''2\f\< r8 g'''8( aes''' b''') | }
codaTwoFluteTwo = { aes''2->(\ff des'''2 | f'''2. ges'''4 | aes'''2 bes'''4 aes'''4 | ges'''2. f'''4) \breathe | es'''2.( f'''4 | des'''1~\> | des'''1~\f | des'''1) \breathe | fis''1\subP | g''1\< | f''1\mp\< | f''1\f\< | }
% c021: 211-218 Fl 1-2 a2 double trumpet 1's theme B an octave above (Rimsky-Korsakov PDF 75: in the top register two flutes suffice to double a trumpet at the upper octave)
% c019: 211-218 Ob 1 and Cl 1 double trumpet 1's theme B at the unison (Rimsky-Korsakov PDF 74-75: a wood-wind added to a brass melody gives a finer legato; Ex. 78, 93-94)
% c080 (cyclic; A&S Unit 28, PDF 491-492 and 499 point 3: flat 2 tends to move down; PDF 496-497: a chromatic step is written as a minor 2nd, not on the same staff degree): 219 Ob 1 C5 (was D sharp 5).
%   Ob 1 doubles Tpt 1's theme B at the unison through 218; its D flat 5 now falls to C with Tpt 1 (D flat - C - B - C, protected top line) instead of rising to D sharp 5 on the same staff degree. The thread's D sharp stays in the violas and Hn 3 (D sharp 4).
codaTwoOboeOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~\> | des''1~\f | des''1) \breathe | c''1\subP | e''1\< | d''1\mp\< | d''1\f\< | }
% c010: 215 Ob 1 and Hn 3 spelled D sharp like the violas: E flat (Tpt 1, 213) becomes D sharp and rises to E (A&S PDF 588, 597-598).
% c035 (Gould PDF 65-67): 211 Ob 2 and Cl 2 as tied minims, so Ob 2's F5 above Ob 1's A flat is not read as one chord and Cl 2's unison A flat does not touch Cl 1's stem. Sound unchanged.
% c052 (harmony; A&S Unit 24, PDF 406-408): 214 Ob 2 resolves the 7th G flat to F with Ob 1 on beat 4 instead of holding it against the resolution.
codaTwoOboeTwo = { \tag #'score { f''2\ff~ f''2 } \tag #'part { f''1\ff } | f''1 | des''1 | ges''2. f''4 \breathe | es''1 | des''1\> | des''1~\f | des''1 \breathe | c''1\subP | e''1\< | d''1\mp\< | d''1\f\< | }
% c130 (Casanelles ch. 5, PDF 226-227 and 236: the instrument is part of a theme's meaning; Debussy's cor anglais with trumpet as a signifying blend): 217-220 the cor anglais, theme B's own instrument in movement II (41-44), joins Hn 1 on the answer at movement II's own pitch (A flat 3-D flat 4-F4-G flat 4), then A flat 4 (219) and G4 (220) with Hn 1. Its only notes after 186.
codaTwoCorAnglais = { R1*6 | aes2(\f^\markup \italic "espress." des'2 | f'2. ges'4) | aes'1\subP | g'2 r2 | R1*2 | }
codaTwoClOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~\> | des''1~\f | des''1) \breathe | aes'1\subP | g'1\< | g'1\mp\< | aes'1\f\< | }
% c060 (cyclic lens; A&S Unit 29, PDF 504: the augmented sixth's sharp 4 is a passing tone to 5; Sebesky ch. 1, PDF 13-14, focus): 220 Cl 2 and Vln I (lower) take F sharp up to G, so the only E4 arriving by step from outside is the violas' D sharp -> E (with Hn 3), the thread's own voice
codaTwoClTwo = { \tag #'score { aes'2\ff~ aes'2 } \tag #'part { aes'1\ff } | aes'1 | ges'1 | aes'1 \breathe | f'1 | f'1\> | f'1~\f | f'1 \breathe | fis'1\subP | g'1\< | f'1\mp\< | f'1\f\< | }
codaTwoBsnOne = { f1\ff\> | f1\f | bes1 | c'1 \breathe | aes1 | aes1 | aes1~\> | aes1\mp \breathe | c'1\p | c'1\< | b1\mp\< | b1\f\< | }
codaTwoBsnTwo = { des1\ff\> | des1\f | ges,1 | aes,1 \breathe | f,1 | f,1 | f,1~\> | f,1\mp \breathe | aes,1\p | g,1\< | g,1\mp\< | d,1\f\< | }
codaTwoCbsn = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 \breathe | f,,1 | f,,1 | f,,1~\> | f,,1\mp \breathe | aes,,1\p | g,,1\< | g,,1\mp\< | d,,1\f\< | }
% c051 (melody; Sebesky ch. 6, PDF 211-212, Ex. 279-280: a background line that shadows the tune too closely distorts the focus): 212 and 214 the violins no longer move a beat ahead of theme B
% (214 Vln I F5 against the tune's G flat 5, Vln II D flat 5 against E flat 5; 212 beat 4 A flat 5 against G flat 5); they now take the tune's own note on beat 4 (212 Vln I G flat; 214 Vln I and II dotted minim then F/D flat). Vln II keeps D flat at 212 (E flat there made fifths with Cl 2 into 213).
% c054 (orchestration; Adler ch. 8, PDF 249-250, 265-266): 212-214 Vln I doubles theme B an octave above Tpt 1 with the flutes (8'+4') instead of a shadow line that
% touched the tune at the unison on some beats and ran a third beside it on others (revises c051, keeps its aim: nothing moves against the tune).
% c118 (expression; Adler ch. 2, PDF 37-38: unslurred notes change bow on every note, the only string slurs are bow slurs): 212-214 Vln I-II slurred one bar per bow on theme B, as the
% winds' phrase and the violins' own 215-216 (were detached half notes and quarters); 217-218 Vln I-II and Vc change bow at will on the held f (PDF 39: do not overload the bow in slow passages; the Cb had it since c106).
codaTwoVlnOne = { des'''2\ff\> des'''4 c'''4 | f'''2.(\f ges'''4) | aes'''2( bes'''4 aes'''4) | ges'''2.( f'''4) | es''4( f'' ges'' aes'') | bes''( c''' des''' es''') | f'''1~\cbaw | f'''1 | <fis'' c'''>1\subP^\markup \italic "div." | <g'' c'''>1\< | <f'' b''>1\mp\< | b''2\f\<^\markup \italic "unis." r8 \once \override Beam.positions = #'(-0.25 . 0.25) g'''8( aes''' b''') | }
codaTwoVlnTwo = { aes''2\ff\> aes''4 ges''4 | f''2(\f des''2) | des''2( ges''4 f''4) | es''2.( des''4) | c''4( des'' es'' f'') | ges''( aes'' bes'' c''') | des'''1~\cbaw | des'''1 | <c'' fis''>1\subP^\markup \italic "div." | <c'' g''>1\< | <b' g''>1\mp\< | <d'' aes''>1\f\< | }
% c106 (playability; Adler ch. 3, PDF 76 and 88: in orchestral writing only easy double stops, otherwise divisi; PDF 108: the bass bow is shorter, so a lengthy tenuto is
%   marked 'change bow at will'): 211 violas restate 'div.' after the double bar, key change, letter O and page turn (div. since 205, held thirds/fourths 211-218);
%   217-218 basses 'change bow at will' on the tied F (two bars of Largamente at f, about 3.3 s).
% c138 (expression; Casanelles ch. 6, PDF 290: a soft line is heard only when what sounds with it is made quieter, in the hall that is done in the marking): 217-218 violas, cellos and basses diminish f > mp with the held F/A flat chord in the winds and low brass (c108), so the f echo of theme B in Hn 1-2 and the cor anglais (A flat 3-G flat 4) is not under f strings in its own register; they enter 219 at p. Vln I-II (F6/D flat 6, above the echo) keep f and the sub. p at 219.
codaTwoVla = { <des' f'>2\ff\>^\markup \italic "div." q | q\f q | <ges' bes'>2 q | <aes' c''>2 q | q q | <aes' des''>2 q | q\> q | q\mp q | <c' dis'>1\p^\markup \italic "div." | <c' e'>1\< | <b f'>1\mp\< | <d' f'>1\f\< | }
codaTwoVc = { des2\ff\> des'2 | des2\f des'2 | ges1 | aes1 | f1 | f,1 | f1~\cbaw\> | f1\mp | aes,1\p | g,1\< | g,1\mp\< | d1\f\< | }
codaTwoCb = { des,2\ff\> des2 | des,2\f des2 | ges,1 | aes,1 | f,1 | f,,1 | f,1~\cbaw\> | f,1\mp | aes,,1\p | g,,1\< | g,,1\mp\< | d,1\f\< | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); word cues (the drum staff takes no cue notes) at 221-222 before the first crash at 223, after 222 bars
codaTwoPerc = \drummode { R1*8 | R1*2 | \tag #'score { R1*2 } \tag #'part { R1^\markup \tiny "Tpt. 1: B, cresc." | R1^\markup \tiny "Fl. 1: scale" } | }

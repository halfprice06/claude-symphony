\version "2.24.0"
% CODA, bars 211-222 (c013: 211-214 augmented to 211-218; old 215-218 are now 219-222, every later bar +4). 211-218: the D flat episode, ff, in the trumpets: theme B's single recall from movement II, its second half,
% ending on D flat (mvt2 c100 sketch; cyclic-notes: give the forte D flat to the trumpets, not movement II's bar 61 tutti). D flat over F
% at 213-214 is the Neapolitan sixth of C. 215: German sixth of C spelled with D sharp in the violas; 216: cadential 6/4, the violas' D sharp
% rises to E natural (cyclic-notes 'Owed' item 9: the E flat/E natural thread closed in the violas with an augmented sixth); 217: V7;
% c013: theme B augmented (note values doubled, 8 bars, about 13 s at 2 = 72 against movement II's 16 s; was 6.7 s), so it is heard as the theme
% and not as a fast figure. Harmony per old half bar now per bar: D flat (211-212, re-struck f at 212), G flat maj7 (213: the F of trumpet 2 is the
% chord's 7th and falls to E flat in 214; no G flat above it), A flat 7 (214), F minor 7 (215), D flat over F (216-218, the scale in 215-216).
% 218 (c002): movement I's stop chord B-D-F-A flat itself, D in the bass (vii°6/5 over the timpani's G), so the arrival is not a root-position V-I (cadence plan: the first is 254-255). Top voice D flat - C - B (- C at 219).

% c028: 211-218 theme B phrased in two halves with a breath after 214, as movement II phrases it (mvt II bSec, breath between the halves);
% the upper woodwinds that double the trumpets (Fl 1-2, Ob 1, Cl 1, and Ob 2/Cl 2 on their shared staves) stay ff with them instead of dropping to f (Adler II PDF 188-189: doubling at pitch strengthens the tune)
% c042 (harmony; A&S PDF 380, 393, 388): 222 the Fl 1/Vln I run into C7 is G-A flat-B (was G-A natural-B against the held A flat of the stop chord: an augmented octave, and flat 6 replaced by natural 6 before it reaches 5).
% The augmented second A flat-B is an arpeggiation inside the diminished seventh (A&S PDF 380).
codaTwoTptOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~ | des''1~ | des''1) | c''1\subP | c''1\< | b'1\mp\< | b'1\f\< | }
codaTwoTptTwo = { f'2->(\ff aes'2 | des''2. es''4 | f''2 ges''4 f''4 | es''2. des''4) \breathe | c''2.( des''4 | aes'1~ | aes'1~ | aes'1) | fis'1\subP | g'1\< | f'1\mp\< | aes'1\f\< | }
codaTwoTptThree = { des'1\ff\> | des'1\f | ges'1 | es'1 | aes'1 | f'1 | f'1~ | f'1 | c'1\subP | e'1\< | d'1\mp\< | d'1\f\< | }
% c046 (Adler PDF 292, 303: periodic rests, after high playing): Hn 1-2 rest 211-214 (they played every bar 199-228, about 50 s, with written B flat 5 / G5 held at 207-210)
codaTwoHnOne = { R1*4 | aes'1\f | aes'1 | aes'1~ | aes'1 | aes'1\subP | g'1\< | g'1\mp\< | f'1\f\< | }
codaTwoHnTwo = { R1*4 | c'1\f | des'1 | des'1~ | des'1 | c'1\subP | c'1\< | d'1\mp\< | d'1\f\< | }
% c035 (Gould PDF 65, 67): 215-218 Hn 3 (F3) lies below Hn 4 (A flat 3); 215 is written as tied minims so the stems show the crossing that a semibreve chord hid. Sound unchanged.
codaTwoHnThree = { aes1\ff\> | aes1\f | des'1 | c'1 | f2~ f2 | f1 | f1~ | f1 | dis'1\subP | e'1\< | f'1\mp\< | d'1\f\< | }
codaTwoHnFour = { f1\ff\> | f1\f | ges1 | ges1 | aes2~ aes2 | aes1 | aes1~ | aes1 | c'1\subP | c'1\< | b1\mp\< | b1\f\< | }
codaTwoTbnOne = { f1\ff\> | f1\f | ges1 | es1 | f1 | f1 | f1~ | f1 | fis1\subP | g1\< | g1\mp\< | aes1\f\< | }
codaTwoTbnTwo = { des1\ff\> | des1\f | des1 | c1 | aes,1 | aes,1 | aes,1~ | aes,1 | c1\subP | c1\< | b,1\mp\< | b,1\f\< | }
codaTwoBassTbn = { des1\ff\> | des1\f | ges,1 | aes,1 | f,1 | f,1 | f,1~ | f,1 | aes,1\subP | g,1\< | g,1\mp\< | d1\f\< | }
codaTwoTuba = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 | f,,1 | f,,1 | f,,1~ | f,,1 | aes,,1\subP | g,,1\< | g,,1\mp\< | d,1\f\< | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
codaTwoTimp = { aes,4->\ff r4 r2 | aes,4\f r4 r2 | R1 | aes,4 r4 aes,4 r4 | R1*4 | aes,1:32\subP | g,1:32\<~ | g,1:32\mp\<~ | g,1:32\f\< | }
% c036 (Adler PDF 186: above A6 the flute's notes are approached best by scale): 222 Fl 1 joins Vln I's run G6-A6-B6 into the C7 at 223 (was a leap B5-C7 at fff).
codaTwoFluteOne = { aes''2->(\ff des'''2 | f'''2. ges'''4 | aes'''2 bes'''4 aes'''4 | ges'''2. f'''4) \breathe | es'''2.( f'''4 | des'''1~ | des'''1~ | des'''1) | c'''1\subP | c'''1\< | b''1\mp\< | b''2\f\< r8 g'''8( aes''' b''') | }
codaTwoFluteTwo = { aes''2->(\ff des'''2 | f'''2. ges'''4 | aes'''2 bes'''4 aes'''4 | ges'''2. f'''4) \breathe | es'''2.( f'''4 | des'''1~ | des'''1~ | des'''1) | fis''1\subP | g''1\< | f''1\mp\< | f''1\f\< | }
% c021: 211-218 Fl 1-2 a2 double trumpet 1's theme B an octave above (Rimsky-Korsakov PDF 75: in the top register two flutes suffice to double a trumpet at the upper octave)
% c019: 211-218 Ob 1 and Cl 1 double trumpet 1's theme B at the unison (Rimsky-Korsakov PDF 74-75: a wood-wind added to a brass melody gives a finer legato; Ex. 78, 93-94)
codaTwoOboeOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~ | des''1~ | des''1) | dis''1\subP | e''1\< | d''1\mp\< | d''1\f\< | }
% c010: 215 Ob 1 and Hn 3 spelled D sharp like the violas: E flat (Tpt 1, 213) becomes D sharp and rises to E (A&S PDF 588, 597-598).
% c035 (Gould PDF 65-67): 211 Ob 2 and Cl 2 as tied minims, so Ob 2's F5 above Ob 1's A flat is not read as one chord and Cl 2's unison A flat does not touch Cl 1's stem. Sound unchanged.
% c052 (harmony; A&S Unit 24, PDF 406-408): 214 Ob 2 resolves the 7th G flat to F with Ob 1 on beat 4 instead of holding it against the resolution.
codaTwoOboeTwo = { f''2\ff~ f''2 | f''1 | des''1 | ges''2. f''4 | es''1 | des''1 | des''1~ | des''1 | c''1\subP | e''1\< | d''1\mp\< | d''1\f\< | }
codaTwoClOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4) \breathe | es''2.( f''4 | des''1~ | des''1~ | des''1) | aes'1\subP | g'1\< | g'1\mp\< | aes'1\f\< | }
% c060 (cyclic lens; A&S Unit 29, PDF 504: the augmented sixth's sharp 4 is a passing tone to 5; Sebesky ch. 1, PDF 13-14, focus): 220 Cl 2 and Vln I (lower) take F sharp up to G, so the only E4 arriving by step from outside is the violas' D sharp -> E (with Hn 3), the thread's own voice
codaTwoClTwo = { aes'2\ff~ aes'2 | aes'1 | ges'1 | aes'1 | f'1 | f'1 | f'1~ | f'1 | fis'1\subP | g'1\< | f'1\mp\< | f'1\f\< | }
codaTwoBsnOne = { f1\ff\> | f1\f | bes1 | c'1 | aes1 | aes1 | aes1~ | aes1 | c'1\subP | c'1\< | b1\mp\< | b1\f\< | }
codaTwoBsnTwo = { des1\ff\> | des1\f | ges,1 | aes,1 | f,1 | f,1 | f,1~ | f,1 | aes,1\subP | g,1\< | g,1\mp\< | d,1\f\< | }
codaTwoCbsn = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 | f,,1 | f,,1 | f,,1~ | f,,1 | aes,,1\subP | g,,1\< | g,,1\mp\< | d,,1\f\< | }
% c051 (melody; Sebesky ch. 6, PDF 211-212, Ex. 279-280: a background line that shadows the tune too closely distorts the focus): 212 and 214 the violins no longer move a beat ahead of theme B
% (214 Vln I F5 against the tune's G flat 5, Vln II D flat 5 against E flat 5; 212 beat 4 A flat 5 against G flat 5); they now take the tune's own note on beat 4 (212 Vln I G flat; 214 Vln I and II dotted minim then F/D flat). Vln II keeps D flat at 212 (E flat there made fifths with Cl 2 into 213).
% c054 (orchestration; Adler ch. 8, PDF 249-250, 265-266): 212-214 Vln I doubles theme B an octave above Tpt 1 with the flutes (8'+4') instead of a shadow line that
% touched the tune at the unison on some beats and ran a third beside it on others (revises c051, keeps its aim: nothing moves against the tune).
codaTwoVlnOne = { des'''2\ff\> des'''4 c'''4 | f'''2.\f ges'''4 | aes'''2 bes'''4 aes'''4 | ges'''2. f'''4 | es''4( f'' ges'' aes'') | bes''( c''' des''' es''') | f'''1~ | f'''1 | <fis'' c'''>1\subP^\markup \italic "div." | <g'' c'''>1\< | <f'' b''>1\mp\< | b''2\f\<^\markup \italic "unis." r8 \once \override Beam.positions = #'(-0.25 . 0.25) g'''8( aes''' b''') | }
codaTwoVlnTwo = { aes''2\ff\> aes''4 ges''4 | f''2\f des''2 | des''2 ges''4 f''4 | es''2. des''4 | c''4( des'' es'' f'') | ges''( aes'' bes'' c''') | des'''1~ | des'''1 | <c'' fis''>1\subP^\markup \italic "div." | <c'' g''>1\< | <b' g''>1\mp\< | <d'' aes''>1\f\< | }
codaTwoVla = { <des' f'>2\ff\> q | q\f q | <ges' bes'>2 q | <aes' c''>2 q | q q | <aes' des''>2 q | q q | q q | <c' dis'>1\subP^\markup \italic "div." | <c' e'>1\< | <b f'>1\mp\< | <d' f'>1\f\< | }
codaTwoVc = { des2\ff\> des'2 | des2\f des'2 | ges1 | aes1 | f1 | f,1 | f1~ | f1 | aes,1\subP | g,1\< | g,1\mp\< | d1\f\< | }
codaTwoCb = { des,2\ff\> des2 | des,2\f des2 | ges,1 | aes,1 | f,1 | f,,1 | f,1~ | f,1 | aes,,1\subP | g,,1\< | g,,1\mp\< | d,1\f\< | }

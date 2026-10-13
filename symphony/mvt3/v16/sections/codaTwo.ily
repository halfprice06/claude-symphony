\version "2.24.0"
% CODA, bars 211-222 (c013: 211-214 augmented to 211-218; old 215-218 are now 219-222, every later bar +4). 211-218: the D flat episode, ff, in the trumpets: theme B's single recall from movement II, its second half,
% ending on D flat (mvt2 c100 sketch; cyclic-notes: give the forte D flat to the trumpets, not movement II's bar 61 tutti). D flat over F
% at 213-214 is the Neapolitan sixth of C. 215: German sixth of C spelled with D sharp in the violas; 216: cadential 6/4, the violas' D sharp
% rises to E natural (cyclic-notes 'Owed' item 9: the E flat/E natural thread closed in the violas with an augmented sixth); 217: V7;
% c013: theme B augmented (note values doubled, 8 bars, about 13 s at 2 = 72 against movement II's 16 s; was 6.7 s), so it is heard as the theme
% and not as a fast figure. Harmony per old half bar now per bar: D flat (211-212, re-struck f at 212), G flat maj7 (213: the F of trumpet 2 is the
% chord's 7th and falls to E flat in 214; no G flat above it), A flat 7 (214), F minor 7 (215), D flat over F (216-218, the scale in 215-216).
% 218 (c002): movement I's stop chord B-D-F-A flat itself, D in the bass (vii°6/5 over the timpani's G), so the arrival is not a root-position V-I (cadence plan: the first is 254-255). Top voice D flat - C - B (- C at 219).

codaTwoTptOne = { aes'2->(\ff des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4 | es''2. f''4 | des''1~ | des''1~ | des''1) | c''1\subP | c''1\< | b'1 | b'1 | }
codaTwoTptTwo = { f'2->(\ff aes'2 | des''2. es''4 | f''2 ges''4 f''4 | es''2. des''4 | c''2. des''4 | aes'1~ | aes'1~ | aes'1) | fis'1\subP | g'1\< | f'1 | aes'1 | }
codaTwoTptThree = { des'1\ff\> | des'1\f | ges'1 | es'1 | aes'1 | f'1 | f'1~ | f'1 | c'1\subP | e'1\< | d'1 | d'1 | }
codaTwoHnOne = { f'1\ff\> | f'1\f | ges'1 | ges'1 | aes'1 | aes'1 | aes'1~ | aes'1 | aes'1\subP | g'1\< | g'1 | f'1 | }
codaTwoHnTwo = { des'1\ff\> | des'1\f | des'1 | c'1 | c'1 | des'1 | des'1~ | des'1 | c'1\subP | c'1\< | d'1 | d'1 | }
codaTwoHnThree = { aes1\ff\> | aes1\f | des'1 | c'1 | f1 | f1 | f1~ | f1 | dis'1\subP | e'1\< | f'1 | d'1 | }
codaTwoHnFour = { f1\ff\> | f1\f | ges1 | ges1 | aes1 | aes1 | aes1~ | aes1 | c'1\subP | c'1\< | b1 | b1 | }
codaTwoTbnOne = { f1\ff\> | f1\f | ges1 | es1 | f1 | f1 | f1~ | f1 | fis1\subP | g1\< | g1 | aes1 | }
codaTwoTbnTwo = { des1\ff\> | des1\f | des1 | c1 | aes,1 | aes,1 | aes,1~ | aes,1 | c1\subP | c1\< | b,1 | b,1 | }
codaTwoBassTbn = { des1\ff\> | des1\f | ges,1 | aes,1 | f,1 | f,1 | f,1~ | f,1 | aes,1\subP | g,1\< | g,1 | d1 | }
codaTwoTuba = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 | f,,1 | f,,1 | f,,1~ | f,,1 | aes,,1\subP | g,,1\< | g,,1 | d,1 | }
codaTwoTimp = { aes,4->\ff r4 r2 | aes,4\f r4 r2 | R1 | aes,4 r4 aes,4 r4 | R1*4 | aes,1:32\subP | g,1:32\< | g,1:32 | g,1:32 | }
codaTwoFluteOne = { f'''1\ff\> | f'''1\f | f'''1 | es'''1 | f'''1 | aes'''1 | f'''1~ | f'''1 | c'''1\subP\< | c'''1 | b''1 | b''1 | }
codaTwoFluteTwo = { des'''1\ff\> | des'''1\f | des'''1 | c'''1 | c'''1 | f'''1 | des'''1~ | des'''1 | fis''1\subP\< | g''1 | f''1 | f''1 | }
codaTwoOboeOne = { aes''1\ff\> | aes''1\f | f''1 | aes''1 | aes''1 | f''1 | aes''1~ | aes''1 | dis''1\subP\< | e''1 | d''1 | d''1 | }
% c010: 215 Ob 1 and Hn 3 spelled D sharp like the violas: E flat (Tpt 1, 213) becomes D sharp and rises to E (A&S PDF 588, 597-598).
codaTwoOboeTwo = { f''1\ff\> | f''1\f | des''1 | ges''1 | es''1 | des''1 | des''1~ | des''1 | c''1\subP\< | e''1 | d''1 | d''1 | }
codaTwoClOne = { des''1\ff\> | des''1\f | des''1 | c''1 | c''1 | aes'1 | aes'1~ | aes'1 | aes'1\subP\< | g'1 | g'1 | aes'1 | }
codaTwoClTwo = { aes'1\ff\> | aes'1\f | ges'1 | aes'1 | f'1 | f'1 | f'1~ | f'1 | fis'1\subP\< | e'1 | f'1 | f'1 | }
codaTwoBsnOne = { f1\ff\> | f1\f | bes1 | c'1 | aes1 | aes1 | aes1~ | aes1 | c'1\subP\< | c'1 | b1 | b1 | }
codaTwoBsnTwo = { des1\ff\> | des1\f | ges,1 | aes,1 | f,1 | f,1 | f,1~ | f,1 | aes,1\subP\< | g,1 | g,1 | d,1 | }
codaTwoCbsn = { des,1\ff\> | des,1\f | ges,,1 | aes,,1 | f,,1 | f,,1 | f,,1~ | f,,1 | aes,,1\subP\< | g,,1 | g,,1 | d,,1 | }
codaTwoVlnOne = { des'''2\ff\> des'''4 c'''4 | bes''2\f aes''2 | f''2 bes''4 aes''4 | ges''2 f''2 | es''4( f'' ges'' aes'' | bes'' c''' des''' es''') | f'''1~ | f'''1 | <fis'' c'''>1\subP\< | <e'' c'''>1 | <f'' b''>1 | b''2 r8 \once \override Beam.positions = #'(-0.25 . 0.25) g'''8( a''' b''') | }
codaTwoVlnTwo = { aes''2\ff\> aes''4 ges''4 | f''2\f des''2 | des''2 ges''4 f''4 | es''2 des''2 | c''4( des'' es'' f'' | ges'' aes'' bes'' c''') | des'''1~ | des'''1 | <c'' fis''>1\subP\< | <c'' g''>1 | <b' g''>1 | <d'' aes''>1 | }
codaTwoVla = { <des' f'>2\ff\> q | q\f q | <ges' bes'>2 q | <aes' c''>2 q | q q | <aes' des''>2 q | q q | q q | <c' dis'>1\subP\< | <c' e'>1 | <b f'>1 | <d' f'>1 | }
codaTwoVc = { des2\ff\> des'2 | des2\f des'2 | ges1 | aes1 | f1 | f,1 | f1~ | f1 | aes,1\subP\< | g,1 | g,1 | d1 | }
codaTwoCb = { des,2\ff\> des2 | des,2\f des2 | ges,1 | aes,1 | f,1 | f,,1 | f,1~ | f,1 | aes,,1\subP\< | g,,1 | g,,1 | d,1 | }

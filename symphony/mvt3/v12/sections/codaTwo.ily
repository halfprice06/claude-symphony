\version "2.24.0"
% CODA, bars 211-218. 211-214: the D flat episode, ff, in the trumpets: theme B's single recall from movement II, its second half,
% ending on D flat (mvt2 c100 sketch; cyclic-notes: give the forte D flat to the trumpets, not movement II's bar 61 tutti). D flat over F
% at 213-214 is the Neapolitan sixth of C. 215: German sixth of C spelled with D sharp in the violas; 216: cadential 6/4, the violas' D sharp
% rises to E natural (cyclic-notes 'Owed' item 9: the E flat/E natural thread closed in the violas with an augmented sixth); 217: V7;
% 218 (c002): movement I's stop chord B-D-F-A flat itself, D in the bass (vii°6/5 over the timpani's G), so the arrival is not a root-position V-I (cadence plan: the first is 254-255). Top voice D flat - C - B (- C at 219).

codaTwoTptOne = { aes'4->(\ff des''4 f''4. ges''8 | aes''4 bes''8 aes''8 ges''4. f''8 | es''4. f''8 des''2~ | des''1) | c''1\subP | c''1\< | b'1 | b'1 | }
codaTwoTptTwo = { f'4->(\ff aes'4 des''4. es''8 | f''4 ges''8 f''8 es''4. des''8 | c''4. des''8 aes'2~ | aes'1) | fis'1\subP | g'1\< | f'1 | aes'1 | }
codaTwoTptThree = { des'1\ff\> | ges'2\f es'2 | aes'2 f'2 | f'1 | c'1\subP | e'1\< | d'1 | d'1 | }
codaTwoHnOne = { f'1\ff\> | ges'2\f ges'2 | aes'2 aes'2 | aes'1 | aes'1\subP | g'1\< | g'1 | f'1 | }
codaTwoHnTwo = { des'1\ff\> | des'2\f c'2 | c'2 des'2 | des'1 | c'1\subP | c'1\< | d'1 | d'1 | }
codaTwoHnThree = { aes1\ff\> | des'2\f c'2 | f2 f2 | f1 | dis'1\subP | e'1\< | f'1 | d'1 | }
codaTwoHnFour = { f1\ff\> | ges2\f ges2 | aes2 aes2 | aes1 | c'1\subP | c'1\< | b1 | b1 | }
codaTwoTbnOne = { f1\ff\> | ges2\f es2 | f2 f2 | f1 | fis1\subP | g1\< | g1 | aes1 | }
codaTwoTbnTwo = { des1\ff\> | des2\f c2 | aes,2 aes,2 | aes,1 | c1\subP | c1\< | b,1 | b,1 | }
codaTwoBassTbn = { des1\ff\> | ges,2\f aes,2 | f,1 | f,1 | aes,1\subP | g,1\< | g,1 | d1 | }
codaTwoTuba = { des,1\ff\> | ges,,2\f aes,,2 | f,,1 | f,,1 | aes,,1\subP | g,,1\< | g,,1 | d,1 | }
codaTwoTimp = { aes,4->\ff r4 r2 | aes,4\f r4 aes,4 r4 | R1*2 | aes,1:32\subP | g,1:32\< | g,1:32 | g,1:32 | }
codaTwoFluteOne = { f'''1\ff\> | ges'''2\f es'''2 | f'''2 aes'''2 | f'''1 | c'''1\subP\< | c'''1 | b''1 | b''1 | }
codaTwoFluteTwo = { des'''1\ff\> | des'''2\f c'''2 | c'''2 f'''2 | des'''1 | fis''1\subP\< | g''1 | f''1 | f''1 | }
codaTwoOboeOne = { aes''1\ff\> | bes''2\f aes''2 | aes''2 f''2 | aes''1 | dis''1\subP\< | e''1 | d''1 | d''1 | }
% c010: 215 Ob 1 and Hn 3 spelled D sharp like the violas: E flat (Tpt 1, 213) becomes D sharp and rises to E (A&S PDF 588, 597-598).
codaTwoOboeTwo = { f''1\ff\> | ges''2\f ges''2 | es''2 des''2 | des''1 | c''1\subP\< | e''1 | d''1 | d''1 | }
codaTwoClOne = { des''1\ff\> | des''2\f c''2 | c''2 aes'2 | aes'1 | aes'1\subP\< | g'1 | g'1 | aes'1 | }
codaTwoClTwo = { aes'1\ff\> | ges'2\f aes'2 | f'2 f'2 | f'1 | fis'1\subP\< | e'1 | f'1 | f'1 | }
codaTwoBsnOne = { f1\ff\> | bes2\f c'2 | aes2 aes2 | aes1 | c'1\subP\< | c'1 | b1 | b1 | }
codaTwoBsnTwo = { des1\ff\> | ges,2\f aes,2 | f,1 | f,1 | aes,1\subP\< | g,1 | g,1 | d,1 | }
codaTwoCbsn = { des,1\ff\> | ges,,2\f aes,,2 | f,,1 | f,,1 | aes,,1\subP\< | g,,1 | g,,1 | d,,1 | }
codaTwoVlnOne = { des'''4\ff\> des'''8 c''' bes''4 aes''4 | ges''4\f bes''8 aes'' ges''4 f''4 | es''8( f'' ges'' aes'' bes'' c''' des''' es''') | f'''1 | <fis'' c'''>1\subP\< | <e'' c'''>1 | <f'' b''>1 | b''2 r8 g'''8( a''' b''') | }
codaTwoVlnTwo = { aes''4\ff\> aes''8 ges'' f''4 des''4 | des''4\f ges''8 f'' es''4 des''4 | c''8( des'' es'' f'' ges'' aes'' bes'' c''') | des'''1 | <c'' fis''>1\subP\< | <c'' g''>1 | <d'' g''>1 | <d'' aes''>1 | }
codaTwoVla = { <des' f'>1\ff\> | <ges' bes'>2\f <aes' c''>2 | <aes' c''>1 | <aes' des''>1 | <c' dis'>1\subP\< | <c' e'>1 | <d' f'>1 | <d' f'>1 | }
codaTwoVc = { des2\ff\> des'2 | ges2\f aes2 | f2 f,2 | f1 | aes,1\subP\< | g,1 | g,1 | d1 | }
codaTwoCb = { des,2\ff\> des2 | ges,2\f aes,2 | f,2 f,,2 | f,1 | aes,,1\subP\< | g,,1 | g,,1 | d,1 | }

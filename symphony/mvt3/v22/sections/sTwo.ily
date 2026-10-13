\version "2.24.0"
% SECOND THEME IN MAJOR, bars 67-82, E flat major: theme F2 in the violins in octaves (Vln I at B flat 6 at most, 78, c011; movement III's
% C7 is kept for the C-major arrival at 219), the cellos' counter-melody (the bass counterline movement I lacked), harp broken chords,
% violas off the beat. Flute 1 and oboe 1 join the tune from 77 for its climax. 81-82 animando into the closing group.

sTwoVlnOne = { bes''2.(\mf^\markup \italic "arco, cantabile" g''4) | f''4( es''4 g''4 bes''4) | f'''2( es'''4 d'''4) | c'''2( bes''2) | aes''2.( c'''4) | bes''4( aes''4 g''4 f''4) | g''2( es''2) | f''1 | bes''2.( g''4) | f''4( es''4 g''4 bes''4)\< | es'''2. f'''4\upbow | bes'''4(\f\downbow aes'''4 g'''4 f'''4) | es'''2.( d'''4) | c'''4( bes''4 aes''4 g''4)\> | f''2( d''2) | es''1\mf | }
sTwoVlnTwo = { bes'2.(\mf^\markup \italic "arco" g'4) | f'4( es'4 g'4 bes'4) | f''2( es''4 d''4) | c''2( bes'2) | aes'2.( c''4) | bes'4( aes'4 g'4 f'4) | g'2( es'2) | f'1 | bes'2.( g'4) | f'4( es'4 g'4 bes'4)\< | es''2. f''4\upbow | bes''4(\f\downbow aes''4 g''4 f''4) | es''2.( d''4) | c''4( bes'4 aes'4 g'4)\> | f'2( d'2) | es'1\mf | }
sTwoFluteOne = { R1*10 | es'''2.(\p\< f'''4 | bes'''4\f aes'''4 g'''4 f'''4) | es'''2.( d'''4 | c'''4 bes''4 aes''4 g''4\> | f''2 d''2 | es''1)\mf | }
sTwoOboeOne = { R1*10 | es''2.(\p\< f''4 | bes''4\f aes''4 g''4 f''4) | es''2.( d''4 | c''4 bes'4 aes'4 g'4\> | f'2 d'2 | es'1)\mf | }
sTwoVc = { g2(\mf^\markup \italic "arco, espress." aes4 bes4) | aes2( g2) | c'2( es'4 d'4) | c'2( bes2) | aes2( c'4 es'4) | d'2( aes2) | g2( bes4 aes4) | aes2( f2) | g2( aes4 bes4) | aes2( g2) | bes2( c'4 f'4) | es'2( d'2) | c'2( aes4 c'4) | es'2( d'2) | aes2( f2) | g1 | }
sTwoVla = { g2(\mf^\markup \italic "arco, unis., espress." aes4 bes4) | aes2( g2) | c'2( es'4 d'4) | c'2( bes2) | aes2( c'4 es'4) | d'2( aes2) | g2( bes4 aes4) | aes2( f2) | g2( aes4 bes4) | aes2( g2) | bes2( c'4 f'4) | es'2( d'2) | c'2( aes4 c'4) | es'2( d'2) | aes2( f2) | g1 | }
sTwoCb = { es,1\mf^\markup \italic "arco" | d,2 es,2 | c,1 | aes,,2 g,,2 | f,,1 | bes,,1 | es,2 c,2 | bes,,1 | g,,2 es,2 | d,2 es,2 | g,,2 aes,,2 | c,2 d,2 | aes,,1 | aes,,2 bes,,2 | bes,,1 | es,1 | }
sTwoBsnTwo = { es1\pp | d2 es2 | c1 | aes,2 g,2 | f,1 | bes,1 | es2 c2 | bes,1 | g,2 es2 | d2 es2 | g,2 aes,2 | c2 d2 | aes,1 | aes,2 bes,2 | bes,1 | es1 | }
sTwoHarpR = { \stemUp es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 | f'8 aes'8 bes'8 d''8 es'8 g'8 bes'8 es''8 | es'8 aes'8 c''8 es''8 es'8 aes'8 c''8 es''8 | es'8 aes'8 c''8 es''8 es'8 g'8 bes'8 es''8 | es'8 f'8 aes'8 c''8 es'8 f'8 aes'8 c''8 | f'8 bes'8 d''8 f''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 c''8 es''8 | f'8 bes'8 d''8 f''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 | f'8 aes'8 bes'8 d''8 es'8 g'8 bes'8 es''8 | es'8 g'8 bes'8 es''8 es'8 f'8 aes'8 c''8 | es'8 g'8 c''8 es''8 f'8 bes'8 d''8 f''8 | es'8 aes'8 c''8 es''8 es'8 aes'8 c''8 es''8 | es'8 aes'8 c''8 es''8 f'8 bes'8 d''8 f''8 | f'8 aes'8 bes'8 d''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 \stemNeutral | }
sTwoHarpL = { es,1\mf^\markup \small \harp-pedal #"--^|^--^" | d,2 es,2 | c,1 | aes,,2 g,,2 | f,,1 | bes,,1 | es,2 c,2 | bes,,1 | g,,2 es,2 | d,2 es,2 | g,,2 aes,,2 | c,2 d,2 | aes,,1 | aes,,2 bes,,2 | bes,,1 | es,1 | }
sTwoClOne = { es'1\pp | d'2 es'2 | es'1 | es'1 | es'1 | d'1 | es'1 | d'1 | es'1 | d'2 es'2 | es'1 | es'2 d'2 | es'1 | es'2 d'2 | d'1 | es'1 | }
sTwoClTwo = { bes1\pp | aes2 bes2 | aes1 | aes2 bes2 | aes1 | bes2 aes2 | bes2 c'2 | bes2 aes2 | bes1 | aes2 bes2 | bes2 aes2 | c'2 bes2 | aes1 | aes2 bes2 | aes1 | bes1 | }
sTwoBsnOne = { es1\pp | d2 es2 | c1 | c2 es2 | c1 | d1 | es2 c2 | d1 | es1 | d2 es2 | es2 c2 | c2 d2 | c1 | c2 d2 | d1 | es1 | }
sTwoHnOne = { R1*8 | es'1\p | d'2 es'2 | es'2 c'2 | c'2 d'2 | c'1 | c'2 d'2 | d'1 | es'1 | }
sTwoHnTwo = { R1*8 | g1\p | aes2 g2 | g2 aes2 | g2 bes2 | aes1 | aes2 bes2 | aes1 | g1 | }

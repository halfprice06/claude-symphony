\version "2.24.0"
% COUNTERSTATEMENT, bars 27-42, ff. Theme F1 in the bass (cellos, violas, bassoons, horns 3-4; basses an octave lower);
% the violins play a running countersubject in eighths (Adler part 2 PDF 172-186: polyphonic texture, foreground and counterline).
% 35-38: the head in the violins in A flat, then B flat minor; 39-42: V of E flat, diminuendo into the transition.
% Woodwinds and horns 1-2 hold the harmony; trombones join at 35. No repeated-eighth hammering in the basses: that layout is
% movement I's first-theme tutti and is kept for the coda (cyclic-notes 'Owed' item 7).

pTwoVlnOne = { c'''8(\ff bes'' aes'' g'' f'' d'' b' d'') | bes'8( d'' f'' aes'' c''' aes'' f'' c'') | b'8( d'' f'' d'' g'' f'' es'' d'') | b'8( c'' d'' f'' es'' g'' c''' es''') | d'''8( c''' bes'' g'' es'' g'' bes'' es''') | des'''8( c''' bes'' aes'' f'' aes'' c''' f''') | aes''8( g'' f'' es'' d'' f'' aes'' c''') | b''8( c''' d''' b'' g''4) r4 | aes''2->( es''4. f''8 | g''4-.) f''8( es''8 des''4-.) c''4-. | bes''2->( f''4. ges''8 | aes''4-.) ges''8( f''8 es''4-.) d''4-. | f''2->(\> bes'4. c''8 | d''4-.) c''8( bes'8 aes'4-.) g'4-. | f'2( d'4. es'8 | f'2.)\mf r4 | }
pTwoVlnTwo = { c''8(\ff bes' aes' g' f' d' b d') | bes8( d' f' aes' c'' aes' f' c') | b8( d' f' d' g' f' es' d') | b8( c' d' f' es' g' c'' es'') | d''8( c'' bes' g' es' g' bes' es'') | des''8( c'' bes' aes' f' aes' c'' f'') | aes'8( g' f' es' d' f' aes' c'') | b'8( c'' d'' b' g'4) r4 | aes'2->( es'4. f'8 | g'4-.) f'8( es'8 des'4-.) c'4-. | bes'2->( f'4. ges'8 | aes'4-.) ges'8( f'8 es'4-.) d'4-. | f'2->(\> bes4. c'8 | d'4-.) c'8( bes8 aes4-.) g4-. | f'2( d'4. es'8 | f'2.)\mf r4 | }
pTwoVc = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | aes,1 | es2 aes,2 | bes,1 | f,2 bes,2 | bes,1\> | bes,1 | bes,1 | bes,2. r4\mf | }
pTwoVla = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | aes2 c'2 | es'2 c'2 | bes2 des'2 | c'2 d'2 | d'1\> | d'1 | aes1 | f2. r4\mf | }
pTwoBsnOne = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | aes1 | g2 aes2 | des'1 | c'2 d'2 | d'1\> | d'1 | d'1 | d'2. r4\mf | }
pTwoBsnTwo = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | aes,1 | es2 aes,2 | bes,1 | f,2 bes,2 | bes,1\> | bes,1 | bes,1 | bes,2. r4\mf | }
pTwoHnThree = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | c'1 | bes2 c'2 | des'1 | c'2 d'2 | f'1\> | f'1 | f'1 | f'2. r4\mf | }
pTwoHnFour = { c'2->(\ff g4. aes8 | bes4-.) aes8( g8 f4-.) es4-. | d4( g8 aes8 b4 d'4) | f'2-> es'4( d'4) | es'2->( bes4. c'8 | des'4-.) c'8( bes8 aes4-.) g4-. | f4( aes8 c'8 f'4 aes'4) | g'2.-> r4 | aes1 | g2 aes2 | bes1 | a2 bes2 | bes1\> | bes1 | bes1 | bes2. r4\mf | }
pTwoCb = { c2->(\ff g,4. aes,8 | bes,4-.) aes,8( g,8 f,4-.) es,4-. | d,4( g,8 aes,8 b,4 d4) | f2-> es4( d4) | es2->( bes,4. c8 | des4-.) c8( bes,8 aes,4-.) g,4-. | f,4( aes,8 c8 f4 aes4) | g2.-> r4 | aes,,1 | es,2 aes,,2 | bes,,1 | f,2 bes,,2 | bes,,1\> | bes,,1 | bes,,1 | bes,,2. r4\mf | }
pTwoCbsn = { c,2->(\ff g,,4. aes,,8 | bes,,4-.) aes,,8( g,,8 f,,4-.) es,,4-. | d,,4( g,,8 aes,,8 b,,4 d,4) | f,2-> es,4( d,4) | es,2->( bes,,4. c,8 | des,4-.) c,8( bes,,8 aes,,4-.) g,,4-. | R1*2 | aes,,1 | es,2 aes,,2 | bes,,1 | f,2 bes,,2 | bes,,1\> | bes,,1 | R1*2\! | }
pTwoFluteOne = { g''1\f | bes''2 aes''2 | g''1 | g''1 | g''1 | aes''1 | aes''1 | g''1 | aes''1 | g''2 aes''2 | des'''1 | c'''2 d'''2 | bes''1 | aes''1 | aes''1 | aes''1 | }
pTwoFluteTwo = { es''2\f d''2 | d''2 f''2 | d''1 | d''2 es''2 | es''1 | f''1 | f''2 d''2 | d''1 | es''1 | es''1 | des''1 | es''2 d''2 | d''1 | d''1 | d''1 | d''1 | }
pTwoOboeOne = { es''2\f d''2 | d''2 f''2 | d''1 | d''2 es''2 | es''1 | f''1 | f''2 d''2 | d''1 | es''1 | des''2 es''2 | des''1 | es''2 d''2 | d''1 | d''1 | d''1 | d''1 | }
pTwoOboeTwo = { g'1\f | bes'2 aes'2 | g'1 | g'1 | g'1 | aes'1 | aes'1 | g'1 | aes'1 | g'2 aes'2 | bes'1 | a'2 bes'2 | bes'1 | aes'1 | aes'1 | aes'1 | }
pTwoClOne = { g'1\f | f'2 aes'2 | f'1 | f'2 g'2 | g'1 | aes'1 | aes'2 f'2 | g'1 | aes'1 | g'2 aes'2 | bes'1 | f'1 | f'1 | f'1 | f'1 | f'1 | }
pTwoClTwo = { c'2\f b2 | bes2 c'2 | b1 | b2 c'2 | c'2 bes2 | des'2 c'2 | c'1 | b1 | c'1 | bes2 c'2 | bes1 | c'2 bes2 | bes1 | bes1 | bes1 | bes1 | }
pTwoHnOne = { g'1\f | f'1 | f'1 | f'2 g'2 | g'1 | f'1 | f'1 | g'1 | aes'1 | g'2 aes'2 | f'1 | f'1 | f'1 | f'1 | f'1 | f'1 | }
pTwoHnTwo = { c'2\f b2 | bes2 c'2 | b1 | b2 c'2 | c'2 bes2 | des'2 c'2 | c'1 | b1 | c'1 | bes2 c'2 | bes1 | a2 bes2 | bes1 | bes1 | bes1 | bes1 | }
pTwoTbnOne = { R1*8 | es1\f | es2 es2 | des1 | c2 d2 | f1\> | f1 | R1*2\! | }
pTwoTbnTwo = { R1*8 | c1\f | bes,2 c2 | bes,1 | a,2 bes,2 | d1\> | d1 | R1*2\! | }
pTwoBassTbn = { R1*8 | aes,1\f | es2 aes,2 | bes,1 | f,2 bes,2 | bes,1\> | bes,1 | R1*2\! | }
pTwoTimp = { c4->\ff r4 r2 | R1*3 | c4-> r4 r2 | R1 | R1 | g,4-> g,4 g,4 r4 | aes,4->\f r4 r2 | es4 r4 aes,4 r4 | R1*6 | }

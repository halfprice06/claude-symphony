\version "2.24.0"
% CLOSING GROUP, bars 83-98, E flat major, Tempo I, f to ff. 83-86: theme F1's head in major in the high winds and violins;
% 87-90: the head in the low strings and bassoons under the violins' turn figure (motive x), cadence in E flat at 90 (root V-I is
% allowed in E flat; the rule against it applies to C); 91-94: codetta chords, the brass's off-beat rhythm; 95-98: the E flat chord
% gains its seventh (V7 of A flat), then the bass falls E flat - D flat - C to V of F minor, diminuendo to p: the development starts in F minor.

% c032 (harmony; A&S PDF 267): 88-89 Tbn 2 D3-E flat3 | F3 (was F3-E flat3 | D3: 5ths with the bass's B flat-A flat at 88 and with Vln I's A-B flat at 89-90).
% c053 (form; A&S Unit 18, PDF 290-292, Ex. 18-2/18-3, Mendelssohn Op. 53/3: a descending series of 6/3 chords is a contrapuntal bridge from the tonic to the cadence;
% PDF 291: the upper voices may move in parallel 4ths; PDF 293: alternate doublings, leading tone not doubled): 87-90 no longer state F1's head in the low strings and
% bassoons. That layout (Vla, Vc, Cb, bassoons, f) opens the development nine bars later (99), so the development entered with the closing group's own idea and only the
% key marked the new section. 87-90 are now I6 - vii6 - vi6 - V6 - ii4/3 - V7 - I over the bass G-F-E flat-D-C-B flat-E flat (Vc, Cb, Bn 2, Cbn), the 6/3 voices in
% Vla (double stops), Tbn 1-2 and Bn 1, under the unchanged violin scale figure (89b: F, not D, under the violins' A-B flat, which would make fifths into 90); the horn off-beats at 89-90 follow the new chords (they had I on V and V on I); the 7th A flat of V7 is only in Bn 1 and Tbn 1 (unison), not doubled at the octave.
% c052 (harmony; A&S Unit 25, PDF 439 rule of doubling, PDF 405: the 7th resolves down): 96 the bass stays on E flat (E flat 7 in root position, its 7th D flat only in the top voice) instead of doubling the soprano's E flat-D flat-C in octaves; 97 Cl 1 C5, so the 7th B flat of C7 is not doubled.
% c054 (orchestration; Adler ch. 8, PDF 255, 257, 266): 87-90 Tbn 1-2 rest (they doubled Bn 1 and the violas' 6/3 voices at the unison, f, in the A3-E flat4 register of Vln II's
% scale figure); Fl 1 doubles Vln I's figure at pitch (without its low octave notes), so the figure carries; the trombones' first entry is now the ff codetta at 91.
closVlnOne = { es'''2->(\f bes''4. c'''8 | d'''4-.) c'''8( bes''8 aes''4-.) g''4-. | f''4( bes''8 c'''8 d'''4 f'''4) | es'''2-> r2 | r4 bes''8( aes'' g'' f'') es''( d'' | es''8 f'' g'' aes'') bes''4-> bes'4-> | r4 f''8( es'' d'' c'') bes'( a' | bes'8 c'' d'' es'') f''4-> f'4-> | <bes' g''>4->\ff r8 <bes' g''>8 <bes' aes''>4-> r4 | <bes' g''>4-> r8 <bes' g''>8 <bes' aes''>4-> r4 | <g' es''>4-> r4 <bes' d''>4-> r4 | <g' es''>2-> r2 | es''1\>( | des''1) | c''1\p~ | c''2. r4 | }
closVlnTwo = { es''2->(\f bes'4. c''8 | d''4-.) c''8( bes'8 aes'4-.) g'4-. | f'4( bes'8 c''8 d''4 f''4) | es''2-> r2 | r4 bes'8( aes' g' f') es'( d' | es'8 f' g' aes') bes'4-> bes4-> | r4 f'8( es' d' c') bes( a | bes8 c' d' es') f'4-> f'4-> | <es' bes'>4->\ff r8 <es' bes'>8 <d' bes'>4-> r4 | <es' bes'>4-> r8 <es' bes'>8 <d' bes'>4-> r4 | <es' bes'>4-> r4 <d' bes'>4-> r4 | <es' bes'>2-> r2 | g'1\>( | g'1) | g'1\p~ | g'2. r4 | }
closFluteOne = { es'''2->(\f bes''4. c'''8 | d'''4-.) c'''8( bes''8 aes''4-.) g''4-. | f''4( bes''8 c'''8 d'''4 f'''4) | es'''2-> r2 | r4 bes''8(\f aes'' g'' f'') es''( d'' | es''8 f'' g'' aes'') bes''4-> r4 | r4 f''8( es'' d'' c'') bes'( a' | bes'8 c'' d'' es'') f''4-> r4 | g'''4->\ff r8 g'''8 aes'''4-> r4 | g'''4-> r8 g'''8 aes'''4-> r4 | es'''4-> r4 d'''4-> r4 | es'''2-> r2 | R1*4 | }
closFluteTwo = { es''2->(\f bes'4. c''8 | d''4-.) c''8( bes'8 aes'4-.) g'4-. | f'4( bes'8 c''8 d''4 f''4) | es''2-> r2 | R1*4 | es'''4->\ff r8 es'''8 f'''4-> r4 | es'''4-> r8 es'''8 f'''4-> r4 | bes''4-> r4 bes''4-> r4 | bes''2-> r2 | R1*4 | }
closOboeOne = { es''2->(\f bes'4. c''8 | d''4-.) c''8( bes'8 aes'4-.) g'4-. | f'4( bes'8 c''8 d''4 f''4) | es''2-> r2 | R1*4 | bes''4->\ff r8 bes''8 bes''4-> r4 | bes''4-> r8 bes''8 bes''4-> r4 | g''4-> r4 f''4-> r4 | g''2-> r2 | es''1\p( | des''1) | c''1~ | c''2. r4 | }
closOboeTwo = { R1*4 | R1*4 | g'4->\ff r8 g'8 aes'4-> r4 | g'4-> r8 g'8 aes'4-> r4 | es''4-> r4 d''4-> r4 | es''2-> r2 | R1*4 | }
closClOne = { es'2->(\f bes4. c'8 | d'4-.) c'8( bes8 aes4-.) g4-. | f4( bes8 c'8 d'4 f'4) | es'2-> r2 | R1*4 | es''4->\ff r8 es''8 d''4-> r4 | es''4-> r8 es''8 d''4-> r4 | bes'4-> r4 bes'4-> r4 | bes'2-> r2 | bes'1\p~ | bes'1 | c''1~ | c''2. r4 | }
closClTwo = { es'2->(\f bes4. c'8 | d'4-.) c'8( bes8 aes4-.) g4-. | f4( bes8 c'8 d'4 f'4) | es'2-> r2 | R1*4 | bes'4->\ff r8 bes'8 bes'4-> r4 | bes'4-> r8 bes'8 bes'4-> r4 | g'4-> r4 f'4-> r4 | g'2-> r2 | g'1\p~ | g'1 | e'1~ | e'2. r4 | }
closBsnOne = { es'1\f | f'2 bes2 | bes2 aes2 | g2 r2 | es'2\f d'2 | c'2 bes2 | aes2 aes2 | g2-> r2 | g4->\ff r8 g8 aes4-> r4 | g4-> r8 g8 aes4-> r4 | es'4-> r4 d'4-> r4 | es'2-> r2 | R1*4 | }
closBsnTwo = { es1\f | aes,2 bes,2 | d2 bes,2 | es2 r2 | g2\f f2 | es2 d2 | c2 bes,2 | es2-> r2 | es4->\ff r8 es8 d4-> r4 | es4-> r8 es8 d4-> r4 | g4-> r4 f4-> r4 | es2-> r2 | es1\p~ | es1 | c1~ | c2. r4 | }
closCbsn = { R1*4 | g,2\f f,2 | es,2 d,2 | c,2 bes,,2 | es,2-> r2 | es,4->\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }
closHnOne = { R1*4 | R1*2 | r4 aes'4->\f r4 bes'4-> | r4 g'4-> r4 bes'4-> | g'4->\ff r8 g'8 aes'4-> r4 | g'4-> r8 g'8 aes'4-> r4 | g'4-> r4 aes'4-> r4 | g'2-> r2 | R1*4 | }
closHnTwo = { R1*4 | R1*2 | r4 f'4->\f r4 f'4-> | r4 es'4-> r4 f'4-> | es'4->\ff r8 es'8 f'4-> r4 | es'4-> r8 es'8 f'4-> r4 | es'4-> r4 f'4-> r4 | es'2-> r2 | R1*4 | }
closHnThree = { R1*4 | R1*2 | r4 c'4->\f r4 d'4-> | r4 bes4-> r4 d'4-> | bes4->\ff r8 bes8 bes4-> r4 | bes4-> r8 bes8 bes4-> r4 | bes4-> r4 bes4-> r4 | bes2-> r2 | R1*4 | }
closHnFour = { R1*4 | R1*2 | r4 aes4->\f r4 bes4-> | r4 g4-> r4 bes4-> | g4->\ff r8 g8 f4-> r4 | g4-> r8 g8 f4-> r4 | g4-> r4 f4-> r4 | g2-> r2 | R1*4 | }
closTptOne = { R1*8 | bes'4->\ff r8 bes'8 bes'4-> r4 | bes'4-> r8 bes'8 bes'4-> r4 | bes'4-> r4 bes'4-> r4 | bes'2-> r2 | R1*4 | }
closTptTwo = { R1*8 | g'4->\ff r8 g'8 f'4-> r4 | g'4-> r8 g'8 f'4-> r4 | g'4-> r4 f'4-> r4 | g'2-> r2 | R1*4 | }
closTptThree = { R1*8 | es'4->\ff r8 es'8 d'4-> r4 | es'4-> r8 es'8 d'4-> r4 | es'4-> r4 d'4-> r4 | es'2-> r2 | R1*4 | }
closTbnOne = { R1*8 | g4->\ff r8 g8 aes4-> r4 | g4-> r8 g8 aes4-> r4 | g4-> r4 aes4-> r4 | g2-> r2 | R1*4 | }
closTbnTwo = { R1*8 | es4->\ff r8 es8 f4-> r4 | es4-> r8 es8 f4-> r4 | es4-> r4 f4-> r4 | es2-> r2 | R1*4 | }
closBassTbn = { R1*8 | es,4->\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }
closTuba = { R1*8 | es,4->\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | R1*4 | }
closTimp = { R1*7 | es4\f r4 r2 | es4->\ff r8 es8 r2 | es4-> r8 es8 r2 | es4-> r4 r2 | es2-> r2 | R1*4 | }
closVla = { es'8(\f g' bes' g') es'8( g' bes' g') | f'8( aes' bes' aes') es'8( g' bes' g') | d'8( f' bes' f') d'8( f' aes' f') | es'8( g' bes' g') es'4 r4 | <bes es'>2\f <aes d'>2 | <g c'>2 <f bes>2 | <es aes>2 <f bes>2 | <es bes>2-> r2 | <es' bes'>4->\ff r8 <es' bes'>8 <f' bes'>4-> r4 | <es' bes'>4-> r8 <es' bes'>8 <f' bes'>4-> r4 | <es' bes'>4-> r4 <d' bes'>4-> r4 | <es' bes'>2-> r2 | bes1\>( | bes1) | bes1\p~ | bes2. r4 | }
closVc = { es4\f g4 bes4 g4 | aes4 f4 g4 es4 | bes,4 d4 f4 aes4 | es2 r2 | g2\f f2 | es2 d2 | c2 bes,2 | es2-> r2 | es4->\ff r8 es8 d4-> r4 | es4-> r8 es8 d4-> r4 | es4-> r4 bes,4-> r4 | es2-> r2 | es1\>~ | es1 | c1\p~ | c2. r4 | }
closCb = { es,4\f g,4 bes,4 g,4 | aes,4 f,4 g,4 es,4 | bes,,4 d,4 f,4 aes,4 | es,2 r2 | g,2\f f,2 | es,2 d,2 | c,2 bes,,2 | es,2-> r2 | es,4->\ff r8 es,8 bes,,4-> r4 | es,4-> r8 es,8 bes,,4-> r4 | es,4-> r4 bes,,4-> r4 | es,2-> r2 | es,1\>~ | es,1 | c,1\p~ | c,2. r4 | }

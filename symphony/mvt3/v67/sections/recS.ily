\version "2.24.0"
% SECOND THEME IN THE RECAPITULATION, bars 171-198. 171-186: theme F2 in C minor, muted trumpet 1 in unison with the cor anglais
% (cyclic-notes 'Owed' item 1: on a repeat, a muted trumpet doubling the cor anglais); oboe 1 doubles the climax in unison and flute 1 at the octave (181-183, c011, as flute 1 at 61-63).
% Accompaniment as at 51. Deceptive cadence at 186 (V - VI): the C-major statement starts from A flat.
% 187-198: theme F2 in C major in the violins with the cellos' counter-melody (as at 67, a minor third lower); its consequent turns
% to E flat over A flat (mixture, 198), and the coda's C-minor tutti follows. Movement I's withheld sounds stay for the coda.

% c032 (harmony; A&S PDF 283): 177 Cl 2 C4 on beat 3 (was F3: F-G under the solo's C-D, parallel 5ths into V at 178).
% c041 (Adler ch. 7, PDF 185-186, 201, 205): 181-183 Fl 1 at the unison (was G6, the shrill register), Ob 1 rests (a unison oboe overshadowed the cor anglais, whose G5 = written D6 is its thin, pinched register); the climax keeps cor anglais + muted trumpet with flute colour.
% c058 (expression; Sebesky ch. 1, PDF 12-13 economy): 195-198 clarinets rest as at 75-78 (c047): they doubled Hn 1-2 at the unison, pp under the horns' p.
recSFluteOne = { R1*10 | r2 r4 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods \once \override Staff.Hairpin.minimum-length = #7 d''4(\p\< | g''4\mf f''4\> es''4 d''4) | c''2.(\p bes'4) | R1*3 | R1*10 | c'''2.(\p\< d'''4 | es'''1)\f | }
recSOboeOne = { R1*26 | c''2.(\p\< d''4 | es''1)\f | }
recSCorAnglais = { g'2.(\p^\markup \italic "dolce cantabile" es'4 | d'4 c'4 es'4 g'4 | d''2 c''4 bes'4 | aes'2 g'2) \breathe | f'2.( aes'4 | g'4 f'4 es'4 d'4 | es'2 c'2 | d'1) \breathe | g'2.( es'4 | d'4 c'4 es'4 g'4\< | c''2. d''4 | g''4\mf f''4\> es''4 d''4) \breathe | c''2.(\p bes'4 | aes'4 g'4 f'4 es'4 | d'2 b2 | c'1) | R1*12 | }
recSClOne = { c'1\pp | b2 c'2 | c'1 | c'1 | c'1 | b1 | c'1 | b2. r4 | c'1 | b2 c'2 | c'1 | c'2 b2 | c'1 | c'2 b2 | g1 | aes1 | R1*12 | }
recSClTwo = { es1\pp | f2 es2 | f1 | f2 es2 | f1 | g2 f2 | es2 c'2 | g2 f2 | es1 | f2 es2 | es2 f2 | es2 g4 r4 | es1 | f1 | g2 f2 | es1 | R1*12 | }
% c035 (Gould PDF 65): 195 and 197 Bn 1 and Bn 2 exchange notes (C/E, C-C/E-F) so Bn 1 stays the upper part; same sound.
recSBsnOne = { c1\pp | b,2 c2 | c1 | c1 | c1 | b,1 | c1 | b,1 | c1 | b,2 c2 | c1 | c2 b,4 r4 | c1 | c2 b,2 | b,2 g,2 | aes,1 | c1\p | b,2 c2 | a,1 | a,2 c4 r4 | a,1 | b,1 | c2 a,2 | b,2. r4 | e1 | d2 c2 | e2 f2 | es2. r4 | }
recSBsnTwo = { R1*16 | c1\p | b,2 c2 | a,1 | f,2 e,2 | d,1 | b,1 | c2 a,2 | g,1 | c1 | b,2 c2 | c2 c2 | aes,1 | }
% c059 (holistic, Tchaikovsky 4/iv; Adler part 1 PDF 238 Schubert: each thematic element scored differently; PDF 255: the third time, alter the scoring; PDF 267 Brahms 1/ii and
% PDF 270 Copland: one wind quietly doubling a string line): 187-194 Hn 1 p dolce doubles Vln II (the tune's lower octave), so the C-major statement is no longer scored exactly as 67-74.
recSHnOne = { R1*16 | g'2.(\p^\markup \italic "dolce" e'4) | d'4( c'4 e'4 g'4) | d''2( c''4 b'4) | a'2( g'2) \breathe | f'2.( a'4) | g'4( f'4 e'4 d'4) | e'2( c'2) | d'1 | c'1\p | d'2 c'2 | e'2 f'2 | es'1 | }
recSHnTwo = { R1*16 | R1*8 | g1\p | g2 g2 | c'2 a2 | aes1 | }
recSTptOne = { g'2.(\p^\markup \italic "con sord., dolce cantabile" es'4 | d'4 c'4 es'4 g'4 | d''2 c''4 bes'4 | aes'2 g'2) \breathe | f'2.( aes'4 | g'4 f'4 es'4 d'4 | es'2 c'2 | d'1) \breathe | g'2.( es'4 | d'4 c'4 es'4 g'4\< | c''2. d''4 | g''4\mf f''4\> es''4 d''4) \breathe | c''2.(\p bes'4 | aes'4 g'4 f'4 es'4 | d'2 b2 | c'1) | R1*12 | }
% c063 (form; Adler II PDF 263-264, 267: a colour kept back stays fresh, Mozart keeps the orchestral horns and flutes silent while a soloist of that kind plays;
% PDF 261-262: roles exchanged): the harp's only texture in the movement is broken-chord eighths under a major-mode cantabile (67, 123, 187, 235); 187-198 were 67-78 again,
% harp included. The harp rests at 187-198, so its fourth use, under the owed C-major second-theme head at 235, comes after 104 bars of silence; the eighth-note motion
% moves to the minor half (violas 171-186).
recSHarpR = { R1*16 | R1*12 | }
recSHarpL = { R1*16 | R1*12 | }
recSVlnOne = { R1*16 | g''2.(\mf^\markup \italic "arco, cantabile" e''4) | d''4( c''4 e''4 g''4) | d'''2( c'''4 b''4) | a''2( g''2) | f''2.( a''4) | g''4( f''4 e''4 d''4) | e''2( c''2) | d''1 | g''2.( e''4) | d''4( c''4 e''4 g''4)\< | c'''2. d'''4\upbow | es'''1\f\downbow | }
% c063 (form, the recapitulation's second hearing; Adler ch. 17, PDF 257-258 dialogue with a changed answering colour, PDF 267 the orchestra reduced when the solo lies in its soft register,
% PDF 274 accompaniment kept registrally distant from a woodwind solo, PDF 288 Haydn changes the doubling on the repeat): 171-186 Vln II rest (their pizz. C4-F4 lay inside the cor anglais's low fifth,
% B3-F4); the solo sounds above violas, cellos, basses and the low wood-wind pad only, so the C-minor statement no longer repeats 51-66's background a third lower, and Vln II's arco entry at 187 is a fresh colour.
recSVlnTwo = { R1*16 | g'2.(\mf^\markup \italic "arco" e'4) | d'4( c'4 e'4 g'4) | d''2( c''4 b'4) | a'2( g'2) | f'2.( a'4) | g'4( f'4 e'4 d'4) | e'2( c'2) | d'1^\markup \italic "sul G" | g'2.(^\markup \italic "ord." e'4) | d'4( c'4 e'4 g'4)\< | c''2. d''4\upbow | es''1\f\downbow | }
% c063 (form; Adler II PDF 288, Haydn: on a repeat the scoring changes, "devices like these add great variety"; PDF 269-270, Sibelius VC and Bartok PC 3: a soft,
% rhythmically independent weaving background under the solo; PDF 259-260): 171-186 were 51-66 transposed in every accompanying part. The violas now weave arco sul tasto pp
% eighths on the same dyads (E flat3-A flat3, an octave and more below the cor anglais and muted trumpet), so the recapitulated second theme keeps the movement's eighth-note
% motion and is not a copy of 51; 187 'ord.' (they are already arco and unis.).
recSVla = { es8(\pp^\markup \italic "sul tasto" g es g) es8( g es g) | d8( f d f) es8( g es g) | f8( aes f aes) f8( aes f aes) | f8( aes f aes) es8( g es g) | d8( f d f) d8( f d f) | d8( g d g) d8( f d f) | es8( g es g) f8( c' f c') | d8( g d g) d8( f d f) | es8( g es g) es8( g es g) | d8( f d f) es8( g es g) | es8( g es g) d8( f d f) | es8( f es f) d8( g d g) | es8( c' es c') es8( c' es c') | f8( aes f aes) d8( f d f) | d8( g d g) d8( f d f) | aes8( c' aes c') r2 | e2(\mf^\markup \italic "ord., espress." f4 g4) | f2( e2) | f4( g4 a2) | a4( b4 c'2) | f2( a4 c'4) | b2( f2) | e2( g4 f4) | f4( e4 d4 f4) | e2( f4 g4) | f2( e2) | g2( c'4 d'4) | c'1 | }
% c027 (texture; Adler II PDF 259-260): 189-190 counter-melody as at 69-70, F-G-A | A-B-C (no octaves with the tune's C-B-A-G). 186 Cl 1 A flat3 below the solo's C4 (was E flat4 above it; Adler II PDF 274).
% c051 (Sebesky PDF 208, Ex. 273): 194 Vc/Vla F-E-D-F under the tune's held D (as 74), the 7th resolving to E at 195.
recSVc = { c4\pp^\markup \italic "pizz." r4 r2 | b,4 r4 c4 r4 | aes,4 r4 r2 | f,4 r4 es,4 r4 | d,4 r4 r2 | g,4 r4 r2 | c4 r4 aes,4 r4 | g,4 r4 r2 | es,4 r4 r2 | b,4 r4 c4 r4 | es,4 r4 f,4 r4 | f,4 r4 g,4 r4 | aes,4 r4 r2 | f,4 r4 g,4 r4 | g,4 r4 r2 | aes,4 r4 r2 | e2(\mf^\markup \italic "arco, espress." f4 g4) | f2( e2) | f4( g4 a2) | a4( b4 c'2) | f2( a4 c'4) | b2( f2) | e2( g4 f4) | f4( e4 d4 f4) | e2( f4 g4) | f2( e2) | g2( c'4 d'4) | c'1 | }
recSCb = { c,4\pp^\markup \italic "pizz." r4 r2 | b,,4 r4 c,4 r4 | aes,,4 r4 r2 | f,,4 r4 es,4 r4 | d,4 r4 r2 | g,,4 r4 r2 | c,4 r4 aes,,4 r4 | g,,4 r4 r2 | es,4 r4 r2 | b,,4 r4 c,4 r4 | es,4 r4 f,,4 r4 | f,,4 r4 g,,4 r4 | aes,,4 r4 r2 | f,,4 r4 g,,4 r4 | g,,4 r4 r2 | aes,,4 r4 r2 | c,1\mf^\markup \italic "arco" | b,,2 c,2 | a,,1 | f,,2 e,,2 | d,1 | b,,1 | c,2 a,,2 | g,,1 | e,1 | b,,2 c,2 | e,2 f,2 | aes,,1 | }

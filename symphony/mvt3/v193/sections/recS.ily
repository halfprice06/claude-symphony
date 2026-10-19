\version "2.24.0"
% c126: Cl 2 and Bsn 1 breathe after 178 with the solo's breath (pp pads 171-182).
% SECOND THEME IN THE RECAPITULATION, bars 171-198. 171-186: theme F2 in C minor, muted trumpet 1 in unison with the cor anglais
% (cyclic-notes 'Owed' item 1: on a repeat, a muted trumpet doubling the cor anglais); oboe 1 doubles the climax in unison and flute 1 at the octave (181-183, c011, as flute 1 at 61-63).
% Accompaniment as at 51. Deceptive cadence at 186 (V - VI): the C-major statement starts from A flat.
% 187-198: theme F2 in C major in the violins with the cellos' counter-melody (as at 67, a minor third lower); its consequent turns
% to E flat over A flat (mixture, 198), and the coda's C-minor tutti follows. Movement I's withheld sounds stay for the coda.
% c073 (form; A&S PDF 95, Ex. 6-4: a tonic's meaning depends on its function; the C-major tonic belongs to the arrival at 223 and the cadence at 263):
% 187-197 are transposed into A flat major (\transpose c aes,), the key that the deceptive cadence at 186 opens; 198 (A flat with E flat on top) is unchanged and is now
% the statement's own tonic, reached plagally (197 D flat - 198 A flat), ff into the C-minor tutti (VI - i, as before). C major, and the violas' E natural
% (they began 187 on E3, the thread pitch class), are now first heard at 219-223. Cb 190, 193-194 and violas 194 are re-voiced inside the range (Cb E1, viola C3).

% c103 (form; A&S Unit 26, PDF 448 Ex. 26-7, PDF 456 Point 4; corpus Dvorak 9/iv cadence.csv): 183 bass E flat (i6; was A flat, VI). In the exposition the cor anglais
% theme has a deceptive cadence at 63 and an authentic one at 66; the recapitulation must avoid root V-i in C, so 186 became deceptive too, and 182-183 / 185-186 were two
% identical G-A flat deceptive cadences three bars apart (with 165-166 and 204-205, four in 40 bars, all onto A flat). 183 now closes on the inverted tonic (V-i6, allowed),
% so the deceptive cadence at 186 is heard as the turn into A flat. Violas G3-C4 at 183 (were E flat3-C4: octaves G-E flat with the cellos).
% c032 (harmony; A&S PDF 283): 177 Cl 2 C4 on beat 3 (was F3: F-G under the solo's C-D, parallel 5ths into V at 178).
% c041 (Adler ch. 7, PDF 185-186, 201, 205): 181-183 Fl 1 at the unison (was G6, the shrill register), Ob 1 rests (a unison oboe overshadowed the cor anglais, whose G5 = written D6 is its thin, pinched register); the climax keeps cor anglais + muted trumpet with flute colour.
% c074 (orchestration; Adler ch. 5, PDF 135: background away from the register of a melody of similar colour): 171-180 Cl 1 rests; its C4/B3 line doubled Bn 1 an octave higher
% and met the cor anglais and muted trumpet at the unison on C4 (172, 177, 180). It re-enters at 181 under the solo's high bars.
% c074 (Adler ch. 5, PDF 127, 141, 151-152): 187-196 Vln II play the tune in unison with Vln I (they were an octave lower, down to A flat3-B flat3 on the G string, their weakest register);
% the violas, with Hn 1, take the lower octave (E flat4-A flat3, their middle strings) instead of doubling the cellos' counter-melody on the C string; the cellos carry the counter alone; violas rejoin it at 197.
% c058 (expression; Sebesky ch. 1, PDF 12-13 economy): 195-198 clarinets rest as at 75-78 (c047): they doubled Hn 1-2 at the unison, pp under the horns' p.
% c148 (expression; A&S Unit 3, PDF 53-54: 195-198 is a four-bar group whose goal is the next strong bar, 199; PDF 50: a held note's continuation is weaker than its attack): 198 the held chord (Fl 1, Ob 1, Bn, Hn 1-2, strings) crescendos f < into the ff at 199, as 82 does into 83; c068's 'full crescendo 196-198' had stopped at 198's downbeat. Bowing and the down-bow at 198 unchanged.
recSFluteOne = { R1*10 | r2 r4 \once \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods \once \override Staff.Hairpin.minimum-length = #7 d''4(\p\< | g''4\mf f''4\> es''4 d''4) | c''2.(\p bes'4) | R1*3 | R1*10 | \transpose c aes, { c'''2.(\p\< d'''4 } | es'''1)\f\< | }
% c165 (MOLA PDF 5; as c105/c135): Ob 1 rests 167-196 (30 bars) and enters p in the poco rit. at 197: Vln I cue at 195-196. The contrabassoon rests 167-198 and
% enters ff at 199 like the low brass that c105 cued: the cellos at 197-198 (\transposedCueDuring c, so its octave-up part shows them at sounding pitch). Score and MIDI unchanged.
recSOboeOne = { R1*24 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vlnOne" #UP { R1*2^\markup \tiny "Vln. I" } } | \transpose c aes, { c''2.(\p\< d''4 } | es''1)\f\< | }
recSCorAnglais = { g'2.(\p^\markup \italic "dolce cantabile" es'4 | d'4 c'4 es'4 g'4 | d''2 c''4 bes'4 | aes'2 g'2) \breathe | f'2.( aes'4 | g'4 f'4 es'4 d'4 | es'2 c'2 | d'1) \breathe | g'2.( es'4 | d'4 c'4 es'4 g'4\< | c''2. d''4 | g''4\mf f''4\> es''4 d''4) \breathe | c''2.(\p bes'4 | aes'4 g'4 f'4 es'4 | d'2 b2 | c'1) | R1*12 | }
recSClOne = { R1*10 | c'1\pp | c'2 b2 | c'1 | c'2 b2 | g1 | c'1 | R1*12 | }
recSClTwo = { es1\pp | f2 es2 | f1 | f2 es2 | f1 | g2 f2 | es2 c'2 | g4( f4 d4 f4) \breathe | g2 es2 | f2 es2 | es2 aes2~ | aes2 g4 r4 | es1 | f1 | g2 f2 | es1 | R1*12 | }
% c035 (Gould PDF 65): 195 and 197 Bn 1 and Bn 2 exchange notes (C/E, C-C/E-F) so Bn 1 stays the upper part; same sound.
% c092 (A&S PDF 83, Ex. 5-18: parallel octaves; PDF 76: the leading tone not doubled): 185-186 Bn 1 B2-D3 | C3 (was B2-G2 | A flat2) and Cl 1 G3 | C4 (was G3 | A flat3): both moved G-A flat in octaves with the bass into the deceptive cadence; VI now doubles its 3rd C.
recSBsnOne = { es2\pp c2 | b,2 c2 | c1 | c1 | c1 | b,1 | c1 | b,1 \breathe | c1 | b,2 c2 | c1 | c2 g,4 r4 | c1 | c2 b,2 | b,2 d2 | c1 | \transpose c aes, { c1\p } | \transpose c aes, { b,2 c2 } | \transpose c aes, { a,1 } | \transpose c aes, { a,2 c4 r4 } | \transpose c aes, { a,1 } | \transpose c aes, { b,1 } | \transpose c aes, { c2 a,2 } | \transpose c aes, { b,2. r4 } | \transpose c aes, { e1 } | \transpose c aes, { d2 c2 } | \transpose c aes, { e2\< f2 } | es2.\f\< r4 | }
% c164 (Adler ch. 5, PDF 135, Ex. V-26: wider intervals between the lower parts, as in the overtone series): 194 Bn 2 E flat2 then E flat3 on beats 3-4, a ninth above the Cb's D flat2 (as Bn 2's B flat2 over A flat1 at 74), not a major second above it (c163's V4/2).
recSBsnTwo = { R1*16 | \transpose c aes, { c1\p } | \transpose c aes, { b,2 c2 } | \transpose c aes, { a,1 } | \transpose c aes, { f,2 e,2 } | \transpose c aes, { d,1 } | \transpose c aes, { b,1 } | \transpose c aes, { c2 a,2 } | \transpose c aes, { g,2 g2 } | \transpose c aes, { c1 } | \transpose c aes, { b,2 c2 } | \transpose c aes, { c2\< c2 } | aes,1\f\< | }
% c059 (holistic, Tchaikovsky 4/iv; Adler part 1 PDF 238 Schubert: each thematic element scored differently; PDF 255: the third time, alter the scoring; PDF 267 Brahms 1/ii and
% PDF 270 Copland: one wind quietly doubling a string line): 187-194 Hn 1 p dolce doubles Vln II (the tune's lower octave), so the C-major statement is no longer scored exactly as 67-74.
% c092 (A&S PDF 83, PDF 87 point 7: octaves with leaps in both voices): 197 Hn 2 E flat3-F3 (was A flat3-F3: E flat3-A flat3 moved in octaves with the tune's E flat5-A flat5).
% c166 (Rimsky-Korsakov ch. I, PDF 44): Hn 1-2 breathe at the end of 198; Hn 1 played 191-204 (about 20 s, f < into the ff tutti at 199) without a rest.
recSHnOne = { R1*16 | \transpose c aes, { g'2.(\p^\markup \italic "dolce" e'4) } | \transpose c aes, { d'4(\< c'4 e'4 g'4) } | \transpose c aes, { d''2(\> c''4 b'4) } | \transpose c aes, { a'2(\! g'2) \breathe } | \transpose c aes, { f'2.( a'4) } | \transpose c aes, { g'4( f'4 e'4 d'4) } | \transpose c aes, { e'2( c'2) } | \transpose c aes, { d'1 } | \transpose c aes, { c'1\p } | \transpose c aes, { d'2 c'2 } | \transpose c aes, { e'2\< f'2 } | es'1\f\< \breathe | }
recSHnTwo = { R1*16 | R1*8 | \transpose c aes, { g1\p } | \transpose c aes, { g2 g2 } | \transpose c aes, { g2\< a2 } | aes1\f\< \breathe | }
% c075 (MOLA PDF 5, Example 5): the mute comes off in the rest at 187; "senza sord." stays at 199
recSTptOne = { g'2.(\p^\markup \italic "con sord., dolce cantabile" es'4 | d'4 c'4 es'4 g'4 | d''2 c''4 bes'4 | aes'2 g'2) \breathe | f'2.( aes'4 | g'4 f'4 es'4 d'4 | es'2 c'2 | d'1) \breathe | g'2.( es'4 | d'4 c'4 es'4 g'4\< | c''2. d''4 | g''4\mf f''4\> es''4 d''4) \breathe | c''2.(\p bes'4 | aes'4 g'4 f'4 es'4 | d'2 b2 | c'1) | R1*12^\markup \italic "togli sord." | }
% c063 (form; Adler II PDF 263-264, 267: a colour kept back stays fresh, Mozart keeps the orchestral horns and flutes silent while a soloist of that kind plays;
% PDF 261-262: roles exchanged): the harp's only texture in the movement is broken-chord eighths under a major-mode cantabile (67, 123, 187, 235); 187-198 were 67-78 again,
% harp included. The harp rests at 187-198, so its fourth use, under the owed C-major second-theme head at 235, comes after 104 bars of silence; the eighth-note motion
% moves to the minor half (violas 171-186).
recSHarpR = { R1*16 | R1*12 | }
recSHarpL = { R1*16 | R1*12 | }
% c138 (expression; Casanelles ch. 4, PDF 151 and 155: a lyrical string legato swells into the note of arrival; PDF 150, 152: the expressive crescendo and diminuendo are what notation must ask for): 188-190 a swell < > into the phrase's peak at 189 in Vln I-II, violas and Hn 1, as the cor anglais's statement has at 180-182; same at 68-70 (sTwo.ily).
% c165 (as at 67; c065): no "arco" for the violins at 187. Vln I never plays pizz. in the movement, Vln II last plucked at 115-122 and has bowed since 127.
recSVlnOne = { R1*16 | \transpose c aes, { g''2.(\mf^\markup \italic "cantabile" e''4) } | \transpose c aes, { d''4(\< c''4 e''4 g''4) } | \transpose c aes, { d'''2(\> c'''4 b''4) } | \transpose c aes, { a''2(\! g''2) } | \transpose c aes, { f''2.( a''4) } | \transpose c aes, { g''4( f''4 e''4 d''4) } | \transpose c aes, { e''2( c''2) } | \transpose c aes, { d''1 } | \transpose c aes, { g''2.( e''4) } | \transpose c aes, { d''4( c''4 e''4 g''4)\< } | \transpose c aes, { c'''2. d'''4\upbow } | es'''1\f\<\downbow | }
% c063 (form, the recapitulation's second hearing; Adler ch. 17, PDF 257-258 dialogue with a changed answering colour, PDF 267 the orchestra reduced when the solo lies in its soft register,
% PDF 274 accompaniment kept registrally distant from a woodwind solo, PDF 288 Haydn changes the doubling on the repeat): 171-186 Vln II rest (their pizz. C4-F4 lay inside the cor anglais's low fifth,
% B3-F4); the solo sounds above violas, cellos, basses and the low wood-wind pad only, so the C-minor statement no longer repeats 51-66's background a third lower, and Vln II's arco entry at 187 is a fresh colour.
recSVlnTwo = { R1*16 | \transpose c aes, { g''2.(\mf^\markup \italic \override #'(baseline-skip . 2.3) \column { "cantabile" "unis. with Vln I" } e''4) } | \transpose c aes, { d''4(\< c''4 e''4 g''4) } | \transpose c aes, { d'''2(\> c'''4 b''4) } | \transpose c aes, { a''2(\! g''2) } | \transpose c aes, { f''2.( a''4) } | \transpose c aes, { g''4( f''4 e''4 d''4) } | \transpose c aes, { e''2( c''2) } | \transpose c aes, { d''1 } | \transpose c aes, { g''2.( e''4) } | \transpose c aes, { d''4( c''4 e''4 g''4)\< } | \transpose c aes, { c''2. d''4\upbow } | es''1\f\<\downbow | }
% c063 (form; Adler II PDF 288, Haydn: on a repeat the scoring changes, "devices like these add great variety"; PDF 269-270, Sibelius VC and Bartok PC 3: a soft,
% rhythmically independent weaving background under the solo; PDF 259-260): 171-186 were 51-66 transposed in every accompanying part. The violas now weave arco sul tasto pp
% eighths on the same dyads (E flat3-A flat3, an octave and more below the cor anglais and muted trumpet), so the recapitulated second theme keeps the movement's eighth-note
% motion and is not a copy of 51; 187 'ord.' (they are already arco and unis.).
% c067 (texture; Sebesky ch. 3, PDF 142 Ex. 202: sul tasto to natural sound adds body at the climax; PDF 144 Ex. 194): 181-182 the violas play ord. p < mp > under the solo's peak, sul tasto pp again from 183.
% c114 (balance; Rimsky-Korsakov PDF 51: in soft passages one string section = one wind; c094/c098 set 67's counter-melody and bass mp under the mf tune): 187 violas, cellos and basses mp (were mf, level with the tune in Vln I+II unison), crescendo 196, mf 197, f 198 as before.
recSVla = { es8(\pp^\markup \italic "sul tasto" g es g) es8( g es g) | d8( f d f) es8( g es g) | f8( aes f aes) f8( aes f aes) | f8( aes f aes) es8( g es g) | d8( f d f) d8( f d f) | d8( g d g) d8( f d f) | es8( g es g) f8( c' f c') | d8( g d g) d8( f d f) | es8( g es g) es8( g es g) | d8( f d f) es8( g es g) | es8(\p\<^\markup \italic "ord." g es g) d8( f d f) | es8(\mp aes es aes)\> d8( g d g) | g8(\pp^\markup \italic "sul tasto" c' g c') g8( c' g c') | f8( aes f aes) d8( f d f) | d8( g d g) d8( f d f) | aes8( c' aes c') r2 | \transpose c aes, { g'2.(\mp^\markup \italic "ord., espress." e'4) } | \transpose c aes, { d'4(\< c'4 e'4 g'4) } | \transpose c aes, { d''2(\> c''4 b'4) } | \transpose c aes, { a'2(\! g'2) } | \transpose c aes, { f'2.( a'4) } | \transpose c aes, { g'4( f'4 e'4 d'4) } | \transpose c aes, { e'2( c'2) } | \transpose c aes, { d'1 } | \transpose c aes, { g'2.( e'4) } | \transpose c aes, { d'4(\< c'4 e'4 g'4) } | \transpose c aes, { g2(\mf\< a2) } | c'1\f\< | }
% c027 (texture; Adler II PDF 259-260): 189-190 counter-melody as at 69-70, F-G-A | A-B-C (no octaves with the tune's C-B-A-G). 186 Cl 1 A flat3 below the solo's C4 (was E flat4 above it; Adler II PDF 274).
% c051 (Sebesky PDF 208, Ex. 273): 194 Vc/Vla F-E-D-F under the tune's held D (as 74), the 7th resolving to E at 195.
% c097: 190-193 the cellos' counter-melody follows the change at 70-73 (sTwo.ily): C-D-E | C-A-C | B-F | G-A-G in the C template, in sixths and tenths under the tune instead of octaves.
% c121 (Adler ch. 3, PDF 99: the cello's G string is the least strong and carries less well; PDF 91 Ex. III-39: violas and cellos coupled on a counter-line):
% 187 the cellos carry the counter-melody alone (the violas left it for the tune's lower octave at c074), starting C3-E flat3 on the G string, so they play mf with
% the tune instead of mp (c114's mp assumed a counter in two sections, as at 67); they hold mf to 196 and crescendo from 197 to f at 198.
% c137 (texture; Adler ch. 16, PDF 230-231: the countertheme keeps its own line; A&S PDF 83 octaves; as c092 for Hn 2 at 197): 197 beats 3-4 violas and cellos F3 (were A flat 3-B flat 3 in octaves with the tune's A flat-B flat in Vln I-II);
% the counter-melody rises E flat-F-A flat under the tune (no octaves with the basses' D flat-A flat either) instead of joining it.
recSVc = { c4\pp^\markup \italic "pizz." r4 r2 | b,4 r4 c4 r4 | aes,4 r4 r2 | f,4 r4 es,4 r4 | d,4 r4 r2 | b,4 r4 r2 | c4 r4 aes,4 r4 | g,4 r4 r2 | es,4 r4 r2 | b,4 r4 c4 r4 | es,4 r4 f,4 r4 | f,4 r4 g,4 r4 | es,4 r4 r2 | f,4 r4 g,4 r4 | g,4 r4 r2 | aes,4 r4 r2 | \transpose c aes, { e2(\mf^\markup \italic "arco, espress." f4 g4) } | \transpose c aes, { f2( e2) } | \transpose c aes, { f4( g4 a2) } | \transpose c aes, { c'4( d'4 e'2) } | \transpose c aes, { c'2( a4 c'4) } | \transpose c aes, { b2( f2) } | \transpose c aes, { g2( a4 g4) } | \transpose c aes, { f4( e4 d2) } | \transpose c aes, { e2( f4 g4) } | \transpose c aes, { f2( e2) } | \transpose c aes, { g2(\< a2) } | c'1\f\< | }
recSCb = { c,4\pp^\markup \italic "pizz." r4 r2 | b,,4 r4 c,4 r4 | aes,,4 r4 r2 | f,,4 r4 es,4 r4 | d,4 r4 r2 | b,,4 r4 r2 | c,4 r4 aes,,4 r4 | g,,4 r4 r2 | es,4 r4 r2 | b,,4 r4 c,4 r4 | es,4 r4 f,,4 r4 | f,,4 r4 g,,4 r4 | es,4 r4 r2 | f,,4 r4 g,,4 r4 | g,,4 r4 r2 | aes,,4 r4 r2 | \transpose c aes, { c,1\mp^\markup \italic "arco" } | \transpose c aes, { b,,2 c,2 } | \transpose c aes, { a,,1 } | des,2 c,2 | \transpose c aes, { d,1 } | \transpose c aes, { b,,1 } | aes,,2 f,2 | es,2 des,2 | \transpose c aes, { e,1 } | \transpose c aes, { b,,2\< c,2 } | \transpose c aes, { e,2\mf\< f,2 } | aes,,1\f\< | }

% c105 (MOLA PDF 5: logical cues are expected during long rests, audible and obvious, in the reading key): part-only cues (tag 'part) in 197-198 for the
% brass and timpani that enter ff/f at N (199) after 32 bars of rest (31 for the timpani) through L, M and a poco rit.: Vln I's climb to E flat 6 f for the
% trumpets and horns (horns an octave lower, \transposedCueDuring, so the cue stays on the stave), the cellos' line for the trombones, tuba and timpani.
% c135 (MOLA PDF 5: logical cues during long periods of rest; Example 4, PDF 10): Ob 2 rests 167-198 (32 bars, through the Poco meno mosso, M and the poco rit.) and enters ff at 199 with no cue,
% while the brass with 28 bars of rest have one (c105). Part-only cue of Ob 1, its stand partner, at 197-198. Score and MIDI unchanged.
recSOboeTwo = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "oboeOne" #UP { R1*2^\markup \tiny "Ob. 1" } } | }
recSTptTwo = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vlnOne" #UP { R1*2^\markup \tiny "Vln. I" } } | }
recSTptThree = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vlnOne" #UP { R1*2^\markup \tiny "Vln. I" } } | }
recSHnThree = { R1*26 | \tag #'score { R1*2 } \tag #'part { \transposedCueDuring "vlnOne" #UP c { R1*2^\markup \tiny "Vln. I" } } | }
recSHnFour = { R1*26 | \tag #'score { R1*2 } \tag #'part { \transposedCueDuring "vlnOne" #UP c { R1*2^\markup \tiny "Vln. I" } } | }
recSCbsn = { R1*26 | \tag #'score { R1*2 } \tag #'part { \transposedCueDuring "vc" #UP c { R1*2^\markup \tiny "Vc." } } | }
recSTbnOne = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vc" #UP { R1*2^\markup \tiny "Vc." } } | }
recSTbnTwo = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vc" #UP { R1*2^\markup \tiny "Vc." } } | }
recSBassTbn = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vc" #UP { R1*2^\markup \tiny "Vc." } } | }
recSTuba = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vc" #UP { R1*2^\markup \tiny "Vc." } } | }
recSTimp = { R1*26 | \tag #'score { R1*2 } \tag #'part { \cueDuring "vc" #UP { R1*2^\markup \tiny "Vc." } } | }

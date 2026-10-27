\version "2.24.0"
% c303 (form; Rimsky-Korsakov ch. IV, PDF 130: 'Diminuendo effects are accomplished by the elimination of the instruments in the reverse order (brass, wood-wind, strings)';
%   PDF 127: 'the transition from a complex to a simple timbre, by the suppression of one of the groups, belongs essentially to the diminuendo'; PDF 116: whether a passage is a complement to or a contrast with what comes after):
%   234, the last chord of the plagal close, is the seam between the coda's first stage (brass chorale) and its second (movement I's second theme in the strings, p, at 235). The brass, timpani and woodwinds no longer
%   hold and release with the strings on 234 beat 3 at one level: brass and timpani resolve on 234 beat 1 (quarter, p), woodwinds on beats 1-2 (half, mp), strings keep the dotted half (mf) with the violins' pickup,
%   so the chorale group leaves first and the strings that carry 235 are the last group sounding, as at 39-42, 133-134 and 167-170. Pitches, chords, the 233 diminuendo and 235 unchanged; every chord tone of 234 stays in strings and woodwinds.
% c182 (A&S Unit 5, PDF 81-82: no dissonant leaps): 225 Bn 2 C3 and Cbsn C2 (octave up), so 226-227 go B-A by step (were B1-A2 and B0-A1, rising sevenths forced by the range).
% c126 (Adler PDF 230): Cbsn breath after 228 (226-230 low register, B0-C1).
% THE C-MAJOR ARRIVAL AND CHORALE, bars 223-234 (c020: bar numbers updated from v01), Maestoso (cyclic-notes 'Owed' items 2-4). 223: trumpet 1's B rises to C, coupled with
% the timpani; the stop chord of 222 resolves; the first sustained forte major chord in full brass; string tremolo and the violins' C7 here
% and only here; crash cymbals, no tam-tam. 224-228: the brass chorale, the motto in major G-E-D-C-D flat-C, trombone colour with horns
% and trumpets, independent bass C-C-B-A-F (cyclic-notes, mvt I critic 160); c002: 227 A minor - augmented triad A-D flat-F - F (no 5ths E-F over A-B flat, A&S PDF 83). 226-230: the violins (with flutes, oboes, clarinets)
% in canon two bars after the brass. 229-230: movement I's timpani pulse c4 r8 g,8 c4 r4 between the phrases. 231-234: plagal close over
% the C pedal with mixture (IV - I - iv - I); no root-position V-I in C before the last cadence (262-263).

% c028: 224 the timpani's release stroke is f with the chorale (it inherited fff); 234 the diminuendo's mf sits on the last chord, not on the rest after it
% c029 (Rimsky-Korsakov PDF 82, 100): 224 Hn 3-4 C4 (were G3, E3): the brass chord in close order with no gap between G3 and E4, the third no longer doubled below the alto
% c036 (Adler PDF 230: give the contrabassoon periodic rests; PDF 198/175 double reeds): Bn 1-2 and Cbn rest 231-234 (they had played every bar since 211); the C pedal stays in tuba, bass trombone, cellos, basses. 223 B.cl C3 (PDF 216: low C is risky).
% c042 (harmony; A&S PDF 377, 394): 226 Fl 2 and Ob 2 G (were E: an unprepared, unresolved second against the chorale's D in Tpt 1, Hn 2-3, Tbn 1, Cl 2); 227 second half Fl 2/Ob 2 A and Cl 2 F
% (were C and E held against the brass's D flat and F: C sounded with the motto's chromatic D flat in the same octave). The canon line itself (Vln, Fl 1, Ob 1, Cl 1) is unchanged.
% c136 (playability; Adler ch. 9, PDF 292: in a loud slow passage not too many notes on one breath): breath after the fff arrival chord 223, before the chorale's f entry at 224, in Tpt 1-2, Hn 1-4, Tbn 1-2 (B.tbn and tuba already breathe after 225). No note, rhythm or dynamic changed; 222->223 untouched.
arrivalTptOne = { c''1\fff \breathe | g'1\f | e''1 | d''1 | c''2 des''2 | c''1 | R1 | c''1\f | a'1 | g'1 | aes'1\> | g'4\p r2. | }
arrivalTptTwo = { g'1\fff \breathe | e'1\f | c''1 | g'1 | a'1 | a'1 | R1 | g'1\f | f'1 | e'1 | f'1\> | e'4\p r2. | }
arrivalTptThree = { e'1\fff | R1*11 | }
arrivalHnOne = { c''1\fff \breathe | g'1\f | g'1 | g'1 | e'2 f'2 | f'1 | R1 | e'1\f | f'1 | e'1 | f'1\> | e'4\p r2. | }
arrivalHnTwo = { g'1\fff \breathe | e'1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'4\p r2. | }
arrivalHnThree = { e'1\fff \breathe | c'1\f | c'1 | d'1 | a1 | a1 | R1 | g1\f | a1 | g1 | aes1\> | g4\p r2. | }
arrivalHnFour = { c'1\fff \breathe | c'1\f | g1 | g1 | e2 f2 | f1 | R1 | e1\f | f1 | e1 | f1\> | e4\p r2. | }
arrivalTbnOne = { g1\fff \breathe | g1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'4\p r2. | }
% c244 (orchestration; Adler ch. 11, adler2 PDF 38-41, Ex. XI-21, Tchaikovsky 4/i 285-290: the cantus firmus of the climactic tutti is given to the tenor trombones a2 in unison;
%   PDF 15: above mf two horns equal one trumpet or trombone, so Tbn 1 alone with Hn 2 was 1-1.5 units on the motto against Tpt 2 + Hn 1 on the inner G4/C5; Ex. XI-1, PDF 15-16, and c029: no low third under the alto):
%   224-228 Tbn 2 doubles Tbn 1 on the major motto at movement I's pitch (G3-E4-D4-C4-D flat 4-C4); its old notes are kept by Hn 4 (G3 226, E3/F3 227, F3 228) and Hn 3 (C4 225), and its E3 at 224,
%   the doubled third below the alto that c029 removed from the horns, is dropped. Top line, Tbn 1, bass, canon and dynamics unchanged; no layer added (c159).
arrivalTbnTwo = { e1\fff \breathe | g1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | g1\f | f1 | g1 | f1\> | e4\p r2. | }
arrivalBassTbn = { c1\fff | c1\f | c1 \breathe | b,1 | a,1 | f,1 | R1 | c1\f | c1 | c1 | c1\> | c4\p r2. | }
arrivalTuba = { c,1\fff | c,1\f | c,1 \breathe | b,,1 | a,,1 | f,,1 | R1 | c,1\f | c,1 | c,1 | c,1\> | c,4\p r2. | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
% c146 (Adler ch. 12, PDF 55 and 84, Piston: "a fortissimo for the timpani doubled by bass drum" leaves nothing else audible; ch. 14, PDF 141: a loud bass drum can obliterate the tutti): 223 the timpani roll starts fff and diminishes to the f of 224, and the bass drum strikes ff, so the string tremolo, the violins' C7 and the violas' E4 sound through the arrival chord; the crash stays fff.
arrivalTimp = { c1:32\fff\> | c4\f r4 r2 | R1*4 | c4\f r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\f~ | c1:32~ | c1:32\>~ | c4:32\p r2. | }
arrivalPerc = \drummode { << { \tweak style #'xcircle cymc1^\fff } \\ { bd1_\ff } >> | R1*11 | }
% c335 (Gould, Behind Bars PDF 62-64, 66: a second between two parts displaces the lower part, and each accidental stands beside its own notehead): at 229.3 the flat of Fl 2's B flat5 printed before Fl 1's C6 and read as C flat6, and the heads touched; score-only force-hshift puts B flat5 with its flat on the left, C6 to its right
arrivalFluteOne = { c''''1\fff | R1*2 | g''1~\ff | g''2 e'''2~ | e'''2 d'''2~ | d'''2 \tag #'score { \once \override NoteColumn.force-hshift = #1.2 } c'''4 des'''4 | c'''1 \breathe | a''1\f | g''1 | aes''1\> | g''2\mp r2 | }
arrivalFluteTwo = { g'''1\fff | R1*2 | g''1~\ff | g''2 a''2 | a''1 | a''2 \tag #'score { \once \override NoteColumn.force-hshift = #0 } bes''2 | a''1 \breathe | a''1\f | g''1 | aes''1\> | g''2\mp r2 | }
arrivalOboeOne = { c'''1\fff | R1*2 | g''1~\ff | g''2 e'''2~ | e'''2 d'''2~ | d'''2 c'''4 des'''4 | c'''1 \breathe | c''1\f | c''1 | c''1\> | c''2\mp r2 | }
% c044 (orchestration; Adler ch. 15, PDF 169: two ideas separate when scored in opposing timbres and designs; PDF 159 no. 2, register for the dynamic; PDF 165): 226-228 Ob 2 and Cl 2 an octave higher, under the wood-wind/string canon instead of at pitch inside the brass chorale (Ob 2 G4 = Tpt 2/Hn 1, Cl 2 D4-F4 = Hn 1-3/Tbn 1). Pitch classes unchanged; 229 both return to their octave when the brass rest (Cl 2 F5-E5 over Ob 2 B flat4-A4 would be fifths at 229-230).
arrivalOboeTwo = { g''1\fff | R1*2 | g''1~\ff | g''2 a''2 | a''1 | a'2 bes'2 | a'1 \breathe | a'1\f | g'1 | aes'1\> | g'2\mp r2 | }
arrivalClOne = { e'''1\fff | R1*2 | g''1~\ff | g''2 e'''2~ | e'''2 d'''2~ | d'''2 c'''4 des'''4 | c'''1 \breathe | f''1\f | e''1 | f''1\> | e''2\mp r2 | }
arrivalClTwo = { c'''1\fff | R1*2 | d''1\ff | e''2 f''2 | a''1 | g'2. f'4 | e'1 \breathe | c''1\f | c''1 | c''1\> | c''2\mp r2 | }
arrivalBassCl = { c1\fff | R1*11 | }
% c154 (orchestration; Adler ch. 11, PDF 15-16: the timpani are coupled with the brass on the harmony's own tones; movement I 179-180, the model of the 229-230 pulse, puts it over the C pedal): 229 Bn 1-2, Cbsn, Vc, Cb hold C (were E-B flat): the timpani's f C on beat 3 struck a ninth over the B flat-minor half bar in the one bar the brass rest. Canon, top line and timpani unchanged.
% c156 (playability; Adler adler1 PDF 230: low notes take considerable breath, give periodic rests): Bn 1-2 breathe after 228 with the contrabassoon (226-230 were five bars, about 21 s at 2 = 56, on one breath at f)
arrivalBsnOne = { c1\fff | c1\f | c1 \breathe | b,1 | a,1 | f1 \breathe | c1 | c1 | R1*4 | }
arrivalBsnTwo = { c,1\fff | c,1\f | c1 \breathe | b,1 | a,1 | f,1 \breathe | c,1 | c,1 | R1*4 | }
arrivalCbsn = { c,,1\fff | c,,1\f | c,1 \breathe | b,,1 | a,,1 | f,,1 \breathe | c,,1 | c,,1 | R1*4 | }
% c027 (texture; Adler II PDF 273-274, 283): 226-230 the canon's lower octave (Ob 1, Cl 1, Vln II) is moved up to the canon's upper octave, so it no longer crosses above the chorale's top line (Tpt 1 C-D flat-C, 227-228).
% c115 (Gould PDF 47: keep a phrase at one octave; ledger lines, not octave signs, for isolated notes in parts; strings read up to five ledger lines): 223 C7 without 8va,
% so the run G6-A flat6-B6 of 222 is seen to rise a step into C7 (the 8va showed it as a falling seventh to written C6), as Fl 1 at 223 and Vln I at 222;
% stem up, so the three tremolo strokes stand above the note, clear of the five ledger lines
% c149 (Bruckner 4/iv coda: string figuration kept under the brass chorale; Rimsky PDF 131: a sustained part between converging groups guarantees unity; PDF 133, Ex. 264: the harmonic basis in a different timbre and octave from the melody; PDF 141, Ex. 281: strings tremolo under the brass at the climax): 224-225 Vln I C6 and Vln II E5-G5 keep the arrival tremolo mf under the chorale's first two bars, so the texture does not drop to a mid-register brass block between the fff chord and the canon at 226. No C7, no chorale or canon note changed.
% c243 (form and pacing; Adler ch. 17, adler2 PDF 263-264: Dvorak and Tchaikovsky introduce the string soloist after a contrasting colour, 'the solo colour is therefore very fresh';
%   PDF 267: Mozart keeps the soloist's own colour out of the accompaniment; PDF 268-269, Sibelius: the entry is couched in a sparse texture; this score's own 171-186 -> 187, violins rest before their F2):
%   231-234 Vln I rests after the canon's last C6 (230) and re-enters only with the pickup G4 to the S head (234.4, mf), so the coda's third stage (235) starts in a colour that has not
%   sounded for 8 s. The top line A5-G5-A flat 5-G5 that Vln I doubled is taken by Fl 2 a2 with Fl 1 (Fl 2's F5-E5 stays in Cl 1 and Vln II); harmony, Vln II pulse, dynamics unchanged.
%   The harp part's cue before 235 now quotes Vln II.
% c331 (melody; A&S Unit 21, PDF 346-347 sec. 1-2 and Ex. 21-1, Mozart 41/iv bars 9-12 (corpus Mozart_Sym41_mvt4.ly: r2 c2~ | c2 b2 | r2 d2~ | d2 c2): a line in tied halves, displaced by half a bar
%   against a whole-note subject, makes suspensions and is a counterpoint in its own right, 'rhythm rather than melody'; PDF 350-351 sec. 9 (7-6), PDF 351 sec. 10 (9-8 with the 6th held); PDF 348 sec. 3 (resolution down by step)):
%   226-230 the canon (Vln I-II, Fl 1, Ob 1, Cl 1) keeps its entry on G5 at 226 but each later note arrives half a bar late, tied over the barline: G5 held over vi (227, the 7 of vi7),
%   E6 held over IV (228, 7-6 to D6), D6 held over the C bass (229, 9-8 to C6), then C-D flat in quarters so the line is back on C6 at 230 (the D flat stays on the B flat-minor half bar, not on 230's C-major brass chord).
%   227 first half Fl 2 and Ob 2 tie their G5 with the canon (they had C6, above the held G5; E5 made octaves with Hn 1 and the violas G-E). 229 Cl 2 holds G4 to beat 4 (g'2. f'4), so Cl 1's 9-8 D6-C6 makes no fifths with it.
%   The held D6 also removes the fifths D6/A3 -> C6/G3 that Vln I-II and the violas made at 228->229 (A&S PDF 365-366 sec. 27: suspensions turn parallel motion into oblique). Brass chorale, its top line, bass, violas, dynamics and 223 unchanged.
arrivalVlnOne = { \once \override Stem.direction = #UP c''''1:32\fff | c'''1:32\mf | c'''1:32 | g''1~\ff\cbaw | g''2 e'''2~ | e'''2 d'''2~ | d'''2 c'''4 des'''4 | c'''1 | R1*3 | r2. g'4(\mf | }
% c100 (cyclic lens; A&S Unit 23, PDF 388: flat 6 is active toward 5 and moves to it; Unit 29, PDF 503: the augmented-sixth tones resolve by half step): 223 Vln II upper takes G5 (was C6).
%   222's Vln II D5-A flat 5 is movement I's stop-chord layout at its bar 138, where that A flat 5 is never resolved; at the arrival it now falls A flat 5 -> G5 at pitch,
%   as Tpt 1 B4 -> C5 (movement I's last trumpet B4) and the violas' F4 -> E4 resolve their stop-chord tones at pitch. Lower desk D5 -> E5 unchanged.
% c154 (orchestration; Adler ch. 11, PDF 14: the brass easily overshadow the rest; PDF 15: at f a single horn is half a trumpet, so the middle register is full; Ex. XI-1, PDF 15-16): 231-233 Vln II takes the violas' portato quarters on its own F5-E5-F5, above the f brass (top Tpt 1 A4-G4-A flat 4), so the pulse c153 gave the violas (A3-G3-A flat 3, at the unison with Hn 3 and inside Hn 4, Tbn 1-2) is heard until the harp's eighths at 235. Pitches, harmony and dynamics unchanged.
arrivalVlnTwo = { <e'' g''>1:32\fff | <e'' g''>1:32\mf | <e'' g''>1:32 | g''1~\ff\cbawU | g''2 e'''2~ | e'''2 d'''2~ | d'''2 c'''4 des'''4 | c'''1 | f''4--(\f f''4-- f''4-- f''4--) | e''4--( e''4-- e''4-- e''4--) | f''4--(\> f''4-- f''4-- f''4--) | e''2.\mf g'4( | }
% c080 (cyclic; A&S Unit 28, PDF 491: over a cadential 6/4 the tonic note is passing, not a goal; it becomes a goal only when V moves on to I): 223 lower violas E4 (was G4).
%   The violas' E4 at 220 lies over the cadential 6/4 and moves on to F4 at 221; the thread's goal is the tonic at 223, where the violas now sound E4, movement I's last viola pitch (I 182, on C major), with E5 above. Lower viola D4 -> E4 by step.
% c081 (melody/voice leading; A&S Unit 3, PDF 54: dissonances arise from and resolve by stepwise motion; Unit 22, PDF 377: vii°7's dissonances resolve normally): 223 violas unis. E4 (was <e' e''>): the upper violas take the stop chord's F4 down a step to E4, the only F->E resolution in its own octave (it leapt F4->E5); the lower violas keep D4->E4, so both desks hold the thread pitch E4 on the tonic.
% c153 (form/pacing; Adler ch. 17, PDF 259-260: the background keeps a rhythm of its own; PDF 288, Orff: an accompaniment figure gives rhythmic support without covering; ch. 15, PDF 192: the seams of a hand-over must not show): 231-233 the violas restart their 224-228 portato quarters on their plagal-close notes (A3, G3, A flat 3; pitches, harmony and the f > mf unchanged), so the four whole-note bars at 2 = 56 keep the pulse that the timpani carry at 229-230 until the harp's eighths take it at 235.
% c159 (Adler PDF 142-144, 154): 231-233 violas hold A3-G3-A flat 3 (v149); the portato pulse stays in Vln II alone.
arrivalVla = { e'1:32\fff^\markup \italic "unis." | e'4--(\f e'4-- e'4-- e'4--) | c'4--( c'4-- c'4-- c'4--) | g4--( g4-- g4-- g4--) | e4--( e4-- f4-- f4--) | a4--( a4-- a4-- a4--) | g2 bes2 | g1 | a1\f | g1 | aes1\> | g2.\mf r4 | }
% c085 (Adler ch. 2, PDF 30): 223 cellos 'div.' on the tremolo C3-G3 (each desk one note); 224 'unis., change bow at will'.
% c325 (Adler part 2 PDF 301, proofreading; Gould PDF 41): in the narrow whole-note bar 224 "change bow" ran 0.5 mm across the barline of 225 (Vc, Cb); the text starts half a space earlier, centred between the barlines
arrivalVc = { <c g>1:32\fff^\markup \italic "div." | c1\f-\tweak X-offset #-0.5 \cbawU | c1 | b,1 | a,1 | f1 | c1 | c1 | c1 | c1 | c1\> | c2.\mf r4 | }
arrivalCb = { c,1:32\fff | c,1\f-\tweak X-offset #-0.5 \cbaw | c,1 | b,,1 | a,,1 | f,1 | c,1 | c,1 | c,1 | c,1 | c,1\> | c,2.\mf r4 | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); Vln I 231-234 before the harp's entry at 235, after 152 bars
arrivalHarpR = { R1*8 | \tag #'score { R1*4 } \tag #'part { \cueDuring "vlnTwo" #DOWN { R1*4^\markup \tiny "Vln. II" } } | }

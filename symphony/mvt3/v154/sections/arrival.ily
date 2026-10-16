\version "2.24.0"
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
arrivalTptOne = { c''1\fff \breathe | g'1\f | e''1 | d''1 | c''2 des''2 | c''1 | R1 | c''1\f | a'1 | g'1 | aes'1\> | g'2.\mf r4 | }
arrivalTptTwo = { g'1\fff \breathe | e'1\f | c''1 | g'1 | a'1 | a'1 | R1 | g'1\f | f'1 | e'1 | f'1\> | e'2.\mf r4 | }
arrivalTptThree = { e'1\fff | R1*11 | }
arrivalHnOne = { c''1\fff \breathe | g'1\f | g'1 | g'1 | e'2 f'2 | f'1 | R1 | e'1\f | f'1 | e'1 | f'1\> | e'2.\mf r4 | }
arrivalHnTwo = { g'1\fff \breathe | e'1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2.\mf r4 | }
arrivalHnThree = { e'1\fff \breathe | c'1\f | c'1 | d'1 | a1 | a1 | R1 | g1\f | a1 | g1 | aes1\> | g2.\mf r4 | }
arrivalHnFour = { c'1\fff \breathe | c'1\f | g1 | g1 | e2 f2 | f1 | R1 | e1\f | f1 | e1 | f1\> | e2.\mf r4 | }
arrivalTbnOne = { g1\fff \breathe | g1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2.\mf r4 | }
arrivalTbnTwo = { e1\fff \breathe | e1\f | c'1 | g1 | e2 f2 | f1 | R1 | g1\f | f1 | g1 | f1\> | e2.\mf r4 | }
arrivalBassTbn = { c1\fff | c1\f | c1 \breathe | b,1 | a,1 | f,1 | R1 | c1\f | c1 | c1 | c1\> | c2.\mf r4 | }
arrivalTuba = { c,1\fff | c,1\f | c,1 \breathe | b,,1 | a,,1 | f,,1 | R1 | c,1\f | c,1 | c,1 | c,1\> | c,2.\mf r4 | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
% c146 (Adler ch. 12, PDF 55 and 84, Piston: "a fortissimo for the timpani doubled by bass drum" leaves nothing else audible; ch. 14, PDF 141: a loud bass drum can obliterate the tutti): 223 the timpani roll starts fff and diminishes to the f of 224, and the bass drum strikes ff, so the string tremolo, the violins' C7 and the violas' E4 sound through the arrival chord; the crash stays fff.
arrivalTimp = { c1:32\fff\> | c4\f r4 r2 | R1*4 | c4\f r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\f~ | c1:32~ | c1:32\>~ | c2.:32\mf r4 | }
arrivalPerc = \drummode { << { \tweak style #'xcircle cymc1^\fff } \\ { bd1_\ff } >> | R1*11 | }
arrivalFluteOne = { c''''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 \breathe | a''1\f | g''1 | aes''1\> | g''2.\mf r4 | }
arrivalFluteTwo = { g'''1\fff | R1*2 | g''1\ff | c'''2 a''2 | a''1 | a''2 bes''2 | a''1 \breathe | f''1\f | e''1 | f''1\> | e''2.\mf r4 | }
arrivalOboeOne = { c'''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 \breathe | c''1\f | c''1 | c''1\> | c''2.\mf r4 | }
% c044 (orchestration; Adler ch. 15, PDF 169: two ideas separate when scored in opposing timbres and designs; PDF 159 no. 2, register for the dynamic; PDF 165): 226-228 Ob 2 and Cl 2 an octave higher, under the wood-wind/string canon instead of at pitch inside the brass chorale (Ob 2 G4 = Tpt 2/Hn 1, Cl 2 D4-F4 = Hn 1-3/Tbn 1). Pitch classes unchanged; 229 both return to their octave when the brass rest (Cl 2 F5-E5 over Ob 2 B flat4-A4 would be fifths at 229-230).
arrivalOboeTwo = { g''1\fff | R1*2 | g''1\ff | c'''2 a''2 | a''1 | a'2 bes'2 | a'1 \breathe | a'1\f | g'1 | aes'1\> | g'2.\mf r4 | }
arrivalClOne = { e'''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 \breathe | f''1\f | e''1 | f''1\> | e''2.\mf r4 | }
arrivalClTwo = { c'''1\fff | R1*2 | d''1\ff | e''2 f''2 | a''1 | g'2 f'2 | e'1 \breathe | c''1\f | c''1 | c''1\> | c''2.\mf r4 | }
arrivalBassCl = { c1\fff | R1*11 | }
arrivalBsnOne = { c1\fff | c1\f | c1 \breathe | b,1 | a,1 | f1 | e2 bes,2 | c1 | R1*4 | }
arrivalBsnTwo = { c,1\fff | c,1\f | c,1 \breathe | b,,1 | a,1 | f,1 | e,2 bes,,2 | c,1 | R1*4 | }
arrivalCbsn = { c,,1\fff | c,,1\f | c,,1 \breathe | b,,,1 | a,,1 | f,,1 \breathe | e,,2 bes,,2 | c,,1 | R1*4 | }
% c027 (texture; Adler II PDF 273-274, 283): 226-230 the canon's lower octave (Ob 1, Cl 1, Vln II) is moved up to the canon's upper octave, so it no longer crosses above the chorale's top line (Tpt 1 C-D flat-C, 227-228).
% c115 (Gould PDF 47: keep a phrase at one octave; ledger lines, not octave signs, for isolated notes in parts; strings read up to five ledger lines): 223 C7 without 8va,
% so the run G6-A flat6-B6 of 222 is seen to rise a step into C7 (the 8va showed it as a falling seventh to written C6), as Fl 1 at 223 and Vln I at 222;
% stem up, so the three tremolo strokes stand above the note, clear of the five ledger lines
% c149 (Bruckner 4/iv coda: string figuration kept under the brass chorale; Rimsky PDF 131: a sustained part between converging groups guarantees unity; PDF 133, Ex. 264: the harmonic basis in a different timbre and octave from the melody; PDF 141, Ex. 281: strings tremolo under the brass at the climax): 224-225 Vln I C6 and Vln II E5-G5 keep the arrival tremolo mf under the chorale's first two bars, so the texture does not drop to a mid-register brass block between the fff chord and the canon at 226. No C7, no chorale or canon note changed.
arrivalVlnOne = { \once \override Stem.direction = #UP c''''1:32\fff | c'''1:32\mf | c'''1:32 | g''1\ff\cbaw | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1\f | g''1 | aes''1\> | g''2.\mf g'4( | }
% c100 (cyclic lens; A&S Unit 23, PDF 388: flat 6 is active toward 5 and moves to it; Unit 29, PDF 503: the augmented-sixth tones resolve by half step): 223 Vln II upper takes G5 (was C6).
%   222's Vln II D5-A flat 5 is movement I's stop-chord layout at its bar 138, where that A flat 5 is never resolved; at the arrival it now falls A flat 5 -> G5 at pitch,
%   as Tpt 1 B4 -> C5 (movement I's last trumpet B4) and the violas' F4 -> E4 resolve their stop-chord tones at pitch. Lower desk D5 -> E5 unchanged.
arrivalVlnTwo = { <e'' g''>1:32\fff | <e'' g''>1:32\mf | <e'' g''>1:32 | g''1\ff\cbawU | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | f''1\f | e''1 | f''1\> | e''2.\mf g'4( | }
% c080 (cyclic; A&S Unit 28, PDF 491: over a cadential 6/4 the tonic note is passing, not a goal; it becomes a goal only when V moves on to I): 223 lower violas E4 (was G4).
%   The violas' E4 at 220 lies over the cadential 6/4 and moves on to F4 at 221; the thread's goal is the tonic at 223, where the violas now sound E4, movement I's last viola pitch (I 182, on C major), with E5 above. Lower viola D4 -> E4 by step.
% c081 (melody/voice leading; A&S Unit 3, PDF 54: dissonances arise from and resolve by stepwise motion; Unit 22, PDF 377: vii°7's dissonances resolve normally): 223 violas unis. E4 (was <e' e''>): the upper violas take the stop chord's F4 down a step to E4, the only F->E resolution in its own octave (it leapt F4->E5); the lower violas keep D4->E4, so both desks hold the thread pitch E4 on the tonic.
% c153 (form/pacing; Adler ch. 17, PDF 259-260: the background keeps a rhythm of its own; PDF 288, Orff: an accompaniment figure gives rhythmic support without covering; ch. 15, PDF 192: the seams of a hand-over must not show): 231-233 the violas restart their 224-228 portato quarters on their plagal-close notes (A3, G3, A flat 3; pitches, harmony and the f > mf unchanged), so the four whole-note bars at 2 = 56 keep the pulse that the timpani carry at 229-230 until the harp's eighths take it at 235.
arrivalVla = { e'1:32\fff^\markup \italic "unis." | e'4--(\f e'4-- e'4-- e'4--) | c'4--( c'4-- c'4-- c'4--) | g4--( g4-- g4-- g4--) | e4--( e4-- f4-- f4--) | a4--( a4-- a4-- a4--) | g2\cbaw bes2 | g1 | a4--(\f a4-- a4-- a4--) | g4--( g4-- g4-- g4--) | aes4--(\> aes4-- aes4-- aes4--) | g2.\mf r4 | }
% c085 (Adler ch. 2, PDF 30): 223 cellos 'div.' on the tremolo C3-G3 (each desk one note); 224 'unis., change bow at will'.
arrivalVc = { <c g>1:32\fff^\markup \italic "div." | c1\f\cbawU | c1 | b,1 | a,1 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\> | c2.\mf r4 | }
arrivalCb = { c,1:32\fff | c,1\f\cbaw | c,1 | b,,1 | a,,1 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\> | c,2.\mf r4 | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); Vln I 231-234 before the harp's entry at 235, after 152 bars
arrivalHarpR = { R1*8 | \tag #'score { R1*4 } \tag #'part { \cueDuring "vlnOne" #DOWN { R1*4^\markup \tiny "Vln. I" } } | }

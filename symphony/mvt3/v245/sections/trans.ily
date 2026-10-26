\version "2.24.0"
% TRANSITION, bars 43-50, over the B flat pedal (V of E flat), p to pp, poco rit. at 49-50.
% The intro's turn figure (motive x, bars 3-4) passes from flute 1 to clarinet 1 to oboe 1, each time darker:
% G flat (45) and C flat (47) bring in E flat minor before the second theme (call and response between solo winds over held strings).
% c052 (harmony; A&S Unit 24, PDF 413-414: neighbours over a held bass return; PDF 439: do not double the 7th): 49-50 violas hold C flat as a 9-8 suspension and fall to B flat on beat 3 of 49 (a direct C flat-B flat with Vln II's G flat-F would be parallel fifths), Vln II F4 (G flat falls back to F), so the V7 of E flat is complete and its 7th is not tripled.
% c093 (A&S Unit 14, PDF 214 and 220): 43 the figure's lower neighbour is A flat (the 7th of V7 of E flat, held by Bn 1), not A natural, which tonicized B flat against the held A flat; as the same figure at 89.
transFluteOne = { r4 f''8(\p es''8 d''8 c''8 bes'8 aes'8 | bes'8 c''8 d''8 es''8 f''4) r4 | R1*6 | }
% c228 (expression; Adler ch. 15, adler2 PDF 190-191, 'Coloring a Note', Ex. XV-37: a held pp pitch passed from one wind to another, the second entering under the first;
% PDF 190, Ex. XV-36: the two must overlap; PDF 192: at a change of colour the seams must not show): Bn 1 held the seventh A flat3 for eight bars and re-attacked it at 47
% (with the oboe's entry) and 49 (with Hn 1's D4). Now Bn 1 holds it tied 43-47.2 and Cl 2 takes the same A flat3 pp at 47, under Bn 1, to 50.3, then resolves it to G flat3 at 51
% in its own part. Same pitch, same harmony; no re-attack on the held seventh.
transClOne = { R1*2 | r4 bes'8(\p aes'8 ges'8 f'8 es'8 d'8 | es'8 f'8 ges'8 aes'8 bes'4) r4 | \partCombineSoloII R1*4 \partCombineAutomatic | }
transClTwo = { R1*4 | aes1\pp~ | aes1~ | aes1~ | aes2. r4 | }
transOboeOne = { R1*4 | r4 ges''8(\p f''8 es''8 des''8 ces''8 bes'8 | aes'2 ges'2) | aes'1\pp~ | aes'2. r4 | }
transBsnOne = { aes1\pp~ | aes1~ | aes1~ | aes1~ | aes2 r2 | R1*3 | }
transHnOne = { R1*6 | d'1\pp~ | d'2. r4 | }
transVlnTwo = { f'1\pp~ | f'1~ | f'1~ | f'2 d'2 | ges'1~ | ges'1 | f'1~ | f'2. r4 | }
transVla = { d'1\pp~ | d'1~ | d'1~ | d'2 c'2 | ces'1~ | ces'1~ | ces'2 bes2~ | bes2. r4 | }
transVc = { bes,1\pp~\cbaw | bes,1~ | bes,1~ | bes,1~ | bes,1~ | bes,1~ | bes,1~ | bes,2. r4 | }
transCb = { bes,,1\pp~\cbaw | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,2. r4 | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); Ob. 1 at 47-48 before the trumpet solo at 51, after 50 bars of rest
transTptOne = { R1*4 | \tag #'score { R1*2 } \tag #'part { \cueDuring "oboeOne" #UP { R1*2^\markup \tiny "Ob. 1" } } | R1*2 | }
% c206 (playability; Adler ch. 4, PDF 116: harp harmonics are bell-like, very soft, "must be accompanied very lightly", best written between C3 and A5 and notated an octave below the sound with a circle; PDF 112: show the starting pedal setting): the harp's first sound is three single harmonics B flat (written B flat 3, sounding B flat 4) p on beat 1 of 43, 45 and 47, under the pp held strings and before each wind's motive-x run starts on beat 2, so the transition's 2+2+2+2 hand-over has a soft chime on its pedal tone. Movement II (83) and the scherzo (375) use harp harmonics; the finale had none. The pedal setting is already the E flat major setting of 67, so no change is needed before 67. MIDI: \harmOctF plays the sounding octave, softly (as the scherzo's \harmOct).
harmOctF = #(define-music-function (m) (ly:music?) #{ \set PianoStaff.midiMaximumVolume = #0.6 \transposition c'' #m \transposition c' \set PianoStaff.midiMaximumVolume = #1.0 #})
transHarpR = { R1*8 | }
transHarpL = { \harmOctF { bes4-\flageolet\p -\tag #'score ^\markup \small \harp-pedal #"--^|^--^" -\tag #'part ^\markup \small "Ped.: D C B♭ / E♭ F G A♭" ^\markup \small \italic "harm. (sound 8va)" } r4 r2 | R1 | \harmOctF { bes4-\flageolet } r4 r2 | R1 | \harmOctF { bes4-\flageolet } r4 r2 | R1*3 | }

\version "2.24.0"
% TRANSITION, bars 43-50, over the B flat pedal (V of E flat), p to pp, poco rit. at 49-50.
% The intro's turn figure (motive x, bars 3-4) passes from flute 1 to clarinet 1 to oboe 1, each time darker:
% G flat (45) and C flat (47) bring in E flat minor before the second theme (call and response between solo winds over held strings).
% c052 (harmony; A&S Unit 24, PDF 413-414: neighbours over a held bass return; PDF 439: do not double the 7th): 49-50 violas hold C flat as a 9-8 suspension and fall to B flat on beat 3 of 49 (a direct C flat-B flat with Vln II's G flat-F would be parallel fifths), Vln II F4 (G flat falls back to F), so the V7 of E flat is complete and its 7th is not tripled.
% c093 (A&S Unit 14, PDF 214 and 220): 43 the figure's lower neighbour is A flat (the 7th of V7 of E flat, held by Bn 1), not A natural, which tonicized B flat against the held A flat; as the same figure at 89.
% c278 (expression; Adler ch. 7, adler1 PDF 186 Ex. VII-4 (Brahms 4/iv flute: a crescendo on each rising half-figure, mp < >), PDF 227 Ex. VII-93
%   (Tchaikovsky 6/i bassoon: every figure of a solo wind line carries its own hairpin), PDF 185 Ex. VII-2, PDF 198 Ex. VII-32, PDF 210 Ex. VII-56 (register colours)):
%   43-48 the three solo statements of the scale figure (bars 3-4; "motive x" in older comments) were one flat p. Fl 1 (44) and Cl 1 (46) now swell on the rising half of the figure into its top note;
%   Ob 1, the darkest and last, has a diminuendo on its two closing halves (48) into the pp it holds at 49. Notes, slurs and levels otherwise unchanged.
transFluteOne = { r4 f''8(\p es''8 d''8 c''8 bes'8 aes'8 | bes'8\< c''8 d''8 es''8 f''4)\! r4 | R1*6 | }
% c228 (expression; Adler ch. 15, adler2 PDF 190-191, 'Coloring a Note', Ex. XV-37: a held pp pitch passed from one wind to another, the second entering under the first;
% PDF 190, Ex. XV-36: the two must overlap; PDF 192: at a change of colour the seams must not show): Bn 1 held the seventh A flat3 for eight bars and re-attacked it at 47
% (with the oboe's entry) and 49 (with Hn 1's D4). Now Bn 1 holds it tied 43-47.2 and Cl 2 takes the same A flat3 pp at 47, under Bn 1, to 50.3, then resolves it to G flat3 at 51
% in its own part. Same pitch, same harmony; no re-attack on the held seventh.
transClOne = { R1*2 | r4 bes'8(\p aes'8 ges'8 f'8 es'8 d'8 | es'8\< f'8 ges'8 aes'8 bes'4)\! r4 | \partCombineSoloII R1*4 \partCombineAutomatic | }
transClTwo = { R1*4 | aes1\pp~ | aes1~ | aes1~ | aes2. r4 | }
transOboeOne = { R1*4 | r4 ges''8(\p f''8 es''8 des''8 ces''8 bes'8 | aes'2\> ges'2) | aes'1\pp~ | aes'2. r4 | }
transBsnOne = { aes1\pp~ | aes1~ | aes1~ | aes1~ | aes2 r2 | R1*3 | }
% c247 (Rimsky-Korsakov ch. III, PDF 107 and 110, Ex. 164: stopped horn notes resemble the oboe and cor anglais, and stopped horns may share one chord with them, p or sfp;
%   PDF 107: middle notes of a stopped horn over a low clarinet give 'a beautiful dark tone'; Adler PDF 308: stopped horn for single notes and soft passages):
%   49-50 Hn 1's D4 under Ob 1's A flat4 and over Cl 2's A flat3 is stopped (+), p (a stopped p is about an open pp), so the transition's last chord takes the darker E flat-minor colour
%   and the trumpet's open solo at 51 is the first open brass melody after it. Pitch, rhythm and the other parts unchanged.
transHnOne = { R1*6 | d'1\p-\stopped~ | d'2. r4 | }
% c264 (Casanelles, Hyperorchestra ch. 6, PDF 271-273, Fig. 6.1, Mahler 1/i 17-25: before the distant trumpets the dominant pedal is spread over the whole range, pp, up to the violins' highest octave;
%   PDF 259 and 274: a chord built as a harmonic spectrum (instrumental synthesis); Rimsky-Korsakov PDF 85: chords follow the harmonic scale and the harmonic notes must not be lacking in the upper parts;
%   Casanelles PDF 269-270, 275-276: the harp harmonic gives the attack the pp sul tasto entry lacks, the violins give the chime its sustain):
%   43-50 Vln I hold B flat5 pp (sul tasto until v276; an artificial harmonic since c276), the 16th partial of the basses' B flat1, over Vla D4 (5th), Vln II F4 (6th), harp B flat4 (8th) and, at 49, Ob 1 A flat4 (7th),
%   so the transition's dominant sounds as one spectrum from B flat1 to B flat5 and the motive-x runs (top G flat5) move inside it. Released with the others on 50 beat 4; Vln I re-enter ord. at 67.
% c276 (playability; Adler ch. 2, adler1 PDF 66-67, Ex. II-72, II-73, II-75: an artificial harmonic is a stopped note with the node a fourth above touched, sounding two octaves above
%   the stopped note, "the same flutey, silvery sound as the natural harmonics"; written as the stopped note with a diamond a fourth above, the sounding note added; low ones are secure;
%   PDF 46: the harmonic isolates one overtone of the string): 43-50 Vln I play B flat5 as an artificial harmonic on the G string (B flat3 stopped with the first finger in 2nd position,
%   E flat4 touched with the fourth), pp, instead of sul tasto. c264's 16th partial of the basses' B flat1 is now itself a harmonic, without vibrato, an octave above the harp's harmonic
%   B flat4 (43, 45, 47); Dvorak 9/i 91-98 (corpus, mutopia Sym9 strings.notesA.ily: Vln I hold a harmonic ppp under the solo winds' second theme) and Mahler 1/i 1-25 (c264's model,
%   violins in harmonics) do the same. The printed voice is silent in the MIDI; a voice without engravers plays the sounding B flat5. Same pitch, rhythm and dynamic as v276.
transVlnOne = { << \new Voice \with { \remove "Note_performer" } { <bes~ es'\harmonic~ \tweak font-size #-2 \parenthesize bes''>1\pp^\markup \italic "harm."\cbaw | <bes es'\harmonic>1~ | <bes es'\harmonic>1~ | <bes es'\harmonic>1~ | <bes es'\harmonic>1~ | <bes es'\harmonic>1~ | <bes es'\harmonic>1~ | <bes es'\harmonic>2. r4 }
  \new Voice \with { \remove "Note_heads_engraver" \remove "Stem_engraver" \remove "Tie_engraver" \remove "Rest_engraver" \remove "Dots_engraver" \remove "Dynamic_engraver" \remove "Script_engraver" \remove "Text_engraver" \remove "Beam_engraver" } { bes''1\pp~ | bes''1~ | bes''1~ | bes''1~ | bes''1~ | bes''1~ | bes''1~ | bes''2. r4 } >> | }
transVlnTwo = { f'1\pp~ | f'1~ | f'1~ | f'2 d'2 | ges'1~ | ges'1 | f'1~ | f'2. r4 | }
transVla = { d'1\pp~ | d'1~ | d'1~ | d'2 c'2 | ces'1~ | ces'1~ | ces'2 bes2~ | bes2. r4 | }
% c267 (texture; Sebesky ch. 3, PDF 140 rule 7: the lowest cello need not double the bass, and a distance between cello and bass lets the strings "float";
%   PDF 147: a gap of a seventh between the low voices "would have diluted the sonority"; PDF 145-146: the second cello adds a chord tone for richness, not to reinforce the bass;
%   PDF 139 note 2: the basses do not hold a line alone, so half the cellos keep B flat2): 43-50 the cellos divide, B flat2 under F3, so the V7 over the B flat pedal
%   has its fifth in the low-middle register (the gap B flat2-A flat3 was a minor seventh) and F3 is the third partial of the basses' B flat1 under c264's B flat5.
transVc = { <bes, f>1\pp^\markup \italic "div."~\cbaw | <bes, f>1~ | <bes, f>1~ | <bes, f>1~ | <bes, f>1~ | <bes, f>1~ | <bes, f>1~ | <bes, f>2. r4 | }
transCb = { bes,,1\pp~\cbaw | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,1~ | bes,,2. r4 | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); Ob. 1 at 47-48 before the trumpet solo at 51, after 50 bars of rest
transTptOne = { R1*4 | \tag #'score { R1*2 } \tag #'part { \cueDuring "oboeOne" #UP { R1*2^\markup \tiny "Ob. 1" } } | R1*2 | }
% c206 (playability; Adler ch. 4, PDF 116: harp harmonics are bell-like, very soft, "must be accompanied very lightly", best written between C3 and A5 and notated an octave below the sound with a circle; PDF 112: show the starting pedal setting): the harp's first sound is three single harmonics B flat (written B flat 3, sounding B flat 4) p on beat 1 of 43, 45 and 47, under the pp held strings and before each wind's motive-x run starts on beat 2, so the transition's 2+2+2+2 hand-over has a soft chime on its pedal tone. Movement II (83) and the scherzo (375) use harp harmonics; the finale had none. The pedal setting is already the E flat major setting of 67, so no change is needed before 67. MIDI: \harmOctF plays the sounding octave, softly (as the scherzo's \harmOct).
harmOctF = #(define-music-function (m) (ly:music?) #{ \set PianoStaff.midiMaximumVolume = #0.6 \transposition c'' #m \transposition c' \set PianoStaff.midiMaximumVolume = #1.0 #})
transHarpR = { R1*8 | }
transHarpL = { \harmOctF { bes4-\flageolet\p -\tag #'score ^\markup \small \harp-pedal #"--^|^--^" -\tag #'part ^\markup \small "Ped.: D C B♭ / E♭ F G A♭" ^\markup \small \italic "harm. (sound 8va)" } r4 r2 | R1 | \harmOctF { bes4-\flageolet } r4 r2 | R1 | \harmOctF { bes4-\flageolet } r4 r2 | R1*3 | }

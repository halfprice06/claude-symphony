\version "2.24.0"
% MOVEMENT I'S SECOND THEME IN C MAJOR, bars 235-246 (cyclic-notes 'Owed' item 5): the violins' singing statement of the falling
% major head with its pickup (234) and the chromatic counter (clarinet 1 and violas), molto cantabile, over the C pedal (basses, timpani);
% movement I withheld it (its §2 item 1). 239-242: a continuation to A6, flutes and oboe with the violins.
% 243-246: movement I's horn call in major, E-C-B-C, in trumpets 1-2 with horns 1-2 two octaves below (cyclic-notes 'Owed' item 8);
% G pedal, then V4/3 (D bass), stringendo into the Più allegro.
% c020 (bars 235-246): 241-243 bass D-F-E-G: ii (241) - II6/5 (242) - III# (E major, 243 first half) - V (cadential 6/4, 243 b3 to 246) - I (247).
% The major-third cycle of movements I and II (C - A flat - F flat/E) closes inside C major: I (235) - III# - V (A&S PDF 395 points 5b and 6:
% III# in the arpeggiation I-III#-V, approached by II6 so that G does not move straight to G sharp; A&S PDF 456 Ex. 26-9 and PDF 463 point 7:
% I-tonicized III-V in major). The trumpets' and horns' E of the horn call is the root of the E-major chord; Vln I (lower divisi) has the only G sharp
% and takes it to G in the same voice (A&S PDF 394: no split cross relation, no doubled chromatic tone); the timpani (no E) wait for the G. Replaces c003's V6/5 of V at 242, which had the same aim (no I6 before the 6/4).

% c030 (cyclic lens; themes-mvt1.ly mvtOneThemeSCmajor, invariant 4 | 2.~ 8 8 | 4 2 4): 246 beat 4 Hn 2, Cl 1 and violas give the brass statement of
% movement I's second-theme head at 247 its pickup G3, so it opens with the rising sixth G-E of movement I bar 146 (Hn 1 + Vla at G3), as the violins' statement does at 234-235.
% c032 (harmony; A&S Unit 17, PDF 266-267, 276-277): 239-240 the Cl 1 + viola counter is movement I's own C-B-B flat | A (as at 235-236), a third under the tune (was A-G sharp-G | F: D-C over G-F, parallel 5ths with the tune); 240 Hn 3 F4 (was C4: E-C over the bass A-F, 5ths); 236 Bn 1 A3 (was F3: G-F under the tune's D-C, 5ths).
% c056 (playability; Adler part 1 PDF 30: without "div." a chord is played as a double stop): 243-245 violins marked div., unis. at the run in 245 (Vln II C4-E5 at 243 is a tenth across non-adjacent strings, impossible as a double stop).
sHeadVlnOne = { \once \override TextSpanner.bound-details.left.text = \markup \italic "sul A" e''2.~(\startTextSpan e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 f''8 a''8) | c'''2( b''2)\stopTextSpan | e'''2.~(\f^\markup \italic "ord." e'''8 d'''8) | c'''4( a'''2-- g'''4) | f'''4.( e'''8 d'''4 c'''4) | d'''2( c'''2) | <gis' e''>2\<^\markup \italic "div." <g' e''>2 | <g' e''>4 <g' d''>2. | <d' b'>2 r8 g''8(^\markup \italic "unis." a'' b'' | \once \override Beam.positions = #'(-0.25 . 0.25) c'''8 d''' e''' f''' g'''2)\! | }
sHeadVlnTwo = { \once \override TextSpanner.bound-details.left.text = \markup \italic "sul A" e''2.~(\startTextSpan e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 f''8 a''8) | c'''2( b''2)\stopTextSpan | e''2.~(\f^\markup \italic "ord." e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 c''4) | d''2( c''2) | <e' b'>2\<^\markup \italic "div." <c' e''>2 | <c' g'>4 <b g'>2. | <b f'>2 r8 g'8(^\markup \italic "unis." a' b' | c''8 d'' e'' f'' g''2)\! | }
sHeadClOne = { r4 c''4(\p b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 c''4(\mf b'4 bes'4 | a'2) a'2~( | a'4 g'4 f'2 | c'2 d'2) | b2\< c'2 | g'1 | f'1 | f'2. g4\! | }
sHeadVla = { r4 c''4(\p b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2) | g'2( f'2) | r4 c''4(\mf b'4 bes'4 | a'2) a'2~( | a'4 g'4 f'2) | c'2( d'2) | b2\< c'2 | g1 | f2 r8 g8( a b | c'8 d' e' f' g'4) g4\! | }
sHeadFluteOne = { R1*4 | e'''2.~(\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | d'''2 c'''2) | R1*2 | r2 r8 g''8(\f a'' b'' | \once \override Beam.positions = #'(-0.25 . 0.25) c'''8 d''' e''' f''' g'''2) | }
sHeadOboeOne = { R1*4 | e''2.~(\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | d''2 c''2) | b'2 r2 | R1*3 | }
% c049 (Rimsky-Korsakov PDF 138-139: under a soft cantabile line, strings doubled by wood-wind and wood-wind doubled by horns are the combinations that cover it; reduce the
% sustaining parts): 235-238 Bn 1-2 rest (Bn 2 doubled the cellos, Bn 1 the horns' G-A-A-G); the harmony stays complete in Hn 3-4, cellos, basses and harp; they enter f at 239.
sHeadVc = { c1\p | c1 | d2 f,2 | g,1 | a,1\f | f,1 | d1 | d,1 | e,2\< g,2 | g,1 | d1 | d1\! | }
sHeadCb = { c,1\p~\cbaw | c,1~ | c,1~ | c,1 | a,,1\f | f,,1 | d,1 | d,1 | e,2\< g,2 | g,,1 | d,1 | d,1\! | }
sHeadBsnTwo = { R1*4 | a,1\f | f,1 | d1 | d,1 | e,2\< g,2 | g,1 | d1 | d1\! | }
sHeadBsnOne = { R1*4 | c'1\f | c'1 | a1 | d'1 | b2\< c'2 | c'4 b2. | b1 | b1\! \breathe | }
sHeadHnThree = { g1\p | a1 | a1 | g1 | e'1\mf | f'1 | a1 | d'2 c'2 | b2 r2 | R1*3 | }
sHeadHnFour = { e1\p | f1 | f1 | f1 | c'1\mf | a1 | f1 | a1 | R1*4 | }
% c046 (playability; Adler PDF 292, 309, 321: a slurred phrase is one breath, brass need room to breathe): 246 Tpt 1-2 and Hn 1 end the horn call on beat 3 (were whole notes into 247, where they re-enter ff with no gap after holding C6)
% c048 (expression; A&S Unit 3, PDF 53-54: a four-bar hypermeasure leads to its goal on the next strong bar): 244-246 Tpt 1-2 and Hn 1-2 crescendo with the strings and wood-winds into ff at 247 (they held f under the others' crescendo)
sHeadTptOne = { R1*8 | e''2->(\f c'''2~ | c'''4 b''2.~\< | b''2 c'''2~ | c'''2.) r4 | }
sHeadTptTwo = { R1*8 | e'2->(\f c''2~ | c''4 b'2.~\< | b'2 c''2~ | c''2.) r4 | }
sHeadHnOne = { R1*8 | e'2->(\f c''2~ | c''4 b'2.~\< | b'2 c''2~ | c''2.) r4\! | }
sHeadHnTwo = { R1*8 | e2->(\f c'2~ | c'4 b2.~\< | b2 c'2~ | c'2.) g4\! | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
sHeadTimp = { c1:32\pp~ | c1:32~ | c1:32~ | c1:32 | R1*4 | r2 g,2:32\p\<~ | g,1:32~ | g,1:32~ | g,1:32\f | }
sHeadHarpR = { g8 c'8 e'8 g'8 g'8 e'8 c'8 g8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | g8 b8 d'8 g'8 g'8 d'8 b8 g8 | a8 c'8 e'8 a'8 a'8 e'8 c'8 a8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | a8 c'8 d'8 a'8 a'8 d'8 c'8 a8 | R1*4 | }
% c075 (MOLA PDF 5): pedal diagram score-only (tag 'score)
sHeadHarpL = { \ottava #-1 \set Staff.ottavation = #"8" c,1\p-\tag #'score ^\markup \small \harp-pedal #"---|----" | c,1 | d,1 | g,,1 | a,,1\mf | f,,1 | d,1 | d,,1 \ottava #0 | R1*4 | }

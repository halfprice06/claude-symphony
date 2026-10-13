\version "2.24.0"
% MOVEMENT I'S SECOND THEME IN C MAJOR, bars 235-246 (cyclic-notes 'Owed' item 5): the violins' singing statement of the falling
% major head with its pickup (234) and the chromatic counter (clarinet 1 and violas), molto cantabile, over the C pedal (basses, timpani);
% movement I withheld it (its §2 item 1). 239-242: a continuation to A6, flutes and oboe with the violins.
% 243-246: movement I's horn call in major, E-C-B-C, in trumpets 1-2 with horns 1-2 two octaves below (cyclic-notes 'Owed' item 8);
% G pedal, then V4/3 (D bass), stringendo into the Allegro molto.
% c020 (bars 235-246): 241-243 bass D-F-E-G: ii (241) - II6/5 (242) - III# (E major, 243 first half) - V (cadential 6/4, 243 b3 to 246) - I (247).
% The major-third cycle of movements I and II (C - A flat - F flat/E) closes inside C major: I (235) - III# - V (A&S PDF 395 points 5b and 6:
% III# in the arpeggiation I-III#-V, approached by II6 so that G does not move straight to G sharp; A&S PDF 456 Ex. 26-9 and PDF 463 point 7:
% I-tonicized III-V in major). The trumpets' and horns' E of the horn call is the root of the E-major chord; Vln I (lower divisi) has the only G sharp
% and takes it to G in the same voice (A&S PDF 394: no split cross relation, no doubled chromatic tone); the timpani (no E) wait for the G. Replaces c003's V6/5 of V at 242, which had the same aim (no I6 before the 6/4).

sHeadVlnOne = { \once \override TextSpanner.bound-details.left.text = \markup \italic "sul A" e''2.~(\startTextSpan e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 f''8 a''8) | c'''2( b''2)\stopTextSpan | e'''2.~(\f^\markup \italic "ord." e'''8 d'''8) | c'''4( a'''2-- g'''4) | f'''4.( e'''8 d'''4 c'''4) | d'''2( c'''2) | <gis' e''>2\< <g' e''>2 | <g' e''>4 <g' d''>2. | <d' b'>2 r8 g''8( a'' b'' | \once \override Beam.positions = #'(-0.25 . 0.25) c'''8 d''' e''' f''' g'''4 \once \override Beam.positions = #'(-0.25 . 0) a'''8 b''')\! | }
sHeadVlnTwo = { \once \override TextSpanner.bound-details.left.text = \markup \italic "sul A" e''2.~(\startTextSpan e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 f''8 a''8) | c'''2( b''2)\stopTextSpan | e''2.~(\f^\markup \italic "ord." e''8 d''8) | c''4( a''2-- g''4) | f''4.( e''8 d''4 c''4) | d''2( c''2) | <e' e''>2\< <c' e''>2 | <c' g'>4 <b g'>2. | <b f'>2 r8 g'8( a' b' | c''8 d'' e'' f'' g''4 a''8 b'')\! | }
sHeadClOne = { r4 c''4(\p b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 a'4(\mf gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2 | c'2 d'2) | b2\< c'2 | g'1 | f'1 | f'1\! | }
sHeadVla = { r4 c''4(\p b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2) | g'2( f'2) | r4 a'4(\mf gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2) | c'2( d'2) | b2\< c'2 | g1 | f2 r8 g8( a b | c'8 d' e' f' g'4 a'8 b')\! | }
sHeadFluteOne = { R1*4 | e'''2.~(\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | d'''2 c'''2) | R1*2 | r2 r8 g''8(\f a'' b'' | \once \override Beam.positions = #'(-0.25 . 0.25) c'''8 d''' e''' f''' g'''4 \once \override Beam.positions = #'(-0.25 . 0) a'''8 b''') | }
sHeadOboeOne = { R1*4 | e''2.~(\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | d''2 c''2) | R1*4 | }
sHeadVc = { c1\p | c1 | d2 f,2 | g,1 | a,1\f | f,1 | d1 | f,1 | e,2\< g,2 | g,1 | d1 | d1\! | }
sHeadCb = { c,1\p~^\markup \italic "change bow at will" | c,1~ | c,1~ | c,1 | a,,1\f | f,,1 | d,1 | f,,1 | e,,2\< g,,2 | g,,1 | d,1 | d,1\! | }
sHeadBsnTwo = { c1\p | c1 | d2 f,2 | g,1 | a,1\f | f,1 | d1 | f,1 | e,2\< g,2 | g,1 | d1 | d1\! | }
sHeadBsnOne = { g1\p | f1 | f2 a2 | g2 f2 | c'1\f | c'1 | a1 | d'1 | b2\< c'2 | c'4 b2. | b1 | b1\! | }
sHeadHnThree = { g1\p | a1 | a1 | g1 | e'1\mf | c'1 | a1 | c'1 | R1*4 | }
sHeadHnFour = { e1\p | f1 | f1 | f1 | c'1\mf | a1 | f1 | a1 | R1*4 | }
sHeadTptOne = { R1*8 | e''2->(\f c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1) | }
sHeadTptTwo = { R1*8 | e'2->(\f c''2~ | c''4 b'2.~ | b'2 c''2~ | c''1) | }
sHeadHnOne = { R1*8 | e'2->(\f c''2~ | c''4 b'2.~ | b'2 c''2~ | c''1) | }
sHeadHnTwo = { R1*8 | e2->(\f c'2~ | c'4 b2.~ | b2 c'2~ | c'1) | }
sHeadTimp = { c1:32\pp | c1:32 | c1:32 | c1:32 | R1*4 | r2 g,2:32\p\< | g,1:32 | g,1:32 | g,1:32\f | }
sHeadHarpR = { g8 c'8 e'8 g'8 g'8 e'8 c'8 g8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | g8 b8 d'8 g'8 g'8 d'8 b8 g8 | a8 c'8 e'8 a'8 a'8 e'8 c'8 a8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | a8 c'8 d'8 a'8 a'8 d'8 c'8 a8 | R1*4 | }
sHeadHarpL = { c,1\p^\markup \small \harp-pedal #"---|----" | c,1 | d,1 | g,,1 | a,,1\mf | f,,1 | d,1 | f,,1 | R1*4 | }

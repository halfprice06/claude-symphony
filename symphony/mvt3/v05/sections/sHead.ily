\version "2.24.0"
% MOVEMENT I'S SECOND THEME IN C MAJOR, bars 231-242 (cyclic-notes 'Owed' item 5): the violins' singing statement of the falling
% major head with its pickup (230) and the chromatic counter (clarinet 1 and violas), molto cantabile, over the C pedal (basses, timpani);
% movement I withheld it (its §2 item 1). 235-238: a continuation to A6, flutes and oboe with the violins.
% 239-242: movement I's horn call in major, E-C-B-C, in trumpets 1-2 with horns 1-2 two octaves below (cyclic-notes 'Owed' item 8);
% G pedal, then V4/3 (D bass), stringendo into the Allegro molto. c003: 237-238 bass D-F-F sharp-G (A&S PDF 215: 4-#4-5 with V6/5 of V), so 238 drives into the cadential 6/4 at 239 instead of closing on I6.

sHeadVlnOne = { e''2.~ e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2) | e'''2.~(\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | d'''2 c'''2) | <g' e''>1\< | <g' e''>1 | <d' b'>2 r8 g''8( a'' b'' | c'''8 d''' e''' f''' g'''4 a'''8 b''')\! | }
sHeadVlnTwo = { e'2.~ e'8 d'8 | c'4 a'2-- g'4 | f'4. e'8 d'4 f'8 a'8 | c''2 b'2) | e''2.~(\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | d''2 c''2) | <c' g'>1\< | <c' g'>1 | <b f'>2 r8 g'8( a' b' | c''8 d'' e'' f'' g''4 a''8 b'')\! | }
sHeadClOne = { r4 c''4(\mf b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 a'4( gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2 | c'2 d'2) | g'1\< | g'1 | f'1 | f'1\! | }
sHeadVla = { r4 c''4(\mf b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | r4 a'4( gis'4 g'4 | f'2) a'2~( | a'4 g'4 f'2 | c'2 d'2) | g1\< | g1 | f2 r8 g'8( a' b' | c''8 d'' e'' f'' g''4 a''8 b'')\! | }
sHeadFluteOne = { R1*4 | e'''2.~(\f e'''8 d'''8 | c'''4 a'''2-- g'''4 | f'''4. e'''8 d'''4 c'''4 | d'''2 c'''2) | R1*2 | r2 r8 g''8(\f a'' b'' | c'''8 d''' e''' f''' g'''4 a'''8 b''') | }
sHeadOboeOne = { R1*4 | e''2.~(\f e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | d''2 c''2) | R1*4 | }
sHeadVc = { c1\mf | c1 | d2 f,2 | g,1 | a,1\f | f,1 | d2 f,2 | fis,1 | g,1\< | g,1 | d1 | d1\! | }
sHeadCb = { c,1\mf~ | c,1~ | c,1~ | c,1 | a,,1\f | f,,1 | d,2 f,,2 | fis,,1 | g,,1\< | g,,1 | d,1 | d,1\! | }
sHeadBsnTwo = { c1\mf | c1 | d2 f,2 | g,1 | a,1\f | f,1 | d2 f,2 | fis,1 | g,1\< | g,1 | d1 | d1\! | }
sHeadBsnOne = { g1\mf | f1 | f2 a2 | g2 f2 | c'1\f | c'1 | a1 | d'1 | b1\< | b1 | b1 | b1\! | }
sHeadHnThree = { g1\p | a1 | a1 | g1 | e'1\mf | c'1 | a1 | c'1 | R1*4 | }
sHeadHnFour = { e1\p | f1 | f1 | f1 | c'1\mf | a1 | f1 | a1 | R1*4 | }
sHeadTptOne = { R1*8 | e''2->(\f c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1) | }
sHeadTptTwo = { R1*8 | e''2->(\f c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1) | }
sHeadHnOne = { R1*8 | e2->(\f c'2~ | c'4 b2.~ | b2 c'2~ | c'1) | }
sHeadHnTwo = { R1*8 | e2->(\f c'2~ | c'4 b2.~ | b2 c'2~ | c'1) | }
sHeadTimp = { c1:32\pp | c1:32 | c1:32 | c1:32 | R1*4 | g,1:32\p\< | g,1:32 | g,1:32 | g,1:32\f | }
sHeadHarpR = { g8 c'8 e'8 g'8 g'8 e'8 c'8 g8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | g8 b8 d'8 g'8 g'8 d'8 b8 g8 | a8 c'8 e'8 a'8 a'8 e'8 c'8 a8 | a8 c'8 f'8 a'8 a'8 f'8 c'8 a8 | a8 d'8 f'8 a'8 a'8 f'8 d'8 a8 | a8 c'8 d'8 a'8 a'8 d'8 c'8 a8 | R1*4 | }
sHeadHarpL = { c,1\mf | c,1 | d,1 | g,,1 | a,,1 | f,,1 | d,1 | fis,,1 | R1*4 | }

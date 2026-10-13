% INTRODUCTION, bars 1-10 (Allegro con fuoco). After movement III (the scherzo, E major at its end) and a pause.
% c026 (rework for four movements): the scherzo ends pp on G sharp alone (Hn 1 G#4, Vln I G#5) after a harp E-major chord and a pizzicato E.
% The finale takes that G sharp as A flat, in the same players at the same pitch (Hn 1 A flat 4, Vln I A flat 5), now ff, as the root of the
% German sixth A flat - C - E flat - F sharp; the scherzo's other chord tones move by step: E -> E flat (Vc E3 -> E flat 3) and B -> C.
% Direct ff start, no quiet held A flat first: the scherzo has already held the G sharp pp for 17 bars (368-384); after a pause a second quiet
% A flat would repeat that ending, and Beethoven 5's quiet pedal works only because its scherzo runs attacca into the finale (cyclic rule: no soft opening).
% 1-2 and 5-6: German sixth -> V, tutti without trumpets (their first melody is the second theme at 51).
% 3-4: the strings' answer, a turn figure on V (the finale's own motive, reused in the transition and development).
% 7-10: dominant preparation; the low strings anticipate the first theme's rhythm on V; crescendo into A.

introFluteOne = { c'''1->\ff | b''4-> r4 r2 | R1*2 | c'''1-> | b''4-> r4 r2 | R1*2 | d'''1\p\< | f'''2 d'''4-> r4\! | }
introFluteTwo = { fis''1->\ff | g''4-> r4 r2 | R1*2 | fis''1-> | g''4-> r4 r2 | R1*2 | b''1\p\< | b''2 b''4-> r4\! | }
introOboeOne = { es''1->\ff | d''4-> r4 r2 | R1*2 | es''1-> | d''4-> r4 r2 | R1*2 | f''1\p\< | aes''2 f''4-> r4\! | }
introOboeTwo = { c''1->\ff | b'4-> r4 r2 | R1*2 | c''1-> | b'4-> r4 r2 | R1*2 | d''1\p\< | d''2 d''4-> r4\! | }
introCorAnglais = { fis'1->\ff | g'4-> r4 r2 | R1*2 | fis'1-> | g'4-> r4 r2 | R1*4 | }
introClOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1-> | g'4-> r4 r2 | R1*2 | b'1\p\< | b'2 b'4-> r4\! | }
introClTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1-> | d'4-> r4 r2 | R1*2 | g'1\p\< | g'2 g'4-> r4\! | }
introBassCl = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1-> | g,4-> r4 r2 | R1*4 | }
introBsnOne = { c1->\ff | b,4-> r4 r2 | R1*2 | c1-> | b,4-> r4 r2 |
  d2\p( g,4. aes,8 | b,4 c8 d8 es4 f4) | g4\<( aes4 b4 c'4 | d'4 es'4 f'4-> d'4->)\! | }
introBsnTwo = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1-> | g,4-> r4 r2 |
  d2\p( g,4. aes,8 | b,4 c8 d8 es4 f4) | g,1\<~ | g,2 g,4-> r4\! | }
introCbsn = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1-> | g,,4-> r4 r2 | R1*2 | g,,1\p\<~ | g,,2 g,,4-> r4\! | }
introHnOne = { aes'1->\ff | g'4-> r4 r2 | R1*2 | aes'1-> | g'4-> r4 r2 | R1*2 | g'1\p\< | g'2 g'4-> r4\! | }
introHnTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1-> | d'4-> r4 r2 | R1*2 | d'1\p\< | d'2 d'4-> r4\! | }
introHnThree = { c'1->\ff | b4-> r4 r2 | R1*2 | c'1-> | b4-> r4 r2 | R1*2 | b1\p\< | b2 b4-> r4\! | }
introHnFour = { fis1->\ff | g4-> r4 r2 | R1*2 | fis1-> | g4-> r4 r2 | R1*2 | g1\p\< | g2 g4-> r4\! | }
introTbnOne = { es1->\ff | g4-> r4 r2 | R1*2 | es1-> | g4-> r4 r2 | R1*4 | }
introTbnTwo = { c1->\ff | b,4-> r4 r2 | R1*2 | c1-> | b,4-> r4 r2 | R1*4 | }
introBassTbn = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1-> | g,4-> r4 r2 | R1*4 | }
introTuba = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1-> | g,,4-> r4 r2 | R1*4 | }
% Timpani: the scherzo ends tuned E, G, B, E (E2, G2, B2, E3). In the pause each drum moves within its range: 32" E2 -> G2, 29" G2 -> A flat 2,
% 26" B2 -> C3, 23" E3 -> E flat 3 (no drum moves more than a minor third). Adler PDF 112: give the setting at the start.
introTimp = { aes,4->\ff^\markup \column { \italic "Timpani: G, A♭, C, E♭" \italic "(retune in the pause: E → G, G → A♭, B → C, E → E♭)" } r4 r2 | g,4-> r4 r2 | R1*2 |
  aes,4-> r4 r2 | g,4-> r4 r2 | g,4\p r4 r2 | g,4 r4 r2 | g,4\< r4 g,4 r4 | g,8 g,8 g,8 g,8 g,4->\f r4 | }
introVlnOne = { <c'' aes''>1->\ff\dnup | <b' g''>4->\downbow r4 r2 |
  r4 g''8(\f f''8 es''8 d''8 c''8 b'8 | c''8 d''8 es''8 f''8 g''4->) g'4-> |
  <c'' aes''>1->\ff\dnup | <b' g''>4->\downbow r4 r2 | R1*2 | r4 g'8(\p\< aes'8 b'8 c''8 d''8 es''8 | f''8 g''8 aes''8 b''8 d'''4->) r4\! | }
introVlnTwo = { <es' c''>1->\ff\dnup | <g d' b'>4->\downbow r4 r2 |
  r4 g'8(\f f'8 es'8 d'8 c'8 b8 | c'8 d'8 es'8 f'8 g'4->) g4-> |
  <es' c''>1->\ff\dnup | <g d' b'>4->\downbow r4 r2 | R1*2 | r4 g8(\p\< aes8 b8 c'8 d'8 es'8 | f'8 g'8 aes'8 b'8 d''4->) r4\! | }
introVla = { <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 |
  r4 g'8(\f^\markup \italic "unis." f'8 es'8 d'8 c'8 b8 | c'8 d'8 es'8 f'8 g'4->) g4-> |
  <es' fis'>1->\ff\dnup^\markup \italic "div." | <d' g'>4->\downbow r4 r2 | R1*2 | d'1\p\<^\markup \italic "unis." | d'2 d'4-> r4\! | }
introVc = { <aes, es>1->\ff\dnup | g,4->\downbow r4 r2 | R1*2 | <aes, es>1->\ff\dnup | g,4->\downbow r4 r2 |
  d2\p( g,4. aes,8 | b,4 c8 d8 es4 f4) | g4\<( aes4 b4 c'4 | d'4 es'4 f'4-> d'4->)\! | }
introCb = { aes,,1->\ff\dnup | g,,4->\downbow r4 r2 | R1*2 | aes,,1->\dnup | g,,4->\downbow r4 r2 | R1*2 | g,,1\p\<~ | g,,2 g,,4-> r4\! | }

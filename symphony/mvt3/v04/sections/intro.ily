% INTRODUCTION, bars 1-10 (Allegro con fuoco). After a pause: movement II's last chord (A flat - C - E flat) becomes a German sixth
% with F sharp added, ff, and resolves to V of C (cyclic-notes "Start here for movement III": Opening; A&S PDF 593).
% 1-2 and 5-6: German sixth -> V, tutti without trumpets (their first entry is the second theme at 51).
% 3-4: the strings' answer, a turn figure on V (motive x, reused in the transition and development).
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
introHnOne = { fis'1->\ff | g'4-> r4 r2 | R1*2 | fis'1-> | g'4-> r4 r2 | R1*2 | g'1\p\< | g'2 g'4-> r4\! | }
introHnTwo = { es'1->\ff | d'4-> r4 r2 | R1*2 | es'1-> | d'4-> r4 r2 | R1*2 | d'1\p\< | d'2 d'4-> r4\! | }
introHnThree = { c'1->\ff^\markup \italic "senza sord." | b4-> r4 r2 | R1*2 | c'1-> | b4-> r4 r2 | R1*2 | b1\p\< | b2 b4-> r4\! | }
introHnFour = { aes1->\ff^\markup \italic "senza sord." | g4-> r4 r2 | R1*2 | aes1-> | g4-> r4 r2 | R1*2 | g1\p\< | g2 g4-> r4\! | }
introTbnOne = { es1->\ff | g4-> r4 r2 | R1*2 | es1-> | g4-> r4 r2 | R1*4 | }
introTbnTwo = { c1->\ff | b,4-> r4 r2 | R1*2 | c1-> | b,4-> r4 r2 | R1*4 | }
introBassTbn = { aes,1->\ff | g,4-> r4 r2 | R1*2 | aes,1-> | g,4-> r4 r2 | R1*4 | }
introTuba = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1-> | g,,4-> r4 r2 | R1*4 | }
% Timpani: movement II ends tuned A flat, C, D flat, E flat; the D flat drum is retuned to G during the pause.
introTimp = { aes,4->\ff^\markup \column { \italic "Timpani: retune D♭ → G during the pause" \italic "(G, A♭, C, E♭)" } r4 r2 | g,4-> r4 r2 | R1*2 |
  aes,4-> r4 r2 | g,4-> r4 r2 | g,4\p r4 r2 | g,4 r4 r2 | g,4\< r4 g,4 r4 | g,8 g,8 g,8 g,8 g,4->\f r4 | }
introVlnOne = { <c'' fis''>1->\ff\downbow | <b' g''>4-> r4 r2 |
  r4 g''8(\f f''8 es''8 d''8 c''8 b'8 | c''8 d''8 es''8 f''8 g''4->) g'4-> |
  <c'' fis''>1->\ff\downbow | <b' g''>4-> r4 r2 | R1*2 | r4 g'8(\p\< aes'8 b'8 c''8 d''8 es''8 | f''8 g''8 aes''8 b''8 d'''4->) r4\! | }
introVlnTwo = { <es' c''>1->\ff\downbow | <g d' b'>4-> r4 r2 |
  r4 g'8(\f f'8 es'8 d'8 c'8 b8 | c'8 d'8 es'8 f'8 g'4->) g4-> |
  <es' c''>1->\ff\downbow | <g d' b'>4-> r4 r2 | R1*2 | r4 g8(\p\< aes8 b8 c'8 d'8 es'8 | f'8 g'8 aes'8 b'8 d''4->) r4\! | }
introVla = { <es' fis'>1->\ff\downbow | <d' g'>4-> r4 r2 |
  r4 g'8(\f f'8 es'8 d'8 c'8 b8 | c'8 d'8 es'8 f'8 g'4->) g4-> |
  <es' fis'>1->\ff\downbow | <d' g'>4-> r4 r2 | R1*2 | d'1\p\< | d'2 d'4-> r4\! | }
introVc = { <aes, es>1->\ff\downbow | g,4-> r4 r2 | R1*2 | <aes, es>1->\ff\downbow | g,4-> r4 r2 |
  d2\p( g,4. aes,8 | b,4 c8 d8 es4 f4) | g4\<( aes4 b4 c'4 | d'4 es'4 f'4-> d'4->)\! | }
introCb = { aes,,1->\ff | g,,4-> r4 r2 | R1*2 | aes,,1-> | g,,4-> r4 r2 | R1*2 | g,,1\p\<~ | g,,2 g,,4-> r4\! | }

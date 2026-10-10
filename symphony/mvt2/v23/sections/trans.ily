% TRANSITION, bars 31-36 (3/4). Bass clarinet solo over an A flat pedal (bassoon 2, contrabassoon),
% the theme's arpeggio and chromatic tail re-heard over the tonic. Woodwinds alone (no strings, no timpani).

% c020: 31-36 are a woodwind choir alone on the tonic (critic 119's woodwind-choir note; Rimsky-Korsakov PDF 89-90):
% the A section closes on A flat and D flat enters at 37 by phrase modulation, with no V7 of D flat before it
% (A&S PDF 452, Ex. 26-11; cyclic-notes, changes 111-120). The common-tone diminished seventh at 33 is kept.
transBassCl = {
  r4 es8(\mp^\markup \italic "solo, espr." f8 aes8 c'8 | es'2.~ | es'4 d'4 des'4 | c'2 bes4) \breathe |
  aes2.~(\> | aes4\p\< bes4 c'4 |
}
transClOne = { R2. | c'2.\pp | c'4 b4 bes4 | c'2. | es'2. | es'2. | }
transClTwo = { R2. | aes2.\pp | aes4 f4 f4 | aes2. | c'2. | c'2. | }
transBsnOne = { R2.*4 | aes2.\pp | aes2. | }
transBsnTwo = { aes,2.~\pp | aes,2.~ | aes,2 \breathe aes,4~ | aes,2.~ | aes,2.~ | aes,2 r4 | }
transCbsn = { aes,,2.~\pp | aes,,2.~ | aes,,2 r4 | R2.*3 | }

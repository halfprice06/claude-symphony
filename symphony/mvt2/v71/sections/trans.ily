% TRANSITION, bars 31-36 (3/4). Bass clarinet solo over an A flat pedal (bassoon 2, contrabassoon),
% the theme's arpeggio and chromatic tail re-heard over the tonic. Woodwinds alone (no strings, no timpani).

% c020: 31-36 are a woodwind choir alone on the tonic (critic 119's woodwind-choir note; Rimsky-Korsakov PDF 89-90):
% the A section closes on A flat and D flat enters at 37 by phrase modulation, with no V7 of D flat before it
% (A&S PDF 452, Ex. 26-11; cyclic-notes, changes 111-120). The common-tone diminished seventh at 33 is kept.
transBassCl = {
  r4 es8(\mp^\markup \italic "solo, espr." f8 aes8 c'8 | es'2.~\< | es'4\mf\> d'4 des'4 | c'2\p bes4) \breathe |
  aes2.~(\> | aes4\pp\< bes4 c'4 |
}
% c027: the clarinets leave 32-36. They lay a third below the bass clarinet in its own register and family, moved in its
% rhythm at 33, doubled its C4 at 34 and sat above its A flat3 at 35-36 (Adler part 2 PDF 264 and 267: Mozart keeps the
% solo's own family out of the accompaniment; PDF 259-260: the accompaniment neither duplicates nor imitates the solo's
% rhythm; PDF 274: keep the accompanying forces registrally distant, especially under a woodwind solo).
% The same harmony (common-tone diminished seventh at 33 b2 kept) goes to cor anglais and bassoon 1, a double-reed colour;
% the lower voice holds F from 33 b2 into 34 and falls to E flat3 on 34 b2; the cor anglais steps to A flat3 at 34, so nothing doubles the solo's C4.
% At 35-36 the solo's A flat3 is the top voice over bassoon 1's E flat3 and bassoon 2's A flat2 pedal.
transCorAnglais = { R2. | c'2.(\p^\markup \italic "dolce" | c'4 b4 bes4 | aes2.) | R2.*2 | }
transBsnOne = { R2. | aes2.(\pp | aes4 f2~ | f4 es2) \breathe | es2.~ | es2 r4 | }  % c066: breath at 34/35 (about 17 s held at pp from 32 to 36), staggered from bassoon 2's at 33 (Adler part 1 PDF 175, 188)  % F tied over the bar (6-5 over the pedal): the two accompanying voices do not move together into 34, and no parallel fourths with the cor anglais
transBsnTwo = { aes,2.~\pp | aes,2.~ | aes,2 \once \override BreathingSign.direction = #DOWN \breathe aes,4~ | aes,2.~ | aes,2.~ | aes,2 r4 | }
transCbsn = { aes,,2.~ |  % c063: tied from 30
  aes,,2.~ | aes,,2 r4 | R2.*3 | }

\version "2.26.0"
% RETRANSITION, bars 65-70 (Tempo I, 3/4). The E of the A minor bar slips to E flat (V of A flat).
% Horn 1 alone over the double basses' and timpani's E flat: the motto's tail E flat-D-D flat-C to B flat.

retrVlnOne = { R2.*5 | r2 es''8(\p^\markup \italic "espr." f''8 | }
retrVlnTwo = { des'2.)\pp^\markup \italic "unis." | des'2.\> | R2.*3\! | r2 es'8(\p^\markup \italic "sul D" f'8 | }  % c076: sul D, as at 22 (Rimsky-Korsakov PDF 26: on a lower string go no higher than the fourth position, the octave or ninth; E flat5 is the ninth of D). Was sul G (c031)
retrVla = { g2.)\pp^\markup \italic "unis., sul C" | g2.\> | R2.*4\! | }
retrVc = { bes,2.\pp | bes,2.\> | R2.*4\! | }
retrCb = { es,2.\pp~^\markup \italic "change bow at will" | es,2.~ | es,2.~ | es,2.~ | es,2.~ | es,2. | }
retrTimp = { R2.*2 | es2.:32\ppp~ | es2.:32~ | es2.:32~ | es2:32~ es8 r8 | }  % c056: roll ends on a tied stroke with the horn and bassoons (Adler part 2 PDF 80, Ex. XII-47)
retrHnOne = { R2.*2 | \set Staff.soloText = "1. solo" es'2.(\p\<^\markup \bold "1. solo" | d'4\mp\> des'4 c'4 | bes2.~ | bes2)\pp r4 | \set Staff.soloText = "1." }  % c046: label written out: after horn 2's "2." at 61-62 the part-combiner no longer prints it  % c035: one label, "1. solo"
% c043: bassoon 1 enters at 68 a third under horn 1's tail (D-D flat-C over B flat-B flat-A flat), so the tail over the held dominant is the
% 8-7-6-5 / 6-5-4-3 progression and 68 b3 is a passing 6/4 (A flat-C over E flat) into V7 at 69 (A&S PDF 311-314, Ex. 19-14, 19-16).
retrBsnOne = { R2.*3 | bes2(\pp^\markup \bold "1." aes4 | g2.) | g2 r4 | }
retrBsnTwo = { R2.*4 | des2.\pp | des2 r4 | }

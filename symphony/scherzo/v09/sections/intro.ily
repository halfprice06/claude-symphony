% INTRODUCTION, bars 1-12 (Allegro vivace). After a pause following movement II.
% 1-3: Hn 1 holds G sharp 4 alone: movement II's last A flat heard again as G sharp, the third of E major (cyclic-notes "Four movements").
% 4-7: the horn call of movement I (E flat-C-B, 3-1-7) in E major: G sharp-E-D sharp-E. D sharp is spelled as E major's leading tone.
% 7-8: clarinets and bassoon turn the chord to E minor (G natural replaces G sharp).
% 9-12: timpani alone: motive x (quarter, two eighths, quarter), the rhythm of the scherzo theme (a melodic timpani figure, still unused in I and II).

introClOne = { R2.*6 | g'2.~\pp | g'2 r4 | R2.*4 | }
introClTwo = { R2.*6 | e'2.~\pp | e'2 r4 | R2.*4 | }
introBsnOne = { R2.*6 | b2.~\pp | b2 r4 | R2.*4 | }
introHnOne = { gis'2.~\pp | gis'2.~ | gis'2.\< | e'2.\> | dis'2. | e'2.~\! | e'2 r4 | R2.*5 | }
introHnTwo = { R2.*2 | b2.~\pp\< | b2.~\> | b2.~ | b2.~\! | b2 r4 | R2.*5 | }
introTimp = { << R2.*2 { s2.^\markup \small \column { "Timpani: E, G, B, E" "(retuned during the pause)" } s2. } >> | e,4\pp r4 r4 | R2.*5 | b,4\p b,8 b,8 g,4 | e,4 r4 r4 | b,4 b,8 b,8 e4 | e,4 r4 r4 | }
introVc = { R2.*2 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | e,4 r4 r4 | R2.*6 | }
introCb = { R2.*2 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | e,,4 r4 r4 | R2.*6 | }

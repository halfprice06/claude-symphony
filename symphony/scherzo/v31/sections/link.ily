% LINK to the trio, bars 141-152. The intro in reverse: Hn 1 G natural (141-144) rises to G sharp (145), E major;
% the harp enters with E major (pedals set during 105-140); poco rit. 149-152.

linkClOne = { R2.*4 | e'2.\pp | e'2. | e'2. | e'2 r4 | R2.*4 | }
linkClTwo = { R2.*4 | b2.\pp | b2. | b2. | b2 r4 | R2.*4 | }
linkBsnOne = { b,2.\pp | b,2. | b,2. | b,2 r4 | R2.*8 | }
linkBsnTwo = { e,2.\pp | e,2. | e,2. | e,2 r4 | e,2.\pp | e,2. | e,2. | e,2 r4 | R2.*4 | }
linkHnOne = { g'2.~\pp | g'2.~ | g'2.~ | g'2 r4 | gis'2.~\< | gis'2.~ | gis'2.\> | gis'2 r4\! | R2.*4 | }
linkTimp = { R2.*4 | R2.^\markup \small \italic "muta G in G♯" | R2.*3 | e,4\pp r4 r4 | R2. | b,4 r4 r4 | R2. | }
linkHarpR = { \once \override MultiMeasureRestText.self-alignment-X = #LEFT \once \override MultiMeasureRestText.parent-alignment-X = #LEFT R2._\markup \small "Ped.: D♯ C♯ B / E F♯ G♯ A" | R2.*7 | r4 <gis' b' e''>4\arpeggio r4 | R2. | r4 <gis' b' e''>4\arpeggio r4 | R2. | }  % c026: pedal setting printed at 141, before the entry, in Adler's letter form DCB/EFGA (PDF 112)
linkHarpL = { R2.*8 | e,4\pp r4 r4 | R2. | e,4 r4 r4 | R2. | }
linkVc = { R2.*8 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | }
linkCb = { R2.*8 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | R2. | }

% LINK to the trio, bars 141-152. The intro in reverse: Hn 1 G natural (141-144) rises to G sharp (145), E major;
% the harp enters with E major (pedals set during 105-140); poco rit. 149-152.

% c190: the E4/B3 pad under Hn 1 at 145-148 moves from Cl 1-2 to Bsn 1-2 (same pitches), so the clarinet colour is fresh when Cl 1 enters
%   with the trio tune at 153 (Adler II PDF 263: a contrasting colour introduces the soloist; PDF 267, item 4: no colour competition for the solo)
% c135: "1." at 141 (Bsn 1 alone after rests; no automatic label; MOLA PDF 4, Ex. 6)
linkBsnOne = { b,2.\pp^\markup \bold "1." | b,2. | b,2. | b,2 r4 | e'2.\pp | e'2. | e'2.\> | e'2 r4\! | R2.*4 | }
linkBsnTwo = { R2.*4 | b2.\pp | b2. | b2.\> | b2 r4\! | R2.*4 | }
% c036: the E2 pedal 141-148 moves from Bsn 2 to the bass clarinet: pp on the bassoon's lowest fifth (B flat 1-F 2) is insecure and needs a firmer attack
% (Adler PDF 174-175, 226); the clarinet family keeps its full dynamic range down to its lowest notes and the bass clarinet's chalumeau is its best register (Adler PDF 175, 210, 217)
linkBassCl = { e,2. | e,2. | e,2. | e,2 r4 | e,2.\pp | e,2. | e,2.\> | e,2 r4\! | R2.*4 | }
% c051: 147-148 Hn 1 G sharp-A-G sharp, T's first two notes at T's pitch, so the trio tune grows out of the pivot G sharp that Cl 1 takes at 153
%   (Sebesky PDF 206: an introduction built on the tune's initial two-note motive; PDF 222: the last orchestral note gives the soloist its first note).
% c124: p at 147 gives the crescendo from 141's pp a target (MIDI rose to a default mf with the staff-level dynamics, c124 score.ly; Adler II PDF 154: the background a level under the foreground)
linkHnOne = { g'2.~\pp | g'2.~ | g'2.~ | g'2 r4 | gis'2.~\< | gis'2.~ | gis'2(\p\> a'4 | gis'2) r4\! | R2.*4 | }
linkTimp = { R2.*4 | R2.^\markup \small \italic "muta G in G♯" | R2.^\markup \small \italic "soft sticks" | R2.*2 | e,4\pp r4 r4 | R2. | b,4 r4 r4 | R2. | }  % c055: "soft sticks" at 146, three bars before the pp strokes at 149 and 151 (was at 153 with one bar to change; Adler II PDF 294: instructions well ahead, above the staff)
linkHarpR = { R2.*8 | r4 <gis' b' e''>4\arpeggio r4 | R2. | r4 <gis' b' e''>4\arpeggio r4 | R2. | }  % c026: pedal setting printed at 141, before the entry, in Adler's letter form DCB/EFGA (PDF 112)
linkHarpL = { \once \override MultiMeasureRestText.self-alignment-X = #LEFT \once \override MultiMeasureRestText.parent-alignment-X = #LEFT R2._\markup \small "Ped.: D♯ C♯ B / E F♯ G♯ A" | R2.*7 | e,4\pp r4 r4 | R2. | b,,4 r4 r4 | R2. | }  % c174: 151 B1 with Vc/Cb/timpani (was E2, a fourth above the basses' B1; Casanelles PDF 274, harmonic series)
linkVc = { R2.*8 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | }
linkCb = { R2.*8 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | R2. | }
% c045: the pedal setting at 141 printed below the harp's LH staff, clear of the barline between the two harp staves (MOLA PDF 8, Example 7).

% LINK to the trio, bars 141-152. The intro in reverse: Hn 1 G natural (141-144) rises to G sharp (145), E major;
% the harp enters with E major (pedals set during 105-140); poco rit. 149-152.

% c190: the E4/B3 pad under Hn 1 at 145-148 moves from Cl 1-2 to Bsn 1-2 (same pitches), so the clarinet colour is fresh when Cl 1 enters
%   with the trio tune at 153 (Adler II PDF 263: a contrasting colour introduces the soloist; PDF 267, item 4: no colour competition for the solo)
% c135: "1." at 141 (Bsn 1 alone after rests; no automatic label; MOLA PDF 4, Ex. 6)
% c234: 141-144 Bsn 1 B3 (was B2): the pp wind chord E2 (B. cl.) - B2 - G4 (Hn 1) had a 20-semitone hole between the bassoon and the horn and its only
%   close interval at the bottom; Adler I PDF 257 (Ex. VIII-24): the greater gap lies between the bass and the next voice, the upper voices close. Now E2 - B3 - G4,
%   the bassoon a third under Hn 1, as Bsn 1's B3 under the clarinets at 7 (the link is the intro in reverse); B3 passes to Bsn 2 at 145 as a common tone.
% c288: 141-148 the pp pad under Hn 1 (Bsn 1-2, B.cl.) slurred by four-bar phrase with tenuto: unmarked, the bass clarinet's E2 and the bassoons were re-tongued
%   on every downbeat while Hn 1 ties its G and G sharp over the same bars (Adler I PDF 309, 321: separate notes are tongued; PDF 303 and 319: soft attacks in the low register are the hard ones).
linkBsnOne = { b2.--(\pp^\markup \bold "1." | b2.-- | b2.-- | b2--) r4 | e'2.--(\pp | e'2.-- | e'2.--\> | e'2--) r4\! | R2.*4 | }
linkBsnTwo = { R2.*4 | b2.--(\pp | b2.-- | b2.--\> | b2--) r4\! | R2.*4 | }
% c036: the E2 pedal 141-148 moves from Bsn 2 to the bass clarinet: pp on the bassoon's lowest fifth (B flat 1-F 2) is insecure and needs a firmer attack
% (Adler PDF 174-175, 226); the clarinet family keeps its full dynamic range down to its lowest notes and the bass clarinet's chalumeau is its best register (Adler PDF 175, 210, 217)
linkBassCl = { e,2.--( | e,2.-- | e,2.-- | e,2--) r4 | e,2.--(\pp | e,2.-- | e,2.--\> | e,2--) r4\! | R2.*4 | }
% c051: 147-148 Hn 1 G sharp-A-G sharp, T's first two notes at T's pitch, so the trio tune grows out of the pivot G sharp that Cl 1 takes at 153
%   (Sebesky PDF 206: an introduction built on the tune's initial two-note motive; PDF 222: the last orchestral note gives the soloist its first note).
% c124: p at 147 gives the crescendo from 141's pp a target (MIDI rose to a default mf with the staff-level dynamics, c124 score.ly; Adler II PDF 154: the background a level under the foreground)
linkHnOne = { g'2.~\pp | g'2.~ | g'2.~ | g'2 r4 | gis'2.~\< | gis'2.~ | gis'2(\p\> a'4 | gis'2) r4\! | R2.*4 | }
% c333: 149-152 Hn 3-4 take up the trio's E-B drone pp as Hn 1's G sharp ends, so the musette background (drone, harp chord, pizz. bass) is in place
%   one four-bar group before Cl 1 brings T in at 153, and the horn sound is dovetailed across 148-149 instead of four bars of isolated plucks (Adler II PDF 192:
%   seams do not show; 263: the background colour first, so the solo colour enters fresh; 268-270: Sibelius and Bartok set the background before the solo).
linkHnThree = { R2.*8 | b2.~\pp | b2.~ | b2.~ | b2 r4 | }
linkHnFour = { R2.*8 | e2.~\pp | e2.~ | e2.~ | e2 r4 | }
linkTimp = { R2.*4 | R2.^\markup \small \italic "G muta in G♯" | R2.^\markup \small \italic "soft sticks" | R2.*2 | e,4\pp r4 r4 | R2. | b,4 r4 r4 | R2. | }  % c055: "soft sticks" at 146, three bars before the pp strokes at 149 and 151 (was at 153 with one bar to change; Adler II PDF 294: instructions well ahead, above the staff)
% c336: "G muta in G♯" (was "muta G in G♯"): the old pitch, then muta, then the new pitch, as Adler II PDF 312 gives the term ("Change C to E: Sol muta in Mi").
linkHarpR = { R2.*8 | r4 <gis' b' e''>4-\tweak extra-spacing-width #'(-1.0 . 0) \arpeggio r4 | R2. | r4 <gis' b' e''>4-\tweak extra-spacing-width #'(-1.0 . 0) \arpeggio r4 | R2. | }  % c026: pedal setting printed at 141, before the entry, in Adler's letter form DCB/EFGA (PDF 112)
linkHarpL = { \once \override MultiMeasureRestText.self-alignment-X = #LEFT \once \override MultiMeasureRestText.parent-alignment-X = #LEFT R2._\markup \small "Ped.: D♯ C♯ B♮ / E♮ F♯ G♯ A♮" | R2.*7 | e,4\pp r4 r4 | R2. | b,,4 r4 r4 | R2. | }  % c174: 151 B1 with Vc/Cb/timpani (was E2, a fourth above the basses' B1; Casanelles PDF 274, harmonic series)
linkVc = { R2.*8 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | }
linkCb = { R2.*8 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | R2. | }
% c045: the pedal setting at 141 printed below the harp's LH staff, clear of the barline between the two harp staves (MOLA PDF 8, Example 7).

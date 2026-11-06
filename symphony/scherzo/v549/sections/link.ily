% c498 (lens 8, A&S Unit 21): 147-148 Hn 1 ties T's A4 over the barline (gis'2 a'4~ | a'4 gis'2~, was gis'2 a'4 | gis'2.~): the upper neighbour becomes a
%   suspended neighbour, a 4-3 over the E-B pad (A-S PDF 359-360 sec. 18, Ex. 21-23b: neighbouring tones suspended before resolving; PDF 349 sec. 7: 4-3 with a 5th,
%   bass doubled; PDF 354 sec. 12: no G sharp in the pad before beat 2). Shaded < into the tie, hidden mp peak, > to a hidden pp (PDF 348 sec. 4). The link now
%   previews T's head (G sharp-A, c051) and T's tied A-G sharp cell (bars 3-4, c331) at T's pitch before Cl 1 takes them at 153. G sharp held into 149 beat 1 (c340) as before.
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
% c547 (lens 7, Rimsky-Korsakov PDF 108: four-part harmony of bassoons and horn in soft passages gives a balanced, transparent tone; PDF 112: octave doublings
%   strengthen one another, the low harmonic sounds supporting the high): 141-144 the E-minor pad is E2 (B. cl.) - B3 (Bsn 2) - E4 (Bsn 1) - G4 (Hn 1), the same
%   voicing as the E-major pad at 145-148, so the only change at 145 is Hn 1's G -> G sharp (the intro reversed) and the minor pad has its root inside it
%   (was E2 - B3 - G4, three parts; c234's close upper voices kept). Each bassoon now holds one pitch through the link (Bsn 1 E4, Bsn 2 B3 with c413's C sharp at 146).
linkBsnOne = { e'2.--(\pp | e'2.-- | e'2.-- | e'2--) r4 | e'2.--(\pp | e'2.-- | e'2.--\> | e'2--) r4\! | R2.*4 | }
% c413: 146 Bsn 2 C sharp 4 (was B3), a 5-6-5 neighbour B3-C sharp 4-B3 inside the E-major pad under Hn 1's held G sharp 4: E2-C sharp 4-E4-G sharp 4 is I with 6 for 5,
%   not vi (A&S Unit 18 PDF 299-300, Ex. 18-14: 'not VI6'; Ex. 18-19a, j: neighbouring 6/3, 6 displacing 5; PDF 290: the 6/3's fluid sound suits a transition), so the
%   eight-bar pad 141-148 moves once in the major half, as Dvorak 9/iii colours its E-pedal link to the trio with VI6 over E (bars 201-208, 231-234). Bass E2 and Hn 1 unchanged.
linkBsnTwo = { b2.--(\pp | b2.-- | b2.-- | b2--) r4 | b2.--(\pp | cis'2.-- | b2.--\> | b2--) r4\! | R2.*4 | }
% c036: the E2 pedal 141-148 moves from Bsn 2 to the bass clarinet: pp on the bassoon's lowest fifth (B flat 1-F 2) is insecure and needs a firmer attack
% (Adler PDF 174-175, 226); the clarinet family keeps its full dynamic range down to its lowest notes and the bass clarinet's chalumeau is its best register (Adler PDF 175, 210, 217)
linkBassCl = { e,2.--( | e,2.-- | e,2.-- | e,2--) r4 | e,2.--(\pp | e,2.-- | e,2.--\> | e,2--) r4\! | R2.*4 | }
% c051: 147-148 Hn 1 G sharp-A-G sharp, T's first two notes at T's pitch, so the trio tune grows out of the pivot G sharp that Cl 1 takes at 153
%   (Sebesky PDF 206: an introduction built on the tune's initial two-note motive; PDF 222: the last orchestral note gives the soloist its first note).
% c124: p at 147 gives the crescendo from 141's pp a target (MIDI rose to a default mf with the staff-level dynamics, c124 score.ly; Adler II PDF 154: the background a level under the foreground)
% c340: Hn 1 holds its G sharp 4 through 148 into the downbeat of 149, where the Hn 3-4 drone enters, and leaves on beat 2 as the harp plucks G sharp 4:
%   the pivot pitch (movement II's A flat) passes Hn 1 -> harp -> Cl 1 (153) without the one-beat silence that 148 beat 3 had (Adler II PDF 190-192, Ex. XV-37, XV-40:
%   each colour of a held note enters before the last one stops, and seams do not show; c333 meant the drone to take over 'as Hn 1 leaves'). 148 beat 3 is Hn 1 alone, as bars 1-2.
linkHnOne = { g'2.~\pp | g'2.~ | g'2.~ | g'2 r4 | gis'2.~\< | gis'2.~ | gis'2(\p a'4\<~ | a'4-\tweak stencil ##f \mp\> gis'2~ | gis'4)-\tweak stencil ##f \pp r4 r4 | R2.*3 | }
% c333: 149-152 Hn 3-4 take up the trio's E-B drone pp as Hn 1's G sharp ends, so the musette background (drone, harp chord, pizz. bass) is in place
%   one four-bar group before Cl 1 brings T in at 153, and the horn sound is dovetailed across 148-149 instead of four bars of isolated plucks (Adler II PDF 192:
%   seams do not show; 263: the background colour first, so the solo colour enters fresh; 268-270: Sibelius and Bartok set the background before the solo).
linkHnThree = { R2.*8 | b2.~\pp | b2.~ | b2.~ | b2 r4 | }
linkHnFour = { R2.*8 | e2.~\pp | e2.~ | e2.~ | e2 r4 | }
linkTimp = { R2.*4 | R2.^\markup \small \italic "G muta in G♯" | R2.^\markup \small \italic "soft sticks" | R2.*2 | e,4\pp r4 r4 | R2. | b,4 r4 r4 | R2. | }  % c055: "soft sticks" at 146, three bars before the pp strokes at 149 and 151 (was at 153 with one bar to change; Adler II PDF 294: instructions well ahead, above the staff)
% c336: "G muta in G♯" (was "muta G in G♯"): the old pitch, then muta, then the new pitch, as Adler II PDF 312 gives the term ("Change C to E: Sol muta in Mi").
% c476: 149/151 the harp's entry is the chord of its last sound (375), E4-G#4-B4 in octave harmonics, LH E3-G#3, RH B3 written
% (Adler part 1 PDF 116: bell-like; two or more harmonics in one hand within a fifth; best written range C3-A5; very soft, so only lightly
% accompanied - here a pp horn drone and single pp strokes). The beat-1 bass E2/B1 is left to the pizz. basses and timpani, so both hands
% are free to place the harmonics. The harmonic G#4 takes over Hn 1's G#4 (released after beat 1 of 149) at the same pitch, as at 375.
harmOctLink = #(define-music-function (m) (ly:music?) #{ \set PianoStaff.midiMaximumVolume = #0.6 \transposition c'' #m \transposition c' \unset PianoStaff.midiMaximumVolume #})
linkHarpR = { R2.*8 | r4 \harmOctLink { b4-\flageolet } r4 | R2. | r4 \harmOctLink { b4-\flageolet } r4 | R2. | }  % c026: pedal setting printed at 141, before the entry, in Adler's letter form DCB/EFGA (PDF 112)
linkHarpL = { \once \override MultiMeasureRestText.self-alignment-X = #LEFT \once \override MultiMeasureRestText.parent-alignment-X = #LEFT R2._\markup \small "Ped.: D♯ C♯ B♮ / E♮ F♯ G♯ A♮" | R2.*7 | r4 \harmOctLink { <e gis>4-\flageolet\p^\markup \small \italic "harm." } r4 | R2. | r4 \harmOctLink { <e gis>4-\flageolet } r4 | R2. | }  % c174: 151 B1 with Vc/Cb/timpani (was E2, a fourth above the basses' B1; Casanelles PDF 274, harmonic series)
% c367: 149 and 151 the cellos rest (were pizz. E2/B2 with the basses, harp LH and timpani on the same roots): the trio's frame is harp and basses alone, as at 153-168, and the cellos' first sound after 139 is T at 169 (c037). Sebesky PDF 140 rule 7, PDF 145 Ex. 195. 'arco' at 169 removed: the cellos last played arco (133-139).
linkVc = { R2.*12 | }
linkCb = { R2.*8 | e,,4\pp r4 r4 | R2. | b,,4 r4 r4 | R2. | }
% c045: the pedal setting at 141 printed below the harp's LH staff, clear of the barline between the two harp staves (MOLA PDF 8, Example 7).

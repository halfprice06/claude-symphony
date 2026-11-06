% INTRODUCTION, bars 1-12 (Allegro vivace). After a pause following movement II.
% 1-2: Hn 1 holds G sharp 4 alone, with a fermata on bar 2 (c020): movement II's last A flat 4 (Vln II) heard again as G sharp, the third of E major (cyclic-notes "Four movements").
% 3-6: the horn call of movement I (E flat 3-C 4-B 3, 3-1-7, rising sixth) in E major: G sharp 3-E 4-D sharp 4 (c010), left on its 7th over V (c030):
% movement I leaves the call's B unresolved (I 13-14) and the finale resolves it in major (IV 243-246); the scherzo quotes it and does not resolve it.
% 7-8: clarinets and bassoon turn the chord to E minor (G natural replaces G sharp); the bass reaches E only here (c030).
% 9-12: timpani alone: motive x (quarter, two eighths, quarter), the rhythm of the scherzo theme.
% c090: 9-10 B2-(B-B)-G2-E2 is movement II's last timpani sound, its solo answer E flat 3-C 3-A flat 2 (II 84-85, the falling triad 5-3-1), a major third lower
%   (A flat -> E, the key relation of II and III); II's C and A flat drums are retuned in the pause to this G and E. The finale's timpani
%   take motive x a major third lower again (IV 143-145, on G). Not literal (rhythm motive x, not II's 4. 8 4): keep the pitches B-G-E at 9-10 so the chain holds.

% c040: 7-8 Cl 1 E5 above Cl 2 G4 (was G4 over E4): the horn call's D sharp 4 (5-6) is no longer taken to E4 at its own pitch a beat later, and movement II's last
%   clarinet E flat 4 (Cl 2, II 89-92) is not answered by Cl 2's E4; the E flat/D sharp -> E thread at E4 stays open for the finale (Hn 3 and violas, IV 219-220).
%   As in movement I (I 13-15), the call's 7th meets the tonic only in another octave (Adler II PDF 188: register changes what a line is heard to do).
introClOne = { R2.*6 | e''2.~\pp | e''2\> r4\! | R2.*4 | }
introClTwo = { R2.*6 | g'2.~\pp | g'2\> r4\! | R2.*4 | }
% c090: Bsn 1 holds B3 from 4 to 8 (was Hn 2 at 4-7, Bsn 1 from 7): the horn call is a single horn line, as movement I has it (I 13-14: Hn 2-4 rest) and as the
%   motto tail at 357-360 is (c060). Adler II PDF 264 (Mozart, Horn Concerto No. 2: the orchestral horns never play while the solo horn plays) and PDF 274 (Beethoven,
%   Violin Concerto iii: the bassoon's middle register set against the solo); the B is common to E major (4-6) and E minor (7-8), so one bassoon note carries both.
% c150: Bsn 1 enters pp, a level under the horn call's p (bar 4), and holds it: a second colour added at the solo's level on the solo's diminuendo thickens the call
%   where it should thin (Rimsky-Korsakov PDF 127: a group added for a crescendo enters pp; the diminuendo works by taking colours away); c099's one-level rule.
% c160: the horn call sounds over a low dominant pedal, as in movement I (I 13-14: Hn 1 E flat 3-C 4-B 3 over Bsn 2 G2, below the call's lowest note):
%   Bsn 2 holds B2 from 4 (was Bsn 1 B3, a fourth under the call's E4 and inside its range G sharp 3-E4); Bsn 1 adds B3 at 7 with the clarinets' E minor.
%   Sebesky PDF 12-13 (Ex. 1: the line in the lower-middle register taken out so the primary element stands out), PDF 13-14 (focus). Pitch classes unchanged.
introBsnOne = { R2.*6 | b2.~-\tag #'score ^\pp -\tag #'part \pp | b2\> r4\! | R2.*4 | }  % c235: Bsn 1 pp above the shared staff: Bsn 2 holds its B2 from 4, so a pp below read as a second pp for Bsn 2; the part keeps it below (Adler II PDF 294, 301 Ex. XVIII-10a)
introBsnTwo = { R2.*3 | b,2.~\pp^\markup \bold "2." | b,2.~ | b,2.~ | b,2.~ | b,2\> r4\! | R2.*4 | }
% c088: 3-6 the horn call under one slur, as movement I quotes it (I 13-14 es4( c'2~ c'4 b2)); Adler I PDF 309: a phrase under one slur is one breath and soft-tongued (Ex. X-8, X-9, X-11 horn solos slurred by phrase). Notes unchanged.
introHnOne = { gis'2.~\pp | gis'2. | gis2.(\<^\markup \italic "espress." | e'2.\p\> | dis'2.~ | dis'2)\! r4 | R2.*6 | }  % c030: the call stops on its 7th (D sharp 4) over V, unresolved, as movement I's call stops on B 3 (I 13-14); the finale resolves this D sharp 4 at its own pitch in Hn 3 (IV 219-220) and brings the call back in major at IV 243-246 (c360: the comment named only 243-246)  % c010: the horn call keeps movement I's rising sixth (3 up to 1): G sharp 3 -> E 4, after the pivot G sharp 4 (1-2)  % c388: 'espress.' at 3, the start of the call (Adler PDF 304-305, 309: every horn solo example carries a character word; Ex. X-11 pp ... expressif)
% c430: 1-2 Vln I hold G sharp 5 ppp an octave above Hn 1 and stop with it at the fermata, so the movement starts with the sound it ends with
%   (Hn 1 G sharp 4 + Vln I G sharp 5, 368-376) and the finale takes over in the same players (IV 1: Hn 1 A flat 4, Vln I A flat 5).
%   Casanelles PDF 215, 224-225: one specific sound tied to one meaning (here the G sharp = A flat pivot); PDF 222: shared material at its
%   finished state makes a work sound "composed by a single person". The horn call (3-6) stays a single horn line (c090).
% c470: 7-8 Vln I G5 pp on top of the clarinets' E-minor chord: the violins' G sharp 5 of 1-2 becomes G5 in the same voice and octave, so the
% change of mode G sharp -> G natural (3 of E in both forms) is heard as one line (A&S PDF 387: two tones for one degree, "dramatic juxtaposition";
% PDF 394, Ex. 23-12b: a chromatic succession in one voice). Mendelssohn's E-major overture (A&S Ex. 23-1a, PDF 386) gives its turn to E minor to
% the violins, pp, who then play the minor theme, as Vln I does here at 13; the G5 is also the first note of theme A's tail at 14. It mirrors the
% finale's Vln I A flat 5 -> G5 at IV 1-2 as Cl 2's G4 mirrors Hn 1's A flat 4 -> G4 (c270), and movement I's G sharp 5 (Cl 1, I 78) -> G5 (Vln I, I 79). Cl 2 G4 and no E4 at 7-8 unchanged (c040, c270). Cautionary natural: the player held G sharp 5 four bars earlier.
% c499 (lens 9; Casanelles PDF 271-272, Fig. 6.1, Mahler 1/i 17-25: the call sounds over a sustained high pp string pedal, the static layer that places it;
%   PDF 280: the sustained string section as the smooth, static pad; A&S PDF 367 sec. 28 and PDF 415, Ex. 24-25 Chopin op. 56/3: a top-voice pedal, the major 3rd held
%   while the lower voices move; Rimsky-Korsakov PDF 84: upper pedal notes are more effective in the orchestra): 3-6 Vln I holds its G sharp 5 ppp through the horn call
%   (was a rest after the fermata) and moves straight to G natural at 7 under one slur, so c470's G sharp -> G change of mode is one unbroken line. Consonant with every
%   note of the call (3rd, 6th, 5th above D sharp 4); no new pitch; Hn 1 still plays the call alone among the horns (c090).
introVlnOne = { gis''2.~\ppp^\markup \italic "senza sord." | gis''2.~ | gis''2.~^\markup \italic "change bow freely" | gis''2.~ | gis''2.~ | gis''2.( | g''!2.~)\pp | g''2\> r4\! | R2.*4 | }  % c442: movement II (v469) ends with violins and violas con sord. (II 84-92); the mutes come off in the pause, so the first entry is marked (Adler II PDF 312: senza sordino = the state at the entry), as Hn 3-4 at 73
introHnTwo = { R2.*12 | }  % c090: rests (its B3 of 4-7, c010, moves to Bsn 1): Hn 1 plays the call alone
introTimp = { << R2.*2 { s2.^\markup \small \column { "Timpani: E, G, B, E" "(retune in the pause: A♭ → E, C → G, D♭ → B, E♭ → E)" \italic "hard sticks" } s2. } >> | e,4\pp r4 r4 | R2.*5 | b,4\p b,8 b,8 g,4 | e,4 r4 r4 | b,4 b,8 b,8 e4 | e,4 r4 r4 | }
introVc = { R2.*2 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | e,4 r4 r4 | R2.*5 | }  % c030: the tonic E comes with the E-minor chord (7), so 5-6 stay on V under the horn's D sharp
% composer (2026-10-19): "tutti pizz." because movement II v255 ends with "4 soli" basses (request from the movement II thread)
introCb = { R2.*2 | e,,4\pp^\markup \italic \column { "tutti" "pizz." } r4 r4 | R2. | b,,4 r4 r4 | R2. | e,,4 r4 r4 | R2.*5 | }
% c116: the harp's starting pedal setting at bar 1, in the score and the part, like the timpani's tuning label (Adler part 1 PDF 112: "indicate how the pedals
%   should be set at the beginning of a work", letter form D C B / E F G A). The harp ends movement II on D flat C B flat / E flat F G A flat, so the pause
%   brings D (left foot), E and A (right foot). Not a "Ped." text, so the part keeps it (parts-lib partCleanHarp drops only pedal-change letters, MOLA PDF 5).
introHarpL = { \once \override MultiMeasureRestText.self-alignment-X = #LEFT \once \override MultiMeasureRestText.parent-alignment-X = #LEFT R2._\markup \small \line { \italic "set pedals in the pause:" "D♮ C♮ B♭ / E♮ F♮ G♮ A♮" } | R2.*11 | }

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
introBsnOne = { R2.*3 | b2.~\p\> | b2.~ | b2.~\pp | b2.~ | b2\> r4\! | R2.*4 | }
% c088: 3-6 the horn call under one slur, as movement I quotes it (I 13-14 es4( c'2~ c'4 b2)); Adler I PDF 309: a phrase under one slur is one breath and soft-tongued (Ex. X-8, X-9, X-11 horn solos slurred by phrase). Notes unchanged.
introHnOne = { gis'2.~\pp | gis'2. | gis2.(\< | e'2.\p\> | dis'2.~ | dis'2)\! r4 | R2.*6 | }  % c030: the call stops on its 7th (D sharp 4) over V, unresolved, as movement I's call stops on B 3 (I 13-14); its resolution in major is the finale's (243-246)  % c010: the horn call keeps movement I's rising sixth (3 up to 1): G sharp 3 -> E 4, after the pivot G sharp 4 (1-2)
introHnTwo = { R2.*12 | }  % c090: rests (its B3 of 4-7, c010, moves to Bsn 1): Hn 1 plays the call alone
introTimp = { << R2.*2 { s2.^\markup \small \column { "Timpani: E, G, B, E" "(retune in the pause: A♭ → E, C → G, D♭ → B, E♭ → E)" \italic "hard sticks" } s2. } >> | e,4\pp r4 r4 | R2.*5 | b,4\p b,8 b,8 g,4 | e,4 r4 r4 | b,4 b,8 b,8 e4 | e,4 r4 r4 | }
introVc = { R2.*2 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | e,4 r4 r4 | R2.*5 | }  % c030: the tonic E comes with the E-minor chord (7), so 5-6 stay on V under the horn's D sharp
introCb = { R2.*2 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | R2. | e,,4 r4 r4 | R2.*5 | }

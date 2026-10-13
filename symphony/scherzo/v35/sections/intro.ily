% INTRODUCTION, bars 1-12 (Allegro vivace). After a pause following movement II.
% 1-2: Hn 1 holds G sharp 4 alone, with a fermata on bar 2 (c020): movement II's last A flat 4 (Vln II) heard again as G sharp, the third of E major (cyclic-notes "Four movements").
% 3-6: the horn call of movement I (E flat 3-C 4-B 3, 3-1-7, rising sixth) in E major: G sharp 3-E 4-D sharp 4 (c010), left on its 7th over V (c030):
% movement I leaves the call's B unresolved (I 13-14) and the finale resolves it in major (IV 243-246); the scherzo quotes it and does not resolve it.
% 7-8: clarinets and bassoon turn the chord to E minor (G natural replaces G sharp); the bass reaches E only here (c030).
% 9-12: timpani alone: motive x (quarter, two eighths, quarter), the rhythm of the scherzo theme (a melodic timpani figure, still unused in I and II).

introClOne = { R2.*6 | g'2.~\pp | g'2 r4 | R2.*4 | }
introClTwo = { R2.*6 | e'2.~\pp | e'2 r4 | R2.*4 | }
introBsnOne = { R2.*6 | b2.~\pp | b2 r4 | R2.*4 | }
introHnOne = { gis'2.~\pp | gis'2. | gis2.\< | e'2.\p\> | dis'2.~ | dis'2\! r4 | R2.*6 | }  % c030: the call stops on its 7th (D sharp 4) over V, unresolved, as movement I's call stops on B 3 (I 13-14); its resolution in major is the finale's (243-246)  % c010: the horn call keeps movement I's rising sixth (3 up to 1): G sharp 3 -> E 4, after the pivot G sharp 4 (1-2)
introHnTwo = { R2.*3 | b2.~\p\> | b2.~ | b2.~\! | b2 r4 | R2.*5 | }  % c010: enters with Hn 1's E4 at 4 (no crossing under Hn 1's G sharp 3 at 3)
introTimp = { << R2.*2 { s2.^\markup \small \column { "Timpani: E, G, B, E" "(retune in the pause: A♭ → E, C → G, D♭ → B, E♭ → E)" \italic "hard sticks" } s2. } >> | e,4\pp r4 r4 | R2.*5 | b,4\p b,8 b,8 g,4 | e,4 r4 r4 | b,4 b,8 b,8 e4 | e,4 r4 r4 | }
introVc = { R2.*2 | e,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,4 r4 r4 | R2. | e,4 r4 r4 | R2.*5 | }  % c030: the tonic E comes with the E-minor chord (7), so 5-6 stay on V under the horn's D sharp
introCb = { R2.*2 | e,,4\pp^\markup \italic "pizz." r4 r4 | R2. | b,,4 r4 r4 | R2. | e,,4 r4 r4 | R2.*5 | }

# Movement I (Allegro, C minor): current state for the other movement threads

Owner: the movement I thread ("Movement I, loops from v401" since 2026-10-26 20:56 UTC; "Movement I, loops from v300" from 2026-10-19 21:30 UTC; before that "Movement I, 200 more loops"). Series 3 works from v221; this file is updated as changes are promoted. Last update: v531 (cycle 530). Series 3 is finished at v421. Series 4 (cycles 421–620 → v621, thread "Continue movement 1 loop to v621", Dan 2026-10-31) is listed under "Series 4 changes" at the end. Series 3 runs to v421 (Dan, 2026-10-25). Changes since v221 that touch other movements are listed under "Series 3 changes" at the end; facts above are corrected in place. The theme record is in [themes-mvt1.ly](themes-mvt1.ly), with its index in [themes-mvt1.md](themes-mvt1.md).

Pitch names: C4 = middle C. The double basses and contrabassoon are given at sounding pitch, as the section files write them.

## Opening (bars 1–8, Lento, crotchet = 50)

- **Bars 1–4: the motto, low and bare.** Bass clarinet and cellos play it in unison, with the double basses an octave lower, pp with small swells: pickup G2 on beat 4 of bar 1, then E♭3 (dotted minim tied to a quaver), D3 (quaver), C3 (minim), D♭3, C3 tied into a semibreve C3 at 4. Pitches G–E♭–D–C–D♭–C.
- Under it, timpani roll C3 ppp, bars 1–4, fading through bar 4 with the motto (since v420; no closing stroke). The first-bar label is "Timp. in G, A♭, C, E♭ / soft sticks".
- **Bar 5:** double basses hold C2 pp alone. The cor anglais enters on beat 4, p espressivo, with the motto a fifth higher: D4 | B♭4–A4 | G4–A♭4–G4 | G4. The G is held until beat 3 of bar 9.
- **Bars 6–8: strings pp.**
  - Bar 6: E♭ major over G. Double basses G2 (unison since v230), cellos G3, violas B♭3, Vln II E♭4.
  - Bar 7: D♭ major over F, the Neapolitan sixth. Basses F2 (unison since v230), cellos A♭3, violas D♭4, Vln II F4.
  - Bar 8: C major. Basses C2, cellos G3, violas C4, Vln II E♮4, with the cor anglais on G4.
  - Hairpins: < at 7, p > at 8. Vln II's E♮4 at 8 turns to E♭4 at 9.
- Violins I, flutes, oboes, clarinets, bassoons, horns, trumpets, trombones and tuba are silent in 1–8.

## Ending (bars 175–182)

**Tempo.** Più lento (crotchet = 72) from 171; rit. 177–178; Tempo I (Lento, crotchet = 50) from 179; fermata on 182.

**Bars 175–179.**
- The trombone chorale, pp dolce: Tbn 1 G3–E♭4–D4–C4/D♭4–C4, Tbn 2 E♭3–G3–F3–G3/F3–E♭3, bass trombone G2–E♭3–D3–C3/D♭3–C3. The bass clarinet and cellos double the bass trombone, and the double basses play it an octave lower.
- Tam-tam pp, soft stick, at 175, left to ring and damped at the end of 182 (since v277).
- Cl 1, pp: E♭4 on beat 4 of 175, C5 at 176–177, B4 at 177, left unresolved.
- Vln II and violas hold the inner parts, pp.
- Vln I enters with the last motto at beat 4 of 177, pp: G4 | E♭5 | (E♭5) D5 | C5 D♭5 | C5 | C5, diminuendo to ppp.
- The timpani play the first group's pulse `c4 r8 g,8 c4 r4`, pp, at 179–180, then roll C3 ppp at 181–182.
- Tbn 1 breathes after 179, restrikes C4 at 180 and stops on beat 1 of 181, ppp. Tbn 2, bass trombone and bass clarinet stop at the end of 179.

**Last chord (182), bottom to top, ppp, under a fermata:**

| Note | Instruments |
|---|---|
| C2 | double basses; harp |
| G2 | harp |
| C3 | cellos; harp; timpani roll |
| G3 | Horn 4 |
| C4 | Horn 3 |
| E4 | violas (the only E♮; they hold E♭4 at 179–181, morendo, and change to E♮ at 182) |
| G4 | Violins II |
| C5 | Violins I |

Horns 3 and 4 enter ppp at 181. The harp chord C2–G2–C3 sounds only at 182.

**Into movement II.**
- Five parts cross into movement II, written as a fermata with \laissezVibrer: Vln I C5, Vln II G4, violas E4, cellos C3 and Horn 3 C4.
- The double basses, Horn 4, timpani, harp and tam-tam release at the end of 182 (the tam-tam is damped there since v277). The harp is marked "étouffez" on beat 4 of 182, so it damps with the basses and timpani.
- The final barline is a thin double bar.
- "attacca" is printed at the end: in the score as a text end mark on Vln I, and in every part through partGlobal in parts-gen.py.

## Key plan and rehearsal marks

Key signatures are set in global.ily. Areas without a key signature of their own come from the section files' harmony.

| Bars | Mark | Section | Key |
|---|---|---|---|
| 1–14 | | Introduction (Lento) | C minor. Motto 1–8. Rising-sixth chain 9–13: i – iv – iiø7 – German sixth (12) – V (13). Horn call over V at 13–14. |
| 15–32 | A | First theme P (Allegro appassionato) | C minor. Stop chord vii°7 at 26 resolves to i at 27. Hammered ff tutti 27–32. |
| 33–46 | B | Transition | From C minor to V of A♭: four-horn call 41–42, V4/2 – I6 of A♭ at 44–45. |
| 47–68 | C | Second theme S (Poco meno mosso) | A♭ major (key signature). Peak 64. Bass G♭–F♭–E♭ at 60–62 (iv6 over F♭ at 61) into the cadential 6/4 at 62. Deceptive cadence to F minor at 68. |
| 69–76 | D | Codetta and flute motto | A♭ major, f, 69–72: I–I6 \| ii7–vii°7/V \| V7 \| I. Flute motto 73–76 over an A♭ pedal, darkened to A♭ minor (F♭, mixture iv6/4 at 76). |
| 77–96 | E | Development: head dialogue and fugato | C minor key signature. Head in A♭ minor (77), E minor (78–79), C minor (80–81); ff over A♭ at 82. Fugato entries on D (Vc 85), G (Vla 88), C (Vln II and C.a. 91), F (Vln I 94); chain G–C–F–B♭, ending in B♭ minor. |
| 97–102 | F | S in B minor, ff | B minor (key signature): the fugato's B♭ minor shifted up a semitone. |
| 103–110 | | Both heads combined | A minor key signature. D minor → V of E minor (103–106, f); E minor → B♭ minor → cadential 6/4 and V of F minor (107–110, p). |
| 111–116 | | Wedge | C minor key signature; F minor at 111, the S-head rhythm rising to Vln I's D6 at 116, into the dominant pedal. |
| 117–130 | G | Dominant pedal and retransition | G pedal. Trombone motto, second form, 117–121. Climax fff 122 (A♭ over G). Collapse 123–126. Stretto of the half-augmented motto 127–130. |
| 131–146 | H | Recapitulation, first group | C minor. Stop chord at 138 (bass D). F minor at 139. A♭6 (Fl 1) over a D♭ bass at 140. |
| 147–157 | J | Recapitulation, second group (Poco meno mosso) | C major (key signature). S head 147–150; ♭VII at 156. |
| 158–166 | K | Climax and dissolution | C major. ♭VI (A♭ bass) at 160, fff. E♮→E♭ in the violas at 166. |
| 167–170 | L | Coda, forte (Tempo dell'Allegro) | C minor (key signature). Head in the brass over a C pedal. Stop chord over C at 170, fermata. |
| 171–182 | M | Coda, soft (Più lento, then Tempo I) | C minor. 171–174: i – iv – Neapolitan sixth – cadential 6/4 – V. 175–179: chorale over the motto bass. Ends on C major (violas' E♮ at 182). |

## Timpani tunings

| Bars | Tuning or change |
|---|---|
| 1 | G2, A♭2, C3, E♭3 (label "Timp. in G, A♭, C, E♭"). Medium sticks from 15. |
| 34 | "muta A♭ in B♭". B♭2 roll at 40; E♭3 roll at 41–43. |
| 44 | "muta B♭ in A♭" |
| 84 | "muta A♭ in B♮". A single B2 stroke at 97 (B minor). |
| 98 | "muta B♮ in A♭" (since v297; was at 111). From here to the end: G, A♭, C, E♭. |
| 175 | "soft sticks" marked (after the G2 roll at 174). The last bars (179–182) use only C3 and G2. |

The C drum stays on C for the whole movement. All retunings use the A♭ drum. Movement I ends tuned G, A♭, C, E♭.

## Tempo markings and duration

| Bars | Marking |
|---|---|
| 1 | Lento, crotchet = 50 |
| 15 | Allegro appassionato, crotchet = 126 |
| 45–46 | poco rit. |
| 47 | Poco meno mosso, crotchet = 112 |
| 62–63 | poco animando |
| 66–68.2 | rit. |
| 68 (beat 3) | Tempo dell'Allegro, crotchet = 126 (since v369; mark D stays at 69) |
| 121–122 | allargando |
| 123–126 | sostenuto |
| 127 | a tempo |
| 145–146 | poco rit. |
| 147 | Poco meno mosso, crotchet = 112 |
| 156–157 | poco animando |
| 160–164 | largamente (holds until the rit. at 165; critic 488) |
| 165–166 | rit. |
| 167 | Tempo dell'Allegro, crotchet = 126 (fermata at 170) |
| 171 | Più lento, crotchet = 72 |
| 177–178 | rit. |
| 179 | Tempo I (Lento), crotchet = 50 (fermata at 182) |

Duration: v221's full.midi lasts 430.8 s, about 7:11. The score's front page says "c. 7½ minutes".

## Climax hierarchy

There are three climaxes on A♭, rising in strength:

1. **Bar 82, ff.** First-theme head in tutti over an A♭ bass (double basses repeat A♭1 in quavers). The top is E♭6 (Fl 1, Vln I). Since v305 the held brass are f under the ff head, with ff strokes at 83; since v309 Tpt 2 rests at 82 and enters on the strokes at 83; since v345 Bsn 1 doubles the violas' lowest octave of the head.
2. **Bar 122, fff.** A♭6 in Vln I (tremolo) and Fl 1 over the G pedal (A♭ as the minor ninth of V). Since v445 the cellos tremolo A♭3–G3 with the upper strings at 122–123 (double basses hold G1 untremoloed), so 122 is a full-string fff tremolo; it differs from IV 223 in harmony (V♭9 over G), top note (A♭6), percussion (tam-tam) and the absence of the trumpets' B→C. The upper parts fade from 123 (since v319), the pedal parts from 124. Tam-tam fff (heavy beater) 122, diminuendo from 124 ("damp gradually") to p at 126, damped at 127 (since v229). It arrives from the trombone motto at 117–121.
3. **Bar 160, fff.** A♭6 in Vln I and Fl 1·2, with Vln II and Ob 2 an octave lower (Vln II since v230; Ob 2 since v242, when Ob 1 moved to the countermelody with Cl 1) over an A♭ bass (♭VI). Suspended-cymbal roll at 159 ending in one soft-stick suspended-cymbal stroke fff l.v. at 160 (since v251; until v250 a crash), tied through 163 and damped at 164 (since v277); since v329 it is shaded ('damp gradually', diminuendo 162 to p at 163). Movement I has no clashed cymbals. Since v408 Cl 2 joins Ob 1 and Cl 1 on the counter at 158–159 (G5–C6 | B5–F5, a2 with Cl 1) and plays E♭5 from 160.1 (was E5 | D5 | C5); the counter is Ob 1 + Cl 1·2 over Hn 3·4.

The fff marks are at 122 and 160 only.

The A♭6 peaks:
- Vln I reaches A♭6 at 31, 72, 122 and 160. Fl 1 doubles it at each of these, Fl 2 at 72 and 160. Vln II never reaches A♭6 (since v258 its highest note is C6, the tremolo at 152).
- At 140, Fl 1 reaches A♭6 alone (Vln I is an octave lower) over a D♭ bass.
- No violin note in movement I is higher than A♭6. The violins never reach C7.

## Brass use

**Trumpets.**
- Where they play: 26–33, the sf quaver at 41, 69–72 (Tpt 1 has the S head at f with Ob 1 and the flutes), 82–83, 113–116, 122–123, 131–134, 138–143 (Tpt 3 to 142; the stop chord at 138 is a fresh trumpet entry, as at 26), 158–162 and 167–170.
- Tpt 1 moves B4→C5 into the minor tuttis at 26→27, 28→29 (over the E♭ bass, i6) and 138→139, and at forte also at 161→162 (C5 held through 162, ff, over A1: V7–vi) and inside the P head at 168 (Tpt 1·2). It plays B4–C5 softly at 113. None of these lands on a C-major chord; the finale's 222→223 is the first.
- Tbn 1 B3→C4 at 159→160 (into ♭VI, fff; since v375) and 161→162.
- Their last note is at 170: Tpt 1·2 accented B♮4 under the fermata, unresolved; Tpt 3 F4. They are silent 171–182.
- There is no trumpet solo and no soft trumpet melody.

**Horns.**
- Hn 1 alone plays the horn call E♭3–C4–B3 at 13–14. This is the only undoubled horn melody, and its B is unresolved.
- All four horns play E♭3–C4–B♭3 at 41–42.
- Hn 1 plays the S head with the cellos at 46–52, with Bsn 1 and the cellos at 103–106, and with the violas at 146–150.
- Hn 1·2 play the P head at 69–72 and 167–169, ending on B3 at 170. They join the second form of the motto at 117–121 and the climax line at 158–161.
- Hn 3·4 end ppp on C4 and G3 at 181–182. Hn 3 crosses into movement II.

**Trombones.**
- They play held chords in the tuttis, the P head (low) at 131–134, and the motto's second form ff at 117–121.
- The pp chorale with tam-tam is at 175–179. Tbn 1 continues to beat 1 of 181.
- At 175–179 Tbn 1 and the bass trombone double the motto in octaves.

**Tuba.** It plays only the bass, never a melody. Its highest note is F2. Its last note is C2 at 170.

**Not used anywhere in movement I:** muted or stopped brass, a high four-horn unison (movement I has horn pairs in unison at 158–161, Hn 3·4 to C5 and Hn 1·2 on A♭4 at 160; its only four-horn unison is the low call at 41–42), a full low-brass unison in the bass, the falling major motto in full brass at forte (G–E–D–C appears only at mp–mf in Hn 1/violas/cellos at 147–150), and a root-position C-major chord in the full brass at forte. Bar 158 has the full brass ff on the cadential 6/4 of C over the G pedal (Tpt 1 E5, Tpt 2 G4, Tpt 3 C4, Hn 1·2 E4, Hn 3·4 G4/C5, Tbn 1 C4, Tbn 2 G3, B.tbn G2, tuba G1); it goes to V7 at 159 and is cut off by ♭VI at 160, so C is never reached.

## Do not reuse: kept for the finale (from cyclic-notes.md, checked against v221)

These are reserved for the finale. The other movements should not use them. Their state in v221:

- **The trumpets' B→C on the C-major arrival, resolving the stop chord B–D–F–A♭.**
  - In v221 the stop chord is at 26 (bass B), 138 (bass D) and 170 (over C, fermata). It goes to C minor at 27 and to F minor at 139.
  - Tpt 1·2 end on B4 at 170.
- **String tremolo with the violins' C7.**
  - The violins never reach C7.
  - String tremolo is used in movement I. Movement II held it back except at 61–64, so in the finale it belongs to the arrival.
- **The falling major motto G–E–D–C in full brass at forte.** It is not in v221.
- **The brass chorale in major, f–ff, with trumpets and horns, no tam-tam, and an independent bass.** v221 has only the pp minor chorale at 175–179.
- **The violins' C-major statement of the S head with its chromatic counter over a C pedal.**
  - It is not in v221.
  - `recTwoMelodyA` in v221/sections/recTwo.ily is unused and lacks its pickup.
  - The complete version is in v99/sections/recTwo.ily and in themes-mvt1.ly (mvtOneWithheld*).
- **A fast ff full-brass combination of the two heads in C major.** v221 combines them only at f in A♭ (69–72) and at f/p in minor keys (103–110).
  - Met in the finale (v71, 247–254): Tbn 1·2 on the first-theme head under the trumpets' second-theme head.
- **The hammered tutti layout turned to major.** In v221 it is heard only in C minor with the P head: 27–32, 131–134 and 167–170.
- **The horn call in major (E–C–B→C) in the trumpets.** v221 has it only in minor, in Hn 1 (13–14) and Cl 1 (175–177).
- **The timpani pulse `c4 r8 g,8 c4 r4`.** It is at 179–180 in v221 and is unused in movement II.
- **Closing the E♭/E♮ thread in the violas.** v221 ends on the violas' E♮ at 182 without closing it, and movement II turns it back to E♭.
- **A tuba melody, a high four-horn unison (movement I has horn pairs in unison at 158–161, Hn 3·4 to C5 and Hn 1·2 on A♭4 at 160; its only four-horn unison is the low call at 41–42), a full low-brass unison in the bass, and the first cymbal crash of the finale.** None of them is in v221. Since v251 it has no clashed cymbals at all (bar 160 is a suspended-cymbal stroke), so the finale's crash at 223 is the first in the symphony.
- **C major as a key in movements II and III** (the scherzo is told not to use it). Movement I has C major only softly (147–166, and as V of F minor at 110), never confirmed at forte.
- **D♭ as a key in C, ♭VI moving to ♭II in C, and a theme restated on ♭II** (added at cycle 300). Movement I has none of them: its ♭II is always a chord (structural N6 → V at 20–22, 140–143, 172–174; neighbour D♭s inside the tonic at 3, 7→8, 178, 180). Bar 115 is a one-bar ff root-position D♭ chord over a passing bass, not a key. Movements II and IV already use these.

## Series 3 changes (v221 → current)

- v223: Hn 3 B3→C4 at 165–166 (leading tone resolves; was B3→G3). Vc D3 tied at 145 (was B2). Vln II G4 on beat 4 of 46.
- v225: hammered tutti inner brass at 28–31 no longer double the bass (Tpt 2 G4 at 28 beat 1 and F4 on beat 3 since v303, as at 132; B♭4 at 30; Tpt 3 F4 F4 G4 A♭4–F4 at 28–31; Hn 2 G4 at 30). The finale follows this at its 199–204. Cl 1 F4 at 145–146.
- v226: stems on the middle line follow their neighbours (engraving only).
- v227: Vln I bowing 11–13; Vc pizz. cut on beat 3 of 63; Vln II "unis." at beat 3 of 73.
- v228: Vln II and violas enter after the P pickup at 15 and 17; double basses rest 85–89 (fugato subject alone); violas 156–157 re-voiced.
- v229: tam-tam fades 124–126; brass crescendo into 41 and 122; Cl 1 B4 at 177 fades.
- v230: Vln II an octave below Vln I at 158–161; double basses unison G2/F2 at 6–7.
- Unchanged so far: the motto, P and S heads, horn call 13–14, stop chords, coda 171–182 notes, the last chord and the five tied parts, timpani tunings and the timpani pulse 179–180, the "Do not reuse" list.
- v231: Cl 1 at 78 takes the A♭5 common tone as G♯5 for one beat over the E-major chord (was A♭5 held against the horns' G4).
- v232: cellos double the S tune with Vln II and the cor anglais at 97.4–102 (the bass stays in Cb, Cbsn, B.cl, Bsn 2, B.tbn).
- v233: the cadential 4–3s at 66→67 and 164→165 are tied over the barline and resolve on the second eighth; Hn 3 B3 on beat 2 of 165; harp G5–D6–F6 at 165.
- v234–v239: brass voicing at 40, 72 (Tbn 1 E♭4, Tbn 2 C4), 166 (Hn 4 G3); beam slopes; fugato free voice in violas/Bsn 1 at 94–95; portato dash on the P head's repeated C (c4--) at 16, 28, 132, 144, 168 and similar figures; bowing marks at 34–41, 69–71, 139, 158–162.
- v240–v251: oboes swap lines at 158–163 (Ob 1 with Cl 1 on the countermelody, Ob 2 on the tune's middle octave); bass D at 25 beat 4 (iv – iiø7 – vii°7 into the stop chord); Tpt 1 B4 at 133; held brass ff under the fff tune at 160; rest positions and no 8va in the Vln I part; harp étouffez at 68 and B pedal left on B♭; violas G3 at 144–146; Vln II G4 at 175–176 (was E♭4); hairpins on the ff S at 97–102; v251: no clashed cymbals (suspended-cymbal stroke at 160).
- v252–v256: cellos sul G for the motto at 1–3 and 175–178; Vln I sul D for the last motto at 177–182 (movement II continues "(sul D)" over the tied C5 to its bar 4; keep both); Cl 1 A♭4–G4 at 164; trombones p< into the sf at 41; bar 82 Fl 2 with Fl 1 on top and Cl 2 with Cl 1 on the head.
- v257–v261: part-combine fixes; Cbsn breath at 134; Vc at 91; Vln II tremolo C6 halo at 152; swells at 56–57; fade at 13; Hn 4 breathes on beat 4 of 25. Harp reaches D♭7 at 57–59 (C7 at 56). Nothing another movement quotes changed.
- v262–v270: viola A♭3 falls to G3 on beat 4 of 177 (i6 – V4/3 – i under the chorale); Bsn 1 B♭3 at 37 (E♭-minor seventh complete, four real parts); violas, Hn 3·4 and the off-beat dyads f at 131–134 (were ff); Vln II, Vla, Vc, Cb mp at 144 under Bsn 1's answer; C.a. with Vln II 94–95, Cl 1 from 96; tuba breathes after 121, Hn 3 on beat 4 of 123; tenutos on the S climax's E6 (158) and A♭6 (160) in every part with the tune; one solo cello at 171–174, Tutti at 175. Nothing another movement quotes changed; the five tied parts, the chorale top line, the timpani pulse and the last chord are unchanged.
- v272–v280: A♭ held at 116 in Ob 2, Cl 1, Hn 1, Tbn 2, Vln II (no A♮); viola A♭3 at 51 (V6/5 of IV); bass G♭ through 60 (G♭–F♭–E♭ at 60–62); Cl 1 takes the link into S at 45–46 and the oboes rest 44–68; suspended cymbal tied 160–163 and damped at 164, tam-tam damped at the end of 182; violas rest 56–59 (the counterline keeps their E♭4–E4–F4); Vc/Cb mf at 15–22; B.cl mf at 103; Ob 2 accents at 142; Vln I 'pp espr.' at 177. Nothing another movement quotes changed; the five tied parts, the chorale top line, the timpani pulse and the last chord are unchanged; theme record 35/35.
- v282–v290: cellos G3–A♭3 at 45 (Cl 1's 7–6 B♭–A♭ is not anticipated); Hn 4 F♯3 with Hn 3 on the German sixth at 12 (was A♭2 on the bass; the chord's pitch classes are unchanged); Tpt 2 E♭4 on the ff stroke at 33 (was G4), as at 143; Hn 3 holds B3 at 122–124 (was D4 at 122–123) and resolves to C4 at 125 in the i6/4 over the G pedal; Vc and Bsn 1 hold C3 at 143 (was C3–D3); accents on C–B at 142 in Hn 3, Tpt 3 and Tbn 1; Bsn 2/Cbsn diminuendo from the note at 125; cello tenor clef before the pickup at 97; Fl 1 joins the violins' octave at 100 (8va at 97–99 only). Nothing another movement quotes changed: 27–32, the stop chords 26/138/170, the coda 167–182, the five tied parts, the timpani pulse and the last chord are unchanged; theme record 35/35 against v290.
- v292–v301: inner voices (Vla, Cl 2) follow the motto E♭–D–D♭–C at 119–120; Vln II and violas clear the Vln I pickup into P at 19, 37 and 143 (rhythm only); part cues and multi-bar rest layout (MOLA); timpani 'muta B♮ in A♭' at 98; Hn 1·2 enter on beat 3 of 24 (the hemiola's third cell); Cl 1 'dolce' and diminuendo at 45–46, 'espr.' at 175. Cellos stay at pitch at 101–102. v303: Tpt 2 F4 on beat 3 of 28 (was G4; vii°6/5 over D; at 132 the same pitches embellish V over G). v305: held brass f at 82 (strokes ff at 83); Hn 4 G3 at 23.4–24.2 (was G2). v307: Ob 2 rests from beat 3 of 42. v309: horn call 13–14 marked '1. Solo', 'espr.' (notes and dynamics unchanged); B.tbn and tuba f at 131; Tpt 2 rests at 82. v313–v319 (inner parts and notation only; nothing another movement quotes): Vln II E♭5 held through 54 and violas A♭3/C4 at 55; Vln II C5/B♭5 at 151; bassoons uncrossed at 156–166; cellos in bass clef 146–155; bow changes at 12 (Vln II, Cb) and 'change bow at will' for the violas' E4 at 181–182 into movement II; Tbn 2 doubles the tenor line at 139–142 (139–141 since v415, G3 at 142 as at 32); upper parts fade from 123; Cl 1 tenuto at 45; v320: Tbn 1 C4–B3–A♭3, Tbn 2 G3–F3–F♯3 at 113–116 (lines swapped, low line up an octave). Nothing another movement quotes changed: 27–32, the stop chords, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.

- v322–v331: Vln I·II sul D at 55.4–57.1; Tpt 3 D♭4 from 140.3 into 141 and Tbn 2 rest at 124; violas div. at 166 (thread pitches unchanged); violas enter on 144.2-and; held motto C3 fades at 4 and 179; suspended-cymbal stroke shaded 162–163; text placement at 55; v332: cor anglais doubles Cl 2 on the P head at 69–72. v333–v340: bassoons in octaves at 158–161; Vln I 8va removed at 31 and 71–72 (notation only, same pitches); harp damping at 61, 63; Cl 1 up an octave at 156–157; bowing marks at 45, 54, 143–144, 166. Nothing another movement quotes changed (MIDI diff v321→v330: three note events, none in a quoted bar).
- v342–v351: Cb "sul A" on the motto at 2–3 and 176–178 (notation); Bsn 1 doubles the violas' P head at 82; engraving at 14/15, 68/69, 123; Bsn 1·2 breathe after 159 and 163; Hn 3 rests on 104.1 and 105.3 and enters B3 on 145.3 under Bsn 1; swells on the S head 103–108. Nothing another movement quotes changed: theme record 35/35 against v350; 27–32, the stop chords 26/138/170, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v352–v361: timpani roll p< at 80 and held Hn 1·2/trumpets f (no crescendo) at 139–141 (c354); 'a2' on beat 1 of 158, Hn 4 rest hidden at 146, Vln I cue at 175–176 (c355); Hn 3·4 breathe after 22 and 39 (c356); Cl 1·2 pad from beat 2 of 35, Bsn 2 B♭2 at 41–43 (was E♭3), Hn 4 enters on beat 2 of 69 (c357); Vc/Cb pp under the p tune at 56–61, pickup slurred at 155.4 (c358); 'Cor anglais in F' / 'C.a. (F)' (c359). Nothing another movement quotes changed: theme record 35/35 against v360; 27–32, the stop chords 26/138/170, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v362–v371: Ob 2 leaves after A4 at 163 (Vln II carries the line down); 'medium sticks' printed over 25 in the score (the part keeps it at 15); percussion part 'take heavy beater' (from 117), 'take soft sticks' (from 156), 'take soft stick' (from 171), part only; violins swell from 58.4 and fade through the half cadence at 59; rit. 66–68.2 and Tempo dell'Allegro from beat 3 of 68 (mark D stays at 69). Nothing another movement quotes changed: theme record 35/35 against v370; 27–32, the stop chords 26/138/170, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v372–v381: violas take B♭3 on beat 3 of 44 with Hn 1's 7–6; Tbn 1 D4–B3 at 159, B3→C4 into the fff ♭VI at 160; 'molto cantabile' at 56, 'change bow at will' at 73, timpani muta at 84 placed for spacing; violins swell into B♭5 at 65–66; C.a. fills at 147–152 'dolce' with small swells, p. Nothing another movement quotes changed: theme record 35/35 against v380; 27–32, the stop chords 26/138/170, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v382–v391: inner parts B–B♭–A♭ by step at 115 (Ob 2, Cl 1, Hn 1, Tbn 1, Vln II; was B–A♭); Vln II halo E5/G5–D5/G5 at 154 above the violas' tune; horn breaths (Hn 4 after 58, Hn 3 after 166); accents on Vc/Bsn 1 C4–B3 at 142; Hn 4 crescendo from the tied mf of 129 to f at 131; part-only swells at 103–105 and cues. Nothing another movement quotes changed: theme record 35/35 against v390; 27–32, the stop chords 26/138/170, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v392–v401: cellos G2 on the ff strokes at 83 (was G3); Hn 4 G3 at 135–137 as at 23–25 (V6/5, was a bare diminished triad); timpani roll ends in one ff stroke at 141.1; flutes leave the fff G6/D6 after two beats at 123; Fl 1 swells into A♭5 at 73–74; cor anglais slurred at 153–155; the coda cor anglais holds D♭5 for two beats at 173 (N6), falling to C5 on the 6/4 at 174 (was D♭ for one beat); string and horn part fixes. Nothing another movement quotes changed in pitch: theme record 35/35 (the coda cor anglais line updated for rhythm); 27–32, the stop chords 26/138/170, the coda harmony 171–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v402–v411: violins leave F♭5 by skip to D♭5 on 61.4-and (was E♭5); Vln II B4→C5 at 154–155; bass D on 137.4 (was A♭), as at 25.4; Hn 1 A♭4 on 25.2–4 and 137.2–4 (was F4), held into the stop chords at 26 and 138 (layouts unchanged); Hn 3·4 score stave in bass clef 135–157 (engraving); violas double up-bow at 11, Vln II 'non div.' at 122; Cl 2 on the climax counter 158–160; Hn 3·4 and Tbn 1 f> on the restruck notes at 124; 'molto espr.' on the four-horn call at 41. Nothing another movement quotes changed: theme record 35/35 against v410; MIDI of 1–20, 26–32, 46–50, 138, 146–150 and 170–182 identical to v401; in 158–161 only Cl 2 changed.
- v412–v420: Vln I 'sul D' at 9.4–10 (as at 177); Tbn 2 G3 under the C–B strokes at 142 (as at 32; Tbn 1 keeps C4–B3); Tpt 3 hands B3 to Tbn 1 at 159.3 and strikes E♭4 fresh at 160; beam slopes on ledger-line groups and minimum stem lengths (engraving); horns p on the C-major resolution at 166 (was mp), crescendo into 167; timpani roll fades through bar 4. Nothing another movement quotes changed in pitch; the stop chords 26/138/170, 27–32, the coda notes 167–182, the five tied parts, the timpani pulse and the last chord are unchanged.
- v421 (release check): 'draft' removed from the stamp ('Full score in C — v421, 27 October 2026'); front page gives c. 7½ minutes for movement I and c. 25 minutes for the symphony. No note changed; MIDI of 1–14, 26–32, 138, 170 and 175–182 identical to v321; theme record 35/35; the finale's quotations (27–32 = IV 199–204, 179–180 = IV 229–230, 12 = IV 1, 138 = IV 222) and the five tied parts into II 1 hold.

## Seeds of later movements (found by critic 230; keep them when revising)

- Bars 78–79: Hn 1·2 (G4–F♯4–F4–E4, from beat 4 of 78) and the cellos (G3) state the E-minor head, then Ob 1 and Vln I (G5–F♯5–F5–E5, from 79) answer an octave higher: the scherzo's theme A bar 2, at its pitch in Ob 1/Vln I. With Cl 1's G♯5 at 78 (keep that spelling) it foreshadows the scherzo's opening and its last Vln I G♯5.
- P's second bar has the rhythm of the scherzo's motive x.
- Bar 106: Hn 1's D♯5 is left unresolved, like the scherzo's horn call.
- Bar 108: Vln II's D♯4 rises to F4 in B♭ minor at 109 (no E♭ sounds at 109–110); the finale's violas take D♯4 to E4 at its 219–220.
- Bar 12: the German sixth is the finale's first chord, violas on E♭4 in both. Since v285 Horns 3·4 hold F♯3 at 12 and Hn 3 resolves it to G3 at 13 (Hn 4 rests), the pitch of the finale's Horn 4 F♯3 at its bar 1 (to G3 at 2), so the ♯4 is in the horns at the same pitch in both.
- Bars 171–174: the minor second theme is one solo cello beside the cor anglais (since v270; Tutti at 175), like the finale's single-voice minor statements of its second theme.
- Bar 37: Bsn 2 E♭3, Hn 4 G♭3, Bsn 1 B♭3, Hn 3 D♭4, the symphony's first E♭-minor sound, ahead of the finale's E♭-minor second theme.
- Bars 45–47: Cl 1 ends the link into S on E♭4 (beat 3 of 46) and Hn 1 takes E♭3 on beat 4 as the pickup to the A♭ S head (since v275). Movement II enters theme A the same way: Cl 2 E♭3 to beat 2 of II 6, Hn 1 E♭3–F3 on beat 3.
- Bars 60–62: the bass falls G♭–F♭–E♭ by whole bars (Cb G♭2–F♭2–E♭2, harp G♭1 at 60; since v274), with iv6 of A♭ over F♭ at 61, into the cadential 6/4 at 62. This is the bass of movement II's climax (G♭1–F♭1 at II 62, E♭2 at II 65) and its F♭→E♭ thread (II 5, 21, 78, 88).
- Peaks across the symphony: the violins' highest notes rise A♭6 (I) – B♭6 (II) – B6 (III) – C7 (IV); movement I has fff only at 122 and 160. Keep movement I below these.
- Bars 77–83: the bass moves A♭–E–C, the symphony's key cycle in small.
- Keep Tpt 1 B4 and Tpt 2 F4 in the stop chords at 26 and 138: the finale (v241) uses the same trumpet layout at its 138.
- Movement I's bar 138 stop chord, for the record: bass D; Vln II D5/A♭5; violas F4/B4; Tpt 1 B4; Tpt 2 F4; Hn 1 A♭4 (corrected at v251: earlier versions of this note said Tpt 1 A♭4).
- Bars 37–44: the B♭1 pedal (39–40) reaches E♭ at 41, a passing key that turns into V of A♭ at 44. The finale's transition holds the same B♭1 and makes E♭ minor its real key at its 51; since v358 Bsn 2 holds the pedal's B♭ (B♭2) through 41–43 over the E♭ bass, so the B♭ carries on as a common tone into the E♭ chord, as in the finale's transition.
- Bar 75: A♭7 spelled with G♭ (V7 of D♭) moves to D♭ minor 6/4 at 76, ahead of the finale's A♭7 → D♭ at its 209–211. Bar 12 spells the same sound as the German sixth, as the finale's 219 does. Keep both spellings (cycle 300).
- Bars 46–52: Hn 1 with the cellos over harp in A♭ (the S head) is the colour of movement II's theme A (Hn 1 over harp, II 7–14); movement II keeps its solo fresh by dropping the cellos and putting its wind chord at 3–6 first (cycle 310).
- Bar 13: the horn call's E♭3–C4 in Hn 1 is the span movement II's theme A fills at the same pitch and in the same player (E♭3 F3 A♭3 C4); the scherzo's trio tune fills it in E (cycle 310).
- Bars 179–180: the timpani pulse `c4 r8 g,8 c4 r4` is the scherzo's motive x with its first quaver silent; the figure runs II 84–85 → III 9, 363–371 → IV 9, 143, 178 (motive x, pp, after III 363–371), 229 (this pulse form, C3 r8 G2 C3). Keep the eighth rest (cycle 310).
- Bars 171–174: the solo cello and cor anglais duet is answered by movement II's solo violin with Ob 1 at 15–22 (cycle 310).
- Bars 111–116: the bass falls F–E–E♭–D–D♭–C → G by whole bars, the motto tail enlarged; B.cl E♭3–D3–D♭3–C3 at 113–116, the motto's own pitch. With movement II's B.cl tail at II 32–34 that makes three at E♭3; the finale should not add another (cycle 330).
- Bars 70 and 73: the stop chord as D–F–A♭–C♭ over the A♭ pedal. At 73 the violas hold C♭4, movement II's bar 33 chord with the same spelling and pitch, C♭4 and A♭1 (cycle 330); at 70 the C♭ is C♭5 (violas' arpeggio, Ob 2).
- Bars 7–9: the cor anglais holds G4 to 9.3 and Vln I takes the same G4 at 9.4 (Rimsky-Korsakov PDF 125–126, transfer on a common note); movement II's 89 hands Cl 1's C5 to Vln I's C5 the same way.
- Bars 23–26 and 135–138: four slurred groups of three crotchets over three bars of 4/4, a 3/4 grouping inside 4/4 (A&S Ex. 3-7 type), not a hemiola, though older lines here call it one. It is not meant to match the scherzo's true hemiola.
- Bars 27, 30, 131: timpani `c4 r8 c8 c4 r8 c8` ff, the hammered form of the coda pulse at 179–180; keep the timpani rhythm of 27–32 and 131 (the finale quotes 27–32 at pitch).
- Bar 13: the horn call's rising sixth E♭3–C4 is answered twice by the scherzo's trio tune: its head fills the sixth (G♯4–A4–B4–E5), and since scherzo v322 its bar 3 falls a sixth (D♯5–F♯4).
- Bars 73–80: Vln II E♭4–G♭4–F♭4–E♭4 (73–77), then E♭4–E♮4–E♭4 (77–80), all at one pitch: the movement's ♭6–5 motive in A♭ minor, then respelled inside the A♭–E–C cycle; Vln II's and Fl 1's F♭ (F♭5 at 75) anticipate movement II's F♭→E♭ thread. Keep Vln II 73–80 and Fl 1 F♭5 at 75 (cycle 333).
- Bar 110: a soft C-major triad over C2 (C7 at 105 and 112) works as V of F minor, as in Mozart K. 457 (A&S PDF 449), not as a tonic (cycle 340).
- Bars 73–76 (A♭ pedal, Hn 4 A♭3, F♭ mixture at 76) are the same chord as movement II's 3–6.
- The E♭4/E4 thread stays at one pitch: violas at 12, 147 (with Hn 1, the C-major S head; quoted at IV 247), 166 and 179–182, Vln II at 8–9 and 77–80 (E♭4, E4 from beat 3 of 78 over the E-major chord of the A♭–E–C bass, E♭4 again at 80).
- Movement I never confirms C major at forte: its C-major cadences (154→155 pp, 165→166 p) are soft, so the finale's 222→223 is the first strong one. Keep it so.

## Series 4 changes (v421 → current)

- v422–v431: Cl 1 and Vln II E♭4 at 24.3–25.1 and 136.3–137.1; viola A♭4 at 68; Ob 1 holds F5–G5 and Ob 2/Fl 2 take the P phrase at 117–121; Bsn 2 A2, Bsn 1 E3 at 162; Hn 3·4 clef plan; Cb up-bow at 5; MIDI expression for sub. p, pp espr., fp (global.ily expr-volume; MIDI only). Nothing another movement quotes changed: theme record 35/35 (run themecheck.py with `--beats 4`; without it the tool assumes 3/4 and reports 0/35); MIDI of 1–14, 26–32, 46–50, 138, 146–150, 170–182 identical to v421.
- Seeds recorded by critic 430: 79→80 Vln II E4→E♭4 over the bass E→C, the E-to-C-minor step at the pitch where the finale's opening E♭4 answers the scherzo's last E4. 107: B.cl G3–F♯3–F3–E3 in E minor, the 78–79 cello pitch. 97–122: development stations B (97) – D (103) – F (111) – A♭ over G (122) spell the stop chord B–D–F–A♭ onto V; the finale's 222→223 resolves the same chord to C major.
- v432–v441: no note changed; bow marks only (c438: Vln I 68.3/69, Vc 69, Vla 19, solo Vc 171). Theme record 35/35; MIDI notes identical to v431.
- Key plans (critic 440): movement I uses the minor-key plan I–VI ‖ IV–V–I (A&S PDF 454, Beethoven 9/i); the finale uses I–III with a G minor → G major development. Keep them different. Minor v appears in movement I only at the fugato's first entry (85–86); G otherwise stays a major dominant pedal (117–130).
- v442–v451: cellos tremolo A♭3–G3 at 122–123 with the upper strings (c444); Vln I written at pitch at 121–123, no 8va (c445, notation); rest positions at 62.4, 102, 126.4, 134.4 (c445); harp étouffez at 57.1 and 165.3 (c446). Nothing another movement quotes changed: theme record 35/35 (`--beats 4`); full.midi note-ons identical to v441; reserve limits hold.
- v452–v461: Cb crescendo at 169 into the 170 stop chord (c458); score-only spacing of whole-bar notes at 4, 76, 176, 182 and Hn 1/Hn 3 part tags at 163 (c455). Nothing another movement quotes changed: full.midi note-ons identical to v451; theme record 35/35.
- v462–v471: no score change (only the draft stamp). Reserves and theme record (35/35) hold.
- v472–v481: no score change; reserves re-checked on the MIDI (critic 480). Precision: at 178.3 the whole texture is a root-position D♭ chord for two beats, a neighbour chord, not a key.
- v482–v491: no note changed (full.midi note lists identical); score-only barline spacing at 111–118 (c485); tempo table corrected: largamente holds 160–164 (c488). Theme record 35/35.
- v492–v501: Cl 1 crescendo at 129–130 into the ff at 131 and Cl 1 slur at 164–165 moved to the tie's first note (c498; no pitch changed, vl.txt identical); Bsn 1 breath mark at end of 22 (c496); parts only: Vla cues in Vln II at 89–90 and Vln I at 153–154 (c495). ♭II plan rechecked (c500). Theme record 35/35.
- v502–v511: violas' 157 arpeggio F3–A♭3–C4–F4 (was A♭3–F4–A♭4; c502); Vc and Bsn 1 at 141–142 slur ends on the tied C, B♮ a fresh down-bow/tongued (c505); Hn 2 and Hn 4 mf> on the restruck notes at 163 (c508). Nothing other movements quote changed; finale reserves (A♭6 ceiling, no trumpet melody, no F1/F2 hints) intact (c510). Theme record 35/35.
- v512–v521: Vln II 177 A♭4–F4 (was F4; removes octaves with Tbn 2, c512); violas 158 C4/E4 double stop (was C4/G4; the cadential 6/4 has its sixth on the downbeat, c514); violas in treble clef 107–110 (c515); basses up-bow at 110 (c516); viola swell at 108 peaks on the 9 (c518); harp mp at 47 (was p, c519). Release check c520: no quoted bar changed (MIDI of 1–14, 26–32, 46–50, 138, 146–150, 170, 178–182 identical to v421); reserves intact; header stamped "v521, 1 November 2026". Theme record 35/35.
- v522–v531: violas E4 on 159.1 rising to F4 with the tune (c522; the only MIDI change since v521); viola stem directions held down at 27–30, 88–89, 139, 167–169 (c525, notation only); first r07 render of the series (v527). Seed noted (c530): 158–162 Tpt 3 C4–B3–E♭4–D4–C4, the motto tail E♭–D–C in whole bars inside the ♭VI climax, without its D♭ (♭VI→♭II in C is the finale's); the finale's chorale 224–228 completes it. Theme record 35/35.
- Cross-movement (scherzo v471, 2026-11-01): the scherzo's Vln I G♯5 at bars 1–2 turning to G5 pp at bar 7 restates movement I 78–79 G♯5 → G5 at pitch. Treat the 78–79 Vln I G♯5–G5 as quoted.


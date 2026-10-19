# Movement I (Allegro, C minor): current state for the other movement threads

Owner: the movement I thread ("Movement I, 200 more loops", series 3 from 2026-10-19). Series 3 works from v221; this file is updated as changes are promoted. Last update: v231 (cycle 230). Changes since v221 that touch other movements are listed under "Series 3 changes" at the end; facts above are corrected in place. The theme record is in [themes-mvt1.ly](themes-mvt1.ly), with its index in [themes-mvt1.md](themes-mvt1.md).

Pitch names: C4 = middle C. The double basses and contrabassoon are given at sounding pitch, as the section files write them.

## Opening (bars 1–8, Lento, crotchet = 50)

- **Bars 1–4: the motto, low and bare.** Bass clarinet and cellos play it in unison, with the double basses an octave lower, pp with small swells: pickup G2 on beat 4 of bar 1, then E♭3 (dotted minim tied to a quaver), D3 (quaver), C3 (minim), D♭3, C3 tied into a semibreve C3 at 4. Pitches G–E♭–D–C–D♭–C.
- Under it, timpani roll C3 ppp, bars 1–4. The first-bar label is "Timp. in G, A♭, C, E♭ / soft sticks".
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
- Tam-tam pp l.v. at 175.
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
- The double basses, Horn 4, timpani and harp release at the end of 182. The harp is marked "étouffez" on beat 4 of 182, so it damps with the basses and timpani.
- The final barline is a thin double bar.
- "attacca" is printed at the end: in the score as a text end mark on Vln I, and in every part through partGlobal in parts-gen.py.

## Key plan and rehearsal marks

Key signatures are set in global.ily. Areas without a key signature of their own come from the section files' harmony.

| Bars | Mark | Section | Key |
|---|---|---|---|
| 1–14 | | Introduction (Lento) | C minor. Motto 1–8. Rising-sixth chain 9–13: i – iv – iiø7 – German sixth (12) – V (13). Horn call over V at 13–14. |
| 15–32 | A | First theme P (Allegro appassionato) | C minor. Stop chord vii°7 at 26 resolves to i at 27. Hammered ff tutti 27–32. |
| 33–46 | B | Transition | From C minor to V of A♭: four-horn call 41–42, V4/2 – I6 of A♭ at 44–45. |
| 47–68 | C | Second theme S (Poco meno mosso) | A♭ major (key signature). Peak 64. Deceptive cadence to F minor at 68. |
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
| 111 | "muta B♮ in A♭". From here to the end: G, A♭, C, E♭. |
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
| 66–68 | rit. |
| 69 | Tempo dell'Allegro, crotchet = 126 |
| 121–122 | allargando |
| 123–126 | sostenuto |
| 127 | a tempo |
| 145–146 | poco rit. |
| 147 | Poco meno mosso, crotchet = 112 |
| 156–157 | poco animando |
| 160–162 | largamente |
| 165–166 | rit. |
| 167 | Tempo dell'Allegro, crotchet = 126 (fermata at 170) |
| 171 | Più lento, crotchet = 72 |
| 177–178 | rit. |
| 179 | Tempo I (Lento), crotchet = 50 (fermata at 182) |

Duration: v221's full.midi lasts 430.8 s, about 7:11. The score's front page says "c. 7½ minutes".

## Climax hierarchy

There are three climaxes on A♭, rising in strength:

1. **Bar 82, ff.** First-theme head in tutti over an A♭ bass (double basses repeat A♭1 in quavers). The top is E♭6 (Fl 1, Vln I).
2. **Bar 122, fff.** A♭6 in Vln I (tremolo) and Fl 1 over the G pedal (A♭ as the minor ninth of V). Tam-tam fff (heavy beater) 122, diminuendo from 124 ("damp gradually") to p at 126, damped at 127 (since v229). It arrives from the trombone motto at 117–121.
3. **Bar 160, fff.** A♭6 in Vln I and Fl 1·2, with Vln II and Ob 1 an octave lower (Vln II an octave below Vln I at 158–161 since v230) over an A♭ bass (♭VI). Suspended-cymbal roll at 159 and crash cymbal at 160, the movement's only cymbal.

The fff marks are at 122 and 160 only.

The A♭6 peaks:
- Vln I reaches A♭6 at 31, 72, 122 and 160. Fl 1 doubles it at each of these, Fl 2 at 72 and 160. Vln II never reaches A♭6 (since v230 its highest note is B♭5).
- At 140, Fl 1 reaches A♭6 alone (Vln I is an octave lower) over a D♭ bass.
- No violin note in movement I is higher than A♭6. The violins never reach C7.

## Brass use

**Trumpets.**
- Where they play: 26–33, the sf quaver at 41, 69–72 (Tpt 1 has the S head at f with Ob 1 and the flutes), 82–83, 113–116, 122–123, 131–143, 158–162 and 167–170.
- Tpt 1 moves B4→C5 into the minor tuttis at 26→27 and 138→139.
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

**Not used anywhere in movement I:** muted or stopped brass, a high horn unison, a full low-brass unison in the bass, the falling major motto in full brass at forte (G–E–D–C appears only at mp–mf in Hn 1/violas/cellos at 147–150), and a sustained forte C-major chord in the full brass.

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
- **A tuba melody, a high horn unison, a full low-brass unison in the bass, and the first cymbal crash of the finale.** None of them is in v221. Its only cymbal crash is at 160.
- **C major as a key** (the scherzo is told not to use it).

## Series 3 changes (v221 → current)

- v223: Hn 3 B3→C4 at 165–166 (leading tone resolves; was B3→G3). Vc D3 tied at 145 (was B2). Vln II G4 on beat 4 of 46.
- v225: hammered tutti inner brass at 28–31 no longer double the bass (Tpt 2 G4 at 28, B♭4 at 30; Tpt 3 F4 F4 G4 A♭4–F4 at 28–31; Hn 2 G4 at 30). The finale follows this at its 199–204. Cl 1 F4 at 145–146.
- v226: stems on the middle line follow their neighbours (engraving only).
- v227: Vln I bowing 11–13; Vc pizz. cut on beat 3 of 63; Vln II "unis." at beat 3 of 73.
- v228: Vln II and violas enter after the P pickup at 15 and 17; double basses rest 85–89 (fugato subject alone); violas 156–157 re-voiced.
- v229: tam-tam fades 124–126; brass crescendo into 41 and 122; Cl 1 B4 at 177 fades.
- v230: Vln II an octave below Vln I at 158–161; double basses unison G2/F2 at 6–7.
- Unchanged so far: the motto, P and S heads, horn call 13–14, stop chords, coda 171–182 notes, the last chord and the five tied parts, timpani tunings and the timpani pulse 179–180, the "Do not reuse" list.
- v231: Cl 1 at 78 takes the A♭5 common tone as G♯5 for one beat over the E-major chord (was A♭5 held against the horns' G4).

## Seeds of later movements (found by critic 230; keep them when revising)

- Bar 79: Ob 1 and Vln I play G5–F♯5–F5–E5, the scherzo's theme A bar 2 at the same pitch.
- P's second bar has the rhythm of the scherzo's motive x.
- Bar 106: Hn 1's D♯5 is left unresolved, like the scherzo's horn call.
- Bar 108: Vln II's D♯4 is reinterpreted as E♭4; the finale's violas take D♯4 to E4 at its 219–220.
- Bar 12: the German sixth is the finale's first chord, violas on E♭4 in both.
- Bars 77–83: the bass moves A♭–E–C, the symphony's key cycle in small.
- Movement I's bar 138 stop chord, for the record: bass D; Vln II D5/A♭5; violas F4/B4; Tpt 1 A♭4; Tpt 2 F4.

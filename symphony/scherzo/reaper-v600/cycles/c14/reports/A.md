# Critic A, cycle 14: articulation and phrasing (on the c13 render)

Data: `cycles/c13/render/` stems and master, `cycles/c13/build_render/parts.json` (byte-identical to `build/parts.json` today), `cycles/c12/render/` and its parts.json for comparison (each on its own tempo map), printed marks from `build/mockup-events.tsv`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1). An eighth lasts 114 ms at quarter 264 and 132 ms at 228. No REAPER step, nothing changed outside this report; the scratch folder is deleted, so the methods are described here.

Measure S: Movement II's `tools/pcx.py` `s_start` (the function `s_onsets.py` calls): on a join to a different pitch the earlier of pcX and the robust band crossover, on an entry pcX. I ran it on 21 tracks over the whole movement (4,611 notes, 3,902 readings; same-pitch repeats are not read by S), on c13 and on c12. Heard length of a note = the next note's S minus its own S plus the printed slot. Levels are stem RMS in the stated windows unless a band is named. All numbers below are measured unless marked inferred.

Not re-measured this cycle: harp, timpani, pizzicato level edges, re-bow dips, con sordino and sul A lanes, accent 2-5 kHz fronts (c13's critic A: no accent over +5.3 dB; the data of those notes did not change).

## Manual notes (slot A3: May 2021 manual, PDF p.75-81, Hollywood Solo Violin, read in full; `loop/MANUAL-GAPS.md` #3)

The library is not installed. The pages are read for what the bars 349-356 solo (1st Violins KS Master DIV A) can borrow.

| Manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.75: in the Solo Violin dynamics and vibrato are linked on CC1; the Orchestra series keeps them independent | Violin I solo, qn 1044-1068 | Not linked. The track's CC1 lane is one point (72) for the whole solo while CC11 runs 8-124. A soloist's vibrato widens with the dynamic. A CC1 lane that follows the CC11 phrase shape is the nearest equivalent (finding 4, last step); check the 55-76 zone first, where two vibrato layers sound together on other KS Masters |
| p.75, p.81: "LegSus" keeps the legato transition and the sustain in one sample layer, "allowing for less cross-fading to preserve the feeling of a live performance" | every string legato line | The opposite is done on three tracks: the solo changes row (Leg Slur MAX / Leg BC MAX) at 7 of 18 joins, the cellos' trio tune at 15 of 30, Violins I in bars 209-224 at 15 of 30. Row-change joins are the ones that move between renders (finding 4) |
| p.75-77 (Long Solo group): overlapping notes are blended and lose their attack; non-overlapping notes "trigger with their regular attacks" | the solo's slurs and its one phrase start | Followed: all 18 joins overlap by 60 ms (EastWest's template: 41-80 ms), the entry at 1044 has no note before it |
| p.79: Leg Bow Change gives "a dramatic and expressive bowing to accent the second note"; Leg Bow Change Smooth "a soft, non-slurred attack" | the solo's four Leg BC MAX notes (1049, 1053, 1056, 1065), dolce p | Questionable for "dolce": the section KS Master has no smooth bow-change row, and 1049 read +99 ms in c13 against -2 ms in c12 on identical data. One row (Leg Slur MAX) with a level-only start shape at the printed new bows is the closer reading |
| p.79-81: on every legato patch "timing between legato intervals is adjusted (tighter or looser) based on how hard or soft you play (Note Velocity)" | solo at velocity 82 throughout (`LEG_VEL_SPANS`), cellos' trio tune at 80 | Used as a fixed value. `mockup-kit/LEARNINGS.md` line 118 found velocity did not move the Violins I KS Master's crossovers, so I do not propose velocity as a timing cure; it is one variant of the range test in finding 2 |
| p.80: Leg Slur "shines at slow to medium tempos when there's plenty of time to hear the individual transitions"; Leg Runs is for fast notes | the eighths inside the trio tune (132 ms) | The cellos' slur transition takes about 285 ms at velocity 80 (lead plus S on 512 and 524), more than twice the eighth. Finding 2 |
| p.80-81: legato transitions exist for intervals "up to an octave in either direction" | Violoncellos 648 (up 14 semitones) and 840 (up 16), both on Leg Slur MAX with lead 0 | Not allowed for: they start with the row's first-note attack and read +124 and +164 ms. Finding 3 |
| p.75: the solo library's mics are close and mid alternatives, no surround | the solo's Close-only DIV A patch, Close -3.6 dB, width 0.2, Stereo Double 0.4 | Consistent with a close solo. Its "soft end over the limit" is a measuring artefact (finding 6) |

## Totals and the state-guard question (measured)

Share of readings more than 25 ms / 60 ms from the beat, c12 -> c13, whole movement: Violins I 37 / 7 % -> 30 / 5 %; Violins II 39 / 7 -> 36 / 7; Violas 35 / 9 -> 34 / 9; Violoncellos 46 / 13 -> 44 / 11; Flute 1 20 / 3 -> 17 / 3; Flute 2 38 / 13 -> 36 / 12; Oboe 1 24 / 7 -> 22 / 4; Cor anglais 30 / 9 -> 24 / 7; Clarinet 2 23 / 4 -> 19 / 3; Clarinet 1, bassoons and horns unchanged within 2 points; Violin I solo 53 / 16 -> 58 / 16.

Stale state: none in the audio. On legato joins whose data is the same in c12 and c13 (lead within 3 ms, same rows) the median change of S is 0 ms on every track, including the three the guard named after the render (Horn 4: 19 joins, none moved 25 ms; Violins I: 97 joins, median 0; Violoncellos: 178 joins, median 0). A stale state would shift them by about -45 ms. What did move is a different effect, in finding 4.

Short rows: the staccato theme is on the beat as in c12 (Violins I bars 13-28: 1 of 45 notes over 60 ms, the staccatos within -27..+31 ms). No printed note of the thematic lines is silent.

## Findings

### 1. Theme head, Violins I, nine soft statements: the accented half note dies before the slur continues, and the staccato after the eighth pair is 4-14 dB louder than the pair (measured; cure inferred)

Where: the appoggiatura figure of theme A (accented half note slurred to two eighths, then a staccato quarter), half notes at qn 39, 51, 69, 75, 285, 759, 771, 789, 795 (bars 14, 18, 24, 26, 96, 254, 258, 264, 266), on Sus Marc LITE.

Timing is now right: first eighth S -32..-46 ms, second -16..0, each heard 116-160 ms (printed 114), the staccato after -7..+2 by S. Keep the row and the 0.09 s re-attack leads.

Level is not. Violins I stem, dB:

| half note at | half 0-150 ms | 150-300 | 300-440 | first eighth | second eighth | staccato after | staccato before the half |
|---|---|---|---|---|---|---|---|
| 39 | -34.2 | -34.4 | -45.5 | -40.7 | -40.8 | -34.5 | -39.8 |
| 51 | -36.8 | -40.8 | -52.6 | -46.8 | -47.2 | -32.8 | -39.0 |
| 69 | -32.3 | -34.3 | -39.5 | -38.6 | -40.7 | -34.0 | -33.1 |
| 75 | -35.2 | -35.4 | -46.8 | -42.1 | -42.7 | -34.8 | -38.4 |
| 285 | -39.1 | -39.2 | -50.9 | -43.8 | -43.2 | -34.3 | -44.7 |
| 759 | -33.8 | -34.0 | -45.2 | -40.5 | -40.2 | -33.7 | -37.6 |
| 771 | -35.1 | -39.4 | -50.8 | -47.2 | -47.2 | -34.3 | -39.1 |
| 789 | -31.8 | -33.5 | -38.4 | -37.5 | -39.7 | -35.6 | -30.3 |
| 795 | -34.9 | -35.1 | -46.6 | -42.4 | -42.3 | -34.9 | -40.2 |

Three things in it:
1. The half note falls 11-16 dB between its first 300 ms and its last 140 ms (50 ms frames at 39: -36, -35, -33, -31, -35, -41, -43, -48, -47). That is the Sus Marc LITE sample at velocity 56 with flat CC11 (`ONE_TIME_c14.md` item 4 names the same caveat from Movement I). c12 had the same fall (-47, -49), but the eighths then started as legato targets 210 ms before their beat and covered it; with 90 ms leads the hole is exposed. A slurred note that is 12-23 dB down for its last 150 ms does not connect to the eighths: the figure is heard as a short accent, a gap, two soft notes.
2. The pair's level step starts 0.41 qn (93 ms) before the first eighth's beat (`LEVEL_SHAPES`, `(q - 0.45, 0), (q - 0.41, a)`), so it also cuts the half note's tail by the step: at 51 and 771 the tail reaches -52.6 / -50.8 dB (frames -59, -57 at 51; c12 -54, -55). At those two the steps (-11 / -16) put the eighths at -47, 10-12 dB under the half note's start and 6 dB under the pairs of the other statements.
3. The staccato quarter after the pair is 4-14 dB over the pair (median +7) and 3-10 dB over the staccato quarter before the half note in 8 of 9 statements (c12: -38.8, -34.3, -35.6, -34.6, -38.9, -36.3, -38.5, -38.6, -39.1; c13 is 1.5-4.6 dB higher in 7 of 9). The step returns to 0 dB 0.02 qn after the staccato's beat and lifts the second eighth's ring with it: the staccato's pitch band passes the second eighth's band 38-52 ms after the beat (c12: 12-40 ms before it), which is the actor's open item. The resolution of an appoggiatura should be the lightest note of the bar; here it is level with the accent (-34.5 against -34.2 at 39) and above it at 51 and 285.

The actor's other open item (second eighth 7-11 dB over the half note at 53.5, 287.5, 773.5) is a reading against the half note's faded tail. Against the half note's first 300 ms the second eighth is 2-10 dB under it.

Fix, in `build/score_config.py` (the `_C13_V1_PAIRS == "marc"` block), tested first on the bars 13-28 range render that block was built for (discard the first render after the build):
1. Set the eighths' level at the source. They play at velocity 78-94 (`vel_by_cc` `[(34, 70), (46, 78), (58, 86), (72, 94)]`) next to a half note at 56-64. Change to `[(34, 50), (46, 56), (58, 62), (72, 70)]` and render with `C13_V1_LEVELS=0`. If the eighths then sit within 3 dB of the half note's first 300 ms, drop the level steps. If the row ignores velocity, keep steps but as in 2.
2. If steps stay: start the step at the first eighth's sounding start, not before it (`(q - 0.12, 0), (q - 0.06, a)` instead of `(q - 0.45, 0), (q - 0.41, a)`; the eighth's note-on is 0.40 qn before the beat and it sounds 58 ms later), make 53 / 773 `(-6, -9)` like 77 / 797, and do not return at the staccato: end the shape `(q + 0.93, b - 3), (q + 1.5, 0)` so the return falls in the staccato's decay, and give that staccato quarter the level back by velocity (`VEL_SET` on q + 1: 57 -> about 66; fit on the range render).
3. Hold the half note up through its second half, before the hall where possible: a CC11 rise on the note from its printed value at +0.15 s to +14 at +0.40 s (51 -> 65 at qn 39; the row's own fall is 11-16 dB, this gives back about half), back to the printed value at the first eighth's note-on. If no CC11 shape rule reaches a single note, use `LEVEL_SHAPES` `[(h + 0.7, 0), (h + 1.55, 6), (h + 1.62, 0)]` (h = the half note's onset); the fall of 6 dB there is inside the eighth's attack, not under a rest.
4. Trim the staccato after the pair so it is the lightest note: target 2-3 dB under the pair (`note_trims.json` on q + 1 with `NOTE_TRIM_RAMP_S` 0.05, about -4 dB after step 1 or 2 has removed the lifted ring; measure before fitting).
Accept: half note's last 140 ms within 8 dB of its first 300 ms; eighths within 4 dB of each other and 1-5 dB under the half note's first 300 ms in all nine statements; staccato after the pair not over the pair and within 2 dB of the staccato before the half note; S of the four notes unchanged within 15 ms.

### 2. Cellos' trio tune (bars 169-184, with Horn 3 in unison to bar 176): the two downbeats after the eighth pickups are now 72 and 136 ms late, and the pickups last twice their length (measured; cure needs a range test)

Where: Violoncellos qn 504-552, arco espress., the first statement of T in the strings. c13 moved four early notes later with negative `leg_leads.json` rows (511.5: S -141 -> -55; 518: -114 -> -27; 523.5: -108 -> -13; 528: -119 -> +32). Two side effects:
- The notes after the two eighth pickups lost lead through the cap from the moved onset: 512 lead 280 -> 213 ms, S +2 -> +72; 524 lead 259 -> 162 ms, S +23 -> +136. Lost lead and added lateness agree (67 -> 70, 97 -> 113 ms).
- The eighths 511.5 and 523.5 are heard for 259 and 281 ms (printed 132). Horn 3, which doubles the line, plays 511.5 / 512 at +16 / -33 ms, so at bar 171 the horn's downbeat comes 105 ms before the cellos', and at 524 the cellos are 64 ms behind the horn.
The line as a whole: 13 of 30 joins outside 25 ms, 5 outside 60 (c12 by this measure: 14 and 5), range -66..+136.

Cause: the cellos' Leg Slur MAX transition at velocity 80 needs about 285 ms from note-on to the new pitch on these joins (512: 213 + 72; 524: 162 + 136 = 298; c12: 280 + 2, 259 + 23). The eighth before lasts 132 ms and itself needs about 125 ms to speak (511.5: lead 181, S -55). Both notes cannot be on time with these transitions: the downbeat's note-on would have to come before the eighth's.

Fix: the downbeat matters more than the pickup (the horn and the harp's off-beats mark it). On the cellos' range-test setup of c13 (`rangetest/`, qn 504-552, discard the first render), compare:
- (a) cap lifted on the two downbeats, as c13 did for the solo: `LEG_CAP_FRAC["Violoncellos"]` rows `(511.9, 512.1, 1.0)` and `(523.9, 524.1, 1.0)` with their c12 leads (0.280 / 0.259 s), keeping the new rows at 511.5 / 523.5. The note-ons of pickup and downbeat are then 33-65 ms apart, under the 100 ms minimum: check that the eighth still speaks (its pitch band within 6 dB of the downbeat's for 80 ms or more).
- (b) the c12 rows restored at 511.5 and 523.5 (eighths about -140 / -110, downbeats +2 / +23).
- (c) (a) with velocity 124 on 511.5, 512, 523.5, 524 (manual p.79-80: velocity tightens the interval timing; not reliable on the Violins I KS Master, untested on the cellos').
Take the variant with both downbeats within 40 ms and the eighths heard 100-200 ms; if none, take (b). Then fit 506 (+55), 522 (+58), 526 (+62), 532 / 533 (-62 / -66), 535.5 (-52) only after finding 4's row decision, because 15 of this line's 30 joins change row and such joins do not hold a fit. The join notch at 506 is keyed in absolute qn: 506's lead is unchanged this cycle (208 ms, S +55 in both renders), but any refit of it must move the notch with it (key it in seconds from the note-on, Movement II c53 critics).

### 3. Legato-row string notes that follow a short Sus MAX or staccato note, or leap more than an octave, still start 70-190 ms late; bar 49 beat 1 is the worst (measured; cure from the finale, inferred for this score)

Bar 49 beat 1 (qn 144), the accented f start of the second idea's second phrase: Violins I +116, Violins II +105, Violas +139 ms against Flute 1 +8, Oboe 1 +28, Cor anglais +14, Clarinet 2 +35, Bassoon 1 +39, Violoncellos +22. The strings arrive a tenth of a second after the winds on an accent. c13's generic lead (`LEG_HEAD_AFTER_ROW_LEAD_S`) is held at 34 ms by the cap after an eighth pickup.

The same class, c13 values (lead in brackets):
- after a Sus MAX eighth: Violins I 157.5 +84 (34), 385.5 +80 (34; c12 +45), 853.5 +52 (34); Violins II 853.5 +162 (34; the next note, 854, reads -123, so the pair 853.5 / 854 is swallowed into one change); Violoncellos 157.5 +90 (34), 853 +124 (68); Violas 382 +72 (136), 387 +78 (68), 855 +55 (68).
- after a staccato, lead 120: Violins II 123 +127 and 819 +125 (the f heads of the answering phrase, bars 42 and 274), Violoncellos 171 +114, 207 +99, 891 +141, 867 +79, 180 +72.
- leaps over an octave on the legato row, lead 0 (manual p.80-81: no transition sample beyond an octave): Violoncellos 648 +124 (up 14 semitones, bar 217), 840 +164 (up 16, bar 281).
- soft, not for this cure: Violas 672 +75 and 1065 +125, Violas 828 +187 (pp entry on the sub. p), Violins II 360 +102 (sub. p entry, lead 200).

Fix: finale technique 49 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`: S +85..+144 -> -38..+26 ms on nine notes): play the note as a Sus MAX stroke 0.06 s early instead of as a legato-row head. The tools here have the pieces (`DOWNBOW_STROKE_AT`, `ROW_LEAD_S`, `ROW_LEAD_KEEP_END`, `ROW_TRIM_STROKES` in `tools/score_to_parts.py`; `DOWNBOW_STROKE_AT` is already used for the hemiola strokes). Add to `DOWNBOW_STROKE_AT`: Violins I 144.0, 157.5, 385.5, 853.5; Violins II 144.0, 123.0, 819.0, 853.5; Violas 144.0, 382.0, 387.0, 855.0; Violoncellos 157.5, 853.0, 171.0, 207.0, 891.0, 648.0, 840.0, with a 0.06 s row lead, and take these onsets out of `LEG_HEAD_AFTER_ROW_LEAD_S["at"]`. The note after each stroke, if slurred to it, then joins from a Sus MAX note: give it the technique's 0.09 s lead and measure it. Leave the soft ones (velocity 41 and under, and the two sub. p entries) on the legato row with their entry leads; for Violas 828 raise the entry lead from 0.12 to 0.25 s (`entry_leads.json`), it is the only string section 180 ms behind the celli (+6) on the sub. p.
Accept: 144 in Violins I, II and Violas within 40 ms of the beat and within 50 ms of Flute 1; every listed note within 50 ms; first 150 ms of each stroke not more than 3 dB over its body (weight, not bite).

### 4. Joins that change legato row move by about 100 ms between renders of the same data; one legato row per line is the right cure for Violins I, the cellos and the solo (measured; the cure's cost is from Movement II)

Evidence in this project: on joins with identical data in c12 and c13, 10 of 138 whose row differs from the previous note's row moved more than 45 ms, against 4 of 340 same-row joins. The moves have fixed sizes: Violins I 146 (+66 -> -46), 159 (+57 -> -49), 387 (-41 -> +59), 540 (+18 -> +106), 644 (+39 -> -67): 88-112 ms, Movement II's 105 ms; Violoncellos 380 (-29 -> +31), 933 (+3 -> -106), 948 (+6 -> -75); Violin I solo 1049 (-2 -> +99), 1054 (-48 -> +37). So three of the actor's readings are takes, not results: "Violins I 146 now too early" (its row changed nothing certain), and the cellos' 933 / 948. Do not fit leads on these.

The comparison inside c13: bars 209-224, Violins I and II play T in octaves on the same onsets. Violins II (one legato row since c02's `ROW_REMAP`) has 8 of 30 joins outside 25 ms and no join that moved between c12 and c13 (0 of 95 same-row joins on the track moved 25 ms). Violins I (15 row changes in the 30 joins) has 17 of 30 outside 25 ms.

Lines to move to one row, by row changes among their legato joins: Violins I bars 209-224 (15 of 30), 177-184 (5 of 14), 185-208 (4 of 14), second idea 45-56 and 121-140 (5 of 17 each), 277-288 (2 of 11); Violoncellos trio tune 169-184 (15 of 30), bars 209-224 (13 of 27), 301-324 (6 of 19), second idea 45-56 (5 of 17); Violin I solo 349-356 (7 of 18). Violins II, Violas and Violas div are already on one row.

Fix: `ROW_REMAP` `{"Leg BC MAX": "Leg Slur MAX"}` on Violins I, Violoncellos and Violin I solo (the form Violins II and Violas use). It also unloads Leg BC MAX on Violins I (27.2 thousand regions for 32 notes, c13 critic A's count) and on the other two. Then, as Movement II c52 did and as this project's c13 range test showed is required (all 30 joins 120-260 ms early without it):
- refit every lead on the remapped lines from two range renders per section (discard the first after the build), with S; expect the former Leg BC targets 70-150 ms early before the refit;
- keep a keyswitch at least 0.15 s before the remaining row-change targets (a legato note after a Sus or staccato row) with `KS_MIN_LEAD_S`, which finding 3 reduces further;
- compensate the row's level at f / ff (Movement II: Leg Slur MAX 2.3-5.2 dB softer than Leg BC MAX there): measure bars 209-224 Violins I against Violins II before and after and put the difference in `ROW_TRIM_DB`;
- side effects to check, from Movement II's c53 critics: (1) a printed new bow that now starts like the middle of a slur. In c13 this does not occur yet: of the string notes over 1.15 s only ppp / pp entries start soft (Violins I 0 and 1089: -6.3 / -6.2 dB first half second against the second; Violas 708 -5.6; Violas div 1056 -10.0), and those are printed fades in. After the remap, measure the first 0.5 s of every former Leg BC note of a quarter or longer and give the soft ones a level-only start shape (about +3 dB over the first 0.15 s). (2) Join notches and fills keyed in absolute qn (celli 506 / 570, Clarinet 1 459, per CHANGES unchanged this cycle): re-key them from the note-on in seconds before the leads on those lines move.
- On the solo, with the rows gone, draw CC1 with the CC11 phrase shape (now one point at 72; manual p.75) only if a one-track test shows no doubled vibrato layers in 55-76.
Accept: no join on the remapped lines moves more than 25 ms between two range renders; Violins I bars 209-224 at most 9 of 30 outside 25 ms; the solo against Flute 1 "col Vl. solo" at most 3 of 19 onsets more than 40 ms apart (now 7, with 5 over 60: 1049 +90, 1055 +60, 1061 +72, 1061.5 -142, 1065 -72; the two around 1061 are Flute 1's own -78 / +161, the 120 ms lead from the slur-start join rule that c13 left).

### 5. Flute 2 against Flute 1 in the second tutti (bars 305-320, a2 in unison, running slurred eighths): 15 of 65 shared notes more than 60 ms apart (measured)

Flute 2, qn 912-960: 14 of 66 readings over 60 ms and 36 over 25 (Flute 1: 1 and 10 of 71). Flute 2 minus Flute 1 on shared onsets: median +16 ms, 27 of 65 over 40, 15 over 60. c13's extra 0.03 s of lead did not help (the actor's count agrees). The lateness is fixed per pitch pair and repeats to the millisecond, so a table will hold. Same-row joins, lead 51 ms, S per pair: D sharp 6 -> C sharp 6 +93, +93; F sharp 6 -> E6 +84, +92; E6 -> B5 +92; B5 -> G5 +111; B5 -> F sharp 5 +88; E6 -> D sharp 6 +58, +57, +58; F sharp 6 -> D sharp 6 +60; E6 -> F sharp 6 +52; C sharp 6 -> B5 +39, +41; G sharp 6 -> G6 +43; A6 -> G6 +28, +27, +30, +28 (one +101); F sharp 6 -> F6 0, 0; G6 -> A6 -4..+17. D sharp 6 -> E6 reads -117..-137: the estimator on E - D sharp - E, leave it.

Fix: `LEG_PAIR_EXTRA_S["Flute 2"]` (the table exists in `tools/score_to_parts.py`, keyed by MIDI pitch pair), seconds, 0.8 of the excess over Flute 1's median: `(87, 85): 0.07, (90, 88): 0.065, (88, 83): 0.07, (83, 79): 0.08, (83, 78): 0.065, (88, 87): 0.04, (90, 87): 0.045, (88, 90): 0.035, (85, 83): 0.025, (92, 91): 0.03`. The total lead (51 + up to 80 ms) passes the eighth's 114 ms on five pairs, so print the realised leads before rendering (c13's lesson on caps); where the cap holds a pair, accept the capped value. If more than 8 shared notes stay over 60 ms apart, lower Flute 2 by 3 dB in 912-960 (`roles.json`) so that Flute 1 sets the line: at ff in the top octave the second flute's late changes smear every bar.
Also for the winds, one value: Oboe 1's row lead 0.055 -> 0.02 s (`LEG_HEAD_AFTER_ROW_LEAD_S`): its first slurred eighths of the loud heads read -39..-56 ms (209, 317, 347, 353, 821, 893, 917, 947, 953, 1001; median -43, as the actor found).

### 6. Smaller items (measured)

- The two soft ends "over the 0.30 s limit" are artefacts of the check, not longer tails. Violins II 444.5: the dry stem is the same in c12 and c13 (10 dB fall 0.29 s by the check, 0.21 s counted from the note-off at 444.786, 20 dB in 0.32 s, both cycles); the 0.31 comes from the R Strings stem, which there carries the double basses (-52 dB, as loud as Violins II) and changed with the return pan. Violin I solo 1066.8: counted from the note-off (1066.81) the dry stem falls 10 dB in 0.09 s and 20 dB in 0.155 s (c12: 0.075 / 0.13 s), so Stereo Double adds about 20 ms. The check reads 0.33 because its reference peak moved from 0.10 to 0.22 s before 1066.8, and because the solo's last note is 1.5 dB lower than in c12 (-47.2 against -45.7 dB in the 100 ms before the note-off; the solo's RMS over 1044-1066.8 is unchanged, -40.3 against -40.4), so "10 dB down" now lies at the level of the other strings' hall. Nothing needs shortening. Change the check (`check13.py`, block `hall`): time from the note-off to -10 dB on the dry stem alone.
- Violoncellos fugato pairs: 173 -76, 173.5 -36, 869 -52, 869.5 -30 ms (leads 220 / 150). Halve the added leads as the actor proposes (`SHORT_SUS_LEAD_AT` 0.16 -> 0.10 s at 173.5 / 869.5; the row at 173 / 869 0.22 -> 0.16 s).
- Violins I first eighth of the theme-head pairs: -32..-46 ms. `REATTACK_LEAD_AT` 0.09 -> 0.07 s on the nine first eighths only.
- Same-pitch staccato pairs on the trumpets and the cellos (dips 2.2-2.5 dB, c13's numbers; not re-measured): shortening failed because these rows play the sample out. Untested and inferred: a CC11 dip before the hall between the two notes (the wind rule `WIND_DETACH_DIP_MAX_GAP_S` writes one; extend it to the brass short row: CC11 to 60 % for 40 ms ending at the second note-on), on a range render of bars 105-108 first. `STAC_LEN_SPANS` 0.7 can be removed; it changed nothing.
- Keyswitches still sit 7-8 ms before the note at every row change (`KS_MIN_LEAD_S` off). Finding 4 removes most row changes inside lines; switch the rule on for what remains.

## Do not touch

The staccato rows, leads and lengths of the theme in every section; Violins I's Sus Marc LITE eighth pairs and their 0.09 s leads (timing only: both eighths heard 116-160 ms); the woodwinds' one-value row leads except Oboe 1's; Clarinet 1's trio tune (bars 153-168: 0 of 31 over 60 ms); Violins II's and the Violas' single legato row; the negative `leg_leads.json` rows that worked (celli 345 / 945 / 844 / 350 / 880, Violas 150 / 831, Violins II 848); `BEAT_STRETCH = {}`; the hall settings (both "long" soft ends are measuring artefacts); Stereo Double on the solo at 0.4; Horn 1's link at bar 56 stays out.

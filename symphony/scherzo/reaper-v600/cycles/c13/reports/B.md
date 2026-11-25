# Cycle 13, critic B: balance and levels (render under review: c12)

Method. Levels are K-weighted mean-square levels in dB, both channels summed, in 10 ms frames of the dry stems and the master of `cycles/c12/render/`, placed on the score with the tempo map of `cycles/c12/build_render/parts.json`. "Note level" is the mean from 30 ms to 400 ms after the score onset (to the note end if shorter). "Peak" is the highest 30 ms mean (strokes) or 100 ms mean (master). Where it matters I give plain RMS as well. Comparisons: c08 stems, c10 and c11 masters, the delivered mp3 decoded to WAV. "Measured" marks numbers from the audio or the build data, "inferred" marks judgements of cause or audibility.

## Manual notes (group B1: PDF pages 137, 140, 150-151 of the May 2021 HO manual; MANUAL-GAPS.md)

| What the page says | Where it applies | Does the render follow it |
|---|---|---|
| p. 137, Articulations view: each row of a KS Master has a load button and its own volume knob, "to adjust the loudness of each articulation". | Rows of one track that play at different levels for the same controller values: Violins I "Sus Marc LITE" against "Sus MAX" (hemiolas, bars 101-104 and 301-304), Violins I "Stac RRx14" pickups before a sustained downbeat (qn 155.5, 383.5, 851.5). | Partly. The row knobs stay at the patch values and the pipeline corrects rows in the track envelope (`ROW_TRIM_DB`, `LEVEL_SHAPES`). `ROW_TRIM_DB["Violins I"]` has no "Sus Marc LITE" entry, and the note at 155.5 is not in parts.json `row_trimmed`. Findings 1 and 2. |
| p. 140, Master channel: the gain fader changes the instrument's output "without affecting the relative mix of the microphone sub-mixer channels". | `build/mix.json` `gain_db` (c12 brass gains). | Yes. c12's +2 / +3 dB moved every brass note by exactly that amount. Finding 5 uses the same control. |
| p. 150, Note Velocity Sensitivity: velocity selects the sampled dynamic layer and cannot change inside a note, so it is the dynamic control for short instruments; the curve is linear by default. | Parked short rows (CC11 at 120, level by velocity): Violins I's staccato pickups and head notes; the timpani strokes (velocity only). | Partly. The linear default is in use and the velocity scales of the rows do not match: Violins I "Stac RRx14" at velocity 109 is 8 dB over the same section's ff "Sus MAX" downbeat (finding 2); the timpani fall 12 dB between velocity 80 (mf) and 64-68 (p), where the strings fall 7 dB between f and p (finding 3). |
| p. 151, Prepping MIDI CCs: send CC1 and CC11 before the first note. | Every track's first note. | Yes (the 3 qn pre-roll). |
| p. 151: CC7 sets a track's ceiling in the mix, CC11 shapes the line. On the LITE string instruments CC11 is loudness only and CC1 "handles both dynamics and vibrato simultaneously". | Balance corrections; Violins I's "Sus Marc LITE" notes. | Balance corrections sit in the volume envelope and `gain_db`, so CC11 keeps the printed layer: yes. On the Marc LITE hemiola notes CC1 rises 90 to 98 and CC11 88 to 114 together, so layer and loudness both climb (measured in parts.json); the level step written for the row in c06 (-5 / -2 dB) is too small for that (finding 1). |
| MANUAL-GAPS #6: Timpani Hrd KS not used; the felt patch plays the whole movement. | The p timpani solo of bars 9-12. | Not used (memory). Finding 3 raises the level only; it does not change the stick. |

## The checks asked for

Stale tracks (measured). No sign of stale legato state in the c12 audio. Legato joins by `pcx.scan` on the c12 stems: Violins I n 118 median +16 ms, front minus body -0.4 dB; Violas n 67, +3 ms, -0.9 dB; Violoncellos n 198, +9 ms, -0.8 dB; Bassoon 2 n 22, +12 ms, -2.7 dB; Horn 4 n 16, +1 ms, +0.9 dB; Horn 2 n 16, +42 ms, +2.6 dB; Contrabassoon n 14, +72 ms, -0.7 dB. Stale state would put the medians near -45 ms with fronts 3-5 dB loud. The two tracks the guard did not flag read the same (Violins II +1 ms, +0.1 dB; Flute 1 +7 ms, +1.1 dB). The Contrabassoon's data is unchanged and it reproduces c11 at 0.00 dB (CHANGES), so the state went stale after the audio was written. c11 and c10 stems no longer exist; this check is against the stale signature, not against those renders.

Horn 1's staccato at qn 165 (measured). It does not stand out. In the tutti chord its first 0.2 s is -39.3 against Violins I -28.0, Double basses -28.1, Clarinet 1 -37.3, Clarinet 2 -36.8, Contrabassoon -36.7 and the master -21.7. Horn 2 at -43.3 is the low one. No row needed.

## Findings, ranked by listener impact

### 1. Violins I's hemiola notes on "Sus Marc LITE" are the loudest stem events outside the summit, and the hemiola is louder than the ff theme it leads to

Where: bars 101-104 (qn 300-312) and 301-304 (qn 900-912), Violins I, against Violins II an octave lower.

Measured. Violins I's six half notes: 300 -22.7, 302 -19.0, 304 -17.8, 306 -16.6, 308 -16.7, 310 -19.5; reprise 900 -16.9, 902 -21.6, 904 -20.4, 906 -16.4, 908 -14.8, 910 -16.7. Violins II on "Sus MAX" with the same CC11: -30.7, -27.0, -23.9, -22.5, -22.5, -23.5 and -26.4, -30.7, -27.3, -23.1, -21.5, -21.7. Violins I is 4.0-8.0 dB over its octave in the first hemiola and 5.0-9.5 dB in the second (plain RMS 3.3-5.1 dB). Violins I's own level in the ff theme that follows is -21.0 to -23.5 per bar, and at the fff summit -15.4 to -17.8 per bar, so the f-to-ff hemiola plays 4-6 dB over the section's ff and, in the reprise, at its fff level. In the 0.4 qn around 908.5 Violins I is at -11.6 with the next stem (Violins II) at -22.0. Master peaks (100 ms): 308.2 -10.8, 898.9 -10.5, 908.5 -9.6, against 1005.4 -10.0, 1007.3 -9.4, 1010.8 -9.8, 1013.0 -9.3 at the summit. Master per bar: 103 -13.0, 104 -12.8, then the theme at 105-119 -13.9 to -17.6. Data: `build/score_config.py` puts the two spans on "Sus Marc LITE" (`ART_SPANS`, 299.5-311 and 901.5-911) with level steps of -5 dB (299.4-311.9) and -2 dB (901.05-911.9) in `LEVEL_SHAPES["Violins I"]`; the second was set in c06 to match the c05 render's level, not the balance. `RIDE_TRIMS` then takes 2 dB off both passages in the delivery only.

Judgement (inferred). The listener hears one section alone on top for four bars, then a drop when the full orchestra enters with the theme, and a reprise peak that equals the summit. The delivery ride hides part of the bar level but not the balance inside the bars.

Fix. `LEVEL_SHAPES["Violins I"]` in `build/score_config.py`: change the row `[(299.3, 0.0), (299.4, -5.0), (311.9, -5.0), (312.0, 0.0)]` to -8.0 and the row `[(900.95, 0.0), (901.05, -2.0), (911.9, -2.0), (912.0, 0.0)]` to -6.5. Leave the sf stroke at 900 (its own span, 899.6-900.1) as it is. Expected: Violins I half notes -19.6 to -22.5 (first) and -19.3 to -21.2 from 906 (second), 3-5 dB over Violins II, bar 103 about 1.5-2 dB lower in the master, master peak at 908.5 about -12. Then re-measure bars 103-104 and 303-304 against bar 105 and 305 and reduce the two `RIDE_TRIMS` rows at 300 and 897 by what the mix now does itself (they are on the Do-not-touch list for their position, not their depth).

### 2. Single staccato notes of Violins I 7-8 dB over the notes around them: the pickup at qn 155.5 and the f head notes at 204 and 888; the c12 pickup rows are now too deep

Where: Violins I, bar 52 beat 3+ (qn 155.5, the eighth before the ff of bar 53), bar 69 (qn 204) and bar 297 (qn 888), bars 128 and 284 (qn 383.5, 851.5).

Measured.
- 155.5: D6 on "Stac RRx14", velocity 109, CC11 parked at 120, volume lane +2.3 dB. Violins I stem -12.5 to -14.8 for 120 ms, then -21.4 on the ff downbeat at 156 (Sus MAX, CC11 114). The master reads -11.8 to -13.3 for those 120 ms against -17 to -19 before and after; the next stem is 13 dB lower (Violins II -27.8, celli -30.7, both also at velocity 109). It is the only event outside the tuttis in the master's top 45 peaks, and it has been there since c08 (c08 -11.1, c10 -11.6, c11 -12.1, c12 -11.8 at +40 ms).
- 204 and 888: the first note of an f entry of the theme head, A5 "Staccatissimo RRx9", velocity 87. 204: -21.4, then -31.6, -30.3, and the same A5 at 206 -28.5. 888: -22.8, then -32.9, -31.3, -29.7. The first note is 7 dB over the same pitch two beats later with a lane difference of 2.8 and 2.0 dB. Master: 9-11 dB over the 0.35 s before and 6-7 dB over the 0.35 s after.
- 383.5 and 851.5 after c12's rows (-6 on Violins I, -9.5 on Violins II): Violins I's pickup is -31.5 / -31.8 and its downbeat -23.1 / -23.2 (8.4 / 8.6 dB under). In the master the pickup's 60 ms read -21.7 (383.5) and -23.9 (851.5), which is the level of the held note before it (-22.7, -24.4), and the downbeat's first 80 ms read -17.8 and -16.5. The pickup is no longer a separate event in the master (inferred), and the step into the downbeat is 3.9 and 7.4 dB. Violins II: 383.5 -30.4 against 384 -30.0 (right), 851.5 -34.6 against 852 -27.2.

Cause (inferred from the data): on parked short rows the level comes from velocity alone (manual p. 150), and Violins I's short rows at velocities 87-109 sit far above the Sus MAX notes at the CC11 of the same dynamic. `ROW_TRIM_DB["Violins I"]["Stac RRx14"]` did not reach 155.5 (not in `row_trimmed`).

Fix, all in `LEVEL_SHAPES["Violins I"]` (short notes, so shapes, not note trims):
- add `[(155.42, 0.0), (155.47, -8.0), (155.93, -8.0), (155.99, 0.0)]`. Target -21.5 to -22.5, 0-1 dB under the downbeat; master about -17.
- add `[(203.75, 0.0), (203.8, -4.5), (204.6, -4.5), (204.7, 0.0)]` and `[(887.75, 0.0), (887.8, -4.5), (888.6, -4.5), (888.7, 0.0)]`. Target 2-3 dB over the A5 at 206 / 890 (the entry keeps its `beat_db` weight).
- change the c12 rows at 383.47-383.93 and 851.47-851.93 from -6 to -3. On Violins II change -9.5 to -7.5 on both (383.5 is right now, 851.5 is 7 dB under; the downbeat's take differs between the two, CHANGES B #2). Target: pickup 3-5 dB under the downbeat on Violins I, and visible in the master 1-2 dB over the held note before it.

### 3. The timpani's p solo in bars 9-12 is 9-12 dB under the ppp opening and 12-16 dB under the p theme

Where: bars 9-12 (qn 24-36), Timpani alone, motive x twice, printed p (qn 24). Related: the first stroke of the soft statements (c12's open item).

Measured. Stroke peaks: -47.3, -44.5, -44.8, -47.1, -47.6 and -46.4, -43.4, -44.0, -44.3, -45.6 (velocity 64-68, CC1 60, volume lane 0). Master per bar: bars 9-12 -49.0, -52.4, -47.6, -48.4; bars 1-2 (ppp violins, pp horn) -41.4, -39.8; bars 3-6 (horn call) -37.1 to -32.6 with a bar at -40.5; bar 13 (theme, p) -36.1. In the delivered mp3: bars 9-12 -37.2, -40.6, -36.2, -36.1 against -27.0 to -28.5 for bars 1-2 and -24.5 for bar 13. These four bars are the quietest stretch of the delivered file and nothing else plays in them. Mapping: the timpani at printed f (bars 91, 94) peak at -24 to -26.6, so p to f is 20 dB on the timpani; Violins I's bar medians are -42.2 (p) and -35.0 (f) in `metrics.md`. Velocity 64-68 to velocity 80 (bar 99, mf) is 12 dB. `mix.json` `soft_trim_db` excepts the timpani.
First strokes by peak (first stroke, then the other three): 288 -45.7 / -43.5 -43.8 -43.2; 291 -46.4 / -40.7 -42.4 -40.6; 294 -39.6 / -33.4 -34.4 -32.4; 297 -35.0 / -31.3 -32.6 -31.4; 720 -50.1 / -46.7 -47.7 -46.8; 738 -50.1 / -44.9 -48.0 -46.2; 744 -50.2 / -45.7 -46.5 -42.5. The f statements at 270 and 279 are level (-26.3 / -26.6 -25.1 -23.9) because the lane already carries +6 dB on their first stroke.

Judgement (inferred). The motive the movement is built on is first heard alone here, and at this level it reads as a gap of 2.7 s with faint thuds. A real timpani p in an empty texture is at least as present as ppp violins.

Fix. `build/roles.json` "Timpani": add `[23.5, 35.5, 7]` (target: strokes -37 to -40.5, bars 9-12 about -42 to -45 in the master, between the ppp opening and the p theme). Keep the velocities, so the soft felt layer stays. First strokes: `LEVEL_SHAPES["Timpani"]` steps over [q - 0.05, q + 0.9] (as the f statements have): 291 +4.5, 294 +6, 297 +3, 738 +4, 744 +5, 720 +3, 288 +2. Do not add the timpani to `soft_trim_db`: that would lift the pp rolls too (Dan's item 5).

### 4. Oboe 1's half notes equal the whole first violin section in the f unison of the second idea

Where: bars 130-131 (qn 387-393) and 286-287 (qn 855-861): Flute 1, Oboe 1 and Violins I in unison (G5, F#5, E5), f. Also bars 51-52 (qn 150-155), Oboe 1 an octave under Violins I and Flute 1.

Measured. Oboe 1 at 387 / 389 / 391: -27.4, -29.1, -28.8 (855-859: -27.4, -29.1, -28.7). Violins I on the same notes: -28.0, -25.9, -29.5. Flute 1: -35.5, -36.0, -35.2. Plain RMS says the same: Oboe 1 -29.4, -31.1, -30.6; Violins I -30.0, -27.8, -31.6; Flute 1 -36.3, -37.4, -35.8. One oboe is level with sixteen violins and 6-8 dB over the flute it doubles. Inside the oboe's own slur the four quick notes before (384-386: B5, C#6, B5, A5) are -37.1, -29.3, -39.3, -37.8, so the line steps up 10 dB at the first half note with CC11 falling from 90 to 88; the flute's same line is even (-34.3, -32.2, -33.8, -35.5, then -35.5). At 150-154 Oboe 1 is -25.8, -28.5, -26.2 against Violins I -25.3, -29.1, -27.3. Data: `mix.json` Oboe 1 `dyn_trim_db` f +3.5, ff +6; no pitch trims; the quick notes are 0.16-0.26 s long on "Leg Slur MAX".

Judgement (inferred). The unison takes the oboe's colour on the long notes and loses it on the quick ones. By Rimsky-Korsakov's forte equivalence (one string section equals two woodwinds) a single oboe belongs 3 dB or more under the section.

Fix. `build/roles.json` "Oboe 1": add `[386.8, 393.0, -4.5]`, `[854.8, 861.0, -4.5]` and `[147.8, 155.4, -3]`. Target: Oboe 1 4-5 dB under Violins I and 2-3 dB over Flute 1 on the half notes, and the step from 386 to 387 cut from 10 to about 5.5 dB. The existing rows on Oboe 1 (`[372, 384, -3]`, `[828, 840, -4]`) stay.

### 5. Trumpets: still 9-11 dB under Violins I in the theme and 15 dB under at the summit; a trumpet-only step does not disturb the family order

Where: bars 105-119 odd (qn 312-357), 333-339 (qn 996-1017). Trumpet 1, Trumpet 2.

Measured. Per bar at 105-119 (odd bars): Trumpet 1 -31.2 to -32.6, Trumpet 2 -31.7 to -33.6, Violins I -21.0 to -23.5. Summit, bars 337-338: Trumpet 1 -32.5 / -31.9, Trumpet 2 -31.3 / -30.3, Violins I -17.8 / -16.7, master -10.5. Per band against the master (dry stems): at 105-119 the two trumpets are -13.6 dB in 500-1000 Hz, -11.0 in 1-2 kHz, -13.6 in 2-5 kHz; at the summit -13.3, -14.2 and -23.7, with the strings at -0.8 and the woodwinds at -10.1 in 2-5 kHz. Trumpet 1's sustained A4 at 1008-1012 is -31.9 against -27.7 for its B4 at 1005 with CC1 rising 86 to 90. Why c12 stopped at +2 dB: the brass family at 300-312 is 1.0 dB over the woodwinds. That margin comes from the low brass (-24.2) and horns (-26.8); the trumpets there sum to -30.1. Trumpets +2 dB changes the brass family by +0.3 dB at 300-312 (-21.6 to -21.3; woodwinds -22.6), +0.4 at 312-360 (-23.9 to -23.5; woodwinds -21.5) and +0.6 at the summit (-21.2 to -20.6; woodwinds -16.5, strings higher still).

Judgement (inferred). At 11-14 dB under the master in their own bands the repeated quarters are masked for most of each bar, and at the summit the trumpets add nothing a listener can identify.

Fix. `build/mix.json` `gain_db`: Trumpet 1 3.11 to 5.11, Trumpet 2 3.25 to 5.25. `build/roles.json`: add `[1005, 1016.5, 2]` on both trumpets. `build/pitch_trims.json`: "Trumpet 1": {"69": 3} for the sustained row. Trombones, tuba and horns unchanged. Expected: Trumpet 1 7-8.5 dB under Violins I on the odd bars, about 11 dB under at the summit. Checks: no brass 2-5 kHz front over its body (item 9); each trumpet at 994-995.5 still 3 dB or more under its own 996; the order strings, woodwinds, brass at 1005-1014.

### 6. Dynamic mapping: the first woodwinds are louder at ff (bars 72, 300) than at the fff summit

Where: bar 72 (qn 213-216), bar 300 (qn 897-900), bars 336-338 (qn 1005-1014). Flute 1, Oboe 1, Clarinet 1.

Measured. Per bar: Flute 1 -24.4 (72), -21.1 (300), then -25.7, -22.8, -24.6 at the summit; Oboe 1 -25.1, -23.3, then -31.5, -26.9, -27.4; Clarinet 1 -24.1, -22.4, then -28.7, -29.2, -28.6. At bar 300 the three are within 1.0-3.2 dB of Violins I (-20.1), and the master is -12.2, louder than every bar of the ff theme (-13.9 to -17.6) and 1.6 dB under the summit bars. The summit rows in `roles.json` (`[996, 1017, -3 / -4]` on every woodwind, from c01) hold the first players down there while the second players are not held (Flute 2 -24.1 to -24.7, Oboe 2 -25.8 to -26.5, Clarinet 2 -24.1 to -24.9, level with or over their first players).

Judgement (inferred, low impact). The chords of bars 72 and 300 are woodwind-heavy and the reprise chord is close to the summit's level; at the summit the first oboe and clarinet sit under their seconds.

Fix. `build/roles.json`: on Flute 1 add `[897, 900, -2]`; on Oboe 1 add `[897, 900, -1.5]`; Clarinet 1 already has -5 there. At the summit change Oboe 1 `[996, 1017, -3]` to -1 and Clarinet 1 `[996, 1017, -4]` to -2 (target: each first player level with its second, woodwind family at 1005-1014 about +0.5 dB). Check the limiter (2.8 dB now) after the render.

## Measured and in balance (no change asked)

- Theme A, bars 13-28: Violins I -30.0 to -37.6 per bar over Violins II -48.2 to -52.5, violas -44.4 to -47.9, pizzicato celli -43.4 to -51.6, basses -45.8 to -53.1. Counterstatement 29-36: Flute 1 -38.1 to -45.6 and Oboe 1 -40.2 to -45.6 against Violins I's answers at -39.1 to -40.3.
- The two sub. p: bar 121 -30.7 after -15.7 / -20.0; bar 277 -33.9 after -23.9 / -28.5.
- Trio: Clarinet 1 -31.2 to -37.2 over the harp (-41.0 to -44.3 where it has chords) and Horns 3-4 (-46.5 to -52.7); celli -32.9 to -39.2 over Violins II con sord. -42.9 to -45.3; Violins I -30.8 to -36.5 over the celli at 177-182; Oboe 1 -35.3 to -40.2 over the harp -46.5 to -47.4. Return 209-217: Violins I -29.1 to -32.1, Violins II -30.1 to -34.4, Clarinet 1 5-8 dB under, violas' two halves -40.7 to -46.5.
- Solo passage 349-355: solo -32.2 to -40.1, Flute 1 6.4 to 9.5 dB under it per bar, Violins II 9-13 dB under. Horn 1's motto tail -32.5 to -35.9 over -41 to -47.
- Timpani at f in bars 91 and 94 (-24 to -26.6 peaks over pp strings) follows the print.
- Summit family order: strings, woodwinds, brass (full band re the master: -2.9, -5.5, brass parts -13.5 to -16.8).

## Do not touch

Keep: the c12 brass gains on trombones, bass trombone and tuba, and the horn gains; the brass rows at 994-995.5; `family_scale_skip_cc1`; the c12 join offsets and `LEG_HEAD_MIN_GAP_S`; the harp `VEL_SET` rows and the trim at 216; the timpani velocities (`lh_vel_add`), roll trims, the summit roll rows and `TIMP_DAMP_AT`; the f statements' first-stroke lane at 270 and 279; the C6 rows at 69 and 789; the solo, Flute 1, Violins II and Violas div rows at 1044-1068; Horn 1's closing contour and `[1100.25, 1128, 6]`; the trio's harp caps and Clarinet 1 trims at 456-504; the "Sus Marc LITE" row choice for the hemiolas and the theme heads (finding 1 changes its level step only); the CC11 drops at the sub. p's and the sfp; `SHORT_CC11_PARK`; the returns, sends, mics and EQ set as built; Horn 1's staccato at 165 (no row).

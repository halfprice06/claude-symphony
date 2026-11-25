# Cycle 39, critic A: articulation and phrasing (on the c38 render)

## Inputs

- The c38 render: `cycles/c38/render/` (Clarinet 1, bass clarinet, Bassoon 1 and celli after the stem fix), `render_first/`, the master and `metrics/`.
- The c37 render, for an A/B against the old hall.
- `cycles/c38/CHANGES.md`, `cycles/c38/actor_scripts/hall_c37.json` and `hall_c38.json`.
- `cycles/c38/rendered_build/parts.json`, `build/score_config.py`, `build/rebow_fills.json`, `build/early_fills.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py`.
- `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, `loop/MANUAL-GAPS.md`.
- The May 2021 HO manual, PDF pp.75-81 (row A3, cycle 39), read in full.

## How levels were measured

- Levels are plain RMS in dB on the stem, or on the master where stated.
- The window is 50 ms unless another length is given. Flute and oboe joins use 200 ms windows (kit LEARNINGS §6).
- Positions are score qn on the parts.json tempo map.
- "Hole" means the minimum after the join under the lower of the two neighbouring bodies.

## Manual notes (A3, PDF pp.75-81: Hollywood Solo Violin, licensed but not installed)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| The solo library has Close/Mid plus vintage Close/Mid mics instead of Surround/Vintage. Its CC1 links dynamics and vibrato depth, where HO keeps them separate (p.75). | Violin I solo, bars 17-22 (qn 48-65, "solo, senza sord., dolce"), on `1st Violins KS Master DIV A`. That patch is Close only and has the HO separation. | Partly. CC1 is held at 72 (`CC1_HOLD`), so the vibrato layer does not follow the p < > shape. Measured on the stem: the long notes at 51 and 63 carry 53-57 cents of pitch spread (p5-p95) and 5-6 dB of level wobble, so the half section does play with vibrato. A CC1 that follows the hairpin is a small, inferred gain. It is not a finding. |
| Long Solo: a legato script blends overlapping notes, and non-overlapping notes get their normal attack (p.75-77). Flautando, Grand Détaché RRx2, Lyrical Vib/Mute, Sus Exp and the Sus NV/VB layer sets are on CC1 with 2-3 levels (p.76-78). | The solo's two slurred phrases, 48-54 and 60-65. | Yes. Each phrase is one slur on Leg Slur MAX. The first note of each phrase does not overlap anything (attack), and the 9 joins inside overlap. A Solo Violin track would take Leg Slur or Leg Lyr Vib (below), with CC1 from the printed p and its hairpins. |
| Shorts: Marcato Vib, Martelé, Pizzicato RRx4, Sforzando, Spiccato (p.78-79). | None. The solo has no short notes. | Not applicable. |
| Legato is true monophonic legato. Leg Bow Change accents the second note, Leg BC Fast gives a clear attack, Leg BC Smooth gives a soft non-slurred attack (p.79-80). | The solo's joins are all slurred. | Yes. No join in the solo is a bow change, so Leg Slur is the right row. |
| Leg Exp Vib and Leg Lyr Vib suit slow tempi. Leg Slur "shines at slow to medium tempos", and velocity tightens or loosens the transition time (p.80). | 52 bpm Adagio, 72-80 velocity on the solo's targets (`VEL_SET`, c32 A #5). | Yes. The longer transitions follow the manual's slow-tempo advice. Measured join dips are -0.8..4.4 dB (30 ms windows, hall_c38). The worst is 62 at 4.4 dB, unchanged from c37's 4.3. |
| LegSus: a combined legato/sustain layer. CC1's value at note-on picks one of 2 dynamic layers with no crossfade, and CC1/CC11 then shape loudness mid-note (p.81). | A future Solo Violin track. | Not installed (MANUAL-GAPS #3). If it is used, CC1 must be written before each note-on at the printed level, because a later move changes only loudness. |
| Phrase ends under the drier hall. | Solo phrase ends at 54 and 65. | Measured. The release falls 13 dB by +0.23 s and about 20 dB by +0.45 s (c37: 11/17). This is within the kit's 13-17 dB at +0.3 s, and the oboe and the tutti violins take over at once, so it is not a finding. |

## Findings, ranked by what a listener would hear

### 1. Trombone 1, bar 63 (qn 213, 215): the quotation's accent and its next legato target each lost 3-4 dB in c38. The accent no longer stands over its pickup in the master (measured; cause inferred)

**Where.** Trombone 1, ff marcato quotation. The 213 accent is the legato target of the 212.5 pickup. 215 is the legato target from 214.5.

**Evidence (measured).** The MIDI, CC11, CC1, CC7 and volume envelope are identical in c37 and c38. 200 ms levels:

| Window | Track | c37 (dB) | c38 (dB) | Change |
|---|---|---|---|---|
| 213.0-213.3 (accent) | Trombone 1 stem | -19.9, -17.7, -17.9, -18.4 | -23.9, -21.7, -21.3, -21.8 | -3.5..-4.0 |
| 212.5-212.9 (pickup) | Trombone 1 stem | n/a | within 0.4 dB of c37 | none |
| 214.6-214.8 | Trombone 1 stem | n/a | within 0.4 dB of c37 | none |
| 213.0-213.3 mean, CC7 span | Trombone 1 stem | -18.4 (c36 also -18.4) | -22.0 | -3.6 |
| 213.0-213.2 vs 212.6 | Master | 1.4-2.3 dB over the pickup | -0.5..0 dB | accent gone |
| 215.0 vs 214.8 | Trombone 1 stem | -23.5 vs -20.0 | -26.9 vs -20.1 | hole 6.8 dB |
| 215.0 vs 214.8 | Master | -22.6 vs -19.3 | -25.2 vs -19.5 | 5.7 dB fall |

- The accent's 2-5 kHz energy over the first 80 ms, against the body, is -4.8 dB (c37 -6.7). The master's 2-5 kHz jump at 213 is -1.6 dB, so there is still no bite.
- At 215 the 2-5 kHz attack now sits +2.3 dB over its sagging body (c37 -3.4). The note reads as a bright front and then a hole.

**Cause (inferred).** Both changed spans are exactly the pre-hall CC7 cuts from c30/c32: 85 (-3.5 dB) over 212.9-213.35 and 95 (-2.5 dB) over 214.9-215.3. These cuts were fitted when the legato transitions played 11 dB brighter (config comment, c32 A #2b). The Flute 1 CC7 lane at 212 and the violas' at 83 moved by 0.2-0.7 dB only. So either the full Opus rebuild changed the transition layer on these two targets (they changed between builds once before, c31-c32), or the halved hall return no longer fills the cut. The fix is the same in both cases.

**Fix.** In `build/score_config.py`, in the line that appends to `CC7_POINTS["Trombone 1"]` (the c32 A #2b block):
- Raise the 213 floor: `(212.9, 85), (213.35, 85)` -> `(212.9, 110), (213.35, 110)`, which is +2.3 dB, pre-hall (S3-safe).
- Raise the 215 floor: `(214.9, 95), (215.3, 95)` -> `(214.9, 120), (215.3, 120)`, which is +2.0 dB.
- Keep the `ACCENT_SWELL_S_AT` and `LEVEL_SHAPES_S` swells, and the velocities.

**Targets.**
- Trombone 1 213.0-213.3 at 2.5-4 dB over 212.6-212.9.
- Master at 213.0-213.2 at least 1 dB over 212.6.
- The 215 hole at most 4 dB under 214.8 on the stem.
- 2-5 kHz attack minus body at 213 still under -3 dB, and the master's 2-5 kHz jump under +2 dB (Dan item 9).

Re-measure these two notes after every full Trombone 1 rebuild.

### 2. Flute 1, bar 44 (qn 136): still the straight-tone LegRep sustain after vibrato notes. Re-checked, unchanged; c38 A #1's fix stands (measured, fix inferred)

**Evidence (measured, c38).** The repeat still re-articulates:
- No gap: the 50 ms minimum at 136.0 is -49.1 dB, no deeper than the flute's own vibrato trough of -51.0 at 135.8.
- The re-attack peaks at -41.8 dB at 136.15, about 5 dB over the 135 note.
- The master rises 1.5 dB at 136.05-136.2.

Its sustain is the patch's Non Vib group, so the tone changes against the notes around it:

| Measure | 134 | 135 | 136.6-137.4 | 137.5-138.9 |
|---|---|---|---|---|
| 4-6 Hz level modulation (20 ms envelope, p5-p95, detrended) | 7.3 dB | 8.1 dB | 2.0 dB | 1.2 dB |
| Spectral centroid | n/a | 1189 Hz | 760 Hz | 1011 Hz |

c37 measured the same to within 0.3 dB and 40 Hz. With half the hall return, this straight, darker tone is less covered for 3 s of the pp duet with the cor anglais (inferred).

**Fix.** As c38 A #1. In `score_config.py`:
- `ART_SPANS["Flute 1"] = [{"from": 125.85, "to": 139.5, "art": "Leg Slur Rep"}]` (FL KS Master key 36). `FL Leg Slur Rep.oib` is installed in `Flute/04 Legato/`.
- Keep `WIND_SLUR_REP_MERGE_SKIP = {"Flute 1": [136.0]}`.
- New generic `SLUR_REP_ABUT_AT = {"Flute 1": [136.0]}` in `tools/score_to_parts.py` (empty default). The previous same-pitch note ends 0.01 qn before the onset, with no overlap; manual p.112 says "without space".
- CC1 dip 0 on the listed repeat in `cc1_fn0`.
- Remove the c37 post-render `LEVEL_SHAPES["Flute 1"]` cut over 136.4-139.7, and keep the 133.8-139.5 +5 shape.
- Full Flute 1 rebuild: the row set changes.

**Targets.**
- 4-6 dB of modulation at 136.6-138.9.
- A re-articulation 2-4 dB over the 135 note, with no sag under the body.
- Body about -48 dB.

Fallback: keep LegRep RRx4, and lift only its post-attack sag (+3 dB over 136.25-136.45).

### 3. S1: printed string repeats still rendered as hidden bow changes: Violins II 289/292, violas 62/70/79, basses 144/156/168/253/265 (measured; audibility in the master inferred)

**Method.** I listed every printed, untied same-pitch repeat in `mockup-events.tsv` (100 places). For each I measured the stem dip and the re-attack in 50 ms windows, c37 against c38. The drier hall changed these by only 0-0.6 dB:
- Printed separate repeats: median dip 4.2 -> 4.4 dB.
- Fast figures (notes under 0.34 qn), median onset contrast: Flute 1 5.3 -> 5.4 dB, violas 5.2 -> 5.3 dB.

The drier hall did not separate the weak cases below. Each needs a change in the rendering.

**Violins II, bars 88-89 (qn 289, 292).** v600 prints three separate notes: A flat 4 at 286, 289 and 292, pp con sord. "Change bow at will" starts only at 292, with a tie.
- Now 289 is a `REBOW_AT` piece whose `rebow_fills.json` shape ("Violins II" "289": -3 dB, then +9.6 dB at +0.36 s) hides the bow change completely: dip 0.4 dB, re-attack 1.9 dB.
- 292 is merged, and `NOTCH_SKIP` drops its notch: dip 2.2 dB.
- Fix:
  - Remove 289.0 and 292.0 from `NOTCH_SKIP["Violins II"]`, and set `MERGE_NOTCH_AT["Violins II"][292.0] = 12`.
  - In `rebow_fills.json` "Violins II" "289", scale the lift points from +0.08 to +0.56 s by 0.6, so the new bow keeps about a 3 dB sag instead of being flattened.
  - Target: 2.5-4 dB dip and re-attack at 289 and 292 on the stem, with no hole over 6 dB.
- The "Violas div" A flat 3 at 289/292 is the same printed case: dip 2.2 / 0.4. Its re-bows sit at 288.6 and 291.7, which are not the printed bows. If the 289/292 Vln II change works, move them to 289.0/292.0. These notes are 3.5 s long, under the 4.5 s loop limit, so loop sync is not a risk. Then refit the two shapes.

**Violas, bars 21-27.** Unslurred repeated notes are merged by the string merge rule with the soft 8 CC notch. They play as one note (c38 stem dip / re-attack):

| Track | qn | Dip | Re-attack | Master dip |
|---|---|---|---|---|
| Violas | 62 | 0.4 | 2.4 | 0.8 |
| Violas div | 70 | 0.8 | 2.5 | n/a |
| Violas div | 79 | -1.5 | 3.3 | n/a |

- Violins II 50 needed 18 CC to reach a 5 dB dip (c34).
- Fix: `MERGE_NOTCH_AT["Violas"] = {62.0: 16}` and `MERGE_NOTCH_AT["Violas div"] = {70.0: 16, 79.0: 16}`. These are CC11, so pre-hall. Check that the split track is built under the name "Violas div".
- Target: a 2.5-4 dB dip on the stem.

**Double basses.** These are Sus MAX repeats with the 0.03 qn same-pitch gap:

| qn | Dip (dB) | Re-attack (dB) | Bar context |
|---|---|---|---|
| 144 | 1.4 | 2.6 | the 144 note also starts a new slur |
| 156 | 1.6 | 6.5 | |
| 168 | -0.5 | 7.4 | |
| 253 | 1.2 | 5.1 | |
| 265 | 1.0 | 7.7 | bar 80 cadence |

- Fix: `REP_RETONGUE_AT["Double basses"] = [144.0, 156.0, 168.0, 253.0, 265.0]`. That path in `build_track` is not family-gated, and gives a 0.06 qn gap.
- If the dip stays under 2 dB, add a pre-hall CC7 fall (127 -> 100 over the last 0.12 s before each onset, back to 127 at the onset) through `CC7_POINTS["Double basses"]`.
- Target: a 2-4 dB dip.

### 4. Legato joins in the exposed wind and horn solos are 1-3.5 dB deeper under the drier hall (measured)

**Evidence (measured).** On connected joins over the whole score (781), the hole under the lower body (200 ms windows for winds, 100 ms for the rest):
- Median 1.6 -> 1.8 dB.
- Joins of 5 dB or more: 53 -> 66.

Most of the new ones are in solo lines, where the master follows the stem:

| Join | Hole c37 -> c38 (dB) | Master at the join, c38 |
|---|---|---|
| Flute 1 130 (bar 41) | 2.5 -> 6.0 | 2.4 dB dip (c37 1.1) |
| Flute 1 131.5 | 4.5 -> 5.7 | 2.3 dB dip |
| Flute 1 271 (bar 81) | 5.2 -> 6.7 | n/a |
| Oboe 1 143 (bar 45) | 3.5 -> 5.6 | n/a |
| Oboe 1 146 | 6.0 -> 7.4 | n/a |
| Horn 1 193 (bar 58) | 4.7 -> 6.9 | n/a |
| Bassoon 1 256 (bar 77) | 3.2 -> 5.6 | n/a |

c38 refit only joins over 6 dB on the 30 ms measure.

**Fix.** `build/early_fills.json`, dB = hole - 3, held to the sag minimum, each checked against the 30 ms peak for overshoot (kit §6). Apply them as a stem fix plus `--mix-only` as in c38, or as part of the build:
- Flute 1 "130": raise the existing fill by 1.5 dB.
- Flute 1 "131.5": new {db 2.7, pre_s 0, hold_s 0.2}.
- Flute 1 "271": new {db 3.5, pre_s 0, hold_s 0.3}.
- Oboe 1 "143": 4.4 -> 5.5.
- Horn 1 "193": new {db 3.5, hold_s 0.3}.
- Bassoon 1 "256": new {db 2.5, hold_s 0.15}.

Leave Oboe 1 146 alone: it was removed in c34 for a 2.5 dB overshoot. Leave Flute 1 111 alone: it is already at 7.9 dB.

**Target.** Each listed hole at 4 dB or less, with no 30 ms peak over the louder body by more than 2 dB.

**Not a finding.** The string joins over 7 dB (Violins I/II 80, celli 140 and 142.5, Violins I 251.5) dip only 1-3 dB in the master. The actor already tried and reverted Violins I/II 80.

### 5. Horn 2, bar 62 (qn 208): the ff tenuto D flat 4 repeat is still not re-tongued (measured; masked in the tutti)

**Evidence (measured).**
- On the stem the level drifts down across the onset: -22.9, -23.3, -24.0, -25.0, -25.7 dB over 207.8-208.05. There is no new peak: re-attack 1.4 dB, dip 3.1 dB.
- A volume step from +7.1 to +4.6 dB falls exactly on 208, which hides the attack further.
- The master shows no dip at 208 (0.9 dB): the ff tutti covers it.

**Correction to c38 A #3.** The 1FH KS Master does have "LegRep RRx4" (key 34) and "Leg Slur Rep MAX" (key 84) (`ks_maps.json`). Both are slurred or legato repetitions. This is an unslurred tenuto stroke, so a Sus re-tongue is the right model.

**Why it is not re-tongued now (read).** The 204 note is on the Leg row with no slur, so the generic `WIND_REP_RETONGUE` path skips it.

**Fix.**
- `REP_RETONGUE_AT["Horn 2"] = [208.0]` (0.06 qn gap).
- `CC7_POINTS["Horn 2"] = [(207.7, 127), (207.92, 100), (208.0, 127)]`: a pre-hall fall of 2 dB into the gap.
- Move the +7.1 -> +4.6 step to start at 208.1.

**Target.** A 3-5 dB dip before 208 and a return to body level by +0.15 s. Low priority.

### 6. Patch options (inferred)

- **Bars 17-22 violin solo.** The Solo Violin library would give the solo a single player's timbre and linked CC1 vibrato (p.75). Its Leg Slur or Leg Lyr Vib patch fits the slow tempo (p.80). This is the largest timbral gain for the solo, but it is not installed (MANUAL-GAPS #3). Until then the DIV A track is right.
- **Basses 4 soli, bars 65-70 and 87-92.** `Basses KS Master DIV A.oib` (MANUAL-GAPS #8) remains the one installed patch change with a timbral gain in this lens.
- **Brass portato rows for the bar 61-62 tenutos.** Still not needed. Every brass tenuto except Horn 2's 208 re-articulates.

## Checked and fine (measured)

- **Re-bows.** 200 ms dips at re-bows are 5 dB or less on every stem. Steps over 3 dB are Violins II 263.92 (+5.6, inside the cadence crescendo, as in c37), Violins II div 113.7 (+5.3), and the morendo pieces 303.x. The basses' 220-238 pedal SD is 1.95 dB (c37 2.04).
- **Loop pulse.** No loop pulse. Autocorrelation at 3.95 s of the 100-300 Hz band and of the centroid is at most 0.19 on the master final chord (292-304), on the basses' pedal and master over 220-238, and on Violins I and violas over 292-304.
- **Legato rows.** No chord or simultaneous onset on any Leg row, on any track.
- **Pizzicato, bars 37-44.** The -6 dB arrival is +0.019 s (violas) and +0.022 s (basses) after the score onset.
- **Tremolo entries at 204, 208, 212 and 216.** No hole on any section.
- **Timpani.** Rolls at 226-237.5 have a 100 ms step SD of 7.39 dB (c37 7.37). Strokes at 172, 203, 209.5, 277, 278.5 and 279 are within 1.5 dB of c37.
- **Harp.** Rolls run from the bottom at 0.035 qn per note.
- **CC15 mutes.** Every change falls in a rest. The horn mutes at 271.5 take Horns 3 and 4: v600 prints con sord. in both parts.
- **Trombone 1 218 accent.** 2-5 kHz attack minus body is -15.7 dB, and the accent stands about 2.5 dB over its neighbours.

## Do not touch

- fx_volume 0.095 and the 160 Hz hall low cut.
- Trombone 1's velocities, accent swells and the 218 accent. Change only the two CC7 floors in finding 1.
- The violas' Detache portato with its leads.
- The bars 61-64 tremolo rows and sf lanes.
- Every re-bow and loop fit not named in finding 3. This includes the final-chord points of Violins I, violas, celli and basses, the bar 66 down-bow re-bows and the opening chord.
- `WIND_SLUR_REP_MERGE_SKIP` for Flute 1 136.
- The pizzicato rows and timing.
- CC15 placement.
- The Violin I solo on DIV A with its v72-80 legato velocities.

# Cycle 11, critic B (balance and levels), on the c10 render

Method. Levels are K-weighted (BS.1770 shelf and high-pass applied in the frequency domain) energy means on the stems and master in `cycles/c10/render/` (after the c10 stem fix), placed on the score with the parts.json tempo map. Spans are in score qn; bar b starts at qn 3(b-1). "Per beat" means 1 qn windows. Plain-RMS history comes from each cycle's `metrics/metrics.json` (`bar_db`). Note data (velocity, CC1, CC11, vol_db, row) comes from `build/parts.json` and `cycles/c09|c10/build_render/parts.json`. Marks come from `build/mockup-events.tsv` and score pages 2 and 7 (pdftoppm). K and plain values share no common scale with LUFS; compare them with each other. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c11-B/` (deleted).

## Manual notes (cycle 11, slot B: group B5, May 2021 HO manual PDF pages 114-115, 154-155, 158-159, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.114-115: percussion categories. In the Basics kits, CC11 and velocity set loudness, velocity selects the dynamic layer (up to 16 levels), and the felt timpani long hits alternate LH and RH | Timpani on `Timpani Flt KS` (its own patch, p.123-124), not a kit | Yes (measured in parts.json). Timpani velocities v41-125 (quartiles 64 / 80 / 93, 182 notes). The track gets no CC11; it gets CC1 for the roll layers and CC7 (138 points) for the c04 damping. So loudness comes from velocity and the envelope, as the page describes. Hand alternation is `TIMP_RH_ALT`. The rolls rank well under the theme in every tutti (101-120: timpani -32..-41 K against Violins I -24..-26). |
| p.154: Humanizer (random note-on/off delay, velocity, tuning, volume, pan) | every track | Correctly not used (read). I decoded all 31 saved states in `jobs/*.b64`, and none contains a MIDI-tool filter. Renders stay repeatable, which the per-onset trim tables depend on. |
| p.154-155: MIDI Compressor on velocity or one CC; notes under the threshold are not played | every track | Correctly not used. Level range is handled by `deliver_master.py` after the mix. A velocity compressor would also flatten the timpani's 16 velocity layers. |
| p.155: MIDI Echo | none | Not applicable. |
| p.158: Automation window, macros | Opus mixer, mics, reverb | Not used, by design. Every level lives in parts.json (CC1 / CC7 / CC11 before the hall, vol_db after it) and mix.json. |
| p.159: MIDI Controller Mapping; "avoid conflicting MIDI CC messages" | every CC the pipeline sends | Yes (read). Every KS Master maps controllers 1, 5, 7, 10, 11, 15, 22, 36, 64, 65, 68, 69 to their own numbers, and the string masters also map 70. The harp and harmonics states have no CC1, and the timpani state has no CC1 or CC11. parts.json sends CC1 on 29 tracks, CC11 on 30, CC15 on 7, CC70 on 2, CC7 on 1, plus the round-robin reset (CC16) on 5 tracks. CC16 is Opus's preference-level reset (2025 p.92), not a controller map, so nothing conflicts. Balance relevance: on the clarinets and brass, CC1 crossfades the dynamic layers (`CC1_DYN_TRACKS`). Any rule written in "dynamic-lane units" therefore moves those tracks by layers, not by a small CC11 amount. That is the cause of finding 1. |

## Standing checks (Dan's ears), measured on c10

- **Loop pulsing (item 8): none.** Autocorrelation at 3.95 s of the detrended level / 100-300 Hz band / spectral centroid. Violins I 0-23 +0.16 / -0.25 / +0.02. Violins I 1089-1128 -0.10 / -0.03 / -0.06. Violins I 420-445 -0.58 / -0.58. Horn 1 1110-1128 -0.34 / -0.19 / -0.10. Celli 605-624 -0.25 / -0.26 / -0.20. Celli 1070-1091 -0.28 / -0.32 / -0.15. Horn 4 drone 456-504 -0.12 / 0.00 / -0.10. Master 1089-1128 -0.15 / +0.13 / -0.17.
- **S3 (subito).** Master in 50 ms frames from 0.2 s before the mark. qn 360: -31.0, -31.5, -35.7, -38.4, -37.9, -37.3, -35.4. qn 828: -35.9, -38.6, -42.0, -42.7, -41.1, -38.6. No step to silence. R Strings decays smoothly under both (360: -41.5 to -48.5 over 0.5 s).
- **S1 (repeats).** The theme head's B-B eighths at 37 / 37.5 dip 4.6 dB on the Violins I stem and 2.9 dB on the master. The c10 pizz. violas fix measured below.
- **Low end (tuttis).** 20-100 Hz share of the master: 101-120 -23.2, 301-320 -20.9, 333-339 -22.5 dB (Dvořák whole-piece -21.7). Not boomy. Basses carry 33 / 46 / 84 % of that band and timpani 68 / 45 / 5 %.

## Findings, ranked by what a listener would hear

### 1. c10's wind phrase-shape scale (x1.4) acted on the clarinets' CC1, which on these tracks is the dynamic-layer control. It raised Clarinets 1-2 by 2.6-4.5 dB in the second idea (bars 46-52) and Clarinet 1 by 2.7-3.9 dB in the trio's ff return (bars 210-211). Their mf accompaniment and doubling now sit level with or over the f espress. strings and over the wind melody (measured)

**Score (pages 2 and 7).**
- Bars 45-56: the second idea. The melody is in Fl 1, Ob 1 and cor anglais (mf espress.), Violins I-II and violas (f espress.), with the celli espress. Clarinets 1-2 (mf, two-voice chords) and Horns 1-2 (mf tenuto chords) accompany.
- Bar 209: Violins I-II "f espress." carry the trio tune. Clarinet 1 "mf espress." doubles Violins II's line.

**Cause (read and measured).** `PHRASE_SHAPE` offsets are in dynamic-lane units: CC11, or CC1 on `CC1_DYN_TRACKS` (score_to_parts.py line 949, `ps_cc1` at line 3344). c10's `"family_scale": {"wind": 1.4}` (score_config.py line 775, phrase_off at line 3449) therefore multiplied the clarinets' CC1 arch. CC1 crossfades the clarinet's dynamic layers.
- The c09 -> c10 data diff for Clarinet 1 over 135-150: CC1 77-79 -> 81-84. vol_db, CC11 and velocities are identical.
- The c10 actor expected about +0.4 dB ("not measured separately").
- c09 -> c10 plain-RMS `bar_db` deltas:
  - Clarinet 1 bars 46-52: +4.0, +3.9, +3.9, +2.6, +2.6, +2.6, +2.7; bars 210 / 211: +3.9 / +2.7.
  - Clarinet 2 bars 47-52: +3.6, +3.5, +2.6, +4.5, +4.4, +3.9.
  - No oboe, flute, cor anglais or bassoon bar moved more than 0.6 dB at its 90th percentile.

**Measured, second idea (K, span means):**

| qn | Violins I | Oboe 1 | Flute 1 | Cor anglais | Clarinet 1 | Clarinet 2 | Horn 1 |
|---|---|---|---|---|---|---|---|
| 138-144 (bars 47-48) | -33.2 | -35.3 | -38.7 | -37.9 | **-33.1** | -36.5 | -35.8 |
| 144-150 (bars 49-50) | -32.6 | -35.9 | -35.0 | -40.7 | **-33.5** | -34.8 | **-33.0** |

- Per half bar at 142.5-144: Clarinet 1 -31.0 / -31.8 against Violins I -37.7 / -30.7 and Oboe 1 -40.5 / -37.6.
- In the later statements the same accompaniment sits 4-9 dB under Violins I: 372-384 Clarinet 1 -42.4 against -33.6, and 840-852 -39.5 against -35.8. The mapping is consistent everywhere except the first statement.
- Horn 1 at bars 49-50 has been level with Violins I since c00 (plain -34.9 / -32.6 against -33.4 / -34.7). Rimsky-Korsakov (Principles p.23) gives one horn the weight of two woodwinds, so a mf horn chord tone needs to sit clearly under the strings' f espress. (inferred).

**Measured, trio return (K, per beat):**
- qn 627 / 628: Clarinet 1 -32.7 / -30.7, against Violins I -35.4 / -35.6 and Violins II -36.9 / -35.4.
- qn 640 / 641: Clarinet 1 -33.6 / -33.3, against Violins I -37.5 / -35.4.
- Bar means: 210 Clarinet 1 -32.7, Violins I -34.9, Violins II -36.6. Bar 214: -34.4 / -34.6 / -35.7.
- On top of the CC1 rise, the soft-tune trims from c03-c08 add to the same notes. These are the pitch trims G#4 +4, B4 +4.5 and C#5 +4.5, held into the next note by `LEG_JOIN_TRIM_HOLD` (`leg_join_holds` [627, 629, 4.5], [639, 640, 4.5]), and the note trims 629 +4, 634 +3.5 and 650 +4, copied in c08 from the solo statement 168 qn earlier. Together they put vol_db at +5.7..+6.8 over 627-629 and +6.4 at 640, while Violins I's vol stays at 0 to +1.5.
- Research FINDINGS part 6 ("doublings share one curve, with each track's level trim on top") is broken here: the doubling clarinet carries per-note boosts that the violins do not.

**Fix.**
1. Generic, in `tools/score_to_parts.py` `phrase_off`: a new PHRASE_SHAPE key `"family_scale_skip_cc1"` (default False). When True, `family_scale` is not applied on tracks where `ps_cc1` is true. In `build/score_config.py`: `PHRASE_SHAPE = {**PHRASE_SHAPE, "family_scale_skip_cc1": True}`. Expected: the clarinets return to their c09 levels in bars 46-52 and 210-211 (-2.6..-4.5 dB). Flutes, oboes, cor anglais and bassoons are unchanged.
2. `build/roles.json`: "Horn 1" `[138, 153, -3]`.
3. Trio return only. Add the 624-672 onsets of Clarinet 1's boosted pitches to `build/pitch_trims.json` "Clarinet 1" `_skip_onsets`: 624, 627, 634, 638, 639, 646, 648, 657, 658, 660, 661. Remove the positive copies in `build/note_trims.json` "Clarinet 1" ("629.0", "634.0", "650.0", "659.0", "662.0"). Keep the negative ones (661 -2.5, 666 -5.5) and leave the 456-504 solo statement as it is.

**Targets (K).**
- 138-150 span means: Clarinet 1, Clarinet 2 and Horn 1 each at least 3.5 dB under Violins I and at least 1 dB under Oboe 1.
- 624-645 per beat: Clarinet 1 at least 2 dB under Violins I on every beat where Violins I sounds, and never over Violins II.
- The trio's solo tune 456-504 within 0.5 dB of c10.

### 2. The basses' arco G sharp 1 (MIDI 32) plays 8-10 dB over every other bass note at the same controls. A pp held note rises to the celli's mp tune in the trio (bars 170 and 178), and the f bass line becomes the loudest string in bar 48 (measured)

**Measured.**
- Per-pitch fit: each bass note's level after vol_db, regressed on CC11 and velocity per row. G#1 reads +9 dB at 142 (Leg Slur MAX, v118), +9 at 507 and +9 at 531 (Sus MAX, v41, CC11 46), and +4 at 651. The other pitches have medians within ±3 dB.
- Trio, bars 169-171 (half-beat windows): the basses' G#1 at 507-510 rises to -39.6 / -38.5 / -39.8, the same as the celli's mp tune (-37.9 / -39.7 / -38.2). The other bass notes of the phrase sit at -48..-53 (510-516, same v41, CC11 46-48, vol 0). At 531-534: basses -39.4 against celli -38.5. Plain RMS bar 170: basses -40.2, celli -39.5. The score (page 7) prints the basses pp arco and the celli mp espress.
- Bar 48 (142-144): basses -34.7 / -32.5 / -30.5 / -31.9, against Violins I -37..-39 and celli -45..-47. That is 3-8 dB over the violins' f espress. melody.
- Bar 218 (651-654): basses -29.4..-37.6 against celli -36.4..-39.9.
- The fault dates from the port (c00 bar 170: basses -43.5, celli -41.8 plain). `pitch_trims.json` already cuts G#1 by 5 dB, but only on "Pizz RRx4" (`_arts`).

**Fix.** In `build/note_trims.json` "Double basses": `{"142.0": -6, "507.0": -7, "531.0": -7, "651.0": -3}`, with `NOTE_TRIM_RAMP_S` "Double basses" `{142.0: 0.1, 507.0: 0.1, 531.0: 0.1, 651.0: 0.1}` (the default 0.6 s ramp is most of a 3 qn note at quarter 228). The broader alternative is `"_all_arts_pitches": [32]` in `pitch_trims.json`, which applies the pizz -5 to every row. It would also lower the arco G#1s at 339, 597 and 627, which read only +1..+2. Simulate with `stem_fix.py --out` before writing (LEARNINGS c09: `_all_arts` trims moved a stem about twice their value).

**Targets.** Each G#1 within 2 dB of the neighbouring bass notes. Basses at least 5 dB under the celli in bars 169-176. Basses under Violins I and the celli in bar 48.

### 3. Bars 125-127 (qn 372-382): Horn 4's sub. p crescendo to mf rises on the early hairpin curve and sits level with Violins I, over the pp espress. entries of Flute 1 and Oboe 1 (measured)

**Score.** At 360, Horns 2 and 4 play sub. p, both with crescendos to mf (Horn 4 to 382, Horn 2 to 384). Violins I-II carry the espress. line. Flute 1 and Oboe 1 enter at 372, pp espress.

**Measured (K).**
- 372-378 span means: Violins I -38.2, Violins II -38.9, Flute 1 -41.7, Oboe 1 -45.4, **Horn 4 -39.3**, Horn 2 -44.7.
- Per beat at 376: Horn 4 -36.9 against Violins I -40.1 and Flute 1 -40.7.
- Horn 4's CC1 goes 59 -> 72 over 372-381. Its notes jump from -46.6 (369) to -40.3 (372).
- Cause (read): Horn 4's hairpin is 10 qn long, just under `cresc_long`'s `min_qn` 10.5, so it takes the early `"cresc": (0.4, 0.7)` curve. Horn 2's 12 qn hairpin takes the late curve and stays 6.5 dB under Violins I.
- Lowering `min_qn` to 10 would also catch the 10 qn sfp < hemiolas at 300 and 900, which c10 kept off the long curve on purpose.
- In the reprise (840-846), Horn 2 alone sits 3.6 dB under Violins I.

**Fix.** `build/roles.json` "Horn 4" `[372, 381.5, -4]`.

**Target.** Horn 4 over 372-381 at least 3 dB under Violins I and no louder than Flute 1. The mf arrival at 382 unchanged.

### 4. Coda bar 332 (qn 993-996): the low brass and trumpets reach their f level on beat 2-3, a beat before the printed f, and then stay flat or fall into the arrival (measured)

**Score (page 12).** Trumpets, trombones, bass trombone and tuba enter pp at 993 with a crescendo to f at 996. Horns 1-2 enter p, crescendo to ff. The strings play the theme f, rising to ff at 996.

**Measured (K, per beat; 995 is the last beat of the crescendo, 996-998 the f arrival):**

| track | 993 | 994 | 995 | 996 | 997 | 998 |
|---|---|---|---|---|---|---|
| Tuba | -48.6 | -40.3 | **-35.9** | -37.1 | -37.2 | -39.7 |
| Trombone 1 | -47.5 | -45.8 | **-38.6** | -37.8 | -35.8 | -35.9 |
| Trumpet 1 | -51.3 | -40.3 | -38.5 | -33.1 | -36.4 | -36.3 |
| Horn 1 | -49.1 | -40.7 | -34.9 | -31.0 | -31.3 | -31.6 |
| ten brass summed | -33.7 | -29.4 | -27.7 | -24.6 | -24.1 | -25.7 |
| five string sections summed | -24.5 | -24.5 | -25.4 | -21.3 | -20.9 | -21.7 |

- At 995, the brass sum is 2.3 dB under all the strings together. Horn 1, the tuba and Trumpet 1 are each louder than Violins I (-39.9, between its staccato notes).
- The 3 qn crescendo takes `"cresc": (0.4, 0.7)`. c10's roles cut the horns only (Horns 3-4 -4 over 990-995.8, Horns 1-2 -3 over 993-995.8).
- A brass swell from pp lands on the downbeat (Rimsky-Korsakov p.23: brass swell pp to ff very well; inferred for timing).

**Fix.** `build/roles.json`, all ending before the arrival:
- "Trumpet 1", "Trumpet 2" `[994, 995.9, -3]`
- "Trombone 1", "Trombone 2", "Bass trombone", "Tuba" `[994, 995.9, -4]`
- Horns 1-2: change -3 to -5 over 994-995.8

**Targets.** Each brass track at 995 at least 3 dB under its own 996-998 mean. The brass sum at 995 at least 5 dB under the string sum. Master 993-996 still rising (c10: -22.3 / -22.1 / -20.1 / -17.1).

### 5. Two c10 trims short of target: the reprise violas' pizz. beat 2, and Oboe 2's F5 (measured)

- **Violas pizz. pp, 756-810** (c10 B #5). Note level, first 0.1 s:
  - Violas: beat 2 -53.1 (n 14), beat 3 -49.8.
  - Violins II: beat 2 -51.5, beat 3 -50.1.
  - The sections now match within 2 dB, but the violas' beat 2 is still 3.3 dB under their beat 3 (target 1 dB). The +4 role and +3 trims gave +4.4 dB instead of the expected +7.
  - Fix: `build/note_trims.json` "Violas" beat-2 onsets (757 ... 799) +3 -> +5.5, steps as now.
- **Oboe 2 F5** (c10 B #2, `{"77": -4, "_all_arts": true}`).
  - At 903-905 (sfp <) it is still 3-5 dB over Oboe 1 (-33.0 / -31.3 / -31.8 against -38.7 / -36.2 / -34.0), at CC11 88 against its own E flat 5 at CC11 108 (-33.6).
  - At 990-991 it sits 3-4 dB under the F#5 before it (-48.9 / -44.2 against -44.9 / -41.1) on a rising crescendo.
  - Fix: keep the pitch trim and add `build/note_trims.json` "Oboe 2" `{"900.0": -2, "903.0": -3, "990.0": 3}` with `NOTE_TRIM_RAMP_S` 0.1.
  - Targets: Oboe 2 within 1 dB of Oboe 1 at 903-905, and 990 between its 987 and 993 neighbours.

## Measured and in balance (for the record)

- **Theme A 13-28.** Violins I -34..-41 over the basses' pizz. (-48..-56), the celli (-46..-55) and the timpani. Counterstatement 29-36: Flute 1 / Oboe 1 / Violins I trade at -41..-48.
- **Sub. p.** 121-124: Violins I -35..-41, Violins II and violas -41..-46, Horns 2 / 4 -43..-48. 277-280: Flute 1 -38..-43 and Oboe 1 -39..-46 over violas -45..-48, clarinets -45..-51 and horns -48..-52.
- **Trio.**
  - Clarinet 1 -34..-42 over the harp (-44..-58) and the drone (Horn 4 -49.5..-50.4, Horn 3 -53).
  - Celli -36..-44 over Violins II con sord. (-46..-49).
  - Violins I 3-4 dB over the celli at 177-182 (the octave doubling leads).
  - Oboe 1 -38..-40 at 185-188.
  - Violas div within 1-3 dB of the violas at 209-224.
  - c10's Horn 1 / Flute 1 roles at 221-222 hold (Horn 1 -41.4, Flute 1 -36.9 against Violins I -34.8 / -33.2).
- **Codetta 225-236.** Oboe 1, Clarinet 1 and Bassoon 1 lead in turn (-35..-42) over violas, Violins II, harp and the pedal.
- **Tuttis 101-120.** Trumpets -36..-38 (11-13 dB under Violins I, present, not on top). Trombones and tuba -35..-41. Timpani -32..-41.
- **Summit 336-338.** Violins I -18.4..-20.8, Violins II -21.6..-23.4, woodwinds -25.8..-34.4, horns -31.5..-33.4, trumpets -33.4..-37.5, trombones and tuba -33..-39, timpani -31.5..-34.5. Strings over woodwinds over brass, as printed.
- **Solo 349-356.** Solo -35..-45, Flute 1 4-6 dB under, Violins II "la metà" 8-12 dB under. Horn 1's motto 357-360 -35.5..-38 over violas -44..-48.
- **The c10 coda-build fix (B #1) holds.** Every wind and horn is under Violins I in bars 329-332, and the master rises 329-333.

Do not touch: c10's `cresc_long` curve on the coda build and its horn roles; the summit's string-over-woodwind-over-brass order with no brass accents and `UNI_BOOST`; c09's tutti violas +4 and the flute / cor anglais f staccato roles; c08's Violins II trims and celli roles at 624-672; the trio's harp caps and Clarinet 1's solo-tune trims at 456-504; c10's Horn 1 / Flute 1 roles at 660-669; the solo / flute / celli roles at 349-356 and Horn 1's close role; the timpani roll trims and `TIMP_DAMP_AT`; the sub. p and sfp CC11 drops.

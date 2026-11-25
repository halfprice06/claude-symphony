# Cycle 15, critic A: articulation and phrasing, and the per-note volume envelope (on the c14 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB on the dry stems of `cycles/c14/render/`. "Measured" = a number from the c14 stems, `build/parts.json` or an Opus state in `jobs/`; "inferred" = reasoned, not tested.

Method for the envelope (measured). I ran a copy of `tools/score_to_parts.py` in my scratch folder that tags every `vol_parts` item with the source line that appended it and writes each layer's dB curve; the layers sum to `parts.json` `vol_db` (median error 0.0 dB, 95th percentile 0.3 dB) and the rebuilt parts.json equals `build/parts.json` except for the re-bow note splits of three tracks. Slow layers: role rows longer than 2 qn, hairpin gains, chord cuts, the CC11-park level return, timpani roll shapes, held-decrescendo shapes, final fade. Per-note layers: everything else. The gain and the dynamic trims of `build_reaper.py` `vol_points` are slow and were left in. Movement I's test: per note, stem level from the score onset over 0.35 s (or to the next onset), and the same with a layer's mean over that window subtracted; "step" is the absolute level difference between consecutive notes of a line.

## Manual notes (May 2021 HO manual, PDF pages 89-94, read in full)

| Manual | Where it applies here | Does the render follow it |
|---|---|---|
| p.89-90: DIV A / DIV B are the left or right chair of each stand, Close mics only; "the loudness of a divisi part is not much less than if the whole section were playing" | Violin I solo bars 349-356 (DIV A), Violas div bars 209-224 and 349-356 (DIV B); basses' div. octaves bars 253-268 | Solo and violas: yes. Basses: no, both octaves on the full section with a -3 dB chord cut each (MANUAL-GAPS #9, still open) |
| p.90: mix the divisi Close mics with the non-divisi patch for the other mic positions | the same divisi tracks | Not used (c14 rejected Close + Main on divisi with numbers); no change asked |
| p.91: Détaché "longer than staccato but come to a well defined end" | plain and tenuto quarters next to staccatos in the theme and the tutti countermelody | Not used. The row "Detache" is in the 1st and 2nd Violins KS Masters (read in `ks_maps.json`), not loaded. Inferred candidate only |
| p.91: Sustain is looped; bow direction is a round robin; three vibrato levels | every held string note; the re-bows | Yes (AUTO_REBOW, fills) |
| p.91-92: Marcato Sustain "plays a marcato sample in addition to the multiple sustain samples. The marcato sample ends relatively quickly" | Violins I theme head, 39 notes on "Sus Marc LITE" (the accented half note and the two slurred eighths of nine figures) | Partly. Read in `jobs/23_1st_Violins_KS_Master.b64`: the row has overlay groups "V1 Marc Shrt rrx1/2" (release 295 ms) and release-trail groups at volume 2.8 (p) and 3.98 (mf), which is +9 and +12 dB. Each slurred eighth gets a marcato front and a loud trail (finding 2) |
| p.92: Flautando and Harmonics exist only in the 2nd Violins; harmonics sound two octaves above the fundamental, from G4 | Violins I harmonic E6, bars 141-149 | Yes: the two notes (qn 420 and 432.5) play on the Violins II track's "Harmonics" row (`score_config.py` line 700). BRIEF and the lens text ("no harmonic row") are out of date |
| p.92: "the Sustain patch ... played pp with no vibrato (i.e., with the Mod Wheel pulled all the way down) achieves a similar sound" to flautando | Violins I ppp G sharp 5, bars 1-8 and 364-376 | Not followed: CC1 is 38-39 there (measured in parts.json). Inferred small gain; not ranked |
| p.92: Pizzicato is a round robin of 2 or 4 samples | all pizz. passages | Yes (CC16 resets from c07) |
| p.93-94: Spiccato Marcato MOD and Staccato Marcato MOD: CC1 "gives you the ability to control the accent of individual notes within a part"; Shorts MOD SPEED | metric weight and accents inside staccato lines | Not followed: the weight is 342 volume-envelope steps (finding 4). These are separate patches (02 Short / MOD COMBOS), not KS Master rows |
| p.94: Staccatissimo is "like Staccato, but with notes of even shorter duration"; Staccato On Bow stops the bow on the string | Violins I theme on "Staccatissimo RRx9" | Yes. Same-pitch pairs in Violins I's theme dip 5.0 dB median (7 pairs, bars 13-28), inside the 3-6 dB target (measured) |
| p.94: Repetitions: not a round robin, has release trails, "more realistic than just playing the same staccato note multiple times" | the theme's B-B and E-E eighths | Not used and not needed on the strings (dips above) |

## What the per-note layers do, line by line (measured)

Whole movement, all 31 tracks: the per-note layers carry 73 % of the envelope's travel (sum of absolute dB changes), the slow layers 27 %. Largest per-note layers: row trims 16.3 % (310 items), pitch trims 17.0 % (574), accent swells 8.0 % (235), level shapes 5.5 % (91), timpani attack 5.4 % (86), beat weight 4.2 % (342), note trims 4.1 % (127), early fills 2.5 % (66). 2,288 notes have a slot of an eighth or less; 765 of them (33 %) have more than 1 dB of envelope movement inside the note and 282 more than 3 dB. The layers that move inside those short notes: row trim 282 notes, pitch trim 184, chord cut 100 (violas), CC11-park return 84. The written envelope has 313 excursions of 3 dB or more that go out and come back within 45 ms while a note sounds.

Median note-to-note step, with the per-note layers / with them subtracted; "layer" names the one that makes the difference (median step with only that layer removed).

| line | with / without | verdict | layer |
|---|---|---|---|
| Violins I theme, bars 13-28 (36-84) | 2.0 / 2.4 | helps | c14 theme rows (3.1 without them); beat weight hurts (1.8 without) |
| Violins I reprise theme (756-804) | 1.9 / 2.2 | helps | theme rows |
| Violins I counterstatement (84-132) | 3.5 / 2.7 | hurts | beat weight (2.7 without) |
| Flute 1 counterstatement (84-132) | 2.9 / 3.7 | helps | pitch trim (3.9 without); accent swell hurts (2.3) |
| Oboe 1 counterstatement | 2.2 / 2.4 | no effect | row trim no effect (2.2) |
| Second idea 132-168: Violins I, Flute 1, Oboe 1 | 1.5 / 1.5, 4.3 / 4.3, 3.2 / 3.0 | no effect | |
| Fugato: celli 168-216, Violins I 204-216 | 3.2 / 2.8, 4.3 / 3.3 | hurts | beat weight |
| Fugato: violas 180-216, Violins II 192-216, celli 864-900 | 3.6 / 3.6, 2.0 / 1.9, 3.2 / 3.0 | no effect | beat weight helps Violins II (2.6 without), hurts violas (3.2) |
| Violas fugato reprise 876-900 | 2.0 / 2.7 | helps | beat weight |
| Tutti 312-360: Violins I, Violins II, Flute 1 | 2.0 / 2.3, 1.7 / 1.5, 3.2 / 3.4 | no effect | Flute 1 row trim on 43 notes: 3.1 without |
| Trumpet 1 repeated quarters 300-360 | 1.5 / 1.5 | no effect | |
| Second idea 360-420: Violins I | 2.4 / 2.1 | hurts | accent swell, level shape |
| Clarinet 1 second idea 360-420, trio tune 456-504, return 624-672, codetta 672-708 | 2.6 / 3.5, 2.3 / 4.6, 3.8 / 4.9, 1.1 / 6.4 | helps | pitch trim (3.7-4.9 without) |
| Celli trio tune 504-552, Horn 3 with them, Violins I 528-552 | 2.1 / 2.2, 2.9 / 2.6, 1.3 / 1.3 | no effect | |
| Oboe 1 trio middle 552-588; Clarinet 1 588-624 | 2.8 / 2.7; 4.5 / 4.1 | no effect; hurts | pitch trim |
| Violins I trio return 624-672 | 1.5 / 1.1 | hurts | level shapes |
| Oboe 1 codetta 672-708 | 3.0 / 4.9 | helps | early fills |
| Reprise second idea 828-864: Violins I / Oboe 1 / celli | 2.2 / 1.6, 2.5 / 3.1, 2.3 / 2.1 | hurts / helps / no effect | row trim (Violins I) |
| Coda build 984-1017 Violins I; solo 1044-1068; Flute 1 col solo | 2.6 / 2.6, 1.1 / 1.3, 3.0 / 3.0 | no effect | |
| Horn 3 coda recall 1020-1044 | 0.5 / 2.3 | helps | pitch trim |
| Pizz.: celli 6-90, basses 6-90, basses div. 756-804 | 2.0 / 3.6, 0.9 / 2.7, 1.3 / 4.1 | helps | plucked pitch trims |
| Timpani, all strokes | 2.1 / 2.2 | no effect | attack shape hurts (1.6 without), metric table helps (2.5 without) |

Shapes that are needed by this measure: the per-pitch level corrections (clarinets, horns, Flute 1, plucked celli and basses), the c14 theme-head rows, the oboe's early fills, the re-bow fills (not re-measured here; c14's numbers stand). Not needed: any movement inside a note of an eighth or less. With one level per short note (the per-note sum sampled at 40 % of the note, held from boundary to boundary, simulated on the stems) the median step of the 49 lines changes by 0.3 dB or less in 46 of them (Violas 876-900 improves 2.0 to 1.5).

## Findings

### 1. Row trims and pitch trims return to 0 dB between the notes of a run: a 5-9 dB sawtooth at eighth-note rate (measured)

Where: every staccato run of Flute 1, Flute 2, Oboe 1 (bars 29-44, 105-120, 305-320, 329-336) and the trimmed pitches of Clarinet 1, Horn 2, cor anglais; the violas' "non div." double stops of bars 105-120 and 305-320 (chord cut, 1.5 dB, 100 notes).

What: this is what Dan saw in REAPER. Oboe 1, bar 105 (qn 313-314.5), three staccato notes on "Stac DblTng RRx9" with `ROW_TRIM_DB` -5: the written envelope reads 0.1, 5.1, 0.1, 5.1, 0.1, 5.1 dB, one cycle per note. Flute 1, same bar: row trim +6 and pitch trim +3 (B5): -1.2, 7.8, -1.2, 7.8, -1.2, 4.8 dB. The comment in `score_to_parts.py` (row-trim block, about line 5733) says "Consecutive trimmed notes are one step (no bump at each join)", but segments merge only when the next note starts within 0.06 qn of the segment's end, and for a detached note the segment ends at the written note end (313.25 for a note whose successor starts at 313.41), so no staccato run ever merges. The pitch trim uses `trim_shape` with a 0.25 qn ramp (57 ms at quarter 264): on a staccato eighth it is a rise through the whole note and never reaches its value (c12 found the same on note trims).

Evidence: row trim moves more than 1 dB inside 282 short notes, pitch trim inside 184. Flute 1's same-pitch pairs dip 11.1 dB (bars 29-44) and 11.3 dB (105-120) because the envelope cuts each tail; target 3-6 dB. Simulation on the c14 stems with the two layers held as one flat level across each run (gaps under 0.16 s filled): Flute 1 dips 11.1 to 8.8 and 11.3 to 8.5 dB, median step 2.9 to 2.8 and 3.2 to 3.1; Flute 2 (312-360) step 3.4 to 3.2; Oboe 1 step 2.2 to 2.2 (84-132) and 1.9 to 2.5 (312-360, my flat value takes the run's extreme, so fit the level again); envelope travel of the two layers over 312-360 falls from 381 to 71 dB (Oboe 1), 516 to 120 (Flute 1), 501 to 87 (Flute 2). Removing row trims, pitch trims and beat weight from the envelope altogether halves the per-note travel of the whole movement (13,552 to 6,589 dB) and takes the notes with more than 3 dB of swing from 21.7 % to 16.7 %.

Fix, in order of preference:
- (a) At the source (inferred, needs a one-track range test). Opus regions carry an optional per-region `volume` (linear): 1,020 of 100,200 regions in `jobs/05_CL_KS_Master.b64` and 46,474 of 297,590 in the 1st Violins state have one as shipped. Add to `tools/build_reaper.py`, next to `rt_gain`, a function that multiplies or sets `volume` on every region whose `row` is a listed KS row and whose `keyMin..keyMax` contains a listed pitch, driven by `build/pitch_trims.json` (it already has the form track, pitch, `_arts` rows) and by a new `mix.json` key `"row_gain_db": {row: dB}` for `ROW_TRIM_DB`. Then set the corresponding envelope layers to zero. Rows with a dynamic threshold (`ROW_TRIM_DB` second value 72 / 80 / 100) can be limited to the groups whose name ends in f or ff. Clarinet 1's 12 `_skip_onsets` become note trims of the opposite sign. First test: Clarinet 1 alone, B4 +4.5 and A4 -2.5 as region volumes, envelope pitch trims off, a range render of bars 153-168 twice; pass if the per-note levels match c14's within 1 dB.
- (b) If (a) fails: keep the envelope but hold. In the row-trim block take `s1_` as the moved onset of the next note on the same row when it starts within 1.0 qn (new generic `ROW_TRIM_HOLD_QN`, default 0 = today's behaviour, scherzo 1.0). In the pitch-trim block give notes whose slot is 0.5 qn or less a flat step (ramp 0.04 qn centred on the score onset) held to the next onset, merged when the next note has the same trim. Same hold for the `chord` cut across gaps under 1 qn.

### 2. Violins I theme head: a 20 ms spike on the first slurred eighth, and the second eighth rings through the landing staccato (measured)

Where: the nine soft figures, first eighth at qn 41, 53, 71, 77, 287, 761, 773, 791, 797 (bars 14, 18, 24, 26, 96, 254, 258, 264, 266); landing staccato one beat later.

What, spike: c14's figure row holds the half note's lift `u` until 0.02 qn before the eighth's beat, while the older half-note row (-7.8 to -15 dB) returns to 0 by about 0.1 to 0.02 qn before it. For 20-30 ms the sum is at `u` alone. The written envelope jumps 7.3 (qn 40.97), 11.8 (52.98), 7.5 (76.98), 11.4 (286.98), 7.3 (760.98), 10.9 (772.98), 7.4 (796.97) dB and falls back. On the stem the 20 ms frame on the eighth's beat stands 3.4, 4.2, 1.1, 5.1, 3.8, 5.4, 3.3 dB over the frame after it; with the level-shape layer subtracted the level rises smoothly through the beat in all seven. The two figures without a lift (71, 791) have no spike. c14's check used 300 ms windows and could not see it.

What, landing: the second eighth's note-off is 109 ms before the landing's beat, yet its pitch stays 15-17 dB over the landing's pitch at -40 ms (harmonics 1-3, 40 ms windows) and the landing's pitch becomes the stronger one only 45-70 ms after the beat (qn 42, 288, 774, 798, 54, 78, 762). The stem level is flat (-39.4 to -39.6 dB at qn 42) from -160 ms to the beat: no separation. Cause (read in the state, inferred as the cause): the Sus Marc LITE release-trail groups play a one-shot trail at +9 dB (p) and +12 dB (mf) after every note-off, and the row's 120 ms release cap does not touch them.

The c14 question on S at 42 / 288 / 774 / 798 (-61 to -130 ms): the note is not early. It is the measure. The beat-weight step (+1.5 dB) starts at the landing's note-on, 45 ms before the beat, and the figure row steps +3 dB on the beat; both act on the ringing eighth, and S reads that rise as the onset. By pitch the landing is 45-70 ms late.

Fix:
- `build/score_config.py`, the c14 block (`_c14_lv`, line 1159 on): write one row per figure. End the older half-note row with the same crossfade (its last two points at `q_ - 0.02` and `q_ + 0.02`), or fold its level into the figure row so no two rows overlap at the beat. Check afterwards that no envelope point within 60 ms of the nine beats is higher than both neighbours by more than 1 dB.
- `build/mix.json`, Violins I: `"rt_gain_db": {"db": -9.0, "rows": ["Sus Marc LITE"]}` (the mechanism the horns already use on Sus MAX). Test on a range render of bars 13-28: pass if the landing's pitch is dominant by +20 ms and the half note's tail is not shorter than now by more than 2 dB at 140 ms before its end. If the trail is not the cause, cap the "V1 Marc Shrt" overlay groups' release (295 ms) at 120 ms through `sus_release_cap_ms` (it matches groups by a dynamic suffix today, so it needs a `"groups"` name option).
- Keep the figure's `b` level until the landing's beat plus 0.02 qn and do not start any step at the landing's moved note-on (see finding 4 for the beat weight).

### 3. A level step between two legato notes lands on the old note's last 60 ms: deeper join holes on Clarinet 1 and the cellos (measured)

Where: Clarinet 1 at qn 138 (bar 47), 399 (bar 134), 468 (bar 157, the trio tune), 840 (bar 281) and nine more joins; Violoncellos at 339 and 939 (bars 114, 314), 390, 594; Violins I at 155.5 (bar 52).

What: Clarinet 1's pitch trims are +4.5 (B4, C sharp 5), +4.0 (G sharp 4) next to -2.5 (A4) and -2.0 (C5), so the envelope steps 6.5-7 dB at a join. The step runs from 60 ms before the score onset to the onset, with the target's note-on at -35 ms: the old note is pulled down while it still sounds. Hole at the join (lowest 20 ms frame against the quieter neighbour body), with / without the per-note layers: 138: 8.1 / 1.7 dB; 399: 10.1 / 4.8; 468: 6.2 / -1.5; 840: 8.5 / 3.2. Thirteen Clarinet 1 joins have a per-note fall of 3 dB or more inside the old note's last 80 ms, all from the pitch trim. The trims themselves are needed (table above). Cellos: c14's row-level steps (`build/c14_row_levels.json`) on two consecutive notes return to 0 between -80 and -20 ms and come back at the beat, a 6 dB notch 60 ms wide: 339: 4.7 / -1.8; 939: 5.0 / -1.7; 390: 4.2 / -0.7; 594: 5.6 / 0.8. Violins I 155.5: the c13 row `[(155.2, 0), (155.25, -8), ...]` starts 0.3 qn before the staccato pickup and cuts the last 60 ms of the note before it by 5.8-8 dB (hole 9.0 / 1.0). All tracks: holes over 6 dB at 135 of 1,568 connected joins with the per-note layers, 113 without.

Fix: finding 1 (a) removes the clarinet case, because a region volume moves with each note's own sample through the transition. Otherwise, in `trim_shape` centre the step of a legato target 10 ms after the score onset with a 40 ms ramp instead of on the moved note-on. `c14_row_levels`: when the next note also has a step, crossfade from one value to the other on its score onset without passing through 0. Violins I 155.5 row: start at 155.46 with a 0.04 qn ramp.

### 4. Beat weight is 342 envelope steps that start before the beat and help no line consistently (measured)

Where: the string short rows in the Allegro spans (`SHORT_CC11_PARK["beat_db"]`: downbeat +1.5, the eighth after a beat -0.5), all five string tracks.

What: median step with / without this layer alone: Violins I counterstatement 3.5 / 2.7, cellos' fugato 3.2 / 2.9, violas' fugato 3.6 / 3.2, Violins I fugato 4.3 / 3.8, Violins I theme 2.0 / 1.8 (worse with it); Violins II fugato 2.0 / 2.6, violas 876-900 2.0 / 2.5, Violins I tutti 2.0 / 2.2, coda build 2.6 / 2.9 (better with it). Each step starts at the moved note-on, 45 ms before the beat on Violins I, so it lifts the ring of the note before (finding 2). The manual's own tool for weight inside a staccato part is CC1 on the Staccato / Spiccato Marcato MOD patches (p.93-94), and FINDINGS section 23 has the experts' short-note velocity follow the position in the beat.

Fix: set `"beat_db"` to None in `SHORT_CC11_PARK` and put the weight in velocity (`score_to_parts.py` already writes `metric_vel` for other rules: downbeat +6, the eighth after a beat -3 as a first value on "Staccatissimo RRx9", "Stac RRx9 / RRx14", "Spiccato RRx9"). Before the render compare on a range pass of bars 13-44: downbeat staccato minus the staccato after it should be +1 to +2 dB; if velocity moves the level by less than 0.5 dB (as c02 found on the wind row), leave the weight out rather than return it to the envelope. This removes 342 items and 4.2 % of the travel.

### 5. Timpani attack shape: 86 strokes with up to 8.5 dB inside the note, and a larger stroke-to-stroke step with it (measured)

Where: the Timpani track, every stroke that gets the attack shape (`score_to_parts.py` timpani block, the `env` appended near line 4617), 31 of them an eighth or shorter with more than 3 dB of swing inside the note.

What: median stroke-to-stroke step over all 181 strokes: 2.1 dB with every layer, 1.6 dB with the attack shape alone subtracted, 2.5 dB with the metric table alone subtracted. The metric table (42 items) earns its place; the attack shape does not by this measure. 52 % of the timpani's notes swing more than 3 dB inside the note, the highest share of any track.

Fix: build with the attack shape off for the single strokes of motive x (bars 3-12, 91-100, 253-272) and compare the strokes' 2-5 kHz first 80 ms against c14 on a range pass; keep it only on strokes where the stem shows the fault it was written for. Put stroke weight in velocity (the patch is velocity-layered; CC7 per articulation stays).

### 6. Accents: weight is there and there is no bite, but accented long notes speak late (measured)

Where: 264 accented notes of 0.25 s or more on Violins I, Violins II, violas, cellos, basses, Flute 1, Flute 2, Oboe 1, cor anglais, clarinets.

What: the swell is 0 dB at the score onset and at its value 30-40 ms later, so it does not peak late (the finale's fault is not present). Stacking over 4.5 dB happens on 7 notes only (Oboe 1 five, Clarinet 1 two; wind `GENTLE_ACCENT` db 3.5). The 2-5 kHz front (first 50 ms) is under the body on every track (-1.7 to -7.7 dB): no bite. But the first 50 ms of the accented notes is under their own body: Violins I -3.6 dB, Violins II -2.7, basses -4.2, cor anglais -4.2, Flute 1 -2.3, Flute 2 -2.7, against -0.6 to +1.3 for plain notes of the same length. The envelope is not the cause (with / without it within 0.5 dB); the Sus MAX front is slow. The swell does give the level over the note before: violas +2.5 with / +0.1 without, Violins II +2.1 / +1.2, Oboe 1 +0.8 / -2.0.

Fix: `GENTLE_ACCENT["wind"]["db"]` 3.5 to 3.0 (Movement I's cap). For the late front use what c12 measured (entry lead 0.03-0.05 qn on the accented Sus MAX notes of Violins I, Violins II and basses, `REATTACK_LEAD_AT` or the entry-lead table), not a larger swell. No new envelope rows.

## Do not touch

The c14 theme-head levels themselves (pair 2.5-3.7 dB under the half note; the rows help: step 2.0 against 3.1 without them), only their overlap at the beat; the pitch-trim values on Clarinet 1, the horns, Flute 1 and the plucked cellos and basses (they lower the step by 1-5 dB), only where they are applied; the oboe's early fills in the codetta; the re-bow fills; the timpani metric table; the accent swell's timing and the plain-sustain accents (2-5 kHz front under the body everywhere); Violins I staccato pair separation (5.0 dB) and Trumpet 1's repeated quarters (4.8 dB, 32 pairs); the harmonic E6 on the Violins II "Harmonics" row; the one-row legato refit of c14.

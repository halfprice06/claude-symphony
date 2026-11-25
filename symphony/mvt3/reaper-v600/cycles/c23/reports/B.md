# Cycle 23, critic B: balance and levels (on the c22 render)

Sources:
- the c22 stems and master, the delivered `mvt3-mockup-c22.mp3`, and the c21 and c19 stems for comparison;
- `build/parts.json`, `build/roles.json`, `build/mix.json`, `build/mockup-events.tsv`;
- score pages 7, 13 and 15;
- the 1TP and 1FH KS Master `.oib` files (read with zlib/json, nothing written).

I ran copies of the unchanged `tools/deliver_master.py` on the c22 master with edited `ride_trims` in a scratch `parts.json`. The base run reproduces the c22 mp3 exactly: -14.0 LUFS, LRA 11.9, limiter 6.0 / 4.3 / 4.7 dB at final / 223 / 263.

Method notes:
- Stem levels are mean power over 1/8-qn frames on the score's tempo map. "K" means a K-like weighting (60 Hz high-pass plus a +4 dB shelf at 1.5 kHz, from ffmpeg), mono sum.
- Bar loudness on the mp3 is the EBU momentary maximum over 400 ms windows lying wholly inside the bar. `actor_scripts/deliv_meas.py` lets each bar's windows run 0.2 s into the next bar, so its "222 -8.0" is bar 223's attack. Inside the bar, 222 reads -9.4.
- "Measured" means read from audio, data or patch files. "Inferred" means a judgement from those numbers.

## Manual notes

MANUAL-READING.md has no row for cycle 23, so I did not read a page range. Below are the pages and patch reads behind my findings, and the MANUAL-GAPS items they touch.

| what the manual or patch says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Brass staccato: "staccato notes with the highest velocity include an attack that includes the rougher sound of overblowing" (p.101). The 1TP KS Master "1Tp Stac rrx1-9" regions have velocity layers 1-54, 55-75, 76-94 and 95-127 (patch read). | Trumpets 1-2 mf off-beats, bars 159-166 (qn 632.9-662.5), "Stac DblTng RRx9" | c21 (velocity 96) played the top layer. c22 (velocity 92) plays the 76-94 layer. The whole c21-to-c22 drop of 6-10 dB is the layer change. Finding 3. |
| Legato Repetitions: "retongued repetitions ... repeated notes within a legato phrase" (p.101). Legato Slur Repetitions: same-pitch notes "played consecutively without space" use a retongued sample (p.106). MANUAL-GAPS #2: LegRep RRx4 is installed in 1FH, 1TB and 1TU and has never been tried. | Chorale same-pitch whole notes, bars 224-234 and 255-262 | Not used. The repeats are Sus MAX notes with a 0.05 qn (27 ms) gap and a CC11 fall. Finding 4. |
| 1FH KS Master: every `MidiController` for CC1 and the Global Group's CC11 has `fadeTime` 120 ms (patch read). | All horn CC dips, including c22's `move_fall` | Confirms the actor's suspicion: a CC11 fall shorter than about 120 ms is smoothed away. Finding 4. |
| Velocity and CC11 both set the harp's level (p.69; c22 ruling 1) | Harp | Yes since c22. Checked under "other checks". |

## 1. The fff arrivals barely rise over the bar before on the mp3. The ride rows at bar 223 cut the arrival 2.5 dB more than its upbeat bar. Ride rows that lower the bars before each arrival give +4.5 / +1.2 / +1.4 dB within the limiter budget (measured, by simulation)

**Where:** delivery `ride_trims` (`build/score_config.py` `RIDE_TRIMS`), bars 221-223 (qn 880-892), 257-263 (1024-1052) and 271-279 (1080-1116).

**Evidence (measured).** Steps are the momentary maximum of the arrival bar minus that of the bar before, with windows inside each bar:

| arrival | mix | mp3 c22 |
|---|---|---|
| 223 over 222 | +5.3 | +1.7 |
| 263 over 262 | +1.3 | +0.5 |
| final over 277 | +3.0 | +0.6 |

- At bar 223 the delivery keeps a third of the mix step. Two things reduce it:
  - The ride row is -3.0 dB on bar 222 and -5.5 dB on bar 223, so the row alone takes 2.5 dB off the step.
  - The 2:1 top ride and the limiter take most of the rest: 4.3 dB of limiting on 223, 1.2 dB on 222.
- At bar 263 the mix step itself is small, because the crescendo has already arrived. Per stem from the last half note before qn 1048 to the first half note after it:
  - Violins I -2.6 dB, Trumpet 1 -0.9 dB, the winds' return -4.8 dB;
  - the brass return only +1.2 dB;
  - only the crash (+28 dB) and Horn 1 (+6.8 dB) step up.
  - A listener gets the arrival from the cymbal and the harmony, not from level (inferred).
- Answer to the coordinator: +0.3 / +0.5 / +0.6 dB (c22's measure) or +1.7 / +0.5 / +0.6 dB (in-bar windows) is not a heard step at 223, which is printed f with a crescendo to fff, plus crash and bass drum. The scherzo's +1.3 LU came from a pre-arrival ride, and the same approach works here (table below).

**Simulated deliveries on the c22 master** (copies of `deliver_master.py`, the loudness loop and the other rows unchanged):

| variant | 223 step | 263 step | final step | limiter final / 223 / 263 | LRA / p10 | other |
|---|---|---|---|---|---|---|
| c22 | +1.7 | +0.5 | +0.6 | 6.0 / 4.3 / 4.7 | 11.9 / -22.6 | 130 > 131 by 1.3 |
| pre-rows equal to the arrival rows (V1) | +3.6 | +0.9 | +1.3 | 6.1 / 4.4 / 4.8 | 11.9 | |
| pre-rows 2.5 dB under the arrival rows (V2) | +6.3 | +1.8 | +2.0 | 6.1 / 4.4 / 4.8 | 11.9 | crescendo 1032 -> 1047 shrinks to +0.5 dB; bar 221 over 222 (inverted) |
| **recommended (V12)** | **+4.5** | **+1.2** | **+1.4** | **6.2 / 4.8 / 4.9** | **11.6 / -22.4** | crescendo 1032 -> 1047 **+2.1** dB (c22 +1.6); 275 -> 277 +3.2; 130 / 131 / 132 -11.1 / -10.9 / -10.0 (now rising) |

The V12 rows. Replace the existing rows with these:
- **Bar 223.** Replace `[[883.5,0],[884,-3],[887.9,-3],[888,-5.5],[891.5,-5.5],[892,0]]` with `[[879.5,0],[880,-4.5],[884,-6.0],[887.9,-6.0],[888,-4.5],[891.5,-4.5],[892,0]]`.
  - The ramp starts at bar 221 (printed mp with a crescendo), so 220 < 221 < 222 < 223 stays in order: -18.9 / -15.8 / -12.0 / -7.4.
  - A flat -6 on bar 222 alone (V7) left bar 221 1.7 dB over 222, a reversed crescendo.
- **Crescendo into 263.** Replace `[[1031.5,0],[1032,-1.5],[1040,-1.0],[1046,-0.5],[1047.8,0]]` with `[[1023.5,0],[1024,-2.5],[1032,-3.5],[1040,-3.0],[1046,-2.5],[1047.8,-2.5],[1047.95,0]]`.
  - It starts at the printed f and crescendo of bar 257, so bars 257-263 rise: -12.8 / -12.5 / -12.2 / -12.2 / -11.5 / -8.9 / -7.7.
  - Starting it at 1032 (V8) put bar 259's ff 2.7 dB under bar 258.
- **Into the final chord.**
  - Replace `[[1079.5,0],[1080,-2.5],[1088,-2.5],[1088.5,0]]` with `[[1079.5,0],[1080,-2.5],[1088,-1.0],[1096,-1.5],[1104,-3.0],[1107.8,-3.5],[1107.95,0]]`.
  - The final row's arrival value stays -4.0.
- **Bar 130.** Add `[[511.5,0],[512,-1.5],[519.5,-1.5],[520,0]]` (bars 129-130). This fixes c22's open item "bar 131 1.3 dB under 130 on the mp3".

**Cost (measured):**
- Bars 273-275 (ff, Largamente, before the printed crescendo at 275) sit 0.4-1.7 dB under bar 272. In c22 they sat 0.7-1.5 dB over it. A stronger pre-ride there (V9, V11) made that sag 2-3 dB, so I kept it small.
- The final and bar 223 now tie at -7.4 LUFS momentary. c22 had the final 0.3 dB over 223.
- The limiter is 0.2 dB over c22 at the final chord.

**Not done here, mix side (inferred):** 263's mix step is +1.3 dB because Violins I and the winds fall at qn 1048. For a bigger 263 step, look at those two stems at the arrival, not at the delivery.

## 2. The second violins' portato quarters in bars 230-233 are 8-11 dB under the violas at the same f. The cause is a chorale-wide -7 dB role row set for the tremolo of bars 223-225 (measured)

**Where:** Violins II, bars 226-233 (qn 900-932). `build/roles.json` "Violins II" `[888.0, 936.0, -7.0]` (plus `[892, 900, -2]`).

**Score:**
- Bars 223-225: Vln II tremolo, fff then mf.
- Bars 226-229: Vln II ff with Vln I on the tune, "unis., change bow at will".
- Bars 230-233: Vln II f, slurred tenuto quarters (portato), the only moving part. Violas, celli and basses hold whole notes and the brass play the chorale (page 13).

**Evidence (measured, K, per bar):**

| bar | 230 | 231 | 232 | 233 |
|---|---|---|---|---|
| Violins II | -42.1 | -44.8 | -44.5 | -46.9 |
| Violas (f, whole notes) | -36.3 | -33.8 | -36.6 | -38.8 |
| Trumpet 1 (f, chorale) | -32.9 | -33.9 | -34.2 | -37.7 |

- The -7 dB row covers the whole chorale, so it also takes 7 dB off the portato line and off the ff tune of 226-229, where Vln II is 7-8 dB under Vln I in unison.
- c19 had the same gap (Vln II -47.4..-50.6 against violas -35.7..-39.0), so the fault is not new.
- This matches Dan's "inner lines hidden behind the melody" (inferred).

**Fix (role level only, edge in a rest):**
- Split the row into `[888.0, 899.9, -7.0]` (the tremolo bars, unchanged) and `[899.9, 936.0, -1.0]`.
- Vln II's tremolo note ends at qn 899.85, and the next note starts at 900.0, so the step falls in the gap.
- Expected (inferred, +6 dB on the stem): the portato line at about -38.5..-41 K, 2-4 dB under the violas' held notes. The ff tune in 226-229 comes about 3-4 dB under Vln I.
- Keep `row_volume_db` Violins II "Tremolo" -4 and `[892, 900, -2]`.

## 3. Trumpets 1-2 off-beats, bars 159-166: the c21-to-c22 drop is a velocity-layer change at 94/95, not a slope. +7 (velocity 95) is the right value (measured)

**Where:** Trumpets 1-2, qn 632.9-662.5. `build/score_config.py` `INSTR_POST["vel_add"]` row `{"from": 632.9, "to": 662.5, ...}` (add 4 now). Row "Stac DblTng RRx9" with the `short_cc_park` CC11 at 100.

**Evidence (measured):**
- The same notes played at velocity 96 in c21 and 92 in c22. Every other value is unchanged; the c21 data is in `cycles/c22/before/parts.json`.
- Note peaks fell 6.0-12.6 dB (median about 7) on all 30 notes. Horn 3, the reference, is identical in both renders.
- In the 1TP KS Master the "1Tp Stac rrx1-9" regions split velocity at 1-54 / 55-75 / 76-94 / 95-127. Velocity 92 plays the 76-94 layer and 96 the 95-127 layer.
- c22's estimate of 0.5 dB per velocity step was wrong: the whole change is the layer switch.

**Value:**
- Base velocity 88 plus 7 is 95, the lowest velocity of the 95-127 layer. c21 measured -2.2 / -3.3 dB under Horn 3 on that layer (target about -3).
- Any add from +4 to +6 (velocity 92-94) stays in the lower layer at about -9 / -11 dB.
- So: `add` 4 -> 7.

**Timbre:**
- The manual says the highest-velocity brass staccatos carry an overblown attack (p.101). I measured the 2-5 kHz share of the first 80 ms: c21 (top layer) is 2.1 / 0.9 dB brighter than c22 (Trumpet 1 / 2), -4.7 / -7.3 dB against -6.8 / -8.2 dB. That is a small difference at velocity 95.
- If the actor rejects the top layer for an mf mark, the instrument-side alternative inside the 76-94 layer is:
  - velocity 94 (add 6);
  - `short_cc_park` cc11 100 -> 127 on these two tracks over 632.9-662.5. That is +4.2 dB; CC11 is volume at 40 log10 on brass.
  - It gives about -4.6 / -7.0 dB under Horn 3 (inferred). A role row of +1 / +3.5 dB over 632-664 (Trumpet 1 / 2) closes the rest.

## 4. Chorale same-pitch repeats: the gap is 27 ms, and the patch smooths CC1 and CC11 over 120 ms, so no CC fall can make the 4 dB dip. Use a real gap with a capped release, or test the LegRep row (measured cause, inferred fix)

**Where:** Horns 1-4, Trombones 1-2, Bass trombone and Tuba, chorale bars 224-234 (qn 892-936) and 255-262 (1016-1048).

**Evidence (measured):**
- The 1FH KS Master's Global Group CC11 controller and every CC1 controller have `fadeTime` 120 ms. This confirms the actor's suspicion.
- The repeats in parts.json:
  - Horn 1 G4: 895.77 + 3.95 ends at 899.72, the repeat starts at 899.77.
  - Trombone 1 C4 at 915.72 / 919.72 / 923.72 / 927.72, each 3.95 qn long.
  - Bass trombone C3 the same.
  - So the gap is 0.05 qn, 27 ms at Maestoso (quarter = 0.536 s). The release fills it.
- The trumpets' repeats got 5.1-6.1 dB dips in c22 from a 0.1 s gap, a 12-unit fall and a 240 ms release cap. That is the nearest working recipe in this score.

**Fix (two options, A first):**
- **A.** Same-pitch joins only, in the chorale spans above:
  - gap 0.10 s (`WIND_REP_RETONGUE_BY` gap for these spans, or a `gap_set` row; 0.19 qn at Maestoso, 0.29 qn at Più allegro);
  - `cap_release` "set" 200 ms on the note before each repeat (the trumpets' tool);
  - the fall of 12-18 units, kept.
  - Keep c19's pitch-changing overlaps (0.04-0.05 s) and the per-track lead stagger, so the master's bar-line holes do not reopen. Check them with c22's 60-500 Hz hole measure: 0.7-3.3 dB now, limit 4.
  - Expected: 4-6 dB per instrument (inferred from the trumpets).
- **B (MANUAL-GAPS #2, p.101).** A range test of "LegRep RRx4" on Horn 1, Trombone 1 and Bass trombone over 915-932 (the four C4 / C3 repeats). Each repeat is its own note ending at the next onset, with no CC fall. The row is installed in 1FH and 1TB and has never been tried.

## 5. Two held inner chord voices are 11-14 dB under their partner at the same printed dynamic: Horn 3 in bars 235-237 and Oboe 1 in bars 143-144 (measured)

**Horn 3, bars 235-237 (qn 935.9-947.8), p chords of Hn 3-4.**
- Measured, K: Horn 3 at -54.2 / -54.5 / -53.5 against Horn 4 at -42.6 / -40.6 / -39.4. The upper voice of the chord is missing.
- Both tracks have identical velocity (53), CC1 (36-45) and CC11 lanes and the same Sus MAX row, so the gap is the samples' level by pitch at the pp layer.
- Over every held note of Horns 1-4 at the same CC1 of 36-37, levels by pitch:
  - G3 -53.2 / -54.1 and A3 -53.2 / -54.1 dB;
  - E3 / F3 -42.2 / -39.1..-40.2 dB (Horn 4's notes here).
  - At CC1 44-45, G3 reads -40.9 / -45.9, so the pp layer is the weak one.
- **Fix.** `cc_scale` over qn 935.5-947.8: Horn 3 +8 dB, Horn 4 -3 dB, k 40. CC11 is volume on brass, so Horn 3's CC11 goes from about 45 to 71.
  - Expected: Horn 3 within 1-3 dB of Horn 4 (inferred).
  - The edges fall in the rest before 935.9 and before the D4 at 947.9, which is already at -43.3.

**Oboe 1, bars 143-144 (qn 568-576).** Oboe 1 F5 and Clarinet 1 D5 hold whole notes, both mf (Ob 1 / Cl 1 unison in 141-142).
- Measured, K: Oboe 1 -50.2 / -50.3 against Clarinet 1 -39.3 / -39.1. In bars 141-142, where they play the same notes, they are within 0-4 dB.
- Contributors (read):
  - the oboes' Sus MAX region gain for F5 (77) is -7.0 dB;
  - track gain is -6.5 dB, the lowest of the winds;
  - CC11 63-67 across the held notes.
- **Fix.** `cc_scale` Oboe 1 +5 dB over qn 567.9-576.0, k 33 (the value c20 used for Bassoon 1). CC11 goes from about 65 to 92.
  - Expected: about 5-6 dB under the clarinet, an audible chord tone (inferred).
  - Do not change the F5 region gain: it evens F5 against C5 / E5 elsewhere (c18 ruling).

## 6. The basses' hammered eighths at 205-210 are still under c19, and one negative role row is left on them (measured)

**Where:** Double basses, qn 816-840. `build/roles.json` "Double basses" `[820.0, 840.0, -4.0]`, plus the delivery row -1.5 at 792-840.

**Evidence (measured, 1/8-qn frame power, p90 / mean):**

| render | p90 | mean |
|---|---|---|
| c19 | -30.5 | -34.5 |
| c21 | -32.5 | -36.5 |
| c22 | -31.9 | -35.7 |

- Celli and timpani are unchanged since c19 (-34.1 / -37.9). So the basses stand 2.2 dB over the celli, against 3.4 dB in c19.
- The note lengths changed in c22 (0.30 -> 0.33 qn). The velocities are the same.

**Fix.** Role `[820.0, 840.0, -4.0]` -> `[820.0, 840.0, -2.5]`, edges in the rests of the eighths' row. It is a passage level, a role row. Expected +1.5 dB, back to c19 (inferred).

This is a stale negative row from c18 ("one row [820, 840, -4] kept"), the kind Movement I c61 found burying lines.

## Other checks (measured unless marked)

**Solos above their accompaniment, K, solo minus the power sum of all other stems while the solo sounds:**
- Trumpet 1 at 51-66: +1.8. Loudest other is Clarinet 2, 6.5 dB under.
- Violins I+II at 67-82: +0.1. Celli counter-melody 4.9 dB under.
- Bassoon 1 at 115: +3.6.
- Muted Trumpet 1 with cor anglais at 171-186: +2.6.
- Theme in the bass at 27-34: 2-5 dB over the violins' countersubject per bar.
- Trumpets' theme B at 211-218: -0.3 against everything else together; loudest other stem 8.3 dB under.
- Chorale 224-225: brass 6-7 dB over the mf string tremolo. 226-228: the ff violin and wind tune at or over the brass f. 255-262 brass +1.8.
- Molto cantabile 235-238: violins 5-9 dB over every other family.
- All in order.

**Harp (coordinator's question):** not too far down.
- Bar 235: 10 dB under the violins' mf tune (K; 8.4 by the actor's measure), 2.4 dB under Clarinet 1's p line, 2.5 dB over the p violas. That is the right place for p arpeggios under an mf tune (inferred).
- At 123-128 the harp's p figure is 3.1 dB under Bassoon 1's p solo at 115 and 3.4 dB under Clarinet 1's dolce p line over it. That is inside B's c22 limit of 5 dB.
- No change.

**Percussion:**
- Crash cymbals in the first half quarter after each arrival sit 9-11 dB under the master (K): heard, not dominant.
- Bass drum and timpani are 15-22 dB under the master at 223 / 278. They do not cover.
- The crash is one stroke at 1108 tied into the final quarter, as printed.
- Timpani stroke medians: pp -42.9, mf -32.4, f -28.2, ff -23.7 dB peak, identical in c19, c21 and c22. The f-to-ff step of 4.5 dB is in order, so Movement I c60's "f/ff strokes 0.4-4.8 dB soft" does not apply here.

**Movement I c60 check:** no loud chord after a quiet bar rises over a climax. With in-bar windows the loudest non-climax bars are 277 (-8.0) and 1 / 5 (-8.6), all under 223 / 263 / final (-7.7..-7.4).

**Stale negative role rows (Movement I c61, scherzo c20):**
- Searched `roles.json`. Two rows bury moving lines: findings 2 and 6.
- Checked against Violins I and kept:
  - Violins II / Violas `[40,104]`, `[792,816]` and Violas `[600,680]`: unison span levels, all or nearly all onsets on Violins I's pitch class.
  - The `[1088,1116]` divisi rows: c16 stem-fix passage roles, on the do-not-touch list.
- Open, not shown to be wrong: Violins II `[600,680,-2.9]` (44 of 105 onsets unison) and Violas `[984,1056,-2.4]` (17 of 64 unison) cover partly independent lines. Measure them before the next cut.

## Do not touch

- The harp velocity path and its gains.
- The 1048 cap ramps and the 1032-1048 hairpin hold.
- The fff caps and steps at 888.
- The chorale's pitch-changing overlaps and per-track lead stagger (c19).
- Violins II "Tremolo" row volume and the tremolo bars' -7 dB (888-899.9).
- The `[1088,1116]` string passage roles.
- The timpani stroke ladder.
- `short_cc_park` on the trumpets.
- The trumpet f / ff 240 ms release.
- The -14 stage with the loudness loop and 2:1 top ride.
- No per-note move in the track volume envelope (Dan).

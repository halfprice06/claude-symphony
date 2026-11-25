# Cycle 22, critic C: dynamics over time (render of cycle 21)

Material: `cycles/c21/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `cycles/c21/mvt3-mockup-c21.mp3`, `cycles/c21/CHANGES.md`, `build/parts.json`, `build/score_config.py`, `build/roles.json`, `build/mix.json`, `build/mockup-events.tsv`, the Dvořák 9/i reference (`symphony/render/assets/refs/`, used only for the loudness distribution). Loudness is BS.1770 via ffmpeg ebur128: M = momentary (400 ms), S = short-term (3 s), both centred, 10 Hz. Stem levels are plain RMS per half or whole quarter note on the parts.json tempo map. "Measured" means a number from these files; "inferred" means reasoning no render has tested. Nobody in the loop can hear, so every audibility statement is inferred.

Delivery simulations: an unmodified run of `tools/deliver_master.py` on the c21 master with the c21 `build/parts.json` reproduces the delivered c21 file (-14.0 LUFS, LRA 12.2, TP -1.1, limiter 5.7 dB). Variants were run on copies of parts.json and mix.json with only `ride_trims` edited. Scratch scripts were deleted.

## Manual notes

MANUAL-READING.md has no row for cycle 22 (the plan ends at c20), so I read no fixed range. I read the pages behind this lens's open problems and checked the MANUAL-GAPS items that touch them.

| Manual (May 2021 HO, PDF page) / gap | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.101, brass "Long" / Sustain | Brass sustains are held "indefinitely" by looping the samples. CC1 sets the dynamics: all 4 layers play and CC1 picks which are heard, "so you can create a realistic crescendo and/or decrescendo during a held note". | The brass crescendo into bar 263 (qn 1040-1048, f/ff to fff) and into the final chord (1096-1108). | No at 1040-1048: CC1 is held flat at 108 from 1040 to the arrival by the c20 cap, and the brass fall 5-6 dB (finding 1). Partly at 1096-1108: CC1 rises 109 -> 120 but starts in the top layer, so it adds little (finding 3). |
| p.104, brass "Crescendos" | Recorded single-note crescendo instruments, Fast / Medium / Slow, "often more realistic than using MIDI volume or expression". | Same two crescendos. MANUAL-GAPS "Considered and ranked low" dismissed them because "the CC1 crossfade already follows printed hairpins". | Not used. The premise no longer holds at 1040-1048 (CC1 capped). A "Cres Med" test on Horns 1-2 / Trombones 1-2 at 1044 is a fallback if finding 1's CC fix is not enough. |
| p.101 (loops) and DIGEST §7 / p.109 (woodwind sustains looped); BRIEF item 7 | Long notes are looped samples; held notes over about 6 s can pulse. | Horn 4's pp A flat 3 held 6.4 s in bars 43-47 (qn 168-186). | No: it dips 6-9 dB twice, about 2.9 s apart, in its band and in the master's (finding 4). |
| MANUAL-GAPS #12, recorded crescendo rolls (p.123, 125) | Felt Cresc rolls end on a stroke. | Timpani crescendos 1040-1048 and 1096-1108. | Not needed now: the CC1 roll rises 89 -> 121 and the stem rises 8 dB (1040 -37.9 -> 1047 -29.7 dB) and 6 dB (1096 -38.4 -> 1104 -30.1). |

## Answers to the coordinator's items (my lens)

- **The fff tie (final -7.6, 223 -7.8, 263 -7.9 M on the mp3).** I do not think this is a failure of the printed shape (measured and read). The score marks all three arrivals fff with the same forces: every wind, brass, timpani and percussion staff at qn 888, 1048 and 1108, approached by a crescendo each time. Nothing in the print ranks the final chord or bar 223 above 263. A real recording clusters its top just as tightly. Short-term loudness from the 95th percentile to the maximum is 1.6 dB on the Dvořák 9/i reference and 1.9 dB on the c21 mp3; max minus the 90th percentile is 2.2 and 2.6 dB. Do not spend more ride or limiter budget separating them. What does fail is the approach to 263 and the final chord: findings 1 and 3.
- **Master clip (+0.6 dBFS, float stem sum peak 1.073).** Nothing audible: `render_cycle.py` replaced the clipped 24-bit file with the float stem sum, and the mp3 is made from that (my re-delivery from it reproduces c21 exactly). For a clean file every cycle, make the replacement in `render_cycle.py` unconditional: always write the float stem sum as `00_Master.wav`, not only when the peak reaches 0.9999. The master has no FX, so the content is identical. If the REAPER-written file itself must not clip, put -2 dB on the REAPER master fader. That gives a peak of about 0.85, and the delivery's constant gain removes the 2 dB, so the mp3 does not change.
- **Loudness range.** Master LRA 22.6 LU and mp3 12.2 LU: on target. The mp3's p10 short-term is -22.6.
- **Movement II c57 (top ride 2:1, a pre-climax bar level with the climax).** It applies in part. The last bar before each arrival on the mp3 is 1.6 dB (222 / 223), 1.7 dB (262 / 263) and 1.1 dB (277 / 278) under its arrival. None is level with it, but at 262 the ride rows that keep it under also flatten the crescendo (finding 1).
- **Scherzo c19 Horn 1 A4 -> G sharp 4 legato hole.** It does not apply: no horn track has an A4 to G sharp 4 legato pair.

## Findings, ranked

### 1. The crescendo into the fff at bar 263 (qn 1032-1048) does not grow; the brass get 5-6 dB softer through it

Measured. In the score, winds and strings have ff at 1032 with a crescendo to fff at 1048 (bars 259-262). The brass and timpani crescendo from 1040.

- **Master (M, every 2 qn from 1032):** -15.4, -15.0, -15.2, -15.3, -15.2, -14.9, -13.0, -13.3, then -10.1 at 1048. That is +0.5 dB over the first 12 of the 16 qn.
- **Brass family:** -20.8 at 1032, -22.7 at 1040, -19.5 at 1046. Horn 1 goes from -30.8 at 1040 to -35.7 at 1047, and Trombone 1 from -26.3 at 1032 to -32.7 at 1045, both inside the printed crescendo.
- **mp3:** M is flat within ±0.6 dB from 1024 to 1047 (six bars), then +1.8 dB at the arrival. Bars 259-262 read -9.4, -9.6, -9.8, -9.6.
- **Causes, from parts.json and score_config.py:**
  - The c20 ruling-2 caps (`score_config.py` c20 block, loop `for _arr, _from, _end in ((888.0, 884.0, 892.0), (1048.0, 1040.0, 1052.5))`) hold every track at the ff resting value from 1040 to the arrival. Violins I CC11 drops 113 -> 105 at 1040, Oboe 1 110 -> 104, Clarinet 1 CC1 117 -> 108. The brass are held flat at CC11 100 and CC1 108. With flat CC1 the horn sustain decays inside each note, and the B3 at 1044 is quieter than the C4 before it.
  - The brass hairpin gain from the 1024-1032 crescendo is released at 1036.75-1038.25 (Horn 1 vol 5.5 -> 3.5 dB, Trombone 1 2.0 -> 0.0 dB) before the next crescendo starts at 1040.
  - Two delivery rows press the last bar: 1043.5-1046.5 at -2 dB and 1045.5-1052 at -1.5 dB.
  - The cap was right at 888, where the crescendo starts at mf and stays under it (Horn 1, Trombone 1 and Trumpet 1 rise from -37..-42 to -26..-32 dB over 884-887). At 1048 the crescendo starts at ff, above the cap.

Fix (instrument side, held levels and delivery rows only):

- **(a) Caps for the 1048 arrival:** in `score_config.py` c20 ruling 2, make the 1048 caps ramps and leave the 888 caps as they are.
  - strings CC11 `[(1040.0, 108), (1047.9, 112)]`, then the arrival steps to 118;
  - woodwinds CC11 `[(1040.0, 107), (1047.9, 110)]`, then 115;
  - brass and clarinets CC11 `[(1040.0, 102), (1047.9, 106)]`, then 112;
  - brass CC1 `[(1040.0, 108), (1047.9, 116)]`, then 120.

  Each line keeps at least 3-6 units of step at the arrival, so ruling 2's step survives. CC1 on the brass is the patch's own crescendo (p.101): about 0.21 dB per unit (B, c20), so +8 units is about +1.7 dB plus brightness.
- **(b) Brass hairpin gain:** hold it from 1032 to 1040 on Horns 1-2, Trumpet 3 and Trombones 1-2, so the 1024-1032 gain is not released before the 1040-1048 crescendo starts. Use a vol_set row `[(1036.0, None), (1036.5, "at:1036.0"), (1040.0, "at:1036.0")]` in the c20 `_vs20` style, or `HP_CHAIN` 8 qn for these tracks. It is a printed-dynamic ramp held at a phrase level, not a per-note move.
- **(c) Delivery rows** (`score_config.py` c21 block, the w11 rides):
  - delete the 1043.5-1046.5 -2 dB row;
  - start the 1045.5 row at the arrival: `[(1047.8, 0), (1047.95, -1.5), (1051.5, -1.5), (1052, 0)]`.

  Simulated on the c21 master (variant v5, together with finding 2's rows): mean M over 1044-1048 -10.1 -> -8.9 dB, bar 263 unchanged at -7.9, limiter on 263 unchanged (2.9 dB rms-window maximum), bar 262 -9.6 -> -8.6 (still 0.7 dB under 263), I -14.0, LRA 12.2.

Targets on the c22 stems and mp3:
- master M rises at least 1 dB per bar over 1032-1046;
- the brass family does not fall anywhere in 1032-1047;
- mp3 1040-1047 at least 1.5 dB over 1032-1039;
- 263 still at least 0.5 dB over bar 262.

### 2. Ride rows invert two printed shapes on the delivered file: the opening ff is no louder than the f arrival of bar 10, and the f arrival at bar 131 is under its own crescendo

Measured (mp3 M per bar; master in brackets):

- **Bars 1 / 5 (ff tutti) against bars 10-11 (mf < f into the theme):**
  - mp3: -9.5 / -9.6 against -9.7 / -10.8, so the ff is 0.2 dB over the crescendo bar;
  - master: -15.7 / -15.8 against -22.0 / -23.8, so 6 dB over.
  - Cause: bars 1-2 and 5-6 carry two rows each (-2.5 and -1.5 dB, rows starting at 0.0 / 15.75 and 0.0 / 15.5), so the opening chords lose 4 dB. Meanwhile the quiet lift for bars 7-8 (mf, master -37 dB) carries about +13 dB into the bar-10 crescendo, against +6.5 dB at bar 1.
- **Bars 130-132 (crescendo mf -> f at qn 520, ff in the harp at 524):**
  - mp3: 130 -10.0, 131 -12.4, 132 -11.2, so the arrival is 2.4 dB under the crescendo;
  - master: -23.4, -21.8, -20.5, a 2.9 dB rise.
  - Cause: the rows 519.75-528.25 (-2 dB) and 523.5-528.5 (-2 dB) start exactly at the arrival.

Fix in the `RIDE_TRIMS` rows (`score_config.py`, the c20 "short ff stabs" block and the c21 additions):

- delete the -1.5 dB rows on bars 1-2 and 5-6 (keep the -2.5 dB rows);
- delete the 519.75-528.25 row (keep 523.5-528.5);
- add `[(31.5, 0.0), (32.0, -2.0), (44.0, -2.0), (48.0, 0.0)]`, which lowers the bar 9-11 crescendo and its arrival evenly and keeps the crescendo's own shape.

Simulated with finding 1's rows and finding 3's final row (v5):
- bars 1 / 5 -8.6 / -8.7, now 2.5 dB over bar 10 (-11.1) and 4.2 dB over bar 11 (-12.8); limiter on bar 1 1.9 dB (rms-window maximum, was 0.9);
- bars 130 / 131 / 132 -10.1 / -10.8 / -9.6, so 132 is over 130. Bar 131 is still 0.7 dB under 130 from the top ride's smoothing; the master rises there;
- unchanged: I -14.0, LRA 12.2, p10 -22.7, TP -1.1, limiter on the final chord 5.6 dB (c21 5.7), every fff within 0.1 dB.

Bar 1 stays 0.7 dB under the fff arrivals.

### 3. The three-bar crescendo into the final fff (qn 1096-1108, bars 275-277) keeps a fifth of its rise on the mp3; the brass are already at the top of their layers and the winds' note shapes fall inside it

Measured.

- **Bar maxima, bars 275 -> 276 -> 277 -> 278:**
  - master: -14.9, -14.3, -11.8, -8.6, so +3.1 dB through the crescendo, then +3.2 at the arrival;
  - mp3: -9.3, -9.0, -8.7, -7.6, so +0.6 dB through the crescendo (19 % kept), then +1.1.
- **Brass family:** +2.4 dB at 1100, then back to +2.4..-0.9 dB around the dotted rhythm. Horn 1 sits at -27..-28 dB from 1097 to 1108.
  - Horn 1 and Tuba CC1 run 109 -> 120. At ff the brass KS Masters already sit in the top layer, so the CC1 crossfade adds little (DIGEST §8: above about 108 CC1 mostly adds brightness).
  - The tracks' hairpin gain is only +2 dB (`hpgain` [1096, 1108, 2.0]).
  - Horn 1's fader also steps 5.25 -> 1.88 dB at 1103.8, between its notes, inside the crescendo.
- **Winds:** the family is flat (-30.0 at 1096, -30.0 at 1106). Oboe 1 CC11 falls 106 -> 102 over 1097-1100.5, inside the printed crescendo: the driving-music phrase shape (start high and fall) is acting inside a hairpin. Research batch 3 says "printed hairpins take over".
- **Delivery:** the final ride row ramps -3.5 dB across bar 277 (`[(1104, 0), (1107.9, -3.5)]`). Measured effect: +0.3 dB at bar 277 when the row is reshaped, because most of the flattening is the top ride and the limiter (bar 278 limiter 4.6-4.7 dB rms-window maximum).

Fix:
- **(a)** Brass hairpin gain over 1096-1108: 2 -> 4 dB (Horns 1-4, Trumpets 1-3, Trombones, Tuba). Woodwinds 3-4 -> 5 dB. These are printed hairpins as dB ramps.
- **(b)** Remove Horn 1's step at 1103.8: hold the role level through to 1108.
- **(c)** In `tools/score_to_parts.py` PHRASE_SHAPE, skip the falling shape on any note whose onset lies inside a printed crescendo hairpin. This is a generic rule. Measure Oboe 1 at 1097-1101 and Clarinet 1 at 1096-1103 afterwards.
- **(d)** Final ride row `[(1087, 0), (1104, 0), (1107.8, -1.0), (1107.95, -3.5), (1113, -3.5), (1113.5, 0)]`: the step lands at the downbeat. Simulated in v5: limiter on the chord unchanged, bar 277 -8.7 -> -8.4.

Target: on the master, bar 277 at least 4 dB over bar 275 (now 3.1), and bar 278 still at least 2.5 dB over bar 277. On the mp3, bar 277 at least 1.2 dB over bar 275 (now 0.6).

If (a)-(c) leave the brass flat, the fallback is the p.104 crescendo row ("Cres Med") on Horns 1-2 at 1096. That costs one row per track and a rebuild (memory: 45 GB settled).

### 4. Horn 4's pp held A flat 3 in the transition (bars 43-47, qn 168-186) pulses 6-9 dB, and the master follows it

Measured. The note is on "Sus MAX", velocity 41, 6.4 s long, with CC11 37, CC1 28 and the fader flat until the fade at 5.8 s. Stem level in 0.25 s windows, from the note-on:

- -52.7 at 0.5 s, -57.0 at 1.75 s, -51.5 at 2.5 s, -59.6 at 4.75 s, -53.4 at 5.25 s;
- two dips of 4.5 and 7.6 dB, 2.9-3.0 s apart, with no controller moving.

In the 190-230 Hz band the master dips with it: -6.9 / -7.8 dB at the same windows, against -6.3 / -8.9 on the stem. The horn is the only voice there in a pp passage (master about -40 dB M). It is a looped brass sustain (p.101), and a 7-8 dB dip twice in 6 s is heard as a wobble in the soft pedal (inferred).

Fix: the standing rule forbids the old `loop_fills.json` fader bumps, so put the fill in CC11, which is volume on the horn KS Master (k = 40 dB per decade, c20 block). Add a `cc_scale` entry for Horn 4 in score_config.py:

`{"lane": "cc11", "k": 40.0, "pts": [(171.4, 0), (172.5, 3.0), (173.1, 4.5), (173.8, 3.0), (174.6, 0), (179.8, 0), (180.8, 5.0), (181.5, 7.0), (182.1, 5.0), (182.9, 0)]}`

That moves CC11 37 -> about 55 at the deeper dip. Positions come from the c21 stem (dip centres 1.85 s and 4.85 s after qn 167.9). Refit them on the c22 stem, because a different round robin moves them.

Target: the stem's band level within ±2.5 dB over 0.5-5.5 s of the note.

The same scan found no other wind or brass note over 2.8 s with a ripple over 6 dB that is not explained by printed hairpins, except Contrabassoon 568 (6.8 dB, CC moving) and the flutes at 156 (decrescendo). Those need no action now.

## Checked and working (measured)

- **Hairpins:** 624 hairpins of 2 qn or longer measured on their own stems. Crescendos rise a median 6.6 dB, diminuendos fall a median 4.4 dB. The outliers that are real faults are in findings 1 and 3. Most others are fp / sfp fronts or entries inside the hairpin.
- **sfp of bar 149 (qn 592):**
  - master M 14.0 dB at the front, falling to 21.6 at 593.5 (7.6 dB in a 400 ms window), back to -12.3 by 596.5;
  - mp3 6.8 dB.
- **Sudden drops:**
  - sub. p at 872: master 218 -> 219 3.4 dB, from mf/mp to p;
  - the bar-223 fff -> bar-224 f: 8 dB M on the master, 3.7 dB on the mp3, with the crash ringing under it.
- **The p-pp transition into the second theme:** mp3 bars 40-50 fall from -13.1 to -24.0 M, and bar 51 rises to -20.4 for the trumpet's p solo.
- **Timpani crescendo rolls into 263 and the final chord:** they rise 8 and 6 dB (see the manual table).
- **The final chord's ring:** from the written end (1113.0) the master falls 10 dB in about 0.17 s and 20 dB in 0.38 s. The late slope is about 50 dB/s, so -60 dB comes 0.9 s after the end. This is inside the wetness ceiling and the c08 target (-20 dB in 0.40-0.50 s, slightly fast). The mp3 ends 2.9 s after qn 1112.

Do not touch: the 888 caps and steps (the crescendo into 223 rises 11-16 dB on Horn 1, Trombone 1 and Trumpet 1 and steps 3-8 dB at the arrival); the sfp front of bar 149; the timpani CC1 roll crescendos; the delivery stage (-14 LUFS, 2:1 top ride, loudness loop, ratio 1.8), the 223 rows (-3 / -5.5) and the final chord's -3.5 dB level; FINAL_RING; the subito rows in CC11.

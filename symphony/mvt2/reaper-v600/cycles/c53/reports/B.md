# Cycle 53, critic B: balance and levels (render under review: c52)

## Method

- Stems 01-32, the four return stems and the master of `cycles/c52/render` (these carry the post-render stem fix), the unfixed string stems of `cycles/c52/render_first`, and the data of `cycles/c52/rendered_build` (it exists). c51 and c50 from their own `render` and `rendered_build`, each on its own time map.
- K-weighted and A-weighted power per 10 ms frame (4096-point FFT), the scripts of the c50-c52 B reports, so the numbers compare directly. Note body = mean over 20-80 % of the played note. Fine curves are unweighted stem RMS in 30 ms steps. The master equals the sum of the 36 stems (residual -164 dB), so every master figure below can be traced to a stem.
- New this cycle: a scan of every string legato join (503 joins) for the level peak of the transition against the bodies of the two notes around it, with the same peak read on the master; the applied stem-fix gain read as delivered stem minus `render_first`; each `JOIN_NOTCH` window compared with the peak it was written for.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 53 (the schedule ends at c47), so no page range was read.

| Source | Where it applies | Does the render follow it |
|---|---|---|
| May 2021 HO manual p.79 and p.86 (Leg Bow Change against slur legato; the bow change row is described as one that will "accent the second note") | the 116 notes that left Leg BC MAX in c52 | The accent is gone as expected: at the tenuto half notes of bars 61-62 the attack peak over the body fell (Violins II 204 +8.4 -> +4.2 dB, 208 +7.9 -> +2.9, Violoncellos 210 +5.9 -> +1.5) and the dip at each bow change stayed (median 2.0 -> 2.5 dB over 22 joins). The bow changes are still marked; see "Slot questions" |
| `mockup-kit/LEARNINGS.md` section 5 (about one string legato join in ten has a transition peak 5-12 dB over both bodies; notch of peak minus 2 dB; a peak can move 0.1 s) | all string lines | Count unchanged by the row change (52 of 503 joins at 6 dB or more; c51 55 of 494), but several notches no longer sit on their peak (finding 1) |
| `MANUAL-GAPS.md` 8 (half-section patches for "4 soli") | basses bars 65-70, Violoncellos div bars 83-86 | In use. The pedals move by 3 dB inside one bow without any re-bow (finding 5) |
| `EW-TEMPLATE-PLAN.md` section 8 (phrase arch, long notes keep moving) | Horn 1 bars 57-59 | The printed crescendo is there on average, but note to note the line goes up and down by 5-8 dB (finding 3) |

## Slot questions from the loop lead

- **Bars 60-62 and 78-81, level.** Restored. Of the 43 notes there that changed row, 38 are within 1 dB of their c51 body and all are within 2.0 dB. Remaining: Violins II 204 -2.0, 208 -1.9, 210 -1.4 (no row was written for them), Violoncellos 256 -2.0 and 269 -2.0, Violins I 262 -1.3. Whole movement: 1298 of 1349 notes within 1 dB of c51, 1339 within 2 dB, median 0.0 (measured).
- **Bars 60-62 and 78-81, tone.** No change. Level in 1.8-6.5 kHz minus level in 150-1300 Hz over each note body, c52 minus c51: median +0.06 dB over the 112 moved notes (10th to 90th percentile -1.7 to +1.9), -0.05 dB over the 64 loud ones, and no relation to the size of the level row (correlation 0.05). The softer playing of Leg Slur MAX is a level difference, not a darker layer, so a gain row is the right repair (measured).
- **The stem-fix gain itself.** Smooth. Read as delivered stem minus `render_first`, the gain moves from one note's value to the next without returning to 0 between rows (celli 259-265: +2.4, +4.8, +4.3, +5.0, +2.4, +4.7 dB with 60-80 ms ramps). The string return was not raised with the dry stems: R Strings against the dry strings is 1.0-2.1 dB lower than in c51 in bars 60-62 and 79-80. The return is 24-28 dB under the dry strings, so the master does not change; the next real render will bring it back (measured).
- **The 11 long notes with a stronger start.** On the delivered stems five of them are real and are transition peaks before the beat, not strong starts of the body: Violoncellos 81, 186, 188, 193 and Violas div 87. Three of the five were made larger by the stem-fix row, which begins at the note-on and so lifts the transition as well as the body. Violoncellos 253, 202, 261, 182 and Violins I 87 and 80 read within 1 dB of c51 (start minus body) or better. All in finding 1.
- **Violins II 197.5.** Finding 2.
- **Re-bow dips at the cap.** Finding 5: leave them.
- **Printed bow changes.** By level, none is lost in the two loud passages (table row above). I did not check the soft ones.

Solo margins, K (c51 in brackets): Horn 1 bars 7-14 +7.5 (+7.5); Oboe 1 15-16 +3.1 (+3.0); Violin I solo 17-18 +7.1 (+7.1); bass clarinet 31-36 +5.3; Flute 1 37-40 +4.3 (+4.3); cor anglais 41-44 +1.9 (+1.9) and 47-50 +2.5 (+2.5); Trombone 1 63-64 +6.4 (+6.2); Clarinet 1 85-89 +1.4 K / +4.7 A (+1.6 / +4.7). Climaxes: bar 61 strings -16.7, brass -17.9, woodwinds -19.8, timpani -32.0; bar 79 strings -22.6, woodwinds -22.2, brass -27.2, timpani -37.7. Strings 0.3-0.5 dB under c51, everything else equal. Dynamic mapping (A-weighted medians of note bodies): pp woodwinds -54.7, horns -54.5, strings -54.4, divisi and solo -54.4; p -49.5 / -48.8 / -47.9 / -45.4; mf -42.5 / -38.5 / -39.4 / -41.0; f woodwinds -39.0, horns -34.3, strings -36.5. Within 1 dB of c51.

## Findings

### 1. String transition peaks stand 6-15 dB over both notes at about ten joins and are heard in the master; three were enlarged by the c52 level rows and five notches no longer sit on their peak

Where: Violoncellos 68.5 (bar 23, the first note pair of the counter-melody), 240.5 (bar 71, the same figure), 249, 81, 174, 193; Violins II 190 and 266; Violins I 186 and 86.5; Violas 256; Violas div 71 and 87.

What is wrong: at these joins the legato transition is a burst 100-250 ms before the beat. Peak over the higher of the two note bodies, with the same moment on the master against the master 0.15-0.45 s either side (c51 in brackets):

| Join | Stem peak | Master | Envelope at the peak |
|---|---|---|---|
| Violoncellos 68.5 | -25.6 dB, +14.8 over -40.4 / -44.6 (+10.9) | +8.3 (+5.5) | fill at +4.5 to +5.0 dB; the -8 dB notch starts after it |
| Violoncellos 240.5 | +8.4 (+6.2) | +5.2 (+3.4) | notch covers the second half only |
| Violoncellos 249 | +8.1 (+3.9) | +4.6 (+2.6) | none |
| Violins I 86.5 | +7.8 (+5.5) | +4.3 (+4.0) | notch 0.11 qn late |
| Violoncellos 81 | +6.7 (+0.2) | +4.2 (+2.5) | c52 row: -4.0 -> +7.2 dB at -120 ms |
| Violins II 190 | +7.3 (+0.7) | +3.7 (-0.1) | rises +5.6 -> +10.0 dB at -215 ms |
| Violins I 186 | +7.1 (+6.6) | +5.1 (+5.6) | none |
| Violoncellos 174 | +8.9 (+8.9) | +3.2 (+3.8) | none |
| Violoncellos 193 | +5.5, 9.7 over the body from 0.3 s | +2.0 | c52 row: 0 -> +4.7 dB at -135 ms |
| Violas 256 | +7.5 (+4.3) | +2.2 (+0.2) | none |
| Violins II 266 | +8.0 (+7.3) | +2.4 (+0.9) | none |
| Violas div 71 / 87 | +10.3 (+4.4) / +5.9 | under 1 | none (soft, pp) |

The worst is the celli at 68.5. Stem in 30 ms steps from 450 ms before the beat: -40, -40, -39, -38, -36, -33, -30, -27, -26, -26, -31, -37, -41, -44, -48, -52, -46, -44. That is a 14 dB burst and then a hole 8 dB under the next note, at p, under the muted violins' theme. The master goes -34, -33, -31, -30, -27, -25, -25, -27, -32. In c47-c50 the same peak read -31 dB and the master +5 to +6.

Cause (measured for 68.5, inferred for the group): `JOIN_NOTCH` windows are written in absolute score qn. The c51 tempo map and the c51-c52 lead refits moved the note-ons, and the windows stayed. At Violoncellos 68.5 the note-on moved 60 ms earlier (lead 0.22 -> 0.28 s); the peak is still 107-117 ms after the note-on; the window was +63..+208 ms after the note-on in c50 and is +130..+268 ms now. So the notch gives -3.9 dB at the peak instead of -8 and its full depth falls in the hole after it, while the early fill of +5 dB before it now lies on the peak. The same check on the 22 negative windows of Violins I, Violins II and Violoncellos finds the peak outside the window at Violins II 177.35 (peak at +101 ms, window +154..+324), 245.39, 242.99, 270.41, 82.84 and Violins I 86.38.

The count of spiking joins did not rise with the row change (6 dB or more: 55 -> 52; 8 dB or more: 22 -> 25; with a master bump of 2 dB or more: 26 -> 27), so one row per line is not the cause. The c52 additions are the three rows that step up at the note-on.

Fix:
(a) `tools/score_to_parts.py`: add `JOIN_NOTCH_S = {track: {score onset: (from s, to s, dB)}}`, seconds relative to the target's moved note-on (`n["qn"]`), converted like `LEVEL_SHAPES_S`. Windows then follow every later lead change. Convert the existing `JOIN_NOTCH` rows with the offsets they had on the render they were fitted on.
(b) `build/score_config.py`, values fitted on the c52 stems (peak minus 2 dB over the span where the stem is more than 2 dB over both bodies; qn on the c52 map, seconds from the note-on in brackets):
- Violoncellos: replace (68.37, 68.49, -8.0) by (68.15, 68.40, -10.0) [-0.12..+0.16 s] and end the early fill of 68 (`early_fills.json` "68": 4) at the note-on of 68.5 (qn 68.257), because 10 dB alone leaves +7; replace (240.37, 240.45, -5.0) by (240.25, 240.40, -6.4) [-0.06..+0.11]; add (248.83, 248.98, -6.1) [-0.01..+0.16], (173.81, 174.04, -6.9) [+0.03..+0.26].
- Violins I: replace (86.38, 86.51, -5.5) by (86.27, 86.39, -5.8) [-0.06..+0.08]; add (185.72, 185.96, -5.1) [-0.05..+0.19].
- Violins II: add (265.79, 265.91, -6.0) [0..+0.16]; move (177.35, 177.52, -4.3) 0.09 qn earlier.
- Violas: add (255.88, 256.01, -5.5) [+0.05..+0.20]. Violas div: add (70.89, 71.04, -8.3) [+0.08..+0.25] and (87.03, 87.10, -3.9) [+0.18..+0.26].
(c) `build/level_fits.json`, the c52 rows: start each row after the transition instead of at the note-on. Change the first two points from `[on, 0], [on + 0.06, g]` to `[score onset + 0.02, 0], [score onset + 0.14, g]` in `rowlevel52.py` for every row of +2 dB or more; that alone removes the added part at Violoncellos 81 (then add (80.87, 81.00, -2.0)), 193 and 188. Violins II 190: the rise from +5.6 to +10.0 dB is older than c52; delay it by 0.2 s or add (189.69, 189.88, -5.3).

Simulated on the c52 stems and master with the windows of (b) only: stem peaks left at +2.0 to +4.4 dB (68.5 at +7.1 before the fill is shortened); master bumps 68.5 +8.3 -> +4.8, 240.5 +5.2 -> +1.9, 249 +4.6 -> +1.1, 81 +4.2 -> +0.6, Violins II 190 +3.7 -> +0.5, 174 +3.2 -> -0.2, 256 +2.2 -> -0.1, 186 +5.1 -> +3.1, 86.5 +4.3 -> +2.6. All of this is level-only and can go in by `stem_fix.py`.

Acceptance: no string join with a 30 ms stem peak more than 5 dB over both bodies and a master bump over 2.5 dB; Violoncellos 68.5 stem peak not over -34 dB.

Judgement: levels, window positions and the simulation measured; that the windows went stale through the lead changes is measured at 68.5 and inferred for the others.

### 2. Violins II sit 2-4 dB lower than in c51 against Violins I at 197.5-198.25 and in bars 61-62

Where: Violins II, F5 at 197.5 and the first quarter beat of D flat 5 at 198 (bar 59, the theme in octaves, f); A flat 4 at 204, F5 at 208, E5 at 210 (bars 61-62, ff tenuto).

Evidence (measured, K per quarter beat): bar 59 before the note, Violins I over Violins II by 2.8-3.5 dB (196.25-197.25). At 197.5 / 197.75 / 198.0: Violins II -32.7 / -31.2 / -31.9, Violins I -27.4 / -27.6 / -26.2, so 5.3 / 3.6 / 5.7 dB apart. In c50 the first two read 0.7 and 2.6; 198.0 has read -31.9 in every cycle. Velocity, CC11 and envelope are the same as in c50; the note is 0.47 s long and its legato transition takes most of it. Bars 61-62: Violins I over Violins II 3.8 -> 5.0 dB and 4.8 -> 6.2 dB (c51 -> c52), because 204, 208 and 210 play 2.0, 1.9 and 1.4 dB softer on Leg Slur MAX and got no row (the actor's unweighted measure put them under its 1 dB threshold; 206 got +1.1).

Fix (`build/level_fits.json`, "Violins II", seconds from the score onset, same form as the c52 rows):
- "197.500": [[-0.25, 0], [-0.19, 3.5], [0.46, 3.5], [0.52, 3.0], [0.70, 3.0], [0.80, 0]] (covers the first quarter beat of 198 as well; predicted 197.5 -29.2, 197.75 -27.7, 198.0 -28.9, that is 2.2 / 0.1 / 2.7 dB under Violins I).
- "204.000" +2.0, "208.000" +1.9, "210.000" +1.4, each from the score onset + 0.02 s (ramp to + 0.14 s) to the note end, per finding 1(c).

Judgement: measured; the predictions assume the envelope is linear in dB.

### 3. Horn 1's counter-melody in bars 57-59 rises and falls by 5-8 dB from note to note under one printed crescendo

Where: Horn 1, qn 188-202 (mp at 188, crescendo under one slur to the f at 196, crescendo again from 200 to the ff at 204).

Evidence (measured, K note bodies): 188 A flat 4 -36.8; 190 F sharp 4 -31.7; 192 F4 -36.0; 193 E flat 4 -29.8; 195.5 F4 -36.4; 196 F sharp 4 -27.2; 198 E flat 4 -31.6; 199 E4 -26.4; 200 E flat 4 -29.2; 201 F4 -28.9; 202 F sharp 4 -23.8. Against the mean of its two neighbours: 192 -5.2, 195.5 -7.9, 198 -4.8, 190 +4.6, 193 +6.4, 196 +6.8. The F4 pitch trim (`pitch_trims.json` Horn 1 "65": early +1, body -5) was set on soft notes: F4 reads +0.6 against its neighbours at p (qn 32), -5.2 at mf (192, CC11 75) and -2.4 at f (201). 198 moved -1.6 dB between c51 and c52 on unchanged data (it also drifted in c48), and its trim is +1.5.

Fix (`build/note_trims.json`, "Horn 1"; or add 192 and 195.5 to the F4 trim's `_skip_onsets` and trim from there): 192 +3.5; 195.5 +4.0; 190 -2.0; 198 +1.5 -> +3.0. Predicted line: -36.8, -33.7, -32.5, -29.8, -32.4, -27.2, -30.1, -26.4, -29.2, -28.9, -23.8. The eighth at 195.5 stays 5 dB under the note after the breath, as a phrase end.

Side effect on the open breath at 196 (C1 of c52): the gap is 184 ms and the stem floor in it is -42 dB, 5 dB under the pickup and 13 dB under the note after it. With the pickup at -32.4 the dip against it becomes about 9.5 dB (10 wanted) without touching the gap. Do not deepen the gap further: the floor is the horn's release and Opus's hall, and a faster volume fall would cut that ring (S3).

Judgement: levels measured; the dynamic dependence of the F4 trim rests on four notes; the breath prediction inferred.

### 4. One envelope point on Violoncellos div at qn 284.021 is 5.4 dB over its neighbours

Where: Violoncellos div, A flat 2 pedal, 120 ms before the re-bow at 284.141 (bar 86, ppp).

Evidence (measured): `vol_db` reads -0.6 dB at 284.00, **+4.8** at 284.021, -2.0 at 284.04 (40 ms and 18 ms apart). The stem reads -51.1, **-48.4**, -52.5 in 30 ms steps there, in c51 and in c52. A scan of all 32 tracks for a single point 3 dB or more over both neighbours within 80 ms finds this one and the timpani stroke at 262 (+3.3, a stroke trim, intended).

Fix: find which two envelope parts meet at 284.021 in `score_to_parts.py` (the end of the fill of 281.716 and the start of the residual correction of 284.141, both in `rebow_fills.json`), and make the first end at the value the second starts with. Level-only.

Judgement: measured; the two sources inferred from the c52 CHANGES list.

### 5. Re-bow dips at the cap (Double basses 225.215, Violoncellos div 284.141): stop raising the fills

Evidence (measured): Double basses 225.215: the 50 ms minimum is -53.1 dB at +20 ms, 4.0 dB under the 0.35 s before the re-bow (-49.2) but 2.4 dB under the 0.4 s after it (-50.7). The level before is a rise inside the old bow (-48.3 at -0.3 s), not the pedal's level. Over the six pieces of this pedal, more than 0.6 s away from any re-bow, the 100 ms level runs from -54.1 to -48.5 dB (5th-95th percentile -52.6 to -49.6); in the first 0.45 s after the re-bows it runs from -53.2 to -49.5. The re-bows are inside the movement the pedal has anyway. Violoncellos div 284.141: minimum -54.3 at +370 ms, 3.4 dB under the level before, 1.7 under the level after; inside its pieces the pedal runs from -53.4 to -50.3 (5th-95th). At these pitches a 30-50 ms window holds 2-4 periods, so single readings scatter by about 1 dB.

Fix: none to the fills. Change the acceptance in `rebow52.py` / `fit_rebows.py` to the lowest 50 ms within 0.4 s after a re-bow against the mean of 0.5-0.9 s after it, limit 3 dB, and report the 5th-95th percentile spread inside the pieces beside it. By that measure 225.215 reads 2.4 and 284.141 reads 1.7.

Judgement: measured.

## Checked, no change proposed

- Bars 61-62 tenuto half notes on one row: the bow changes dip 2.5 dB (median of 22 joins; Violins II 204 / 208 / 210 4.1 / 4.2 / 3.6, Violoncellos 210 6.2), without the Leg BC attack bump. For "molto sostenuto" that is in order (inferred). If a clearer new bow is wanted at 204 and 208 (printed down-bows), a 1.5-2 dB swell in the volume envelope over the first 0.25 s of the note is the cheap test. The manual's Leg Bow Change Smooth (p.79, p.87) is not a row of the 1st Violins or Celli KS Master (`ks_maps.json`); it would need its own patch and instance, which the memory rule does not allow without removing another.
- Horn 2 208 (`REP_GAP_AT`, not measured by the actor): the stem falls from -26 to -36 dB at 0 to +60 ms after the beat and is back within 3 dB at +200 ms; the dip is 10 dB (c51 4 dB). The low point lies on the beat, so the new note is heard late; for critic A. The master does not move (-14 to -15 dB).
- Violas 81 (`REP_GAP_AT`): the 90 ms gap gives a stem dip of 2-3 dB (-39 -> -42 -> -40). Weak as a repeat; for critic A.
- Bass register, timpani and low brass at both climaxes, the wind solos, Clarinet 1 in the coda: equal to c51 within 0.2 dB (figures above).
- Violas 256 and 257.5 read +6.4 and +3.3 dB over c51 as note bodies; this is the transition peak of finding 1 inside a 0.45-qn note, not a body level.

## Do not touch

Everything on the c50-c52 B lists; one legato row per string line and `KS_ROWCHANGE_LEAD_S` 0.15 (the join peaks are not a reason to go back to Leg BC MAX: their count did not rise); the 66 c52 level rows' body values (only their start, finding 1c); the tone of bars 60-62 and 78-81 (unchanged, no EQ or CC11 change needed); the re-bow fills at Double basses 221.8-235.659 and Violoncellos div 275.527-284.141 (finding 5); the breath gaps at 196 and 204; the C1 shapes at Horn 1 196-204; the bass clarinet shape at 108 and the Flute 1 rows at 108 / 111; hall, sends and `deliver` settings.

Scratch folder: `/private/tmp/claude-501/mockup-loop/mvt2-c53-B/` (185 MB: frame-level caches of the c52 stems, no audio; `lib.py`, `d1.py` / `e1.py` note-by-note c51 against c52 with spectral tilt, `g2.py` stem-fix gain, `s1.py` start against body, `j1.py`-`j7.py` join peaks, notch windows and the simulation, `cfg.py` reads `JOIN_NOTCH` from a `score_config.py`, `v1.py` violins at 197.5, `r3.py`-`r6.py` re-bows and pedals, `h1.py` Horn 1 196 / Horn 2 208 / Violas 81, `g3.py` envelope spikes, `k1.py` bow changes and violin balance). Left in place, as the loop lead's notes ask.

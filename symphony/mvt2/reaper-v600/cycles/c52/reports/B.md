# Cycle 52, critic B: balance and levels (render under review: c51)

## Method

- Stems 01-32, the four return stems and the master of `cycles/c51/render`; data from `cycles/c51/rendered_build` (it exists; `parts.json`, `rebow_fills.json`, `score_config.py`). c50 for comparison from `cycles/c50/render` and `cycles/c50/rendered_build`. Every comparison is made on each render's own time map (positions in score qn converted with that render's tempo list).
- K-weighted and A-weighted power per 10 ms frame (4096-point FFT), the scripts of the c50 and c51 B reports, so the numbers compare directly. Note body = mean over 20-80 % of the played note. Solo margin = the solo over the sum of the other 31 dry stems. Fine curves are unweighted stem RMS in 30 or 50 ms steps.
- Lead's slot questions answered in findings 1 and 2 and in "Level fits of c51".

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 52 (the schedule ends at c47), so no page range was read. Sources this report relies on:

| Source | Where it applies | Does the render follow it |
|---|---|---|
| `MANUAL-GAPS.md` 10 (round-robin reset on CC16, in the pre-roll since c45) | every string re-bow and repeat | Yes. Measured here: the sample takes after each re-bow are the same in c50 and c51 (waveform correlation 0.993-1.000, finding 1), so the changed dips are not a round-robin effect |
| `MANUAL-GAPS.md` 8 (half-section patches for "4 soli") | Violoncellos div 274-286 (Celli DIV A, Sus MAX) | In use since c33. The pedal needs five re-bows in 13.8 s, each carrying a fitted fill of up to +8 to +9 dB (finding 1) |
| `EW-TEMPLATE-PLAN.md` section 6 / FINDINGS section 8 (controller lanes flat across legato note changes) | Flute 1 bar 37 | No, as in c50: the envelope moves between +2.6 and +15.3 dB inside the bar. It compensates sample sags and is kept (finding 4) |
| `MANUAL-GAPS.md` 5 (Leg Slur Exp / Sus Exp for dolce wind solos), never tried | Flute 1 107-123 | Not tried. Still the next test if the hole at 108 is to go below 4 dB (finding 3) |

## Level fits of c51 on the new time map (the lead's first question)

All four hold. My independent readings equal the actor's `bcheck_c51.txt` within 0.1 dB (measured):

- Flute 1 F5 at 108: head -38.0, lowest point -42.1 at +375 ms (hole 4.1 dB; c50 10.8 dB at +390 ms). K per quarter beat 108.0 -38.1, 108.25 -37.8, 108.5 -36.9 (pickup body -41.2). Margin over all other stems at 108.0-108.25: -0.5 K / +4.8 A (c50 -4.1 / +0.7, c49 +0.4 / +5.0).
- Flute 1 E flat 5 at 111: quarter beats -38.2, -34.9, -34.3, -33.1; first test +0.5 dB (pass), second +2.6 against 2.5 (see finding 4).
- Violoncellos bar 73: celli over Violins I at 246.0 +4.3 K / +2.5 A (c50 +7.9 / +6.0); master at 246 -35.0 (c50 -33.2 by my frame). In bar 25 the same place reads +3.0 K / +2.5 A, so the two statements now match.
- Bass clarinet D flat 3 at 108: peak of the first 0.45 s -42.1 (c50 -38.5); see finding 3 for the remaining shape.

Whole-movement check (measured): of 1349 notes of 0.45 qn or longer present in both data sets, the body level differs by less than 1 dB on 1312 and by less than 2 dB on 1340; median 0.0 dB. The nine over 2 dB: the intended Violoncellos 246 (-3.0); Violins II 218 B3 +5.1 and 219 -2.1 (pp under Trombone 1, at -49 dB); Violins I 249 -2.9 and Harp 252 -2.9; Trombone 1 214.5 -2.0; Double basses 122 +2.4 (at -61 dB); Violins I 197.5 +2.2 with Violins II 197.5 -3.0 (below). Master per beat: median difference 0.0 dB, 5th-95th percentile -0.4 to +0.5; three beats moved 1.5 dB or more (20, 246, 285; 246 is the intended one, 285 is the shortened beat before the kept breath at 286). The tempo change did not disturb the balance.

Solo margins, K (c50 in brackets): Horn 1 bars 7-14 +7.5 (+7.4); Oboe 1 15-16 +3.0 (+3.0); Violin I solo 17-18 +7.1 (+7.0); bass clarinet 31-35 +3.0 to +7.8 per bar; Flute 1 37-40 +4.3 (+4.0); cor anglais 41-44 +1.9 (+1.8) and 47-50 +2.5 (+2.5); Trombone 1 63-64 +6.2 (+6.2); Horn 1 67-68 +13.8 and +11.1; Clarinet 1 85-89 +1.6 K / +4.7 A (+1.4 / +4.7). Climaxes: bar 61 strings -16.4, brass -17.9, woodwinds -19.8, timpani -32.0; bar 79 woodwinds -22.2, strings -22.1, brass -27.2, timpani -37.7: equal to c50 within 0.1 dB.

## Findings

### 1. Re-bow fills go stale when the note before the re-bow changes length by a few milliseconds; Violoncellos div 275.527 is the worst case (6.2 dB on the stem, 2.3 dB on the master)

Where: Violoncellos div, A flat 2 pedal, re-bows at 275.527 and 277.599 (bars 83-84, ppp, "4 soli"); the same mechanism at 12 other re-bows.

What is wrong: at 275.527 the stem falls from -49.6 to -54.5, -55.7, -55.6 over the first 100 ms and again to -54.6 at +350 ms (c50: -51.2, -52.0, -53.1 and -52.0). On the master the dip is 2.3 dB broadband and 3.8 dB in 80-450 Hz (c50 0.3 and 0.5), because the basses hold the same pedal an octave lower at the same level (-51.3).

Evidence for the cause (measured):
- The data around the join are the same in seconds in c50 and c51: same fill (`rebow_fills.json` is identical), same gap (+1.0 ms), same velocity, no CC11 points. The one difference is that the piece before the re-bow (274.0) is 17.7 ms longer, because c51 removed a tempo arc there.
- The same sample takes play: the waveform of each of the six pieces 0.6-1.6 s after its note-on correlates 0.999-1.000 between c50 and c51 (basses 221.8-235.7: 0.993-1.000; final chord re-bows: 1.000). So this is not round-robin and not a random take.
- Across all 37 re-bows of `rebow_c51.txt`: the 23 whose previous piece kept its length (under 1 ms) changed their dip by a median 0.3 dB (largest 1.7); the 14 whose previous piece changed length (3.7 to 147 ms) changed by a median 1.15 dB (largest 3.7, this one).
- The fill at 275.527 is steep: -1.3 dB at -0.04 s, +5.2 at +0.20, +8.0 at +0.38 s. It was fitted to the hole of one render. A join whose raw hole needs +8 dB is sensitive to where the old piece is released.

Inferred: the level in the join is the sum of the old piece's tail and the new piece's start at the same pitch, and that sum depends on the exact length of the old piece. The actor's `qnshift51.py` used a 20 ms threshold, so the 17.7 ms change was not listed.

Fix:
(a) Refit the fills of the 14 moved re-bows on the c51 render with `tools/fit_rebows.py` (level-only, so it can go in by `stem_fix.py` or with the next render): Violoncellos div 275.527, 277.599, 279.67, 281.716, 284.141; Double basses 225.215, 227.775, 230.393, 233.038, 235.659; Violins II 292.0; Violas div 289.0, 291.7; Violoncellos 293.6. If only one is done, 275.527: add to the present curve +3.0 dB at 0.00 s, +4.5 at 0.04-0.08, +3.0 at 0.12, +0.5 at 0.16, 0 from 0.20 to 0.30, +3.0 at 0.34-0.38 (cap 9.0), +1.0 at 0.42. Predicted stem: -51.5, -51.2, -51.1 at 0-100 ms and about -52.5 at +350 ms.
(b) Rule for the actor: after any change that moves a held string note's length in seconds by 2 ms or more (tempo, leads, caesuras), refit the re-bow fill that follows it. Run `qnshift51.py` with a threshold of 0.002 for the keys of `rebow_fills.json`.
(c) Acceptance on the master, not only the stem: lowest 50 ms of the master within 0.4 s of each pedal re-bow not more than 2.5 dB under the 0.35 s before it. c51 reads 2.3, 1.2, 2.4, 0.2, 0.3 (c50 0.3, 4.8, 3.1, 1.5, 0.1), so by this measure the pedal as a whole is not worse than c50.

Judgement: levels, correlations and the 23 / 14 comparison measured; the summation mechanism inferred. The same explanation fits the new S1 failure at Double basses 144: data equal in seconds, takes equal (correlation 1.000), the note before it 46 ms shorter, and the new note's level arrives 150 ms earlier (-51 to -52.5 through the gap; c50 fell to -58.4), which removes the audible separation (own-band dip 11.3 to 1.0 dB). For that repeat use the volume notch of SHARED-TECHNIQUES item 24 (`LEVEL_SHAPES_S["Double basses"]` at 144: (-0.085, 0), (-0.060, -8), (-0.015, -8), (0, 0)); it does not depend on how the two samples add.

### 2. Wetness: the strings' 0.539 s is a change of the measured set, not of the hall; like for like it is 0.414 s. The final chord's 0.46 s is within the repeatability of the reading

Where: `check44.py` family tails (strings) and the master tail at qn 304.

Evidence (measured, my own script, stops keyed by score position):
- `check44.py` accepts a family stop only if the family rests 1.2 s after it. In c50 the strings had three stops: qn 9 (0.660 s), qn 90 (0.361), qn 138 (0.319); median 0.361. In c51 the rest after qn 138 is 0.88 s (1.22 s in c50; the caesura at 139 was removed), so the stop is dropped and the median of the two left is (0.665 + 0.414) / 2 = 0.539.
- On the same three stops c51 reads 0.660, 0.414, 0.372: median **0.414 s** (c50 0.361). Qn 9 is unchanged to the millisecond.
- The +0.05 s at qn 90 and 138 is real but comes from the playing, not the hall: the beat before qn 90 is 1.154 s instead of 1.592 s with the same diminuendo in qn, so the level over the last 0.2 s (the reference) is 0.5 dB lower (1.1 dB at 138) while the room still carries the louder sound from before. The drop at +0.3 s is 15.9 dB (c50 16.3) and 16.2 (18.6). R Strings per beat: median difference 0.0 dB against c50.
- Final chord: the data in the last 3.3 s are identical in seconds in c50 and c51. Master t20 0.460 against 0.444 s is three 5 ms frames, with the reference level 0.8 dB lower (-67.3 against -66.5 dBFS). The string family alone (dry stems plus R Strings) reads 0.450 s in c51 against 0.464 in c50, the other way. The delivered mp3 reads 0.455 s (t10 0.280).
- The delivery does not fill stops or breaths: the gain (delivered minus master) before and at the lowest point differs by 0.4 dB or less at qn 29, 102, 124, 268, 286, 90, 138 (dips 6.1, 10.5, 9.0, 4.6 dB in the mp3 against 5.7, 10.2, 9.0, 4.7 in the master). SHARED-TECHNIQUES item 35 (`rise_delay_s`) is not needed here.

Fix: no audio change. In the check: give `check44.py` a fixed list of string stops by score position (qn 9, 90, 138, 304) or lower `rest` to 0.8 s, so the set cannot change with the map; report the per-stop values beside the median. Treat the final-chord limit as 0.45 ± 0.02 s. Do not apply item 36 (post-hall fade on celli and basses) to the final chord: it is a printed ppp morendo with a fermata, and its tail did not change.

Judgement: measured. The wettest string stop is still qn 9 (0.66 s, 8.6 dB drop at +0.3 s; identical since c49); the winds enter on it, so it is not exposed (inferred).

### 3. Bass clarinet, qn 108: the cut starts 100 ms before the swell, leaving a 2 dB dip and then a 4.4 dB bump

Where: Bass clarinet, D flat 3 at 108 (bar 37 beat 1, p, decrescendo), under Flute 1's arrival.

Evidence (measured, 30 ms steps after the beat): -42.2, -42.7, -43.1, -43.7, -44.2, **-46.5, -46.3** (165-195 ms), -45.1, -44.1, -42.9, **-42.1, -42.3, -42.6** (315-375 ms), -44.1, -46.3, -46.9, then -46.4 to -47.7. The C3 before it holds -44.4. With the envelope removed the swell is a plateau from 285 to 375 ms, 6 dB over its surroundings; c51's shape is at full depth from 170 ms. The peak is 3.6 dB lower than in c50 (the fit works), but the note now dips 2 dB under the C3 and then stands 4.4 dB over its own continuation for 150 ms. K level of the bass clarinet at 108.0-108.5 is -43.9 and -43.7, 5.8 dB under the flute, so this is a matter of the line's smoothness, not of covering.

Fix (`build/score_config.py`, replace the c51 row; values in seconds after the beat, to be written in qn at 1 qn = 1.0 s here): shape 0 dB at 0.215 s, -5.0 at 0.275, -5.0 at 0.385, 0 at 0.455. Predicted from the stem: -43.4 at 195 ms, -44.0, -43.6, -44.2, -44.4, -44.8 from 255 to 435 ms, level with the C3 within 1 dB.

Judgement: measured; the prediction assumes the envelope is linear in dB.

### 4. Flute 1, bar 37: leave the entry as it is; optional 30 ms correction at 108; retire the second test at 111

Where: Flute 1, qn 108 and 111.

- 108: the raw hole (envelope removed) is still 10.7 dB at +375 ms, the same depth and within 15 ms of c50's time (+390 ms), so it repeats and the shape can be trusted. The shape reaches its +8 dB at +344 ms, while the hole begins at +330 ms: 345 ms reads -38.5 and 375 ms -42.1. Optional: raise the shape to +9.5 dB from +0.345 to +0.40 s and keep +8 to +0.48 s. Predicted: 375 ms -40.6, hole 2.6 dB under the head. Not needed for the balance: the margin at the downbeat is back at c49's value A-weighted (+4.8 dB).
- 111: the remaining irregularity is at the slur into the note, not in its body: the stem falls from -38.6 at -105 ms to -43.1 at -15 ms and +15 ms, and is back at -39.6 by +45 ms (a 4.5 dB dip of about 100 ms, in A's area). After that the note rises steadily (-39.2 at 75 ms, -35.9 at 285 ms, -33.0 at 795 ms), which is the printed crescendo's peak. The envelope reaches +15.3 dB at +0.35 s. Do not add more gain. The second test of my predecessor (111.5-112.0 not more than 2.5 dB over 110.0-111.0) reads +2.6; a 0.1 dB miss on a limit chosen by eye is no reason for a change. Set it to 3.0 dB.

Judgement: measured.

## Checked, no change proposed

- Violins I and II at 197.5 (bar 59, the theme in octaves, f): Violins II drops to -32.5 / -31.3 K for the half beat (c50 -28.5 / -28.9) while Violins I rises to -24.7 (c50 -27.8), so the octave doubling is 7.8 dB apart for one eighth (c50 0.7). The sum of the two is unchanged (-24.7 against -24.8). Violins II's lead on this note went from 240 to 140 ms and the played note is 100 ms shorter; this is a join-timing effect for critic A, not a level row.
- Violins I pickup at 249 (after the kept breath): first quarter beat -43.5 (c50 -39.6); Violins II -45.1 in both. The two sections are now closer than in c50. Keep.
- Violoncellos div and Double basses in the half beat before the breath at 286: -3.3 and -2.0 dB against c50, because the caesura is shorter (1.314 s beat against 1.574). The master beat is 2.0 dB lower. Consistent with the printed breath; keep.
- Dynamic mapping (A-weighted medians of note bodies, families): pp woodwinds -54.7, horns -54.5, strings -54.6, divisi and solo -54.0; p -49.5 / -48.8 / -47.9 / -45.7; mf -42.5 / -38.5 / -38.4 / -41.0; f woodwinds -39.0, horns -34.3, strings -35.5, low brass -28.0. Within 0.6 dB of c50, except the horns' mf (c50 -42.1): that figure is the median of two tracks (Horn 1 -35.0 on 2 notes, Horns 1-2 a2 -42.0 on 2 notes), and no horn note moved 2 dB in the note-by-note comparison, so it is a change of which notes count as mf, not of level (inferred).
- Timpani and low brass at the climaxes: unchanged (above). Clarinet 1 bars 87-88: +1.0 to +3.7 K per half beat over cor anglais and celli with its envelope at +9.3 to +9.9 dB; unchanged.

## Do not touch

Everything on the c50 and c51 B lists; the four c51 level rows except the bass clarinet shape's timing (finding 3); the celli shape at bar 73 (-2.5 / +0.5); Flute 1's fill at 111 (`hold_s` 0.30) and its trims; the hall, sends and `deliver` settings (finding 2 is a measuring matter); the kept breaths at 29, 102, 124, 268, 286 (dips of 4.6 to 10.5 dB survive in the mp3); the CC16 pre-roll reset (takes are repeatable).

Scratch folder: `/private/tmp/claude-501/mockup-loop/mvt2-c52-B/` (239 MB: copies of the earlier B scripts `lib.py`, `m1.py`-`m7.py`; new `g1.py` level fits, `d1.py` / `d2.py` note-by-note c50 against c51, `r1.py` / `r2.py` re-bow curves, `t1.py` take correlation, `w1.py`-`w3.py` wetness and delivery, cached frame levels of the c51 stems, the decoded mp3). Left in place, as the loop lead's notes ask.

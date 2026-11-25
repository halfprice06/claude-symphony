# Critic B, cycle 55 (render of cycle 54): the volume envelope, statistics and the with/without test; balance

Data used: `build/parts.json` (byte-identical to `cycles/c54/build_fix/parts.json`, the delivered stems after the stem
fix), `build/mix.json`, the stems in `cycles/c54/render/` (01-32, dry; the four return stems were not touched).
Scratch folder, left in place (4.6 MB, no audio): `/private/tmp/claude-501/mockup-loop/mvt2-c55-B/`.
No REAPER, no bridge job, nothing written outside this report and the scratch folder.

Manual notes: `loop/MANUAL-READING.md` has no row for cycle 55 (the table ends at 47), so no page reading this cycle.

## Method

1. Layers. I ran a copy of `tools/score_to_parts.py` in the scratch folder (`tagrun2.py`) in which every item added to
   `vol_parts` is tagged with the source line that appended it; its `parts.json` is byte-identical to `build/parts.json`.
   Each of the 2,300 items was then evaluated alone, which gives the dB contribution of every layer at every time
   (`items.json`). The actual envelope is `build_reaper.vol_points()` (gain, `vol_db`, dyn/soft trims, tail holds).
2. Classes. Slow: role rows, hairpin gains, mix dyn/soft trims, phrase arch, divisi chord cut, final fade, the timpani
   roll rules. Per-note level: pitch trims, note trims, METRIC_DB, phrase tops, UNI_BOOST. Per-note shape: early fills,
   re-bow fills, loop fills, SWELL_DB, sostenuto holds, JOIN_NOTCH / JOIN_NOTCH_S, slur pair release, accent swells,
   bloomv, timpani loud attack. `LEVEL_SHAPES` / `LEVEL_SHAPES_S` (which include `level_fits.json`) hold all three
   kinds, so each row was classed by its form: 2 s or more over two or more onsets = slow, one plateau on one note =
   level, anything else = shape.
3. Test. Per onset, stem RMS over the first 0.35 s, with the envelope, with the shape class divided out sample by
   sample, and with shape and level divided out. Median absolute step between consecutive onsets of a line (gap under
   0.5 s). For notes of 1.2 s or more also front (0.1-0.45 s) minus tail (last 0.35 s) and the standard deviation of
   100 ms frames. Per row: the standard deviation of 100 ms frame levels within 0.4 s of the row, with the row and
   with it divided out ("more even" = at least 0.3 dB lower with the row).
   In the second run (`stemsB.py`) role rows stay in the slow class and each re-bow list is split into its median
   (kept) and the rest (shape); a third variant caps the shape class at +-3 dB.

All figures below are measured unless marked inferred.

## Statistics (measured)

Whole piece, 32 tracks, 346 s: **21,990 envelope points**, 63.6 per second in total. 1,507 onsets, 14.6 points per onset.

| track | points | onsets | per onset | per second | per sounding second | travel dB | of it inside notes | notes moving 3 dB or more inside | of those unmarked |
|---|---|---|---|---|---|---|---|---|---|
| Violins I | 1,649 | 107 | 15.4 | 4.8 | 10.9 | 953 | 86 % | 43 | 13 |
| Violins II | 2,429 | 151 | 16.1 | 7.0 | 10.1 | 1,377 | 85 % | 76 | 23 |
| Violas | 2,008 | 285 | 7.0 | 5.8 | 8.7 | 1,076 | 73 % | 47 | 16 |
| Violoncellos | 2,460 | 127 | 19.4 | 7.1 | 10.2 | 1,546 | 87 % | 88 | 25 |
| Double basses | 2,337 | 112 | 20.9 | 6.8 | 9.9 | 1,392 | 84 % | 55 | 21 |
| Flute 1 | 689 | 63 | 10.9 | 2.0 | 8.9 | 536 | 72 % | 34 | 4 |
| Oboe 1 | 609 | 43 | 14.2 | 1.8 | 9.5 | 451 | 72 % | 34 | 12 |
| Cor anglais | 700 | 39 | 17.9 | 2.0 | 9.0 | 376 | 79 % | 25 | 9 |
| Bassoon 1 | 899 | 61 | 14.7 | 2.6 | 7.4 | 657 | 73 % | 43 | 19 |
| Horn 1 | 711 | 51 | 13.9 | 2.1 | 9.0 | 432 | 74 % | 27 | 5 |

(All 32 tracks: scratch `stats.txt`.) The reference projects have 0.01-0.36 points per second per track (lead inbox).

- Travel: 12,068 dB in total. **77 % inside single notes**, 16 % within 40 ms of a note start or end, 7 % in rests.
- By class: shape 7,743 dB, per-note level 3,338, slow rows 2,832, mix trims and phrase arch 2,637.
- **644 of 1,507 notes (43 %) move 3 dB or more inside the note.** 199 of the 644 (31 %) have no hairpin over them, no
  dynamic inside them and no accent, tenuto, portato or fermata (timpani rolls and the final fade counted as marked).
  The shape class alone moves 404 notes by 3 dB or more: largest layer early fill on 206, re-bow fill 91,
  `level_fits` shapes 34, JOIN_NOTCH_S 28, `LEVEL_SHAPES` 16, all others 29.
- Grid: 14,954 points (68 %) lie on the 0.125 qn grid; 5,133 (23 %) are exactly collinear with their neighbours; 5,851
  (27 %) are stair steps of 0.3 dB or less one grid step apart (the dyn/soft trim following the 1-CC steps of
  `dyn_curve`, and hairpin gains sampled on the grid).
- Fast notes are not where this movement's envelope moves: violas' pizzicato triplets bars 37-44, 3.1 points and
  1.8 dB of travel per onset; the portato eighths of bars 48-51, 5 points for 15 onsets. The movement is on legato and
  held notes.

Layers by size (items, tracks, travel, largest value):

| layer | written by | class | items | tracks | travel dB | max dB |
|---|---|---|---|---|---|---|
| re-bow fill | `build/rebow_fills.json` (`tools/fit_rebows.py`) | shape | 80 | 8 | 3,173 | 10.0 |
| early fill | `build/early_fills.json` | shape | 308 | 19 | 2,311 | 8.0 |
| pitch trim | `build/pitch_trims.json` | level | 195 | 11 | 1,467 | 8.0 |
| hairpin gain | `score_to_parts.py` `hpgain` | slow | 207 | 26 | 1,140 | 7.0 |
| role rows | `build/roles.json` | slow (183 single-note rows: level 128, shape 55 by form) | 562 | 32 | 2,368 | 10.0 |
| `LEVEL_SHAPES_S` / `level_fits.json` | `build/level_fits.json`, `build/score_config.py` | level 93, shape 42 | 137 | 18 | 1,194 | 12.0 |
| `LEVEL_SHAPES` | `build/score_config.py` | slow 93, level 37, shape 29 | 159 | 32 | 899 | 16.5 |
| long-note swell | `SWELL_DB` 1.5 (`score_to_parts.py` line 222, item `swell_db`) | shape | 193 | 27 | 680 | 1.5 |
| note trim | `build/note_trims.json` | level | 83 | 17 | 628 | 10.0 |
| JOIN_NOTCH, JOIN_NOTCH_S | `build/score_config.py`, `build/join_notch_fits.json` | shape | 44 | 8 | 410 | 11.2 |
| sostenuto hold | `SOST_SUSTAIN_DB` 2.5 (`swell_sost` contours) | shape | 54 | 22 | 260 | 2.5 |
| METRIC_DB | `METRIC_DB` (harp, pizzicato) | level | 113 | 3 | 237 | 1.5 |
| slur pair release | `SLUR_PAIR_RELEASE` -2.5 | shape | 15 | 7 | 75 | 2.5 |
| phrase tops | `PT_DB_PER_ST` in `LEAD_SPANS` | level | 31 | 7 | 66 | 1.9 |
| accent swell | `GENTLE_ACCENT` | shape | 9 | 8 | 58 | 6.5 |
| timpani rules, divisi cut, final fade, loop fill, bloomv, UNI_BOOST | `score_to_parts.py` | slow / shape / level | 43 | | 623 | |

## The with / without test on the main lines (measured; role rows kept, re-bow lists split)

Median note-to-note step in dB: with the envelope / shape class capped at +-3 dB / shape off / shape and level off.
Long notes: front minus tail with / cap / shape off.

| line | n | with | cap 3 | shape off | shape + level off | front - tail with / cap / off | shape class |
|---|---|---|---|---|---|---|---|
| Horn 1, theme bars 7-14 | 22 | 1.49 | 1.63 | 1.52 | 2.33 | -1.2 / -1.4 / -1.9 | no change; level helps |
| Oboe 1, bars 15-22 | 11 | 2.29 | 3.16 | 2.89 | 2.88 | -0.8 / -1.8 / -3.9 | helps |
| Violin I solo, bars 17-22 | 11 | 1.65 | 1.65 | 1.65 | 1.49 | 8.0 / 8.0 / 8.0 | none present |
| Violins I, theme bars 22-30 | 24 | 1.99 | 1.86 | 2.54 | 2.54 | -1.5 / -2.5 / -4.0 | helps |
| Violins II, theme bars 22-30 | 24 | 2.15 | 1.30 | 1.42 | 1.12 | -2.3 / -2.9 / -5.2 | hurts the step, helps the long notes |
| Violoncellos, counter-melody 23-30 | 18 | 2.54 | 2.85 | 3.92 | 4.01 | -4.7 / -4.1 / -4.2 | helps |
| Violas div, bars 23-30 | 11 | 2.86 | 2.86 | 4.69 | 4.80 | 0.9 / 0.9 / 0.7 | helps |
| Bass clarinet, solo 31-36 | 12 | 2.51 | 2.11 | 1.68 | 1.79 | 0.3 / 0.3 / 0.1 | hurts |
| Flute 1, theme B 37-44 | 30 | 1.96 | 2.29 | 2.42 | 3.55 | -0.8 / -1.7 / -2.2 | helps; level helps more |
| Cor anglais, bars 41-44 | 14 | 1.54 | 1.64 | 1.78 | 1.92 | 1.2 / -0.1 / -3.4 | helps a little |
| Oboe 1, bars 45-47 | 9 | 1.87 | 2.30 | 1.43 | 0.91 | 1.8 / -0.9 / -3.9 | hurts the step |
| Violoncellos, bars 45-47 | 9 | 1.82 | 1.93 | 3.57 | 3.57 | -0.6 / -5.1 / -8.0 | helps |
| Cor anglais, quotation 47-50 | 6 | 2.40 | 2.40 | 1.89 | 1.31 | -2.4 / -2.4 / -2.7 | hurts |
| Violas, pizzicato 37-44 | 87 | 1.72 | 1.79 | 1.97 | 2.16 | | small help |
| Violas, portato 48-51 | 15 | 1.10 | 1.10 | 1.10 | 1.10 | | none present |
| Violins I, bars 53-60 | 30 | 0.81 | 0.87 | 1.57 | 1.17 | -3.3 / -3.3 / -3.5 | helps |
| Violins II, bars 53-60 | 30 | 1.21 | 1.21 | 1.70 | 1.70 | -2.7 / -2.7 / -2.7 | helps |
| Horn 1, bars 53-60 | 19 | 2.34 | 2.18 | 3.65 | 2.82 | 2.9 / 2.5 / 0.1 | helps the step |
| Violoncellos, bars 53-60 | 19 | 2.37 | 2.22 | 1.78 | 1.90 | 0.3 / -1.3 / -1.3 | hurts the step |
| Violins I, tutti 61-64 | 6 | 4.08 | 1.76 | 1.28 | 2.77 | -1.8 / -1.8 / -1.4 | hurts (6 onsets, printed sf: weak evidence) |
| Violins II, tutti 61-64 | 8 | 5.36 | 3.21 | 2.93 | 3.00 | -1.8 / -2.6 / -3.2 | hurts (same caveat) |
| Trombone 1, quotation 63-64 | 10 | 2.59 | 1.89 | 2.59 | 1.28 | 16.3 / 14.0 / 11.2 | fitted level rows hurt |
| Violins I, A' 71-78 | 26 | 1.56 | 1.56 | 1.65 | 1.65 | -2.0 / -2.0 / -2.4 | no change |
| Violins II, A' 71-78 | 26 | 2.00 | 1.97 | 1.79 | 1.72 | -3.5 / -3.5 / -4.6 | no change |
| Violoncellos, counter-melody 71-78 | 18 | 2.43 | 1.90 | 2.13 | 1.87 | -1.4 / -3.3 / -4.9 | step: none; long notes: helps |
| Bassoon 1, bars 71-78 | 9 | 4.30 | 4.68 | 3.86 | 6.07 | -4.1 / -4.8 / -5.6 | shape hurts, level helps |
| Violins I, bars 79-82 | 9 | 1.88 | 1.44 | 0.99 | 0.78 | -1.0 / -1.0 / -0.7 | hurts |
| Violins II, bars 79-82 | 9 | 2.21 | 2.23 | 2.88 | 2.74 | -0.7 / -0.6 / 0.5 | helps |
| Violoncellos, bars 79-82 | 7 | 1.92 | 2.76 | 3.36 | 2.79 | 2.5 / 2.0 / 1.3 | helps |
| Clarinet 1, coda 85-89 | 4 | 2.65 | 2.46 | 2.31 | 1.68 | -4.8 / -4.8 / -4.9 | 4 onsets: no verdict |
| Double basses, coda | 12 | 2.63 | 2.68 | 4.01 | 3.30 | 1.2 / 0.9 / -1.2 | helps (re-bow fills) |
| Violas div, coda | 10 | 4.44 | 5.27 | 5.01 | 5.01 | -0.2 / -1.7 / -4.4 | helps |

Of 44 lines (all in scratch `repB.txt`): the shape class lowers the step by 0.3 dB or more on 16, raises it on 10,
changes nothing on 18. This differs from Movement I: here most of the shape class is fitted correction of the samples,
and it works on the strings. Long notes (1.2 s or more), median standard deviation of 100 ms frames with / without the
shape class: strings 2.28 / 2.69 dB (93 notes more even by 0.5 dB or more, 22 less even, of 348); winds 1.69 / 1.57
(22 / 14 of 227); brass 1.88 / 1.81 (6 / 4 of 83). The shape class does not make wind and brass long notes more even.

Balance (153 track-by-section cells): shape off changes a section level by 1 dB or more in 27 cells, 2 dB or more in
5, largest 3.4 dB (Horn 4 bars 23-30 +3.4, Violoncellos 79-82 -2.9, Violins II 61-64 -2.8, Timpani 65-70 +2.7,
Violoncellos 61-64 -2.3). Shape capped at 3 dB: 3 cells of 1 dB or more, largest 1.5. **Shape and level off: 63 cells of
1 dB or more, 34 of 2 dB or more, 20 of 3 dB or more, largest 6.3.** Balance between tracks does not depend on the
shape class once role rows and the re-bow lists' medians are kept; it does depend on the per-note level class.

## Findings

### 1. Two thirds of the points are slow layers drawn as stairs; write them as ramps (keep, key differently)
Where: every track. Layer: mix dyn/soft trims and hairpin gains, written by `tools/build_reaper.py` `vol_points`
(0.125 qn grid, a point at every value change) from `vol_db` sampled in `score_to_parts.py` (`vgrid`, 0.25 qn plus
breakpoints). Evidence: with both per-note classes removed the envelope still has 16,096 of the 21,990 points; Horns
1-2 a2 carries 418 points for 8 notes and 60 dB of travel. A Douglas-Peucker pass at 0.1 dB (dB against seconds)
leaves 13,965 points of the full envelope (-36 %) and 5,921 of the slow-only envelope; at 0.25 dB 9,349 and 3,555.
Before / after on the stems: none, the level change is at most the tolerance (computed, not rendered; inferred that
REAPER's interpolation between the kept points stays within it, since REAPER interpolates in its fader scale: verify
with a `stem_fix.py`-style comparison of old and new `vol_points`, as the Scherzo did in c15).
Fix: in `vol_points`, after `vals` is final, drop every point that lies within 0.1 dB of the line between its kept
neighbours (exact breakpoints from `vol_bp` are kept when they are extremes). No musical change; the track view
then shows ramps where the score has hairpins and steps where it has dynamics.

### 2. Early fills are the "peak on every note": 203 of 308 measurably help, 61 do not (keep the 203, remove the 61, no 3 dB cap)
Where: 19 tracks, mostly Violoncellos (65 rows), Violins II (43), Violins I (30), Oboe 1 (28), Bassoon 1 (26), Flute 1
(25), Cor anglais (24), Horn 1 (20). Layer: early fill, `build/early_fills.json`, written at `score_to_parts.py` lines
4431-4449: a lift of 2-8 dB (median 3.8; 186 over 3 dB, 40 of 6 dB or more) from just before the onset to 0.10 s
after it, gone by 0.35 s. This is what gives a legato line one peak per note in the track view.
Evidence: on the 253 filled notes of 0.9 s or more, front (0-0.35 s) minus body (0.45-0.85 s) is -2.5 dB with the fill
divided out and -1.2 dB with it; 159 notes come closer to 0, 54 move away; 31 end with the front 2 dB or more over
the body, and 25 of those 31 were already at or over the body without the fill. Per track, without -> with: Oboe 1
-3.7 -> -1.3, Cor anglais -5.0 -> -1.7, Bassoon 1 -3.3 -> -0.9, Horn 1 -2.5 -> -1.1, Violoncellos -2.7 -> -1.0,
Flute 1 -1.7 -> 0.0; Violins II -1.2 -> -1.2 and Violas -1.9 -> -1.9 (no gain). Local evenness: 189 rows more even,
29 less, 90 unchanged. On the lines the layer alone lowers the median step on 11 and raises it on 7 (Violoncellos
bars 53-60 by 1.08 dB, Bass clarinet solo 0.86, Violins II theme 22-30 0.68, Violins I 79-82 0.65, Cor anglais
quotation 0.39). Capping at 3 dB gives back half of the gain where the fills work (Violoncellos 45-47 front minus
tail -0.6 with, -5.1 capped, -8.0 off; Oboe 1 15-22 step 2.29 / 3.16 / 2.89), so a cap is the wrong tool for this
layer.
Fix: per-row decision. Three tests per row (local evenness, distance from the mean of the two neighbours, front
against body; `rows.py`, table in scratch `early_fill_rows.json`) give keep 203, undecided 44, remove 61. Remove
candidates (score onset, dB): Flute 1 120(+4) 189(+6) 191.5(+2) 196(+5) 200(+1) 258.5(+2); Oboe 1 43.5 45 55.5
196(+4) 270.5(+7); Cor anglais 127.5 130 152 163; Clarinet 1 184 195(+4) 266 270(+4); Bass clarinet 21 92(+4);
Bassoon 1 24 36 145 182(+5) 200 231(+7) 238 255(+5) 262(+5); Horn 1 182; Violins I 68 71 80 84 86 86.5 184 186
270(+4) 292; Violins II 108(+6) 159 206(+5) 261 270.5; Violas 3 75 84 246; Violoncellos 51(+6) 56 68.5 77 164(+5)
180(+6) 186 206 253(+6) 259; Violoncellos div 53. Several were tuned in c53-c54 (Violoncellos 68.5, 77, 253, Violins
I 80, Bassoon 1 200): simulate the removal on the stems against those cycles' own checks before taking it. Keep the
rest and give `early_fills.json` rows the rule "a new row needs a before/after stem figure".

### 3. Re-bow fills carry balance as well as shape: split each list (keep; key differently)
Where: 80 lists on Violins I, Violins II, Violas, Violoncellos, Double basses and the three divisi tracks; coda
(qn 275-304), the introduction, bars 65-70, 37-40. Layer: re-bow fill, `build/rebow_fills.json` (fitted by
`tools/fit_rebows.py`), written at `score_to_parts.py` lines 4541-4570. Largest layer by travel (3,173 dB); every
list moves 5.6-14 dB (median p5-p95 8.0 dB) inside one held note.
Evidence: 60 of 80 lists make their note more even, 7 less (median frame deviation 3.19 dB without, 2.17 with), so
the layer is needed for Dan's item 8. But 48 of 80 lists have a median of 2 dB or more away from 0 (Double basses
225.1-227.7 +7.4 dB, 221.7-238.4 +4.5 to +5.5; Violins II 295.7-302.1 -5.4 to -6.0; Violoncellos 165.2 -6.0): that
part is level, not shape. With the layer switched off whole, Double basses bars 65-70 fall 4.1 dB; with the medians
kept no cell of the basses moves 1.5 dB.
Fix: in `fit_rebows.py` (or at load in `score_to_parts.py`) subtract each list's median and write it as a role row
over the same span in `build/roles.json`; the remaining list is the shape class. The on / cap3 / off switch then leaves
balance alone. Keep the fills on in every setting used for a delivery; cap3 on this layer costs the coda (Violas div
front minus tail -0.2 with, -1.7 capped, -4.4 off).

### 4. Four rule layers have no measured benefit: 293 rows (remove from the envelope; the swell and release stay on CC11)
- Long-note swell, `SWELL_DB` 1.5 (`score_to_parts.py` line 222, items `swell_db`, lines 4245-4247): 193 rows on 27
  tracks, +1.5 dB at 40 % of a long note, unmarked. Local evenness: more even 2, less even 54, unchanged 133. Line
  step medians change by 0.06 dB or less on all lines but two (Violas div 23-30 +0.95 rougher without it, Violas div
  coda 1.19 smoother without it). The same notes already have the CC11 swell (code comment at line 4245). Remove
  the dB copy (`SWELL_DB = 0` in `build/score_config.py`).
- Sostenuto hold, `SOST_SUSTAIN_DB` 2.5 (lines 4411-4429): 54 rows. Winds and brass, 31 rows: more even 5, less 14.
  Strings, 21 rows: more even 8, less 3; the only line it changes is Violas bars 61-64 (step 0.47 with, 1.49 without).
  Remove on winds and brass, keep on the strings in bars 61-64 (printed molto sostenuto).
- Phrase tops (lines 4850-4876, `PT_DB_PER_ST`, `LEAD_SPANS`): 31 rows of at most 1.9 dB. More even 0 of 20 measured;
  it raises the median step on four lines (Cor anglais quotation by 0.61 dB, Violins II theme 22-30 by 0.53, Oboe 1
  45-47 by 0.40, Bass clarinet solo by 0.30) and lowers it on none. Remove (`PT_DB_PER_ST = 0`), or move to CC11 if a
  critic wants the contour kept: inferred that CC11 is the right place, not measured.
- Slur pair release, `SLUR_PAIR_RELEASE` -2.5 dB (lines 4700-4746): 15 rows; more even 4, less 4, unchanged 7; no line
  changes by 0.1 dB. It is a fall in the envelope after the hall (S3 concern). Move the fall to CC11 or remove.
Together with finding 2 this removes about 350 per-note rows without touching a line that measures better
with them.

### 5. The per-note level class is balance: do not switch it off; move section-sized rows to roles and stop trims returning to 0 (keep, key differently)
Where and evidence: with pitch trims, note trims and plateau rows divided out, 34 of 153 section cells move 2 dB or
more: Timpani 61-64 -6.3 (a `LEVEL_SHAPES` plateau +4.5 and a role), Double basses 83-92 +5.3 and 65-70 -4.0
(`pitch_trims.json` Double basses, -4.3 / +4.0 dB mean), Oboe 1 37-44 -4.9 (`note_trims.json`, +5.0 dB mean), Violas
65-70 -3.4 (`note_trims.json` +3.7), Bassoon 1 bars 7-14, 31-36, 65-70 -3.7 to -4.2 (`pitch_trims.json`). Solo margins
(named part against the sum of all other dry stems) with / shape off / shape and level off: Horn 1 bars 7-14 +8.9 /
+8.9 / +9.3; Bass clarinet 31-36 +5.5 / +5.5 / +6.1; Flute 1 37-44 -2.4 / -2.1 / -3.0; Oboe 1 45-52 -6.4 / -7.5 /
-10.8; Clarinet 1 coda -2.7 / -3.4 / -5.8; Horn 1 53-60 -7.2 / -7.7 / -9.4. On the lines the pitch trims lower the
step on 9 (Flute 1 37-44 by 1.45 dB, Bassoon 1 71-78 by 1.29, Cor anglais 41-44 by 0.71, Horn 1 theme by 0.42) and
raise it on 4 (Double basses 53-60 by 1.43, Horn 1 53-60 by 0.83, Flute 1 79-82 by 0.46, Double basses coda 0.35).
At 45 joins a level row falls toward 0 dB between two notes that both carry a trim of the same sign of 1 dB or more
(pitch trims 24, `level_fits` plateaus 13, note trims 8): a notch in the envelope at the join with no purpose.
Fix: (a) the switch for this class should offer on and cap, not off; (b) rows that set a whole phrase (Oboe 1
`note_trims` in 108-140, Violas 220-238, Timpani `LEVEL_SHAPES` 203.98-209.4, Horn 4 `LEVEL_SHAPES` 84.5-90.5) belong in
`build/roles.json`; (c) in `trim_shape` (`score_to_parts.py` lines 4268-4296) and the plucked-step branch, when the next
note carries a trim, ramp from this note's value to the next one's over the same [next moved onset - 0.05, + 0.03]
window instead of through 0; (d) add `_skip_onsets` in `pitch_trims.json` for Double basses 172-204 and Horn 1
172-204 after a stem simulation (the trims there were fitted for other passages). METRIC_DB (113 rows of 0.5-1.5 dB
on harp and pizzicato) lowers the step by 0.24-0.47 dB on its three lines: keep, or move to velocity (inferred that
the plucked patches follow velocity closely enough; Slot C has the patch evidence).

### 6. The switch, and what each setting would cost here (proposal for the actor)
`tools/score_to_parts.py`: tag each `vol_parts` item with a class at the append (the line-to-class table is in scratch
`common.py`, `NAMES` and `CLS`), with `LEVEL_SHAPES` / `LEVEL_SHAPES_S` rows taking an explicit class field instead of
the form rule used here; `VOL_CLASS = {"shape": "on" | "cap3" | "off", "level": "on" | "cap3"}`, plus a per-layer
override. Expected from the stems:
- shape off: 6,977 points with finding 1 applied (-68 %); 16 lines rougher, 10 smoother; string long notes less even
  (2.28 -> 2.69 dB), fronts of legato notes 1.3 dB weaker at the median; balance within 3.4 dB (5 cells over 2).
- shape cap3: balance within 1.5 dB; keeps the step gain on Violins I 22-30 and 53-60, Violins II 53-60, Violas div
  23-30; loses it on Oboe 1 15-22, Violoncellos 23-30 and 79-82, and half of the long-note gain.
- recommended: shape on, minus findings 2 and 4, with finding 3's split, and finding 1's ramps. Range-test the lines
  where the shape class hurts with it off for that line only: Bass clarinet 90-108 (step 2.51 -> 1.68), Cor anglais
  147-160 (2.40 -> 1.89), Violoncellos 172-204 (2.37 -> 1.78), Violins I 262-274 (1.88 -> 0.99), Violins II 63-90
  (2.15 -> 1.42, but its long notes need the fills: front minus tail -2.3 with, -5.2 off, so remove only the five
  listed rows there).
Standing checks: none of this was tested against S1-S3 or the solo timing; JOIN_NOTCH / JOIN_NOTCH_S (44 rows; 26 more
even, 3 less) and the accent swells (9 rows; the score prints 2 accents) are Slot A's to judge. The 61-64 tutti
figures rest on 6-9 onsets with printed sf and tremolo entries and should not decide anything alone.

## Lens, second priority (measured, section averages on the dry stems)
- The named solos keep their margins and none depends on the shape class by more than 1.1 dB (finding 5). Timpani
  bars 61-64 sit 20.3 dB under the sum of the other stems and bars 79-82 18.7 dB under: not covering. Low brass bars
  61-64 4.8 dB under the rest.
- Bars 45-52: Oboe 1 (-47.7 dB) is under the Cor anglais (-45.9) over the section and level with the pizzicato basses
  (-47.8); the section average mixes the oboe's head (45-47) with the cor anglais quotation (47-50), so this needs a
  per-bar check before any change. Not measured further this cycle.
- Open items from c54 (Clarinet 1 289, Violins II 154 and 47, Bassoon 1 262) were not re-measured.

Do not touch: re-bow fills as a layer (60 of 80 lists even out their note), the early fills on Oboe 1, Cor anglais,
Bassoon 1, Horn 1 and Violoncellos outside the listed rows, pitch trims on Flute 1 37-44, Cor anglais 41-44, Bassoon 1
71-78 and the Horn 1 theme, role rows, the timpani roll rules, the divisi chord cut and the final fade.

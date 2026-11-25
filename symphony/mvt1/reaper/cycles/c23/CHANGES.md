# Cycle 23: changes (actor)

All 15 critic findings except C #6 (tempo) were accepted. Four tracks were fully rebuilt (Violins I, Violins II, Violoncellos: the Sus Marc LITE row for the A #2 test; Violas: the c22 `rt_ms` revert). Everything else was `--midi-only`. After the render a level-only stem fix applied the accent refits (A #1 steps 2-3), new fills, a level correction for the A #2 strokes, a further Horn 1 cut (B #1) and a peak notch.

REAPER steps:
1. Fresh start (`-new`), project opened (33 tracks).
2. `build_reaper.py build/parts.json jobs --midi-only` on 20 tracks (all winds, Horns 1-3, Horns a2, the five string tracks). Violins I, Violins II, Violas and Violoncellos changed Opus state and were fully rebuilt.
3. Saved. The quit job timed out and REAPER was killed after the save. Fresh start, open, then `render_cycle.py 23`.
4. Level-only stem fix (two passes, below), then `render_cycle.py 23 --measure-only`.
5. In the same session: `build_reaper.py --mix-only` on the 19 tracks the stem fix changed. Saved. The quit job timed out again; REAPER was killed after the save.

Files:
- `cycles/c23/before/`: the c22 tools and data.
- `cycles/c23/rendered_build/`: the data and code the render was made from.
- `cycles/c23/render_first/`: the original master and the 19 stems the stem fix replaced.
- `cycles/c23/actor_scripts/`: the measurement scripts used here (`chk.py`, `xover.py` / `xosum.py` crossovers, `joins.py`, `spacing.py`, `pdiff.py`, `ccchk.py`; `lib.py` holds the K/A-weighted envelopes). The scratch folder was deleted.

## Code

- `tools/score_to_parts.py`:
  - `STAC_LEAD_S` {track: s}. A printed-staccato string note on a "Stac" row starts that many seconds early and keeps its played length. A previous note that would overlap ends 0.02 qn before the moved onset. CC11 holds from the moved onset. Not applied to REP_SPLIT or measured-tremolo strokes. parts.json `stac_leads`.
  - `STR_REST_SHORT` {"at": {track: [(a, b)]}, "frac", "max_qn", "min_bpm"}. Inside a listed span, an unslurred string note of max_qn or less (written) that is followed by a written rest ends at frac × its written length after the score onset. parts.json `rest_short`.
  - `ACCENT_BODY_S_SHORT` / `ACCENT_BODY_SHORT_MAX_S` (0.8 s): the body-cut ramp for accented notes shorter than 0.8 s.
  - `ART_SPANS` entries take `"poly": True`, so chords in the span take the row as well.
  - `STR_STROKE_ROWS` = ("Sus MAX", "Sus Marc LITE"): string rows that take the Sus MAX stroke leads (re-tongue lead, and the Leg -> Sus entry path). Without this the Marc LITE strokes lost their 0.06-0.10 s leads.
  - `SHORT_SUS_LEAD_CAP_FRAC` and an `ABUT_LEAD` "cap_frac" key: a lead never takes more than that share of the previous note's slot.
    - Reason: C's 0.10 s leads left the listed viola sixteenth (152.5) only 0.04 qn (0.02 s), and Violins II's slurred sixteenths 0.08 s.
- `tools/fit_accents.py --front-s S`: every note, accents and neighbours alike, is measured on its front, from min(moved onset, score onset - 0.03 s) to the score onset + S. The peak search is off in this mode.
- `tools/fit_accent_bodies.py --short-s` (default 0.8 s): a note shorter than this uses a body window of +0.28 s .. its played end - 0.03 s.
- `build/mix.json`: the Violas `rt_ms` 400 removed (the c22 test that failed).

## Accepted (in the render)

| Finding | Change | Measured c22 -> c23 | Pass? |
|---|---|---|---|
| A #1 step 1 | GENTLE_ACCENT wind/string `swell_s` (0.07, 0.25, 0.6) -> (0.03, 0.15, 0.40), `swell_s_leg` (0.04, 0.35, 0.7) -> (0.03, 0.22, 0.50). Brass unchanged | Before the refit, front-body (onset..+0.15 against +0.30..+0.75 s), accented minus plain: winds <0.75 s -1.2 -> +1.5, ≥0.75 s +0.8 -> +2.6; strings -1.3 -> -0.2, +0.7 -> +1.5 | partial (completed by the refit below) |
| A #2 test | `ART_SPANS` "Sus Marc LITE" (poly) on Vln I/II 327.9-331 and 563.9-567.9, celli 283.9-286 | See "Test results" | partial |
| A #3 | `STAC_LEAD_S` Violins I 0.05, Violas 0.03 | Vln I Stac -3 dB point +0.110 -> +0.065 s, peak +0.130 -> +0.095. Violas +0.090 -> +0.050, peak +0.120 -> +0.080 | partial (pass ≤ +0.05 / ≤ +0.09) |
| A #4 test | `STR_REST_SHORT` Violas 520-536, frac 0.6 (15 dyads); `rt_ms` reverted | Drop from the dyad front to the last 0.07-0.12 s of the rest (my measure): median 2.6 (0.2-9.9) -> 9.9 (8.5-13.0) dB. Dyad front -31.5 -> -31.8 dB | yes |
| B #1 | Hn1/Hn3 `HP_TARGET_AT` 644 "mf+". Horn 1 and Horn 2 -3 dB from 644.25 to 652 (the stale fff hold). Stem fix: Horn 1 a further 0 -> -4 dB over 644.6-647 | Hn1 - Hn2 K per half beat 644.5-647.5: +3.8 +9.0 +7.9 +10.0 +9.6 +6.2 +4.0 -> +2.8 +6.8 +3.3 +4.8 +4.1 +0.4 -1.1. Oboe 1 - Horn 1 (A): -3.2..-0.9 -> +0.7..+7.0. Master K at 646.5: -21.8 -> -22.9 | yes |
| B #2 | Vc / Bn1 / Cl1 +2.5, Vln I / II -1.5 over 520.3-536 | Theme onset margins (A) median -1.1 -> +1.4; covered 12 -> 3 of 18. Theme minus descant K +1.8 -> +5.0. Master -18.6 -> -18.1 K | yes |
| B #3 | Oboe 1 shape, 579.2-581.7 (-5 dB at its deepest) | Oboe 1 per half beat 579.5-581.5: -34.4 -33.9 -31.4 -31.1 -37.3 -> -36.7 -38.5 -36.4 -35.8 -38.1 (as simulated). Master 580.5/581: -30.5/-30.2 -> -34.1/-33.5 | yes |
| B #4 | Bass clarinet -2.5 (2.7-16.6), celli +1.5 (2.7-12.1) | Bass clarinet minus celli (A), bars 2/3/4: +7.2 / +2.5 / +3.7 -> +3.2 / -1.5 / +1.2. Master K bars 2-4: -34.7 / -36.0 / -42.6 -> -34.7 / -35.9 / -43.5 | yes |
| C #1 | `LEG_CAP_FRAC` 0.75 over 0-728 on Vln II / Violas / celli; `LEG_MIN_GAP_S` 0.10 on all three | Crossover, groups capped in c22 (median): Vln II Leg Slur +0.160 -> +0.075, Leg BC +0.085 -> +0.017; Violas Leg Slur +0.117 -> +0.062, Leg BC +0.110 -> +0.030; celli Leg Slur +0.102 -> +0.030. Joins of 6 dB or more: Vln II 12 -> 8, violas 3 -> 6, celli 8 -> 7 | partial (Vln II / violas Leg Slur over +0.05) |
| C #2 | `ABUT_LEAD` lists: violas +66 onsets, celli 17, Vln II +12 (0.10 s, `cap_frac` 0.45); `SHORT_SUS_LEAD_S` 0.06 -> 0.10 (cap 0.45) | Unled Sus MAX crossover: violas +0.105 -> +0.045 (n 79), celli +0.120 -> +0.060, Vln II +0.150 -> +0.075. Vln II short-sus led +0.080 -> +0.040 | partial (≤ +0.04 target) |
| C #3 | `LEG_LEAD_S` Clarinet 0.05 | Clarinet 1 Leg Slur +0.082 -> +0.042 (n 76), earliest -0.030 | yes |
| C #4 | `LEG_ART_EXTRA_S` Vln II Leg BC -0.03 -> +0.03, Violas Leg BC +0.05 | Cap-free Leg BC: Vln II +0.032 -> -0.033 (Leg Slur -0.000); violas +0.040 -> -0.020 (Leg Slur -0.020) | violas yes; Vln II overshoots 0.033 s |
| C #5 | `entry_leads.json` Vln I/II 118 +0.10, Vln II 383 +0.10, Violas 118 +0.05; `ENTRY_LEAD_ART_S["Violins II"]` Leg Slur +0.06 | Crossover Vln I 118 +0.105, Vln II 118 +0.085, 383 +0.040 s (C measured arrivals +0.20 / +0.20 / +0.25) | partial |

### Test results (A #2, Sus Marc LITE)

Front (-0.03..+0.15 s) minus body (+0.30..+0.75 s), time of the peak, and 2-5 kHz in the first 80 ms minus the body. c22 (Sus MAX) -> c23:

| Stroke | Front - body | Peak (s) | 2-5 kHz | Whole-note level |
|---|---|---|---|---|
| Vln I 328 | -1.1 -> +3.7 | 0.23 -> 0.07 | -0.7 -> +4.2 | +5.9 |
| Vln I 330 | -4.9 -> +4.8 | 0.48 -> 0.07 | -6.4 -> -0.2 | +7.5 |
| Vln I 564 | -6.5 -> +0.5 | 0.52 -> 0.20 | -5.1 -> -5.6 | +5.5 |
| Vln I 566 | +0.3 -> +10.0 | 0.21 -> 0.16 | -5.6 -> +6.7 | +7.3 |
| Vln II 328 | -1.8 -> +0.4 | 0.28 -> 0.14 | -1.4 -> -0.8 | +2.6 |
| Vln II 330 | -5.9 -> -4.8 | 0.29 -> 0.35 | -5.2 -> -2.0 | +3.2 |
| Vln II 564 | -2.0 -> +2.9 | 0.41 -> 0.17 | -2.8 -> -2.8 | +6.8 |
| Vln II 566 | +0.3 -> +7.8 | 0.29 -> 0.17 | -4.9 -> +1.1 | +8.2 |
| Vc 284 | -1.6 -> +1.9 | 0.24 -> 0.18 | -6.1 -> -4.3 | +6.2 |
| Vc 285 | -9.8 -> +1.4 | 0.50 -> 0.18 | -6.1 -> +0.9 | +1.8 |

Across the 10 strokes:
- median front - body -1.9 -> +2.4 dB;
- median peak 0.29 -> 0.17 s (3 of 10 at 0.15 s or earlier);
- 2-5 kHz at +2 dB or less on 8 of 10 (Vln I 328 +4.2 and 566 +6.7 brighter).

The row plays 2-8 dB louder than Sus MAX at the same CC11 and envelope. The stem fix put each stroke back to its c22 whole-note level + 0.5 dB.

Controls changed by under 1 dB (bars 32 and 72 upper strings, violas 328/330).

Verdict: partial pass. The row moves the weight to the front of the note (the hammer strokes no longer swell). Two Violins I strokes carry a brighter front. Before extending the row to bars 32, 72 and 131, judge the two bright strokes by listening, and treat the level offset as a property of the row.

## After the render: level-only stem fix (`stem_fix.py`, two passes)

1. **A #1 steps 2-3** (refits on the c23 render):
   - `fit_accents.py 23 --front-s 0.18 --lo 2 --hi 4`:
     - strings: with the c20 options and skips, plus the Marc LITE strokes;
     - winds: default options.
     - Front-window "over" median: strings +1.7 -> predicted +2.8 dB, 35 -> 64 of 141 in 2-4 dB; winds predicted median +2.9, 106 of 141 in 2-4 dB.
     - The refit gave two -6 dB whole-note steps (Flute 1 118 and Bassoon 1 328, measured against staccato neighbours). Both were put back to their c22 values.
   - `fit_accent_bodies.py --min-s 0.45 --front-min 2 --max-cut 3`, strings and winds: body cuts on 64 string accents and 90 wind accents. Predicted front-body: strings -0.2 -> +1.8, winds +0.3 -> +2.0.
   - Measured after the fix (accented minus plain front-body):

     | Family | Notes under 0.75 s | Notes 0.75 s or longer |
     |---|---|---|
     | Winds | +3.3 | +2.5 |
     | Strings | +2.0 | +1.5 |
     | Brass (control) | unchanged | unchanged |

   - Item 8 (2-5 kHz first 80 ms minus body, median): winds -6.2 -> -4.9, strings -3.5 -> -3.3, brass -8.5 -> -8.5. Over +3 dB: winds 9 -> 10, strings 6 -> 7. A front-weighted level swell raises this measure by itself, so the +1.3 dB on the winds is front level, not a brighter sample.
2. **Fills:** `auto_fills.py 23` was merged only for the tracks whose timing changed: Violoncellos (13 retimed, 4 new, 4 removed or lowered) and Clarinet 1 (5 new or raised).
3. **A #2 levels:** each Marc LITE stroke back to its c22 level + 0.5 dB (steps of -1.4..-7.7 dB).
4. **B #1:** Horn 1 0 -> -4 dB over 644.6-647, held to 648.2.
5. **Peak notch:** the master's new top sample peak was 1.603 at qn 641.14 (c22 1.427 there): the timpani tie stroke 0.41, tuba 0.26, celli and low brass in phase, with +0.09 each from the retimed Clarinet 1 and Violins II. Timpani and tuba -2 dB over 641.0-641.3: peak 1.465 there; the top peak is now 1.531 at 636.14.

All stems are within 0.3 dB of c22 in whole-file RMS.

## Rejected / deferred
- C #6 (tempo arcs at the sostenuto and largamente, RAMP_SPANS ends at 252/628) deferred. The evidence is inferred, and it is a whole-project tempo rewrite that moves the climax arrivals and the limiter. This cycle already changed timing on four string tracks and the clarinets; keep timing changes measurable one at a time.
- B #3's optional Oboe 1 180 shape: not simulated, not made.
- Horn width revert: still deferred (no horn rebuild).

## Open for c24
- **Vln II Leg BC extra:** +0.03 overshoots. Cap-free Leg BC targets now cross -0.033 s, against Leg Slur -0.000, and 8 new Leg BC targets cross at -0.09..-0.12 s (236, 260, 373.5, 396, 404, 523, 531, 620). Try 0.0.
- **Early targets after the 0.75 cap:**
  - celli 418 -0.15, 563 -0.145, 225.5 -0.09, 588 -0.08;
  - violas 378, 589, 600 at -0.085..-0.10.
- **Still late:** Vln II and violas Leg Slur targets in the formerly capped groups, +0.075 / +0.062 s.
- **A #2:** extend Marc LITE to bars 32/72/131, or not, after listening. The Vln I 328/566 fronts are 4-7 dB bright in 2-5 kHz.
- **Joins (30 ms) that got worse:**
  - celli 529: 1.2 -> 6.2 dB;
  - Clarinet 1 107.5 and 213: 3.1/4.3 -> 6.8/8.3 dB;
  - violas at 6 dB or more: 3 -> 6.
- **Climax margin:** 160 > 122 is 0.88 dB on delivered S (c22 1.08).

## Before / after (c22 -> c23, after the stem fix)

| Measure | c22 | c23 |
|---|---|---|
| Master integrated (float stem sum) | -16.2 LUFS | -16.3 LUFS |
| Master LRA | 22.6 LU | 22.5 LU |
| Master sample peak | 1.552 (qn 636.33) | 1.531 (qn 636.14) |
| Master true peak | +3.8 dBFS | +3.7 dBFS |
| Delivered integrated | -19.7 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.5 LU |
| p10-to-max span | 19.1 dB | 18.9 dB |
| Delivery limiter | 2.1 dB | 2.0 dB |
| Delivered true peak | -1.6 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.55 / 4.48 dB | 8.60 / 4.48 dB |

Notes on the render as first made, before the stem fix: delivered LRA 14.6 LU, limiter 2.6 dB, sample peak 1.603.

- Climax order (delivered S max): 160 -10.12 > 122 -11.00 > 167-170 -13.21.
- Attack probe: 0 flagged.
- Item 7 (master 100-300 Hz / centroid autocorrelation at 3.95 s): unchanged from c22 within 0.08 in all five held passages.
- REAPER memory: 18 GB with 0 compressed at the render start; 45 GB with 0 GB compressed after the render; 46 GB with 34 GB compressed later, idle during analysis.
- Delivered mp3: `cycles/c23/mvt1-mockup-c23.mp3`.

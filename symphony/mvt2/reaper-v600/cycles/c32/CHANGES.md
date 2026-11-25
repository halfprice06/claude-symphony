# Cycle 32 (actor), 2026-11-07

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c31 render). Snapshot: `before/`. Data the render was made from: `rendered_build/` (parts.json, mix.json). First-render stems of the stem-fixed track and master: `render_first/`. The first actor attempt made every data change and the `--midi-only` build (`build.log`, 15 tracks, 0 errors), then stopped before the render (`NOTES-interrupted.md`). A second attempt rendered, measured, stem-fixed and wrote this file.

## Changes (files and parameters)

- **A #1 (BRIEF item 9), Trombone 1 bars 63-64.** `build/entry_leads.json` Trombone 1 212.5: 0.06 qn (about c30's 0.11 s) back, so the legato into the slurred accent at 213 uses c30's timing again. `note_trims.json` Trombone 1 213 -3.5 and 215 -2.2 removed. `score_config.py` LEVEL_SHAPES_S: 216 tenuto +3.5 dB over the note; 217.5's +2.5 lift removed; 218 lifted up to +3 dB after the onset, before the printed decrescendo.
- **A #3, violas sotto voce portato 152-168.** Per-note CC7 in the rests (`CC7_POINTS["Violas"]`): A3 18 (-4 dB), B3 33, D4 40, A flat 3 / E flat 4 28. Entry leads 164.5/166.5 0.15 -> 0.08.
- **A #4 / B #4, Violins II div 108-124.** Role -5 -> -1.
- **A #5 (S1), Violins II 45/50.** `MERGE_NOTCH_AT {"Violins II": {50.0: 14}}`; `rebow_fills.json` 5.15 (the 45 tenuto) -3 dB at -0.12..+0.08 s and 0 at +0.12..+0.36 s.
- **B #1, stale series 1 loop fills.** `loop_fills.json`: Double basses 3/168/204, Violins II 108/116, Violoncellos 63 and Violoncellos 3's 5.59/6.71 s lifts removed. New WARNING in `tools/score_to_parts.py` when a LOOP_FILLS lift ends after the note's first piece.
- **B #2, Horn 1 counter-melody bars 54-60.** Horn 1 roles [176,188] 0.5 -> 2.5, [188,204,-2,4] -> +2; Bassoon 2 [187.5,195.5,-6,0.5].
- **B #3, bars 25-26.** Violoncellos [72,77,-2,0.5]; Violins I and II [71.9,78,2,0.5]. Note trims Violoncellos 74 +4 and Violins I 72 -3 removed.
- **B #5, Horn 1 p solo.** Horn 1 note trims 24 +3, 25.5 +2, 26 +2; Bassoon 1 [23.5,28.5,-2] and [231.5,237,-2,0.5].
- **B #6, "4 soli".** Double basses [220,238,-3]; Violoncellos [273.9,286,-3,0.5].
- **C #1, Flute 1's sf at 212.** CC7 127 -> 57 (-7 dB) from 211.96 to 213 (before the hall).
- **C #2, bars 79-81.** Flute 1 roles [262.6,263.5] -3 -> -6, [263.5,265.9] +1 -> -2, new [265.9,271,-3].
- **C #3, bar 29 joins.** JOIN_NOTCH Violins I (85.84-85.98, -6), Violins II (85.79-85.95, -5) and (86.78-86.98, -5.5), Violoncellos (76.82-76.98, -4).
- **C #4, soft horn colour.** `mix.json` loud_eq on Horns 1, 2 and 4: highshelf 1200 Hz -4 dB, wet 1 in soft passages and 0 at 194-220 and 261-270 (Horn 4: 0 from 261 on, where its mute EQ takes over).
- **C #5, coda clarinet.** Clarinet 1 [280,286,-2.5,0.5].
- **C #6, solo violin vibrato.** `CC1_HOLD["Violin I solo"] = 72` (mostly Sus Vib on the DIV A KS Master, read in the .oib). `score_to_parts.py` now applies CC1_HOLD on vibrato-crossfade patches too. After the render: `mix.json` Violin I solo gain_db -1 -> +0.4 (stem fix, see below).

No Opus state changed (no articulation row, mic, hall or seat).

## Rejected or deferred

- **A #2** (Double basses re-bow pieces swinging 11-14 dB): deferred. It needs a re-bow refit, and the fitted re-bows are Do-not-touch without a new fit.
- **A #6** (celli "4 soli" on the Violoncellos div track): deferred. B #6's level change was used instead.
- Auto fills were not re-run.

## Measured (c31 -> c32, plain RMS dB on the stems)

- A #1 Trombone 1: fall after 213 less steep (213.25-214: -20.6/-24.9/-27.5/-30.1 -> -18.6/-21.5/-24.0/-26.6); 216-217 +3.5 dB (-27.8 -> -24.5); 217.5 -2.1; 218 +0.7.
- A #3 violas: A3 bars -3.6..-3.8 dB, B3/D4 bars up to +1.5..+2.9; the violas now sit 11-17 dB under the cor anglais.
- A #4/B #4 Violins II div 108-124: -52.9 -> -48.9 (main Violins II -47.7 -> -48.0).
- C #1 Flute 1 212.0-213: -6.4..-7 dB; master 212.0-212.4 -1.1..-1.6 dB. The delivery limiter fell from 1.4 to 0.9 dB.
- C #2 Flute 1: -2.7 / -3.0 / -3.3 dB in the three spans; Violins I unchanged (-31.7).
- C #3: master bump at 85.875 -35.7 -> -39.7, at 86.875 -36.1 -> -38.0; Violins I 85.75 -40.9 -> -46.8; celli 76.875 -36.7 -> -41.0.
- B #2: Horn 1 188-196 -40.7 -> -36.8, Bassoon 2 -36.5 -> -41.8 (horn now 5 dB over it, was 4 under); Horn 1 176-188 +1.8.
- B #3: celli 72-77 -38.1 -> -40.9, Violins I 72-78 -43.4 -> -40.9, Violins II -42.2 -> -40.2.
- B #5: Horn 1 over Bassoon 1 at 24-28.5 5.3 -> 7.7 dB; at 232-236 2.1 -> 4.0 dB.
- B #6: Double basses 220-238 -3.0 dB; celli 274-286 -2.8 dB.
- C #4: Horn 1 1-5 kHz share 140-186 -14.9 -> -16.9 dB, 230-258 -16.4 -> -18.4; Horn 2 230-258 -14.3 -> -16.1. Level change from the shelf alone under 0.3 dB. (c30's soft layers measured -19..-21; the shelf closes about 40% of that gap.)
- C #5: Clarinet 1 280-286 -40.7 -> -43.1.
- C #6: CC1 72 took the solo 1.4 dB under c31 (bars 48-65 -42.8 -> -44.2; first bar -3.7). Stem fix +1.4 dB (gain_db -1 -> +0.4) puts it back at c31's level.
- A #5 Violins II 50: the merged repeat's notch is 0.8-2.3 dB deeper in the 50.0-50.25 frames.

## Build and render

- parts.json had been regenerated with no WARNING; `--midi-only` on 15 tracks, 0 errors (first attempt).
- **Lock held 01:23:33 to 01:50:53 (27 min).** `reaper_ctl.py restart` (32 tracks); memory rose 20 -> 44 GB over 8 minutes and stayed flat at 44 GB (35 GB compressed) for 3 minutes; Audio_Init via `_c32_audio_init.lua`: 48000 / 512 / no input, Mac Studio Speakers. 152 GB free; MAC DRIVE mounted. `render_cycle.py 32 --force-memory` (compressed memory over the gate).
- After the render: stem fix on Violin I solo (`stem_fix.py 32 cycles/c32/rendered_build build --apply "Violin I solo"`), `build_reaper.py --mix-only "Violin I solo"` (`build-mix-stemfix.log`), save, quit, unlock; then `render_cycle.py 32 --measure-only` (`render_cycle_measure.log`).
- **REAPER memory after the render: 45 GB (25 GB compressed).**

## Key numbers (c31 in brackets)

- Master: -21.4 LUFS (-21.3), LRA 23.7 (24.0), TP -2.9 dBFS (-2.3), sample peak 0.718, no clipping.
- Delivered `cycles/c32/mvt2-mockup-c32.mp3`: -19.7 LUFS (-19.8), LRA 15.5 LU (15.6), TP -1.7, span 17.3 dB (17.4), limiter 0.9 dB (1.4).
- Climax order: bars 61-62 -16.0/-16.1 dB against bars 79-80 -18.4/-19.0.
- Attack probe: 0 of 20 flagged (c31 0). Trombone 1 212.5 starts -0.08 s (limit 0.06, ok: early side).

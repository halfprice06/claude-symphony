# Cycle 42: changes (actor; coordinator's release-cap decision, critics A/B/C on the c41 render)

This cycle ran in two attempts. On 2026-11-07 the disk had 24 GiB free (under the 30 GB rule), so it stopped before the build; see `NOTES-interrupted.md`. It resumed on 2026-11-08 once the coordinator reported 41 GB free.

- Snapshot before the changes: `before/`.
- Data the render was made from: `rendered_build/`. Final data after the stem fix: `build/`.
- Scripts in `actor_scripts/`:
  - `check42.py`: checks of the accepted findings. Output on c41: `check42_c41.txt`; first render: `check42_first.txt`; final: `check42_final.txt`.
  - `linger42.py`: the basses' old pitch at soft pitch changes.
  - `relevel41.py`: copied from c41.
  - `turn_lock.sh`: the turn rule.
  - `state_check.txt`: output of the state check.
- c41's `m41.py` and c40's `rbdips.py` were reused: `m41_c42_first.txt`, `m41_c42_final.txt`, `rbdips_c42_*.json`.

## Changes

- **Bar 66 niente (A #1, C #1).** `tools/fit_rebows.py` now includes each track's CC7 lane in the planned level, `+ 20*log10(cc7/127)`. Before, the fit read c30's niente CC7 fade as a hole and filled it back in.
  - Refit with the CC7 plan, before the render: the 223 holds on Violins II, Violas and Violoncellos (+6.9 / +8.6 / +1.2 -> +0.5 / +2.1 / -5.3 dB; c39's were +0.9 / 0.0 / -4.8) and Violins II 263.921 (-4.6 -> -6.0, clamped).
- **Release caps (coordinator, `build/mix.json`).**
  - String sections: pp/p 400 -> 600 ms; mf-ff 300 ms kept.
  - Violin I solo, Violoncellos div, Violins II div, Violas div: 300 ms on every layer -> 300 ms mf-ff / 600 ms pp/p.
  - Horns unchanged.
  - These 9 tracks' Opus states changed, so they were rebuilt fully in a single build. The other 6 changed tracks were `--midi-only`.
- **Soft repeats (Dan's S1).**
  - `tools/score_to_parts.py`: `STR_REP_NEW_BOW["sus_fall"]` now also applies before soft STR_REP_NEW_BOW strokes and portato strokes, replacing a smaller portato fall.
  - `build/score_config.py`: Violins II, Violas and Violoncellos get 8 CC over 0.06 s at p or softer; basses 10 -> 12 CC.
  - In parts.json this adds falls at Violins II 49.875 (50), Violoncellos 127.84 (128) and Double basses 143.84 / 155.86 / 167.87.
- **A #3.**
  - Violas 69 and 248.5 are in `DOWNBOW_STROKE_AT`. They take the existing Leg -> Sus entry path: velocity 105, leads 0.06 / 0.115 s, a 0.04 qn gap.
  - Their c41 LEVEL_SHAPES_S fills are removed.
  - Basses 144: the -5 dB shape is removed; the 12 CC sus_fall replaces it.
- **B #1.** Horn 1's 182 shape +5 -> +2 dB, and +3 dB over 184.1-195.35.
- **B #2.** Horn 1's role over 16.5-42 +2.5 -> +4.5 dB; Bassoons 1-2 and bass clarinet -1.5 dB over 17.5-41.9 (`build/roles.json`).
- **B #3.** Flute 1 +2 dB over 120.4-123.95 (role).
- **C #3.** Oboe 1 gets a LEVEL_SHAPES step of +4.2 dB at 148.0, back to 0 at 148.59. The swell C measured comes from the HP_SOFT_DEC gain ramp over 148-148.59, not from the role. C's role edit would have lifted the end of the note before (147.45-147.95), so I did not use it.
- **C #5.**
  - Violins I and II +2 dB over 190-199.6, ramping in over 190-194.
  - Celli -3 dB role now starts at 186.5, with the end ramp unchanged.
  - Violins II +4 dB over 252.5-253.55, back to 0 under the 254 attack. I moved C's 253.45 end so that no fall lands on the held note.
- **After the render, level only (stem fix on 8 string tracks, plus `--mix-only` while holding the lock).** The longer releases filled the re-bow dips, so the c41 fills overshot: 33 attack peaks over 2.5 dB and 18 over 3.5 dB, Violas 87 +8.1.
  - Refit command: `fit_rebows.py 42 cycles/c42/rendered_build/parts.json --hold-max-after 298:0 --window "Double basses:2.6" --skip "Double basses:273.229"` on the 8 string tracks.
  - `relevel41.py` re-levelled the basses' pedal 221.8-235.659 to the c39 means +1.5 dB, the basses' coda 276.05-283.605 to the c39 means, and Violoncellos div to the rendered means.
  - Violins I 264.417's +2.5 dB from 0.6 s (c41 B #2) is put back, because the refit had dropped it.
  - A #4 / C #4: the refit brought back the bar 91 rise. Two slow LEVEL_SHAPES fix it: Violas -4.5..-5.5 dB over 298-298.6, easing to 0 by 300.1; Violas div -3.5 dB over 297.8-298.6, easing to 0 by 300.3.

## Measured (c41 final -> c42 final; `check42_*.txt`, `m41_*.txt`)

- **Bar 66 niente**, master per 0.5 qn from 222.5: c41 -41.3 -40.3 -41.2 -40.2 -40.8 -45.9 -47.5 -> c42 -41.2 -40.0 -41.8 -44.5 -45.8 -49.5 -49.3. It now falls steadily from 223, by 9.3 dB to 225.5.
  - Stems from 223 to 225.5: Violins II -41.9 -> -58.4, violas -51.4 -> -68.8, celli -47.4 -> -67.0.
- **Violins I minus Violins II (A)** per 0.25 qn over 264-265.75: c41 5.3 .. 0.8 -> c42 7.1 5.9 5.6 5.5 5.5 4.9 4.1 -0.7.
- **Bar 91**, per 0.25 qn over 297.5-299: Violas -52.3 then at most -52.7 (c41: up to -47.3); Violas div about 3 dB under Violins I (c41: level with or over them). The master no longer rises at 298.
- **Release.**
  - String soft phrase ends: t20 median 0.34 -> **0.44 s**; t10 0.21 s, unchanged. Divisi/solo: t20 0.32 -> 0.43 s.
  - Final chord, master: t10/t20 0.22/0.34 -> **0.30/0.47 s**, inside the 0.43-0.58 s target. Stems 0.45-0.47 s.
  - The steepest 0.1 s step is now 7.3 dB at 0.4-0.5 s (c41: 8.4 dB at 0.2-0.3 s). Smaller and later, but not yet the smooth fall of the uncapped c39 render (about 3 dB per 0.1 s).
  - Only Violoncellos 87 falls more than 10 dB in 0.05 s (10.6 dB, as before).
- **Soft repeats** (15 printed repeats; stem / master dip, my own measure):
  - Stem median 5.6 -> 6.1 dB; master median 3.0 -> **3.4** dB.
  - Master dips under 3 dB: 7 -> 4 (Violins II 45 1.8, Violas 69 2.1, Double basses 168 2.0, Double basses 156 2.9).
  - Violas 248.5: stem 6.8 -> 11.4, master 2.5 -> 3.2. Violas 69: stem 5.2 -> 8.0, master 2.0 -> 2.1.
  - Violins II 45 (1.8) and basses 144 (stem 3.8 -> 3.3, master 4.1 -> 3.8) are about unchanged. On the coordinator's two named repeats: Violins II 45 is still under 3 dB in the master; basses 144 holds above 3 dB.
- **Re-bows** (final stems): dip median 2.7 dB, p90 4.4, max 7.4; attack peaks over 3.5 dB: 6 (max 5.0). c41: 7 (max 5.0).
- **B #2:** Horn 1 over Bn1 + Bn2 + BCl + harp (A) per bar 7-14: c41 3.5 1.2 2.2 5.4 3.2 5.7 0.7 3.3 -> c42 6.9 4.5 5.5 8.7 6.5 9.1 4.0 6.5. Every bar is over B's +2.5 target.
- **B #1:** Horn 1 minus Violins I (A) over 184-195.5: median about -8 -> about -6. The head (182.4-183.0) at 7.1 A against the f note at 196 at 4.6: still 2.5 dB over. Open.
- **B #3:** Flute 1 over all others (A) over 120-123.5: minimum 0.6 -> 2.6 dB.
- **C #3:** Oboe 1's rise over 148.0-148.75 is 7.2 -> 3.9 dB. The master falls 2.5 dB after the fp peak (c41 about 1.8).
- **C #5:** master rises 5.7 dB from 188 to 196 (c41 5.1); Violins I rises 3.5 dB over 190-195 (c41 flat). Violins II at 252-253.5 sags 2 dB (c41 5-7).
- **State check** (`tools/state_check.py`, copied from Movement I c47, against c41): no state runs on any track.
  - Single-note flags on tracks not rebuilt: Horn 4 268 +5.2 dB / -50 ms. It is the first Leg Slur MAX note after a Sus note that ends exactly at 268, and its legato target at 270 is sample-identical, so I judged it not a flipped legato state and did not rebuild it.
  - Also Bass clarinet 21 (pcX -191 ms, level +1.2) and Trombone 1 217.5 (+1.7 dB). Both are below the run threshold.
- **Basses' old pitch at soft pitch changes** (Movement I c47 note; `linger42.py`, old minus new harmonics at +0.35 s):
  - Most changes are unchanged.
  - Worse: 286 (bar 87, A flat 1 -> F 1) -10.0 -> **+0.8 dB**; 246 -18.7 -> -7.2; 61 -18.4 -> -10.8.
  - The 600 ms pp cap lets the old note ring under the new one at these three changes. A stem fix cannot change this; open for c43.
- **Delivery and checks.**
  - Master -20.4 LUFS, LRA 23.9 LU, TP -0.4 dBFS, sample peak 0.946.
  - Delivered `cycles/c42/mvt2-mockup-c42.mp3`: -19.8 LUFS, LRA 15.5 LU, TP -1.6 dBTP, p10-to-max span 19.0 dB (at the limit), limiter about 2.6 dB.
  - Attack probe 0 late or holes. No clipping; 32 stems present.
  - Image: correlation below 250 Hz 0.66, side/mid -6.1 dB (unchanged).

## Rejected or deferred

- **A #5** (Trombone 1 215 velocity 118): its own condition, no master-audible bite, holds.
- **A #6** (basses 4 soli on DIV A): not in this cycle's list. It needs memory and another refit of the basses.
- **C #2a (700 ms) and C #2c (horn mf cap 350)**: the coordinator chose 600 ms and to leave the horns.
- **C #4**: its re-levelling of Violas div was done with level shapes instead.
- **MANUAL-GAPS**: none tried, to keep the cycle lean.

## Open for c43

- The basses' old pitch rings at soft pitch changes 286 / 246 / 61. Options: a basses-only pp cap around 400 ms, or a CC11 fall on the old note before a soft pitch change.
- Violins II 45 and Violas 69 master dips about 2 dB: Violins II 45 is a p slur-head stroke above the sus_fall max_cc; Violas 69 sits under the bar 23 tutti.
- Horn 1's 182 head is still 2.5 dB (A) over its own f.
- Final chord: a 7.3 dB / 0.1 s step at 0.4-0.5 s.
- Delivered span 19.0 dB (limit 19).

## REAPER and lock

- First attempt: lock 18:58:01-19:01:38 on 2026-11-07; REAPER started but no project was opened, and it was quit without saving.
- Second attempt: lock 2026-11-08 07:34:54-08:19:37 (45 min), after the turn rule (no other waiter).
- REAPER settled at 44 GB with 0 compressed after the open (memory flat for 2 min) and before the render (no `--force-memory`). After the render it was at 45 GB, 34 GB compressed.
- Disk free 35 GB before the render. Audio 48000 Hz / 512, no input. Build of 15 tracks (9 full) about 3 min.

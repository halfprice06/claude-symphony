# Cycle 29 (actor): changes on the c28 render's findings

Critic reports: `cycles/c29/reports/A.md` (articulation), `B.md` (balance), `C.md` (blend), all on the c28 render. Snapshot before any change: `cycles/c29/before/`. Data the render was made from: `cycles/c29/rendered_build/`.

## What changed

### Stale re-bow data (A #1, B #1, C #1; BRIEF item 8)

- `build/loop_profiles.json`: deleted Violins I `0`, Violoncellos `274`, Double basses `220`/`271` and Timpani `226`. These are series 1 profiles on notes that the re-bows now split. Each new bow restarts the sample, so the profile's phase no longer matched. The timpani roll's layer changed in c28.
- `build/rebow_fills.json`:
  - Deleted the stale keys Violins II 44.341/50.352 and Double basses 222.452.
  - Refitted Violins II 45/51 and Double basses 221.8-235.659 and 276.05-283.605 on a stem_fix simulation of c28 with the profiles taken out (`fit_rebows.py 28 build/parts.json --stems <sim> --skip "Double basses:273.229" --hold-max-after 301:0`). The other refitted keys moved by less than 1 dB and were kept at their c28 values.
  - Double basses 273.229 now has no fill: the p-to-ppp decrescendo sat in its reference window, and c28's chain lifted the ppp pedal to the p level.
  - After the refit, the pieces were levelled by constant offsets per key, simulated:
    - Cb 221.8-235.659: -2.2/-5.6/-0.7/+0.2/+4.1/+5.1 dB, so each piece sits at about -50 dB.
    - Cb 276.05-283.605: -1.7/-3.9/-0.9/-0.9 dB, about -52.5.
    - Vc 277.566/279.637/281.683/284.151: +1.4/+1.4/+6.2/+7 dB, so the celli no longer fall through their crescendo.
- `tools/fit_rebows.py`: new generic option `--stems DIR` (measure stem_fix-simulated stems).
- `tools/score_to_parts.py`: new generic WARNINGs:
  - a REBOW_FILLS key with no re-bow within 0.01 qn;
  - a LOOP_PROFILES key on a re-bowed note.

  Order of work: run `fit_rebows.py` after the last REBOW_AT, rebow_moves or space_rebows change.

### Balance (B; `build/roles.json`, `build/note_trims.json`)

- Clarinet 1 [204,210,-4] and Flute 2 [206,210,-2] (B #4).
- Bassoon 2 [262,268,4] -> -1 and Oboe 1 [262,268,6] -> 4 (B #5). Note trims Violoncellos 265 -4 and Cor anglais 266 -3.
- Violoncellos [124,138,-3,1] (B #6).
- Harp harmonics [273.9,277.6,4] (B #2).
- Timpani `LEVEL_SHAPES` -2 dB from 226.5, falling to -6 at 237 and back to 0 by 240 (B #3: the ppp roll decrescendo).

### Articulations (A; `build/score_config.py`, c29 block)

- **Trombone 1 (A #2).**
  - 213: the swell (`ACCENT_DB_AT` 0) is replaced by an onset-weighted shape: +4 dB at 0.03 s, 3.5 at 0.18 s, 0 by 0.45 s.
  - 215.0: +4.5 dB.
  - 217.5: `SLUR_PAIR_RELEASE_DB_AT` 0, plus +2.5 dB.
  - 218 accent: set to 4, and raised to 6.5 dB after the render (stem fix, below).
- **Violas' pizz. bars 41-44 (A #3).** `VEL_SET` floor of 48 on the pp beats (124-127, 132-137.67).
- **Violas' Detache bars 48-51.**
  - Entry leads (A #5): +0.10 s on the seven A3 eighths and +0.15 s on 164.5/166.5 (`build/entry_leads.json`).
  - The c28 -13 dB stem-fix role is moved to `CC7_POINTS["Violas"] = [(152.2, 28), (167.98, 127)]` (C's S3 note: CC7 acts before the hall, so it no longer cuts the previous note's hall tail).
- **Timpani 172 (A #4).** Stroke v64 -> 72 with +4 dB over 0.6 s, and the roll's top capped at -4 dB over 171.6-171.94.
- **Harp harmonics (A #6).** Velocities 275.5 -> 48 and 276 -> 64.
- **Harp damp (A #6).**
  - `HARP_RING_S = 2.0`.
  - `HARP_DAMP_STAFF["R.H."] = 0`.
  - `mix.json` Harp `env_release_ms` 200.
  - Every harp note now rings 2 s past its written end, and the bar 83 "R.H. étouffez" cuts the R.H. notes.

### Blend (C; `build/mix.json`)

- Wind group send 0.35 -> 0.6, and Violin I solo send 0.5 -> 0.8 (C #2; tried instead of MANUAL-GAPS #4).
- Width 0.05 on Fl1, Fl2, Ob1, Ob2, CA, Cl1, Cl2, Bn1 and Bn2 (C #3).
- Violins II div high shelf at 1.5 kHz, -6 dB (C #4).
- Violoncellos side shelf list: low shelf 200 Hz -2 and high shelf 1.5 kHz +4 (C #5).

## Rejected or deferred

- **C #6 (low-mid tilt):** optional and small. The Cb bell2 is do-not-touch.
- **CC1 dynamics on brass and clarinets (MANUAL-GAPS #1):** deferred again. This cycle already changes the wind states (send and width) and the re-bow fits, so a change to the layers would confound both.
- **A smaller observations** (breath at 268 on Oboe 1/Clarinet 1, the bar 79 run, legato join fills, smoothing the 4 soli shapes): left. The loop-profile removal was the larger lever on the soli pedals.
- **B #3's Cb role [225.5,238,4,1]:** done through the fill offsets instead.
- **B #2's Cb role [273.25,286,-5]:** done through the refit and offsets instead.

## Build and render (2026-11-06)

- `parts.json` regenerated with no WARNING. pdiff against `before/` shows changes only where listed.
- Opus state changed on 13 tracks (11 winds: send and width; Harp: release; Violin I solo: send). `build_reaper.py --midi-only` rebuilt those fully and wrote the other 19 MIDI-only; 0 errors.
- Lock taken 20:54:19, released 21:26:25: **held 32 min**. Fresh start and open, build, restart. Memory settled at 44 GB with 34 GB compressed (flat for 3 min), so the render was run with `--force-memory`. The audio device read 48000/512, no input, Mac Studio Speakers. Disk: 182 GB free; MAC DRIVE mounted.
- After the render, a level-only stem fix (`stem_fix.py 29 cycles/c29/rendered_build build --apply "Trombone 1" Violas`; the originals are in `render_first/`) and `--mix-only` for both tracks while still locked:
  - Trombone 1's 218 accent 4 -> 6.5 dB. Its front measured +0.5 dB over the 0.3 s before it; after the fix, +2.8.
  - Violas [123.6,125.95,-4,0.3] and [133.95,138.2,-4,0.5]. With the velocity floor the pp beats came up level with the p beats; after the fix the peaks are -46.5/-45.2 dB against -41.9 at 126-128. c28 was -50 against -42.
- **REAPER memory after the render: 44 GB (26 GB compressed).**

## Key numbers (c28 in brackets)

- Master: -21.3 LUFS (-21.1), LRA 23.9 (24.6), TP -1.7 dBFS, sample peak 0.822, no clipping. 33 files (32 stems + master).
- Delivered `cycles/c29/mvt2-mockup-c29.mp3`: -19.7 LUFS (-19.8), LRA 14.0 LU (14.6), TP -1.8, span 16.3 dB (16.7), limiter 1.1 dB (1.2).
- Attack probe: 1 of 20 flagged. It is the same Violins II qn 212 tremolo dip as in c26-c28 (6.5 dB against a 6 dB limit).
- Climax: master bars 61-62 -15.7 dB, unchanged; bars 79-80 -19.1 (-18.9).

## Did each change work (stem RMS dB, c28 -> c29)

- **Wobble (median 1 s range):**

  | Passage | c28 | c29 |
  |---|---|---|
  | Cb 222-238 | 8.0 | 4.6 |
  | Cb 273-286 | 11.1 | 6.5 |
  | Vc 275-286 | 7.8 | 3.7 |
  | Vln I 1-9 | 8.7 | 6.1 |
  | Timpani 226-237 | 4.0 | 2.8 |
  | Master 274-285.5 | 6.7 | 3.8 |

  Target 4 dB: met on Vc, the master and the timpani. The Cb coda and Vln I are still over it.
- **Coda:** Cb 280-285 -46.9 -> -52.8. Celli 277-286 -54.3 -> -51.0, now above the Cb. Clarinet 1 -42.7 -> -41.4, 11 dB over the Cb. Harp harmonics 274-277 -55.5 -> -52.9; their peaks are -46.0/-43.2/-47.7 (was -50.0/-43.9/-53.0, spread 9.1 -> 4.5 dB). The plucked harp under the first harmonic is -67.5 dB (c28 -61.8), 21 dB under it.
- **Bars 67-70:** Cb pedal -56.5 -> -49.9. The timpani roll is -55.5 (226-232), falling to -58.5 (232-237.5) where c28 held -54. The pedal is now 5-8 dB over the roll.
- **Violins II, bars 15-17:** 44.5-45.0 -37.9 -> -44.9 and 50.4-50.8 -42.9 -> -49.4. The stale bulges are gone.
- **Climax inner parts:**
  - Clarinet 1 206-210: -25.7 -> -28.6, 1.5 dB under Violins I.
  - Bassoon 2 262-265: -26.9 -> -30.8.
  - Vc 265: -23.1 -> -26.6.
  - Cor anglais 266: -25.9 -> -27.4.
- **Bars 41-44:** celli -43.5 -> -46.4 under the cor anglais at -39.4.
- **Trombone 1:** 215.07-215.45 -29.6 -> -25.1. Note bodies over 214.5-217.5 are now within 3.8 dB (c28 6.4). The 213 peak is at +0.03 s (c28 +0.45).
- **Timpani 172:** the roll's end is -45.7 and the stroke's first 80 ms -43.7, so the stroke is now 2 dB over the roll (c28: 6.4 dB under).
- **Violas Detache via CC7:** the span is -51.0 (c28 stem-fixed -51.3), so CC7 28 gave the planned -13 dB.
- **Wind send:** the solo levels rose 0.3-0.8 dB (Ob1, Fl1, CA), Clarinet 1's coda solo 1.4 dB and the bass clarinet solo 1.8 dB. The early-drop and tail measures were not repeated here; that is left for critic C.

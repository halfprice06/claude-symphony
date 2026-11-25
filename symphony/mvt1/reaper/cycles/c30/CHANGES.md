# Cycle 30: changes (actor, final cycle)

`loop/ONE_TIME.md` applied: this is the last cycle, so only changes that could be simulated on the c29 stems were made. There were no tests, no row or patch swaps, no Opus-state rebuilds and no tempo-map changes. Every one of the 12 critic findings is level-only, and all 12 were accepted. One of them, A #4, went in deeper than the critic proposed.

Before REAPER was touched, the whole change set was simulated on the c29 stems with `stem_fix.py 29 cycles/c30/before build --out <scratch>` plus `deliver_master.py`. The c30 render then matched the simulation within 0.5 dB on every check. Nothing measured worse than c29, so no stem fix was applied. The project, `build/` and `parts.json` are exactly the state of the delivered render.

parts.json changed only in `vol_db` / `vol_bp` on 31 tracks, plus `pitch_trimmed` on Bassoon 1 and the `early_fills` list on the celli. The `_all` shapes reach every non-percussion track. Notes, keyswitches, CC lanes and the tempo map are identical to c29.

Files:
- `before/`: the c29 tools and data.
- `actor_scripts/c30check.py RENDER_DIR PARTS MP3`: every c30 pass criterion.
- `check_c29.txt`, `check_c30.txt`: its output on the c29 render and on the c30 render.

REAPER steps:
1. Fresh start, open (33 tracks).
2. `build_reaper.py build/parts.json jobs --mix-only` on the 31 changed tracks.
3. Save, then quit. The quit timed out, so REAPER was killed after the save.
4. Fresh start, open, `render_cycle.py 30`, save, quit (killed after the save).

## Accepted

| Finding | Change | Measured, c29 -> c30 (render) | Pass? |
|---|---|---|---|
| A #1 celli/viola early fills on the old note | `early_fills.json`: `pre_s` 0 on Violoncellos 650, 422, 266, 66, 712, 10, 4, 694 and Violas 429. Violoncellos 687 fill removed. `LEVEL_SHAPES_S` Violoncellos 687.0 (A's shape: -2 over -0.20..-0.03 s, +7 over 0..+0.36 s, 0 by +0.52 s) | 40 ms peak in the old pre_s window over the larger body, stem: 422 +5.5 -> +3.5, 66 +5.4 -> -0.6, 712 +4.3 -> +0.9, 694 +1.1 -> -4.6, Vla 429 +5.0 -> +4.2, 10 +3.3 -> +2.5, 4 +3.6 -> +3.2, 687 +9.2 -> +1.0. Bar 172 master: the A-flat4 tail burst -26.9 is gone (max -29.6 now), and the G4's first 0.4 s sits 0.6 dB under the A-flat4 body (was 3.3 under). No join dip grew by more than 1.2 dB (694: 2.1 -> 3.3 on the stem, master unchanged) | yes at 687 and on most joins. Vla 429 (+4.2) and Vc 4 (+3.2) stay over A's 3 dB on my measure, which uses different body windows from A's |
| A #2 bars 43-44 horn duet | A's Horn 2 and Horn 1 `LEVEL_SHAPES` | Horn 2 G4 spread over 168.4-171.8: 11.6 -> 4.0 dB. Horn 1 over Horn 2 from 170: 16.4 -> 8.4 dB at Horn 1's entry frame, 1-3 dB after it. Horn 1 B-flat4 burst (-38/-36) gone (-45/-43). Master 172-176 in 0.2 s frames: -36.8 ... -40.2, -37.9, -38.3 ... -39.7 (c29 -35.8 -34.7 -38.1 ... -35.6 -37.0) | mostly. The one +2.3 dB step at 174.9 comes from the celli and Violins II moving under the horns (horns are falling there), not from the horns |
| A #3 celli bar 153 | `LEVEL_SHAPES` Violoncellos 611.1-611.97, -4.5 | Master 611.1-612.0 peak over the 610-611 median +4.4 -> +2.3 dB. 612 entry unchanged (master -36.5, celli -41.9) | yes |
| A #4 fugato celli 352 | `LEVEL_SHAPES` Violoncellos 351.9-353.95 at **-5.5** (A: -4) | Celli minus violas per 0.5 qn window from 352.2: +2.7 / +4.1 / -3.2 -> -2.8 / -1.8 / -8.8 dB. With A's -4 the simulation gave -1.3 / +0.1, still level with the violas on this measure | yes |
| B #1 Oboe 1 bars 45-46 | `LEVEL_SHAPES` Oboe 1 181.95-183.2, -6 | K bodies 176 / 178 / 179.5 / 180 / 182: -44.5 -42.0 -42.5 -40.0 **-34.7 -> -40.7**. Oboe re M at 182: -2.1 -> -5.5 | yes |
| B #2 cor anglais bar 93 | `LEVEL_SHAPES` Cor anglais 370.98-372.0 at -6, and B's optional +3 over 369.98-370.7 | K bodies 368 / 369 / 370 / 371: -37.8 -34.4 -39.5 -29.0 -> -37.9 -34.4 -36.6 -35.3. Master K at 371.0-371.5: -26.0 -> -27.1 | yes |
| B #3 Bassoon 1 C-sharp4 | `pitch_trims.json` Bassoon 1 `_all_arts_pitches` [61], `_skip_onsets` [351.0, 391.5] | K bodies 280 / 382 / 396 / 400 / 407.5 / 476: -33.2 -27.9 -28.5 -28.4 -26.6 -23.8 -> -38.1 -32.9 -33.4 -33.4 -30.6 -28.7, now within the range of their neighbours (-30..-38) | yes |
| B #4 Violins I bar 114 | `LEVEL_SHAPES` Violins I 453.05-455.55, +4 | Vln I K per 0.5 qn 452.5-456: -28.9 -31.5 -34.3 -35.1 -32.9 -33.3 -29.1 -28.0 -> -28.9 -29.1 -30.3 -31.1 -28.9 -29.6 -27.2 -27.7. Master K +0.3..+0.5 dB over 453-456; the master's own dip in bar 114 (2.1 -> 1.9 dB) comes from the winds' long notes, as B said | yes |
| B #5 bass clarinet B-flat2 | `note_trims.json` Bass clarinet 364 / 372 / 380 / 382 -4, `NOTE_TRIM_RAMP_S` 0.1 s | K bodies -33.5 -32.7 -30.8 -28.9 -> -37.4 -36.6 -34.5 -32.6. Re M at 364/372: -6.5/-7.4 -> -10.0/-11.0 | yes |
| C #1 fff tam-tam ring, bars 122-126 | `LEVEL_SHAPES` Tam-tam [(485, 0), (488, 3), (492, 7), (496, 9), (504.2, 9), (504.4, 0)]; the stroke and the damp at 504.2 are unchanged | Tam-tam minus master per 2 qn 488-502: -13.3 -17.6 -16.4 -17.2 -16.5 -16.2 -14.2 -16.3 -> -9.8 -12.0 -10.1 -9.1 -8.1 -8.1 -6.2 -8.0. First qn after 484 unchanged (-21.68). mp3 per qn 492-503 falls -14.8 ... -27.5, then -26.9 at 503 (+0.6; the simulation gave -0.1 there, and the stems match the simulation, so this is master-sum variance) | yes (one 0.6 dB step at 503 against C's 0.5) |
| C #2 delivery top ride + coda | `tools/deliver_master.py` TOP_RATIO 1.6 -> 2.5; `_coda26` -2 -> -3.5 dB (every track from the chorale, and the tam-tam) | See the before/after table. Limiter 2.1 -> 0.9 dB, p50-p10 5.5 -> 6.4 dB, max-p75 9.4 -> 8.6 dB. Coda bars 175-181 delivered -29.7..-31.4 (c29 -28.3..-30.0), above the intro's bars 4-5 (-33.1 / -33.6) | yes, except coda bar 176 (-29.7), which is 0.6 dB over the p bar 44 (-30.3) that A #2 lowered |
| C #3 coda cello solo lift | `LEVEL_SHAPES["_all"]` [(679.80, 0), (679.88, 2), (685.0, 2), (691.0, 0)] | mp3 bars 171-174: -26.8 -24.9 -24.5 -23.4 -> -25.3 -23.9 -24.3 -23.4 (growth 3.4 -> 1.9 dB). 692 still the loudest qn of 684-694 (-19.8). Drop from 677 to 681 15.9 -> 14.5 dB | yes |

## Rejected / deferred

None of the c30 findings were rejected. These items stay open, as both critics advised:
- the a2 brass tracks (A, patches);
- the 38-inch tam-tam patch (C, not checkable before the last render);
- the bars 80-81 Trombone 1 stab (B, 1.5-2 dB);
- the recapitulation second-theme sample hairpins (C).

## Before / after (c29 final -> c30)

| | c29 | c30 |
|---|---|---|
| Master integrated | -16.4 LUFS | -16.4 LUFS |
| Master LRA | 22.9 LU | 22.5 LU |
| Master sample peak / true peak | 1.524 / +3.7 dBFS | 1.463 / +3.3 dBFS (float stem sum, as in every cycle) |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.6 LU | 15.4 LU |
| p10-to-max span | 19.5 dB | 19.6 dB |
| Delivery limiter | 2.1 dB | 0.9 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.69 / 4.54 | 8.61 / 4.47 |
| Band shares 20-100 / 100-250 Hz | -16.84 / -8.61 | -16.8 / -8.63 |

- **Climax order** (delivered S max): 160 -10.67 > 122 -11.72 > 167-170 -13.01 > bar 26 -14.45. 160 is 1.05 dB over 122 (c29: 1.20).
- **S distribution** (mp3): p50-p10 5.5 -> 6.4, max-p75 9.4 -> 8.6, p99-p90 5.2 -> 4.8 dB.
- **Motion** fell 0.08 / 0.07 dB, under the loop's 0.2 dB regression mark.
- **Attack probe:** 0 flagged (12 checks).
- **Item 7** (`cycles/c25/actor_scripts/loopscan.py 30`): master Lento / 175-178 / 179-182 / 160-164 band at 3.95 s +0.40 / -0.09 / -0.38 / -0.46, the same as c29.
- **Item 8:** no accent data changed.
- **REAPER memory:** 18 GB with 0 compressed at the render start, 45 GB with 30 GB compressed after the render (`metrics/memory.txt`). Other processes: com.apple.Virtualization 2.7 GB (+4.7 compressed), Steam Helper 2.4 GB, python3.12 2.1 GB and 1.5 GB.

## Final state

The loop ends here. Notes on what is left:

**Open (measured, not changed):**
- The a2 brass tracks (2TP Leg Slur MAX, 2TB Sus MAX). They need new Opus instances at the 45 GB memory limit, full rebuilds and refits.
- The oboe seats (an Opus state change; c29 C #4).
- The 100-250 Hz share is -8.6 dB, at the low end of the references (-6.6..-8.75). It comes from the voicing, not the EQ.
- Celli K re master in bars 117-120 is 0.7 dB under c27.
- The recapitulation second-theme hairpins (Oboe 1 580-582, celli 596-598, Horn 1 589-591) are sample shapes that trims did not turn around.
- Bars 80-81: the Trombone 1 stab is 1.5-2 dB over the a2 horns.
- The larger 38-inch tam-tam patch is untried.
- Clarinet 1 414/422 render bright or dull at random per render. The c27 cut is kept.

**Needs a listener:**
- **The widened celli top (c29).** A side high shelf at 1.5 kHz +4 dB plus a side bell at 170 Hz -2 dB on the celli. Check the exposed celli (bars 85-87 and 171-174) for a hollow or phasey top.
- **The Clarinet 1 attack cuts at bars 104/106 (qn 414/422).** These are c27 `LEVEL_SHAPES_S`, -7.5 dB over the first 0.12 s. They suit the bright state, which this render has. Listen for a dull or late-sounding attack.
- **The Sus Marc LITE strokes at bars 83 and 142.** These are string stroke rows (`STR_STROKE_ROWS`). Check they sound like weighted strokes and not a different section.
- From this cycle: whether the fff tam-tam's longer ring through bars 124-126 reads as the roar of the climax rather than a separate wash, and whether the pp coda now sounds softer than the p passages without getting distant.

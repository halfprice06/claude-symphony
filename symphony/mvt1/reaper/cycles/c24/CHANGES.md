# Cycle 24: changes (actor)

13 of 15 findings were accepted. A #3 (Trumpets a2 track) and C #5 (low-mid EQ test) were deferred. No Opus state changed. All 33 tracks were written with `build_reaper.py build/parts.json jobs --midi-only --tempo`, which included the new tempo map, the basses' ReaEQ and the harp velocities. There was no stem fix after the render.

Level changes were simulated on the c23 stems before the build (`actor_scripts/sim.py`, `meas.py`, `m2.py`). The render was then compared with c23, each on its own tempo map (`actor_scripts/cmp.py`, `cmp2.py`; output in `cmp.txt`).

REAPER steps:
1. Fresh start (`-new`), open the project (33 tracks), `--midi-only --tempo` on all tracks. Tempo markers: 506, no mismatches. Every track stayed midi-only; none was fully rebuilt.
2. Save. The quit job timed out and REAPER was killed after the save.
3. Fresh start, open, `render_cycle.py 24`.
4. Save. The quit job timed out again and REAPER was killed after the save.

Files: `before/` holds the c23 tools and data, `rendered_build/` holds what this render was made from, and `actor_scripts/` holds the scripts used here.

## Code (generic)

- `tools/score_to_parts.py`:
  - `LEVEL_SHAPES_S` {track: [(score qn, [(s, dB), ...])]}: exact level shapes in seconds around a score onset, converted on the real tempo map. Per-note corrections keep their length when the tempo changes.
  - `APEX_SKIP`: a set of arc start qns whose apex beat is not held. The default is defined before the config is read.
- `tools/fit_accents.py` (A #1, step 2; not run this cycle; a dry run on c23 winds worked):
  - `--line-max` (default 5.0). After the iteration, an accent predicted more than this many dB over its next two plain notes has its swell lowered by the excess + 1 dB. Each note is measured on [score onset, min(+0.30 s, next onset)].
  - `--front-pickup-s` (default 0.10). In `--front-s` mode, a pickup's slurred target is measured from score onset + 0.10 s.
  - The wind `--max-total` default goes from 6.0 to 4.5.

## Accepted (all in the render; c23 -> c24 measured on the renders)

| Finding | Change | Measured | Pass? |
|---|---|---|---|
| A #1 | `LEVEL_SHAPES_S` cuts of min(rise, over-next - 3.5) dB over the score onset -0.03..+0.35 s on 12 accents. Clarinet 1 505 was left to B #4 | Over the next two plain notes: Ob1 105 +6.2 -> +3.2; Cl1 151 +6.6 -> +4.7, 273 +6.7 -> +3.8, 105 +6.5 -> +3.4, 521 +4.3 -> +3.1; Bn1 382 +8.6 -> +3.5; Vln II 325/381/525 +7.6/+7.3/+7.0 -> +1.8/+4.1/+2.2; Vla 325 +8.1 -> +4.0; Vc 521/382 +7.6/+4.4 -> +3.5/+2.9. At bar 27, Oboe 1 minus Flute 1 front went +1.5 -> -1.2 | yes |
| A #2 | Bar-142 Marc LITE strokes: c23 step rows raised by the body change (Vln I 566 +5.8, Vln II 566 +3.4, Vln I 564 +1.6, Vln II 564 +1.3), and seconds front shapes from -0.13 to +0.25 s (-8.1 / -6.3 / -1.6 / -1.3) | Front - body: Vln I 566 +10.5 -> +2.8, Vln II 566 +8.3 -> +2.5, Vln I 564 +3.4 -> +1.8, Vln II 564 +4.5 -> +3.2. Bodies -32.3/-32.4 -> -26.8/-29.4 (c22 -26.4/-29.5). Bars 141-142 master -17.69 -> -17.62 | yes |
| A #4 | Refit (`fit_rebows.py 23 --tracks "Violins I"`) simulated: rows changed by under 1 dB, median dip -3.6 -> -3.55. Not kept. Instead a +4 dB fill at re-bow 711.855 (the only real hole; the others are the sample's ±3 dB bow swing) | Stem dips (80 ms) [-1.2 -3.3 -5.7 -3.9 -5.6 -2.6] -> [-1.7 -3.4 -1.8 -3.9 -5.7 -2.4], median -3.6 -> -2.9. Master unchanged | partial |
| A #5 | `LEG_ART_EXTRA_S` Vln II Leg BC +0.03 -> 0.0 | Vln II targets moved +0.06 qn later as planned (parts.json). Joins and crossovers not re-measured | build checked |
| B #1 | Bar 26 shapes (Vln II / violas -3.5, Vln I -1.5 from 100.35; brass -1.5 from 100.3) | Master per half beat 100.5-102.5: -13.4/-13.2/-13.6/-13.8/-13.4 -> -14.3/-14.4/-15.0/-15.0/-14.5, attack -12.0 -> -11.7. Vln I/II/Vla -22.3/-21.7/-23.2 -> -23.8/-25.1/-26.7 (Vln I is the top string again). Delivered S max bar 26 -13.85 -> -14.42 (1.3 under 167-170) | yes |
| B #2 | Basses `bell2` 87 Hz -6 dB 0.25 oct -> 87.3 Hz -10 dB 0.15 oct (ReaEQ read back 87.2 Hz -10.1 bw 0.14) | Bowed notes, 60-100 minus 160-300 Hz (+0.1..+1.2 s): F2 +5.8 -> +2.4; Eb2 +4.9 -> +5.2; E2 +2.8 -> +2.7; G2 +3.3 -> +3.5. Master bar 10 -31.8 -> -31.9 | yes |
| B #3 | Bar 84 celli/basses shapes. (actor) The celli shape is held at -2/-3 to the note's end, plus a -9 dB notch over 335.98-336.2. Reason: the G2 bloomed again at its end, and its note-off played a 0.3 s burst at -25 dB on the stem and master, 7-8 dB over the bar | Celli per quarter, c23: -42 .. -33 (+9) .. -25. c24: -41 .. -38 (+3) .. -33. Master at 336.0 -25 -> -32 | yes |
| B #4 | Clarinet 1: 227 fill removed, -2.5 dB at 226.95-227.1 (back by 227.6); fills at 505 / 507.5 5.5/6.7 -> 2.5/3.5 (`_auto` notes: exclude in refits) | Cl1 227 front minus Vln I 227 front +6.8 -> +3.2. Fronts at 505 / 507.5 -2.3 dB; 505 over its next notes +4.5 -> +1.6 | yes (505 now a little under 2) |
| B #5 | Oboe 1 shapes at 178-182 | Per half beat, c23: -46.2 -40.7 -38.9 -43.3 -43.4 -37.8 -36.3 -35.6. c24: -46.4 -43.3 -41.8 -43.5 -43.7 -41.5 -41.3 -39.7. Peaks 4-5 dB lower | yes |
| C #1 | Horn 1 / celli shapes 193.2-198.2. (actor) 196 raised further than C's values (Horn 6.0/5.5, celli 6.5/6.0) after simulation. Recap celli shape at 595.65-598.1 | Exposition sum: 193.5 -38.0 -> -35.7, 195 -34.4 -> -32.0, 196 -35.8 -> -30.5 (+1.5 over 195, 0.6 under 191/192). Median 193.5-198 -35.7 -> -32.0. Master 196 over 195 +2.0. Recap celli 596 -37.3 -> -33.0 (595.5 -35.2); master 596 over 595 +0.8 -> +1.9 | yes |
| C #2 | Movement-I `HARP_PITCH_VEL` (C's table) | Harp level bars 47-68 -41.09 -> -41.47; 156-166 -41.39 -> -40.54 (both within 1 dB). On my broadband onset-rise measure, p10-p90 17.7 -> 16.9 dB. C's per-pitch harmonic measure not rerun | partial / unverified |
| C #3 | `STR_REP_DETACH` on Double basses 664-676 with +1.5 dB hold. (actor) The on/off steps are -1.2/+1.6 (C proposed 0/0). Reason: 0/0 simulated worse (front on-off +3.25 -> +4.71 dB), because the dips act at the note ends | Stem front on-off +3.25 -> +1.92. Master -0.16 -> -0.35. n vs n-2 0.85 -> 0.90. Bars 167-169 RMS -29.62 -> -29.87 | yes |
| C #4 | `PHRASE_ARCS` + (184,200), (488,504,"sub"), (636,648,"sub"), (664,679,"sub"). `RAMP_SPANS` (244,252,115), (620,628,115). (actor) `APEX_SKIP` {664}: the coda arc's apex hold would have put a 4% held beat (673) in the middle of the ff trumpet theme | Tempo: 185-191 113.7, 196-198 107.5, 199 103.0 (as recap 596-599). 502/503 98/95. 637 96 (apex hold, Violins I top), 646/647 98/95. 677/678 123.5/119.7. Bar 64-65 holds 119.4 (was rising to 119.9), then -1.3% into the rit. at 260. Bars 158-159 hold 120.0. Re-bow points unchanged in qn. Movement +0.87 s. One articulation flip from the tempo change: Vln I/II 259.5 (slurred eighth, 0.25 s) Sus MAX -> Leg Slur target. Clarinet 1/2 at 637 (96 bpm) lost their 0.035 s re-tongue lead | yes (tempo); effect inferred |

## Rejected / deferred
- **A #3 (Trumpets a2 on the 2TP KS Master), deferred.** It is a new 34th instance (about +2 GB on a 45-46 GB render) and a full new track with copied shapes. It needs a cycle of its own, together with a memory check.
- **C #5 (low-mid bells on 12 tracks), deferred.** C advised its own cycle when C #4 is in. Each FX change breaks the stem-sum simulation for the track's other passages.
- **A #4 refit, not kept.** See the table.

## Before / after (c23 -> c24)

| | c23 | c24 |
|---|---|---|
| Master integrated | -16.3 LUFS | -16.3 LUFS |
| Master LRA | 22.5 LU | 22.5 LU |
| Master sample peak | 1.531 | 1.488 (qn 636.04; next 1.435 at 484.53, 1.378 at 640.54) |
| Master true peak | +3.7 dBFS | +3.5 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.5 LU | 14.4 LU |
| p10-to-max span | 18.9 dB | 19.0 dB |
| Delivery limiter | 2.0 dB | 1.8 dB |
| Delivered true peak | -1.6 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.60 / 4.48 | 8.58 / 4.52 |

- Climax order (delivered S max): 160 -10.07 > 122 -10.97 > 167-170 -13.10 > bar 26 -14.42 (c23: bar 26 -13.85).
- Attack probe: 0 flagged.
- Whole-file stem RMS: within 0.2 dB of c23 on every stem.
- REAPER memory: 18 GB with 0 compressed at the render start; 46 GB with 21 GB compressed after the render; 46 GB with 36 GB compressed at the quit.
- Item 7 was not re-measured. Re-bow points did not move. The fills are unchanged except at 711.855.

## Open for c25
- **A #3, Trumpets a2.** Test it with a memory budget.
- **C #5, low-mid EQ test.**
- **Harp.** Rerun C's per-pitch onset measure on c24 and do a second, smaller `HARP_PITCH_VEL` pass.
- **Violins II Leg BC joins and crossovers.** Not re-measured after the 0.0 extra.
- **Violins I re-bow dips.** 722.781 and 724.465 still dip -3.9/-5.7 on 80 ms frames. That is the sample's 3 Hz swing; a fill would follow it.
- **Accent refits.** The c24 `LEVEL_SHAPES_S` accent cuts are part of the envelope. A refit with `fit_accents.py --front-s 0.18 --line-max 5` should run before those cuts are removed. Skip Vln I/II 564/566 (hand values) and Clarinet 1 505/507.5/227 (`--exclude` in `auto_fills.py`).
- **Bars 64-65.** They hold 119.4, not the printed 118.
- **Vln I/II 259.5.** These are now Leg Slur targets; check that join.

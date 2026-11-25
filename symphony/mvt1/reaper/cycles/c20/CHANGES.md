# Cycle 20: changes (actor)

This cycle reverted the two failed c19 tests, ran one new articulation test (the 1st Violins "Slur Runs" row), changed two timing rules and made level and EQ changes.

REAPER steps:
1. Fresh start, project opened (33 tracks).
2. `build_reaper.py build/parts.json jobs --midi-only` on Horn 1, Horn 2, Violins I, Violins II, Violas, Violoncellos, Double basses and Horns a2. Violins I was fully rebuilt (Slur Runs row loaded) and so were the Violas (Stac On Bow row unloaded).
3. Save, quit, fresh start, open, render.
4. Two level-only stem fixes after the render (`stem_fix.py 20 cycles/c20/rendered_build build --apply` on 4 stems, then `stem_fix.py 20 <fix-1 parts/mix> build --apply "Violins I"`). The originals are in `cycles/c20/render_first/`.
5. `render_cycle.py 20 --measure-only`, then `build_reaper.py --mix-only` on Violins I, Violins II, Violas and Double basses. Save, quit. The quit job timed out at 60 s and REAPER had exited.

Files:
- `cycles/c20/before/`: the c19 tools and data.
- `cycles/c20/rendered_build/`: the data and code the render was made from.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c20-actor/`. It holds `pdiff.py` (parts.json diff), `A/` (critic A's scripts run on c20: `runs2.py`, `run606s.py`, `heads2c.py`, `accshape.py`, `pkr3.py`, plus `barrms.py`, `lvcmp.py`, `nb.py`, `cbfront.py`) and `C/lowc.py`.

## Code (tools/score_to_parts.py, generic)

- `LEG_ROWS_EXTRA = ("Slur Runs",)` and `_lg(art)`. Every legato test in the module that used `"Leg" in art` (20 places) now goes through `_lg()`. A row without "Leg" in its name can therefore play as monophonic legato: overlaps, legato targets, the keyswitch guard and the bow-change pass.
- `STACLEG_SPANS` entries can be `(a, b, art)`, so a span can name its own row.
  - A span with its own row keeps the fast_leg velocities: targets FAST_LEG_VEL 127, the first note keeps its own velocity.
  - The span's first note takes the usual entry and re-tongue leads. Before, it was unled. `n["art"] in LEG_ROWS_EXTRA` is now accepted by the entry-lead branch.
  - The span's last note joins a target outside the span as a Leg BC / bow-change target, with LEG_OVERLAP. The output stage then moves its end with the target's lead.
- `SLUR_HEAD_LEAD["lead_s"]`: the slur head's own lead in seconds, at most its target's lead.
- `GROUP_LEAD_AT {track: [(a, b, lead_s)]}`: every note with a score onset in [a, b] moves lead_s earlier together.
  - The notes before b keep their played lengths, and a legato overlap into the led target is moved at the output stage.
  - Notes before the group end at the first moved onset + 0.03 qn.
  - CC11 is held from each moved onset.
  - parts.json key `group_leads`.

## Accepted

### Reverts of the c19 tests (critic A #3)
- `DOWNBOW_STROKE_AT`: removed celli 91/317/539 and Violins I 100/142/154/548. Celli 321 and Violins I 533 stay as strokes.
- The c18 `accent_fits` rows are back (Violins I 100/142/154/548, celli 317), as is the `accent_bodies` row for Violins I 142. All of them were refitted after the render (below).
- The c19 stem-fix body set-backs on celli 91/539 were removed.
- MIDI and keyswitches on these notes match the c18 build, except Violins I 153.643, which is 0.18 qn shorter because of the c19/c20 slur-head lead on 156.
- Front (onset..+0.15 s) minus body (+0.45..+0.75 s), c18 / c19 / c20:

  | Note | c18 | c19 | c20 |
  |---|---|---|---|
  | Vc 91 | -4.9 | -7.6 | -4.9 |
  | Vc 317 | -2.7 | -4.3 | -2.7 |
  | Vc 539 | -3.3 | -5.3 | -3.3 |
  | Vln I 100 | -1.8 | -2.2 | -1.8 |
  | Vln I 142 | -0.4 | -1.3 | -0.1 |
  | Vln I 154 | -3.1 | -4.1 | -3.0 |
  | Vc 321 (kept stroke) | | -0.5 | -1.6 |
  | Vln I 533 (kept stroke) | | -0.2 | -1.1 |

  The reverted notes are back within 0.3 dB of c18, which passes. The kept strokes stayed within 1 dB of c19 (Vc 321 1.1 dB).
- The letter-G violas (c19 A #5) are back on Sus MAX: the ART_SPANS row was removed, the Violas fully rebuilt, and the -3 dB level shape removed.
- PICKUP_LIFT Violoncellos 320.5 +2.5 dB. Pickup minus target body: -6.4 -> -3.8 dB (pass band -6..-2).

### A #1 (test PASSED): Violins I slurred sixteenth runs on the "Slur Runs" row
- The row was read from the patch file: 1st Violins KS Master row 18, key 42. Its regions are the LegSl p/mf/ff transition samples plus "HsScl" / "WsScl" half-step and whole-step scale samples (mp/mf, up and down).
- Spans: `STACLEG_SPANS["Violins I"] = [(127, 128, "Slur Runs"), (158, 160, ...), (270, 272, ...)]`. Run notes are at v127, with a 0.02 qn overlap and no lead.
- Targets:
  - 160 and 272 join from the run as Leg BC targets with the c19 lead, as in c19.
  - 128 (an accented down-bow ff eighth) was a Sus MAX stroke in c19 (STR_ACC_AFTER_SUS after the Sus run). It is now a Leg BC target too. As a listed Sus stroke after the legato row, its lead cut the run's last note to 0.09 qn.
  - 128 measured 2.5 dB under its c19 level, so a +2.5 dB shape from its moved onset was added (stem fix 2). Its 0.5 qn stem RMS is now +1.2 dB over c19 and the master +0.1.
- Own-pitch dominance (share of each note's slot in which its pitch leads) and first dominance from the score onset:

  | Bar | Share c19 | Share c20 | First c19 | First c20 |
  |---|---|---|---|---|
  | 32 | 0.52 / 0.24 / 0.62 (median 0.52) | 0.60 / 0.68 / 0.92 (median 0.68) | +0.082 / +0.117 / +0.092 | +0.072 / +0.062 / +0.047 |
  | 68 | median 0.36 | 0.00 / 0.71 / 0.85 / 0.97 / 0.89 / 0.83 / 0.58 (median 0.83) | median +0.127 s | median +0.047 s |
  | 40 | median 0.08 | median 0.50 | | |

  - Bar 32's first-dominance median of +0.062 s is on the +0.06 limit.
  - In bar 68 the first transition, from the v53 head A-flat4 to C5, still never leads.
- Stem RMS against c19:
  - 127-128: -0.2 dB.
  - 158-160: -1.1 dB. Over the same span the master is -0.8 dB, which includes the B #1 Violins II cut.
  - 270-272: -1.35 dB (pass ±1.5).
- 2-5 kHz in the first 80 ms minus the body on the targets 128/160/272: -3.3 / -5.6 / -8.0 dB (pass ≤ +2).
- Violins II bar 32 (the control, Sus MAX) is unchanged: shares 0.84 / 0.16 / 0.96 / 0.98.
- Memory: the row load was not separately measurable. REAPER was 46 GB after the render (c19 45 GiB).

### A #2 (partial): bar 152 group lead
- `GROUP_LEAD_AT` Violas and Violoncellos (606.5, 607.0, 0.12 s). The run and the F (607) move 0.2274 qn earlier together, and the A (606.0) is cut 0.01 qn before the run's keyswitch.
- F first leads from its score onset: violas +0.17 -> +0.11 s (pass ≤ +0.08), celli +0.29 -> +0.21 s (pass ≤ +0.15). Both moved only 0.06-0.08 s for 0.12 s of lead.
- Run pitches that lead for part of their slot: violas B 0.69, E 1.00 (c19 B 0.46, D 0.46, E 0.71); celli B 0.85, E 1.00 (c19 E 0.86). Two of four in each section, which passes.
- Largest 30 ms dip against the 200 ms before, over 605.8-608: violas 3.3 -> 5.3 dB (a new dip just over the 5 dB limit), celli 6.5 -> 6.0 dB.

### A #4 (pass): SLUR_HEAD_LEAD lead_s 0.10
- Over the 21 Violins I heads, the time the head pitch starts to lead went from a median of -0.062 to +0.013 s (pass -0.02..+0.04).
- Target takeover median +0.303 -> +0.313 s (pass, within 0.02).
- Six heads still start -0.062..-0.077 s early. 152 reads -0.327, as in c19 (-0.147); the measure there picks up the note before.

### B (level only; plain RMS re master, c19 -> c20)
- #1 Violins II tremolo shapes (bars 39-41 -1..-6 dB, bars 80-81 0..-6 dB):
  - 156-160: Violins II -6.9 -> -12.1. Violins I -13.3 -> -13.5, so the tremolo now sits under the melody.
  - 321-324: Violins II -3.9 -> -7.7. Violins I -12.5 -> -10.8, Flute 1 -21.1 -> -19.5.
  - Master bars 39/40/41: -24.3 / -21.8 / -20.5. Bars 80/81/82: -28.4 / -24.8 / -16.2. Each bar is louder than the one before.
- #2 Horns a2 -4 dB over 310.2-313.4:
  - Over 312.5-313.5 the horns go -2.0 -> -3.8, Oboe 1 -12.6 -> -10.6 and Violins I -9.0 -> -7.0.
  - Master bars 77-80: -34.3 / -32.1 / -32.3 / -28.4. Bar 79 sits 0.2 dB under bar 78; the critic simulated a 0.7 dB rise.
- #3 Lento bar 12 (violas -2.5, Violins I +2.5): Violins I minus violas over 44.5-46 went -3.7 -> +0.6 dB. Trombone 1 is unchanged.
- #4 Horn 2 -3 dB at bar 32: -9.0 -> -11.8 re master over 124-126.

### C
- #1 Basses `loud_eq` third spec, an 80 Hz low shelf at -5 dB (the loud spans, not the coda span). Master band level re 250 Hz-2 kHz, loud (top 10%) / soft (bottom 30%):

  | Band | c19 loud / soft | c20 loud / soft |
  |---|---|---|
  | 30-60 Hz | -26.2 / -27.7 | -29.9 / -27.7 |
  | 60-100 Hz | -13.4 / -11.3 | -14.5 / -11.3 |
  | 100-250 Hz | -7.5 / -5.1 | -7.7 / -5.1 |

  - Loud frames now carry less sub-bass than soft frames (pass: 2.2 and 3.2 dB under, against the 2 and 3 dB targets).
  - 100-250 Hz moved -0.2 dB and loud-frame level -0.08 dB.
- #2 Coda basses steps on the attacks (stem-fixed to -0.8 / +1.2 dB, with a period-6 irregularity of ±0.6). 40-300 Hz in the first 100 ms of each eighth (my measure, which reads lower than the critic's), c19 -> c20:
  - Stem on-minus-off: +2.5 -> +0.4 dB.
  - Stem n/n-2 median: 0.09 -> 0.74 dB. Pairs within 0.3 dB: 86% -> 14%.
  - Master on-minus-off: +1.6 -> +0.8 dB.
  - Bars 167-169 basses RMS: +0.5 dB.
  - The first values, -1.0 / +2.5, rendered on-minus-off at -1.1 with RMS +1.3 dB.
- #3 Violas bars 107-110: the 429 trim went 5 -> 1.5 -> 3.0 (the stem fix raised it again), the fill 5 -> 2.5 dB, and the role became [424, 437.5, 1.5].
  - Bodies 428 / 429 / 431 / 432 / 434 / 436 (dB): c19 -34.0 / -33.5 / -42.9 / -46.0 / -44.8 / -39.9; c20 -37.0 / -38.0 / -42.8 / -44.5 / -43.3 / -39.8.
  - The tenuto bump is gone and 436 is the line's top after 428/429. Flute 1 stays over the violas from 432.
- #4 Bars 51-52 Horn 1 +3.5 / celli +2.5 over 204.3-205.6:
  - Master fall from the 203 peak: 9.9 -> 4.8 dB (pass ≤ 7).
  - Horn 1 stem fall to its minimum: 15.5 -> 12.0 dB, a mean of 8.6 dB under the peak (target 6).

### Accent refit after the render (strings; critic A #3)
- `fit_accents.py 20 cycles/c20/rendered_build/parts.json --family string --keep-long-qn 1.4 --pickup-over 2.5 --skip` Violins I 62/65/82/533, Violas 536, celli 536/321 `--write`.
- 73 of 133 predicted in 2-4 dB (median +3.05). 2 have 2-5 kHz over +3 dB.
- `fit_accent_bodies.py ... --max-cut 3 --write`: 18 accents, front-body median -1.29 -> +1.17 predicted.
- Applied by stem fix (Violins I, Violins II, Violas, Double basses, together with C #2/#3).

## Rejected or deferred
- C #5 (hall fx volume 0.19 -> 0.16): deferred. It needs a full rebuild of every track and refits of every fill and re-bow shape, so it should have a cycle to itself.
- B #5 / C smaller items: no change, as proposed.
- A #2 F velocity max(vel, SOST_VEL): not needed, the F is already v124.

## Before / after (c19 -> c20, after stem fixes)

| Measure | c19 | c20 |
|---|---|---|
| Master integrated (float stem sum) | -16.3 LUFS | -16.4 LUFS |
| Master LRA | 22.5 LU | 22.5 LU |
| Master sample peak | 1.523 | 1.480 |
| Master true peak | +3.7 dBFS | +3.4 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 19.0 dB | 18.9 dB |
| Delivery limiter | 1.8 dB | 1.7 dB |
| Delivered true peak | -1.7 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.57 / 4.50 dB | 8.62 / 4.47 dB |

- Climax order (delivered S max): 160 -10.10 > 122 -11.50 > 167-170 -13.10 (c19 -10.10 / -11.60 / -13.20).
- Attack probe: 0 flagged.
- REAPER memory: 26 GB with 0 compressed at the render start; 46 GB with 33 GB compressed after it.
- Delivered mp3: `cycles/c20/mvt1-mockup-c20.mp3`.

## Open for c21
- A #2: the F at 607 still leads only at +0.11 (violas) and +0.21 s (celli), and the violas have a new 5.3 dB dip in 606-608.
- Bar 68: the first run transition (A-flat4 -> C5 from the v53 head) never leads.
- Violins I 128 is now a Leg BC target with +2.5 dB, so its front is a legato arrival, not a fresh stroke.
- Six slur heads are still 0.06-0.08 s early.
- Bar 79 is 0.2 dB under bar 78.
- Horn 1's bar 52 is still 8.6 dB under its 203 peak (mean).

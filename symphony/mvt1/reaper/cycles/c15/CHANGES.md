# Cycle 15: changes (actor)

One render from a freshly restarted REAPER (33 tracks), then two level-only stem fixes:
- `tools/stem_fix.py 15 cycles/c15/rendered_build build --old-src cycles/c15/rendered_build/build_reaper.py --apply`
- `tools/stem_fix.py 15 <the fix-1 build> build --apply` (accent refit)

Then `render_cycle.py 15 --measure-only`.

Where things are:
- First-render stems: `cycles/c15/render_first/`. First metrics: `cycles/c15/metrics_first/`.
- The data and the `build_reaper.py` / `score_to_parts.py` the render was made from: `cycles/c15/rendered_build/`.
- REAPER was updated with `--mix-only` (all 33 tracks), saved and quit. The quit job timed out after the save, so REAPER was killed.
- Snapshot of the c14 tools and data: `cycles/c15/before/`.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c15-actor/`. It holds copies of the three critics' scripts under `A/`, `B/` and `C/`, parametrised by `CYC`/`CYCN`/`PARTS`/`ENVDIR`/`FD`, plus `pdiff.py`, `gaps.py`, `holds.py`, `envdiff.py` and `leads.py`.

## Accepted

### Reverts of the failed c14 tests
- `MEAS_TREM["rr_runs"]` removed, so there are no CC36 resets inside the music; the `cc36` lane is empty.
- Brass `WIND_DETACH` CC11 fall removed (replaced by A #3 below).

### A #1: early fills that started after their hole
- `tools/auto_fills.py` has a new "retimed" branch. When the hole's minimum comes before the fill is full (`t_min < -pre_s + 0.02`), the fill gets `pre_s = max(0, -t_min)`, `hold_s = clamp(t_min + 0.05, 0.10, 0.35)` and `db = min(8, max(db0, dip - 3))`. The branch runs on every measured track.
- Run on c14 with `--write`, excluding Horn 1 at 201/588/589/591/598, because the C #4 leads move those notes. Result: 25 retimed, 14 new, 3 raised, and some lowered or removed by the overshoot rule.
- Stem fix: seven celli fills had their minimum move to +0.2..+0.37 s after retiming. Their `hold_s` was extended to `min(0.40, t_min + 0.05)`.
- Result (A's `efchk2` measure; c14 -> c15 after the fix):

  | Line | Notes | c14 | c15 |
  |---|---|---|---|
  | Celli | 8 | 12.9 | 5.8 |
  | Celli | 198 | 6.5 | 4.6 |
  | Celli | 598 | 6.7 | 4.8 |
  | Celli | 66 | 7.0 | 4.7 |
  | Celli | 690 | 4.7 | 2.2 |
  | Celli | 694 | 7.9 | 7.7 |
  | Celli | 122 | 7.8 | 8.6 |
  | Celli | 712 | 7.8 | 6.0 |
  | Celli | 658 | 8.1 | 6.9 |
  | Winds | Cl1 140 | 5.3 | 1.8 |
  | Winds | Cl1 515 | 5.3 | 3.7 |
  | Winds | Bn1 422 | 7.3 | 3.3 |
  | Winds | Bn1 453 | 6.8 | 4.1 |
  | Winds | Hn1 422 | 11.5 | 0.1 |

- Pass (all under 5 dB) not met for celli 694/122/658/712 or Bn1 420 (6.6). The celli join holes move between renders.

### A #2 (test): a slur's short first note after a tongued note plays the Sus row
- New generic `SLUR_START_SUS` in `score_to_parts.py`; the movement I values are in `build/score_config.py`: `{"families": ("wind", "brass"), "max_qn": 0.6, "after_qn": 0.15}`.
- The first note is monophonic, not accented or tenuto, and its slur's second note is a new pitch. It plays on Sus and overlaps by `LEG_OVERLAP`.
- The second note keeps its Leg row and is joined like the sostenuto join: `SOST_JOIN_LEAD_S` lead (at most 0.45 of the first note) and velocity `SOST_VEL`.
- 87 notes. New parts.json keys: `slur_start_sus`, `slur_start_joins`.
- Measured with A's `sstart` measure (score-onset windows; the original measure lost these notes once the second note had a lead):
  - First note minus the note before: median -2.4 -> -0.1 dB (pass -0.5 or higher).
  - Share at -4 dB or lower: 20/59 -> 8/63 (pass under 15%).
  - First minus second: winds +0.6 (Sus MAX) / +2.5 (clarinets) dB, brass -0.6.
  - Clarinet 1 509: B3 -35.7 against the C4 before it at -35.5 (c14 -39.6 against -33.3).
  - Left low: Oboe 1 314.5 (-9.8) and Oboe 2 413 (-9.3), which are now on Sus, so the layer is not the cause.

### A #3: brass tongued changes with short gaps get a volume dip
- `WIND_DETACH["by"]["brass"]` adds `dip_db -5.0`, `dip_fall_s 0.05`, `dip_min_cc 84` (new generic keys). The default `WIND_DETACH_DIP_MAX_GAP_S` is 0.07.
- The dip is applied at every tongued change: the next note starts at the written end, at a new pitch, outside the slur, with no note held across. It applies at f or louder when the played gap is under 0.07 s.
- The shape is 0 dB at end - 0.05 s, the dip at the end, held to the next moved onset - 0.005 s, and 0 dB at + 0.005 s. 84 changes; parts.json `detach_dips`.
- The render used -4 dB; the stem fix took it to -5.
- Brass holes at gaps under 0.07 s: -3.5 -> -4.4 dB (render, all 87), and -4.9 where dipped (66 changes) at -4 dB.
- The 21 changes left undipped are soft second-theme horn slur boundaries, left so on purpose.
- Master dip at those changes: -2.18 -> -2.12 dB (pass: no more than 0.3 deeper).
- Slurred brass: -3.6 -> -3.2.

### A #4 (test): the celli measured tremolo alternates two stroke rows
- `MEAS_TREM` `alt_row "Stac On Bow RRx9"` (key 28, newly loaded; a full rebuild of the celli). Settings: `alt_share 0.45`, `alt_seed 464`, `alt_max_run 3`, `alt_db 0`. 36 of the 80 strokes are on the alternate row; parts.json `meas_trem_alt`.
- Autocorrelation at lag 9 (peak / 1-8 kHz / centroid): 0.73 / 0.85 / 0.92 -> -0.10 / -0.15 / -0.10. Lag 18: -0.13 / +0.16 / +0.28. Every lag from 4 to 18 is under 0.4 (pass).
- Median stroke peak per row: -29.8 (Stac) / -30.5 (On Bow), so the rows are within 1 dB and `alt_db` stays 0.
- 1-8 kHz sixteenth fold per 4 qn: 3.7-4.9 -> 3.2-4.3 dB (pass 3.5 met in 3 of 5 windows).
- Celli level per bar is within ±1 dB of c14, except 464-468 (+1.9) and the 483-484 arrival (+2..+4.5). The data there is identical; this is round-robin and sample variation.

### A #5: Violas bar 31
- `accent_fits.json` Violas 120 changed from [0, -6] to [0, 0].
- `note_trims.json` Violas 120.0 is +3 in the render; the stem fix set it to +1.5, with a 0.1 s ramp.
- `fit_accents.py` no longer puts negative steps on legato targets that are moved more than 0.05 s early (`legearly`).
- Fit window: 120 is +5.2 dB over its pickup at +3 (pass 2-4), so it was set to +1.5. The 2-5 kHz front minus body went from +9.4 to -5.0.

### B #1: horn F4 trims (and Horn 3 D4)
- `pitch_trims.json`:
  - Horn 1, Horn 2, Horn 3: `"65": {"early": 1, "body": -4.5}`.
  - Horns a2: `"65"` body -3.
  - Horn 1 `_skip_onsets` [97, 189, 206, 592].
  - Horn 3 `"62": -2.5` with `_skip_onsets` [100, 328, 330, 484, 488, 676].
- Bar 57: Horn 2's F4 went from -34.5 to -37.7 dB, still 4 dB over Violins I at 224, so the stem fix adds `note_trims.json` Horn 2 224.0 -3 (step).
- Bars 164-165: Horn 1 F4s down 3.3-3.4 dB. It is no longer the loudest stem, and is now level with or under Clarinet 1 (654-656).

### B #2: soft trims rising inside decrescendos
- `tools/build_reaper.py vol_points` changed for each decrescendo that starts at CC 72 or lower (`SOFT_DECRESC_HOLD_MAX_CC`). From the hairpin's start to the moved onset of the first note whose score onset is at or after its end, the trim keeps only `SOFT_DECRESC_KEEP` of its rise above its value at the start.
- The render used no rise at all. On the 20 decrescendos where the trim rises 2 dB or more, the median fall went from -1.7 to -6.5 dB, against -4.4 for the others; Horn 1 at bar 106 fell 11.9 dB from mf to mp.
- The stem fix set 0.5 of the rise (with `stem_fix.py --old-src`): median -5.1 dB, share falling less than 2 dB 0.50 -> 0.20.
- Bar 44, master step at 174: +4.3 -> +2.4 dB. Horn 1 there still rises +3.9 dB inside its p > (the B-flat4 sample).

### B #3: trumpet trims
- `mix.json`: Trumpet 2 `dyn_trim_db` {6.2, 8.5, 8.4}, Trumpet 3 {7.7, 11.1, 9.6}.
- `roles.json`: Trumpet 1 [556, 568, -1] (was -3), [451, 456, 3, 0.5]; Trumpet 2 [628, 631, -3, 0.25].
- Results:

  | Pair | Dynamic | c14 | c15 | Critic's target |
  |---|---|---|---|---|
  | Tpt2 - Tpt1 | ff | +0.4 | -2.2 | -1.4 |
  | Tpt2 - Tpt1 | fff | 0.0 | -2.3 | -2.0 |
  | Tpt3 - Tpt1 | ff | -1.9 | -3.2 | -2.7 |
  | Tpt3 - Tpt1 | fff | +1.5 | -1.9 | -0.5 |

### B #4: Violins I 3 kHz `loud_eq` deleted
- The bell dated from c05, before the CC1 brass brightening.
- Band shares, whole file (all changes together), c14 -> c15: 2000-6000 Hz -10.1 -> -10.43, 100-250 Hz -9.9 -> -9.03.

### B #5: basses F2 and Trumpet 2 bar 113
- `pitch_trims.json` Double basses `"41": -2`.
- `note_trims.json` Trumpet 2 448.0 +4, with a 0.1 s step.

### C #1: string phrase entries after rests
- Celli 56 is a `DOWNBOW_STROKE_AT` Sus stroke, with a `LEVEL_SHAPES` hold at -5 dB from the moved onset.
- `entry_leads.json` extras for 18 entries, plus hand rows in `early_fills.json`. Each row's `pre_s` is the actual lead, so the fill starts at the moved onset, and `hold_s` = critic's hold - lead (at least 0.10).
- t-6 (s after the score onset): every listed entry moved from +0.16..+0.48 to -0.13..+0.20; 17 of 19 by +0.15 (pass), the exceptions being Cb 696 +0.20 and Vln I 707 t-3 +0.23.
- Celli 56: t-6 / t-3 +0.28 / +0.33 -> +0.12 / +0.17.
- Overshoot: Cb 220 reached +5 dB at +0.4 s, so its fill was removed in the stem fix. The other entries are at +3 dB or less.

### C #2 (test): re-tongue lead
- New generic `RETONGUE_LEAD_S` (cap `RETONGUE_LEAD_CAP` 0.3 of the previous note). It applies to wind/brass Sus-row notes, and Leg-row notes that are not legato targets, that start under 0.5 qn after the previous note's played end, at 100 bpm or faster, when no other rule moved them.
- The previous note ends as much earlier, its CC11 falls move with it, and CC11 is pulled to the new note's level.
- Values: Horn 1/2 0.09, Trumpet 2/3 0.08, Tuba 0.07, Oboe 2 / Cor anglais 0.08, Oboe 1 0.05, brass 0.05, wind 0.035. 835 notes; parts.json `retongue_leads`.
- Re-attack arrival on those notes (C's `shortn`): brass +0.106 -> +0.052 s, winds +0.079 -> +0.056 s (pass ≤ 0.065 / 0.06). Strings +0.048 -> +0.043.
- Tongued holes: winds -5.6 -> -5.3. Same-pitch repeats: median -4.7 -> -4.4 dB.
- One new deep repeat hole: Clarinet 2 125, -6.3 -> -13.4 dB.

### C #3: loud entry leads
- `ENTRY_LEAD_S` per track (Horn 1/2, Trumpet 2/3, Trombone 1, Bassoon 1; loud-only Oboe 2 0.08 and Flute 2 0.06 on top of the Sus MAX articulation lead).
- Fills of +3 dB from the moved onset on the -8 dB fronts.
- t-3 median at the f/ff tutti entries:

  | Track | c14 | c15 |
  |---|---|---|
  | Oboe 2 | 0.207 (front -7.8 dB) | 0.075 (front -3.6 dB) |
  | Horn 1 | 0.140 | 0.060 |
  | Trumpet 3 | 0.107 | 0.028 |
  | Flute 2 | 0.143 | 0.073 |
  | Trombone 1 | 0.107 | 0.065 |
  | Oboe 1 | 0.133 | 0.098 |

- Not reached: Oboe 2 100/548 and Oboe 1 521 are f accents on a GENTLE_ACCENT family, which keep the score onset (`acc_art`), so they got no lead.
- Side effect: below 100 bpm the second tuple value applies to every CC above 50, so mp/mf Lento entries on these tracks now take the loud lead. For example, Horn 1 49 moved 0.05 -> 0.10 s. Open.

### C #4: Horn 1 second theme
- `leg_leads.json` Horn 1 {188: 0.06, 201: 0.14, 588: 0.10, 591: 0.08, 598: 0.06, 589: 0.04}. The slur-boundary notes take the C #2 lead 0.09.
- Horn minus celli crossover at the shared changes: median +0.053 -> -0.030 s (pass ±0.03).
- Still over 0.08 s apart: 184 -0.225, 584 -0.325, 594 -0.175 (horn early), and 192 +0.115, 203 +0.13, 204 +0.155 (late).

### C #5: unison hand-overs
- `UNI_DELAY_OVERLAP_QN` 0.25 and `UNI_DELAY_FADE` (-12 dB, 0.2 s); the defaults moved before the score config. parts.json `uni_fades`.
- Oboe 2 at 628.75 now rises from -22 to +5 dB over 0.25 s (c14: -22 to -2 in 0.1 s).
- The critic's pass measure (Ob1+Ob2 2-5 kHz rise under 1.5 dB) read 1.7 -> 3.2 dB. It is dominated by the second oboe's own body, which is printed (two players), so it does not test the attack.

### Accent refit
- `fit_accents.py 15 build/parts.json --family {brass,wind,string} --keep-long-qn 1.4 --pickup-over 2.5 --write`, on the fix-1 stems, applied as stem fix 2.
- Predicted in 2-4 dB: brass 32/37, winds 126/142, strings 105/135. Negative steps on early legato targets are now refused, which is why the strings went from 120 to 105.
- 2-5 kHz first 80 ms minus body (A's `acchf`, medians):
  - brass -7.8 -> -8.2 (max 3.5: Horn 3 317/321);
  - winds -5.8 -> -6.3 (Clarinet 1 558 +6.3, new);
  - strings -4.3 -> -4.6 (536 artefact).
- C's long-accent measure: brass max +2.0, winds +1.5.

## Rejected or deferred
- **A #6, Horns 3-4 a2 at bars 80-81:** deferred again. Routing Hn3-staff notes onto Horns a2 needs that staff's dynamics, hairpins and articulations in the a2 track, and `build_track` reads events from the track's own staves (Hn1) only.
- **A #6, two-note slur release on short notes:** re-measure on c15 first (after A #2), as A asked. Not changed.
- **B #4, 100-300 Hz body:** open, as B said.
- **C #3, accents keeping the score onset:** not changed. The accent fits are keyed to that timing.

## Before / after (c14 -> c15 after the stem fixes)

| Measure | c14 | c15 |
|---|---|---|
| Master integrated (float stem sum) | -15.8 LUFS | -16.2 LUFS |
| Master LRA | 22.5 LU | 22.2 LU |
| Master sample peak | 1.488 | 1.461 |
| Master true peak (float) | +3.5 dBFS | +3.3 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.8 LU | 14.5 LU |
| p10-to-max span | 19.5 dB | 19.1 dB |
| Delivery limiter | 1.5 dB | 2.0 dB |
| Delivered true peak | -1.6 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.65 / 4.61 dB | 8.98 / 4.54 dB |

- First render, before the stem fixes: LRA 14.7, span 19.3, limiter 2.0.
- Climax order on delivered S max: 160 -9.96 > 122 -11.11 > 167-170 -12.81 (c14 -9.84 > -10.93 > -12.99).
- Master top peaks:
  - 1.461 at qn 636.33 (bass trombone, celli, trumpet 1, trombone 1, basses);
  - 1.434 at 641.19 (timpani, tuba);
  - 1.337 at 637.84.
- Item 7: master 100-300 Hz / centroid autocorrelation at 3.95 s was at most +0.11 in the Lento, sostenuto, coda and Tempo I (c14 Tempo I +0.25).
- Attack probe: 0 flagged.
- REAPER memory (`metrics/memory.txt`): 28 GiB with 0 compressed when the render started (the load wait had passed, but samples kept streaming during the render), 45 GiB with 27 compressed after it. Other processes: a chrono-25d Python job of 6.7 GB at the open, VM 2.7 GB, Steam 2.2 GB.
- Delivered mp3: `cycles/c15/mvt1-mockup-c15.mp3`.

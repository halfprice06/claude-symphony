# Cycle 25: changes (actor)

The ONE_TIME tasks were done first. Of the 14 critic findings, 12 were accepted (A #1 and A #2 partly), one was a test that passed for the woodwinds only (C #1), and A #4 was deferred.

The render was made with 8 tracks fully rebuilt for the C #1 width test (Horn 1-4, Trumpet 1, Cor anglais, Oboe 1, Clarinet 1). The other 25 tracks were written with `--midi-only`. The tempo map did not change. After the render, two level-only stem fixes were applied:
1. The brass accent refit, the Oboe 1 fills, and the breath-split shapes on Bass clarinet / Horn 4 (11 stems).
2. Two Oboe 1 hole fills.

Both fixes went into REAPER with `--mix-only`, each time from a fresh start, and were saved.

Files:
- `before/` holds the c24 tools and data.
- `rendered_build/` holds what the render was made from.
- `render_first/` holds the 12 stems and the master as rendered.
- `actor_scripts/` holds the scripts: `loopscan.py`, `masteracf.py`, `sim.py`, `meas.py`, `chainfit.py`, `post.py`, `xover.py`, `stereo.py`, `levcmp.py`, `peaks.py`, `smax.py`, `pdiff.py`.
- Measurement output is in `loopscan_c24.txt`, `loopscan_c25.txt`, `stereo_c24.txt`, `stereo_c25.txt`, `levcmp_c24_c25.txt` and `actor_scripts/post_final.txt`.

REAPER steps:
1. Fresh start, open (33 tracks), `build_reaper.py build/parts.json jobs --midi-only` on all tracks. The 8 width tracks reported "Opus state changed" and were fully rebuilt.
2. Save. Quit timed out, so REAPER was killed after the save.
3. Fresh start, open, `render_cycle.py 25`.
4. Save and quit (the quit was killed after the save).
5. Fresh start, open, `--mix-only` on the 11 stem-fixed tracks, save, quit.
6. Fresh start, open, `--mix-only "Oboe 1"` (second fix), save, quit.

## ONE_TIME

**#1, loop pulse on the c24 render.** Measured with `actor_scripts/loopscan.py`; the full lists are in `loopscan_c24.txt` and `loopscan_c25.txt`.
- Method:
  - Every held pitch span of 6 s or more was measured, with re-bow, re-strike and breath-split pieces merged.
  - Each span was measured on its stem from start + 0.5 s to end - 0.3 s, in 20 ms frames.
  - Two features were detrended: the 100-300 Hz band level and the spectral centroid.
  - Each feature's autocorrelation was taken at 3.95 s, and the largest value at lags 2.5-5.0 s was also recorded.
- Strings: every section's spans are split by re-bows into pieces of at most 4.3 s.
  - Every string value at 3.95 s was under 0.4.
  - One exception, celli at qn 11 (0.69 / 0.53), is a 5.5 s window. A 3.95 s lag leaves only 1.35 s of overlap there, and the pieces are 2.6 s, so no piece is longer than the loop.
- Timpani rolls: all re-struck, all under 0.4.
- Winds and brass: the single-sample notes at 0.4 or above were:
  - Bass clarinet 11 (centroid 0.72 at 3.95 s, -6.6 dB re master, in the Lento);
  - Bass clarinet 464 (band 0.64);
  - Horn 4 289 (0.44 / 0.34, pp, -10.0 dB re master);
  - Bassoon 2 476 (0.72 / 0.83 at its own lag, 4.7-4.9 s).
- Left alone, because they read under 0.4 at 3.95 s and their windows are too short for any other lag: Bass clarinet 480, Contrabassoon 484, Trombone 1 716 and Tuba 488 (all 6.0-6.7 s, at -10 to -19 dB re master).
- Fix: `BREATH_SPLIT_AT` (existing rule, dip -1.5 dB) at irregular points, giving pieces of 2.1-3.1 s:
  - Bass clarinet 11: [13.5]; Bass clarinet 464: [469.5, 474.5];
  - Horn 4 289: [295.0, 299.5];
  - Bassoon 2 476: [481.5, 487.0, 491.0].
- c25 result (band / centroid at 3.95 s):

  | Note | c24 | c25 |
  |---|---|---|
  | Bass clarinet 11 | 0.21 / 0.72 | 0.01 / 0.20 |
  | Bass clarinet 464 | 0.64 / 0.39 | -0.03 / 0.23 |
  | Horn 4 289 | 0.44 / 0.34 | 0.01 / -0.26 |
  | Bassoon 2 476 (best lag) | 0.72 / 0.83 | 0.20 / 0.20 |

- The split pieces re-enter at their own sample level. Fixed in stem fix 1 (`LEVEL_SHAPES_S`):
  - Bass clarinet 13.5: the second piece swelled +2.7 dB. Now flat within 0.5 dB (-48.4 dB, as c24).
  - Horn 4 295/299.5: a +3.5 dB bloom and then a 4 dB hole at the re-entry. Now within 2 dB.
- Stem dips at the re-entries are 3-5 dB in 80 ms frames. Master dips there are 1-3.7 dB.
- Master values at 3.95 s:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento bars 5-12 | -0.08 | -0.17 |
  | Final chord bars 179-182 | -0.39 | -0.08 |
  | Bars 175-178 | -0.11 | +0.08 |
  | Bars 160-164 | -0.50 | -0.17 |

- The whole Lento (bars 1-14) reads +0.39. That window holds rests and phrase-level dynamics, and its autocorrelation falls steadily from 0.57 at 2.5 s to 0.31 at 4.8 s, with no peak at the loop period. Sub-windows (bars 1-4, 4-7, 8-11) are all negative, so this is not a loop.

**#2, the c24 tempo side effects.** Both are fixed with two new generic options in `score_to_parts.py`:
- `SHORT_SUS_AT` {track: [score qn]}: listed slurred, monophonic notes take the short_sus path (Sus MAX) whatever their length on the shaped map. Set for Violins I/II 259.5.
  - Both notes are back to their c23 MIDI: Violins I 259.5, v83, 0.202 qn; Violins II 259.301, 0.364 qn.
  - Critic A had measured the c24 Leg Slur version as acceptable (Violins I dip -11.5 -> -8.5 dB). The ONE_TIME asked for the unintended flip to be undone.
- `GATE_BPM_PRE_ARC` (default True) with `gate_bpm()`: every tempo-gated rule reads the map before phrase arcs and pushes, i.e. the printed tempi plus rit. ramps. The rules are the re-tongue and entry-mid leads, REP_SPLIT, WIND_REP_RETONGUE_SHORT, STR_REST_SHORT and SYNCO_SHAPE.
  - The only notes that changed in parts.json are Clarinets 1/2 at 637: 637.000 -> 636.942, the c23 value.
  - Clarinet 1 now reaches its 0.3 s peak - 3 dB at +0.01 s (c24 +0.04).

## Accepted

| Finding | Change | Measured (c24 -> c25 render, after the stem fixes) | Pass? |
|---|---|---|---|
| A #1 hemiola accents | Swells fitted by simulation on c24 (`chainfit.py`, target +3 dB step, cap 4.5, chain notes only: a note sounds up to the onset) in `accent_fits.json`: Clarinet 1/2, Bassoon 1, Violoncellos at 91-545. Plain swells, no step trims (A's 0.5 dB steps ramp in over 0.6 s and ate the next accent's step). The `--chain` tool mode was not built. | Stem steps: Cl1 539 -0.3 -> +3.0, 542 +0.4 -> +1.6; Cl2 all +2.3..+3.0; Bn1 +1.8..+4.3; Vc 91/539/545 +2.8..+3.0. Under target: Cl1 91 +1.1, 94 +1.5 (swell cap); Vc 94 +0.0, 542 +1.3 (the c19 -4.5 dB cut on Vc 91.3-93.95 ramps out inside 94's before-window). Master: 539 -0.3 -> +0.3, 542 +0.5 -> +0.8, 94 +1.2 (target +1.5..+2.5: horns, violas and basses carry these beats). Bars 22-25 / 134-138 still rise to bar 25 / 138 | partial |
| A #2 brass accent timing (test) | `GENTLE_ACCENT["brass"]` swell_s (0.04, 0.25, 0.6) -> (0.03, 0.15, 0.40), swell_s_leg (0.03, 0.22, 0.50). Brass refit after the render: `fit_accents.py 25 --family brass --front-s 0.18 --line-max 5 --keep-long-qn 1.4 --pickup-over 2.5`. Skips: Tbn1 521/529, every brass qn 100 (the line guard zeroed the bar-26 ff chord accent against the softer bars after it), Tuba 548. Horn 3 317/321 kept at c24 (the refit drove them to the -6 dB cap). 22 entries changed | Peak time median 0.22 -> 0.20 s; peaking after 0.2 s 57 -> 40%; front - mid -1.3 -> -0.7 dB (120 accents). Refit predicted 20/32 in 2-4 dB over neighbours (front window; the render had 0/32), hf > 3 dB: 0. A's targets (0.15 s, 30%, >= 0 dB) not reached: the Sus MAX attack sets the peak time | partial |
| A #3 Oboe falling whole steps | `LEG_PAIR_EXTRA_S["Oboe 1"]` (76,74) 0.12, (74,72) 0.10; fills 498 5.8 -> 3.8, 582 retimed (pre 0.07, hold 0.35); exact fills at 90 / 538 (stem fix 2: the earlier transition sag now fell on the beat, 7-8 dB) | Crossovers 90 +0.215 -> +0.055, 115.5 +0.16 -> +0.075, 397.5 +0.14 -> -0.055, 498 +0.235 -> +0.135, 538 +0.23 -> +0.115, 555.5 +0.165 -> +0.08, 582 +0.26 -> +0.045 s. Holes (60 ms) 582 5 -> 4.5 dB; 90 / 538 4 / 3 dB after the fills | mostly (498/538 still +0.12-0.14) |
| B #1 bass trombone | `dyn_trim_db` f/ff/fff 3.9/6.3/4.7 -> 1.4/3.3/2.2 | Btbn re master: bar 97 -9.1 -> -11.8, 143 -11.2 -> -14.0, 133-134 -13.3 -> -16.0, 160-161 -11.6 -> -14.1, 169-170 -12.0 -> -14.9, 72-73 -12.2 -> -14.9. Master -0.1..-0.35 dB in those bars | yes |
| B #2 letter K | `DOWNBOW_STROKE_AT["Violins I"]` += 628 (a Sus MAX stroke v105, the 627.5 eighth now a led Leg target), Violins II 628 front -2.5 dB (`LEVEL_SHAPES_S`) | Re master per 0.25 qn at 628.0/628.25/628.5: Vln I -13.5/-15.9/-13.6 -> -10.6/-8.7/-10.0; Vln II -7.0/-6.2/-6.0 -> -11.4/-8.3/-9.1. Vln I now level with or over Vln II (expected about -7 not reached) | yes |
| B #3 recap winds over the theme | Flute 1 552.5 pickup lift 8 -> 4; -3 dB Flute 1 553-557.2; -2.5 dB Oboe 1 542-547.8 | Oboe 1 - Vln I +0.6/-0.2/+0.9/+2.3/+0.7/+0.6 -> -2.0/-2.3/-1.6/-0.5/-1.9/-1.4 (exposition -2.4..+0.8). Flute 1 552.5 +5.5 -> +1.6, then -3.9..+0.5 (target -2.7..+1.1, two notes 1 dB under) | yes |
| B #4 Horn 4 in ff chords | `dyn_trim_db` 1.0/1.5/0.5 -> 2.5/4.0/2.0 | Hn1 - Hn4 at 120/122/460/556/560: 10.1/10.7/8.0/10.1/9.8 -> 8.7/9.2/6.2/8.7/8.4 (B expected 2.5 dB less; 1.4-1.8 measured) | yes |
| C #1 solo width (test) | `width` 0.05 and seats on Horn 1-4, Trumpet 1, Cor anglais, Oboe 1, Clarinet 1 (full rebuilds). Horns a2 not changed | Per-pitch R-L SD at 400-1000 Hz (`stereo.py`, isolated sustains): Cor anglais 4.2 -> 3.0, Oboe 1 6.0 -> 3.7, Clarinet 1 4.7 -> 2.4; 1.25-4 kHz SD 2.5/1.7/2.0 -> 1.6/0.8/0.6. Clarinet 1 bars 51-58 neighbour steps 8.2 / 3.9 -> 1.4 / 0.2 dB. Horn 1-4 2.5/2.0/3.0/3.0 -> 2.5/2.1/3.0/3.0 and Trumpet 1 4.8 -> 4.7: no change (as c21's 0.3 -> 0.15). Master correlation 0.519 -> 0.533; 250 Hz-4 kHz 0.531 -> 0.549, above 4 kHz 0.550 -> 0.559, below 250 Hz 0.504 -> 0.499. Per-dynamic note levels (c09 method, `levcmp.py`) within -0.26..+0.48 dB of c24 on every bin with any notes; medians -0.0..+0.12 dB. No level restore needed | woodwinds yes; brass no (SD 1.5 target not reached anywhere) |
| C #2 crash ring | Crash shape +3.4 dB at 638.0, +5 dB from 638.5 over c09 (C proposed +2.9/+4; that simulated -8.0 dB at +2.0 s) | Crash 4-12.5 kHz minus rest at +1.0/+1.5/+2.0/+2.5 s: -4.5/-7.0/-12.2/-18.7 -> -2.0/-2.5/-7.7/-13.6 | +1.5 s yes, +2.0 s 0.7 dB short |

## Rejected / deferred
- **A #4 (Horn 3 316.5-322.5 onto the Horns a2 track; Trumpets a2 patch), deferred.** Part (a) needs a per-window staff list in `TRACK_WINDOWS` (code). It would also rebuild Horn 3 and Horns a2 in the same cycle as the C #1 horn width test. Part (b) is a 34th instance, which needs its own memory check. Its own cycle.
- **C #1 extension to the other solo tracks, not done.** C asked for it only after the test passed, and on the brass it did not.
- **Delivery limiter 2.2 dB (c24 1.8).** The top master peak, 1.538 at qn 484.53, comes from celli 0.30 + timpani 0.21 + Trumpet 2 + violas + tam-tam. These are the same values as c24, but the narrowed Clarinet 1 (+0.07) and Trumpet 1 (+0.06) now add in phase there; c24 had 1.435. This is within the 3 dB target. No notch was made at the letter-G arrival (do-not-touch region).

## Before / after (c24 -> c25, after the stem fixes)

| | c24 | c25 |
|---|---|---|
| Master integrated | -16.3 LUFS | -16.4 LUFS |
| Master LRA | 22.5 LU | 22.5 LU |
| Master sample peak | 1.488 (qn 636.03) | 1.538 (qn 484.53; next 1.450 at 637.70, 1.408 at 636.03) |
| Master true peak | +3.5 dBFS | +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 19.0 dB | 19.1 dB |
| Delivery limiter | 1.8 dB | 2.2 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.58 / 4.52 | 8.53 / 4.50 |

- Climax order (delivered S max): 160 -10.00 > 122 -11.08 > 167-170 -13.17 > bar 26 -14.52. In c24: -10.07 / -10.97 / -13.10 / -14.42. The margin 160 over 122 went from 0.90 to 1.08 dB.
- Simulated before the render on the c24 stems: delivered LRA 14.3, limiter 1.5 dB. The render's limiter came out 0.7 dB higher, from the 484.53 phase sum (see above).
- Attack probe: 0 flagged.
- REAPER memory: 18 GB with 0 compressed at the render start, and 45 GB with 0 compressed after the render (c24: 46 / 21 compressed).

## Open for c26
- **A #4**: Horn 3 316.5-322.5 onto the a2 track, and Trumpets a2 with a memory budget.
- **Brass accent timing.** The peak median is still 0.20 s after the beat. Swell timing and level fits cannot move it, because the Sus MAX attack sets it. The next step is a row with a faster attack, or a front shape that starts before the onset.
- **Brass per-pitch stereo offsets** (Horn 1-4, Trumpet 1: SD 2-5 dB at 400-1000 Hz). Two width tests changed nothing. Inferred: the offsets come from the samples' own L/R content, possibly carried into the true-stereo hall by the pre-fader sends. Measure R-L on release tails against sustains before trying anything else. The horns' width stays at 0.05 (no measured difference from 0.15).
- **Extend width 0.05** to the other solo woodwinds (Flute 1/2, Oboe 2, Clarinet 2, Bass clarinet, bassoons, contrabassoon), which pass by the same measure. Check that master 250 Hz-4 kHz correlation stays at or under 0.56 (it is 0.549 now).
- **Hemiola master steps** at 539/542 (+0.3/+0.8). These need the horns, violas and basses accents too. Also the Violoncellos 94 before-window (the c19 cut on 91).
- **Oboe 1 498 / 538 crossovers** are still +0.135 / +0.115 s.
- **Master peak at qn 484.53** (1.538) sets the 2.2 dB limiter.
- **Run auto_fills on every lead line.** The c25 pass was applied to Oboe 1 only. It proposed 11 new fills elsewhere, among them Clarinet 1 227, which c24 removed by hand.

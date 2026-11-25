# Cycle 14: changes (actor)

One render from a freshly restarted REAPER (33 tracks), then one level-only stem fix (`tools/stem_fix.py 14 cycles/c14/rendered_build build --apply`). First-render stems are in `cycles/c14/render_first/`, first metrics in `cycles/c14/metrics_first/`, and the data the render was made from in `cycles/c14/rendered_build/`. REAPER was then updated with `--mix-only` (all tracks), saved and quit (it exited by itself). Snapshot of the c13 tools and data: `cycles/c14/before/`. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c14-actor/`:
- `pdiff.py`: parts.json diff;
- `peaks.py`: master peaks and the stems behind them;
- `m/checks.py`, `m/stems.py`, `m/stemsK.py`: the critics' criteria, the last one K-weighted;
- `A/`: critic A's scripts pointed at c13/c14.

Build note: the first `build_reaper.py --midi-only` was run from `build/` with `jobs`. That pointed at an empty `build/jobs`, so all 33 tracks were fully rebuilt in place. Only the four expected states differed from `jobs/`, and their `.b64` files were copied to `jobs/`. The stray folder was moved to scratch, and the project was then saved and restarted as usual. README now says which jobs directory to use.

## ONE_TIME: memory

`footprint` was read on settled sessions; top's GiB figure is in brackets.

| State | Footprint | Compressed |
|---|---|---|
| c13 project, fresh open, settled | about 46 GB [43 GiB] | 33 GiB |
| c14 project, fresh open, settled (before the render) | 46.48 GB [43 GiB] | 0 |
| After the render | [44 GiB] | 11 GiB |
| c13, after its render | [45 GiB] | 32 GiB |

Candidates, each measured:
- **Single-note Leg Port MAX rows** (Violins I/II at 225, celli at 685). Unloaded, then reloaded in a settled session: 46.01 -> 46.13 GB, so the three rows cost about 0.1 GB. The portamento stays (`PORT_TARGETS` unchanged).
- **Percussion merge.** Deleting the Crash cymbals instance in a settled session freed under 0.01 GB (46.135 -> 46.135; re-adding it 46.143). A merged percussion instance would save nothing measurable and would change the stem numbering, so the merge was not made.
- **Mic columns.** Every track already loads only Close + Main, and only the rows it plays (read back from every `jobs/*.b64`). Removing a mic would change the sound of a whole section, so no mic was unloaded.
- **c13 Detache row:** reverted (below), part of the same 0.1 GB-scale reload.

The settled footprint is the same as c13's, and nothing measured was worth cutting. The render ended at 44 GiB with 11 GiB compressed (c13: 45 / 32). The lower compression probably comes from the other processes on the machine, not from this cycle's changes. Other processes at render time: VM 2.7 GB, Steam 2.2 GB, two other users' Python processes 1.5 and 1.3 GB.

## Accepted

### Reverts of the c13 tests (A #5)
- Double basses `ART_SPANS` Detache 104-124 removed (`ART_SPANS = {}`). This was a full rebuild of the basses.
- Suspended cymbal back to key 64, `lead_s` 0.25.
- Brass `WIND_DETACH` back to gap 0.09 s / frac 0.18.

### Two-note slur release (A #1), new generic rule
- `score_to_parts.py` `SLUR_PAIR_RELEASE = {"db": -2.5, "from_s": 0.10, "full_s": 0.20, "max_qn": 1.0}`.
  - It applies to the second note of a slur of exactly two onsets, wind/brass/string.
  - Both notes are at least an eighth, and the second is at most 1 qn written.
  - The second note is not accented, tenuto or sf, and is not a hairpin's end.
  - No crescendo or rising printed level lies between the two onsets.
  - The shape is 0 dB at the moved onset + 0.10 s, -2.5 dB at + 0.20 s, held to the next moved onset, then back to 0. One shape per onset; parts.json `pair_release`.
- 52 notes on 21 tracks. Flute 1 109.5 is one of them, and it is A #6's pickup, so A #6's separate -2.5 dB cut was not added.
- Measured with A's `sigh3.py`, second minus first, flat-plan set, c13 -> c14:

  | Family | c13 | c14 | Share at -1 dB or louder |
  |---|---|---|---|
  | Strings (n 10) | -0.3 | -3.0 | 0.67 -> 0.30 |
  | Winds | +0.5 | 0.0 | |
  | Brass | -0.2 | +1.1 | |

  The strings pass. Winds and brass miss the target, for two reasons:
  - A's set includes 4 qn two-note slurs, which the rule leaves alone by design.
  - On eighths at 126 bpm (0.24 s) the shape reaches -2.5 dB only in the note's last 0.04 s. The eighth pairs moved -0.2..-1.4 dB (Trumpet 1 669.5 +5.3 -> +3.9, Clarinet 1 374 +3.4 -> +3.2), and Bassoon 1 353/362 moved -5/-8.6 (bassoon renders are not reproducible).

  Open: start the release earlier on short notes.

### Balance and dynamics, level only (B #1-#5, C #1-#6, A #4)
- **B #1 string soft trims.** `soft_trim_db` set to Violins I / celli {6, 6, 5}, Violins II {6, 5, 2}, violas {5, 6, 5}; the Violins II role [584, 619, +2] was deleted.
  - Solo minus the loudest string (K, per-qn median): Horn 1 bars 43-44 -5.5 -> +0.1, Oboe 1 bar 45 -0.4 -> +0.8, trombone chorale 175-178 -2.9 -> -0.5 dB.
- **B #2 / C #5, the bar-43 bloom.** Violins II shape (C's) and a violas -4 dB shape at 169.5.
  - Violins II per half qn 168-173: -46.3..-33.5 -> -49.6..-45.1 dB (a 4.5 dB range; pass 4).
  - Master 170-172 against 169: +0.4 -> +0.2 dB (pass 0; marginal).
- **B #3, the exposition ff basses.**
  - Role [104, 128, 3, 1], and the `loud_eq` wet held at 1 over 94-127.
  - The first render put the basses about 8 dB up instead of 4 (the Detache revert, the role and the held EQ together). The stem fix lowered the role to 1.5 dB.
  - Cb re master (K), bars 27-31: c13 -18.0/-21.5/-19.6/-23.0/-18.9 -> c14 -11.1/-14.9/-16.1/-17.0/-16.1. Bars 131-134: -12.6.
  - Cb minus celli, bars 28-31: -7.5/-6.9/-8.7/-10.4 -> -0.9/-2.7/-2.7/-6.9 (target -1..-3).
- **B #4, Horns a2.** Window roles now end with the note they cut (316.1, 406.2, 484.1), plus a phrase-end taper at 314.
  - The first render's -2.5/-5 dB taper left the a2 2.5 dB over Violins I at 314.5-315 (K). Stem fix: [(314.0, 0), (314.2, -5), (314.6, -7.5), (316.0, -8), (316.2, 0)].
  - a2 minus Violins I per half qn 314-316: c13 +0.2/+8.5/+5.9/+7.9 -> -4.5/-1.9/-5.8/-5.3 dB.
- **B #5, the coda bass.** Basses second `loud_eq` spec, 66 Hz +4 dB bw 0.6 over 662-680.
  - Master 60-100 Hz share in 664-680: -23.5 -> -17.9 dB. Other tutti: 104-124 -19.7, 520-536 -18.7, 636-644 -19.9.
  - 63 Hz third-octave of the file re 1 kHz: -1.2 dB.
- **C #1, bar 51.** Horn 1 cut over the 203 quarter; the celli hold ends at 203.05.
  - The first render's -5 dB took the master arrival from +5.1 to +0.3 dB. Stem fix: -1.5 dB.
  - Master arrival +1.8 dB (pass +1.5..+3.5). Delivered bar 51 M max -17.99 -> -20.79, under bar 61 (-18.21).
- **C #2, the bar-159 E6 fill.** The fill now lets go after the E6 (633.9 -> 635.0), and the A-flat6 gets +2 dB on both violin sections.
  - Master M 636.5-638 minus 634.5-635.5: +0.37 -> +1.87 dB (pass 1.5).
  - Delivered M max at bar 160: 0.76 dB over bar 122 (pass 0.8; c13 0.28) and 1.72 over bar 170 (pass 1.5).
- **C #3, the morendo.** `_all` shape from 724.25, steepened by the stem fix at 725.0/725.6.
  - Master per half qn 724-728: -40.3 -40.1 -39.9 -38.9 -39.1 -39.2 -39.3 -45.5 -> -40.6 -40.9 -42.5 -42.5 -44.0 -45.0 -46.0 -52.9. There is no rise; 727 is 5.4 dB under 724.
- **C #4, letter G.** Held ff parts +2.5 dB over 468.6-479.6, plus the basses' bloom cut and fill.
  - Master M bars 116-122: c13 -13.0 -12.7 -14.1 -15.2 -14.7 -12.1 -7.4 -> c14 -12.7 -13.1 -12.8 -13.8 -13.3 -12.2 -7.3.
  - Bars 118-120 are now within 0.7 dB of bar 117, and bar 122 is 6.0 dB over bar 120.
- **C #6, bar 148.** Celli sag fill and Horn 1 +2.5 dB.
  - Celli 591.0-591.6: -33.2..-37.2 -> -31.4..-32.6 dB, now flat.
  - Master 591-592 against 590-590.5: -1.8 -> -1.55 dB (pass 0.5; not met).
- **A #4, Horn 4 at 289.** Loop fill [4.78 s, +7 dB, 0.5 s].
  - The dip went from -10.2 dB at +4.80 s to none there. The deepest point left is -4.7 dB at +6.45 s, and the highest +2.2 dB.

### Stem fix: the master's top peak
- The first render's top sample peak was 1.725 at qn 641.72 (c13 1.587 there): the celli, tuba, Trombone 1 and bass trombone sustaining before the bar-161 change.
- A -2.5 dB notch over 641.62-641.78 on those four tracks took the peak to 1.488 and the delivery limiter from 2.8 to 1.5 dB. The next peaks are 1.368 at 637.79 and 1.348 at 490.79.

## Tests that failed (left in the render and the tools; replace or revert in c15)
- **A #2: CC36 round-robin resets inside the music** (`MEAS_TREM["rr_runs"]`, 13 resets in 464-484). Celli stroke autocorrelation at lag 9:

  | Feature | c13 | c14 |
  |---|---|---|
  | Peak | 0.71 | 0.73 |
  | 1-8 kHz share | 0.82 | 0.85 |
  | Centroid | 0.93 | 0.92 |

  Pass was under 0.3. A CC36 inside the music does not reset the Stac RRx9 round robin on the Celli KS Master. CC36 is labelled "Repetition: Reset RR" in the controllerMap, and the Repetition script is off (CC69 0) on the strings. Next: alternate two rows, or vary the strokes' velocity or length.
- **A #3: the brass `WIND_DETACH` CC11 fall** (10 CC over the last 0.10 s, notes of 0.6 qn or less).

  | Brass change | c13 | c14 |
  |---|---|---|
  | Gap under 0.06 s | -3.1 dB (n 41) | -3.5 dB (n 84) |
  | Slurred | -3.6 | -3.6 |

  Pass was -5.0 or deeper. At f/ff, 10 CC of CC11 moves about 1 dB on these patches (kit section 4: 1.2 dB per 10 CC at CC 88-128). Next: put the fall in the volume envelope (dB), not CC11.

## Rejected or deferred
- **A #6, Horns 3-4 a2 at 316.5-324** (`TRACK_WINDOWS` from the Hn3 staff): deferred. It needs a routing change, and memory is at the guide.
- **A #6, the Trumpet/Trombone a2 patches:** memory (a new instance each).
- **A #1's accent refit** (`fit_accents.py`): deferred to the next cycle. It needs a render with the release in place, and this cycle's level checks would mix with it.
- **A #6, bass trombone low notes:** no action, as A said.

## Before / after (c13 -> c14, after the stem fixes)

| Measure | c13 | c14 |
|---|---|---|
| Master integrated (float stem sum) | -16.1 LUFS | -15.8 LUFS |
| Master LRA | 21.8 LU | 22.5 LU |
| Master sample peak | 1.600 | 1.488 |
| Master true peak (float) | +4.1 dBFS | +3.5 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.2 LU | 14.8 LU |
| p10-to-max span | 18.5 dB | 19.5 dB |
| Delivery limiter | 2.3 dB | 1.5 dB |
| Delivered true peak | -1.6 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.74 / 4.53 dB | 8.65 / 4.61 dB |

- Delivered mp3: `cycles/c14/mvt1-mockup-c14.mp3`. First render, before the stem fix: limiter 2.8 dB, the same LRA and span.
- The span is 0.5 dB over the 19 dB target. It comes from B #1's lower string pp, and B's simulation had predicted 18.9 dB.
- Climax order on delivered S max: 160 -9.84 > 122 -10.93 > 167-170 -12.99 (c13 -10.15 > -10.83 > -12.87).
- Simulation before the render (c13 stems, level changes only): LRA 14.7, span 19.2, limiter 2.3. The render measured 14.8 / 19.5 / 2.8, and the extra limiting came from the 641.72 crest.
- Item 8: 2-5 kHz first 80 ms minus body, median (max), c13 -> c14:
  - brass -8.2 (3.8) -> -7.8 (2.6), with no brass accent over +3 dB;
  - winds -5.6 (9.7) -> -5.8 (3.7).
- Attack probe: 0 flagged.
- REAPER memory: 43 GiB with 0 compressed when the render started, 44 GiB with 11 compressed after it (`metrics/memory.txt`).

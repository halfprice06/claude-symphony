# Cycle 01 (actor), on the c00 render and the critics' reports A, B, C

Render: `cycles/c01/scherzo-mockup-c01.mp3` (one render, full rebuild of all 31 tracks, stem fix on three string stems afterwards). Measurement scripts: `cycles/c01/actor_scripts/` (`post.py` before/after checks, `cut.py` tutti cut-off decay, `rowsamples.py` row -> sample folders, `arts.py` per-note rows from parts.json, `lv.py` helpers). Snapshot of the tools and data before the cycle: `cycles/c01/before/`; the data the render was made from: `cycles/c01/build_render/`.

## Dan's standing note S4 (too wet, mushy; coordinator, 2026-11-07)

- `build/mix.json` `reverb.fx_volume` 0.19 -> 0.095 (-6 dB on the shared hall return; the Movement I thread's shared value). Sends, IR, wet 2.0, true stereo, high cut 5.5 kHz unchanged. A first attempt at lowering the per-track sends was reverted before the build, as instructed.
- New `reverb.low_cut_hz` 160 (hall input low cut). `tools/build_reaper.py` now writes it (the `low_cut_hz` block copied from `mockup-kit/pipeline/build_reaper.py`: Bandpass `filterActive`, `lowFilterFreq` = `lowCutFreq`). Checked in the generated state (`jobs/24_*.b64`: lowFilterFreq 160, highCutFreq 5500).
- Every Opus state changed, so every track was fully rebuilt.
- Measured: the master's drop 0.3 s after each tutti cut-off, relative to the peak before the release (`cut.py`):

  | cut-off | c00 | c01 |
  |---|---|---|
  | bar 120, qn 358 | -11.7 dB | -13.9 dB |
  | bar 132, qn 393.5 | -11.7 dB | -16.2 dB |
  | bar 288, qn 861.5 | -10.3 dB | -14.4 dB |
  | bar 339 (G.P.), qn 1015 | -15.5 dB | -15.9 dB |

  So every tutti cut-off now meets the 13 dB target (recordings: 13-17 dB). The late decay did not change: T60 from the -20..-40 dB segment after the G.P. cut-off is 3.5 s (c00) and 3.7 s (c01). The fx volume lowers the tail, not its slope, so the late decay is still over 2 s. **Open**: try a shorter hall (Opus IR envelope, manual p.133-134) in a later cycle.
- Soft bars after loud ones lost the old tail: bar 122 (the sub. p) has the basses -9 dB, tuba / contrabassoon / bass trombone -6..-7 dB against c00, which is the ff hall tail no longer filling the p.
- Delivered LRA 13.9 -> 13.6 LU. The master is -0.1 dB quieter integrated (-19.7 -> -19.8 LUFS after the stem fix).

## Accepted and made

- **A #1, DOWNBOW_STROKE_AT** (`build/score_config.py`). The 27 Violins I, 13 Violins II, 10 viola and 3 celli onsets the critic listed are now fresh Sus MAX strokes. Added 1008 / 1010 / 1012 for all four sections: with 1005 a stroke, `STR_ACC_AFTER_SUS` had turned those accented half notes into v127 strokes with no lead, and had left the celli's 1008 as a same-pitch Leg Slur re-attack. **Result: the change did not work.** Accent level over the staccato before it, as the mean of the first 150 ms minus the 100 ms peak of the staccato (Violins I):

  | onset | 39 | 51 | 69 | 75 | 111 | 123 | 285 | 315 | 327 | 759 | 789 | 795 | 819 | 915 | 999 | 1005 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | c00 (dB) | -14.9 | -7.3 | -10.2 | -14.7 | -5.4 | -3.3 | -14.8 | -3.1 | -2.9 | -9.2 | -8.9 | -9.1 | -7.3 | -3.0 | -7.8 | -16.9 |
  | c01 (dB) | -14.1 | -14.6 | -13.6 | -14.0 | -9.0 | -4.4 | -8.5 | -6.2 | -0.5 | -12.2 | -10.6 | -12.2 | -9.0 | -3.3 | -9.5 | -13.6 |

  At p the strokes play at velocity 52 (`REBOW_VEL_BY_CC` at CC 46) and are as slow as the Leg Slur first-note layer. The master in the first 0.15 s of bar 336 is -1.2 dB against the beat before it (c00 -0.6). Kept for now: the strokes match the printed bowing, and the summit balance was fitted on them (below). **Open for c02**: raise the stroke velocity (try the accent's own velocity, about 90-105, as Movement I's "velocity 105 or more" Leg -> Sus path), or test "Sus Marc LITE" / "Marc Shrt RRx4" on these heads, and measure 2-5 kHz attack minus body as well.
- **A #2, re-bow fills**: `tools/fit_rebows.py 0 cycles/c01/before/parts.json --write --skip "Violoncellos:612.591" --hold-max-after 1120:3.0` wrote `build/rebow_fills.json`. Violins I has 5 fitted re-bows and the celli 1078.442. The celli's 612.591 was skipped because it falls right after the pp that ends a decrescendo and the fit came out -6 dB (Movement II c29's case). The hold after 1120 is capped at +3 dB because those re-bows lie under the final fermata. Violins I's dip in the first 1.2 s against the 0.75 s before (0.1 s frames): 6.5 / 433.2 / 1103.9 / 1116.4 / 1125.1 went from -8.6 / -10.4 / -9.0 / -7.5 / -8.4 to **-1.1 / -2.0 / -1.7 / -2.3 / -1.7 dB**. The master in bar 370 is +3.2 dB.
- **A #3, tutti staccatissimo** (S1): `ART_SPANS` over 312-360 and 912-960 with `"mark": "staccato"` and `"poly"`, at the Stac row's velocity:
  - Rows, each checked against its region sample folders (`actor_scripts/rowsamples.py`): Violins I "Stac RRx14" (V1 StacSs), Violins II "Stac Slur RRx6" (V2 StacSs), violas and celli "Staccatissimo RRx16" (StacSs). Each has pp/mp/f/ff layers.
  - `ROW_TRIM_DB` for the new rows starts at the replaced rows' values.
  - Master dip between the eighths of each pair, bars 105-120: 3.2 / 1.8 / 0.6 / 2.0 / 2.2 / 1.7 / 2.9 -> **3.1 / 3.7 / 0.6 / 3.6 / 1.2 / 2.4 / 4.3 dB**.
  - Bars 305-320: 3.3 / 0.6 / 0.4 / 1.8 / 1.3 / 1.7 / 2.0 -> **3.8 / 3.3 / 1.1 / 4.6 / 1.9 / 1.1 / 3.3 dB**. That is better, but 325/925 and some others are still under the 3.5 dB target.
  - The strings in the tuttis got louder: Violins II +2..+6 dB in bars 106-118 and 306-312, Violins I +2..+4.
- **A #4 / C #5, MANUAL-GAPS #1**: every printed woodwind staccato on "Stac DblTng RRx9" for Flute 1, Flute 2, Oboe 1, Oboe 2, cor anglais, Clarinet 1, Clarinet 2 and Bassoon 1 (`ART_SPANS` 0-1128, `vel_by_cc` (22,44) (34,54) (46,64) (58,72) (72,82) (88,96) (114,112) (124,118)). `STAC_LEAD_S` is 0.02 s on these tracks (cor anglais 0.03).
  - Same-pitch eighth pairs, median stem dip: Flute 1 3.8 -> 5.0 dB, Oboe 1 4.1 -> 4.9 (but p10 2.5 -> 0.0), Clarinet 2 2.4 -> 4.7, cor anglais 3.8 -> 4.7.
  - Level of the staccatos against c00 (100 ms peak at the onset, median): Oboe 1 **+4.9 dB**, Clarinet 2 +1.5, Flute 1 -1.1, Flute 2 -1.0, Bassoon 1 -0.9, cor anglais **-4.5 dB**. **Open for c02**: per-track velocity tables (Oboe 1 lower, cor anglais higher), then a look at the Oboe 1 pairs that no longer separate.
- **A #5**: Double basses pizz. pitch trims (`build/pitch_trims.json`, `_arts` Pizz RRx4): 32 -5, 33 -6, 28 +2, 40 +1. The critic's 44 / 45 (-5) were left out because simultaneous notes' trims add in the envelope: an A1+A2 octave would have taken -11 dB against its +5.7 residual. 40 is +1 so the E octave gets +3.
- **A #6**: `PORT_TARGETS = {"Violins I": {640.0: 100}}` (Leg Port MAX loaded). Not measured this cycle.
- **B #1**:
  - Horn pitch trims (`pitch_trims.json`, `_all_arts`): Horn 4 52 -4 / 54 +4 / 66 +4 / 68 +3.5; Horn 1 66 +4 / 68 +3.5; Horn 2 66 +4 / 68 +3.5 / 64 -3; Horn 3 64 -3 / 68 +3.5.
  - Horn 4 soft trims ppp / pp 14 / 13.5 -> 10 / 9.5.
  - Roles: Horn 3 [456-504 -3, 708-720 -4]; Horn 4 [360-381 -4, 456-504 -2 (added after a simulation: the critic's set left the clarinet only 0-3 dB over the drone), 684-720 -3]; Horn 2 360-381 -4; Clarinet 1 456-504 +2.
  - Clarinet 1 minus Horn 4 per two bars from 153: -9.7..-3.4 -> **+0.8..+8.7 dB** (median about +4).
  - Bar 121 onward: Violins I minus Horn 4 went from about 0 to +2..+4 dB in the simulation.
- **B #2 + C #1**: roles Violin I solo +7, Flute 1 -6 and Violoncellos -2 over 1044-1068. Solo minus flute per bar 349-356 went from -7.0..-10.9 to **+1.4..+5.8 dB**.
- **B #3**: summit roles over 1002-1017:
  - Cor anglais -3, Bassoon 1 -3, Clarinet 2 -5, Flute 1/2 -4, Clarinet 1 -4, Oboe 2 -4, Oboe 1 -3, Contrabassoon -3, Bassoon 2 -1.5. These are reduced by B #4's trim changes.
  - At 306-312 and 906-912: Clarinet 1 -5, cor anglais -2.5, Clarinet 2 -3.
  - The single winds at 1005-1014 now sit at -25..-27 dB (c00 -18..-21).
  - The critic's string lifts were not made, because the strokes raised the strings (below).
- **B #4**: dyn trims Bassoon 1 f / ff 3.5 / 2.5 -> 0 / 0, Bassoon 2 4 / 3 -> 0.5 / 0.5, cor anglais 2.5 / 3 -> 0 / 0.5.
- **B #5**: Timpani role [300.0, 300.5, -12]. This is a short cut on the burst only: the critic's -8 over 300-303 had also pushed the roll body at 301-303 down to -37..-47 dB in the simulation. Simulated burst: -18.3 -> -30.3 dB.
- **C #2**: `loud_eq` (Movement I's bands; wet ramps over 298-300 ... 358-360, 898-960, 982-1017) on celli, basses, Bassoon 2, contrabassoon, bass trombone and tuba. No timpani.
- **C #3**: Violas div gain 6 -> 2 dB, width 0.3 -> 0.45. Violas div minus Violas per two bars of 209-224 went from +2.9..+7.2 to **-2.9..+2.4 dB**.
- **C #4**: side low shelves, Double basses 100 Hz -15 -> -4 dB and Timpani 150 Hz -9 -> -4 dB. Master L/R correlation was not re-measured this cycle.
- **C #6**: widths Clarinet 2 and Trumpet 2 0.05, Contrabassoon 0.15.
- Pre-existing WARNING (c00 printed it too): Horn 1 mp at qn 624 sat at CC 52. Added `HP_TARGET_AT {"Hn1": {618.0: "mf-"}}`: the p < > mp crest now reaches 68 and the > lands on 58. parts.json has no WARNING.

## Stem fix after the render (level only, `tools/stem_fix.py --apply`; originals in `render_first/`)

The summit strokes put the celli +8..+11 dB, violas +5..+7 and Violins II +3..+5 over c00 in bars 336-338. The float master peaked at 1.489 and the delivery limiter took 5.9 dB. Roles over 1005-1016 (violas 1002-1016): Violoncellos -6, Violas -3, Violins II -2. Results:
- master peak 1.026;
- delivery limiter 3.1 dB;
- bar 337 -12.1 dB is still the loudest bar, but only 1.2 dB over bar 304 (-13.3; c00 margin 2.9 dB).

The same data went into REAPER with `build_reaper.py --mix-only Violoncellos Violas "Violins II"` and was saved before the quit.

## Rejected or deferred

- A #6 harmonic on the 2nd Violins Harmonics row: deferred. It needs a second routing window per track in `score_to_parts.py`, and its re-bow is now filled (433.2 dip -2.0 dB).
- C #5 trumpet staccato rows: deferred (no measurement of 1TP "Stac DblTng" brightness at f yet).
- B #3's Violins I +2 / Violins II +1.5 at the summit: not made (the strokes raised the strings).

## Measured summary

- Master (after the stem fix): -19.8 LUFS integrated, LRA 21.8 LU, true peak +0.2 dBFS (float stem sum, peak 1.026).
- Delivered mp3: -19.9 LUFS, LRA 13.6 LU, TP -1.6 dBTP, limiter 3.1 dB, p10-to-max span 19.0 dB.
- Attack probe: all 20 attacks and the opening ok. The two failures are the string legato spread, Violins I SD 89 ms and Violins II 93 ms (limit 75), already failing at c00 (80 / 96).
- REAPER memory: settled 49 GB with 16 GB compressed before the render, 50 GB with 32 GB compressed after. That is over the 45 GB cap; c00 was 45 GB. The 13 newly loaded rows cost about 4 GB. The render passed the memory gate without `--force-memory`. **Open**: unload or drop rows (for example the wind stac row on Oboe 2 / Bassoon 1 / Clarinet 1, which have few staccatos).
- Lock held 08:55:21-09:23:49 (28.5 min), after a 48 min wait behind Movement I. Full build 73 s.

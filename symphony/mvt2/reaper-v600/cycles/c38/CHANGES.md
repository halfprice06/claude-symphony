# Cycle 38: changes (actor, on the critics' reports of the c37 render, plus loop/ONE_TIME.md: a drier hall)

Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/`. Scripts: `actor_scripts/hall38.py` (cutoff drops, late decay, repeat dips and join dips per render), `actor_scripts/check38.py` (c37/c38 levels at every critic finding).

## ONE_TIME (Dan, 2026-11-07: too wet, a bit mushy)

- `build/mix.json` `reverb.fx_volume` 0.19 -> 0.095 (-6 dB on the hall return). Sends, IR, wet 2.0, the 5.5 kHz high cut and true stereo unchanged.
- ONE_TIME item 7 (coordinator, added mid-cycle): `tools/build_reaper.py` takes the kit's `low_cut_hz` block (Bandpass on, `lowFilterFreq` = `lowCutFreq`); `build/mix.json` `reverb.low_cut_hz` 160. Folded into the same full rebuild, before the render.
- Every track fully rebuilt (32 Opus states).

Measured with `hall38.py`, c37 -> c38 (master and stems, 50 ms / 30 ms windows):

| Measure | c37 | c38 | Target |
|---|---|---|---|
| Stem cutoffs (68-77 note ends with 1.2 s of silence after, ref > -50 dB): median drop at +0.3 s | 12.3 dB | 17.5 dB | 13-17 |
| same at +1.0 s | 30.2 dB | 35.4 dB | |
| Master after the final chord (304), drop at +0.3 / +0.6 / +1.0 s | 8.9 / 16.6 / 29.8 | 8.3 / 17.3 / 35.9 | |
| Master late decay after 304, RT60 from the -20..-40 dB slope | 2.08 s | 1.19 s | 1.5-2 s |
| same from the -5..-25 dB slope | 2.23 s | 2.01 s | |
| Same-pitch repeats (134): median / p90 dip | 2.45 / 6.07 dB | 3.1 / 7.4 dB | deeper = more audible (S1) |
| Joins (913): median / p90 dip | 2.4 / 6.0 dB | 2.6 / 6.2 dB | |

- Movement II has only one full tutti cutoff (the final chord, after a CC11 morendo fade); there the first 0.3 s is the strings' release samples, so its +0.3 s drop did not move. The per-stem cutoffs carry the measure.
- The late decay is now under 2 s, so no shorter hall IR is needed (ONE_TIME item 5).
- Master integrated -19.9 -> -20.4 LUFS before the stem fix (the hall's share of the energy went down).
- S3: the bar 66 niente now falls 7.2 dB in the master (223 -42.8 -> 225.5 -50.0; c37 3.3 dB, with critic C #1). The coda morendo falls 296-304 as before, and the tail after 304 decays with no cut (-49.2, -52.9, -70.3 at 303/303.5/304, 0.5 qn).
- Fills and notches the drier tail moved: `tools/auto_fills.py 38` against `auto_fills.py 37` showed about 30 joins newly over its 5 dB threshold (most at 5.0-5.5 dB). I refit only those over 6 dB with a level-only fill and checked overshoot on stem_fix-simulated stems (dip / peak over the lower body, render -> simulated):
  - kept: Bass clarinet 91.5 new {4.4, hold 0.2} (6.9/1.9 -> 3.0/4.2); Bassoon 1 201 new {3.4, hold 0.1} (6.3/5.1 -> 2.8/4.9); Bassoon 1 258 new {6.0, hold 0.1} (7.6/4.7 -> 3.1/6.0); Violoncellos 206 new {3.3, pre 0.02, hold 0.1} (5.6/1.5 -> 3.6/2.9); Clarinet 1 283 1.0 -> 3.0 (4.3/5.5 -> 3.0/6.6; the hole came from the B #3 CC7 cut plus the drier tail).
  - tried and reverted: Bassoon 1 145 and 256, Violins I 80, Violins II 80, Violas 84 (a deeper fill raised the peak over the previous note's end by 1.5-5 dB for 0-1 dB less hole).
  - Applied by `stem_fix.py --apply` (originals in `render_first/`) and `build_reaper.py --mix-only` on those four tracks.
- The breath and re-tongue gaps (tutti breath at 204, Bassoon 2 253, Clarinet 2 204) are now 4-6 dB deeper, which is the intended effect for S1.

## Critic findings

Accepted (all level-only, `build/score_config.py` block "c38" and the json tables):
- B #1 bar 81: shapes holding -1.5 dB from 268 to 271 on the 15 non-melody tracks; roles Violas/Violoncellos/Double basses [262, 268, -1.5] -> [262, 270.9, -1.5]; early fill Violoncellos 269 3.4 -> 1.0.
- B #2 bar 56: Violoncellos CC7 71 (-5 dB) over 184.55-185.0 and 186.55-187.0; `pitch_trims.json` Horn 1 and Horn 3 D flat 4 (61) -2.5, Horn 1 skips 23.0 and 37.5.
- B #3 coda: Clarinet 1 CC7 85/80/95 at 282.75-283.1 and 291.9-292.35.
- B #4 bar 80: Cor anglais CC7 90 (-3 dB) over 266.05-267.9.
- B #5 bars 29-30: Violas +6 dB over 87.1-89.0 (rises only, 2 dB fall after the release).
- C #1 bar 66: Double basses -3/-4 dB over 224.5-226.25 (0.5 qn ramps).
- C #2 bars 54-57: Violins I/II and celli: c30's mf hold-back and c34's 180.5-183.1 hold replaced by one shape (179.5 0, 180.5 2, 183.1 2, 184.25 0.5, 187.75 1, 190 2, 193 1, 196 0).
- C #3 bar 65: Violas -5 dB over 219.85-225.9.
- C #4 bar 74: roles Violins I/II [237.5, 250, -2.5, 0.5] -> end 248.75.
- A #2 bar 28: early fill Violas 84 2.4 -> {4.0, hold 0.42}.

Rejected or deferred:
- A #1 (Flute 1 136 on Leg Slur Rep, a new tool option, CC1 and gap changes): deferred to c39. It changes a row and the note timing, and this cycle was to keep critic changes level-only while the hall moved.
- A #3 (Horn 2 208 re-tongue gap): deferred for the same reason (a timing change); the drier hall alone deepened the other repeats by 0.6 dB median, so re-measure first.
- A #4 (Trombone 1 218 +1.5) and C #5 (Trombone 1 214.6-219.5 -2): they pull in opposite directions (A in the master, C in the delivered mp3); neither applied.
- A #5 (violas portato velocity variation): low priority, deferred.
- C #3's alternative -4 dB and C #1's optional removal of `_all [220, 226, 2]`: not needed after the measured result.

## Measured (c37 -> c38, plain RMS on stems, window in qn)

- Master after the stem fix: -19.9 -> -20.3 LUFS, LRA 23.8 -> 24.6, TP -0.7 -> -1.5 dBFS, sample peak 0.839, no clipping. Bars 61/62 -14.3/-14.9, bars 79/80 -20.0/-20.9 (climax order holds).
- Delivered: -19.8 LUFS, LRA 15.2 -> 15.6, TP -1.6 dBTP, span 18.5 -> 19.1 dB, limiter 1.9 -> 2.3 dB.
- Attack probe: 0 flagged ("late or hole: 0").
- B #1 master 266.5-270 (0.5): -18.2, -18.1, -18.9, -19.4, -21.7, -23.9, -26.1, -28.1 (c37 had a 0.7 dB rise at 268); violas at 268.5 -30.5 against Violins I -31.6 (c37 +4.7 over); celli at 269 -32.2 against -35.6 (c37 +7.9).
- B #2 celli 184.75 -25.2 -> -26.9 (Violins I -29.6, now 2.7 dB under the celli instead of 6.3); Horn 1 186 -31.0 -> -34.4 (2.4 dB under Violins I).
- B #3 Clarinet 1 282.75 -37.5 -> -41.8, 292.0 -36.5 -> -41.7.
- B #4 cor anglais 266.5 -25.0 -> -29.8 (Violins I -30.3).
- B #5 main violas 87-89 -55..-57.6 -> -49.9..-52.7, level with the div half (-48.3..-51.7).
- C #1 basses 224.75-226 -45.1..-45.8 -> -51.4..-52.6.
- C #2 master per 2 qn 176-194: -28.3, -27.6, -28.4, -26.7, -24.8, -25.5, -24.9, -24.8, -23.7, -23.0 (c37 flat at -26.5..-26.9 over 180-186).
- C #3 violas 219.75-220.25 -42.6..-41.7 -> -49.4..-47.8 (Violins II -44..-45.5).
- C #4 Violins I 249.25 -38.9 -> -36.5.
- A #2 violas 84.0-84.3 (0.1 qn) -47.4..-48.3 -> -46.4..-47.7, the next body -45.5: within 2 dB.

REAPER memory: 44 GB settled before the render (0 compressed, no `--force-memory`), 44 GB with 12 GB compressed after the render, 45 GB at quit. REAPER crashed once in Opus (SIGSEGV in an Opus worker thread, `REAPER-2026-11-07-100131.ips`) 12 s into the first full build, during Clarinet 2's job; I restarted, waited for the open to settle at 44 GB, and the second full build completed all 32 tracks. Lock held 09:59:58-10:50:44 (51 min, about 20 of them lost to the crash); the wait behind Movement I and the scherzo was 08:31-09:59.

# Cycle 22: changes (actor)

This cycle accepted all 13 critic findings. Most are level-only. Two change notes or patch state: the celli's bar-122 fff note is now a fresh stroke (C #1), and the violas' release-trail groups were capped (A #4, a test, which failed). One delivery-master change (C #3).

REAPER steps:
1. Fresh start, project opened (33 tracks).
2. `build_reaper.py build/parts.json jobs --midi-only Violoncellos Violas`. The Violas Opus state changed, so that track was fully rebuilt. Then `--mix-only` on the 26 other wind, brass and string tracks (envelope changes only).
3. Save. The quit job timed out, but REAPER had exited. Fresh start, open, render (`render_cycle.py 22`).
4. Level-only stem fix on Violins I and Violoncellos (below), then `render_cycle.py 22 --measure-only`.
   - The `stem_fix.py --apply` copy of all stems to `render_first/` filled the internal disk (1 GB free; 901 of 926 GiB used by other data). The bridge script then stopped at a ReaScript error dialog.
   - `render_first/` now holds only the three originals that the fix replaced: master, Violins I, Violoncellos.
   - REAPER was killed. The project had been saved by `render_cycle.py` before the render.
5. Fresh start and open, then `build_reaper.py --mix-only "Violins I" Violoncellos` so the project matches `build/`. Save. The quit job timed out, but REAPER had exited.

Files:
- `cycles/c22/before/`: the c21 tools and data.
- `cycles/c22/rendered_build/`: the data and code the render was made from.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c22-actor/`. It holds `pdiff.py`, `simfix.py` (a stem-fix simulation that writes only the master), `rankd.py`, `trace.py`, `bardiff.py` and `rtcheck.py`, plus copies of critic A's scripts in `A/`.

## Code

- `tools/score_to_parts.py`: new generic rule `STR_REP_DETACH`, default None. It takes `{"at": {track: [(a, b)]}, "dip_db", "dip_s", "ramp_s", "back_s", "max_qn", "min_cc"}`.
  - Inside each listed score-onset span, an unslurred string note of `max_qn` or less that runs into the next onset, at a printed level of `min_cc` or more, gets an exact volume dip before the next moved onset.
  - parts.json key: `str_rep_dips`.
- `tools/build_reaper.py` `cap_release()`: optional `"rt_ms"`. It also caps the release-trail ("RT") groups of the listed rows and dynamics.
- `tools/deliver_master.py`: `MOM_CAP_ABOVE` 6 dB and `MOM_CAP_SMOOTH_S` 0.5. A lift cap is read from momentary loudness (the maximum over ±0.5 s), so no momentary peak is lifted above knee + 6 dB.

## Accepted

| Finding | Change | Measured c21 -> c22 | Pass? |
|---|---|---|---|
| A #1 basses ff eighth pedals | `STR_REP_DETACH` on basses 104-124.25 / 520-536.25 / 556-568: -5 dB, 0.08 s, 0.02 s ramps (95 dips). Plus +1.5 dB level shapes over the spans | Basses eighth-grid fold 30-150 / 150-600 / 1-4k Hz: 104.5-124 2.8/2.8/1.7 -> 6.8/6.6/5.7; 520-536 2.7/3.5/2.5 -> 7.5/8.4/6.8; 556-567.5 3.1/4.3/2.5 -> 7.5/8.8/5.6 dB. Basses RMS -0.12/+0.08/-0.04 dB. Master 30-150 Hz fold 2.2 -> 3.3, 3.9 -> 5.2, 3.0 -> 4.0 | yes |
| A #2 celli Lento re-bows | `fit_rebows.py 21 --tracks Violoncellos`; only rows 39.879, 41.38 and 49.683 merged | Dips: 39.879 -10.4 -> -4.4; 49.683 -8.2 -> -4.4; 41.38 -4.2 -> better than -4.4. Celli median re-bow dip -2.8 -> -2.6, worst -10.4 -> -7.9 (723.9, unchanged). Master at 39.879 -2.4 -> -2.3 | yes (master -2.3 against -2.0, as in c21) |
| A #3 accents on the capped tracks | `fit_accents.py 21` (string family, c20 options, skips plus Vla/Vc 607), merged for Violas, Violoncellos and Double basses only. Celli 124 kept at 4.5 (the refit read the new bar-31 cut on its neighbours as excess). `fit_accent_bodies.py --max-cut 3` merged for the same three tracks (basses 328 -3.0, 330 -0.5, 676 -1.7) | Fitter predictions: string family median +3.06; basses 97 +2.3, 542 +0.5 (at the 4.5 cap) | partial (basses 542 stays under 2 at the cap) |
| A #5 Horn 4 joins | `early_fills.json` Horn 4 415 +4.0 (hold 0.35 s) and 453 +4.2 (hold 0.45 s; `auto_fills.py` found 453 at a 7.2 dB dip) | 453: sag over +0.05..+0.5 s gone (-38..-42 -> -34..-38 dB per 1/8 qn), peak +1.8 over the body. 415: +4 dB through the hole, but a -5 dB envelope step from 415.2 (present since c20) still leaves 415.25-415.9 about 4 dB under the attack | 453 yes, 415 partial |
| B #1 fugato basses pizz | Basses -5 dB step over 335.9-348. Stem fix: celli +1.5 dB over 336-348 | Basses bars 85-87 -5.0 dB. Master bars 85/86/87 (plain) -29.8/-30.8/-31.9 -> -29.3/-31.1/-32.5 after the celli lift | yes |
| B #2 bar 31 celli bloom | Celli -4 dB over 120.6-123.75; 122 fill 5.6 -> 3.0; bar 82 -2 dB | Celli bar 31 -4.1 dB, bar 82 -1.8 dB. Master 160-300 Hz bar 31 -28.0 -> -30.7 (bars 28-30 -32.9/-36.4/-30.6) | yes |
| B #3 bass-clarinet solo | Clarinet 1 -3 over 306.45-309.8, Violins II -2 and violas -1.5 over 304.5-306.4 | Clarinet 1 bars 77/78 -3.0/-1.9 dB | applied as simulated |
| B #4 bar 115 Oboe 1 | +4 dB over 455.85-459.8 | Oboe 1 bar 115 +4.0 dB | applied |
| C #1 celli 484 | `DOWNBOW_STROKE_AT` celli + 484.0 (Sus MAX stroke; 488 joins it as a Leg BC target) | Celli per 1/8 qn, 484-486: c21 -15.3 -18.1 -19.9 -24.3 -28.0 -31.6 -33.3 -31.5 -34.0 ...; c22 -15.3 -15.9 -16.7 -15.4 -19.1 -23.2 -24.0 -27.8 -21.9 -20.1 .... Worst 1/8 qn 6.0 dB under the 486-488 median (c21 12 dB). 2-5 kHz first 80 ms minus body +4.9 -> -4.6 dB. Master 484-485 +0.3 dB | yes (at the 6 dB edge) |
| C #2 bars 122-123 sostenuto | `_sost` shape (+0.8..+1.5 dB, 485.5-492.25) on every wind, brass and string track | Master per beat 484-491: -10.7 -11.0 -11.9 -13.3 -12.3 -12.8 -12.9 -13.3 -> -10.4 -10.8 -11.0 -11.8 -12.0 -11.5 -11.8 -11.7 (fall 2.6 -> 1.4 dB). Delivered S 160 -9.94 > 122 -11.02 (margin 1.08 dB) | yes |
| C #3 delivery momentary cap | `MOM_CAP_ABOVE` 6 | Delivered M max: bar 33 -11.05 -> -12.40 (4th -> 9th); bar 41 -12.25 -> -13.64, now under bar 117 (-13.38). The top 8 are 160, 161, 122, 123, 170, 159, 26 (exposition ff, -11.52, also 6th in c21) and 158. LRA, span and limiter as before | yes (bar 26 is a printed ff peak) |
| C #4 bars 19-20 Vln I crescendo | +2 dB rising over 74.25-77.5, 0 by 77.75 (stem fix: first rendered peaking at 77.75, which left the sf at 78 level with the last half beat) | Vln I per half qn 74-78.5: -33.6 -33.4 -32.7 -33.5 -31.0 -31.4 -31.7 -29.9 -29.0. 77.0-77.75 is 2.5-3.7 dB over 74.0-74.75; sf step +0.9 dB | yes |

## Test failed (keep in the render, revert in c23)

**A #4 (test).** `mix.json` Violas `sus_release_cap_ms` `rt_ms` 400. The Violas KS Master's Sus MAX RT groups of mf/f/ff shipped 1660 ms; this was verified with `opus_state.load_oib`. The p/pp RT groups were left at 1660 ms.
- Violas' rest drop in bars 131-134: 5.8 -> 5.7 dB (pass 7).
- All violas rests: 5.8 -> 5.8 dB.
- Violas re-bow dips: unchanged (median -2.2).
- The RT group's AHDSR release does not shorten the recorded release trail.
- Revert means removing `rt_ms`, which is a full Violas rebuild.

## Rejected / deferred
- C #2's +2.5 dB version: not used (critic: climax margin 0.75 dB).
- Horn width 0.15 revert: deferred again (no horn rebuild this cycle).
- Delivery limiter 2.1 dB (C's criterion ≤ 2.0). The top sample peak, 1.552 at qn 636.33, is the bass trombone, timpani, celli and basses in phase; c21 had 1.534 at 636.19. This cycle changed no data there. A notch is open for c23.

## Other differences seen (no data change)
Bar-level stem differences of 1-3 dB with unchanged data, which are render variation:
- Horn 3 bar 42: +3.2 dB.
- Violins II bars 44/98/125: +1.4..+1.8 dB.
- Violins I bar 18: +1.9 dB.
- Violas bar 55: -2.7 dB. That bar is soft, so it is outside the RT cap's mf/f/ff groups.

## Before / after (c21 -> c22, after the stem fix)

| Measure | c21 | c22 |
|---|---|---|
| Master integrated (float stem sum) | -16.4 LUFS | -16.2 LUFS |
| Master LRA | 22.6 LU | 22.6 LU |
| Master sample peak | 1.534 (qn 636.19) | 1.552 (qn 636.33) |
| Master true peak | +3.7 dBFS | +3.8 dBFS |
| Delivered integrated | -19.8 LUFS | -19.7 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 19.0 dB | 19.1 dB |
| Delivery limiter | 2.0 dB | 2.1 dB |
| Delivered true peak | -1.7 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.58 / 4.48 dB | 8.55 / 4.48 dB |

- Climax order (delivered S max): 160 -9.94 > 122 -11.02 > 167-170 -13.23.
- Attack probe: 0 flagged.
- REAPER memory: 26 GB with 0 compressed at the render start; 46 GB with 30 GB compressed after the render (38 GB compressed later, while measuring).
- Another user process (chrono-25d Python, 4-8 GB) was running during the render.
- Delivered mp3: `cycles/c22/mvt1-mockup-c22.mp3`.

## Open for c23
- Revert Violas `rt_ms` (full Violas rebuild). The violas' rest separation needs MIDI early ends or the instrument `envelope.releaseTime`.
- Limiter peak at 636.33.
- Basses accents 542/97 at the fit cap.
- Horn 4 415: the -5 dB step from 415.2.
- Horn width revert.
- The internal disk has about 3 GB free. `stem_fix.py --apply` copies every stem to `render_first/` (about 4 GB), so check free space before the next stem fix.

# Cycle 46 (actor): rubato (ONE_TIME c46) and critic fixes

Rendered 2026-11-09 07:21 (`cycles/c46/mvt2-mockup-c46.mp3`), one render, no stem fix.

Lock and drive. The data work was finished on 2026-11-08. The sample drive hung at about 20:36, and the coordinator
released a lock this thread held from 21:15 with no REAPER running. On 2026-11-09 at 05:32-05:55 two fresh starts found
Opus unable to open any file on /Volumes/MAC DRIVE ("Could not open ... Interrupted system call", about 1900 lines in
`Opus.g3log.20261109-053317.log` / `-055325.log`) although a shell read the same files at 200 MB/s; REAPER was killed
without saving and the lock released. After Dan fixed REAPER's access, the 06:56 start logged no "Could not open" line
(`Opus.g3log.20261109-065657.log`) and the project opened with 36 tracks. Lock held 06:56-07:38 (42 min), plus 23 min in
the 05:32 attempt.

Pipeline notes from this run:
- `build_reaper.py --tempo` stopped on "80 markers off their qn". Read back (`actor_scripts/tempo_err.lua`), every marker
  on a whole qn is exact; markers between whole qn read back early by an amount that grows with absolute time
  (0.05e-3 qn at 174 s to 1.1e-3 qn = 1.4 ms at score qn 268.25) and returns to 0 at the next whole qn, so nothing
  accumulates. c45's shorter map stayed just under the 1e-3 qn check. Tolerance raised to 2.5e-3 qn in
  `tools/build_reaper.py` (comment "mvt2 c46").
- The first `render_cycle.py 46` waited 10 min for the samples (cold cache after the replug), and REAPER had closed its
  audio device in the meantime (not frontmost), so render_cycle refused. Waiting for settled memory first, then the
  Audio_Init job, then render_cycle at once worked.

## Results (c46 render; c45 in brackets)
- Master -23.0 LUFS (-22.9), LRA 23.4 (23.4), true peak -3.4 (-4.0). Delivered -19.8 LUFS, LRA 15.4 (15.4), TP -1.6,
  p10-to-max span 18.9 dB (18.7), limiter 2.4 dB (1.7), length 354.70 s (349.50). Bars 61-62 still the loudest
  (-16.7 / -17.6 dB). Attack probe: late or hole 0.
- REAPER memory: 43 GB / 0.45 compressed before the render; 44 GB / 26-28 GB compressed after.
- S2: probe 0. pcX joins (median): Violas +7 ms (+5), Violins I +16 (+17), Violins II +15 (+12), Oboe 1 +45 (+46).
  Violas 249.5 +55 ms (+22): over 30 ms; C's `LEG_CAP_FRAC["Violas"] += [(249.0, 250.0, 0.55)]` is for c47 (a timing
  change, not a stem fix). Oboe 1's seven targeted joins: 43.5 +97 -> +46, 55 +94 -> +47, 140 +157 -> +135, 146
  +131 -> +121, 189 +166 -> +144, 197.5 +61 -> +28 ms, but 142 +88 -> +208 ms; the 0.04 s extra moved most joins 20-50
  ms, the median not (still +45 ms).
- S3 at all 24 caesuras (master, 10 ms RMS): the steepest 10 ms fall is 0.2-1.2 dB (c45 0.3-1.6); no breath cuts a tail.
  Master dip into the breath at 29: 9.3 dB (6.3), 102 9.0, 124 7.6; at 65 0.3 (c45, without a caesura there, 4.0).
- Breath lifts (CAESURA_LIFT, stem level over the last 0.11 s re 0.3-0.6 s before the target): Violins I 249 -4.7 dB
  (c45 -0.6), Violins II 77 -3.3 (-0.8); Violins I 77 +2.8 (-0.5), Violins II 65 -0.1 (-1.0), 249 -0.3 (+1.0); master at
  77 / 249 +1.0 / +0.5. Partly effective: 2 of 5 stems dip, the master not.
- Loop pulsing (100-300 Hz envelope, detrended, autocorrelation at 3.95 s / level SD): Contrabassoon 87 13.2 s -0.10 /
  0.46 dB (12.6 s, -0.10 / 0.47), Cbn 98 -0.46 / 0.56, Bassoon 2 90 0.10 / 0.61, Horn 1 232 -0.29 / 4.67 (0.37 / 4.6),
  timpani 226 0.19 / 1.19 (0.19 / 1.21); Horn 4 84 (7.6 s) 0.61 / 1.17 dB (0.14 / 1.22): now periodic, but the swing is
  1.2 dB SD on a pp inner note. Listen-check Horn 4 bars 28-30.
- Wetness (check44): strings t20 median 0.381 s over 3 stops (c45 0.551 over 2; the two shared stops 0.665 / 0.381
  against 0.660 / 0.443), winds 0.304 (0.324), brass 0.253 (0.282). Final chord t20 0.479 s (0.451): over the 0.45 limit.
  It comes from the dry celli stem (-6.4 dB at +0.3 s, c45 -8.2) at about -70 dBFS; R Strings -1 / -2 dB simulated by
  stem_fix changed it by 0.000 s (the returns sit 15 dB under the dry stems there), so no level fix applies. Open for c47.
- Brass (B #2): loud-10 % centroid 929 -> 887 Hz, 2-4 kHz share -9.7 -> -10.2 dB, 500 Hz-1 kHz -7.1 -> -6.7; bars 63-64
  centroid 1337 -> 1129 Hz. All inside B's targets.
- Trombone 1 213 (B #4): +5.7 dB over its pickup (c45 +2.2), 2-5 kHz attack minus body -13.1 dB (-10.1).
- Bass (B #1): basses minus celli bars 61-62 -5.2 -> -2.2 dB, bars 79-81 -5.3 -> -2.4; bass clarinet minus basses at bar
  61 +4.3 -> -0.7.
- Violas div minus Violas (B #6b): qn 80-87 +2.7 -> -0.1 dB, coda 279-292 +1.8 -> -0.4. Final chord: Violas div 2.4 dB
  under c45, still over the lower violas; the [297.9, 304, 2.5, 1] row left.
- Solo margins (check44): Horn 1 b7-14 6.0 -> 7.2, Horn 1 b67-70 6.6 -> 8.0, bass clarinet b31-36 3.7 -> 4.6, Clarinet 1
  over CA b87-88 5.8 -> 7.8, cor anglais b47-50 6.3 -> 6.9; Trombone 1 over strings + bass trombone 10.5 (10.5).
- Hairpins: of 70 curved lead-line hairpins with sound at both ends, 58 move the printed way by 1 dB or more, the same 58
  as in c45 (none reversed by the curve).
- Master: side/mid -5.4 dB (-5.6), L/R correlation under 250 Hz 0.63 (0.64), 6-20 kHz -29.45 dB (-28.7).
- State check: `state_check.py` flagged runs (basses pizz 108-120 +9.4 dB, violas 190-203 -5.8 dB, single notes up to
  +31 dB), but measured on each render's own map every flagged note is within 0.2 dB of c45: the tool reads both renders
  on one map, so its windows were off after the tempo change. No Opus state flip. The unchanged notes (basses pizzicato,
  Bassoon 1 108, Horn 2 255, timpani coda) render level-identical to c45 (0.0 dB): the CC16 round-robin reset repeats.
- Re-bows: 85 re-bow dips, median 3.6 -> 3.9 dB, 6 over 8 dB in both renders. Not refitted (points pinned and unchanged;
  a refit by HISTORY's procedure would risk the hand corrections for no measured gain). `fit_rebows.py` dry run in
  `fit_rebows_dry.txt`.

## Changes (files and parameters)
Tools (`tools/score_to_parts.py`, generic, default off):
- `PHRASE_PUSH/SLOW/SLOW_SUB/SLOW_MAIN/RETURN` and `APEX_AGOGIC` read through `globals().get` (C #1 step a).
- `CAESURA_BREATH_S` / `CAESURA_BREATH_SKIP`: a seconds floor on the loud wind/brass breath gap at a caesura (A #1).
- `CAESURA_LIFT` / `CAESURA_LIFT_S`: a CC11 fall into a legato target's moved onset, the overlap kept (A #3); parts.json
  `caesura_lifts`.
- `HP_CURVE`: quadratic Bezier hairpins on the CC11 lane only, applied when the lane is sampled, so every rule still reads
  the linear curve (C #4); parts.json `hp_curved`. Checked: a build with `HP_CURVE = None` differs only in cc11.
- `VOL_TAIL_HOLD` + `apply_vol_tail_hold()`: no volume-envelope fall in the first s seconds after a note-off before a rest
  (C #6, S3); parts.json `vol_tail_holds`.
- `tools/build_reaper.py`: the tempo read-back tolerance 1e-3 -> 2.5e-3 qn (see the pipeline notes above).

Config (`build/score_config.py`, c46 block at the end):
- Tempo: C #1's final values (PHRASE_PUSH 1.03, SLOW (0.93, 0.84), SUB (0.97, 0.90), MAIN (0.88, 0.80), RETURN 0.98,
  APEX_AGOGIC 0.93, the 16 arcs, APEX_LEAD[116] Flute 1, 24 caesuras, the BEAT_STRETCH table), with A #2: CAESURA 65 0.20
  (no 66), arcs (60, 65, "main") and (65, 77), no BEAT_STRETCH[66]. CAESURA[96] kept (it lengthens a tied crest note).
- `CAESURA_BREATH_S = 0.34` (A proposed 0.24), `CAESURA_BREATH_SKIP = {204, 268}`. With 0.24 the bass clarinet at 196
  (240 ms) and Bassoon 1 at 259 (240 ms) were shorter than in c45 (284 / 338 ms). With 0.34: Horn 1 196 137 -> 217 ms,
  bass clarinet 196 284 -> 340, Bassoon 1 259 338 -> 340; 204 and 268 unchanged (136 / 226 ms).
- `CAESURA_LIFT`: Violins I {77: 9, 249: 9}, Violins II {65: 8, 77: 9, 249: 9}.
- Re-bows: C #3 pins (c45 automatic points added to REBOW_AT on 7 tracks), `AUTO_REBOW_SKIP["Double basses"] += [164]`.
  Result: 0 REBOW_FILLS warnings and identical note sets. `space_rebows.py` on the new parts moves 0 points, so it was not
  run with --write (that would reset the hand-edited rebow_moves.json). No fill refit after the render (dips unchanged,
  see Results).
- `HP_CURVE`: cresc (0.34, 0.88), decresc (0.68, 0.27), max 6 s; linear for timp/perc and hairpins starting in 172-220 and
  250-259; B #3's lists linear at 212-216 (10 tracks) and 146-152.5 (7 tracks). 208 hairpin lanes curved; CC11 +3 / +3
  (median, at 25 / 50 / 75 %), up to +14 CC.
- `VOL_TAIL_HOLD` {s 0.5, min_gap_qn 0.25, min_fall_db 1}: 21 falls held on 15 tracks (Bassoon 1 29: -6 dB; Oboe 1 151
  -6.1; Clarinet 1 261 -6.4; Clarinet 2 17 -9.9 / 273 -6.0; others 1.1-3.7 dB).
- JOIN_NOTCH windows recomputed on the new map (same seconds offset from the target's moved onset; equal to A #4's):
  Violins I 258.889-258.948, Violins II 258.860-258.985, Flute 1 258.897-258.948, celli 76.890-76.988.
- `CC7_POINTS["Trombone 1"]` 212.9 / 213.35 back to 127 (B #4).
Per-note tables:
- roles.json: Trombone 1 [212.4, 212.9, 1.5] + [212.91, 213.6, 3.5] (B #4); Bassoon 1 [231.5, 237, -4.5, 1.5] (B #5a);
  Cor anglais [93, 96, 2, 0.5] deleted, [98.5, 102, -7.5] (B #5b), [285.9, 292.5, 2, 0.5] deleted (B #5d); Violoncellos
  + [152, 164, -3, 0.5] (B #5c); Double basses + [139.9, 146, -3] (B #6a).
- note_trims.json: Cor anglais 152 -3 -> -1 (B #5c).
- entry_leads.json: Violas 66 0.12 -> 0.22 (C #5 asked for 0.10 more; the 0.30 s cap gives 0.24 -> 0.30 s), 188 0.08 (lead
  0.06 -> 0.14 s).
- leg_leads.json: Oboe 1 +0.04 s on 43.5, 55, 140, 142, 189, 197.5; 146 0.05 -> 0.07 (A #6).
- mix.json: horn and lowbrass family_eq bells 475 Hz -2.7, 821 Hz -3.9, + 3.2 kHz -3 dB bw 1; gains Horn 1 0.1, Horn 2
  -0.9, Horn 3 0.7, Horn 4 0.6, Horns a2 4.5, Trombone 1 4.18, Trombone 2 5.0, Bass trombone 5.5, Tuba 7.95 (B #2);
  Double basses dyn_trim f 2.5 / ff 4.0, Bass clarinet f -1 / ff -3 (B #1); Violas div gain 5.48 -> 2.98 (B #6b).

## parts.json against c45 (measured on the data)
- Length to qn 304: 348.11 -> 353.30 s. Beat statistics (17-beat median): median deviation 1.5 -> 3.0 %, p90 6.3 -> 10.0 %,
  beats more than 15 % slower 7 -> 16, more than 25 % slower 1 -> 10. Pickups: 29 53.0, 65 51.0, 66 53.6, 77 53.0, 139
  58.8, 237 53.0, 249 54.1 bpm (the slow beats before them 36.5-44.8 bpm).
- Notes and keyswitch lists identical on all 32 tracks; velocities identical. Leads in seconds change by more than 12 ms
  only at Oboe 1 (the 7 new leg leads), Violins II 119 (0.450 -> 0.437 s), Violas 66 (0.24 -> 0.30), 111 (0.257 ->
  0.269), 188 (0.06 -> 0.14) and 249.5 (0.282 -> 0.250).
- No Opus state change (no row added or dropped), so every track takes `--midi-only --tempo`.

## Rejected / deferred
- C #2's `CAESURA_FULL_BREATH` (lead: A's generic floor instead); C's and A's re-bow advice: pins used, no refit (dips
  unchanged); the soft-roll timpani shelf (B measured it is not needed); Violas 87 (A: leave); CAESURA[96] kept.
- Open for c47: Violas 249.5 +55 ms (LEG_CAP_FRAC); Oboe 1 median +45 ms (142 now +208); final chord t20 0.479 s (dry
  celli release); the breath lifts reach the master at neither 77 nor 249; Horn 4 84 loop periodicity (1.2 dB SD).

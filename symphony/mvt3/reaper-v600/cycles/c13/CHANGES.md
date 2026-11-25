# Cycle 13 changes (actor, 2026-11-09)

Scripts: `cycles/c13/actor_scripts/` (`pn.py`, `statecmp.py`, `ksgaps.py`, `voldiff.py`, `sim13.py`, `stops13.py`,
`kstest.py`, `padrange.py`, `precheck.sh`, `drift13.py`, `post13.py`, `wait_lock.py`, `settle.py`, `phase1.sh`, `phase2.sh`,
`after_render.sh`). Logs: `cycles/c13/logs/`. Snapshot of the tools and tables before the cycle:
`cycles/c13/before/`. Builds: `build/parts.json` (rendered: `KS_LEAD_S = None`, bar 75 lead rows refitted),
`cycles/c13/parts_kslead.json` (the build with `KS_LEAD_S = 0.045` that the range test rejected),
`cycles/c13/parts_nolead.json` (the rendered build before the bar 75 refit), `cycles/c12/final_build/` (the c12 data all
comparisons use).

Two score changes arrived from the coordinator during the cycle and are in the rendered build (LilyPond run at 20:24 on
score commit a56b9ee9, parts.json built from that MIDI):
- bar 75 (qn 296-300), Violins I and II: dotted half, then two slurred eighths on beat 4 (Bb, G, Ab; Violins II an
  octave lower). No note at 298.0 or 298.5 any more.
- bar 150 beat 4 (qn 599.0): the D pickup is removed in Bass clarinet, Contrabassoon, Tuba, Violoncellos and Double
  basses. No config row referred to that note. Side effects in the data: the cc11 lanes of the five tracks differ from
  c12 by up to 7 around bar 150, and the volume envelope is higher than c12 from the removed note's onset to the track's
  next note (Bass clarinet +1.0 dB over qn 598.89-678.99, Tuba +0.5 dB over 598.89-631.11), because the pickup's own
  note trim is gone. Only the release of the G at 599.0 sounds inside those spans.

  One row was added for it: `ROW_LEAD_KEEP_END` Violoncellos "Sus MAX" (591.9, 592.1). With the pickup gone, the celli's
  led chord at 592 would have ended at 598.776 (early by its lead); with the row it ends at 598.886 with the other
  strings. The celli's chord at 600 now has velocity 91 (c12 105), because the divisi-entry rule applies only to a
  chord entered from an abutting note. LilyPond also wrote `build/mockup.pdf` (new file in the work folder).

parts.json against c12: 0 warnings; no track's Opus state inputs change (`statecmp.py`), so no full rebuild.

## What changed

### Tools

1. `tools/deliver_master.py`: `RISE_DELAY_S` (critic C #1 fix A). The ride gain at time t is the lower of its value at t
   and at t - RISE_DELAY_S, so gain rises run late and gain falls stay on time. Default 0 (off); set per score in
   mix.json `"deliver": {"rise_delay_s": ...}`; environment override `DELIVER_RISE_DELAY_S`.
2. `tools/score_to_parts.py`:
   - `KS_LEAD_S` (seconds, default None = the old 0.06 qn rule) and `KS_AFTER_PREV_ON_S = 0.005` (critic A #3). A
     keyswitch that is not placed in a rest goes KS_LEAD_S before the moved note-on of its note and not earlier than
     5 ms after the track's previous note-on. A keyswitch in a rest stays there and is at least KS_LEAD_S before the
     note-on. A keyswitch to a non-legato row that would fall inside a sounding legato-row note keeps its old time, so
     the keyswitch-cut rule shortens no note; the re-bow back keyswitch is not doubled.
   - `RR_RESET_AT` now also acts on percussion tracks (`build_perc_track`); a qn without a stroke is sent as given.
   - `ROW_SLUR_OVERLAP_S` values may be a list of `(from_qn, to_qn, seconds)` spans (first match wins); 0.0 in a span
     ends the note before exactly at the moved onset.
   - `LEG_RAMP_OK = {track: [score qn]}`: level-shape rows meant to act inside a listed legato target's transition are
     not reported by `LEG_RAMP_WARN`.
3. No change in `build_reaper.py`, `render_cycle.py`, `stem_fix.py`, `state_guard.py`, `measure.py`,
   `probe_attacks.py`.

### Config (`build/score_config.py` c13 block, `build/roles.json`, `build/leg_leads.json`, `build/mix.json`)

1. Bassoon 1 solo, qn 456-488 (A #1, B #3). Four `LEVEL_SHAPES` rows: 458.9-461.0 +4.5 dB; 461.9-463.0 -2.5 dB;
   471.9-476.0 -3 dB then +6 dB; 478.9-486.0 +3 / -5 / -2 / +3 dB. One `LEVEL_SHAPES_S` row at 464.0:
   `[(-0.14, 0), (-0.10, 5), (0.10, 5), (0.22, 2), (0.30, 0)]`, with `LEG_RAMP_OK = {"Bassoon 1": [464.0]}`. The 150 ms
   lead at 464 is kept.
2. Timpani fff rolls (B #1). `LEVEL_SHAPES_S` at 888.0 `[(0.20, 0), (0.45, 5), (1.95, 5), (2.08, 0)]` and at 1108.0
   `[(0.30, 0), (0.50, 4), (1.95, 4), (2.09, 0)]`. The first strokes are outside both rows.
3. Horn 1 p theme, bars 139-140 (B #2). `LEVEL_SHAPES_S` at 552.0 `[(-0.14, 0), (-0.12, 14), (0.63, 14), (0.72, 0)]`,
   at 556.0 `[(-0.03, 0), (-0.01, -8), (0.19, -8), (0.23, 0)]`, at 558.0 `[(-0.03, 0), (-0.01, -4.5), (0.55, -4.5),
   (0.60, 0)]` (one row for the notes at 558 and 559). Two deviations from B, both measured on the c12 stem: +14 dB
   instead of +10 (the note read -56.0 dB, 12 dB under the second note, so +10 left it 3.6 dB under the others), and
   the fall placed at 0.63-0.72 s, under the rise of the next note, because an earlier fall made a dip before the
   slurred 554. No velocity-table change.
4. Stop margin (C #1, B #5).
   - Fix A: mix.json `"deliver": {"rise_delay_s": 0.6}`.
   - Fix B: `POST_SHAPES_S` release fades of -6 dB. Violoncellos at 5.0 `[(0.08, 0), (0.40, -6), (1.20, -6),
     (1.32, 0)]`, 21.0 `[(0.08, 0), (0.40, -6), (0.72, -6), (0.81, 0)]`, 374.0 `[(0.03, 0), (0.35, -6), (0.42, -6),
     (0.47, 0)]`; Double basses at 5.0 and 21.0 `[(0.08, 0), (0.40, -6), (1.50, -6), (1.70, 0)]`, 374.0 `[(0.03, 0),
     (0.35, -6), (0.55, -6), (0.62, 0)]`. Every row is back at 0 dB before the track's next entry. B's `LEVEL_SHAPES_S`
     rows at 4.0 and 20.0 were not added. Returns and master_eq are unchanged.
5. Low end in bars 255-256. Double basses `LEVEL_SHAPES` `[(1015.5, 0), (1016.0, 2.5), (1024.0, 2.5), (1024.5, 0)]`;
   roles.json Bass trombone `[1016, 1032, -3.0]` -> `[1024, 1032, -3.0]`. No tuba change.
6. Crash cymbals at bar 263 (A #4, C #4). roles.json "Crash cymbals" `[[1046, 1060, -3.0]]` deleted;
   `RR_RESET_AT["Crash cymbals"] = [887.5, 1047.5, 1107.5]` (CC16 127, half a quarter before each of the three
   strokes). The patch "22in Zildjian K Crash.oib" has the groups "Long RRx1/2/3".
7. Muted Trumpet 1, qn 680-744 (A #2). `ROW_SLUR_OVERLAP_S["Trumpet 1"]["Mute Sus"]` as spans: 0.03 s at 685, 691,
   717, 725; 0.06 s at 687, 692, 694, 719, 726; 0.02 s at 688, 723; 0.0 for the rest of 680-744.
   `ROW_LEAD_S["Trumpet 1"]["Mute Sus"]`: 0.085 s at 687, 692, 694, 719, 726; 0.065 s at 723; 0.035 s elsewhere.
   Flutter and the per-bar roles at 680-732 are unchanged.
8. Solo returns (C #2, C #3), mix.json: "Bassoon 1" `"return": {"to": "R Winds", "db": -8.0}` (was none); "Trumpet 1"
   return -10.0 -> -8.0 dB (C asked -6.5; -8.0 is the coordinator's value). No other send or return fader changed.
9. Small items:
   - leg_leads.json Flute 2 618.0 0.12 -> 0.03 and 650.0 0.17 -> 0.03.
   - Violins I "4 soli" at 485: `LEVEL_SHAPES_S` `(485.0, [(-0.14, 0), (-0.12, 4), (0.12, 4), (0.18, 0)])`.
   - `RR_RESET_AT` at the pizzicato entry: Violoncellos and Double basses 200.0, Violins II and Violas 201.0.
   - roles.json Flute 1 `[404, 408, 1.5]`.
10. Keyswitch lead (A #3): tested with `KS_LEAD_S = 0.045` and rejected by the range test (below); the rendered
    build has `KS_LEAD_S = None` (the 0.06 qn rule). A's Violins II 152 group is kept without it: `DOWNBOW_STROKE_AT` + 152.0,
    `ROW_LEAD_KEEP_END` "Sus MAX" (151.9, 152.1), `ROW_LEAD_S` "Sus MAX" (151.9, 152.1, 0.07), `NOTE_END_AT` 151.5 ->
    151.636. A's `ART_SPANS` form broke the slur from 152 into 154, so the stroke is made with `DOWNBOW_STROKE_AT`.
    Moving the note at 152 to another row took the -4 dB `ROW_TRIM` off the ff eighths at 148.5-150.0 (volume-envelope
    diff +4.0 dB over 148.31-150.36); a `LEVEL_SHAPES` row `[(148.302, 0), (148.362, -4), (150.302, -4), (150.362, 0)]`
    gives it back, so the envelope differs from c12 only over 151.76-152.18 (+4.0 dB).

Volume-envelope diff of the rendered build against c12 (`logs/voldiff_final.log`): Flute 1 404.13-415.87 +1.5; Flute 2
617.13-617.49 and 649.04-649.49 -5.0 (the moved lead dips); Bass clarinet and Tuba as described above; Bassoon 1, Horn 1,
Timpani, Violins I, Violoncellos, Double basses as listed; Bass trombone 1015.63-1023.99 +3.0; Crash cymbals
1045.63-1060.49 +3.0; Violins II 151.76-152.18 +4.0. No other track differs.

### Not taken, rejected or deferred

- A's `STR_REP_AFTER_STAC` change: tried in a scratch build; no note changes row, so it is not applied.
- B's `LEVEL_SHAPES_S` rows at 4.0 and 20.0 (coordinator: not on top of fix B).
- Crash cymbals +3.5 dB shape at 1048 (coordinator: not this cycle).
- Item 11 (B's ride hold over bars 42-50): not done.
- The low-wind swell cap from the other movements would act only on the bass clarinet in 680-744: not taken.
- C #5 (R Winds irSetup 0.5 -> 0.43) and C #6 (Mid mic on cor anglais): c14.
- No trims against drifted single notes (Violoncellos 100 and 1009, Horn 1 570, Flute 1 423).

## Measured before the render (simulation on the c12 stems, `stem_fix.py --out`, `sim13.py`, `stops13.py`)

Item 1, Bassoon 1, highest 100 ms level per note (dBFS, c12 -> simulated): 459 -52.2 -> -47.7; 460 -52.1 -> -47.6; 462
-42.7 -> -45.2; 472 -42.8 -> -45.8; 475 -52.9 -> -46.9; 479 -51.0 -> -48.0; 480 -41.4 -> -46.4; 482 -44.2 -> -46.2; 484
-51.4 -> -48.4. Unchanged: 456 -44.6, 461 -46.9, 463 -46.9, 464 -44.0, 466 -47.9, 467 -49.2, 468 -49.8, 470 -46.9, 476
-44.8, 477 -48.7, 478 -49.5. The A4 at 464 is the loudest note of 456-470. Outside -47 +-2.5 dB: 464 (the printed mp)
and 468 (-49.8, 0.3 dB outside, inside the printed decrescendo; left). Lowest 50 ms window around 464: -49.4 dBFS (c12
-54.4; limit -51).

Item 2, Timpani stem, 250 ms windows: bar 223 -28.3 -29.6 -32.5 -33.1 -34.0 -35.0 -36.0 -36.0 (index at 127 Hz -10.2
-> -5.2 dB); bar 278 -30.5 -32.1 -30.0 -31.6 -31.7 -28.7 -31.3 -32.0 -35.5 (index at 160 Hz -3.0 -> +1.0 dB on my
scale, which reads about 4 dB higher than B's). Master float peak unchanged (1.014 at 420.95 s).

Item 3, Horn 1 stem means (dBFS): 552 -56.0 -> -42.0; 554 -43.2 -> -42.3; 555.5 -45.1; 556 -35.9 -> -43.9; 557 -44.5;
557.5 -44.5; 558 -39.5 -> -44.0; 559 -40.3 -> -44.8. mp3 window 556.0-556.5: 1.0-2.0 dB over the four windows before.

Item 4, stops (drop at +0.3 s in dB / time to -20 dB in s):

| stop | c12 master | c12 mp3 | fix A only, mp3 | A and B, master | A and B, mp3 |
|---|---|---|---|---|---|
| bar 2 | 14.0 / 0.43 | 12.3 / 0.49 | 13.0 / 0.46 | 16.5 / 0.36 | 15.2 / 0.42 |
| bar 6 | 15.0 / 0.42 | 13.4 / 0.44 | 13.9 / 0.44 | 17.0 / 0.36 | 15.6 / 0.38 |
| bar 94 | 12.9 / 0.40 | 12.3 / 0.41 | 12.8 / 0.41 | 15.9 / 0.36 | 15.9 / 0.37 |
| bar 113 | 19.1 / 0.31 | 17.2 / 0.36 | 18.0 / 0.32 | | 18.0 / 0.32 |
| bar 166 | 15.1 / 0.39 | 14.2 / 0.39 | | | 14.7 / 0.39 |
| bar 204 | 14.6 / 0.45 | 14.1 / 0.45 | | | 14.1 / 0.45 |
| final chord | 14.5 / 0.45, RT60 1.30 | 14.4 / 0.47, RT60 1.43 | | | 15.4 / 0.43, RT60 1.34 |

Item 5, 31.5-125 Hz share of the master (dB): bar 254 -14.1; bar 255 -22.3 -> -20.5; bar 256 -20.8 -> -19.2; bar 257
-17.3. Step from bar 254 to 255: 6.4 dB (target 6 or less; closed by the coordinator whatever the result).

Item 6 (level part only): crash at 1048, first 0.5 s -29.8 -> -26.8 dBFS. Item 9: Violins I 485 first eighth -71.1 ->
-67.9 dBFS; Flute 1 in bar 102 against the master without it -1.2 -> +0.3 dB.

Delivery of the simulated master: -19.8 LUFS, LRA 14.7 LU, TP -1.5 dBTP, limiter about 2.5 dB, ride maximum +12.2 dB.

Item 8, calibration of "solo alone" on the c12 stems (`post13.py returns`): absolute 0.5 s grid; a frame counts when the
soloist is over -57 dBFS and every other track of its family is under -80 dBFS; the figure is the return's energy re
the stem's over those frames. c12: Bassoon 1 alone in 17 of 23 frames (C: 16 of 24; R Winds is silent there);
Trumpet 1 qn 680-744 24 of 47 frames, -16.1 dB (C: 23 of 47, -16.4); qn 200-264 52 of 55 frames, -15.3 dB (C: 50 of
53, -15.1). C's counts are not reproduced exactly by a plain half-second grid; the levels agree within 0.3 dB.
Expected with -8.0 dB on Trumpet 1: about -14.1 and -13.3 dB, which is outside C's 11.5-13 dB target (C asked -6.5).
Estimate of the conditions from the c12 stems and the send gains (return inputs): bars 1-2 R Winds 100-250 Hz +0.05 dB,
R Brass +0.00 dB; bars 112-113 R Winds 100-250 Hz +1.08 dB, R Brass +0.71 dB.

Item 9, Flute 2 at 618 and 650: critic A's measure (harmonic envelopes, new pitch within 6 dB of its body) and critic
C's (perceived onset, `tools/pcx.py`) disagree in sign on these joins. On c12 my `j6` gives A's numbers (new pitch in at
-78 / -186 ms, two pitches together 111 / 147 ms) and `pc` gives C's (+49 / +114 ms). With the rows at 0.03 the lead is
0.19 s (c12 0.28 / 0.33 s), close to the 0.16 s of the joins at 602 and 634, which neither critic flagged (c12: `j6`
-10 / -9 ms, `pc` +48 / +49 ms; Flute 1 `j6` -45 ms). The coordinator's value is kept; both measures are reported
after the render.

Lock: `reaper_lock.acquire` keeps no queue, and the other folders' waiters restart every few minutes, so process age
does not show who has waited longest. `actor_scripts/wait_lock.py` takes the lock only when it is free and no folder
that was already waiting when it started is still ahead.

## Lock period, before the render (2026-11-10)

The actor was stopped by a usage limit at 22:15 on 2026-11-09 while waiting; so was Movement II's actor, which held the
lock from 20:53 to 05:53. The waiter was restarted at 05:07, the Scherzo went first (05:53-06:41), and Movement III
locked at 06:41:32.

Item 10, range test (`kstest.py`, `logs/kstest_compare.log`; ranges qn 28-64, 88-134, 408-430, 984-1016; two renders
of the project as saved by c12, R0a and R0b, then two of the `KS_LEAD_S = 0.045` build, R1a and R1b):
- Check (a) failed. The c12 "drifted" notes are two-valued from one render to the next on the same data. Flute 1 423
  read +4.3 dB against c12 in R0a and 0.0 in R0b, Violins I 42 0.0 and -3.7, Horn 3 119 -3.9 and 0.0, Violoncellos 100
  0.0 and -3.9, Double basses 114 0.0 and -5.1. With the lead they keep doing it (Flute 1 423 +4.3 / 0.0, Horn 3 119
  0.0 / -3.9, Violas 131 +2.4 / +0.4). Of the 15 listed notes, 5 were at the c11 value (within 1 dB) in both R1 renders, 3 in both
  R0 renders, and 4 in none of the four. The lead does not fix them.
- Check (b) failed for both builds, so it does not separate them: of 375 other long notes on equal data, 38 and 40
  were more than 0.5 dB from c12 in R0a / R0b, 58 and 52 in R1a / R1b (over 2 dB: 2, 6, 9, 7). R0b minus R0a: 36 notes
  over 0.5 dB (5th / 95th percentile -0.35 / +0.49 dB); R1b minus R1a: 12 (-0.06 / +0.14 dB). One note was changed by
  the lead in both renders (Violas 115 -4.0 dB).
- Result: `KS_LEAD_S = None`, as the task rules. The option stays in `score_to_parts.py`. The drift is not a
  keyswitch-timing effect.

Pre-check of the changed passages on range renders (`precheck.sh X1`, ranges qn 140-158, 284-304, 583-654, 661-746, on
the `KS_LEAD_S = 0.045` build; `logs/precheck_X1.log`), and a second one after the revert (X2: 140-158 and 284-304,
`logs/precheck_X2_post13.log`):
- Violins II 152: the hole is gone with and without the keyswitch lead (the same numbers in X1 and X2): lowest 50 ms
  level around the note -50.7 dBFS (c12 -67.6 at +170 ms), body 152.5-153.5 -32.5 dBFS (c12 -54.2), perceived onset
  +57 ms (c12 +270).
- Bar 75, Violins I: with the old row (299: +0.081 s) the G's note-on was 264 ms before the beat and it read 59 ms
  early (perceived onset; per-pitch crossing -26 ms), the A flat +43 ms (+62), the F at 300 +95 ms (+168). Rows changed
  once: leg_leads.json Violins I 299 0.081 -> 0.03, new 299.5 0.045 and 300 0.09 (both end at the 0.45 qn cap: note-ons
  -213 / -188 / -188 ms). X2 then read -101 / +13 / -8 ms (crossing -69 / +31 / +47 ms). The same unchanged note at
  296 read +84 ms in X1 and +38 ms in X2, so these measures move by about 50 ms between two renders and a row cannot be
  fitted to 20 ms on them. No further change. Violins II (velocity 73 eighths, fixed 60 ms lead; rows have no effect
  there) read -23 / +43 / +24 ms in X1 and -23 / +43 / +21 ms in X2: left as it is.
- Trumpet 1 and the flutes: values as in the full render (below).

State guard (Movement I c53): after the range renders, `reaper_ctl.py save` stored 20 ms legato attacks on two tracks
(`state_guard_1.log`: Trombone 2 12 attacks, Double basses 8). Both were rebuilt in full (`build3_full.log`), the
project was saved again and the guard read 0 stale (`state_guard.log`) before the restart.

Builds in REAPER, in order: `build1.log` (`--midi-only`, all tracks, `KS_LEAD_S = 0.045`), `build2.log` (`--midi-only`,
all tracks, the rendered data), `build3_full.log` (Trombone 2, Double basses, full).

## After the render (`render.log`, `metrics/`, `logs/render/`; c12 values by the same scripts in brackets)

Render: 35 stems and the master, no clipping (float peak 0.992 at 420.97 s, true peak -0.1 dBFS; the master is REAPER's
own, not the stem sum), attack probe 0 flags (c12: 1). Master -20.6 LUFS, LRA 23.0. Delivered mp3 -19.8 LUFS, LRA
14.6 LU, true peak -1.5 dBTP, limiter about 2.3 dB (2.6), span 19.1 dB, ride +12.2 / -2.1 dB. mp3 bars 41 -> 42 step
9.2 dB (9.7).

Stops (`stops13.log`; drop at +0.3 s / time to -20 dB):

| | bar 2 | bar 6 | bar 94 | bar 113 | bar 166 | bar 204 | final chord, RT60 (-5..-35 / -5..-25) |
|---|---|---|---|---|---|---|---|
| mp3 c13 | 15.7 dB / 0.39 s | 16.1 / 0.38 | 17.4 / 0.33 | 19.7 / 0.29 | 19.5 / 0.31 | 14.2 / 0.45 | 0.43 s; 1.33 / 1.51 s |
| mp3 c12 | 12.3 / 0.49 | 13.4 / 0.44 | 12.3 / 0.41 | 17.2 / 0.36 | 14.2 / 0.39 | 14.1 / 0.45 | 0.47 s; 1.43 / 1.59 s |
| master c13 | 16.8 / 0.36 | 17.5 / 0.35 | 17.3 / 0.32 | 20.4 / 0.28 | 21.7 / 0.30 | 14.5 / 0.45 | 0.46 s; 1.30 / 1.48 s |
| master c12 | 14.0 / 0.43 | 15.0 / 0.42 | 12.9 / 0.40 | 19.1 / 0.31 | 15.1 / 0.39 | 14.6 / 0.45 | 0.45 s; 1.30 / 1.47 s |
| c13 without the two sends | 16.6 / 0.36 | 17.2 / 0.35 | 17.3 / 0.32 | 19.2 / 0.31 | 21.2 / 0.30 | 14.6 / 0.45 | 0.45 s |

Every stop is under the 0.50 s ceiling and the final chord under 1.5 s on the -5..-35 dB fit (1.51 s on the -5..-25 dB
fit). The master falls 17.5 and 17.3 dB in 0.3 s at bars 6 and 94, 0.3-0.5 dB past the 17 dB limit of item 4; bar 166
changed without a config change there (15.1 -> 21.7 dB; the basses' levels in bars 162-164 moved with the new
round-robin reset, see the drift check).

Items:
1. Bassoon 1 (highest 100 ms per note): 459 / 460 -52.2 / -52.1 -> -47.7 / -47.6, 462 -42.7 -> -45.2, 472 -42.8 ->
   -45.8. Range of the p notes -49.8 to -44.0 dB; outside -47 +-2.5: 464 (-44.0, the note meant to be loudest, and it is
   the loudest of 456-470) and 468 (-49.8). 50 ms windows around 464: lowest -49.4 dBFS (c12 -54.4).
2. Timpani: bar 223 stem 250 ms windows -28.3 -29.6 -32.5 -33.1 -34.0 -35.0 -36.0 -36.0 (c12 -28.4 -32.8 -37.5 ...
   -40.8), index at 127 Hz -5.7 dB (-10.2); bar 278 body -30.0 to -32.1 dBFS, index at 160 Hz +0.3 dB (-3.0). First
   strokes unchanged; master peak there -0.07 dBFS (c12 +0.12).
3. Horn 1 note means: 552 -56.0 -> -42.0, 554 -42.3, 555.5 -45.1, 556 -35.9 -> -43.9, 557 -44.7, 557.5 -44.7, 558
   -39.5 -> -43.9, 559 -40.3 -> -44.8: all within 2 dB of -44, the first note 0.3 dB over the second. Master window
   556.0-556.5 -40.3 dBFS, 1.2 dB over the four windows before it (c12 +6.9).
4. Stops: table above. mp3 bar 2 15.7 dB and 0.39 s (targets 14 dB, 0.46 s); final chord RT60 1.33 s (target 1.35).
5. 31.5-125 Hz share: bar 255 -22.3 -> -20.2 dB, bar 256 -20.8 -> -19.2 dB; steps from bar 254 (-14.2) 6.0 and 5.0 dB.
   Closed.
6. Crash cymbals, first 0.5 s: 888 -26.5, 1048 -26.8 (c12 -29.8), 1108 -26.8 (c12 -27.1) dBFS; 4-12 kHz band of the
   three strokes within 0.4 dB of each other (c12 3.4 dB apart). The stroke at 1048 is the c12 sample 3.0 dB louder (the
   deleted role); the reset changed the stroke at 1108 by 0.3-0.4 dB. Limiter 2.3 dB, so the row stays deleted.
7. Trumpet 1 "Mute Sus" (`joins6b.py`, 18 joins it can measure): two pitches together median 50 ms, highest 96 ms, over
   60 ms at 8 joins (c12 by the same run: 55, 144, 9); the crossing is within 30 ms of the beat at 8 of 18 (c12 4).
   Target not met: 684, 686, 716, 718 (85-87 ms, crossing +58..+62 ms), 715 (96), 728 (91), 690 (69), 694 (62) stay
   over 60 ms with an overlap of 0.0 or 0.06 s; the sample's release holds the old pitch. Next: end the note before
   20-30 ms ahead of these joins and lead them by a further 30 ms.
8. Solo returns. Conditions: stops at bars 2, 6, 113 with the sends 0.36 / 0.35 / 0.28 s, without them 0.36 / 0.35 /
   0.31 s (not longer); R Winds 100-250 Hz in bars 1-2 +0.13 dB (limit 1.0); R Brass in bars 1-2 0.00 dB (limit 1.5).
   No fallback needed. Levels in the solo-alone frames: R Winds 9.9 dB under the Bassoon 1 stem (C's target 11-13: 1.1
   dB too wet; a send of -9.5 to -10 dB would meet it); Trumpet 1's return 14.0 dB under its stem in 680-744 (c12 16.1)
   and 13.3 dB in 200-264 (c12 15.3), against C's 11.5-13 (C asked for -6.5 dB). The Bassoon 1 send does not make C #5
   necessary: R Winds in bars 1-2 and the stop times are unchanged.
9. Flute 2 at 618 / 650 (rows 0.03): not met. Perceived onset +149 / +172 ms (c12 +49 / +114), Flute 2 minus Flute 1
   120 / 223 ms (c12 127 / 165); per-pitch measure new pitch in at -58 / -133 ms (c12 -78 / -186), two pitches together
   120 / 161 ms. The joins at 634 moved on unchanged data (Flute 2 +49 -> +1 ms; per pitch -9 -> +109 ms), so these
   joins are not stable from render to render. Violins I 485: first note -71.1 -> -67.9 dB. Flute 1 against the master
   without it in bar 102: -1.2 -> +0.3 dB. Pizzicato resets: in the data (CC16 at 199.9-200.9); see the drift check.
10. Keyswitch lead: not in the render (range test above). Violins II 152: lowest 50 ms level -50.6 dBFS (c12 -67.6),
    body -32.5 dBFS (c12 -54.2), perceived onset +57 ms (c12 +270); the next note at 154 reads +107 ms (c12 -99).

Drift check (`drift13.py --noks`, threshold 2 dB, qn 296-300.5 skipped; `logs/render/drift13.log`): target of under 10
notes not met. On the 27 tracks without a new reset 25 long notes moved by 2 dB or more on unchanged data (c12: 35 on
all tracks); 9 of them are c12-list notes back at their c11 level, 16 are new. Bassoon 2, the clarinets, cor anglais,
Horn 4, Trumpets 2 and 3, Trombone 2, Tuba, Timpani and harp have none. On the four tracks with the new pizzicato reset
73 notes after qn 200 moved (Double basses 52, up to +9.6 dB on single notes; 16 basses' bars over 2 dB), which is the
reset's effect on every later round-robin choice of those tracks, not drift. The master on the 201 bars without any
data change: median 0.00, 5th / 95th percentile -0.39 / +0.40 dB, no bar off by 1 dB.
The four notes named by the coordinator: Violoncellos 100 unchanged against c12 (still +3.9 dB over c11), Violoncellos
1009 -5.7 dB (back at the c11 level), Horn 1 570 unchanged (still +6.1 over c11), Flute 1 423 unchanged (still 4.3
under c11). Together with the range test (the same project rendered twice gives two levels on these notes) this points
at round-robin position, not at keyswitch timing. Proposed for c14: a CC16 reset in the pre-roll of every track, and
the test "two range renders in a row are equal".

Bar 75 (Violins I / II, dotted half, two slurred eighths on beat 4): rendered with the new rhythm. Violins I note-ons
296.0 -278 ms, 299.0 -213 ms, 299.5 -188 ms, 300.0 -188 ms re the grid. Time at which each pitch becomes the loudest
(`bar75_own.py`, harmonic envelopes): Violins I G -61 ms, A flat +45 ms, F (300.0) +43 ms; Violins II G +15 ms, A flat
+35 ms, F -43 ms. Perceived onset (`pcx`): Violins I 296.0 +10, 299.0 -101, 299.5 +13, 300.0 -6 ms; Violins II +96,
+11, +30, -64 ms. Each eighth as its own pitch: Violins I G 314 ms and A flat 206 ms of 208 ms; Violins II G 228 ms,
A flat 130 ms (62 %). None is under 50 %. Violins I's G is early by 61-101 ms and was not refitted further (the two
measures moved by about 50 ms between two renders of the same data).

Bar 150: no note at qn 599.0 on Bass clarinet, Contrabassoon, Tuba, Violoncellos, Double basses (parts.json and
stems). Release at 599.0 on the master: -10 dB at +98 ms, -20 dB at +318 ms, lowest -40.6 dBFS at +326 ms (c12 -31.4
with the pickup); no click (master 4-12 kHz +0.4 dB at the release against the band before). Stems: Bass clarinet -20
dB at +142 ms, Tuba +136, Contrabassoon +188, Violoncellos +68, Bass trombone +146, Bassoons +168 / +244, Timpani +240
ms; the Double basses fall 19 dB by +324 ms. The G at 600.0: Contrabassoon perceived onset -37 ms, first 0.3 s -41.1
dBFS, gap from its -20 dB point 0.223 s; Violoncellos -14 ms, -32.6 dBFS, gap 0.366 s; Double basses -15 ms, -35.0
dBFS. Master 50 ms levels from 599.0: -21 -24 -28 -30 -32 -34 -37 -39 -36 -29 (the entry) -24 -22.

REAPER memory: 44 GB settled with 0 GB compressed before the render (after the first open of the lock period 44 GB with
30 GB compressed), 45 GB after the render. State guard on the project saved at quit: 0 stale.
Lock: 06:41:32 to 07:44:25, 63 minutes (start and open 1 min, first settle 14 min, range renders and builds 21 min,
restart and settle 13 min, render 10 min, measurements and quit 3 min).
Disk: the c12 stems, `cycles/c12/render_first` and the range-render WAVs are deleted; 40 GB free.

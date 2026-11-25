# Cycle 12: changes (actor, on the c11 render)

Snapshot of the tables and tools before this cycle: `cycles/c12/before/`. Scripts: `cycles/c12/actor_scripts/`
(`apply12.py` table edits; `check12.py CYCLE [PARTS] [block ...]` the per-finding measurements, blocks `bar56 timp harp
joins brass pick c6 rebow fl1 hn3 notch v2dip ob retongue open hall`; `acc12.py CYCLE` front against body of the
accented half notes; `ot12.py CYCLE [width|sfp|bass|low8]` ONE_TIME measurements; `rep12.py CYCLE [PARTS]` repeated-note
dips by class; `trims12.py` note trims against note length; `fam12.py` family levels per span; `m12.py` helpers). c11
scripts reused read-only: `stemdiff11.py`, `unchanged11.py`, `splice11.py`, `ridechk11.py`, `wait_mem.py`. Data as
rendered: `cycles/c12/build_render/`. Measurements: `cycles/c12/records/` (`*_c11.txt` = the same script on the c11
render, `*_c12.txt` on this render: `check12`, `acc12`, `ot12`, `rep12`, `fam12`; `stemdiff_horns_c11_c12.txt`,
`unchanged_tracks_c11_c12.txt`; the four state guard results). Logs: `build.log`, `render_cycle.log`, `settle1.log`,
`settle2.log`, `build_stale_after_render.log`, `top_after_render.txt`.

STATUS: rendered 2026-11-10 06:29-06:37 CST with `tools/render_cycle.py 12 --force-memory` (one render, no stem fix, no splice). Lock held 05:53:41-06:41:28 (47.8 min). mp3: `cycles/c12/scherzo-mockup-c12.mp3`.

Levels are K-weighted dB of the named stem unless stated. "pcX" = perceived onset of the new pitch with the previous
pitch excluded (`pcx.scan`), in ms against the notated onset; positive = late. Positions are score quarter notes (qn);
bar b starts at qn 3(b-1).

## 0. Score change from Dan (not a critic finding)

Approved by Dan 2026-11-10 01:14Z, score commit 0a79d901: Horn 1's solo link in bar 56 is removed. Applied to the build
copy only (`build/sections/sA.ily` sAHnOne last bar `b'4-. r4 r4 |`; `build/sections/sB.ily` `sBHnOne = { R2.*14 |`),
then `lilypond -o mockup mockup.ly` (exit 0, 141 warnings as before) and `score_to_parts.py`. Horn 1 now has B4 (71) at
sq 165 as a staccato quarter (`qn 164.912, dur 0.5, vel 84`, row StacSs RRx9: the same timing, length and velocity as
Horn 2's G4) and no note at sq 166; the old pitch 70 note is gone from parts.json. No table or config row was keyed to
the removed note or to the join 165 to 166 (leg_leads, JOIN_NOTCH, LEVEL_SHAPES, note_trims, fills, accent bodies and
score_config checked); the `leg_head_gaps` row at 164.604 that this cycle's new rule had produced went with the note.

Measured c11 -> c12 (`check12.py bar56`): Horn 1's stem over 166-168 -44.2 -> -63.5 dB (decay only). Master per 0.25 qn over 166-168: -32.2 -35.6 -37.2 -40.4 -42.3 -44.6 -45.9 -45.1, then the cellos at 168 (-33.7): a fall with no new onset. Horn 1's staccato at 165: first 0.2 s -42.7 dB (20 ms peak -36.9) against Horn 2's -46.7 (-41.8): Horn 1 is 4.0 dB over Horn 2 with the same velocity, length and lanes (c11's legato note was 7.1 dB over). Not corrected: the two play different pitches of the same row; a -4 dB `LEVEL_SHAPES` row on Horn 1 at 164.9-165.5 would equalise them if wanted (c13). The horn stem comparison shows the expected difference at 165.5-168.

## 1. Critics' findings

| finding | status | change | measured c11 -> c12 |
|---|---|---|---|
| A #1 timpani: motive x's downbeat stroke is the weakest of the three | accepted | `TIMP_RH_ALT["lh_vel_add"] = [(55, 10), (63, 8), (71, 4), (79, 6)]` (new generic key in `score_to_parts.py`: velocity added to left-hand strokes by velocity band; parts.json `timp_lh_vel`). 31 left-hand strokes raised: 64 -> 68 x12, 56 -> 64 x9, 52 -> 62 x2 (1110, 1111.5), crescendo strokes 57 -> 65 ... 76 -> 82; the 297 stroke stays 80 | first-stroke deficit against the statement's other strokes: 291 -8.1, 294 -12.5, 309 -3.6, 720 -9.0, 738 -10.3, 744 -13.3, 909 -5.7, 1086 -9.6, 1098 -9.6, 1110 -10.3 dB -> 291 -6.7, 294 -7.2, 309 -3.6, 720 -3.2, 738 -4.8, 744 -7.6, 909 -5.7, 1086 -4.1, 1098 -4.0, 1110 -1.8 dB. The soft statements gained 1.4-8.5 dB; A's 2 dB target is met at 1110 only. Open: more velocity on the first stroke of 291, 294, 744 |
| A #2 harp tune bars 73-80: uneven note levels | accepted | 22 `VEL_SET` rows keyed (qn, pitch) with A's velocities (216: 65, 217: 54, 218: 52, 219: 61, 221: 62, 221.5: 61, 222: 57, 223: 63, 224: 54, 225: 56, 227: 52, 227.5: 58, 228: 53, 229: 57, 230: 42, 231: 52, 233: 56, 233.5: 53, 234: 54, 235: 54, 236: 63, 237: 59). `VEL_SET` now applies after the velocity caps and accepts (qn, pitch) keys; each key hit one note, 20 changed | SD 3.3, range 14.2 dB, 216 -6.5, 230 +7.8 against the median; same-pitch spread 57: 5.8, 77: 7.3, 79: 5.4, 81: 10.8, 82: 2.4 -> SD 3.3 -> 2.2 dB, range 14.2 -> 9.5; same-pitch spread 57: 5.8 -> 3.1, 77: 7.3 -> 0.5, 79: 5.4 -> 3.7, 81: 10.8 -> 4.4, 82: 2.4 -> 2.1 (all under 8) |
| A #3 timpani summit roll bar 336 sinks under the tutti | accepted | Timpani `LEVEL_SHAPES` row over 1005.7-1007.9 now rises to +10 at 1007.0, +12 at 1007.5, +15 at 1007.85 (was +8 flat); new row +5 dB over 1008.0-1008.45 for the stroke at 1008 | roll per 0.5 qn -26.5 -32.3 -32.2 -32.3 -35.1 -39.1 -> -26.5 -32.3 -31.6 -30.8 -32.2 -33.7 (the last half beat is 0.7 dB under A's -33); stroke 1008 -29.8 -> -25.3 (1010 -25.5, 1012 -24.3 unchanged) |
| A #4 early legato joins; arrival at bar 201 | accepted | `leg_leads.json` (`apply12.py`): A's listed offsets (Violins II 598 -0.113, 600 -0.109, 595.5 -0.102, 593 -0.098; Violas 598 -0.098, 600 -0.078; Violins I 600 +0.055, 597 +0.062; Violoncellos 331 / 931 -0.101) and 38 other joins by the c07 rule `round(clip(0.7 x (pc/1000 - 0.02), +-0.15), 3)` from A's perceived onsets (Violins II 12, Violas 7, Violoncellos 18, Violins I 591) | changed joins, median pcX: Violins II n 16 -105; Violoncellos n 20 -77; Violas n 9 -91; Violins I 591 -103, 597 +109, 600 +98 ms -> changed joins (pcX): Violins II n 16 median -105 -> -19 ms, outside +-50 ms 16 -> 0; Violoncellos n 20 -77 -> -13, 20 -> 0; Violas n 9 -91 -> -15, 9 -> 0; Violins I 591 -103 -> +32, 600 +98 -> +48, 597 +109 -> +109 (did not move: open). Joins under -40 ms per track: Violins I 9 -> 7, Violins II 20 -> 5, Violas 17 -> 10, Violoncellos 33 -> 13. Attack probe: late or hole 0 |
| A #5 harp off-beat chords: round-robin colour | deferred | see below | - |
| B #1 trumpets and trombones too low | accepted | `mix.json` gain_db: Trombone 1 5.23 -> 8.23, Trombone 2 5.81 -> 8.81, Bass trombone 6.33 -> 9.33, Trumpet 1 1.11 -> 3.11, Trumpet 2 1.25 -> 3.25; Tuba unchanged. Includes the level these tracks lose to their width (ONE_TIME 11: Trumpet 1 1.05 dB, Trumpet 2 0.95, Trombone 1 0.92, Trombone 2 0.77, Bass trombone 0.63) | against Violins I, odd bars 105-119, median: Trumpet 1 -11.9, Trumpet 2 -13.1, Trombone 1 -15.3, Trombone 2 -12.8, Bass trombone -15.1 -> Trumpet 1 -9.9, Trumpet 2 -11.1, Trombone 1 -12.4, Trombone 2 -9.8, Bass trombone -12.2 (each track moved by exactly its gain: +2.00 / +3.00 dB on every note, `unchanged11.py`). B's 6.5-8.5 dB for the trumpets is not reached; I stopped at +2 because the first tutti's brass is already 1.2 dB over the woodwinds (300-312: wind -22.5, brass -21.3, strings -17.1). 994-995.5 stays 4.6-9.0 dB under each track's own 996-999; the chord at 309: trumpets -31.1 / -34.0, trombones -31.0 / -30.3 against Violins I -29.2; 2-5 kHz front minus body medians -7.0 to -0.9 dB (no hard fronts). Summit 1005-1011: strings -12.8 / -13.6, wind -17.3 / -16.1, brass -20.3 / -21.0 (order holds) |
| B #2 eighth pickup before the f of the second idea | accepted | `LEVEL_SHAPES` over the pickup eighth: Violins I -6 dB at 383.47-383.93 and 851.47-851.93; Violins II -9.5 dB on the same spans | pickup minus downbeat: Violins I +1.9 / +1.9, Violins II +7.8 / +8.0, master +2.0 / +1.7 dB -> Violins I -7.8 / -7.8, Violins II -1.1 / -7.7, master -2.2 / -5.0 dB. 383.5 is inside B's 1-3 dB; 851.5 is 2 dB past it, because Violins II's downbeat at 852 came out 6.8 dB louder than in c11 with identical data (-33.2 -> -26.4; 384 stayed -33.0). Open for c13: Violins I's row -6 -> -4 |
| B #3 Violins I accented C6 | accepted | `LEVEL_SHAPES["Violins I"]` -4.5 dB over 69.0-70.0 and -4.0 dB over 789.0-790.0 | 69 -28.2, 789 -28.1 -> 69 -32.7 (-4.5), 789 -32.1 (-4.0) |
| B #4 closing bars: Violins I bow changes, Horn 1's last note | accepted | `rebow_fills.json` Violins I 1103.814, 1116.299, 1125.156 refitted; `roles.json` Violins I `[1116, 1128, -2.5]` replaced by the ramp `LEVEL_SHAPES` `[(1113.0, 0.0), (1122.0, -2.5), (1128.0, -2.5)]`; Horn 1 two contour rows over 1111.7-1120.5 and 1120.5-1127.0 | re-bow before / 100 ms minimum / after: 1103.814 -50.0 / -51.3 / -48.5; 1116.299 -47.9 / -52.5 / -52.8; 1125.156 -49.1 / -53.7 / -53.0 -> c12: 1103.814 -50.0 / -51.8 / -48.8 (dip 1.7, after minus before +1.2); 1116.299 -48.0 / -52.1 / -52.4 (dip 4.1, -4.4); 1125.156 -49.2 / -53.5 / -53.0 (dip 4.3, -3.8): the refits changed the dips by 0.3-0.5 dB only; the last two are level steps of the lane, not holes (open). Horn 1's last note per qn 1111-1128 now falls evenly: -45.9 -45.5 -46.4 -46.9 -47.0 -47.4 -47.9 -47.9 -48.6 -48.6 -50.8 -51.4 -51.4 -51.3 -51.1 -51.3 -53.5 (c11 rose to -43.0 at 1113) |
| B #5 Flute 1 against the solo violin | accepted | `roles.json` Flute 1 `[1050, 1065.5, -3.5]` | solo violin minus Flute 1: 1051.5 +2.0, 1052 -0.7, 1054 -1.1, 1058 -1.6, 1064 -3.2 -> +5.5, +2.8, +2.4, +1.9, +0.3 (each +3.5); span 1050-1065.5: Flute 1 -48.0, solo -41.6. B's 4 dB is met at the first note only (open: another -2) |
| B #6 horns under the celli; Horn 3's F#3 | accepted | `roles.json` Horn 3 `[313, 360, 2]`, `[913, 960, 2]`; `pitch_trims.json` Horn 3 "54": 3 | Horn 3 minus celli: 312-360 -3.6, 912-960 -6.9; F#3 323 -40.0, 356 -38.9, 923 -43.0, 956 -42.1 -> 312-360 -1.7, 912-960 -5.0; F#3 323 -35.0, 356 -33.9, 923 -38.0, 956 -37.1 (+5.0 each). The F#3 joins with the mirror ramp (see Other changes) read +12, +13, +13, +14 ms; 511.5 +15, 800 +4, 1026 +3 |
| C #1 three legato transitions and one arrival note too loud | accepted | `JOIN_NOTCH` Violoncellos `(505.5, 506.0, -7.0)`, `(569.4, 569.9, -5.0)`; Clarinet 1 `(458.95, 459.2, -4.0)`; `LEVEL_SHAPES["Horn 1"]` -6 dB over 1076.85-1077.4, back by 1078.0 | join peak over the notes each side (stem / master): celli 506 +11.6 / +10.0, 570 +3.0 / +2.9, Clarinet 1 459 +7.1 / +5.2 -> celli 506 +4.6 / +3.6, 570 -1.7 / -1.6, Clarinet 1 459 +3.3 / +2.2; Horn 1 1077 first 20 ms frames -36.6 -36.4 -38.9 against 1071's -34.1 -34.1 -35.7 (was -31.2 -30.4 -32.9). Celli 506 is 1.6 dB over C's 3 dB (open) |
| C #2 Violins II drop at the re-bow in bars 141-149 | accepted | `rebow_fills.json` Violins II 432.497 new, capped at +10 dB | 431-436 max minus min 13.0 dB, minimum at 433.75 -> 4.2 dB, minimum at 433.75 (-51.3 against -60.1); no overshoot |
| C #3 Oboe 1's first trio note | accepted | `note_trims.json` Oboe 1 552 +5 with `NOTE_TRIM_RAMP_S` 0.1; `LEG_VEL_SPANS["Violoncellos"]` `(504.5, 552.0, 80)` -> `(503.3, 552.0, 80)` | Oboe 1 552-553 -49.8 against 553-554.5 -44.7 -> -45.5 against -43.9 (1.6 under; was 5.1). Basses at 504: body +3.0 dB |
| C #4 accented half notes of the two ff tuttis start under their body | accepted, by other means than C proposed | `entry_leads.json` Violins II 315 / 915 0.03, 327 / 927 0.05, Violins I 315 / 327 / 915 / 927 0.04; `ACCENT_DB_AT` 4.5 with `ACCENT_SWELL_S_AT` `(0.0, 0.08, 0.24)` on Violins I 315, 327, 915, 927 and Violins II 315, 327, 915, 927, 345, 945 | front (0-80 ms) minus body (100-200 ms): Violins I 315 / 915 -4.6, 327 / 927 -3.0; Violins II 315 -2.3, 327 -3.5, 345 -5.1, 915 -1.7, 927 -3.3, 945 -6.7; master 315 -3.2, 327 -2.5, 915 -2.3, 927 -2.3 -> Violins I 315 -1.2, 915 -1.3, 327 / 927 -1.4; Violins II 315 -0.4, 327 -1.1, 345 -3.8, 915 +0.1, 927 -1.0, 945 -4.9; master 315 -2.5, 327 -1.8, 915 -2.1, 927 -0.7. The violins' fronts rose 1.3-3.4 dB and their onsets moved from +19..+53 ms to -13..+10 ms (Violins I 915 -33); the master's front is still under its body (C's 0 dB not met: the other tracks of the tutti set it). Open |
| C #5 harp: one velocity per span, first tune note not heard | in part | `note_trims.json` Harp 216 +5 (a step over 215.956-216.868); the cap shift is rejected, see below | 216 full band -49.3 against 217-219 -36.8 -> -40.3 against -36.8 (216's 600-5000 Hz deviation from the tune's median -6.5 -> +3.9) |
| Bassoon 2 joins 40-80 ms later than c08 (orchestrator) | not stale state | the track was stale in the saved project | 519 -27, 546 -3, 632 +13, 654 +145, 663 +13 ms on c11 -> identical after the full build (519 -27, 546 -3, 632 +13, 654 +145, 663 +13 ms). The stale state was not the cause; the track has no pitch or note trims, so Movement II's c50 finding 1 (positive trim on a legato target) does not apply either. By my measure only 654 is late. No lead changed; 654 is open for c13 |

Rejected or deferred, with reasons:

- C #5's cap shift (new 4-tuple rows in `VEL_CAP_SPANS`, generic, off here): the shift is anchored on the span's top
  velocity, so one loud note sets the level of the rest. Simulated per span: 216-240 top 98, 45 of 53 notes at the floor
  43; 456-504 30 notes at 30 and 46 at 33; 552-576 41 at 30; 672-711 30 at 30, 28 at 33; 1020-1044 50 at 42; mean
  change -1.0 to -11.9 velocity steps. `HARP_PITCH_VEL` offsets were measured at one layer and overstate differences at
  velocity 56 by 2-3 times. The scherzo keeps its 3-tuple clip rows; bar 73's first note gets the +5 dB step and the
  tune A's per-note velocities.
- A #5 (harp patch swap for the off-beat chords' colour): deferred. A second harp patch does not fit under the 45 GB
  cap, and the harp's étouffez ends and cap levels are on the Do-not-touch lists.
- C #4's body cuts (`accent_bodies.json`) and an accent refit: not used. A body cut starts 0.18 s after the onset,
  after C's 100-200 ms body window, and the standard swell lowers C's metric. Longer entry leads and a front-weighted
  swell were used instead.
- C #1's celli trim at 506 (`"506.0": -3.0`): kept; the notch is added to it.
- ONE_TIME 4 / 21 / 22 (string repeat gaps): not adopted, see section 2.
- Note trims on notes shorter than the 0.6 s ramp (ONE_TIME 5): listed, left as fitted, see section 2.
- First tutti, brass against woodwinds: with B #1's gains the simulation puts the brass 1.3 dB over the woodwinds at
  300-312 (equal in c11). Re-measured below.

Other changes:

- ONE_TIME 2 (sf of the sfp at qn 900): post-fader bumps over 0.35 qn: Flute 1 +4 dB in all (lane 7.0 -> 8.0 at
  899.69), Flute 2, Oboe 1 (4.0 -> 7.0) and Clarinet 1 +3 dB; back by 900.75. Cor anglais entry lead 0.06 s at 900
  (`entry_leads.json`; note at 899.736).
- ONE_TIME 16: `RR_RESET_AT` gains 312.0 and 912.0 on Flute 1, Flute 2, Oboe 1, Cor anglais and Clarinet 2.
- ONE_TIME 29: `note_trims.json` Double basses +3 dB on the arco E2 at 140, 150, 504, 513, 624, 633, 666, 1071, 1074,
  1077, 1080, each with `NOTE_TRIM_RAMP_S` 0.1.
- `LEG_HEAD_MIN_GAP_S = {"wind": 0.032, "brass": 0.032}` (new generic rule: a legato-row note that starts a phrase less
  than this after the note before it is shortened at its predecessor to leave the gap; parts.json `leg_head_gaps`).
  Rows (gap before -> 32 ms): Bassoon 1 227.846, 251.846 (13.6), 644.867, 668.867 (7.9); Bassoon 2 515.867, 539.867
  (15.8); Horn 1 146.604, 155.604 (6.8), 641.658 (15.8), 1004.568 (6.2); Horn 2 143.78, 155.78 (6.8), 371.78, 839.78
  (13.6), 1004.76 (6.2); Horn 3 227.78, 251.78 (13.6), 998.76 (6.2); Horn 4 227.78, 251.78, 263.78, 371.78 (13.6),
  695.8252 (17.2). Aimed at the re-tongue holes of the orchestrator's note.
- `roles.json` Violas div `[1044, 1068, 3]`.
- `END_LEG_KS = {"Violins I": 5.0, "Violas": 5.0, "Bassoon 2": 5.0}`: the state-guard test, section 3.

Largest volume-lane differences c11 -> c12 (parts.json): Violins II 383.47-383.93 -9.55, 851.47-851.93 -9.56,
433.2-435.3 +10.0, +4.3..+4.5 at 315 / 327 / 345 / 915 / 927 / 945; Violins I 68.93-70 -4.51, 789 -4.0, 383.47 / 851.47
-6.05, +4.3..+4.6 at 315 / 327 / 915 / 927, 1127.92 -7.07; Timpani 1007.38-1008.05 +7.0; Horn 3 +5.0 at 323-324.1,
356-357.1, 923, 956; Oboe 1 552.38 +5.0; Flute 1 -3.5 over 1050-1065.5.
- Coordinator, Movement II c50 finding 1 (a positive pitch trim on a legato target read 60-100 ms late there with the
  0.25 qn ramp): the only positive trim added this cycle on legato targets is Horn 3's +3 dB on F#3 (323, 356, 511.5,
  800, 923, 956, 1026). New generic option `PITCH_TRIM_MIRROR` (a set of track names, empty by default): on those tracks
  such a trim starts over [moved onset - 0.05, + 0.03] qn. `score_config.py`: `{"Horn 3"}`. Only Horn 3's `vol_db`
  changed in parts.json (regeneration 7). Measured: those joins read +3 to +15 ms. Oboe 1's +5 dB at 552 is a slur's
  first note (not a legato target) and keeps its 0.1 s ramp. Bassoon 2 has no trims.
- Coordinator, Movement I c53 and Movement II c50 notes followed: guard on every save including the post-render save;
  more than 45 s between restart and render (memory settle 715 s, then audio init); render into an empty folder. Not
  used this cycle (pending for c13 if a finding needs them): range-render fitting limits, delivery EQ variants on one
  master, staccato per-pitch shapes on the alias track, substituting a return stem to test return levels.
  `~/.rpr-bridge/inbox/a7ba029ad458.running` was left alone and did not block the bridge.

## 2. ONE_TIME (`loop/ONE_TIME_c12.done.md`)

| item | result |
|---|---|
| 1 gap dip on repeated low-string arco eighths | not applicable: 0 runs of repeated arco eighths on celli or basses |
| 2 sf of the sfp at qn 900 | adopted (bumps above). c11 fronts against each track's ff accent at 897: Flute 1 -8.2, Flute 2 -6.4, Oboe 1 -5.4, Clarinet 1 -5.7, Clarinet 2 -2.0, Bassoon 1 -0.6, Bassoon 2 +2.1, Contrabassoon +1.1, Oboe 2 +6.7 dB; the horns are marked p there (no bump). fronts (first 0.1 s) c11 -> c12: Flute 1 -32.5 -> -31.7, Flute 2 -38.2 -> -35.2, Oboe 1 -33.0 -> -30.2, Clarinet 1 -31.4 -> -28.2; Cor anglais -52.2 -> -35.1 (its onset +106 -> -25 ms); master peak at 900 -12.8 dB at 0 ms |
| 3 negative leg_leads row before the clamp | done in c11 (`LEG_LEAD_CLAMP_TOTAL`) |
| 4, 21, 22 string repeats by slur state; new-bow notch; detach dip | measured on c11 (`rep12.py`): `rep_rebows` n 16, median dip -1.6 dB, 13 under 3 dB; `rep_sus_gaps` median 6.0 dB, 7 of 25 under 3 dB (celli 306 0.0, 910 -0.4, 1010 0.9; basses 310 2.5, 910 2.0, 1010 1.7); portato strokes loud n 33 median 0.6, soft n 2 median 4.6; strokes n 8 median 1.8; unclassified loud n 239 median 2.2, soft n 18 median -0.2. Not adopted: no critic flags a string repeat, C's S1 check passes and C lists the separation of repeated notes as Do-not-touch. Horns' repeats: `LEG_HEAD_MIN_GAP_S` this cycle; re-tongue holes after `LEG_HEAD_MIN_GAP_S`: Horn 3 605.81 5.6 -> 3.8, Bassoon 2 515.87 8.5 -> -1.3, 539.87 7.7 -> 1.7; unchanged: Horn 1 141.7 7.0, 998.57 9.7, 659.66 5.8, Horn 3 521.81 4.0, Horn 4 371.78 6.3 -> 6.7. String classes as on c11 (`rep_rebows` median -1.8, `rep_sus_gaps` 6.0, strokes 1.3) |
| 5 note trims on short notes | `trims12.py`, 95 trims. Plucked trims are steps. Under 80 % of the request with the 0.6 s ramp: Clarinet 1 461 (+1.7 of +4.0), 466 (+2.8 of +3.5), 482 (+1.7 of +4.0), 491 (+0.7 of +2.0), 493 / 661 (-1.1 of -2.5); Clarinet 2 834 (+4.5 of +6); Violas 159 (+2.6 of +4) and eleven 0.11 s notes at 628-664 (+0.3..+1.2 of +1.5..+7; the lane continues past the note end through `LEG_JOIN_TRIM_HOLD`); Violas div seven at 625-661 (+1.1 of +6); Violoncellos 504 (+3.2 of +5), 828 (+2.5 of +5). Decision: left as they are (they were fitted with the ramp in effect and several are on Do-not-touch lists); only the new trims of this cycle got 0.1 s ramps. Dead row found: Violoncellos 297.0 -4.0 matches no note |
| 6 delivery ride after a subito | `ridechk11.py` on c11: delivery gain flat at +6.4..+7.1 dB over 819-846; f -> p step 825 -> 828 master -5.4, delivered -5.6 dB; after the G.P. the gain is +2.5 (1011), +3.2 (1014), +4.1 (1017), +6.3 (1020), +7.2 (1032); summit -> pp step master 25.6, delivered 21.9 dB. No change |
| 7, 17, 26 unchanged tracks between renders | done (`records/unchanged_tracks_c11_c12.txt`): the 6 tracks with identical data (Oboe 2, Bass clarinet, Contrabassoon, Tuba, Harp harmonics, Violin I solo) reproduce c11 at +0.00 dB median, largest single note 0.45 dB, lag 0 ms; the 5 brass tracks with only a gain change moved by exactly +2.00 / +3.00 dB. Master per bar: c12 minus c11 median +0.00, p10 -0.2, p90 +0.3; bars 2 dB or more apart: 24 (-3.0, B #3), 169 (-2.8, C #1), 284 (-2.0, B #2), 372 (-2.2, B #4), all intended. c12 minus c10 (master only): median +0.00, p10 -0.6, p90 +0.4; bars 5, 24, 48, 169, 281, 342, 372 by 2.0-3.4 dB (c11's and c12's intended changes). No EQ change this cycle (item 9) |
| 8 state guard in the tools | done: `build_reaper.py --midi-only` fully rebuilds stale tracks, `render_cycle.py` refuses a stale project (`--force-stale` overrides). Results in section 3 |
| 9 remove EQ changes before comparing renders | no EQ change this cycle |
| 10 "drop" phrase type | not applicable: no such type here; `subito_falls` has 15 rows, all at printed subito marks |
| 11 width costs level | measured from each stem's mid / side: Trumpet 1 1.05 dB, Trumpet 2 0.95, Trombone 1 0.92, Trombone 2 0.77, Bass trombone 0.63. Inside B #1's gains, not added twice |
| 12 width and side EQ together | no width or side EQ change |
| 13 clamped low-wind swell into the volume envelope | already there (`hpgain`, 393 rows). CC11 reaches 127 on 1 point each on Bassoon 1, Bassoon 2, Contrabassoon, Cor anglais (3 on Clarinet 2), only in the summit crescendo 1002-1005. No change |
| 14 reversed short crescendos | 563 hairpin spans, 0 reversed (two flagged were `SHORT_CC11_PARK` values on staccato notes) |
| 15 | withdrawn by Movement I |
| 16 CC16 reset before a repeated-note passage | adopted: `RR_RESET_AT` 312.0 / 912.0 on five woodwind tracks. Single notes there may differ from c11 by 1-6 dB (a take change, not a level change) |
| 18 | supports 1, 2, 4, 5; no action of its own |
| 19 short stage return | not tried, as instructed |
| 20 pitch_check.py | not applicable: no mic or width change |
| 23 late sfp peak in the tutti | c11 master peak at 900 is on time (-12.9 dB at 0 ms), no late-sfp notch needed; 902 peaks -20.9 at +100 ms, 904 -17.6 at +480 ms. c12: 900 -12.8 at 0 ms, 902 -20.9 at +100 ms, 904 -17.5 at +480 ms (unchanged); pcX at 900: Violins II -59, Oboe 1 -42, Cor anglais -25, Flute 1 -19, Violins I +5; Flute 1 904 +146; basses' step at 902 -10.0 dB |
| 24 per-pitch join measurement | in use (`pcx.scan`); c12 medians: Violins I +16, Violins II +1, Violas +3, Violoncellos +9, Double basses -54, Flute 1 +7, Flute 2 +30 (c11 +46), Oboe 1 -2, Clarinet 1 +17, Bassoon 1 +15, Bassoon 2 +12, Horn 1 +28, Horn 3 +13, Horn 4 +1 ms |
| 25 pre-render simulation | done, see Render |
| 27 phrase arc keys | not applicable: no phrase arc or tempo change |
| 28 ride rows over soft passages | none: the six `ride_trims` rows are cuts at loud bars (299.6-312.4 -2, 897-912.4 -2, 212.5-216.3 -1.5, 576-602 -2, 624-649 -1, 659-672 -2). Soft ending 1083-1125: automatic gain +11.1 -> +13.0 dB, falls stay falls. No change |
| 29 basses' weak arco E2 | adopted: pitch 40 bodies -4.9 dB (n 10) against the track's other pitches at the same CC11 (regression 0.240 dB per CC11 unit, n 81); +3 dB trims on 11 onsets. the body at 504 rose 3.0 dB (-55.3 / -55.1 / -54.1 -> -52.3 / -52.1 / -51.1); the regression measure removes the lane, so it still shows pitch 40 at -4.4 dB |
| 30 | results only |
| 31 | rule followed |

## 3. State guard and the stale post-render save

Three guard runs (`tools/state_guard.py`, offline read of the saved .rpp against `jobs/NN_<stem>.b64`):

| when | result |
|---|---|
| 1. project as saved after the c11 render, before the build | 5 stale of 31, 0 missing: Bassoon 2 (18 groups), Horn 4 (16), Violins I (58), Violas (52), Violoncellos (52); saved attack 20.0 ms against written 438-1380 ms (`records/state_guard_before_build.json`) |
| 2. after the full build of every track, before the render | 0 stale, 0 missing (`records/state_guard_after_build.json`) |
| 3. project saved after the c12 render | 7 stale: Bassoon 2 (18), Contrabassoon (24), Horn 2 (16), Horn 4 (16), Violins I (58), Violas (52), Violoncellos (52) (`records/state_guard_after_render.json`). These 7 were then rebuilt in full without playback and the project saved: 0 stale (`records/state_guard_final_save.json`), so c13 starts from a clean save |

Why the post-render save is stale (orchestrator's question). Facts from the c10 and c11 saves and the data rendered:

1. Only the legato sustain groups differ, and only in the envelope attack (20.0 ms saved). Other saved runtime values
   differ on every track, so the attack is the only marker.
2. No track whose legato row was still selected at the end of the render was stale (8 tracks in both renders: Oboe 1,
   Cor anglais, Clarinet 1, Clarinet 2, Bassoon 1, Violins II, Violin I solo, Violas div), including three whose last
   legato note was a phrase's first note.
3. Every stale track had left its legato row for "Sus MAX" before the end, with that keyswitch 2-70 ms after the last
   legato note's end, and the next note repeated the same pitch within 6-76 ms (keyswitch at: Bassoon 2 902.816,
   Violins I 1103.794, Violas 1079.98, Horn 4 1007.73, Violoncellos 1073.98, Contrabassoon 902.8).
4. On 4 of the 5 stale tracks of each render the last legato-row note was a phrase's first note; Violas' was a join
   (stale in both).
5. Six tracks left the legato row and were clean in both renders: Flute 1, Double basses, Horn 3, Horn 1, Flute 2,
   Horn 2. Horn 2's final sequence equals Horn 4's, which was stale.
6. It is not deterministic: the Contrabassoon (identical data) was stale after c10 and clean after c11; Violoncellos
   the reverse.

Reading: the legato row's script sets the sustain groups' attack to 20 ms for a phrase's first note and puts the patch
value back at a join or while its row stays selected. When the track changes rows straight after, the 20 ms can stay in
the instance, and the next save stores it. This agrees with Movement I's c53 note; it does not predict every track
(facts 5 and 6).

Test in this render (`END_LEG_KS`, generic, off by default): Violins I, Violas and Bassoon 2 (stale after both renders)
get their legato row's keyswitch once more at qn 1133.0, 5 qn after the score's last release, where no note follows.
Controls, unchanged: Horn 4 and Violoncellos (stale after c11), Contrabassoon (stale after c10).

Result: the remedy does not work. All three treated tracks were stale again after the render, as were the three controls, and Horn 2 (clean after c10 and c11, final sequence equal to Horn 4's) was stale for the first time. A keyswitch after the last note does not put the patch value back. `END_LEG_KS` is rejected; its three rows stay in `build/score_config.py` only because they are in the rendered data (remove in c13; the extra keyswitch at qn 1133 makes no sound). What works: the guard on every save, and a full rebuild of the stale tracks with no playback before the save (done here after the render; 24 s for 7 tracks).

## 4. Coordinator notes

- Horn stems against c11 (`stemdiff11.py`, 2 dB): 29 / 27 / 103 / 8 half beats differ for Horn 1-4 (`records/stemdiff_horns_c11_c12.txt`). All sit where the data changed: Horn 1 165.5-168 (Dan's change), 1076.5-1077.5 (C #1), 1112.5-1123 (B #4); Horn 3 313-360 and 914-959 (+2 role, +5 on F#3); the rest are notes whose ends moved under `LEG_HEAD_MIN_GAP_S` (Horn 1 156-164.5, Horn 2 156-159.5, 372-375.5, 840-841.5, Horn 3 228-230, Horn 4 228.5-230, 372), 2-7 dB either way. Horn 1 642-643.5 is 13-23 dB higher than in c11 (-60.1 -> -44.5) with identical data: that note was nearly missing in c11 and is present now. No attack is lost; nothing was spliced.
- Re-tongue holes over 8 dB (C's list; my measure on c11): Horn 1 141.7 7.0, 998.57 9.7, 659.66 5.8 (164.6 removed by
  Dan's change); Horn 3 605.81 5.6, 521.81 4.0; Horn 4 371.78 6.3; Bassoon 2 515.87 8.5, 539.87 7.7 -> c12: Horn 1 141.7 7.0, 998.57 9.7, 659.66 5.8; Horn 3 605.81 3.8, 521.81 4.0; Horn 4 371.78 6.7; Bassoon 2 515.87 -1.3, 539.87 1.7. One hole over 8 dB is left (Horn 1 998.57).
- Open list from c11 (pcX by `r.pc`): Oboe 1 672 +194; Violins II 672 +248, 708 +138, 900 -59; Flute 1 904 +146;
  basses 1071 +144, 504 +112; solo 1044 +139; Violas 1020 +109; Horn 1 at 6 +97; basses' step at 902 -10.0 dB; master
  639 / 640 / 641 -30.0 / -28.9 / -28.0 -> c12: Oboe 1 672 +194; Violins II 672 +248, 708 +138, 900 -59; Flute 1 904 +146; basses 1071 +149, 504 +120; solo 1044 +139; Violas 1020 +109; Horn 1 at 6 +97; basses' step at 902 -10.0 dB; master 639 / 640 / 641 unchanged. None of these was worked on in c12; all stay open (Movement II's c50 finding 4: no per-note refit in c12).
- Hall (Dan's limit, c05): G.P. 1016: drop at +0.3 s 20.5 dB, 20 dB fall 0.30 s, RT60 1.32 s; final chord 1128: 20.1 dB, 0.31 s, RT60 1.40 s; soft ends 0.14-0.29 s; returns re dry R Strings -14.39, R Brass -25.14 (+0.65 from B #1's gains), R Winds -15.68, R Perc -27.60, all -11.67 dB. Inside every limit; not drier either (c11: G.P. drop 20.4 dB at +0.3 s, tutti 20 dB fall 0.30 s, RT60 1.34 s, soft ends
  0.14-0.29 s; returns re dry R Strings -14.34, R Brass -25.79, R Winds -15.58, R Perc -27.58).
- Comparison with c11 and c10: see ONE_TIME 7 / 17 / 26 above. Master -20.8 LUFS, LRA 23.4, true peak -1.5 (c11 -21.0 / 23.0 / -1.7; c10 -21.0 / 23.1 / -1.2).

## Research items

| item | status |
|---|---|
| EW template mix (c06), returns and sends (c07-c09), c08 EQ set, brass track width (c10) | adopted, unchanged. Hall measured after B #1's brass gains: RT60 1.32-1.40 s, G.P. drop 20.5 dB, inside Dan's limit |
| finale SHARED-TECHNIQUES 13-17 | adopted as in c11, unchanged |
| finale SHARED-TECHNIQUES 18-23 | 19 adopted (sf bumps at 900); 20 done in c11; 22 measured, trims left (list in section 2); 23 checked, no change; 18 not applicable (no repeated arco eighths on the low strings); 21 measured, not adopted (no finding on string repeats) |
| finale SHARED-TECHNIQUES 24-33 (ONE_TIME 21-31) | 28 (simulation) and 29 (drift check) adopted as checks; 27 (per-pitch joins) in use; basses' weak pitch adopted (+3 dB on E2); 24, 25 measured, not adopted; 26 checked, not needed; 30 not applicable |
| wind phrase-shape scale x1.4 (c10) | kept on CC11 tracks; rejected on CC1-dynamics tracks (c11: clarinets +2.6..+4.5 dB) |
| Movement II c48: `fp_falls`, unchanged-track comparison | first not needed; second run each cycle (done, see ONE_TIME 7 / 17 / 26) |
| Movement I c52 state guard | adopted and now enforced in `build_reaper.py` and `render_cycle.py`; three results in section 3 |
| Movement I c52 items 9-15 | 9, 12 no EQ or width change; 10 not applicable; 11 adopted inside B #1's gains (0.63-1.05 dB); 13 already in the envelope; 14 0 reversed crescendos; 15 withdrawn |
| Movement II c49 items 16-20 | 16 adopted (CC16 resets at 312 / 912 on five woodwinds); 17 adopted as a check; 18 no action; 19 not tried; 20 not applicable |
| batch 6 #3 shared curves, CC11 -> CC1 pass 2, separate legato tracks | pending (memory / pass 2) |

## MANUAL-GAPS

- Row 12 corrected: CC16 is in use since c07 (`RR_RESET_AT`), extended this cycle.
- #6 timpani hard sticks: not tried; a second timpani instance does not fit under the 45 GB cap. Pending.

## Tool changes (generic, off by default)

- `tools/score_to_parts.py`: `TIMP_RH_ALT["lh_vel_add"]` (output `timp_lh_vel`); `VEL_CAP_SPANS` 4-tuple shift rows
  (output `vel_cap_shift` / `vel_cap_pre`); `VEL_SET` applied after the caps, with optional (qn, pitch) keys;
  `LEG_HEAD_MIN_GAP_S` (output `leg_head_gaps`); `END_LEG_KS` (output `end_leg_ks`); `PITCH_TRIM_MIRROR`.
- `tools/build_reaper.py`: `--midi-only` fully rebuilds a track whose saved Opus state is stale (prints
  `<track>: saved Opus state is stale (state_guard: AHDSR attacks differ), full rebuild`).
- `tools/render_cycle.py`: prints `state_guard: stale [...]` and exits on a stale project unless `--measure-only` or
  `--force-stale`.

## Render

Pre-render simulation (ONE_TIME 25; `stem_fix.py --out` on the c11 stems for the 12 tracks with level-only changes,
then `deliver_master.py`): delivered -19.9 LUFS, LRA 14.8 LU, true peak -1.5 dBTP, limiter about 2.8 dB, ride +10.0 /
-3.1 dB (c11 real: -19.8, 14.8, -1.4, 2.9). Family levels, c11 -> simulation (wind / brass / timpani / strings):
300-312 -22.5 / -22.6 / -30.7 / -17.1 -> brass -21.2; 993-1005 brass -23.2 -> -22.3; 1005-1008 -17.3 / -20.9 / -28.5 /
-12.8 -> brass -19.8, timpani -27.6 (strings > woodwinds > brass holds); 1008-1011 brass -21.8 -> -20.9.

Steps (2026-11-10 CST). Lock taken 05:53:41 after Movement II's c50 actor released it (it had held it since 20:53 the
evening before). 05:54 start and open (warm cache, 18 GB in 30 s). 05:55:05 full build started 5 s after the open: REAPER
crashed at 05:55:20 in an Opus thread (EXC_BAD_ACCESS; `~/Library/Logs/DiagnosticReports/REAPER-2026-11-10-055520.ips`)
while the seventh track's instance was replaced; nothing had been saved. 06:00 start and open again, memory settled at
45.0 GB after 723 s; 06:13:25 full build of all 31 tracks (66 s, no mismatches, `build.log`); save; guard 0 stale;
`build_render/` copied; restart; settled at 45.0 GB after 715 s; `audio_init.lua` (48000 Hz, 512, no input); render
06:29:12-06:36:59 with `--force-memory` (42 GB compressed, settled). Save, guard (7 stale), full rebuild of those 7, quit
with save, guard 0 stale, unlock 06:41:28. Lock 47.8 min. Newest Opus log: no "Interrupted system call".

Result: master -20.8 LUFS, LRA 23.4 LU, true peak -1.5 dBFS, sample peak 0.846; no stem at or near full scale, 31
instrument stems and 4 return stems present. Delivered -19.8 LUFS, LRA 14.8 LU, true peak -1.5 dBTP, limiter about
2.8 dB, ride +10.0 / -3.1 dB (the simulation: -19.9 / 14.8 / -1.5 / 2.8). Attack probe: late or hole 0. Metrics'
`silent_notes`: Violas 579 (A3, mp) as in c10 and c11 (open). REAPER after the render 45 GB, 32 GB compressed
(`top_after_render.txt`). Family levels as simulated within 0.1 dB (300-312 brass -21.3; 1005-1008 brass -20.3, timpani
-27.6). Disk: 42 GB free after deleting c11's stems, return stems and `render_first/` WAVs (kept c11's master and mp3)
and the five files in `Backups/`. cycles/c08's stems are still there (deletion refused in an earlier session; not
retried).

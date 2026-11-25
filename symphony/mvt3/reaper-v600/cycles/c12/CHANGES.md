# Cycle 12 changes (actor, 2026-11-09)

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c11 render). Snapshot: `before/` (the c11 final build and tools).
Scripts in `actor_scripts/`: `ver12.py` (the per-item numbers below), `drift12.py` (level changes on unchanged data),
`simcmp12.py` (real master against the master simulated before the render), `dl_meas.py` (delivery), `lib12.py`
(helpers from c11's `m11.py`), `vp12.py`, `sim_a.py` / `sim_b.py` / `sim_c.py` (simulation on the c11 stems),
`joins6.py` and `joins6b.py` (the muted trumpet's joins). Logs: `lock.log`, `start.log`, `open.log`, `build1.log`,
`restart.log`, `audio_init.log`, `render.log`, `top_after_render.txt`, `deliver_check.log`, `stem_fix.log`,
`mixonly.log`, `deliver_final.log`, `measure_final.log`, `quit.log`, and the measurement logs in `logs/`.
Builds: `rendered_build/` (as rendered), `final_build/` (after the level-only fix). `render_first/` holds the master and
the two stems of the first render; `metrics_first/` its metrics. `render/`, `metrics/` and the mp3 are the fixed state.

## What changed

Tools (`tools/score_to_parts.py`, comments "mvt3 c12"; all other tools equal `before/`):
- `ROW_SLUR_OVERLAP_S = {track: {row: seconds}}` (A #3): at a `ROW_LEAD_S` join under one printed slur the note before
  ends this long after the moved onset instead of 0.02 qn before it. parts.json `row_slur_overlaps`. Default: none.
- `ROW_LEAD_KEEP_END = {track: {row: [(from_qn, to_qn)]}}` (A #4): a led stroke in a listed span keeps its note end, so
  the played gap before the next stroke does not grow by the lead. Default: none.
- `STR_REP_NEW_BOW["plain"]["force"] = {track: [score onsets]}` (A #1): listed same-pitch repeats take the new-bow gap at
  any dynamic, under a slur and inside `STR_REP_DETACH` / skip spans. A listed onset that cannot take it prints a WARNING.
- `tools/state_guard.py`: copy of Movement I's tool (coordinator, Movement I c52). Read-only check of the saved .rpp for
  stale Opus legato state.

Config (`build/score_config.py` c12 block; `mix.json`, `pitch_trims.json`, `roles.json`, `note_trims.json`,
`rebow_fills.json`, each with a `_c12` note). Numbers are the coordinator's items:
1. B #1, basses under the second chorale (bars 255-260): pitch trims Double basses E2 +6, F2 / E flat 2 / F1 +3 dB (all
   rows); role row [988, 1020, +3, ramp 4] -> [988, 1032, +3]; Tuba role [1016, 1032, -3] deleted.
2. C #1, delivery tone: `master_eq` without the 167 Hz -1.6 dB bell, plus a 1.5 kHz -1.5 dB bell (bw 1.0). High-pass
   42 Hz and the 6 kHz -3 dB shelf stay.
3. A #2 / C #3, sfp at 592: `LEVEL_SHAPES_S` notch 0.11-0.40 s after the mark, (0.11 s, 0), (0.19, g), (0.30, g),
   (0.40, 0) with g = -5 dB Bass trombone and Trombone 2, -4 Horn 3 and Tuba, -3 Horn 1 and Trombone 1; the c11 +3 dB
   front (591.95-592.35) now also on Bass trombone, Trombone 2, Tuba and Trumpet 3. No bump above +3: the simulated first
   0.1 s of the master was already over the ff before. No new row.
4. A #1, cello same-pitch repeats: `STR_REP_DETACH` on Violoncellos 64-104 and 596-672 `dip_db` -5 -> -10, `dip_s` 0.08 ->
   0.10; +4 dB level shapes on the repeats at 630 and 658 (629.76-630.6, 657.76-658.6; each follows a legato-row note
   at velocity 124 and started 7-10 dB under it); forced new-bow gaps at Violoncellos 325, 327, 832 and Violas 728 (data
   gaps 24 / 23 / 10 / 11 ms -> 90 / 90 / 90 / 74 ms). Not forced, with the reason: Violas 426, 556, 564 (p repeats that
   the "soft" rule plays as re-bow pieces with fitted fills; the force rule does not cut re-bow pieces), Violoncellos 564
   (a staccato eighth before a slur start; the sample ends by itself), Violins I 896 (tremolo to tremolo), Violins I 876
   and Violins II 880 (held p chords under the printed "change bow at will"). After the render, level-only: a volume
   notch inside the forced gap at Violoncellos 325 (-8 dB) and Violas 728 (-16 dB); see "After the render".
5. B #2 / B #3, loud woodwind pitches: Flute 1 `dyn_trim_db` f -1.5 -> -3.5, ff -1 -> -4.0, `soft_trim_db` mf 2.5 -> 0.5;
   Flute 2 `soft_trim_db` mf 2.5 -> 0.5; Oboe 1 `dyn_trim_db` ff 6 -> 4.5; pitch trims Flute 1 G6 -5, Flute 2 E flat 6
   -5, Oboe 1 F5 -5, E5 -3.5, A flat 5 -3.5, G5 -4.0; Flute 1 roles [304, 320, -7], [1012, 1016, -4], [1108, 1113.5,
   -2.5], [168, 176] +4 -> +5. Two values go beyond B's: Flute 1 ff -4.0 (B: -3.0; with -3.0 the simulated flute was
   still the loudest stem in 8 loud bars) and Oboe 1 G5 -4.0 (B: -2.5; that left the held G5 at 900-905 3.4 dB over
   Violins I). The role rows are follow-ups from the simulation (the `_c12` note in `roles.json` gives each reason).
6. A #3, muted Trumpet 1 solo (680-744): `ROW_SLUR_OVERLAP_S` Trumpet 1 "Mute Sus" 0.03 s (22 slurred joins: data overlap
   -7 ms -> +30 ms); +3 dB level shapes over D4 / C4 (683.92-685.86, 715.92-717.86; both sat 4.2-4.5 dB under the E flat 4
   next to them on equal data); role [680, 712, +2] replaced by per-bar rows 680-684 0, 684-688 -1, 688-692 +2, 692-696
   +5, 712-716 +1.5, 716-724 0, 724-728 -6.5, 728-732 +3.5 (from the simulated differences to the cor anglais, target 3 dB
   under it). The balance target is met; the join target is not (the overlap lengthened the time in which both pitches
   sound; see "Measured").
7. C #4, delivery ride: C's offsets on the 164 row (166 -0.4, 168 -1.5, 170 -2.2, 172 -2.75, 174 -3.2, 176 -3.1, 178
   -2.8, 180 -2.5, 182 -2.1, 184 -1.7, 186 -1.58, 188 -1.45, 190 -1.08, 192 -0.7, 194 -0.35), so the total delivery gain
   rises about linearly from 164 to 196; the 679 row is now (679, 0), (680, +1), (696, +2.55), (743, +2.55), (744, 0)
   (it reached its value at 680 before).
8. C #2, tempo: `PHRASE_ARCS` + (888, 912) and (916, 936, "sub"). The four cello re-bow fills of the held C3 are keyed
   in seconds-spaced positions that moved 1.6-8.6 ms with the arcs: `rebow_fills.json` keys renamed 915.324 -> 915.327,
   919.963 -> 919.971, 924.603 -> 924.615, 929.243 -> 929.259.
9. A #4, basses' on-beat eighths in 1088-1108: `ROW_LEAD_S` "Sus MAX" 0.03 s on every beat (20 onsets) with
   `ROW_LEAD_KEEP_END` on the span. The gap before each beat goes from 73 to 43 ms and the c11 beat-gap dip stays; 0.06 s
   would leave 13 ms and drop the dip.
10. B #6, fff at bar 263: note trims Trumpet 1 1044 -3, 1048 +2.5, Horn 3 1044 -2 dB; Trumpet 1 role [1032, 1047.5, +2,
    ramp 1] -> [1032, 1054, +2, ramp 1].

Opus states: none changed (offline comparison of `state_for()` for all 31 tracks, and no "full rebuild" line in
`build1.log`). Tracks written: all 31 with `--midi-only --tempo`, because a tempo-map change needs every item
recreated. MIDI data differs from c11 on 28 tracks (20 of them only by the few-ms shifts in the chorale); Cor anglais,
Bass clarinet and Harp have equal data.

`state_guard.py` on the saved .rpp: before this cycle's build 31 tracks, 0 stale, 0 missing; after the build and save
the same. No track needed a full rebuild.

## Rejected or deferred
- Item 11 (low priority): Flute 2 at 650 and 618 and Bassoon 1 at 464 were not worked on.
- C #2's optional arcs on the bassoon solo, (456, 472, "sub") and (472, 488, "sub"): not added. They would move the
  joins that c11 fitted there.
- "Sus Accent MAX" at 592: dropped by all three critics; the notch and bumps of item 3 need no row.
- B's +5 to +6 dB bumps at 592: not used (see item 3).
- Movement II c48's fp finding (per-dynamic volume trims read an fp spike as a printed f): the finale's `vol_points()`
  reads it the same way. Not changed: on the c11 stems the fp fronts are 9.7-17.0 dB over the level after them at 548
  (strings) and 15.0-16.9 dB at 832 (Trombone 1, Horn 1), so no fp front is weak, and the port would raise the brass
  fronts at 832 by 8-12 dB and undo the c09 fits.
- Movement II's CC16 reset table (`RR_RESET_AT`): not added (coordinator: a later cycle).
- Closed by the coordinator and not touched: the 315 Hz hump in J, tuba / contrabassoon -3 dB, "Leg Slur Exp" on cor
  anglais and Oboe 1, bar 275 beyond item 5.

## Mistake to record
While checking the Opus states offline I executed `tools/build_reaper.py` up to its `--mix-only` branch. That part
includes `returns_job()`, which rewrote `jobs/90_returns.lua` (a generated file that every build rewrites) and sent it
to the bridge. The bridge
refused it ("REAPER is held by scherzo ... is outside it"), so the Scherzo thread's REAPER was not touched. The offline
check now stops before the main section.

## After the render
- Level-only fix, no re-render. Two of item 4's forced gaps stayed filled by the release tail of the note before: by the
  item's measure the first render gave 3.8 dB at Violoncellos 325 (data gap 24 -> 90 ms) and -4.4 dB at Violas 728 (gap
  11 -> 74 ms; a pp repeat at -67 dB after a note at -62 dB). Added `LEVEL_SHAPES_S` notches inside the gap, in seconds
  before the note-on: Violoncellos 325 (-0.085 s, 0), (-0.060, -8), (-0.015, -8), (0, 0); Violas 728 (-0.070, 0),
  (-0.050, -16), (-0.015, -16), (0, 0). At the violas -12 dB gave only 3.1 dB in the simulation, because the repeat is
  5 dB softer than the note before; -16 dB gives 7.1 dB. The celli reach 10.1 dB.
- Steps: both depths simulated with `tools/stem_fix.py --out` on the rendered stems (`logs/fix_sim.log`); written to
  REAPER with `build_reaper.py --mix-only` for Violoncellos and Violas while holding the lock (`mixonly.log`), saved,
  and the saved .rpp checked for the notch points (`logs/rpp_notch_check.log`); `stem_fix.py --apply` then rewrote the
  two stems and the float master (`stem_fix.log`; a file operation, run 10 s after the unlock). The first render's
  master and two stems are in `render_first/`. `render_cycle.py 12 --measure-only` re-ran the metrics, the attack probe
  and the delivery on the fixed files (`measure_final.log`); the first render's metrics are in `metrics_first/`.
- `final_build/parts.json` differs from `rendered_build/parts.json` only in the `vol_bp` / `vol_db` of Violas and
  Violoncellos. The master changes by at most 0.4 dB in single 20 ms frames around the two notches; the loudness figures
  are the same as on the first render.
- `state_guard.py` on the final saved .rpp: 31 tracks, 0 stale, 0 missing. No track was stale at any of the three
  checks (before the build, after the build, after the final save).
- No second render and no full rebuild for the notes that moved on unchanged data (list under "Measured"): the state
  guard finds no stale track, the per-track medians are 0.00 dB, the moves are single notes in both directions, and a
  full rebuild of the 12 tracks would move the joins fitted in c10-c12 and need another render (one render per cycle).
  No trims were written against the drifted notes.

## Measured (c11 -> c12 on the fixed files; `ver12.py`, K-weighted on the stems' own scale unless named)
- **Basses under the second chorale (item 1)**, stem bars 255-260 (Z): 15.9 / 11.4 / 20.6 / 27.0 / 25.6 / 23.7 -> 21.0 /
  19.4 / 23.6 / 29.9 / 27.7 / 25.7; bars 253-254 and 261-262 unchanged. Per pitch (30-400 Hz): F1 11.2 -> 14.1, E flat 2
  11.1 -> 13.9, E2 10.3 -> 15.9, F2 15.8 -> 18.8; other pitches unchanged. Tuba (A) 255-258 +3.0 (23.0 / 22.2 / 20.5 /
  19.1 -> 26.0 / 25.2 / 23.5 / 22.2). Master 31.5-125 Hz minus the full band, bars 255-260: -25.4 / -23.5 / -19.2 /
  -16.1 / -16.7 / -18.5 -> -22.3 / -20.8 / -17.4 / -14.1 / -16.2 / -18.2. B's target for the master (no more than 17 dB
  under in bars 255-257) is met in none of the three by this measure: 255 and 256 are 5.3 and 3.8 dB short, 257 0.4 dB.
  B's own c11 figures were -24.7 / -17.2 / -19.0, so the two measures differ in bar 256; bar 255 is short by either.
  B's target for the stem is met: on B's scale the basses' bars 255-256 go from -43.3 / -49.8 to about -38.2 / -41.8 dB
  Z (range -42 to -37). Not raised further for that reason.
- **Delivery tone (item 2)**, mp3 octave shares of the loud frames (c11 -> c12): 63-125 Hz -14.6 -> -13.0, 125-250
  -11.9 -> -9.9, 250-500 -7.4 -> -6.4, 500-1000 -5.9 -> -5.7, 1-2 kHz -4.4 -> -6.0, 2-4 kHz -10.6, 4-8 kHz -20.2 ->
  -19.9; centroid 1059 -> 927 Hz. Decay to -20 dB after the stops: bar 2 0.47 -> 0.50 s (the ceiling), bar 6 0.44 ->
  0.45, bar 94 0.41 -> 0.42, bar 113 0.32 -> 0.37, bar 166 0.37 -> 0.40, bar 204 0.44.
- **sfp at 592 (item 3)**, master: first 0.1 s minus the ff before -0.5 -> +0.2 dB; peak +0.5 dB at +0.235 s -> +0.4 dB
  at +0.020 s; 0.2-0.3 s -0.1 -> -1.6; 0.3-0.4 s -4.8 -> -5.6; the p (0.45-0.9 s) -7.4 -> -7.3. Stems, first 0.1 s /
  0.2-0.3 s: Bass trombone +0.3 -> +3.2 / +3.3 -> -1.7; Trombone 2 +0.7 -> +3.5 / +3.4 -> -1.6; Tuba +0.2 -> +2.9 /
  +2.9 -> -1.3; Horn 3 +2.6 / +2.7 -> -1.2; Horn 1 +0.3 / -0.5 -> -3.3; Trombone 1 -1.4 / -1.5 -> -4.3; Trumpet 3
  -0.5 -> +2.4 / -5.6. Target met (peak within +0.10 s, first 0.1 s at or above the ff).
- **Cello and viola same-pitch repeats (item 4)**, dip = body after the onset minus the minimum 20 ms RMS in the 150 ms
  before the note-on: Violoncellos 70 8.7 -> 15.0; 98 5.1 -> 11.4; 602 -5.5 -> 6.2; 604 5.8 -> 9.7; 606 6.3 -> 11.3; 608
  2.2 -> 7.0; 630 -2.1 -> 6.9; 658 2.5 -> 11.3; 325 2.6 -> 10.1 (3.8 before the notch); 327 8.4 -> 11.3; 832 -1.5 -> 6.2;
  Violas 728 -3.9 -> 7.1 (-4.4 before the notch). 12 of 12 sites at 6 dB or more (`logs/ver12_i4_final.log`).
- **Loud woodwind pitches (item 5)**, track minus Violins I over the 92 loud bars, median / 90th percentile: Flute 1
  +0.6 / +6.9 -> -2.3 / +3.0; Flute 2 -4.7 / +2.9 -> -4.6 / +0.9; Oboe 1 -1.6 / +4.5 -> -4.1 / +0.7. Flute 1 is the
  loudest stem in 23 -> 3 loud bars (90, 198, 249). Sites: bar 278 Flute 1 +2.4 -> -5.0; bar 91 +11.0 -> +4.1; bar 78
  +4.8 -> -4.9; bar 110 +8.4 -> +0.5; bar 254 +6.9 -> 0.0; Oboe 1 bar 246 +12.2 -> +7.3; bar 274 +9.2 -> +2.7; bar 226
  +6.9 -> +1.4; 900-905 +7.4 -> +1.9. Solo bars (track minus the loudest other stem, A): Flute 1 bar 43 +4.1 -> +5.1,
  44 +7.9 -> +7.7, 89 +7.3 -> +5.0, 102 +3.5 -> +1.6, 105 +8.6 -> +6.6; Oboe 1's solo bars unchanged.
- **Bar 275 (re-measured, nothing else done)**: loudest stem Trumpet 1 33.9 (second Trumpet 3 33.1), unchanged; Flute 1
  minus Violins I -0.7 -> -2.6; Oboe 1 minus Violins I +1.2 -> -3.3. Master K bars 273-278: 45.0 / 45.2 / 44.8 / 45.4 /
  47.5 / 49.8 -> 44.7 / 44.5 / 44.3 / 45.4 / 47.5 / 49.6.
- **Muted Trumpet 1 (item 6), balance**: Trumpet 1 minus cor anglais per bar (A), bars 171-174 and 179-183: -0.8 / -0.9 /
  -2.3 / -6.2 / -4.3 / -3.7 / -3.2 / +3.8 / -6.6 -> -2.7 / -2.3 / -2.0 / -2.8 / -2.8 / -2.2 / -3.0 / -2.1 / -3.2. All nine
  bars are 2-4 dB under: met.
- **Muted Trumpet 1 (item 6), joins**: not met. The 20 ms RMS dip of the item (new body minus the minimum in the 100 ms
  before the beat) has a median of 2.6 -> 2.2 dB with 7 of 22 joins inside 1.5-4.5 dB, but it mostly measures the
  sample: "Mute Sus" has its own amplitude flutter of about ±6 dB with a period near 120 ms inside held notes, the same
  in c11 and c12. Measured per pitch instead (`joins6b.py`: envelopes of harmonics 2-7 of the old and of the new pitch,
  40 ms window): the time in which both pitches are within 6 dB of their bodies went from a median of 34 ms (max 101;
  over 60 ms at 7 of 22 joins) to 70 ms (max 144; over 60 ms at 13 of 22); within 10 dB 89 -> 125 ms. The depth at
  which the two envelopes cross went from a median of -4.4 to -2.8 dB; it lies inside 1.5-4.5 dB at 11 -> 10 joins
  (c11: 10 deeper, 1 shallower; c12: 6 deeper, 6 shallower). The analysis window adds about 20 ms to each time. So the
  +30 ms overlap removed 4 of the 10 deep joins and doubled the two-pitch time; the coordinator's "no join holds two
  pitches for more than 60 ms" fails at 13 of 22 joins (7 of 22 already in c11 with a 7 ms data gap: the release tail
  holds the old pitch). The fix is MIDI data, so it waits for c13: overlap 0-0.01 s, or +0.03 s only at the joins that
  were deeper than 4.5 dB in c11 (685, 687, 688, 691, 692, 694, 715, 717, 719, 726). Note bodies by pitch: C4 -57.9 ->
  -55.1, D4 -57.4 -> -55.9, E flat 5 -48.5 -> -55.2, F5 -44.3 -> -51.0, G5 -44.2 -> -49.6 (`logs/ver12.log`,
  `logs/joins6b.log`).
- **Delivery ride (item 7)**, mp3: bar 41 -> 42 step 8.8 -> 9.7 dB (target 8.6 or more); bar 43 minus bar 42 -0.1 ->
  -1.1 (not above: met); bar 44 minus 43 +4.2 -> +2.8. Bars 169-174: -30.7 / -35.8 / -35.7 / -34.5 / -31.9 / -32.5 ->
  -30.4 / -35.0 / -36.8 / -35.0 / -32.3 / -31.6: bar 170 -> 171 now falls 1.8 dB (c11 rose 0.1; the master falls 3.6).
  Loudest bars 278 -14.0, 223 -14.4, 277 -15.4, 263 -16.1, 262 -16.8.
- **Tempo (item 8)**: bar starts 224-228 move by -0.024 / -0.055 / -0.087 / -0.087 / -0.087 s, 229-234 by -0.018 s, bar
  235 by +0.021 s; bar lengths 223 2.143 -> 2.119 s, 224 and 225 2.111, 228 2.212, 234 2.182. The cello re-bow dips of
  the held C3 went from 4.6 / 3.2 / 2.5 / 6.4 to 3.8 / 2.7 / 1.9 / 4.3 dB.
- **Basses' on-beat eighths (item 9)**, time from the beat until the 30-120 Hz level is within 3 dB of the slot's peak,
  span 1088-1108, downbeats / other beats: stem +88 / +86 -> +70 / +70 ms; master +20 / +14 -> +18 / +0 ms. The stem
  target (+40 ms or less) is not met: 18 of the 30 ms lead arrived. The beat-gap dip already ends at the moved onset,
  so there is no level-only fix. The other spans are within 8 ms of c11 on the stem.
- **fff at bar 263 (item 10)**: bar 263 minus bar 262 -0.7 -> +0.5 dB Z, -0.4 -> +0.8 K, -0.3 -> +1.0 A (262 Z 48.3 ->
  47.8, 263 47.6 -> 48.3). Trumpet 1 bars 262 / 263 / 264: 40.7 / 36.3 / 32.8 -> 38.7 / 40.3 / 36.6. Met.
- **Keep list**: basses' gap dips (30-120 Hz, on-beat / off-beat medians): stem 792-816 14.6 / 9.4 -> 13.6 / 10.3;
  816-840 and 1056-1088 unchanged; 984-1056 stem 18.9 -> 18.6 on-beat, master 7.8 / 7.5 -> 9.3 / 8.4; 1088-1108 stem
  10.6 / 7.1 -> 9.1 / 8.6, master 9.0 / 8.5 -> 8.5 / 10.3. The c11 bumps at 592 and the violas' chord-repeat gaps (slur
  starts 12.5 dB, louré 6.15) are unchanged. Bar 42: the master is 0.9 dB lower than in c11 because Violins I's note at
  164 came out 2.3 dB lower on unchanged data; the mp3 step grew. Wetness: see the decay times under item 2.
- **Flutes' pcx attack (item 11, not worked on)**: Flute 2 618 +49 and 650 +114 ms, unchanged. Flute 1 618 +28 -> -78,
  634 -64 -> -41, 650 -30 -> -51; Flute 2 1007 -38 -> +96, 1074 +49 -> +64 (unchanged data: state drift, see below).
- **Simulation against the render** (`simcmp12.py`; real master minus the master simulated before the render from the
  c11 stems, per bar, Z): 233 bars with unchanged data: median -0.00, 5th percentile -0.30, 95th +0.21, largest 1.80;
  34 bars with changed data: median +0.02, -0.18, +0.17. Off by 1 dB or more: bars 26 (+1.8), 30 (-1.1), 33 (-1.1),
  106 (-1.4), 169 (-1.1), each from a drifted note on a track with unchanged data.
- **Level changes without a data change** (coordinator, Movement II c49; `drift12.py`, c12 against c11, stem level
  minus the envelope difference where notes, keyswitches and controllers are equal; threshold 2.0 dB). Per-track bar
  medians are 0.00 on all 31 tracks. Tracks with a bar or a long note that moved 2 dB or more: Flute 1 (bar 28 -2.1;
  notes 74 +2.7, 423 -4.3, 634 -2.8), Flute 2 (1007 +6.1, 1074 -3.0), Oboe 1 (796 +3.7), Clarinet 1 (1084 +2.4),
  Bassoon 1 (106 -2.1, 119 -3.8, 1058 +3.6), Horn 1 (bars 14 -2.3, 143 +2.6, 217 -2.4; notes 570 +6.1, 866 -3.8), Horn 3
  (119 +3.9, 122 +3.7), Violins I (42 +3.7, 164 -2.3, 316 -2.4), Violins II (bars 15 -2.5, 113 +2.4, 155 -2.1; notes 42
  +4.9, 56 -3.4, 448 +2.4, 616 -2.7, 670 +3.3, 1060 -6.7), Violas (131 -2.4, 442 -3.1, 961 +2.3, 1014 -3.9),
  Violoncellos (bars 26 +3.6, 253 +4.5; notes 100 +3.9, 609 -2.9, 753 -2.3, 762 -3.2, 792 +2.8, 993 -3.9, 1009 +5.1),
  Double basses (114 +4.3). The other 19 tracks have none. Against c10: only 4 bars have equal data and envelopes on
  every track in c10, c11 and c12; on those the master moved +0.00 dB (median) from c10 to c11 and -0.05 dB (5th
  percentile -0.25) from c11 to c12. A per-track comparison with c10 was not possible: the c10 stems were deleted in
  c11 and only its master is kept.
- **Silent-note list**: Violins II 152 (ff) and 376 (mp) as in c11. New: Violoncellos 564 (mp, p47) at -10.8 dB A
  against the track's mp median of 10.9. Its data and envelope equal c11 (note-on 563.45, 5.31 qn, velocity 53,
  "Leg BC" keyswitch at 563.42 after a staccato B2) and its whole-note level moved only -49.4 -> -49.9, but its first
  0.6 s is 7-10 dB weaker than in c11 (200 ms steps: c11 -64 / -61 / -54 / -50 / -48 / -46, c12 -73 / -71 / -60 / -53 /
  -49 / -46); equal from 0.8 s on. Open for c13. Oboe 1 872 left the list with an unchanged level (-64.6): the track's
  median moved with the item 5 trims.
- **Loudness**: master -20.6 LUFS (c11 -20.3), LRA 22.9 LU (22.6), true peak +0.1 dBFS (-0.2), float sample peak 1.014
  (0.972; 2 samples over 1.0 at 420.953 s in the final chord, every stem under 0.4). Delivered mp3 -19.7 LUFS (-19.8),
  LRA 14.6 LU (15.0), TP -1.5 dBTP (-1.6), limiter about 2.6 dB (1.6; pre-limiter peaks +1.11 dBFS at 420.98 s and
  +0.11 at 419.33 s), p10-to-max span 19.0 dB (19.3), ride +12.2 / -2.1 dB, length 425.15 s. The limiter figure rose
  with the removal of the 167 Hz bell (simulated 2.2 dB before the render); it is under the 3 dB limit.
- **Attack probe**: 1 flag, Violoncellos qn 24 +0.43 s (limit 0.15), the known build-shape artefact (c10 and c11 +0.43 s).

## Open after this cycle
- Item 6 joins: two-pitch time over 60 ms at 13 of 22 joins (see above; needs MIDI data).
- Item 9: basses' on-beat eighths in 1088-1108 at +70 ms on the stem (target +40); master +18 / +0 ms.
- Item 1: master low band 22.3 and 20.8 dB under the full band in bars 255 and 256 (target 17; the basses' stem is
  inside B's range).
- Item 11 (not worked on): Flute 2 at 650 (+114 ms) and 618 (+49 ms), Bassoon 1 at 464.
- Violoncellos 564: the first 0.6 s is 7-10 dB weaker than in c11 on equal data.
- The notes that moved 2-6.7 dB on unchanged data (list above), among them Flute 2 1007 (+6.1 dB, attack -38 -> +96 ms)
  and Violins II 1060 (-6.7 dB).
- Delivery: limiter 2.6 dB (limit about 3); bar 2's stop decays to -20 dB in 0.50 s, which is the wetness ceiling.

## REAPER
- Waited for the Scherzo's c11 actor (lock held from 16:44:46; this cycle's waiter started 17:09:02). Lock
  17:23:32-18:14:40 (51 min). Movement I's c53 actor was waiting behind it.
- start 17:23:44-17:24:19; open 17:24:26-17:24:43 (35 tracks); `--midi-only --tempo` of all 31 tracks
  17:24:57-17:25:36 (tempo map 434 markers, no mismatch); save; `state_guard.py` 0 stale; restart 17:26:11-17:28:11;
  memory settled at 44 GB (10-11 GB compressed) by 17:39; audio device closed and reopened 17:41:02 (48 kHz, 512, no
  input); render with `--force-memory` 17:41:08-17:54:46 (exit 0); measurements and the notch simulation; `--mix-only`
  of Violoncellos and Violas 18:13; save; quit 18:14:36; unlock 18:14:40.
- REAPER memory after the render: 45 GB, 29 GB compressed (`top_after_render.txt`); idle at 18:00 and 18:13: 44 GB,
  44 GB compressed.
- Disk: 70 GB free before the render. The c11 stem WAVs are deleted (`cycles/c11/render/00_Master.wav` and the c11 mp3
  are kept, as is `cycles/c10/render/00_Master.wav`); 64 GB free now.

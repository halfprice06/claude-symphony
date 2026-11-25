# Cycle 54 (actor): the bottom octave, notes that fell out of their lines, the ff cadence

Rendered 2026-11-11 07:56-08:04 (one full render; five range passes before it), one stem fix after it (Clarinet 1).
Critic reports `reports/A.md`, `B.md`, `C.md`; the lead's merge (`lead_c54.md`) was followed and wins where it differs
from a report. Every table edit is in `actor_scripts/edits54.py` (computed from `before/`), every rule entry in the c54
block of `build/score_config.py`. All level changes were simulated on the c53 stems first (`sim_final.txt`); the render
agrees with the simulation within 1.5 dB on 178 of 196 figures, the other 18 being the two changes that were not
level-only (Violins II 154 and its linear diminuendo) and the basses' EQ (`tcmp_c54.txt`).

## 0. First: the c53 stem-fix rows
`--mix-only` from `cycles/c53/build_fix` on Violins I, Violins II, Violas, Violoncellos, save, state guard 0 stale
(`build_mix_c53rows.log`, `state_guard_after_c53rows.json`), before any c54 data.

## 1. Mix (B #2, C #1): Double basses EQ, `build/mix.json`
Simulated on the c53 stems (`mixsim54.py`; `mixsim_C.txt`, `mixsim_C2.txt`, `mixsim_B.txt`, `mixsim_final.txt`):

| share of the master, dB | c53 | (C) row kept | (C2) row removed | (B) bell2 -2 | taken | c54 render | Brahms 1/ii, 4/ii |
|---|---|---|---|---|---|---|---|
| 56-112 Hz, whole | -15.2 | -10.7 | -10.8 | -12.8 | -11.6 | **-11.5** | -7.9, -7.3 |
| 70-112 Hz, whole | -16.5 | -13.0 | -13.3 | -14.5 | -13.8 | **-13.7** | -10.3, -9.5 |
| 56-112 Hz, bars 61-62 | -17.2 | -11.4 | -11.4 | -14.4 | -12.4 | -12.2 | |
| 56-112 Hz, bars 71-78 | -15.4 | -9.5 | -12.3 | -12.0 | -11.6 | -11.5 | |
| 56-112 Hz, bars 79-81 | -16.0 | -9.7 | -9.7 | -13.0 | -11.1 | -11.0 | |
| 56-112 Hz, bars 83-92 | -8.0 | -6.5 | -6.5 | -6.5 | -6.7 | -7.0 | |
| 140-355 Hz, whole | -5.8 | -6.1 | -6.1 | -5.9 | -6.0 | **-6.0** | -9.1, -8.5 |

Taken: variant C with two values between. `bell2` 80 Hz -6 removed; `bell` 140 Hz +4.5 -> +2.0; the c41 `loud_eq` row
(80 Hz, qn 254-262) +4 -> **+2** (with +4 the passage rose 2.06 dB more than the bars around it at 56-112 Hz, over the
lead's 2 dB; without the row 1.46 dB less; with +2: 0.0); the climax row's 100 Hz shelf -3 -> **-1.5** instead of
removed (kept at half as the guard for the D flat 2 at 204 / 262, series 1 c16). Coda: `roles.json` Double basses
`[273.9, 283.0, 2.0, 1.0]` -> 1.0.
The lead's limits on the taken variant, c53 -> c54 render (`shares_c54_fix.txt`, `boom_c54_fix.txt`): largest per-bar
K-weighted rise from the EQ +0.79 dB simulated (bar 84; in the render bars 83-85 rise under 0.5 dB; the only bar over
1 dB is bar 10, +1.75, which is Horn 1's pitch trims, section 2); delivered span 18.1 dB (19), limiter 1.0 dB (3);
master sample peak 0.581 -> 0.606. Boom check at 56-112 Hz (each bass note against the mean of its two neighbours):
the largest growth of a note's excess is 3.3 dB (limit read as 4); two notes cross 4 dB by this measure (E1 at 210:
+1.9 -> +4.5; E flat 2 at 268: +1.4 -> +4.1), which the shelf does not change (it lowers the neighbours alike); the
measure already had 27 of 110 notes over 4 dB in c53 because neighbours on other pitches have their fundamentals
outside the band. Celli and 140-355 Hz were not cut further.

## 2. Levels (in the render)
- **B #1** (before / note / after, dB; c53 -> c54): Flute 1 133.5 -56.5 -> -47.6 (a `LEVEL_SHAPES_S` shape that follows
  the note's decay, to +12 dB, gone at the next note-on), 135 -53.1 -> -49.1, 199 -42.4 -> -35.4; Violins II 47
  -57.7 -> -49.8 (+8, B +7); Violoncellos div 63 -54.5 -> -46.8; Violoncellos 68.5 / 240.5 / 249 / 77 / 199
  -42.9 / -46.7 / -48.1 / -48.2 / -37.4 -> -41.2 / -42.2 / -44.1 / -44.2 / -32.9; Bassoon 1 201 -42.5 -> -34.5 (as a
  `level_fits.json` row: as a note trim it moved S by 26 ms in the simulation). Ten of the eleven within 3 dB of the
  mean of their neighbours (Violins II 47: 3.2).
- **A #2**: Violoncellos 253 and Violins I 80, A's shapes. 100 ms steps from the beat, 253: -39.8 -39.3 -39.6 -40.3
  -42.6 -46.5 -> -35.2 -34.7 -33.4 -33.3 -36.5 -39.1; S -14 -> -4 ms. Violins I 80: on the beat -39.9 -> -36.9, S
  -5 -> +1 ms. Violins II 146: closed without a shape.
- **C #3** Horn 1 `pitch_trims.json`: 56 +3, 55 +2.5, 67 +2, 68 3 -> 5, and 53 (F3) +2.5 (the pickups at 17.5 / 29.5
  were 3-4 dB under both neighbours); onset 39 in `_skip_onsets`. Theme bodies 17-39: 18: -42.8 -> -39.8, 26 / 27:
  -41.7 / -41.1 -> -38.7 / -38.6, 30: -44.0 -> -41.0, 35 / 36: -39.4 / -40.9 -> -37.4 / -38.9, 39 stays -41.2; the
  diminuendo of bars 12-14 now runs -33.5 -37.4 -38.9 -36.9 -38.9 -41.3 -40.3 -41.2. Other passages with these
  pitches: 175 (+2.4, still 5.7 dB under its neighbours), 188 (+2.0, from 2.8 dB under its neighbours to 0.8), 210
  (a skipped onset): no narrowing needed.
- **B #5** Horn 1 pickup 195.5: shape +4 -> +7.5 dB: body -33.0 -> -29.6 (E flat -29.8, F sharp -27.9); gap floor
  -42.2 dB unchanged, breath dip 8.9 -> 11.7 dB by `breath52.py`.
- **B #3** Violas 81 / 82 +5 dB: -44.7 / -45.9 -> -39.7 / -40.9. Bassoon 1: role `[200, 204, -4]` -> **-2.5** (B: -1,
  which put the note at 202 2.5 dB over the ff after it), note trim 199 +2, `dyn_trim_db` ff 1.5 -> 3.0: bodies
  198-210 -33.2 -36.3 -36.9 -42.5 -34.0 | -34.1 -33.6 -> -33.2 -34.3 -35.3 -34.5 -31.4 | -32.6 -32.1.
- **C #4** the ff cadence. The rule behind the 3 dB fall over 266-267: the hairpin gain of the crescendo 261-262
  (`HP_GAIN_DB` +3, held to the first onset after the arrival, 266, released over `HP_REL` 1 qn). A `LEVEL_SHAPES` row
  cancels the release up to 268. Violins I +2 / Violins II +1.5 dB over 262-268 as shapes that begin 0.45 s after
  the beat (C's role edits moved S at 262 and 268 by 32-35 ms in the simulation). Violins II: `HP_CURVE["linear"]`
  (268, 271); re-bow fill at 263.921 +2 dB. Per quarter 262-270, c53 -> c54: Violins I -29.7 -30.6 -29.8 -29.3 -33.0
  -35.0 -32.9 -38.2 -39.2 -> -28.8 -28.6 -27.8 -27.3 -29.4 -30.1 -32.5 -38.2 -39.2; Violins II -32.3 -33.5 -36.2
  -34.8 -33.6 -35.3 -35.4 -36.3 -35.4 -> -31.8 -32.0 -32.7 -31.2 -30.2 -31.2 -33.9 -38.0 -37.0 (the 13.3 dB step at
  271 is now 11.8). Master bars 79-80 +0.6 / +0.7 dB; bar 61 stays about 4 dB louder.
- **C #5** Violoncellos 188-196: the row that took the crescendo back was `note_trims` 193 -3 (with the f trim, 1.6 dB):
  193 -> +0.5. Per half bar 188-196: -36.0 -32.8 -32.6 -35.1 -30.3 -> -36.0 -32.8 -31.0 -32.9 -30.3.
- **B #4** `JOIN_NOTCH_S`: Violins II 177 (-0.12, -0.02, -4.5): burst -31 / -30 -> -36 / -35 dB; Violins I 65.5
  (-0.14, -0.05, -3): -37 / -36 -> -40 / -39; Violins I 86.5 depth -4.1 -> -6.0 and body +2.5: peak over body under
  3 dB.

## 3. Timing and articulation
- **A #1 Clarinet 1 289.** The gap was not set by `gap_s`: the 286 note is on the legato row and ends 0.01 qn before
  the keyswitch to Sus Non Vib, which lay `KS_LEAD` 0.06 qn before the note. New generic `KS_LEAD_AT` (keyswitch 0.02
  qn before 289): gap 81 -> 46 ms. Range pass: the stem's dip did not shrink (9.3 -> 10.0 dB; its floor is the
  release under the slow start of the new note), so a fill over the join was added, rendered at +5 dB (stem dip 4.7,
  master 6.3, a bump before the beat) and refitted in the stem fix. Delivered: stem dip 9.3 -> **3.3 dB**, master dip
  7.9 -> **5.6 dB** (A wanted 4; Horn 3 and Violins II dip at the same moment, and the stem is at S1's 3 dB minimum).
  The "Leg Slur Rep" row was not tried.
- **A #3 Violins II 154.** Lead 160 -> 280 ms (range pass: crossover +396 -> +310 ms, the lower pitch's own band 6 dB
  down at +174 -> +70 ms) -> **350 ms**, the clamp: crossover +244 ms, own band at **-8 ms** (A: within 40 ms),
  identical in two passes and in the full render. Level steps from the beat -49.5 -52.7 -56.9 -53.5 -53.7 -> -52.2
  -49.6 -50.6 -48.7 -46.4 with A's +4 dB lift.
- **A #4 Violoncellos 68.** Lead 350 -> 300 ms (`leg_leads.json` 0.08; the row lead is 0.22 s): S / pcX -65 -> **-14 ms**
  (range passes and render). 68.5: +10 -> -2; 77: -49 -> -15 ms with B's body row.
- **RR_RESET trial (adopted).** `RR_RESET_AT["Violins II"] = [58.0]`. Passes p1 / p2 (no reset) agree to 0 ms, q1 / q2
  (reset) agree to 0 ms; 9 of 24 joins of bars 22-30 differ by 15-87 ms between the two states, and the reset passes
  give exactly the c53 full render's values (66 / 72 / 75: -18 / -47 / -3 ms; without: +49 / +40 / -51). The full
  c54 render repeats them again (`S_moved_c54_fix.txt`).
- `tools/s_onsets.py`: octave joins (S = crossover, `old_fall6`) and the `flat` flag.

## 4. Render, state, checks
- Master -22.8 LUFS, LRA 23.8, true peak -4.4 dBFS, sample peak 0.606 (c53 -22.9, 23.4, -4.7, 0.581). Delivered
  -19.8 LUFS, LRA 15.1, TP -1.6 dBTP, limiter about 1.0 dB, span 18.1 dB, 347.40 s (c53 -19.8, 14.8, -1.6, 1.2, 18.3).
  Attack probe: late or hole 0.
- S (`S_report_c54_fix.txt`): all 727 joins within 25 / 60 ms 642 / 710 -> 640 / 711; lines outside 25 / 60 ms 54 / 11
  -> 54 / 10. Moved 20 ms or more on unchanged data: Bassoon 1 262 (-2 -> +48 ms), Violins II 270.5 (-20 -> +1).
- Wetness t20 (`check52.py`): strings 0.429 s, winds 0.284, brass 0.272; final chord 0.455 s. S1: own-band median
  7.8 dB, under 3 dB 5 of 49 (c53: 8.0, 4). S3: master dip at 196 / 204 3.6 / 3.4 dB. Join peaks 6 / 8 dB over both
  bodies 19 / 5 of 460 (20 / 5).
- state_guard: 0 stale of 32 before the work, after the c53 rows, after the `--midi-only`, before the restart, inside
  `render_cycle.py`, after the render, after the stem-fix `--mix-only` and on the project saved by quit. state_check
  against c53: no state run, no timing run.
- REAPER 39 GB / 0 compressed before the render (no `--force-memory`), 40 GB / 0 after. Audio device at every reading:
  CoreAudio, Mac Studio Speakers, 48000 Hz, 512, no input; no setting changed.
- Builds: `--mix-only` 4 (c53 rows) + 2, `--midi-only` on 10 tracks, Violins II and Clarinet 1 once more, Trombone 1
  rebuilt in full, `--mix-only` Clarinet 1 after the stem fix. **REAPER holds every row of the delivered render.**
- Lock: first wait 21:14-21:59 on 10 Nov (run stopped by the usage limit, lock never held); second wait 04:57-07:16;
  held 07:16:39-08:09:04 = **52 min**, no idle time; REAPER quit and unlocked before the remaining analysis.
- Disk: 75 GB free before the render, 69 GB at the end. Range-pass audio deleted; scratch deleted.

## 5. Not done / open
- Clarinet 1 289 master dip 5.6 dB (4 wanted): next step the "Leg Slur Rep" row (a full rebuild of Clarinet 1) or less
  dip on Horn 3 / Violins II at the same beat.
- Violins II 154: crossover still +244 ms at the lead clamp (the octave transition at pp is slow).
- A #6 (test only, `a6_c53.txt`): the master dips at 293.15 / 293.83 / 294.42 vanish when either the Clarinet 1 stem
  or the Violins I stem is taken out: two sources on one pitch at near-equal level. No fix made.
- The boom measure needs neighbours on the same pitch class to mean anything; E1 at 210 and E flat 2 at 268 stand
  4.5 / 4.1 dB over their neighbours at 56-112 Hz.
- Violins II 47 is 3.2 dB under its neighbours (3 wanted); Violins II still 11.8 dB down at the barline of 271.
- Not tried: wind legato velocity, Port LITE / Leg Runs, the mono divisi layer. `loop/MANUAL-GAPS.md`: no item tried
  (item 2's "Leg Slur Rep" named as the next step for Clarinet 1 289).

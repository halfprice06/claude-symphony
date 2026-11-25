# Cycle 14 changes (actor, 2026-11-10)

Scripts: `cycles/c14/actor_scripts/` (`rr.py` range renders and the "two renders are equal" test, `smeas.py` measure S,
`refit2.py` second lead step with the neighbour rule, `pluckfit.py` pizzicato trims, `post14.py` item checks,
`leadcheck.py`, `pn2.py`, `wait_lock.py`, `settle.py`, `p1.sh`, `p1_analyse.sh`, `p2.sh`, `after.sh`; `pcx51.py` is
Movement II c51 critic A's `pcx.py`). Logs: `cycles/c14/logs/`. Snapshot of tools and tables before the cycle:
`cycles/c14/before/`. Reports: `cycles/c14/reports/A.md`, `B.md`, `C.md` (on the c13 render).

parts.json against c13: 0 warnings; no track's Opus state inputs change (`cycles/c13/actor_scripts/statecmp.py`), so
every track is written with `--midi-only --tempo` (the tempo map changed). The re-bow lists are equal, so
`space_rebows.py` was not run.

## What changed

### Tools

1. `tools/build_reaper.py`: `PRE_RR_RESET` (item 1). CC16 127 (parts.json `rr_reset_cc`, Opus's own reset controller)
   at `RR_RESET_QN` in the pre-roll of every track that already gets the CC36 reset (all but the harp), as Movement I
   c43 and Movement II c45 do. `REP_OFF_FAMILIES` is unchanged (strings only): see "Not taken".
2. `tools/score_to_parts.py`:
   - `RR_RESET_ALL_AT` (list of score qn), `RR_RESET_ALL_SKIP`: a CC16 reset on every pitched track 0.02 qn before the
     moved onset of its first note at or after each listed qn. A section's takes then do not depend on the data before
     it, and a range render that starts before a listed point plays the takes of the full render.
   - `RR_RESET_KS_RESTATE` (default True): before each such reset that lies in a rest the keyswitch in force is sent
     again (parts.json `ks` entries with `"restate": true`). REAPER does not chase keyswitches into a time selection.
   - `HP_CURVE["decresc_last_max_qn"]` and `["decresc_last_min_s"]` (critic C #2): a diminuendo longer than max_qn stays
     linear; a last onset less than min_s before the hairpin's end is not used for the "falls on its last note" curve.
   - `ROW_SLUR_OVERLAP_S`: a negative value is a gap (the note before ends that long before the moved note-on).
   - `ROW_TRIM_STROKES` {track: [score qn]}: listed `DOWNBOW_STROKE_AT` strokes take the `ROW_TRIM_DB` row trim and
     count as the Leg-row neighbour of the notes around them.
3. No change in `render_cycle.py`, `deliver_master.py`, `stem_fix.py`, `state_guard.py`, `measure.py`,
   `probe_attacks.py`.

### Config (`build/score_config.py` c14 block, `build/*.json`)

Item 1, repeatability. `RR_RESET_ALL_AT` = 40, 104, 168, 200, 264, 328, 392, 456, 536, 600, 680, 744, 792, 840, 888,
936, 984, 1056, 1088 (the rehearsal letters and the starts of the pizzicato / solo passages). The c13 `RR_RESET_AT`
points stay (pizzicato 200 / 201, the basses' spans, the crash strokes).

Item 2, timing.
- (a) `DOWNBOW_STROKE_AT` ("Sus MAX" strokes; the slur's next note joins from them), with a `ROW_LEAD_S` span (0.06 s;
  0.09 s after the range pre-check on Violins I 97.5 and 610, Violins II 310, Violas 76 and 642), `ROW_LEAD_KEEP_END`
  and the row trim of the notes around them (tools: `ROW_TRIM_STROKES`): Violins I 50, 66, 82, 97.5, 134, 610;
  Violins II 50, 66, 82, 97.5, 310; Violas 76, 610, 642; Violoncellos 114, 130, 310; Double basses 114.
  Not a stroke: Double basses 130 (the same-pitch note at 131 would start as an unled "Leg Slur MAX" note). The
  unslurred note after the strokes at 66 (Violins I and II, qn 68) is now a "Sus MAX" note with a 0.09 s lead (it was a
  "Leg BC MAX" target). These strokes do not add row changes: the row change moves from the stroke to the note after it.
- (a) The entries of bars 67 and 187 (Violins I / II 264 and 744, Violoncellos 264; the task's "748" is read as A's
  744): tried as strokes in the range pre-check and taken back. The "Sus MAX" stroke at that level rose as slowly as the
  legato first note (Violins I, 100 ms steps from the beat: c13 -51 -48 -43 -39 -37, stroke -55 -50 -43 -44 -39 dB).
  They stay legato entries, with `entry_leads.json` +0.10 s (total at the 0.30 s cap) and a +5 dB front after the fader
  (`LEVEL_SHAPES_S` `[(-0.33, 0), (-0.31, 5), (0.12, 5), (0.40, 0)]`).
- (a) `entry_leads.json`: Double basses 128 +0.10 (realised +51 ms), Violins I 824 +0.12, Violins I 806 -0.05 (with a
  listed extra the entry branch gives the note the family and row entry lead it did not have: total 0.09 s, A asked
  +0.09). Not listed: Bassoon 1 118 (a row there removed its 35 ms re-tongue lead) and Bassoon 1 472 (a row left 7 ms of
  the printed breath before it; 89 ms without).
- (b) `leg_leads.json`, string tracks: A's table (new = old + 0.9 x S); the rows of notes that became strokes
  are removed. 12 table rows are entries, not legato targets, and went to `entry_leads.json` (Violins I 40, 72, 608,
  656, 792.5; Violins II 40, 72, 80, 96, 600; Violas 656; Double basses 112; after the range pre-check Violins II 600
  and Violas 656 were removed again, and `leg_leads.json` Violins I 51 and Violoncellos 115 went back to their c13
  values, Violoncellos 311 +0.069 -> +0.01: see the pre-check below). 18 table rows have no effect in the build
  (lead at the 0.9 cap of the note before, or not a legato target) and are left at their c13 values: Violins I 135.244,
  135.496, 135.748, 283.5, 285, 310, 676, 765, 808, 810, 947.5, 982; Violins II 285, 670; Violas 92; Double basses 115,
  118, 120. Every other row moved its note-on within 12 ms of the request (`leadcheck.py`; list in
  `logs/leg_leads_refit.log`).
- (b) winds and brass, no per-onset fits: `LEG_ART_EXTRA_S["Horn 1"]` "Leg Slur MAX" +0.02 s; `ROW_LEAD_S["Horn 1"]`
  "Sus MAX" 0.04 s at 52, 68, 612, 628 with `ROW_LEAD_KEEP_END`; `LEG_VEL_EXTRA_S["Trumpet 1"]` +0.02 s over velocity
  118 (the p solo at velocity 96 is not touched); `entry_leads.json` Horn 1 605, 621, 637, 653, 1061, 1069 -0.10 s (one
  value for the class "Leg Slur MAX after a Marc Shrt quarter"). Trombone 1, Bassoon 1's joins: no change (medians +2 /
  +3 ms, mixed signs).
- (d) Bar 75: Violins I 299 0.03 -> -0.04, Violins II 300 -0.055 (both in A's table).
- Tempo: `CAESURA` 72: 0.06 -> 0.03 s, 104: 0.08 -> 0.035, 392: 0.08 -> 0.035, 632: 0.06 -> 0.03, 664: 0.06 -> 0.03,
  816: 0.05 -> 0.025, 1108: 0.10 -> 0.04 (no printed mark at any of them; each beat now under +5 %, was +7.0..+12.0 %).
  `PHRASE_ARCS` (248, 264) "main" -> "sub" and (760, 776) default -> "sub" (+9.4 % and +6.4 % -> +3.7 %; no breath mark
  at 264 or 776). Kept: the arcs that end on a printed breath mark (232, 296, 712, 744, 856, 872, 912, 968) and every
  printed rit. / allargando / stringendo ramp.
- Item 6, muted Trumpet 1: `ROW_SLUR_OVERLAP_S` -0.045 s at 684, 686, 716, 718 (a 45 ms gap; lead unchanged).

Item 3, dynamics.
- C #1, bar 222: `ART_SPANS` Violins I 883.9-886.0 "Sus MAX"; `LEVEL_SHAPES_S` Trumpet 1 and Horn 1 at 884
  `[(-0.05, 0), (-0.03, 4), (0.30, 4), (0.55, 0)]`; the cello trim is C #5.
- C #2, bars 39-41: `HP_CURVE` `decresc_last_max_qn` 6.0, `decresc_last_min_s` 0.35. CC11 on the violins over 152-164
  is now 114, 96 (155.1), 77 (158.5), 68 (160), 47 (163.75); it was 114 -> 90 by 163.4, then 46. Other diminuendos whose
  lane moved by 4 CC or more: 668-676 (7 tracks, up to 24 CC), 673-676 (Violins I / II, 13), 725.5-728 (Violas, 6),
  959-968 (Violins I / II, 12).
- C #3, stringendo: `SHARED_HP["Violins I"]` (978.0, 984.5, "cresc"); `LEVEL_SHAPES` Horns 1-2 and Trumpets 1-2
  `[(978.5, 0), (982.6, 3), (982.9, 3), (982.95, 0)]` (C's row ended at 983.85, inside the led notes of 984).
- C #5: `pitch_trims.json` Violoncellos 43 -4.0, 44 -3.0 (all articulations); `roles.json` Violoncellos [592, 600, +1.5]
  (simulation: the 31.5-125 Hz share of bar 149 fell 2.0 dB with the trim, limit 1.5).
- C #6: `LEVEL_SHAPES_S` Clarinet 2 at 184 and 680, Clarinet 1 at 200, Bass clarinet at 680
  `[(-0.085, 0), (-0.04, -18), (0, -18), (0.8, -6), (1.6, 0)]` (the note-ons are 32-35 ms before the beat; C's first
  point at -0.05 s would have stepped after the note-on).

Item 4, balance.
- B #2: `LEVEL_SHAPES_S` at 40 on Violins I, Violins II, Violas `[(0.05, 0), (0.15, -2), (0.70, -2), (0.90, 0)]`; lifts
  of the second note as level shapes with the short mirror ramp at the target's moved note-on: Violins II 42 +1.5, 74
  +3.5, 602 +3.0, Violas 42 +1.5 (`LEG_RAMP_OK` lists them).
- B #3: `mix.json` Flute 2 `dyn_trim_db` f -1.5 -> -2.5, ff -1 -> -2.0 (B: -3.0; simulated on the c13 stems, -3.0 put
  Flute 2 1.6-3.0 dB under Flute 1 in bars 158, 252, 272); `pitch_trims.json` Flute 2 89 -2, 91 -3, 93 -4;
  `roles.json` Flute 1 [952, 964, -3.0].
- B #5: `note_trims.json` Harp 524 -5 -> -9; Clarinet 1 481, 483, 484 -4 -> -7.
- A #3: `LEVEL_SHAPES` Trumpet 1 and Trumpet 2 at 987.16-988.97 (+7) and 990.61-999.95 (+4 / +2, then +7), A's values.
- Coordinator: the release fades after the stops of bars 6 and 94 (`POST_SHAPES_S` 21.0 and 374.0, celli and basses)
  -6 -> -5 dB.

Score change during the cycle (coordinator, 2026-11-10): bar 90 (qn 356-360), Oboe 1 and Clarinet 1: the run is B flat,
C, D, E flat in eighths from 356.0, an accented F quarter at 358.0, rest on beat 4. LilyPond was run again
(`build/mockup.midi`, `mockup-events.tsv`); only Oboe 1 and Clarinet 1 events in 356.5-359 changed. No config row
referred to the removed notes (leg_leads, entry_leads, note_trims, roles, LEVEL_SHAPES checked); the volume envelope
returns to its level before the tracks' next note at 360. After the range pre-check (S at 358: Flute 1 +28, Oboe 1 +14,
Clarinet 1 +40 ms): `ROW_LEAD_S` Flute 1 "Sus MAX" 0.015 s and Clarinet 1 "Sus Non Vib" 0.03 s at 358, note ends kept.

Item 4, pizzicato (B #1): `build/pluck_trims.json`, fitted by `pluckfit.py` on the two range renders (every pluck
equal in both): 46 cello and 33 bass plucks in 200-264, 456-488, 680-744, each trimmed to its track's median (clipped
to +-6 dB), as seconds-keyed shapes from just before the pluck's note-on to just before the next note-on.
`note_trims.json` Double basses arco 276 -4.0, 278 -3.5, 294 -4.0, 296 -4.0, 299 +4.0 (3 dB or more off the running
median of five notes). The pizzicato takes after the reset at 200 were the c13 takes (the fit on c13 gave the same
bass values), so B's table would have been valid for the basses; it was refitted anyway because the cello pitch trims
changed the cello levels.

Item 5, delivery: `RIDE_TRIMS` rows 163.95 and 679.0 replaced by two rows fitted on the c14 master (`ridefit.py`,
`logs/ridefit_1.log`): the gain rises through the printed diminuendos (152-166, 664-678) and is flat over 166-198 and
678-743.

### Not taken, rejected or deferred

- Movement I c54's one-row theme (`STEADY_LINE`, arrived during the lock period): not ported. It needs the rule's five
  code sites, per-note level steps fitted on a render and probably a new row ("Sus Marc LITE" is not loaded: an Opus
  state change on three or four string tracks at 44-45 GB). First item for c15, with the coordinator's caveat (measure
  the start against the body of quarters and longer notes; do not use the row there if the body is over 4 dB under).
- Keyswitch 0.15 s early on row-change joins of one string track (Movement II c52): `KS_LEAD_S` is one value for all
  tracks, so it needed its own build and range pair. c15.
- `REP_OFF_FAMILIES` on winds and brass (B): not tested. CC69 0 turns the Repetition script off, which changes how
  repeated wind and brass notes sound, and it could not be separated from the CC16 result without a second build. After
  the reset the wind and brass notes that still differ between two renders are legato-row notes (below), which the
  Repetition script does not explain.
- `refit2.py`'s "second step" and "new row" proposals (15 rows): not applied. The notes they name are row-change joins,
  which take one of two start times from render to render (below); only its four reverts were applied.
- Bassoon 1 464 -0.04 s (A): the c13 level shape at 464 is placed on that note's lead (do-not-touch).
- Trombones' staccato eighths at 996-997.5 (A #3, second part), Horn 1's stopped note at 668 (A), the timpani plateau
  of bar 278 (C): not in the coordinator's list.
- A #4's bass notes outside 264-300 (348, 352, 410, 620, 632 ...): c15, on the c14 render (they were measured on takes
  that the section resets changed).
- Flute 2 at 618 / 650, woodwind width, the brass chorale lean-off, C #5 / C #6 of c12: as ruled.

## Lock period (2026-11-10, 11:22:25 to 12:19:11, 57 minutes)

Waited from 08:33 behind Movement II (to 09:06) and Movement I (to 11:22), `wait_lock.py`. Start and open 2.5 min,
settle 10 min (45 GB, 33 GB compressed), `--midi-only --tempo` build of all tracks 35 s (`build1.log`, 0 full
rebuilds), two range sets 9 min, analysis and edits 3 min, `--midi-only` build of seven tracks (`build2.log`), save,
state guard 0 stale, restart. The restart "settled" at 25 GB while the samples were still loading at about 0.6 GB/min
(the c05 trap); `p2.sh` was stopped before the render and `p2b.sh` waited for 44 GB (12:06). Render 12:06:46 to
12:16:19. Quit, state guard on the saved project 0 stale, unlock.

### Item 1: two range renders of one project (`logs/eq_Ra_Rb.log`, `shiftrep_Ra_Rb.log`)

Ranges (score qn): 37-138, 198-330, 352-362, 390-428, 454-490, 534-574, 598-746, 981.5-1016 (the coordinator's five
places are inside them), rendered twice in a row from the build with the pre-roll and section resets.
- Notes of 0.9 qn or longer and every pizzicato note, counted from each track's first reset inside the range: 2036 of
  2123 equal within 0.5 dB, 52 differ by more than 1 dB, 17 by more than 2 dB. Before a range's first reset: 85 of 214
  equal (takes before a reset are arbitrary in a range render).
- c13 drift-list notes inside the ranges: 54 of 64 equal within 0.5 dB. Every pizzicato note is equal to 0.00 dB (the
  cello notes that had moved by up to 9.7 dB with the c13 reset). Not equal: Horn 1 74 (+5.1 dB), Bass trombone 410
  (-5.2), Contrabassoon 119 (-4.0), Violins I 42 (-3.5), Violas 131 (-3.4) and 994 (-3.3), Trombone 1 410 (-2.9),
  Oboe 2 991, Bassoon 1 106, Flute 1 74.
- Every note that still differs by more than 2 dB is a legato-row note ("Leg Slur MAX" / "Leg BC MAX"). On measure S,
  of the notes that moved 25 ms or more between the two renders, 42 are row-change joins (of 300), 7 same-row joins (of
  537), 9 entries (of 180). The shifts are near fixed values (Violins I / II -92 to -129 and +93 to +100 ms, basses
  -73 / +69, Horn 1 -112 to -146). This is Movement II c52's finding: a legato target whose row differs from the row
  of the note it joins takes one of two start times, and its level over a fixed window moves with it.
- Result: the reset makes round-robin takes repeatable (pizzicato, sustains, short rows); it does not make row-change
  legato joins repeatable. It does no harm and stays. The full render's notes on the 24 tracks with unchanged data
  equal the first range render within 0.5 dB on 991 of 1030 notes (5 over 2 dB, all legato-row notes), so a range
  render that starts before a reset can be used to fit levels.

### Item 2: timing on measure S (`logs/S_table_c13_Ra.log`, `logs/render/S_table.log`; notes outside 25 ms / 60 ms)

| segment | notes | c13 render | range render Ra (first build) | c14 render |
|---|---|---|---|---|
| bars 11-26 (Violins I, II, Violas, Horn 1) | 256 | 138 / 46 | 111 / 34 | 104 / 30 |
| bars 27-34 (five lines) | 175 | 90 / 26 | 76 / 17 | 77 / 12 |
| bars 51-66 (Trumpet 1) | 41 | 10 / 1 | 10 / 1 | 10 / 1 |
| bars 67-82 (Violins I, II, Violoncellos) | 140 | 86 / 26 | 60 / 18 | 64 / 20 |
| bars 151-170 (five lines) | 325 | 141 / 58 | 105 / 26 | 118 / 29 |
| bars 171-186 (Cor anglais, Trumpet 1) | 65 | 19 / 6 | 19 / 5 | 20 / 5 |
| bars 187-198 (Violins I, II) | 62 | 37 / 14 | | 27 / 5 |
| bars 199-210 (Violins I, basses) | 150 | 55 / 11 | | 53 / 9 |
| bars 211-222 (Trumpet 1) | 16 | 6 / 4 | | 8 / 4 |
| bars 235-246 (Violins I) | 33 | 26 / 6 | | 17 / 6 |
| bars 247-270 (Trumpet 1, Horn 1, Trombone 1) | 120 | 68 / 28 | | 56 / 23 |
| all 29 lines | 1383 | 676 / 226 | | 554 / 144 |

My script reproduces A's table on c13 line by line (676 / 226). Per line in the c14 render: Violins I bars 11-26
25 / 10 -> 15 / 1 (range -77..+60 ms), Violins II 34 / 8 -> 20 / 1, Violas 50 / 19 -> 46 / 19, Horn 1 29 / 9 -> 23 / 9
(median +16 -> +4 ms); recapitulation Violas 33 / 18 -> 25 / 4, Horn 1 40 / 21 -> 27 / 9; Violins I and II F2 (bars
67-82) maximum +260 / +270 -> +73 / +91 ms. A's targets (under 300 and 70 for all lines; at most 10 of 59 outside 25 ms
on the theme) are not met. The two renders of the first build differ on 384 / 102 against 391 / 107 (row-change joins),
so about 10 notes per count are render noise.
Strokes in the pre-check (S, c13 -> two renders): Violins II 50 +117 -> +14, 66 +144 -> 0, 82 +117 -> +19, 97.5 +117 ->
+26; Violins I 66 +86 -> -10, 134 +99 -> +2; Violoncellos 114 +124 -> -25, 130 +87 -> +19; Double basses 114 +85 -> -38.
Neighbour rule: four rows reverted (Violins I 51 S +63 -> -95; Violoncellos 115 +90 -> -150; Violins II 600 +43 ->
-83; Violas 656 +75 -> +108); 13 changed notes were not stable between the two renders and were left.
Muted Trumpet 1 (`joins6b.log`): two pitches together at 684 / 686 / 716 / 718 85 / 84 / 86 / 87 -> 36 / 42 / 38 / 44
ms; over 60 ms at 3 of 18 joins (c13 8), median 46 ms (50).

## After the render (`render.log`, `metrics/`, `logs/render/`)

Render: 35 stems and the master, no clipping (sample peak 0.844, true peak -1.4 dBFS), attack probe 0 flags, every
track present. Master -20.6 LUFS, LRA 22.9 LU. Delivered mp3 (after the ride refit, `render_cycle.py 14
--measure-only`): -19.8 LUFS, LRA 14.9 LU, true peak -1.5 dBTP, limiter about 2.1 dB, span 19.4 dB, ride +11.5 / -2.0
dB. REAPER 44 GB before the render (0 compressed), 45 GB after.

Stops (`stops.log`; drop at +0.3 s / time to -20 dB):

| | bar 2 | bar 6 | bar 94 | bar 113 | bar 166 | bar 204 | final chord, RT60 (-5..-35) |
|---|---|---|---|---|---|---|---|
| master c14 | 17.7 dB / 0.35 s | 17.9 / 0.35 | 16.6 / 0.33 | 19.5 / 0.31 | 14.9 / 0.38 | 14.4 / 0.45 | 14.9 / 0.47; 1.27 s |
| master c13 | 16.8 / 0.36 | 17.5 / 0.35 | 17.3 / 0.32 | 20.4 / 0.28 | 21.7 / 0.30 | 14.5 / 0.45 | 14.4 / 0.46; 1.30 s |
| mp3 c14 | 16.5 / 0.38 | 16.6 / 0.38 | 16.7 / 0.36 | 18.8 / 0.31 | 14.4 / 0.39 | 14.1 / 0.45 | 15.6 / 0.41; 1.32 s |
| mp3 c13 | 15.7 / 0.39 | 16.1 / 0.38 | 17.4 / 0.33 | 19.7 / 0.29 | 19.5 / 0.31 | 14.2 / 0.45 | 15.2 / 0.43; 1.33 s |

Bar 94 is back under 17 dB. Bars 2 and 6 are at 17.7 / 17.9 dB on the master, over the 17 dB limit although the bar 6
fade is 1 dB smaller: the low strings' takes there changed with the resets. Not fixed (it needs a stem fix and a
`--mix-only` write); c15: the fades at 5.0 and 21.0 from -6 / -5 to about -4 dB. Bar 166 is back at 14.9 dB.

Items (`post14.log`; plain RMS, c13 -> c14):
- C #1, bar 222: partly. Master per quarter 882-886: -24.3 -21.9 -25.5 -22.1 -> -25.0 -22.8 -24.8 -21.5 (the dip at 884
  3.6 -> 2.0 dB; target under 1); Violins I 884.0-884.5 -40.9 -> -38.5 dBFS (target -36); Trumpet 1 / Horn 1 first 0.3 s
  -44.5 / -42.6 -> -40.6 / -38.6.
- C #2, bars 39-42: master bars 39-42 -27.9 -31.9 -33.8 -43.3 -> -28.1 -33.5 -38.3 -44.8 (steps 4.0 / 1.9 / 9.5 -> 5.4 /
  4.8 / 6.5 dB); Violins I 162-164 against 164-166: 10.9 -> 3.1 dB. mp3 bar 41 -> 42: 9.2 -> 5.1 dB (target 4-6). Bar 42
  itself is 1.5 dB lower on the master (limit 1; the old curve's fall ran into its first beat) and 1.9 dB higher in the
  mp3. Other diminuendos, master bars 168 / 169 / 170 / 182 / 240 / 241 / 242: -1.1 / -0.7 / -0.5 / -0.1 / 0.0 / -0.5 /
  -0.4 dB; only bar 168 moves by more than 1 dB.
- C #3, stringendo: Violins I 980-983 -45.8 -49.9 -45.1 -42.9 -> -38.3 -39.6 -36.2 -34.2 (Violins II -40.4 -42.1 -37.9
  -35.3); master per quarter 976-983 +0.2..+2.0 dB; the quarters still do not rise evenly (-26.7 -24.9 -26.8 -25.3 -24.0
  -26.3, then -24.1 at 984).
- C #5: cello G2 notes -3.0 to -4.0 dB; 31.5-125 Hz share of bars 147-150 -0.2 / +1.1 / +1.7 / +0.5 dB lower (bar 149
  1.7 dB, limit 1.5), bars 199-204 within 0.3 dB.
- C #6: first 0.2 s under the level at 1.6-2.0 s by 17.3 dB (Clarinet 2 184), 13.7 (Clarinet 1 200), 16.2 (Clarinet 2
  680), 23.5 (Bass clarinet 680); c13 0.7 / -3.0 / -0.4 / 7.0.
- B #2: not met. Head-to-second-note fall: Violins I bar 11 7.9 -> 8.0 dB, Violins II 6.4 -> 9.3, Violas 4.6 -> 3.3,
  master 5.1 -> 5.0; Violins II bar 19 10.4 -> 7.3, bar 151 7.8 -> 6.8. The second note at 42 is one of the two-valued
  row-change joins (Violins II 42 -4.5 dB between the two range renders, Violins I 42 -3.5), so a level trim cannot
  hold it; it belongs to the one-row theme test of c15.
- B #3: Flute 2 against Flute 1 in bars 154 / 158 / 252 / 272: +2.8 / +1.8 / +3.4 / +4.1 -> +0.4 / -1.8 / -0.1 / -0.3
  dB; Flute 1 against Violins I at 952-964 +2.3 / -0.3 / +0.9 -> -0.6 / -3.2 / -1.5 dB.
- B #5: harp at 524, first 100 ms -27.2 -> -31.2 dBFS (timpani -31.6); Clarinet 1 under Bassoon 1 in bars 121 / 122 by
  3.3 / 5.1 -> 3.9 / 6.3 dB.
- A #3: Trumpet 1's notes of 984-1000 -45.1..-32.8 -> -38.1..-31.4 dBFS, Trumpet 2 -44.6..-29.0 -> -37.2..-28.8
  (Horn 1 -35.4..-28.6).
- B #1: pizzicato peaks on the full render: Violoncellos range 16.6 -> 3.1 dB (SD 4.7 -> 0.6), Double basses 12.5 ->
  2.7 dB (SD 2.6 -> 0.6). Basses arco 264-300: 276 / 278 -44.4 / -45.3 -> -47.3 / -47.9, 294 / 296 -42.8 / -44.0 ->
  -45.8 / -46.7, 299 -52.0 -> -51.0 dBFS (range 12.6 -> 9.6 dB; 268 / 270 at -54.4 / -55.4 are still the weak ones).
- Delivery (item 5): gain (mp3 minus master) bars 42-50 +10.0 to +10.4 dB (c13 +6.6 to +11.7), bars 170-176 +10.6 to
  +10.9 (c13 +7.7 to +13.4); mp3 bars 42-50 -34.8 -34.4 -32.7 -32.8 -31.4 -34.1 -30.8 -35.0 -36.7: bars 49-50 are
  under bars 42-43. The gain steps up 1.9 dB into bar 51 with Trumpet 1's entry (the 200-264 row).
- Bar 90 (new): S at 358.0 Flute 1 +17, Oboe 1 +14, Clarinet 1 +11 ms (all within 25 ms of the beat and 6 ms of each
  other); the runs before it Flute 1 +8..+17, Oboe 1 -10..-5, Clarinet 1 +12..+21 ms.
- Bar 75: perceived onset Violins I G -101 -> -34 ms (note-on -213 -> -143 ms), A flat +13, F -8; Violins II G +11,
  A flat +50, F -64 -> +83 ms (its -0.055 s row overshot; crossover +88 ms). Each eighth sounds as its own pitch for
  100-132 % of its length (`bar75_own.log`).
- Bar 150: master 50 ms levels from 599.0: -23.6 -27.3 -29.3 -32.0 -33.7 -35.7 -37.1 -35.6, entry -29.4 -26.9 -23.2
  (c13 -23.3 ... -38.8 -38.1, -29.9 -25.2 -21.7): unchanged, no glitch.
- Master per bar against c13: median -0.05 dB, 5th / 95th percentile -0.72 / +0.60; off by 1.5 dB or more: bars 26, 40,
  41, 42, 171.
- Tempo (coordinator's checklist): no re-bow point lies within 4 qn of a changed arc or caesura, so no fill was refitted.
  Printed breath gaps on both maps (37 breath marks): the only changes of 5 ms or more are 251 (median 410 -> 416 ms)
  and 472 (Bassoon 1, before its row was removed). Stops are measured at the same six bars; each render on its own map.
- Not checked after the lead changes on Horn 1 and Trumpet 1 (coordinator's item 4): the level hole at their joins.

Disk: the c13 stems and the range WAVs are deleted (6.1 GB freed); `cycles/c13/render/00_Master.wav` and the c13 mp3
are kept. `cycles/c14/rendered_build/` holds the rendered tables.

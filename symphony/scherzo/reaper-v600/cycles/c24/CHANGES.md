# Cycle 24: changes (actor, on the c23 render)

STATUS: **rendered once**, 2026-11-18 02:05-02:12 CST, from a freshly restarted REAPER (guard 0, memory settled at 44 GB,
0 GB compressed). Attack probe: late or hole 0. No stem fix.
- mp3: `cycles/c24/scherzo-mockup-c24.mp3`. Data as rendered: `cycles/c24/build_render/`. Records: `cycles/c24/records/`.
- Lock (`phase.log`): queued 20:14 behind mvt1 c62 and mvt3 c26; held 22:27-23:01 (range tests, final build) and,
  after waiting for disk, 01:36-02:14 (open, envelopes, restart, render, save). 72 min in all.
  - Disk was 19-22 GB free during the first hold (under the 30 GB rule), so I did the final build, saved, quit and
    unlocked without rendering, and re-queued; disk reached 44-48 GB at 00:03.
- REAPER memory: 44 GB settled before the render, 44 GB after it (0 GB compressed); 55 GB after the range-test batch.
- The save after the render left Horn 2 / Horn 4 stale again (Opus rewrites their 1FHs attacks). Both were rebuilt, the
  project saved again, and the guard reads 0 stale.
- Disk: c23's stems deleted (00_Master.wav and mp3 kept), my range WAVs deleted; 44 GB free at the end.
- Master -21.2 LUFS, LRA 22.3, TP -0.4 dBFS, sample peak 0.953 (no clipping). All 36 files present and sounding.

## Bar 23 figure (first check; `records/fig24.txt`)

Decay before the next note-on / decay at the trough before the next note's first 10 ms peak (critic A #3's measure) /
trough between eighths, dB, c23 -> c24:

| occurrence | c23 | c24 |
|---|---|---|
| **bar 23** (qn 67) | 3.4 / 4.5 / 3.4 | **4.4 / 7.7 / 5.5** |
| bar 23 per note (F# -> G, G -> A, A -> B), at the trough | 2.4, 10.2, 6.5 | 6.4, 9.3, 11.9 (range test) |
| bar 38 / 42 / 70 | 11.0 / 6.9 / 7.7 at the trough | 10.9 / 7.1 / 7.7 |
| bars 106 / 118 / 263 / 306 / 318 | unchanged (+-0.1) | |
| bar 110 / 310 | 10.5 / 10.7 | 14.9 / 14.4 |
| bar 116 / 316 | 7.6 / 7.6 (trough 5.2 / 5.1) | 11.0 / 10.7 (trough **2.7 / 2.9**) |
| **bar 115 / 315** | 5.8 / 5.4 | **3.3 / 3.3** (worse) |
| bar 274 / 298 / 334 | 12.8 / 9.1 / 11.4 | 13.0 / 8.5 / 12.8 |
| Violins II, 15 occurrences | | unchanged except bar 66 (15.2 -> 17.6) |

- Bar 23: better on every reading. The pair is -9.0 / -6.2 dB against its neighbours (range test; c23 -7.2 / -10.5).
- **Regression at bars 115 / 315** (tutti, qn 343 / 943) and the trough of 116 / 316: the slurred pair and the Stac
  RRx14 B5 after it are unchanged data. The F sharp 5 before each pair now plays "Spiccato RRx9" (its own decay
  13.0 -> 20.5 dB), which moves the round-robin position of the later Stac RRx14 notes (c22 learning), and the B5 at
  344 / 944 now enters on a weaker take (A -> B at the trough 5.6 -> 4.3, B -> C 5.9 -> 1.5). It is not a level fault, so
  no stem fix. For c25: keep the F sharp 5 of the tutti statements (342 / 346 / 942 / 946) on Stac RRx14, or add a CC16
  reset on Violins I before 342 / 942.

## Changes made

### Tools (generic, off by default)
- `tools/build_reaper.py`:
  - mix.json **`note_slew`** (Dan's rule, critic B #1): inside sounding stretches (notes less than `rest_s` apart) the
    written envelope changes at most `rate_db_s`. A backward pass makes each move end at its written time and start
    earlier. A stretch after a rest takes its first value in that rest (10-30 ms before the note-on, or inside a shorter
    rest). `max_ramp_qn` caps how far back a move may start (Movement I c62's note); a move that needs more breaks the
    rate and stays in the guard's list. `skip_hairpins` (tested, not used: below). Scherzo: rate 4 dB/s, 2 qn,
    rest 5 ms, timpani and Rls / Roll rows left alone.
  - `sus_release_cap_ms` spec keys `orphan_only` / `deactivate` (critic A #2): act only on a row's groups that have no
    start mode while its other groups rotate by RoundRobin; switch them off instead of capping.
- `tools/score_to_parts.py`: `STAC_ROW_BY_PITCH` {track: [(lo, hi, row)]} (critic A #1); `ARRIVAL_WEIGHT_MOVED` (qn:
  the arrival step ends 5 ms before the track's moved note-on, held to the arrival note's end, released over that many
  qn); PHRASE_SHAPE types key `build_start`.
- `tools/deliver_master.py`: the room bed is now Movement I c62's function (coordinator's note). Differences found in
  c23's version: one generator with seed 20261118 (theirs: seeds 6201 / 6202 / 6203), low cut (f/84)^4 / sqrt(1 +
  (f/84)^8) (theirs (f/84)^4 / (1 + (f/84)^4)), RMS normalisation with 50 ms ramps (theirs: peak), and the bed added
  after the trim and fade (theirs: before, so the fade-out takes the bed too). Level -60 LUFS in both.
  On the c23 master the new bed changes nothing measured (I -14.0, LRA 10.5, TP -1.4).

### `build/score_config.py` (c24 block; switches C24_PS, C24_SPIC, C24_FL, C24_F23, C24_CEL; `C23_FHP` now off)
1. Celli [362, 396, -4] and violas [192, 198, 3.5] as CC11 spans: celli (361.45, 396, -9) (CC11 41 -> 32, at the edge of
   the 18-32 region that hardly responds), violas (191.4, 196.7, +8). `ARRIVAL_WEIGHT_MOVED` 0.5.
2. PHRASE_SHAPE start -12 -> -4, rise [(0.4, 3), (0.8, 8)] -> [(0.4, 2), (0.8, 4)], peak 10 -> 6, end -12 -> -8, wind scale
   1.4 -> 1.0, builds enter at -6 (critic C #1). Violas 576 on "Sus MAX" plus CC11 +8 over 575.4-588 (critic B #4).
3. (roles.json) theme A: celli [36, 84, -2] removed, basses [36, 90, -3] (critic C #3).
4. Violins I D5 / D sharp 5 / F sharp 5 staccatos on "Spiccato RRx9" (critic A #1).
5. Flute 1 into 105 / 305 (critic B #3): `C23_FHP` off, `drop_always` [310, 910], velocities 70 -> 100 over the hemiola.
6. Bar 23: CC11 (66.72, 67.12, +20) (critic A #3).
7. Smaller: celli legato targets 6 or more semitones away at velocity 112 (11 notes; A #4a); CC16 round-robin reset on the
   celli at 167 (C #5); ride row [645-659] -1.5 removed (C #6); harp velocity cap 45 over 1040-1068 (B #5); CC11 -8
   counter-shape on the celli's hot joins at 516 / 526 (C #2a).

### `build/roles.json`, `build/mix.json` (`actor_scripts/apply24.py`, rerunnable from `before/`)
- Role edges moved to the moved note-on or to a rest: celli [310.6, 360, 4.5] / [910.6, 960, 4.5] (were 312 / 912),
  celli [612, 623.3, 3.2] / [623.6, 648, -1.5], violas [312.5, 359.45, 4] / [359.45, 420, -1.8], harp [672, 1019, -3].
  The fourth value of a roles.json row is an end-ramp length, not an end level, so B's four-value rows could not be
  written as given; the remaining ramps are drawn by note_slew.
- mix.json `note_slew`; Violins I `sus_release_cap_ms` + orphan spec (deactivate).
- Opus state changes: Violins I only (orphan groups). The final build wrote all 31 tracks (`--midi-only`, stale and
  legato tracks rebuilt), then `--mix-only` for the final envelopes in the second hold.

## Item 1: Dan's rule, the fixed guard (`actor_scripts/guard24.py`; lists in `records/guard_before.txt`, `guard_after.txt`)

The guard reads the envelope REAPER gets (`vol_points`), every note from 60 ms after its moved note-on to its end
(legato overlaps included), with no exempt windows. Timpani left out, harp counted apart.

| measure | c23 data | c24 as rendered |
|---|---|---|
| step: 1.5 dB within 0.5 s at over 6 dB/s | 175 (+27 harp) | **25 (+14 harp)** |
| first 0.35 s of a note: 1.5 dB or more (finale c27) | 205 (+5 harp) | **64 (+6 harp)** |
| critic B's: 2 dB within 0.5 s at 20 dB/s or faster | 59 (+19 harp) | **0** |
| steps wholly inside printed hairpins (exempt from the two first rows) | | 48 |

- c23's causes (layer attribution from an `STP_LAYERS` build): dynamic-trim steps at printed marks on the score onset of
  led notes (most, no layer named), the trims following the sfp's spike shape at 900 (all winds and strings, 5-9 dB),
  hairpin-gain releases, role edges (celli 312 / 912 / 362 / 576 / 624, violas 197 / 360, Horn 1 651 / 659 / 1068,
  Oboe 1 146 / 675), uni_role edges (Horn 3, Bassoon 1 654), arrival weight (1005), level rows (Clarinet 1 471 / 472).
- **Target (0) not met, by choice.** With no ramp cap the slew reached 0 / 0 / 0, but 56 track-bars changed their mean
  sounding level by more than 1.5 dB and moves reached 7 qn. Cap 4 qn: 7 / 28 notes left, 35 track-bars. Cap 3 qn:
  16 / 41, 26 track-bars. **Cap 2 qn (adopted, Movement I c62's rule): 25 / 64 notes left, 16 track-bars over 1.5 dB**
  (`records/slew_moves.txt`). The longest move is 4.9 qn (a chain of moves); 104 moves span more than 1 qn.
- Every note still listed holds a move that the 2 qn cap made steeper than 4 dB/s. By track: harp 17 (ringing chords
  under role and trim steps), Clarinet 2 10, Flute 1 8, Clarinet 1 7, Bassoon 2 4, Contrabassoon 3, others 1-2. These
  need the step moved to a rest or carried by CC7 (finale technique 135/136), not tried this cycle.
- Track-bars changed over 1.5 dB by the slew: trombones / tuba bar 331 -3.2..-5.9 (their p < f crescendo of 0.6 s, trim
  falling 15 dB against it, now enters lower), **celli bar 276 +4.7 and bar 348 +5.4** (the pp trim's rise at the sub. p
  828 and at the 1044 entry is anticipated over the joined notes before them: the forte before the sub. p of bar 277 is
  louder on the celli; to fix in c25 with the step in CC7 or a rest), celli 192 -2.2, violas 276 +2.1, Horn 1 356 +2.5,
  Bassoon 2 200 +2.3, others 1.5-2.0.
- Printed hairpins are rate-limited too, against the finale's advice: with `skip_hairpins` the guard kept 35 / 107
  failing notes, most at hairpin starts on led notes (role and trim steps that coincide with the hairpin). Of 237
  hairpins with a fast written move, 148 move with the hairpin and 89 against it (trim counter-moves); the backward
  pass keeps the written level at each hairpin's end except at 23 hairpins (`actor_scripts/hpdir24.py`).
- 17 of 31 trim tables are U-shaped (falling from pp to f, rising again to ff), so a held note's trim moves against a
  crescendo up to f (finale c27 note). Not changed.
- Envelope table: c23 4,686 points, 0.84 per note, 16.9 per second; c24 4,522, 0.81, 16.3 (timpani left out).

## Measured (c23 -> c24 full renders)

- **Lyrical entries** (`lyr24.py`, entry note's first 0.3 s against the median of the next three; 91 lyric / build
  phrases in the lyrical spans): 7 dB or more under 6 -> **3**, 6 dB or more under 8 -> 3, median -0.5 -> -0.2. Left:
  Horn 1 651 -9.0, basses 579 -8.4, Clarinet 1 576 -8.3 (a crescendo is printed from the last two). My measure counts
  fewer phrases than critic C's (108).
- **Violas' p cresc line 576-588**: first note -57.8 -> -55.6 dB, then -46.9 / -38.5 / -38.6 -> -44.7 / -36.8 / -34.5;
  celli unchanged (-47.9). The first note is still 8 dB under the celli (open).
- **Theme A** basses minus celli on the shared onsets 36-90: +7.4 -> **+2.4 dB** (target -1..+2).
- **Violins I staccato separation by pitch** (whole movement, median dB; 60 ms peak median):

  | pitch | pairs | c23 | c24 |
  |---|---|---|---|
  | D5 (74) | 5 | 0.7 (-44.7) | **4.7** (-38.2) |
  | D sharp 5 (75) | 12 | 2.2 (-39.2) | **7.6** (-35.8) |
  | F sharp 5 (78) | 3 | 0.0 (-43.7) | **6.0** (-37.7) |
  | B4 (71) | 20 | 5.3 | 5.2 |
  | E5 (76) / B5 (83) | 3 / 8 | 5.2 / 4.3 | 4.5 / 3.2 |
  | all | 54 | 4.2 (-42.7) | **5.2** (-38.4) |

  By passage: 48-132 4.0 -> 7.1, 311-360 5.0 -> 6.0, 756-828 4.4 -> 6.3, 912-960 4.7 -> 6.1. Tails of isolated quarters at
  +0.5 s after the peak: -38..-50 -> -37..-104 dB (81 -93, 801 -59, 827 -61, 957 -104; 165 / 393 / 861 unchanged at
  -37..-41: those are followed by other notes' ring).
- **Flute 1 into 105 / 305**: first ff E6 over the E6 two notes later +8.2 -> **+5.1** (312), +4.8 -> **+1.8** (912).
  Target (2 dB) met at 912 only. The hemiola notes are 0-5 dB lower than c23 (no held gain, velocity 70-100), so the
  crescendo is heard as rising only over 306-310. Open.
- **Celli trio tune 504-552** (bodies): std 2.5 -> 2.3, steps over 4 dB 7 -> 3; 516 -34.1 -> about -39 (range test).
  Violin I solo: std 3.5 -> 3.3.
- **Accents** (revised measure, against the detached note before): Flute 1 -0.4 -> -0.9, Oboe 1 -2.5 -> -2.5,
  Violins I -4.5 -> -3.4, violas -0.7 -> -0.4, celli -1.3 -> +1.0, the others within 0.2 dB. Over +3: Violins I 0 -> 2,
  Violins II 6 -> 7, violas 4 -> 5, celli 4 -> 5. Dan's target (median +1..+2) is still met only by the celli.
- **Timing** (measure S, `timing13.py`; c23's stems were deleted before its run, so c18 is the reference): over 25 ms
  27 % (c18 26 %), over 60 ms 5 % (c18 5 %).
- **Per-bar master against c23**: median -0.02 dB. Over +1.5: bar 58 +1.9 (celli round robins: the new reset puts them
  back near c22, which read +2.9 over c21), 62 +1.6, 290 +1.6, **336 +2.3** (the summit downbeat: arrival weight moved to
  the note-ons). Under -1.5: 170 / 172 / 173 -1.8..-2.2 (fugato celli, same reset), 192 -1.8 (violas / celli CC11 rows),
  210 -1.6 (trio).
- Hall: master G.P. drop at +0.3 s 17.9 dB, 20 dB fall 0.37 s, RT60 1.40 s; mp3 18.9 / 0.33 / 1.38; `hall14.py`: G.P.
  17.5 dB, t20 0.35, RT60 1.50, soft ends 0.07-0.19 s. Inside Dan's limit.

## Delivery, against the shared spec (c24 mp3)

| | c23 | c24 |
|---|---|---|
| 1. I / TP | -14.0 / -1.4 | **-14.0 LUFS / -1.3 dBTP** |
| 2. summit lead | +0.64 over 318 | **+0.55 over 335** (+0.7 over every tutti outside 333-339) |
| 3. f -> ff | 2.22 | **2.24 LU** |
| 4. p10 short-term | -20.2 | **-20.1** |
| 5. limiter summit / 105-120 / 305-320 / 72 / 300 / final | 2.8 / 2.2 / 2.1 / 1.0 / 0.8 / 0.1 | **3.8** / 2.3 / 2.2 / 0.5 / 0.9 / 0.1 |
| 6. LRA | 10.5 | **10.5** |

- Climax order on the mp3: 336 -7.4, 338 -7.5, 337 -7.6, 339 -7.8, then 335 -8.0, 318 -8.1, 110 -8.3; no bar outside the
  summit within 0.5 LU. Trio ff 209-224 -10.6 -> -9.8 (ride row removed).
- Crescendo arrivals: 41 +0.6, 72 +0.6, 105 -0.4, 129 +0.0, 197 +0.8, 209 +1.2, 285 +0.5, 300 +1.5, 304 +0.2, 305 -0.4,
  329 +2.3, 336 +0.6.
- The summit takes 1 dB more limiting (pre-limiter crest +2.3 dBFS at 240.9 s) because the arrival weight now lands at
  the note-ons; still under the 6 dB limit.

## Range tests (`records/ranges.txt`; Violins I 48-132, 311-360, 767-800; celli 415-552; same-start control P0)
- P1 (orphan groups off) / P2 (all c24 Violins I and celli changes) / P3 (orphan release cap 100 ms): rendered within a
  minute of a rebuild after one 5 s discard, each lost 1-10 notes at -130 dB (`silent24.py`), on rows the change did not
  touch too. Void. P2b (a second render of P2) and P4 (rebuild, memory settled 129 s, two discards) lost none and read
  the same to the decimal. Adopted on P4: separation 3.0 -> 6.7 (48-132), 5.0 -> 6.0 (311-360), 4.9 -> 6.9 (767-800);
  60 ms peaks equal or higher (B4 -0.4 dB); bar 23 better (above). The orphan-cap variant was not re-run clean.
- Celli 415-552 (P2b against P0): std 2.5 -> 2.3, steps over 4 dB 7 -> 3, 516 -34.2 -> -39.2, sag -2.9 -> -5.7.

## Rejected, deferred, not done
- A #5 (hemiola accent bumps removed by a crescendo cap): the mechanism is different. Violins I's hemiola strokes play
  "Sus Marc LITE", which ACCENT_CC skips as a row with its own accent; Violins II's bump is the configured 2 units under
  loud_cc 98. No cap removes them. Not changed.
- A #4b (leg_leads refit from pcx), C #2b ("Leg BC MAX" on celli 512 / 524: the row is not loaded), C #4 (timpani hard
  sticks): not done (lock time).
- Finale techniques sent during the cycle (135 dynamic trims as CC7, 136 role edges into rests with CC7 holding the
  difference, 139 soft legato heads, 140 Violins II accents): not tried; 135 / 136 are the route for the notes the guard
  still lists.
- The coordinator's B replacements written as four-value roles rows: not possible as written (fourth value is an
  end-ramp length); replaced by edges at the moved note-on plus the slew.

## Faults still audible (Dan's rule: no envelope fix)
- The celli's sub. p at bar 277 / pp entry at 349: the forte bar before is 4.7 / 5.4 dB louder (slew anticipation).
- Bars 115 / 315 figure decay 5.8 / 5.4 -> 3.3 dB (round-robin positions).
- Flute 1 312 still 5 dB over 314; violas' first p note at 576 8 dB under the celli.
- 25 + 64 notes with a capped-ramp move inside them (harp, clarinets, Flute 1 the most).

## Research items

| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; fixed guard (above) |
| accents by the KS Masters' accent rows | adopted: flutes, Oboe 1; rejected: cor anglais, Clarinet 2, Violins II / violas Marc rows |
| shared -14 delivery + room-noise bed | adopted; bed now identical to Movement I's |
| one legato row per string line, keyswitch 0.15 s ahead | adopted (unchanged) |
| per-region / per-row volume in the Opus state | adopted (+ orphan groups switched off on Violins I) |
| CC16 resets | adopted on the celli fugato (167); separate legato tracks, timpani hard sticks, recorded crescendo rolls pending |

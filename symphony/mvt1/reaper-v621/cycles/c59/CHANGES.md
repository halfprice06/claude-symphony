# Cycle 59: changes (actor)

Render: `cycles/c59/render/` (main pass, then pass 2; no stem fix). Delivered: `cycles/c59/mvt1-mockup-c59.mp3`.
Nobody listened. Every figure is measured on dry stems or the master unless marked.

## Rule
Dan: no per-note level or shape on the track volume envelope, on any track, and no level rows fitted to earlier
renders. Result, read from a rule dump of the shipped build (`actor_scripts/tags59.py`): envelope items from a per-note
rule 0 on every track; fitted level rows 0. Everything below is in the instrument (CC11 / CC1 per phrase, region and row
volumes, velocity, rows, note lengths and gaps) or is a slow role. No accent or lift is a shape inside a note: a CC11
offset is flat from a note-on to a note end, or it changes the end values of a printed hairpin.

## What changed, in the coordinator's order (files: `build/score_config.py` c59 block, `build/mix.json`, `build/roles.json`)

1. **Cello solo bars 171-174.** `mix.json` Cello solo `region_gain_db`: Leg Port MAX -8 (every region of the row), C5
   +5, B4 +3. One CC11 lane for the phrase (`CC11_LANE` through the alias's `set`; `build/solo_lane59.json`, lane "D").
   Range renders 678.5-697, twice each, second kept (`rangetest/sBB`, `sCB`, `sDB`): lane B (62 / 78 / 76 / 82 / 88 /
   64 / 50) had the crest C5 at -34.1 with D4 at -33.2 over it; lane C (56 -> 70 -> 76 -> 96 -> 70 -> 58) had the
   crest loudest (-33.0, next -35.1) but the short E-flat 4 at 689.5 at -45.0, 8 dB under its neighbours, because of
   the E-flat 4 legato -4 entry. Shipped lane D: lane C starting at 48, that entry removed. Per note, c58 -> c59 (dB):
   E-flat 4 -31.6 -> -33.7, D4 -32.6 -> -34.6, C4 -35.2 -> -35.2, A-flat 4 (Port) -27.3 -> -35.1, G4 -37.5 -> -37.8,
   F4 -36.1 -> -36.3, E-flat 4 (short) -41.3 -> -41.4, C-sharp 4 -38.1 -> -37.0, F4 (short) -42.9 -> -39.5, A-flat 4
   (short) -39.3 -> -36.9, C5 -40.4 -> -33.0, B4 -43.4 -> -39.6. The crest is the loudest note; range of the first
   eleven notes 15.6 -> 8.4 dB. Left: the two short slurred notes at 689.5 and 691 stay 4-6 dB under their neighbours.
2. **Horn 4 soft layer.** The horn patch crossfades its dynamic layers on CC1, so critic B's CC11 map alone would not
   have changed the layer: `CC11_REMAP["Horn 4"]` (pp 50, p 56, mp 62, with (8, 8) at the bottom so a morendo still
   dies away) and the same map before `CC1_DYN_MAP` (`CC1_BASE_REMAP`, new). `mix.json` Horn 4 soft trims p 14.4 ->
   5.0, pp 8.0, ppp 10.0, mp 5.0; the inert pp entry removed; F3 Sus MAX -2 on all layers and a further -6 on the pp
   and mf layers (added after the first range render, where F3 stood 7.2 dB over G3). Range renders bars 19-22 and
   104-112 (`h12B`, `h22B`): F3 -39.4 -> -52.3, G3 -51.6 -> -54.0 at p: F3 over G3 12.2 -> 1.7 dB. Bar 111: Horn 4 F3
   -39.6 -> -50.6, Horn 1 A-flat 4 -59.6 -> -52.8: Horn 4 over Horn 1 20.0 -> 2.2 dB (target: not over; not met by
   2.2). Horn 1: A-flat 4 +7 and G4 +4 on the pp and mf layers, B-flat 4 Sus MAX +3. Bassoon 1 A-flat 3 gains halved.
3. **Solo and melody shapes in CC11.** New `CC11_ADD` (flat offsets from a note-on to a note end, or changed hairpin
   ends; on the brass and clarinets CC1 moves with them): Horn 1 412-416 +5 units (8 in the first range render gave
   B-flat 4 +6.5 and A4 +6.8 dB; with 5: D4 +0.1, B-flat 4 +6.1 including its +3 row gain, A4 +4.5), bar 111 crescendo
   from 52, 171 +5, 587.5-589 +7; Clarinet 1 176-183, 416.4-418.4, 504.4-507.9 +8; Cor anglais hairpin start 66 -> 74;
   Bass clarinet 432.5 +16; Horn 3 165-168 100 -> 60 becomes 84 -> 54; Trumpet 3 456-464 87 -> 100 becomes 80 -> 81.
   `LEVEL_TO_CC`: role rows on one or two notes that start after a rest or on a printed dynamic convert from 0.5 s on
   (62 dropped rows -> 28 dropped), on each track's own level curve (`build/cccurve59.json`, critic B's curves with
   thin segments replaced by the family's and slopes clamped to 0.06-0.70 dB per unit), at most +12 / -36 units, never
   upward past 116 (brass) / 120; the steps of a converted row now lie just before the moved note-ons
   (`moved_edges`). This gives the low brass under the melody in bars 124-126 (Trombone 1 88 -> 62 becomes 82 -> 54,
   Bass trombone 80 -> 54, Tuba 34 -> 25 becomes 27 -> 19, Bassoon 2 78 -> 63 at the start), Horn 1 497-501 +5 to +6
   units, Clarinet 1 576-582 at 12, Clarinet 1 / 2 137-144 46 -> 38, Bass clarinet 384-388 104 -> 82. `mix.json`: Bass
   clarinet A-flat 2 cut only on Sus Non Vib / Leg Slur, C2-E-flat 2 +4 / +4 / +6 / +4; Flute 1 A-flat 5 +5 on Sus MAX
   only, +2 on Leg Slur MAX.
4. **Oboe 1.** `soft_trim_db` mf 3.1 -> 7.0, p 5 -> 9.5, mp 8.5.
5. **Theme.** `roles.json` Violoncellos `[56, 88, -3.5]` -> `-2.0`. Violins I 82-94: the finished CC11 goes through
   (73 -> 80, 62 -> 71, 90 and up unchanged) (`CC11_FLOOR` with a map). The coordinator's end value 84 was
   range-rendered first: the line then fell 3.8 dB over 82-86 (c58 12.6, c56 5.7, c53 7.0); with 80 it falls 7.4 dB
   (C5 at 86: -46.7 -> -42.5; c56 -41.5).
6. **Accents.** `ACCENT_FLAT` per track from critic A's table, ceilings 120 / 122 / 118, `tutti_scale` off, no flat
   rise on an sf note. sf: `SF_TOP` (finished CC11 96 strings, 110 winds, 102 brass). `FP_SPIKE = ("f", 0.5, 0.9)`.
7. **Re-bows, config only.** Violas: the automatic points 30.03, 34.69, 38.65 unlisted (`REBOW_NONE` (28, 42) also
   removed the printed bow changes at 32, 36, 40 in the first build, so it is not used there); celli one change at
   295.0 in the note 286-304; basses `REBOW_NONE` (722.7, 729); Violins I `REBOW_NONE` (707.5, 715.5): the tied
   E-flat 5 is one bow on Leg Slur MAX; `SUS_ENTRY_AT["Violins I"] = [720.0]`.
8. **String shorts.** Violins I Staccatissimo RRx9 -3.5, Violas Stac RRx9 -2.5 (region volumes over the row); celli
   338.5-347 velocity 77 -> 68 (8 notes).
9. **Held same-pitch repeats on strings.** `REP_MIN_GAP` `held_s` 1.0, `held_gap` string 0.03 s (no accent, staccato
   or sf on the second note).
10. **Join holes.** `WIND_DETACH` `soft` (gap 0.015 s where the printed level is under CC11 60, woodwinds); Flute 1
    634.0 velocity 100; Violins II Marc doubling ends at 572; Violas tremolo diminuendo 160-168 not under CC11 45.
11. **Basses' pedal.** `roles.json` Double basses `[508, 516, -2, 2]` -> `[500.5, 516, -3, 2]`; it covers one tied
    note, so it is played as a CC11 offset (30 -> 42 becomes 27 -> 35, 42 -> 62 becomes 36 -> 52).
12. **Envelope points.** `tools/build_reaper.py` `ENV_THIN["tol_db"]` 0.5 -> 0.75.

## Measured results (c58 render -> c59 render)

### Envelope (`envelope_table.md`)
Per-note envelope items per track: 0. Fitted rows: 0. Points 4515 -> 3951. Points per second: Violins I 0.50 -> 0.42,
Violins II 0.61 -> 0.52, Violas 0.64 -> 0.55, celli 0.73 -> 0.61, basses 0.49 -> 0.41 (aim 0.4: met by no string
track); winds and brass 0.15-0.47; timpani 1.28. Notes with 3 dB or more of envelope inside 365 -> 348.

### Guards
Violins I 56-87.9: S robust SD 9 ms (guard 12), 2 over 40 ms; long notes front minus tail -1.8 dB (guard 3). 56-127:
12 ms, 6 over 40. 536-576: 18 ms, 6 over 40. Theme over celli bars 15-22 per quarter: median +7.0, lower quartile
+4.3 (c58 +9.3 / +5.9; target 3.9 or more). Range renders before the full render gave 10 ms and -1.8 dB.

### Faults (`faults_table.md`, `faults_c59.txt`; same script as c58)
| | c58 | c59 |
|---|---|---|
| join holes (6 dB for 80 ms) | 30 | 25 |
| same-pitch repeats under 3 dB | 50 of 252 | 49 of 260 |
| re-bow holes | 17 of 62 | 14 of 52 |
| long notes sagging 6 dB | 62 | 61 |
| pulse on a held note | 13 | 13 |
| pitches 4 dB out of line | 7 | 6 |
Join holes gone: Flute 1 634, Violins II 574, Violas 44 and 76, celli 464 is still listed. Smaller: Oboe 1 168 14.2 ->
10.4 dB, Bassoon 2 268 15.2 -> 11.5. Unchanged: Violas 168 (17.8 dB: the CC11 floor on the tremolo did not close the
step into the legato p), Flute 1 47, Flute 2 560, Violins II 91 and 105.

### Isolated accents (`accent_table.md`; critic A's script and definition, run on both renders)
All isolated accents (151): median +1.4 -> +1.7 dB, quartiles +0.7 / +2.5 -> +1.3 / +2.6, maximum +8.8 -> +9.6;
inside +1.5 to +2.0: 16 -> 30; under +1: 61 -> 20; over +3: 30 -> 32. Strings +3.7 -> +2.2 (quartiles +1.5 / +3.3),
winds +1.2 -> +1.7 (+1.3 / +2.3), brass +1.1 -> +1.7 (+1.2 / +3.1). Track medians: Violins I +3.8 -> +2.2, Violins II
+3.8 -> +2.6, trumpets +0.6 / +0.8 / +0.6 -> +1.2 / +1.6 / +1.5, Clarinet 1 +0.9 -> +1.5. Over the +3 limit: Bass
trombone +3.2 (n 6; +1.5 in c58). At +2.5 to +2.7: Tuba, Violins II, Horn 4, Bass clarinet (n 1). Under +1.5: Flute 2
+1.4, Trombone 2 +1.3, Trumpet 1 +1.2, Horns a2 +1.0. Single accents of +5 to +9.6 remain (Horn 1, Oboe 1, Flute 1,
celli, basses, Tuba): row and pitch sample level, not the CC11 rise. sf at 78.0 on Violins I: +3.4 -> +2.0 dB against
its neighbours. 2-5 kHz front excess -1.9 dB (5 of 139 over +3). Printed accents of 0.3 s or more at CC11 84 or more
whose lane does not rise at the note: 99 -> 94 by `accaudit59.py`; those left are the second and later notes of
accent runs (already at the accent value), accents on a subito drop, and notes already at the ceiling.

### Passages (stem body level per note, c59 minus c58, `notes59.py`)
- Cor anglais bar 7: G4 +2.4 dB (bar 7 stem -37.8 -> -37.1; the crest was not raised).
- Horn 1: bar 111 A-flat 4 +6.8 (stem bar -57.3 -> -49.2); 171 C5 +3.5; 498 C4 +1.7 (asked +3.5); 587.5 D4 +1.3
  (asked +3.5); bars 103-104 as in item 3.
- Clarinet 1: 176-183 +0.4 to +2.1; 416.5 +2.7; 504.5-507.5 +3.9 to +2.0; F4 576-582 -9.5 (asked -5: too far).
- Bass clarinet: 304.5 E-flat 2 +4.0, 308 A-flat 2 +4.5, 432.5 F2 +4.0.
- Oboe 1: bar 79 +3.5 on every note; bar 145 G4 +4.5, E5 +3.8.
- Flute 1 A-flat 5 at 292: -3.2 (master bar 74 -2.9).
- Low brass bars 124-126: Trombone 1 -3.3, Bass trombone -3.9, Tuba -4.5. Horn 3 165: -1.5 (asked -3.5). Trumpet 3
  456 / 460: -1.5 / -0.4 (asked -3).
- Basses' pedal 500.5-516: -2.0 / -4.7 / -1.6 by piece (bars 125-129 stem -43.1 -> -45.3; c57 -48.4).
- String shorts: celli 338.5-340 -36.7 -> -39.0 (c56 -41.6); Violas 350.5-352 -41.8 -> -44.1 (c56 -46.5); Violins I
  374-386 -34.5 -> -36.2.
- Violins I 708-715 on one bow: SD about its trend 1.3 dB, largest departure from the 1 s median 2.8 dB (the two c58
  pieces: 1.3 / 0.8 and 2.8 / 2.2): no pulse found; the 8 dB step inside the tied note is gone (bar 179 master -3.6).
- Violins I last note on Sus MAX: SD 3.7 -> 3.2 dB, autocorrelation at 3.95 s +0.77 -> +0.65, largest departure 11.5
  -> 8.1 dB. The loop pulse is smaller and still there (Violins II on the same row: 1.8 dB, -0.28).
- Horn 4 last chord (pp, G3): +1.1 to +4.1.

### Master bars more than 1.5 dB off c58 (`bars59.py`), with cause
Over: bar 174 +5.0 (Cello solo crest C5 +7.4 and B4 +3.8: intended; bar 174 was 2.8 under c57 in c58).
Under: bar 172 -5.4 and 171 -1.8 (Cello solo A-flat 4 on Leg Port MAX -7.9, first note -2.0: intended); 179 -3.6
(Violins I tied note on one bow); 74 -2.9 (Flute 1 A-flat 5); 87 -2.7 (celli shorts at velocity 68; 2.1 under c57 as
well, so this one went further than asked); 20 -1.8 (Horn 4 F3). Median of all bars -0.03 dB.
Against c57: 18 over, 16 under (bar 7 -7.2, 21 -4.6, 86 -4.0, 47 -3.8).

## Left audible (not patched with volume)
- 14 re-bow holes of 8-16 dB (list in `faults_table.md`); Violas 36 is now 13.3 dB.
- Loop pulse on the Violins I last note (SD 3.2 dB).
- Horn 4 F3 still 2.2 dB over Horn 1's A-flat 4 in bar 111; Horn 4's G3 at p 2.4 dB under c58.
- Cello solo: the short slurred notes at 689.5 and 691 are 4-6 dB under their neighbours.
- Clarinet 1 F4 576-582 9.5 dB down (5 asked); Horn 1 498 and 587.5, Horn 3 165, Trumpet 3 456-464 short of their
  rows by 1.5-2.5 dB.
- Cor anglais bar 7 crest (87 kept; the instrument is flat from 88 to 104).
- Violas 168 step of 17.8 dB from the tremolo into the legato p; Flute 1 47, Flute 2 560, Oboe 1 168, Bassoon 2 268
  join holes of 10-14 dB.
- Bass trombone accents +3.2 dB; single accents of +5 to +9.6 dB on six tracks; Trumpet 1 fff at bar 122 (its +2 row
  has no CC11 room and is not played).
- The notes after the sf at 78 (80.5-81.5) are 3.0-3.5 dB under c58: the level after an sf top is the top minus 8.
- Celli bars 85-87 2.7 dB under c58 at bar 87.
- 28 short role rows still dropped (tutti rows of +1 to +2 dB at 567.75-572.5 and -2.5 at 672-676 among them).

## Dropped from the work order
- 7, last part: alias track on Sus MAX for the seven printed bow changes (four more string instances in pass 2).
- 12, second part: the 57 + 38 movable hairpin gains into CC11 (the gain items are built after the CC11 lane is
  sampled; not a cheap change).
- 13: Cor anglais Main mic range test (two full rebuilds and four range passes; left out to shorten the lock).
- 10: the 0.10 s entry lead after a soft tongued join (the gap alone was done).
- MANUAL-GAPS: none tried. EW-TEMPLATE-PLAN, FINDINGS, mockup-kit LEARNINGS and HISTORY were not re-read in full
  this cycle (the coordinator's notes, the three reports and c58's CHANGES were).

## Not verified
The mp3 and the clips by ear; the basses' fp at 128.0 in its first 0.2 s (body +1.3 dB only measured); the dips at the
32 held same-pitch bow changes one by one (only the fault counts); every converted role row's level (11 checked
above); whether the CC1 shift that goes with a CC11 offset on brass and clarinets changes the tone audibly; the new
per-pitch gains across short and long notes beyond a check on the c58 stems (Horn 1 G4: short and long notes both
2-3 dB under F4 at higher CC11; A-flat 4 and the bass clarinet's C2-D2 have long notes only); the main render ran
with 0.05 GB compressed before and 27 GB after; pulse on the celli's two 4.3 s pieces at 286-304.

## Render conditions
- Lock: waiter from 17:55, held 20:05 to the end of `p8.sh` (`lock_wait.log`); nothing taken by hand.
- State guard: 0 stale at the start, after the build, after the range renders and before the main render; after the
  render saves Trumpet 1 (main) and Bassoon 1 stac, Flute 1 stac (pass 2) were stale and were rebuilt in full.
- Range renders: every variant twice, second kept, 45 s after each pass (`rangetest/`, `p2.log`, `p2r.log`,
  `p4a.log`, `p4d.log`). Full rebuilds: 7 tracks in the first build, Horn 1 and Horn 4 once more, Cello solo twice,
  with restarts between the batches.
- Attack probe: late or hole 0 (main and pass 2). State check: 2 runs on unchanged MIDI, both intended row or region
  volumes (Bass clarinet 366-370 +4.0, Violins I 116.5-117.5 -3.5).
- Memory: REAPER 43 GB before the main render (0.05 GB compressed), 44 GB after; 19-20 GB in pass 2. Disk 26 GB free
  before the render (WAVs deleted in the four allowed folders).
- Delivery: -19.8 LUFS integrated, LRA 14.9 LU, true peak -1.7 dBTP, limiter about 0.7 dB, p10-to-max span 18.0 dB,
  433.60 s. Master: -19.9 LUFS, LRA 23.5 LU, true peak -0.7 dBFS, sample peak 0.926. No clipping.

## For Dan
`cycles/c59/ab/`: c58 then c59, one gain for both halves: bars 15-23 (master, Violins I stem) and bars 171-174
(master, Cello solo stem).

## Tools (all new keys off by default; with C59=0 parts.json is byte-identical to c58's, checked)
`score_to_parts.py`: `CC11_ADD`, `CC11_LANE`, `CC11_FLOOR` (value or map), `CC1_BASE_REMAP`, `SF_TOP`, `ACCENT_FLAT`
`skip_sf`, `LEVEL_TO_CC` `after_rest_min_s` / `rest_s` / `curves` / `max_units` / `max_units_down` / `ceil` /
`moved_edges`, `REP_MIN_GAP` `held_s` / `held_gap`, `WIND_DETACH` `soft`. `build_reaper.py`: `ENV_THIN` 0.75.
`cycles/c59/actor_scripts/`: `dump59.py`, `pdiff59.py`, `accaudit59.py`, `notes59.py`, `pulse59.py`, `camic59.py`
(not run), `accA/` (critic A's accent script on any render, `acc_iso.py`), the c58 scripts renumbered, `p1.sh`-`p8.sh`.

# Cycle 41 (series 2, end of the first block of ten loops): changes

Inputs: critics A (articulation), B (balance), C (holistic) on the c40 render, and the coordinator's notes (Violins I full
rebuild first; the c40 data left only in build/ to reach both projects; which findings to take; the shared lock; delete
critic A's scratch). Snapshot: `cycles/c41/before/`. Scripts: `cycles/c41/actor_scripts/` (`c41check.py OLD NEW
section ...`: vln1, joins, breath, solo, c696, c548, reps, bal, climax; `legtest.py`: legato joins of a main string stem
against test stems; `splice41.py`). Records: `c41check_final.txt`, `legtest_ab.txt`.

Run (lock held 02:10-03:13; free when I arrived):
1. Edits; parts.json regenerated and diffed (`cycles/c33/actor_scripts/pdiff.py`, `cycles/c40/actor_scripts/envdiff40.py`):
   only the intended notes, keyswitches, CC lanes and envelope spans moved; tempo map identical.
2. `reaper_ctl.py lock`, start, open; `build_reaper.py build/parts.json jobs --midi-only` (31 tracks MIDI-only, Horn 1 and
   Trumpet 2 fully rebuilt for their new LegRep row), then `build_reaper.py build/parts.json jobs "Violins I"` (full
   rebuild, coordinator #1). `reaper_ctl.py restart`; 33 tracks; Mac Studio Speakers, no input, 48000 / 512, running.
3. `render_cycle.py 41` (no --force-memory: 0 GB compressed). Probe 0.
4. Stem fix (6 stems) and the Trumpet 2 splice; the same data written to the main project (`--midi-only`, 6 tracks);
   `reaper_ctl.py quit`.
5. Second pass: start, `--pass2 open`, `build_reaper.py ... --midi-only --pass2` (5 tracks MIDI-only, the 4 test tracks
   new), `--pass2 restart`, `render_cycle.py 41 --pass2` (9 instances; test stems to `test_stems/`, 38 stems summed).
   Probe 0. Test tracks deleted from the pass-2 project (`del_tracks.lua`) and from parts.json; Bassoon 1 stac written
   (`--midi-only --pass2`, its inherited notch move); `--pass2 quit`; `unlock`.

## Coordinator #1: Violins I fully rebuilt

The c41 Violins I stem matches c40's spliced FP4 audio outside its sul window and outside the spans where its envelope
changed: per 1 s frame median +0.00 dB, p10 -0.07, p90 +0.02, 4% of frames more than 1 dB apart (Violins II 5%, the
round-robin spread). c40's unspliced render was +0.65 / +0.71 median, p90 +2.2. No splice needed. After the render the
saved project holds CC70 default 127 on all 604 groups of all four string KS Masters (`rppstate.py`), so later
`--midi-only` builds keep the right finger positions (each CC70 lane ends on 127).

Inside the sul window (bars 56-59, Violins I and II in unison) Violins I is now 0.3-1.3 dB lower re the master than in
c40, whose audio there came from the stale-state instance; the unison line's master level moved 0.2-0.6 dB K. No change.

## Coordinator #2: the c40 data that was only in build/

- DIV A contour and join rows (pass 2): the Cello solo stem per 2 qn over 680-696 equals c40's stem-fixed stem (0.0 dB in
  7 of 8 frames, +0.2 in one); joins unchanged (dips 0.2-3.4, bursts -1.5..+2.7 except 687 +4.7).
- Celli 696 counter-shape: the 696 front in 100 ms windows (re the body) is identical to c40's stem-fixed stem.
- Celli 548 lead 0.01: moved onset 547.853 (c40 547.622). Perceived attack of the chord's G-sharp3 (rise 19 dB) -0.014 s
  (c40 -0.127); the C3 has a 5 dB rise and no reliable estimate.

## Accepted

- **A #1** 12 JOIN_NOTCH rows (`build/score_config.py` c41). Measured on c41 (after the stem fix below), dip / burst, c40 ->
  c41: Bassoon 1 131 -1.1 / +8.1 -> 3.9 / +1.3 (master burst +5.0 -> +0.3); celli 575 -1.5 / +5.7 -> 0.1 / +1.3 (pc -0.2
  -> 0.0 s); celli 191 3.9 / +6.2 -> 3.8 / +3.5 (master +6.2 -> +3.9; the rest of the burst is the new note's rising
  body); Clarinet 1 507 +4.8 -> +2.3; Violas 436 +6.4 -> +1.3; Oboe 1 315.5 +4.6 -> +4.1 (its transition differed between
  renders with identical data); Bassoon 1 138 +6.2 -> +1.3; Violas 182 +4.6 -> +1.9 (pc -0.3 -> -0.1); Horns a2 164 +3.8
  -> +2.3; Violas 28 +7.8 -> +1.9; Violins II 259 +6.2 -> +1.9; Violas 613 -0.3 / +8.6 -> 0.0 / +3.5. As rendered, A's
  spans for Bassoon 1 131 and Violas 613 began 0.06-0.13 qn before this render's spike and cut the old note's tail (new
  dips 4.9 / 5.4 dB): moved onto the spikes by stem fix (130.87-131.18; 612.75-613.0 at -6.8); celli 191 -4 -> -5.5.
- **A #2** breaths (stem dip, played gap): Horns a2 636 1.4 -> 10.6 dB (212 ms); Oboe 2 636 3.0 -> 11.7 (122 ms); Flute 2
  636 6.8 -> 7.7 (112 ms); Horn 4 536 -0.3 -> 3.9 (Horn 3 3.9); Trombone 2 632 2.3 -> 2.4 with the CC11 fall alone, 6.9
  with a c38 gap dip by stem fix (`LEVEL_SHAPES_S` `_gd18`). Trombone 2 keeps its default 0.3 qn gap (A's 0.22 would have
  shortened it). Oboe 2's 0.22 qn gap was at first filled again by its entry lead, which the old gap had capped (lead =
  min(lead, gap - 0.02 qn)): `entry_leads.json` Oboe 2 636 0.065 -> -0.075 keeps the onset at 635.89 (c40 635.90).
- **A #3** Cello solo `LEVEL_SHAPES_S` at 685 (alias tables): the swing after the shift +0.2 -> +0.3 s 8.0 -> 3.7 dB;
  685 burst +2.1 -> +1.3; per 2 qn unchanged.
- **A #5** (optional) LegRep RRx4 on Horn 1 452 / 528 / 624 and Trumpet 2 456 (kept), 124 (reverted). The gap minimum did
  not change (dip vs the lower body Horn 1 1.8 / 3.2 / -1.3 as in c40), but the repeats re-attack 2-5 dB louder over
  their first 0.5 s with a brighter front (2-5 kHz front minus body Horn 1 452 -11.5 -> -6.6, 624 -15.5 -> -9.2): re-attack
  over the gap 452 4-5 -> 8-10 dB, Trumpet 2 456 3-5 -> 5-6. Body excess past 0.1 s trimmed by stem fix (452 -2 dB, 456
  -1.5 dB; now +1.4 / -0.6 dB re c40 at +0.1-0.2 s). Trumpet 2's accented ff 124 came out +4..+6 dB over c40 with a
  shallower dip (1.0 -> -0.4): row removed, its c40 audio spliced back over 123.77-127.6 (`splice41.py`, linear
  crossfades in the re-tongue gap and the rest; now within 0.1 dB of c40). Memory: the main project settled at 45 GB as
  in c40.
- **B #1** roles Cor anglais [586, 605, 4] -> [586, 598.5, 4]: the third answer (A re M) 603 / 604 -4.4 / -5.6 -> -7.2 /
  -8.4; cor anglais minus the loudest tune voice -2.1 / -3.3 dB (was the loudest voice).
- **B #2** bar 125 shapes: Horn 1 minus Violins I per half beat 498.0-499.5 +1.8 / +0.2 / -5.1 / -2.2 -> +1.8 / +2.9 /
  +2.4 / +0.8; minus Oboe 1 at 499 / 499.5 -1.2 / -2.5 -> +4.3 / +3.3.
- **B #3** one `_all` row into each fff (the c40 hold-back rows and the old ramps replaced): master K steps per beat into
  636 (632-636) +1.7 / +0.4 / +2.2 / +3.1 -> +1.8 / +0.5 / +3.3 / +2.5; into 484 +1.6 / 0.0 / +3.3 -> +1.3 / +0.8 / +3.4.
  Delivered S max 160 -11.3 over 122 -12.3 (+1.0 LU; c40 +0.9).
- **B #4** roles Cor anglais [682.75, 689, -2.5]: solo minus cor anglais per half beat 683-688.5 median +1.2 -> +3.8 dB A,
  under 3 dB 11 -> 3 of 12. RIDE_TRIMS refit check: the fit moves at most 0.09 dB (kept).
- **B #5** Cor anglais stac shapes: per note minus Violins II -7.5..+4.6 -> -6.3..+3.1 dB (363.5 -7.5 -> -3.5; 365 / 365.5
  +4.6 / +4.2 -> +0.6 / +0.2; 367.5 -0.9 -> +3.1).
- **B side note** `render_cycle.py` records memory at start, after the settle wait ("before render") and after the render.
- Tools (generic): `score_to_parts.py` `TEST_TRACKS` (parts.json "test"; the tempo lead line ignores them),
  `render_cycle.py --pass2` writes test stems to `cycles/cNN/test_stems/` outside the sum, `build_reaper.py` mix key
  `legato_speed` (LegatoSpeed script parameters). README updated.

## C #1: LegatoSpeed START_MAX / RELEASE A/B (second pass, not adopted)

Four fresh instances played the Violas' and Violoncellos' own notes, lanes and leads over the whole track (celli resting
over the coda solo as on the main track): A = START_MAX at BUMPRED (Violas 3890, Celli 3130), B = START_MAX 4800 with
RELEASE 300 ms (patch 2173 / 510, 2709 / 443). Away from the transitions they match the main stems (per 1 s frame median
0.00 dB; Violas p90 +0.6 includes 128-142, where the alias's CC11 / CC1 lanes differ by 3 CC and which is left out of
the join measures). Every monophonic legato join (124 viola, 263 celli), my method (`legtest.py`; the window is the
contiguous time around the crossover with the two pitches' harmonic bands within 6 dB, shared bins left out; it reads
shorter than C's: violins 86-101 ms median, p75 112-120):

| | window median / p75 (ms) | per-join window change | crossover median | pc robust SD / >60 ms off | joins with dips >= 5 dB |
|---|---|---|---|---|---|
| Violas main | 98 / 133 | | +23 ms | 117 / 62% | 9 |
| Violas A | 98 / 134 | +0 ms | +1 | 105 / 57% | 13 |
| Violas B | 94 / 134 | +0 ms | -19 | 117 / 60% | 18 |
| Celli main | 108 / 146 | | +8 | 96 / 53% | 24 |
| Celli A | 110 / 148 | +0 ms | 0 | 93 / 52% | 24 |
| Celli B | 108 / 148 | +0 ms | -14 | 81 / 44% | 33 |

START_MAX moves the whole transition earlier (a lead change, as the c38 actor predicted) and does not shorten the slide;
crossover and pc agree within 30 ms on 22-29% of joins in every variant. C's criteria (window at the violins' values, no
new 5 dB dips) fail for all four. Not adopted; recorded in MANUAL-GAPS (Results c41) and LEARNINGS. The test tracks are
gone from parts.json and the pass-2 project; their stems stay in `test_stems/`.

## Rejected or deferred

- **A #4** not made: its premise does not hold. Strings (and winds) have used the swell A proposed, (0.03, 0.15, 0.40),
  since c23 (`build/score_config.py`, c23 section); A read the default in score_to_parts.py. The accented-versus-plain
  front gap it measured is real but mixes rows (accented f notes are mostly fresh Sus MAX strokes, plain ones legato
  transitions); C #2 (a marcato row) is the route for attack colour.
- **B #6** (CC16 round-robin reset) deferred as planned: it changes every track's sample choice and the existing fits.
  This render shows the same symptom (identical data, Oboe 1's 315.5 transition and a release tail in bar 127 differ
  by up to 4 dB).
- **C #2** (Marc Sus LITE brass test), **C #4** (bar 62 CC7 test): not done this cycle (the C #1 test filled the second
  pass). **C #3** (per-mic width) deferred to the planned rebuild cycle covering both passes.

## Measured state (c41 final: main stems + stem fix + Trumpet 2 splice + second-pass stems; 38 stems)

- Master (float stem sum): -16.9 LUFS, LRA 23.6 LU, true peak +2.5 dBFS, sample peak 1.332.
- Delivered `cycles/c41/mvt1-mockup-c41.mp3`: -19.8 LUFS, LRA 14.9 LU, TP -1.7 dBTP, limiter about 0.5 dB (top
  pre-limiter peak 378.73 s, -1.02 dBFS), p10-to-max span 19.3 dB, ride trims -1.37..+3.67 dB over 680-696.
- Delivered S max: 160 -11.3 > 122 -12.3 (+1.0) > 167-170 -13.4 > 26 -14.6; 140 -15.1, 117 -15.5, 158 -15.7, 131-134
  -15.8, 69-72 -16.3.
- Attack probe: 0 late or holes (main and second pass). Silent-note list: only its two known false alarms (Trombone 1
  552, Timpani 727). Every stem present; per-bar levels against c40 differ only where the data changed, plus round-robin
  spread.
- REAPER: main project 19 GB at start, settled at 45 GB (0 compressed) before the render, 46 GB with 16 GB compressed
  after. Second pass (5 tracks + 4 test instances): 11 GB at start, 19 GB settled and after (0 compressed).

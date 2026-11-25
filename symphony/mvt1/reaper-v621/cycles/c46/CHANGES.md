# Cycle 46 (series 2): changes

## For Dan: what to listen for in c46

In c45 the violas were too loud in bars 34-38, 44, 129, 135-136 and 145. In bar 34 they covered the bassoon solo, and in bar 145 they were as loud as the first violins under the oboe's dolce. The cause was a test track that did not play the violas' own dynamics and had replaced the real viola part. c46 fixes it: the bassoon is 3-8 dB above the violas again in bar 34, as it was in c44. Soft string endings now die away instead of stopping: listen to the final chord, the end of the slow introduction (bar 14) and bar 146. The timpani roll at bar 174 no longer covers the bassoons' low G, and the roll under the horn solo in bars 13-14 settles under the strings after its first notes. The three timpani crescendo rolls in bars 62, 115 and 140 now grow into what follows. The two loudest arrivals (bar 122 with the tam-tam, bar 160 with the cymbal) step up more clearly. The opening cello and bass swell in bars 1-4 grows as it did before the hall was made drier. At letter F (bars 98-102) the trombone and horn half notes on each downbeat sit under the tune; their answering eighths keep their level. The coda cello solo (bars 171-174) is better in time: the notes that came in late or early now land within about 40 ms of the beat, except two. Short first notes of slurred pairs in the violins and cellos are easier to hear (for example bars 17, 37, 65 and 105).

## Values for the other movements (Movement II, scherzo, finale)

All measured on Movement I in this cycle.

1. **Check a test track's data before using its stem (B #1, generic).** A pass-2 test alias that duplicates a main track must play exactly that track's notes, keyswitches, CC lanes and volume envelope. In c45 it did not: `score_to_parts.py` carried each "espr." boost to the end of the alias's window (a rule meant for solo aliases), which put CC1 40-55 and CC11 3-42 higher over 17-25% of each whole-piece alias. The Horn 1 and Violins II aliases also played notes that their sources rest in (Horns a2, the f62 windows).
   - Tools: `alias_dup()` (during the build of an alias whose source also plays its notes, the solo-window rules do not act); `tw_own(track, lo, hi)` (the windows where a track keeps its own notes, used as the test alias's windows); `tools/alias_check.py PARTS [MIX] [track ...] [--stems MAIN TEST]`. `score_to_parts.py` runs the check on every TEST_TRACKS alias, and `render_cycle.py --pass2` writes it to `test_stems/alias_check.txt`. Solo aliases are unchanged: with the tools fix alone, parts.json was byte-identical to before.
   - Before a test stem replaces a main stem, also compare the two stems per bar. Outside the tested effect they should agree within 1 dB. Here the Violins I / II and Violas test stems agreed. The celli and basses test stems differed by 1-2.5 dB in 8-10 bars, from the second instance's round robins, so they were spliced in only from the final chord.
2. **The c45 release-trail result (`rt_gain_db` -6), re-tested with matched data.** Its c45 numbers are withdrawn (c45 CHANGES item 4 and LEARNINGS are corrected).
   - **Violas pass.** The c46 main stem (trail -6) was compared with c45's main-pass stem (trail 0) on the same notes and lanes: the figures' old pitch at +70 ms -6.2 -> -8.4 dB, early tail (0.15-0.25 s) -12.1 -> -17.0 dB re body, late tail (0.4-0.6 s) -7.9 -> -8.1, legato joins dipping 5 dB or more 14 -> 12 of 129. One ending fell more than 10 dB in 50 ms (0 before).
   - **Violins II fail.** Early tail -11.4 -> -13.7, late tail 2.1 dB lower, détaché -10 dB point 0.254 -> 0.270 s, joins dipping 5 dB or more 26 -> 43 of 125.
   - **Horn 1 fail.** Early tail -11.8 -> -14.1, late tail 1.0 dB lower, 5 dB joins 1 -> 8 of 47. On these patches the trail also fills the legato transitions.
3. **String release caps by dynamic (C #1).** `build_reaper.py` `sus_release_cap_ms` takes a list of specs. Movement I now uses 150 ms at mf-ff and 350 ms at pp/p on Sus MAX and Sus Marc LITE. The patches ship 524-931 ms at pp/p; c44 used 150 ms at every dynamic. Pass-2 test, the same notes per section, 150-everywhere -> 350 at pp/p (median over soft phrase ends; 10 dB / 20 dB fall times):

   | Section | Soft ends t-10 / t-20 (s) | Soft ends drop at 0.05-0.1 s (dB) | Final note-off t-10 / t-20 (s) |
   |---|---|---|---|
   | Violins I | 0.09 / 0.31 -> 0.13 / 0.31 | -5.8 -> -4.4 | 0.08 / 0.15 -> 0.13 / 0.28 |
   | Violins II | 0.10 / 0.22 -> 0.21 / 0.30 | -5.6 -> -5.6 | 0.06 / 0.22 -> 0.11 / 0.26 |
   | Violas | 0.09 / 0.19 -> 0.16 / 0.22 | -8.9 -> -5.1 | 0.08 / 0.14 -> 0.16 / 0.22 |
   | Violoncellos | 0.11 / 0.32 -> 0.17 / 0.33 | -8.7 -> -3.7 | 0.11 / 0.32 -> 0.17 / 0.33 |
   | Double basses (19 ends, mostly p) | 0.14 / 0.58 -> 0.13 / 0.55 | -7.3 -> -6.9 | 0.07 / 0.26 -> 0.12 / 0.28 |
   | Master, final chord | | | 0.09 / 0.33 -> 0.12 / 0.33 |

   - mf-ff phrase ends were unchanged on every section (loud-end medians identical), and so were levels (0.5 s frames: median 0.00 dB).
   - Critic C's stem criteria pass on violas and celli. The master target does not: C asked for -10 dB at 0.2 s or later and -20 dB at 0.5 s or later, against 0.12 / 0.33 here. References: Brahms 1/ii 0.40 / 0.79 s, Brahms 4/ii 0.20 / 0.48 s; c43 (uncapped, old hall) 0.40 / 0.67.
   - Adopted as a step. The next test is 500 ms, or no cap at pp/p. Movement II measured 300 / 400 ms (mf-ff / pp-p): soft ends fell 10 dB in 0.21 s and 20 dB in 0.34 s, against 0.44 s uncapped.
4. **Horn pp cap (Movement II's question).** In the 1FH KS Master the Sus MAX dynamic layers sit at CC1 0 (pp, release 562 ms), 50 (mf, 394), 82 (f, 316) and 118 (ff, 237); read from the patch.
   - Movement I's soft horns play CC1 42 at p, 28 at pp and 18 at ppp. Assuming a linear crossfade between layers, that is about 84%, 56% and 36% mf layer.
   - The 237 ms cap covers both the pp and mf layers here, so soft horn releases are capped either way. A pp-only cap would act on less than half the sound at p.
5. **Positive stroke trims start at the moved onset (A #2, generic, strings).** `score_to_parts.py` `NOTE_TRIM_FROM_MOVED` (families / tracks, default strings) with `NOTE_TRIM_FROM_MOVED_MAX_S` 0.15. A positive note trim with a short per-onset ramp on an early, non-legato note starts at its moved onset - 0.01 qn and is full by the moved onset + 0.03 qn (exact breakpoints).
   - Before, the trim started at the score onset, so a led stroke played its first 0.2-0.3 s at the previous note's level.
   - Celli strokes, time with the pitch band more than 6 dB under the body: 84 144 -> 96 ms, 88 82 -> 6, 152 220 -> 0, 156 296 -> 200, 448 190 -> 124.
   - Wind and brass are left out: the trims it would move there are fitted accent and a2 steps.

## Run

- **Lock.** Waited behind the finale (16:19) and Movement II (16:47) threads; nobody else was waiting when my waiter started at 16:55. Lock held 17:32-18:57.
- **Main pass.** `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` (all 33 tracks MIDI-only; no Opus state changed), `restart` (33 tracks; 48000 / 512, no input), `render_cycle.py 46` (probe 0 late or holes), `quit`.
- **Pass 2.** `start`, `--pass2 open`, `--pass2 --midi-only` (7 production tracks MIDI-only, 7 new test aliases built), `--pass2 restart`, `render_cycle.py 46 --pass2`.
  - REAPER crashed 380 s into that render (EXC_BAD_ACCESS in an Opus worker thread, `~/Library/Logs/DiagnosticReports/REAPER-2026-11-07-181334.ips`), leaving truncated files.
  - Stopped the hung job, removed the truncated `render_pass2/`, `start`, `--pass2 open`, `render_cycle.py 46 --pass2` again: 14 stems, 7 to `test_stems/`, every alias check OK.
- **Swaps and stem fix.**
  - `actor_scripts/swap46.py` put the Violins I / II and Violas soft-cap test stems in place of the main stems. `splice46.py` kept the celli and basses main stems up to qn 711.7 / 711.85 and took the test stems from there (30 ms crossfade).
  - Then `stem_fix.py 46 cycles/c46/rendered_build build --apply` (Violins I 496 notch shortened, Cello solo 691 notch and 694 fill) and `render_cycle.py 46 --measure-only`. Originals in `render_first/`.
- **REAPER data.** The test tracks were deleted from the pass-2 project (`del_tracks.lua`), which was saved with 7 tracks; `--pass2 quit`, `unlock`.
  - Another thread was waiting, so I did not rebuild in REAPER with the post-render data: the 350 ms caps (five string tracks and the f62 aliases) and the stem-fix envelopes (Violins I, Cello solo).
  - c47's `build_reaper.py --midi-only` (and `--pass2 --midi-only`) fully rebuilds those instances, because their Opus state differs from `jobs/*.b64`, and rewrites the envelopes.
- **Records.** Snapshot `cycles/c46/before/`; render-time builds `rendered_build/` and `rendered_build_pass2/`; scripts in `cycles/c46/actor_scripts/`.

## Accepted

### B #1 (mandatory): the c45 Violas stem

- **Tools fix.** See "Values" 1. With only the tools fix, the regenerated parts.json was byte-identical to c45's (every production alias included). Re-run on the c45 test aliases, the check now passes the Violas alias. It still shows the Horn 1 / Violins II aliases' extra notes, which `tw_own()` windows remove.
- **Result.** The c46 Violas stem against c45's `render_first/30_Violas.wav`, with the old stem scaled by the new-minus-old envelope (`abstem46.py`): per bar median -0.05 dB. Only bars 21 (-1.0), 103 (-1.6) and 121 (-1.1) differ by 1 dB or more: the trail gain on the running figures. The same script on the c45 swap reproduces B's +7.1 / +5.8 / +3.0 / +2.6 / +2.8 (bars 34-38), +3.9 (44), +2.2 (129), +3.4 / +2.7 (135-136), +6.3 (145).
- **Balance (K):**
  - Bassoon 1 minus Violas at qn 132-135: c44 +4.2 / +3.9 / +6.4 / +6.8, c45 -2.9 / +4.1 / +1.8 / -5.1, c46 +4.1 / +2.7 / +7.3 / +7.9.
  - Violins I minus Violas at 136 / 137: c45 -0.1 / +0.2 -> +8.6 / +8.1.
  - At 576 / 577: c45 -1.6 / -2.3 -> +3.3 / +3.9.
- c45 CHANGES "Values" item 4 and loop/LEARNINGS (c45 release-trail bullet) now say the result is withdrawn.

### C #1 / A #5: soft string releases

- See "Values" 3. Test aliases "Vla / Vc / Vln I / Vln II / Cb softcap test" over each source's own windows (`tw_own`). Adopted in mix.json on Violins I, Violins II, Violas, Violoncellos, Double basses and the f62 aliases.
- The re-bow fills were not refit, though the c44 rule asks for a refit after a release change. Measured instead (`cycles/c44/actor_scripts/rebows44.py`): the longer soft release made the re-bow dips shallower and no step grew.
  - Automatic re-bow dip medians, c45 -> c46: Violins I 3.7 -> 2.8, Violins II 2.4 -> 1.6, Violas 3.3 -> 2.1, celli 3.0 -> 2.2, basses 2.9 -> 2.4 dB.
  - Printed re-bows: Violins II 4.0 -> 2.4, Violas 4.9 -> 3.4, celli 4.8 -> 4.8.
  - Steps of 3 dB or more: 1 / 1 / 1 / 2 / 6 (c45 1 / 2 / 0 / 2 / 6).
  - Refit after the next cap change.

### C #2 re-test (Horn 1, Violins II)

- See "Values" 2. Not adopted; Violas keeps -6.

### Timpani (Dan's priority): B #2, C #4

- **Bar 174.** `roles.json` Timpani [692, 696, 6] -> 2. Timpani minus the louder bassoon at 78-196 Hz per qn 692-695: +11.3 / +10.6 / +10.4 / +11.7 -> +7.3 / +6.6 / +6.4 / +7.7 dB.
- **Bars 13-14.** `LEVEL_SHAPES` -3 dB from 49.5 to 55.3. Timpani minus the louder of celli and basses at 78-196 Hz per qn 52-55: +9.7 / +9.5 / +7.7 / +4.8 -> +6.7 / +6.5 / +4.7 / +1.8.
- **The three crescendo rolls (C #4 a).** 0 -> +4 dB ramps over 244-248, 456-460 and 556-560. Growth, last third minus first third: +0.5 / +2.1 / +0.1 -> +3.1 / +4.8 / +3.1 dB.
- The recorded Felt Cresc test (C #4 b) was not done (see "Rejected or deferred").

### S2 timing: A #1, A #4, A #2

- **A #1, Cello solo.** Leads refit as A gave them: `LEG_LEADS` 684 -0.03, 685 +0.07, 687 +0.10, 688 -0.02, 689.5 +0.05, 690 +0.04, 691 +0.06, 694 +0.03; `ENTRY_LEADS` 680 0.14. The level contour and join shapes moved with the moved onsets: piecewise-linear remap of each crossfade span, joins shifted by their target's change, the 685 seconds shape by +0.081 s.
  - pcX robust SD 93 -> 42 ms (A's target under 45); median +9 -> +11 ms.
  - Per note, c45 -> c46: 680 -93 -> -48, 684 +63 -> +20, 685 -93 -> -24, 690 +156 -> +28, 691 -62 -> +5, 689.5 -16 -> -26.
  - Still late: 687 +89 -> +118 (its crossover +93 -> +24), 688 +49 -> +69, 694 +153 -> +102 (crossover +204 -> +82).
  - The 691 transition burst (+8.6 dB over the body, new with the shorter lead) was notched and the 694 dip (5.4 dB) filled by stem fix: 691 burst 1.2 dB, 694 dip 3.8 dB.
- **A #4, Violins I entries.** `entry_leads.json` per onset, A's values. 286 was left out: a listed extra put it on the capped entry path (realised 0.05 s, later than its unlisted 0.12 s).
  - pcX over the 14 listed onsets: median +62 -> +16 ms. 56.5 -45 -> +6, 112.5 +39 -> -1, 127 +45 -> +20, 136.5 +68 -> +16, 322.5 +47 -> +21, 521 +55 -> +15, 568.5 -43 -> +6, 619 +79 -> -18.
  - Overshot: 472.5 +68 -> -48 and 474.5 +70 -> -43 (A's +0.05 on top of their c43 extras).
  - Did not move: 88 +72 -> +83 and 536 +105 -> +170 (inferred: the soft mf start, as in A #2 cause B).
- **A #2, strokes.** The generic trim fix ("Values" 5). Celli 152 now perceives early on pcX (-179 ms), but pcX is confounded there by the same pitch before it. On the band, the stroke is 2.7 dB under its body at the beat with no time under -6 dB.
  - The row A/B (Stac Leg BC + Slur + Port MAX against Sus Marc LITE) was not run. An offline build showed that `STR_REP_NEW_BOW` puts strokes back on Sus MAX after `ART_SPANS`: the test aliases got only the velocities, and celli 88's next note continued on the new legato row. The test needs a tools change: strokes keep an ART_SPANS row that is listed in STR_STROKE_ROWS.

### Levels: A #3, B #3, C #2, C #3

- **A #3 notches.** `JOIN_NOTCH` Violins I (69.604, 69.793, -5.9), (495.675, 495.96, -5.4); Violas (77.723, 78.112, -4.9), (290.010, 290.147, -2.4), 81 replaced by (80.590, 80.842, -4.2); Violoncellos (415.511, 415.850, -5.5); Bassoon 1 (375.011, 375.437, -3.0). A's -4.5 was reduced because the 375 fill is back at its c44 value {2.6 dB, pre 0, hold 0.18 s}.
  - Bursts over the louder body, c45 -> c46: Violins I 70 +7.5 -> +1.8, Violins I 496 +5.4 -> +1.3, Violas 81 +6.2 -> +2.6, Violas 290 +4.4 -> +3.1, celli 416 +7.3 -> +3.2, Bassoon 1 375 +7.3 -> -0.4 (join dip 3.1 dB on its own frames).
  - Violas 78: +7.7 -> +5.6. The rest is a swell at the end of the note before, ahead of the notch: identical audio in both renders, +9 dB at 77.6-77.66.
  - Violins I 496: the notch first ran to 496.167. This render's audio dips 5-6 dB at 496.0-496.1 (c45 held +5 dB there), so the join dipped 7.9 dB; the notch was shortened to 495.96 by stem fix (dip 4.3 dB).
- **B #3, letter F.** -4 dB on the Trombone 1 / Horns a2 half notes (bars 98-102). Tune minus brass (K), downbeats: +2.0 / +1.6 / +2.4 / +4.8 / +2.2 -> +4.9 / +4.1 / +4.9 / +6.9 / +4.1 (B simulated +5.1 / +4.0 / +4.9 / +6.9 / +4.1). Beats 3-4: +5.7 / +7.0 / +1.9 / +2.9 / +7.4 -> +6.2 / +7.6 / +2.2 / +3.0 / +8.0. The optional 398.5 lift cut was not made.
- **C #2, fff arrivals.** Lift rows `_all` +1.0 dB at 636 and 484, C's smaller variant.
  - Delivered steps into 636 / 484: +2.0 / +2.3 -> +2.8 / +3.3 dB; master +2.1 / +2.2 -> +3.1 / +3.2.
  - Delivery limiter 0.4 -> 1.0 dB (the peak is the bar-160 stroke) and span 19.3 dB. Without the lifts the span would be 19.2, so other c46 changes took the span over 19.0. +1.5 was not tried.
- **C #3, opening swell.** Celli and basses shapes over qn 3.8-12. Master K growth 3 -> 6: +5.4 -> +7.5 dB (c43 +7.7); 8 -> 10: +5.7 -> +6.4.

### Optional items done

- **A #5, slur heads.** `PICKUP_LIFT`: Violins I 259.5 +6, 146.5 +5, 377 +4, 66.5 +2.5, 61 +2, 58.5 +3; celli 419.5 +6, 355.5 +5, 533.5 +3.5. Broadband head level minus the next note's first 0.3 s, c45 -> c46:
  - Violins I: 259.5 -8.3 -> -4.5, 146.5 -5.8 -> -2.7, 377 -1.8 -> +0.6, 66.5 -6.1 -> -4.6, 61 +1.2 -> +0.4, 58.5 -3.5 -> -1.7.
  - Celli: 419.5 -8.1 -> -4.2, 355.5 -5.6 -> -2.0, 533.5 -5.6 -> -2.8.
  - My measure includes the previous note's tail in the head window, so it does not reproduce A's baseline (A had 377 at -7.4, 61 at -4.6).
- **A #6, portato bodies.** Violins I 60 body -3.0 -> -4.5, 140 -2.0 -> -4.0, 108 a -1.0 body (front 0). With my band measure (eighth's band peak against the tenuto's band median), the body is 2.7 / 1.3 / 0.8 dB lower than in c45 at 60 / 140 / 108; 572 is unchanged.
- **C #6, loud_eq spans.** The celli `loud_eq[2]` and basses `loud_eq[3]` end at 285.9-286.0 instead of inside the tied pp half note. The basses' bar-33 span ends at 128.0-128.4, before the fp whole note.

## Rejected or deferred

- **A #2 row A/B:** needs a tools change (see above). For c47: let `STR_REP_NEW_BOW` strokes keep an `ART_SPANS` row listed in `STR_STROKE_ROWS`, and keep the next note on its own row.
- **C #4 (b), recorded crescendo rolls (MANUAL-GAPS #12):** not done (time). The level ramps give the printed growth.
- **C #5, harp thumb-pick layers:** not done (optional).
- **Horn 1 seat -0.53, Main 0.2 on Clarinet 1 / Horn 1 / Trumpet 1:** not done. B measured the solo images 2-4 dB wider with no change in balance margins, so this is low priority.
- **B #3 optional (398.5 lift 6 -> 3):** not done.
- **For c47:**
  - The soft cap at 500 ms or with no pp/p cap (master final release target 0.2 / 0.5 s), then a refit of the final chord's re-bow fills.
  - Violins I entry leads at 472.5 / 474.5 back by 0.05 s; Violins I 88 / 536 (pcX +83 / +170).
  - Cello solo 687 / 688 / 694 (pcX +118 / +69 / +102).
  - Violas 78 (+5.6 dB, the previous note's swell).
  - The delivered span 19.3 dB (target 16-19).
  - Rebuild the main and pass-2 instances listed under "Run".

## Measured

**Master** (float sum of 40 stems): -17.3 LUFS, LRA 23.3 LU, true peak +3.1 dBFS, sample peak 1.423 (c45: -17.4 / 23.4 / +1.6 / 1.206). The peak is the bar-160 stroke with the +1.0 dB lift.

**Delivered** `cycles/c46/mvt1-mockup-c46.mp3`: -19.7 LUFS, LRA 14.9 LU, TP -1.8 dBTP, p10-to-max span 19.3 dB, limiter about 1.0 dB (c45: -19.8 / 14.9 / -1.9 / 19.0 / 0.0).

**Delivered S max:** 160 -11.3 > 122 -12.1 > 167-170 -13.6 > 26 -14.2; 158 -15.7, 117 -15.3, 140 -15.1, 131-134 -15.6, 69-72 -16.3.

**Attack probe:** 0 late or holes. Legato robust SD (Violins I / II, Violas, celli) 51 / 42 / 52 / 50 ms; c45 45 / 42 / 55 / 49.

**Silent notes:** the two known false alarms only (Trombone 1 552, Timpani 727).

**Cut-off tails** (master drop at 0.15 / 0.3 s):

| Cut-off (qn) | c45 | c46 |
|---|---|---|
| 679 (tutti) | -11.6 / -19.6 | -12.6 / -19.7 |
| 288 | -12.7 / -18.2 | -12.4 / -16.3 |
| 125.9 | -11.9 / -18.6 | -11.9 / -18.6 |

Fermata late RT 1.81 s.

**REAPER memory:**
- Main project: 23 GB at start, 44 GB settled (0 compressed), 45 GB (24 GB compressed) after the render.
- Pass 2 (14 tracks, 7 of them tests): 14 GB at start, 34 GB settled, 37 GB after (0 compressed).

# Cycle 45 (series 2): changes

## For Dan: what to listen for in c45

The orchestra is wider again: c44's drier hall had pulled the sound towards the middle, and the winds, brass, cellos and basses now spread across the stage as they did before, without the extra echo. Listen to any full passage, for example the second theme's tutti at bars 69-72 and the recapitulation at bars 131-143, where the cellos and basses also have their warmth back. In the cellos' and violas' repeated notes, which became new bow strokes in c44, the new strokes now land on the beat instead of slightly behind it: listen to the cellos at bars 12, 22, 94 and 168 and the violas and basses in the cross-rhythm of bars 135-137. The repeated tenuto note of the first theme (bars 16 and 144 in the first violins) is now an even pair of notes rather than a weak short note followed by a swelling one. At bar 147 the tune in horn, violas and cellos is balanced again (the violas had been 4 dB too loud from bar 145 to the climax). At bars 127-128 the cellos' soft repeated G under the clarinet solo is no longer covered by the timpani roll, and at bars 39-40 the cellos' held note no longer stands out above the violins' run. The violas' running figures (bars 97-102 and 117-122) are a little cleaner, and the soft bow changes inside the long held notes (the final chord, bars 45-46 and bar 146) no longer leave small holes.

## Values for the other movements (Movement II, scherzo, finale)

All measured on Movement I in this cycle.

1. **Stereo width after the drier hall (C #1).** Dry orchestras are narrow: with `fx_volume` 0.095 the master's L/R correlation rose from 0.57 to 0.69 (below 250 Hz 0.59 -> 0.78) and side/mid fell from -5.6 to -7.3 dB, narrower than all five references (0.49-0.55, -4.7..-5.4 dB).
   - **Step 1 (mix only):** set every side-only low cut that was added against the louder true-stereo hall to 0 dB (here `side_shelf` 200 Hz -2 lowshelf on Contrabassoon / Bass trombone / Tuba removed, Timpani 200 Hz -2 -> 0, Violoncellos / Double basses 170 Hz bell -2 -> 0; the 250 Hz +1.5 side high shelves stay).
   - **Step 2 (Opus state change, full rebuild):** `tools/build_reaper.py apply_mix` reads mix.json `width_by_mic` {mic label: width} (group or track): each listed mic's pan spread is max(track width, its own width), so the Close mic keeps the seat. Values: groups `wind`, `horn`, `trumpet`, `lowbrass` `{"Main": 0.35}`; Violoncellos and Double basses `{"Main": 0.45}`. Mic labels in the HO states: Close, Mid, Main, Surround, Vintage.
   - **Result (master, c44 -> c45):** correlation below 250 Hz 0.781 -> 0.567, 250 Hz-4 kHz 0.684 -> 0.637, above 4 kHz 0.550 -> 0.531, all 0.685 -> 0.618; side/mid -7.3 -> -6.3 dB. Per stem 250 Hz-1 kHz: celli 0.87 -> 0.70, basses 0.85 -> 0.73, Flute 1 0.90 -> 0.85, Horn 1 0.89 -> 0.78, Trumpet 1 0.85 -> 0.69. Stem levels (stereo power) unchanged within 0.15 dB on every rebuilt wind and brass track; no gain re-match was needed.
   - **Limits not yet met:** 250 Hz-4 kHz 0.637 (C: 0.62 or less), side/mid -6.3 (C: -6.0 or wider); Horn 1's image moved 1.7 dB toward the centre (C: 1 dB; move its seat 0.05 outward); the per-pitch R-L SD at 1.25-4 kHz rose over C's 1.2 dB on Clarinet 1 (0.41 -> 1.44), Horn 1 (0.73 -> 1.34) and Trumpet 1 (1.06 -> 2.00) (C: Main 0.2 on those tracks); the other solo winds stay at 0.67-1.15 dB.
2. **Re-bow fill lists end with their note (B #1, generic).** `score_to_parts.py` `REBOW_FILL_END_S` (default 0.12 s): a `rebow_fills.json` list that ends on a non-zero value holds to the end of the note its re-bow belongs to and is gone 0.12 s later, when a later note of the track starts before the next list. Lists ending on 0 dB keep their points (adding breakpoints re-samples the envelope, LEARNINGS c40). Check after any refit: c44's lists at qn 576 had held +4.1 / -2.0 dB over 26-29 bars.
3. **Sus-gap repeats take the re-tongue lead (A #1, generic).** `STR_REP_NEW_BOW` "sus_min_s" repeats (unslurred same-pitch Sus MAX repeats given the stroke gap) now take the string re-tongue lead (`RETONGUE_LEAD_S`, or the new `"sus_lead_s"` on tracks with none: 0.10 s here for the basses). Without it they sounded +94 ms median (23 repeats); with it +24 ms (18 -> 3 more than 60 ms late).
4. **Release-trail gain (C #2, `rt_gain_db`): withdrawn (c46).** `build_reaper.py` mix key `rt_gain_db` {"db", "rows"} scales every release-trail group's SourceProcessor volume (an Opus state change); the tool stands. The test result does not: the three pass-2 test aliases did not play their sources' data (score_to_parts.py carried each "espr." boost to the alias window's end: CC1 +40..+55 and CC11 +3..+42 over 17-25% of each track; the Horn 1 and Violins II aliases also played the Horns a2 / f62 notes their sources rest in). The violas "pass" and the Violins II / Horn 1 "fail" are void, and the "Vla rt test" stem that replaced the Violas stem played the violas 3-7 dB too loud in bars 34-38, 44, 129, 135-136 and 145. Do not use these numbers; see `cycles/c46/CHANGES.md` for the re-test with matched data.

## Run

- **REAPER lock.** Movement II held REAPER from 13:27, the scherzo from 14:05; my waiter started at 14:28 with no other waiter, and the lock was mine 14:35-15:35.
- **Main pass.** `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` in three batches with a save after each (25 tracks fully rebuilt for `width_by_mic`, 8 MIDI-only), `restart` (33 tracks; 48000 / 512, no input), `render_cycle.py 45` (probe 0 late or holes), `quit`.
- **Pass 2.** `start`, `--pass2 open`, `--pass2 --midi-only` for the 7 pass-2 tracks (Trumpets a2 and the three stac aliases fully rebuilt) and five new test aliases (3 release-trail, 2 legato), `--pass2 restart`, `render_cycle.py 45 --pass2` (12 stems; 5 test stems to `cycles/c45/test_stems/`).
- **Stem fix** (level only, `stem_fix.py 45 cycles/c45/rendered_build build --apply`, originals in `render_first/`): Violas 136 eighth, Clarinet 1 224, five soft re-bow holes; the Violas stem replaced first by the "Vla rt test" stem (it was believed to play the Violas' notes and envelope with the trail gain; it did not: c46 B #1, CC1 / CC11 differed over 17.5% of the track). `render_cycle.py 45 --measure-only`.
- **REAPER data.** Test tracks deleted from parts.json and the pass-2 project (`cycles/c45/del_tracks.lua`), `--pass2 --midi-only` for the f62 aliases and Cello solo (they carry their sources' envelopes), `--pass2 quit`; main `start`, `open`, `--midi-only` Clarinet 1 / Violins II / Violas (fully rebuilt with the trail gain) / Violoncellos, `quit`, `unlock`.
- **Records.** Snapshot `cycles/c45/before/`; render-time builds `rendered_build/` and `rendered_build_pass2/`; scripts in `cycles/c45/actor_scripts/`.

## Accepted

### B #1: the re-bow fill holds (tool, generic)

- `REBOW_FILL_END_S` (see "Values" 2). Scan of every string track: only B's three lists end on a non-zero value and hold past their note: Violas 576 (+4.1 dB, held 582-687.8), Violins II 576 (-2.0 dB, 582-699), Violoncellos 172 (-0.53 dB, 178-289). The envelope changed exactly over those spans. No other per-note table holds a value (early fills, loop fills, accent bodies, crescendo fronts and level shapes have explicit ends; note trims end at the next moved onset by design).
- Result (A re M): Violas minus celli over bars 147-150 +4.3 -> +0.1 dB (B simulated +0.2), Horn 1 re M -9.7 -> -7.8 (B -7.8); Violas re M in bars 157-170 down 3.6-4.6 dB, Violins II up 1.5-3.8 dB in bars 147-164.

### S2 / A #1: the new strokes' leads

- Generic: the sus-gap repeats take the re-tongue lead ("Values" 3).
- Per onset (`build/retongue_leads.json`, measured on c44 with `tools/pcx.py`, same-pitch repeats with no exclusion band): strokes 0.9 x (pcX - 0.015 s), the sus-gap repeats the same minus their new 0.10 s, capped at 0.12 s, skipped under 0.015 s; Violas 80 / 500 left as A asked; basses 570 / 676 corrected for the 0.3 x previous-note lead cap. Values: Violoncellos 47 +0.11, 84 +0.06, 88 +0.04, 152 / 156 +0.09, 164 +0.02, 326 +0.03, 374 +0.09, 448 +0.05, 456 +0.12, 656 / 668 +0.07; Violas 372 +0.12, 537 -0.03, 538 / 544 -0.04, 540 +0.02, 136 +0.10; Double basses 125 / 388 -0.10, 156 / 537 / 546 -0.02, 404 -0.05, 538 / 676 -0.04, 540 +0.02, 541 +0.07, 543 -0.03, 544 / 632 -0.08, 548 +0.04. No LEAD WARNING on these onsets; CC11 at every moved onset equals its score-onset value.
- Result (stem pcX, c44 -> c45): strokes median +92 -> +42 ms (more than 60 ms late 10 -> 7 of 15); sus-gap repeats +94 -> +24 ms (18 -> 3 of 23). S1 dips (A's measure, stem / master medians): strokes 7.8 / 4.5 -> 7.5 / 5.1 dB, sus gaps 6.4 / 1.7 -> 7.3 / 3.0.
- Still late: celli 152 (+118 ms: its slow fresh Sus MAX attack reaches -6 dB of its body at the same time after the score onset whatever the lead; more lead only moves the gap earlier), celli 656 (+257, two rises) and 326 (-231, estimator), Violas 372 (+88), basses 544 (+112).

### A #2: the portato tenutos

- Violins I 59.5 / 571.5 eighth trims (-4 / -3.5) removed (note_trims.json and the `_steps` ramp list); per-tenuto `LEVEL_SHAPES_S` (front from the moved onset to +0.10 s, body from +0.14 s to the next moved onset; A's values): Violins I 60 +1.7 / -3.0, 572 +1.8 / -2.0, 140 0 / -2.0; Violas 108 +1.8 / 0, 668 +1.3 / 0; Violoncellos 524 +1.2 / 0.
- Violas 136 (p): +0.10 s re-attack lead and, after the render, a +6 dB lift on the eighth (it gave way to 0.11 s and barely spoke: -6 dB against c44, the tenuto 11 dB over it), no early fill, -2 dB on the tenuto body from +0.15 s; its -2.5 note trim removed.
- Result (pitch band, re the tenuto's body; c44 -> c45): Violins I 60 eighth -11.0 -> -4.9, front -9.5 -> -4.8; 572 eighth -7.9 -> -6.1, front -5.6 -> -3.6, pcX -110 -> +20 ms; 140 eighth -7.2 -> -1.7, pcX -49 -> +4; Violas 108 front -5.3 -> -3.7, 668 -4.8 -> -3.6; celli 524 front -4.1 -> -2.6, pcX +46 -> -42. Violas 136 after the stem fix: eighth peak level with c44's, the hole moved before the beat (-0.20..-0.05 s), tenuto body 2 dB over the eighth.
- Not met: Violins I 60 / 572 bodies stay 4-4.7 dB over their eighth's peak (A: -1..+2) and 60's pcX stays +119 ms (the body's late swell before the next legato note).

### B #4, B #3, B #2, C #3

- **B #4** (bars 39-40): B's body cut after the celli 152 / 156 stroke fronts (`LEVEL_SHAPES`). Celli minus the loudest other stem at 155-159: -1.1 / -0.7 / +4.7 / +5.9 / +3.3 -> -4.6 / +0.3 / +0.7 / +1.2 / -0.7 dB A; master step into the bar-41 sf +5.9 -> +7.0 dB.
- **B #3** (bars 127-128, Dan's timpani rule): celli +3.5 dB over 504-512, timpani -2 dB over 504-512 (`LEVEL_SHAPES`). Celli minus timpani at 79-125 Hz per qn 506-511: +8.4 / +4.4 / +2.4 / +3.0 / +2.0 / +0.5 -> +13.5 / +9.6 / +7.8 / +8.8 / +8.0 / +6.3 dB; the roll still grows with its printed crescendo from bar 129.
- **B #2**: the celli 170 / 125 Hz and basses 180 Hz `loud_eq` bells also over bar 33, bar 41, 69-72, letter F-104, 136-137 and 143 (B's points). Master 100-250 re 250 Hz-2 kHz: bars 69-72 -10.1 -> -7.8, 136-137 -11.8 -> -7.6, letter F -14.1 -> -12.4, bar 33 -11.6 -> -10.4, bar 41 -10.3 -> -7.7, bar 143 -8.7 -> -6.4 dB.
- **C #3**: Trumpet 1's 5 kHz -6 shelf to 644.5. Its share of the master's 8-16 kHz at 642.9-644 -1.4 -> -3.9 dB; master 8-16 kHz re 0.5-2 kHz -33.9 -> -37.4.

### A #3: legato sags after the drier hall

- `auto_fills.py 44` on its default lead lines (c33 exclusions, plus celli 272 / 670 whose removal would leave 6-7 dB holes), then every changed fill simulated on the c44 stems (`fillsim45.py`): six retimes with the 0.35 s hold overshot the louder body by 3.5-6.7 dB (Horn 1 201, Bassoon 1 517 / 453, celli 460 / 598, Clarinet 1 247) and were reverted or shortened; Clarinet 1 700 and celli 201 reverted, celli 629 dropped. Hand fills: Oboe 1 582 {5.5 dB, pre 0.10 s, hold 0.06 s}, Clarinet 1 517 {5.5, 0.05, 0.10}. After the render Clarinet 1 224's new fill had lifted a note front that had no hole (+3.7 dB): replaced by a shape over its later sag (+0.38..+0.50 s). 34 fill entries changed in all (`build/early_fills.json`).
- Result (stem dip, c44 -> c45): Oboe 1 582 5.0 -> 3.2, Clarinet 1 517 6.1 -> 2.3, celli 372 5.5 -> 2.8, 413 6.4 -> 1.5, 402 4.1 -> 3.4, 196 5.4 -> 2.9, Bassoon 1 517 4.6 -> 1.8, 453 6.3 -> 3.6, Clarinet 1 178 5.7 -> 3.3, 224 sag 12 -> 6 dB.

### C #1: stereo width

See "Values" 1.

### A #5 / C #2: soft re-bows and release trails

- **Re-bow fills refined, no cap change.** fit_rebows.py smooths over 0.12 s and skips pieces under 1 s, so a refit cannot reach the 0.1-0.3 s pitch-band dips A measured. Instead: (a) the final chord's re-bows with a dip of 4 dB or more got a short correction on top of their c44 fit (0.7 x the dip over -0.06..+0.5 s, at most +5 dB; `rbrefine45.py`, 14 lists); (b) after the render, five soft printed re-bows with 8-13 dB holes (Violas / Violins II 580 at bar 146, celli 176 / 180 at bars 45-46, Violins II 192) got `LEVEL_SHAPES_S` rows filling them to 4 dB under the level before (`rbshape45.py`).
- Result (stem pitch-band dip): final chord Violas 716.5 / 718.9 / 721.3 / 726.8 5.4 / 4.6 / 5.6 / 7.2 -> 2.5 / 4.0 / 4.4 / 3.7 dB, basses 726.1 8.3 -> 3.3, Violins II 723.3 / 724.8 6.4 / 6.3 -> 4.5 / 3.1, celli 715.5 / 723.9 8.6 / 7.8 -> 4.3 / 4.6; Violas 580 14.5 -> 6.9, Violins II 580 11.9 -> 7.4, celli 176 11.6 -> 6.1 (box-10-ms measure). The 150 ms caps and the phrase-end drops are unchanged (cut-off tails within 0.5 dB of c44).
- **C #2** (pass 2): see "Values" 4 (withdrawn in c46: the test aliases' lanes did not match their sources). Adopted on Violas (mix.json `rt_gain_db` -6; the test stem replaced the Violas stem, the Violas instance fully rebuilt in the main project afterwards).

## Rejected or deferred

- **A #4 legato on the shared slurred eighths (test, pass 2):** Violins II onsets more than 30 ms from Violins I 26 -> 24 of 34 (A's target 6 of 57), joins of 6 dB or more 3 -> 6; violas 32 -> 31 of 44, 1 -> 7. Not adopted; the alias key `"globals"` that made the test possible stays in the tools.
- **A #5's 350 ms pp / p cap:** not made (the fill refinement brought the measured re-bow dips under 5 dB, and the soft phrase-end drop is kept).
- **C #2 on Violins II and Horn 1:** not adopted (see "Values" 4; the verdict is void, re-tested in c46).
- **Viola divisi test:** not done.
- **For c46 (C #1 limits):** Horn 1 seat -0.48 -> -0.53; Main 0.2 on Clarinet 1, Horn 1, Trumpet 1; if side/mid stays under -6 dB, the hall Width test (C's fallback, `reverb width` 1.5 in pass 2).
- **For c46 (S2):** celli 152 and Violas 372 still late; the gap before loud strokes (A's optional 0.045 s) untried. Violins I 60 / 572 portato bodies.

## Measured

**Master** (float sum of 40 stems): -17.4 LUFS, LRA 23.4 LU, true peak +1.6 dBFS, sample peak 1.206 (c44: -17.3 / 23.5 / +2.4 / 1.313).

**Delivered** `cycles/c45/mvt1-mockup-c45.mp3`: -19.8 LUFS, LRA 14.9 LU, TP -1.9 dBTP, p10-to-max span 19.0 dB, limiter about 0.0 dB (c44: -19.8 / 14.9 / -1.8 / 19.1 / 0.4).

**Delivered S max:** 160 -11.5 > 122 -12.2 > 167-170 -13.5 > 26 -14.2; 158 -15.6, 117 -15.4, 140 -15.0, 131-134 -15.6, 69-72 -16.3 (all within 0.2 dB of c44).

**Attack probe:** 0 late or holes; legato robust SD 45 / 42 / 55 / 49 ms (c44 49 / 42 / 52 / 50).

**Silent notes:** the two known false alarms only (Trombone 1 552, Timpani 727).

**Cut-off tails** (master drop at 0.15 / 0.3 s): 679 -11.6 / -19.6 (c44 -10.3 / -19.6), 288 -12.7 / -18.2, 125.9 -11.9 / -18.6; fermata late RT 1.80 s (c44 1.78).

**REAPER memory:** main project 21 GB at start, 43 GB settled (0 compressed), 44 GB (24 GB compressed) after the render; pass 2 (12 tracks, 5 of them tests) 16 GB at start, 28 GB settled and 29 GB after (0 compressed).

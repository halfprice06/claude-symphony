# Coordinator notes for cycle 57 (read first)

## Dan's standing complaints, in order
1. (2026-11-11) The track volume envelope has large peaks and valleys on individual notes, also on fast notes; it looks unnatural to him. c56 cut points 52200 -> 32612 but the count of notes with 3 dB or more inside fell only 2334 -> 2129 (aim was half). On the strings it barely moved (Violins I 175 -> 166, Violas 272 -> 271, celli 243 -> 229, basses 247 -> 235). This stays the first concern.
2. (2026-11-10) The string theme at rehearsal A (bars 15-23) felt choppy and not in steady time. Keep: Violins I 56-90 S robust SD 10 ms (1 over 40), long notes front minus tail 2.0 dB or less.
3. Earlier: articulations, per-track balance and blend, timpani rolls must not cover other parts, "mushy" low-mids.

## c56 facts (cycles/c56/CHANGES.md and cycles/c56/envelope_table.md have the full record)
- Delivery -19.7 LUFS, LRA 14.4, TP -1.7 dBTP, 433.45 s.
- New: generic NOTE_LEVEL pass (one level per onset), level changes on the score onset with a 40 ms crossfade, swells capped at 3 dB, ENV_THIN 0.1 dB, Double basses mute_eq deleted and 87.3 Hz bell at -4 dB (70-112 Hz share -15.0 -> -13.7).
- Regressions: theme over celli lower quartile +3.56 dB (target 3.9; c55's +4.95 included a 14 dB release jump); Violins I 128-158 body step 3.0 -> 3.4; celli 520-536 front step 2.4 -> 3.1; S readings moved with no note-on change (Violas 104-127 12 -> 21 ms, celli 520-536 19 ms with 6 over 40).
- Seven spans are on a skip list (left as built); four were applied by stem fix after the render and are in REAPER.
- Not done: common level for the theme's eighths; steady_levels54 refit; Horn 1 crescendo-note trim limit (40, 94, 620, 662); 484 horn front; harp levels to velocity; Oboe 1 95-100; celli 520-536 S; Horns 3-4 p +2 dB; Celli 603 arrival 0.8 dB under 601; Violas 612-616 flat instead of falling; bar 160 over bar 122 only 0.7 dB.
- Not verified on the render: final chord and Oboe 1 fills, single bass pitches after the bell change, clarinets bars 26-32 and 139-142, tutti-stop decays.

## Critic instructions for this cycle
- SAFETY for all critics: never exec tools/build_reaper.py whole to reuse vol_points; it sends jobs to whoever holds REAPER. Cut the source before ENV_LUA as tools/stem_fix.py does. Read-only on everything outside cycles/c57/critic_scripts/<slot>/.
- Critic A (articulation): besides your lens, take the string tracks and classify every note that still has 3 dB or more of envelope movement inside it by the layer that causes it (repeated-note dips, accents, fills, body lifts, re-bow fills, the step to the next note's level, skip-list spans). For each class give count, median size, and a stem-based test of whether removing or halving it makes the line less even (note-to-note step, join holes, separation of repeated notes). The aim is a list the actor can act on: which classes can go, which can be halved, which must stay. Check that a cap clips the deviation from the note's mean level, not the absolute value. Also verify the unverified items above.
- Critic B (balance): verify single bass pitches (B flat 1 to E2) after the bell change against the celli and tuba; the theme over celli +3.56 against the 3.9 target (propose the cheapest slow-layer fix, not a per-note one); melody over accompaniment where c56's NOTE_LEVEL changed levels (compare stems c55 and c56, list passages with a change over 1.5 dB in the melody-minus-accompaniment margin); Horns 3-4 at p.
- Critic C (blend and space): also check the mono divisi tracks ("Violins I f62", "Violins II f62", "Cello solo") for room against the wide sections, woodwind width (near-mono / Stereo Double), the 140-355 Hz share against the Brahms references used in symphony/mvt2/reaper-v600/cycles/c54/reports/B.md, and whether a retest of Sus MAX one-row with the finale's class leads is worth a range render.

## Actor constraints
- Shared REAPER lock: use wait_lock.py with a running waiter process; never take the lock by hand; if two waiters started in the same second, the folder path that sorts first goes first.
- First range render after a rebuild is unusable: render each variant twice, discard the first. State guard at cycle start and before the full render. Wait 45 s after each range pass.
- No score change. No commit. Nothing published. No REAPER preference changed.

## Notes collected from the other movements
# Finale c15 techniques 53-59 (symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md), for Movement I c57+
- 53 One-row theme on "Sus MAX" (not Marc LITE): violins' half notes hold level (27 of 29 within 4 dB), timing improved. Movement I c55 range test found Sus MAX worse (7.9 dB sag, 8 of 39 over 40 ms): retest with the finale's class leads before ruling it out; it would remove the need for body lifts (fewer envelope points).
- 54 Class leads fitted in one step: old lead + median S per (track, span, class); fit15.py.
- 55 Per-note level refit adds envelope points; weigh against Dan's envelope point.
- 56 Keyswitch 0.15 s early: on Leg Slur MAX / Leg BC MAX lines joins read 36-45 ms later; refit leads if used.
- 57 No gain: brass legato velocity cap 112; lead on basses' off-beat sustain eighths.
- 58 Sustain row with capped releases stops drier (drop at +0.3 s 14.9 -> 18.1 dB): check stops after a row move.
- 59 Waiter tie rule: folder path that sorts first goes first (mvt1 before mvt2/mvt3/scherzo). State guard again at the next cycle's start.

# Finale c16 / scherzo c14-c15 envelope findings (2026-11-11)
- Row trims and pitch trims return to 0 dB between detached notes of a run (merge rule never merges detached notes; pitch-trim ramp 0.25 qn longer than the note): 33 % of envelope travel in the scherzo. Hold across the run.
- 35-38 % of points collinear grid samples; 0.1 dB thinning halves the count (REAPER interpolates in envelope scale, not dB).
- Split three classes for on/off tests: slow, per-note level, per-note shape; switch off only shape (scherzo balance depends on per-note level layers).
- Accent swells start at the score onset, peak late, stack to 4.5-5.4 dB: accented notes start weaker. Front-weight and cap at 3 dB.
- UNI_BOOST 3 dB note to note worsens lines; make it a phrase level. Beat weight (metric_db) helps no line and starts 45 ms early.
- A level step on the beat moves single S readings by 60-130 ms with identical MIDI.
- Timpani: +6 dB envelope spikes on loud strokes = velocity +22 from the instrument.
- A row change inside a slurred line makes the following joins late (+58..+114 ms).
- Scherzo one legato row + keyswitch 0.15 s early + two-step lead refit: joins outside 25 ms 48 -> 9 of 100.
- Bass bells: check low notes one by one after removal (G1/A1 +2-4 dB against 0.7 for E1/B1).

# Adagio c54 results (2026-11-11)
- Bass: 80 Hz -6 bell removed, 140 Hz bell +4.5 -> +2, climax 100 Hz shelf halved: 56-112 Hz share -15.2 -> -11.5 dB, +0.8 dB per bar at most, limiter 1.0 dB. Two bass notes about 4 dB over neighbours after.
- RR_RESET_AT on a line: range passes and full render give identical joins (9 of 24 joins 15-87 ms away without).
- Hairpin gain held to the next onset and released over one quarter writes an unprinted 3 dB fall after a crescendo. Role edits move S by 32-35 ms; shapes starting after the attack window do not.
- Wind re-tongue gap is set by keyswitch time, not gap_s: KS_LEAD_AT in symphony/mvt2/reaper-v600/tools/score_to_parts.py (gap 81 -> 46 ms).
- symphony/mvt2/reaper-v600/tools/s_onsets.py now marks octave joins and flags level-band joins.

# Adagio c55 critics on the envelope (2026-11-11)
- SAFETY: critics must not exec tools/build_reaper.py whole to reuse vol_points (it sends jobs to whoever holds REAPER); cut the source before ENV_LUA as stem_fix.py does. Put this in every critic prompt.
- Travel by class: shape 59 %, slow 23 %, per-note level 17 %.
- No benefit there, removed: SWELL_DB, SOST_SUSTAIN_DB on winds/brass, METRIC_DB on harp and pizzicato, PT_DB_PER_ST / phrase tops, SLUR_PAIR_RELEASE.
- Benefit, kept: re-bow fills, early fills (minus about 60 rows), join notches, level fits, pitch and note trims.
- Faults: level trims keyed to the moved note-on cut the previous note's last 140 ms; trims fall to 0 dB between neighbours that both carry a lift; start shapes stack (8 dB or more) and peak after the beat.
- A 3 dB cap must clip the deviation from the note's mean, not the absolute value.
- Stairs on the 0.125 qn grid for hairpins and roles: ramps plus 0.1 dB simplification halve the count.
- Balance depends on per-note levels (up to 6.3 dB), not on shapes.

## Coordinator decisions on the c57 critic reports (actor: carry these out in this order)
1. Envelope on the strings (Dan's first concern; reports/A.md findings 1-3).
   a. Scale steady_levels54 about each span's median: 0.55 on Violins I 56-160, 0.7 on 536-576. Guard: Violins I 56-90 S robust SD 12 ms or less, long notes front minus tail 2.5 dB or less, on a range render.
   b. The 54 config-shape edges of 2.5 dB or more inside sounding notes: move each to the next score onset; drop the 16 that add a step the stem does not have (list in A.md).
   c. Remove the 14 Violas note-trim rows with no gain; Violins II row trims at half.
   d. Halve join fills where A's test shows no loss (celli join holes).
   e. Keep: repeated-note dips, re-bow fills, notches, theme body lifts, celli/basses pitch trims, accents at the cap.
   f. Range test only, one pair, low priority, after everything else and only if lock time allows: Violins I 56-90 on a row that does not decay (Sus MAX one-row with the finale's class leads) with the body lifts removed. Report front minus tail, S and step; do not ship it this cycle unless all three theme guards pass.
   Report the same before/after table as c56 (envelope_table.md) plus the count strictly inside the note.
2. Double basses pitches (B.md finding 1): pitch_trims "41" 3 -> -1.5, "37" add -2, "39" 3 -> 5, "43" -6 -> -4, "36" add +1.5 (skip onset 8.0), "32" -3.5 -> -5; note_trims 172.0 -3, 42.0 -3. EQ note-cut bells stay as c56 left them. Check bar 44 Horn 1 solo margin afterwards (target back to -2.5 or better).
3. Theme over celli: roles.json Violoncellos [56, 84, -2] -> [56, 88, -2]. Target lower quartile 3.9 or more.
4. Space (C.md): "Cello solo" seat 0.35 -> 0.20, reaper_pan 0.15 -> 0, width 0.2 -> 0.45 with a pass-2 range test (targets in C.md); Clarinet 2 and Contrabassoon width 0.05 with gain re-matched; Trumpets 1-3 send_offset_db R Brass +3.0; R Perc send -6 on the timpani group and -4 on the harp group. Trumpet rt_gain_db +18: range test only.
5. Low end in loud passages (C.md finding 3): take the half step on the Double basses loud_eq given in C.md (not the full one) and the master_eq change 3b (delete the 167 Hz bell, 260 Hz -1.5 -> 290 Hz -2.5). Guards: no single bar up more than 1.5 dB on the master, true peak and delivery loudness as before (-19.7 +/- 0.3 LUFS).
6. Horns 3-4 (B.md finding 3): no "drive" phrase shape on phrases whose notes average 2 qn or more (new config key); Horn 3 / Horn 4 soft_trim p +2.0; Horn 3 note trims +3 at 652.0 and 654.0. List every held line the new key changes and its level change.
7. Small: pickup eighths before long theme notes lost 2.3-4.7 dB in c56 (Violins I 66.5, 69.0, 72.5, 77.5, 144.5, 148.5): restore to within 1.5 dB of the neighbouring eighths. SHORT_SUS_AT celli 408.0 and Violins II 404.5. Re-bow fills still pulsing (A.md finding 4: Violins I 724.47, 726.51; celli 715.54, 719.48, 723.92, 725.21): residual refit. Celli qn 180 hole: reduce the -9.5 dB pre-cut. Accents under +1 dB over neighbours: residual refit to +2.5 dB on Bass clarinet, Bassoons 1-2, Horn 1, Oboe 1. Oboe 1 note at 90 and recap 536-548. Violas repeated notes with a gap under 40 ms: test a 60-80 ms gap on one passage.
Not this cycle: tutti-stop decays (C says the mix is already drier than the references early; leave), legato overlap 45-80 ms, MANUAL-GAPS.
If lock time runs short, ship 1a-1e, 2, 3, 4, 5 and carry the rest.

## Addition 2026-11-11 16:26 UTC (Dan heard c56: "it definitely sounds better so im wondering if we should go further or why we couldn't")
- Default for decision 1 is now: remove a per-note layer unless its removal causes a fault a listener would hear (hole, pulse, blurred repeat, sagging long note), not only a worse step median.
- Three-state clips (c56, shape class off, all per-note layers off) of bars 15-23, 23-26, one repeated-note and one bow-change passage in cycles/c57/ab3/. Paths go to the coordinator for the mockups page.

## Method change 2026-11-11 16:28 UTC (Dan: "i don't understand why its really necessary at all on a per note basis")
Replaces decision 1. Track volume envelope = slow balance only. Per-note fixes move to the instrument side (note-off gaps, overlaps, velocity, row choice, one CC11 value per note-on) or go away; any per-note volume move kept is a listed exception. Rule text: mockup-kit/README.md, section "Rule: the track volume envelope is for slow balance only".

## Tightened 2026-11-11 16:30 UTC (Dan: "i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem")
No exceptions list. Zero per-note layers on the track volume envelope. A fault that the instrument side cannot fix stays audible and is reported.

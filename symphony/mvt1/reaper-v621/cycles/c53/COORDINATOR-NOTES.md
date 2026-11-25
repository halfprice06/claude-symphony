# Notes for the c53 actor (from Movement II c48, relayed 2026-11-09)
1. fp and the per-dynamic level trims. build_reaper.py vol_points() reads the printed dynamic curve; in Movement II an fp spike was read as a printed f and the trim dipped the track volume 4 to 6 dB under the attack. Movement II now reads the p it falls to (parts.json key fp_falls). Movement I has one fp: Contrabasses at score qn 128 (bar 33). Measure the Cb volume lane and the stem around that attack; port fp_falls only if the dip is there.
2. After --midi-only builds a track can change level and timing on unchanged data (Movement II Trombone 1: +2.6 to +3.6 dB, 27 to 49 ms early). A full rebuild of the track fixes it. Do not fit rows on audio from a --midi-only build (same cause as the c51 brass rows).
3. Score source: build/sections/dev.ily line 386-387 changed (Violin II bar 110 hairpin, notation only). mockup.midi is identical and parts.json is identical; the only events change after the next LilyPond rebuild is one cresc start fewer at 436 and a cresc end at 440 on VlnII.

## (4) Finale c11 techniques 18-23 (measured there; full text in symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md)
Apply only where a c53 critic finding matches; measure before and after.
- 18. Repeated low-string eighths: measure at the fundamental (30-120 Hz). If on-beat strokes are weak, add a volume dip only in the played gap before each beat (-9 dB, note-off + 6 ms to next onset - 3 ms) and start the downbeat's metric step at the onset.
- 19. sf of an sfp on winds and brass: a post-fader bump (+3 dB over 0.35 qn, +4 on the weakest front) works as it does on strings. Try it before a Sus Accent row.
- 20. Legato lead tables: add a negative per-onset row to the total lead (base + velocity extras) before the clamp, not after clamping the base.
- 21. String chord repeats: a tenuto repeat inside one slur and one that starts a new slur need different gaps (0.06 s and 0.12 s). Slur starts are `slur -1` in the events list.
- 22. Note trims ramp in over 0.6 s, so on eighths they barely act (+3 dB realised +0.5). Use a level shape over the run.
- 23. Delivery ride after a subito: hold the row at 0 through the subito bar and ramp in over about 10 qn. When simulating, keep the parts.json copy next to mix.json or the delivery ratio falls back to 3.0.

## (5) Left open by the c52 actor (cycles/c52/CHANGES.md)
- Celli CC1 macro fails A's join rule (8 of 147 joins 2 dB or more deeper; violas without it 3 of 71). It is still in build/. SUPERSEDED by decision 1 in section (7): keep it.
- Width: 250 Hz-5 kHz correlation 0.566 and side/mid -5.53 dB are just past the reference edges (0.56, -5.4). The side bell at -3.5 dB was simulated inside. Decide with the c53 C report (blend and space lens).
- Flute 2 is 75-118 ms late at qn 280, 636, 639.5, 642: per-onset leads (finale technique 14: two players on one line need separate join leads).
- Bar 84: master rise +4.4 dB against the limit of 2; cello and bass sum varies 5.8 dB.
- Violins I sf at qn 78 peaks at +0.14 s (1.1 dB above its first 0.1 s).
- String diminuendi fall earlier now (50 % share 0.40 to 0.52), from the linear long ones.
- REAPER does not hold the post-render level rows (Horn 3 [165.5, 168, -3.5], cor anglais [584, 608, +1.5], the stem-fix shapes, note trim 601). They are in build/. Any `--midi-only` build rewrites every track's envelope, so check them after the build.
- Horn 1 legato-minus-other level +1.6 dB (limit 1.5).
- State-check flags expected: trumpet runs of about -3.5 dB (width loss, not modelled); basses +3.4 dB at 198-212 and 569.5-572 (round robins moved by the resets).

## (6) From Movement II c49 (symphony/mvt2/reaper-v600/cycles/c49/CHANGES.md)
- State drift is wider than one comparison shows: its c48 had basses, divided celli and Horn 1 notes 2-6 dB off on unchanged data, and c49 returned to c47's state. Run state_check.py against N-1 and N-2 (here c52 and c51; c51 was partly stale, so also c50).
- A mid-score CC16 round-robin reset is repeatable (two range renders identical after it); table RR_RESET_AT in its tools/score_to_parts.py.
- Finale items 18, 19, 21, 22 worked there: gap dip on bass repeats (30-120 Hz dip 2.7 to 7.7 dB), sf bump on bass trombone (+3 dB in the first 0.1 s), 0.12 s gaps on soft string repeats (dips 1.5-3.2 to 3.3-9.0 dB).
- New tool symphony/mvt2/reaper-v600/tools/pitch_check.py: per-pitch level change against the track after a mic or width change. Use it on the trumpets and trombones if the width or side EQ changes.
- A short "R Stage" return to widen a solo was dropped there as too wet. Do not add returns.

## (7) Decisions for c53 where the critics differ or leave a choice (these override the reports)
Reports: cycles/c53/reports/A.md, B.md, C.md. Do every ranked finding of A and B as written unless a line below changes it.

1. **Celli CC1 macro: keep it.** A re-measured with controls: 6 of 261 celli joins grew 2 dB or more (2.3 %) against 2.9 % and 3.2 % on tracks without the macro. The c52 actor's 8 of 147 against 3 of 71 is not a difference. Do not remove the map.
2. **Side bell stays at -4.5 dB.** Brass width per C: `track_width` trumpets (1-3, a2) 0.65, trombones (1, 2, bass) 0.75. Re-measure the make-up gains with the c52 range test (each stem within 0.3 dB of the no-width render). Pass: correlation below 250 Hz, 250 Hz-5 kHz, and side/mid all inside the references.
3. **Brass tail (C): half of C's step, behind a range test.** BRIEF S4 and Dan's "too wet" note stay in force, so the limit is the master, not the brass. Set `returns["R Brass"]["fader_db"]` -10.97 to -7.97, trumpet send offset -6 to -3, lowbrass offset -10 to -7, horn group `send_offset_db` {"R Brass": -1.0}. Range-test bars 82-83, 121-126 and 167-170 before the full render. Pass: brass tail at 0.3-0.6 s after cut-offs within 4 dB of the strings' tail, and every tutti stop on the master no wetter than c49 (time to -20 dB and the 0.3-0.6 s level). If the master fails at any stop, go back to the c52 values and report it. Do not go to C's full step in this cycle.
4. **Trumpets 1-3 release (C):** run C's pass-2 test on the note ending at 101.88 s first. Apply `rt_gain_db` only if the test shows the stem's fall at 180 ms moving toward the trombones' (-21.5 dB); start at +6 dB, not +9. If the test does not confirm the cause, leave it and report.
5. **Delivery master EQ (C), delivery only:** replace the 8008 Hz +0.8 dB shelf with a 3000 Hz -1.0 dB shelf, and move the bell from 167 Hz -1.6 dB to 260 Hz -2.0 dB (bandwidth 1.0). Pass: 2-6 kHz and 6-20 kHz shares closer to the references than c52, 250-500 Hz at or under the highest reference, delivered loudness -19.8 LUFS within 0.3, climax order unchanged (160 > 122 > 167-170 > 26). Keep the c52 master EQ values in CHANGES.md so it can be reverted.
6. **A #4 clamp order:** make the one-line fix, then re-measure all 16 onsets with a negative per-onset row; any that now lands late gets its row re-fitted.
7. **A, cor anglais at qn 275 (+158 ms with a -0.04 row):** measure it a second way on the stem before changing anything. Change the row only if both measures agree.
8. **B #4 Oboe 1 level shapes (+8 dB at 500-503.8, +6 dB at 496-497.9):** apply, then check on the stems that Oboe 1 does not pass Violins I in bars 124-126 (it doubles them; target 2-5 dB under). The CC1 floor of 64 on held notes is a range test only this cycle; report the result, do not ship it.
9. **B, Horn 3 row [165.5, 168, -3.5] and cor anglais [584, 608, +1.5]:** apply once in the build (they are in roles.json but not in the project). Replace the cor anglais row's check with one value per answer, per B #3.
10. **Finale item 18 on the basses (bars 27-31, 131-134, 140-142):** only if time allows after everything above; it is low priority per A.
11. **C's timing observation** (horn and double-bass sound at bars 25 and 137 beat 2 starting 0.3-0.45 s after the mapped note-on): check with the attack probe and one direct stem measure. If real, fix; if it is C's time map, write that in CHANGES.md for the c54 tempo critic.
12. **State check:** run state_check.py against c52 and c50 (c51 was partly stale). The state guard must read 0 stale tracks before each render.
13. No new returns, no change to any REAPER preference, no change to the score sources.

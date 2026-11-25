# Cycle 10: changes (actor)

Render c10 from a freshly restarted REAPER (32 tracks; 29 tracks updated with `build_reaper.py --midi-only`, no patch reloads), then one level-only stem fix (`tools/stem_fix.py`; first-render files in `cycles/c10/render_first/`). REAPER was updated afterwards with `build_reaper.py --mix-only` (the 16 stem-fixed tracks), saved and quit, so the project matches `build/`. Snapshot of the c09 tools and data: `cycles/c10/before/`. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c10-actor/` (`crit.py`, `misc.py`, `rbcheck.py`, `seam*.py`, `pdiff.py`).

Every level-only change was first simulated on the c09 stems (`stem_fix.py 9 cycles/c10/before build --out ...`) and the simulation was checked against each critic's pass criterion. The render matched the simulation within 0.1-0.3 dB everywhere these were measured, so the renders are now repeatable enough to tune by simulation.

## Accepted

### Second theme head (A #1 with C #3a/b, combined)
- `build/early_fills.json` quarter fills (`pre_s` 0.10, `hold_s` 0.40): Horn 1 188/588 +6.5 (A proposed +5; +5 left the quarter 3.9 dB under the eighth in the simulation), Violoncellos 188 +2.5, 588 +5.0, 684 +5.5, Violas 588 +2.5.
- `build/note_trims.json`: Horn 1 189 -2 -> -6, 589 -4, 201 -4, 601 -4, 191 +3 and 591 +4.5 (C's arrival notes; `NOTE_TRIM_RAMP_S` 0.25 s so the lift is there on the arrival's first beat), 192 +4 -> 0 and 592 +5 -> +1 (the unmarked downbeats were the phrases' loudest beats); Violoncellos 189 -4, 589 -5, 601 -5, 685 -3; Violas 601 -4.
- `LEVEL_SHAPES`: Horn 1 -2.5 dB over 190.1-190.85 (the tenuto's bloom); the celli's c08 ramps at 189 (new) / 589 held through the arrival to 591.9/191.9 (C's 192.0 hold made the bar-49 downbeat louder still), 201 held to 204.2.
- Measured (c09 -> c10): Horn 1 189 quarter minus eighth -7.0 -> -3.3 dB, tenuto peak minus quarter +15.2 -> +3.1, arrival 191 6.6 dB under the crest -> 1.0 over it (stem); Horn 1 589 -7.0 -> -3.2, +12.4 -> +1.9, arrival -9.0 -> -2.0 under. Celli 189: -2.8 -> -1.4 / +8.6 -> +3.7; 589: -5.0 -> -3.3 / +13.0 -> +3.5; 685: -5.2 -> -1.6 / +8.5 -> +0.7. Master: exposition beat 192 is still 0.8 dB over the printed crest at 196 (C's criterion not met; c09 1.1 dB at 192.5 against 196).

### Lento cello/bass sustains (A #2)
- `build/rebow_fills.json` by hand: Double basses 38.003 hold -4.4..-6 -> -0.5 (the fit's pre window sat in a sample dip), plus +4..+5 dB over +1.7..+2.3 s (a second dip before the bar-10 bow change); Violoncellos 37.377 cut -2.5 over +1.6..+1.95 s (the sample swells 10 dB there; A's "+4 hold from +1.6 s" would have lifted that swell) and +4 over +2.12..+2.75 s (the dip after it).
- `build/loop_fills.json` (first use in movement I; placed on the c09 stems, seconds after the moved start): Violoncellos 24.0 / 176.0 [-6 dB bloom cut at 1.0, +4 lift at 2.2], 4.0 [+5 at 2.0, width 0.3], 704.0 [-5 at 0.93]; Double basses 36.0 [+6 at 2.1], 48.0 [+5 at 1.87]. `score_to_parts.py`: overlapping bumps now take the value of larger size, so negative bumps work (before: `max()` dropped every cut).
- `NOTCH_SKIP` (as A's item 3, without moving re-bow points): no 14-CC bow-change notch at celli 40.0, 52.0, 164.0, 720.0 and violas 52.0, where an automatic re-bow 0.12-0.52 qn before already changes bow. The re-bow shapes of those rows were refit on c10 (`fit_rebows.py 10 --tracks Violoncellos,Violas --skip ...`); kept for celli 51.87 (dip -3.7 -> -2.0 dB) and 719.483 (-4.6 -> -1.6, master -2.9 -> -2.6); the 39.879, 163.877 and violas 52.384 refits were no better and were not kept. Note: `fit_rebows.py --write` with `--skip` drops every skipped row of the listed tracks from the file; the rows were merged back by hand.
- Measured: bars 9-11 master fall at 39.5 3.6 -> 2.1 dB under the running maximum (A's 1 dB criterion not met); basses 37.5-39.5 hole -44.8 -> -38.8..-40.5 dB; celli 24/176 blooms +6.3/+7.0 -> +3.2/+3.3 dB over the note's median, the +2.1 s dips 4-6 dB shallower; celli 4.0 dip 7.1 -> 3.2 dB (the first placement at 1.98 s / width 0.45 made a +5 dB bump before the dip and was narrowed in the stem fix); basses 48.0 dip 7.6 -> 3.5 dB.

### Other articulation items
- A #4 step 1: harp étouffez at qn 650 (over a rest): `LEVEL_SHAPES["Harp"]` -30 dB over 650.08-651.9, `tail_hold: false` for the Harp in `build/mix.json`. Harp stem 650.3-651.9 now 36.6 dB under its level before the mark (c09 6.6).
- A #5: Horn 2 453 hand fill (`early_fills.json`: +6 dB, `pre_s` -0.15, `hold_s` 0.44): hole -9.9 -> -3.9 dB. `auto_fills.py 9 --write` (16 new, 10 raised, 6 lowered/removed; Violoncellos 684/589 excluded for the hand fills).
- C #6: `BREATH_SPLIT_AT` Cor anglais 27.0 [31.3]; Horn 4 720 middle split 723.8 -> 724.3. Loop autocorrelation at 3.85-4.05 s (level / centroid): Cor anglais 27-35 -0.01/0.50 -> -0.06/0.12, Horn 4 720 0.49/0.52 -> 0.14/-0.02.

### Balance (B)
- B #1 Violas `roles.json` [388.5, 408, -4] -> +2 and [464, 484, -3.5, 4] -> +2.5 (the c05 do-not-touch rows: they matched the strokes to c04's level, which was already buried). Violas -19.5..-24.4 -> -13.5..-18.5 dB re master per bar.
- B #2 `tools/fit_accents.py`: long notes protected with `>=`, run with `--keep-long-qn 1.4` (the output length of dotted quarters that end early is 1.43-1.45 qn, so 1.5 never protected them); 24 negative-step rows on such notes deleted, all three families refit on c09 and again on c10 (stem fix). Violins I 477 [0, -6] removed by hand again (c09 precedent). Measured on c10 before the refit: brass 32/37 in 2-4 dB, strings 112/135, winds 121/140 (c09 32/36, 121/135, 105/140); refit prediction 32/37, 117/135, 123/140. 2-5 kHz first 80 ms minus body: medians brass -7.7, strings -9.9, winds -11.5 dB; positive only on the known artefacts (Horn 1 273, Violas 120/536, Oboe 1 328, Clarinet 1 120).
- B #3 `find_unisons` (`UNI_BY_DYN`, generic): the louder printed dynamic is kept first. Horn 1 now plays the ff A-flat3 at 670 (Horn 4's chord tone enters at 671.4 by `UNI_DELAY`) and its mf E4 at 418 (Horn 3 from 418.9). Horn 1 re master 670-671.5 -17.6 -> -11.8 dB (theme notes around it -9.7), 418-419 -24.4 -> -10.2.
- B #4 timpani `LEVEL_SHAPES` at 245.5-249.5 and 316.3-324: bars 62-63 roll -5.6..-7.5 -> -8.1..-9.4 dB re master; bars 80-81 drops 3.5 dB after the attack and grows into bar 82.
- B #5 `pitch_trims.json` Double basses A-flat1 (32) -3.5 (skip 244, 132, 216); Flute 1 roles [432, 438, 3, 0.25], [291, 300, 2]; Bass clarinet [432, 440, -2] (simulated by B: margins -0.9 -> +2.7, -1.9 -> +1.8 dB).

### Dynamics over time (C)
- C #1 `tools/deliver_master.py` `FAST_CAP_ABOVE` 4.0: delivered M max bar 160 over bar 170 0.2 -> 1.6 dB, over bar 82 0.8 -> 2.5; delivered S max 160 -10.3 > 122 -10.9 > 169 -12.8 (c09 -10.6 / -11.1 / -11.9).
- C #2 bars 60-61: second ramps from 238 (Violins I +7, II +5, Horn 3 and Violas +3). Master beats bar 60 -27.3 -27.3 -26.7 -27.7, bar 61 -24.6 -24.3 -25.0 -24.1 (beat 4 of 61 3.2 dB over beat 1 of 60; c09 -0.5); fall into the sub. p 8.3 -> 11.6 dB.
- C #4 bar 159: Trumpet 1 F5 pitch trim -6 -> -2, Horn 1 633 trim -5 removed, Clarinet 1 pitch trims halved (79 -3, 80 -1.5, 82 -2), a start-low shape on the 11 brass tracks (-3 dB at 632.3, 0 at 635.4; Trumpets 1-2 -5.5 in the stem fix). Growth over 632.3-635.5 (c09 -> c10): Trumpet 1 -3.0 -> +0.6, Trumpet 2 -3.3 -> +0.5, Horn 1 -1.0 -> +0.7, Trombone 1 +1.0 -> +3.1, Tuba +3.4 -> +5.5; master beat 1 of 160 over beat 1 of 159 2.8 -> 4.4 dB.
- C #5 soft-passage roles (Bassoon 1 [128.5, 140, 3], Violas [132, 140, 2], celli/basses [336, 352, 2], Clarinet 1 [504.5, 512, 2], celli [680, 696, 1.5], cor anglais [683, 696, 1.5], `_all` [696, 719, -3, 1]; percussion is outside `_all`). Delivered S: bar 34 -31.6 -> -30.2 (now over bars 5 / 14, -32.7 / -31.3); bars 85-87 -27.1 / -24.8 / -26.0 (bar 85 is 0.2 dB under bar 175, 86-87 over); bars 175-180 -26.2..-27.6, at least 1.4 dB under bar 173 (-24.8).

## Rejected or deferred

- C #3c (dynamic trims of the CC1 tracks held at each note's onset): rejected. The c09 per-dynamic trims compensate the CC1 layers' level (Horn 1 mp +7.2, f -0.8); held at the onset, a held note crescendoing mp -> f would keep the mp trim on the f layer and land about 8 dB over a struck f. The flat 184 crescendo is the sample's and the shapes, not the trim slope (c08, before the CC1 change, measured the same).
- A #3 a2 horn track: deferred again. The actor prompt checks for 32 tracks and the brief caps REAPER at about 45 GB (43 GB after this render); a 33rd instance needs a cycle that changes the track count deliberately.
- A #4 step 2 (étouffez at 244 and 654, new notes start with the damp): needs a second harp instance; deferred with A #3.
- A #2 item 3 as written (moving re-bow points onto the bow change): replaced by `NOTCH_SKIP`, which keeps the fitted re-bow rows.
- Not reached: A #1 / C #3 phrase crest (192 still 0.8 dB over 196), A #2 bars 9-11 (master 2.1 dB under its running maximum), C #4 trumpets (+0.5..+0.6 dB, target 1), C #5 bar 85.

## Before / after (c09 -> c10, after the stem fix)

- Master (float stem sum): -16.3 -> -16.3 LUFS integrated, LRA 21.1 -> 21.9 LU, sample peak 1.452 -> 1.381 (true peak +2.8 dBFS on the float sum). Top peaks 636.43 (bass trombone 0.49, Violins I/II, tuba), 637.63, 485.0 (tam-tam, bass trombone), 635.11 (Violins I E6 fill 0.70).
- Delivered mp3: -19.8 -> -19.8 LUFS, LRA 14.7 -> 14.2 LU, p10-to-max span 18.2 -> 18.2 dB, limiter 2.0 -> 1.0 dB, -1.5 dBTP. Motion (mp3) 8.84/4.70 -> 8.59/4.48 dB: the fall comes from the delivery cap (the c09 master through the new delivery measures 8.60/4.56), which removes the ride's lift from short loud bars by design.
- Attack probe: 0 flagged (first render and stem fix).
- REAPER memory: 42 GB (3.5 GB compressed) before the render, 43 GB with 30 GB compressed after it (other processes: about 2.8 GB VM, 2 GB Steam, 1.5 GB python).

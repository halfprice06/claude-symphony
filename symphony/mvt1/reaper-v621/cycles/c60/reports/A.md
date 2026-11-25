# Cycle 60, critic A: articulation and phrasing (re-bows, joins, accents, basses' eighths, tutti chord changes; harp, timpani, percussion, pizzicato, breath marks in brief)

Under review: the c59 render (`cycles/c59/render/`, `render_pass2/`) and `build/` (`build/parts.json` is byte-identical to `cycles/c59/rendered_build/parts.json`). Scripts and caches (28 MB): `cycles/c60/critic_scripts/A/`. Everything is measured on the dry stems, the master, or read from the data unless marked inferred. Nobody listened. Levels are 30 ms frames, 10 ms hop. "Master band dip" is the master filtered to 0.8-5 times the note's fundamental; "control" is the same statistic at times 0.7-1.6 s away from the change with no bow change within 0.45 s.

Not read this cycle: README.md, HISTORY.md, EW-TEMPLATE-PLAN.md, FINDINGS.md, and the LEARNINGS files beyond searches for re-bow, release and velocity; so I do not list which template sections are unapplied. Read: the c60 coordinator notes, BRIEF.md, `cycles/c59/CHANGES.md`, the c59 fault and accent tables, my c59 report. `~/.rpr-bridge/libs/ew_ho/ks_maps.json` was not opened (out of bounds), so I cannot name alternative rows for a patch; the Adagio's c57 reports could not be opened (access denied), so its loop facts are taken from the coordinator's notes and checked against this render.

## Manual notes (May 2021 HO manual, pages picked for the re-bow question)

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.89-90: DIV A / DIV B are one chair of each stand, Close mics only; a divisi part is "not much less" loud than the section; mix them with the non-divisi patches for the other mics | the doubling instance for staggered bow changes (finding 1c) | not used; if built, use the full-section KS Master for the copy (as `Violins I f62` does), not a DIV patch: the Adagio found DIV copies mono and 1.7-3 dB narrower |
| p.91-92: sustain samples "are looped so they continue to play as long as the note is held" | every string piece longer than the first pass of the sample | three pieces are longer than the loop and pulse (finding 1a) |

## 1. Re-bows: the 14 holes are not what the master shows; too many automatic changes; three pieces loop; printed bow changes speak 0.37 s late (strings, bars 3-14, 46, 72-76, 116-130, 178-182). Measured; sizes after are inferred.

Scripts: `rebow.py` (c59 definition, 70 re-bows, 14 holes), `rb_detail.py`, `rb_master.py`, `rb_master_all.py`, `chains.py`, `longp.py`, `tmpl.py`.

**What the master shows.** At the 43 automatic changes the master band dips 2.8 dB (median; quartiles 1.2 / 3.9); at control times 2.6 dB; dip minus control 0.0. At the 27 printed same-pitch changes 2.1 against 1.5. Two of 70 reach 6 dB in the master, none for 80 ms. The stem holes of 8-16 dB are real on the stems, but 9 of the 14 are 12-24 dB under the rest of the orchestra in their own band. The master dips of 5 dB or more that stand over their control are in two places: the printed changes of the Lento (Violins I 44.0, basses 47.0, Violas 296.0) and the final chord (basses 720.0 7.0 dB with 60 ms 6 dB under, Violins II 717.1 6.0, Violas 721.3 5.4 and 726.8 5.5, basses 718.2 5.2).

**The 14 holes, one by one.**

| re-bow (qn, bar) | stem depth dB, time 6 dB under | cause | CC11 | pieces around it, s | master band dip (control median / max) | verdict |
|---|---|---|---|---|---|---|
| Violins I 44.0 (12) | 12.3, 150 ms | printed: tie, downbow, f | 82 | 1.32 -> 3.41 | 4.4 (1.4 / 2.3) | printed re-attack, heard; lead (1b); no alias |
| Violas 36.0 (10) | 13.3, 210 | printed whole note, no tie | 54 | 4.92 -> 4.70 | 3.9 (1.1 / 3.5) | this is the printed separation; lead (1b) |
| Violas 40.0 (11) | 8.9, 110 | printed | 72 | 4.70 -> 2.14 | 3.5 (1.7 / 3.7) | same |
| Violas 52.0 (14) | 8.0, 90 | printed | 34 | 2.45 -> 3.61 | 0.5 (0.2 / 1.8) | not in the master; lead only |
| Violas 296.0 (75) | 8.4, 120 | printed whole note | 41 | 1.89 -> 1.64 | 6.6, 40 ms (2.0 / 6.1) | printed, heard; lead (1b) |
| Celli 180.0 (46) | 10.2, 280 | printed, after the slur | 34 | 1.20 -> 0.82 | 3.8 (3.1 / 4.5) | printed; lead (1b). The step of -8.9 dB is Leg Slur MAX against Sus MAX at one CC11 |
| Basses 47.0 (12) | 9.3, 120 | printed upbow after the tie | 88 | 3.70 -> 1.18 | 5.8 (2.6 / 5.7) | printed; lead (1b) |
| Basses 297.045 (75) | 16.2, 160 | automatic | 33 | 2.32, 2.91, 3.28 in an 8.5 s note | 0.8 (5.8 / 11.3) | not in the master; one change instead of two (1a) |
| Basses 489.716 (123) | 10.3, 80 | automatic, fff pedal | 125 | ten pieces of 2.7-3.7 in 29.3 s | 2.0 (4.2 / 6.6) | not in the master; six pieces (1a) |
| Basses 714.671 (179) | 9.3, 120 | automatic | 38 | 3.23 -> 4.16 | 3.9 (4.4 / 4.8) | final chord: 1a and 1c |
| Basses 720.004 (181) | 11.0, 130 | automatic | 38 | 2.16 -> 3.18, then 9.67 | 7.0, 60 ms (5.2 / 5.3) | final chord, heard: 1a and 1c |
| Violas 725.52 (182) | 9.3, 90 | automatic | 20 | 3.20, 2.53, 2.37 in 8.2 s | 1.0 (2.4 / 4.0) | two pieces of 4.1 s (1a) |
| Celli 295.0 (74) | 8.4, 100 | automatic, the one change in 8.5 s | 34 | 4.27 -> 4.24 | -1.1 (-0.9 / 3.1) | not in the master; leave |
| Celli 717.638 (180) | 8.2, 100 | automatic | 38 | ten pieces of 1.8-3.8 in 22.7 s | 2.0 | five pieces (1a), 1c |

What a hole is (rise and release of Sus MAX read from entries after rests and ends before rests, `tmpl.py`, 1-4 notes per CC11 band, so approximate): at CC11 under 70 a new Sus MAX note is 9 dB under its body 0.10 s after the note-on, 6-8 dB at 0.20 s, 2-5 dB at 0.30 s; the old note is 4 dB down 0.10 s after its note-off and 9-10 dB at 0.20 s. The power sum gives a 5 dB dip, which is the median of all 70 (4.2-6.0 per section). The 14 holes are the deep end of that distribution, not a separate fault.

**1a. Fewer automatic changes; no piece longer than the sample's first pass.** `longp.py`: every string piece over 5.2 s has its largest level autocorrelation at 3.96-4.00 s: Violins I 720-728 (13.0 s, Sus MAX) r +0.64, SD about its trend 3.1 dB; basses 722.67-728 (9.67 s, new in c59) r +0.49, SD 2.4 dB, range 10.9 dB; Violins I 708 (7.95 s, Leg Slur MAX) r +0.65 but SD 1.2 dB. Violins II 717.1-728 (16.3 s) has no peak there (r +0.32 at 1.58 s). So the loop is 3.96 s long in this render, which fits the Adagio's figure (first pass to 5.90 s, loop back to 1.93 s): a piece up to 5.3 s plays no repeated material. My c59 advice to merge the basses' last two pieces was wrong: I gave the merged piece as 3.8 s and it is 9.67 s with the rit. and fermata.
The automatic pieces are far shorter than that limit: 59 of 102 pieces at re-bows are under 3.0 s (medians: celli 2.2 s, Violins II 2.1, Violas 2.8, basses 3.2). With pieces of at most 5.3 s (`chains.py`) the automatic changes go 43 -> 29:

| held note | automatic changes now | with pieces up to 5.3 s |
|---|---|---|
| Celli bars 7-14 (27.8-55.0; the pieces between printed changes are 3.6-5.0 s) | 5 (dips 5.2-9.3 dB) | 0 |
| Celli bars 3-4 (6.3 s) | 2 | 1 |
| Celli final chord (22.7 s) | 8 | 4 |
| Basses bars 12-14 (8.5 s) | 2 (dip 13.7 dB at 52.92) | 1 |
| Basses bars 72-76 (286-304, 8.5 s) | 2 | 1, at about 293.6 (0.66 s before the celli's 295.0) |
| Basses pedal bars 116-130 (29.3 s) | 8 | 5 |
| Basses final chord (22.5 s) | 4, last piece 9.67 s | 4, five pieces of 4.5 s |
| Violas bars 178-182 (14.6 + 8.2 s) | 6 | 3 |
| Violins I last note (13.0 s) | 0 | 2 (pieces 4.3 s) |
| Basses bars 3-5 (11.0 s) | 1 | 2 |

Fix (`build/score_config.py`): the frozen lists (`_REBOW_FROZEN`, `REBOW_AT`) hold the old 3.1 s points, so re-list them: remove from `REBOW_AT["Violoncellos"]` every non-integer point in 28-56 (29.383, 33.403, 37.377, 41.38, 49.683) and one of the two in 10.8-16; give the celli's final chord four points and the basses' pedal five; basses 286-304 one point near 293.6; remove `REBOW_NONE["Double basses"]` (722.7, 729) and space the basses' final chord in five pieces; two points in Violins I 720-728 (on Sus MAX, about 4.3 s apart, 0.6 s from any other section's change). `REBOW_SEG_S` 3.1 -> 4.6 and `REBOW_MAX_S` 5.2 -> 5.3 for anything not listed; keep `tools/space_rebows.py` spacing (0.6 s).
Expected: automatic changes 43 -> 29; automatic holes 7 -> 3 or 4 (basses 297, Violas 725.5 and one of the basses' final pair go with their points; celli 717.6 may move to a new point); the five celli dips of bars 7-14 gone; basses' last piece SD 2.4 -> about 1.4 dB with no 4.0 s peak; Violins I last note SD 3.1 -> about 1.5 dB at the cost of two bow changes on the top voice (see 1c). c59 found no added pulse on 19 pieces that lost a split at 5.2 s (largest departure 4.6 dB against 4.4 on control pieces).

**1b. Printed same-pitch bow changes have no lead.** All 23 printed changes of 1 s or more start on the score onset (lead 0 ms) and reach within 3 dB of their own body 365 ms after the beat (median; quartiles 300 / 468; 415 ms at CC11 under 60, 285 ms above). The lowest frame is 50-270 ms after the beat. A bow change is centred on the beat; here the gap starts on the beat and the note arrives a third of a second late (Dan's S2). The c19 re-tongue lead skips notes that the re-bow code handles, and these are in `rebows`.
Fix: a lead for held same-pitch string repeats, in the rule that sets the 30 ms gap: `REP_MIN_GAP` new key `"held_lead_s": [(60, 0.20), (127, 0.12)]` by CC11 (`tools/score_to_parts.py`, where `held_gap` is applied; the old note ends `held_gap` before the moved note-on). Expected: arrival +415 -> about +215 ms at soft levels and +285 -> +165 ms above; the lowest frame from +50..+270 ms to -150..+70 ms; stem depth unchanged (8-13 dB), master dip unchanged (3.5-6.6 dB, which is the separation S1 asks for at a printed repeat). Check Violins I 44.0, Violas 36.0 and 296.0, basses 47.0 with `rb_detail.py`.

**1c. Alias instance: only for the final chord.** The score prints "change bow at will" there, which is staggered bowing inside each section. Form (the Adagio's c56 doubling): for 711.8-728 each of Violins I, Violas, celli and basses gets a copy on its own full-section KS Master, Sus MAX, in pass 2 (`ALIAS_TRACKS`, "windows" [(711.8, 728.0)], `hold_lanes` True); both instances hold the note with pieces of 4.3-5.3 s, the copy's changes halfway between the main track's (at least 2 s from them and 0.6 s from every other section's); each instance 3 dB down for the span as a divisi cut (`roles.json`, one row per track, edges at the note-on). The printed changes elsewhere get no alias: their dip is wanted, and at the automatic changes outside the coda the master shows nothing.
Expected (from the Adagio's medians, 6.2 / 8.1 / 5.5 -> 2.3 / 4.6 / 1.5 dB): pair dips at a change 3 dB or less plus scatter; master band dips in bars 179-182 from 5.2-7.0 to about 2-3 dB; Violins I's two new changes not heard as holes. Cost: four string instances in pass 2 (19-20 GB there in c59). If the lock time does not allow it, do 1a alone and leave Violins I on one bow (the pulse stays: SD 3.1 dB).

## 2. Sustained tutti chord changes: every brass long note ends 90 ms before the next note-on, winds 50 ms (bars 12, 28-31, 70-71, 102, 112-116, 123, 132, 139-142, 159-162, 168-170). Measured; sizes after are inferred from the finale.

`barline.py`: joins between two notes of 0.8 s or more on sustain rows (not legato, not staccato), 732 joins on 22 tracks. Written silence between note-off and note-on: brass 90 ms on every track (`WIND_DETACH["by"]["brass"]["gap_s"]` 0.09), winds 50 ms (`gap_s` 0.05; 15 ms at soft levels since c59). Lead 35-80 ms, so the silence lies before the bar line and the new note rises through it. Stem dip per join, median: Trumpet 1 11.7 dB, Trumpet 2 10.5, Tuba 9.1, Trumpet 3 9.0, Trombone 2 6.7, Bass trombone 6.2, Horn 1 6.2, Trombone 1 5.7, Clarinet 1 5.7, Flute 1 5.5, Clarinet 2 5.2, Oboe 2 5.0; 264 of 732 are 6 dB or more; the lowest frame is 12-57 ms before the beat.
At the 26 onsets where 8-17 wind and brass tracks change together, the dry wind-and-brass sum dips 3.3 dB (median; 6.0 at bar 123 and bar 168, 5.0 at 122.0, 4.9 at bars 102 and 116) and the master 2.4 dB; 8 of 26 master dips are 3 dB or more (6.4 at qn 122, 5.8 at 404, 5.2 at 564, 4.9 at 668, 4.0 at 562). This is the finale's c19 finding in this movement: the tutti breathes out before each chord.
Fix (`build/score_config.py`, `WIND_DETACH`; `tools/score_to_parts.py` where the gap is chosen): a long-note form, `"long": {"min_s": 0.8, "brass": {"gap_s": -0.04}, "wind": {"gap_s": -0.03}, "same_pitch_gap_s": 0.025}`: when both notes are 0.8 s or longer, the second has no accent, sf or staccato, and the row is a polyphonic sustain row, the old note ends 0.03-0.04 s after the new note-on at a pitch change, and 0.025 s before it at a same-pitch join. Leads unchanged. Short notes and accented arrivals keep the 90 / 50 ms gap (the S1 separation was tuned on them).
Expected: stem dips at these joins from 5-12 dB to 2-3 dB (a legato-size sag); wind-and-brass sum dip 3.3 -> about 1 dB; master dips of 3 dB or more 8 -> 2 or fewer. Check with `barline.py`; also re-run the repeat count (same-pitch long joins must keep 3 dB of separation).

## 3. The tremolo step at Violas 168 and the join holes: diminuendos end under the level they arrive at (bars 9, 43, 68, 126). Measured; the cause of the envelope step is inferred.

`join.py`, `v168.py`, `envsteps.py`, `envsteps2.py`, `undershoot.py`.

- **Violas 168.0 (17.8 dB "hole").** Printed: tremolo sf at 160, diminuendo, mf at 164, diminuendo, pp sustained at 168. Stem per beat: 160 -38.2, 164 -53.0, 167 -60.8, then the pp note -51.4 and -48.8. The pp is 9-12 dB louder than the end of the diminuendo into it. With the envelope removed the join is right: tremolo end -57.6 (CC11 46), pp -60.8 (CC11 34), a 3 dB step down. The step is the track volume envelope: -3.2 dB flat over 164-167.88, +9.4 dB from 168.0, a 12.6 dB jump in 60 ms at a join with no rest. `dyn_curve` falls 72 -> 51 over 164-167, so the pp trim should have come in over the hairpin; it is held and stepped at the note-on (inferred: the 3 dB/s edge guard, which treats it as a sudden printed change). The c59 CC11 floor of 45 could not close it.
- **Violas 500.0 (bar 126), same cause.** Printed: diminuendo from the fff tremolo at 488 to p at 500. Stem: 488 -33.3, 492 -44.6, 496 -56.0, 500 (p) -44.6. Envelope +3.4 / +2.0 / +1.2 / -1.2 / +6.9: an 8 dB step at 500. The bar before the p is 11.4 dB under the p.
- Nine more envelope steps of 5-9 dB at connected joins are row compensations that land right (Violins I and II into the Tremolo row at 664 and 484, celli 286 f Marc into pp); leave them.
- **Oboe 1 168.0 (10.4 dB).** The diminuendo 166-168 ends at CC11 20-25; the p it arrives at is 34. Old note -62 to -66 dB at the join, new note -56.
- **Bassoon 2 268.0 (11.5 dB).** Not a hole: the level rises from -61 to -50 with no dip. The diminuendo 262-268 ends at CC11 32-33; the p at 268 starts at 43-52.
- The same undershoot on 26 diminuendo ends that run into a note (CC11 just before the join 6 units or more under CC11 just after); four rise 4 dB or more on the stem: basses 32.0 +9.0 (25 -> 40), Bassoon 2 268.0 +7.6, Contrabassoon 168.0 +6.2 (32 -> 46), Bassoon 1 500.0 +6.1 (44 -> 50).
- **Flute 1 47.0 (13.2 dB).** A tongued change at f after the tied G-sharp 5 on Leg Slur MAX; the row change makes the old note end 87 ms before the new note-on, and the Sus MAX note has no lead: lowest frame -56 dB (body -39) at +30 ms, back at +150 ms. Violins I play the same change legato.
- **Flute 2 560.0 (14.1 dB).** The F6 at 558 falls 4.7 dB over its own 0.9 s at flat CC11, then the 50 ms gap at ff. On this patch (FL2 KS Master, Sus MAX, CC11 104) the sample shapes differ by pitch: A-flat 5 falls 5.0-6.0 dB inside the note (4 of 4 notes), G5 rises 12-14 dB (2 of 2), F5 rises 5-7 (3 of 3). That is the source of Flute 2's four "sags" in the fault table.

Fixes:
1. The dynamic trim follows a printed hairpin: where a hairpin joins two printed dynamics with no rest, the trim ramps over the hairpin's length instead of stepping at its end (`tools/build_reaper.py` `vol_points`, the edge rule that moves a trim step to the note-on; a ramp over a printed hairpin is hairpin gain, which the rule allows). Violas 160-168 would ramp at 3.3 dB/s over both hairpins, 488-500 at 1.2 dB/s. Remove `CC11_FLOOR["Violas"]` (160, 168, 45) with it, or the tremolo will rise during its diminuendo. Expected: step at 168.0 +9.3 -> under 3 dB; bar 125 (496) from 11.4 dB under the p to about 5 (the rest is Leg BC MAX at CC11 73 lying 3 dB under Sus MAX at 55).
2. A diminuendo that ends on a printed dynamic with no rest ends at that dynamic's CC11, not under it: `CC11_FLOOR` rows Oboe 1 (166, 168, 34), Bassoon 2 (262, 268, 43), Contrabassoon (164, 168, 46), Bassoon 1 (496, 500, 50), Double basses (28, 32, 40); better, the same test in the hairpin code. Expected: Oboe 1 168.0 10.4 -> about 4 dB; the four upward steps of 6-9 dB -> under 3.
3. Flute 1 47.0: the old note ends 0.03 s before the new note-on (the keyswitch can lie inside the old note: it acts on the next note-on, as the c06 string Leg -> Sus entries already do), and the new note takes the flute re-tongue lead (0.07 s). Expected 13.2 dB for 120 ms -> about 6 dB under 80 ms (inferred).
4. Flute 2 560.0: finding 2's long-note form shortens the gap; the F6's own fall stays. Expected 14.1 -> about 9 dB. Left audible; a region gain cannot change a shape inside a note.

## 4. Basses' repeated eighths: every stroke sounds, 80 ms late (bars 27-31, 82, 131-133, 141-142, 167-169). Measured.

`cb8.py`, 94 same-pitch eighths on Sus MAX at 126 bpm (slot 238 ms). Length 0.62 of the slot (147 ms), lead 60 ms. Separation between strokes 6.0-9.6 dB (median per passage); 3 of 94 under 3 dB. So this is not the finale's "one pulse per quarter". But the loudest frame is 74-90 ms after the beat in every passage (quartiles +61 / +95): the note is still rising when it is released, so the peak sits at the note-off (+87 ms). The beat is a third of an eighth late on the bottom voice. In three passages the off-beats peak 2.8-4.7 dB over the beats (520-532: -25.6 against -30.3; 560-566; 664-676); 104-124 is even. I did not find the cause (the c58 round-robin reset test changed nothing).
Fix (`build/score_config.py`): `RETONGUE_LEAD_S["Double basses"]` 0.06 -> 0.12 for these runs, length unchanged (note-on 120 ms before the beat, note-off 27 ms after it). Do not lengthen to 70 %: the peak follows the note-off, so a longer note peaks later. Expected: peak +80 -> about +20 ms; separation unchanged. Stac On Bow on the basses is still untested and I could not read the patch's row list.

## 5. The single accents of +5 to +9.6 dB are neither row level nor pitch sample level. Measured.

`bigacc.py`: the 11 isolated accents of +4.5 dB or more in `cycles/c59/actor_scripts/accA/cache/acc_c59.json`, each against every other note of its track, pitch and row.
- Horn 1 (+9.6), Tuba (+5.6), Trombone 2 (+5.0), all at 328.0: the score prints ff with the accent after f at 324. The measure compares with notes at the f before. On the pitch's own curve the accent is +1.5 dB (Horn 1: CC11 100 -34.4, 116 -32.9), +0.5 (Tuba) and +1.5 (Trombone 2). The rest is the printed f -> ff step.
- Flute 1 (+8.0) and Oboe 1 (+5.2) at 553.0: inside the crescendo f -> ff that starts at 552.5.
- Oboe 1 113.0 (+8.5), celli 94.0 (+6.8), Violins I 325.0 (+5.0) are on legato rows, where one pitch at one CC11 spreads by 4-8 dB from note to note (Oboe 1 F5 on Leg Slur MAX: -38.6 at CC11 101, -44.8 at 102, -46.3 at 93). Basses 94.0 and 100.0 (+4.5, +5.7): Sus MAX on one pitch reads -34.4 at CC11 93 and -27.4 at 95. Each has one or two matches.
No fix. A row volume or a per-pitch region gain would move every note of the row or pitch and leave the spread. For the table: drop accents whose note carries a new printed dynamic or lies inside a hairpin; the maximum then falls to about +6 and the count over +3 dB by five.

## 6. Brief checks on what the last two reports skipped. Measured.

`brief.py`, `brief2.py`, `brief3.py`.
- **Breath marks (35 printed, 30 at a join):** all are played: silence 42-300 ms (median 143), stem depth 4-26 dB. Thin ones: Bassoon 1 636.0 (42 ms, 6.3 dB), Horn 4 88.0 (59 ms; Horn 3 at the same breath 119 ms), Flute 1 636.0 (62 ms), Oboe 2 644.0 (60 ms). At the breath before the fff at 636 the ten staves stop 132-242 ms before the beat, which reads as a section breathing. Optional: a floor of 100 ms on breath silences.
- **Pizzicato (basses 33 notes, celli 3):** the stroke is within 6 dB of its peak 23 ms after the beat on the basses (quartiles +10 / +58), 77 ms on the celli (3 notes); bowed entries on the same track 53 ms. Same pitch and velocity differ by 1.1-3.4 dB (round robins). No change.
- **Harp:** the 15 rolled chords start on the beat with the bass notes and the lowest right-hand note, then +30/+60 or +40/+80 ms; CC11 constant at 110; same pitch and velocity differ by 1.9 dB (median), 6.8 at most (A-flat 5 at velocity 76). The étouffez marks at 650, 658 and 727 fall to silence within 0.3 s. No change.
- **Timpani:** single strokes are within 6 dB of their peak 20 ms after the beat (quartiles +19 / +21), none under velocity 62; rolls are in pieces of 1-5.7 s with SD 0.7-2.6 dB about their trend; 3 of 27 roll-to-roll joins dip 5 dB or more (4.64, 469.9, 727.0; 6.1 at most). The bumps of 8-10 dB at 484, 497.1 and 664 are printed arrivals. No change.
- **Tam-tam:** the fff stroke at 484 is within 6 dB of its peak 180 ms after the beat and peaks at +716 ms; the pp stroke at 696 at +120 ms. `PERC_MAP["Tam-tam"]["tamtam"]["delay_s"]` is +0.05. A heavy tam-tam blooms late, so the peak is right; the start could sit on the beat: `delay_s` 0.05 -> -0.08 (inferred, small).
- **Suspended cymbal:** the roll's peak is 38 ms after 636.0. The Crash track's ring peaks 464 ms after it at -31.4 dB, against -33.0 dB for the stroke itself, and is 14 dB over the cymbal 1 s later; level is critic B's question, the shape is as designed.
- **Keyswitches:** 1076; the shortest time to the next note-on is 10 ms (7 cases). **Staccato:** 74 of 75 on short rows at half the slot. **Tenuto:** full length (1.00-1.05 of the slot) in every family.

## Do not touch
`REBOW_MAX_S` at 5.2-5.3 and the celli's single change at 295.0; Violins II's one bow on Sus MAX through the last chord (no loop peak); Violins I 708-715 on one bow (SD 1.2 dB); the 30 ms `held_gap` at printed bow changes and their dips (3.5-6.6 dB in the master is the printed separation); the 90 / 50 ms tongued gap on short and accented notes; the basses' eighth length (0.62 of the slot); the nine envelope steps that compensate row levels (Tremolo, Marc); accent CC11 values (the +5 to +9.6 dB readings are not accent faults); timpani stroke timing and velocities; harp velocities and constant CC11; pizzicato timing; the suspended cymbal's `lead_s`.

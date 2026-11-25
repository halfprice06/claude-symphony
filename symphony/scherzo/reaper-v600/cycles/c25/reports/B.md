# Cycle 25, critic B (balance and levels), on the c24 render

Measured on `cycles/c24/render` (stems, returns, master), `cycles/c24/scherzo-mockup-c24.mp3` and `cycles/c24/build_render/` (parts.json, roles.json, mix.json, score_config.py). Stems are compared with `cycles/c18/render`, masters and mp3s with c23. Positions are score quarter notes (qn); bar b starts at qn 3(b-1). (m) means measured, (i) means inferred.

How I measured:
- **Envelopes.** I loaded `tools/build_reaper.py` cut before `ENV_LUA`, as `actor_scripts/guard24.py` does, and ran its `vol_points` with c24's settings. I then ran it again with each part switched off (`ENV_NO_SLEW`, `ENV_NO_GUARD`), and once more with the dynamic trims flattened: each track's trim table set to its largest value, which is the envelope that finale technique 135 would leave. The guard rules are guard24's: a step is 1.5 dB within 0.5 s at more than 6 dB/s; the first-0.35 s test flags a change of 1.5 dB or more.
- **Stems.** Bar and window powers. For note levels, the 90th percentile of 50 ms RMS in each bar.
- **Line masking.** `cycles/c23/actor_scripts/inner23.py`, run unchanged.
- **mp3.** ffmpeg ebur128 momentary loudness; a bar's value is the median of its momentary readings.

## Manual notes

`loop/MANUAL-READING.md` has no row for c25 (the schedule ends at c20), so I did not do the page reading. Instead I read the pages behind finding 1, and I used `loop/MANUAL-GAPS.md`.

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the continually changing dynamics" (May 2021 manual p.64); "VOLUME (CC 7) is best used to set the overall upper limit on the volume of each track in the mix, relative to each of the other tracks" (p.151) | The dynamic trims (mix.json `dyn_trim_db` / `soft_trim_db`) and the role rows are relative levels between tracks. That is CC7's job by the manual. | No. No track except the timpani writes CC7. All of these levels go into the post-hall volume envelope, and that is where most of the guard's remaining notes come from (finding 1). |
| CC7 law: 20·log10 (mockup-kit LEARNINGS section 3). Finale technique 128 (HS string KS Masters) and 135 (HO woodwind and brass KS Masters) measured a residual of 0.00 dB median and 0.4 dB p90. | Every wind, brass and string track here uses one of those KS Master families. | CC7 is not used. The Harp ("Harp Sus RR", not a KS Master) has no CC7 measurement (finding 3). |
| MANUAL-GAPS #9: half-section patch for Violins II "la metà" (p.89-90, p.222) | Violins II from bar 349 (full section at -3 dB) | Not used. I measured no fault from it: the solo, with Flute 1 and Violins II joined to it as doublers, leads by +13.7 / +15.0 dB in bars 349-356 (m). |

## Answers to the cycle 25 questions

**The guard's remaining notes (25 steps, 64 first-0.35 s changes) (m).** I classified the 70 non-harp notes:

| cause | notes |
|---|---|
| a printed hairpin or dynamic mark at the score onset of a note that starts earlier (a led note) | 26 |
| the sfp at qn 900 | 15 |
| hairpin-arrival releases and phrase shapes | 20 |
| role edges | 9 |

Most of them come from one mechanism. The dynamic trims are read from `dyn_curve`, which runs on score time, but the notes start at their moved onsets. Across the movement, 163 led notes play their first 0.1-0.3 qn at the previous dynamic's trim, off by 1.5 dB or more. The worst are the trombones and tuba at 993 (+12..+15 dB) and Clarinet 1 / Clarinet 2 / Bassoon 2 at the sub. p 828 and at 816 / 876 / 891 (8-9 dB). `note_slew` and `note_move_guard` then try to repair those heads inside the sounding notes.

I simulated finale technique 135: trims out of the envelope, envelope at gain plus each track's largest trim, CC7 = 127·10^((trim − largest)/20). With note_slew and note_move_guard as they are, the guard drops from 25 / 64 to **12 / 35 notes**. Replacements for what is left are in findings 1 and 3.

**The 16 track-bars that note_slew moved (m).** Most of them are corrections, not faults. Keep their levels.
- **Celli, bars 276 and 348.** These bars are nearly silent on the celli stem (-69 and -85 dB). The +4.7 / +5.4 dB is the first 0.53 / 0.46 qn of the next note: the sub. p note at 828 (moved onset 827.47) and the pp entry at 1044 (moved onset 1043.54).
  - The written envelope gave that head the forte's trim (-3 dB), then stepped +6 dB at 828, 0.13 s into the note.
  - The slew put the head at the note's own level.
  - The forte before the sub. p is unchanged: bar 275 reads -44.3 dB in both c18 and c24, and bar 349 reads -49.9 in both.
- **Trombones / tuba, bar 331.** The written trim jumped +13.5 dB at the pp mark of the pp < f crescendo at 993 and fell 13.5 dB against it. Slewed, the crescendo starts softer (Trombone 1 -57.2 against -51.3 dB in c18) and reaches the same f (-35.5 against -35.4).
- With trims in CC7 read on moved time (finding 1), 13 of the 17 track-bars I count are at the written level and need no slew. The four left are the role rows of Flute 2 302, Horn 1 208 / 356 / 218 and celli 192, each 1.5-2.9 dB.

**Inner lines (inner23.py; c24, with c18 in brackets) (m).** These lead:
- theme A, Violins I bars 13-28: +11.5..+15.3 (+10.8..+15.5);
- Clarinet 1's trio tune: +10.4..+13.1;
- celli 169-184: +5.2..+8.8 (+7.4..+9.8);
- Violins I 177-184: +13.7 / +5.2 (+15.8 / +8.1);
- Oboe 1 at 185: +12.4;
- trio ff 209-224: +12.0..+15.7;
- the solo with Flute 1: +13.7 / +15.0;
- Hn 1's motto tail: +13.1 / +13.9;
- Hn 1's last G sharp: +16.9.

Violins II's con sord. arpeggios came up as intended: -5.5 / +0.3 / -5.3 / -7.3 (-8.7 / -4.1 / -9.4 / -13.1).

These are under the rest:
- the reprise's second idea, Flute 1 + Oboe 1 at the sub. p (bars 277-280): -0.4 / -0.1 (finding 4);
- the codetta's first oboe phrase (bars 225-228): -6.9 (-7.0);
- the violas with Violas div in the trio ff (bars 213-224): -2.1 / -4.2 / -4.9 (-3.7 / -5.6 / -8.4) (finding 5).

**Per-bar master and mp3 against c23 (m).**
- Master: as the actor reported (median -0.02).
- mp3: median +0.1 dB. 17 bars moved by 1.0 dB or more. Each is a c24 change or round-robin noise: 58 +2.1, 62 +1.7, 290 +1.7 and 35 +1.5 (celli / fugato round robins), 217 +1.5 and 219 +1.1 (ride row removed), 170 / 173 -1.3 / -1.5, 192 -1.5.
- Section medians on the mp3 are within 0.7 dB of c23. p10 of the bar medians is -22.0.
- The summit bar 336 is the loudest bar (-7.5). The ff arrivals at 105 / 305 read 0.7 dB under bars 103-104 / 303-304, where the brass f crescendo peaks (bar 104: Trumpet 1 -29.6, trombones -30.4..-31.4, against -34.0 / -35.8 at 105). This follows the print (brass f from 309, strings ff at 310) and is not a fault.

## Findings, ranked by what a listener would hear

### 1. The dynamic trims are read on score time and written into the post-hall envelope. Move them into CC7, read at the moved onsets (finale 135). (m; the result after the change is simulated)

**Where:** every wind, brass and string track; 163 note heads off by 1.5 dB or more.
- Worst: Trombone 1 / Trombone 2 / Tuba at 993 (+15.3 / +12.1 / +15.4 dB over 0.29 qn);
- Clarinet 1 at 816 / 828 / 876 / 891 (±9.2);
- Bassoon 2 at 420 / 816 (±8.5);
- Contrabassoon at 618 (+8.3);
- Clarinet 2 at 396 / 816 / 828 / 1080 (±8.0);
- Violas at 300 (-8.0).
By track, Clarinet 1 has 20 such heads, the celli 16, Bassoon 2 12 and the violas 12.

**What is wrong.** `vol_points` takes `trim(step_at(dyn, q))` from `dyn_curve`, which is on score time, while the notes, CC11 and keyswitches are on moved time. A mark at a note's score onset therefore changes the trim 0.1-0.5 qn after the note has started. note_move_guard and note_slew then smear that step across the joined notes. This produces:
- most of the 64 first-0.35 s changes;
- the 16 shifted track-bars;
- the reversed crescendo in finding 3.
The trims also cut hall tails when they change in a rest, because the envelope acts after the Opus hall (BRIEF S3).

**Evidence (simulated with the c24 data):**

| version | steps | first-0.35 s changes | track-bars more than 1.5 dB from the written level |
|---|---|---|---|
| as rendered | 25 | 64 | 17 |
| trims flattened (135) | 12 | 35 | 5 |
| no note_move_guard, trims as is | 40 | 90 | — |
| no note_move_guard, trims flattened | 23 | 50 | — |

The last two rows show that note_move_guard must stay.

**Fix.** In `tools/build_reaper.py` (generic; a mix.json key such as `"trims_to_cc7": true`, scherzo on):
1. **Envelope.** Write the envelope at `gain_db + max(trim table)`.
2. **CC7 lane.** Write a CC7 lane `127·10^((trim(q) − max)/20)`: 20·log10 law, events every 10 ms on ramps.
   - Merge it with no existing lane except the timpani's, which stays as it is.
   - CC7 ranges: Trombone 1 trim range 15.5 dB gives CC7 21-127; Oboe 1's 4.1 dB range gives 79-127. The 1-step resolution is under 0.4 dB everywhere.
3. **Moved time.** Read `trim` from a moved-time copy of `dyn_curve`. Every curve point at a note's score onset moves to that note's moved onset, and a hairpin's curve starts at the moved onset of the note at its start. `score_to_parts.py` knows each note's shift (`shift[id(n)]`) and can write `dyn_curve_moved`.
4. **Holds.** Apply `SOFT_DECRESC_HOLD` and `cresc_trim_hold` to the CC7 values instead of the envelope.
5. **CC7 in rests.** In rests longer than `TAIL_HOLD_MIN_S`, hold CC7 like the envelope's tail hold and change it 30 ms before the next moved onset. CC7 also scales the releasing voices.
6. **Start and end.** Put the first CC7 value in the pre-roll. End the lane at its last value, not at 127. A reset under a ringing tail would move the tail before the hall.

Finale technique 135 measured the same law on these patch families (residual 0.00 dB median). Range-test one track per family before adopting.

### 2. At the summit (bar 336), the trumpets, printed f, now play over the fff woodwinds and the ff horns (m)

**Where:** Trumpets 1-2, qn 1004.76-1007.73; also Trombones 1-2 and Horns 1, 2 and 4.

**What is wrong.** `ARRIVAL_WEIGHT_AT[1005] = (-2.0, 2.5, 1.0)` applies to every wind, brass and string track that starts a note on 1005. With c24's `ARRIVAL_WEIGHT_MOVED` the +2.5 is held to the end of the arrival note: 2.97 qn on the trumpets and 8.97 qn on Trombone 1. Each trumpet's envelope steps from -1.2 dB at 1004.4 to +4.5 dB at its moved onset (+5.7 dB). Their printed dynamic stays f from 996: no crescendo, no new mark. The woodwinds and strings have the printed crescendo into fff.

**Evidence (bar note level, p90 of 50 ms RMS, dB):**

| | bar 335 | bar 336 | change | c18 bar 336 |
|---|---|---|---|---|
| Trumpet 1 | -33.4 | -25.4 | +8.0 | -29.3 (+4.1) |
| Trumpet 2 | -34.1 | -27.0 | +7.1 | |

Others in bar 336: Flute 1 -25.9, Flute 2 -24.6, Oboe 1 -26.7, Clarinet 1 -28.6, Clarinet 2 -26.1, Horn 1 -28.8, Horn 2 -35.5.

Trumpet 1, printed f, is the loudest wind or brass note in the bar except Flute 2. It is 3.4 dB over Horn 1's ff.

The score prints horns ff against trumpets f, which is Rimsky-Korsakov's rule: "two horns are needed to one trumpet", so the horns are marked one degree stronger (Principles of Orchestration, p.23, `reference-books/text/rimsky-principles/p0041.txt`). The two should arrive about equal, both under the fff woodwinds and strings. Dan's note on this summit is "weight, not bite" (BRIEF item 9, score coda.ily c200).

**Fix.**
- **Tool.** In `tools/score_to_parts.py` (the arrival-weight loop near line 6305), give the weight only to tracks whose printed dynamic at the arrival is louder than at `qa − pre_qn` (a printed crescendo or a louder mark into it). Make it a generic option, `ARRIVAL_WEIGHT_RISE_ONLY = True`. At 1005 that removes the trumpets, trombones and horns.
- **Hold length.** Cap the held +db at `min(arrival note end, qa + 1.5)`, so that a 9 qn trombone note does not carry the weight to bar 338.
- **Summit lead.** To keep spec 2 (lead 0.5 LU or more over every rival), raise the remaining tracks' value from 2.5 to 3.0 (`(-2.0, 3.0, 1.0)` in `build/score_config.py`).
- **Estimate (i):** brass power share at bar 336 is 0.126 of the master. Without their weight the master falls about 0.37 dB, and +0.5 dB on the others restores about +0.45 dB. The summit lead stays near +0.6 LU. Trumpet 1 lands near -31 dB p90 in bar 336, beside Horn 1 and 3-5 dB under the fff flutes and oboes.

### 3. What the guard still lists after finding 1, with a replacement for each class (m; the class counts are from the c24 data with trims flattened)

The 12 steps and 35 first-0.35 s changes left are 42 notes.

**a. Printed hairpins that start at a led note's score onset (15 notes).**
- Notes: Bassoon 1, Bassoon 2, Clarinet 1, Clarinet 2 and Contrabassoon at 213; Bassoon 2, Contrabassoon, Flute 2 and Oboe 1 at 1002; Clarinet 1 966; Horn 1 621; Horn 3 1028; Oboe 1 1036; Violins I 542; celli 519.
- Every one moves in the printed direction: the decrescendo 213-216 falls 1.6-1.8 dB in the first 0.35 s. The guard flags them only because the note starts 0.13-0.6 qn before the hairpin.
- These are allowed ramps (Dan: "section dynamics with hairpins as ramps").
- **Fix.** Start the hairpin's `slow:hairpin` ramp in `score_to_parts.py` at the moved onset of the note on its start, and use the same start in guard24's `inhp` test.

**b. Role edges inside joined notes (7 notes, plus Oboe 1's two below).**
- **Horn 1 at 1068** (rest of 14.7 s before): move the edges of `[1020, 1068, -2.5]` / `[1068, 1080, 3]` to 1067.70.
- **The others have no rest of 0.1 s or more within 1 qn**, so CC7 should carry the step at the moved onset nearest the edge, as finale technique 136 does:
  - celli 876 (`[864, 876, 5]`, gap 0.02 s): CC7 at 875.47;
  - Clarinet 1 900 (`[900.5, 912, -5]`): CC7 at 899.85;
  - Clarinet 2 838 (`[828, 840, -3]`): CC7 at the moved onset of the first note after 840;
  - Horn 1 442 (`[420, 444, 3]`): CC7 ramp over the last 0.3 qn of the 441.78 note;
  - Violins I 1012 (`[1008, 1014, 4.5]` / `[1014, 1017, 2.5]`): CC7 at 1007.6 / 1013.6;
  - Flute 1 384 (`[372, 384, -5]`, which ends at the arrival): CC7 at 383.85.
- **Oboe 1 at 387-390 and 855-858: a reversed crescendo.** The printed crescendos fall 6.0 / 5.7 dB on the stem, and did so in c18 too.
  - The role `[386.8, 393, -4.5]` / `[854.8, 861, -4.5]` is written as a fall at 386.3-386.8, inside the joined 386 note.
  - note_move_guard holds the level and lets it back at 2 dB/s across the printed crescendo, so the envelope falls 5.7 → 2.0 dB over 387-391 against the crescendo.
  - **Fix.** Put this role in CC7 over 386.3-386.8 and 854.3-854.8, where it is written. note_move_guard does not touch CC7, and the crescendo then rises from the lower level on CC11.

**c. The sfp at 900 (Clarinet 1, Clarinet 2, Flute 1, Oboe 1).**
- The sf spike is a +3..+4 dB `level` row before 900, and the fall to p is a `slow` fall of up to 5.6 dB in the first 0.35 s. This is a subito drop in the post-hall envelope, which BRIEF S3 forbids.
- **Fix.** Write `FP_SPIKE` as a CC11 (or CC7) shape on these tracks, so the hall rings under the p.

**d. Hairpin-arrival releases and phrase shapes (16 notes).**
- Hairpin gain released inside the arrival note: Flute 1 and cor anglais at 156 (-1.4 dB in the first 0.35 s), violas 735.
- Phrase shape (`shape` class) inside long notes: celli 573, a 6.6 dB step inside a 3.74 qn note; celli 519; Violins I 1012.
- The solo passage's small printed hairpins on joined notes: Violins II 1057 / 1061.5 / 1064 and the Violin I solo 1061.5 / 1064.
- **Fix.**
  - Hold the hairpin gain to the arrival note's end and release it in the rest after, the rule `ARRIVAL_WEIGHT_MOVED` uses.
  - Write `PHRASE_SHAPE` into CC11, since it shapes a line (manual p.151).
  - The solo hairpins are covered by (a).

**e. Harp (14 steps + 6 first-0.35 s changes, bars 77-80, qn 231-238).**
- Role and trim steps under ringing chords.
- **Fix.** CC7 on "Harp Sus RR" has no measured law. Range-test CC7 127 / 90 / 64 on one chord (expect -3.0 / -6.0 dB) before moving the harp's steps into CC7. Until then, the harp stays on its velocity cap.

### 4. The reprise's second idea (bars 277-280) is no louder than its pp accompaniment, because two role rows turn the tune down (m)

**Where:** Flute 1 and Oboe 1 espress. at the sub. p, qn 828-840. The accompaniment is Clarinets 1-2 pp, Horns 2-3 pp tenuto, violas pp and celli.

**Evidence.**
- The line (Flute 1 + Oboe 1, inner23): -0.4 / -0.1 dB over all others, louder in 41 / 58 % of frames.
- The same idea at 121, on Violins I-II, leads by +13.5.
- Window levels: Flute 1 -41.3, Oboe 1 -43.6, violas -47.3, Clarinet 1 -47.9, celli -48.7, Clarinet 2 -49.2, Horn 2 -49.6 dB.
- `roles.json` has Flute 1 `[828, 840, -3.5]` and Oboe 1 `[828, 840, -1.5]`. c07 set them to put Flute 1 over Oboe 1.

**Fix.**
- Delete the Flute 1 row. Flute 1's 828 note follows a 0.5 s rest, so the edge is in a rest.
- Keep Oboe 1 at -1.5, but move its start to 827.79, the rest before its moved onset 827.82.
- Lower the pp accompaniment by 2 dB with CC7 from each note's moved onset at 828 to 840: Clarinet 1, Horn 2, Horn 3, violas. Use CC7 rather than the envelope, because these edges coincide with the subito and must not cut the forte's hall tail (S3).
- **Expected (i):** the line +3..+4 dB on the inner23 measure, with Flute 1 still about 2 dB over Oboe 1.

### 5. Inner voices: the violas' upper div. voice in the trio ff, and the codetta's first oboe phrase (m)

**a. Violas + Violas div, qn 636-672 (bars 213-224).**
- Measured -2.1 / -4.2 / -4.9 dB under the rest. This is better than c18 (-3.7 / -5.6 / -8.4) but still the weakest line in a passage where the score gives the violas div. thirds against the tune.
- Violas div alone at 636-648 is -21.0, and -14.4 under the bass clarinet.
- **Fix.** Raise Violas div by 2 dB with CC7 over 624-672 (start in the pre-roll value or in the rest before its first moved onset), or lower the bass clarinet by 2 dB with a role row over 636-660, edges in its rests. Target: the pair at -2 or better in every window.

**b. Oboe 1, qn 672-684 (bars 225-228).**
- p dolce over pp Violins II / violas / Clarinet 2: -6.9 under the rest. The oboe is only 4.0 dB over Clarinet 2's pp and 5.3 over Violins II's.
- A role row `[672, 676.5, 4]` already lifts the first notes.
- **Fix.** Lower Violins II, violas and Clarinet 2 by 2 dB over 672-684 with CC7 (all three start together at 672 after the rit. bar), or extend the oboe row to 684 with its end edge in the rest after the 681 note.

The violas' first note at 576 (8 dB under the celli, by the actor's count) is the same kind of entry. The line's window value improved to -2.5 / +2.6 (c18 -2.8 / -1.8).

Do not touch:
- Theme A's balance: Violins I +11.5..+15.3 over the pizzicato bass and timpani; basses over celli +2.4.
- The trio tune in all four statements and Violins II's con sord. lift.
- The solo violin with Flute 1, Hn 1's motto tail and last G sharp.
- The sub. p contrasts: bar 120 to 121 is -5.7 dB, bar 276 to 277 is -5.5 dB on the mp3.
- The celli's sub. p and pp entry heads, the trombones' softer pp start at 993 (keep these levels when the slew is replaced).
- note_move_guard: removing it doubles the guard count.
- The delivery: -14.0 LUFS, LRA 10.5, summit the loudest bar.
- The c24 hall.

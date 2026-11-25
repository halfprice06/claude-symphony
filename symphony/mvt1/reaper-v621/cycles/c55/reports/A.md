# Critic A, cycle 55: articulation and phrasing (review of the c54 render)

Data: `cycles/c54/render/*.wav` (stems and master), `cycles/c54/rendered_build/parts.json`, the c53 render with its own `rendered_build/parts.json` for comparison, `build/score_config.py`, `build/steady54.json`, `build/steady_levels54.json`, `build/mockup-events.tsv`. Times come from `pcx.TM(parts["tempo"]).sec(qn)` of each render's own map (coordinator fact 1). Every number is measured on these files unless marked inferred.

Measures used on the theme lines (per note, stem, mono sum):
- front = highest 10 ms RMS from -30 to +100 ms around the score onset; body = median level over 40-90 % of the printed length; tail = median over the last 130-30 ms before the printed end.
- sounding share = time the note's own harmonic band (`pcx.band_env`, previous pitch excluded) is within 10 dB of its maximum, against the printed length.
- join hole = lower of the two notes' bodies minus the lowest level from -100 to +80 ms; hole length = time more than 6 dB under that.
- two-pitch time and crossover = `pcx.pair_window`.
- bite = 2-5 kHz level over -20..+60 ms minus 2-5 kHz level of the body (and the same for 0.5-2 kHz).

## Manual notes

Own choice of pages (May 2021 manual, PDF pages), taken from what c54 changed.

| Manual says | Page | Where it applies here | Does the render follow it |
|---|---|---|---|
| Marcato Sustain "plays a marcato sample in addition to the multiple sustain samples. The marcato sample ends relatively quickly"; the combination gives "extra power at the start of the note". | 91-92 | Every theme note of Violins I 56-127 and 536-576, Violins II 104-127 and 552-576, Violas 104-127, Violoncellos 520-536 (117 notes on Violins I). | The row is used as described, but on every note, long ones included. On the violins the extra power at the start is 6-9 dB of the sample's own level and the note then falls away (finding 1). |
| LITE instruments hold about half the dynamic and vibrato layers of MAX. | 61-62 | The same notes: the theme's dotted quarters, halves and the tied D-flat6 now play the LITE sustain layers. | Followed as a consequence of the row. Whether the held notes lost vibrato was not measured (inferred risk; see finding 1, option B). |
| "For any legato patch to generate a slur or portamento, two notes must have no significant time gap"; a slur makes the transition "as seamless as possible", a bow change accents the second note while connected. | 78, 98-99 | Printed slurs inside the theme (59-60, 61.5, 67-68, 75-77.5, 80.5-81.5, 84.5-85.5 and their returns). | No. The theme has no sampled transitions any more; a slurred note is a new sustain note that starts when the previous one ends, with the 150 ms release as the only connection (answers below). |
| String Sustain rows alternate up-bow and down-bow samples (round robin); RR reset makes playback repeatable. | 91, 145 | CC16 resets before each theme entry after a rest (`cc16` in parts.json, 10 on Violins I). | Yes. |
| Slur Runs (1st and 2nd Violins only) contain fast notes, slurs and sustained notes at three vibrato levels on CC1. | 96 | Tested by the c54 actor for the theme and rejected on timing (S SD 40 ms). | Nothing to change. |

## The coordinator's questions for critic A

**1. Does the theme on the marcato-sustain row still read as slurred where slurs are printed?** About as much as in c53, which was little; it did not get worse on the eighths (measured).

| Violins I 56-127 | c53 | c54 |
|---|---|---|
| slurred joins (37): hole median / over 6 dB / longer than 30 ms | 3.8 dB / 4 / 1 | 4.4 dB / 12 / 3 |
| slurred joins: two-pitch time median | 78 ms | 46 ms |
| bow-change joins (34-35): hole median / over 6 dB | 5.3 dB / 14 | 5.8 dB / 16 |
| slurred eighth targets (23): front minus body | +2.0 dB | +1.3 dB |
| bow-change eighths: front minus body | +4.4 dB | +1.3 dB |

A slurred join and a bow change now differ by 1.4 dB of hole depth and by the 30 ms gap, and by nothing in the attack of the second note (both +1.3 dB). Violins I 536-576, Violins II and Violas read the same way (slurred hole medians 4.0-5.0 dB, two-pitch 32-84 ms). The slurred eighths do not carry a marcato stab: their front is 1.3 dB over the body and their 2-5 kHz front is 1.3 dB under the body. So the slurs are not broken, but they are not audibly different from separate bows either. See finding 6 for a test.

**2. Are accents turned into bite?** Not into spectral bite, but into a level stab (measured). Accented theme notes of Violins I (13 in 56-127): front minus body +4.0 dB in c53, +11.8 dB in c54; 2-5 kHz front against body -0.4 → +4.1 dB, 0.5-2 kHz -1.6 → +5.7 dB. The front is no brighter than the body (2-5 kHz rises less than 0.5-2 kHz), so it is not a click. It is a note that starts 12 dB over where it continues, against Dan's 2-4 dB of weight. Violins I 536-576: +6.1 → +11.0 dB; Violins II +4.4 → +6.6 and +5.3 → +7.5; Violoncellos +5.0 → +8.9; Violas unchanged at +4.6. Finding 2.

**3. The repeated c'' at the bar 15-16 barline (qn 60.0).** Acceptable (measured). C5 band: 26 dB at -140..-120 ms, minimum 20 dB at +20 ms, back to 23-24 dB at +40 ms; broadband -35 dB before, -43 dB at 0..+20 ms, -38 dB at +40 ms. An 8 dB broadband dip, about 40 ms wide, with the new note back at +40 ms. The c53 state was one 630 ms note. The tenuto quarter comes back 1-3 dB under the eighth before it, so it has no weight of its own; that is part of finding 1 (the body of this note is fine: front minus tail 3.0 dB, sounding share over 100 %). The other same-pitch repeats: Violins I 108.0 dip 8.3 dB (band) at -12 ms, back at +6 ms; 572.0 6.3 dB at +14 ms, back at +46 ms; Violoncellos 524.0 11.0 dB at +2 ms, back at +72 ms; Violins II 108.0 only 4.7 dB (band), 7.3 dB broadband. No change proposed for 60.0; the actor's 110 ms test read early.

**4. Is "choppy" gone?** On the eighths, yes. On the long notes, no: a new fault replaced the old one (measured; finding 1).

| Violins I 56-127 | c53 | c54 |
|---|---|---|
| eighths (46) sounding under 60 % of their length | 0 | 1 |
| eighth to eighth body steps over 6 dB (29 pairs) | 0 | 4 |
| notes of a quarter or longer (33): sounding under 60 % | 1 | 12 |
| the same notes: front minus tail, median | 2.9 dB | 9.7 dB |
| next note's front minus this note's tail: median / over 6 dB | 1.7 dB / 3 | 7.1 dB / 23 |
| all neighbour body steps over 6 dB (75 pairs) | 5 | 18 |

The limit "every printed note sounding at least 60 % of its length, neighbours within 6 dB" fails on 12 of 33 long notes and 18 of 75 neighbour pairs of the first statement, and on the master (below).

## Open items in this lens

| Item | Measurement on c54 | Verdict |
|---|---|---|
| A #5 Flute 1 115.5 breath gap ("yes", not measured) | The note still ends at qn 116.000 in `rendered_build/parts.json` and in `build/parts.json`. Main track -34.4 dB at the beat and -38.2 dB at +60 ms; staccato peak -38.9 dB (c53: -33.4 / -37.0 / -38.9). | Not applied: the `BREATH_GAP_AT["Flute 1"]` row at config line 3908 has no effect on this note. Finding 4. |
| A #6 three join fills (rows in, not measured) | Violoncellos 672: stem dip 13.9 → 4.5 dB, master 4.2 → 2.6. Horn 1 415: 11.3 → 7.3, master 3.1 → 3.2. Oboe 1 95: 11.3 → 8.0, master 3.6 → 2.9. Oboe 1 99: 13.3 → 9.8, master 0.8 → 1.2. | Celli pass on the stem (limit 6). Horn 1 415 and Oboe 1 95 / 99 fail the stem limit; 415 and 95 fail the master limit of 2. Finding 5. |
| A #1 cor anglais 26 | Stem dip 0.9 dB, master 1.1 (confirms the actor). The same solo at 24.0 is unchanged: stem 5.9 dB for 172 ms, master 4.4 dB. | 26 closed. 24.0 open, finding 5. |
| Slur-start joins after decision 3 (93 not re-checked) | 79 wind and brass joins, c53 → c54: crossover median +46 → +32 ms, robust SD 59 → 27, outside ±40 ms 48 → 30, outside ±80 ms 23 → 6; two-pitch time median 92 → 56 ms, over 100 ms 30 → 7; broadband dip median 1.3 → 2.5 dB, over 6 dB 6 → 6. | The change works. Outliers in finding 5. Timing rows belong to critic C; single-estimator readings (fact 4). |
| Row changes between consecutive notes (fact 4) | Violins I 56-128: 36 of 70 joins (24 into a legato row) → 1 of 70 (0); 536-576: 17 of 33 → 0; Violins II 6 of 20 → 1 and 5 of 14 → 0; Violas 5 of 19 → 1; Violoncellos 5 of 16 → 0. Winds unchanged: Flute 1 7 of 25 and 4 of 22, Oboe 1 6 of 24 and 3 of 21, Clarinet 1 7 of 13 and 12 of 25, Bassoon 1 9 of 15, Trombone 1 9 of 15 (3-5 per line into a legato row). | Strings closed. The winds' theme lines still change row at a third to a half of their joins. |
| Re-bow fills in bars 15-32 and 131-144 not refitted | No re-bow point lies inside 56-128 or 520-572. Violins II 576.0: dip 4.7 → 10.8 dB (the note before it now sits at -62 dB, see finding 1). Violas 576.0 and 580.0: equal to c53 within 0.4 dB. | One row to refit after finding 1 is fixed. |
| Keyswitches, chords on legato rows | No keyswitch closer than 5 ms to its note, no chord on a legato row, on all 42 tracks. | In order. |

## Findings, ranked

### 1. The theme's long notes are a stab and a tail on Sus Marc LITE: they fall 8-15 dB inside the note (measured)

Where: every note of a quarter or longer in the `STEADY_LINE` spans of Violins I (56-127, 536-576), Violins II (552-576, and 118, 120 in 104-127) and Violoncellos (520-536). Violas are not affected (front minus tail 4.4 dB, as c53).

What is wrong: the row's marcato sample carries the level for the first 0.15-0.25 s and the LITE sustain under it is much lower. Violins I, bar 15 beat 2 (E-flat5, accented dotted quarter, 714 ms), 50 ms steps from the beat: -35 -33 -32 -36 -39 -41 -41 -44 -43 -45 -46 -45 -45 -46 dB, then the next eighth enters at -35. In c53 the same note read -33 -31 -34 -37 -37 -34 -37 -36 -37 -37 -36 -36 -38.

| line, notes of a quarter or longer | front minus tail c53 → c54 (median) | sounding under 60 % | next front minus tail over 6 dB |
|---|---|---|---|
| Violins I 56-127 (33) | 2.9 → 9.7 dB | 1 → 12 | 3 → 23 |
| Violins I 536-576 (22) | 1.1 → 7.7 | 0 → 4 | 2 → 11 |
| Violins II 104-127 (10) | 4.5 → 7.0 | 0 → 2 | 0 → 5 |
| Violins II 552-576 (8) | 3.9 → 9.5 | 0 → 3 | 2 → 4 |
| Violas 104-127 (10) | 4.7 → 4.4 | 0 → 0 | 0 → 1 |
| Violoncellos 520-536 (6) | 4.0 → 4.7 (unaccented 8.8) | 1 → 3 | 0 → 2 |

Worst single notes in c54 (front minus tail, sounding share): Violins I 57.0 12.0 dB / 39 %, 62.0 13.6 / 46 %, 65.0 12.2 / 42 %, 70.0 (half note) 9.7 / 53 %, 73.0 13.1 / 38 %, 78.0 (the sf D-flat6, tied, 1.19 s) 12.0 / 27 %, 86.0 14.5 dB, 105.0 14.8 / 41 %, 113.0 16.1 / 52 %, 118.0 15.3 / 43 %, 120.0 11.7 / 31 %, 548.0 (1.43 s) 16.2 / 19 %, 569.0 12.7 / 40 %, 574.0 13.0 / 59 %; Violins II 118.0 13.8 / 42 %, 120.0 14.4 / 42 %, 572.0 and 574.0 (half notes) 14.1 and 20.7 dB with the body at -62 and -63 dB (c53 7.1 and 4.2). Even the plain quarters of bars 23-25 and 135-137 fall 5-10 dB in 476 ms (c53: -5 to +3).

It is in the master: the pitch band of the 55 long Violins I theme notes falls front to tail by a median 1.1 dB in c53 and 5.5 dB in c54 (over 8 dB on 5 → 20 notes); in bars 15-22, where the violins are alone on the tune, 12-15 dB (57: 13, 62: 14, 65: 12, 73: 12, 78: 15, 82: 13).

Parts (Violins I 56-127, medians): of the 9.7 dB, 7.5 dB is the sample at a flat envelope and 2.0 dB is the volume lane. On the 13 accented notes it is 8.8 dB sample plus 4.5 dB lane (finding 2). The c24 lesson already says this of the row ("a stab, then a tail 12 dB down. Set the step from the body (+0.30 s on) and trim the front on its own"); the c54 level steps in `steady_levels54.json` are one step per note fitted to the whole note, so they set the front and leave the body low.

The phrase therefore reads long note loud-then-gone, eighths at full level, which a listener can still call choppy; the EW-TEMPLATE-PLAN sections 6-8 say the opposite of long notes (late-peak swells, lean-off of about 2 after the onset inside slurs).

Fix (range test both on Violins I 56-90, keep the S measure as the guard: robust SD and median must stay within 5 ms of c54's 6 / +2):
- A (keeps one row, so no fitted lead moves). For every `STEADY_LINE` note of 0.9 qn or longer on Violins I, Violins II and Violoncellos add a body lift in the volume lane, in seconds from the score onset: 0 dB to +0.12 s, rising to +D at +0.32 s, held to 0.03 s before the next moved note-on (through the release, c33 lesson), back to 0 at that note-on. D = the note's measured front minus tail minus 3 dB, capped at 9; as a first pass D = 5 on Violins I unaccented notes, 6 on accented ones after finding 2 is applied, 5 on Violins II, 4 on the celli's unaccented long notes, 0 on Violas. `LEVEL_SHAPES_S` already takes rows of this form (config line 3875); or add `"body_db": {score qn: D}` beside `level_db` in `STEADY_LINE` (`tools/score_to_parts.py`, the volume stage that reads `level_db`). Then refit `steady_levels54.json` for those notes from the body, not the whole note.
- B (if A leaves the body thin or without vibrato; inferred risk from the LITE layers, p.61-62). Put notes of 1.5 qn or longer on Sus MAX through `STEADY_LINE` `at` rows (`build/steady54.json`: `{"art": "Sus MAX", "lead_s": 0.06}`), keeping eighths and quarters on Sus Marc LITE. Sus MAX is a sustain row, so it repeats between renders (c54 lesson); c54's Sus MAX variant read a median of -28 ms at a 90 ms lead, hence 60 ms. Each such note needs its own level step (the row plays 8-10 dB lower on the violins).
- Accept when, on the full render: front minus tail of every note of a quarter or longer is at most 5 dB (accented at most 6), sounding share at least 60 % on all of them, next front minus tail at most 6 dB, and the master's pitch-band front minus tail median is under 3 dB.
- After that, refit the Violins II re-bow fill at 576.0 (dip 10.8 dB now).

### 2. Accents in the theme: the c53 accent shape is stacked on the marcato sample (measured)

Where: accented theme notes of Violins I (57, 62, 65, 73, 82, 100, 105, 110, 113, 118, 120, 124, 125; 548, 553, 558, 564, 566, 569), Violins II, Violoncellos (521, 526, 529).

What is wrong: front minus body +4.0 → +11.8 dB (Violins I 56-127), numbers under question 2. The volume lane still holds the shapes fitted for Sus MAX and the legato rows: at 57.0 it goes -6.3 dB at the beat, -2.4 at 57.063, -9.3 at 57.84 (parts.json `acc_fitted`, `accent_body` [57.0, -2.4], `build/accent_fits.json`, `build/accent_bodies.json`). That is 4.5 dB (median) of front-over-body from the lane on top of the 8.8 dB the row brings.

Fix: in `tools/score_to_parts.py`, skip the accent swell, the fitted accent trims and the `accent_body` cut for a note that carries `n["steady"]` on a "Marc" row (or empty those notes' rows in `build/accent_fits.json` and `build/accent_bodies.json`); the marcato sample is the accent. With finding 1's lift of 6 dB the accented notes then read about +3 dB front over body. Accept at +2 to +5 dB front minus body and a 2-5 kHz front at most 2 dB over the 2-5 kHz body (now +4.1).

### 3. Violoncellos, recapitulation theme 520-536: uneven eighths and a 21 dB fall on the accented A-flat (measured)

Where: Violoncellos 520-536 (with Clarinet 1, Bassoon 1, Trombone 1). This is also the line that fails S (robust SD 28 ms).

What is wrong: eighth-to-eighth body steps over 6 dB on 5 of 7 pairs (c53: 1); all neighbour pairs 8 of 18 (c53: 2). Bodies in order from 520.5: -32.5, -36.2, -36.4, -29.6, -34.9, -37.6, -29.2, -39.3, -41.2, -31.4, -41.2, -37.4, -30.6, -40.2, -32.7, -31.3, -34.2, -36.3, -37.6 dB. The eighths at 525.0 (-29.2) and 525.5 (-39.3) are 10 dB apart; 532.5 / 533.0 / 533.5 read -30.6 / -40.2 / -32.7. The accented A-flat3 at 526.0 peaks at -27 dB and is at -48 dB 450 ms later, with the next note at -30: its lane falls from -0.3 dB at 526.063 to -12.7 at 526.84 (a c53 shape for the old row), and the row adds its own fall. Slurred eighth targets have a front 7.0 dB over the body (violins 1.3).

Fix: refit `build/steady_levels54.json` "Violoncellos" on the full c54 stem so that each eighth's body is within 2 dB of the line's shape (the c54 fit was on a range render and the celli offset is 1.5 dB, so the old per-note rows dominate); remove the shape that takes 526.0 to -12.7 dB (find it by the breakpoints 526.21 -5.2 / 526.5 -8.53 / 526.84 -12.7; it looks like the c54 B #1 celli trim) and give 526.0 the finding 1 lift. Accept at eighth-to-eighth steps over 6 dB on at most 1 pair and 526.0 front minus tail at most 6 dB, with the accent at 526 still 2-4 dB over its neighbours.

### 4. Flute 1 115.5: the breath-gap row did nothing; the C6 still covers the first staccato (measured)

Where: Flute 1 main track, qn 115.5 (C6), against "Flute 1 stac" at 116.0.

What is wrong: see the open-items table. The note plays 115.437-116.000 in both parts.json files, as in c53.

Fix: `build/score_config.py`: `NOTE_END_AT["Flute 1"] = {**NOTE_END_AT.get("Flute 1", {}), 115.5: 115.8}` (the table of `tools/score_to_parts.py` line 1150, used for the celli at 534.0), and delete the `BREATH_GAP_AT` row at line 3908. Check in parts.json before building that the note ends at 115.8. Accept when the main track is at least 6 dB under the staccato's peak at +60 ms.

### 5. Join holes that remain (measured; stem and master as in c54's finding 6)

| Track, qn | Stem dip, width under -3 dB | Master dip | Now |
|---|---|---|---|
| Oboe 1 95.0 | 8.0 dB, 132 ms | 2.9 dB | fill of 5 dB in; raise to 8, `hold_s` 0.15 |
| Oboe 1 99.0 | 9.8 dB, 190 ms | 1.2 dB | raise to 8, `hold_s` 0.19 (stem only; low priority) |
| Horn 1 415.0 | 7.3 dB, 69 ms | 3.2 dB | the stem dip halved but the master did not move: the crossover reads +116 ms (c53 +82), so the hole in the master is the late A4, not the level. A timing row for critic C's list rather than more fill |
| Cor anglais 24.0 | 5.9 dB, 172 ms | 4.4 dB | no row yet: `early_fills.json` "Cor anglais" `"24": {"db": 4.5, "pre_s": 0.0, "hold_s": 0.17}`, the form that fixed 26 |
| Oboe 1 109.5 | 10.8 dB (c53 8.3) | not measured | slur-start join, crossover +106 ms |
| Flute 2 639.5 | 10.0 dB (c53 6.4) | not measured | slur-start join; 16-18 dB under the master at 634, so low priority |
| Cor anglais 275.0 | 9.4 dB (c53 3.2) | not measured | came with the Sus-head change; crossover +42 ms as the coordinator lists |
| Violins II 576.0 re-bow | 10.8 dB (c53 4.7) | not measured | refit after finding 1 |

Slur-start joins whose crossover is still more than 80 ms late on this one estimator (for critic C to confirm a second way): Trombone 1 523.0 +122 and 531.0 +90, Horn 1 415.0 +116, Flute 2 633.0 +110, Oboe 1 109.5 +106, Bass clarinet 427.0 +82.

### 6. Slurs inside the theme: a range test to separate them from bow changes (measured state, inferred gain)

Where: the 37 slurred joins of Violins I 56-127 (and the returns), all at velocity 83 with `overlap_s` 0.0.

What is wrong: under question 1. A slurred join and a bow change differ by 1.4 dB of hole and nothing else. EW-TEMPLATE-PLAN section 5 (overlap 45-80 ms on string legato lines) is not applied here: the theme has none.

Test (Violins I 56-72, one range render, two variants against c54 as shipped): (a) `overlap_s` 0.04 for slurred notes; (b) the same plus velocity 60 on slurred targets (in `STEADY_LINE`, a `"slur_vel"` key, or per-onset `at` rows with `"vel": 60`). The row is polyphonic, so an overlap is two notes sounding, not a transition. Adopt a variant only if slurred holes fall to a median of 3 dB or less with none over 6 dB, bow-change holes stay at 5-7 dB, and S keeps robust SD under 10 ms with the slurred-note median within 10 ms of the bow-change median (now +15 against +25 by pcX). If velocity changes the speaking time of the row (not known for the strings' row; on the brass row it sets a filter, p.101), drop (b). Lower priority than findings 1-4.

## Checked and in order (no change needed)

- The eighths of the theme on Sus Marc LITE: sounding share at least 80 % on 45 of 46, front 1.3 dB over the body, no 2-5 kHz front (median bite -1.5 dB over all 79 notes; 90th percentile +4.2, all of it on the accented long notes). Body SD of the eighths 2.5 dB (c53 2.8).
- Same-pitch repeats in the theme (S1): dips of 6-13 dB in the pitch band on Violins I 108, 112.5, 572, Violoncellos 524, 528.5; 60.0 as in question 3.
- Decision 3 (slur heads end 30 ms before the second note): two pitches together for a median 56 ms, was 92.
- Cor anglais 26, Violoncellos 672: fixed.
- Keyswitch placement and monophonic legato rows on all tracks.

Not checked this cycle: tremolo, pizzicato, harp, timpani and percussion technique (no data changed there in c54; c54's report found them in order), the loop fold on held notes, the winds' theme lines note by note, the reference recordings.

## EW-TEMPLATE-PLAN sections this lens touches that are not applied

- Section 5, legato overlap 45-80 ms: none inside the theme (finding 6); elsewhere as c54 (about 20 ms).
- Section 6, "long notes are late-peak swells", and section 8, "long notes keep moving": the theme's long notes do the reverse (finding 1). Section 6's two tracks per string section (a legato track with LegatoSpeed and a KS Master track): not applied; the theme now uses neither legato row.
- Section 7, lean-off of about 2 units after the onset inside slurs: the theme's notes lean off by 6-9 dB from the sample alone.
- Section 8 tutti entry spread and section 10 beat-position velocity: as in c54, not applied.
- MANUAL-GAPS: no new gap tried in c54; #2 (repetition rows) is now moot for the theme's repeats, which separate on the sustain row.

Do not touch: the one-row rule for the theme and its leads (`STEADY_LINE` lead classes, the 58 rows of `steady54.json`, the CC16 resets) and the constant 126 over 56-128 and 504-576; the eighths' levels on Violins I, Violins II and Violas; the repeat handling at 60.0, 108.0 and 572.0 (`rep_lead_s` 0.085, `rep_gap_s` 0.05); decision 3's `head_end_s` 0.03 and `SOST_JOIN_LEAD_S` 0.07; the cor anglais fill at 26 and the celli fill at 672; the Violas' theme notes as a whole; keyswitch placement; the wind staccato rows of bar 30; harp, timpani and percussion rows.

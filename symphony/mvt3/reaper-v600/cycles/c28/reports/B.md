# Cycle 28, critic B (balance and levels), on the c27 render

Measured on the c27 stems and master (`cycles/c27/render/`, K-weighted power in 10 ms frames, score qn mapped through `cycles/c27/parts_rendered.json`'s tempo map), the c26 stems for before/after comparisons, and the c16 / c22 / c27 mp3s for the holistic comparison. "Rel" means a stem's level against the sum of the 31 dry stems in the same window. Scripts were in my scratch folder (deleted).

## Manual notes

MANUAL-READING.md has no row for cycle 28 (the plan ends at cycle 20), so I skipped the page reading and used MANUAL-GAPS.md plus the pages behind my findings.

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| CC7 (Volume) sets a track's level against the other tracks; CC11 shapes the line (May 2021 HO manual p.64, p.151; DIGEST rows CC7 / CC11) | c27 moved every dynamic trim and role carry into CC7 (`dyn_trim_to_cc7`, `ROLE_EDGE_IN_REST`) | Yes, CC7 is the right control. But the role carries put the CC7 change at the wrong time (finding 1). CC7 passage levels are also the right tool for findings 2-4. |
| MANUAL-GAPS "CC7 (p.64, p.151)": CC7 acts before Opus's hall (measured in Movement I: a -12 dB CC7 drop left the hall tail unchanged) | A CC7 change inside a held note does not cut the hall, so it passes S3 | This is why the finding-1 fix can put the carry at the edge itself, inside the note. |
| Velocity sets the loudness of short articulations; long notes are shaped by CC11 (p.64) | Bass clarinet sustains at 1040 / 1044, velocity 109 / 118 | Partly. The 1040 note-on gives a +6.0 dB step while CC11 moves 1 unit, so velocity scales this row's sustain level too (measured). Balance it with CC7, not velocity (finding 3). |
| Brass and the clarinets: CC1 is the dynamic layer and CC11 is volume (p.64; LEARNINGS k 20) | Trumpets 1-2 at 989 / 991 | Yes. A per-note correction belongs in CC11, which keeps the layer (finding 5). |

## Findings, ranked by what a listener on earbuds would hear

### 1. ROLE_EDGE_IN_REST put role levels in the wrong place at the three biggest moments (measured)

**Where:** bar 223 (qn 888-892), bar 263 (1048-1054), the final chord (bars 278-279, qn 1108-1113.5) and bars 40-42 (156-168).

**What is wrong:** when a role edge falls inside a held note and no rest is near, c27's carry moves the envelope edge into a rest. The CC7 ramp that replaces it is centred on the note-on of the sounding note (`tools/score_to_parts.py`, `_edge_fix`, the `role_cc7.append` lines use `on_`), not on the edge. For an edge several qn into a long note, the level change moves back to that note's attack.

`cycles/c27/role_moves_over_1qn.txt` against the notes, with c27 minus c26 on the stem between the note-on and the edge:
- **Final chord.** The final-chord lifts end at 1113.5, after the chord, but are cancelled at the chord's attack (1107.9, 5.6 qn early). Violins I [1107.9, 1113.5, +5] measures -4.8 dB, violas (+4) -3.7, celli (+3) -2.9, Violins II (+2) -1.9, Trumpet 1 [1104, 1113.5, +3] -2.9, Trumpets 2-3 and Trombones 1-2 (+1.5) -1.4..-1.6. Flute 1's -2.5 cut is cancelled the same way: +2.4 dB.
- **Bar 223.** Violins I [892, 899.9, -6] (the printed mf at 892) now falls -6 dB at the fff attack 887.9: -5.5 dB over the arrival bar. Vln I rel at 223 went from -12.0 (c26) to -17.2 dB; upper strings from -8.6 to -10.7.
- **Bar 263.** Trumpet 1 [1032, 1054, +2] ends at the 1048 fff attack instead of 1054. CC7 goes 127 -> 101 over 1047.6-1048.25, -1.8 dB. Trumpet 1 carries the chorale tune, and it now falls 2.5 dB from the last quarter of 262 into 263. This is part of the open "263 step" fault.
- **Bars 40-42.** Flute 1 [168, 176, +5] starts at 155.9, 12.1 qn early: +3.8 dB at the start of its printed decrescendo (156-158).

**Effect at the ending:** the final chord's stem sum fell 1.3 dB. Upper strings rel went from -6.7 to -9.0 and timpani/percussion from -13.1 to -11.8. The timpani are now rank 3 in bars 278-279 (-11.1 rel), the only place in the movement where a roll ranks above 9th. The delivery rides hid the loss in loudness (final still +0.5 over 223) but not in balance. Two items in this lens are hit: the strings and trumpets in the final chord, and timpani / low brass not covering at the ending.

The Movement I c62 warning (a guard moved ramps up to 19 qn) applies here in a new form. The envelope moves are level-neutral, but the audible CC7 change lands 4-12 qn from the edge: Flute 1 168 by 12.1 qn, Violins I 1024 by 8.2, Trumpet 1 1054 by 6.1, the 1113.5 group by 5.6, Violins I 892 by 4.1, Trombones 1020 by 4.15. The Trombones 1020 move happens to land on the printed mf at 1016, which is acceptable.

**Fix in `tools/score_to_parts.py` `_edge_fix`:** in the CC7 carry branch, centre the ramp on `c_ = on_ if abs(e_ - on_) <= 0.5 else e_`. Use a half-width of `max(hw_, 0.5 * (x1_ - x0_))`, so the row's own ramp is kept (for example the 1 qn ramp of Trumpet 1's 1054 row). Add a parameter `ROLE_EDGE_IN_REST["carry_at_edge_qn"] = 0.5`. This stays within Dan's rule: CC7 is instrument-side and acts before the hall (MANUAL-GAPS), and the track envelope still moves only in rests. Expected:
- Violins I at 223 back to about -12 rel.
- Final-chord upper strings back to about -6.7 rel, timpani back to about -13 rel.
- Trumpet 1 +1.8 dB at 263, so the 263 step gains about +0.3 dB on the master.

Then refit the summit rides: the final gains about 1.3 dB before the rides, so the final ride can come down and limiting can drop. Recheck `role_moves_over_1qn.txt`: every carry ramp should now sit within 0.5 qn of its edge.

### 2. Trumpet 1's solo (bars 51-66) is the weakest solo of the movement (measured)

**Where:** qn 200-264.

**What is wrong:** the "solo, dolce cantabile" (p) leads the loudest single accompaniment stem by only +3.8 dB median, p10 -1.4. 72% of its sounding frames are under a 6 dB lead. It leads the whole accompaniment sum by just +0.3 dB. Compare the other solos with the same measure: cor anglais 171-186 +8.6 / +5.6, bassoon 115-122 +6.5 / +4.5, trumpets' theme B 211-216 +9.5 / +4.0.

The main rival is Clarinet 2, printed pp: 818 frames, within 0.2 dB of the solo in bar 57 and 3-4 dB in bars 52, 56, 60 and 64. Next are Clarinet 1 (399 frames), Flute 1 (171) and the basses (104). Clarinet 2 carries a pp soft trim of +7.0 dB (`mix.json`) plus a roles.json row [200, 266, +5.0], about +12 dB of lift. Its pp sounds like p, so the dynamic mapping is inconsistent here. In 500-2000 Hz the trumpet still leads the accompaniment by about 6.5 dB median, so its tone stands out, but in loudness it is level with the clarinets.

**Fix in `build/roles.json`** (existing edges, values only): Clarinet 2 [200, 266] +5.0 -> +1.0, Clarinet 1 [200, 264] -4.0 -> -6.0, Trumpet 1 [200, 264] +3.2 -> +5.2. A level-only simulation on the c27 stems gives +7.8 dB median over the loudest other (p10 +2.3) and +3.9 over the sum. Clarinet 2 stays audible as the inner line Dan asked for: it is still +8 dB over its other pp passages. The passage gets about 1 dB louder, so the 199.95-264 delivery ride (+4.03) can come down by the same amount.

### 3. The bass clarinet is the loudest stem of the tutti in bar 261, and has been since c16 (measured)

**Where:** qn 1040-1048.

**What is wrong:** in bar 261 (ff, crescendo to the fff) the bass clarinet's held A flat 1 is the loudest stem: -8.7 rel, against Trumpet 1 (the chorale tune) -9.9 and Trombone 1 -11.0. It also carries 20% of the master's 30-150 Hz in that bar (-7.1 dB share). The top-three tables show it first or second in bar 261 in c16, c20, c22, c24, c26 and c27.

The cause is a +6.0 dB step at the 1040 note-on (-32.4 -> -26.4 dB). The velocity goes 91 -> 109 while CC11 moves only 110 -> 111, with `dyn_trim_db` ff +3.5 on top. By orchestration norms a single bass clarinet in its low register cannot top a trumpet and trombones at ff (Rimsky-Korsakov's forte equivalents: one trumpet or trombone is worth several woodwinds). The same excess makes it "fall" 2.0 dB into the fff at 263, one of the open 263 faults.

**Fix in `build/score_config.py`:** a CC7 passage level on Bass clarinet of 81 (-4 dB, 20 log10) from 1039.70 to 1047.87. Both edges sit in the existing gaps (the breath 1039.60-1039.90 and 1047.81-1047.94), so no note is touched. Expected: bar 261 Bcl -30.3, 2.8 dB under Trumpet 1. The line still grows through the crescendo (+2 dB from 1038 to 1040), and the fff at 1048 becomes a +2 dB step instead of -2.

### 4. In bars 67-82 the cello counter-melody and the violas are level with the violins' tune (measured)

**Where:** qn 264-328.

**What is wrong:** Violins I+II (F2, printed mf) lead the loudest other stem by only +3.7 dB median, p10 -1.4. 74% of frames are under 6 dB; the rivals are celli (701 frames), violas (572), Horn 1 (251) and harp (141). In bars 71, 72, 74, 76 and 77 the cello/viola/Horn 1 group is louder than the two violin sections together (+0.9..+2.3 dB), and the celli alone are within 1 dB in bars 76-77. The print has violins mf over violas and celli mp. The violins win only above 2 kHz (+6..+16 dB), so the line reads as bright but not as the leader.

**Fix in `build/roles.json`:** Violas [264, 292, 4.0, 2.0] -> 1.0; Violoncellos [264, 292, 5.0, 2.0] -> 3.0; Violins II [264, 328] +3 -> +4. Add Violins I [263.5, 328, +1.0], with its edges in the rests before 264 and after the phrase at 328, which ROLE_EDGE_IN_REST handles. Leave Horn 1's c27 lift (role 7). Simulated on the c27 stems: +5.9 dB median over the loudest other, p10 +0.9. The cello line stays within about 3 dB of the tune, so it is still a counter-melody.

### 5. Trumpets 1-2 at 989 and 991 bulge 7 dB in the Più allegro head (measured)

**Where:** qn 984-998, printed f, a tenuto only on 989.

**What is wrong:** per-note levels, first 0.4 s of each note, Trumpet 1:
- 988 -36.2, 989 -29.6, 991 -28.9, 992 -36.3, 993.5 -33.7.
- 989 is +6.6 dB over its neighbour and 991 is +7.4 over 992. The c26 figures were +4.0 / +5.9.

Trumpet 2 is +3.8 / +2.8. CC1 is flat at 102-104 across these notes, and 989's CC11 bump is only 85 -> 96 (+1.1 dB). So 991's excess comes from its legato target (velocity 118, forced by the c26 `_vc26` row 990.9-991.1) and the c27 CC1 +12 lift (inferred). A tenuto wants 2-3 dB; 991 has no mark at all.

**Fix in `build/score_config.py`** (c27 block, k 20 `cc_scale` rows like the c27 clarinet rows): CC11 -5 dB on Trumpets 1-2 at 991 (990.65-991.66, ramp in over the 0.06 s before the moved note-on) and -3 dB on 989 from +0.4 s to its end (988.95-990.6), so the tenuto's first 0.4 s keep their weight. Target: 989 +2..+3 over 988, 991 within 2 dB of 992, Trumpet 1 per-note range 984-998 under 6 dB (now 7.4).

### 6. Holistic, c27 against c16 and c22: soft passages fixed, but the C-major arrival has lost its contrast (measured on the mp3s)

On the delivered mp3s, levels relative to each file's mean:

**Better:** the soft sections now sit +1.9..+4.4 dB higher than in c16 (relative to each file's mean) and +0.1..+2.6 dB higher than in c22:
- transition 43-50: -8.9 -> -6.9;
- trumpet solo 51-66: -7.5 -> -5.6;
- bassoon solo: -9.5 -> -7.6;
- cor anglais / muted trumpet 171-186: -9.6 -> -5.2.

This is Dan's AirPods request met, with the delivery spec.

**Worse:** bar 223 stands only 3.9 dB over the chorale that follows (224-233). It was 10.4 in c16 and 5.8 in c22. Bar 223 is -4.4 dB against the mean compared with c16 (-1.1 against c22), and 273-277 is -3.1 (-1.2). Two things cause this: the arrival lost Violins I (finding 1), and the c24 chorale ride row 892-901 (+3 dB) lifts the bars right after it. A listener hears the arrival as a step rather than an arrival.

**Fix:** land finding 1 first. Then lower the delivery ride row 892.0-901.0 from +3.0 to +1.0 dB (`build/score_config.py` ride rows) and re-run the delivery loop. Target: 223 at least 6 dB over 224-233 on the mp3, the c22 value. 224-233 are not rival ff / fff bars, so spec items 1-6 are unaffected. Lowering a loud passage slightly raises LRA, and p10 is untouched.

## Other checks in this lens (no change needed)

These checks are measured:
- **Counterstatement 27-34:** the theme in the bass group (bass clarinet, bassoon 1, contrabassoon, horn 3, tuba, violas, celli, basses) leads the flute/violin countersubject by 2-7.6 dB K. The basses are the loudest single stem in 5 of 8 bars.
- **Theme B 211-216:** the trumpets lead the loudest other by +9.5 dB median.
- **Chorale 230-233:** the Violins II / viola tremolo sits 5.8-7.6 dB under the brass. In 226-228 the winds and Violins I lead the brass, as printed (ff over the brass's f).
- **Last chorale 255-264:** the chorale group and the running figure are within ±3 dB, matching their equal printed ff.
- **Low end:** the basses carry 45-70% of 30-150 Hz at every climax. The master's 20-100 Hz share (-12.4 dB) lies between the Brahms references (-7.9 / -8.5) and the Dvořák one (-21.7), so the low end is not boomy.
- **Timpani rolls:** never above rank 9 except 278-279 (see finding 1).
- **Crash cymbals:** they dominate above 5 kHz for about one quarter. At 263 they are the loudest K stem in the first half-quarter (-8.8 rel, against -11.1 at 223 and -11.7 at 278), because the 263 tutti is weak. Leave them: they help the 263 step.
- **Dynamic mapping:** median stem levels at p agree within about 3 dB across families (Tuba and the second parts are softer). Woodwinds rise only 1.3-3.6 dB from f to ff, against brass 4.5-9.1 and strings 2.6-5.3. That is close to the real narrower range of winds, so I am not proposing a change.
- **Other coordinator items** (gate items, stop dryness, Horn 3, bass re-bows, late notes): not measured by B this cycle.

**Do not touch:** trims in CC7 (`dyn_trim_to_cc7`) and ROLE_EDGE_IN_REST plain moves within 1 qn (only the carry's ramp position changes, finding 1); the cor anglais / muted trumpet balance; the theme B trumpet roles; the counterstatement bass balance; the chorale tremolo levels; `TIMP_ARRIVAL_RAMP` and the 1108 roll CC7; the crash and bass drum levels; the room bed at -60 LUFS (Movement I's version, already unified); Horn 1's counter-line role 7 in 67-74; the soft-passage gains and the -14 LUFS delivery stage.

# Cycle 24, critic B (balance and levels), on the c23 render

Measured on `cycles/c23/render` (stems, returns, master), `cycles/c23/scherzo-mockup-c23.mp3` and `cycles/c23/build_render/` (parts.json, roles.json, mix.json, score_config.py). Stems are compared with `cycles/c18/render`. Masters and mp3s are compared with c22. Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Each judgement is marked (m) measured or (i) inferred.

Measures used:
- **Stem level.** Mean of the two channels' powers in 5 ms frames, averaged over a window. Values are dB on a common arbitrary scale.
- **Note-wise masking.** For each note of a line, take the 0.3 s after its moved note-on. In the 1/3-octave band around each of harmonics 1 to 4, compute the line's power against the sum of every other stem and the four returns. Keep the best harmonic, then take the median over the notes in a 2-bar window.
  - A track that doubles the line counts as part of it. c23's actor asked for a pitch test here, so a doubling now needs the same pitch or an octave (not just the same pitch class) at the same onset, on 70 % of the doubler's notes and 50 % of the line's notes. This removes c23's bass clarinet / double basses artefact.
- **Fader guard.** Here the envelope is `vol_db` exactly as written (only the slow class is written; the `shape` and `level` lanes in `vol_cls` are diagnostic only). A note fails when the envelope moves 2 dB or more within 0.5 s at 20 dB/s or faster, anywhere from 60 ms after the moved note-on to the note's end. Timpani are excluded (roll shapes).
- **M.** ffmpeg ebur128 momentary loudness. A bar's value is its median M.

## Manual notes

`loop/MANUAL-READING.md` has no row for c24 (the schedule ends at c20), so I skipped the page reading. I used `loop/MANUAL-GAPS.md` and the manual pages behind findings 3 and 4.

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Sustain Accent: "The MIDI Velocity parameter controls the loudness of the attack. The Mod Wheel controls the loudness of the sustained note" (May 2021 manual p.100) | Flute 1's accented hemiola halves at 300-310 / 902-910 on "Sus Accent MAX" (velocities 70, 70, 90, 90, 90, 90) | Partly. The crescendo is carried by CC11, which the rest map caps at 108, plus a held envelope gain. Velocity, the attack control this row has, is flat over the last four notes (finding 3). |
| Sustain: dynamics follow the controller, and all dynamic layers play at once with one or two audible (p.100) | strings and woodwinds at p (violas 576-588) | Yes. CC11 sets the level here (BRIEF facts). |
| MANUAL-GAPS #8 (Leg Slur Exp / slower legato for cantabile lines) | violas' p line 576-588, whose first note starts a slur from silence on Leg Slur MAX | Not used. Finding 4 proposes a cheaper row change. |
| MANUAL-GAPS #10 (horn portato rows for tenutos) | Horns 1-2's tenuto quarters at 105-120 / 305-320 | Not needed. Their level follows the print (c23 B; unchanged). |

## Answers to the cycle 24 questions

**Per-bar master and mp3 against c22 (m).**
- Master: median 0.00 dB. Bars that moved 1 dB or more:
  - bar 57: -1.5 (celli round robins; c22 read +2.6 there);
  - bars 217 / 218: -1.2 / -1.3 (the Flute 1 trio row);
  - bar 334: -1.1 (the woodwind summit rows).
  Every one of these is an intended change or round-robin noise.
- mp3: median +0.01. Only bar 57 moved (-1.5). Against c18 the mp3 is +0.9 dB (median), with quiet passages +1.4..+2.0.
- Quiet passages on the c23 mp3 (bar-median M):

  | passage (bars) | M |
  |---|---|
  | retransition (89-100) | -21.0 |
  | link (141-152) | -20.0 |
  | development (57-72) | -19.2 |
  | Meno mosso (341-348) | -19.2 |
  | end (364-376) | -18.9 |
  | codetta (225-240) | -18.2 |
  | introduction (1-12) | -18.2 |

  p10 of the bars is -22.2 and the median -16.5. With the -14 LUFS delivery, Dan's "too soft overall" is now a matter for the delivery spec, which is met. What is left from his note is inner lines (finding 4).

**Inner lines through the movement (Dan, 2026-11-17).** I scanned every track window with 3 or more onsets and 2 or more pitches (doublings joined by the pitch test above) (m).
- All the tunes lead, as in c23:
  - Clarinet 1's trio tune;
  - celli 169-184, +13.5 with Violins I;
  - Violins I at 177, +7..+11;
  - Oboe 1 at 185;
  - the counterstatement tune +3.7..+16.9;
  - the solo violin with Flute 1.
- Windows under -6 dB outside the tuttis:
  - the violas' p cresc line of bars 193-196, -6.8, with the line's first notes at -50..-60 (finding 4);
  - the celli's pp line in the solo passage (bars 349-352), -8.3 under the harp;
  - Clarinet 1's mf second-idea syncopations (bar 45), -6.8;
  - Horn 2's f quarters (bar 71), -8.4.
- In the tuttis: Horns 1-2's f tenuto quarters (105-120, 305-320) at -5..-11, the timpani strokes, and Bassoon 1 at bar 333 (-12.8, under the summit row). These follow the print and the norm (c23 B). No change.
- Against c18, more than 3 dB worse:
  - Violas div bars 211-213: -1.7 / -4.2, was +1.3 / -0.4 (bass clarinet row deleted in c22, accepted then);
  - Clarinet 1 bars 49 and 299: -2.5 / -3.0, was +1.7 / +1.4 (accompaniment);
  - Violins I at 177-181: +7..+11, was +12..+15, because Violins II's con sord. arpeggios came up 5-9 dB, which was wanted.

**Role rows by cause.** Three role edges in the 9 slope-guard notes are drawn at a score onset that sits inside a led note: celli 312 / 912 / 362 and violas 197. Two more found below are of the same kind (celli 576, 624). The Harp [672, 711, -3] row ends inside ringing chords. Horn 1 [756, 864, -1.5] and [1020, 1068, -2.5] are still inert (harmless).

**Sub. p at 121 / 277.** Violas at 360 carry a fader step inside the subito note (finding 1).

## Findings, ranked by what a listener would hear

### 1. Dan's no-fader rule is broken in about 67 notes, not 9: the slope guard exempts steps that land inside led notes at printed marks and in hairpin spans (m)

**What I measured.** The written envelope, by my guard above: 67 non-harp notes have a step of 2 dB or more at 20 dB/s or faster inside the sounding note. 160 notes fail with the harp's crescendo ramps and slower moves counted.

**Why `slope17.py` lists only 9.** It skips:
- every printed hairpin's whole span;
- -0.05..+0.3 qn around every printed mark with a CC change of 3 or more;
- the part of each note after the next note-on (legato overlaps).

A step drawn on the score onset of a note that starts 0.1-0.5 qn earlier (a lead or a legato target) is therefore never seen.

**The audible ones, checked on the stems** (step time measured from the moved note-on):

| track, qn | envelope step | when | stem, 80 ms before -> after | cause |
|---|---|---|---|---|
| Violoncellos 576 (bar 193) | +3.3 -> -3.8 dB | +0.00-0.07 s | -34.0 -> -47.7 | role [552, 576, 3.2] -> [576, 612, -3.8]. The edge starts at the moved note-on, so the attack sounds at the old level and the note drops 7 dB. It also cuts the 573 note's tail. |
| Violas 360 (sub. p, bar 121) | +2.7 -> -1.8 | +0.11-0.15 s | -45.9 -> -57.3 | role [312.5, 360, 4] -> [360, 420, -1.8] on the score onset; the note is led 0.53 qn. The subito note starts at the ff level, then the fader cuts it and its hall (S3). |
| 22 wind, brass and string tracks at 1005 (the summit) | 2.5-4.5 | +0.03-0.10 s | Violins II +5.0, Horn 2 +4.9 | ARRIVAL_WEIGHT_AT 1005 (-2 -> +2.5 dB, full by score 1005 + 0.05 s) lands inside every led summit note |
| Violoncellos 624 (trio ff return) | +3.5 -> +0.5 | +0.10-0.14 s | | role [612, 624, 3.2] -> [624, 648, -1.5] |
| Flute 2 903 | 4.6 at 202 dB/s | | | sfp trough row 900-906 edge |
| Horn 1 442 / 651 / 1068 | 5.4 / 5.3 / 4.9 | | | the link solo role end, the trio climb, the motto-tail role [1068, 1080, +3] edge inside the led note |
| Oboe 1 386 / 854 | 5.1 / 5.1 | | | role [386.8, 393, -4.5] / [854.8, 861, -4.5] edges |
| Clarinet 1 900 | 5.0 | | | the sfp |

The full list is reproducible with the guard described above.

**Fix.**
1. `cycles/c17/actor_scripts/slope17.py` (or its successor):
   - anchor the mark zone on each track's moved note-on of the note at the mark (that is, moved note-on -0.02..+0.04 s), not on score qn -0.05..+0.3;
   - exempt hairpin spans only for moves at 6 dB/s or slower;
   - check the overlap of legato notes too.
   Report its count beside this one.
2. `tools/score_to_parts.py`, `ROLE_EDGE_MOVED`: when an edge would land inside a led note with no rest before it, draw it as a ramp over the preceding printed hairpin, if there is one, at 3 dB/s or less. Otherwise convert it to `CC11_ADD_SPANS` with the step at that note's moved note-on (pre-hall).
   - Celli 576: the print has decresc 573-576 into p. Use roles [552, 573, 3.2], [573, 575.85, 3.2, -3.8], [575.85, 612, -3.8], a ramp over 0.75 s inside the printed decrescendo.
   - Violas 360: end [312.5, 360, 4] at 359.45, so its fall sits in the 0.15 qn rest before the moved note-on (the CC11 drop 106 -> 51 at 359.462 already makes the subito). Start [360, 420, -1.8] at 359.45.
   - Celli 624: [612, 623.3, 3.2], [623.3, 623.6, 3.2, -1.5] (in the rest after the 621 note), [623.6, 648, -1.5].
3. `ARRIVAL_WEIGHT_AT`: draw the +2.5 dB step on each track so that it is full at that track's moved note-on of the arrival note. Start it 0.03 s earlier, in the last moments of the note before. This needs a new option, e.g. `ARRIVAL_WEIGHT_MOVED = True`. The -2 dB hold-back ramp stays as it is.

**Expected (i).** No step inside a sounding note at 576, 360, 624 or 1005. The celli at 576 keep a p attack instead of a 7 dB sag. The violas' subito keeps the ff tail under the p.

### 2. The 9 slope-guard notes of c23: an instrument-side or ramped replacement for each (m: causes from the written envelope; i: expected results)

| track, qn | cause (measured in vol_db / vol_cls) | replacement |
|---|---|---|
| Violoncellos 312 (note from 310.64) and 912 (910.61) | role +4.5 starts at 312 / 912 over 0.25 qn: 3.0 -> 7.3 dB in 0.06 s, 0.31 s into the tied G3. The crescendo gain (+3) is already held there. | Ride the printed crescendo: `roles.json` Violoncellos [298, 310.6, 0, 4.5], [310.6, 360, 4.5] and [898, 910.6, 0, 4.5], [910.6, 960, 4.5], replacing [312, 360, 4.5] / [912, 960, 4.5]. With the +3 hairpin gain that is 2.9 dB/s at most, under the guard. The arrival level is the same 7.3 dB. |
| Violoncellos 362 (361.47) | role [362, 396, -4] edge on the score onset of a legato target led 0.53 qn | Delete the row. Add `CC11_ADD_SPANS` Violoncellos [(361.45, 396, -9, -9)]: at CC11 37-41 the strings give about 0.4-0.5 dB per unit, so -9 is about -4 dB. The step is at the legato transition, before the hall. |
| Horn 2 1005 (1004.76), Oboe 1 1005 (1004.83) | ARRIVAL_WEIGHT_AT 1005 (finding 1); for Oboe 1 also the 1002-1005 crescendo gain arriving inside the note | `ARRIVAL_WEIGHT_MOVED` (finding 1). This fixes the other 20 tracks at 1005 too. |
| Horn 3 936 (935.78) and 953 (952.74); also 350 / 353 in the first tutti, +2.9 / +4.5 dB, not on the c23 list | `slow:uni_role` (`UNI_BOOST_AS_ROLE`, score_to_parts.py near line 6523): Horn 3 carries +3 dB while Horn 4's unison is dropped. The edges are fixed 0.4 qn before / 0.5 qn after the run, so they fall inside Horn 3's tied and slurred notes. | Generic, in that block: snap the rise to end at the run's first moved note-on, starting no earlier than the previous note's end. Snap the fall into the rest after the run's last note. Where the next note is tied or slurred with no rest, ramp at 3 dB/s or less across it. |
| Harp 708 (chords ringing from 702-708 to about 717) | role [672, 711, -3] releases over 711.125-711.5 inside the ringing chords | The harp's next note is at 1020. Make it [672, 1019, -3]: the release then falls in the rest. |
| Violas 197 (196.74) | role [192, 198, 3.5] end drawn over 197.0-197.12, inside the pp slur head led 0.26 qn | Delete the row. Add `CC11_ADD_SPANS` Violas [(191.4, 196.7, 8, 8)] (CC11 32-48 there: about +3.5 dB). It returns at 197's moved note-on, a fresh slur head, before the hall. |

### 3. Flute 1 into bars 105 / 305: the first ff note juts out because the +4 dB crescendo gain is held through it and released after it, and CC11 falls into the arrival (m)

**Print.** Bars 101-104: the hemiola half notes in unison with Violins I (B5 A5 F#5 D#6 B5 A5), f < ff at 312. At 912 the same, after the sfp.

**Measured** (parts.json and stems).
- `vol_db` holds +4.0 dB from 310 to 311.85. It then falls to -1.8 at 313: the gain plus role [312, 360, -1.8] together, 5.8 dB in 0.26 s (22 dB/s), across the first ff quarter (moved note-on 311.912). At 912 it falls from +3.65 to 0 over 912.09-913. `keep_rel_db_s` 2.8 is not honoured at this arrival.
- First ff quarter E6 against the identical E6 two notes later (same velocity 112, same row): 312 -22.2 vs 314 -30.6 (+8.4 dB); 912 -23.7 vs 914 -28.7 (+5.0).
- Flute 1 minus Violins I: at the A5 before the arrival -8.6 dB; on the arrival quarter +5.1 (312) and +3.1 (912); two notes later -3.3 / -1.6.
- The crescendo itself: stem body 300 -40.4, 302 -39.0, 304 -39.6, 306 -31.8, 308 -33.6, 310 -34.3. It peaks on the D sharp 6 and falls 2.5 dB into the arrival as the line descends.
- CC11 is written 108 at 308.75, then 107, 106, 105, 104, **102 at 311.75**. The c23 `C23_FHP` add of up to +20 is applied before `CC11_REST_MAP` (127 -> 108), so its rise is lost, while its return to 0 over 311.3-311.75 survives as a fall under the last A5.

**Fix.**
1. `build/score_config.py`: set `C23_FHP` to "0" (remove the inert ramp; it writes a decrescendo into the arrival).
2. `HP_GAIN_TO_CC11["Flute 1"]`: add `"drop_always": [310.0, 910.0]`, so no envelope gain is held into the arrival.
3. Carry the crescendo with the control this row has for it (manual p.100, velocity = attack loudness):
   - `VEL_SET` Flute 1 {300: 70, 302: 76, 304: 82, 306: 88, 308: 94, 310: 100};
   - {902: 70, 904: 78, 906: 86, 908: 94, 910: 100}, leaving the sfp at 900 untouched.
   With the c23 overlay row at -1.5 dB, check each half note against the note before: +3 dB at most (Dan's accent cap).

**Expected (i).**
- 312 / 912 E6 about 4 dB lower: level with 314 / 914 and about -1..+1 dB against Violins I.
- The crescendo heard as growing attacks into the arrival rather than as a step after it.
- Nothing changes for Violins I, so the bar 23 figure check is unaffected.

### 4. Violas' p cresc line, bars 193-196 (qn 576-588), is hidden: its first notes are 6-14 dB under the celli and basses, which print the same p (m)

**Print.**
- At 576 violas, celli, basses (arco), Violins I, Clarinets 1-2 and Bassoon 1 are all p < f into bar 197 (Clarinet 1, Violins II and violas espress. f).
- The violas have the only moving line: A3 (quarter) and the slurred eighths B3 A3 G#3 A3 into a held A3; then B3, C#4 B3 A3 B3 into a held B3.

**Measured.**
- Violas' note levels (first 0.25 s): 576 **-59.7**, eighths -51.0 / -49.4 / -53.4 / -54.7, held A3 -50.0; second phrase 582 -38.3, eighths -45.6..-52.6, held -44.5.
- Bar 193 stem levels: violas -53, celli -46, basses -45, Clarinet 1 -42, Violins I -47.
- Note-wise masking median -6.8 dB (p25 -9.3), with the celli the loudest masker.
- Identical in c18 (the data has not changed).

**Cause.**
- The first note starts the slur from silence on "Leg Slur MAX". Its first-note layer speaks slowly at CC11 46: the same note at the second phrase's CC11 59 reads 21 dB louder.
- The eighths are 0.13 s long at CC11 47-52.

**Fix** (`build/score_config.py`):
- `ART_AT["Violas"][576.0] = "Sus MAX"` (the row is loaded; it is the row of the eighths after it).
- `CC11_ADD_SPANS["Violas"] += [(575.4, 588.0, 8, 8)]`: +3.5..+4 dB at CC11 46-70, and the brighter layer the line needs.
- Keep Violoncellos [576, 612, -3.8] with the ramp of finding 1.

**Expected (i).** The line's first notes come up 6-10 dB, to about the celli's level, and the median masking reaches about -2 dB. Measure the violas against the celli per note at 576-588 after the build.

### 5. Smaller hidden inner material (m; fixes i)

- **Celli pp line, bars 349-352** (E3 G#3 G#3 E3 A3 G#3 F#3 under the solo violin): -8.3 dB median, p25 -12.3, under the harp's chords in its own bands. Stem levels: celli -47..-50, harp -53..-68.
  - Fix: `VEL_CAP_SPANS` Harp (1040, 1068, 45), the instrument-side route used at 216-264 in c04. Do not add a role row.
- **Violas div, bars 211-213**: -1.7 / -4.2, 3-4 dB worse than c18 since the bass clarinet's row was deleted. They are accompaniment (div. thirds under the ff tune).
  - Fix: if wanted, `CC11_ADD_SPANS` Violas div [(629.5, 648, 6, 6)] rather than a fader row.
- **Clarinet 1, bar 49 and bar 299**: -2.5 / -3.0, 4.3-4.4 dB worse than c18. Accompaniment, within norm. No change.

### 6. Delivery and section balance (m): no fault to fix

- The delivered file meets the shared spec as c23 reported: -14.0 LUFS, -1.4 dBTP, summit +0.64 LU, f -> ff +2.2, p10 -20.2, LRA 10.5.
- The per-bar master moved only where c23 intended (above).
- If finding 1's arrival-weight change lowers the summit downbeat's first 50 ms on the led tracks, recheck spec item 2 (summit lead 0.5 LU or more over bar 318). The step still arrives at each note-on, so the change should be under 0.1 LU (i).

## Do not touch

- The c22 / c23 bar 23 and bar 38 / 263 states (nothing above changes Violins I).
- The woodwind summit rows from 996, with celli / Horn 1 at 1004.75.
- Flute 1 [648, 660, -4] and the flute accent overlay (-1.5 dB, G6 -2 dB).
- The c22 inner-line rows: Clarinets 1-2 over 37-43, the coda Violins II / violas, Horn 4.
- The con sord. Violins II lift (now +5..+9 dB over c18).
- The delivery chain with the room-noise bed and its ride rows.

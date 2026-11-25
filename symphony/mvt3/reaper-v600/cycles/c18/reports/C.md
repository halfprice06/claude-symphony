# Critic C, cycle 18 (dynamics over time), on the c17 render

Lens: hairpins and phrase shapes, the loudness arc against the score, loudness range of the master and the mp3, swells and loop pulsing, decays, the final chord. Measured on `cycles/c17/render/` (36 stems, `00_Master.wav`), `mvt3-mockup-c17.mp3`, the c16 stems for comparison, and `build/parts.json` (tempo map, notes, CC lanes, `vol_db`). Methods: BS.1770 K-weighted level per quarter and per bar (master c17, master c16, mp3); 10 ms power envelopes of every stem; ffmpeg ebur128; printed marks from `build/mockup-events.tsv`. Read: BRIEF, README, HISTORY, c17 CHANGES, FINDINGS Parts 1-6 (sections 6-11, 16-17, 21-22 in full), EW-TEMPLATE-PLAN, the c14 dynamics report, MANUAL-GAPS. Every number below is measured unless marked inferred.

## Manual notes (third round, own pages: May 2021 HO manual PDF p.91-92, 101-103; MANUAL-GAPS.md read)

| Manual (PDF page) | What it says | Where in this mockup | Does the c17 render follow it? |
|---|---|---|---|
| p.101 | Brass "Sustain Accent": velocity sets the loudness of the attack, the Mod Wheel (CC1) the loudness of the sustained note. | The sfp of bar 149 (qn 592) on horns, Trumpet 3, trombones, tuba. | No. The note is on the plain sustain at the resting ff controller values with no bump; the sf is 1.1 dB under the ff before it (finding 2). MANUAL-GAPS line 318 lists the row as not tried (memory). The controller route in finding 2 needs no new row. |
| p.101 | "Sustain Marcato Long / Short": a marcato attack weaker than Sustain Accent; velocity sets a low-pass filter on the attack (soft velocity = darker). | Brass accents; the sf head. | Not used (c17: accents are CC bumps). After Dan's "a little bit over done", no accent row should be added (finding 1). |
| p.91-92 | Strings "Marcato Sustain" adds a marcato sample to the sustain for "extra power at the start of the note". | String sf at 592. | Not used; Movement I measured it 2-8 dB louder with a 2-5 kHz burst (MANUAL-GAPS line 43). Keep it out; use CC11. |
| p.91 | String Sustain: looped, and a round robin that alternates up-bow and down-bow samples, so each new note is a new bow stroke. | The pedal C of bars 229-234 (celli, basses re-attack C on every bar line) and the downbeat of bar 222. | It behaves as described, and that is the fault: every string and brass part starts a new slow sustain sample within the same 30 ms (finding 3). The score prints "change bow at will" for celli and basses at qn 892. |
| p.101 | Brass sustains: four dynamic layers on CC1, so a held note can grow or fall. | Chorale 892-936, final chord. | Yes. Final chord stems hold within 1-3 dB over 2.1 s; crescendo rolls and held brass grow with the lane. |
| p.103 | "Sforzando Crescendo" only on Solo Horn and Solo Tuba. | sfp < ff, bar 149. | Not available for the sections. Closed. |

## State through this lens

- Master -20.1 LUFS, LRA 23.2 LU, true peak -1.0 dBFS. mp3 LRA 15.0 LU (low -30.5, high -15.5), true peak -1.5. Delivery gain (mp3 minus master, K-weighted per bar) is flat where it must be: bars 42-50 +10.0 dB on every bar, 51-66 +11.8 to +12.4, 114-126 +11.8 to +12.1, 170-186 +10.4 to +10.7. No swell under static soft music (the c14 fault is gone). Climaxes in the mp3: bar 278 -9.9, bar 223 -10.8, bar 262 -13.4, bars 1 / 5 -14.9 / -14.6, bars 147-150 -15.4 to -15.8. Order correct.
- Crescendos, K-weighted per quarter: 107-110, 135-147, 197-199, 209-211, 219-223, 243-247, 255-263 all rise without a reversal over 2 dB, except the downbeat of bar 222 (finding 3). 169 held crescendo arrivals checked on the stems (level 0.1-0.4 s against 0.7-1.2 s after the note-on): none gives back 3 dB or more except the final-chord harp and two clarinet notes. The Scherzo's "arrivals give back 6-7.5 dB" does not apply here.
- Timpani rolls (item 5): 19 rolls measured in 0.5 s windows. Every roll is 3.2 dB or more under the loudest other stem in every window; rolls without a hairpin settle (920-933: -36.0 to -41.4 dBFS in 2 s; 600-607: -34.1 to -40.5); crescendo rolls grow with the texture (876-888: -47.2 to -25.5). The Scherzo's "flat-CC1 rolls fall 16-19 dB within the bar" does not apply: the held ff roll 584-592 stays within -33.0 to -35.0.
- Loop pulsing (item 7): no string note sounds longer than 5.5 s. The 11 longer notes are percussion rings, timpani rolls with hairpins, Horn 4 at 168 (6.5 s), Horn 2 at 152, Contrabassoon at 568, Clarinet 2 at 184. None shows a positive 3.95 s autocorrelation in both the 100-300 Hz level and the centroid. No finding.
- Final chord: master -9.8 to -13.1 dBFS over the 2.08 s of the chord, stems within 1-3 dB; after the release -20 dB at 0.41 s, -40 at 0.85 s, -60 at 1.25 s, smooth to -84. Unchanged from c16. Nothing to change.

## Findings

### 1. Accents (Dan: "a little bit over done now"): the c17 bump adds 1.7-1.9 dB to each accented note and doubles the share of accents standing 5 dB out of the line. Halve it

**Measured (733 accented notes on 27 tracks; level of the first 0.3 s against the mean of the unaccented neighbours within 3 notes at the same printed dynamic; c16 with the same windows):**

| family | excess c16, median (over 3 dB / over 5 dB) | excess c17 | accented note c17 minus c16, median / p90 | plain neighbours c17 minus c16 |
|---|---|---|---|---|
| woodwinds (276) | +0.4 (25 % / 16 %) | +2.4 (44 % / 25 %) | +1.7 / +2.5 | 0.0 |
| brass (202) | +1.2 (31 % / 12 %) | +3.0 (49 % / 23 %) | +1.7 / +2.8 | 0.0 |
| strings (255) | +0.4 (20 % / 7 %) | +2.6 (47 % / 20 %) | +1.9 / +3.4 | -0.2 |

On the master, at the 40 onsets where 8 or more tracks carry an accent, the first 0.25 s stands +2.2 dB over the surrounding 3 s (c16 +1.1); those windows rose a median 1.7 dB (p90 2.4) while the phrase bodies rose 0.4 dB.

**Where the accents break a line:**
- Bars 91-94 (qn 360-376, 21-25 tracks accent every half bar): master accent over the phrase +6.2 at 360, +3.8 at 362, +3.8 at 364, +3.4 at 366, +3.2 at 369, +3.8 at 371, +4.3 at 372. The passage is all accents, so the bump raises the section (+1.3 to +1.7 dB per bar over c16) and each chord front. This is the "+1.4 dB in 83-98" of CHANGES.
- Bar 26 (qn 100) +4.3 (c16 +1.0); bar 99 (qn 392) +7.8 (c16 +5.8); bars 204 (qn 812, 813) +3.2 / +4.1 (c16 +1.2 / +2.3); bar 147 (qn 584) +2.9 (c16 +1.0); bars 2 / 6 (qn 4, 20) +2.5 / +2.1.
- Single lines, accent over neighbours: Violins I qn 38 (bar 10) +9.3; Violoncellos qn 15 (bar 4) +8.9; Violas qn 366 +9.3 and 356 +8.6; Tuba 360-366 +8.6 to +9.7 (ff median +7.2, 14 notes); Flute 1 qn 360 +11.3, 584 +11.1, 628 +9.3, 806 +10.5, 998 +14.1; Oboe 1 qn 358 +14.4, 612 +10.9, 644 +11.3, 801 +11.8; Trumpet 3 median +4.6 (17 of 36 over +5). Part of each of these was there in c16 (register, a long accented note beside a short pickup); the bump added 1.2-2.3 dB on top.
- Timbre: the 2-5 kHz share of the first 80 ms against the body at the tutti accents is -0.5 dB median, p90 +1.5 (c16 -0.8 / +1.6). The accents are weight, not bite. The fault is amount only.

**Did the lower resting CC11 flatten ff against f?** No. Plain ff notes are within 0.2 dB of c16 (table), and the median ff-minus-f distance of the stems (`metrics.md` medians) moved +0.1 dB (c16 to c17: Violins I 2.9 -> 2.4, Violins II 4.0 -> 3.4, Horn 1 7.5 -> 10.0, Trumpet 2 5.2 -> 7.0, Trombone 1 3.3 -> 4.7). Keep `rest_map` and the make-ups.

**Fix (`build/score_config.py`, `_C17_ACC`), about half the c17 amount:**
- strings: `amt [(46, 4), (72, 5), (88, 8), (114, 10)]`, `max` 116 (was 8 / 10 / 16 / 19, max 124);
- woodwinds: `amt [(34, 1), (46, 3), (72, 5), (88, 7), (114, 10)]`, `max` 116 (was 2 / 5 / 10 / 14 / 20);
- brass and clarinets: `amt_rel` 0.21 -> 0.10, CC1 part +5 -> +2 (horns +7 -> +3, clarinets +6 -> +3); Horn 1 0.16 -> 0.08; trumpets 0.13 -> 0.06, CC1 +3 -> +1;
- Tuba and Trumpet 3 `amt_rel` 0.05 (their c16 excess was already +2.4 / +3.7);
- a cap: where an accented note's resting value plus bump would put it more than 12 units over the previous note's value on the same row, clip the bump to 12 (new key `max_step`), so no accent adds more than about 1.5 dB.
- Do not extend any amount to the oboes, Horn 3, Trumpet 2 or the basses.

**Expected:** accented notes +0.8 to +1.0 dB over c16 instead of +1.7 to +1.9; stem medians about +1.3 to +2.1 dB over neighbours; master tutti accents about +1.6 dB over the phrase; bars 91-94 back within 0.7 dB of c16. **Targets:** median +1.5 to +2 dB per family, share over +5 dB back at the c16 values (16 / 12 / 7 %), no tutti accent window more than 1.0 dB over its c16 level.

### 2. The sfp of bar 149 has no sforzando, and the strings now reach the printed ff of bar 150 half a second late

**Where:** qn 592-600, every staff with the mark (all but Trumpets 1-2, who keep their accented ff half notes).

**Measured, master in 0.1 s steps from qn 592 (t = 0):** before -13.6 dBFS; -0.1 s -17.4; 0 to 0.3 s -16.8, -16.4, -14.7; then -20.1, -23.3, -23.8, -26.1 (0.6 s); -22.5, -21.3, -18.8, -18.5, -18.1, -16.7, -16.1, -15.2, -13.8 (1.5 s = qn 596). The sf peaks 1.1 dB under the ff that precedes it, after a 3.8 dB hole. Stems, first 0.2 s of the sf against their own level before: Violins I -28.6 / -31.1 against -25.3; Violas -31.3 against -26; Double basses -31 to -33 against -24; Horn 1 -31.0 / -31.5 against -27; Trombone 1 -29.6 / -29.9 against -24.7; Timpani level. Only Trombone 2 (+1.5) reaches its former level.

**Cause:** the sf note starts at the resting controller values (CC11 103-105 strings, 100 brass, CC1 98-108) with no bump; the fall begins at 592.38. The front that made the sf in c15 was a per-note fader shape and went with Dan's rule. The printed sfp is a dynamic, not an accent script, so `INSTR_POST["accent"]` skips it.

**Second fault (c17 regression):** `cc_cap` holds the upper strings at CC11 52-54 until 594.5 and reaches 106 only at 597.5. At the printed ff (qn 596) Violins I stand at CC11 80. Stems at 596 (c16 in brackets): Violins I -27.9 (-23.2), Violas -31.1, Violoncellos -28.6 (-19.8); the strings reach their ff level at +2.1 to +2.3 s instead of +1.5 s. Master bar 149 -1.2 dB and bar 150 -0.6 dB against c16; master at 596 -13.8 (c16 -11.8). The print is sfp with a hairpin from 592 to ff at 596, so the p is a moment, not a held level.

The p itself is right: floor 12.5 dB under the ff on the master; strings 14-19 dB, brass 12-20, timpani 13, woodwinds 8-11 under their own ff. The Movement II fault (sf > p swelling 5-11 dB once the envelope half is gone) does not occur.

**Fix (`build/score_config.py`, `INSTR_POST`):**
1. `cc_shape` at 592.0 on every sfp track, lane cc11: `pts [(-0.03, +A), (0.16, +A), (0.22, 0)]` measured from the moved note-on, A = +12 strings (to about 116), +10 woodwinds, +12 brass and clarinets with a CC1 part of +4 from 0.08 s before. Shift the start of the existing fall from 592.38 to 592.6 (0.2 s after the note-on) so the bump is not cut.
2. `cc_cap` on the four upper string tracks: `pts [(592.9, 52), (593.6, 58), (595.0, 86), (596.0, 105)]`; remove the points at 597.5 and 600.
3. Leave the woodwind fall for now (it is a printed fp shape in the fader and falls at 15-18 dB/s; see finding 4 for moving it to CC11).

**Targets:** master 0-0.2 s after 592 at or above -13.6 dBFS and under -11.5; no 0.1 s window in 592.0-592.6 under -16; floor between -24 and -27; master at 596 within 1 dB of -12; Violins I at 596 at or above -24.5.

### 3. Holes where every sustaining part starts a new note at the same instant: the downbeat of bar 222 (7 dB for 0.3 s) and the chorale's bar lines (3.5-4.3 dB)

**Bar 222 (qn 884), measured, master in 50 ms steps:** -14.0 at -0.2 s, -18.4 at -0.1 s, -21.0, -21.6, -20.6, -20.8, -20.9, -20.7 from 0 to +0.3 s, -19.2 at +0.4 s, -17.8 at +0.6 s, -15.5 at +0.7 s. c16 is the same within 0.6 dB. This is the last bar of the p < mp < f < fff build into the C-major arrival; the printed f at 884 arrives as a 7 dB drop. Stems: Violins I -24.2 -> -37.0; Violins II -19.6 -> -34.3; Violoncellos -19.4 -> -32.8 and still -28 at +0.7 s; Trumpet 1 and Horn 1 enter at -48 / -40 and need 0.6 s to reach -31. The c15 fix was per-note fronts in the fader, removed in c16.

**Chorale, master dip in the 0.45 s around each bar line (lowest 30 ms frame against the 0.3 s before):** 904 -4.3, 908 -3.6, 912 -3.5, 916 -3.6, 920 -1.8, 924 -4.3, 928 -2.3, 932 -1.8 dB (c16 -3.2, -3.5, -3.5, -3.2, -2.4, -5.1, -2.6, -3.3). At each bar line the dips fall within the same 50 ms on every stem: Trombone 1 -3 to -8 dB, Trumpet 1 -5 to -10, Tuba -2 to -6, Violoncellos -6 to -10, Double basses -3 to -8, Flute 1 -8 to -17, Clarinet 1 -8 to -13, Timpani -6.6 at 916 and 920.

**Cause:** the slow start of each new sustain sample (CHANGES and Movement I agree). `rebow_join`'s 8-unit swell cannot fill it. What makes it audible is that nothing holds through: c17 put the celli's and basses' pedal C bow changes on the bar lines (ruling 7), where the brass breathe and the woodwinds re-tongue. The score prints "change bow at will" for both at 892.

**Fix (notes and gaps only):**
1. Celli and basses 912-936: one tied C per track again (the `STR_REP_NEW_BOW` skip of c01 back for the celli from 912), re-bows placed by `tools/space_rebows.py` away from the bar lines: celli at qn 914, 918, 922, 926, 930; basses at 913, 917, 921, 925, 929, 933 (each 2.1 s, under the 3.95 s loop). Keep `rebow_join` (5 ms gap, swell 8) on those joins. The low strings then cover every bar line, and the brass cover each bow change.
2. Woodwinds 900-936, whole-note and longer joins: `INSTR_POST["gap_set"]["wind"] = [{"from": 900.0, "to": 936.5, "min_qn": 3.0, "gap_s": 0.03}]`; Flute 2 and Clarinet 2 take the breath half a beat late (their previous note 0.5 qn longer; a new per-track `shift_qn` in the same row), so the pair never gaps together.
3. Timpani roll 920-933: no re-strike at the bar lines (check the roll is one note; the -6.6 dB at 916 and 920 are the stroke-to-roll joins: start the roll's keyswitch and note 0.03 s before the stroke's end).
4. Bar 222: Violins II and Violas hold their bar-221 note 0.12 s over the bar line (`note_end` with a negative `early_s`, or the existing overlap rule), and the new note's note-on leads by 0.12 s (`entry_leads.json`, qn 884.0, Violins I, Violins II, Violas, Violoncellos: 0.12; Trumpet 1 and Horn 1: 0.15 with CC1 at the f value from the note-on instead of mf). Violoncellos: the D3 at 884 on the same row as the G2 before it with `rebow_join`-style 5 ms gap.

**Targets:** master dip at the chorale's bar lines 2 dB or less; master 884.0-884.6 never more than 3 dB under the mean of 883-884; master per quarter non-decreasing from 880 to 888 within 1 dB (now -16.5, -19.6, -15.8).

### 4. Fader audit under Dan's rule: 81 moves faster than 3 dB/s still act inside single notes, and one fitted bar row reverses a printed diminuendo

**Method:** every `vol_db` segment of 1 dB or more steeper than 3 dB/s, merged into moves, kept when it lies inside a sounding note at least 60 ms from both ends and totals 2 dB or more. 117 moves; 36 belong to the printed sfp (592-600) and fp (832-834). The other 81:

| class | n | examples (track, qn) | what to do |
|---|---|---|---|
| level step between printed dynamics, 3-5 dB falling over 0.2-0.4 s from 0.06-0.3 s after the note-on (the note starts hot, then drops) | 40 | Bassoon 2 at 40 (f -> mf, +3 -> 0), 332, 440, 580, 796 (8.2 -> 3.0), 840; Bassoon 1 332, 360, 578, 794 (5.2 -> 0), 892; Oboe 1 330, 793; Horn 1 300 (4 -> 0); Horns 1-2, Trumpets 1-2 at 892 (3 dB in 0.26 s); Trombones 1-2 at 1016 | finish the move 0.03 s before the moved note-on (`dyn_step_on` currently skips these: they are ramps, not jumps; give the trim ramps the same anchor) |
| entry ramp ending inside the note | 15 | Violoncellos 264 (+4.0 in 0.22 s), 488 (+4.5); Double basses 488 (+5.0), 744 (+4.0); Violas 264, 816; Violins II 744, 935 (+9.7 dB in 0.48 s, the edge of the 888-936 stem-fix row); Flute 1 964 | same anchor; Violins II 935 goes with the row (below) |
| release of hairpin gain in a note's last 0.45 s | 12 | Violins I / II 295, 775; Violoncellos 383, 967; Violas 931; Flute 1 168, 320 (+7.0 in 0.34 s) | start the release at the next note-on, or spread it over the whole last note (under 3 dB/s) |
| mid-note | 8 | six woodwinds at 1052 (-2 dB in 0.17 s); Contrabassoon 578; Harp 511 | stretch to 3 dB/s |
| instant 3 dB step at the score onset, 60-70 ms into a led note | 6 | Flute 2 914, 932; Oboe 1 932; Violas 384; Double basses 384, 968 | Movement I c58 (2) still applies here: key to the moved note-on |

`stepcheck.py` reads 0 because it tests 2 dB within 60 ms; these are 10-30 dB/s over 0.1-0.4 s. Envelope density: strings 2.3-2.8 points/s, but 85 % of the points lie on straight ramps (greedy 0.1 dB thinning leaves 0.32-0.40 points/s), so the count is a writing matter, not movement.

**Fitted rows (`build/roles.json`, 267 rows), by cause:**
- Bar means of removed shapes, delete: Trumpet 1 [680,684,0], [684,688,-1], [688,692,2], [692,696,5], [712,716,1.5], [716,724,0], [724,728,-6.5], [728,732,3.5]. Measured on the stem with the envelope taken out, the muted line is a clean diminuendo at 724-728: -39.0, -43.1, -46.0, -47.6, then -51.9 at 728. With the rows it is -44.5, -49.0, -52.5, -54.1, then -48.4: the p arrival at 728 is 5.7 dB louder than the note before it, with fader steps of 3.9 dB at 724 and 6.0 dB at 728 (72 and 109 dB/s). Replace by CC1 on "Mute Sus" (0.8 dB per unit, c17): CC1 at 720 / 723 / 724 / 725 / 726 / 727 57 / 59 / 58 / 54 / 51 / 47 (was 57 / 61 / 64 / 58 / 54 / 47), 728 unchanged at 35; pitches 67 and 68 +4 units in the `note_cc` pitch table in place of the +2 / +5 rows.
- Sample or row level, move to the instrument: Violins II [888,936,-7] and Violins I / II / Violas [1088,1116,-7.5 / -8.5 / -4] (tremolo and divisi chord levels: `row_volume_db` "Tremolo" and a chord-size CC11 offset in `note_cc`, as ruling 9 asked); Double basses [792,840,-4], [984,1080,-2] (short-row level: `row_volume_db` "Stac On Bow RRx9" -3).
- Mapping of the one-row spans, move to CC11 in `steady_levels.json`: the four upper strings' [40,104], [600,680], [792,816], [984,1056] rows (-5.0 to +2.0 dB).
- sfp / fp / sub. p level rows (16 rows [593,596], 12 rows [833.25,839], 10 rows [871.7,878]): these are the p halves of printed subito marks and act for 1-2 s under one held note. They break S3 (a fall in the fader cuts the hall). Move each to a CC11 offset over the same span at 0.6 dB per unit (woodwinds: Flute 1 / 2 -12 dB -> the lane to its floor plus CC7 for the rest; clarinets and bassoons -5.5 to -9 dB -> -9 to -15 units).
- Real phrase decisions, keep: the role rows of 4 bars or more (counter-melodies 264-300, solo levels 200-264 and 680-744, bass-line doublings with a 4 qn ramp, the chorale balance rows 892-928, 1016-1048, the final chord rows).

### 5. The f of the introduction's turn figure fell 2-3 dB while the ff chords rose 3-5 dB, and one printed level now spans 9-13 dB in two places

**Bars 1-6, strings (measured, c17 minus c16):** chord of bars 1-2 and 5-6 (qn 0-5, 16-21): Violins I +3.3, Violins II +2.8, Violas +1.3, Violoncellos +4.4 to +4.7, Timpani +3.9, horns +0.8 to +2.2. Figure of bars 3-4 (qn 8.8-16, printed f): Violins I -0.7 overall and -2.0 to -3.3 per quarter over 9-13, Violins II -0.7, Violoncellos -1.7 (-2.3 to -3.8 per quarter). Master bar 1 +1.2, bar 2 +2.6, bar 3 -2.4. Bar 1 to bar 3 is now 17.7 dB (c16 14.2); on Violins I the step from the ff chord body (-25.8) to the f figure (-37.3 over 9-13) is 11.5 dB (c16 5.6).

**Cause:** the ff make-up (+1.3 dB on the string tracks) was fitted on legato lines. On "Sus MAX" chords CC11 114 -> 103 costs nothing (the row is flat above about 106, the Scherzo's finding), so the chord keeps the make-up and the accent bump on top. At f, `rest_map` and `row_dyn` ("Sus MAX" -4 to -6 units at 88) put the figure at CC11 75-82 where c16 had 88.

**Corrected values (instrument side; check on a range render 0:24):**
- Figure: `_C17_NOTE_CC`, upper strings, a span entry `{"lane": "cc11", "from": 8.8, "to": 15.95, "add": 7}` (CC11 82-89; expect +2 to +3 dB).
- Chords: span entries `{"from": -0.1, "to": 5.1}` and `{"from": 15.9, "to": 21.1}` with `add` -10 on Violins I and II, -14 on Violoncellos, -4 on Violas (expect -2 to -3 dB with the halved accent of finding 1). If CC11 proves flat down to 93, say so in LEARNINGS: then the only instrument-side lever for a "Sus MAX" ff chord is the Opus row volume.
- Bars 83-98: no make-up change. The excess is the accents of 91-94 (finding 1) and the Double basses (+4.8 dB over 344-376, +6.2 to +9.8 in bars 90-96, the loudest stem of bars 91 and 110 at -29.0 / -27.1 dBFS): the E flat 2 region gain of +8 dB. That value was fitted in the 30-125 Hz band; broadband it puts the basses over the trumpets. Try +5 (critic B's call).

**Arc (inferred from the same numbers):** ff tuttis sit at -16 to -18 (bars 1, 91-94, 110-113, 199-204, K-weighted), the f first theme at -25 to -30 (bars 11-26), the mf second theme in the violins at -30 to -32 (bars 67-76). Bar 204 (ff) to bar 205 (f, same hammered texture less trumpets) is -18.4 to -27.4, woodwinds and horns falling 12-13 dB. One step from mf to f is 3-4 dB and from f to ff 9 dB or more. The c14 comparison with the Dvořák recording showed the same shape (the mockup's upper quartile of short-term loudness 3-4 dB further under its peak). A first step that needs no new rule: `dyn_trim_db` f +1.5 dB on the horns and the woodwinds (Horn 1 f is -2.0 now, Flute 1 -3.5), then re-measure bars 11-26 and 205-208 against 199-204 (target: f tutti 6-7 dB under ff tutti).

### 6. Smaller items

- **Stop of bar 166** (qn 662): drop at +0.3 s 13.5 dB (c16 14.9), -20 dB at 0.47 s. Cause: the Double basses stand at -23.2 dBFS before the stop (region gains) and at -37.6 at +0.3 s, level with the string return. Fix as bar 204: `note_end` Double basses `{"end": 662.0, "early_s": 0.06}` and `cc_shape` CC11 `[(-0.2, 0), (-0.06, -24), (0.44, -24), (0.5, 0)]`. With my detector (reference 0.05-0.20 s before the release) the other stops read: bar 2 15.1 dB / 0.46 s, bar 6 14.7 / 0.45, bar 94 15.0 / 0.43, bar 113 15.8 / 0.46, bar 204 15.5 / 0.40, final 14.7 / 0.41. All inside 14.5-17; bars 2 and 204 need no refit by this measure (the actor's 17.3 / 17.4 come from a later reference window). If bar 204's CC11 fall is cut from 32 to 24 units, expect about 14.5 dB: leave it at 32.
- **dal niente** (manual p.63, still open from c14): Clarinet 2 at 184 is at -48.4 dBFS 0.1 s after the note-on and within 0.6 dB for 5.6 s (CC11 34 flat); Clarinet 1 at 200 -52.2 at +0.1 s; Clarinet 2 at 680 -51.7; only the Bass clarinet at 680 fades in (CC11 24 -> 34, 7 dB in 0.5 s). Fix in CC11, `cc_shape` at the three clarinet onsets: `[(-0.03, -22), (0.5, -10), (1.2, 0)]` (clarinets: CC11 is plain volume). Target: first 0.2 s at least 8 dB under the body.
- **Held unison at Horn 4 qn 552** (+9.5 -> 0 dB at 22 dB/s inside the note, role [548,552,+7.5] ending): a one-bar +7.5 / +10.5 dB row on Horns 3-4 is a per-note level; move to CC1 or delete and re-measure.

## Answers to the coordinator's list (my lens)

- Chorale dips: the 8-unit swell is not the lever; no split (pedal tied) with re-bows off the bar lines is (finding 3). A second instance is not needed: celli and basses are the two interleaved voices.
- Stops: only bar 166 (above).
- Section loudness 1-10 and 83-98: finding 5.
- sfp 149: finding 2; no swell after the p, but no sf and a late ff.
- Slow rows fitted to old layers: finding 4.
- Movement I c58 (2) and (3): apply (46 dynamic-step and onset moves inside notes; shapes at 10-30 dB/s). c58 (5) re-bow holes from the bloom: applies (finding 3). Scherzo "arrivals give back": does not apply. Movement II "sf > p swells": does not apply. Movement I c57 (5) drive shape sinking held horns: not seen (chorale horn notes hold within 1.5 dB after the head).

**Do not touch:** the delivery chain and the ride rows (gain flat within 0.3 dB over 42-50, 170-186; LRA 15.0); `rest_map` and the make-ups outside the two intro spans (plain ff notes within 0.2 dB of c16); the timpani CC7 fold, roll levels and settles (every roll 3 dB or more under the loudest stem); the crescendo rolls; the p floor of the sfp (12.5 dB) and Trumpets 1-2's ff through it; the final chord and its release; the builds 107-110, 135-147, 219-221, 255-263; the re-bow layout elsewhere (no string note over 5.5 s, no loop pulsing); the bar 204 note ends and CC11 fall; `vol_guard`; the muted trumpet's CC1 pitch table apart from the values in finding 4.

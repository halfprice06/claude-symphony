# Cycle 16, critic A: articulation and phrasing after the removal of the per-note volume moves (on the c15 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB on the stems of `cycles/c15/render/` against `cycles/c14/render/`, read on each cycle's own `build_render/parts.json`. "Measured" = a number from those stems, from parts.json or from the config; "inferred" = reasoned, not tested. Nobody heard the audio. Every fix below is on the instrument side (CC11, velocity, row, note length, gap, patch state) or is a change to a slow envelope rule; none adds a per-note volume move.

Not measured this cycle (data unchanged from c14 except the envelope): harp, pizzicato and arco changes, sul A, con sordino, timpani rolls and stroke hardness (critic B has the timpani), loop pulsing on brass and winds.

## Manual notes (May 2021 HO manual, PDF pages 95-99, read in full)

| Manual | Where it applies here | Does the render follow it |
|---|---|---|
| p.96-97 Slur Runs (1st and 2nd Violins only): sustains on CC11, no velocity; "a minimum speed is sixteenth notes at about 125 beats per minute" (8.3 notes per second) | the slurred eighths of the theme head and the fugato (8.8 notes per second at quarter 264) | Not used; c13 tested and rejected it. No change asked |
| p.97 Tremolo and Measured Tremolo TS: CC11 only, tempo-synced | none (the scherzo has no tremolo) | Not applicable |
| p.98 Repetitions (in the manual: Violas and Basses; the KS Masters of all five sections list "Repetitions TS"): one note repeated for a little over a second, about a dozen pulses, tempo-synced, CC11 crossfades 3 layers, no velocity | S1, the theme's two repeated staccato eighths; the violas' and basses' repeated quarters | Not used, and not suitable: the figure is two strokes, the row is a fixed burst of a dozen. The separate strokes already separate (short after short, peak over the floor before it: Violins I 11.3 dB, Violins II 10.6, violas 9.9, celli 16.1, flutes 14.8-16.6, Oboe 1 10.7, trumpets 8.1-9.6; unchanged from c14) |
| p.99: "For any legato patch to generate a slur or portamento, two notes must have no significant time gap"; "the first note of a phrase has no legato effect at the start" | every slurred line; the re-bows of held notes | Slurred lines: yes (overlap 60 ms; joins with a hole over 6 dB: celli 11 of 185, Violins II 4 of 92, violas 4 of 63, Violins I 0 of 73). Re-bows: a same-pitch re-bow cannot be a legato transition, so each one is a new first note on "Sus MAX"; at ppp that first note needs over a second to reach its level (finding 1) |
| p.99 legato rows are monophonic; CC22 64-127 makes them polyphonic | chords on legato rows | Followed (chords go to Sus rows; not re-checked) |
| p.99 Legato Slur Staccato: "adds a Slur Staccato accent to notes that do not have a legato connection to the previous note ... the first note of each legato phrase [receives] a slightly stronger attack" | accented slur heads at p to mf (second idea, bars 45, 121, 125, 277, 281; the theme's appoggiatura in the winds) | Not used. The rows exist in the loaded KS Masters ("StacSl Leg BC + Slur + Port MAX" in both violin sections, "Stac Leg BC + Slur + Port MAX" in violas and celli; the woodwind masters have "Leg Slur Accent MAX"). A candidate for finding 2, second choice after CC11 |
| p.99 Legato Bow Change: "string players sometimes have to change the direction ... the sound of the bow changing direction" | re-bows inside a slurred line (c14 moved all "Leg BC MAX" notes to "Leg Slur MAX") | Unloaded since c14; no change asked |

## The c15 actor's list of faults, measured on the c15 stems

| projected fault | real? | size (c14 -> c15) |
|---|---|---|
| printed accents without level (296) | yes | 274 measurable accents: median level over the mean of the two neighbours +1.2 -> +0.1 dB; under +1 dB: 128 -> 167 (finding 2) |
| row-to-row jumps of 3-6 dB | yes, on five tracks | finding 3 |
| dips at 9 re-bows | yes, larger than projected | five exposed re-bows dip 9.4-13.1 dB (c14 1.2-3.7) (finding 1) |
| 66 soft phrase heads late | mostly no | the 11 fills on entries after a rest: the -6 dB point moved 0-10 ms (they were late in c14 too, at the 0.30 s lead cap); first 100 ms 1-2 dB lower. Real: Violas div 1044 (0 -> +140 ms), celli 794 (+60 -> +240 ms), 542 (+80 -> +140) (finding 6) |
| bumps at 5 joins | three of five | celli 506 +2.2 -> +6.4 dB, 764 +0.1 -> +2.7, 800 +1.7 -> +3.3; celli 570 has no bump but a hole (3.1 -> 7.9 dB); Clarinet 1 459: none (0.0) (finding 6) |
| less separation on slurred wind and brass repeats | small | 8 notes lost 2-3 dB; the larger fault is older (finding 5) |
| remaining notes with over 3 dB inside | 152 by my count, 67 without a printed hairpin, dynamic or fade | finding 4 |

## Findings

### 1. The held ppp G sharp of Violins I and the harmonic E6 now break at every re-bow: 9-13 dB holes, then 3-6 dB softer for over a second (measured)

Where: Violins I bars 1-8 (re-bow at qn 6.446) and bars 364-376 (re-bows at 1103.814, 1116.299, 1125.156); the harmonic E6 on the Violins II track (re-bow at 432.5). These are the exposed held notes of Dan's note 8.

What: each re-bow is a new "Sus MAX" note that starts 0.03 qn after the old one ends. At CC11 22-25 the new sample needs about 0.4 s to speak and 1.5-2 s to reach the old level. c14 covered this with re-bow fills of 9-14 dB; they are gone.

Evidence (lowest 40 ms frame within -0.25..+0.5 s of the re-bow against the 0.5 s before it; step = +0.6..+1.0 s against before):

| re-bow | c14 dip / step | c15 dip / step |
|---|---|---|
| Violins I 6.446 | -3.0 / -0.3 | -9.4 / -5.6 |
| Violins I 1103.814 | -3.7 / -0.6 | -13.1 / -6.2 |
| Violins I 1116.299 | -1.2 / -0.7 | -12.0 / -3.5 |
| Violins I 1125.156 | -1.6 / +0.2 | -13.0 / -4.4 |
| Violins II 432.5 (harmonic) | -1.5 / +1.2 | -10.9 / +0.1 |

The four pieces of the last note are 4.0, 3.7, 3.7 and 3.4 s long, so the final G sharp falls into a hole every 3.7 s, which is a stronger pulse than the 3.95 s sample loop the re-bows were written to hide. Its 0.1 s levels read -43.5 (piece 1, on "Leg Slur MAX"), -47, -47.5, -50.5 dB (pieces 2-4, on "Sus MAX"): a staircase down, where the score has one ppp note. The last re-bow falls on the downbeat of bar 376, the fermata bar. The other re-bows (violas 675-1080, celli 579-1080) dip as they did in c14 (within 1 dB, except violas 1080: -8.2 -> -12.3).

Fix, in this order:
- `build/score_config.py`: `AUTO_REBOW_SKIP = {"Violins I": [0.0], "Violins II": [420.0]}`. Both notes are short (5.25 s and 5.69 s): one bow each passes the 3.95 s loop point once, which cannot pulse. This removes two of the five holes. Inferred: check the folded 3.95 s measure on both after the render.
- The last note (14.7 s) cannot be one bow. Play it on two instances that change bow at different times, which is what "change bow freely" means in a section. The "Violin I solo" track (1st Violins KS Master DIV A) is silent after qn 1068. Route a copy of the G sharp to it for 1089-1128 (`TRACK_WINDOWS` or a new generic `HELD_DOUBLE = {"Violins I": [(1089.0, 1128.0, "Violin I solo")]}`), on its already loaded "Leg Slur MAX" row (no new row, no memory), with its re-bows placed halfway between the Violins I re-bows (`REBOW_AT`: Violins I about 1103.8 and 1116.3; solo track about 1096.5, 1110.0 and 1121.0), and no re-bow on either track after 1122. Both tracks at their ppp CC11, the solo track's role about 3 dB under Violins I, and Violins I's own role for 1089-1128 lowered by the same amount the sum gains (a constant, measured on a range pass). Simulation on the c15 stem (the stem plus a copy shifted 1.86 s, each -3 dB): lowest 0.1 s frame 4.3 dB under the median instead of 11.7 dB. Inferred for the real DIV A sample (Close mics only, half section): test on a range render of 1086-1128 before the full render; pass if no 0.1 s frame of the two-stem sum is more than 5 dB under the median.
- Put the first piece on the same row as the others (`REBOW_SAME_ROWS` or a `first_art` of "Sus MAX" for a tied note that is re-bowed): piece 1 on "Leg Slur MAX" is 3.5 dB over piece 2 on "Sus MAX" at the same CC11.
- If the doubling test fails, re-bow the last note once (two pieces of about 7.4 s, `REBOW_SEG_S` raised for this note through `REBOW_AT` = [1107.0] and `AUTO_REBOW_SKIP`), accept one hole in bar 370, and list it in CHANGES.md.

### 2. Printed accents carry no weight, and the theme's accented appoggiatura is the weakest note of its figure in the oboe and Flute 2 (measured; the CC amounts partly inferred)

Where: all 321 accents. The clearest case is the theme's accented half note after the staccato figure (qn 111, 123, 207, 315, 327, 345, 351, 819, 891, 915, 927, 945, 951) and the accented heads of the second idea (132, 144, 360, 372, 828, 840).

Evidence. Accent over the mean of its two neighbours (0.35 s from the score onset), c14 / c15 medians, by CC11 at the accent:

| | p-mp (CC under 70) | mf-f (70-104) | ff (105 or more) |
|---|---|---|---|
| strings (143 accents) | -0.3 / -2.1 | +1.6 / 0.0 | +0.9 / 0.0 |
| woodwinds (131) | -0.9 / -1.2 | +1.3 / -0.3 | +1.7 / +1.0 |

Per line in c15: Oboe 1's appoggiatura is -8.8 dB (111), -3.8 (123), -6.5 (132), -2.6 (207), -4.8 (819), -11.4 (828), -5.2 (891) against its neighbours, and 0.2-0.6 at ff (315, 345, 351, 915, 951; c14 +5.4..+5.7). Flute 2: -4.1 to -7.0 at 315, 345, 351, 819, 945 (it was as low in c14). Violins I at f: +0.1 (123), +0.7 (207), -2.0 (819), -0.8 (891). Violas mf-f: +2.2 -> -0.4. No bite anywhere: the 2-5 kHz share of the first 80 ms is at or under the body's on every track (-3.5 to +1.3 dB, as in c14).

Why CC11 does nothing now: accents sit at the plain note's CC11 (medians 100-114 on strings, 111-126 on woodwinds; the added bump is 0-4 units). Level by CC11 on "Sus MAX" with the fader divided out, medians over notes: Violins I -32.4 (CC 85-100), -27.2 (108-116), -27.5 (116-127); Violins II -33.8, -27.0, -26.6; violas -33.5, -29.2, -28.4; celli -32.2, -28.9, -27.5. The rise is between about 92 and 106 (0.3-0.5 dB per unit) and the lane is flat above 106. Velocity does nothing on these rows.

Fix (`build/score_config.py`, `tools/score_to_parts.py`):
- mf-f and softer (93 accents): `ACCENT_BUMP_AT = {track: 12}` for Violins I, Violins II, Violas, Violoncellos, Double basses, Flute 1, Flute 2, Oboe 1, Oboe 2, Cor anglais, Bassoon 1, Bassoon 2, Contrabassoon, capped at CC11 112 (so the fff layer is never reached: Movement I c02's 14.5 dB click came from a bump into that layer). The bump's length is now 0.3 qn (68 ms at quarter 264): give it seconds through a new generic `ACCENT_BUMP_S = (0.15, 0.25)` (held 0.15 s from 0.01 qn before the moved onset, back to the curve over 0.25 s). At 0.3-0.5 dB per unit this is +3.5 to +6 dB at mf and about +3 at f.
- ff (152 accents): give the accent room by lowering the plain notes. In the spans with printed accents at ff (bars 101-120, 300-320, 333-339) plain string and woodwind notes rest at CC11 100 (new generic `CC11_REST_CAP = {family: [(from qn, to qn, cap)]}`), accents go to 116, and the lost level (measured 1-2 dB on strings between CC 100-108 and 108-116) goes into `mix.json` `dyn_trim_db` "ff" of those tracks. Clarinets (CC1 carries their dynamic): the same in CC11 only, resting 100, accent 121.
- Slur-head accents under f on woodwinds (Oboe 1 111, 132, 828, 840, 87, 99, 276; Flute 1's p accents: 10 of 15 under +1 dB): they play the first-note layer of "Leg Slur MAX". Lower the Sus threshold for accented slur heads (line 2572 of `score_to_parts.py`, `base(q) >= DYN["f"] - 4`) to a new generic `ACCENT_SUS_MIN_CC` (default 84 = today; woodwinds 44) so the head is a tongued "Sus MAX" note joined to the slur, as `SLUR_START_SUS` already does. Second choice, by range test only: "Leg Slur Accent MAX" on those heads.
- Range test before the full render: bars 105-120 on Violins I, Violins II, Oboe 1. Pass: accent +2.5 to +3.5 dB over its neighbours (median), under 20 % of accents below +1 dB, 2-5 kHz of the first 80 ms no more than 3 dB over the body.

### 3. Row levels: staccato and sustain rows of the same line are 4-9 dB apart on Flute 1, Flute 2, Oboe 1, Violins II and celli (measured)

Where and evidence (adjacent notes on different rows with CC11 within 8 units; median level difference, c14 -> c15, n):

| track | rows | dynamic | c14 | c15 |
|---|---|---|---|---|
| Flute 2 | "Stac DblTng RRx9" over "Sus MAX" | ff / mf-f | +7.9 / +4.7 | +6.0 (n 6) / +7.9 (n 3) |
| Flute 1 | "Stac DblTng RRx9" under "Sus MAX" | ff / mf-f | +0.6 / -4.3 | -5.3 (n 7) / -4.0 (n 4) |
| Flute 1 | "Stac DblTng RRx9" under "Leg Slur MAX" | mf-f | -4.9 | -5.4 (n 6) |
| Oboe 1 | "Stac DblTng RRx9" over "Leg Slur MAX" / over "Sus MAX" | mf-f | +1.1 / +1.5 | +5.8 (n 7) / +9.5 (n 4) |
| Violins II | "Sus MAX" over "Leg Slur MAX" | ff / mf-f | +2.9 / +2.5 | +5.4 (n 3) / +4.2 (n 6) |
| Violoncellos | "Leg Slur MAX" over "Sus MAX" | p | +3.4 | +4.5 (n 12, 10 of them over 3 dB) |
| Violas | "Leg Slur MAX" against "Sus MAX" | p | 9 of 14 pairs over 3 dB | 11 of 14 |

The same shows in the whole-row medians with the fader divided out: Violins II "Sus MAX" -27.0 against "Leg Slur MAX" -35.0 dB at CC 108-116, and -49.4 against -45.0 at CC 40-55 (the sign turns with the dynamic, as the finale found). Oboe 1's and Flute 2's hot staccato row is also why their accented half notes sit under the figure before them (finding 2). Flute 2 was this far off in c14 already.

Fix (`build/mix.json`, `region_gain_db`, the mechanism of c15; no fader):
- Flute 2: `"row_db": {"Stac DblTng RRx9": -6.0}`.
- Oboe 1 and Flute 1 differ by dynamic, so a whole-row gain is wrong for them. Add to `tools/build_reaper.py region_gain` an option `"row_dyn_db": {row: {dynamic suffix: dB}}` that applies the gain only to regions of groups whose name ends in the listed dynamic, the selection `sus_release_cap_ms` already uses (for a short row whose layers are chosen by velocity, select by the region's velocity range instead). Values: Oboe 1 "Stac DblTng RRx9" mf and f layers -5; Flute 1 "Stac DblTng RRx9" f and ff layers +4; Violins II "Leg Slur MAX" f and ff +4; Violoncellos "Sus MAX" pp and p +4; Violas "Sus MAX" pp and p +2.
- Test as c15 tested the pitch gains: one whole-piece pass of these five tracks, per-note readings against this table; pass if every pair above is within 2 dB. Then re-check the section balance (critic B), since the row levels move whole passages by 1-2 dB.

### 4. What still moves inside notes: 67 of 152 notes are not a printed hairpin, dynamic or fade; the crescendo arrivals fall back 6-7.5 dB inside the note they arrive on (measured)

Count: 152 notes have more than 3 dB of written envelope between 40 ms after the score onset and the note's end (the actor counted 156); 85 lie under a printed hairpin, a dynamic change or the final fade. The other 67, by cause:

- Crescendo arrivals (20 notes). After the crescendos into f at qn 120 (bar 41), 384 (bar 129), 588 (bar 197) and 852 (bar 285) the envelope gives the crescendo's gain back while the arrival note is held: Bassoon 1 at 120 / 384 / 852: 7.3 / 7.4 / 7.5 dB; Bassoon 2 7.3 / 7.2 / 7.3; Contrabassoon 384 / 852: 7.4; Clarinet 1 at 120: 7.3; Clarinet 2 at 588: 7.3; celli 384: 6.0; basses 384 / 852: 6.2; smaller at 156, 312, 912 (3.4-4.0). The printed dynamic is f throughout, and CC11 goes on rising (88 to 95). On the stems the held B of bars 129-130 falls from -29.2 to -32.0 dB (basses) and -30.2 to -38.3 (Bassoon 1), and the master falls from -18.4 dB (qn 383) to -23.2 (qn 387-389): the f hemiola cadence of bars 129-131 arrives and sinks 4.8 dB in four beats. c14 had the same fall, faster (0.5 s). Source: the dynamic trims (mp +9 dB, f 0 on the bassoons) with `cresc_trim_hold` released over 1.0 s, plus the hairpin gain's release.
  Fix: `mix.json` `cresc_trim_hold`: do not release on a clock. Hold the amount to the end of the note that sounds at the arrival and release it over the following rest or across the next printed dynamic (new key `"release": "note_end"`; `release_s` stays as the ramp length after that point). The same rule for the hairpin gain's release (`hpgain`). This keeps the envelope slow and puts its move where no note sounds.
- Hard steps inside a sounding note (about 12 notes): celli 339 and 939, 5.9 and 5.6 dB down within 50 ms, 0.5 s into a 0.55 s ff note (a role edge at about qn 341.2); basses 93, 6.0 dB down within 50 ms at qn 95.7; timpani strokes 390, 858 and 1008, +5.0 dB within 50 ms, 50-70 ms after the stroke (the edge of the roll's settle: the stroke gets louder after its attack, stem -34.1 then -32.1 dB at 390); Horn 3 348 and 353 (4.6 and 3.1); celli 612 (+5.0 at +60 ms).
  Fix: `build/roles.json` and the roll-settle rule: every edge of a slow row is placed in the nearest rest, or at the moved note-on of the next note when there is no rest, never between a note's moved onset and its end. A check for `score_to_parts.py`: warn for each role or level-row edge of 2 dB or more that lies inside a sounding note of its track.
- Bar 338, the last chord before the G.P. (qn 1011-1014; 12 notes): +3 dB at 1011.5, -3 at 1013.5 and -3 at 1014 on Violins II, violas (6.0 dB inside the note), celli (5.7), clarinets (5.4-5.5), bassoons, Oboe 2, cor anglais (3.9). The chord sinks 6 dB before its cut-off, which weakens the stop before the silence (S3).
  Fix: one level for 1011-1017 on these tracks (the +3 unison span of one chord removed or extended back to 1008; the ride row's -1 dB kept).
- Left alone: timpani roll shapes at 384, 852, 1005 (12 dB, Dan's roll rule), and steps of 3.0-3.5 dB that cross a led note-on at +60 ms (Flutes 130, Flute 1 213 / 384, Clarinet 2 123 / 853, bass clarinet 264): move them to the moved note-on with the same check.

### 5. S1: repeated tenuto notes run together in Horn 1, in the trumpets' last three chords, and in a third of the other horns' repeats (measured)

Where: Horn 1's repeated tenuto dotted halves (qn 147-159, 300-309, 636-651, 900-909, 993-1005) and "Port Lng" repeats (630, 633, 663); Trumpets 1 and 2 at 1008, 1010, 1012 (three tenuto A4 half notes, bars 337-338) and Horns 1 and 4 at 1011-1014; Horn 2 and Horn 4 repeats at 303-309, 603-609, 657, 687, 1008.

Evidence (peak of the second note's first 120 ms over the lowest 15 ms frame before it): Horn 1, 24 repeats: median 2.2 dB, 13 under 3 dB, played gap 35 ms (`WIND_REP_RETONGUE_BY["Horn 1"]` gap_s 0.035, set in c08 against 7-11 dB dips). Trumpets at 1008-1012: 0.0-0.1 dB, gap 6 ms: the three chords are one note. Horn 1 and Horn 4 into 1014: 0.1 dB, gap 6 ms. Horns 2-4 with a 70 ms gap: medians 5.0 / 8.0 / 4.6 dB, under 3 dB on 9 of 28, 5 of 21, 13 of 36 (c14: 8, 4, 9). The removed detach dips cost 2-3 dB on Horn 4 303 / 306 / 309 (4.1 -> 2.3, 3.8 -> 2.0, 4.4 -> 2.2) and 609, Horn 3 603 (3.7 -> 0.6), Horn 2 657 (3.2 -> 0.7) and 1008 (5.5 -> 2.9), Horn 1 306 / 309 / 909 (2.1 -> 0.3). Woodwind repeats did not change (bassoons 7-8 of 40-43 under 3 dB in both cycles, all in the pp bars 143-147).

Fix (`build/score_config.py`): `WIND_REP_RETONGUE_BY["Horn 1"]` gap_s 0.035 -> 0.065, frac 0.15 -> 0.2, fall_cc 4 -> 8; "Horn" gap_s 0.1 kept but with a floor: a new generic `REP_GAP_FLOOR_S = {"brass": 0.09, "wind": 0.065}` applied to the played gap (note-off to the next moved note-on) of every same-pitch repeat that is not under one slur, which also catches the 6 ms gaps at 1008-1014 (their re-tongue lead eats the gap). Finale c17 measured 5-13 dB of separation at 90 ms on these patches and none under 60 ms. Target after the render: Horn 1 median 3-6 dB (not c08's 7-11), no brass repeat under 2 dB.

### 6. Legato phrase heads and joins: three bumps and five late heads are real; the rest of the projected list is not (measured)

Where and evidence:
- Join bumps (highest 20 ms frame within -0.12..+0.2 s of the score onset over the louder neighbour's body), c14 -> c15: celli 506 +2.2 -> +6.4 dB, 764 +0.1 -> +2.7, 800 +1.7 -> +3.3. Celli 570 has a hole instead (lowest frame under the quieter neighbour 3.1 -> 7.9 dB). Clarinet 1 459: no bump (0.0), and Clarinet 1's four join holes of c14 are smaller (138: 7.6 -> 2.4; 399: 9.4 -> 3.8; 468: 8.5 -> 3.9; 840: 8.9 -> 6.0).
- Velocity is a usable lever on the celli: of their soft joins (CC11 under 60), targets at velocity 70-90 bump over 3 dB on 0 of 13, targets at 91-110 on 14 of 55.
- Heads: Violas div 1044 (bar 349) reaches body -6 dB at 0 -> +140 ms; celli 794 +60 -> +240 ms and 542 +80 -> +140; Bassoon 1 353 and 953 (first 100 ms -0.3 -> -5.0 dB under the body); Clarinet 1 576 (-1.6 -> -6.2). The other soft entries were as late in c14 (Oboe 1 672 +190 ms, Flute 1 1044 +270, Violin I solo 1044 +210, Violins II 672 +180, 708 +130, violas 1020 +150, basses 504 +110) and sit at the 0.30 s lead cap; they fade in at pp, which a dolce entry may do.

Fix (`build/score_config.py`, `build/entry_leads.json`):
- Legato velocity 80 on the celli targets 764 and 800 (now 100) and 570 (now 100) through `VEL_SET`; 506 is already 80: lower its predecessor's overlap from 60 to 40 ms (`LEG_MIN_GAP_AT` or the overlap rule for 504-507) and re-measure.
- Violas div 1044: entry extra 0.08 -> 0.20 s (the cap allows 0.30 total); celli 794 and 542: the head note's CC11 lifted by 10 for the first 0.25 s (`ACCENT_CC_AT`, the c11 mechanism: (10, 1.0)); Bassoon 1 353 / 953 and Clarinet 1 576: the same lift, (8, 0.75).
- No change to the other entries.

## Do not touch

The short strokes and their separation (every staccato pair separates by 8-19 dB; MIDI lengths are 50 % of the slot in every section; only the coda's Violins II and celli play 35 %, a small difference); the legato joins of Violins I (0 holes over 6 dB), the celli's and Horn 3's trio-tune timing of c15; the per-region pitch gains in the Opus state; the "Sus Marc LITE" row at -8 dB (the theme's accented half note stands +1.8 to +6.6 dB over its figure at qn 39, 51, 69, 75, 285, 759, 771, 795); the absence of bite (2-5 kHz front at or under the body on every accented track); the rule itself: nothing in this report needs a per-note fader move.

# Cycle 18, critic B (balance and levels), on the c17 render

All levels are measured on `cycles/c17/render` (stems and master), against `cycles/c16/render` and `cycles/c15/render`, on the parts.json tempo map. The tempo map is the same in all three cycles. "Bar mean" is the mean power over the bar. "M max" is the highest EBU momentary loudness (400 ms) of the master, from ffmpeg ebur128. "p90" is the 90th percentile of 100 ms frames. Positions are score quarter notes (qn). Each claim is marked measured (m) or inferred (i).

## Manual notes (May 2021 HO manual, slot B6: PDF p.32-34, 43, 46, 191-192)

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Streaming and preload by drive type, Never Preload, multi-threaded voice renderer (p.32-33) | render-to-render repeatability on tracks whose data did not change | yes (m): c16 to c17 per-bar difference on unchanged tracks is median 0.00 dB (Harp, Harp harmonics, Oboe 2 max 0.0-0.3 dB). Tuba, trombones and Horn 3 move only in bars whose data changed |
| Round Robin reset controller or note (p.34) | the repeated pizzicato and staccato strokes. `RR_RESET_AT` uses CC16 (MANUAL-GAPS #12) | yes (m): the celli's pp pizzicato B2 in bars 89-98, 10 strokes at velocity 52, peak range 1.9 dB, consecutive median 1.3 dB (c16 at velocity 41: 8.6 / 5.1 dB). The basses' B1 range is 4.6 dB, unchanged |
| The instrument's Volume slider is the same control as its Play page channel and Mix fader (p.43) | track level set in REAPER (`mix.json gain_db`) or in Opus | yes: levels are set in REAPER and as region volumes. No Opus fader is automated |
| System usage: voices, RAM (p.46); All Instances window: purge and preload per instrument and articulation (p.191) | memory: 43 GB settled, unused rows unloaded | yes (CHANGES c17) |
| Voice Limit per instrument: voices are stolen when it is reached, and each mic and articulation counts (p.192) | the "non div." double and triple stops at bars 72, 300 and 336-339 on Violins II, violas and celli (2-3 notes x 2 mics) | no sign of stealing (m): the bar 72 chord is 12.4 dB over bar 71 on Violins II and 9.1 dB on violas. The limit value in the saved states was not read |
| Key Range and Octave (p.192) | not used | n/a |

## Climax order (m)

Master M max, c17 (c16): summit bars 336-338 -11.7 (-10.6); tutti 105-120 -11.9 (-12.9), whose peak is at qn 328.4 (bar 110); tutti 305-320 and bar 304 -13.1 (-13.4); bar 333 ff -15.3 (-14.0); bar 300 ff -15.7 (-10.5); bar 53 ff -16.4 (-15.8); bar 72 ff -16.9 (-11.8); bars 209-224 (printed f, ff only at 218) -17.1 (-17.1). Mean of the loudest 3 s: summit -12.6, tutti 105-120 -15.4.

c17 fixes c16's inversion: in c16, bar 300 (-10.5) was louder than the summit (-10.6), and bar 72 was 1.1 dB over the brass tutti. Two problems remain. Bars 72 and 300 now fall 5.1 and 2.6 dB under the tuttis (finding 1). One Flute 2 note brings the tutti's peak to 0.2 dB under the summit (finding 4).

## Verdict on the 30 bars of `records/bars_c17_vs_c16.txt` (m, causes per finding)

- **c17 is closer to the print.**
  - 42, 130, 198, 286 (the bar after an f arrival): equal to c15 within 0.8 dB. c16's held arrival gains were the c16 critics' "+1-2 dB" fault.
  - 67: c15 +0.4.
  - 90, 93, 97: the celli's pp pizzicato is now at the basses' pp pizzicato (-52.1 against -51.7 over bars 89-98; c16 was 7 dB under).
  - 184: Bassoon 2 equals c15.
  - 290: the celli's fugato entry is within 1.2 dB of its exposition counterpart in bar 58 (c16 was 2.9 dB under).
  - 326: the violas' pp head is 2.0 dB under the celli's identical pp head in bar 325 (c16 was 3.2 dB over). One fix is still needed: see the note in finding 6.
  - 349: the solo is audible from its first note.
  - 364-365: Horn 1's pp G sharp equals c15 and its own pp G sharp in bars 1-2, within 1.3 dB.
  - 374, 376: Horn 1's last note was raised on purpose. Its ppp end is still 3.6 dB under bars 372-373.
- **c16 is closer.**
  - 41, 129, 195-197, 284-285: crescendo arrivals that now arrive short (finding 2).
  - 137-138: the low group, raised by rows, at printed p (finding 3).
  - 264: Flute 1's accented C6 at the top of its hairpin. CC11 is 70 (c16 80), because Flute 1's accent `add` is 2. Raise it to 5; accents are critic A's lens.
  - 312: the celli's countermelody (finding 6).
- **Neither is right.** In 72-73 and 300, c17 overshoots by about 2-3 dB and c16 was louder than the tuttis (finding 1).

## Findings, ranked by what a listener hears

### 1. Bars 72 and 300 (qn 213, 897): the woodwinds' ff accented arrival is softer than the f bar before it (m)

The print: winds and strings crescendo from f into an accented ff chord, without the low brass (bar 72 also has a decrescendo). On the stems, the c17 rise into the arrival beat (`hp.py`, the arrival beat against the hairpin's first beat) is reversed or flat:

| track | 211-213 rise, c15 / c16 / c17 | 895-897 rise, c15 / c16 / c17 |
|---|---|---|
| Flute 1 | +9.3 / +10.1 / -2.7 dB | +6.3 / +9.8 / -2.9 dB |
| Clarinet 2 | +5.1 / +5.6 / -0.4 | +5.4 / +6.0 / 0.0 |
| Bassoon 1 | (210-213) +0.8 / +1.9 / -2.3 | (894-897) +1.5 / +2.7 / -1.3 |

At the arrival beat against c15: Flute 1 -10.3 / -7.4, Clarinet 1 -4.2 / -4.1, Clarinet 2 -6.2 / -6.0, Bassoon 1 -7.4 / -7.2, Bassoon 2 -6.3 / -6.2, Oboe 1 -3.6 / -2.1 dB. In the same bars, Flute 1's bar mean is 5.9 dB under bar 71, and Bassoon 1's is 4.3 dB under bar 71.

There are three causes, all in the data.
- (a) `score_config.py` `ACCENT_CC` per track writes `"add_at": {213.0: min(8, l_), 897.0: min(8, l_)}`, where `l_` is the track's `add_loud`. That gives 0 on Flute 1, Cor anglais, Clarinet 1, Clarinet 2 and Bassoon 1 (all `add_loud` 0) and 4 on Oboe 1. The "+8 at 213 / 897" of item 4 never reached these tracks: Flute 1's CC11 is 104 at 212.814, and the clarinets fall from 104 straight away (c16: 114).
- (b) `HP_GAIN_TO_CC11` `drop_ends` [213, 897] removed the +4 dB crescendo gains (Bassoon 1 +7) for all families, with nothing in their place.
- (c) Flute 1's `region_gain_db` "Sus MAX" f layer `88: -5`, sized for accented E6 notes elsewhere, also hits these unaccented-row ff arrivals on E6.

The strings lose 3-5 dB in the same bars (Violins II -4.1, violas -4.6, celli -4.8 on bar means). That is the dropped +3 dB envelope gain plus a faster CC11 fall (c17 reaches 98-100 at 214.0; c16 115). `CHORD_CC11` is a smaller share.

Fix (instrument side; the hairpin itself is printed):
- `ACCENT_CC`: write `add_at` 8 for every wind track at 213 and 897, not `min(8, l_)`. The winds' CC11 is not flat above 104: Flute 2's bump from 107 to 117 gave +2.9 dB at bar 110.
- `HP_GAIN_TO_CC11`: limit `drop_ends` to the "string" family. For woodwinds, carry the crescendo 211-213 / 895-897 as the printed hairpin ramp. In bar 72, release it inside the printed decrescendo 213-216. At 897, release it with the printed sfp fall at 900.22, so no release crosses the upbeat.
- Flute 1 `region_gain_db` "Sus MAX" f `88`: -5 to -2.

Expected (a stem-sum estimate with the winds at their c15 level): bar means +2.0 / +1.7 dB, M max about -14.9 / -14.0. That is 2-3 dB under the brass tutti and the summit, which is the printed order. Raise the strings' share by +1-2 dB only if the woodwind fix falls short. Do it with a slower CC11 fall on the 213 / 897 chords (hold 112 to 214.0), not with an envelope row.

### 2. Crescendo arrivals on CC11 arrive 3-7 dB short on bassoons, clarinets and violas (m)

Of 271 printed crescendos of 2 qn or more that sound on their track, 66 track arrivals are 1.5 dB or more under both c15 and c16 at the arrival beat.

| arrival | bar | track, dB under c15 |
|---|---|---|
| qn 120 | 41 | Clarinet 1 -3.6, Clarinet 2 -6.0, Bassoon 1 -6.8, Bassoon 2 -4.3, violas -4.4 |
| qn 384 | 129 | Bassoon 1 -3.9, Bassoon 2 -5.0, Contrabassoon -2.9, Violins I -2.9, celli -3.3 |
| qn 588 | 197 | Clarinet 1 -4.1, Clarinet 2 -4.0, Bassoon 1 -3.9, violas -3.5, basses -2.9 |
| qn 852 | 285 | Bassoon 2 -5.0, Bassoon 1 -3.3, Contrabassoon -3.1, celli -2.9 |
| qn 210 / 894 | 71 / 299 | both bassoons -4.2 to -4.4 |

`records/hp_to_cc11_clipped.txt` predicted 1.8 dB for these, at 0.22 dB per unit. The measured loss is 2-4 times that. Bassoon 1 at 384, for example: CC11 88 rises to 97 (+9 units), the envelope's +3.9 dB is gone, and the net is -3.8 dB. The bassoon's CC11 near the top gives about 0 dB per unit, as the c17 actor itself found for the removed Bassoon 1 lifts. The kept 25 (into the ff arrivals 309 / 310 / 909) arrive; three of them run over: Flute 2, Contrabassoon and Horn 1 are +2.6 to +3.1 dB over c15 at 309 and 909.

Fix:
- `HP_GAIN_TO_CC11`: convert a gain only on tracks whose measured CC11 slope across the arrival's range is at least 0.15 dB per unit. Take the slope from a range test or from c16 / c17 pairs like the one above. Bassoon 1, Bassoon 2, Contrabassoon, both clarinets and the violas fail it on these numbers.
- On those tracks, leave the gain in the envelope as the printed hairpin ramp (Dan's rule allows hairpins as ramps). Hold it with `cresc_trim_hold` to the next printed dynamic or rest, and release it at 2.8 dB/s or less (finale technique 77) so the slope guard stays clean.
- For the clarinets, the CC1 dynamic crossfade (`CC1_DYN_TRACKS`) is the other instrument-side route: make CC1 reach the f map value at the arrival.

This also answers which of the 28 dropped gains arrive short: all of them on winds (finding 1).

### 3. Second idea after the sub. p (bars 121-128, 277-284) and bars 137-138: rows put back in c17 put the low group over the espress. melody (m)

The first-render drops were answered with section rows that lift whole passages, including the p bars:
- Bassoon 1 [360, 420, +2.5], [828, 864, +3.0]
- Bassoon 2 [360, 420, +2.5], [828, 864, +2.5]
- Contrabassoon [360, 420, +2], [828, 864, +2]
- Double basses [360, 420, +2], [828, 864, +1.5]
- Violoncellos [360, 420, +1.5] (it overlaps [362, 396, -4])

Melody over the low group (Bassoons 1-2, Contrabassoon, celli, basses), as the median and lower quartile of 100 ms frames:

| passage | c15 | c16 | c17 |
|---|---|---|---|
| bars 125-128 (Violins I, Flute 1 and Oboe 1 espress. pp/p) | -0.9 / -1.8 dB | -0.9 / -2.1 | -2.9 / -3.8 |
| bars 121-124 (Violins I) | | +8.8 | +6.6 |
| bars 281-284 | -0.7 | -0.6 | -1.6 / -3.0 |

In bars 121-128 the basses (p) are the loudest stem, at -40.4 dB median against Violins I at -41.0. Bassoon 1 is at -42.9. In bars 137-138 (printed p) the celli and basses are 1.5-2.0 dB over c16 and c15.

Orchestration norm (inferred): an espress. violin line at p over a p bass line should lead by several dB. The bar means "0.9-2.3 dB under c16" in 121-140 / 253-288 come only from the f arrivals (finding 2). In the p bars the low group is now higher than c16.

Fix: delete these rows from `roles.json`:
- the nine above;
- Clarinet 1, Clarinet 2 and Bassoon 2 [108, 132, +2.5];
- Clarinet 1, Clarinet 2 and Bassoon 1 [576, 600, +2.0]. The last two overlap -3 rows, so the net is -1.

Recover the arrivals through finding 2's hairpin ramps. Check the master per bar against c17 afterwards; Movement I c58 and c60 lost bars when rows went without a replacement.

### 4. Bar 110 (qn 327-329): Flute 2's A6 is 10.5 dB over Flute 1's identical A6 and is the tutti's loudest moment (m)

In the ff tutti both flutes play the same notes (39 unison bars over the movement; median Flute 2 - Flute 1 = -2.3 dB). At the held, accented A6 (qn 327, MIDI 93) Flute 2 reads -20.4 dB in the 400 ms window, louder than Violins I (-22.8). Flute 1 reads -33.2. That window is the tutti's M max: -11.9 LUFS, 1.0 dB over c16 and 0.2 dB under the summit's peak.

The causes add up in Flute 2's favour:
- roles Flute 2 [312, 360, +3.5] against Flute 1 [312, 360, -1.8]: 5.3 dB apart in unison;
- `_ACC_BY` Flute 2 `add_loud` 10 against Flute 1's 0: CC11 107 to 117 on Flute 2, 108 on Flute 1;
- Flute 2 "Sus MAX" f layer +3.

The same three put Flute 2 5-6 dB over Flute 1 in bars 337-338 (-27.4 / -26.7 against -32.6 / -32.8; c16 had them within 2 dB).

Fix:
- Flute 2's roles [312, 360, 3.5] and [912, 960, 1.9]: set them to Flute 1's -1.8, or delete both flutes' rows.
- `_ACC_BY` Flute 2 (12, 10) to (5, 4). Its isolated-accent p90 is +5.4 now.
- Flute 2 `pitch_db` 93: -2 to -4.

Expected (inferred): Flute 2 at bar 110 about -27 dB, and the tutti's M max back to about -13. That keeps the summit clearly on top in peaks as well as in its 3 s mean (now 2.8 dB over).

### 5. Coda summit: the ff accented timpani strokes (qn 1008-1014) are softer than the f strokes before them (m)

The print: f at 996, a crescendo from 1002 into the ff roll at 1005, then accented half notes at 1008, 1010 and 1012 and the accented E-E stroke at 1014. Stroke peaks over the first 100 ms of the timpani stem:

| strokes | c16 | c17 |
|---|---|---|
| 996-1004 (printed f, role +2.5) | -18.4 to -21.6 dB | unchanged |
| 1008 / 1010 / 1012 / 1014 | -20.0 / -24.0 / -24.1 / -19.7 (velocity 121-125, role -4) | -24.8 / -23.1 / -23.2 / -24.3 (velocity 104, no role) |

1008 and 1014 lost 4.6 dB. The printed f approach is now 3-5 dB louder than the ff summit strokes. The timpani's bar means are -2.1 dB in bar 337 and -2.4 in bar 339. Violins I is 11.8 dB over the timpani at the summit (c16 11.4), so the strokes have room.

Fix:
- `VEL_SET["Timpani"]` 1008 / 1010 / 1012 / 1014: 104 to 114 (between the c16 and c17 readings: 17-21 units cost 3.1-8.8 dB on these round robins);
- delete the role [996, 1004.9, +2.5], a three-bar lift of a printed f under an ff.

Keep the summit roll and Dan's roll rule. No roll is the loudest stem in any roll bar of c17. The timpani is second only in bar 237, 0.5 dB under Violins II, the same as c16.

### 6. Celli's tenor countermelody in the ff tuttis, bars 112-114 and 312-314 (qn 333-342, 933-942): 2-4 dB under its own Sus MAX bars (m)

The countermelody is espress. at 312 / 912, with Bassoon 1 and Horns 3-4. Its slurred notes 332-342 play "Leg Slur MAX" at CC11 103-106 with no envelope offset. Celli bar means:

| bars | c15 | c16 | c17 |
|---|---|---|---|
| 105-110 (Sus MAX) | | | -30.9 to -34.1 |
| 112-114 (Leg Slur MAX) | -28.1 to -30.3 | -28.1 to -30.3 | -34.4 / -35.3 / -34.5 |

Bars 312-314 are the same (c17 -34.2 / -35.1 / -34.4). The c14 +6 lines carried this; c17 unwrote them. Its replacement, `row_dyn_db` "Leg Slur MAX" {f: +1.5, ff: +1.5}, gave 0.2 dB. Inferred: the region that sounds at CC11 103-106 is not labelled f or ff in the patch.

Fix: in the celli's `region_gain_db`, give "Leg Slur MAX" +3 on every layer that sounds at CC11 96-108. Try `row_dyn_db` with mf, f and ff, and check on a range pass of pitches 55-60 at CC11 104 that the region volume arrives, as Movement II c56 #2 did. Violins II already carries "Leg Slur MAX" f / ff +2.0: check it the same way.

Small item in this class: the violas' accented D4 at 978 (bar 327) loses the +14 of `CC11_ADD_SPANS` (974.8, 978): CC11 drops from 40 to 31 at the led note-on 977.414. Extend the span to 979.4.

## Role rows sorted by cause (177 in `build/roles.json`, m)

- **9 rows under 1 dB: delete.** Harp [216, 240, 0]; Violas, Violins II and celli [168, 312] and [864, 912] at -0.7 / -0.8; celli [648, 672, +0.5]. Violins I [1089, 1128, -0.5] is a pair with the solo's role (do-not-touch).
- **7 rows under two bars.**
  - Timpani [300, 300.5, -12] is a single-stroke volume cut, against Dan's rule: replace it with `VEL_SET` on that stroke.
  - Trumpets [994, 995.5, -4 / -5] and Horns 3-4 [990, 995.8, -4]: CC1 offsets on the brass's dynamic lane.
  - Oboe 1 [672, 676.5, +4]: a region gain for its pitch.
  - Horn 1 [0, 5.9, +4]: a phrase row, keep.
- **17 overlapping pairs: merge into one row each, or delete with their cause.** Examples: celli [552, 624, +3.2] with [576, 612, -7]; celli [360, 420, +1.5] with [362, 396, -4]; Bassoon 1 and Clarinet 2 [576, 600, +2] over -3; Timpani [264, 312, +2] with the -12 stroke; Violins II [996, 1004.75, -3] with [996, 1016, -2]; Violins I [1004.75, 1017, +2.5] with [1008, 1014, +2].
- **39 mapping rows on the tutti and summit spans.** Six tracks have one sign in both tuttis: Clarinet 2 -3, violas +4, Timpani +2.5, celli +2.5, Horn 3 +2, Oboe 1 -2.2 / -1.6. Move them into `dyn_trim_db` "ff" only after measuring the same track's other ff passages (bar 53, 209-224 at f / ff, 333). Otherwise keep them as slow rows. Flute 2's +3.5 / +1.9 are finding 4. Trombone 1, bass trombone and tuba +2 exist only in 105-120, which is correct: they rest in 289-324.
- **30 rows put back in c17 on the low group and clarinets: findings 2-3.** Replace them with hairpin ramps, not passage lifts.
- **The other 83 are passage and phrase decisions.** Solo, Horn 1, the trio's Violins II +4, the violas' development rows and the cut wind rows of the counterstatement. Not re-measured one by one here.

Slope (m, my own reading of the c17 envelope): 62 notes have a move of 1.5 dB or more within 0.5 s inside the note, away from printed hairpins and dynamics on their track. Most are role edges at the moved note-on of tutti entries (312, 912, 1005) and the summit's ramp from 1013 to 1014. That ramp is 2.6-6 dB on 13 tracks inside the 1012 half note, unprinted, but it was in c16 as well and does not dip the master: -15.5 dB at 1013.5-1013.95 against -16.1 at 1012.3-1012.9. The actor's guard counts 8, against stricter exclusions.

**Do not touch:** the celli's pp pizzicato at velocity 52 (even strokes, at the basses' level); the summit's margin over both tuttis on bar means and on the 3 s mean; trumpets 10 dB under the theme group in 105-120 and the theme group 5.9 dB over the low brass and timpani; Horn 1's pp G sharp levels (bars 1-2, 364, 372-376); the solo's role from 1040; the trio tune margins (Clarinet 1 +5.7 dB over harp and drone, the celli +4.5, the celli with Violins I +8.7, Oboe 1 +6.8); timpani rolls under Dan's rule; `CHORD_CC11` on the strings.

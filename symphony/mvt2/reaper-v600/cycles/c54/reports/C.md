# Cycle 54, critic C: dynamics over time; where the low-mid weight and the 70-112 Hz shortage come from (review of the c53 render)

## Method

I measured the c53 master, its 36 stems (with the post-render stem fix) and the delivered mp3 with my own numpy scripts, and read the data the render was made from in `cycles/c53/rendered_build/` (parts.json, mix.json, roles.json, level_fits.json, pitch_trims.json, score_config.py, mockup-events.tsv). Positions are score quarter notes converted on the c53 tempo map. Envelope values come from `build_reaper.py vol_points()` (through the actor's `lib53.load_build`, read only). EQ responses come from `tools/eqresp.py`. The two Brahms slow movements exist here only as stored measurements (`symphony/render/critics/c04/ref_brahms*_ii_musopen/metrics.json`). I did not use REAPER, changed no setting and deleted nothing. Each judgement is marked measured, simulated or inferred.

Scratch folder, left in place (110 MB, no simulated audio; one decoded copy of the delivered mp3): `/private/tmp/claude-501/mockup-loop/mvt2-c54-C/`.

Not read in full: `loop/HISTORY.md`, `mockup-kit/LEARNINGS.md` and the research FINDINGS were searched for the items this report touches (bass EQ history, template EQ, divisi), not read end to end.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 54 (last row: cycle 47), so there was no page range.

| Source | Where it applies | Does the render follow it |
|---|---|---|
| May 2021 HO manual, Divisi Instruments (p.89-90 as cited in `MANUAL-GAPS.md` item 8): divisi patches have Close mics only; the other mics come from the non-divisi patch at an adjusted level | Violas div, Violins II div, Violin I solo, Violoncellos div | No: the four tracks play Close alone and are exactly mono (finding 6) |
| May 2021 HO manual, text lines 2374-2375 (PDF page not checked): all instruments fade to silence on CC11 | Strings' niente, bar 66 (qn 223-226) | Yes: CC11 34 -> 12, stems fall 9-13 dB per quarter, the basses' pedal stays |
| EW template (FINDINGS lines 40-45, 176; `EW-TEMPLATE-PLAN.md` line 129): basses EQ is -2.4 to -3.6 dB at 205-250 Hz only; strings bus HPF 53 Hz; master HPF 42 Hz | Double basses `eq` in `build/mix.json` | No: the basses also carry an 80 Hz -6 dB bell from series 1 (c25) that the template does not have (finding 1) |

## Findings

### 1. The bottom octave is missing: the basses' EQ cuts the fundamentals of D flat 2 and E flat 2 by 5 dB and lifts their octaves

**Where.** Whole movement; most at the two ff tutti (bars 61-62, 79-81), bars 71-78 and the E flat pedal of bars 65-70. Track Double basses, `build/mix.json` `eq` and `loud_eq`.

**What is wrong (measured).** Share of total energy, master, in dB. Third-octave figures depend on the key (both Brahms movements are in E major, this one in A flat), so I use octave bands as well.

| | 56-112 Hz | 70-112 Hz | 112-224 Hz | 224-447 Hz | 140-355 Hz |
|---|---|---|---|---|---|
| Brahms 1/ii | -7.9 | -10.3 | -10.5 | -7.7 | -9.1 |
| Brahms 4/ii | -7.3 | -9.5 | -8.7 | -7.4 | -8.5 |
| c53 whole | -15.6 | -17.0 | -8.8 | -6.1 | -6.0 |
| bars 61-62 (ff) | -17.8 | -22.0 | -8.7 | -6.0 | -6.4 |
| bars 79-81 (ff) | -16.1 | -21.6 | -8.5 | -6.0 | -5.6 |
| bars 71-78 | -16.1 | -16.8 | -9.0 | -6.9 | -6.0 |
| bars 83-92 (coda) | -8.4 | -8.5 | -9.5 | -7.8 | -6.9 |

In octave bands the low-mid excess is 0 to 1.5 dB (112-224 Hz inside the Brahms pair, 224-447 Hz 1.3-1.6 dB over). The 3 dB figure for 140-355 Hz comes partly from where this key's tonic and dominant fall (A flat 3 at 208 Hz, E flat 4 at 311 Hz, both inside the band; the Brahms pair's strongest bands are 400 and 500 Hz, just above it). The large difference is below: 7-8 dB too little at 56-112 Hz over the whole piece, and 11-12 dB too little at 70-112 Hz in the two ff tutti. A mix with normal 150-350 Hz and no 60-110 Hz under it is one description of "mushy" (inferred).

**Where the two bands come from (measured, share of the master's band energy).**
- 70-112 Hz: Double basses 67 % whole piece (100 % in bars 23-30, 95 % in 71-78, 68-72 % at the ff tutti), Violoncellos 18 %, Bass clarinet 8 %, Timpani 5 %.
- 140-355 Hz: Violoncellos 28 % (65 % in bars 23-30, 39 % in 53-60), Horn 1 12 % (78 % in bars 7-14), Violas 10 %, Double basses 6 % (21 % in bars 71-78), Tuba 6 %. These are the fundamentals of printed lines.
- Hall returns: all four together 2.4 % of 140-355 Hz whole piece and under 0.2 % of 70-112 Hz (their 160 Hz high pass). The largest single case is R Winds, 10 % of 140-355 Hz in bars 31-36. The hall is not the source of either figure.

**The cause (measured from mix.json with `eqresp.py`).** Static EQ of the Double basses at this movement's bass pitches:

| | A flat 1 (52 Hz) | D flat 2 (69) | E flat 2 (78) | A flat 2 (104) | D flat 3 (139) | E flat 3 (156) |
|---|---|---|---|---|---|---|
| now (hp 35, bell2 80 Hz -6, bell 140 Hz +4.5, 228 Hz -3, 315 Hz -2.2) | -3.2 | -5.0 | -5.4 | -1.8 | +1.9 | +1.5 |
| at the two ff tutti with `loud_eq` (100 Hz shelf -3, 150 Hz +4) | -5.6 | -6.7 | -6.7 | -1.3 | +5.0 | +4.9 |

The basses play E flat 2 for 42 s and D flat 2 for 28 s (the dominant of A flat and the tonic of section B). The EQ moves 7 dB from each fundamental to its octave, and 11.6 dB at the ff tutti, which is where the 70-112 Hz share is lowest. On the stem, E flat 2 at qn 221.8 has its second harmonic 3.6 dB over the fundamental and D flat 2 at 204 has it 4.0 dB under; without the EQ the fundamentals would lead by 3.3 and 15.7 dB (the note at 204 lies under the `loud_eq`). The 80 Hz bell dates from series 1 (c25); c41 then added an 80 Hz +4 dB `loud_eq` row at qn 254-262 to undo it for three bars. This is the same pattern the scherzo found. Smaller cuts of the same kind: Tuba and Contrabassoon low shelf 70 Hz -4 dB (-2.5 / -1.7 dB at E flat 2); Harp high pass 80 Hz plus bells (-5 dB at E flat 2).

**Fix (simulated on the c53 stems: zero-phase EQ change on the Double basses stem, master = master + stem difference).** In `build/mix.json`, Double basses:
1. remove `bell2` 80 Hz -6 dB;
2. `loud_eq` first row: remove the `lowshelf` 100 Hz -3 dB band (keep the 150 Hz bell);
3. `bell` 140 Hz +4.5 -> +2.0 dB;
4. remove the second `loud_eq` row (qn 254-261.9, 80 Hz +4 dB), which only offsets the bell removed in step 1 (not in my simulation).

Result of steps 1-3: EQ at D flat 2 / E flat 2 -0.3 / -0.1 dB (+4.6 / +5.3), at D flat 3 / E flat 3 +1.0 / +0.5 (-0.8 / -1.1).

| share, dB | 56-112 Hz now -> new | 70-112 Hz | 112-224 Hz | 140-355 Hz |
|---|---|---|---|---|
| whole | -15.6 -> -11.2 | -17.0 -> -13.8 | -8.8 -> -8.9 | -6.0 -> -6.3 |
| bars 61-62 | -17.8 -> -12.1 | -22.0 -> -17.4 | -8.7 -> -8.7 | -6.4 -> -6.7 |
| bars 71-78 | -16.1 -> -10.1 | -16.8 -> -10.7 | -9.0 -> -9.5 | -6.0 -> -6.4 |
| bars 79-81 | -16.1 -> -10.3 | -21.6 -> -18.3 | -8.5 -> -8.7 | -5.6 -> -5.9 |
| bars 83-92 | -8.4 -> -6.9 | -8.5 -> -7.1 | -9.5 -> -9.9 | -6.9 -> -7.3 |

Bass stem +1.1 to +3.5 dB by passage, master +0.1 to +0.3 dB, master sample peak 0.581 -> 0.611. The coda is already at the recordings' share, so take the gain back there: `roles.json` Double basses `[273.9, 283.0, 2.0, 1.0]` -> `+0.5`, and add `[283, 304, -1.5]`. Step 1 alone gives 56-112 Hz -12.0 and 70-112 Hz -13.9 whole piece; a half step (bell2 -3) gives -13.9 / -15.6. The Tuba and Contrabassoon shelves change the whole-piece figure by under 0.1 dB; they can stay.

Do not cut the celli further for the 140-355 Hz figure: it does not move with any bass change (-6.0 -> -6.3), it is mostly printed fundamentals, and c53 already took 2.1 dB from the celli against the rest in bars 22-27.

### 2. Horn 1's theme (bars 7-14): the low notes are 4-7 dB weaker than the middle ones at one CC11 value, so the phrase starts on its softest note and the diminuendo of bars 12-13 turns round

**Where.** Horn 1, qn 17-42, alone over a pp accompaniment (the master follows the horn stem within 1 dB).

**What is wrong (measured, note bodies, dB).**

| qn | 17 | 17.5 | 18 | 19.5 | 20 | 22 | 23 | 24 | 26 | 27 | 30 | 31.5 | 32 | 34 | 35 | 36 | 37 | 37.5 | 38 | 39 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pitch | E♭3 | F3 | A♭3 | C4 | E♭4 | D4 | D♭4 | C4 | A♭3 | G3 | A♭3 | C4 | F4 | B♭4 | A♭4 | G4 | E♭4 | D♭4 | C4 | A♭3 |
| CC11 | 54 | 54 | 46 | 46 | 58 | 54 | 50 | 46 | 46 | 50 | 46 | 46 | 55 | 57 | 56 | 54 | 52 | 51 | 49 | 49 |
| stem | -38.8 | -40.3 | -42.7 | -36.9 | -34.7 | -35.3 | -39.8 | -39.3 | -41.4 | -41.7 | -43.9 | -37.0 | -35.6 | -33.7 | -39.3 | -41.1 | -37.7 | -39.3 | -40.3 | -41.7 |

- The first long note of the theme (A flat 3, downbeat of bar 7, 1.5 quarters, p dolce espr.) is 2.4-3.9 dB under its own pickup and 5.8 dB under the C4 that follows at the same CC11. The same at bar 11 (-43.9, then C4 -37.0). Level minus envelope: A flat 3 -51.9 / -52.5, G3 -51.7, C4 -44.2 to -48.3.
- From the A flat 3 of bar 7 to the E flat 4 two beats later the line rises 8 dB, and from the A flat 3 of bar 11 to the B flat 4 of bar 12 it rises 10.2 dB, where the score prints a one-beat hairpin and p to mp. The printed crescendo at 20-21 itself measures +1.2 dB.
- The diminuendo of bars 12-14 (mp at 34 to p at 39) runs -33.7, -39.3, -41.1, then **-37.7** on E flat 4, -39.3, -40.3, -41.7: 7.4 dB in the first two beats, then a 3.4 dB rise.

**Fix.** `build/pitch_trims.json`, Horn 1 (it already holds `"65"`, `"66": 4`, `"68": 3`, `"60": -2`, `"61": -2.5`, `"62": -3`): add `"56": 3` (A flat 3) and `"55": 2.5` (G3), `"67": 2` (G4), and raise `"68"` 3 -> 5 (A flat 4). Predicted note bodies: 18: -39.7, 26: -38.4, 27: -39.2, 30: -40.9, 35: -37.3, 36: -39.1, 39: -38.7; the arpeggio of bar 7 then rises 5 dB to its peak and the diminuendo runs -33.7, -37.3, -39.1, -37.7, -39.3, -40.3, -38.7. If the last A flat 3 (qn 39, the p goal) should not sit above the notes before it, give onset 39.0 a `note_trims` row of -1.5 or list it in `_skip_onsets`. `_all_arts` is true, so the trims reach the same pitches elsewhere (every other A flat 3, G3, G4 and A flat 4 on the track): check those with the simulation in `lib53.py` before the build. Inferred: +3 dB on a note without a CC11 change keeps its timbre.

### 3. The ff cadence (bars 79-81): the strings are softer at ff than at the f before it, Violins II sag inside bar 79, both violin sections sag through bar 80, and Violins II do not fall in the diminuendo of bar 81

**Where.** Violins I, Violins II, qn 259-271. Per quarter (dB):

| qn | 259 | 260 | 261 | 262 (ff) | 263 | 264 | 265 | 266 | 267 | 268 (dim.) | 269 | 270 | 271 (p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Master | -22.5 | -22.6 | -19.3 | -18.4 | -19.8 | -20.7 | -19.6 | -20.3 | -21.0 | -22.8 | -27.5 | -30.3 | -35.2 |
| Violins I | -29.3 | -28.2 | -27.6 | -29.7 | -30.6 | -29.8 | -29.3 | -33.0 | -35.0 | -32.9 | -38.2 | -39.2 | -45.3 |
| Violins II | -34.7 | -32.5 | -26.3 | -32.3 | -33.5 | -36.2 | -34.8 | -33.6 | -35.3 | -35.4 | -36.3 | -35.4 | -48.7 |

**What is wrong (measured).**
- All strings together: bar 78 (f, crescendo) -23.1, bar 79 (ff) -23.7, against -18.0 in bar 61 (ff). The master's ff arrival at 262 is +0.9 dB over the beat before and is carried by the entering winds and horns. Violins I's envelope steps from +11.2 dB at 261 to +6.7 at 262: `roles.json` `[250, 262, 2]` ends, `[262, 268, -1.5]` and `[261.5, 269, -1, 1]` begin, the hairpin gain of 261-262 (+3) ends.
- Violins II fall 3.9 dB from 262 to 264 inside "ff molto sostenuto". The re-bow piece from 263.921 carries CC7 101 (qn 264.0-265.75) and a volume row of -6 to -8.6 dB.
- Both sections lose 3 dB in the envelope across 266-267.6 (vol_db -1.0 -> -4.0 on Violins I, -0.5 -> -3.5 on Violins II); Violins I fall 5.7 dB from 265 to 267 and then rise 2.1 dB at 268, where the printed diminuendo starts (level fit +3.2 at 268).
- Violins II stay within 1 dB over 268-270 (CC11 at 270: 84 against Violins I 69; its hairpin 268-271 is still in `hp_curved`, and vol_db rises to +2.5 at 270.46), then fall 13.3 dB at the barline. In 269-270 they are the loudest stem, 2-4 dB over Violins I, whom they double an octave lower. The master's largest step of the diminuendo (4.9 dB) is at that barline.

**Fix.**
- `build/score_config.py`: add Violins II to the tracks that get `HP_CURVE["linear"]` for `(268.0, 271.0)`, as c53 did for Violins I; remove whatever lifts Violins II to +2.5 dB at 270.46 (the vol_db points `[269.75, 0.21], [270.4622, 2.5]`). Target: Violins II within 1.5 dB of Violins I's fall per quarter (about -35, -38, -40, -47).
- `roles.json`: Violins I `[250, 262, 2]` -> `[250, 268, 2]`; Violins II: remove `[262, 268, -1.5]`. Predicted Violins I at 262-265 about -28, level with its f in bar 78; master +0.4 dB in bar 79 (inferred from stem shares). The climax stays 5 dB louder on the master.
- Violins II re-bow piece at 263.921: CC7 101 -> 113 or the fitted row 3 dB higher (`build/rebow_fills.json`), so 264-265 read about -33.
- Find the rule that writes the 3 dB fall over 266-267.6 on both violin tracks and hold it flat to 268 (the note at 266 has no trim in roles, note_trims or level_fits; I did not find its source).

### 4. Hairpins that do not move on their own stem: 23 of 229, most of them inaudible; the celli in bars 56-58 are the audible case

**Measured.** For every hairpin in parts.json with the track sounding at both ends (229 of 341), stem level in the first and last third (at most one quarter): 114 crescendos, median rise 4.4 dB, 10 rise under 1 dB (5 fall); 115 diminuendos, median fall 5.4 dB, 13 fall under 1 dB (4 rise). The scherzo's mechanism exists here too: in 40 crescendos the volume envelope falls by more than 1 dB (soft trim tapering into a lower f trim, or a role), in 19 diminuendos it rises. But the scherzo's symptom does not: winds against strings rise through both big crescendos (bars 53-61: -14.2 -> -2.8 dB; bars 75-79: -8.3 -> +0.2 dB).

Audible cases:
- **Violoncellos qn 188-196** (bars 57-58, mf crescendo to f, "espr." at 190): stem -0.2 dB, envelope -6.4 dB while CC11 goes 73 -> 87. Per half bar from 184: -31.8, -35.7, -36.0, -32.8, -32.6, -35.1, then -30.3 at the f. Rows: `roles.json` `[186.5, 204, -3, 4]`, `note_trims` `"193": -3`, `pitch_trims` `"46": -5`. The master has a flat spot there (-25.8 at 184, then -27.1, -27.5, -26.5) inside the animando crescendo. Fix: `note_trims` `"193"` -3 -> -1 and the role `[186.5, 204, -3, 4]` -> `[186.5, 204, -1.5, 4]`; target celli at 194 no lower than at 190.
- **Violoncellos 180-184** -1.4 dB (the line falls to C2 at 182); no change asked.
- **Violas, Violins II, Violoncellos 218-220** (tremolo p to pp under the trombone's last note): +0.2 / +0.9 / -0.7 dB. The master falls 16 dB there on the trombone alone, so this is masked; no change asked.

Inaudible (stem 15-20 dB under the master): Clarinet 1 176-182 (0.0 dB, envelope -4.9: its soft trim pp 5.4 -> p 1.4), Bassoon 1 146-148 (+0.3), Bass clarinet 105-108 (-2.4).

### 5. The delivered mp3 meets item 6; the price is the size of the two builds

**Measured.** Master -22.9 LUFS, LRA 23.4 LU, p10-to-max short-term 30.3 dB. mp3 -19.8 LUFS, LRA 14.8 LU, p10-to-max 18.3 dB, true peak -1.6 dBTP. Ride gain between +3.2 dB (bar 61) and +17.0 dB (bars 1 and 92). No 2-quarter step of 2 dB or more on the master is reversed on the mp3. Bar 61 is the loudest on both (mp3 short-term -10.3 against -12.6 in bar 79). The morendo of bar 91 keeps 9.5 of 9.7 dB.

| | master | mp3 | kept |
|---|---|---|---|
| crescendo bars 53-61 | +21.8 dB | +13.3 dB | 61 % |
| build bars 71-79 | +17.7 dB | +9.5 dB | 54 % |
| fall bars 61-65 | -29.9 dB | -21.2 dB | 71 % |

On the mp3 the horn's bar 8 (p) reads -19.9 dB, level with bars 54-57 (mp to mf, strings, horn and winds: -18.2 to -20.6). That follows from RATIO 2.4 at LRA 14.8. RATIO 2.2 would return some of it (inferred) but took the span to 19.1 dB in c44 (limit 19). **No change asked.** If Dan asks for bigger crescendos, the room is 1.2 LU of LRA and 0.7 dB of span.

### 6. The mono divisi tracks matter in two places only; no patch change asked this cycle

**Measured.** All four divisi stems have left-right correlation 1.00 (side/mid -10.8 dB or lower). Where the master's image is narrowest, the divisi track is not the cause: bars 37-40 side/mid -9.8 dB with Violins II div 13.4 dB under the master (the narrow source is Flute 1, width 0.05); bars 23-30 are the widest passage of the piece (-4.3 dB) with Violas div 13.7 dB under the master. The divisi track carries the passage in bars 83-86 (Violoncellos div -6.4 dB re master, side/mid -9.4 dB) and bars 17-22 (Violin I solo -3.4 dB, side/mid -7.7 dB). The first is "4 soli" and the second a solo, where a narrow source is correct.

**If the lead wants the c53 test taken further (inferred, not simulated):** keep the DIV patch for Close and add the section patch's Main mic alone as a second layer about 8 dB under it (the manual's method). The 11.1 dB per-note spread c53 measured between the two patches then moves each note's total by about 0.3 to 1.5 dB, inside the lead's 1 dB condition after one trim for most notes. It needs a second instrument in the same Opus instance and a memory check (REAPER stood at 40 GB after c53), so it is a test, not a default.

## Checked, no finding (measured)

- Animando crescendo bars 53-60 on the master per half bar: -35.7, -36.3, -31.3, -30.4, -30.6, -28.8, -25.8, -27.1, -27.5, -26.5, -24.5, -23.1, -21.1, -21.1, -19.1, -16.1, then -13.8 at bar 61. One flat spot (bars 56-57, finding 4).
- Bar 47 fp: master -33.2 (147.5), -29.5 (148.0), -33.8 (148.5); Violins II, violas and basses fall 9-11 dB in half a quarter on CC11 (58 -> 44); the envelope moves under 1.5 dB.
- Bars 63-64: strings sf then diminuendo to p (stems -27 -> -40 to -48), Trombone 1 -22 to -26 dB throughout; its last note falls 21 dB in one quarter (1.38 s) to the printed p, 11 dB of it in the first 0.67 s (CC11 114 -> 52, CC1 106 -> 50, envelope 8 -> 0 dB between 218.19 and 218.5). The trombone has no hall send, so nothing is cut.
- Niente bar 66: Violins II -45.0, -49.4, -58.6, gone by 226; violas and celli alike; the basses' pedal -50 to -51 throughout. Violins II's down-bow at 223 is a 3.5 dB bump the violas and celli do not have (minor).
- Coda: bars 83-86 (ppp) -44 to -45.5, bars 87-89 (pp) -39 to -42, bar 91 -45.1, -47.2, -50.5, final chord -51 to -52 for 4 s (within 0.8 dB, no pulse), then -11 dB in 2 s and silence 1.5 s later.
- Loop pulsing: 13 notes of 6 s or more remain after the re-bows; autocorrelation of level at 3.95 s at most +0.18 (Contrabassoon 87). No finding.
- Soft ladder on the master: ppp bars 83-86 -45, pp bars 87-89 -40, p bars 15-22 -37 to -40: 5-8 dB from p to ppp, as the soft trims intend.

## Not measured by me

Join timing (S), S1 separation, accent attacks, phrase-end decays against recordings, the timpani rolls, Horn 2 208 and the open start sags (Violins I 80, Violins II 146 / 154, Violoncellos 253).

**Do not touch:** the four returns and their 160 Hz high passes; the celli's 170 Hz bell at +1.5 dB and the Harp's 200 Hz bell; the delivery settings (`RATIO` 2.4, `TOP_RATIO` 2.0, `rise_delay_s` 0.6); the fp at 148 on CC11; the niente of bar 66; the final chord's level rows and fade; the wind and horn rows of the crescendos 188-204 and 256-262 (winds rise against strings there); `HP_CURVE["linear"]` (268, 271) on the eight tracks c53 gave it to; the basses' 228 Hz and 315 Hz family bands and the 150 Hz `loud_eq` bell at the two ff tutti.

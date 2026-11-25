# Cycle 24, critic B: balance and levels (render c23)

## Method

All numbers come from the stem-fixed c23 render (`cycles/c23/render/`, 33 stems) and `build/parts.json` of 08:35, which matches the stem fix. Envelopes are per 10 ms: K-weighted plus eight bands. "A" is A-weighting built from those bands. "Re M" means a stem minus the master over the same window. The c22 comparison stems came from `cycles/c22/render/`, and PDF pages 2-4, 9, 14, 16 and 18 (printed pages 1-3, 8, 13, 15, 17) were checked against the data. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c24-B/`, which is deleted:
- re-run from the c23-B set: `fam.py`, `dynx.py`, `bardyn2.py`, `bardynmode.py`, `top21.py`, `oncov.py`, `softpeak.py`, `hpcons.py`, `tpch.py`, `rolls21.py`, `perc21.py`, `loopchk.py`, `accents.py`, `cbpitch.py`, `boom.py`;
- new: `hot.py` (stems more than 5 dB over their own median at the printed dynamic), `bloomscan.py` (soft notes that rise 5 dB or more inside the note at flat CC), `barstems.py`, `lane.py` (CC11, vol_db and level per step), `simall24.py` (envelope simulation of the fixes below).

## What holds (measured)

**Family ladders** (K medians of note bodies; unchanged from c22 within 0.4 dB):

| Family | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| Winds | -45.6 | -42.0 | -41.2 | -38.7 | -36.6 | -32.2 | -26.7 |
| Brass | -46.2 | -43.8 | -41.0 | -37.3 | -33.2 | -27.9 | -23.4 |
| Strings | -47.0 | -42.4 | -39.0 | -37.4 | -34.0 | -27.9 | -22.6 |

- p sounds like p in all three families: the spread is 1.8 dB. Bar level against the median printed dynamic: correlation 0.90, slope 3.66 dB per step.
- At f, one string section sits 2.6 dB over one woodwind and one trombone 5-6 dB over it. That matches Rimsky-Korsakov's resonance ratios.

**Trumpets.**
- On three-note chords, Trumpet 1 sits over Trumpet 2 by a median of +2.4 dB at f and at ff. Trumpet 2 sits under Trumpet 3 by -1.0 dB at f and -0.3 dB at ff (`tpch.py`, 28 bars). A slightly weak middle voice is not worth a change.
- The a2 trumpet theme at 167-170 has a melody onset margin of +3.5 dB.
- The pp trumpet entry at 448 sits 5-10 dB under the winds and strings and grows with the printed crescendo.

**Percussion and timpani** (unchanged from c23):
- Tam-tam 484: -8.6 K re M over 0.3-1.5 s.
- Crash 636: 5-20 kHz at -2.7 re M.
- Suspended cymbal: 5-20 kHz peak at -9.4 re M.
- No long timpani roll is the top stem. The opening ppp roll sits 3.5-6 dB under the basses, which meets the kit's 3-5 dB rule.

**Melody onset margins** (A, median and onsets covered):

| Bars | Median | Covered |
|---|---|---|
| 15-18 | +6.8 | 0 of 18 |
| 47-54 | +6.7 | 3 of 27 |
| 98-102 | +4.4 | 0 of 16 |
| 136-143 | +4.2 | 1 of 29 |
| 147-154 | +5.6 | 2 of 31 |
| 167-170 | +3.5 | 2 of 16 |
| 131-134 (Trombone 1 is in the theme) | +1.3 | 6 of 18 |
| 158-161 (tutti fff) | +0.1 | 4 of 10 |
| 56-63 | +2.9 | 7 of 21 (c23: +4.2 and 6 of 21; see finding 4) |

**Dan's checks.**
- Loop pulsing (`loopchk.py`): the same 8 unsplit notes of 6 s or more as in c23. The worst is still the bass clarinet at qn 11, with 100-300 Hz autocorrelation 0.81 and centroid autocorrelation 0.75. After the c23 B #4 cut it sits at -6.8 re M, no longer the top stem.
- Accents, 2-5 kHz in the first 80 ms minus the body, and the accent's level over its unaccented neighbours:

  | Family | 2-5 kHz median | Over +3 dB | Level over neighbours (median) |
  |---|---|---|---|
  | Brass | -5.5 | 2 of 126 | +3.3 |
  | Winds | -3.0 | 11 of 217 | +2.4 |
  | Strings | -1.3 | 10 of 177 | +3.0 |

  Violas 536 (+15.9) belongs to A's lens.

## 1. Bar 26: the ff tutti chord plays almost at the fff climax level, and the inner strings swell to the top of it (measured; fix simulated)

**Where.** qn 100-103.5, score p. 2 (bar 26).
- A three-beat ff accented chord for every instrument closes the bars 23-25 crescendo.
- At bar 27 the brass drop to f and the theme starts.

**Evidence.**
- Master K per half beat over 100.5-102.5: -12.3, -12.3, -12.6, -12.8, -12.6.
  - That is about 2 dB under bar 122 (fff with tam-tam, -9.5..-10.6) and 3.5 dB under bar 160 (-8.5..-9.5).
  - It is 4.5 dB over the median ff bar (-17.8 K) and 5.4 dB over the bar either side (bar 25 -18.6, bar 27 -18.7 RMS).
- Delivered mp3, maximum short-term loudness (S):

  | Passage | S max |
  |---|---|
  | Bar 160 | -10.1 |
  | Bar 122 | -11.0 |
  | Bars 167-170 | -13.2 |
  | Bar 26 | -13.9 |
  | Bar 82 | -14.9 |
  | Bar 140 | -14.7 |

  An exposition ff chord sits 0.7 dB under the third climax. That threatens the climax order 160 > 122 > 167-170.
- Where it comes from (`lane.py`): every string section and the oboe, horns and flute get a crescendo arrival gain at 100 (`hpgain` [88, 100]: strings +3, Oboe 1 +4, Horn 1 +2). On top of that come the accent fits and an ff CC11 of 114.
  - Violins II (D5+A♭5 dyad) and the violas (F4+B4) then bloom after the attack while vol_db stays flat at +1.5:
    - Violins II -22.0 -> -19.2;
    - violas -28.4 -> -22.1.
  - Violins II is the top stem in bar 26 (-7.6 A re M), over Violins I with the top B5.
  - Per stem against its own ff median:

    | Stem | Over its ff median |
    |---|---|
    | Violins II | +6..+9 |
    | Violas | +3..+9 |
    | Violins I | +2..+6 |
    | Tuba | +2.3..+4.5 |
    | Trombones | +1..+3 |

  - Violins II (-19.2..-19.9) and the violas (-22.1..-22.8) are louder here than at the bar-122 fff (-21.3..-22.2 and -24.2..-26.1).
  - Trumpets and trombones are within 1 dB of their own bar-122 fff levels.

**Fix.** Add level shapes in `build/score_config.py` `LEVEL_SHAPES`; the attack at 100.0 is untouched:
- Violins II and Violas: `[(100.35, 0.0), (100.9, -3.5), (103.2, -3.5), (103.6, 0.0)]`.
- Violins I: `[(100.35, 0.0), (100.9, -1.5), (103.2, -1.5), (103.6, 0.0)]`.
- Trumpets 1-3, Trombones 1-2, Bass trombone and Tuba: `[(100.3, 0.0), (100.6, -1.5), (103.2, -1.5), (103.6, 0.0)]`.
- This is level only, so a stem fix is enough.

**Simulated** (`simall24.py`):
- Master K 100.5-102.5: -12.3/-12.3/-12.6/-12.8/-12.6 -> -13.3/-13.8/-13.9/-14.3/-13.8 (about -1.3 dB). The attack window stays at -11.4.
- Violins II -19.2..-20.5 -> -22.7..-23.4, now under its fff level.
- Violins I is the top string again (-20.7 against Violins II -23.4 at 101).
- Expected delivered S max for bar 26 is about -15, which is 1.8 dB under 167-170. That figure is inferred from the master change; the delivery ride is slow.

## 2. Double basses F2: the 87 Hz fundamental is still 4-6 dB hotter than the neighbouring pitches, so every bowed F2 makes the master boom (measured; EQ response computed)

**Where.** Bowed F2 (MIDI 41) notes at qn 24/26 (bar 7), 36/38 (bar 10, the Lento pp chord), 148 (38), 252 (64), 268 (68), 360 (91), 378 (95), 440 (111).

**Evidence** (`cbpitch.py` and a per-note check, first 1.2 s of each note):
- Basses' 60-100 Hz minus their 160-300 Hz, median: F2 +5.0 (range +2.3..+7.0, 10 notes). The neighbours: E♭2 -0.8 (13 notes), E2 -2.6, G2 +2.2.
- Master 60-100 Hz re 300-1000 Hz while the basses hold F2: median -11.2 dB; at bar 10 (qn 36), -5.3. While they hold E♭2 the median is -17.4.
- The basses supply 99-102% of the master's 60-100 Hz on these notes.
- The 60-100 Hz band carries 56-77% of each F2 note's energy.
- The c18 bell (`mix.json` Double basses `bell2` 87 Hz -6 dB, 0.25 oct) cut it, but not enough. The kit's LEARNINGS 14 already listed F2 as +3.9 dB at the end of movement II.
- Bar 10 is a soft, exposed Lento chord, and there the F2 is heard as boom under the pp strings and bassoons (inferred).

**Fix.** `build/mix.json`, Double basses `eq`: change `bell2` to `{"band": "bell2", "hz": 87.3, "db": -10, "bw_oct": 0.15}`.
- RBJ peaking response, computed (change against the current bell):

  | Note | Hz | Change (dB) |
  |---|---|---|
  | D2 | 73 | +0.3 |
  | E♭2 | 78 | +0.4 |
  | E2 | 82.4 | -0.2 |
  | F2 | 87.3 | -4.0 |
  | F♯2 | 92.5 | -0.5 |
  | G2 | 98 | +0.2 |
  | F3 | 175 | 0 |

- Predicted per-note effect: the F2 notes drop 1.8-2.7 dB in plain level. The master changes by 0.1-0.3 dB (0.3 at bar 10). F2's 60-100 minus 160-300 goes from about +5 to about +1, inside the neighbours' range.
- Check ReaEQ's bandwidth definition against these numbers on the render. This is an FX change on one track: rebuild the basses' mix only, with no MIDI change.

## 3. Bar 84: the celli's sub. p G2 swells 8 dB inside the note and the basses rebound 7 dB, an unprinted hairpin in the most exposed bar of the development (measured; fix simulated)

**Where.** qn 332-335.5, score p. 7.
- After the ff tutti accent at 330, the celli hold G2 (4 qn) and the basses hold G1 (3 qn), both marked sub. p.
- The celli solo (mf) follows at 336.5.

**Evidence** (`lane.py`, 0.25 qn steps):
- Celli: -42.0 at 332, then -34.0 at 333.25-333.5, back to -41.6 by 335.
  - CC11 is flat at 46-50 and vol_db flat at -4.9..-3.5.
  - The note is a fresh first note on Leg Slur MAX (keyswitch at 329.25), so it plays the slow first-note layer (LEARNINGS 5-6).
- Basses: -30.6 at 332, a dip to -41.8 at 332.75, then up to -35.0 at 333.5. CC11 is flat at 44-46.
- The celli are the top stem through the bar (+0.3 K re M at the peak, `bloomscan.py`). Their peak of -34.0 is above the celli's own mf median (-35.6) for a printed sub. p.
- This is the largest swell among exposed soft notes in the movement: the only one over -1 re M with a rise of more than 5 dB.

**Fix.** `LEVEL_SHAPES`:
- Violoncellos: `[(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, 0.0)]`.
- Double basses: `[(332.9, 0.0), (333.15, -3.5), (334.3, -3.5), (334.8, 0.0)]`.
- Either shape ends before the celli's 336.25 pickup and the basses' 336 pizz.

**Simulated:**
- Celli 332-335 per quarter: -42.0 -42.9 -42.2 -42.1 -40.4 -39.0 -39.0 -39.9 -40.2 -39.8 -40.4 -41.8 -42.1. The rise is now 3 dB, not 8.
- Basses' peak -35.0 -> -38.5.
- Master over 333-334.25: -29.2..-31.8 -> -31.3..-33.9, so the sub. p reads as a drop.
- Alternative: play this one note on Sus MAX (`ART_SPANS` Violoncellos 331.7-336.0 "Sus MAX") so the bloom does not occur. That needs a rebuild of the celli track; the level shape does not.

## 4. Clarinet 1: two of the c23 post-render fills overshoot. qn 227 covers the Violins I melody, and qn 505 puts a 5.8 dB bump into the bar-127 solo (measured)

**Where.**
- qn 227 (bar 57, B♭4 at the end of the 226-227 slur in the p espr. counter-line, under the Violins I theme).
- qn 505 (bar 127, the accented E♭4 in the solo p cresc.).
- Both are `build/early_fills.json` Clarinet 1 entries, added or raised by the c23 stem fix (`auto_fills.py 23` merged for Clarinet 1).

**Evidence.** Join peak (8-frame smoothing, 0-0.4 s) minus the louder of the previous note (-0.45..-0.15 s) and the body (+0.45..+0.85 s), c22 -> c23:

| qn | Fill | c22 over neighbours | c23 over neighbours |
|---|---|---|---|
| 227 | new +3.7 | +5.2 | +7.0 |
| 505 | new +5.5 | +2.8 | +5.8 |
| 507.5 | 3.3 -> 6.7 | -1.1 | +3.0 |
| 409 | 0.1 -> 1.7 | | +4.5 (accent; acceptable) |

- At 227, Clarinet 1 A over the first 0.3 s went from -40.0 to -36.1. It is now 4.6 dB over the Violins I onset at 227, the worst covered melody onset in bars 56-63.
- That is why the 56-63 onset median fell from +4.2 to +2.9.
- At 505 the clarinet is the only voice above pp (-0.6..-0.9 re M). An accent of +5.8 over its neighbours is above the 2-4 dB accent rule. In c22 it was +2.8.
- The other new c23 fills land within -3.3..+2.4 of their neighbours: Clarinet 1 107.5/213/267/309.5/610/700, and the celli fills 48-687 (all -3.2..+3.5).

**Fix.** In `build/early_fills.json` Clarinet 1:
- Remove the 227 fill and add a note trim at 227 of -2.5 dB (`build/note_trims.json`; ramp over 227.0-227.6 back to 0).
- Set 505 to `db` 2.5 and 507.5 to `db` 3.5.
- Keep a note in `_auto` so `auto_fills.py` does not re-add them. Its hole test reads the join minimum, not the peak that follows it, so it adds fills where the sample's own rise already covers the join.
- Expected (inferred from the c22 levels): 227 about +4.5 over its neighbours and under Violins I; 505 about +3.

## 5. Oboe 1 bars 45-46: the p solo notes swell 8-9 dB inside each note to the oboe's own f level (measured; fix simulated)

**Where.** qn 178-182, score p. 4.
- The oboe solo p: A♭4 (1.5 qn), G4, F4 (2 qn), E♭4, all under one slur, with no hairpin.
- It is the exposition's twin of the bar-146 note fixed in c23 (B #3). The optional 180 shape from c23 was not made.

**Evidence:**
- CC11 is flat at 46 and vol_db at +4.0.
- A♭4 at 178: -44.9 -> -37.0 at 179.
- F4 at 180: -42.5 -> -33.7 at 181.75.
- The F4 peak of -33.7 is above Oboe 1's mf median (-37.9) and its f median (-34.6).
- Master over 180.75-181.75: -31.3..-33.7. The oboe sets the level of a p bar.

**Fix.** `LEVEL_SHAPES["Oboe 1"] += [[(178.3, 0.0), (178.75, -3.0), (179.4, -3.0), (179.6, 0.0), (180.25, 0.0), (180.6, -3.0), (181.0, -5.0), (181.9, -5.0), (182.0, 0.0)]]`

**Simulated:**
- Oboe 1 peaks: 179 -37.0 -> -40.0; 181-181.75 -35.3..-33.7 -> -40.3..-37.9. Each note now rises about 3 dB, a held p with a little shape.
- Master over 180.75-181.75: -31.3..-33.7 -> -33.1..-36.0.

## Measured, no change proposed
- **Hairpin consistency** (`hpcons.py`):
  - Bar 41: Oboe 1 against Oboe 2, and Clarinet 1 against Clarinet 2. Both pairs follow the same CC.
  - Bar 95: Violins I's crescendo is printed to ff at 387, and Violins II's to ff at 381, so the 3.5 dB Violins II lead at bar 96 is as printed.
- **Celli 696** (pp, bar 175): rises 8 dB from its first-note front, but sits level with the trombone chorale.

## Do not touch

- The family ladders and soft trims; the brass loud trims and trumpet trims; the a2 trumpet theme at 167-170.
- The percussion patches, gains, timing and the tam-tam bell.
- `TIMP_CC1_MAP` with the c21 tutti roll shapes; the opening timpani roles.
- The c23 B shapes (Horn 1/2 644-652, recap 520-536 roles, Oboe 1 579-582, bars 1-4 bass clarinet/celli) and the c22/c21 B shapes.
- The climax order 160 > 122 > 167-170. Finding 1 lowers bar 26 only and touches no climax window.
- The Cb 180 Hz body bell and the loud-EQ rows. Finding 2 changes only the 87 Hz `bell2`.

# Critic B, cycle 16: balance and levels (render c15)

Method. I measured K-weighted (BS.1770) 10 ms frames for the c15 master and all 29 stems, and A-weighted 50 ms frames for comparisons across registers. Everything is placed on score qn with the parts.json tempo map, which matches the c15 render (parts.json 19:27, render 20:05). I read the printed marks from `build/mockup-events.tsv` and the score pages, and the gain chain from parts.json `vol_db`/`dyn_curve` and mix.json. Fixes were simulated by scaling the stem frames by the proposed dB changes. Scripts are in `/private/tmp/claude-501/mockup-loop/c16-B/`. They are the c15-B set re-pointed at c15, plus `beatA.py` (A-weighted per beat, all stems), `holes.py` (solo notes 6 dB under both neighbours), `ccmap.py` (CC11 and total dB per printed dynamic), `bandstem.py` (per-stem band shares at the climaxes), `sim82.py` and `nl.py`.

## Delivery, c15 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -23.6 LUFS | -19.8 LUFS |
| LRA | 23.2 LU | 15.9 LU |
| True peak | -4.5 dBFS | -1.6 dBTP |
| p10-to-max short-term span | 26.6 dB | 18.7 dB |
| Limiter | | 1.9 dB |
| Climax (bar 62) rise over the 15-20 s before | 12.9 dB | 11.4 dB |
| 5 s level moves reversed by the ride | | 0 |

Every target is met. None of the fixes below touches bars 61-62, the loudest passage.

## What holds (measured)

- **CC11 mapping.** It is the same in every family: ppp 22, pp 34, p 46, mp 55-62, mf 72, f 88, ff 114 (`ccmap.py`).
- **pp and p across families.** Per-note medians (K):

| | pp | p |
|---|---|---|
| Winds | -46.9 | -39.2 |
| Brass | -47.9 | -38.8 |
| Strings | -47.3 | -41.8 |

- **pp accompaniment.** In eight soft passages every pp voice sits between -44 and -52 K.
- **Melody over its loudest accompanying stem** (A-weighted median per beat):

| Passage | Margin |
|---|---|
| Horn, bars 7-14 | +8.8 |
| Oboe, bars 15-16 | +10.7 |
| Oboe, bars 19-20 | +13.0 |
| Solo violin | +9.4 |
| Theme A | +8.4 / +9.1 |
| BCl | +6.6 |
| Flute, bars 37-40 | +5.4 (was +4.7) |
| CA | +4.5 / +7.5 |
| Theme B | +8.4 |
| Bars 70-74 | +7.7 |
| Bars 75-78 | +9.1 |
| Cl1, bars 85-86 | +11.6 |

- **The c15 B fixes did what was predicted.**
  - Cb pizz. no longer leads in bars 37-40.
  - In theme A, the printed mf at qn 82 is 3-4 dB K over the bar 24 swell (-29.7 against -33.0..-34.5).
  - The horn crest at qn 32-35 (-31.2..-32.8) is over the bar 8 swell (-33.5).
- **Timpani.** Every roll and stroke is 13-25 dB K under the master. No roll covers anything.
- **Climax families.** In bars 61-62 the brass carry 15-17% of the energy and the timpani 1%.
- **Cb against Vc.** In the soft bars 83-92 the Cb is -4..+0.6 dB K against the Vc.

## 1. Bar 82 cadence: the oboe's inner Ab4 is louder than the melody's Ab5 (measured; simulated)

**Where.**
- Bar 82, qn 271-273.5, the p chord that ends the climax section.
- The melody's last note, Ab5, is in Flute 1 and Violins I (both p >).
- Oboe 1 holds Ab4 (p >) in the middle of the chord.

**What.** K per 0.25 s from qn 271 (`sim82.py`):

| Part | Level, first 0.75 s | Level, next 2 s |
|---|---|---|
| Oboe 1 | -31.8..-35.7 | -37.7..-38.9 |
| Flute 1 | -44.7..-47.3 | -41.7..-50.5 |
| Violins I | -37.2..-40.0 | -38.9..-43.8 |

- The oboe is 0..+5.8 dB over the sum of flute and Violins I in every frame.
- A-weighted per half beat, qn 271-272.5: oboe 22.2 / 16.5 / 16.2 / 15.9; Vln I 16.4 / 13.8 / 14.2 / 11.7; Fl1 under 10.7 / 13.4 / 10.1 / under 6.8.
- On the chord that resolves the climax, the listener hears the oboe's inner note as the top line, and the flute's Ab5 is missing.

**Cause** (parts.json Oboe 1 `vol_db`):
- `early_fills.json` Oboe 1 "271": 7 puts +10.7 dB at 271.04, falling to +0.4 at 271.45. It stacks on the end of roles [268, 271, 4].
- The flute's Ab5 legato target falls 9 dB below its 270.5 note and keeps falling (Flute 1 vol_db is 0 from 270.75).

**Fix.**
- `build/early_fills.json` Oboe 1: "271" 7 -> 3. Do not remove it: the fill may be covering a sample sag, and the simulation with no fill opens a -48.5 hole in the first 0.25 s.
- `build/roles.json` Oboe 1: add [271, 274, -4].
- `build/note_trims.json` Flute 1: add "271": 3.

**Predicted.**
- Oboe minus (flute + Vln I): -3..-1 dB over the first second, then -1..+0.7. It was +0..+5.8.
- The top voice rises from -36.6..-42.7 to -36.1..-41.9.
- Bar 82 master level moves by under 1 dB. The soft-passage delivery numbers are unaffected.

## 2. Oboe solo, bar 46 downbeat: an 8 dB hole lets the cello's imitation cover the oboe (measured)

**Where.** Oboe 1 "dolce espr." p, qn 144: the Bb4 that starts the second slur of the solo (bars 45-47).

**What.**
- Per note (K, 0.08-1.0 s window): 143 -36.5, **144 -44.5**, 145 -36.9.
- `holes.py` finds this as the only note in any solo or melody span that falls 6 dB or more under both its neighbours.
- Frame by frame from qn 144 the oboe is at -43.8..-48.9 for 0.8 s.
- A-weighted at qn 144.0, the Violoncellos (p, imitating the oboe one bar later) are at 10.8 against the oboe's 8.8. That is the only beat of the solo where an accompanying part is louder.
- **Cause.** The note is a fresh attack after a 0.05 qn gap (slur break), at vel 53 on Sus. The c10 role [139, 151, 2.5] is the only lift.
- Oboe 1 Bb4 is 3 dB low at qn 145.5 as well (-39.8 against -36.9 before it).

**Fix.**
- `build/note_trims.json` Oboe 1: add "144": 7 and "145.5": 3.
- If the attack is still slow after that, also add `early_fills.json` Oboe 1 "144": {"db": 4, "pre_s": 0, "hold_s": 0.3}.

**Predicted.**
- qn 144 at about -37.5 K, within 1 dB of its neighbours.
- About +5 dB A over the Vc on that beat (was -2).

## 3. Bars 79-80: the tenor line (horns a2, celli, bassoon 1, all f) is still under the held viola and second-violin notes (measured; musical weight inferred)

**Where.** qn 262-265.5. Hn 1-2 a2 (rendered on Horn 1 with the unison boost), Vc and Bn1 play Db4-C4-Bb3-Ab3 in unison. Vla and Vln II hold ff notes.

**What.** A-weighted per half beat (`beatA.py`):

| qn | Line sum | Vla | Vln II |
|---|---|---|---|
| 262 | 27.8 | 27.8 | 25.8 |
| 262.5 | 28.1 | 28.9 | 30.2 |
| 263 | 26.2 | 30.0 | 29.5 |
| 263.5 | 27.0 | 30.4 | 30.4 |
| 264 | 27.2 | 29.7 | 31.1 |
| 264.5 | 26.0 | 28.8 | 31.1 |

- After the downbeat, the line is 2-5 dB under the louder sustained voice.
- The horn fades down the line. Per note (K): Db4 -30.9, C4 -33.0, **Bb3 -36.1**, Ab3 -31.4.
- The c15 Vc +2 (B #5) moved the line by about 1 dB (Vc+Bn1 K sum -28.2..-29.0, was -28.8..-30.7). That is not enough.
- The violas and Vln II carry the c12 climax lift [262, 268, 2.5].
- Inferred: in a real tutti, two horns, the celli and a bassoon in unison at f are the clearest voice after the tune (Adler and Rimsky both treat a doubled horn line as cutting through string harmony). Here the line reads as an inner murmur.

**Fix.**
- `build/roles.json`:
  - Horn 1 [262, 265.5, 3].
  - Bassoon 1 [262, 265.5, 2].
  - Violas and Violins II [262.5, 265, -2.5, 0.25]. This starts after the downbeat, so the climax attack is unchanged.
- `build/note_trims.json` Horn 1: "264": 2 (the Bb3).

**Predicted.**
- The line against the louder sustained voice moves from -2.1..-5.1 to about -1..+1 dB A.
- The bar 79 master changes by -0.3 dB or less, so the climax and limiter numbers stay where they are.

## 4. Theme A reprise, bars 71-74: printed p but as loud as the mp first statement (measured; expected difference inferred)

**Where.**
- First statement, qn 66-78: Vln I+II mp, from the bar 22 pickup.
- Reprise, qn 238-250: Vln I "p espr.", Vln II "p sul D", Vc "cantabile" p.

**What.**

| | First statement (mp) | Reprise (p) |
|---|---|---|
| Vln I K | -36.3 | -35.5 |
| Vln I+II A | 19.6 | 20.8 |
| Master momentary | -32.5 LUFS | -31.7 LUFS |
| mp3 momentary | -22.9 | -22.6 |

- The softer printed reprise is 0.3-1.2 dB louder.
- **Cause.**
  - Between CC 46 and CC 58 the string samples change level by only about 2 dB (`ccmap.py`). The p soft trim (+3.5) then takes back half of that.
  - Violins I [244, 262, 2] (c05) starts the second build-up lift at bar 73, two bars before the printed mp at qn 250.
  - The `LEAD_SPANS` soft hairpin gain (+3 dB) applies to the reprise swells but not to the first statement's swell at qn 68 (`SWELL_NO_SOFT_GAIN`).
- p and mp are a level apart. Inferred: a real section plays them 3-5 dB apart.

**Fix.** `build/roles.json`:
- Violins I [244, 262, 2] -> [250, 262, 2].
- Add [237.5, 250, -2.5, 0.5] to Violins I, Violins II and Violoncellos. The celli are included to keep their c08 relation to the melody.
- Leave the pp Violas, Cb, Cl2 and Bn2 alone.

**Predicted.**
- Reprise master about -34 LUFS, 1.5 dB under the first statement.
- Vln I K about -38.
- The melody's margin over the Vc is unchanged (+7.7 median).
- Check the mp3 too: the slow ride may give back part of the cut. The target is at least 1 LU under bars 23-26 in the mp3.

## 5. Bar 81: Bassoon 2 swells against the printed decrescendo and sits level with the melody (measured)

**Where.**
- qn 268-270, bar 81, ff > p.
- The melody descends in Fl1/Ob1 (octaves) and Vln I.
- Bn2 holds an Eb3 under the same decrescendo.

**What.**
- parts.json Bassoon 2 `vol_db`: 2.1 at 267 -> 5.8 at 268 -> **8.6 at 268.18**, then a straight fall to 0 at 270.95.
- That is a +8.6 dB rise at the start of a decrescendo, after roles [262, 268, 4] has ended. It sits on the `entry_leads` 268 note.
- K per half qn:

| qn | Bn2 | Fl1 | Ob1 | Vln I |
|---|---|---|---|---|
| 268 | -27.3 | -22.7 | -33.3 | -23.3 |
| 268.5 | -30.3 | -27.6 | -30.8 | -28.0 |
| 269 | **-29.3** | -35.0 | -31.8 | -33.3 |
| 269.5 | -33.6 | -38.2 | -35.3 | -32.4 |

- A-weighted at qn 269, Bn2 is at 24.9, against Ob1 25.0 and Fl1 22.1. A held inner note is level with the descending tune.

**Fix.**
- `build/note_trims.json` Bassoon 2: add "268": -5.
- Better, find the vol part that writes the 268.18 peak (it is not `hpgain`, `hp_soft` or `early_fills`: all are empty for this note) and stop it on a note that starts a decrescendo.

**Predicted.** Bn2 at -32..-38 K over qn 268-269.5, and about 20 A at qn 269, under the flute and oboe.

## 6. Low end at the climaxes: the Cb Db2 fundamental makes the 63 Hz band, and 112-180 Hz is thin (measured; the remedy needs a test)

**Where.** Bars 61-62 and 79-80, and the loudest 10% of frames.

**What.**
- 1/3-octave re 1 kHz, loud frames (`loudspec.py`):

| Hz | 63 | 126 | 159 |
|---|---|---|---|
| Mix | -7.4 | -10.1 | -10.5 |
| Dvorak | -25.6 | -1.1 | +1.7 |

- The 63 Hz excess over Dvorak is 4.7 dB in soft frames and 8.6 dB in mid frames.
- Per stem in bars 61-62 + 79-80 (`bandstem.py`):
  - 55-80 Hz is 97% Double basses.
  - 112-180 Hz is Cb 40%, BCl 24%, Timp 15%, Tuba 10%, Cbn 7%, BTbn 5%. The celli add nothing: they play above it.
- The master 55-80 Hz band is 2.7 dB over 112-180 Hz.
- The long-term 63 Hz band rose from -5.3 (c05) to +1.7 (c15) after c13 removed the Cb 90 Hz -5 low shelf. The reason was critic C's sub-bass target against the Brahms references, which are in E with B1 pedals.
- The Dvorak and Brahms references disagree by 27 dB at 63 Hz, so I cannot set a firm target. The shape is a concern in its own right: a boom at 69 Hz with a dip one octave up at the climax.

**Fix (A/B test).**
- `build/mix.json` Double basses eq: add {"band": "lowshelf", "hz": 80, "db": -3}. Band 1 is free on this track. Keep the 160 Hz +3 bell and the 25 Hz high pass.
- Pass if all of these hold:
  - loud-frame 63 Hz falls by at least 3 dB;
  - the 126/159 Hz bands do not fall;
  - the Cb-Vc K balance in bars 83-92 stays within -5..+1 dB;
  - the 20-100 Hz band share stays at or above -18 dB.
- Do not change the Cb gain or its soft trims for this.

## Do not touch

- The CC11 dynamic map and the soft-trim table, including the per-track overrides.
- `deliver_master.py` and TARGET_I; the delivery numbers are on target.
- The c15 B fixes:
  - `SWELL_NO_SOFT_GAIN`;
  - Cb pizz. role 2;
  - Fl1 Bb4/C5/Db5 trims;
  - the bar 30 Vc/Cb cadence roles;
  - the Vc [262, 265, 2, 0.25].
- The bars 61-62 wind and brass roles, and `_all` [204, 212, -1].
- The timpani levels, `TIMP_HP_DB_FACTOR` and `TIMP_TIE_STROKES`.
- The c14 soft solo roles and the coda `_all` -2.
- The Tbn1 marcato velocities and shape.

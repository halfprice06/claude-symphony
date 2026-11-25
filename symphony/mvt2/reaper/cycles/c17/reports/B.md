# Critic B, cycle 17: balance and levels (render c16)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for the c16 master and all 29 stems, and placed them on score qn with the parts.json tempo map (parts.json 21:16, render 21:17). Printed marks come from `build/mockup-events.tsv` and score pages 5-8. The gain chain comes from parts.json `vol_db`/`dyn_curve`, mix.json, roles.json, pitch_trims.json and early_fills.json. I simulated fixes by scaling stem frames. The scripts are in `/private/tmp/claude-501/mockup-loop/c17-B/`: the c16-B set re-pointed at c16, plus `share.py` (family shares), `hns.py`/`simhn.py` (horns at the climaxes), `decay.py` (held-note decay), `loudest.py` (loudest stem per beat), `simcoda.py`, `lowbr.py` and `fl.py`.

## Delivery, c16 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -23.0 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.1 LU (target 14-16: 0.1 over) |
| True peak | -2.9 dBFS | -1.6 dBTP |
| p10-to-max short-term span | 27.2 dB | 18.9 dB |
| Limiter | | 3.2 dB (largest gain reduction 3.7 dB at qn 207.87) |
| Climax rise over the 15-20 s before | 13.5 dB | 11.7 dB |
| 5 s moves reversed by the ride | | 0 |

The qn 207.94 sample peak (-2.94 dBFS) is a sum of many stems in phase. In simulation, a -4 dB dip on the Violins II join alone lowers it by only 0.17 dB, so I do not propose a fix for it here.

## What holds (measured)

- **CC11 map.** It is the same in every family: ppp 22, pp 34, p 46, mf 72, f 88, ff 108-114.
- **Family medians per note (K):**

| | pp | p | f |
|---|---|---|---|
| Winds | -46.8 | -39.1 | -31.7 |
| Brass | -47.9 | -38.8 | -32.1 |
| Strings | -47.1 | -41.6 | -31.7 |

- **Strings against winds at ff.** Bars 61-62, A-weighted: Vln I 32.2 against Fl1 29.4 and Ob1 29.3, so +2.8 dB. Rimsky (rimsky-principles.txt p51-52, book pp. 33-34) says one string section equals two winds in forte, which is +3 dB. That relation is correct.
- **Solo margins over the loudest accompanying stem (A, median):**

| Passage | Margin |
|---|---|
| Horn, bars 7-14 | +8.8 |
| Oboe, bars 15-16 | +10.9 |
| Solo violin | +9.7 |
| BCl | +6.6 |
| CA, bars 47-51 | +7.6 |
| Ob, bars 45-46 | +7.4 |
| Cl1, bars 85-86 | +11.0 |
| Horn, bars 67-70 | +2.3 to +20 (falls with the printed decrescendo to pp) |

- **pp accompaniment.** In all eight soft passages, every voice sits between -43 and -53 K.
- **Timpani.** No roll covers anything.
- **c16 B fixes.**
  - Bar 82: the oboe no longer leads.
  - Bar 79: the tenor line sum (Hn1+Vc+Bn1) is at +3.7..-1.1 dB A against the louder held voice. That is my target, not an overshoot, when A-weighted.

## 1. Horns at f are 4-6 dB too weak at both ff climaxes, under single woodwinds and under the mf trombones (measured; norm from Rimsky)

**Where.**
- Bars 61-62 (qn 204-212): Hn 1-2 (Horn 2 plays) and Hn 3-4 at f, with ff winds and strings and mf trombones/tuba.
- Bars 79-80 (qn 262-268): Hn 1-2 a2 at f (on Horn 1) and Hn 3-4 at f, with ff winds.

**What.** A-weighted per span (`hns.py`):

| qn | Hn2 | Hn3 | Hn4 | Hn1 | Fl1 | Ob1 | Tbn2 (mf) | BTbn (mf) |
|---|---|---|---|---|---|---|---|---|
| 204-208 | 23.3 | 22.2 | 22.4 | | 28.2 | 29.9 | 24.9 | 27.4 |
| 208-212 | 24.3 | 25.2 | 22.0 | | 30.4 | 28.5 | 25.4 | 26.4 |
| 262-265 | | 19.4 | 21.3 | 24.0 | 26.9 | 26.1 | | |

- **Family share in bars 61-62** (`share.py`, A):

| Family | Share |
|---|---|
| Woodwinds | 47% |
| Strings | 36% |
| Low brass | 10% |
| Horns | 6% |

- In bar 79, Horn 3 is under Bassoon 1 (19.4 against 23.5).
- **Norm** (rimsky-principles.txt p51, book p. 33): in forte, "Horn = 2 Clarinets = 2 Oboes = 2 Flutes", and "Trumpet = Trombone = Tuba = 2 Horns". Page 41 (book p. 23) says horns should be marked one degree stronger than the other brass to balance them.
- With the horns one degree under the winds (f against ff), each horn should be about level with one wind. Here each horn is 4-6 dB under. The horns should also be about level with the mf trombones, and here they are 2-5 dB under.
- The four-horn chord, which gives a tutti its weight in the middle register, is the weakest family at both climaxes.

**Fix** (`build/roles.json`):

| Track | Change |
|---|---|
| Horn 2 | [204, 212, 2] -> [204, 212, 5] |
| Horn 3 | [204, 212, 2] -> [204, 212, 5]; [261.5, 271, -1] -> [261.5, 268, 2, 0.5] plus [268, 271, -1] |
| Horn 4 | [204, 212, 2] -> [204, 212, 5]; [262, 268, 2] -> [262, 268, 5, 0.5] |
| Horn 1 | [262, 265.5, 3] -> [262, 268, 4, 0.5] |
| `_all` | [204, 212, -1] -> [204, 212, -1.4], to hold the climax level and the limiter |

Do not touch the low brass: the C #1 low-octave roles stay.

**Predicted** (`simhn.py`):
- The horns reach 25-29 A at bar 61-62 and 24-28 at bar 79, within 1-4 dB of the loudest single wind and level with the trombones.
- The master rises 0.3-0.5 dB A before the `_all` change, and about 0 after it.
- The bar 81 decrescendo is unchanged, because the lifts end at 268 with a 0.5 qn ramp.

## 2. Bars 77-78: Bassoon 2's inner E flat 3 is the loudest stem in the orchestra on two beats (measured)

**Where.**
- qn 256-262. The tune is in Fl1 and Vln I, p/mp crescendo to f at bar 78, with Cl1 and Vln II in thirds.
- Bassoon 2 holds harmony notes: Eb3 at 256, Fb3 at 259, Eb3 at 261.

**What.**
- Loudest stem per beat (`loudest.py`, A):
  - qn 257: Bn2 27.5 over Vln I 25.1 and Fl1 24.0.
  - qn 261: Bn2 28.1 over Vln I 26.2.
  - At 256 and 259, Bn2 is second, 2.5-3 dB under Vln I.
- K per note: 255 -36.9, **256 -30.8**, 259 -30.7, **261 -25.9**. The qn 261 Eb3 is the loudest wind note in bars 75-78, and louder than the ff winds in bar 79 (-29..-32).
- **Cause.** Bassoon 2 `vol_db` steps to +8.8 at 256.25, to +12.6 at 258 and to **+12.8 at 261.95**. These gains stack on each other:
  - the pitch_trims Eb3 (51) +6 from c13, which was made for soft passages;
  - the C #1 role [258, 269, 3, 1];
  - the f trim +2;
  - the crescendo gain.
- The c16 actor already skipped the same trim at qn 268 for the same reason (B #5).

**Fix.**
- `build/pitch_trims.json` Bassoon 2 `_skip_onsets`: [268] -> [256, 261, 268].
- If qn 257 is still over the tune after that, add roles Bassoon 2 [256, 258, -2].

**Predicted.**
- Bn2 256 about -36.8 K and 261 about -31.9 K.
- A-weighted at 257: 21.5 against Vln I 25.1. At 261: 22.1 against 26.2.
- Bars 77-78 master: -0.2 dB.

## 3. Bar 79: Flute 1's ff B flat 6, the top of the tune, fades 10 dB during the held note, then jumps 13 dB at qn 266 (measured)

**Where.** Flute 1, qn 262-266. The ff Bb6 is tied over the bar line and doubles Vln I at the climax of the reprise.

**What.**
- K per 0.25 qn (`fl.py`): 262.25 **-23.8**, 263.0 -28.2, 264.0 -31.2, 265.0 **-34.5**, then at 266.0 (F6) **-21.4**.
- `vol_db` on the note only moves from -3.8 to -2.5 and back, so the fall is in the sample.
- `decay.py` checked every f/ff held wind note of 2 qn or more for its level change minus the planned volume change. The median is -0.3 dB, and this note is the outlier at -7.2. No hairpin is printed.
- The Vln I unison rises from 28.6 to 32.9 A, so the summed top line holds. But the flute colour is gone by the second beat, and it comes back as a 13 dB jump on the F6. Inferred: this is heard as the flute dropping out and re-entering.

**Fix.**
- `build/roles.json` Flute 1: add [262.6, 263.5, 3] and [263.5, 265.9, 7]. They chain under `ROLE_CHAIN`.
- Leave the auto fill at 266 as it is.

**Predicted.**
- The held note falls by at most 4 dB (about -24 to -28 K).
- The step into 266 drops from 13 dB to about 6 dB.
- Bar 79-80 master: +0.2 dB or less.

## 4. Coda, bars 87-88: Clarinet 1's line drops into the pp string and horn chord after the breath (measured)

**Where.** qn 286-292.
- Cl1 continues its bar 85 dolce solo at pp.
- Vln II (Ab4), Vla (unis., sul C) and Hn 3-4 (con sord.) enter pp under it.

**What.**
- Cl1 minus the loudest other stem, A per half beat (`simcoda.py`): median **+1.7**, minimum **-2.8** (qn 288.5, under Vln II).
- In bars 85-86 the same was +9..+17.
- At the bar 87 downbeat the violas (8.8) and Horn 4 (7.7) are within 0.3-1.4 dB of the clarinet (9.1).
- Cl1 notes (K): 286 -44.3, 289 -45.7. Vln II pp carries a +9 dB soft trim (Vln I +2).
- The coda `_all` -2 lowers every track, so it does not change this relation.

**Fix** (`build/roles.json`):
- Clarinet 1: add [286, 292, 2.5].
- Violins II: add [286, 292, -2].
- Violas: add [286, 292, -1].
- Leave the Horn 4 note trims (286 -5, 289 -3) as they are.

**Predicted.**
- Margin median +4.9, minimum +1.7 (was +1.7 / -2.8).
- The coda master stays within 0.3 dB, so the pp ending and its ride are unaffected.

## 5. Bars 19-20: the oboe's p solo swells to the woodwinds' f level (measured)

**Where.** Oboe 1, qn 54-59, p with an untargeted < >, over pp strings.

**What.**
- K per note: 54 -44.5, 55.5 -34.2, **56 -31.4**, **57 -32.8**.
- The winds' f median is -31.7 and their mp median is -36.8. The swell should reach about mp, one level over p.
- The same oboe's swell in bars 15-16 peaks at -34.4.
- **Cause.** CC11 rises 46 -> 68 (mf), and on top of it `vol_db` reaches **+11.3 at 56.25 and +13.9 at 57.15**. That is roles [54, 60, 2], hpgain [54, 57, 3], the soft-lead hairpin +3, the p soft trim, and the early fills at 55.5/56/57.
- Margin over the loudest accompaniment: +14.5 at qn 58 and +18.7 at qn 56 (A). The other soft solos sit at +7..+11.

**Fix.** `build/roles.json` Oboe 1: add [55.5, 58.5, -3]. It chains inside [54, 60, 2].

**Predicted.**
- Peak about -34.5 K, level with the bars 15-16 swell.
- Margin about +11.
- The quiet start at 54 is unchanged.

## 6. Horn inner voices: a missing beat in bar 80 and a pp horn over p strings in bar 30 (measured)

**Bar 80, qn 267-268.**
- Horn 4's printed Ab3 (qn 265, 3 qn, in mockup-events.tsv) is missing from parts.json. Horn 4's level there is 4.0 A at qn 265-268, against 20-22 for the other horns.
- **Cause.** `find_unisons()` in `tools/score_to_parts.py` (line 2387) dropped it as a unison copy of Horn 1's Ab3 (265-267). It drops a copy that outlasts the kept note by up to 1.0 qn. For that last beat of the bar, the f horn chord has no Ab3.
- **Fix.** Change the test `x[1]["end"] > keep[1]["end"] + 1.0 + EPS` to `+ 0.25 + EPS`, so that this pair is left (both play). Check the stderr unison log for any other pair the change affects.

**Bar 30, qn 87.5-89.**
- Horn 4 (pp) is the loudest stem: 10.6 / 7.5 / 6.1 A against Violins I at 7.8 / 7.2 / 5.6, which are printed p >.
- Rimsky (p51) puts one piano wind level with one string section. A pp horn should therefore sit under a p section.
- **Fix.** roles.json Horn 4: change [0, 17, -2] to also cover the cadence. Add [86, 90, -3].

## Do not touch

- The CC11 map and the soft-trim table.
- The string-to-wind balance at the climaxes, which matches Rimsky.
- The C #1 low-octave roles and `loud_eq`.
- `deliver_master.py`.
- The c16 B changes: bar 82 oboe, Ob1 144, the bar 79 tenor-line roles, the reprise -2.5.
- Timpani levels, `TIMP_HP_DB_FACTOR` and `TIMP_TIE_STROKES`.
- The soft solo roles in bars 7-14, 17-22, 31-36, 41-51 and 85-86.
- The Tbn1 bar 63 marcato levels.

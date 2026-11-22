# Cycle 30, critic C: dynamics over time (lens C2), on the c29 render and its delivered mp3

Sources:
- the c29 stems, returns and master (`cycles/c29/render/`), with `cycles/c29/build_render/` (parts.json, roles.json, score_config.py);
- the delivered `cycles/c29/scherzo-mockup-c29.mp3`, decoded at 48 kHz and aligned to the master at +238 samples;
- the c28 master and the c18 stems for comparison (c18 levels lowered by 3 dB for `global_gain_db`).

Method:
- Levels are K-weighted (BS.1770) mean power in LUFS-style dB.
- "Bar mean" is the level over the whole bar. "Mmax" is the loudest 400 ms window in the bar.
- Times come from the parts.json tempo map; bar b starts at qn 3(b-1).
- Every hairpin in `build/mockup-events.tsv` (130 of 1.5 qn or longer) was measured on the summed stems of the staves that carry it and on the mp3.
- Delivery simulations ran a scratch copy of `tools/deliver_master.py` on the c29 master, with an environment override for MOM_CAP_ABOVE and edited copies of parts.json `ride_trims`. Nothing in `tools/` or `build/` was changed. The spec was measured with `cycles/c23/actor_scripts/spec23.py`.

My scratch folder `/private/tmp/claude-501/mockup-loop/scherzo-c30-C/` has been deleted.

## Manual notes

MANUAL-READING.md has no row for c30, so I did no scheduled reading. I used MANUAL-GAPS.md and `guides/eastwest-hollywood-orchestra/DIGEST.md` for the controller pages behind the fixes below.

| reading (PDF page) | where it applies | does the render follow it |
|---|---|---|
| CC11 shapes loudness over time and crossfades the layers; CC7 or the fader sets each track's ceiling (p.63-64, p.151; MANUAL-GAPS "c25 result") | Horn 1's last G sharp (finding 2) carries a +6 dB volume-envelope row on top of CC11 +14. | Partly. The level of the last note is set in the envelope by a one-note row, which Dan's rule of 2026-11-11 forbids. |
| Brass sustains: CC1 crossfades 4 dynamic layers, so CC11 is plain level on the horns (p.101; MANUAL-GAPS #4) | The fix for finding 2 moves the level into CC11 and keeps CC1. | Yes, CC1 is unchanged by the fix. |
| Timpani rolls: CC1 crossfades 8 dynamic layers (p.124). MANUAL-GAPS #7: recorded crescendo rolls (Felt Cresc) are not used. | The pp < f roll of bars 205-208 (finding 3) gets its crescendo from CC1 56 -> 88 and CC7 21 -> 50, but its envelope jumps at the start of the crescendo and then falls. | The CC side follows the manual. The envelope works against it. #7 stays untried; not for this cycle. |

## What passes on c29 (measured; keep)

- **sfp < at bar 301 (qn 900-910).**
  - On the master the sf lasts 900-900.5 (-18 dB). It falls to the p by 901.5 (-26.8, a 9 dB drop) and holds the p to 906, then rises to -19.4 at 910.5 (+7.4 dB).
  - The strings' hall return falls from -34 to -49 dB under the p, so the sf rings into it (S3).
  - On the mp3: sf -8.6, p -12.9, ff -8.9. c26's one-beat hiccup is gone.
- **Both sub. p's (S3).**
  - Bar 121 (qn 360): the tutti ends before the rest, R Strings decays without a step (-44 -> -47.7 dB), and the p enters 15 dB under the ff on the master (8.5 LU on the mp3).
  - Bar 277 (qn 828): 9 dB on the master, 7.5 LU on the mp3.
- **The fugato's growth.** Bars 59 -> 72 rise 16 LU on the mp3 (-25.4 -> -9.4).
- **The accelerando's crescendo.** Bars 241 -> 252 rise 6 LU (-20.8 -> -14.7).
- **The codetta's fade.** -18.6 -> -24.9 LU over bars 225-240.
- **The held chord's fade.** Bars 361-364 (pp >): the stems fall 13.4 dB, the mp3 falls 7 LU.
- **Timpani rolls with a printed crescendo.**
  - Bars 101-103 (qn 300-309): +23 dB from p to f, ending 10.6 dB under the master.
  - Bars 301-303 (qn 906-909): +5.8 dB.
  - Rolls with no crescendo settle: 384 and 852 fall 5-6 dB.
- **No loop pulsing.** I measured each held note's level envelope, detrended, and its autocorrelation at 3.95 s:

  | held note | autocorrelation at 3.95 s |
  |---|---|
  | Violins I + Violin I solo G sharp, 1089-1128 | +0.02 |
  | Horn 1 G sharp, 1101-1128 | +0.26 |
  | Violins II harmonic E6, 420-445 | -0.20 |
  | Horns 3-4 drone, 456-504 | -0.13 |

- **Hairpins in general.**
  - Median crescendo +4.8 dB, median diminuendo -5.7 dB on the stems that carry them.
  - Of the 23 that read under 1 dB or reversed, most are windows that start on an sf or accent, or stretch over a rest. The one with an audible cause is finding 3.
- **The delivery spec.** All six items pass (-14.1 LUFS, -1.2 dBTP, lead +0.60 LU, f -> ff 2.23 LU, p10 -21.0, LRA 11.4, limiter 3.9 dB).

## Findings, ranked by what a listener would gain

### 1. On the mp3 the p and pp solos are as loud as the f passages. The quiet-passage lift raises their peaks up to knee + 3 dB, so the horn call, the clarinet and violin solos and Hn 1's espress. tail sit level with the second idea's f and the f hemiola. The close also gets 3.7 dB more lift than the held chord before it (measured; fix simulated)

Where: the soft solos and the f passages below, on the mp3 (Mmax):

| bar | what is printed | Mmax |
|---|---|---|
| 4-5 (qn 9-15) | Horn 1's call, pp < p > | -10.3 / -10.4 |
| 82 (qn 243) | Clarinet 1 dolce | -10.8 |
| 162 (qn 483) | Clarinet 1, the trio tune, p < | -11.2 |
| 179 (qn 534) | Violins I + celli, mp | -10.4 |
| 350-351 (qn 1047-1053) | the Violin I solo, pp < > ("sempre pp" in Flute 1) | -11.6 |
| 357 (qn 1068) | Horn 1 espress. p | -12.7 |
| 41 | second idea, f | -10.7 |
| 101 | f hemiola, first tutti bar with brass | -11.3 |
| 197 | trio, f | -12.0 |
| 209 | trio, f | -11.7 |
| 105 | ff tutti | -8.7 |

What is wrong (measured):
- On the master the horn call is 9.2 dB under bar 101 (bar means -34.0 / -24.8 dB). On the mp3 it is 0.1 LU over it (bar means -11.7 / -11.8).
- The delivery gives bar 4 +22.3 dB and bar 101 +12.9 dB. The violin solo bars get +19.1..+19.5 dB, the ff tutti +10.8.
- The source is `deliver_master.py`'s momentary cap. `MOM_CAP_ABOVE = 3.0` lets a lifted momentary peak reach knee + 3 dB, which is the level of the f passages.
- A p horn solo 2.6 LU under the ff tutti and level with the f, and a pp violin solo louder than the trio's f, turn the movement's soft-loud contrast into one level for anything exposed.
- The same lift grows as the close thins: +21.7 dB at bar 361, +24.3 at 372, +25.4 at 376. Bars 368-374 sit 4.2-4.4 LU over bar 364 (finding 2 has the other half of this).

Fix (delivery only; no REAPER):
1. `tools/deliver_master.py`: `MOM_CAP_ABOVE, MOM_CAP_SMOOTH_S = 0.0, 0.5` (was 3.0). Add a scherzo comment with the numbers below.
2. `build/score_config.py` `RIDE_TRIMS`, four rows; then re-run score_to_parts. Only parts.json `ride_trims` changes, so no build is needed.
   - Horn call: `[(5.0, 0.0), (6.0, -2.0), (16.5, -2.0), (18.0, 0.0)]`
   - Violin solo and Hn 1's tail: `[(1043.0, 0.0), (1044.0, -2.0), (1079.0, -2.0), (1080.0, 0.0)]`
   - The close: `[(1088.0, 0.0), (1092.0, -1.0), (1100.0, -2.5), (1128.0, -2.5)]`
   - The existing 305-320 row `[(914.6, 0), (915, -1.0), (959, -1.0), (961, 0)]` deepened to -1.5. This keeps the summit lead, which the cap alone takes to +0.55.

Simulated on the c29 master (all six spec items pass):

| | c29 mp3 | with the fix |
|---|---|---|
| I / TP | -14.1 / -1.2 | -14.1 LUFS / -1.2 dBTP |
| summit lead | +0.60 (bar 318) | **+0.63** (bar 335) |
| f -> ff | 2.23 | 2.27 LU |
| p10 short-term | -21.0 | -21.1 |
| LRA | 11.4 | **11.6** |
| limiter at the summit | 3.9 | 4.0 dB |
| horn call bars 4 / 5, Mmax | -10.3 / -10.4 | **-13.3 / -13.4** |
| Clarinet 1 bars 82 / 162 | -10.8 / -11.2 | -11.8 / -11.8 |
| violin solo 350-351 / Hn 1 357 | -11.6 / -12.7 | **-13.7 / -14.1** |
| close, bar means 364 / 368 / 372 / 376 | -22.2 / -18.0 / -17.8 / -21.3 | -22.5 / -20.2 / -20.1 / -23.5 |
| arrivals 41 / 197 | +1.8 / +0.6 | +2.3 / +1.2 |

The cost:
- The trio's f bars 197 / 209 come down 0.6 LU (-12.6 / -12.3). They are still 1.2-1.3 LU over the solos.
- The intro mean falls -17.4 -> -18.6 because the horn call is in it. The quiet passages' means move by 0.3 LU or less.

Re-run the simulation on the c30 master. If the summit lead reads under +0.55, deepen the 305-320 row to -2.0 rather than raise the cap.

### 2. The ppp close gets louder instead of fading. Horn 1's last G sharp enters 4.6 dB over the horn relay it takes over and lands louder than its own pp inside the chord, because a +6 dB one-note envelope row sits on it (measured; fix partly inferred)

Where: qn 1089-1128 (bars 364-376). Horn 1's G sharp 4 from 1100.77 (pp at 1101, > 1113-1122 to ppp). Horn 3's relay is 1092-1101 (pp, > 1101-1106). Violins I's ppp G sharp 5 runs 1089-1128 with its Violin I solo double.

What is wrong (measured):
- The horn sum (Horn 1 + Horn 3) across the relay, by quarter: 1097 -48.7, 1099 -48.1, 1101 -45.5, 1103 **-43.5** dB. That is +4.6 dB in 1.1 s at a printed pp entry under a decrescendo. The master rises 1.9 dB with it.
- Horn 1 per bar: 361 -46.6 (pp, in the held chord), 366-367 -55.0 / -57.8 (the end of its printed >), 368-373 **-45.0..-45.5** (pp). So the pp G sharp is 1.5 dB over the pp of the chord it grew out of.
- Master 364 -> 368: +3.2 dB. mp3 364 -> 372: +4.4 LU. The movement's last page swells where the print says pp, >, ppp.
- The source, in parts.json Horn 1:
  - `vol_db` rises from -2.5 dB at 1097 to +6.0 at 1102, from roles.json Horn 1 `[1100.25, 1128, 6]`, c02 +10, c08 +6. It is a fader row for exactly one note.
  - On top of it, CC11 48 from `CC11_ADD_SPANS["Horn 1"] (1100.7, 1128.0, 14, 14)`.

Fix (instrument side; `--midi-only` on Horn 1):
- roles.json Horn 1: delete `[1100.25, 1128, 6]`. Dan's rule removes it anyway.
- `build/score_config.py`, c30 block: `CC11_ADD_SPANS["Horn 1"]` row `(1100.7, 1128.0, 14, 14)` -> `(1100.7, 1128.0, 20, 20)`.
  - Inferred: +6 units at 0.55-0.61 dB per unit on the horns at CC11 46-58 (Movement I c59, quoted in score_config) gives about +3.5 dB, so the net is about -2.5 dB.
  - Keep CC1 and the two LEVEL_SHAPES rows. They are valid while the moved onset 1100.772 and CC1 stay.

Pass on the render:
- Horn 1 bars 368-373 at -47.5 dB ± 1 (no louder than bar 361).
- The horn sum from 1099 to 1103 rises 1 dB or less.
- Master 364 -> 368 rises 1 dB or less.
- Horn 1 still within 2 dB of Violins I + solo in bars 368-374 (B's audibility check).

Then re-fit finding 1's close row: bars 368-375 on the mp3 within 0..+1 LU of bar 364. If the CC11 step reads more than 1 dB off the target, report it rather than adding envelope.

### 3. The pp < f timpani roll of bars 205-208 jumps 4.6 dB in a quarter at the start of its crescendo, then the envelope falls 6 dB while the CCs rise: the crescendo is heard as a bump and a plateau (measured)

Where: Timpani soft, qn 612-624 (pp at 612, cresc from 618, f at 624). Dan's priority 5: only a printed crescendo makes a roll grow, and it should grow through the hairpin.

What is wrong (measured on the stem):
- Per quarter: 616.75 -50.7, 617.5 -54.0, 618.0 -49.5, **618.25 -44.9**, 618.75 -42.6, 619 -41.6. Per qn after that: 620 -42.4, 621 -41.8, 622 -38.8, 623 -38.0.
- So the first 0.25 qn of the crescendo carries +4.6 dB (+7 dB from 617.5), and the remaining 5.75 qn only +6.5.
- The source is two -3 dB passage levels that release together in 617.5-618.5:
  - the c03 role `[612, 618, -3]` (0.5 qn ramp);
  - the c08 LEVEL_SHAPES row `[(612.5, 0.0), (617.5, -3.0), (618.5, 0.0)]`.
- `vol_db` goes 13.0 -> 19.8 dB from 617.5 to 618.5, then falls from 20.97 at 619.25 to 14.92 at 623.9. Meanwhile CC7 rises 23 -> 50 and CC1 57 -> 88, so the envelope cancels about half of the CC crescendo.
- At 623 the roll is still 8.3 dB under the master. Nothing needs the fall for balance.

Fix (envelope roll shape, which Dan allows as slow balance; the alias copies the Timpani lanes):
- roles.json Timpani `[612, 618, -3]` -> `[612, 618, -3, 3]`, so the role releases over 618-621.
- `build/score_config.py`, c30 block: replace the LEVEL_SHAPES Timpani row `[(612.5, 0.0), (617.5, -3.0), (618.5, 0.0)]` with `[(612.5, 0.0), (617.5, -3.0), (618.0, -3.0), (621.0, 0.0)]`.
- Find the source of the 619.25-623.9 fall in the parts.json `vol_tags` (`slow:timp_roll` from TIMP_ROLL_TRIM_DB, since 618 is in TIMP_ROLL_TRIM_HOLD_SKIP). Remove 618.0 from `TIMP_ROLL_TRIM_HOLD_SKIP`, so the trim holds 60% of its value under the hairpin as on every other crescendo roll.

Pass:
- No 0.5 qn step over 2 dB in 617-620.
- Rise 618 -> 623.5 of 8 dB or more on the stem.
- The roll stays at least 6 dB under the master at 623 (it reads 8.3 now).

The c29 alias windows and sticks stay as they are.

### 4. Verdict on the coda build (bars 329-336): the master climbs 15.5 dB from 984 to 1005, the mp3 only 5.6 LU. The build is heard as a step at 329, then a slow rise. Nothing safe fixes this in c30; do not trade the summit lead for it (measured)

What is wrong (measured, per half bar):

| qn | master (dB) | mp3 (LU) | delivery gain (dB) |
|---|---|---|---|
| 984 | -27.8 | -12.8 | +15.1 |
| 994.5 | -20.8 | -10.8 | +10.0 |
| 1003.5 | -13.7 | -8.2 | +5.5 |
| 1005 | -12.3 | -7.2 | +5.2 |

- The mf -> f crescendo of bars 329-332 rises 2.0 LU on the mp3 (7.0 dB on the master).
- The ff -> fff of bars 333-335 rises 1.2 LU (3.2 dB on the master).
- The arrival at bar 336 is +0.7 LU.
- The summit is pinned by the limiter at Mmax -7.3/-7.4:
  - It reads the same in every simulation (top ratio 1.5, top threshold 0 dB, cap 0).
  - The highest pre-limiter peaks are the strings' downbeats of bars 337-339 (qn 1008.8, 1011.4, 1014.3: master -3.4 / -3.1 dBFS; Violins II, Violins I and violas peak at -8.8..-13 dBFS each).
- The coda ride row (-2 to -5.5 dB over 993-1004.6) only holds bars 332-335 under that ceiling.
- The master has the right arc: the summit is 6.7-8 dB over the ff tuttis. The delivery keeps 0.6 LU of it.

For after this run, not c30: lower the strings' crest in bars 337-339 so the summit can sit higher at the same true peak. Then shorten the coda row.

In c30, do not touch:
- the coda ride row;
- TOP_ABOVE -3;
- the 1005 passage levels.

Every alternative I simulated kept the summit at the ceiling and lowered its lead (top threshold 0 dB: +0.51 LU).

### 5. Optional, only if finding 1's margins hold on c30: the Più mosso's pp entries (bars 325-327) are the softest music on the mp3 (-30 LU), 10 LU under the other pp passages. Dan's AirPods note applies here first (measured; simulated)

Where: qn 972-984. The pp fugato entries of the celli, violas, Violins II and Violins I, between the ff tutti close (bar 320) and the coda's crescendo.

What is wrong (measured):
- mp3 bar means: 325 -30.0, 326 -29.6, 327 -25.6. The ppp opening reads -19.4, the pp link -20.4, the Meno mosso pp -19.6, p10 -21.0.
- On the master bar 325 (-45.6) is as soft as bar 1 (-44.8). But the delivery lifts it only +15.6 dB against +25.4 at bar 1, because the 5 s lift smoothing reaches back to the ff of bar 320.
- Inferred: at one comfortable headphone volume these entries drop out.

Fix (delivery only): `RIDE_TRIMS` row `[(971.0, 0.0), (972.5, 4.0), (980.5, 4.0), (983.5, 0.0)]`, on top of finding 1.

Simulated:

| | with finding 1 alone | with this row added |
|---|---|---|
| stretto mean | -27.5 | -23.0 |
| bars 325 / 326 | | -25.2 / -24.7 |
| arrival at 329 | | +2.9 (still the movement's biggest step) |
| integrated | | -13.8 LUFS |
| summit lead | | +0.56 |
| f -> ff | | 2.13 |
| LRA | | 11.3 |
| p10 | | -20.6 |

All items pass, but the summit lead and f -> ff margins are thin. Adopt only if the c30 simulation keeps the lead at +0.6 or more.

### 6. Older faults still audible, for the record (measured; no change proposed this cycle)

- **The ff tutti theme lands under its crescendo.** Bar 105's Mmax is 0.5 LU under bar 104 on the mp3 (c26 #6, c28, c29).
- **Weak tutti downbeats.** The theme's downbeats stand only +0.3 dB over beats 2-3 on the mp3 (312-360), against +2.4 in theme A.
- **Soft strokes over pp.** The timpani strokes of the ritmo di tre battute (bars 91 and 94) read -14.4 / -14.8 LU on the mp3, 6-14 LU over the pp bars between them (90: -28.7, 93: -28.6). They are the loudest events of bars 89-99.

None of these can be fixed safely together with findings 1-3 in one render.

## Do not touch

- the sfp < shape at 900-910 and both sub. p's (S3 holds);
- the fugato growth, the codetta fade, the accelerando crescendo and the held chord's fade at 361-364;
- the timpani rolls of bars 101-103 and 301-303 and the settles on unprinted rolls;
- the felt-timpani alias windows (435-864, 1020-1128) and the hard-stick Allegro;
- the re-bows and HELD_DOUBLE of the last violin G sharp (no loop pulse);
- the coda ride row, TOP_ABOVE -3 and the 1005 passage levels (finding 4);
- the c26 woodwind figure state and Dan's bar 23 figure (none of the changes above touch it);
- the room bed and the delivery chain apart from MOM_CAP_ABOVE and the ride rows in finding 1.

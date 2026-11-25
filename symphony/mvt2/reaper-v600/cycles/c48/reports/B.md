# Cycle 48, critic B: balance and levels (on the c47 render)

c48's one-time task (loop/ONE_TIME.md) is to adopt the finale's shared techniques where they improve Movement II's measurements. In my area that means item 2 (the bar 47 fp, with each part's p-against-ff drop), the level side of items 3, 11 and 12, and the c47 carry-overs (inner held notes under a tune, the Oboe 1 eighths, Horn 4 at qn 84).

## Method

- I measured the 32 dry stems, the 4 return stems and the master of `cycles/c47/render/`. For comparison I used c45 (before the c46 hairpin curves) and c46. Each render is read on its own `rendered_build/parts.json` tempo map.
- Levels are K-weighted (BS.1770, FFT-applied) unless I say otherwise. Envelopes use 50 ms windows with a 5 ms hop, power of both channels. Note bodies are the mean over 20-80 % of the moved note.
- Own-band margin is the lead's level over the sum of every other dry stem, in 1/3-octave bands from 100 Hz to 10 kHz, weighted by the lead's energy per band.
- Item 11 and item 12 were simulated exactly on the c47 stems: the RBJ responses of the old and new ReaEQ bands (the same formula as `deliver_master.biquad_h`) applied by FFT. The basses have no send (`return: []`), so the master changes by exactly the stem change. For the winds I applied the same ratio to R Winds.
- Labels: **measured** (from the render or the data), **predicted** (arithmetic on measured levels), **inferred** (a judgement about what a listener hears).
- I changed no audio settings and touched no REAPER, build or tool file. Scratch was in `/private/tmp/claude-501/mockup-loop/mvt2-c48-B/` and is deleted.

## Manual notes

MANUAL-READING.md has no row for cycle 48, so I did no page reading. The table lists the manual facts and MANUAL-GAPS items this report relies on.

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.53: note velocity is for short articulations because it cannot change mid-note; CCs shape sustained notes. DIGEST §2 (M1 c06, measured): velocity is ignored on the KS Master sustain rows. | The bar 47 fp (Violins II, Violas, Double basses on Leg Slur MAX / Sus MAX). | Yes. The finale's `FP_VEL` (fp velocity 96) would change nothing here. The fp has to come from CC11 timing (finding 1). |
| p.99, p.144: a legato transition plays only when notes overlap, and velocity sets the transition speed. | Violins II and Violas at qn 148 play v124 slur transitions from their 146 notes. No slur is printed into 148. | No. An fp on a new bow needs a fresh attack. As played, the attack is the soft transition sample (finding 1). |
| p.69: Harp Sustain RR plays a Nail Pick at velocity 124-127. | Harp, Harp harmonics. | Yes. Highest velocities are 104 and 70, so the finale's item 9 cap (123) is not needed. |
| MANUAL-GAPS #8: 4 soli on half-section patches. | Celli 4 soli on Vc div (bars 83-86); basses 4 soli (bars 65-70, 87-92). | Levels on target: Vc div pp -48.9 against celli pp -48.3. Only the timbre is open. |
| MANUAL-GAPS #7: recorded crescendo rolls (Felt Cresc). | Timpani 168, 200, 261. | Not tried. Roll levels are fine: -15 to -23 dB under the master per beat at both climaxes ("Also measured"). |

## ONE_TIME items in my area

**Item 2 (fp).** This is finding 1. It includes each part's own drop and the p-against-ff table for every part.

**Item 3 (sub. p): nothing to adopt in Movement II (measured on the data and the render).**
- v600 prints no "sub.". I scanned every track's printed-dynamics curve (`dyn_curve`) for a fall of 10 CC or more within 0.5 qn. The only one is the fp at 148 on Violins II, Violas and basses.
- No `phrase_shape` phrase starts on a drop of 6 CC or more. A PHRASE_SHAPE "drop" type would therefore change no phrase.
- `HELD_DECRESC_DB` is off in this config: `held_decresc` is empty on all 32 tracks. HELD_DECRESC_CARRY would have nothing to carry.
- S3 at 148 holds. The fp's fall is in CC11 (before the hall), and the returns are post-fader sends, so the hall keeps ringing.
- The breath before bar 59 (qn 195-196) is a short decrescendo into a fresh f, not a subito.
  - Master per 0.125 qn from 195.125: -20.9 / -21.1 / -22.5 / -23.8 / -23.6 / -21.7.
  - Steepest 10 ms fall over 195-196.1: 3.1 dB, including the note gaps.
  - R Strings stays at -49 to -53 and R Winds at -38 to -42 through it, so the hall rings on.

**Item 11 (winds family 1 kHz bell -3.1 to -1.55 dB): drop it for Movement II, with this evidence (measured and simulated).**
- The master is not off the references in the band this bell touches:
  - 500 Hz-2 kHz share: -3.73, against Dvořák -3.46, Brahms 1/ii -3.82 and Brahms 4/ii -4.41 (inside the range).
  - 2-6 kHz share: -9.96, against -10.53 / -12.43 / -11.78 (0.6-2.5 dB bright). A 1 kHz lift on the winds does not address that.
- Simulated with -1.55 dB on all eleven winds and on R Winds, the master's band shares move by 0.15 dB or less:

  | Band | Now | With the change |
  |---|---|---|
  | 500 Hz-1 kHz | -6.44 | -6.33 |
  | 1-2 kHz | -6.98 | -6.83 |
  | 2-8 kHz | -9.75 | -9.85 |

- If critic C wants it anyway for wind colour, these make-ups keep each wind stem's K level (its own K change in brackets). Put them in `mix.json` `gain_db`.

  | Track | Make-up (dB) | K change |
  |---|---|---|
  | Flute 1 | -0.5 | +0.53 |
  | Flute 2 | -0.8 | +0.82 |
  | Oboe 1 | -0.55 | +0.56 |
  | Oboe 2 | -0.45 | +0.45 |
  | Cor anglais | -0.9 | +0.91 |
  | Clarinet 1 | -0.55 | +0.57 |
  | Clarinet 2 | -0.35 | +0.36 |
  | Bass clarinet | -0.45 | +0.43 |
  | Bassoon 1 | -0.35 | +0.36 |
  | Bassoon 2 | -0.3 | +0.32 |
  | Contrabassoon | -0.15 | +0.17 |

**Item 12 (basses high-pass 53 to 35 Hz): adopt.** This is finding 4.

## Findings, ranked by what a listener will hear

### 1. Bar 47 (qn 148): the strings' fp is not heard. Its attack arrives 250-350 ms late as a swell, and in the master the beat is the quietest moment of the bar (measured; fix predicted)

**Where:** Violins II, Violas and Double basses, printed fp then a decrescendo to pp, on the B flat minor downbeat after the 146-148 crescendo. In the same bar: Oboe 1 mf > (the tune), celli mp >, bassoons p >.

**Evidence (measured, c47, K 50 ms windows, times re the beat at 170.177 s):**

- **The master** reads -32.0 at -100 ms, **-36.4 on the beat**, -34.1 at +150 ms, -31.3 at +350 ms, then -30.4 to -31.0.
  - So there is no accent and no fall after it: from the strings' peak to the p body after it, the master's drop is 0.0 dB.
  - The dip on the beat is Oboe 1's re-tongue on its repeated D flat 5 (146 to 148; the oboe falls from -34.6 to -42.2), which the strings do not fill.
  - c46 reads the same within 0.2 dB.

- **Each part's own drop.** Peak = 50 ms max from the note-on to 148.5; body = mean over 148.6-149.2.

  | Part | Note-on | Before | f peak (time) | p body | Drop | Own f / ff median |
  |---|---|---|---|---|---|---|
  | Violins II | -240 ms | -49.4 | -41.0 (+290 ms) | -46.3 | **5.3** | f -31.0 |
  | Violas | -225 ms | -48.6 | -38.5 (+250 ms); join peak -38.1 at -100 ms | -48.0 | 9.5-10.0 | ff -28.4, mf -41.4 |
  | Double basses | -160 ms | -49.5 | -37.7 (+350 ms) | -46.7 | 9.3 | f -36.1 |

  Violins II's f is 10 dB under its own f. All three peak a quarter of a second after the beat (S2).

- **Cause (read in parts.json):**
  - The CC11 spike is written at 148.02-148.2 (84-88) and falls to 46 by 148.4 (`FP_SPIKE = ("f", 0.2, 0.4)`, c34).
  - The basses' led note-on at 147.8965 holds CC11 46 until 148.0. This is the pull, which copies the curve's value at the score onset (`final(148.0)` = the p level), and the spike ramps in only after it.
  - Violins II and Violas play 148 as Leg Slur MAX transitions at v124, 0.15 qn early, so their attack is the p transition sample.
  - The decrescendo printed at the same onset does not overwrite the c47 spike (the spike is on all three lanes). It would overwrite a step at the mark, because its start points sit at q (the finale's case).
  - This is the finale's item 2 bug: the led notes start on the p layer and swell into the f.

**Fix:**
- (a) `tools/score_to_parts.py`: port the finale's `FP_SPIKE_AT_MARK` (mvt3 `tools/score_to_parts.py` around lines 772-778, 1820 and 1865-1872). It has two parts:
  - the attack step at q itself (`t0_ = q`), so the pull carries the f level from the moved note-on;
  - `fp_hp[q] = q + fall_`, used in the hairpin branch (mvt3 line 1980), so the 148 decrescendo starts at 148.4 and does not overwrite the step.

  In `build/score_config.py`, set `FP_SPIKE_AT_MARK = True` and keep `FP_SPIKE = ("f", 0.2, 0.4)` (0.21 / 0.42 s at this tempo). Leave `FP_VEL` unset (the manual note above).
- (b) `build/score_config.py`: `DOWNBOW_STROKE_AT["Violins II"] = DOWNBOW_STROKE_AT.get("Violins II", []) + [148.0]` and `DOWNBOW_STROKE_AT["Violas"] += [148.0]`. This gives fresh Sus MAX strokes with an entry lead, with the 146 note cut at the keyswitch, so the fp has a bow attack that the pull can carry. Both tracks already load Sus MAX (`art_counts` 19 / 73), so there is no Opus state change.
- (c) After the render, measure each part's own drop, as the finale did (peak from the note-on to 148.5, minus the mean over 148.6-149.2). Where a part is under 10 dB, add `roles.json` [148.9, 151.0, -(10 - drop)], at most -8 dB. For Violas use 152.4 instead of 151.0, since its pp is at 152.5. With post-fader returns a volume-envelope step leaves the hall ringing (finale item 3).

**Predicted:**
- With each part's f within 0 to 3 dB of its own f median at the beat, the master on the beat goes from -36.4 to about -32 to -30.5 (+4 to +6 dB), which is 1.5-3 dB over the end of the crescendo before it.
- Each part's drop: Violins II about 12, Violas and basses about 10.
- After the fall, Oboe 1 (mf, -31 to -33) carries on over the p strings, so the master itself falls only 1-2 dB. As the finale says, judge each part's own drop, not the master's.
- Inferred: the fp is heard as a string accent on the downbeat. Today it is a late swell under the oboe.

**Per-part p-against-ff, every part (measured, c47).** Median K per 1 qn bin where the part plays, grouped by its printed dynamic (step-held). The finale's rule is p at least 10 dB under ff.

| Part | p | ff (f where no ff) | Drop |
|---|---|---|---|
| Flute 1 | -40.7 | -29.5 | 11.2 |
| **Oboe 1** | -41.5 | -34.6 (f -37.7, mf -35.8) | **6.9** |
| **Cor anglais** | -43.9 | -34.1 | **9.8** |
| Clarinet 1 | -45.7 | -29.5 | 16.2 |
| Clarinet 2 | -45.2 | -33.2 | 12.0 |
| Bass clarinet | -43.6 | -31.6 | 12.0 |
| Bassoon 1 | -47.8 | -34.1 | 13.7 |
| Bassoon 2 | -50.9 | -32.7 | 18.2 |
| Contrabassoon | pp -52.0 | -33.1 | 18.9 |
| Horn 1 | -40.4 | -25.4 | 15.0 |
| Horn 2 | -48.8 | -28.4 | 20.4 |
| Horn 3 | pp -50.9 | f -29.8 | 21.1 |
| Horn 4 | pp -51.0 | f -35.2 | 15.8 |
| Trombone 2 | -51.6 | f -24.6 | 27.0 |
| Bass trombone | -46.7 | f -26.6 | 20.1 |
| Tuba | -45.0 | f -29.1 | 15.9 |
| Timpani | -47.9 | f -37.8 | 10.1 |
| Harp | -48.8 | f -31.8 | 17.0 |
| Violins I | -40.2 | -22.5 | 17.7 |
| Violins II | -44.0 | -26.5 | 17.5 |
| Violas | -46.7 | -28.4 | 18.3 |
| Celli | -41.4 | -24.6 | 16.8 |
| Basses | -48.9 | -30.5 | 18.4 |
| Violas div | -48.3 | -35.1 | 13.2 |

- Only Oboe 1 and the cor anglais fall under 10 dB. Both p figures are lifted solo lines (solo roles), and both ff figures are tutti doublings (Oboe 1's bar 80 note was cut 8 dB in c47).
- I would not add p rows there. Lowering the p solos would undo the solo margins, which are the lens's first priority ("Also measured").
- Oboe 1's mf goal at 148 (-31.8 body) sits above its own f and ff medians. That comes from c42's +4.2 step against a sample swell, so leave it.

### 2. Oboe 1, bar 46 (qn 142-143): the eighth-note turn sinks to the accompaniment's level (measured; c47 carry-over)

**Where:** Oboe 1 "dolce espr." p.
- E flat 5 at 142 (moved onset 141.898) and D flat 5 at 142.5 (moved onset 142.443).
- Between the D flat 5 half note at 140 and the C5 at 143.

**Evidence (measured):**
- **Bodies, c47:** 140 -39.2, **142 -44.6, 142.5 -45.0**, 143 -39.8, 144 -41.4. The eighths are 5.4 / 5.8 dB under the half note before them and 4.8 / 5.2 dB under the note after.
- **Bodies, c46:** 142 -43.0, 142.5 -41.9 (3.8 / 2.7 dB under 140).
- **c45:** -43.6 / -43.3.
- **Quarter beats 142.0-143.0, Oboe 1:** -44.4, -42.2, **-46.9**, -40.6.
- **Strongest accompaniment at 142.5-142.75:** Violins II -47.0, Violas -47.3, Bassoon 1 -48.7. The tune is level with the second violins there.
- **Why:** c47's shorter fill holds (0.08 / 0.15 s, critic A) filled the join holes but no longer lift the bodies (c47 CHANGES "Open"). The 143 fill (6 dB, pre 0.12 s) starts at about 142.73 and lifts only the last part of 142.5.
- **Inferred:** the turn at the top of the phrase is heard as a soft gap in the line.

**Fix:** `build/score_config.py`:
```
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(142.02, 0.0), (142.10, 3.0), (142.70, 3.0), (142.72, 0.0)]]
```
- It starts after 142's fill hold, so the 142 front is not raised. On 142.5 it raises the fill front and the body together, so critic A's 200 ms overshoot (measured against the body) does not grow.
- It ends before the 143 fill begins (moved onset 142.848 minus 0.12 s), so the 143 front is untouched.
- Level only: simulate it with `cycles/c47/actor_scripts/sim47.py` / `m47.py`, or apply it as a stem fix.

**Predicted:**
- Bodies about -41.9 / -42.3: 2.4-3 dB under 140 and 2.1-2.5 dB under 143, as a lighter turn should be.
- 142.5-142.75 at about -43.9, which is 3.1 dB over Violins II.
- Master +1 dB over those two quarter beats, nothing elsewhere.

### 3. Bar 81 (qn 269-269.5): the celli's held D flat 4 rises over the tune's descent. The c46 hairpin curve lifted the inner parts more than the tune (measured; the Movement I c51 check)

**Where:** The tune descends in eighths in Violins I, Violins II and Flute 1 (E flat 6 to A flat 5, 269-271; Violins II an octave lower) under the printed decrescendo from 268 to the p at 271. The inner voices hold under it:
- celli D flat 4: Leg Slur target at 268.869, v124, 2 qn;
- Violas E flat 4.

**Evidence (measured):**
- **Celli over 269.0-269.5:**
  - c45 (linear hairpins) -33.8, with Violins I at -36.0 (+2.2 over the tune);
  - c46 and c47 -31.0, with Violins I at -34.1 (**+3.1**).
- **Transition peak at 269.25-269.375:** -31.0 in c45, -28.2 in c47, **5.4 dB over Violins I** (-33.6).
- **K, 269.0-269.5:** the celli are the loudest stem.
- **A-weighted, 269.0-269.5:** Violins I -36.1, celli -36.5, Violins II -36.7. The celli are level with the tune.
- **Cause:** c46's curve holds the celli's CC11 up in the first third of the decrescendo. At 269.0 it reads 107, against c45's 96 (+11 CC). The tune's notes gained only 1.9 dB.
- **Violas:** -37.4 in c45, -35.4 in c47 (1.3 dB under Violins I).
- **Rest of the screen:** I compared every curved decrescendo over 1 qn (124 of them) from c45 to c47. No other inner held note rose more than 1.8 dB against the master. The basses at 268-271 rose +2.9 dB, mostly from c46's f trim, and stay 7 dB under Violins I.
- **Inferred:** a cello swell surfaces in the middle of the cadence's falling line.

**Fix:** `build/score_config.py`:
- Add `(268.0, 271.0)` to `HP_CURVE["linear"]` for `"Violoncellos"` and for `"Violas"`.
- Add `LEVEL_SHAPES["Violoncellos"] += [[(268.95, 0.0), (269.0, -2.0), (269.4, -2.0), (269.7, 0.0)]]` on the transition peak.
- These are CC11 and level only.

**Predicted:**
- Celli at 269.0-269.5 about -35.8, which is 1.7 dB under Violins I (unchanged at -34.1); the peak about -33.
- Violas about -37.4 (3.3 dB under the tune).
- Celli at 269.5-270 about -38.3, against -34.7 today (c45's linear value).
- Master at 269 down 0.5 dB at most. Bars 79-80 and the climax order are untouched.

### 4. Item 12: the basses' high-pass at 53 Hz thins their main pedal notes. Moving it to 35 Hz adds fundamental and no boom (measured by exact simulation)

**Where:** `build/mix.json` `tracks["Double basses"]["family_eq"][0]`: `{"type": "hp", "hz": 53.0, "bw": 2.0}`. This is the track's own copy of the string family EQ, with the Duc 228 Hz bell.

**Evidence (measured):**
- **The 53 Hz high-pass at the basses' fundamentals:** A flat 1 (51.9 Hz) -3.7 dB, G flat 1 (46.2) -4.9, E1 (41.2) -6.2, B flat 1 (58.3) -2.8.
- **At 35 Hz the same notes lose** -1.2, -1.7, -2.3 and -0.9 dB, so they gain **+2.5, +3.2, +3.9 and +1.9 dB**.
- **A flat 1 is the basses' most-held pitch:** 58.6 qn of notes (bars 2-3, the A flat close at bar 30, bars 42-44, 51-52, 58-60, 71-75, and the pedal from bar 82 to the end). Next come E flat 2 (36.1 qn), D flat 2 (24.9) and B flat 1 (20.1).
- **The basses carry** 68 % of the master's 40-60 Hz energy and 78 % of its 30-100 Hz energy.
- **Master band shares** (all active frames / loudest 15 % / softest 40 %):

  | Band | All active | Loudest 15 % | Softest 40 % |
  |---|---|---|---|
  | 20-100 Hz | -17.97 -> **-17.26** | -18.23 -> -17.47 | -14.85 -> -14.42 |
  | 40-60 Hz | -34.17 -> -32.48 | -35.00 -> -33.32 | -28.14 -> -26.32 |
  | 100-250 Hz | -7.52 -> **-7.49** | | |

  The boom region does not move.

- **References for 20-100 Hz:** Dvořák (lossy) -21.67, Brahms 1/ii -8.54, Brahms 4/ii -7.88 (stored metrics). The kit's c13 target was -14.5 to -12.5. The change moves toward these and stays under the target.
- **Per passage, 20-100 Hz share:**

  | Passage | Now | With 35 Hz |
  |---|---|---|
  | Coda A flat pedal | -13.38 | -13.08 |
  | Bars 65-70 | -20.35 | -19.51 |
  | Bars 61-62 | -18.58 | -17.73 |
  | Bars 79-80 | -17.82 | -16.64 |
  | Bar 59 | -13.46 | -13.03 |

- **Basses' K level:** +0.28 dB overall, so no make-up is needed.
- The delivery master's 42 Hz high-pass (`master_eq`) stays. The gain is linear, so the delivered file keeps it.

**Fix:** Change that band's `"hz"` from 53.0 to 35.0. This is a ReaEQ value with no Opus state change. Leave the other string tracks at 53.

**Predicted / inferred:** steadier weight under the coda's ppp A flat pedal and the A flat closes, solid not boomy, since nothing above 100 Hz moves. If Dan hears thickness, listen at bar 59 beats 3-4 (G1 +2.8 dB, the spot c47 B named) before touching the trims.

### 5. Horn 1's counter-melody, bar 60 (qn 202-204): a role releases across the printed crescendo, so the held G flat 4 is masked going into the ff (measured; small)

**Where:** Horn 1, f with a crescendo from 200 to the ff at 204, against the theme in Violins I/II, Flute 1 and Oboe 1.

**Evidence (measured, c47):**
- **Own-band margin, bars 59-60:** +0.5 dB median, with 44 % of frames under 0. In c46 it was -1.7 and 62 %, so c47's +2.5 role helped.
- **Remaining masked beats:** 198 -0.2, 200 -1.0, 202 -0.2, **203 -4.5 (100 % of frames)**.
- **K per beat at 201 / 202 / 203:** Horn 1 -26.7 / -25.4 / -26.6, against Violins I -27.3 / -24.9 / -21.9. The horn falls while the violins rise 3 dB.
- **Cause:** `roles.json` Horn 1 [188, 204, 2, 4] ramps its +2 dB out over 200-204, exactly the printed crescendo. On top of that, the 202 fill decays 4.2 dB by 202.6. The envelope therefore falls 13.3 -> 7.7 dB over 202.35-203.95, while CC11 and CC1 climb.

**Fix:** In `build/roles.json` "Horn 1", change [188, 204, 2, 4] to **[188, 203.9, 2, 0.1]**. It holds +2 to the end of the crescendo and still ends before c36's bar 61 front shape.

**Predicted:**
- +1.0 dB at 202 and +1.5 dB at 203. The own-band margin at 203 goes to about -3; bar 60 overall goes to about +1.5.
- Master bar 60 +0.1 dB. Bar 61 stays the loudest.
- Inferred: a modest gain, because this is the end of the counter-line under the violins' climb.

## Also measured, no change

**Solo margins, c46 -> c47.** None got worse; all are positive except the two counter-melodies. Figures: K margin over all other stems; lead minus the strongest single stem (percentage of frames where the lead is under it); own-band margin.

| Solo | c46 | c47 |
|---|---|---|
| Horn 1, bars 7-14 | +5.0 | +6.0 / +9.0 (0 %) / +15.1 |
| Oboe 1, bars 15-16 | +1.6 | +2.1 / +5.2 (4 %) / +15.5 |
| Solo violin, bars 17-18 | +6.6 | +6.6 |
| Oboe 1, bars 19-20 | +3.3 | +3.3 |
| Solo violin, bars 21-22 | +3.3 | +3.3 |
| Bass clarinet, bars 31-36 | +5.5 | +5.5 |
| Flute 1, bars 37-40 | +2.9 | +2.9 |
| Cor anglais, bars 41-44 | -0.9 | -0.4 / +2.2 (20 %, Flute 1) / +14.5 |
| Oboe 1, bars 45-47 | +1.7 | +2.0 |
| Cor anglais, bars 48-50 | +1.4 | +1.4 |
| Trombone 1, bars 63-64 | +7.9 | +8.1 |
| Horn 1, bars 67-70 | +5.8 | +5.7 / own-band +13.3 |
| Clarinet 1, bars 85-89 | +1.2 | +1.6 / +5.0 (17 %) / +14.1 |
| Horn 1 counter, bars 53-58 | | own-band +3.4 (27 %) |
| Celli counter, bars 71-74 | | own-band +5.0 (19 %) |

**Climaxes.** Family sums relative to the strings (K):

| Bar | Winds | Horns | Low brass | Timpani |
|---|---|---|---|---|
| 61 | -3.3 | -5.9 | -3.3 | -15.5 |
| 62 | -2.8 | -5.2 | -4.8 | -22.5 |
| 79 | 0.0 | -5.2 | | -15.5 |
| 80 | -1.2 | -4.8 | | -16.7 |

- Timpani minus the master per beat: -15 to -23 dB over 200-212 and 260-272. The rolls never cover.
- The low brass sit under Violins I and the celli at bars 61-62. Trombone 1 correctly leads bars 63-64.
- Single ff woodwinds at bars 61-62 sit 5.7-12.5 dB under Violins I. The norm in Rimsky-Korsakov's resonance table would be about 3 dB under, so the wind family there is about 3 dB light. I leave it: the c37 brass +3 is protected, the delivery limiter is at 2.0 dB, and bars 79-80 are at the norm.

**Dynamic mapping across families.**
- p sits together: leads -40 to -46, accompaniment -44 to -51, in every family.
- pp accompaniment is -48 to -53 everywhere, except the coda violas. Both halves (Violas F3/E flat 3, Violas div A flat 3, con sord.) sit at -55 to -62 per bar, 4-8 dB under the celli and Violins II. Horn 3 con sord. and Clarinet 2 double the A flat 3 and E flat 4. These are the series 1 coda balance rows, so I leave them.
- Divisi against full sections at pp: Violins II div -50.2 against -49.1; Vc div -48.9 against -48.3.

**Horn 4 at qn 84 (level side).**
- The sample's dip at 85.5-86.5 is -53..-55 against -46 before and -47.5 after, and it rebounds to 4 dB over its start by 87.
- The master's K there is -37 to -39, 15 dB over the horn. In the horn's second-harmonic band (311 Hz) the dip moves the master about 2 dB, within its own movement.
- Inferred: inaudible as a level change.
- If C wants it smoothed, replace c47's [(84.5, 0), (86.5, -5.5), (90, -5.5), (90.5, 0)] with [(85.0, 0), (85.4, 4.0), (86.1, 4.5), (86.4, -3.0), (86.75, -5.0), (88.0, -6.0), (90.0, -6.0), (90.5, 0)]. These points are fitted from the envelope-free sample level.

**Bass clarinet repeat at 265:** an articulation item (S1). I did not measure it.

**Do not touch:**
- the c47 fills and wind entry leads;
- Oboe 1's c42 +4.2 step at 148 and its 139/145/266 trims;
- the c46/c47 solo roles and the Horn 1 [198, 203.9, 2.5] role;
- the basses' f/ff trims 2.5/4.0 and their 140 Hz / bell2 80 Hz EQ;
- the c37 bars 61-62 brass +3 and the c36 Horn 1 bar 61 front shape;
- the timpani roll shapes and the 277 step;
- the return faders and IR envelope;
- the coda balance rows;
- the final-chord fade;
- the string family EQ high-pass at 53 Hz on every string track except the basses.

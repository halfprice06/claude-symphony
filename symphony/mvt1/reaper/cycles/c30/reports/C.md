# Cycle 30, critic C: dynamics over time (render c29)

Lens: the shape of every hairpin and phrase; the loudness arc against the score (the sostenuto climax with the tam-tam at bars 122-126, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda); loudness range of the master and the mp3 (BRIEF item 6); swells and loop pulsing on held notes (item 7); decays; comparison with real recordings.

## Method

- **Material.** The stem-fixed c29 render (`cycles/c29/render/`, master and 33 stems), `mvt1-mockup-c29.mp3`, and `cycles/c29/rendered_build/parts.json` (tempo map, notes, hairpins, `dyn_curve`, `vol_db`). Score pages 1, 9-12, 14-17 read.
- **Loudness.** ffmpeg ebur128 at 10 Hz. M is shifted 0.2 s and S 1.5 s so that each window is centred. The mp3 lines up with the master at lag 0 (correlation of M 0.961). Stem levels are stereo power in 10 ms frames.
- **Delivery simulation.** I applied gain shapes to the master, or to a stem that is then summed back into the master. The result went through a copy of `tools/deliver_master.py` with TOP_RATIO and TOP_ABOVE read from the environment. With no change the copy reproduces c29 exactly: LRA 14.6 LU, span 19.5 dB, limiter 2.1 dB, S max 160 -9.99 / 122 -11.19 / 170 -13.14 / bar 26 -14.60.
- **Printed dynamic per bar.** The loudest printed mark among the staves that play in the bar, read from `build/mockup-events.tsv`.
- **Scratch.** The scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c30-C/`. The folder is deleted (BRIEF rule). Every window is stated below so that each number can be measured again.

## State of the arc (measured)

**Master and mp3.**
- Master: -16.4 LUFS, LRA 22.9 LU.
- mp3: -19.8 LUFS, LRA 14.6 LU, TP -1.6 dBTP, p10-to-max span 19.5 dB, limiter 2.1 dB.
- Five-second moves of 3 dB or more: 107, median share kept 0.78, 0 inversions.
- Correlation of bar level with the bar's printed dynamic: master 0.86, mp3 0.80.

**Climaxes and arrivals (mp3, power mean of M per beat).**
- Bar 121 crescendo, 480-483: -16.1 -14.9 -14.0 -13.2; 122 at -11.1. Bars 122-123 hold within -10.7..-11.8. Bars 124-126 fall from -15.4 to -27.2 over 12 beats.
- Bar 159 cymbal roll, 632-635: -13.8 -13.2 -12.1 -11.6; 160 at -9.7.
- Into the recapitulation, 516-519: -23.2 -22.1 -20.8 -18.4; 131 at -16.1.
- Coda 169 crescendo: 672 -18.4 to 676 -12.0.
- Order on S max: 160 -9.99 > 122 -11.19 > 170 -13.14 > bar 26 -14.60.
- Rise of each peak over the median S of the 20 s before it:

  | Peak | Master | mp3 |
  |---|---|---|
  | 160 | 21.9 dB | 14.3 dB |
  | Letter G | 13.4 dB | 8.7 dB |
  | 170 | 8.1 dB | 7.3 dB |
  | 131 | 7.3 dB | 6.3 dB |
  | 122 | 4.9 dB | 4.8 dB |

  122 comes after the letter-G ff, so its rise is small.

**Hairpins per track** (451 of 1 qn or longer; last third against first third of the stem).
- 295 crescendos: median +4.6 dB, 35 under +1 dB.
- 156 decrescendos: median -5.0 dB, 18 under 1 dB.
- The weak ones on exposed lines are in the recapitulation's second theme:
  - Oboe 1 580-582 decrescendo: +2.5 dB.
  - Celli 596-598 decrescendo: +2.0 dB.
  - Horn 1 589-591 crescendo: -1.6 dB on the stem, master -1.6 dB.
- These repeat in c28 within 0.2 dB, and they come from the sample. The 589 notes are hot in their first 0.5 qn and dip 5 dB at 589.75, and the Oboe E5 swells inside the note under its -7 dB cut. Halving the 589 note trims did not turn the swell around in a stem simulation, so I propose no change.

**Delivered levels by printed dynamic (median bar level, mp3 M).**

| | ppp | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|---|
| mp3 (dB) | -35.9 | -29.1 | -28.3 | -24.8 | -24.6 | -22.1 | -17.6 | -11.3 |
| master (dB) | -44.0 | -37.1 | -31.8 | -29.0 | -28.8 | -24.1 | -16.1 | -8.2 |

Finding 2 deals with this.

**Short-term (S) distribution against a recording (dB).**

| | p50-p10 | p90-p50 | p99-p90 | max-p75 |
|---|---|---|---|---|
| Dvořák 9/i (measured now) | 11.7 | 12.3 | 1.5 | 4.8 |
| Brahms 1/i (c26-C) | 11.2 | 6.7 | 2.2 | 4.9 |
| Brahms 4/i (c26-C) | 7.6 | 5.0 | 3.1 | 6.4 |
| c29 mp3 | 5.5 | 7.6 | 5.2 | 9.4 |

**Item 7 passes (measured).**
- Autocorrelation at 3.95 s of the 100-300 Hz band level and of the spectral centroid (20 ms frames, quadratic detrend):

  | Passage | Band | Centroid |
  |---|---|---|
  | Final chord 712-728, master | -0.32 | -0.09 |
  | Final chord, string stems | -0.14..-0.04 | -0.07..+0.06 |
  | Final chord, Horns 3/4 | -0.22 | -0.20 |
  | Final chord, timpani | -0.20 | -0.07 |
  | 696-712, master | -0.05 | +0.04 |
  | 484-504, master | -0.28 | -0.21 |
  | 20-44, master | -0.18 | -0.11 |

- Only three notes of 6 s or more are left unsplit (Contrabassoon 484, Bass clarinet 480, Tuba 488). Their level, band and centroid autocorrelations are all at most +0.13.

**Item 8 passes (measured).**
- 2-5 kHz over -10..+80 ms minus +120..+400 ms:

  | Family | n | Median | p90 |
  |---|---|---|---|
  | Strings | 170 | -8.2 | -2.5 |
  | Winds | 186 | -11.7 | -4.4 |
  | Brass | 106 | -15.0 | -7.4 (max -1.0) |
  | Timpani | 12 | -2.6 | +1.2 |

- The outliers are known cases:
  - Violas 536 at +11.6 is the masked double stop.
  - Clarinet 1 558 (+6.5) and 414 (+3.1) are the per-render bright state.

**Unprinted swells.** Held notes of 2.5 s or more with no hairpin and an exposure above -6 dB: 4 notes. None needs action. The largest is celli 176, which rises 6.5 dB into the mf at 183.

**Decays.** The bar-170 fermata chord falls from -18.4 to -52.3 dB (M) over the 0.5 qn fermata rest at 24 bpm (1.25 s). The final chord's tail is unchanged from c26-C.

## 1. The fff tam-tam of bar 122 is never heard as more than an attack: it sits 11-17 dB under the orchestra from the stroke on, and the existing envelope ramps it down with the brass (measured; simulated fix)

**Where.** Tam-tam, qn 484 (bar 122, heavy beater, fff, l.v., damped at 127), through the sostenuto 123 and the diminuendo of 124-126 (qn 484-504). Score page 11.

**Evidence (measured).**
- **Stem against master, power per qn (dB):**

  | qn | 484 | 488 | 492 | 496 | 500 | 503 |
  |---|---|---|---|---|---|---|
  | Tam-tam | -21.7 | -24.2 | -33.5 | -41.8 | -45.9 | -49.6 |
  | Master | -10.6 | -12.1 | -16.6 | -24.9 | -31.5 | -32.6 |
  | Tam-tam re master | -11 | -12 | -17 | -17 | -14 | -17 |

  The tam-tam falls as fast as the orchestra's diminuendo, so it never comes out of the texture as the brass releases (492-496) and the woodwinds and strings reach p (bar 126).
- **By band (tam-tam minus master, 2 qn windows from 484):**
  - 600 Hz-2 kHz: -7.8, -8.8, -12.4, -15.8, then -15..-21.
  - 2-5 kHz: -5.2, -6.6, -10.8, -17.3, then -19..-36.
  - 5-12 kHz: -6.8 and -9.0, then -22.6 at 488 and -40 from 490.
- **The stem by itself.** The 5-12 kHz band peaks 0.5 s after the stroke and is 33 dB down by 3.5 s. The whole stem falls 24 dB in 9.6 s (2.5 dB/s).
- **The envelope pulls it down further.** The rendered `vol_db` on the Tam-tam (parts.json): +2 at 484, +6 at 487, held to 492, then a ramp from +6 to 0 over 492-500. The track also gets the `_damp` at 504.2.

**Inferred effect.** A heavy-beater fff tam-tam is the signature of this climax. In a hall its roar is still heard after the brass cut off and while the orchestra dies to p; that is what "l.v." and the damp at 127 are written for. Here it is heard only as the first second of the stroke. Bars 124-126 sound like a plain orchestral diminuendo, and the damp at 127 changes nothing audible.

**Fix (level only, stem fix can apply it).** `build/score_config.py`, after line 218 (`PERC_MAP["Tam-tam"]["_damp"]`):

```python
# c30 C #1: the fff tam-tam (484) sat 11-17 dB under the orchestra through 124-126 and its envelope fell with the brass;
# hold it up so the wash comes through the diminuendo (net envelope about +8 at 488, +12 at 492, +11 at 496, +9 at 500-504.2)
LEVEL_SHAPES["Tam-tam"] = LEVEL_SHAPES.get("Tam-tam", []) + [
    [(485.0, 0.0), (488.0, 3.0), (492.0, 7.0), (496.0, 9.0), (504.2, 9.0), (504.4, 0.0)]]
```

- The shape starts after the stroke, so the attack and the 484 peak are unchanged.
- It ends where the damp starts, so the damp now cuts from a louder level, as printed.
- `LEVEL_SHAPES["Tam-tam"]` is read by the perc track (the `_coda26` line 1473 already uses it), and this shape lies outside `_coda26`.

**Simulated (tam-tam stem through the shape, summed into the master, then delivered).**
- **Tam-tam re master:**

  | qn | 488 | 492 | 496 | 500 | 502 |
  |---|---|---|---|---|---|
  | Before | -12 | -17 | -17 | -14 | -17 |
  | After | -9.7 | -9.4 | -8.1 | -6.1 | -8.1 |

  Its decay over 492-502 slows from 3.2 to 2.2 dB/s.
- **The master's diminuendo is kept:**
  - The master moves by at most 0.7 dB in 496-503.
  - The mp3 per qn 492-503 runs -15.4 to -27.8. Before it ran -15.5 to -27.8.
  - No beat rises against the one before, apart from those already rising in c29 (it was 0 inversions before and after).
- **The rest is unchanged:**
  - S max 122: -11.19 -> -11.01. 160 stays at -9.99, so the margin is 0.98 dB.
  - Limiter 2.1 -> 2.0 dB, LRA 14.6, span 19.5.

**Criterion.**
- On the stem fix: tam-tam minus master at most -10 dB over 492-503 (power per 2 qn), and the first 1 qn after 484 unchanged within 0.5 dB.
- mp3 per qn from 492 to 503 never more than 0.5 dB above the qn before.
- 160 still over 122 by at least 0.8 dB on S max.

**Not proposed this cycle.** The library also has a `38in Large Tam Tam.oib` (Cymbal Pairs folder). It has the same Long RR / Short / Crs groups plus Bowed and Scrapes, and region roots from key 36. A larger instrument would decay more slowly in the high band. It cannot be checked before the one remaining render, so I leave it as an open item.

## 2. The delivered soft half has no steps between pp and p or between mp and mf, while the two fff climaxes stand further above the loud music than in any reference; a stronger top ride frees 0.8 dB of span, and the coda's pp can take it (measured; simulated fix)

**Where.**
- The whole file: `tools/deliver_master.py`.
- The coda's pp chorale and Tempo I (bars 175-182, qn 696-729), through the c26 `_coda26` shape in `build/score_config.py` (line 1468 on).

**Evidence (measured).**
- **Delivered levels by printed dynamic** (table above):
  - pp -29.1 and p -28.3: 0.8 dB apart.
  - mp -24.8 and mf -24.6: 0.2 dB apart.
  - ff -17.6 to fff -11.3: 6.3 dB.
  - The master has 5.3 dB between pp and p, but the ride's 2.5:1 lift below the knee and its +10 dB cap remove most of it.
- **The coda.** Its pp chorale and Tempo I deliver at -28.3..-30.1. That is as loud as the p bars of the transition and the development (43-45, 107-108, 126-127, 145: -28..-30).
- **The top of the distribution.**
  - mp3 max-p75 is 9.4 dB, against 4.8-6.4 in the three recordings.
  - p99-p90 is 5.2 dB, against 1.5-3.1.
  - The span is fixed at 16-19 dB (BRIEF item 6). About 5 dB of it sits above the ff plateaus, and the soft half is squeezed to p50-p10 = 5.5 dB, against 7.6-11.7 in the recordings.

**Inferred effect.** On one headphone volume the pp chorale and Tempo I of the coda sound no softer than any p passage of the movement. Meanwhile the two fff climaxes jump further above the ff music than they do in a real recording.

**Fix (delivery plus level only, no re-render needed for either part).**
- `tools/deliver_master.py`: `TOP_ABOVE, TOP_RATIO = -3.0, 1.6` -> `-3.0, 2.5`. The top ride acts only above p95 - 3 dB, which here means bars 25-26, 116-124, 140, 158-162 and 169-170.
- `build/score_config.py` line 1471, the c26 coda shape: `_coda26 = [(695.5, 0.0), (695.875, -2.0), (732.0, -2.0)]` -> `[(695.5, 0.0), (695.875, -3.5), (732.0, -3.5)]` (simulated as -1.5 dB from 695.6/695.95; the difference is inside the rest before the chorale). The same object goes to `_all` and to the Tam-tam, so the morendo, the Tempo I +1.5 and the celli/basses 721.5-729 shapes keep their relative steps.

**Simulated (both, together with finding 1 and finding 3; the master gain is the same as the mix change).**

| | c29 | Simulated |
|---|---|---|
| Span | 19.5 dB | 19.5 dB |
| LRA | 14.6 LU | 15.2 LU |
| Limiter | 2.1 dB | 1.3 dB |
| p50-p10 | 5.5 dB | 6.4 dB |
| max-p75 | 9.4 dB | 8.6 dB |
| Inversions | 0 | 0 |
| Share kept | 0.78 | 0.77 |

- **By printed dynamic:** ppp -37.2, pp -30.3, p -28.1, mp -24.6, mf -24.4, f -21.8, ff -17.4, fff -11.6. pp now sits 2.2 dB under p (c29: 0.8).
- **Coda bars 175-182 (mp3):** -30.8 -29.6 -30.2 -30.0 -30.4 -30.5 -31.4 -37.2. They stay above the intro's quietest bars 4-5 (-33.0 / -33.3).
- **Climaxes on S max:** 160 -10.60 > 122 -11.59 > 170 -12.95 > bar 26 -14.40. Margins: 160 over 122 1.0 dB (c29 1.2), over 170 2.35 dB (c29 3.15).
- **Rise of 160** over the 20 s before it: 14.3 -> 13.5 dB.
- **Loudness motion (`tools/motion.py`):** 4.54 -> 4.47 dB, dS4 p90 8.69 -> 8.59. Both falls are under the loop's 0.2 dB regression mark.

**Gentler option.** TOP_RATIO 2.0 with `_coda26` at -3.0:
- span 19.6, LRA 15.0, p50-p10 6.1, limiter 1.6;
- pp -30.0 against p -28.2;
- 160 -10.34 > 122 -11.35.

**Criterion.**
- mp3 span 16-19.6 dB, LRA 14-16 LU, 0 inversions, limiter at most 2.5 dB.
- Order 160 > 122 > 170 > 26 on S max, with 160 over 122 by at least 0.8 dB.
- Median pp bar at least 1.5 dB under the median p bar.
- Coda 175-181 delivered under every p bar listed above and above -33 dB.

## 3. The coda cello solo grows 3 dB in the mp3 while the master holds it level: the ride's lift is still recovering from the ff fermata (measured; simulated fix)

**Where.** Bars 171-174 (qn 680-696), Più lento. Celli mp espr. with five small swells to the crest at 174, and the cor anglais p imitation. Score page 17.

**Evidence (measured).**
- **Bar level:**

  | Bar | 171 | 172 | 173 | 174 |
  |---|---|---|---|---|
  | Master | -29.6 | -29.2 | -29.6 | -29.8 |
  | mp3 | -26.7 | -24.8 | -24.3 | -23.6 |

- **Ride gain per qn (mp3 M minus master M):** +2.0 at 680, +3.5 at 683, +4.9 at 688, +6.3 at 693. The 3 s smoothing carries the zero lift of the ff fermata chord (676-679) about 12 s into the solo.
- **The first beat.** The solo's opening beat delivers at -29.9, 4 dB under its next two beats (-25.6 at 682-683).
- This is the same mechanism c26-C described. The c26 and c28 coda shapes fixed the chorale and the 689-693 steps, not this growth.

**Inferred effect.**
- The mp solo is heard as a slow 4-bar crescendo that the score does not print. Its printed shape is level mp with swells and a crest at 174.
- The first notes after the fermata sound distant.

**Fix (level only, stem fix can apply it).** `build/score_config.py`, with the coda shapes (after line 1473):

```python
# c30 C #3: the ride's lift rises +2 -> +6 dB across the cello solo (171-174) after the ff fermata, so the mp solo grows
# 3 dB in the mp3 with a level master; lift its first bars in the mix and hand over to the ride by 691
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(679.80, 0.0), (679.88, 2.0), (685.0, 2.0), (691.0, 0.0)]]
```

- The shape starts after the fermata chord's tail has fallen below -60 dB (679.75 master -63.9). It is at full value before the first moved onsets (violas 679.904, celli 679.928).
- It adds at most +0.7 dB to the c28 steps at 689.18-691 and nothing from 691, so 692 stays the solo's crest.
- The perc tracks are silent there.

**Simulated (master gain, with findings 1-2).**
- mp3 bars 171-174: -25.1 -23.7 -24.0 -23.4. The growth goes 3.1 -> 1.7 dB, and the first beat 680 goes -29.9 -> -28.4.
- 692 stays the crest of 684-694, at -19.7 against -24.0 at 690-691.
- The drop from the fermata chord (677) to the solo (681) is 14.6 dB in the mp3 (c29 15.9; master 20.0).
- The chorale stays 6 dB under the solo (c26-C's criterion was at least 2.5).

**Criterion.**
- mp3 bar 174 minus bar 171 at most 2 dB.
- 692 still the loudest qn in 684-694.
- mp3 drop from 677 to 681 at least 13 dB.

## Measured, no change proposed

- **Recapitulation second theme hairpins** (Oboe 1 580-582, celli 596-598, Horn 1/celli 589-591): repeatable sample shapes (above). A trim change does not turn them around.
- **Bar 129.** The mf arrival after the bar-128 crescendo delivers 0.9 dB under 510 (master flat). That is small, and the Clarinet 1 shapes there are c26's.
- **Letter G.** The ff plateau (bars 116-120) sags 1.2 dB in the mp3 (master 0.5 dB) under the top ride before 121's crescendo. Finding 2 adds about 0.4 dB to this sag. The arrival at 122 still rises 3.8 dB.

## Do not touch

- The climax order 160 > 122 > 170 with ARRIVAL_WEIGHT_AT 484/636, the letter-G hold and the c22 `_sost` shape.
- The bar-121 and bar-159 crescendo shapes, the crash shape, and the tam-tam stroke and `_damp` at 504.2 (finding 1 only lifts the ring between them).
- The delivery RATIO 2.5, CAP 10, knee, 3 s smoothing, FAST_CAP_ABOVE 4 and MOM_CAP_ABOVE 6 (finding 2 changes TOP_RATIO only).
- The morendo and the celli/basses 721.5-729 shapes, Tempo I +1.5, and the c28 coda celli/cor anglais steps (findings 2-3 only offset them).
- The re-bow rows, breath splits and loop fills (item 7 passes), and the accent swells, fits and cuts (item 8 passes).
- Every c29 and earlier do-not-touch item in HISTORY.md.

# Cycle 26, critic C: dynamics over time (render c25)

Lens: the shape of every hairpin and phrase; the loudness arc against the score (the sostenuto climax with the tam-tam at bars 122-126, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda); loudness range of the master and the mp3 (BRIEF item 6); swells and loop pulsing on held notes (item 7); decays; comparison with real recordings.

## Method

- Material: the stem-fixed c25 render (`cycles/c25/render/`, 33 stems and master), `mvt1-mockup-c25.mp3`, and `build/parts.json` (11:18, the stem-fixed c25 state; its tempo map is identical to `cycles/c25/rendered_build/parts.json`).
- Loudness: ffmpeg ebur128 at 10 Hz, with M shifted 0.2 s and S 1.5 s so the windows are centred. Stem levels are plain stereo power in 10 ms frames.
- Simulations:
  - Level shapes were applied to the c25 stems and summed (`simshape.py`), or a gain was applied to the master (`mgain.py`).
  - The result was delivered through a copy of `tools/deliver_master.py` (`dmb.py`). With no change, the copy reproduces c25 exactly: LRA 14.4 LU, span 19.1 dB, limiter 2.2 dB.
- Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c26-C/`. They are the c22-C set pointed at c25, plus these new ones:
  - `swell2.py`: unprinted swells and sags on held notes;
  - `dist.py`: S distribution against the recordings;
  - `cmpd.py`: per-bar comparison of delivered variants;
  - `dmb.py`: the ride with optional segment breaks.

## State of the arc (measured)

**Master and mp3.**
- Master: -16.4 LUFS, LRA 22.5 LU. Bar level against the bar's loudest printed dynamic: r = 0.888 (c21 0.886).
- Delivered: -19.8 LUFS, LRA 14.4 LU, limiter 2.2 dB, 268 five-second moves with a median share kept of 0.78 and 0 inversions.
- The p10-to-max span is 19.1 dB, 0.1 dB over the brief's 16-19 dB.

**Climaxes.**
- Order on delivered S max: 160 -10.0 > 161 -10.3 > 159 -10.7 > 122 -11.1 > 123 -11.2 > 121 -12.1 > 170 -13.2.
- The master's rise over the median of the 20 s before each climax:

  | Climax | Master | Delivered |
  |---|---|---|
  | qn 636 (bar 160) | 22.2 dB | 14.6 dB |
  | qn 484 (bar 122) | 5.7 dB | 5.4 dB (it follows the letter-G ff) |
  | letter G | 13.3 dB | 8.9 dB |

**The arrivals hold.**
- Bar 121 crescendo: master M per beat -12.4 -11.6 -10.9 -9.5, then 122 at -7.2.
- Bars 122-123 hold within 1.4 dB (the c22 `_sost` shape).
- Bars 124-126 fall smoothly from -13.4 to -30.7 dB per beat over 7 s.
- Bar 159 crescendo: -10.7 -9.8 -8.6 -7.9, then 160 at -6.0.
- Recapitulation 131: -15.3..-15.9 per beat. The exposition ff (bars 27-31) is -15.2..-16.0.

**Hairpins per track.**
- 429 hairpins; 56 move less than 1 dB the printed way (c21: 52).
- Crescendo median +4.9 dB, decrescendo median -5.3 dB.

**Against the recordings** (S distribution, dB):

| | p50-p10 | p90-p50 | p99-p90 | max-p95 | max-p75 |
|---|---|---|---|---|---|
| Brahms 1/i | 11.2 | 6.7 | 2.2 | 2.6 | 4.9 |
| Brahms 4/i | 7.6 | 5.0 | 3.1 | 3.8 | 6.4 |
| Dvořák 9/i | 11.7 | 12.4 | 1.5 | 1.6 | 4.8 |
| c25 master | 8.5 | 12.4 | 7.0 | 5.9 | 13.1 |
| c25 mp3 | 5.1 | 7.5 | 5.4 | 4.6 | 9.3 |

The delivered soft half is still squeezed: p50-p10 is 5.1 dB against 7.6-11.7 in the recordings. c18-C showed the ride parameters cannot open it inside the span. Findings 1 and 2 open it to 5.8 dB in the mix.

**Item 7 passes (measured).**
- Master 100-300 Hz band / centroid autocorrelation at 3.95 s:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | +0.05 | 0.00 |
  | Bars 43-46 | -0.03 | +0.17 |
  | Coda 175-178 | +0.03 | +0.14 |
  | Tempo I 179-182 | -0.14 | -0.02 |
  | Bars 122-126 | +0.02 | -0.11 |

- Bars 73-76 read -0.47 / -0.21 (rhythm, not loop).
- The c25 loop scan already split the wind and brass notes.

**Item 8 passes (measured).** 2-5 kHz over the first 80 ms minus the body:

| Family | n | Median | p90 |
|---|---|---|---|
| Strings | 171 | -6.5 | -3.2 |
| Winds | 234 | -8.1 | -3.1 |
| Brass | 172 | -9.5 | -3.9 |
| Timpani | 14 | -11.0 | -7.7 |

The only outlier is Violas 536 at +11.1 (the known masked double stop).

**Decays (measured).**
- The fermata rest at 679.5 falls 52 dB in 2.2 s.
- The final ppp chord follows the morendo from -42.7 (724) to -52 (727.5). After the note-off at 728 it decays about 28 dB per second (-62.5 at 433.5 s, -91 at 434.5 s), a natural hall tail.
- The tam-tam fff at 484 decays about 2.5 dB/s until the damp at 504.2.

## 1. The coda dies away on the master but plays as a plateau in the mp3: the pp chorale is as loud as the mp cello solo before it (measured; simulated fix)

**Where.** Bars 171-182 (qn 680-729): Più lento, the celli's mp espr. solo (171-174), then the pp chorale with the tam-tam pp (175-178), Tempo I pp (179-180), and the morendo to ppp (181-182). Page 17 of the score.

**Evidence (measured, per-bar momentary power mean, dB).**

| Bar | 171 | 172 | 173 | 174 | 175 | 176 | 177 | 178 | 179 | 180 | 181 | 182 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Printed | mp | | | | pp | | | | pp | | > | ppp |
| Master | -30.1 | -30.3 | -31.0 | -31.9 | -34.8 | -34.2 | -34.7 | -34.9 | -36.8 | -36.7 | -37.9 | -43.4 |
| mp3 | -26.9 | -25.3 | -25.1 | -25.4 | -27.4 | -26.4 | -26.8 | -26.8 | -28.6 | -28.6 | -29.7 | -35.2 |

- **Solo against chorale.** The master falls 4.4 dB from the solo (171-174) to the pp chorale (175-178). The mp3 falls 1.0 dB, and bar 176 (pp) delivers louder than bar 171 (mp).
- **The whole coda.** The master's twelve-bar dying away (13 dB) is 8 dB delivered, and 5.5 of those 8 dB are in the last bar. Bars 171-178 deliver within 2.3 dB of each other.
- **Cause: the ride's lift.** Lift per qn: 680 +3.8, 684 +6.0, 688 +7.3, 692 +8.1, 696 +8.9, 704 +9.7, then +10.0 (the cap) from 710. The lift grows 5 dB across the solo, because the 3 s smoothing carries the zero lift of the ff bars 167-170 forward into it. That cancels the master's fall into the chorale.
- **Where a mix cut passes.** From 696 the lift is at or within 1.1 dB of the cap. A mix cut there passes into the mp3 almost 1:1. This is the region where c18-C said soft-half mix work is passed on.

**Inferred effect.** On headphones the coda does not die away: the pp chorale and Tempo I sound as present as the cello solo, and the music only fades in the last bar. The ppp ending is louder than the Lento's pp at bars 4-5 (mp3 -32.9 / -33.2).

**Fix (level only; stem fix can apply it).** `build/score_config.py`, after the c24 morendo/coda shapes:

```python
# c26 C #1: the coda's pp chorale and Tempo I 2 dB down on every track (the ride is at its cap there, so it passes)
_coda26 = [(695.6, 0.0), (695.95, -2.0), (732.0, -2.0)]
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [_coda26]
LEVEL_SHAPES["Tam-tam"] = LEVEL_SHAPES.get("Tam-tam", []) + [_coda26]   # perc tracks do not read "_all" (line 4593)
```

Timpani (family "timp") goes through `build_track` and reads `_all`, so it needs no line of its own.

- The shape starts after the solo's last note (the chorale's moved onsets lead 696 by up to 0.30 s; 695.6 keeps the fall complete before them).
- It adds the same offset to the morendo, the celli/basses 721.5-729 shapes and the Horn 3 notch, so none of their shapes change.
- Harp's ppp at 724 goes through `_all`.

**Simulated (master gain on c25, then the delivery copy).**

| Bar | 171 | 172 | 173 | 174 | 175 | 176 | 177 | 178 | 179 | 180 | 181 | 182 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mp3, -2 dB | -26.9 | -25.4 | -25.0 | -25.4 | -29.1 | -28.2 | -28.7 | -28.8 | -30.7 | -30.7 | -31.8 | -37.3 |

- **Solo against chorale:** 1.0 -> 3.0 dB (master 4.4).
- **Coda shape:** the coda now falls in steps 174 -> 175 -> 179 -> 181 -> 182, as printed.
- **Whole file:**

  | | c25 | -2 dB coda |
  |---|---|---|
  | LRA | 14.4 LU | 15.2 LU (the centre of 14-16) |
  | p50-p10 | 5.1 dB | 5.8 dB |
  | Span | 19.1 dB | 19.9 dB |
  | Limiter | 2.2 dB | 2.1 dB |

  The other measures are unchanged: 0 inversions, median share 0.78, climax order and values within 0.1 dB.
- **Gentler option, -1.5 dB:**
  - span 19.7 dB, LRA 15.0 LU;
  - chorale 175-178 at -27.6..-28.5, contrast 2.5 dB.
- **The span.** The coda is about 10% of the file, so it sets p10. Its pp bars then deliver at -30.7..-31.8, still above the Lento's -32.9 / -33.2, so soft passages stay as audible as they are now. I recommend -2 dB, and accepting a span 0.9 dB over the guideline in exchange for the printed morendo. This is the actor's call against BRIEF item 6.

**Not proposed: a ride break at the fermata rest (tried, measured).** I re-smoothed the ride separately after the silent fermata rest at 679.5, where the master stays under -48 LUFS M for 0.8 s; it is the only loud-to-soft rest in the movement.
- It lifts bar 171 by +2.9 dB and lets the coda's fall through.
- It also shrinks the drop from the bar-170 ff fermata to the Più lento from 11.1 to 8.2 dB delivered. The master's drop is 16.1 dB, and comparable ff-to-pp drops elsewhere deliver about 85%, for example 83 -> 84 at 14.9 of 17.8 dB.
- The mix cut keeps that drop.

**Criterion.**
- Delivered bars 175-178 at least 2.5 dB under the mean of 171-174.
- Delivered 179-181 under 175-178.
- LRA 14-16 LU, limiter at most 2.5 dB, 0 inversions.
- Delivered S max of 160, 122 and 170 within 0.2 dB of c25.

## 2. The retransition crescendo into the recapitulation (bars 127-128, pp/p < mf) is flat for its first two bars; the rise happens only at bar 129 and 130 (measured; simulated fix)

**Where.** qn 504-512.
- Clarinet 1's p solo with a hairpin to mf at 129. It is the loudest stem, 1-2 dB under the master.
- Under it: Horns 3-4 pp <, celli tremolo pp <, basses pp <, timpani pp <.
- Then bar 129 mf, bar 130 f < into the ff recapitulation at 131. Page 11 of the score.

**Evidence (measured).**
- **Master power per qn, 504-517:** -34.8 -34.1 -33.8 -33.9 -32.9 -35.1 -33.6 -33.0 | 512: -32.7 -28.8 -29.1 -28.7 | -25.3 -24.4. That is +1.8 dB over the two-bar hairpin, then +4 at 513 and +7 by 517.
- **Per bar:**

  | Bar | 127 | 128 | 129 | 130 | 131 |
  |---|---|---|---|---|---|
  | Master | -31.8 | -31.0 | -27.0 | -19.8 | -15.5 |
  | mp3 | -29.1 | -28.6 | -25.6 | -19.7 | -16.2 |

  Delivered per qn rises only +0.7 dB over 504-511.
- **Clarinet 1 stem per qn:** -37.2 -35.0 -37.6 -37.3 -35.3 -37.1 -35.3 -36.2 -36.5, then the mf at 513 at -31.6. The stem moves +0.1 dB over its hairpin (`hpexp.py`).
- **The controllers do move.** CC11 rises 46 -> 72, and the volume envelope already carries the c18 shapes (net about +5.8 dB from 505 to 512).
- **Why the stem is flat.**
  - The line descends E-flat5 -> D -> C-sharp -> C -> B3 -> C -> A-flat4 -> G4 into the clarinet's weaker throat and low register.
  - The two accent fits at 505 (+3.24) and 510 (+5.0) make bumps at both ends of the hairpin. The notes between sag back.
- **The accompaniment does grow:** celli +9, basses +9, timpani +11, Horn 4 +9 dB. It sits 8-15 dB under the clarinet.

**Inferred effect.** The ear follows the clarinet, so the approach to the recapitulation stands still for two bars (3.8 s) and then rises in a step at the mf.

**Fix (level only; stem fix can apply it).** `build/score_config.py`, after the c18 Clarinet 1 shapes (line 903):

```python
# c26 C #2: Clarinet 1's p < mf (505-512) still flat on the stem (+0.1 dB; the line falls into the throat/low register)
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(504.75, 0.0), (511.5, 4.0), (512.9, 4.0), (513.2, 0.0)]]
```

The shape starts after the pickup lift (504.5-505.0) and returns to the existing mf line at 513. The 513 E-flat5 (-31.6) stays the louder note.

**Simulated (stems).**
- Master per qn 504-513: -34.8 -33.7 -33.3 -33.1 -31.5 -33.2 -31.0 -30.7 -30.7 -28.7. The hairpin rises +4.1 dB (was +1.8), with no step at 513.
- Delivered per qn 504-513 (with finding 1):

  | | 504-511 | 512 | 513 |
  |---|---|---|---|
  | c25 | -29.2..-28.5 | -27.2 | -25.0 |
  | Fix | -29.5..-26.4 | -26.1 | -25.4 |

  Bar 128 goes -28.6 -> -26.6.
- Limiter, LRA and climaxes are unchanged (the combined run is the one in finding 1).

**Criterion.**
- Clarinet 1 stem over 510.5-512 at least 3 dB over 505.5-507.
- Master over 510-512 at least 3 dB over 504-506.
- No master qn in 508-516 lower than the qn before it by more than 1 dB, except 509, where the c25 dip is the clarinet's breath.

## 3. Lento bar 3: the opening motif's second swell (pp < >, qn 8-12) rises 3 dB, against 7 dB for the identical first swell in bar 2 (measured; simulated fix)

**Where.** Celli, basses and bass clarinet in unison, pp, with the same printed `< >` in bars 2 and 3 (CC11 34 -> 56 -> 34 in both). It is the movement's first melodic idea, and the celli are the loudest stem (exposure -3.1 dB). Page 1 of the score.

**Evidence (measured, master power per half qn).**
- Bar 2 (4.0-8.0): -37.6 -36.2 -36.4 -36.0 -34.1 -30.5 -33.4 -35.3. The crest is +7.1 dB over the start, at 6.5-7.0.
- Bar 3 (8.0-12.0): -36.2 -34.9 -35.5 -35.9 -33.6 -33.8 -37.3 -40.6. The crest is +2.6 dB over the start, at 10.0, and 3.1 dB under bar 2's crest.
- Celli per quarter qn over 8-10: -39 -39 -37 -36 -39 -40 -40 -41 -40, then 10.0 -36. The c18 fill (8.82-9.2 +7) closed the old 7 dB hole, but the note still sags 2-4 dB through 9.0-10.0. The descending B-flat -> A-flat -> G line ends below the crest that bar 2 reaches.

**Inferred effect.** The second gesture of the opening sounds weaker than the first. As printed, it is the same swell rising to the D-flat.

**Fix (level only).** `build/score_config.py`, after the c18 bar-3 fills (line 910):

```python
# c26 C #3: bar 3's swell to the D-flat (qn 10) +3 dB at its crest, matching bar 2's
for tn_ in ("Violoncellos", "Double basses", "Bass clarinet"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES[tn_] + [[(8.5, 0.0), (9.75, 3.0), (10.25, 3.0), (11.0, 0.0)]]
```

**Simulated (stems).** Master per half qn from 8.0: -36.2 -34.4 -33.9 -33.2 -30.9 -32.7 -37.3 -40.6. That is a crest of +5.3 dB, at 10.0, 0.4 dB under bar 2's. The decrescendo 10-12 is kept. Peaks are unchanged (the movement's peak is at 484).

**Criterion.**
- Master crest of bar 3 (max half qn in 9.5-10.5) within 1.5 dB of bar 2's (6.0-7.0).
- Rise over 8.0-8.5 at least 4.5 dB.
- No half qn in 8.5-10.0 lower than the one before by more than 1 dB.

## 4. The coda cello solo's first swell (qn 680-683.5, mp <) peaks 1.2 s early and sags 4-5 dB before its top (measured, repeatable c22-c25; simulated fix)

**Where.** Violoncellos, the held E-flat4 that opens the Più lento solo (sq 680, 3.35 qn = 2.8 s). Printed mp `<` to 683.5 (HP_TARGET_AT mf), then `>`. The celli are the coda's melody (exposure -0.6 dB).

**Evidence (measured, celli stem per 0.2 s from the onset).**
- -36.3 -35.6 -37.0 -33.1 -34.3 -32.1 -32.9 -33.7 -31.1 -32.3 -35.0 -36.1 -36.0 -31.9 -34.7.
- The note peaks at 1.6 s, then falls 4-5 dB at 2.0-2.6 s while CC11 still rises (70 -> 74). The volume envelope there is flat (-1.5 dB until 683.25).
- The values are identical in c22, c23, c24 and c25 to 0.1 dB, so it is the sample (inferred).
- The master follows it: -31.2 at 1.6 s, -34.6 / -35.6 / -34.7 at 2.0-2.6 s.

**Inferred effect.** The solo's first crescendo turns back before its top, so the line's opening sounds hesitant rather than espressivo.

**Fix (level only).** `build/score_config.py`, with the coda shapes:

```python
# c26 C #4: the coda solo's first note sags 4-5 dB at 682.4-682.9 before the hairpin top (sample, repeatable)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(682.15, 0.0), (682.55, 3.5), (683.15, 3.5), (683.3, 0.0)]]
```

The shape ends before the 683.5 note's moved onset and its existing step (683.25-683.27).

**Simulated (master per 0.2 s from 680).** At 1.8-2.6 s: -30.9 -31.7 -32.3 -31.8 -29.4 (c25 -31.8 -34.6 -35.6 -34.7 -30.2). The crest is now at the hairpin's end (2.6 s) and 1.8 dB over the 1.6 s peak.

**Criterion.**
- Celli 2.0-2.6 s at most 1.5 dB under the 1.4-1.8 s level.
- The 2.6-2.8 s window is the note's loudest.

## Measured, no change proposed

- **Climax margins.** Delivered S 160 over 122 is 1.1 dB; M 160 -9.1 > 122 -10.5. The letter-G hold, the bar-121 shape and the `_sost` shape hold the order.
- **Hairpins still under 1 dB.**
  - The second-theme swells (147-155): Horn 1 589 -1.6, celli 596/598, violas 596 +3.5. These lie inside the c12/c16/c24 shape sets, which move 1-2 dB between renders.
  - Violas bar 110 (-7.0 dB): the hand +5 dB note trim on its A-flat5 at 436 makes the hairpin's start the line's peak. The master still rises into 111.
  - The Oboe 1 bar 146 decrescendo (+2.3): it ends on the c23 B #3 shape, and the oboe sits 3 dB under the master.
- **The delivery ride.** The long crescendos keep 51-60% of their master rise in the mp3: bars 9-12 +13.6 -> +8.0, 111-117 +13.4 -> +8.1, 156-158 +6.6 -> +3.4. That is the 2.5:1 ride by design. c18-C's 12 variants showed the parameters cannot change it inside the span. Findings 1-2 are mix work instead.

## Do not touch

- The delivery settings: RATIO 2.5, CAP 10, 3 s smoothing, TOP_RATIO 1.6, FAST_CAP_ABOVE 4, MOM_CAP_ABOVE 6.
- Climax order 160 > 122 > 170, with ARRIVAL_WEIGHT_AT 484/636, the 636 strokes and E6 fill, the bar-121 shape, the letter-G hold and the c22 `_sost` shape.
- The timpani 632-636 and crash shapes, and the tam-tam damp at 504.2 with its bell.
- The morendo 724-729 and the celli/basses 721.5-729 shapes (finding 1 only offsets them).
- The c18 bar-3 fills and the Clarinet 1 504.5 pickup lift (findings 2-3 add to them).
- The re-bow rows and breath splits (item 7 passes), and the accent swells and fits (item 8 passes).
- Every c25 do-not-touch item in HISTORY.md.

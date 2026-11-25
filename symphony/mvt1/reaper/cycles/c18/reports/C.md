# Cycle 18, critic C: dynamics over time (render c17)

Lens: the shape of hairpins and phrases; the loudness arc against the score (bars 121-126 with the tam-tam, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda); the loudness range of the master and the mp3 (BRIEF item 6); swells and loop pulsing on held notes (item 7); decays; comparison with a real recording.

## Method

- **Material.** I measured the stem-fixed c17 render (`cycles/c17/render/`, where the master is the float sum of the stems) and `mvt1-mockup-c17.mp3`, against `build/parts.json` (21:16, the stem-fixed state). Score qn maps to file time through the parts.json tempo map.
- **Loudness.** ffmpeg ebur128 at 10 Hz. M is shifted 0.2 s to centre it; S is shifted 1.5 s. Stem levels are plain stereo power in 10 ms frames.
- **Simulations.**
  - Piecewise dB shapes in qn are applied to the c17 stems and summed (`simshape.py`).
  - The sum then goes through a copy of `tools/deliver_master.py` with its parameters exposed (`dmx.py`).
  - With no shapes, this chain reproduces c17 exactly: LRA 14.4 LU, span 19.1 dB, limiter 2.3 dB, peak 1.538.
- **Scripts.** All in `/private/tmp/claude-501/mockup-loop/mvt1-c18-C/`.
  - The c14-C battery, pointed at c17: `bars.py`, `hp.py`, `hptrack.py`, `mw.py`, `climax.py`, `swell.py`, `loops.py`, `loops2.py`, `msweep.py`, `evalm.py`.
  - New:
    - `arr.py`: each crescendo's arrival against its top;
    - `hpexp.py`: per-track hairpins on exposed stems;
    - `tw.py`: per-track windows;
    - `ev3.py`: score marks;
    - `win2.py`: loop autocorrelation per window;
    - `ev4.py`: delivery contrasts and climax;
    - `stemsim.py`, `simwin.py`, `simrun.sh`;
    - `cym.py`: suspended cymbal bands.

## State of the arc (measured)

**Master and delivery.**
- Master: -16.4 LUFS, LRA 22.2 LU (the Dvořák 9/i reference measures 21.8).
- Bar level against the bar's loudest printed dynamic: r = 0.885 (c13 0.88).
- Delivered: LRA 14.4 LU, p10-to-max span 19.1 dB (0.1 over the target), limiter 2.3 dB, -1.7 dBTP.
- 5 s moves (265 of them): median share kept 0.79, 0 inversions.

**Climax order holds.**

| Bar | Delivered S max | Delivered M max |
|---|---|---|
| 160 | -9.99 | -9.40 |
| 122 | -11.17 | -10.11 |
| 167-170 | -12.94 | -10.76 (bar 170) |

- Bar 160 is 1.8 dB over bar 159 on M.
- The bar-159 crescendo (30 tracks) grows +2.5 dB. The fff arrives +1.9 dB over its last beat. Bars 160-161 hold within 1 dB.

**Bars 121-126.**
- The bar-121 crescendo arrives with a +2.7 dB step at the tam-tam fff (master M per beat: 483 -9.8, 484 -7.1).
- The sostenuto bar 123 sits 1.5-2.3 dB under the downbeat of 122.
- Bars 124-126 fall smoothly, -14.4 -> -28.4 dB.
- I tried a +3/+4 dB hold on Horns 1-2 (which decay 5-9 dB inside their fff whole notes). It moved the master only 0.2 dB, so the sag is shared by every family. No change proposed.

**Coda.**
- The final ppp morendo falls steadily: master 724 -41.2, 726 -44.2, 727 -48.4.
- The pp chorale of bars 175-180 holds -34..-37 dB.

**Item 7.**
- Master sliding 10 s windows flag only:
  - two-bar rhythmic patterns in the Allegro (bars 25, 40, 67-69, 78, 90, 129-131);
  - Lento bars 6-8 (centroid 0.40-0.44, 100-300 Hz 0.35), where no stem passes 0.30 (cor anglais 0.27, violas 0.30). I take this to be the solo's rhythm (inferred).
- Stem flags over 6 s are the same set as c14: masked stems or repeated-note patterns.
- Re-bows and timpani re-strikes stay at or under 0.35.

**Suspended-cymbal roll, bar 159.**
- Its 4-12 kHz band is 50-75 dB under the master until qn 633.5, and reaches -5 dB at 635.5.
- The tutti is ff with a crescendo in that bar, so a real pp roll would also be covered until it swells (inferred). No change proposed.

**Arrivals.** Of the 26 crescendo endings with 4 or more parts, only two arrive under the crescendo's own top while the score asks for a rise: qn 464 (-2.0 dB) and qn 512 (-1.9 dB). The others under their top are phrase ends, the subito p at 244, or the punctuating ff chord of bar 97. Findings 1 and 2 cover the two.

## 1. Letter G (bar 117): the ff tutti arrives 1.1-2.0 dB under the top of the six-bar crescendo, because the c14/c16 letter-G hold starts one bar late (measured, simulated)

**Where.** qn 460-480: the `mp cresc.` from bar 111 to ff at 117 on every part, then ff held to the bar 121 allargando.

**Evidence (measured).**
- **Master M per beat, 460-467:** -13.8 -12.1 -12.2 -13.5 | -13.7 -13.1 -13.6 -14.1.
  - Bar 116, beats 2-4: -12.5 dB. Bar 117: -13.6 dB.
  - Delivered M max: bar 116 -13.79, bar 117 -15.25.
  - Every other tutti arrival after a crescendo in the movement steps up (+0.5 to +4.7 dB over the crescendo top): bars 26, 69, 122, 138, 158, 160, 167, 170.
- **Score (page 10).**
  - Trumpets and Clarinets reach ff in bar 116. At 117 the trumpets stop (as printed) and the clarinets drop to f triplets.
  - The tutti ff arrival at 117 is 4 horns (1-2 a2), trombones a2, bass trombone, tuba, bassoons, contrabassoon, bass clarinet and strings.
- **Why it is weak.**
  - The c14 hold (`score_config.py` line 706) and its c16 successor `_lg_new` (line 810) start at 467.6 and are full only at 468.6. The arrival bar 117 has none of it, while bars 118-120 get +2.5 dB.
  - On the arrival, Horns a2 measure -32.1 dB, under Horn 3 alone (-28.6). Brass as a family falls from -19.6 (462) to -21.2 (464).

**Fix.** `build/score_config.py`, the c16 replacement loop at line 809-813. Start `_lg_new` at the arrival and add 1 dB through bars 118-120:

```python
_lg_new = [(463.9, 0.0), (464.05, 3.0), (467.6, 3.0), (468.6, 3.5), (479.6, 3.5), (483.5, 4.0), (484.0, 0.0)]
```

- Same ten tracks (Horn 3, Horn 4, Horns a2, Bass trombone, Tuba, Contrabassoon, Violins II, Bassoon 1, Bassoon 2, Bass clarinet).
- It is level-only, so the stem fix can apply it.
- The Double basses shape and `ARRIVAL_WEIGHT_AT` 484 are unchanged.

**Simulated on the c17 stems (`s1d`).**

| | Master 116 beats 2-4 | 117 | 118 | 119 | 120 | 121 | 122 |
|---|---|---|---|---|---|---|---|
| c17 | -12.5 | -13.6 | -14.0 | -14.8 | -14.0 | -11.5 | -7.9 |
| fix | -12.4 | -11.8 | -13.3 | -14.2 | -13.4 | -11.3 | -7.9 |

- Delivered M max: bar 116 -14.05, bar 117 -13.66.
- The bar-121 crescendo and the step into 122 are kept (+2.1, +3.4 dB).
- Whole file: LRA 14.5, span 19.1, limiter 2.2 dB.
- A +2.5 dB arrival with no change to 118-120 (`s1`) also lifts the arrival (+0.3 dB). But it leaves bars 118-120 2.2 dB under 117 on the master and 2.4 dB under on the mp3, which brings back the c14 sag.

**Criterion:**
- master bar 117 at least 0.5 dB over bar 116 beats 2-4;
- bars 118-120 within 2 dB of 117;
- bar 122 at least 3 dB over bar 121 on M.

## 2. Recapitulation approach (bars 127-129): the pp < mf build grows only +1.4 dB, because Clarinet 1 starts its p solo 8-11 dB hot and then falls after its mf, and the celli eighths sag (measured, simulated)

**Where.** qn 504-520 (page 11).
- From the a tempo, Clarinet 1 has a p < mf solo (504.5-512).
- Under it, celli unis., basses, timpani and Horn 4 play pp < mf (512), then f (516) < ff (520).

**Evidence (measured).**
- **Master by window:**

  | qn | 505-508 | 508-512 | 512-516 | 516-520 |
  |---|---|---|---|---|
  | master (dB) | -31.2 | -29.8 | -27.9 | -19.6 |
  | delivered (dB) | -28.7 | -27.6 | -26.7 | -19.7 |

  - Two bars of printed pp < mf rise +1.4 dB (delivered +1.1).
  - `hp.py`: 504-512 arrival minus start +0.2 dB.
  - Bar 127 (pp) sits only 1.2 dB under the p bar 126 on the mp3.
- **Clarinet 1** is the loudest stem (-33..-37 dB). Per beat 505-516: -33.3 -34.7 -37.9 -34.1 -35.2 -32.6 -34.9 | -36.7 -34.3 -36.9 -37.4. It does not grow, and falls after the mf.
  - Its volume envelope is +8.4..+11 dB from 505. That is the roles +5 [504,520] and +2 [504.5,512], the accent fit 3.24 at 505, and the 9.5 dB pickup lift to 505.0.
  - The c06 shape `[(504.5,0),(512,3),(513,3),(514,0)]` (line 210) takes 3 dB away at 513-514, while CC11 holds 72 (mf) to 518.75. The stem falls to -41.0 at 516-517.
- **Celli.** The pp quarters measure -48.1 / -48.1 / -39.1 / -43.5. The eighths 508-512 that carry the crescendo sit at -41.7..-45.2, because the envelope steps from -4.1 to -6.0 dB at 507.75-508.

**Fix** (`build/score_config.py`, `LEVEL_SHAPES`; all level-only):
- **Clarinet 1, start.** Add `[(504.95, 0.0), (505.05, -3.0), (508.0, -2.0), (511.0, -0.5), (512.0, 0.0)]`. The pickup lift up to 505.0 is untouched.
- **Clarinet 1, after the mf.** Replace the c06 shape at line 210 with `[(504.5, 0.0), (512.0, 3.0), (514.0, 4.5), (519.5, 4.5), (520.3, 0.0)]`, so the mf line holds through the f crescendo of bar 130. It ends before the ff at 520.5.
- **Violoncellos.** Add `[(507.7, 0.0), (508.0, 2.0), (511.7, 4.0), (511.95, 0.0)]`.

**Simulated (`sall`, with findings 1 and 4 at +2.5).**

| | Clarinet 1, 505-512 | Clarinet 1, 512-520 | Celli 508-512 |
|---|---|---|---|
| c17 | -33.3 -36.0 -34.7 -33.6 | -35.4 -37.1 -41.0 -37.7 | -43.1 / -44.9 |
| fix | -36.1 -38.4 -36.2 -34.2 | -33.7 -32.6 -36.5 -33.5 | -40.6 / -41.6 |

| Window (qn) | 505-508 | 508-512 | 512-516 | 516-520 |
|---|---|---|---|---|
| Master (dB) | -32.9 | -30.2 | -26.8 | -19.5 |
| Delivered (dB) | -30.4 | -27.9 | -25.6 | -19.6 |

- Master rise 505-508 to 512-516: +6.1 dB (was +3.3).
- p -> pp at 127 on the mp3: -2.6 dB (was -1.2).
- Whole file: LRA 14.5, span 19.1, limiter 2.3. Climax S: 160 -10.03 > 122 -11.22 > 170 -13.02.

**Criterion:**
- master 512-516 at least 4.5 dB over 505-508;
- Clarinet 1 no 1-qn window after 512 more than 3 dB under its 512-513 level before 520.

## 3. Lento bar 3: the low strings' second swell has a 7 dB hole 1 s into the crescendo, the same in every render since c15 (measured, simulated on plain power)

**Where.** qn 8-10, the bar-3 pp `<` on celli, basses and bass clarinet (page 2). It is the first 12 s of the movement, and the celli are the loudest stem.

**Evidence (measured).**
- **Master plain power per eighth-qn, 8.5-9.25:** -34.2 -32.9 -38.6 -40.2 -38.5 -35.7.
  - Celli: -36.4 -35.3 -42.2 -48.8 -48.3 -48.9.
  - Basses: -40.7 -41.3 -43.9 -46.5.
  - Bass clarinet: -42.5 -44.5 -47.8 -47.1.
  - All three samples settle 1.0-1.3 s after their 8.0 notes begin. The celli fall 13 dB.
- **The celli profile is identical in c15, c16 and c17** (to 0.1 dB; c14 within 1 dB). It does not move between renders.
- **The celli envelope makes it worse.**
  - The early fill "8" (6.1 dB, hold 0.4 s) and the loop fill "8.0" `[1.0, 5.0, 0.35]` hold +5.7..+6.5 dB to qn 8.8, then fall to +1.2 at 8.94.
  - That is 0.35 s before the sample's own dip ends. The fill builds a bump at 8.4-8.75 and then a cliff.

**Fix** (`build/score_config.py`, `LEVEL_SHAPES`):
- Violoncellos `[(8.74, 0.0), (8.82, 7.0), (9.2, 7.0), (9.32, 3.0), (9.45, 0.0)]`
- Double basses `[(8.7, 0.0), (8.82, 3.5), (9.0, 3.5), (9.15, 0.0)]`
- Bass clarinet `[(8.7, 0.0), (8.8, 3.0), (9.0, 3.0), (9.12, 0.0)]`
- In `build/loop_fills.json`, lower the celli "8.0" entry to `[[1.0, 3.0, 0.35]]` (inferred: about 2 dB off the 8.4-8.75 bump).
- The re-bow rows are untouched.

**Simulated (plain power on the stems).**
- Celli 8.75-9.5: -38.4..-42.1 instead of -42.2..-48.9.
- Master 8.625-9.125: -32.9 -35.4 -37.1 -35.8 -34.9, instead of -32.9 -38.6 -40.2 -38.5 -35.7.

**Criterion:** master eighth-qn levels over 8.0-10.0 with no step down of more than 3 dB; celli 8.75-9.5 within 5 dB of their 8.5-8.75 level.

## 4. Bassoon 1 solo, bar 34: the last note of the f > mf phrase jumps 4-8 dB over the notes before it, because its legato fill overshoots (measured, simulated)

**Where.** qn 128.5-133: the bassoon's espr. solo after the bar-33 cadence. The stem is within 1 dB of the master. The `>` runs 130.5-132 to the mf.

**Evidence (measured).**
- Bassoon 1 per quarter-qn, 130.5-132.25: -40.4 -38.5 -37.0 -36.8 | -32.6 -34.9 | -38.4.
- The C4 at 131.5 is the loudest note of the decrescendo: +4.2 dB over the note before, +7.8 over 130.5. `hpexp.py`: 130.5-132 measures +5.6 dB where the score has a decrescendo.
- Envelope: +3.0 at 130.5, -1.5..-2.0 at 131.0 (the slur join), then +6.4 at 131.37 and +8.3 to 131.75 (role +3 plus `early_fills.json` "131.5" 5.3 dB, hold 0.1 s), back to +3.0 at 132.25. CC11 falls 88 -> 77 as printed.

**Fix** (`build/score_config.py`): add `LEVEL_SHAPES["Bassoon 1"]` `[(131.47, 0.0), (131.55, -4.5), (131.75, -4.5), (132.24, 0.0)]`. This keeps the fill's part before the onset, which covers the join hole (131.25-131.375 measures -40.8). It is level-only.

**Simulated (stem).**
- 131.5-131.75: -32.6 -> -36.8; 131.75-132: -34.9 -> -38.4; 132-132.25: -38.4 -> -39.7.
- The phrase now falls 131 -> 132. The master moves with it, since the bassoon is the only voice over the low strings.

**Criterion:** no quarter-qn window of Bassoon 1 in 131.5-132.25 louder than 131.0-131.5.

## 5. The delivered mp3 compresses the soft half of the movement to 4.9 dB, and the ride's parameters cannot open it inside the span target (measured; no change proposed, so the actor does not spend a cycle on it)

**Evidence (short-term loudness).**

| | p50-p10 | p95-p50 | max-p95 |
|---|---|---|---|
| Delivered | 4.9 dB | 9.6 dB | 4.6 dB |
| Master | 8.5 dB | 14.6 dB | 6.2 dB |
| Dvořák 9/i | 11.7 dB | 12.9 dB | 1.6 dB |

- **Coda.** The mp cello solo of bars 171-174 against the pp chorale of 175-178: master -4.0 dB, delivered -1.2 dB. The pp bars 175-178 deliver at -26.6..-27.4 dB, against -24.9..-27.0 for bars 171-174.
- **Ride parameters tried** (12 variants, `dmx.py`: RATIO 1.8-2.2, TOP_RATIO 1.8-2.5, CAP 6-9, knee 8, TOP_ABOVE -4):
  - none raises p50-p10 above 5.3 dB without span 19.6-21.2 dB;
  - CAP 7 gives 6.4 dB at span 20.8;
  - TOP_RATIO 2.0-2.5 brings bar 170 within 0.3-0.6 dB of bar 160 on M.
- **Mechanism.** The 3 s smoothing and the 10 dB cap act on whole passages, so the soft contrasts inside a passage (2-5 dB) are mostly absorbed. The climax's 4.6 dB over p95 uses span budget that Dvořák spends on its soft half.

**Proposal.**
- Leave `deliver_master.py` as it is.
- If Dan asks for more pp/mp contrast on headphones, the brief's span target (16-19 dB) is what has to give, not the ride.
- In the mix, further work on the soft half (soft trims) would only be passed on in the cap region (master S under about -35).

## Do not touch

- The ride and delivery settings: ratio 2.5, cap 10, 3 s smoothing, top ride 1.6, FAST_CAP_ABOVE 4.
- The bar-121 shape with `ARRIVAL_WEIGHT_AT` 484 (finding 1 only moves the letter-G hold's start and level, and keeps its 483.5-484 end).
- The c14 E6 fill and the 636 arrival weight and strokes (bar 160 is 1.8 dB over 159 on M).
- The morendo shape at 724-729.
- The bar-51 and bar-148 shapes, and the c12/c15 second-theme shapes.
- AUTO_REBOW rows, _REBOW_FROZEN and the re-bow fills (item 7 passes on the master everywhere music is held).
- The timpani re-strike plans; the tam-tam damp at 504.2.
- The suspended-cymbal key 64 / lead 0.25.
- PICKUP_LIFT values (finding 2 leaves Clarinet 1 504.5's lift as it is).
- The celli MEAS_TREM role [464,484,-6].
- The climax order 160 > 122 > 169.

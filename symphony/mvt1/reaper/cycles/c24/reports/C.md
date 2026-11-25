# Cycle 24, critic C: holistic comparison (render c23)

## Method

I compared the stem-fixed c23 render (`cycles/c23/render/`, `cycles/c23/rendered_build/parts.json`) with c00, with c18 (five cycles back), with the Dvořák 9/i recording (lossy MP3, decoded to 48 kHz) and with the stored measurements of Brahms 1/i and 4/i (musopen, lossless; `symphony/render/critics/c00/ref_brahms*_i_musopen/metrics.json`). The whole-file measures come from `symphony/render/tools/measure.py`, the tool that made the reference metrics, run on each master and on the delivered mp3. Note times use each cycle's own tempo map (`rendermap.wrap`). Levels are RMS dB. The scripts were throwaway and the scratch folder has been deleted. Each finding states its windows so the actor can repeat it.

## State of the render

**What has improved since c00 (measured).**
- Brightness now follows loudness: the centroid rises 0.287 octave per 10 LU, against 0.24 in c00. Brahms 1/i is 0.462, Brahms 4/i 0.297 and Dvořák 0.155.
- Loud-minus-soft shape at 2.5/5/10 kHz is +4.1/+9.3/+9.4 dB. Brahms 1/i is +6.3/+10.3/+10.2.
- The delivered mp3 measures 14.5 LU. Short-term loudness medians:
  - Lento -27.6 LU;
  - second theme -24.5;
  - first-theme ff -16.9;
  - letter G -14.6;
  - bar 160 -10.8;
  - Tempo I -29.4.
  Every soft passage is within 12 dB of the ff theme, and the climax stays on top.

**The large-scale shape has not moved since c00 (measured).**
- Section means, c00 / c18 / c23:

  | Section | c00 | c18 | c23 |
  |---|---|---|---|
  | Lento | -31.0 | -30.3 | -30.8 |
  | First theme | -20.7 | -20.3 | -20.6 |
  | Second theme | -30.7 | -30.3 | -30.2 |
  | Development | -21.2 | -20.4 | -20.4 |
  | Coda Allegro | -17.8 | -17.9 | -17.9 |

  Only the recapitulation's second theme moved: +2.8 dB, in c13.
- I fitted bar levels to the highest printed dynamic and to log2 of the number of staves playing:

  | | c00 | c18 | c23 |
  |---|---|---|---|
  | dB per dynamic step | 1.69 | 1.90 | 1.87 |
  | Residual SD (dB) | 4.00 | 3.93 | 3.89 |

- Twenty-three cycles of work have gone into notes, joins and accents. The weak points left are a few musical passages where a phrase does not do what the score asks, and two textures that repeat mechanically. They are ranked below.

**BRIEF item 7 passes (measured).** Master autocorrelation at 3.95 s, 100-300 Hz band / spectral centroid:

| Passage | Band | Centroid |
|---|---|---|
| Lento 5-12 | -0.08 | -0.02 |
| Second theme 47-55 | 0.08 | 0.00 |
| Bars 160-164 | -0.01 | -0.06 |
| Bars 175-178 | -0.09 | 0.08 |
| Tempo I 179-182 | -0.22 | -0.13 |

- No string note is longer than 6 s (they are all re-bowed).
- Horn 4's pp tied A-flat3 at 289 (15 s) wanders 5-9 dB on its own stem. It is masked on the master (inferred), so no change is proposed.

**BRIEF item 8 passes (measured).** 2-5 kHz from -10 to +80 ms against +120 to +400 ms, on the 619 printed accents:

| Family | c18 median | c23 median | c23 p90 |
|---|---|---|---|
| Strings | -3.0 | -1.4 | +1.9 |
| Winds | -6.5 | -2.7 | +1.6 |
| Brass | -6.7 | -4.5 | +0.7 |

- The c23 front swells moved the medians toward 0. They are still under it; watch them.
- The outliers are artefacts:
  - Horn 1/2 at 670 (+18/+13) is the release of 669.5, because the Horns a2 track plays 670;
  - Violas 536 is the known double stop.

## 1. Second theme, bars 49-50 and 149-150: the dolce tune sags in the middle of its first phrase, and the celli fall onto the top note of the printed crescendo (measured)

**Where.** Horn 1 and Violoncellos in unison, bars 49-50 (qn 192-198). Printed: < on 195-196 to the A-flat4, > from 196 to 198. The same bars in the recapitulation (qn 592-598, celli an octave below the horn, top note C4 at 596). This is the first statement of the movement's main lyric theme.

**Evidence.** Body level, +0.1 s to the end of the note or +1.0 s at most, on the Horn 1 and celli stems and their power sum. c18 matches within 0.5 dB, so this has stood for at least five cycles.
- **Exposition sum.**
  - Bars 47-48 median -33.3 dB (-31.3..-36.3).
  - From 193.5 to 198: -39.6, -35.9, -35.1, -37.7, -37.0, -37.1, a median of -37.0, which is 3.7 dB under bars 47-48. The C4 eighth at 193.5 is 7.8 dB under the D-flat4 before it.
- **Horn 1 alone.** -34.3..-38.3 in bars 47-48, falling to -40.1..-43.4 over 193.5-198.
- **The crescendo 195 -> 196.**
  - Horn +3.3 dB.
  - Celli -35.8 -> -39.9 (-4.1).
  - Sum -1.9.
  - Master -35.1 -> -35.0 (flat).
- **Recapitulation.**
  - Celli: A3 at 595.5 -30.0, C4 at 596 -38.4 (-8.4 dB onto the top note).
  - Sum -30.5 -> -33.5.
  - Master -29.8 -> -30.6.
- **Data.**
  - Horn 1's volume envelope falls from +5.5 dB at 191 to +1.0..+2.5 dB over 193.5-195 while CC11 stays at 67.
  - On the celli, CC11 rises 79 -> 84 into 196 and the volume is flat at +2.4..+2.7.
  - So the sag in the horn comes from the envelope, and the fall in the celli comes from the samples on those pitches (inferred).

**Inferred effect.** The line goes slack where it should open out. A listener follows this tune more closely than anything else in the movement.

**Fix.** `build/score_config.py`, `LEVEL_SHAPES`:
- Horn 1: `[(193.2, 0.0), (193.45, 3.0), (195.0, 3.0), (195.9, 4.5), (197.6, 4.5), (198.2, 0.0)]`.
- Violoncellos, exposition: `[(193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.9, 5.0), (197.6, 4.0), (198.2, 0.0)]`.
- Violoncellos, recapitulation: `[(595.65, 0.0), (595.92, 6.0), (597.0, 5.0), (597.9, 2.0), (598.1, 0.0)]`. Its fall stays inside the printed >.

These are level-only changes, so they can be simulated on the c23 stems first and applied by stem fix.

**Targets** (on the sum, same windows):
- 196 at least 1.5 dB over 195, and within 1.5 dB of 191/192;
- median over 193.5-198 within 2 dB of the bars 47-48 median;
- recapitulation: celli 596 within 2 dB of 595.5, and the sum at 596 no lower than 595.5 - 0.5;
- master 196 and 596 at least 1 dB over 195 and 595.

Keep the c20 bar 51-52 shapes.

## 2. Harp, bars 47-68 (and 156-166): the second-theme arpeggios jump 10-15 dB from note to note, and the top notes of the figures drop out (measured)

**Where.** Harp (`Harp Sus RR.oib`), the p arpeggio accompaniment under the second theme: qn 184-272, 110 notes. It is the third-loudest stem in bars 49-55, so it is exposed (metrics.md).

**Method.** For each note, I measured the onset increase of the note's own pitch (harmonics 1-2, ±3%): the energy in the 0.1 s after the onset minus the 0.1 s before it. The result was normalised to velocity 64, using the within-pitch slope measured on this render (0.37 dB per velocity step, 94 notes), and to the volume envelope.

**Evidence.**
- p10-p90 over bars 47-68 is 19.6 dB.
- Inside single bars, relative to the loudest note of the bar:
  - bar 48: D-flat4 -13, A-flat4 -4, D-flat5 -15, F5 0, A-flat5 -10;
  - bar 53: E-flat4 -2, B-flat4 0, D-flat5 -11, G5 -8, B-flat5 -14.
- Per-pitch medians against the overall median:

  | Weak pitches | dB | Strong pitches | dB |
  |---|---|---|---|
  | D-flat5 (11 notes) | -5.0 | F5 (7 notes) | +7.4 |
  | B-flat5 (5) | -8.5 | B-flat4 (8) | +5.6 |
  | F6 (7) | -6.8 | E-flat5 (5) | +4.5 |
  | E-flat6/E6 (2 each) | -7.3/-7.5 | F4 (4) | +9.7, despite its -8 velocity |

- With a simpler fixed-window measure the spread is the same in c18 and c23: 10.9 dB.

**Cause (measured in the code).**
- `HARP_PITCH_VEL` in `tools/score_to_parts.py` is movement II's c09 table, `{58: 12, 57: 7, 60: 5, 63: 5, 65: -8, 66: -4}`. `score_config.py` never refits it for this movement.
- Every other harp note plays at velocity 64.
- LEARNINGS section 9 records ±4-9 dB pitch unevenness in this patch at one velocity.

**Inferred effect.** The figures do not ripple evenly: notes drop out of each arpeggio, and the pattern repeats bar after bar under the dolce theme.

**Fix.** `build/score_config.py`, a movement-I `HARP_PITCH_VEL` that replaces the default.
- Values are relative to the base velocity. They are -deviation/0.37, halved for pitches with a single note, and capped at ±12 for this pass:

  ```python
  HARP_PITCH_VEL = {55: -6, 56: -12, 58: 5, 60: 5, 61: 9, 63: 0, 64: -8, 65: -12, 66: -12, 67: 6, 68: -9, 70: -12,
                    72: -7, 73: 12, 75: -12, 76: -10, 77: -12, 78: 12, 81: 12, 82: 12, 83: 10, 84: 10, 85: -12,
                    86: 12, 87: 12, 88: 12, 89: 12, 92: 5, 94: 12, 96: 4, 97: 12}
  ```

- This is a `--midi-only` rebuild of the Harp.
- Hold the harp stem's level over bars 47-68 within 1 dB of c23. Correct it with the harp's `gain_db` if it moves, and keep CC11 constant (LEARNINGS 9).
- After the render, refit with the same measure; round robins vary, so expect a second, smaller pass.

**Targets.**
- p10-p90 at most 12 dB over bars 47-68;
- every pitch with two or more notes within ±4 dB;
- the top note of each figure no more than 4 dB under the figure's median.

## 3. Coda, bars 167-169 (qn 664-676): the basses' f eighths limp; every off-beat swells in late, while the ff pedals that have STR_REP_DETACH are even (measured)

**Where.** Double basses, 24 C2 eighths at velocity 83 on Sus MAX, CC11 88. They are the only moving low part under the brass and wind whole notes.

**Evidence.** 40-400 Hz envelope in 5 ms frames. "Arrival" is the first frame within 6 dB of the note's own peak. The note's window is its 238 ms slot.

| Span | c18 on-beat (arrival / peak, ms) | c18 off-beat | c23 on-beat | c23 off-beat |
|---|---|---|---|---|
| 664-676 (coda) | -30 / -15 | +50 / +225 | -30 / -30 | **+85 / +210** |
| 520-536 | -30 / 45 | -25 / **115** | -20 / 45 | +15 / 60 |
| 556-568 | -30 / **155** | -25 / 40 | +5 / 73 | -20 / 42 |
| 104-128 | | | +20 / 115 | -22 / 100 |

- In the coda, the on-beat window's maximum is the previous off-beat's swell.
- Front (-10..+90 ms, 40-300 Hz), on-beats minus off-beats: stem +6.9 dB, master +3.1 dB. Bodies (100-200 ms) are the reverse: the off-beats are 6-7 dB over the on-beats.
- The pattern has a strict period of 2: front n against n-2 is within 0.92 dB median, and spectral distance at lag 2 is 0.9 dB against 5.2 dB at lag 1.
- The same two-sample alternation limped in 520-536 and 556-568 in c18. Since c22 it is even there, because `STR_REP_DETACH` (a -5 dB dip over the last 0.08 s before each next onset) cuts the late swell.
- The c20 coda step shape (`_cb20`: -0.8 on-beat, +1.2 off-beat) lifts the off-beats, which are the late notes.

**Inferred effect.** A long-short lurch in the bass at the coda's ff return of the theme.

**Fix.** `build/score_config.py`:
- Add `(664.0, 676.0)` to `STR_REP_DETACH["at"]["Double basses"]`. Its `min_cc` 84 is met: the coda's CC11 is 88.
- In `_cb20`, set the on/off alternation to 0/0, keeping the period-6 irregularity row.
- Add the +1.5 hold the other spans use, `[(663.85, 0.0), (663.95, 1.5), (676.0, 1.5), (676.1, 0.0)]`, adjusted after the render.

**Targets.**
- Off-beat arrival at most +30 ms and peak at most +120 ms, as in 520-536;
- stem front on-off within ±2 dB, master 40-300 Hz under 1.5 dB;
- front n against n-2 median at least 0.5 dB;
- bar 167-169 RMS within 0.5 dB of c23.

## 4. Four passages run at a fixed tempo: the exposition's second theme (bars 47-50), the sostenuto (123-126), the largamente (160-164) and the coda Allegro into the fermata (167-170) (tempo map measured; effect inferred)

**Measured.** `parts.json` tempo map:
- qn 184-200 holds 112.0 for 17 beats. The same bars in the recapitulation (584-600) have an arc: 113.7 at 585, easing to 107.5 / 103.0 at 596-599. The exposition has none, because `PHRASE_ARCS` lists (584, 600) but not (184, 200).
- qn 488-504: 16 beats at 100.0 (9.6 s).
- qn 636-656: 20 beats at 100.0 (12.0 s).
- qn 664-679: 15 beats at 126.0, then the fermata (7.1 s).
- Elsewhere the Allegro sections vary 1.4-2.5% (beat-tempo SD).
- So the first statement of the lyric theme, the two broad climaxes and the approach to the bar-170 fermata are the only stretches with no shaping. All four are places where a conductor would shape the tempo most.

**Fix.** `build/score_config.py`:
- `PHRASE_ARCS = PHRASE_ARCS + [(184, 200), (488, 504, "sub"), (636, 648, "sub"), (664, 679, "sub")]`.
  - The first copies the recapitulation's depth.
  - The next two are c23 C #6, deferred.
  - The last gives the run into the fermata a small give on its last beats.
- Also take c23 C #6's ramp-end fix: `RAMP_SPANS` (244, 260, 115) -> (244, 252, 115) and (620, 632, 115) -> (620, 628, 115).

Re-bows are frozen in qn (`_REBOW_FROZEN`). CAESURA 636, the suspended-cymbal lead and BEAT_STRETCH 679 stay.

**Checks.**
- Bars 49-50 ease 3-5% into 196-198, as at 596-599;
- bars 123-126, 160-162 and 169-170 slow 2-5% only on their last two beats;
- bar 65 -> 66 drops by no more than 1.5%;
- re-measure the 636 arrival, the limiter and the climax order 160 > 122 > 167-170.

Do this in the same cycle as finding 1, so the bar 49-50 shapes are fitted on the new map.

## 5. The tutti lacks low-mid body (125-160 Hz) against all three references (measured; the fix is a simulated test that closes about a quarter of the gap)

**Evidence.**
- **Long-term third-octaves re 1 kHz, 125 / 158 Hz:**

  | | 125 Hz | 158 Hz |
  |---|---|---|
  | c00 | -6.5 | -6.0 |
  | c23 | -5.3 | -4.0 |
  | Brahms 1/i | +1.6 | -1.0 |
  | Brahms 4/i | +2.1 | +0.4 |
  | Dvořák | -2.1 | +0.2 |

- **Loud-minus-soft shape at 157 Hz:** c00 -6.3, c18 -2.9, c23 -3.0, against +2.8 / +4.2 / +5.2 in the references. Every reference gains low-mid body when loud, and the mockup loses it.
- **Loud frames** (top 10% of 0.4 s frames), relative to 250-2000 Hz:

  | | 100-160 Hz | 160-250 Hz | 60-100 Hz |
  |---|---|---|---|
  | c23 | -11.7 | -10.1 | -15.1 |
  | Dvořák | -8.8 | -6.1 | -23.2 |

  So the mockup is heavier than Dvořák under 100 Hz and thinner at 100-250 Hz.
- **Who supplies 160-250 Hz in loud frames:** celli 37%, basses 24%, timpani 19%, tuba 6%, violas 3.8%, trombones and bass trombone 4.8% together, bassoons 0.8%. The bass trombone's own 160-250 Hz is 18.9 dB under its 500-2000 Hz.
- Some of the gap is the pitches each piece plays (line spectra), so do not chase the whole difference (inferred).

**Fix (test).** `build/mix.json`, static `eq` bells, bw 1.0 octave:

| Track | Band | Setting |
|---|---|---|
| Violas | bell | 170 Hz +3 |
| Bassoon 1, Bassoon 2 | bell | 150 Hz +3 |
| Trombone 1, Trombone 2 | bell | 160 Hz +3 |
| Bass trombone | bell | 140 Hz +3 |
| Bass clarinet | bell | 150 Hz +2 |
| Horn 3, Horn 4, Horns a2 | bell | 150-170 Hz +2 |
| Violoncellos | bell2 | 125 Hz +3 -> 135 Hz +5 (no free slot; simulate it first) |

**Simulated** on the c23 stems (power sum, celli as 140 Hz +2.5):

| | 125 Hz | 158 Hz | 198 Hz |
|---|---|---|---|
| Long-term | +1.1 | +0.8 | |
| Loud frames | +1.0 | +0.3 | +0.8 |

- Master loud-frame level +0.10 dB, soft +0.34 dB; celli stem +0.8 dB, the others +0.03..+0.4.

**Targets.**
- 125 / 158 Hz long-term at least 1 dB higher, and loud-minus-soft at 157 Hz at least -1.5;
- 60-100 Hz unchanged;
- climax order and limiter re-measured.

Only these tracks' FX change, but each one breaks the stem-sum simulation for its other passages (LEARNINGS 15). Measure each track's level afterwards and correct its gain. Give it its own cycle if this one carries finding 4.

## Smaller items (measured; no change proposed this cycle)

- **Tutti cut-off.** At the bar-170 fermata (qn 679) the master falls 20 dB in 0.55 s (c18 0.53). The references' median is 0.485 s (Brahms 1/i) and 0.49 s (Dvořák). The c20 C #5 hall `fx_volume` 0.19 -> 0.16 test is still open. It is small next to the items above, and it needs every fit redone.
- **Tutti attack spread.** At the ten largest tutti entries, the stems' arrivals spread with a median SD of 51 ms and p10-p90 of 100 ms. That is not mechanically tight. Flute 2 at 104/128 (+235/+245 ms) is the only late outlier that is not by design.
- **Stereo above 4 kHz.** Correlation is 0.544 (c00 0.491); the references are 0.384-0.525. No action.

## Do not touch

- Item 7: the re-bow and loop work;
- the c23 accent swells and their fits;
- STR_REP_DETACH on its three spans;
- the delivery settings and the climax order 160 > 122 > 167-170;
- the recapitulation's (584, 600) arc;
- the c20 bar 51-52 Horn 1/celli shapes;
- the brass 4 kHz and Tpt1 climax shelves;
- the basses' 80 Hz loud shelf and 87 Hz bell;
- every c23 do-not-touch item in HISTORY.md.

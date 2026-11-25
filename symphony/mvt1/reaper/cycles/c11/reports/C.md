# Cycle 11, critic C: tempo, timing and transitions (render c10)

## Method

I measured the stem-fixed c10 render (`cycles/c10/render/`) against `build/parts.json`, which is the data c10 was rendered from. Score qn was converted to file time on the parts.json tempo map, which the render follows since the c03 pre-roll fix. Unless stated otherwise, levels are stereo power in 20 ms windows at a 5 ms hop.

I used these measures:
- **Beat lengths:** every beat's length on the tempo map. I listed beat-to-beat changes over 7.5% and runs of 12 or more beats at an unchanged tempo.
- **Pitch crossover:** for 1642 contiguous pitch changes on monophonic stretches, the first frame where harmonics 1-4 of the new pitch exceed those of the old pitch for 20 ms. Harmonics the two pitches share were excluded. FFT 2048, hop 5 ms. Times are from the score onset.
- **Entries after 0.4 s or more of silence:** first sound (peak - 20 dB) and arrival (peak - 6 dB) within the first 0.6 s.
- **Re-attack arrival:** for repeated and off-beat notes, the time from the local minimum to peak - 6 dB.
- **Ensemble sync:** at every onset shared by 4 or more tracks in the Allegro, each track's time minus the median at that onset.
- **Keyswitch lead:** the time from each keyswitch to the first note that uses it.
- **Brief items 7-8:** autocorrelation at 3.95 s of the master's 100-300 Hz band level and spectral centroid, detrended over 2 s, against control lags of 3.0 and 5.0 s. Accents: 2-5 kHz energy in the first 80 ms minus the body.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c11-C/` (`common.py`, `xover.py`, `xover2.py`, `entries.py`, `motor.py`, `sync.py`, `timp.py`, `ks.py`, `loopacc.py`, `shape.py`, `notes_at.py`).

## Checks that pass (measured)

- **Printed tempo steps.** Every rit., allargando and animando ramp starts and ends at its printed values:
  - bar 46 ends at 113, into the 112 of bar 47;
  - bar 68 ends at 86.5, into the 126 of bar 69;
  - bar 122 ends at 102, into the 100 of bar 123;
  - bar 166 ends at 79.5, into the 126 of bar 167;
  - bar 178 ends at 51.5, into the 50 of bar 179;
  - the animando of bars 156-159 reaches 120.9 against the printed 120.
- **Bar-170 fermata.** The ff chord is gone by 380.5 s (qn 679 is at 380.14 s). The master is at -60..-69 dB before the cello enters at 382.64 s.
- **Ending.** Bar 182 (30 bpm) lasts 8.0 s. The master is under -76 dB 0.8 s after qn 728, and the mp3 ends 1.66 s after qn 728, so the attacca stays an attacca.
- **Keyswitches.** All 878 used keyswitches come at least 9.5 ms before their note.
- **The off-beat motor of bars 15-22.**

  | | Vln II | Violas | basses | Vln I | celli |
  |---|---|---|---|---|---|
  | median arrival (s) | +0.052 | +0.045 | +0.036 | -0.014 | -0.002 |
  | p90 (s) | +0.12 | +0.125 | +0.09 | +0.08 | +0.06 |

  Vln II, Violas and basses play the off-beats; Vln I and celli play the downbeats.
- **Short trumpet figures in bars 27-30.** Arrivals -0.01..+0.05 s.
- **Brief item 7.** Autocorrelation at 3.95 s (band / centroid), with the 3.0 / 5.0 s control lags in brackets:

  | passage | band | centroid |
  |---|---|---|
  | Lento bars 5-12 | -0.06 (control -0.07 / -0.13) | -0.03 |
  | coda bars 175-178 | -0.21 | -0.03 |
  | bars 179-182 | -0.01 | -0.05 |
  | sostenuto bars 123-126 | -0.24 | -0.49 |

  No loop period is visible.
- **Brief item 8.** Accents at 0.6 qn or longer, 2-5 kHz first 80 ms minus body:

  | | n | median (dB) | p90 (dB) | over +3 dB |
  |---|---|---|---|---|
  | brass | 124 | -15.1 | -6.4 | 0 |
  | winds | 202 | -12.8 | -6.2 | 1 |
  | strings | 172 | -10.3 | -5.4 | 1 |

## 1. Phrase-arc endings fall on rhythmic figures and in front of the animandos: uneven hammer strokes in bar 72, a dragged run into bar 33, a 12% jump at both sub. p animandos (measured on the tempo map; effect on the listener inferred)

**Where.**
- **Bar 72, qn 284-286.** Three accented down-bow tutti chords on beats 1-3 (all strings, horns, trumpets, low brass, timpani).
- **Bar 32, beat 4, qn 127.** The violins' sixteenth run, with crescendo, into the ff chord of bar 33.
- **Bar 61 beats 3-4 into bar 62 (qn 242-244), and bar 155 beats 3-4 into bar 156 (qn 618-620).** The beats before the sub. p "poco animando".

**What is wrong.**
- **Bar 72.** `PHRASE_ARCS (272, 286, "main")` ends in the middle of the bar. Its x0.95/x0.88 slowing falls on the first two hammer strokes: beats of 0.501, 0.541 and 0.476 s (119.7 / 110.9 / 126.0 bpm). Three equal strokes come at three different spacings, the third 13.6% faster than the second.
- **Bar 32.** `(120, 128, "main")` puts the sixteenth run at 110.9 bpm, and the ff downbeat follows at 126 (+13.6%). The c07 report flagged the same thing (finding 4, inferred note), and it was not changed.
- **Bars 61 and 155.** The default-depth arcs `(232, 244)` and `(600, 620)` slow the last two beats to 107.5 / 103.0. The animando ramps start at 115, so the beat at the sub. p jumps +11.6%: the music brakes and then lurches forward exactly where the score asks for a gradual push.
- **Other jumps.** Listing every unprinted beat-to-beat change over 7.5% also finds the "main" arc returns at qn 220 (+10.2%), 332, 408 and 440 (+10.2% each), and 696 (bar 175, +13.6%). These come at section breaks, where a snap back is plausible, so I list them only as checks.

**Fix** in `build/score_config.py`, after the c08 block:
- Bar 72: replace `(272, 286, "main")` with `(272, 284, "sub")`, and add `BEAT_STRETCH[284.0] = 0.95` and `BEAT_STRETCH[285.0] = 0.95`. The strokes then come 0.501 / 0.501 s apart and the third lands at 126. Beat 286 stays at 126, so the celli's held A-flat from 286 and its `REBOW_AT` points 289.145 / 293.758 / 298.37 keep their place relative to the note start.
- Bar 32: `(120, 128, "main")` becomes `(120, 128, "sub")`, giving beat 127 at 119.7.
- Bars 61 and 155: add a depth "open" in `tools/score_to_parts.py` `phrase_arcs()`: `slow = (1.0, 1.0)` when `depth == "open"`, with the default push. Mark `(232, 244, "open")` and `(600, 620, "open")`. The animando then starts from about 112 to 115 (+2.7%).

**Checks.**
- No unprinted beat-to-beat change over 8% in qn 120-128, 240-248, 280-290 and 616-624.
- The parts.json `rebows` rows for celli/basses in qn 280-300 are unchanged.
- Total length changes by under 0.3 s.

## 2. The Lento (56 beats), Tempo I (12 beats) and the transition of bars 33-44 (48 beats) run at an exactly constant tempo (measured; musical effect inferred)

**Where.**
- Bars 1-14 (qn 0-56): the low unison phrase, the cor anglais espr. solo of bars 5-9, the crescendo to the f of bar 12 with the bassoons' breath mark in bar 10, and the horn/oboe close of bars 13-14.
- Bars 179-181 (qn 712-724).
- Bars 33-44 (qn 128-176): the bassoon solo espr. of bars 33-36 and the violas' mp theme of bars 34-36.

**What is wrong.**
- The three passages hold one tempo for 56 beats (1.200 s each, 67.2 s), 12 beats and 48 beats (126.0).
- These are the three longest constant runs on the map. The fourth is the printed largamente (20 beats at 100).
- Every other a-tempo stretch has had arcs since c04/c08.
- The Lento arcs were proposed in c07 (C #5) and deferred because they move the automatic re-bow points. These re-bows now carry the c10 hand shapes: Cb 38.003, Vc 37.377 and the refit 51.87.

**Fix**, in this order, in `build/score_config.py`:
1. **Freeze the re-bows.** Add every current parts.json `rebows` point (first element of each row) to `REBOW_AT`:
   - qn < 56: Violins I 2, Violins II 6, Violas 8, Violoncellos 13, Double basses 13;
   - qn ≥ 712: 3 / 6 / 6 / 8 / 6;
   - the transition: Violoncellos 152.46, 163.88, 169.15 and Double basses 166.01.

   Merge these with the existing Violoncellos and Violas lists. `rebow_fills.json` and `NOTCH_SKIP` are keyed by these qn. `loop_fills.json` is keyed in seconds after the note start; none of its four notes contains a re-bow, so it is unaffected.
2. **Add the arcs.**

   ```
   PHRASE_ARCS += [(0, 16, "sub"), (16, 36), (36, 48), (48, 56, "main"), (128, 144), (144, 160, "sub"), (712, 724, "sub")]
   TEMPO_PUSH += [(36, 46, 1.015)]
   ```

   `(48, 56, "main")` slows into the Allegro's new tempo, which is not a ramp, so the c07 reversal does not arise. Do not end an arc at 176, where the poco rit. ramp starts.

**Expected.** About +2.5 s.

**Checks.**
- Every parts.json `rebows` row has the same qn after the build.
- After the render: re-bow dips within 1 dB of c10 (refit with `fit_rebows.py` if a dip grows by more than 1.5 dB), Lento loop autocorrelation still ≤ 0.1, and the bar-15 entry unchanged.

## 3. The hemiola of bars 23-25 and 135-137: the Violins II and violas reach the accented pitch changes 0.17 s late (measured)

**Where.** Violins II and Violas at qn 91, 94, 97, 539, 542 and 545, plus Violas 575. These are accented Sus MAX quarters every third beat, against the 4/4. The score's accents fall on the pitch changes.

**What is wrong.**
- The crossovers are +0.155 / +0.205 / +0.13 / +0.205 / +0.185 / +0.125 s (Violins II) and +0.115 / +0.16 / +0.165 / +0.17 / +0.16 / +0.19 / +0.19 s (Violas): medians +0.170 and +0.165.
- Flute 1, Clarinet 1 and Horn 1 play the same accents and cross at +0.03..+0.07 s.
- The notes have no lead (moved onset = score onset), and the old note ends 0.019 s before. This is the abutting Sus MAX case that `ABUT_LEAD` fixes on the basses (c07: +0.155 -> +0.070 s).
- The cross-rhythm is carried by these accents, so a 0.17 s delay at 128 bpm (a third of a beat) blurs the hemiola in both the exposition and the recapitulation (inferred).
- Violins I's four abutting Sus changes (59.5, 107.5, 139.5, 571.5) cross at +0.06 and need nothing.

**Fix** in `build/score_config.py`:

```
ABUT_LEAD["Violins II"] = {"lead_s": 0.10, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False,
                           "at": [91.0, 94.0, 97.0, 539.0, 542.0, 545.0]}
ABUT_LEAD["Violas"] = dict(ABUT_LEAD["Violins II"], at=[91.0, 94.0, 97.0, 539.0, 542.0, 545.0, 575.0])
```

`skip_next_same` must be False. Each of these notes is followed by a same-pitch quarter (92, 95, 98, ...), so True would skip all of them.

**Checks.**
- After the render, crossovers under +0.08 s.
- No new dip over 4 dB at the following same-pitch strokes (92, 95, 98, 540, 543, 546), measured with `motor.py` against c10. That is the c15 bassoon failure mode.
- Refit the string accents there (`fit_accents.py --family string`), because the onset moves under the swell.

## 4. Wind and brass Sus chord changes cross 0.04-0.06 s after the strings, and flute/oboe Sus entries have no entry lead (measured)

**Where.** Abutting Sus pitch changes in the Allegro (126/112 bpm), mostly tutti harmony changes. Also flute and oboe Sus MAX entries on f/ff downbeats: qn 100, 104, 324, 484, 520, 548, 664.

**What is wrong.** Pitch-change crossover medians, all without a lead:

| track | n | median crossover (s) |
|---|---|---|
| Horn 1 | 38 | +0.098 |
| Trombone 1 | 26 | +0.092 |
| Trombone 2 | 15 | +0.080 |
| Trumpet 1 | 24 | +0.073 |
| Trumpet 2 | 14 | +0.075 |
| Trumpet 3 | 14 | +0.075 |
| Oboe 1 | 33 | +0.085 |
| Oboe 2 | 30 | +0.092 |
| Flute 2 | 28 | +0.105 |

For comparison:
- Horn 3 with the c07 `ABUT_LEAD` 0.06: +0.015 (n=35).
- Strings with legato leads: Vln I Leg Slur +0.025, Vln II +0.015, Vla +0.035, Vc Leg BC +0.060.
- Against each onset's median: Flute 2 +0.030 (p90 +0.115), Oboe 2 +0.025 (p90 +0.121), Horn 1 +0.018 (p90 +0.096). Every other track is within -0.020..+0.013 apart from the contrabassoon, which is early (-0.046).

The flute and oboe Sus MAX entries:
- They start at the score onset, because `ENTRY_LEAD_S` covers only the bassoons among the winds and `ENTRY_LEAD_ART_S["wind"]` has no "Sus MAX".
- First sound: Fl2 520 +0.026 / 664 +0.049, Ob2 520 +0.026 / 664 +0.019, Ob1 664 +0.024 s. The brass in the same chords sound at -0.02..-0.06.
- They reach peak - 6 dB at +0.15..+0.24 (Oboe 2 median +0.166 over 14 entries).

Inferred: the top and middle of the tutti chords arrive after the strings and bass. This softens chord changes that the score marks ff.

**Fix** in `build/score_config.py`:

```
for t_ in ("Horn 1", "Horn 2", "Trombone 1", "Trombone 2", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Oboe 1", "Oboe 2", "Flute 2"):
    ABUT_LEAD[t_] = {"lead_s": 0.05, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}
ENTRY_LEAD_ART_S["Flute"] = {"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus MAX": 0.04}
ENTRY_LEAD_ART_S["Oboe"] = dict(ENTRY_LEAD_ART_S["Flute"])
```

`by_name` takes the capitalised track key before the family key, so the bassoons, clarinets and cor anglais keep the "wind" values.

**Checks.**
- Crossover medians +0.03..+0.06 on the listed tracks.
- Flute/oboe first sound within ±0.02 s of the brass at the listed downbeats.
- No new same-pitch holes (skip_next_same).
- Refit the brass and wind accents (`fit_accents.py --family brass`, `--family wind`, `--keep-long-qn 1.4`), because their onsets move under the fitted swells.

## 5. Timpani strokes now come 0.05 s after the strings at shared onsets (measured; the size of the change is inferred)

**Where.** 63 timpani strokes in the Allegro that share an onset with other tracks.

**What is wrong.** Timpani arrival minus the other tracks' re-attack arrival:
- strings +0.053 s (176 pairs);
- winds +0.012 (236);
- brass +0.000 (285);
- the whole ensemble +0.022 (p25 -0.010, p75 +0.054).

`TIMP_DELAY_S` 0.06 dates from c03, when the strings reached -6 dB at +0.08-0.10 s. Since the c07 mid-layer entry leads they arrive earlier. If finding 4 moves the brass chord changes 0.04 s earlier, the timpani will also trail the brass.

**Fix** in `build/score_config.py`: `TIMP_DELAY_S = 0.045`. Only if finding 4 is applied, and together with it.

**Check.** Timpani minus brass -0.01..+0.01 s and minus strings under +0.04 s on the next render.

## Do not touch

- The `RAMP_SPANS` realisation of the printed rit., allargando and animando steps, and the rit. clamp in `smooth_tempo`.
- `CAESURA {636: 0.15}` with the suspended-cymbal lead.
- `BEAT_STRETCH {679: 0.6}` (2.5 s fermata, silent before the cello).
- The final bar at 30 bpm and the 1.0 s mp3 tail (attacca).
- Keyswitch placement.
- The c07 mid entry lead 0.12 and `SHORT_SUS_LEAD_KEEP_OVERLAP` (the bars 15-22 motor is on time).
- `ABUT_LEAD` on the basses and Horns 3/4.
- The string Leg Slur / Leg BC leads.
- The c08 development and coda arcs, apart from the ends in finding 1.
- The re-bow rows and their fitted shapes. Freeze them in qn before any tempo change near them.

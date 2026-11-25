# Cycle 10, critic C: dynamics over time (render c09)

Lens: the shape of hairpins and phrases, the loudness arc of the movement against the score (the fff at 122-123 with the tam-tam, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda), the loudness range of the master and the delivered mp3 (BRIEF item 6), loop pulsing on long notes (item 7), and decays.

Method. I measured the stem-fixed c09 render (`cycles/c09/render/`, where the master is the float stem sum) and `mvt1-mockup-c09.mp3`. Score qn maps to file time through the `build/parts.json` tempo map, which is the same as c08's. Loudness is ffmpeg ebur128 at 10 Hz. M is the 400 ms window, shifted 0.2 s to centre it. S is the 3 s window, shifted 1.5 s. Stem levels are plain stereo power in 10 ms frames.

I ran two kinds of simulation:
- **Delivery changes:** a copy of `tools/deliver_master.py` with extra options, run on the c09 master. With no options it reproduces c09 exactly: LRA 14.7 LU, span 18.2 dB, limiter 2.0 dB.
- **Level changes:** dB shapes applied to the c09 stems, then summed.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c10-C/`:
- `bars.py`: bar levels against the printed dynamic;
- `hp.py`, `hptrack.py`, `hpcmp.py`: hairpins on the master, per track, and c08 against c09;
- `win.py`, `notes.py`: level windows and per-note levels;
- `loops.py`, `loops2.py`, `expo.py`, `msweep.py`: item 7;
- `stale.py`: notes carrying trims;
- `dm.py`, `dm2.py`, `dm3.py`, `runv.sh`, `runv3.sh`, `evalm.py`: delivery variants;
- `sim.py`, `simshape.py`, `cmpbars.py`.

## State of the arc (measured)

- **Master:** -16.3 LUFS, LRA 21.1 LU. Bar level against the bar's loudest printed dynamic has a correlation of 0.84.
- **Delivered file:** LRA 14.7 LU, p10-to-max span 18.2 dB, limiter 2.0 dB, 1 inversion among 256 five-second moves of 3 dB or more, median share of each move kept 0.80.
- **Climax order holds on S:**

  | | bar 160 | bar 122 | bar 169 |
  |---|---|---|---|
  | master S max | -6.8 | -7.7 | |
  | delivered S max | -10.6 | -11.1 | -11.9 |

- **Diminuendo after the tam-tam is well shaped:** master bars 122-127 measure -7.6 / -8.9 / -14.6 / -24.0 / -29.3 / -33.7 dB (M). The p arrives at bar 126.
- **Recapitulation:** the ff at 131-134 (-15.1..-15.9) matches the exposition's ff theme (bars 27-31, -13.9..-15.8).
- **The ppp ending:** delivered bar 182 measures -32.1 dB, the same as bar 1.
- **Item 7 on the master (measured, `msweep.py`):** 10 s windows across the whole movement, autocorrelation at 3.85-4.05 s, 100-300 Hz band and spectral centroid.
  - The Lento (bars 1-14), the bar 122-126 sostenuto and the coda (bars 171-182) all stay under 0.35.
  - The windows flagged in the Allegro sit on 2-bar rhythmic patterns (8 qn = 3.8 s at q=126), not on held notes.

## 1. The delivered file makes the ff of bars 82-83 and 167-170 as loud as the fff climax at bar 160 (measured, simulated)

**Where:** delivered mp3, bars 82-83, 167-170, 158-161 and 121-123.

**Evidence: maximum momentary loudness (M max) per bar.**

| | bar 160 | bar 170 | bar 82 | bar 122 |
|---|---|---|---|---|
| master | -5.6 | -8.9 | -9.8 | -6.6 |
| delivered | -9.6 | -9.8 | -10.4 | -9.9 |

- On the master, bar 160 is 3.3 dB over bar 170 and 4.2 dB over bar 82. In the delivered file the margins are 0.2 and 0.8 dB.
- On S max, the delivered margins over bars 170 and 82 are 1.4 and 1.8 dB.

**Cause.** I took the gain apart bar by bar (`dm.py` writes the ride's gain curve and the pre-limiter file).
- The ride's lift is computed from S smoothed with a 3 s Gaussian, and the gain is smoothed again. Short ff passages next to soft ones therefore inherit their neighbours' lift: bar 170 +2.5 dB, bars 82/83 +1.7/+2.1, bar 167 +1.4.
- The long climax takes the top ride: bar 160 -1.5 dB, bar 159 -1.2, bars 121/122 -1.1.
- The limiter's share is small and even: 0.2-0.6 dB everywhere.

The ride therefore moves 4 dB of differential gain against the climax. It was built to lift soft passages, and it also lifts the ff bars inside its window.

**Fix** (`tools/deliver_master.py`, after `gdb` is computed): cap the slow lift by a lift computed from the frame's own loudness, so that the lift cannot reach frames that are themselves loud:

```
Sf = smooth(S, 1.0)
fastcap = np.clip((knee + 4.0 - Sf) * (1 - 1 / RATIO), 0, CAP_DB)
lift = smooth(np.clip((knee - Ss) * (1 - 1 / RATIO), 0, CAP_DB), SMOOTH_S)
top  = smooth(np.clip((Ss - (loud + TOP_ABOVE)) * (1 - 1 / TOP_RATIO), 0, None), SMOOTH_S)
gdb  = smooth(np.minimum(lift, fastcap), 0.5) - top
```

On c09, knee = -18.2 LUFS.

**Simulated on the c09 master (`dm3.py`, FM=4):**
- **Margins:** bar 160 over bar 170 goes from 0.2 to 1.5 dB on M and from 1.4 to 2.4 dB on S. Over bar 82 it goes from 0.8 to 2.3 dB on M and from 1.8 to 3.2 dB on S. Bar 122 stays -0.3 dB under bar 160.
- **Delivery figures:** LRA 14.7 -> 14.2 LU, span 18.2 -> 18.1 dB, limiter 2.0 -> 1.4 dB, median share kept 0.80 -> 0.79, inversions 1 -> 1.
- **Soft bars:** within 0.1-0.2 dB of c09.
- **Ride speed:** the ride's fastest change is 2.1 dB/s (c09 0.9), so it does not pump.

I rejected two other variants:
- A max filter on S, which reduces the lift near loud passages: the span goes to 19.0-19.8 dB and the soft bars lose 1-1.4 dB.
- A faster smoothing (SMOOTH_S 1-2 s): LRA 12.3-13.5 LU and share kept 0.59-0.72.

**Criterion:** delivered M max at bar 160 at least 1.5 dB over bars 170 and 82; LRA 14-16 LU; span at most 19 dB; inversions no more than now.

## 2. Bars 60-61: the crescendo into the sub. p still does not grow, seven cycles after it was first listed (measured, simulated)

**Where:** qn 236-244 (bars 60-61).
- The hairpin `<` is on Vln I/II, Vla, Cl1, Bn2, Hn2-4 and Cb, from mf.
- "sub. p" on every part at 244.
- The c06 shapes `_hp236` (+4 dB ramp) and `_subp` are in `build/score_config.py`.

**Evidence.**
- **Master M per beat:** bar 60 -23.9 -23.9 -23.8 -24.8, bar 61 -22.5 -23.5 -24.3 -24.7. The last two beats of the crescendo are under its first beat. Hairpin last third minus first third: -0.6 dB on the master, -0.1 delivered.
- **Violins I carry the tune**, a falling line from B-flat5 to E-flat5. Per note they fall 6 dB:

  | qn | 236 | 239.5 | 240 | 242 | 243 | 243.5 |
  |---|---|---|---|---|---|---|
  | dB | -30.8 | -32.4 | -32.8 | -34.3 | -33.1 | -36.8 |

  This happens although CC11 rises 74 -> 85 and the envelope +2.0 -> +5.7 dB. The descending pitches play quieter in the samples than the hairpin adds. Per track: Vln I -3.4, Horn 3 -1.8, Vln II +0.2 dB.
- **What works:** the sub. p itself falls 7.9 dB.

**Fix** (`build/score_config.py`): add second shapes on top of `_hp236`, starting from the second note (238), gone before the subito:
- Violins I `[(238.0, 0.0), (243.9, 7.0), (243.94, 0.0)]`;
- Violins II the same with 5.0;
- Horn 3 and Violas the same with 3.0.

**Simulated (`simshape.py s3`):**
- Bar 61 beats go to -21.3 -21.2 -21.4 -20.6, against bar 60's -23.9 -23.9.
- The hairpin goes from -0.6 to +2.9 dB, and the fall into the sub. p from 7.9 to 10.9 dB.
- Violins I's last note then sits about level with its first, under a growing texture: the line holds its level while the music around it grows.

**Criterion:** master beat 4 of bar 61 at least 2.5 dB over beat 1 of bar 60; at least 8 dB from 243-244 to 244-246.

## 3. Second theme, bars 47-50 and 147-150: the crescendos collapse on their arrival notes, and an unmarked note is the loudest of the phrase (measured, simulated)

**Where:** Horn 1 (dolce solo) with the Violoncellos (dolce, in unison), qn 184-200 and 584-600.

**Evidence: master M per beat.**

| | crest of the `<` 189-191 | its arrival note | unmarked note | printed crest |
|---|---|---|---|---|
| exposition | 190: -27.9 | 191: -30.2 | 192.5: -26.3 | 196: -28.6 |
| recapitulation | 590: -25.1 | 591: -28.5 | 592.5: -26.4 | 596: -26.8 |

- Each `<` peaks halfway through and drops 2.3 / 3.4 dB on the note it leads to.
- The loudest moment of the exposition phrase is the unmarked bar-49 downbeat (192.5).
- **The arrival collapses for two reasons:**
  - Horn 1's 189/589 notes sag as legato targets and then swell inside the note. Quarters of the note are -41.2 -40.8 -34.0 -31.8 (exposition) and -39.5 -35.5 -30.9 -33.1 (recap); the arrival notes 191/591 then measure -37.7 / -39.7.
  - The celli's c08 hand shapes in `LEVEL_SHAPES["Violoncellos"]` release just before the arrival: `[(589.0,0),(590.95,2.5),(591.3,0)]`. The celli's 589 note measures -35.3 -30.9 -28.9 -33.1, and 591 measures -33.8. LEARNINGS section 4 records the same error at f.
- **The first `<` (184-187.5 / 584-587.5) plays flat on the held horn note.** Quarters are -37.6 -37.1 -39.1 -36.8 and -34.2 -33.8 -36.2 -34.8, although CC11 goes 61 -> 81 and CC1 55 -> 77 (the mp to f layers).
  - Cause: the c09 per-dynamic trims in `mix.json` (Horn 1 soft_trim mp +7.2, mf +2.0, f -0.8) are read along the printed dynamic curve by `build_reaper.vol_points`.
  - Across this hairpin (curve 58 -> 80) they take -6.6 dB off the note while the layers add it.
  - The same trim slope sits inside every brass and clarinet hairpin. Measured over all hairpins, horn crescendos are a median 0.4 dB smaller than in c08 (decrescendos 1.0 dB smaller). The two control tracks without a CC1 change (Violins I, Violoncellos; 65 crescendos) are unchanged at +0.0.

**Fix:**
- (a) `LEVEL_SHAPES["Violoncellos"]` in `build/score_config.py`: hold the 189/589 ramps through the arrival note, `[(589.0,0),(590.95,2.5),(592.2,2.5),(592.7,0)]`, and the same at 189 (add the missing exposition shape `[(189.0,0),(190.95,2.5),(192.0,2.5),(192.5,0)]`). Hold the 201 shape to 204.2 as well.
- (b) Horn 1 `LEVEL_SHAPES`: -2.5 dB over 190.0-190.95 and 590.0-590.95 (the bloom); +3 dB on 191-192 and 591-592 (`note_trims.json` 191.0/591.0 +3); the 192/592 note trims +4/+5 down to +2/+3, so that the unmarked downbeat stops being the crest.
- (c) Generic, `tools/build_reaper.py vol_points`: for `CC1_DYN_TRACKS`, read the dynamic trim at each note's score onset and hold it through the note, instead of along the hairpin. Static per-dynamic levels stay as fitted; the crescendo inside a held note stays as the layers make it.
  - (c) changes level inside every brass and clarinet hairpin. Refit `accent_fits.json` for brass afterwards, as HISTORY requires.

**Simulated (a)+(b) (`simshape.py s4`):**
- The drop from crest to arrival goes from -4.3 to -0.7..-1.3 dB (exposition) and from -5.0 to -1.0..-2.7 dB (recap, M windows of 0.5 qn).
- I did not simulate (c): the trim change is a step at note onsets, and my plain-amplitude simulation cannot separate it from the CC1 layer change.

**Criterion:**
- The arrival note of each `<` (191, 591, 203, 603) is within 1 dB of the hairpin's crest.
- Horn 1's held 184/584 notes rise at least 2 dB from the first to the last quarter.
- 196/596 is the loudest beat of its phrase.

## 4. Bar 159, the crescendo into the fff: the brass do not grow, and two stale trims make a hole on beat 2 (measured, simulated)

**Where:** qn 632-636. `ff <` on every part, the suspended-cymbal roll pp <, a breath, then fff largamente at 160.

**Evidence.**
- **Brass across the hairpin** (last third minus first third, c08 -> c09): Trumpet 1 +0.2 -> -3.3 dB, Trumpet 2 -0.3 -> -2.1, Horn 1 -1.2, Clarinet 2 +3.0 -> +0.7. On the master the hairpin grows +1.4 dB.
- **Trumpet 1 per note:** 629 E5 -24.7, 633 F5 -27.4, 634 G5 -25.0. The F5 sits 3.5 dB under its neighbours inside the crescendo.
  - Cause: `build/pitch_trims.json` Trumpet 1 "77": -6, all articulations. It was set on the old CC1-fixed layers.
- **Horn 1:** `note_trims.json` 633.0: -5 (c08 B #1, also set before the CC1 change). It makes a -6.9 dB envelope step (vol 9.68 -> 2.81 at 633.02), and 633 measures -24.7 against 629 -21.9 and 634 -23.3.
- **Other CC1-track trims.** `stale.py` measures each trimmed note against its untrimmed neighbours within 3 qn:
  - The Clarinet 1 pitch trims (G5 -6, A-flat5 -3, B-flat5 -4) leave 9 phrase-top notes 2.3-6.5 dB under their neighbours, at 121.5, 309.5, 419-421, 557.5-561.5 and 639.5.
- **The trims fall from ff to fff.** In `mix.json` the fff anchor is below the ff anchor on 11 of the 13 CC1 tracks (horns -2.7 / -1.6 / -2.3 / -4.5, trumpets -0.7 / -1.6 / -1.0, trombones -1.4 / -1.4, clarinets -0.8 / -1.9 dB). Read along the curve, these subtract inside every ff < fff hairpin.

**Fix:**
- `pitch_trims.json`: Trumpet 1 "77" -6 -> -2. Re-measure its other F5 notes; 640 is also 2.5 dB under.
- `note_trims.json`: Horn 1 633.0 -5 -> 0.
- Clarinet 1 pitch trims halved (79: -3, 80: -1.5, 82: -2), then re-measured.
- On the 11 brass tracks, a start-low shape in `build/score_config.py` `LEVEL_SHAPES`: `[(631.9,0.0),(632.3,-3.0),(635.4,0.0)]`. The crescendo starts under the end of bar 158 and grows into the fff; the arrival and breath shapes are untouched.
- Finding 3(c) removes the ff-to-fff trim slope inside the hairpin.

**Simulated (`simshape.py s2`, the shape plus the two trims as level):**
- Master beat 1 of bar 159 -8.8 -> -9.8 dB, beat 3 -7.2 -> -7.4.
- The hairpin goes from +1.4 to +2.3 dB, and the rise from beat 1 of 159 to beat 1 of 160 from 2.8 to 3.8 dB.
- Delivery with finding 1: limiter 1.5 dB, master peak unchanged (1.452).

**Criterion:** every brass track grows at least 1 dB over 632-636; master beat 1 of 160 at least 3.5 dB over beat 1 of 159.

## 5. Soft passages in the delivered file do not keep the printed order (measured, simulated; one judgement inferred)

**Evidence: delivered S per bar.**
- **Bar 34**, the Bassoon 1 solo (f espr. to mf, `1. Solo`, after the ff cutoff of bar 33) with the violas mp: -30.7 dB. It is the 5th quietest bar of the movement on S and the quietest on M (-34.3), under the pp Lento bars 5 and 14 (-31.8 / -30.5).
  - On the master it is 4-5 dB over those bars (-35.7 against -40.7 / -39.8). The ride lifts it only about +1.4 dB, because bar 33's ff is inside its 3 s window.
- **The mf fugato** (bars 85-88, -28.5 / -26.4 / -27.5 / -27.6) and the Clarinet 1 p < mf theme of bars 127-128 (-30.0 / -29.3) sit in the bottom decile (p10 -28.8 dB).
- **The pp coda chorale** (bars 175-178, -25.5 / -25.1 / -25.4 / -25.4) is louder than:
  - the mp espressivo cello solo before it (bars 171-174, -28.5 / -25.4 / -26.0 / -27.4);
  - every printed mf passage above;
  - the Lento's mp phrases (bars 2/3/6/7, -25.0 / -26.6 / -24.7 / -24.6).
- **Master medians by the bar's loudest printed dynamic:** pp -33.2, p -31.8, mp -34.0, mf -30.5 dB. Delivered: pp -26.5, p -28.5, mp -29.2, mf -26.1. In the delivered file pp bars are louder than p and mp bars.
- **Real orchestra (inferred):** a section or solo line marked mf/espr. should sit over a pp chorale. The final fade should begin from under the cello solo, not from above it.

**Fix** (`build/roles.json`, level only, so a stem fix can apply it). The ride gives back about 60% of a soft-passage mix change (coda -3 dB arrived as -1.0..-1.6 dB delivered), so the values are larger than the target change:
- Bassoon 1 [128.5, 140, +3], Violas [132, 140, +2].
- Violoncellos and Double basses [336, 352, +2], on top of the c06 rows.
- Clarinet 1 [504.5, 512, +2].
- Violoncellos [680, 696, +1.5] and Cor anglais [683, 696, +1.5].
- `_all` [696, 719, -3, ramp 1 qn], percussion excluded. Check that `_all` rows reach `build_perc_track`; the tam-tam pp stroke should keep its level against the strings.

**Simulated (`sim.py s1` + finding 1's delivery):**

| bars | c09 delivered | simulated |
|---|---|---|
| 34 | -30.7 | -29.5 (now over bars 5 and 14) |
| 85-87 | -28.5 / -26.4 / -27.5 | -27.0 / -24.8 / -26.0 |
| 127-128 | -30.0 / -29.3 | -29.0 / -28.2 |
| 171-174 | -28.5 / -25.4 / -26.0 / -27.4 | -27.5 / -24.6 / -25.0 / -26.3 |
| 175-178 | -25.5 / -25.1 / -25.4 / -25.4 | -26.8 / -26.2 / -26.4 / -26.4 |
| 179-180 | -26.2 / -26.6 | -27.6 / -28.2 |
| 181-182 | -29.1 / -32.1 | -28.8 / -31.8 |

The chorale now sits under the cello solo's crest, and the coda falls bar by bar from 178. LRA 14.1 LU, span 18.0 dB, limiter 1.4 dB.

**Criterion:**
- Delivered bar 34 above bars 5 and 14.
- Bars 85-87 above bars 175-178.
- Bars 175-180 at least 1 dB under the louder of bars 172-173.

## 6. Item 7 on single stems: two exposed held notes still cycle in tone colour (measured)

**Method.** Every held note or same-pitch run of 7 s or more, per stem, from 0.8 s after the start to 0.3 s before the end. Detrended over 2 s. Autocorrelation at 3.85-4.05 s.

**Results.**
- **The string re-bows hold:** every string run is at or under 0.26 for the 100-300 Hz band, 0.35 for the centroid and 0.41 for level. Examples: the final chord's Vln II 0.06 / 0.08, Vc 0.19 / 0.14, Cb 0.04 / -0.01.
- **The timpani re-strikes hold:** at most 0.20.
- **Cor anglais, qn 27-35** (bars 7-9, the tied pp note 8 qn long, 9.6 s): centroid 0.65 (window 27-36: 0.42), level 0.29, swing 3.2 dB.
  - The cor anglais is the top line there, 6 dB under the master broadband.
  - The master's own centroid autocorrelation in that window is -0.28, so it is an inner colour change on the solo, not a master pulse.
- **Horn 4, the final chord** (720, three breath splits): level 0.65, centroid 0.59, swing 5.2 dB, 10 dB under the master. Horn 3 measures 0.16 / 0.22.
- **Stems masked by the tutti,** 12-20 dB under the master: Bassoon 2 at 476 (0.65 / 0.49), Bass clarinet at 464 (0.59). I leave them.

**Fix:**
- `BREATH_SPLIT_AT["Cor anglais"] = {27.0: [31.3]}`, one breath at an irregular point inside the tie (about 5 s / 4.6 s pieces), with the c07 breath fall.
- Horn 4 720: move the middle split so that the pieces differ by at least 0.5 s, e.g. `[721.6, 724.3, 725.9]`.
- Re-measure both stems.

**Criterion:** centroid and level autocorrelation under 0.35 on both stems.

## Do not touch

- The bar 122-127 diminuendo, the p arrival at 126, and the tam-tam damp.
- The sub. p falls at 84 and 244.
- The climax order (160 > 122 > 169) and the 636 ARRIVAL_WEIGHT with its string stroke shapes and the E6 fill.
- The suspended-cymbal timing and CAESURA 636.
- The AUTO_REBOW rows and shapes, the timpani re-strike plans and the c06 horn breath splits on Horn 3. On the master, item 7 passes everywhere the music is held.
- The ppp ending level (delivered bar 182 = bar 1) and the SCORE_END fade.
- The delivery ride's ratio 2.5, cap 10 and 3 s smoothing for the soft side (finding 1 changes only what the lift may do to loud frames), and the top ride 1.6.

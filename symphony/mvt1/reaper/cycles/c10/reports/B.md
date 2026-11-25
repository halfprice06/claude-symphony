# Cycle 10, critic B: balance and levels (render c09)

## Method

All numbers come from the stem-fixed c09 render (`cycles/c09/render/`), on the tempo map in `build/parts.json`. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c10-B/`.

- Levels are K-weighted power in 10 ms hops, mean of L and R (`env.py`, `lib.py`). Only differences are used.
- "re master" is the stem level minus the master level over the same window.
- A note body runs from onset +0.08 s to the note end or onset +1.5 s, whichever comes first. The printed dynamic comes from each track's `dyn_curve`.
- `tab.py` lists the loudest stems per window. `solo.py` gives a printed solo's margin over the loudest other sounding stem in 1 qn windows. `mel.py` and `grp.py` give group power sums. `uni.py` lists the unison drops.
- Level-only fixes were simulated on the audio (`simaudio.py`), then run through `tools/deliver_master.py`. Findings 1, 2, 4 and 5 together:
  - delivered LRA 14.7 -> 14.8 LU
  - span 18.2 dB unchanged
  - limiter 2.0 dB unchanged
  - sample peak 1.452 -> 1.453
  - The climaxes are not touched.

## What holds (measured)

- **The printed dynamics map consistently across families.** Note-body medians in dB:

  | Family | p | f | ff |
  |---|---|---|---|
  | Single winds | -41..-46 | -36.5..-38.7 | -31..-35 |
  | Horns | -41.8..-42.8 | -33.4..-36.7 | -28.7..-30.2 |
  | Trombones | | -31.2..-31.9 | -25.5..-26.4 |
  | Trumpets | | -34.2..-34.6 | -25.4..-29.1 |
  | String sections | -40..-44 | -32.3..-37.9 | |

  - At ff this is close to Rimsky-Korsakov's resonance table: string section and horn about +3 dB over one woodwind, trumpet and trombone about +6.
  - The c09 CC1 change left every printed dynamic within about 1 dB of c08. Loud brass is +1 dB K-weighted, from the brighter layers (inferred, not a level problem).
- **Climax 158-161.** The theme group (flutes, oboe, clarinet, horns, trumpets, violins, celli) sits +1.5 dB over all accompaniment combined. Its loudest stem is 2-6 dB over the loudest accompaniment stem.
- **Percussion.**
  - Crash: -12.4 re master at qn 636, then decays.
  - Suspended cymbal: inaudible for 3 beats, then grows into the crash (-19.9 by qn 635).
  - Tam-tam fff: -9.7 re master at qn 484, settling to -15.
  - Tam-tam pp at 696: -10 re master at the stroke.
- **Low end.**
  - Basses minus celli in 61 soft bars: median -3.8 dB (c08 -5.1). Movement II found -2.6 to be right.
  - Loud frames: 60-100 Hz is -13.1 dB re 300-1000 Hz.

## 1. Violas' f eighth and triplet motor buried in the two big tutti passages, bars 97-102 and 116-121 (measured)

**Where:** qn 388-408 and 464-484, track Violas.

**What is wrong (measured):** The violas play the passage's only continuous rhythm, under the ff theme in Fl/Ob/V1 (V2 and CA an octave lower) and the long-note brass. Printed f eighths in 97-102; f triplets in 117-120.

- They sit -19.7..-24.7 dB re master per bar.
- That ranks them 15th-22nd of 31 stems, under every single woodwind doubling the theme.
- Elsewhere the same section reaches -9..-15 re master at f and ff (bars 23-30, 137-138, 157-161).
- The c04 render, before the strokes existed, already had them at -20..-23. So the burial is old.

**Cause:** the c05 roles [388.5, 408, -4] and [464, 484, -3.5, 4]. They took the new Sus strokes back to the old level, which was already too low.

**Fix:** `build/roles.json`, Violas: replace those two rows with [388.5, 408, 2] and [464, 484, 2.5, 4], a net +6 dB. Keep `ROW_TRIM_SKIP` as it is (the passage is all strokes).

**Simulated:**
- Violas -13.8..-18.8 re master, rank 9-17.
- Master over bars 97-102 and 117-121 changes by +0.07/+0.09 dB.

## 2. Accented 1.5 qn theme notes are cut by negative accent-fit steps (measured; tool bug)

**Where:** `build/accent_fits.json` rows with a step of -2 dB or less on accented notes of 1.4 qn or longer:

- BCl 425; Bn1 382, 521; Cl1 105; Fl1 113; Hn1 278; Ob1 105, 113
- Violas 349, 665; V2 273, 361; Vc 521

**What is wrong (measured):**
- `tools/fit_accents.py` line 157 protects only notes with `slen > keep_long_qn`. The default is 1.5, so every dotted-quarter accent is unprotected. This is the same boundary that c09 fixed by hand for Violins I 477.
- **Violas 665** (bar 167, the a2 brass/viola ff theme): row [0, -4.54].
  - In the envelope the pickup sits at +5.4..+6 dB and the accented long note at -1.5.
  - On the stem: pickup -27.8 dB; first quarter of the accent -29.4; body 665.25-666.25 -36.3..-38.6; the notes after it -31..-33.
  - So the accent is a short blip followed by a 5-9 dB hole on the theme's long note.
- Body against neighbours elsewhere: Bn1 521 -7.4, Vc 521 -4.2 (bar 131 theme), Va 349 -3.9. The ff wind notes at 105/113 measure 0..+1, where an accent should be 2-4 over.

**Fix:**
- `tools/fit_accents.py`: make the test `W1[k]["slen"] >= A.keep_long_qn`, and run it with `--keep-long-qn 1.0`.
- Delete the listed negative-step rows, then refit: `fit_accents.py 9 ... --family string|wind|brass --write`.
- This is level only, so it can go in as a stem fix.

**Simulated** (Violas 665 step removed): the long note's body rises 4.5 dB, level with the notes after it and still under the pickup's swell. A refit should then place its swell.

## 3. The unison rule drops a ff theme note in favour of a softer chord tone: Horns 1-2 at qn 670 and Horn 1 at qn 418 (measured)

**Where:** `tools/score_to_parts.py` `find_unisons()`.

**What is wrong (measured, `uni.py`):** The rule keeps the slurred copy first, then the longer one; it never looks at the printed dynamic.

- **qn 670, bar 168 beat 3:** Horns 1-2 a2 play the ff accented A-flat3 (1.5 qn) of the theme. The rule keeps Horn 4's 2 qn chord tone at f (velocity 83, f CC1/CC11), so both theme horns drop it.
  - Horn 1 over 670-671.5: -18.0 dB re master, against -7.4..-9.3 for its neighbouring theme notes.
  - Horn 4 there: -13.7.
  - Trumpet 1 and the violas carry the note alone.
- **qn 418, bar 105:** Horn 1's mf solo line (doubled by the celli) loses its E4 to Horn 3's mp chord note. Horn 1 there: -24.6 dB re master, against -9.4..-13.0 either side.

These are the only 3 of 263 dropped notes where the dropped copy is printed louder than the kept one.

**Fix:**
- In `find_unisons`, rank `keep` by printed dynamic first: `curve_at(dyn_curve, q)` of each copy, louder wins. Then slurred, then length.
- The longer, softer chord copy then goes through the existing `UNI_DELAY` path: it starts at the kept note's end minus `UNI_DELAY_OVERLAP_QN`. So Horn 4 keeps its chord from about 671.4.
- This is a MIDI change; it needs the render.

## 4. Timpani crescendo rolls become the loudest stem over the melody: bars 62-63 and 80-81 (measured)

**Where:** Timpani at qn 244-250 and 316-324.

**What is wrong (measured):**
- **Bars 62-63:** the timpani play a pp < roll; the violins have the sub. p "poco animando" melody.
  - The hairpin ramp (vol -3 -> +3.7 dB, CC7 22 -> 33) plus the tie stroke at 248 (velocity 91) bring the roll to -6.8 re master at qn 247 and -6.5 at 248.
  - That is top or second over V1 (-7.8/-5.9) and V2 (-7.5/-5.7).
- **Bars 80-81:** the timpani play an f < ff roll under p < tremolo strings and the f motive stabs.
  - The roll stays -5.1..-5.8 re master and is top or second in 7 of 8 beats.
  - It grows only 2.7 dB in absolute level (-33.3 -> -30.6) while the master grows 8 dB. It sits on top from the start and does not lead the crescendo.
- Brief rule 5: start at the printed dynamic, then settle under the texture.

**Fix:** `build/score_config.py`, append to `LEVEL_SHAPES["Timpani"]`:
- `[(245.5, 0), (246.5, -2), (247.5, -3.5), (248.6, -3.5), (249.5, 0)]`
- `[(316.3, 0), (316.9, -3.5), (319.5, -3), (323.9, 2), (324.0, 0)]`

The bar-82 strokes are untouched.

**Simulated:**
- Bar 62-63: -9.1..-9.7 re master, under both violin sections.
- Bars 80-81: the roll keeps its f attack on the downbeat, falls 3.5 dB behind the stabs, then grows 5.1 dB (-34.2 -> -29.1) into bar 82.

## 5. Soft flute solos sit under held accompaniment: bars 73-76 and 109-110 (measured)

**Where:** Flute 1 at qn 291-300 ("1. p espr.", then pp) and qn 432-440 ("1. espr." mp).

**What is wrong (measured):**
- **Bars 73-76:**
  - The flute's margin over the loudest other stem is -0.9 dB (median); it is covered in 5 of 9 windows, mostly by the basses' held pp A-flat1.
  - The basses' A-flat1 (MIDI 32) is the hot pitch movement II found. Its median residual is +3.8 dB over 13 notes against the track's same-dynamic median: soft notes +3.5..+5.6 (286, 292, 297, 304, 308, 220, 224).
  - c09 trimmed only qn 132.
- **Bars 109-110:**
  - The flute's margin is -1.9 dB; it is covered in 6 of 8 windows by the bass clarinet's p figure.
  - Flute 1's mp notes have a median of -44.8 dB (7 notes), 3-4 dB under its own p (-41.1) and mf (-41.6).
  - Its soft trims have no mp anchor, so mp gets the p->mf interpolation (+3.9). The notes are low-register B-flat4-D-flat5 (-45..-46 dB).

**Fix:**
- `build/pitch_trims.json`, Double basses: add `"32": -3.5` and extend `_skip_onsets` to `[244.0, 132.0, 216.0]` (132 already has its -7 note trim; 216 is pizz.).
- `build/roles.json`:
  - Flute 1: [432, 438, 3, 0.25]; and [291, 300, 2] on top of the existing +3.
  - Bass clarinet: [432, 440, -2].

**Simulated:**
- Bars 73-76: margin -0.9 -> +2.7 dB, covered 5/9 -> 1/9.
- Bars 109-110: margin -1.9 -> +1.8 dB, covered 6/8 -> 1/8.
- Master in those bars -0.2 / +0.04 dB; delivery unchanged.

## Dan's two checks (measured)

**Loop pulse.** 15 notes are longer than 6 s. The highest autocorrelations at 3.95 s:

| Note | 100-300 Hz | Centroid | Stem re master |
|---|---|---|---|
| Bass clarinet, qn 480 | 0.60 | | -19 dB |
| Horn 4, qn 289 | | 0.57 | -11 dB |
| Bass clarinet, qn 464 | 0.40 | 0.47 | |
| Cor anglais, qn 27 | | 0.41 | -6.7 dB |

- The master over 464-500 and 696-728 measures -0.25/-0.18 (band) and +0.04/-0.07 (centroid): no pulse in the mix.
- None of the findings above lengthens a held note. Finding 5's flute lift covers the Horn 4 note at 289 a little more.

**Accents.** 2-5 kHz, mean of the first 80 ms minus the body at +0.15..+0.45 s:
- Trumpets, trombones and tuba: medians -3.8..-12.4 dB, maximum +2.9.
- Horns: p90 +4.4..+9.0. Worst cases: Horn 3 qn 91 +14.1, Horn 1 qn 670 +11.3. The 670 reading is the hole of finding 3, not a burst.
- Finding 2 adds level to long accented notes' bodies, not to their attacks, so it lowers these readings.

## Do not touch

- The soft and dyn trims fitted in c09 for brass, clarinets and contrabassoon, and the trumpet loud trims. They give the even family mapping above.
- The bar 158-161 theme balance; the climax order (160 > 122 > 167-170); `ARRIVAL_WEIGHT_AT` with the E6 fill.
- The c07 bars 69-71 inner-voice roles and the c09 chorale, recap and second-theme horn rows.
- The tam-tam, suspended-cymbal and crash levels and timing.
- `accent_fits.json` rows other than the listed negative steps. Refit after findings 1-3.

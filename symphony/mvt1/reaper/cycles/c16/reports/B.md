# Cycle 16, critic B: balance and levels (render c15)

## Method

All numbers come from the stem-fixed c15 render (`cycles/c15/render/`, 33 stems) and `build/parts.json` / `build/mix.json` as they were when that render was measured (18:23). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c16-B/`: the c15-B set plus `span.py`, `top4.py` (K-weighted stems re master per bar), `ladder.py`, `rawladder.py`, `steps.py` (dynamic ladders), `trimtab.py` (gain + trim per printed dynamic), `secbal.py`, `hornspots.py`, `hornraw.py`, `h4sim.py` (section balance inside the horns), `solos.py`, `cbsoft.py`, `lowsim.py`, `tilt.py`, `contrib_loud.py` (low end), `tptspots.py`.

Definitions: level = K-weighted power in 10 ms hops; "re master" = stem minus master over the same window; "raw" = note body minus the track's volume envelope (gain + vol_db + dyn/soft trim); "pitch-matched step" = for each pitch a track plays at two printed dynamics (notes of 0.35 s or more, outside hairpins), the difference of the median bodies, then the median over pitches.

## What holds (measured)

- Family levels per printed dynamic are consistent at the soft end. With roles removed, median note bodies at pp are winds -45.7, brass -45.7, strings -45.1 dB; at p -43.7 / -43.6 / -42.0; at mf -40.9 / -39.0 / -38.4. This matches Rimsky-Korsakov's rule that in piano all winds, wood or brass, and one string department are of about equal strength (Principles, PDF p51).
- In forte, horns are +3.5 to +4 dB over a single woodwind and trumpets/trombones +7 to +8 (RK: horn = 2 woodwinds, trumpet = trombone = 2 horns). Horn minus trombone at f/ff/fff is -2.6..-4.1 dB. Tuba minus bass trombone is -1.2 dB at ff.
- On the master, bars whose prevailing printed dynamic is f measure a median -23.1 dB, ff -16.7, fff -9.8, and p -33.5. The climax order is unchanged.
- Percussion:
  - The crash at qn 636 sits at -2.9 dB re master in 5-20 kHz over the first 0.4 s and at -5.1 dB to 1 s.
  - The suspended-cymbal crescendo peaks at -3.4 dB in 5-20 kHz just before the crash.
  - The tam-tam fff at 484 is -7.7 dB K re master from 0.3 to 2 s and settles to -15 dB.
  - The timpani grow only in the printed bar-80/81 crescendo (-9.1 dB re master at the ff).
- Dan's checks:
  - Accents, 2-5 kHz over the first 80 ms minus the body: brass median -7.7 dB (3 of 145 over +3, maximum +3.2: Tpt1 284, Hn3 317/321); winds -6.7 (7 of 220); strings -4.4 (6 of 192; the worst are the known qn 536 tail artefact).
  - Loop pulsing: 8 unsplit notes last 6 s or more. The worst is Bass clarinet qn 11 (6.1 s, 100-300 Hz autocorrelation at 3.95 s 0.81, centroid 0.75). That note carries printed < > hairpins and only 2 s of lag overlap, so the reading is unreliable (inferred).
  - Master windows 0-16, 464-500 and 696-728 read +0.07 or less. The 160-176 window reads +0.45/+0.34 over 7.6 s of a printed ff > mf > p decrescendo that the quadratic detrend does not remove (inferred, not a loop).

## 1. Horn 4, the lowest horn, is the loudest horn in most loud chords (measured)

**Where.**
- Bars 26, 40-41, 69-70, 97, 114.
- Bars 117-124 (letter G and the sostenuto).
- Bars 130-134, 142, 167, 169.
- In general, every f/ff/fff chord where Horn 4 holds its G3/F3/E♭3.

**What is wrong.** Horn 4 is the loudest of the horns that hold through the beat:

| Printed dynamic | Beats where Horn 4 is loudest | Next most often loudest |
|---|---|---|
| f | 33 of 72 | Horn 3, 21 |
| ff | 26 of 64 | Horn 1, 21 |
| fff | 4 of 8 | |

The median of Horn 4 minus the loudest other horn is +1.1 dB at ff and +0.3 at fff.

Examples, re master (K):

| Bars (qn) | Horn 4 | The other horns |
|---|---|---|
| 117-120 (464-478), G3 | -7.8..-10.8 | Horn 3 (G4) -9.8..-14.3; Horns a2 (two players) -10.9..-15.9 |
| 41 (160-161) | -7.7..-12.1 | Horn 3 -11.7..-16.9 |
| 130 (518-519) | -4.6..-6.5 | Horn 4 is the second-loudest stem in the orchestra, over the theme entry (finding 2) |
| 131 (520-522) | -10.1..-13.3 | Horns 1-3 -17.7..-21.9 |

At letter G, Horn 4's held pedal is the loudest brass stem (-9.9 re master over 464-480), above Horn 3, Horns a2, Trombone 1 and the tuba.

**Cause.**
- The envelope gives Horn 4 more than any other horn at loud dynamics. In `build/mix.json`, Horn 4 `dyn_trim_db` is f 2.5, ff 5.3, fff 2.8, against Horn 3 at 0.9 / -0.4 / -0.2.
- With gain, that puts Horn 4 1.6 / 5.7 / 3.0 dB over Horn 3 at f / ff / fff.
- The samples themselves are what a real fourth horn gives. Raw G3 at ff is -29.9 dB, against Horn 3's G4 at -26.0 and C4 at -26.3. The low register is about 4 dB weaker.
- The trim more than cancels that difference. RK (PDF p41) asks for two horns to balance one trumpet; nothing asks for the fourth horn to lead its section.

**Fix.**
- `build/mix.json` Horn 4 `dyn_trim_db`: `{"f": 1.0, "ff": 1.5, "fff": 0.5}`.
- `build/roles.json` Horn 4: change `[504, 518, -4, 2]` to `[504, 520, -4, 0.5]`. The cut now opens at 516-518 and lets the pedal jump to -4.6 dB re master at 518.5, two beats before the recapitulation.
- This is level only, so it can be applied with `stem_fix.py`.
- Refit `accent_fits.json` for Horn 4 accents afterwards.

**Simulated** (stem scaled by the trim change):

| Measure | Now | After |
|---|---|---|
| Horn 4 minus loudest other horn, ff (median) | +1.1 | -2.7 |
| Horn 4 minus loudest other horn, f (median) | -2.3 | -3.8 |
| Share of beats with Horn 4 on top, ff | 57% | 16% |
| Share of beats with Horn 4 on top, fff | 57% | 14% |
| Share of beats with Horn 4 on top, f | 24% | 17% |
| Horn 4 at letter G, re master | -9.9 | -13.5 (master -0.27 dB) |

The fff climaxes (484-496, 636-644) lose 0.1 dB or less.

## 2. Bar 130: the theme's return in Bassoon 1 and Violins II is 6-10 dB under the dominant pedal (measured)

**Where.** Bar 130, qn 515.5-520, the bar before the recapitulation.

**What the score has.**
- Bassoon 1 ("1.") and Violins II, both f, play the head of the first theme (G-E♭-D) two octaves apart.
- Under them, the pedal crescendo: celli repeated G2 sixteenths (f<), Cb G (f<), Horns 3-4 (Horn 4 on G3, f<) and the timpani roll (f<).

**Evidence** (re master, per half beat 516-520):

| Part | Re master | Note |
|---|---|---|
| Bassoon 1 | -9.2..-13.5 | theme |
| Violins II | -12.6..-15.2 | theme |
| Celli | -2.9..-7.4 | loudest stem |
| Horn 4 | -4.6..-9.1 | |
| Double basses | -6.1..-12.1 | |
| Timpani | -10.5..-16.0 | |

Over 516-520, the master is led by the celli at -4.6 and Horn 4 at -7.3, with Bassoon 1 at -10.4. Both theme parts are printed at the same f as the pedal, so the accompaniment needs the usual cut (kit LEARNINGS 13: 3-7 dB).

**Existing roles in this bar.**
- Celli `[512, 520, -4, 2]`.
- Clarinet 1's theme roles end at 520.
- Bassoon 1 and Violins II have nothing before 520. They have `[520, 536, +2]` and `[520, 536, -3.5]`.

**Fix** (`build/roles.json`):
- Bassoon 1 `[515.5, 520.25, 4, 0.25]`.
- Violins II `[515.5, 520.25, 3, 0.25]`.
- Celli: add `[515.5, 520, -3, 0.5]` on top of the existing -4.
- Horn 4: finding 1, plus `[515.5, 520, -2, 0.5]`.

Expected:
- Bassoon 1 about -6..-9 and Violins II about -9..-12 re master.
- Celli about -6..-10 and Horn 4 about -9..-12.
- The theme is then the loudest line or level with the pedal.
- The step into the f/ff of bar 131 keeps its size, because the celli and Horn 4 open again at 520.

## 3. Lento, bars 7-9: the cor anglais espr. solo is 6-12 dB under the celli's crescendo crest (measured)

**Where.** qn 26-32, Violoncellos, Violas, Cor anglais.

**What the score has.** The CA's espr. solo (p < >, mp at its peak) runs into the held G4 at qn 27, falling to pp at 28. Under it, the strings swell pp < p (24-28) > pp (28-32). At qn 26.75 the printed CA (CC 55-62) is a full dynamic above the celli (CC 42).

**Evidence.**
- At 26.75 the celli are 5.6 dB over the CA (-34.7 against -40.3 dB absolute).
- Over 27-28, the celli are -2.9 re master and the CA -9.3, a margin of -6.4.
- Over 28-31, the double basses and Violins II sit 2.8-4.6 dB over the CA.
- Over the whole solo (qn 19-35), the CA is covered in 7 of 16 beats.

Two causes, both measured:

- **(a) The re-bow fill at celli 26.516 overshoots.**
  - The `build/rebow_fills.json` shape "26.516" holds its +10 dB cap from +0.12 to +0.32 s and has a second bump of +7.5..+8.7 at +0.88..+0.96 s.
  - At 0.06 s resolution, the celli stem dips to -41.4 at +0.14 s. It then peaks at -33.6 (+0.44 s), -31.5 (+0.98 s) and -32.1 (+1.5 s), against -36.8 just before the re-bow.
  - So there are three bumps of +3..+5 dB in 1.5 s, at the top of a pp < p hairpin. They read as accented swells, under a solo that is falling away.
  - The fill was fitted on an older render.
- **(b) The pp < p swell is too large.** It rises by:

  | Part | Rise over qn 24.5 to 27-28 |
  |---|---|
  | Celli | +7.8 dB |
  | Violas | +6..+8 |
  | Violins II | +5.9 |
  | Double basses | +2 |

  The pitch-matched string pp-to-p step elsewhere in the movement is +4.5 dB.

**Fix.**
- `build/rebow_fills.json` Violoncellos "26.516": cap every value at +4 dB, and set the 0.84-1.04 s points to at most +2. Or refit that one re-bow with `tools/fit_rebows.py 15 build/parts.json` on the c15 stems.
- `build/roles.json`:
  - Violoncellos `[24, 29, -2.5, 1.0]`.
  - Violas `[24, 29, -2, 1.0]`.
  - Cor anglais `[26.5, 32, 2.5, 1.0]`. This raises its held G4 and pp re-entry and keeps its printed decrescendo shape.
- All level only.

Expected: CA minus loudest other stem at 27-28 goes from -6.4 to about 0, and at 28-31 to about -1..+1. The strings' crest stays audible as a swell of about +5 dB.

## 4. The double basses are the loudest stem in held soft chords, and they fade behind the celli as the dynamic rises (measured; band comparison partly inferred)

**Where.**
- Soft: bars 5, 13, 14 (the end of the Horn 1 solo, qn 52-56), 145 and 175 (the trombone chorale).
- Loud: every f/ff tutti.

**Evidence.**
- **The bass is the loudest stem in six soft bars (K).** Their numbers are:

  | Bar | Printed | Basses | Next loudest |
  |---|---|---|---|
  | 5 | pp | -2.3 | CA -4.3 |
  | 13 | p | -7.4 | Vln I -7.5, Horn 1 solo -9.3 |
  | 14 | pp | -6.8 | Horn 1 p -7.4 |
  | 145 | pp | -7.3 | Vln I -9.2 |
  | 165 | mp | -6.7 | |
  | 175 | pp | -6.6 | celli -7.9; trombones' dolce chorale -9.2/-9.7 |

  At qn 54-55, the pp basses (-5.0) are 6.8 dB over the horn solo's last note (-11.8).
- **Basses against the master and the celli, by printed dynamic:**

  | Dynamic | Basses re master (median) | Basses minus celli |
  |---|---|---|
  | pp | -11.3 | |
  | mf | -11.2 | -1.2 |
  | f | -13.1 | -1.8 |
  | ff | -14.3 | -2.6 |
  | fff | -15.5 | -3.8 |

- **The pitch-matched mf-to-f step on the basses is +0.5 dB** (8 pitches). The envelope dips at f: gain + trim is mf -4.3, f -7.0, ff -6.0.
- **The master's 100-160 Hz share falls with loudness; the Dvořák reference's rises.**

  | Frames | Mix | Dvořák 9/i |
  |---|---|---|
  | Softest 20% | -8.8 | -13.4 |
  | Loudest 10% | -13.9 | -11.0 |

  In the loudest 10% of frames the basses supply 42% of 100-160 Hz and 63% of 60-100 Hz. Over the whole file, 100-250 Hz is under all three references: -9.03 against -6.61 (Dvořák), -8.75 (Brahms 1/ii) and -7.55 (Brahms 4/ii).
- So the bottom is heavy in soft held passages and light in the tutti. The Dvořák file is a lossy MP3, so the 20-100 Hz comparison is not used. The 100-160 Hz trend is the evidence (inferred in part).

**Fix** (`build/mix.json` Double basses):
- `soft_trim_db` pp: 2.0 to 0.5 (keep ppp and p).
- `dyn_trim_db`: `{"f": 2.5, "ff": 4.0}` (now 1 / 2). The envelope then rises from mf (-4.3) through f (-5.5) to ff (-4.0) instead of dipping at f.
- Do not touch the 80 Hz / 100 Hz bells.

**Estimated.**
- Loud frames: 100-160 Hz share +0.9 dB and 60-100 Hz +1.4.
- Basses minus celli at ff: -2.6 to about -0.6.
- Soft bars: the basses 1.5 dB lower, which puts the horn solo (bars 13-14) and the bar-175 chorale over them.
- Check the bar-160 low-brass/basses crest with the limiter (c14 notch at 641.7) after the change.

## 5. Inside a track, f is barely louder than mf in the strings and woodwinds; in the brass it is 7 dB louder (measured; the size of the fix is inferred)

**Where.** Strings and woodwinds, every passage marked mf next to one marked f. Clearest on Violins I, Celli, Double basses and Bassoon 1.

**Evidence.**
- **Pitch-matched step mf to f, as heard:**

  | Family | Step | Pitches |
  |---|---|---|
  | Strings | +1.1 | 31 |
  | Winds | +0.5 | 18 |
  | Brass | +7.4 | 5 |

  Per track: Violins I -1.3, Celli +1.0, Double basses +0.5, Bassoon 1 +0.4, Clarinet 1 +0.8.
- **The neighbouring steps are larger.** f to ff is +6.2 / +6.5 / +5.5, and string mp to mf is +2.5.
- **With roles removed**, mf to f is strings +2.7 and winds +1.9 against brass +5.3. Part of the flat step comes from role cuts in f passages, and part from the f anchor.
- **The envelope (gain + trim) dips at f below both mf and ff** on these tracks:

  | Track | mf | f | ff |
  |---|---|---|---|
  | Violins I | 6.0 | 3.5 | 6.5 |
  | Violins II | 5.2 | 3.5 | 7.0 |
  | Celli | 0.7 | -2.0 | -2.5 |
  | Flutes | 1.2 | -5.3 | -2.3 |
  | Oboes | -2.2 | -3.3 | +0.7 |
  | Harp | -1.5 | -3.0 | -2.0 |

  The Clarinet 1 f trim (-4.2) is justified: its raw sample level jumps +9.5 dB from mf to f, at the layer change.
- **Effect on hairpins.** String crescendos from mf to f grew a median +0.2 dB over 9 hairpins, against +7.9 for p to f. The tutti master is not affected the same way, because f passages have more players.

**Fix** (test on the strings first, level only):
- `build/mix.json` Violins I `dyn_trim_db` f -1.5 to 0. Add `soft_trim_db` `"mf": 1.0` so mf stays where it is; Violins I has no mf anchor, so the f change would otherwise lift mf by 1.5 dB.
- Violins II f -2.5 to -1.0, with an mf anchor of `"mf": -0.8`.
- Celli f -2 to -1.
- Basses as in finding 4.
- Leave the woodwinds until the strings' result is measured.

Pass: string mf to f +2.5..+4 dB pitch-matched, f to ff +4.5..+5.5, climax order and delivered span unchanged.

## 6. Trumpet section: the c15 trims leave inverted chords at f (measured, smaller)

**Where.** Bars 27-31 (qn 104-122, f), bar 122 (484-485, fff) and bar 139 (552).

**Evidence** (re master, held chords):

| Spot | Trumpet 1 | Trumpet 2 | Trumpet 3 |
|---|---|---|---|
| qn 112-113, bar 29 | -16.0..-16.1 | -13.0..-13.6 | -12.6..-14.8 |
| qn 552 | -12.2 | -9.6 | -9.2 |
| qn 484 | -16.4 | -13.9 | -14.8 |

- At qn 112 Trumpet 1 is not a melody voice (it doubles Clarinet 2, Horn 3 and Trombone 1).
- Where Trumpet 1 doubles the melody (bars 82-83, 116, 158-161), its 5-7 dB lead over Trumpet 2 is right and should stay.
- The cause is the f trims: Trumpet 2 6.2 and Trumpet 3 7.7, against Trumpet 1 6.1, on lower and weaker samples.

**Fix** (`build/roles.json`):
- Trumpet 2 and Trumpet 3 `[104, 124, -2, 0.5]` and `[551.5, 554, -2.5, 0.25]`.
- Trumpet 1 `[484, 486.5, 2, 0.25]`.
- Expected: Trumpet 1 level with or 1-2 dB over the lower parts in those chords.

## Do not touch

- The soft-end family balance (pp/p/mf within 2 dB across families) and the forte section ratios.
- The string soft trims from c14 (except the basses' pp in finding 4).
- The climax order with `FAST_CAP_ABOVE` 4 and the top ride 1.6.
- Trumpet 1's melody lead at bars 82-83, 116 and 158-161, and its coda a2 lift.
- Percussion patches, gains, roles and timing (crash, suspended-cymbal lead, tam-tam fff and pp with damp).
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`.
- The Horn 1 F4 and Horn 3 D4 pitch trims.
- The c15 decrescendo trim hold (`SOFT_DECRESC_KEEP` 0.5).
- The second-theme fills / `HP_TARGET_AT` set.
- The letter-G Vln I/II and woodwind roles.
- `_REBOW_FROZEN` and every re-bow fill other than celli 26.516.
- `accent_fits.json`, except a refit after finding 1.

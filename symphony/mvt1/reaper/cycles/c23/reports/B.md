# Cycle 23, critic B: balance and levels (render c22)

## Method

All numbers come from the stem-fixed c22 render (`cycles/c22/render/`, 33 stems) and `build/parts.json` of 03:42, the build that matches it, with `roles.json` and `score_config.py`. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c23-B/`. The envelope cache and page images were deleted when I finished; `env.py` rebuilds the cache in about a minute.

- Re-run from the c22-B set: `env.py`, `fam.py`, `dynx.py`, `bardyn2.py`, `bardynmode.py`, `top21.py`, `oncov.py`, `margA.py`, `mel.py`, `rolls21.py`, `perc21.py`, `tpch.py`, `loopchk.py`, `accents.py`, `kbar.py`, `qtab.py`.
- New scripts:
  - `hpcons.py`: a hairpin shared by two partner parts, where one part's CC changes 12 or more steps more than the other's.
  - `softpeak.py`: the peak of each soft note (ppp-mp, no printed crescendo) against the same track's own mf median.
  - `lowown.py`: which stems own the master's low bands in the loud spans.
  - `refbands.py`: low-band profile of the master against the Dvorak reference, split into loud, middle and soft seconds.
  - Simulations: `simhn162.py`, `simrecap.py`, `simob146.py`, `simbcl1.py`.

Terms:
- "K" means K-weighted and "A" means A-weighted.
- "Re M" is a stem minus the master over the same window.
- "Onset margin" is the melody stem minus the loudest other sounding stem over the first 0.3 s of each melody onset (A).
- Melody and accompaniment were read from score pages 1-17.

## What holds (measured)

**Family dynamic ladders.** K medians of note bodies.

| Family | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| Winds | -45.6 | -41.9 | -40.7 | -38.7 | -36.3 | -32.1 | -26.6 |
| Brass | -46.2 | -43.8 | -40.8 | -36.9 | -33.2 | -27.8 | -23.4 |
| Strings | -47.0 | -42.5 | -39.0 | -37.2 | -33.7 | -27.9 | -22.6 |

- p sounds like p in all three families: the spread is 1.9 dB.
- Bar level against the median printed dynamic: correlation 0.90, slope 3.66 dB per step. This is unchanged from c21.

**Brass sections against Rimsky-Korsakov's forte ratios.** At f (K):
- One trumpet -32.0..-34.9, one trombone -30.6..-31.8, one horn -34.7..-36.6.
- Horns therefore sit 3-5 dB under trumpets and trombones, which matches the 2:1 ratio.
- Trumpets on chords: Trumpet 1 sits -1..+6 dB over Trumpet 2 (`tpch.py`), which is normal for a top voice.
- In bars 167-169 the a2 trumpets carry the ff theme at -6..-7 A re M, the top stem over f accompaniment. That is as printed.

**Percussion and timpani.**
- Tam-tam fff (484): -8.6 K re M from 0.3 to 1.5 s.
- Crash (636): 5-20 kHz at -2.6 re M.
- Suspended-cymbal roll: peak 5-20 kHz at -9.5.
- Timpani: no long roll is the top stem. The tutti f/ff/fff rolls rank 13th-27th.

**Melody onset margins (A), unchanged or better:**

| Bars | Median | Covered |
|---|---|---|
| 15-18 | +8.4 | 0 of 18 |
| 47-54 | +8.2 | 1 of 18 |
| 147-154 | +7.9 | 0 of 22 |
| 98-102 | +4.1 | 0 of 16 |
| 139-143 | +3.1 | 1 of 20 |
| 167-170 | +4.0 | 2 of 16 |
| 56-63 | +4.2 | 6 of 21 |

At the bar 158-161 climax the median is +0.4 with no onset under -1. The brass are level with the tune there, which suits fff.

**Dan's checks.**
- Loop pulsing: the same 8 unsplit notes of 6 s or more. The worst is still Bass clarinet 11.0: 100-300 Hz autocorrelation 0.81, centroid 0.75.
- Accents, 2-5 kHz in the first 80 ms minus the body:

  | Family | Median | Over +3 dB |
  |---|---|---|
  | Brass | -5.4 | 2 of 126 |
  | Winds | -5.8 | 6 of 217 |
  | Strings | -3.7 | 6 of 178 |

  Violas 536 is still the worst, at +14.1 (A's lens).

## 1. Bar 162: Horn 1 does not take part in the brass decrescendo. It rises to the top stem under Violins I, 4-5 dB over the ff oboe and clarinet line and 10 dB over Horn 2, which plays the same hairpin (measured; fix simulated)

**Where.** qn 644-648, score p. 15.
- Every brass part has ff with a decrescendo:
  - Trumpets, trombones and tuba go to mp at beat 3 (targeted, CC 114 -> 58).
  - The horns' hairpin runs on to p at bar 164.
- Oboe 1 and Clarinet 1 carry ff lines. Violins and celli are ff.

**Evidence.**
- Horn 1 against Horn 2, K, per half beat 644.5-647.5: +3.6, +9.0, +7.9, +9.9, +9.7, +6.3, +4.0.
- Horn 1 in A re M rises while the master falls (`top21.py 0.5`):

  | qn | Horn 1 re M | Master |
  |---|---|---|
  | 644.5 | -10.0 | -18.9 |
  | 646.5 | -5.3 | -25.0 |

  It is second only to Violins I (-3.7..-5.9). Oboe 1 minus Horn 1 is -4.4..-5.7 A over 645-647.
- Cause 1, CC11. Horn 1 and Horn 3 get an untargeted decrescendo (`hairpins` [644, 648]), so `dyn_curve` falls only 114 -> 102 by 647.4. Horn 2 and Horn 4 have hairpin [644, 652] targeted to p and fall 114 -> 79 by 648.
- Cause 2, volume. Horn 1 and Horn 2 `vol_db` hold +3.0 dB from 644.5 to 652. Horn 3 and Horn 4 release to 0 by 645.
  - All four horns have the same hpgain [632, 636, 3.0].
  - So the hold is the fff-arrival hold (`FFF_HOLD_CAP`, c02 C #1a) not releasing on the two tracks that rest during the Horns a2 window 628-643.5 (inferred).
- `hpcons.py` finds this pair as the largest partner mismatch in the movement: Horn 1 -14 CC against Horn 2 -33 CC over the same hairpin.

**Fix.**
1. In `score_config.py`: `HP_TARGET_AT = dict(HP_TARGET_AT, Hn1={**HP_TARGET_AT.get("Hn1", {}), 644.0: "mf+"}, Hn3={644.0: "mf+"})`. This lands Horn 1/3 at CC 78 at 648, where Horn 2/4 are (79).
2. Release the held +3 dB on Horn 1 and Horn 2 at 644 as on Horn 3/4: make the fff hold end at the 644 ff mark on tracks whose notes resume after a TRACK_WINDOWS gap. Fallback: `LEVEL_SHAPES["Horn 1"] += [[(644.25, 0.0), (644.5, -3.0), (648.3, -3.0), (648.5, 0.0)]]`, and for Horn 2 `[(644.25, 0.0), (644.5, -3.0), (651.8, -3.0), (652.0, 0.0)]`.

**Simulated** (`simhn162.py`). A Horn 1 envelope of 0 / -3 / -10 dB at 644.25 / 644.5 / 646.5, held to 648.3 (fixes 1 and 2 together are about -8..-10 here):
- Horn 1 minus Horn 2, K, 644.5-647.5: -0.2, +3.5, +0.6, +0.9, -0.3, -3.7, -6.0. That is too far at the end. With the CC target the result should sit nearer 0 (inferred).
- Oboe 1 minus Horn 1: -4.9..-5.7 -> +4.5..+5.6 over 645.5-647.
- Top four stems at 646.5: V1, Ob1, Vc, Hn3.
- Master K at 646.5: -21.8 -> -23.0. The printed decrescendo now reads in the master.
- The climax windows (636-644) are not touched.

## 2. Bars 131-134, recapitulation: the ff first theme (clarinets, bassoons, celli, trombones) is covered in 14 of its 19 onsets, mostly by the Violins I descant (measured; fix simulated)

**Where.** qn 520-536, p. 12.
- The theme returns ff in Cl a2, Bn a2 and Vc, with Tbn 1-2 marked f (merged on Trombone 1, +3 dB UNI_BOOST).
- Fl/Ob/V1/V2 play an ff descant in half and quarter notes.
- The trumpets play f in the timpani rhythm, and the basses have ff eighths.

**Evidence** (`oncov.py`, `margA.py`, `mel.py`):
- Onset margins (A): median -1.4, covered 14 of 19, 5 under -3, worst -5.7 (525.5 and 533.5, Tb1 against V1).
- Coverers: V1 9, Va 2, Fl1 1.
- Half-beat margins: K median -0.7 (16/30 covered, mostly by the basses' eighths); A median -0.4 (19/30, V1 11).
- Theme group against everything else, K: median -4.5 dB per beat.
- This is the first theme's return, and it is the most-covered tune left in the movement. c22 B #5 named it as the next step if it was heard as lost.
- Existing roles over 520-536: Vc +2, Bn1 +2, Tb1 -0.5, V1/V2 -3.5.
- The Tb1 role and its fits are do-not-touch (c17 B), so the fix leaves the trombone alone.

**Fix.** In `roles.json` or as `LEVEL_SHAPES` over 520.3-536 with 0.2 qn ramps:
- Violoncellos, Bassoon 1 and Clarinet 1: +2.5.
- Violins I and Violins II: -1.5.

**Simulated** (`simrecap.py`, "VcBnCl+2.5 desc-1.5"):
- Onset margin median -1.4 -> +1.1.
- Covered 14 -> 5 of 19; under -3: 5 -> 1 (worst -4.4).
- Theme group K: -4.5 -> -2.3.
- Master K over the span: -18.53 -> -18.01. That is 8 dB under the climax, so the climax order and the limiter are not affected.
- Adding -2 dB on the timpani changes nothing measurable. Leave the timpani as it is.

## 3. Bars 145-146: Oboe 1's dolce p E5 swells 8.7 dB inside one note to the oboe's own ff level, before its printed decrescendo (measured; fix simulated)

**Where.** qn 579-582, p. 13.
- The score has `g'4(\p dolce e''4~ | e''2\> d''2)` over pp clarinets, horns 3-4, strings and timpani.
- There is no printed crescendo.

**Evidence** (`softpeak.py`, envelope per 0.25 s):
- The E5 starts at -39.8 K and peaks at -31.1/-31.0 at 580.5-581, the start of the decrescendo.
- That peak is 8.6 dB over Oboe 1's own mf median and at its ff median (-31.9).
- The rise is in the 1-2 kHz band (-41.5 -> -32.5): it is in the sample, not in the data.
  - `cc11` falls 48 -> 28 over 580-582.
  - `vol_db` falls -1.0 -> -3.4.
  - CC1 holds at 110.
- The oboe is -0.6..-0.9 A re M. It lifts the whole master 4 dB in a pp bar: bar 146 is the second-loudest pp-mode bar (-32.3 against a pp median of -36.6).
- This is the largest soft-note overshoot in the movement among wind and brass notes.
- The exposition's matching note at 180 (bar 46) swells less (+4.8 dB rise, peak +4.1 over its mf median).

**Fix.** `LEVEL_SHAPES["Oboe 1"] += [[(579.2, 0.0), (579.9, -3.0), (580.3, -5.0), (581.2, -5.0), (581.7, 0.0)]]`. A NOTE_TRIM/bloom rule on this onset would do the same.

**Simulated** (`simob146.py`):
- Oboe 1 per half beat 579.5-581.5: -34.4 -33.9 -31.4 -31.1 -37.2 -> -36.8 -38.5 -36.4 -35.7 -37.8. That is a held p about 3 dB over the oboe's p median, a solo's level.
- Master K at 580.5-581: -30.6/-30.1 -> -34.1/-33.3.
- Optional, same shape halved: Oboe 1 at 180 (`[(180.2, 0.0), (180.8, -2.5), (181.6, -2.5), (182.0, 0.0)]`). Not simulated.

## 4. Bars 1-4: the bass clarinet sits 2-6.5 dB (A) over the celli in the pp unison and owns the 1-5 kHz bands, so the opening reads as a bass-clarinet solo and its loop-pulsing held note (qn 11) is exposed (measured; the balance is a judgement, inferred)

**Where.** qn 3-16, p. 1. Bass clarinet, celli and basses play the opening line pp in unison, after the timpani's ppp roll.

**Evidence** (`kbar.py`, bars 2/3/4):

| Weighting or band | Bass clarinet minus celli | Bass clarinet minus basses |
|---|---|---|
| A | +6.5 / +1.8 / +3.3 | +8.6 / +6.9 / +5.8 |
| K | +0.6 / -1.2 / +4.7 | |
| 1-2 kHz, bass clarinet re M | -1.0..-2.9 | |
| 2-5 kHz, bass clarinet re M | -0.4..-1.7 | |

- In the 1-2 kHz band the celli sit at -4.5..-8.9 re M, and in 2-5 kHz at -6.2..-12.5.
- One player against a cello section and a bass section at the same printed pp should colour the line, not lead it. Rimsky-Korsakov treats a doubling wind as a tint on the string unison (inferred).
- The bass clarinet's 6.1 s C at qn 11 is the movement's worst loop-pulsing note (autocorrelation 0.81). In bar 4 it is the top stem at -2.2..-3.6 A re M. Lowering it also hides the pulse.

**Fix.**
- `LEVEL_SHAPES["Bass clarinet"] += [[(2.7, 0.0), (2.9, -2.5), (16.4, -2.5), (16.6, 0.0)]]`. It adds to the existing +3 dB shape at 8.7-9.12 and leaves it in place.
- `LEVEL_SHAPES["Violoncellos"] += [[(2.7, 0.0), (2.9, 1.5), (11.9, 1.5), (12.1, 0.0)]]`. It stops before the celli's re-bow fills at 12.1-15.25.

**Simulated** (`simbcl1.py`):
- Bass clarinet minus celli (A), bars 2/3/4: +2.5 / -2.2 / -0.7.
- Master: A bars 2-4 -40.9/-42.0/-49.7 -> -42.2/-42.3/-50.3; K -34.7/-36.0/-42.6 -> -34.8/-35.8/-43.2.
- The opening's soft level is kept within 0.6 dB K, so the p10 span is unaffected.

## 5. Measured, no change proposed

- **Low end in loud passages** (`refbands.py`, loudest 30% of seconds, band minus 300-1000 Hz):

  | Band | Mix | Dvorak |
  |---|---|---|
  | 40-60 Hz | -33.0 | -41.9 |
  | 60-100 Hz | -15.4 | -22.4 |

  - The basses own 20-100 Hz in every tutti (`lowown.py`: -0.2..-3.7 re M).
  - The Brahms references (stored band shares) are heavier still, so I propose no change. If the low end is heard as heavy, the basses' 60-100 Hz is the place to cut.
- **Coda tam-tam pp (696):** -10..-13 K re M for 1.5 s, almost all under 300 Hz (1-5 kHz -23..-43). It is audible as a soft-stick hum, not a crash. Leave it.
- **Bar 72.5:** the celli's subito pp note (qn 286, Leg Slur MAX) opens at -20 K for 50 ms, 20 dB over its own body, and decays over 0.5 s. It is masked by the brass ff accents on the same beat (master -19). A's lens, if anyone hears it.
- **Bar 97:** bass trombone ff whole note, top stem in A (-5.5..-5.8) for beats 1-3 before the ff tune enters. That is printed ff alone in a held chord. Leave it.

## Do not touch

- The family ladders and soft trims; the brass loud trims and roles; the trumpet trims and the a2 trumpet theme at 167-169.
- The percussion patches, gains and timing; `TIMP_CC1_MAP` with the c21 tutti roll shapes.
- The c22 B shapes (fugato basses -5 / celli +1.5, bar 31/82 celli, bars 77-78, Oboe 1 bar 115) and the c21 B shapes (Ob1 648 target, bars 163-166, cor anglais, celli 691.6, Violins II 453, Horns a2 310.5).
- The recap Trombone 1 role -0.5 with its fits.
- The climax order 160 > 122 > 169. Fixes 1-4 change no climax window.

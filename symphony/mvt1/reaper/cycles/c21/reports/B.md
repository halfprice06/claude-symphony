# Cycle 21, critic B: balance and levels (render c20)

## Method

All numbers come from the stem-fixed c20 render (`cycles/c20/render/`, 33 stems) and `build/parts.json` of 01:26, the build that matches it, with `roles.json` and `score_config.py`. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c21-B/`. The c20-B set was re-run on c20 (`env.py`, `fam.py`, `dynx.py`, `oncov.py`, `margA.py`, `grpA.py`, `loopchk.py`, `accents.py`, `simpts.py`). New scripts:

- `top21.py`: the four loudest stems re master (A) per half bar, for the whole movement.
- `stems.py`: chosen stems re master per beat.
- `rolls21.py` and `rollsb.py`: each timpani roll's level re master, its rank, and its 60-300 Hz share against the master and the basses.
- `perc21.py`: the percussion strokes.
- `tpch.py`: the three trumpets on three-note chords.
- `simca.py`, `simca2.py`, `simcoda.py`, `simob.py`, `sim164.py`, `simtimp.py`: envelope simulations of the fixes below.

"A" means A-weighted and "K" means K-weighted. "Onset margin" is the melody stem minus the loudest other sounding stem over the first 0.3 s of each melody onset. Melody and accompaniment were read from score pages 3, 7-13 and 15-18. A-weighting understates low instruments, so every finding about cellos, basses or timpani was also checked in K or in a frequency band.

## What holds (measured)

**Dynamic ladders** (K, median note bodies) are unchanged from c19 within 0.3 dB:

| Family | p | mf | f | ff |
|---|---|---|---|---|
| Winds | -41.7 | -38.7 | -36.2 | -32.1 |
| Brass | -43.9 | -37.1 | -33.2 | -27.9 |
| Strings | -42.3 | -37.0 | -33.5 | -27.5 |

- p is within 1.6 dB across the three families.
- Against the median stem at the same printed dynamic (`dynx.py`): Trumpet 2/3 sit at +0.2..+2.6. Trumpet 1 sits at +4 at f/ff, because it plays the a2 lines alone (Trumpet 2 has no notes at 664-680) and the top note of chords. On three-note trumpet chords Trumpet 1 is a median 2.2 dB over Trumpet 2, which is normal for a top voice.

**Percussion.**
- Tam-tam fff (484): -8.2 K re master over 0.3-1.5 s.
- Tam-tam pp soft stick (696): -9..-11 K, 4th to 6th stem in K.
- Crash (636): 5-20 kHz -2.7 re master.
- Suspended-cymbal roll: peaks at -22 K / -9 dB in 5-20 kHz into the crash.
- None of them covers a melody.

**c20 B changes.** The bars 39-41 melody onsets now have a median of +1.2, with 1 of 21 under -3. Bars 77-81: median +3.2, none under -3.

**Other melody passages** (A onset margin):

| Bars | Median | Covered / onsets |
|---|---|---|
| 15-22 | +5.5 | 3 / 38 |
| 47-55 | +6.1 | 4 / 28 |
| 117-121 | +2.0 | 3 / 21, none under -3 |
| 140-144 | +2.5 | |
| 178-182 | +2.8 | |

**Dan's checks.**
- Loop pulsing: the same 8 unsplit notes of 6 s or more as in c19. The worst is still Bass clarinet 11.0 (bar 3, 6.1 s, -4.8 dB re master, the top stem there): 100-300 Hz autocorrelation 0.81, centroid 0.75. That is A's lens, but it is the most exposed held note in the movement.
- Accents, 2-5 kHz in the first 80 ms minus the body:

  | Family | Median | Over +3 dB |
  |---|---|---|
  | Brass | -5.5 | 2 of 126 |
  | Winds | -5.8 | 7 of 217 |
  | Strings | -3.5 | 4 of 178 |

  The worst is still Violas 536 (+13.6).

## 1. Bars 163-166: the Violins I line is covered in 9 of its 13 onsets (5 under -3 dB). Oboe 1 does not take part in the decrescendo it shares with the violins, and the mp counter-lines in the violas and Clarinet 1 sit 4-7 dB over the mp melody (measured; fix simulated)

**Where.** qn 648-664, p. 17, after the fff climax. Violins I descend from ff, decresc to mp at bar 164, rit. at bar 165, p at bar 166. Oboe 1 doubles them an octave lower in bar 163 under the same hairpin. Violas and Clarinet 1 have mp imitative figures in bars 164-166.

**Evidence.**
- V1 onset margins 648-664: median -2.3; covered 9 of 13; 5 under -3; worst -7.2 at 654 (by the violas).
- `mockup-events.tsv` gives Oboe 1 a decresc from 648 to 650 with no target dynamic. Its `dyn_curve` falls only 114 -> 102, while Violins I's falls 114 -> 62 by 651.75.
- Over 650-651.9, re master (A):

  | Stem | dB |
  |---|---|
  | Oboe 1 | -3.7..-6.6 |
  | Violins I | -4.5..-10.1 |

  So the oboe's held F (650, 2 qn) is 2-5 dB over the line it doubles, and the decrescendo is not heard.
- At 653.5-654 the violas and Clarinet 1 are -3.0/-3.3 re master, against Violins I at -7.0/-10.2. All three are printed mp.

**Fix.** In `build/score_config.py`:
- `HP_TARGET_AT["Ob1"] = {648.0: "mf"}`, so the oboe falls with the violins.
- Exact shapes, if the hairpin target is not preferred or after it:
  - `LEVEL_SHAPES["Violins I"] += [[(651.8, 0.0), (652.0, 3.0), (661.8, 3.0), (662.2, 0.0)]]`
  - `LEVEL_SHAPES["Violas"] += [[(652.0, 0.0), (652.3, -2.0), (661.8, -2.0), (662.0, 0.0)]]`
  - `LEVEL_SHAPES["Clarinet 1"] += [[(651.8, 0.0), (652.0, -2.0), (661.8, -2.0), (662.0, 0.0)]]`
- Simulated with Oboe 1 at -5 dB over 650-652.2 (`sim164.py`):
  - V1 onset median -2.3 -> +1.1; covered 9 -> 3; under -3 5 -> 0; worst -7.2 -> -2.2.
  - Violins I over Clarinet 1 over 652-662: median +2.1 -> +7.1, never under.
  - Master bars 163/164/165: -26.0/-29.4/-32.1 -> -26.2/-29.2/-32.0. The diminuendo is kept.
- Judgement on the voices (inferred): the counter-lines stay audible as mp imitations 4-7 dB under the top line. If the actor reads the viola figure as the leading voice in bar 164, use -1 instead of -2 on the violas.

## 2. Bar 153: the cor anglais's sustained p notes cover the mf second-theme melody (violas, celli) by up to 4.3 dB K / 7.9 dB A, because the +4 dB role written for its p answers runs to qn 620 (measured; fix simulated)

**Where.** qn 602-620, p. 15. Horn 1, violas and celli play the second theme. Bars 147-152 have the cor anglais's p echo fragments, then from bar 153 it holds sustained p notes with the bassoons: 608 (3.76 qn), 612, 614, 616. Horn 1 rests over 608-612.

**Evidence.**
- `roles.json` Cor anglais `[586, 620, 4]` (c04 B #3: the answers sat under the pp Violins II tremolo).
- On the 608 whole note the cor anglais rises from -14.1 to -2.6 K re master by 610.5. Its `vol_db` goes 4.0 -> 5.5 and CC11 47 -> 50, so the rest of the rise is the sample's own bloom.
- Melody minus cor anglais over 602-620 (half beats):

  | Weighting | Median | Under 0 | Worst |
  |---|---|---|---|
  | A | +2.3 | 12 of 36 | -7.9 at 611.0 |
  | K | +4.2 | 6 of 36 | -4.3 at 610.5 |

- Onset margins 584-620: 7 covered, 4 under -3, all by the cor anglais.

**Fix.**
- `roles.json` Cor anglais `[586, 620, 4]` -> `[586, 605, 4, 0.5]`, so it ends after the last answer (604).
- `LEVEL_SHAPES["Cor anglais"] += [[(608.0, 0.0), (608.6, -2.0), (611.6, -2.0), (612.0, 0.0)]]` to hold the bloom of the bar-153 whole note.
- Simulated (`simca2.py`):
  - Melody minus cor anglais: A median +2.3 -> +5.6, under 0 12 -> 4, worst -1.9; K median +4.2 -> +7.9, never under.
  - Master bars 152/153/154: -32.0/-32.4/-35.4 -> -32.3/-33.2/-35.9.
  - The cor anglais is still 6-12 dB over the pp Violins II there.

## 3. Coda bars 173-174: the cello solo's high point (C5 at 692, the crest of the printed < >) is 4 dB under its bar-172 note, and the cor anglais (p, +6 dB of stacked roles) is level with it or over it (measured; fix simulated)

**Where.** qn 683-695, p. 18. The cellos have the mp espr. solo with hairpins ending in the 691-692 crescendo to C5 and a decrescendo to bar 175. The cor anglais has the p espr. imitation.

**Evidence.**
- Cello stem K per bar 171-174: -33.4 / -33.5 / -35.8 / -37.7.
  - 692-694 (the crest): -36.8.
  - 685-687 (the tenuto A-flat4 of bar 172): -32.8.
  - The master falls from bar 173 to 174: -32.8 -> -34.7.
- The cor anglais carries `[683, 695, 2.5]`, `[683, 696, 1.5]` and `[683.0, 694.0, 2.0]`, so +6 dB.
- From 691 it holds C5, the same pitch the cellos arrive on at 692.
- Cello minus cor anglais, half beats 683-695:

  | Weighting | Median | Under 0 |
  |---|---|---|
  | A | +1.7 | 9 of 24 |
  | K | +3.4 | 5 of 24 |

  At 691.5-692.5 the margin is -0.8..-1.8 K.

**Fix.**
- `LEVEL_SHAPES["Cor anglais"] += [[(687.3, 0.0), (687.6, -2.5), (694.6, -2.5), (694.8, 0.0)]]`. This leaves the imitation's entry at 683-687 as it is.
- `LEVEL_SHAPES["Violoncellos"] += [[(691.6, 0.0), (691.9, 4.0), (693.2, 4.0), (693.8, 0.0)]]`.
- Simulated (`simcoda.py`, with +3 on the celli):
  - The crest goes -36.8 -> -34.3 dB (+4 brings it level with bar 172).
  - Cello over cor anglais: K never under (worst +1.3); A under 0 in 3 of 24 (worst -0.9).
  - Master bar 174: -34.7 -> -34.3.

## 4. The f/ff/fff timpani rolls in the loud tuttis (bars 117-123, 158-160, 167-169) start at only 4-12% of the master's 60-300 Hz energy and sit 5-9 dB under the basses in that band (measured; whether they are too low is inferred)

**Evidence** (`rollsb.py`, `rolls21.py`). Roll front (first 0.3 s) as a share of the master's 60-300 Hz:

| Rolls | Front share | Body vs basses (same band) |
|---|---|---|
| Letter G f rolls, 464-480 | -11.5..-15.9 | -5.2..-9.2 |
| fff at 484 / 488.6 (vel 127) | -10.2 / -11.6 | -4.6 / -5.6 |
| ff 628-632, fff 636 | -5.4..-7.7 | -6.2..-7.9 |
| f 664 (5.7 s, bars 167-169) | -6.9 | -5.9 |

- In A every one of these rolls ranks 17th-26th of 32 stems.
- Rule 5 asks for the printed dynamic at the start and a settle under the texture after it. These rolls start under the texture, so the fff arrival at bar 122 has no audible drum. This is consistent with LEARNINGS' note that the rule overshot on the soft rolls in movement II (c25).

**Fix (test).** In `score_config.py`:

```
LEVEL_SHAPES["Timpani"] += [[(463.9, 0), (464.05, 3), (491.5, 3), (492.0, 0)],
                            [(627.9, 0), (628.05, 3), (643.5, 3), (644, 0)],
                            [(663.9, 0), (664.05, 3), (675.5, 3), (676, 0)]]
```

- The existing settle still acts on top.
- Simulated (`simtimp.py`):
  - Fronts -10..-16 -> -7.6..-13.0. Bodies remain 1.6-6.2 dB under the basses.
  - Loudest 3 s window (K): 122 -10.68 -> -10.61, 160 -8.88 -> -8.80, 167-170 -13.59 -> -13.57. The climax order and the limiter are unaffected.
- Leave the ff roll at 492.98 (bar 124 decrescendo) and the soft rolls alone.

## 5. Smaller items (measured; low priority)

- **Violins II tremolo, bar 114.25-114.5.** It is still over the Vln I mp-cresc melody: V1 onsets 453.5/454 at -4.3/-3.5 against V2, and V2 is -8.3/-8.9 re master against V1 at -9.8/-11.2.
  - Optional: `LEVEL_SHAPES["Violins II"] += [[(452.8, 0), (453.2, -3), (455.8, -3), (456.2, 0)]]`.
  - The rest of bars 111-116 has a median margin of +1.1.
- **Bar 79 is 0.1 dB under bar 78** (-32.2 / -32.1). The Horns a2 accented mf entry (311) is still the top stem at -1.8 K re master. A further -1.5 dB on the c20 Horns a2 shape over 310.5-311.5 would give the bar-78-79 rise.
- **Bass clarinet 11.0 loop** (above): its 6.1 s note is the solo line in bar 3. A's lens should split it (a same-pitch re-tongue near 9.0 s), or add a `loop_fills` shape on it.

## Do not touch

- The c20 B shapes: Violins II 152-162 / 316-324, Horns a2 310-313.9, bar-12 violas/Vln I, Horn 2 bar 32.
- The c20 C shapes: bar-51 Horn 1/celli, coda basses steps, basses 80 Hz loud shelf.
- The trumpet roles and trims, and the Trumpet 1 climax loud_eq. The trumpet section balance is now normal.
- The percussion patches, gains, roles and seats.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB` and the roll settle. Finding 4 adds shapes on top and does not change them.
- The c04 cor anglais answer lift up to qn 605, and the c16 cor anglais imitation entry at 683-687.
- `accent_fits.json` / `accent_bodies.json`, `_REBOW_FROZEN`, `FAST_CAP_ABOVE` 4 with top ride 1.6.
- The climax order 160 > 122 > 169. Findings 1-4 together change the loudest 3 s windows by at most 0.08 dB.

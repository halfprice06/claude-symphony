# Cycle 22, critic B: balance and levels (render c21)

## Method

All numbers are from the stem-fixed c21 render (`cycles/c21/render/`, 33 stems) and `build/parts.json` of 02:34, the build that matches the stem fix, with `roles.json`, `early_fills.json` and `score_config.py`. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c22-B/`. The c21-B set was re-run on c21 (`env.py`, `fam.py`, `dynx.py`, `top21.py`, `margA.py`, `rolls21.py`, `perc21.py`, `tpch.py`, `loopchk.py`, `accents.py`). New scripts:

- `kbar.py`: chosen stems re master per bar, K, A or one band.
- `rankK.py`: the loudest stems over a span, K or one band.
- `lowbar.py`: the master's low bands per bar against 300-1000 Hz.
- `pizz.py`, `pizzabs.py`: the double-bass pizzicato peaks (50 ms, K) by printed dynamic.
- `spread.py`: each track's median note body per printed dynamic, phrase by phrase, listing spreads of 7 dB or more.
- `relown.py`: a passage's note bodies against the same track's median at that dynamic.
- `bloom.py`: the rise inside long f/ff notes.
- `qtab.py`: A-weighted stems re master per half beat.
- `cmp2021.py`: c20 against c21 per span. It uses the c20 envelopes in `mvt1-c21-B/env`.
- `simpz.py`, `simvc.py`, `simbcl.py`: envelope simulations of fixes 1-3.

"K" means K-weighted and "A" means A-weighted. "Re master" is the stem minus the master over the same window. Melody and accompaniment were read from score pages 2-18. A-weighting understates the low strings and K-weighting overstates them at moderate levels (c18 B), so every finding about celli or basses was checked in both, or in a frequency band.

## What holds (measured)

**Dynamic ladders.** These are K medians of note bodies.

| Family | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| Winds | -45.6 | -41.9 | -40.8 | -38.7 | -36.3 | -32.1 | -26.7 |
| Brass | -46.2 | -43.8 | -40.8 | -36.9 | -33.2 | -27.9 | -23.6 |
| Strings | -47.0 | -42.4 | -39.1 | -37.1 | -33.8 | -27.5 | -23.4 |

- p sounds like p in all three families: they are within 1.9 dB of each other.
- At f and ff, one string section or one brass player is 3-4.5 dB over one wind player. That matches Rimsky-Korsakov's forte ratios.
- Bar level against the median printed dynamic: correlation 0.90, slope 3.65 dB per step.

**Trumpets.** On three-note chords Trumpet 1 sits -1..+6 dB over Trumpet 2. That is normal for a top voice. In bars 167-169 Trumpet 1 plays the a2 theme alone, 2-3 dB over Horns a2 (K -7.6..-8.0 re master). That fits two trumpets against two horns.

**Percussion and timpani.**
- Tam-tam fff (484): 0.3-1.5 s at -8.3 K re master. That is printed fff, l.v.
- Tam-tam pp (696): 1-5 kHz at -23..-43 re master.
- Crash (636): 5-20 kHz at -2.7.
- Suspended-cymbal roll: 5-20 kHz peak at -9.4, 1.5-4 s before the crash.
- Timpani rolls after the c21 +3 dB: f/ff/fff tutti rolls rank 13th-26th in A, and no long roll is the top stem. The bar 128-129 mp/mf roll ranks 3rd and 6th inside its printed crescendo, under the Clarinet 1 solo.

**Basses after the release cap.** The basses are 1.0-1.4 dB lower (K) in their f/ff eighth passages: bars 15-18, 27-32, 82-83, 131-134, 140-142, 167-170. Celli and Violins I did not change (`cmp2021.py`). In K, the basses minus the celli at bars 27/28/29/30 is +4.7 / 0.0 / -1.8 / -0.1 dB. The c14 target was -1..-3, so the bass is still solid. No level restore is needed for balance.

**Dan's checks.**
- Loop pulsing: the same 8 unsplit notes of 6 s or more as in c20. The worst is still Bass clarinet 11.0: 100-300 Hz autocorrelation 0.81, centroid 0.75.
- Accents, 2-5 kHz in the first 80 ms minus the body:

  | Family | Median | Over +3 dB |
  |---|---|---|
  | Brass | -5.5 | 2 of 126 |
  | Winds | -5.8 | 6 of 217 |
  | Strings | -3.7 | 7 of 178 |

  The worst is still Violas 536 at +14.1.

## 1. Bars 85-87 (fugato): the double-bass mf pizzicato is 8.4 dB louder than its f pizzicato and as loud as the cello subject. Three stacked roles (+7 dB) cause it (measured; fix simulated)

**Where.** qn 336-348, score p. 8. The celli play the fugato subject mf. The basses play pizz. mf quarter notes under it.

**Evidence.**
- Basses' pizzicato peaks (50 ms, K, `pizzabs.py`), medians by passage:

  | Bars | Printed | Peak (K) |
  |---|---|---|
  | 47-55 | pp | -43.3 |
  | 147-155 | pp | -47.2 |
  | 107-109 | p | -46.5 |
  | 85-87 | mf | -29.6 |
  | 103-106 | f | -38.0 (velocity 83 against 73 here) |

  The mf passage is the loudest pizzicato in the movement. `spread.py` also flags it: the basses' mf note bodies are -32.4 at bars 85-88 and -41.1 / -38 / -36 elsewhere.
- Against the subject, at each pluck (re master, K): basses -4.7 / -1.9 / -0.5 / -2.5 / -3.0, celli -1.4 / -4.3 / -1.5 / -1.4 / -2.8. Two plucks are louder than the melody.
- The pizzicato makes the passage boom.
  - The master's 60-100 Hz band at the plucks is +15.4 / +4.7 / +10.7 / +0.5 / -8.9 dB against 300-1000 Hz.
  - Bars 85-87: +1.7 / +4.9 / +0.8. The movement's median is -14.1.
- Cause, in `roles.json`, Double basses `[336, 358, 3]` (c02 fugato), `[336, 348, 2]` (c06) and `[336, 352, 2]` (c10 soft-passage lift). The `vol_db` reaches +10.0 at 341.98. The celli have their own roles, so these rows only need to stay on the celli.

**Fix.** In `score_config.py`, add a step shape. It is at full depth before the first pluck, per LEARNINGS 13 for plucked notes:

```
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(335.8, 0.0), (335.9, -5.0), (348.0, -5.0), (348.3, 0.0)]]
```

Simulated (`simpz.py`):
- Pizzicato peaks go to -33.5..-38.5 K. That is still 3.4 dB over the f pizzicato of bar 103, which is right for an exposed two-part texture.
- Re master: -4.7..-8.7.
- The cello subject is on top at every pluck.
- 60-100 minus 300-1000 Hz at the plucks: +14.4 / +0.3 / +5.9 / -4.7 / -11.8.
- Master K for bars 85/86/87: -30.3/-31.6/-32.3 -> -31.0/-33.1/-34.2.
  - If the delivery ride does not make up the 1.5-1.9 dB, put +1.5 dB on the celli over 336-348. They carry the subject (inferred).
- Bar 84 (the sub. p arco note) is untouched.

## 2. Bar 31 (and bar 82): the celli's ff bass notes bloom 6 dB and rise over the Violins I theme. The master's 160-300 Hz jumps 3.5-5.5 dB (measured in K and A; fix simulated)

**Where.** qn 120-124, p. 3. The celli play ff half notes (A-flat3 at 120, F3 at 122) under the ff theme in Violins I, flutes and oboes. Bar 82 (qn 324-328), the A-flat2 under the ff motive, is the same case, but in K only.

**Evidence.**
- Celli ff note bodies (K) on the same line, bars 27-32:

  | Pitches | Body (K) |
  |---|---|
  | C4-E-flat4 (104-114) | -36.5..-30.8 |
  | A-flat3 (120) | -24.6 |
  | F3 (122) | -23.6 |
  | G3 (124) | -24.1 |

  - Across the movement, ff F3/A-flat3 have a median -24.8 and C4 has -33.6.
  - The A-flat3 at 120 grows from -27 to -21 dB within its first 0.8 s (50 ms frames). That is the sample's own bloom; no hairpin is printed.
  - `early_fills.json` adds 3.3 dB at 120 and 5.6 dB at 122 (hold 0.35 s). The `vol_db` goes from the -3 role to +2.6 at 121.86.
- Bar 31 re master:
  - K: celli -6.8, the loudest stem; Violins I -9.3. In bars 27-30 the celli were -11.7..-15.7.
  - A at 31.5: celli -9.8, Violins I -9.5. The two are level.
- Violins I minus celli per half beat over 120-124, K: +2.0 +3.9 -1.2 -4.4 -3.3 -3.1 -6.5 -6.4.
- Master 160-300 Hz: bar 31 -23.9, against bars 28-30 -28.8 / -29.4 / -25.4. The celli supply it alone (-0.9 dB re the master band). That is the bass line booming, not a solid floor.
- Bar 82: celli -8.3 K re master, top stem over Violins I -10.9. The existing -3 shape is in place. In A the celli are not in the top four.

**Fix.**
- `LEVEL_SHAPES["Violoncellos"] += [[(120.3, 0.0), (120.6, -4.0), (123.75, -4.0), (124.0, 0.0)]]`. It starts after the A-flat3's attack and fill, and returns before the 124 accent (accent fit 4.5 kept).
- Optional, K only: `[(324.25, 0.0), (324.5, -2.0), (327.9, -2.0), (328.2, 0.0)]`, on top of the existing bar-82 -3.

Simulated (`simvc.py`):
- Violins I minus celli at 120-124: +2.5 +7.6 +2.8 -0.4 +0.7 +0.9 -2.5 -3.1. The last beat is the F3 with its 5.6 dB fill. Lowering that fill to 3.0 dB in `early_fills.json` should take the rest (inferred).
- Celli re master in bar 31: -6.8 -> -9.9.
- Master 160-300 Hz in bar 31: -23.9 -> -26.6, in line with bars 28-30.
- Master K in bar 31: -17.3 -> -17.8. Bar 82: -15.6 -> -15.9, celli -8.3 -> -9.9.

## 3. Bars 77-78: the bass-clarinet solo (mf espr.) is level with the p tremolo and 3.5-5.3 dB under the mp clarinet answer (measured in A; fix simulated)

**Where.** qn 304.5-310, p. 8. The bass clarinet has its "Solo mf espr." phrase over Violins II and violas p tremolo. Clarinet 1 answers mp from 306.5 on high notes (B5 at 307) while the solo's eighth-note tail is still sounding.

**Evidence** (`qtab.py`, A, re master).

| qn | Bass clarinet | Clarinet 1 | Violins II |
|---|---|---|---|
| 305-306 | -3.5..-4.5 | — | -3.9..-4.2 |
| 307.0-307.5 | -6.8 / -7.5 | -3.3 / -2.1 | — |
| 309.0 | -5.3 | -3.6 | — |

- Bass clarinet minus the loudest other stem, per half beat 304.5-310: +3.2 -0.5 +0.7 -0.3 -1.4 -3.5 -5.3 +3.7 +0.5 -1.7 +1.6 -4.1.
- Clarinet 1 there is +2.9 dB over its own mp median, while the bass clarinet is at its own mf median (+0.3).
- `roles.json` already has Bass clarinet `[304.5, 310, 2]` and Violins II `[304, 320, -3, 4]`.

**Fix.** In `score_config.py`:

```
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(306.3, 0.0), (306.45, -3.0), (309.8, -3.0), (310.2, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(304.3, 0.0), (304.5, -2.0), (306.4, -2.0), (306.6, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(304.3, 0.0), (304.5, -1.5), (306.4, -1.5), (306.6, 0.0)]]
```

- Simulated (`simbcl.py`): +5.2 +1.5 +2.7 +1.6 -1.2 -0.7 -2.3 +6.1 +3.5 +1.3 +1.6 -4.1.
  - The remaining negatives are the clarinet's first two notes over the solo's last eighths, which the score sets one dynamic apart.
  - 310.0 is the solo's release.
- The answer stays 1-3 dB under the solo, an mp imitation.

## 4. Bar 115: Oboe 1 enters f without the crescendo gain the others carry, 7 dB under Oboe 2 and 3-5 dB under the flutes in unison (measured; small)

**Where.** qn 456-460, p. 11. Flutes a2, Oboe 1 and Violins I play the f quarter notes of bar 115 into letter G. Oboe 2 holds under them.

**Evidence.**
- Oboe 1 note bodies at 456-459: -42.7 / -42.8 / -42.4 / -40.9 K. That is under its own p median (-39.3).
- Its f median elsewhere is -34.6 (`spread.py`: 13.6 dB spread across its f passages).
- In the same notes:
  - Oboe 2: -35.1..-35.7 (`vol_db` +4..+5.5 from its mp crescendo ramp).
  - Flute 1: -36.7..-40.1.
- Oboe 1's `vol_db` is 0 over 455-460, because it enters cold (LEARNINGS 4).

**Fix.** `LEVEL_SHAPES["Oboe 1"] += [[(455.7, 0.0), (455.85, 4.0), (459.8, 4.0), (460.3, 0.0)]]` brings the oboe to its partners' level in the unison (inferred: not simulated). At -21 dB re master it does not change the bar's balance.

## 5. Bar-level notes (measured; no change proposed)

- **Recapitulation, bars 131-134.** The theme (clarinets, bassoons, trombones, celli) against the ff descant (flutes, oboes, violins): A onset margin median -0.4, covered 20 of 30, mostly by Violins I. K median -1.0, covered 16 of 30, mostly by the basses' eighths.
  - The roles already cut the violins 3.5 dB and lift the celli, bassoons and Trombone 2.
  - c20 B left it alone unless a listener hears the theme lost. It is the most-covered tune that remains. If it is heard as lost, the next step is Violins I/II -1.5 more over 520.5-536 (not simulated).
- **Bar 12 (Lento f).** The basses' A-flat2 whole note blooms +9.5 dB and is the top stem in K (-7.2..-8.6 re master, owning 100-160 Hz). In A it is not in the top four. Leave it unless the low end is heard as heavy there.

## Do not touch

- The trumpet trims and roles (section balance normal).
- The percussion patches, gains and timing.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`, and the c21 +3 dB tutti roll shapes. No roll covers anything.
- The c21 B shapes: Oboe 1 hairpin target at 648, bars 163-166, cor anglais 586-605/608/687, celli 691.6, Violins II 453, Horns a2 310.5.
- The basses' release cap and their f/ff trims. The 1-1.4 dB they lost leaves the bass at the c14 target.
- The celli's fugato roles.
- `accent_fits.json` / `accent_bodies.json`, the soft trims, the family dynamic ladders, and the climax order 160 > 122 > 169. Fixes 1-4 change no loud window.

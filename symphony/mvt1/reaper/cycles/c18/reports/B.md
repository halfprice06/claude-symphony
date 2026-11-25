# Cycle 18, critic B: balance and levels (render c17)

## Method

All numbers come from the stem-fixed c17 render (`cycles/c17/render/`, 33 stems) and the build that matches it (`build/parts.json` 21:16, `mix.json`, `roles.json`, `accent_fits.json`, `pitch_trims.json`). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c18-B/`. The c17-B set was re-run on c17 (`env.py`, `steps.py`, `fam.py`, `top6.py`, `rank.py`, `loopchk.py`, `accents.py`). New scripts: `aw.py` (A-weighted per-window ranking), `margA.py` (melody top minus accompaniment top, K and A), `grpcmp.py`, `tpt.py`/`tptn.py` (trumpet section per onset), `near.py` (near-pitch dynamic steps), `perc18.py`, `boom.py`, `cbharm.py`/`cbeq.py` (bass harmonics and an EQ simulation), and `simtp*.py`/`simmarg*.py` (stem simulations).

Definitions:
- "K" is K-weighted power in 10 ms hops.
- "A" is an A-weighting applied to eight band envelopes (20-60 ... 5-20k Hz).
- "re master" is stem minus master over the same window.
- Simulations scale the c17 stems by the proposed dB curve and sum them again.

Melody and accompaniment were assigned from the score pages (pp. 1-17 at 90 dpi) and `mockup-events.tsv`.

## What holds (measured)

**Family ladders** (median note bodies, wind / brass / string):

| Dynamic | Wind | Brass | String |
|---|---|---|---|
| pp | -45.6 | -46.2 | -47.1 |
| p | -41.5 | -43.9 | -42.5 |
| f | -36.2 | -32.9 | -33.4 |
| ff | -32.3 | -28.2 | -27.3 |
| fff | -26.6 | -23.3 | -23.3 |

- p sounds like p in every family, within 2.4 dB.
- At f, a woodwind sits about 3 dB under a string section, and the brass about 3 dB over the winds. This matches Rimsky-Korsakov's ratios.
- Master by the loudest printed dynamic: pp -37.9, p -34.6, mp -32.5, mf -31.3, f -26.6, ff -17.6, fff -10.6. There are no reversals.

**Percussion:**
- Crash fff (qn 636): stem -11.7 dB K re master and -2.2 dB re master at 5-20 kHz for 0.6 s. It lifts the master's 5-20 kHz band by 4.7 dB re 300 Hz-2 kHz, then decays by +3 s.
- Tam-tam fff (484): the loudest stem for about 3 s (-7.5 K re master at +0.6 s), over a sustained chord with no melody.
- Tam-tam pp (696): a 60-100 Hz hum. It is not among the 7 loudest stems A-weighted.
- Suspended cymbal: as in c16. The pp start of the roll is masked under the ff tutti until about 1 s before the crash, and it peaks on the crash.

**Trumpets at ff/fff:**
- Trumpet 1 over Trumpet 2 on shared onsets: median +1.7 dB at ff (14 onsets), +3.4 at fff (5).
- Trumpet 1 over Trumpet 3: +3.9 at ff, +2.4 at fff.
- Trumpet 1 leads the coda theme (bars 167-169) at -6.3..-8.4 K re master.

**Dan's checks:**
- Loop pulsing: the same 8 unsplit notes of 6 s or more as in c16.
  - Horn 4 289: 100-300 Hz autocorrelation 0.58, centroid 0.55, borderline.
  - Bass clarinet 11: 0.81, under printed hairpins.
  - Master windows 0.06 or less, except 160-176 (+0.52), which is the printed decrescendo trend.
- Accents, 2-5 kHz energy in the first 80 ms minus the body:

  | Family | Median | Over +3 dB |
  |---|---|---|
  | Brass | -7.0 | 3 of 133 |
  | Winds | -5.9 | 10 of 220 |
  | Strings | -3.3 | 5 of 186 |

  The worst brass case is Horn 3 536, the known bar-134/135 artefact. Trumpet 1 284 is +2.8 dB on the attack and +7.5 dB over its own line (see finding 2).

**Melody margins (A-weighted):**
- Bars 23-25: +2.7, covered 1/24 half-beats. The c12 open item is closed.
- Bars 27-31: +3.6.
- Second theme, bars 47-52: +8.5.
- Soft solos (cor anglais, Horn 1, Flute 1, Clarinet 1, Oboe 1, the viola solo at 107-108): each is the loudest stem.

**A measurement note on the low strings (measured; the conclusion is inferred).** The K-weighted per-beat ranking marks the double basses as the loudest stem at bars 131-132 (ff eighths, 3-5 dB over Violins I) and at 129.5, 157.75 and 165. A-weighted, the basses are 3-5 dB under the violin theme at 131-132, and are never the top stem there. K-weighting counts the 40-100 Hz fundamentals almost at full weight; a listener at moderate headphone level does not. Do not cut the basses' global f/ff trims on the K ranking alone. Use both weightings for bass-against-treble balance (LEARNINGS 13).

## 1. Bars 53-55: the harp's p arpeggios cover the cello melody as it falls from mf to p (measured; fix simulated)

**Where.** qn 208-220. The harp has p arpeggios (printed p at 184 and 220). The celli carry the melody (dolce, mf from 183, decrescendo at 212, p at 216), with the Clarinet 1 mp line from 207.

**Evidence.**
- Melody top (celli, Horn 1, Clarinet 1) minus accompaniment top, per half beat:
  - A: median +1.1 dB, covered 9 of 22, worst -4.2.
  - K: median +1.2, covered 10 of 22, worst -4.8.
- The harp is the covering stem in 7 of the 9 A-weighted cases:

  | Beat | Harp re master (A) | Celli re master (A) |
  |---|---|---|
  | 53.25 | -3.7 | -4.8 |
  | 54.00 | -4.1 | -3.9 |
  | 54.12 | -3.3 | -4.3 |
  | 54.25 | -3.0 | -6.8 |
  | 55.12 | -2.2 | -6.5 |
  | 55.25 | -3.5 | -6.1 |

- In bars 47-52, where the melody is louder, the margin is +8.5 dB, so the harp's level only shows once the celli fall.
- **Cause.** The harp is not in `soft_trim_db._except`, so it gets the global p +5 dB on top of gain -4. Harp p (-45.5 dB median) is as loud as harp mp (-44.9).

**Fix.**
- `build/roles.json`, Harp: add `[206, 220, -3, 1]`. Level only, so `stem_fix.py` can apply it.
- Leave the global soft trim.

**Simulated** (harp -3 dB, 208-220):
- A: median +1.1 -> +3.3, covered 9 -> 5 of 22, worst -4.2 -> -2.3.
- K: covered 10 -> 4 of 22.
- Master -0.5 dB over those three bars.
- The harp stays at -6..-10 dB re master, still clearly heard.

## 2. The second trumpet stands over the first at f: bars 69-72, 115 and 139-140 (measured; fix simulated)

**Evidence** (`tptn.py`, A-weighted bodies over +0.03..+0.6 s on onsets shared by both trumpets).
- At f, Trumpet 1 minus Trumpet 2: median -0.1 dB over 25 onsets. Trumpet 1 is under on 13 of them, and by more than 2 dB on 5.
- Worst cases:

  | Bar | Onset (qn) | Trumpet 1 minus other |
  |---|---|---|
  | 72.25 | 285 | Trumpet 2 -6.2 |
  | 71 | 280 | Trumpet 2 -4.7 |
  | 139.5 | 554 | Trumpet 3 -3.5, Trumpet 2 -2.4 |
  | 115 | 456 | Trumpet 2 -3.1 |
  | 140 | 556 | Trumpet 2 -2.6 |
  | 72 | 284 | Trumpet 2 -2.0 |

- At ff and fff the order is right (above).

**Bars 69-72** (p. 6). Trumpet 1 doubles the tune of Flutes, Oboes and Violins I at f. Trumpet 2 holds A-flat4/G4 under it, then both play the accented chords of bar 72.
- Trumpet 2 is the second or third loudest stem at 70.12, 70.75-71.25 and 72.12-72.88 (A -6.7..-9.3 re master). Trumpet 1 is at -11..-17 there.
- Causes:
  - **The role ends at the accented chord.** `roles.json` Trumpet 2 `[272, 284, -3]` ends at 284, so the bar-72 chords get the full +3 back, plus the GENTLE_ACCENT +2.5 swell (`vol_db` +2.5..+2.9 at 284.08/285.08/286.08).
  - **Trumpet 1's accents are cut instead of swelled.** `accent_fits.json` gives Trumpet 1 "284" `[0.0, -6.0]` and "285" `[0.0, -5.82]`. The fitter compared the high A-flat5/E-flat5 with Trumpet 1's quieter bar-71 line, and it still measures +7.5 dB over that line. Do not raise Trumpet 1 here; lower Trumpet 2.
  - **The held G4 swells.** Trumpet 2's held G4 at 280 carries a +1.5 dB long-note swell (vol -2.8 -> -1.5 -> -3.0 over 280-283).
- The f trims favour the lower parts: Trumpet 1 6.1, Trumpet 2 6.2, Trumpet 3 7.7.

**Fix** (level only):
- `build/mix.json` Trumpet 2 `dyn_trim_db` f 6.2 -> 4.7, with an mf anchor at the current mf value so mf does not move.
- `build/roles.json` Trumpet 2:
  - `[272, 284, -3]` -> `[272, 288, -3, 1]`;
  - add `[279.75, 284, -1.5, 0.25]`;
  - `[551.5, 554, -2.5, 0.25]` -> `[551.5, 557, -2.5, 0.25]`.
- `build/roles.json` Trumpet 3: `[551.5, 554, -2.5, 0.25]` -> `[551.5, 557, -2.5, 0.25]`.
- Keep Trumpet 1 284/285 in `--skip` at their current values on the next accent refit, so the fitter does not cut them further.

**Simulated:**
- Trumpet 1 minus Trumpet 2 at f: median -0.1 -> +1.8, under on 13 -> 3 of 25, worst -6.2 -> -1.7.
- Specific onsets: 285 -> -1.7, 280 -> +0.3, 284 -> +3.3, 456 -> -1.6, 554/556 -> -0.4/-0.7.
- Trumpet 1 minus Trumpet 3 at f: worst -3.5 -> -1.5.
- ff is unchanged (+1.7).
- Master -0.1 dB over bars 70-72.

## 3. Recapitulation, bars 131-134: the trumpets (printed f) stand 2.5-3 dB higher in the mix than in the same passage of the exposition, and top the ff themes (measured; fix simulated)

**Score.** pp. 2 and 12. Bars 27-30 and 131-134 give the trumpets the same f rhythmic figure (Trumpets 1-2 a2, Trumpet 3) under ff strings and woodwinds.

**Evidence.** Over the 16 qn of each passage:

| Stem | Exposition, 104-120 | Recapitulation, 520-536 |
|---|---|---|
| Trumpet 1, re master (K / A) | -15.8 / -14.6 | -13.0 / -11.4 |
| Trumpet 3, re master (K / A) | -16.8 / -16.1 | -15.0 / -13.5 |
| Violins I, re master (K) | -8.7 | -11.2 |
| Trumpets minus Trombone 1 (A) | +0.5 | +3.3 |

- In the recapitulation Violins I carries `roles.json` `[520, 536, -3.5]`.
- c17 B #1 lowered Trombone 1 here (-0.5 role) but left the trumpets.
- Melody top (Violins I/II, Flute 1, Oboes, celli, Bassoon 1, Trombone 1) minus accompaniment top, A-weighted: median +1.7 dB, covered 10 of 32 half-beats, worst -8.2.
- Trumpet 1 is the covering stem in 8 of the 10, at its eighth-note attacks: 131.12 -7.3, 131.62 -8.4, 132.12 -7.7 A re master, over Violins I -9.3..-10.5.

**Fix.** `build/roles.json`: Trumpet 1, Trumpet 2 and Trumpet 3 `[520, 536, -2.5, 0.5]` (level only).

**Simulated:**
- A: covered 10 -> 5 of 32, median +1.7 -> +2.1.
- Trumpets minus Trombone 1: +3.3 -> about +0.8, the exposition's balance.
- Master -0.2 dB.
- Brass weight inside the tutti is kept: the trumpets stay at -13.9..-16 A re master, the same as in the exposition.

## 4. Every double-bass F2, and the 87 Hz second harmonic of every F1, booms: the sample's fundamental is 7-16 dB stronger than at the neighbouring pitches (measured; EQ effect simulated on the note spectra)

**Where.**
- F2 notes: qn 36-38, 148, 252, 268, 360, 378, 440, 552, 588-608. That is bars 10, 38, 64, 68, 91, 95, 111, 139 and 148-153, from pp to f.
- F1 notes: 72-81 (bars 19-21), 97, 545, 624 (bar 157, f, 4 qn) and 648.

**Evidence** (`cbharm.py`: FFT of each bass note of 0.8 s or more over +0.15..+1.5 s).
- Fundamental minus the stronger of harmonics 2-3:

  | F2 | D2 | E-flat2 | E2 | G2 | A-flat2 | C2 |
  |---|---|---|---|---|---|---|
  | +12.7 (10 notes) | +2.0 | -3.8 | +0.3 | +5.5 | +7.1 | -3.2 |

- The master's 20-100 Hz band re 300 Hz-2 kHz at F2 notes is -9.5 dB, against -12.9 at D2 and -17.7..-19.5 at E2/E-flat2.
- At F1 the 87 Hz second harmonic puts the master at -10.4 dB. Bar 157 (F1, f) is the third most bass-heavy bar of the Allegro on `boom.py` (-4.8 against a movement median of -13.1).
- The kit had found F2 hot in movement II as well (LEARNINGS 14: +3.9 dB left after the c25 bell; a -2 dB trim was proposed). Here `pitch_trims.json` has "41": -2. A level trim lowers the whole note and leaves the 87 Hz peak standing over its own harmonics.

**Fix** (`build/mix.json`, Double basses `eq`):
- Replace `{"band": "bell2", "hz": 100, "db": -2, "bw_oct": 0.8}` with `{"band": "bell2", "hz": 87, "db": -6, "bw_oct": 0.35}`. The ReaEQ in `build_reaper.py` has one free bell2 slot, so the narrow bell replaces the broad one.
- Net change against the current EQ: 60 Hz -0.2 dB, 80 Hz -2.8, 87 Hz -4.4, 95 Hz -2.0, 100 Hz -0.6, 110-160 Hz +0.3..+0.5. The 125-180 Hz body is untouched.
- Then set `pitch_trims.json` Double basses "41" from -2 to 0. The EQ takes 3.5 dB off the F2 notes' power, so the note level falls 1.5 dB net.
- Leave the loud-tutti `loud_eq` (bell2 98 Hz -4) as it is.
- This is a mix change (`--mix-only` before the render), not a stem fix.

**Simulated** (per-note spectra with the net EQ curve):

| Pitch | Master 20-100 Hz re 300 Hz-2 kHz | Bass stem power |
|---|---|---|
| F2 | -9.5 -> -13.7 (the C2/D2 range) | -3.5 dB |
| F1 | -10.4 -> -14.7 | -2.5 dB |
| E2 | -17.7 -> -20.9 | -0.8 dB |
| Other pitches | within 1.2 dB | within 0.8 dB |

Check after the render: the master's 20-100 Hz share in the loud frames, which must stay within 0.5 dB of c17, and the c13/c14 coda 60-100 Hz measures.

The G1/G2/B1 pedals at bars 127-130 and 175 are also bass-heavy in context (-8..-9 re 300 Hz-2 kHz). Their fundamentals are normal for the instrument, and A-weighted they sit under the clarinet solo and the trombone chorale. No change is proposed for them (inferred).

## Do not touch

- The family ladders, the trumpet ff/fff trims and the coda roles.
- The c17 recapitulation Trombone 1 role and accent hand values. Finding 3 adds only trumpet rows.
- The percussion patches, gains, seats, roles and timing: tam-tam fff/pp, crash, sus. cymbal key 64 / lead 0.25.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB` and the c17 soft-roll roles.
- The basses' global f/ff trims and the 180 Hz body bell. The K-only evidence against them does not hold A-weighted.
- The c16/c17 fugato, bar-121/124/125 and bar-130 roles; the string f trims with their mf anchors; the soft-solo roles; the Horn 4 trims.
- `accent_fits.json`, including Trumpet 1 284/285 (skip them in refits).
- `_REBOW_FROZEN`; the climax order (160 > 122 > 169) with `FAST_CAP_ABOVE` 4 and the top ride 1.6.

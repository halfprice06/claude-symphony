# Cycle 13, critic B: balance and levels (render c12)

## Method

All numbers come from the stem-fixed c12 render (`cycles/c12/render/`), mapped through `build/parts.json`. That file is dated 12:45, after the stem fix, so it matches the render. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c13-B/`. They are the c12-B set plus these:
- `samedyn.py`: stem minus same-dynamic stems.
- `pairs2.py`: same-window instrument pairs.
- `solos.py`: solos.
- `accents.py`
- `sim2.py` to `sim6.py`: simulations.

Definitions:
- **Level:** K-weighted power in 10 ms hops (L+R mean). Only differences between levels are used.
- **re master:** the stem level minus the master level over the same window.
- **Note body:** from onset +0.08 s to the note's end or to +1.5 s, whichever comes first.
- **Pairs:** two stems that both hold a note through the same 1 qn window at the same printed dynamic.
- **Simulations:** the dB change is applied to the stem envelopes and the master is re-summed.

## What holds (measured)

**Dynamic mapping across families at soft levels.** Median note bodies:

| Dynamic | Woodwinds | Horns | Trombones and tuba | Strings |
|---|---|---|---|---|
| p | -39..-46 | -42..-45 | | -40..-44 |
| pp | -44..-46 | | -46..-48 | -43..-46.5 |

So p sounds like p, and pp like pp, within about 3 dB in every family. The timpani rolls sit lower, by the settle rule.

**Master per bar, by the bar's median printed dynamic:**

| ppp | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| -40.2 | -34.5 | -31.8 | -29.2 | -27.7 | -22.7 | -17.1 | -9.8 |

The order is monotonic. On 3 s maxima the climaxes run 160 (-9.1) > 122 (-10.0) > 169/170 (-13.0/-13.2) > 26 (-13.8).

**Melody over accompaniment** (top melody stem minus top other stem, 1 qn windows):

| Passage | Bars | Margin (dB) |
|---|---|---|
| First theme | 15-23 | +3.7 |
| ff themes | 27-30 | +3.5 |
| ff themes | 97-102 | +3.0 |
| ff themes | 139-142 | +4.3 |
| ff themes | 158-161 | +3.3 |
| Second theme, Hn1+Vc | 47-55 | +5.2 |
| Second theme, recap | 147-155 | +5.1 |
| Coda cello solo | 171-174 | +6.5 |
| Violas p espr. | 107-108 | +7.3 |

- Bars 23-25 and 135-137 are fixed: the tune is on top in nearly every beat.
- In the second theme, Horn 1 (mp) sits 2.6 / 1.3 dB under the celli (mf), which is correct.
- The brass f harmony under the ff themes stays 3-7 dB under Violins I.

**Trumpets and percussion against the rest:**
- At f the trumpets equal the trombones: Tp1-Tb1 -0.5, Tp2-Tb2 -0.2, Tp3-BTb +1.3 dB.
- Tp1 minus Oboe 1 is +2.6 at f and +2.9 at ff.
- Tam-tam fff (qn 484): -7.9 dB re master at +0.3..1 s.
- Crash (636): 5-20 kHz -3.1 dB re master over its first 0.3 s.
- Suspended cymbal: its pp < reaches 5-20 kHz -5.3 dB re master in the last half beat before the crash.
- Tam-tam pp (696): -7.7 on the stroke, then -10..-18.
- Timpani f/ff strokes: +1.5 / +0.9 over the basses.
- All of these fit the print.

**Dan's checks:**
- *Loop pulse:* 14 notes are longer than 6 s. The master over the held passages reads (100-300 Hz autocorrelation at 3.95 s / centroid):

  | Passage | Band | Centroid |
  |---|---|---|
  | 464-500 | -0.24 | +0.06 |
  | 696-728 | -0.29 | -0.09 |
  | 712-728 | -0.46 | -0.05 |

  The worst stem is Bass clarinet 480 (band 0.60), at -19 re master: inaudible.
- *Accent attacks:* 2-5 kHz, first 80 ms minus the body.
  - Brass: median -6.8 dB. 5 of 143 are over +3: Hn3 536 +6.1, Hn1 311 +5.4, Hn1 273 +4.9, Tp1 676 +3.3, Tp1 284 +3.1.
  - Winds: median -6.0.
  - The wind and string outliers at qn 536 (Va +18, Bn1 +12, Cl1 +7) come from the ff-to-mf drop at bar 135: the attack window holds the ff tail. They are not hard attacks.
- None of the fixes below changes an attack, a CC11 lane or a note length.

## 1. The fff brass chords (bars 121-123 and 160-161) are bottom-heavy: Trumpets 2-3 and Horns 3-4 fall back at fff, and the celli are the loudest stem of bar 123 (measured; reference Rimsky-Korsakov)

**Where.** qn 484-492 (the fff sostenuto chords with the tam-tam) and qn 636-644 (the main climax). Trumpets 2-3, Horns 3-4, Violoncellos.

**Evidence: pairs** (same window, same printed dynamic):

| Pair | f | ff | fff (windows) |
|---|---|---|---|
| Trumpet 2 - Trombone 2 | -0.2 | -0.9 | -3.8 (12) |
| Trumpet 3 - Bass trombone | +1.3 | -0.6 | -2.5 (12) |
| Trumpet 1 - Trombone 1 | -0.5 | +1.8 | -0.5 (10) |
| Horn 3 - Trombone 2 | -1.4 | -3.8 | -5.4 (10) |
| Horn 4 - Trombone 2 | -2.8 | -5.9 | -6.4 (7) |
| Horn 1 - Trombone 1 | -1.9 | -3.2 | -1.9 (10) |

- Rimsky-Korsakov (Principles, "Comparison of resonance") puts "Trumpet = Trombone = Tuba = 2 Horns" in loud passages, so a horn should sit about 3 dB under a trombone.
- At fff the inner trumpets are 2.5-3.8 dB light, and Horns 3-4 are 2.4-3.4 dB light. Horn 4 is also 2.9 dB light at ff.
- The cause is in `build/mix.json` `dyn_trim_db`: the fff anchors of these four tracks sit well under their ff anchors, more than the trombones' do.

  | Track | ff | fff |
  |---|---|---|
  | Trumpet 2 | 10.5 | 7.4 |
  | Trumpet 3 | 12.1 | 9.6 |
  | Horn 3 | -0.4 | -2.7 |
  | Horn 4 | 3.8 | -0.7 |

**Evidence: bars 122-123.**
- The celli are the loudest stem: -10.7 dB re master over 484-492 and -8.8..-10.4 per beat at 488-491. Next: Violins I -11.7, Trombone 1 -13.3, Trombone 2 -11.2..-11.7.
- metrics.md bar 123: celli -20.5, the next stem -24.1.
- The celli give most of the master's 160-300 Hz there (share -2.2 dB).
- They play an inner G3/A♭3 at CC11 125-127, with the 150 Hz +6 dB loud EQ, and +3..+5 dB in their volume envelope (crescendo hold plus the 484 arrival weight).
- In this chord the trombones and trumpets, not the cellos, should carry the weight.

**Fix (level only, a stem fix will do):**
- `build/mix.json` `dyn_trim_db` fff:
  - Trumpet 2: 7.4 -> 10.4
  - Trumpet 3: 9.6 -> 11.6
  - Horn 3: -2.7 -> -0.2
  - Horn 4: -0.7 -> 2.8
- `build/roles.json` Violoncellos: add `[484, 492, -3, 1]`.
- Optional: Horn 4 ff 3.8 -> 5.3.

**Simulated (`sim2.py`):**

| | Before | After |
|---|---|---|
| Tp2 / Tp3 at 484-492 (re master) | -15.1 / -14.1 | -12.4 / -12.5 |
| Hn3 / Hn4 at 484-492 | -17.7 / -17.9 | -15.6 / -14.8 |
| Tp2 at 636-644 | -16.4 | -13.8 |
| Hn3 at 636-644 | -14.6 | -12.4 |
| 3 s max, bar 122 | -10.17 | -9.98 |
| 3 s max, bar 160 | -9.00 | -8.68 |

- Top five stems at 488-492 after the fix: Vln I, Tbn 2, B.tbn, Tpt 2, Tpt 3. Before: Vc, Vln I, Tbn 2, B.tbn, Vln II.
- Master: +0.22 / +0.14 dB at 122-123, +0.31 at 160-161.
- The margin of 160 over 122 widens from 1.17 to 1.30 dB, so the climax order holds. The delivery limiter may take about 0.3 dB more at 160.
- The accent fits are unaffected: the anchors follow the printed curve, so accents inside a fff span move with their neighbours.

## 2. The final chord (bars 181-182, qn 720-728) is a violin note with a faint chord under it (measured levels; inferred judgement)

**Where.** The strings' pp > ppp morendo chord and the ppp horns. The voicing, read from parts.json:

| Part | Note |
|---|---|
| Violins I | C5 |
| Violins II | G4 |
| Violas | E4, the major third |
| Celli | C3 |
| Basses | C2 |
| Horns 3/4 | C4 / G3 |

**Evidence (per qn, re master):**

| Part | Level |
|---|---|
| Violins I | -3.3..-5.3 |
| Violins II | -7.6..-9.3 |
| Violas | -7.6..-10.5 |
| Celli | -10.4..-13.0 |
| Basses | -11.9..-14.8 |
| Horns 3/4 (ppp) | -9.0..-14.4 |

- Violins I stand 4 dB over Violins II, 4.5-5 dB over the violas' third, 6-7 dB over the celli and 8 dB over the basses.
- Both horns sit above the celli and the basses.
- Every string section is printed at the same dynamic. Rimsky-Korsakov treats string sections as equal in piano.
- The top-heavy balance comes from the Violins I re-bow pieces (vol +3.2..+3.9 at 722.8-723.3) and the low strings' soft slope. The c12 shapes improved the bass, but only part of the way.
- Inferred: a listener hears a held high C with the colour note E barely present, at the end of the movement.

**Fix:** `build/roles.json`. Leave the c12 `LEVEL_SHAPES` on the celli and basses and the re-bow rows as they are.
- Violins I: `[720, 729, -2.5, 0.5]`
- Violas: `[720, 729, 2]`

**Simulated (`sim5.py`):**

| qn | Vln I | Violas | Master |
|---|---|---|---|
| 720-724 | -4.4 -> -6.6 | -7.9 -> -5.6 | -0.30 dB |
| 724-728 | -4.6 -> -6.8 | -9.0 -> -6.7 | -0.35 dB |

- Violins II and the celli rise 0.3 dB relative to the master.
- The morendo becomes slightly deeper, and the chord's top three voices end within about 2 dB of each other.
- To keep Violins I on top by 1 dB, use Violas +1 instead.

## 3. Coda theme, bar 169 beats 3-4 (qn 674-676): the ff theme sinks to the level of the f accompaniment (measured)

**Score.**
- Theme, ff: Trumpets 1-2 a2 (played by Trumpet 1), Horns 1-2 a2 (Horn 1) and violas.
- Accompaniment: Fl/Ob/Cl, Tbn 1-2, Violins I/II div. chords and celli, all f, with a < hairpin into the ff fermata chord of bar 170.

**Evidence (0.5 qn windows, re master):**
- Bars 167-168: the theme leads by 4-8 dB (Tp1 -4..-7).
- At 674.5-676 the theme reads:

  | Stem | Level |
  |---|---|
  | Trumpet 1 | -10.3..-11.3 |
  | Horn 1 | -11.4..-13.7 |
  | Violas | -18.5..-20.5 |

  Against it: Trombone 2 -10.5..-10.8, Violins II -10.7..-11.3, Violins I -11.4..-12.2, Flute 1 -11.9..-13.8.
- The theme margin is +0.5 / -0.6 / -0.6 dB. At 672.5 the celli (-6.7) cover the pickup by 5.2 dB.
- The violas, a full voice of the unison theme, sit 8-9 dB under Trumpet 1, even with their +3 role.

**Fix:** `build/roles.json`. Existing c02 rows here: Violins I `[664,676,-3]`, Violins II `[664,680,-4]` and `[676,680,-3]`, Violas and Horn 1 +3/+2 on `[664,680]`. Add these new rows on top of them:
- `[672, 676, -2.5]` on Trombone 1, Trombone 2, Violins I, Violins II, Flute 1, Oboe 1, Clarinet 1 and Violoncellos.
- `[672, 676, 1.5]` on Trumpet 1.
- `[672, 676, 2]` on Violas.

All end at the fermata downbeat, so the ff chord of 170 is untouched.

**Simulated (`sim6.py`, celli not included):**

| qn | Theme margin | Master |
|---|---|---|
| 674.0 | +3.5 -> +7.5 | |
| 674.5 | +0.5 -> +2.5 | -0.6..-0.7 dB |
| 675.0 | -0.6 -> +1.8 | -0.6..-0.7 dB |
| 675.5 | -0.6 -> +2.2 | -0.6..-0.7 dB |

- The step into the ff chord grows from +3.5 to +4.1 dB, so the printed crescendo still arrives.
- The celli row also clears the 672.5 pickup.

## 4. The bass line thins as the tutti gets louder: the double basses lose 5 dB against the celli between pp and fff (measured gap; inferred fix)

**Evidence: pairs, Double basses minus Violoncellos:**

| pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|
| -2.5 (51) | -1.4 (26) | -2.7 (13) | -3.5 (23) | -4.1 (45) | -5.4 (35) | -7.7 (9) |

Sustained-note bodies from mf to f:

| Section | mf -> f |
|---|---|
| Basses | +1.4 dB |
| Celli | +2.9 |
| Violas | +4.8 |
| Violins II | +5.8 |

- Same-dynamic median: the basses sit at -2.2 / -3.2 / -3.2 dB at f / ff / fff.
- Part of the cause is in `vol_points` (`tools/build_reaper.py`). The basses' soft trim p +8 has no mp/mf anchor and tapers to f 0. That gives about +5.7 at mp, +3.0 at mf and 0 at f, so the trim takes back 3 dB of the mf-to-f step.
- At ff/fff the celli's loud EQ and roles widen the gap further; finding 1 removes the worst case.

**Not a plain level raise.** Simulated `sim4.py`, basses +2 dB at f-fff:

| Band | Change in the loud tuttis |
|---|---|
| Master K | +0.04..+0.09 dB |
| 20-60 Hz | +1.7..+1.9 dB |
| 60-100 Hz | +0.8..+1.7 dB |
| 100-160 Hz | +0.2..+1.1 dB |

A plain raise would add boom (the master's 63 Hz third-octave is already -1.6 re 1 kHz against -6.2 in the Dvořák reference) and barely any audible weight.

**Fix (inferred; check against critic C's low-band numbers before rendering):** `build/mix.json` Double basses.
- `loud_eq` bell 160 Hz +4 -> +6 dB (bw 1.0).
- `loud_eq` bell2 98 Hz -2 -> -4 dB (bw 0.5).
- `dyn_trim_db` f 0 -> 1, ff 1 -> 2.

The aim is +1.5..+2 dB in the basses' 100-250 Hz body at f/ff with the 60-100 Hz band unchanged.

**Target:** Cb minus Vc at f/ff about -3 dB, as at mf.

## 5. The opening ppp roll is louder than every later soft roll, and runs over the strings at the end of bar 4 (measured; low priority)

**Evidence: timpani roll bodies, 0.3-3 s after each piece:**

| Roll | qn | Body (dB) |
|---|---|---|
| Opening ppp | 0-16 | -44.1..-47.2 |
| p | 48-56 | -51..-58.5 |
| pp | 502 | -51.8 |
| pp | 692 | -49.2 |
| Final ppp | 720-728 | -52..-55 |

- The movement's first and softest-marked roll is 5-8 dB above the others.
- The cause is the c01 role `[0, 16, 12]` on top of the c12 ppp trim.
- Against the quietest sustained string section it reads -0.7..-4.7 dB through bars 1-3. That is the 3-5 dB-under target of LEARNINGS section 13. At qn 12.2 and 14.2 (bar 4, where the strings decrescendo away) it is +3.0..+3.1 dB over them.

**Fix:** `build/roles.json` Timpani. The solo opening (bar 1) stays as it is.
- Replace `[0, 16, 12]` with `[0, 12, 12]` and `[12, 16, 9, 1]`.

**Expected:** bar 4 at about 0 dB against the strings. Master bar 4 -0.6 dB, which matters little after the delivery ride.

## Do not touch

- The c12 timpani CC1 map with `TIMP_ROLL_TRIM_DB`.
- The c11 trumpet f/ff trims, which make the trumpets equal the trombones at f.
- The percussion gains, patches and timing (tam-tam fff, crash, sus. cymbal crescendo, tam-tam pp).
- The second-theme `HP_TARGET_AT` rows, shapes and fills.
- The bars 23-25 / 135-137 roles.
- The c12 final-chord `LEVEL_SHAPES` on the celli and basses.
- `_REBOW_FROZEN` and `rebow_fills.json`.
- `accent_fits.json`.
- The climax order (160 > 122 > 169).
- `FAST_CAP_ABOVE` 4 with the top ride 1.6.
- `UNI_BY_DYN`.
- The soft trims of the woodwinds, horns, trombones and upper strings: p and pp match across families within about 3 dB.

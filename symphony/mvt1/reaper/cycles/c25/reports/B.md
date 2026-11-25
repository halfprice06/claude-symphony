# Cycle 25, critic B: balance and levels (render c24)

## Method

All numbers come from `cycles/c24/render/` (33 stems and the master; no stem fix after this render) and `build/parts.json`, which is identical to `cycles/c24/rendered_build/parts.json` (same tempo map). I computed envelopes per 10 ms frame (stereo power, 4096-point STFT): K-weighted, A-weighted, and eight bands (30-60, 60-100, 100-300, 300-1k, 1-2k, 2-5k, 5-10k, 10-20k Hz).

- "re M" means a stem minus the master over the same window.
- Note levels are measured from the score onset + 80 ms to min(note end, + 1.5 s).
- Printed dynamics come from each track's `dyn_curve`.
- I checked score pages 2, 6, 8-11 and 13-18 against the data.

Scratch scripts were kept in `/private/tmp/claude-501/mockup-loop/mvt1-c25-B/` and deleted afterwards: `env.py`, `notes.py`, `ladder.py`, `bartop.py`, `beats.py`, `groups.py`, `pairs.py`, `doub.py`, `chords.py`, `hot.py`, `acc.py`, `loop.py`, `lowend.py`, `simbt.py`.

## What holds (measured)

**Family ladders.** These are medians of note bodies (K, in dB):

| Family | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| Winds | -45.0 | -41.3 | -41.3 | -39.1 | -36.8 | -32.2 | -26.6 |
| Brass | -45.6 | -43.1 | -39.6 | -36.9 | -33.1 | -27.1 | -22.9 |
| Strings | -46.6 | -41.6 | -39.9 | -37.1 | -33.7 | -29.1 | -22.5 |

- p sounds like p across the families (spread 1.8 dB).
- At f and ff, one string section sits 3.1 dB over one woodwind, as in Rimsky-Korsakov.

**Trumpets.**
- Pairs at the same dynamic (K): Trumpet 1 over Trumpet 2 by +0.9..+2.4; Trumpet 2 against Trumpet 3 -0.3..-1.0.
- The a2 theme at 167-170 is the top stem, 3 dB over the Horns a2.

**Percussion.**
- Tam-tam 484 fff: -8.8 K re M over 0.3-1.5 s. Tam-tam 696 pp: -10..-16 re M.
- Crash 636: 2-5 kHz -9.3, 5-10 kHz -3.5, 10-20 kHz -0.4 re M at the hit.
- The suspended-cymbal roll grows from inaudible at 632-634 (printed pp under a ff tutti) to -2.4 re M at 5-10 kHz at 635.75.

**Timpani.**
- No roll is the top stem.
- The bars 80-81 roll at -7.7..-9.2 K re M is printed f < under p strings.

**Dan's checks.**
- *Loop pulsing.* Only 11 unsplit notes of 6 s or more remain, all winds and brass.
  - Highest 100-300 Hz autocorrelation at 3.95 s: Bass clarinet 480 (0.66, at -17 re M) and 464 (0.54/0.52 centroid, at -13).
  - Horn 4 at 289 (bars 73-76 pp): 0.48/0.56, but its level stays within ±2 dB of a slow decay at -9.8 re M.
  - No action.
- *Accents*, 2-5 kHz over the first 80 ms minus the body:
  - brass median -4.6, 3 of 168 over +3;
  - winds -2.4, 11 of 232;
  - strings -1.0, 11 of 193.
  - Violas 536 (+16.1) is known and belongs to A's lens.

## 1. The bass trombone is the loudest low-brass voice in every loud tutti. Its f/ff/fff trims are 5 dB above Trombone 1 (measured; fix simulated)

**Where.** Every f-fff tutti. The worst places:

| Bars | Situation |
|---|---|
| 97 (letter F downbeat) | Whole-note ff bass; the top stem |
| 143 | Marcato ff chord; the top stem |
| 72-73, 133-134, 160-161 | Third in the bar |
| 30 | Second |
| 169-170 | Over Violins I |

**Evidence (measured):**
- `build/mix.json` Bass trombone `dyn_trim_db`:

  | Track | f | ff | fff |
  |---|---|---|---|
  | Bass trombone | +3.9 | +6.3 | +4.7 |
  | Trombone 1 | -0.9 | +0.8 | -0.6 |
  | Trombone 2 | +1.9 | +3.3 | +1.9 |
  | Tuba | -1.4 | -2.8 | -1.6 |

  On top of this the bass trombone gets a +4 dB 140 Hz `loud_eq` bell. These values come from movement II's mix (Bass trombone f/ff 6/8), cut once by 2 dB in c09-c12. The c01 cut that lowered Trombone 1/2 never reached the bass trombone.
- In the loudest 15% of master frames the bass trombone carries 6.6% of the A-weighted energy: 5th of 33 stems, after Violins I/II, Trombone 1 and Trumpet 1. Trombone 2 has 4.2% and Tuba 3.2%. Its 2-5 kHz and 5-10 kHz shares (5.9%, 5.1%) equal Trombone 1's, so it sounds as bright as the first trombone.
- A-weighted pairs at the same printed dynamic:
  - Trombone 2 minus bass trombone: f +1.1, ff -0.5, fff -0.8.
  - Bass trombone minus Tuba: +4.8, +3.3, +2.9.
- Rank among the stems in loud bars: in the top 3 in 12 of 53 bars and the top 5 in 23, the same as Trombone 1 (12/26), which carries tunes. The tuba is in the top 3 in 0 bars.
- Bar 97: the bass trombone's ff whole note sits at -5.2 A re M (-4.4 on beat 3), 4-5 dB over the other held bass voices (celli -6.9, basses -14.3, bass clarinet -16 on beats 2-3) and 8.5 dB over Violins I.
- Bars 133-134: the bass trombone's whole notes (-10.6/-11.0 re M) are level with Trombone 1's theme (-10.3; printed f).
- Bars 160-161: -10.3/-11.2 re M, against Violins I at -9.5/-10.2 on the fff tune.
- Adler and Rimsky-Korsakov treat the bass trombone in tutti as the foundation under the tenor trombones, not a voice equal to the first trombone (inferred).

**Fix.** `build/mix.json`, `tracks["Bass trombone"]["dyn_trim_db"]` = `{"f": 1.4, "ff": 3.3, "fff": 2.2}` (-2.5/-3/-2.5). Keep the 140 Hz loud_eq bell and the soft trims.

This is level only, so a stem fix or `--mix-only` is enough. Simulated on the c24 sample stream (master minus (1-g) times the stem, g from the printed-dynamic curve):

| Place | Bass trombone re M (A) | Bass trombone - Violins I | Master |
|---|---|---|---|
| Bar 97 | -5.2 -> -7.5 (second, not first) | | -0.70 dB |
| Bar 143 beat 1 | -9.0 -> -11.8 (4th) | | -0.28 dB |
| 133-134 | -10.8 -> -13.6, under Trombone 1's theme | | |
| 160-161 | | -0.9 -> -3.4 | -0.16 dB |
| 169-170 | | -0.1 -> -3.1 | |
| 72-73 | | +1.3 -> -1.2 | |

- The master falls 0.1-0.2 dB at the other climaxes. Plain RMS: 160 -10.14 -> -10.24, 122 -10.98 -> -11.07, 167-170 -17.71 -> -17.86, bar 26 -14.96 -> -15.02.
- The climax order is unchanged.
- The master sample peak goes 1.488 -> 1.432, so the delivery limiter takes slightly less.

## 2. Letter K (bar 158, qn 628): Violins I has no attack on its ff down-bow G5, so the melody's first beat sits 7-9 dB under Violins II (measured)

**Where.** qn 627.5-628.75, score p. 16, the start of the recapitulation climax: tutti ff, down-bow printed on both violin parts.

**Evidence (measured):**
- In parts.json Violins I has one note G5 at 627.5 lasting 1.2 qn and no note at 628.
  - The slurred G5 eighth at 627.5 and the printed down-bow G5 quarter at 628 were merged by the slurred same-pitch merge (`SLUR_REP_MERGE_SUS`, a CC11 notch only).
- Violins II has a different pitch before its 628 (G4 to G5). It is listed in `DOWNBOW_STROKE_AT` (c06) and plays a fresh Sus MAX stroke at velocity 105.
- A re M per 0.25 qn, 628.0-628.75:

  | | 628.0 | 628.25 | 628.5 | 628.75 |
  |---|---|---|---|---|
  | Violins I | -11.0 | -13.7 | -11.5 | -11.8 |
  | Violins II | -4.1 | -4.8 | -4.6 | -8.3 |

  - From 629 the two parts are level (-10.0 / -11.7), in unison on E6.
  - Violins I falls 4 dB from its pickup (627.75: -6.8) into the downbeat while the master rises 3.5 dB.
  - The Violins II stroke is +9.2 dB over its own ff median, the hottest string note in the hot-note scan.
- The roles add to the gap: Violins I `[628, 644, -0.5]` and Violins II `[628, 644, 2.5]` in `build/roles.json`.

**Fix:**
- `build/score_config.py`: `DOWNBOW_STROKE_AT["Violins I"]` += `[628.0]`.
  - The stroke is assigned before the slur-repeat merge (`score_to_parts.py` lines 1721 / 1909), so the merge's `_lg(next art)` test then fails and 628 becomes a fresh Sus MAX stroke, as on Violins II.
  - Rebuild Violins I MIDI.
- Then lower the Violins II stroke front: `LEVEL_SHAPES_S["Violins II"]` += `[(628.0, [(-0.02, 0.0), (0.03, -2.5), (0.35, -2.5), (0.6, 0.0)])]`.
- Expected (inferred from Violins II's stroke at the same velocity and the 3 dB role difference): Violins I at about -7 A re M on the downbeat, about level with Violins II.

## 3. Recapitulation bars 136-139: Oboe 1 and Flute 1 sit over the Violins I theme they double, unlike the exposition twin (measured)

**Where.**
- qn 542-548 (bars 136-137): Oboe 1 in unison with Violins I, mf cresc.
- qn 552.5-557.3 (bar 139): Flute 1 an octave above Violins I, f cresc. Score pp. 13-14.

**Evidence** (A, the wind note minus the Violins I note on the same onset):

| | Range | Median |
|---|---|---|
| Exposition twin, Oboe 1, qn 89-99 (bars 23-25, same pitches) | -2.4..+0.8 | -0.5 |
| Recapitulation, Oboe 1, 542-547 | +1.1, +1.3, +3.4, +2.7, +1.5, +1.9 | +1.7 |
| Recapitulation, Flute 1, 552.5-557 | +7.1, +4.1, +0.6, +0.3, +4.6, +2.3, +2.2, +3.6 | +2.9 |

- Bar 137: Oboe 1 is the top stem (-5.2 A re M, Violins I -6.7).
- Bar 139: Flute 1 is the top stem (-7.6, Violins I -9.9).
- Flute 1's 552.5-556.5 notes are 8-12 dB over its own f/ff medians.
- The 552.5 pickup carries `PICKUP_LIFT["Flute 1"][552.5] = 8.0` dB. The exposition twin 104.5 has 3.2.
- In forte a string section should sit about +3 dB over one woodwind (Rimsky-Korsakov). Here the theme turns into a wind line exactly where the exposition kept it in the violins (inferred).

**Fix (level only, stem fix possible):**
- `PICKUP_LIFT["Flute 1"][552.5]`: 8.0 -> 4.0.
- `LEVEL_SHAPES["Flute 1"]` += `[[(552.85, 0.0), (553.0, -3.0), (557.2, -3.0), (557.45, 0.0)]]`.
- `LEVEL_SHAPES["Oboe 1"]` += `[[(541.7, 0.0), (541.95, -2.5), (547.8, -2.5), (548.1, 0.0)]]`.
- Expected: Oboe 1 minus Violins I about -1.4..+0.9 (the exposition's range); Flute 1 about -2.7..+1.1 after the pickup; 136-139 master about -0.3 dB.
- Leave the 536-548 roles (+1.5/+2/+2.5) as they are, so the 536-541 notes are not lowered.

## 4. ff horn chords are top-heavy: Horn 4 sits 8-11 dB under Horn 1 inside one chord (measured)

**Where.** Four-horn ff chords at qn 112-122 (bars 29-31), 460 (bar 116), 556-562 (bars 140-141), 100 and 328-330.

**Evidence:**
- K, each horn minus the mean of the four, on common onsets of 1 qn or longer:

  | Dynamic | Horn 1 | Horn 2 | Horn 3 | Horn 4 | Chords |
  |---|---|---|---|---|---|
  | ff (median) | +2.9 | +1.1 | -0.9 | -2.35 | 21 |
  | f (median) | +0.6 | +0.45 | -0.3 | -1.9 | |

- Worst chords:

  | qn | Horn 1 | Horn 4 |
  |---|---|---|
  | 120 | +4.4 | -5.9 |
  | 122 | +4.6 | -6.1 |
  | 460 | +5.4 | -3.4 |
  | 556 | +4.8 | -4.8 |
  | 560 | +4.5 | -5.0 |

  Horn 1 to Horn 4 is 8.2-10.7 dB.
- In the brass-chord spread scan, Horn 4 is 5 dB or more under the chord median in 9 of 72 chords; no other brass voice is under that often.
- All four horns use the same 1FH KS Master. The ff level rises with pitch: A♭4/G4 -26.9/-25.5, F3-A♭3 -31..-31.7. Horn 4's low chord tones get no correction.
- Horn 4 `dyn_trim_db` is f 1.0, ff 1.5, fff 0.5.

**Fix.** `build/mix.json` Horn 4 `dyn_trim_db` -> `{"f": 2.5, "ff": 4.0, "fff": 2.0}`.
- Horn 4 is exposed only in soft passages (roles -4 at 248-268 / 504-520 stay).
- Expected (inferred, level only): spread on the worst ff chords 8.2-10.7 -> about 5.7-8.2 dB. Master change under 0.1 dB.

## Do not touch

- The family ladders, soft trims and the f/ff string-over-wind ratio.
- The trumpet trims and roles (pairs within 2.4 dB; the a2 theme at 167-170 on top).
- The percussion patches, gains and timing: tam-tam, crash, suspended-cymbal lead.
- `TIMP_CC1_MAP` and the tutti roll shapes.
- The Bass trombone 140 Hz `loud_eq` bell and soft trims (finding 1 changes only `dyn_trim_db`).
- The c24 bar-26, bar-84, Oboe 178-182 and second-theme shapes.
- The climax order 160 > 122 > 167-170 > bar 26 (none of the fixes reorders it).

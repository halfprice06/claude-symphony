# Cycle 11, critic B: balance and levels (render c10)

## Method

All numbers are from the stem-fixed c10 render (`cycles/c10/render/`), on the tempo map in `build/parts.json`. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c11-B/`.

- Levels are K-weighted power in 10 ms hops, mean of L and R (`env.py`, `lib.py`). Only differences are used.
- "re master" means the stem level minus the master level over the same window.
- A note body runs from onset +0.08 s to the note end or onset +1.5 s, whichever comes first. The printed dynamic is read from each track's `dyn_curve`.
- `ctx.py` compares each stem with the median of all stems at the same printed dynamic in the same 1 qn window.
- `solo.py` gives a melody's margin: its loudest stem minus the loudest other sounding stem, per 1 qn window. `top.py` counts the beats where each stem is the loudest. `tab.py` lists the stems per window.
- Fixes were simulated on the envelopes (`esim.py`, `sim11.py`, `solo_lib.py`): the planned dB change is applied to the stem and the master is re-summed.
- Scores were read from `score.pdf` pages 1-17 and `build/mockup-events.tsv`.

## What holds (measured)

**Dynamic mapping by family.** Stem minus the median of the same-dynamic stems in the same window:

| Group | p | f | ff |
|---|---|---|---|
| Single woodwinds | -1.5..+0.3 | -0.4..-3.7 (second players lowest) | |
| Horns 1-3 | | -1.7..+1.0 | |
| Trombones and bass trombone | | +1.6..+2.2 | +2.5..+3.4 |
| Violas | -0.3 | +0.6 | |
| Violins II | | +2.0 | +3.1 |

- Violins I sit at +3.6..+6.6, mostly because they carry the tune. The basses read -1.3..-3.3, which is the K-weighting's low-frequency penalty.
- Timpani: f +0.5, ff 0.0. Rolls: pp -6.2, p -2.2. These are under the texture, as brief rule 5 asks.
- Every c10 balance fix landed in the render:
  - Violas in bars 97-102 and 117-121: -14..-19 dB re master.
  - Flute 1 solos: bars 73-75 margin +2.6 dB, bars 109-110 +1.8 dB.
  - Climax 158-161: Violins I/II are the top stems, brass -10..-14 dB re master.

**Percussion.**
- Crash at qn 636: -12.7 dB re master. Its 4-12 kHz ring is 49% of the master's 5-20 kHz band.
- Suspended cymbal: inaudible until qn 634, then grows into the crash.
- Tam-tam fff at qn 484: -9.7 dB re master. It is the top stem for 2 beats, then rings at -12..-16 to the damp.
- Tam-tam pp at qn 696: 4th stem, -9.1 dB re master.

**Low end.** In the loudest 10% of frames, 60-100 Hz is -13.3 dB re 300-1000 Hz; the band shares are within the lossless references. No change is proposed.

## 1. Bar 124: the bar-122 brass lift and string cut run on into the decrescendo bar and bury the flute, oboe and violin line by 6-10 dB (measured)

**Where:** qn 492-496, bar 124.
- Fl1, Ob1 and V1 ("loco") hold a unison G5, decrescendo, into the descending answer of bar 125.
- Trombones a2 and bass trombone hold G3/G2, also decrescendo.

**What is wrong (measured):** The roles written for the fff chord of bars 122-123 do not end at bar 124:
- Trombone 1/2 `[484, 496, 2.5, 2]`
- Bass trombone, tuba and trumpets `[484, 496, 2, 2]`
- Violins I `[484, 496, -4]`
- Flute 1 `[484, 494, -3]`

So through bar 124 the brass are lifted 2-2.5 dB and the melody is cut 3-4 dB.

Stems re master at qn 492 / 493 / 494 / 495:

| Stem | 492 | 493 | 494 | 495 |
|---|---|---|---|---|
| Trombone 1 | -8.2 | -5.8 | -5.1 | -4.6 |
| Bass trombone | -7.0 | -6.4 | -5.3 | -4.8 |
| Violins I | -12.7 | -14.0 | -17.5 | -18.5 |
| Oboe 1 | -14.6 | -14.3 | -13.8 | -14.6 |
| Flute 1 | -14.6 | -19.9 | -16.5 | -14.4 |

- The best melody stem is 5.7 / 8.3 / 8.8 / 9.8 dB under the loudest accompaniment.
- Trombone 1 falls only 1.4 dB across its printed decrescendo, while the master falls 3.5 dB.

**Fix:**
- `build/roles.json`:
  - Trombone 1 and Trombone 2: `[484, 492.5, 2.5, 1]`.
  - Bass trombone, Tuba, Trumpet 1-3: `[484, 492.5, 2, 1]`.
  - Violins I: `[484, 492, -4]`.
  - Flute 1: `[484, 492, -3]`.
  - Keep Violins II `[484, 496, -4]`: its bar-124 part is the div. chord.
- `build/score_config.py`, `LEVEL_SHAPES` for Trombone 1, Trombone 2 and Bass trombone: `[(492.0, 0), (493.0, -3), (495.0, -7), (496.0, -7), (496.3, 0)]`.
- This is level only, so it can be a stem fix.

**Simulated:**
- Melody minus loudest accompaniment at 492-495: -5.7/-8.3/-8.8/-9.8 -> +0.4/+2.1/-1.1/-2.1 dB.
- Master: -0.1 dB at qn 491, -0.75..-3.4 dB inside bar 124. Bar 124 now falls as printed (fff to the p of bar 126).
- Bars 122-123 (the climax and `ARRIVAL_WEIGHT_AT` 484) are unchanged within 0.1 dB.

## 2. Celli accompaniment plays at the melody's level in the f/ff Allegro passages (measured)

**Where:** bars 23-26 (qn 88-104), 91-102 (qn 360-408) and 135-138 (qn 536-552).

**What is wrong (measured):**
- At f and ff the celli stand +3.3 dB over the median of the same-dynamic stems. Violas are at +0.6, Violins II at +2.0.
- Celli are the loudest stem in 185 beats, second only to Violins I (245).
- In these passages the celli play bass and supporting long notes:
  - accented dotted halves in bars 23-25 and 135-137;
  - slurred long notes in bars 91-93;
  - ff whole notes in bars 97-102.
- The tune is in V1 + Fl1 + Ob1 (bars 23-26 and 135-138), in CA + V2 + Va (bars 91-93), and in Fl/Ob/CA/V1/V2 (bars 98-102).

Melody margin over the loudest accompaniment stem (median), with the celli as the top accompaniment:

| Bars | Margin | Celli top in |
|---|---|---|
| 23-26 | -2.9 dB | 7 of 15 windows |
| 91-93 | -2.3 dB | 9 of 12 |
| 94-96 | -0.2 dB | 6 of 12 |
| 98-102 | +0.1 dB | 18 of 20 |
| 135-138 | -1.2 dB | 11 of 15 |

- In bars 98-102 the celli whole notes (B1-E2, 42-52) sit at -5.7..-8.4 dB re master, beside Violins I at -6.3..-7.9.
- Movement II's c21 lesson applies here: old cuts went stale as other tracks rose. The celli already carry -3 dB cuts at qn 56-72 and 104-128, but not in these spans.

**Fix:** `build/roles.json`, Violoncellos:
- Add `[88, 104, -3]` (it chains into the existing `[104, 128, -3]`).
- Add `[360, 408, -3]` (after the celli's own lifts, which end at 358).
- Add `[536, 552, -3]`.
- Optional, bars 23-25: Violas `[88, 99.5, -2.5]`, Violins II `[88, 99.5, -2]`. These are the mf accompaniment quarters, the top stems at qn 88.

**Simulated (celli only):**

| Bars | Margin before -> after | Covered windows | Master |
|---|---|---|---|
| 23-26 | -2.9 -> -1.1 dB | | -0.33 dB |
| 91-93 | -2.3 -> -1.0 dB | | -0.77 dB |
| 94-96 | -0.2 -> +0.7 dB | | -0.41 dB |
| 98-102 | +0.1 -> +3.1 dB | 8/20 -> 1/20 | -0.40 dB |
| 135-138 | -1.2 -> +0.5 dB | 12/15 -> 5/15 | -0.34 dB |

With the optional violas/V2 rows, bars 23-25 go -3.1 -> -0.2 dB (master -1.07 dB inside the crescendo to bar 27; bar 27's ff is untouched).

## 3. Horn 4's low notes (C3-F3) play at their f level at p and mp, and stick out of soft chords (measured)

**Where:** Horn 4, MIDI 48-53.

**What is wrong (measured):** Horn 4 note-body medians:

| Printed dynamic | C3-F3 (48-53) | F#3-C4 (54-62) |
|---|---|---|
| p | -37.1 (n8) | -47.5 (n9) |
| mp | -38.9 (n6) | -45.4 (n7) |
| mf | -36.2 | -40.1 |
| f | -36.9 | -35.5 |

- At f the two registers match; at p the low notes are 10.4 dB hot. Horn 3 at p measures -41..-45.
- Same chord, same printed p (qn 652): Horn 4 D3 -38.0 dB, Horn 2 C4 -47.6 dB.
- Where Horn 4 is the top or second stem of a soft chord:
  - bars 19-21 (p, -8..-11 re master, beside the V1 tune);
  - bar 105, qn 416: mp, top at -6.9, over Horn 1's mf line;
  - bars 163-164, qn 651-652: p, top at -5.3 / -7.4, over Oboe 1's f phrase.
- The existing trims at 224 (-4) and 240 (-5) leave those notes at -41.6 and -35.8 dB.

**Fix:** `build/note_trims.json`, Horn 4. Use a 0.1 s ramp (`NOTE_TRIM_RAMP_S["Horn 4"]` for these onsets).
- -7 dB at 40.0, 72.0, 76.0, 80.0, 440.0, 620.0, 652.0
- -5 dB at 88.0, 412.0, 415.0, 416.0, 418.0, 660.0
- -3 dB at 152.0, 624.0, 648.0
- 224.0: -4 -> -8; 240.0: -5 -> -9
- Do not trim f/ff notes.

**Simulated:**
- Horn 4 re master: bars 19-21 -10.8 -> -16.2 dB (rank 4 -> 8); bar 105 -10.0 -> -13.6 (rank 4 -> 8); bars 162-165 -10.7 -> -14.5 (rank 5 -> 11).
- Low p notes land at about -44 dB, between Horn 3 p and Horn 4's own G3-B♭3.
- Master -0.07..-0.35 dB in those spans.

## 4. Trumpets sit 2.5-4 dB under the trombones, and at f under the horns (measured; reference Rimsky-Korsakov)

**Reference:** Rimsky-Korsakov, Principles, "Comparison of resonance": in loud passages Trumpet = Trombone = Tuba = 2 Horns.

**What is wrong (measured):** Same onsets, same printed dynamic, note bodies:

| Pair | f | ff | fff |
|---|---|---|---|
| Trumpet 1 - Trombone 1 | -3.8 (n14) | -3.5 (n7) | -0.3 |
| Trumpet 2 - Trombone 2 | -2.6 | -2.4 | -4.0 |
| Trumpet 1 - Horn 1 (target about +3) | -0.9 (n13) | +2.2 | |
| Trombone 1 - Horn 1 | +0.4 | +3.0 | |

- Within the section at ff, Trumpet 2/3 are 1.4/2.7 dB under Trumpet 1.
- Bars 69-71 (qn 272-284): Trumpets 1-2 double the f closing tune with Fl/Ob/V1. They sit -14.2/-13.3 dB re master, under the horns' a2 counter-line (Horn 1 -6.1..-13). The tune's margin is -1.5 dB, covered 7 of 12.
- The trumpets' 2-5 kHz accent attack is fine: first 80 ms minus body, median -3.7/-10.1/-10.8 dB.

**Fix:** `build/mix.json` `dyn_trim_db` (fff unchanged; the climaxes and limiter peaks are not touched):
- Trumpet 1: f 3.6 -> 6.1.
- Trumpet 2: f 3.7 -> 6.2, ff 9.0 -> 10.5.
- Trumpet 3: f 5.2 -> 7.7, ff 10.6 -> 12.1.

**Simulated:**
- Tune margin in bars 69-71: -1.5 -> -0.4 dB. Trumpet 2 becomes the 4th stem there.
- Bars 131-134: Trumpet 1 -15.7 -> -13.3 dB re master.
- Master +0.08..+0.28 dB in the f/ff tutti spans, +0.01 dB at 158-162.
- Bars 167-170 are unchanged; Trumpet 1 is already the top stem there, under its -4 role.

## 5. Bars 13-14: Horn 1's mp solo is covered by the violins' and flute's held G5, which barely decrescendos (measured)

**Where:** qn 48-56.
- Violins I hold G5 (whole note) and Flute 1 G5 (half) from the f of bar 12, with untargeted decrescendos.
- Horn 1 enters "1." mp at qn 49 (E♭3-C4, then B3 p in bar 14) over V2 p > pp.

**What is wrong (measured):**
- The horn's margin is -4.2 dB (6 of 6 windows covered).
- Violins I sit -5.0/-4.6/-2.7 dB re master at qn 49/50/51; Horn 1 sits at -8.4/-6.1/-8.6.
- The violins' decrescendo falls only about 2.3 dB across bar 13.
- In bar 14 the Violins II pp chord (-3.2..-6.1 re master) covers Horn 1's p B3 (-8.1..-13.9).

**Fix:** `build/score_config.py` `LEVEL_SHAPES`:
- Violins I: `[(48.0, 0), (49.0, -2), (50.0, -4.5), (51.5, -6), (52.2, -6), (52.5, 0)]`.
- Flute 1: `[(48.0, 0), (49.0, -2), (50.0, -4.5), (50.6, -4.5), (51.0, 0)]`.
- `build/roles.json` Violins II: `[52, 56, -3]`.

**Simulated:**
- Horn margin -4.2 -> -0.1 dB (covered 6/6 -> 3/6): bar 13 -3.4 -> 0.0, bar 14 -5.0 -> -2.0.
- Master bar 13 -0.9 dB, bar 14 -1.1 dB. This is the printed decrescendo into the pp bar; the delivery ride is at its cap there.

## Dan's two checks (measured)

**Loop pulse on held notes.** 14 notes are longer than 6 s. Highest autocorrelations at 3.95 s:

| Note | 100-300 Hz | Centroid | Stem re master |
|---|---|---|---|
| Bass clarinet, qn 480 | 0.60 | | -19 dB |
| Horn 4, qn 289 (G#3) | | 0.57 | -11 dB |
| Bass clarinet, qn 464 | 0.40 | 0.47 | |

- The master over qn 464-500 and 696-728 reads -0.25/-0.25 (band) and +0.03/-0.07 (centroid): no pulse in the mix.
- None of the findings lengthens a note. The Horn 4 trims leave the qn 289 note alone (pitch 56).

**Accent attacks.** 2-5 kHz, mean of the first 80 ms minus the body at +0.15..+0.45 s:
- Brass medians: Horn 1-3 -2.8..0.0, Horn 4 -8.5, trumpets -3.7..-10.8, trombones and tuba -6.3..-12.4 dB.
- Known outliers: Horn 3 qn 91 +14.1, Horn 2 qn 665 +9.9 (the pickup's brightness).
- Finding 4 lifts the trumpets' attack and body together, so the ratio is unchanged. Their 2-5 kHz rises about 2.5 dB against the other sections on f accents only (Trumpet 1 max +3.3 dB at qn 284).
- The other findings lower levels only.

## Do not touch

- The c10 viola rows (bars 97-102 and 117-121).
- The flute and bass clarinet roles and the double-bass A♭1 trim from c10.
- The timpani shapes at 245.5-249.5 and 316.3-324.
- `UNI_BY_DYN`.
- The climax 158-161 balance (V1/V2 on top, brass -10..-14 dB re master) and the climax order (160 > 122 > 169).
- The 484 roles before qn 492 and `ARRIVAL_WEIGHT_AT`.
- The percussion levels, patches and timing.
- The brass, clarinet and contrabassoon per-dynamic trims except the trumpet values in finding 4.
- `accent_fits.json`. Refit it after findings 1, 3 and 4, because they change levels around accented brass notes.

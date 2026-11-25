# Cycle 19, critic B: balance and levels (render c18)

## Method

All numbers come from the stem-fixed c18 render (`cycles/c18/render/`, 33 stems) and the build that matches it (`build/parts.json` 22:38, `mix.json`, `roles.json`, `score_config.py`).

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c19-B/`:
- Re-run on c18: the c18-B set (`env.py`, `fam.py`, `near.py`, `rank.py`, `aw.py`, `margA.py`, `loopchk.py`, `accents.py`).
- New:
  - `oncov.py`: melody minus the loudest other stem, A-weighted, over the first 0.3 s of every melody onset.
  - `pairdyn.py`: pairwise stem differences by printed dynamic.
  - `brtop.py`: half-beats where a brass, timpani or percussion stem stands 1.5 dB or more over every other stem.
  - `secspread.py`, `nearsoft.py`, `lowtb.py`, `lowsec.py`, `lowcel.py`.
  - Simulations: `esim2.py`, `sim_lg3.py`, `sim_fug.py`, `sim_bn.py`, `sim_122.py`.

Definitions:
- "A" is an A-weighting applied to the eight band envelopes. "K" is K-weighted power.
- "re master" means stem minus master over the same window.
- The simulations scale the stem band envelopes by the proposed dB curve and add the change to the master power. This is an incoherent-sum approximation, accurate to a few tenths of a dB on these windows.

Melody and accompaniment were assigned from the score pages (pp. 2-18 at 90 dpi) and `mockup-events.tsv`.

## What holds (measured)

**Family ladders** (K, median note bodies):

| Family | pp | p | mf | f | ff | fff |
|---|---|---|---|---|---|---|
| Winds | -45.6 | -41.4 | -38.6 | -36.2 | -32.3 | -26.7 |
| Brass | -46.2 | -43.9 | -37.1 | -33.3 | -28.0 | -23.3 |
| Strings | -47.1 | -42.3 | -37.2 | -33.4 | -27.4 | -23.4 |

- p sounds like p in all three families, within 2.5 dB.
- Pitch-matched mf -> f steps:
  - Winds +1.7..+3.0 dB.
  - Violins and violas +4.1..+6.8 dB.
  - Brass +3.7..+7.7 dB.
- Section ratios follow Rimsky-Korsakov (*Principles* p. 23: in forte, two horns equal one trumpet or one trombone), A-weighted:
  - Trombone 1 minus Horn 1: +2.3 dB at f.
  - Trumpet 1 minus Trombone 1: +0.1 at f, +1.5 at ff.
  - Trumpets a2 minus Horns a2 in the coda theme (bars 167-170): +3.8.
  - Trumpet 2 and Trumpet 3 minus Trumpet 1: -1.3..-3.5 at every loud dynamic.
- Tutti melody margins (onset measure, A):
  - Bars 98-102: covered 0 of 16, median +4.1.
  - Bars 139-143: covered 1 of 20, median +3.2.
  - Bars 167-170: median +3.1.
  - Second theme, recapitulation (bars 147-155): the Horn 1 + violas + celli tune is on top at every beat.
- Timpani: never within 7 dB of the master except the bar-1 solo roll and two ff strokes (bars 80, 132).
- Loudest stems:
  - Tam-tam fff (qn 484): the loudest stem for about 3 s, over a held chord.
  - Crash (636): 5-20 kHz lift as in c18.
- Low end: the loud windows' 100-160 / 160-300 Hz shares are -12.4 / -8.9 dB against -3.4 at 300 Hz-1 kHz. Nothing points to boom from the celli's loud EQ.
- Dan's checks:
  - Loop pulsing: the same 8 unsplit notes of 6 s or more as in c17. The worst is Bass clarinet 11 (100-300 Hz autocorrelation 0.81, under printed hairpins). Master windows are 0.04 or less, except 160-176 (+0.44, the printed decrescendo).
  - Accents, 2-5 kHz in the first 80 ms minus the body:

    | Family | Median | Over +3 dB |
    |---|---|---|
    | Brass | -7.1 | 3 of 133 |
    | Winds | -5.9 | 8 of 220 |
    | Strings | -3.1 | 7 of 186 |

    These are the same cases as c17. The worst is Violas 536 at +16 dB (the bar-134/135 release spot, which is A's lens).

## 1. Letter G, bars 117-120: the bass trombone carries the +3/+4 dB "held parts" lift while it plays the moving countermelody, and covers the ff theme (measured; fix simulated)

**Where.** qn 464-480 (p. 10, letter G).

**Score.**
- The theme is ff in Flute 1, Oboe 1, Violins I and Violins II (unis.).
- The countermelody is ff in long notes, E-flat4 - D4 - C-sharp4 - C4 from 468. It is played by Trombones 1-2 a2 (the Trombone 1 track), Horns a2 and Bassoon 1. The Bass trombone doubles it an octave lower, on its own.
- Horn 3/4, Tuba, Contrabassoon, Bassoon 2 and Bass clarinet hold pedals.

**Evidence.**
- `score_config.py` `_lg_c18` (+3 dB from 464.05, +4 over 468.6-483.5) is applied to ten tracks as "held ff parts". Bass trombone is one of them, but from 468 it moves with the countermelody. Trombone 1, which carries the same line in the upper octave with two players, is not lifted.
- A-weighted, 468-480 re master:

  | Stem | dB |
  |---|---|
  | Bass trombone | -8.2 |
  | Violins I | -8.2 |
  | Violins II | -9.6 |
  | Trombone 1 (a2) | -10.0 |
  | Horns a2 | -10.4 |

  Over 464-480: Bass trombone -7.9, Violins I -8.7, Trombone 1 -10.8.
- A single bass trombone stands 2.9 dB over two tenor trombones on the same line an octave above. By Rimsky-Korsakov's ratios it should sit about 3 dB under them, so the excess is about 6 dB.
- Bass trombone minus Trombone 1 elsewhere at ff/fff: -2.2..+1.9 per 4-bar group. At letter G it is +2.9, the largest in the movement (`lowtb.py`).
- Theme onsets (Violins I onsets, theme stems against the loudest other stem, first 0.3 s, A):
  - median -0.5 dB; covered 14 of 21; under -3 dB on 7; worst -11.2.
  - The covering stem is the Bass trombone on 10 of the 14, Horn 3 on 3.
  - For comparison, the same measure gives 0 of 16 covered at bars 98-102 and 1 of 20 at bars 139-143.
- In bar 117 itself (464.2-467.8) the Bass trombone's held G2 with the +3 lift is the loudest stem: -7.4 against Violins I -10.2.

**Fix.** Level only, so `stem_fix.py` can apply it.
- In `build/score_config.py`, take "Bass trombone" out of the `_lg_c18` loop and give it its own shape that keeps only the crescendo part:

  `[(463.9, 0.0), (479.2, 0.0), (479.6, 4.0), (483.5, 4.0), (484.0, 0.0)]`

  This is equal to -3 dB over 464.05-467.6 and -4 dB over 468.6-479.2 against c18.
- Add `LEVEL_SHAPES` on Violins I, Flute 1 and Oboe 1: `[(463.9, 0.0), (464.2, 2.5), (483.5, 2.5), (484.0, 0.0)]`.
  - This rises with the theme's first pickup and ends where `_lg_c18` ends, so the bar-121 crescendo does not lose level at 480 (the c16 C #1 lesson).
- Leave the hold on the other nine tracks as it is.

**Simulated** (`sim_lg3.py`, variant B):
- Theme onsets: median -0.5 -> +2.0 dB; covered 14 -> 7 of 21; worst -11.2 -> -7.2. The remaining coverers are Horn 3 (4), Tuba (2) and Bassoon 1 (1), mostly on the theme's weak pickup eighths.
- 468-480 A re master: Violins I -5.9, Violins II -9.8, Trombone 1 -10.2, Horns a2 -10.6, Horn 3 -10.8, Bass trombone about -12.
- Master K per bar:

  | Bar | 116 | 117 | 118 | 119 | 120 | 121 |
  |---|---|---|---|---|---|---|
  | c18 | -15.1 | -14.0 | -15.3 | -16.3 | -15.4 | -14.0 |
  | Fix | -15.1 | -14.0 | -15.2 | -16.1 | -15.2 | -13.5 |

  The c18 C #1 results hold within 0.2 dB: bar 117 over 116, and bar 119 2.0 under 117. Bar 121 rises 0.5 dB; bar 122 stays 3.5 dB over it.
- An extra Horn 3 -2 over 468.6-479.6 (variant C) changes the onset counts by less than one; not needed.

`_lg_c18` is on the c18 do-not-touch list. This finding does not change its shape or the bar levels it was fitted to. It only removes one track that was listed by mistake and puts the level back on the theme.

## 2. Fugato, bars 88-90: the celli keep their first-entry roles (+5 dB, then +3) under the second entry, and the mp counter-subject covers the mf subject (measured; fix simulated)

**Where.** qn 348.5-358 (p. 9).

**Score.**
- Second subject entry: Bassoon 1 and Violas, mf, from 348.5 (accents and staccato as printed).
- The celli, who played the first entry alone (bars 85-87, mf), go on with the counter-subject at mp (printed at 348).
- The basses play pizz. mf.

**Evidence.**
- `roles.json` Violoncellos has `[336, 358, 3]`, `[338, 348, 3]` and `[336, 352, 2]`. The roles add up, so parts.json `vol_db` for the celli reads:

  | qn | 340-347 | 349-352 | 353-356 |
  |---|---|---|---|
  | Celli vol_db | +8.0 | +5.0 | +3.0 |

- The entry gets the same +5: Violas and Bassoon 1 `[348, 358, 5]`.
- With the soft trims (celli at CC 58: +3.0 dB; violas at CC 72: +0.7), the mp celli carry 2.3 dB more envelope than the mf violas.
- Subject onsets, first 0.3 s, A:
  - median -1.7 dB; covered 9 of 14; worst -6.6.
  - The celli are the covering stem on all 9 (e.g. 89.00 -2.2, 89.25 -2.3, 90.50 -2.6 dB).
- Celli minus the subject per half beat: median +2.0 dB, over 0 on 14 of 23.
- The neighbouring entries, measured the same way:

  | Entry | Bars | Covered | Median |
  |---|---|---|---|
  | 3 (CA + Violins II, after the c17 fix) | 91-93 | 6 of 14 | +0.9 |
  | 4 (Flute 1 + Violins I) | 94-96 | 5 of 15 | +1.5 |

**Fix.** In `build/roles.json`, Violoncellos:
- `[336, 358, 3]` -> `[336, 348, 3]`
- `[336, 352, 2]` -> `[336, 348, 2]`
- Keep `[338, 348, 3]`.

The celli then lose their lift as the subject enters, so the mp counter-subject has no role. Level only.

**Simulated** (`sim_fug.py`, celli -5 over 348.4-352 and -3 over 352-358):
- Subject onsets: median -1.7 -> +2.5 dB; covered 9 -> 3 of 14.
- Celli minus the subject: median +2.0 -> -1.9; over 0 on 14 -> 8 of 23.
- The worst case (-6.6 at 359) is the celli's printed crescendo into entry 3. It stays, as it should.
- Master K, bars 88/89/90: -34.0/-32.5/-29.2 -> -34.9/-33.1/-30.0. Bar 91 is unchanged at -28.4. The crescendo into entry 3 still rises 4.6 dB.

## 3. Lento, bars 10-11: the bassoons' pp crescendo chord rises level with, then over, the Violins I mp melody (measured; fix simulated)

**Where.** qn 36-48 (p. 2).

**Score.**
- Bassoons 1-2: a held two-note chord, pp at bar 9, crescendo to f at bar 12.
- Violins I: the mp melody from bar 10, crescendo to f at bar 12.
- Strings: pp crescendo.

**Evidence.**
- Violins I minus the loudest other stem per half beat, A:
  - median +0.4 dB; covered 11 of 24; worst -3.1.
  - Onsets: 42.0 -0.9, 43.0 -4.5 (Bassoon 2 the coverer on both).
- At 1/16-note resolution:
  - 10.50-10.69: Bassoon 1 is the loudest stem (-4.4..-5.2 re master; Violins I -7.2..-7.6).
  - 11.38-11.75: Bassoon 2 is the loudest stem (-4.3..-6.7; Violins I -6.4..-8.8).
- **Cause.** The soft trims are the largest of any wind: Bassoon 1 pp +10 / p +7, Bassoon 2 pp +12 / p +8 (`mix.json`). They hold a pp line at the melody's mp level once both crescendos start. There are no roles on either bassoon before qn 50.
- The printed dynamics put the bassoons a step under the violins through the whole crescendo.

**Fix.** In `build/roles.json`, add Bassoon 1 `[36, 48, -3, 1]` and Bassoon 2 `[36, 48, -3, 1]`. The cut opens over 47-48 into the f at bar 12. Level only.

**Simulated** (`sim_bn.py`, -3 dB over 36-47.8):
- Violins I margin: median +0.4 -> +1.7; covered 11 -> 5 of 24.
- Bassoon 2 re master in bar 11: -9.3 -> -11.9 dB (A).
- Master K, bars 9-12: -35.5/-30.5/-24.6/-21.6 -> -35.5/-31.3/-25.2/-21.8. The crescendo still rises 13.7 dB over the four bars, with no step against the printed shape.
- Bassoon 1 -2 / Bassoon 2 -4 gives covered 7 of 24. Equal cuts are better.

## 4. Bars 122-123 (fff, qn 484-492): Trombone 2's F3 and the bass trombone's G2 are the two loudest pitched stems, 2.2-2.8 dB over Trombone 1 in the same chord (measured; fix simulated)

**Score.** pp. 11-12. A held fff diminished-seventh chord over the G pedal, with the tam-tam fff. The Violins I / Flute 1 top line falls A-flat6 -> G6.

**Evidence.**
- 484.3-491.8 A re master:

  | Stem | Note | dB |
  |---|---|---|
  | Tam-tam | | -9.8 |
  | Trombone 2 | F3 | -10.0 |
  | Bass trombone | G2 | -11.0 |
  | Violins II | | -12.1 |
  | Trumpet 1 | A-flat4 | -12.3 |
  | Oboe 1 | | -12.6 |
  | Trombone 1 | A-flat3 | -12.8 |
  | Trumpet 2 | | -13.0 |
  | Violins I | | -13.1 |

- Trombone 2 minus Trombone 1, A, by 4-bar group (`lowtb.py`):
  - +2.5 at fff in bars 121-124.
  - -3.4..+1.8 everywhere else at f/ff/fff, median about 0.
- Bass trombone minus Trombone 1: +2.2 at fff in bars 121-124.
- The three trombones carry the same roles here (`[484, 492.5, 2.5, 1]`; Bass trombone `2`), so the difference is the samples at these pitches.
  - Note bodies (K): Trombone 1 A-flat3/G3 -22.3/-24.3; Trombone 2 F3 -20.8/-22.2.
  - At 636-640 Trombone 1's C4/B3 measure -20.7/-20.8.
- One inner voice of the brass chord stands out by itself.

**Fix.** In `build/roles.json`:
- Trombone 2 `[484, 492.5, 2.5, 1]` -> `[484, 492.5, 0, 1]` (delete the row).
- Bass trombone `[484, 492.5, 2, 1]` -> `[484, 492.5, 0, 1]`.

Level only. This leaves Trombone 1 and the trumpets' +2/+2.5 alone.

**Simulated:**
- A re master: Trombone 2 -12.2, Trombone 1 -12.5, Bass trombone -12.6. The chord's pitched order becomes Violins II -11.7, Trumpet 1 -12.0, then the trombones.
- Master K over the chord: -10.77 -> -11.05.
- The climax order is safe: bar 122 moves down, away from bar 160 (c18 delivered 160 -10.10 > 122 -11.31 > 167-170 -13.11). Bar 122 stays about 3.7 dB over bar 121.

## 5. Smaller items (measured; no change proposed this cycle)

- **Horn 3 and Horn 4 soft dynamics are flattened by the soft trims.**
  - Soft trims: Horn 3 pp +15.8 / p +15.4 / mp +8.4; Horn 4 pp +16.7 / p +12.0 / mp +6.7. Horn 1 has p +10.6 / mp +7.2.
  - Pitch-matched steps:

    | Step | Horn 4 | Horn 3 | Horn 1 | Strings | Winds |
    |---|---|---|---|---|---|
    | pp -> p | -0.5 | | | +3.5..+6.1 | +4.7..+6.8 |
    | p -> mp | +1.7 | +0.2 | +6.3 | | |

  - Horn 3's pp chords at bars 57-60 (-39.1 dB) are louder than its mp inner line at bars 101-108 (-43.6/-45.3).
  - These are accompaniment chords 12-19 dB under the master, so no listener-level problem was found. A Horn 3 p anchor of about +12 would restore the order. That trim is worth fitting at the next horn-trim refit, not by itself.
- **Harp, bar 157:** the f chord (qn 624, velocity 100) is 0.5 dB under the mf chord at 620 (velocity 90). The trim falls 1.5 dB from mf to f. Harp `dyn_trim_db` f 1 -> 2.5 would fix it; this is a small item.
- **Tam-tam pp (qn 696):** still a 60-100 Hz hum with nothing above 300 Hz (A -16 re master in its first 1.5 s). This is known since c01. Changing it needs a different sample or articulation; it is not a level fix.

## Do not touch

- The family ladders and wind f trims with their mf anchors.
- The trumpet trims and roles, including the c18 Trumpet 2 f trim and the recapitulation trumpet roles; the coda trumpet and horn balance.
- The other nine tracks of `_lg_c18`, with `ARRIVAL_WEIGHT_AT` 484.
- The c17 fugato entry-3 roles (360-372) and the bar-121/124/125 roles; Trombone 1's and the trumpets' 484-492.5 roles.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`; the percussion patches, seats, gains and timing.
- The basses' 87 Hz bell and the celli's loud EQ.
- `accent_fits.json` and `accent_bodies.json`; `_REBOW_FROZEN`.
- The climax order (160 > 122 > 169) with `FAST_CAP_ABOVE` 4 and top ride 1.6.

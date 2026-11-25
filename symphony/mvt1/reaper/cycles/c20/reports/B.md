# Cycle 20, critic B: balance and levels (render c19)

## Method

All numbers come from the stem-fixed c19 render (`cycles/c19/render/`, 33 stems) and `build/parts.json` (00:00, the stem-fixed build that matches it), `roles.json`, `mix.json`, `score_config.py`.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c20-B/`:
- The c19-B set, re-run on c19: `env.py`, `fam.py`, `near.py`, `brtop.py`, `oncov.py`, `aw.py`, `loopchk.py`, `accents.py`.
- New:
  - `dynx.py`: each sustained stem's A level against the median stem at the same printed dynamic in the same beat.
  - `tremcmp.py`: tremolo-row level of Violins II against Violas and Violins I in the same beats, with and without the volume envelope.
  - `trem81.py`: per-beat A level with the track's `vol_db`.
  - `grpA.py`: group power per beat.
  - `accbal.py`: fitted accents that end up as the loudest stem.
  - `simpts.py`: envelope simulation with exact `(qn, dB)` point shapes, the same format as `LEVEL_SHAPES`. Driven by `sim40.py`, `sim81.py`, `sim81b.py`, `sim12.py`, `sim32.py`, `sim19.py`, `simall20.py`.

Definitions:
- "A" is the A-weighted sum of the eight band envelopes, and "re master" means stem minus master over the same window.
- "Onset margin" is the melody stem minus the loudest other sounding stem over the first 0.3 s of each melody onset. "Covered" means the margin is under 0.

Melody and accompaniment were assigned from the score pages (pp. 1-17 at 90 dpi).

## What holds (measured)

**c19 B changes.** All four landed as simulated or better (onset margins):

| Change | Result on c19 | c19 simulation |
|---|---|---|
| Letter G, bars 117-120 | median +2.0, covered 3 of 18, worst -2.0 | covered 7 of 21 |
| Fugato entry 2, bars 88-90 | median +4.1, covered 1 of 12 | |
| Lento, bars 11-12 | median +0.9, covered 2 of 5, worst -2.5 | |
| Bar 122 trombones | Tb2 -13.9, Bass trombone -13.4 re master, under Trombone 1 | |

**Family ladders.** K, median note bodies:

| Family | pp | p | mp | mf | f | ff | fff |
|---|---|---|---|---|---|---|---|
| Winds | -45.6 | -41.7 | -40.7 | -38.7 | -36.2 | -32.1 | -26.7 |
| Brass | -46.2 | -43.9 | -40.9 | -37.1 | -33.2 | -27.9 | -23.5 |
| Strings | -47.0 | -42.3 | -39.1 | -37.0 | -33.4 | -27.3 | -23.4 |

- p sounds like p in all three families, within 1.6 dB.
- With `dynx.py` (A, per beat, against the median stem at the same printed dynamic):
  - Woodwinds, horns, violas and celli sit at -1.5..+1 dB at every dynamic.
  - The trumpets sit at +1..+4 at f/ff and the trombones at +3..+4. That is the brass-over-wind margin Rimsky-Korsakov's ratios ask for (a horn is about two woodwinds, a trumpet or trombone about two horns), or a little under it.
  - Violins I sit at +5 at every dynamic, as the usual melody.
  - The basses and contrabassoon read low only because of the A-weighting.

**Melody margins elsewhere.** Onset margin, A:

| Bars | Median | Covered |
|---|---|---|
| 15-22 | +5.8 | 2 of 38 |
| 27-32 | +3.6 | 6 of 30 |
| 47-54 | +6.5 | 3 of 27 |
| 56-68 | +3.2 | 8 of 45 |
| 98-102 | +1.4 | 2 of 16 |
| 103-106 | +5.1 | 3 of 19 |
| 139-143 | +2.6 | 1 of 20 |
| 147-155 | +6.5 | |
| 167-170 | +2.4 | 2 of 15 |
| 175-180 | +3.8 | 1 of 11 |

**Percussion.**
- Tam-tam fff (qn 484): the top stem at -19.8..-24 re master for about 3 s, as printed.
- Crash (636): -23.6 re master A, a 5-20 kHz lift.
- Suspended-cymbal roll: rises from -99 to -29.5 dB into the crash.
- Final chord: Violins I, Violins II and violas within 2 dB; celli 5 dB under.

**Dan's checks.**
- Loop pulsing: the same 8 unsplit notes of 6 s or more. The worst is Bass clarinet 11 (100-300 Hz autocorrelation 0.81). Master windows are 0.02..-0.46, except 160-176 (+0.30, the printed decrescendo).
- Accents, 2-5 kHz in the first 80 ms minus the body:

  | Family | Median | Over +3 dB |
  |---|---|---|
  | Brass | -5.4 | 2 of 126 |
  | Winds | -5.8 | 8 of 217 |
  | Strings | -3.3 | 10 of 178 |

  The worst is still Violas 536, +13.6 (A's lens).

## 1. The Violins II tremolo row is 4-12 dB hotter than the violas' and Violins I's, and the -3 dB roles that hold it down release exactly into the crescendos of bars 39-40 and 80-81, where it becomes the loudest stem over the melody (measured; fix simulated)

**The row is hot** (`tremcmp.py`, A, same beats, same CC11, `vol_db` removed):

| Passage | Violins II tremolo minus violas tremolo |
|---|---|
| p, bars 37 and 77-79 | +4.0..+10.0 |
| f, bars 39-40 | +1.1..+3.6 |
| bars 80-81 crescendo, CC 50 -> 106 | +6.6 -> +12.0 |
| fff, bar 122 | +17 (against violas' tremolo) |

Against Violins I's tremolo on the same chords:
- bars 167-170 (two notes on each track): -0.7..+6.0, median about +3;
- bar 122: +3.0..+7.6, but Violins II has two notes there and Violins I one.

In bars 37-41 and 77-81 Violins II plays one tremolo note at a time. The violas play one, or two at bar 40, so divisi does not explain the excess.

**Current fixes.** The loop has handled this passage by passage with roles: -7..-9 at 440-464, -6 at 584-620, -7 at 484. Two are only -3 and ramp out over 4 qn into a printed crescendo: `roles.json` Violins II `[144, 156, -3, 4]` and `[304, 320, -3, 4]`. The crescendo's +3 string hairpin gain then lands on top.

**Bars 39-41** (qn 152-164, p. 4). Violins I, Flute 1 and Oboe 1 have the 16th-note line crescendo to sf. Violins II and violas play the tremolo chord, f at bar 40.
- Bar 40, A:

  | Stem | dB |
  |---|---|
  | Violins II | -28.8..-30.3 |
  | Violins I | -33.5..-34.6 |
  | Violas | -35.1..-37.4 |

- Melody onset margin: median -3.1; covered 15 of 18; 9 under -3; worst -5.5. Violins II is the coverer on 13.

**Bars 80-81** (qn 316-324, p. 7, letter E). Violins II and violas tremolo, p cresc. to ff at bar 82. Over it, the f motif entries: bassoons, Horns 3-4, trombones and celli at 80.1; Oboe 1 and Violins I at 80.6; trombones and celli at 81.1; Flute 1 and Violins I at 81.6.
- From 316 to 323 Violins II rises 16.5 dB (-42.9 -> -26.4 A), the violas 8.5 dB (-46.8 -> -38.3).
- At 81.75 Violins II is 4 dB over Violins I's f entry and 13.6 dB over Flute 1.
- At 324 (the ff downbeat) it falls to -27.8. Its own ff arrival is under the end of its tremolo.
- Entry onset margins 316-324: median -1.8; covered 4 of 8; 4 under -3; worst -7.5 (322.5). Violins II is the coverer on all four.

**Fix.** Level only, so `stem_fix.py` can apply it. Add two shapes to `build/score_config.py`:

```
LEVEL_SHAPES["Violins II"] += [[(151.9, 0.0), (152.0, -1.0), (156.0, -6.0), (159.9, -6.0), (160.0, -3.0), (162.0, -3.0), (162.5, 0.0)],
                               [(315.9, 0.0), (316.0, 0.0), (323.6, -6.0), (324.2, -6.0), (324.3, 0.0)]]
```

These add to the existing roles. The second shape is back to 0 before Violins II's ff pickup (moved onset 324.374).

**Simulated** (`sim40.py`, `sim81b.py`):
- Bars 39-41:
  - Melody margin median -3.1 -> +0.8; covered 15 -> 6 of 18; under -3: 9 -> 1.
  - Bar 40: Violins II -34.8..-36.3, Violins I -33.5..-34.6, violas unchanged.
  - Master bars 39/40/41: -23.3/-20.4/-19.2 -> -23.8/-21.2/-19.3. The crescendo still rises 4.5 dB into the sf.
- Bars 80-81:
  - Entry margins: covered 4 -> 2 of 8; under -3: 4 -> 0; worst -7.5 -> -2.1.
  - Violins II at 323: -32.4, under its ff arrival (-30.2).
  - Master bars 80/81/82: -27.2/-22.9/-15.4 -> -27.4/-24.5/-15.5. Each bar is still louder than the one before.

**Generic alternative (inferred, not simulated).** A per-row offset for the Violins II "Tremolo" row of about -5 dB on all its notes. `ROW_TRIM_DB` cannot do it, because it skips long and re-bowed notes and needs a Leg note nearby. The four existing Violins II tremolo roles would then have to be refitted.

## 2. Development, bars 78-79: the Horns a2 mf entry is the loudest event of the passage. It is louder than the f entries that follow, and it covers the next mf entry (Oboe 1 / Violins I / celli) by 6 dB (measured; fix simulated)

**Where.** qn 310.5-314 (p. 7). The motif passes through mf entries:

| qn | Entry |
|---|---|
| 304.5 | Bass clarinet solo, mf |
| 307 | Clarinet 1, mp |
| 310.5 | Horns 1-2 a2, mf, accented first note |
| 312.5 | Oboe 1 + Violins I + celli, mf |

f entries follow at bar 80.

**Evidence.** Mean A over each entry's first 1.5-3 qn:

| Entry | dB |
|---|---|
| Horns a2 311-313.5 | -33.6 |
| Bass clarinet | -43.5 |
| Oboe 1 / Violins I, 312.5-315 | -39.1 / -39.6 |
| Trombone 1 f, 316.5 | -36.2 |
| Violins I f, 318.5 | -35.0 |

- At 78.75 the horns are -0.6 re master, and the master is 4-6 dB over the bars before.
- `dynx.py`: Horns a2 stand +13 dB over the median stem at mf, the largest excess of any brass entry.
- Oboe 1 / Violins I onsets at 312.5 and 313.0: -6.3 and -5.9 dB under the horns' tail.
- **Cause:** shaping layers stacked on one figure in the a2 track's `vol_db`:
  - `PICKUP_LIFT` +4.7 at 310.5;
  - `accent_fits.json` Horns a2 `"311": [5.0, 0.21]`;
  - `early_fills.json` `"312.5"` +5 dB;
  - `vol_db` reaches +5.0..+5.9 over 310.8-311.5.

**Fix.** Level only. Add an exact shape and leave the fitted rows untouched (they are on the c19 do-not-touch list):

`LEVEL_SHAPES["Horns a2"] += [[(310.0, 0.0), (310.2, -4.0), (313.4, -4.0), (313.9, 0.0)]]`

It starts before the pickup's moved onset (310.265) and is back to 0 under the existing release notch (-6..-9 from 314.2).

**Simulated** (`sim81b.py`, horns alone):
- Oboe 1 / Violins I entry at 312.5-313.0: -6.3/-5.9 -> -2.3/-2.1. Under -3: 2 -> 0 of 5.
- The horn entry becomes -37.6 A, under the f entries (-36.2, -35.0). It is still 6 dB over the bass clarinet's mf, which is the ratio Rimsky-Korsakov gives for two horns against one wind.
- Master bars 78/79: -30.8/-30.5 -> -32.0/-31.3, so bars 77-80 now rise steadily (-34.3, -32.0, -31.3, -27.4 with finding 1).
- -3 dB instead of -4 leaves the onsets at -3.3. Use -4.

## 3. Lento climax, bar 12: the melody's f note sags after its automatic re-bow, and the violas' f double stop and Trombone 1 (printed mf) sit level with it or over it for a beat and a half (measured; fix simulated)

**Where.** qn 44-48 (p. 1).
- Violins I with Flute 1: the f arrival on A-flat5, held from bar 11.
- Violas: a C4/E-flat4 double stop, f.
- Trombones 1-2 and bass trombone: mf.

**Evidence** (A re master, half beats 44.5-46.0):

| Stem | dB |
|---|---|
| Violins I | -10.0..-10.8 |
| Violas | -7.8..-8.3 (the loudest stem) |
| Trombone 1 | -10.6..-11.9 |
| Flute 1 | -12.8..-15.9 |

**Cause (measured):**
- The 43.0 Violins I note (3.95 qn = 4.7 s at q=50) is re-bowed at 44.835.
- Its `rebow_fills.json` row "44.835" pulls the body -3..-6 dB from +0.32 s to the end. That holds the f arrival at the crescendo's pre-arrival level.
- The violas' two notes are two full-section samples (LEARNINGS section 8: about +2 dB over one note). They carry the full +1.5..+3 dB string crescendo gain.

**Fix.** Level only. In `build/score_config.py`:

```
LEVEL_SHAPES["Violas"] += [[(43.8, 0.0), (44.0, -2.5), (47.8, -2.5), (48.0, 0.0)]]
LEVEL_SHAPES["Violins I"] += [[(45.05, 0.0), (45.2, 2.5), (46.4, 2.5), (46.6, 0.0)]]
```

The second shape is equal to capping that re-bow fill's body cut at about -3 dB. Alternatively, edit `rebow_fills.json` "44.835" from +0.36 s on.

**Simulated** (`sim12.py`):
- Violins I over violas at 44.5-46.0: -1.6..-2.7 -> +0.6..+3.7. Violins I over Trombone 1: +0.6..+3.6.
- Melody onset margin worst -2.5 -> -1.2.
- Master bar 12: -21.9 -> -22.0. The 13.7 dB rise over bars 9-12 is kept.

## 4. Bar 32: Horn 2's accented F4 is the loudest stem of the ff accented chords, and the trumpet accents stand 5-8 dB over their neighbours (measured; horn fix simulated; lower priority)

**Where.** qn 124-126 (p. 3). Two accented ff tutti quarter-note chords before letter B.

**Evidence:**
- Horn 2 at 124/125: note body -25.7/-27.3 A. Its other F4s in bars 29-31 are -31.6..-32.6, with the F4 pitch trim on all of them.
- `accent_fits.json` gives Horn 2 "124" 4.47, Horn 1 "124" [5.0, 1.0], Horn 3 "124" 4.16.
- Per half beat Horn 2 is the top stem at -8.2..-9.4 re master; Violins I (top note) is at -10.4..-11.5.
- `accents.py`, level over unaccented neighbours:

  | Note | dB |
  |---|---|
  | Trumpet 2, 125 | +8.0 |
  | Trumpet 1, 125 | +6.0 |
  | Horn 4, 125 | +5.1 |
  | Trumpet 1, 124 | +4.7 |

  The brief's rule is 2-4 dB.

**Fix.** `LEVEL_SHAPES["Horn 2"] += [[(123.7, 0.0), (123.8, -3.0), (125.9, -3.0), (126.1, 0.0)]]`.

**Simulated** (`sim32.py`):
- Onset margin at 124/125: -2.9/-3.3 -> 0.0/-1.8.
- Horn 2 drops to the level of the other brass. Master bar 32: -17.7 -> -17.9.
- The trumpets stay the top stems on the off-beat halves (Trumpet 1 -6.9..-8.7 re master). That is idiomatic for a ff accented tutti chord, so no trumpet change is proposed.

## 5. Smaller items (measured; no change proposed)

- **Bars 19-22, violas espr. counter-line.** It sits a median 5.9 dB under the Violins I theme (both printed mf<f) and 4.3 dB over the celli.
  - Simulated +2.5 / +3.5 dB on the violas: their onset margin -6.2 -> -3.7 / -2.7, but the theme's covered onsets 2 -> 7 of 20.
  - Leave it.
- **Bars 131-134, recapitulation theme vs the descant.** Theme: clarinets, bassoons, trombones, celli. Descant: flutes, oboes, violins ff.
  - Theme group -4.8..-6.9 re master; descant -2.1..-6.6; accompaniment group -1.6..-5.3.
  - Theme onsets covered 11 of 18, but only 2 under -3 (worst -3.8, Violins I).
  - Already cut by the c17/c18 roles. No change unless another critic hears the theme lost.
- **Bars 111-116.** The Violins II tremolo chords cover 5 Violins I crescendo onsets by -1.3..-4.3 dB, despite the -7..-9 role.
  - The same row problem as finding 1. Recheck after it, or take the generic row offset there.

## Do not touch

The c19 B roles (letter-G bass trombone shape and the theme +2.5, fugato celli roles ending at 348, Lento bassoons -3, bar-122 trombone roles), and every other c19/c18 level item on the HISTORY do-not-touch list:
- `_lg_c18` with `ARRIVAL_WEIGHT_AT` 484;
- the trumpet trims and roles;
- the Horns a2 windows and roles (findings 2 and 4 add shapes; they do not change these);
- `accent_fits.json` / `accent_bodies.json`;
- the basses' 87 Hz bell and the celli loud EQ;
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`;
- the percussion patches, gains and timing;
- `_REBOW_FROZEN`;
- the climax order 160 > 122 > 169 with `FAST_CAP_ABOVE` 4 and top ride 1.6. The combined findings 1-4 leave the master's loudest 3 s window unchanged (-8.77 dB K).

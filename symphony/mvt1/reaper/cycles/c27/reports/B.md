# Cycle 27, critic B: balance and levels (render c26)

## Method

All numbers come from `cycles/c26/render/`, the stems and master after the c26 stem fixes. Notes, dynamics and envelopes come from `build/parts.json` and `build/mix.json`.

- **Envelopes.** Per 10 ms frame (2048-point STFT, stereo power): K-weighted, A-weighted, plain power, bands 30-100 / 100-300 / 300-1k / 1-2k / 2-5k / 5-10k Hz, and the spectral centroid.
- **"re M"** is a stem minus the master over the same window. K is used unless A is named.
- **Pitch fundamentals.** For per-note fundamental strength I used a long FFT (the whole note body, 0.15 s to 2 s) and the energy within ±3% of harmonics 1-4. The 2048-point bands smear notes near 100 Hz, so they are not used for that.
- **Score pages checked:** 2-5, 8, 11-14, 16-18.

Scratch scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c27-B/` (`lib.py`, `ladder.py`, `bars.py`, `cover.py`, `peer.py`, `groups.py`, `win.py`, `fund.py`, `simeq3.py`, `dan.py`, `acc2.py`, `loop2.py`, `timp.py`, `tpt.py`, `tubacmp.py`). I delete the folder when I finish.

## What holds (measured)

**Dynamic mapping between families.** I compared each track with the median of the other tracks that hold a note in the same 1-qn window with the same flat printed dynamic (at least 4 tracks from 2 or more families).
- Woodwinds, horns, trombones, bass trombone and tuba sit within about ±2 dB of their peers at p, f and ff.
- Violins I sit +2..+5 and celli +1..+4. Both are melody or bass carriers, so this is expected.
- At fff the bass woodwinds sit 4-6 dB under their peers (bass clarinet, bassoons, contrabassoon). That is normal.

**Per-track ladders.** Median K body per printed dynamic rises from p to fff on every track that plays at more than three levels. The f to ff step is 4-6 dB for strings, winds, horns, trumpets and trombones.

**Trumpets.**
- In f/ff chords Trumpet 1 sits 1-7 dB (A) over Trumpets 2/3. Trumpet 2 sits about 1.5 dB under Trumpet 3 (median).
- The trumpets carry the bar 115-116 line, where they are printed ff a bar ahead of the tutti (score p. 10).
- Trumpet 1 carries the 167-170 theme, with the theme group 4.3-5.3 dB K re M and no other group covering it.

**Percussion.**
- Crash at 636: K -12.8 re M; it supplies half of the master's 5-10 kHz.
- The suspended-cymbal roll grows from -54 to -19 re M into the crash.
- Tam-tam 484 fff: -7.8..-10.3 K re M for 4 qn, then decays. It is the top stem of bar 122 (printed fff, heavy beater).
- Tam-tam 696 pp: -12 K re M.

**Timpani.**
- Rolls without a printed crescendo stay 11-18 dB under the master.
- The final ppp roll (720-727) sits 1-3 dB under the quietest string section.
- The bars 179-180 pp strokes peak at -10..-13 re M: audible, and under the chorale.

**Melody over accompaniment.** These hold in the passages I re-checked: bars 5-9, 13, 19-22 (violas espr. over celli in A), 45-46, 73-76, 117-121, 131-134 (theme group -3.5..-4.9 K re M against descant -6..-9.6 and brass chord -5.7..-7.9), 140-142, 158-162, 167-170 and 171-182.

**Dan's checks (measured).**
- *Loop pulse.* I scanned 34 merged same-pitch held spans of 6 s or more (strings, winds, horns, timpani).
  - The highest 3.95 s autocorrelation is 0.32: harp repeated notes at 247.5 (not a loop) and the violas' final chord centroid (0.30).
  - Everything else is ≤ 0.18.
  - Master over the coda chorale: -0.27 band / -0.16 centroid. Final chord: -0.17 / -0.17.
- *Accents.* 2-5 kHz over the first 80 ms minus the body at +0.15-0.6 s:
  - brass median -3.9 dB (7 of 168 over +3);
  - winds -2.5 (13 of 232);
  - strings -0.9 (9 of 169).
  - Only three accents also carry the master's 2-5 kHz and make it jump more than 3 dB over its own body. Two of them are finding 2.

## 1. The basses' B1 and D2 boom: bars 11-12, 97-98 and 113-114 (measured; fix simulated)

**Where.** Double basses, wherever they play these two pitches:
- **D2 (73.4 Hz):** qn 40-44 (bar 11, Lento f), 254, 278, 452 (bar 114) and 548.
- **B1 (61.7 Hz):** qn 100 (bar 26 ff) and 384/388 (letter F, bars 97-98 ff whole notes; score p. 9).

**What is wrong.** On these two pitches the Basses KS Master's fundamental is about as strong as harmonics 2-4 together. On the neighbouring pitches it is 6-21 dB weaker. So these notes put a boom under the master that the other bass notes do not.

**Evidence (measured).**

Fundamental minus harmonics 2-4, Cb stem, median per pitch:

| Pitch | dB |
|---|---|
| G1 | -20.6 |
| A♭1 | -21.0 |
| A1 | -17.2 |
| B♭1 | -12.3 |
| **B1** | **-2.2** |
| C2 | -5.9 |
| C♯2 | -1.8 |
| **D2** | **+0.6** |
| E♭2 | -8.2 |
| E2 | -7.0 |

Master 30-100 Hz minus 300-2k Hz:

| Where | Note | dB |
|---|---|---|
| Bars 97-98 (whole note) | B1 | -8.8 |
| Bar 11 | D2 | -6.0 |
| Bar 114 | D2 | -10.6 |
| Bar 26 | B1, same pitch, fuller tutti | -16.6 |
| Bars 27-31 | other ff tutti | -19.1 |
| Bar 32 | other ff tutti | -11.1 |
| Bars 138-142 | other ff tutti | -16.8 |
| Bars 160-162 | other ff tutti | -18.5 |

- At 384 the basses supply nearly all of the master's 30-100 Hz (share -0.8 dB).
- In bars 11-12 the basses (printed f, like everyone) are the top or second stem: -6.9..-8.4 re M, against the Vln I tune at -6.6..-9.5. Most of the basses' K level there is the fundamental.
- `mix.json` gives the basses only the F2 notch (bell2 87.3 Hz -10, 0.15 oct) and the 180 Hz body bell. The climax `loud_eq` windows do not cover bars 11-12 or 97-102.
- Movement II needed the same kind of fix for D2 (kit LEARNINGS section 14).

**Fix.**
- In `build/mix.json` Double basses, add a static second ReaEQ through the existing wet-EQ path. Use `mute_eq` (square step) or a one-element `loud_eq` spec with constant wet:

  ```json
  "mute_eq": {"from_qn": -2.5, "bands": [{"band": "bell", "hz": 61.7, "db": -6, "bw_oct": 0.25}, {"band": "bell2", "hz": 73.4, "db": -5, "bw_oct": 0.25}]}
  ```

- `from_qn` -2.5 lands inside the pre-roll, so the EQ is on from the first note. Do not use qn -3: `set_mute_eq` already inserts a 0 point at project time 0.
- This needs `--mix-only "Double basses"` with an FX rebuild.

**Expected (simulated with the RBJ bell response on the c26 Cb stem, master = master - old stem + new stem).**

Master 30-100 minus 300-2k:

| Where | Now | After |
|---|---|---|
| Bar 11 | -6.0 | -12.2 |
| Bars 97-98 | -8.8 | -15.2 |
| Bar 114 | -10.6 | -16.8 |
| Bar 26 | -16.6 | -22.0 |
| Bar 70 | -16.4 | -22.2 |

- The master's 100-300 Hz moves by under 0.05 dB in every span except bar 12 (-0.25).
- Master K moves by -0.03..-0.27 dB.
- The Cb stem K falls 2.3 dB in bar 11 (so it sits under the Vln I tune) and 1.1 dB in bar 97.
- Side effects:
  - C2 and C♯2 fundamentals lose about 5.5-6 dB. On the master that is -1.4 dB of 30-100 Hz in bars 1-4 (pp unison opening; master K -0.11).
  - B♭1 loses 4.8 dB, but its fundamental is already weak.
- Check the bar-3 swell after the render. If the opening sounds thin, narrow both bells to 0.18 oct.

## 2. Clarinet 1's accented G5s at 414 and 422 (bars 104 and 106): a bright attack that the master carries (measured)

**Where.** Bars 103-106, score p. 9:
- Clarinet 1 and Oboe 2 in unison, f, on the development's woodwind line.
- The accented G5 on beat 3 of bars 104 and 106 plays Sus Non Vib.
- The master is about -27 K here.

**Evidence (measured).**

| | 414 | 422 |
|---|---|---|
| Stem 2-5 kHz, first 80 ms minus body | +11.2 dB | +9.1 dB |
| Master 2-5 kHz over the 150 ms before | +7.4 dB | +9.6 dB |
| Master 2-5 kHz over its own body | +6.5 dB | +7.1 dB |

- In those 80 ms the clarinet alone is the master's 2-5 kHz (share -1.0..-1.8 dB).
- Oboe 2, on the same pitch, does not flag.
- In K the clarinet goes from -9.7 re M before the note to -4.8 at the attack and -7 in the body. That is a 2-5 dB level accent, but most of it is a 2-5 kHz burst. This is the brief's rule 4 and item 8 failing on a wind.
- Cause, in the volume envelope:
  - `accent_fits.json` Clarinet 1 414/417/422 = [5.0, 1.0]. That is the largest wind swell value, and it peaks 0.03-0.15 s after the onset (the c23 swell timing), right on the sample's bright attack.
  - Then comes the `accent_bodies` cut (-1.9 / -3.0) plus the G5 pitch trim -3.
  - Together these make a 10-14 dB front-to-body shape in the envelope: +6.8 dB at 414.06, -7.4 at 414.8.
- Velocity is not the lever. The KS Master sustain rows ignore velocity (c06 B #1).

**Fix.**
- `build/accent_fits.json` Clarinet 1: "414", "417", "422" [5.0, 1.0] -> [2.0, 1.0].
- Add all three to the fit's skip list so a later `fit_accents.py` run does not restore them.
- Expected: master 2-5 kHz jump about 4 dB instead of 6.5-7.1. The accent still sits about +2 K over the body, because the body cut stays.
- Level only, so `--mix-only "Clarinet 1"`.
- If A's lens owns accent fitting, hand this to A. The measure sits under my lens because the master carries it.

## 3. Bar 40 (qn 156-160): the timpani pp< roll is the top stem in K over the f orchestra and Violins I's run (measured; audibility in A inferred smaller)

**Where.** Bar 40, score p. 4:
- Timpani roll on B♭2, printed pp < to the ff/sf of bar 41.
- Strings, horns, bassoons and trombones are printed f. Violins I/II and Flute 1/Oboe 1 have the rising sixteenth run into bar 41.

**Evidence (measured), re M per 0.5 qn:**

| | 158.0 | 158.5 | 159.0 | 159.5 |
|---|---|---|---|---|
| Timpani K | -10.1 | -8.6 | -12.9 | -12.1 |
| Violins I K | -11.0 | -12.3 | -12.4 | -7.3 |
| Timpani A | -18.1 | -17.4 | -15.0 | -11.7 |
| Violins I A | -9.4 | -9.5 | -11.1 | -10.6 |

- Per 1 qn K window, the timpani is the loudest stem at 158-159 (-10.1 and -8.6, against Vln I -11.0/-12.3). In A it reaches Vln I's level only in the last half beat.
- The track volume envelope holds +19..+21 dB at the roll's start and still +14 at 159.9, on top of the CC11 ramp 34 -> 114.
- The brief says a roll grows only by its printed crescendo and is not the loudest stem unless the timpani lead. Here it leads in K for the bar's last two beats.

**Fix.**
- `build/score_config.py` `LEVEL_SHAPES["Timpani"]` += `[(157.5, 0.0), (158.25, -2.5), (159.9, -2.5), (160.0, 0.0)]`. It ends on the bar-41 stroke so the sf keeps its full level. Level only.
- Expected (level shift): timpani K -11..-13 re M at 158-159, at or under Vln I. In A it stays under Vln I to the downbeat. The roll still grows about 9.5 dB across the bar (c26: 12).
- The master in bar 40b drops about 0.3 dB, and the bar-41 sf is unchanged.

## 4. Bars 27-31 (qn 104-124): the brass printed f sit as close under the ff melody as the ff brass do in the recapitulation (measured; effect inferred)

**Where.** Score p. 2:
- Bars 27-31 put the theme ff in flutes, oboes, clarinets, Violins I/II and violas, with horns 1-2 ff.
- Trumpets, trombones, bass trombone and tuba are printed f, one level under.
- In bars 139-142 (p. 13) the trumpets are ff and the trombones and tuba f.

**Evidence, groups re M per 2 qn:**

| Group | Bars 27-31 K | Bars 27-31 A | Bars 139-142 K |
|---|---|---|---|
| Melody group | -3.0..-4.8 | -2.2..-3.6 | -2.5..-3.9 |
| f brass (3 trumpets, 2 trombones, bass trombone, tuba) | -5.0..-7.2 | -4.1..-7.3 | -3.9..-8.0 |
| Horns (ff) | -6.7..-13.1 | | |

- The melody margin over the brass group is 1.0-3.6 dB K (2.2-4.3 A) in the exposition and 1.3-4.5 dB K in the recapitulation. The printed f gives no extra margin.
- The ff horns sit 1.5-4 dB under the f brass.
- The trombones (f) are 3-5 dB over the ff Horn 2, Flute 2, Bassoon 1 and contrabassoon in 20-48 of the 1-qn windows from 104 to 126 (the covering scan, `cover.py`).
- Trumpets 2/3 already carry [104, 124, -2, 0.5]. Trombones 1/2 and the tuba have no role there.
- By Rimsky-Korsakov's forte ratios, a trombone at f is about two horns at ff. So the trombones should match the ff horns, not sit 1.5-4 dB over them (inferred).

**Fix.**
- `build/roles.json`: add `[104, 124, -2.0, 0.5]` to Trombone 1, Trombone 2 and Tuba (the same row the trumpets have). Leave the bass trombone alone: it sits 2-3 dB under the tuba in K and at its level in A.
- Expected (level shift):
  - brass group about 1.3 dB lower;
  - melody margin 2.3-4.9 dB K;
  - trombones level with the ff horns;
  - master about -0.4 dB over bars 27-31.
- Bar 26 (the arrival) and bar 32 are outside the span. The bar 26 delivered peak and the climax order 160 > 122 > 167-170 > 26 do not move.
- Simulate the delivered span and limiter before the render.

## Do not touch

- The c26 letter-G roles and the Horn 4 ff trim 2.
- The trumpet trims and roles. Trumpet 1 over Trumpets 2/3 in chords, and the bar 115-116 trumpet lead, are printed.
- The percussion gains, shapes and timing: tam-tam 484/696, crash shape, suspended-cymbal lead.
- `TIMP_CC1_MAP` and the roll shapes outside bar 40.
- The c26 tuba bell2 and the basses' 87.3 Hz bell2 (finding 1 adds bells; it does not replace these).
- The soft trims and `dyn_trim_db` tables: the cross-family peer check passes.
- The coda balance (bars 171-182), the bar-3 swell, the second-theme shapes and the recapitulation theme roles at 520-536.
- The climax order 160 > 122 > 167-170 > bar 26.

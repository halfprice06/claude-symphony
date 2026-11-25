# Cycle 26, critic B: balance and levels (render c25)

## Method

All numbers come from `cycles/c25/render/`. That folder holds the 33 stems and the master after both c25 stem fixes, so it matches what was delivered. The note and controller data come from `build/parts.json`.

- **Envelopes.** I computed envelopes per 10 ms frame (stereo power, 4096-point STFT): A-weighted, K-weighted, plain power, six bands (30-100, 100-300, 300-1k, 1-2k, 2-5k, 5-10k Hz) and the spectral centroid.
- **"re M"** means a stem minus the master over the same window. K-weighting is used wherever low instruments are compared, because A-weighting under-reads tuba, timpani and basses.
- **Note bodies** run from the onset + 0.1-0.15 s to min(note end, + 1.5-2 s).
- **Printed dynamics** come from each track's `dyn_curve`.
- **Score pages checked:** 2, 3, 5-13, 16-18.

Scratch scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c26-B/`; I delete the folder when I finish. They are `env.py`, `kenv.py`, `lib.py`, `ladder.py`, `top.py`, `win.py`, `hier.py`, `peer.py`, `bardyn.py`, `groups.py`, `sim.py`, `chord.py`, `hot.py`, `loop.py` and `acc.py`.

## What holds (measured)

**Melody against accompaniment in the ff tuttis.** The melody group (Violins I+II, Flutes, Oboe 1, Clarinet 1, K) sits over the four horns together:

| Bars | Margin over the horns |
|---|---|
| 26-32 | 3.5-6.0 dB |
| 138-142 | 5-8 dB |
| 158-161 | 3-5 dB |

The trumpet section sits 4-7 dB under the ff melody in bars 27-31 and 3-6 dB under it in bars 138-142. The one exception is letter G (finding 1).

**Trumpets.**
- In chords, Trumpet 2 and Trumpet 3 are within about 1-2 dB of each other, and Trumpet 1 is 1-5 dB on top.
- At 167-170, Trumpet 1 plays the a2 theme as the top stem: -6.2 A re M, 4.2 dB over the Horns a2 and 5.4 dB over the f Trumpet 3.
- Against peers at the same printed dynamic in the same 2-qn window, Trumpet 1 sits +2.5/+4.3 at f/ff and Trumpets 2/3 sit +0.0..+1.7. The ratio between trumpet and woodwind is about what Rimsky-Korsakov gives for forte.

**Percussion.**
- Tam-tam 484 fff: -6..-9 A re M for 2 s, then decays. 2-10 kHz stays 5-7 dB under the master.
- Tam-tam 696 pp: -10..-16 K re M.
- The suspended-cymbal roll rises from inaudible at 632 to -2.6 dB re M at 5-10 kHz at 635.75.
- No timpani roll is the top stem. In K the rolls sit 1.1-14.5 dB under the loudest stem.
- The pp/ppp rolls without a printed crescendo sit -1..-2.5 dB against the quietest string section. The f< roll at bars 80-81 is +2.5/+5.3 over the p strings, as printed.

**Coda.**
- Bars 171-174: the cello solo is the top stem (-0.6..-3 A re M), with the cor anglais imitation 3-5 dB under it.
- Bars 175-178: the pp chorale is even.
- Final chord: Violins I, violas, horns and basses all lie within 5 dB of each other. The master falls 38.7 -> 47.6 dB K over bars 179-182.

**Dan's checks.**
- *Loop pulsing.* On my method (1 s detrend), I scanned 59 merged held spans of 6 s or more.
  - The highest autocorrelation at 3.95 s is Horn 4 at qn 512 (bars 129-130 crescendo pedal): band 0.57, -11 A re M.
  - The master over the final chord reads -0.27 (band) / -0.15 (centroid). Bars 175-178 read -0.26 / -0.17.
  - No action from this lens.
- *Accents*, 2-5 kHz over the first 80 ms minus the 2-5 kHz body:
  - brass median -8.6 dB, 4 of 148 over +3;
  - winds -4.8, 13 of 220;
  - strings -3.2, 9 of 180.
  - The worst cases are the qn 536 entries (Violas +17, celli +13, Bassoon 1 +12). Those measure the ff tail of bar 134 under the subito mf of bar 135, which belongs to A's lens.

## 1. Letter G (bars 117-121, qn 464-484): the held ff horns and tuba are as loud as the ff melody (measured; fix simulated)

**Where.** qn 464-484, score p. 10.
- The melody: Violins I/II in unison, Flutes, Oboe 1 and Clarinets, ff.
- Under it, sustained ff harmony from Horns 1-2 a2 (the Horns a2 track), Horn 3, Horn 4 and the tuba.

**Evidence (measured):**
- Groups, each summed and re M (K, 4-qn windows from 464):
  - melody -4.2..-5.8;
  - four horns -5.4..-7.6;
  - tuba -9.2..-11.5.
- In A (2-qn windows), the horns are within 1 dB of the melody or over it: horns -4.9..-6.4, melody -3.3..-5.4. At 474-476 the horns are on top.
- In every other ff tutti the horns sit 3.5-8 dB under the melody (see "What holds"), and the tuba sits at -12..-19 K re M.
- The single tracks carry it: Horn 4 (a held G3) is -8.5..-10.2 A re M and Horn 3 is -9.1..-10.8.
  - In bars 117-121, Horn 4 is the second or third loudest stem in the orchestra.
  - At 464-468 Horn 4 is 5 dB over the Horns a2 pair on the same pitch (-9.2 vs -14.2 A). One player sounds louder than two.
- Cause, in `build/score_config.py` and `build/mix.json`:
  - The c18 "held parts" hold `_lg_c18` gives +3..+4 dB over 464-484 to Horn 3, Horn 4, Horns a2, Tuba and others.
  - c25 raised the Horn 4 ff trim to 4.0.
  - Horn 1 already has -2 there, Trombone 1 -5 and the bass trombone -3. Horn 3, Horn 4 and the tuba have no cut.
  - The track volume envelopes over 466-480: Horn 3 +4.0..+6.1, Horn 4 +4.0..+6.1, Tuba +4.0..+6.8, Horns a2 +0.6..+3.4.

**Fix.** Add these rows to `build/roles.json` (4-qn end ramp, like Trombone 1's row, so the bar-121 crescendo still opens into 484):
- `"Horn 3": [464, 484, -3.5, 4]`
- `"Horn 4": [464, 484, -4.0, 4]`
- `"Tuba": [464, 484, -3.0, 4]`

This is level only, so a stem fix or `--mix-only` is enough.

**Simulated on the c25 stems** (A, re the new master; master minus (1-g) times each stem):

| Measure | Before | After |
|---|---|---|
| Horn section re M | -4.9..-6.4 | -6.5..-9.0 |
| Melody margin over the horns | -1..+2 dB | +2.4..+4.5 dB |
| Tuba re M | -10.5..-12.6 | -12.7..-14.9 |
| Horn 4 at 464-468, against the Horns a2 pair | +5 dB over | level (-13.5 vs -14.1) |

- The master falls 0.5-1.0 dB (median 0.74) over 464-482.
- The arrival on the bar-117 downbeat stays over the crescendo top: master K at 464.5-465.0 is -13.2..-13.4 against -13.7 at 462. That is the c18 C #1 condition.
- Bar 122 and the climax order are not touched.

## 2. Violas qn 436 (bar 110): a stale +5 dB note trim makes the p Ab5 jump 9 dB over its phrase and over the mp flute in unison (measured)

**Where.** Bar 110 downbeat, score p. 9.
- The violas' p espressivo line climbs to Ab5 (tenuto, inside a crescendo).
- From bar 109, Flute 1 doubles it in unison, marked mp.

**Evidence (measured, K):**
- The previous viola notes (432-435.5) sit at -41.5, -41.7, -41.7 and -37.4.
- The Ab5 sits at -37.0..-37.8 for its first 0.25 s, then steps to -31.0..-32.5 for the rest of the note.
- The next note (438, G5) falls to -42.0.
- So the Ab5 is +9.6 dB over the median of its neighbours (+5 dB from the step), 4.1 dB over the mp flute on the same pitch (-36.5), and the top stem of the bar (-1.2..-1.4 A re M at 436.5-437).
- The step comes from `build/note_trims.json` `"Violas": {"436.0": 5.0}`. The volume envelope goes from +1.5 to +6.7 dB at 436.3.
  - That trim was added in c12 (A #3, a tenuto step trim) when the note measured 5.6 dB under its neighbours.
  - The note itself now plays 4 dB over them before the trim acts, so the trim is stale (kit LEARNINGS section 4, "Old negative note trims go stale"; the same holds for positive ones).
- A scan of every note trim of +2.5 dB or more found no other note over +4.6 dB against its neighbours.

**Fix.**
- `build/note_trims.json`: `"Violas"` `"436.0"`: 5.0 -> 0.0. Keep 429.0 +3.0: that note is +4.0 over its neighbours, as a tenuto should be.
- Expected (inferred from the note's first 0.25 s): body about -37.5, +4 dB over its phrase, level with the flute unison. That is a tenuto crest, not a jump.
- Level only.

## 3. Horn 4's ff trim (c25 B #4) puts it over Horn 3 in the Horn 3-4 pair outside the chords it was meant for (measured)

**Where.** Common Horn 3/Horn 4 onsets, 0.9 qn or longer.

**Evidence (measured).** Horn 4 minus Horn 3 (K, medians by printed dynamic):

| Dynamic | pp | p | mp | f | ff |
|---|---|---|---|---|---|
| Horn 4 - Horn 3 | -4.5 | -2.1 | -1.6 | -0.1 | +0.8 |

The places where the low horn is now the louder one:

| qn | Bar | Horn 4 - Horn 3 |
|---|---|---|
| 156 / 160 | 40-41 | +2.1 / +3.0 |
| 272-278 | 69-70 | +3.1..+3.3 |
| 328 / 330 | 83 | +4.0 / +4.6 |
| 492 | 124 | +3.6 |
| 520 | 131 | +3.5 |
| 528 / 532 | 133-134 | +2.0 / +4.7 |
| 464-480 | 117-121 | +0.6..+1.7 (letter G, finding 1) |

- At 520 Horn 4's held ff C is the third loudest stem (-9.8 A re M), level with the recapitulation theme carriers (Clarinet 1 -9.7, Bassoon 1 -10.6, celli -11.5). Horn 3 holds the upper note of the same ff chord at -13.5.
- At 162 Horn 4 is the second loudest stem.
- c25 B #4 set `dyn_trim_db` f/ff/fff 1.0/1.5/0.5 -> 2.5/4.0/2.0 from five chords (120, 122, 460, 556, 560) where Horn 4 was 8-11 dB under Horn 1.
  - In four of those five, Horns 3-4 are printed f and Horns 1-2 ff (score pp. 3 and 14), so part of that gap is printed.
  - At 120/122 Horn 4 is still 3.4-3.5 dB under Horn 3, so the boost did not reach its target and overshoots elsewhere.

**Fix (level only):**
- `build/mix.json` Horn 4 `dyn_trim_db` ff 4.0 -> 2.0. Keep f 2.5 and fff 2.0.
- `build/roles.json` `"Horn 4": [524, 536, -2.5, 1]`, for the f bars 132-134 after the ff chord.

**Expected (simulated as level shifts):**

| qn | Horn 4 - Horn 3 now | After |
|---|---|---|
| 328 / 330 | +4.0 / +4.6 | +2.0 / +2.6 |
| 520 | +3.5 | +1.5; Horn 4 -11.8 A re M, out of the top three |
| 528-534 | +2.0..+4.7 | -0.5..+2.2 |
| 160 | +3.0 | +1.0 |

- The master changes by less than 0.3 dB everywhere.
- The f chords that c25 fixed (120/122/556/560) do not move.
- At letter G this -2 adds to finding 1's -4.0. Set Horn 4's letter-G role to -2.0 instead of -4.0 if both are taken.

## 4. Bar 97 (letter F downbeat, qn 384-388): the bass clarinet is as loud as the whole cello section on the ff B2 whole note (measured)

**Where.** Bar 97, score p. 9. Seven bass voices hold a ff whole note: bass clarinet, Bassoon 2, contrabassoon, bass trombone, celli, basses, plus Bassoon 1. The ff melody enters on the pickup.

**Evidence (measured).** Over 384.1-387.9:

| Voice | K re M |
|---|---|
| Celli | -6.5 |
| Basses | -7.3 |
| Bass clarinet | -7.5 |
| Bassoon 2 (same pitch, B2) | -10.4 |
| Bass trombone (same pitch) | -10.6 |
| Contrabassoon | -15.9 |

- In A the bass clarinet is the top stem of the bar (-7.0 / -6.3 re M on the two half-bars).
- Cause: the crescendo gain of bars 95-96 (`hpgain` [376, 384, +4.0]) is still +4.0..+5.1 dB in the bass clarinet's volume envelope over the whole note. The celli carry a -3 role there ([360, 408, -3]).
- By Rimsky-Korsakov's forte ratio, one woodwind sits about 3 dB under a string section (inferred). Here it equals the section and is 3 dB over the bassoon and bass trombone on the same pitch.

**Fix.**
- `build/roles.json` `"Bass clarinet": [384, 388, -3.0, 0.5]`.
- Expected: about -10.5 K re M, level with Bassoon 2 and the bass trombone; master -0.2 dB in bar 97. Bassoon 2 has the same +4 gain but is already 3 dB under; leave it.
- Level only.

## 5. Tuba E2/F2: the fundamental carries most of the master's 30-100 Hz on those notes (measured; audibility inferred, small)

**Where.** Tuba E2 at qn 116 (bar 30, f) and 444 (bar 112, p). Tuba F2 at 120 (bar 31, f), 440 (bar 111, pp) and 560 (bar 141, f).

**Evidence (measured).**
- On the tuba stem, 30-100 Hz minus 300-1k Hz is -7.1 (E2) and -5.7 (F2). Every other tuba pitch reads -13.7..-22.6.
- The tuba's share of the master's 30-100 Hz band, against the basses' share:

  | qn | Tuba | Basses |
  |---|---|---|
  | 116 | -2.1 dB | -6.6 dB |
  | 120 | -3.8 dB | -8.2 dB |
  | 560 | -6.0 dB | -11.8 dB |

  On the other tuba notes the tuba's share is -10..-22 and the basses carry the band.
- The master's 30-100 minus 300-1k rises 3.4-6 dB on these notes against the bar before (560: -19.9 -> -13.9).
- The basses got an 87.3 Hz -10 dB bell for the same F2 resonance in c24. The tuba has only a 70 Hz -4 dB low shelf, plus an E2 pitch trim of -4 (`pitch_trims.json`; the `_doc` there still says +5.1).

**Fix.**
- `build/mix.json` Tuba `eq` += `{"band": "bell2", "hz": 84, "db": -5, "bw_oct": 0.3}`, the same key form as the basses' bell2.
- Simulated by band power: master 30-100 Hz re 300-1k at 116 / 120 / 560 goes from -18.8 / -14.8 / -13.8 to about -21.6 / -16.3 / -14.8. The tuba's K body changes by under 0.5 dB (inferred: the bell sits below its 100-300 Hz body).
- This needs a Tuba FX rebuild. Lowest priority.

## Do not touch

- The melody-over-horns margins in bars 26-32, 138-142 and 158-161.
- The trumpet trims and roles: Trumpet 1 carries the a2 theme at 167-170, and the Trumpet 2/3 pairs are within 2 dB.
- The percussion gains, shapes and timing: tam-tam 484/696, crash, and the suspended-cymbal lead.
- `TIMP_CC1_MAP` and the roll shapes.
- The c25 Bass trombone and Horn 4 f/fff trims (finding 3 changes only Horn 4's ff value).
- The c18 letter-G theme lift (+2.5 on Violins I, Flute 1, Oboe 1) and `ARRIVAL_WEIGHT_AT` 484.
- The Violas 429 tenuto trim and the Flute 1 436 trim.
- The coda balance (bars 171-182).
- The climax order 160 > 122 > 167-170 > bar 26. None of the fixes reorders it; the largest master change is -0.7 dB in bars 117-121.

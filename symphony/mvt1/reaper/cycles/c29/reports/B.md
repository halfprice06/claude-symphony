# Cycle 29, critic B: balance and levels (render c28)

## Method

All numbers come from `cycles/c28/render/` (the stems and master after the c28 stem fix). Notes, dynamics and envelopes come from `build/parts.json`, `build/roles.json`, `build/pitch_trims.json`, `build/mix.json` and `build/mockup-events.tsv`.

Each stem and the master got a 10 ms envelope (2048-point STFT, stereo power), A-weighted, approximately K-weighted, or limited to a band. "re M" means stem minus master over the same window. Per-note levels are taken on the note body (onset + 0.03..0.15 s to the note end, at most 0.5-2 s). Below mf I judge balance in A and quote K where it matters, as c28 B did. Simulations add (gain - 1) x stem to the master in the sample domain, which is exact for level-only changes.

Score pages checked: 2-5, 8-11, 14-18.

## What holds (measured)

- **Dynamic mapping between families.** I compared same-dynamic sustained notes that sound together (overlap of at least 0.5 qn, no hairpin; medians in A):
  - Trumpets against trombones: f -0.3, ff -1.0, fff -0.1 dB.
  - Trumpets over horns: +4.2 / +2.6 / +2.0.
  - Trumpets over single woodwinds: +4.2 / +4.1 / +3.1.
  - Rimsky-Korsakov (Principles, "Comparison of resonance", text p. 51) gives trumpet = trombone = 2 horns = 4 woodwinds in forte, and "fairly equal balance" for all winds in piano.
  - At pp, horns sit -0.8 against woodwinds and trombones -1.7. At p, horns sit -2.5.
  - The new trumpet tracks therefore sit where the norms put them. On sustained notes of 0.8 s or more, every track's K ladder rises from p to fff.
  - The apparent pp outlier for the trumpets (Trumpet 1 at -33 A) is the bars 113-115 crescendo, not a mapping error.
- **Timpani.** Timpani sit under the strings, horns and trombones at the same dynamic (A: -3 against woodwinds, -4 against horns, -9..-14 against Violins I at f/ff). No roll is the loudest stem except in the solo bars 1-4.
- **Percussion.**
  - Crash at 636: in the 6-14 kHz band it carries -2..-3 dB of the master over the first 0.5 s and -8 at 1 s.
  - Suspended-cymbal roll: -9 -> -2.5 dB of the master 4-12 kHz band over its last 0.5 s.
  - Tam-tam 484: the top stem of bar 122 (-8.5 A re M).
  - Tam-tam 696 (pp, soft stick): -15 A re M at the stroke, a low hum.
  - All of this matches the printing.
- **Celli loud EQ (the c28 C #3 test).** On the loudest 10% of 0.4 s frames, master 160-250 Hz minus 500-2k is:

  | Render | 160-250 minus 500-2k (dB) |
  |---|---|
  | c27 | -8.3 |
  | c28 | -6.9 |
  | Dvořák 9/i reference | -4.4 |

  By this measure the test does not make the loud tuttis boxier than the reference (inferred). Keep it unless a listener objects.
- **Dan's checks.**
  - Loop pulsing: the master's 100-300 Hz autocorrelation at 3.95 s is -0.03 (bars 1-4), -0.31 (175-178) and -0.40 (179-182). Every string stem in 179-182 sits between -0.08 and -0.19, so there is no pulsing.
  - Accents: the median 2-5 kHz front (first 80 ms) minus body on f+ accents is -3.0 / -1.6 / -2.5 dB for Trumpets 1/2/3, -2.5 for Trombone 1 and -1.6 for Horns a2. None reaches the 7-13 dB burst Dan heard.
  - All fixes below are level-only, so they do not touch either check.

## 1. Bars 103-106 (qn 408-424): the mf counter-line in Horn 1, Bassoon 1 and celli sits 5-9 dB under the f oboe/clarinet figure (measured; fix simulated)

**Where.** Score p. 9.
- Ob 2 and Cl 1-2 a2 play the accented f figure.
- Hn 1, Bn 1 and Vc play the long slurred mf line in octaves, F4-E4-D4, B♭4-A4-G4, climbing to E5.
- Hn 3-4 hold mp harmony, B.cl. and Cb (pizz.) play f.

**Evidence (A, re M).**
- Per 2 qn window:
  - Figure group (Ob 2 + Cl 1 + Cl 2): -4.1, -1.2, -2.2, -4.8, -1.5, -1.6, -3.9, -2.0.
  - Counter-line group (Hn 1 + Bn 1 + Vc): -9.2, -9.9, -7.9, -5.4, -9.9, -9.7, -3.4, -6.0.
  - So the gap is 5-9 dB in six of the eight windows.
- Per voice: Horn 1 sits at -13..-16 through 408-419, Bassoon 1 at -12..-18 and celli at -10..-17, against Clarinet 1 at -2..-7.
- In K the group gap is still 2-6 dB.
- The line carries the passage's melodic counterpoint. It has three instruments against the figure's two lines, and its printed mark is only one step softer. By Rimsky-Korsakov's forte ratios (one horn = two woodwinds; the cello section = two woodwinds) it should sit 2-4 dB under the figure, not 5-9 (inferred).
- Part of the cause: Horn 1's F4 at 408 is played with the c15 F4 pitch trim (`pitch_trims.json` Horn 1 "65" body -4.5). No role row covers 408-424 for any of these tracks.

**Fix.** `build/roles.json`, level only, so it can go in by stem fix:
- Horn 1 `[407.5, 419.5, 3.5, 0.5]`. Stop at 419.5: the climb to E5 at 420 already reaches -4.6 re M.
- Bassoon 1 `[407.5, 423.5, 3.5, 0.5]`.
- Violoncellos `[407.5, 423.5, 3.5, 0.5]`. The celli `[360, 408, -3]` row ends here and is not changed.

**Simulated (A, re M, 2 qn windows).**
- Horn 1 -13.8/-16.0/-12.4/-12.1/-14.7/-13.1 -> -11.0/-13.0/-9.7/-9.6/-11.8/-10.9.
- Bassoon 1 -14.5..-8.0 -> -11.8..-5.6.
- Celli -13.5..-11.2 -> -10.7..-8.5.
- Clarinet 1 -8.9..-3.0 -> -9.6..-3.6.
- The figure stays on top by 2.5-5 dB per voice. Master +0.5..+1.1 dB over bars 103-106, no new loudest moment.

## 2. Bars 115-116 (qn 456-463.5): the flutes' a2 and Oboe 1's f entry with the tune sit 7-12 dB under Violins I and under the pp-cresc trumpets (measured; fix simulated)

**Where.** Score p. 10.
- Fl 1-2 a2 enter f at bar 115 on the tune (D♭6 C6 D6 E♭6, then D6 held into the ff of letter G), in unison with Violins I.
- Ob 1 enters f an octave lower, on the same pitches as Trumpet 1.
- Violins I have been in mp cresc since bar 111. The trumpets play pp cresc from bar 113 and reach ff at bar 116.

**Evidence (re M, per quarter, 456-462).**
- A: Flute 1 -16.4..-20.9, Flute 2 -16.4..-24.3, Oboe 1 -12.6..-18.9, against Violins I -7.3..-10.3 and Trumpet 1 -7.7..-11.5.
- K: Flute 1 -18.4..-22.5, Violins I -9.3..-12.0.
- The two flutes together sit about 6 dB under Violins I. Rimsky-Korsakov's forte ratio (Violins I = 2 flutes) puts them level with Violins I.
- The same Flute 1 doublings elsewhere sit -1.5..-4.1 dB under Violins I (c28 B table).
- c28 fixed letter G from 463.5 on. These two lead-in bars are now the outlier.
- Cause: the flutes' f trim is -4 dB (`mix.json` Flute 1/2 `dyn_trim_db` f -4, ff -1). On the printed f the flutes play their f layer while Violins I and the trumpets are already high in their crescendos.

**Fix.** `build/roles.json`:
- Flute 1 and Oboe 1: move the start of the c28 rows `[463.5, 479.5, 4.0, 1.5]` back to 455.5, giving `[455.5, 479.5, 4.0, 1.5]`. One continuous row, so the two ramps do not stack at 463.5-464.
- Flute 2: add `[455.5, 463.5, 4.0, 0.5]`.

**Simulated (A, re M).**
- Flute 1 -16.4..-20.9 -> -12.8..-17.4.
- Flute 2 -16.4..-24.3 -> -13.0..-20.4.
- Oboe 1 -12.6..-18.9 -> -9.4..-15.1.
- Violins I -7.3..-10.3 -> -7.5..-10.9. They stay the top string line, now 2-4 dB over the flute pair.
- Trumpet 1 moves 0.3-0.6 dB.
- Master +0.2..+0.7 dB, and the crescendo into 117 still rises.

## 3. Whole movement: the double basses' F1 and F2 play 3-7 dB under their neighbours, and G1 plays 2 dB over (measured)

**Where.**
- Every Cb F1 (MIDI 29) and F2 (41), for example:
  - bars 19-22 (qn 72-82, mf);
  - bars 140-141 (560-561.5, ff eighths);
  - bar 138 (552-553.5, f).
- G1 (31): bars 16, 18, 21-22, 82-85, 132, 134.

**Evidence (K, note body against the median of the neighbouring notes at the same printed dynamic, other pitches).**

| Pitch | n | Median | IQR |
|---|---|---|---|
| F1 (29) | 10 | -3.6 | -5.6..-2.1 |
| F2 (41) | 18 | -3.1 | -5.5..-1.2 |
| G1 (31) | 28 | +2.2 | +1.0..+3.3 |

- In bars 19-21 the F1 notes sit at -42.5..-44.0 K against G1 at -34.6..-37.8 and C2 at -35.9..-41.7. That is 7 dB within one mf bass line. In A the gap is 3-5 dB.
- At 560-561.5 (ff) F2 sits at -38.2 K against D♭2 at -30.3..-33.2 and D2 at -32.0..-33.6.
- The spectrum explains it:
  - On these notes the second harmonic carries most of the stem: G1's 98 Hz holds about 80% of the 30-2000 Hz energy, F1's 87 Hz about 44%.
  - The c24 basses bell2 (87.3 Hz -10 dB, 0.15 oct) sits on F's 87 Hz partial.
  - When the bell went in, F2's pitch trim had already been set to 0 (c18, against the earlier 87 Hz -6 bell). F1 never had a trim.
  - G1's 98 Hz partial sits on the resonance that c28 trimmed on G2 (43), but G1 itself has no trim.
- No other low track is uneven. Celli, tuba, contrabassoon and bass trombone have no pitch beyond ±2.4 dB.
- A real section plays the F and G of one line at one level. Here the bass line sags on every F and leans on every low G (inferred as audible, since the gap reaches 7 dB in bars 19-21).

**Fix.**
- `build/pitch_trims.json` Double basses: `"29": 3`, `"41": 3`, `"31": -2`. `_all_arts` is already true.
- A broadband trim keeps each note's spectral shape. The c24 F2 measure (60-100 minus 160-300 Hz on the note) is unchanged, while the note level returns to its neighbours.
- Expected master change: about +0.1..+0.4 dB on the F notes and -0.1..-0.3 on the G1 notes (the basses sit at -8..-22 K re M there). It can be applied by stem fix.
- Re-measure the per-pitch medians after the render. Target: F and G1 within ±1.5 dB of their neighbours.
- Leave A♭1 (`"32": -3.5`) as it is. It now reads -2.4, so it is at most 1-2 dB overcut, which is not worth a change this cycle.

## 4. Bar 40 (qn 156-160): the f trombone chord is level with the mf-crescendo melody it accompanies (measured; fix simulated)

**Where.** Score p. 4.
- Violins I, Flute 1 and Oboe 1 play the melody, mf cresc. into the accented note and the sixteenth run to the sf of bar 41.
- Trombones 1-2 and the bass trombone hold an f whole-note chord. Horns 3-4 and the strings are also f.

**Evidence (A, re M, per half quarter, 156-159.5).**

| Track | re M |
|---|---|
| Trombone 1 | -8.9..-12.3 |
| Trombone 2 | -7.9..-10.3 |
| Violins I | -9.0..-11.5 |
| Flute 1 | -5.9..-11.9 |
| Oboe 1 | -9.3..-18.8 |

- So each trombone voice sits at or above each melody voice. Trombone 2 is the top stem of the bar (-9.2 re M over the bar against Violins I -9.8).
- Printed f against mf cresc. allows the brass to be strong, but the tune should stay on top (Dan's item 2). Rimsky-Korsakov's forte ratio has a trombone equal to two woodwinds, so a trombone chord at full f covers a single flute/oboe line unless it is balanced down (inferred).

**Fix.** `build/roles.json` Trombone 1, Trombone 2, Bass trombone `[155.5, 159.75, -3, 0.2]`. End before 160 so the sf stab at bar 41 keeps its level.

**Simulated (A, re M).**
- Trombone 1 -8.9..-12.3 -> -11.2..-14.8.
- Trombone 2 -7.9..-10.3 -> -10.1..-12.8.
- Violins I -8.4..-10.9 and Flute 1 -5.7..-11.3, now 1.5-3 dB over each trombone.
- Master -0.5..-0.9 dB in bar 40. That widens the step into the sf of bar 41 (bar 41 is 2.2 dB over bar 40 now).

## Smaller observations (not ranked as findings)

- **Bar 143 (qn 568-569).** The ff wind/brass eighth-note stab is played 0.6 qn. Its tail (Trombones -7.8..-8.5 re M at 568.5) covers the Violins I f pickup at 568.5 (-18.3 re M). A hall would mask part of it as well. Shortening this stab is an articulation question for critic A.
- **Coda 175-177.** Clarinet 1's pp line sits 1.6-5 dB over each chorale voice (K). That is soft but audible. I left the c26/c07 coda balance as it is.

Do not touch: the trumpet levels against trombones/horns/woodwinds (all four dyn trims), the timpani and percussion levels (crash and suspended-cymbal shapes, tam-tam rows), the c28 celli loud_eq bell2 test with its -0.8 roles, the c28 basses G2/A♭2 trims with their skip list and the c24/c27 basses bells, the c28 letter-G Flute 1/Oboe 1 rows (extend them, do not replace them), the coda chorale balance, and every c28 do-not-touch item.

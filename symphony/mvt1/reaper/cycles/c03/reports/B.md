# Cycle 3, critic B: balance and levels (render c02)

## Method

I measured the stem-fixed render in `cycles/c02/render/` and its delivered mp3.

- Levels are K-weighted stereo power on 25 ms hops.
- Note bodies run from onset +0.08 s to min(end, +1.0 s).
- "A minus B" is the median, over A's note bodies, of A's level minus B's level in the same window.
- Per-pitch residuals are each note's body minus its volume envelope (`build_reaper.vol_points`), fitted against CC11 per track. They show the sample's own deviation; the net deviation is the residual plus any pitch trim.
- Simulations use `sim3.py`. Roles are applied as in `sim2` (0.5 qn ramps). `dyn_trim_db` changes are applied as the difference between `vol_points` on the old mix and on a scratch copy of `mix.json`. Pitch trims are steps over the notes' spans.
- Each simulation is the c02 master plus the changed stems, run through `tools/deliver_master.py`.
- With no change it reproduces c02 exactly: LRA 15.2 LU, span 19.9 dB, limiter 1.9 dB.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c03-B/`: `invert.py` (accompaniment louder than a voice printed louder), `pair.py`, `samedyn.py`, `steps2.py`, `unis.py`, `pitchmed2.py`, `topq.py`, `timp.py`, `macro2.py`, `hf.py`, and `sim3.py` with the specs `s1`-`s6.json` and `all.json`.

## The c02 roles worked (measured, melody minus accompaniment)

| Bars | Pair | Margin (dB) | Target / note |
|---|---|---|---|
| 15-18 | Violins I over celli | +4.7 | was -3.7 |
| 27-32 | Violins I over celli | +7.1 | |
| 111-116 | Violins I over Violins II | +3.2 | |
| 117-120 | Violins I over Trombone 1 | +2.0 | |
| 140-142 | Violins I over Trumpet 1 | +3.6 | |
| 158-161 | Violins I over Trombone 1 | +7.3 | |
| 167-170 | Violas over Violins II | +2.4 | was -8.1 |
| 56-66 | Violins I over harp | +5.2 | |

The climax order holds: delivered bar 160 -9.5, bar 122 -10.9, bar 169 -12.0 LUFS short-term.

The flute mf anchor worked: Flute 1 mf -41.5 dB, Oboe 1 mf -41.7 dB.

## 1. Crescendo pedals cover the theme: Clarinet 1 in bars 127-130 and the tuba in bars 111-114

**Bars 127-130 (qn 504-520), measured.** The score has the Clarinet 1 theme (p with an accent, < to mf at bar 129) over a G pedal that grows from pp through mf to f: Horn 4, timpani roll, celli and basses.

The clarinet is under the pedal throughout:

- Bars 127-128: Horn 4's pp pedal -42.3 / -40.0 dB per 2 qn, Clarinet 1 -45.9 / -47.8 dB.
- qn 504-512: Clarinet 1 is 5.5 dB under Horn 4, 4.8 dB under the basses and 1.8 dB under the timpani.
- Bar 129 (qn 512-516, Clarinet 1 mf, pedal mf): Clarinet 1 is 11.2 dB under Horn 4, 10.3 under the celli and 7.7 under the timpani.
- Solo minus everything else over bars 127-133: median -16.1 dB.
- Horn 4 is the loudest stem in bars 127-129. Bars 127-128 are among the delivered file's 10th-percentile bars.

The cause, from the data:

- The pedal tracks carry the pp soft trim of +7 dB, then CC11 and hairpin dB ramps. Horn 4's envelope is +3 dB at pp.
- Clarinet 1's override is only p +2 (`mix.json` soft_trim_db), and here it plays in its weak low register (G3-Eb4).
- A printed pp pedal therefore sounds over a printed p solo.

**Bars 111-114 (qn 440-456), measured.** The tuba's pp crescendo pedal (F2-D2) is the loudest stem in bars 112 and 114.

- It measures -32.9 / -34.3 / -31.4 dB at qn 444 / 446 / 452, against the Violins I mp melody at -33.7 / -34.7 / -34.0 and the p horns at -38 to -41.
- The tuba's E2 (40) has a +5.1 dB residual.

**Fix: `build/roles.json`.**

- Clarinet 1 `[504, 520, 5]`
- Horn 4 `[504, 518, -4, 2]`
- Timpani `[504, 518, -3, 2]`
- Violoncellos and Double basses `[508, 516, -2, 2]`
- Tuba `[440, 456, -5, 2]`, released into the ff at qn 460

Expected result:

- Bars 127-128: Clarinet 1 about 3 dB over Horn 4.
- Bar 129: Clarinet 1 roughly level with each pedal voice.
- Bar 130: the theme passes to Bassoon 1 and Violins II at f, so no change is needed there.

Simulated delivery: LRA 15.2 LU, span 20.0 dB, limiter 1.9 dB. The delivered file does not move.

## 2. Hot pitches on the second players of a shared patch were never trimmed; Horn 3's C5 sets the master peak

c02 trimmed hot pitches on the first players only. The same patch, played by the second player, shows the same deviations untrimmed (measured; residuals against each track's own CC11 fit).

**Horn 3, C5 (72): +4.9 dB.** This is Horn 1's +5.1 pitch, which has a -5 trim.

- At the climax it is the loudest stem at qn 631 (-20.1 dB, over Violins I -23.8, Horn 1 -23.5 and Trumpet 1 -24.8). It is level with the Trumpet 1 melody over bars 158-161 (Trumpet 1 minus Horn 3: -0.2 dB).
- At the master's top peak (qn 637.77, 1.220) Horn 3 contributes 0.268, the second-largest share after Violins I (0.342).

**Flute 2, Eb6 (87) +9.7, F6 (89) +5.3, G6 (91) +9.4 dB.** Flute 1 has 91 at -5; Flute 2 has no trims.

- In unison with Flute 1, Flute 2 is +7.3 dB over it on Eb6 and +7.1 on G6.
- At qn 635 Flute 2's G6 measures -17.5 dB: level with all of Violins I and 7.2 dB over Flute 1 on the same note.

**Others.**

- Tuba E2 (40) +5.1 dB (finding 1).
- Clarinet 2 Ab4 (68) -5.3 dB. Clarinet 1 has +5 on this pitch. Its long notes are in bars 26 and 138-141.
- Cor anglais A4 (69) +6.1 dB, +10 on the bar-152 note at qn 604. Kit LEARNINGS 13 found English horn A4 at +9.

**Fix: `build/pitch_trims.json`.** Flute 2's Ab6 (92) is not trimmed: at qn 637 it is already 2.7 dB under Flute 1.

```
"Horn 3": {"72": -5, "_all_arts": true}
"Flute 2": {"87": -5, "89": -3, "91": -6, "_all_arts_pitches": [91]}
"Clarinet 2": {"68": 4, "_all_arts_pitches": [68]}
"Cor anglais": {"69": -5}
"Tuba": {"40": -4}
```

Simulated:

- Horn 3 alone: master peak 1.220 -> 1.158, limiter 1.9 -> 1.5 dB.
- The whole set: peak 1.138, limiter 1.3 dB, LRA 15.2 LU, span 19.8 dB.

Re-check Horn 3's C5 at qn 630-638 after the render: it is an a2 note, so it should still sit about 1-3 dB under Violins I.

## 3. Second theme, bars 63-66: held accompaniment covers the Clarinet 1 counterline and the flute doubling

Measured, qn 248-268. In the score:

- Violins I/II have the f melody, doubled by Flute 1 ("1.", mf).
- Clarinet 1 (mf) and Horn 2 (mp) have the espressivo counterline in unison.
- Horns 3 and 4 hold mp chord tones, Bassoon 2 holds mp notes, and the harp plays mf arpeggios.

The measurements:

- Clarinet 1 is 8.3 dB under Horn 3, 5.5 under Bassoon 2, 4.1 under the harp and 2.8 under Horn 4.
- Horn 3 is the second-loudest stem at qn 252 and 254 (-32.6 / -35.9 dB). It is only 3.7 dB under the Violins I f melody, which should be two printed levels above it.
- The Flute 1 mf doubling is 5.7 dB under Horn 3 and 8.4 under Violins I.
- The `invert.py` scan of printed-louder voices sitting under printed-softer ones flags this passage: Clarinet 1 mf under Bassoon 2 mp by 6.8 dB and under Horn 3 mp by 7.2 dB.
- The c01 counterline roles (Clarinet 1 +3 and Horn 2 +2 at qn 220-244) end before bar 62.

**Fix: `build/roles.json`.**

- Horn 3 and Horn 4 `[248, 268, -4]`
- Bassoon 2 `[252, 264, -3]`
- Clarinet 1 `[252, 262, 3]`

Expected margins:

| Pair | Before | After |
|---|---|---|
| Clarinet 1 against Horn 3 | -8.3 | about -1 |
| Violins I over Horn 3 | +3.7 | about +7.7 |

Simulated delivery: unchanged (15.2 LU, 19.9 dB, 1.9 dB). The harp is still the loudest stem at qn 258-262 (-36.4 / -33.7 against Violins I -36.8 / -34.0). If the actor wants it lower, end the existing Harp role at 268 with -5 instead of -3 from qn 256 (inferred).

## 4. ff tutti: brass harmony and an a2 horn still level with or over the melody in bars 28, 82 and 116-117

Measured:

- **Bar 82 (qn 324-332).** The Violins I ff melody (G5-Eb7 run) is only +0.6 dB over Trombone 2 and the bass trombone and +2.3 over Trombone 1. The trombones hold harmony half and whole notes. Trombone 2 is the loudest stem at qn 326 (-24.7 dB).
- **Bar 28 (qn 108-112).** Horn 1 (a2, the F4 that is +2.9 dB hot) holds a harmony whole note at -24.7 dB, the loudest stem. Violins I measure -27.6 at qn 108 and -23.5 at qn 110 (Horn 1 -24.9).
- **Bar 116 (qn 460-464).** Trumpet 3's low D4, the bottom of a ff trumpet chord, is the loudest stem at qn 460 (-24.6 dB). It is louder than Trumpet 1 (-26.5) and Violins I (-24.8). The cause is Trumpet 3's ff trim of 11 dB against 8 dB on the others; at the same onsets Trumpet 3 elsewhere sits 1-2 dB under Trumpets 1/2 at ff, so this note is the outlier.
- **Bar 117 (qn 464-468).** Horn 1's a2 G3 is the loudest stem at qn 466 (-25.1 against Violins I -25.8).

Kit LEARNINGS 13 targets 3-5 dB of melody margin over held harmony at ff.

**Fix: `build/roles.json`.**

- Trombone 1, Trombone 2 and Bass trombone `[324, 332, -3]`
- Horn 1 `[104, 112, -3]` and `[464, 472, -2]`
- Trumpet 3 `[456, 464, -3]`

Simulated: LRA 15.3 LU, span 20.0 dB, limiter 1.9 dB. Bar 82's delivered maximum falls -12.3 -> -12.7 LUFS, which takes it further under bar 169.

## 5. Low and middle woodwinds barely grow from f to ff: their ff trims are below their f trims

Measured. These are within-track, pitch-matched steps from printed f to printed ff, on single notes of 0.6 qn or more:

| Track or family | f to ff (dB) |
|---|---|
| Bassoon 1 | +0.6 |
| Bass clarinet | +0.5 |
| Contrabassoon | +2.6 |
| Bassoon 2 | +2.9 |
| Clarinet 1 | +3.0 |
| Flutes and oboes | +5.2 to +6.2 |
| Brass | +5.3 |
| Strings | +4.5 |

The cause is in `mix.json` `dyn_trim_db`. These tracks taper down from their f anchor (CC 88) to their ff anchor (CC 114), and that cancels most of CC11's top-layer growth (about 1.2-1.8 dB per 10 CC on winds, kit LEARNINGS 4):

- Clarinets 1/2 and bass clarinet: f -1.5, ff -3
- Bassoon 1: f +1.5, ff -0.5
- Bassoon 2: f 2, ff 0
- Contrabassoon: f 0.5, ff -2

The flutes (-4 / -1) and oboes (2 / 4) rise instead.

Where a listener hears it: in the ff recapitulation theme, bars 131-134 (qn 520-536), clarinets 1/2 and bassoons 1/2 play the theme in unison with the trombones (f) and celli (ff).

- The four woodwinds together sum 8-9 dB under that theme group (winds -32.5 to -33.6 dB per bar, theme group -24.1 to -27.6).
- Rimsky-Korsakov's ratio (one trombone about four woodwinds) puts them about 3-4 dB under (inferred).
- In bar 134 the theme group is 3.6 dB under the upper ff counterline (flutes, oboes, violins).

**Fix: `build/mix.json` `dyn_trim_db`.**

- Clarinet 1, Clarinet 2, Bass clarinet: ff -3 -> 0
- Bassoon 1: ff -0.5 -> 2.5
- Bassoon 2: ff 0 -> 3
- Contrabassoon: ff -2 -> 1

Each is then the f value plus 1 to 1.5 dB.

Simulated: theme group +0.5 / +0.5 / +0.8 / +1.2 dB in bars 131-134; delivered LRA 15.2 LU, span 20.1 dB, limiter 1.5 dB (it does not raise the climax peaks). A level-only change; it can go in with `stem_fix.py`.

## 6. Middle dynamics are compressed: printed mf and f differ by 1.6 LU in the delivered file

**Measured.** Per-bar level grouped by each bar's loudest printed dynamic (bar counts in brackets):

| Dynamic | Master (dB) | Delivered (LUFS momentary, power mean) |
|---|---|---|
| ppp (2) | -41.9 | -31.3 |
| pp (11) | -36.2 | -26.9 |
| p (23) | -33.9 | -28.3 |
| mp (14) | -31.8 | -25.5 |
| mf (35) | -30.9 | -24.6 |
| f (38) | -27.2 | -23.0 |
| ff (52) | -19.3 | -18.2 |
| fff (7) | -12.2 | -11.5 |

- From p to f the delivered file spans 5.3 LU, against 4.8 LU for f to ff and 6.7 LU for ff to fff.
- The pp bars come out louder than the p bars: the ride is at its +10 dB cap in both.
- Within tracks (pitch-matched, single notes):

| Family | p > mp | mp > mf | mf > f |
|---|---|---|---|
| Winds | +2.1 | +0.8 | -0.1 |
| Strings | +1.7 | +1.8 | +1.1 |

**Two causes.**

- Measured: the soft-trim taper from p (+5) to each track's f trim removes 3.5-6.5 dB across p to f.
- The delivery ride (2.5:1 under its knee) then divides what is left. A 3.7 dB mf-to-f step in the master comes out as 1.6 LU.

Whether a listener hears mf and f as the same level is inferred. The numbers say printed f bars are only 1.6 LU over mf bars.

**Fix to test.** Raise every wind and string track's `dyn_trim_db` "f" by +2 and leave "ff" alone, so only the mf-to-f range widens.

Simulated: delivered mf -24.4, f -22.2 (mf to f 2.2 LU), ff -18.5; LRA 15.1 LU, span 19.9 dB, limiter 1.6 dB. This is a small gain. A larger one needs a change to the ride's knee or ratio, which belongs to critic C's lens.

If the actor takes findings 2 and 5, the f trims of the bassoons and clarinets change in the same file: apply this +2 on top of those values.

**All of findings 1-5 together, simulated:** LRA 15.3 LU, span 19.9 dB, limiter 1.4 dB, master peak 1.181. Delivered maxima: bar 160 -9.6, bar 122 -10.8, bar 159 -11.7, bar 169 -12.0, bar 82 -12.7 LUFS.

## Dan's two listening checks (no finding, measured)

**Loop pulse.** Autocorrelation at 3.95 s of the 100-300 Hz level and the spectral centroid:

| Passage | Stem | Level | Centroid |
|---|---|---|---|
| Final chord, qn 712-728 | Master | +0.05 | +0.06 |
| Final chord, qn 712-728 | String stems | -0.22 to +0.21 | |
| Tam-tam, qn 484-500 | Master | -0.48 | |
| Coda chorale, qn 696-712 | Celli, Trombone 1 | at most +0.16 | at most +0.20 |

All are under movement II's 0.39-0.63 problem level.

**Accents.** 2-5 kHz in the first 80 ms minus the body, accented notes, median (p90):

| Stems | Median (p90), dB |
|---|---|
| Trumpets | +0.6 (+2.5) / +0.1 / -2.8 |
| Trombones | -2.9 / -1.7 / -1.1 |
| Horns 1/3 | -0.5 (+3.1) / -1.7 |
| String sections | -2.3 to -0.4, p90 at most +4.3 (Violas) |
| Woodwinds | -3.8 to -1.1 |

None is near the 7-13 dB burst.

## Do not touch

- The c02 roles listed above, the climax order (bar 160 over 122 over 169), and FFF_HOLD_CAP.
- The trumpet `dyn_trim_db` values other than the bar-116 role: Trumpet 3 sits 1-2 dB under Trumpets 1/2 at f/ff, and the trumpets are 2-5 dB under the trombones and 1-3 dB over the horns at ff.
- The brass and woodwind GENTLE_ACCENT.
- The crash level. At qn 636 the crash carries the master's 5-20 kHz band (-1.5 to -2.8 dB under the master's level in that band) while sitting 8 dB under it in 2-5 kHz.
- The tam-tam fff (6 dB under the master in 2-5 kHz in its first half second).
- The global soft trims 7/7/5.
- The basses' level and EQ: 20-100 Hz share -15.6 dB, 100-250 Hz -9.1 dB, slightly light and not boomy.
- The opening and bar-76 timpani roles.
- The Flute 1/2 mf anchor.

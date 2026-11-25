# Cycle 4, critic B: balance and levels (render c03)

## Method

I measured the stem-fixed c03 render in `cycles/c03/render/` and its delivered mp3. The c03 time axis is correct, so score qn maps to file time through the parts.json tempo map with no shift.

- Levels are K-weighted stereo power on 25 ms hops.
- A note body runs from onset +0.08 s to min(end, +1.0 s), or +1.5 s where marked.
- "A minus B" is the median, over A's note bodies, of A's level minus B's level in the same window.
- The envelope is `build_reaper.vol_points` (roles, trims, hairpin gains and the mix dyn/soft trims). "Raw" means the body minus that envelope.
- Simulations use `sim3.py`: the c03 master plus role and pitch-trim changes on the stems, delivered with `tools/deliver_master.py`. With no change it reproduces c03 exactly: LRA 15.3 LU, span 19.9 dB, limiter 2.7 dB, peak 1.369.

Scripts and specs are in `/private/tmp/claude-501/mockup-loop/mvt1-c04-B/`:

- `notes.py`, `samedyn.py`, `pair.py`, `mfchk.py`: dynamics per track, same-onset comparisons, pairs.
- `fam.py`, `top.py`, `timpstroke.py`.
- `perc2.py`, `percspec.py`: percussion against the master by band.
- `lowstem.py`, `lowend.py`: low-end shares.
- `loop.py`, `acc.py`: Dan's two checks.
- `sim3.py` with `s_fff2.json`.

## Is p the same p in every family? (measured)

Body medians in dB K, all notes at each printed dynamic:

| Dynamic | Winds | Horns | Trumpets | Trombones / tuba | Strings |
|---|---|---|---|---|---|
| pp | -42.3..-46.5 | -41.3..-45.2 | -41.9..-45.4 | -42.8..-46.3 | -43.1..-44.1 (basses -47.6) |
| p | -40.9..-46.2 | -41.8..-43.7 | | | -39.1..-44.5 |
| f | -37.0..-39.1 | -35.0..-35.7 | -33.6..-34.6 | -31.0..-32.1 | -33.4..-38.8 |
| ff | -31.3..-35.1 | -29.1..-29.6 | -26.9 / -27.4 (Trumpet 3 -32.5) | -26.3..-30.5 | -25.7..-33.9 |

- From pp to ff the families agree within 2-3 dB at the soft dynamics.
- At f and ff they follow Rimsky-Korsakov's forte ratios (*Principles*, p. 33: trumpet = trombone = tuba = 2 horns, horn = 2 woodwinds). The same-onset gaps at ff:
  - Trumpet 1 is +2.0 over Horn 1 and +5.2/+6.5 over Flute 1/Oboe 1.
  - Trombone 1 is +2.3 over Horn 1 and +4.0/+6.5 over Oboe 1/Flute 1.
- The new trumpets fit the brass at f and ff. Trumpet 1 at f is 1.8 dB under Trombone 1 and 2.9 over Horn 1.

Three places break the pattern: fff (finding 1), the soft timpani strokes (finding 2) and Trumpet 3's lowest notes (finding 4).

The middle steps are small but not reversed. These are same-pitch medians with the envelope's share in brackets:

| Track | mp to mf | mf to f |
|---|---|---|
| Violins I | +1.1 dB (envelope -1.9) | +3.0 |
| Clarinet 1 | +2.3 | +0.8 |
| Flute 1 | +2.0 | +3.8 (envelope -3.7) |

The soft-trim taper (p +5 to each f trim) takes about 2 dB out of each step. That is the known trade-off against the delivered loudness range (c03 rejected B #6), so I propose no change there.

## 1. At both fff tutti the brass harmony sits level with or under single woodwinds; Bassoon 1 and Flute 1 are louder than the trombones

**Where:** bars 122-123 (qn 484-492, fff chord with tam-tam, no melody) and bars 160-161 (qn 636-644, fff climax).

**What is wrong (measured):** at fff the families are no longer in the ratio they hold at ff.

Stem levels at qn 636-644:

| Stem | Level (dB) | Note |
|---|---|---|
| Violins I | -17.5 | melody |
| Horn 1 | -22.0 | |
| Trumpet 1 | -22.5 | |
| Flute 1 | -22.8 | |
| Bassoon 1 | -24.3 | |
| Trombone 1 | -24.5 | |
| Bass trombone | -26.4 | |
| Trumpet 3 | -26.6 | |
| Trombone 2 | -27.7 | |
| Tuba | -27.9 | |

Stem levels at qn 484-492:

| Stem | Level (dB) |
|---|---|
| Flute 1 | -22.7 |
| Bass trombone | -24.5 |
| Trombone 2 | -25.4 |
| Oboe 1 | -25.8 |
| Trumpet 1 | -26.4 |
| Trombone 1 | -26.9 |
| Tuba | -29.3 |
| Trumpet 2 | -29.2 |

- At qn 488-492, Flute 1 (G6, -21.6) is 6.6 dB over Trumpet 1.
- The 10 brass sum to -18.1 dB at qn 484-492, against -17.3 for the 11 woodwinds and -16.3 for the strings.
- Rimsky's forte ratio puts one trombone about 6 dB over one woodwind. Here Trombone 1 is level with or under Flute 1 and Bassoon 1 at both fff points, while at ff it is 4-6.5 dB over them.

**Cause (measured from parts.json):** the crescendo dB gains held into the fff (`HP_GAIN_DB` wind 4 / string 3 / brass 2, `HP_CHAIN_RISE_FFF`, `FFF_HOLD_CAP`) and the c02 brass roles.

Envelope medians on the fff notes:

| Track | Envelope (dB) |
|---|---|
| Flute 1 | +5.5 |
| Oboe 1, Clarinet 1, Bassoon 1 | +4.0 |
| Horn 1 | +9.9 |
| Horn 3 | +6.0 |
| Violins I | +7.5 |
| Violoncellos | +6.0 |
| Trumpet 1 | +3.5 |
| Trombone 1, Tuba | 0.0 |
| Bass trombone, Trumpet 3 | -0.5 |

- At qn 638 Bassoon 1's envelope is +11.1 dB.
- At bar 122 the trombones have no printed hairpin into the fff, so they get no gain while the winds get +5.1.
- At bar 160 the +2 brass gain is cancelled by the c02 roles (Tbn1, Tbn2, BTbn, Tpt3 [628,644,-3]; Tuba -2).
- The samples add little on their own from ff to fff (raw, same tracks): Trombone 1 -0.1 dB, Trumpet 1 +0.9, Tuba +0.7.

A listener hears a climax led by strings and woodwinds, with the trombones and tuba as a background layer (inferred).

**Fix: `build/roles.json`.** Remove the c02 [628,644] brass cuts and add:

| Track | Rows |
|---|---|
| Trombone 1 | `[484,496,3,2]` |
| Trombone 2 | `[484,496,3,2]` |
| Bass trombone | `[484,496,2,2]` |
| Tuba | `[484,496,2,2]` |
| Trumpet 1, Trumpet 2 | `[484,496,2,2]` |
| Trumpet 3 | `[484,496,2,2]` |
| Bassoon 1 | `[628,644,-4]` |
| Bassoon 2 | `[628,644,-2]` |
| Flute 1 | `[484,494,-3]` |
| Flute 2 | `[484,494,-2]` |

The cuts to remove are Trombone 1/2 and Bass trombone `[628,644,-3]`, Tuba `[628,644,-2]` and Trumpet 3 `[628,644,-3]`. All of this is level-only, so it can go in with `stem_fix.py`.

**Simulated with finding 4:**

- Delivered LRA 15.3 LU, span 20.1 dB, limiter 2.7 -> 2.9 dB, master peak 1.369 -> 1.440 (same instant, qn 637.9, which Violins I and Horn 1 dominate).
- Climax order kept (delivered short-term maxima): bar 160 -9.6, 122 -10.5, 169 -12.0 LUFS.
- Master RMS +0.6 dB over qn 484-496 and +0.4 dB over qn 636-644.

**Expected levels:**

- qn 636-644: Trombone 1 -21.5, Bassoon 1 -28.3. The Violins I melody stays 4.0 dB over the loudest brass harmony stem, inside kit LEARNINGS 13's 3-5 dB.
- qn 484-492: Trumpet 1 -24.4, Trombone 2 -22.4, Flute 1 -25.7.

If the limiter must stay at 2.7 dB, add Flute 2 `[636,640,-2]`; Flute 2 is the third contributor at the peak sample.

**Generic alternative (inferred, not simulated):** brass 2 -> 3 in `HP_GAIN_DB` and 0.5 -> 1.0 in `HP_CHAIN_RISE_FFF`. It would not reach bar 122, which has no brass hairpin.

## 2. The coda timpani strokes (bars 179-180) are inaudible, and the bar-174 pp roll is 10-12 dB under the quietest strings

**Where:** Timpani, qn 712, 713.5, 714, 716, 717.5 and 718 (pp, soft sticks, the C-G-C figure at Tempo I), and the pp roll at qn 692.

**What is wrong (measured):**

- The six strokes peak at -53.0 to -60.9 dB K in their first 0.3 s.
  - The master is at -33.8 to -35.2 and the loudest string section at -39.0 to -44.4.
  - That puts the strokes 17-26 dB under the master and 9-20 dB under the loudest string.
  - Their bodies are -62 to -65.5 dB, 15 dB under the quietest section, the basses (-49 to -50.5).
- They play at velocity 56, which is the pp entry of the stroke-velocity map in `score_to_parts.py` (`(34, 56)`). Kit LEARNINGS 10 measured an 8-16 dB step between velocity 56 and 64 on the felt patch and says to use 60-64 for pp/p strokes that must be heard.
- The pp roll at qn 692-696 measures -53.4 / -56.1 dB against the violas at -43.1 / -44.6. That is 10-12 dB under the quietest section, against the kit target of 3-5 dB under. Its settle is -6 to -11 dB in the volume envelope.
- The final ppp roll (qn 720-728, -54.4 / -56.9) is level with the basses and is fine.

This figure is the timpani's only struck motif in the coda, answering the opening roll. As rendered it is not heard (inferred).

**Fix.**

- `build/score_config.py`: `TIMP_VEL = {712.0: 62, 713.5: 62, 714.0: 62, 716.0: 62, 717.5: 62, 718.0: 62}`. Keys are `round(n["qn"], 2)` before the `TIMP_DELAY_S` shift, which is the score onset for timpani.
- After the render, check that the stroke peaks sit 3-6 dB under the loudest string section (about -45 dB). Trim any excess with a step role, not a ramp (kit LEARNINGS 13, plucked/struck notes).
- `build/roles.json`: Timpani `[692, 696, 6]` for the bar-174 roll.

## 3. Bars 147-155: the cor anglais p answers sit under the pp Violins II tremolo

**Where:** Cor anglais, qn 586.5-620 (bars 147-155, printed p). The answers come against the mf dolce theme in the violas and celli and the Violins II pp div. sul tasto tremolo chord.

**What is wrong (measured):**

- Cor anglais minus Violins II, median over its 16 notes: -2.6 dB.
- Per note it ranges from -5.5 to -1.0 dB, except qn 604 at +2.7.
- On the held notes of bars 153-155 (qn 608-620) it is -2.9 / -0.7 / -5.5 / -5.2 dB.
- Cor anglais minus the theme: -7.3 against the celli and -6.3 against the violas.

A printed p wind voice sits under a printed pp accompaniment. Part of this comes from the c03 stem fix Violins II [584,619,+2], which restored the tremolo's level after the sul tasto EQ. The p answers do not come through between the theme's phrases (inferred).

**Fix: `build/roles.json`.** Cor anglais `[586, 620, 4]`.

Expected: about 1-3 dB over Violins II and 2-4 dB under the theme. The A4 at qn 604 (pitch trim -5) ends about 1.7 dB under the celli.

## 4. Trumpet 3's B3 is 4-5 dB under Trumpet 2 at ff/fff

**Where:** Trumpet 3, pitch 59 (B3), at qn 328 and 330 (bar 83, ff), 484 and 488 (bars 122-123, fff, the B natural of the chord) and 632 (bar 159).

**What is wrong (measured):**

- Same onsets, same printed dynamic: Trumpet 3 minus Trumpet 2 is -4.5 dB raw at ff (n=3) and -3.9 at fff (n=2). As heard it is -5.1 and -3.9.
- This is despite Trumpet 3's ff trim of 11 against 8 on Trumpets 1/2.
- Its other pitches are within ±1.2 dB of Trumpet 2 at f (n=23), and C4 (60) is -1.2 raw.
- At bars 122-123 the B3 is 6-7 dB under Trumpet 1 (-32.4 / -33.4 against -25.5 / -27.4). The trumpet chord is top-heavy where the score gives the lowest trumpet the chord's B natural.

**Fix: `build/pitch_trims.json`.** `"Trumpet 3": {"59": 4, "_all_arts": true}`. It is included in the simulation of finding 1.

## The new percussion tracks (measured, no change)

**Tam-tam fff (qn 484).**

- It is the loudest single stem in its first 0.5 s: -20.0 dB, against Violins II -20.4 and the master -11.2.
- 30-100 Hz: -1.5 to -4 dB under the master.
- Over 0.5-2 s: 9 dB under the master at 3-6 kHz and 11 dB under at 6-16 kHz.
- It decays to -41 dB (master -26) by +8 s and is damped at bar 127 as printed.

**Suspended cymbal (bar 159).**

- It is inaudible for its first 1.4 s, which is expected under the ff crescendo: 35-70 dB under the master in every band.
- In its last 0.3 s it rises to 6 dB under the master at 6-16 kHz and peaks 0.2 s before the crash.

**Crash fff (qn 636).**

- For 0.3 s it carries the master's 6-16 kHz band (-2.1 dB re the master in that band) and 3-6 kHz (-5).
- In K-weighted level it is 11-12 dB under the master, so it does not cover the tutti.

**Tam-tam pp (bar 175).**

- It is a low hum: 30-100 Hz within 1-5 dB of the master band, nothing above 3 kHz.
- K-weighted it is 9-14 dB under the master.

All four are plausible against real recordings (inferred), and none covers a melody.

## Dan's two checks (measured)

**Loop pulsing.** Autocorrelation at 3.95 s of the 100-300 Hz level and of the spectral centroid:

| Passage | Stem | 100-300 Hz | Centroid |
|---|---|---|---|
| Final chord, qn 712-728 | Master | -0.16 | 0.00 |
| Final chord, qn 712-728 | Each string stem | -0.11..+0.11 | -0.11..+0.12 |
| Opening roll, qn 0-16 | Timpani | +0.22 | +0.11 |
| qn 720-728 | Timpani | +0.16 | +0.11 |
| Tam-tam fff, qn 484-500 | Tam-tam | -0.08 | -0.36 |
| Coda chorale, qn 696-712 | Celli, Trombone 1 | at most +0.17 | at most +0.17 |

One exception: Horn 4's final ppp G3 (qn 720-728) reaches +0.93 / +0.70 with a 12 dB swing in 100-300 Hz. It sits 15 dB under the master in that band, so it is inferred inaudible. It is critic A's to judge.

**Accents.** 2-5 kHz energy in the first 80 ms minus the body, accented notes, median (p90):

| Stems | Median (p90), dB |
|---|---|
| Trumpets 1/2/3 | -4.4 (-0.3) / -11.5 / -13.4 |
| Trombones | -8.1 to -12.3, p90 at most -3.2 |
| Horns 1/3 | -3.0 (+2.6) / -0.8 (+2.8) |
| Strings | -2.9 to -3.0, p90 at most +2.7 |
| Woodwinds | -4.2 to -4.9, p90 at most +1.5 |

No accent is near the 7-13 dB burst.

## Do not touch

- The c03 roles that worked (measured on c03):
  - Clarinet 1 over the Horn 4 pedal in bars 127-128: +2 to +9 dB per 2 qn.
  - The bars 63-66 counterline: Clarinet 1 level with the harp and Horns 2/3.
  - Bar 82: Violins I 2-7 dB over each trombone.
  - The tuba under the bars 111-114 melody.
- The c02/c03 roles not named in finding 1, and the climax order (160 > 122 > 169).
- FFF_HOLD_CAP and HP gains for strings and winds. Finding 1 changes only the brass/wind balance at the two fff points, by roles.
- The trumpet `dyn_trim_db` values (f/ff balance with trombones and horns is right) and the a2 unison handling (+3 dB on the kept note).
- The percussion gains, keys and timing.
- The global soft trims 7/7/5 and the Flute 1/2 mf anchor.
- The basses' level and EQ. In loud frames the basses carry 30-100 Hz; 100-250 Hz is light against Dvořák (-14.9/-11.6 against -10.8/-8.0 dB), but that reference is lossy and the Brahms references are not on disk (kit LEARNINGS 14).
- The final ppp timpani roll role.
- Brass, wind and string GENTLE_ACCENT.

# Critic B, cycle 25: balance and levels (render c24)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for every c24 stem and the master. I mapped them to score qn with the parts.json tempo map and compared them with the printed marks (`build/mockup-events.tsv`, score pages 1-8) and with the control data in parts.json (cc11, cc7, vol_db, notes). Fixes were simulated by applying their dB to the stem frames. The scripts are in `/private/tmp/claude-501/mockup-loop/c25-B/`:
- `clim.py`: every stem's level per window, with its printed dynamic.
- `over.py`: accompaniment more than 3 dB over the melody.
- `famacc2.py`: family medians per dynamic.
- `band.py`, `mask.py`, `bandenv.py`: band shares, per-band masking and band envelopes.
- `beat.py`: fluctuation in the fundamental band.
- `pluck.py`: harp attacks.

## Delivery, c24 (ffmpeg ebur128 agrees with metrics.md)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.7 LU | 16.0 LU (target 14-16) |
| True peak | -3.9 dBFS | -1.6 dBTP |
| p10-to-max span | | 18.4 dB |
| Limiter | | 1.9 dB |

Finding 1 lowers the loudest cello frames at both climaxes by about 3 dB. That should lower the bar 61 master peak by up to 0.8 dB in 0.1 qn frames, and the bar mean by about 0.3 dB (inferred from the stem share). The other fixes touch soft passages and move the LRA and span by less than 0.2 (inferred).

## What holds (measured)

**The dynamic mapping agrees across families.** Accompaniment notes, median K:

| | winds | brass | strings |
|---|---|---|---|
| pp | -47.4 | -47.5 | -46.9 |
| p | -42.3 | -40.3 | -43.8 |
| mp | -37.4 | -39.4 | -41.1 |

Each step is 3-5 dB in every family.

**Every p solo sits at the same level.** Median K over each passage:

| Solo | Median K |
|---|---|
| Horn, bars 7-14 | -37.9 |
| Oboe, bars 15 and 19 | -38.6 / -37.8 |
| Solo violin | -37.4 |
| Flute, bars 37-40 | -39.4 |
| Cor anglais, bars 41 and 47 | -37.6 / -37.9 |
| Horn, bars 67-70 | -37.9 |
| Clarinet, pp coda | -40.7 |

The pp coda is 2-3 dB under the p solos, which is right.

**The climax balance follows Rimsky-Korsakov** (`reference-books/text/rimsky-principles.txt`, lines 1965-1990 and 1509-1517). In forte, a trombone or tuba equals 2 horns, and a horn equals 2 woodwinds or one violin section. Horns are marked one degree above the other brass to balance, as this score does at bar 61 (horns f, low brass mf). Measured, bars 61-62 (qn 204-212, K):
- Violins I: -21.7..-24.5.
- Each ff woodwind: -24..-28, which is 3-6 dB under Violins I (half a section).
- Horns f: -25.6..-28.4.
- Tuba mf: -23.2..-25.9, which is 2-3 dB under Violins I in K and 6-9 dB under in A.
- Trombone 1's ff marcato solo at bar 63: -18.9, which is 3 dB over Violins I at ff (two sections).

None of this needs a change.

**No accompaniment stem covers a soft solo** by more than 2 dB K, except the items below.

## 1. Bars 61 and 80: the cellos' A flat 3 is 4-6 dB hotter than their other f/ff notes. It is the loudest stem in both climaxes and bursts 5-7 dB over the ff violin melody (measured; sample cause inferred)

**Where.** Violoncellos, two notes:
- qn 204-206: bar 61 beats 1-2, A flat 3, ff, molto sostenuto.
- qn 265-267: bar 80 beats 1-2, A flat 3, f, the tenor counter-line.

**What.**

1. **Hot against the neighbouring notes.** Mean K over the first 2 qn of each note:

   | Note | A flat 3 | Neighbours | Excess |
   |---|---|---|---|
   | qn 204 | -21.4 | -24.6..-26.6 | +4.3 |
   | qn 265 | -22.5 | -28.0..-33.9 | +6.0 |

   The excess is not in the control data:
   - CC11 is the same on all these notes (119-122 at 204, 89-92 at 265).
   - At qn 265.9-266.0 vol_db is at +3.1, below its +3.5 at 265.8.

2. **Only the loud A flat 3 is hot.** The six A flat 3 notes at p/mp (qn 72, 81, 139, 244, 253) sit within 1 dB of their neighbours. The A flat 3 at qn 261 (f) already carries a -8 note trim from an earlier cycle. I infer that the f/ff layer of this one sample is hot.

3. **The excess pulses.** In `bandenv.py`, the 180-240 Hz band (the 208 Hz fundamental) swings 22 -> 45 dB with a period of about 0.45 qn, while the bands above 240 Hz stay within about 5 dB.

4. **Against the melody.**

   | Window | Vc | Vln I | Note |
   |---|---|---|---|
   | qn 204.1-205.9, mean | -21.4 | -22.6 | |
   | qn 265.1-266.9, mean | -22.5 | -24.0 | |
   | qn 204.9-205.2, 0.1 qn peak | -18.7 | | +5.7 over Vln I and Fl1 |
   | qn 265.8-266.2, 0.1 qn peak | -17.5 | | +6.8 over them |

   In metrics.md the Vc is the loudest stem of bar 80 (-26.7 RMS) and of bar 61 (-25.7 RMS).

5. **The printed marks.** At qn 265 the Vc is marked f under the ff tune (score p. 7). At bar 61 every string section is ff, and the cellos are an inner voice under the violins' top line.

**Fix.** `build/note_trims.json`, "Violoncellos": add `"204": -3` and `"265": -4`, next to the existing `"261": -8`. The default 0.6 s ramp is fine for these sustained notes.

**Predicted** (simulated on the stem frames):

| Note | Mean K now | With the fix | Vln I | Peak frame now | With the fix |
|---|---|---|---|---|---|
| qn 204 | -21.4 | -24.4 | -22.6 | -18.7 | -21.7 |
| qn 265 | -22.5 | -26.5 | -24.0 | -17.5 | -21.5 |

- At qn 204 the Vc ends 1.8 dB under Violins I.
- At qn 265 the Vc ends 2.5 dB under Violins I, and still 1.5-2 dB over its own other f notes, so the tenor line keeps the weight the c15/c16 fixes gave it.

If critic A proposes a notch shape for the pulse instead, use the same depth.

## 2. The three ppp timpani rolls (bars 2-3, 67-70 and 89-92) sit 14-23 dB under the rest of the orchestra and are masked in almost every band (measured levels; audibility inferred)

**Where.** Timpani, all three rolls are printed ppp:
- qn 3-8.5: A flat 2, the opening, under the strings' pp chord.
- qn 226-237.5: E flat 3, under the horn solo.
- qn 292-304: A flat 2, the final chord.

**What.**

1. **Level against the rest of the orchestra** (K, per qn):
   - qn 3: -53.3 against -39.2 for the rest (-14.1), then -20.5 by qn 6.
   - qn 226-237: -51.1..-58.1, which is 13-23 under.
   - qn 292-303: -55.4 -> -64.6, which is 16-21 under.

2. **Against the other ppp/pp stems** in the same bars (K):

   | | Timpani | Other stems |
   |---|---|---|
   | Opening | -53..-60 | Vc/Cb pp -45.9/-46.4 |
   | Final | -55..-63 | Cb/Vc pp -47..-49; Vc ppp in bar 92 -54.6 |
   | Median, whole piece | | string ppp -50.8 |

   The roll starts 2-4 dB under the strings' ppp and then falls 5-10 dB further.

3. **Masking** (`mask.py`, 1/3-octave bands, timpani minus everything else):

   | Band | qn 294-300 | qn 4-9 |
   |---|---|---|
   | 100 Hz (the fundamental, on the Vc/Cb A flat) | -24.8 | -25.0 |
   | 160 Hz | -10.4 | -19.9 |
   | 200 Hz | -12.9 | -12.2 |
   | 315-1000 Hz | -16..-26 | -16..-23 |

   Only the 125 Hz band is level (+1.6). I infer that the opening and closing rolls are not heard as timpani.

4. **Cause, from parts.json and the tools.**
   - The roll is printed ppp, which gives roll_db -36.
   - The c03 flat cut of -6 applies to every soft roll.
   - The 5 dB settle applies.
   - The track gain is -7.
   - The track is in `soft_trim_db._except`, so it never received the +3 dB ppp/pp lift that every other track got in c08.
   - The 292 roll's envelope goes from -8.0 to -17.0 by qn 303.25.

   The c03 cut was made when soft rolls sat level with the pp strings (about -48 K). They now sit 7-11 dB under them.

**Fix.** `build/roles.json`, "Timpani": add three rows. They do not overlap the existing rows (168, 277, 200, 261.5).
- `[3, 8.5, 4]`
- `[226, 237.5, 3]`
- `[292, 304, 4]`

Leave the settle and the f/ff rolls as they are.

**Predicted** (K):

| Roll | Now | With the fix | Reference |
|---|---|---|---|
| Opening | -53..-60 | -49..-56 | 3-10 under the pp basses |
| Horn solo | -51..-58 | -48..-55 | 15+ under the horn |
| Final | -55..-64 | -50..-60 | 3-8 under the bass strings, about 3 under the ppp Vc in bar 92 |

- Masking at qn 294-300: 125 Hz +5.6, 160 Hz -6.4, 200 Hz -8.9. The roll becomes a low halo under the chord and is never the loudest stem (BRIEF rule 5).
- The mp3's soft-passage lift and the LRA hardly move: the timpani is under 2% of the energy in these bars.

## 3. Bar 78 beat 3: the a2 horns' p < f pickup peaks a beat early. For 0.25 qn it is the loudest stem, 4.9 dB over the violin tune and over its own f arrival (measured)

**Where.** Horns 1-2 a2, the C4 pickup at qn 261-262 into bar 79. Printed p with a crescendo to the f of bar 79 (p. 6). Around it, Violins I/II, Fl1, Cl1, Bn2 and the low strings are f, in the poco allargando.

**What.**

1. **Horn K per 0.25 qn:**

   | qn | 261.25 | 261.5 | 261.75 | 262.0 (the f arrival) |
   |---|---|---|---|---|
   | Horn K | -34.7 | -29.5 | **-25.2** | -25.9 |

2. **The rest at qn 261.75:** Violins I -31.5 (the turn figure), Bn2 -31.5, Fl1 -30.9, Cb -30.2.
   - `over.py` flags qn 261.7-262.0 at +4.9 over the melody.
   - In A the horns are +3.6 over Violins I.

3. **Cause, in vol_db:** +2.0 at qn 261.25, +4.25 at 261.75, +6.0 at 262. Three things lift the pickup on top of the CC11 rise (54 -> 88):
   - The climax role `[262, 268, 4, 0.5]` ramps in over the fixed 0.5 qn before its start (qn 261.5-262).
   - The hpgain `[261, 262, 2]`.
   - The swell.

**Fix.**
- `build/note_trims.json`: add `"Horns 1-2 a2": {"261": -3}`.
- `tools/score_to_parts.py` `NOTE_TRIM_RAMP_S`: add `"Horns 1-2 a2": {260.892: 0.1}`. The lookup compares the moved `qn` (260.892 in parts.json), not `sq`. A 261.0 key would not match and the 0.6 s default would apply.

The trim ends at the next moved onset (qn 261.918), so the f arrival keeps its full level.

**Predicted.**
- Pickup top at qn 261.75: -25.2 -> about -28.2 K, which is 2.3 dB under its f arrival.
- It is then within 2-3 dB of the f strings and winds. The crescendo still rises 6.5 dB across the beat.

## 4. Bar 37: the flute's first theme B note is level with the bass clarinet's held last note, which keeps swelling after the flute enters (measured; open since c19 B #3)

**Where.** Two notes at qn 108-110:
- Bass clarinet D flat 4, the p arrival that ends its solo, a half note.
- Flute 1 F5, the first note of theme B, p (p. 2, bar 37).

**What.**
1. **Flute minus bass clarinet:**

   | qn | 108.5 | 109.0 | 109.5 |
   |---|---|---|---|
   | K | +0.2 | +1.3 | 0.0 |
   | A | +2.0 | +4.1 | +3.7 |

   The flute leads only from qn 110, when the bass clarinet releases.

2. **Cause.** The bass clarinet's CC11 keeps rising through the flute's entry: 55 at qn 108.1 -> 58 at 108.75, then a taper to 46 at 110. That is the long-note swell on its own arrival note. The c19 role `[105, 110.5, -4]` lowers the whole span but leaves the shape.

3. **The marks.** The score has the bass clarinet's crescendo end at bar 37 (pp < p). The phrase is over, and the new theme takes the foreground.

**Fix.** `build/note_trims.json`, "Bass clarinet": add `"108": -3` (default 0.6 s ramp). It reaches -3 by about qn 108.5, which is where the overlap is.

**Predicted:**

| qn | 108.5 | 109.0 | 109.5 |
|---|---|---|---|
| Flute minus BCl, K | +3 | +4 | +3 |
| Flute minus BCl, A | +5 | +7 | +6.5 |

The bass clarinet's p arrival is still 3 dB over its pp of bar 36 (qn 106: -47.5 K).

## 5. Smaller items for the actor's judgement (measured)

- **Oboe entry, qn 54.0** (bar 19). Violins II are still +1.5 K over the oboe in the first 0.5 qn. The c24 `NOTE_TRIM_RAMP_S` works: vol is +7 by qn 54.09. What remains is the oboe sample's slow speech, which is critic A's lens. I propose no level change.
- **Single bursts in bar 61:**
  - Violins II at qn 206.3: +4.9 K over Violins I for 0.1 qn.
  - Bassoon 2 at qn 208.0: +3.7 over Violins I for 0.1 qn.

  These are join or attack spikes. List them for critic A's spike scan rather than as level changes.
- **Harp attacks.** In bars 71-78 the harp attacks are 8-20 dB under the summed texture. At qn 255-261 the texture grows to f around the printed p harp, and the attacks are 18-20 dB under. That follows from the printed dynamics, and Rimsky lists the harp among the instruments a sustained tutti covers. No change.

## Do not touch

- The cross-family dynamic map: CC11, `soft_trim_db` and the family trims. pp/p/mp agree within 1-3 dB across families, and all p solos sit within 2 dB of each other.
- The bar 61-63 balance (horns f, low brass mf, Tbn1 ff marcato), which matches Rimsky's proportions. That includes the low-brass roles `[204, 212, ...]` and `[200, 214, 3, 1]`.
- The coda balance (c24 B #2 + C #4) and `HP_SOFT_ACC_SKIP` 283.
- The Timpani `[277, 280, 10]` role and the f/ff roll levels.
- The existing Vc note trim 261 -8.
- `deliver_master.py`.

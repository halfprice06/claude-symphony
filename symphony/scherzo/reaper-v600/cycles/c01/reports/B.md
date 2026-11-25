# Cycle 01, critic B (balance and levels), on the c00 render

Measured on `cycles/c00/render/` stems and master: plain RMS per bar or per 0.125-1.5 qn window on the parts.json tempo map, plus per-pitch residuals of every horn note of 1.5 qn or longer against a pooled CC11/CC1 fit, with gain, vol_db and soft/dyn trims removed. Levels are dBFS RMS unless marked otherwise. The master figures in the simulations are float sums of the c00 stems with the proposed gains applied, using 0.5 qn ramps.

## Manual notes (cycle 1, slot B: group B1, PDF pages 137, 140, 150-151; MANUAL-GAPS.md read)

| page | what it says | where it applies here | render follows? |
|---|---|---|---|
| 137 | Each KS Master articulation row has a load button and a volume knob that sets that row's loudness | row-level differences, e.g. Stac vs Sus MAX vs Leg Slur MAX (`ROW_TRIM_DB` for Violins I/II, violas, celli) | Yes in effect. The pipeline sets row trims in the volume envelope, not on the row knob. Unused rows are unloaded (`UNLOAD_UNUSED_ROWS`). |
| 140 | The master channel's gain fader sets the instrument's output without changing the mic mix | `mix.json` `gain_db` | Yes. The gain goes into REAPER's volume envelope after Opus, so the mic mix is unchanged. |
| 150 | Velocity picks the dynamic layer and is "most often used in short instruments" because it cannot change mid-note | harp, pizzicato and timpani strokes use velocity; sustains use CC11 with fixed velocities | Yes |
| 151 | Send CC1 and CC11 before the first notes | the 3 qn pre-roll carries every first CC | Yes |
| 151 | CC7 sets each track's overall ceiling; CC11 shapes the line. On string and woodwind patches CC11 controls dynamics and CC1 controls vibrato | timpani rolls are shaped with CC7 (CC7 28 at the p roll of bar 101) and made up by `TIMP_ROLL_TRIM_DB`, up to +18.6 dB in the post-hall volume envelope | No. This causes finding 5. The woodwinds' CC1 100-120 at the summit is vibrato, as the page describes. |

From MANUAL-GAPS: #6 (hard-stick timpani) and #9 (half-section basses) are not balance problems on this render. #3 (no solo violin library) is relevant to finding 2: the DIV A half section stands in for the solo, so its level has to be set by gain.

## Findings, ranked by what a listener would hear

### 1. Low horns at pp/p sit above the tunes they accompany: trio drone, codetta, retransition, and the sub. p chord of bar 121

- **Where.** Bars 153-168 (qn 456-504): the Horn 3/4 E-B drone (pp) under Clarinet 1's trio tune (p, dolce). Bars 229-240 (qn 684-720): the Horn 4 pp pedal under the codetta woodwinds and the start of the retransition. Bars 121-127 (qn 360-381): the Horns 2/4 tenuto chord (sub. p) under the Violins I/II espress. second idea.
- **Evidence (measured).**
  - Trio tune, bars 153-167: Horn 4 (E3) plays at -31.8 to -38.1 against Clarinet 1 at -37.4 to -46.5, so the pp drone is 5-12 dB above the p tune. With an approximate K-weighting it is still 4-13 dB above (bar 153: Horn 4 -37.5, Clarinet 1 -50.3).
  - Horn 4 is the loudest stem in every bar from 153 to 168, and again in 229-236 and 237-240. In 237-240 Horn 4 pp sits at -33.7 against Horn 3 -41..-47, Horn 1 -41..-50 and violas -45..-50.
  - Horn 3 (B3) and Horn 4 (E3) have identical CC11 (32-36), CC1 (60), velocity (41), row (Sus MAX) and envelope, yet Horn 4 is 8-12 dB louder.
  - The per-pitch residuals on the 1FH KS Master give Horn 4 E3 +4.2 dB (18 notes) and Horn 3 B3 -3.2 (20 notes). The same fit gives G sharp 4 -4.0 (Horn 1, 12 notes; Horn 3 -7.6), F sharp 4 -4.0 / -3.7 (Horns 1/2), E4 +2.7 / +5.3 (Horns 2/3) and Horn 4 F sharp 3 -4.9 (10 notes).
  - Movement II measured the same patch the same way: horn Gb4 +4 and Ab4 +3 in `symphony/mvt2/reaper-v600/build/pitch_trims.json`. Here `pitch_trims.json` is empty.
  - Across the movement Horn 4's pp median is -34.3, against -41.9 / -42.5 / -44.2 for Horns 3/2/1. All four horns carry soft trims of +13 to +13.5 dB at pp and +9.7 to +12 at p (Movement I's values).
  - Bar 121, first 0.5 qn: Horn 4 enters at -38 while the Violins I espress. line is at -47..-42. Over bars 121-126 Horns 2/4 are at -32.5..-38.6 against Violins I at -37.4..-41.2, so the accompaniment sits 0-5 dB above the melody.
- **Judgement.** The drone and the tenuto chord should sit 3-5 dB under the line they accompany. The low-register excess is in the samples (measured); the soft trims make it worse (inferred).
- **Fix.**
  - (a) Add to `build/pitch_trims.json`:
    - `"Horn 4": {"52": -4, "54": 4, "66": 4, "68": 3.5, "_all_arts": true}`
    - `"Horn 1": {"66": 4, "68": 3.5, "_all_arts": true}`
    - `"Horn 2": {"66": 4, "68": 3.5, "64": -3, "_all_arts": true}`
    - `"Horn 3": {"64": -3, "68": 3.5, "_all_arts": true}`

    Hn 1's G sharp 4 is the motto note of bars 1-2 and 372-376; +3.5 makes it as even as its neighbours.
  - (b) In `build/mix.json`, set Horn 4 `soft_trim_db` pp 13.5 -> 9.5 and ppp 14 -> 10.
  - (c) Add to `build/roles.json`:
    - `"Horn 3": [[456, 504, -3], [708, 720, -4]]`
    - `"Horn 4": [[360, 381, -4], [684, 720, -3]]`
    - `"Horn 2": [[360, 381, -4]]`
    - `"Clarinet 1": [[456, 504, 2]]`
  - Expected result (simulated by subtraction): the trio drone at about -40..-46 against the clarinet at -35..-44.
  - Check bar 153 after the render: Clarinet 1 3-5 dB over Horn 4.

### 2. The Violin I solo (bars 349-356) is 7-10 dB under the flute doubling it and under the celli

- **Where.** qn 1044-1068: Violin I solo (DIV A), Flute 1 "col Vl. solo" at the same pitch, Violins II "la metà" an octave below, celli, violas div. Printed dynamic pp everywhere.
- **Evidence (measured).**
  - Per bar 349-356, Violin I solo is at -45.5 to -52.5, Flute 1 at -37.1 to -41.9 (approximately K-weighted: solo -46..-54, flute -36..-44), and the celli at -44.1 to -46.9.
  - In bars 352-355 the solo is 3-8 dB under the celli accompaniment as well.
  - The solo's CC11 is 42-64, the same range as the flute's (42). Its gain_db is 0.4, carried from Movement II's entry for another context. The DIV A half section is recorded quieter than the full section (inferred from p.89-90's half-section note in the A1 group).
- **Judgement.** The solo is the printed lead ("solo, gli altri tacet"), and the flute doubles it. As rendered, a listener hears a flute solo with a faint violin under it (inferred).
- **Fix.** In `build/roles.json`, add `"Violin I solo": [[1044, 1068, 7]]` and `"Flute 1": [[1044, 1068, -3]]`. If the envelope headroom matters, set `mix.json` Violin I solo `gain_db` 0.4 -> 7.4 instead of the role. Target: the solo 1-3 dB over Flute 1 and 5 dB or more over the celli. The solo stem peaks at 0.03, so +7 leaves plenty of headroom.

### 3. Single woodwinds are the loudest stems at the ff/fff arrivals (bars 104, 304, 336-338); the summit sum overshoots by +2.7 dBFS

- **Where and evidence (measured).**
  - Summit, bars 336-338: Cor anglais -15.1 (bar 337), Bassoon 1 -17.1..-19.7, Clarinet 2 -19.5..-20.4 and Flute 1 -18.0 (bar 336). Each is one player, yet each sits 2-8 dB over every string section (Violins I -21.9..-27.6, Violins II -21.1..-24.0, celli -20.7..-25.6, violas -25.8..-33.0).
  - Bars 104 and 304: Clarinet 1 (A5) at -21.5 / -18.5 and Cor anglais at -22.0 are the loudest stems, over Violins I at -24.3 / -24.5.
  - Cause, from parts.json vol_db at qn 1005: the winds take `HP_GAIN_DB` wind 4 plus `HP_CHAIN_RISE_FFF` wind 0.75 for +7.0 dB (Cor anglais 9.7 with its accent), against Violins I +3. `mix.json` adds ff trims of Cor anglais +3 and Bassoon 1 +2.5.
  - The master's float peak of 1.367 (+2.7 dBFS) at 240.9-242.8 s comes from these bars, and the delivery limiter takes 4.9 dB there (BRIEF item 6 asks for about 3 at most).
- **Judgement.** In a real orchestra the fff violins carry the theme (B6 with Flute 1) over doubling woodwinds. As rendered, the summit is woodwind-led and clipped by the limiter (inferred from the balance; the overshoot is measured).
- **Fix.**
  - Add to `build/roles.json` over [1002, 1017]:
    - Cor anglais -6, Bassoon 1 -6, Clarinet 2 -5
    - Flute 1 -4, Flute 2 -4, Clarinet 1 -4, Bassoon 2 -4, Oboe 2 -4
    - Oboe 1 -3, Contrabassoon -3
    - Violins I +2, Violins II +1.5
  - Add over [306, 312] and [906, 912]: Clarinet 1 -5, Cor anglais -5, Clarinet 2 -3, Bassoon 1 -3.
  - Simulated:
    - Sum peak +2.72 -> +0.83 dBFS.
    - Bars 336/337/338: -11.5/-9.5/-11.2 -> -14.1/-12.2/-13.2.
    - Bars 104 and 304: -13.4 -> -15.1 and -12.4 -> -14.6.
    - The summit stays the loudest bar by 2.4 dB over bar 304.
    - At 336-338 the strings sit at -21.2..-23.1 and the woodwinds at -24.1..-25.3.
  - The generic alternative is `HP_CHAIN_RISE_FFF["wind"]` 0.75 -> 0.25 in `build/score_config.py`, which is about -2 dB on every wind at a chained fff. It is not enough alone.
  - If finding 4 is applied as well, reduce the Bassoon 1/2 and Cor anglais roles here by the dyn-trim change (2.5-3.5 dB).

### 4. Bassoons and cor anglais at f are as loud as the full violin sections across the movement

- **Evidence (measured).**
  - Stem medians at printed f: Bassoon 1 -33.6, Bassoon 2 -35.0, Cor anglais -35.1, against Violins I -34.7, Violins II -38.7, violas -40.2 and celli -35.0. Flute 1 is at -39.7 and Oboe 1 at -40.2.
  - Bars 45-52, the second idea (espress. in Fl 1, Ob 1, Cor anglais and the strings): Bassoon 1 plays the unmarked bass line (G2-E3), yet it is in the top three stems in 5 of 8 bars, at -29.1..-35.2, level with the Violins I melody (-24.8..-38.4).
  - Bars 38-40: Bassoon 1/2 are at the top (-32.8..-37.6).
  - The f/ff dyn trims are Movement I's: Bassoon 1 +3.5/+2.5, Bassoon 2 +4.0/+3, Cor anglais +2.5/+3. Movement I had bassoon solos at f (inferred).
- **Fix.** In `build/mix.json` `dyn_trim_db`, set:
  - Bassoon 1 f 3.5 -> 0, ff 2.5 -> 0
  - Bassoon 2 f 4.0 -> 0.5, ff 3 -> 0.5
  - Cor anglais f 2.5 -> 0, ff 3 -> 0.5

  Target: a single woodwind at f 3-5 dB under a violin section at f when it is not the lead. Re-check the bar 105-120 tenor countermelody (Bn1 with Hn 3-4 and celli, espress.). It is doubled, so it should still read (inferred).

### 5. The p timpani roll at bar 101 starts with a 0.5 s burst louder than the f tutti (BRIEF item 5)

- **Where.** qn 299.75-300.75. The roll starts at p (qn 300, 9 qn, crescendo to f at 104) right after the bar-100 mf strokes (296-299).
- **Evidence (measured).**
  - In 0.25 qn windows, the timpani stem reads -26.0 at 299.75, -18.3 at 300.0, -22.8 at 300.25 and -26.2 at 300.5. Violins I (f) reads -39.6..-31.7 over the same windows.
  - The master window at 300.0 is -18.0, so for one beat the p roll is the loudest thing in the orchestra, 21 dB over the f violins.
  - Mechanism, from parts.json: CC7 steps 120 -> 28 at 299.98 while vol_db steps 0 -> +18.6 (`TIMP_ROLL_TRIM_DB` at p). The ring and hall of the CC7-120 mf strokes are boosted by 18.6 dB in the post-hall envelope.
  - This is the case manual p.151 warns about: CC7 is used to shape the roll, and the envelope makes up for it.
  - No other roll has strokes just before it. The rolls at 384, 612, 708, 906 and 993 start cleanly and settle to rank 8-10 among the stems.
- **Fix.** Add to `build/roles.json` `"Timpani": [[300.0, 303.0, -8]]`. Its ramp runs 299.5-300, after the 299.09 stroke's attack. That removes the burst and starts the roll at about -30, under the f strings, before the printed crescendo.
  - Generic alternative in `tools/score_to_parts.py`: make the roll's vol_db make-up ramp in over 0.25 qn after the roll onset when a stroke sounded within 1 qn before, instead of stepping at onset - 0.02.
  - Re-check bar 101 for rank: the roll should be no louder than the f string sections.

## Do not touch

- The trumpets' repeated quarters in 105-120 and 305-320 (-34..-35 against Violins I -27..-30: present, not on top).
- Theme A at bar 13 (Violins I 5-6 dB over celli, violas and the pizzicato basses).
- Hn 1's motto tail at 357-360 (7-8 dB over the violas).
- The roll settling at 129-130, 205-208 (it grows only inside its printed crescendo), 237-240, 285-286, 303 and 332.
- The summit staying the loudest bar.
- The Violins II con sord. arpeggios in 169-184 (10-15 dB under the celli tune, as pp accompaniment).

# Cycle 16, critic C: holistic comparison (on the cycle 15 render)

Under review: `cycles/c15/render` (master and 29 stems), `cycles/c15/mvt2-mockup-c15.mp3`, `cycles/c15/metrics`, `build/parts.json` (written 19:27, before the c15 render at 20:05), `build/{mix,roles,early_fills}.json`, `tools/score_to_parts.py`, `tools/build_reaper.py`, `tools/deliver_master.py`, score pages 2, 5, 6 and 7. Comparisons:
- cycle 0 (`cycles/c00`, measured with `cycles/c00/before/parts.json`)
- five cycles back, cycle 10 (`cycles/c10`, measured with `cycles/c11/before/build/parts.json`)
- the references: the Dvorak 9/i Columbia MP3 (audio), and Brahms 1/ii and 4/ii (stored metrics in `symphony/render/critics/c04/ref_brahms*_musopen/`, the only slow-movement references).

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c16-C/`:
- `m_c10`, `m_c15`, `m_mp3`, `m_c10mp3`, `m_S*`: `symphony/render/tools/measure.py` on each master, mp3 and simulation.
- `sections.py`, `motion.py`: c12-C's section loudness and loudness-motion scripts.
- `tempo.py`: tempo statistics per section.
- `loudspec.py`: 1/3-octave spectrum of the loudest 10% and the middle 40-60% of frames.
- `band.py`, `stemspec.py`, `kw.py`: per-stem band shares, spectra and K-weighted levels at the climaxes.
- `sim.py`: level and EQ changes applied to the c15 stems in score-time windows and summed. The stems sum to the master exactly, so this is exact for level changes. The EQ is an FFT approximation of a bell. `dm/` holds the simulated outputs of the unchanged `deliver_master.py`.
- `legdips.py`, `autofill.py` (writes `joins_c15.json`), `fl.py`, `holes.py`, `holes2.py`: dips at legato joins and at onsets.
- `vel.py`, `acc.py`: velocity runs and per-beat accompaniment levels.

## Where the render stands (measured)

| | c00 | c10 | c15 | c15 mp3 | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|---|---|
| I (LUFS) | -24.2 | -23.6 | -23.6 | -19.8 | -23.0 | -19.1 |
| LRA (LU) | 20.0 | 21.6 | 23.2 | 15.9 | 15.2 | 16.9 |
| L/R correlation | 0.18 | 0.58 | 0.59 | 0.59 | 0.51 | 0.55 |
| centroid of loudest 10% (Hz) | 448 | 1007 | 988 | 963 | 835 | 782 |
| loud minus soft shape at 157 Hz (dB) | +1.8 | -3.2 | -2.6 | -3.7 | -0.4 | +5.1 |
| 100-250 Hz share (dB) | -4.9 | -9.4 | -10.1 | -9.5 | -8.8 | -7.6 |
| std of 10 s blocks, softer half (dB) | 2.0 | 1.5 | 2.5 | 1.7 | 2.2 | 2.2 |
| phrase-scale motion (dB) | 3.5 | 3.6 | 3.8 | 3.0 | 4.6 | 3.9 |

The mp3 measures LRA 15.9 LU, a span of 18.7 dB and a limiter of 1.9 dB. All three are inside the brief's targets.

Section loudness in the mp3, in LU relative to integrated (c10 mp3 in brackets):
- intro -6.7 (-6.0)
- horn solo -4.1 (-5.4)
- bars 15-22 -4.6 (-5.6)
- tune -3.0 (-3.3)
- bars 37-52 -4.4 (-5.2)
- build +2.2 (+2.4)
- bars 61-64 +7.5 (+8.3)
- bars 79-82 +5.9 (+4.8)
- coda -7.4 (-6.9)

The two climaxes are 1.9 LU apart (c10 4.4).

Since c10, the large-scale shape has been fixed (measured):
- the climax weighting
- the layering of the soft half (intro and coda 2.5-3 LU under the solos)
- phrase-scale motion, now inside the Brahms range

The room and stereo image are also inside the reference range. What still sounds made by a machine is smaller in scale, and it repeats across the piece:
- the loud tutti have a thin low middle and too much top
- most legato note changes in the solo lines sag
- the rubato is one template, applied to every phrase alike
- the accompaniment has no metric weight

By passage, the weakest are:
1. Bars 61-62 and 79-80: their tone.
2. The flute lines in bars 37-44, 57-60 and 77-80: holes at the joins.
3. Bars 15-22: a hesitation every two bars.
4. Bars 37-52: the pizzicato and harp beats all weigh the same.

## 1. The ff tutti (bars 61-62, 79-80) lack low-middle body. Measured; simulated fix

**Where:** qn 204-212 and 262-268, all tracks. The bass octave is Db2/Db3: Cb, Cbn and Tuba on Db2, and Bn2, BCl, BTbn and Timp on Db3.

**What is wrong:** as the orchestra gets louder, the mockup gains top but no bass. The loudest frames sound violin-lit and thin.

**Evidence (measured):**
- In the loudest 10% of frames, the 125 and 160 Hz bands are -11.9 and -10.5 dB relative to 1 kHz. The Dvorak loud frames have -1.3 and +1.7. In the middle 40-60% of frames the mockup matches Dvorak at 125/160 (-8.2/-3.7 against -8.2/-2.6). So the deficit appears only at loud levels.
- Against the two slow-movement references:
  - loud minus soft at 157 Hz: -2.6 dB, against -0.4/+5.1
  - at 5 kHz: +11.1, against +5.3/+10.4
  - at 10 kHz: +12.1, against +4.9/+10.6
  - centroid of the loudest 10%: 988 Hz, against 782-835. It has not moved since c10 (1007).
- At bars 61-62, Vln I supplies 59% of the master's 2-6 kHz. The bass-octave instruments sit 19-30 dB under the master's 1 kHz band at 125 Hz:
  - BCl -19.3, Tuba -19.3, Cbn -20.1, BTbn -22.3, Bn2 -30.2
  - Cb at 125 Hz is -15.9, 9.5 dB under its own 63 Hz fundamental.
- `mix.json` already tilts the loud strings toward the top: Vc `dyn_trim_db` f -2 / ff -2.5, and Vln I ff +1.5.

**Simulations** (`sim.py`, through the unchanged `deliver_master.py`):

| case | centroid loud 10% | 157 Hz loud-soft | 100-250 share | limiter | mp3 LRA / span | Vln I margin (K-weighted) at 204 / 262 |
|---|---|---|---|---|---|---|
| c15 | 988 | -2.6 | -10.1 | 1.9 | 15.9 / 18.7 | +3.3 / +3.2 |
| S6 levels only | 877 | -2.0 | -9.4 | 2.7 | 16.1 / 18.9 | +2.2 / +2.3 |
| S7 = S6 + 150 Hz bell +4 on Vc/Cb | **854** | **0.0** | **-8.3** | **2.4** | 16.2 / 19.0 | +2.2 / +2.3 |

- S7 puts the loud-frame 125/160 bands at -7.3/-6.8 (from -11.9/-10.5).
- A version with Vc +2.5 (S3) made the celli level with Vln I at qn 204 (margin 0.3 dB). Keep the Vc lift at +1.

**Fix:**
1. `build/roles.json`: add these spans with a 1 qn end_ramp, `[200, 214, dB, 1]` and `[258, 272, dB, 1]`, to:
   - Double basses +3, Contrabassoon +4, Bassoon 2 +4
   - Tuba +3 and Bass trombone +3 (they rest in bar 79, so only the first span sounds)
   - Bass clarinet +2, Timpani +2, Violoncellos +1
   - Violins I -1, Violins II -0.5

   These add to the existing [204,212] and [262,268] roles. Check in parts.json that `vol_db` at qn 206 and 264 equals old + new. Per LEARNINGS c09, spans that meet must crossfade.
2. `tools/build_reaper.py`: generalise `set_mute_eq` to take a list of wet points instead of one `from_qn` step. Then add to `mix.json` for Violoncellos and Double basses:

   `"loud_eq": {"points": [[199,0],[201,1],[213,1],[215,0],[257,0],[259,1],[271,1],[273,0]], "bands": [{"band": "bell", "hz": 150, "db": 4, "bw_oct": 1.0}]}`

   Score qn plus PRE, as `mute_lua` does. This is a second ReaEQ whose Wet is automated, so the soft passages keep today's spectrum, which already matches the reference.
3. Do step 1 first if step 2 cannot be built this cycle. It gets about half the gain.

**Check:**
- the centroid of the loudest 10% is 900 Hz or lower
- loud minus soft at 157 Hz is -1 dB or higher
- Vln I stays at least 2 dB over every other stem (K-weighted) at qn 204-212 and 262-268
- the limiter stays at or under 2.8 dB (LEARNINGS: the simulation under-predicts by about 0.5)
- mp3 LRA is 16.3 or less

If the LRA goes over 16, take the Bassoon 2/Cbn values down by 1.

## 2. Legato joins in the solo lines still sag at most note changes. The flute is the worst line, and per-note fills have not kept up. Measured

**Where:**
- Flute 1 throughout (bars 37-44, 47, 57-60, 77-80)
- Oboe 1 (bars 15-20, 47-50, 58-60, 79-81), Cor anglais (bars 32-34, 41-44, 51), Horn 1, Clarinet 1
- the Vc countermelody

**What is wrong:** a player's legato is continuous. Here the level falls 5-12 dB about 0.2-0.35 s after many note changes, inside the Opus legato transition, and then recovers. Inferred listener effect: a small pumping on each note, the most frequent machine trait left in the exposed solos.

**Evidence (measured).** For joins where the previous note runs into a note of 0.45 s or more, the dip is measured against the lower of the two note bodies, with a 30 ms envelope (`autofill.py`, `legdips.py`):

| line | joins | median dip | dips of 5 dB or more | of those, already in early_fills |
|---|---|---|---|---|
| Flute 1 | 52 | 4.8 | 23 | 5 |
| Oboe 1 | 36 | 4.4 | 17 | 6 |
| Cor anglais | 24 | 4.6 | 10 | 8 |
| Horn 1 | 49 | 2.7 | 7 | 0 |
| Clarinet 1 | 25 | 3.1 | 6 | 2 |
| Bass clarinet | 11 | 3.6 | 3 | 2 |

- Across the eleven lead and string tracks, long-note joins measure a median dip of 3.3 dB in c00, 4.5 in c10 and 4.2 in c15. Joins of 6 dB or more number 68, 106 and 93.
- The flute's long joins: 7 of 18 reach 6 dB or more in c00, 12 of 18 in c15.
- 23 joins that already have a fill still dip 5 dB or more. The fill was sized on an earlier render, or sits too early. Examples:
  - CA 131.5: fill 5, dip 8.1 at +0.23 s
  - CA 132: fill 4, dip 8.8 at +0.19 s
  - Fl1 190: fill 5, dip 9.8 at -0.05 s
  - Fl1 252: fill 6, dip 9.7 at +0.40 s
  - Ob1 270/270.5/271: dips 7.1-8.0
- Unfilled worst cases:
  - Fl1 193 11.7, 257.5 11.3, 258.5 10.9, 200 9.0, 255 8.0
  - Ob1 190 10.0
  - CA 152 11.8
  - Vc 188 11.4 and 146 13.1
- The full list, with dip time and velocity, is in `joins_c15.json`.

The per-note method works (LEARNINGS c11: 14 of 15 joins went from 7-11 to 3-5 dB). But each cycle adds a handful of fills while leads and arcs move the sags, so the count of large joins has not fallen since c10.

**Fix:** make the fills a measured pass instead of hand edits.
- New `tools/auto_fills.py PREV_CYCLE`. It reads `cycles/cPREV/render` stems and the parts.json that produced them, and runs the join measurement in `autofill.py` (score onsets on that parts.json tempo map). It applies to Flute 1, Oboe 1, Cor anglais, Clarinet 1, Bass clarinet, Horn 1, Violin I solo and Violoncellos.
- For every join with a dip of 5 dB or more that has no entry, it writes into `build/early_fills.json`:
  - `{"db": min(6, dip - 3), "pre_s": max(0, -t_min), "hold_s": clamp(t_min + 0.05, 0.10, 0.35)}`
  - Tag these entries `"_auto"` in the track's `_doc` so they can be regenerated.
- For an existing entry whose join still dips 5 dB or more, it raises `db` by `min(3, dip - 4)`, capped at 8. It moves `hold_s` to the measured minimum + 0.05 s.
- Hold only to the sag minimum, never past +0.35 s. LEARNINGS c11: Horn Ab4 and other samples swell by themselves after +0.3 s, and a longer hold overshot by 4-10 dB.

Run it once on c15, regenerate parts.json, and check that the diff touches only `vol_db`/`vol_bp`. This is a level-only change, so the c10 simulation method can preview it on the c15 stems before the render.

**Check:**
- joins of 5 dB or more in the six wind/horn lines go from 66 to under 25
- no filled join rises more than 2 dB over its body between +0.3 and +0.6 s
- the Flute 1 median falls under 4 dB

## 3. The rubato is one template applied to every phrase. The crescendos and the Largamente arrival are metronomic. Tempo measured; effect inferred

**Where:** the tempo map (`PHRASE_ARCS` in `tools/score_to_parts.py`).

**Evidence (measured, beat bpm from the parts.json map):**
- Bars 15-22 have the same shape every two bars, at the sub-phrase ends:
  - bar 16: 52/51/46
  - bar 18: 52/51/49
  - bar 20: 52/51/49
  - bar 22: 52/49/43

  Each is followed by 50/52/52.
- Every phrase ends the same way: two slower beats and a return. The phrase apex is never marked. Bars 8, 12, 24 and 28 are flat at 52-53 through the horn solo crests and the mf peak of the tune.
- Passages that are flat to the decimal:
  - bars 61-62 (Largamente, molto sostenuto, ff): 8 beats at 54.0
  - bars 75-77 (crescendo p/mp to f into the poco allargando of bar 78): 9 beats at 52.0
  - bars 37-39: 60/61 with no change

  56% of the beats in bars 1-34 and 52% in bars 37-46 are exactly at the base tempo.
- Inferred: real phrasing moves forward into a crescendo and gives the apex note a little extra time. A predictable slow-down every two bars reads as programmed.

**Fix**, in `score_to_parts.py`. Whole-beat steps only, so `add_caesuras` is unaffected:
1. `TEMPO_PUSH = [(244, 253, 1.025), (78, 84, 1.02), (21, 24, 1.015)]` (bars 75-77, 27-28, 8). Multiply the tempo across each span, starting 1 beat in. Apply it after `phrase_arcs` and skip it where `RAMP_SPANS` overlap.
2. `APEX_AGOGIC`: for each `PHRASE_ARCS` span, find the beat that holds the highest note of the lead line, taking the track with a `LEAD_SPANS` or solo role there. Multiply that beat by 0.96, unless it is one of the last two beats. Also lengthen the Largamente downbeats, qn 204 and 208, by x0.94.
3. In bars 15-22, keep the "sub" depth only on (48, 54). Remove (42, 48) and (54, 60) from `PHRASE_ARCS`, so that bars 19-22 run to the cadence at qn 66 as one phrase.

Expected: the total length changes by under +1.5 s. The leads follow automatically (`qn_before`). Use `--midi-only --tempo`.

**Check:**
- the attack gate
- no caesura exit
- bars 75-77 rise to about 53.5 bpm and then hand over to the printed allargando with no step up at bar 78

## 4. The accompaniment has no metric weight: downbeats are no stronger than weak beats, and long runs of notes share one velocity. Measured; effect inferred

**Where:**
- bars 37-52: Cb/Vc pizz. and the harp under the flute and cor anglais solos
- bars 7-14: the harp, bassoon and bass clarinet chords under the horn solo
- bars 71-78: the viola figure

**Evidence (measured):**

Per-onset attack peak (30 ms envelope, first 0.2 s), mean by beat relative to the line's mean:

| line | beat 1 | beat 3 | other beats | peak std |
|---|---|---|---|---|
| Cb pizz. 37-52 | +0.2 | -0.3 | | 1.7 |
| Vc pizz. | -0.6 | +0.6 | | 2.4 |
| Harp 37-52 | +0.7 | -0.2 | | 3.8 |
| Harp 7-14 | -1.1 | +0.7 | beat 2 +0.9 | 3.3 |
| Violas 71-78 | -2.6 | +1.5 | | |

- Identical velocities in a row: Harp 19, Cb 18, Bass clarinet 18, Bassoon 1 16.
- The velocity means are lower on downbeats than on other beats in every string track (for example Vln II 104 against 119). This is because legato targets take v120-124. It does not affect the plucked lines, but it shows that no rule sets weight by metre.
- Inferred: a pizzicato bass or a harp in a slow 4/4 or 3/4 leans on the downbeat. Evenly weighted plucks (only round-robin and pitch noise) sound sequenced.

**Fix**, in `score_to_parts.py`: `METRIC_VEL = {"downbeat": 6, "mid": 3, "weak": -3}`, applied to notes whose articulation contains "izz" and to the Harp track. "mid" is beat 3 in 4/4. Skip notes with an accent or sf, notes inside `LEAD_SPANS`, and the harp's rolled-chord inner notes, so that `HARP_PITCH_VEL` and the roll offsets keep their order.

At 0.3-0.6 dB per velocity step (LEARNINGS c09), +6/-3 gives a downbeat lean of about 2-3 dB. This is a velocity change, so the level simulation cannot preview it. Render, then rerun `acc.py`.

**Check:** the beat-1 mean is 1.5-3 dB over the line mean in bars 37-52, and the pizz. peak std stays under 3 dB.

## 5. Smaller observations (measured)

- **Solo wind vibrato is one value.** CC1 at 60% of each long note is exactly 100 on 89% of Flute 1, 77% of Oboe 1 and 81% of Cor anglais long notes, whatever the dynamic or position in the phrase. HO says CC1 sets vibrato "when available". Before shaping it, check on one flute note at CC1 60 against 100 whether these KS Masters respond. If they do, scale CC1 with the phrase arc: 85 at phrase starts, 100-110 at the apex.
- **Remaining onset holes in the master** (≥4 dB at onsets, c10 → c15):
  - bars 37-52: 21 → 26, mostly pizz. decays under the solos, which is natural
  - bars 53-60: 7 → 14, the Vc/Vln I/Vln II joins at qn 178, 186 and 193

  The bars 53-60 joins are covered by finding 2's pass if the Vc and strings are included.

## Do not touch

- The section balance and the delivery numbers: climax gap 1.9 LU in the mp3, mp3 LRA 15.9 / span 18.7 / limiter 1.9, and the intro and coda under the solos.
- The `_all` climax rows and the soft-trim table.
- The room, seats and widths (L/R correlation 0.59 against 0.51-0.55).
- The low-end high-passes, and the soft-passage spectrum, which matches the reference at 125-160 Hz. Add finding 1 only as level-dependent (wet-automated) EQ, not as static EQ.
- `SOST_HOLD_THROUGH`, `LEG_ART_EXTRA_S`/`LEG_SOFT_EXTRA_S`, `qn_before` leads, the caesuras and the fermata.
- The phrase-arc depths outside bars 15-22, and the `RAMP_SPANS`.

# Cycle 20, critic C: holistic comparison (on the cycle 19 render)

Under review: `cycles/c19/render` (master and 32 stems), `cycles/c19/mvt2-mockup-c19.mp3`, `cycles/c19/metrics`, `build/parts.json` (00:17, before the c19 render at 00:44), `build/{mix,roles}.json`, `tools/deliver_master.py`, score pages 1-7.

Comparisons:
- cycle 0 (`cycles/c00`, measured with `cycles/c00/before/parts.json`)
- five cycles back, cycle 14 (`cycles/c14`, measured with `cycles/c15/before/build/parts.json`)
- the references: Brahms 1/ii and 4/ii (stored metrics in `symphony/render/critics/c04/ref_brahms*_musopen/`) and the Dvorak 9/i Columbia MP3

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c20-C/`. `measure.py` needs scipy, so run it with `/usr/bin/python3`; the reaper venv does not have scipy.
- `m_c19`, `m_c14`, `m_c19mp3`, `m_c14mp3`: `measure.py` output.
- `sections.py`, `motion.py`, `loudspec.py`, `tempo.py`, `beatbpm.py`: section loudness, loudness motion, spectra and tempo.
- `ride.py`, `ride2.py`: delivery ride per section, and how much of the master's level motion survives in the mp3.
- `dm/dmx.py`, `dm/dmx2.py`: `deliver_master.py` with `SM`/`RATIO`/`KNEE` read from the environment (`dmx2.py` also caps the slow ride at the fast ride's gain). `dm/*.mp3` are their outputs.
- `sim75.py`: level-only simulation of finding 1 on the c19 stems, which sum to the master.
- `corr.py`, `corr2.py`, `harpcorr.py`, `harpE.py`, `bandcorr_t.py`: stereo correlation per stem, band and time window.
- `simside.py`, `simside2.py`: simulation of finding 2.
- `metric2.py`: metric weight of plucked lines. `legnotes.py`, `holes.py`, `legdips.py`: joins and onset holes.

## Where the render stands (measured)

| | c00 | c14 | c19 | c19 mp3 | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|---|---|
| I (LUFS) | -24.2 | -23.8 | -22.4 | -19.8 | -23.0 | -19.1 |
| LRA (LU) | 20.0 | 23.5 | 23.8 | 16.1 | 15.2 | 16.9 |
| True peak (dBFS) | | -4.5 | -3.8 | -1.6 | | |
| centroid of loudest 10% (Hz) | 448 | 987 | 845 | 842 | 835 | 782 |
| L/R correlation <250 / 250-4k / >4k | 0.17/0.22/-0.02 | 0.56/0.60/0.49 | 0.43/0.60/0.50 | 0.45/0.59/0.50 | 0.60/0.48/0.38 | 0.62/0.52/0.47 |
| phrase-scale motion (1 s vs 20 s, dB) | 3.5 | 3.8 | 3.6 | 2.8 | 4.6 | 3.9 |
| 10 s block std, softer half (dB) | 2.0 | 2.5 | 1.8 | 1.5 | 2.2 | 2.2 |

Delivered mp3 (from `deliver_master.py`): span 18.5 dB, limiter 2.0 dB. The two climaxes are 1.5 LU apart in the mp3 (short-term max -9.4 and -10.8).

Since c14, the room, the loud spectrum and the section balance have held, and the loud-frame centroid has reached the Brahms range (987 -> 845 Hz). The 1/3-octave shape of the loudest 10% still has less 125-160 Hz than the Dvorak reference (-7.7/-5.5 against -1.3/+1.7 relative to 1 kHz), but the band shares match the two Brahms references, so I leave the spectrum alone.

What still marks the render as made by a machine is at the scale of whole passages:
- The build-up to the recapitulation climax does not grow.
- The bass and the harp have a stereo image that a hall does not produce.
- The plucked accompaniment has no downbeat.
- Some exposed soft stretches run at a metronome tempo.

The legato joins are no longer the main problem. Most of the large dips my 30 ms join probe finds (Cl1 188 and 286, Ob1/Fl1/Cl1 204 and 268) are printed breaths or caesuras.

## 1. Bars 75-78: the crescendo into the recapitulation climax does not grow. In the delivered mp3 it rises 1.5 dB over three bars, and the f in bar 78 is no louder than bar 77. Measured; the fix is simulated.

**Where:** qn 250-262, all tracks. Score page 6: bar 75 starts p/mp with a crescendo to f at bar 78 (poco allargando), then ff at bar 79.

**What is wrong:** the crescendo starts too loud and arrives soft. Inferred listener effect: three bars of build that stay at one level, followed by a 6-7 dB jump into the ff. The main structural arrival of the reprise sounds like a sudden step, not like the end of a build.

**Evidence (measured).** Bar RMS, master:

| | 74 | 75 | 76 | 77 | 78 | 79 |
|---|---|---|---|---|---|---|
| c00 | -32.7 | -30.3 | -27.1 | -25.7 | -24.8 | -17.4 |
| c14 | -35.9 | -30.4 | -29.0 | -26.0 | -26.3 | -20.1 |
| c19 | -38.4 | -30.1 | -29.0 | -25.9 | -25.7 | -18.8 |

The c19 mp3 (power dB) reads 74 -29.7, 75 -22.9, 76 -23.2, 77 -21.2, 78 -21.4, 79 -14.8. From the printed p/mp to the printed f (75 -> 78), that is +1.5 dB, and bar 76 sits under bar 75. The first build, by comparison, measures +4.4 dB in the mp3 from the p at bar 57 to the f at bar 59.

Per beat, the master falls at the f arrival: 258 -21.7, 259 -22.3, 260 -23.6, 261 -22.1, then 262 -15.7.

The causes, in the data:
- **Bar 75 enters 8.3 dB over bar 74 for a one-level step (p -> mp).** The step is 3.7 dB per dynamic level in the bar-level fit over the movement (`bardyn.py`). Vc 249 -> 250 goes -41.2 -> -33.3 despite its [250,262,-5] role. Vln I goes -42.9 -> -34.1.
- **CC11 rises to 92 at 259.75 and then falls back inside the f bar**: Fl1 and Cl1 reach 83 at 260.875, Vln I and Vc 87. The printed f is 88 (`DYN`). The rule that writes this fall is probably a swell or return rule, but I did not trace it.
- **The Vln I volume envelope peaks at +6.1 dB at 256.75** (the top note, phrase-top lift). It falls to +2.5 dB at the 259 arrival.
- **The ride in `deliver_master.py` lifts bar 75 more than bar 78** (keep factor 0.61 in bars 71-78, `ride.py`).

**Simulation (`sim75.py`, all stems, level only):** -3 dB from 250 (ramp in from 249.6), held to 253, back to 0 at 258.5; +1.5 dB from 259 to 261.5, back to 0 at 261.9. The output, through the unchanged `deliver_master.py`:
- mp3 bars 75-78: -25.1, -24.7, -21.1, -20.0. The rise is +5.1 dB (was +1.5), and bar 78 now sits 1.1 dB over bar 77.
- The bar 79 ff is unchanged (-14.8).
- LRA 16.1, limiter 2.0 -> 1.7 dB, span 18.5 -> 18.1.

**Fix:**
1. `build/roles.json` `_all`: add `[250, 258.5, -3, 5.5]` (it opens over the last 5.5 qn, so it is -3 at 250-253 and 0 at 258.5) and `[259, 262, 1.5, 0.5]`. Per LEARNINGS c09, check in parts.json that the second row does not add to any existing row at 259-262 (the a2 horns' [269,278,-5] starts later). Check also that `vol_db` at 251 is the old value -3 and at 260 the old value +1.5 on Vln I, Vc and Fl1.
2. `tools/score_to_parts.py`: find the rule that lowers CC11 from 92 to 83-87 between 259.75 and 260.875 on Flute 1, Clarinet 1, Violins I and Violoncellos. Hold CC11 at no less than the printed f (88) until the next printed change at 262.
3. This is level and CC data only: `--midi-only`.

**Check:**
- mp3 bars 75 -> 78 rise at least 4.5 dB, and each bar is louder than the one before.
- Master beat 259 is at or above beat 258.
- Bar 79 is unchanged within 0.5 dB.
- Limiter at most 2.0 dB, and mp3 LRA at most 16.3.

## 2. Since the true-stereo hall (c17), the bass band is decorrelated and the harp's main register is out of phase between left and right. Measured; effect inferred; the fix is simulated.

**Where:** the whole movement. The harp in bars 7-14, 37-44, 53-56 and 71-78. Timpani, tuba, bass trombone and double basses.

**What is wrong:** in a recorded hall the bass is the most correlated band, and the image opens up towards the top. Here it is the other way round: low 0.43, mid 0.60, high 0.50, against Brahms 0.60-0.62 / 0.48-0.52 / 0.38-0.47. Below 250 Hz the c19 master is less correlated than c14 (0.56). Dan listens on headphones. Inferred effect: an anti-phase or uncorrelated low band sounds diffuse, wide and without a location inside the head, and the harp's bass chords have no place. On a mono fold the harp's 120-250 Hz band loses 4.8 dB.

**Evidence (measured, `corr2.py`, `harpE.py`, `bandcorr_t.py`).** 120-250 Hz L/R correlation, c16 -> c19 (c17 changed the hall to `S. Cal Hall Perc TS FR 3.3s` and the harp width to 0.12):

| | 120-250 Hz, c16 -> c19 | Tail only (0.2-1.0 s after release) | Share of the master's 120-250 Hz |
|---|---|---|---|
| Harp | 0.72 -> -0.42 | 0.72 -> -0.61 | 3.5% |
| Timpani | 0.50 -> 0.12 | 0.50 -> 0.16 | 8.7% |
| Tuba | 0.65 -> 0.38 | 0.54 -> -0.08 | 5.2% |
| Bass trombone | 0.74 -> 0.12 | | 1.2% |
| Double basses | 0.31 -> 0.17 | | 29% |
| Master | 0.44 -> 0.39 | | |

- The tails carry the drop, so the hall return is the main source. The harp is the worst case: its seat is far off centre (-0.72) and its mic channels sit at -0.84/-0.60.
- The harp's mono sum at 120-250 Hz is -4.8 dB (c16 -0.7 dB).
- The harp's 250 Hz-1 kHz band has been near 0.1 in every cycle since c14, so the patch's own mics are wide there.

**Simulation (`simside2.py`).** M/S on the stems of Harp, Harp harmonics, Timpani, Tuba, Bass trombone, Contrabassoon, Double basses and Violoncellos, with the side channel cut 8 dB below about 250 Hz and full above (side gain 0.4 + 0.6 x 2nd-order high-pass at 250 Hz). Results, summed:
- Master correlation: <120 Hz 0.52 -> 0.84, 120-250 Hz 0.39 -> 0.67. 250-4k and >4k are unchanged.
- Energy: -1.0 dB under 120 Hz and -0.8 dB at 120-250 Hz.
- Per stem at 120-250 Hz: Cb 0.59, Tuba 0.71, Timp 0.48, BTbn 0.63. The harp only reaches -0.10, because its anti-phase content extends above 250 Hz.

A full side high-pass (180 Hz) took <120 Hz to 0.92, more mono than the references, so use a shelf.

**Fix:**
1. **The bass instruments.** `build/mix.json` gets a new per-track key `"side_shelf": {"hz": 200, "db": -6}` on Double basses, Violoncellos, Tuba, Bass trombone, Contrabassoon and Timpani. `tools/build_reaper.py` applies it after the existing ReaEQs as three FX:
   - `JS: utility/KanakaMSEncoder1` (stock Cockos Mid/Side Encoder: ch1 = (L+R)/2, ch2 = (L-R)/2)
   - a ReaEQ with one low-shelf band at 200 Hz, -6 dB, whose input and output pins are mapped to channel 2 only (`TrackFX_SetPinMappings`; channel 1 passes untouched)
   - `JS: utility/KanakaMS5` (Mid/Side Decoder, Center Level 0 dB)

   These are REAPER FX after Opus, not Opus state, so `--mix-only` and `--midi-only` can apply them. The stems still sum to the master. Check that with the chain at 0 dB the stem equals the old one to -100 dB.
2. **The harp, as a test.** Set Harp and Harp harmonics `width` 0.12 -> 0.3 (the c16 value, when the harp measured +0.72), keep the seat at -0.72, and give both the same side shelf at 300 Hz, -8 dB. This is a state change, so it needs a full rebuild of those two tracks.

**Check:**
- Master correlation <250 Hz 0.55-0.65, and 250-4k unchanged ±0.02.
- Harp 120-250 Hz at 0.3 or more, and its mono-sum loss at 120-250 Hz under 2 dB.
- Master 100-250 Hz band share within 0.5 dB of c19.
- Tail R-L balance of the strings within 1 dB of c19.

If the harp is still negative, try a harp seat of -0.5 next cycle.

## Checked, no change: the delivery ride (measured)

The ride in `tools/deliver_master.py` (`SMOOTH_S` 3.0, `RATIO` 2) keeps 83-94% of the master's level motion in the soft sections and 61-70% in the builds (`ride.py`: slope of mp3 level on master level per section). Phrase-scale motion is 3.4 dB in the master and 2.6 dB in the mp3, against 3.9 and 4.6 in the Brahms recordings. The horn's swell to its mp crest (bar 7 -> 12) is +4.4 dB in the master and +3.3 dB in the mp3.

I tested slower rides on the c19 master plus the finding 1 simulation (`dm/dmx.py`, `dm/dmx2.py`). None is worth taking:

| SMOOTH_S / RATIO | LRA | limiter | soft-half keep | bars 61-62 vs 79-80 (mp3 dB) |
|---|---|---|---|---|
| 3 / 2 (now) | 16.1 | 1.7 | 0.83-0.94 | -12.9 / -14.6 |
| 6 / 2.5 | 16.2 | 1.3 | 0.90-1.00 | -13.4 / -14.4 |
| 8 / 3 | 16.4 | 1.8 | 0.91-1.00 | -13.6 / -13.9 |
| 8 / 4 | 16.1 | 1.7 | 0.95-1.00 | -14.0 / -14.0 |

- A slower ride looks ahead into the soft coda and lifts bars 79-80, so the second climax becomes as loud as the first (gap 1.7 -> 0 dB). The brief requires the climax to stay clearly the loudest.
- Limiting the slow ride to the fast ride's gain (`dmx2.py`) protects the climaxes, but then the soft half is the same as now.
- Leave `deliver_master.py` as it is. The phrase motion has to come from the mix.

## 3. The plucked accompaniment has no metric weight: downbeats are as weak as, or weaker than, the other beats. Measured; effect inferred.

**Where:**
- the harp under the horn solo (bars 7-14, qn 18-42) and under the flute (bars 37-44, qn 108-140)
- the viola pizz. eighths (bars 41-44, qn 124-140)
- the Vc/Cb pizz. (bars 37-40)

**Evidence (measured, `metric2.py`: peak of a 30 ms window in the first 0.2 s of each onset, stereo power).** Downbeat minus the mean of the rest of the bar:
- Harp 7-14: -1.6 dB
- Harp 37-44: +1.3 dB
- Viola pizz. 41-44: -0.6 dB, and on-beat minus off-beat eighths -1.0 dB
- Vc pizz. 37-40: -0.8 dB

Onset peak std is 2.2-3.7 dB. So the round-robin and pitch noise is larger than any metric pattern. c16's `METRIC_VEL` attempt (velocity) gave a 0.5-1.2 dB lean and doubled the Cb spread (1.7 -> 3.3 dB), because velocity also changes the sample.

**Fix:** a level step instead of velocity. In `tools/score_to_parts.py`, add `METRIC_DB = {"down": 1.5, "mid": 0.5, "off": -1.0}` (mid = beat 3 in 4/4; off = off-beat eighths):
- Apply it to notes on an articulation containing "izz" and to the Harp track, inside `METRIC_SPANS = [(18, 42), (108, 140), (172, 188)]`.
- Write it as a `vol_bp` step at full value on the attack, the same way as the pizz. pitch trims (LEARNINGS c12: 0 at onset - 0.03 s, full by -0.01 s, held to the next onset).
- Skip accented notes and `LEAD_SPANS`.

This is level only, so the actor can simulate it on the c19 stems before rendering.

**Check:** with `metric2.py` on the c20 stems:
- the downbeat minus the rest of the bar is +1 to +2.5 dB in every listed line
- viola on-beat minus off-beat is +0.5 to +2 dB
- onset peak std rises by no more than 0.5 dB

## 4. Exposed soft passages still run at an exact metronome tempo. Tempo measured; effect inferred.

**Where (beat bpm from the parts.json map, `beatbpm.py`):**
- bars 1-6: 18 beats at 52.0
- bars 31-34 (the BCl/CA duet with its mf crest in bar 33): 12 beats at 52.0
- bars 45-46 (oboe and cello p<, into the mf of bar 47): 8 beats at 60.0
- bars 48-49 (poco sostenuto, CA solo): 8 beats at 54.0
- bars 83-85: 9 beats at 52-53

62% of the beats in bars 1-34 sit exactly on the base tempo (c14 57%). The phrase arcs and pushes since c16 touch other passages.

**Fix (whole-beat steps, `--midi-only --tempo`):**
- Add `TEMPO_PUSH` entries (93, 99, 1.02) (bars 32-33) and (140, 147, 1.02) (bars 45-46).
- Add `APEX_AGOGIC` beats at qn 97 (the duet's mf crest, x0.96) and 147 (the oboe/cello crest before the printed poco rit., x0.97).
- Leave bars 1-6, 48-49 and 83-85 flat. These are held chords and a sostenuto, and their evenness is correct.

**Check:**
- the attack gate passes
- no step up at bar 47's poco rit. or at 108
- the total length changes by under 0.5 s

## Do not touch

- The loud spectrum and `loud_eq` (loud centroid 845 Hz, inside the Brahms range).
- The section balance (climaxes 1.5 LU apart in the mp3).
- The c19 leg_leads, pair leads, `LEG_CAP_FRAC` and `CAESURA_BREATH_QN`.
- The final tail hold and the tail hold through rests.
- The true-stereo hall itself (its tails balance L/R; fix its low band per finding 2, not by changing the IR).
- The breaths at 188, 204, 268 and 286, which my join probe flags as dips. They are printed.
- `deliver_master.py` (see the ride check above).

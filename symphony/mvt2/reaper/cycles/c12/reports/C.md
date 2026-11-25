# Cycle 12, critic C: holistic comparison (on the cycle 11 render)

Under review: `cycles/c11/render` (master and 28 stems), `cycles/c11/mvt2-mockup-c11.mp3`, `cycles/c11/metrics`, `build/parts.json`, `build/{mix,roles,note_trims}.json`, `tools/score_to_parts.py`, `tools/deliver_master.py`. Comparisons: `cycles/c00` (cycle 0), `cycles/c06` (five cycles back; its onset timing is unreliable because of memory compression, but its levels are fine), and the reference metrics: Dvorak 9/i in `metrics.md`, plus Brahms 1/ii and 4/ii (two slow movements; stored metrics and loudness series in `symphony/render/critics/c04/ref_brahms*_musopen/`).

Scratch and scripts are in `/private/tmp/claude-501/mockup-loop/c12-C/`:
- `m_c00`, `m_c06`, `m_c11`, `m_mp3`: `symphony/render/tools/measure.py` run on each master and on the mp3, the same tool that produced the Brahms metrics. I ran it with `~/.venvs/stained-glass/bin/python -I`, because the reaper venv has no scipy.
- `sections.py`: section loudness on the real tempo map.
- `motion.py`: macro and phrase-scale loudness motion.
- `ridesim.py`: `deliver_master.py`'s ride re-run on the c11 master with section gains applied.
- `bandstem.py`: per-stem band shares.
- `inner.py` and `tempo.py`: parts.json checks.

## Where the render stands (measured)

| | c00 | c06 | c11 | c11 mp3 | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|---|---|
| I (LUFS) | -24.2 | -25.1 | -23.7 | -19.9 | -23.0 | -19.1 |
| LRA (LU) | 20.0 | 23.9 | 21.5 | 14.4 | 15.2 | 16.9 |
| short-term p50, rel. I | -6.4 | -13.0 | -12.6 | | -3.6 | -5.7 |
| L/R correlation | 0.18 | 0.53 | 0.58 | | 0.51 | 0.55 |
| centroid, loudest 10% (Hz) | 448 | 1101 | 1000 | | 835 | 782 |
| std of 10 s blocks, softer half (dB) | 2.0 | 1.9 | 1.5 | **1.0** | 2.2 | 2.2 |
| phrase-scale motion, std of (1 s minus 20 s) loudness | 3.5 | 3.9 | 3.6 | **2.7** | 4.6 | 3.9 |

Delivery for c11: the master measures -23.7 LUFS, LRA 21.5 LU and -3.6 dBTP. The mp3 measures -19.9 LUFS, LRA 14.4 LU and -1.6 dBTP, with a span of 18.9 dB and about 3.5 dB of limiting. The climax rises 14.7 dB over the preceding 20 s in the master and 13.2 dB in the mp3. The median share of 5-s moves kept is 0.82, with 0 inversions.

Since cycle 0 the problems that made the mockup sound wrong outright have been fixed: the stereo image, the 63 Hz boom, missing articulations, dead joins and late entries. Room, seating and spectrum are now inside the reference range. Long notes are shaped: of 515 notes of 2 s or longer, 77 are flat, and 46 of those are harp. What still sounds machine-made is the large-scale shape:
- The two climaxes are not weighted as the score weights them.
- The soft half of the piece (bars 1-52 and the coda) arrives at one loudness.
- The pulse is a metronome between the printed tempo changes.

## 1. The recapitulation climax (bars 78-81, ff) has shrunk to an echo of bar 61. Measured.

**Where:** bars 79-81 (qn 262-271), all winds and strings, compared with bars 61-62 (qn 204-212).

**What is wrong:** both are printed ff tutti. Bar 61 adds trombones and tuba (mf) and timpani ff. Bar 79 has horns f and timpani f, and no trombones. A real orchestra plays bar 79 perhaps 1.5-2.5 dB under bar 61. The render puts it almost 5 LU under. Across the cycles, bar 61 has been built up and bar 79 has been left alone.

**Evidence (measured):**

| | c00 | c06 | c11 | c11 mp3 |
|---|---|---|---|---|
| max short-term (S), bars 59-64 minus bars 78-82 | -0.1 | 2.2 | **4.8** | 4.1 |
| bar 79 minus bar 61 (bar RMS) | -0.2 | -2.5 | **-5.0** | |
| bar 81 minus bar 61 (bar RMS) | -4.0 | -6.6 | **-9.0** | |

- Bar 79 (-22.1 dB) is now softer than bar 60, the f crescendo into the first climax (-20.9).
- From c06 to c11, bars 61-62 rose 2.8 dB absolute. Bars 79-80 did not move (-22.4 to -22.3).

Per stem in bars 79-80 against bars 61-62:
- Vln I: -30.4 against -25.9. Vln II: -32.7 against -27.5. Vc: -33.3 against -27.8.
- Fl2 fell 5.6 dB and Bn2 6.4 dB from c06 to c11.

The cause is in parts.json (`vol_db` at the downbeats, qn 204.5 against 263):
- Bar 61 gets +2 to +9 dB on nearly every track: chained hpgain of 7 dB for the winds, held by `SOST_HOLD_SHARE`, plus the c11 B #1/#2 roles (Ob2 +8.5, Cl1 +7.9, Tuba +6.5, Vln II +5.9).
- Bar 79 gets 0 to +1 dB, and several cuts:
  - Fl1 and Fl2 -5.1 and -5.2 (Fl1 role [262,270,-2] plus pitch trims)
  - Ob2 -3.2, Bn2 -3.8, Hn3 -4.8
  - note_trims at 262: Fl2 -6, Ob2 -4, Bn1 -5, Cl1 -2; Vc 261 -8; Bn1 269 -7
- The f-to-ff step at 259/262 has no hairpin, so no hpgain reaches the arrival.

**Fix:**
- `build/roles.json`:
  - Add [262, 268, 2.5] (end_ramp 2) to Vln I, Vln II, Vla and Cb.
  - Add [262, 268, 2] to Vc, which keeps the existing [262,274,-1] as a chain.
  - Add [262, 268, 3] to Fl1, Ob1, Cl1, Cl2, BCl, Bn1 and Cbn.
  - Change Fl1 [262,270,-2] to 0, and remove it.
- `build/note_trims.json`:
  - Flute 2 262: -6 -> -3. Oboe 2 262: -4 -> -1. Bassoon 1 262: -5 -> -2. Bassoon 2 259: -5 -> -2.
  - Keep Vc 261 -8. It sits on the pickup.
- Take back 1 dB at bars 61-62. Add [204, 212, -1] to every track that carries a c11 bar-61 role, or lower `SOST_HOLD_SHARE` from 0.5 to 0.35.

**Simulated** (`ridesim.py`, case C: +2 dB on bars 79-81 and -1 dB on bars 61-62, through the unchanged `deliver_master.py` ride):
- Climax gap: 4.8 -> 1.8 LU.
- Limiter: 3.5 -> 2.5 dB.
- mp3 LRA: 14.4 -> 15.3. Span: 19.6 -> 17.9 dB.

**Check:** S max for bars 78-82 is 1.5-2.5 LU under bars 59-64. Bar 79 is louder than bar 60. Vln I keeps +3 dB or more over the winds in bars 79-80.

## 2. The soft half of the movement comes out at one loudness: the ppp opening is as loud as the p horn solo, and the coda as loud as both. Measured; musical effect inferred.

**Where:** bars 1-6 (ppp), 7-14 (horn solo p/mp), 15-22 (p solos), 31-52 (pp-mp) and 83-92 (ppp/pp, morendo).

**What is wrong:** the score's soft dynamics are layered. The ppp introduction sits under the dolce espr. horn solo that grows out of it. The p solos sit over pp accompaniments. The coda thins to ppp. In the mp3 all of these come out within 0.5 LU of each other. Inferred listener effect: the first four minutes have no dynamic perspective, and the coda does not recede.

**Evidence (measured):**

Section power-mean of momentary loudness, LU relative to integrated:

| bars | 1-6 ppp | 7-14 | 15-22 | 31-36 | 37-52 | 65-70 | 83-92 |
|---|---|---|---|---|---|---|---|
| master | -15.0 | -13.7 | -13.0 | -12.4 | -12.4 | -15.9 | -15.4 |
| mp3 | -5.5 | -5.6 | -5.6 | -5.2 | -5.1 | -7.5 | -6.7 |

- S max: the intro, the horn solo and the coda all reach -36.1/-36.1/-36.2 in the master.
- In the mp3 the intro is louder than the horn solo (-23.1 against -24.3).
- The std of 10 s blocks in the softer half is 1.0 dB in the mp3 and 1.5 dB in the master, against 2.2 dB in both Brahms slow movements. Phrase-scale motion is 2.7 against 3.9-4.6 (table above).

There are two causes:
1. The global `soft_trim_db` is {ppp 3, pp 3, p 3.5}. It lifts ppp exactly as much as p, so in level only the CC11 layer separates them. Measured stem medians: Vln I ppp -45.3 / pp -45.6 / p -43.2; Cl1 ppp -47.1 / pp -49.4 (inverted).
2. The ride sits at its +10 dB cap in the ppp sections and gives the horn solo only +8.1 dB, so it takes back a further 1.4 dB of the difference.

**Fix:**
- `build/mix.json` `soft_trim_db`: ppp 3 -> 1. Leave pp and p unchanged. Keep the per-track overrides, but where an override lifts ppp above pp (Bassoon 1 ppp 4, Bassoon 2 ppp 5), set it 2 dB under that track's pp value.
- Leave `deliver_master.py` as it is. I simulated ratio 1.7 with cap 9: LRA 15.7, and 17.6 in combination with these changes, which is outside the target.

**Simulated** (case D = finding 1 plus -2 dB on bars 1-6 and 83-92):
- The intro is 1.7 LU under the horn solo and the coda 2.3 LU under it (was +0.1 and -0.8).
- mp3 LRA 16.2, span 18.8 dB, limiter 2.5 dB.

The real trim reaches only the ppp-marked notes, so the section change will be about 1.5 dB and the LRA about 15.8. If LRA goes over 16, use ppp 1.5.

**Check:**
- In the mp3, bars 1-6 are 1.5-2.5 LU under bars 7-14, and bars 83-92 are 2 LU or more under them.
- The softer-half 10 s block std is 1.5 dB or more.
- LRA is 14-16 and the limiter does 3 dB or less.

## 3. The pulse is a metronome between the printed tempo changes: no phrase shaping at all. Tempo map measured; effect inferred.

**Where:** bars 1-34 (about 114 s), 37-46, 65-77 and 83-88.

**What is wrong:**
- In bars 1-34, 101 of 102 beats are exactly 52.0 bpm. The only exceptions are the 0.25 qn caesura dips at qn 29, 42, 48 and 66, each worth 0.08-0.12 s.
- Bars 37-46 are exactly 60 except the caesuras at qn 124 and 140, and bars 65-77 are exactly 52 except qn 237.
- Every phrase ending lands exactly on the grid: the horn solo's cadences in bars 10 and 14, the oboe/violin answers in 16, 18, 20 and 22, and the tutti tune in 26 and 30.

Inferred: this is now the most obvious machine trait at normal listening level. An orchestra under a conductor broadens slightly into a cadence and moves slightly forward through a rising line, even without a printed rit. Performance studies of Romantic slow music (Repp; Todd's phrase-arch model) put phrase-final lengthening at roughly 10-30% of the last beat. I could not measure rubato in the references with the tools here, so the amounts below are conservative.

**Fix (`tools/score_to_parts.py`):**
- Add `PHRASE_ARCS`, applied after `smooth_tempo` and before `add_caesuras`. The phrase list (from the score: melody slurs, breath marks and rests):
  - (18, 30), (30, 42): horn solo, bars 7-10 and 11-14
  - (42, 48), (48, 54), (54, 60), (60, 66): oboe / solo violin
  - (66, 78), (78, 90): tune
  - (90, 102): transition
  - (108, 124), (124, 140): flute, cor anglais
  - (220, 226), (226, 238): retransition horn
  - (238, 250): A2 first phrase
  - (274, 286): coda
- Skip any phrase that overlaps `RAMP_SPANS`.
- For each (a, e):
  - Multiply the tempo by 1.015 from a + 1 qn to the phrase's midpoint, then by 1.0 to e - 2.
  - Multiply by 0.96 over [e - 2, e - 1) and by 0.92 over [e - 1, e).
  - Write the steps on whole-qn boundaries only, so that no step falls inside a caesura's (q0 - 0.25, q0) span. `add_caesuras` then reads the slowed beat as `b_in`.
- Each phrase gains about 0.08-0.12 s net, which is under 2 s for the whole movement. Leads already use `qn_before` on the real tempo map, so they follow automatically.

**Check:**
- The attack gate passes 19 of 19.
- The final-beat lengthening at each listed phrase end is 0.08-0.15 s.
- No caesura exit.
- The total length changes by less than 1%.

## 4. The pp bass clarinet's reed buzz sits on top of the horn solo, and the c11 soft trims made it worse. Measured; audibility inferred.

**Where:** bars 3-14 (qn 6-42). Bass clarinet pp pedal and accompaniment under the Hn1 "dolce espr." solo.

**What is wrong:** a low-register pp bass clarinet should be the darkest sound in the texture. In the render it supplies more 2-6 kHz energy than the solo horn above it, and it is the loudest stem in bars 3-5.

**Evidence (measured, `bandstem.py`, stems in bars 7-14):**
- BCl 2-6 kHz: 30.4 dB (-19.9 dB relative to its own total). Hn1: 27.0 dB (-28.8 relative).
- BCl supplies 67% of the master's 2-6 kHz in these bars, against Hn1's 31%.
- The BCl band is harmonic (spectral flatness 0.016), not noise: it is the patch's pp reed tone.
- Since c06 the BCl stem rose 3.4 dB and Hn1 1.4 dB. Horn over BCl went from 7.5 to 5.5 dB overall, and from -0.8 to -3.4 dB in 2-6 kHz.
- BCl also supplies most of the master's 20-100 Hz here (35.0 of 35.8 dB).

**Fix:**
- `build/mix.json`, Bass clarinet: add `soft_trim_db` {ppp 0, pp 1, p 3.5}, so pp gets 2 dB less than the global value.
- Add an `eq` `highshelf` at 2.5 kHz, -4 dB. Apply it to this track only. The shelf type is the one c09 added for Vln I.

**Check:** in bars 7-14, Hn1 is 7 dB or more over BCl overall and 2 dB or more over it in 2-6 kHz. The BCl solo at bars 31-34 stays the loudest stem.

## 5. The tutti climaxes are lit almost entirely by the first violins: bright, without brass colour. Measured; fix inferred, lower priority.

**Where:** bars 61-62 and 79-80.

**Evidence (measured):**
- The centroid of the loudest 10% of frames is 1000 Hz, against 835 and 782 Hz in the Brahms references.
- The loud-minus-soft shape at 157 Hz is -2.9 dB, against -0.4 and +5.1: the low body does not grow with the dynamic.
- In bars 61-62, Vln I supplies 62% of the master's 2-6 kHz, and the four horns and the trombones supply under 3% each.
- Hn1 is at -48 dB in bars 61-62 (Hn2 -33.4). The unison drop leaves the a2 line to Horn 2 alone, at +3 dB.

**Fix:** in `build/roles.json`, Horn 2, Horn 3 and Horn 4 [204, 212, 2], plus Hn2/Hn4 [262, 268, 2] with finding 1. Do not add more top-end cut on Vln I. The c09 shelf holds the melody margins.

**Check:** the loudest-10% centroid is 900 Hz or lower, and Vln I's margin at bar 61 stays at +3 dB or more.

## 6. Bar 89 still rises in a ppp/pp morendo coda. Measured; small.

Relative to bar 61, bars 87-92 measure -22.3, -24.0, **-21.9**, -22.5, -24.4 and -27.6. Bar 89 is 2.1 dB over bar 88. It is the Vln I pp entry under a printed rit. (c08 C #4 flagged this.)

**Fix:** in `build/roles.json`, Violins I [286, 292, -2]. This joins the existing [292, 304, -3] through `ROLE_CHAIN`.

**Check:** bars 89-92 each sit at or below bar 88.

Do not touch:
- The solo track and its window; the hold_s early fills; BC_SOFT on the violas.
- The seats, widths and hall: L/R correlation 0.58, against 0.51-0.55 in the references.
- The low-end EQ scheme: 63 Hz and band shares are within the reference range.
- The `deliver_master.py` ride parameters (2:1, cap 10, -19.5 LUFS). Fix the shape in the mix, as above.
- The bar 61-62 wind evening and low-brass roles from c11. Only scale them by -1 dB.
- The caesuras, `qn_before` leads and the 0 inversions in delivery.

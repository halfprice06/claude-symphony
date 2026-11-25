# Critic B, cycle 14: balance and levels (render c13)

Method. The c13 stems, as K-weighted (BS.1770) 10 ms frames and as A-weighted 50 ms frames, placed on score qn with the parts.json tempo map. I use A-weighting to compare a melody with its accompaniment in other registers, and K-weighting for levels within one register and for the delivery numbers. Per-pitch sample residuals are each note's level minus its volume envelope (gain, vol_db, soft/dyn trims) minus 0.25 dB per CC11 step (`pgroup.py`). I simulated the proposed changes by scaling the c13 stems, summing them, and running `tools/deliver_master.py` unchanged (`sim4.py`, `simA.py`). Scripts: `/private/tmp/claude-501/mockup-loop/c14-B/`.

## Delivery, c13 (measured)

| | Master | mp3 | All fixes below, simulated |
|---|---|---|---|
| Integrated | -23.3 LUFS | -19.8 LUFS | -19.8 |
| LRA | 23.9 LU | 15.8 LU | 15.6 |
| True peak | -3.6 dBFS | -1.6 dBTP | -1.6 |
| p10-to-max span | 26.7 dB | 18.2 dB | 18.0 |
| Limiter | | 3.2 dB (bars 61-62) | 3.1 |
| Climax rise over the 15-20 s before | 12.7 dB | 10.9 dB | |
| 5 s level moves reversed by the ride | | 0 | |

All delivery targets are met. The limiter works only at qn 204-211 (bars 61-62, peaks from Vln I, Vln II and Vc) and for one 0.1 s window at qn 264.

## What holds (measured)

- Dynamic mapping across families, per-note medians (K):
  - pp: winds -46.6, brass -47.3, strings -47.3.
  - p: -40.3 / -41.1 / -41.7.
  - mp: -38.2 / -38.7 / -38.3.
  - f: -32.5 / -32.9 / -33.1.
  - p sounds like p in every family, within 1.4 dB.
- Melody over its loudest accompanying stem, A-weighted median:
  - Theme A (Vln I+II): +7.8 / +8.8.
  - Theme B (bars 53-56): +8.4. Bars 57-60: +6.9. Bars 70-74: +7.9. Bars 75-78: +9.5.
  - Ob bars 45-46: +8.0. CA bars 47-51: +5.7. BCl: +5.7. Cl1 bars 85-86: +10.5.
- Bar 61 section balance:
  - The melody (Fl1, Vln I) is at 29-35 A. Woodwinds ff are at 27-31, horns f at 20-26.
  - Low brass, printed mf, are at 20-25: one trombone at mf sits just under one woodwind at ff. Rimsky (Principles p. 33, `reference-books/text/rimsky-principles/p0051.txt`) gives trombone = 2 horns = 4 woodwinds in loud passages, so this is a correct reading of the mf.
  - Timpani at 13-22. No family covers the tune.
- Bar 63: the Tbn1 ff marcato solo is 9-14 dB A over the strings' sf > p, as printed.
- The qn 200 timpani crescendo roll (c13's open item) is not hot:
  - In 0.5 qn K windows it is 7.6, 8.4 and 9.4 dB under Vln I at qn 202, 202.5 and 203, inside the 6-9 target.
  - A-weighted it is 10-14 dB under Vln I.
  - c13's figure of 4.7 dB came from a longer window. Do not add the proposed -1.5 role.

## 1. Both horn solos sit only about 2 dB over their pp accompaniment, and the printed mp of bar 12 is not the high point of the first solo (measured)

**Where.** Horn 1 "1. solo, dolce espr." p, bars 7-14 (qn 17-42), over Bn1, Bn2, BCl and harp at pp. Horn 1 "1. solo" p < mp > pp, bars 67-70 (qn 226-238), over Bn1/Bn2 pp, the Cb pedal and the timp ppp roll.

**What.**
- Horn against the energy sum of its accompaniment, A-weighted per beat:
  - Bars 7-14: median +1.9 dB, minimum -3.5. The horn is level with or under the chord at qn 18, 25, 26, 33, 37, 39 and 40.
  - Bars 67-70: median +1.9, minimum -2.5.
- In K the horn is -38..-42 per three-beat window. Each accompaniment voice is -45..-50, and their sum is about -40.5. The solo is about 1 dB over its own accompaniment. Every other exposed solo in the movement is 3-6 dB over its accompaniment.
- c13's Bassoon Eb3 +6 and G3 +4 pitch trims made the chord about 1 dB louder, as intended, which also took 1 dB off the solo's margin.
- In the first solo, the notes under the printed mp (qn 34-38.5, bars 11-13) have a median of -41.2 K. The p notes of bars 7-10 are at -40.3, and the unmarked < > swell of bar 8 peaks at -36.4 (qn 22). The phrase's printed peak is 2 dB under an unmarked swell four bars earlier. The c08 F4 trim (body -5 at qn 32.5-33.75) sits at the start of the bar 11 crescendo and absorbs most of it.
- Delivery, mp3 loudness: intro (bars 1-6) -26.2 LUFS against the horn solo -25.2. That is 1.0 LU, against the c12 target of 1.5-2.5.

**Fix.** `build/roles.json`:
- Add `"Horn 1": [16.5, 42, 2.5]` and `[226, 238, 2]` to its rows.
- Add `[33.5, 38.5, 1.5, 1.0]` so the mp crest of bar 12 becomes the top of the solo. Keep the F4 pitch trim (sample sag).
- Keep [176, 188, -3] and [188, 204, -2, 4].

**Predicted** (simulated with the two +2.5/+2 rows; the crest row was not simulated):
- Horn over its summed accompaniment: +4.4 median (minimum -1.0) in bars 7-14 and +3.9 (minimum -0.5) in bars 67-70.
- mp3: horn solo -24.4 against the intro -26.3, a 1.9 LU gap (target met). Bars 67-70 -24.8 against bars 65-66 -30.1.
- No effect at the climaxes (included in the delivery simulation above).

**Check after the render.** The horn is at least +3 dB A over the summed accompaniment on 80% of beats. qn 34-35 is the loudest point of the bar 7-14 solo.

## 2. Cello cantabile counter-melody: a 9 dB swing between adjacent notes in bars 24-25 and 72-73 (measured)

**Where.** Violoncellos "unis., cantabile" p, the same figure in both statements:
- Ab3 at qn 72 and 244 (bars 25 and 73), both Leg Slur MAX.
- Then C4 at qn 74 and 246 and Bb3 at qn 75 and 247.

**What.**
- Per note (K, first 1.5 s):
  - qn 72 Ab3 -35.3, qn 74 C4 -44.0, qn 75 Bb3 -39.6.
  - qn 244 Ab3 -34.1, qn 246 C4 -42.6, qn 247 Bb3 -38.3.
- An 8.5-8.7 dB fall from one quarter-length note to the next, inside one slur, at a flat printed p.
- Patch residuals, relative to the line's typical +1.5 dB:
  - Ab3 +5.9 (n8, spread 4.2).
  - C4 -3.3 (n6).
  - Bb3 +0.5, F3 +2.0, Db4 +2.5.
- The Ab3 is the loudest note of the counter-melody in both statements, so the line bulges on the tonic and drops out on the next note. The other Ab3 and C4 notes are already covered by onset trims (81, 253, 261) or lie inside crescendos, where note level does not isolate the sample. So these four onsets are the ones to fix.

**Fix.** `build/note_trims.json`, Violoncellos: add `"72": -3, "74": 4, "244": -3, "246": 4`. Do not use a pitch trim: on Ab3 it would also cut qn 253, 261 and 265, which are already trimmed or in the bar 75-80 crescendo.

**Predicted.**
- qn 72/74/75: -38.3 / -40.0 / -39.6.
- qn 244/246/247: -37.1 / -38.6 / -38.3.
- The largest step falls from 8.7 to 1.7 dB. The Vc stays 7-9 dB A under the Vln I+II theme. It was 9 dB under at qn 72, the worst beat.

## 3. Bar 15: the oboe solo's first two beats are level with the pp muted second violins (measured)

**Where.** Oboe 1 "1." p, C5 at qn 42 (already note-trimmed +5 in c13) and the notes to qn 44.5. Violins II "con sord." pp.

**What.**
- A-weighted half beats:

| qn | 42.0 | 42.5 | 43.0 | 43.5 | 44.0 | 44.5 |
|---|---|---|---|---|---|---|
| Oboe 1 | 5.0 | 11.0 | 10.5 | 11.3 | 13.1 | 17.4 |
| Violins II | 4.3 | 9.5 | 10.6 | 11.5 | 11.4 | 9.5 |

- Over qn 42-44.5 the oboe's median margin is +0.7 dB, minimum -0.2. The c13 trim helped only the first half beat.
- Bar 19 (qn 54) now works: the oboe is 2-13 dB over the strings from qn 55.
- The oboe's C5 residual is still -5.6 dB.

**Fix.**
- `build/note_trims.json` Oboe 1 `"42": 5 -> 8`.
- `build/roles.json` Violins II: add `[42, 44.5, -2]`.

**Predicted** (simulated). Oboe over Vln II at qn 42-44.5: median +4.9, minimum +1.9.

## 4. Clarinet B flat 4 is about 3-4 dB hot, so the second clarinet tops the first and the first clarinet tops the mp horn (measured)

**Where.** Clarinets 1 and 2 (same KS Master), Bb4 (70) at qn 178 (Cl1) and qn 190, 196, 242.5, 255 (Cl2).

**What.**
- The Bb4 residual is +3.6 dB against the clarinets' median. Its own neighbours are G4 +3.0, Bb4 +3.6, B4 -1.4 and Db5 -0.3, so the whole G4-Bb4 area is slightly hot and Bb4 is the highest of it.
- Bar 54, qn 178: Cl1 (pp < p) jumps from 6.3 to 15.3 A in one beat and is 4.4-5.4 dB over Horn 1, which is printed mp and leads the line.
- Bars 57-59:
  - At qn 190 (mp) Cl2 is -35.5 K against Cl1 -39.7, and Cl2 is the loudest accompanying stem in bars 57-60 on six beats.
  - At the f arrival, qn 196, Cl2 is -29.7 against Cl1 -32.2.
- This is minor next to findings 1-3: these are inner lines, and the melody stays 7 dB clear.

**Fix.** `build/pitch_trims.json`:
- Clarinet 2: add `"70": -3` (the track already has `_all_arts`).
- Clarinet 1: add `"70": -3` and add 70 to `_all_arts_pitches` ([68, 70]).

**Predicted.**
- qn 178: Cl1 12.3 A against Hn1 10.9.
- qn 190 and 196: Cl2 within 1 dB of Cl1.
- qn 255: -37.3, still 1.4 dB over qn 254 inside the p < f crescendo.

## 5. Final chord: the first violins' top C5 sits 2 dB under the second violins' A flat 4 once the clarinet leaves (measured; the musical weight is inferred)

**Where.** Bars 90-92, qn 297-304. Vln I C5 (pp, then > ppp) against Vln II Ab4. The roles.json row Violins I [292, 304, -6] comes from c12.

**What.**
- A-weighted per beat, Vln I minus Vln II: median -1.9 dB, minimum -3.0 (Vln I 6.2-8.8, Vln II 7.8-10.3).
- Until qn 297 the C5 is doubled by Cl1, so the top is clear. After that the soprano of the closing chord is the quietest violin voice.
- Both parts carry the same printed dynamic, and Vln I has the top note.

**Fix.** `build/roles.json` Violins I: [292, 304, -6] -> [292, 304, -4].

**Predicted.** Vln I minus Vln II at qn 297-303: median +0.1, minimum -1.0. Coda mp3 loudness is unchanged at -26.2 LUFS (included in the delivery simulation).

## Do not touch

- The soft-trim table and its per-track overrides (cross-family p/pp/mp within 1.4 dB).
- `deliver_master.py`, its ride and TARGET_I.
- The bar 61-62 wind and low-brass roles, and the `_all` [204, 212, -1]. The limiter is at 3.2 dB, and the brass mf reads correctly against the woodwind ff.
- The qn 200 timpani roll and `TIMP_HP_DB_FACTOR` 1.0: it measures 7.6-9.4 dB K under Vln I, inside target, so do not add the -1.5 role.
- The c13 Vc div gain +4 and its answers.
- The bassoon Eb3/G3, clarinet Ab4, Cb and CA pitch trims (fix the horn solo margin with the horn role, not by undoing them).
- The Tbn1 accent overrides at bar 63.

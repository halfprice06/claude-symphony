# Critic B, cycle 22: balance and levels (render c21)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for the c21 master and all 32 stems, and placed them on score qn with the parts.json tempo map. Printed marks come from `build/mockup-events.tsv` and score pages 1-8. Control data comes from parts.json (`cc11`, `vol_db`, notes), roles.json, mix.json, note_trims.json and pitch_trims.json. I compare instruments in the same register with K-weighting, and a melody against accompaniment in other registers with both K and A. I simulated each fix by applying its dB shape to the stem frames (0.5 qn ramps for roles rows, 0.04 qn ramps for `JOIN_NOTCH`). Scripts are in `/private/tmp/claude-501/mockup-loop/c22-B/` (the c21-B set re-pointed at c21, plus `spread.py`, `bulge.py`, `buried.py`, `harpall.py`, `harpatk.py`, `fine.py`, `simbn.py`, `simcb.py`, `climband.py`, `lowref.py`).

## Delivery, c21 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -3.9 dBFS | -1.6 dBTP |
| p10-to-max short-term span | 26.5 dB | 18.5 dB |
| Climax rise over the 15-20 s before | 13.1 dB | 11.3 dB |
| Limiter | | 1.9 dB |
| 5 s moves reversed by the ride | | 0 |

The loudest short-term window is at 230.2 s (qn 208.6, bar 62). None of the fixes below touches bars 61-62 or 79-80. Findings 1, 2 and 4 lower short bumps in soft passages, so p10 may fall by up to 0.1-0.2 dB. Finding 3 raises a p/pp harp line by 4 dB. Both effects are inferred to be well inside the targets.

## What holds (measured)

- The CC11 map is the same in every family at note onsets: ppp 22, pp 34, p 49-54, mp 61-65, mf 71-77, f 88, ff 114.
- Note-median K levels by printed dynamic are in order on every sustained track.
  - pp: winds -45.6..-47.2, strings -45.3..-47.1, horns 3/4 -47.6/-48.3.
  - p, accompaniment: -41.3..-44.7. p solo lines: -37.5..-39.1.
- c21 open item, bar 56 -> 57. The RMS step of -1.7 dB comes from the low end. Summed K: bar 56 -26.0, bar 57 -26.5, bar 58 -23.2. Summed A: 26.3, 27.6, 30.7. The crescendo is not reversed.
- c21 open item, Vc in bars 57-58. Vc minus Vln I per beat, K: -6.8, -5.6, -3.1, -1.9, -3.1, +0.4, -2.8, -1.1 over qn 188-195. A: 4-9 dB under. This is inside the c21 target.
- Solo margins over the accompaniment, A-weighted median:
  - Horn bars 7-14 +5.8, oboe bars 15-16 +7.9, solo violin +7.1, BCl +6.4.
  - CA bars 41-44 +10.0 against the pad without the flute canon; the flute is 0-8 dB A under the CA except in bar 44 (p, both voices held).
  - CA bars 47-51 +6.0, horn bars 67-70 +6.5. Cl1 bars 85-88 is 13-18 dB A over each accompanying stem.
- Tutti section balance follows Rimsky-Korsakov. At bars 61-62 and 79-81, the 700-2000 Hz band is led by Fl1/Fl2/Vln I/Ob1 (each -6.6..-9.7 dB relative to the band total). The tuba (mf) and Cb (ff) own 60-250 Hz, with the Cb 4 dB over the tuba. Timpani rolls settle 5-8 dB under the texture after their strokes.
- Vln I and Vln II in unison: Vln I minus Vln II is +0.7 K in bars 22-30 and -0.3 K in bars 52-56.

## 1. Bassoon 2 rises to the level of the solo three times in exposed soft passages (bars 10, 45, 69) (measured; cause partly inferred)

**Where.** Bassoon 2, pp accompaniment:
- qn 27-30 (bar 10), under the horn solo (p).
- qn 140-144 (bar 45), under the oboe solo "dolce espr." (p).
- qn 232 (bar 69 downbeat), under the horn solo (p < mp).

**What.**
- Bar 10, Bb2 held 3 qn. The note sits at -50..-52 K, then swells to -40.2..-40.6 at qn 28.3-28.7 and falls back by 29.2. That is +11 dB inside a pp note.
  - The horn is at -37.5..-38.0 there, so Bn2 comes within 2-3 dB K of the solo.
  - At the horn's note change (qn 28.8-29.0) Bn2 is 1-13 dB K over the horn.
  - The other pp accompaniment (Bn1, BCl, harp) is at -48..-54.
- Bar 45, Bb2 whole note. The same shape: -52 at qn 140.5, -39.6 at 141.9, -53 at 142.8. The oboe is at -36..-38 K.
  - The oboe's margin over the pp pad (Vln II, Vla, Cb, Bn2) falls to +1.6..+2.1 K at qn 141-143. It is +5.8..+7.5 in the beats around.
- Bar 69 entry, Db3. The first 0.2 qn measures -34.2 K, against the note's own body of -43.7 and the horn's -38.4. That puts a pp accompaniment entry 4 dB K over the solo. A: Bn2 16.5 against the horn 14.1.

**Cause.**
- Bars 10 and 45: the long-note CC11 swell takes Bn2 from 34 to 38 (`score_to_parts.py` contour "swell", +4 CC at 40%), with vol_db up to +1.5.
- Across all of Bn2's held notes, the Bb2 level at each CC11 value is: CC 34 -51.9, 35 -52.5, 36 -49.5, **37 -41.4**, 38 -41.3. Other pitches rise 1-3 dB per CC unit in the same range: Ab2 -45.2 -> -43.7, Eb3 -43.8 -> -42.4. So the Bb2 sample in the Bassoon KS Master (Bn2 shares Bn1's patch) jumps about 8 dB at CC11 37. I infer this is a dynamic-layer boundary.
- Bar 69: an entry transient on the moved start at qn 231.947. vol_db is -2 there, then -4.8.

**Fix.**
- `build/roles.json` Bassoon 2: add `[28.2, 28.8, -7]` and `[141.5, 142.3, -7]`.
- A cleaner alternative in code: cap the CC11 swell for this pitch, e.g. a new `SWELL_CC_CAP = {"Bassoon 2": {46: 36}}` checked where the "swell" contour adds +4 CC (`score_to_parts.py` near line 1541). This keeps Bb2 on the lower layer. It would also cover the smaller Bb2 bumps at qn 144-147 and 247 (+5..+7 dB). Use one or the other, not both.
- `tools/score_to_parts.py` `JOIN_NOTCH`: add `"Bassoon 2": [(231.95, 232.15, -7.0)]`.

**Predicted** (`simbn.py`, shapes applied to the stem frames):
- Bar 10: Bn2 -47.5 K over qn 28.25-28.75, against the horn at -37.9 and Bn1 at -49.6. It sits with the other bassoon, about 10 dB under the solo.
- Bar 45: the oboe margin over the pad at qn 141/142 goes from +1.7/+2.1 to +3.3/+3.1 K. Bn2 goes from -41.9 to -48.1.
- Bar 69: the entry goes from -37.1 to about -42.2 K over qn 232.0-232.25. That is 3 dB under the horn.

## 2. Double basses: the E flat 2 sustain sample swells 5-8 dB at 1.6 s, which puts the basses level with or over the theme A melody (bars 22, 26, 29) (measured)

**Where.** Double basses, every held E flat (MIDI 39) of about 3 qn:
- qn 63 (bar 22, pp).
- qn 75 (bar 26, p, theme A).
- qn 84 (bar 29, mf with a printed decrescendo to the p of bar 30).

**What.**
- Every one of these notes rises 2 dB over its early sustain at +1.40 s after the moved start and peaks at +1.60-1.65 s: +5.2, +6.6 and +8.0 dB. There is a smaller second rise at +3.0 s.
- The CC11 and vol_db curves are flat or falling at these points. In bar 29, CC11 falls 62 -> 52, so the rise comes from the sample.
- Bar 29, qn 85.07-85.64 (inside the printed decrescendo of the theme A cadence):
  - Cb -36.6 K, against Vln I -43.1 and Vln II -41.2, which carry the tune, and Vc -43.5.
  - The basses are 6.5 dB K over the melody for 0.6 qn. At the 0.2 qn scale they go from -42.6 to -35.0 and back to -41.9 within one beat.
- Bar 26, qn 76.07-76.57: Cb -38.4, level with Vln I (-37.8) and 5 dB over the note's own body.
- `melacc.py` flags qn 87-89 as the weakest points of theme A: the melody is 4.8-6.6 dB K under the summed accompaniment.

**Fix.** `tools/score_to_parts.py` `JOIN_NOTCH`, new entry: `"Double basses": [(64.12, 64.50, -4.0), (76.10, 76.62, -5.0), (85.10, 85.62, -6.0)]`. These are score-qn positions for the c21 tempo map and the c21 `ABUT_LEAD` start (0.16 s early). If the tempo or the lead changes, place them at the moved start + 1.40..1.95 s.

**Predicted** (`simcb.py`):
- Over qn 85.10-85.62 the Cb mean goes from -36.1 to -42.1 K, level with Vln I (-43.4) under the decrescendo.
- Bar 26: -38.2 -> -43.2, 5 dB under Vln I.
- The note's contour stays within ±2 dB of its sustain. There is one 0.05 qn frame 2-3 dB low at each notch's end; move the end by 0.05 qn if the stems show it.

## 3. Bar 60: the cello line swells 7 dB K over the melody on the legato join into F3 (measured)

**Where.** Violoncellos, qn 200.5-200.9 (bar 60, beat 1, f with a printed crescendo to the ff of bar 61). There is a smaller swell at qn 202.85-202.95 (beat 3). Vln I holds the melody's whole note ("poco allargando").

**What.**
- Vc per 0.05 qn: -28.4 at qn 200.2, rising to **-17.0 at 200.75**, then -25.8 at 201.0. That is an 11 dB swell lasting about 0.4 s.
- Vln I is at -23.4..-24.5 over the same frames, so the Vc is 7 dB K over the melody. Per beat it is the loudest stem at the start of bar 60 (-22.2 K at qn 200). `metrics.md` ranks the Vc loudest in bars 58, 60, 61 and 62 in RMS.
- In A-weighting the Vc stays 2 dB under Vln I (27.3 against 29.3). So the bump is low-mid weight (150-400 Hz), which K and the ear count more than A does.
- At qn 202.85-202.95 the Vc reaches -18.8, 4 dB over Vln I (-22.6).

**Cause** (inferred). The Leg Slur transition into F3 (note at qn 200.77, velocity 124, the fastest and loudest transition layer) sounds before the moved onset, on top of the c06 crescendo gain (vol_db +1.7 there). The early fill at 201.0 (+4.45) comes after the peak, so it does not cause it.

**Fix.** `JOIN_NOTCH` Violoncellos: add `(200.52, 200.90, -5.0)` and `(202.84, 202.97, -3.0)`.

**Predicted:** peak -17.0 -> about -22.0 K, 1-2 dB over Vln I. At qn 202.9: -18.8 -> -21.8. The crescendo into bar 61 is unchanged, because Vc per beat at qn 201-203 does not move.

## 4. Bars 71-78: the harp's p/pp chords are buried, 17-25 dB A under the mix at their attacks (measured level; audibility inferred)

**Where.** Harp, qn 238-262.
- Bars 71-74: pp low octave/fifth dyads doubling the Cb.
- Bars 75-78: p rolled chords and bass notes under the reprise (score p. 6).

**What.** Harp onset level minus the master in the first 0.2 s, A-weighted, and the harp's share of the master's 1-5 kHz band (`harpall.py`), by passage:

| Bars | Printed | A rel. median (max) | 1-5 kHz rel. median |
|---|---|---|---|
| 7-14 | pp | -14.4 (-9.9) | -18.0 |
| 37-44 | p | -15.9 | -25.6 |
| 53-56 | mp/p | -12.3 (-4.5) | -16.9 |
| **71-78** | **pp/p** | **-18.5 (-13.4)** | **-32.2** |
| 81-82 | mf/p | -15.5 | -24.2 |

- Bars 71-74 dyads: -17..-25 A. Bars 75-78 chords: -13..-19 A. Bass notes: -25..-27 A.
- These are the lowest values of any harp passage, 4 dB under bars 7-14, where the harp is also pp under a solo.
- Causes:
  - The harp track gain is -4.
  - The c20 C #1 `_all` row `[250, 258.5, -3, 5.5]` takes another 3 dB in bars 75-77.
  - Nothing lifts the harp in this passage (harp roles cover only qn 108-140 and 172-188).
- Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt` lines 1803-1816) calls the harp "never a very powerful instrument" and an instrument of colour. Here the colour is missing: at -18 dB A at its own attacks, I infer the chords are masked by the p/mp strings and woodwinds and add no pluck to the reprise.

**Fix.** `build/roles.json` Harp: add `[238, 262, 4]`.

**Predicted:**
- Onsets about -14.5 A relative in bars 71-78, the same as bars 7-14.
- The harp's low dyads stay 3-5 dB K under the Cb they double (harp -47..-53 K plus 4, against Cb -43..-48).
- The low-band total in bars 71-74 rises by about 0.5 dB (inferred from the levels).

## 5. Smaller items, measured, for the actor's judgement

- Bar 65, strings pp after the bar 64 p decrescendo. Vln II rises from -46.8 to -40.9 K across the tied note (qn 220-222.5) while its vol_db falls. Summed string K: bar 64 beat 4 -38.5, bar 65 -39.6/-38.7/-38.2. The pp is about as loud as the end of the p bar. This is the bowed sustain sample swelling. A `[221, 223, -2]` row on Violins II would make the pp step audible, but it works against the c19 `_all [220,226,2]` lift, which was made for the mp3's soft passages. Leave it unless the soft targets have room.
- Harp roles `[124, 140, -7]` (bars 41-44): the harp is -25.6 dB in 1-5 kHz under the CA solo. The CA margin is +10 A without the flute, so 2-3 dB of this cut could be returned if the chords should be heard. Not required.

## Do not touch

- The CC11 dynamic map and the family soft trims (consistent pp to ff).
- Tutti balance at bars 61-62 and 79-81: woodwind/violin top line, tuba mf under the Cb ff in 60-250 Hz, the timpani settle.
- The c21 B rows: Vc/Cb `[188,204]` -3/-1, Vc trims 190/193, Bn2 skips 193/198, Fl1 `[191.5,196,-3]`, Fl1 bar 37-40 lift and trims, Hn1 `[176,188,0.5]`, Harp 26 -5.
- The solo margins listed under "What holds".
- Timpani levels, `deliver_master.py`, and the `_all` soft-passage lifts.

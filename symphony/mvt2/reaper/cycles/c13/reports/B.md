# Critic B, cycle 13: balance and levels (render c12)

Method. K-weighted (BS.1770) levels in 10 ms frames from the c12 stems, placed on score qn with the parts.json tempo map. A-weighted 50 ms frames were used where instruments in different registers are compared (melody against accompaniment), because K-weighting overstates the low strings and the harp body at these playback levels. Per-pitch sample levels were estimated as the note level minus its volume envelope (gain, vol_db, soft/dyn trims) minus 0.25 dB per CC11 step, compared with notes within 3-4 semitones on the same patch (`pscan.py`, `pgroup.py`). Delivery was simulated by scaling stems with the proposed dB spans, summing, and running `tools/deliver_master.py` unchanged (`sim3.py`). Scripts: `/private/tmp/claude-501/mockup-loop/c13-B/`.

## Delivery, c12 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -23.6 LUFS | -19.8 LUFS |
| LRA | 23.9 LU | 15.7 LU |
| True peak | -3.9 dBFS | -1.6 dBTP |
| p10-to-max span | 26.9 dB | 18.4 dB |
| Limiter | | 3.0 dB (bars 61-62, 1.1-3.5 dB; bar 80, 1.2-1.6 dB) |
| Climax rise over the level 15-20 s before | 12.8 dB | 11.1 dB |
| 5 s level moves reversed by the ride | | 0 |

All delivery targets are met. The limiter peaks come from Violins I/II and the celli at qn 204-211, not from brass or timpani. All fixes below together, simulated: mp3 LRA 15.9, span 18.2, limiter 2.9, master peak unchanged (-3.91 dBFS).

## What holds (measured)

- Cross-family dynamic mapping, per-note medians (K): pp winds -47.5 / brass -47.3 / strings -47.4; p -40.9 / -41.1 / -41.9; mp -38.5 / -38.7 / -38.3. p sounds like p in every family to within 1 dB.
- The c12 fixes landed:
  - Theme A: Vln I qn 68-70 at -35.5..-35.7, level with the qn 65-67 energy mean (-35.3). The mf at qn 82 (-31.3) is 4 dB over that mean and 2.1 dB over qn 72.
  - Bar 1: Vln I -47.6 against Vln II -48.0. Bars 89-90: Vln I -45.0, Vln II -44.4.
  - Coda horns con sord. at qn 286-294: -46..-49, level with the strings (-43..-49).
  - Bar 34: CA level with or under the BCl solo.
- Melody over its loudest accompanying stem, A-weighted median: Hn1 bars 7-14 +5.1; theme A +8.3/+8.8 (Vln I+II); BCl bars 31-36 +5.4; Fl bars 37-40 +5.1; Ob bars 45-46 +7.6; CA bars 47-51 +5.6; bars 70-74 +3.9; Cl1 bars 85-86 +10.5.
- Timpani: no roll is the loudest stem. The ff roll at qn 204 is 13 dB (A) under Vln I; the ppp rolls are at -55 K.

The remaining balance faults are local. Most of them are pitch-dependent sample levels that put single notes 5-9 dB out of line with the printed dynamic, mainly in instruments that no earlier pitch trim covers (clarinets, bassoons, oboe, double basses).

## 1. Clarinets: A flat 4 sounds 8 dB weaker than its neighbours on both clarinets, so the tonic drops out of the inner lines (measured)

**Where.** Clarinet 2, 12 notes: qn 194, 200, 210, 238, 241, 244, 250, 253, 254, 261, 262, 271 (bars 58-62, 70-76, 79, 82). Clarinet 1, 3 notes: qn 204, 250, 259.

**What.** Residual sample level by pitch (both tracks use the same KS Master):

| Pitch | Ab4 (68) | G4 (67) | Bb4 (70) | F4 (65) |
|---|---|---|---|---|
| Residual against neighbours | -8.2 dB (n15) | +4.9 (n2) | +5.9 (n6) | +6.3 (n4) |

Ab4 sounds as written B flat 4, the throat note; the sample reproduces its weakness in full. Consequences:
- Bars 71-72 (Cl2's pp line): Ab4 -52.0 and -49.8 K against F4 -44.6, Bb4 -43.0 and Db4 -47.2.
- Bars 75-77: Cl2 Ab4 at qn 253-254 is -44.7/-44.0, then Bb4 at qn 255 is -34.2. The printed p < f over three bars plays as a 10 dB step in one beat (A-weighted 11.2 -> 21.3).
- Bar 79 downbeat, ff: Cl2 (Ab4) -35.0 against Cl1 -29.2. The second clarinet is 6 dB under the first on the same dynamic.

**Fix.** `build/pitch_trims.json`:
- `"Clarinet 2": {"68": 6, "_all_arts": true}`. Cl2 plays only Sus Non Vib, so without `_all_arts` the trim does nothing.
- Clarinet 1: add `"68": 6` and `"_all_arts_pitches": [68]`. Keep 79 -6 and 80 +5.

**Predicted** (stem gain):
- Bars 71-72 Ab4: -46.0/-43.8, level with the line.
- qn 253-255: -38.7, -38.0, then -34.2. A 4 dB rise inside the crescendo.
- qn 262: Cl2 -29.0, level with Cl1.

At the climaxes this adds about 0.3 dB to the master. It is included in the delivery simulation above (limiter 2.9).

**Check after the render.** Cl2 Ab4 notes within 3 dB of the neighbouring notes at the same CC.

## 2. Bars 15 and 19: the oboe solo starts 3-9 dB under the pp strings; a hot viola F4 covers it in bar 19 (measured)

**Where.** Oboe 1 "1." p, first note C5 (dotted quarter): qn 42 (bar 15) and qn 54 (bar 19). Violas pp F4 (65): qn 54 (bar 19) and qn 48 (bar 17, under the Vln I solo).

**What** (A-weighted, half beats):

| qn | 42.0 | 42.5 | 54.0 | 54.5 |
|---|---|---|---|---|
| Oboe 1 | 3.0 | 6.0 | 2.9 | 5.8 |
| Loudest accompaniment | Vln II 4.3 | Vln II 9.5 | Vla 8.6 | Vla 14.9 |

- The solo is audible only from its second note. Per note (K), Ob1 C5 is -50.6 (qn 42) and -50.9 (qn 54), against -44.3 and -39.9 for the next two notes, with CC11 only 11-14 higher.
- The pitch residual for Ob1 C5 (72) is -5.7 dB against its neighbours (qn 42, 54, 143, 200).
- In bar 19 the viola's F4 is the loudest stem of the bar (-39.2 K), 9.5 dB over the other viola pp notes within 10 qn. Its residual at pp is -55.7 against -63..-66 for E4, C4 and Db4. At mf (qn 81-83) the same pitch is not hot, so this is the pp layer only.
- The existing Violas F4 -8 pitch trim applies to pizz. only (`"_arts": ["Pizz RRx4"]`).

**Fix.** `build/note_trims.json`:
- Oboe 1: add `"42": 5` and `"54": 5`. These are onset trims, not a C5 pitch trim, because Ob1's C5 at qn 200 is inside the bar 60 crescendo.
- Violas: add `"54": -7` and `"48": -4`.

**Predicted** (A-weighted):
- qn 54/54.5: Ob1 7.9/10.8 against Vla 1.6/7.9, so the oboe leads by +6.3/+2.9 instead of trailing by -5.7/-9.1.
- qn 42/42.5: Ob1 8.0/11.0 against Vln II 4.3/9.5.

**Check after the render.** Ob1 over the loudest accompanying stem by at least +2 dB from qn 42.25 and qn 54.25.

## 3. Bassoons: E flat 3 is 6 dB weak and G3 5 dB weak, so the pp chords under the horn solo lose their fifth (measured)

**Where.** Bassoons 1-2 (same KS Master), 15 Eb3 (51) notes: qn 18, 27, 30, 31, 36, 100, 102, 180, 193, 198, 200, 243, 256, 261, 268. Five G3 (55) notes: qn 23, 38, 198, 232, 235.

**What.**
- Residuals against neighbours: Eb3 -6.2 dB (n15, the largest group on the patch), G3 -4.8 (n5).
- Bars 7-14, pp chords under the Hn1 solo, per note (K):
  - Bn1: Eb3 -53.3, -52.2, -55.5 and G3 -51.8, -51.5, against Ab3 -44.2..-47.9.
  - Bn2: Eb3 -52.7, -51.3 against C3 -44.2..-46.6 and F3 -46.0.
- The pp chord changes its internal balance by 8 dB from note to note, and the dominant (Eb) falls under the BCl and the harp.
- Bars 35-36 (BCl solo ending): Bn1 Eb3 -52.0/-55.9 against Bn2 -51.0 in the same chord.

**Fix.** `build/pitch_trims.json`:
- `"Bassoon 1": {"51": 6, "55": 4, "_all_arts": true}`
- Bassoon 2: add `"51": 6, "55": 4` (the track already has `_all_arts`; keep 49 -5).

**Predicted.** Bars 7-11: Bn Eb3 -46..-49.5 and G3 -47.5..-48, within 1-4 dB of the other chord tones.

## 4. Double basses: E flat 2 is 6 dB weak and D flat 2 4 dB hot, so the bass line bulges and drops out (measured)

**Where.** Double basses on Sus MAX:
- Eb2 (39), 13 notes: qn 63, 71, 75, 84, 180, 193, 220, 243, 256, 261, 268, and others.
- Db2 (37), 19 notes.
- Ab1 (32) is still +4.7 after the c07 -5 trim. I leave it alone: it is the tonic pedal in bars 2-3, 52 and 89-92, and Cb sits level with Vc there.

**What** (K, per note):

| Passage | Notes |
|---|---|
| Bars 27-29 | Db2 -36.0, -35.2 (qn 80, 81) -> Bb1 -38.2 -> Eb2 -46.1 (qn 84). An 11 dB drop where the printed mf > accounts for about 3 dB. |
| Bars 55-56 | Gb1 -38.8 -> Eb2 -42.3 -> Db2 -34.7 (qn 178, 180, 182). |
| Bar 58 | Bb1 -39.5 -> Eb2 -45.3 -> Ab1 -38.0 -> Db2 -35.5 (qn 192-195). |

Residuals: Eb2 -5.5 dB (n13), Db2 +3.8 (n19).

The same bass line on the celli has no such holes (Vc residual spread is under ±5 dB). The Db2 bulge is also what made bar 53's Cb read 5 dB over the theme B entry in K-weighted level. A-weighted, the melody is still 8-10 dB on top there, so that is not a cover problem.

**Fix.** `build/pitch_trims.json`, Double basses: `{"32": -5, "37": -2, "39": 4, "_arts": ["Sus MAX"]}`. This replaces `_all_arts`.
- Pizz. Eb2/Db2 are not uneven (pizz. Eb2 -59..-61 against pizz. Db2 -60..-62), so the trims must not reach the pizz. notes of bars 37-44.
- This also removes the Ab1 -5 from the two pizz. Ab1 notes (qn 130, 136). Their residual is -69, already 7 dB under the pizz. Db2, so that is a correction.

**Predicted:**
- qn 84: -42.1 after Db2 -33.2..-37.2, a 5 dB fall inside the printed diminuendo.
- qn 180: -38.3 between -38.8 and -36.7.
- qn 193: -41.3 between -39.5 and -38.0.

## 5. Bars 53-56: the harp's p-mp arpeggios are 3-8 dB under the celli at the same printed dynamic and about 12 dB under the melody (measured; audibility inferred)

**Where.** Harp right-hand sextuplets, qn 172-188, printed p < mp, the same marks as the celli and basses.

**What** (A-weighted per beat):

| qn | Harp | Violoncellos | Bn2 | Vln I+II |
|---|---|---|---|---|
| 172-175 | 0.7-3.9 | 7.8-8.9 | 6.4-10.7 | 15.2-20.2 |
| 176-179 | 1.6-5.8 | 10.5-10.6 | 10.3-12.3 | 18.8-23.8 |
| 180-183 | 9.1-10.1 (mp) | 6.6-15.0 | | |

- The harp's -4 dB role [172, 188] (c03/c04, set when the harp was measured against the CA solo) keeps it the quietest accompaniment stem in its own figure.
- Rimsky (Principles, `reference-books/text/rimsky-principles/p0047.txt`): the harp "is never a very powerful instrument", and the orchestrator has to make room for it. Here the texture leaves that room (single wind lines, strings p), and the figure carries the accompaniment's motion. A further 4 dB cut is not needed for balance. I infer that the harp is masked in bars 53-54.

**Fix.** `build/roles.json`, Harp: delete `[172, 188, -4]`. Keep [108, 124, -4] and [124, 140, -7] under the flute and CA solos.

**Predicted.** Harp 4.7-9.8 at qn 172-179, level with the celli and 9-11 dB under the melody. No measurable delivery change (included in the simulation).

## 6. Cor anglais solo, bars 41-44: D flat 4 dips 4-5 dB under the phrase (measured; small)

**Where.** CA "solo, dolce cantabile" p < mp, Db4 (61) at qn 125, 134 and 151.

**What.**
- qn 125: -44.8 between -41.7 and -42.0.
- qn 134: -44.0 between -38.5 and -39.1.
- qn 151 (the bar 47 pickup): -45.3.
- Residual against neighbours: -4.9 dB (n3).
- The Fl1 countermelody (same p < mp) comes within 2-4 dB of the CA at these notes (A-weighted 14.5-15.1 against CA 16.2-18.1 at qn 132-134).

**Fix.** `build/pitch_trims.json`, Cor anglais: add `"61": 4` (legato notes, which all three are). Keep 69 -5.

## Do not touch

- The soft-trim table and its per-track overrides: pp/p/mp agree within 1 dB across families.
- The c12 theme A note trims, the Vln I [0, 9.2, -5] and [292, 304, -6] roles, and the coda horn roles. All are measured at target.
- The bar 61-62 and 79-81 wind and low-brass roles and the `_all` [204, 212, -1]: the climax gap and wind spread are acceptable, and the limiter is at 3.0 dB.
- `deliver_master.py`, its ride, and TARGET_I.
- The Cb EQ and the Cb/Vc balance in the soft bars. Change the Cb only by the per-pitch trims in finding 4.
- The timpani roll tables and the bar 84 role.

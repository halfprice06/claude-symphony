# Critic B, cycle 21: balance and levels (render c20)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for the c20 master and all 32 stems, and placed them on score qn with the parts.json tempo map. Printed marks come from `build/mockup-events.tsv` and score pages 1-8. Gains come from parts.json `cc11`/`vol_db`, roles.json, mix.json, pitch_trims.json, note_trims.json and early_fills.json. I compare instruments in the same register with K-weighting, and a melody against accompaniment in other registers with A-weighting. I simulated the proposed changes by applying them as dB shapes (0.5 qn ramps for roles, note spans for trims) to the stem frames. Scripts are in `/private/tmp/claude-501/mockup-loop/c21-B/`: `prep.py` (K frames), `melacc.py` (melody group against the summed accompaniment), `accover.py` (accompaniment stems over the melody), `ptscan.py` (pitch-trimmed notes against their neighbours), `trkdyn2.py`/`famdyn.py` (dynamic map), `fenv.py`/`fenvA.py` (one stem against another per 0.25 qn), `flsum.py` (flute against the pad sum), and `sim21.py`/`sim21run.py` (the simulation of findings 1-5).

## Delivery, c20 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.6 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -3.8 dBFS | -1.6 dBTP |
| p10-to-max short-term span | 26.5 dB | 18.5 dB |
| Climax rise over the 15-20 s before | 13.5 dB | 11.6 dB |
| Limiter | | 2.2 dB |
| 5 s moves reversed by the ride | | 0 |

None of the findings below touches bars 61-62 or 79-80, so the limiter and the climax peak are unaffected (inferred). Finding 3 raises one p flute line by about 2 dB in bars 37-40, which is a quiet passage, so p10 can only rise.

## What holds (measured)

- The CC11 map is consistent across families: at note onsets ppp 22, pp 34-36, p 46-55, mp 58-74, mf 72-76, f 88, ff 115 on every track.
- Note-median levels, K: winds pp -46.6 / p -39.8 / mp -37.6 / f -32.6 / ff -30.6; strings pp -46.6 / p -42.2 / mp -38.2 / f -32.4 / ff -27.2.
- Section balance in the tutti follows Rimsky-Korsakov (rimsky-principles.txt lines 1966-1990: in forte one string section equals two woodwinds; in piano it equals one):
  - Bar 61: woodwinds summed -18.8 K against strings summed -17.4.
  - Bar 82 (p > pp): woodwinds summed -35.9 K against strings summed -37.6. That is +1.7 dB for ten winds against five string sections, which is what the rule predicts.
- The solo margins over the summed accompaniment, A-weighted median:
  - Horn bars 7-14 +5.8, oboe bars 15-16 +7.9, solo violin bars 17-18 +7.1, BCl bars 31-36 +6.4, CA bars 47-51 +4.6, horn bars 67-70 +6.5.
- No timpani roll is the loudest stem. Low brass at bars 61-62 sit under the Cb and Vc in the 25-125 Hz band.
- The c20 viola lift in bars 23-29 landed: Vla + div are 3-5 dB K under Vln I.
- Cb pizz. onsets in bars 37-44 have a standard deviation of 2.4 dB (0.3 s attack window), which is normal for a section.

The findings below are passages where a line is far from the level its printed dynamic and role imply. Most are old cuts that later cycles have made stale.

## 1. Bars 56-58: the lower strings drop 5-9 dB at the start of the printed crescendo; the cello "espr." line falls under the bassoon that doubles it, and one bassoon note jumps over the tune (measured)

**Where.** Qn 188-196. Score p. 4: from bar 57 (qn 188) every string part has a crescendo from the mf of bar 56 to the f of bar 59. The Vc line is marked "espr." at qn 190. Bn2 (mp) doubles the Vc in unison at qn 188-195.

**What.**
- The vol_db envelope steps down at the barline into bar 57, against the crescendo: Vc +2..+4.9 dB → -5.8 dB, Cb +2..+3.4 → -2.9, Vln II +2..+3.4 → +0.2. CC11 is 72-75 on both sides of the barline.
- Mix bar RMS: bar 56 -29.8, bar 57 -31.5 (master), and -20.1 → -22.6 in the mp3. A crescendo that begins 2.5 dB softer than the bar before it is a reversed dynamic in the delivered file.
- Vc per beat, K, qn 188-191: -41.6, -40.6, -39.8, -39.2. That is 8-10 dB under Vln I (-31.8..-32.3) and 2 dB under Bn2 (-37.3..-39.1), which plays the same pitches at a softer printed dynamic. A-weighted, the Vc is 10-11 dB under Vln I. The espr. note at qn 190 is the lowest.
- Bn2 Eb3 at qn 193 (printed mp) measures -29.7 K and 24.1 A. That is 6.7 dB over its own qn 192 note, and 1.2 dB A over Vln I, which carries the tune at mf. Its G3 at qn 198 is 3.3 dB over its neighbours.

**Cause.**
- Violoncellos `[188, 204, -6, 4]` (c02, when the celli were 9-10 dB over the violins).
- `note_trims.json` Violoncellos `"190": -4` (c05, when the Vc was 0.5-1 dB over Vln I at qn 190; c05 B report line 32). Together they put -9 dB on the espr. note.
- Double basses `[188, 204, -3, 4]` (c05).
- Since then Vln I has gained +5 dB track gain and its own +2 role here, so these cuts are now 6-8 dB too deep.
- Bn2's bumps come from `pitch_trims.json` Bassoon 2 `"51": 6, "55": 4` with `_all_arts`. Those values were measured at soft levels and now also apply in the mp-to-f crescendo.

**Fix.**
- `build/roles.json`:
  - Violoncellos `[188, 204, -6, 4]` → `[188, 204, -3, 4]`.
  - Double basses `[188, 204, -3, 4]` → `[188, 204, -1, 4]`.
- `build/note_trims.json` Violoncellos:
  - `"190": -4` → `-1.5`.
  - Add `"193": -3`. The Eb3 at qn 193 is already a peak in the Vc line, -31.5 K against -34.9 on the beat before.
- `build/pitch_trims.json` Bassoon 2: `"_skip_onsets"` [256, 261, 268] → [193, 198, 256, 261, 268].

**Predicted** (`sim21run.py`, measured on the stems with the shapes applied; the sound is inferred):
- Vc qn 188-191: -38.8, -37.5, -34.3, -33.8 K, which is 2-7 dB under Vln I and 0-4 dB over the Bn2 unison. Bar 58: 1.5-3 dB K and 4.5-5.5 dB A under Vln I.
- Bn2 qn 193: -35.6 K, between its neighbours (-36.5 / -32.2).
- K sum, bar 56 → 57: -26.4 → -27.1 now; -26.2 → -26.6 predicted. Most of the RMS drop is Cb/Vc low end, so the RMS step shrinks more than the K step.
- Target: bar 57 within 0.5 dB K of bar 56, and Vc 2-5 dB K under Vln I through bars 57-58.

## 2. Bar 58: the p flute is 1-6 dB A over the mf violins it doubles in unison (measured)

**Where.** Flute 1, qn 191.5-196. Fl1 (p, cresc.) plays the Vln I tune (mf, cresc.) at the same pitch, up to B flat 6. Ob1 and Vln II double an octave lower.

**What** (per 0.25 qn, `fenvA.py`):
- Fl1 minus Vln I, A-weighted: +3.1, +4.8, -3.4, -4.4, -3.9, +5.8, +1.6, +4.5, +1.1, +5.7, +0.7, +0.9, -2.9, +0.7, +0.9, +5.8, +1.1 over qn 191.75-195.75.
- K per beat: Fl1 -29.2 / -30.7 / -28.6 at qn 193-195, against Vln I -30.8 / -29.7 / -29.1.
- The flute leads the tune for the whole bar, with a 5-6 dB peak on every onset. Bar 57 is right: there the flute is 2-6 dB under the violins.
- This is the same pattern as c20 B #4 (bar 77). A doubling printed two levels softer should colour the line, not take it over.

**Cause.**
- The crescendo takes CC11 from 47 to 86 by qn 195.6, in the flute's loudest register.
- The c16 auto fills put +2.2..+6.0 dB on each onset: `early_fills.json` Flute 1 `"193": 6.0`, `"194": 4.6`, `"195.5": 2.8`, `"192": 2.7`, `"191.5": 2.2`. auto_fills measured dips against the flute's own sustain, not its level against the violins.

**Fix.**
- `build/roles.json` Flute 1: add `[191.5, 196, -3]`. It ends at the f arrival, so bar 59 is unchanged.
- `build/early_fills.json` Flute 1: `"193"` 6.0 → 3.0 and `"194"` 4.6 → 2.5. Note both under `_auto` (as in c20 for 257.5/258.5) so `auto_fills.py` does not raise them again.

**Predicted** (`sim21run.py`): Fl1 minus Vln I, A-weighted, -7.4..+2.8 per 0.25 qn, median about -1.7. The onset peaks fall to +1.1..+2.8. K: the flute is 0-5 dB under Vln I in bar 58. At qn 196 (f) the flute is level with the violins, as before.

## 3. Bars 37-40: the flute's theme B falls under the pp string pad on every short note (measured)

**Where.** Flute 1, qn 108-124, "1." p, theme B. The accompaniment (score p. 2): Vln II div. sul tasto pp (two tracks), violas pp triplets, Vc/Cb pizz. p, harp p.

**What** (`flsum.py`, A-weighted, flute against the summed accompaniment over each flute note):
- Long notes: +2.1..+8.1 dB.
- Short notes: qn 110 -1.3, 110.5 -0.1, 113 -1.9, 113.5 -1.6, 117 +0.9, 117.33 -2.8, 117.67 +1.1.
- Median margin +1.2 dB, minimum -2.8. The other wind solos measure +4.6..+7.9 against their accompaniment in the same way.
- In K, the eighths and triplets measure -42.0..-46.5, which is 4-9 dB under the long notes around them (-37.1..-40.1). Vln II alone (-42.8..-45.4) matches them.
- The pad is correctly soft stem by stem (the flute is 4-8 dB A over each). Three pp string tracks summed come up to the p flute, which is about what Rimsky's piano rule predicts, so the flute needs its own lift. The c20 viola lift (`[108, 124, -4]` → -1.5) added 2.5 dB to the pad here.

**Cause.**
- The flute's legato short notes lose 4-6 dB against the long notes. This is the transition samples (pitch trims 78 +4, 72/73 +3 already apply, inferred not enough).
- The only lift is Flute 1 `[108, 112, 2]`, which ends at the barline of bar 38.

**Fix.**
- `build/roles.json` Flute 1: add `[112, 124, 2]`. It chains to the existing row.
- `build/note_trims.json` Flute 1: add `"110": 4, "110.5": 4, "113": 4, "113.5": 4, "117": 4, "117.333": 4, "117.667": 4`. These are eighth and triplet notes shorter than the 0.6 s ramp, so trim_shape reaches about 3 dB of the 4.

**Predicted** (`flsum.py sim`, simulated as +3 on these notes): margin median +4.1, minimum +1.7 (qn 110). The eighths are within 2-3 dB of the long notes. The pad is unchanged, so Vln II/Vla stay pp in timbre and level.

## 4. Bars 54-56: Horn 1's "espr." counter-line sits under the harp figuration, because of a c06 cut that is now stale (measured)

**Where.** Horn 1, qn 176-188. "1. espr." p → mp, doubled by Cl1 pp → p, against Vln I + II unison (p → mp < mf) and the harp's mp sextuplets (score p. 4).

**What** (per 2 qn, `beatsA.py`):
- Hn1 K -41.5, -41.3, -38.5, -42.5, -41.7, -38.4 over qn 176-187.
- Harp K -41.2, -38.6, -37.7, -37.5, -38.6, -38.6. Vln I K -35.5, -36.9, -36.8, -32.8, -29.8, -33.6.
- A-weighted: horn 10.3-16.4, harp 9.0-13.5, Vln I 17.1-23.5.
- The horn is 3-12 dB under the louder violin section and 0-5 dB K under the harp accompaniment. In qn 182-185 the harp is 3-5 dB over the horn.
- c06 B #5 set Horn 1 `[176, 188, -3]` when the horn was 1 dB over each violin section. Its target was "Horn 1 at least 2 dB under the louder violin section". Since then the violins have gained 5-6 dB in this passage, so the margin is now 3-12 dB, not 2.

**Fix.** `build/roles.json` Horn 1: `[176, 188, -3]` → `[176, 188, 0.5]`. Leave the Cl1 doubling (pp/p) as it is.

**Predicted** (`sim21run.py`, simulated at +3.5):
- Horn K -38.1, -37.8, -35.0, -39.0, -38.2, -34.9. That is about level with the harp, 3-6 dB under the louder violin in qn 176-185, and 1.3 dB K / 3.3 dB A under at qn 186.
- The qn 180 Gb4 (Gb4 pitch trim +4, early fill 4.2) comes to 1.8 dB K / 1.5 dB A over Vln I for one beat. If the actor wants the c06 target everywhere, add `note_trims.json` Horn 1 `"180": -2`.

## 5. Bar 9 beat 3: a harp dyad is 6-8 dB louder than the harp's other onsets and covers the horn solo for a beat (measured)

**Where.** Harp, qn 26 (C sharp 2 + F 3, struck together, velocity 52, printed pp). Horn 1 solo p (score p. 1).

**What** (0.5 qn after each onset, K): the harp onsets in qn 18-41 measure -43.0..-51.7, median about -47.5. The qn 26 dyad measures -39.1 K and 6.9 A. In the same window the horn is -44.4 K and 9.1 A, so the dyad is 5 dB K over the solo. It is the only harp onset in bars 7-14 that comes out over the horn. `accover.py` and `melacc.py` mark qn 26 as the horn solo's weakest point (-2.6 dB K against the accompaniment sum).

**Cause** (inferred): the two notes are struck together with no arpeggio, unlike the other dyads, and the F3 sample is louder. Neither velocity nor METRIC_DB differs from the neighbouring onsets.

**Fix.** `build/note_trims.json`: add `"Harp": {"26": -5}`. Harp note trims use the 0.6 s ramp, which misses a pluck's attack. So implement it either as a harp pitch-trim step (`pitch_trims.json` Harp `{"53": -5, "37": -3, "_skip_onsets": [...]}`, which would also hit other F3/C sharp 2 onsets), or extend the c12 pizz. step shape in `score_to_parts.py` (the `"izz" in art_` branch near line 2147) to Harp note trims. I recommend the second, so that only this onset changes.

**Predicted:** dyad about -44 K, inside the harp's range and level with or under the horn on that beat.

## Do not touch

- The CC11 dynamic map and the family soft trims (consistent across winds, brass and strings at pp to ff).
- The tutti section balance at bars 61-62 and 79-81, including the low brass mf under the Cb/Vc.
- The c20 viola rows in bars 23-29 and 37-40; the c19 BCl/CA, Hn1 crest and a2 horn roles; the bar 60 woodwind rows (c20 B #2); the Fl1 bar 77 values (c20 B #4).
- The solo margins (horn bars 7-14 and 67-70, oboe, solo violin, BCl, CA, Cl1 bars 85-86).
- Timpani levels, including the bar 84 pp strokes.
- `deliver_master.py`.

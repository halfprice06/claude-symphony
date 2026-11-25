# Critic B, cycle 24: balance and levels (render c23)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for every c23 stem and the master, and mapped them to score qn with the parts.json tempo map. I compared the control data in parts.json (`cc11`, `vol_db`, `hpgain`, notes) and the build files (roles.json, note_trims.json, pitch_trims.json) with the printed marks in `build/mockup-events.tsv` and score pages 3-8. I simulated each fix by applying its dB shape to the stem frames. The scripts are in `/private/tmp/claude-501/mockup-loop/c24-B/` (`lib.py`, `prep.py`, `melA.py`, `melacc.py`, `famacc.py`, `look.py`, `pair.py`, `simhn.py`, `sim86.py`, `contrib.py`, `drop.py`).

## Delivery, c23 (measured; ffmpeg ebur128 agrees with metrics.md)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.7 LU | 16.0 LU (target 14-16) |
| True peak | -4.0 dBFS | -1.6 dBTP |
| p10-to-max short-term span | | 18.5 dB (target 16-19) |
| Limiter | | 1.7 dB |

All the fixes below lower or raise short passages of 1.5-3 qn in p/pp music. None of them touches bars 61-62 or 79-80. I infer that the LRA, the span and the limiter move by less than 0.2.

## What holds (measured)

- **Same dynamic, same level in every family** (accompaniment notes, median K):
  - pp: winds -47.5, brass -47.4, strings -46.8.
  - p: winds -42.3, brass -39.9 (n=6), strings -43.8.
  - Each step pp -> p -> mp is 3-5 dB in every family.
- **Solo margins.** In almost every soft solo, the melody minus the loudest other single stem (A-weighted, median per passage) is +6 to +13 dB: horn bars 7-14 +9.6, oboe bars 15/19 +9.9/+9.7, solo violin +9.3, flute bars 37-40 +8.0, CA bars 47-51 +7.4, clarinet bars 85-86 +13.2.
- **The c23 B fixes worked.**
  - Bar 45: Bn2 is 8.7-10 dB K under the oboe.
  - Bar 78: the low octave is under Vln I.
  - Coda: Cl1 at qn 288 is 3.6 dB A over Horn 4.
- **Timpani rolls.** No roll is the loudest stem:
  - The ff/f rolls at 204, 262 and 265 start 5 dB under the loudest stem and settle 10-13 dB under it.
  - The ppp rolls at 3, 226 and 292 stay 7-23 dB under.
  - The one exception is the pp melodic figure at qn 277 (bar 84, the `[277,280,10]` role). It is exposed there and leads by design.

## 1. Bar 55: the horn countermelody's mp arrival is 2-6 dB over the two violin sections that play the theme, and 3 dB over the horn's own solo crests (measured)

**Where.** Horn 1, qn 179.5-181 (bar 55, beat 4 of bar 54 to beat 2; the G flat 4 at qn 180). Violins I and II play theme B in unison, p < mp then <> (score p. 4). Horn 1 and Clarinet 1 play the "1. espr." counter-line, p < mp.

**What.**
- Horn 1 minus (Vln I + Vln II), per 0.5 qn, K / A:

  | qn | 176-179 | 179.5 | 180.0 | 180.5 | 181.0 | 181.5-188 |
  |---|---|---|---|---|---|---|
  | K | -3..-9 | +2.3 | +4.0 | +4.9 | -1.8 | -3..-11 |
  | A | -5..-10 | +1.1 | +2.9 | +5.6 | -2.1 | -5..-13 |

  For 1.5 qn the countermelody is the loudest voice in the orchestra.
- Horn 1 K over each crest:
  - bar 55 (counter-line, qn 179.5-181): **-30.1**
  - bar 12 (solo, p<mp, qn 33-34.5): -33.6
  - bar 68 (solo, mp crest, qn 228.5-230): -32.8

  The counter-line is 2.7-3.5 dB louder than the horn's own solo crests at the same marking.
- Cause, from parts.json. CC11 on this note matches the solo crests (66-70 at qn 180-181; the bar 68 crest is also at 66). The volume envelope is the difference: it jumps from +5.4 to **+11.8 dB at qn 180.15** and holds +8.6..+9.0 to qn 181. Three things stack on the onset:
  - pitch_trims Horn 1 `"66": 4` (all G flat 4s)
  - the c22 `HP_SOFT_GAIN_AT` Horn 1 176: 5.0, held to the arrival
  - early fills

  The note trim 180: -2 ramps in over 0.6 s, so it misses the onset.
- The c22 C #1 rule treated qn 176 as a solo hairpin. Here the line accompanies the violins. Rimsky-Korsakov's balance tables give one horn about the weight of a full string section at the same dynamic. Two violin sections in unison with the tune should therefore sit over one horn at mp.

**Fix.** `build/roles.json` Horn 1: add `[179.25, 180.75, -6.5]` (default 0.5 qn ramps). It chains with the existing `[176, 188, 0.5]`. Do not change pitch_trims `66`, which the other G flat 4s use.

**Predicted** (`simhn.py`, -5 simulated, then scaled to -6.5). Horn minus violins:

| | qn 179.5 | 180.0 | 180.5 | 180.75 |
|---|---|---|---|---|
| K now | +1.3 | +5.1 | +5.5 | +4.3 |
| K with the fix | -3.6 | -1.4 | -1.0 | -1.0 |
| A now | +0.4 | +4.2 | +6.5 | +4.9 |
| A with the fix | -4.6 | -2.3 | 0.0 | -0.6 |

- The horn's crest becomes about -36 K. That is still 2-3 dB over its p start at qn 176 (-38..-39), so the printed p < mp still reads.
- The crest is then 3 dB under the horn's solo crests, which is right for a countermelody.

## 2. Bar 86: the strings' ppp < pp crescendo peaks before its arrival and passes the clarinet solo, while the clarinet fades 8 dB into its breath (measured)

**Where.**
- The strings, qn 283-286: Violoncellos, Violas, Double basses and Violas div, ppp with a printed crescendo to the pp of bar 87.
- The clarinet, qn 284.5-286: Clarinet 1, solo dolce, pp. Its D5 (qn 283-286) ends at the breath mark of qn 286 (p. 7-8).

**What.**
- **Vc K:**
  - -48.4 at qn 283 to **-39.7 at qn 285.5**, which is +8.7 dB for ppp -> pp. A dynamic step is 3-5 dB elsewhere in the strings.
  - Then -41.4..-46.0 at the pp arrival (qn 286-286.5). The crescendo's top comes half a beat before its goal.
  - Vla rises 6 dB and Vla div 7 dB over the same span.
- **Cl1 K:** -39.6 (qn 284) -> -42.5 -> -45.7 -> **-47.8 (qn 285.5)**, then the release. In parts.json:
  - CC11 41 -> 32 over qn 284.4-285.6 (the `swell_taper` contour on a note that ends at a breath).
  - vol_db +7.0 -> +0.75 over qn 283-285.5.
- **Clarinet minus strings (Vc + Vla + Cb + Vla div):**

  | qn | 284.0 | 284.5 | 285.0 | 285.25 | 285.5 |
  |---|---|---|---|---|---|
  | K | +4.8 | 0.0 | -3.9 | -5.8 | -9.4 |
  | A | +10.1 | +5.8 | +2.0 | +0.2 | -2.4 |

  Clarinet minus Vc alone at qn 285.5: -8.1 K.
- The two shapes cross. A printed accompaniment crescendo should not swallow the end of the solo phrase. The score has no decrescendo on the clarinet; the breath only needs the small taper before the gap.
- Contributing cause: the c22 rule `HP_GAIN_SOFT_ACC_DB` (2.5 dB) adds its ramp to a 12-step CC11 rise (22 -> 34).

**Fix.**
1. `tools/score_to_parts.py`: `HP_SOFT_ACC_SKIP = [298.0, 283.0]`. The CC11 rise alone carries the ppp -> pp, as it does for the 131 other hairpins measured before c22.
2. `build/roles.json` Clarinet 1: add `[284.25, 285.75, 4]`. It offsets most of the taper and leaves the last 0.25 qn before the breath falling.

**Predicted** (`sim86.py`):

| qn | 284.5 | 284.75 | 285.0 | 285.25 | 285.5 |
|---|---|---|---|---|---|
| Clarinet minus strings, K | +3.1 | +4.8 | +1.9 | +0.1 | -3.2 |
| Clarinet minus strings, A | +8.9 | +10.2 | +7.7 | +6.1 | +3.8 |
| Clarinet minus Vc, K | +7.8 | +9.6 | +4.6 | +2.0 | -1.9 |

- The strings' crescendo becomes about 6 dB, still the largest step in the passage.
- The clarinet's 0.25 qn breath gap (qn 285.75) is unchanged.

## 3. Bar 83: the last harp harmonic (E flat 6, qn 276) is 7 dB under the one before it and 6 dB K under the ppp cellos (measured)

**Where.** Harp harmonics, qn 275.5-277 (bar 83, a tempo). The harmonics are the only moving voice over Vc/Cb ppp (p. 7).

**What.**
- Note levels, K over the first 1.5 s of each note: 273 -47.0, 273.5 -43.0, 274 -50.4, 275.5 -49.7, **276 -58.3**.
- At its onset, qn 276-276.25, the E flat 6 is -53.1/-57.8 K against the Vc at -47.3/-47.1. In A it is -0.7/-7.6 against -3.0/-1.7.
- The C6 at qn 275.5 is -45.6 K. The figure Ab-C-Eb ends on its weakest note.
- The track's share of the master is -58 dB, but in bar 83 it moves the master by up to 2.1 dB (`drop.py`). The line is meant to be heard.

**Fix.** `build/note_trims.json` "Harp harmonics": `{"276": 5}`. First check that the c21 plucked-step rule (a step on the attack, not the 0.6 s ramp) covers this track as it covers "Harp". If it does not, add the track to that rule's list.

**Predicted:** the E flat 6 onset at about -48 K and +4 A against the Vc. That is still under the C6 before it (-45.6), and the harmonic stays soft.

## 4. Bar 83: the ppp cello pedal under the harmonics swells 6 dB at qn 274.75 although its CC11 falls (measured; cause inferred to be the sample)

**Where.** Violoncellos, qn 274.5-275.5. This is the tied A flat 2 that starts at qn 273.9, ppp, "change bow at will".

**What.**
- Vc K: -50.7 (qn 274.5) -> **-44.9** (274.75) -> -45.4 -> -46.5. It stays at -46..-47 to qn 277.
- In the same frames CC11 falls 28 -> 20, and vol_db rises +0.75 -> +3.9 at qn 274.8. That rise is the `loop_profiles` correction, which is tuned for a dip at this point.
- The bump lands exactly under the harmonics at qn 275-275.25. There the Vc is 9-14 dB K over the harp harmonics.

**Fix.** In `build/loop_profiles.json` or `build/loop_fills.json` (whichever writes the +3.9 at qn 274.8), take that point down by 3 dB for the Violoncellos A flat 2 at qn 274. Or add `JOIN_NOTCH` Violoncellos (274.70, 275.30, -3.0). This sits close to critic A's loop-pulse area. If A reports this bump, use A's value.

**Predicted:** Vc about -48 K at qn 274.75-275.25, level with the rest of the pedal. With finding 3 the harmonics come to within about 1 dB K of the cellos and about 4 dB A over them.

## 5. Bar 19: the oboe's entry note speaks under the strings for its first 0.25-0.5 qn (measured; same as the c23 B #5 item, still open)

**Where.** Oboe 1, qn 54.0-54.5 (bar 19). The strings are pp con sord. and re-articulate on the same beat.

**What.**
- Oboe minus Vln II, K: -3.5 at qn 54.0, -4.5 at qn 54.25. The oboe leads from qn 54.5 onwards (+4.7, and +10..+13 after that).
- At qn 42 (bar 15) the gap is smaller, -1.6..-3.2 K at qn 42.0-42.5.
- The note trims (54: +5, 42: +6) ramp in over 0.6 s, so they arrive after the strings' attack.

**Fix.** Two options. Either make the note trims for Oboe 1 54 and 42 steps on the attack, as the plucked rule does: a per-onset ramp, for example `NOTE_TRIM_RAMP_S = {"Oboe 1": {54.0: 0.1, 42.0: 0.1}}` in `score_to_parts.py` where note trims are built (`ramp = 0.6 * ...` near line 2506). Or add `build/entry_leads.json` Oboe 1 54 0.06. If critic A covers this onset, A's fix takes precedence.

**Predicted** (inferred): oboe about level with Vln II at qn 54.0 and +3 at qn 54.25.

## 6. For the rule 7 memory cut: the level cost of each small track (measured; merge consequences inferred)

`drop.py` gives the largest change in the master (0.5 s windows) if the track were removed altogether. A merge into a sibling instance keeps the notes, so it costs much less than these numbers.

| Track | Largest master change | Where | Windows over 0.5 dB |
|---|---|---|---|
| Oboe 2 (3 notes) | -0.18 dB | | 0 |
| Trombone 2 (4) | -0.19 dB | | 0 |
| Tuba (4) | -0.48 dB | | 0 |
| Flute 2 (5) | -0.56 dB | | 1 |
| Violins II div (5) | -0.65 dB | | 1 |
| Horn 2 (9) | -0.66 dB | | 2 |
| Violoncellos div (8) | -0.80 dB | | 2 |
| Horns 1-2 a2 (8) | -0.97 dB | | 3 |
| Contrabassoon | -1.7 dB | bar 31 | 8 |
| Violas div | -1.55 dB | | 19 |
| Harp harmonics | -2.1 dB | bar 83 | 7 |
| Violin I solo | -9.2 dB | | 26 |

- The first eight rows are the cheapest to merge as far as balance goes. For example, Oboe 2, Flute 2 and Trombone 2 could play their few notes on a polyphonic articulation of their first-desk instance, if the patch allows it.
- Keep the last four rows (Contrabassoon, Violas div, Harp harmonics, Violin I solo) as separate tracks: they carry exposed lines.
- Whatever merges, keep each moved line's level within 1 dB of c23 at bars 61-62 and 79-80 (Fl2/Ob2/Tbn2/Tuba). Their roles there were tuned in c11-c16.

## Do not touch

- The CC11 dynamic map, the family soft trims and `soft_trim_db`: pp/p/mp agree across families within 1-3 dB.
- The climax balance at bars 61-62 and 79-81, including the c16 low-octave rows and their c23 start at 261.5.
- The c23 roles Vc `[73.5,78,-2]`/`[245.5,250,-2]` and Cl1 `[287.4,289,2.5]`.
- `SWELL_CC_CAP` "*".
- The Timpani `[277,280,10]` role.
- `HP_GAIN_SOFT_ACC_DB` everywhere except the qn 283 skip.
- `deliver_master.py`.

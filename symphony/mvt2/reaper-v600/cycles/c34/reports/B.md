# Cycle 34, critic B: balance and levels (on the c33 render)

**Method.** I used the final stems in `cycles/c33/render/`, which include the stem-fixed Violoncellos div, and `build/parts.json`, which equals `cycles/c33/rendered_build/` apart from that stem fix.
- **Level scale.** K-weighted: the BS.1770 response applied to 4096-point spectra, frames every 50 ms, ungated, both channels summed. On this scale the master reads about 3 dB under its gated LUFS.
- **Note bodies.** From onset + 0.15 s to 0.05 s before the note's end.
- **Other bands.** Unweighted 20-100 Hz, 100-300 Hz, 300-2000 Hz and 2-5 kHz.
- **Accompaniment.** The power sum of every other stem.
- **Printed dynamic.** Read from each track's `dyn_curve`.
- **Simulations.** dB arithmetic on the stem frames, using the role and dyn-trim shapes copied from `score_to_parts.py` and `build_reaper.py`. The master is re-summed as stem power.
- **Labels.** "Measured" means a number from the render, parts.json, a table or a patch state. "Inferred" means a judgement about what a listener hears.

## Manual notes (B1: May 2021 HO manual pp. 137, 140, 150-151; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.137, Articulations view: each row has a LOAD button and a VOLUME knob that sets that articulation's loudness. | Rows loaded per track (`UNLOAD_UNUSED_ROWS`). Row-level offsets: Violas Detache sits 13 dB under Leg Slur MAX through the CC7 lane 152.2-167.98; the GENTLE_ACCENT notes play Sus MAX inside Leg Slur lines; the re-bow pieces play Sus MAX. | Load: yes. In `jobs/23_Violas_KS_Master.b64` only rows 0, 2, 6, 10, 16 and 18 are loaded (read). Volume: every `layerMatrix/rows[i]/volume` and `articulations/trigger[i]/volume` is 1.0 in the states (read). The knob acts before the hall and on the whole row, so it could replace the Detache CC7 lane. That lane works (c29), so nothing needs to change. Keep the knob in mind for any future row that is a fixed number of dB off. |
| p.140, Master channel: the GAIN fader sets the instrument's output without changing its mic mix; PAN keeps the relative mic panning. | Track balance. | Balance gain lives in REAPER's volume envelope (`gain_db` plus vol_db), which acts after the Opus hall. Opus channel 0 stays at the patch default (0.966 in the Violas state, read). Seats are written as mic pans (mix.json c05). This is consistent: an envelope gain on a sustained passage scales the hall with it. Only fast falls cut tails (S3), and no fix below uses one. |
| p.150, Note velocity sensitivity: the curve is linear by default (0); velocity selects dynamic layers, "most often used in short instruments". | Harp, timpani and pizzicato, where velocity is the dynamic. | Followed. Sensitivity is 0.0 in the Harp and Timpani states (read). Harp velocities follow the printed dynamic (pp 52-56, p 64-70, mp 74-80, f 100-104 in parts.json). Measured result: p in bar 75 is -35..-40 dB against -44..-47 for pp in bars 71-74, so p sounds as p. |
| p.151, Prepping CCs: send CC1 and CC11 before the first note. CC7 "is best used to set the overall upper limit" of a track; CC11 shapes the line and crossfades the dynamic layers; what CC1 does depends on the library. | The 3 qn pre-roll. CC11 picks the layers and the volume envelope does the balance. CC1 is vibrato on strings and woodwinds and the dynamic layers on brass and clarinets (`CC1_DYN_TRACKS`). CC7 lanes are used for pre-hall shaping. | Pre-roll, CC11 and CC1: as the manual says. CC7 deliberately departs from the manual's "ceiling" use: it carries pre-hall shapes (Detache, the bar 63 lanes, niente, Trombone 1 at 213/215) because the envelope acts after the hall (S3). That departure is correct here. The balance tables follow the manual's split: trims in the envelope, so CC11 keeps each printed dynamic's timbre. |

From MANUAL-GAPS, only #8 (half-section patches for the 4 soli) touches this lens. The celli 4 soli of bars 83-86 are on the DIV track since c33. The basses' 4 soli (bars 65-70 and 87-92) still play the full section at -3 dB. Finding 3 measures the second of those passages.

## 1. The violas are 4-10 dB under the second violins at the same printed mf-ff, and 10 dB under them in bar 75 (measured). The c03/c05 viola cuts went stale as the violins were raised.

**Where.**
- Bars 57-60 (qn 188-204): the violas' triplet and then sextuplet motor of the crescendo into the climax, mp < f.
- Bars 75-78 (qn 250-262): the violas' eighth-note figure, p < f.
- Bars 79-80 (qn 262-268): ff, molto sostenuto.
- Tracks: Violas and Violas div.

**Evidence.**

*Per bar, violas (with Violas div) minus Violins II (with Violins II div), measured, bars where both print the same dynamic:*

| Dynamic | Bars | Median | Range |
|---|---|---|---|
| ppp | 5 | +1.2 | |
| pp | 29 | -2.0 | |
| p | 4 | -1.4 | |
| f | 3 | -5.0 | |
| ff | 6 | -4.1 | |

*Bar by bar, violas against Violins II:*
- Bar 57 (mp against mf): -7.8.
- Bar 58: -8.6.
- Bar 59 (f, sextuplets): -4.8.
- Bar 60: -5.0.
- Bar 75 (p against mp): **-10.5**.
- Bar 78 (f): -7.6.
- Bar 79 (ff): -7.1.
- Bar 80 (ff): -4.5.

*Note medians by printed dynamic (Violas / Violins I / Violins II / Violoncellos):*
- mp: -40.7 / -35.7 / -36.7 / -38.5.
- mf: -39.3 / -32.0 / -33.8 / -34.1.
- f: -35.0 / -27.3 / -28.4 / -30.6.
- ff: -27.3 / -22.3 / -24.2 / -24.9.

*Bar 75 against the winds at the same printed p (measured):*
- The violas' p eighths (-46.1..-48.9) are 5-9 dB under Bassoon 1 (-39.6), Clarinet 2 (-41.2), Horn 2 (-44.6) and the harp (-35.5..-39.9).
- They are softer than their own pp eighths in bars 72-74 (-42.7..-46.7).
- Ranks: the violas are 12th in bar 75 and 16th-19th of 32 stems in bars 79-81.

*Causes (read):*
- `mix.json` Violas and Violas div `dyn_trim_db {"f": -2, "ff": -3}`. Series 1 c03 set these when the violas were the loudest stem at bars 61-62. That critic's target was "Vla at Vln II -1 ±1 dB at every dynamic".
- Since then Violins II has been raised: c33 moved its f/ff trims +2 and added roles at 188-204 and 249.9-258.5. Violins I has had roles added.
- `roles.json` Violas `[196, 204, -4, 4]` (series 1 c05) takes another 4 dB off the sextuplets in bars 59-60.
- In bars 75-77 the global row `_all [250, 258.5, -3, 5.5]` applies.
- The violas' soft trims fall from pp 5 to p 3.5, so the printed pp→p step in bar 75 nets about 1.5 dB less than its CC11 rise.
- This is mockup-kit LEARNINGS §13: "Level cuts set early go stale as other tracks are raised."

*Norms:*
- Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt` lines 879 and 1981-1987) gives 14 second violins and 12 violas, "practically the same" in number.
- He treats each string department as equal to one wind in piano and to two winds in forte.
- So violas belong about 1-2 dB under Violins II at the same dynamic. They do not belong 5-10 dB under, nor under single winds at p.
- Adler (adler1.txt line 7931) notes that a viola note can be "much stronger" than the same pitch in the second violins.

**Why it matters (inferred).**
- The inner voice that drives both crescendos is close to inaudible: the sextuplets of bars 59-60 and the eighths of bars 75-78.
- The two big approaches therefore sound like melody plus bass with a hollow middle.
- The ff chords of bars 79-80 lose their alto.

**Fix (level only; `stem_fix.py` can simulate and apply it).**
1. `build/mix.json` "Violas" and "Violas div": `dyn_trim_db {"f": 0, "ff": -1.5}`. The p anchor is unchanged, so nothing below mp moves.
2. `build/roles.json` Violas: `[196, 204, -4, 4]` → `[196, 204, -2, 4]`.
3. `build/roles.json` Violas: add `[249.9, 258.5, 4, 5.5]`. This is the same opening shape as the `_all` row, so the violas end up net +1 dB in bars 75-76, and the gain is 0 at the f arrival (259).

**Simulated.** Results per bar for fixes 1 and 3, with role 2 between the -1 and -1.5 cases simulated:

| Bar(s) | Violas c33 | Violas simulated | Reference |
|---|---|---|---|
| 57-58 | -39.3 / -36.3 | -38.5 / -34.7 | |
| 59 | -34.7 | about -30.3 | Violins II -29.9 |
| 60 | -28.0 | about -25.8 | Violins II -23.0 |
| 61 / 62 | -25.6 / -26.2 | -24.1 / -24.7 | Violins I -20.5 / -19.5 |
| 75 | -46.0 | -41.6 | Violins II -35.5 (mp) |
| 76 / 77 | -39.3 / -35.1 | -35.4 / -32.9 | |
| 78 | -32.0 | -30.0 | |
| 79 / 80 | -30.8 / -28.0 | -29.3 / -26.5 | |

- Bars 61-62: the violas stay 3.6 dB under Violins I, so the c03 problem does not return.
- Master: +0.0..+0.3 dB. The largest moves are bar 59 (+0.3) and bar 76 (+0.3).
- Climax order: bars 61-62 -11.75 / -11.83 against bars 79-80 -14.03 / -14.73 (K-weighted bar levels). The margin is unchanged at 2.3 dB.

**Check after the render.** Violas minus Violins II at f/ff should be -1..-3 dB. In bar 75 the violas should be no softer than in bar 74.

## 2. The celli's pp re-entry in bar 87 (qn 286-289, F2) swells 7 dB at a flat CC11 and becomes the loudest string by 8-16 dB under the clarinet solo (measured)

**Where.** Violoncellos, note 286 (F2, "tutti", pp, 2.92 qn), under Clarinet 1's dolce phrase and the cor anglais's dolce entry.

**Evidence (0.25 qn K-weighted frames, measured).**
- **Celli.** 286.25 -47.3, 286.5 -46.1, 286.75 -42.8, 287.0 -41.6, **287.5 -39.8**, 288.0 -42.7, 288.5 -44.4, 289.0 -48.5.
- **Controls.** CC11 34 throughout. vol_db moves only -4.0 → -2.5 → -4.0, a 1.5 dB swell from the role ramps.
- So the sample itself blooms by about 6 dB at a pp with no printed hairpin.
- **The other strings at 287.5.**
  - Violins II (pp) -48.9: the celli are 9 dB over.
  - Violas (pp, both halves) -54.5: 15 dB over.
  - Basses (4 soli, pp) -55.6: 16 dB over.
- **Over 287-289.** Celli -42.3 against Violins II -49.4.
- **Elsewhere at pp.** The celli's pp median across the movement is -45.6, within 0.3 dB of Violins II (-45.3). So 286 is a local bloom, not a level-table error.
- The c33 report flagged the final chord as bottom-heavy (celli loudest). The same voicing problem starts here, 15 qn earlier.

**Why it matters (inferred).**
- A pp chord whose bass note swells 7 dB on its own sounds like an unmarked crescendo in the celli.
- The swell pulls attention from the clarinet's phrase, which it trails by only 3.4 dB at 287.5 (Clarinet 1 -36.4).

**Fix.**
- `build/roles.json` Violoncellos: add `[286.9, 288.9, -5, 0.5]`. It ramps in over 286.4-286.9 after the attack, is full until 288.4, and opens to 0 at the note's end. The 289 note is unaffected.
- Simulated (0.25 qn): 286.5-289 runs -48.1..-44.8 (mean -46.8 over 287-289, was -42.3). That is 2.6 dB over Violins II and flat with the note's first beat.
- Master: -0.4 dB at 287-288.
- If the actor prefers the shape before the hall (S3), use the same shape as a CC7 lane instead: `CC7_POINTS["Violoncellos"]` += (286.4, 127), (286.9, 71), (288.4, 71), (288.9, 127). 71 = 127·10^(-5/20).
- The role version is level only and goes through `stem_fix.py`.

## 3. The basses' coda 4 soli (bars 87-92, qn 286-304) sit 8-13 dB under the tutti celli at the same pp: the 16-foot A flat is thin (levels measured; target inferred)

**Evidence (measured).**
- **Basses note bodies, 286-298.** -53.7..-56.7. Ranks 9th-11th of the stems.
- **Celli tutti, same notes.** -43.0..-49.4 (-45..-48 after finding 2).
- **Final chord.** 301-303: basses -58.2..-61.4 against celli -54.0..-56.4, a 4-5 dB gap. That part is fine.
- **Against their own tutti.** The basses' full-section pp median is -49.9, so these 4 soli are 5-6 dB under it.
- **Against the c32 target.** c32 B #6 set the 4-soli -3 dB with a target of "3-4 dB under the tutti". The coda pieces landed lower: `_all [283.5, 304, -2]` and the bass row `[292.5, 304, -4]` stack on top of `SOLI_AS_META`'s -3.
- **Low band.** In bar 87 the basses supply only -11.2 dB of the master's 20-100 Hz band; the celli supply the rest.

**Why it matters (inferred).** Under the clarinet and cor anglais duet, the bass of the pedal reads as celli alone. The octave below, which the score gives to four solo basses, is felt only in the last chord.

**Fix.**
- `build/roles.json` Double basses: add `[285.9, 299.75, 2, 0.5]`. It meets the existing `[299.75, 304, 5]`, so `score_to_parts.py` crossfades the two (ROLE_CHAIN) and the final chord is unchanged.
- Expected: basses about -52..-54.5 at 286-298, 3-4 dB under their tutti pp, as c32 intended.
- Master change under 0.2 dB. Level only.
- Do this after finding 2, because finding 2 changes the celli it is measured against.
- Low priority. The timbral answer is still MANUAL-GAPS #8, Basses Divisi DIV A in a second pass.

## Checks asked for in this lens

All measured unless marked inferred.

**Solos over their accompaniment.**
- Each entry gives the 1 qn margin over the accompaniment sum (median and minimum), then over the loudest single stem.
- I also scanned 0.5 qn frames where the solo note sounds, counting frames within 1 dB of the loudest other stem.

| Solo | Over accompaniment (median / min) | Over loudest stem | 0.5 qn frames within 1 dB |
|---|---|---|---|
| Horn 1, bars 7-14 | +1.5 / -0.7 | +5.4 | 1 |
| Oboe 1, bars 15-16 | +4.9 | +7.0 | 0 |
| Solo violin, bars 17-18 | +5.8 | +9.0 | 0 |
| Oboe 1, bars 19-20 | +4.2 | +6.6 | 1 (the 54 entry, +0.3 over the celli) |
| Solo violin, bars 21-22 | +1.0 | +5.2 | 1 (64, phrase end) |
| Bass clarinet, bars 31-36 | +3.1 | +5.2 | 98.0 and 101.5 (see below) |
| Flute 1, bars 37-40 | +3.6 | +8.6 | 0 |
| Cor anglais, bars 41-44 | +2.3 | +5.5 | 0 |
| Oboe 1, bars 45-47 | +1.4 | +6.9 | 0 |
| Cor anglais, bars 47-50 | +2.9 | +6.4 | 0 |
| Clarinet 1, coda bars 85-89 | +0.6 | +5.8 (min +3.2) | 0 |

- **Bass clarinet at 98.0 and 101.5.** It is level with the cor anglais (+0.5 / -0.2). The cor anglais prints p against the bass clarinet's mp there, a 1-2 dB question only.
- **Horn 1 bars 7-14.** In 300-2000 Hz the horn leads the accompaniment by +2.4 dB and every single stem by 7-9 dB. It is heard (inferred).
- **Clarinet 1, coda.** At 282-284 it is 10-14 dB over the ppp pedal, at the level of the p solos of bars 7-22. c32 already cut 280-286 by 2.5 dB, and this render matches c32 exactly at 280-295. I leave it alone to avoid reversing a recent change. It is a solo over ppp, and the duet bars 87-89 keep it only 3-6 dB over the cor anglais (inferred).

**c33 B fixes, re-measured.**
- **Horn 1 at 204.** -20.3, ranked 2nd. Over 205-207: -23.7..-24.6. Horns group at 204-208: -20.3 (c32 -23.0).
- **Violins II minus Violins I.** Bars 59/60: -2.9 / -1.5 (c32 -6..-8).
- **Bass clarinet at 91.** +2.3 over Bassoon 2.
- **Bars 23-24.** Celli over basses +3.4 / +10.9.
- **Final chord.** Celli and violas within 2 dB.
- All held.

**Dynamic mapping.**
- At pp the string sections lie within -45.3..-46.8 and the accompanying winds within -45.7..-47.6. The basses are -49.9, which is acceptable on the K scale for their range.
- At ff the string sections are 3-6 dB over the single winds, which is the forte ratio. The violas are the exception (finding 1).
- p is louder than pp in every family once each is taken in the same passage. Two examples: Clarinet 1 at 175-178 against 182-186, and the harp in bars 71-74 against bar 75.
- The overall medians mix solo roles with accompaniment, so the median p ≈ pp of Clarinet 1 is not a table error.

**Divisi and soli tracks.**
- Violins II div against Violins II, bars 37-40: within 0-3 dB.
- Violas div against Violas: within 2 dB in bars 23-28, and summed 1-2 dB under Violins II in bars 87-91.
- Violoncellos div (4 soli ppp, bars 83-86) against the tutti basses at ppp: -54.6 / -53.9 / -56.2 / -51.7 against -52.3..-52.7.
- 4 soli basses in bars 65-70: about 15 dB under Horn 1.

**Climaxes, bars 61-64 and 79-82 (group sums, K-weighted).**
- qn 204-208: strings -16.1, winds -17.1, horns -20.3, low brass -19.7, timpani -33.9.
- qn 262-266: strings -17.9, winds -17.6, horns -23.3, timpani -31.1.
- **Timpani.** The f roll from 204 ranks 17th-22nd (13-20 dB under the top). At 261-268 it ranks 11th-20th.
- **Low brass at f.** Trombone 2 ranks 2nd-7th at 206-211 (-22.5..-23.9), about level with the ff horns: one trombone ≈ two horns (Rimsky, as above). Nothing covers.
- **Bars 63-64.** Trombone 1's quotation leads as printed.
- **Climax order.** K-weighted bars 61/62 -11.8 / -11.9 against bars 79/80 -14.1 / -14.8.

**Bass.**
- Master 20-100 Hz share against K-weighted total, 1 s windows:
  - soft 30%: -16.2 median (Dvořák 9/i mp3 -18.6);
  - middle: -22.0 (-20.7);
  - loud 10%: -23.0 (-26.8).
- 100-300 Hz: -6.0 / -8.7 / -8.8 against -8.8 / -8.8 / -7.0.
- The heaviest bars (31 and 35 at -9 dB) are the bass clarinet's own chalumeau fundamentals, not a pedal. Bars 83-84 (-8) are the coda's ppp A flat 1. Solid, not boomy. No change.

**Harp after c33's sustain change.** +1 to +3 dB per bar against c32. It is still 8-15 dB under the master wherever it accompanies, so it needs no correction.

**Do not touch:**
- The climax order and the timpani and low-brass levels at bars 61-64 and 79-82.
- Horn 1/2's bar 61 roles (c33).
- Violins II's c33 f/ff trims and roles.
- Trombone 1's quotation levels, accents and CC7/EQ shapes.
- Flute 1's CC7 at 211.96-213.
- The bar 63 and niente CC7 lanes.
- The c32/c33 solo levels: Oboe 1, the Violin I solo with CC1 72 and gain +0.4, Flute 1, the cor anglais, Clarinet 1's coda with the c32 -2.5, and the bass clarinet's bar 31 trims.
- The Violas Detache CC7 lane.
- The celli 4 soli on the DIV track at -5.2.
- The c33 final-chord viola/celli roles.
- The Cb and timpani side shelves.
- The horn CC1 map and the soft-horn loud_eq.
- The harp env_sustain 1.0.

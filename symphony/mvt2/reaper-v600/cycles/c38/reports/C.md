# Cycle 38, critic C: dynamics over time (on the c37 render)

Scope: the loudness arc against the score (the bar 47 fp, the animando crescendo of bars 53-60 into the Largamente of bars 61-64, the bar 66 niente, the ff cadence of bars 79-82, the ppp coda and the bar 91 morendo), the loudness range of the master and the mp3 (BRIEF item 6), swells and loop pulsing on long notes (item 8), and decays.

Method:
- Levels are stereo-power RMS on the c37 stems and master. "S" is EBU short-term loudness (3 s window, centred), "M" is momentary loudness (0.4 s, centred), both read with ffmpeg the way `deliver_master.py` reads them. qn are mapped to seconds through the rendered parts.json tempo map.
- Simulations: each change is applied to the affected stems as a gain curve in qn. This is exact for volume-envelope changes, because the envelope acts after the Opus hall. The new master is the old master plus the stem differences. I then ran a scratch copy of `tools/deliver_master.py`. Unchanged, it reproduces the delivered c37 file: LRA 15.2, span 18.5, limiter 1.9.
- Labels: "measured" means a number from these files; "inferred" means reasoned from them, from the manual or from earlier cycles.

## Manual notes (MANUAL-READING row 38, slot C: D3 = A6's PDF pages 68-71, read for levels; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.68: Hollywood Harp uses solo-instrument mics (vintage close/mid instead of surround); Maestro patches pick articulations by velocity or by CC1 ("MOD") | Harp (stem 21) on `Harp Sus RR.oib`, Harp harmonics (stem 27) on `Harp Harmonics.oib` | Yes. No MOD patch is used, so CC1 plays no part on the harp tracks. |
| p.69: Sustain RR alternates Pluck Long and Thumb Pick by round robin at velocity 1-123, with 5 dynamic levels each; velocity 124-127 plays a nail pick; "CC 11 and Note Velocity control overall loudness" | Every harp note: the bar 7-14 arpeggios (pp), bars 37-44 (p), bars 53-56 figures, the bar 75-78 crescendo and the f stroke at 261 | Yes (measured). CC11 is fixed at 110 and the dynamic comes from velocity: pp v44-64, p v56-76, mp v76-80, f v100-104. No note reaches 124, so the nail pick is never triggered. Median onset level (first 0.25 s) per printed dynamic: pp -46.6, p -43.6, mp -39.5, f -26.5 dB, which is monotone. The bar 7-14 pp arpeggios sit about 4 dB under Horn 1's p theme. |
| p.70: Pluck has 5 velocity levels, Harmonics 2, Nail Pick 2; harmonics have no fundamental and "a float-like quality" | Harp harmonics bar 83 (v58-70, p, dolce) | Yes. All three harmonics are in the lower of the two layers. That suits dolce. |
| p.70-71: Repetition Rep lets repeated notes ring their full length; Gliss maps | None: v600 has no fast harp repeats and no glissandi | n/a |
| p.69-70: plucked notes decay naturally (no sustain articulation) | The A flat 1 at 271 (bar 82), the arpeggio tails under the melody, the harp's last note at 273.5 (the harp is not in the final chord) | Yes since c33 (`env_sustain` 1.0, release 200 ms): the 271 note rings for 8.7 s. One small departure: in the bar 75-77 crescendo (250-256, v66 rising to v80) the onsets zigzag -37.2, -42.3, -36.8, -43.4, -39.5 dB. The velocity steps are in order, but the c36 trim of -4.5 at 253 and the sample's unevenness leave the line uneven. It sits under the strings, so it is not ranked. |

MANUAL-GAPS items that touch this lens: #7 (Felt Cresc rolls) is still untried; the rolls' crescendos measure correctly with the current shapes (Checked). #2 (repetition rows) is not a dynamics item. Nothing in pages 68-71 calls for a change.

## Findings, ranked by what a listener would hear

### 1. The bar 66 niente: under the dying strings the basses' pedal swells 5 dB, so the passage fades only halfway (measured; fix simulated)

**Where.** Double basses, E flat pedal (4 soli, pp), qn 224.25-226.3. This is the bow piece around the re-bow at 225.215 (`rebow_fills.json` "Double basses" "225.215", raised in c36 A #1). The upper strings play the printed niente from 223 to 226, and Horn 1 enters p at 226.

**What is wrong (measured).** As the niente takes Violins II, violas and celli to nothing, the basses' volume envelope rises from +0..+2 dB to +4.6..+9.3 dB:

| qn | 222.0 | 223.0 | 223.75 | 224.5 | 224.75 | 225.25 | 225.75 | 226.0 | 226.5 |
|---|---|---|---|---|---|---|---|---|---|
| Double basses (0.25 qn RMS) | -53.4 | -54.2 | -53.8 | -51.3 | -48.3 | -48.8 | -48.1 | -48.5 | -53.6 |
| Violins II (0.5 qn) | -47.9 | -48.3 | | -50.9 | | -56.2 | -60.1 | -70.9 | |
| Violas (0.5 qn) | -48.6 | -48.9 | | -56.0 | | -64.7 | -68.1 | -76.7 | |

- The basses become the loudest stem from 224.5 on.
- The master falls only 3.4 dB, from -44.3 at 223 to -47.7 at 225.5.
- Momentary loudness, 222.5-223.5 against 224.9-225.9: master -41.7 -> -45.9, mp3 -30.8 -> -33.9.
- The listener hears an unprinted swell on a pp pedal in the one bar where the score asks the orchestra to vanish. The mp3's 5 s loudness move over 221.2-225.4 also reads as rising (master -1.4/-2.0, mp3 +0.2/+0.7). Part of that rise is the 3 s window reaching Horn 1's entry, so on momentary loudness the niente is shallow rather than reversed.

**Fix.** In `build/score_config.py`, `LEVEL_SHAPES["Double basses"]` += `[(224.0, 0.0), (224.5, -3.0), (225.0, -4.0), (226.25, -4.0), (226.35, 0.0)]`.
- The cut covers both sides of the 225.215 join equally, so c36's join fill keeps its shape relative to the pieces around it.
- It ends where the next piece's own dip begins (vol_db 7.07 -> -5.5 at 226.34-226.5), so no step is added.
- The ramps are slow (0.5 qn), so S3 does not apply.

**Simulated (together with findings 2 and 3):**
- Basses at 224.75-226.0: -52.1..-52.8. The pieces before read -53..-54.6, and 226.5 reads -53.6.
- Momentary 222.5-223.5 against 224.9-225.9: master -43.0 -> -49.0, mp3 -31.9 -> -36.9. The niente's drop grows from 3.1 to 5.0 LU in the delivered file.

**Optional.** The series 1 lift `_all [220, 226, 2]` (c18, made for the old delivery; the current lift is at its cap here) also raises the niente by 2 dB and releases at 225.5-226, under Horn 1's entry. Removing it would deepen the fade by 2 dB more. I did not simulate it.

### 2. Bars 54-57: the "poco a poco animando" crescendo stalls for 10 beats, and the volume envelope steps down 5-6.5 dB at the printed mf (measured; fix simulated)

**Where.** Violins I, Violins II and Violoncellos, qn 178-190. The score marks mp at 178, a crescendo 180-184, mf at 184, a crescendo 188-196 and f at 196.

**What is wrong (measured).** Two shapes meet at the mf arrival:
- c34 C #6's hold `[(179.5,0),(180.5,2.5),(183.1,2.5),(184.1,0)]` ends;
- c30 C #2's mf hold-back `[(183.5,0),(184.25,-2.5),(187.75,-2.5),(188.5,0)]` starts.

Violins I's vol_db therefore falls from +4.05 at 183.1 to -0.8 at 184.25 and -2.5 at 184.6. That is a 5-6.5 dB step down exactly where the crescendo should arrive. The stems peak at 183.75-184.25 (Violins I -29.5) and then drop 5-8 dB (Violins I -37.8 at 185.0).

The result, plain RMS of the master per 2 qn from 176 to 194: -31.0, -30.5, -29.9, -29.7, -29.6, -29.7, -28.7, -28.3, -26.9, -25.4.

| qn | 176 | 178 | 180 | 182 | 184 | 186 | 188 | 190 | 192 | 194 | 196 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| master S | -29.5 | -27.5 | -26.7 | -26.9 | -26.6 | -27.1 | -26.2 | -24.9 | -23.7 | -22.1 | -20.7 |
| mp3 S | -21.1 | -19.6 | -19.1 | -19.8 | -20.0 | -20.8 | -20.4 | -19.5 | -18.6 | -17.3 | -16.5 |

- The master is flat within ±0.5 dB from 179 to 188, through a printed crescendo and an mf arrival.
- The delivery's lift falls by 2 dB over the same span, because it looks ahead to bars 58-61. So in the mp3 the crescendo and the mf read as a 1.2 LU decline (178 -19.6 -> 186 -20.8; momentary -18.2 -> -21.7).
- c30 held the mf back so that the crescendo to f would carry. Since then c34 raised 180.5-183.1 and the bar 60-61 strings, so the hold-back now cuts a step into the line instead of lowering a plateau.

**Fix.** In `build/score_config.py`, on Violins I, Violins II and Violoncellos, replace both shapes (the c30 C #2 first shape and c34 C #6's shape, lines 524-530 and 663-664) with one shape:

`[(179.5, 0.0), (180.5, 2.0), (183.1, 2.0), (184.25, 0.5), (187.75, 1.0), (190.0, 2.0), (193.0, 1.0), (196.0, 0.0)]`

On Violins I and II this adds to c30's second shape (190 -> 195: 0 -> 2 / 1.5), so the sum rises 2.0 -> 2.2 -> 2.3 over 190-195 with no dip. I simulated three other variants (a full release of the hold-back, a hold to 188, a hold to 190). Each made a 3-4 dB jump at 184 and a new 1-1.5 LU sag at 186-191 in the mp3. This shape was the only one that kept the master monotone.

**Simulated:**

| qn | 178 | 180 | 182 | 184 | 186 | 188 | 190 | 192 | 194 | 196 |
|---|---|---|---|---|---|---|---|---|---|---|
| master S | -27.5 | -26.9 | -27.2 | -24.9 | -24.6 | -24.5 | -23.7 | -22.9 | -21.6 | -20.7 |
| mp3 S | -19.9 | -19.7 | -20.5 | -18.7 | -18.8 | -19.1 | -18.7 | -18.2 | -17.2 | -16.6 |

- The mf now arrives about +2 LU in both the master and the mp3, and the line keeps rising to the f.
- Bar 60 onward is unchanged within 0.1 LU.
- Delivered LRA stays 15.2, span 18.6, limiter 1.8 dB.
- A 0.8 LU dip at 180-182 remains inside the 180-184 hairpin. It is sample unevenness (celli C2 at 182 -40 dB), not the envelope.

### 3. The violas' decrescendo into bar 65 ends 5-6 dB louder than it started: the pp arrival is a jump up (measured; fix simulated)

**Where.** Violas, qn 218-221. The score marks p at 216, a decrescendo 218-220, then pp at 220 (G3, the chord under the coming niente).

**What is wrong (measured).**
- The decrescendo's hpgain takes the envelope to -2.5 dB at 220. Then the violas' own pp soft trim (`mix.json` Violas `soft_trim_db.pp` 5, against p 3.5) brings it to +3.5 by 220.5: +6 dB in half a beat.
- The stem reads -50.8..-51.1 at 218.75-219.25, then -45.8, -45.6 and -44.7 at 219.75-220.25. The 220 note's legato lead starts it at 219.85.
- The violas are the loudest stem in the first beat of the pp bar, ahead of Violins II (-47.0), which carry the niente line.
- The listener hears the decrescendo turn round into a small accent on the pp, in a bar with nothing but strings (master -42 dB).

**Fix.** In `build/score_config.py`, `LEVEL_SHAPES["Violas"]` += `[(219.5, 0.0), (219.85, -5.0), (225.9, -5.0), (226.1, 0.0)]`. This keeps the pp trim elsewhere.
- The cut ends after the niente; c30's niente CC7 lane runs on top of it and still ends in silence.
- -4 dB is enough if the actor prefers the violas level with Violins II.

**Simulated.** Violas 219.75-221 read -50.7, -50.6, -49.7, -52.5 and -52.9 (the decrescendo ended at -51). Master S at 220-221 moves from -39.5/-40.5 to -40.3/-41.8.

### 4. Bar 74: the violins' mp pickup at 249 plays under the p phrase before it, and the mp3 deepens the dip before the A' crescendo (measured; fix simulated, small)

**Where.** Violins I and II, qn 248.8-250. The score marks mp at 249 on the pickup into bar 75, then a crescendo 250-256.

**What is wrong (measured).**
- Violins I's vol_db at the pickup is -5.3..-3.4 dB. The p phrase before it was at -2..-3, the result of role `[237.5, 250, -2.5, 0.5]` plus the decrescendo release. The pickup notes read -46.5/-41.9/-45.8 dB, the same as or under the p phrase (-41..-45).
- Master S over 240-249: -31.6 -> -34.7 (-3.1). mp3: -20.6 -> -25.9 (-5.3). Bar 74 becomes the softest point of bars 71-78 in the delivered file: the lift drops 2.2 dB ahead of the crescendo.
- I tested shorter lift smoothing in the delivery: `DELIVER_LIFT_SMOOTH_S` 3 and 2. They moved this dip by only 0.4-0.7 LU and lowered the delivered LRA to 14.7 / 14.4. I do not recommend them.

**Fix.** In `build/roles.json`, Violins I and Violins II: `[237.5, 250, -2.5, 0.5]` -> `[237.5, 248.75, -2.5, 0.5]`. The celli keep 250, because their mp is at 250.

**Simulated.** The pickup comes up 1.1-1.8 dB in the master (249.0 -41.4 -> -39.9, 249.25 -38.7 -> -36.9), and mp3 S at 248-249 goes from -25.5/-25.9 to -25.3/-25.5. This is a small audible gain: the mp is played. The mp3 dip is mostly the delivery's look-ahead, and I found no delivery setting that removes it without losing range.

### 5. In the mp3, Trombone 1's last accent (218) is louder than the first (213), although the master has it 1.7 dB softer (measured; low priority)

**Where.** Trombone 1's quotation, qn 212.5-219.5. The score marks ff marcato, accents at 213 and 218, and a decrescendo to p from 218.

**What is wrong (measured).** Maximum momentary loudness, master / mp3:

| Passage | Master | mp3 |
|---|---|---|
| 212.5 | -13.8 | -11.8 |
| 213-214.5 | -17.0 | -14.6 |
| 214.5-216 | -19.3 | -15.9 |
| 216-217.9 | -20.0 | -15.4 |
| 218 | -18.7 | -13.9 |

- The delivery's gain under the line rises from +1.9 dB at 213 to +4.7 at 218.
- The cause is mostly the top ride (`TOP_ABOVE` -3, `TOP_RATIO` 2.5, 3 s smoothing), which still holds 213 down next to the climax. `MOM_CAP_ABOVE` 3 -> 1.5 changed nothing (-14.6 / -14.1).
- This is the passage of Dan's note 9 (BRIEF). c34 C #4 measured 0.3 LU here; it is 0.7 LU now.

**Fix (optional).** `LEVEL_SHAPES["Trombone 1"]` += `[(214.3, 0.0), (214.6, -2.0), (219.5, -2.0), (219.6, 0.0)]`.
- Simulated: mp3 218 -14.7 against 213 -14.6 (level), and 214.5-218 lower by 0.2-0.8 LU. The 218 accent still stands 0.9 LU over 216-217.9.
- The ride gives back most of a master cut here, so expect little. Leave it if the actor prefers not to touch the c32-c34 trombone shapes.

## Checked and fine (measured)

- **Delivered file.** -19.8 LUFS, LRA 15.2, span 18.5 dB, limiter 1.9 dB; all five largest pre-limiter peaks are in bars 61-63 (qn 204.4-212.2). The master LRA is 23.8 LU (Dvořák 9/i reference 21.8). The combined simulation of findings 1-3 delivers LRA 15.2, span 18.6, limiter 1.8, I -19.8.
- **Climax order.**

  | Measure | Bars 61-62 | Bars 79-80 |
  |---|---|---|
  | Master Smax | -10.6 / -10.7 | -15.7 / -16.2 |
  | mp3 Smax | -10.2 / -9.7 | -12.2 / -12.7 |
  | mp3 Mmax | -8.9 | -11.4 |

  The climax is 2-3 LU clear in the delivered file. Bar 60's crescendo rises from -19.1 to -11.7 S (master) into the ff, and the bar 63 sf falls 10 dB under the trombone as printed.
- **Bar 47 fp (qn 148, `FP_SPIKE` 0.2/0.4).**
  - Violas -51 -> -40.4 at 147.9-148.4 -> -48 by 148.75.
  - Basses -53 -> -38.6 -> -46.8.
  - Master +3.5 dB for about 0.5 qn, then p. It reads as a forte stroke, and the drop is in CC11 (S3).
- **Cadence and coda.**
  - Bars 79-82 decrescendo: master S -16.2 (262) -> -24.1 (270) -> -29.0 (271) -> -36.1 (273) -> -39.7 (274), smooth.
  - Morendo: master S 296-301 reads -39.1 -> -47.4. The final ppp chord holds at -49..-51 dB RMS for 5 s, fades with CC11 18 -> 8 over its last beat, and the hall tail falls about 25-30 dB/s after 304, not cut by the envelope.
  - The coda (bars 85-90, pp) reads -37..-40 S, level with the intro's pp and with Horn 1's p theme (bars 7-10, -37.6..-37.9). The 292-295 peak follows the printed clarinet < >.
- **Hairpins.** 178 hairpins of 1 qn or more on fully sounding notes. Crescendos median +5.0 dB, decrescendos -7.0. Apart from findings 2 and 3, the flat or reversed ones are short or edge cases: Horn 1 20-21 (1 qn), Flute 1 108-111 and cor anglais 124-128 (flat, 0.0/+0.2 dB; soft solo crescendos in dolce lines), and harp 250-256 (see Manual notes).
- **Loop pulsing (BRIEF item 8).** I checked every held note chain over 6 s on every stem (61 chains): 100-300 Hz band and log-centroid after a 2 s detrend, autocorrelation at 3.95 s and best period 3.3-4.6 s.
  - Coda and final chord: every string chain reads 0.02-0.32 at 3.95 s (Violins I 292 0.15, Violas div 286 0.09, Cb 292 0.19).
  - The opening Violins I hold reads 0.08 / 0.04.
  - Two chains show a stem cycle that is masked in the master:
    - the contrabassoon pedal at 87-98 (centroid 0.83 at 3.65 s; master 0.02);
    - the timpani ppp roll at 226-238 (6.2 dB folded swing at 3.85 s on the stem, 13 dB under the master in its band; master autocorrelation 0.02).
  - Short chains (6-7 s) give autocorrelations of 0.9 and above at 3.5-3.75 s from too little overlap; those values are not evidence.
- **Unprinted swells.** The 8-10 dB rises flagged in c34 (Violas 42, Violins II 108, Bassoon 2 140) are slow pp entries that reach their body after 1.5-2 qn, not swells after the body. Each sits under a solo that is crescendoing (Oboe 1 at 42) or 6-9 dB louder. Not ranked.

**Do not touch:** the c30 niente CC7 lanes; the c34/c35 bar 61-62 string holds and the bar 79-80 `_all` -1.5 (climax order); the bar 60 brass CC1 crescendos and timpani roll shapes; `FP_SPIKE` 0.2/0.4; the morendo `_all` rows 298.5-303.5 and the final-chord re-bows and fills; the delivery settings (RATIO 2.2, KNEE 6, LIFT_SMOOTH_S 5, MOM_CAP_ABOVE 3); the harp velocity map (no nail pick) and `env_sustain` 1.0; c37's Cb coda pedal shape.

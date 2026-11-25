# Cycle 34, critic C: dynamics over time (on the c33 render)

Scope: the loudness arc against the score (the bar 47 fp, the animando crescendo of bars 53-60, the Largamente climax of bars 61-64, the bar 66 niente, the ff cadence of bars 79-82, the coda and the bar 91 morendo), the loudness range of the master and the mp3 (BRIEF item 6), swells and loop pulsing on held notes (item 8), and decays.

Method. Levels are stereo-power RMS on the c33 stems and master. The stems sum to the master exactly (residual -207 dB). "Smax" is the maximum EBU short-term loudness (3 s window, centred) in a bar, and "Mmax" is the maximum momentary loudness (0.4 s window). For simulations I multiplied the c33 stems by the proposed dB shapes, summed them, and ran a scratch copy of `tools/deliver_master.py` that adds environment overrides for TOP_ABOVE, TOP_RATIO and MOM_CAP_ABOVE. With no changes it reproduces the delivered c33 mp3 (LRA 15.7, span 17.7, limiter 1.4, same Smax per bar).

## Manual notes (MANUAL-READING row 34, slot C: D2, pp. 101-102; plus MANUAL-GAPS.md)

| Manual (PDF page) | Where it applies here | Followed? |
|---|---|---|
| p.101: brass Sustain patches set the dynamic with the mod wheel (CC1); all 4 layers play at once and CC1 crossfades them, so a crescendo on a held note sounds real | Trombone 2, Bass trombone and Tuba pp < f in bar 60 (qn 200-204); Horns 1-2 a2 bars 79-82; Horn 1's solos | Yes, since c30 (`CC1_DYN_TRACKS`). Measured: CC1 30 -> 84 over 200-204, and the stems rise 21-23 dB (Trombone 2 -50.2 -> -28.6, Tuba -44.6 -> -28.3). The horns keep CC1 57-72 below f (c31, because of the legato transition table). That departs from the manual on purpose and should stay. |
| p.101: Sustain Accent: velocity sets the loudness of the accent, CC1 the sustain | Trombone 1's accents at 213 and 218 (bars 63-64) | No, on purpose (BRIEF item 9): Sus MAX with a volume swell and CC7/EQ on the heads (c33). Keep it. |
| p.101: Sustain Marcato: velocity sets a low-pass filter on the marcato attack (harder means brighter) | Trombone 1's "marcato" quotation from 212.5 | No: Sus MAX at v106-112 (`MANUAL-GAPS.md` #11). Leave it alone; the render's problem in bar 64 is the delivery lift (finding 4), not the attack. |
| p.101: Portato (full length, not tied); Legato Repetitions | brass tenutos in bars 61-62; repeated brass notes | Not used (`MANUAL-GAPS.md` #9, #2). This is not a dynamics question. |
| p.101: Sustains loop indefinitely | every held note, brass and winds included (BRIEF item 8) | The string holds pass (see "Checked and fine"). The bass clarinet's 12.7 s pedal does not (finding 3). |
| p.102: Shorts carry no release trail, so hold the last note for the room; staccato at top velocity overblows | none: v600 has no brass shorts | n/a |

## Findings, ranked by what a listener would hear

### 1. The Largamente ff of bar 61 is weaker than the last beat of bar 60, and in the mp3 the climax is barely louder than the ff cadence (measured; fix simulated)

**Where.** Violins I, Violins II and Violoncellos, qn 203.75-206 (the bar 61 downbeat). Master and mp3, bars 61-62 against bars 79-80.

**What is wrong.**
- **The strings drop at the ff downbeat.** On the stems the strings fall at the printed ff arrival while CC11 jumps from 113 to 119:

  | Stem | 203.5-204 | 204.5-205.5 |
  |---|---|---|
  | Violins I | -22.6 | -25..-28.6 |
  | Violins II | -22.5 | -26.7..-28.3 |
  | Violoncellos | -21.5 | -23.9..-28.8 |

- **Why.** Three volume-envelope releases land on qn 204 at once:
  - the role `[188, 204, 2]` ends;
  - the hpgain of 3 dB drops to half (`SOST_HOLD_SHARE` 0.5);
  - the c30 C #2 shape `(195, 2) ... (204, 2), (206, 0)` releases.

  Violins I's vol_db falls 5.6 -> 1.95 dB in 0.25 qn and reaches -2.5..-4 by 206. The celli fall 3.6 -> -2.4 dB by 204.5.
- **The master barely grows.** RMS reads -16.4 dB at 202.75-204, -15.6 at 204-206 and -15.5 at 206-208.
- **The mp3 flattens it further.** The top ride (`TOP_ABOVE -3`, `TOP_RATIO 2.5`) compresses the master's 2.3 LU gap between bars 61-62 and 79-80:

  | Measure | Climax (bars 61-62) | Cadence (bars 79-80) | Gap |
  |---|---|---|---|
  | Master Smax | -12.2 / -12.3 | -14.6 / -14.9 | 2.3 LU |
  | mp3 Smax | -11.1 / -10.5 | -11.5 / -11.8 | 0.4-1.0 LU |
  | mp3 Mmax | -9.7 | -10.3 | 0.6 LU |

  BRIEF item 6 asks for the climax to stay clearly the loudest. In the delivered file it does not.

**Fix.**
- **Strings over bar 61-62.** In `build/score_config.py`, add a hold over the Largamente that starts just after the downbeat and ends before the 212 sf:
  - `LEVEL_SHAPES["Violins I"]` and `["Violins II"]` += `[(204.0, 0.0), (204.2, 3.0), (211.6, 3.0), (211.9, 0.0)]`
  - `LEVEL_SHAPES["Violoncellos"]` += `[(204.0, 0.0), (204.2, 3.5), (211.6, 3.5), (211.9, 0.0)]`

  A cleaner alternative gives about the same result: end the two Violins roles `[188, 204, 2]` at 211.9 and hold c30's second C #2 shapes to 211.6 instead of releasing them at 204-206; then add the celli shape alone.
- **The cadence.** `LEVEL_SHAPES["_all"]` += `[(261.75, 0.0), (262.25, -1.5), (267.75, -1.5), (268.25, 0.0)]`. This is c30 C #3's cadence half at -1.5 instead of -0.8; it was deferred in c30, not rejected.
- `tools/deliver_master.py` stays unchanged.

**Simulated (stems and delivery):**

| Measure | Now | After |
|---|---|---|
| Master RMS 204-206 | -15.6 | -14.5 |
| Master RMS 202.75-204 | -16.4 | -16.4 (the ff now arrives) |
| Master Smax gap, climax over cadence | 2.3 LU | 4.7 LU |
| mp3 Smax gap | 1.0 LU | 2.3 LU |
| mp3 Mmax, 204 against 262 | -9.7 / -10.3 | -9.4 / -11.3 |
| Delivered LRA | 15.7 | 15.1 |
| Delivered span | 17.7 | 18.3 |
| Limiter | 1.4 dB | 2.2 dB |

Bars 52-60 and the soft passages are unchanged within 0.3 LU. For a 3.0 LU gap, also set `TOP_RATIO` 2.5 -> 1.6; the limiter then reaches 2.8 dB and the span 19.3 dB, at the top of the target. I do not recommend that.

### 2. Unprinted 7-8 dB swells inside soft held string notes; the worst one makes bar 65 swell into the niente (measured)

**Where.** Violins II, C sharp 4 "sul G", qn 220-223 (bar 65). The score has a decrescendo to pp at 220, a tied pp, and the niente from 223.

**What is wrong.**
- **The swell.** CC11 holds at 34 and vol_db holds at -3.5, yet the stem rises 8 dB inside the sample:

  | qn | 220 | 221 | 222 | 222.5 |
  |---|---|---|---|---|
  | Violins II | -47.9 | -43.0 | -40.9 | -39.7 |

  Violins II is the loudest stem in bars 65-66, so the master swells too (-42.1 at 220 -> -39.7 at 222). The listener hears a crescendo where the score has a decrescendo, just before the line is meant to die away.
- **The re-bow fill matches the swollen level.** The fill at 223 (`rebow_fills.json` "Violins II" "223", up to +9.4 dB) was fitted to the swollen pre-level, so the niente starts from it. The c30 niente CC7 ramp itself works: Violins II falls -44.3 at 223 -> -59.9 at 225.5 -> -70.9 at 226.
- **The same kind of swell elsewhere.** These are exposed in the texture:

  | Note | Swell | Where it peaks | Master |
  |---|---|---|---|
  | Violoncellos 286 (bar 87, coda, pp tutti under Clarinet 1's dolce motto) | +7.4 dB | -49.4 -> -42.0 at 287.5 | +4.4 dB; CC11 swells 34 -> 38 across a layer edge |
  | Violoncellos 64.84 (bar 22) | +10.5 dB | | |
  | Violins II 108 (bar 37, under Flute 1) | +8.4 dB | | |
  | Violas 42 (bar 15) | +9.2 dB | | |
  | Bassoon 2 140 (bar 45) | +7.6 dB | | |

  The last two sit 4-8 dB under the solo, so they matter less. c30 C #5 found the same notes; it was deferred, never applied.

**Fix.**
- **Bar 65.** `LEVEL_SHAPES["Violins II"]` += `[(220.75, 0.0), (221.0, -4.0), (221.75, -4.5), (222.0, -6.5), (222.5, -7.5), (222.85, -7.5), (222.95, 0.0)]`. Simulated on the stem: 221-223 holds at -47 to -48.6 dB, and the master over 221-223 drops from -41.0/-39.7 to -43.3/-43.7.
- **The re-bow fill.** Subtract 4 dB from the Violins II "223" fill points from -0.04 s to 1.48 s (floor 0), so the niente starts near -47 instead of -44. Then refit it with `tools/fit_rebows.py --stems` on the c34 render.
- **The rest.** `SWELL_CC_CAP` add `"Violins II": {"*": 0}, "Violas": {"*": 0}, "Violoncellos": {"*": 0}, "Violas div": {"*": 0}` (as for the bassoons): soft long notes then keep their CC11 off the layer edge, and the swell moves to SWELL_DB. Also `LEVEL_SHAPES_S["Violoncellos"]` += `(286.0, [(0.5, 0.0), (1.0, -3.0), (1.7, -6.0), (2.3, -5.0), (3.0, 0.0)])`.

Aim for at most 3 dB of rise inside any unmarked soft note. Re-measure on the render, because the CC11 cap changes the layer mix.

### 3. The bass clarinet's 12.7 s pp pedal (bars 3-6) cycles in tone colour (measured cycle; audibility inferred)

**Where.** Bass clarinet A flat 2, qn 6-17 (one tied note, `Sus Non Vib`). It is the loudest or second-loudest stem in bars 3-5 (metrics.md).

**What is wrong.**
- **The cycle.** The note was folded at its strongest period, after the level was detrended over 2 s:

  | Band | Period | Autocorrelation | Folded swing |
  |---|---|---|---|
  | 500-1000 Hz | 4.40 s | 0.94 | 6.4 dB |
  | 1-4 kHz | 4.25 s | 0.76 | 5.2 dB |
  | 200-500 Hz | 3.60 s | 0.72 | 5.1 dB |
  | 80-200 Hz | 3.50 s | 0.30 | 1.3 dB |

  The full-band spectral centroid autocorrelates at 0.86 at 3.70 s. So the level is steady and the colour cycles. This is the effect Dan heard on the final chord (BRIEF item 8).
- **Why earlier checks missed it.** c30 checked only 100-300 Hz and the centroid at exactly 3.95 s, which this woodwind loop does not use.
- **For comparison.** Horn 4 over the same bars reads at most 0.5, and every string hold reads 0.2 or less.

**Fix.**
- Split the note once near its middle with the re-bow mechanism: `REBOW_AT["Bass clarinet"] = [11.6]`. It works on any track (score_to_parts.py line 4728). Give it the track's own articulation: add a generic `REBOW_ART_BY = {"Bass clarinet": "Sus Non Vib"}` next to `REBOW_ART`.
- `REP_RETONGUE_AT["Bass clarinet"]` 9/12/15 is dead (c27) and can go.
- Fit the join with `fit_rebows.py` after the render. A breath re-attack at pp in a held pedal is idiomatic and needs no score mark.
- If the split is rejected, `fit_loops.py 33 build/parts.json "Bass clarinet:6.0:4.4"` flattens only the level part, not the colour.
- **Check on the render:** 500-1000 Hz autocorrelation at 3.5-4.5 s under 0.4.

### 4. The delivery lift makes Trombone 1's last accent (218, bar 64) louder than the start of the quotation (measured; fix simulated)

**Where.** mp3, qn 213-219.

**What is wrong.**
- **The master.** The quotation falls slightly: Mmax -17.1 at 213, -18.7 at 218.
- **The mp3.** The lift looks ahead into the pp of bar 65 and raises the gain under the trombone from +3.1 dB at 213 to +7.2 dB at 218. The 218 accent (printed ">" with a decrescendo to p) then reads -11.5 Mmax against -14.2 at 213, and is the loudest moment of the mp3 outside bars 60-63.

This is the passage of Dan's "accents are too harsh" note (BRIEF item 9).

**Fix.** In `tools/deliver_master.py`, set `MOM_CAP_ABOVE` 6.0 -> 3.0. Simulated on the c33 master:
- 218: -11.5 -> -13.9 Mmax (0.3 LU over 213).
- 215-217 fall 0.4-1.2 dB.
- Nothing else in the file moves by more than 1 dB of momentary loudness. LRA, span and limiter are unchanged (15.7, 17.7, 1.4).
- 4.0 gives -13.1 at 218 if 3.0 seems too strict.

### 5. The bar 47 fp is a short blip (measured level; perception inferred)

**Where.** qn 148, Violins II, violas and basses under Oboe 1's mf line (`FP_SPIKE = ("f", 0.12, 0.25)`, the generic default).

**What is wrong.**
- The spike peaks for about 0.25 qn (0.27 s at the poco rit.):
  - Violins II: -47.1 at 148.0, -41.9 at 148.25, -47.5 at 148.5.
  - Basses: +12 dB for one 0.06 qn frame.
- The master rises 3.6 dB (-35.2 -> -31.6) for about 0.2 s and is back by 148.4.
- A string fp is a full bow stroke of f followed by p. At this length it reads as a click in the accompaniment, not a forte attack. The drop is in CC11, so S3 is met.

**Fix.** In `build/score_config.py`, set `FP_SPIKE = ("f", 0.2, 0.4)`; this is the only fp in v600. **Inferred:** about +2 dB more energy on the violins. Check on the render that the master peak stays under 3 dB over Oboe 1 at 148-148.5.

### 6. The strings dip at the start of the bar 55 crescendo, and the mp3 flattens bars 54-56 (measured)

**Where.** Violins I, Violins II and Violoncellos, qn 178-183. The score has mp at 178, a crescendo 180-184, and mf at 184.

**What is wrong.**
- **The dip.** The soft hairpin gain of the 172-178 crescendo (hpgain `[172, 178, 2.5]`) is released over 178-181, just as the next crescendo starts. The c22 bridge rule (`HP_MF_BRIDGE_REL`) holds only mf/f arrival gains, so this gain is not held. In 179-182 the vol_db falls from 3.25 to 0.62 dB while CC11 rises only 61 -> 65, and the stems fall at the start of the printed crescendo:

  | Stem | Before | 181-182 |
  |---|---|---|
  | Violins II | -35.1 at 179 | -41.3 |
  | Violins I | -36.6 at 178 | -39.6 |
  | Violoncellos | -35.9 at 180 | -41.2 at 182 |

- **In the mp3.** Bars 54-56 read -19.3, -19.6 and -19.9 Smax: a falling line inside "poco a poco animando ... cresc." The lift falls about 0.9 dB per bar, and the master grows only 0.9 LU over the same span.

**Fix.**
- **Generic.** Apply the c22 bridge to the soft hairpin gains (`HP_GAIN_SOFT_DB`, `HP_GAIN_SOFT_ACC_DB`) as well: when another crescendo starts within `HP_CHAIN` with no softer mark or decrescendo between, hold the gain to its start and release it over `HP_MF_BRIDGE_REL`.
- **Per-onset equivalent.** `LEVEL_SHAPES` += `[(179.5, 0.0), (180.5, 2.5), (183.1, 2.5), (184.1, 0.0)]` on the three tracks. It ends where c30's mf hold-back starts.

**Simulated.** Master bar 54-55 Smax -27.4/-27.1 -> -26.7/-26.4. mp3 bars 54-56 -19.3/-19.6/-19.9 -> -19.0/-18.9/-19.8. Bar 56 stays low because c30's mf hold-back is deliberate.

## Checked and fine (measured)

- **Delivered file.** -19.7 LUFS, LRA 15.7, span 17.7 dB, limiter 1.4 dB. Bar 1 -25.8, coda bar 83 -29.2 and final chord -33.1 Smax: soft passages stay audible, and the final chord is 7.3 LU under bar 1. The master LRA of 24.3 LU is near the Dvořák 9/i reference (21.8 LU, LEARNINGS).
- **The arc.**
  - The master rises 19.6 LU from bar 52 to the climax and 16.9 LU over bars 71-79.
  - Hairpins of 1 qn or more: 115 crescendos with a median rise of +5.7 dB and 113 decrescendos with a median fall of -7.1 dB. Apart from findings 1 and 6, the outliers are edge effects of harp arpeggios and entries.
  - The brass crescendos of bar 60 rise 21-23 dB on CC1.
  - The timpani: the pp < roll rises -38.7 -> -22.4 into the f stroke at 203. The ff roll settles from -31 to -37.5 within a beat, under the texture. The pp < at 261 leads into f at 262 and settles at -35.
- **The bar 66 niente.** It fades 15-25 dB through the hairpin on Violins II, violas and celli (c30's CC7 lanes); only its starting level is wrong (finding 2).
- **The morendo and coda.** Master Smax bars 89-92 read -36.8, -37.4, -41.1 and -47.0. The 82 -> 83 decrescendo into the coda is smooth.
- **Loop pulsing on string holds.** I measured 100-300 Hz band and centroid autocorrelation at 3.95 s after a 2 s detrend. The opening Violins I hold, Cb 221-238 and 274-304, Violoncellos div 274-286, celli, Violins II and Violas div in the coda, Horn 3 286-297, Horn 4 3-18 and the master 274-301 all read between -0.19 and +0.20.

**Do not touch:**
- the c30 niente CC7 lanes;
- the horn CC1 split (57-72 below f) and the brass CC1 dynamics;
- Trombone 1's Sus MAX accents and its 213/215 CC7 and shelf;
- the string re-bows and fills in the coda and final chord;
- the delivery's RATIO/KNEE (2.2 / 6) and smoothing;
- the timpani roll shapes in bars 2-3, 52 and 60;
- c30's bar 56 mf hold-back.

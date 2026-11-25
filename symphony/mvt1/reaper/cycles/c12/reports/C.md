# Cycle 12, critic C: holistic comparison (render c11)

## Scope and method

I reviewed the stem-fixed c11 render (`cycles/c11/render/`, `metrics/`, `mvt1-mockup-c11.mp3`, built from `cycles/c11/rendered_build/parts.json`) against:
- cycle 0 (`cycles/c00`, on the c01/before map with the 1/6 qn shift, as `rendermap.py` does);
- cycle 6, five cycles back (`cycles/c06`, on `cycles/c07/before/parts.json`);
- the Dvořák 9/i Columbia recording (`symphony/render/assets/refs/dvorak9_i_columbia.mp3`, the only reference audio on disk) and the loudness series of Brahms 1/i, 4/i, 1/ii, 4/ii in `symphony/render/critics/c00`, `c04`.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c12-C/`. The c08-C battery (`dist2.py`, `sect.py`, `dynbar.py`, `tempo.py`, `sync.py`, `hpall.py`, `ptop.py`, `tutticresc.py`, `loop.py`, `acc.py`, `metric.py`) was rerun on cycles 0/6/11. New scripts: `pslope.py` (lead-line level against pitch), `hp2nd.py` and `notelv.py` (second-theme hairpins, per-note levels), `contour.py` (half-beat level with the printed marks), `seg.py` (per-stem change over a span), `bloom2.py` (held notes rising against CC11), `attk.py` (2-5 kHz at strong onsets), `tilt.py` (band shares by loudness, against Dvořák), `lowmid.py`, and `simtop.py` / `simmeas.py` (stem simulation of dynamic trims through `tools/deliver_master.py`). Levels are stereo power. Score qn is converted to file time with each render's tempo map.

## c00 -> c06 -> c11 in brief (measured)

What improved:
- **Tempo.** Beats exactly on a printed mark went 88% -> 72% -> 52%. The longest run at one tempo went from 208 beats to 208 and then to 23 beats. Every section now moves inside its phrases.
- **Ensemble.** At tutti entries, the median spread of entry times between sections (p10-p90) went 0.145 -> 0.141 -> 0.122 s.
- **Tone colour at loud dynamics.** In the loudest 6 dB of the master (3 s windows), the 2-6 kHz share is c00 -12.6, c11 -10.4 dB against Dvořák -10.4, and the 6 kHz+ share is -33.8 -> -29.3 against -28.8. The c09 CC1 brass layers did this: loud passages now brighten the way a real orchestra does.
- **Dynamics against the score.** Bar level against the bar's loudest printed dynamic: correlation 0.804 -> 0.814 -> 0.823. Held-note crescendos go the right way in 82/92 -> 79/92 -> 84/94; moving decrescendos in 67/84 -> 71/84 -> 76/86.
- **Delivered mp3.** LRA 17.3 -> 15.2 -> 14.2 LU; span from p10 to max 21.7 -> 20.0 -> 18.1 dB; p75->max 9.6 -> 10.6 -> 9.1 dB. The Brahms/Dvořák recordings measure 4.8-7.6.
- **Dan's item 7 (loop pulsing).** On every held passage the master's 100-300 Hz band and its centroid have an autocorrelation of 0.22 or less at the 3.95 s loop period. The largest values: intro roll, band +0.18 and centroid +0.15; bars 1-14, band +0.22 at 4.6 s; control (Allegro) -0.04. Nothing pulses.
- **Dan's item 8 (accents).** On the master, the 35 brass accents measure 2-5 kHz over the first 80 ms minus the body at a median -9.2 dB (worst -4.3, at qn 536). None is harsh.

What has not moved or got worse is listed below, with the passages that are now the weakest.

## 1. The second theme's opening phrase (bars 47-50 and 147-150, Horn 1 and celli, dolce) has lost its swells. The c10/c11 hole fills levelled every note, and the fill at the crest makes the end of the printed decrescendo the loudest note (measured)

**Where.** Horn 1 and Violoncellos at qn 184-199 and 584-599. This is the movement's lyrical centre: a dolce theme with a < > on almost every half bar. The c10 and c11 work there aimed at legato holes. As a result, the head of the theme is now the most mechanical-sounding passage in the movement.

**Measured: per-note levels** (`notelv.py`; dB at 0.05-0.25 s after the start of each note / over its last 0.25 s):

| | Hn1 184 C (< to 187.5) | 187.5 B♭ (>) | 188 A♭ (end of >) | 189 F ten. |
|---|---|---|---|---|
| c00 | -42.5 / -38.1 | -40.2 | -44.5 | -37.2 |
| c06 | -42.1 / -37.6 | -39.7 | -45.8 (hole) | -43.8 (hole) |
| c11 | -36.6 / -36.5 | -37.3 | -37.7 | -36.6 |

- In c11 the five notes of bars 47-48 all lie within 4.6 dB. The long C, which carries the printed crescendo, changes by 0.0 dB from start to end; c06 rose 4.5 dB.
- The second statement behaves the same way:
  - Hn1 584 rises +3.1 dB;
  - the 588 quarter is level with the eighth before it;
  - the celli's 588 quarter starts at -29.9 dB, 4.2 dB *over* the 587.5 eighth and the loudest note of the phrase, although it is the end of a decrescendo.

**Measured: hairpins** (`hp2nd.py`; last third minus first third of each hairpin):
- Horn 1, Violoncellos and Violas in 184-220 and 584-620: right way by 1 dB or more in 26 / 25 / 22 of 39 hairpins (c00 / c06 / c11).
- Reversals that are new since c06 (c06 -> c11):
  - Horn 1 184-187.5 < +3.3 -> -0.1;
  - Horn 1 187.5-188 > -4.0 -> +2.1;
  - Horn 1 584-587.5 < +3.1 -> +0.1;
  - Horn 1 587.5-588 > -3.9 -> +2.0;
  - Horn 1 196-198 > -2.1 -> +1.1.
- Wrong in all three cycles:
  - Horn 1 596-598 > +4.2. The C5 at 596 grows -36.9 -> -32.8 inside its printed decrescendo, and the 598 B4 starts at -32.2, the loudest note of bar 150.
  - Violoncellos 196-198 > +0.1.
  - Violoncellos 589-591 < -1.3.

**Measured: phrase tops** (`pslope.py`; each lead-span note against the mean of the notes within ±4 qn):
- Notes 4 or more semitones above the local mean are louder by: Violins I +3.0 dB (n13), Horn 1 +1.7, Violoncellos -0.4 (n14; c00 -1.4, c06 -0.1).
- In the celli, the PT_* contour does nothing here. The theme has a hairpin on nearly every note, and `PT_OFF_IN_CRESC` and the hp-soft spans zero the contour inside them. The hairpins alone have to make the shape.

**Cause (measured in parts.json and build/).**
- **Horn 1 184 / 584.** The volume envelope starts at +4.9 dB: role +2.5 plus the c10 auto fill of 2.4 dB ("dip 5.4 dB at +0.04 s"). It sags to +2.7 at 184.65 and returns only to +3.5 at 187.5. The crescendo is therefore in CC11 alone (61 -> 81), and CC11 hardly changes the level on this note.
- **The quarter fills at 188/588** (`early_fills.json`): Horn 1 188 and 588 +6.5 dB, hold 0.55 s; Violoncellos 588 +5.0, 188 +2.5. They fill the c06 hole and also cancel the decrescendo.
- **Horn 1 598 and 198** are auto fills of +5.5 and +2.7 dB. They sit on the note that ends the bar-50/150 decrescendo.
- **Horn 1 596.** The sample swells about 4 dB on its own, while vol_db falls only -0.4 -> -2.3 dB.

**As heard (inferred).** The dolce theme comes out as evenly placed long notes. The "breathing" written on every half bar is absent at the start of both statements. That is the first thing a conductor would correct in this section.

**Fix** (`build/score_config.py`, c12 block; `build/early_fills.json`):

1. **Swell the long first note in the volume envelope** (CC11 alone does not do it):
   ```
   for o_ in (0, 400):
       LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(184.25 + o_, 0.0), (187.4 + o_, 3.5), (187.6 + o_, 3.5), (187.85 + o_, 0.0)]]
       LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(184.25 + o_, 0.0), (187.4 + o_, 3.0), (187.6 + o_, 3.0), (187.85 + o_, 0.0)]]
   ```
2. **Make the quarters at the end of the decrescendo land under the eighth instead of over it:**
   - in `early_fills.json`: Horn 1 "188" and "588" db 6.5 -> 3.0; Violoncellos "588" 5.0 -> 1.0, "188" 2.5 -> 1.0;
   - auto fills: Horn 1 "598" 5.5 -> 2.0, "198" 2.7 -> 1.0.
3. **Generic guard, so the next auto_fills pass does not restore these.** In `tools/auto_fills.py`, a fill on a note whose onset lies inside or at the end of a printed decrescendo of its own track may bring the note at most to 1.5 dB under the note before it (measured on the stem: body of the previous note minus body of this note, minus 1.5, floored at 0).
4. **Horn 1 crest at 596 / 196:**
   ```
   LEVEL_SHAPES["Horn 1"] += [[(596.1, 0.0), (597.9, -4.0), (598.05, 0.0)], [(196.1, 0.0), (197.9, -2.5), (198.05, 0.0)]]
   ```

**Pass criteria** (`hp2nd.py`, `notelv.py`):
- Horn 1 184 and 584: end minus start +3 dB or more.
- The 188/588 quarters 2-4 dB under the eighth before them, in Horn 1 and celli.
- No new hole: the 189/589 tenuto starts no more than 4 dB under the 188/588 quarter (the c10 problem).
- Horn 1 596-598 > at -1 dB or lower.
- 30 or more of the 39 hairpins the right way.
- Refit the Horn 1 accents if any sit in 184-206 or 584-606 (`fit_accents.py --family brass`).

## 2. Attacks have become duller than a real orchestra's, and duller with every cycle. Accents now start darker than the sound before them (measured; the audible effect is inferred)

**Where.** All loud entries and accents; most audible on the brass accents of the Allegro (bars 27-32, 69-72, 131-142, 167-170) and on the tutti chord changes.

**Measured** (`attk.py`): strong onsets, meaning jumps of at least 6 dB within 20 dB of the 99.5th percentile. For each: 2-5 kHz in the first 80 ms minus 2-5 kHz in the body (0.15-0.40 s), and that difference minus the same difference at 100-1000 Hz ("tilt").

| | n | 2-5 kHz front minus body, median (p25..p75) | tilt |
|---|---|---|---|
| Dvořák 9/i | 269 | -4.2 (-6.7..-1.4) | -1.1 |
| c00 | 54 | -5.0 (-6.7..-3.5) | -1.9 |
| c06 | 44 | -5.6 (-7.4..-3.1) | -2.2 |
| c11 | 43 | -6.2 (-7.5..-4.0) | -2.6 |

The brass accents on the master (`acc.py`, 35 accents):

| | front minus body | front minus the 0.25 s before |
|---|---|---|
| c00 | -6.2 | -3.7 |
| c06 | -8.0 | -4.3 |
| c11 | -9.2 | -4.8 |

So the first 80 ms of a c11 brass accent has 4.8 dB less 2-5 kHz energy than the sound just before it.

Dan's harsh case (movement II c24) was the opposite: +7 to +13 dB over the body. The brief's target is "weight, not bite". The render is now 2 dB under a real orchestra's typical front and still moving away from it.

**Cause (measured in config).**
- `GENTLE_ACCENT` brass: plain Sus, the swell full only at +0.07 s.
- c06 cut the swell 4.0 -> 2.5 dB.
- `accent_fits.json` adds level but not brightness.
- With CC1 now selecting the brass dynamic layers (c09), every accent sits on its printed dynamic's layer. The front of the note is the slow Sus attack of that layer.

**As heard (inferred).** Accents read as small swells rather than stresses, and ff chord changes have soft edges. The rhythm of the Allegro loses definition. Because this is a matter of brightness, the level measurements, which all pass, do not show it.

**Fix** (a bounded test, `tools/score_to_parts.py` GENTLE_ACCENT brass branch; `build/score_config.py`):
- A short CC1 lift on brass accents at f and louder: +8 CC1 (about a third of the f -> ff layer distance in `CC1_DYN_MAP`, 86 -> 108) from the moved onset to +0.10 s, ramped back over 0.10 s. No accent sample, no CC11 bump, no velocity: those were the harsh parts.
- Bring the volume swell forward: `swell_s` (0.07, 0.25, 0.6) -> (0.04, 0.25, 0.6).
- New keys: `GENTLE_ACCENT["brass"]["cc1_front"] = (8, 0.10, 0.10)` and `swell_s=(0.04, 0.25, 0.6)`.
- Refit the brass accents afterwards (`fit_accents.py --family brass --keep-long-qn 1.4`), because the CC1 lift adds level.

**Pass criteria:**
- Master brass accents, 2-5 kHz front minus body: median -5..-3 dB.
- No accent over 0 dB. That is still 7 dB under Dan's harsh case.
- Front minus the 0.25 s before: median 0 dB or more.
- Strong-onset median (`attk.py`) -5 dB or higher.
- Accents still 2-4 dB over their neighbours in level.
- If any accent passes 0 dB, take the CC1 lift on that track to +5.
- This change needs Dan's ears. Flag it in CHANGES.md as the one to listen to (bars 131-142).

## 3. The tutti decrescendo after the transition's sf (bars 41-42, qn 164-168) has stayed flat in every cycle. Horn 1 grows under the printed > and covers it (measured)

**Where.** Bar 41, sf tutti > to the mf of bar 42 > to p at bar 43. Horn 1 has the melodic line (E♭3 -> C4 -> B♭3, ff, > from 165).

**Measured** (`tutticresc.py`, `seg.py`, `contour.py`):
- Shared decrescendos 164-168 (6 tracks) and 166-168 (7 tracks), master change: -1.4 / -0.6 (c00), -1.0 / -0.5 (c06), -1.0 / +0.2 dB (c11). These are two of the six tutti hairpins in the movement that are still under 2 dB the right way. The other 24 measure 2-12 dB.
- c11 stems, 164.1-165.0 against 167.0-167.9:
  - master -26.0 -> -27.0;
  - **Horn 1 -30.3 -> -28.1 (+2.2)**, the loudest stem by 6 dB;
  - Oboe 2 +2.6, Clarinet 2 +1.9;
  - Violins II -8.7, celli -6.7, violas -5.5, basses -5.4. The strings do their decrescendo; the winds and Horn 1 do not.
- Horn 1's vol_db steps 6.0 -> 13.2 dB at 165.02 (the auto fill of 2.4 at 165 on top of the leg-target shaping) and is still +6.1 at 166.25. CC11 goes 113 -> 101.
- Inside the sf > of 160-164, Flute 2's held G5 rises from -45.6 (161.5) to -35.7 dB (163.5) while CC11 falls 97 -> 74 and CC1 falls 87 -> 79. The cause is a sample bloom or the CC1 crossfade (inferred). Oboe 1 is flat (-34.2 -> -35.6) under the same >.

**As heard (inferred).** After the transition's climax the music should die away into the quiet of bars 43-46. Instead the horn holds its ff and the upper winds swell, so the p at bar 43 arrives as a step.

**Fix** (`build/score_config.py`):
```
LEVEL_SHAPES["Horn 1"] += [[(165.3, 0.0), (167.9, -6.0), (168.05, 0.0)]]
LEVEL_SHAPES["Flute 2"] = LEVEL_SHAPES.get("Flute 2", []) + [[(161.6, 0.0), (162.6, -6.0), (163.9, -8.0), (164.05, 0.0)]]
for tn_ in ("Oboe 1", "Oboe 2", "Clarinet 2"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(164.2, 0.0), (167.9, -4.0), (168.05, 0.0)]]
LEVEL_SHAPES["Oboe 1"] += [[(160.6, 0.0), (163.9, -3.0), (164.05, 0.0)]]
```
Also delete the Horn 1 "165" early fill (2.4 dB), or apply finding 1's decrescendo guard to it.

**Pass criteria:**
- Master 167.0-167.9 at least 3 dB under 164.1-165.0.
- Horn 1 -4 dB or more across the same windows.
- Flute 2 at no point inside 160-164 over its level at 160.5.
- The p of bar 43 (qn 168-172) no more than 6 dB under 167-168 on the master, so the line reads as a decrescendo rather than a cut.

## 4. Loud tutti lacks low-mid body: 100-250 Hz is 1.9 dB under Dvořák in the loudest frames, and the trombones and horns contribute little of it (measured; the fix is inferred)

**Measured** (`tilt.py`, `lowmid.py`; 3 s windows by level below the 99th percentile):
- 100-250 Hz share in the loudest 0-6 dB: c00 -10.7, c06 -10.1, c11 -9.2 dB, against Dvořák -7.3.
- At 6-12 dB below the loudest: c11 -9.3 against -7.6.
- In soft passages the mockup has more 100-250 Hz than Dvořák (-8.1..-8.4 against -11.6..-12.8). The deficit is only at the loud end.
- Whole-movement shares (`metrics.md`): -9.13 dB against Dvořák -6.61, Brahms 1/ii -8.75, Brahms 4/ii -7.55.
- In the loud tutti spans (qn 100-128, 520-568, 628-648, 664-680), the master's 100-250 Hz band comes from: celli -5.9 dB, timpani -6.6, basses -7.3, tuba -8.6. Trombone 2 gives -16.2, bass trombone -17.0, Trombone 1 -21.8, Horn 4 -22.4, violas -15.5.
- The bass trombone's own 100-250 Hz share is -14.4 dB, which is low for an instrument whose ff fundamentals lie at 60-250 Hz.
- The celli and basses already carry +6 / +4 dB loud_eq at 150/160 Hz. More there would make them boomy.

**As heard (inferred).** The fortissimo tutti is bright and loud but thin in the middle. The weight a real orchestra gets from trombones, low horns and violas at 150-300 Hz is missing.

**Fix** (`build/mix.json`, a test): add a `loud_eq` bell of +2.5 dB at 220 Hz, bw 1.0 oct, with the existing loud_eq `points` list, on Trombone 1, Trombone 2, Horn 3, Horn 4 and Violas. For Bass trombone, use +2 dB at 160 Hz and remove its `side_shelf` lowshelf -2 dB at 200 Hz in the loud spans only. Leave celli, basses, tuba and timpani alone.

**Pass criteria:**
- Loudest-6-dB 100-250 Hz share -8.3 dB or higher.
- 250-500 Hz share up by no more than 1.5 dB.
- 2-6 kHz share within 0.5 dB of now (the c09 brightness must stay).
- Delivered limiter no higher than 2 dB.

## 5. The ff tutti sit 5-9 dB under the bar-160 fff against 1.5-4 dB in c00, but a uniform ff lift costs the climax order. Do not apply one (measured and simulated; a constraint for the actor)

**Measured** (`ffrel.py`; master without percussion, relative to bars 160-161):

| | 27-32 | 82-83 | 97-102 | 116-121 | 131-134 | 140-142 | 167-170 | 122-123 |
|---|---|---|---|---|---|---|---|---|
| c00 | -3.8 | -1.6 | -5.7 | -2.0 | -4.2 | -3.0 | -2.8 | +1.6 |
| c11 | -7.1 | -5.1 | -9.3 | -6.2 | -7.6 | -5.2 | -6.9 | -1.1 |

- Per-track medians: ff -> fff +2.3 dB in c00, +5.2 dB in c11. The c02-c09 climax work (fff hold, fff anchors, roles) built this gap.
- Master p75->max is 13.0 dB against 4.8-7.6 in the recordings. The whole top of the range rests on the two climaxes.

**Simulated** (`simtop.py`: stems re-gained by each track's printed CC curve, then `deliver_master.py`):

| | delivered LRA | span | p75->max | 122 | 169 (coda 167-170) | 160 |
|---|---|---|---|---|---|---|
| now | 14.2 | 18.1 | 9.1 | +9.0 | +7.1 | +9.4 |
| ff +2 dB | 15.2 | 17.9 | 8.4 | +8.0 | +7.6 | +8.6 |
| ff +3 dB | 15.8 | 18.2 | 8.3 | +7.4 | +7.8 (order lost) | +8.3 |

The ff passages gain only 0.5-0.8 LU in the delivered file, because the delivery normalisation and top ride take most of the lift back. Meanwhile the 122-over-coda margin falls from 1.9 to 0.4 LU, and the order is lost at ff +3 dB.

**Recommendation.** Keep the ff/fff trims as they are. Any later level lift for the ff tutti must exclude qn 664-680 (the coda, printed f/ff) and must be checked against 122 > 169 on the delivered file.

## Do not touch

- The c11 tempo arcs and `_REBOW_FROZEN`. The tempo is now the strongest gain since c00.
- `ABUT_LEAD` and the entry leads: tutti entry spread 0.122 s.
- The CC1 brass layers with the c09 trims: the loud-end brightness now matches Dvořák.
- `GENTLE_ACCENT` without accent samples or CC11 bumps. Finding 2 adds only a CC1 front; the rest stays.
- The re-bow rows and fitted shapes, and the re-strike plans: no loop pulsing on any held passage.
- The delivery settings (top ride 1.6, `FAST_CAP_ABOVE` 4) and the climax order 160 > 122 > 169.
- `CAESURA` 636 and `BEAT_STRETCH` 679; the pre-roll meter fix; `TIMP_DELAY_S` and the suspended-cymbal timing.

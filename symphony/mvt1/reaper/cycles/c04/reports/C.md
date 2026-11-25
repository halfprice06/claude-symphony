# Cycle 4, critic C: holistic comparison (render c03)

## Scope and method

I reviewed the c03 render (stem-fixed `render/`, `metrics/`, `mvt1-mockup-c03.mp3`) against two baselines:
- cycle 0 (`cycles/c00`, read on its own 1/6 qn-shifted map from `render_shift.json`);
- real recordings: the Musopen Brahms 1/i, 4/i, 1/ii and 4/ii loudness series and metrics in `symphony/render/critics/c00` and `c04`, and the Dvořák 9/i band levels.

There is no render five cycles back.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c04-C/`:
- `lib.py`, `dynbar.py`, `stl2.py`, `dist.py`, `top5.py`: macro dynamics;
- `ptop.py`, `hp.py`: melodic shape;
- `loop.py`, `loop2.py`, `timp.py`: loop pulse;
- `acc.py`: accent attacks;
- `sync.py`: tutti onsets;
- `b41.py`, `beats.py`: per-beat levels.

## c00 to c03 in brief (measured)

What improved:
- Soft passages are 3-4 dB louder in the master: bars 177-182 +3.3 to +4.3 dB.
- The subito marks now read as subito: bar 84 -10.5 dB.
- The fff at bar 160 is now the loudest moment: delivered short-term max -9.7 LUFS, against -10.8 at bar 122 and -11.8 at bar 170.
- The timing axis is correct.

Movement and loop pulse:
- Loudness motion on the delivered mp3 went from 9.55 / 5.00 to 8.78 / 4.76 dB (dS4 p90 / 1s-20s).
- That is still above every reference: Brahms 1/i 7.89 / 4.53, 4/i 5.91 / 3.12, 1/ii 8.55 / 4.56, 4/ii 6.29 / 3.92. The fall is not a loss of movement.

Dan's two checks on the master:
- **Loop pulse (item 7).** The 100-300 Hz band and centroid autocorrelation at 3.95 s stays under 0.25 on every held passage: the second-theme pedal, development 471-512, the coda solo and the final chord 712-728 (-0.14 / +0.05). The one exception is the opening roll (finding 4).
- **Accent attacks (item 8).** On the master, the 2-5 kHz energy in the first 80 ms of the 35 brass accents measures a median -8.2 dB under the note body (worst -0.2 dB, qn 536). It also sits -4.7 dB under the 0.25 s before. No accent is harsh.

Where the render still sounds like a machine is phrasing: melodic shape, tempo, and how the middle dynamics sit against the peaks. Movement II built tools for all three, and every one is switched off in movement I's config.

## 1. Melodies are played flat or inverted: the top note of a phrase is softer than the rest, and half the soft crescendos in the solo lines do not grow (all lead lines)

**What is wrong.** `LEAD_SPANS` is `{}` in `score_to_parts.py` and is not set in `build/score_config.py`. It switches on movement II's lead-line shaping:
- the phrase tops (c18, `PT_DB_PER_ST` 0.3, clip -1.5..+2 dB);
- the soft-hairpin dB ramps on lead lines (`HP_GAIN_SOFT_DB` +3, `HP_SOFT_DEC_DB` -2, c14).

None of this is active in movement I. CC11 alone moves a p line only 0.11-0.19 dB per CC (kit LEARNINGS 4).

**Evidence: phrase tops (measured, `ptop.py`).** I took 18 lead slurs of 4 or more notes: Violins I themes 56-104 and 520-576, Horn 1 and celli 184-220, Violins I 220-244, celli 680-696, Clarinet 1 504-520, Oboe 1 and Flute 1 128-184. For each note I measured the stem body (onset +0.06 s to +0.6 s).
- The highest note is the loudest in only 3 of the 18.
- The highest note minus the rest is a median -0.75 dB.
- Level against pitch has a median slope of -0.12 dB per semitone. Upper samples at a constant CC11 are softer, so every climb sags.
- Examples:
  - Violins I at 84: top note -2.4 dB, r = -0.96.
  - Violins I at 554.5: top note -2.8 dB.
  - Oboe 1 at 176: top note -6.7 dB.

**Evidence: soft hairpins (measured, `hp.py`).** These are the hairpins of the solo lines in bars 5-10, 47-61, 127-129, 147-155 and 171-174. The rise is the last third of the hairpin minus the first third.
- 11 of 23 crescendos rise 1 dB or less:
  - Horn 1 184, 201, 589;
  - celli 184, 201, 504, 584, 589;
  - Clarinet 1 236, 504;
  - Violins I 228.
- 2 of 18 decrescendos rise: Horn 1 596 (+2.5 dB) and celli 196 (+3.2 dB).
- Movement II measured the same fault before c14: 7 of 20 crescendos flat or falling.

**As heard (inferred).** Phrases do not breathe. The theme's high points come out as small dips, and the dolce horn/cello theme and the cello solo sound evenly bowed and blown. This is one of the clearest marks of a sequenced rendering.

**Fix.** Add this to `build/score_config.py`; score qn, rebuild every track with `--midi-only`:

```
LEAD_SPANS = {"Violins I": [(56, 128), (220, 244), (440, 480), (520, 576), (620, 644)],
              "Cor anglais": [(20, 36)], "Horn 1": [(184, 220), (584, 620)],
              "Violoncellos": [(184, 220), (584, 620), (680, 696)],
              "Clarinet 1": [(504, 520)], "Violas": [(664, 680)]}
HP_SOFT_EXTRA_SPANS = {"Clarinet 1": [(220, 244)], "Horn 2": [(220, 244)], "Cor anglais": [(683, 695)]}
```

- Keep the `PT_*` and `HP_GAIN_SOFT_DB` defaults.
- Check that the first theme's accent swells (`ACCENT_*`) still take precedence on accented onsets, as in movement II.
- This is a volume-envelope change only (CC11 unchanged). It can be checked against a stem-fix simulation before the render.
- It also feeds `APEX_AGOGIC` in finding 2.

**Pass criteria** (same 18 slurs and 41 hairpins):
- the top note is loudest in at least 10 of 18 slurs;
- the median top minus rest is +1 dB or more;
- no more than 4 crescendos rise 1 dB or less;
- no decrescendo rises;
- climax order and delivered limiter unchanged within 0.3 dB.

## 2. The tempo is exactly the metronome mark for 88% of the movement (all sections outside the printed rit./animando)

**What is wrong (tempo map measured, musical effect inferred).**
- 643 of 728 beats sit exactly on a printed metronome mark.
- The longest unbroken runs:
  - qn 272-480: 208 beats at 126.0, 99 s, the whole closing and development up to the allargando;
  - qn 56-176: 120 beats at 126;
  - qn 184-244: 60 beats at 112;
  - qn 0-56: the whole Lento, 56 beats at 50;
  - qn 680-704: 24 beats at 72 under the cello solo.
- `PHRASE_ARCS`, `TEMPO_PUSH` and `APEX_LEAD` are all empty in the mvt1 config. `APEX_AGOGIC` has no lead line to read (finding 1).
- Movement II needed this layer (kit LEARNINGS 17: +0.03-0.11 s per phrase). The c03 critic C's arcs were deferred only because Lento and coda arcs move the refitted re-bow points.

**As heard (inferred).** After finding 1, the even tempo is the most obvious remaining sign of a machine. Phrase ends arrive without any lengthening, and crescendos into the ff arrivals (bars 23-26, 38-41) do not move forward.

**Fix, in two steps** (`build/score_config.py`).

*Step 1, now.* Arcs only over spans where no string note carries a re-bow, so `rebow_moves.json` and `rebow_fills.json` stay valid. The parts.json `rebows` rows show none in qn 56-150, 200-244, 520-576 or 584-620.

```
PHRASE_ARCS = [(56, 72, "sub"), (72, 88), (104, 120, "sub"), (120, 128, "main"),
               (200, 220, "main"), (220, 232, "sub"), (232, 244),
               (520, 536, "sub"), (536, 552), (552, 568, "sub"), (568, 576, "main"),
               (584, 600), (600, 620)]
TEMPO_PUSH = [(88, 100, 1.015), (148, 160, 1.015), (552, 564, 1.015)]
```

- Bars 23-25 lead into the ff of bar 26, bars 38-40 into the sf of bar 41, and the recapitulation's crescendo into the ff.
- Keep the existing `CAESURA` and `BEAT_STRETCH`.
- The (88, 104) span is a crescendo, so it gets the push and no arc.
- After the build, diff the `rebows` rows of parts.json against c03. They must be identical. If one differs, drop the arc that overlaps it.

*Step 2, in the cycle that refits re-bows anyway.* Add the c03-C arcs `(0, 16, "sub"), (16, 32, "sub"), (32, 48), (48, 56, "main"), (680, 696), (696, 704, "sub")`. Then run `score_to_parts`, `space_rebows --write`, `score_to_parts` again, and `fit_rebows` on that render.

**Pass criteria:**
- total length change +1.5 to +3 s;
- no tempo jump over 8% at an arc's return (movement II c15/c16 hitch);
- beats exactly on the printed mark under 70%;
- re-bow rows unchanged (step 1);
- climax order unchanged.

## 3. The middle of the dynamic range sits too far under the peaks compared with real recordings (whole movement; most audible in the mp-f passages)

**Measured** (`dist.py`, `top5.py`; short-term loudness percentiles relative to the integrated loudness, frames above -60 LUFS):

| | p50 | p75 | p95 | max | p50→max | p75→max | p95→max |
|---|---|---|---|---|---|---|---|
| c03 master | -10.3 | -2.7 | +4.2 | +9.4 | 19.7 | 12.1 | 5.2 |
| c03 mp3 | -4.8 | -0.1 | +5.5 | +10.0 | 14.8 | 10.1 | 4.5 |
| Brahms 1/i | -4.2 | +1.1 | +3.4 | +6.1 | 10.3 | 5.0 | 2.7 |
| Brahms 4/i | -2.0 | +1.2 | +3.9 | +7.6 | 9.6 | 6.4 | 3.7 |
| Brahms 1/ii | -3.6 | +0.1 | +5.0 | +7.6 | 11.2 | 7.5 | 2.6 |
| Brahms 4/ii | -5.7 | +0.2 | +5.4 | +7.0 | 12.7 | 6.8 | 1.6 |

- Only five moments make up the delivered file's top 5%: bars 25-26, 82-83, 121-124, 158-162 and 169-170.
- They stand 10 dB over the file's upper quartile, where the recordings show 5-7.5 dB.
- In bar terms (bar RMS by the loudest printed dynamic; `dynbar.py`, crude):
  - p -34.5, mp -31.9, mf -32.1 and f -28.1 dB span 6.4 dB;
  - f to ff alone is 9 dB.
- The delivery ride lifts the quiet passages, but it cannot raise the mp-f body, which already sits above its knee.
- c03 critic B measured the same thing in its own terms: printed mf and f 1.6 LU apart in the delivered file. B #6 (+2 dB on every f trim) was rejected because it took 1.1 LU from f to ff.
- Against the recordings that cost is the right direction. A real ff stands about 5-7 dB over the loud body, not 10.

**As heard (inferred).** The movement sounds like long stretches of medium-soft music with a few sudden walls of sound. A real orchestra's f carries more of the weight between climaxes.

**Fix** (`build/mix.json`, level only, so it can be a stem fix: `tools/stem_fix.py 4 OLD NEW --apply`):
- On every wind, brass, string and harp track: add `"mf": 1.5` to the global `soft_trim_db` anchors (`build_reaper.vol_points` reads mp/mf anchors).
- Add +1.5 dB to each `dyn_trim_db["f"]`.
- Leave ff unchanged.
- Leave `FFF_HOLD_CAP` and the chain rise as they are.

**Simulate before applying.** Targets for the delivered file:
- p75→max at most 8.5 dB;
- p50→max at most 13 dB;
- LRA 14-16 LU;
- limiter 3 dB or less;
- climax order 160 > 122 > 170 kept, with bar 160 still at least 1 dB over every other bar.

If the order slips, take the mf anchor to +1 before cutting the f step.

## 4. The opening timpani roll pulses at its sample loop: the first sound of the movement (qn 0-16; also qn 48 and 720)

**Measured** (`timp.py`; level and centroid detrended over 6 s, best autocorrelation at lags 2.5-4.6 s).

| Note | Length | Level vs master | Stem level | Stem centroid | Master |
|---|---|---|---|---|---|
| qn 0-16 (opening roll) | 18.6 s | -9.6 dB, the loudest element of bars 1-3 | 0.56 at 3.50 s | 0.71 at 3.50 s | level 0.32, centroid 0.29 |
| qn 48 | | -17.9 dB | 0.63 | 0.84 | |
| qn 720 | | -15.2 dB | 0.55 | 0.64 | |

- The master's control values (the Allegro, qn 56-104) are 0.20 / 0.07.
- The opening is therefore the one place where the loop shows on the master. The c03 level profile only reduced it: the stem's level autocorrelation went from 0.69 (c00) to 0.56, the centroid from 0.68 to 0.71.
- A level profile cannot remove a colour cycle (kit LEARNINGS, first section).
- qn 484 (centroid 0.88) is masked by the tam-tam and the fff brass: master 0.15 / 0.23.

**Fix** (`tools/score_to_parts.py`, new generic rule `TIMP_ROLL_RESTRIKE`, applied at output like `AUTO_REBOW`):
- Split every Timpani roll (`Timpani Flt Rls`) longer than 6 s into same-pitch roll notes with irregular piece lengths of 2.3-3.3 s (seeded per note).
- Start each new piece 0.08 s before the previous one ends. The patch is polyphonic, and felt roll onsets are soft.
- Add velocity ±3 per piece.
- Leave the CC7/CC11, roles and volume shapes on the original note.
- Remove the `loop_profiles.json` entries for the split notes (Timpani 0, 48, 720), so they are not applied to a different sample cycle. Keep 484 as the unsplit control.

**Pass criteria:**
- stem centroid autocorrelation 0.3 or less on 0 and 720;
- no level step over 1.5 dB at any re-strike (80 ms window);
- master bars 1-4 band autocorrelation at 3.95 s 0.15 or less.

If the re-strike shows a bump, fit a short volume dip per re-strike with `fit_rebows.py`'s method.

## 5. The sf of bar 41 (the transition's tutti arrival) collapses within half a beat (qn 160, strings and winds)

**Where.** The score has strings and winds f with a crescendo through bar 40, then sf with a decrescendo to mf at bar 42. The horns enter ff a2 on the same downbeat.

**Measured.**
- `score_dyn` sees the sf from f, so CC11 goes 88 -> 96-100 and falls to 72-78 by qn 160.75 (`score_to_parts.py` sf/decresc branch: post = level - 10 at q + 0.75).
- Master per half beat (qn 158-162): -22.1, -22.1 | -17.1, -19.1, -22.6, -23.4.
  - The arrival is only 5 dB over the crescendo's last beat.
  - It is back under bar 40's level within one beat.
  - It sits 4.3 dB under bar 26's ff chord (-12.8).
- Violins II get quieter at the sf: -29.7 -> -30.1 -> -36.9 dB.

**As heard (inferred).** The crescendo of bars 38-40 arrives on a fp, and the horns' ff a2 call stands alone.

**Fix** (`build/score_config.py` plus a small hook in the sf branch of `score_to_parts.py`): add `SF_ARRIVAL_AT = {160.0: "ff"}`. At a listed onset:
- the spike goes to `DYN["ff"]` (114);
- the post-spike level is ff - 8 (106) instead of level - 10;
- the printed decrescendo carries the fall to bar 42's mf (72) across the bar.

Pass criteria:
- master beat 1 of bar 41 within 2 dB of bar 26 (about -14 dB per 0.5 qn);
- no fall over 4 dB inside the first beat;
- bar 42 within 1 dB of c03.

## Do not touch

- `AUTO_REBOW` with the `space_rebows` points and fitted `rebow_fills.json`: the master loop autocorrelation is under 0.25 on every held passage.
- Brass, wind and string `GENTLE_ACCENT`: master accent 2-5 kHz is a median 8 dB under the body.
- The pre-roll meter fix and `rendermap.py`.
- `TIMP_DELAY_S`, `CAESURA` 636 and the suspended-cymbal lead.
- The climax order (160 > 122 > 170) and `FFF_HOLD_CAP`.
- The c01-c03 soft trims and delivery settings: LRA 15.3 LU, limiter 2.7 dB.
- The `RAMP_SPANS` realisation of every printed rit., allargando and animando.

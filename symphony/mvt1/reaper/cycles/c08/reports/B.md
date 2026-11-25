# Cycle 8, critic B: balance and levels (render c07)

## Method

All numbers come from the stem-fixed c07 render (`cycles/c07/render/`), on the parts.json tempo map. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c08-B/`.

- **Levels:** K-weighted power, mean of L and R (3 dB under the LUFS channel-sum scale; only differences are used), 10 ms hops, from a 4096-point STFT. The master equals the float sum of the stems (residual -160 dB).
- **Note bodies:** score onset +0.08 s to min(note end, onset +1.5 s). The printed dynamic is read from each track's `dyn_curve`.
- **Hot-note residual:** a note's body minus the track's median body at the same printed dynamic (`dynmap.py`, residual scan).
- **Simulations:** `simfull.py` applies role rows, note trims and loud-span EQ changes to the stems. `deliver_master.py` then runs on the sum. `cl.py` reads the delivered short-term maxima. With no change it reproduces c07 exactly: LRA 15.3 LU, span 20.0 dB, limiter 2.0 dB, bar 160 -9.33 > bar 122 -10.07 > bars 167-170 -12.40 LUFS.

## What holds (measured)

**The dynamic mapping is consistent across families from pp to f.**

Note medians, dB:

| Group | pp | p | mf | f |
|---|---|---|---|---|
| Single winds | -41..-46.5 | -41..-46 | -37.9..-42.1 | -36.4..-39.8 |
| Horns | -41..-45 | -41.9..-43.5 | -35.3..-37.4 | -34.3..-36.1 |
| Trumpets | -41.6..-45.4 | | | -33.9..-34.8 |
| Trombones | -40.8..-44.4 | | | -30.9..-31.9 |
| String sections | -43..-45 | -42..-44.7 | -35.1..-39.8 | -32.9..-36.6 |

- The new trumpet tracks sit with the horns at pp and f, 2.7 dB under Trombone 1 at f and 1 dB over it at ff. Rimsky-Korsakov expects about level.
- **Percussion:**
  - Tam-tam fff stroke: -8.1 dB re master at bar 122, level with the violins, as a printed solo stroke would be.
  - Tam-tam pp stroke at bar 175: not among the six loudest stems, 4-6 dB under the strings.
- **Delivery:** within the brief's targets.

**Where the mapping breaks:**

- **ff to fff.** String sections gain +6.5..+8.7 dB. Trumpets, trombones and tuba gain only +1.8..+4.7 (finding 2).
- **Double basses against the celli** at the same dynamic: pp -1.5, p -1.9, mf -2.6, f -6.1, ff -7.6, fff -11.0 dB (finding 5).
- **Violas against the second violins:** ff -3.3, fff -8.7 dB (finding 4).

## 1. Hot pitches at f/ff make the wrong stem the loudest in tutti bars

**Where:** celli, Oboe 1, Horn 1, Flute 1/2, bass clarinet, Clarinet 1 and Trombone 1, across the Allegro.

**What is wrong (measured).** Body residuals at f/ff against the track's same-dynamic median:

| Track and pitch | Articulation | Residuals at f/ff (dB) | At mf/p | Effect |
|---|---|---|---|---|
| Violoncellos A-flat3 (56) | Sus MAX / Leg BC MAX | qn 100 +8.7, 548 +8.4, 556 +8.8, 526 +5.7, 272 +5.1 | -3.0..+0.4 | Celli are the loudest stem in bar 26 (-7.8 dB re master, the ff chord) and bar 138 (-7.1, 3.6 over Violins I). In bar 140 they are level with the Violins I tune. Kit LEARNINGS 13 records the same pitch and layer in movement II. |
| Oboe 1 F5 (77) | | 95 +5.5, 99 +7.2, 100 +7.9, 113 +9.7, 479 +6.2, 553 +13.3, 557 +7.8 | -0.3..+3.1 | No pitch trim exists. |
| Horn 1 F4 (65) | | 97 +7.4, 633 +10.2 | | At qn 633 Horn 1 is the loudest stem of the climax melody (-7.4 re master). This is the known Solo Horn F4 (kit LEARNINGS 13); movement I has no pitch trim for it. |
| Flute 1 G6 (91) | Sus MAX | 118 +7.3, 121.5 +6.7, 160 +10.0, 482 +7.1, 561.5 +6.6 | | Despite the -5 all-articulation trim. |
| Flute 2 E-flat6 (87) | Sus | 285 +12.6, 459 +10.2 | | The -5 trim is legato-only. |
| Bass clarinet A-flat2 (44) | Sus Non Vib | 284 +6.3, 286 +5.5, 554 +9.1 | | |
| Clarinet 1 | | 414 +6.4, 417 +6.3, 422 +4.9 | | The c07 trims reached -2.3 of the planned -6. Clarinet 1 is still the loudest stem in bars 104-106 (-4.3..-5.8), 2.1-2.4 dB over Oboe 2 in unison. |
| Trombone 1 D4 (62) | | 632 +3.7, 676 +5.6 | | In the bar-170 ff chord Trombone 1 is the loudest brass stem, 8 dB over Horn 3 on the same D4. |

**Fix.** Add these rows to `build/note_trims.json`:

| Track | Rows |
|---|---|
| Violoncellos | "100.0": -5, "548.0": -5, "556.0": -5, "526.0": -3 (in the recapitulation theme), "272.0": -3 |
| Oboe 1 | "95.0": -3, "99.0": -4, "100.0": -4, "113.0": -5, "479.0": -3, "553.0": -6, "557.0": -4 |
| Horn 1 | "97.0": -4, "633.0": -5 |
| Flute 1 | "118.0": -4, "121.5": -4, "160.0": -5, "482.0": -4, "561.5": -4 |
| Flute 2 | "285.0": -6, "459.0": -6 |
| Bass clarinet | "284.0": -4, "286.0": -4, "554.0": -5 |
| Clarinet 1 | "414.0": -3, "417.0": -3, "422.0": -2 |
| Trombone 1 | "632.0": -2, "676.0": -2 |

- Use `NOTE_TRIM_RAMP_S` 0.1 s for these onsets. The default 0.6 s leaves the attack hot.
- Leave out Horn 1 278 and 673: they are fitted accents in `accent_fits.json`.
- Use note trims, not pitch trims: the same pitches are even at mf/p.

**Simulated:**

| Bar | Before | After |
|---|---|---|
| 26 | Celli loudest | Violins II loudest (-7.0); celli out of the top three |
| 138 | Celli loudest | Violins II / violas / Violins I within 1.2 dB on top |
| 140 | Celli level with Violins I | Violins I 3.4 dB over the next stem |
| 159 | Horn 1 -9.5 | Horn 1 -10.7, under Violins I and Trumpet 1 |
| 170 | Trombone 1 -9.1 | Trombone 1 -10.7, level with Trombone 2 |

## 2. The bar 122-123 fff tutti chord is led by the violins, and its middle is hollow

**Where:** qn 484-492, the second climax (sostenuto, tam-tam fff).

**What is wrong (measured).** Levels re master, qn 484.3-487.5:

| Stems | Level (dB) | Note |
|---|---|---|
| Violins I / II | -9.6 / -8.5 | |
| Trumpet 1 | -13.2 | |
| Trombones 1 / 2, bass trombone | -14.3 / -12.5 / -12.4 | |
| Tuba | -16.9 | |
| Horns 1-4 (all fff) | -17.8..-20.6 | |
| Violas | -21.4 | Tremolo row on B3 + D4, velocity 127, envelope about -1 dB: 13 dB under Violins II |
| Double basses | -26.8 | 0.3% of the master's K power |

- Over 484-492 the violins supply 68% of the master's 2-5 kHz. All trumpets and trombones together supply 6%.
- The tam-tam supplies 58% of 60-100 Hz.
- Rimsky-Korsakov (*Principles*, "Comparison of resonance", text p. 51-52) gives, in forte: one string section = 2 woodwinds, and trumpet = trombone = tuba = 2 horns = 4 woodwinds. A trumpet or trombone should therefore stand about 3 dB over a violin section, and a horn level with one.
- Measured, the violins are 4-6 dB over the trumpets and trombones and 8-11 dB over the horns.
- The cause is the ff-to-fff growth: strings +6.5..+8.7 dB, brass +1.8..+4.7.
- **Inferred:** the second climax sounds like a high violin tremolo with a tam-tam, not like a full brass chord.

**Fix: `build/roles.json`.** Add these rows, starting at 484.0 with a 0.2 qn ramp so the bar-121 approach is untouched:

| Track(s) | Row |
|---|---|
| Violins I, Violins II | [484, 492, -3] (on top of the existing [484, 496, -4]) |
| Horns 1-4 | [484, 492, +4] |
| Violas | [484, 492, +6] |
| Double basses | [484, 492, +4] |
| Trumpets 1-3 | [484, 492, +1.5] (with the existing +2: +3.5) |

Keep the tam-tam, `ARRIVAL_WEIGHT_AT` 484 and the `_all` row.

**Simulated.** Levels re master after the change:

| Stems | Level (dB) |
|---|---|
| Violins I / II | -12.6 / -11.5 |
| Trumpet 1 | -11.8 |
| Trombones | -12.4..-14.3 |
| Horns | -13.9..-16.6 |
| Violas | -15.5 |
| Double basses | -22.8 |

On its own, the change moves the bar 122 short-term maximum from -10.07 to -10.19 LUFS. Together with the other findings it moves to -9.97. The climax order is kept.

## 3. In the bar-82 ff motive, Trumpet 1 is buried under its own section's held notes

**Where:** qn 324-328.

**The score:** Fl, Ob, Cl 1, Tpt 1, Vln I/II and Vla play the accented motive ff. Trumpet 2 holds A-flat4 and Trumpet 3 holds E-flat4. The celli play an ff half note.

**What is wrong (measured):**

| Stem | Level re master (dB) | Note |
|---|---|---|
| Trumpet 1 (motive) | -12.3..-14.7 | from 325 to 327.5 |
| Violins I (same motive, octave up) | -5.6..-9.4 | |
| Trumpet 2 (held note) | -8.1..-12.2 | over Trumpet 1 by 2.6-6.6 dB at 326.5-327.5 |
| Celli | -3.5 at 324.5; -7.5 over the bar | the loudest stem of the bar |
| Violas (motive) | -18.2..-19.7 | 11 dB under Violins I |

In 324-332 Trumpet 1 supplies 1% of the master's 2-5 kHz and the violins 82%. The trumpet doubling, which should colour the motive, is inaudible (inferred).

**Fix: `build/roles.json`.**

| Track | Row |
|---|---|
| Trumpet 1 | [324.4, 328, +4], ramp 0.2 |
| Trumpet 2, Trumpet 3 | [324, 328, -2] |
| Violoncellos | [324, 328, -3], ramp 0.25 |
| Violas | [324.5, 328, +3] |

**Simulated:**

- Trumpet 1: -9.1..-9.9 re master, 1.5-2 dB under Violins I and over its section's held notes.
- Celli: -9.5..-12.5.
- Bar 82 delivered: -12.81 -> -12.94.

## 4. The violas fall away at ff when they double a theme

**Where:** bars 27-30, qn 104-120. The theme is in three octaves: Violins I G5, Violins II G4, violas G3.

**What is wrong (measured):**

| Section | Level re master per bar (dB) |
|---|---|
| Violins I | -5.7..-9.4 |
| Violins II | -10.5..-14.3 |
| Violas | -14.5..-18.2 |

- Across the movement, violas minus Violins II at the same dynamic is -0.5 at pp, -1.0 at mf and -0.6 at f, but -3.3 at ff and -8.7 at fff.
- Celli minus violas grows from +0.3 (pp) to +3.5 (ff) and +5.8 (fff).
- `mix.json` gives the violas `dyn_trim_db` f -2, ff -3. That trim suits their accompaniment figures (bars 98-102 and 158-161, which also have roles) but not a doubled theme.
- **Inferred:** the lowest octave carries the theme's body, and it is missing.

**Fix:** `build/roles.json` Violas [104, 120, +2.5]. Bar 82 is covered in finding 3.

Do not change the ff trim: the accompaniment passages need it.

## 5. Low end at the loud tutti: a 125-160 Hz hole that the basses cannot fill

**What is measured:**

- **Spectrum** (loudest 10% of frames, 1/3-octave re 1 kHz) against the Dvořák reference:

  | Band | Mix minus reference (dB) |
  |---|---|
  | 50-80 Hz | +5.5..+14.4 |
  | 100 Hz | +1.2 |
  | 125 Hz | -7.5 |
  | 160 Hz | -7.9 |

  The 50-80 Hz excess may come partly from the lossy reference (kit LEARNINGS 14). Over the whole movement, 100-250 Hz is also 1-3 dB under all three references.

- **Who supplies the low end:**
  - The basses supply 59-79% of 60-100 Hz in the loud tutti, but only 0.3-1.6% of K loudness.
  - The basses sit 7.6 dB (ff) and 11 dB (fff) under the celli, which carry the bass line's audible weight through their +6 dB loud bell at 150 Hz.

**What was simulated:**

| Change | Effect |
|---|---|
| Basses: loud `bell2` 98 Hz -4 replaced by a low shelf 80 Hz -4, +2 dB gain | 100 Hz +2.5 dB, 125/160 Hz +0.1..+0.3 dB |
| Basses +3 with celli -3 on the shared bass lines | 20-60 Hz +3 dB, 100-160 Hz -1..-2 dB (worse both ways) |

So the hole is in the voicing, as in kit LEARNINGS 14, and raising the basses only adds boom. Do not raise the basses or cut the celli for this.

**Optional fix:** add a loud_eq bell at 140 Hz on Tuba, Bass trombone and Contrabassoon (+4 dB, 1 oct) and on Bassoon 2 and Timpani (+3 dB). Use the existing loud spans. Simulated: 125/160 Hz +1.2/+1.8 dB, delivery unchanged (LRA 15.3, limiter 2.0, climax order kept).

## Combined simulation of findings 1-4

- Delivered: LRA 15.3 -> 15.0 LU, span 20.0 dB, limiter 2.0 -> 2.1 dB, -1.6 dBTP.
- Climax order: bar 160 -9.27 > bar 122 -9.97 > bars 167-170 -12.49. The margin narrows 0.74 -> 0.70 dB.
- Spec: `sall2.json` in the scratch folder.

## Dan's two checks (measured)

**Loop pulse.** 17 notes are longer than 6 s (the strings are re-bowed). The highest autocorrelation at 3.95 s:

| Note | 100-300 Hz | Centroid | Stem re master |
|---|---|---|---|
| Bass clarinet, qn 492 (7.2 s) | 0.83 | 0.58 | -13.6 dB, under the bar 124-125 trombones |
| Horn 4, qn 289 | 0.67 | 0.27 | -9.8 dB |
| Bass clarinet, qn 480 / 464 | 0.60 / 0.40 | | |
| Bassoon 2, qn 48 | 0.54 | | |

On the master: 464-500 band -0.24, 696-728 -0.10. No change proposed from this lens. If critic A finds the bass clarinet audible, it is a `BREATH_SPLIT_AT` candidate (inferred).

**Accents.** 2-5 kHz in the first 80 ms minus the body. The 85 ms analysis window reads short notes high.

| Track(s) | Median (dB) | p90 (dB) | Worst |
|---|---|---|---|
| Trumpets, trombones, tuba | -6.8..-12.9 | | |
| Horns | -0.6..-7.7 | +6.8..+7.8 | Horn 3 286 +13.1, Horn 1 665 +10.6 (c07's own fit read 665 at +3.6) |
| Strings and woodwinds | -1.8..-7.2 | | |

The horn outliers should be checked with `fit_accents.py`'s 2-5 kHz print before acting.

## Do not touch

- The soft trims (global 7/7/5 and the per-track overrides). They give the even pp/p/mf mapping above.
- The trumpet loud trims (f 7, ff 8; Trumpet 3 8/11).
- The tam-tam fff stroke, its damp and `tail_hold` false. The suspended cymbal and crash levels and timing.
- `accent_fits.json`: refit if a brass role around an accent moves.
- The c07 roles at [628, 644] and the chorale roles at [696, 712].
- The climax order (160 > 122 > 167-170). `ARRIVAL_WEIGHT_AT` 484/636.
- The celli's 150 Hz loud bell and the basses' EQ: finding 5 shows the alternatives are worse.

# Cycle 8, critic A: articulation and phrasing (render c07)

Scope: every wind, brass, string, timpani and harp note in `build/parts.json` (the c07 build after its stem fix, which is what `cycles/c07/render/` carries), measured on the c07 stems and master.

Scripts, 5 ms feature files and a simulation copy of `tools/` + `build/` are in `/private/tmp/claude-501/mockup-loop/mvt1-c08-A/`:
- The c07-A scripts were rerun on c07: `acc2.py`, `after.py`, `joins.py`, `tremj.py`, `hrep.py`, `breath.py`, `longloop.py`, `rebow.py`, `slurs.py`, `markmap.py`.
- New scripts:
  - `accfam.py`: the `fit_accents.py` measure applied to winds and strings.
  - `notelv.py`: per-note level, CC11 and envelope.
  - `susbloom.py`, `stacsep.py`, `ties.py`, `chordleg2.py`, `uni.py`, `a2exp.py`, `timp.py`, `trace.py`.
- `sim/`: a copy of `tools/` and `build/`, where `fit_accents.py --family string|wind --write` was run. Its output is `sim/fit_string.txt`, `sim/fit_string5.txt` and `sim/fit_wind.txt`, and the resulting table is `sim/build/accent_fits.json`. The project's own `build/` was not touched.

## Checks that passed (measured)

- **Dan's item 8 (2-5 kHz energy in the first 80 ms minus the body).**
  - Medians by family:

    | Family | Median |
    |---|---|
    | Strings | -2.5..-5.3 dB |
    | Woodwinds | -4.0..-11.4 dB |
    | Brass | -4.2..-16.1 dB |

  - On the master, the 2-5 kHz jump at an accent is a median +0..+1.4 dB.
  - The positive readings are known window artefacts:
    - Horn 1 at 665 reads +13.9 dB from the score onset. This is the bright ff pickup before the legato target; it reads +3.6 dB from the sounding onset (c07 CHANGES).
    - Bassoon 1, Clarinet 1 and the celli at 536 read +16.7, +6.6 and +8.5 dB. This is the earlier-note artefact.
- **Dan's item 7 (loop pulse).**
  - String re-bow dips are unchanged from c06/c07. The master dip at re-bows is a median -1.5..-2.4 dB per section; the worst stem joins are celli 163.877 (-6.4 / step -9.3) and 37.377 (-6.1 / +5.0), the deferred refit.
  - No wind or brass note of 9 s or more has a level autocorrelation over 0.6 at the loop period.
  - The 6-8 s spans that read high are only two periods long, so the readings are unreliable: Bassoon 2 at 684 (0.91), Bass clarinet at 492 (0.72, swing 7.1 dB, stem 13 dB under the master) and Horn 3 at 724.6 (0.74).
  - The timpani roll restrikes hold at 0.08-0.46.
- **Legato structure.**
  - No chord or held overlap is sent to a Leg row (`chordleg2.py`: 0).
  - Every slurred wind and brass note past a slur's first note is on a Leg row, except the listed portato re-tongues (Flute 1 393, Oboe 1 405, Horn 1 413).
  - Wind and brass join dips: median 0.3-4.5 dB. String joins: median 1.7-2.5 dB, with 2-5 joins per section at 6 dB or more.
  - The remaining wind and brass holes of 6 dB or more are Flute 2 279 (10.2 dB, no better option per c07), Horn 2 453 (8.9) and Horn 2 266 (6.6).
- **Ties.** No tied note is re-attacked except the planned timpani tie strokes and the basses' "change bow at will" re-bows.
- **Staccato** (`stacsep.py`). Every printed staccato separates by a median 8-15 dB per note on its row: wind Sus MAX at half length 7.8-12.8 dB, string Stac rows 11.3-15.0 dB.
- **Pizzicato and harp.** Unchanged and passing.
- **Wind and trumpet repeats.** Medians 4.2-6.7 dB.
- **Brass accents** (`fit_accents.py`, c07). 33 of 36 sit 2-4 dB over their neighbours.

## 1. The string accents, including the Violins I's main theme, mostly do not sound: 50 of 137 sit less than 1 dB over the unaccented notes around them

**Measured** (`accfam.py`). This is `fit_accents.py`'s own measure on the c07 stems: the level over +0.05..+0.35 s against up to two unaccented same-dynamic neighbours on each side, within 2.5 qn.

| Family | Accents | In 2-4 dB | Under 1 dB | Over 5 dB |
|---|---|---|---|---|
| Brass (fitted in c07) | 36 | 33 | 0 | 2 |
| Strings | 137 | 28 | **50** | 29 |
| Woodwinds | 146 | 34 | 29 | **52** (finding 2) |

**Violins I.** 21 of 38 accents are under 1 dB, median +0.8. Most are the theme head: an eighth pickup slurred to an accented dotted quarter, a 6-12 semitone leap up, on Leg Slur MAX.

Bars 15-19, f, CC11 88 throughout (`notelv.py`, 0.05-0.35 s levels):

| qn | Note | Level |
|---|---|---|
| 56.5 | pickup | -39.2 |
| **57** | accent | **-36.7** (body -34.7) |
| 58.5 | | -36.1 |
| 59 | | -35.4 |
| 59.5 | C5, merged slur-end note on Sus MAX | -32.4, body **-28.2** |
| 61 | | -30.7 |
| 62 | accent | -31.9 |
| 64.5 | pickup | -40.5 |
| **65** | accent | **-37.3** |
| 67 | | -33.9 |
| 67.5 | | -32.8 |
| **73** | accent | **-35.9** |
| 75 | | -33.4 |

The +3 dB string swell is in the envelope (57.147: +5.0 against +2.0 around it), so the accent is weak in the sample, not missing in the data. As with the brass theme heads in c07 (LEARNINGS "Accents (c07)"), the legato transition carries over the quiet slur-first-note pickup. On top of that, the slur's last note, merged onto Sus MAX (59.5), blooms 4 dB inside the note and ends 7.2 dB over the Leg note before it (`susbloom.py`; Violins I 571.5: +5.9).

The recapitulation (bars 131-134, ff, CC11 114) shows the same order:

| qn | Note | Level |
|---|---|---|
| 521 | accent | -31.6 |
| 523 | unaccented | -29.3 |
| 525 | accent | -29.8 |
| 529 | accent | -32.6 |
| 531 | unaccented | -30.8 |

Other sections:
- Violins II: under 1 dB at 521 (-4.3), 536 (-3.3) and 529 (-2.0).
- Violoncellos: 342 (-3.9).

Inferred: in the leading voice of the first theme, the stress falls on the weak resolution note and not on the accented dotted quarter. The phrase swells toward its end. This is the most audible articulation fault left, and it comes back in every statement of the theme (bars 15-19, 35-38, 131-134).

**Fix.** The c07 tool already covers strings: `GENTLE_ACCENT["string"]` exists, and `ACCENT_FITS` applies to every gentle family.

1. Run `tools/fit_accents.py 7 build/parts.json --family string --max-trim 5 --write`.
   - Simulated in `sim/` with the c07 parts.json as both reference and build: 127 of 137 accents are predicted in 2-4 dB (median +2.97, min -0.2, max +6.5). With the default `--max-trim 3` the figure is 123 of 137.
   - Violins I fits: 57 [5.0, +4.41], 65 [5.0, +5.0] (predicted -0.1, still short), 113 [5.0, +5.0], 521 [5.0, +4.11].
   - It also writes negative trims where accents stand too high: Violins II and violas down to -6 dB, on strokes.
   - The fit is level only, so the actor can render it, or apply it to the stems with `stem_fix.py` and then refit (c07 method).
2. `build/note_trims.json`: Violins I 59.5 -4.0 dB and 571.5 -3.5 dB (merged slur-end Sus MAX notes).
   - They are not accents, so the fit does not see them.
   - Use the step shape for notes on Sus rows that are joined (ramp-in 0.1 s, not 0.6 s), so the bloom is cut from the start.
3. Theme heads that are still short after one render (65, 113, 479): add them to `ACCENT_DB_AT` with a higher swell cap rather than a larger step trim.

**Pass:**
- Strings with 2-4 dB over their neighbours: at least 100 of 137, measured by `fit_accents.py`.
- Violins I at 57, 65, 73, 521 and 529: +2 dB or more over 59/67/75/523/531.
- 2-5 kHz first-80-ms minus body still 0 dB or less.
- Delivery limiter no higher than 2.0 dB + 0.5.

## 2. Woodwind accents stand 5-17 dB over their neighbours (52 of 146), and the theme accents in Clarinet 1 are the worst

**Measured** (`accfam.py`). The wind gentle swell (3.5 dB at f, 2 dB softer) adds to rows and samples that already sit high:

| Track | Accents | In 2-4 dB | Over 5 dB | Examples |
|---|---|---|---|---|
| Clarinet 1 | 37 | 8 | **19** | 105 +8.7, 124 +8.1, 564 +8.2, 414 +7.8, 475 +7.2 |
| Flute 1 | 32 | 3 | 11 | 553 +10.5, 113 +9.1, 156 +7.0 |
| Oboe 1 | 31 | 8 | 10 | 553 +17.5, 113 +13.9, 475 +11.5, 330 +11.4 |

Some are under 1 dB: Flute 1 110 -4.6, Oboe 1 285/118/124 about -3.

Inferred: in the tutti the woodwind accents poke out of the line. Dan's rule 4 asks for emphasis, about 2-4 dB.

**Fix.** Run `tools/fit_accents.py 7 build/parts.json --family wind --write`, after the string fit, so that both stay in `accent_fits.json`. Simulated in `sim/`: 138 of 146 predicted in 2-4 dB (median +2.97).

One guard is needed in `fit_accents.py` `plan()`. Several of the high readings have a single neighbour that is the slur's own short first note: Oboe 1 553 (only 552.5), Flute 1 553, Clarinet 1 553. That pickup plays the legato row's slow first-note layer and never reaches body level, so the fit answers with a -6 dB trim on the phrase's arrival note (simulated: Flute 1 553 [0, -6.0], Oboe 1 [.., -6.0]).
- Do not use as a neighbour a note of 0.5 qn or less that starts a slur.
- Leave an accent alone when no neighbour remains.
- Use `--min-trim -4` for winds.

**Pass:**
- Woodwinds with 2-4 dB over their neighbours: at least 110 of 146.
- No wind accent more than 5 dB over its neighbours.
- No fitted trim on an accent whose only neighbour was a slur pickup.

## 3. Doubled lines play as one solo sample +3 dB: the horns a2 in all three statements of the theme and at the climax, trumpets a2 in the coda

**Measured** (`uni.py`). These are the notes that `find_unisons()` drops from the second player, whose copy is then played by the first player's track, with +10·log10(2) dB.

| Player | Notes dropped | Main spans (dynamic) |
|---|---|---|
| Horn 2 | 97 | 272.5-286 (bars 69-72, f, the closing theme, 19 notes); 381.5-404 (bars 96-101, f, 20); 628-643.5 (bars 158-161, ff, the climax, 13); 662-676 (bars 166-169, the coda theme, 16) |
| Clarinet 2 | 65 | 272.5-286, 408.5-423.5, 520.5-534 (ff) |
| Bassoon 2 | 47 | 520.5-544 (ff, 24) |
| Trombone 2 | 32 | 464-480, 520.5-534 (19) |
| Trumpet 2 | 23 | 664.5-676 (ff, 16) |

- Horn 1 in those spans sits 8.7-13.7 dB under the master (`a2exp.py`). It carries the tune in bars 69-72 and 166-169.
- Kit section 8 measured identical-patch unisons at correlation 0.999. One solo sample louder is a solo horn, not two.

Inferred: the closing theme and the coda theme sound like a solo horn (and a solo trumpet) playing loudly, without the width and slight beating of two players. In an ff a2 this is a change of instrument colour, not a level detail.

**Fix** (horns first: the patch is mapped and was used in movement II c18).
1. **New track.** In `build/score_config.py` `TRACKS`, add `("Horns 1-2 a2", ["Hn1"], B + "2 French Horns/06 Keyswitch/2FH KS Master.oib", "brass", <Horn 1 pan>)`.
   - Rows: Sus MAX and Leg Slur MAX only. The `2FH KS Master` map is already in `ks_maps.json`.
   - Mics: Close 0.5 / Main 1.0.
   - Gain: start at Horn 1's gain +4.6 dB (kit section 8, c18), then set it from the render.
2. **Routing.** Do not use whole `TRACK_WINDOWS` windows. `TRACK_WINDOWS` holds one window per track, and Horn 2 has its own notes inside two of the spans (276.0 A-flat3, 668.0 C4), which would land on the legato row as chords.
   - Add `A2_ROUTE = {"Horns 1-2 a2": {"pair": ("Horn 1", "Horn 2"), "spans": [(272.5, 286.5), (381.5, 404.5), (628.0, 644.0), (662.0, 677.0)]}}` in `score_to_parts.py`.
   - A Horn 1 note whose Horn 2 copy `find_unisons()` drops, and that falls inside a span, moves to the a2 track without the +3 dB.
   - Everything else stays on Horn 1 and Horn 2.
   - The a2 track takes Horn 1's per-onset tables (leads, fills, accent fits) by score onset. Refit its accents with `fit_accents.py` after the render.
3. **Trumpets** 664.5-676 the same way on `2 Trumpets/06 Keyswitch/2TP KS Master.oib`, after dumping its keyswitch map with `libs/ew_ho/dump_ks.py` (it is not in `ks_maps.json`). Do this in a later cycle if memory is short.
4. **Woodwinds.** No a2 patch exists for clarinets or bassoons, only 3-player ensembles. Leave them.

**Memory.** One more instance with two rows. c07 settled at 43 GB (23 compressed). The 32 instances average about 1.3 GB, so 44-45 GB is expected. Check `top` after loading settles, per BRIEF item 9.

**Pass:**
- The a2 track's level over 272.5-286 and 662-676 within ±1 dB of c07's Horn 1 (roles unchanged).
- Its legato join dips no worse than Horn 1's median of 1.0 dB.
- No chord on its Leg row.
- REAPER under 46 GB after the render.

## 4. Tremolo still re-attacks at every chord change and every bar (Violins II bars 147-153, pp; celli bars 117-121, f)

**Measured** (`tremj.py`, `longloop.py`, `trace.py`). The tremolo data are unchanged since c06; c07 deferred A #4.
- **Violins II, "div. sul tasto" pp under the recapitulation's second theme:**
  - The chord changes at 592/596/600/604/608 dip -3.7/-6.8/-4.8/-7.7/-4.8 dB on the stem, and -1.1..-2.3 dB on the master at 596-608.
  - In all, 11 of 41 tremolo changes in the movement dip 4 dB or more:

    | Track | Changes (dip) |
    |---|---|
    | Violins II | 304 (-9.9), 484 (-5.5), 440 (-4.8) |
    | Violins I | 484 (-7.7) |
    | Celli | 464 (-7.0), 468 (-4.5) |

- **Celli, five untied G2 tremolo whole notes, bars 117-121 (464-484, f, `cresc.` from 480):**
  - The stem pulses once per bar. Each re-attack starts 2-4 dB down and rises to a peak about 0.8 s into the bar.
  - Peaks: -31.5 dB at 469.8, 473.6 and 477.8. Troughs: -36..-37 dB at 467.3, 471.5, 475.7 and 479.5.
  - Level and 100-300 Hz autocorrelation at the two-bar lag (3.81 s): **0.88 / 0.89**; centroid 0.91; swing **7.9 dB**. This is the highest periodic reading of any held line in the movement.
  - The volume envelope also puts a +3.1..+4.4 dB, 0.25 qn bump at each barline (468, 472, 476, 480: -1.87 -> -0.6 -> -5.0 dB). Its source rule was not identified; the chord cut (`chord_db`) boundary at the note change is the likely one.

Inferred: the sul tasto pad pulses once per bar, and the celli's f tremolo under the build to the tam-tam sounds as five separate strokes instead of one tremolo.

**Fix** (`tools/score_to_parts.py`).
1. **Chord changes.** c07-A #4 as specified: `TREM_JOIN_TRACKS` (all four upper sections); moving voices start `TREM_LEAD_S` 0.3 s early; old notes end at the new score onset + 0.4 qn (`TREM_OVERLAP_QN`); a pitch held across a change continues as one note with a 3 CC notch.
2. **Celli.** `TREM_MERGE_AT = {"Violoncellos": [(464.0, 484.0)]}`.
   - Merge the same-pitch tremolo notes into one held note.
   - Split it at output like `TIMP_ROLL_RESTRIKE`: abutting same-pitch Tremolo pieces of irregular 2.5-3.3 s, seeded, never on a barline, the old piece ending 0.005 qn before the new one.
   - This removes the bar-period pulse without one 9.5 s sample looping.
   - Remove the bar-start envelope bump for merged notes.

**Pass:**
- Every tremolo change dips 3 dB or less on the stem.
- Celli 464-484: level autocorrelation at 3.8 s under 0.4, swing under 4 dB.
- Violins II mean level over 584-619 within ±1 dB of c07.

## 5. Horn breaths and the soft horn pedal are still not separated; loud woodwind breaths at the climax are shallow

**Measured** (`breath.py`, `hrep.py`). Dips at printed breaths:

| Breath (qn, dynamic) | Dip |
|---|---|
| Horn 1, 475 (f) | -3.1 dB |
| Horn 3, 256 (p) | -3.2 dB |
| Horn 3, 536 | -2.1 dB |
| Horn 4, 512 (pp) | -2.6 dB |
| Flute 1 / Oboe 1, 636 (before the fff) | -3.0 / -3.9 dB |
| Controls: Trumpet 1, Trombone 1, Bass trombone at 636 | -7.5..-10.7 dB |

- `BREATH_FALL_BY` applies only at mf or louder, and Horn 1 475 at f still reads -3.1 dB.
- Horn 4 repeats: median -2.7 dB, 8 of 12 under 3 dB (232, 256, 484, 488, 496, 624). Horn 3 is now -5.0 dB with none under 3.

**Fix** (`build/score_config.py`).
- `BREATH_GAP_AT`: 0.4 qn for Horn 1 475, Horn 3 256/536 and Horn 4 512.
- `BREATH_FALL_CC`: 8 for the same breaths, also below mf (soft horns need the fall too: kit section 7, c15).
- `BREATH_FALL_BY`: a "wind" entry of 8 CC for Flute 1 / Oboe 1 at 636.
- Horn 4 repeats: `WIND_REP_RETONGUE_BY["Horn 4"] = {"gap_s": 0.14, "frac": 0.35, "fall_cc": 14, "fall_s": 0.18}`.

**Pass:**
- Every listed breath dips 4 dB or more.
- Horn 4 repeat median 3.5 dB or more.

## 6. Smaller items

- **Timpani metric weight** (measured, `timp.py`). Off-beats and pickups still hit as hard as the downbeats they lead to: bars 27-30, 105.5 -27.3 against 104 -26.9 and 107.5 -26.8 against 108 -23.9 dB. Bar 82's eighths run -23.8 down to -25.8 dB, a flat ladder. Velocity moved this only 0.6 dB (c07). Extend `METRIC_DB` (now used for plucked notes) to the Timpani Flt Lng strokes at f and louder: down 0, beat 3 -1.0, beats 2/4 -2.0, off-beats/pickups -3.0 dB, as a step at full value on the stroke (kit section 10, c10). Pass: off-beats 2-4 dB under the next downbeat.
- **Horn 2 joins 453 (8.9 dB) and 266 (6.6 dB)** (measured). Leave them for `auto_fills.py` on the next pass. If they survive it, add them to `--exclude` with a hand fill of dip - 3 dB held to the sag minimum (kit section 6).
- **Celli re-bows 163.877 / 37.377 and basses 166.01** (measured, deferred since c07): dips of -6.4/-6.1/-5.3 dB and steps of -9.3/+5.0/-4.2 dB. Refit with `fit_rebows.py` together with the next re-bow change.

## Do not touch

- `accent_fits.json` brass entries and brass `keep_legato`.
- `GENTLE_ACCENT` articulations (no accent samples on any family: 2-5 kHz attack minus body negative everywhere).
- `ROW_TRIM_DB` with `ROW_TRIM_SKIP`.
- The slurred-repeat merges and the strokes' velocity rule, `REP_SPLIT`, `STR_SHORT_AFTER_SUS`, `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`.
- `WIND_REP_RETONGUE` for woodwinds, trumpets and trombones, and the c07 horn values for Horns 1-3.
- The 632/636 low-brass breath gaps.
- `AUTO_REBOW` rows, `space_rebows` and the fitted re-bow shapes; the timpani re-strike plans; `BREATH_SPLIT_AT`.
- `PORTATO_JOIN_AT`, `PORT_TARGETS`, `META_DB`.
- Pizzicato and harp rows and velocities; staccato rows (8-15 dB per-note separation).
- `TIMP_DELAY_S` and the sus. cymbal and crash timing; the pre-roll meter fix; the climax order (160 > 122 > 169).

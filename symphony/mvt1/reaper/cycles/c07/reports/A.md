# Cycle 7, critic A: articulation and phrasing (render c06)

Scope: every wind, brass, string, timpani and harp note in `build/parts.json` (the c06 build). Measurements are on the c06 stems after the stem fix and on the master. Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c07-A/`.

- The c06-A scripts were rerun on c06: `acc2.py`, `joins.py`, `rep2.py`, `rebow.py`, `longloop.py`, `breath.py`, `xall.py`.
- New scripts:
  - `rowoff2.py`: Sus against Leg level at the same CC11.
  - `after.py`, `accneg.py`, `head.py`, `head7.py`: accent weight.
  - `tremj.py`: tremolo chord changes.
  - `hrep.py`: repeats.
  - `markmap.py`, `slacc.py`: which articulation row each printed mark is played on.
  - `vt.py`: the Violins I eighth test.

## Checks that passed (measured)

- **Accent attacks (Dan's item 8).** 2-5 kHz energy in the first 80 ms minus the note body, median per track:

  | Family | Median range |
  |---|---|
  | Strings | -1.6..-5.4 dB |
  | Winds | -4.8..-11.2 dB |
  | Brass | -3.5..-16.5 dB |

  - The only positive brass readings are Horn 1 at 665 (+4.9 dB) and 273 (+3.3 dB). Both are slurred accents that are re-tongued (finding 3).
  - The 536 outliers (Bassoon 1 +15.4, Clarinet 1 +6.2, celli +6.2) are the known earlier-note artefact.
- **Loop pulsing (Dan's item 7).** Every string re-bow series is within the c06 figures: master dip at re-bows -1.4..-2.2 dB median.
  - Long held winds and brass: no note of 9 s or more has a level autocorrelation over 0.6.
  - A few 6-8 s spans read 0.7-0.9: Horn 4 at 228, Bassoon 2 at 684, Bass clarinet at 492. These windows are only about two loop periods long, so the reading is unreliable, and the stems sit 10-16 dB under the master.
- **Legato structure.**
  - No chord is sent to a Leg row.
  - Wind and brass legato joins have a median dip of 0.3-4.5 dB.
  - String joins: median 1.6-2.5 dB, with 2-5 joins per section at 6 dB or more.
  - Pizzicato, the harp rolls and the harp étouffez are unchanged since c05 and still pass.
- **Wind and trumpet repeats** (c06 `WIND_REP_RETONGUE`): Trumpets 1-3, Contrabassoon, oboes and clarinets have median dips of 4-7 dB.

## 1. Loud string lines change level by 4-6 dB when they switch between Sus MAX and the Leg rows, so the main theme's accented notes sit under the unaccented eighths that follow them

**Measured** (`rowoff2.py`). Adjacent non-accented notes, under 4 semitones apart, at the same CC11 (±2), one on Sus MAX and one on Leg Slur MAX or Leg BC MAX. The volume envelope is removed, and the level is taken over +0.08..+0.3 s. Sus minus Leg at CC11 80 or more:

| Track | Sus minus Leg | Pairs |
|---|---|---|
| Violins II | **+4.7 dB** (IQR +2.3..+5.7) | 12 |
| Violas | **+5.6 dB** | 9 |
| Violoncellos | +2.1 dB | 4 |
| Violins I | +1.7 dB | 20 (most of its eighths are now on Leg, see item 6) |

At soft levels the offset is small or reversed (celli -3.5 dB). This matches kit section 6: Sus MAX and Leg Slur sustains differ by 3-9 dB at one CC11. The winds and brass show no consistent offset.

**Measured: effect on the printed accents** (`after.py`). The accented note's first 0.03-0.2 s against the loudest of the next 2-3 unaccented notes. Accents more than 2 dB under a later unaccented note:

| Track | Accents under a later note |
|---|---|
| Violins I | 6 of 26 |
| Violins II | 6 of 24 |
| Violas | 7 of 22 |
| Violoncellos | 2 of 7 |

Examples:
- **Bar 27, Violins II, ff, constant CC11 113-114.** The accented E-flat (105, Leg Slur MAX, +3 dB accent swell) reads -34.0 dB. The slurred Sus MAX eighths after it read -31.0, -27.5 and -24.6 dB, so the accent sits **9.4 dB under** the note that follows it. The same happens at 113 (-4.8 dB) and at 553 (-12.3 dB, partly the printed cresc.).
- **Violins I:** 569 sits 6.4 dB under the Sus eighth at 571.5.
- **Violas:** 105 sits -3.3 dB under the note after it.
- **Stac rows:** the Stac RRx9 rows play louder still. Violas 349/381 sit -6.0/-7.8 dB under the staccato after them, celli 337/342 -4.4/-9.6 dB (mvt I LEARNINGS c04: Stac strokes 5-8 dB over the merged notes).

Inferred: the theme's stress pattern is reversed. The long accented note is the quietest note of the figure, and the eighths swell out of it. A listener hears the line as lurching in level each time it changes row.

**Fix** (generic, new table `ROW_TRIM_DB` in `tools/score_to_parts.py`; movement I values in `build/score_config.py`).
- **Format:** `{track: {art: (dB, min_cc)}}`.
- **Which notes:** a string note on a listed row, with CC11 at its onset of `min_cc` or more, that has a Leg-row note within 1 qn on the same track (a mixed line).
- **Exclusions:**
  - accented notes (they keep their swell);
  - `DOWNBOW_STROKE_AT` strokes;
  - re-bow pieces;
  - `REP_SPLIT`, `STR_SHORT_AFTER_SUS` and `rep_stac` strokes (these already carry fitted roles).
- **Shape:** a stepped volume trim at the moved onset, ramped over `NOTE_TRIM_RAMP_S`, held to the next onset. This is the same shape as `note_trims`.
- **Start values** (about 85% of the measured offsets):

  | Track | Row | Trim | min_cc |
  |---|---|---|---|
  | Violins II | Sus MAX | -4.0 dB | 80 |
  | Violas | Sus MAX | -4.5 dB | 80 |
  | Violas | Stac RRx9 | -4.0 dB | 80 |
  | Violoncellos | Sus MAX | -1.5 dB | 80 |
  | Violoncellos | Stac RRx9 | -4.0 dB | 80 |
  | Violins I | Sus MAX | -1.5 dB | 80 |
  | Violins I | Stac RRx14 | -3.0 dB | 80 |

- **Rendering:** this is level only, so it can be done as a stem fix if the actor prefers (LEARNINGS section 15).
- **Balance:** it lowers the loud passages slightly. Check the climax order (160 > 122 > 169) and critic B's balance; the limiter should not rise.

**Pass criteria.**
- `rowoff2.py` Sus minus Leg at CC11 80 or more within ±1.5 dB on every string track.
- Accents more than 2 dB under a later unaccented note: 2 or fewer per string track.
- Violins II at 105: -2 dB or better (now -9.4).
- Climax order kept.

## 2. Horns, Bassoon 2 and the low brass do not separate repeated notes or breaths: the release and hall fill a 0.06 s gap

**Measured: repeats** (`hrep.py`). Unslurred same-pitch repeats, all re-tongued by `WIND_REP_RETONGUE` (gap 0.06 s, fall 6 CC). Dip under 3 dB:

| Track | Repeats | Under 3 dB | Median dip |
|---|---|---|---|
| Horn 1 | 14 | 7 | -2.6 dB |
| Horn 2 | 12 | 9 | -1.3 dB |
| Horn 3 | 30 | 11 | -4.1 dB |
| Horn 4 | 36 | 27 | -1.8 dB |
| Bassoon 2 | 19 | 9 | -3.1 dB |

Horns 1-4 together: 54 of 92 repeats dip less than 3 dB.

- **Horns 3/4, bars 19-22 (p):** Horn 4 at 76/80/84/86 reads -0.7/-0.5/-2.3/-2.5 dB, so the four half notes still sound as one.
- **Bassoon 2, bar 82 (qn 324-327.5, ff):** seven repeated eighths with the basses' strokes and the timpani read -0.6..-2.1 dB. The note ends at 0.375 of 0.5 qn, which leaves 0.06 s at 126 bpm. The basses and the timpani articulate each eighth; the bassoon holds one long note.
- For comparison, the trumpets read -5.6..-7.2 dB and the trombones -3.8 dB.

**Measured: breaths** (`breath.py` and the 636 trace). Lowest 40 ms within -0.4..+0.15 s of the breath, against the level 0.3-0.6 s before it.

Horn breaths:

| Breath (qn) | Dip |
|---|---|
| Horn 1, 475 | -3.0 dB |
| Horn 4, 512 | -2.6 dB |
| Horn 3, 536 | -0.3 dB |

**Bar 160 (the movement's fff climax).** Every brass player has a printed breath at 636 (Trumpets 2 and Trombone 2 at 632). The c06 entry leads used up most of the caesura's 0.12 qn rest for the low brass:

| Track | Gap after the c06 leads | Dip at the breath |
|---|---|---|
| Trombone 1 | 0.056 qn | -0.7 dB |
| Bass trombone | 0.065 qn | -1.6 dB |
| Trumpet 3 | 0.02 qn | -2.5 dB |
| Trumpet 1 (control) | | -10.7 dB |
| Horn 1 (control) | | -6.4 dB |

Kit section 7 says the same: a loud horn breath needs a longer gap plus a fall.

Inferred: horn harmony and doubled pedals lose their pulse, and the low brass play straight through the breath that sets up the climax.

**Fix** (`tools/score_to_parts.py` note-length pass, the `WIND_REP_RETONGUE` branch and the breath branch; `--midi-only`).
1. **Per-family override.**
   - Horns (Solo French Horn tracks): `WIND_REP_RETONGUE_BY = {"horn": {"gap_s": 0.10, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}}`.
   - Short repeats (note of 0.5 qn or less at 100 bpm or faster, any wind or brass): `frac` 0.45 and `fall_cc` 8, so Bassoon 2's eighths sound at about half length, like the basses' `REP_SPLIT` strokes.
2. **Horn breaths.** Every horn breath at mf or louder gets a 10 CC fall over the note's last 0.2 qn: the default `BREATH_FALL_CC` for horn tracks, with the 0.3 qn gap unchanged.
3. **Bar 160.**
   - `BREATH_GAP_AT` {"Trombone 1": {632.0: 0.22}, "Bass trombone": {632.0: 0.22}, "Trumpet 3": {632.0: 0.22}}.
   - `BREATH_FALL_CC` 10 for the same three notes.
   - The 632 notes then end about 0.17 s before the beat, and the c06 entry leads stay.
   - Check the delivered 636 step (+2.6 dB now) and the limiter; a deeper breath before the beat should help the step.

**Pass criteria.**
- Median repeat dip 3.5-7 dB on Horns 1-4 and Bassoon 2.
- Horn 4 at 76-86: at least 3 dB.
- Bassoon 2 at 324-327.5: at least 4 dB on each eighth.
- Every horn breath at mf or louder, and Trombone 1, Bass trombone and Trumpet 3 at 636: dip at least 4 dB.
- Climax step and limiter no worse.

## 3. The brass slurred accents in the main theme's head (Horn 1, Trumpet 1, Trombone 1) are re-tongued on Sus: the slur breaks and the accent lands soft or bright

**Score.** The theme head `g8( es'4.->)` / `g8( f'4.->)` is in Horn 1 at qn 273 (bar 69) and 665/673 (bars 167-169), in Trumpet 1 at 665/673, and in Trombone 1 at 521/529 (bars 131-133). The eighth pickup is slurred to the accented dotted quarter, a leap of 8-10 semitones.

**Measured** (`slacc.py`, `head.py`, `head7.py`).
- These 7 notes are the only slurred accents in the movement that are not on a Leg row. The `GENTLE_ACCENT` brass branch has no `keep_legato`, so the accent plays Sus MAX / Sus Non Vib MAX after a 0.07 qn gap.
- Every woodwind and string slurred accent stays legato: 70 notes.
- Results per note:

  | Note | Accent minus pickup (first 0.25 s) | Other |
  |---|---|---|
  | Trumpet 1 665 | -0.6 dB | |
  | Trumpet 1 673 | +0.6 dB | |
  | Horn 1 273 | +1.7 dB | 2-5 kHz first 57 ms minus body +3.3 dB |
  | Horn 1 665 | +0.6 dB | 2-5 kHz first 57 ms minus body **+4.9 dB** (the brightest brass attacks in the movement) |
  | Horn 1 673 | +6.0 dB | |
  | Trombone 1 521 | +6.1 dB | first 120 ms 4.1 dB under its own body; reaches body only at +0.25 s |
  | Trombone 1 529 | +4.9 dB | first 120 ms 3.3 dB under its own body; reaches body only at +0.25 s |

- The same figure in Violins I reads +2.6 dB (median of 11) with no gap.

Inferred: the brass state the theme with a gap and a re-attack where the strings and winds slur. The accent is either bright (Horn 1) or late (Trombone 1), not a weighted arrival.

**Fix** (`build/score_config.py`).
- Set `GENTLE_ACCENT["brass"]["keep_legato"] = True`. The slurred accent then stays a Leg Slur MAX target with the normal legato lead and legato velocity, and takes only the 2.5 dB volume swell (the wind rule of mvt I c01).
- The c04/c06 holes on 8-9-semitone joins were portato joins (tenuto, 10 CC notch). These are plain legato joins, and Horn 1's 23 plain joins measure a median dip of 1.0 dB (worst 4.0).
- Fallback, for any of the 7 that dips 6 dB or more: keep it on Sus, but end the pickup at the accent's moved onset + 0.02 qn (no gap) and give the accent the 0.05 s brass entry lead.
- Do not use the `Leg Slur Accent MAX` row (Dan's item 8: accent samples bite).

**Pass criteria.**
- Accent minus pickup +2..+5 dB on all 7.
- 2-5 kHz first 80 ms minus body at or under 0 dB.
- Join dip under 6 dB.

## 4. Tremolo chord changes open 4-8 dB holes, and held tremolo pitches are re-attacked each bar (Violins II, bars 147-155 and 76-80; celli 117-121)

**Measured** (`tremj.py`). At each Tremolo-row chord change, the lowest 100 ms in -0.05..+0.8 s against the lower of the 0.4 s before and the body at +0.9..1.5 s. 10 of 41 changes dip 4 dB or more.

- **Violins II, "div. sul tasto" pp under the recapitulation's second theme (584-616):**
  - Dips at 592/596/600/604/608: -3.6/-7.0/-4.8/-7.7/-4.7 dB.
  - The trace at 596: -40.3 dB before, -45.7/-48.3/-45.2 dB at +0/+0.2/+0.4 s, -42.5 dB at +0.8 s. The old chord releases before the new tremolo reaches its body.
  - The stem is 8-13 dB under the master, which is quiet but exposed. The master dips -1.2..-2.3 dB at 596-608.
  - The top A5 is repeated untied in every chord (588-608), so the same pitch stops and restarts each bar.
- Other changes that dip:

  | Track | Changes |
  |---|---|
  | Violins II | 304 (-10.2 dB), 484 (-5.4) |
  | Violins I | 484 (-7.7), 664 (-5.2) |
  | Celli | 464/468 (-3.8/-4.7) |

Inferred: a soft tremolo background pulses once per bar. A real section changes chord within the tremolo.

**Fix** (generic, `tools/score_to_parts.py`; the Flautando mechanism of mvt II c16).
1. **Moving voices.** New `TREM_JOIN_TRACKS = ("Violins I", "Violins II", "Violas", "Violoncellos")`.
   - On consecutive Tremolo notes, the new chord's moving voices start `TREM_LEAD_S` = 0.3 s early.
   - The old chord's moving notes end at the new score onset + `TREM_OVERLAP_QN` = 0.4 qn. The Tremolo row is polyphonic, so the overlap is a crossfade.
2. **Held pitches.** A pitch present in both chords continues as one note with a 3 CC notch at the bar line, using the slurred-repeat merge path. This also covers the celli's five whole notes at 464-480 (c06 deferred `TREM_MERGE_AT`).

**Pass criteria.**
- All Tremolo chord changes dip 3 dB or less on the stem.
- No change in the stems' mean level over 584-619 of more than ±1 dB (tremj body).

## 5. Timpani strokes are all at one velocity, so pickups and offbeats hit as hard as downbeats (bars 27-30, 82, 131-134)

**Measured** (parts.json; stroke peaks on the stem):

| Passage | Velocity | Peaks |
|---|---|---|
| Bars 27-30 (104-119.5, ff) | v110 on every stroke | -24.8..-27.3 dB |
| Bar 82 (324-327.5, ff) | v110 | -23.9..-25.0 dB, flat |
| Bars 131-134 (520-535.5) | v110 | -25.3..-26.8 dB |

- In bars 27-30 the eighth pickups (105.5, 107.5, 117.5, 119.5) read -26.2..-27.3 dB, level with the downbeats they lead into (-26.5..-26.9).
- In bars 131-134 the offbeat eighths match the downbeats.
- Velocity does change the Flt Lng level: v110 -> v121 at pitch 43 measured +3.9 dB (108 against 124).

Inferred: the ff timpani rhythm sounds mechanical. A timpanist plays the pickup lighter than the beat it leads to, and lets the bar's strong beats carry.

**Fix** (`tools/score_to_parts.py`, the `METRIC_VEL` rule now used for pizzicato and harp; add the family "timp").
- Applies to Timpani Flt Lng strokes only, not rolls or accents.
- Velocity offsets:

  | Position | Velocity offset |
  |---|---|
  | Downbeat | 0 |
  | Beat 3 | -3 |
  | Beats 2 and 4 | -5 |
  | Offbeat eighths and pickups | -9 |

- Add a seeded ±2 jitter.
- This is about -3 dB on the pickups at the measured 0.35 dB per velocity step. Keep the c03 `TIMP_DELAY_S`.

**Pass criteria.**
- Pickups and offbeats 2-4 dB under the following downbeat.
- Downbeat peaks unchanged within 0.5 dB.

## 6. Smaller items (ranked)

- **A #5 test (Violins I eighths on Leg Slur MAX): keep it rather than revert.** Measured: on the 45 test eighths of 0.19-0.27 s, the crossover is +0.065 s, against Violins II on Sus MAX at +0.095 s. At the 17 onsets both sections play, the stem dips are equal: -4.8 against -4.5 dB median. The master dip is -2.1 dB, and only 4 of 45 reach -4 dB on the master. The extra stem dips are a property of these figures, not of the Leg row. Move only the worst three back to Sus MAX (259.5 -10.1 dB, 455.5 -9.5, 77.5 -8.3) with a per-onset exception.
- **Wind portato joins (open from c06), measured.**

  | Join | Dip |
  |---|---|
  | Flute 2, 279 | 10.2 dB |
  | Flute 1, 393 | 6.8 dB |
  | Oboe 1, 405 | 6.5 dB |

  The others are now under 6 dB. Use the c06 fallback (Sus MAX with a 0.05 s lead) on these three only. Velocity does nothing on Sus rows (c06), so give no velocity change.
- **Celli re-bow at 163.877, measured.** Dip -6.5 dB, level step -9.3 dB (stem 11 dB under the master); 37.377: dip -6.1, step +5.0; basses 166.01: -5.3 / -4.2. Refit these three with `fit_rebows.py` on c06.
- **a2 horns (`2FH KS Master`), deferred again in c06 for memory.** Still the right patch for the six Horn 1+2 a2 spans: 84 notes on one solo sample +3 dB, including the climax 628-643.5. The c06 render settled at 43 GB with 27 GB compressed, so first free memory by unloading unused mics on the four solo-horn tracks.

## Do not touch

- `GENTLE_ACCENT` articulations and swells (attacks measured above), and `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES` cuts.
- `ARRIVAL_WEIGHT_AT` 636/484.
- The slurred-repeat merges, `STR_SHORT_AFTER_SUS`, `REP_SPLIT`, and the strokes' velocity rule.
- `WIND_REP_RETONGUE` for woodwinds and trumpets: medians 4-7 dB.
- `AUTO_REBOW`, `space_rebows`, the fitted re-bow shapes, and the timpani re-strike plans.
- `TIMP_DELAY_S`, harp rolls and pitch velocities, the pizzicato rows, `PORT_TARGETS`, `META_DB`, and `PORTATO_JOIN_AT` Horn 1.
- `BREATH_SPLIT_AT` horn points, the crash and sus. cymbal timing, the pre-roll meter fix, and the climax order (160 > 122 > 169).

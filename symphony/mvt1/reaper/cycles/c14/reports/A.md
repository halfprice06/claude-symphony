# Cycle 14, critic A: articulation and phrasing (render c13)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c13 build after its stem fixes; note timing is identical to `cycles/c13/rendered_build/parts.json`), measured on the c13 stems and master (`cycles/c13/render/`), with patch tables read from the `.oib` files (`mockup-kit/opus/opus_state.load_oib`).

Scripts, 5 ms feature files and outputs are in `/private/tmp/claude-501/mockup-loop/mvt1-c14-A/`. The c13-A battery was rerun on c13 (`out_*.txt`). New scripts:
- `rrcyc.py`, `rrscan.py`: round-robin periodicity of repeated strokes.
- `sigh2.py`, `sigh3.py`: two-note slurs, second note against first.
- `seamscan.py`, `trace_l.py`: single loop-seam dips in long notes.
- `pick2.py`: accent over pickup, measured on moved onsets.
- `dbow.py`: breaks before repeated down-bows.
- `pz.py`, `pz2.py`, `pz3.py`: pizzicato attack shapes.
- `oibmin.py`, `ccall.py`, `cc1grp.py`: sample ranges and controllers in the patches.

## Checks that passed (measured)

- **Legato.**
  - No chord sits on a Leg row.
  - Join dips by track have medians of 1.6-2.6 dB on strings and -0.5-3.5 dB on winds and brass.
  - Joins of 6 dB or more: Violins I 2, Violins II 3, Violas 3, celli 5. These are the same joins as on c12.
- **Horns a2 (new 2FH track).** It legatos as well as the solo horn did, or better.
  - Crossovers in 272-286 / 664-676: median +0.03 s. c12 Horn 1 on the same notes: +0.07 s.
  - Join dips mostly 3-5 dB. Horn 1 on c12: 4-10 dB.
  - Brass 2-5 kHz first 80 ms minus body: median -8.2 dB, max +3.8 (Trumpet 1 676).
- **Re-bows (item 7).**
  - The master dips at the re-bows (median -1.96 dB) as much as at control times (-1.89 dB).
  - Final chord: autocorrelation at 3.95 s is under 0.2 in level, 100-300 Hz and centroid on the master and on every string stem.
  - The celli's -9.8 dB "step" at 163.877 is the printed sf > mf > pp decrescendo (CC11 114 -> 26), not a fault.
- **Accents.**
  - 2-5 kHz first 80 ms minus body: brass -8.2, winds -5.6, strings -4.4 dB (medians).
  - Every reading over +3 dB is a pickup's tail or a subito dynamic. Examples: Clarinet 1 558 is the eighth before it; Violas 536 is ff -> sub. mf.
  - Accent over pickup, measured from the moved onsets (`pick2.py`; LEARNINGS c13 says to measure legato targets this way):
    - 0 of 177 are 2 dB or more under their pickup.
    - The celli at 521/317 and Bassoon 1 521 now read -0.5 to +2 dB.
    - Only Flute 1 110 is left, at -2.3 dB (13.8 dB under the master).
- **Measured tremolo** (bars 117-121): celli fold on the sixteenth grid 4.0 dB. See #2 for its round robins.
- **Other articulations.**
  - Staccato separates 7.8-14.5 dB per track.
  - Breath marks dip 3.5-15 dB.
  - Tremolo joins: median -0.8 dB, 1 of 33 at 4 dB or more.
  - Repeated down-bows (bars 32, 72, 83) break 5-11.5 dB on the string stems.
  - Pizzicato reaches -3 dB of its peak in a median 0.05 s, for all velocities. The late "peaks" of c12-A's 40 ms windows were beating, not slow attacks.
  - Harp étouffez and timpani tie strokes are unchanged from c12.

## 1. Two-note slurs have no release: the second note is as loud as the first (about 60 slurred pairs, themes and answers throughout)

**Measured** (`sigh3.py`). The set is every two-note slur with both notes at least an eighth long and neither note accented or tenuto. Second-note body (moved onset +0.12 s to the next note's moved onset) minus first-note body, where the stem is within 15 dB of the master:

| Family | n (flat or falling plan) | Median, second minus first | Within 1 dB or louder |
|---|---|---|---|
| Strings | 15 | -0.3 dB | 67% |
| Winds | 11 | +0.5 dB | 73% |
| Brass | 10 | -0.2 dB | 70% |

"Flat or falling plan" means CC11 and the volume envelope are flat or falling between the two notes, so the differences come from the samples.

Exposed examples, second minus first:

| Track | Onset (bar) | Second minus first | Stem re master |
|---|---|---|---|
| Violins I | 69 (bar 18) | +2.2 dB | -1.9 dB |
| Violins I | 61 (bar 16) | +0.5 | -2.2 |
| Violins I | 141 (bar 36) | +2.8 | -5.8 |
| Trumpet 1 | 669 (bar 168, coda theme) | +5.3 | -6.1 |
| Clarinet 1 | 374 (bar 94) | +3.4 | |
| Clarinet 1 | 413 (bar 104) | +3.5 | |
| Flute 1 | 109 (bar 28) | +2.6 | |

Most are the figures `b8( c'8)`, `d'8( c'8)`, `cis''8( d''8)` of the first theme and its development (`sections/recOne.ily` 29-47, `dev.ily` 58-99, `coda.ily` 23/121-129).

Every rule so far shapes the first note of a slur or the joins. Nothing shapes how a slur ends.

**Inferred.** Players lean on the first note of a slurred pair and lift the second (the bow or breath releases). Played level, the theme's "sigh" figures and the lead-ins to its accented dotted quarters sound flat and keyboard-like. This is the most widespread phrasing gap left in the render.

**Fix:** a new generic rule in `tools/score_to_parts.py`, with defaults set in `build/score_config.py`:

`SLUR_PAIR_RELEASE = {"db": -2.5, "from_s": 0.10, "full_s": 0.20, "max_qn": 1.0}`

Scope:
- Applies to a slur of exactly two notes whose second note is at most `max_qn` long and is not accented, tenuto or sf.
- Skip pairs where the printed dynamic curve rises between the two onsets (a crescendo) and pairs whose second note is a hairpin's target.

Level shape on the second note:
- 0 dB at its moved onset + `from_s`, starting after the legato sag (LEARNINGS section 6: never cut at a target's moved onset).
- `db` at + `full_s`.
- Held to the note's end and back to 0 at the next note's moved onset.
- Write it as exact `LEVEL_SHAPES` points, as for the c13 pickup cuts, and apply it once per onset when sections are divided.

Do not change note ends: a slur's last note already ends 0.05 qn early before a new slur.

Refit afterwards: the accent fits whose neighbours include these notes (`tools/fit_accents.py --keep-long-qn 1.4 --pickup-over 2.5`, all families).

**Pass:**
- On the flat-plan set, median second minus first between -1.5 and -3.5 dB per family, with under 30% at -1 dB or louder.
- Join dips at these pairs no more than 1 dB deeper than c13.
- No accent-over-neighbour fit moves out of 2-4 dB.

## 2. The celli's measured tremolo repeats a 9-stroke round-robin pattern (bars 117-121, 80 strokes)

**Measured** (`rrcyc.py`, `rrscan.py`). The c13 `MEAS_TREM` strokes (G2, `Stac RRx9`, v96, 0.119 s apart, 464-484) cycle through the row's nine takes in a fixed order.

Autocorrelation of the per-stroke values after detrending, by lag in strokes:

| Value | Lag 9 | Lag 18 | Lags 1-8 |
|---|---|---|---|
| Peak level | 0.71 | 0.74 | -0.34 to +0.25 |
| 1-8 kHz share | 0.82 | 0.84 | |
| Centroid | 0.93 | 0.90 | |

The cycle by position (mean over 9 cycles):
- The 5th take is 4.2 dB weaker and 4.9 dB brighter (1-8 kHz share).
- Takes 6-9 are darker (centroid 134-144 Hz against 164-199 Hz).
- The same 9-stroke shape returns every 1.07 s, nine times.
- Celli are 14.8 dB under the master there.

No other run in the movement repeats this way:
- the bars 129-130 written-out figures (28 strokes) give 0.04 / 0.51;
- every other RR run is shorter or changes pitch.

**Inferred.** A section of celli playing measured sixteenths never repeats one 9-note pattern exactly. The regular weak and bright stroke every 1.07 s, drifting against the half-bar (8 strokes), makes the motor sound mechanical, like a loop under the build to bar 122. This is a new artefact from c13's (correct) change to strokes.

**Fix** (deterministic, HO manual CC table: CC36 Round Robin Reset, any value 1-127 triggers a reset to the first take):
1. Add `MEAS_TREM["rr_runs"] = [7, 5, 8, 6, 4, 9, 5, 7, 6, 8, 4, 7, 5, 9]`, used cyclically.
2. In `tools/score_to_parts.py`, where `MEAS_TREM` expands a note into strokes, emit a CC36 point (value 127) 0.02 qn before the first stroke of each run. Store it in a new `cc36` lane in parts.json.
3. In `tools/build_reaper.py`, write the `cc36` lane like `cc15`/`cc70`. It sits beside the pre-roll reset at `RR_RESET_QN`, which stays.

Runs of 4-9 make the cycle aperiodic. The weak, bright 5th take then appears only in runs of 5 or more, at irregular places. No new row is loaded, so this is a MIDI-only change for the celli.

**Pass:**
- Celli 464-484 stroke autocorrelation under 0.3 at lag 9 and under 0.4 at every lag 4-18, for peak, 1-8 kHz share and centroid.
- Sixteenth-grid fold 3.5 dB or more (c13 4.0).
- Level per bar within ±1 dB of c13.
- Master 464-484 within ±0.3 dB.

## 3. Tongued brass eighths are still as smooth as slurs (80 changes in the ff tutti themes, bars 69-72, 98-102, 131-134, 167-170)

**Measured** (`detw2.py` on c13, holes by gap):

| Gap | n | Hole median |
|---|---|---|
| Under 0.06 s | 41 | -3.1 dB |
| 0.06-0.08 s | 39 | -3.5 dB |
| 0.08-0.095 s | 254 | -5.1 dB |
| Over 0.095 s | 25 | -7.0 dB |
| Slurred | 151 | -3.6 dB |

- The short-gap changes are on Horns a2 22, Trombone 1 20, Trumpet 1 13, Horn 1/2 15, Horn 3 4.
- c13's frac 0.30 test did not deepen them (LEARNINGS c13).
- Winds pass: tongued -5.4 against slurred -4.1 dB.

**Inferred.** The tutti themes' unslurred brass eighths run together, so the brass rhythm of these themes is heard only through the strings.

**Fix:**
1. Revert `WIND_DETACH["by"]["brass"]` to `{"gap_s": 0.09, "frac": 0.18}`.
2. Give the `WIND_DETACH` branch of `tools/score_to_parts.py` (the `elif WIND_DETACH and family in ("wind", "brass")` block, about line 1861) the same CC11 fall as `WIND_REP_RETONGUE`:
   ```python
   if wd_.get("fall_cc"):
       fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], wd_["fall_s"]))
       cc_falls.append((fa_, n["end"], wd_["fall_cc"], max(0.01, e0 - n["end"])))
   ```
   Apply it only when the note is 0.6 qn or shorter.
3. Set brass `"fall_cc": 10, "fall_s": 0.10`. On the Hollywood Brass KS Masters CC11 drives only the Global Group volume (c09), so the fall changes level, not the dynamic layer. The c07 horn repeats gained about 2 dB from a 12 CC / 0.15 s fall.
4. Refit brass accents afterwards.

**Pass:**
- Brass tongued changes with gaps under 0.08 s at -5.0 dB or deeper.
- Slurred unchanged within ±0.3 dB.
- Master dips at the tutti changes in 272-286, 391-408, 520-534 and 664-676 no more than 1 dB deeper than c13.

## 4. Horn 4's pp pedal in bar 73 has a 10 dB loop-seam hole (289-304)

**Measured** (`seamscan.py`, `trace_l.py`). Horn 4's tied A-flat3 pp (moved start 288.79, 7.24 s, Sus MAX) has a hole at +4.5-5.1 s after the moved start:
- level falls to -10.0 dB at +4.80 s (relative to +3-4 s), 100-300 Hz to -12.2 dB;
- the centroid flicks from 315 to 450 Hz;
- the note then settles 3.5 dB lower.

CC11 and the volume envelope are flat or rising there (CC11 36-38, +1.0..+1.5 dB ramp). Horn 4 is 12.1 dB under the master and the master dips 1.8 dB. No other wind or brass note over 3 s has a single dip over 6 dB within 18 dB of the master. The scan's other hits are bassoon crescendo wobble at 36 (-6.7) and string re-bow pieces already fitted.

**Inferred.** A soft horn pedal that drops out for half a second in a quiet bar (mix -32.7 dB) is heard as a hiccup in the held chord.

**Fix:** `build/loop_fills.json`: `"Horn 4": {"289.0": [[4.78, 7.0, 0.5]]}`. That is seconds after the moved start, dB, and full width. The width follows the -5 dB span of the dip (kit c10: size it to the dip).

**Pass:**
- Dip under 4 dB.
- No bump over +2 dB within ±0.5 s.

## 5. Revert the c13 articulation tests as planned (measured on c13)

- **Double basses `ART_SPANS` Detache 104-124.** Eighth-grid fold 1.3 dB against 1.1 on Sus MAX, and 1-2 dB quieter. Revert it; this is a full rebuild of the Double basses, since the row is loaded only for it. With Marc Shrt (c03) also failed, keep the basses' repeated eighths on Sus MAX. Their motor comes from the timpani and the upper strings.
- **Brass `WIND_DETACH` frac 0.30:** see #3.
- **Suspended cymbal key 65:** back to key 64, `lead_s` 0.25.

## 6. Smaller items

- **Flute 1 110** (bar 28): the only accent still under its pickup on moved onsets (-2.3 dB, 13.8 under the master). A pickup cut like c13's: `LEVEL_SHAPES["Flute 1"]` -2.5 dB from the pickup's moved onset to the accent's.
- **More a2 patches.** These are the next real patch upgrades, but memory blocks them (c13: 45 GB with 33 instances; each two-row instance is about 1 GB). They become possible only if a slot is freed.
  - Trumpets 1-2 unison (dropped as unisons): the coda theme 664.5-676 and the recap head 520-524. `2 Trumpets/06 Keyswitch/2TP KS Master.oib` exists.
  - Trombones 1-2 unison: 464-480 and 520.5-534 (`2 Trombones EXP/04 Keyswitch/2TB KS Master.oib`).
  - Horns 3-4 a2, bars 80-81 (316.5-324). This one needs no new instance: the existing Horns a2 track is free there. It needs `TRACK_WINDOWS` to take notes from the Hn3 staff in that window.
- **Bass trombone.** Its C2-D-flat2 notes (3 notes) are stretched from E2 samples on the Solo Trombone p/mp/f layers; only the ff layer has pedal samples. Its other 96% of notes are inside the sampled range. No action.

Do not touch:
- the Horns a2 track, its windows and per-window roles;
- `MEAS_TREM` itself (only add the RR resets);
- `REP_SPLIT` strokes;
- `TREM_JOIN`/`TREM_SPLIT` for the upper strings;
- `WIND_DETACH` for winds;
- `GENTLE_ACCENT` with `swell_s_leg`;
- the c13 pickup `LEVEL_SHAPES`;
- `accent_fits.json` (refit only after #1/#3);
- `_REBOW_FROZEN`/`REBOW_AT` with `rebow_fills.json` and `NOTCH_SKIP`;
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB` and the re-strike plans;
- `PORTATO_JOIN_AT`;
- `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`;
- `ROW_TRIM_DB`;
- harp `env_release_ms` 200 with `HARP_RING_S`;
- the pizz., staccato and tremolo rows;
- the fermata-679 release;
- the climax order (160 > 122 > 169);
- the sus. cymbal timing (key 64).

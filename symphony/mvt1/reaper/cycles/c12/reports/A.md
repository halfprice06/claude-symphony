# Cycle 12, critic A: articulation and phrasing (render c11)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c11 build after its stem fix, which is what `cycles/c11/render/` carries), measured on the c11 stems and master, plus the layer and controller tables of every patch in use, read from the `.oib` files with `opus_state.load_oib`.

Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c12-A/`:
- The c11-A battery, rerun on c11: `joins`, `tremj`, `rebow`, `rbctl`, `longloop`, `breath`, `hrep`, `stacsep`, `ten2`, `ties`, `timp`, `harp`, `pizz`, `arco`, `headfig`, `solo`, `susbloom`.
- New scripts:
  - `integ.py` / `integ2.py`: chords on Leg rows, and keyswitches sent while a note sounds.
  - `slaud.py`: slurred notes on non-legato rows.
  - `slurc.py` / `detw2.py` / `detw3.py`: slurred against tongued note changes.
  - `rbiso.py`: the re-bow dip with the re-bowing stem taken out of the master.
  - `final.py`: the loop on the final chord.
  - `timpl.py` / `timpcr.py`: timpani brightness by articulation and dynamic.
  - `cc1scan.py` / `cc1bc.py` / `rowcc.py`: the CC1/CC11 layer tables per patch row.
  - `ten2.py` / `tenm.py`: tenuto weight.
  - `dev98.py`, `solojoin.py`, `cae.py`.
- `tools/fit_accents.py` ran without `--write`, scratch in `fa/` (`fa_*.txt`). It swaps `build/accent_fits.json` out and back in during a run. The content was restored unchanged; only the file's mtime moved.

## Checks that passed (measured)

- **Accents (Dan's item 8).**
  - Predicted from c11: brass 33 of 37 in 2-4 dB over their neighbours (median +2.99), strings 116/135, winds 124/140.
  - 2-5 kHz in the first 80 ms exceeds the note body by more than 3 dB only on the known window artefacts (Violas 120/536, Bassoon 1 536).
  - No accent has bite.
- **Re-bows (Dan's item 7).**
  - The master's dip at the 92 re-bows has a median of -1.95 dB (p10 -3.83). At control times it is -2.01 (p10 -4.10).
  - Every master dip deeper than -4 dB comes from the rest of the orchestra, not from the re-bowing section. With that stem taken out of the master, the dip stays as deep or gets deeper (Vc 289.145: -5.5 master, -6.2 without the celli; Vln II 189.62: -5.1 / -5.4).
  - The Vc 163.877 "step" (-6.7 dB) is the printed sf > mf > pp on three unslurred whole notes, not a seam.
  - Final chord (qn 720.5-727.5): autocorrelation at 3.95 s is under 0.2 in level, 100-300 Hz and centroid on the master and on every string stem. Horn 3 is +0.28/+0.33 (100-300 Hz/centroid).
  - No other held note of 9 s or more loops above 0.5.
- **Legato integrity.**
  - No chord sits on a monophonic Leg row.
  - Of 1078 slurred non-first notes, only Fl1 393, Ob1 405 and Hn1 413 are re-tongued: wide-leap portato tenutos, as chosen in c06/c07.
  - The 54 keyswitches sent while a note still sounds all fall 0.06 qn before an abutting next note.
- **Other articulations.**
  - Tremolo joins: median -0.8 dB (1 of 35 at 4 dB or more).
  - Staccato separates 4.5-21 dB per note.
  - Pizzicato decays a median of 11 dB by +0.4 s.
  - Breath marks dip 3.5-15 dB.
  - Harp étouffez at 244/650/654 falls 15-25 dB in 0.25-0.5 s.
  - Timpani tie strokes are present.
  - Second-theme tenutos: master first 0.35 s against the quarter is -0.6 / -2.9 / -0.5 / +2.0 / -0.3 dB at 189/201/589/601/685. This is the c11 fix, kept.

## 1. Every timpani roll plays one sample layer: the Rls row has 8 dynamic layers on CC1, and the timpani track gets no CC1 (all rolls, bars 1-4, 11, 39-42, 61-63, 70, 75, 79-81, 114-126, 129-130, 139-140, 143-145, 157-160, 166-170, 173, 179-182)

**Measured, from the patch.** In `Timpani Flt KS.oib` the "Timpani Flt Rls" row has eight sample groups, V1-V8:
- Every region covers velocity 1-127.
- Each group's Source volume is driven by a cc 1 MidiController through a crossfade table: V1 full at CC1 0-9, V2 23-26, V3 38-41, V4 54-58, V5 71-73, V6 86-90, V7 102-105, V8 118-127. Neighbours overlap.
- The Lng/Sht stroke groups have no CC1 controller: strokes are velocity-layered.

`tools/score_to_parts.py` (timp branch, about line 2546) sets `cc11, cc1 = [], []`, and parts.json Timpani has an empty `cc1` lane. Velocity, roll_db (CC7) and the volume envelope are the only dynamics a roll gets.

**Measured, on the stem** (`timpl.py`, `timpcr.py`; 1-8 kHz share of the roll body, and 2-5 kHz share):

| | 1-8 kHz share | 2-5 kHz share |
|---|---|---|
| Strokes, pp (v62, qn 712-717) | -33..-40 dB | -48..-54 |
| Strokes, ff (v121, 564/676) | -13.8 | -22..-24 |
| Rolls, ppp (opening, qn 2.5-14, v29) | -14.9 | -25.4 |
| Roll, pp (40) | -11.5 | -20.9 |
| Roll, mf (456) | -12.2 | |
| Roll, ff (560) | -11.5 | |
| Roll, fff (636) | -12.3 | -21.7 |

- Strokes spread 20 dB in brightness from pp to ff. Rolls from ppp to fff spread only 4.8 dB, in no order by dynamic.
- Crescendo rolls get louder without getting brighter:
  - 40-44 pp < f: +15 dB level, share -11.6 -> -11.3.
  - 156-160 pp < ff: +15 dB, -13.8 -> -14.0.
  - 632-636 < fff: +5 dB, -13.4 -> -12.8.

**Inferred.** The movement opens on a ppp roll that has the colour of a loud roll turned down: hard and close rather than a soft felt rumble. The printed crescendo rolls into the climaxes (bars 11, 40, 121, 159) only get louder. This probably explains the kit's notes that a roll is "about 14 dB louder than single strokes at the same CC7" and that soft rolls needed large cuts (section 10).

Which layer actually sounds is not established:
- The group states store `value` 23 (V1) and 119 (V8) and 0 for the rest.
- The brightness, at or above the ff strokes, points to V8 or a loud layer.

**Fix:**
1. `tools/score_to_parts.py`, timp branch:
   - Keep `cc11 = []`.
   - Write a CC1 lane from the printed dynamic curve, the same way `cc1_fn0` does for `CC1_DYN_TRACKS`: `value_at(TIMP_CC1_MAP, base(q))` sampled on a 0.125 qn grid over each roll, including its hairpins.
   - Set the value 0.02 qn before each roll onset, with the first value in the pre-roll.
   - New generic table: `TIMP_CC1_MAP = [(22, 5), (34, 24), (46, 40), (58, 56), (72, 72), (88, 88), (114, 104), (124, 122)]`. These are the layer centres read from the .oib, ppp..fff.
   - Strokes are unaffected.
2. Levels:
   - The soft layers are quieter in themselves. Render once, measure every roll's body level against c11 per printed dynamic, then retune `roll_db` (the CC7 table) or a Timpani `soft_trim_db` / `dyn_trim_db` in mix.json, so each dynamic keeps its c11 level. This is the c09 brass method; apply it by stem fix.
   - The layers now carry part of each hairpin's growth, so re-measure crescendo growth and lower `TIMP_HP_DB_FACTOR` (1.0) if rolls overshoot.
   - Keep the `TIMP_ROLL_RESTRIKE` plans. There are no timpani `loop_profiles` left to refit. Recheck the roll loop autocorrelation, because the new layers have their own loops.

**Pass:**
- The roll 1-8 kHz share rises with the printed dynamic, with a spread of 8 dB or more from ppp to fff.
- The crescendo rolls at 40, 156, 480 and 632 brighten by 3 dB or more across their hairpins.
- Per-dynamic roll levels are within ±1.5 dB of c11 after the trim.
- The roll centroid autocorrelation at the loop period is no higher than c11 (0.06-0.46).
- A long roll is never the loudest stem unless the timpani lead (rule 5).

## 2. Tongued wind and brass notes join as smoothly as slurred ones: unslurred note changes have no tonguing gap (640 changes, all families; most exposed at bars 28-31, 98-102, 158-161)

**Measured** (`detw2.py`, `detw3.py`). Different-pitch adjacent notes with the stem within 18 dB of the master. The hole is the lowest 20 ms window at the change, against the louder of the two bodies.

| Family | Class | n | Hole median (p25) |
|---|---|---|---|
| Brass | unslurred, abutting | 300 | -3.0 (-4.6) dB |
| Brass | slurred | 150 | -3.3 (-5.0) |
| Brass | unslurred with the 0.033 s gap that accents and some notes already get | 66 | -4.0 (-7.1) |
| Winds | unslurred, abutting | 340 | -3.6 (-5.1) |
| Winds | slurred | 381 | -4.2 (-5.7) |
| Winds | unslurred with a gap | 158 | -6.1 (-9.6) |

- The 2-5 kHz rise at the change is no higher on tongued notes than on slurred ones (wind -1.0 vs -0.8, brass -1.2 vs -0.2).
- Most affected tracks: Bassoon 1 62 changes, Clarinet 1 60, Bassoon 2 60, Horn 1 53, Horn 3 53, Trombone 1 39, Flute 1 37, Trumpet 1 28.
- Most affected passages:
  - The ff unslurred eighth figures of bars 98-102: Bn1 391-408 (14 changes, hole -3.2), Tbn1 391-407.5 (13, -2.8), Hn1 391-404 (10, -2.3).
  - The brass of bars 28-31 (108-124).
  - The climax brass of bars 158-161 (628-644).

**Cause** (`tools/score_to_parts.py`, the note-end pass at about lines 1735-1830): an unslurred, unaccented, untenuto Sus note into a new pitch matches no branch and keeps its written end. c11's `ABUT_LEAD` then ends it at the next note's moved onset. So tongued lines play as overlapping Sus crossfades, about as smooth as the slurs next to them.

**Inferred.** Dan's item 1 (slurs audible as printed) needs contrast. When tongued and slurred lines sound alike, the printed slurs disappear in the winds and brass.

**Fix** (generic, `tools/score_to_parts.py`): a new rule `WIND_DETACH = {"gap_s": 0.05, "frac": 0.12}`. Place it as a branch before the final `elif is_leg:`.
- Condition: family is wind or brass, not legato, not the same pitch, not in the same slur as the next note, and the next onset within 0.01 qn of the written end.
- Effect: `n["end"] = e0 - min(e0 - qn_before(e0, gap_s), frac * dur)`.
- The earlier sostenuto/Largamente, tenuto and accent branches keep precedence.
- Where `ABUT_LEAD` moves the next onset, end the old note `gap_s` before the moved onset rather than at it: never extend an end that this rule shortened.

**Pass** (rerun `detw2.py` with `CYC=c12`):
- Unslurred-abutting holes are at least 1.5 dB deeper than slurred in the same family: wind about -5.7 or deeper, brass about -4.8 or deeper.
- Slurred joins are unchanged within ±0.3 dB.
- The c11 C #4 crossover medians (Horn 1 +0.040, Trumpet 1 +0.018, Oboe 1 +0.022 s, ...) move by 0.02 s or less.
- At the tutti chord changes in 108-124, 391-408 and 628-644, master dips are no more than 2 dB deeper than c11.
- Refit accents for brass and winds (`fit_accents.py --keep-long-qn 1.4`), because their neighbours change.

## 3. Tenuto phrase tops sit 2-6 dB under the note before them (bars 104, 108-110, 148, 51, 108; Horn 1, Violas, Flute 1, Bassoon 1, celli)

**Measured** (`ten2.py`, `tenm.py`; body = +0.1..+0.5 s, pre = -0.3..-0.05 s). A tenuto asks for full length with weight. Twelve of the 41 printed tenutos have a body under the note before:
- **Horn 1 413** (bar 104, B♭4 after D4, slurred, re-tongued on Sus MAX v73): **-5.1 dB**. The line Horn 1 + Bassoon 1 + celli (all tenuto there) sits at -2.0, and the master at -1.9.
- **Violas 436** (bar 110, with Flute 1 "1. espr."): Violas **-5.6**, Flute 1 **-3.2**, the pair -4.1. They lead at -6 dB re master.
- **Violas 589** (bar 148): -4.4, first 0.35 s -3.7 against the quarter (`headfig.py`).
- **Violas 429:** -2.4.
- **Horn 1 / celli 201:** -2.1 / -1.5; the line -1.7, the master -2.6.
- **Bassoon 1 413:** -1.9.
- **Oboe 1 400 / 405:** -3.6 / -1.9.
- **Violins I 393:** -2.0.

The development tutti tenutos at 393-405 are fine as a group: the melody group sum dips at most 2 dB and its body is +0.7..+3.7, because the sections dip at different times. Leave those.

**Cause.**
- The tops of these leaps (5-8 semitones up) fall on samples about 0.1 dB per semitone quieter at one CC11 (loop LEARNINGS c04), plus the join sag.
- No trim acts on these notes. `note_trims.json` has none at Horn 1 413, Violas 436/589, Flute 1 436 or Bassoon 1 413. The trims at Horn 1 189/201 and Violas 601 are bloom cuts.

**Fix** (level only, so it can be stem-fixed):
1. `build/note_trims.json`:
   - Horn 1 `"413.0"` +5.0
   - Violas `"436.0"` +5.0 and `"589.0"` +4.0
   - Flute 1 `"436.0"` +3.0
   - Bassoon 1 `"413.0"` +2.0
   - Violas `"429.0"` 3 -> 5.0
2. `build/score_config.py`: `NOTE_TRIM_RAMP_S` 0.1 for these onsets, so the trim is a step at the moved onset held through the note.
3. Leave Horn 1 413 on Sus: portato joins over 8-9 semitones left 10-12 dB holes (loop LEARNINGS c04/c06).

**Pass:**
- Each listed tenuto's body is 0 to +3 dB over the note before on its stem.
- No 30 ms spike over +3 dB at the onset.
- Lines 413 and 436 at 0 dB or more over the note before on the group sum.

## 4. The a2 doublings are still one solo sample, and a recorded two-player patch is on disk (Horns 1-2 bars 69-72, 96-101, 116-121, 157-161, 166-170; Trumpets 1-2 bars 167-170; Trombones 1-2 bars 131-134)

**Measured.**
- `find_unisons` drops 88 of Horn 2's 189 notes and plays Horn 1 +3 dB on `1FH KS Master`.
- Kit section 8: an identical-patch unison is one coherent sample, about one louder horn.
- In the a2 theme statements the kept stem leads at -8.7..-10.8 dB re master:
  - Horn 1 272.5-286: -10.0
  - Horn 1 628-643.5: -10.8
  - Horn 1 662-676: -9.1
  - Trumpet 1 664.5-676: -8.7
  - Trombone 1 520.5-534: -10.4
- Printed "a2": Hn2 310.5 (text) and the Tpt 1-2 coda theme.
- On disk: `Hollywood Brass Opus Instruments/2 French Horns/06 Keyswitch/2FH KS Master.oib`, `2 Trumpets/06 Keyswitch/2TP KS Master.oib`, `2 Trombones EXP/04 Keyswitch/2TB KS Master.oib`.

**Inferred.** The ff themes at the closing, the climax and the coda sound like one strong player. A pair sounds wider, with the slight pitch and timing spread that a unison sample cannot give.

**Fix:** the c11-A #6 plan, in a cycle with no other build change.
1. Free a slot. The Tam-tam (key 36; 484-505, 696) and Crash cymbals (key 60; 636) never overlap. Put them in one Opus instance as two instrument zones, each keeping its mixer, mics, seat, `LEVEL_SHAPES`, roles and the tam-tam `_damp`.
2. Load `2FH KS Master` on the freed track (`TRACK_WINDOWS` with the a2 windows). Its gain is the solo-horn track's +4.6 dB (kit c18), without the +3 dB unison boost.
3. Measure the a2 level per window (±1 dB of c11) and REAPER memory (one two-row instance is about 1 GB; c11 settled at 43 GB).

If that works, the same recipe covers 2TP for the coda trumpets.

## 5. Smaller items (measured)

- **Repeats still sounding tied** (`hrep.py`):
  - Trombone 1 at 122 / 456 / 492 / 564: -2.9 / +0.2 / -2.2 / -1.1 dB, at a 0.06 s gap.
  - Horns 3/4 in the final chord, 722.3 / 721.6: -2.8 / +1.1, at a 0.06 s gap.
  - Fix: `WIND_REP_RETONGUE_BY["Trombone"] = {"gap_s": 0.08, "fall_cc": 10}`, and the final-chord horn repeats at the horns' 0.10 s.
- **Accents far over their neighbours with no fit possible** (fit 0, protected long or slurred-legato accents):
  - Violins I 477: +8.9 dB
  - Clarinet 1 105: +8.6
  - Bassoon 1 382: +8.2
  - Flute 1 156: +8.1
  - Clarinet 1 273: +7.7
  - Oboe 1 113: +7.4

  The neighbours are short pickup eighths, so this reads a long note against short ones more than an accent. 2-5 kHz is under the body in all six. Look at them by ear before changing anything.
- **Bass clarinet:** checked and correct. The BC KS Master crossfades its p/mp/f layers on CC11 (the Clarinet KS Master uses CC1), so leaving it out of `CC1_DYN_TRACKS` is right.

Do not touch:
- `accent_fits.json` and GENTLE_ACCENT for all three families (refit after #2, with `--keep-long-qn 1.4` and `--pickup-qn`).
- `_REBOW_FROZEN` / `REBOW_AT`, `space_rebows` rows, `rebow_fills.json` and `NOTCH_SKIP`: the master cannot tell re-bows from control times.
- The c10/c11 second-theme fills and tenuto trims at 189/191/201/589/591/601/685.
- `PORTATO_JOIN_AT`, `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`, `TREM_JOIN` / `TREM_SPLIT` / `TREM_ENTRY_LEAD_S`, `REP_SPLIT`, `STR_SHORT_AFTER_SUS`, `ROW_TRIM_DB`.
- `WIND_REP_RETONGUE`, breath gaps, `BREATH_SPLIT_AT`.
- Harp `env_release_ms` 200 with `HARP_RING_S`.
- The pizzicato and staccato rows.
- `TIMP_ROLL_RESTRIKE` plans, `TIMP_DELAY_S` and the cymbal timing.
- `CC1_DYN_MAP` with the c09 CC1-track trims.
- The `ABUT_LEAD` leads (only their old-note end changes under #2).
- The climax order (160 > 122 > 169).

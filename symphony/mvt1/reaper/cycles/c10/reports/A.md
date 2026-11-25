# Cycle 10, critic A: articulation and phrasing (render c09)

Scope: every wind, brass, string, timpani, percussion and harp note in `build/parts.json` (the c09 build after its four stem fixes; it is what `cycles/c09/render/` carries), measured on the c09 stems and master. Scripts and 5 ms feature files: `/private/tmp/claude-501/mockup-loop/mvt1-c10-A/`. These are the c09-A scripts rerun on c09 (`joins.py`, `tremj.py`, `rebow.py`, `longloop.py`, `breath.py`, `hrep.py`, `stacsep.py`, `ten2.py`, `susbloom.py`, `ties.py`, `timp.py`, `hp.py`, `hp2.py`, `harp.py`, `chordleg2.py`, and `accfam.py`, which is `fit_accents.py` in measure-only mode). New scripts: `fig.py` (the second-theme figure), `beats.py` (levels per beat), `rbnotch.py` (re-bows next to CC11 notches), `seam.py` / `seam2.py` (dips inside single string notes), `crescrev.py`. Nothing under `build/` or `tools/` was written. `tools/fit_rebows.py` was run without `--write`, to read its summary only.

## Checks that passed (measured)

- **Accents, Dan's item 8.** Accents over their same-dynamic neighbours are in 2-4 dB on most notes:
  - brass 29 of 36 (median +3.0);
  - strings 107 of 138 (+3.05);
  - winds 102 of 146 (+3.05).

  2-5 kHz first 80 ms minus body is a median -13.8 / -10.0 / -11.8 dB for brass / strings / winds. Only five readings are positive: Horn 1 273 (+2.4), Violas 536/120, Bassoon 1 536 and Clarinet 1 120. All are slur-pickup or window artefacts. The c09 Violins I theme heads (57/65/113/479, now Sus strokes) are inside 2-4 dB.
- **Legato.** No chord or simultaneous note on any Leg row (`chordleg2.py`), and no keyswitch later than its note. Join dips have a median of 0.3-3.9 dB per track. The few joins of 6 dB or more are listed in item 6.
- **Tremolo.** The c09 entry leads hold: Violins II 304, Violins I 664, celli 464 and Violins I/II 484 no longer open with a hole (stem level steady within 3 dB through the change). 34 other changes dip a median 0.8 dB.
- **Other articulations.**
  - Staccato separates 5-19 dB per note.
  - Ties re-attack only at the planned timpani strokes and the basses' "change bow at will".
  - Breaths dip 4-19 dB everywhere.
  - Repeats on Horn 1-3 and Bassoon 2 dip a median 4.1-6.6 dB.
  - Timpani off-beats sit 2-12 dB under the next downbeat.
- **Dan's item 7.** No note of 9 s or more loops above 0.6 at the 2.8-4.3 s lag in level, 100-300 Hz or centroid. String re-bow dips are a median 1.2-3.6 dB per section and 1.5-2.4 dB on the master. The final ppp chord's master holds within ±0.7 dB over qn 724-727.

## 1. The second theme's head figure still collapses on the quarter and surges on the tenuto (Horn 1, celli, violas; bars 48, 51, 148, 151, 172)

**Measured** (`fig.py`; windows: eighth = its onset +0.05..+0.45 qn, quarter = the quarter's middle, tenuto peak = the highest 0.25 qn window in its first 1.8 qn):

| Track, tenuto at qn | Quarter minus eighth | Tenuto peak minus quarter | Master: quarter beat minus beat before / tenuto peak minus quarter beat |
|---|---|---|---|
| Horn 1, 189 (bar 48) | **-6.3** (stem -36.5 -> -46.5 at 188.4) | **+14.6** (-31.1 at 190.3) | -1.8 / **+6.3** |
| Horn 1, 589 (bar 148) | **-6.7** | **+12.5** | -2.4 / **+6.5** |
| Horn 1, 201 / 601 (bars 51, 151) | -1.4 / -3.0 | +9.4 / +7.3 | +1.7 / +3.9; -0.5 / +6.4 |
| Violoncellos, 589 / 601 / 685 | -3.9 / +2.9 / **-5.6** | **+12.0 / +11.2 / +9.2** | 685: -3.4 / +6.1 |
| Violas, 601 | -0.2 | +8.3 | |

The c09 rules worked as written: the short `>` now moves CC11 only 81 -> 75, and the portato notch is 4 CC. Even so, the stem of the melody (Horn 1) falls 10 dB for the whole quarter and then rises 15 dB to the middle of the tenuto. The c09 CHANGES note "pass not reached" for this.

The trace at 189 shows where the change comes from:
- The quarter (A♭3, Leg Slur MAX v124) is low for its full 0.53 s, not only in a 0.15-0.4 s transition.
- The tenuto F4 (Leg Slur MAX v100) starts at -41 dB and then blooms 10 dB between +0.45 and +0.75 s.
- Over the same span CC11 moves only 76 -> 79 and the volume envelope +0.5 -> +1.2 dB. The bloom is in the sample, not in the plan.

**Inferred.** The printed shape is a `<` over the tenuto half note, at p dolce. The listener hears a melody that drops out for one note and then swells about 6 dB on the master within one beat. It happens at all five statements of the theme head. This is the most exposed tune of the movement after the first theme.

**Fix** (level only: can be stem-fixed with `tools/stem_fix.py` and rendered next cycle):
1. `build/early_fills.json`, quarter fills held through the quarter (`pre_s` 0.10, `hold_s` 0.40):
   - Horn 1 `"188"` +5.0 and `"588"` +5.0;
   - Violoncellos `"588"` +3.5 and `"684"` +4.0;
   - Violas `"588"` +2.5;
   - Violoncellos `"188"` +2.5.
2. `build/note_trims.json`, tenuto trims. Use the default 0.6 s ramp, so the start of the tenuto keeps its level and the bloom at +0.45..+1.0 s is cut:
   - Horn 1: `189` -2 -> -6, `589` -> -5, `201` -> -4, `601` -> -4;
   - Violoncellos: `589` -5, `601` -5, `685` -4;
   - Violas: `601` -4.
   - Keep the bars-47-52 / 147-152 `roles.json` lifts.
3. Leave the existing hand fill Horn 1 `"201.0"` (9 dB, the c04 portato hole) as it is.
4. Run `fit_accents.py` only if it lists an accent inside 184-205 / 584-605 / 680-690 (none now).

**Pass:**
- At 188, 588 and 684, the quarter is 1-3 dB under the eighth on Horn 1 and the celli.
- Every tenuto peak is +2..+5 dB over its quarter on the stem.
- The master's tenuto peak is at most +3.5 dB over the quarter beat.
- No new join dip of 6 dB or more at 189/589/685.

## 2. Exposed soft cello and bass sustains in the Lento swell and sag 7-10 dB inside single notes; in the bars 9-11 crescendo the re-bow shapes lock in a sag and the master falls 3.6 dB

**Measured.**
- **The printed pp < f of bars 9-11 (qn 32-44, celli G2/A♭2, basses).** The 0.5 qn levels per stem (`beats.py`):
  - celli -30.7 dB at 38.5, then **-39.7** at 39.5 and -43.8 at 40.0;
  - basses -38.0 at 37.0, then **-44.8** from 37.5 to 39.5;
  - **the master -28.2 at 38.5, then -31.8 at 39.5**, which reverses a printed crescendo by 3.6 dB for 1.2 s.

  Three causes, from the stem, `vol_db` and `build/rebow_fills.json`:
  - (a) Basses, the F2 note at 36.0: the sample itself falls 8-9 dB at +1.85 s (37.54 qn), before the re-bow at 38.003. The fit's "pre" window (0.45-0.10 s before the re-bow) sat inside that dip. Its hold (-4.4 dB from +0.2 s, -1 dB to the end) therefore keeps the new piece at the dip level: stem -43 dB, against -38.6 dB without the shape.
  - (b) Celli: the 37.377 piece carries a fitted +10 dB shape for 0.3 s, then +6 at +0.9 s. The raw sample of that piece falls 9 dB at +1.9 s (39.0 qn).
  - (c) Celli: the automatic re-bow at 39.879 falls 0.12 qn before the printed bow change at 40.0 (the score's second A♭2 whole note, merged). The 14-CC notch at 40.0 (70 -> 56) makes a second dip 0.15 s after the re-bow. `rbnotch.py` finds the same pairing at:
    - celli 51.87/52.0 (dip -4.4), 163.877/164.0 (-8.0), 719.483/720.0 (-6.9);
    - violas 52.384/52.0 (-4.1).
- **Same-sample shapes inside single soft cello notes** (`seam2.py`). Leg Slur MAX at CC11 31-35: 4 of 6 long notes dip 7-9 dB at +1.9-2.1 s, and the A♭3s also bloom +7-8 dB at +0.9 s:
  - Celli 24.0 (bar 7, A♭3): -43.5 dB for 0.8 s, **-35.1 at +0.9 s**, -44.1 at +2.1 s, -35.8 at +2.7 s. The master is -37.5 -> **-32.7** at +0.9 s.
  - Celli 176.0 (bar 45, A♭3): the same shape (-44.6 -> -34.8 -> -47.3 -> -39.3). The master is -37.7 -> -33.2.
  - Celli 4.0 (bar 2, C3): -37.7 at +1.6 s, **-47.8 at +1.87 s**, -38.2 at +2.6 s. The bass clarinet's unison covers most of this on the master.
  - Celli 704.0 (bar 177, D3): +7 dB at +0.9 s, then a steady 10 dB decay through a printed `<`.
  - Basses 48.0 (-8.5 at +1.75 s), 13.381 (-6.5), 712.0 (-7.1).
  - The celli are 3.6-4.9 dB under the master at 24, 176 and 4.0: they carry the line there.
- `fit_rebows.py 9 build/parts.json --tracks "Violoncellos,Double basses"` (no write) would move 14 celli holds and 9 basses holds by 3 dB or more. A full refit is too blunt.

**Inferred.** In the Lento and the coda the cello line breathes with the sample rather than with the hairpins: a 5 dB surge on the master a second into a pp note in bars 7 and 45. In the crescendo into the bar-12 f, the bass drops out for a beat.

**Fix:**
1. `build/rebow_fills.json`:
   - Double basses `38.003`: set the hold to -0.5 (every point after +0.12 s to -0.5; the first 0.12 s as now).
   - Violoncellos `37.377`: cap the shape at +4 dB, then hold +4 from +1.6 s to +2.4 s (the seam).
   - Delete Violoncellos `39.879` and `41.38`, and refit them after item 3.
2. `build/loop_fills.json` (the kit c16/c20 seam lift, read by `score_to_parts.py`; empty in movement I). Keys are score onsets, matched like the `early_fills` keys; values are [s after the moved start, dB, width s]:
   - Violoncellos `24.0` and `176.0`: [[0.95, -6.0, 0.35], [2.1, 5.0, 0.45]];
   - Violoncellos `4.0`: [[1.87, 6.0, 0.35]];
   - Violoncellos `704.0`: [[0.95, -5.0, 0.35]];
   - Double basses `36.0`: [[1.95, 6.0, 0.45]];
   - Double basses `48.0`: [[1.75, 6.0, 0.4]].

   Cap each lift at 80% of the measured dip, as in the kit.
3. `tools/score_to_parts.py`, `AUTO_REBOW` (generic): `REBOW_SNAP_QN = 0.5`. An automatic re-bow point within 0.5 qn of a printed same-pitch note boundary inside a merged note moves onto that boundary, and the boundary's bow-change notch is dropped. In movement I this affects celli 39.879, 51.87 and 163.877 and violas 52.384. Then run `space_rebows.py --write` and `score_to_parts.py` again, and check the `rebows` rows of the other sections.
4. Refit only the moved points, with `fit_rebows.py` and `--skip` for every other row.

**Pass:**
- Over qn 32-44 the master's 0.5 qn level never falls more than 1 dB below its running maximum. Celli and basses never fall more than 2 dB below theirs.
- Celli 24/176: no 0.15 s window more than 3 dB over or under the note's mean from +0.5 s to the end.
- Master at 24/176: +1.5 dB or less at +0.9 s.

## 3. The doubled horn line is still one solo horn sample +3 dB in the four a2 statements of the closing theme

**Measured.** Inside 272.5-288, 381.5-406, 628-644 and 664.5-679, every Horn 2 onset is a unison with Horn 1: 69 notes, with no Horn 1-only or Horn 2-only notes. `find_unisons()` drops all of them (Horn 2 `unison_dropped` 84 in all), and Horn 1 plays them +3 dB on `1FH KS Master`. Horn 1 sits 9.7 / 14.3 / 10.9 / 8.9 dB under the master in the four spans. Kit section 8: identical-patch unisons correlate at 0.999, so this is one player made louder, not two.

Other unisons played the same way:
- Trombones 1-2: 520.5-536, 19 notes, the recapitulation's first theme, Trombone 1 10.3 dB under the master;
- Trumpets 1-2: 664.5-679, 16 notes, "a2" ff;
- Clarinets 1-2 and the flutes: 272-288 and 628-644.

The recorded two-player patches are on disk:
- `2 French Horns/06 Keyswitch/2FH KS Master.oib`, whose map is in `ks_maps.json`: Sus MAX, Leg Slur MAX, ...;
- `2 Trombones EXP/04 Keyswitch/2TB KS Master.oib`;
- `2 Trumpets/06 Keyswitch/2TP KS Master.oib`.

**Inferred.** In the loud closing-theme statements (bars 69-72, 160-161, 167-169) the horns sound as one strong solo horn, without the width and slight beating of a pair. This is the one remaining place where a different recorded patch, rather than a level, changes the colour.

**Fix** (movement II c18 recipe, kit section 8):
1. Append the track `("Horns 1-2 a2", ["Hn1"], B + "2 French Horns/06 Keyswitch/2FH KS Master.oib", "brass", -0.45)` to `TRACKS`. Load only the Sus MAX and Leg Slur MAX rows, with Close 0.5 / Main 1.0, gain = Horn 1 + 4.6 dB, and the Horn 1 seat.
2. Add it to `CC1_DYN_TRACKS`. It starts with "Horn"; check that the 2FH layer groups also use CC1 with `opus_state.load_oib` before the build.
3. `TRACK_WINDOWS` in `score_to_parts.py` takes one window per track. Make it a list of windows: `{"Horns 1-2 a2": [(272.5, 288, True), (381.5, 406, True), (628, 644, True), (664.5, 679, True)]}`, with the same four windows `False` on Horn 1 and Horn 2.
4. Re-group unisons after routing (kit c19).
5. Refit `accent_fits.json` for the a2 track's accents (273, 311, 665, 673).
6. Leave trumpets and trombones for a later cycle, one new instance per cycle (memory: c09 ended at 43 GB).

**Pass:**
- The a2 track's level over each window is within ±1 dB of c09's Horn 1.
- Join dips no worse than Horn 1's median (1.1 dB).
- No chord on its Leg row.
- Accents in 2-4 dB.
- REAPER 46 GB or less after the render (record it in CHANGES.md).

## 4. The harp's étouffez is still not played (bars 62, 163-164; unchanged from c09)

**Measured** (`harp.py`, the same numbers as c09): at qn 244 (étouffez, sub. p) the bar-61 chord rings into the new arpeggio.
- E3 reads 28.7 / 13.8 / 21.5 / 17.9 dB in the first 1.6 s.
- When E♭3 enters at 245.5 (24.9 dB), E3 is still at 21.5 dB: a semitone clash 3 dB apart for about 0.8 s.
- E4 decays only 28.8 -> 14.4 dB over 1.2 s.

At 650 (étouffez over a rest) the F2 rings 24 -> 13 dB through the rest. At 654 (m.d.) A♭5/F6 ring under the new G1/G2. `score_to_parts.py` has no étouffez rule. Harp Sus RR rings after note-off (kit section 9), so shortening notes does nothing. No Hollywood Harp patch is a damped articulation.

**Inferred.** The sub. p A♭-minor arpeggio of bar 62 starts blurred by a ringing E-major chord a semitone away.

**Fix:**
1. Where no harp note starts within 0.3 s after the mark (650.0, and the final 727.0), damp the existing Harp track with the c06 percussion pattern. Use `LEVEL_SHAPES["Harp"]` [(650.0, 0), (650.08, -30), (651.9, -30), (651.98, 0)], plus `tail_hold: false` for Harp in `build/mix.json`. No new instance is needed.
2. For 244.0 and 654.0, where new notes start with the damp, route only the damped chords (the 242.0 chord; the 652.0 right-hand chord) to a second `Harp Sus RR.oib` track, "Harp (damped)", with the same seat, mics and gain. Its envelope falls by 30 dB over 0.08 s at the étouffez and is restored before its next note.
3. Do step 2 only if REAPER settles at 44 GB or less with item 3's new track. Otherwise do it next cycle.

**Pass:**
- At 244.0-246.0 the old E3/E4 sit at least 15 dB under the new arpeggio notes within 0.2 s.
- The harp stem over 650.1-651.9 is at least 25 dB under its level at 649.9.

## 5. Smaller items (measured)

- **Legato holes of 6 dB or more** (`joins.py`; candidates for the next `auto_fills.py` pass, or for hand fills of dip - 3 dB held to the sag minimum):
  - Horn 2 453: **8.9 dB**, open since c08 (not a lead-line track, so `auto_fills.py` skips it; use a hand fill in `early_fills.json`).
  - Violins I 720 (Leg BC, the last Lento phrase, the loudest stem there at 3.9 dB under the master): 7.5 dB.
  - Celli 112: 7.6. Celli 365 / 369: 7.6 / 6.4. Celli 8.0 (bar 3): 7.2.
  - Violins II 245 / 637 / 236 / 405: 6.0-6.4.
  - Violas 517: 6.1.
- **Accents under their neighbours** (`accfam.py`):
  - Horn 1 273, the closing-theme head (Leg Slur target): +0.4 dB. On the a2 track (item 3) it will need a refit anyway.
  - Bassoon 1 521: -2.8. Clarinet 1 409: -0.85. Bass clarinet 425: -1.0. Celli 521: +1.0. Flute 1 110: +0.7.

  Refit only these rows (`fit_accents.py --family wind|string`). The Horn 1 refit waits for item 3.
- **Patch check, trombones.** The bass trombone plays the Solo Trombone KS Master. Its p/mp/f sustain layers have no sample root below E2 (`1Tb p/mp/f` roots 40-72), so the three development notes D2/C♯2/C2 (452, 456, 460) are tenor samples pitched down 2-4 semitones. Only 3 of 67 notes are affected, so no change is needed now. If a patch cycle comes, `2 Trombones and 1 Bass Trombone/3TB` patches have a real bass trombone.

## Do not touch

- `accent_fits.json` and the GENTLE_ACCENT articulations of all three families, with `--keep-long-qn` / `--pickup-qn`.
- The c09 Violins I theme-head strokes (57/65/113/479).
- `HP_SHORT_*` rules and `PORTATO_JOIN_NOTCH`.
- `TREM_ENTRY_LEAD_S`, `TREM_JOIN` / `TREM_SPLIT` seeds.
- `ROW_TRIM_DB` with `ROW_TRIM_SKIP`.
- `WIND_REP_RETONGUE*`, breath gaps and falls, `BREATH_SPLIT_AT`.
- `REP_SPLIT`, `STR_SHORT_AFTER_SUS`, `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`.
- `PORT_TARGETS`, `META_DB`.
- `METRIC_TIMP_DB`, `METRIC_BOWED`.
- Staccato rows, pizzicato and harp velocities.
- `AUTO_REBOW` and `space_rebows` everywhere outside the rows named in item 2, the re-strike plans, `TIMP_DELAY_S` and the cymbal timing.
- CC1_DYN_MAP with the c09 brass and clarinet trims.
- The climax order (160 > 122 > 169).

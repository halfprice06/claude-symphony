# Cycle 27, part 1: the offline port of series 1 (v77, c26) to score v600

Done 2026-11-06 without REAPER. The baseline render (part 2) is the c27 actor's job: it writes `CHANGES.md` here and the c27 entry in `loop/HISTORY.md`. `port/` holds the check scripts and their logs (below).

## Starting state

- `build/score_config.py` started as `mockup-kit/pipeline/example-config/score_config.py`. Evaluating both files shows that every table in it equals the inline table of series 1's final `symphony/mvt2/reaper/tools/score_to_parts.py` (c26; c27 had critics only, and `cycles/c27/before/` equals the final `build/*.json`), and every other top-level value of series 1's tool equals the current generic default (`port/tblcmp.py`, `port/defcmp.py`). The per-note JSON files of `example-config/` are byte-identical to series 1's final `build/*.json`. So the starting config is the c26 state (`port/score_config.c26.py`).
- It does not reproduce c26's parts.json with today's tools, nor with `mockup-kit/pipeline/`'s: on v77's own events and MIDI, 9 of 32 tracks come out identical with this folder's tools (11 with the kit's), the tempo map is identical, and the differences come from generic rules added in Movement I c01-c36 that are on by default (`port/newdefs.py` lists them: hairpin swell rules, SHORT_SUS_*, REP_SPLIT, WIND_REP_RETONGUE, SLUR_PAIR_RELEASE, TIMP_DELAY_S, FP_SPIKE, HELD_DECRESC, ...). The example config switches off only AUTO_REBOW and GENTLE_ACCENT and sets REBOW_VEL 41. Series 2 keeps the generic rules on (the brief's choice), so c27 is c26's tables plus today's generic rules on v600.

## Extraction (`build/mockup.ly`)

- v600 carries 53 hidden dynamics (`-\tweak stencil ##f \mp` etc.): MIDI-only levels the composition loop added because LilyPond's MIDI velocity is one value per note-on. They also ended hairpins in the score. `mockVol` now replaces each by a hairpin stop (`\!`), so it still ends its hairpin in the events ("cresc 1") but sets no level. Read as dynamics they had moved many lines a level up and broken hairpins (Violins I bars 23-24 swell read as mf, the bar 58 crest, Horn 1 bar 8), and removed outright they had made the next hairpin run to the next printed mark (Violins I 241 > ran to 249).
- `mockVol` also drops the score's `midiMinimumVolume`/`midiMaximumVolume` (cor anglais bars 47-53, Clarinet 1 coda), `instrumentEqualizer` and `midiExpression` (the strings' MIDI niente and the bar 91 morendo, CC11 in score.midi): velocities come from the mockup's table alone, CC11 from `score_to_parts.py`.
- After the change, 411 of the 1143 notes common to v77 and v600 (onset, staff, pitch) still have another velocity; these follow v600's own new dynamics and hairpins (LilyPond interpolates velocity under hairpins).

## Tools (`tools/score_to_parts.py`; all generic, defaults on)

- `SOLI_AS_META`: "4 soli"/"soli" on a string part reads like "metà" (`META_DB` -3 dB until "tutti"/"unis."/"div."): Cb 220-238 and 286-304, Vc 274-286.
- "via sord." is a mute-off word for CC15, but a change with no later note is not written (v600 prints it on the final chord for the next movement; it would have switched the mutes off under the chord).
- `AUTO_REBOW_SKIP_TREM`: held tremolos are not re-bowed (the Sus MAX re-bow would turn the 4 qn tremolos of bars 61-64 into sustains).
- Re-bow chord partners: a note that starts with an auto-re-bowed note and ends with it (or up to 0.15 qn earlier) gets the same keyswitch back (the Violas' 204 chord, one note cut 0.03 qn short, stopped the build).
- `REBOW_SAME_ROWS = ("Flautando",)`: a held Flautando note is re-bowed on Flautando (Violins II div. sul tasto, bars 37-40, was turning ordinario at each re-bow).
- `SUBITO_AT` {staff: [qn]}: listed marks are reached at once and are never a hairpin's target (used for the f after the bar 58 breath).
- The dynamic-curve check reads an fp after its spike (the 4 "fp at 148" warnings were the spike's first 0.02 qn).
- A "portato" script reads as a tenuto (v600 violas, bars 48-51; it was not read).
- `tools/stem_fix.py` scratch defaults renamed `mvt2-stemfix-*` (the Movement I thread uses `stemfix-*`).

## Config (`build/score_config.py`; each change carries a "v600 port:" comment)

- `SCORE_TITLE` "mvt2-mockup". `TRACKS` unchanged (32 tracks, same stems): v600 has no trumpet or percussion notes.
- `TRACK_SPLITS`: Violoncellos div (63,66) -> (62,66); Violins II div threshold 64 -> "rank" (114 has F sharp 4 + B flat 4); Violas div (277,289) -> (266,269) and (279,304). `TRACK_WINDOWS` unchanged (the solo is still bars 17-22; "a2" still 261-272).
- `RAMP_SPANS` (212,220,54) -> (216,220,54): the allargando starts at bar 64. `CAESURA`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH`, `APEX_LEAD` unchanged (every printed breath they answer is still there; v600's new breaths at 196 and 208 got no caesura).
- `REBOW_VEL` 41 -> None (by printed level, 38-45 at the final chord). `AUTO_REBOW` and `GENTLE_ACCENT` back to the generic defaults (on).
- `REBOW_AT` additions: the opening chord (Vln I 2.4/4.6/7.35, Vln II 5.15, Vla 5.7, Cb 6.25, Vc 6.8; the automatic points fell within 0.22-0.25 s), bar 66's printed down-bow at 223 (Vln II, Vla, Vc; with `NOTCH_SKIP` 223), and Violas div's A flat 3 in the final chord (287.3, 288.6, 291.7, 295.3, 298.3, 301.25, 302.95; at least 0.35 s from the c26 points of the other five sections).
- `HP_TARGET_AT` + `SUBITO_AT` at bar 58: the < from 188 goes to the crest v600's hidden marks give (f in Vln I/II, mf in Fl1/Ob1), the f at 196 is a fresh level after the breath (it was held at CC 82 under its f). `DYN["pp-"]` 28 and `HP_TARGET_AT` Cl2 295 -> pp- (the morendo now reaches the printed ppp; series 1 had the same warning and played CC 16).
- Removed (changed or missing notes): VEL_SET Vc/Cb 286; Tbn1 212.5 v96 -> v106 (no longer an accent: the top of the c14 Marc Lng fall); ACCENT_DB_AT/ART_AT/SWELL_S_AT Tbn1 212.5; BC_SOFT_SKIP Vln II 57, Vla 159, Vc 62/160/220; PORT_TARGETS Vc 83; BREATH_GAP_AT and BREATH_FALL_CC Horn 1 195; HP_SOFT_GAIN_AT Horn 1 176, Flute 1 126; MERGE_NOTCH_AT Vc 148; NOTE_TRIM_RAMP_S Cl1 256, Vc 180, Horns a2 261; REP_RETONGUE_AT Bn2 23; ABUT_LEAD Bn1 at 27; SHARED_DYN Bn1 259 (v600 prints it on Bn1); TIMP_TIE_STROKES 211 -> 209.5 (moved); JOIN_NOTCH Vln I 249.37, Vc 181.85/202.84/285.75, Vla 161.86, Ob1 144.81, Cb 76.10/285.95, Bass clarinet 93.03/93.39/93.89.
- Kept although v600 changed nearby: `SWELL_NO_SOFT_GAIN`, `SWELL_SOFT_GAIN_AT` and `HP_SOFT_GAIN_AT` Violin I solo 48 (the shapes changed only by v600's hidden marks, which the mockup does not read; the swells are shorter now), `HP_TARGET_AT` Hn3/Hn4 268, `PORT_TARGETS` Vln I/II 82 (now f), `MARCATO_SPANS` (v600 adds slurs and a tenuto inside the marcato line).

## Per-note tables (`build/*.json`)

Rule (`port/port_tables.py`): an entry is dropped when its note is missing, or changed in a way its kind depends on. Level shapes (note_trims, loop_fills, loop_profiles): pitch, length, printed dynamic, articulation. Early fills: pitch, length (unless both are 1 qn or more), the adjacent note before (another pitch within 0.25 qn), articulation. Timing (leg_leads): pitch, the adjacent note before, articulation. Entry leads: pitch only. `_skip_onsets`: pitch only. Bowing marks and fermatas are ignored; nearby hairpins and later notes do not drop an entry. In the TRACK_SPLITS windows the section is checked on its lowest note and the div track on its upper note. `_auto` lists follow. 89 dropped, 3 moved, the rest kept (`port/port_log.txt` lists each with its reason, kept-with-changes too):

- `note_trims`: Flute 1 254 (missing), 129, 129.5 (pitch, dyn), 258 (dyn); Clarinet 1 256 (dyn), 204 (pitch, length); Bass clarinet 93 (pitch, dyn), 108 (pitch); Bassoon 1 208 (pitch), 269 (tenuto added); Bassoon 2 172, 182 (missing), 190 (dyn), 196 (pitch), 253 (tenuto added); Violoncellos 139 (dyn), 164, 180, 261 (pitch), 81 (length), 265 (dyn); Timpani 271 (missing); Violins I 82, 83, 84 (dyn); Violins II 82, 83, 84 (dyn); Horn 1 180 (pitch, dyn); Harp harmonics 276 (dyn); Horns 1-2 a2 261 (dyn).
- `early_fills`: Flute 1 128, 129.5, 132, 134, 135 (pitch), 250, 252, 193 (missing), 194, 256 (note before); Oboe 1 145 (pitch), 193 (missing); Clarinet 1 182 (pitch), 184 (note before), 251.5, 252 (missing); Bassoon 1 267, 269 (tenuto added); Horn 1 180, 195 (pitch), 184 (note before), 203 (missing), 267, 269 (tenuto added); Horn 2 210 (pitch); Bass clarinet 91.5, 92, 92.5, 98, 99 (the solo an octave lower); Violas 251.5 (note before); Violins II 59 (note before); Violoncellos 157, 159 (missing), 160, 164, 180, 219, 247 (pitch), 77, 162, 220, 249 (note before), 267 (tenuto added); Violins II div 108 (pitch); Violas div 277 -> 279 (moved: the coda entry is now at 279).
- `leg_leads`: Violins I 210 (pitch: now a double stop), 262 (note before); Violoncellos 180 (pitch), 204 (note before); Horn 1 195 (pitch); Bass clarinet 92.5, 106 (octave).
- `entry_leads`: Clarinet 2 268 (pitch); Violins II div 108 (pitch); Violas and Violas div 277 -> 279 (moved).
- `loop_profiles`: Violoncellos 164 (pitch); Timpani 292 (no coda roll in v600). `loop_fills`: all kept.
- `pitch_trims` `_skip_onsets`: Clarinet 1 204, Bassoon 2 198 (pitch). Pitch keys kept (sample properties of the patch).
- `rebow_fills`: all kept (the held notes under every c26 point are unchanged; the Violas' added A flat 3 plays on Violas div).
- `roles` (`port/roles_log.txt`): dropped Timpani [292,304,4] (no notes), Bass clarinet [93.5,99,-6,2.5] (the register burst it answered is gone), Horn 1 [179.25,180.75,-6.5] (the mp arrival moved to 182), Violoncellos [148,151,3,2] (now printed mp), Trombone 2 / Bass trombone / Tuba / Horn 2 [204,212,...] (bar 61 lifts for a printed mf, v600 prints f; Horn 2 ff), Violoncellos [262,268,2] and [262,265,2,0.25] (bar 79 lifts for f, v600 prints ff); changed Harp [238,262,4] -> [238,256,4] (v600 adds mp at 256 and an f stroke at 261), Violas div [276.5,304,-5] -> [278.5,286,-5]; Violas div copies the Violas rows from 289 and [266,268,2.5] (the c18 rule: div tracks copy their section's roles).
- `probe.json`: the Violoncellos pizz. refs 108-116 replaced by the Double basses' 110-116 (v600's celli rest there).
- `rebow_moves.json`: new (written by `tools/space_rebows.py --write`): 11 automatic points moved.

## parts.json against series 1's c26 parts.json

- 32 tracks, same names, order, stems and patches. Notes 1466 -> 1526 (after merges, unison drops, splits and re-bow pieces). Tempo map 418 -> 402 points; only qn 212-219.75 differ (the allargando); 348.9 -> 348.2 s to qn 304.
- Opus states that change (rows; these tracks need a full rebuild, and the empty `jobs/` cache makes every track a full rebuild anyway): new rows Clarinet 2 Leg Slur, Bassoon 2 Leg Slur MAX, Horn 1 Sus MAX, Horn 3 and Horn 4 Leg Slur MAX, Double basses Leg Slur MAX, Violoncellos div Leg BC MAX, Violas div Sus MAX (re-bows), Horns 1-2 a2 Sus MAX; no longer used Flute 2 Leg Slur MAX, Violoncellos Leg Port MAX and Pizzicato RRx4. Every new row is a row the patch has; none was loaded in series 1's c26 states for those tracks.
- Every track's pitch range lies inside its patch's mapped keys (read from the `.oib` regions) and clear of its keyswitch keys; the bass trombone's D2 (qn 218) plays an E2 sample two semitones down, as in series 1.
- `score_to_parts.py` prints no WARNING.

## Re-running the checks

`port/run_check.py [-b]` lists the status of every onset-keyed c26 entry against v600 (it reads series 1's build and the kit's example config; `-b` only the changed ones). `port/port_tables.py OUTDIR` writes the ported JSON tables into OUTDIR and prints the log; `port/port_roles_docs.py`, run in a folder holding `newjson/` and `port_log.txt`, ports roles.json and adds the `_doc` notes. `port/show.py STAFF QN0 QN1` prints both scores' events for a staff and span. `port/summary.py OLD NEW` and `port/pcmp.py OLD NEW` compare two parts.json files.

# Cycle 16, critic A (articulation and phrasing) on the c15 render

All numbers are measured on `cycles/c15/render/` stems and master and on `build/parts.json` (identical to `cycles/c15/rendered_build/parts.json`) unless a line says "inferred". Envelope = the track volume envelope as `build_reaper.py vol_points` writes it. To split it by rule I ran a copy of `tools/score_to_parts.py` in scratch that records the source line of every `vol_parts.append` (its parts.json is byte-identical to `build/parts.json`); "per-note layers" are all rules except roles, hairpin gains, held decrescendos, divisi / chord cuts, swell, sostenuto, timpani roll rules and the final fade.

## Manual notes (third round: pages behind the volume-envelope question)

| Manual (May 2021, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.64 and p.151: Volume (CC7, the fader) sets a track's level against the other tracks; Expression (CC11) shapes "the continually changing dynamics" of a line; it is "as opposed to shaping an individual musical line" that volume is meant | every track | No. The fader carries 0.8-16.4 points per second on the pitched tracks (strings 9.3-16.4); CC11 has 1.0-4.9 and CC1 1.3-2.7 on the eight tracks I counted. The EW template and the expert files (FINDINGS parts 1, 3, 6) have 7-44 points per second in CC1 / CC11 and 0-0.36 in volume |
| p.53, p.64, p.150: note velocity sets loudness and timbre of short articulations (Staccato, Staccatissimo, Marcato) through velocity-mapped dynamic layers | string staccato quarters of the first theme (bars 11-34, 151-170), hammered eighths | Partly. The staccato rows play at velocity 100 and are then pulled down 4-8 dB by the fader on every note (finding 1) |
| p.137: each row of a KS Master has a VOLUME KNOB "to adjust the loudness of each articulation" | "Staccatissimo RRx9" / "Stac RRx9" against "Sus MAX" on the five string tracks; "Tremolo" (`ROW_GAIN_DB` -3 / -4); Violins II "Sus MAX" (`ROW_TRIM_DB` -4) | No. Row level differences are per-note fader steps (`steady_levels.json` `level_default`, `ROW_TRIM_DB`, `ROW_GAIN_DB`). `build_reaper.py` already edits the row list of the patch state (the `loaded` flag, near line 276); the knob is not used |
| p.151: CC11 gives "swells in the middle of a note" and crescendos | printed accents (1109 in the score), hairpins | Hairpins: yes in CC11, plus a dB gain in the fader. Accents: no CC or velocity change (`GENTLE_ACCENT`), the whole accent is a fader swell (finding 2) |
| MANUAL-GAPS #1 (p.101, 62-63: filtered marcato attack for brass accents), still open | brass heads of 247-262, chorale | Not used. Horn and trumpet accent fronts are still duller than plain notes (finding 2) |

## First priority: the per-note volume automation (answer for Dan)

**What Dan saw, counted (measured).** 53,696 volume points on 31 tracks. Strings 23,074 (Violins I 3,946, Violins II 4,002, Violas 4,074, Violoncellos 4,135, Double basses 6,917; 9.3-16.4 points per second, 4.8-10 per note). Winds 15,906 (0.8-5.3 per second), brass 12,765 (2.4-4.5), timpani 1,798. 2,385 of 9,061 notes have a swing of 3 dB or more between their moved note-on and their end, 602 have 6 dB or more; 1,039 of the 2,385 (44 %) carry no accent, sf / fp, tenuto, staccato, hairpin or dynamic change (strings 542 of 1,023, winds 210 of 702, brass 200 of 491, timpani 87 of 157). 54 % of all fader travel (sum of dB moved) lies inside single notes (strings 44 %, winds 76 %, brass 58 %). Of 2,346 notes of an eighth or less, 563 move 3 dB or more inside the note (301 of them are the basses' repeated eighths). Within-note swing per track: median 0-3.0 dB (timpani 6.0), 90th percentile 3.5-7.4 dB (timpani 8.7), maximum 8-28 dB.

**Why it is there (measured, by rule).** Points written / dB travelled / notes that this rule alone moves 3 dB or more (of which an eighth or shorter):

| rule | points | travel dB | notes >= 3 dB | reason it was added |
|---|---|---|---|---|
| accent swells (`GENTLE_ACCENT`, 27 tracks) | 6,911 | 5,945 | 570 (6) | every printed accent is a fader swell, +2.5 to +3.5 dB |
| basses / celli repeat dips and beat gaps (`STR_REP_DETACH`) | 1,616 | 4,823 | 186 (133) | S1: separate the repeated eighths |
| pitch trims | 1,606 | 2,590 | 289 (60) | per-pitch sample level differences |
| hairpin dB gain | 11,940 | 2,030 | 127 (0) | printed hairpins; a ramp is written as a stair of grid points |
| timpani roll rules | 1,296 | 2,032 | 155 (42) | Dan's roll rule |
| divisi / chord cuts | 717 | 1,607 | 56 (8) | full-section sample per chord note |
| theme level steps (`steady_levels.json`) | 663 | 1,599 | 82 (0) | c15 one-row theme |
| roles | 2,849 | 1,561 | 92 (1) | balance |
| `LEVEL_SHAPES_S` (fronts, notches) | 735 | 1,358 | 93 (2) | hand-fitted faults |
| `ROW_TRIM_DB` | 676 | 1,285 | 78 (37) | Sus row louder than legato row |
| unison boost (`UNI_BOOST`) | 454 | 1,221 | 224 (23) | one player sounding for two |
| brass re-tongue dips (`WIND_DETACH`) | 341 | 1,081 | 99 (21) | S1 |
| metric steps on bowed eighths | 1,179 | 849 | 4 (4) | down-beat / off-beat pattern |
| re-bow fills | 1,270 | 623 | 25 (0) | holes at re-bows of long notes |
| held decrescendo | 1,712 | 576 | 23 (0) | printed |
| pair release, note trims, arrival, `LEVEL_SHAPES`, fade, swell, others | 1,790 | 1,913 | 103 | single fixes |

Short answer for Dan: the instrument's own lanes (CC11, CC1, velocity) are nearly flat inside phrases, and almost every correction made in 15 cycles was written into the fader: accents, level differences between articulation rows and between pitches, separation of repeated notes, holes at bow changes. Only part of it is audible as intended; findings 1-3 say which part helps, which does nothing, and which hurts.

**Does it help? Median note-to-note level step per line (stem RMS over the first 0.35 s of each note; "off" = the same minus the per-note layers' mean over that window; "cap" = per-note layers limited to +-3 dB), measured:**

| line | with | off | cap 3 | verdict |
|---|---|---|---|---|
| Violins I first theme 11-26 / 151-170 | 1.8 / 1.5 | 2.9 / 2.2 | 2.1 / 1.6 | helps (theme level steps) |
| Violins II first theme | 1.7 / 1.8 | 1.4 / 1.9 | 1.7 / 1.9 | nothing |
| Violas first theme | 1.9 / 2.2 | 2.3 / 2.8 | 2.2 / 2.6 | helps a little |
| Horn 1 first theme | 3.0 / 3.1 | 2.5 / 2.7 | 2.7 / 2.6 | hurts (unison boost steps, accents) |
| Celli / basses 27-34 | 3.6 / 1.3 | 4.4 / 3.5 | 3.6 / 1.9 | helps |
| Bassoon 1 / Tuba 27-34 | 2.4 / 2.4 | 2.0 / 0.9 | 2.0 / 2.4 | hurts (accent swells) |
| Second theme 67-82 (Violins I, II, celli) and 187-198 | 1.7-2.8 | 1.7-2.7 | same | nothing |
| Trumpet 1 solo 51-66, cor anglais, transition solos, Clarinet 1 | 1.7-2.5 | same | same | no per-note layer there |
| Trumpet 1 muted 171-186 | 2.0 | 2.9 | 2.0 | helps (4 fitted shapes) |
| Bassoon 1 solo 115-122 | 1.5 | 2.7 | 1.5 | helps (c13 shapes) |
| Codetta 91-98: Trumpet 1 / 2, Violins I | 3.2 / 2.8 / 3.3 | 2.7 / 1.2 / 1.7 | same as with | hurts as a step measure; these are the accent swells |
| Hammered 199-210: Violins II, Violas | 2.8 / 5.0 | 2.2 / 4.4 | 2.9 / 4.4 | hurts (accents, row trim, metric steps) |
| Piu allegro 247-270: Violins I, Horn 1, Trumpet 3 | 2.4 / 2.4 / 2.9 | 1.6 / 1.9 / 2.5 | 2.4 / 2.0 / 2.9 | hurts (accents, unison boost, dips) |
| Piu allegro Trumpet 1 | 1.5 | 1.7 | 1.8 | helps (c14 shapes) |
| Chorale 223-234 brass | 1.6-3.7 | same | same | no per-note layer; celli 1.7 against 2.9 off (re-bow fills help) |

Balance does depend on the layers here, unlike Movement I: with them off the whole-movement stem RMS moves by -2.4 dB on Horn 1, -1.5 on Trumpet 1 and Horn 2, -1.2 on Horn 3, +1.7 on the harp, +1.2 on the celli, +1.1 on Oboe 1; 0.0-1.0 dB on the other 22 pitched tracks. The horn and trumpet amounts are the unison boost, which is a balance layer written note by note.

The S timing scatter of the theme is not an artefact of the level steps: on the nine string lines of bars 11-34 and 151-170 the correlation between S and the envelope step at a "Sus MAX" join is -0.40 to +0.40 with no common sign; notes with a step of 2 dB or more are outside 25 ms in 38 of 124 cases (31 %), the others in 66 of 287 (23 %).

## Findings

### 1. The theme's level steps run 40-125 ms ahead of the notes, and most of them are one row offset (bars 11-34, 151-170; Violins I, II, Violas 40-104 and 600-680, Violoncellos and Double basses 104-136)

What is wrong. `STEADY_LINE` `level_db` writes each note's level from 0.03 s before its moved note-on. With leads of 40-125 ms the previous note is still sounding, so its last 70-150 ms are played at the next note's level. On the slurred eighths (178 ms long, lead 64 ms) 53 % of each eighth sounds at the following note's level. This is the up-and-down on fast successive notes that Dan saw: 506 listed values, 222 of them 3 dB or more, 52 of them 6 dB or more (range -14.0 to +9.0 dB).

Evidence (measured). 138 theme joins have a step of 2 dB or more.
- Falling steps (72 joins, ten groups by track and row pair): hole at the join (the lower body minus the lowest 20 ms frame) 3.2-5.5 dB per group as rendered, median 4.3 (basses "Sus MAX" to staccato 10.6 dB); with the same step moved to the next note's score onset -2.0 to 5.8 dB, median 3.1 (simulated on the stem; the celli gain nothing, 4.8 / 4.8); the old note's last 60 ms sit 0.6-7.1 dB under its body as rendered, and 1.2-3.6 dB over it with the moved step (the old note keeps its own level to its end).
- Rising steps (66 joins): the old note's last 60 ms rise 1.5-5.4 dB over its body (a swell into the next note), -1.1 to +1.7 dB with the moved step.
- Violins I entries 61 and 64 read late on S because the step of the following eighth (+4.4 and +2.8 dB) arrives 85-100 ms after their beat; stem slices of 50 ms from the beat at 61: -5.0, -0.7, +10.5, +8.3 dB against the 0.25-0.40 s slice. This is a level-shape artefact, not lateness.
- The values are mostly a row offset. Violins I: "Staccatissimo RRx9" median -6.25 dB (SD 1.4) against "Sus MAX" +0.4 (SD 1.6). Row medians per span: Violins I 0.4 / -6.0 and -0.5 / -6.5; Violas "Sus MAX" 1.5 and -4.4, "Stac RRx9" -4.8 and -5.8; Violoncellos -0.6 / -8.1; Double basses +3.2 / -4.0.
- Median note-to-note step with only this rule varied (the table above varies all per-note layers), bars 11-26 / 151-170: current 1.8 / 1.5 (Violins I), 1.7 / 1.8 (Violins II), 1.9 / 2.2 (Violas), 3.6 (celli), 1.3 (basses); one level per row and span plus only the fitted values that differ 3 dB or more from the row level (94 values instead of 506): 2.6 / 1.8, 1.9 / 1.8, 2.0 / 2.9, 3.5, 1.9; one level per row only: 3.3 / 2.1, 2.4 / 2.1, 2.6 / 3.1, 6.5, 3.1; no steps: 5.1 / 3.3, 2.1 / 2.1, 2.4 / 3.2, 5.9, 4.1.

Fix.
- `tools/score_to_parts.py`, the `STEADY_LINE` "level_db" block (the `_sl_sp` / `lv_` code before `LEVEL_SHAPES_S`): add a span key `level_at` with values "moved" (now) and "score". With "score" the breakpoints are `(sec_to_qn(ts - 0.012), cur_), (sec_to_qn(ts + 0.008), v_)` where `ts` is the score onset of the note in seconds; for a note after a rest of 0.3 qn or more keep the moved note-on (nothing is sounding). Set "score" on all eight spans in `build/score_config.py` (`_C15_SPANS` loop).
- Row offsets out of the fader: per-row volume in the Opus state (manual p.137). In `build_reaper.py`, where the row list is edited for `loaded`, write a mix.json key `row_volume_db` {track: {row: dB}} to the row's volume field (read the field name from one patch JSON with `opus_state.load_oib`). Start values: Violins I "Staccatissimo RRx9" -6.0; Violas "Stac RRx9" -5.0; Violoncellos "Stac RRx9" -7.5 (keep "Sus MAX" at 0 and move its span level into `roles.json` rows for 40-104 / 600-680 / 104-136: Violas -3.0, Violoncellos -1.5, Double basses +3.2 with "Staccato RRx9" then -7.2 against it). This is an Opus state change: rebuild the five string tracks in full and verify on a range render that the staccato quarters outside the theme (which lose the same amount) are re-trimmed by `ROW_VEL_BY_CC` or a role. If the field cannot be written, the fallback is velocity: `_str_stac_vel` (88, 100) -> (88, 84) inside the spans, then refit (velocity also softens the timbre; measure 2-5 kHz).
- Reduce `build/steady_levels.json` to the values that differ 3 dB or more from the row level after the two changes (expect about 94 of 506), refit those on the range render with a window that starts at the score onset.
- Range test (bars 11-34 and 151-170, each variant rendered twice): A current; B `level_at` "score" only; C = B plus row offsets and the reduced table. Accept when the median step stays within 0.5 dB of A on each line, join holes at falling steps are under 3.5 dB median, the old note's tail is within +-2 dB of its body, and S out-of-25 counts do not rise.

### 2. Accents on strings and woodwinds swell after the attack, run into the next note and stack (all accented notes; counted on Violins I, II, Violas, Violoncellos, Flute 1, Oboe 1, Clarinet 1, Bassoon 1; 247-270, 199-210, 91-98, the theme's accented halves)

What is wrong. `GENTLE_ACCENT` for "string" and "wind" is 0 dB at the score onset, +3.0 / +3.5 dB from +0.07 s to +0.25 s, back to 0 at +0.60 s. A quarter lasts 0.34-0.36 s at Tempo I and Piu allegro, so the swell is still +2.1 dB when the next note starts and falls through that note's first 0.24 s. It starts at the score onset although the note began 40-110 ms earlier. On runs of accents the swells add (peak 4.5-5.4 dB against a nominal 3.0-3.5; Violins I 16 of 77 accents start on the previous swell). It is the largest per-note source (6,911 points, 570 notes of 3 dB or more). Dan's rule 4 asks for weight on the note, 2-4 dB, without a click; what is rendered is a note whose start is weaker than a plain note's.

Evidence (measured, notes of 0.3 s or longer at f or louder; front = score onset to +0.08 s, body = +0.15 to +0.35 s):

| track | plain notes | accents as rendered | accent shape removed | front-weighted shape (simulated) |
|---|---|---|---|---|
| Violins I (68 accents) | -1.8 | -3.4 | -1.8 | -0.3 |
| Violins II (61) | -2.8 | -3.6 | -2.2 | -0.4 |
| Violas (52) | -2.2 | -2.2 | -0.8 | +0.8 |
| Violoncellos (43) | -1.5 | -2.8 | -1.2 | +0.2 |
| Oboe 1 (40) | -2.1 | -3.0 | -1.1 | +0.7 |
| Clarinet 1 (41) | -1.3 | -3.7 | -1.8 | -0.1 |
| Flute 1 (53) | +0.8 | -2.9 | -1.0 | +0.8 |
| Bassoon 1 (42) | -1.5 | -2.2 | -0.6 | +1.4 |

Brass (swell from the moved note-on, 0.02 / 0.18 / 0.45 s since c09): Trombone 1 and Bass trombone accents have the stronger front (-1.4 / 0.0 against -3.4 / -3.2 plain); Horn 1, Horn 3, Trumpet 1, Trumpet 2 still do not (-3.5 to -4.5 against -2.0 to -2.7) and Horn 1's accented fronts are 3.0 dB duller in 2-5 kHz relative to broadband than its plain fronts (-5.2 against -2.2). The median 2-5 kHz front minus body of the accents is negative on every brass track (-0.8 to -10.1 dB): no bite, which is to be kept. (Brass fronts here are measured from the moved note-on to the score onset + 0.08 s.)

The "long notes that fall 6-12.5 dB on Sus MAX" are partly this: on Violas 52 and 612, Violoncellos 116 and Double basses 104 and 120 the envelope itself falls 4.3-4.8 dB between +0.2 s and the note's end (accent swell plus c15's +3 dB front from `LEVEL_SHAPES_S`, both on the same accented half). Stem falls 5.1 / 5.9 / 8.1 / 7.4 / 12.5 dB, so without the envelope 0.8 / 1.6 / 3.6 / 2.6 / 7.7 dB. Only Double basses 120 (7.7 dB) and Violas 668 (5.6 dB, envelope +1.3) fall in the sample.

Fix (`build/score_config.py`, `tools/score_to_parts.py` accent block near "c09 (A #5): loud accents get weight in dB").
- `ACCENT_SWELL_FROM_MOVED = ("brass", "string", "wind")`; `GENTLE_ACCENT["string"]["swell_s"]` and `["wind"]["swell_s"]` = (0.02, 0.12, 0.35) with the plateau end counted from the score onset (new key `hold_from_score`: True; the brass keep their shape).
- New rule in the same block: the shape's last point is `min(shape end, next moved onset - 0.01 s, note end)`; a new accent shape is combined with a still-running one by `max`, not by addition (`ACCENT_NO_STACK = True`).
- Accented notes of 0.20 s or less: one level for the note, 0.67 x db from the moved note-on to the note's end (`ACCENT_SHORT_FLAT_S = 0.20`).
- Remove the c15 `LEVEL_SHAPES_S` fronts (+3 dB, -lead to +0.30 s) on the accented halves in `_C15_ACC` once the accent itself is front-weighted (they are the same weight twice); keep the +1 dB at 40 and 600.
- Body shapes as slow shapes for the two notes that really fall: `LEVEL_SHAPES_S` Double basses 120.0 [(0.45, 0), (1.0, +5), (end, +5)] and Violas 668.0 [(0.45, 0), (1.2, +4), (end, +4)], rising only after +0.45 s (so S does not move).
- Horn and trumpet fronts: range-test MANUAL-GAPS #1 on Horn 1 only (the accented heads 984-1048 on "Sus Marc LITE" / "Marc Sus" at velocity 60-80, no swell); accept if the front is within 1 dB of the plain notes' and 2-5 kHz front minus body stays under 0 dB. Memory: one row.
- Range test (bars 247-262, 199-206, 91-98, 11-26): accept when accented fronts are 0 to +2 dB over the plain notes' front-minus-body value on each track, the first 0.24 s of the note after an accent no longer falls (envelope change under 1 dB there), and the accent-to-neighbour level difference stays 2-4 dB.

### 3. Layer plan for the actor's range test ("per-note layers off", "capped at 3 dB", current), with the layers that must stay

Remove or rewrite (each with the measurement above):
- Theme level steps: rewrite as in finding 1 (helps: +0.4 to +2.4 dB on the step median when removed; faulty timing).
- Accent swells: rewrite as in finding 2.
- `UNI_BOOST` (454 points, 224 notes of 3 dB or more, 13 wind and brass tracks): a balance amount of +3.0 / +4.8 dB written per note, on the 0.125 qn grid from the score onset. After a rest the note starts at 0 dB and ramps up between the score onset and +45 ms, that is 110-170 ms after a led note began (Horn 1 at 44.69: 0 dB until 45.0, +3.0 at 45.125; read in the written envelope). Horn 1 has 37 of 152 entries with a rise of 2 dB or more later than 30 ms after its note-on (the count includes its accent swells). Removing it lowers the step median 0.2-0.4 dB on Horn 1 in three sections. Rewrite in `score_to_parts.py` at the "kept note of a same-patch unison" loop: merge consecutive boosted notes less than 0.5 qn apart into one span from 0.05 s before the first moved note-on to the last note's end (same value), new value only where the count of doubled players changes, at the score onset. Expected: Horn 1 points 1,923 -> about 1,500, no level change on the bodies (inferred).
- `ROW_TRIM_DB` (676 points; 37 short notes of 3 dB or more) and `ROW_GAIN_DB`: move to `row_volume_db` (finding 1) on the tracks rebuilt for it; elsewhere keep.
- Point thinning, no change in sound: `vol_points` writes every grid value that differs from its neighbours, so each linear ramp is a stair of points 0.125 qn apart. Dropping points that lie within 0.1 dB of the straight line between their neighbours gives 53,696 -> 33,469 points (Violins I 3,946 -> 2,446, Double basses 6,917 -> 4,862, Horn 1 1,923 -> 1,295); 0.25 dB tolerance 25,159. Add this pass at the end of `vol_points` (after `vol_post`), tolerance 0.1 dB, never across a `vol_bp` breakpoint.

Cap at 3 dB: pitch trims on notes of an eighth or less (60 notes), and any remaining fitted theme step on a note of an eighth or less. The cap test above shows the cap loses 0.1-0.6 dB of evenness on the lines the layers help and removes nothing that hurts, so a global cap is not the answer; the per-rule changes are.

Keep (measured reason):
- Basses' and celli's repeat dips and beat gaps (1,616 points): the basses' repeated eighths separate by a median 7.9 dB (199-210) and 7.8 dB (247-270); c11 measured master on-beat dips 7.8-10.6 dB with them. They are the reason Double basses carry 6,917 points. Still open inside them: 31 of 244 repeats under 3 dB (finding 4).
- Re-bow fills (1,270 points, 94 % inside notes): celli chorale step 1.7 dB with, 2.9 without; the four re-bows at 915.3-929.3 show no dip (0.5 to -0.9 dB).
- Pitch trims on notes longer than an eighth (balance: B's c12 trims; celli Q theme 2.4 with, 3.0 without).
- `LEVEL_SHAPES` / `LEVEL_SHAPES_S` with a named fault: Bassoon 1 solo (1.5 with, 2.4 without), muted Trumpet 1 (2.0 / 2.9), Trumpet 1 984-1000 (1.5 / 2.2), the 592 sfp notch and fronts, bar 222 / 245 fronts, dal niente shapes.
- Brass re-tongue dips, pair release, metric steps (one level per note already: 4 % of their travel is inside notes), hairpin gains, held decrescendos, divisi cuts, roles, timpani rules, arrival weight.

Variants for the range test (bars 11-34, 91-98, 115-122, 151-170, 199-210, 247-262; each twice): V0 current; V1 per-note layers off except the Keep list; V2 the rewrites of findings 1-3. Measures per line: median and 90th-percentile note-to-note step, join holes, accent fronts, S out of 25 / 60 ms, per-track RMS within 0.5 dB of V0, and the counts of this report (points, points per second, notes of 3 dB or more inside the note, share unmarked). Target for V2: under 30,000 points, unmarked notes of 3 dB or more under 400 (now 1,039), no line's step median more than 0.5 dB over V0.

### 4. S1: repeated notes that do not separate (bars 199-210 Violas; the head's repeated C at 988, 992.5, 996 on Trombone 1, Violoncellos, Bassoon 1; basses' eighths)

Evidence (measured; dip = the lower of the two bodies minus the lowest 20 ms frame around the re-attack, on the stem).
- Violas 792-840: 15 same-pitch repeats, median dip 1.2 dB, 9 under 3 dB (796.0 1.6; 800.5 0.8; 818 / 820 / 822 chords 0.4 / 1.1 / 1.0; 825.5 -1.9; 829.5 0.4; 831.5 1.2). The gap between the note-off and the next moved note-on is 45-53 ms (795.5 ends 795.725, 796.0 starts 795.85; 817.5 ends 817.678, 818.0 starts 817.828): the 60 ms lead of the next "Sus MAX" note takes it out of the 0.09 s gap, and the 150 ms release fills the rest. Violas 984-1080 and 888-936 are fine (median 6.9 and 9.6 dB).
- Head motif D - C sharp - C | C (tenuto): Trombone 1 988.0 1.1 dB, 992.5 1.9, 996.0 -0.2; Violoncellos 1.8 / 2.2 / 2.5; Bassoon 1 988.0 1.4, 996.0 0.2. On Trombone 1 and Bassoon 1 the third eighth is a "Leg Slur MAX" target 120 ms long (987.5, moved to 987.275, duration 0.353 qn); it speaks late and its release covers the 77 ms gap. The research default for repeat gaps is 60-100 ms (strings median 90, brass 98).
- Double basses: 21 of 162 repeats under 3 dB in 247-270 (988.5 -3.0, 989.5 0.2, 1004.5 -1.1, 1008.5 -0.3, 1009.5 0.1 ...), 10 of 82 in 199-210 (800.5-803.5 1.9-2.2, 837.5 -0.8).
- Also under 3 dB: Trumpet 3 993.5 (2.2), 1078.0 (0.6); Trombone 2 and Bass trombone 836.0 (1.6 / 2.7); Violins II 796.0 (2.2), 996.0 (1.6), 1056.5 (1.8); Oboe 1 924.0 / 928.0 (1.1 / 1.9), 836.0 (-0.4); Bassoon 2 892.0 (0.6).

Fix.
- `build/score_config.py` `ROW_LEAD_KEEP_GAP["Violas"] = {"Sus MAX": [(792.0, 840.0)]}`, `["Violins II"]` (792, 800) and (992, 1060), `["Violoncellos"]` (984.0, 1000.0): the note before ends earlier by the lead, so the played gap is 0.09 s again. Expected dip 4-6 dB (inferred from the violas' 6.9 dB in 247-270 where the gaps are whole).
- Trombone 1 and Bassoon 1 987.5 and 995.5 (and 989.5 where it repeats): play the third eighth on "Sus MAX" as a re-tongued short (`ART_AT` or the track's `SHORT_SUS` list), end it 0.09 s before the tenuto C's moved note-on; keep `WIND_DETACH`'s dip there.
- Where a site is still under 3 dB on the range render, a notch keyed in seconds from the next note's moved note-on (`LEVEL_SHAPES_S` on that note: [(-0.075, 0), (-0.055, -8), (-0.008, -8), (0.004, 0)]); Movement II measured this form (joins over 5 dB 21 -> 3 of 460). Basses: the same notch at the listed sites instead of a deeper general dip.
- Check after the change that no repeat's gap shows as a hole in the master (the hall return covers it): master dip 2-5 dB at the viola sites.

### 5. Four tutti stops are drier than the 14-17 dB range; a return ride on the tail restores them (bars 2, 6, 113, 166)

Evidence (measured, the actor's measure: 20 ms RMS, drop at +0.3 s against the 0.15 s before the stop; my values 17.8 / 18.3 / 20.5 / 18.1 dB, time to -20 dB 0.35 / 0.34 / 0.28 / 0.39 s). At +0.3 s the dry stems and the four hall returns have equal power at bars 2, 113 and 166 (-42.2 / -42.4, -45.3 / -45.3, -44.3 / -44.3 dBFS) and the returns lead at bar 6 (-43.1 / -42.0). The loudest single stems there are the celli at bars 2 and 6 (-45.3 / -47.5; they carry the c13 release fade) and "R Strings" (-45.7 / -44.8); at bar 166 "R Strings" -45.8 and Double basses -46.7 while Violins I and II have fallen 23.5 / 25.4 dB ("Sus MAX" with the 150 ms cap). Removing the celli / basses release fades at 5.0 and 21.0 gives only -1.2 / -0.8 dB (simulated).

Simulated on the stems (master plus the four return stems raised from 0.05 s before the stop, held 0.9 s, released over 0.3 s):

| stop | now | returns +2 dB | +3 | +4 | +6 |
|---|---|---|---|---|---|
| bar 2 (qn 5.06) | 17.8 dB / 0.35 s | 16.8 / 0.36 | 16.2 / 0.38 | 15.6 / 0.43 | 14.3 / 0.45 |
| bar 6 (21.06) | 18.3 / 0.34 | 17.3 / 0.36 | 16.7 / 0.37 | 16.0 / 0.42 | 14.7 / 0.43 |
| bar 113 (450.0) | 20.5 / 0.28 | 19.2 / 0.30 | 18.5 / 0.35 | 17.8 / 0.38 | 16.1 / 0.41 |
| bar 166 (662.0) | 18.1 / 0.39 | 16.7 / 0.42 | 16.0 / 0.47 | 15.1 / 0.47 | 13.4 / 0.47 |

Fix. `build/mix.json` new key `return_rides`: [[5.06, 3.0], [21.06, 3.5], [450.0, 6.0], [662.0, 3.0]] (score qn of the stop, dB), written by `build_reaper.py` as volume-envelope points on the four return tracks: 0 dB at stop - 0.05 s, the value at stop + 0.05 s, held to + 0.9 s, 0 dB at + 1.2 s or 0.05 s before the next note-on of any track, whichever is first. Expected 16.2 / 16.4 / 16.1 / 16.0 dB with -20 dB reached in 0.38-0.47 s (ceiling 0.50 s). The ride acts only on the ring after the dry sound has stopped; no send is raised. Leave the c15 release fades as they are. Bars 94 and 204 and the final chord (15.6 / 14.3 / 14.9 dB) need nothing.

### 6. Timing classes still open (S from `cycles/c15/logs/render/S_c15.json`)

- Entries after rests on "Sus MAX", Violins I. 48.0 and 608.0 are really late: the stem is -10.1 / -11.9 dB in the first 50 ms after the beat, -6.1 / -9.2, -4.3 / -8.1, -1.5 / -3.8 dB in the next three 50 ms slices, with a flat envelope (leads 90 / 66 ms). Fix: `steady_leads.json` class "first" for entries after a rest of 0.5 qn or more: 0.15 s on 40-72 and 0.14 s on 600-632 (per-onset `at` rows 48.0 and 608.0), not a level shape. 61.0 and 64.0 are the artefact of finding 1 (fixed by `level_at` "score"). 40.0 and 600.0: the stem overshoots +5.7 / +2.1 dB at +0.10-0.15 s where the +1 dB front and the accent swell meet; finding 2's shape removes the late rise; re-measure before changing their leads (107 / 123 ms).
- First theme "Sus MAX" joins: medians -11 / -9 / -7 ms (bars 11-26) and -2 / -1 / -5 (151-170) with interquartile ranges of 20-39 ms; 12 + 20 of Violins I's joins are outside 25 ms. The class leads are centred; the spread is per note. Violas' staccato quarters in 151-170 are late: "Stac RRx9" after "Stac RRx9" +70 ms median (4 notes), "Stac RRx9" after "Sus MAX" +31 (8): `ROW_LEAD_S["Violas"]["Stac RRx9"]` (600, 680) +0.04 s.
- Hammered eighths 199-210, class causes: Violins I "Sus MAX" joins -11 ms median, 11 of 33 outside 25 ms (lead 10 ms too long: `ROW_LEAD_S` "Sus MAX" (792, 840) -0.01 s); its four "Leg BC MAX" joins +42 ms, its legato-row entries after "Sus MAX" +50 ms (2) and after a staccato +99 ms (1) (row changes: put 792-816 of Violins I on one "Sus MAX" span as in the theme, test on a range render); Double basses' eighths +13 ms median, interquartile -3 to +25, 24 of 83 outside 25 ms and the first eighth -86 ms.
- Piu allegro 247-270, class causes: Horn 1 "Leg Slur MAX" joins +14 ms median with an interquartile range of 60 ms (11 of 19 outside 25 ms), its legato entries +61 (3 notes), "Sus MAX" entries -20 (6); Trumpet 1 legato joins +18 (interquartile +3 to +53, 9 of 17 outside); Trombone 1 "Sus MAX" notes joined after a legato note +37 (5 of 7 outside), "Sus MAX" entries after a legato note -87 (2), one legato-row repeat after "Sus MAX" +135. The slurred eighth pairs of the heads take the full legato transition at 170 ms per eighth. Fix: one row lead correction per track (Horn 1 legato +0.015 s, Trumpet 1 +0.02 s, Trombone 1 "Sus MAX" joined after legato +0.035 s, "Sus MAX" entries after legato -0.08 s) and a pitch-pair table for the pairs outside 40 ms after that (`LEG_PAIR_EXTRA_S`, the c15 method that brought Horn 1 (65, 64) from -152 to -37 ms).
- Still open from c15 and unchanged in my reading: Violins I 744 (+72 ms: entry lead 0.17 -> 0.22 s), Violins II 300 (-59 ms: `leg_leads.json` row +0.05), codetta chord 360 (Trombone 1 -49, Double basses +56).

## Do not touch

The basses' and celli's repeat dips and beat gaps with the CC16 resets; the re-bow fills (celli chorale re-bows 0.5 to -0.9 dB); the one-row theme spans and `steady_leads.json` (only the timing and size of the level steps change); the brass accent shape on Trombone 1 and Bass trombone (fronts 2.0-3.2 dB over plain) and the absence of a 2-5 kHz burst on every brass accent; Bassoon 1's, muted Trumpet 1's and Trumpet 1 984-1000's fitted shapes; the 592 sfp notch and fronts; bar 222 / 245 fronts; the violas' repeats in 223-234 and 247-270 (9.6 / 6.9 dB); brass repeats in the chorale and coda 1 (medians 4.0-13.8 dB); the c15 release fades; every closed item of the task (brass legato velocity cap, keyswitch 0.15 s on legato rows, 315 Hz hump, "Sus Accent MAX" on brass, "Leg Slur Exp" on cor anglais and Oboe 1, `KS_LEAD_S` 45 ms, `END_LEG_KS`, solo return sends, a drier mix).

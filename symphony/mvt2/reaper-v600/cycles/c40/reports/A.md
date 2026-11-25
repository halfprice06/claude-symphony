# Cycle 40, critic A: articulation and phrasing (on the c39 render)

## Inputs and methods

- Render: `cycles/c39/render/` (master and 32 stems), `cycles/c39/rendered_build/parts.json`, `mix.json`, `score_config.py`, `cycles/c39/CHANGES.md`, `cycles/c39/reports/A.md`.
- Also read: `build/mockup-events.tsv`, `build/rebow_fills.json`, `tools/score_to_parts.py`, `tools/fit_rebows.py`, `v600/sections/coda.ily` and `aTwo.ily` (harp), and `loop/ONE_TIME.md`. Movement I's `STR_REP_NEW_BOW` was read in `symphony/mvt1/reaper-v621/tools/score_to_parts.py` (the classification pass, lines 2317-2357) and its `cycles/c44/CHANGES.md` item 3.
- Manual: May 2021 HO manual, PDF pp.68-71 (row A6, cycle 40), read in full; `loop/MANUAL-GAPS.md`.
- Levels are stereo-power RMS on the stems in dB.
- **Own-pitch level** is the energy of a note's 1st and 2nd partials (±3 %) in 40-60 ms FFT windows. It separates a note from the other notes of the same section and from the rest of the master.
- **Repeat measure (S1):** dip = median level over -0.45..-0.15 s minus the minimum over -0.12..+0.12 s; re-attack = maximum over the next 0.35 s minus that minimum.
- Positions are score qn on the c39 tempo map.

## Manual notes (A6, PDF pp.68-71: Hollywood Harp)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| The harp has solo-instrument mics: Close, Mid, Main, plus vintage Close/Mid in place of Surround (p.68). | Harp and Harp harmonics tracks (group mics Close 0.6 / Main 1.0, send 0.3). | Yes. Main exists on the harp, so the harp reaches the hall like the orchestra. |
| Maestro, Angels and the Bisbigliando combos pick articulations by velocity or CC1 (p.68-69). | Not used. Harp Maestro has no samples below MIDI 48 (kit §9). | Correctly not used. |
| Sustain RR alternates Pluck Long (RRx1) and Thumb Pick (RRx2) at v1-123, 5 dynamic layers each. Nail Pick plays at v124-127. CC11 and velocity set loudness (p.69). | Harp track, `Harp Sus RR.oib`, 158 notes. | Yes (measured). Velocities are 44-104, so no note reaches the nail pick. CC11 is fixed at 110 and dynamics come from velocity (kit §9). The bar 53-55 same-pitch replucks (0.67 qn apart) alternate the two round-robin samples, so no "machine gun". |
| Harmonics: a separate patch with 2 velocity layers, no fundamental, a hollow sound (p.70). | Coda, bar 83 (qn 274/275.5/276), "dolce, harm., L.H. (sound 8va)", p. | Yes (measured). The Harp harmonics track plays the sounding pitches A flat 4 / C5 / E flat 5 (68/72/75). Energy sits at those pitches, not an octave lower. The three own-pitch peaks are within 1.7 dB of each other at v58/58/70. |
| Pluck (5 layers), Thumb Pick, Nail Pick, Pres de la Table, Gliss Technique, Double Hit, Bisbigliando, FX/Gliss (p.70-71). | v600 prints no près de la table, glissando, bisbigliando or grace notes for the harp. | Not applicable. |
| Repetition Rep: repeated notes ring their full length without the machine-gun effect (p.71). | The only same-pitch replucks are 0.67-1 qn apart (bars 53-55, bar 11). | Not needed at these speeds. |
| "R.H. étouffez" (score, coda.ily c406): damp at 83 b1 the strings plucked at 82 b2-3; the A flat 1 is tied into 83 (let ring). | Harp 272-274. | Yes (measured). F4 falls 15 dB in 0.1-0.2 s after 274 (release 200 ms). The tied A flat 1 rings on with no re-pluck: the 271 note's 7.76 qn length is the score's tie, not a dropped note. |
| Rolled chords from the bottom (kit §9: 40 ms per note at mp or softer). | 29 rolled chords. | Yes (measured). 40 ms per note. |

## Findings, ranked by what a listener would hear

### 1. Violins I's re-entry at bar 25 (qn 72): its own C5 arrives 0.34 s after Violins II's, in unison, at the start of the theme. Cause: the "tutti" text makes the bow change start on Leg Slur MAX's slow first-note layer (measured; cause read in the code)

**What the parts show (read, parts.json).**
- Violins II plays 71 -> 72 as a Leg BC MAX bow-change target with overlap.
- Violins I's 71 note (Leg BC) ends at 71.794. Its 72 note starts at 71.824 on a fresh `Leg Slur MAX` keyswitch, with no overlap. That is the first-note layer, not a transition.
- parts.json `bc_skipped` = [72.0, 249.0] on Violins I. The skip comes from the c09 rule in `score_to_parts.py` (about line 2147): a "tutti"/"solo" text at the onset means "different players". The rule was written for qn 65, where the solo ends and the section enters. At 72, "tutti, con sord." only marks the leader rejoining. The section was already playing bars 23-24 and changes bow here.
- This is why c39's `VEL_SET` v124 had no effect (c39 measured +0.12 -> +0.20 s broadband). Velocity sets legato transition time, and here there is no transition.

**Own-pitch measurement (C5 partials, measured).**

| Track | Own-pitch body | Reaches body - 6 dB at | Notes |
|---|---|---|---|
| Violins I | 25.6 | +0.32 s | A short burst at -0.24 s (the note-on, led by c35's `REATTACK_LEAD_AT` 0.20 s), then 12-20 dB under body until +0.30 s |
| Violins II | 21.8 | -0.02 s | |
| Master | n/a | +0.08 s, then a second rise at +0.32 s | |

- Violins I is 3.8 dB louder than Violins II, so the master's C5 rises in two steps: a smeared, doubled attack on the theme's first note.
- The JOIN_NOTCH `(71.90, 72.08, -4.5)` on Violins I lies inside that hole.

**Fix (`build/score_config.py` and `tools/score_to_parts.py`).**
- Add a generic `BC_NEWP_KEEP = {}` (default empty). In the c09 `newp_` test, ignore the text when the onset is listed. In movement II's config: `BC_NEWP_KEEP = {"Violins I": [72.0]}`.
- Then 72 is a Leg BC MAX target with LEG_OVERLAP from 71, and its keyswitch back to Leg Slur moves to 73.35, as Violins II's does.
- Remove `REATTACK_LEAD_AT["Violins I"][72.0]` (0.20).
- Remove the Violins I JOIN_NOTCH `(71.90, 72.08, -4.5)`.
- Keep `VEL_SET["Violins I"][72.0] = 124`: it now sets the BC transition, like Violins II's v124. Let the normal BC leg lead apply (Violins II's is 0.15 qn).
- Leave 249.0 alone: a wide-leap skip there is right.

**Target.**
- Violins I's own-pitch C5 at body - 6 dB within ±0.05 s of Violins II's.
- No burst before the beat.
- Master C5 reaching body - 3 dB in one rise by +0.12 s.

### 2. S1 string repeats, and what ONE_TIME's `STR_REP_NEW_BOW` would and would not do for each flagged one (measured; coverage read in the movement I code)

**What the rule covers (read).** Movement I's classification acts only on a same-pitch pair that the legato merge would join, both notes on a legato row (`_lg(art)`), monophonic. Each repeat becomes one of three classes:
- **stroke:** accented, base CC >= mf 72, last mark >= mp, or a slur head at p or louder;
- **portato:** a slurred tenuto;
- **soft:** everything else. The merge stays, and a re-bow point at the printed onset replaces the CC11 notch.

Sus MAX -> Sus MAX repeats are reached only by `sus_min_s`, at mf or louder and 0.4 s or longer. Flautando notes are never reached.

**The flagged repeats on the c39 render.** Own-pitch values are stem / master, dip and re-attack in dB. The c39 actor's broadband numbers are in `cycles/c39/CHANGES.md`.

| Repeat | Printed | Now (parts.json) | Own-pitch dip / re-attack | STR_REP_NEW_BOW | What else it needs |
|---|---|---|---|---|---|
| Violins II 289 (A flat 4) | pp con sord., separate | `REBOW_AT` piece **and** a CC11 notch 34 -> 26 (c39 removed it from NOTCH_SKIP) plus a fitted fill | stem 0.2 / 0.1, master 0.6 / 7.4 | soft: a re-bow point at 289, which it already is. No change. | (a) Drop the notch: put 289 back in `NOTCH_SKIP`, or let the rule replace it. (b) A fill that does not flatten the bow change (below). The 286 body falls 6-7 dB over the last 0.5 s and the new piece settles 2.5-3.4 dB under it (step -3.4 dB, measured). This reads as a fade, not a new bow. |
| Violins II 292 | pp, tied on ("change bow at will") | merged, `MERGE_NOTCH_AT` 12. Automatic re-bows at 290.9 and 293.0 sit 1.1 qn before and 1.0 qn after it. | stem 4.3 / 3.1, master 2.9 / 10.3 | soft: a re-bow at 292.0 | Remove `MERGE_NOTCH_AT["Violins II"][292.0]`. Remove the 290.9 and 293.0 points and their `rebow_fills.json` rows: three bow events in 2.1 qn. The tied 292-304 already has points from 295.8 on. |
| Violas 62 (A flat 3) | pp, unslurred | merged into 60 on Leg Slur MAX, notch 16 (c39, no measured effect) | stem 3.4 / 6.5, master 0.0 / 9.1 | soft: a re-bow at 62 | Remove `MERGE_NOTCH_AT["Violas"][62.0]`. The 60-63 note is 3.4 s long, so no loop point conflicts. |
| Violas div 70 (A flat 4) | p, unslurred | merged into 69 on Leg BC MAX, notch 16 | stem 2.4 / 0.0, master 2.2 / 0.3 | soft: a re-bow at 70 | Remove `MERGE_NOTCH_AT["Violas div"][70.0]`. |
| Violas div 79 (E flat 4) | p < | merged into the 78 Leg Slur MAX v53 note. No notch: the notch path does not see it. | stem -2.7 / 3.5 (the cresc rises through it) | soft (CC 53 < 72), **if** the classification pass sees the 78/79 pair on the split track | Check that parts.json `rep_rebows` on "Violas div" lists 79.0. If not, add `REBOW_AT["Violas div"] = [79.0]`. |
| Violas div 289 / 292 (A flat 3) | pp, same case as Violins II | merged. Automatic points at 287.3, 288.6 and 291.7: five bow events in 286-292 where the score has three, none on the printed bows. | 292: stem -3.0 / 5.2. Steps at 288.6 -2.4 dB and at 291.7 **+4.6 dB** (200 ms, measured). | soft: re-bows at 289 and 292 | Remove 287.3, 288.6 and 291.7 with their fill rows. 286-289 is about 3.5 s and needs no loop point. Keep 295.3 onward. |
| Double basses 144 (B flat 1) | pp, new slur head (144-146) | **not merged.** A Leg Slur MAX note after the 0.06 qn re-tongue gap, so it plays the first-note layer. | stem 3.1 / 2.3, master 1.4 / 3.1 (no attack; the level falls after the onset) | **not covered**: no merge, not Sus -> Sus | Play it as a fresh Sus MAX stroke that 146 joins from: `DOWNBOW_STROKE_AT["Double basses"] = [144.0]` (the path exists, empty, at score_config line 638). Remove 144 from `REP_RETONGUE_AT` and from the c39 CC7 fall. |
| Double basses 156 / 168 / 253 | pp, pp, p < (CC 40 / 40 / 60) | Sus MAX -> Sus MAX with a 0.06 qn (about 0.07 s) gap and the c39 CC7 fall 127 -> 100 | 156 2.4 / 6.5 (re-attack peaks at +0.14..+0.2 s), 168 -2.8 / 1.2, 253 -2.3 / 2.9 | **not covered**: `sus_min_s` needs >= mf. Their gap is already longer than its 0.06 s. | ONE_TIME's 150 ms Sus MAX release cap is the first fix: c39 showed that the gap and a post-note CC7 fall do nothing while the 323-931 ms release fills the gap. Also give them `STR_REP_NEW_BOW`'s `sus_lead_s` 0.10 s (S2: the 156 re-attack is late). Easiest: `sus_min_s` with a per-track `stroke_cc` override `{"Double basses": DYN["pp"]}`. Remove the CC7 falls at 144/156/168/253/265 (no measured effect). |
| Double basses 265 | ff | Sus MAX, re-tongued (0.06 qn) | stem 2.5 / 9.6. Separated. | covered by `sus_min_s` (gap and lead) | Keep the longer of the two gaps (REP_RETONGUE's 0.06 qn), so the onset is not handled twice. Re-measure the lead. |

**Other repeats the rule would reach (scan of all 57 printed untied string repeats).**
- **Soft:** Violins II 144 (merged, notch 9, plus an automatic point at 142.89; stem dip 3.5, re-attack 1.5). Also Violas 50/69/71/87/248.5/253/271/283, Violas div 82/267, and Violoncellos 148.
- **Strokes:** Violoncellos 128 (p slur head).
- **Portato:** Violins II 44/50.
- **Violoncellos 66.** The "unis., cantabile, sul D" first note of the bars 23-28 counter-melody is merged into the held E flat 3 with no notch (stem dip -2.2). The rule would make it soft (p, not a slur head), but it starts a phrase: list it as a stroke, `DOWNBOW_STROKE_AT["Violoncellos"] = [66.0]`.

**The fill target is the second half of the fix (inferred from the fit code and c39's 289).** `fit_rebows.py` fills each piece back to the level before it over 0-1.5 s. That is right for hidden loop re-bows, but it erases the printed bow changes that S1 wants heard: the 289 fill +5.7 dB at +0.36 s left a 0.1 dB re-attack.
- For every printed-bow point (the rule's `rep_rebows`, Violins II 289), pass `--skip "Track:qn"` to the refit that ONE_TIME item 2 asks for.
- Then add a hold-only row: `[[-0.04, 0], [0.25, 0], [0.45, H], ...]`, where H = (previous body - new body), measured 0.5-1.5 s after the point.
- Target at printed bows: a 3-5 dB stem dip with the new stroke back at the old body level within ±1 dB by +0.4 s. Movement I's soft re-bows reached a 3.9 dB median.

### 3. Violins II sul tasto, bars 37-40 (qn 108-124): six printed half- and quarter-note repeats play as merged notes, with bow changes at loop-driven places 0.3-0.9 s off the printed bows (measured positions; audibility inferred)

**Score.** pp, "div., sul tasto", unslurred, under Flute 1's dolce cantabile theme:
- upper voice: B flat 4 at 112 / 114 / 116, and F sharp 4 at 118 / 119 / 120;
- lower voice: C sharp 4 at 108 / 112, and D sharp 4 at 119 / 120.

**Render (parts.json, Flautando on both tracks).**

| Track | Printed bows | Rendered bow events (offset from the nearest printed bow) |
|---|---|---|
| Violins II div | 114, 116, 119, 120 | 110.053, 113.7 (-0.30 s), 116.097 (+0.10 s), 119.877 (+0.88 s), nothing at 120 |
| Violins II | 112, 120 | 111.198 (-0.79 s), nothing at 120 |

- At the printed onsets: Violins II 112 own-pitch stem dip 2.4 dB (master 1.0); 120 0.4 dB; Violins II div 120 0.7 dB.
- The half-note pulse of the accompaniment becomes a drone whose bow changes fall off the beat.
- `STR_REP_NEW_BOW` does not reach these notes: Flautando is not a legato row.

**Fix.**
- `REBOW_AT["Violins II div"] += [114.0, 116.0, 119.0, 120.0]`.
- `REBOW_AT["Violins II"] += [112.0, 120.0]`.
- Remove the automatic or moved points 110.053, 113.7, 116.097 and 119.877 (Violins II div) and 111.198 (Violins II) with their `rebow_fills.json` / `rebow_moves.json` rows. At q=60 the printed pieces are 1-2 s long and need no loop points. Bar 37's 4 qn notes are 4 s, under the 4.5 s limit.
- Fit as in finding 2: printed points skipped, hold only.

**Target.** A 3-4 dB own-pitch dip at each printed onset, none between them, and no step over 2 dB.

### 4. Trombone 1, bar 63 (qn 215): the second note of the ff marcato slur still sags 4-5 dB under the slur head (measured)

**Evidence (0.125 qn windows).**
- Levels: 214.625-214.75 at -20.3/-20.2 dB, then 214.875 at -25.3, 215.0 at -24.2, 215.25 at -22.8.
- In the first 300 ms, 215 sits 4.4 dB under the 300 ms before it. Its 2-5 kHz attack minus body is -1.4 dB: a brighter front on a weaker note.
- Cause (read). `LEVEL_SHAPES_S["Trombone 1"]` (c36 A #4, score_config line 682) holds 214.5 at +4.0 dB to 0.40 s and ramps it to 0 at 0.50 s, which is exactly where 215 starts (214.91). 215 gets only +1.5.
- The accents are right (measured):
  - 213: +2.5 dB over its pickup, 2-5 kHz attack minus body -9.1 dB, master 2-5 kHz jump -4.9 dB;
  - 218: +3.3 dB, -18.5 dB, -4.1 dB.
  Both give weight without bite (BRIEF item 9).

**Fix.** In that block:
- 214.5: `(0.04, 4.0), (0.40, 4.0), (0.50, 0.0)` -> `(0.04, 2.5), (0.40, 2.5), (0.50, 0.0)`.
- 215.0: `(0.03, 1.5), (0.50, 1.5)` -> `(0.03, 2.5), (0.50, 2.5)`.
- Keep the CC7 floors 110/120 and the accents.

**Target.** 214.5, 215 and 215.5 within 1.5 dB of each other in 0.125 qn windows, and no step over 2 dB at 214.9.

### 5. Brass tenutos of bar 62 (qn 208), molto sostenuto ff: the horns' tenuto notes are not re-articulated (measured on the stems; masked in the master, inferred)

**Evidence.** Re-attack at 208 (50 ms):

| Track | Re-attack at 208 | Notes |
|---|---|---|
| Horn 1 | -0.1 dB | Sus MAX, starting 0.02 qn after the 204 note ends, which is too short a gap to hear |
| Horn 2 | 0.9 dB | same-pitch D flat 4 (c39 A #5, still open) |
| Horn 3 | 1.5 dB | |
| Trombone 2 | 2.2 dB | |

Bass trombone (23 dB) and tuba (20 dB) do re-attack. The printed tenutos are unslurred, so they are separate tongued notes at full length. Horn 4 doubles Horn 3 and is dropped as a unison (kit §8), which is correct.

**Fix.**
- `REP_RETONGUE_AT["Horn 2"] = [208.0]`.
- For Horn 1 and Horn 3 at 208 and 210, end the previous note 0.06 qn early: the same re-tongue path, which is not pitch-gated in `build_track`. If it is, add a `SUS_GAP_AT` list.
- Lower priority than 1-4: the ff tutti covers it (master dip 0.9 dB at 208).

### 6. Breath before the climax (qn 204): the bass trombone takes 0.03 s and Trombone 2 0.08 s, where every other wind takes 0.14-0.18 s (measured; small)

**Evidence.** These are the gaps between the 200/202 notes' ends and the 204 onsets on the stems' MIDI, on the c39 map with the 0.10 s caesura. The breath mark is printed in both parts.

**Fix.** End the bass trombone's 200 note and Trombone 2's 202 note at the same time as the other brass. Find what sets these two note ends (parts.json `breath_splits` / `end_at`) and match Tuba's 0.176 s gap.

## Checked and fine (measured)

- **No legato chords.** No simultaneous onset and no overlap over 0.35 qn on any Leg row, on any track.
- **No loop pulse.** Autocorrelation at 3.95 s of the 100-300 Hz band and of the centroid is at most 0.23 on: the final chord (master and every string stem, 292-304), the basses' 4 soli pedals (220-238, 286-304), Violoncellos div 274-286, and the opening chord (0-9).
- **Re-bow dips.** All 87 string re-bows are at 5 dB or less in 200 ms windows, except Violins II 289 (7.7, finding 2). The steps over 3 dB are the coda points in finding 2, Violoncellos 223 (the printed bar 66 niente) and the morendo pieces 302-303.3.
- **Viola portato, bars 48-51.** On Detache, each of the 15 notes rises 9-23 dB from the gap, and b-6 is within -0.06..+0.06 s of the score onset. These are separate pressure strokes on the beat.
- **Pizzicato, tremolo entries, CC15.** As c39 found. The mutes (on at 9.5, off at 90.5, coda 268.5-274.5) change only in rests, and the score's later senza sord. points (108, 124, 171) fall in rests for those tracks.
- **Timpani.** Strokes at the tied roll ends 203 and 209.5 play on Flt Lng.

## Do not touch

- The harp setup: Sus RR, velocities 44-104, CC11 110, env_sustain 1.0 / release 200 ms, 40 ms rolls, the tied A flat 1 at 274.
- Harp harmonics on sounding pitch.
- The violas' Detache portato and its leads.
- Trombone 1's velocities, accent swells, CC7 floors 110/120 and the 218 accent. Change only the two shapes in finding 4.
- Every loop re-bow point not named in findings 2-3, including the final-chord points of Violins I, violas, celli and basses, the bar 66 down-bow re-bows and the opening chord.
- The bars 61-64 tremolo rows.
- The basses' re-tongue at 265.

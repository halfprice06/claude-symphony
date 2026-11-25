# Cycle 15: changes (actor, on the c14 render)

Snapshot before this cycle: `cycles/c15/before/`. Scripts: `cycles/c15/actor_scripts/` (`tag15.py`, `patch15a.py`,
`patch15b.py`: the one-off edits of `tools/score_to_parts.py`; `apply15.py`: table edits, run once; `envstats15.py BUILD`:
envelope statistics; `resid15.py`: which layer makes the remaining swing; `sim15.py NEW_BUILD`: a new envelope simulated
on the c14 stems; `simpchk15.py BUILD`: the simplification pass against the full envelope; `pcmp15.py OLD NEW`: parts.json
diff; `mkvtest.py`, `wholepass15.py`, `vt15.py`, `adopt15.py`, `refit15.py`: the lock-phase tests; `divenv15.py`: stems
with the envelope divided out; `lk.sh`, `wait_lock.py`). Records: `cycles/c15/records/`.

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB unless noted.

STATUS: rendered once on 2026-11-11 (12:04-12:20 CST, freshly restarted REAPER, 43-44 GB settled, 0 GB compressed
before the render; 50 GB / 32 GB compressed after it). No stem fix. Lock held 11:13:24-12:22:49 CST (69.5 min, of which
about 20 min idle on a usage limit) after waiting from 07:50 behind Movement II, Movement I and the finale.
mp3: `cycles/c15/scherzo-mockup-c15.mp3`. Data as rendered: `cycles/c15/build_render/`.

**For c16, first thing under the lock:** the saved project holds 4 stale Opus states after the render (Flute 2, Horn 2,
Horn 4, Violins I: `records/state_guard_final_save.txt`); run `tools/state_guard.py` and rebuild them.
**Not deleted (refused by the session's permission check, not retried):** c14's stems (2.8 GB), `cycles/c15/rangetest/`
(1.4 GB of test-pass WAVs), `Backups/` (0.9 GB). 59 GB free.

## Result in numbers

| | c14 | c15 |
|---|---|---|
| master | -20.8 LUFS, LRA 22.7, TP -1.5, sample peak 0.835 | -21.0 LUFS, LRA 22.7, TP -1.4, sample peak 0.840 |
| delivered mp3 | -19.8 LUFS, LRA 14.9, TP -1.5, limiter 3.0 dB, span 19.8 | -19.8 LUFS, LRA 14.8, TP -1.6, limiter 2.4 dB, span 19.1 |
| attack probe | late or hole 0 | late or hole 0 |
| volume envelope: points / per note / per second (31 tracks) | 40,724 / 7.1 / 146.6 | 4,545 / 0.8 / 16.4 |
| notes with over 3 dB inside (moved note-on to note end) | 22 % | 6 % |
| notes with over 3 dB strictly inside (from 40 ms after the score onset); of these without accent, hairpin or dynamic change | 598; 310 | 156; 57 |
| out-and-back excursions of 3 dB within 0.25 s | 635 | 67 |
| master level per section against c14 (15 sections) | | within 0.3 dB |
| stems per section against c14 | | within 1.0 dB except: Cor anglais bars 57-104 +2.6, 121-140 +3.0, 301-324 +1.6; Trombone 2 105-120 -2.0 (B #4, intended); Timpani 13-56 -1.4, 209-224 +1.8, 325-340 -1.6; Flute 1 57-104 -1.1; Bassoon 1 341-376 -1.2 |
| measure S, `timing13.py`, outside 25 / 60 ms | 26 % / 5 % (envelope divided out: 26 % / 6 %) | 26 % / 5 % (envelope divided out: 26 % / 6 %) |
| legato joins outside 25 / 60 ms (`s14.py`): Violins I, Violins II, Violas, Violoncellos, solo | 9 / 3 of 100, 43 / 13 of 104, 33 / 3 of 67, 24 / 9 of 200, 3 / 0 of 18 | 10 / 3, 41 / 11, 32 / 3, 28 / 7, 3 / 0 |
| hall: G.P. drop at +0.3 s, 20 dB fall, RT60; final chord | 20.7 dB, 0.24 s, 1.30 s | 20.8 dB, 0.24 s, 1.30 s; 20.7 dB, 0.25 s, 1.32 s |
| soft ends | 0.06-0.22 s | 0.06, 0.22, 0.11 s (`records/hall14_c15.txt`) |
| returns re dry | -12.81 dB | -12.74 dB |
| REAPER memory | 43 GB settled | 43-44 GB settled, 0 compressed; 50 / 32 after the render |

## Dan's decision during the cycle (2026-11-11 16:30Z): no per-note volume moves

"yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways
to fix our problem." The cycle's first half (below, "Main subject") cleaned the per-note layers; this decision then took
them all off the fader. What is rendered:

- `build/score_config.py` `VOL_CLASSES = ("slow",)` (new generic option): the track volume envelope holds roles, hairpin
  gains, timpani roll shapes, arrival weights, held decrescendos, the fade, single-level `LEVEL_SHAPES` rows of a bar or
  more (`LEVEL_ROW_SLOW_QN` 3.0: 14 rows) and the unison boost as role spans (`UNI_BOOST_AS_ROLE`: 26 spans), plus the gain and
  the dynamic trims of `build_reaper.py`. No pitch, row or note trim, no accent swell or body, no fill, notch, dip,
  release, re-bow fill, beat weight or timpani spike is played. They are still computed and stored in parts.json
  `vol_cls` / `vol_tags` as the record (`records/per_note_layers_not_played.json`).
- Moved to the instrument side:
  - per-pitch sample-level corrections (`build/pitch_trims.json`, 14 tracks, was 574 envelope items) are per-region
    volumes in the Opus state (`tools/build_reaper.py region_gain`, `mix.json` `region_gain_db`; `PITCH_TRIM_IN_OPUS`).
    Whole-piece pass and render against the simulation target (c14 stem x new envelope with the trims): notes off by
    more than 1 dB / 2 dB: Oboe 2 0 / 0 of 36, Trumpet 1 0 / 0 of 63, Oboe 1 10 / 3 of 304, Flute 1 24 / 9 of 371,
    Clarinet 2 18 / 6 of 234, Cor anglais 20 / 16 of 219, Flute 2 35 / 10 of 162, Clarinet 1 90 / 33 of 263 (12 of them
    its former skip onsets, +3.5..+3.8), Horn 4 22 / 2 of 88, Horn 3 46 / 9 of 141, Horn 2 69 / 13 of 158, Horn 1
    87 / 28 of 154 (these counts include a constant -0.3..-1.2 dB of the check's mono sum). State guard clean after
    the builds;
  - Violins I "Sus Marc LITE" row -8 dB in the Opus state (`row_db`) in place of the nine theme-head level rows and the
    hemiola rows' 8 dB: pair body / landing staccato c14 -> c15 (dB): 41: -38.5, -39.3 -> -39.7, -40.1; 53: -43.2,
    -42.4 -> -41.9, -38.5; 287: -43.6, -43.3 -> -40.3, -40.5; 773: -41.4, -42.2 -> -41.5, -41.2; 791: -36.8, -37.0 ->
    -36.8, -42.1. Landing pitch over the second eighth's pitch at +20 ms: positive in 7 of 9 figures (c14 2 of 9);
  - string short rows back on their printed CC11 (`SHORT_CC11_PARK` None; the park's return carried 2-8 dB per section
    on the fader): string stems within 1.0 dB of c14 in every section;
  - timpani loud single strokes: velocity +22 (`TIMP_LOUD_VEL_ADD`), no spike: level over 20-170 ms -1.1 dB (median,
    83 strokes; 10th..90th -2.5..+0.8), peaks -1.6 dB, tuttis -0.3 / -0.5 dB, coda -1.7 dB; but the 2-5 kHz share of the
    first 80 ms rose 5.0 dB (median; B's limit was 3): harder strokes. For c16: +14 and a role (B's fallback);
  - passage constants in `build/roles.json` where a per-note level carried a section's balance (flutes and oboe in the
    two tuttis, the coda build's woodwinds and inner strings, Clarinet 2 552-624, Violins II "la meta" 1044-1068,
    Violas div. 624-672 and double stops 360-420, celli 552-624, basses 504-552, Violins I 1089-1128).

### Per-note layers no longer played, and the faults left audible (for cycle 16, instrument side only)

| layer (items; tracks) | what is audible without it (measured on the c14 stems with the layer divided out, or on the c15 render) |
|---|---|
| accent swells 235 and bodies 61 (strings 134, Flute 1 22, Oboe 1 22, cor anglais 14, clarinets 17, others) | printed accents carry no level of their own: accented note over the note before +2.5 -> +0.1 dB (violas), +2.1 -> +1.2 (Violins II), +0.8 -> -2.0 (Oboe 1) (critic A #6). Coda woodwinds held by roles only. Instrument side: CC11 headroom (finale c17: lower the resting CC, accents at 121-124 for 0.15 s) |
| note trims 133 (basses 49, violas 27, celli 12, Clarinet 1 11, Flute 2 10, Violas div 7, Clarinet 2 6, others) | single notes 3-8 dB off their line again, among them this cycle's B #5: Double basses D2 / E2 at qn 138 / 140 (-7 / -10 dB under their neighbours), 642 (-14.5 dB), G1 at ff +3 dB over E1; Clarinet 1 243 / 735 / 904, Bassoon 1 699 / 702, Oboe 1 1036 (c14 C #4) |
| row trims 119 (Oboe 1 25, celli 23, violas 18, Flute 1 16, Violins I 13, Flute 2 12, Violins II 12) | loud Sus MAX / staccato notes 3-5 dB over the legato row beside them (strings); flute ff staccatos 6 dB weaker against their slurred notes (the tutti level is in a role) |
| early fills 66 (celli 22, Bassoon 1 15, Clarinet 1 11, Oboe 1 5, others) | soft phrase heads speak 100-200 ms late again (critic C #6: celli 504 +140 ms with, +243 without); step medians: Oboe 1 672-708 3.0 -> 4.8 dB, Clarinet 1 672-708 2.0 -> 4.0, 624-672 4.0 -> 5.1 |
| level rows 55 with several levels or under a bar (Violins I 19, Timpani 11, celli 7, Horn 1 5, others) | Violins I 155.5 pickup +8 dB; the timpani's p-solo first-stroke steps (bars 9-12); celli row-level steps on former Leg BC notes (single notes 3-6 dB softer); Violins I sfp at 900 is 8 dB softer (the row gain) |
| timpani metric table 42, attack shape on 3 rolls | stroke-to-stroke step 2.1 -> 2.5 dB (A); f rolls start without their +6 dB |
| wind / brass detach dips 39 (horns 25, low brass 11, trumpets 3) | slurred or tenuto repeats separate less (S1): to check on the c15 stems; instrument side: gap floor 0.09 s brass, 0.065 s winds (finale c17) |
| re-bow fills 9 (Violins I 4, celli 3, Violins II 1, violas 1) | a dip at each re-bow of the held notes (Dan's note 8): 5.5 dB at the last one in c13; Violins I's ppp G sharp of bars 364-376 is the exposed case |
| join notches 5 (celli 4, Clarinet 1 1), releases 14, chord cuts, bloom 1, swell 1 | transition bumps of 4-7 dB at celli 506 / 570 / 764 / 800 and Clarinet 1 459; violas' non div. double stops +1.5 dB (bars 105-120, 305-320) |
| region gain misses | Cor anglais A4: +2.6..+3.0 dB over bars 57-104 and 121-140 (the -3.5 dB correction does not reach its notes); horns: 10-18 % of notes 2-5 dB under the target (legato-joined notes); Clarinet 1's 12 skip onsets +3.5..+3.8 dB |



## Main subject, first half of the cycle: the per-note layers cleaned (superseded on the fader by the decision above; the tools stay)

"How much the volume adjustment was adjusted in large peaks and valleys on so many individual notes, even with fast
successive notes volume peaks up and down every note. To me it seemed unnatural."

### What was done

| item | change (files, parameters) |
|---|---|
| 1. three classes | `tools/score_to_parts.py`: every `vol_parts` item is added with `vol_add("class:layer", item)` (61 call sites; `tag15.py` lists which site got which tag). Classes: slow (roles, hairpin gains, timpani rolls, arrival weight, held decrescendo, fade), level (pitch, row and note trims, park return, level rows, chord cut, unison boost, metric table), shape (accents, accent bodies, fills, notches, detach dips, releases, swells, timpani attack, beat weight). parts.json per track: `vol_cls` (three step lanes whose sum is `vol_db`), `vol_tags` (items per layer), `accent_q`; with `STP_LAYERS=1` also one lane per layer (`vol_layers`). `tools/build_reaper.py vol_points`: `ENV_SHAPE=off` / `ENV_SHAPE=capN` writes the envelope without the shape class or with it limited to N dB (for tests). With no option set the retagged tool reproduced c14's parts.json exactly (31 tracks, 0 differences) |
| 2. one level per run | new generic `ONE_LEVEL` (off by default; scherzo: notes whose sounding length or slot is 0.55 qn or less): the listed per-note layers get one value per note (the mean of the built lane at 20 / 40 / 60 % of the note), held from the join with the note before to the join with the note after; equal neighbours make no point. New generic `ROW_TRIM_HOLD_QN` (1.0): a row trim holds through the gaps of a run. New generic `TRIM_STEP_S`: pitch trims, row trims and note trims listed with a ramp of 0.05 s or less are flat levels with a 40 ms step |
| 3. shapes | beat weight off (`SHORT_CC11_PARK["beat_db"]` None: 342 steps); `GENTLE_ACCENT` wind 3.5 -> 3.0 dB and new generic `ACCENT_SWELL_MAX_DB` 3.0; inside notes of an eighth or less accents, accent bodies and trims are one level (`ONE_LEVEL` tags). Shape class kept otherwise (test below) |
| 4. steps that cut the note before | `join_ramp` (new, used by `ONE_LEVEL` and `TRIM_STEP_S`): when the note before ended 60 ms or more before the moved note-on, the step ends at the note-on; otherwise (an overlap, or a wind legato whose MIDI gap is a few ms) it is centred after the next note's SCORE onset: +10 ms, Clarinets +50 ms (`TRIM_STEP_S["center_by"]`), short notes +5 ms. c14's row-level steps on consecutive notes are one line (17 rows in 7 lines on the celli); Violins I's 155.5 row starts on the score onset |
| 5. theme head | the nine figures of Violins I: one row per figure in C's form (`build/score_config.py`, c15 block): the half note's body level runs to the first eighth's note-on (q - 0.40) and crossfades to the eighths' level by q - 0.20; the lift `u` is dropped; the landing staccato keeps c14's level without the beat weight |
| 6. stairs | new generic `VOL_GRID_QN` (0.125, build_reaper's own grid: slow ramps are no longer 0.25 qn stairs) and `mix.json` `env_simplify_db` 0.1 (`env_simplify_max_seg_db` 4): Douglas-Peucker on the written points, the distance taken in REAPER's fader scale over seconds |
| 7. timpani | new generic `TIMP_LOUD_VEL_ADD` (22, cap 125, worth 3 dB): 83 loud single strokes take velocity +22 instead of the +6 dB spike; 4 strokes whose velocity the cap clipped get the rest as one flat level; the 3 rolls at f keep their attack shape |

### Result on the written envelope (`envstats15.py`; `records/envstats_c14.txt`, `envstats_c15.txt`)

Three stages: c14; the cleaned per-note layers (first half; built, simulated, not rendered); slow only (rendered).

| track | c14 points / per note / over 3 dB in the note / strictly inside (unmarked) | cleaned: points / per note / over 3 dB | rendered: points / per note / per second / over 3 dB / strictly inside (unmarked) |
|---|---|---|---|
| Flute 1 | 1972 / 5.3 / 27 % / 18 (8) | 617 / 1.7 / 16 % | 296 / 0.8 / 1.1 / 9 % / 8 (4) |
| Oboe 1 | 2015 / 6.6 / 18 % / 21 (8) | 517 / 1.7 / 13 % | 211 / 0.7 / 0.8 / 5 % / 5 (3) |
| Clarinet 1 | 2281 / 8.7 / 51 % / 66 (26) | 935 / 3.6 / 41 % | 329 / 1.3 / 1.2 / 9 % / 8 (3) |
| Bassoon 1 | 1843 / 8.2 / 20 % / 23 (15) | 337 / 1.5 / 19 % | 248 / 1.1 / 0.9 / 13 % / 15 (8) |
| Horn 1 | 1249 / 8.1 / 28 % / 17 (3) | 413 / 2.7 / 23 % | 226 / 1.5 / 0.8 / 7 % / 7 (0) |
| Horn 4 | 718 / 8.2 / 50 % / 8 (6) | 249 / 2.8 / 30 % | 95 / 1.1 / 0.3 / 6 % / 0 (0) |
| Timpani | 1028 / 5.6 / 52 % / 94 (77) | 263 / 1.4 / 12 % | 97 / 0.5 / 0.3 / 8 % / 14 (7) |
| Violins I | 5538 / 10.8 / 17 % / 38 (4) | 1119 / 2.2 / 15 % | 242 / 0.5 / 0.9 / 1 % / 3 (1) |
| Violins II | 3537 / 7.0 / 12 % / 38 (11) | 653 / 1.3 / 10 % | 208 / 0.4 / 0.7 / 2 % / 2 (0) |
| Violas | 3961 / 8.0 / 23 % / 52 (28) | 1050 / 2.1 / 22 % | 247 / 0.5 / 0.9 / 5 % / 6 (0) |
| Violoncellos | 3996 / 8.7 / 22 % / 52 (33) | 1047 / 2.3 / 20 % | 351 / 0.8 / 1.3 / 9 % / 10 (4) |
| Double basses | 2045 / 6.6 / 22 % / 49 (42) | 770 / 2.5 / 23 % | 206 / 0.7 / 0.7 / 5 % / 7 (4) |
| Violin I solo | 493 / 25.9 / 5 % / 0 | 81 / 4.3 / 5 % | 80 / 4.2 / 0.3 / 5 % / 0 |
| all 31 tracks | 40,724 / 7.1 / 22 % / 598 (310) | 10,929 / 1.9 / 17 % | 4,545 / 0.8 / 16.4 / 6 % / 156 (57) |

What still moves 3 dB inside a note in the rendered envelope: hairpin gains and their releases, role edges, held
decrescendos, timpani roll shapes, the dynamic trims across printed hairpins. Leftovers to check in c16 (finale c17
#6): unison role spans that cover one or two notes, role edges and hairpin releases that step under a led note.

Definitions: "over 3 dB in the note" is c14's measure (max - min of the written envelope between the moved note-on and
the note's end). "After the join" starts 40 ms after the score onset, when the join's crossfade is over (a level step
into a led legato note lies inside the MIDI note by design); in brackets the notes among these that carry no accent,
hairpin or dynamic change. "Returns" are excursions of 3 dB or more that are back within 0.25 s.

Excursions of 3 dB or more that go out and come back within 60 ms: c14 313 (critic A, 45 ms) -> 58 on the built data.
Oboe 1 bar 105 (A's example, 0.1 / 5.1 dB per eighth): one level from 313.0 to 314.69.

What remains, by the layer with the largest swing (notes with over 3 dB after the join, built data, `resid15.py`):
pitch trims 68 (the step into a clarinet note stands 50 ms after the score onset, so it falls after the 40 ms mark:
a level step between two pitches, no shape), hairpin gains 66 and roles 26 (slow ramps under long notes), accent bodies
39 and accents 14 (printed accents), early fills 37, level rows 29 and note trims 24 (rows written for single notes by
earlier critics; the 0.6 s note-trim ramps are kept: c09 measured why), park return 13, held decrescendos 9, re-bow fills
9, row trims 8, timpani roll shapes 7, wind detach dips 6. Short notes that still move by more than 1 dB (323 of
2,283, was 763): the park return's mirror of Opus's 120 ms CC11 fade on the first stroke of a staccato run (74), level
rows (51), role edges (49), a row-trim step into a slurred-to short note (49), hairpin gains (40). Moving the park's
CC11 steps into the gaps before and after a run was built and dropped (the share stayed 17 %: the gaps are a few ms).
No level returns to 0 dB between the notes of a run any more.

### The layer test (ONE_TIME_c15 item 1), simulated on the c14 stems (`sim15.py`; the envelope is a gain after the instrument)

Median note-to-note step (0.35 s from the score onset) on critic A's 50 lines, c14 -> c15 data: 46 lines within 0.5 dB;
better by 0.5 dB or more: Flute 1 84-132 3.0 -> 2.4, Violins I 204-216 4.3 -> 3.2, Violoncellos 168-216 2.5 -> 1.9,
Clarinet 1 672-708 2.0 -> 1.5; worse by 0.5-0.7: Violins I 756-804 1.3 -> 1.9 (the downbeat staccatos lose the beat
weight; the same change improves 36-84 from 1.8 to 1.7), Oboe 1 312-360 1.7 -> 2.2 (the stem without any envelope
reads 1.5), Violoncellos 828-864 1.8 -> 2.4 and Horn 3 1020-1044 0.8 -> 1.5 (both lines' MIDI changes this cycle, so
the simulation is not valid there). Balance per track and section: every change over 0.5 dB is an intended one (brass
bars 101-104 -1.0..-1.2, Trombone 2 bars 105-120 -2.0; timpani not simulable, see the render check).

Shape class off: 6 lines worse by 0.5 dB or more (Clarinet 1 672-708 2.0 -> 3.9, Oboe 1 672-708 3.0 -> 4.7: the early
fills; Violins I 984-1017 +0.5; Clarinet 1 624-672 +0.5), 2 better (Violins I 204-216 2.5: the printed accent at 207;
Horn 3 504-552 1.8), woodwinds in bars 325-340 0.7-1.2 dB lower. Shape class capped at 3 dB: equal to the full
envelope except Oboe 1 672-708 (3.1 -> 3.7: its fills need more than 3 dB). The class stays; what was removed is the
beat weight, the movement inside short notes and the timpani spikes.

Join holes (lowest 20 ms frame against the quieter neighbour body; c14 / c15 data / stem without envelope): Clarinet 1
138: 8.4 / 2.4 / 2.4, 399: 10.2 / 4.3 / 4.7, 468: 7.7 / 2.2 / 0.3, 840: 8.6 / 2.6 / 2.2; Violoncellos 339: 3.8 / -1.7 /
-1.6, 939: 4.2 / -1.7 / -1.6, 390: 3.5 / 3.5 / 0.4, 594: 3.6 / 2.6 / 3.9; Violins I 155.5: 9.0 / 1.0 / 1.4.
Same-pitch staccato pairs (dip before the second note): Flute 1 84-132 9.6 -> 8.1, 312-360 11.4 -> 7.3, Flute 2
8.4 -> 6.6, Oboe 1 10.2 -> 9.6 (target 3-6; the envelope no longer cuts each tail), Violins I 6.0 -> 5.6, Trumpet 1
7.2 -> 7.2.
Theme head, frames -40..-20 / -20..0 / 0..+20 ms around the first slurred eighth and its body: 41: -44.4 / -36.2 /
-40.3 / -37.2 -> -45.6 / -42.7 / -41.3 / -37.1; 53: -49.6 / -37.2 / -40.8 / -41.0 -> -48.3 / -47.5 / -43.3 / -41.8;
287: -51.2 / -39.6 / -44.9 / -42.5 -> -50.8 / -47.9 / -46.4 / -42.5 (the spike is gone in all nine).

Simplification (`simpchk15.py`): 41,622 -> 10,991 points; largest difference between the two drawn curves 0.10 dB in
the fader scale used, 0.23 dB if REAPER drew lines in amplitude, 0.13 dB if in dB. REAPER's real scale was then read (`jobs/env_scale.lua` -> `tools/env_scale.json`: 716.2 at 0 dB, 483.9 at -12, 363.3 at -20, 171.0 at -40; not a power law); the pass uses that table and the rendered envelope is within 0.10 dB of the unsimplified one.

### Lock-phase tests

- A's per-region volume (item 2): tested on all 14 pitch-trim tracks at once on a whole-piece pass (V2, the first pass
  after the build discarded) and adopted (numbers above). The pass and the full render gave the same per-note readings.
- Item 5: A's rt_gain -9 dB and Sus MAX for the pair were not range-tested; the row gain of -8 dB lowers the trails with
  the row and the landing's pitch now leads at +20 ms in 7 of 9 figures. Left: Sus MAX for the pair (finale 53).
- Item 7: timpani result above (level kept, timbre harder).
- A cello and bass range pass after the restart showed that silent pizzicato notes in pass V2 (qn 18, 114, 117) were a
  loading effect of the pass, not of the region gains (all present after the restart and in the render).

## Timing (critic C)

| finding | change | result |
|---|---|---|
| C #1 Violins II / violas bars 49-52 | fallback rows in `leg_leads.json` (the full refit with `KS_MIN_LEAD_S` was not done: lock time) | Violins II 148 / 150 / 152 / 154: +91 / +114 / +58 / +73 -> +18 / -7 / +8 / +18 ms; 846 +69 -> -14; 146, 134, 374, 840 unchanged (+72, +77, +98, +66: held by the cap). Violas 146 +50 -> +17, 152 +50 -> +8. Violins II joins outside 25 / 60 ms 43 / 13 -> 41 / 11 of 104 |
| C #2 celli and Horn 3 trio tune | celli: 510's -0.115 s row removed, `LEG_MIN_GAP_AT` (new generic) 0.06 s in 504-576, v112 on 512 / 524 / 536 / 567 / 572; Horn 3: legato targets +0.05 s, re-tongued heads 0.12 s (`RETONGUE_LEAD_AT`) | celli 510 +117 -> -11, 512 +110 -> +17, 567 +106 -> -9, 572 +96 -> +2, 524 +158 -> +108 (still late: the row's limit after an eighth), 536 -5 -> +42. Horn 3 (S): 523.5 +32, 524 +70, 1022 +48, 1023 +18, 1025 +18 (c14, C's pc / xr: +60..+124) |
| C #4 | `REATTACK_LEAD_AT` Violins I 144 0.13 (realised 0.078), 385.5 / 853.5 0.085 (realised 0.051: cap), Violins II 144 0.085, Violas 855 0.11; entry extras celli 648 / 840 +0.06, Violins II 123 / 897 +0.025; Violas 828 extra removed; Violins I 855 row -0.051 | Violas 855 +68 -> +2; celli 840 +56 -> -4; Violins II 123 +62 -> +34, 897 +69 -> +18, 144 +34 -> +15; Violas 828 +261 -> +185 (back to c13's reading; the CC11 lift was not built); Violins I 144 +76 -> +70 (cap); Violins I 855 -61 -> +77: overshoot, take half back in c16; Violins I 372 +105 -> +136 (not changed, not better) |
| C #5 Flute 2 | 943.5 listed | 943.5 +113..+129 -> +74; 921.5 / 922.5 / 931.5 / 954.5 +82 / +61 / +59 / +71 (unchanged data) |
| C #6 | Violins I 624 entry extra +0.06 | no reading in `timing13.py`'s spans; unverified |
| Flute 1 qn 132 | none | +143 ms again (c14 +148): real, not a render accident; open |

## Balance (critic B)

| finding | change | result |
|---|---|---|
| B #4 bar 104 brass, Trombone 2 | `roles.json`: low-brass role from 312, Trombone 2's row removed, trumpets -1.5 in 309-312 | Trombone 2 bars 105-120 -2.0 dB (now level with Trombone 1 by B's numbers); brass bars 57-104 -0.5..-1.1 |
| B #5 basses 138 / 140 / 642, G1 | note trims written, then not played (Dan's decision) | fault left, see the table above |
| B #6 summit in the delivery | `RIDE_TRIMS` row -1 dB over 1004-1017 | delivered span 19.8 -> 19.1 dB, limiter 3.0 -> 2.4 dB |
| B #2 stairs, B #3 timpani, B #1 classes | see above | |

## Coordinator notes

- Movement II c54: `cresc_trim_hold` release 0.5 -> 1.0 s (a hold released over half a second writes an unprinted
  fall of up to 2.5 dB right after a crescendo's arrival; at 2.5 s the woodwinds, celli and basses stood 0.6-1.6 dB
  higher over whole sections on the simulation, so 1.0). RR_RESET_AT on refitted lines: not used (no refit this cycle).
- Movement II c55: the 3 dB cap is not used here; SWELL_DB (1 item), sostenuto (0), phrase tops (0), slur-pair
  releases (14) and the metric table (42 timpani items, A: it helps) are small or measured useful here: unchanged.
  No script of this cycle runs build_reaper.py past `ENV_LUA`.
- Text: `loop/BRIEF.md` and `loop/LENSES.md` corrected (brass rest in bars 289-324; the harmonic E6 on the Violins II
  "Harmonics" row).

## Rejected, deferred, left

- Not done: the Violins II / violas refit with `KS_MIN_LEAD_S` 0.15 (C #1 first choice) and RR resets; A #6 entry leads on
  accented Sus MAX notes; Violas 828 as a Sus MAX stroke with a CC11 lift; Sus MAX for the theme head's pair; any
  MANUAL-GAPS item other than the per-region volume (recorded there).
- Built and dropped before the decision: the park's CC11 steps moved into the gaps (no gain); +1.5 dB back on the
  landing staccato (step median 1.7 -> 2.3 dB); `cresc_trim_hold` release 2.5 s (sections +0.6..+1.6 dB; 1.0 s kept).
- The c14 WARN of `score_to_parts.py` (three celli early fills ramp inside a led transition) still prints; those fills
  are no longer played.
- Crescendo hold (finale 67: apply per confirmed hairpin): not reviewed beyond the release time.
- ONE_TIME_c15 item 2 (bass EQ): c14 had already removed the bells; no change. Item 3: no new rule.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ set, seats, wind send, return pans | adopted (unchanged) |
| one legato row per string line with refit (Movement I c54, Movement II c52) | adopted on Violins I, celli, solo (c14); Violins II / violas pending (per-onset rows only) |
| "EastWest's templates have no volume automation; reference projects 0.01-0.36 points per second" (ONE_TIME_c15) | adopted by Dan's decision: 146.6 -> 16.4 points per second over 31 tracks (0.3-1.3 per track), slow balance only |
| velocity for timpani stroke weight (manual p.123) | adopted (+22); level -1.1 dB, 2-5 kHz front +5 dB: reduce to +14 in c16 |
| per-region volume in the Opus state for per-pitch corrections (critic A #1a) | adopted on 14 tracks and one row (numbers above); misses on cor anglais A4 and legato-joined horn notes |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier, stays out |
| CC16 resets everywhere, delivery rise delay, CC11 -> CC1 pass 2, separate legato tracks, timpani hard sticks | pending |

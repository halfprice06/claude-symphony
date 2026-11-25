# Cycle 55, critic C: the volume envelope (references, instrument-side homes, whole-piece off / cap test), the bass, dynamics over time; on the c54 render

Material: `cycles/c54/render/` (delivered stems and master), `cycles/c54/build_fix/parts.json` (byte-identical to `build/parts.json`), `build/score_config.py`, `build/*.json`, `tools/score_to_parts.py`, `tools/build_reaper.py` (`vol_points`, source cut before `ENV_LUA`, nothing sent to REAPER), the reference projects in `/Users/gooby/sandbox/mockup-reference-cn1rc0/mockup-kit/reference/`, `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md`. Scratch (13 MB, left in place, no simulated audio kept): `/private/tmp/claude-501/mockup-loop/mvt2-c55-C/`.

Method. I ran a copy of `score_to_parts.py` in scratch (`stp_cls.py`) that tags every envelope item with the source line that adds it and writes one lane per layer; its parts.json is byte-identical to the build's, so the lanes are the real ones. Each layer has a class: slow (roles, hairpin gains, timpani dynamic trims, final fade, level shapes that span three notes or more), per-note level (one value per note), per-note shape (moves inside a note). `LEVEL_SHAPES` / `LEVEL_SHAPES_S` / `level_fits.json` rows are classed one by one from their points against the notes. The envelope is a gain after the instrument (and, since c44, before the hall returns), so a layer is removed from a stem by dividing its lane out. Simulated masters are the rendered master plus the stem differences; the hall returns are not re-simulated, so master changes are slightly understated. Per-note measures use 10 ms power frames: body (20-80 % of the note), front (first 0.35 s), join hole (mean of the two bodies minus the lowest 30 ms level within 120 ms of the join), join peak, dip inside unmarked long notes, note-to-note body step. All figures below are measured unless marked inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 55 (it ends at 47), so no page range was read. From `MANUAL-GAPS.md` and the kit, used below:

| Source | Where it applies | Render follows it? |
|---|---|---|
| HO manual p.101 (MANUAL-GAPS line 29): brass sustains take their dynamic from velocity and CC1 | horns (`CC1_DYN_TRACKS`), a home for brass shape instead of the envelope | Partly: CC1 moves 58-108 on Horn 1, shape is still in the envelope |
| p.144 (MANUAL-GAPS lines 75-78): legato velocity sets transition time, not level | early fills on legato targets cannot become velocity | n/a |
| Kit LEARNINGS section 3 (lines 54, 66): CC7 is linear amplitude inside Opus; CC11 moves 5.7 / 3.5 / 2.5 / 1.2 dB per 10 steps at CC 0-40 / 30-60 / 50-80 / 88-128 and changes the layer | CC7 can carry any exact level; CC11 carries shape with its timbre | CC7 used on timpani only |
| Kit LEARNINGS line 423: velocity does nothing on Sus MAX / Sus Non Vib rows (0.01 dB) | accents and trims on sustain rows cannot become velocity | n/a |
| Kit LEARNINGS lines 59-61, 195-197, 204-206: velocity is the dynamic on harp, pizzicato and timpani strokes; rolls hardly follow it; small metric velocity steps failed (0.5-1.2 dB of 2-3 planned) | harp / pizz. metric layer, viola pizz. pitch trims, timpani loud attack | The metric layer is in the envelope and measures neutral (finding 1) |

## The envelope in numbers (answer to Dan's question)

- 22,022 points on 32 tracks for 1,507 note onsets in 346 s: 14.6 points per onset. Violins I 1,650 (4.8 per second), Violins II 2,430 (7.0), violas 2,009 (5.8), celli 2,461 (7.1), basses 2,338 (6.8); winds and Horn 1 540-900 (1.6-2.6 per second).
- Envelope travel by class: shape 8,277 dB (59 %), slow 3,260 dB (23 %), per-note level 2,394 dB (17 %). The largest shape layers by points: re-bow fills 4,418 (8 tracks), long-note swell 3,330 (27 tracks), early fills 1,340 (19 tracks), level-fit rows 1,556, sostenuto hold 569.
- References (my count of `<VOLENV` points): EastWest's two templates have no volume envelope on any of 59 / 86 tracks. Duc's Mahler Adagietto, the closest music, has 11 envelopes with 5-120 points over 572 s, 0.01-0.21 points per second, a median of 0.8-5.9 s between points and a median step of 0.5-1.9 dB: phrase-level rides. Duc's LOTR: 15 envelopes, 3-18 points, at most 0.12 per second. Our strings carry 23-700 times that density.
- What the references use instead (their MIDI): CC1 at 25-77 events per note and CC11 at 4-78 per note on every Mahler string track, velocity spread (sd) 23-31. Ours: CC11 3-9 events per note, CC1 190-790 events per track, velocity sd 10-34. In their library CC1 is the dynamic; in HO that role is CC11 (CC1 on brass and clarinets).
- Why ours looks as it does: most of the movement is compensation for sample behaviour (slow starts of legato targets, re-bow dips, transition peaks, per-pitch level differences), fitted per note from renders, plus four generic layers that shape every long or plucked note without a score mark, plus slow layers that are written as stairs on the 0.125 qn grid.
- The "up and down on every fast note" case in this movement is the viola pizzicato triplets of bars 41-44: the envelope at successive notes reads 10.9, 8.7, 6.0, 11.2, 9.6, 7.2, 9.9, 7.4 dB (per-pitch pizz. trims of +4 / +3 / 0 and the metric layer +1.5 / +0.5 / -1 / -1). Flute 1's 20 short notes step a median 3.6 dB note to note (pitch trims, level fits, early fills, note trims).

## Whole piece with the shape class off, capped, and flattened

| variant | points | master I / LRA | join holes of 6 dB or more (all sections) | long notes starting 3 dB or more under their body | worst main lines (median note-to-note step, dB, with -> variant) |
|---|---|---|---|---|---|
| as rendered | 22,022 | -22.8 LUFS / 23.8 | 298 | 176 | |
| shape off | 15,758 | -23.7 / 23.5 | 371 | not counted | Oboe 1 15-22 1.86 -> 3.49; celli 71-78 1.50 -> 3.48; Violins I 79-82 2.23 -> 4.37; Horn 1 53-60 2.28 -> 3.14; Flute 1 37-44 1.80 -> 2.36 |
| shape clipped to +-3 dB (absolute) | 20,134 | -23.0 / 23.7 | 328 | not counted | celli 71-78 1.50 -> 3.29; Oboe 1 15-22 1.86 -> 2.85 |
| in-note deviation clipped to +-3 dB around each note's mean | (not rebuilt) | | 309 | 187 | celli 71-78 1.50 -> 1.76; all others within 0.3 |
| one level per note (shape replaced by its mean over the note) | (not rebuilt) | | 372 | 302 | Oboe 1 15-22 1.86 -> 2.70; celli 71-78 1.50 -> 2.68; Violins I 23-30 2.61 -> 3.28 |

By passage with the shape class off (master per bar within 1 dB at 78 of 92 bars):
- Worse: the coda (join holes of 6 dB or more 16 -> 31, unmarked long notes with a 3 dB dip 34 -> 45), the retransition bars 65-70 (dips 4 -> 10, basses -4.1 dB: re-bow fills and the E flat 2 pitch trim), bars 37-44 (holes 54 -> 69), bars 45-52 (20 -> 29), the strings' theme bars 23-30 (29 -> 36), the celli counter-melody in A' (above), the ff cadence (celli -5.0 dB), bars 63-64 (master -2.6 dB: Violins II -3.7, celli -4.1).
- Better: Horn 1's theme bars 7-14 (dips 7 -> 2, range inside unmarked long notes 5.0 -> 3.7 dB), celli bars 45-52 (step 2.90 -> 1.90), Trombone 1's quotation (3.11 -> 1.74), the bass clarinet solo (2.23 -> 1.81), join peaks at the climax (21 -> 14).
- Unchanged: violas 48-51 (1.25 either way), Violins II's lines, the solo violin, the basses' lines, bars 53-60 as a whole.

## Findings

### 1. Four generic layers move every long or plucked note and measure as no help: remove them from the envelope (measured)

Where: all tracks. `score_to_parts.py` `swell_db` (`SWELL_DB` 1.5: +1.5 dB at 40 % of every long note, 0 at 80 %, 3,330 lane points on 27 tracks); the sostenuto hold (`SOST_SUSTAIN_DB` 2.5: rises 2.5 dB into the next note, 569 points, 22 tracks); `METRIC_DB` on harp and pizzicato (+1.5 / +0.5 / -1, 200 points, 3 tracks); the phrase-top contour (`PT_DB_PER_ST`, 196 points, 7 tracks). None answers a score mark.

Evidence, each layer divided out alone, on the notes it touches:
- Long-note swell (223 notes): dip inside unmarked long notes 3.4 -> 3.0 dB (27 notes better by 1 dB or more, 2 worse), range 6.4 -> 6.0 (39 better, 4 worse), join hole 4.5 -> 3.8.
- Sostenuto hold (77 notes): join hole 3.0 -> 3.3 dB (its only gain), join peaks of 26 notes better without it, the tail stands 1.0 dB over the front with it and level with it without.
- Metric layer (147 notes): step 1.5 -> 1.5 dB. Phrase-top contour (78 notes): step 1.9 -> 2.0.
- All four off together and accent swells clipped to +3 dB (variant K, stems): Horn 1 theme bars 7-14 median step 2.03 -> 1.36 dB; dips of 3 dB or more in bars 7-14 7 -> 1 and bars 23-30 17 -> 13; join holes of 6 dB or more fall or hold in all 13 sections (298 -> 279); no main line worsens by more than 0.4 dB (bass clarinet 2.23 -> 2.64, Violins I 53-60 1.00 -> 1.39). Level cost: eight tracks lose 1.1-1.4 dB in bars 61-64 (the hold's lift at the end of the ff long notes).

Fix (`build/score_config.py`): `SWELL_DB = 0`, `SOST_SUSTAIN_DB = 0`, `METRIC_DB = {}`, `PT_DB_PER_ST = 0`. Give the climax its 1.2 dB back as a slow row: `LEVEL_SHAPES["_all"]` `[(203.5, 0), (204.25, 1.2), (211.75, 1.2), (212.25, 0)]` in place of the -0.4 row, then re-check the delivered span. Verdict per layer: remove. If a swell on espressivo long notes is wanted later, put it on CC11 (5-10 steps at CC 50-80 is 1.5-2.5 dB and brings the layer change with it), not in the envelope.

### 2. The fitted shape layers do measurable work; a blanket off, a clip on the absolute value, or one level per note each lose something Dan checks (measured)

Evidence, each layer divided out alone:
- Early fills (`early_fills.json`, 360 notes, 19 tracks): join hole 4.3 -> 5.5 dB (172 notes worse, 25 better); front minus body -0.5 -> -2.0 dB (231 notes start weaker). Keep.
- Re-bow fills (`rebow_fills.json`, 125 notes, 8 tracks): join hole 3.0 -> 5.0 dB (58 worse, 4 better), dip in the note 3.7 -> 4.9 (32 worse), front minus tail -0.4 -> -2.9. Keep (BRIEF item 8).
- `JOIN_NOTCH_S` / `JOIN_NOTCH` (68 notes): join peak 2.3 -> 2.9 and 2.7 -> 3.1 dB, 29 worse, none better. Keep.
- `level_fits.json` / `LEVEL_SHAPES_S` rows that move inside the note (136 notes): step 2.2 -> 3.1 dB (51 worse, 23 better), 33 notes start weaker without. Keep. These rows also carry body level: without them the celli fall 4.6 dB in bars 79-82, 2.4 dB in 61-64 and 1.9 dB in 71-78.
- `LEVEL_SHAPES` rows of class shape (95 notes): step 3.1 -> 4.3 (37 worse, 14 better). Keep.
- Pitch trims (`pitch_trims.json`, 314 notes): step 2.0 -> 3.4 dB (128 worse, 50 better). Note trims (`note_trims.json`, 122 notes): step 2.2 -> 3.1 (56 worse, 19 better), but join hole 5.2 -> 4.6 and 35 join peaks better without them: the trims help the level and hurt the join, which is slot A's step-timing question.
- Balance depends on the per-note level class: with it off as well, Clarinet 2 bars 1-6 -9.4 dB, timpani bars 1-6 and 65-70 +12.8, basses coda +5.7 and intro +5.5, Oboe 1 37-44 -4.8, Violins I bars 61-64 step 3.07 -> 6.74.
- Accent swells (10 notes): front minus body 11.8 -> 8.7 dB without; values up to +6.5. Cap at +3 (BRIEF item 4).
- Slur-pair release (18 notes): join hole 5.2 -> 4.9 without (9 better): it deepens the hole it sits on. Cap at -1.5 dB or leave to slot A.

Fix (`tools/score_to_parts.py`):
- Tag each `vol_parts` item with a class where it is appended (my table is `envlib.py` `NAMES` in scratch) and add `ENV_CLASS = {"slow": "on", "level": "on", "shape": "on"}` with shape values `on / cap3 / flat / off`. `cap3` must clip the deviation from the note's own mean, not the value: that variant holds every main line within 0.3 dB and costs 11 join holes, where the absolute clip breaks the celli counter-melody (1.50 -> 3.29) and takes 2.3 dB off the celli at the cadence. `flat` only for notes of an eighth or less.
- Split the c52b / c53 rows of `level_fits.json` (Violoncellos 38 rows, Violins I 22, Violas 6) into a body value (class level) and a start shape (class shape), so the switch does not move balance.
- Keep the rule from Movement I: a new per-note row needs a before / after stem figure.

### 3. Instrument-side homes: what can leave the envelope, with the test for each (measured facts, inferred gains)

Since c44 the hall is a post-fader return, so the envelope and CC7 both act before the hall; S3's reason for preferring CC over the envelope no longer applies, and moving exact levels to CC7 would change the picture Dan sees and nothing he hears. The moves below are the ones with a musical reason.

| layer | home | basis | action |
|---|---|---|---|
| long-note swell, sostenuto hold | CC11 if wanted at all | CC11 2.5 dB per 10 steps at CC 50-80, with the layer | remove (finding 1) |
| hairpin gains (`HP_GAIN_DB`, 6,236 lane points) | stay in the envelope | kit line 78: at p CC11 moves 0.1-0.2 dB per step | keep, write as ramps (finding 4) |
| early fills of 4 dB or more on soft entries | CC11 lift at the note-on (+10 to +22 for 0.5 qn) | Scherzo c11: a CC11 lift moved soft re-attacks from +31..+177 to -47..+50 ms where a volume swell did not | range render of bars 23-26 and 83-86 with the lift and no fill; adopt per note only with a before / after front level and S |
| early fills on legato targets, join notches, re-bow fills, loop fills | none | velocity sets transition time only (p.144); the faults are in the samples | keep |
| pitch trims on sustain rows | none (velocity has no effect on Sus rows) | kit line 423 | keep as one level per note |
| viola pizz. pitch trims (+4 / +3 dB, 30 notes; step 3.1 -> 3.8 without) | velocity | pizzicato follows velocity; round robins vary 1-3 dB | range test bars 41-44 with velocity +8 / +6 and no trim; keep whichever gives the smaller peak spread |
| harp / pizz. metric layer | none | velocity steps failed (kit line 61), envelope neutral | remove |
| timpani loud attack (+6 dB, 7 notes) | velocity on strokes (about 3 dB per 22 steps, Scherzo c15); CC7 on rolls | the patch has no CC11 | move for strokes, test on bar 53 and bar 61 |
| timpani settle, soft-roll -6, roll trims | CC7 (linear amplitude, exact) or stay | kit lines 54, 204-208 | keep; cosmetic either way |
| accent swells | stay, capped +3 | BRIEF item 9: CC11 into the top layer is the harsh attack | cap |
| brass in-note shape (Horn 1, Trombone 1) | CC1 (`CC1_DYN_TRACKS`) | manual p.101 | no new envelope shapes on brass; the Trombone 1 quotation steps 3.11 dB with its rows and 1.74 without |

### 4. Two thirds of the points are slow curves drawn as stairs; the same curves need under half the points (measured)

Evidence: with the whole shape class off 15,758 points remain. Hairpin gains hold 6,236 lane points on 26 tracks and roles 4,890: `score_to_parts.py` samples them on a 0.25 qn grid and `vol_points` on 0.125 qn. A line simplification of the written curves (time against dB) keeps 13,966 points at 0.1 dB tolerance and 9,353 at 0.25 dB; with finding 1 applied 11,324 and 8,400 (Violins I 770, Violins II 1,009, violas 782, celli 1,046, basses 940; 2.2-3.0 per second). Re-bow fills are sampled every 20-25 ms: 4,418 points for 125 notes.

Fix: in `tools/build_reaper.py` `vol_points`, after the tail-hold and subito passes, drop every point that lies within 0.1 dB of the line between its kept neighbours, computed in REAPER's envelope scale (Scherzo c15: REAPER interpolates in that scale, not in dB); in `score_to_parts.py` emit hairpin gains and roles as their own breakpoints instead of grid samples; in `tools/fit_rebows.py` fit each list with at most 6 points at 0.5 dB. Check with a stem simulation that no 10 ms frame moves more than 0.3 dB. No audible change is intended; this is what makes the lanes readable in REAPER. Even then the strings stay about ten times denser than Duc's, which is the cost of the fitted layers of finding 2.

### 5. Bass after the c54 EQ: the two flagged notes are not booms, the loudest bass-band moments are even, and the remaining deficit is in the tuttis only (measured; the size of a further step inferred)

Evidence (Double basses stem and master, 56-112 Hz, 20-80 % of each bowed note):
- E1 at qn 210 (bar 62): stem band 9.4 dB against 10.7 for the G flat 1 before it and 15.6 for the D flat 2 at 204. Its "+4.5 over the neighbours" comes from the other neighbour, the A1 at 212 in the bar 63 fall (-0.9). The E1 sample has its fundamental 28 dB under its second harmonic and its third harmonic (123 Hz) 10 dB over the second.
- E flat 2 at 268 (bar 81): stem band 4.3 dB against 14.0 for the D flat 2 at 262 and 265. Its neighbours are the B flat 1 at 267 (0.4: fundamental 58 Hz at the band edge, second harmonic outside the band) and the A flat 1 at 271 in the diminuendo. Master share during the note -14.4 dB.
- The six highest master 56-112 Hz levels of the piece lie within 2 dB: D flat 2 at 204 16.0, A flat 1 at 200 15.9, E1 at 210 15.4, G1 at 198 14.3, D flat 2 at 262 and 265 14.0.
- The neighbour measure is governed by where each pitch's partials fall: master share during the note by pitch, median: A flat 1 -7.9 (27 notes), D flat 2 -11.8 (13), E flat 2 -14.4 (17), B flat 1 -19.7 (12). The B flat 1 notes are level in full band (bar 80: +3.4 dB over the neighbours' bodies).
- Share by section (my frames give -12.1 whole where c54's method gives -11.5): soft passages with basses -7.3 (coda), -9.2 (37-52), -9.3 (intro), which is the Brahms range (-7.9 / -7.3); tuttis -11.1 (53-60), -12.8 (61-64), -12.2 (71-78), -11.7 (79-82); passages without basses -13 to -22 (bars 7-22, 31-36). The basses supply 78-98 % of the dry 56-112 Hz energy in the tuttis. The Brahms audio is not on disk (only stored third-octave figures, both movements in E major with B1 and E2 inside the band), so time-resolved comparison is not possible.

Fix (`build/mix.json`, Double basses `loud_eq`): no static change, and no per-note trims for 210 or 268. In the climax row (points 190-216 and 254-271) change the 100 Hz low shelf from -1.5 to +1.0 dB, and extend a +1.5 dB 80 Hz shelf row over bars 71-77 (qn 238-254). Simulated as +2 dB of the basses' band in bars 53-64 and 71-82: share -11.1 / -12.8 / -12.2 / -11.7 -> -9.6 / -11.1 / -10.4 / -9.9, whole piece -12.1 -> -10.5, master level +0.12 to +0.17 dB. Guard: the D flat 2 at 204 is already the loudest bass-band note, so check that it stays within 3 dB of 200 and 210 and that no bar rises more than 1 dB K-weighted. Do not go to the full Brahms figure: the soft sections are already there.

### 6. Dynamics over time: nothing to change this cycle (measured)

Master per bar (stereo-sum frames): fp at bar 47 -34.5 between -37.1 and -39.5; bars 53-61 -36.0, -30.9, -29.6, -26.2, -26.6, -23.4, -20.7, -17.1, -13.6 (bar 57 is 0.4 dB under 56, where ten parts restart at p / mp with a new crescendo at qn 188, as printed); 62-66 -14.6, -21.0, -25.9, -43.2, -45.0; cadence 78-82 -21.1, -18.9, -19.6, -25.7, -36.7, the climax 5 dB over it; coda -44.1 to -39.1, then -42.5, -46.8, -52.1. Master LRA 23.8 LU; delivered mp3 -19.8 LUFS, LRA 15.1 LU (target 14-16), true peak -1.6 dBFS, span 18.1 dB by the actor's figure (limit 19). With finding 1 applied the shape of this arc holds within 1 dB per bar except bars 61-64, which the slow row restores.

## Do not touch

Early fills, re-bow fills, loop fills, `JOIN_NOTCH_S`, the level-fit rows and the pitch and note trims as levels (finding 2), until each has an instrument-side replacement with a before / after figure. The timpani settle and soft-roll cut (BRIEF item 5). The divisi / chord cut. The basses' static EQ after c54 and the soft-section bass level. The delivered loudness range and the crescendo of bars 53-61. The viola portato eighths of bars 48-51 (step 1.25 dB in every variant).

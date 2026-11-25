# Cycle 57, critic A: articulation and phrasing; the string envelope by layer

Under review: the c56 render (`cycles/c56/render/`, stems with the four stem fixes) and `build/` (identical to what the stems carry). Scripts: `cycles/c57/critic_scripts/A/`. Everything is measured on the dry stems or read from the data unless marked inferred. Nobody listened.

How the layers were separated: `tools/score_to_parts.py` was run read-only into my scratch folder with `STP_DUMP_VP` (output byte-identical to `build/parts.json`), and a patched copy (`s2p_predump.py`) dumped the envelope items with their rule names before `NOTE_LEVEL` merges them. The written envelope comes from `build_reaper.py` cut before `ENV_LUA`. That run read `~/.rpr-bridge/libs/ew_ho/ks_maps.json` and imported `opus_state.py` (read only, no job, no REAPER contact). Stem tests are level-only: stem level minus the layer (removed) or minus half of it (halved).

Manual notes: `loop/MANUAL-READING.md` has no row for c57, so no page range was read. From `MANUAL-GAPS.md`: #7 (half-section divisi patches) and #5 (expressive wind rows) are still untried; #8 (velocity on the Marc LITE row) failed in c55. Not read this cycle: README.md, FINDINGS.md; HISTORY.md and both LEARNINGS files were only searched for the rows named below.

EW-TEMPLATE-PLAN sections my lens touches that are not applied: section 5 legato overlap (plan 45-80 ms on strings, 33-58 ms on winds and brass; as built the median is 21 / 19 / 21 ms, 41 of 625 string joins inside the range); section 6 "no per-note bumps, shape per phrase" (finding 1); section 6 two tracks per string section; section 7 lean-off inside slurs. Section 8 repeat gaps: string repeats have a median gap of 80 ms, but 79 of 478 are under 40 ms (finding 6).

## 1. String envelope: which layers cause the 3 dB notes, and which the stems need (coordinator's request)

Count per onset (a chord counts once), critic C's window (moved note-on to note end): 1002 of 2091 string onsets move 3 dB or more (Violins I 179, Violins II 154, Violas 213, celli 248, basses 208); 365 of them strictly inside the sounding note. Each onset is assigned to the layer with the largest movement inside it. "as / half / off" are stem readings with the layer as rendered, halved, removed, on the notes that carry it.

| class | onsets (VI / VII / Va / Vc / Cb) | median, p90 dB | eighth or shorter | stem test (as / half / off) | verdict |
|---|---|---|---|---|---|
| repeated-note dips | 269 (0 / 24 / 90 / 28 / 127) | 5.0, 6.0 | 208 | separation: VII 7.1 / 5.2 / 4.6, Va 6.7 / 4.7 / 3.0, Vc 4.6 / 3.0 / 2.1, Cb 4.8 / 3.7 / 3.0 dB; repeats under 6 dB 130 / 179 / 214 of 251 | must stay, full depth |
| step to the next note's level (`note_level`) | 188 (44 / 21 / 31 / 64 / 28) | 4.3, 7.1 | 75 | by rule, see below | Violins I theme steps: scale to 0.55 (finding 2); the rest stays |
| slow layers inside long notes (hairpin gain, roles, dynamic trim) | 134 (16 / 23 / 37 / 37 / 21) | 4.4, 8.4 | 20 | not per-note | stays; do not count it against Dan's point |
| config level shapes (`LEVEL_SHAPES`, tag `shape`) | 133 (30 / 28 / 15 / 43 / 17) | 4.5, 8.0 | 38 | body step 2.5 / 2.6 / 2.9, front 2.9 / 2.9 / 3.0; basses 3.4 as against 2.9 off | keep the steps at note starts; remove the 16 edges inside notes (finding 3) |
| theme body lifts (`steady_body`) | 84 (66 / 12 / 2 / 4 / 0) | 7.7, 11.3 | 20 | long notes front minus tail 2.5 / 5.4 / 8.9 dB; join holes over 6 dB 49 / 55 / 65 of 128 | must stay in full while the theme is on Sus Marc LITE |
| re-bow and loop fills | 51 (5 / 14 / 10 / 10 / 12) | 10.4, 17.2 | 0 | dip at the re-bow, per section 1.7-2.9 / 3.5-5.7 / 4.8-9.4 dB; dips over 4 dB 23 / 53 / 86 of 100 re-bows | must stay; 8 are over-filled (finding 4) |
| accent swell and body | 40 (12 / 7 / 10 / 9 / 2) | 3.0, 6.0 | 0 | front minus tail +2.4 / +0.8 / -0.4 dB | stays at the 3 dB cap |
| join fills (`early`) | 38 (2 / 3 / 4 / 28 / 1) | 4.2, 6.0 | 0 | celli (82 notes): weak start 2.0 / 2.7 / 3.2 dB, join holes over 6 dB 8 / 10 / 19 of 76 | keep; halving costs 0.7 dB and 2 holes if the count matters more |
| skip-list spans (as built in c55) | 29 (0 / 10 / 0 / 19 / 0) | 4.2, 8.5 | 16 | body step 1.8 / 2.3 / 2.8, front 2.1 / 2.3 / 3.2 | stay as built |
| join notches | 19 (4 / 2 / 8 / 5 / 0) | 5.4, 5.8 | 5 | bump at the join 1.0-2.0 dB with, 4.3-5.7 without; bumps over 3 dB 4 / 13 / 18 of 23 | must stay |
| syncopation, pair release, tenuto | 16 (0 / 10 / 6 / 0 / 0) | 6.0 | 0 | level range inside the note 4.9 / 6.4 / 7.6 (Violins II 4.1 / - / 9.8) | stay |
| crescendo front | 1 | 3.0 | 0 | 6 notes, no clear reading | leave |

The per-note level by the rule that wrote it (joins where the rule writes a step of 1 dB or more; note-to-note body step at scale 0 / 0.5 / 1, then front step):
- `steady_level` (theme): Violins I 123 joins, body 2.9 / 1.4 / 1.6, front 2.5 / 1.6 / 1.8: over-corrects, finding 2. Violas 3.4 / 2.0 / 2.1, celli 4.3 / 2.8 / 2.2: keep.
- `ptrim`: celli 7.0 / 6.0 / 4.6, basses 4.0 / 3.4 / 2.8: must stay. The celli trims under-correct (best scale 1.7 on body, 1.5 on front); the celli remain the least even string line.
- `ntrim`: celli 5.0 / 4.1 / 3.9 keep. Violas 2.4 / 2.3 / 2.6, front 1.2 / 1.6 / 2.2: no gain, the 14 rows can go.
- `metric`: Violas 1.8 / 1.8 / 1.5, basses 2.1 / 2.0 / 1.7: small gain, steps of 1-1.5 dB, never 3 dB alone: keep.
- `pickup`: Violins I 3.6 / 2.7 / 3.1, front 3.8 / 3.0 / 2.9: keep.
- `rowtrim`: Violins II body 2.5 / 1.3 / 2.9 with front 3.5 / 3.7 / 3.7: halve. Violins I and Violas: body is better at half, front better at full: leave.

Result for the aim "half the count": not reachable by trimming. Dips, body lifts, re-bow fills, notches and the slow layers are 557 of the 1002 onsets and the stems get worse without each of them. Scaling the Violins I theme steps moves the count only 179 -> 170 (6 dB or more 95 -> 89), because the same notes also carry a body lift; it does halve the size of the steps Dan sees between neighbouring theme notes. What would lower the count is a change of means, not of amounts: the theme on a row that does not decay (the Sus MAX retest in the coordinator's notes would remove the 84 body lifts and most of the 44 Violins I steps), and a count that leaves out the slow layers and the separation dips (they are articulation, like a note-off).

The caps (read in `score_to_parts.py`): `ACCENT_SWELL_CAP_DB` limits the swell's own height above the note's level, `shape_max_db` scales the summed shapes so that their range about the note's level is 6 dB or less, `EARLY_FILL_CAP` limits the fill's height. None clips an absolute value. The cap sees only the `shape_tags`: it fired on 31 notes in the movement. Body lifts, re-bow fills, dips, notches and config shapes pass beside it, so 140 string onsets still move 6 dB or more strictly inside the note (largest layer: re-bow fill 47, body lift 25, kept shapes 24, config shape 23, slow 14).

## 2. Violins I theme: the per-note level steps are about twice too large (bars 15-40, 135-144). Measured.

For each join, the stem step with the rule taken out (d) against the written step (c); perfect correction is d = -c. Least squares over 123 joins gives d = -0.59 c on the body and -0.59 c on the front. By span: 56-90 body 0.51, front 0.46; 104-160 0.54 / 0.69; 536-576 0.83 / 0.50. By join type the factor is 0.51-0.67 everywhere (eighth to eighth 0.58 / 0.59, long to long 0.54 / 0.67).

Bars 15-23 (qn 56-90, 36 joins), the passage Dan called choppy: body step 2.8 with no correction, 1.2 at half, 2.0 as rendered; front step 1.9 / 1.0 / 1.8. As rendered the fronts are no more even than with no correction at all. Whole theme: body 2.9 / 1.4 / 1.6, front 2.5 / 1.6 / 1.8.

Fix: `build/steady_levels54.json`, Violins I: for each span (56-90, 104-160, 536-576) replace each value v by m + k (v - m), m = the span's median value; k = 0.55 for 56-160 and 0.7 for 536-576. Written steps between neighbours fall from median 3.3, p90 8.8, max 15.1 dB to about 1.8 / 4.8 / 8.3. Inferred: the theme's lower quartile over the celli rises, because the deepest cuts (-15.5 dB at 58.5) are halved. Leave Violas and celli values. Guards: Violins I 56-90 S robust SD 10 ms or less on a range render (twice, second kept; a level step on the beat moves S readings), front minus tail 2.0 dB or less, Violins I minus celli lower quartile.

## 3. Sixteen config-shape edges make a step inside a sounding note that the stem does not have without them. Measured.

Of the string `LEVEL_SHAPES` items of 2.5 dB or more, 132 edges fall on a note start (level steps, fine), 56 items are slow ramps, 54 edges of 2.5 dB or more within 0.12 s lie inside a sounding note. Over those 54 the stem step across the edge is 3.1 dB with the item and 2.7 without (over 3 dB: 30 with, 23 without). Edges that add a step (qn, stem step with / without, dB): celli 696.17 +9.1 / +2.7, 8.78 +5.1 / -1.9, 7.27 +4.9 / +0.9, 310.77 +6.6 / +3.6; Violins II 566.58 +8.6 / +2.3, 192.11 +6.0 / +2.5, 580.12 +4.8 / -0.1, 389.12 +4.5 / +0.7, 400.37 +4.6 / +2.1; Violins I 565.53 -7.1 / -2.7, 720.20 -5.7 / -0.2, 160.44 -5.5 / -2.4; Violas 580.67 -4.3 / +0.5; basses 714.62 -5.9 / -3.0, 672.20 -4.0 / -1.0, 718.12 -3.8 / -0.9. Edges that cure a sample step and must stay: Violins I 565.71 (3.0 / 11.1), 140.25, 572.25; Violins II 565.71, 78.42, 78.67; celli 556.87, 566.25; Violas 580.12, 580.20.

Fix: in `build/score_config.py` `LEVEL_SHAPES` / `LEVEL_SHAPES_S`, move each of the 16 edges to the next score onset with the 40 ms crossfade `NOTE_LEVEL` uses, or make it a ramp over the note; drop the item where the step without it is under 1 dB (celli 7.27, Violins II 580.12 and 389.12, Violins I 720.20, Violas 580.67). List and test: `critic_scripts/A/shapes.py`.

## 4. Re-bows: c56's final-chord fix holds on Violas and Violins II; Violins I and celli still pulse, and four re-bows elsewhere still dip. Measured.

Final chord (qn 712-728), bump = highest 100 ms level near the re-bow minus the level before and after: Violas 1 bump over 3 dB (725.52: 3.2, with a 5.1 dB dip), Violins II none: the c56 lowering is verified. Violins I 724.47: 0.1 s levels -58.7, -55.9, -52.0, -57.7 (bump 6.6 dB; the fill peaks at +12.8 dB); 726.51: -61.3, -58.3, -61.1, -64.9, -67.8; 722.78: dip 5.0 dB. Celli 715.54, 719.48, 723.92, 725.21: bumps 3.3 / 4.3 / 4.7 / 4.7 dB under fills of +9 to +10 dB; with the fill halved they read 2.1 / 1.6 / 2.3 / 0.0 with dips of 3.2 / 2.6 / 1.3 / 2.3.

Elsewhere: Violins I 44.0 dip 7.2 dB (-36.5, -37.8, -43.1, -38.4; the fill gives only +4.1 at the low frame); celli 289.14 dip 7.2; Violas 292.0 5.8 and 52.0 5.1.

Celli qn 180 (bar 46, the repeated A flat before the second theme) is not a re-bow but a new note; the `rebow_fills` row cuts -8.4 / -9.5 / -5.8 dB over the 0.3 s before it and the Sus MAX note at velocity 45 then needs 0.3 s to speak: 0.1 s levels -51.4, -53.7, -56.1, -59.6, -60.3, -63.7, -66.4, -61.8, -54.5. That is a hole of 12-15 dB for 0.4 s in a p line.

Fix: `build/rebow_fills.json`: Violins I 724.47 and 726.51 and the four celli rows lowered by the stem's excess (as `rebowres56.py` did for the Violas), about half; Violins I 44.0 raised by 3-4 dB at the dip frame. Celli 180: limit the cut to -5 dB over the last 0.08 s (the `STR_REP_DETACH` shape) and give the note an entry lead of about 0.12 s (`build/entry_leads.json`) or an early fill of +4 dB for 0.25 s.

## 5. Accents: weight without bite is met; about a third of the wind and string accents do not stand out at all. Measured, with the caveat below.

2-5 kHz level of the first 80 ms against the note body, all 598 accented notes: median -2.5 (winds), -4.2 (brass), -2.1 (strings); over +6 dB only Violas 536 (+10.4), Bassoon 1 536 (+7.5), Violins I 160 (+6.3), basses 160 (+6.3), Clarinet 1 120 (+6.0). Front over the mean front of the nearest unaccented neighbours: winds median +1.9, strings +2.3, brass +3.0. Under +1 dB: winds 61 of 150, strings 49 of 156. Per track medians: Bass clarinet +0.1, Bassoon 2 +0.3, Bassoon 1 +0.4, Horn 1 +0.4, Oboe 1 +0.9, celli +1.2, Trombone 1 +1.4. Oboe 1 and Horn 1 carry c56's `ACCENT_PLAIN` (swell 1.5 dB or less): the lines became more even and the accents disappeared. Over +5 dB: strings 28 of 156, winds 17 of 150 (the largest, Violins II and Violas 286, are entries after a rest and not comparable). Caveat: neighbours inside a hairpin bias single readings; the medians are safe.

Fix: rerun `tools/fit_accents.py` as residuals on the c56 stems with the target +2.5 dB over the neighbours' fronts, swell 0 to 3 dB, for the accents now under +1 dB on Bassoon 1 and 2, Bass clarinet, celli, Trombone 1; on the `ACCENT_PLAIN` lines allow the fitted value up to 2.5 dB instead of 1.5. This adds movement inside marked notes only.

## 6. Smaller items, verified or open

- Oboe 1 bars 23-25 (88-100), after c56: bodies -54.1 -46.6 -38.8 -43.7 -41.9 -40.5 -36.9 -38.9 -40.9 -36.7 -35.2 -35.1; body step 3.1 -> 2.1. The note at 90 still stands 7.8 dB over 89 and 4.9 over 91. The recapitulation 536-548 was not touched (step 3.5 -> 3.6; 538 at -42.7 between -47.6 and -48.0). Fix: `build/early_fills.json` Oboe 1 90 and 538 to 1.5 dB.
- Repeated notes (S1): string same-pitch repeats up to 1 s apart, re-bows left out: 478, separation median 6.6 dB, 212 under 6 dB. By gap between note-off and note-on: under 40 ms 79 repeats, median 4.5 dB; 40-100 ms 332 repeats, 6.9-7.1 dB. Violas Sus MAX repeats have a median gap of 18 ms (basses 80 ms). Test (range render): Violas repeats ending 60-80 ms before the next note-on (plan section 8), dips kept. Inferred gain about 2 dB.
- Tutti stops on the master, drop 0.3 s after the stop: bar 83 -20.9 dB, bar 138 -19.8, fermata 679 -18.3 (c55 -21.2 / -20.3 / -19.5): all over the 13 dB target.
- Clarinets after the f trim change: bars 26-32 within -1.0..+0.0 dB of c55, bars 139-142 within -0.6..+0.4.
- No chord and no overlap over 0.25 s on a legato row on any track (1603 legato notes). No note-on moved in c56, so keyswitch timing is as in c55.
- Not checked: loop pulsing folded at 3.95 s, timpani and harp technique, S on the theme (no new render), single bass pitches (critic B).

Do not touch: repeated-note dips at full depth on all four sections; `steady_body55.json`; the re-bow fills outside the rows named in 4; join notches; the celli and basses pitch trims; `pickup` lifts; the skip-list spans; the accent cap at 3 dB; the Violas and celli `steady_levels54` values; the basses' repeated eighths on Sus MAX (Marc Shrt and Detache were tested and rejected in c03 and c13).

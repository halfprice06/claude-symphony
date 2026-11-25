# Critic C, cycle 55: holistic, steadiness of rhythm first (render c54, score v621)

## Manual notes (no row for c55 in MANUAL-READING.md; pages chosen for this lens, MANUAL-GAPS.md used)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.91-92 | Marcato Sustain "plays a marcato sample in addition to the multiple sustain samples ... provides extra power at the start of the note." | The c54 theme row (Sus Marc LITE) on Violins I 56-127 / 536-576, Violins II, Violas, Violoncellos 520-536 | Used. The fixed marcato front is why these notes start within a robust SD of 9 ms (table 2). It also puts a bow front on slurred notes; that is critic A's check, not measured here. |
| p.99 | A legato transition needs two notes with no gap on the legato patch; "the first note of a phrase has no legato effect at the start of the note." | Every string legato note whose predecessor plays another row (183 exposed joins in the Allegro) | Not followed by the leads: these notes get a transition lead (150-290 ms) but play no transition. They start a median 23 ms earlier than same-row joins and scatter more (table 3). Findings 2-4. |
| MANUAL-GAPS #8 | Legato velocity 50-75 gives a longer recorded slide on the cantabile lines; never tried. | Second theme (celli 184-244, violas / celli 584-636) | Not applied. I do not recommend it before the timing of those lines is fixed (finding 2): a longer slide adds to the spread unless the lead is refitted. |

EW-TEMPLATE-PLAN sections this lens touches and their state: section 5 (legato overlap 45-80 ms) not applied on the c54 theme lines (no overlap by design) and unmeasured elsewhere; section 6 (two tracks per string section, one legato track and one KS track) not applied, and it is the structural fix for row-change joins (finding 2); section 7 (winds shifted early by a fixed amount per track) not applied, the leads are per note (finding 3); section 8 (tutti entry spread 36-55 ms, seeded) not applied by design, yet the render has an unplanned 55-92 ms spread (finding 5); sections 8-9 (tempo: phrase-end breaths, 20 % of beats changed) are the source of the phrase arcs judged in finding 1.

## Method (measured)

- Time map: `cycles/c54/rendered_build/parts.json` (`tempo`, each note's `qn` and `sq`), read with `symphony/mvt2/reaper-v600/tools/pcx.py` `TM`. Printed tempo: the tempo track of `build/mockup.midi`. c49 and c53 were measured on their own `rendered_build/parts.json`.
- Measure S: `pcx.s_start` (the earlier of pcX and the robust crossover on joins, pcX alone on entries and repeats), in ms against the score beat. Scanned: every printed note (top voice per onset, matched to `mockup-events.tsv` so re-bow pieces are left out) of the 37 sustaining stems; 4,400 notes per render. "Exposed" = stem within 12 dB of the master over the note's first 0.35 s, tremolo left out. Spread is the robust SD about the line's own median, so a common offset does not count.
- Items over 100 ms were checked a second way (4096-point spectrum, harmonics 1-3 of the new and the old pitch, 30 ms steps). Readings I could not confirm are named as such.
- I cannot hear. Statements about what a listener notices are inferred from these numbers.

## Table 1. Every unprinted tempo step still in the map (measured from parts.json against the printed tempo)

Printed ramps (176-184, 244-270, 448-464, 480-488, 576-584, 620-632, 656-664, 704-712) follow the print and are not listed. c54 flattened 56-128 and 504-576: both read exactly 126 on every beat.

| Span (bars) | Source | Printed | Played, bpm by beat (only the beats that differ) | Largest single beat | Net time |
|---|---|---|---|---|---|
| 0-16 (1-4) | arc sub | 50 | last 2 beats 49, 47.5 | -5 % | +0.09 s |
| 16-36 (5-9) | arc | 50 | 48.5, then 50.8 x9, last 2 beats 48, 46 | -8 % | +0.03 |
| 36-48 (10-12) | arc + push 37-46 | 50 | 48.5, 51.5 x5, 50.8 x4, 48, 46 | -8 % | -0.06 |
| 48-56 (13-14) | arc main | 50 | 48.5, 50.8 x3, 50, 50, 47.5, 44 | -12 % | +0.21 |
| 128-144 (33-36) | arc | 126 | 127.9 x7 (beats 129-135), last 2 beats 121, 115.9 | -8 % | +0.01 |
| 144-160 (37-40) | arc sub | 126 | first beat 122.2, last 2 beats 123.5, 119.7 | -5 % | +0.05 |
| 184-200 (47-50) | arc + apex | 112 | 113.7 x7, then bar 50 = 107.5, 112, 107.5, 103 | -8 % | +0.04 |
| 200-220 (51-55) | arc main + apex | 112 | 109.1 (beat 201), 113.7 x8, last 2 beats 106.4, 98.6 | -12 % | +0.05 |
| 220-232 (56-58) | arc + apex | 112 | 108.6, then 107.5 at beat 225, last 2 beats 109.8, 106.4 | -5 % | +0.08 |
| 232-244 (59-61) | arc + apex | 112 | 108.6, 113.7 x3, 109.1 (beat 236), 113.7 | -3 % | 0.00 |
| 272-284 (69-71) | arc open | 126 | 127.9 x5 | +1.5 % | -0.04 |
| 284-286 (72) | BEAT_STRETCH x0.95 twice | 126 | 119.7, 119.7 | -5 % | +0.05 |
| 308-324 (78-81) | push x1.015 | 126 | 127.9 x15 | +1.5 % | -0.11 |
| 324-332 (82-83) | arc main | 126 | 127.9 x3, last 2 beats 119.7, 110.9 | -12 % | +0.07 |
| 332-348 (84-87) | arc sub | 126 | 122.2 first, last 2 beats 123.5, 119.7 | -5 % | +0.05 |
| 348-360 (88-90) | arc sub | 126 | 122.2 first, last 2 beats 123.5, 119.7 | -5 % | +0.05 |
| 364-384 (92-96) | push x1.015 | 126 | 127.9 x19 | +1.5 % | -0.13 |
| 384-396 (97-99) | arc open | 126 | 127.9 x5 | +1.5 % | -0.04 |
| 396-408 (100-102) | arc main | 126 | 127.9 x5, last 2 beats 119.7, 110.9 | -12 % | +0.06 |
| 408-416 (103-104) | arc sub | 126 | 122.2 first, last 2 beats 123.5, 119.7 | -5 % | +0.05 |
| 416-424 (105-106) | arc | 126 | 122.2, 127.9 x3, last 2 beats 121, 115.9 | -8 % | +0.06 |
| 424-432 (107-108) | arc sub + apex | 126 | 122.2, then 121 (beat 429), 123.5, 119.7 | -5 % | +0.07 |
| 432-440 (109-110) | arc sub | 126 | 122.2 first, last 2 beats 123.5, 119.7 | -5 % | +0.05 |
| 488-504 (123-126) | arc sub | 100 | last 2 beats 98, 95 | -5 % | +0.04 |
| 584-600 (147-150) | arc + apex | 112 | 113.7 x7, then bar 150 = 107.5, 112, 107.5, 103 | -8 % | +0.04 |
| 600-620 (151-155) | arc + apex | 112 | 108.6, 113.7 x9, 107.5 at beat 615 | -4 % | -0.03 |
| 635.75-636 (159) | CAESURA 0.15 s | 120 | 54.5 for a quarter beat | +0.15 s | +0.15 |
| 636-648 (160-162) | arc sub + apex | 100 | 96 (beat 637), last 2 beats 98, 95 | -5 % | +0.07 |
| 664-679 (167-170) | arc sub | 126 | last 2 beats 123.5, 119.7 | -5 % | +0.04 |
| 679-680 (170) | BEAT_STRETCH x0.6 | 40 | 24 (the fermata over the rest) | -40 % | +1.0 |
| 680-696 (171-174) | arc main + apex | 72 | 73.1 x7, then bar 174 = 69.1, 72, 68.4, 63.4 | -12 % | +0.11 |
| 712-724 (179-181) | arc sub | 50 | last 2 beats 49, 47.5 | -5 % | +0.09 |

In the 126-bpm music outside the two flattened spans, 110 of 318 beats (128-176, 270-448, 464-480, 664-679) are off the printed tempo by more than 1 %. Bars 103-110 hold four two-bar arcs in a row: every second barline has the same 122.2 start and 123.5 / 119.7 (or 121 / 115.9) end. `tempo push 452-464` and `phrase arc 440-452` are skipped by the tool (they meet the printed stringendo) and have no effect.

## Table 2. Spread of sounding note starts (S) by section and line, c54 (c53 in brackets where it changed)

Robust SD in ms, then notes more than 60 ms from the line's median / notes measured. Lines with fewer than 6 exposed notes are left out. Bold = on the c54 one-row treatment.

| Section (bars, qn) | Strings | Winds and brass |
|---|---|---|
| Lento (1-14, 0-56) | Vln I 39, 2/9; Vc 52, 4/12; Cb 64, 4/11 (slow swelling notes: pcX is least reliable here) | Cor anglais 24, 0/6 |
| A theme (15-32, 56-128) | **Vln I 9, 0/79** (42, 9/78); Vln II 36, 4/20; Va 39, 1/12; Vc 47, 3/22; Cb 24, 2/22 | Fl 1 7, 0/13; Ob 1 46, 0/6 (median -58); Bn 1 15, 0/6 |
| B transition (33-46, 128-184) | Vln I 40, 1/36; Va 38, 5/13; Vc 57, 4/8 | Cl 1 23, 0/8; Bn 1 24, 0/14 |
| C second theme (47-68, 184-270) | Vc 45, 11/54; Vln I 31, 3/18; Vln II 47, 2/16; Vln I f62 42, 2/19; Vln II f62 47, 1/18 | Cl 1 27, 3/30; Hn 1 22, 1/18; Hn 2 22, 0/27 |
| D closing (69-76, 270-304) | Vln I 36, 2/18; Va 64, 3/11; Vc 28, 2/8 | Fl 1 22, 1/8; Tpt 1 18, 0/7 |
| E development (77-96, 304-384) | Vln I 30, 0/29; Vln II 30, 1/24; Va 47, 5/23; Vc 36, 7/43; Cb 101, 7/12 | Bn 1 13, 1/12; B cl 25, 0/12; Cl 1 15, 0/7; stac tracks 13-24 |
| F development (97-112, 384-448) | Vln I 33, 2/21; Vln II 56, 3/12; Va 56, 2/18; Vc 55, 5/15 | Fl 1 6, 0/16; Bn 1 13, 1/20; Hn 1 17, 2/12; Tbn 1 19, 1/13; B cl 44, 3/17 |
| Stringendo and G (113-120, 448-480) | Vln I 37, 3/28 (median +28); Vln II 45, 1/12 | Fl 1 7, 0/9 |
| Allargando to a tempo (121-130, 480-520) | Vln I 29, 1/7 (median +45); Vc 31, 4/17 | Cl 1 28, 0/16 |
| H recap theme (131-146, 520-584) | **Vln I 15, 0/43** (36, 6/38); Vc 27, 4/27 (45, 3/24); Cb 10, 3/28 | Fl 1 10, 0/10; Ob 1 25, 2/9 (median -44); Cl 1 18, 1/19; Bn 1 18, 1/19; Tbn 1 46, 0/10 |
| I recap second theme (147-159, 584-636) | Va 53, 9/39; Vc 43, 10/45; Vln I 45, 1/11 | Hn 1 27, 2/22; Cor anglais 4, 0/10; Cl 1 12, 0/7 |
| Largamente (160-166, 636-664) | Vln I 59, 6/20; Vln II 21, 2/10; Vc 33, 3/21 | Tpt 1 19, 0/6 |
| K coda Allegro (167-170, 664-680) | Va 44, 1/6; Cb 1, 1/13 | Horns a2 39, 1/13; Trumpets a2 21, 1/11 |
| L Più lento (171-178, 680-712) | Cello solo 16, 0/12; Va 28, 0/6 | |

Whole Allegro (qn 56-680), all exposed notes, deviation from each line's median:

| | c49 | c53 | c54 |
|---|---|---|---|
| Strings: robust SD, share over 40 ms, share over 60 ms | 40 ms, 34 %, 17 % | 38, 32 %, 16 % | 33, 28 %, 14 % |
| Winds and brass | 23 ms, 14 %, 5 % | 24, 17 %, 9 % | 20, 14 %, 5 % |

## Table 3. The same notes by row and kind of start (c54, Allegro, exposed)

| Family, row | Kind | n | Median | Robust SD | Over 40 ms | Over 60 ms |
|---|---|---|---|---|---|---|
| Strings, c54 one-row lines (Sus Marc LITE) | join | 113 | 0 | 9 | 3 % | 1 % |
| Strings, c54 one-row lines | entry after a rest | 25 | +2 | 21 | 16 % | 8 % |
| Strings, legato rows | join, same row before | 271 | +8 | 37 | 31 % | 12 % |
| Strings, legato rows | join, other row before | 183 | -15 | 42 | 36 % | 15 % |
| Strings, legato rows | entry | 61 | +18 | 49 | 38 % | 26 % |
| Strings, Sus MAX | join | 102 | -13 | 61 | 52 % | 27 % |
| Strings, Sus MAX | entry | 85 | +24 | 24 | 20 % | 13 % |
| Strings, Slur Runs | join | 14 | +18 | 53 | 36 % | 21 % |
| Strings, staccato rows | entry | 33 | +13 | 19 | 9 % | 6 % |
| Winds and brass, legato | join | 239 | +4 | 21 | 11 % | 4 % |
| Winds and brass, Sus | entry | 267 | -1 | 21 | 12 % | 7 % |
| Winds and brass, legato | entry | 55 | -16 | 30 | 31 % | 15 % |

## Answer to the coordinator's question

Yes for the tempo map, partly for the rows.

- **Tempo (measured map, inferred effect).** Remove every arc, push, apex hold and beat stretch from all music printed at 126 (128-176, 270-448, 464-480, 664-679), and reduce the two second-theme spans at 112 (184-244, 584-620) to a broadening of the last two beats of a phrase. Keep the arcs of the Lento, the sostenuto (488-504), the largamente (636-648), the Più lento solo and Tempo I, the caesura at 636 and the fermata stretch at 679. Reasons: (a) the +1.5 % pushes (9 ms per beat, 75 beats in table 1) are too small to be heard as motion and only move the fits; (b) the arc ends take 5-12 % off single beats (25-65 ms on a 476 ms beat) eleven times in bars 78-110, where the score prints no change and the music drives toward a printed stringendo at bar 113; (c) bars 103-110 repeat one two-bar tempo shape four times, a periodic pattern no conductor produces; (d) bar 50 and bar 150 zigzag 107.5 / 112 / 107.5 / 103 in four beats; (e) Movement II removed all of them and its critic found no phrase that read as mechanical, and the c54 theme now sits on exactly 126 with no reported loss.
- **One row per line (measured).** The c54 result holds on the full render (table 2: Violins I 42 → 9 and 36 → 15), and the rest of the string writing still measures 30-60 ms with 12-27 % of notes over 60 ms. Extend the Sus Marc LITE treatment to the fast marked lines (finding 2 lists them). Do not put the lyrical slurred lines on it without a range test (finding 3): they need a different one-row rule.

## Findings, ranked by what a listener would gain

### 1. Unprinted tempo steps in the rest of the Allegro (measured map; effect inferred)

**Where.** Table 1, rows 128-160, 272-286, 308-440, 664-679 (126 bpm) and 184-244, 584-620 (112 bpm).

**What is wrong.** See the answer above. The same complaint Dan made about bars 15-32 ("doesn't feel like it's really playing in perfect time") applies by construction to bars 33-40 and 78-110: the steps there are the same size as the ones c54 removed (126 → 121 / 115.9 / 110.9).

**Fix.** `build/score_config.py`, a c55 block after the c54 one, same filter:
- `_C55_FLAT = ((128, 176), (270, 448), (464, 480), (664, 679))`; drop every `PHRASE_ARCS` and `TEMPO_PUSH` entry inside these spans; delete `BEAT_STRETCH` keys 284.0 and 285.0; keep 679.0. The arc (664, 679, "sub") may stay if the actor prefers the two slower beats into the fermata chord (a held chord, no rhythm to disturb); everything else goes.
- Second theme: change (184, 200), (200, 220), (220, 232), (232, 244), (584, 600), (600, 620) to the "sub" form and add their start qn to `APEX_SKIP`. Check on the printed map that no beat differs from its neighbour by more than 3 % except the last two beats of a phrase, and that bars 50 and 150 no longer alternate.
- Cost: note lengths in these spans change by up to 65 ms per beat, so re-bow fills, join fills and stop lists keyed in seconds must be refitted or keyed by qn (c54 left the fills of bars 15-32 and 131-144 unrefitted; do both sets together). Total duration changes by less than 0.4 s.
- Check: `parts.json` tempo equals the printed tempo on every beat of the four spans; the phrase-end joins of the lead lines keep their S within the limits of finding 2.

### 2. Fast marked string lines outside the theme still scatter 30-45 ms (measured)

**Where.** Violins I bars 33-40 (qn 128-158; the theme's own figure, 6 accents, 34 of 38 notes in slurs, 32 eighths; rows now Leg Slur 18, Sus MAX 9, Slur Runs 8, Leg BC 3; 16 of 31 joins change row; robust SD 40, 10 of 36 over 40 ms). Violins I and II bars 113-120 (448-480; 23 and 18 unslurred notes with accents on Leg BC / Leg Slur; robust SD 37 and 45; Violins I sit a median 28 ms late, and the C-sharp at 456.0 reaches the previous pitch's level only at +150 ms: confirmed on the spectrum). Development strings bars 77-96 (304-384: Violins I 24 of 31 unslurred, Violas 27 of 40, Violoncellos 34 of 53; robust SD 30 / 47 / 36). Violas bar 110 (438.0): the G is a Leg Slur note after a Sus MAX note with lead 0 and reaches the old pitch's level at +270 ms of a 476 ms quarter (confirmed on the spectrum).

**What is wrong.** Table 3: these lines mix three or four rows, each with its own attack time and its own lead table. Joins from another row start a median 23 ms before same-row joins; Sus MAX joins have a robust SD of 61 ms.

**Fix.** `build/score_config.py` `STEADY_LINE` (the c54 rule, same row and leads): add Violins I 128-158 (stop before the Slur Runs group at 158), Violins I and II 448-480, and the unslurred, accented spans of Violins I, Violas and Violoncellos in 304-384 (staccato notes stay on their rows, as the rule already does). Fit per-onset rows on one range render per span as c54 did, then per-note level steps (`steady_levels54.json` method). Add Violas 438.0 to `DOWNBOW_STROKE_AT` or give it a 0.09 s lead through `retongue_leads.json` if it is not inside a steady span. Target per line on the full render: robust SD under 20 ms, at most 1 note over 40 ms from the median.

### 3. The second theme and the largamente: the leading string lines are the least steady exposed lines in the movement (measured)

**Where.** Violoncellos bars 47-61 (184-244, the dolce tune, stem 2-6 dB under the master: robust SD 46, 11 of 54 over 60 ms in 184-270; 13 of 53 joins switch between Leg Slur and Leg BC). Violas and Violoncellos bars 147-159 (584-636: 53 and 43 ms, 9 of 39 and 10 of 45 over 60 ms; 10 and 14 row-change joins; the two sections are over 30 ms apart on 18 of 35 shared onsets). Violins I bars 160-166 (636-664, the fff tune: 59 ms, 6 of 20 over 60 ms, 8 of 19 row-change joins; Violins II against Violins I over 30 ms apart on 9 of 22 onsets). Examples confirmed on the spectrum: Violins I 637.0 (A-flat 6, a Leg BC note with a 220 ms lead after the Sus MAX down-bow at 636) is the louder pitch from 80 ms before the beat; Violoncellos 266.0 crosses at +190 ms.

**What is wrong.** Eighths at 112 last 268 ms; a quarter of these notes start more than 60 ms off, in both directions, on the line the listener follows. The pattern is by row: notes after a Leg BC note read early (-46 to -91 ms at 193.5, 201, 213, 601, 605.5, 613), slurred eighths after a Leg Slur note read late (+52 to +90 at 225.5, 228.5, 233.5, 265.5, 596, 621).

**Fix.** These are slurred cantabile lines, so the marcato row is not the default. Range-test three variants on Violoncellos 184-204 and Violins I 636-652 and ship the steadiest that critic A's join measure accepts:
1. One legato row for the whole line (Leg Slur MAX only; no Leg BC inside the line; `STEADY_LINE` with `row="Leg Slur MAX"`, one lead per class fitted on the range render). c54 measured this as poor on the 126-bpm theme (robust SD 47); the notes here are longer, so it may differ.
2. Sus MAX with a 45-80 ms overlap (EW-TEMPLATE-PLAN section 5) and one 90 ms lead (c54: 27 ms on the theme).
3. Sus Marc LITE as shipped in c54 (9-15 ms), with the level steps, if 1 and 2 stay over 25 ms.
In all three the fff down-bow at 636 keeps its Sus stroke and the note at 637.0 gets the lead of a bow change (0.05 s), not 0.22 s. Target: robust SD under 25 ms, no note over 60 ms, Violins I and II within 30 ms on 20 of 22 onsets in 636-664.

### 4. Bars 131-134: the four instruments on the theme are not together (measured; three single readings unconfirmed)

**Where.** Recapitulation, qn 520-536: Violoncellos (Sus Marc LITE since c54), Clarinet 1, Bassoon 1, Trombone 1.

**What is wrong.** Per onset, the spread between the earliest and the latest of the four lines has a median of 69 ms (19 onsets; 13 of them over 50 ms). Against the celli: Clarinet 1 over 60 ms apart on 6 of 18 onsets, Bassoon 1 6 of 19, Trombone 1 5 of 19. The celli themselves fail the c54 limit (robust SD 27-28, entries at 522.5, 525.0 and 528.5 read +196, +74, -65). The largest single readings (celli 522.5, Trombone 1 532.0 at -178, Clarinet 1 532.0 at +112) are pcX-only and I could not confirm them a second way; the count stays over the limit without them. The same holds in the forte restatement for the oboe: Oboe 1 against Violins I is a median 17-20 ms early with 6 of 12 (88-104) and 7 of 12 (536-552) onsets over 30 ms apart, while Flute 1 is within 30 ms on 9 of 13.

**Fix.** The open c54 item: one lead per row per track plus a pitch-pair table for Clarinet 1, Bassoon 1, Trombone 1 and Oboe 1 over 88-127 and 520-576, fitted on S from one range render (Movement II: joins outside 25 ms 97 → 26 of 263). For the celli, refit the three entry rows in `build/steady54.json` (522.5, 525.0, 528.5) and the same-pitch repeat at 524. Target: each line within ±30 ms of the celli (or of Violins I) on at least 16 of 19 onsets.

### 5. Tutti entries: unplanned spread with single sections 100-190 ms out (measured with pcX; outliers need a second check by the actor)

**Where.** S of every track that starts a note on the same beat: qn 128 (19 tracks, 10th-90th percentile spread 76 ms), 272 (84), 464 (69), 480 (88), 488 (92), 520 (72), 636 (71), 676 (90). Outliers: Double basses 272 (-100), 464 (-127), 552 (+187), 664 (-94), 676 (+129); Oboe 2 104 (-141), 128 (-73), 160 (-82); Flute 2 488 (+127); Bassoon 1 636 (+115).

**What is wrong.** Expert files spread tutti entries 36-55 ms first to last (plan section 8). Here the middle 80 % already spans 55-92 ms and one or two sections fall outside it, always the same tracks. Oboe 2 was moved in c54 by half-amplitude; S still reads it early, so the two measures disagree on its swelling attack: check with a band envelope before changing it.

**Fix.** `build/entry_leads.json`: rows for Double basses at 272, 464, 552, 664, 676 and Flute 2 488 after a band-envelope check on the stems. Then the plan's seeded per-section offset can be added on a known base. Target: 10th-90th percentile spread 35-55 ms at the eight beats above, no track over 80 ms from the median.

### 6. Comparison with c00, c49 and a recording (measured on the delivered mp3s and masters)

| | c00 (v221) | c31 | c49 | c54 | Dvořák 9/i (lossy) |
|---|---|---|---|---|---|
| Integrated loudness, LRA | -19.8 LUFS, 17.3 LU | -19.7, 14.7 | -19.8, 14.8 | -19.7, 14.3 | -14.8, 21.8 |
| 3 s level, 10th to 95th percentile | 16.9 dB | 14.1 | 14.3 | 13.8 | 23.9 |
| Band share 100-250 / 250-500 / 2-6 k / 6-14 k Hz (dB re 40 Hz-14 kHz) | -8.8 / -6.2 / -12.1 / -30.8 | -8.2 / -6.3 / -11.6 / -31.6 | -9.1 / -5.7 / -11.6 / -31.8 | -8.9 / -5.8 / -10.0 / -30.1 | -6.8 / -6.5 / -10.3 / -28.6 |
| Spectral centroid of loud frames, median and IQR | 741, 253 Hz | 799, 281 | 811, 260 | 868, 329 | 849, 370 |

- Against c49: the tone balance moved to the recording's (2-6 kHz share -11.6 → -10.0 against -10.3; centroid spread 260 → 329 against 370). String note starts: table 2 (33 against 40 ms over the Allegro, and 9-15 against 36-42 on the theme).
- Tutti stops, by qn on each render's own map, drop of the master 0.25-0.35 s after the stop (c49 → c54): bar 25 (qn 102.9) 19.9 → 20.6 dB; bar 31 (128.5) 15.6 → 16.1; bar 82 (330.9) 15.7 → 14.4; bar 137 (550.9) 20.2 → 21.0; bar 169 (678.9) 18.0 → 18.0. Four of five are no wetter than c49; bar 82 is 1.3 dB less at 0.3 s and 1.0 dB more over 0.3-0.6 s. Bar 71 (287.9) reads 16.4 → 13.0 and bar 141 (568.5) 12.5 → 8.9, but neither is a clean stop: at 568.5 Violins I play the pickup and the Violins II stem is louder after the "stop" than before it. They should not count. The limit "no wetter than c49" is met within 1.3 dB.
- The delivered range (13.8 dB over 3 s windows, LRA 14.3) is the headphone target, not a fault.

**Weakest passages now (by these measures):** the second theme in both statements (finding 3), the largamente violins (finding 3), bars 131-134 (finding 4), bars 33-40 and 113-120 (finding 2), the development's tempo wobble (finding 1).

**What still reads as a machine (inferred):** the periodic two-bar tempo shape in bars 103-110; note starts that scatter by sample row and not by musical position (early after a bow-change sample, late after a slur sample); the same tracks out at every tutti entry.

## Do not touch

The constant 126 over qn 56-128 and 504-576 and the one-row Sus Marc LITE theme lines with their per-onset rows (Violins I 9 and 15 ms); the printed ramps and the stringendo 448-464; the caesura at 636 and the fermata stretch at 679; the Lento, sostenuto, Più lento and Tempo I arcs; wind and brass legato joins (robust SD 21 ms, 4 % over 60) and the staccato tracks (13-24 ms); Flute 1 on the theme (7-10 ms); the Cello solo (16 ms); the delivery chain and the hall sends (stops within 1.3 dB of c49).

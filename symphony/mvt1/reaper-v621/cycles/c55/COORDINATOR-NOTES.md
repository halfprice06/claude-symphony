# Coordinator notes for cycle 55 (critics and actor read this first)

Under review: cycles/c54/. Read cycles/c54/CHANGES.md (tables at the top) and cycles/c54/COORDINATOR-NOTES.md "PRIORITY 1".

## Dan's standing complaint (2026-11-10), still the first concern
"the main theme that comes in at rehearsal mark A, the melody in the strings feels choppy and doesn't feel like it's really playing in perfect time/rhythm". c54 put the theme lines on one row (Sus Marc LITE, rule STEADY_LINE in tools/score_to_parts.py), removed the unprinted tempo steps over qn 56-128 and 520-576, and measured on S (cycles/c54/coordinator_scripts/theme_S.py; stable copy of the measure: symphony/mvt2/reaper-v600/tools/s_onsets.py): Violins I bars 15-23 robust SD 46 → 6 ms, notes over 40 ms from the median 15 → 1. The coordinator re-ran it on the c54 stems and got the same.
Every critic checks, within its lens, that the fix did not trade steadiness for a new fault:
- A: does the theme on a marcato-sustain row still read as slurred where slurs are printed (joins: level hole depth and length, two-pitch time), are accents not turned into bite, is the repeated c'' at the bar 15-16 barline (re-articulated, 40-80 ms late) acceptable, is "choppy" gone (every printed note sounding at least 60 % of its length, neighbours within 6 dB)?
- B: are the per-note level steps (build/steady_levels54.json) even, is the theme still over the celli by the c53 margin?
- C: steadiness over the WHOLE movement, not only the theme: list every unprinted tempo step still in the map (PHRASE_ARCS, TEMPO_PUSH, beat stretches, caesuras) with its size, and S spread per thematic line and section. Movement II removed all unprinted tempo changes and its critic found no phrase that read as mechanical. Recommend, with numbers, whether Movement I should do the same everywhere outside the Lento.

## Facts about the c54 render
1. Tempo map changed (constant 126 over 56-128 and 520-576). Comparisons with c53 must use each render's own map; state_check against c53 gives false runs. Stop lists must be fixed by qn.
2. Three stem-fix rows (basses final chord, celli 159, timpani 535) are on the c54 stems and in build/ but not in REAPER; they arrive with the next full build. Sixteen of c53's seventeen stem-fix rows were not individually checked on the c54 stems.
3. The render ran with 45 of 46 GB of REAPER memory compressed (--force-memory); the attack probe read 0 late and 38 of 39 unchanged notes are within 25 ms of c53. Treat an isolated late note with suspicion and say so.
4. String join timing between identical-data renders is not repeatable where the legato target's row differs from the row of the note it overlaps (Movement II: 33 of 163 such joins moved 25 ms or more; fixed shift per section, Violins I 105 ms, celli 59, violas 45-50, basses 112). Count row-change joins per thematic line.
5. Sampler variation on single notes 2-6.7 dB between renders; report level changes on unchanged data only for runs of notes.

## Open items from c54
- Celli theme 520-536: robust SD 28 ms, 5 notes over 40 ms (fails).
- Cor anglais 275: now +42 ms late with the Sus-head fix (was -84 early in c53, +158 late in c52). Violas 368 (-52 ms), Violins II 290 (-61 ms), Horn 1 520 (+35 ms).
- Re-bow and join fills in bars 15-32 and 131-144 were not refitted on the new tempo map; breath gaps in ms not listed on both maps.
- The other 93 slur-start joins were not re-checked after the Sus-head change. Winds: row lead per track plus pitch-pair table not done (Movement II: joins outside 25 ms 97 → 26 of 263).
- Oboe 1 F5-A-flat5: 4 of 22 notes still within 2 dB of Violins I. Celli quarter 159 +3.2 dB (target 4). Arco E2 on basses not measured. A #5 and A #6 rows from c54 are in but unmeasured. Bar 152 32nd run and the wind hang at tutti stops not done.
- Tutti-stop decays could not be verified (the stop list was in seconds of the old map): re-measure with stops by qn; limit is no wetter than c49.
- Brass tail: half step stays, no return change. Finale item 18 on the basses open.

## Techniques from the other movements not yet tried here
SCRATCH/c55-actor-notes.md and SCRATCH/c54-actor-notes.md, where SCRATCH=/private/tmp/claude-501/-Users-gooby-sandbox-claude-composes/14e09066-475e-46e9-9cac-174084980a38/scratchpad (finale items 24-45; note item 35, the delayed-rise delivery ride, for the stop decays).

## Coordinator decisions on the c55 critic reports (actor: this order)
0. **PRIORITY 1: the theme's long notes are now a stab followed by a body 8-15 dB lower** (A #1-#2, B #1; both critics, independent measures). Violins I 56-127: front minus tail median 2.9 → 9.7 dB, 12 of 33 long notes sound under 60 % of their length (c53: 1), the next note steps up over 6 dB on 23 (c53: 3); in the master the pitch band falls 12-15 dB inside notes in bars 15-22; theme over celli lower quartile +4.08 → +2.90; bar 138 Violins I top B5 9-10 dB under Violins II. Dan was told the theme is fixed; this is the part of "choppy" that c54 made worse, so it must be right in c55. Do:
   a. Skip the accent swell, accent fits (accent_fits.json) and accent_body rows on STEADY_LINE notes on the Marc row (the sample has its own front), and compensate in the level steps.
   b. Range-test two cures for notes of a quarter or longer and ship the one that measures better: (i) per-note body lift on the Marc row (about +5 dB from +0.12 to +0.32 s, held through the release; B's table), (ii) notes of 1.5 qn or longer on Sus MAX through `at` rows with the Marc row kept for the eighths. For (ii) check with paired renders that the row change does not bring back the two start times (keyswitch at least 0.15 s before the note). Targets on the full render, Violins I 56-127 and 536-576, Violins II, celli: front minus tail median under 4 dB on long notes, no more than 2 long notes sounding under 60 %, next-note step over 6 dB on no more than 3, theme over celli lower quartile at least +3.9 dB, bar 138 Violins I within 3 dB of Violins II, and S unchanged (robust SD under 15 ms, at most 1 note over 40 ms).
   c. Fit the level steps on a body window, not the first 0.3 s only (B: add it to levels54.py). Refit the ff restatement 104-128 on the full render (B #3: eighth at 119.5 is 5-7 dB under its neighbours). Celli 520-536: refit steady levels, remove the leftover lane shape at 526 (falls 21 dB) (A #3).
   d. A #6: range test to tell slurs from bow changes in the theme (overlap 0.04 s, lower velocity on slurred targets); adopt only if S holds and slurred-join holes get shallower than bow-change holes by at least 2 dB.
   Put before/after tables for a-d at the top of CHANGES.md, with S beside them.
1. **Tempo map (C #1): approved.** `_C55_FLAT = ((128,176),(270,448),(464,480),(664,679))`, delete BEAT_STRETCH 284/285, second-theme arcs (184-244, 584-620) reduced to "sub" with APEX_SKIP. Keep the Lento, sostenuto, largamente, Più lento and Tempo I arcs, the caesura at 636 and the stretch at 679. Then refit re-bow and join fills where pieces changed length, and list breath gaps in ms on both maps (also still owed for 15-32 and 131-144 from c54).
2. **Extend one-row treatment to fast marked lines (C #3)**: Violins I bars 33-40, Violins I/II bars 113-120 (456.0 150 ms late), unslurred development strings 304-384, Violas 438.0 (270 ms late). Apply 0a-0c to them from the start so they do not get the stab.
3. **Lyrical string lines (C #4)**: celli second theme 184-270, violas/celli 584-636, Violins I largamente 636-664 (637.0 80 ms early): range test of three one-row variants (Leg Slur only, Sus MAX with overlap, Sus Marc LITE) on S and on join hole depth; ship per line whichever is best; not the marcato row by default. If time runs out, do the test for the celli second theme only and list the rest as open.
4. Winds: per-track row lead plus pitch-pair table (C #5; open from c54), first for bars 131-134 (celli, Clarinet 1, Bassoon 1, Trombone 1 a median 69 ms apart) and Oboe 1 in the forte restatements. Cor anglais 275 (+42 ms) is settled inside this table.
5. B #2 bar 30 string staccatos -3 to -5 dB (rows given). A #4 Flute 1 115.5 via NOTE_END_AT. A #5 join holes (Oboe 1 95/99, Horn 1 415, cor anglais 24.0, Violins II re-bow 576.0). B #4 Oboe 1 trims at 97, 98, 100, 476.
6. C #6 tutti entries (basses at 272, 464, 552, 664, 676; Flute 2 at 488): check with a band envelope first; change leads only where confirmed. Low priority.
Closed: tutti stops are no wetter than c49 within 1.3 dB (measured by qn); bars 71 and 141 do not count. Repeated c'' at 60.0 acceptable. Delivery: finale item 35 (delayed-rise ride) may be tested on the c55 master as a delivery variant and shipped only if LUFS, LRA and true peak are unchanged and stop drops improve.
The three c54 stem-fix rows and c53's seventeen must be in REAPER after this cycle's full build; confirm on stems.

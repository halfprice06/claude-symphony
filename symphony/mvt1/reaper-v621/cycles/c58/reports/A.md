# Cycle 58, critic A: articulation and phrasing (accents, re-bows, legato, basses' eighths)

Under review: the c57 render (`cycles/c57/render/`, stems after the three stem fixes) and `build/` (the rendered data plus the level-only balance rows). Scripts and caches: `cycles/c58/critic_scripts/A/`. Everything is measured on the dry stems or read from `build/parts.json` unless marked inferred. Nobody listened. Levels "with the envelope removed" are stem levels minus the written track volume envelope (`build_reaper.py` cut before `ENV_LUA`), so they show what the instrument gives.

Not read this cycle: README.md, HISTORY.md, FINDINGS.md and EW-TEMPLATE-PLAN.md in full (I used the coordinator's notes, `cycles/c57/CHANGES.md`, `MANUAL-GAPS.md` and searches of the LEARNINGS files). `MANUAL-READING.md` has no row for c58, so no page range was read; manual pages below are quoted from `MANUAL-GAPS.md`, not re-read. EW-TEMPLATE-PLAN sections my lens touches that are still not applied: 5 (legato overlap and legato velocity, finding 4) and 6 (accents by controller, finding 1). Section 8 (repeat gaps) is applied.

Not checked: harp, timpani and percussion technique, pizzicato and tremolo rows, loop pulsing folded at 3.95 s, breath marks.

## 1. Accents: 609 printed accents have no emphasis; velocity cannot give it; CC11 can (bars 15-46, 69-83, 131-146, 167-170 mostly; all families). Measured.

State now (`acc.py`, `acc2.py`). 609 accented onsets on the pitched tracks (strings 180, winds 252, brass 177; the score prints 663 accent marks). Each accented note against unaccented notes of the same track, row and pitch at CC11 within 5 units, first 0.3 s, envelope removed: winds 0.0 dB (quartiles -0.3 / +0.4, 119 matched), brass 0.0 (-0.1 / +0.1, 108), strings on Sus MAX 0.0 (47). 94 % of wind accents and 90 % of brass accents are under 1 dB. The accented notes carry no CC11 over their unaccented neighbours (median +0 units). Front against body: -0.9 to -1.0 dB in every family; 2-5 kHz front excess -0.5 / -1.3 / -1.7 dB (strings / winds / brass), so there is no bite either. Dan's priority 4 (2-4 dB of weight) is not met anywhere.

Which rows respond to velocity (`velcc.py`: body and front level on velocity, with pitch and CC11 bins as covariates; velocity follows the printed dynamic, so only tracks where the two are not collinear give a tight reading):
- Sustain rows do not respond. dB per 10 velocity units, body: Flute 1 Sus MAX -0.01 ± 0.06, Contrabassoon +0.04 ± 0.10, Bass trombone -0.01 ± 0.12, Trombone 1 +0.13 ± 0.15, Trumpet 3 -0.07 ± 0.23, Bass clarinet Sus Non Vib -0.22 ± 0.19, Clarinet 1 -0.06 ± 0.23. Strings Sus MAX +0.6 to +0.9 ± 0.4 with velocity and CC11 correlated at 0.85-0.90, so this is not separable from CC11; fronts read the same.
- Leg Slur MAX on strings: the front (not the body) rises with velocity: Violas +0.85 ± 0.20, Violins I +0.71 ± 0.19, Violins II +0.45 ± 0.16 dB per 10; celli -0.33 ± 0.33 (none). 30 velocity units give 1.4-2.5 dB on the front only.
- Sus Marc LITE (Violins II, 19 notes, velocity 52-111): -0.8 ± 0.5 body, -1.6 ± 0.6 front: no positive response (agrees with the c55 range test).
- Rows whose level is velocity: pizzicato and the short rows (already used that way). The apparent responses of Leg BC MAX (Violins I) and LegRep RRx4 (Contrabassoon) in the table come from two notes each and are not real.
Result: no row now used for accented sustained notes can take an accent from velocity.

Level against CC11 on the sustain rows (`cccurve.py`, piecewise linear with a pitch effect, body 0.10-0.40 s). Level relative to CC11 124:

| CC11 | 88 | 98 | 100 | 104 | 106 | 110 | 114 | 118 |
|---|---|---|---|---|---|---|---|---|
| winds (714 notes) | -4.6 | -4.1 | -3.8 | -3.1 | -2.8 | -2.1 | -1.4 | -0.9 |
| brass (626) | -5.9 | -4.6 | -4.3 | -3.6 | -3.3 | -2.5 | -1.8 | -1.1 |
| strings (351) | -6.4 | -3.9 | -3.4 | -2.4 | -1.9 | -1.8 | -1.7 | -1.0 |
| Violins I Sus MAX (73) | -6.0 | -5.7 | -4.9 | -3.3 | -2.6 | -1.9 | -1.3 | -0.8 |

The 114-127 segment is the well-sampled one (winds 298 notes, brass 160, strings 55): 0.14, 0.18 and 0.13-0.17 dB per unit. The curve is not flat above 106 in this movement, but it is shallow. Between 98 and 114 the fit rests on 22-55 notes per family (strings 23), so those columns are ± 1 dB. Winds and brass are nearly flat from 88 to 98 (+0.05 and +0.13 dB per unit, 147 and 257 notes).

Where the accents sit: `DYN` gives f = 88, ff = 114, fff = 124. Accents at CC11 110-119: strings 93, winds 134, brass 75. At 80-95: 54 / 76 / 80. At 120 or more: 0 / 3 / 3. Lengths: 70 under 0.3 s, 393 of 0.3-1 s, 146 of 1 s or more.

Headroom, read from the table:
- f accents (CC11 88), with no change to the resting value: a rise to 110 for the note's length gives winds +2.5, brass +3.4, strings +4.5 dB (Violins I +4.1). A rise to 106 gives strings +4.5 (family) / +3.4 (Violins I), so 104-106 is enough on strings. 210 accents.
- ff accents (CC11 114) as mapped now: a rise to 127 gives winds +1.8, brass +2.3, strings +1.7 to +2.2 dB. Under the 2-4 dB target for winds, at its lower edge for the rest.
- ff resting lowered: strings 104 gives +2.4 dB to 124 (Violins I +3.3) and costs 0.7 dB of body (Violins I 2.0); winds 104 gives +3.1 to 124 (+3.5 to 127) and costs 1.7 dB; winds 98 would give +4.1 but puts ff on the same level as f (the 88-98 plateau), so 104 is the better value for winds here; brass 100 gives +4.3 to 124 and +3.2 to 118, and costs 2.5 dB.

Fix (instrument side, as coordinator item 2):
1. `build/score_config.py`: resting CC11 of ff at 104 on strings and winds, 100 on brass (a per-family cap on the dynamic lane, e.g. `PHRASE_SHAPE["cap"]` = {"string": 104, "wind": 104, "brass": 100} if that key caps the printed level, else `DYN["ff"]` per family); make up the body with the allowed track-level dynamic trim: ff +0.7 dB strings (+2.0 Violins I), +1.7 winds, +2.5 brass. fff stays 124.
2. Accents as CC11 for the note's whole length, flat, starting 0.02 qn before the moved note-on and returning at the note end: `ACCENT_BUMP_AT = {track: units}` exists in `tools/score_to_parts.py` (line 3397: `bumps.append((n["qn"], acc_bump_, 0.3))`); it needs the note's length in place of 0.3 and a ceiling. Values: +20 units at f (88 to 108) and to 124 at ff on strings and winds; brass +20 at f and a ceiling of 118 at ff (below the fff layer; Dan's item 8). Not on notes under 0.3 s (70 notes: leave them) and not on the 27 string notes already on Sus Marc LITE.
3. Expected: f accents +2.5 (winds), +3.4 (brass), +3.4 to +4.5 (strings); ff accents +3.1 (winds), +3.2 (brass), +2.4 to +3.3 (strings). Check after the render with `acc2.py` (matched emphasis, target 2-4 dB) and the 2-5 kHz front excess (now -0.5 to -1.7 dB; must stay under +3).
This is one flat CC11 value per accented note, which is what item 2 asks for; it is not a shape inside the note.

Where Marc rows fit. Strings: 27 accents already play Sus Marc LITE (Violins II 14, celli 6, Violas 5, Violins I 2). Their front minus body is +0.5 dB against -2.4 on Sus MAX (105 accents), with no 2-5 kHz excess (-0.4), so the row gives 2.9 dB of front weight. Its level against Sus MAX at the same pitch and CC11 differs by section: Violins II +5.4 front / +3.7 body (24 notes), Violas -0.5 / -1.4 (14), celli -5.5 / +1.0 (9, some at velocity 28-31). The row fits accented string notes of 0.3-1 s at f and ff that start a bow (130 string accents are in that length range; 45 string accents are on legato rows and must stay there). It does not fit notes of 1 s or more (c57: front minus tail 7.5 dB on the theme). Before extending it, set a row volume per section in the Opus state (`layerMatrix.rows[].volume`: Violins II about -4 dB; check the row's other users first). Brass: Marc Sus LITE failed at low velocity (MANUAL-GAPS, c47 test) and Sus Accent MAX is harsh; no Marc row fits brass. Winds: the woodwind KS Masters used here have no such row in use; CC11 only.

## 2. Re-bows: the 16 holes by cause, and what fits each (bars 6-13, 45-46, 72-76, 179-182). Measured; expected sizes partly inferred.

All 100 re-bows (`rebow.py`, `rebow2.py`, `rebow3.py`): 81 dip 3 dB or more; 21 are holes by my window (6 dB under the lower of before and after for 80 ms or more; the actor's 16 plus Violins I 724.47, celli 41.38 and 52.0, Violas 32.0, basses 166.0).

What the hole is. The new Sus MAX piece is slow, not the gap: depth does not depend on the written note-off gap (median 5.3 dB at 0-20 ms, 5.8 at 20-45, 6.0 at 45-100). On the upper strings the level 0.35-0.5 s after the re-bow is still 3.7 dB under the level before it (median, 69 re-bows), and the time back to 3 dB under is 0.25-0.30 s; on the basses it is back in 0.15 s. Starting the held note on Sus MAX would not change this here: the first re-bow of a note that began on Leg Slur MAX and the later Sus-to-Sus re-bows read the same (-3.7 and -3.8 dB, depth 5.4 and 6.1).

Three causes:
- (a) 74 automatic splits. 24 of them are in printed notes of 4.7-5.0 s (the Lento whole notes of bars 6-13, qn 20-52): `REBOW_MAX_S` is 4.5 s, so a note 0.2-0.5 s over the limit is cut in two. They include 3 holes and 19 dips of 3 dB or more.
- (b) 22 printed repeats (a new note of the same pitch in the score, e.g. Violas' whole notes C4 at 292 and 296, celli Ab at 180 after the slur). These are written bow changes.
- (c) 4 ties with a printed bow mark (Violins I 44: tie, downbow, f; basses 47: tie, upbow).

Options and sizes:
- N: no split. Hole to 0. Applies to (a) under 5.2 s: `REBOW_MAX_S` 4.5 -> 5.2 in `build/score_config.py`, and remove the frozen points of those notes from `REBOW_AT` (a note with listed points keeps them). Removes 24 re-bows. The loop (3.95 s) then runs 0.75-1.05 s past its first pass on those notes; pulse on them not measured (inferred small).
- A: alternate the pieces between the track and an idle second instance, each piece held 0.4 s into the next (the upper strings need 0.3-0.4 s to bloom). Same pitch cannot overlap on one track; on two instances it can. Expected: no hole; at most a +3 dB bump for 0.1-0.2 s where both sound (inferred, incoherent sum). Needs a pass-2 alias per section (`ALIAS_TRACKS`, source = the section, windows = every second piece, the source resting there through `TRACK_WINDOWS`) and one new generic key for the piece overlap. With only Sus MAX loaded the pass-2 project (19-20 GB) has room.
- D: double the held note on a second instance whose re-bows fall between the first's (both at -3 dB). Dip after = -10 log10(0.5 (1 + 10^(-depth/10))): 2.2-2.9 dB for the holes below. Simpler than A (one alias window per held note, `REBOW_AT` set for the alias through the alias's `"set"`), but leaves 2-3 dB.
- C: CC11 +7 units over the first 0.45 s of the new piece. My slope for strings at CC11 40-72 is 0.37 dB per unit (+2.6 dB); the Adagio's 0.6 gives +4. Not enough alone for any hole of 8 dB or more; this is also a per-note CC shape, so I do not recommend it.
- F: fewer pieces. The final chord has 29 re-bows in 16 qn (celli 8 pieces of about 2.5 s, basses 6, Violins II 6, Violas 6); `REBOW_SEG_S` 3.1 with jitter 0.45 gives pieces down to 2.4 s. Pieces of 3.6-3.9 s (just under the loop) would cut the count by a third. No size gain per hole.

| re-bow (qn) | depth dB, time 6 dB under | cause | held note | CC11 | level re the other stems | fits | after |
|---|---|---|---|---|---|---|---|
| Violins I 44.0 | 14.0, 150 ms | tie + downbow, f | 43-47, 4.8 s | 82 | -8 | A | no hole |
| Violas 36.0 | 11.9, 230 | printed repeat | bar 10 of 28-42 | 52 | -8 | A | no hole |
| Violas 296.0 (and 292.0: 8.3) | 8.4, 150 | printed repeat | 290-299.4 | 41 | -9 | A | no hole |
| Violas 725.52 | 10.6, 190 | automatic | 724-728, 8.0 s | 22 | -9 | A or D | 0 / 2.6 |
| Celli 26.52 | 13.8, 220 | automatic | 24-28, 4.8 s | 43 | -13 | N | 0 |
| Celli 180.0 | 9.6, 230 | printed repeat | 178-182 | 34 | +1 (celli lead) | A | no hole |
| Celli 289.15, 298.37 | 8.0 / 11.1, 80 / 170 | automatic (`REBOW_AT`) | 286-304, 8.6 s, 4 pieces | 34 | -8 | F to 2 pieces, then A or D | 0 / 2.4-2.7 |
| Celli 717.64, 721.87 | 9.9 / 8.5, 140 / 110 | automatic | 712-728, 9 pieces | 34 | -11 | F, then A or D | 0 / 2.4-2.6 |
| Basses 38.0 | 13.9, 100 | automatic | 36-40, 4.7 s | 61 | -12 | N | 0 |
| Basses 47.0 | 9.6, 100 | tie + upbow | 44-48 | 88 | -13 | A | no hole |
| Basses 50.34 | 7.1, 120 | automatic | 48-55, 8.4 s | 42 | -24 | leave (24 dB under the rest; inferred masked) | 7.1 |
| Basses 297.05 | 16.2, 160 | automatic | 286-304, 8.6 s | 33 | -8 | A or D | 0 / 2.9 |
| Basses 714.67, 720.0 | 8.6 / 7.8, 90 / 100 | automatic | 712-728, 7 pieces | 34 | -8 / -3 | F, then A or D | 0 / 2.3-2.4 |

Also from N at no extra cost: celli 41.38 (9.3 dB, in 40-44) and the 19 smaller dips of bars 6-13. The final chord is printed "change bow at will": real sections change at different times inside the section, which is what A and D model; on one instance per section each change is the whole section's.

Order of work: N first (config only, 3 of the 21 holes and 24 re-bows gone). Then one alias per string section covering 28-56, 286-304 and 712-728 with option A if the overlap key is written, else D. Expected count: 21 holes -> 2 or fewer with A (basses 50.34 left), about 21 -> 3 holes with D but every remaining dip at 2.2-2.9 dB.

## 3. Basses' repeated eighths: the 26 are a two-sample alternation, and every eighth peaks 140 ms after its beat (bars 27-31, 82, 131-133, 141-142, 167-169). Measured.

`bassrep.py`, `bassalt.py`. 139 repeats, all on Sus MAX, median separation 8.0 dB. Of the 26 under 3 dB, 24 are eighths at q = 126 (slot 0.24 s, written gap 90 ms, the note sounds 148 ms), 23 at CC11 113-118, and 22 read 1.2-2.9 dB. In 20 of the 26 the new note's front is 2 dB or more over the body of the note before it. The MIDI of the on-beat and off-beat eighths is identical (velocity 91, length 0.311 qn, flat CC11); the samples alternate:

| qn | peak level on the beat | off the beat | off minus on |
|---|---|---|---|
| 104-124 | -32.7 dB | -30.5 | +2.3 |
| 520-532 | -29.9 | -26.8 | +3.1 |
| 664-676 | -33.1 | -27.8 | +5.3 |
| 560-566 | -34.5 | -32.7 | +1.9 |

(these levels include the bar rows, which are flat inside each bar). The separation measure compares the dip with the weaker neighbour, so a weak on-beat note before a strong off-beat note fails: all 13 failing repeats of bars 27-31 sit on a half beat. The fault a listener hears is the reversed metre (off-beats 2-5 dB over the beats) more than a missing gap. Second reading: the loudest frame of each eighth comes 137-149 ms after the score onset (the notes are unled and sound 148 ms), so each eighth reaches its level as it ends, more than half an eighth late (S2; for critic C).

What the instrument offers:
- Round-robin reset per beat. The track already sends CC16 once per bar (`cc16` at 103.85, 107.98, ...). After a reset the first two eighths read -27 / -28 (104), -27 / -30 (108), -26 / -23 (520), -25 / -29 (526) against -33 / -29 for the following pairs; 664 reads -33 / -27 and contradicts. A CC16 0.02 qn before every beat in the eighth spans (104-124, 324-328, 520-532, 560-566, 664-676; the `rr_reset` code path) would give every pair takes 1 and 2. Expected: off minus on from +2.3..+5.3 dB to about -1..-3 dB (beats stronger), repeats under 3 dB 26 -> about 10 (inferred from four of five bars).
- "Stac On Bow RRx9" (Basses KS Master key 76, loaded by default) at the written length, velocity from CC11 (`ART_SPANS`, `full_len`): the scherzo measured 9.8-12.8 dB separation with a 76-118 ms rise. Not tried on the basses of this movement; Marc Shrt, Detache and a release cap were tried and failed (LEARNINGS c03, c13, c22). It would also bring the peak earlier than 140 ms.
- A longer gap alone does little: 150 -> 80 ms release moved 16 -> 13 of 33 in the c57 range test, and `REP_MIN_GAP` is at its 40 % cap.
Fix: test both in one pass-2 run on a basses alias over 100-126 (two `TEST_TRACKS`: CC16 per beat; Stac On Bow RRx9 with a 0.06 s lead). Keep the one with off minus on at or under 0 dB and separation median over 8 dB; guard: peak time after the beat under 100 ms. If neither passes, the alternation stays and is listed.

Other tracks, same measure: Contrabassoon 8 of 40 (Sus MAX 8 of 26 under 3 dB, LegRep RRx4 0 of 14, median 7.1 against 3.8: move its remaining Sus MAX repeats at 536-544 and 632 to LegRep RRx4, which the track already loads). Celli Sus MAX 8 of 14 at CC11 under 72 (G2 at 501-512); Violas 7 of 85, all with a written gap under 60 ms (slots over 0.6 s; `REP_MIN_GAP` did not reach them: 192, 204, 208, 212, 272, 632, 662); Violins II 4 of 7 on the Tremolo row (not repeats in the sense of S1).

## 4. Legato: overlap is written in quarter notes and comes out at 19-21 ms; legato velocity is 124. Measured; the gain from changing either is small.

`legato.py`, `joins.py`, `legvel.py`. Joins onto legato rows at a new pitch:

| family | joins | overlap p10 / median / p90 | in the reference range | velocity median | velocity 90-98 | velocity 120+ |
|---|---|---|---|---|---|---|
| strings | 720 | 19 / 21 / 28 ms | 6 % (45-80 ms) | 124 | 7 % | 87 % |
| winds | 470 | -15 / 19 / 40 | 15 % (33-58 ms) | 100 | 4 % | 1 % (45 % under 90) |
| brass | 179 | 10 / 20 / 40 | 16 % (33-58 ms) | 124 | 1 % | 79 % |

Cause of the overlap: `LEG_OVERLAP = 0.04` in `tools/score_to_parts.py` is in quarter notes: 19 ms at q = 126, 21 ms at q = 112, 48 ms at q = 50 (only the Lento is in range). No chord reaches a legato row (0 notes with another note sounding on the same track).

Does it matter on the stems? Depth of the dip at each join (envelope removed), strings: overlap 0-25 ms median 2.8 dB, p90 5.5, 8 % of joins 6 dB or more (259 joins); 25-45 ms 2.6 / 6.6 / 20 % (30); 45 ms or more 2.5 / 4.4 / 3 % (33). Winds 3.0 / 1.7 / 3.0 dB median for the three bins, brass 1.7 (0-25 ms). The median does not move; the share of deep joins falls from 8 % to 3 % on strings, with tempo confounded (the long overlaps are the Lento). Joins after a written gap do worse: strings 6.4 dB median (11 joins; Violins II 62.5, 68.5, 70.5, 76.5, 82.5 at 5.8-8.6 dB: tied syncopations that start on Leg Slur MAX 58 ms after the previous note ended, so they play the slow first-note attack).

Velocity and the transition bursts: front minus body of Leg Slur MAX targets of 0.45 s or more, strings at velocity 124: median +0.8 to +2.1 dB, 34 of 127 at 3 dB or more (Violins I 5 of 18, Violins II 4 of 25, Violas 9 of 32, celli 16 of 52); at velocity 86-98: 6 of 32. The front rises 0.45-0.85 dB per 10 velocity units on Violins I, II and Violas and not on the celli (finding 1). So 124 -> 96 takes about 1.3-2.4 dB off the fronts of three sections and nothing off the celli, where most bursts are. Transition timing moves with velocity (c03: 25-80 ms between 105 and 120), so leads would need a refit.

Fix:
1. Overlap in seconds: a generic `LEG_OVERLAP_S = {"string": 0.06, "wind": 0.045, "brass": 0.045}` in `tools/score_to_parts.py`, converted to quarter notes at the join's tempo wherever `n["end"] = e0 + LEG_OVERLAP` is set (lines 2965-3002, 3104); `FAST_LEG_OVERLAP` stays. Expected: string joins 6 dB or more deep 8 % -> about 3-5 % (inferred); no change to the median. Low risk: the old note's end moves by 40 ms, the target's lead does not.
2. Violins II 62.5, 68.5, 70.5, 76.5, 82.5 and Violas 62.5, 68.5, 70.5: start these on Sus MAX (they follow a gap, no transition can sound). Now 5.8-8.6 dB dips; expected under 4 (inferred from the Sus MAX fronts of the same bars).
3. Legato velocity: do not change it blanket. Test `LEG_VEL_SPANS` = 96 on Violas and Violins II over bars 47-61 on a range render with the legato lead + 0.03 s, twice, second kept; keep only if fronts 3 dB over the body fall (Violas 9 of 32 now) and S stays within 10 ms. The celli's bursts (16 of 52) are not a velocity effect; they are per-pitch (critic B's region gains).

## 5. Keyswitches 10-30 ms before the note they serve (for critic C's item 6). Read from the data.

Keyswitch lead under 50 ms: Violins I 100, Violins II 106, Violas 93, celli 182, Clarinet 1 59, Bassoon 1 26, Oboe 1 25, Flute 1 24, Horns a2 17, Oboe 2 16; minimum 10 ms on Violins II, Violas and celli (176, 180, 292, 300, 576, 580, 289.145), 13-14 ms elsewhere. The Adagio's minimum is 0.15 s. The attack probe reports no late note, and I found no note that measurably played the previous row, so this is a risk, not a measured fault: a re-bow piece whose Sus MAX keyswitch arrives 10 ms before it (celli 180, 289.145; Violas 292) is exactly where a missed switch would put the same-pitch note on Leg Slur MAX's slow first-note layer. Fix: in the keyswitch placement of `tools/score_to_parts.py`, put each keyswitch at max(previous note-on + 0.01 qn, note-on - 0.15 s) instead of a fixed short lead, where the previous note has ended or is on a row that ignores the switch until the next note-on. No level effect expected; it removes a cause of render-to-render differences.

## Do not touch
The 27 string accents on Sus Marc LITE (front minus body +0.5 dB, no 2-5 kHz excess); the theme on Sus MAX with its leads; `REP_MIN_GAP` (Violas 0 of 71 repeats under 3 dB at 85-110 ms gaps); Contrabassoon LegRep RRx4 (0 of 14 under 3 dB); the Lento's legato overlaps (already 48 ms); no chord on any legato row; brass and wind accent fronts free of 2-5 kHz excess (-1.3 and -1.7 dB): keep the accent ceiling at 118 on brass.

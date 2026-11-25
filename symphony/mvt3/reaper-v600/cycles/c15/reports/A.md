# Cycle 15, critic A: articulation and phrasing (render c14)

All numbers come from the c14 stems and master (`cycles/c14/render/`), `build/parts.json` (identical to `cycles/c14/rendered_build/parts.json`), `build/mockup-events.tsv`, and the c14 actor's S table (`cycles/c14/logs/render/S_c14.json`, 1383 notes on 29 lines; S = the earlier of pcX and the band crossover). Levels are RMS in dB re full scale on mono sums. Score time to seconds uses the tempo map in parts.json. I cannot listen: every verdict "by ear" is inferred and marked so. Row names are those of `ks_maps.json`.

## Manual notes

Third round. Pages read in full for this cycle's main question (which row a fast theme line can stay on): 91-99 of the May 2021 HO Opus manual (strings: long, short, effects, legato, keyswitch), and 144 (Monophonic True Legato). `loop/MANUAL-GAPS.md` read; no item there covers a one-row theme.

| Manual (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Sustain (p.91): the Sustain instruments have a bow-direction round robin "that alternates between up and down bow strokes"; they suit lines "that need a consistent sound no matter how long the notes are held". | "Sus MAX" notes inside the first theme (Violins I / II, Violas, bars 11-26, 151-170). Every "Sus MAX" note is a new bow stroke, so a line that stays on this row has one kind of start on every note. | Partly. In the violins' theme 26 of 59 notes are on "Sus MAX" and the row changes 36 times in 16 bars (finding 3). Same-row "Sus MAX" joins are the steadiest long-row class of the render (Violins I 0 of 113 outside 60 ms). |
| Marcato Sustain (p.91-92): a marcato sample plus looped sustain samples; "extra power at the start of the note". | The candidate row "Sus Marc LITE" for a one-row theme (Movement I c54). | Not used and not loaded. The manual confirms the caveat from Movement I: the start is a separate, stronger sample, so quarters and longer notes get a strong start over a weaker body. 37 of the theme's 59 notes are quarters or longer (finding 3 proposes "Sus MAX" instead). |
| Détaché (p.91): notes "longer than staccato" with "a well defined end"; they work "whether you play the samples to the end or you end the note before that". | A second candidate for the theme's eighths and quarters. The row "Detache" exists in all five string KS Masters (key 30 violins, violas, celli; 79 basses; not loaded). | Not used. Worth one range variant only if "Sus MAX" fails; Movement I c15 measured no gain over "Sus MAX" on 0.16 s notes. |
| Staccato rows (p.94): 9-16 round-robin sets; Staccato On Bow stops the bow on the string. | The theme's staccato quarters ("Staccatissimo RRx9" on Violins I, "Stac RRx9" on Violins II, Violas, Violoncellos, "Staccato RRx9" on basses). | Yes for the upper strings (joins onto short rows: median +1 ms, robust SD 13, 12 of 75 outside 25 ms). The low strings' staccato quarters are 28-95 ms late (finding 1e). |
| Legato (p.98-99): two notes need "no significant time gap"; "the first note of a phrase has no legato effect". | Every legato-row note that starts a phrase after a rest (theme entries at qn 40, 48, 72, 80, 96, 600, 608 and so on). | Followed, and it is a timing cost: 66 legato-row entries read median -14 ms, robust SD 37, 37 outside 25 ms and 15 outside 60 ms, against 0 to 1 of 8-17 outside 60 ms for "Sus MAX" entries on the same tracks (finding 3). |
| Legato Slur Staccato and the combination rows (p.99): they "add a Slur Staccato accent to notes that do not have a legato connection", and in the rows with Bow Change, Slur and Portamento "Opus decides which of the components to play based on the MIDI data". | The second theme (bars 67-82, 187-198), where the violins alternate "Leg Slur MAX" and "Leg BC MAX" 24 and 16 times, and whose first note swells in slowly. Row "StacSl Leg BC + Slur + Port MAX" (key 50 Violins I, 47 Violins II; "Stac Leg BC + Slur + Port MAX" key 90 Violoncellos). | Not used. One row could replace both keyswitched rows and firm up the entry (finding 4, range test). Movement I tried it only on repeated strokes and sextuplets. |
| Monophonic True Legato (p.144): velocity sets the transition time (110-127 shorter); "it does not affect loudness". | Brass legato targets at velocity 118-124 in f and ff (`LEG_VEL_STRONG`). | The render follows the rule, but on Horn 1 and Trumpet 1 the high velocities time worse, not better (finding 2). |
| Keyswitch (p.99) and FINDINGS section 9: keyswitches sit 40-800 ms before the note they switch. | All tracks. | No: 1627 of 2196 keyswitches (74 %) are under 40 ms before their note-on (median 12.5 ms; strings 10.7 ms). `KS_LEAD_S` 45 ms was tested in c13 and is closed; the 0.15 s test on row-change joins is still open (finding 3, variant). |

## Summary of the timing lens

On 17 theme lines (first theme bars 11-26 and 151-170, counterstatement 27-34, second theme 67-82 and 187-198; 921 notes) 384 notes are outside 25 ms and 96 outside 60 ms (measured, S). 258 joined notes have a legato row on one side of a row change; they hold 141 of the 384 and 38 of the 96. So 63 % of the notes that are off are not row-change joins. They fall into the classes of findings 1 and 2, each with one cause and one fix. The one-row theme (finding 3) is still needed for repeatability and for even levels, but it will not by itself meet the targets.

Spread between the four parts that play the first theme together (Violins I, II, Violas, Horn 1; S at each printed note, measured): bars 11-18 median 40 ms, over 50 ms at 11 of 30 notes, maximum 116; bars 151-158 median 47 ms, over 50 ms at 13 of 30, maximum 113; bars 159-166 median 63 ms, over 50 ms at 20 of 29, maximum 163 (Violins I's octaves against the rest).

## Findings, ranked

### 1. Late and early notes that are not row-change joins: five classes with fixed offsets (measured)

Where: first theme and its accompaniment (qn 40-104, 600-680), counterstatement (104-136).

Evidence and fix per class (S against the beat; fixes in `build/score_config.py` unless named):

a. "Sus MAX" notes whose note-on sits on the beat (lead 0). They are the first note of a slur group that follows the last note of the group before with a 0.01 qn gap, and slurred chord notes. 79 notes: Violins I 39 (median +25 ms, 19 outside 25, 11 outside 60), Violins II 17 (+40, 12 outside 25), Violas 8 (+65, 8 outside 25, 6 outside 60), Double basses 10 (+21), Violoncellos 5 (+20). The same row with a 60 ms lead reads +2 (Violins I, 113 notes) and +11 (Violins II, 82 notes).
   - Worst case: Violins I's theme in octaves, bars 159-163 (div., qn 634-651). All 14 notes after the first have lead 0 and read +72, +18, +36, +4, +26, +80, +22, +122, +98, +90, +34, +78, +25, +40 ms; the halves and quarters are the late ones (642, 644, 646, 647, 650). A second measure (time at which the note's own band reaches half its body level) gives +79, +105, +104, +78, +146 ms at 642, 644, 646, 647, 650. The violas and Horn 1 play the same notes at -41..+69 ms, so the top octave of the theme lags the rest by about 90 ms for three bars.
   - Fix: give these notes the row's lead. `ROW_LEAD_S` "Sus MAX": Violins I 0.09 s at 634, 642, 643, 644, 646, 647, 648, 650 and 0.06 s at 635.5, 637.5, 641, 641.5, 651.5, 653.5 (with `ROW_LEAD_KEEP_END`); Violins I group heads in 104-136 (every even qn 106-134, median +18) 0.02 s; Violins II group heads in 632-660 (every even qn, median +40) and 667, 675: 0.04 s; Violas 74, 80, 82, 84, 86, 88, 90, 96, 98, 100 (+60..+68): 0.06 s. Better, in `tools/score_to_parts.py`: the rule that gives slurred "Sus MAX" notes 60 ms should also cover slur-group heads after a gap under 0.02 qn and chord notes (new key, default off).
   - Target: these 79 notes median within 15 ms, none outside 60 ms.

b. The violas' "leggiero" eighths, bars 19-26 (qn 72-104, mf, velocity 73, "Sus MAX", 60 ms lead): 52 same-row joins, median +29 ms, robust SD 34, 28 outside 25, 10 outside 60. Per position in the group of four: head +60..+68 (class a), second +32..+44, third +17..+24, fourth +56..+112. Fix: `ROW_LEAD_S["Violas"]` "Sus MAX" over 72-104: 0.09 s on the second and third eighth, 0.10 s on the fourth (cap at 0.45 of the eighth, 80 ms: use 0.08). Confirm on a range render, because the fourth note returns to the second's pitch and S may read it late.

c. Violins I's countersubject, bars 27-34 (104-136, "Sus MAX"): the third eighth of each group reads early in 14 of 16 groups (median -34 ms, range -54..-22), the head +18, the second +10, the fourth +20. Heard lengths of the four eighths: about 170, 135, 235, 175 ms for a printed 179. Fix: third eighths (qn x.0 on odd quarters: 105, 107, ... 133) lead 0.06 -> 0.03 s; heads 0.02 s (class a). Target: all four positions within 15 ms of each other.

d. Staccato quarters in the low strings (104-136): Violoncellos "Stac RRx9" (lead 25 ms) +30, +5, +64, +23, +5, +95 ms; Double basses "Staccato RRx9" (lead 0) +60, +28, +51, +44, +4, +31 ms. The upper strings' staccato rows with 35-45 ms leads read -21..+18. Fix: `STAC_LEAD_S` (or the row lead used for `stac_leads`) Double basses 0.04 s, Violoncellos 0.05 s. The two outliers after a rest (cello 111 +64, 127 +95) are the second of two staccato quarters; check them after the change.

e. "Sus MAX" joined from a legato-row note with the 60 ms lead: Violins I -33 ms (14 notes, robust SD 21), Violins II -46 (14, SD 7), Violas -37 (10, SD 6); 28 of 38 outside 25 ms. These are row changes, but they are repeatable: the offset is fixed, because the legato note is cut at the new note-on and the "Sus MAX" stroke speaks at once. They are the eighth before each staccato quarter (43.5, 59.5, 75.5, 91.5, 603.5, 619.5) and the first eighth of the rising figure (49, 81, 97, 609, 657). Finding 3 removes them; if the one-row theme is not built this cycle, set their lead to 0.02 s.

Count (measured): classes a-d hold about 95 of the 243 misses that are not at row changes; legato-row entries after a rest hold about 30 more (finding 3); class e is 28 of the 141 misses at row changes.

### 2. Brass legato at velocity 116 and over is unsteady: Horn 1 and Trumpet 1 (measured)

Where: Horn 1 on the first theme at f and ff (qn 72-104, 600-664), Horn 1 and Trumpet 1 in the Più allegro (984-1080), Trumpet 1 in coda 2 (840-888).

Evidence: same-row "Leg Slur MAX" joins (no row change on either side), split by the target's velocity.

| Track | velocity under 116 | velocity 116 and over |
|---|---|---|
| Horn 1 | 16 joins, median +7 ms, robust SD 19, 4 outside 25, 0 outside 60 | 56 joins, median +11, robust SD 45, 32 outside 25, 13 outside 60 |
| Trumpet 1 | 37 joins, median -10, robust SD 16, 8 outside 25, 0 outside 60 | 26 joins, median +18, robust SD 50, 14 outside 25, 6 outside 60 |

Horn 1 in bars 11-18 (mf, velocity 112, lead 80-85 ms) stays within -27..+32 ms on 15 of 16 joins (the other: 51 at +47). The same notes in bars 19-26 (f, velocity 118, lead 80-82 ms) read +65, -26, -64, -21, 0, +72, -25, +108, +14, +82, -28, +92. In the recapitulation (ff): +28, -31, +50, +88, +30, -63, +48, +50, +52, +64. The values sit in three groups (about -60..-25, 0..+30, +50..+108), which is the two-valued behaviour c14 found on row-change joins, here without a row change. The c14 actor's shift list has Horn 1 moving -112 to -146 ms between two renders. The split by velocity is confounded with the dynamic (CC1 level), so the cause is inferred; the remedy is cheap to test.

Research default concerned: "legato velocity follows the dynamic" (FINDINGS section 12, `LEG_VEL_STRONG` brass ladder 100-124). This is a measured reason to cap it for brass.

Fix: `LEG_VEL_STRONG["brass"]` = `[(52, 100), (65, 106), (127, 112)]` (cap 112; `LEG_VEL_EXTRA_S` brass row for 112 already exists). Remove `LEG_VEL_EXTRA_S["Trumpet 1"]` (127, 0.02). Then one lead per track from the capped class: Horn 1 "Leg Slur MAX" stays 0.08 s, Trumpet 1 stays. Range-test qn 70-106 and 598-666 twice before the render. Targets: Horn 1's theme joins robust SD under 25 ms and at most 3 outside 60 ms in each statement (now 9 and 9); two range renders equal within 25 ms on 9 of 10 joins. If the cap does not help, put Horn 1's theme on "Sus MAX" with a 0.04 s lead in 72-104 and 600-664: its 11 "Sus MAX" joins read median +32 ms at leads of 0-40 ms, range -15..+61.

Separate, same track: Horn 1 entries on "Leg Slur MAX" after a rest: 40 -50, 64 -77, 614 -62 (lead 90-110 ms: reduce to 0.05 s), 54 +44; "Sus MAX" entries 72 -58, 664 -70 (lead 0.09 -> 0.03 s). Horn 1's stopped note at 668 ("Stop Sus", lead 0) reads +189 ms: `ROW_LEAD_S["Horn 1"]` "Stop Sus" 0.12 s.

### 3. The first theme changes row on two joins in three; one row per line (measured; expected gains inferred)

Where and what, per part. "Legato-side changes" are joined notes with a legato row on one side (the two-valued class); changes onto a staccato row are not counted, because those notes time well.

| Line | Notes | Row changes (joined) | Legato-side changes, with qn | Outside 25 / 60 ms, of which at those changes |
|---|---|---|---|---|
| Violins I, bars 11-26 | 59 | 36 (27) | 19: LS>Sus 43.5, 49, 59.5, 75.5, 81, 91.5, 97; Sus>LS 51, 83, 99; LS>BC 52, 56, 84, 88, 100; BC>LS 55, 58, 87, 90 | 15 / 1, 10 / 1 |
| Violins II, bars 11-26 | 59 | 36 (27) | the same 19 qn | 20 / 1, 9 / 0 |
| Violas, bars 11-26 | 79 | 23 (17) | 13: LS>Sus 43.5, 49, 59.5, 80, 96; Sus>LS 50, 66, 77; LS>BC 52, 56, 68; BC>LS 55, 58 | 46 / 19, 9 / 4 |
| Horn 1, bars 11-26 | 59 | 25 (19) | 11: LS>Sus 52, 68, 84, 88, 100; Sus>LS 74, 90; Marc Shrt>LS 77, 80, 93, 96 | 23 / 9, 5 / 2 |
| Violoncellos, bars 27-34 | 30 | 19 (15) | 11: LS>Sus 107.5, 113, 123.5, 129; Sus>LS 115, 131; LS>BC 116, 120, 132; BC>LS 119, 122 | 13 / 2, 6 / 0 |
| Double basses, bars 27-34 | 29 | 17 (14) | 10: LS>Sus 107.5, 113, 116, 123.5, 129, 132; Sus>LS 115, 118, 130; Stac>LS 128 | 16 / 5, 4 / 2 |
| Bassoon 1, bars 27-34 | 30 | 14 (9) | 5: Sus>LS 106, 122; LS>Sus 116, 120, 132 | 13 / 3, 5 / 2 |
| Violins I, bars 151-170 | 77 | 34 (23) | 15: LS>Sus 603.5, 609, 619.5, 657; Sus>LS 611, 626, 657.5, 670, 676; LS>BC 612, 616, 628, 660; BC>LS 615, 618 | 32 / 10, 8 / 3 |
| Violins II, bars 151-170 | 105 | 22 (16) | 12: LS>Sus 603.5, 609, 619.5; Sus>LS 610, 626, 670, 676; LS>BC 612, 616, 628; BC>LS 615, 618 | 34 / 6, 8 / 5 |
| Violas, bars 151-170 | 67 | 43 (32) | 24: LS>Sus 603.5, 609, 619.5, 635.5, 641, 651.5, 657, 678; Sus>LS 611, 626, 643, 657.5; LS>BC 612, 616, 628, 644, 648, 660; BC>LS 615, 618, 647, 650, 676; Sus>BC 672 | 25 / 4, 13 / 2 |
| Horn 1, bars 151-170 | 61 | 29 (22) | 14: Sus>LS 602, 618, 634, 650; LS>Sus 612, 616, 628, 644, 648, 660; Marc Shrt>LS 608, 624, 640, 656 | 27 / 9, 11 / 3 |

(LS = "Leg Slur MAX", BC = "Leg BC MAX", Sus = "Sus MAX". Violins I's countersubject, bars 27-34, already stays on "Sus MAX": 1 change, at 135.244.)

Why this matters beyond the S counts:
- The joins above are the ones c14 found two-valued between renders (42 of 300 moved 25 ms or more), so no lead or level fitted on them holds.
- Levels follow the row. Violins I, bars 11-18, all at one printed f: whole-note RMS per note from -35.2 (head) to -48.2 dBFS (the eighth at 49.5), 13 dB. On the sum of the four theme stems the range is 9.7 dB and the median step between neighbouring notes 2.3 dB; on the master (400-6000 Hz) 10.7 dB and 1.6 dB.
- Legato-row entries after a rest are unsteady: 66 such notes read median -14 ms, robust SD 37, 15 outside 60 ms. "Sus MAX" entries with the 60 ms lead: Violins I median -14, robust SD 33, 1 of 17 outside 60; Violins II -4, SD 17, 0 of 10; Violas -2, SD 10, 0 of 8.
- Same-row "Sus MAX" joins with the 60 ms lead: Violins I median +2 ms, robust SD 28, 40 of 113 outside 25, 0 outside 60; Violins II +11, SD 20, 22 of 82, 0 outside 60.

Which row. For Violins I, Violins II, Violas (bars 11-18, 151-166), Violoncellos and Double basses (27-34): "Sus MAX" on every note that is not staccato, the staccato quarters on their present rows ("Staccatissimo RRx9" Violins I; "Stac RRx9" Violins II, Violas, Violoncellos; "Staccato RRx9" basses). Two rows, and every remaining change is onto or off a staccato quarter (twice per two bars, with the bow off the string, as a player changes stroke there). Not "Sus Marc LITE": it is not loaded (an Opus state change on four tracks at 44-45 GB), 37 of the 59 notes are quarters or longer (8 halves, 4 dotted quarters, 1 dotted half), where Movement I measured the body 8-15 dB under the start, and MANUAL-GAPS records +4.2 / +6.7 dB at 2-5 kHz on two Violins I notes (c23), against Dan's "weight, not bite". "Sus MAX" is loaded on every string track, so the test is `--midi-only`.

Implementation: port `STEADY_LINE` from `symphony/mvt1/reaper-v621/tools/score_to_parts.py` (five sites) and set in `build/score_config.py`, variant "sus":
`{"art": "Sus MAX", "lead_s": 0.06, "tongue_lead_s": 0.06, "first_lead_s": 0.06, "rep_lead_s": 0.06, "overlap_s": 0.0, "gap_s": 0.03, "rep_gap_s": 0.05, "rr_reset": True}` on spans Violins I and II (40, 104) and (600, 632), Violins I (632, 664) with class a's leads, Violas (40, 72) and (600, 664), Violoncellos and Double basses (104, 136). Leave the staccato quarters to `STAC_ROW`. Drop the `DOWNBOW_STROKE_AT`, `leg_leads.json` and `ROW_TRIM_STROKES` rows inside the spans (they have no target left). Violins II's `ROW_TRIM_DB` "Sus MAX" -4 must not apply inside the spans (the whole line is on the row now); refit one level per span instead.

Long notes that need a level shape on "Sus MAX" (measured on the two "Sus MAX" halves already in the line, Violins I 66 and 68: first 80 ms 4.5-7 dB under the body, so an accented half swells in instead of starting with weight): the accented halves and the dotted half at 40, 52, 56, 68, 72, 84, 88, 100 and 600, 612, 616, 628, 632, 644, 648, 660. Give them lead 0.09 s and `LEVEL_SHAPES_S` `[(-0.09, 0), (-0.07, 3), (0.12, 3), (0.30, 0)]` (the form of the c10 string sf bump), the head notes 40 and 600 only +1 (finding 5). The dotted quarters (42, 58, 74, 90 and +560) need no shape. Check the first 80 ms against the body: target 0 to +3 dB.

Expected (inferred from the class numbers above): Violins I + II, bars 11-26: 35 notes outside 25 ms now, 19 of them at the 38 legato-side changes; at the same-row rate (27-35 %) about 12 of those 38, so about 28; entries 40, 48, 72, 80, 96 within 25 ms. The larger gain is that two renders agree (target: S within 15 ms on every theme note between two range renders of 37-106) and that the level range of the theme's notes at one dynamic falls from 13 dB to under 6 dB per stem.

Variants to range-test in the same lock (qn 37-106, each twice): (i) as above; (ii) the present rows with the keyswitch 0.15 s before each legato-side change on Violins I only (the open c14 test; it needs `KS_LEAD_S` per track); (iii) "Detache" on the eighths and quarters only if (i) reads a robust SD over 30 ms. Bassoon 1 and Horn 1 stay on their legato rows (Movement I: no gain from the rule on wind rows); for Horn 1 see finding 2.

### 4. Second theme in the violins: entry at bar 187 is 148 ms early, six overshot leads, and 24 / 16 changes between two legato rows (measured)

Where: Violins I, II and Violoncellos, bars 67-82 (qn 264-328); Violins I, II, bars 187-198 (744-792).

Evidence:
- Entries. Bar 67 (264), 50 ms levels: Violins I reaches -43.2 dBFS 100 ms before the beat and -39.7 at the beat (body -39.2); S +65 (Violins I), +64 (Violins II), -89 (Violoncellos). Bar 187 (744): Violins I is at -44.8 dBFS 150 ms before the beat, within 1.1 dB of its body (-43.7); S -148 ms. Violins II there reads -31. The same lead (0.30 s) and +5 dB front give +65 at one entry and -148 at the other, so the front is too much at 744 where the note speaks faster (E flat 5, p).
- Overshot leads from the c14 refit (not row-change scatter: the leads are 270-350 ms): Violins I 296 -100, 312 -92, 779 -111, 747 -75; Violins II 296 -81, 747 -57; Violoncellos 286 -178, 298 -141, 304 -167, 264 -89, 266 -62, 288 -68. Late the other way: Violins II 272 +83, 285 +91, 300 +86, 312 +63, 765 +109; Violins I 283.5 +64, 310 +73.
- Row changes: Violins I and II 24 each in bars 67-82 (all joined, all between "Leg Slur MAX", "Leg BC MAX" and "Sus MAX"), 16 each in 187-198; Violoncellos 24. Legato-side changes hold 11-13 of the 20-22 notes outside 25 ms on each line.
- Same-row "Leg BC MAX" joins are steady on the violins (Violins I 54 -15, 86 +5, 307 +33, 308 -6, 614 -14, 787 +19, 788 +3).

Fix:
1. `entry_leads.json`: Violins I 744 total lead 0.30 -> 0.17 s and remove its +5 dB front in `LEVEL_SHAPES_S` (keep Violins II 744, which is in time). Keep 264 as it is for the violins (a soft start 65 ms late on a dolce entry at 2 = 72 is acceptable, inferred); Violoncellos 264 lead 0.30 -> 0.21 s.
2. `leg_leads.json`: Violins I 296 -0.09, 312 -0.08, 779 -0.10, 747 -0.065; Violins II 296 -0.07, 747 -0.05; Violoncellos 286 -0.16, 298 -0.125, 304 -0.15, 266 -0.055, 288 -0.06 (0.9 x S). Do not refit the late ones: every one of them is a legato-side row change (two-valued).
3. Range test (qn 262-330, twice each) of one legato row for the line: (i) every joined note on "Leg Slur MAX" with one lead per track (Violins I 0.20 s, Violins II 0.25 s, Violoncellos 0.24 s: the medians of the present same-row leads), bow changes marked only by the slur gap already in the data; (ii) the combination row "StacSl Leg BC + Slur + Port MAX" (Violins I key 50, Violins II key 47; Violoncellos "Stac Leg BC + Slur + Port MAX" key 90) on the whole line at velocity 100-112 (manual p.99: the row chooses bow change, slur or portamento from the MIDI data and gives unconnected notes a firmer start, which is what the entry at 264 lacks). Variant (ii) loads one row per track: check memory first, and reject it if any join slides (portamento) where the score has no glissando. Adopt the variant with the lower robust SD and equal renders; otherwise keep the present rows.

Targets: bars 67-82 and 187-198, each violin line at most 10 notes outside 25 ms and 2 outside 60 ms (now 22 / 5, 22 / 6, 12 / 3, 15 / 2); entry at 744 within 40 ms on both violin parts.

### 5. The first theme's head: the second note is 7-9 dB under the first (measured; audibility inferred)

Where: bar 11 (qn 40 -> 42), Violins I, II, Violas, Horn 1; less at bar 151.

Evidence: sum of the four theme stems, whole-note RMS: 40 at -31.0 dBFS, 42 at -38.3 (fall 7.3 dB); master 400-6000 Hz -30.3 -> -39.5 (9.2 dB). Violins I alone -35.2 -> -43.3. The recapitulation's same join (600 -> 602) falls 3.7 dB on both. The printed marks are an accent on the half and a slur into the dotted quarter at one f; Dan's accent is 2-4 dB. The half at 40 is also the loudest note of the first eight bars by 2.8 dB (next: 52 at -33.8). The second note is a two-valued legato join (c14: -3.5 / -4.5 dB between two range renders), so trims on it did not hold.

Is it audible: yes (inferred). A 9 dB fall after the first note makes the theme's head sound like a sforzando and a subito piano; the same bar in the recapitulation shows the intended shape.

Fix: with finding 3 both notes are "Sus MAX" strokes with stable levels. Then: remove the c14 lifts on 42 (Violins II +1.5, Violas +1.5) and the head shape `[(0.05, 0), (0.15, -2), (0.70, -2), (0.90, 0)]`; fit `STEADY_LINE` "level_db" for 40 and 42 on the range render so that the sum of the four stems falls 3-4 dB from 40 to 42 (start values: 40 -2 dB, 42 +2 dB on the three string tracks). Horn 1: `LEVEL_SHAPES_S` 42 +2 dB from its moved note-on. Target: master 400-6000 Hz fall 3-5 dB at bar 11 and at bar 19 (qn 72 -> 74), bar 151 unchanged.

### 6. S1: two same-pitch repeats of the combined head figure do not separate in the master (measured)

Where: Più allegro, bars 247-250, the bass instruments' figure (Trombone 1, Bassoon 1, Violoncellos): C3 eighth to C3 quarter at 987.5 -> 988 (tenuto) and 995.5 -> 996 (staccato).

Evidence: dip under the two notes' bodies at the repeat. 995.5 -> 996: Trombone 1 3.4 dB, Bassoon 1 3.2 dB, Violoncellos 5.9 dB (its gap is 7 ms); the master's C3 band shows no dip (-0.1 dB). 987.5 -> 988: Trombone 1 1.8 dB, Bassoon 1 3.6, Violoncellos 4.4; master band 4.7 dB. The wind and brass gaps are already 77 ms and 47 ms, but the release tail fills them. For comparison the basses' hammered eighths dip 9.6 dB (coda, 82 repeats, 8 under 6 dB) and 11.3 dB (Più allegro, 161 repeats, 16 under 6 dB), and the violas' repeats in 816-832 dip 7.7-20.7 dB in the master's band.

Fix: `tools/score_to_parts.py` detach dip on these six repeats (`STR_REP_DETACH` for the cello, the wind / brass re-tongue dip for the others): a -8 dB notch over the last 60 ms before the repeat's note-on, in CC1 on Trombone 1 (CC1 is its dynamics lane) and CC11 on Bassoon 1 and the cello, not in the volume envelope (S3); Violoncellos 995.5: end the eighth 60 ms before 996 (research default: string repeat gap 90 ms). Target: stem dip 6 dB or more on all six, master C3 band 4 dB or more at both places.

Also S1, smaller: Violas 795.5 -> 796 (tenuto repeat, dip 2.7 dB stem, 3.0 dB master band) and the second of each pair in 816-832 on the stem (2.4-3.6 dB at 818, 820, 822, 828, 830 with a 50 ms gap; the master band still dips 7.7-16.9 dB there, so leave them).

## Tempo (coordinator's question)

Measured on the parts.json map, per half-note beat against the printed tempo.
- No printed tempo word is under-realised. poco rit. 49-50: 160.7, 149.9 into 144. animando 82: 150.9, 160.0 into 168. poco rit. 149-150: 156.8, 139.8 (last beat 136, -19 %). poco rit. 197-198: 160.7, 149.9. Bars 205-210: 171.5, 175.8, 178.7, 181.0, 183.0, 185.0. allargando 221-222: 127.0, 113.5 into Maestoso 112 (it lands on the new tempo without overshooting). stringendo 245-246: 140.9, 160.8 into 176. allargando 271-272: 165.3, 151.9 into 144.
- Unprinted changes over 3 % that remain: (i) the seven caesuras, each on the last half-beat before the point: bar 18 -4.0 %, 26 -4.7, 98 -4.7, 158 -4.0, 166 -4.0, 204 -3.4, 277 -4.6 (25-33 ms each; six of the seven fall on a rest or a stop). (ii) Phrase arcs without a printed breath mark, last half-beat -3.5 %: bars 54, 62, 66, 70, 78 (Poco meno mosso) and 174, 182, 190, 194 (Tempo I), 234, 238. (iii) Arcs that end on a printed breath mark: -6.0 % (bars 58, 74, 178, 214, 228) and -8.6 % (186, 218, 242); these are allowed by the brief.
- Verdict (inferred): none of these lies inside the first theme's running notes. The four at Tempo I under the muted trumpet (174, 182, 190, 194) are the only unprinted steps in a passage the score keeps at the main tempo "so it does not replay the exposition's pacing" (global.ily, c073); set those four arcs to end at -3 % or less. Leave the rest.

## Open items from c14: audible or not, with targets

- Bar 222 (allargando into the arrival): master per quarter 882-887: -25.0, -22.8, -24.8, -21.5, -20.2, -19.9; the dip at 884 is 2.0 dB inside a crescendo. Violins I: -33.8 before the bar line, -38.5 in 884.0-884.5, and again -37.2 / -39.7 at 886.0-887.0 where the line goes back to "Leg Slur MAX" for the run (it was -30.2 just before). Audible as a small sag, low priority (inferred). Target: master 884 at -23.5 or over (dip 1 dB or less). Fix: Violins I `LEVEL_SHAPES_S` 884 `[(-0.06, 0), (-0.04, 3), (0.5, 3), (0.8, 0)]`, and keep "Sus MAX" through 886-888 (`ART_SPANS` end 886.0 -> 888.0) so the run does not drop 7 dB.
- Bars 39-42: master per half bar from 152: -26.8, -30.0, -32.8, -34.2, -37.6, -39.1, -43.3, -47.1, then bar 43 -44.7. Steps of 1.4-4.2 dB, no reversal, no step over 4.2 dB. The diminuendo is right by measurement (inferred by ear). Bar 42 is not too soft: its second half is 2.4 dB under bar 43's first half, and the ride lifts both in the mp3. Close it.
- Stringendo 245-246: master per quarter 976-983: -25.6, -24.6, -26.7, -24.9, -26.8, -25.3, -24.0, -26.3, then 984 -24.1. The level is flat for two bars after rising 5 dB in bar 244, and the last quarter before the Più allegro falls 2.3 dB. Printed: cresc. molto to the ff of 247. Audible as a crescendo that stalls (inferred). Target: 980-983 each within 0.5 dB of or above the quarter before, 983 at -23.5 or over, 984 at least 2 dB over 983. This is critic C's item; from my lens the alternating quarters (+1.0, -2.1, +1.8, -1.9, +1.5) are the on-beat and off-beat pattern of the eighth runs, so even them with the run's note trims, not with a ramp.
- Violins II 300 (+83 in c14's bar-75 check, +86 in S): a "Sus MAX" > "Leg BC MAX" change. Not refittable (two-valued). It goes away under finding 4's one-row test; otherwise make 299-300 "Sus MAX" like 299.5 with the 60 ms lead.
- Basses arco 264-300 (mp throughout): per-note RMS -56.3 (264, E flat 2), -54.3 (268, D2), -55.6 (270, E flat 2), -52.6 (288, E flat 2) against -46.2..-51.7 for the 15 lower notes. The weak notes are the two highest pitches. Barely audible under the theme (inferred); fix with `pitch_trims.json` Double basses MIDI 38 +4, 39 +5 at mp in 264-304 (or `note_trims.json` 264 +5, 268 +4, 270 +5, 288 +3). Target: range 6 dB or less (now 10.1).
- Join level holes after the Horn 1 / Trumpet 1 lead changes (measured now: minimum of a 15 ms RMS within -120..+180 ms of the beat, under the lower of the two bodies). Horn 1 40-104: median 0.7 dB, 1 of 32 over 6 dB (qn 90, 6.4 dB at +137 ms). Horn 1 600-664: median -0.3, none over 6. Trumpet 1 open solo 200-264: median 2.2, 2 of 36 over 6 dB (246, 248, both before the beat). Trumpet 1 coda 2, 840-888: 3 of 10 over 6 dB, two of them after the beat (844: 6.2 dB at +98 ms; 851: 6.8 dB at +151 ms). Cor anglais 680-744: 4 of 36 over 6 dB (708: 7.8 dB at +178 ms; 732: 8.4 dB at +77 ms; 738: 10.6 dB at -46 ms). Not audible on the horn; the two late holes on Trumpet 1 at 844 and 851 are on the leading voice at ff: `LEVEL_SHAPES_S` Trumpet 1 +3 dB over 0.05-0.20 s after those two beats.
- Flute 2 at 618 / 650: own-band half-level onset Flute 2 -62 / -55 ms, Flute 1 -51 / -34 ms. The two flutes are within 11 / 21 ms of each other; both are early. Close the Flute 2 item; shorten both flutes' leads at these two notes by 0.03 s.
- Muted Trumpet 1 gaps (684, 686, 716, 718): the 45 ms gaps leave dips of 1.9-2.2 dB, the same size as the slurred joins around them (1.0-4.5 dB). The slur still reads as connected (inferred) and the two-pitch time is halved. Keep.
- `REP_OFF_FAMILIES` on winds and brass: no evidence for it in this render (wind and brass same-pitch repeats that fail do so because the release fills the gap, finding 6). Leave untested.
- Pizzicato under the solos, clarinet dal niente entries, harp at 524, ride holds: nothing against them in my lens.

## Checks with no finding (measured)

- Brass accents, Più allegro and the last bars: tilt jump (2-5 kHz minus 200-1000 Hz, first 80 ms against 150-400 ms) median -14.1..+2.4 dB per track, p90 +3.5 or under (highest: Trombone 1 in 263-279, median +2.4, maximum +3.9 at 1081). Accented notes peak 4.2-5.7 dB over unaccented ones on Trumpet 3, Horn 3 and Trombone 1 in 247-262 with no tilt jump: weight without bite. Master half-note beats 247-262: tilt jump median +0.1, p90 +2.4 dB (over +2 at 1002, 1006, 1022, 1030, led by Violins I and Trumpet 1's entries, not by an accent sample). The two large master values in the chorale (bars 224 and 226, +7.5 / +7.8) are the fff chord's release under the printed mf, not attacks.
- Held notes over 5 s: 18 in the piece. Those without a printed hairpin vary 2.9-4.1 dB peak to peak on 0.25 s RMS (Horn 1 360, Oboes 360, Horn 2 328), except Horn 1 328 (7.7 dB over 5.1 s: check for a loop step next cycle). The strings hold nothing over 5 s on one bow.
- Hammered eighths: basses' repeats dip 9.6 dB (coda) and 11.3 dB (Più allegro) at the median.

## Do not touch

The CC16 resets and restated keyswitches; `pluck_trims.json`; the `HP_CURVE` keys (bars 39-42 now fall 1.4-4.2 dB per half bar); the staccato rows of the upper strings and their 35-45 ms leads (joins onto them: median +1 ms, robust SD 13); Violins I / II's 60 ms lead on slurred "Sus MAX" joins (0 of 195 outside 60 ms); Horn 1's bars 11-18 at velocity 112 (15 of 16 joins within 32 ms); Trumpet 1's open solo at velocity 96 (10 of 41 outside 25, 1 outside 60) and its muted joins with the 45 ms gaps; the bar 90 leads (Flute 1, Oboe 1, Clarinet 1 within 25 ms); the brass accents' plain-sustain fronts (no tilt jump); the basses' beat gaps; the printed rit. / allargando / stringendo ramps and the arcs that end on printed breath marks.

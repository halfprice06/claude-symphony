# Critic C, cycle 15 (tempo, timing and transitions), on the c14 render

Data: `cycles/c14/render/` (35 stems, `00_Master.wav`), `cycles/c14/rendered_build/parts.json` (tempo map, notes, keyswitches), `build/mockup.midi` (the printed tempo steps), `build/global.ily`, and the actor's S files `cycles/c14/logs/render/S_c14.json` (full render) and `cycles/c14/logs/S_Ra.json` / `S_Rb.json` (the two range renders of one project). I ran the actor's `smeas.py` (measure S) unchanged on 17 more tracks in six tutti sections that the 29 lines do not cover (bars 1-10, 83-98, 135-150, 199-204, 247-254, 273-277; 1,620 notes), and an envelope measure of my own on the basses' eighths. Times are on the render's own tempo map. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c15-C/` (deleted). I cannot hear: "audible" is inferred from the numbers unless marked measured.

## Manual notes

MANUAL-READING has no fixed row for c15 (third round, own pages). I read p.91-99 of the May 2021 HO manual in full (string Long, Short, Effects and Legato types), because the open question is which single row a fast string line can stay on. `loop/MANUAL-GAPS.md` read; item 8 is answered in the last row.

| Manual (PDF page) | What it says | Where it applies here | Does the c14 render follow it? |
|---|---|---|---|
| p.91 Sustain | Sustain plays as long as the note is held (looped) and has a round robin that alternates up and down bows on each note. | The first theme (bars 11-26, 151-170) and F1 in the bass (27-34). 26 of 59 Violins I theme notes are already on "Sus MAX". | Partly. "Sus MAX" notes that follow a "Sus MAX" or staccato note are the stable class: 0 of 285 joins and 0 of 45 entries moved 25 ms between two renders. The theme still leaves that row 27 times in 45 joins (finding 1). Measured. |
| p.91-92 Marcato Sustain | A marcato sample plays on top of the sustain samples and "ends relatively quickly": extra power at the start of the note. | The candidate one-row patch "Sus Marc LITE" (Movement I c54). | Not loaded here. The manual's description is the coordinator's caveat (strong start, weaker body) and it applies to every note, also to the theme's slurred second notes. For the Finale's theme I recommend "Sus MAX" instead (finding 1). Inferred. |
| p.91 Détaché | Longer than staccato, with a defined end; cannot be held; "do not have a legato connection to the following note". | Detached quarters and eighths of F1. | Not used. Not needed: the staccato rows read within 25 ms on 101 of 124 notes (c14 A). Read only. |
| p.96-97 Slur Runs | 1st and 2nd Violins only; meant for very fast runs, "a minimum speed is sixteenth notes at about 125 beats per minute" (8 notes per second). | The theme's slurred eighths at 2 = 84 are 5.6 notes per second; the scales of bars 3-4 and 246 are faster. | Not used, correctly for the theme: it is under the row's minimum speed, and Movement I measured S SD 40 ms on it against 22 for the marcato sustain. Read. |
| p.98-99 Legato | Which legato type to use "depends on factors such as tempo"; a slur or portamento needs "no significant time gap"; the first note of a phrase has no legato effect; legato instruments are monophonic. | Every "Leg Slur MAX" / "Leg BC MAX" note of the themes. | The rule is followed, but the manual says nothing about a legato note entered from another row. Measured here: a legato-row note after a "Sus MAX" note took a different start time in 22 of 54 cases between two renders (finding 1). |
| p.94 Repetitions; p.98 Repetitions (Violas, Basses) | About a dozen bow changes in one sample, tempo-synced on the TS rows, not round robin. | The basses' hammered eighths (792-840, 984-1108). | Not used. The basses' own strokes are steady where they carry no extra lead (finding 4), so the row is still not needed. Read. |
| MANUAL-GAPS #8 (p.144) | Legato velocity 60-75 for slower transitions on cantabile lines. | Second theme, bars 67-82 and 187-198. | Stay closed: 14 of 140 second-theme notes are already 60 ms or more early or late; a slower transition would widen that. Measured. |

## State through this lens (measured)

- **Printed tempo words: none is under-realised.** Render tempo per half-note beat against the score's MIDI steps: poco rit. 49-50 164.0 / 157.5 / 152.5 / 147.5 (printed 160, 160, 150, 150) into 144; animando bar 82 within 1 % of 152 / 160; bars 149-150 161.9 / 152.0 / 144.0 / 136.0 (156, 156, 140, 140) into 168; poco rit. 197-198 as 49-50; accelerando 205-210 within 1.2 % of 172 / 176 / 180 / 184; allargando 221-222 133.8 / 121.0 / 115.0 / 112 (124, 124, 112, 112; the two bars last 4.00 s against 4.08 s printed); stringendo 245-246 within 1 % of 136 / 146 / 156 / 166 into 176; allargando 271-272 169.9 / 161.0 / 155.0 / 149.0 (164, 164, 152, 152) into 144. Every section tempo (168, 144, 168, 144, 112, 132, 176, 144) is exact. Total 423.83 s against 423.11 s printed.
- **Unprinted changes over 3 % that remain** (single half-note beats): the seven caesuras +3.5 to +4.9 % (qn 70, 102, 390, 630, 662, 814, 1106); phrase-arc end beats +3.7 % at 214, 246, 262, 278, 310, 694, 726, 758, 774, 934, 950; +6.4 % at 230, 294, 710, 854, 910; +9.4 % at 742, 870, 966. The -1.5 % pushes (bars 55-56, 71-72, 79-80, 175-176, 183-184, 211-212, 215-216, 223-225, 239-240) are under the limit. See finding 6.
- **The caesuras sit in silence.** At all six caesuras inside the Allegro no track has a note sounding, ending or starting in the stretched quarter (parts.json); only the harp glissando crosses the one at 1108. They lengthen a general rest by 25-40 ms and no note value.
- **Stops (fixed list by qn).** No stem hangs over. Time to -10 dB after the common note end: most stems 50-200 ms, Violoncellos 230-435 ms, Flute 2 285-295 ms, the timpani's ring 670-700 ms at bars 94, 113, 166. The timpani ring is 15-20 dB under the master at +0.3 to +0.5 s (bar 94: -53.9 against -35.0 dBFS) and the cello tail 7-11 dB under it, so neither sets the tail. Master at +0.3 s by my 50 ms measure: bar 2 16.3 dB, bar 6 16.2, bar 94 13.8, bar 113 18.2, bar 166 13.8, bar 204 13.8. The planned -4 dB fades at bars 2 and 6 are consistent with these. I ask for nothing drier or wetter.
- **Breaths and entries.** Master in 50 ms steps around each big entry: bar 27 -52 at -150 ms, -39 at -100, -35 at -50, then -31, -26, -23; bar 99 and bar 151 the same shape (body reached about 100 ms after the beat, 13-16 dB of pre-sound from the led notes in the 100 ms before it). Bar 223: -18 on the beat, -14 at +100 ms, no hole before it. Bar 278: -26 at -50 ms, -19, -17, -14. No entry is cut by a lead and no breath is filled. Nothing to change.
- **Second-theme entries (bars 67 / 187, lead 0.30 s, +5 dB front).** Violins I at 264 in 50 ms steps from -300 ms: -82 -68 -53 -48 -44 -45 (beat) -42 -44 -40 -40 -39 -36: 6 dB under the body on the beat, at the body by +250 ms. At 744: -72 -59 -52 -47 -43 -44 (beat) -44 -43 -43 -41: at the body on the beat, 4-9 dB under it in the 100 ms before. Both read as soft cantabile entries, not as late notes. Keep. S reads -148 ms on Violins I 744 because the swell has no edge; do not fit a row to it.
- **Final chord and fermata.** The fermata is printed on the half rest after the chord (all staves, qn 1114), not on the chord. The chord lasts 2.08 s (1108-1113) plus the 0.45 s ring; the file keeps 8 s after the score end. Correct as printed.
- **Keyswitch leads.** 2,528 keyswitches, median 12.5 ms before the note-on, 5th percentile 10.2, minimum 7.1 (10 under 8 ms). The audio block of the render is 10.7 ms. See finding 1 for the one place this may matter.

## Findings

### 1. Thematic string lines: the unstable joins are the ones that enter or leave a legato row. Take the first theme off the legato rows ("Sus MAX" plus the staccato row); it costs no memory (measured; the result on the theme is inferred from the stable class)

**Where:** Violins I, Violins II, Violas bars 11-26 (qn 40-104) and 151-170 (600-680); Violoncellos and Double basses bars 27-34 (104-136); second theme Violins I / II and Violoncellos bars 67-82 (264-328), Violins I / II 187-198 (744-792).

**Which row changes move.** From the actor's two range renders (same project, same data), share of joins whose S moved 25 ms or more:

| class of join (row before > row of the note) | joins | moved 25 ms+ | moved 60 ms+ |
|---|---|---|---|
| strings "Sus MAX" > "Sus MAX" | 285 | 0 | 0 |
| strings "Sus MAX" > staccato row; entries on "Sus MAX" or a staccato row | 48; 69 | 0; 0 | 0; 0 |
| strings "Leg Slur MAX" > "Leg Slur MAX", "Leg BC MAX" > "Leg BC MAX" | 79 | 2 | 0 |
| strings "Leg Slur MAX" <> "Leg BC MAX" | 109 | 8 | 6 |
| strings legato row > "Sus MAX" | 52 | 10 | 1 |
| strings "Sus MAX" > legato row | 37 | 14 | 8 |
| strings entry on "Leg Slur MAX" after a rest (in the theme: after a staccato or "Sus MAX" note) | 28 | 7 | 2 |
| winds / brass "Sus MAX" or "Marc Shrt" > "Leg Slur MAX" | 16 | 7 | 3 |
| winds / brass same-row legato | 149 | 5 | 1 |

So c14's statement "42 of 300 row-change joins" is three different classes. A change between a sustain row and a staccato row never moved. A note on a legato row after a "Sus MAX" note moved in 38 % of cases, by 90-130 ms on the violins. A change between the two legato rows moved in 7 %, but by the same 90-100 ms when it did. c14's "Sus MAX" strokes removed 14 such targets and put the row change on the next note (Violins I 51, 83, 99 are now "Sus MAX" > "Leg Slur MAX").

**Row changes inside each line** (c14 build; S of the c14 render in ms where it is 55 or more off):

| line | joins | changes | "Sus MAX" > legato row | legato row > "Sus MAX" | "Leg Slur MAX" <> "Leg BC MAX" | entries on a legato row after another row |
|---|---|---|---|---|---|---|
| Violins I 11-26 | 45 | 27 | 51 (+59), 83, 99 | 43.5, 49, 59.5, 75.5, 81, 91.5, 97 | 52, 55, 56, 58, 84 (-77), 87, 88, 90, 100 | 48, 72, 80, 96 |
| Violins II 11-26 | 45 | 27 | 51, 83, 99 | same seven | same nine | 48, 72, 80, 96 |
| Violas 11-26 | 70 | 17 | 50, 66, 77 (-64) | 43.5, 49, 59.5, 80 (+62), 96 (+62) | 52, 55, 56 (-73), 58, 68 | 48, 92 (-62) |
| Violoncellos 27-34 | 23 | 15 | 115, 131 | 107.5, 113, 123.5, 129 | 116, 119, 120, 122, 132 | 112, 128 |
| Double basses 27-34 | 23 | 14 | 115 (+102), 118 (+84), 130 | 107.5, 113, 116, 123.5, 129, 132 | none (no "Leg BC MAX") | 112, 128 (joined from the staccato row) |
| Violins I 151-170 | 61 | 23 | 611, 626 (+104), 657.5 (+93), 670 (+65), 676 (+58) | 603.5, 609, 619.5, 657 (-55) | 612, 615, 616, 618, 628, 660 | 608, 656 |
| Violins II 151-170 | 95 | 16 | 610, 626 (+122), 670 (+107), 676 (+67) | 603.5, 609, 619.5 | 612 (+78), 615 (-108), 616, 618, 628 | 608 (-55) |
| Violas 151-170 | 51 | 32 | 611, 626, 643, 657.5 (+83), 672 | 603.5, 609, 619.5, 635.5, 641 (+69), 651.5, 657, 678 | 612, 615, 616, 618, 628, 644, 647, 648, 650, 660, 676 | 608, 632, 640, 656, 664 |
| Violins I 67-82 | 47 | 24 | 284.5 | 284, 326 | 21 (296 -100, 312 -92, 268 +55, 278 -55) | none |
| Violins II 67-82 | 47 | 24 | 285 (+91), 300 (+86), 311 | 283, 299, 309.5, 326 (+58) | 17 (272 +83, 296 -81, 312 +63) | none |
| Violoncellos 67-82 | 41 | 24 | 311 | 309.5 (+66), 324 | 21 (286 -178, 304 -167, 288 -68) | none |
| Violins I 187-198 | 30 | 16 | 765 | 763 | 14 (779 -111) | none |
| Violins II 187-198 | 30 | 16 | 765 (+109) | 763 | 14 (752 -69) | none |

The other changes in each line are "Sus MAX" > staccato row (8 per violin line in the theme) and need nothing.

**First theme and F1 in the bass: one sustain row.** Play every note of these lines that is now on "Leg Slur MAX" or "Leg BC MAX" on "Sus MAX", and leave the staccato quarters on "Staccatissimo RRx9" (Violins I), "Stac RRx9" (Violins II, Violas, Violoncellos) and "Staccato RRx9" (Double basses). The line then has two rows, and both kinds of change between them are in the classes that never moved. Reasons for "Sus MAX" over "Sus Marc LITE": it is loaded (no Opus state change at 44-45 GB), it holds its level on the theme's half notes (no strong start with a body 8-15 dB under it), and c14 already measured it on this theme at f: the strokes at Violins II 50, 66, 82, 97.5 read +14, 0, +19, +26 ms and Violins I 66 and 134 -10 and +2 ms with 0.06-0.09 s leads. In the c14 render the theme's "Sus MAX" joins read Violins I median +4 ms, robust SD 15 (n 11), Violins II +34, SD 15 (one more 0.03 s of lead), against a range of -77..+59 for the legato-row notes.
- Notes that move to "Sus MAX": Violins I and II 40, 42, 48, 51, 52, 54, 55, 56, 58, 72, 74, 80, 83, 84, 86, 87, 88, 90, 96, 99, 100 (14 on "Leg Slur MAX", median length 1.3 quarters, longest 2.2; 7 on "Leg BC MAX", median 2.1) and the legato-row notes of 600-680 (17 on Violins I, 14 on Violins II, 27 on Violas); Violas 16 notes in 40-104; Violoncellos 12 and Double basses 10 in 104-136. The eighths and the staccato quarters are already off the legato rows.
- Leads by class (start values; fit once on a range render pair, they will hold because the class is repeatable): slurred join (the note before ends at the new note-on, `ROW_SLUR_OVERLAP_S` +0.03 s so its release covers the attack) 0.09 s; after a bow change (0.03 s gap) 0.06 s; entry after a rest 0.09 s; Violins II 0.03 s more on each.
- Level: "Sus MAX" plays over the legato rows at one CC11 (Violins II carries `ROW_TRIM_DB` -4). Fit one trim per track on the range render (median of the moved notes against their c14 level), then the head: with the head and the second note on one row the 8.0 / 9.3 dB fall after the head note (B #2) can be set by a level shape, which it could not while 42 was a two-valued join.
- Long notes that need a level shape: none for the sample's sake (the sustain loops at level; the longest theme note is 3.1 quarters, 1.1 s). Give each half note the lean-off the legato rows gave it: -1.5 dB from 0.3 s to the note end, as `LEVEL_SHAPES_S`.
- How: Movement I's `STEADY_LINE` rule with row "Sus MAX", or, without the port, `ART_SPANS` on the five string tracks over (39.9, 104.0), (599.9, 680.0) and (103.9, 136.0) with art "Sus MAX" for non-staccato notes, plus the `ROW_LEAD_S` / `ROW_SLUR_OVERLAP_S` spans above and `ROW_LEAD_KEEP_END`. The 14 c14 strokes and their `leg_leads.json` neighbours inside these spans lose their purpose; remove those rows so they do not stack.
- Check after the range pair: 0 notes of the three lines moving 25 ms between the two renders; Violins I and II theme notes outside 25 ms at most 8 of 59 each, none outside 60; slurred pairs (40-42, 52-54-55, 56-58) with a dip of at most 4 dB at the join and no gap; the theme's bar levels within 1 dB of c14.

**Second theme: stay on the legato rows, remove the "Sus MAX" islands.** The second theme is slow enough for legato (2 = 72; 30 of 48 notes are a quarter or longer on "Leg Slur MAX") and its "Leg Slur MAX" <> "Leg BC MAX" changes moved in only 7 % of cases. The notes worth changing are the few that pass through "Sus MAX":
- Violins II bar 75: 299 and 299.5 are on "Sus MAX" and the F at 300 enters "Leg BC MAX" from them. That is why 300 read +83 ms after its row was changed, and why Violins II differs from Violins I in the same bar. Give Violins II the rows Violins I has there (299 and 299.5 on "Leg Slur MAX", 300 on "Leg BC MAX"; Violins I measured G -34, A flat +13, F -8 ms) and set its `leg_leads.json` 300 row back to the c13 value. Do not fit 300 again before that.
- Violins II 285 (+91) and 765 (+109), Violins I 765 (+47): the note after a "Sus MAX" eighth. Either list them in `DOWNBOW_STROKE_AT` with the 0.09 s lead (as c14 did at 310), or keep the eighth before them on "Leg Slur MAX".
- One range test, one track: Violins II 264-328 with every "Leg BC MAX" target as a "Leg Slur MAX" join with the `BC_SOFT` notch (`max_cc` raised to 90 inside (264, 328)); accept only if notes outside 60 ms fall from 6 to 2 or fewer of 48 and the bow changes still show a 2-4 dB dip. Otherwise leave the two legato rows.

**Keyswitch lead.** Among legato > "Sus MAX" joins, 10 of 48 with the keyswitch under 15 ms before the note-on moved between the two renders, against 2 of 41 with 15 ms or more. The split is confounded with tempo (the 0.03 qn lead is 10.7 ms at 168, one audio block), so this is weak evidence, but it is the first number that points at the keyswitch. The untested "keyswitch 0.15 s before row-change joins" is worth one range pair on the second theme, where the rows stay.

### 2. "Sus MAX" joins are late or early by a fixed amount that depends on whether the note has a lead: notes of one line sit 55-80 ms apart (measured; repeatable class, so one lead per class holds)

**Where:** every string track. These are not row-change joins: they are the largest remaining class (142 of 362 same-row "Sus MAX" / staccato joins outside 25 ms on the 29 lines).

**Evidence** (S, same-row "Sus MAX" joins, lines and tutti sections together; n, median, robust SD):
- No lead: Violins I short notes at CC11 100+ +19 (n 28, SD 8), long notes +72 (n 13); Violins II +40 (n 22, SD 18-19); Violoncellos +27 to +34 (n 27); Violas soft +65 (n 8, SD 1).
- 0.06 s lead: Violins I -12 at CC11 100+ (n 82), -1 at 80-99 (n 64); Violins II +6 / +10 (n 104); Violas -9 / -13 at CC11 80+ (n 31), +40 under 80 (n 36, SD 30).
- 0.11 s lead (the c07 span 328-392): Violas -53 (n 31, SD 21), Violins II -39 (n 12, SD 8).
- Places where both classes meet in one line: Più allegro 984-1016, Violins I notes with the lead -29 and without it +33; Violas there -36; Violins II and Violoncellos without it +39 / +29. Introduction bars 1-10: Violins II +55 (SD 5), Violas +41, Violoncellos +30, Violins I +27, all without a lead. Violas bars 21-26 (qn 80-104, the accompaniment figure): the on-beat eighth with no lead +65 at every one of eight (SD 1), the others +20 to +112; 14 of the line's 19 notes outside 60 ms are here. Violins I 634-650 (bars 159-163): eight notes of a quarter to a half with no lead, +72 to +122; Violins I 970-976: +96 to +156.

**Fix (`build/score_config.py`, `ROW_LEAD_S[track]["Sus MAX"]` spans with `ROW_LEAD_KEEP_END`; values = present lead + S):**
1. Violas and Violins II (328.0, 392.0): 0.11 -> 0.06 s.
2. Violas (80.0, 104.0): 0.10 s on every abutting note, the on-beat eighths included (if those are `STR_REP_NEW_BOW` strokes, set the lead there).
3. Violins I (633.0, 651.0): 0.08 s; (969.0, 977.0): 0.10 s.
4. Più allegro (984.0, 1056.0): one lead of 0.03 s for every "Sus MAX" join on Violins I, Violins II, Violas, Violoncellos (it replaces the 0.06 s short-note lead on Violins I and Violas inside the span).
5. Introduction (0.0, 40.0): Violins II 0.05, Violas 0.04, Violins I and Violoncellos 0.03 s on the notes that have none.
6. As a generic rule if the actor prefers one: `SUS_JOIN_LEAD_S = {"Violins I": 0.03, "Violins II": 0.045, "Violas": 0.04, "Violoncellos": 0.03}` for abutting "Sus MAX" notes of 0.8 quarter or longer that take no other lead, doubled under CC11 80.

**Targets:** each class median within 15 ms; Violas bars 11-26 from 46 / 19 to under 25 / 5 outside 25 / 60 ms; Violins I recapitulation from 32 / 10 to under 22 / 4.

### 3. Codetta, bars 91-93 (qn 360-372): the low brass and Horn 1 strike 25-73 ms before the beat and the strings 27-73 ms after it (measured)

**Where:** the ff hammer strokes before the stop of bar 94, and the brass entries of the closing group from qn 328. Not in the 29 lines.

**Evidence** (S per stroke at 360 / 364 / 369): Trombone 1 -73 / -52 / -47, Bass trombone -37 / -22 / -24, Horn 1 -63 at 360 (-62 median on its five entries of 328-360, SD 3), Trumpet 2 -35 / -42 / -12; against Violins II +56 / +41 / +68, Violas +56 / +54 / +57, Double basses +52 / +31 / +39, Violins I +73 at 369, timpani +14 / +10 / +14, Trumpet 1 +2 / +3 / -17. The spread between the first and the last part is 129, 166 and 120 ms on these three chords; over the section the middle half of the parts spans 42 ms and only 59 % of parts are within 30 ms of each chord's median (bars 199-204: 32 ms and 73 %). The tuba is -95 and -97 at 362 and 366 and within 26 ms elsewhere. By class: brass "Sus MAX" entries with the 0.09 s lead read -42 to -62 (Horn 1, Trombone 1, Trumpet 2), with 0.05 s -20 to -25 (Trombone 1, Bass trombone, SD 2-7); the same tracks' entries in bars 199-204 read -9 to +15.

**Fix (`build/entry_leads.json`, negative extras; these are sustain-row entries, which did not move between renders):** Trombone 1 360, 361.5, 364, 365.5, 369: -0.05; Trombone 1 362, 366, 372 and Bass trombone 360-372 (all nine): -0.02; Horn 1's entries of 328-360 that carry the 0.09 s lead: -0.06; Trumpet 2 360, 361.5, 364, 365.5: -0.04; Tuba 362, 366: read the realised lead and cut it by 0.09. Strings, positive extras: Violas and Violins II 360, 364, 369: +0.05; Double basses 360, 364, 369, 371: +0.04, 372: +0.08; Violins I 369: +0.06. Print the realised lead of every row (`LEAD_WARN_S`); a negative row on a note without a lead does nothing.

**Target:** every part within 30 ms of the timpani on the nine strokes of 360-372; first-to-last spread under 70 ms.

### 4. The basses' eighths limp in the last two sections: on-beat strokes 32 ms early, off-beat strokes 22-36 ms late (measured twice, S and envelope)

**Where:** Double basses 1088-1108 (bars 273-277, Largamente) and 1056-1088 (bars 265-272).

**Evidence:** half-rise time of each eighth on the stem (30-2500 Hz, 6 ms frames) against the grid: 1088-1108 on-beat -32 ms (n 20, SD 1), off-beat +22 (n 20, SD 19); S gives -37 and +33 (SD 1 each). The on-beat strokes carry c12's 0.03 s lead, the off-beat strokes none. An eighth is 208 ms there, so the strokes alternate about 262 and 154 ms. In 1056-1088 no stroke has a lead and the off-beat ones are late: on-beat -6 (SD 1), off-beat +36 (SD 20). In 792-816 and 984-1016 the two differ by 9-10 ms (+9 / +18, +2 / +12): steady. The c12 lead was fitted on pcX, which Movement I c54 showed cannot time a same-pitch repeat.

**Fix (`build/score_config.py`, the c12 block near line 731):** delete the `(q_ - 0.02, q_ + 0.02, 0.03)` rows for q in 1088..1107 and add `(q_ + 0.48, q_ + 0.52, 0.02)` for the off-beat eighths of 1088-1107 and `(q_ + 0.48, q_ + 0.52, 0.035)` for 1056-1087, with the span (1055.98, 1108.0) in `ROW_LEAD_KEEP_END`. The beat-gap dips end at the moved onset, so check that the dip before each beat still ends at the on-beat note-on. **Target:** on-beat and off-beat medians within 10 ms of each other and of the grid, measured by the envelope half-rise, not by pcX.

### 5. Winds and brass: three fixed offsets and one wrong pair extra (measured)

- **Clarinet 1, "Leg Slur" joins:** +23 ms median, robust SD 10, n 40 (13 outside 25 ms; +22 to +25 in each of bars 135-150, 199-204, 247-254). `LEG_ART_EXTRA_S["Clarinet 1"] = {"Leg Slur": 0.02}`. Expected 13 -> about 2 outside 25 ms.
- **Oboe 1, "Sus MAX" entries with the 0.07 s lead:** -45, -48, -50 ms in bars 135-150, 199-204 and 273-277 (n 14, SD 5-12). Cut that entry lead to 0.03 s for Oboe 1 (the six entries of bars 1-10 read +48 and are a different class; leave them). Pairs: `LEG_PAIR_EXTRA_S["Oboe 1"]` (79, 77): +0.06 (S +68, +70 at 992, 1008), (77, 76): +0.035 (+39, +39), (74, 72): -0.035 (-41, -33, -52, -32, +4).
- **Horn 1, pair table** (77 same-row legato joins: median +8, SD 36, 39 outside 25 ms; of the 66 notes whose pitch pair occurs twice or more, 49 are within 25 ms of their pair's median, so pairs explain most of the spread): `LEG_PAIR_EXTRA_S["Horn 1"]` (59, 62): +0.05 (S +47, +72, +50, +50 at 51, 83, 611, 643); (50, 53): -0.06 (-64, -63 at 81, 641); (65, 64): -0.13 (-152, -128 at 993.5, 1009.5: these carry `LEG_EXTRA_S["Horn 1"] {65: 0.15}`, the source-pitch extra, which is wrong for this falling semitone).
- **Legato-row entries that are early:** Trumpet 1 200 (-89) and 984 (-88), Trombone 1 984.5 (-124) and 988 (-148): `entry_leads.json` -0.06 on the trumpet's two, -0.10 on the trombone's two. These are legato-row entries, the class that moved in 2 of 28 wind and brass cases; check them on the range pair first.

### 6. Tempo: keep the map; two optional trims (measured map, inferred benefit)

Nothing printed is missed and the Allegro themes carry no unprinted change except the caesuras, which fall in silence. Two places are worth a decision:
- **Bars 171-198 (qn 680-792) run at Tempo I, 2 = 84.** The score keeps the recapitulated second theme at the main tempo (comment in `global.ily`: no meno mosso here), yet the arcs move single beats between 153.5 and 170.5 (qn 742: +9.5 %, 710: +6.4 %, 694 / 726 / 758 / 774: +3.7 %, pushes -1.5 %) over a pizzicato accompaniment, which marks every beat. Movement II removed such changes in its Allegro and lost nothing. Option: set (728, 744) from "main" to "sub" (+9.5 -> +3.7 %; the printed breath at 744 keeps a lengthened beat) and drop the -1.5 % pushes in 680-792. The arcs of bars 51-82 (Poco meno mosso) stay.
- **Caesuras at 72 and 632** stand inside the theme (bars 18 / 19 and 158 / 159). They delay the second phrase's entry by 30 ms against the pulse, which is the size of the timing error this cycle is trying to remove. Option: delete these two; keep 104, 392, 664, 816, 1108 (section entries). After either change: `--midi-only --tempo` on all tracks, and compare re-bow fill keys with the built positions (LEARNINGS c12).

## Answers to the coordinator's items

- **B #2, first-theme head (fall 8.0 / 9.3 dB):** audible as an accented head with a swallowed second note (inferred). The second note is the join after a legato-row entry (40 moved -41 / +3 ms and 48 -56 / 0 between the two renders). It is solved by finding 1, then a level shape; target a fall of 3-5 dB.
- **Bar 222 (dip 2.0 dB):** measured cause: at qn 884 every string and wind part starts a new note together (stem step into the quarter: Violoncellos -7.6 dB, Violins II -4.8, Clarinet 2 -4.8, Double basses -4.2, Flute 2 -4.1, Oboe 1 -3.0, Violins I -2.5) while the brass only arrive during that quarter (+6.5 to +8.5 dB, +3 to +7 more at 885). Master per quarter 880-888: -31.0 -27.4 -23.2 -21.5 -23.6 -20.0 -18.8 -18.5, then -14.4. Slightly audible; target 1 dB. `LEVEL_SHAPES_S` at 884.0 `[(-0.05, 0), (0.0, 3), (0.35, 3), (0.6, 0)]` on Violoncellos, Violins II, Double basses and +2.5 on Violins I (after the fader, so the hall is not cut).
- **Bars 39-42:** the diminuendo is right. Master per quarter from 152: -24.9 -25.7 -28.4 -29.1 -31.6 -31.6 -32.3 -34.8 -36.4 -35.9 -36.8 -38.1 -40.6 -41.9 -45.1 -47.2: no step over 2.7 dB, 2.5 dB into bar 42. Bar 42 is not too soft: it is the hairpin's end and the ride lifts it 10 dB in the mp3. Leave it.
- **Stringendo 245-246, "uneven quarters":** not a fault. The low quarter is 983 (-25.0 after -22.6): Horn 1 falls 11.4 dB, Horn 2 7.7, Trumpets 1-2 4.2-4.9, Clarinet 1 8.6 because their tied notes end at 983 and beat 4 is their rest before the Più allegro, while Violins I / II rise 2.0 / 2.6 dB. Only the Violas' -7.6 dB into 983 is worth a look by B. Close it.
- **Violins II at qn 300:** a "Sus MAX" > "Leg BC MAX" join (finding 1); change the rows, not the lead.
- **Keyswitch 0.15 s test:** see the last paragraph of finding 1. **`REP_OFF_FAMILIES` on winds and brass:** no evidence for it in this lens; the wind and brass notes that moved between renders are legato-row notes after another row (7 of 16), not repeats.
- **Not measured this cycle:** the join level holes after the Horn 1 / Trumpet 1 lead changes, Flute 2 at 618 / 650, the basses' arco notes 268 / 270, the muted trumpet gaps, the dal niente entries, the harp at 524, the pizzicato line.

**Do not touch:** the tempo map's printed ramps and section tempos (every printed word is realised within 3 % per beat, except the smoothed first beat of each ramp); the caesuras at 104, 392, 664, 816, 1108 and the arcs of bars 51-82; the returns, sends and release fades (no stem hangs over at any stop; nothing drier); `FINAL_RING` and the final chord's length; the entries of bars 67 / 187 with their 0.30 s lead and +5 dB front; the staccato rows and their leads (no staccato-row note moved between renders); the pre-roll and section CC16 resets with the restated keyswitches; the basses' strokes in 792-816 and 984-1056 (on-beat and off-beat within 10 ms); the bar 90 leads; the 0.045 s gaps of the muted trumpet; `HP_CURVE` (bars 39-42); percussion on the grid (timpani +7 to +14 ms, SD 3-10, in all six sections); and the closed items in the coordinator's list.

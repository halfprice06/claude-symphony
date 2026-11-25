# Critic B, cycle 55: balance and levels (c54 render)

Under review: `cycles/c54/render` (main and pass-2 stems with the three stem fixes, the master), `build/parts.json`, `build/steady_levels54.json`, `build/steady54.json`, `build/accent_fits.json`, `build/accent_bodies.json`, `build/score_config.py`, `cycles/c54/CHANGES.md`. `cycles/c55/COORDINATOR-NOTES.md` was read first.

Method. Dry per-track stems (returns excluded), K-weighted, 4096-sample Hann FFT, hop 1024, stereo power, windows in score quarter notes on each render's own tempo map (c53: `cycles/c53/rendered_build/parts_after_fix.json`; c54: `build/parts.json`). This is the scale of the actor's `q54.py`; I reproduce its c54 rows (celli minus Violins I 97-99: -1.8 -1.2 -2.7; Oboe 1 median -5.4; timpani 7.0 6.0 6.1 6.0). Only differences are used. Per-note values: "front" = score onset +0.02 s to +0.30 s, "body" = +0.30 s to the next score onset, on notes of 1.5 quarters or longer. Fine envelopes are broadband RMS in 60 ms windows. "After the fix" numbers are dB additions to the measured frames, not renders. Nothing was rendered; REAPER, the lock, `build/`, `tools/` and `~/.rpr-bridge` were not touched.

## Answers to the coordinator's questions for critic B

**1. Are the per-note level steps even?** The fronts are, on four of five Violins I spans. The long notes are not, and that is the main fault of this render (finding 1). Measured on the full c54 render:

| line | front residual SD against the printed shape, c53 → c54 (dB) | front steps over 4 dB between neighbours | long notes: body minus front, median, c53 → c54 |
|---|---|---|---|
| Violins I 56-88 | 2.0 → 1.1 | 4 → 0 | -0.7 → -8.8 (7 notes) |
| Violins I 88-104 | 1.7 → 0.4 | 0 → 0 | -2.5 → -6.2 (1) |
| Violins I 104-128 | 1.8 → 2.4 | 5 → 3 | -2.1 → -8.9 (5) |
| Violins I 536-552 | 1.7 → 0.5 | 0 → 0 | -3.2 → -10.0 (1) |
| Violins I 552-576 | 3.8 → 1.2 | 4 → 0 | -1.7 → -6.6 (6) |
| Violins II 104-128 | 2.4 → 2.0 | 5 → 3 | -1.3 → -5.0 (5) |
| Violins II 552-576 | 2.9 → 1.7 | 2 → 2 | -2.0 → -5.6 (6) |
| Violas 104-128 | 1.9 → 1.9 | 4 → 5 | -1.6 → -1.7 (5) |
| Violoncellos 520-536 | 2.5 → 1.2 | 4 → 0 | -0.5 → -5.4 (4) |

The steps were fitted on the first 0.3 s of each note (`levels54.py`), so they level the fronts and say nothing about what follows. The ff restatement (104-128) was not refitted on the full render and is less even than c53 on Violins I (finding 3).

**2. Is the theme still over the celli by the c53 margin?** The median is (Violins I minus celli per quarter, 56-88: +6.36 → +6.50). The lower part of the distribution is not: lower quartile +4.08 → +2.90, quarters under +3 dB 5 → 8, quarters under 0 2 → 3 (quarter 71: +0.9 → -4.3). The celli are unchanged within 1.2 dB in every quarter; all of the loss is Violins I in the quarters that hold the body of a long note (quarter 57.. : 17.2 → 15.4, 60: 15.3 → 11.7, 63: 14.8 → 10.1, 66: 15.9 → 15.0, 71: 11.8 → 7.0, 79: 19.9 → 14.1, 82-83: 22.5, 16.6 → 17.4, 12.1). With finding 1's fix simulated the margin returns to median +6.51, lower quartile +3.94, 5 quarters under +3, 2 under 0, which is c53's distribution.

Other spans, melody group minus the sum of all other dry stems (median / lower quartile, c53 → c54): 88-104 -1.6 / -2.8 → -1.5 / -3.9; 104-128 -1.9 / -4.5 → -2.9 / -4.2; 520-536 -0.6 / -1.9 → -1.2 / -1.6; 536-552 -0.9 / -3.2 → -2.4 / -3.6; 552-576 -0.8 / -2.0 → -1.0 / -2.6. Every span lost 0.1-1.5 dB of median margin; the three worst quarters are 549-551 (-5.4 -7.5 -4.8 → -10.6 -10.9 -10.1).

## Manual notes

No row for c55 in `loop/MANUAL-READING.md` (third round: critics pick their pages). Read in the May 2021 HO manual: p.90-91 (Hollywood Strings instrument types, Marcato Sustain), p.99-100 (Sustain, Sustain Accent, Sustain Marcato Long and Short); also `MANUAL-GAPS.md`, `DIGEST.md` row for "Marcato Sustain", and `loop/LEARNINGS.md` entries c23, c24, c33 on this row.

| Reading (2021 manual, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Marcato Sustain "plays a marcato sample in addition to the multiple sustain samples. The marcato sample ends relatively quickly" and gives "extra power at the start of the note" (p.90-91). | Every theme note since c54 (Sus Marc LITE: 117 Violins I notes, 51 Violins II, 27 Violas, 19 celli). | The row is used as a general sustain. On eighths the marcato sample is the whole note, which is why the fronts are even. On dotted quarters and longer the marcato sample ends and the note falls to the sustain layer: 1-5 dB from the sample alone (finding 1). |
| In the brass Sustain Marcato patches velocity sets a low-pass filter on the marcato samples: harder notes are "harsher" in the attack (p.100). The strings page does not say what velocity does on Marcato Sustain. | Accented theme notes are sent at velocity 103, the others at 83. | Not verified for strings. Measured: 2-5 kHz in the first 0.1 s against the body on the 20 accented Violins I notes, median +1.3 dB in c53, +6.8 dB in c54 (range -0.1 to +10.7); BRIEF item 8 names 7-13 dB as the harsh range. Most of this is the low body, and finding 1's lift removes 3-8 dB of it. Lens A should check the rest. |
| Sustain Accent: velocity is the loudness of the attack, the Mod Wheel the loudness of the sustain (p.100). | An alternative for the accented long notes if the Marc row's front stays too far over its body. | Not used; no need if finding 1's fix measures well. |

`loop/LEARNINGS.md` c24 already holds the rule this render breaks: "Sus Marc LITE carries its level in its first 0.25 s ... Set the step from the body (+0.30 s on) and trim the front on its own", and c33: hold such steps through the release.

MANUAL-GAPS still open for this lens: #12 Felt Cresc rolls, #5 expressive rows for wind solos, #4 Mid mics on winds. None explains a level problem found here.

## EW-TEMPLATE-PLAN sections this lens touches

Section 7 (per-note lean-off inside slurs: a median of -2 controller units by 0.4-0.8 s, "the phrase swell carries the line") is listed in c54's CHANGES as not applied. The c54 theme now has the opposite of it at ten times the size: each long note leans off 6-10 dB (finding 1). Section 10 ("doublings share one curve") holds in the lanes for the theme's octave doublings, but the per-note steps differ by up to 8 dB between the three octaves on one note (finding 3). Not applied and unchanged since c53: section 5 (legato overlap; the theme has none by design), section 6 (two tracks per string section), section 8 (tutti entry spread), section 10 beat-position velocity outside the listed spans. Applied without a level problem: sections 1, 3, 9.

## Checks that pass (measured)

- c54's B rows, re-measured: celli minus Violins I 97-99 -1.8 -1.2 -2.7; melody group minus celli 156-159 +4.0 +7.4 +4.7 +3.8 (with the stem fix; 0.2 short at 159, no action); celli accent 526 2.9 dB; celli minus Violins I 557.0 / 557.5 -2.6 / -3.4; bass clarinet minus tuba -6.9..-1.0; Oboe 1 minus Violins I median -5.4; timpani under the theme group 7.0 6.0 6.1 6.0.
- Printed f is now the same level in the first and the last statement of the theme: fronts of bar 15 (56.5-59.5) 14.4 17.4 13.7 16.0 13.7 against bar 143 (568.5-571.5) 16.0 19.1 15.9 15.6 15.5. In c53 bar 143 was 4-10 dB under bar 15 at the same mark (4.8 13.2 10.9 10.7 8.1). Keep.
- Dynamic mapping by family, median of full quarters under one printed mark with no hairpin (c54): f winds 3.4-8.3, horns 6.6-8.1, trumpets 8.6-12.4, trombones and tuba 9.9-12.4, timpani 12.7, strings 3.8-15.8; ff winds 8.4-15.3, horns 12.7-14.5, trumpets 15.2-18.3, low brass 13.6-17.4, timpani 15.2, strings 11.2-19.0; pp winds -8.7..-0.4, brass -9.1..-5.0, strings -7.2..-2.6, timpani -9.7. Each track rises with each mark from mf up; no track changed its median by more than 0.6 dB against c53 except those c54 changed on purpose (Oboe 1 -1.5..-3.3, bass clarinet fff -5.0, the theme strings -0.3..-1.4, basses p +2.9 and ff +1.1 from the resets and pitch trims).
- Trumpets and percussion, unchanged data, equal to c53 within 0.6 dB: Trumpet 1 against Violins I at 636-641 25.4-26.6 against 25.8-27.7; tam-tam fff 484-488 5-9 dB under the sum of the other stems; cymbal stroke 636 16 dB under the rest; tam-tam pp 696 9 dB under. Timpani is the loudest dry stem in 7 quarters (0, 1, 2, 106, 384, 524, 560), as many as c53; 106 and 560 are new and come from finding 1 (the Violins I body there fell 4-5 dB).
- Double basses arco E2 (open item): -2.0 dB against the track's own controller fit (6 notes; c53 -4.1). Within the 2 dB target on this K-weighted measure (inferred pass; low notes read low on it).

## Findings

### 1. Every long theme note is a stab followed by a body 6-10 dB lower (measured); this is audible as the choppiness Dan names, and it puts the melody's held notes under the accompaniment

Where. All STEADY_LINE notes of 1.5 quarters or longer: Violins I 57, 62, 65, 70, 73, 78, 82, 100, 105, 110, 113, 118, 120, 548, 553, 558, 564, 569, 574; Violins II 78, 105, 118, 120, 558, 564, 572, 574; Violas 105, 118; celli 521, 526, 529, 534. These are the goal notes of each motif (the accented dotted quarters) and the held top notes of the cadence chords.

Evidence.
- Front minus body per note, c53 → c54 (dB): Violins I 57 Eb5 2.2 → 8.9; 62 Ab4 0.5 → 9.0; 65 F5 0.3 → 10.2; 70 G4 0.6 → 6.8; 73 0.7 → 7.7; 78 (sf) 1.8 → 8.8; 82 1.9 → 7.4; 105 2.7 → 8.9; 110 2.1 → 9.5; 120 0.9 → 9.9; 548 3.2 → 10.0; 553 -0.6 → 7.0; 558 1.5 → 7.3. Rule 4 asks 2-4 dB for an accent.
- 60 ms envelope of Violins I 57 (dBFS from -60 ms): c53 -36 -33 -32 -30 -34 -34 -33 -35 -34 -35 -35 -34 -36; c54 -38 -34 -31 -30 -35 -38 -39 -42 -42 -44 -43 -44 -44. The c54 note is 9-10 dB under c53 from +0.3 s to its end, and the eighth that follows it starts 5-8 dB above that body (body 8.4, next fronts 13.7 16.0 13.7). The same at 62, 65, 82, 105, 120.
- Two causes add up. (a) The volume lane still carries the accent swells fitted in c15-c25 for rows with a slow front (`build/accent_fits.json` Violins I 57: 4.5, 62: 5.0, 65: 5.0, 73: 4.5, 82: 5.0, 105-120: 4.5, 548: 3.11; `build/accent_bodies.json` 57: -2.4, 110: -3.0, 120: -1.8): the lane falls from -2.4 dB at 57.06 to -9.3 at 57.84, from -1.9 to -6.9 at 62, from -2.0 to -7.3 at 548. (b) The Marc row's own marcato sample ends (manual p.90-91): 1-5 dB more. `levels54.py` measures only the first 0.3 s, so the step is set from the front.
- Whole-note level of the accented dotted quarters fell 2.4-5.3 dB against c53 (57: 17.0 → 14.6; 65: 18.4 → 14.8; 82: 22.0 → 16.7) while the unaccented eighths rose 2-6 dB (56.5: 8.7 → 14.4; 59: 12.8 → 16.0; 64.5: 8.7 → 14.9). The printed accents now carry less sound than the notes around them.
- Bar 138 (qn 548-552, f, accent, tutti chord with Violins I and Flute 1 on the top B5): Violins I per quarter 549-551 18.6 15.1 4.0 (c53) → 8.8 9.2 -2.6; Violins II 18.2 18.3, Violas 18.7 19.4, Oboe 1 13.1 13.4, Trumpet 1 15.1 14.9. The top voice of the chord is 9-10 dB under each inner string section and 4 dB under one oboe.
- Bar 26 (qn 100-104, ff): Violins I 22.4 → 17.8 at 101 against Violins II 20.7. Bar 140 (558 Ab5, 3.5 quarters): Violins I 22.0 19.5 → 16.6 16.4 at 559-560, where the timpani become the loudest stem.
- 2-5 kHz front against body on the accented Violins I notes: median +1.3 → +6.8 dB (57 +5.6, 62 +8.5, 65 +8.7, 110 +9.7, 120 +10.7, 125 +10.1).

Fix (level only; can be made on the stems with `tools/stem_fix.py` and verified before any render).
1. `build/accent_fits.json` and `build/accent_bodies.json`: set the entries on STEADY_LINE onsets to 0 (Violins I 57, 62, 65, 73, 82, 105, 110, 113, 118, 120, 548, 558, 564, 569; Violins II 105, 110, 113, 118, 120, 558, 564; Violas 105, 110, 113, 118, 120; celli 521, 526, 529). The Marc row supplies the front; a swell on top is not needed. Add the removed swell value to the same onset in `build/steady_levels54.json` so the front level stays where it is (for example Violins I "57.000" -8.9 → -4.4 with the 4.5 swell gone and the -2.4 body cut gone).
2. The rest of the sag as a body lift per note, in `build/score_config.py` `LEVEL_SHAPES_S[track]`, row `(onset, [(0.20, 0.0), (0.36, L), (E - 0.04, L), (E - 0.01, 0.0)])` with E the next note's moved onset in seconds after this onset. L is the total lift below minus what step 1 already removed (swell plus body cut of that onset). Total lifts (c54 body to the lower of the c53 body and front minus 2 dB): Violins I 57 +6.9, 62 +7.0, 65 +8.2, 70 +4.6, 73 +4.6, 78 +5.3, 82 +5.4, 100 +3.0, 105 +6.9, 110 +7.5, 113 +5.1, 118 +3.7, 120 +7.9, 548 +8.0, 553 +5.0, 558 +4.2, 564 +2.5, 574 +3.4; Violins II 78 +4.1, 105 +3.0, 118 +3.4, 120 +6.3, 558 +3.0, 564 +2.6, 572 +6.1, 574 +3.2; Violas 105 +3.2, 118 +2.2; celli 521 +2.2, 526 +6.6, 529 +3.1. Also Violins I 569 (front minus body 8.8): remove its 4.5 swell and -2.2 body cut as in step 1.
3. `cycles/c54/actor_scripts/levels54.py`: add the body window (+0.30 s to the next onset) for notes of 1.5 quarters or longer and print front minus body; make "front minus body 2-4 dB on accented notes, 0-2 dB on unaccented" a limit next to the residual SD. Record the rule in STEADY_LINE's comment (LEARNINGS c24).

After the fix (dB addition to the measured frames): front minus body 2.0-3.5 dB on 27 of 31 notes; Violins I minus celli 56-88 median +6.51, lower quartile +3.94, 5 quarters under +3 (c53: +6.36, +4.08, 5); bar 138 Violins I 16.8 17.2 at 549-550 (1.5-2 dB under Violins II and Violas, 3.7 over Oboe 1); bar 26 Violins I 20.8 21.2 at 101-102 (level with Violins II); bar 140 20.8 20.6 at 559-560. Timing is not touched. Check on S that no onset reading moves (the lift starts 0.2 s after the onset).

### 2. Bar 30 (qn 116-117.5): the strings' four ff staccato eighths are 3-5 dB over the theme's eighths and level with the accent fronts (measured)

Where. Violins I, Violins II, Violas, Staccatissimo strokes inside the ff restatement.

Evidence. First 0.2 s of each stroke, c53 → c54: Violins I 16.7 18.7 17.7 21.9 → 22.5 21.2 21.6 22.3; Violas 10.9 9.8 8.7 13.1 → 14.1 12.4 11.1 14.1; Violins II 12.3 15.6 13.9 12.9 → 17.3 15.6 13.9 11.5. The Violins I strokes are now even (spread 5.2 → 1.3 dB) but stand 3.5-5 dB over the line's unaccented eighth fronts (14.3-19.5, median 18.0) and at the level of the accented fronts (20.5-22.1); no accent is printed on them. Cause in the data: the lane returns from the theme's -8.2 dB step to -0.1 dB for exactly these four notes (`vol_db` 115.91 to 117.73), and the round-robin resets changed the takes. Violins II's first stroke is 5.8 dB over its fourth.

Fix. `build/score_config.py` `LEVEL_SHAPES`: Violins I `[(115.90, 0.0), (115.93, -3.5), (117.72, -3.5), (117.75, 0.0)]`; Violas the same with -3.0; Violins II `[(115.90, 0.0), (115.93, -4.5), (116.40, -4.5), (116.45, 0.0)]` and `[(117.45, 0.0), (117.48, 2.0), (117.72, 2.0), (117.75, 0.0)]`. After (dB addition): Violins I 19.0 17.7 18.1 18.8; Violas 11.1 9.4 8.1 11.1; Violins II 12.8 15.6 13.9 13.5.

### 3. The ff restatement (104-128) was not refitted on the full render: weak eighths in all three octaves at 119.5, and single notes 4-8 dB off their neighbours (measured)

Where and evidence (fronts, dB; the note, then its neighbours).
- 119.5 (the eighth between the accents at 118 and 120): Violins I 15.5 (22.1, 20.9); Violins II 10.7 (15.7, 16.8), c53 16.5; Violas 7.8 (14.6, 13.4), c53 15.8. The note is 5-7 dB under both neighbours in every octave.
- Violins I 106.5 D6 14.3 (21.1, 18.0), c53 18.9.
- Violins II 109.5 C5 8.6 (12.8, 15.2); 108 C5 tenuto 11.6, c53 15.9.
- Violas 109 B3 7.9 (12.7, 9.9), c53 11.0.
- Front residual SD on Violins I 104-128 is 2.4 dB (c53 1.8; the other Violins I spans 0.4-1.2), largest residual 7.6 dB.
- The steps for one note differ between the octaves by up to 8 dB (119.5: -5.2 / -8.4 / -3.2; 107.5: -8.2 / -14.4 / -4.3), so the octave balance changes note by note: Violins I minus Violins II fronts range from 3.4 to 9.4 dB over the 27 notes.

Fix. `build/steady_levels54.json`: Violins I "106.500" -8.2 → -5.0, "119.500" -5.2 → -2.0; Violins II "119.500" -8.4 → -4.0, "109.500" -12.6 → -9.0, "108.000" -13.4 → -10.5; Violas "119.500" -3.2 → +1.5, "109.000" -3.2 → -0.5. Then run `levels54.py fit cycles/c54/render build/parts.json --lo 104 --hi 128` on the full render (after finding 1's rows, which change the long notes) and accept its rows where the residual is over 2 dB. Target: front residual SD 1.5 dB or less on each of the three tracks and Violins I minus Violins II within 4-8 dB on every note.

### 4. Oboe 1 in unison with Violins I at bar 25 is within 1.5 dB of the whole section (measured; low priority)

Where. Oboe 1 at 97 (Ab5), 98 (G5), 100 (B5 chord, F5 in the oboe) and 476 (G5): the 4 of 22 onsets c54 left over -2 dB.

Evidence. Oboe 1 minus Violins I per quarter: 97 -0.6, 98 -1.4, 100 -1.1, 476 -0.7. The other 18 onsets read -2.2 to -15.8 (median -5.4). At 97-99 Violins I read 19.1 20.1 19.8 and Oboe 1 18.5 18.7; Flute 1, on the same notes, 14.8-18.7.

Fix. `build/note_trims.json`, Oboe 1: "97.0": -2.0, "98.0": -1.5, "100.0": -2.0, "476.0": -1.5 (0.1 s ramp as on its other trims). After: -2.6 -2.9 -3.1 -2.2. Re-measure 100 after finding 1 (the Violins I body there rises 3 dB, which alone gives about -2.5 on the later quarters of that note).

## Remarks (no action asked)

- Trumpet 2 at printed f reads 8.6 against Trumpet 1 12.4 and Trumpet 3 11.5 (medians of 32-35 quarters; c53 the same within 0.6). At ff and fff it sits with Trumpet 3 (15.7 / 15.2, 19.1 / 19.9). Whether the second trumpet's f chord notes are too soft depends on the voicing; not checked chord by chord.
- Timpani ppp roll at 300-303 reads -5.2 to -7.9, 2-5 dB over the pp rolls at 168-171 and 576-581 (-8.8 to -11.4). The bar-76 roll has had its own role since c01; inferred, not judged against the texture here.
- Violins I at 574-575.5 (last notes of the theme before the poco rit.) are 3.7-10.3 dB over c53 (13.4, 11.4 against 9.7, 1.0). The hairpin there asks a fall; bar 144 on the master is 13.5 against c53's 12.0. A critic of dynamics should check the step into the p at 576.

## Check table for the c55 render

| Row | c54 | Target |
|---|---|---|
| Front minus body on the 31 long theme notes | 4.2-11.5 dB, median 7.7 | 2-4 accented, 0-2 unaccented |
| Violins I minus celli 56-88: median / lower quartile / quarters under +3 | +6.50 / +2.90 / 8 | +6 or more / +3.9 or more / 5 or fewer |
| Violins I at 549, 550 against Violins II and Violas | 9-10 dB under | 0-3 dB under |
| Violins I at 101 against Violins II | -2.9 | within 1 dB |
| 2-5 kHz front minus body, accented Violins I notes, median | +6.8 | under +4, none over +7 |
| Violins I staccato fronts 116-117.5 against the line's eighth median | +3.2 to +4.5 | -1 to +1 |
| Front residual SD, 104-128, Violins I / II / Violas | 2.4 / 2.0 / 1.9 | 1.5 or less |
| Fronts at 119.5 against their neighbours, three octaves | 5-7 dB under | within 3 dB |
| Oboe 1 minus Violins I on the 22 ff onsets | 4 over -2 | none over -2 |
| S per theme line (lens C's table) | as c54 | unchanged within 5 ms |
| All rows of c54's check table | as above | unchanged within 1 dB |

## Do not touch

Keep: the theme on one row with the c54 leads and per-onset rows (no fix here moves a note-on or a note end); the front levels of the eighths and quarters in 56-104 and 536-576 (residual SD 0.4-1.2 dB) and the level of bars 143-144 against bar 15; the round-robin resets before the theme's entries and on the basses; every c54 B row (celli trims at 97, 120, 122, 152, 156, 526 and the shapes at 157-160 and 556.75-558.25, bass clarinet role 464-492, Oboe 1 pitch trims 77 / 79 / 80, basses pizzicato trims and resets, timpani shape 532-536); every c53 B row; timpani roll levels, trumpet dyn trims, tam-tam and cymbal gains, brass widths with their make-up; CC11 and CC1 lanes (every fix here is in the volume lane).

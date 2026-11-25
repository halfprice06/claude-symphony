# Cycle 14, critic A: articulation and phrasing (render c13)

All numbers come from the c13 stems, master and delivered mp3 (`cycles/c13/`), the c12 master and mp3, `build/parts.json` (the rendered build) and `build/mockup-events.tsv`. Levels are RMS in dB re full scale on mono sums. I cannot listen to audio: every verdict "by ear" is inferred from the measurements and is marked so. Score time to seconds is taken from the tempo map in parts.json.

## Manual notes

Third round, pages chosen for this cycle's main question (timing of legato lines and repeatability): 98-99, 105-106 and 143-146 of the May 2021 HO Opus manual, read in full (147-149 are the finger-position tables). `loop/MANUAL-GAPS.md` items 6 and 8 are answered in the last two rows.

| Manual (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Strings legato (p.98-99): which legato type to use "depends on factors such as tempo"; a slur needs "no significant time gap"; "the first note of a phrase has no legato effect". | Every string line on "Leg Slur MAX" / "Leg BC MAX". In the Allegro (quarter = 357 ms, eighth = 179 ms) the measured time from note-on to the audible new pitch is 166-194 ms (median) on these rows. | Partly. Overlaps are right (45 ms on every string join, 35 ms on winds and brass; no chord on a legato row). But 39 measured string notes enter a legato row directly after a note on another row. They get no transition and play the row's slow first-note layer (finding 1). |
| Monophonic True Legato (p.144): velocity sets the transition time (50-60 longer, 110-127 shorter) and does not change loudness. | String legato targets are at velocity 112-124 (the shortest setting); first notes at 73-103. | Yes. No faster setting is left, so the remaining lateness must be solved by lead or by row choice. MANUAL-GAPS item 8 (velocity 60-75 on cantabile lines) should stay closed while finding 1 is open. |
| Brass legato (p.105-106): slur only within an octave and without a gap; the Mod Wheel sets loudness; velocity sets transition speed. | Trumpets 1-2 and Horn 1 in the Più allegro, bars 247-250. | The rule is followed. The level is not even: at CC1 84-90 the trumpets' joined notes are 10-13 dB under their own first note and their Sus-row note (finding 3). |
| Round Robin Reset (p.145): Opus remembers the next sample of each round robin; a second playback starts where the first one stopped ("A B A", then "B A B") unless a reset is sent. | Every track. parts.json holds no reset in the pre-roll (`cc36` is empty on all 31 tracks; `cc16` exists only at the listed points on the crash cymbals, the basses and three string tracks). | No. This is the manual's own description of the c13 result "the same project rendered twice gives two levels". It supports the planned CC16 reset in every track's pre-roll (MANUAL-GAPS item 6; finding 4). |
| Legato and Portamento scripts, CC5 "Time" (p.143-144): these act on the emulations, not on the true-legato samples. | String and wind KS Masters. | Not used, correctly. CC5 cannot shorten a "Leg Slur MAX" transition. |
| Repetition script (p.145): random detune or neighbour sample. | Hammered eighths. | Not used, correctly (it is random; the build uses round-robin rows and gaps). |

## Method

Audible start of a note: measure S of Movement II's c51 critic A (the earlier of pcX and the crossover of the old and new pitch bands, with the version of the crossover that handles A-B-A figures; entries and repeats use pcX alone). I ran it on 29 line segments, 1385 notes, and found 1383. Limits: S reads about +15 ms late on entries with a 30 ms attack; at 35 joins pcX and the crossover fall on opposite sides of the beat and more than 100 ms apart (cellos bars 67-82, cor anglais bars 171-186). Those are long, soft transitions that straddle the beat and are left out of the correction table. The same pitch pair on the same row and velocity repeats its latency: 61 such groups, median range 6 ms, 43 within 25 ms. So the scatter is in the data and the samples, not in the measure.

Per line (S in ms against the beat; "out 25 / out 60" = notes more than 25 / 60 ms from the beat):

| Line | Notes | Min | Max | Median | Out 25 | Out 60 |
|---|---|---|---|---|---|---|
| Violins I, F1 theme, bars 11-26 | 59 | -111 | +99 | -3 | 25 | 10 |
| Violins II, same | 59 | -93 | +144 | -1 | 34 | 8 |
| Violas, same | 79 | -85 | +108 | +21 | 50 | 19 |
| Horn 1, same | 59 | -79 | +103 | +16 | 29 | 9 |
| Violoncellos, F1 in the bass, bars 27-34 | 29 | -60 | +124 | +23 | 18 | 9 |
| Double basses, same | 29 | -102 | +168 | +28 | 23 | 10 |
| Bassoon 1, same | 30 | -48 | +117 | +3 | 13 | 4 |
| Tuba, same | 23 | -25 | +52 | +13 | 6 | 0 |
| Violins I, countersubject, bars 27-34 | 64 | -64 | +99 | +11 | 30 | 3 |
| Trumpet 1, open solo, bars 51-66 | 41 | -79 | +59 | -10 | 10 | 1 |
| Violins I, F2, bars 67-82 | 48 | -102 | +260 | -4 | 26 | 7 |
| Violins II, same | 48 | -83 | +270 | -20 | 32 | 7 |
| Violoncellos, counter-melody, bars 67-82 | 44 | -178 | +199 | -25 | 28 | 12 |
| Violins I, recapitulation, bars 151-170 | 77 | -86 | +122 | 0 | 34 | 12 |
| Violins II, same | 105 | -111 | +58 | +5 | 34 | 7 |
| Violas, same | 67 | -119 | +86 | -7 | 33 | 18 |
| Horn 1, same | 61 | -122 | +189 | +19 | 40 | 21 |
| Trumpet 1, same (staccato) | 15 | -8 | +19 | 0 | 0 | 0 |
| Cor anglais, F2, bars 171-186 | 41 | -138 | +22 | -10 | 10 | 6 |
| Trumpet 1 muted, bars 171-186 | 24 | -56 | +45 | +9 | 9 | 0 |
| Violins I, F2 in C major, bars 187-198 | 31 | -111 | +87 | -4 | 19 | 9 |
| Violins II, same | 31 | -95 | +204 | -30 | 18 | 5 |
| Violins I, coda 1, bars 199-210 | 61 | -237 | +156 | -11 | 26 | 7 |
| Double basses, hammered eighths, bars 199-210 | 89 | -99 | +67 | +15 | 29 | 4 |
| Trumpet 1, coda 2, bars 211-222 | 16 | -71 | +167 | +18 | 6 | 4 |
| Violins I, Q, bars 235-246 | 33 | -58 | +165 | -18 | 26 | 6 |
| Trumpet 1, Più allegro, bars 247-270 | 34 | -50 | +102 | +13 | 15 | 4 |
| Horn 1, same | 45 | -138 | +102 | +20 | 31 | 15 |
| Trombone 1, same | 41 | -157 | +136 | +2 | 22 | 9 |
| All | 1383 | | | | 676 | 226 |

Swallowed or short notes: no note of these lines is missing. No note on a sustained or legato row sounds for less than 40 % of its printed length in its own pitch band, and no note of the F1 theme is more than 12 dB under its line's median. Staccato quarters sound 179 ms of 357 ms (50 %, inside the research range of 50-62 %).

## Findings, ranked

### 1. The fast thematic lines are not together and not in time: legato-row notes start between 110 ms early and 144 ms late (measured)

Where: F1 theme in Violins I, Violins II, Violas and Horn 1 (bars 11-26, qn 40-104; recapitulation bars 151-170, qn 600-680), F1 in the bass (bars 27-34), and the legato lines after them. This is the fault Dan heard in Movement I's theme.

Evidence (measured):
- On the sum of the four theme stems, bars 11-26: 24 of 59 theme notes are more than 25 ms from the beat and 11 more than 60 ms (range -109 to +124 ms). The distance between two neighbouring notes is wrong by more than 40 ms at 24 of 58 joins (an eighth is 179 ms). Bars 151-170: 33 of 77 outside 25 ms, 12 outside 60 ms, 33 of 76 joins wrong by more than 40 ms.
- The four doubled parts disagree with each other. Spread between the earliest and the latest of the four at one printed note: qn 42 121 ms, 50 107, 52 114, 56 102, 58 143, 66 161. At the staccato quarters the spread is 14-36 ms.
- The scatter belongs to the legato rows. Strings, by class (S median, robust SD, notes outside 25 ms): staccato joins and staccatissimo notes -11 to +3 ms, SD 9-13, 6 of 59; "Sus MAX" joins +13, SD 29, 167 of 376; "Leg Slur MAX" after a legato note -25, SD 44, 121 of 177; "Leg BC MAX" -32, SD 36, 74 of 111; "Leg Slur MAX" after a note on another row +49, SD 72, 29 of 35; "Leg Slur MAX" entries +28, SD 80, 32 of 39.
- Class A, a legato-row note after a short "Sus MAX" note. The apex notes of the theme at qn 50, 66, 82 and 97.5 follow a "Sus MAX" eighth. Violins II reads +117, +144, +117, +117 ms; Violins I +45, +86, +82, +97; the cellos at 114 and 130 +124 and +87; the basses +85 and +49. At Violins II qn 66 the F5 eighth stays at full level until 165 ms after the beat and the A flat 5 reaches its body 210 ms after the beat. The note-on is already 139-161 ms early, 18-40 ms after the eighth's own start, so a longer lead is not possible.
- Class B, leads that are too long. "Leg BC MAX" notes have a median lead of 213 ms against a median latency of 173 ms; "Leg Slur MAX" after a legato note 212 ms against 194 ms. The c04 rows in `build/leg_leads.json` were fitted on pcX, which reads late on targets that swell slowly, so they pushed these notes early (the same result as in Movement II).
- Horn 1: "Leg Slur MAX" after a "Marc Shrt" quarter is 98-126 ms early at qn 605, 621, 637, 653, 1061, 1069 (lead 150 ms); a "Sus MAX" note joined from a legato note has no lead and is +29 to +70 ms late (qn 52, 68 and the same notes in the recapitulation).

Fix:
1. Class A (`tools/score_to_parts.py`, new generic rule, default off, for example `LEG_NEEDS_LEG_PREV = {"families": ("string",), "prev_max_s": 0.25}`): a slurred string note that would enter a legato row directly after a note on a non-legato row of at most 0.25 s plays as a "Sus MAX" stroke joined with the slur overlap, with the short-note lead (`SHORT_SUS_LEAD_S`, 0.06 s), and the next note joins from it as `DOWNBOW_STROKE_AT` already does. Until the rule exists, list the onsets in `DOWNBOW_STROKE_AT` in `build/score_config.py`: Violins I 50, 66, 82, 97.5, 134, 610; Violins II 50, 66, 82, 97.5, 310; Violas 76, 610, 642; Violoncellos 114, 130, 310; Double basses 114, 130 (each is a legato-row note after a "Sus MAX" note of 78-112 ms that reads 45-144 ms late). Expected (inferred from the "Sus MAX" join class): about +13 ms, SD 29, instead of +49, SD 72. Check the level of each moved note: "Sus MAX" sits over the legato rows at one CC11 (Violins II already has `ROW_TRIM_DB` -4).
2. Class B and the rest: refit `build/leg_leads.json` on S, not on pcX. New row = old row + 0.9 x S (S in seconds; positive S means more lead), within `LEG_LEAD_CLAMP`. The table at the end of this report gives the change for every unambiguous legato-row note of these lines that is 40 ms or more from the beat (about 220 notes). Horn 1's six notes after "Marc Shrt" are in it (-0.09 to -0.115 s).
3. Before the refit, make renders repeatable (finding 4) and confirm with two range renders of qn 36-108 that S moves by less than 15 ms on these notes.

Targets: on the sum of the four theme stems, bars 11-26, at most 10 of 59 notes outside 25 ms and none outside 60 ms; spread between the four parts under 50 ms at every note; all lines together under 300 notes outside 25 ms (now 676) and under 70 outside 60 ms (now 226). Predicted if every legato-row note is refitted this way (inferred, 0.9 of each change arriving): 290 and 63; the remainder is mostly "Sus MAX" joins.

### 2. The violins' second theme starts with a slow swell: the first note is 200-270 ms late (measured)

Where: Violins I and II, bar 67 (qn 264, "mf, cantabile", dotted half) and bar 187 (qn 744); Violoncellos qn 264; also Violins I qn 824 and 806, Double basses 128, Bassoon 1 118 and 472.

Evidence: the notes are first notes on "Leg Slur MAX" (velocity 73) with a 195-210 ms lead. Violins I stem in 50 ms steps from 0.2 s before the beat at 264: -79, -67, -56, -54, -51 (beat), -51, -48, -47, -43, -43, -39, -39, -36 dB. The body (-38 dB) is reached 0.35-0.40 s after the beat; at the beat the note is 13 dB under it. The master rises 12 dB between the beat and +0.45 s. S: Violins I +260, Violins II +270, cellos +199 ms at 264; +87 and +204 at 744; Violins I 824 +156, 806 +94; basses 128 +124; Bassoon 1 118 +117. The Bassoon 1 solo's second phrase (qn 472, "Leg Slur Exp", lead 35 ms) is at -59 dB on the beat and at its body (-46 dB) 0.25 s later (S +192 ms).

Fix: `build/score_config.py` `DOWNBOW_STROKE_AT`: Violins I and II add 264.0 and 744.0; Violoncellos add 264.0 (a "Sus MAX" stroke, then the slur continues; the tool already does this at Violins II 152, where the body came up from -54 to -32 dB). If the Sus stroke is too hard for "cantabile", the second choice is `build/entry_leads.json` +0.10 s on these onsets (the total is capped at `ENTRY_CAP_S` 0.30 s, which leaves the body about 0.1 s late). `entry_leads.json`: Bassoon 1 "472.0": 0.10, "118.0": 0.08; Double basses "128.0": 0.10; Violins I "824.0": 0.12, "806.0": 0.09. Targets: each of these notes within 6 dB of its body 0.10 s after the beat, S under +60 ms.

### 3. Trumpets 1 and 2 in the Più allegro head, bars 247-250 (qn 984-1000): the slurred notes are 10-13 dB under the first note and the tenuto note (measured)

Evidence: Trumpet 1 per note (mean level, dBFS): E5 at 984 -33.9; D5 -42.4; C5 -44.1; A5 at 989 (tenuto, "Sus Non Vib MAX") -33.0; G5 -38.6; F5 -43.2; E5 -44.4; D5 -44.3; F5 -44.9; A5 -41.7; C6 -41.4; B5 -39.6. Trumpet 2 a third lower: -34.3, -43.6, -44.1, -29.3, -35.6, -44.5, -43.5, -42.3, -43.9, -44.6, -43.0, -44.3. Horn 1 plays the same line an octave lower within 3.7 dB (-32.1 to -36.0). Both trumpets are printed f (CC1 84-90, CC11 88), the horn ff. The per-bar stem levels are the same in c09-c13 (Trumpet 1 bars 247-250: -34.0, -34.6 to -35.0, -42.0 to -42.2, -40.1), so this is not drift. In bars 265-268, at CC1 105-108, the same row is level with the Sus row (-27 to -34 dB). The trumpets' "Leg Slur MAX" joined notes fall off steeply under CC1 about 100: median -43.6 dB at CC1 80-92 against -33.7 dB at CC1 104-112 (envelope removed).

What a listener gets (inferred): in the combined theme head the trumpets sound only on E5 and A5; on the moving notes they are 8-10 dB under Horn 1.

Fix (level only, `build/score_config.py`): `LEVEL_SHAPES["Trumpet 1"]` and `["Trumpet 2"]` add `[(987.16, 0.0), (987.20, 7.0), (988.93, 7.0), (988.97, 0.0)]` and `[(990.61, 0.0), (990.65, 4.0), (991.66, 4.0), (991.70, 7.0), (999.85, 7.0), (999.95, 0.0)]`. The steps sit on the moved note-ons of the notes at 987.5, 991 and 992 (parts.json `qn` 987.20, 990.65, 991.70; 102-120 ms before the beats). Trumpet 2: +2 instead of +4 on 990.65-991.66 (its note at 991 is already at -35.6 dB). The +4 dB step at 990.65 also lifts the last 0.13 s of the tenuto note; simulate it on the stem (`stem_fix.py --out`) and move the step to 991.0 if the tenuto's end swells. Target: every note of 984-1000 within 4 dB of -36 dB on both trumpets, 2-5 dB under Horn 1. Check the brass tilt jump at 989 and the limiter afterwards. Do not raise CC1: the printed f against the horns' ff is kept.

Also in this passage: the staccato eighths of Trombones 1 and 2 at qn 996-997.5 are 60-85 ms pieces of "Sus MAX" and are 8-10 dB under the notes around them (-42 to -45 dB against -35). `LEVEL_SHAPES` +5 dB over 995.95-997.95 on both, and a played length of 0.10 s, would bring them to about -38 dB (inferred).

### 4. Double basses from bar 51: 25 long notes moved the master's bass by 3-9 dB with the new reset (measured), and the levels are not repeatable

Evidence: of 158 bass notes longer than 0.5 s from qn 200, 25 changed the master's 30-130 Hz band by 3 dB or more between c12 and c13 while the full-band level moved less than 1.5 dB. Now too weak (low band against the full band): qn 270 (bar 68) -26.1 dB, 4.6 dB lower than in c12; 348 (bar 88) -25.4, 8.8 lower; 352 (bar 89) 6.6 lower; 410 (bar 103) -23.0, 6.0 lower; 620 (bar 156) -20.4, 5.7 lower; 632 (bar 159, the entry after the caesura) -25.6, 4.8 lower. Now too loud: 344 (bar 87) -4.8 dB, 8.8 higher; 318 (bar 80) 7.0 higher; 652 and 654 (bar 164) 6.3 and 4.6 higher. The downbeat of the recapitulation (qn 600) is 5.8 dB stronger, which suits it. On the stem, long notes at one dynamic differ by up to 14 dB (bars 187-196, all velocity 63 and CC11 46-62: A flat 1 at 744 and 768 -40.5 and -39.6 dB, G1 at 780 -40.1, against -50 to -54 dB for F sharp 1, E1, C sharp 2, D2, E flat 2). The pizzicato notes are fine: 60 notes, -61 to -48 dB, median -55.

Cause (manual p.145, and c13's range test): the round-robin position is not reset at the start of a render, and each reset inside the piece changes every later choice. The per-note and per-pitch trims of the basses were fitted on other round-robin choices.

Fix: (a) `tools/score_to_parts.py`: send the reset controller (`rr_reset_cc`, CC16 127) in the pre-roll of every track, at qn -1.0, after the first keyswitch; (b) `build/score_config.py` `RR_RESET_AT`: for the five string tracks add the section starts 0, 40, 104, 264, 328, 392, 536, 600, 680, 744 (each in the rest or 0.02 qn before the first note-on, as the basses' rows already do), so that a later change of data cannot move another section; (c) accept the test "two range renders in a row are equal" (no long note moving 1 dB) before any refit; (d) then refit the basses' `pitch_trims.json` and `note_trims.json` rows for qn 264-420 and 600-680 and 744-792 on that render, starting with the notes listed above (targets: long notes at one printed dynamic within 5 dB on the stem; master 30-130 Hz within 3 dB of the notes around them).

### 5. Small timing rows: bar 75, the muted trumpet's joins, Flute 2 (measured)

- Bar 75, Violins I: the G at qn 299 starts 80 ms early (lead 213 ms; the actor read 61-101) and sounds 314 ms in a 208 ms slot, the A flat +33 ms, the F at 300 -4 ms. `leg_leads.json` Violins I "299": 0.03 -> -0.04. Violins II: G +11, A flat +30, F -59 ms; "300": add -0.05. The B flat at 296 reads -102 / -79 ms by crossover and +10 / +96 by pcX on the two parts: a long transition, leave it. Violins II's A flat sounds 81 % of its slot in its own band by my measure (the actor's 62 %): both eighths are heard as two notes on both parts. By these numbers the bar is acceptable after the one row (inferred).
- Bar 150: the rest at 599.0-600.0 lasts 0.45 s. The mp3 falls 14 dB in 0.35 s (-24, -27, -29, -32, -33, -35, -38, -38 dB in 50 ms steps) and the G enters at -30 to -21 dB. A hall that still rings at -38 dB when the next bar starts is normal for a 0.45 s rest; nothing is cut and nothing hangs over (inferred). No change.
- Muted Trumpet 1, bars 171-186: the "Mute Sus" release keeps the old pitch within 6 dB for 63-135 ms after its note-off, and the new pitch speaks 21-57 ms after its note-on at the fast joins. Time with two pitches (my measure): 684 94 ms, 686 82, 716 96, 718 84, 694 114, 692 68, 687 66; median of 22 joins 50 ms. Size of the gap: 0.045 s between the old note's end and the new note-on at 684, 686, 716, 718 (expected 40-50 ms of two pitches), 0.02 s at 683 and 715 (now 50). Do not add lead at these six: the new pitch is already at -8 to +6 ms. At 694 remove the 0.06 s overlap and return the lead to 0.035 s (the new pitch speaks 21 ms after its note-on and is 64 ms early now). At 687 overlap 0.03 s instead of 0.06. Audible: hardly, while the cor anglais doubles it 5-7 dB louder (inferred). Low priority.
- Flute 2 at 618 / 650: S +126 / +136 ms with a 190 ms lead; Flute 1 +29 / -51 ms. Flute 2's entry at 600 and 632 is also +98 ms (the stem stays at -44 dB for 0.25 s before it reaches -38). Flute 2 is 11-12 dB under the master there: not audible (inferred). Stop fitting single rows on it; if anything, play 618 and 650 as "Sus MAX" notes (`ART_SPANS`), since two fits on the legato row moved it the wrong way.
- Bassoon 1 solo: per-note highest 50 ms level -43.7 to -49.6 dB; 464 is the loudest of the first phrase and 468 (-49.6) lies inside the printed decrescendo. Both are fine as they are; no trim for +3.0 / -2.8 dB. Timing: the A4 at 464 is 56 ms early by S (lead 150 ms); `leg_leads.json` Bassoon 1 "464.0": -0.04. The second phrase's first note is in finding 2.

### 6. Unprinted tempo changes are small and are not the cause of finding 1 (measured)

The mockup lasts 424.09 s against 423.11 s at the printed tempos. `TEMPO_PUSH` and `BEAT_STRETCH` are empty. Of 520 half-note beats outside the printed ramps, 26 differ from the printed tempo by 2 % or more, all longer:
- `CAESURA` (the last quarter of a beat before an entry): beat at qn 70 +8.4 % (0.06 s), 102 +11.2 % (0.08 s), 390 +11.2 %, 630 +8.4 %, 662 +8.4 %, 814 +7.0 % (0.05 s), 1106 +12.0 % (0.10 s).
- `PHRASE_ARCS` (the last beat of a phrase in the lyrical sections): +3.7 % at qn 214, 246, 278, 310, 694, 726, 758, 934, 950; +6.4 % at 230, 294, 710, 774, 854, 910; +9.4 % at 262, 742, 870, 966; the beat after an arc is +1.5 % (232, 264, 296, 712, 744).
- Inside the printed ritardandos the steps are ramps; single beats differ from the stepped version by -7.3 % (qn 880, the first beat of the allargando) to +3.0 %.
No beat is 15 % long and there is no snap-back larger than 12 %. The four caesuras inside the fast theme (bars 18, 26, 158, 166) are phrase ends before an entry. Keep all of it.

## Answers to the coordinator's other items

- Wetness and stops: the mp3 falls smoothly at every stop, 2-4 dB per 50 ms for 0.4 s, then slower. Bar 2: -3, -4, -6, -9, -11, -14, -17, -19, -21, -22, -24 dB; bar 94: -4, -6, -8, -11, -12, -14, -18, -20, -23. The largest single 50 ms step is 7 dB at bar 166 (-8 to -15, then a 150 ms shelf at -15 to -17); c12 had the same shape with a 6 dB step. No stop is gated (measured; "sounds cut off" inferred: no). Bars 113 and 166 reach -20 dB in 0.29-0.31 s, drier than the recordings' 0.43-0.58 s. Verdict: right, at the dry end. Do not shorten anything further; the 0.3-0.5 dB past the 17 dB limit at bars 6 and 94 needs no action. C #5 (R Winds irSetup 0.43) is therefore not wanted. C #6 (cor anglais Mid mic) has no evidence in this lens either way.
- Solo returns: not my lens; the proposed sends (Bassoon 1 about -10 dB, Trumpet 1 about -7 dB) do not touch any articulation measure here.
- Ride hold over bars 42-50: still wanted. The ride gain rises from +6.6 to +11.7 dB across bars 42-50, under a printed p to pp; the mp3 goes -36.7, -38.0, -35.3, -34.4, -32.4, -34.1, -30.6, -34.0, -35.3 dB, so bar 48 is 6 dB over bar 42 (measured).
- Timpani rolls at 223 and 278: after the first stroke the roll is the 19th, 16th and 25th loudest stem in bars 223-225 and the 14th / 10th in the two halves of bar 278; in bars 232, 244, 262, 274 it ranks 14-20. Rule met.
- Horn 1 bars 139-140, the crash strokes, Violins II 152 (S +57 ms, body -32.5 dB; the next note at 154 is +69 ms late and is in the table), the low end in 255-256: no fault found. Closed.
- Drift: none of the single moved notes on the 27 tracks without a new reset is audible as a fault by these measures (inferred). The basses' notes are named in finding 4.
- Other movements' findings: per-onset rows on winds and brass should not be extended here (wind legato joins are already -2 ms, SD 17, 10 of 50 outside 25 ms); Horn 1 is the exception, with six notes after "Marc Shrt" 98-126 ms early. A positive pitch trim on a legato target must start with the short mirror ramp: keep that rule when finding 3's shapes are added (their first points sit on the moved note-ons for this reason). Woodwind seat and Stereo Double: not this lens.
- Standing checks on unchanged data: no chord on a legato row; keyswitch leads as in c13 (median 11-24 ms); overlaps 45 / 35 ms; the hammered eighths of the basses in bars 199-210 start at +15 ms (median), 4 of 89 outside 60 ms. Brass accents, tremolo rows, re-bows, pizzicato timing and the harp were measured on c12 by the c13 report and their data and stem bar levels are unchanged (bars 247-262 within 0.4 dB).
- Horn 1's stopped note at 668 ("Stop Sus") is 15 dB under the open f note before it (-52 against -37 dB) while the hairpin to p only starts there. A `LEVEL_SHAPES` +6 dB on 668-672, falling to 0 at 676, would let the stopped colour be heard (inferred).

## Table for finding 1: change of the `leg_leads.json` row in ms (0.9 x S; positive = more lead), legato-row notes 40 ms or more from the beat

Violins I: 40 +40, 51 +55, 56 -55, 58 -70, 72 +55, 74 -40, 83 +90, 88 -100, 99 +80, 100 -50, 135.244 -50, 135.496 -60, 135.748 -40, 269 -35, 272 -50, 283 -50, 283.5 +55, 285 +45, 288 -45, 291 +55, 299 -70, 304 -55, 310 +65, 315 -70, 317 -50, 608 -50, 611 +95, 616 -45, 628 -40, 656 -60, 659 +80, 660 -75, 676 -45, 748 -70, 750 -60, 751 +55, 752 -90, 755 +55, 756 -60, 760 -50, 765 -45, 783 +40, 784 -50, 792.5 -100, 807.5 -40, 808 +95, 810 +55, 941 -50, 947.5 +45, 950 -35, 955.5 -50, 957 -45, 960 -40, 961.5 -45, 964 -50, 966 -50, 982 +150.
Violins II: 40 +45, 52 -50, 55 -70, 58 -85, 72 +50, 74 -40, 80 -40, 83 +55, 88 -65, 90 -45, 96 -35, 272 -60, 275 -40, 276 -40, 280 -45, 285 -60, 286 -40, 288 -75, 290 -45, 300 -55, 312 -60, 315 -45, 317 -40, 322 -50, 600 +40, 602 -60, 612 -60, 616 -65, 618 -95, 628 -85, 670 -100, 760 -70, 768 -50, 779 -85.
Violas: 42 -75, 52 -75, 58 -40, 68 -40, 92 +35, 602 -85, 612 -70, 615 -65, 616 -75, 618 -65, 634 -85, 648 -65, 650 -105, 656 +65, 659 -65, 660 -75, 672 -95, 676 -85.
Horn 1: 51 +55, 54 +50, 58 +45, 64 -70, 65 +40, 74 -70, 75.5 +70, 80 +75, 81 -40, 83 +90, 87 +60, 91.5 +45, 97 +95, 97.5 -45, 99 +90, 602 +65, 605 -90, 611 +65, 614 -60, 621 -105, 624 -60, 624.5 +40, 626 +80, 637 -90, 641.5 +55, 643 +65, 647 +60, 651.5 +65, 653 -110, 656 -65, 992 +50, 993.5 -125, 994 +80, 995 +60, 995.5 +55, 996 +90, 998 +70, 1008 +50, 1009.5 -95, 1010 +75, 1012 +55, 1014 +65, 1061 -110, 1067.5 +40, 1069 -115.
Violoncellos: 106 -50, 115 +80, 131 +55, 132 -55, 270 -45, 272 -50, 277 -45, 278 -60, 290 -35, 302 -45, 317 -70, 318 -40, 322 -50.
Double basses: 112 -50, 115 +90, 118 +65, 119 -90, 120 +150, 122 -90.
Bassoon 1: 106 +40, 123.5 +80, 125 -45.
Trumpet 1: 847 +40, 851 +75, 852 +85, 984 -45, 995 +45, 995.5 +90, 996 +70, 1059.5 +40, 1060 +75, 1062 +50, 1069.5 +70.
Trombone 1: 984.5 -105, 992.5 +120, 993 -40, 1000.5 -40, 1003.5 +70, 1005.5 +45, 1009 +65.
The onsets named in fix 1 of finding 1 (the "Sus MAX" strokes) and in finding 2 (the entries) are left out of this table. A row that would pass 0.45 of the previous note's slot will be capped by the tool; report those instead of forcing them.

Do not touch: the staccato and "Marc Shrt" rows and leads (S within 25 ms on 101 of 124 staccato-row notes of strings and brass); the 45 / 35 ms legato overlaps; the tempo map with its caesuras and arcs; the timpani roll shapes; the crash strokes with their CC16 resets; the Violins II 152 stroke; the Bassoon 1 solo's levels and row; the pizzicato levels and timing; `rise_delay_s` 0.6 and the three release fades (no stop is gated); "Mute Sus" as the muted trumpet's row and its per-bar roles; the 592 sfp; and the closed items (the 315 Hz hump in J, "Sus Accent MAX", "Leg Slur Exp" on cor anglais and Oboe 1, tuba / contrabassoon -3 dB at 984-1056, `KS_LEAD_S`, END_LEG_KS, precautionary rebuilds).

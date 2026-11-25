# Scherzo cycle 12, critic A: articulation and phrasing

Render under review: `cycles/c11/` (stems in `render/`, master, `build/parts.json`, `build/score_config.py`, `tools/score_to_parts.py`). All levels are in dB full scale, measured on the c11 stems (`22_Timpani.wav`, `23_Harp.wav`, the string stems) and on the master. "Lane removed" means the stem level minus the track's `vol_db` value at that time; `vol_db` is a step lane and my subtraction can be wrong by up to 0.5 dB near a step. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

## Manual notes (cycle 12 slot A, group A6: PDF pages 68-71, Hollywood Harp)

| Manual statement (PDF page) | Where it applies in this movement | Does the render follow it |
|---|---|---|
| Hollywood Harp has vintage alternatives for the close and mid microphones in place of surround positions; Maestro patches choose the articulation by velocity or CC1 (p.68) | Harp track, all bars | Not checked (microphones belong to the mix lenses). The render uses a Maestro patch, `01 Maestro Patches/Harp Sus RR.oib`. |
| "Sustain RR": notes alternate between Pluck Long (RRx1) and Thumb Pick (RRx2) between velocities 1 and 123, 5 dynamic levels each; Nail Pick at velocities 124-127; CC11 and velocity control loudness (p.69) | Every harp note: 346 notes, velocities 40-56 | Partly. No note reaches the Nail Pick range, which is right (the score has no nail marking). The alternation of two articulations is audible as uneven levels in the tune of bars 73-80 (finding 2) and as a colour alternation in the off-beat chords (finding 5). |
| Single patch "Pluck": the standard way of playing, rounded notes, 5 dynamic levels, one articulation (p.70) | The slurred "p espress." tune, bars 73-80 (qn 216-240) | Not used. Candidate patch for the tune (finding 2, option 3). |
| "Harmonics": 2 dynamic levels by velocity; "blends well with pizzicato strings" (p.70) | Harmonics in bars 149, 151, 375 (track "Harp harmonics", 9 notes, all velocity 58) | Followed. Stem -43.3 dB; the master carries them at -40.7..-42.2 dB in their band, so they are audible. One velocity for all nine is consistent with a 2-level patch. |
| "Repetition Rep": repeated notes without the machine-gun effect, earlier notes ring to full duration, 2 levels; "Thumb Pick" has a "more guitar-like sound" (p.71) | Repeated off-beat chords, bars 153-167, 185-192 ("non arpegg."), 225-237, 341-348 | Not used. The chords play on Sus RR and alternate between the two articulations (finding 5). |
| Pres de la Table, Gliss Technique, Double Hit, Bisbigliando, FX and the Gliss key map (p.70-71) | Nowhere: the harp part has no près de la table, glissando or bisbigliando marking (searched `v600/sections/*.ily`) | Nothing to follow. |

## Findings, ranked

### 1. Timpani motive x: the downbeat stroke is the weakest of the four, by 8-13 dB in the pp statements (measured)

Where: Timpani, every complete statement of motive x (quarter, two eighths, quarter on B). Worst at bars 241, 247, 249 (qn 720, 738, 744), 363, 367, 371 (qn 1086, 1098, 1110) and bars 98-99 (qn 291, 294).

What is wrong: the motive is a downbeat figure, and in the render its first stroke is the softest. In all 30 complete statements the first stroke is under the loudest later stroke (30 of 30). The median is -3.6 dB; in the 16 soft statements it is about -6.3 dB (range -3.4..-13.2), in the 14 f statements -2.0 dB (range -0.9..-5.3).

Stem peak per stroke (20 ms windows):

| Bar (qn) | Velocities | Stroke 1 | Stroke 2 | Stroke 3 | Stroke 4 |
|---|---|---|---|---|---|
| 241 (720), pp | 56 | -57.4 | -48.4 | -53.4 | -48.6 |
| 249 (744) | 56-58 | -57.7 | -47.1 | -53.4 | -44.4 |
| 363 (1086), pp | 56 | -57.4 | -47.8 | -56.5 | -50.1 |
| 371 (1110), ppp "near the rim" | 52 | -64.2 | -53.9 | -58.7 | -58.3 |
| 98 (291), p cresc. | 64-70 | -50.2 | -42.4 | -43.3 | -42.7 |
| 99 (294) | 73-78 | -46.7 | -34.7 | -36.8 | -34.3 |
| 104 (309), f | 98, 90, 86, 91 | -28.9 | -26.5 | -27.2 | -25.3 |
| 304 (909), f | 96, 91, 88, 90 | -30.6 | -26.4 | -27.2 | -25.4 |

Cause (measured): `TIMP_RH_ALT = {"max_gap_s": 0.8, "add": 24}` (`build/score_config.py` line 157; code in `tools/score_to_parts.py` lines 6120-6134) starts each run on the left-hand region and sends every second stroke to the right-hand region 24 semitones higher. In "Timpani Flt Lng" the two regions are not level-matched at soft velocities. Lane removed, B2 right hand (MIDI 71) minus B2 left hand (MIDI 47) at the same velocity, over the whole movement:

| Velocity | 48-55 | 56-63 | 64-71 | 72-79 | 80-87 | 88-95 | 96-103 |
|---|---|---|---|---|---|---|---|
| Right minus left (dB) | +7.6 | +8.0 | +3.4 | +7.6 | +3.7 | +1.8 | +3.6 |
| Left-hand level | -61.5 | -56.2 | -49.0 | -38.2 | -31.4 | -32.8 | -33.4 |
| Right-hand level | -53.9 | -48.2 | -45.6 | -30.5 | | | |

(n is 15 left / 11 right strokes at 56-63 and 15 / 24 at 88-95; the outer bands have 1-2 strokes each.) The volume lane is flat across the soft statements (0.0..+1.4 dB), so the difference is the samples. The left-hand B2 level also stops rising above velocity 80 (-31.4, -32.8, -33.4), so the `TIMP_METRIC_VEL` reductions on the weak strokes do not make them softer than the downbeat.

Exposure (measured): in bars 367 and 371 the master's 100-320 Hz level after each stroke equals the timpani stem's within 0.7 dB (-63.9/-64.2, -52.1/-52.8, -60.2/-59.6, -52.6/-52.7 at qn 1098-1100). The timpani are alone in that band there, and the downbeat sits 11 dB under the second stroke.

At f the later strokes also carry the ring of the earlier ones (strokes are 114 ms apart), so part of the 2 dB median there is accumulation and not the hand (inferred). I rank the soft statements as the fault and give the f figure as a secondary target.

Fix (velocity, because the lane is already flat):

1. Preferred: in the `TIMP_RH_ALT` block of `tools/score_to_parts.py` add an optional key that raises the velocity of left-hand strokes inside an alternating run, by velocity band, for example `"lh_vel_add": [(55, 10), (63, 8), (71, 4), (79, 6)]` (upper bound of the band, steps added; nothing above 79). The slopes behind these values: the left-hand level rises about 0.9 dB per velocity step between the 56-63 and 64-71 bands and 1.35 dB per step into 72-79.
2. Without a tool change: `TIMP_VEL` (tool line 129, applied at lines 3222-3223 with `max`; keys are onsets rounded to 2 places, as in Movement II's `TIMP_VEL = {278.5: 60, 279.0: 60}`; not yet set in the scherzo config). Left-hand B2 strokes of the soft statements: first strokes at 720, 738, 744, 747, 750, 1086, 1098 from 56 to 64-65 (target about -48 dB, the right-hand level at 56); third strokes at 721.5, 739.5, 745.5, 748.5, 751.5, 1087.5, 1099.5 from 56 to 62-64; bar 371: 1110.0 from 52 to 60-62 and 1111.5 to 57; the same treatment for bars 97-100 (288-298.5), bars 9 and 11 (24, 25.5, 30, 31.5) and bars 135 and 323 (402, 966), scaled by the table above.
3. Alternative: stop the alternation below velocity 80 (`"min_vel": 80`). This returns the same-hand take steps of ±1.4..3.2 dB that Movement I c37 measured, which is smaller than the 8 dB now present.
4. Optional for the f statements: a lane term of about -2 dB on right-hand strokes at velocities 80-103, or +2 dB on the downbeat bump. Test it in the same render; do not apply it unverified.

Target: every stroke of a statement within 2 dB of the others, and the downbeat not under them. Verify with a one-track timpani render (about 5 minutes, scherzo LEARNINGS c08). E2 left hand has a layer step between velocity 52 (-58.3) and 56 (-50.1), which affects the fourth stroke of bars 363, 367 and 371: check it after the change.

### 2. Harp tune bars 73-80: note levels differ by up to 13 dB within one phrase, and the loudest note is an unaccented beat 3 (measured; manual p.69)

Where: Harp, qn 216-240, "p espress.", slurred; the harp is the loudest stem in these bars.

What is wrong: Sus RR alternates Pluck Long and Thumb Pick from note to note (manual p.69). At the capped velocity 56 the two groups sit on different dynamic layers. `VEL_CAP_SPANS["Harp"]` (216-240: 56) is applied after `HARP_PITCH_VEL` and `VEL_SET` (tool lines 3244-3249), so the per-pitch corrections are flattened to 56 and nothing evens the notes.

Evidence: stem level in 600-5000 Hz over the first 100 ms of each note, lane removed, as deviation from the tune's median (-44.4 dB), with a suggested velocity (56 minus deviation / 0.6, kept within 40-76):

| qn | Pitch | Dev. dB | Vel. | qn | Pitch | Dev. dB | Vel. |
|---|---|---|---|---|---|---|---|
| 216 | A5 | -5.4 | 65 | 228 | F5 | +1.8 | 53 |
| 217 | F5 | +1.2 | 54 | 229 | C5 | -0.3 | 57 |
| 218 | A5 | +2.5 | 52 | 230 | F5 | +8.4 | 42 |
| 219 | C6 (crest) | -2.9 | 61 | 231 | A5 | +2.5 | 52 |
| 221 | B-flat5 | -3.9 | 62 | 233 | G5 | -0.3 | 56 |
| 221.5 | A5 | -2.9 | 61 | 233.5 | F5 | +1.9 | 53 |
| 222 | G5 | -0.9 | 57 | 234 | E5 | +1.3 | 54 |
| 223 | D5 | -4.0 | 63 | 235 | G5 | +0.9 | 54 |
| 224 | G5 | +1.1 | 54 | 236 | B-flat5 (crest) | -4.5 | 63 |
| 225 | B-flat5 | +0.3 | 56 | 237 | A5 | -2.1 | 59 |
| 227 | A5 | +2.3 | 52 | | | | |
| 227.5 | G5 | -1.0 | 58 | | | | |

- The F5 at qn 230 (bar 77 beat 3, no accent) is the loudest note of the tune: stem -38.0 dB, 10.5 dB above the note before it. On the master it measures -37.4 dB in 600-5000 Hz, 9.8 dB above the preceding onset, where the other onsets of the tune lie between -40.7 and -49.3.
- Both printed crests fall on weak samples: the C6 at 219 is 4.1 dB under the A5 before it, and the B-flat5 at 236 is 4.9 dB under the G5 before it. HISTORY records the crests as 1-2 dB short of target after the c10 hairpins; this is the cause.
- The first A5 at 216 is 10.5 dB under its repeat at 218. Same-pitch pairs on opposite round-robin groups differ by 6.4 dB (A5), about 8.6 dB (B-flat5), 8 dB (F5) and 4-5 dB (G5).
- The pattern is identical in the c08 and c11 stems to 0.1 dB on qn 222-227, so it is repeatable and a per-onset table will hold.

Fix, in order of preference:

1. Per-onset `VEL_SET["Harp"]` for the 22 onsets with the velocities in the table (the method of Movement I c28, `mockup-kit/pipeline/example-config-mvt1-v621/score_config.py`). This needs `VEL_SET` to be applied after `VEL_CAP_SPANS` in `tools/score_to_parts.py` lines 3244-3249, or the listed onsets exempted from the cap. The median level of the passage does not change, so the cap's level decision stays. Expect 0.6-1.0 dB per velocity step where a note crosses a layer; one verify render and one refit.
2. If the tool order must stay: per-onset step shapes in `LEVEL_SHAPES["Harp"]` of the form `[(a - 0.03, 0.0), (a - 0.01, v), (b - 0.03, v), (b - 0.01, 0.0)]` with v = minus the deviation, a the onset and b the next onset. The ring of the previous note is scaled too, so option 1 is cleaner.
3. Patch alternative: put qn 216-240 on `Harp Pluck Long.oib` (manual p.70 "Pluck": 5 levels, one articulation, no alternation). Velocities and `HARP_PITCH_VEL` need refitting for that patch (inferred; not rendered).

The table is valid while the number of harp notes before qn 216 is unchanged, because the alternation depends on the note count. Whether CC36 resets the harp patch's round robin is not checked.

### 3. Timpani summit roll, bar 336: the roll fades 12.6 dB before the accented strokes, and the accented stroke at bar 337 beat 1 is 5 dB under the next two (measured)

Where: Timpani, qn 1005-1008 (roll, ff; `coda.ily` comment c028 names this roll and the Violins I B6 as the movement's peak) and qn 1008 (bar 337 beat 1, accent).

Evidence:

- The roll is one "Timpani Flt Rls" note (qn 1005.096, velocity 91, CC1 102-104). Stem per 0.5 qn: -26.5, -32.3, -32.2, -32.3, -35.1, -39.1. The last quarter of the bar is 9-15 dB under the roll's start while the master holds -14..-18 dB; in 110-138 Hz the stem is 25-29 dB under the master there.
- Two causes. The sample itself falls about 8 dB across the bar (stem minus lane -34.8 to -43.2). The lane falls from +8.4 at 1007.0 to +3.4 at 1007.85, then to -5.1 at 1007.9 and -9.0 at 1007.99.
- Strokes: 1008 (velocity 121, accent) peak -29.0; 1010 (121) -25.5; 1012 (121, accent) -24.3; chord at 1014 -22.2. Lane removed, 1008 and 1012 agree (-26.3 against -25.8), so the deficit at 1008 is the lane: it stands at -3.0 at that stroke's bump point against +2.0 at 1010 and 1012. The roll's settle is held through the next onset, which is the case kit LEARNINGS line 208 describes.
- The c08 and c11 stems are identical here.

Fix: in `LEVEL_SHAPES["Timpani"]` replace the c07 summit row `[(1005.7, 0.0), (1006.0, 5.0), (1007.0, 8.0), (1007.85, 8.0), (1007.9, 0.0)]` with `[(1005.7, 0.0), (1006.0, 5.0), (1007.0, 10.0), (1007.5, 12.0), (1007.85, 15.0), (1007.9, 0.0)]`, and add a row for the stroke: `[(1007.97, 0.0), (1008.0, 5.0), (1008.45, 5.0), (1008.5, 0.0)]`. The roll row has to rise because the base lane falls about 5 dB under the shape between 1007.0 and 1007.85 and the sample falls 8 dB; the resulting lane ends near +10 dB, under the +12 dB the f rolls already use. An untested alternative for the roll (inferred): raise CC1 from 103 to about 120 over qn 1006.5-1007.85, since the Rls row crossfades its layers on CC1. Targets: roll stem over qn 1007-1008 no lower than -33 dB (its level over 1005.5-1007, still 6 dB under its first stroke, so brief rule 5 holds: the roll settles and does not grow), and the 1008 stroke peaking at -24..-25 dB like 1012. The 1012 stroke already plays at that level, so the limiter load should not rise (inferred).

Same mechanism, smaller, for the actor to check in the same render: the first stroke after the roll at bar 104 (qn 309, -28.9 against -26.5, -27.2, -25.3) and bar 304 (qn 909, -30.6 against -26.4, -27.2, -25.4; lane removed it is 2.8 dB under other left-hand strokes at velocity 96, cause not determined); the E2 stroke after the f roll at bars 131 and 287 (qn 390, 858; velocity 97) peaks -34.3 with the lane at +1.0, against -26.7 for the E2 stroke at qn 312 with the lane at +6.0.

Remark on the f rolls of bars 129-130 and 285-286 (qn 384-390, 852-858), no ranked fix because rule 5 asks for a settle: stem per 0.5 qn -32.2, -37.2, -40.0, -43.1, then -43..-45 to the end. The lane accounts for 9.7 dB of the 13 dB fall (a +4.8 start bump, then the settle), the sample for about 3 dB. From the second beat the stem is 15-22 dB under the master in 110-138 Hz. The kit's settle figure is 5 dB over 3 qn; this is about twice that. If the actor wants the roll to stay audible, halve the settle for these two rolls in `TIMP_ROLL_TRIM_DB`.

### 4. The early legato joins are the joins without a fitted lead; the arrival at bar 201 is spread over more than 100 ms (measured; size depends on the method)

Where: Violins II, Violas, Violoncellos; worst at bars 197-201 (qn 588-600, strings together, crescendo to the trio's forte).

New fact for the actor's open item "joins under -40 ms rose": joins more than 60 ms early are almost all joins that have no entry in `build/leg_leads.json` and still use the track default lead (Violins II 240 ms, Violas 225 ms, Violoncellos 220 ms). Fitted joins have leads of 139-156 ms and pcx medians of -2..+11 ms. The exposition and reprise repeat to 1 ms (celli 331/931 -124, 344/944 -91/-92, 356/956 -85, 317/917 -72, 323/923 -78), so the offsets are deterministic and can be fitted.

Unfitted early joins (score qn: pcx in ms):

- Violins II: 133.5 -96, 373.5 -111, 590 -84, 593 -120, 595.5 -126, 598 -142, 600 -136, 744 -76, 841.5 -117, 842 -97, 846 -98, 1051.5 -118, 1056 -72, 1061 -89, 1063 -117, 1074 -79.
- Violas: 370 -61, 378 -180 (lead 325), 588 -65, 590 -93, 598 -120, 600 -91, 838 -61, 846 -188 (lead 325), 1044 -60.
- Violoncellos: 133.5 -77, 138 -62, 140 -74, 145.5 -76, 150 -77, 152 -73, 193.5 -81, 317 -72, 323 -78, 331 -124, 344 -91, 356 -85, 846 -73, 917 -72, 923 -78, 931 -124, 944 -92, 956 -85, 1056 -65, 1065 -62.
- Violins I: 591 -103 only.

Bar 201 beat 1 (qn 600): Violins I +98 ms, Violins II -136, Violas -91, Violoncellos +58 by pcx. A cruder level-crossover measure gives +20, -100, -90, -10. The two methods disagree on size and agree on direction: the inner strings arrive about 100 ms before the outer strings. The research default for a tutti entry spread is 36-55 ms. At qn 598 Violins II are -142 (-50 by crossover) and Violas -120 (-50); Violins I are late at 597 (+109) and 600 (+98).

Fix: add entries to `build/leg_leads.json` by the file's c07 rule (new total = old + 0.7 x (pcx - 0.02 s), clipped to ±0.15). Start with bars 197-201: Violins II 598: -0.113, 600: -0.109, 595.5: -0.102, 593: -0.098; Violas 598: -0.098, 600: -0.078; Violins I 600: +0.055, 597: +0.062 (added to any existing value); Violoncellos 331 and 931: -0.101. Then the rest of the lists above. Re-measure with `tools/pcx.py`; target ±50 ms (Dan's check S2).

### 5. Harp off-beat chords alternate in colour between the two round-robin groups (measured on the stem; audibility inferred; manual p.69 and p.71)

Where: Harp, Trio bars 153-167 (qn 456-501) and coda bars 341-348 (qn 1020-1044), velocities 40-42.

Evidence: for successive identical chords, the 2-6 kHz level minus the 100-1000 Hz level alternates by 4-6 dB, and the order flips from bar to bar (bar 153: -27.5 / -33.6; 154: -33.4 / -29.0; 155: -29.7 / -34.9; 156: -33.6 / -29.5). Chord levels differ by 1-2.5 dB. This is the Pluck Long / Thumb Pick alternation of Sus RR (p.69); the manual calls Thumb Pick "more guitar-like" (p.71).

Fix to test in a one-track harp render before adopting: these spans on `Harp Pluck Long.oib` (one articulation), with the 42 cap refitted for level. "Repetition Rep" (p.71) is the manual's patch for repeated notes but has only 2 dynamic levels; try it second. If neither is clearly better by ear, keep the patch: the passage is soft and accompanied, and I rank this last.

Two smaller harp observations, no fix asked: the rolled chord at bar 237 (qn 708) starts with two notes together (MIDI 40 and 56 at 708.0, then 59 at +0.152 qn and 64 at +0.303 qn); the roll at bar 361 has velocities 52, 52, 44, 43, 52, 56, which is not a rising or even series.

## Cycle 12 note checks and checks with no finding

- Horn splice (note a): clean. No click at any of the 16 edges (the largest sample difference at each edge is within the 99.9th percentile of the surrounding 0.6 s). Outside the spans the 20 ms levels match the first render within 0-1 dB. Inside, the holes are gone: Horn 4 at qn 252 (minimum -62.4 to -45.5 dB), Horn 1 at 156 (-43.3 to -37.1), 165 (-58.8 to -45.8) and 166 (-66.6 to -44.4), Horn 2 at 159 and 627. Horn 1 at 165 still dips 8.7 dB before the note.
- Stale legato state (note b): no sign of it. Joins from bar 112 on: Violins I pcx median +16 ms and level step +0.3 dB (n 66), Violas -1 ms and +0.5 dB (n 28), Violoncellos +5 ms and +0.1 dB (n 97), control Violins II +2 ms and -0.7 dB (n 63). There is no population 45-85 ms early and 3-5 dB loud. Bassoon 2 matches c10 within 0.74 dB at 0 ms lag.
- Keyswitch timing: no keyswitch on any track lies closer than 0.008 qn before its note-on.
- Con sordino: Violins II CC15 is 127 from qn 445.29 to 552.52 and covers every muted note (501.31-552.02, bars 168-184). The score has con sord. at bar 168, via sord. at 185, senza sord. at 193: followed.
- Harp étouffez: bars 87, 192 and 240 are silent within 1 qn of the last chord.
- Staccato theme head (Dan's check S1), master dips between the eighths: bar 13: 4.3/3.0 and 3.4/2.9 dB; 29: 3.1/2.0 and 2.0/1.3; 61: 3.8/3.4 and 2.9/1.9; 105: 3.1/1.8 and 3.2/1.8; 253: 3.6/2.2 and 4.3/5.9; 305: 3.6/0.0 and 1.9/1.5; 319: 2.5/3.7 and 2.2/1.2; coda 985: 3.0/2.3 and 2.1/1.3; 988: 2.6/1.6 and 1.6/2.7. Of the 36 dips, 14 reach the 3 dB lower bound of the target; the other 22 are 0.0-2.9 dB. In the coda at quarter 288 the Violins I stem dips only 0.6/-0.5 dB at 988. The rows and lengths are on the do-not-touch list, so I report the numbers without a fix.
- Not measured this cycle: the fronts of accents in 2-5 kHz and the sfp at qn 900 (on the actor's list), pizz./arco level changes, re-bows and loop pulsing in long notes (including the timpani rolls of bars 205-208 and 237-240), the solo violin of bars 349-356, breath marks.

Do not touch: the horn splice spans; the Violins II CC15 lane; the harp étouffez note ends (qn 258, 576, 717) and the level of the harp caps (56 / 50 / 42); the harmonics on their own track at velocity 58; the fitted `leg_leads.json` entries whose joins measure within ±50 ms (median -2..+11 ms per track); `TIMP_DELAY_S` 0.02 and `TIMP_DAMP_AT` 1014.5; the flat timpani lane under the soft statements of motive x (fix finding 1 with velocity only); the bar 332 timpani row; staccato lengths 0.25 / 0.50 qn and the theme-head rows; keyswitch timing; and everything on HISTORY's list.

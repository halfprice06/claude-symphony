# Cycle 51, critic B: balance and levels (render under review: c50)

## Method

- Stems 01-32 of `cycles/c50/render` (dry tracks after the volume envelope), the four return stems and the master. K-weighted and A-weighted power per 10 ms frame (4096-point FFT, 48 kHz), the same scripts as my c50 report, so the c49 and c50 numbers compare directly. A note's body is the mean over 20-80 % of the played note. A solo's margin is its level over the sum of the other 31 dry stems. For the passages below I also read the stems at 30 ms steps (unweighted level and the level of the note's fundamental).
- Data: `cycles/c50/rendered_build` (`parts.json`, `roles.json`, `note_trims.json`, `early_fills.json`, `score_config.py`, `score_to_parts.py`). `build/parts.json` is byte-identical to `rendered_build/parts.json` today. Printed marks from `build/mockup-events.tsv`.
- Timing and note starts are critic A's this cycle. Findings 1 and 4 are level holes inside notes of the entry the lead asked me to check; they sit next to A's area, so A's report may cover the same joins from the timing side.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 51 (the schedule ends at c47), so no new page range was read. The table lists what this report relies on.

| Source | Where it applies | Does the render follow it |
|---|---|---|
| May 2021 HO manual, legato sections of each family (text pages 79 and 86 by page-break count): transitions were recorded at several dynamics, and note velocity changes the timing of the join; CC11 and CC1 set loudness | Flute 1 107-113 (Leg Slur MAX, velocity 53 on the pickup, 90-95 on the targets) | The levels do come from CC11 and the envelope. The join itself leaves a level hole about 0.35 s after each flute target (findings 1 and 4), which no controller in the data explains |
| `EW-TEMPLATE-PLAN.md` section 6 and FINDINGS section 8: controller lanes stay flat across legato note changes, no per-note bumps | Flute 1 bar 37: the envelope moves between +2.0 and +13.2 dB from note to note | No. The per-note trims and fills are compensation for sample sags; they are needed while the sags are there, but they are 5-13 dB steps on one line (finding 4) |
| `MANUAL-GAPS.md` 5 (Leg Slur Exp / Sus Exp rows for dolce wind solos), never tried | Flute 1 "dolce cantabile" at 107 | Not tried. If the fills of finding 1 do not hold in a range render, this row is the next thing to test on Flute 1 107-123 |
| `MANUAL-GAPS.md` 8 (half-section patches for div. and 4 soli) | divisi tracks | Levels unchanged from c49 (within 0.2 dB); no level reason to change |

## Findings

### 1. Flute 1, bar 37 beat 1 (qn 108): the slurred arrival is 4-6 dB weaker than in c49 for half a second and has a 10.8 dB hole at +0.39 s

Where: Flute 1, F5 at qn 108 (bar 37), now a legato target after the new C5 pickup at 107.

What is wrong: in c49 the F5 was a fresh attack. In c50 it is reached by a slur, and the first 0.55 s of the theme's first long note is under the accompaniment. Measured (stem, unweighted, 30 ms steps after the beat; c49 in brackets): +30 ms -42.2 (-38.1), +150 -41.0 (-35.7), +270 -39.2 (-38.6), +330 -42.3, +360 -47.2, +390 -50.0 (-38.6), +450 -48.5, +480 -47.4, +510 -44.1, +540 -41.5 (-37.1), +720 -37.0 (-38.2). The F5 fundamental follows the same curve (-41.0 at +240 ms, -53.9 at +390 ms, -43.6 at +540 ms), so the hole is in the note, not in a release tail.

Balance at the downbeat (K / A margin of Flute 1 over all other stems): 108.0-108.25 -4.1 / +0.7 (c49 +0.4 / +5.0); 108.25-108.5 -4.8 / -1.7 (c49 -0.2 / +2.7); from 108.5 on c50 equals c49 within 1 dB (+3.7 / +6.5). The pickup itself is fine: C5 body -41.1 K, margin +3.2 / +5.2 over the bass clarinet's C3. But the arrival's first half beat (-41.0, then -43.1 K) is at or under the pickup (-41.3 K), so the slur leads into a weaker note and the theme is first heard clearly half a beat late.

Cause (inferred): the hole's time matches the dips the actor's `dips_c50.txt` lists at +346, +316 and +347 ms on the flute joins at 112, 117.667 and 119, and the notes at 111 and 112 show the same dip in c49 and c50, so it belongs to the flute's legato join and repeats between renders. Nothing in the data moves at that time: CC11 rises 55 to 62, CC1 80 to 94, the envelope is +2.0 to +2.4 dB. The join 107 to 108 is not in `dips_c50.txt` (its Flute 1 list starts at 110), so no fill was fitted.

Fix (`build/score_config.py`, one row; times in qn, 1 qn = 1.042 s here):
`LEVEL_SHAPES["Flute 1"] += [[(107.96, 0.0), (108.02, 3.0), (108.29, 3.0), (108.34, 8.0), (108.47, 8.0), (108.53, 3.0), (108.62, 3.0), (108.72, 0.0)]]`
Predicted from the stem: head -39 to -36, hole -42 to -39, then -38.5 rising into the printed crescendo; margin at the downbeat about 0 K / +4 A, as in c49. Add `Flute 1:108` to the join list of `dips50.py` and check the row on a short range render (qn 106-110) before the full render, because a +5 dB step placed 40 ms off the hole would be heard as a bump; if the hole's time differs between two range renders, use a flat +3.5 dB from 108.02 to 108.62 only. If the hole stays deeper than 4 dB, test a higher velocity on the F5 (100-110; velocity changes the join's timing on this row) in the same range render.

Judgement: levels measured; cause inferred.

### 2. Violoncellos, bar 73 (qn 245.75-247): the new C4 shape puts the counter-melody 6-8 dB over the violins' theme

Where: Violoncellos, C4 at qn 246 (p, hairpin peak, "cantabile"), against Violins I and II (theme, p).

What is wrong: c50's shape for critic C #4 (`[(244.6, 0), (245.0, -1.5), (245.55, -1.5), (245.75, 4.0), (246.6, 4.0), (247.8, 0)]`) passed C's two conditions with 3.9 and 4.5 dB to spare and raised the cello 6.5 dB at 246.0. Measured, K per half beat (c49 in brackets): Violoncellos 245.0 -38.0 (-36.5), 245.5 -39.2 (-41.9), 246.0 -34.5 (-41.0), 246.5 -36.9 (-40.6), 247.0 -40.1 (-42.1). Violins I at the same half beats: -41.9, -42.4, -42.4, -42.2, -43.0; Violins II -40.8, -44.5, -47.3, -43.9, -44.6. At 246.0 the cello is 7.9 dB K (6.0 dB A) over Violins I and 12.8 dB over Violins II; in c49 it was 1.4 dB over Violins I. The master at 246.0 rose 3.3 dB (-36.5 to -33.2), all of it cello. In the first statement of the same music (bar 25, qn 74, C4 at the hairpin peak) the cello is level with both violin sections (-41.2 against -41.5 and -41.3 K).

Fix (`build/score_config.py`, replace the c50 row):
`[(244.6, 0.0), (245.0, -2.5), (245.55, -2.5), (245.75, 0.5), (246.6, 0.5), (247.8, 0.0)]`
Predicted by subtraction on the stem: 245.0 -39.0, 246.0 -38.0, 246.5 -40.4. C's conditions still pass: 246.0-246.5 minus the loudest half beat of 244-246 about +0.4 (need at least -1), minus 244.0-244.5 about +4.8 (need at least 3). The cello is then 4.4 dB K (2.5 dB A) over Violins I at the peak and under 2 dB over them elsewhere in the bar.

Judgement: measured; the predicted values assume the post-fader shape is linear in dB, which c45 measured.

### 3. Bass clarinet, bar 37 beat 1 (qn 108): the D flat 3 swells 4 dB on arrival and is level with the flute

Where: Bass clarinet, D flat 3 at qn 108 (printed p with a decrescendo to 110; the end of its solo), under Flute 1's arrival.

What is wrong: the note's first 0.4 s is 4 dB over its own body and over the C3 before it. Measured (stem, unweighted, 60 ms steps): -42.6 at +30 ms, -41.8 at +150, -39.8 at +210, -38.5 at +270, -38.8 at +330, -42.1 at +390, -44.7 at +450, -46.0 at +510 and -46.3 to -47.6 after. K levels: 108.0-108.5 -41.4 and -40.9, body -46.1, the C3 before it -44.2 to -45.4. A-weighted it is -45.3 and -44.5 against the flute's -42.6 and -44.6, so the two are level on the downbeat even with the low register discounted. The envelope there is +1.0 falling to -0.4 dB and CC11 is flat at 53-54, so the swell is in the sample (inferred). Series 1 had a note trim for this place (`Bass clarinet 108: -3`, c25 critic B #4); the port removed it because the solo moved down an octave.

Fix (`build/score_config.py`): `LEVEL_SHAPES["Bass clarinet"] += [[(108.04, 0.0), (108.12, -3.5), (108.36, -3.5), (108.46, 0.0)]]`. A note trim is the wrong tool here: it ramps in over 0.6 s and would lower the body, which is already 5 dB under the flute. Predicted: the swell peaks at about -42 unweighted, level with the C3 before it. With finding 1 the flute's A margin on the downbeat comes to about +5 dB.

Judgement: measured; cause inferred.

### 4. Flute 1, bar 37 beat 4 (qn 111): do not add trim; the note's first 0.4 s sags and its second half surges

Where: Flute 1, E flat 5 at qn 111 (the printed peak of the crescendo), the open item from c50 (body 1.0 dB over the F5 at 108, 1.5 wanted).

What I measured: bodies K 108 -37.2, 110 -35.7, 110.5 -35.5, 111 -36.0, 112 -38.3. By my body measure the note at 111 is 1.2 dB over the note at 108. The body figure hides the shape inside the note. Per quarter beat: 110.0-111.0 -34.9, -35.2, -36.8, -36.3; 111.0-112.0 -38.5, -39.5, -34.1, -33.0. The first half of the peak note is 3.3 dB under the beat before it and 5.5 dB under its own second half, and the loudest moment of the bar comes three quarters of a beat after the printed peak. The E flat 5 fundamental reads -46 to -51.5 over the first 0.39 s and -43 to -39 from +0.45 s. The envelope is already +12.4 to +13.2 dB at the note's start and +7.4 at 111.35, where the early fill has decayed and the note trim has not yet ramped in.

The crescendo as a whole is audible without more trim: pickup -41.3, first beat of the F5 -41.0 / -43.1 (about -38.5 after finding 1), 109-110 -35.7, 110-111 -35.7, second half of 111 -33.5. The 1.5 dB test compares the body of a note that contains most of the crescendo with the goal note, and finding 1 will raise the F5's body by about 0.5 dB, so the test will read worse after a real improvement.

Fix: (a) `build/early_fills.json` Flute 1 `"111": {"db": 7.9, "pre_s": 0.0, "hold_s": 0.1}`: set `hold_s` to 0.30, so the fill stays through the sag and is gone by +0.55 s, before the sample's own swell. Predicted quarter beats at 111: -38.5, -34.5, -34.1, -33.0 (the second quarter gains about 5 dB). Keep the note trim at 5. (b) Replace the acceptance test with two that follow the shape: 111.0-111.5 not more than 1.5 dB under 110.5-111.0 (now 2.7 under), and 111.5-112.0 not more than 2.5 dB over 110.0-111.0 (now 2.2 over). (c) No further rise on Flute 1 in this bar: the envelope would pass +15 dB on a solo stem, and the hall send is post-fader.

Judgement: measured; the prediction for (a) is computed from the fill's documented shape.

## Checked, no change proposed

- The pickup at 107 (the lead's question): C5 body -41.1 K / -42.5 A at printed p; margin over all other stems +3.2 K / +5.2 A in its first half and +2.8 / +4.7 in its second. It enters at -43.2 in its first quarter beat and holds -40.8 to -41.3. The bass clarinet's B flat 2 and C3 under it read -45.7 and -45.1. The master rises from -43.3 (106.75) to -38.5 (107.5). The level of the pickup is right; the problem of the entry is the arrival (finding 1) and the bass clarinet's swell (finding 3). The bass clarinet's bar 36 margin fell from +3.0 to +0.2 K because the flute now plays over its last notes; that is the score.
- c50's other level changes arrived as intended (half-bar K levels, c49 to c50): Horn 1 bar 11 second half -34.8 to -37.1 and bar 12 first half -36.5 to -34.4; Cor anglais bar 42 -37.4 / -40.0 to -34.3 / -37.4 (solo margin bars 41-44 +0.1 to +1.8 K, +3.3 to +5.1 A); Violins I bar 59 -27.6 / -28.6 to -24.7 / -25.5 and Violins II +3.0 to +3.5; Clarinet 1 bar 87 first half +1.6; Flute 1's trims at 112-121 are inside my c50 targets (112 -38.3, 113 -41.3, 113.5 -39.9, 121 -42.2). No stem changed by 1.5 dB or more in any other half bar.
- Oboe 1 bar 47: critic C's 2 dB dip after 148.3 lowers the mf note 1.4 to 4.0 dB between 148.75 and 149.75 and the bar's margin from +1.1 to +0.1 K (A +3.6 to +2.7). From 148.5 on the oboe is still +3.8 to +4.8 K over the others; the bar's low average comes from the strings' fp on the downbeat. Keep, unless C's c51 limits are met with a smaller dip.
- Solo margins otherwise equal c49 within 0.3 dB: Horn 1 bars 7-14 +7.4 K; Oboe 1 bars 15-16 +3.0; Violin I solo bars 17-18 +7.0; bass clarinet bars 31-35 +3.1 to +7.6 per bar; Flute 1 bars 37-40 +4.0 (c49 +3.4); cor anglais bars 47-50 +2.5; Trombone 1 bars 63-64 +6.2; Horn 1 bars 67-68 +13.5 and +11.1; Clarinet 1 bars 85-89 +1.4 K / +4.7 A.
- Climaxes: bar 61 strings -16.5, brass -17.9, woodwinds -19.8, timpani -32.0 K; bar 79 woodwinds -22.2, strings -22.1, brass -27.2, timpani -37.7. Timpani and low brass do not cover. The master rises bar by bar from 57 to 61 (-25.7, -22.6, -20.2, -16.2, -12.8), so bar 61 is still the loudest after the +3 dB on the violins in bar 59.
- Bar 60: the Violoncellos' rising line is 1-3 dB over Violins I in K from 201.5 to 203.5 (-22.1 to -19.8 against -25.3 to -20.9) but 2.9 dB under them A-weighted (bodies -28.8 against -25.9), and it was the same in c49. Not a finding on this evidence.
- Dynamic mapping (A-weighted medians of note bodies): pp woodwinds -54.7, horns -54.6, strings -54.9, divisi and solo -53.9; p -49.4 / -48.8 / -47.3 / -45.8; mf -42.5 / -42.1 / -38.3 / -41.0; f woodwinds -39.2, horns -34.3, strings -35.7, low brass -28.0. Unchanged from c49 within 1.1 dB.

## Do not touch

Everything on my c50 list, and from c50: the Horn 1 bar 11 and Cor anglais bars 41-42 shapes; the C1 shapes at 193-204; Clarinet 1 `[286.0, 286.9, 2.5]`; Flute 1's trims at 111-121 and its pickup data at 107 (velocity, CC11 54, the role `[107, 112, 2]`); Horn 1 `198: 1.5`; the Violins II shape through 254; `TOP_RATIO` 2.0 unless the delivery targets fail; no compensation at Trombone 1 217.5.

Scratch folder: `/private/tmp/claude-501/mockup-loop/mvt2-c51-B/` (179 MB: `lib.py`, `m1.py`-`m7.py`, `f1.py`-`f9.py`, cached frame levels of the c50 stems) is left in place, because the launcher's instruction for this run was not to delete files.

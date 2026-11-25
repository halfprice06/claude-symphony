# Critic B, cycle 53: balance and levels (c52 render)

Under review: `cycles/c52/render` (stems and master) and the data that produced it (`build/parts.json`, `build/roles.json`, `build/note_trims.json`, `build/pitch_trims.json`, `build/mix.json`, `build/score_config.py`, `tools/score_to_parts.py`, `cycles/c52/CHANGES.md`).

Method. Levels come from the per-track stems, K-weighted, 8192-sample Hann FFT, hop 4096, one value per quarter note on the tempo map of parts.json. The dB reference is arbitrary; only differences count. "Margin" is the lead stem minus the loudest single other stem in the same quarter. Row medians use the quarters in which the lead is within 15 dB of its maximum in the span. This reproduces the actor's bal52.py within 0.1 dB on the rows I compared. A second scale with hop 1024 ("fine") is used for half-quarter arrivals and reads about 6 dB lower. Bar b starts at qn 4(b-1). Every number is measured on the c52 stems unless it is marked inferred. The "after the fix" numbers are dB additions to the measured stems. Nothing was rendered and REAPER was not touched.

## Manual notes

Third round: critics pick their own pages. I read the woodwind pages (108-110), the controller pages (64, 151), the timpani pages (123-125), the tam-tam and cymbal pages (118-119) and the brass controller pages (101, 105-106) of the 2021 HO manual, with DIGEST.md and MANUAL-GAPS.md.

| Reading (2021 manual, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| CC11 is expression (level), CC7 the track ceiling, CC1 the vibrato crossfade on the Opus woodwind masters (p.64, p.151). p.109's "dynamics of the Sustain patches are controlled with the Mod Wheel" is Play-era text. DIGEST §7.2: on the Flute, Oboe, English Horn and Bassoon KS Masters Vib fades in over CC1 55-64 and Non Vib fades out over 64-76. | `cc1_fn0` in tools/score_to_parts.py gives un-slurred held wind notes CC1 38-55 at ppp to p, so they play the Non Vib layer alone. | The mapping matches the manual. The level does not hold: Oboe 1 and Flute 2 read 10-14 dB under their own CC11 fit in that state (finding 4). |
| Same pages: level belongs to CC11 and the track, not to CC1. | Every fix below is a role row, a level shape or a note trim (track envelope), none is a CC11 change. | Yes, and it matches Dan's priority 6 (do part of the work in the mix). |
| Timpani Felt Rolls: CC11 and velocity set loudness, CC1 the dynamic layer, 8 levels (p.124). | All 16 rolls. | Yes. All rolls re-measured (table below). One level shape ends before its roll does (finding 6). |
| Timpani Felt Cresc: live-recorded crescendos, velocity picks 2 dynamic levels (p.123). MANUAL-GAPS #12: never tried on the 13 timpani crescendo hairpins. | Rolls 2, 4, 6, 8, 9, 11, 13, 14. | Not used. The CC-drawn crescendos stay inside rule 5, so there is no level reason to change patch. It stays a timbre question for lens A. |
| Suspended cymbal rolls (p.119). | Bars 158-160, qn 631-636. | In use. The rise is late: 5.3, 15.5, 20.3, 26.8, 40.8, 42.5 against all stems at 55.7-61.3, so the roll is covered until the last beat. Remark only. |
| Tam-tam (p.118). | Bar 122 fff (qn 484-491), bar 175 pp (qn 696). | Levels fit: fff 50.9-53.8 against winds 53-54, upper strings 52, trombones and tuba 51-53; pp 19.0 against Trombone 1 22.5. |
| Brass: CC1 is the dynamics crossfade, CC11 the level (p.101, p.105-106). | `CC1_DYN_TRACKS` in score_config.py. | Yes. Remark: Trumpet 1's median level is 39.6 at f, 39.0 at ff, 47.8 at fff, so the f to ff step is missing in level. Not examined to a fix. |

MANUAL-GAPS still open and relevant to this lens: #12 (Felt Cresc, above), #5 (expressive rows for wind solos; the Clarinet 1 and cor anglais solos below use plain sustains), #4 (Mid mics on winds).

## EW-TEMPLATE-PLAN sections this lens touches

Applied (c50-c52), with no level problem traced to them: section 1 (mic layout), section 2 (reverb returns), section 3 (section EQ), section 9 "brass as narrow sources" (new in c52; brass minus strings moved by at most 1.1 dB at the four tuttis of the actor's table). Section 8's phrase arch and section 9's hairpin shapes are applied; the low-wind arch has one side effect in level (finding 5).

Applied in the lanes but not in the result: section 10 "doublings share one curve". At bars 124-126 Oboe 1 and Violins I have the same lane within 8 points (oboe 90, 82, 74, 64, 58, 50, 46, 46; violins 82, 75, 69, 61, 56, 49, 46, 46), and the oboe ends 8-13 dB under the violins (finding 4). Section 10 "level lane follows the timbre lane" is what `cc1_fn0`'s held-note table does for winds; on the oboe and second flute it produces the level drop of finding 4.

Not yet applied (as listed in cycles/c52/CHANGES.md, and unchanged in the data): section 5 legato overlap (19-21 ms against 45-80) and legato velocity by dynamic; section 5 CC1-only macro (tried on the celli, failed A's join rule); section 6 two tracks per string section (when it is applied, the same-dynamic rows need a new base); section 7 per-note lean-off; section 8 tutti entry spread and room bed; section 10 beat-position short velocity outside the listed spans.

## The edge rows and the two post-render rows

| Row | Actor's c52 value | Re-measured | What it needs |
|---|---|---|---|
| Violins I theme, bars 15-22 | +3.5 against 3.5 | +3.47 (31 quarters). Bars 15-16 carry the median; bars 17-22 alone read +1.8, six quarters are under 0. | Finding 1. |
| Clarinet 1 coda minimum | +1.9 against 2.0 | +1.9 at qn 699. The row covers 699-705; qn 706 (outside it) reads -1.0. Median fell from +6.6 to +4.8. | Finding 5. |
| Horns minus heavy brass, bars 123-126 | -4.0 | -3.97. Only bar 123 decides it (qn 488-491: -3.6, -4.4, -4.8, -9.2). From 492 the trumpets are gone and the row reads -0.7 to +28. | No mix change. Define the row as qn 484-492 (reads about -4.1) with a band of -5.5 to -4.0. |
| Same-dynamic horns at p and f | 0.5 dB lower than c51 | p -0.46 (n 131), f -0.61 (n 324), the same on all four horns; trumpets and trombones within 0.1. | Re-base the row on c52. Inferred cause: c51's horn tracks held stale legato envelope state (the problem the mockup kit records from scherzo c09), so c52 is the correct base. |
| pp winds | +1.6 from the low-wind arches | +1.3 by my bins. Only the arch spans moved: Bass clarinet 699-710 (+2.1 to +2.8), Bassoon 1 586-595 (+2.3 to +3.5) and 693-694, Bassoon 2 602-607, 612-613, 681-686 (+2.1 to +3.4). Other pp winds within 0.1. | Re-base on c52 or exclude those spans. Side effect in finding 5. |
| Horn 1 legato minus other | +1.6 against 1.5 | Not re-measured (an articulation row). 0.1 dB is inside the repeatability of the method. | No level action. |
| Horn 3 [165.5, 168, -3.5] (post-render) | added after the render | roles.json holds the row and the delivered Horn 3 stem already reads 3.50 dB under the first c52 render at 166 and 167. The project does not hold it. | The c53 build must apply it in the project. If c52's stem correction is a post-render step that would run again, remove it so the cut is not applied twice. No further cut. The row itself should change: Horn 3 plays the same notes as Horns a2 (Eb3 163, C4 164, Bb3 165), so it is a unison partner. Horns a2 plus Horn 3 over the loudest non-horn stem reads 163 -1.9 (Violins II 39.4, Violins I 39.2), 164 +9.0, 165 +8.0, 166 +7.9, 167 +6.2. New row: at least +6 at 164-167. |
| Cor anglais [584, 608, +1.5] (post-render) | added after the render | roles.json holds it and the delivered stem carries +1.50. Cor anglais minus Horn 1 over bars 147-152 reads -5.6; per bar -11.1, -6.4, -3.6, -1.0, -7.3, -7.5. | Keep the row. The median hides the third answer (finding 3). Define the row per answer. |

## Timpani rolls (Dan's standing rule): all 16 re-measured

Margin is the timpani stem minus the loudest other stem per quarter, median and maximum over the roll. "Low share" is the timpani's mean share of the 30-150 Hz energy of all stems.

| # | Bars | Printed | Median / max | Low share | Note |
|---|---|---|---|---|---|
| 1 | 1-4 | ppp, dim. in bar 4 | alone at qn 0-2, then -4.0 to -17.5 | 28 % | Timpani lead at the start. Bar 4 rises against the printed dim. (finding 6). |
| 2 | 11-12 | pp < f | -8.2 / -2.6 | 27 % | f stroke at qn 44: -0.1. |
| 3 | 13-14 | p > pp | -21.5 / -14.9 | 29 % | |
| 4 | 40-43 | pp < ff > pp | -11.6 / -6.1 | 30 % | Low share 46-51 % at qn 157-159, 55 % at 169. |
| 5 | 62-63 | pp < > | -6.0 / -4.9 | 33 % | |
| 6 | 71 | mf < f | -12.0 / -6.7 | 17 % | |
| 7 | 76 | ppp | -4.7 / -3.1 | 17 % | |
| 8 | 80-81 | p < ff | -7.2 / -2.4 | 31 % | |
| 9 | 115 | mf < f | -9.9 / -8.3 | 13 % | |
| 10 | 117-130 | f, fff, dim., cresc. | -9.9 / -1.7 | 17 % | f arrival 464 -4.0, body -5 to -12.5; fff arrival 484 -4.0; 492 -1.7; 493-497 -3.2 to -4.6; 498-515 -10 to -23; crescendo 516-520 up to -4.2. |
| 11 | 140 | f < ff | -7.4 / -4.2 | 28 % | ff stroke at 560: +3.1 on the first half-quarter only. |
| 12 | 144-146 | mp > pp | -13.0 / -4.9 | 22 % | |
| 13 | 158-161 | ff < fff > | -6.2 / -1.3 | 36 % | 628 -1.3 (fine arrival +1.2, 70 % low share); 629-631 -7.9 to -10.1; 632-635 -7.0 to -2.9; fff at 636 -2.1; 637-640 -5.4 to -7.2. |
| 14 | 166-169 | p < f < | -6.8 / -0.1 | 30 % | f arrival 664 -0.1 (fine +2.6 on the half-quarter), then -6.2 to -11.4; ff stroke 676 -0.4. |
| 15 | 174 | pp | -18.8 / -16.0 | 78 % | Under the Cello solo. The low share is high because nothing else plays below 150 Hz. |
| 16 | 181-182 | ppp | -10.9 / -7.0 | 9 % | |

Result (measured): no roll is the loudest stem beyond a half-quarter arrival (560, 628, 664; 44, 636 and 676 are within 0.5 dB of the loudest stem), and every roll sits 5-12 dB under the loudest stem after its arrival. Rule 5 holds on the c52 render. In 30-150 Hz the timpani exceed every single bass stem at qn 157-158, 169, 245-246, 558-559, 628, 630-631, 664 and 692-695; that is a watch list, not a request. The one roll that moves against its printed mark is bar 4 (finding 6).

## Section balance (no finding)

Family sums at the tuttis, in the order brass minus strings, trumpets minus trombones and tuba, trumpets minus Violins I, winds minus strings: bars 25-26 -1.2, -1.7, -1.9, -2.0; 27-32 -0.2, -1.5, -2.3, -0.7; 41-42 -0.2, -0.2, -1.1, -3.7; 115-116 -0.3, +1.0, +1.3, -0.5; 122 +2.8, -1.9, +1.2, +0.3; 123-126 +2.1, -2.9, +0.1, -0.5; 140-141 -3.5, -2.8, -6.0, -0.1; 158-159 -1.3, +1.2, -1.4, -2.7; 160-161 -0.8, +3.7, +0.7, -1.8; 167-170 +1.6, -0.7, +2.4, -1.1. Horns minus heavy brass: 25-26 -3.9, 27-32 -3.0, 41-42 -2.5, 115-116 -6.4, 122 -3.8, 140-141 -6.5, 158-159 -3.7, 160-161 -4.7, 167-170 -5.6.

Reading (inferred). Rimsky-Korsakov's table (Principles, p.33; reference-books/text/rimsky-principles.txt lines 1962-1990) gives, at forte, 1 trumpet = 1 trombone = 1 tuba = 2 horns and one wind = half a string department. For this scoring that works out to horns about 5.4 dB under the heavy brass, winds about equal to the strings and the brass about 5.6 dB over the strings. The render matches the first two. The brass sit 3-7 dB lower against the strings than the table says; earlier cycles set that on Dan's listening notes, and it should stay. At bars 160-161 the trumpets are 3.7 dB over trombones and tuba because Trumpet 1 doubles the Violins I theme an octave lower at qn 629-644 (Trumpet 1 51.7-53.5, Violins I 53.1-49.0); that is the scoring, not a fault. The low band (30-150 Hz) of the master reads 11.0-13.2 dB under the full band in the tuttis and 16.3-21.2 dB under in the soft sections: the bass is solid and not boomy.

p across the families (median stem level at printed p): Cor anglais 31.0, Oboe 2 30.7, Clarinet 1 28.3, Violins I 28.3, Trombone 1 27.6, Bass clarinet 27.4, Horn 2 26.6, Violas 25.9, celli 25.2, Horn 1 25.0, Clarinet 2 24.7, Flute 1 24.4, Bassoon 2 23.9, Violins II 23.8, basses 23.6, Horn 3 22.7, Horn 4 22.1, Bassoon 1 21.7, and Oboe 1 15.3. Oboe 1 is the one track outside the range of the others, 21.7-31.0 (finding 4). Watch item, not examined to a fix: in bars 23-32 the melody group minus everything else reads +0.3, -1.4, -1.4, -5.4, -1.9, -0.9, -2.3, -2.3, -1.3, -4.3 per bar.

## Findings

### 1. Bars 17-22 (qn 64-88): the celli's half notes are as loud as the Violins I theme

Where. Violins I carry the theme (f, crescendo from 72.5, ff at 78). The celli play a printed-mf line in half notes under it.

Evidence (measured). The check row covers bars 15-22 and passes at +3.47 because bars 15-16 read +4.9 to +13.9. Bars 17-22 alone have a median of +1.8. Per quarter, Violins I margin and the loudest other stem: 64 -3.0 (celli; the violins have only an eighth-note pickup), 65 +5.1, 66 +1.8 (celli), 67 +1.0 (celli), 68 +3.8, 69 +6.5, 70 +3.3 (celli), 71 +0.2 (celli), 72 -0.4 (celli), 73 +0.3 (celli), 74 -2.3 (celli), 75 -0.5 (celli), 76 +3.8, 77 +1.7 (violas), 78 +3.5, 79 +4.6, 80 +1.9 (violas), 81 -0.6 (celli), 82 +10.5, 83 +6.6, 84 0.0 (violas), 85 +2.3, 86 +1.6. Six quarters are under 0 and thirteen under +2.

Causes (measured in the data). The lead rows end in the middle of the theme: roles.json Violins I [56, 72, 2] and Violoncellos [56, 72, -2] both stop at qn 72. The celli line is uneven by pitch at a flat lane: on the fine scale F3 (64, 72, 80), Ab3 (66) and Ab2 (74) read 5-8 dB over D3, Eb3 and G3, and F3 and Ab3 swell 4-6 dB in their second quarter. Against c51 the violins are 1.6-3.7 dB lower at qn 81-85 and the celli 0.7-1.2 dB higher at 71-75, which is why the row fell from +4.3 to +3.5.

Fix.
- `build/roles.json`, Violins I: change [56, 72, 2] to [56, 88, 2].
- `build/roles.json`, Violoncellos: change [56, 72, -2] to [56, 84, -2]. Stop at 84 so that the +2.4 dB note trim on the celli note at 84.0 (note_trims.json; see score_config.py line 2905) keeps its effect.
- `build/note_trims.json`, Violoncellos: add "64.0": -2, "66.0": -3, "70.0": -2, "72.0": -2, "74.0": -3, "80.0": -2.

After the fix (dB addition): row median +5.5, lower quartile +3.9, minimum -1.0 at qn 64 (the pickup quarter), every other quarter at +2.0 or more. Per quarter: 65 +7.1, 66 +4.8, 67 +4.0, 70 +5.3, 71 +2.2, 72 +3.4, 73 +6.3, 74 +4.7, 75 +6.5, 76 +5.8, 77 +3.7, 78 +5.5, 79 +6.6, 80 +3.9, 81 +5.4, 82 +12.5, 83 +8.6, 84 +2.0, 85 +4.3, 86 +3.6. The Violins I peak rises from 46.7 to 48.7 at qn 82, under the 52-54 the upper strings reach in the tuttis, so no headroom problem is expected (inferred).

### 2. Bars 115-116 (qn 456-464): the celli's inner voice is the loudest stem in the crescendo

Where. The celli hold F3 (456) and F#3 (460), doubled by Bassoon 1. It is the third of the chord; the basses have Db2 and C2 below. The melody is in Flute 1, Flute 2, Oboe 1, Trumpet 1 and Violins I.

Evidence (measured). Per quarter 456-463: celli 37.0, 41.7, 47.2, 49.0, 44.3, 48.1, 48.3, 43.4; Violins I 42.5, 42.3, 43.7, 43.1, 44.3, 46.8, 46.5, 45.9; melody group 45.3, 45.5, 46.9, 46.6, 47.3, 49.5, 50.7, 51.9. The celli are over Violins I by 3.5 and 5.9 dB at 458-459 and by 1.3 and 1.8 dB at 461-462, they are the loudest single stem in those four quarters, and at 458-459 they are level with or above the whole melody group (group minus celli -0.3, -2.4). The celli's lane here is 79-87, under f, and the stem reads 47-49, above the celli's ff median (42.8) and fff median (45.3). The F3 grows 12 dB inside one note while the lane rises from 79 to 83. Against the celli's own CC11 fit the residuals are +11.1 at 458 and +7.5, +11.0, +11.0 at 460-462. c51 reads the same, so this is not new in c52. Bassoon 1's F#3 at 460-462 reads 43.6, 43.7, 44.0, which is 4 dB over its fff median (39.6); its notes are un-slurred, so the legato-only pitch trim '54': -5 in pitch_trims.json does not reach them. The other harmony stems read 37-43.6.

Fix.
- `build/score_config.py`: `LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [[(456.0, 0.0), (457.0, -2.5), (458.0, -6.5), (459.0, -8.0), (460.0, -8.0), (460.1, -6.0), (463.5, -6.0), (464.0, 0.0)]]`. The celli's envelope already falls from 463.5 into the role [464, 484, -6, 0.5]; after the build, read `vol_db` at 463.5-464.2 and make sure the release of this shape adds no rise there.
- `build/note_trims.json`, Bassoon 1: add "460.0": -5.

After the fix (dB addition): celli 35.8, 37.2, 40.0, 41.0, 38.2, 42.1, 42.3, 40.7; Violins I minus celli +6.7, +5.1, +3.7, +2.1, +6.1, +4.7, +4.2, +5.2; Bassoon 1 38.6, 38.7, 39.0 at 460-462. The melody group's own rise (45.3 to 51.9) is unchanged.

### 3. Bars 151-152 (qn 602-606): the cor anglais's third answer is 10 dB under the tune

Where. The cor anglais answers the tune three times with the same marks (p dolce, lane 46 to 68 to 46): qn 586.5-590, 594.5-598, 602.5-606. Horn 1, violas and celli carry the tune.

Evidence (measured). Cor anglais per quarter: first answer (586-589) 28.2, 30.5, 36.5, 34.1; second (594-597) 24.9, 32.9, 37.7, 35.7; third (602-605) 28.8, 28.3, 26.1, 24.4. On the long note the cor anglais is 0.9 and 4.3 dB under the loudest tune voice in the first answer, 0.3 and 2.8 dB under in the second, and 10.7 and 10.7 dB under in the third. The accompaniment sum at 604-605 (30.3, 28.6) is above it. The printed crescendo into the third long note reads -2.4 dB where the other two rise 6-8 dB.

Cause (measured in the data). `vol_db` is +4.0 at 589.5 and 597.5 and -9.4 at 605.5. Three things stack on the third answer: the pitch trim on A4 (-5), the note trim "604.0": -4.5, and the end of the role [586, 598.5, 4, 0.5] before it. The stems show when it went wrong (plain RMS at 603, 604, 605): c49 -41.3, -40.7, -44.0; c50 -48.3, -50.2, -52.8; c51 and c52 -46.3, -48.3, -50.2. The answer fell 7-9.5 dB in the c50 template rebuild while its two siblings kept their level. Inferred: the -4.5 note trim was set for the old mic set and is no longer needed.

Fix.
- `build/note_trims.json`, Cor anglais: delete "604.0". Remove the matching `NOTE_TRIM_RAMP_S["Cor anglais"]` entry for 604.0 in score_config.py (lines 2150-2152).
- `build/roles.json`, Cor anglais: add [602.25, 606.5, 3.0, 0.25]. Keep [584, 608, 1.5] and [586, 598.5, 4, 0.5].
- Keep the A4 pitch trim (-5): A4 still reads 5.3 dB over the cor anglais fit.

After the fix (dB addition): 603 31.3, 604 33.6, 605 31.9; cor anglais minus the loudest tune voice -3.2 and -3.2, in line with the first two answers.

### 4. Oboe 1 at p: bars 124-126 (qn 496-504) and the chord in bar 43 (qn 168)

Where. In bars 124-126 Oboe 1 and Violins I play the same line in unison (G5 tied, F5, Eb5 at 496, D5 at 497.5, C5 at 498, D5 at 500 for four quarters), decrescendo to p at 500, with Horn 1 mp espr. from 497. In bar 43 Oboe 1 and Flute 2 hold Eb5 in the p wind chord.

Evidence (measured). Per quarter 494-503: Oboe 1 38.4, 36.5, 20.7, 22.0, 27.8, 26.9, 15.3, 12.8, 12.0, 11.8; Violins I 37.0, 33.8, 33.8, 32.1, 31.0, 30.2, 22.9, 20.8, 21.9, 21.0. The oboe is 1.4-2.7 dB over the violins at 494-495 and then 13.1, 10.1, 3.2, 3.3, 7.6, 8.0, 9.9, 9.2 dB under them. At 500-503 the clarinets read 24-30 and Bassoon 1 25-27, so the oboe's held D5 at 12-15 does not sound in the chord. At qn 168 Oboe 1 reads 14.8 and Flute 2 16.5 against Clarinet 1 24.3, Clarinet 2 21.0, Bassoon 2 22.0, Horn 3 21.9, Horn 2 25.1 and strings at 21.2-24.6.

Two measured causes. (a) The oboe patch has a 6-8 dB step in level between Eb5 and E5 on both oboes: residual over the CC11 fit is -4.8 at C5, -5.8 at D5, -5.0 at Eb5 and +3.6 at E5, +2.9 at F5, +2.8 at G5, +4.6 at Ab5. That explains the fall at 496-497 while CC1 is still 100. (b) On the un-slurred held notes the controllers go low together: at 500.5 lane 46, CC11 37, CC1 45; at 502.5 CC11 34, CC1 42; at 168 CC11 33, CC1 42. A fit over both oboes (level = 0.16 x CC11 + 19.8, minus 8.6 when CC1 is under 55; rms 3.7) puts about 8.6 dB on that state; against the fit for CC1 at 64 or more, Oboe 1 reads -11.3 at 168 and -9.8, -12.2, -12.6, -12.7 at 500-503, and Flute 2 -14.2 at 168. Inferred: the Non Vib layer of these two patches is much quieter than the Vib layer. The regression cannot separate that from the Sus row's own behaviour at low CC11, because the two always occur together in this score.

Fix (level now, cause test later).
- `build/score_config.py`: `LEVEL_SHAPES["Oboe 1"]` add [[(499.9, 0.0), (500.0, 8.0), (503.8, 8.0), (504.0, 0.0)]] and [[(495.95, 0.0), (496.0, 6.0), (497.9, 6.0), (498.0, 0.0)]]. The existing -3 dB shape at 498.6-499.9 (line 2627, for Horn 1) stays.
- `build/note_trims.json`: Oboe 1 add "168.0": 7; Flute 2 add "168.0": 6.

After the fix (dB addition): Oboe 1 at 500-503 23.3, 20.8, 20.0, 19.8 against Violins I 22.9-21.0; at 496-497 26.7 and 28.0 (still 4-7 dB under the violins and under Horn 1 from 498); at 168 Oboe 1 21.8 and Flute 2 22.5.

Cause test for a later cycle (inferred, untested; it also changes vibrato, so lens C should hear it): a floor on the held-note CC1 table in `cc1_fn0` for Oboe 1, Oboe 2 and Flute 2, for example a config constant `WIND_HELD_CC1_MIN = 64` applied to the function's last line. Render the bar-125 D5 alone with and without it and compare with the 12-15 it reads now. If the level comes up 8 dB, the trims above can go.

### 5. Bars 175-177 (qn 699-708): the c52 low-wind arch lifted the bass clarinet under the Clarinet 1 solo

Where. Clarinet 1 pp espr. (Eb4 pickup at 699, C5 at 700 for six quarters, B4 at 706 with a decrescendo) over the bass clarinet's pp line.

Evidence (measured). Clarinet 1 margin, c51 to c52: 699 +0.6 to +1.9 (against Trombone 1's chord at 20.8), 700 +8.1 to +4.8, 701 +4.9 to +2.6, 702 +6.7 to +4.2, 703 +8.3 to +6.6, 704 +5.1 to +5.3, 705 +6.6 to +5.9, 706 -0.2 to -1.0 (bass clarinet 22.7 over the clarinet's B4 at 21.7). The bass clarinet rose 2.1-2.8 dB at 700-707 (18.1 to 20.2, 21.0 to 23.4, 21.1 to 23.5, 19.2 to 21.6, 18.9 to 21.6, 18.5 to 21.4, 19.9 to 22.7, 22.9 to 25.7). The cause is the `SWELL_CAP_TO_VOL_DB_PER_CC` arch from C's finding 3 in c52. The row's median fell from +6.6 to +4.8.

Fix.
- `build/roles.json`, Bass clarinet: add [699.5, 708.0, -2.0, 0.5]. This keeps the shape of the arch and returns its level to c51.
- `build/note_trims.json`, Clarinet 1: add "699.0": 1.5. The pickup's +1.9 is measured against Trombone 1's chord, so the bass clarinet row does not change it; the trim gives +3.4.

After the fix (dB addition): 699 +3.4, 700 +5.9, 701 +4.6, 702 +6.3, 706 +1.0; row median about +5.9.

### 6. Bar 4 (qn 12-16): the timpani roll rises against its printed decrescendo

Where. Timpani, ppp roll, lane 17 to 10 over the bar.

Evidence (measured). Timpani 19.5, 17.7, 18.0, 19.4 at qn 12-15 while the celli fall 23.5, 22.0, 21.4, 18.9, so the timpani end the bar 0.5 dB over the celli. The cause is in the data: the level shape at score_config.py line 643, [(12.4, 0.0), (12.9, -3.0), (15.6, -3.0), (15.9, 0.0)], returns to 0 dB over 15.6-15.9 while the last roll note sounds until 16.02 (`vol_db` 16.6 at 14.32, 19.6 at 15.9).

Fix. Change that shape to [(12.4, 0.0), (12.9, -3.0), (16.5, -3.0), (16.95, 0.0)]. Expected: qn 15 at about 18.0 or lower, no rise (dB addition; the roll's own decay should take it lower).

## Check table for the c53 render

| Row | c52 | Target |
|---|---|---|
| Violins I theme, bars 15-22 (qn 56-88): median / lower quartile / quarters under 0 | +3.5 / +0.65 / 6 | median at least +5, lower quartile at least +3.5, none under 0 except qn 64 |
| Celli minus Violins I, qn 456-463 | up to +5.9 | celli at least 2 dB under Violins I in every quarter, at least 4.5 dB under the melody group |
| Bassoon 1, qn 460-462 | 43.6-44.0 | 40 or lower |
| Cor anglais minus the loudest tune voice on each long note (588-589, 596-597, 604-605) | -0.9 / -4.3, -0.3 / -2.8, -10.7 / -10.7 | between -5 and 0 dB in all three answers |
| Oboe 1 minus Violins I, qn 496-503 | -13.1 to -3.2 | within 3 dB at 500-503, within 8 dB at 496-499 |
| Oboe 1 and Flute 2 at qn 168 | 14.8, 16.5 | within 4 dB of the clarinets (21.0-24.3) |
| Clarinet 1 coda, qn 699-706: minimum / median | +1.9 (-1.0 at 706) / +4.8 | minimum at least +2.0 over 699-705, 706 at least 0, median at least +5 |
| Horn unison (Horns a2 + Horn 3) over the loudest non-horn stem, qn 164-167 | +9.0, +8.0, +7.9, +6.2 | at least +6; Horn 3 stem at 166-167 unchanged from the delivered c52 stem |
| Horns minus heavy brass, qn 484-492 | about -4.1 | -5.5 to -4.0 |
| Timpani bar 4 | qn 15 is 1.4 dB over qn 14 | qn 15 not above qn 14 |
| Timpani rolls | none loudest beyond a half-quarter arrival | the same; the table above within 1 dB |
| Same-dynamic rows (horns p and f, pp winds) | moved 0.5 and 1.3-1.6 against c51 | re-based on c52; then within 0.5 dB, with the low-wind arch spans excluded |
| Family sums at the tuttis | list above | within 1 dB of the list |

All other rows of the c52 check table (cycles/c52/CHANGES.md lines 105-113) stay as they are.

## Dan's standing checks through this lens

Priority 2 (each track at its printed dynamic and role): four places fail on the c52 render and are findings 1-4; the Clarinet 1 solo is at the edge (finding 5). Other leads pass: Cor anglais bars 6-9 +11.1, Clarinet 1 bars 127-130 +8.5 (minimum +3.2), Cello solo bars 171-174 +8.3 (minimum +2.8), Violas bars 107-108 +5.7, celli tune bars 47-55 +4.5.

Priority 5 (timpani rolls): holds on all 16 rolls; one shape to correct (finding 6).

Priority 6 (comfortable at one headphone volume, work done in the mix): every fix here is a role row, a level shape or a note trim. None raises a peak of the master: the only upward moves are Violins I +2 dB at qn 72-88 (48.7 against 52-54 in the tuttis), the cor anglais's third answer, the oboe and flute at p, and the Clarinet 1 pickup.

## Do not touch

Keep: the family balance at the tuttis as c52 has it, including the brass sitting under the strings; the timpani roll levels, the soft-roll shelf and HP_CURVE's timpani skip; the Horn 3 row [165.5, 168, -3.5] and the cor anglais row [584, 608, 1.5]; the -3 and -5 dB shapes on Violins I and Oboe 1 at bar 125 for Horn 1; the cor anglais A4 pitch trim (-5) and its role [586, 598.5, 4, 0.5]; the celli role [464, 484, -6, 0.5] and the celli note trims at 84.0 and 88.0; Trumpet 1's level in the theme doubling at qn 629-644; the tam-tam and cymbal gains; the shape of the low-wind arches (only the bass clarinet's level at 699-708 changes); and everything on c52's list (brass bells and the 3.2 kHz bell, the 600 ms basses pp cap, REP_SPLIT gaps, the celli +4.2 dB at 464-484, the Trumpets a2 coda bell, the +0.5 ride rows, deliver_master.py settings).

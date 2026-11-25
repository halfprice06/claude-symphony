# Critic B, cycle 54: balance and levels (c53 render)

Under review: `cycles/c53/render` (the 17 stem-fixed stems, the pass-2 stems, the master) and the data that produced it (`build/parts.json`, `build/roles.json`, `build/note_trims.json`, `build/pitch_trims.json`, `build/mix.json`, `build/score_config.py`, `cycles/c53/CHANGES.md` with its addendum). `cycles/c54/COORDINATOR-NOTES.md` was read first.

Method. Levels are from the dry per-track stems (return stems excluded, so the stem fix's unchanged reverb does not enter), K-weighted, 4096-sample Hann FFT, hop 1024, stereo power, one value per quarter note (or half quarter where stated) on the tempo map of `parts.json` (`pcx.TM`). This scale reads 6.0 dB lower than the actor's `bal53.py` (checked on the celli at qn 456: 30.0 here, 36.1 there); only differences are used. "Low band" is 30-150 Hz unweighted. Comparisons with c41-c52 use the same measure on those cycles' stems. "After the fix" numbers are dB additions to the measured stems, not renders. Bar b starts at qn 4(b-1). Nothing was rendered; REAPER, the lock, `build/` and `~/.rpr-bridge` were not touched.

## Manual notes

No row for c54 in `loop/MANUAL-READING.md` (third round: critics pick their pages). Read in the May 2021 HO manual: p.34 (round-robin reset), p.64 (controllers), p.92-93 (string short articulations), p.108 (woodwind instrument list); also `MANUAL-GAPS.md` and `DIGEST.md`.

| Reading (2021 manual, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Pizzicato is a round-robin instrument with 2 or 4 distinct samples per note (p.92); the Basses row is "Pizz RRx4". | Double basses pizzicato, bars 47-55, 103-109, 147-155 (33 notes). | In use. The four takes and the pitches differ by up to 13 dB at one velocity (finding 4). |
| The round-robin cycle is reset by the controller entered in Preferences (p.34). MANUAL-GAPS #6: Opus is set to CC16. | `RR_RESET_AT` (CC16 lane) on the basses at 104-122 and 520-532. | Yes since c52 (c53 equals c52 note for note on the pizzicato). No reset stands at the start of the three pizzicato passages (finding 4). |
| CC7 sets a track's level against the others; CC11 shapes each instrument's dynamics; velocity is the loudness of short articulations (p.64). | Every fix below is a role row, level shape, note trim or pitch trim (track envelope). None changes CC11 or CC1. | Yes. |
| "Flute 2" is a different player and seat; no samples shared with "Flute" (p.108). The Solo Bass Clarinet and Solo Oboe are single-player patches (p.108). | A single bass clarinet and a single oboe are measured below at the level of a section or of the tuba. | The patches are right; their level is not (findings 2 and 3). |

MANUAL-GAPS still open and relevant to this lens: #12 Felt Cresc rolls, #5 expressive rows for the wind solos, #4 Mid mics on the winds. None explains a level problem found here.

## EW-TEMPLATE-PLAN sections this lens touches

Applied, no level problem traced to them: section 1 (mic layout; timpani run Close -14 / Main -6 with no Surround instead of the plan's -8 / -7 / 0, and the harp mics differ, as c53's CHANGES lists), section 3 (family EQ), section 8 basses bell at 230 Hz, section 9 sends by register and brass as narrow sources, section 6 short notes with CC11 parked.
Applied in the lanes but not in the result: section 10 "doublings share one curve": the celli, bassoon 1 and trombone 2 share one curve in bar 140 and the oboe and violins in bars 25 and 122, yet one patch's hot pitches put it 3-7 dB over its partners (findings 1 and 3).
Not yet applied (unchanged from c53's list): section 5 legato overlap and legato velocity by dynamic, section 6 two tracks per string section (the same-dynamic rows need a new base when it is), section 7 per-note lean-off, section 8 tutti entry spread and room bed, section 10 beat-position velocity outside the listed spans.

## Checks that pass (measured)

- c53's B rows hold on the fixed stems: bars 17-22, 115-116, the cor anglais answers, Oboe 1 at 496-503 and 168, the Clarinet 1 coda, timpani bar 4. I re-measured 456-463 and 494-503 and get the actor's values after the 6 dB scale offset.
- Timpani rolls: none is the loudest stem beyond an arrival (actor's table re-read against my per-quarter levels). Roll 9 and the family sums at bars 115-116 moved because of the celli cut B asked for; take c53's values as the new reference (-8.4 / -4.3; +1.5, +1.0, +1.4, +1.0, -6.4).
- Trumpets: f 29.6-33.7, ff 34.2-37.8, fff 38.0-41.9 on notes held at one printed dynamic, so the f to ff step (4.1 dB on Trumpet 1) is present; the pp entry at qn 448 reads 22.7-23.5, inside the pp range of horns and winds (13-23) and 11 dB under the Violins I line. Trumpet 1 against Violins I at the climax: 45.4-46.5 against 46.7-47.2 at 636-641 (as c52).
- Tam-tam fff (qn 484): loudest single stem for five quarters (47.7 against Violins I 42.7 at 485), 6-9 dB under the sum of the other stems, falling 12 dB in 8 quarters. Tam-tam pp at 696: 13.7 against 21.4 for the rest. Both fit the marks.
- Suspended cymbal: stroke at 636 reads 38.8 against 55.2 for the rest; in 6-20 kHz it leads for one quarter (27.3 against 25.9) and is 6 dB under by 637. The roll before it reads 8.6, 14.6, 21.1, 34.7 at 632-635 against 49-52, so only its last beat is audible. Remark only, as in c53.
- Bars 178-180: Violins I pp espr. 20.8-22.5 against 11-15 for each other stem. The lead is clear.

## Findings

### 1. The celli's held Ab3 and F3 at f and ff are as loud as the tune or louder: bars 25, 31, 40, 132, 140

Where. Violoncellos, harmony or tenor-line half notes under a tune in Violins I (with flute, oboe or trumpet): qn 97-100 (F3), 120-124 (Ab3, F3), 156-160 (Ab3), 526 (Ab3, inside the unison theme), 556-558 (Ab3 slurred into F3).

Evidence (measured). Per-note residual of the celli against their own CC11 fit, notes at CC11 85 or more: Ab3 +4.2 dB median over six notes (120 +3, 156 +4, 272 +4, 484 +3, 526 +7, 556 +6), with the -3 and -5 dB note trims at 272, 526 and 556 already in. This matches the kit's record that this pitch is hot at f and ff only.
- Bar 25: celli 40.2, 43.0, 41.1 at qn 97-99; Violins I 40.2, 39.0, 41.7; Oboe 1 41.6, 39.7, 37.1; Flute 1 28.4, 34.9, 38.7. At 98 the celli are the loudest stem by 3.3 dB and equal the whole melody group (43.0).
- Bar 31: celli 37.5, 39.6, 35.6, 39.4 at 120-123 against Violins I 40.1, 39.5, 38.1, 37.6.
- Bar 40: celli 36.3, 33.8, 38.1, 39.9 at 156-159 against Violins I 33.1, 33.0, 31.9, 33.1 and the melody group (Violins I, Flute 1, Oboe 1) 34.8, 34.9, 34.1, 37.4. The celli are the loudest stem by 3.2, 5.0 and 5.9 dB at 156, 158, 159. `note_trims.json` still holds Violoncellos 152.0 +5.0 and 156.0 +5.5 from c44; c45's body cut no longer covers it (c49 reads the same: celli 3-6 dB over Violins I).
- Bar 132: celli 45.0 on the first half of 526 against 35-36.5 on their neighbouring notes: an accent of 8.5 dB (rule 4 asks 2-4) and 6 dB over the next stem.
- Bar 140: celli 44.9 and 45.7 at 557.0 and 557.5 (39.1 at 556.5, 36.7 at 558) against Violins I 38.8 and 41.0; loudest stem by 4.5 dB and 2.5 dB over the whole melody group (42.6). The -5 dB trim at 556.0 reaches only -2.0 to -0.8 dB in `vol_db`; the F3 target starts at 557.53. c49 read 45.3 and 48.0 there, so this is old.

Fix (all in the track envelope).
- `build/note_trims.json`, Violoncellos: add "97.0": -5, "120.0": -3, "122.0": -3; change "152.0" +5.0 to +3.0, "156.0" +5.5 to 0, "526.0" -3 to -7. `NOTE_TRIM_RAMP_S["Violoncellos"]` 0.1 s for 97.0, 120.0, 122.0 (152, 156 have it).
- `build/score_config.py`: `LEVEL_SHAPES["Violoncellos"]` add `[(157.4, 0.0), (158.0, -3.0), (159.75, -3.0), (160.0, 0.0)]` and `[(556.75, 0.0), (557.0, -6.0), (558.0, -6.0), (558.25, 0.0)]`.
- `build/roles.json`, Violins I: [136.25, 160, 2, 2] to [136.25, 160, 2, 0.25], so the +2 holds through the run into bar 41 (its `vol_db` falls from 3.7 to 2.4 over 158-160 now).

After the fix (dB addition): bar 25 Violins I minus celli +5.0, +1.0, +5.6 and melody group minus celli +8.9, +5.0, +8.3; bar 31 celli 5.6, 2.9, 5.5, 1.2 dB under Violins I; bar 40 celli 30.8, 28.3, 29.6, 31.4, melody group minus celli +4.0 to +6.6; bar 132 accent 4.5 dB; bar 140 celli 38.9 and 39.7 at 557.0 and 557.5 (Violins I 38.8, 41.0; group +3.5). Master at 158-159 falls about 1 dB, which widens the step into the bar-41 sf. The 152 and 156 trims were set in c44 for the strokes' fronts, so the fronts fall with them; if lens A needs the front at 156, keep it with a shape that ends 0.3 s after the onset instead of the note trim.

### 2. Bars 117-123 (qn 464-492): the bass clarinet's pedal G2 is the loudest bass instrument and the largest source of 30-150 Hz

Where. Bass clarinet, held G2 ff under the tutti (with Bassoon 2, contrabassoon, bass trombone, tuba, basses, celli tremolo, timpani roll).

Evidence (measured). Per two quarters 464-482: Bass clarinet 38.9, 39.1, 37.0, 37.9, 37.8, 38.4, 39.6, 36.3, 37.0, 39.1; Tuba 36.5-38.1; Bassoon 2 34.0-37.3; Contrabassoon 33.0-36.0; Bass trombone 30.8-36.2; Double basses 31.7-34.6; celli 31.5-33.6. One bass clarinet is over the tuba in 8 of the 10 windows (up to +4.0 dB), 0.5-5 dB over Bassoon 2 and 1-8.5 dB over the contrabassoon, bass trombone and basses, and it is the fourth-loudest stem of the tutti. Its share of the dry sum's 30-150 Hz per bar 117-123: 34, 33, 37, 33, 25, 37, 30 % (basses 15-21 %, timpani 14-18 %, tuba 5-12 %). In the other tuttis it sits 3-7 dB under the tuba and basses (bars 140-142, 167-170). Cause in the data: `vol_db` is +6.0 to +7.9 at 464-468 and +3.3 to +7.1 after (crescendo gain held from 440-464, the build shape, and c52's +3.5 dB shape at 483.75-491.85), and its residual against its own fit is +6 to +8 on these notes. c41 and c49 read 1.9-2.7 dB higher still, so it has always been there; the tuba's -3 role (464-484) widened the gap. Rimsky-Korsakov's table (one tuba or trombone = two horns = four woodwinds at forte) puts a single low clarinet well under the tuba.

Fix. `build/roles.json`, Bass clarinet: add [464, 492, -5.0, 1.0]. Keep c52's shape at 483.75-491.85 (it holds the note level across the fff arrival).

After the fix (dB addition): 31.3-34.6, which is 0-4.5 dB under Bassoon 2 and 1-7 dB under the tuba; low-band share about 14 % in bar 117; master 30-150 Hz about -1.1 dB in bars 117-120, master K level -0.25 dB.

### 3. Oboe 1 on F5, G5 and Ab5 at ff equals the Violins I section

Where. Oboe 1, every loud note on F5-Ab5: 21 notes at CC11 100 or more (qn 97, 98, 100, 113, 118, 120, 393, 464-480, 482, 484, 488, 558, 628, 634, 640, 642, 643, 676), and the G5 at 492.

Evidence (measured). Median level of Oboe 1's ff notes by pitch: F4-Eb5 27.5-33.8, E5 33.6, F5 39.1, G5 38.2, Ab5 41.6, Bb5-C6 28.0-30.6. The patch is 8-12 dB hotter on F5-Ab5 than on the notes around them at one dynamic; residual against its fit +4.9 (F5, n 11) and +7.1 (Ab5, n 8). Against Violins I on those notes: 97 41.0 / 40.2, 98 39.5 / 39.2, 100 40.7 / 41.6, 484 43.6 / 43.4, 643 43.4 / 43.2, 676 42.3 / 43.2; median over the 21 notes -3.1 dB. Of 87 ff quarters where both play, Oboe 1 is within 3 dB of Violins I or over it in 25. At 464-480 it holds harmony notes (F5, G5) at 37.4-39.1 while Flute 1, which doubles the tune, reads 34.4-38.4. Oboe 2 on lower notes is 4-10 dB under it in the same chords. Rimsky-Korsakov (Principles p.33, as in c53's report): at forte one woodwind is about half a string department. The open item "Oboe 1 over Violins I at 494-495 (+1.8 / +2.2)" is this G5.

Fix. `build/pitch_trims.json`, Oboe 1: add "77": -2.5, "79": -2.5, "80": -4.0, with `"_all_arts_pitches": [77, 79, 80]` (the held notes are Sus rows; the existing "76" and "72" entries stay as they are) and `"_skip_onsets": [148.5, 155.0, 166.0, 313.0, 315.0, 495.5, 539.0, 542.0, 543.0]` (these pitches below f, where the oboe is not hot or was levelled by hand; 495.5 keeps c53's 496 row intact).

After the fix (dB addition): Oboe 1 minus Violins I on the 21 notes median -6.2 dB (97 -3.2, 98 -2.2, 100 -3.4, 484 -3.8, 640 -7.1, 643 -2.3, 676 -4.9); 492-495 about -0.5 dB. Check after the build: c53's row "Oboe 1 2-5 dB under Violins I at 496-503" must read as in c53, and the letter-G gap to Violins I (c22 window 3-8 dB) must hold.

### 4. Double basses: pizzicato notes 9-13 dB apart in one line; E2 weak on every articulation

Where. Pizzicato at qn 184-216 (pp), 408-432, 584-616 (pp); arco E2 at 240, 250, 310, 312, 392, 444.

Evidence (measured; RMS over the first 0.45 s of each pluck). 184-216 at one velocity (41): -53.5 -56.6 -55.7 -50.4 -47.3 -53.5 -50.5 -54.1 -47.3 -52.3 -51.5, spread 9.3 dB. 584-616: -46.8 -49.1 -42.6 -50.2 -50.5 -55.4 -48.6 -44.6 -50.3 -52.5 -47.9, spread 12.8 dB; the D2 at 592 is 4-8 dB over its neighbours and the E2 at 600 5-7 dB under. By pitch across the 33 plucks (net of `vol_db`): D2 +7.3, C2 +3.0, E2 -5.3, Db2 -3.8 against the median. Arco: E2 reads -4.1 dB against the basses' own CC11 fit (nine notes, -3 to -5 on the long ones) and -6 to -16 dB in 30-150 Hz; the track's 87.3 Hz -10 dB notch sits 0.08 octave from E2's fundamental. This is the finale's item 32; of its four pitches only E2 is still off here (F2 +1.6, Eb2 +0.1, F1 +0.7 with the trims already in `pitch_trims.json`). c50 read single plucks up to 8.6 dB differently (592: -51.2), which was the round-robin position before c52's resets; c53 equals c52.

Fix.
- `build/pitch_trims.json`, Double basses: add "40": 4 (the dict already has `_all_arts`).
- `build/score_config.py`, `RR_RESET_AT["Double basses"]`: add 184.0, 408.0, 584.0, so each pizzicato passage starts from the first take whatever is edited before it.
- `build/note_trims.json`, Double basses (step shape, as for every plucked note): "592.0": -6, "608.0": -3, "198.0": -3, "212.0": -3, "188.0": +3, "192.0": +2.5, "208.0": +2.

After the fix (dB addition, valid while the take order stays as in c53): spread 3.3 dB at 184-216 and 5.7 dB at 584-616; arco E2 within 1 dB of the fit. The new resets may change which take plays; re-measure the 22 plucks on the render and adjust the seven trims on the stems if they moved.

### 5. Bar 134 (qn 532-536): the timpani's eight ff strokes are level with the theme's instruments and carry most of the low band (low priority)

Where. Timpani, G2 eighths under the recapitulation's low unison theme (celli, clarinets, bassoons, trombones).

Evidence (measured). Timpani 39.3, 37.7, 38.0, 37.2 against celli 35.0, 39.4, 40.0, 38.0, Bassoon 1 41.7, 35.7, 36.6, 35.7, Clarinet 1 32.5-36.7, Trombone 1 29.5-32.9, Violins I 33.4-35.8; second-loudest stem of the bar, 4.1-4.8 dB under the theme group's sum. In 30-150 Hz it reads 34.3-36.0 against the master's 35.1-37.1 and the basses' 27.6-29.5. Each stroke has a +5.8 to +8.8 dB attack shape in `vol_db`. In bar 82 the same figure sits 2-6 dB under the Violins I tune. Whether this covers the theme for a listener is inferred, not measured.

Fix. `LEVEL_SHAPES["Timpani"]` add `[(531.9, 0.0), (532.0, -2.5), (535.9, -2.5), (536.0, 0.0)]`. After (dB addition): 34.7-36.8, 6.6-7.3 dB under the theme group.

## Open items from c53, decided through this lens

- Oboe 1's front at qn 160, 3 dB low: sampler variation (coordinator fact 3), not a state fault. The nine Oboe 1 notes before it (154-159.75) are identical to 0.1 dB in c52 and the first c53 render per half quarter; only the 160 note differs (first 0.1 s -38.2 in c52, -37.1 as rendered with the +3 bump). No action.
- CC1 floor of 64 on held Oboe 1/2 and Flute 2 notes: not needed for level. With c53's shapes Oboe 1 is 2.9-4.9 dB under its unison partner at 496-503 and within the clarinets' range at 168. Reject; it would also change the non-vibrato colour the pp marks ask for.
- Oboe 1 over Violins I at 494-495: finding 3.
- Family sums at bars 115-116 and timpani roll 9: new reference values, as above.
- Double basses 704-712 against c50: c53 equals c52 per two quarters (7.8, 6.1, 6.4, 9.9, 7.9); c50 read 3.5-10.3 and c49 7.2-13.4. The basses are 3-7 dB under the violas there, which fits the pp close; no action from this lens.
- Finale item 18 on the basses, the stops at bars 71 and 141, the brass tail and the trumpet release: not measured here (lenses A and C).

## Check table for the c54 render

| Row | c53 | Target |
|---|---|---|
| Celli minus Violins I, qn 97-99 | 0.0, +4.0, -0.6 | celli at least 1 dB under in each quarter |
| Celli minus Violins I, qn 156-159 | +3.2, +0.8, +6.2, +6.8 | melody group at least 4 dB over the celli |
| Celli accent at 526 over its neighbours | 8.5 dB | 3-5 dB |
| Celli minus Violins I, 557.0 and 557.5 | +6.1, +4.7 | at most +1 |
| Bass clarinet minus tuba, 464-484 | -1.8 to +4.0 | bass clarinet 1-7 dB under |
| Bass clarinet share of 30-150 Hz, bars 117-123 | 25-37 % | under 20 % |
| Oboe 1 minus Violins I on ff F5-Ab5 notes (median of 21) | -3.1 | -5 to -7; none over -2 |
| Basses pizzicato spread, 184-216 / 584-616 | 9.3 / 12.8 dB | 6 dB or less |
| Basses arco E2 against the track's fit | -4.1 | within 2 dB |
| Timpani under the theme group, 532-535 | 4.1-4.8 | 6-8 |
| All rows of c53's check table | as in CHANGES | unchanged within 1 dB |

## Do not touch

Keep: every c53 B row (Violins I and celli roles to 88 / 84 with the celli note trims 64-80, the celli shape at 456-464, the Oboe 1 shapes at 496-503 and the 168 trims, the cor anglais third-answer role, the bass clarinet role at 699.5-708, the timpani bar-4 shape); the family balance at the tuttis with the brass under the strings; all timpani roll levels and the soft-roll shelf; the trumpet dyn trims and the Trumpet 1 level in the theme doubling at 629-644; tam-tam and cymbal gains; the brass widths 0.65 / 0.75 with their make-up; the Violins I and II -3.5 roles and the low-unison +2 roles at 520-536 (the theme group reads about 1 dB under the sum of everything else there, with each other voice at least 5 dB under it); c52's bass clarinet shape at 483.75-491.85; the existing basses pitch trims; CC11 and CC1 lanes (no fix here changes them).

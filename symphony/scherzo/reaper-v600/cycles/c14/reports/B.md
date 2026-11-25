# Cycle 14, critic B: balance and levels (render under review: c13, second render)

Method. Levels are K-weighted mean-square levels in dB, both channels summed, in 10 ms steps of the dry stems, the four return stems and the master of `cycles/c13/render/`, placed on the score with the tempo map of `cycles/c13/build_render/parts.json` (qn 1128 = 277.87 s). "Peak" is the highest 30 ms mean inside a note's window. Spectra are 1/3-octave band powers of the mono sum (8192-point Hann frames), given as a share of total energy, the method of `symphony/render/tools/rtk.py` that produced the stored reference figures. "140-355 Hz" is the sum of the 158, 198, 250 and 315 Hz bands, "70-112 Hz" the sum of the 79 and 99 Hz bands. EQ responses are computed from the band tables in `build/mix.json` with standard peaking-filter formulas (ReaEQ's exact curves may differ by a few tenths). Simulations rescale a stem's spectrum by the EQ change and add the difference to the master's spectrum (cross terms ignored). c12 stems (own tempo map) are the comparison where named. "Measured" marks numbers from the audio or the build data, "inferred" marks judgements of cause or audibility.

References are second-hand: the two Brahms slow movements exist only as stored third-octave tables (`symphony/render/critics/c04/ref_brahms1_ii_musopen/metrics.json`, `ref_brahms4_ii_musopen/metrics.json`), the figures Movement II's c53 critic C used (140-355 Hz share -9.1 and -8.5 dB, 70-112 Hz -10.3 and -9.5 dB). I also measured the local Dvořák 9/i file (`symphony/render/assets/refs/dvorak9_i_columbia.mp3`, lossy, an old recording): 140-355 Hz -6.1 dB, 70-112 Hz -18.2 dB. The two references disagree by 2.7 dB in the low mids and 8 dB in the bass, and neither is a scherzo in E minor. No recording was downloaded.

## Manual notes (group B2: PDF pages 194-200 of the May 2021 HO manual, read in full as text; MANUAL-GAPS.md)

| What the page says | Where it applies | Does the render follow it |
|---|---|---|
| p. 194, 196: the Mix page has one master channel per instrument and one sub-mixer channel per microphone position, each with volume, pan and a load button. | `build/mix.json` `mic_db` and `pan_by_mic` per group and track (strings Close -4.5 / -6, Main 0; winds Close 0, Main -3.4 to -20.6; horns Close -6.3, Main 0; DIV tracks Close only). | Yes. Oboe 1 and 2 have Main at -20.6 dB, which is Close only in effect; the c13 test of their Main mics is still open (CHANGES C #1b). The Violin I solo and Violas div patches have no Main channel, so their room comes only from the return (see "Soft ends" below). |
| p. 196, 198: an FX bus per instrument; a sub-mixer channel sends to it through an Effects Send with a level slider and a Post switch; "for reverb, post fader is typically used" so the send follows the fader. | The hall. `opus_reverb_off` is true; the four REAPER returns take post-fader sends (`send_profile` "ew"). | Yes, in REAPER instead of Opus. Consequence for my lens (inferred from the routing): every `gain_db`, role and trim change moves a track's hall send by the same amount. The solo's +2.5 dB make-up gain after Stereo Double in c13 raised its send with it. |
| p. 195, 196: Store Mix / Store FX Chain save channel settings inside Opus. | None: the mix lives in `mix.json` and is rebuilt. | Not used, correctly (a stored Opus mix would be lost on a track rebuild). |
| p. 197-200: insert effects per channel; the EQ group is Bass Comp (boost around 32-256 Hz), a 3-band Channel Equalizer and a 6-band Equalizer, described as corrective ("reducing problematic frequencies") or enhancing. | Track EQ. The mockup uses ReaEQ after Opus: per-track `eq`, `mute_eq`, `loud_eq`, `side_shelf`, a family EQ per track and a master EQ. No Opus EQ is loaded. | An Opus EQ would duplicate ReaEQ, so none is needed. The corrective cuts in use were fitted to single notes of Movement I and sit on other notes here: the Double basses pass five EQ stages that sum to about -9.4 dB at 82.4 Hz and -10.3 dB at 61.7 Hz in the tuttis (finding 2). |
| MANUAL-GAPS: Bass Comp and the Opus EQs are unused. | Low end. | Not needed: finding 2 gets the bass back by removing cuts, not by adding a boost. |

## The checks asked for

**"A bit mushy": the master against Movement II's reference figures (measured).**

| passage | 140-355 Hz share | re Brahms pair (-8.8) | 70-112 Hz share | re Brahms pair (-9.9) | who supplies 140-355 Hz (share of all stems) |
|---|---|---|---|---|---|
| whole movement | -7.6 | +1.2 | -15.2 | -5.3 | Violoncellos 23 %, Violas 11, Clarinet 2 10, Double basses 10, Timpani 8 |
| tutti 105-120 | -7.1 | +1.7 | -16.4 | -6.5 | Violoncellos 23 %, Horn 3 15, Clarinet 2 11, Violas 10 |
| tutti 305-320 | -7.6 | +1.2 | -16.8 | -6.9 | Violoncellos 30 %, Clarinet 2 14, Violas 13 |
| coda 329-339 | -9.3 | -0.5 | -20.7 | -10.8 | Double basses 22 %, Timpani 15, Violoncellos 13 |
| fugato 57-72 | -6.8 | +2.0 | -11.2 | -1.3 | Violoncellos 48 %, Violas 16 |
| F major 73-88 | **-2.9** | **+5.9** | -14.5 | -4.6 | Harp 56 %, Horn 4 14, Horn 3 9 |
| trio 153-168 | -7.5 | +1.3 | -17.6 | -7.7 | Harp 69 %, Horn 4 22 |
| trio 169-184 | **-5.0** | **+3.8** | -14.9 | -5.0 | Violoncellos 73 %, Bassoon 2 11 |
| trio 185-208 | -5.2 / -5.0 | +3.6 / +3.8 | -15.3 / -10.8 | | Clarinet 2 38 % and 25 %, Violoncellos 29 %, Violas 26 % |
| trio ff 209-224 | -9.1 | -0.3 | -12.1 | -2.2 | Violoncellos 31 % |
| codetta 225-240 | -5.1 | +3.7 | -15.5 | -5.6 | Clarinet 2 26 %, Bassoon 1 24, Harp 19 |
| reprise 253-272 | -7.0 | +1.8 | -16.0 | -6.1 | Violoncellos 45 %, Clarinet 2 15 |
| Meno mosso 341-363 | -5.7 | +3.1 | -16.4 | -6.5 | Harp 31 %, Violas 20, Horn 3 18 |

Reading. Movement II's excess (3.2-3.7 dB over the Brahms pair for the whole movement, share -5.3 dB) is not in the scherzo as a whole (-7.6 dB, +1.2) and not in its tuttis (+1.2 to +1.7; they are 1.0-1.5 dB leaner than the Dvořák file). It is in the soft passages: the F major episode, the trio from bar 169 to 208, the codetta and the Meno mosso read 3.1-5.9 dB over the Brahms pair, and the softest 40 % of frames read -5.5 dB against -7.9 for the loudest 20 %. The bass octave is 5-7 dB under the Brahms pair nearly everywhere, as in Movement II, and 3 dB over the Dvořák file. The treble is not short: the 1.8-5.6 kHz share is -8.6 dB (Brahms 2-6 kHz -12.4 / -11.8, Dvořák -10.5), so nothing here asks for a treble boost. Findings 2, 3 and 4 give the per-stem changes.

**Stale tracks (measured).** No stale legato state in the c13 audio. Joins by `pcx.scan` on the stems, c12 then c13: Horn 4 n 16, median +1 ms / +1 ms, front minus body +0.7 / +0.6 dB; Violins I n 118 / 100, +16 / +18 ms, -0.8 / -0.6 dB; Violoncellos n 200 / 202, +9 / +13 ms, -0.4 / -0.6 dB; unflagged controls Violins II +1 / +2 ms, Violas +3 / +3 ms, Horn 2 +40 ms in both. Stale state would read about -45 ms with fronts 3-5 dB loud.

**The two soft ends over 0.30 s (measured).** The measure is the time from the highest 10 ms frame of the last 0.3 s to 10 dB under it, on stem plus R Strings.
- Violin I solo at 1066.8 (0.33 s). The dry stem alone reads 0.30 s and its own release falls 30 dB in 0.15 s after the note-off. The reference frame is a bump 0.22 s before the note end, 7 dB over the frames after it. What holds the sum up is the return: R Strings sits 10-13 dB under that peak for more than 0.3 s after the release, so the -10 dB crossing lands on the hall. R Strings against the solo's dry stem in the last second is -6.8 dB; the sections read -8.8 dB (Violins I, 1128), -11.2 dB (Violins I, 23) and -13.7 dB (Violins II, 444.5). Cure: `mix.json` "Violin I solo" `send_offset_db` R Strings 3.6 to 2.4. That drops the hall under the release by about 1 dB and puts the crossing back on the release (about 0.27 s, inferred). The solo is then still the wettest string track by 0.8 dB, which it needs as a Close-only patch.
- Violins II at 444.5 (0.31 s). Here the dry stem alone reads 0.29 s: a 5 dB bump 0.05 s before the score end, a body held for 0.25 s, then the release (350 ms cap for pp and p rows). The hall adds 0.02 s. Cure: a 250 ms release cap on that one note (a third entry in Violins II's `sus_release_cap_ms` limited to the note, or `NOTE_END_AT` 0.03 qn earlier). The 0.01 s excess is inside the measure's own scatter (the reference frame moves with a single 10 ms bump), so this one is low priority.

**The lens text names trumpet quarters in bars 301-320.** The score has the trumpets tacet there (`sections/dC.ily`, c428) and the trombones and tuba tacet from 289 to 331; the silent stems are correct.

## Findings, ranked by listener impact

### 1. Theme A in Violins I: the unaccented staccato that ends the slur is the loudest note of the phrase, and the accented half note before it fades out

Where: all nine soft statements of the theme's second bar: half notes at qn 39, 51, 69, 75, 285, 759, 771, 789, 795 (bars 14, 18, 24, 26, 96, 254, 258, 264, 266), the slurred eighth pairs after them (41, 53, 71, 77, 287, 761, 773, 791, 797) and the landing staccato quarters at 42, 54, 72, 78, 288, 762, 774, 792, 798. Violins I carry the master alone here (master within 1 dB of the stem).

Measured.
- Violins I per quarter-beat (57 ms) from qn 38.75: -39, -31, -29, -27, -26 (half note, printed accent), -35, -37, -41, -38 (its second beat), -35, -36, -35, -34 (the pair), **-28** (landing staccato), -33, -42. From 50.75: -43, -33, -31, -32, -35, -37, -43, **-52, -51**, -40, -42, -42, -40, **-26**, -29, -37. From 770.75: -42, -32, -29, -30, -34, -35, -41, -49, -48, -41, -41, -42, -41, -28, -32, -40.
- Landing note (first half beat) against the pair before it and the next two staccato quarters, c13: 42: -29.8 against -35 and -39.1 / -38.1; 54: -27.5 against -41 and -38.0 / -35.2; 72: -29.1 (-34, -38.2); 78: -29.8 (-36.7, -38.2); 288: -29.6 (-37.8); 762: -28.6 (-34.6, -33.9); 774: -29.3 (-41.3, -36.4); 792: -30.4 (-33, -37.9); 798: -30.0 (-36.6, -37.8). The step from the pair into the landing note is +3.9 to +14.0 dB (median +6.3); the landing note is 4-10 dB over the staccato quarters that follow at the same printed dynamic.
- Same measure on c12: landing notes -28.7 to -33.8, step from the pair -2.3 to +6.3 dB (median +0.8). c13 raised the landing notes by 0.0-4.5 dB (median 3.1) and lowered the pairs at 53 and 773 by 6-7 dB (c13's level steps -11 / -13 there). The half notes read the same in both cycles (means within 0.2 dB), so the fade inside the half note is older than c13.
- Data: the lane (`parts.json` Violins I `vol_db`) steps from -17.6 at 53.93 to -3.1 at 54.02 and returns to -8.2 by 54.35 (at 42: -12.2, -2.5, -7.3): the landing note carries a front 4.8-5.2 dB over the level of the staccato notes after it. `beat_db_notes` accounts for +1.5 of that; I did not identify the rule that writes the rest. The half notes play "Sus Marc LITE" at CC11 43-52 with a flat lane (-13.0 to -14.5 over 51.1-52.5), so their 9-21 dB fall is the row's own decay (the caveat in ONE_TIME_c14 item 4).

Judgement (inferred). The printed shape is an accent on the half note, a slurred pair leaving it, and a light staccato to end the slur. The render gives a half note that is a one-beat bump, a soft pair, and a landing note as loud as the accent's peak. This happens nine times in the movement's main theme with nothing covering it.

Fix (`build/score_config.py`, `LEVEL_SHAPES["Violins I"]`; verify on a one-track range render of bars 13-28 as in `cycles/c13/rangetest/`):
- Landing notes: one step per onset q over [(q - 0.21, 0), (q - 0.19, d), (q + 0.40, d), (q + 0.46, 0)] (the note-on is 0.198 qn early) with d = -3.5 (42), -5.5 (54), -4 (72), -3.5 (78), -4 (288), -4 (762), -4 (774), -2.5 (792), -3 (798). If the actor finds the rule that writes the 5 dB front, cancel it at these nine onsets instead and keep 1.5 dB of the listed values. Target: landing note 0-2 dB over the statement's other staccato quarters and no more than 3 dB over the pair.
- Pairs at 53 / 53.5 and 773 / 773.5: raise c13's steps by 5 dB (53: -11 / -13 to -6 / -8; the same change at 773). Target -35 to -37, as the other seven pairs.
- Half notes: hold the second beat. A level ramp over [q + 0.9, q + 2.0] from 0 to +5 dB at 39, 69, 75, 759, 789, 795 and to +9 dB at 51, 285, 771, falling back before the pair's own step begins; or, better if a range test shows it works on this row, a CC1 rise of about 15 over the second beat (manual p. 151: on the LITE string rows CC1 carries dynamics). Target: the second beat no more than 8 dB under the first beat's peak (now 9-15 dB at 39, 9-17 dB at 759, up to 21 dB at 51 and 20 dB at 771).
Critic A's findings on the timing and row of these notes take precedence where they conflict; these are level targets.

### 2. The bass weight sits at 125-200 Hz instead of 60-110 Hz: Movement I's note cuts on the basses and tuba land on this movement's tonic and dominant, and the celli carry a 5 dB boost above them

Where: every passage with Double basses; most audible in the tuttis 105-120 and 305-320, the coda 329-339, the reprise 253-272, the trio 153-184 and the Meno mosso. `build/mix.json`: Double basses, Tuba, Violoncellos.

Measured.
- Share of 70-112 Hz in the master: tuttis -16.4 and -16.8 dB, reprise -16.0, trio 153-168 -17.6, Meno mosso -16.4, whole -15.2 (Brahms pair -10.3 / -9.5; Movement II was 5-7 dB under them as well).
- Double basses, ff arco notes of bars 105-120, plain level of the stem per pitch: E1 -34.9 (7 notes), B1 -35.3 (4 notes), A1 -31.1 (4), G1 -31.1, G sharp 1 -31.2. The tonic and the dominant are 3.6-4.2 dB under the passing notes of the same line at the same controllers. On E1 the second harmonic (82.4 Hz) is 6.3 dB under the third (123.6 Hz); on A1 the second harmonic (110 Hz) is 17 dB over the third.
- Computed response of the Double basses' own chain: track `eq` bell 87.3 Hz -10 dB (0.15 oct, fitted to an F2 in Movement I) and `mute_eq` bells 61.7 Hz -6 and 73.4 Hz -5 (Movement I's B1 and D2) give -6.8 dB at 82.4 Hz (E2 and the second harmonic of E1), -7.3 dB at 61.7 Hz (B1) and -7.2 dB at 73.4 Hz. With the `loud_eq` (98 Hz -4, 160 Hz +6), the family EQ and the master EQ the tutti total is about -9.4 dB at 82.4 Hz, -10.3 dB at 61.7 Hz and +2.0 dB at 165 Hz. Tuba: bell 84 Hz -5 gives -4.8 dB at 82.4 Hz; it plays E1 and B1 only.
- Violoncellos track `eq` (bells 170 Hz +3 and 125 Hz +3): +5.2 dB at 123-147 Hz, +4.8 at 165, +3.9 at 196, and the `loud_eq` adds 1.5-2 dB more in the tuttis. The celli supply 73 % of the master's 140-355 Hz in bars 169-184, 48 % in the fugato, 45 % in the reprise and 23-30 % in the tuttis.
- `build/pitch_trims.json` already lifts the basses' pizzicato E1 by 2 dB and E2 by 1 dB (c01 residuals), which is the pipeline pushing against these cuts.

Simulated (87.3 and 61.7 Hz bells removed on the basses, 73.4 Hz kept; tuba bell removed; basses' `loud_eq` 160 Hz +6 to +3 and its 98 Hz cut removed; both cello bells removed):

| passage | 70-112 Hz share now / after | 140-355 Hz share now / after | master level change |
|---|---|---|---|
| tutti 105-120 | -16.3 / -13.7 | -7.1 / -7.7 | 0.0 dB |
| tutti 305-320 | -16.9 / -13.9 | -7.6 / -8.4 | 0.0 |
| fugato 57-72 | -11.4 / -10.8 | -6.8 / -7.9 | -0.2 |
| trio 169-184 | -15.0 / -11.2 | -5.1 / -6.7 | -0.4 |
| reprise 253-272 | -16.1 / -13.4 | -7.0 / -8.0 | -0.1 |
| Meno mosso 341-363 | -16.5 / -12.9 | -5.7 / -6.6 (with finding 3's harp bell) | -0.1 |

Bass notes after the change (simulated on each note's spectrum): ff arco E1 +1.4 dB, B1 +1.9 dB, A1 +0.8, G1 +1.6, so the tonic and dominant close about 1 dB of the gap to A1 and the line as a whole gains about 1.5 dB. `build/note_trims.json` also carries +3 dB on eleven arco E2 notes (c12), a second place where the pipeline pushes against the cut; pizzicato B1 +3.7 dB, E2 +3.5, E1 +1.8, C sharp 2 +2.7 (it is already the hottest pizzicato pitch, +5.1 dB over the track's median, which is why the 73.4 Hz cut stays).

Judgement (inferred). The low strings sound thick but not deep: the fundamentals and octave harmonics of E and B are cut by 7-10 dB while the band above them is raised by 2-7 dB. This is the tutti part of "mushy" that level changes can reach. The evidence for more 70-112 Hz rests on the Brahms pair and on the note-to-note figures above; the Dvořák file has less bass than the mockup, so the acceptance figures below stop well short of the Brahms level.

Fix (`build/mix.json`, `--mix-only`):
- "Double basses": remove the `eq` bell2 at 87.3 Hz; in `mute_eq.bands` remove the 61.7 Hz bell and keep the 73.4 Hz one; in `loud_eq.bands` change 160 Hz +6 to +3 and remove the 98 Hz -4 band.
- "Tuba": remove the `eq` bell2 at 84 Hz (keep the 70 Hz low shelf).
- "Violoncellos": remove both `eq` bells (170 Hz +3, 125 Hz +3); `gain_db` 0.54 to 1.0 (the stem loses 0.3-0.6 dB of level); keep its `loud_eq` 150 Hz +2 and the side shelves.
- `build/pitch_trims.json` "Double basses": "28" +2.0 to 0 and "40" +1.0 to -1.0, then re-measure the pizzicato residuals by pitch on the new render (c01's method) before any further trim.
Acceptance: 70-112 Hz share at least -14.5 dB in both tuttis; the gap from ff arco E1 and B1 to A1 and G1 in bars 105-120 at least 1 dB smaller than now (3.6-4.2 dB); the c12 arco E2 note trims re-measured and reduced by what the EQ now gives; 140-355 Hz share at most -6.3 dB in bars 169-184; celli K level in bars 169-176 within 0.5 dB of c13 (-36.3); pizzicato C sharp 2 no more than 3 dB over B1 and E2; basses' K level in bars 13-28 still 10 dB or more under Violins I (now 12-17). If Dan hears boom, restore the 61.7 Hz bell at -3 dB first.

### 3. F major episode, bars 73-80: the harp's espressivo melody is under its own left hand, and the passage is the most low-mid-heavy and the dullest of the movement

Where: bars 73-80 (qn 216-240), Harp (right hand melody A5, F5, C6 ...; left hand F2 with the chord C3-F3-A3), over Horns 3-4 and the bass clarinet. Also the harp's share in bars 153-168 and 341-348.

Measured. Master, bars 73-88: 140-355 Hz share -2.9 dB (5.9 dB over the Brahms pair, 3.2 over the Dvořák file), 1.8-5.6 kHz share -16.9 dB (movement -8.6). The harp supplies 56 % of the 140-355 Hz band. Harp stem, bars 73-80, band powers: 158 Hz 30 dB and 198 Hz 27 dB (the left-hand chord) against 630 Hz 20, 794 Hz 23 and 1000 Hz 14 (the melody's fundamentals): the accompaniment register is 6.7 dB over the melody register inside the one stem. Data: `VEL_CAP_SPANS["Harp"]` caps 216-240 at velocity 56; the left hand plays at 56 and the melody notes at 52-65 (`VEL_SET`, c12), so the cap put both hands on one layer; `roles.json` then takes 3 dB off the whole track, melody included. The family EQ already cuts 304 Hz by 8.3 dB and 1270 Hz by 8.6 dB, and the second cut reaches the melody (-2.3 dB at A5, -4.7 dB at C6, computed), while the first takes 3.6-5.7 dB off the left-hand chord's F3 and A3.

Judgement (inferred). A harpist brings out the top line of an espressivo passage and plays the left hand under it. Here the chord at 130-220 Hz is the loudest thing in the passage for eight bars.

Fix.
- `build/score_config.py`: `VEL_SET["Harp"]` for every left-hand note (pitch 57 and lower) at qn 216-240: 56 to 46. Keep the melody's c12 values.
- `build/roles.json` "Harp": `[216, 240, -3]` to `[216, 240, -1.5]`.
- `build/mix.json` "Harp" `eq`: add `{"band": "bell", "hz": 200, "db": -4, "bw_oct": 1.2}` (Movement II's c53 change). Simulated on this render: 140-355 Hz share bars 73-88 -2.9 to -3.8, bars 153-168 -7.6 to -9.3, Meno mosso -5.7 to -6.3; master level -0.9 dB in bars 73-88 and under 0.3 dB elsewhere.
Target: harp 158 + 198 Hz bands no more than 2 dB over its 630-1000 Hz bands in bars 73-80; passage share -5 dB or lower; harp K level in bars 73-80 within 1.5 dB of c13 (-35.0), so it still leads Horn 4 and the bass clarinet by 5 dB or more; trio chords (bars 153-167) still 6-10 dB under Clarinet 1 (now 5-12).

### 4. Clarinet 2's soft E4 and D sharp 4 play 9-13 dB over its other soft notes: a held pp note covers the bassoon's theme in bars 269-270 and bumps the wind chorale at bar 134

Where: Clarinet 2, held notes on E4 (16 soft ones) and D sharp 4: bars 29-34 (qn 84-102), 133-136 (396-408), 269-271 (804-813), 321-323 (960-969). Clarinet 1's G4 beside it.

Measured.
- Clarinet 2, notes of 1.5 qn or longer, level with the lane removed, by pitch at CC1 40 or lower: E4 -39.7 (n 16), D sharp 4 -39.0 (n 4), B3 -48.9 (n 4), G3 -51.6, G4 -52.9, B4 -51.3. At CC1 41-60: E4 -36.1 (n 9); over 60: -36.8. On this pitch pp and mf are 3.6 dB apart. Clarinet 1 at CC1 40 or lower: E4 and F sharp 4 -39.6, G4 -44.7 (n 5), G sharp 4 -43.1, B4 -45.0 (n 9).
- Bars 269-270: Clarinet 2's held E4 (pp, CC11 34, CC1 28, lane 0) -39.7; Bassoon 1, which has the theme head, -43.6, -48.0, -46.3, -46.5 on its four notes (bar mean -45.3); Clarinet 1's G4 on the same controller values -48.2. The accompaniment note is the loudest stem of both bars, 5.6 dB over the theme.
- Bars 29 and 33: Clarinet 2 -43.7 with its -4 dB role row, against Flute 1 -39.9 / -43.4 and Oboe 1 -42.1 / -42.3 per bar; Clarinet 1's G4 -52.3 in bar 29 (8.4 dB under its partner).
- Bars 133-136, four tenuto chords, all printed p: Clarinet 2 -39.6, **-33.4**, -40.9, -47.0 against the top voice (Clarinet 1) -36.3, -37.7, -37.9, -47.3. The second chord's E4 (CC1 51) is 6 dB over the first (CC1 39) and 4.3 dB over the top voice.
- Bar 323 (decrescendo, CC1 24): Clarinet 2 -37.0 against Clarinet 1 -39.5.
- Clarinet 2 supplies 22-38 % of the master's 140-355 Hz in bars 121-136, 185-208 and the codetta.

Cause (inferred): the patch's soft layer is recorded much stronger on E4 / D sharp 4 than on the throat notes, and Clarinet 2's soft trims (`soft_trim_db` p +7.1, mp +4.3, against Clarinet 1's +5.0 and +2.2) add to it. A plain pitch trim would also lower the mf and f notes, which are in line.

Fix (`build/roles.json`):
- "Clarinet 2": `[84, 108, -4]` to `[84, 108, -6]`; add `[804, 813, -6]`, `[399, 402, -5]`, `[960, 969, -2.5]`.
- "Clarinet 1": add `[84, 89.9, 4]` and `[804, 809.9, 4]` (the soft G4).
Targets: bars 269-270 Clarinet 2 at -45 to -46, under Bassoon 1's first note and level with its bar mean; bar 134 within 1 dB of bar 133 and under Clarinet 1; bars 29 and 33 Clarinet 2 2 dB or more under Flute 1 and Oboe 1; Clarinet 1's G4 within 4 dB of Clarinet 2's E4 in bars 29 and 269.
Generic form, if the actor has time (inferred to be cleaner): a `"_max_cc1": 40` key in `PITCH_TRIMS` (`tools/score_to_parts.py`) so "Clarinet 2": {"64": -6, "63": -5} and "Clarinet 1": {"67": +3} apply to the soft layer only; then the role rows above are not needed.

### 5. Flute 1's theme-head eighths are 6-12 dB under its quarters, so the flute and oboe unison of the counterstatement changes colour inside the head

Where: Flute 1, theme heads on "Stac DblTng RRx9": bars 29 and 33 (qn 84-86, 96-98; with Oboe 1 in unison, p leggiero), 37, 41, 43, and the ff tutti heads at 105-119 and 305-317 (with Flute 2 in unison).

Measured (30 ms peaks: first quarter, eighth, eighth, last quarter).
- Bar 29: Flute 1 -36.8, -47.2, -49.9, -39.1; Oboe 1 -45.0, -42.7, -44.4, -43.6. Bar 33: Flute 1 -37.5, -49.4, -49.7, -39.9; Oboe 1 -44.4, -40.6, -41.6, -44.0. The flute leads the quarters by 5-8 dB and trails the oboe on the eighths by 4-9 dB; the sum of the two falls 5-7 dB from the quarters to the eighths. Clarinet 2's held note (-43.7, finding 4) is over the flute's eighths.
- Over 22 heads the flute's eighths are 5.8 and 5.7 dB under the first quarter (median; worst -11.9). Oboe 1: -2.0 and +0.1 (25 heads). Violins I: -3.9 and -3.0 (48 heads), Violins II -2.7 / -1.8, Violas -1.8 / -0.3.
- By pitch at one velocity on the row: velocity 64, E5 -36.8 to -39.9 against B4 -47.2 to -49.9; velocity 96, A5 -30.5 to -31.1 against D5 -37.9 to -42.2; velocity 112, E6 -15.9 to -23.2 against B5 -26.3 to -27.8. The head always drops a fourth or fifth for the eighths, and on this row the lower pitch is 6-11 dB weaker.
- Flute 1's first tutti note (E6, bar 105) peaks at -15.9, level with each violin section's (-16.6, -16.9), and the same note spreads from -15.9 to -23.2 over eight statements at one velocity.

Judgement (inferred). In the soft counterstatement the listener hears flute quarters and oboe eighths, and the repeated eighths (Dan's S1) are the weakest notes of the bar. In the tuttis the effect is covered by the strings.

Fix. `build/pitch_trims.json`: add "Flute 1": {"71": 6, "74": 5, "83": 3, "_arts": ["Stac DblTng RRx9"]} (staccato row only; trims on short rows are steps). Then in `build/roles.json` "Flute 1" add `[84, 84.6, -2]` and `[96, 96.6, -2]` so the first quarter sits nearer the oboe. Targets: bars 29 and 33 flute eighths 3-5 dB under its quarters and within 3 dB of the oboe's; flute plus oboe sum falling no more than 3 dB into the eighths. Leave Flute 2 (its `pitch_trims` table is `_all_arts`); check after the render whether its B5 eighths in the tutti need the same.

### 6. Violin I solo, bars 349-356: more hall than any string section after c13's make-up gain (low impact)

Where: bars 349-356 (qn 1044-1068), Violin I solo; `mix.json` "Violin I solo".

Measured. R Strings against the solo's dry stem over the last second of the passage: -6.8 dB; the full sections end their soft notes at -8.8 to -13.7 dB (above). The solo's soft end reads 0.33 s because the hall, not the release, holds the level 10-13 dB under the peak for 0.3 s. Balance in the passage is as c13 left it and is right: solo -31 to -43 per bar, Flute 1 7-9 dB under it, Violins II 8-13 dB under, celli -43 to -46.

Fix. `send_offset_db` R Strings 3.6 to 2.4 (as in "The checks asked for"); no change to `gain_db`, the roles at 1044-1068 or the Stereo Double. If c14 tests spread 0.6, re-measure the level loss and put the make-up in `gain_db` with the opposite amount in `send_offset_db`, since the send is post-fader (manual p. 198).

## Measured and in balance (no change asked)

- c13's balance changes hold: timpani solo bars 9-12 master -42.2, -45.7, -40.7, -43.1 (between the ppp opening at -41.4 / -39.8 and the p theme at -36.1); pickups at 155.5, 383.5 and 851.5 are 6.9, 4.3 and 4.2 dB under their downbeats in the master's peaks; trumpets 7-9 dB under Violins I on the odd bars of 105-119 and 8.5-10 dB under at the summit.
- Tuttis 105-119 and 305-319: Violins I -22.3 / -22.2, Violins II -24.6 / -23.1, the two flutes -26.9 and -26.7 (their sum 1.5 dB under Violins I, which fits Rimsky-Korsakov's forte equivalence of two flutes to one violin section), Clarinet 2 with the low octave -28.8, Horn 3 -28.7 / -31.7, timpani -33.4, Double basses -33.0.
- Summit, bars 336-338: Violins I -16.5, Violins II -19.5, Violas -21.2, woodwinds -24.3 to -26.9 each, trumpets -25.0 / -26.6, timpani -29.0; master -10.2 to -10.5 per bar, the loudest bars of the movement (bar 300 -12.5, bar 72 -14.2).
- Trio: Clarinet 1 -31 to -39 over the harp -41 to -55 and Horn 4 -46 to -51 (bars 153-167); celli -33 to -39 over Violins II con sord. -43 to -45 (169-175); Violins I 0-6 dB over the celli (177-182); Oboe 1 -35 to -40 over the harp -46 to -47 (185-188); Violins I -23 to -32 and Violins II -27 to -36 over everything else at 209-223.
- Closing bars: Horn 1's G sharp -41.2 (bar 368) falling to -48.6 (376) with its printed diminuendo to ppp; Violins I flat at -43 to -45. On plain RMS the horn ends 1.6 dB under the violins.
- The two sub. p: bar 121 -31.3 after -15.6 / -19.7; bar 277 -34.5 after -23.9 / -28.9.

## Do not touch

Keep: the four returns, their faders, EQ and IR envelopes, and the c13 wind send offset and return pans; the hall's 180 Hz high-pass (the low-mid excess is in the dry stems: the returns supply at most 5 % of the 140-355 Hz band in any passage); the family EQs and the master EQ; the Double basses' 73.4 Hz cut, its side low shelf and the celli's `loud_eq`; the c12 / c13 brass gains and the brass rows at 994-995.5; the timpani `[23.5, 35.5, 7]` row, first-stroke steps and roll trims; the c13 hemiola steps on Violins I (300-312, 900-912) and the pickup rows at 155.5, 383.5, 851.5; Oboe 1's rows at 147.8-155.4, 386.8-393 and 854.8-861; the solo, Flute 1, Violins II and Violas div rows at 1044-1068 and the Stereo Double; Horn 1's closing contour and `[1100.25, 1128, 6]`; the trio's harp velocity caps (42) and Clarinet 1's trims at 456-504; the "Sus Marc LITE" row choice for the theme's half notes and pairs (finding 1 changes levels only); the CC11 drops at both sub. p's and the sfp; `BEAT_STRETCH = {}`.

# Critic C, cycle 57: blend and space (render c56)

Under review: `cycles/c56/render/` (42 instrument stems, 4 return stems, `00_Master.wav`), the delivered `cycles/c56/mvt1-mockup-c56.mp3`, `cycles/c56/rendered_build/parts.json`, `build/mix.json`. References: the stored metrics of Brahms 1/i, 4/i, 1/ii, 4/ii (`symphony/render/critics/c00`, `c04`; their audio is not on this disk) and the Dvořák 9/i MP3 (audio on disk, lossy, analysed with the same scripts as the render).

Labels. Measured: computed from the audio or the build data. Simulated: computed from the stems' spectra with a filter model (sum of stems equals the master within 0.3 dB in every band, so energies add). Inferred: reasoning from those numbers. Nobody listened. Scripts and their text outputs are in `cycles/c57/critic_scripts/C/` (`stems57.py` and `bands57.py` build the caches; one script per table below; the audio copies and caches were deleted at the end).

## Manual notes

PDF pages of the May 2021 HO Opus manual, chosen for this cycle's questions (divisi tracks, wind width, mic positions, the cymbal patch).

| Manual says (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| DIV A / DIV B patches hold one chair of each stand and exist with Close mics only (p.89). "You can mix the divisi close mics and the other non-divisi mics": for the other positions load the same articulation in its non-divisi version and set its level (p.90) | "Cello solo" (`Celli KS Master DIV A`, Close only), bars 171-174 | No. The track has no room mic at all and is narrowed to a point: stem correlation 0.999 (finding 1) |
| Close mics give presence, Main (Decca tree, fifth row) gives "more room reflections than direct sound", Surround adds depth (p.138). Each position has its own volume, pan and on/off (p.139) | `mic_db`, `pan_by_mic` | Yes for the layout. Two tracks of the wind group kept the group width 0.5 on a Close-led mix (finding 4) |
| Channel Routing can sum a patch to dual mono; Stereo Double widens (p.141) | Woodwind width | Not used, and not needed: the narrow winds are made with `panLeft` / `panRight` (width 0.05). Stereo Double would add a second, artificial width on top of the recorded Close pair; I do not recommend it (inferred) |
| 18in Zildjian Sus Cymbal Cresc: crescendo that peaks and rings, 2 dynamic levels, "very little coloration" in the top (p.119) | Bar 159-160 roll and stroke | Yes. At the climax the cymbals carry 21 % of the master's 6-20 kHz (suspended 11, crash 10); the top-band share there is -26.4 dB, 1.8 dB over the Dvořák file's loudest 2 % of frames. No change asked |
| The room "is heard as long as the samples are playing (including the release trail samples)" (p.222) | Note ends on the dry stems | Not for Trumpets 1-3: -34.5 dB at 0.15-0.30 s after a note end, the other brass -12 to -18.5 (finding 2) |

MANUAL-GAPS in this lens: #4 (Mid mics on the winds) still untried. The winds with their return decay 4-5 dB faster than the strings at 0.15-0.60 s (bar 170: winds -17.1 / -25.5, strings -12.3 / -21.2 dB), as in c53; a Mid-mic test on Oboe 1 and Cor anglais (Main at -20.6 / -11.6 dB, stem correlation 0.99 / 0.91) is the remaining way to give them recorded room. Not ranked this cycle. #7 (half-section divisi) not tried; finding 1 concerns the one DIV track in use.

## EW-TEMPLATE-PLAN sections in this lens: what is not applied

- Section 1: applied, with these deviations. Strings, brass, harp and timpani have `pan_by_mic` Main = "seat" with `width_by_mic` 0.8 (the plan: Main full width, not re-panned). Timpani Close -14 / Main -6 and no Surround (plan -8 / -7 / Surround 0). Harp Close -4.4 / Main 0, no Mid (plan Close 0 / Mid 0 / Main -9). Clarinet 2 and Contrabassoon keep width 0.5 where the other winds have 0.05.
- Section 2: applied with return faders 8 / 9 / 4 / 4 dB under the template (strings / brass / winds / percussion), the impulse cut to half, glue return off.
- Section 3: applied except the timpani +8.6 dB at 84 Hz (absent), the strings' +4 dB shelf (0), brass bells at half depth, harp high-pass 80 Hz. The delivery `master_eq` has an added 260 Hz bell and a 3 kHz shelf in place of the 8 kHz one.
- Section 8: Duc's send profile, tutti entry spread and room-noise bed not applied; celli -1.6 dB and short-row -5.4 dB sends applied.
- Section 9: register sends applied (trumpets -3, low brass -7, bassoons and basses -10), 2.3 kHz low-pass on the returns applied, narrow brass applied.

## Whole-movement figures (measured; all pass unless a finding says otherwise)

| | c56 master | c56 delivered | references |
|---|---|---|---|
| L/R correlation, whole band | 0.549 | 0.545 | 0.491-0.554 |
| below 250 Hz / 250 Hz-4 kHz / above 4 kHz | 0.606 / 0.548 / 0.464 | 0.618 / 0.543 / 0.435 | 0.541-0.624 / 0.473-0.561 / 0.378-0.525 |
| side/mid | -5.35 dB | -5.31 dB | -4.7 to -5.4 |
| pan spread | 0.351 | | 0.314-0.347 |
| 20-100 / 100-250 / 250-500 Hz share | -14.8 / -8.6 / -6.4 | -13.4 / **-9.0** / -5.9 | -7.9 to -8.9 (Brahms), -22.1 (Dvořák) / -6.7 to -8.75 / -5.95 to -7.1 |
| 2-6 / 6-20 kHz share | -9.7 / -28.8 | -9.95 / -30.2 | -10.4 to -12.4 / -28.6 to -32.3 |

Bar 170 stop on the master: 19.9 dB down at +0.3 s (S4 asks for at least 13), 20 dB down after 0.31 s (reference median 0.485 s), late slope 1.84 s (target 1.5-2). The mix is now drier than the recordings in the first 0.3 s; do not dry it further.

## Answers to the coordinator

- **"Violins I f62" / "Violins II f62": same room as the main tracks (measured).** They are the full section patches with the section's mics. Stem correlation 0.416 / 0.509 (Violins I / II main tracks 0.421 / 0.460), side/mid -2.8 / -4.3 dB (-2.9 / -3.8), R-L -7.1 / -4.1 dB (-6.7 / -4.0). In bars 55-61 the master reads correlation 0.505, side/mid -4.4 dB. Nothing to fix.
- **"Cello solo" is the mono track: finding 1.**
- **Woodwind width:** Oboes 0.99, Bassoons 0.92, Cor anglais 0.91, Bass clarinet 0.90, Flute 1 0.87, Clarinet 1 0.77 stem correlation; side/mid -7.7 to -12.4 dB. They are point sources with a seat, which is correct for single players, and the master's width figures are inside the references with them. Two tracks do not match: finding 4. Stereo Double: not recommended (see Manual notes).
- **140-355 Hz share against the Brahms references:** delivered -6.55 dB; Brahms 1/i, 4/i, 1/ii, 4/ii -9.1, -8.2, -9.1, -8.5 (summed from their third-octave bands); Dvořák -6.0. So 1.6-2.5 dB over the four Brahms files and 0.6 dB under the Dvořák. Split by octave the picture is clearer: 180-355 Hz -7.2 dB (Brahms -9.9 to -10.5, Dvořák -7.9) and 90-180 Hz -10.7 dB (all five -7.3 to -9.5). The upper octave is at the top of the references, the lower octave is under all of them, and the lower octave falls further in the loud passages. Finding 3.
- **Sus MAX one-row retest: worth one range-render pair on Violins I 56-90 only, low priority (inferred).** The finale's result (27 of 29 violin half notes within 4 dB) was on violins; its lower strings still fell 6-12.5 dB on 5 of 20 long notes, so do not test the celli or violas. Class leads change timing, not the sag: c55 measured 7.9 dB front minus tail on Sus MAX at this tempo with one 60 ms lead. Adopt only if, without body lifts, 25 of 29 long notes stay within 3 dB and S stays at robust SD 10 ms with at most 1 over 40. The gain for Dan's envelope complaint is at most the 64 body-lift notes (6 % of the 1054 notes with 3 dB inside), and finale technique 55 says the row move then needs a per-note level refit, which writes points back.

## Findings

### 1. The coda solo (bars 171-174) is a near-mono image 5.6 dB to the right (measured)

Where: "Cello solo" (stem 38), qn 680-696, 381.6-395.0 s, with Cor anglais and Bassoon 2.

Evidence:
- Stem: correlation 0.999, side/mid -9.6 dB, R-L +6.0 dB on every note (SD 0.1 dB). The Violoncellos section reads 0.50, -4.0 dB, R-L +4.9 dB (+2.9 dB in bars 175-178, where it takes over). The solo is a point with no recorded room, placed 1-3 dB further right than the section its player sits in.
- Master per bar: bars 171-174 R-L +6.0 / +5.6 / +5.5 / +5.4 dB, correlation 0.94 / 0.90 / 0.85 / 0.90, side/mid -8.5 to -7.6 dB. Over all bars the median is R-L 0.0 dB (10th to 90th percentile -2.9 to +2.7) and correlation 0.55 (0.45 to 0.68). These four bars are the narrowest and most one-sided of the movement. The celli section's own melody in bars 47-50 reads master R-L +0.6 dB, correlation 0.44.
- Everything else sounding is on the right too (Cor anglais R-L +5.2, Bassoon 2 +3.7), and the returns follow their input: R Strings +6.4 dB, R Winds +7.5 dB in these bars. The return under the solo is -12.5 dB, the usual string ratio, so the amount of hall is not the problem; its position and the missing width are.
- On headphones a 13-second solo sits in the right ear (inferred).

Fix (`build/mix.json`, `tracks["Cello solo"]`; pass-2 project only, range test over qn 679-697 before the full render):
- `"seat"` 0.35 → 0.20, `"reaper_pan"` 0.15 → 0.0, `"width"` 0.2 → 0.45. The principal sits at the front desk, nearer the centre than the section's middle. The wider setting lets the DIV A Close pair keep its own stereo picture (Clarinet 2 at width 0.5 reads correlation 0.48, the winds at 0.05 read 0.87-0.99).
- Targets: stem R-L +2.5 to +4 dB (inside the section's +2.9 to +4.9), stem correlation 0.85 or less, per-note R-L SD under 1.5 dB, master bars 171-174 R-L under +4 dB and correlation under 0.80. Re-match `gain_db` to the c56 stem level (K-weighted) after the change.
- If the stem stays above 0.9 at width 0.45, use the manual's own recipe (p.90): an alias track of the same notes on `Celli KS Master` with Main only, 10-12 dB under the solo stem, to supply the room mic. It costs one more pass-2 instance, so try the width first.

### 2. Trumpets 1-3 still end without a release, and their hall share is the lowest of the orchestra (measured)

Where: every note end of "Trumpet 1 / 2 / 3" (`1TP KS Master`); bars 26, 32, 73, 83, 138, 170.

Evidence:
- Dry-stem level after note ends that are followed by a rest (medians, dB under the note body, 0.05-0.15 / 0.15-0.30 / 0.30-0.60 s): Trumpets 1-3 -10 / **-34.5** / **-61**; Trumpets a2 (`2TP`) -7.5 / -18.5 / -28.5; horns -5.5 / -12 to -15 / -26 to -29; trombones -7 / -14 to -18.5 / -28 to -35; tuba -7 / -17 / -32. Time to -20 dB: 0.14 s against 0.21-0.32 s.
- At the six tutti stops the three stems together read -49.5 dB at 0.15-0.30 s (c53: -49.6). Nothing has changed since c53 finding 2.
- Return level under the dry signal, fitted on 2-second bins (R Brass = a·horns + b·trumpets + c·low brass, median error 0.8 dB): horns -18.5 dB, trumpets -22.9, low brass -23.3. Strings -14.1, winds -11.8, timpani -5.9. So the one brass set with no tail of its own also gets 9-11 dB less hall than strings and winds.
- c53's test of `rt_gain_db` +6 moved the 0.30-0.60 s window by exactly 6 dB (-53.6 → -47.6) and the 0.15-0.30 s window by 0.4 dB. From those two numbers the trail sits about 47 dB under the note at 0.15-0.30 s, so it needs about +20 dB, not +6, to reach the other brass (inferred from the c53 table).

Fix, in this order:
- `build/mix.json` `tracks["Trumpet 1"]`, `["Trumpet 2"]`, `["Trumpet 3"]`: add `"send_offset_db": {"R Brass": 3.0}` (group value -3.0; "Trumpets a2" keeps the group value because its stem has a full release). Net +6 dB of return for these three tracks: -16.9 dB under dry, still 2.8 dB drier than the strings. Expected trumpet level at 0.15-0.30 s after a stop about -19 to -21 dB (inferred: return level less 2-4 dB of early decay), which is the Trumpets a2 stem's own figure. The R Brass stem rises by under 3 dB (bound: trumpets are one of three feeds); the master's stop decays move by under 0.5 dB (inferred).
- Range test on Trumpet 1, the stop at 102.15 s (as in `cycles/c53/actor_scripts/tp_rt_test.txt`): `"rt_gain_db": {"db": 18.0, "rows": ["Sus Non Vib MAX", "Leg Slur MAX"]}`. Pass: -26 to -34 dB at 0.30-0.60 s (trombone -26.7 on that stop) and no audible trail under held pp notes (check a pp note end on the stem: the trail must stay 20 dB under the body). Ship on all three if it passes; the send change stands either way.
- BRIEF S4 says not to raise sends for depth. This raises one send on three tracks to cover a release the sample does not have; the master is 19.9 dB down at +0.3 s, well past the 13 dB target.

Still open and not fixable with sends (measured, no change asked): at bar 170 the whole brass with its return is 8.0 dB under the strings at 0.30-0.60 s (-29.2 against -21.2; c53 limit 4). The strings' figure is their Main-mic release, not their return, and the solo brass patches' releases are 5-10 dB shorter. Raising the low-brass send by 4 dB would gain 1.5-2 dB there (inferred).

### 3. Loud passages lose the 56-180 Hz octave-and-a-half; two cuts fitted to the Dvořák MP3 sit exactly there (measured, fixes simulated)

Where: the tutti spans (bars 24-32, 82-83, 115-124, 130-134, 138-142, 157-162), "Double basses" `loud_eq`, and the delivery `master_eq`.

Evidence:
- Share of the master by loudness (same script on both files; frames ranked by level):

| | 56-90 Hz | 90-180 Hz | 180-355 Hz | 710 Hz-2 kHz | 2-6 kHz |
|---|---|---|---|---|---|
| c56 softest 30 % | -11.7 | -9.5 | -6.1 | -6.8 | -12.8 |
| c56 loudest 10 % | -20.4 | -11.3 | -7.6 | -4.0 | -9.5 |
| c56 loudest 2 % | -20.3 | -12.2 | -8.4 | -3.4 | -9.0 |
| Dvořák softest 30 % | -17.6 | -11.4 | -7.2 | -5.3 | -13.3 |
| Dvořák loudest 10 % | -27.4 | -7.3 | -8.1 | -5.3 | -11.3 |
| Dvořák loudest 2 % | -27.7 | -6.0 | -7.9 | -6.1 | -12.3 |

  From soft to loud the recording gains 5.4 dB of 90-180 Hz share; the mockup loses 2.7 dB. The stored Brahms figures agree: loud-minus-soft spectrum shape at 157 Hz +2.8, +4.2, -0.4, +5.1 dB (Dvořák +5.2), mockup -2.4 dB (delivered -1.4); at 79 Hz Brahms -4.7, -0.9, +0.8, +0.7, mockup -8.3. Whole-file 90-180 Hz: delivered -10.7 dB, the five references -7.3 to -9.5.
- So the low-mid problem in the loud bars is a shortage below 180 Hz, not an excess above it. In the soft passages the mockup matches the Dvořák within 1-2 dB in both octaves.
- Who supplies 90-180 Hz in the loudest 10 % of frames: Double basses 34 %, Timpani 26 %, Violoncellos 11 %, Tuba 10 %, R Perc 5 %, Bass clarinet 4 %, Contrabassoon 3 %; trombones, horns and bassoons under 2 % each. The basses play G1 there (median pitch 31): their fundamental band (50 Hz) is 13.6 dB under their 99 Hz band, so the 98 Hz partial is their low end.
- `tracks["Double basses"]["loud_eq"]` cuts that partial in the loud spans: `bell2` 98 Hz -4 dB (0.5 oct) and a low shelf 80 Hz -5 dB. Both date from series 1 (c21: "60-100 Hz 7.5 dB over a Dvořák reference"). The BRIEF now says not to tune the low end to that file; the Brahms files have 13 dB more below 100 Hz. c56 removed the static bells for the same reason and left these two.
- The delivery EQ's bell at 167 Hz, -1.6 dB, 1.39 oct covers 103-270 Hz. The delivered 100-250 Hz share is -8.99 dB, 0.24 dB under the lowest reference (-8.75).

Fix a (`build/mix.json`, "Double basses" `loud_eq`): delete the `bell2` 98 Hz band from the first row (keep its 160 Hz +6 bell); low shelf 80 Hz -5 → -2 in the third row. Simulated on the loudest 10 % of frames (435 of 503 lie inside the spans): 99 Hz band -14.7 → -12.2 dB (Brahms whole-file -10.7 to -13.5), 79 Hz -23.5 → -21.5, 56-90 Hz share -20.5 → -18.5, 90-180 Hz -11.2 → -9.8, level in those frames +0.16 dB. Half step if the coordinator prefers it: bell -2, shelf -3.5 gives 90-180 Hz -10.6 and +0.06 dB.

Fix b (`build/mix.json` `master_eq`, needs no render: `tools/deliver_master.py` on the c56 master): delete the bell at 167 Hz; replace the bell 260 Hz -1.5 dB with 290 Hz, -2.5 dB, 1.0 oct. Simulated on the delivered spectrum: 100-250 Hz -8.99 → -7.90 (inside), 250-500 Hz -5.86 → -6.31 (inside), 90-180 Hz -10.67 → -9.61, 180-355 Hz -7.24 → -7.23, the 315 Hz third-octave band -10.4 → -11.1 (highest reference -12.3), 2-6 kHz -9.95 → -10.03, level +0.07 dB. The ride and limiter are not in the model.

Conflicts and checks: c56's do-not-touch list names the basses' `loud_eq` rows ("they guard the loud bars"); that judgement had no loud-bar measurement against the Brahms files behind it, and this is one. Critic B is checking single bass pitches this cycle; fix a acts only inside the loud spans. After the render: bar 160 over bar 122 (both spans get the change; keep 0.5 dB or more), limiter under 1.5 dB, bar 84 (outside the spans, should not move), and the loud-minus-soft shape at 157 Hz (aim: 0 dB or more).

### 4. Clarinet 2 and Contrabassoon are wide and wander; their desk partners are points (measured)

Where: "Clarinet 2", "Contrabassoon" (`width` not set, so the wind group's 0.5; every other wind has 0.05 or, Bass clarinet, 0.3).

Evidence, per note on the stems:

| | R-L median | SD over notes | range | side/mid |
|---|---|---|---|---|
| Clarinet 1 (width 0.05, seat -0.22) | -3.1 dB | 1.8 | -9.7 to +0.6 | -9.0 dB |
| Clarinet 2 (width 0.5, seat -0.20) | -6.8 dB | 4.0 | -12.1 to +4.5 | -4.6 dB |
| Bassoon 2 (width 0.05, seat 0.22) | +3.5 dB | 1.0 | +0.9 to +6.4 | -10.4 dB |
| Contrabassoon (width 0.5, seat 0.25) | +6.8 dB | 2.3 | +2.8 to +11.4 | -2.5 dB |

Clarinet 2 moves across 16 dB of the image from note to note (per-pitch SD 3.9 dB) and sits 3.7 dB left of Clarinet 1, which has almost the same seat. The Contrabassoon is as far right as the tuba (+7.0) and wider than any string section (stem correlation 0.28, side/mid below 250 Hz -0.6 dB); it supplies 6-8 % of the master's side energy at 90-355 Hz from about 3-4 % of the level.

Fix (`build/mix.json`): `tracks["Clarinet 2"]["width"]` 0.05, `tracks["Contrabassoon"]["width"]` 0.05 (state change: full rebuild of both tracks). Expected (inferred from their partners): Clarinet 2 R-L about -3 dB with SD under 2; Contrabassoon about +4 dB, side/mid about -10 dB. Narrowing changes the level: re-match both `gain_db` to the c56 stems (K-weighted, whole file) and check the Contrabassoon's `soft_trim_db` bars. Master correlation below 250 Hz rises by about 0.01 (0.606 now, reference top 0.624); check it stays inside.

### 5. Timpani and harp sit in a wetter room than every other family, and the percussion return pulls left (measured)

Evidence:
- Return level under the dry stem where one source plays alone (2-second bins): Timpani -5.9 dB (93 bins), Harp -7.0 (28), Tam-tam -3.1 (6). Strings -14.1, winds -11.8, horns -18.5, trumpets -22.9, low brass -23.3. The timpani's hall is 6-8 dB higher, relative to the instrument, than the strings' and winds' and 12-17 dB higher than the brass's. Whole-file the R Perc stem (-45.2 dB RMS) is as loud as R Strings (-44.7) though the percussion plays far less.
- During the rolls R Perc is 4.8-6.1 dB under the dry timpani (bars 1-4, 39-44, 143-147, the final bars) and 2.9 dB under it in the tutti of bars 117-122.
- The Northwest Hall return shifts its input left: harp dry R-L -4.5 dB, return -8.7; tam-tam -4.3 and -8.7; in bars 47-50 the harp's return (R-L -12 dB, level -49.4 dB) is as loud as the string return under the celli melody (-49.3 dB). The string and wind returns follow their input (slope 1.03 and 1.08, offset +0.3 and -1.1 dB).
- In energy the return is small: 3.2 % of the master at 90-355 Hz over the movement (4.5-5.8 % in bars 39-44 and 143-147), 9 % of the master's side energy there. Lowering it changes no master band by more than 0.2 dB (simulated). The gain is the timpani's distance matching the other families and less wash under the rolls (Dan's standing note 3).

Fix (`build/mix.json`): `groups["timp"]`: add `"send_offset_db": {"R Perc": -6.0}`; `groups["harp"]`: add `"send_offset_db": {"R Perc": -4.0}`; `groups["perc"]` unchanged (the tam-tam and cymbal strokes ring in the hall by design). Timpani return then -11.9 dB under dry, the winds' ratio; harp -11.0. Check after the render: timpani stroke decay on the master at the isolated strokes of bars 179-180 (the dry stem alone holds 0.69 s to -20 dB, so the strokes will not go dead), and the roll-settle levels of critic B's table (the roll's total level falls by under 1 dB).

### 6. Observation for the balance lens: the tutti is carried by Violins I above 700 Hz (measured, no blend change asked)

In the loudest 2 % of frames the master's 710 Hz-2 kHz share is 2.7 dB and the 2-6 kHz share 3.3 dB over the Dvořák file's loudest 2 % (-3.4 / -9.0 against -6.1 / -12.3), the mirror of the low shortage in finding 3. Violins I supplies 39-57 % of the master's 2-6 kHz in every tutti checked (bar 26: 26 %; bars 117-121: 53 %; bars 139-142: 57 %; bars 160-161: 39 %) and its 2-6 kHz band is only 1.6 dB under its own 355 Hz-2 kHz band in loud frames (Violins II -4.1, trumpets -7.5 to -8.4, trombones -6 to -8). The Brahms files brighten more than the Dvořák in loud passages (+4 to +6 dB at 2.5 kHz against +2.5), so this is a direction, not a fault proven against all references. If critic B finds the brass under the strings at ff, lifting the brass is the better cure than a further shelf on Violins I (inferred). Solo Trumpet against 2 Trumpets tone: 2-6 kHz -7.5 to -8.4 dB and 6-20 kHz -23 to -26 dB under their own mid band on Trumpets 1-3, -6.3 / -20.8 on Trumpets a2, trombones -6 to -8 / -23 to -25: matched within 2.5 dB, no change asked.

## Dan's checks in this lens

- S4 (too wet): passes with margin (19.9 dB at +0.3 s, bar 170). See the note under the whole-movement table.
- S3: not re-measured.
- Item 7 (loop pulsing), item 8 (accent fronts), S1, S2: not measured by this critic this cycle.
- Seats (stem R-L, whole file): Violins I -6.7, Violins II -4.0, Violas +0.9, Violoncellos +4.9, Double basses +5.2; horns -3.6 to -5.5, trumpets +3.7 to +4.2, trombones +4.7 to +5.7, tuba +7.0; flutes -4.1, clarinets -3.7, oboes +5.2 / +6.7, bassoons +2.5 / +3.3; timpani +1.0; tam-tam and cymbals within 0.6 dB of centre. Master R-L by band: 20-90 Hz +6.4 dB, 90-180 Hz +2.7, 180-355 Hz +1.3, 355 Hz-2 kHz -0.1, 2-6 kHz -2.7. The Dvořák file reads +3.3 / +2.2 / -1.3 / -3.7 from 90 Hz up and has no content below 90 Hz to compare, so the +6.4 dB of the bottom band is recorded here without a judgement.

## Do not touch

The f62 tracks' mics and seats (they match the main violins). The narrow winds (width 0.05) and their seats. Brass `track_width` 0.65 / 0.75 and the brass seats. The side EQ (60 Hz shelf, 180 Hz bell -4.5 dB): correlation below 250 Hz is 0.606, inside the references. The R Strings and R Winds faders and sends. The 2.3 kHz low-pass on the returns and the half-length impulses (late slope 1.84 s). Main-only centred tam-tam and cymbals and their R Perc send. The Double basses' static `eq` as c56 left it (87.3 Hz bell -4, no `mute_eq`) and the `loud_eq` bells at 160 and 180 Hz. The delivery ride, limiter, the 1.18 kHz bell and the 3 kHz shelf.

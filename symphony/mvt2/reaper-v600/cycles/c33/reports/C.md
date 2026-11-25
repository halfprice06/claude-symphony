# Cycle 33, critic C (blend and space): the c32 render of v600

Lens: one room. This covers reverb, seating and panning, mic positions, tone matching between sample sets (the DIV tracks against their sections, the harp harmonics, muted against open strings), and low-end build-up against several reference recordings.

Material:
- the c32 stems and master, with the c28, c29 and c31 renders for comparison;
- `cycles/c32/rendered_build/parts.json` and `mix.json`;
- the Opus states in `jobs/*.b64`, decoded: every loaded mic channel's volume, send and pans, and the hall insert's settings;
- references: the Dvořák 9/i mp3 (decoded and analysed with the same code as the master), and the stored metrics of Brahms 1/ii and 4/ii (`symphony/render/critics/c04/ref_brahms*_musopen/metrics.json`).

Method: frames are 4096-point FFTs every 21 ms, summed into third-octave bands per channel, with the L·R cross term kept so that correlation and R-L can be computed per band. qn are mapped to seconds through the parts.json tempo map. EQ changes were simulated as band gains on the stems' band powers, summed incoherently into the master. On c32 this sum matches the real master within 0.1 dB in the bands used. Side-channel changes were simulated in M/S form: L' = M + gS, keeping the M·S cross term.

Labels: "measured" means a number from these files; "inferred" means reasoned from those numbers, the manual or earlier cycles.

## Manual notes (L2: PDF pages 219-223 of the May 2021 HO Opus manual; pages 220-221 also viewed as images; MANUAL-GAPS.md read)

| Page | What it says | Where it applies here | Render follows it? |
|---|---|---|---|
| 219 | Algoverb: an algorithmic stereo reverb (pre-delay, size, decay, density, early/late, bandwidth, low/high boost, stereo width, mix). | Not used. Every instance holds one convolution hall (below). | n/a. Nothing in the measurements calls for it: the convolution hall's decay matches the references (Do not touch). |
| 220 | Convolution Reverb: input gain, pre-delay, **Send Mono** (collapse the IR's L/R), true-stereo IRs, Bandpass with **High Cut and Low Cut** (30 Hz-18 kHz), **Width** 0-200%, Wet, Dry. | All 32 states (decoded) have the same settings: "S. Cal Hall Perc TS FR 3.3s", true stereo, fx volume 0.19, wet 2.0, dry 1e-6, high cut 5.5 kHz, **low cut 30 Hz (in effect off)**, width 1.0, Send Mono off. | Yes, as configured. The Low Cut is the manual's own lever for reverberant low end. I do not propose it: the lopsided low end measured below comes from the dry mics, not from the hall (finding 1), and a hall change is an Opus state change on all 32 tracks. |
| 221 | IR Envelope Preprocessing: Simple (one decay slider) or Full (start, end, fade-in, fade-out and their curves) to shorten or shape the IR. | `irSetup.envelopeMode 0` (no envelope) on every instance. | Yes. No shortening is needed. Measured from the automatic cut-off estimate the references use, the final chord falls -10/-20/-30/-40 dB at 0.68/1.17/1.49/1.80 s. Brahms 1/ii: 0.40/0.79/1.23/1.64; Brahms 4/ii: 0.20/0.48/1.15/1.72. Every family's tail falls about 25 dB/s after 1 s (table under "Checks"). |
| 222 | Mixing mic positions: the room ambience "is heard as long as the samples are playing (including the release trail samples)". One position (Main is common) is enough for a piece. Each mic can be recorded in its own pass to save RAM. | Woodwinds, horns, trombones, tuba, harp and timpani mix Close + Main; strings Close 0.66 / Main 1.0; DIV tracks Close only. | Partly. Mixing two spaced positions makes the L/R phase depend on pitch. Some notes come out with a fundamental 14-19 dB louder in one channel and near-zero or negative correlation (findings 1, 2). |
| 223 | Each mic position to separate outputs or tracks; several instruments may share an output. | Not used. Each track's mics are summed inside Opus; one stereo stem per track. | n/a. This would only matter for a per-mic EQ, for example narrowing only the Main pair's low end. That is not needed if the side shelves below are used. |

## Findings, ranked by what a listener would hear

### 1. The sub-bass sits in the right ear: the basses' A flat 1 pedal is 18 dB louder on the right (measured; fix simulated)

**Where:**
- Double basses (stem 26), every A flat 1 (MIDI 32, 52 Hz): qn 3 and 6.25 (bars 1-3), 87 (bar 30), 168 (bar 53), 238 and 244 (bars 70-72), and the coda pedal 273.2-304 (bars 83-92).
- The timpani (stem 20) adds a fully decorrelated low end in bars 67-70 and 84-85.

**What is wrong.** The basses' seat (+0.5, width 0.28, Opus pans [0.22, 0.78]) puts their overtones at R-L +7.6 dB, which is the image a listener expects. At the A flat 1 fundamental, though, the left channel is almost empty: R-L is +15..+19 dB on every A flat 1, against a median of +7.6 on the other pitches. Real recordings keep the lowest octave nearly central even when the basses sit on the right. On headphones, which is how Dan listens, the tonic pedal of the opening and the coda becomes a hum in the right ear only (inferred listener effect).

**Evidence (measured).**
- Master, 35-63 Hz, R-L / correlation:
  - whole movement +6.7 dB / 0.74;
  - bars 1-3 +12.7 / 0.42;
  - bars 83-86 +13.3 / 0.44;
  - bars 87-92 +7.4 / 0.58;
  - climax 61-64 +6.9 / 0.77.
- Dvořák 9/i, same bands: 35-50 Hz -1.0 dB, 50-63 Hz +0.5 dB. Above 80 Hz it carries its basses at +3.5 dB right, which is the same seat we use.
- Basses stem alone, 35-50 / 50-63 Hz: bars 1-3 +18.4 / +18.5, bars 83-86 +17.9 / +17.7.
- Timpani stem: correlation below 250 Hz 0.06-0.20, the lowest of all stems. In bars 65-70 it is 10% of the master's energy below 250 Hz, and the master's correlation there is 0.42 (Brahms whole-piece 0.60/0.62).

**Fix** (`build/mix.json`, REAPER-side only, applied by `--mix-only`/`--midi-only`, no Opus state change, no memory):
- Double basses: `"side_shelf": {"hz": 100, "db": -15}`, replacing `{"hz": 200, "db": -2}`. A ReaEQ low shelf at 100 Hz is still about -2..-3 dB at 200 Hz, so c21's setting is roughly kept.
- Timpani: `"side_shelf": {"hz": 150, "db": -9}`, replacing `{"hz": 200, "db": -2}`.

Simulated on the c32 stems, together with finding 2:

| Master, 35-63 Hz | c32 R-L / corr | After the fix |
|---|---|---|
| Whole movement | +6.7 / 0.74 | +2.3 / 0.95 |
| Bars 1-3 | +12.7 / 0.42 | +3.3 / 0.91 |
| Bars 83-86 | +13.3 / 0.44 | +3.5 / 0.97 |
| Bars 87-92 | +7.4 / 0.58 | +2.1 / 0.90 |
| Bars 61-64 | +6.9 / 0.77 | +2.4 / 0.96 |

- Master correlation below 250 Hz: whole movement 0.58 -> 0.63; bars 65-70 0.41 -> 0.53 at 100-250 Hz and 0.56 -> 0.92 at 63-100 Hz.
- The 100-250 Hz image is unchanged (+2.7 dB R-L), so the basses keep their seat.
- Levels: basses -0.3..-0.4 dB, timpani -0.6..-0.8 dB (the side energy removed). Neither needs a level fix.

**Check:** 35-63 Hz R-L under +4 dB in bars 1-3 and 83-92; master correlation below 250 Hz 0.6-0.7 overall.

### 2. The bass clarinet solo (bars 31-36) is wide and phasey, and its longest note leans hard left (measured; fix simulated)

**Where:** Bass clarinet (stem 8), qn 90-108, the "solo, espr." in the chalumeau, an octave lower in v600, over the bassoon and contrabassoon pedal. The worst note is the E flat 3 at qn 93-97 (bar 32, the solo's longest and loudest note). The same pitch is lopsided at qn 193 (bar 58).

**What is wrong.** In this woodwind-only passage the master is the widest and least correlated of the whole movement. The solo's low end sits 8 dB left, although the instrument's seat is central (-0.05) and its overtones sit at -1.7 dB. Inferred listener effect: a solo that should be a focused central line sounds spread and hollow, and its body jumps to the left ear on the E flat.

**Evidence (measured).**
- Master correlation, whole band / below 250 Hz / 250 Hz-1 kHz, by passage:
  - qn 90-108: 0.35 / 0.38 / 0.31, side/mid -2.9 dB;
  - every other passage: 0.46-0.63 overall, side/mid -3.5..-6.4;
  - references: Brahms 0.51/0.55 overall, side/mid -4.9/-5.4.
- In this passage the bass clarinet is 96% of the master's energy below 250 Hz. Its stem: correlation below 250 Hz 0.39, R-L -8.0 dB. On c28 the same notes measured 0.55 and -6.5 dB. Inferred cause of the change: c29 raised the wind group's send to the true-stereo hall from 0.35 to 0.6.
- Per note, the fundamental band is within ±3 dB of the overtones' image except two:
  - E flat 3 at qn 93: R-L -13.9 dB, correlation -0.03, and also -13.4 dB at 198 Hz;
  - B flat 2 at qn 92 and 102: R-L -5.1 and -6.7 dB.
  - The other ten notes: -2.6..+1.4 dB.
- Mechanism (inferred from p.222 and the per-band numbers): the Close and Main mics are summed with different arrival times, so at some pitches the right channel cancels while the left adds.
- The same effect shows on other Close + Main tracks. Horn 1: E flat 4 at qn 226 (bar 67, the solo after the climax) -18.8 dB / correlation -0.40; at qn 193 -15.5 dB; F4 at qn 204 -14.6 dB. Cor anglais D5 at qn 157: +18.8 dB. A side shelf there would cost the horn 1.4-2 dB and pull its low band to the centre, away from its seat at -9 dB, so I do not propose one for the horns.

**Fix** (`build/mix.json`, Bass clarinet): `"side_shelf": [{"band": "lowshelf", "hz": 250, "db": -6}]`, replacing the current `[{"band": "highshelf", "hz": 250, "db": 1.5}]`. The +1.5 dB side boost above 250 Hz was a width setting for the upper winds; the v600 bass clarinet is a bass instrument in this solo.

Simulated:
- E flat 3 at qn 93: -13.9 dB / -0.03 -> -9.2 dB / 0.84;
- master at qn 90-108: correlation at 100-250 Hz 0.27 -> 0.76, side/mid -2.9 -> -4.6 dB;
- level cost: the note -0.9 dB, the passage under 0.5 dB.

-9 dB would give -6.8 dB / 0.93 at about -1.1 dB of level. Re-check the solo's level against the cor anglais and bassoons afterwards (B's lens).

### 3. Violins II div (bars 37-40, sul tasto) is still 9 dB brighter than the other half of its own section (measured; fix simulated)

**Where:** Violins II div (stem 30, `2nd Violins KS Master DIV B`, Close only, Flautando) against Violins II (stem 23, Flautando), qn 108-124, pp, under Flute 1's theme B.

**What is wrong.** c29's finding 4 added a high shelf at 1.5 kHz, -6 dB. That shelf closed only 2.1 dB of the gap at 1-4 kHz (c28 -1.6 dB, c32 -3.7 dB, against the section's -12.9 dB, each relative to its own 250 Hz-1 kHz band); it did more at 4-10 kHz (-17.0 -> -23.0). Third-octave differences, div minus section, after normalising: +6.5 at 794 Hz, +11.6 at 1 kHz, +6.7 at 1.26 kHz, +5.1..+8.4 at 1.6-3.2 kHz, +4.9..+6.3 at 4-5 kHz. So the excess starts below the shelf's corner. The register difference (the div voice is 5-7 semitones higher) accounts for about 2-3 dB: the Violas div / Violas pair, with the same voicing, differs by only +1..+4.7 dB above 1 kHz. Inferred listener effect: an airy, close upper line on top of a dull lower one, where the score has one section playing sul tasto.

**Fix** (`build/mix.json`, Violins II div `eq`): `{"band": "highshelf", "hz": 1000, "db": -10}` in place of the 1500 Hz / -6 dB shelf.
- Simulated: div 1-4 kHz -3.7 -> -7.2 dB, so 5.7 dB over the section, of which about 3 dB is register. 4-10 kHz -23.0 -> -26.4.
- The div voice falls about 1.4 dB, so add +1.4 to its 108-124 role in `build/roles.json`: Violins II div, the row c32 set to -1.
- ReaEQ only, no Opus rebuild.

### 4. At both ff tuttis the 125 Hz octave is 3 dB weak and the 250 Hz octave 2 dB strong against the references (measured; EQ fix only partial, inferred)

**Where:** The loudest 10% of frames: qn 196-220 (bars 59-64) and 259-270 (bars 78-81).

**Evidence (measured).** Octave sums relative to the 250 Hz-2 kHz band:

| | 125 Hz octave | 250 Hz octave | 250 minus 125 |
|---|---|---|---|
| c32, loud 10% | -11.0 | -6.3 | +4.7 |
| Dvořák, loud 10% | -8.0 | -8.1 | 0.0 |
| c32, soft 30% | -7.7 | -5.2 | +2.5 |
| Dvořák, soft 30% | -10.3 | -6.6 | +3.7 |
| c32, whole | -10.4 | -6.4 | +4.0 |
| Brahms 1/ii, whole | -8.1 | -8.8 | -0.7 |
| Brahms 4/ii, whole | -6.2 | -8.0 | -1.8 |

- Loud-minus-soft shape at 157 Hz: c32 -3.7 dB, Dvořák +3.7, Brahms -0.4/+5.1. The orchestra loses low-mid weight as it gets louder, where real ones gain it.
- The soft passages are inside the reference range, so the problem sits in the tuttis. It has been unchanged since c28 (c29 finding 6).

**Contributors in the loud frames (measured):**
- 89-178 Hz: basses 51%, celli 19%, timpani 11%, bass clarinet 11%, bass trombone 3%, tuba 3%, contrabassoon 3%, Bassoon 2 1%.
- 178-355 Hz: celli 32% (they carry the tune at 156-349 Hz), violas 10%, basses 9%, contrabassoon 8%, tuba 7%.
- The 125 Hz line in the score (A flat 2 / C sharp 3 at 104-139 Hz in Bassoon 2, the bass clarinet, the bass trombone and the timpani) is thin: the tuba, contrabassoon and bass trombone stems each have 5.5-10 dB more in their 250 Hz octave than in their 125 Hz octave.
- LEARNINGS §14 already says much of this comes from the voicing.

**Fix (optional, after 1-3).** In the existing loud windows (the basses' `loud_eq` points `[[190,0],[200,1],[214,1],[216,0],[254,0],[259,1],[269,1],[271,0]]`):
- move the basses' loud bell from 150 Hz +4 to **115 Hz +6** (1 oct; keep the 100 Hz -3 shelf);
- add `loud_eq` with the same points and `{"band": "bell", "hz": 125, "db": 4, "bw_oct": 1.0}` on Bass clarinet, Bassoon 2, Bass trombone, Tuba and Contrabassoon.

Simulated: loud-frame 125 Hz octave -10.9 -> -9.4 dB, 250 minus 125 +4.5 -> +3.0, soft passages unchanged. That closes only about a third of the gap. A level-only or EQ fix cannot do more without putting the bass octave over the tune, so I rank this below the image problems. Do not add any boost at 150-250 Hz: that band is already high.

### 5. The "4 soli" celli (bars 83-86) are a full section at -3 dB; the half-section patch is already loaded on another track (inferred)

**Where:** Violoncellos (stem 25), qn 274-286, ppp "4 soli" under the harp harmonics. Violoncellos div (stem 29) holds `Celli KS Master DIV A`, a half section on the Close mic only, and is silent outside bars 18 and 21-22.

**What is wrong (inferred).** `SOLI_AS_META` plays four players as the whole section 3 dB lower (MANUAL-GAPS #8, p.89-90). The chorus of a full section is what distinguishes it from a small group, and level does not remove that.

**Measured tone match** (the reason the div track would blend): Violoncellos div against Violoncellos, over the same frames in bars 18 and 21-22:
- 1-4 kHz +2.2 / +2.3 dB;
- images +6.2 / +5.1 against +5.5 / +5.6 dB R-L;
- early drop 7.4 against 8.9 dB.

The coda's A-weighted balance is basses 4 dB under the celli at qn 274-286 (c29 target 4-8 dB). Moving the celli to the half section will lower them, so re-check that balance.

**Fix.** Route Violoncellos qn 273.9-286 to "Violoncellos div" with `TRACK_SPLITS` in `build/score_config.py` (the c32 A #6 proposal), with no memory cost.
- Move Violoncellos' `rebow_fills.json` entries 277.566, 281.683 and 284.151 to the div track's key, and its role [273.9,286,-3,0.5] with them, setting the role to 0.
- Refit with `fit_rebows.py` after the render.
- If the div track needs a row it has not loaded, it is fully rebuilt.
- The basses' 4 soli (bars 65-70, 87-92) have no div track. Leave them for a second-pass render (MANUAL-GAPS memory plan).

## Checks for items 8-9 and S1-S3 through this lens

**Room (c29 finding 2 follow-up, measured).** Early drop 0.15-0.25 s after a note-off into a rest of 1.1 s or more, 500 Hz-4 kHz:
- winds 9.4 dB (c28: 13.1);
- horns 8.5;
- strings 7.8 (c28: 7.5);
- DIV tracks 4.8.

The wind send change closed the gap to within 2 dB. Median decay after note-offs into rests of 2.6 s or more (dB at 0.6 / 1.0 / 1.6 / 2.4 s):

| Family | 0.6 s | 1.0 s | 1.6 s | 2.4 s |
|---|---|---|---|---|
| Winds | -19 | -31 | -42 | -59 |
| Horns | -22 | -31 | -44 | -59 |
| DIV tracks | -19 | -30 | -43 | -59 |
| Strings | -21 | -34 | -47 | -62 |

Every family decays in parallel. The strings' late tail is 3-4 dB lower, which is consistent with their seats at the front of the stage.

**Stereo (measured).** Master correlation 0.58 / 0.53 / 0.55 / 0.50 in four bands (below 250 Hz / 250 Hz-1 kHz / 1-4 kHz / above 4 kHz); Brahms below 250 Hz 0.60/0.62, 250 Hz-4 kHz 0.48/0.52, above 4 kHz 0.38/0.47. Sections run in concert order from Violins I -7.6 to Double basses +7.9 dB R-L. Harp -10.6 and harp harmonics -9.5 match.

**Muted against open (measured).** The coda's CC15 goes on before each muted entry: violas and Violins II at qn 273.5, Violins I at 274.5, Violas div at 268.5. Celli, basses and the solo/div tracks are right as printed.

**Item 8, loop pulsing (measured).** Master 100-300 Hz level and spectral-centroid autocorrelation at 3.95 s:
- bars 1-6: +0.08 / -0.01;
- bars 65-70: +0.03 / +0.12;
- bars 83-88: +0.01 / -0.04;
- bars 87-92: -0.13 / +0.02;
- final chord: -0.03 / +0.01.

Highest single stems: Double basses +0.25 at bars 87-92 and Violins II +0.24 in the final chord. All are under c29's 0.3 target.

**S3 (measured).** No note-off into a rest has a tail falling more than 22 dB within 0.3 s on any stem, except Violins I at qn 271-274. That note ends a printed decrescendo, so it is not a cut. In parts.json, the vol_db dips inside rests (Timpani 238.45 -17 dB, 271.5 -17.7 dB, 9.45 -13.6 dB) are held flat by `build_reaper.py`'s tail hold, so they do not reach the render.

**Item 9, S1, S2:** not measured here (A's lens).

**Do not touch:**
- the shared true-stereo hall: IR, 30 ms pre-delay, fx volume 0.19, wet 2.0, 5.5 kHz high cut, no IR envelope;
- the c29 wind send 0.6 and width 0.05 on the upper winds;
- the seats in concert order;
- the con sordino lanes and the muted/open colour difference;
- the Violas div / Violas and Violoncellos div / Violoncellos tone match;
- the series 1 Cb EQ set (bell2 80 Hz, 160 Hz +4.5, climax shelf -3);
- the Violoncellos side shelves (low 200 Hz -2, high 1.5 kHz +4).

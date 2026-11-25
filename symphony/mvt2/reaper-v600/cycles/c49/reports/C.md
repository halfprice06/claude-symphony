# Cycle 49, critic C: blend and space (review of the c48 render)

Method. I measured the 32 instrument stems, the 4 return stems and `00_Master.wav` of `cycles/c48/` with my own numpy scripts (inter-channel correlation and right-minus-left level per band and per bar, per-note image, return levels, decays, envelope folds, band shares), read `cycles/c48/rendered_build/` (mix.json, build_reaper.py, score_config.py, parts.json), and compared with `symphony/render/assets/refs/dvorak9_i_columbia.mp3` (stereo measurements) and the stored metrics of the four Brahms movements (spectrum only). "R-L" is right level minus left level in dB; "corr" is the inter-channel correlation (1.00 = mono). No MANUAL-READING row exists for cycle 49, so the manual notes below are the pages this lens uses.

## Manual notes

| Reading (2021 manual, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.138 Microphone Positions: Close captures presence; Mid sits at the stage edge and gives "definition without the sound of close proximity"; Main (fifth row) captures "more room reflections than direct sound". | Every woodwind and horn track (Close + Main loaded, Mid never). Oboe 1: Close 0.939, Main 0.088. | Partly. Oboe 1 is almost Close-only (finding 2). Mid is untested (MANUAL-GAPS #4). |
| p.222, 6.3.1 Multiple Microphone Mixes: "mixing 2 or 3 of the mic positions in the right proportions can add dimension". | Violin I solo (Close only), Oboe 1 (Main 20.6 dB under Close). | No on these two tracks (findings 1, 2). Yes on the sections, horns, flutes, clarinets. |
| p.90 Divisi: the divisi instruments have only Close mics; for room, "mix the divisi close mics and the other non-divisi mics". | Violin I solo (a DIV A patch, bars 17-22), Violins II div, Violas div, Violoncellos div. | No: the four tracks are Close only with no room mic. It is audible only on the solo; the other three are masked by the sections (numbers under "Checked"). |
| p.75 Hollywood Solo Violin: a solo-instrument mic set with Close and Mid. | Bars 17-22. | Not available: licensed but not installed (MANUAL-GAPS #3). |
| p.139 and p.196: each mic has volume, pan and a load switch. | `apply_mix()` in build_reaper.py sets them; a mic volume change is an Opus state change. | Yes. |
| p.140 Master Channel PAN: changes left and right volume "while preserving the relative panning of the individual microphones". | The seat method pans only the Close mic (`pan_by_mic`); a later image correction should be a balance-type pan (REAPER track pan) so the Main picture is kept (findings 3, 4). | Yes. |
| p.68 Hollywood Harp: solo-instrument mic configuration. | Harp (Close 1.0, Main 0.355) and Harp harmonics. | Yes for the mics; the two harp patches do not share one image (finding 4). |
| p.143-144 Con Sordino (CC15, 64-127 on). | Muted string passages and the coda. | Yes: the mute colour is present in the stems. |

## Dan's standing checks, as far as this lens covers them

Loop pulsing (measured): envelope fold at 3.95 s against control periods of 2.7, 3.3 and 4.6 s on every held wind, brass and timpani note of 9 s or longer. No note shows a 3.95 s periodicity above its controls: Flute 1 qn 204 3.31 dB against 2.83 and 2.99; Clarinet 2 qn 292 0.75 against 0.47-0.90; Bassoon 2 qn 90 2.69 against 1.51-2.21; Contrabassoon qn 87 0.77 against 0.65-1.26; Horn 3 qn 289 1.64 against 2.24-2.84; Horn 4 qn 6 1.74 against 0.79-2.81; Timpani qn 226 2.17 against 1.94-3.16. The long string notes are re-bowed and belong to critic A.

Hall after stops (measured): after the final chord (qn 304, 353.30 s) the master is 12.7 dB down at 0.3 s and 29.7 dB down at 0.6 s; the 20 dB decay time is 0.444 s (recordings 0.43-0.58 s). No stop is cut harder than in the recordings, and none is longer.

Wetness (measured): returns against the dry sum of their family: R Strings -23.7 dB, R Brass -13.1, R Winds -12.5, R Perc -7.6. The mix is at the dry end, as in c48. No change proposed to the hall returns.

## Low end against five recordings

Share of total power in dB (measured).

| Band | c48 master | Dvořák 9 i | Brahms (4 movements) |
|---|---|---|---|
| 20-100 Hz | -16.6 | -22.1 | -7.9 to -8.9 |
| 100-250 Hz | -7.6 | all five between -6.7 and -8.8 | |
| 250-500 Hz | -5.6 | all five between -6.0 and -7.1 | |
| 177-354 Hz | -5.8 | -7.9 | -9.9 to -10.6 |

There is no build-up below 250 Hz. The third-octave bands at 198, 250 and 315 Hz are 0.8, 1.2 and 3.7 dB over the highest recording. The 315 Hz band is carried by Horn 1 (-6.6 dB of the band), the celli (-7.4) and the violas (-8.8). The key puts A flat 3, C4 and E flat 4 (311 Hz) in these bands and the recordings are in other keys, so part of the excess is tonal (inferred). I propose no change: the 315 Hz string bell of c48 already acts there, and the horn bell was rejected in c48 and I have no new evidence for it.

## Findings

### 1. Violin I solo, bars 17-18 and 21-22 (qn 47.9-54 and 59.9-65): a mono point source with no room above 1 kHz

What is wrong. The solo is the only passage of the movement where the master is mono in the range the ear uses for width. Master corr at 1-4 kHz per bar: 0.98 (bar 17), 0.98 (18), 0.97 (21), 0.83 (22). In the Dvořák recording the highest value in any window is 0.84, and 6 of 588 s are above 0.8 (measured).

Evidence (measured). The stem has corr 1.00 and R-L -5.1 dB in every band: the DIV A Close mic is one signal panned to a point. The stem carries the master within 0.4 dB above 1 kHz. R Strings under the solo stem: -13.7 dB at 250 Hz-1 kHz, -20.2 dB at 1-2.3 kHz, -26.4 dB at 2.3-4 kHz, -36.0 dB at 4-12 kHz. The hall returns are low-passed at 2.3 kHz, so no hall return can supply width there; raising R Strings would only add level below 1 kHz. A calculation shows what is missing: a decorrelated component 8.9 dB under a mono source gives corr 0.85.

Cause (inferred from mix.json and manual p.90, p.222): `tracks["Violin I solo"]["mics"]` is `{"Close": 0.664}`, a divisi patch has no other mic, and the only room it receives is the low-passed hall.

Fix: a short full-band stage return, first as a test return that does not enter the master. In `build/mix.json`:

- append to `returns`: `{"name": "R Stage", "chunk": "STRING_VERB.txt", "fader_db": -6.0, "hp_hz": 250, "set": {"irSetup": {"envelopeMode": 2, "endPos": 0.25, "decayLength": 0.25}}}` with no `post_eq` (the 2.3 kHz low-pass stays on the four hall returns only). `hp_hz` 250 keeps it out of the 177-354 Hz region. `endPos` and `decayLength` are starting values, half of the hall returns' 0.5 (build_reaper.py lines 253-255).
- set `"test_returns": ["R Stage"]`, so `tools/render_cycle.py` (lines 138-143) writes its stem to `cycles/c49/test_stems/` and keeps it out of `00_Master.wav`.
- append `{"to": "R Stage", "db": 0.0}` to `tracks["Violin I solo"]["return"]`, beside the existing R Strings entry.

`returns_job()` (build_reaper.py line 973) creates the return without rebuilding any instrument. After the render, measure the test stem against the Violin I solo stem at 1-4 kHz in bars 17-18 and compute the fader value that puts it 9 dB under the solo (the stem scales with the fader, so one render is enough). Check that the test stem falls 20 dB within 0.25 s after the last solo note (qn 65); shorten `endPos` and `decayLength` if not. Then remove "R Stage" from `test_returns`.

Acceptance: master corr at 1-4 kHz 0.83-0.90 in bars 17, 18 and 21; master R-L within 1 dB of -5.0; level change of bars 17-18 at most +0.5 dB. My offline model (synthetic decorrelated return, 250 Hz-8 kHz, 0.6 s decay; inferred) gives at -9 dB: corr 0.98 to 0.85 in bars 17-18 and 0.97 to 0.84 in bar 21, R-L -5.0 to -4.6, level +0.4 and +0.1 dB. At -12 dB it gives 0.91 and 0.90.

Alternatives. The template's ALGO GLUE return (`ALGO_GLUE.txt`, EW-TEMPLATE-PLAN section 2, listed as "test in pass 2" and never tested here) through the same test-return mechanism. The manual's own method (p.90: layer the non-divisi 1st Violins Main mic on the same notes) would put the room sound of the full section under a solo and add an Opus instance, so I do not prescribe it. The Hollywood Solo Violin with Close and Mid (p.75, MANUAL-GAPS #3) needs Dan to install it.

### 2. Oboe 1, bars 15-16, 19-20 and 45-47 (qn 42-48, 54-60, 140-152): nearly mono

What is wrong. Master corr at 1-4 kHz: 0.85 (bar 15), 0.93 (16), 0.93 (19), 0.92 (20), 0.83 (45), 0.90 (46), 0.88 (47), against the recording's maximum of 0.84 (measured).

Evidence (measured). The Oboe 1 stem has corr 0.98-1.00 in every band. Stem corr at 1-2.3 kHz against the Main volume of five woodwinds: Oboe 1 (Main 0.088) 0.98; Cor anglais (0.24) 0.92; Flute 1 (0.475) 0.92; Bass clarinet (0.29, width 0.3) 0.88; Clarinet 1 (0.528) 0.60. Master corr per band in bars 15-16: 0.65 (250 Hz-1 kHz), 0.89 (1-2.3 kHz), 0.94 (2.3-4 kHz), 0.98 (4-12 kHz). Simulating R Winds 9 dB higher, which would make every woodwind much wetter, lowers the 1-2.3 kHz value to 0.63-0.72 and barely changes the bands above 2.3 kHz, because the returns are low-passed there. The hall return is not the tool for this.

Cause (inferred from the settings and the trend above): the Close mic is narrowed to `width` 0.05 and the Main mic is 20.6 dB under it (the template value), so the stem is the Close mic alone.

Fix. `build/mix.json`, `tracks["Oboe 1"]["mics"]["Main"]`: 0.088 to 0.24 (the cor anglais value, 11.8 dB under Close). This is one Opus state rebuild of Oboe 1 only. Re-match `gain_db` (now -6.3) so the stem level in bars 15-16 is within 0.3 dB of c48. This departs from the template value on measured evidence, as EW-TEMPLATE-PLAN allows.

Acceptance: Oboe 1 stem corr at 1-4 kHz between 0.80 and 0.95; per-pitch spread of the stem R-L at most 2.5 dB (now 1.1 dB; Cor anglais at Main 0.24 has 1.8 dB, the clarinets at 0.528 have 4.2-5.0 dB, so do not go to the clarinet value); mean stem R-L within 1.5 dB of c48 (+1.6 to +2.4).

Alternative without a rebuild: add `"return": [{"to": "R Winds", "db": -8.36}, {"to": "R Stage", "db": -3.0}]` for Oboe 1 once finding 1's return exists (-8.36 is the wind group's value, repeated in case a track `return` replaces the group's). The model gives, with the stage return 12 dB under the oboe: 0.89 to 0.81 (bars 15-16), 0.92 to 0.88 (bars 19-20), 0.87 to 0.81 (bars 45-47) (inferred). A second step, if Main 0.24 is not enough, is the Mid mic (p.138, MANUAL-GAPS #4, never tried). This is narrower than the c48 proposal to move all wind and horn mics from Close to Main (16 rebuilds, open with Dan).

### 3. Clarinet 1, bars 87-88 (qn 286-292), the two D flat 5: the image jumps 7 dB to the left while the clarinet plays alone

What is wrong. Score (coda.ily): bars 85-88 E flat 5 pp dolce, D5, breath, D flat 5 pp, D flat 5 tenuto, with the clarinet alone in bars 87-88. Stem R-L per note (measured): E flat 5 qn 279.96 -2.0; D5 qn 282.94 -1.8; D flat 5 qn 286.00 -9.2; D flat 5 qn 289.00 -9.0; C5 qn 292.00 -2.4. In the master's note band: -6.0 and -5.0 at the two D flat 5 against -0.4, -3.1 and -1.1 for the neighbours.

Evidence on the cause (measured). The jump belongs to the D flat 5 samples at this dynamic, not to a controller: other D flat 5 on the same track read -0.4 (qn 189.96, CC1 56), -1.5 (qn 194.93, CC1 82), -5.5 (qn 257.44, CC1 73), -5.1 (qn 269.45, CC1 66), which does not follow CC1; both articulations in bars 87-88 (Leg Slur, Sus Non Vib) read the same. Stem corr drops to 0.55 on these notes from 0.89-0.97 on the neighbours.

Fix. A timed track pan on Clarinet 1. This is new code: add a `PAN_POINTS` table to score_config.py, for example `{"Clarinet 1": [(285.9, 0.0), (286.0, 0.5), (291.9, 0.5), (292.0, 0.0)]}`, and write it as a REAPER track pan envelope where the volume envelope is written (build_reaper.py `vol_points()` line 444, the `InsertEnvelopePoint` Lua at line 611, the mix-only rows at line 1084). The sign convention of the pan envelope and the amount must be set on a range render: the target is a stem R-L of -2 to -4 dB on both notes. With the balance model calibrated in c48 (far side at 1 - |pan|) the value is +0.5, and the two notes drop by about 4.8 dB (inferred; the model was calibrated only on a small pan change). The two notes are now 2.5-8 dB louder than their neighbours (-42.3 and -43.0 dB against -50.7, -48.4, -45.5), so the drop goes in the right direction; the level itself belongs to critic B.

Not recommended: lowering Clarinet 1's Main (0.528). It would change the image of every clarinet note and raise the track's correlation, which is now inside the recording's range.

### 4. Harp harmonics, bar 83 (qn 274-276): 8 dB to the left of the harp inside one arpeggio

What is wrong (measured). The three harmonics notes read R-L -10.0, -10.6 and -11.1 dB (pitches 68, 72, 75). The Harp track's 158 notes have a median of -2.5 dB (10th to 90th percentile -3.5 to -1.7), and the harp notes of the same arpeggio just before (qn 271-273.5) read -1.8 to -3.7. R Perc follows the dry image (-10 to -15 dB). Audibility is low: 3 notes, partly masked (master R-L -0.5 over qn 274-277.5).

Cause (inferred from mix.json and `pan_by_mic`): both tracks have `seat` -0.72, but Harp has `width` 0.3 (Close channels at -1.0 and -0.42) and Harp harmonics has `width` 0.05 (both channels near -0.72). The same seat number gives two images.

Fix. `build/mix.json`, `tracks["Harp harmonics"]["width"]`: 0.05 to 0.3, one state rebuild of a 3-note track; then re-match `gain_db` (2.2) so the stem level over qn 274-277.5 is within 0.5 dB of c48. Acceptance: the three notes read R-L -2 to -4 dB. If the width change does not reach that, keep it and add `"track_pan"` (mix-only), starting at +0.2 and set by measurement (LEARNINGS: match seats by measurement). A mix-only route without the rebuild is `track_pan` near +0.5 with `gain_db` about 5.7 dB higher (inferred from the balance model; uncertain at a pan this large).

## Checked, no finding

- The other Close-only tracks are masked (measured): Violins II div in bars 37-40 are 6-15 dB under the master per band (master corr 0.80-0.85 there comes from Flute 1); Violas div 11-22 dB under; Violoncellos div in bars 83-86 8-19 dB under (master corr 0.53-0.75). No room mic is needed for them.
- DIV A and DIV B tone against the sections at matched pitch: within a few dB per band (measured). Mute colour present (measured).
- Seating: the master's pan histogram matches the Dvořák recording (pan spread 0.346 in both) (measured).
- The remaining solo passages sit at or just above the recording's maximum of 0.84 (master corr at 1-4 kHz, measured): Horn 1 bars 8-13 and 68 (0.84-0.87), Bass clarinet bars 31-35 (0.82-0.88), Flute 1 bars 37-40 (0.83-0.88), Cor anglais bars 41-44 (0.80-0.87). No change now. If Dan hears them as dry point sources, the stage return of finding 1 is the tool; re-measure these bars after findings 1 and 2.
- Horn 1 per-note image (-7.2 to -0.1 dB) and the Contrabassoon's pitch 25 (+9.3 dB) are sample properties with low audibility; LEARNINGS records that width does not change them.

Scripts and intermediate data are in `/private/tmp/claude-501/mockup-loop/mvt2-c49-C/` (left in place).

Do not touch: the R Strings -17.97 and R Brass -4.97 faders and the other two hall return faders; the returns' 160 Hz high-pass, 2.3 kHz low-pass and IR envelope (0.5/0.5); all seats and existing track pans; horn width 0.8 and trombone width 1.0; the string mics (Close 0.5, Main 1.0); the DIV track gains and sends; the basses' 35 Hz high-pass, the 315 Hz string bell and the master EQ; the harp's seat, mics and level; Clarinet 1's mic volumes; the Con Sordino colour.

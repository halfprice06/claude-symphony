# Cycle 12, critic B: balance and levels (render under review: c11)

Method. All levels are measured on the c11 render: the dry stems 01-31 (post-fader, post-EQ) for balance, the master for decays and band levels, the mp3 for the delivery. "A" is A-weighted RMS per bar, "Z" unweighted, "K" K-weighted. "Low band" is 31.5-125 Hz. Bar b starts at qn 4(b-1). Each judgement is marked measured or inferred. I did not listen; I did not re-measure the tilt jump or the loop pulsing (cycles/c11/metrics/metrics.md has no tilt line), so nothing below is a claim about those two checks.

## Manual notes

| What the reading says (HO manual, May 2021, PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.114: on the percussion patches loudness is set by CC11 and by velocity, and velocity also selects the recorded dynamic layer (up to 16 layers in Kit 1). | Timpani; Bass drum (qn 888, 1108); Crash cymbals (qn 888, 1048, 1108). | Yes. Crash: velocity 124, CC11 127, level set after the fader (gain -4.4, vol_db -3.0 on 1046-1060). Bass drum velocity 114. Measured result: crash 11.0 to 12.2 dB under the master in its first second. |
| p.114-115: Kit 1 holds timpani and a 32-inch bass drum as short hit, long hit, roll and 1 s crescendo; Kit 2 holds the 36-inch Ludwig bass drum in the same four forms, the 22-inch Zildjian crashes long and short, and suspended-cymbal crescendos. | The Finale loads the single-instrument patches of the same instruments ("36in Ludwig Bass Drum.oib", "22in Zildjian K Crash.oib", "Timpani Hrd KS.oib"). | Yes for the hits. Bass drum: 8-10 % of the low band at 888 and 1108, -47.9 to -49.6 dB A; it does not cover. The recorded crescendo rolls are not used (MANUAL-GAPS #12); I found no balance reason to change that. |
| p.154: the Humanizer adds random note timing (0-100 ms), velocity, tuning, volume and pan. | All tracks. | Not used. Keep it off for balance: the trims below work to 1-3 dB, random velocity or volume would move them, and the render already varies by 2-5 dB on isolated bars between c10 and c11 on unchanged data. |
| p.155: the MIDI Compressor narrows the range of velocities (or of a CC) with threshold, ratio and make-up; notes under the threshold are not played. | A possible tool for uneven samples (Flute 1 G6, Oboe 1 F5, Double basses E2). | Not used, and not recommended here: the unevenness is by pitch, not by velocity, and the threshold can drop notes. `build/pitch_trims.json` is the right tool (findings 1-3). |
| p.158-159: the Automation window maps MIDI controllers to parameters; controllers can be remapped; two parameters should not share a controller by accident. | CC1 (dynamic layer) and CC11 (expression) on every track. | Yes, default mapping. The measured level steps follow the controller data: the basses' 11.5 dB step at qn 1016 (CC11 114 to 88, CC1 98 to 90, velocity 91 to 83; finding 1) and the muted trumpet's 12 dB hairpin (CC1, CC11 and velocity move together; finding 4). |
| MANUAL-GAPS #1 (p.101): on the Sustain Accent patches velocity sets the loudness of the attack and CC1 the loudness of the sustain. | The sfp at qn 592 on the brass. | Not loaded (memory). See finding 5 for whether it is needed. |
| MANUAL-GAPS #4 (p.138-139): Mid microphones in place of Close on the woodwinds, never tried. | Oboe 1 (Close 0.939, Main 0.088). | Not followed. Noted in finding 3; not proposed this cycle because the measured cause there is pitch unevenness. |

## Findings, ranked

### 1. Double basses: E2, F2, E flat 2 and F1 are weak, and the bass almost disappears under the opening of the second chorale (bars 255-260)

Where: Double basses, qn 1016-1040 (bars 255-260), and the other E2 notes (qn 804-808, 1000-1002). Tuba roles row on 1016-1032.

What is wrong (measured): at qn 1016 the score prints f for the basses after ff, with ff for cellos, tuba and bass trombone. The basses fall far more than one dynamic step. Basses Z per bar 253-262: -34.6 -33.4 -43.3 -49.8 -39.1 -33.9 -33.4 -34.9 -30.0 -30.1. Bar 254 to bar 256 is a fall of 16.4 dB; this track's median step from ff to f is 6.5 dB (K medians -33.8 and -40.3). The master's low band minus its full band is -24.7, -17.2 and -19.0 dB in bars 255-257, against -10.8 to -14.7 dB in the first chorale (bars 223-234, bar 228 excepted) and -8.4 to -12.1 dB in bars 261-264. The master's low-band level falls from -35.8 (bar 254) to -43.5 (bar 255) at the moment the chorale enters. The requirement "bass solid" is not met in bars 255-257.

Causes (measured):
- Pitch. Level of the note body with vol_db removed, Z, by pitch. Short notes, CC11 60-95: E2 -51.1 (n 16) against C2 -41.9 (n 84) and A flat 1 -44.3 (n 36). Short notes, CC11 113-127: E2 -41.1 (12), F2 -43.4 (13), E flat 2 -41.6 (11), F1 -40.0 (24) against C2 -36.8 (33) and G1 -36.5 (25). Long notes, CC11 60-95: E2 -48.8 (2), F2 -43.7 (11), E flat 2 -44.7 (7), F1 -42.1 (5) against C2 -38.2 (16) and G1 -37.5 (15). So E2 is 4.5 dB under its neighbours at ff and 7-11 dB under when soft; F2 5.5-7 dB under; E flat 2 5-7 dB under; F1 2-5 dB under. Bars 255-256 are sixteen E2 eighths; bars 259-260 are F1.
- The 87.3 Hz notch in `build/mix.json` (Double basses, -12 dB, 0.15 oct) cuts F2's fundamental and F1's second harmonic, and about 5.5 dB of E2's fundamental (82.4 Hz; computed from the filter formula, inferred). Movement I found the same after its notch and added +3 dB pitch trims for F1 and F2 (Movement I LEARNINGS, c29). The Finale's `build/pitch_trims.json` has no Double basses entry. E2's harmonics 2-3 are also 8-13 dB under C2's at f, so the E2 sample is weak without the notch as well.
- The controller step. At 1016 CC11 goes 114 to 88, CC1 98 to 90 and velocity 91 to 83. The first eighth starts before the change (body -39.5 dB in 30-120 Hz); the next on-beat eighths are at -51 dB. That is an 11.5 dB step between the first and second beat of the bar on one pitch.
- The roles row `[988, 1020, 3.0, 4]` takes the basses' +3 dB away between 1016 and 1020 and no row follows until 1032 (vol_db 2.5 at 1016, -0.5 at 1020, about 0 to 1025).
- Tuba: the row `[1016, 1032, -3.0]` lowers the only sustained instrument on the bass note while ff is printed. Tuba A per bar 255-258: -38.1 -38.7 -40.1 -41.2, against -32.3 -30.8 -29.9 in bars 261-263. I found no recorded reason for this row.

Fix:
- `build/pitch_trims.json`: add `"Double basses": {"40": 6.0, "41": 3.0, "39": 3.0, "29": 3.0, "_all_arts_pitches": [29, 39, 40, 41]}`. Keep the 87.3 Hz notch (the +3 dB on F2 leaves a net cut at its fundamental).
- `build/roles.json`, Double basses: replace `[988, 1020, 3.0, 4]` by `[988, 1032, 3.0]` (it then meets `[1032, 1116, 3.0]`).
- `build/roles.json`, Tuba: delete `[1016, 1032, -3.0]`. Leave the Bass trombone row of the same span (bass trombone A is -35.5 to -35.8 in bars 255-258, 2.5-5 dB over the tuba already).
- Optional, `build/note_trims.json`, Double basses: `"1016.0": -4.0`, so that the step from the first eighth to the next is about 5 dB and not 9.

Expected (inferred): bar 256 from -49.8 to about -41 Z, bar 255 to about -37, bars 259-260 up 3 dB. Targets for the actor's check: E2, F2, E flat 2 and F1 within 2 dB of C2, G1 and A flat 1 at the same CC11 range; basses Z in bars 255-256 between -42 and -37; master low band no more than 17 dB under the full band in bars 255-257. Re-measure the 60-100 Hz band on the F2 and E2 notes against their neighbours after the change: if it is more than +3 dB over, reduce the F2 trim before touching the notch.

This also answers the deferred item "tuba / contrabassoon -3 dB on qn 984-1056": it is not a balance improvement (measured). The tuba holds 5-7 % and the contrabassoon 1 % of the low band on 984-1056 (basses 28-37 %, cellos 40-50 %), and both are 13-20 dB A under the rest in every bar 247-264. The low band there is short of level, not over.

### 2. Flute 1 is too loud in the tuttis, most of all on G6

Where: Flute 1 in the loud tuttis; every G6 (midi 91), including the final chord (bar 278); bars 78 and 80 of the violins' F2.

What is wrong (levels measured; "too loud" by the orchestration norm is inferred): Flute 1 is the loudest of the 31 dry stems in 25 tutti bars (22, 78, 90, 91, 110, 145, 151, 158, 162, 165, 198, 199, 201-203, 239, 240, 249-254, 266, 268). Examples: bar 91 Flute 1 -23.7 against the loudest trumpet -27.8; bar 110 -24.6 against -27.7; bar 254 -27.2 against the violins -32.3. Over the 84 bars in which the master is above -24 dB A, Flute 1 minus Violins I has a median of -1.0 dB and a 90th percentile of +5.0 dB. The other woodwinds on the same measure: Oboe 1 -2.6, Clarinet 1 -4.8, Flute 2 -5.5, Bassoon 1 -8.4. By the Rimsky-Korsakov ratio recorded in the kit LEARNINGS (§13) a string section in forte is about 3 dB over one woodwind, so a single flute belongs at least 3 dB under the first violins.

Causes (measured):
- G6 on the top layer. Note body minus vol_db, A, at CC11 110-127: G6 -23.8 (n 9) against F6 -29.6 (12), E6 -29.2 (7), A flat 6 -32.9 (8), E flat 6 -31.6 (8): 5.4 to 9.1 dB over. At CC11 60-109 the excess is 2.3 to 5.2 dB. In the final chord Flute 1's G6 (-23.3) equals Violins I's three-note chord with its +5 role (-23.3) and is 15 dB over Flute 2's E6, at identical velocity (127), CC11 (124) and vol_db.
- The trims. Flute 1 K medians by printed dynamic: mf -35.3, f -36.1, ff -30.4. Oboe 1, Clarinet 1 and Bassoon 1 at mf are -42.8, -42.5, -43.2; at f -38.7, -38.8, -39.2. So Flute 1 at mf is 7 dB over the other principal woodwinds and louder than its own f. `mix.json` gives it `soft_trim_db` mf +2.5 and `dyn_trim_db` f -1.5: a 4 dB difference in the wrong direction. Flute 2 shows the same (mf -36.7, f -40.8).
- Bars 78 and 80: Flute 1 (printed mf) is the loudest stem while the violins have the F2 theme at f (-31.1 against -33.6 and -34.2; -33.7 against -34.7 and -36.9). At qn 308 and 316, on the pitch it shares with Violins I, Flute 1 is 4.2 and 3.9 dB A over them (CC11 47 to 82, CC1 100-110, vol_db +2.0). Over the whole F2 statement the two violin sections lead the sum of the other stems by 6.0, 5.1, 6.9, 2.9, 3.0, 2.1, 2.9, 0.8, 4.6, 1.3, 1.7, -2.1, 0.9, -1.7, 1.2 and 1.1 dB A in bars 67-82: a lead of 1-3 dB from bar 70 and none in bars 78 and 80.

Fix:
- `build/pitch_trims.json`: add `"Flute 1": {"91": -5.0, "_all_arts_pitches": [91]}`. Flute 2's E flat 6 (midi 87) is 6-10 dB over its neighbours (-29.0 against -39.8, -39.9, -35.1): add `"Flute 2": {"87": -5.0, "_all_arts_pitches": [87]}`.
- `build/mix.json`, Flute 1: `dyn_trim_db` f -1.5 to -3.5, ff -1 to -3; `soft_trim_db` mf 2.5 to 0.5. Flute 2: `soft_trim_db` mf 2.5 to 0.5.
- `build/roles.json`, Flute 1: add `[304, 320, -4.0]`.

Targets: Flute 1 at least 3 dB under Violins I in the median of the loud bars; not the loudest stem in any tutti bar; 4-6 dB under Violins I in bar 278; at least 2 dB under Violins I at qn 308 and 316. The violins' lead in bars 70-82 should rise by about 1 dB where the flute is the main other stem (inferred). Check after the change that Flute 1 keeps its lead where a role row raises it (`[168, 176, 4.0]`, bars 43-44); if that passage loses level against its accompaniment, add the lost amount to that row and not to the trims.

### 3. Oboe 1, carrying both oboes, is the loudest stem on E5, F5, G5 and A flat 5

Where: Oboe 1 in bars 157, 226-227, 246-247, 262 and 274.

What is wrong (measured): Oboe 1 is the loudest dry stem in bars 157 (-30.9), 226 (-28.5 against a trombone at -32.1), 227 (-29.0), 246 (-29.1 against Horn 1 -32.1, and 9.9 dB over Violins I), 247 (-28.2) and 274 (-25.5 against Horn 1 -27.1, Trumpet 1 -29.2, Violins I -32.5). On the held G5 of bars 226-227 (qn 900-905) it is at -31.8 rising to -26.6 per quarter against Violins I -34.4 to -31.6 and Flute 1 -36.7 to -35.3, so 5-7 dB over the first violins inside the first chorale. In bar 262 it equals Violins I (-26.7 and -26.4) and is 6.5 dB over Horn 1. Two oboes in unison come to about the level of one horn or of one string section by the same Rimsky ratios, so +5 to +10 dB over the first violins is outside the norm (inferred).

Cause (measured): the patch is uneven by pitch, and the a2 settings add to it (`dyn_trim_db` ff +6 and the +3.01 dB unison compensation in vol_db). Note body minus vol_db, A, at CC11 110-127: F5 -30.3 (n 11), A flat 5 -30.4 (5), G5 -32.0 (10), E5 -32.3 (9) against C5 -40.2 (10), D5 -40.3 (9), E flat 5 -37.8 (9), F sharp 5 -37.5 (3), A5 -36.5 (3). At CC11 60-109: F5 -36.6 (11), A flat 5 -37.0 (3), G5 -39.7 (6) against C5 -45.5 (13), D5 -43.9 (12), E flat 5 -44.8 (10). F5 is 7-10 dB over C5, D5 and E flat 5 in both ranges, so the trim can apply at every dynamic.

Fix: `build/pitch_trims.json`: add `"Oboe 1": {"77": -5.0, "76": -3.5, "80": -3.5, "79": -2.5, "_all_arts_pitches": [76, 77, 79, 80]}`. If Oboe 1 is still over Violins I by more than 2 dB on the held G5 of bars 226-227, lower `dyn_trim_db` ff from 6 to 4.5 in `build/mix.json`. Measure the same four pitches on Oboe 2 before copying the trims to it.

Targets: E5, F5, G5 and A flat 5 within 3 dB of C5, D5 and E flat 5 at the same CC11 range; Oboe 1 not the loudest stem in bars 226, 227, 246, 247 and 274.

Side effect (inferred): bar 274 holds the F5 and bar 275 the E5, so bar 274 falls about 0.35 dB more than bar 275 in the mix. That removes about half of the "bar 275 under bar 274" item (finding 6).

### 4. Muted trumpet against the cor anglais (bars 171-186): the trumpet's hairpin is twice as wide as its partner's

Where: Trumpet 1 ("Mute Sus" row, qn 680-792) and Cor anglais, bars 171-183 (qn 680-732).

What is wrong (measured): the recorded target is the trumpet about 3 dB A under the cor anglais. Trumpet 1 minus cor anglais per bar: 171 -0.9, 172 -1.1, 173 -2.3, 174 -5.6, 179 -4.2, 180 -3.7, 181 -3.0, 182 +4.0, 183 -6.6. On the printed hairpin (both parts: crescendo from qn 719 to mf at 724, decrescendo from 725 to p at 728) the trumpet rises 12.2 dB (bar 179 -53.5 to bar 182 -41.3) and falls 10.6 dB into bar 183; the cor anglais rises 6.5 dB (bar 179 -49.3 to bar 181 -42.8) and falls 2.5 dB. In bar 182 the two play the same notes and the trumpet is 4 dB over; one bar later it is 6.6 dB under.

Cause (measured): Trumpet 1 is a `CC1_DYN_TRACKS` track, so the hairpin moves its CC1 (42 to 74 to 36), its CC11 (46 to 72 to 46) and its velocity (53 to 73 to 53). The cor anglais keeps CC1 at 100-110 and moves CC11 only (54 to 81 to 48-62). I did not trace the cause of bar 174 (-5.6); the row below corrects its level only.

Fix (values inferred from the measured differences), `build/roles.json`, Trumpet 1:
- replace `[680, 712, 2.0]` by `[680, 692, 2.0]`, `[692, 696, 4.5]`, `[696, 712, 2.0]` (bar 174 from -5.6 to about -3.1);
- add `[724, 728, -6.0]` (bar 182 from +4.0 to about -2.0) and `[728, 732, 3.5]` (bar 183 from -6.6 to about -3.1); the second row meets the existing `[732, 792, 2.0]`.
Bars 179-181 are at -3.0 to -4.2 and need no row.

A cleaner fix needs a tool change: in the CC1 function of `tools/score_to_parts.py` (the `CC1_DYN_TRACKS` branch, near line 4208) hold CC1 at one value (for example 56) over the "Mute Sus" span of `ART_SPANS`, so that the hairpin moves CC11 only, as on the cor anglais. `CC1_HOLD` cannot be used as it is, because it applies to the whole track. I did not test this (inferred).

Target: trumpet 2-4 dB under the cor anglais in every bar of 171-183.

### 5. The sfp at qn 592 has no accent: its first 0.1 s is under the ff before it

Where: bar 149, qn 592; Trombones 1-2, Bass trombone, Tuba, Horns 1 and 3, strings; Trumpet 1's ff accent on the same beat.

What is wrong (measured): master level (unweighted) -19.0 dB in the 0.4 s before the onset, -19.9 in the first 0.1 s, -20.5 from 0.1 to 0.25 s, -23.6 from 0.25 to 0.5 s, -25.2 from 0.5 to 1.0 s. The accent is 0.9 dB under the preceding ff, and the peak of the 10 ms envelope is at +0.265 s. Per stem, level before / first 0.1 s / 0.1-0.25 s / 0.25-0.5 s, and envelope peak:
- Trombone 1 -28.4 / -30.2 / -32.3 / -33.7, peak +0.085 s: the loudest sfp stem, and its front is 1.8 dB under its level before in spite of the +3 dB shape.
- Horn 1 -32.7 / -32.8 / -34.5, peak +0.080 s. Violins I -31.8 / -32.9 / -36.3. Violas -31.9 / -33.9 / -35.2. Double basses -31.2 / -32.9 / -37.1. Violoncellos -30.8 / -30.8 / -29.8.
- Late bodies, with no shape in c11 except Horn 3: Horn 3 -33.6 / -31.5 / -33.0 / -35.2, peak +0.275 s; Trombone 2 -31.9 / -31.5 / -30.0 / -35.2, peak +0.240 s; Bass trombone -33.2 / -33.3 / -33.5 / -35.1, peak +0.270 s; Tuba -37.2 / -37.4 / -35.2 / -39.7, peak +0.225 s. From 0.25 to 0.5 s these four are only 1.6-3.3 dB under their ff, so they also reach the p late.
- Trumpet 1 (ff accent, no sfp) -30.3 / -36.9 / -33.8 / -35.7, then -29.7 from 0.5 to 1.0 s: its front is 6.6 dB under its level before. Trumpet 2 has a clear accent (-35.4 / -29.2 / -27.4).
The c11 shapes end at 592.35 (+0.125 s); the four late stems reach their sample body after the shape has ended. The shapes of +3 to +5 dB are too small: with them most fronts are at or under the level before.

Fix, `build/score_config.py`, `LEVEL_SHAPES` at 592:
- Early stems, same shape as now, `[(591.95, 0.0), (592.0, d), (592.22, d), (592.35, 0.0)]`: Trombone 1 d 3 to 6, Horn 1 3 to 6, Violins I 3 to 5, Violas 3 to 5; add Trumpet 1 d 6 and Trumpet 3 d 4.
- Late stems, a front followed by a short cut: `[(591.95, 0.0), (592.0, d), (592.22, d), (592.4, -4.0), (592.7, -4.0), (592.95, 0.0)]` with d 6 for Horn 3 (now 4) and Trombone 2, d 5 for Bass trombone and Tuba. The cut covers +0.14 to +0.25 s, where their bodies arrive, and ends before the roles rows that start at 593.

Expected (inferred, from a power sum of the stems' first 0.1 s): master first 0.1 s about 1.5 dB over the level before. Targets: first 0.1 s at least 1 dB over the -0.5 to -0.1 s window; 10 ms envelope peak within the first 0.12 s; level from 0.5 to 1.0 s unchanged (-25.2). The shapes are post-fader and broadband, so each stem's own spectrum at the attack does not change (inferred); the actor's tilt-jump metric must confirm that the p90 stays under +3.

Answer on "Sus Accent MAX" (p.101): not needed this cycle. Try the shapes above first; they cost no memory. If the master's first 0.1 s is still under +1 dB, load the row on Horn 3 and Trombone 2 only (the two loudest of the stems whose body arrives at +0.24 to +0.275 s), with velocity 100 or less, because Dan heard it as harsh at 105-110 in Movement II, and only if memory allows (REAPER is at 45 GB against a limit of about 44).

### 6. The fff of bar 263 is not louder than the bar before it; bar 275 is under bar 274

Where: qn 1044-1052 (bars 262-263), Trumpet 1 and Horn 3; qn 1092-1100 (bars 274-275).

What is wrong (measured): all parts reach fff at qn 1048 after a crescendo. Master per bar 261 / 262 / 263: Z -15.2 / -12.8 / -13.3; K -14.5 / -12.0 / -12.3; A (bars 262, 263) -14.5 / -14.9. The crescendo reaches its top at qn 1044, one bar early (master per 2 qn from 1040: -17.6, -17.2, -14.4, -14.7, -14.3, -15.6), and the fff bar is 0.3-0.5 dB under bar 262. Stems, bar 262 / bar 263: Trumpet 1 -20.8 / -25.3 (falls 4.5 dB at the fff); Horn 3 -24.9 / -26.5; Violins I -26.4 / -30.3 (tremolo chord to eighths); Violas -28.7 / -31.8. In bar 262 Trumpet 1 is 4.1 dB over every other stem.

Cause (measured): Trumpet 1's B4 at 1043.85 (velocity 109, vol_db 5.8-8.4) is on a loud pitch and its C5 at 1047.85 (velocity 127) on a weak one: at CC11 110-127, C5 is -30.9 (n 13) against B4 -27.1 (4) and D flat 5 -24.2 (4). The roles row `[1032.0, 1047.5, 2.0, 1.0]` ends before the fff, and `dyn_trim_db` is 8.1 at fff against 9.3 at ff. Horn 3's G4 at 1043.85 is at velocity 127 one bar before the fff.

Fix:
- `build/note_trims.json`: Trumpet 1 `"1044.0": -3.0` and `"1048.0": 2.5`; Horn 3 `"1044.0": -2.0`.
- If bar 263 is then less than 1 dB over bar 262: `build/roles.json`, Trumpet 1, change `[1032.0, 1047.5, 2.0, 1.0]` to `[1032.0, 1054.0, 2.0, 1.0]`.
Expected (inferred, power sums on the dry stems): bar 262 A about -15.2, bar 263 about -14.6 with the note trims and -14.2 with the longer row. Target: bar 263 at least 1 dB over bar 262 in A and Z, and Trumpet 1 no more than 3 dB over the next loudest stem in bar 262 (estimated 2.6 dB after the trims).

Bar 275 (measured): the delivery has bars 273-278 at -18.0, -18.4, -19.0, -18.2, -15.8, -14.3. Of the 0.6 dB between bars 274 and 275, 0.4 dB is in the mix and 0.1-0.2 dB in the ride. The tutti hairpin that starts at qn 1096 begins from a lower level on the held winds and brass (Horn 1 falls 4.1 dB and Oboe 1 3.3 dB from bar 274 to bar 275; Horn 1 vol_db 4.77 to 0.77 and velocity 111 to 91), and Oboe 1's loud F5 lifts bar 274. Fix: finding 3 first (about 0.35 dB, inferred). If bar 275 is still under bar 274, add `[1096, 1100, 2.0, 2]` to Horn 1, Horn 3 and Trombone 1 in `build/roles.json`; the row fades over its last 2 qn, so the end of the crescendo keeps its values. This is the smallest item in the report: a crescendo that starts 0.6 dB lower is within what players do.

## Answers to the coordinator's cycle 12 items

Wetness (measured on the master, 20 ms RMS): time to -20 dB is 0.46 s (qn 5), 0.45 (21), 0.35 (101.75), 0.48 (373.75), 0.29 (450), 0.37 (662) and 0.43 s on the final chord from qn 1113 (0.32 s from 1113.5). All are within the 0.50 s ceiling and none is longer than in c10. The final chord's decay fit gives RT60 1.16-1.22 s. A fit on -15 to -35 dB at qn 5 and 21 gives 1.8-1.9 s, the same as in c10; that fit window differs from the loop's, so compare it with the loop's own number before acting on it. The mix is not too dry: three stops (qn 5, 21, 373.75) drop 12.6-13.3 dB by +0.3 s, less than the 15 dB of Movement I's rule.

Level or timing drift after --midi-only (measured): none found. On unchanged bars the c11 minus c10 stem level has a median of 0.00 dB on all 31 stems (10th and 90th percentiles within -0.2 and +0.1). Many bars are sample-identical (Double basses 171 of 183, Violas 142 of 182, Trumpet 1 51 of 55). Isolated bars differ by 2-5 dB on rebuilt and on untouched tracks alike (Violins II bar 266 +5.4; Violins I bar 222 -3.8, not rebuilt; Oboe 1 bar 160 -1.9, not rebuilt), which is render variation, not a moved track. Limit of the check: a stale state that was already in c10 would not show.

Flute 2 at qn 650: choose the re-attack. Measured: Flute 1's pitch changes +1 to +31 ms after the beat, Flute 2's at +151 ms with a lead of 0.9 qn and velocity 100; Flute 2's old pitch starts to fade 200 ms before the beat and the two pitches overlap for about 350 ms. The transition sample itself is slow, so more lead only lengthens the overlap (inferred). Velocity 122 gives at most about 24 ms (1.1 ms per step, kit LEARNINGS) against 75 ms or more needed, and the kit records velocity as unreliable for timing. Re-attack on Flute 2 only: end the 648 note 0.01 qn before 650 and play 650 on the Sus MAX row with a 0.04 s lead and continuous CC11; Flute 1 keeps the slur on the same pitch and covers the join. Check: Flute 2's pitch change within 40 ms of Flute 1's, and the dip of the flute pair at 650 under 3 dB.

Bassoon 1 at qn 464 (measured): the pitch changes about 80 ms before the beat (new note played at 463.58, velocity 80, note trim +2.0); the level dips 6 dB from -80 to +80 ms and the new note is 10 dB under its body at the beat, within 3 dB of it at about +200 ms. The "+134 ms" is a late level, not a late pitch. Proposal (inferred): reduce the lead to about 0.25 qn and add a shape `LEVEL_SHAPES["Bassoon 1"]` of +3 dB from 463.8 falling to 0 at 464.6; or re-attack as for Flute 2. Do not use velocity.

The 315 Hz hump in J (measured): it is the chord, not a resonance. Shares of the 281-355 Hz band over qn 536-600: Horn 3 29.5 %, Violas 16.1 %, Bass clarinet 7.9 %, Trombone 2 7.5 %, Tuba 5.0 %, Violoncellos 4.5 %. At 584-600 (8.9 and 6.8 dB) Horn 3 (a2), Trombone 2 and the violas hold D4 (294 Hz), Trombone 1 F4, the bass clarinet G2 (third harmonic 294 Hz) and the tuba G1 (sixth harmonic). At 552-560 (7.5 dB) one Horn 1 line gives 74 %. A string-family bell at 315 Hz would reach only the violas' 12-20 % and would cut a written fundamental; Horn 3 -2 dB on 584-600 gives about -0.6 dB. Recommendation: no bell. Either accept 6-8 dB at 584-600 or compute the metric only where no sustained D4-F4 chord tone is doubled.

Leg Slur Exp on cor anglais and Oboe 1: outside this lens; I measured nothing for or against it. The cor anglais's levels in bars 171-184 are steady (-49.3 to -42.8) and give no balance reason to change its patch.

New in c11, judged by measurement:
- The basses' gap dips before the beats work: in 30-120 Hz at 1017-1023 the level before each beat is -71 to -76 dB and the body after it -51 dB. They cost 0.7-0.9 dB of bass level in bars 273-276 and 0.0-0.8 dB in bars 199-210. Keep.
- The sf shapes at 592 work on Violins II (+2.4 dB over the level before) and Horn 3 (+2.1); on the other stems the front stays at or under the level before. Keep the method, raise the values (finding 5).
- The violas' chord-repeat gaps on 840-872 separate the chords: dips of 13.6, 13.3, 7.7 and 15.5 dB at the new bows and 4.5 to 11.5 dB at the louré repeats. Keep.
- The ride after the subito p at bar 42 works: the step from bar 41 to bar 42 is 8.9 dB in the delivery against 9.2 dB in the master. The delivery's gain over the master is +5.8 dB in bar 41 and +6.1 in bar 42, and it rises only afterwards (+8.7 in bar 43, +10.5 in bar 44). Keep.

Other passages of the lens (measured, no action proposed): Trumpet 1's solo, bars 51-66, leads the rest by a median of 5.2 dB A (lowest bar 63, +1.9). The bassoon solo leads by 9.4, 9.2, 13.2, 5.5, 2.9, 3.8 and 2.3 dB in bars 115-121; in bar 122 it is 3.6 dB under the rest (Clarinet 1 -53.4, Bassoon 1 -55.3), and I did not check whether the clarinet takes the line there. The bass theme of bars 27-34 is over the violin and flute figure by 2.7-7.0 dB K in every bar (A: -1.3 to +5.4). Theme B in the trumpets, bars 211-216, is within 1 dB of the sum of all other stems. In the first chorale the brass are 7.6 and 9.4 dB over the violins' tremolo in bars 224-225, and about 8 dB in bars 255-256 of the second; that is above the recorded +5 to +6 dB, and I leave it because the bass under the second chorale (finding 1) should be corrected first. The low instruments, timpani and bass drum are 10-19 dB A under the rest in every bar of 271-279 and do not cover. The harp at qn 488-512 was cut 6 dB in c10 so that the cello tune leads; its note peaks (20 ms) are 0.8 and 4.4 dB over the rest in bars 123-124 and 1.7-4.9 dB under it in bars 125-128. If Dan hears it as too far back there, reduce the note trims from -6 to -3 on 496.0-511.5. Trumpets 2 and 3 at p are 7 dB under Trumpet 1 at p (-53 against -45.8 K); no passage was found where that is audible as a fault.

Do not touch: the Trumpet 1 solo balance of bars 51-66; the crash cymbal level (11-12 dB under the master in its first second, 21-22 dB after 1 s); the bass drum and timpani levels at bar 223 and in bars 271-279; the four returns and their sends (every stop within 0.50 s); the bar 42 ride row; the basses' gap dips before the beats; the violas' chord-repeat gaps (0.12 s new bow, 0.06 s louré); the 87.3 Hz notch on the basses (correct its side effect with pitch trims, finding 1); no 315 Hz bell; the Bass trombone row on 1016-1032; the harp's -6 dB note trims on 488-495.5; the Humanizer and the MIDI Compressor stay off.

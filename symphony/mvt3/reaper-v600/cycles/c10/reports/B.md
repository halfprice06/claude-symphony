# Critic B, cycle 10 (render c09, after its stem fix): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 49-52, 202-204, 208, read in full; second reading of the c04 B row)

c04's B report read these pages on the c03 render. Each of its notes is checked again on c09 (`build/mix.json`, `build/parts.json`, the c09 stems).

| Page | What the manual says | Where it applies | Does c09 follow it? |
|---|---|---|---|
| p.49 | "Load with Effects off" loads instruments without Opus's convolution reverb, so the reverb can be supplied by plugins in the DAW. | Every track. | Yes, and more fully than in c04. Since c06 `reverb.opus_off` removes the Opus hall on all 31 instances, and four Spaces II returns supply the hall (R Strings, R Brass, R Winds, R Perc, rendered as stems 32-35). |
| p.49-51 | Multi-outputs: each mic position goes to its own DAW channel, so each mic can send a different amount to a Spaces II reverb bus. | Each instance has one stereo output. The sends are post-fader from the instrument track, so every loaded mic sends the same amount. | Not used, and no finding here needs it. Depth comes from the Close/Main mix inside Opus (`pan_by_mic`, mics per track) plus register sends. A per-mic send would need 2-3 extra REAPER tracks per instance. The levels below are all offsets on one span, one voice or one dynamic, so mic routing cannot fix them (as in c04). |
| p.51 | Set the number of plugin stereo busses (Preferences > Audio Engine) before using multi-outs. | Not applicable (stereo out). | Not applicable. |
| p.52 | Multi-timbral use: up to 16 instruments per Opus instance, MIDI channels auto-incremented. | 31 instances, one per track. | Not used. It would not change any level and would not save sample memory (c04, unchanged). |
| p.202-203 | De-Esser, Level Amp (fixed compressor with make-up gain), Limiter (ceiling -24..0 dB, release 1-400 ms), Limiting Amp. | No insert dynamics on any track. The only limiter is in `tools/deliver_master.py` (about 0.8 dB on the loudest peak in c09). | Yes. A per-track compressor or limiter would flatten the printed dynamics that CC1/CC11 and the trims produce, and finding 2 depends on those dynamics. Keep them off. |
| p.204 | SSL Bus Compressor (threshold, ratio 2/4/20:1, attack, release, make-up); SSL Channel Strip (input gain, phase invert). | Not used. Loudness range comes from the delivery ride: master LRA 22.0 LU, delivered 14.7 LU. | Yes. A bus compressor would lift exactly the soft accompaniments that findings 3 and 4 measure as too close to their solos. Not recommended (as c04). |
| p.208 | SSL Transient Shaper: Gain, Amount, Speed. **Invert** subtracts the detected attack, leaving more body. Usable on the instrument or on a mic channel. | Not used. New since c04: c09 left the brass accent fronts 3-8 dB duller than the plain notes (CARRYOVER item 5). | Not applied, and it should not be. A positive Amount raises the attack of every note on the track, not only the accents, which is the bite Dan rejected (BRIEF item 4). Invert would make the accents duller still. The accent problem belongs to the rows and the CC timing (critic A). |

MANUAL-GAPS.md was read. #4 (Mid mics) is still the only open item that touches depth and level, and it would move a whole track at every dynamic, so it is not the fix for any finding below. #6 (CC16 reset) is used for the basses. #12 (crescendo rolls) is not needed for balance: every timpani roll is 15-21 dB under the master and ranks 12th or lower (measured, below).

## Method

- Data: the c09 stems 01-35 and the master in `cycles/c09/render/` (the stem-fixed set), with `build/parts.json` for the tempo map, notes and lanes (it carries the stem-fix rows). There is no render offset.
- Framing: a 4096-point STFT with a 25 ms hop. Power is the stereo sum, K-weighted (BS.1770 two-stage curve applied as a power response) and A-weighted. Band powers are kept for 20-100, 30-150, 100-250, 250-500, 500-2k, 2-5k and 5-12 kHz, and for the 250, 315 and 400 Hz third octaves. All levels below are K-weighted unless marked. They are on my own scale, so compare differences, not absolute values with metrics.md.
- Printed dynamics per staff come from `build/mockup-events.tsv`, with sfp / fp read as p and sf marks skipped.
- Note bodies run from the score onset + 0.15 s to the end - 0.05 s, for notes of 0.3 s or longer.
- Pair statistics are per beat (1 qn), counting only beats where both tracks sound under the same printed dynamic; I give the median.
- Balance norms:
  - Rimsky-Korsakov, Principles, PDF p.51: "In loud passages the horns are only one-half as strong: Trumpet = Trombone = Tuba = 2 Horns". A wind equals a string section at p; a string section is about 3 dB over a wind at f. So at f/ff, with one wind as 0 dB: a string section +3, a horn +3, a trumpet or trombone +6.
  - Accompaniment sits 3-7 dB under the melody it supports.
- Dan's checks through this lens:
  - Item 5 (rolls): table in the last section; no roll covers.
  - Item 4 (accents): every fix below is a level change in the volume envelope, so no accent's 2-5 kHz front or spectral tilt changes.
  - Item 7 (loop pulse): no fix changes a note length. The held note in finding 1 lasts 2.7 s, under one 3.95 s loop.
  - S1 and S2: no timing change.
  - S3: every role or trim below starts on a fresh onset of its own track or in a rest. None is a fast fall under a sounding chord.

## 1. Bars 255-258 (qn 1016-1032): the trumpets' chorale motto in doubled values is 6.4 dB under the horns' tune and 3.4 dB under the string tremolo; a c05 cut of -3 dB is the main cause (measured)

**Where.** Trumpet 1 (Tpt 1-2 a2, ff) holds the chorale motto in whole notes: G4 (1016-1024, tied), E5 (1024), D5 (1032), C5, B4, C5. The flutes and oboes join it from 257. Against it, Horns 3-4 a2, Violins II, violas and celli play Movement I's theme ff "espress.", and Violins I hold a tremolo chord. The brief names this as the chorale's last statement.

**Evidence (measured, K).**

| qn | Tpt 1 | Hn 3 (a2) | Violas | Vln II | Vln I (trem.) | Celli | B.tbn | Tuba |
|---|---|---|---|---|---|---|---|---|
| 1016-1024 | -32.5 | -26.1 | -26.5 | -28.0 | -29.1 | -28.5 | -33.8 | -34.9 |
| 1024-1032 | -27.5 | -23.9 | -27.7 | -27.5 | -28.9 | -30.5 | -34.0 | -37.3 |

- On the G4, Trumpet 1 is the quietest pitched part except the bass trombone and tuba. It is 6.4 dB under Horn 3, 6.0 dB under the violas and 3.4 dB under the Violins I tremolo.
- It also fades through the tied note: -31.1, -32.3, -33.0, -34.3 dB per half bar, 3.2 dB in 2.7 s, with CC1 flat at 108. This is the ff sample's own decay; nothing in the data shapes it.
- At 259-262 (qn 1032-1047.5), with c09's +2 dB row, Trumpet 1 is the loudest stem (-23.6 dB). The motto is therefore inaudible for its first two bars and then jumps to the top at 259.
- Cause: `build/roles.json` Trumpet 1 has `[1016, 1032, -3]`, from c05 B #1. That finding read the trumpets' whole notes as "held accompaniment" covering the F2 phrase. Since then, the phrase (Hn 3 + Vla + Vln II + Vc) has come to sit about 6 dB over Trumpet 1, and its power sum is -20.5 dB at 1024-1032. The cut now hides the motto rather than clearing the tune.
- Rimsky's ratio puts a2 trumpets at least level with a2 horns at ff.

**Fix.**
- `build/roles.json`, Trumpet 1: delete `[1016, 1032, -3]`. Trumpet 1 rests in 253-254, so nothing chains onto this row. Check the new-minus-old envelope extremes anyway (Movement I LEARNINGS c48).
- Add a level shape that offsets the G4's decay: 0 dB at 1016.0, +2 dB at 1023.5, back to 0 at 1024.0. Use the shape form, not a 4-value role row, because of the c47 ramp-before-a rule.
- Expected: Trumpet 1 about -29.5 / -24.5 dB in the two bars, or -27.5 / -22.5 with finding 2. That is level with Horn 3 (±1.5 dB) and 2-4 dB under the phrase's power sum. Re-measure against the Violins I tremolo; the target is the trumpet 1-3 dB over it.

## 2. At ff the trumpets are no louder than one horn: the heavy brass sits 2-3 dB under the orchestration norm in every ff brass tutti (measured; the norm is from the book)

**Where.** Trumpets 1-3 at every printed ff: bars 27-42, 147-150, 151-170, 199-210, 211-218, 247-270 and 273-277. The fff spans (223 and the final chord) are close to the norm and are not part of this finding.

**Evidence (measured).**
- Per-beat pairs at the same printed dynamic (median, n beats):
  - Horn 1 minus Trumpet 1: ff +0.3 (62), fff -1.5 (14), f -1.3 (27).
  - Horn 3 minus Trumpet 1: ff +1.1 (49).
  - Horn 1 minus Trumpet 2: ff +0.6 (41).
  - Horn 3 minus Trumpet 3: ff +1.6 (41).
  - Trombone 1 minus Trumpet 1: ff +1.0 (49).
  - Horn 1 minus Oboe 1: ff +3.5 (124). Horns sit right against the winds.
  - Violins I minus Horn 1: ff +0.8 (101). Horns sit right against the strings.
  - Trumpet 1 minus Flute 1: ff +4.0 (80). The norm is +6.
- Section sums in ff tutti chords. The norm for 4 horns against 3 trumpets is -1.8 dB.

| qn | horns minus trumpets | trombones minus trumpets |
|---|---|---|
| 584-592 (147-148) | -0.2 | +2.8 |
| 792-808 (199-202) | +1.8 | -1.6 |
| 888-892 (223, fff) | +1.1 | -0.9 |
| 1032-1048 (259-262) | +0.5 | +1.1 |
| 1100-1108 (276-277) | -2.2 | -0.4 |
| 1108-1113 (278) | -2.7 | -0.4 |

- In the ff stop chord of 147-148, the three trumpets are the three quietest brass stems (-28.4 / -29.3 / -29.4 dB, against Trombone 1 -24.8 and Horn 3 -27.0).
- Per-family note medians at ff: horns -28.0, trumpets -30.1, trombones/tuba -29.5, winds -34.3, strings -30.9 dB. At p the families agree within 2.4 dB (winds -46.5, horns -47.9, trumpets -47.2, low brass -48.0, strings -45.6). So p sounds like p in every family, but at ff the trumpets fall behind.
- c04 B measured Horn 1 minus Trumpet 1 at -1.5 dB at ff. The horns have since gained (c08 chorale/EQ gains, c09's +1.0 make-up with the 315 Hz bell) while the trumpets' ff trims stayed.
- What it means for a listener (inferred): the ff tuttis are horn-coloured on top. The trumpets' brilliance, which the Finale's fanfare writing relies on, is missing.

**Fix.**
- `build/mix.json` `dyn_trim_db.ff`, +2.0 dB on each trumpet: Trumpet 1 7.3 -> 9.3, Trumpet 2 8.0 -> 10.0, Trumpet 3 11.1 -> 13.1. Leave f and fff alone.
- This is a volume-envelope change only, so the accent tilt check (2-5 kHz front against body) is unchanged.
- Targets after the render:
  - Horn 1 minus Trumpet 1 at ff about -1.7 dB.
  - Horns minus trumpets in the ff tutti chords between -3 and -1 dB.
  - Trombones minus trumpets within ±2 dB.
  - 223 and 278 still the loudest bars; delivery limiter under 3 dB (now 0.8).
- Check that no ff-to-sub. p change makes the trim step under a sounding trumpet note. In bars 217-219 the trumpets rest before the sub. p, so I expect none.

## 3. Bars 43-50 (qn 168-200): the motive-x solos (Fl 1, Cl 1, Ob 1, p) open under or level with the Violins I pp harmonic (measured)

**Where.** Flute 1 (168-176), Clarinet 1 (176-184) and Oboe 1 (184-192), each "1." p with a +4 dB role. They play over the B flat pedal chord: strings pp, Violins I "harm." on B flat 5, Horn 4 pp "dolce".

**Evidence (measured).**
- Over the frames where each solo sounds, the accompaniment re the solo is:
  - Flute 1: Vln I -2.4, Vla -4.5, Vc -5.1, Vln II -5.2, Hn 4 -6.9 dB.
  - Clarinet 1: Vln I -4.3, others -6..-9 dB.
  - Oboe 1: Vln I -3.0, others -6..-10 dB.
- Per beat, the solos' first beats sit under the harmonic:
  - Flute 1 -47, -47, -47 dB against Vln I -46..-45.
  - Clarinet 1 -44, -44, -43 against -44..-46.
  - Oboe 1 -47, -46, -45, -44 against Vln I -43, -43, -42, -44.
  - The solos clear the harmonic only at their peaks (-39..-37 dB).
- Violins I hold B flat 5 on Sus MAX with two re-bows (178.95, 188.76). The fitted re-bow fills add +5..+7 dB for about 1.5 qn after each re-bow, during the clarinet and oboe solos. The fills keep the note flat at -44 ± 1 dB, so the -3 dB role has no effect there.
- A string harmonic is a thin, soft sound; a Sus MAX B flat 5 is a full violin note in the flute's register (inferred). At pp the strings already measure 3.3 dB over the winds' pp (note medians -48.3 against -51.6).

**Fix.**
- `build/roles.json` Violins I: `[168, 200, -3.0]` -> `[168, 200, -8.0]`. The re-bow fills stack on top of the role, so leave them unchanged. The role starts on the note's onset at 168, with the existing -1.5 ramp from 167.75.
- Expected: Vln I about -49 dB. Each solo's opening is then 2-5 dB over it and its peak 7-11 dB over, and the harmonic stays at the level of the other pp sections (-47..-50).
- If the clarinet's and oboe's openings still read under 3 dB, the next step is Violins II `[176, 192, -2.0]`, not more solo role.

## 4. Bars 125-128 (qn 496-512): the harp's p arpeggios stand 2-5 dB over the violas' F2 entry and the bassoon / cello counter-line, because the harp trims stop at 496 (measured)

**Where.** The G-major F2 hand-over. The score's own note (dev.ily c033, c038) says: "it is passed upward Vc (123) -> Vla (124) -> Cl 1 (126) -> Vln I + Fl 1 (128) ... the harp keeps the arpeggios", with the harp pp/p under the hand-over. Violas "arco, unis., sul D" p from 495; Bassoon 1 "dolce" p doubling the celli (pp dolce) from 496.

**Evidence (measured).**

| bar | 123 | 124 | 125 | 126 | 127 | 128 |
|---|---|---|---|---|---|---|
| Harp | -48.8 | -48.6 | -41.3 | -41.2 | -41.5 | -39.8 |
| Violoncellos (melody 123-124) | -48.2 | -50.5 | -54.6 | -55.2 | -50.1 | -51.7 |
| Violas (melody from 124.75) | | -56.0 | -44.7 | -43.3 | -46.2 | -49.9 |
| Bassoon 1 (counter-line) | | | -45.2 | -49.1 | -47.2 | -47.3 |

- `build/note_trims.json` Harp has -4 dB on each onset 488.0-495.5 and nothing after it. At 496 the harp rises 7.3 dB, on the same velocities (64/58), while the melody moves to the violas.
- Over the frames where the violas sound (494-508), the harp is +3.2 dB over them, Bassoon 1 -2.5 and the celli -7.9.
- In 123-124 the harp is already level with the cello melody (+0.6 / -1.9 dB), so it needs a little more cut there too.

**Fix.**
- `build/note_trims.json` Harp: -6 dB on every onset from 488.0 to 511.5 (the half-qn arpeggio onsets). That means 488.0-495.5 go from -4 to -6, and 496.0-511.5 are new rows.
- Use the plucked-note step shape (full value at onset - 0.01 s, kit LEARNINGS §13). Leave 512-520 alone, so the harp's crescendo with the tutti into 131 (dev.ily c038) starts from the trimmed level.
- Expected: harp about -47.3 dB in 125-127, so the violas are 1.3-3.9 dB over it and Bassoon 1 level with it. In 123-124 the cello melody is 0-2.6 dB over the harp.

## 5. Bars 234-238 (qn 932-952): Horn 4's p E3/F3 is 9-11 dB louder than Horn 3 in the same chord and covers Clarinet 1's p counter-line (measured; cause by pitch inferred)

**Where.** Horns 3-4, p whole-note chords under the Violins I "molto cantabile" tune (Q, Poco più mosso). Clarinet 1 has a p solo counter-line from 236. Both horns use the 1FH KS Master with identical CC1/CC11 lanes, velocity 53 and volume envelope.

**Evidence (measured).**

| onset | Horn 3 (pitch, K) | Horn 4 (pitch, K) | Hn 4 - Hn 3 |
|---|---|---|---|
| 932 | G3 -50.4 | E3 -41.2 | +9.2 |
| 936 | G3 -52.2 | E3 -41.5 | +10.7 |
| 940 | A3 -50.5 | F3 -39.3 | +11.2 |
| 944 | A3 -49.5 | F3 -38.2 | +11.3 |
| 948 | D4 -43.6 | G3 -50.3 | -6.7 |

- A-weighting gives the same gaps (+10.6..+11.8 dB).
- Over 936-952, Horn 4 (-40.9) is louder than the harp's p eighths (-42.2), the violas (-42.8) and Clarinet 1's solo line (-45.2). Horn 3 (-48.0) is barely there. The chord is heard as a single low horn note, which then drops out at 948 when the voices swap register.
- Pooled residuals of all four horns' soft notes against each track's median at the same dynamic: G3 -6.8 dB (16 notes), A3 -3.2, F3 +3.7. This points to a pitch-dependent sample level on the 1FH Sus row at the p layer (inferred; kit LEARNINGS §13 lists the same kind of spread for Solo Horn).

**Fix.** `build/note_trims.json`, per note, not as pitch trims, because these pitches also appear at f and ff (kit LEARNINGS §13 on pitch trims set at soft dynamics):
- Horn 4: "932.0": -6, "936.0": -6, "940.0": -8, "944.0": -9.
- Horn 3: "932.0": +2, "936.0": +4, "940.0": +3, "944.0": +2.
- Targets: both horns at -47..-48 dB, 2-3 dB under Clarinet 1's line and 5-6 dB under the harp's figure. Horn 4 - Horn 3 within ±2 dB.
- All are fresh whole-note onsets, so no step falls under a sounding note.

## 6. Bars 224-225 (qn 892-900): the violas' f portato quarters are level with the chorale tune (measured; small)

**Where.** The first chorale phrase. Trumpet 1 has the motto G4-E5-D5-C5 (f), doubled an octave lower by Trombones 1-2 a2. The violas play "unis., change bow at will" portato quarters (f), the pulse that arrival.ily c153 asks to keep. Violins I and II hold the mf tremolo.

**Evidence (measured, 892-900).**
- Trombone 1 -32.6, Trumpet 1 -33.5, violas -34.1, Horn 3 -35.0, Trumpet 2 -35.9, Violins I -37.0 dB.
- The violas' accompaniment pulse is 0.6 dB under the tune and over every horn. The norm is a trumpet about 3 dB over a string section at f, and an accompaniment 3 dB or more under the tune.
- Violins I's tremolo is 3.5 dB under the tune, which is right.
- From 226 the tune moves to the ff violins and winds, and the violas (-34.8) sit 6 dB under it. That part is fine.

**Fix.** `build/roles.json` Violas: add `[892.0, 900.0, -3.0, 1.0]`. It starts on the first portato quarter (the fff tremolo ends at 892) and ramps out over 899-900 into the ff at 226. Expected: violas about -37 dB, 3.5 dB under Trumpet 1, still over Horn 1 and Horn 2 so the pulse is heard.

## Coordinator items

**Wetness (verified, measured on the master; aligned at the point where the level first falls 3 dB under the body).**

| stop (qn) | to -20 dB | drop at +0.3 s | RT60 from -10..-30 dB |
|---|---|---|---|
| 5 | 0.38 s | 17.2 dB | 1.65 s |
| 21 | 0.35 s | 17.8 dB | 1.73 s |
| 101.75 | 0.30 s | 19.5 dB | 1.50 s |
| 373.75 | 0.43 s | 15.9 dB | 1.58 s |
| 450 | 0.25 s | 22.0 dB | 1.20 s |
| 662 | 0.40 s | 15.7 dB | 1.58 s |
| 1113 | 0.35 s | 16.1 dB | 1.28 s |

- c09's numbers hold: -20 dB in 0.30-0.41 s at its four stops, and 1.28 s (c09: 1.26) on the final chord.
- The early fall is on the dry side of the recordings (-20 dB in 0.43-0.55 s; drop at 0.3 s 13-17 dB). The late slope is 1.5-1.7 s, inside the recordings' 1.5-2 s.
- The mix is not too dry: the stops end cleanly and the tail is still there. Do not dry it further. If Dan hears it as dry, the first step is the four return faders +1 dB, not the envelope.

**90 ms string repeat gaps on the master (measured, 38 "plain" gaps).**
- Dip in the note's own harmonic band (the gap minimum against the lower of the bodies before and after): stem median 3.5 dB, master median 3.8 dB. 17 of 38 dip 5 dB or more on the master.
- In 5 cases the stem dips 5 dB or more but the master dips under 3 dB (violas 818, 825.5, 826, 864; Violins II 362). There the hall and the doublings fill the gap, as Movement I c51 found.
- The violas' 825.5-831.5 eighths dip 12-17 dB on the stem and -3..+7 dB on the master. This is critic A's area; judge it on the master.

**Inner held notes under a tune (measured).**
- No held note was lifted by the c09 sfp / subito changes.
- HP_CURVE's `decresc_last` only bends a diminuendo that has a later onset inside it (`score_to_parts.py` around line 1984). The Movement I c51 case (one held note under a tune) therefore stays linear here.
- The held inner notes that do stick out come from elsewhere: Horn 4 in Q (finding 5, sample level by pitch) and the Violins I harmonic in C (finding 3, re-bow fills).

**Horns' soft passages, weighted (measured; no lift needed).**
- Note medians at p: horns K -47.9 against winds -46.5, trumpets -47.2 and strings -45.6. At pp: horns -49.9 against winds -51.6 and strings -48.3.
- A-weighted, the horns' p is 3.8 dB under the winds' (A discounts their 200-500 Hz body). K is within 1.4 dB.
- Horn 1's pp under F2 (264-300) is -49.9 dB K. That is 15 dB under the mf Violins I tune, but only 1.9-3.4 dB under the p bassoons in the same bars, which is one dynamic step.
- The stubs Hn 1 118 and Hn 2 122 are mf holds under the ff counterstatement, 6 dB under their own mf median and inaudible under that tutti in any case.
- The 315 Hz bell did not make the soft horns too quiet. Leave them.

**315 Hz hump: per-stem share of the 315 Hz third octave (measured) and its cause (inferred).**

| section | hump | largest shares (the stem's own 315 Hz excess over its 250/400 Hz mean) |
|---|---|---|
| J (536-600) | 8.4 dB | Horn 3 39 % (+23.3), violas 15 % (+9.9), bass clarinet 8 %, Trombone 2 7 % (+20.3), R Brass 6 % |
| P (888-936) | 4.8 dB | violas 25 % (+8.6), Horn 3 22 % (+10.1), contrabassoon 9 %, Horn 1 6 % |
| R (984-1080) | 5.3 dB | Horn 3 19 %, violas 17 %, Horn 1 15 % (+8.7), bass clarinet 7 % |
| whole piece | 4.4 dB | violas 18 %, Horn 3 13 %, Horn 1 12 %, celli 7 % |

- In J the hump is Horn 3's held D4 and E flat 4 (293.7 / 311 Hz fundamentals at 544, 548, 560 and the sfp 592), plus Trombone 2's notes in the same band. It is the written pitches, not a resonance of the mix (inferred from the +20-23 dB own excess on those stems).
- A static EQ that reaches 3 dB in J would cut those notes' fundamentals. I would not chase the 3 dB target in J; the whole-piece 4.4 dB is a fairer measure.

**Timpani rolls (BRIEF item 5, measured).**
- Every roll sits 15.3-21.0 dB under the master and ranks 12th-23rd among the stems: bars 5, 147-152, 209-210, 219-223, 231-238, 243-246, 261-263 and 273-278.
- The timpani's share of 30-150 Hz is 2-22 % (at most 19-22 % in 273-277).
- The sfp roll at 592 is now 21 dB under the master, where c08 read a p louder than the ff before it.

**Bass, arrival and ending (measured).**
- 30-150 Hz at the arrival (888-892): basses 67 %, tuba 20 %, timpani 12 %, bass drum 8 %. At 278: basses 42 %, bass drum 12 %, timpani 9 %, tuba 9 %. The bass drum's share falls to 0-1 % within 0.5 s.
- Band shares over the whole piece: 20-100 Hz -15.1 dB (between the lossy Dvořák at -21.7 and Brahms at -8.5/-7.9), 100-250 Hz -8.9 dB (references -6.6..-8.8). The bass is solid, not boomy.
- The crash is the loudest stem for the first 0.5 s at 888, 1048 and 1108 (8.8-10.3 dB under the master, 62-70 % of 5-12 kHz). By 0.5-2 s it is 15th-19th. It is heard, it marks the downbeat, and it does not dominate.

**Do not touch:**
- Trumpet 1's open solo (bars 51-66: 6.9-15.8 dB over its accompaniment).
- The muted Trumpet 1 with the cor anglais (bars 171-186, 3.8 dB under the cor anglais in unison).
- Theme B in the trumpets (bars 211-218, 3.7 dB over the next non-trumpet stem).
- The F2 tune over its counter-melody (bars 67-82, after c09's Vla/Vc roles: Vln I 5.4 dB over the violas, harp now under both).
- The counterstatement's bass theme (bars 27-34, the a2 horn theme on top, the violin countersubject 2.3 dB under).
- The bassoon solo at bar 115.
- The c09 chorale horn / Trumpet 1 rows at 892-928 and 1032-1047.5.
- The crash (v124) and bass drum (v114).
- Every timpani roll level.
- The wetness numbers above (returns, faders, envelope, register sends).
- The p-level agreement across families (within 2.4 dB).
- The climax order (223 and 278 loudest).

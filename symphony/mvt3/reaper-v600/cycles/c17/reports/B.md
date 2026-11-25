# Cycle 17, critic B: balance and levels (on the c16 render)

All levels are plain RMS dB on the c16 stems (dry, post-fader) unless stated. "Envelope removed" means the stem level minus parts.json `vol_db` and minus the mix.json dynamic trim at that note, so it is the level the instrument itself gave. "Dynamic value" is the pipeline's printed-dynamic number (p 46, mf 72, f 88, ff 114, fff 124), which CC11 follows (CC1 on brass and clarinets). Each judgement is marked measured or inferred. Nobody heard the audio.

## Manual notes (third round: pages behind this cycle's instrument-side level work)

| Manual (May 2021, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.53, p.64, p.150: velocity sets loudness and layer on short articulations only, because it cannot change inside a note; sustained instruments take loudness and layer from the controllers | every accent on "Sus MAX" / "Sus Non Vib" (70-80 % of the 618 accents measured) | No. c16 gives accented sustain notes velocity 111 against 73-100 on plain notes and a controller bump of 5. The velocity does nothing on these rows and the bump is too small (finding 1) |
| p.101: "Sustain Accent": velocity sets the loudness of the attack, the Mod Wheel the loudness of the sustain. "Sustain Marcato": a weaker attack than Sustain Accent, velocity sets a low-pass filter on the attack (low velocity = soft front) | brass accents (item 4 of the brief: weight, not bite); MANUAL-GAPS #1, never tried | Not used. "Marc Sus LITE" is installed on 1FH, 1TP, 1TB, 1TU and is the one brass row with an accent whose brightness is set per note |
| p.91-92: string "Marcato Sustain": a marcato attack layered on the looped sustain, "extra power at the start of the note" | string accents at ff, where CC11 has no room left | Not used ("Sus Marc LITE" is on all five string KS Masters; the scherzo found it takes no level from velocity, so its level is the row volume and CC) |
| p.93-94: Staccato On Bow stops the bow on the string; staccato rows have 9-16 round robins; velocity is their dynamic (p.64) | Double basses 199-210, 247-277 | Partly. The row is right; the velocities used (65-95) lie inside one layer and give no beat weight (finding 3) |
| p.125-126: Timpani Hard Long: CC11 and velocity set loudness, velocity selects up to 16 dynamic levels, left- and right-hand variations, two round robins; Hard Rolls: CC1 selects 8 levels | every timpani stroke and roll | Strokes: velocity is the only level control left after c16 and it is set 12-20 steps too low at f (finding 5). Rolls follow the page |
| p.137: each articulation row of a KS Master has its own volume knob | Leg Slur against Sus rows on strings and horns | Used in c16 for tremolo and staccato rows only; the legato rows still differ from the sustain row by 3-7 dB at f and ff (finding 2) |
| p.151: Volume sets a track's level against the others; Expression shapes the line | the remaining fast fader moves | Mostly followed after c16. 45 unison plateaus of one or two notes and the passage role on the violins from bar 271 are still fader moves that act on single notes or the wrong bars (findings 2 and 4) |

MANUAL-GAPS items still open and used below: #1 (brass "Marc Sus LITE"), #2 (re-tongue rows), #12 (recorded timpani crescendos, not needed here).

## Per-note fader moves still in parts.json (requested check)

Measured on `vol_db` (17,404 points before thinning): 392 notes move 3 dB or more between note-on and the next note-on; 256 lie under a printed hairpin, 63 follow a hairpin gain, 73 are other. What the other classes are:

- Unison level (`UNI_BOOST_HOLD_QN` 2.0): 45 plateaus of +3.0 dB (one of 4.8) that cover one or two onsets and switch over 0.25 qn (90 ms). Examples: Horn 1 qn 795.5-808.25 (+3, 0, +3 on successive whole notes), Trumpet 2 656.7-661.75 (+3, 0, +3 on single notes) and 983.3-995.25 (+6, +3, +6, +3 inside the theme head), Bassoon 1 263.7-299.25 (five plateaus), Oboe 1, Oboe 2, Horn 2, Horn 3, Trumpet 1 691.9-696.25. These are per-note moves in effect and break Dan's rule. Fix in finding 2.
- Release of a held decrescendo: 17 notes take an instant +3 dB step at the score onset of the arrival note, 0.14-0.27 s after its note-on because the note is led (Violins I 296, 776, 914, 950; Violins II 296, 532, 776, 914, 950; Violas 776, 932; Violoncellos 384, 552, 968; Oboe 2 914, 932). Measured on the stems: Violins II 532 -54.5 dB in the 60 ms before the step, -50.8 after; Violoncellos 384 -64.8 / -61.5. Fix: in `score_to_parts.py` release the `held_decresc` gain at the arrival note's moved note-on (`qn`) minus 0.02 qn, not at `sq`.
- Role and dynamic edges: steps of 3-9.6 dB over 0.1-0.25 qn at section starts (Violins II 935.9 +9.6, 263.9 +6.0; Violoncellos 743.9 +5.0; Bass trombone 1031.9 +6.0). They are slow-balance rows; keep them but start each at the first note's moved note-on.
- Printed player counts ("4 soli" Violins I 473-488, 3-7 dB steps), timpani roll levels, the final fade (16.7 dB over 0.3 s on every track at 1113): allowed.

## 1. Accents: the instrument has no room at ff, and the bump is one-fifth of what is needed (bars throughout; all wind, brass and string tracks)

What is wrong (measured). Accent over the unaccented neighbours, median: Flute 1 +1.6, Oboe 1 +0.2, Oboe 2 -4.4, Clarinet 1 +1.3, Bassoon 1 +0.1, Bassoon 2 0.0, Horn 1 +2.5, Horn 3 -0.9, Trumpet 1 +0.3, Trombone 1 +0.3, Bass trombone +0.1, Violins I +0.7, Violins II +1.5, Violas +1.3, Violoncellos +2.2, Double basses -1.3 dB; 42-100 % of each track's accents are under +1 dB (Trumpet 3 is the only track in range, +4.2).

Why (measured). 
- 71 % of the measured accents stand at ff or louder (dynamic value 114+), where the controller has 13 units left. 
- Level per 10 units of the dynamic value, fitted on each track's sustained notes with pitch removed: at 88-101 strings 1.5-3.4 dB (Violins II and Violas about 0), woodwinds 0.4-3.1, horns 1.1-3.4, trumpets 1.4-1.6, trombones 0.7-2.0, tuba 3.0; at 114-127 strings 1.4-2.1 (violins about 0), woodwinds 0.8-1.9 (flutes about 0), horns 2.0-5.3, trumpets 2.0-4.0, trombones 2.3-2.7, tuba 2.3. A bump of 5 is therefore 0.5-1.5 dB, and it lasts 0.3 qn (0.11 s).
- The accent velocity (111) does nothing on sustain rows (manual p.53, p.64).

Fix (instrument side; `build/score_config.py`, `tools/score_to_parts.py` accent branch near line 3523, `build/mix.json`).
1. Headroom. Plain notes on the sustain rows at ff play at 104 instead of 114 on strings and woodwinds (a new table, for example `SUS_FF_BASE = {"string": 104, "wind": 104}`, applied where the row is "Sus MAX" / "Sus Non Vib" and the printed dynamic is 101 or more). Make up the level with the slow dynamic trim: `dyn_trim_db` ff +1.5 dB on those tracks. This also removes most of the row step of finding 2, because the legato rows are 3-7 dB under the sustain row at ff.
2. Amounts for about +3 dB (`ACCENT_BUMP_AT` as {track: {dynamic band: units}}): strings +16 at f and +20 at ff (from 104 to 124); woodwinds +14 at f, +20 at ff; horns +8 at f, +7 at ff (CC1); trumpets +14 at f, +10 at ff; trombones and bass trombone +14 at f, +12 at ff; tuba +10 at f, +12 at ff. At mf and below +10 on every family (slopes there are 3-5 dB per 10).
3. Shape (weight, not bite): the controller reaches the bumped value 20 ms before the note-on, holds 0.15 s, returns to the base by 0.45 s after the onset (in seconds, not 0.3 qn). On notes shorter than 0.3 s hold the bump for the whole note.
4. Rows where the controller cannot do it: 
   - violins and flutes at ff (slope about 0 at the top): accented detached notes on "Sus Marc LITE" (strings, p.91-92) and "Sus Accent MAX" at velocity 70-85 (flutes, oboes), only outside slurs and outside the one-row theme spans; 
   - brass accents at ff where the 2-5 kHz front rises more than 3 dB over the body with the CC1 bump: "Marc Sus LITE" at velocity 50-70 (p.101; MANUAL-GAPS #1). 
   Test each row on one range render before adopting, and measure the 2-5 kHz front against the body (brief item 4).
5. Set accented sustain notes back to the plain velocity (it is unused data).

Expected (inferred from the fitted slopes): medians +2.5 to +3.5 dB on strings, woodwinds and trombones; horns and trumpets +3. Check after the render with `stepmed.py --accents`; the slopes carry 1-3 dB of scatter per track.

## 2. Row levels inside one line: legato rows 3-7 dB under the sustain row at f and ff; one- and two-note unison plateaus (strings, horns, trombone, trumpets; whole movement)

What is wrong (measured, envelope removed, single notes of 0.25 s or longer, same printed dynamic).

| track | f: Leg Slur MAX minus Sus MAX | ff |
|---|---|---|
| Violins I | -2.9 (Leg BC +0.7) | -5.1 (Leg BC -1.5; Tremolo +6.1) |
| Violins II | -4.3 (Leg BC -3.4) | -7.1 (Leg BC -2.2) |
| Violas | -5.0 (Leg BC -3.4) | -3.7 (Leg BC -4.4) |
| Violoncellos | -3.7 | -3.7 (Leg BC -0.3) |
| Horn 1 / Horn 3 | -5.3 / -4.4 | -2.3 / -3.8 |
| Trombone 1 | -6.3 | |
| Trumpet 1 / 2 | -3.3 / -4.8 | +2.6 / +2.9 |
| Oboe 1 | Sus MAX -3.6 under Leg Slur | -2.0 |

At mp-mf the rows are within 2 dB on the strings. This is the c05 "Violins II sustain notes 4 dB over the legato notes" (now +4.3 at f, +7.1 at ff), and it is the main cause of the remaining step medians: Trumpet 1 bars 247-262 has its six "Sus Non Vib MAX" notes +5.5 to +10.9 dB and its "Leg Slur MAX" notes -4.6 to +3.9 dB about the line's median (step median 3.0 dB).

Fix.
- The headroom rule of finding 1 (plain sustain notes at 104 instead of 114 at ff) closes 1.5-2.5 dB of the ff gap. Add a row offset in controller units for the rest: a table `ROW_CC_OFFSET = {track: {row: {"f": units, "ff": units}}}` in `score_config.py`, applied to the note's controller level at its onset and held to the next note: Violins I "Sus MAX" f -10; Violins II "Sus MAX" f -12, ff -10 more than the base; Violas "Sus MAX" f -12, ff -6; Violoncellos "Sus MAX" f -10, ff -8; Horn 1 / Horn 3 "Sus MAX" f -12 (CC1); Trombone 1 "Sus MAX" f -14; Trumpet 1 / 2 "Sus Non Vib MAX" f -12, ff 0. Compensate each track's overall level in `dyn_trim_db` (f +1.0, slow).
- Violins I / II "Tremolo" at ff still +6 dB over the sustain row after the -3 / -4 dB row volumes: `row_volume_db` Tremolo -6 / -8 (see finding 4).
- Unison plateaus: in `score_to_parts.py` (lines 6050-6081) give the fader boost only to groups of 8 qn or longer (`UNI_BOOST_MIN_QN = 8.0`, hold 2.0 -> 4.0); shorter groups get +8 controller units on the kept note instead (CC1 on brass, CC11 elsewhere), no fader move.

Expected (inferred): row differences under 2 dB; Trumpet 1 247-262 step median under 2 dB; the 45 plateaus gone from the envelope.

## 3. Double basses: weak E flat 2 and F, and the short-row eighths (whole movement; bars 199-210, 247-277)

Pitch evenness (measured). The actor's table (spread 12.2 dB: F2 -7.3, F1 -6.0, G1 +4.9) pools notes of different printed dynamics: the G1 notes have a median CC11 of 113, the F1 and F2 notes 88-90. With the dynamic fitted and removed (226 "Sus MAX" notes; residual SD 2.9 dB) the pitch effects are: E flat 2 -7.1 (17 notes), F sharp 1 -4.4, F1 -3.7, F2 -3.7 (with the 87.3 Hz bell at -12), E2 -2.6, E flat 1 -1.9, B flat 1 -1.4, D2 +0.8, B1 +0.9, C2 +1.3, G1 +2.0, C sharp 2 +2.5, A flat 1 +2.9 dB. On the master under ff bass notes, the 28-140 Hz share is -8.9 dB on C2 and -6.5 on G1 (absolute -31.4 and -32.4 dBFS: tonic and dominant are even within 1 dB), and -16.8 on E flat 2 and -13.8 on F2. The low end is solid on C, G, A flat and D, has no boomy bar (loudest 56-112 Hz bar 262, -24.6 dBFS) and has holes on E flat and F: in C minor the third and the subdominant.

Fix.
- Per-pitch controller table on the basses (a new `PITCH_CC = {"Double basses": {pitch: units}}`, added to CC11 at each note-on and held for the note; the line is monophonic): E flat 2 (39) +20, F sharp 1 (30) +14, F1 (29) +12, E2 (40) +8, E flat 1 (27) +6, B flat 1 (34) +4, G1 (31) -6, C sharp 2 (37) -8, A flat 1 (32) -9. Values from 3.2 dB per 10 units below 101 and 1.5 above 114 (fitted). With plain ff at 104 (finding 1; `dyn_trim_db` ff 4.0 -> 5.5) E flat 2 has 23 units of room at ff.
- F2: the bell cuts E2 as well (82.4 Hz is 0.08 octave from 87.3 Hz). With the per-pitch table in place, set the bell to -9 dB and give F2 (41) -4 units; by the fit F2 then stands at about 0 and E2 gains about 1.5 dB (inferred). The c16 range tests (F2 +9.9 / +5.8 dB at -4 / -8) used five F2 notes and the pooled median; repeat the test with the dynamic removed before deciding. If F2 is over +3 dB at -9, go back to -12 and keep F2 at +12 units instead.
- More bottom, if wanted after this: the E flat and F fixes raise the 56-112 Hz share on those bars; no further EQ. 56-112 Hz is at -11.3 dB against Brahms -8; the difference is now pitch holes, not a general lack.

Short-row eighths (measured). The "early and scattered" starts are a measurement artefact, not a lead problem. The half-rise falls before the note-on on the weak eighths (median -76 ms at the second eighth of each half bar in 199-210, -58 ms on velocities 65-69), which cannot be the new stroke: it is the ring of the stronger stroke before it. Three causes:
- `ROW_LEAD_S` acts only on notes that abut the note before (tool comment at line 1219); these strokes are detached, so no value can take. The written note-on leads are 5 ms (792-840) and 20 ms (984-1080).
- Velocity 65-95 gives no level change on "Stac On Bow RRx9": peak by velocity decade -31.0 / -31.2 / -30.7 / -31.1 dB in 984-1080, and 2.7 dB over 30 steps in 792-840. The position pattern 90 / 80 / 80 / 70 therefore gives no beat weight and the weak strokes are not softer by design; they are masked by pitch level and ring.
- Peak level by pitch on this row spans 12 dB: A flat 1 -24.8, D2 -27.5, A1 -27.9, G1 -30.4, C2 -31.0, F1 -31.9, F2 -34.9, E2 -36.7 dBFS (984-1080).

Fix: `ART_SPANS` length 58 % -> 45 % of the slot (0.16 s at 168; FINDINGS section 7 and batch 7: shorts 50-62 % and shorter); velocity pattern across the layer boundary the c16 tests found between 88 and 100, for example 102 / 84 / 92 / 84 with +-4, and measure the beat weight on a range (target 3-4 dB); the `PITCH_CC` table above applies to this row too (CC11 scales the row's volume); remove the two `ROW_LEAD_S` entries. For the S table, measure these strokes by the 1-4 kHz onset, not the broadband half-rise.

## 4. Violins cut 7.5 / 8.5 dB in bars 271-272; chord and tremolo levels belong in the row volume and CC11 (bars 223-234, 271-279)

What is wrong (measured). The stem-fix roles Violins I 1080-1116 -7.5 and Violins II 1080-1116 -8.5 start at bar 271, but the divisi chords and tremolos start at bar 273 (qn 1088, "div."). In bars 271-272 both sections play single lines at ff on Leg Slur / Sus MAX and fall to -46.6 and -45.7 dB, against -34.4 and -38.7 in bar 270 and Violas -34.3, Trumpet 1 -29.1 in the same bars. In the allargando into the Largamente the violins are 8-12 dB under their own level one bar earlier. The string return there is 15.8 dB under the dry strings (13.0-13.8 elsewhere), 2-3 dB dry.

Ending level and room (requested). Bars 273-277: all strings together 4.8 dB under the rest of the orchestra (0.5-4 kHz -6.5), brass +0.9 over the rest; bars 278-279 strings -2 to -3, with Violins I / II the two loudest stems (-28.8 / -28.1). Return minus dry: 273-277 -13.5, 278-279 -13.8 dB, the same as bars 151-165 (-12.8) and 255-262 (-13.6): the room is right from bar 273. The final chord falls 20 dB in about 0.4 s after the cut. Bars 224-234 are at -15.7 (hand scaling): 2-3 dB dry, small.

Chord levels (measured, "Sus MAX" at ff, envelope removed): two-note chords over single notes Violins I +2.3, Violins II +3.1, Violas +1.9, Violoncellos +6.1 dB. Tremolo at ff over the sustain row: Violins I +5 to +8, Violins II two-note +13, three-note +16 dB.

Fix.
- `roles.json`: start the Violins I / II / Violas rows at 1088 instead of 1080 now (a slow-balance correction).
- Then move the cause to the instrument: mix.json `row_volume_db` Tremolo Violins I -3 -> -6, Violins II -4 -> -9, Violas -3, Violoncellos -3; a chord rule in controller units (`CHORD_CC = {2: -8, 3: -12}` on the string tracks, at the chord's onset, held for the chord; Violoncellos two-note -16). With these in, reduce the passage roles to what the next render still needs (expected -1.5 to -3 dB) and delete Violins II 888-936 -7.0.
- Chorale against the tremolo, bars 224-234: brass 1.5 dB under the rest over the passage; in the bars where the brass play, +1 to +4 dB. Trombone 1 is the loudest stem (-38.8), Violins I next (-39.9). No change beyond the row volumes. Bars 255-264: brass +0.7 over the rest (0.5-4 kHz +2.5), Trumpet 1 the loudest stem: right.

## 5. Timpani strokes 3-4 dB short; brass and wind tongued changes with gaps under 60 ms run together

Timpani (measured). Stroke level against velocity over 160 strokes: 0.18 dB per step at f and louder, 0.24 over all strokes. At the printed f the strokes play at velocity 85-101 and measure -42.3 to -44.1 dB; at 108-113 they measure -39.0; ff at 120-125 -36.8. Position gives almost no weight in 247-270: bar start -40.3, second beat -44.5, off-beats -42.0 to -42.5. Against the orchestra: bars 11-34 stem -49.6 with the rest at -29.4; no roll is within 15 dB of the summed rest or within 7 dB of the loudest single stem, including bar 223 (-37.3 against -16.3) and bars 273-279 (timpani and bass drum 17.1 dB under the rest). Nothing covers; the timpani are weak throughout. The roll of bars 231-234 (qn 920-933, f) falls from -41.0 to -60.2 dB, 30 dB under the rest, while the printed diminuendo covers only 928-932.

Fix (`build/score_config.py`): `TIMP_CC1_MAP` stroke velocities (88, 88) -> (88, 102), (114, 104) -> (114, 116), (124, 122) -> (124, 127); `TIMP_METRIC_VEL` {"down": +6, "mid": 0, "beat": -4, "off": -10, "jit": 3} (16 steps from bar start to off-beat, about 3-4 dB; FINDINGS section 23: 15-25 steps). Expected: f strokes +2.5 to +3 dB, ff +2. If the stem is still more than 1 dB under c15, raise `gain_db` -7 -> -6 (a track gain). Limit the settle of the 920 roll to 8 dB before the printed diminuendo (`TIMP_ROLL_TRIM_DB` settle floor, a whole-roll level).

Tongued note changes (measured, f and louder, sustain rows, dip under the softer of the two notes):

| track | gap 0-30 ms | 60-100 ms | over 100 ms | changes under 3 dB |
|---|---|---|---|---|
| Horn 1 | 1.5 dB (14) | 4.7 (43) | 6.7 (5) | 20 of 63 |
| Horn 3 | 0.7 (5) | 4.9 (31) | 5.6 (10) | 14 of 46 |
| Trumpet 1 | 2.8 (4); 30-60 ms -0.6 (3) | 8.7 (22) | 7.7 (11) | 9 of 41 |
| Trombone 1 | 0.6 (9); 30-60 ms -0.7 (5) | 4.8 (64) | 8.2 (4) | 22 of 82 |
| Tuba | 4.5 (9) | 10.3 (53) | 12.5 (9) | 7 of 74 |
| Bassoon 1 | 1.3 (27); 30-60 ms 2.9 (90) | 10.9 (3) | 11.6 (6) | 67 of 126 |
| Oboe 1 | 2.0 (24); 30-60 ms 2.6 (31) | 5.7 (1) | 16.1 (5) | 34 of 61 |

Same-pitch repeats already have 100 ms and dip 6.6-11.0 dB. The notes that run together are the ones played with a gap under 60 ms. Fix: every tongued (unslurred) change on a sustain row gets a played gap of 90 ms on brass and 70 ms on woodwinds (FINDINGS section 12: brass 98, winds 63), capped at 30 % of the note, in the detach rule of `score_to_parts.py` (the gap is set by keyswitch time on wind re-tongues, Movement II c54: check `KS_LEAD_AT`). Horn 1 and Trombone 1 stay near 4.7 dB at 90 ms; if 3 dB is not reached everywhere, put those changes on "LegRep RRx4" (MANUAL-GAPS #2).

## 6. Exposed lines: muted trumpet's register slope, celli pizzicato, re-bow holes, bar 204

- Muted Trumpet 1, bars 171-186 (measured; flat CC11 54, CC1 42, velocity 53): C4 and D4 -4.0 dB, E flat 4 to B flat 4 within 0.5, C5 +3.0, D5 +3.8, E flat 5 and above +7 to +10 about the line's median; the two phrase entries at 680 and 712 (CC1 36) are 5 dB under the other G4 notes (0.8 dB per unit at this level). Step median 3.3 dB. The trumpet is 6.1 dB under the cor anglais it doubles (-55.0 against -48.9); together they are +0.4 dB against the rest (0.5-4 kHz +4.7). Fix: `PITCH_CC["Trumpet 1"]` on the "Mute Sus" row, in CC1 units: C4, D4 +5; C5 -4; D5 -5; E flat 5 and above -8; no entry below CC1 42. Role Trumpet 1 680-744 +3 dB (slow) so the doubling is heard as two colours (inferred preference).
- Bassoon 1 solo 115-122: +4.1 dB over the rest, step median 1.8 dB; pitch offsets under 2 dB except A4 -4.8 (one note: +6 CC11 at 471-472 if it is still low). Trumpet 1 solo 51-66: -0.1 dB against the rest, +5.8 in 0.5-4 kHz, step median 1.7: keep. Violins' F2 67-82: violins -2.3 against the rest, +2.4 in 0.5-4 kHz; the celli counter-melody is the loudest stem in bars 77 and 79 (-35.6 / -36.0 against Violins I -36.3 / -37.1): role Violoncellos 304-316 -2 dB.
- Pizzicato, bars 51-66 and 171-186 (measured, every pluck at velocity 41): Violoncellos peak range 12.1 and 15.7 dB (SD 3.8 / 4.7; B flat 2 -5.3, A flat 2 +5.9, F sharp 2 +4.6; C3 -7.9, E flat 2 -5.0, G2 +5.5), Double basses 8.6 and 6.2 dB. Fix: turn `build/pluck_trims.json` into velocity (`PLUCK_VEL`, about 3 steps per dB to start) and fit it on one range render, with the CC16 resets left where they are.
- Re-bows on soft pedals (measured): Violoncellos 14 re-bows, dip median 4.7 dB, largest 10.1 (C3 qn 919.97, bar 230) and 8.1 (qn 185.29, bar 47); Double basses 7, median 5.0, largest 10.6 (qn 567.03, bar 142) and 7.8 (bar 145); Violas largest 6.4 (qn 564). The old note ends 11-16 ms before the new note-on. Fix: `tools/space_rebows.py`: end the old note 0.25 s after the new note-on ("Sus MAX" is polyphonic), new note at the old note's velocity; test on one range for phasing.
- Bar 204 stop (measured): the dry Violoncellos stem is the tail. After the cut at qn 814 it measures -31.0 dB in the first 0.1 s, -39.1 at +0.2-0.4 s and -46.1 at +0.4-0.6 s; every other dry stem is at -46 or lower by +0.2 s (Double basses -49.4, Violas -50.0) and the four returns are at -47.5 to -52.6. Fix on the instrument: Violoncellos G2 at 813 ends at 813.8 (70 ms early) with CC11 falling 118 -> 70 over 813.6-813.8; Double basses G1 ends at 813.85. No return ride. Expected (inferred): cello tail 8 dB lower at +0.3 s, the master's drop about 15 dB.
- Horn 4, A flat 3 held 6.5 s at qn 168 (bars 43-44): level range 8.9 dB, SD 2.2 dB about its trend: check for loop pulsing (brief item 7).
- Not measured this cycle: the sfp shape of bar 149 on the instrument lanes, the dal niente entries, the bar 222 fronts, the theme head's fall after its first note. First theme 11-26: Violoncellos are the loudest stem (-37.8) over Violins I (-39.0), and Violins I stand 6.4 dB under the rest (0.5-4 kHz -2.8); I did not check which staves carry the tune, so no change is proposed.

Crash cymbals: 14.9, 12.3 and 14.9 dB under the summed rest at bars 223, 263 and 278: heard, not dominant (broadband measure only).

Do not touch: `VOL_PER_NOTE = "off"`; the stop rides at bars 2, 6, 113, 166; the basses' 72 Hz bell and the cello EQ of c16; the theme's staccato velocities (`ROW_VEL_SPANS`) and the one-row spans with `steady_leads.json`; "Stac On Bow RRx9" as the basses' row; the timpani roll levels other than the 920 roll; the Trumpet 1 solo 51-66 and Bassoon 1 solo levels; the brass level in 255-264 and 273-279; the three crash strokes; the returns' level from bar 273.

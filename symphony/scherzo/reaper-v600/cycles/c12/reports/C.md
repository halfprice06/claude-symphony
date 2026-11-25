# Critic C, cycle 12: holistic comparison (render under review: c11)

All levels are RMS in dBFS on the c11 stems and master unless a line says otherwise. "Measured" means a number from the
c11 audio or data; "inferred" means a judgement that follows from the numbers but was not measured directly. Bar b starts
at qn 3(b-1).

## Manual notes (May 2021 HO manual, PDF pages 82-88, and loop/MANUAL-GAPS.md)

Pages 82-88 describe the Hollywood Solo Cello library's instrument types. That library is not installed (MANUAL-GAPS #5,
45 GB memory cap). Where the same instrument type exists in the installed sections (legato, short, keyswitch master), the
statement is applied by analogy, and that is marked inferred.

| What the reading says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Solo instruments have their own microphone set; in the solo libraries dynamics and vibrato depth are linked on CC1, in the HO sections they are independent (p.82) | Violin I solo, bars 349-356 (qn 1044-1068) | Not available. The solo plays on `1st Violins KS Master DIV A.oib` with CC1 held at 72 (`CC1_HOLD`, Movement II c32: on this patch CC1 crossfades the vibrato layers). The line is the most even solo of the render (adjacent-note step median 1.6 dB, measured). Keep. |
| Long Solo instruments: a legato script blends overlapping notes and removes strong attacks; one instrument per vibrato style; CC11 and CC1 set loudness (p.83-85) | same | Not installed. No action. |
| Short: velocity sets loudness and the dynamic layer (3 levels); round robin x2 / x4 (p.85-86) | staccato eighths of theme A (bars 13-28) and its reprise; the ff tuttis (bars 105-120, 305-320) (inferred for the section patches) | Followed. Immediate same-pitch repeats with an identical first 60 ms: strings 0, trumpets 0 (measured). Theme A against its reprise: 3 of 38 onsets identical in Violins I (c07: 33 of 48). |
| Monophonic True Legato: each transition is a separate recording made at several volumes, chosen by note velocity, up to an octave, cross-faded into the sustain (p.86-87) | the trio tunes: Clarinet 1 bars 153-168, celli 169-184 (`LEG_VEL_SPANS` 80), Oboe 1 185-200; Horn 1 bars 357-360 (inferred for the section patches) | Partly. The transition recording's level is not under CC1/CC11, and at three joins it reaches the master 4-9 dB over the notes on each side (finding 1). |
| Legato Slur "shines at slow to medium tempos" (p.87) | trio eighths at quarter 228 (131 ms each) | Join timing is in range after c11 (median join against the beat: Violins I +15 ms, celli +7 ms, measured). No action. |
| LegSus Slur: CC1 picks one of 2 dynamic layers at note start, no crossfade inside the note (p.87-88) | not used in this mockup | Not applicable. |
| Keyswitch Master (p.88) | every KS track | Followed. |

MANUAL-GAPS: #5 (solo strings) and #6 (timpani hard sticks, pending) are not re-reported here.

## The render as a whole

Section levels, master / delivered mp3 (dB RMS):

| Section (bars) | c00 | c07 | c10 | c11 |
|---|---|---|---|---|
| Theme A 13-28 | -38.5 / -29.6 | -38.6 / -30.1 | -37.4 / -29.1 | -37.4 / -29.0 |
| F major episode 73-88 | -29.4 / -25.8 | -35.8 / -29.0 | -35.4 / -28.8 | -35.5 / -28.8 |
| Hemiola 101-104 | -17.3 / -17.9 | -18.9 / -19.6 | -18.7 / -19.4 | -18.7 / -19.3 |
| ff tutti 105-120 | -20.3 / -21.1 | -20.8 / -20.0 | -20.4 / -19.7 | -20.5 / -19.7 |
| Trio, Clarinet 153-168 | -32.1 / -25.5 | -37.1 / -28.4 | -37.1 / -28.2 | -37.3 / -28.2 |
| Trio, celli 169-184 | -34.6 / -27.7 | -35.8 / -28.2 | -35.5 / -27.7 | -35.6 / -27.9 |
| Trio ff 209-224 | -25.9 / -23.8 | -28.3 / -25.1 | -28.0 / -24.9 | -28.1 / -24.9 |
| Reprise tutti 305-320 | -20.4 / -21.4 | -20.5 / -20.0 | -20.5 / -19.9 | -20.5 / -19.9 |
| Coda build 329-335 | -18.6 / -19.3 | -21.0 / -19.3 | -21.4 / -19.7 | -21.4 / -19.7 |
| Summit 336-339 | -11.4 / -13.4 | -16.0 / -14.7 | -16.0 / -14.6 | -16.0 / -14.6 |
| Violin solo 349-356 | -37.4 / -29.8 | -38.2 / -30.2 | -37.6 / -29.6 | -37.5 / -29.5 |
| Close 357-376 | -39.6 / -30.6 | -39.0 / -30.2 | -39.7 / -30.4 | -39.6 / -30.2 |

The balance between sections has not moved by more than about 0.5 dB since c07 (measured). The summit is the loudest
point of the delivered file: momentary maximum -8.5 LUFS against -10.5 (bars 300-304) and -12.0 (the two ff tuttis);
short-term maximum -9.8 against -14.0 and -13.8 (measured).

Whole-mix band shares (dB; 20-100 / 100-250 / 250-500 / 500-2k / 2-6k / 6-20k Hz), side/mid in 2-6 kHz, crest:
scherzo c00 -19.2/-8.8/-6.2/-2.5/-12.6/-32.5, -4.4, 13.2; c07 -17.3/-8.1/-6.2/-3.4/-8.9/-24.7, -3.7, 13.0; c11
-18.6/-8.5/-5.9/-3.2/-9.6/-28.8, -3.7, 12.9; Movement I c52 -16.6/-8.3/-6.4/-3.0/-10.1/-29.3, -4.2, 12.7; Movement II
c49 -17.3/-7.6/-5.6/-3.6/-10.1/-29.6, -4.5, 12.3; Dvorak 9/i (Columbia) -21.7/-6.6/-6.3/-3.5/-10.5/-28.8, -6.1, 11.4. The
scherzo is in line with the other two movements and with the recording in every band (measured). No Beethoven or
Bruckner scherzo recording is in the repository and downloads are not allowed, so the comparison with the model the
score names could not be made on audio.

Answers to the lens questions. Repeated staccato eighths do not sound like one sample (S1 passes, round robins differ).
The summit is the loudest. The weakest passages now are the solo statements of the trio and the Meno mosso (findings 1
and 3), the harmonic of bars 141-149 (finding 2), the fronts of the tutti accents (finding 4) and the harp (finding 5).
One property of the sample set limits the Clarinet 1 tune and has no fix in the config: the level of its upper partials
differs by up to 15-20 dB between neighbouring pitches (A4 -24.1, A5 -25.5 and F#5 -19.6 dB against C#5 -3.9 and E5
-7.4), and CC1 47 to 72 changes that by 0-2 dB (measured).

## Findings

### 1. Three legato transitions and one arrival note are louder than the phrases they belong to

Where: Violoncellos, bar 169 beat 3 (score qn 506, the second note of the "arco, espress." tune, G#3 to A3) and bar 191
(qn 570); Clarinet 1, bar 154 (qn 459, B4, the first downbeat of its tune); Horn 1, bar 360 (qn 1077, G#4, the last note
of the call in bars 357-360).

Evidence (measured, 30 ms frames for the joins, 100 ms frames for the horn):
- Celli 506: the stem reads -29 dB from 90 to 30 ms before the beat, against -37 to -41 on the note before and -40 to
  -45 on the note after: +9.7 dB in the stem, +9.1 dB in the master (master frames -38 -32 -29 -28 -32 -36 -38). c08 had
  the same peak (-34 -30 -30), so it comes from the transition recording (velocity 80, `LEG_VEL_SPANS`), not from c11's
  data. `build/note_trims.json` already has "506.0": -3.0; a note trim lowers the note and the transition together and
  leaves the peak.
- Celli 570 (velocity 100): +7.1 dB in the stem, +4.9 dB in the master, 150 to 30 ms before the beat.
- Clarinet 1 459: +6.5 dB in the stem, +4.1 dB in the master, from the beat to +30 ms. The track's `vol_db` rises from
  1.1 at 458.81 to 10.4 at 459.0 (9.3 dB in 50 ms); the B4 pitch trim (+4.5, `build/pitch_trims.json`) is one of its
  terms and arrives on the transition.
- Horn 1 357-360: the part prints p espress., a crescendo 1068-1071, a decrescendo from 1071 and pp at 1080. The stem
  reads -37 at the printed peak (1071) and -31 -33 -37 in the first 300 ms of the note at 1077; the master reads -36
  and -31 -32 -35. The note inside the decrescendo is 5-6 dB over the printed peak. `vol_db` goes 3.9 (1076.75), 7.0
  (1077.0, the G#4 pitch trim +3.5), 12.2 (1077.34 to 1078.14, the hold fill). c08 was the same (-32 -30).

Manual p.86-87 (by analogy): the transition is its own recording chosen by velocity, so CC lanes do not shape it. The
existing tool for this is `JOIN_NOTCH`.

Fix, `build/score_config.py` (same append pattern as the c09 `JOIN_NOTCH` line and the c10 `LEVEL_SHAPES["Horn 1"]`
lines; `JOIN_NOTCH` positions are in moved time, 0.04 qn ramps):
- `JOIN_NOTCH = {**JOIN_NOTCH, "Violoncellos": JOIN_NOTCH.get("Violoncellos", []) + [(505.5, 506.0, -7.0), (569.4,
  569.9, -5.0)], "Clarinet 1": JOIN_NOTCH.get("Clarinet 1", []) + [(458.95, 459.2, -4.0)]}`. With the celli notch in
  place, test removing the note trim "506.0": -3.0, which was added against the same peak and lowers the whole note.
- `LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(1076.75, 0.0), (1076.85, -6.0), (1077.4, -6.0), (1078.0,
  0.0)]]`.
Targets: each join's peak within 3 dB of the notes on each side in the stem; Horn 1's frames at 1077 no higher than its
frames at 1071 (-37 dB in the stem). That these four peaks are audible is inferred from their size in the master.

### 2. The violins' harmonic in bars 141-149 drops out for half a second at its automatic re-bow

Where: the natural harmonic E6 of Violins I (qn 420-444.8, one tied note, ppp, "harm., change bow freely"), played on
the Violins II track's "Harmonics" row (`BORROW_NOTES`). The automatic re-bow splits it into two notes of 2.83 s and
2.80 s at qn 432.497 (bar 145).

Evidence (measured): the Violins II stem falls from -47/-50 dB before the re-bow to -61 dB at 0.35-0.5 s after it (10-13
dB) and is back at -51 dB about 0.9 s after. In the master the 1250-1400 Hz band (E6 = 1318.5 Hz) falls from -49/-52 to
-64/-65 dB for about 0.3 s. The harmonic is the only high voice in these bars. The row speaks slowly (per quarter from
420: -69 -61 -55 -51), so every new bow starts with this gap. c08 had the same dip. `build/rebow_fills.json` has
`"Violins II": {}`, so this re-bow is the only one on a long exposed note without a fitted fill. The printed "change bow
freely" asks for staggered changes inside the section, which give no dip.

Fix, either of:
- `tools/fit_rebows.py` for Violins II at 432.497, written to `build/rebow_fills.json` (expected shape, seconds from the
  re-bow and dB: `[[0.0, 0.0], [0.25, 5.0], [0.35, 10.0], [0.5, 10.0], [0.7, 5.0], [0.9, 0.0]]`).
- `AUTO_REBOW_SKIP = {"Violins II": [420.0]}` in `build/score_config.py` (one bow of 5.6 s), then the loop-pulsing check
  on the stem, because this row's loops are 1.8-5.2 s long.
Target: no dip over 3 dB in the stem between qn 431 and 436.

### 3. Oboe 1's first note of its trio statement is 6-10 dB under the rest of the phrase

Where: Oboe 1, bar 185 (qn 552, E5, p, "1. espress.", start of the slur). No hairpin is printed before the crescendo at
558-561.

Evidence (measured): the note (velocity 53, note-on 55 ms before the beat, 0.31 s long) reads -55 -53 -52 -50 -49 dB in
50 ms frames from the beat and never passes -49; the eighths after it (velocity 100) read -44 to -42 and the long notes
of the phrase -39 to -46. The master rises from -50 to -46 through the note and reaches -43/-41 on the next notes.
Clarinet 1's equivalent first note at 456 (same velocity 53, same lead) reads -48 -44 -44 -44: it speaks at the beat.
The oboe's CC11 is 37 on this note, the lowest value of its phrase, and its velocity is half that of the next notes.
`note_trims.json` has no Oboe 1 rows and `entry_leads.json` has Oboe 1 only at 672.

Fix: `build/note_trims.json` "Oboe 1": {"552.0": 5.0}. If the note still rises through its whole length, add "552.0":
0.06 under "Oboe 1" in `build/entry_leads.json`. Target: the body of 552 within 3 dB of the eighths at 553-554.5.

Related, measured, no new fix proposed: the celli's first note at 504 (bar 169) has its note-on 180 ms before the beat
and reads -56 -48 -47 -47 -42 -39 -37 in 50 ms frames from the beat, so it comes within 3 dB of its body only 250 ms
after the beat. It already carries a +5.0 dB note trim and a 0.06 s entry lead (c05/c06). The actor's open list names
the basses at 504, not the celli. One test (inferred): start the celli's `LEG_VEL_SPANS` row at 503.3 instead of 504.5,
so the first note has velocity 80 like the rest of the tune (it has 63), and compare the first 300 ms.

### 4. The accented half notes of the two ff tuttis start under their own body

Where: Violins I and II, bars 106, 110, 306 and 310 (qn 315, 327, 915, 927; Sus MAX, velocity 96, 0.46 s long); also
Violins II at 345 and 945.

Evidence (measured): level of the first 80 ms minus the level 100-200 ms after the beat. Violins I stem: -5.0, -3.4,
-5.0, -3.4 dB, with the level peak 160-260 ms after the beat; master: -3.1, -2.6, -2.4, -2.8 dB. Violins II stem: -2.2,
-3.7, -1.5, -3.4 dB at these four, -5.8 and -7.1 dB at 345 and 945. Over all accented long notes of bars 13-56, 97-124
and 301-339 in the 2-5 kHz band, accented notes have weaker fronts than plain ones: Violins I -1.3 dB (n=34) against
+0.3 (n=28), Violins II -1.5 against +0.4, Flute 1 -1.0 against +2.3. `build/accent_bodies.json` has string rows only
for the hemiolas (300-310, 902-910, -3.0 dB each). `build/accent_fits.json` has Violins I at 4.5 on 315, 351, 915, 951
and at 0.0 on 327 and 927, where the front is 3.4 dB under the body.

Fix: run `tools/fit_accent_bodies.py` for Violins I and Violins II at 315.0, 327.0, 915.0, 927.0 and for Violins II at
345.0 and 945.0 (or add the rows by hand at -3.0), and re-fit Violins I "327.0" and "927.0" with `tools/fit_accents.py`.
Expected gain 1-2 dB: the hemiola accents that already have the -3 dB body cut read -3.6 to +1.6 dB in the master
(inferred from those rows). Target: master front minus body at 0 dB or above on the four onsets.

### 5. The harp plays at one velocity per span, and the first note of its tune is not heard

Where: Harp, the six `VEL_CAP_SPANS` (bars 73-80, 81-88, 153-168, 185-192, 225-237, 341-348): 340 of the part's 346
notes. The tune marked "espress." is in bars 73-80 (qn 216-240).

Evidence (measured unless marked):
- 287 of the 340 notes sit exactly on the span's cap (42, 50 or 56); the other 53 are at 40 or 52. The whole part has 8
  distinct velocities. Two expert harp parts in the reference folder have 99 (Duc's Mahler Adagietto, 10th-90th
  percentile 33-102) and 75 (the EW HO demo's "Harp KS Master", 34-94).
- The cap is a clip that runs after the per-pitch offsets (`tools/score_to_parts.py` lines 3182-3183, then 3247-3249,
  read from the code). All 42 notes on pitches with a positive `HARP_PITCH_VEL` offset (quiet samples) sit on the cap,
  and 50 of the 103 notes on pitches with a negative offset (loud samples) sit on it too, so the evening by pitch is
  mostly removed inside the spans.
- In the tune, A5 at the same velocity 56 reads -53, -45, -53, -46, -47, -53 dB in its fundamental's band at qn 216,
  218, 221.5, 227, 231, 237 (8 dB between round-robin samples). The printed hairpins of bars 73-80 are carried by the
  volume lane alone (`vol_db` -3.0 to +1.0 to -3.0), so the tone does not change with them.
- The tune's first onset (qn 216, A5 over F2) reads -50 dB in the stem against -36 to -42 on every later onset of the
  phrase, and the master is at -25 to -34 dB in its first 150 ms (the decay of bar 72). It is not heard (inferred from
  the 16-25 dB difference). c08 was the same.
- In bars 81-88 four notes on F4 are at velocity 40 while their neighbours are at 50: they play the p layer inside an
  mp passage (layer limits from manual p.150 as cited in `build/score_config.py`; that page is outside this cycle's
  reading).

Fix:
- `tools/score_to_parts.py`, the `VEL_CAP_SPANS` block at lines 3247-3249: for the harp, shift instead of clip. Subtract
  (the span's highest velocity before the cap minus the cap) from every note of the span, with a floor of 30 in the
  spans capped at 42 and a floor of 43 in the spans capped at 50 and 56, so each span stays inside the layer the cap
  chose (manual p.150) and the hairpin, the pitch offsets and the metric weight remain as differences below the cap.
- `build/note_trims.json` "Harp": {"216.0": 5.0}.
Check after the render: the same-pitch spread in bars 73-80 falls below 8 dB and the single-note level spread per span
(now SD 3.3-4.3 dB) does not rise. The benefit to the listener is inferred. The chords stay unrolled: the part prints
"non arpegg." in each chordal passage, and the two printed arpeggios (qn 708, 1080) are rolled in the data.

## Requested and standing checks (all measured on c11)

- Splice points: at all 16 edges the largest second difference within 40 ms is 0.51-1.28 times the 99.9th percentile of
  the surrounding 250 ms, there is no 6-20 kHz burst, and the 60 ms levels on each side equal the first render within 0.3
  dB except where the repaired note itself differs (Horn 2 after 158.70 and after 626.70). No clicks and no level steps.
- Re-tongued notes (dip between two notes, 10 ms envelope, against the lower of the two bodies; limit 8 dB): Horn 2,
  trumpets, trombones, tuba and Bassoon 1 have none over 8 dB. Over the limit, and identical in the first render: Horn 1
  at 141.70 (10.7 dB), 998.57 (10.5), 659.66 (9.2); Horn 3 at 605.81 (9.2) and 521.81 (8.2); Horn 4 at 371.78 (8.6);
  Bassoon 2 at 515.87 (10.9) and 539.87 (8.3). Horn 1 at 164.60, inside a spliced span, reads 8.9 dB (c10's audio)
  against 1.6 dB in the first render, where the attack was missing.
- Stale legato state: no effect in the audio. Join front minus body, c11 against c08: Violins I +1.4 / +1.2 dB, Violas
  +1.4 / +1.1, celli +2.3 / +1.7, Bassoon 2 +0.5 / 0.0, Horn 4 +0.8 / +0.8. Join timing medians c10 to c11: Violins I +49
  to +15 ms (the intended lead), Violas +6 to +3, celli +27 to +7. No track is 45 ms early or 3-5 dB loud. The stale
  state was written to the project after the render (inferred).
- Loop pulsing on held notes: none (autocorrelation at 3.95 s: Horn 1's last note +0.01, Violins I's closing G#5 -0.04).
- Re-bows of Violins I's closing G#5: dips of 2.7, 3.2 and 5.7 dB in the stem at 1103.81, 1116.30 and 1125.16, 3-5 dB in
  the master at the last one. Re-fit "1125.156" under "Violins I" in `build/rebow_fills.json` with `tools/fit_rebows.py`.
- S1, separation of repeated notes (stem / master median dip, dB): Violins I theme A 7.8 / 5.6, ff tutti 5.2 / 4.0,
  reprise 9.3 / 5.3, coda build 6.0 / 3.1; Violins II theme 11.3 / 7.4; Violas 8.7 / 6.7; Trumpet 1 5.0 / 4.3. Passes.
- S3, subitos: the hall is not cut at 360, 900 or the G.P. at 1017. Passes.
- Tutti entry spread: first to last instrument 74 ms median (25th-75th percentile 61-90 ms) over 39 tutti onsets, at or
  above the 36-55 ms of the expert MIDI files. Do not add spread.
- Identical samples between the two ff tuttis (312-360 against 912-960, 2.5 minutes apart): Violins I 37 of 38 onsets,
  Violins II 16 of 20. Judged not audible at that distance under the full orchestra (inferred); no change asked.
- Phrase arches are present in the CC lanes of every solo statement (for example celli 504-528 CC11 49 / 71 / 69, Oboe 1
  552-576 37 / 73 / 55, Violin I solo 1044-1056 42 / 69 / 47).

Do not touch: the section balance and the loudness arc (stable since c07, summit loudest by 2 dB momentary and 4 dB
short-term); the hall (inside Dan's limits, subitos do not cut the returns); the whole-mix spectrum and width; the c09
row split between theme A and its reprise; the separation of repeated notes; the tutti entry spread as it is; the horn
splices; the Violin I solo's CC1 hold at 72 and its even levels; the harp caps' choice of layer and the unrolled "non
arpegg." chords; the c11 legato leads of Violins I and the celli.

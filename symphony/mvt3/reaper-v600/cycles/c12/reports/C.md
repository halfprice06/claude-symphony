# Critic C, cycle 12 (holistic comparison) on the c11 render

Compared: c11 master, stems and mp3 against the c00 port baseline, c06 (five cycles back), c10, Movement I c51 (master and mp3, same tools) and one commercial recording (Dvořák 9, first movement). All numbers are my own measurements on the WAV files unless a source is named. "Measured" means read from audio or data; "simulated" means computed from the stems or spectra without a render; "inferred" means a conclusion not checked on audio.

## Manual notes

Open MANUAL-GAPS items first, then the other pages read in full for this cycle (HO/Opus manual, PDF page numbers).

| Reading (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| MANUAL-GAPS #1. Brass "Sustain Accent": velocity sets the attack loudness, the Mod Wheel sets the sustain loudness; "Sustain Marcato" has a softer attack than Sustain Accent (p.101) | sfp at bar 149 (qn 592): Horns 1 and 3, Trombones 1 and 2, Bass trombone, Tuba; accented brass in N, R, T | Not used (no accent row is loaded; 30 "Marc Shrt RRx4" notes only). The sf is made on the Sustain row with a CC1 step and a post-fader bump. Measured: the front is within 0.9 dB of the ff before, so the row is not needed for level. The remaining fault (a second hump at +0.25 s) can be removed without the row (finding 3). |
| MANUAL-GAPS #5. Woodwind "Sus Expressive": a slower attack and a gently increasing vibrato (p.109) | Bassoon 1, qn 456-496 (in use, "Leg Slur Exp"); deferred for cor anglais 680-744 and Oboe 1 376-392, 744-760 | Followed on Bassoon 1. Measured cost: join dips up to 10.8 dB and, at the leap of qn 464, the body arrives 260-400 ms after the beat. Do not extend the row to the other two tracks now (see the answers below). |
| MANUAL-GAPS #6. The Repetition script picks a random detune or neighbouring sample, so playback differs per run; a Round Robin Reset gives identical playback (p.145) | Every track's pre-roll; the basses' spans 792-840 and 984-1108 (`RR_RESET_AT`) | Partly. The reset is sent only on the basses' spans. Measured: between c10 and c11 the 14 rewritten tracks have a median per-bar level difference of 0.00 dB, but single bars differ by up to 5.4 dB on rewritten and untouched tracks alike. That is the size of the round-robin variation without a reset (inferred). |
| MAX patches carry the most dynamic and vibrato layers; LITE about half (p.62) | All sustain and legato rows | Followed (Sus MAX, Leg Slur MAX, Leg BC MAX on every checked track). |
| Woodwind Sustain: 3 dynamic layers, polyphonic (p.109); woodwind legato rows are monophonic transitions | Flute 2 at qn 618 and 650 (finding 5) | The slur row is used and the transition is too slow for these two notes. A Sustain note that overlaps the old note is allowed by the patch and is the proposed fix. |
| "Legato Repetitions RRx4" is made for repeated notes inside a legato phrase (p.110) | Wind repeats inside slurs (K, L-M) | Not used (no "Rep" row in parts.json). Not tested this cycle; the repeats are made with re-tongue gaps on the Sustain and legato rows. |
| Short articulations have no release trails; hold the last note long enough for the room to sound (p.102, p.110) | Tutti stops (bars 2, 6, 26, 94, 113, 166, 204), final chord | Followed. Measured decays below. |
| Brass legato: at most an octave, no gap, monophonic unless CC22 is 0-63 (p.105) | Trumpet 1 chorale 888-936, horn lines | Not checked beyond the attack timing (all accented brass notes within +60 ms). |
| All instruments fade to silence on CC11 (p.63); finger-position tables on CC70 (p.148-149) | Soft endings; viola and cello D4-F4 in J | CC11 is used. The finger-position controller is not used; it would change the colour of the violas' D4 in J but not its level in the 315 Hz band (inferred). |

## Answers to the coordinator's items

**Wetness ceiling.** Within the ceiling at every stop (measured). Drop at +0.3 s / time to -20 dB: bar 2 12.6 dB / 0.46 s; bar 6 16.2 / 0.39; bar 26 17.3 / 0.33; bar 94 14.1 / 0.40; bar 113 19.2 / 0.30; bar 166 16.1 / 0.42; bar 204 17.9 / 0.42. Final chord from qn 1113: -13.7 dB at +0.3 s, -20 dB at 0.44 s, RT60 1.34 s (2 x T(-5..-35)) or 1.29 s (3 x T(-10..-30)). The same detector on three files gives a median of 16.0 dB / 0.39 s for c11, 14.8 / 0.45 for the Dvořák recording and 20.3 / 0.28 for Movement I c51. Return minus dry is -12.4 dB over the whole movement (c07: -12.5), between -9.4 (D) and -13.4 dB (T) by section. **Too dry?** No by Dan's measure. The mix is at the dry end of the recordings' range (bars 26 and 113 fall 20 dB in 0.30-0.33 s; the recordings take 0.43-0.58 s). Do not dry it further; there is no measured reason to add reverb.

**--midi-only drift.** No track moved without a data change (measured). Median c11 minus c10 per-bar stem level is 0.00 dB on all 14 rewritten tracks (p10/p90 within -0.2/+0.1 dB). Attack start times and pcx values on unchanged notes are identical. Horn 3's sfp peak is at 0.275 s in both renders. Movement II's +2.6 to +3.6 dB and 27-49 ms effect does not occur here. I had no timing probe for Trombone 2.

**Flute 2 at qn 650.** A re-attack, not velocity 122 (finding 5).

**sfp at qn 592 and "Sus Accent MAX".** The row is not needed. The fault is a second hump at +0.25 s on six brass tracks, fixed with level shapes at no memory cost (finding 3). If memory becomes free, test the row on Horn 3 only, at moderate velocity and without a CC11 bump.

**Bassoon 1 at qn 464 (+134 ms).** Real, and not a lead problem (measured). The note is D4 to A4 on "Leg Slur Exp" at velocity 80 with a 150 ms lead. The stem's level at the beat is 6 dB under its level before the join. Against its own level at +400 ms, the new A4 is 11.3 dB lower at the beat, 4.6 dB lower at +200 ms and 2.5 dB lower at +260 ms. The causes are the row's slow attack (p.109) and the `note_trims.json` ramp (464.0 +0.5 dB to 465.68 +2.5 dB), which raises the level late. Cheap fix: replace that ramp by a front-loaded `LEVEL_SHAPES["Bassoon 1"]` shape from the moved note-on, `[(463.55, 0.0), (463.62, 3.0), (464.6, 3.0), (465.6, 0.0)]`. Low priority. The other joins of the solo cross at -15..+69 ms with dips up to 10.8 dB (459: 10.2; 475: 10.8; 484: 8.1).

**Bar 275 under bar 274 by 0.6 dB.** Leave it (measured). mp3 bar means: 274 -15.4, 275 -16.0, 276 -15.2, 277 -12.8, 278 -11.2 dB. The dip is in the first half of bar 275, where Horns 1 and 3 start their shapes at -4 and -3 dB. Bars 275 to 278 rise 4.8 dB and the first half of bar 278 (-10.6 dB) is the loudest half-bar of the file. If it must be removed, end the horns' hold at qn 1098 instead of 1099.

**315 Hz hump in J.** It is pitch content, not an EQ fault (finding 6). A string bell at 315 Hz would not reach its main source.

**Leg Slur Exp on cor anglais and Oboe 1.** Do not add it now (inferred from the Bassoon 1 measurements and p.109). On Bassoon 1 the row gives join dips up to 10.8 dB and a late body on leaps to long notes; each row costs 0.1-0.3 GB per track and REAPER is at the 45 GB limit.

**Tuba and contrabassoon -3 dB on qn 984-1056.** Not a balance improvement (simulated on the stems). Shares of the master there: Tuba -13.5 dB full band and -16.3 dB at 30-120 Hz; Contrabassoon -16.2 and -18.6; Violoncellos -3.3 and Double basses -5.8 at 30-120 Hz. With both at -3 dB the master changes by -0.14 dB full band, -0.1 dB at 30-120 Hz, -0.26 dB at 120-400 Hz, and the basses' repeat dips in the master go from 3.3 / 4.8 to 3.2 / 5.1 dB (on-beat / off-beat). Do not do it.

**Basses' gap dips before the beats.** Keep (measured; S1 improved). Master dips at 30-120 Hz, on-beat, c11 against c10: 792-816 3.5 (2.1); 816-840 3.3 (2.6); 984-1056 3.3 (2.6); 1056-1088 4.2 (1.0); 1088-1108 2.9 (2.1) dB. My method (body mean minus the minimum of a 30 ms envelope) gives smaller figures than the actor's. The stem dips of 9-11 dB are not too deep, because the celli and timpani fill the master.

**sf bumps on winds and brass at 592.** Keep; they bring the front to within 0.9 dB of the ff before. Finding 3 adds to them.

**Violas' chord-repeat gaps (840-872).** Keep (measured). Stem dips: new-bow heads median 14.8 dB (n = 7), louré 8.1 dB (n = 16). In the master (150-3000 Hz) they are 4.2 and 1.2 dB, the same as c10 (4.2 / 1.4). The louré gaps are masked in the master; they do no harm.

**Delivery ride after the subito p at bar 42.** The subito is kept (8.8 dB in the mp3, 9.2 in the master), but the gain then rises 5 dB in about 4.3 s (finding 4).

**Brass accents (BRIEF 4, tilt jump).** Pass (measured, 98 accents on the master): tilt jump median -0.2 dB, p90 +2.4 dB (c10: -0.3 / +2.6; limit +3). No accented brass note is later than +60 ms; medians are -80..-5 ms. I simulated a shorter, stronger swell (+4 dB, full 0.02-0.08 s, gone by 0.25 s) on all 11 brass stems: stem fronts rise 0.5-1.7 dB, but the master at the accent onsets moves only from -0.7 to -0.5 dB and the 2-16 Hz modulation of J, N, O, P, R, T does not change within 0.1 dB. No change proposed.

**Timpani rolls (BRIEF 5).** Pass (measured). In the eight roll passages the timpani stem is 15.5-18.5 dB under the master and ranks 14th to 20th of 31 stems. The rise at bars 243-246 (-30 to -12 dB re master) is the printed p to f crescendo.

**Loop pulsing (BRIEF 7).** None found (measured). Only 22 sustain notes last 3.95 s or longer. The master's 100-300 Hz level autocorrelation at a 3.95 s lag is -0.22 (P), +0.01 (T), +0.19 (C), -0.29 (L); other lags from 2 to 8 s span -0.54..+0.47, so 3.95 s does not stand out.

**S1, S2, S3.** S1: improved on the basses, violas' gaps masked. S2: brass accents on time; the open cases are Flute 2 at 650 and 618 (finding 5) and Bassoon 1 at 464. S3: the subito at bar 42 and the tutti stops are clean; the remaining S3 fault is the sfp's second hump (finding 3).

## Comparison

Whole file, same method for every file:

| file | centroid of the loud 10 % (Hz) | side/mid 200 Hz-5 kHz (dB) | L/R correlation 125-250 Hz | level modulation 2-16 Hz (dB) |
|---|---|---|---|---|
| c00 | 1056 | -5.6 | 0.55 | -19.5 |
| c06 | 852 | -2.4 | 0.08 | -21.1 |
| c10 | 1015 | -5.4 | 0.46 | -19.0 |
| c11 | 1014 | -5.4 | 0.46 | -19.1 |
| Movement I c51 | 984 | -4.6 | 0.47 | -19.2 |
| Dvořák 9/i | 805 | -5.4 | 0.55 | -16.9 |

Octave shares of the loudest 10 % of frames (dB re the 40 Hz-16 kHz total):

| file | 63-125 | 125-250 | 250-500 | 500-1k | 1-2k | 2-4k | 4-8k | centroid (Hz) |
|---|---|---|---|---|---|---|---|---|
| c06 master | -15.0 | -5.4 | -6.5 | -8.5 | -6.9 | -10.3 | -19.1 | 852 |
| c11 master | -13.4 | -10.7 | -7.2 | -6.0 | -4.8 | -10.8 | -19.6 | 1020 |
| c11 mp3 | -14.6 | -11.9 | -7.4 | -5.9 | -4.4 | -10.6 | -20.2 | 1059 |
| Movement I c51 mp3 | -13.4 | -9.2 | -5.5 | -6.8 | -6.2 | -10.4 | -20.2 | 923 |
| Dvořák 9/i | -14.4 | -6.9 | -6.5 | -5.9 | -7.1 | -11.3 | -21.9 | 823 |

Per section, c11 against c00 and c06 (master level dB / centroid Hz / 2-16 Hz modulation dB), selected rows:

| section | c00 | c06 | c11 |
|---|---|---|---|
| D (200-264) | -36.6 / 547 / -17.1 | -39.2 / 733 / -21.7 | -41.2 / 858 / -20.5 |
| G-H (392-536) | -21.1 / 909 / -14.1 | -22.2 / 818 / -16.1 | -25.2 / 1016 / -14.4 |
| J (536-600) | -15.0 / 906 / -20.5 | -18.2 / 951 / -21.3 | -20.7 / 1000 / -20.2 |
| L-M (680-792) | -27.5 / 768 / -18.4 | -28.9 / 713 / -21.2 | -31.4 / 923 / -19.9 |
| N (792-840) | -16.1 / 879 / -20.3 | -18.2 / 791 / -21.9 | -20.6 / 937 / -17.3 |
| P (888-936) | -13.8 / 1279 / -19.8 | -17.6 / 1079 / -22.2 | -20.8 / 1153 / -20.9 |
| R (984-1080) | -12.7 / 1025 / -20.3 | -15.3 / 864 / -20.8 | -17.9 / 960 / -20.1 |
| T (1080-1113) | -10.6 / 1084 / -19.0 | -13.0 / 1039 / -20.3 | -15.8 / 1095 / -20.7 |

What changed, in words (measured). Against c06, c11 has more level movement in 14 of 17 sections (N +4.6 dB, Q +3.4, K +2.2, A +1.9), the stereo image is close to the recording (side/mid -5.4 dB, correlation 0.46), the repeats separate and the stops decay inside the ceiling. Against c00, the loud closing sections have less level movement (P -20.9 against -19.8; T -20.7 against -19.0). c11 is brighter than c00 and c06 in the soft sections (D 858 Hz against 547 and 733; L-M 923 against 768 and 713). c10 and c11 are the same in every whole-file measure; c11's changes are local.

Weakest passages now, in order:

1. Bars 147-150 (stop chord and sfp, qn 584-600): two humps on the sfp, and Horn 3's D4 carries the chord.
2. Bars 223-234 (the Maestoso chorale): the tempo is exactly 112.0 for 25.7 s and the level modulation is the lowest of the loud sections.
3. Bars 42-46 and 170-174 (soft transitions): the delivery gain rises during a printed p or pp.
4. Bars 155 and 163 (flutes' unison slurs in K): Flute 2 arrives 96-146 ms after Flute 1.
5. Bars 115-125 (bassoon solo): joins with dips up to 10.8 dB under a tempo of exactly 168.0.

What still sounds like a machine: (a) 98 of 279 bars at an exactly constant tempo; (b) tutti sections with 3-4 dB less level movement than the recording (-20 to -21 dB against -16.9 dB); (c) loud passages that are thin at 125-250 Hz and forward at 1-2 kHz in the delivered file; (d) gain movements of the delivery that do not follow the printed dynamics; (e) 14-18 % of the notes of 1.5 s or longer have flat CC1, CC11 and volume (winds 17 % of 292, brass 18 % of 290, strings 14 % of 247); (f) the basses' short notes in 792-840 use two velocities (83 and 91) on beats and off-beats alike.

## Ranked findings

### 1. Loud passages in the delivered file are thin at 125-250 Hz and forward at 1-2 kHz

Where: every tutti (A, B, F, J, K, N-T), in the mp3. All tracks; the fix is in the delivery only.

What is wrong (measured): in the loudest 10 % of frames the mp3's 125-250 Hz share is -11.9 dB. The recording has -6.9 dB and Movement I's c51 mp3 has -9.2 dB. The 1-2 kHz share is -4.4 dB against -7.1 dB (recording) and -6.2 dB (Movement I). The difference "1-2 kHz minus 125-250 Hz" is +7.5 dB in the Finale mp3, +3.0 dB in Movement I's mp3, -0.2 dB in the recording, and was -1.5 dB in c06. The 500 Hz-1 kHz share matches the recording (-5.9 dB both).

History (LEARNINGS, c07 and c08): c07 took the 100-250 Hz share from -5.5 to -8.5 dB, inside the references' range of -6.6..-8.8 dB. The c08 side shelves took the 125-250 Hz share from -8.5 to -11.3 dB; this was recorded as open and has not been corrected. The c09 side bells fixed the correlation, not the share. In addition c07 removed the template's 1.18 kHz -1.9 dB delivery bell and c08 halved the family mid cuts, while the delivery kept the template's 167 Hz -1.6 dB bell. Movement I still has both delivery bells.

Fix (file `build/mix.json`, key `"master_eq"`; no render needed, rerun `tools/deliver_master.py` on the c11 master to check):

- remove the row `{"type": "bell", "hz": 167.0, "db": -1.6, "bw": 1.39}`;
- add `{"type": "bell", "hz": 1500.0, "db": -1.5, "bw": 1.0}`;
- keep the 42 Hz high pass and the 6 kHz -3 dB shelf.

Simulated on the mp3's frame spectra (the limiter and the quiet-passage lift are not modelled): 125-250 Hz share -11.9 to -10.2 dB, 1-2 kHz -4.4 to -5.5 dB, 500 Hz-1 kHz -5.9 to -5.8 dB, 2-4 kHz -10.6 to -10.8 dB, centroid 1059 to 956 Hz, loud-frame level -0.24 dB. The difference "1-2 kHz minus 125-250 Hz" becomes +4.7 dB. Movement I's bell (1180 Hz, -1.9 dB, bw 1.39) in place of the 1.5 kHz bell gives the same within 0.3 dB (-9.9 / -5.5 / -6.1, centroid 961 Hz). Removing the 167 Hz bell alone gives -10.7 dB and 1011 Hz. A second step, if the first is accepted by ear: set the 167 Hz bell to +1.5 dB instead of removing it (125-250 Hz -9.1 dB, equal to Movement I's mp3; centroid 902 Hz).

Checks after the change: delivered LRA 14-16 LU, limiter under about 3 dB, and the tutti stop at bar 2 (now 0.46 s to -20 dB against the 0.50 s ceiling), because more low-mid level can lengthen the measured decay (inferred).

Notes. `master_eq` is on the c07 do-not-touch list for its shelf (delivered 6-20 kHz share); this proposal leaves the shelf. The comparison uses one recording of another piece, so it gives a direction; Movement I's mp3 is the same-tools reference and points the same way. Advice for the mix lens: do not cut further anywhere in 125-400 Hz.

### 2. The tempo is exactly constant in the chorale and in four other stretches

Where: bars 223-234 (qn 888-936, Maestoso chorale, 112.0 for 25.7 s); bars 99-134 (qn 392-536, 168.0, including the bassoon solo at 456-488 and its answer at 496-504); bars 1-10, 27-42 and 247-270. Together 98 of 279 bars. All tracks.

What is wrong: the tempo map has 424 points and a range of 73.5-185.9 bpm, but `PHRASE_ARCS` covers only 200-324, 680-784, 840-872 and 936-976 (measured from parts.json and score_config.py). In the chorale the map ramps from 142.75 to 112 over qn 880-886, then has no point until the step to 132 at 936. Trumpet 1's phrases run 888-912 and 916-936 with a bar's rest between them; neither phrase has any tempo movement. The BRIEF's research (batch 5, item 5) gives tempo changes on about 20 % of beats in performances. The chorale is also the loud section with the least level movement (-20.9 dB, against -19.8 dB in c00). That a listener hears this as mechanical is inferred; the data are measured.

Fix (file `build/score_config.py`, table `PHRASE_ARCS`; the tool's values are push x1.015, default slowing x0.96 / x0.92, "sub" x0.98 / x0.95 with no push):

- add `(888, 912)`: 113.7 bpm from qn 889 to 900, 112 to 910, then 107.5 and 103 on the last two quarter notes of bar 228;
- add `(916, 936, "sub")`: 109.8 and 106.4 bpm on the last two quarter notes of bar 234, before the step to 132. No ramp span starts at 936, so the arc is not skipped. Use "sub" and not "main" there, because "main" (x0.88) would make the step to 132 a 34 % jump;
- optional, for the bassoon solo: `(456, 472, "sub"), (472, 488, "sub")`.

Checks after the change: S2 on the brass entries of bars 223-228 (the leads are in seconds, so they should hold); the timpani roll and the `DOWNBOW_STROKE_AT` strokes of the violas at 892-912; the length of the mp3 (about +0.3 s). If the push makes the half-bar strokes uneven, use `(888, 912, "sub")`.

### 3. The sfp at bar 149 has a second hump 0.25 s after the mark

Where: qn 592; Bass trombone, Trombone 2, Horn 3, Tuba, Horn 1, Trombone 1 (Trumpet 3 for the front only).

What is wrong (measured): master level against the ff before, by window after the mark: first 0.1 s -0.9 dB; 0.1-0.2 s -1.5; 0.2-0.3 s -0.5; 0.3-0.4 s -5.2; the p from +0.45 s is -10.3 dB. The peak (+0.1 dB) is at +0.255 s. Per stem, 0.2-0.3 s against the first 0.1 s: Bass trombone +2.7 against -0.3; Trombone 2 +2.5 against -0.2; Tuba +1.9 against -1.0; Horn 3 +1.6 against +1.2. The front is right since c11; the sample then keeps rising while CC1 is held at 108 for 0.10-0.14 s (cause inferred), so the chord is struck, sags and swells again before the p.

Fix (file `build/score_config.py`; add to `LEVEL_SHAPES_S`, which takes seconds from a score onset; keep the c11 bumps and `FP_SPIKE_AT_MARK`):

- `LEVEL_SHAPES_S[track]` gets `(592.0, [(0.11, 0.0), (0.19, g), (0.30, g), (0.40, 0.0)])` with g = -5.0 for Bass trombone and Trombone 2, -4.0 for Horn 3 and Tuba, -3.0 for Horn 1 and Trombone 1;
- add the c11 bump `[(591.95, 0.0), (592.0, 3.0), (592.22, 3.0), (592.35, 0.0)]` in `LEVEL_SHAPES` to Bass trombone, Trombone 2, Tuba and Trumpet 3, which do not have it.

Simulated on the stems (returns not changed): first 0.1 s -0.3 dB, 0.1-0.2 s -2.0, 0.2-0.3 s -2.1, 0.3-0.4 s -6.1, p unchanged; the peak moves from +0.255 s to +0.055 s at 0.0 dB. With the notch alone the peak is -0.5 dB at +0.040 s. No patch row and no memory are needed. Trumpets 1 and 2 hold a printed ff there and are not part of the sfp.

### 4. The delivery gain rises during the soft passages after bar 42 and at bars 170-174

Where: qn 164-200 (bars 42-50) and qn 676-692 (bars 170-174), mp3 only. File `build/score_config.py`, `RIDE_TRIMS`.

What is wrong (measured): after the subito p the delivery gain is +6.0 dB at qn 164, +8.1 at 168, +10.0 at 172 and +11.0 at 176, a rise of 5 dB in about 4.3 s. The master goes -38.3, -40.8, -38.4, -39.0 dB over bars 42-45; the mp3 goes -32.1, -32.2, -28.0, -28.1. So bar 43 does not fall (master -2.5 dB), bar 44 is 4.2 dB over bar 43 (master +2.4), and the flute entry at qn 174 ends about 4 dB under the f of bar 41 where the master has 8.9 dB. At bars 170-174 the gain goes from +6.6 to +12.2 dB while the master falls 4.8 dB (-36.1 to -40.9), so the printed p to pp step is delivered as no change (-29.4 to -28.7 dB), and the 680 row adds a 3.2 dB gain step at bar 171.

Fix:

- 164 row (line 668): make the total gain rise linearly from +6.0 dB at qn 164 to +11.0 dB at qn 196. In dB added to the current row values: 166 -0.4, 168 -1.5, 170 -2.2, 172 -2.75, 174 -3.2, 176 -3.1, 180 -2.5, 184 -1.7, 188 -1.45, 192 -0.7, 196 0. I did not check whether `deliver_master.py` sums overlapping rows, so apply these inside the row.
- 680 row: start at +1.0 dB at qn 680 and reach +2.55 dB at qn 696, instead of +2.55 dB one quarter note after 679.

Computed from the measured bar levels (not run through the tool): bars 42-45 become about -32.3, -34.1, -31.0, -30.9 dB, so bar 43 falls 1.8 dB (master 2.5) and bar 44 rises 3.1 dB (master 2.4); the flute at 174 is about 7.1 dB under the f of bar 41. Expected LRA change +0.1 to +0.3 LU from 15.0 (inferred). The 680 change is not simulated. The c11 result that the row must be 0 at the mark stays valid; only the length of the rise changes (c11 tried 6 and 10 qn).

### 5. Flute 2 arrives 96-146 ms after Flute 1 on the unison slurs of bars 155 and 163

Where: Flute 2, score onsets 618.0 (D#6 to A#5) and 650.0 (D#6 to C#6), ff, unison with Flute 1.

What is wrong (measured): pitch crossing against the beat, Flute 1 / Flute 2: 618 +88 / +138 ms; 650 +26 / +146 ms. At 650 the lead is 321 ms (at the 0.35 s clamp), the new pitch stays 17-20 dB under the old one until +230 ms and reaches full level at +466 to +506 ms; the next note starts 535 ms after the beat, so the note is at full level for its last tenth. The dip is 18.3 dB (Flute 1: 0.6 dB). The actor's pcx gives +114 ms at 650 and +49 ms at 618 after c11's leads.

Why not velocity 122: the legato speed maps velocity 30-127 to 0-100 ms (kit LEARNINGS line 116), so 100 to 122 moves the transition by at most about 23 ms. More than 100 ms is missing and the lead cannot grow.

Fix (a re-attack with an overlap; Flute 1 keeps the slur, so the unison still sounds slurred):

- `build/leg_leads.json`: remove Flute 2's rows `"618.0": 0.12` and `"650.0": 0.17`;
- `build/score_config.py`: `ART_SPANS["Flute 2"]` rows `{"from": 617.9, "to": 618.1, "art": "Sus MAX"}` and `{"from": 649.9, "to": 650.1, "art": "Sus MAX"}`;
- keep the previous notes' ends at 618.04 and 650.04 (no `WIND_DETACH` gap on these two joins) and give the new notes the wind entry lead (about 0.055 s), so the two Sustain notes overlap by about 70 ms.

Expected (inferred; the kit's re-tongue recipe and c06 A, where a plain re-tongue without overlap left 6-12 dB holes): Flute 2 within ±40 ms of Flute 1 at both joins and a dip under 6 dB. In parts.json the two notes should read "Sus MAX" with a moved onset about 0.15 qn before the beat. If the tool does not accept a Sustain note inside a slur through `ART_SPANS`, this needs a small tool option; I did not test the tool.

### 6. The 315 Hz hump in J is pitch content; stop tuning to that figure

Where: qn 536-600, mainly the stop chord 584-600. Horn 3, Violas, Bass clarinet, Trombone 2.

What is measured: master hump (315 Hz third octave over the mean of 250 and 400 Hz) J 7.9 dB, stop chord 10.4 dB, P 4.5, R 5.1, whole movement 4.1 dB. Shares of the master's 315 Hz band in the stop chord: Horn 3 -4.5 dB (its own hump 39.3 dB), Violas -7.7, Bass clarinet -9.7, Trombone 2 -9.9, Tuba -11.6, Violoncellos -12.2. In 552-564 it is Horn 1 (-3.4) and Violas (-3.9). A semitone spectrum of J has D4 (293.7 Hz) as the loudest semitone; the neighbours inside the 250 Hz band are 12-29 dB lower. D4 to F4 lie inside the 281-354 Hz band, so the figure follows the key of the passage. The recording's -0.4 dB comes from another piece in another key and is not a target for this bar.

Consequence: a string family bell at 315 Hz (Movement II's step) would cut the violas' and celli's fundamentals, would not reach Horn 3, Trombone 2 or the bass clarinet, and would lower the 125-400 Hz region that finding 1 shows is already low. Do not add it. If the stop chord is still judged heavy on D4 by ear, treat it as a balance question of one chord: Horn 3 -1.5 dB on qn 584-600 in `roles.json` (not simulated; Horn 3 is 3.2 dB over the next source there). Record in LEARNINGS that the hump figure of a single section is not a valid target.

## Do not touch

The basses' beat gaps and metric tables with the CC16 resets; the string, wind and brass sf bumps at 592 and `FP_SPIKE_AT_MARK` (0.10 / 0.30 s); the violas' chord gaps; Bassoon 1's trimmed leads; the bar-275 shapes; the returns, envelope, faders and register sends (wetness is inside the ceiling and at its dry end); `FINAL_RING`; the trumpets' ff trims; the final ride row and the fitted soft ride rows other than the two changes of finding 4; the side bell layout and track widths; the family EQ and the delivery's 6 kHz shelf; the string release caps; the legato velocity floor with its leads; the climax order (bars 223 and 278); the brass `GENTLE_ACCENT` swell (simulated change gave nothing on the master); the tuba and contrabassoon levels in 984-1056; no "Leg Slur Exp" on more tracks and no 315 Hz string bell.

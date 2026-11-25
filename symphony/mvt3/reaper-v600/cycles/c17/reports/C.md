# Cycle 17, critic C: blend and space (render of cycle 16)

Material: `cycles/c16/render/` (31 stems, four returns, `00_Master.wav`), `cycles/c15/render/00_Master.wav` (the c15 stems are deleted), `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, `cycles/c16/CHANGES.md`. Every number is measured on these files unless marked "inferred". Nobody in the loop can hear, so every statement about audibility is an inference.

Measures. Stop: 20 ms RMS envelope, reference = mean of the 0.16 s before the stop, drop at +0.3 s, time to -20 dB. Band levels: FFT power of the mono sum over the stated span. "Share" = band power over full-band power.

Limits of this report. I ran out of working time before measuring everything the coordinator listed. Not measured by me on c16: pizzicato evenness (51-66), divisi chord levels outside the roled passages, Violins II sustain notes next to legato rows, the sfp at bar 149, dal niente entries, bar 222, long notes sagging on "Sus MAX", the theme head's fall, accent amounts per family, the basses' short-row timing, brass tongued separation, timpani stroke velocity. These belong mainly to lenses A and B; I give no values for them. I did not read FINDINGS.md Parts 1-6 in full in this cycle (I used the BRIEF's research sections and the c13 blend report, which cite them); no finding below contradicts a research default except finding 1, which is flagged.

## Manual notes

Third round, no fixed pages. Pages behind this lens's open problems, May 2021 HO Opus manual.

| Manual (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.138: Main mics stand about five rows back and capture "more room reflections than direct sound"; Close mics stand in front of each section. | Double basses (Close 0.5, Main 1.0). The +9 to +12 dB excess of F2 (87.3 Hz) appears only in the loud layer (finding 1) and is a narrow single-pitch peak, which is the behaviour of a room resonance in the Main pair (inferred). | Not tested. A Close-led bass mic mix has never been range-rendered. Finding 1 gives the test. |
| p.139: each mic position is loaded and unloaded separately, with its own volume. | Same. A Close-led mix on one track costs no extra memory (both positions are already loaded). | Applies to the test in finding 1. |
| p.222: the room "is heard as long as the samples are playing (including the release trail samples)". | Tutti stop of bar 204 (qn 814). | The tail there is the celli's G2 release trail, not the returns (finding 2). A return ride cannot fix it. |
| p.142 (4.2.9 Envelope): Release sets how long a sound stays audible after note-off; instruments ship with programmed values. | `sus_release_cap_ms` (strings 150 ms at f/ff). | In use. The cap shortens the sustain group's release but not the separate release-trail sample, which is what holds the bar 204 tail (finding 2); with a 150 ms release and a slow new attack, a same-pitch re-bow leaves a 10-13 dB hole (finding 3). |
| p.142: reverb pre-delay and volume; p.141: reverb on/off, "Load with Effects Off". | Opus hall off on every track; four Spaces II returns. | Yes. Returns against dry are -12.2 to -13.8 dB in every loud section (table under "Ending"). |
| p.138 (Mid: "definition without the sound of close proximity"), MANUAL-GAPS #4. | Woodwind solos. | Still never loaded. Not asked for in this cycle; the faults below rank higher. |

## Answers to the coordinator's blend questions

Ending (bars 271-279), level. Right, measured against c15: master c16 minus c15 is -0.4 dB (271-272), -0.4 dB (273-277), +0.4 dB (278), and within 1 dB in each of 125-500 Hz, 500-2000 Hz, 2-6 kHz and 6-16 kHz, except 125-500 Hz at 271-272 (-1.6 dB). The passage roles restored the c15 balance.

Ending, room. Slightly dry on the strings in the delivered stems, and only there. Return under its family's dry sum:

| span | strings | brass | winds | perc | all returns under all dry |
|---|---|---|---|---|---|
| 151-170 | -13.6 | -13.7 | -9.3 | -6.7 | -12.2 |
| 199-210 | -13.1 | -14.3 | -10.4 | -6.6 | -12.6 |
| 223-234 | -15.1 | -13.5 | -9.6 | -8.9 | -12.5 |
| 247-270 | -13.8 | -14.0 | -9.4 | -7.9 | -12.6 |
| 271-272 | -17.0 | -14.8 | -9.6 | -6.1 | -13.4 |
| 273-277 | -15.0 | -14.8 | -10.1 | -7.1 | -13.3 |
| 278 (final chord) | -14.0 | -16.1 | -12.7 | -8.8 | -13.8 |

The hand scaling of the string return (`retfix.py`, -3.5 and -6.0 dB) left the string hall 3.4 dB lower against its dry sum in 271-272 and 1.5 dB lower in 223-234 than in the other loud sections. The scaling applied one value to the whole return while only Violins I / II / Violas were lowered dry; the celli also send and were not lowered. The saved project uses post-fader sends, so the next render should give about -13.5 dB without any change. Check after the c17 render: R Strings under the string dry sum within -13.5 +-1 dB in 223-234 and 271-277. The final stop is in range (my reading 14.9 dB at +0.3 s, 0.42 s to -20 dB). No change asked.

Low end. Solid on G and A flat, thin on F, and the tonic is lighter than the dominant. Details and fix in finding 1. Whole-file shares c15 -> c16: 28-56 Hz -28.9 -> -26.9 dB, 56-112 Hz -14.2 -> -11.2, 112-224 Hz -10.1 -> -11.7, 224-450 Hz -7.2 -> -7.3. The 56-112 Hz band is now within 3 dB of the Brahms figures and no more should be added across the board: the three bars with the largest 30-125 Hz share are already at -3.4 dB (bar 35), -4.3 (bar 25) and -4.8 (bar 152), all with the basses alone on G1 or A flat 1.

Timpani rolls. In order. The timpani's part of the master's 30-150 Hz power in the seven rolls I checked (147-152, 209-210, 219-222, 231-238, 243-246, 261-262, 273-277) is 2-7 %, and the timpani is in none of them among the three loudest stems.

Muted Trumpet 1 against the cor anglais (bars 171-186). Room is now matched: no change. Stem levels -54.5 dB (trumpet) and -48.6 dB (cor anglais); band shares 180-355 Hz -29.3 against -9.8 dB and 1.4-2.8 kHz -5.4 against -15.4 dB, which is what a straight mute does. The trumpet is 5.9 dB under its doubling partner; whether that is the intended balance is for B.

Bar 204. Finding 2.

Per-note fader moves still in `parts.json`. Finding 4.

## Findings, ranked

### 1. The bottom octave is uneven by pitch, and the F2 bell is right only at ff: F chords lose their bass (bars 213, 215, 217, 228), the tonic is lighter than the dominant

Where: Double basses, whole movement; worst in bars 213-217 and 228 (the chorale's subdominant chord, qn 908), and 255-256.

Evidence (measured).
- Basses' "Sus MAX" notes of 0.3 s or longer with CC11 at 100 or more, level less the fader, median per pitch against the median of the pitch medians: F1 -5.1 (n 3), G1 +0.5 (20), A flat 1 +2.7 (5), B flat 1 0.0 (8), B1 +1.7 (2), C2 +2.7 (7), C sharp 2 +4.3 (3), D2 -0.9 (12), E flat 2 -5.5 (6), F2 -2.9 (5), G2 -0.1 (2), D3 -9.3, E flat 3 -6.2, F3 -10.7 (2 each). Spread 9.8 dB over the pitches with three notes or more.
- With the -12 dB bell, F2's fundamental band at ff is -42.2 dB, level with G2 (-42.8) and D2 (-40.7). So at ff the bell is about right, and the natural excess of the loud layer is 9-12 dB (the actor's range tests agree: +9.9 dB with the bell at -4).
- At CC11 84 (the chorale, velocity 83) the same bell overcorrects. Basses' stem in 30-125 Hz per bar, same CC11 and fader: C2 -41 to -43 dB (bars 224, 225, 229-233), B1 -43, A1 -44, F2 -54 (bar 228), F2 -52 (bar 215), F2 -54 (bar 217). The F2 fundamental is 10-12 dB under its neighbours there. The excess that the bell removes exists only in the loud layer.
- In the master the F bars have a hole in 30-125 Hz: bar 228 -54.0 dB against -39.7 to -42.4 in bars 224-227 and 229-233 (12-14 dB); bar 215 -51.8 and bar 213 (F sharp 2) -46.8 against -37.4 in bars 211 and 214. The tuba (F1, -61 dB) and contrabassoon (F1, -68 dB) do not fill it; the tuba's own 84 Hz -5 dB bell sits on F1's second partial.
- Share of 30-125 Hz in the master's loud bars (127 bars at -29 dB or more), median by the basses' main pitch: G1 -7.6 dB (19 bars), A flat 1 -7.9 (11), C2 -12.0 (29), D2 -10.3 (11), F2 -12.9 (8), E flat 2 -15.2 (7), F1 -15.3 (4), E2 -17.8 (4). Absolute band level: G1 -33.5, C2 -35.8 dB. The dominant carries 2.3 dB more bass than the tonic in level and 4.4 dB more in share. The final chord (bar 278, C2) has -29.8 dB in the band against -25.8 in bar 262 (G1) and -25.2 in bar 148 (G1), although its master level is 1-2.5 dB higher.
- Boomy places: bars 35 and 198 (basses alone on A flat 1, share -3.4 and -5.5 dB) and bars 25 and 152 (G1, -4.3 and -4.8). These are 3-5 dB over the Brahms whole-file figure of about -8. Mild; they come from the same pitch unevenness.

Fix, in this order. All of it is on the instrument or in the static EQ; none of it is a fader move.

(a) Make the F2 bell depend on the dynamic, which is where the excess is. `build/mix.json`, "Double basses": `eq` 87.3 Hz bell -12 -> -2 dB (bw 0.15 oct kept), and restore the score-timed `loud_eq` mechanism that c16 deleted from this track, with one band: 87.3 Hz -10 dB, bw 0.15 oct, active only where the basses' `dyn_curve` is 105 or more (the ff passages; the mechanism switched by passage in Movement I's mix). If the tool can no longer switch an EQ band by passage, the alternative with the same effect is (b). This is a per-pitch fix for F2, so it does not reopen the closed item "relaxing the bell without a per-pitch fix"; record it in LEARNINGS either way. Targets: basses' 30-125 Hz level on the F2 of bars 215, 217 and 228 within 3 dB of the C2 bars beside them (now 10-12 dB under); F2 at ff within 3 dB of the pitch median (now -2.9); master 30-125 Hz in bar 228 at -44 dB or higher.

(b) Range test under the lock, one track, no memory cost (manual p.138-139): Double basses mics Close 1.0 / Main 0.4 against the current Close 0.5 / Main 1.0, bell bypassed, bars 11-34 and 223-234. Measure the same per-pitch table. Accept the Close-led mix if F2's excess at ff is under 4 dB and the spread over the pitches with three notes or more is under 6 dB; then the bell can go to -3 for all dynamics. Check the stops of bars 2, 6 and 94 afterwards: the basses hold the 30-125 Hz tail at bars 94 and 166 (0 to -1 dB against the master's tail in that band).

(c) Per-pitch CC11 offsets for the pitches that stand out upward, where there is room to move. New table in `build/score_config.py` (generic code in `tools/score_to_parts.py`: an offset added to CC11 over each note of the listed pitch on "Sus MAX" / legato rows, held for the whole note, no ramp inside the note), "Double basses": C sharp 2 (MIDI 37) -14, C2 (36) -9, A flat 1 (32) -9, B1 (35) -6 units; values from the table above at about 0.3 dB per unit near the top of the range (kit section 4 gives 0.20-0.32; refit after one range render). Exception: no offset on C2 in bars 223-234 and 271-279, where the tonic needs its weight. The weak pitches (E flat 2 -5.5, F1 -5.1, D3-F3 -6 to -11) cannot be raised by CC11 at ff (CC11 114-119 of 127 gives at most +2 dB). For those I see no instrument-side fix other than the mic test in (b); say so in CHANGES if (b) does not close them. E flat 2 lies 0.17 octave under the bell, so (a) should return part of its loss (inferred, 1-2 dB).

(d) Tonic weight at the end: after (a)-(c), if bar 278's 30-125 Hz level is still more than 2 dB under bar 262's, raise the Contrabassoon's and Tuba's CC11 / CC1 over qn 1108-1113 (they are 16-18 dB under the basses in that band there), not the basses.

Judgement: the pitch table, the dynamic dependence of the F2 excess and the holes in the master are measured. That the peak is a Main-mic room resonance is inferred. Audibility of a 12 dB loss of bass on the chorale's F chord is inferred; I rank it first because it is in the slowest, most exposed tutti of the movement.

### 2. Bar 204 stop (qn 814): the tail is the celli's G2 release trail, so a return ride will not fix it

Evidence (measured). Stop: 12.6 dB at +0.3 s, 0.52 s to -20 dB (c15 by the same measure 13.7 dB / 0.50 s). Stems against the master's tail from +0.2 to +0.5 s: full band Violoncellos -3.7 dB, Horn 2 -11.4, R Strings -12.2, Timpani -13.2, Double basses -13.9, R Brass -14.0. In 30-125 Hz the tail is only 3.1 dB under the body (-40.3 against -37.2 dB) and the celli are 1.0 dB under the master's tail; in 125-250 Hz the celli are 0.4 dB under it. The cello stem falls from -31 dB to -41.8 dB at +0.3 s (10.5 dB; the basses fall 16 dB in 0.1 s). The note is the celli's G2 (MIDI 43, velocity 111, qn 812.79-814.0, "Sus MAX"); it also rises 1 dB at the note end, which is the release-trail sample entering (manual p.222).

Simulated on the c16 stems (dry stems only; the post-fader send follows, so the real effect is a little larger):

| change | drop at +0.3 s | time to -20 dB |
|---|---|---|
| none | 12.6 dB | 0.52 s |
| all four returns -3 dB from the stop | 13.4 | 0.52 |
| all four returns -6 dB | 13.9 | 0.52 |
| celli tail -6 dB (ramp from +0.02 to +0.22 s) | 14.3 | 0.50 |
| celli and basses tails -6 dB | 14.7 | 0.48 |
| celli and basses tails -9 dB | 15.1 | 0.48 |
| celli note ends 0.08 s earlier | 13.9 | 0.46 |

Fix (bar 204 only; instrument side).
- `build/score_config.py`: end the celli's G2 and the basses' G1 of qn 812.8 at qn 813.78 instead of 814.0 (`NOTE_END_AT`, Movement I's tool option; 0.22 qn = 0.08 s at this tempo). The other parts keep their length, so the cut-off itself stays together within 80 ms.
- CC11 fall after the note-off on both tracks, inside Opus and before the send (S3-safe): Violoncellos and Double basses CC11 at qn 813.78 unchanged (118), then 96 at +0.08 s and 80 at +0.20 s, back to the next entry's value at qn 815.5 (celli enter at 815.65, basses at 815.99). Aim: 6 dB off the release trail. If CC11 does not reach the trail samples (Movement I c40: the trail groups take CC11 as a start-mode controller, so they may latch the value at note-off), put the fall before the note-off instead: CC11 118 -> 100 over the last 0.15 s of the note.
- No return ride at this stop. Do not add a negative `return_rides` row: -6 dB on all returns gives 1.3 dB and leaves the time unchanged.
Targets: 14.5-17 dB at +0.3 s and at most 0.50 s. The two changes together should give about 15.5 dB / 0.44 s (inferred from the table; the rows are not additive exactly).

Judgement: cause measured; fix values from simulation; the CC11 behaviour on trails is inferred and needs the range render.

### 3. The chorale's pedal C: the master dips 4 dB at every bar line of 224-234, and the celli change bow off the bar

Where: Violoncellos and Double basses, qn 912-936 (bars 229-234); the same join type at qn 1092-1104 (bars 274-276).

Evidence (measured).
- Printed (mockup-events.tsv): celli C3 and basses C2 as separate whole notes in every bar from qn 912 to 932, no ties. Played basses: note-ons at 915.81, 919.81, 923.81, 927.81, 931.81 (on the bars, 0.19 qn early). Played celli: note-ons at 915.33, 919.97, 924.62, 929.26, that is 0.36 s before bar 230, on bar 231, 0.33 s after bar 232 and 0.67 s after bar 233. `STR_REP_NEW_BOW["skip"]` merges both tracks over 892.5-940.5 and the re-bow spacing (4.64 qn) then decides where the celli change. The celli's CC11 still dips to 74 at each bar line (916, 920, 924, 928) and returns to 88 a quarter of a beat later, inside a sounding note, so the stem has a CC dip at the bar and a separate bow change elsewhere.
- Dip at each join (lowest 20 ms frame in the 0.4 s after the join against the 0.26 s before): basses -6.2, -13.1, -9.9, -12.7, -13.5 dB; celli -5.9, -11.8, -5.8, -11.7 dB. Master at the five bar lines: -4.3, -4.4, -4.3, -4.4, -4.1 dB. The c15 fader fills that covered these are gone (c15 measured 0.5 to -0.9 dB).
- Bars 274-276: celli -5.9, -6.1, -2.8 dB, master -1.9, -5.1, +0.1 dB. Violins I at qn 896 -8.3 dB (master -3.0) and at qn 1095.83 -6.3 dB (master -4.7).
- Cause of the depth: the old note's release is capped at 150 ms at f (`sus_release_cap_ms`, manual p.142) and stops 0.19 qn (0.10 s) before the new note-on, whose "Sus MAX" attack is slow; nothing sounds in between.

Fix (instrument side).
- `build/score_config.py` `STR_REP_NEW_BOW["skip"]`: take Violoncellos out of the 892.5-940.5 skip from qn 912 on (keep 892.5-912 if the merge is wanted there), so the celli play the printed whole notes and change bow on the bar lines with the basses and the brass chord changes. Delete the celli's CC11 dips at 916-928 if they are then written twice.
- For both tracks in 912-936 and the celli in 1088-1104: no gap. Old note-off at the new note's moved note-on plus 0.04 s (an overlap is not possible on the same pitch, so let the 150 ms release run under the new attack), new note 0.10 s early as now (`sus_lead_s`), and a CC11 rise of 8 units from 0.10 s before the join to 0.15 s after it, then back over 0.3 s. That is a bow-change swell on the instrument, the shape the fader fill had.
- If the dip is still over 5 dB in the stem: stagger the two tracks, basses on the bar and celli 0.5 qn later (two desks changing at different times, the score's "change bow at will" at 936 applied four bars early). I rank this second because it departs from the printed attack points.
Targets: stem dip at most 5 dB, master dip at the bar lines of 229-233 at most 2 dB (the brass re-tongue on the same bar lines, so about 1-2 dB is the natural minimum; inferred).

Judgement: positions and dips measured; that a 4 dB master dip at every chord change is heard as chords that do not connect is inferred. Loop pulsing (BRIEF item 7) was not re-measured.

### 4. Fader audit: no per-note rule is left, but 34 sudden steps of 2 dB or more still fall inside sounding notes

Evidence (measured on `parts.json` `vol_db`, before the build's thinning: 17,404 points). Moves of 2 dB or more within 0.06 s: 222, of which 94 lie at a note-on, 27 in rests, and 101 strictly inside a sounding note (more than 0.05 qn from both ends). Of the 101, 59 are the final fade after qn 1113 (correct, leave). The other 42:
- Releases of a hairpin gain written at the score onset while the led note has already started: 3 dB in 5 ms at qn 910.0 (Oboe 1, Violins I, Violins II), 914.0 (Flute 2, Oboe 2, Violins I, Violins II), 932.0 (Flute 2, Oboe 1, Oboe 2, Violas, Double basses), 296.0 and 776.0 (Violins I -3 -> 0 and Violins II 0 -> +3: a role swap), 384.0 (Violas, Violoncellos, Double basses -9.5 -> -6.5), 532.0 (Violins II), 552.0 and 968.0 (Violoncellos; 968.0 also Double basses), 950.0 (Violins I / II +3), 1056.0 (Double basses +3), 1032.0 (Bass trombone +3.6 in 51 ms), 360.09 (Horn 2 -2.2). The note in each case starts 0.12-0.64 qn before the step (its lead), so the step is heard inside the note's first 60-300 ms.
- Player-count and role steps: Violins I 472.9 and 484.9 (-3 dB, "4 soli"), Violins II / Violas / Violoncellos 375.9 (-4 dB, "last 2 desks"; the three notes started at 375.41-375.66).
- Timpani, instant steps at roll ends, 0.05 qn before the next stroke: -5.9 dB at 19.95, -7.3 at 139.95, -5.9 at 591.95, -8.5 at 835.95, -7.3 at 983.95 (the roll's gain stands at +12.3 dB before it), -6.4 at 1043.95, -2.8 at 1047.95; +5 dB steps at 20.5 and 140.5 inside the following stroke's ring.

These are slow-layer rows (hairpin gains, roles, player counts, roll levels), so they are inside Dan's rule in kind, but each is a per-note-sized move in effect. Fix, without adding any per-note rule:
- `tools/score_to_parts.py`: key the end of a hairpin gain, a role edge and a player-count step to the moved note-on (`qn`) of the first note it applies to, minus 0.03 s, not to the score onset; where the previous note abuts, ramp over the last 0.25 qn of the previous note. This removes the group at 910 / 914 / 932 / 296 / 776 / 384 / 532 / 552 / 968 / 950 / 1056 / 375.9 / 472.9 / 484.9.
- Timpani: move the roll level into the instrument. The roll rows take CC1 for their layers (manual p.124-126, cited in MANUAL-READING row 3 B) and CC11 for level; put the roll's settle and hairpin into CC11 / CC1 and let the fader hold one value across roll and stroke. The +12.3 dB roll gain before qn 984 is the largest fader move left in the project; at least cap what the fader carries at 4 dB and move the rest to CC11. The following stroke's level then comes from velocity (B's item).
Target: no move of 2 dB or more within 0.06 s strictly inside a sounding note except the final fade.

Judgement: counts measured from the data; audibility inferred (a 3 dB step 5 ms long on a held wind or string note is the kind of artefact c16 removed elsewhere).

### 5. The strings' hall in the ending and chorale stems (check only)

See "Ending, room" above: R Strings is 3.4 dB lower against the string dry sum in 271-272 and 1.5 dB lower in 223-234 than in the other loud sections, from the hand scaling of the return stem. No config change. After the c17 render, verify R Strings under the string dry sum at -13.5 +-1 dB in both spans; if a stem fix again changes string roles after the render, scale the return by the power-weighted change of the sending tracks (celli included at 0 dB), not by the violins' role value.

## Not changed by c16, still as c13 found

Returns against dry are -12.2 to -13.8 dB in every loud section; every stop except bar 204 is inside 14.5-17 dB by the actor's measure (my readings: bar 94 15.0 dB / 0.40 s, bar 166 15.3 / 0.46, final 14.9 / 0.42; my readings at bars 2 and 6 are 13.9 / 13.6 dB because I placed the stop at qn 5.0 and 21.0, not 5.06 and 21.06, so they do not contradict the actor's 15.1 / 15.4).

Do not touch: the return faders, sends and `irSetup`; the stop rides at bars 2, 6, 113 and 166; the Bassoon 1 and Trumpet 1 sends of c13; the timpani roll levels as heard (2-7 % of 30-150 Hz, never among the three loudest stems), only their carrier changes in finding 4; the passage roles of the c16 stem fix (the ending is within 0.4 dB of c15); the 72 Hz +4 bell and the celli's c16 EQ; the 56-112 Hz share (-11.2 dB): add no general bass boost; the muted trumpet's tone and room; the final chord's ring (14.9-15.5 dB at +0.3 s).

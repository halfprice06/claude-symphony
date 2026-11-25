# Cycle 13, critic C: blend and space (render of cycle 12)

Material: `cycles/c12/render/` (fixed stems, the four returns, `00_Master.wav`), `cycles/c12/mvt3-mockup-c12.mp3`, `cycles/c11/render/00_Master.wav`, `cycles/c11/mvt3-mockup-c11.mp3`, `build/parts.json`, `build/mix.json`, `build/score_config.py`, `tools/deliver_master.py`, `cycles/c12/CHANGES.md`. Every number is measured on these files unless it is marked "inferred". Nobody in the loop can hear, so every statement about audibility is an inference from the measured numbers.

Stop measure: 20 ms RMS envelope; reference level = mean of the 0.15 s before the stop; "drop" = fall 0.3 s after the stop; "time" = time to -20 dB. Recordings fall 13-17 dB in 0.3 s and reach -20 dB in 0.43-0.58 s. Dan's ceiling: -20 dB in 0.50 s or less, RT60 1.5 s or less.

Short verdict. The mix is right: neither too wet nor too dry. The master is inside the ceiling at every stop and equal to c11 within 0.1 dB. The delivered mp3 is at the ceiling at bar 2 (0.49-0.50 s) and falls less than the recordings at bars 2, 6 and 94. The cause is the delivery gain, which rises through the stop, and the celli's own release, not the returns. The new delivery tone is an improvement by measurement. The largest blend faults are local: the Bassoon 1 solo has no hall, and the Trumpet 1 solos are 4-5 dB drier than the other solos.

## Manual notes

May 2021 HO Opus manual. Cycle 13 has no fixed page range, so these are the pages behind this lens.

| Manual (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.138-139: Close mics stand in front of each section (direct sound), Mid at the stage edge (definition without closeness), Main about five rows back (more room than direct sound). Each position is loaded or unloaded separately. | All tracks. Woodwinds are Close-led (Cor anglais Close 0.912 / Main 0.24, Oboe 1 0.939 / 0.088, Flute 1 0.815 / 0.475, Bassoon 1 0.884 / 0.329). Brass and strings are Main-led (Close 0.31-0.5, Main 1.0). | Yes, and it matches the EW template (FINDINGS 1). Woodwind stems are the driest and narrowest (tail -21.5 dB at 0.15-0.25 s after their stops; L/R correlation 0.85-0.99). Mid has never been loaded (MANUAL-GAPS #4): finding 6. |
| p.222: the mic mix decides how dry or wet an instrument sounds; the recorded room is heard as long as samples play, release trails included. | Tutti stops at bars 2, 6, 94. | The tail of these stops below 250 Hz is the celli's and basses' release trails, not the returns: finding 1. |
| p.142, p.220-221: reverb pre-delay; IR envelope (none, simple, full with end time and fade-out). The pages describe the Opus reverb; the returns here are Spaces II with the same envelope idea (`irSetup` envelopeMode 2, endPos 0.5, decayLength 0.5). | The four returns. | Yes. The same fractions give different lengths per IR: RT60 after the final chord R Strings 1.6-1.8 s, R Brass 1.6, R Winds 1.95-2.07, R Perc 1.3-1.4: finding 5. |
| p.196-198: sub-mixer channels (one per mic position), FX bus and the effects send with its level slider. p.140: the master pan keeps the mics' relative panning; the gain does not change the mic mix. | REAPER sends replace the Opus FX bus; they are post-fader, so level shapes move the hall with the dry signal. | Yes. The sfp notch at qn 592 and the notches at qn 325 and 728 do not cut the hall (measured, see "New in c12"). |
| p.136: the Classic mood is the Main mix with the Southern California hall; the Soft mood uses the Mid and Surround (or Vintage) mics through a larger hall. | Soft solos: bars 115-122, 171-186. | Moods are not used (mic mix and hall are set by hand). The Soft mood's mic choice supports the Mid trial in finding 6. |
| p.89-90: a divisi instrument holds one half of a section, in Close mics only; the other positions come from the non-divisi patch at adjusted loudness. | Violins I "dolce, 4 soli" / "gli altri" qn 473-511; "last 2 desks" at qn 376; MANUAL-GAPS #7. | Not used. The 4 soli line plays the full-section patch at velocity 41 and lies 19 dB under the master (stem -64.3, master -44.9 dB; Bassoon 1, Clarinet 1, Harp and Violas are all louder), so the patch choice cannot be heard there. No change asked. |
| p.106-107: brass legato slur patches take loudness from CC1 and the speed of the slur from velocity; the muted articulations are only listed. | Trumpet 1 "Mute Sus", qn 680-744 (the trumpet KS Master has no muted legato row, c12 note). | Emulated with note overlaps; two-pitch time median 70 ms in c12: open item (a). |
| p.116-117: each crash-cymbal pair has three lengths, each in a round robin of three takes; CC11 and velocity set loudness. | Strokes at qn 887.96, 1047.94, 1107.98, all velocity 124. | Partly. The three strokes differ by 3.7 dB at 4-12 kHz in the stem; the weakest falls on the fff of bar 263: finding 4. |
| p.122: 36 in Ludwig bass drum, D1 = felt long; CC11 and velocity set loudness; round robin of four. | Strokes at qn 888 and 1108. | Yes. 30-90 Hz rises by 4.9 and 10.5 dB in the master at the two strokes. No change. |

## Wetness, limiter and tone (coordinator item 1)

Drop at +0.3 s / time to -20 dB (ranges are the aligned and unaligned mp3 readings):

| Stop | c12 master | c12 mp3 | c11 mp3 |
|---|---|---|---|
| bar 2 | 13.1 dB / 0.44 s | 11.6 / 0.49-0.50 | 12.5 / 0.47 |
| bar 6 | 13.9 / 0.43 | 12.6-12.7 / 0.44-0.45 | 13.4 / 0.44 |
| bar 94 | 13.1 / 0.41 | 11.3-11.8 / 0.41-0.42 | 12.7 / 0.41 |
| bar 113 | 18.4 / 0.31 | 17.2-17.6 / 0.36-0.37 | 18.5 / 0.32 |
| bar 166 | 14.6 / 0.39 | 14.0-14.6 / 0.39-0.40 | 16.1 / 0.37 |
| bar 204 | 14.3 / 0.44 | 14.0-14.1 / 0.44 | not measured |
| final chord | 15.2 / 0.43, RT60 1.30 s | 14.2-15.0 / 0.47, RT60 1.45 s | 13.8 / 0.43, RT60 1.45 s |

Bars 18 and 26: master 15.9 dB / 0.21 s and 19.7 dB / 0.32 s. The c11 master equals the c12 master within 0.1 dB at every stop.

- Too wet, too dry or right: right (measured against the ceiling and the recordings). The master passes at every stop. Returns against dry are -13.9 dB over the movement (by section -10.5 to -15.0 dB). The dry sum alone decays in 0.42 s at bar 2, so the returns add 0.02 s there. Lowering the returns would not gain margin. The mp3's loss of margin is treated in finding 1.
- Limiter: the pre-limiter peaks are +1.11 dBFS at 420.98 s and +0.11 dBFS at 419.33 s (both in the final chord) and -1.25 dBFS at 329.53 s, against a limit of -1.5 dBFS. The limiter works 2.6 dB and 1.6 dB in the final chord and 0.25 dB or less everywhere else. Inside the limit of about 3 dB. No change.
- New tone: an improvement by measurement. Loud-10 % octave shares, c11 mp3 -> c12 mp3 (Dvořák 9 first movement / Movement I c51 mp3): 90-180 Hz -12.4 -> -10.5 dB (-7.6 / -10.9); 180-355 Hz -8.1 -> -6.8 (-8.3 / -6.2); 710-1400 Hz -5.4 -> -6.1 (-6.5 / -7.8); 1.4-2.8 kHz -6.0 -> -7.4 (-8.8 / -6.9); spectral centroid 1059 -> 928 Hz (823 / 923). Every changed band moved towards at least one reference and the centroid towards both. Whether it is better by ear is inferred from that.
- Low-end build-up: none. Whole-file 20-100 Hz share: c12 mp3 -14.5 dB, Dvořák (lossy) -21.6, lossless Brahms set -7.9 to -8.9. Master power against the sum of stem powers in the loud 40 % of bars: 31.5-63 Hz median -0.1 dB, 63-125 Hz -0.1, 125-250 Hz +0.1, so the low instruments do not cancel each other. The largest loss is 2.6-2.9 dB in 63-125 Hz on the G2 unison of bars 2 and 6.
- Image: L/R correlation per band (under 125 Hz / 125-250 / 250-1k / 1-5k / 5-12k): c12 mp3 0.61 / 0.47 / 0.51 / 0.53 / 0.46, Dvořák 0.60 / 0.54 / 0.55 / 0.60 / 0.37; side-to-mid within 0.7 dB of the Dvořák up to 5 kHz.

## Findings, ranked

### 1. The delivered mp3 loses the stop margin that the master has (bars 2, 6, 94; final chord)

Where: stops at qn 5, 21, 374 and the final chord (ends qn 1113). Delivery chain; Violoncellos; Double basses.

What is wrong: at bars 2, 6 and 94 the mp3 falls 11.3-12.7 dB in 0.3 s. The master falls 13.1-13.9 dB, the c11 mp3 fell 12.5-13.4 dB, recordings fall 13-17 dB. Bar 2 reaches -20 dB after 0.49-0.50 s (ceiling 0.50).

Evidence (measured):
- The delivery gain rises through the stop. mp3 minus master, from 0.2 s before the stop to 0.3 s after it: bar 2 +1.8 to +1.9 dB (c11 +1.0), bar 6 +1.5 (c11 +0.6), bar 94 +1.5 to +1.6 (c11 -0.1), bar 113 +1.6 to +1.7 (c11 +1.5). By 0.6 s after the stop: +3.0, +2.4, +3.2, +2.8 dB. Bars 18, 26 and 204: about 0.
- The tail is the celli's release. From 0.25 to 0.45 s after the bar 2 stop, the 45-125 Hz band has not decayed (-38.1 dB, body -38.9 dB) and holds about 60 % of the tail's power. Stems against the master's tail in that band: Violoncellos -2.0 dB, Double basses -11.6, Timpani -22.5, every return -23.6 or lower. In 125-250 Hz: Violoncellos -4.0, R Strings -5.7, Timpani -10.8, R Perc -16.2, Double basses -18.1, R Brass -18.3. Bar 6 has the same order (Violoncellos -2.7 and -4.5). At bar 94 the basses hold 45-125 Hz (-0.2) and the celli 125-250 Hz (-4.2). The notes are the celli's G2 and the basses' G1 that end at qn 5.0 and 21.0 (manual p.222: release trails carry the recorded room).
- The 125-250 Hz band reaches -20 dB after 0.36 s in the master and 0.73 s in the mp3 at bar 2 (bar 6: 0.50 and 0.75 s). The gain rise and the EQ change (167 Hz bell removed) both act on the band that the cello release holds. The actor measured the EQ's share as 0.466 -> 0.495 s on the c11 master.

Fix A, delivery, no render: `tools/deliver_master.py`, directly after `gdb = lift - top`: let gain rises wait 0.6 s and leave gain falls as they are. At the script's 10 frames/s: `d = 6; gdb = np.minimum(gdb, np.concatenate([np.full(d, gdb[0]), gdb[:-d]]))`. Simulated on the c12 mp3 (delay applied to the whole measured gain): bar 2 12.5 dB / 0.46 s, bar 6 13.4 / 0.44, bar 94 12.8 / 0.41, bar 113 17.9 / 0.34, bar 166 14.4 dB, final chord 14.8 dB / 0.46 s / RT60 1.33 s. Whole-file level -0.10 dB. Per-bar side effects: bar 95 -0.8 dB, bar 171 -0.6, bars 43 and 51 -0.2, every other bar 0.1 or less. A delay of 0.4 s gives 12.3 dB at bar 2; 0.8 s gives 12.6 dB and costs 1.3 dB in bar 95, so 0.6 s is the value. If bar 171 must keep its c12 level, raise the second point of the 679 row in `RIDE_TRIMS` (`build/score_config.py`) from `(680.0, 1.0)` to `(680.0, 1.6)`.

Fix B, level-only (can be done as a stem fix): release fades on the two stems that hold the tail, in `build/score_config.py` with `POST_SHAPES_S` (seconds after the score position, applied after the tail hold):
- `POST_SHAPES_S["Violoncellos"]`: `(5.0, [(0.08, 0.0), (0.40, -6.0), (1.20, -6.0), (1.32, 0.0)])`, `(21.0, [(0.08, 0.0), (0.40, -6.0), (0.72, -6.0), (0.81, 0.0)])`, `(374.0, [(0.03, 0.0), (0.35, -6.0), (0.42, -6.0), (0.47, 0.0)])`.
- `POST_SHAPES_S["Double basses"]`: `(5.0, [(0.08, 0.0), (0.40, -6.0), (1.50, -6.0), (1.70, 0.0)])`, the same row at `21.0`, `(374.0, [(0.03, 0.0), (0.35, -6.0), (0.55, -6.0), (0.62, 0.0)])`.

The rows return to 0 dB before the next entries (celli qn 8.83, 23.41, 375.41; basses qn 15.83, 31.66, 375.83). Simulated on the dry stems (the post-fader send to R Strings follows the fade, so the real effect is a little larger; this simulation's baseline reads 0.3-0.4 dB above the table): bar 2 13.5 -> 15.7 dB and 0.44 -> 0.37 s; bar 6 14.2 -> 15.9 dB and 0.43 -> 0.37 s; bar 94 13.4 -> 16.4 dB and 0.41 -> 0.37 s. Celli alone give 15.2 dB / 0.39 s at bar 2. A depth of -9 dB adds only 0.7 dB, so -6 dB is enough. Check after the fix that no stop falls more than 17 dB in 0.3 s (the recordings' upper value), so that the fade is not heard as a cut hall (S3).

Targets: mp3 at bar 2 at most 0.46 s and at least 12.5 dB with fix A; at least 14 dB with A and B; master 15-17 dB at bars 2, 6, 94; mp3 final chord RT60 at most 1.35 s. Keep the returns and `master_eq`.

Judgement: causes measured; audibility inferred from Dan's "too wet" note and the 0.9-1.4 dB that the c12 mp3 lost against c11 at these three stops.

### 2. The Bassoon 1 solo has no hall (bars 115-122, qn 456-488)

What is wrong: `build/mix.json` "Bassoon 1" has `"return": null` (the register sends of c07). During the solo R Winds is digitally silent in more than half of the 0.5 s frames, and in all 16 of 24 frames in which the bassoon is the only wind playing. The span figure of R Winds 21.4 dB under the stem (-69.9 against -48.5 dB) comes from the other winds' short entries.

Evidence (measured): own return under own stem in frames where the soloist is alone in its family: Flute 1 (qn 168-178) -11.1 dB; Horn 1 (qn 264-330) -11.9 dB; Oboe 1 (qn 376-394, other winds playing) -9.9 dB. The oboe solo at bars 95-98 has R Winds 10 dB under it; the bassoon solo 17 bars later has none. The bassoon's dry stem has early room from its Main mic (tail -20.5 dB at 0.15-0.25 s) and little after 0.35 s (-36.1 dB). The solo is fully exposed: at qn 464 the stem is -50.5 dB and the master -50.3 dB in 150-1500 Hz.

Research default: FINDINGS 18-19 (Howl's) gives bassoons no send; those are instruments recorded with hall mics. The EW template (FINDINGS 2), whose Close-led woodwind mic mix this mockup uses, sends the whole woodwind bus, bassoons included, at -8.4 dB. For a Close-led solo bassoon the measured numbers favour the template's default. This is a measured exception for Bassoon 1 only and should be recorded in LEARNINGS as such.

Fix: `build/mix.json`, "Bassoon 1": `"return": {"to": "R Winds", "db": -8.0}`. Bassoon 2 and Contrabassoon stay without a send. Target: R Winds 11-13 dB under the stem in the solo-alone frames of qn 456-488; adjust the send by the measured difference. Conditions, because the send is static and the register sends are protected in HISTORY: the stops at bars 2, 6 and 113 must not get longer by more than 0.01 s, and R Winds in 100-250 Hz in bars 1-2 must not rise by more than 1 dB. If either fails, set `"hp_hz": 160` on R Winds (the parameter `tools/fxchunk.py` already supports for R Strings) or lower the send to -10.

Judgement: the missing hall is measured; that it is heard as a change of room is inferred. The late join at qn 464 (+134 ms) is in the same exposed passage; a send will not hide it (open item d).

### 3. The Trumpet 1 solos are 4-5 dB drier than the other solos (muted solo bars 171-186, qn 680-744; open solo bars 51-66, qn 200-264)

Evidence (measured): Trumpet 1's own return under its stem, in frames where it is the only brass: -16.4 dB in the muted solo (23 of 47 frames) and -15.1 dB in the open solo (50 of 53 frames), against -11.1 dB (Flute 1) and -11.9 dB (Horn 1, same -10.0 send). Trumpet stems have the shortest release of all stems: -29 to -34 dB at 0.15-0.25 s after their stops and -57 to -62 dB at 0.35-0.45 s (horns -12 to -15 and -29 to -33 dB). In the duet, R Winds is at -55.8 dB (7.3 dB under the cor anglais; the accompanying winds' dry level is within 1 dB of the cor anglais) and R Brass at -68.2 dB. `metrics.md` lists R Winds among the three loudest stems in bars 173, 177, 178, 181, 184-186. The hall in these bars is the wind hall, 12 dB above the brass hall, so the cor anglais sits in a room and the muted trumpet does not. The tone difference itself (trumpet 180-355 Hz share -26.8 dB and centroid 1202 Hz, cor anglais -9.9 dB and 877 Hz) is what a straight mute does and needs no change.

Fix: `build/mix.json`, "Trumpet 1": `"return": {"to": "R Brass", "db": -6.5}` (from -10.0). Trumpets 2 and 3 and the cor anglais (-7.0) stay. Target: own return 11.5-13 dB under the stem in the solo-alone frames of both solos. Conditions (protected register sends): R Brass in bars 1-2 must not rise by more than 1.5 dB (inferred estimate: +0.8 dB if the seven senders are equal) and no tutti stop may get longer by more than 0.01 s.

Judgement: the level difference is measured; audibility inferred. A hall under the trumpet also covers the note joins of the "Mute Sus" row, which have no sampled slur (manual p.106-107), so decide open item (a) after this change.

### 4. Low end in bars 255-256 and the cymbal at the fff of bar 263

Bars 255-256 (qn 1016-1024). Measured: the master's 31.5-125 Hz share per bar 253-262 is -18.6 / -14.7 / -23.0 / -20.9 / -17.1 / -14.1 / -16.5 / -18.2 / -9.1 / -7.4 dB (the actor's figures for 255-256: -22.3 / -20.8). The step from bar 254 to 255 is 8.3 dB. In bar 255 the band is the basses: stems against the master's band level: Double basses -2.0 dB, Tuba -5.7, Bass trombone -11.1, Timpani -13.0, Violoncellos -17.4; the contrabassoon rests. The basses play detached E2 eighths (0.32 qn, velocity 83); tuba and bass trombone hold E2. Fix: `build/score_config.py`, `LEVEL_SHAPES["Double basses"]` add `[(1015.5, 0.0), (1016.0, 3.0), (1024.0, 3.0), (1024.5, 0.0)]`. Inferred effect: about +2 dB of share (the basses are about 63 % of the band's power). Another 3 dB on the tuba would add 1.0 dB and on the bass trombone 0.3 dB; the tuba already got +3 dB in c12, so the basses are the stem to use. B's target of -17 dB cannot be reached in two bars of detached eighths with the contrabassoon silent. Proposed target: -21 / -19 dB and a step of at most 6 dB from bar 254; then close the item. Is the bass present: yes by measurement (the share equals a recording's whole-file average, Dvořák -21.6 dB); the fault is the step from the bars around it (inferred).

Cymbal, qn 1047.94 (bar 263, fff). Measured: three strokes at velocity 124 give -31.1 / -34.8 / -32.0 dB at 4-12 kHz in the stem and a rise of +10.1 / +4.6 / +16.8 dB in the master. The stroke at the fff is the weakest (a different round-robin take, manual p.116-117). Fix: `LEVEL_SHAPES["Crash cymbals"]` add `[(1047.5, 0.0), (1047.8, 3.5), (1052.0, 3.5), (1053.0, 0.0)]`, and add `"Crash cymbals": [887.5, 1047.5, 1107.5]` to `RR_RESET_AT` so the takes are the same in every render and the trim stays valid; re-measure the three strokes after the first render with the reset and set the trim from that. Target: the three strokes within 1.5 dB at 4-12 kHz in the stem and a rise of at least 7 dB in the master at qn 1047.94. This also serves the fff at bar 263, which the actor measured at only +0.5 dB over bar 262.

Bass drum and timpani need nothing: bass drum see the manual table; timpani stem against master in 60-250 Hz, 142 strokes, median -6.3 dB (10th to 90th percentile -11.9 to -3.1).

### 5. R Winds is the longest and brightest return

Evidence (measured): after the final chord R Winds needs 0.96 s to -20 dB with RT60 1.95-2.07 s; R Strings 0.78 s and 1.6-1.8 s; R Brass 0.65 s and 1.6 s; R Perc 0.58 s and 1.3-1.4 s. At bar 2: R Winds 0.76 s, R Strings 0.59 s. Return against its senders' dry sum, relative to 500-1000 Hz: R Winds -6.4 dB at 5.6-8 kHz and -13.5 dB at 8-12 kHz; R Strings -11.5 and -20.2; R Brass -12.2 and -23.3. One room should decay at one rate; here the families differ by 0.3-0.4 s. With the returns included, the wind family's tail (-15.8 dB at 0.15-0.25 s, -25.0 dB at 0.35-0.45 s) equals the brass's (-14.6 / -25.2), so this is about the late tail only, which is why it ranks low.

Fix (a trial, because the return envelope is protected in HISTORY): `build/mix.json`, returns, "R Winds": `irSetup` `endPos` 0.5 -> 0.43 and `decayLength` 0.5 -> 0.43. The values are inferred from the ratio of the RT60s. Target after the final chord: -20 dB in 0.75-0.80 s and RT60 1.6-1.8 s. Accept only if the wind family's tail at its stops stays at or above -17 dB (0.15-0.25 s) and -27 dB (0.35-0.45 s). The change also gives room for the Bassoon 1 send of finding 2.

### 6. Optional: Mid mics on the cor anglais (MANUAL-GAPS #4)

Evidence (measured): the woodwind stems are near-mono points: L/R correlation 0.85-0.99, side-to-mid -9.5 to -14.0 dB (horns 0.58-0.63 and -5.3 to -6.1 dB). Their dry tail at 0.15-0.25 s is -21.5 dB against -15.9 (brass) and -9.7 (strings). A hall send adds late tail, not early room; the Mid position is the manual's source of definition without closeness (p.138) and the Soft mood's choice (p.136).

Trial on one track and one passage: "Cor anglais" mics Close 0.912 -> 0.55, Mid 0 -> 0.6, Main 0.24; level re-matched to -49.1 dB over qn 680-744. Accept if correlation is under 0.90, side-to-mid at least -8.5 dB, the dry tail at 0.15-0.25 s at least -24 dB (now -29.8), and the attack share within 1 dB. It needs a rebuild of that track and a memory check (p.139: each position loads its own samples). Inferred benefit; do it only if the cycle has room.

## Open items from c12

- (a) Muted Trumpet 1, qn 680-744: use +0.03 s only at 685, 687, 688, 691, 692, 694, 715, 717, 719, 726 and 0.01 s at the other joins (inferred). Target: two-pitch time median 30-45 ms, no join over 60 ms, no join with a dip over 6 dB. Decide after finding 3, because a hall under the trumpet covers the joins. Flutter: the held-note level range (95th minus 5th percentile) of "Mute Sus" is median 5.3 dB, maximum 8.0; the open trumpet solo has 5.0 and 7.9, the cor anglais 2.9. The muted row is no worse than the open row, so the flutter is not a fault in general. It is one only on the D5 at qn 688: 8.0 dB at 9 Hz in the stem, 10.9 dB at 16 Hz in 1.4-5.6 kHz, 7.8 dB in the master. Trial for that note: CC1 8 lower with +1.5 dB of level; accept if the 9 Hz range falls under 6 dB (inferred).
- (b) Basses' on-beat eighths, qn 1088-1108: close. The master's low-band rise is +18 / +0 ms (actor); the band there is shared by basses (-3.4 dB against the master's band level), celli (-5.2), timpani (-6.1) and tuba (-10.2), so the stem's +70 ms is covered. Not audible in the mix (inferred).
- (c) Second chorale, bars 255-256: finding 4.
- (d) Flute 2 at qn 650 (+114 ms): audible (inferred): Flute 2 is the loudest stem in 500-4000 Hz there (-36.0 dB; Violins I -36.2, Horn 1 -36.3; master -28.9). Target +50 ms or less. Qn 618 (+49 ms): inside the normal spread, close. Bassoon 1 at qn 464 (+134 ms): audible (inferred), the stem is the master in its band; target +50 ms or less.
- (e) Violoncellos qn 564: close. The stem is 25 dB under the master in 65-520 Hz (-64.5 against -39.1 dB; Violas, Horn 3 and Bassoon 2 are above it), and the master is -39.1 dB in c12 against -39.4 in c11.
- (f) Master true peak +0.1 dBFS: close. The master is a 32-bit float file, so the two samples at 420.953 s are not clipped; the mp3 is limited to -1.5 dBTP. Only a fixed-point export of the master would clip.

## New in c12

- Tempo arcs (888, 912) and (916, 936): no effect on any space measure (returns against dry in section P -14.1 dB, the same as sections G to R). The musical judgement belongs to the tempo lens.
- Cello and viola same-pitch repeats: the notches do not cut the hall (S3 passes). At qn 325 the cello stem dips from -44.7 to -53.7 dB while R Strings stays at -50 to -53 dB and the master at -34 dB within 1 dB. At qn 728 the viola stem dips 7 dB and R Strings stays at -73 dB.
- Sfp at qn 592: the hall is not cut. Returns against dry: -14.2 dB before the mark, -13.6 / -14.4 / -12.4 dB during the notch, -14.9 dB in the p.
- Flute 1 trims: not too weak in bars 43-44 and 105. By a full-mix measure (Flute 1 stem against the master without Flute 1, 500-4000 Hz, whole bar) the margins are bar 43 +0.6 dB, 44 +3.3, 89 -2.7, 102 -0.6, 105 +0.5. The actor's stem-against-stem margins are +5.1, +7.7, +5.0, +1.6, +6.6. Bars 89 and 102 are the two places where the flute is under the sum of the rest. If B's measure agrees: `LEVEL_SHAPES["Flute 1"]` +1.5 dB over qn 352-356 and 404-408.
- Delivery ride at bars 42-49 and 164-196: the only fault found is the gain rise through the stops (finding 1). The gain reaches its maximum of +11.9 to +12.4 dB at bar 50.
- Fff at bar 263 against 262: +0.5 dB (actor). The cymbal that marks it is the weakest of the three strokes: finding 4.
- Stem fix and drift list: none of the drifted single notes is audible as a fault. Horn 1 at qn 569.66 (+6.1 dB against c11) is the only one that leads its band (stem 2.1 dB under the master); it is 2.7-3.9 dB above its neighbours in the stem and 1.1-1.6 dB in the master, inside a crescendo. Flute 1 qn 423, Horn 3 qn 119 and Violins I qn 42 are 3.4-4.9 dB under the master in their band; the other eleven are 7-21 dB under it. One note for A and B that is not on the list: Horn 1 at qn 572.58 (E-flat 4, velocity 83) is 8.6 dB under the note before it in the stem; the master does not show it.
- Closed items: left closed. I ran no brass-accent check; the tilt jump stays the measure for it.

## Findings from the other movements

- `RR_RESET_AT` (Movement II): the finale has it on the basses only. It would help on Crash cymbals (finding 4, measured reason). Inferred candidates: Timpani at section starts and one short-note track from the actor's drift list as a test of whether the drift is the round-robin position.
- Crescendos shorter than 4 qn: no blend measure depends on it; I measured no place. Left to A and B.
- Clamped low-wind swells in the volume envelope: would help in the Bassoon 1 solo once it has a send, because a post-fader swell moves the hall with the dry signal (inferred). The solo's held notes vary by a median of 2.4 dB.

Do not touch: the sends of strings, horns, Trumpets 2-3, upper winds and percussion, the return faders and the R Strings high-pass at 160 Hz; the c12 `master_eq` and the delivery ratio; seats, widths and the overall image (within 0.07 correlation and 0.7 dB side-to-mid of the Dvořák up to 5 kHz); bass drum and timpani levels; FINAL_RING (final chord 15.2 dB at +0.3 s, RT60 1.30 s in the master); the 592 notch; the cello and viola detach dips and notches; the c12 woodwind trims; the Trumpet 1 per-bar roles; the 164 and 679 ride rows and the bar 42 subito (apart from the rise delay of finding 1); the bars 262-264 trims; the basses' beat gaps and CC16 resets; tuba and contrabassoon at 984-1056.

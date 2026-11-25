# Cycle 13, critic A: articulation and phrasing (render c12)

All numbers come from the c12 stems, master and delivered mp3 (`cycles/c12/`), `build/parts.json` and `build/mockup-events.tsv`. Levels are RMS in dB re full scale on mono sums. I cannot listen to audio. Where the coordinator asks for a verdict by ear, the verdict is inferred from these measurements and is marked "inferred".

## Manual notes

Third round: pages chosen for this lens's open problems (the joins of the muted trumpet solo, legato entries, the harp harmonics). Read in full: pages 68, 70, 99, 104-107, 112-113 of the May 2021 HO Opus manual.

| Manual (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Brass Legato Slur (p.105): a slur is produced only when there is "no significant gap" between two notes and they are at most an octave apart; the patch is monophonic unless CC22 is 0-63. | Trumpet 1 open solo, bars 51-66 (qn 200-264); slurred horn and trombone lines. | Yes. Slurred brass notes overlap, and I found no chord on a monophonic legato row. |
| Brass Legato Slur (p.106): loudness is on the Mod Wheel; velocity sets the speed of the transition (higher is faster). | Trumpet 1 qn 200-264 (`LEG_VEL_SPANS` 96). | Yes. |
| Mutes (p.106): the Mutes folder holds muted staccato, legato slur, crescendo and clusters. | Trumpet 1 con sordino, qn 680-792. | Partly. On disk the solo trumpet has only "1TP Mute Sus", "1TP Mute Sus Accent" and "1TP StacSs DblTng Mute RRx9". The only muted legato row is "3TP Mute Leg Slur.oib" (3 Trumpets/05 Mutes). One muted trumpet has no sampled slur, so the joins are made with note timing (finding 2). |
| Woodwind Legato Slur (p.112): same gap and octave rule as the brass. The page does not say that velocity changes the transition. | Bassoon 1 solo, qn 456-488 ("Leg Slur Exp"); Flute 2 at 618 and 650. | Yes for the rule: the widest leap in the solo is 7 semitones and every join overlaps by 35 ms or more. The faults in the solo are level faults (finding 1). |
| Strings legato (p.99): a slur or portamento needs "no significant time gap"; the first note of a phrase has no legato effect; monophonic by default (CC22); the Basses have only Legato Slur. | Violoncellos qn 564, Violins II qn 152. | Not at these two notes. Each is sent to "Leg Slur MAX" where no join is possible, so it plays the row's first-note layer (finding 3). |
| Keyswitch (p.107 brass, p.113 woodwinds): a KS Master changes articulation by keyswitch notes. Neither page gives a minimum time between the keyswitch and the note. | Every KS Master track. | The render sends the keyswitch a median 10-21 ms before the note where there is no rest (`KS_LEAD` = 0.06 qn). The research default is 40-800 ms (finding 3). |
| Harp (p.68, p.70): "Harp Harmonics" is a single-articulation patch of harmonics; "Angels Harmonics" plays harmonics only at velocities 123-127; CC11 and velocity set loudness. | Harp, bar 43 (qn 168, 176, 184). | Not used. The harmonics are plucks at sounding pitch 70 on "Harp Sus RR" (`HARM_ON_TRACK`). See finding 6. |
| Brass effects (p.104-105): sampled crescendos (including "Crescendo MOD SPEED"), flutter tongue, rips, clusters. | None of these is printed in the finale. The sfp at qn 592 is made with a level shape. | Not applicable. No change proposed. |

## Findings, ranked

### 1. Bassoon 1 solo, bars 115-122 (qn 456-488): note levels do not follow the printed dynamics

Where: Bassoon 1, "solo, espress.", row "Leg Slur Exp" (`ART_SPANS`, 455.9-496). Printed: p at 456, crescendo from 461 to mp at 464, decrescendo from 467 to p at 470, then p without a hairpin from 472 to 484. The bassoon stem is 0.2-3.5 dB under the master on every note, so the stem is what the listener hears.

What is wrong (measured): adjacent notes of the slurred line differ by 6-10 dB where the score and the controllers ask for an even level, and the top note of the crescendo (A4 at 464) starts in a 6 dB dip.

Evidence (measured; highest 100 ms level inside each note, with CC11 in brackets): 456 D4 -44.6 (54); 459 B flat 3 -52.2 (54); 460 A3 -52.2 (53); 461 G3 -46.9 (54); 462 B flat 3 -42.7 (61); 463 D4 -46.9 (64); 464 A4 -44.0 (66); 466 -47.9; 467 -49.2; 468 -49.8; 470 -46.9; 472 C4 -42.8 (60); 475 E flat 4 -53.1 (63); 476 D4 -45.0 (62); 477 -48.7; 478 -49.5; 479 A3 -51.0 (57); 480 B flat 3 -41.5 (56); 482 G3 -44.2 (53); 484 A3 -51.4 (54). The second phrase is printed p throughout and spans 11.6 dB (475 against 480); the step from 479 to 480 is 9.5 dB and from 475 to 476 it is 8.1 dB with CC11 63 and 62. In the first phrase the B flat at 462, in the middle of the crescendo, is 1.3 dB louder than the mp peak at 464. Bassoon 1 has no drifted note in this passage, so these levels repeat between renders.

At 464 the 50 ms level in 50 ms steps from 0.3 s before the beat is -47.5, -48.3, -48.5, -49.1, -53.1, -54.4, -54.1, -54.0, -52.4, -50.3, -48.0, -46.3, -45.7, -44.9, -44.7: a dip of 5-6 dB under the previous note from -0.10 s to +0.15 s. The new pitch itself is on time (it reaches -6 dB of its body 24 ms before the beat with the 150 ms lead), so the lead must stay. The row's long notes start soft and swell; quarter notes end before the swell. That is the cause (inferred from the pattern of short and long notes).

Fix (level only; the row stays): in `build/score_config.py`

`LEVEL_SHAPES["Bassoon 1"] = LEVEL_SHAPES.get("Bassoon 1", []) + [[(458.9, 0.0), (459.0, 4.5), (460.9, 4.5), (461.0, 0.0)], [(461.9, 0.0), (462.0, -2.5), (462.9, -2.5), (463.0, 0.0)], [(471.9, 0.0), (472.0, -3.0), (474.9, -3.0), (475.0, 6.0), (475.9, 6.0), (476.0, 0.0)], [(478.9, 0.0), (479.0, 3.0), (479.9, 3.0), (480.0, -5.0), (481.9, -5.0), (482.0, -2.0), (483.9, -2.0), (484.0, 3.0), (485.0, 3.0), (486.0, 0.0)]]`

`LEVEL_SHAPES_S["Bassoon 1"] = LEVEL_SHAPES_S.get("Bassoon 1", []) + [(464.0, [(-0.13, 0.0), (-0.09, 5.0), (0.10, 5.0), (0.24, 0.0)])]`

Targets: the highest 100 ms level of every note printed p within 2.5 dB of -47 dB (now -53.1 to -41.5); the A4 at 464 the loudest note of 456-470; between 464 -0.1 s and +0.2 s the 50 ms level never more than 2 dB under -48.5 dB. Do not shorten the lead at 464: the new pitch would then arrive about 45 ms after the beat (inferred from the measured 126 ms from note-on to -6 dB).

### 2. Muted Trumpet 1 solo, bars 171-186 (qn 680-744): set the overlap per join, and add lead at five joins

Where: Trumpet 1 on "Mute Sus" (note-on 35 ms early, every slurred join overlapped by 30 ms), doubled in unison by the cor anglais, which is 5-7 dB louder per note.

What is wrong (measured on the trumpet stem; "two-pitch time" is the time around the beat in which the old and the new pitch are both within 6 dB of their own body, from the level of harmonics 2-7 in 40 ms windows): 683 97 ms, 684 105, 685 45, 686 114, 687 5, 688 63, 690 83, 691 15, 692 23, 694 28, 715 144, 716 104, 717 46, 718 116, 719 2, 720 108, 723 64, 724 75, 725 35, 726 0, 727 80, 728 123. Median 70 ms; the cor anglais has 28 ms. The new pitch reaches -6 dB of its body at (ms after the beat) 687 +65, 692 +75, 694 +62, 719 +69, 723 +59, 726 +85; the other joins are between -21 and +37; the cor anglais median is -7. So the joins fall into two groups: long overlaps where the new pitch speaks fast, and late arrivals where it speaks slowly. One overlap value cannot serve both.

In the master the two-pitch time is 105 ms (median) at the 22 doubled joins and 82 ms at the 15 joins the cor anglais plays alone. The hall gives most of it; the trumpet adds about 23 ms.

Answer to the coordinator's choice: neither variant as written. Overlap 0 at 683, 684, 686, 690, 715, 716, 718, 720, 724, 727, 728. Keep 0.03 s at 685, 691, 717, 725, and use 0.02 s at 688 and 723 (63 and 64 ms now, so about 53 and 54 ms; inferred). The planned +0.03 list must lose 715 (144 ms, the longest of all) and gain 725. At 687, 692, 694, 719 and 726 the fault is lateness: lead 0.085 s and overlap 0.06 s (the two-pitch time there is 0-28 ms now, so about 30-58 ms after the change; inferred).

Fix: `tools/score_to_parts.py` near line 1122: let a `ROW_SLUR_OVERLAP_S` value be a list of (from_qn, to_qn, seconds) spans, as `ROW_LEAD_S` already allows (line 1118). In `build/score_config.py`: `ROW_SLUR_OVERLAP_S = {"Trumpet 1": {"Mute Sus": [(684.9, 685.1, 0.03), (686.9, 687.1, 0.06), (687.9, 688.1, 0.02), (690.9, 691.1, 0.03), (691.9, 692.1, 0.06), (693.9, 694.1, 0.06), (716.9, 717.1, 0.03), (718.9, 719.1, 0.06), (722.9, 723.1, 0.02), (724.9, 725.1, 0.03), (725.9, 726.1, 0.06)]}}` with 0.0 elsewhere, and `ROW_LEAD_S["Trumpet 1"]["Mute Sus"]` as a span list: 0.085 at 687, 692, 694, 719, 726; 0.065 at 723; 0.035 elsewhere. Targets on the trumpet stem: two-pitch time 60 ms or less at every join (now 13 of 22 are over), new pitch at -6 dB within 30 ms of the beat (now 6 of 22 are later than +55 ms); in the master, doubled joins no more than 15 ms above the cor-anglais-alone joins.

The row's flutter (measured, 95th minus 5th percentile of the level in 20 ms windows at a 5 ms hop inside a note, after removing a second-order trend, in the note's harmonic bands): at 688 trumpet stem 11.8 dB, cor anglais stem 5.4, master 14.6; at 724 9.7 / 7.7 / 12.2; at 680 8.3 / 5.0 / 8.5; at 712 8.2 / 5.3 / 8.3; shorter notes 2.6-6.4 dB on the trumpet. The master fluctuates as much as the trumpet alone (measured). The likely cause is beating between the two instruments in unison, with the cor anglais 5-7 dB louder (inferred). Inferred: the trumpet's flutter is not audible as a separate fault while the cor anglais doubles it. No change. Velocity does not explain it (the G5 at 724 has velocity 73 and 9.7 dB). "3TP Mute Leg Slur.oib" (p.106) would give sampled slurs but is three players; I do not propose it for a solo.

### 3. Keyswitches 10-21 ms before the note: linked to the equal-data level drift, and two legato entries the row cannot play

Where: every KS Master track; shown at Violoncellos qn 564 and Violins II qn 152.

What is wrong: where a row changes without a rest, the keyswitch is sent `KS_LEAD` = 0.06 qn before the note-on (`tools/score_to_parts.py` line 58, used at lines 3292-3298). Measured gaps: median 10-21 ms per track, minimum 7.1 ms in the strings; on Violins I 220 of 266 gaps are under 40 ms.

Evidence (measured): `cycles/c12/CHANGES.md` lists 35 long notes that moved 2-6.7 dB between c11 and c12 on equal data. 28 of the 35 have a keyswitch 10-23 ms before their note-on. Of all notes of 0.9 qn or longer on the pitched tracks, 856 have a keyswitch less than 30 ms before them and 28 of those drifted (3.3 %); 3690 have a larger gap and 7 drifted (0.19 %). The rate is 17 times higher after a short gap. Each of the 28 is a note joined from a sounding note directly after the row change. Inferred cause: the order in which the sampler handles the row change and the overlapped note-on is not the same in every render, so the note plays as a join in one render and as a first note in another.

Two notes where the result is a hole in the stem (measured):
- Violoncellos 564: a staccato B2 at 563 ("Stac RRx9"), then the keyswitch to "Leg Slur MAX" 10.7 ms before a B2 of 5.31 qn. Stem per 0.1 s from 0.1 s before the beat: -64.6, -69.7, -80.1, -74.8, -69.0, -64.4, -57.8, -55.2, -52.2, -50.0, -47.5, -46.5, -45.2. The note is 20-30 dB under its body for 0.4 s. This is the coordinator's item "7-10 dB weaker than c11 on equal data". The master is not weaker than in c11 there (masked), so it is not audible now (inferred).
- Violins II 152 (ff, accent, start of a slur): F4 on "Leg Slur MAX", keyswitch 21 ms before, overlapping the F6 before it: a leap of 21 semitones into a legato row (the scripts join only within an octave). Stem per 0.1 s from qn 151: -48.1, -47.3, -47.1, -42.9, -42.3, -65.2, -59.0, -54.2, -50.4, -38.8, -40.5: a hole of 0.4 s. The master stays at -27.8 dB (masked).

Fix:
- `tools/score_to_parts.py`: replace the fixed `KS_LEAD` by a time. The keyswitch goes 0.045 s before the note-on, and not earlier than 5 ms after the previous note-on on the track. Target: no gap under 40 ms except where the previous note-on is closer. Check on one stem that notes sounding across a moved keyswitch keep their level within 0.5 dB (a keyswitch should act only on later note-ons; inferred). Then compare two renders of equal data with `drift12.py`: the target is under 10 drifted notes (c12: 35).
- `build/score_config.py`: `STR_REP_AFTER_STAC = {"max_qn": 6.0, "max_gap_qn": 0.5}` (now 1.0). The cello note at 564 is the only string note that enters a legato row on the same pitch after a "Stac" stroke (measured over the five string tracks), so nothing else changes. It becomes a fresh "Sus MAX" stroke. Target: within 6 dB of its body by +0.15 s.
- Violins II 152: `ART_SPANS["Violins II"]` add `{"from": 151.9, "to": 152.1, "art": "Sus MAX"}`, with the note before ending 0.06 s before the new note-on and a lead of 0.07 s. It is the only overlapped string leap over 12 semitones into a legato row (measured; Violins I at 856 leaps 14 semitones after a gap and dips only 2-3 dB).

### 4. Crash cymbals at bar 263 (qn 1048): the fff crash is the weakest of the three

Evidence (measured): all three crashes have velocity 124. Stem level in the first 0.5 s: 888 -26.5 dB, 1048 -29.8, 1108 -27.1. Rise of the master's 4-12 kHz band at the stroke: 888 +7.2 dB, 1048 +4.3, 1108 +16.8. The cause is `build/roles.json` "Crash cymbals": [[1046, 1060, -3.0]]; the other two crashes have 0 dB. I found no reason for this entry in HISTORY.md or the CHANGES files.

Fix: delete that entry. Expected: stem about -26.8 dB, master rise about +6 to +7 dB (inferred). Check the delivery limiter at 1048 (limit about 3 dB; whole-piece value now 2.6); if it goes over, use -1.0 instead of -3.0. This also adds to the step from bar 262 to 263, which is now +0.6 dB (+1.5 dB in the first 0.3 s).

### 5. Low register in bars 253-256 (qn 1008-1024): tuba and bass trombone should give the rest

Evidence (measured; 31.5-125 Hz power against full-band power in the master, per bar 247-262): c12 -13.7, -13.4, -11.3, -13.1, -11.1, -15.1, -18.5, -14.1, -21.6, -15.7, -17.3, -14.0, -15.1, -16.5, -9.4, -7.6; c11 -13.9, -13.0, -11.4, -14.0, -12.1, -16.9, -18.3, -15.2, -24.9, -16.2, -19.1, -15.8, -15.8, -16.9, -9.3, -8.0. c12 gained 3.3 dB in bar 255 and 0.5-1.8 dB in bars 256-258. Bar 255 (-21.6) is still 4.6 dB short of the -17 target and bar 253 (-18.5) 1.5 dB short; the other bars meet it. In bar 255 the stems' low-band level against the master's low band is: Double basses -1.6 dB, Tuba -7.1, Bass trombone -12.3, Timpani -13.6, Violoncellos -15.3. The basses play E2 eighths (velocity 83, printed f) and already carry +3 dB in roles.json and the +6 dB pitch trim on E2, the weak pitch under their 87.3 Hz EQ notch. The tuba and the bass trombone hold E2 at printed ff; the bass trombone still has [1016, 1032, -3.0] in roles.json and the tuba has no entry there. The contrabassoon rests in 1016-1024.

Is the bass present: in bars 256-262 yes by this measure; in bar 255 not yet (inferred from the 4.6 dB shortfall).

Fix (`build/roles.json`): "Tuba" add [1016, 1024, 3.0]; "Bass trombone" change [1016, 1032, -3.0] to [1024, 1032, -3.0]; "Double basses" add 2 dB at [1016, 1020] at most. Estimated gain in the band in bar 255: about +2.8 dB without the basses' 2 dB, about +3.8 dB with it (power sum of the stem shares above; inferred). Critic B owns the balance; this entry answers the coordinator's question of which stem.

### 6. Smaller items

- Flute 1 qn 423 (bar 106, accent at the end of the crescendo in the mf solo): the one drifted note that is probably audible (inferred). Stem -37.4 dB against -34.6 for the accented note at 422; the master is 5.1 dB lower than in c11 during the note. Its keyswitch is 21 ms before it, so the fix in finding 3 should hold it. If it is under -36 dB again in c13, add `[(422.9, 0.0), (423.0, 3.0), (423.9, 3.0), (424.0, 0.0)]` to `LEVEL_SHAPES["Flute 1"]`. Horn 1 at 866 (-3.8 dB, master -1.4) is a possible second. The other listed notes are 4-24 dB under the master and the master moved less than 2 dB: not audible (inferred).
- Flute 2 at 618 and 650: the new pitch is early (-72 and -172 ms) and the old pitch stays until +102 and +74 ms (two-pitch time 112 and 97 ms); Flute 1 in unison arrives at about -40 ms. Flute 2 is 11.6-12.5 dB under the master: not audible (inferred). Smallest fix: `build/leg_leads.json` Flute 2 "618.0" 0.12 to 0.03 and "650.0" 0.17 to 0.03 (target: within 30 ms of Flute 1). A row change is not needed.
- Pizzicato, bars 51-66: all notes have velocity 41. The master's rise at the onsets is 11.4 dB (basses), 8.4 (cellos), 4.5 (Violins II; under 3 dB at 5 of 31) and 5.2 (Violas; under 3 dB at 2 of 31). Timing is good (stem half-rise -9 to +3 ms). Option: velocities 46 / 38 / 42 / 38 by beat on Violins II and Violas, and `RR_RESET_AT` at 200.0 for the four pizzicato tracks.
- Violins I "4 soli", qn 473-476 and 485-488: both parts play on the section "Sus MAX" row at velocity 41 and -10 dB; the eighths are connected (levels within 3 dB), but the first eighth at 485 is 8-13 dB under the next ones (5 dB at 473). Add +4 dB over the first 0.15 s at 485 with `LEVEL_SHAPES_S`. A DIV A patch (p.89-90) is not proposed: Close mics only, and LEARNINGS c10 records that divisi on the KS Master is a level change.
- Harp harmonics, bar 43: plucks at pitch 70, velocity 46; the second partial is already 18-26 dB under the fundamental; the stem is 8-13 dB under the master. "Harp Harmonics.oib" (p.70) needs its own instance because the harp KS Master's keyswitches overlap the harp's low notes. Expected gain small (inferred). Test only if an instance is free.
- Brass accents by the tilt jump (99 printed onsets): whole movement median -0.2, 90th percentile +3.0; bars 247-262 median -0.4, 90th percentile +2.8; bars 263-272 90th percentile +3.4 (1058 +3.3, 1080 +4.1, 1085 +3.9). At the target; no change.
- True peak: the master has 2 samples over full scale at 420.953 s (1.014); the mp3 is at -1.5 dBTP. Not audible. If the WAV master is delivered, lower qn 1108-1112 by 0.5 dB.

## Answers to the coordinator's other items

- Wetness: metrics.md gives 0.50 s at bar 2 and 0.37-0.45 s at the other five stops; my own measure gives 0.30-0.43 s on the master and 0.34-0.43 s on the mp3 (c11 mp3 0.30-0.44 s). Limiter 2.6 dB. Verdict: right, at the upper limit. Do not raise the returns (inferred from the measured decays).
- Tone: delivered c12 minus c11 by octave: 63 Hz +1.5 dB, 125 +1.8, 250 +1.5, 500 +0.6, 1 kHz -0.7, 2 kHz -0.8, 4 kHz +0.3, 8 kHz +0.6. Against the mix's own 1 kHz level the long-term spectrum is now +4.3 dB at 125 Hz (Dvorak reference +7.0), +4.4 at 250 Hz (reference +4.4), -5.0 at 2 kHz (reference -5.2). The change moves the mix toward the reference: an improvement (inferred).
- Basses' eighths, qn 1088-1108: 35-180 Hz half-rise on the on-beat eighths: stem median -15 ms, master median -22 ms (quartiles -34 and +2). Not late. Close this item (measured).
- Tempo arcs (888, 912) and (916, 936): bars 221-236 last 1.89, 2.12, 2.12, 2.11, 2.11, 2.14, 2.14, 2.21, 2.14, 2.14, 2.14, 2.14, 2.14, 2.18, 1.82, 1.82 s. Bar 228 is 3 % longer and bar 234 2 % longer. Keep.
- Cello and viola repeat notches (325, 728): stem dips of 9 dB (80 ms wide) and 11 dB (40 ms); no hole in the master. Keep.
- sfp at 592: the brass sum falls 18 dB by +0.45 s, the master 10 dB; the fastest fall is 2.7 dB per 10 ms on the brass and 1.6 in the master. No glitch. Keep.
- Flute 1 after the trims: loudest stem in bars 43-44 (-4.2 dB re master) and bar 105 (-5.8), second in bar 102 (-5.9), third in bar 89 (-9.8, printed f). Not too weak in its solos.
- Delivery ride: the gain changes 0.5-2 dB per bar in bars 40-51 and 162-197. The fastest change is a fall of 2.7 dB in 0.6 s at qn 742.6-744.2, under a rise of 11.6 dB in the master (the strings' entry): not audible (inferred). Bar 44 is 2.8 dB softer than in c11 (delivered -35.0 dB).
- fff at 263 against 262: +0.6 dB (c11: -0.6 dB). Improved; finding 4 adds to it.
- Hammered eighths (printed only in the Double basses): separation in the master, 200-1000 Hz, bars 199-210: on-beat median 6.3 dB, off-beat 4.5 dB, under 3 dB at 13 of 96 strokes; bars 247-262 5.3 / 4.9 dB; bars 263-270 5.4 / 4.1 dB. S1 passes on most strokes.
- Tremolo and re-bows: the "Tremolo" keyswitches follow the printed tremolos at 888 and 1088; only the cellos re-bow in the chorale (915.3, 920.0, 924.6, 929.3); the other strings' longest notes are at or under the 3.95 s loop. Sul tasto at 376 follows the config (Violins II "Flautando", CC1 20; Violas and cellos CC1 1). Timpani rows switch at the printed rolls; "near the rim" at 708 has no patch in the manual.
- Other movements' findings: (1) `RR_RESET_AT` is set only for the basses; extend it to the four pizzicato tracks at 200.0. (2) The short-crescendo rule would change nothing: 65 printed crescendos are shorter than 4 qn and none has a falling dynamic lane (measured). (3) The low-wind swell cap in the volume envelope would act only on the bass clarinet in 680-744 (23 of 76 notes at CC11 40 or less); the bassoon solo is at CC11 53-66. Low priority.

Do not touch: the sfp at 592; the repeat notches at 325 and 728; the tempo arcs; the Flute 1 / Flute 2 / Oboe 1 trims; the returns and the c12 delivery EQ and ride; the basses' eighths at 1088-1108; the brass rows and accents in bars 247-262; the tremolo keyswitches; the pizzicato timing; the 150 ms lead of the bassoon's A4 at 464; "Leg Slur Exp" on Bassoon 1, cor anglais and Oboe 1; "Mute Sus" as the muted trumpet's row; and the other closed items (the 315 Hz hump in section J, "Sus Accent MAX" on the brass, tuba and contrabassoon -3 dB at 984-1056 outside the change in finding 5).

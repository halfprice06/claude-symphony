# Cycle 13, critic B: balance and levels (review of the c12 render)

Method. All numbers come from my own scripts on `cycles/c12/render/` (35 stems and the master), `cycles/c12/final_build/parts.json`, the c12 and c11 mp3s and the c11 master. Stem and master levels are RMS in dBFS unless stated. "Index" is the audibility index: the third-octave level of a stem minus the level of the master without that stem, in the stem's best band (the 40 Hz band is ignored). Nobody listened to the files. Every "by ear" question is answered from measurements, and the audibility judgement is marked inferred.

## Manual notes

Pages read in full: May 2021 HO manual, PDF pp. 121-126 (bass drums, Timpani Felt, Timpani Hard, Timpani Hard KS). I chose them because the top open problem of this lens is the timpani at the arrival (bar 223) and the ending (bar 278). `loop/MANUAL-GAPS.md` was read; nothing in it changes the rows below.

| What the manual says (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Timpani Hard Rolls: CC1 crossfades the dynamics over 8 recorded levels (p. 126). | Timpani rolls at qn 884-892, 1040-1053, 1088-1102, 1108-1113. | Yes. `TIMP_CC1_MAP` drives CC1. The level is completed by `TIMP_ROLL_TRIM_DB`, which gives fff only 5 dB more than f. See finding 1. |
| Timpani Hard Long: velocity selects up to 16 levels, round robin x2; two notes within 65 ms trigger a double hit (p. 125-126). | Timpani strokes, for example the f stroke at qn 892 (bar 224). | Yes. Velocity sets the stroke level. I did not test for unintended double hits. |
| For the percussion, CC11 and velocity are named as the loudness controls (p. 121-125). | All Timpani and Bass drum levels. | Different, and recorded: the tools found no CC11 response on the Timpani patch in c01 and use CC7 plus the volume envelope. No change proposed. |
| Timpani Hard Cresc (keyswitch E0 in the KS patch): recorded crescendos in three speed ranges, 2 velocity levels (p. 125-126). | Crescendo rolls at qn 884-888 and 1098-1108. | Not used. The rolls use the Rolls row with CC1. This is an option if a later cycle finds the CC1 crescendo static. Not proposed now. |
| Timpani Hard Short (keyswitch C#0): muted hits (p. 126). | Tutti stops at bars 2 and 6. | Not used and not needed. The timpani do not set the decay time at those stops; the celli do (finding 5). |
| 36in Ludwig bass drum: a deep low sound with a woody attack; C1 short, D1 long, E1 and F1 rolls; round robin x4 (p. 121-122). | Bass drum at bars 223 and 278. | Yes. The stroke gives a 50 Hz thump of about 0.6 s with an index of +4 dB (bar 223) and +3 dB (bar 278) at 50 Hz. It is heard and does not cover. |

## Findings, ranked

### 1. The fff timpani rolls at bar 223 and bar 278 are covered after the first stroke (measured)

Where: Timpani, qn 888-892 (bar 223, printed fff with a diminuendo to the f stroke at 892) and qn 1108-1113 (bars 278-279, printed fff).

What is wrong: only the first stroke of each roll is heard. The body of the roll is under the rest of the orchestra, so the printed fff roll at the two loudest places of the movement is absent after a quarter of a second.

Evidence. Timpani stem in 250 ms windows from the downbeat of bar 223: -28.4, -32.8, -37.5, -38.1, -39.0, -40.0, -41.0, -40.8 dBFS. The master in the same windows is -15.2 to -17.9, so from 0.5 s the roll is 21-24 dB under the master. The index in the roll's best band (127 Hz) is -11 dB. From 0.5 s the fff roll is at or under the level of the single f stroke that follows in bar 224 (-37.6). Bar 278: first window -30.5, then -33.8, -34.0, -35.6, -35.7, -32.7, -35.3, -35.9, -36.5; the master is -15.2 to -18.1; index -7 dB at 160 Hz in every window including the first. For comparison, the f roll of bars 273-276 has an index of +1 dB at 101 Hz and is heard.

Cause (read from `build/parts.json` and `tools/score_to_parts.py` lines 4301-4440). The first stroke gets `TIMP_LOUD_ATTACK_DB` = 6.0 plus about 4.5 dB of envelope (vol_db 13.1 at 888.0, 4.2 by 888.75). The roll trim for fff is +2.6 dB: `TIMP_ROLL_TRIM_DB` is fitted so that fff is 5 dB over f, where the brass measure 11-13 dB between f and fff in this render. At bar 223 the -5 dB roll settle is applied on top of the printed diminuendo, because 888.0 is not in `TIMP_SETTLE_SKIP`, and CC7 falls another 6.3 dB (76 to 53) with CC1 (120 to 88). Rimsky-Korsakov describes the kettle-drum tremolo as usable at every dynamic up to fortissimo (Principles of Orchestration, book p. 29-30), so a roll that disappears under a tutti is a mockup fault and not an orchestral norm (inferred from the book; the levels are measured).

Fix, in `build/score_config.py`, level only, first strokes unchanged:

`LEVEL_SHAPES_S["Timpani"] = LEVEL_SHAPES_S.get("Timpani", []) + [(888.0, [(0.20, 0.0), (0.45, 5.0), (1.95, 5.0), (2.08, 0.0)]), (1108.0, [(0.30, 0.0), (0.50, 4.0), (1.95, 4.0), (2.09, 0.0)])]`

The times are seconds from the score onset (bar 223 lasts 2.12 s; qn 1108 to 1113 lasts 2.09 s). Both shapes return to 0 dB before the next event, so the f stroke at 892 and `FINAL_RING` are not changed. The actor should confirm that the generic `LEVEL_SHAPES_S` code (tools lines 5073-5120) is applied to the Timpani track after the timpani's own vol_db. If it is not, the equivalent for bar 223 is `TIMP_SETTLE_SKIP = [888.0, 1108.0]` plus the smaller shape `(888.0, [(0.20, 0.0), (0.45, 3.5), (0.70, 3.5), (1.60, 0.0)])`.

Targets. Bar 223, 250 ms windows: -28.4 (unchanged), then about -30, -32.5, -33, -34, -35, -36, -36, so the roll still falls through the bar and ends 1-2 dB over the f stroke of bar 224. Index at 127 Hz -6 dB or better (now -11). Bar 278: body -30 to -32.5 dBFS, index at 160 Hz -3 dB or better (now -7). The master rises by about 0.1 dB. The pre-limiter peak (+1.11 dBFS at 420.98 s) lies 0.23 s after the bar 278 downbeat, before the shape begins at 0.30 s, so the limiter's work does not rise. Do not raise the first strokes.

### 2. Horn 1's theme at p in bars 139-140: the notes of one phrase differ by up to 20 dB (measured)

Where: Horn 1, qn 551.66-560 (bars 139-140), the first statement of the theme in section J, printed p with an accent on the first note. Horn 1 is the top stem here from the second note on; nothing masks it.

What is wrong: the first note of the tune is too weak, and the staccato F4 at qn 556 is louder than the printed f note four bars later.

Evidence. Stem mean per note: G4 at 551.66 ("Sus MAX", CC1 42, velocity 73) -56.0 dBFS; D4 at 553.80 ("Leg Slur MAX") -43.2; E flat 4 at 555.30 -45.1; F4 at 556.00 (staccato, "Marc Shrt RRx4", velocity 70) -35.9; E flat 4 at 556.66 -44.5; D4 at 557.30 -44.5; C4 at 558.00 (staccato) -39.5; B3 at 559.00 (staccato) -40.3. The printed f G4 at 567.75 is -37.0. During the first note Horn 4 (-49.3), Violas (-50.2), Horn 3 (-50.2) and Clarinet 1 (-51.5) are all louder than the melody. In the mp3 the F4 window (556.0-556.5) is -29.3 against -36.0 and -36.2 for the windows before it: one note 5.5-7 dB over its phrase. The c11 mp3 shows the same (-29.5 against -36.7 and -37.2), so this is not render drift, and no earlier report treats these notes.

Cause. (a) `_hn_stac_vel = [(60, 70), (90, 88), (110, 98), (124, 100)]` has no row under 60, so staccatos at p get velocity 70. Horn 1's f staccatos elsewhere (velocity 77, envelope +3 to +5.4 dB) measure -38.9 to -44.4, so its p staccatos are as loud as or louder than its f staccatos. Of Horn 1's 38 "Marc Shrt RRx4" notes only these three are at a dynamic of 60 or lower. (b) At p the "Sus MAX" row is 10-13 dB under the "Leg Slur MAX" row at the same CC1 (other p sustains near G4 at qn 400.8, 403.7 and 405.7 read -56.5, -57.1 and -56.6).

Fix. Per-note trims in `build/note_trims.json` (format `{track: {score onset: dB}}`): `"Horn 1": {"552.0": 10.0, "556.0": -8.0, "558.0": -4.5, "559.0": -4.5}`, merged with any existing Horn 1 entries. If note trims are clamped below 10 dB, use `LEVEL_SHAPES_S["Horn 1"]` in `build/score_config.py` instead: `(552.0, [(-0.14, 0.0), (-0.12, 10.0), (0.56, 10.0), (0.64, 0.0)])`, `(556.0, [(-0.03, 0.0), (-0.01, -8.0), (0.19, -8.0), (0.23, 0.0)])`, `(558.0, [(-0.03, 0.0), (-0.01, -4.5), (0.55, -4.5), (0.60, 0.0)])`. A more general alternative for the staccatos is a soft part in the velocity table for the span (552.0, 664.0), for example `[(34, 40), (46, 50), (60, 70), (90, 88), (110, 98), (124, 100)]`, which leaves every note at a dynamic of 60 or more unchanged; the actor must fit the two new rows by render because velocity also changes the layer on short rows (manual p. 102, cited in the config comment).

Target: every note of qn 551.66-560 within 3 dB of -44 dBFS stem mean, the first note not under the second, and the mp3 window at 556.0-556.5 no more than 2 dB over the windows before it. The slurred pair at 572.58 / 573.33 in the f statement is 7-9 dB under its neighbours (-46.1 / -45.3 against -37.5 / -39.2), but Horn 1 is 6-16 dB under the master there; leave it this cycle.

### 3. Bassoon 1 solo: the level falls 5-6 dB for 200 ms at the join into qn 464 (measured)

Where: Bassoon 1, qn 464 (bar 117), A4 on "Leg Slur Exp" (note-on 463.58, velocity 80 where its neighbours have 100). The bassoon is the only sound: index +23 to +27 dB.

What is wrong: the stem falls from -48 dBFS (body of the previous note) to -53 / -54 between 100 ms before the beat and 100 ms after it, and reaches the new note's body (-45) only 0.25-0.30 s after the beat. 50 ms steps from -0.30 s: -47.5, -48.3, -48.5, -49.1, -53.1, -54.4, -54.1, -54.0, -52.4, -50.3, -48.0, -46.3, -45.7. This is the place listed as a join 134 ms late; c12's critics A and C found that it is a late level and not a late pitch, and my numbers agree. It was not worked on in c12. Because nothing covers it, it is audible as a hole in the line (inferred).

Fix, in `build/score_config.py`: `LEVEL_SHAPES_S["Bassoon 1"] = LEVEL_SHAPES_S.get("Bassoon 1", []) + [(464.0, [(-0.14, 0.0), (-0.10, 5.0), (0.10, 5.0), (0.22, 2.0), (0.30, 0.0)])]`. Fallback if the raised transition sounds wrong: take qn 463.5-465.9 out of the "Leg Slur Exp" span (lines 588-589) so the note uses the row of its neighbours with velocity 100.

Target: no 50 ms window between -0.15 and +0.25 s more than 3 dB under the previous note's body (-48 dBFS).

### 4. Muted Trumpet 1 solo: keep the +0.03 s overlap at eight joins only (inferred from the actor's join log; flutter measured)

Where: Trumpet 1, "Mute Sus", qn 680-744 (bars 171-186), with the cor anglais.

Overlap. The general +30 ms overlap doubled the time in which two pitches sound. From `cycles/c12/logs/joins6b.log` the overlap is worth its cost at 685, 687, 688, 691, 694, 717, 719 and 726. It is not at 715 (144 ms of two pitches where the dip without overlap was only 4.7 dB) and not at 692 (the crossing moves from +75 to +115 ms after the beat). Use 0-0.01 s everywhere else. `ROW_SLUR_OVERLAP_S = {"Trumpet 1": {"Mute Sus": 0.03}}` (line 692) is per row, so this needs a per-onset form read at the same place in `tools/score_to_parts.py`, for example `ROW_SLUR_OVERLAP_AT = {"Trumpet 1": {685.0: 0.03, 687.0: 0.03, 688.0: 0.03, 691.0: 0.03, 694.0: 0.03, 717.0: 0.03, 719.0: 0.03, 726.0: 0.03}}` with the row default set to 0.0. Target: two pitches together for more than 60 ms at no more than 8 of 22 joins (now 13), and a median of 45 ms or less (now 70).

Flutter. On the three long notes that can be measured, the level modulation is 5.9 dB at 4.4 Hz (qn 711.7), 0.7 dB and 2.0 dB; the median is about ±1 dB. I do not find ±6 dB at 8 Hz. The range of the master's band level is the same with and without the trumpet stem. The flutter is not audible as a fault (measured levels, inferred audibility). No change.

Balance. The muted trumpet is 2-3 dB under the cor anglais in bars 171-174 and 179-183 (target 3 under). Keep the per-bar roles at 680-732.

### 5. The stops at bars 2 and 6 are at the wetness limit because of the celli's own release, not the hall (measured)

Where: Violoncellos, G2 (open string) quarter notes at qn 4.0-5.0 and 20.0-21.0; stops at qn 5.06 and 21.06.

Evidence. In the 0.3 s after the bar 2 stop the Violins I stem falls 23 dB and the Violoncellos stem falls 9 dB. At +0.30 s the celli's direct stem is -39.3 dBFS against -36.0 for the whole master and -46.1 for the R Strings return; at +0.45 s it is -44.4 against -43.1 and -52.3. From +0.3 s the dry cello release is about half to three quarters of the master's power, and the string return is 7-8 dB under it. The celli's envelope is still raised at the release (vol_db +2.1 at qn 5.0, +1.3 at 5.25, +0.6 at 5.5). Bar 6 shows the same pattern.

Fix, in `build/score_config.py`: `LEVEL_SHAPES_S["Violoncellos"] += [(4.0, [(0.40, 0.0), (0.55, -6.0), (1.20, -6.0), (1.60, 0.0)]), (20.0, [(0.40, 0.0), (0.55, -6.0), (1.20, -6.0), (1.60, 0.0)])]` (the note ends 0.36 s after its onset; the celli rest until qn 16 after the first; the actor should check that the second shape ends before the next cello note). By power sum this lowers the master by 1.9 dB at +0.30 s and 3.5 dB at +0.45 s and brings the time to -20 dB forward by 0.03-0.05 s (inferred). Target: 0.45 s or less at bars 2 and 6 on the mp3 by the actor's measure (now 0.50). Do not change the returns for this.

### 6. Violoncellos: three single notes with wrong levels at qn 564, 100 and 1009 (levels measured, audibility inferred)

qn 564 (bar 142). The held B2 (note-on 563.45, "Leg BC", velocity 53, printed crescendo from 564) reads -62.5 dBFS until 564.5 and -59.7 until 566.0, after staccato notes at -50.3 to -53.9. It enters 9-12 dB under the notes before it and stays there for about 0.9 s; it reaches -47.3 from qn 566. This agrees with the actor's "7-10 dB weaker than c11". In the mix the start is masked (index -18 dB), so the listener impact is low. Fix: velocity 100 on this note (`LEG_VEL_STRONG` maps 52 to 100 on string legato rows, but this same-pitch re-attack kept 53), or `LEVEL_SHAPES_S["Violoncellos"] += [(564.0, [(-0.20, 0.0), (-0.12, 9.0), (0.55, 9.0), (1.10, 3.0), (1.60, 0.0)])]`. Target: within 3 dB of -50 dBFS from 0.15 s after 564.

qn 100 (bar 26) and qn 1009 (bar 253). Both are on the actor's drift list and both carry a printed accent (velocity 118 and 124). The note at 100 is 6 dB over the previous note, the note at 1009 is 8-10 dB over its neighbours. These are the only two drifted notes that may be audible as faults. Fix: `build/note_trims.json` `"Violoncellos": {"100.0": -3.0, "1009.0": -4.0}`. Target: an accented note 3-5 dB over its neighbours.

## Answers to the coordinator's items

Wetness. Time to -20 dB at the bar 2 stop: 0.52 s on the c12 mp3 by my method (the actor's method gives 0.50; the c11 mp3 gives 0.50 by mine; the c12 master 0.47). Bar 6 0.47 s, bar 113 0.36 s, bar 166 0.35 s, bar 204 0.42 s; the actor's bars 26 and 94 are 0.28 and 0.42 s. The final chord is 20 dB down about 0.45 s after its fall begins. I did not make a separate RT60 estimate; the returns are unchanged from c11. Verdict: right. The mix is at the limit at the two opening stops only, inside it elsewhere, and not too dry. Add no hall. If margin is wanted at bars 2 and 6, take it from the celli (finding 5).

Limiter. The pre-limiter peak is +1.11 dBFS at 420.98 s (bar 278), which is 2.6 dB of limiting to -1.5 dBTP. The next peak is +0.11 dBFS at 419.33 s (bar 277), 1.6 dB. The limiter works over 2 dB at one place. Confirmed within the limit of about 3 dB.

Tone. Octave shares of the loudest 10 % of frames, c11 / c12 / Dvorak 9 i reference: 63-125 Hz -14.6 / -13.0 / -14.4; 125-250 Hz -11.9 / -9.9 / -6.9; 250-500 Hz -7.4 / -6.4 / -6.5; 1-2 kHz -4.4 / -6.0 / -7.1. The 125-250 Hz, 250-500 Hz and 1-2 kHz bands moved toward the reference. The 63-125 Hz band moved from 0.2 dB under the reference to 1.4 dB over it. The new tone is an improvement (measured against the reference; "by ear" is inferred). Add no further lift under 125 Hz.

Stem-fix notches. Violoncellos qn 325 (bar 82): the stem dips 8-9 dB for 60 ms, the stem is 10 dB under the master, and the master shows no dip (-34.2 to -34.5 through the notch). Violas qn 728 (bar 183): the stem dips 11-12 dB for 40 ms, 14.4 dB under the master, no dip in the master. Neither notch is audible as a fault. Neither produces an audible separation in the mix either; they cost nothing and can stay.

Drifted single notes. Possibly audible: Violoncellos 100 and 1009 (finding 6). Mild: Horn 1 at 570 (3-4 dB over its neighbours). Masked, not faults: Flute 2 1007, Oboe 1 796, Bassoon 1 119 and 1058, Horn 3 122, Violins II 42, 56 and 1060, Violas 1014.

Basses' on-beat eighths, qn 1088-1108. Close it. The master's low band (35-125 Hz) at these beats is formed by basses (-42.5 dBFS), celli (-44.4) and timpani (-45.3) together, and its on-beat rise is on time: the actor measures +18 / +0 ms, and my cruder half-rise measure gives a median of -25 ms. My measure does not reproduce the actor's +70 ms for the stem alone, so I do not use it against that figure. A late bass stem is not audible in the mix (inferred).

Basses under the second chorale. The bass is present: the basses lead the 63-80 Hz bands by +6 to +8 dB in bars 255-256. The master's 31.5-125 Hz share is -21.7 / -22.6 dB by my measure (the actor's -22.3 / -20.8). The basses give almost all of it (-23.3 / -23.5); the tuba gives -28.7 / -26.9 and the bass trombone -33.9 / -30.8; the contrabassoon rests until qn 1023.9. The share reaches -17.4 in bar 257 and -14.1 in bar 258 when the scoring fills in. The gap to -17 in bars 255-256 is the scoring. If the actor wants more, the basses should give it: `build/roles.json` `"Double basses": [1016, 1024, 1.5]` (share to about -20). The tuba and contrabassoon -3 dB at 984-1056 stays. I propose a target of -20 dB for these two bars and closing the item.

Flute 2 at qn 650 and 618. Flute 2 is an inner voice there, 11-12.5 dB under the mix (index -4 / -5 dB in its best band). The late joins are not audible as faults (inferred). Low priority; the planned "Sus MAX" with 70 ms overlap is harmless but changes little for a listener. Bassoon 1 at 464 is finding 3.

Master true peak. +0.1 dBFS on 2 samples of the master WAV is not audible, and the delivered mp3 is at -1.5 dBTP. No action, except that the first stroke of bar 278 must not be raised.

Tempo arcs (888, 912) and (916, 936). Bars 223-233 last 2.11-2.14 s, with bar 228 at 2.21 s and bar 234 at 2.18 s; bars 235-237 last 1.82 s. The arcs lengthen the phrase-end bars by 2-4 %. They change no level. No objection from this lens.

Cello same-pitch repeats. The two notches are masked (above). I found no level fault caused by the detach dip.

sfp at qn 592 (bar 149). Works: the brass fall 13-15 dB within 0.4-0.5 s and rise again from 0.7 s without a second dip; the master goes from -19.8 to -30.5 dBFS at +0.6 s. Keep.

Flute 1 / Flute 2 / Oboe 1 trims. Flute 1 is not too weak. Solo margins over the loudest other stem: bars 43-44 5 and 7 dB, bar 89 about 5 dB, bars 105-106 7 dB. The smallest is bar 102 with 1.6 dB over Clarinet 1; optional `roles.json` `"Flute 1": [404, 408, 1.5]`. At printed f and ff Flute 1 is within 1 dB of Clarinet 1 and within about 3 dB of Oboe 1 (A-weighted medians over steady bars). Across families the levels at p, f and ff agree within about ±4 dB; the p-to-pp step is small on Horn 1 (0.6 dB) and Violins I (1.8 dB), which I report without a fix.

Delivery ride. Bars 42-50: the ride rises 5 dB (0.6 dB per bar), so in the mp3 bars 49-50 are 3-4 dB over bars 42-43, where the master has them 1-2 dB under. The rate is slow enough not to be heard as a gain change (inferred), but it reverses the printed p-to-pp direction of section C. Optional: hold the ride within 1.5 dB over bars 42-50 and take the rest at the bar 50/51 boundary, where Trumpet 1's solo begins. Bars 164-196: +8 to +12 dB in 171-186, steps of +3 at 166/167 and +2 at 170/171; acceptable. Other steps over 1 dB per bar: 66/67 (-4), 94/95 (+4), 146/147 (-3).

fff at bar 263 against 262. Bar 263 is 1 dB over bar 262 in the mp3 (K-weighted), and its first 0.6 s is 1.0 dB under the hits of bars 223 and 278 on the master. The step is small. If a larger step is wanted, lower bar 262 by 1 dB in the ride; do not raise 263 (inferred).

Solos and roles not mentioned above (all measured, all in order): Trumpet 1 bars 51-66 leads by 6-13 dB; the violins lead bars 67-82 by 3-8 dB; the bassoon solo of bars 115-121 leads by 11-14 dB; the harp has an index of +3 to +11 dB at every onset; the theme group of bars 27-34 (Horn 3, tuba, bass clarinet, contrabassoon, celli, basses) leads; Trumpets 1 and 2 lead theme B in bars 211-216 by 1-6 dB; in the first chorale the brass are 7-9 dB over Violins II and Violas in bars 224-225, and the woodwinds and Violins I have the melody in bars 226-228; in the second chorale (bars 258-263) the group levels on one A-weighted scale are trumpets 8.0 to 12.4, low brass 4.1 to 10.8, horns 5.0 to 9.6, woodwinds 6.7 to 9.8 and each string section -3.3 to +4.5, so the chorale is over the string tremolo; the crash cymbals have an index of +6 to +8 dB at 10 kHz on the stroke and -7 dB in the body, heard and not dominant; the basses have an index of +2 to +15 dB at 50-80 Hz throughout, and the master's 63-125 Hz share is 1.4 dB over the reference: solid and not boomy (inferred).

Closed items. I have no new evidence on the 315 Hz hump, "Sus Accent MAX", "Leg Slur Exp" on cor anglais and Oboe 1, or the tuba / contrabassoon -3 dB. Finding 2 is in section J but concerns note levels, not the hump.

Findings from the other movements. (a) `RR_RESET_AT` is already in the finale's config (line 554) for the Double basses only. Extending it to the tracks whose short notes drifted, with reset points at the bar lines before the drifted notes, is an inexpensive test of whether that drift is round-robin state. I did not check which drifted notes are on round-robin rows (inferred). (b) Movement I's short-crescendo rule: I did not test the finale's hairpins against it. The place where its intent applies is Violoncellos qn 564 (finding 6): the start of a crescendo is 9-12 dB under the notes before it. The crescendo is 4 qn long, so the rule's threshold does not catch it. (c) Clamped low-wind swells: the finale's tools already contain `HP_SWELL_CEIL` and `HP_LOUD_SWELL_DB`. In the passages of this lens no low-wind swell covers a solo, so I have no place to apply it.

Other checks. Loop pulsing: no held note is longer than the loop length except the timpani roll at 1088, which `TIMP_ROLL_RESTRIKE` covers. The brass tilt-jump accent check was not repeated; it is outside this lens. No research default is rejected in this report.

Do not touch: the first strokes of the timpani, bass drum and crash cymbals at bars 223, 263 and 278; the four returns and their sends; the c12 delivery EQ (42 Hz high-pass, 1.5 kHz -1.5 dB bell, 6 kHz -3 dB shelf); the tuba / contrabassoon -3 dB at 984-1056; Trumpet 1's per-bar roles at 680-732 and its 6-13 dB lead in bars 51-66; the sfp notch and fronts at 592; the Flute 1 / Flute 2 / Oboe 1 f and ff trims and pitch trims; the notches at 325 and 728 and the celli's detach dip; the basses' gain, beat gaps and metric tables with the CC16 reset; the ride rows at 164 and 679 and the final ride row; the bar 262-264 trims; the bar 42 subito; `FINAL_RING`; the trumpets' ff trims; the per-dynamic string caps; the legato velocity floor of 100; Horn 3's role at 548-564; the f timpani roll of bars 273-276.

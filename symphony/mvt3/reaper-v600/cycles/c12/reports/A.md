# Cycle 12, critic A: articulation and phrasing (render under review: c11)

Method. I read the brief, history, learnings, the research findings (Parts 1-6) and the template plan, then measured the c11 stems, master and mp3 with my own scripts (band envelopes from FFT band-pass filters, per-note onset and join levels, per-bar levels, third-octave spectra, note and controller data from `cycles/c11/rendered_build/parts.json`). "Measured" means a number from those scripts. "Inferred" means a judgement about what a listener hears or about a cause I could not isolate. Not re-measured this cycle: loop pulsing (the 3.95 s fold) and the re-bow dips of the chorale (bars 223-234); I have no new statement on them.

## Manual notes (May 2021 HO manual; cycle 12 slot A: p.72-74, 116-117, 121-122)

| Reading (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| Harp "Maestro Gliss" and "Gliss Angelic" hold one recorded glissando per white key, each with a fixed root and scale (p.72-74). | Harp glissando, bar 277 (qn 1106-1108), printed tuning C D E G A. | Yes. No recorded glissando has the printed tuning, so the render plays 15 notes (G3 to E6) on `Harp Sus RR.oib`, 0.127 qn apart, velocity 90-112. The harp stem is 2-4 dB under the master at 1106.5-1106.9 and 13-21 dB under at the start (measured). Keep. |
| Cymbal pairs: C3 long, D3 short, E3 shorter; 3 round robins, 7 velocity layers (p.116). | Crash, qn 888, 1048, 1108. | Yes. Key 60 (C3 long), velocity 124, on `22in Zildjian K Crash.oib`. Onset within 4 ms of the beat (-20 dB re peak); the strokes at 888 and 1048 ring 9.0 s; the last one ends with the cut-off (-61 dB 0.3 s after the note end). |
| p.117 describes the 20in pair as the one with the broadest spectrum for full-orchestra passages. | Same three strokes. | Open. The 22in stem is 10.7-12.8 dB under the master at the strokes. Whether the crash is heard enough is B and C's question; a patch change costs one instance. |
| Snare and field drums (p.121). | Not in the score. | Not applicable. |
| 36in Ludwig Bass Drum: C1 felt short, D1 felt long, E1 felt roll, G1-E2 felt crescendos, up to 12 velocity layers (p.122). | Bass drum, qn 888 and 1108. | Yes. Key 38 (D1 felt long), velocity 114. Peak 41 ms after the beat, -20 dB after 0.26-0.29 s. The stem is 16 dB under the master (balance: B and C). |
| Timpani Felt KS and Felt Cresc exist next to Hard KS (p.123-125; MANUAL-GAPS #12). | Printed "soft sticks" at qn 680, "near the rim" at 708, "medium sticks" at 856; 13 roll crescendos. | No. `Timpani Hrd KS.oib` plays the whole movement. Deferred for memory in earlier cycles; still open. |
| MANUAL-GAPS #13: the 1TB patch has no sample for B flat 1. | Bass trombone, qn 416. | Still open. |
| Harp harmonics have their own patch (MANUAL-GAPS list). | Harp, bar 43 (qn 168, 176, 184). | No. The harmonics are ordinary plucked notes at the sounding octave (B flat 4, velocity 46). Still open; memory permitting. |

## Ranked findings

### 1. Cello repeats of the same pitch on Sus MAX have no new bow (S1)

Where: Violoncellos, repeated G2 half notes in bars 25, 152, 158, 165 (qn 98, 604, 630, 658), and the repeats that kept a 10-24 ms data gap: Violoncellos qn 325 and 327 (tenuto quarters), 564, 832; Violas 426, 556, 564, 728; Violins I 876, 896; Violins II 880.

Evidence (measured). The detach dip is in the data (for qn 98: -5 dB from 97.50, back to -1.5 dB at 97.79; note gap 90 ms). The stem shows no separation: the level dip is 1.4 dB at 98, 3.4 dB at 604, 1.9 dB at 630 and 1.8 dB at 658. For all cello repeats with a 75-105 ms gap the median dip is 3.4 dB and 7 of 15 are under 3 dB; the violas' same class has a median of 9.2 dB (n 46). At 630 and 658 the first note sits at -27 to -32 dB and the 300 ms after the repeat sit at -34 to -42 dB: the first note is on a legato row (velocity 124, note-on 150 ms early), the repeat is a Sus MAX note at velocity 96 (note-on at 629.72 and 657.72), so the repeat starts 7-10 dB under the note before it. The cello stem is 4.3 dB under the master at 98 and 7.2 dB under at 604, so the line is exposed. Cause (inferred): the Sus MAX release fills the gap and the new note has a slow, quieter start, so there is neither a gap nor an attack.

Fix. In `build/score_config.py`:
- `STR_REP_DETACH["at"]["Violoncellos"]`: give the spans (64.0, 104.0) and (596.0, 672.0) the options `{"max_qn": 2.0, "same_pitch_only": True, "dip_db": -10.0, "dip_s": 0.10}`.
- Raise the start of the repeats at 630 and 658 to the level of the note before: `LEVEL_SHAPES["Violoncellos"] += [[(629.72, 0.0), (629.76, 4.0), (630.6, 4.0), (631.0, 0.0)], [(657.72, 0.0), (657.76, 4.0), (658.6, 4.0), (659.0, 0.0)]]`. If the tools can set the velocity of a Sus MAX repeat that follows a legato-row note, use the previous note's velocity (124) instead of the shape.
- The sites with 10-24 ms gaps did not get the 0.09 s gap of `STR_REP_NEW_BOW` although 325 and 327 carry tenuto marks at mp. Find why the "tenuto" and "plain" classes skipped them and bring them to 0.09 s.
Accept when each listed site has a dip of 6 dB or more (minimum 20 ms RMS in the 150 ms before the onset against the body after it).

### 2. The sfp of bar 149 (qn 592) still swells 0.25 s after the onset; four stems cause it

Where: Trombone 2, Bass trombone, Tuba, Horn 3 at qn 592.

Evidence (measured). In the first 0.1 s the master is within 1 dB of the ff before it, so the c11 bumps (+3/+4 dB on Horn 1, Horn 3, Trombone 1, Clarinet 1, Bassoon 1) do put the front at the level of the preceding ff. The master's late peak (+0.26 s) comes from Trombone 2 (stem peak at +0.245 s), Bass trombone (+0.27 s), Tuba (+0.23 s) and Horn 3 (+0.275 s); each sample swells 2.4-3.2 dB after its onset. With these four stems removed the master is flat after the front. CC1 on the brass starts to fall at +0.136 s and reaches 42 at +0.30 s, which is later than the swell. Trombone 2's trim row steps down at the onset (-0.5 dB at 591.89, -2.5 at 592.0, -4.4 at 592.11), so its front is cut and its swell is kept. Horn 3's c11 bump ends at 592.25 (+0.09 s), before its swell.

Answer to the open item: "Sus Accent MAX" is not needed for the sfp as a whole. Fix without memory cost first, in `LEVEL_SHAPES` (1 qn = 364 ms here):
- Bass trombone and Tuba: `[(591.95, 0.0), (592.0, 3.0), (592.40, 3.0), (592.55, -2.5), (592.85, -2.5), (593.1, 0.0)]`.
- Trombone 2: move the -4 dB step of its trim row from 592.0-592.11 to 592.40-592.55, then add `[(592.40, 0.0), (592.55, -1.5), (592.85, -1.5), (593.1, 0.0)]`.
- Horn 3: keep the c11 bump and add `[(592.35, 0.0), (592.55, -2.5), (592.85, -2.5), (593.1, 0.0)]`.
Accept when the master's level at +0.2 to +0.3 s is at least 3 dB under its first 0.1 s. If the row is still wanted afterwards, load it only on Trombone 2 and Bass trombone (1TB, key 25) and Tuba (1TU, key 61) (p.101); Horn 3 comes next. The other brass do not need it (inferred from the stems).

### 3. The muted trumpet solo is tongued at some slurred joins and connected at others

Where: Trumpet 1, con sordino, bars 171-183 (qn 680-730), printed slurs 680-694 and 712-728, "Mute Sus" row of `1TP KS Master.oib`.

Evidence (measured). `ROW_LEAD_S = {"Trumpet 1": {"Mute Sus": 0.035}}` starts each note 35 ms early and ends the note before it 7 ms earlier still, so every slurred join is a fresh attack after a gap. The level minimum in the 100 ms before each beat, against the new note's body: 9 of 22 joins are deeper than 4.5 dB (683: 6.6, 688: 8.0, 690: 9.7, 715: 9.8, 720: 6.1, 719: 5.8, 685: 4.8, 687: 4.8, 717: 4.7 dB) and 5 are under 1.5 dB (684, 691, 694, 716, 728). At 690 the stem falls from -47 to -59 dB for about 50 ms. With identical data (velocity 53, CC1 42, CC11 54) the note bodies differ by 4.9 dB: E flat 4 -51.0, D4 -55.2, C4 -55.5, G4 -52.2, D5 -51.0, C5 -50.6, B flat 4 -53.4, A flat 4 -54.2 dB. D4 and C4 are 4.2-4.5 dB under the E flat 4 next to them in both phrases (683-686 and 715-718). The stem is 4.4-11.7 dB under the master, so it is the leading voice. Inferred: the line alternates between tongued and slurred joins with no reason in the score, and the pitch-to-pitch level spread is heard as dynamics that are not printed. The library has no muted legato row for this trumpet (loop/LEARNINGS.md line 8).

Fix. In `tools/score_to_parts.py`, at the `ROW_LEAD_S` step (comment near line 1115): for a join under a printed slur, end the previous note 0.03 s after the moved onset instead of 0.02 qn before it. Suggested key: `ROW_SLUR_OVERLAP_S = {"Trumpet 1": {"Mute Sus": 0.03}}`. Mute Sus is a polyphonic sustain row, so the old note's release covers the new attack. Then level the pitches over 680-730 in `LEVEL_SHAPES["Trumpet 1"]`: +3 dB on the D4 and C4 notes (qn 684, 685, 716, 717). Accept when all join minima are within 4 dB of the body and no join holds two pitches for more than 60 ms. No memory cost. The overlap value is inferred; it has to be measured after the build.

### 4. The basses' on-beat eighths in bars 273-277 arrive about 90 ms after the beat (S2)

Where: Double basses, qn 1088-1108 (Largamente, hammered eighths on C2, Sus MAX).

Evidence (measured). Time from the beat until the stem's 30-120 Hz level is within 3 dB of the slot's peak: qn 792-816 +42/+49 ms (downbeats/other beats), 816-840 +20/+15, 984-1056 +28/+43, 1056-1088 +10/+9, 1088-1108 +89/+90 ms. The passages 1056-1088 and 1088-1108 have the same pitch, velocity 83, CC1 90, CC11 88 and length 0.325 qn. In 1088-1108 the tuba, contrabassoon, cellos and timpani hold long notes, so the basses alone carry the eighth-note pulse in the low band: the master's 30-120 Hz level is flat until +55 ms and peaks at +95 to +135 ms, against +15 to +35 ms in 1056-1088. Cause (inferred): 1 qn is 417 ms here against 341 ms, the gap before the beat is 73 ms against 61 ms, the old note's release has decayed further when the -9 dB beat gap ends, and the slow attack of the new Sus MAX note is exposed.

Fix. In `STR_REP_DETACH` or the tools' string re-tongue lead, give the on-beat eighths of the span (1088.0, 1108.25) an onset lead of 0.06 s with the beat gap ending at the moved onset; or lengthen the off-beat eighths of that span from 0.325 to 0.40 qn (the length factor that now gives 0.65 of the slot; gap 42 ms). Accept at +40 ms or less by the measure above. The c11 beat gaps on 792-840 and 984-1088 are good and stay (see the answers below).

### 5. Bassoon 1's top note at qn 464 enters 8-10 dB low

Where: Bassoon 1 solo, bars 115-124 (qn 455-496), A4 at qn 464 (bar 117, cresc. to mp), `ART_SPANS` "Leg Slur Exp" (config lines 588-589).

Evidence (measured). The note data are identical in c10 and c11, and the c11-minus-c10 residual is 27-40 dB under the stem: the sound did not change. The reported move from +59 to +134 ms is an effect of the onset estimator on a slow swell. The actual shape: the D4 before it stops about 100 ms before the beat, and the A4 is 8 dB under its final level 100 ms after the beat, 4 dB under at +200 ms and reaches it at +300 to +400 ms. Front minus body over the solo has a median of -1.0 dB, with -6.0 dB at 462, -7.5 dB at 464 and -9.9 dB at 472. Inferred: the top of the phrase is heard as a sag, then a swell.

Fix. `LEVEL_SHAPES["Bassoon 1"] += [[(463.55, 0.0), (463.72, 5.0), (464.25, 5.0), (464.85, 0.0)], [(461.72, 0.0), (461.9, 4.0), (462.3, 4.0), (462.8, 0.0)], [(471.72, 0.0), (471.9, 6.0), (472.3, 6.0), (472.8, 0.0)]]`. If the sag stays above 4 dB, take 463.5-465.9 out of the Leg Slur Exp span (Leg Slur MAX there). This also answers the deferred item: do not put Leg Slur Exp on the cor anglais and Oboe 1 until these joins are fixed, because the row brings the same slow starts (inferred from the bassoon).

### 6. Flute 2: close the qn 650 item on the sum; its legato row is uneven against Flute 1

Where: Flute 2, qn 648-652 (bar 163) and its unison passages with Flute 1.

Evidence (measured). On `FL2 KS Master.oib` the D flat 6 needs about 435 ms from note-on to its perceived attack on the legato row, and the reading moved 1:1 with the lead (0.9 qn = 321 ms in c11). The same zone is slow on Sus MAX too (+98, +97, +176 ms at qn 600, 632, 660; Flute 1 +11, +27, +14 ms). In the sum the join is on time: Flute 1 plus Flute 2 at 650 reads -31 ms, the upper winds -33 ms, and Violins I double the line. On unison notes Flute 2's Leg Slur MAX level against Flute 1 has a median of -5.8 dB (p10 -13.9, p90 +2.2); on Sus MAX the median is -0.2 dB.

Answer to the open item. The score slur runs 648-652, so a re-attack at 650 breaks a printed slur; of the two ideas I choose velocity 122. My recommendation is to stop chasing the single-stem number: judge the join on the flute sum (already within 40 ms) and restore c10's lead at 650 (0.448 qn; undo the c11 change to Flute 2 in `SOST_JOIN_LEAD_S` / `LEG_VEL_EXTRA_S`), because the 0.9 qn lead starts the new pitch about 250 ms before the beat, 15-20 dB under the note it leaves (inferred from the lead and the stem level). For the unevenness, add +4 dB to Flute 2 over its slurred unison spans with Flute 1 (per-row trim if the tools have one, otherwise `LEVEL_SHAPES["Flute 2"]`); B and C should confirm the balance.

## Answers to the coordinator's items

- Wetness (measured, c11 master): the tutti stops at qn 5, 21, 661 and 1113 reach -20 dB in 0.40, 0.38, 0.38 and 0.36 s; the final chord reaches -60 dB at about 1.45 s. Both are within the ceiling. The returns are 13.8 dB under the dry sum over the movement. I do not find the mix too dry (inferred); no change proposed.
- `--midi-only` drift (measured): no track moved without a data change. On unchanged passages the c11-minus-c10 master residual is -143 dB (qn 459-463.9), and the per-track residuals and cross-correlations of the 14 tracks show no level or timing change.
- Bar 275 (measured): master bars 274/275 are -21.0/-21.5 dB, the mp3 -19.3/-19.9 dB. The fall comes from the c11 shapes of critic B #1 (Horn 1 -4 dB, Horn 3 -3 dB, Trombone 2 -2 dB from 1095.8 to 1099): Horn 1, which carries Horns 1, 2 and 4, goes from -28.1 to -34.0 dB. A 0.5 dB fall per bar is below what is heard as a step (inferred). Optional: end the three holds at qn 1098 instead of 1099; Trumpet 1's figure, which they clear, ends at 1097.92.
- 315 Hz hump in J (measured): it is the scored pitches D4 (293 Hz) and F4 (349 Hz) next to an empty 250 Hz band (-12.1 dB re the 315 Hz band; no harmony pitch lies in 223-281 Hz). Contributors in the band, in dB re the stems' power sum: Horn 3 -5.0 (D4 held for 28.6 of 64 qn), Bass clarinet -10.2 (third partial of G2), Trombone 2 -10.5, Violas -10.6, Tuba -12.5, Violoncellos -13.5. It is not a resonance; a 315 Hz bell would cut the fundamentals of held notes. If less is wanted, trim Horn 3 by 1.5-2 dB over 536-600.
- Basses' beat gaps (measured): no holes. Time more than 12 dB under the slot peak has a median of 4-25 ms on the beats in 792-840 and 984-1088 (slots 170-179 ms), and the off-beat eighths peak 1.3-6.7 dB under the beats. Keep. The exception is finding 4.
- sf bumps at 592: see finding 2.
- Violas' chord-repeat gaps (measured): the 0.12 s new-bow gap separates at every site (n 8, median dip 8.4 dB, minimum 3.9 dB). The 0.06 s louré gap gives a median of 5.8 dB (n 16), with three sites under 3 dB (qn 92, 796, 820); that fits louré. Keep both values.
- Ride after the subito p at bar 42 (measured): the subito is 8.9 dB in the mp3 (9.0 dB in the master). Bar 43 is level with bar 42 in the mp3 (master -2.3 dB) and bar 44 is 4.3 dB over bar 43 (master +2.4 dB): the ride adds about 4.6 dB over bars 43-44, where the score has p and pp. If it is heard as a swell (inferred), move the ride's peak from qn 172 to 182.
- Tilt jump at brass accents (measured, 98 sites): p90 +3.3 dB on the master (c07 3.6; target under 3), median -0.1; brass heads of 984-1048: median -0.5, p90 +2.6. Worst sites: qn 408 (+4.8), 1058 (+4.7), 568 (+4.4), 40 (+4.4). At the target within 0.3 dB; no general change proposed.
- Other checks (measured): no chord is sent to a legato row; legato overlaps are 35 ms (winds, brass) and 45 ms (strings); keyswitches lead their notes by 7 ms or more; tremolo rows are on every scored tremolo note (888-1112); pizzicato onsets in 200-264 have medians of +7 to +33 ms; the harp's étouffez marks fall 20 dB within 0.2 s.

Do not touch: the returns and the wetness; the `--midi-only` workflow; the basses' beat gaps and 0.65 eighth length on 792-840 and 984-1088; the violas' 0.12 s and 0.06 s chord gaps; the crash (key 60) and bass drum (key 38) strokes, their timing and the final cut-off; the harp glissando built from Sus RR notes and the étouffez damping; legato overlaps and keyswitch leads; the pizzicato leads; the tremolo rows; the subito p at bar 42; the c11 brass heads of 984-1048.

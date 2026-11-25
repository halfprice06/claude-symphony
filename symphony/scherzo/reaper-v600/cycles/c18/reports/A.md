# Cycle 18, critic A: articulation and phrasing (on the c17 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB on the stems of `cycles/c17/render/` read against `cycles/c17/build_render/parts.json` (the MIDI and CC data as rendered; the stem fix changed role rows only). Comparisons use `cycles/c16/render/` with `cycles/c16/build_fix/parts.json` and `cycles/c15/render/` with `cycles/c15/build_render/parts.json`. Join timing is the actor's measure S (`cycles/c14/actor_scripts/s14.py`, run by me on the c17 stems; c16 values from `cycles/c16/records/S_c16.json`). "Measured" means a number from these files. "Inferred" means reasoned but not tested. Nobody heard the audio. Every fix below is on the instrument side (CC11, CC1, velocity, row, lead, note length). None of them moves the volume envelope.

## Manual notes (May 2021 HO manual, cycle 18 slot A: PDF pages 100, 103-107, brass)

| what the page says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.100: Hollywood Brass has Solo Horn, 2 Horns, 6 Horns, Solo Trumpet, 2 Trumpets, 3 Trumpets, and so on; KS Masters per section | Horns 1-4 on 1FH KS Master; trumpets on solo patches | Yes. No unison horn or trumpet line calls for a 2-player patch: Hn 3-4 have separate parts in the trio drone, and the trumpets play in thirds and fifths at bars 101-120 |
| p.103: brass Repetitions patches play a run of re-tongued notes at a base tempo of 120 / 145 / 170 bpm, synced to the host, with CC1 for loudness | the trumpets' repeated staccato quarters and eighths, bars 101-120 and 329-336 | Not used, and correctly so: the fastest base tempo (170) is far from quarter 264 / 288. On "StacSs DblTng RRx9" the repeats separate by 5.5-6.3 dB (bars 105-120) and 4.8-6.1 dB (bars 329-336) on the stems (measured, S1). Keep it |
| p.103: Double Tongue rows ("tiki tiki") | trumpets' short notes | Followed: "StacSs DblTng RRx9" |
| p.103: Sforzando Crescendo (Solo Horn, Solo Tuba): an sf attack, then a strong crescendo; velocity sets both | the tutti sfp < at bar 301 | Not applicable. The horns carry no sfp there (woodwinds and strings only), and the score keeps sf off the brass |
| p.104-105: brass crescendo patches (fast / medium / slow, or MOD SPEED on CC1 in three steps); trills; flutter; clusters | Hn 1 "p cresc" at 1068-1071 | Not used. The crescendo is short and slurred inside a legato line, so a CC crescendo is right |
| p.105: a brass slur needs no gap and an interval of at most an octave; legato patches are monophonic by default, CC22 0-63 makes them polyphonic | every brass "Leg Slur MAX" join | Followed: 0 joins over an octave and 0 chords on a legato row on all ten brass tracks (measured) |
| p.106: on legato rows the Mod Wheel sets volume and opens overblow near 127; **velocity sets the transition speed** ("the harder you press, the faster the slur") | Hn 1's motto tail 1068-1080; the trio drone; Hn 1's call bars 3-6 | CC1 stays 60-71, far from overblow: followed. The motto tail's transitions run at velocity 106-112, the fastest kind of slur. They leave an 8-20 dB sag after each slurred note (finding 2), and slower transitions are the manual's own control for that |
| p.106: Legato Slur Accent (accent strength by velocity); Legato Slur Repetitions (re-tongued same-pitch slurred notes) | no printed brass accents; Hn 1's tied G sharps | Not used, correctly: the score keeps accents off the brass, and Hn 1's G sharps are ties, not repeats |
| p.106-107: mutes and stopped horn; KS Masters switch rows by keyswitch | Hn 3-4 "senza sord." at bar 73 (qn 216) | No con sord. is printed for the brass, so "senza sord." is only a reminder; no mute row is needed. Brass keyswitches: no KS_MIN_LEAD fault found |

MANUAL-GAPS #2 (repetition rows): for the brass, p.103 rules them out at this tempo (above). For the strings I did not test them.

## Findings, ranked by what a listener would hear

### 1. String legato joins swell about an eighth before the beat and then sag. The join notches that covered this went with the shape layer at c15. The c17 celli CC11 dip ends before the swell it was meant to cut (measured; fix inferred)

Where: every string "Leg Slur MAX" line. The exposed cases are the trio tune in the celli (bars 169-184, qn 504-552), the second idea (bars 45-56, 121-140, 277-288) and the soft legato of the codetta and coda (violas 693 / 726 / 1035, Violins II 681 / 744 / 1071, celli 600 / 777 / 1065).

Evidence:
- At each join I compared the loudest 10 ms frame between the moved note-on and the beat with the mean of the new note's body (beat + 0.12 to + 0.45 s). Median excess: Violins I +3.3 dB (27 joins), Violins II +3.4 (23), violas +3.6 (43), celli +3.7 (61). 40 of the 154 string joins exceed 6 dB: Violins II 7, violas 14, celli 18. The same reading on the woodwind legato rows gives +0.1 to +1.1. So the max-against-mean bias is about 1 dB, and the strings' excess is real. The excess is the same at every dynamic (CC11 under 55: +3.8; 55-85: +3.0; over 85: +3.8) and at every velocity (velocity 90 or less: +3.8; over 90: +3.7).
- Timing, on the 70 joins whose excess is 4 dB or more: the energy peaks 58-90 ms after the moved note-on (medians per section), which is 98-128 ms before the beat. Within 0.5 s after the beat the level then falls 9-12 dB below that peak. Measure S reads these same joins within about 30 ms of the beat, because it finds the new pitch's harmonic onset, not the loudness. The pitch arrives on time, but the loudness lands an eighth early and the arrival note is weak.
- Trio tune, celli 504-552. Mean of beat + 0.10 to + 0.45 s against the 0.15 s before the beat: median -3.0 dB, and 6 of 13 joins fall more than 3 dB (c16 -2.0, c15 -2.6). Worst is 516 (bar 173): -28.5 dB at qn 515.5-515.75, then -42.4 at 516.25, so a 14 dB swell sits 65-130 ms before the beat. Also 546 -5.8, 520 -4.8, 512 -4.4, 507 -3.8.
- The qn 504 / 506 join. c17 wrote CC11 -14 units across 504.95-505.6 (the swell found at c16), but the swell sits at 505.5-505.75 in both renders: c16 -34.5 dB, c17 -34.3. By then CC11 is back at 60 (505.5) and 64 (505.6), so the dip cut 505.0-505.4 (-38.3 at 505.25) and left the swell standing. The level still falls 6 dB at the beat (505.5 -34.3, 506.0 -40.5).
- Cause. `JOIN_NOTCH_S` (celli 506, 570, 764, 800; Clarinet 1 459) and the older `JOIN_NOTCH` rows are "shape:join_notch" items. Since `VOL_CLASSES = ("slow",)` (score_config.py, Dan's rule of 2026-11-11) they are no longer written, which is correct under that rule. Nothing on the instrument side replaced them.

Fix: a new generic rule in `tools/score_to_parts.py`, `LEG_TRANS_CC` (CC11), with its scherzo values in `build/score_config.py`. On string Leg rows, at every pitch-changing legato join whose lead is 0.12 s or more:
- CC11 falls from the moved note-on + 0.03 s.
- It holds until the beat - 0.02 s.
- It returns to the resting value by the beat + 0.10 s. No pre-fall.
- Depth: 6 units for an excess of 4-6 dB, 9 units for 6-9 dB, 12 units over 9 dB. The strings' own slope is about 0.7 dB per unit under CC11 100 (finale technique 80). Write the depths as a per-join table generated from this measurement, not one global value.
- Hold the depth to the score onset as Movement II c57 #3 did for soft-entry shapes, so that it covers the swell however long the lead is.
- Range-test first on the celli at 504-552 (the 13 joins) and on violas 693 / 726 / 1035. Delete the c17 `CC11_ADD_SPANS` celli entry (504.95, 505.6, -14), because it is mistimed. Target: excess under +3 dB on 80 % of string joins, and celli 504-552 body against pre-beat at -1.5 dB or better.

### 2. Horn 1's motto tail (bars 357-360, qn 1068-1080) sags 8-20 dB after every slur. The tied G sharp has a 12 dB hole one beat after its arrival (measured; fix inferred)

Where: Hn 1 espress., B4-B flat 4-A4-G sharp 4, p < > into the pp held G sharp (score: p cresc 1068-1071, decresc 1071-1077). The horn is exposed over the fading chord.

Evidence (Horn 1 stem, 20 ms frames, c17; c16 is the same within 1-2 dB):
- At 1071 (note-on 1070.77, velocity 112) the level is -33.0 dB, then -42.9 at 1071.75 and -47.7 at 1072.75.
- At 1074 (velocity 106) it is -34.0 at 1073.5, then -43.1 at 1074.75.
- At 1077 (G sharp, tied for 20 qn, velocity 106) it is -32.9 at 1076.75, then -50.1 at 1077.75 and -51.3 at 1078.0, and back up to -39.5 at 1079.0. That is a 12 dB hole inside one held note, 0.75-1.25 qn after the arrival (c16: -49.4 at 1078.25).
- Excess at the join (same reading as finding 1): 1077 +12.4, 1071 +10.9, 1074 +7.8. Elsewhere Horn 1 reads 598 +12.6 and 442 +11.9. Horn 1's median excess rose from +4.2 (c16) to +6.7 (c17) with the Close-led mics, which hide less of the sag under room sound.
- CC1 moves only 71 to 67 across the tail and CC11 only 73 to 58, so the controllers do not cause it.

Fix (inferred, range-test the four notes):
1. Velocity 106-112 on the three slurred arrivals is the fastest transition (manual p.106: velocity sets transition speed). Set Horn 1 1071 / 1074 / 1077 to velocity 72 with `NOTE_VEL_AT` or the legato velocity span, and 1068's entry stays as it is. A slower slur is longer and overlaps the start of the new sustain. Movement II c57 #4 measured that legato velocity does not change the burst level, so check the sag on the stem and not only the onset.
2. If the hole at 1077.75-1078.25 remains: a CC1 lift of +6 to +8 units over 1077.3-1078.6. CC1 is Horn 1's dynamic crossfade (`CC1_DYN_TRACKS`), so it brings in a louder layer under the hole. Return it over 0.5 s. This is a controller shape on the instrument, not the track envelope.

Target: no fall over 6 dB inside 1071-1080 that the printed decrescendo does not explain (the decrescendo is about 3 dB by CC).

### 3. The eight second-idea joins are fixed, but their row-change eighths now start up to 107 ms early. Seven other joins are outside 60 ms (measured; per-join values inferred at slope 1)

The c17 lead cap (`PREV_MIN_SOUND_S`) worked:

| join | c16 S / lead (ms) | c17 S / lead (ms) |
|---|---|---|
| Violins I 146 / 374 | +150 / 94, +144 / 94 | +16 / 210, +25 / 215 |
| Violins II 146 / 374 / 840 | +136, +151, +128 | +10 / 220, +15 / 245, +26 / 174 |
| celli 842 / 144 | +140, +71 | +29 / 205, +40 / 114 |
| **Violins II 134** | +144 / 94 | **-90 / 230** (now early) |

The earlier refits also hold: celli 321 +24, 921 +7, 570 -1, 350 -3, 768 +7, 536 -32 (all were 33-55 ms off in c16). Totals: Violins I 12 of 98 joins outside 25 ms and 4 outside 60; Violins II 29 / 3; violas 18 / 2; celli 45 / 4.

Outside 60 ms on c17 (S / lead in ms):
- The eighths that open these figures: Violins II 133.5 -107 / 200 and 373.5 -99 / 245; Violins I 145.5 -67 / 235 and 373.5 -68 / 235. Their row-change lead is now larger than they need, and the cap of finding 1 of c16 no longer hides it.
- Celli 348 -127 / 210, 933 -69 / 180, 948 -70 / 155, 333 -60 / 210.
- Violas 594 -71 / 265 and 1056 +88 / 225.
- Violins I 597 +92 / 132 and 361.5 +62 / 80.

Fix: `build/lead_set.json`, new lead = old lead + S (slope 1, inferred). Only the eighths 133.5 / 145.5 / 373.5 sit on a row change, so their entries belong under the row-change lead; the rest are legato leads.

| track | qn: new lead (s) |
|---|---|
| Violins II | 134: 0.14; 133.5: 0.10; 373.5: 0.15 |
| Violins I | 145.5: 0.17; 373.5: 0.17; 597: 0.22; 361.5: 0.14 |
| Violoncellos | 348: 0.09; 933: 0.115 (the third value in three cycles: it reads -86 / +37 / -69, so take the midpoint of the last two leads, 0.18 and 0.155 = 0.17, if 0.115 swings late); 948: 0.09; 333: 0.15 |
| Violas | 594: 0.195; 1056: 0.31 |

Re-read S on these 14 after the render. Target: none outside 60 ms.

### 4. Wind and brass detached joins leave 50-90 ms of silence. The wind-and-brass sum dips 4.4 dB there, against 2.5 dB where the gap is 20 ms or less (measured)

Where: unslurred note changes with no printed rest, on notes of 0.4 s or more (`WIND_DETACH` gap_s 0.05 / frac 0.12 on winds, 0.09 / 0.18 on brass, in `build/score_config.py`). Median gap per track: Flute 2, Oboes and contrabassoon 65 ms; Clarinets and Bassoons 50; Horns 1 and 4, trombones and tuba 90.

Evidence:
- I took the 70 onsets where three or more wind and brass tracks change note with no rest. The dip of the wind-and-brass stem sum in beat - 0.15 to + 0.05 s against its surroundings (beat - 0.40 to - 0.20 and + 0.15 to + 0.35 s) has a median of 3.8 dB; the master's median is 2.6.
- Split by the joins' median gap: 50 ms or more (43 joins), wind and brass 4.4 dB and master 3.5; 20 ms or less (19 joins), 2.5 and 1.8.
- Worst joins: qn 402 (bar 135, 9.2 / master 8.2), 243 (bar 82, 7.4 / 7.4), 120 (bar 41, 7.3 / 6.6), 963 (bar 322, 7.1 / 6.6), 999 (bar 334, the coda build, 11 tracks, 7.7 / 4.5), 648 (bar 217, 9.1 / 5.5).
- Bars 41-42 are among the actor's 20 master bars more than 1.5 dB down against c16.
- Movement I c60 and finale c19 measured the same mechanism (2.4-5.3 dB master dips from 50-90 ms gaps).

Fix in `build/score_config.py` `WIND_DETACH`:
- Pitch-changing joins where both notes last 0.4 s or more: gap_s 0.0 with the old note ending 0.03 s after the new note-on. The sustain rows are polyphonic, so this needs a new key, e.g. "overlap_s": 0.03, in the `WIND_DETACH` block of `tools/score_to_parts.py`. Same values for brass, replacing gap 0.09.
- Same-pitch joins (173 of the 356 track-joins): gap_s 0.025, frac 0.08, so repeats stay separate (S1). Keep `REP_GAP_FLOOR_S` for short repeats; only notes of 0.4 s or more change.

Target: wind-and-brass dip median under 2.5 dB at these 70 joins, with the S1 separation of the theme head unchanged.

### 5. Accents: medians are inside the target. The outliers have three causes. Two Violins I accents on "Sus Marc LITE" bite (measured)

The accent shape is not over before the beat on led notes: on 57 led string accents the bump holds to a median of 85 ms or more after the beat, and only three end 100-122 ms before it (Violins I 315 / 927, celli 867), and those return to rest 256 ms after the beat. There are no printed brass accents. The 2-5 kHz share of the first 80 ms against the body is -3.0 to +2.2 dB on every accent I checked except two:
- **Violins I 51 and 771** (bars 18 and 258, the theme at mp leggiero, "Sus Marc LITE" at velocity 56 / 61): 2-5 kHz share +6.4 and +6.1 dB over the body, and +7.2 / +7.5 dB over the neighbours in the first 100 ms. The same figure on "Sus MAX" with the CC bump (327, 927) reads +0.9 / +1.1 dB and -3.0 dB of 2-5 kHz. 39 and 759 on the Marc row read +1.9 and +1.7 dB. This is bite, which Dan has asked to avoid.
  Fix: `ART_AT` Violins I 51.0 and 771.0 to "Sus MAX", taking the track's `ACCENT_CC` (3 / 12) like 327. The row is already loaded.
- **Flute 2 327** (bar 110, tutti): +8.2 dB over the neighbours in the first 100 ms (acc17's measure: +11.0). The accented A6 moves from "Stac DblTng" to "Sus MAX". There CC11 117 (bump +10 over 107) meets the "Sus MAX" f-layer region gain of +3 (c17 item 4). Fix: Flute 2 `ACCENT_CC` add_loud 10 to 3, or skip the bump on a note whose row changes, since the row change already carries the step.
- **The measure.** acc17's 0.35 s window counts a staccato eighth neighbour (0.11 s long) as a quiet note, so the theme's "staccato quarter, then accented half" figure reads high. Violins II 345 is +5.0 by acc17 but -1.6 dB in the first 100 ms; 819 +6.7 against +3.2; 123 +6.3 against +3.6. Of acc17's eight tracks with a 90th percentile over +3.5, most of the excess is this window. Compare the first 100 ms when a neighbour is shorter than 0.35 s.
  Real excess left by that measure: Clarinet 2 345 / 945 at +3.5 / +3.6 with no CC bump ("Leg Slur Rep" flat at CC11 104: row or sample level, so take 2 dB in that row's region volume for C5, pitch 72); Clarinet 1 999 +4.0; Bassoon 1 213 +5.0 (an ff arrival, which should be excluded as a new dynamic).

I could not run the matched comparison asked for (same track, pitch, row and resting CC11, outside hairpins and new dynamics). Of 51 eligible accents only 7 had two or more matching plain notes, because the scherzo's accents sit mostly inside hairpins or on the theme figure.

### 6. Pizzicato: the celli pp strokes of bars 89-98 are even now. Both sections' round-robin cycles put the weakest stroke on a fixed bar of the "ritmo di tre battute" groups (measured; audibility inferred)

- Celli at qn 264-291 (pp pizz., velocity 52): range 6.0 dB across the 10 strokes (c16 16.2 at velocity 41), so the c17 change worked. The cycle is -51.7 / -47.1 / -48.3 dB at 264 / 267 / 270, repeating every three bars. The first bar of each printed three-bar group (264, 273, 282, which are bars 89, 92, 95, where the head enters) is the weakest stroke, 4.5 dB under the next.
- Basses at velocity 41, same span: -50.7 / -49.5 / -52.9, so the third bar is the weakest (range 4.4 dB without the mp stroke at 294).

Fix: a CC36 round-robin reset (`rr_reset`) at 263.9 on both tracks so that the loudest sample falls on each group's first bar. Alternatively velocity +4 on 264 / 273 / 282 / 291 for the celli only; stay at 52-56, inside the layer above the 50 / 51 edge.

## Checked and fine (measured)

- S1, the repeated staccato eighths of the theme head. Dip before the second eighth: Violins I 5.2-6.7 dB in every statement; Flute 1 7.9-8.9; Oboe 1 8.0-10.8; Clarinet 1 9.7-9.8; cor anglais 6.8-7.1; trumpets 4.8-6.3; violas and celli in the coda 7.2 / 7.7.
- S2. Energy centroid of the first 110 ms of the off-beat staccato eighths: +24 to +40 ms after the beat on every section in bars 13-28, 105-120, 253-276, 305-320 and 329-336. Strings, winds, trumpets and timpani sit within 16 ms of each other.
- Tutti entries after rests of two quarters or more (10 chords of 8+ entries): spread median 95 ms. The contrabassoon and bassoons speak first (median -36 to -43 ms), tuba and Violins II last (+46 / +51). Small; no action.
- Last G sharp (bars 364-376): sum of Violins I and the solo copy -47 to -50 dB per second; detrended autocorrelation at 3.95 s 0.06 (c16 0.31, c15 0.19); standard deviation 1.8 dB. No loop pulse. Horn 1's last note is -44 to -51 dB per second (c16 -44 to -53).
- Brass legato: no join over an octave and no chord on a monophonic row (p.105).

**Do not touch:** the eight second-idea leads and the celli refits of c17 (except the 14 joins in finding 3); the string Stac / Staccatissimo / Spiccato rows and lengths of the theme head (S1 and S2 above); the trumpets' "StacSs DblTng" repeats; the celli pp pizzicato at velocity 52; the last G sharp's doubled re-bows (no pulse); the accent shape keyed from the moved note-on with the 0.08 s hold on led notes; `VOL_CLASSES = ("slow",)`.

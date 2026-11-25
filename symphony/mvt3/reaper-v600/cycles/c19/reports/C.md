# Critic C, cycle 19 (tempo, timing and transitions), on the c18 render

Data: `cycles/c18/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `build/parts.json` (the data of the c18 render: tempo map, notes with score onset `sq` and moved onset `qn`, keyswitches, CC lanes), `build/mockup.midi` (the printed tempo steps), `build/score_config.py`, and the actor's S file `cycles/c18/logs/render/S_c18.json` (1,817 notes on the 29 thematic lines plus 18 extra lines).

My own measures, all on the stems (scratch scripts deleted):
- **Half-rise.** 2 ms hop, 16 ms RMS envelope (24-30 ms on the bass instruments); floor = the minimum in the 80 ms before the moved note-on; the time, against the score onset, at which the amplitude is halfway from the floor to its maximum in the first 0.25 s. It is used only on notes that start after a gap; "true entries" start after 0.15 s or more of silence on the track (1,358 notes). The timpani reads +19 ms with SD 1 ms on 101 strokes (`TIMP_DELAY_S` 0.02 plus an instant attack), which gives the detector's own error.
- **Fold.** A band envelope folded at the quarter-note period over a span of constant tempo. It gives the mean stroke profile of a repeated figure and does not depend on timing single strokes.
- **Bar-line profile.** 30 ms frames around each chorale bar line, per stem and on the master.

I cannot hear. "Audible" is inferred from the numbers unless a line says measured.

## Manual notes

MANUAL-READING has no fixed row for c19 (third round). I read p.100-112 of the May 2021 HO manual in full (Hollywood Brass and Orchestral Woodwinds: Long, Short, Effects, Legato, Mutes, Keyswitch) and p.93-94 (string short types), because this lens's top open problems are wind and brass whole-note changes and the basses' short row. `loop/MANUAL-GAPS.md` read; item 2 (re-tongue rows) is still open and applies to finding 2.

| Manual (PDF page) | What it says | Where it applies here | Does the c18 render follow it? |
|---|---|---|---|
| p.101, p.109 Sustain (brass, woodwinds) | Sustain patches play as long as the note is held; all dynamic layers start together and the Mod Wheel (brass, clarinets) fades between them. Nothing limits them to one voice. | The chorale's whole notes, bars 224-234 (qn 892-936), 21 wind and brass tracks on "Sus MAX" / "Sus Non Vib (MAX)". | Not used. Every change of pitch is written with a 45-90 ms silence before the new note, though the old and the new pitch could overlap on these rows (finding 2). Measured. |
| p.105, p.112 Legato (brass, woodwinds) | A slur is played only when there is "no significant gap" between the two notes and they are at most an octave apart; legato instruments are monophonic. | The same whole-note changes, if a connected change is wanted without an overlap. | Not used in the chorale (all 21 tracks stay on sustain rows). Second choice after the overlap. Read only. |
| p.101, p.109-110 Legato Repetitions; p.106 Legato Slur Repetitions | A re-tongued sample for repeated notes inside a legato phrase; in the woodwinds a sustained non-vibrato note plus a short note as the re-tongued attack, round robin x4. | The same-pitch whole notes across the chorale's bar lines (0-6 tracks per bar line: Horn 2, Trombone 1, Bass trombone, Tuba, Oboe 1, Clarinet 2 at 924-932). | Not loaded (MANUAL-GAPS item 2, still open). These are the notes that cannot overlap, so they are the right place for the first test of that row. Read only. |
| p.102, p.110 note under Short (brass, woodwinds) | Short articulations have no release trails; the room sound is at the end of the main sample, so the MIDI notes must be held long enough ("play the MIDI notes in a connected fashion") for that end to be heard. | The same principle on the basses' "Stac On Bow RRx9" eighths (792-840, 984-1108), written 0.225 qn long (80 ms at 168). | Not followed. The note-off comes 30-35 ms before the stroke's own peak (finding 3). Measured. |
| p.94 Staccato On Bow | The bow does not lift at the end of the note but "comes to a full stop"; round robin of 9-16. | Double basses, 320 notes on this row. | The row is the right one for hammered eighths. The stop of the bow is at the end of the sample, which the 80 ms note cuts off (finding 3). Inferred. |
| p.94 Repetitions (strings), p.103 (brass) | A dozen repeats in one sample with real bow changes; tempo-synced, recorded at 170, 145 and 120 bpm; best within about 10 bpm of the recorded tempo; has release trails. | Basses' eighths at 168-184 (bars 199-210) and 176 (bars 247-270): the 170 row fits both. | Not used. It is the fallback if the range test of finding 3 fails. Read only. |
| p.106 Legato Slur, velocity | Velocity sets the speed of the legato transition (harder = faster). | Horn 1, Trumpet 1 and the violins' legato joins, all at velocity 110 or more in c18. | Followed. The legato joins of the 29 lines are centred (medians -12 to +19 ms); what remains is spread (robust SD 24-33 ms), not an offset. Measured. |

## State through this lens (measured)

- **Tempo map.** Unchanged since c15. Every printed tempo word is realised: the render's 423.76 s against 423.11 s printed; every section within 0.2 s of its printed length. 23 of 558 half-note beats differ 3 % or more from the printed step (phrase-arc end beats -3.5 to -8.6 %, the caesuras -3.4 to -4.7 %, the smoothed first beat of three ramps +3.6 to +7.9 %). 126 of 558 beats (23 %) carry a tempo change, which meets the research default of about 20 % (FINDINGS Part 5).
- **Thematic lines (S, the actor's file).** 661 / 177 of 1,817 outside 25 / 60 ms. By class the medians are centred: string "Sus MAX" joins 0 to +3 ms (n 692), string legato joins -4 to -12, Horn 1 legato +10, Trumpet 1 -1. No lead bucket with 10 or more notes is off by more than 30 ms. The remaining error on these lines is spread, so more per-note lead fitting there will not pay.
- **Tracks outside the S table.** Second winds, bassoons, Horns 2-4, Trombone 2 and the tuba have never been in it. Their entries carry fixed offsets of 25-125 ms (finding 1).
- **Keyswitches.** 2,313; median 13.4 ms before the note-on, 5th percentile 10.2, 242 under one audio block (10.7 ms), 10 under 8 ms, 493 at 100 ms or more. Unchanged since c15; no new evidence either way.
- **Final chord.** Unchanged and correct as printed (the fermata is on the rest). Stop 15.1 dB at +0.3 s.

## Findings

### 1. Tutti entries are spread over 150 ms because six tracks always speak first (measured; the gain is inferred from the class medians)

**Where:** every tutti downbeat. Oboe 2, Flute 2, Trombones 1-2, Bassoons 1-2, Contrabassoon, and Horns 3-4 on their long-lead entries.

**What:** at chords where 8 or more wind, brass and string tracks enter after a rest (37 chords), the first and the last half-rise are a median 148 ms apart (10th to 90th percentile 78 ms), and 65 % of these chords span more than 100 ms. The research default for an orchestral tutti entry is 36-55 ms first to last (FINDINGS section 12). The early tracks are the same at each downbeat:

| chord (qn, bar) | earliest four (ms against the beat) | latest |
|---|---|---|
| 16 (bar 5) | Oboe 2 -68, Flute 2 -56, Trombone 2 -52, Trombone 1 -50 | Tuba +41 |
| 436 (bar 110) | Oboe 2 -126, Flute 2 -72, Trombone 2 -50, Trombone 1 -40 | Trumpet 1 +32 |
| 600 (bar 151) | Flute 2 -65, Clarinet 2 -53, Clarinet 1 -51, Bassoon 1 -49 | Trombone 1 +57 |
| 792 (bar 199) | Oboe 2 -109, Flute 2 -73, Trombone 2 -49, Bassoon 1 -47 | Horn 4 +51 |
| 1108 (bar 278) | Oboe 2 -127, Flute 2 -77, Trombone 2 -53, Bassoon 1 -49 | Tuba +26 |

At qn 792 the Oboe 2 stem is within 5 dB of its body from 120 ms before the beat (-45 dBFS at -120 ms, body -40), and Flute 2 from 80 ms before it; Oboe 1 and Flute 1 beside them reach their bodies in the 20 ms before the beat. The timpani sit at +19 ms. So the chord starts with a second oboe and flute, then the trombones and bassoons, then the rest, then the timpani.

**Evidence by class** (true entries; realised lead; median, robust SD, n):

| track, row | lead now | half-rise | change |
|---|---|---|---|
| Oboe 2 "Sus MAX" | 0.15 s | -68 (SD 39, n 12) | -0.08 |
| Oboe 2 "Sus MAX" (re-tongue lead) | 0.12 | -96 (SD 5, n 5) | -0.08 |
| Flute 2 "Sus MAX" | 0.10 | -64 (SD 12, n 16; 14 outside 40 ms) | -0.06 |
| Bassoon 1 "Sus MAX" | 0.06 | -44 (SD 12, n 24) | -0.04 |
| Bassoon 2 "Sus MAX" | 0.05 | -34 (SD 4, n 36) | -0.03 |
| Contrabassoon "Sus MAX" | 0.04 | -26 (SD 7, n 25) | -0.025 |
| Bassoon 1 "Stac DblTng RRx9" | 0.03 | -17 (SD 4, n 37) | -0.015 |
| Trombone 1 "Sus MAX" | 0.09 | -40 (SD 4, n 13) | -0.04 |
| Trombone 2 "Sus MAX" | 0.09 | -49 (SD 5, n 14) | -0.045 |
| Horn 3 / Horn 4 "Sus MAX" | 0.10 | -59 (SD 5, n 8) / -49 (SD 15, n 8) | -0.05 |
| Horn 2 "Sus MAX" | 0.09 | -33 (SD 21, n 8) | -0.03 |
| Clarinet 1 "Leg Slur" entries | 0.06 | -42 (SD 15, n 9) | -0.035 |
| Tuba "Sus MAX" | 0.05 | +25 (SD 20, n 26) | +0.02 |
| Cor anglais "Sus MAX" | 0 | +35 (SD 8, n 7) | +0.03 |
| Violas "Stac RRx9" | 0.04 | +33 (SD 8, n 16) | +0.03 |

Classes that need nothing (within 20 ms): Flute 1, Oboe 1 and Clarinets 1-2 on their sustain rows (0 to +7), Bass trombone -9, Trumpets 1-2 (-3 to +8), Horn 3 on the 0.05 s lead (0), every "Stac DblTng RRx9" class of the trumpets and upper winds (-12 to +16), harp +7. The strings' "Sus MAX" entries after rests read +38 to +47 with SD 40-63 ms (Violins I, Violins II, Violas, lead 0.06): they depend on the dynamic, as c15 found, and one class value will not fix them.

**Why it was missed:** the leads of Oboe 2 and Flute 2 date from c04 (`ENTRY_LEAD_S` "Oboe 2" (0.0, 0.11, 0.0), "Flute 2" (0.0, 0.06, 0.0), set at 0.6 x a residual measured with the old estimator), and no later S table contains these tracks.

**Fix (`build/score_config.py`):**
- `ENTRY_LEAD_S`: "Oboe 2" (0.0, 0.11, 0.0) -> (0.0, 0.03, 0.0); "Flute 2" (0.0, 0.06, 0.0) -> (0.0, 0.0, 0.0); "Bassoon 2" (0.05, 0.05) -> (0.02, 0.02); "Contrabassoon" (0.04, 0.04) -> (0.015, 0.015); "Trombone 1" and "Trombone 2" (0.06, 0.09, 0.05) -> (0.06, 0.045, 0.05); "Bassoon 1" the value that gives the realised 0.06 s -> 0.02; "Horn 2" loud value 0.06 -> 0.03; Horns 3 / 4: the eight entries each that realise 0.10 s -> 0.05 (print them with `LEAD_WARN_S`; I could not tell from the config which rule gives them 0.10).
- `RETONGUE_LEAD_S`: "Oboe 2" 0.12 -> 0.04; "Flute 2" 0.07 -> 0.03.
- `ENTRY_LEAD_ART_S`: a "Clarinet 1" entry with "Leg Slur" 0.055 -> 0.02; "Cor anglais" with "Sus MAX" 0.03.
- Tuba: entry lead +0.02 (0.05 -> 0.07); Violas `STAC_LEAD_S` +0.03.
- Add Flute 2, Oboe 2, Bassoon 2, Trombone 2, Horn 3 and Tuba to the measured lines (the half-rise on true entries is enough; S is not needed for notes after a rest), so these classes are watched.
- These are sustain-row entries, the class that did not move between two renders (c15), so one pass should hold. The woodwind accent bump and the dal niente shapes are keyed to the moved note-on and move with the lead.

**Target:** each class median within 15 ms of +5; true entries outside 40 ms from 362 of 1,358 (27 %) to under 15 %; first-to-last spread at the chords above under 100 ms (the class medians alone predict a median of 113 ms from 148; the rest is the strings' dynamic-dependent entries and the legato-row entries).

### 2. Chorale bar lines: the dip is before the bar line, where 15-20 wind and brass players are silent in the same 100 ms; after it the low strings start 0.2-0.45 s late (measured; fix inferred)

**Where:** bars 224-234, qn 896-932, every wind and brass track; Violoncellos 900-912; Double basses 896-904 and 920; Violins II 900.

**What, before the bar line.** On the master the lowest 30 ms frame at the ten bar lines is 2.4-5.3 dB under the level before, and it lies at -10 to -90 ms (median -60 ms): at -70 ms at 916, -60 at 912, 920 and 928, -40 at 908. The master is back within 1 dB at 0 to +50 ms at seven of the ten. So the hole is the gap before the new notes, not their slow start. Per stem: every wind and brass whole note ends 45-90 ms before the next note-on (c18's per-player breaths, 0.035-0.085 s), the new notes start 35-90 ms before the bar line, and so all the silences fall between -140 and -20 ms. Stem dips in that window: flutes 7-16 dB, oboes 5-13, clarinets 6-15, horns 2-9, trumpets 6-10, trombones 5-11, tuba 5-9. Spreading the breaths by 50 ms could not move them out of a window 100 ms wide. The dry stems make it worse: after the stop of bar 204 the upper woodwinds are 25-31 dB down after 0.2 s, the trumpets 37-49 dB, the strings 17-22, the horns 8-14 (this answers the coordinator's note on woodwind release: it applies here, and the trumpets fall faster still).

**What, after the bar line.** Most wind and brass stems are within 3 dB of their new level between -40 and +50 ms, so their leads are right. Slow ones: Trombone 1 +110 to +150 ms at 896, 900, 920, 924 (lead 0.05), Oboe 1 +150 at 920 and 924, Horn 1 +120 at 904. The low strings are late:
- Violoncellos "Leg BC MAX" at 904, 908, 912 (lead 0.157 s, velocity 118): 6-10 dB under the level before from -30 to +150 ms, back within 3 dB at +190, +300, +310 ms.
- Double basses "Sus MAX" at 900, 904, 920 (lead 0.07-0.10 s, no overlap): 8-9 dB down, back at +220, +450, +420 ms.
- Violins II at 900 (bar 226): the G5 after the tremolo is on "Leg Slur MAX" with no lead and no overlap and is the pitch the tremolo held. The stem falls from -44 to -76 dBFS at +150 ms and is still at -53 at +570 ms: a hole of 12 dB or more for 370 ms at the start of the violins' line. Violins I (same note, coming from another pitch) lose 6 dB at most.

**Fix (instrument side; `INSTR_POST` in `build/score_config.py`, block "mvt3 c18" ruling 4):**
1. Changes of pitch (8-11 of the tracks at each bar line): no gap. The old note ends 0.03 s after the new note's moved note-on, on the same track and row (sustain rows are polyphonic; p.101 / p.109). In `gap_set` terms: `gap_s` -0.03 for a whole note followed by another pitch; if the tool takes no negative gap, add an `overlap_s` key beside it. The old note's release then covers the new note's rise.
2. Same pitch across the bar line (896: Bassoon 1, Horns 1-3, Bass trombone, Tuba; 908: Flute 2, Oboe 2, Horns 1, 3, 4, Trumpet 2; 920-932: Horn 2, Trombone 1, Bass trombone, Tuba, Oboe 1, Clarinet 2, Flute 2 / Oboe 2 at 920): these cannot overlap. Gap 0.035 s, in two groups so they do not coincide: Tuba, Bass trombone, Horn 2 end 0.11 s before the bar line and start 0.075 s before it; Trombone 1, Oboe 1, Clarinet 2 end 0.045 s before it and start 0.01 s before it. A CC11 / CC1 lift of 8 % from the note-on, held 0.30 s, back over 0.55 s, no fall before it. If one more row can be loaded, test "LegRep RRx4" on Tuba and Trombone 1 for these six notes (MANUAL-GAPS item 2; p.101).
3. Leads of the slow starters: Trombone 1 whole notes 892-932 0.05 -> 0.12 s; Oboe 1 0.07 -> 0.12 at 920 and 924; Horn 1 at 904 0.09 -> 0.15.
4. Violoncellos 900-912: `ART_SPANS` "Sus MAX" over (899.5, 916.0) in place of "Leg BC MAX", each note starting 0.15 s before the bar line and the old note held 0.10 s past the new note-on (different pitches, so the overlap is allowed). Double basses 896-908 and 920, 928: lead 0.15 s with the same 0.10 s overlap at 900, 904, 908 (different pitches); 920 and 928 are the pedal's same-pitch bow changes and stay with the c18 join.
5. Violins II 900: `ART_SPANS` {"from": 899.9, "to": 900.1, "art": "Sus MAX"} with a 0.07 s entry lead, the tremolo ending 0.03 s before it (the c14 fix of Violins I at 884). Check Violins II 904 onwards for the join out of that note.
6. Range test 838:940 as in c18. **Targets:** master lowest 30 ms frame at 896-932 within 2 dB of the level before at eight of ten bar lines; no wind or brass stem dip over 4 dB at a change of pitch; celli and basses within 3 dB of their level by +80 ms; Violins II at 900 no frame more than 6 dB under its level.

No per-note fader move is needed for any of this.

### 3. The basses' hammered eighths sound as one late pulse per quarter (measured)

**Where:** Double basses, "Stac On Bow RRx9", bars 199-210 (qn 792-840), 247-272 (984-1088), 273-277 (1088-1108): 320 notes.

**Evidence** (stem folded at the quarter period; 150-3000 Hz band, 10 ms window):

| span | on-beat stroke: rise, peak position | off-beat stroke | 40-150 Hz band, whole cycle |
|---|---|---|---|
| 792-816 | 5.2 dB, peak +74 ms | 2 dB at about +70 ms after its place | 2.4 dB |
| 984-1016 | 5.1 dB, +73 ms | no bump (0.1 dB) | 3.3 dB |
| 1016-1056 | 2.8 dB, +93 ms | 0.5 dB | 2.6 dB |
| 1056-1080 | 6.7 dB, +78 ms | 0.9 dB | 4.9 dB |
| 1088-1107 | 8.9 dB, +74 ms | 5.1 dB at +77 ms | 5.6 dB |

The timpani on the same grid: 6-12 dB, half-rise +23 to +24, peak +33 to +39 ms. So in the two fast sections the basses give a quarter-note swell of 3-5 dB that peaks 35-40 ms after the timpani's, and the off-beat eighth is all but missing; only the Largamente (eighth = 208 ms) shows two strokes. In the master's 40-150 Hz band the eighth-note figure does not exist (off-beat 0-1.3 dB in every span). This is S1 for the figure that carries the pulse of both codas.

Cause (measured on the data): each note is 0.225 qn long, 80 ms at 168 bpm, and starts 35-40 ms before the beat, so the note-off is 40-45 ms after the beat while the stroke's own peak comes at +74 ms, about 110 ms after the note-on. The note is released before the sample has spoken, and its end (the bow stopping on the string, p.94) is not played. The off-beat strokes also carry velocity 81-86 against 95-102 and the c17 CC11 beat weight, which takes the little they have. This also explains the two disagreeing detectors of c17: there is no clean stroke edge to time. c16's "separation 9.8-11.7 dB" may have been read with a window shorter than one period of C2 (15 ms); with a 6 ms window I see 3-4 dB of ripple on a held note.

**Fix (`build/score_config.py`; range test 790:820 and 982:1000 first):**
1. Length: the short row's 45 % of the slot -> 70 % (0.35 qn; 125 ms at 168, 119 ms at 176), so the note-off falls after the peak. The expert range for string shorts is 50-62 % of the slot (FINDINGS section 20), but those are spiccato rows, which speak faster.
2. Lead: 0.04 -> 0.075 s on every stroke of 792-840 and 984-1088 (peak from +74 to about +40, with the timpani); 1088-1108 the same.
3. Off-beat strokes: velocity to within 8 steps of the on-beat ones (88-94) and the CC11 beat weight halved.
4. If the off-beat bump stays under 3 dB: test "Repetitions TS" (p.94; recorded at 170 bpm, the tempo of both sections) on 792-816 with one note per bar; it costs one row on one track.
5. Measure with the fold, not with single-stroke onsets. **Targets:** on-beat and off-beat bumps both 4 dB or more in the 150-3000 Hz band at 792-816 and 984-1016, their peaks within 15 ms of each other and at +30 to +50 ms; the master's 40-150 Hz band with an off-beat bump of 1.5 dB or more.

This also settles whether the row volume knob acted (coordinator's question): compare the on-beat peak level in the same band (c18: -40.1 dBFS at 792-816, -40.2 at 984-1016) after moving the -1.5 dB to region volumes.

### 4. Two long string notes start from silence (measured)

- **Violoncellos, bar 142 (qn 564, pp, the B2 of 5.3 quarters on "Leg Slur MAX" after three "Stac RRx9" quarters, lead 0.196 s):** the stem is at -71 to -80 dBFS from the bar line to +200 ms and reaches -55 only at +650 ms; the note's level is about -50. The note is half a second late. This is the known class (a legato-row note entered from another row plays its slow first-note layer). Fix: `ART_SPANS["Violoncellos"]` {"from": 563.9, "to": 569.4, "art": "Sus MAX"}, entry lead 0.12 s. Target: within 6 dB of its level by +100 ms.
- **Violins II, bar 226 (qn 900):** finding 2, item 5.
- Candidates from the same scan (12 dB or more under the level before for 160 ms or more after a note start; check against the printed dynamics before acting): Double basses 856 (bar 215, 270 ms), 148 (bar 38, 210 ms), 964 (bar 242, 180 ms), 504 (bar 127, 390 ms); Violoncellos 302 (bar 76, 170 ms). Bars 149 and 224 are printed drops and are excluded.

### 5. Bar 204: the celli and basses leave 75-200 ms before the tutti, and the stop is 2 dB too dry (measured; values inferred)

**Where:** the cut-off at qn 814. **Evidence:** master 18.1-19.2 dB down at +0.3 s (limit 17; c17 17.4). At the common note end the basses' stem is already 18 dB under its level and the celli's 13 dB (the c17 early end of 0.075 s with a CC11 fall that starts 0.215 s before the stop), while most other stems are within 5 dB of theirs (flutes, oboes, clarinets, horns, trombones and violins 0-3 dB; trumpets 3-4; violas 7). 100 ms later the basses are at -32 dB. So the bass leaves the chord first, and the 30-150 Hz content that would carry the tail is gone before the stop. The trumpets fall 48 dB in 0.2 s and the upper woodwinds 25-31 dB, so nothing else fills it.
**Fix (`INSTR_POST` "note_end" and "cc_shape" at 814.0):** `early_s` 0.075 -> 0.03 on both tracks; the CC11 shape [(-0.215, 0), (-0.075, -24), (0.44, -24), (0.50, 0)] -> [(-0.10, 0), (-0.03, -12), (0.44, -12), (0.50, 0)]. Do not touch the returns. **Target:** 15-17 dB at +0.3 s; basses and celli within 6 dB of their level at the common note end. If the celli's open G2 hangs over again (c17's reason for the early end), keep the celli's fall at -18 and change only the basses.

### 6. Tempo: keep the map; give the arrival at bar 223 a broadened last beat (map measured, benefit inferred)

Every printed word is realised and the Allegro sections carry no unprinted change beyond the caesuras. One place works against the score's intent. The allargando of bars 221-222 runs 134, 121, 115, 112 quarter-note bpm per half-note beat: it reaches the Maestoso tempo (112) one beat early and holds it, and the first beat of bar 223 is then 113 (the +1.5 % push of the arc (888, 912)). The largest arrival of the movement (trumpet B to C, crash cymbals fff, bass drum) therefore comes in strict time, slightly faster than the beat before it. `CAESURA` has entries at 72, 104, 392, 632, 664, 816 and 1108 and none here. The printed allargando and the rule on rubato inside a printed rit. support a broadening that lasts to the bar line.
**Fix (`build/score_config.py`):** the ramp of (880, 888) to end at 104 bpm on the last half-note beat (886-888: 108, then 104 over the last quarter) with the Maestoso at 112 from 888; `CAESURA[888.0] = 0.05`; remove the +1.5 % push from the first two beats of the arc (888, 912). The two bars lengthen by about 0.12 s. Then `--midi-only --tempo` on all tracks, and compare re-bow fill keys with the built positions (LEARNINGS c12). Everything else in the map stays.

## Answers to the coordinator's items that touch this lens

- **Accent bump timing (0.03 s before the moved note-on, held 0.06 s, back by 0.22 s).** The shape is keyed to the moved note-on. On notes with a lead of 0.15 s or more (string legato leads are 0.12-0.29 s, Oboe 2's entries 0.15 s) it is back at rest 70 ms or less after the beat, and on leads over 0.22 s it has ended before the beat. Movement II c57 item 3 applies: key the bump to max(moved note-on, score onset - 0.05 s). Inferred from the data; I did not measure accent levels (lens A / B).
- **Chorale rise times:** finding 2. The dip is before the bar line; a CC11 lift after the note-on cannot fill it.
- **Upper-woodwind release:** measured at the stop of bar 204: flutes, oboes and clarinets 25-31 dB down 0.2 s after the note end, trumpets 37-49, strings 17-22, horns 8-14, trombones 17-20. It is the reason a 45-85 ms breath makes a 5-16 dB hole on a wind stem.
- **Basses' short rows, calibration plan:** use the fold of finding 3 on two range spans (790:820, 982:1000) with three variants: length 45 / 70 %, lead 0.04 / 0.075 s, off-beat velocity -15 / -6. Measure the on-beat and off-beat bump height and peak time in 150-3000 Hz and 40-150 Hz.
- **Re-tongue rows for the eighths of bars 91-92 and 277:** not measured this cycle. The first use I would make of a re-tongue row is the chorale's same-pitch whole notes (finding 2, item 2).
- **Keyswitch 0.15 s ahead (Scherzo c16):** no new evidence here; the first theme already has it (`KS_LEAD_SPANS`), and c15 measured the second theme's joins 36-45 ms later with it. Leave.
- **Not measured (other lenses):** accent levels per family, the fader-guard side effects, pizzicato, the muted trumpet at bar 182, Horn 3 in bars 27-34, the CC11 curve of "Sus MAX" above 100, horn L/R phase (critic B).

**Do not touch:** the printed ramps and section tempos, the caesuras at 104, 392, 664, 816, 1108 and the arcs of bars 51-82 and 171-198; the leads of the 29 thematic lines (`leg_leads.json`, `steady_leads.json`, the Horn 1 and Trumpet 1 pair tables: every class median is within 20 ms); the one-row theme spans and the first-theme `KS_LEAD_SPANS`; the entry leads of Flute 1, Oboe 1, Clarinets 1-2, Bass trombone, Trumpets 1-2 and every "Stac DblTng RRx9" class (within 20 ms); `TIMP_DELAY_S` 0.02 and percussion on the grid (timpani +19 ms, SD 1); the stops of bars 2, 6, 94, 113, 166 and the final chord with `FINAL_RING` (15.0-15.8 dB); the returns and sends; the sfp front of bar 149; the pedal's two-bar notes and their joins at 916-932; the pre-roll and section CC16 resets; no per-note move in the track envelope.

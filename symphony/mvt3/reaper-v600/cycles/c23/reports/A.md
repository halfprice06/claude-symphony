# Cycle 23, critic A: articulation and phrasing (on the c22 render)

Sources: the c22 stems and master (`cycles/c22/render/`), the c21 stems for comparison, `build/parts.json` (the c22 data), `cycles/c22/before/parts.json` (the c21 data), `build/score_config.py`, `build/mockup-events.tsv`, `build/sections/codaOne.ily`, and the installed `.oib` patch files, which I decoded read-only (Flute, Flute 2, Oboe, English Horn, Clarinet, Bassoon, Solo French Horn, Solo Trombone and Solo Trumpet KS Masters).

"Measured" means a number taken from these files. "Inferred" means a conclusion that a render has to confirm. Nobody heard the audio. Every fix below acts on the instrument: CC11 / CC1, velocity, note lengths, rows, or Opus script and state settings. None of them moves the track volume envelope per note.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 23, so I skipped the fixed reading. I read the pages behind my findings, plus `loop/MANUAL-GAPS.md` (#2 re-tongue rows, #5 expressive rows, the c22 entries).

| Manual (May 2021 HO, PDF page) / patch file | Where it applies | Does the render follow it |
|---|---|---|
| p.112: woodwind Legato Slur joins only with no gap and within an octave; p.144: velocity sets the transition timing, not the loudness | Wind legato targets (finding 3) | Followed. Velocity cannot fix the holes: c22's velocity floor changed nothing. |
| Patch files: woodwind "Leg Slur MAX". The TLeg transition groups have A54 / H264 / D177 to 0 (oboe), H412 (cor anglais), A72 / H300 / D237 to 0 (Flute 2), A92 / H512 to 0 (bassoon), and S 1.0, never faded, on Flute 1. The connected sustains "OBs" / "EHs" / "Fl2s" / "1Fls" / "Cls" / "Bss" fade in over 440 / 465 / 525 / 738 / 553 / 438 ms. They play the sustain sample from its own start, the same `startSample` as the detached first-note groups (Flute 096: 6996, loop from 62752). A "LegatoSpeed" script releases the old voice after RELEASE 210-254 ms and has an `SSOFFSET` parameter (1956 on oboe and clarinet, 0 on the others). Its `SUS_GROUP_SUBSTRING` is "Obs" on the oboe and "CLs" on the clarinet, but the groups are named "OBs" and "Cls". | Finding 3 | Shipped values, untouched. The substring case mismatch on oboe and clarinet is new. Nobody has tried `SSOFFSET`. |
| "Leg Slur Exp" row (MANUAL-GAPS #5) | Finding 3 | Not a fix: it has the same TLeg groups and the same sustain fade-in times (patch) |
| p.101 and p.109-110: Legato Repetitions plays "a sustained non-vibrato note and a short note to act as the retongued attack", RRx4. Patch: 1FH "LegRep RRx4" = RR attack groups A55 / D1000 to 0, plus sustain groups A190-237. Every brass sustain group's CC1 / CC11 `MidiController` has `fadeTime` 120 ms | The chorale's repeated whole notes (finding 1) | Not used (MANUAL-GAPS #2 still untried). The 120 ms controller fade confirms the c22 note: a CC11 fall of about 0.1 s is smoothed away |
| Solo Trumpet "Stac DblTng RRx9" (patch): velocity layers 1-54 / 55-75 / 76-94 / 95-127; Velocity->Volume intensity 0.6 inside a layer | Trumpet off-beats 159-166 (finding 2) | The c22 change crossed a layer boundary (finding 2) |
| p.101: brass sustains take their dynamic from CC1, and CC11 is the Global Group volume (patch) | Trumpet 3 accents (finding 4) | Followed: the accent is a CC11 volume bump with no layer change, so it adds weight without bite |

## Findings, ranked by what a listener would gain

### 1. The chorale's repeated brass whole notes (bars 224-234) still do not re-tongue. The 0.025 s gap is the cause, not the CC11 fall (measured; fix values from measured data)

Where: qn 894-936.
- Horn 1 at 896 / 900 / 908.
- Horns 3-4 at 896-908.
- Trombone 1 and Bass trombone at 920 / 924 / 928 (and 896).
- Tuba, and Oboe 1 at 924-932.
- Tracks 13-15, 19, 21, 22 and 3.

Evidence. I measured each repeat's dip on the c22 stems (150-6000 Hz, 20 ms windows): the new note's peak in its first 0.12 s minus the floor from 0.15 s before to 0.03 s after the moved note-on.

| | dips (dB) |
|---|---|
| Horn 1 | 1.0 / 0.5 / 3.0 |
| Trombone 1 | 1.5 / 1.5 / 1.4 / 1.3 |
| Bass trombone | 3.1 / 2.1 / 1.3 / 1.3 / 1.0 |
| Horn 4 | 0.5 / 3.0 |
| Oboe 1 | 2.3 / 1.6 / 0.8 |

Across every held brass same-pitch repeat in the c22 render (all four horns, the trombones, bass trombone, tuba and trumpets; staccato and marcato rows excluded), the dip follows the gap:

| gap before the new note-on | n | median dip | under 3 dB |
|---|---|---|---|
| under 0.04 s (the chorale's 0.025 s) | 27 | 3.0 dB | 13 |
| 0.08-0.12 s | 67 | 6.7 dB | 7 |
| 0.12-0.20 s | 100 | 9.4 dB | 7 |

Inside the 0.025 s group, the notes that c19 leads by 0.11-0.20 s are the worst (Horn 1, Trombone 1, Bass trombone: median 1.4 dB, n 12). Notes led by 0.04-0.10 s do better (Horn 2: 5.5-5.9 dB at 920-928; Tuba: 3.6-4.8).

The c22 CC11 fall (18 units) cannot help:
- Every brass CC controller fades over 120 ms (patch), so a fall of about 0.1 s is smoothed.
- The lane rises back while the old note is still sounding. On Trombone 1 at 924, the lane is at 70 at 923.53 and back at 88 at 923.71, but the old note ends at 923.673, so the old note swells back up before it stops.
- With a 237 ms release, the 25 ms gap is filled.

Fix (`build/score_config.py`, the c19 chorale block near line 1736):
- On the `"pitch": "same"` `gap_set` row (`gap_s` 0.025) and on the `onset_lead` row's `"gap_s": 0.025`, use 0.12 s for Horns 1-4, Trombones 1-2, Bass trombone and Tuba, and 0.08 s for Oboe 1-2 and Clarinets 1-2. The wind repeat median from the research batch is 63 ms. At Maestoso 2 = 56 (112 qn/min), 0.12 s is 0.224 qn.
- Keep the pitch-change overlaps (`"pitch": "diff"`) and the printed-breath rows.
- Remove the c22 `move_fall` / `fall_cc` 18 on those rows (it does nothing measurable). Use no CC11 fall at all on these whole notes.
- Expected (from the table, measured relation): median 6.5-9 dB.
- Alternative, if the gap test reopens master holes: put the same-pitch repeats on "LegRep RRx4" (the recorded re-tongue). It is one more row on Horns 1-4 and on Trombone 1 / Bass trombone ("LegRep RRx4" is in the 1TB KS Master), so check memory first.
- Pass: every listed repeat 6 dB or more. In the master's 60-500 Hz band, no bar-line hole over 6 dB at 896 and 920-932 (c22: 0.7-3.3 dB; c18's fault was 4-12 dB). At 896, 6 brass and 3 wind tracks repeat together, so check that bar first.

### 2. Trumpets 1-2's mf off-beats (bars 159-166) fell into the next velocity layer down. +7 is the right add; +6 or less repeats the fault (measured)

Where: Trumpets 1-2, "Stac DblTng RRx9", the staccato off-beats at qn 633-661 (printed mf, staccato).

Evidence:
- c21 played them at velocity 96 (+8), c22 at 92 (+4). CC11 (park 100) and CC1 (85) are identical in both.
- The row's velocity layers are 1-54 / 55-75 / 76-94 / 95-127 (patch). So 96 -> 92 crossed from the top layer into the 76-94 layer.
- Note peaks, c21 -> c22, on the same 15 notes: Trumpet 1 -5.0 to -13.0 dB (median -7.3), Trumpet 2 -5.1 to -10.4 (median -6.6).
- Inside one layer, Velocity->Volume has intensity 0.6, so a few steps cost only a fraction of a dB (inferred from the table).
- This is a layer step, not a slope of about 1.6 dB per velocity step. A linear fit between +4 and +8 would mislead.
- c21's +8 measured -2.2 / -3.3 dB against Horn 3, about the -3 target.

Fix: `build/score_config.py`, Ruling 7 `vel_add` for Trumpets 1-2 at 632.9-662.5: `add` 4 -> 7. The base velocity is 88, so the notes play at 95, the lowest velocity of the top layer.
- Expected (inferred): -2.4 / -3.5 dB against Horn 3 (c21's level less a few tenths).
- Do not use +6 or less: velocity 94 or under is the 76-94 layer, about 7 dB softer.
- Raising CC11 cannot replace the layer: the park is 100, and 127 gives only +4.1 dB (40 log10(127/100)).
- Pass: note peaks 2-4 dB under Horn 3, and 2-5 kHz in the first 80 ms no more than c21's.

### 3. The wind legato "holes" are mostly vibrato on the 30 ms measure. About 11 real ones remain: the transition sample and the connected sustain are both low at once (measured; fix inferred)

Re-measured: the c22 measure (`holes22.py`, 30 ms windows) counted Flute 1 / Flute 2 / Oboe 1 / Cor anglais / Clarinet 1 / Bassoon 1 at 7 / 9 / 6 / 6 / 5 / 8 joins of 6 dB or more.

With a 200 ms window, the count falls to 2 / 2 / 3 / 2 / 1 / 0. Kit LEARNINGS section 6 already says to measure flute, oboe and cor anglais joins this way, because their vibrato reads as holes at 30 ms. Many 30 ms "holes" repeat inside the sustained body: Flute 1 at 848 dips -15 dB at +0.38 s and -10 dB at +0.66 s; Flute 2 at 842 dips -13 dB at +0.7 s. That is vibrato modulation, not a join.

The real holes (200 ms window):

| track | qn | interval | depth (dB) |
|---|---|---|---|
| Flute 1 | 138 | 92->87 | 7.8 |
| Flute 1 | 330 | 87->82 | 8.2 |
| Flute 2 | 330 | | 6.6 |
| Flute 2 | 842 | | 6.7 |
| Oboe 1 | 384 | 73->72, p, v60 | 9.9 |
| Oboe 1 | 964 | | 6.1 |
| Oboe 1 | 1014 | | 7.9 |
| Cor anglais | 708 | | 6.3 |
| Cor anglais | 738 | | 7.0 |
| Clarinet 1 | 606 | | 6.8 |

Each is a dip of 8-15 dB, 0.15-0.3 s long, starting about 0.06-0.10 s after the moved note-on. In 20 ms steps relative to the body, Oboe 1 at 384 reads -6 -9 -10 -11 -11 -11 -12 -14 -11 -10 -9 -6 dB.

In a 60 ms frame at the dip:
- the new pitch's first four harmonics are 8-14 dB under their own body;
- the old pitch is 13-48 dB under.

So the old voice is already gone, and the new note is quiet. Neither the transition nor the connected sustain carries it.

The patch explains it (Manual notes):
- The legato script releases the old voice (RELEASE 210-254 ms).
- The TLeg transition sample starts about 0.33-0.5 s into its recording.
- The connected sustain fades in over 440-738 ms on a concave curve, and it plays the sustain sample from its own start, that is, the slow onset of a detached note.

c22's 200 ms attack cap made the sustain's own onset arrive sooner, which is consistent with its failure.

Fix (one range test of Flute 1, Flute 2, Oboe 1, Cor anglais and Clarinet 1, over qn 320-392, 600-760 and 836-1016, against a control range from the same start). No code change is needed: `build/mix.json` already passes `"legato_speed"` parameters into the LegatoSpeed script (`tools/build_reaper.py`, near line 529).
- (a) Set `"legato_speed": {"SSOFFSET": 11025}` (0.25 s at 44.1 kHz, the sample rate in the .ews headers) on those tracks. The parameter name suggests a start offset for the connected sustain, so it should enter on its steady tone instead of its attack (inferred).
  - On the oboe and clarinet, also set `"SUS_GROUP_SUBSTRING": "OBs"` and `"Cls"` to match the group names.
  - This is an Opus state change: rebuild those tracks fully.
- (b) If (a) changes nothing measurable: a new mix.json key in `tools/build_reaper.py`, modelled on `cap_attack()`. It adds 11025 to every region `startSample` of the connected sustain groups ("1Fls", "Fl2s", "OBs", "EHs", "Cls") and leaves their attack at the shipped value. The loop starts I read on the flute (55536-67880 samples) lie well past this offset, so the offset stays inside the attack portion. Check each patch's loop starts before applying it.
- (c) Only if holes remain: LegatoSpeed `RELEASE` 210-254 -> 320 ms, to keep the old pitch under the dip.
- Pass:
  - 200 ms-window holes of 6 dB or more go from 11 to 4 or fewer;
  - the old pitch is at least 10 dB under the new body at +0.15 s (no smear);
  - pcx join timing stays within ±25 ms of c22;
  - 2-5 kHz in the first 80 ms rises no more than 3 dB.
- Change the actor's measure (`holes22.py`) to a 200 ms window on flute, oboe and cor anglais, so the next cycle does not chase vibrato.

### 4. Trumpet 3's accents (bars 255-262) are still only +1.1 dB: its plain notes ride the crescendo up to the accent's CC11 level (measured; fix values inferred)

Where: Trumpet 3, accented half notes 1016-1044 (printed accents at 1016, 1020, 1024, ...; cresc. from 1024).

Evidence (parts.json):
- At 1024, CC11 is 97 at the note-on and falls to 90 by 1024.6.
- The plain note at 1026 sits at CC11 93-96, because of the crescendo and the re-tongue return to 88-93.
- So the accent is 1-4 units over its neighbours, 0.4-1.5 dB by 40 log10. The actor's +1.1 dB matches.
- Ruling 8 took the trombones' rule (CC11 0.10 × rest). The trombones' rule works on their tied 7.6 qn notes, where no plain notes rise beside the accents.
- In the brass KS Masters CC11 is the Global Group volume (patch), so a larger CC11 bump adds weight without a brighter layer.

Fix: `build/score_config.py` Ruling 8 block (near line 2243): for Trumpet 3 over 1016-1048, use `amt_rel` 0.20 (the generic brass value is 0.21) with the `_C17_ACC_SHAPE` timing (hold_s 0.15, end_s 0.45). The 120 ms controller fade smooths shorter holds. Keep CC1 at +3.
- Expected (inferred): a peak near CC11 106-108 against 93-95, so +2-2.5 dB over the plain notes.
- Do not raise accents elsewhere (Dan, c17).
- Pass: accented minus plain peaks +2 to +3 dB. 2-5 kHz in the first 80 ms stays under the body, so Dan's "weight, not bite" holds (c21: -1.7 dB).

### 5. The basses' accelerando eighths (bars 205-210) are cut off before their own peak (measured; fix inferred)

Where: Double basses, "Stac On Bow RRx9", qn 816-840 (A flat 1 pedal, accelerando 168 -> 186 qn/min).

Evidence. The peak of each stroke (30-2000 Hz, 10 ms windows, before the next note):
- 816-840: the strokes last 0.110 s, and the median peak comes at 0.120 s after the note-on. 79 % of the strokes peak at or after the note-off.
- 792-816 (higher pitches): the strokes last 0.107 s and peak at 0.087 s. Only 40 % peak at or after the note-off.

So the low strokes are released while still rising. That is why the stroke p90 tracked the note length so closely:

| cycle | note length | stroke p90 |
|---|---|---|
| c19 | 0.35 qn | -31.7 |
| c20 | 0.30 qn | -41.0 |
| c21 | 0.30 qn, +4 dB region and +24 CC11 | -34.7 |
| c22 | 0.33 qn | -33.9 |

Timing is fine: each stroke reaches its peak minus 3 dB 0.015 s before the beat (0.1 s lead).

Fix: `build/score_config.py`, the 816-840 "Stac On Bow" length: 0.33 -> 0.37 qn. That is 0.13 s at 172-184 qn/min, which covers the 0.12 s rise.
- Expected (inferred): p90 back to c19's level (-31.7) or a little over, because of c21's region gain.
- Separation: the eighth slot is 0.5 qn, and c19 at 0.35 qn separated by 7.7 dB.
- Pass: p90 -32.2 or louder; dips between strokes 7 dB or more.

### 6. Horn 4's held A flat 3 (bars 43-47) still wobbles, because both CC11 fills peak 0.24-0.30 qn after the dips they fill (measured; fix inferred)

Where: Horn 4, one 6.5 s pp note (qn 167.73-185.9, "Sus MAX", v41).

Evidence (60-5000 Hz, 0.1 s windows):
- A sag of -4.7 dB at qn 172.80 and a loop-seam dip of -7.3 dB at qn 181.26 (0.25 s wide, with a spectral-centroid jump to 318 Hz).
- The c22 fill (C's points from the c21 stem) peaks at 173.1 and 181.5. That is 0.30 / 0.24 qn late, before the 120 ms controller fade adds to the delay.
- After the second dip the level overshoots to 0 dB at about qn 182, because the 3.1 qn wide fill is still +5 there.
- This is the Movement I c61 lesson: the fill was placed on score time, but the note-on is led 0.27 qn.

Fix (`build/score_config.py`, the Horn 4 CC11 fill near line 2235):
- First fill: shift it 0.45 qn earlier: (171.0, 0), (172.05, 3.0), (172.65, 4.5), (173.35, 3.0), (174.15, 0).
- Second fill: narrow it to the dip: (180.45, 0), (180.85, 5.0), (181.1, 7.0), (181.4, 5.0), (181.8, 0).
- Expected (inferred): the 0.25 s level range drops from 7.2 to about 4-5 dB.
- Pass: 5 dB or less, with no point over the note's median body by more than 1.5 dB.

## The coordinator's c22 list, through this lens

- **Trumpet repeats.** Verified, with the same kind of measure. Median dips: Trumpet 1 7.1 dB (n 17), Trumpet 2 5.5 (n 18), Trumpet 3 6.2 (n 48); 3 under 3 dB on each.
  - The weak ones are the coda's c4 r8 c8 figure (793.5-807.5, the eighths after the printed eighth rest): Trumpet 2 1.6-2.8, Trumpet 3 2.2-2.6.
  - The figure's quarter ends on time (793.0), but the eighth is led 0.065 s, so the printed rest shrinks from 0.18 to 0.11 s, under the 240 ms release.
  - If anything changes there: the eighths at 793.5 / 795.5 / 805.5 / 807.5 with no lead (on the beat, as the staccato rows do). Low priority.
- **Chorale repeats.** Finding 1. The 120 ms controller fade is confirmed in the patches (every brass sustain group: `MidiController` CC1 / CC11 `fadeTime` 120.0). Not proposed: a deeper or longer CC11 fall. The channel lane also lifts the releasing old voice.
- **Wind legato holes.** Finding 3.
- **Basses' eighths 816-840.** Finding 5.
- **Horn 4 wobble.** Finding 6.
- **Trumpet off-beats.** Finding 2: +7, not "about +7 untested". The value comes from the layer table, and +6 would fail.
- **Trumpet 3 accents.** Finding 4.
- **Other movements:**
  - Movement I c61, "move CC11 rises with moved note-ons": applies here (finding 6, Horn 4).
  - Movement I c61, "wind velocity floor did not help": consistent with c22.
  - Scherzo c19, Horn 1 hole fixed on "Sus MAX": applies; c22's Horn 1 now has 0 of 19 holes.
  - Scherzo c20, "repeated string staccatos run together on long short-row releases": does not apply to the basses' "Stac On Bow" (dips 10 dB and more), but finding 5 is the reverse case (a note too short for its rise).
  - Scherzo c20, "compare range tests with a control range from the same start": built into finding 3's test.
- **Not checked through this lens:** the fff arrival steps, the harp at 235, the timpani stroke levels (Movement I c60). These are for B and C.

Do not touch:
- the c19 chorale pitch-change overlaps and printed-breath gaps;
- the Horn 1 "Sus MAX" joins at 90 / 286 / 868 (0 holes of 6 dB or more);
- the trumpet 240 ms f / ff release cap and its 0.1 s re-tongue gap (repeat medians 5.5-7.1 dB, note ends intact);
- the basses' 0.30 qn strokes outside 816-840 and their 10 dB and larger separations;
- the Tremolo rows from bar 223;
- the harp's Harmonics / Gliss Technique rows on keys 112 / 113;
- the cor anglais "Sus MAX" unison spans;
- the brass accents in 1088-1108 (+0.2 to +1.5 dB, with no 2-5 kHz bite).

# Cycle 03, critic A: articulation and phrasing (render c02)

Material: `cycles/c02/render/` (stems after the Violins I stem fix, master), `cycles/c01/render/` and `cycles/c00/render/` for comparison, `build/parts.json` (the c02 data plus the stem-fix level steps; tempo map, moved onsets, keyswitches and lanes as rendered), `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py`, `tools/auto_fills.py`, the woodwind and 1st Violins KS Master `.oib` files (rows, sample folders, region counts and velocity bands read with `opus_state.py`), score pages 2, 5 and 7, and May 2021 HO manual PDF pages 108-113 (group A4). Times come from the parts.json tempo map, with qn 0 at 0 s of the rendered files. Levels are RMS on the stems in 10 ms windows (5 ms or 2.5 ms hop) unless the text says master. Each judgement is marked **measured**, **read** (code, patch file or score) or **inferred**.

## Manual notes (A4, PDF pages 108-113, read in full; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 108 | "Flute 2" is a different player in a different seat; no samples are shared with "Flute", so a unison does not collapse into one performance. | Flute 1 and Flute 2 (a2 at bars 41-44, the tuttis). | Followed: Flute 1 on FL KS Master, Flute 2 on FL2 KS Master (read). |
| 109 | Sustain dynamics on the Mod Wheel, all three layers playing at once (Play-era text; the 2025 manual p.52 puts dynamics on CC11 and the vibrato crossfade on CC1). | Every wind Sus and Leg note. | Followed as the 2025 manual: CC11 dynamics; the clarinets on CC1 dynamics (`CC1_DYN_TRACKS`). |
| 109 | **Sus Expressive**: slower attack and gently increasing vibrato. | The dolce / espress. phrase starts: Clarinet 1 bar 153, Oboe 1 bar 185, the codetta's dolce woodwinds 225-236. | Not used. The row is cheap (Sus Exp 1.0-1.6 thousand regions per KS Master, read). An option for later cycles (inferred gain). |
| 109-110 | **Legato Repetitions** (LegRep RRx4): a non-vibrato sustain plus a short re-tongued attack (4 round robins), "for repeated notes within an otherwise legato phrase". | The slurred tenuto repeats (portato) of the link (bassoons and bass clarinet, bars 141-148), the hemiola (bars 101-104, 301-304) and the coda (bars 321-323). | Not used. Several of these repeats do not separate at all (finding 3). |
| 110 | Short notes have no release trails; hold staccato MIDI notes long enough for the natural decay to sound in the rests. Staccatissimo is shorter than staccato. | 600+ printed wind staccatos on "Stac DblTng RRx9" (Flute 1/2, Oboe 1, cor anglais, Clarinet 2), played at half their written length (eighths 57 ms at quarter 264). | Mostly followed. At the same pitch and velocity, the eighths come out only 1-2 dB under the quarters (measured), and Movement I read a 340-562 ms release on the row. The theme head's same-pitch eighth pairs dip 5-7 dB on the wind stems (good, S1). |
| 110 | Double tonguing ("tiki tiki") for fast note sequences; Marcato = short notes with a strong accent. | The theme head's eighths (0.114 s apart); the accents. | The DblTng row fits the eighths. Marcato rows are correctly not used: Dan's rule is weight, not bite. |
| 111 | Runs, trills, flutter tongue, fixed-speed repetitions, FX. | None printed; the fixed-speed repetition loops (145/170 bpm) do not fit 528 eighths per minute. | Not applicable (MANUAL-GAPS #15). |
| 112 | Legato needs no gap and at most an octave between the notes; legato patches are monophonic (CC22 0-63 makes them polyphonic). | Every wind slur. | Followed. No slurred wind interval is wider than an octave (`WIND_WIDE_LEG` 12), and no chord reaches a wind legato row (checked in parts.json). |
| 112 | **Legato Slur Repetitions**: the second and third occurrences of a pitch inside a slur use re-tongued samples. | The clarinets' slurred repeated quarters (bars 50-54, 129, 285). | Not used. These repeats are merged into one note and are not heard (finding 2). The Clarinet KS Master has "Leg Slur Rep" (15.6 thousand regions against 13.7 for "Leg Slur", read); the Bassoon and Bass clarinet KS Masters have none. |
| 112-113 | Slur Runs: strong slur only for seconds; dynamics on CC; many voices. | No woodwind scale runs. | Not applicable. |
| (read, not on these pages) | Every woodwind KS Master also has "Leg Slur Accent MAX" (CL: "Leg Slur Accent"), which layers StacSs attacks on the legato head (16-21 thousand regions). | Accented slur heads (counterstatement bars 30-38). | Not used, and not recommended now: memory, and the StacSs front is the opposite of weight, not bite. |

MANUAL-GAPS additions: #2 should record that the clarinets' slurred repeats (merged, 0 dB) and the link's portato repeats are the scherzo's clearest cases for "Leg Slur Rep" and "LegRep RRx4". #8 should note that "Sus Exp" costs only 1.0-1.6 thousand regions per woodwind KS Master.

## Findings, ranked by what a listener would gain

### 1. The nine p/mp theme-head accents of Violins I now bite: "Sus Marc LITE" at v70-94 triggers its *f* marcato attack.

- **Where.** Violins I at qn 39, 51, 69, 75 (bars 14-26), 285 (bar 96), 759, 771, 789 and 795 (bars 254-266). These are the c02 `_MARC_HEADS`, with their stem-fix level steps `_MARC_FIX`.
- **Read (.oib).** The row is the sustain layers plus a short-marcato attack layer chosen by velocity: "V1 MarcSh mp" at velocity 1-65, "V1 MarcSh f" at 66-108 and "V1 MarcSh ff" at 109-127. The c02 `vel_by_cc` (34,70) (46,78) (58,86) (72,94) puts every p/mp head on the **f** marcato attack.
- **Measured.**
  - Violins I stem, 2-5 kHz over the first 110 ms minus the body (+0.15..+0.4 s): +3.2 to +4.7 dB at all nine heads. At c01 (Sus MAX strokes) it was -4.9 to -8.2.
  - Master, 2-5 kHz over the head's first 110 ms minus the 2-5 kHz peak of the staccato before it: 39 +5.2, 51 +0.3, 69 +9.3, 75 +5.6, 285 +5.0, 759 +7.3, 771 +0.5, 789 +8.5, 795 +6.1 dB. At c01 these were -5.7 to -13.9.
  - The heads with the smallest level steps (69: -2.4 dB, 789: -2.8 dB) jump the most. The broadband level is right (+2.0..+2.6 dB, c02), so the extra comes from brightness.
  - Compare the kit's harsh trombone accents (master 2-5 kHz jump +10 dB before the fix, +2 after; mockup-kit LEARNINGS section 7). Here the bite falls on the p leggiero theme.
- **Fix.** In `build/score_config.py`, c02 block, change the `_MARC_HEADS` `ART_SPANS` to `"vel_by_cc": [(34, 50), (46, 56), (58, 61), (72, 64)]`. Every head then stays in the mp marcato band (velocity 65 or less).
  - Re-fit `_MARC_FIX` on the c03 render with the same method: an exact step per head, landing at +2 dB over the staccato before it. The softer attack should need smaller cuts (inferred).
  - If the mp band is still bright, add a front trim per head in `LEVEL_SHAPES["Violins I"]`: -3 dB from the moved onset to +0.10 s, then back to the head's step by +0.15 s.
  - Pass: Violins I 2-5 kHz front minus body at 0 dB or under, and the master's 2-5 kHz jump at +2 dB or under, with the heads still +2..+4 dB over the staccato before them.

### 2. The clarinets' slurred repeated notes sound as one held note (S1). The manual's Legato Slur Repetitions row is made for this.

- **Where (read: score p.5 and the event list).**
  - Bar 129 (qn 384-387): Clarinet 1 G4 and Clarinet 2 B3, f, four repeated quarters under one slur.
  - Bar 285 (qn 852-855): Clarinet 1, the same figure in the reprise.
  - Bars 45-54 (qn 135-159): Clarinet 2's repeated G4/A4 quarters under slurs (135, 153, 156-158), and Clarinet 1 at 147 and 158.
  - All are listed in parts.json `slur_rep_merged`: Clarinet 1 148, 159, 385, 386, 387, 853, 854, 855; Clarinet 2 136, 154, 157, 158, 159, 385, 386, 390.
- **Measured.** Dip at each repeat (mean of -0.2..-0.08 s minus the minimum over -0.08..+0.06 s, stem):
  - Clarinet 1: 385 / 386 / 387 = 0.0 / -0.6 / 2.7 dB; 853 / 854 / 855 = -2.0 / 0.0 / -0.1 dB.
  - Clarinet 2: 154 -0.1, 157 -2.3, 158 0.2, 159 0.2, 385 1.4, 386 -1.9 dB.
  - The 10 ms envelope of Clarinet 1 over 384.6-388 rises smoothly from -42 to -37 dB with no trace of the three re-attacks.
- **Why (read).** `score_to_parts.py` merges a wind same-pitch note inside a slur into the note before (mvt1 c05). It marks the merge with a `WIND_SLUR_REP_NOTCH` of 8 CC11 (88 -> 80 and back over 0.25 qn). The clarinets' dynamics are on CC1 (`CC1_DYN_TRACKS`), and the notch falls inside a crescendo, so it does not dip.
- **Fix (manual p.112; Movement I c37-c38 measured the same row: Clarinet 1 motif repeats 3.0-4.0 -> 5.5-9.0 dB).**
  - Memory-neutral form: `REP_ROW = {"Clarinet 1": [(0.0, SCORE_END, "Leg Slur Rep")], "Clarinet 2": [(0.0, SCORE_END, "Leg Slur Rep")]}` in `build/score_config.py`.
    - REP_ROW moves both the Leg Slur and the Sus Non Vib notes to the row, so those two rows unload. Regions per track: 13.7 + 1.2 thousand out, 15.6 in, about +0.7 thousand (read). Clarinet 2 keeps its Stac row.
    - The merge code already skips slurred repeats inside a REP_ROW span (mvt1 c39). The repeats then take the re-tongue gap and CC11 fall, with the gap clamped by the scherzo's `REP_ROW_GAP_S` (0.06, 0.15). That keeps them clear of the row's 30 ms VoiceTimer (mvt1 c37-c38).
    - Risk (inferred): every clarinet legato join now runs on this row. After the render, check that every Clarinet 1/2 note sounds (no note 15 dB or more under its neighbours) and that the trio's join holes (finding 4) are no worse.
  - Targeted alternative if the whole-track swap misbehaves: spans (147.9, 148.1), (158.9, 159.1), (384.9, 387.1), (852.9, 855.1) for Clarinet 1 and (135.9, 136.1), (153.9, 159.1), (384.9, 386.1), (389.9, 390.1) for Clarinet 2. This costs about 15.6 thousand regions per track (about 0.7 GB each at c02's 4 GB per 92 thousand).
  - Last resort with no new row: `MERGE_NOTCH_AT` 20 CC at those onsets (inferred 3-4 dB).
  - Pass: every listed repeat dips 3-6 dB on the stem.

### 3. Woodwind portato (slurred tenuto repeats) is uneven: some voices pulse, others in the same chord hold one tone.

- **Where (read).** Every case is a slurred same-pitch repeat whose second note carries a tenuto:
  - The link, bars 141-148 (qn 420-441, ppp under Violins I's harmonic): Bass clarinet E2, Bassoon 1 E4, Bassoon 2 B3, dotted halves.
  - The hemiola, bars 102-104 / 302 (qn 303-309, 903-909): Oboe 1/2, Flute 2, Clarinet 2, Bassoon 2, contrabassoon.
  - The fugato close, bars 321-323 (qn 963, 966): Clarinet 1/2, cor anglais, Bassoon 1.
- **Measured (same dip measure as #2).**
  - Link: Bass clarinet 426 / 429 / 435 / 438 = 0.4 / 0.4 / 0.4 / 0.4 dB (only 423 dips, 5.3). Bassoon 2 423 / 426 / 429 = 0.6 / 0.4 / 0.9. In the same chord, Bassoon 1 dips 6.1-7.0 at every one, so one voice of the three pulses and two hold.
  - Coda: Clarinet 1 963 / 966 = -1.3 / -0.4, Clarinet 2 0.4 / 0.5, cor anglais 966 1.1.
  - Hemiola: Oboe 1 303 / 903 = 0.1 / 0.8, Clarinet 2 303 1.0, contrabassoon 303 / 903 = 0.6 / 1.3. The later repeats of the same bars dip 3.5-10.8.
- **Why (read in parts.json).** These repeats are not in `rep_retongued` (Bass clarinet lists only 423; Bassoon 1/2 none of 420-441). Each note ends about 0.06 qn (14 ms at quarter 264) before the next moved onset, with no CC11 fall. That is the plain same-pitch gap, although `WIND_REP_PORTATO = True` should have given them the `WIND_REP_RETONGUE` 0.06 s gap and 6 CC fall.
  - Bassoon 1's dips come from its Sus MAX re-attack rising slowly, not from a gap.
  - At quarter 126, Movement I measured 0.06 qn (29 ms) giving 2-6 dB on bassoon and bass clarinet (kit section 7). The same qn here is half the time.
- **Fix.**
  - (a) In `tools/score_to_parts.py`, find why the `WIND_REP_PORTATO` branch (the `same_pitch and WIND_REP_RETONGUE` test, about line 2655) skips these second notes when it takes Bass clarinet 423. Make the portato repeats take the re-tongue gap and fall.
  - (b) Manual p.109-110, the recorded re-tongue:
    - `REP_ROW["Bass clarinet"] = [(0.0, SCORE_END, "LegRep RRx4")]`. The track plays only Sus Non Vib, so this is a row swap of about +1-2 thousand regions (inferred from the other KS Masters' 2.1-3.3 thousand).
    - `REP_ROW["Bassoon 2"] = [(419.9, 442.0, "LegRep RRx4")]` (+2.7 thousand regions, read). Make it `[(419.9, 442.0, "LegRep RRx4"), (299.9, 310.0, "LegRep RRx4"), (899.9, 910.0, "LegRep RRx4")]` if memory allows.
    - Keep `REP_ROW_GAP_S` (0.06, 0.15).
  - Target: a gentle, matched pulse, 2-4 dB on Bass clarinet, Bassoon 1 and Bassoon 2 alike at 423-438 (Bassoon 1's 6-7 dB may want `MERGE`-style smoothing later), and 2-4 dB at the coda and hemiola repeats.

### 4. The trio tune in Clarinet 1 does not sing: neighbouring notes jump up to 10 dB at one controller value, and the clarinet and bassoon legato joins dig 4-9 dB holes.

- **Where.** Clarinet 1 bars 153-168 (qn 456-504, dolce), 197-200 (576-600), the ff return 209-224 (624-672) and the reprise's second idea 281-288 (840-862). Also Clarinet 2 and Bassoon 1 legato lines.
- **Measured: pitch.** Body levels at CC11 49 and envelope +2 dB in the trio tune:
  - G sharp 4 at 456: -50.6 dB; B4 at 459: -50.6; A4 at 468: -41.4; G sharp 4 at 466: -51.4; B4 at 478: -50.0 (envelope removed).
  - Per-pitch residual of all Clarinet 1 Leg Slur bodies, after a CC11 fit: G sharp 4 -5.8 (n 10), B4 -3.5 (18), A4 +4.0 (13), C5 +3.2 (4), C sharp 5 -1.9 (6).
  - c01 gives the same values within 0.3 dB, so this is a property of the samples. The kit found Clarinet A flat 4 (the throat B flat) at -8 (mockup-kit LEARNINGS section 13).
  - Clarinet 2: C sharp 4 -6.6 (n 3). Its f C sharp 4 at 210 and 894 sits 16 dB under its neighbours.
- **Measured: joins.** Hole at a legato join = the lower of the two notes' bodies minus the minimum over moved onset -0.03 s .. score onset +0.06 s. Median per track:
  - Clarinet 1 4.2 dB (46 of 84 joins over 4 dB), Clarinet 2 4.9, Bassoon 1 4.7.
  - Against those: Oboe 1 2.5, Flute 1 1.5, cor anglais 1.1, Horn 1 2.0.
  - Worst Clarinet 1 joins: 629 / 630 / 634 / 638 = 5.4 / 7.2 / 8.8 / 7.8 dB (bars 210-213, ff), 848 / 850 / 857 = 5.2 / 11.6 / 8.7, 578 8.9, 466 7.6.
  - Flute 1's "col Vl. solo" joins at 1054 / 1055 (bar 352) fall 13-15 dB between notes on the 10 ms envelope. The solo violin covers part of that.
- **Fix.**
  - (a) `build/pitch_trims.json`: `"Clarinet 1": {"68": 4.0, "71": 3.0, "69": -2.5, "72": -2.0, "_arts": ["Leg Slur", "Sus Non Vib"]}` and `"Clarinet 2": {"61": 4.0, "_arts": ["Leg Slur", "Sus Non Vib"]}`. That is about two thirds of each residual, as the kit does. If finding 2's REP_ROW lands, the notes still carry these rows' names to every other rule ("the keyswitch only").
    - Pass: the trio tune's same-CC bodies within 3 dB of each other.
  - (b) On the c03 render (after the pitch trims), run `tools/auto_fills.py 3 build/parts.json`, dry run first, for joins dipping 5 dB or more. Add "Clarinet 2" and "Bassoon 1" to its `TRACKS` / `RAISE_TRACKS`, which is a generic list in the tool; Flute 1 and Clarinet 1 are already in it.
    - The fills belong to the next cycle, because the pitch trims move the bodies the tool measures against.

### 5. Oboe 1's staccato row plays hot at f/ff, so its theme-head accents are the softest notes of the head.

- **Where.** Oboe 1's accented half note after the staccato quarter and eighths: qn 123, 207, 315, 345, 351, 819, 891, 915, 945 and 951 (bars 42, 70, 106-118, 274, 298, 306-318).
- **Measured.**
  - The accent's first 150 ms (Sus MAX with the `GENTLE_ACCENT` swell) minus the peak of the staccato before it: -8.2 / -9.4 / -6.6 / -5.4 / -6.8 / -10.4 / -9.5 / -6.7 / -5.7 / -6.9 dB. Flute 1 at the same onsets: -0.9..-3.0.
  - Oboe 1's staccato peaks minus Flute 1's outside the counterstatement: +4.5 dB at c02, against -1.6 at c00 on Sus slices.
  - The c02 velocity table (-12) moved the counterstatement only (-0.4 dB there), because the row's level barely follows velocity (c02 LEARNINGS).
  - Accent bite is not the problem: 2-5 kHz front minus body -1.4..-9.2 dB.
- **Fix.**
  - Generic, in `tools/score_to_parts.py` (the `ROW_TRIM_DB` block, about line 4991): let `ROW_TRIM_DB` apply to wind tracks too. Today it reads `if family == "string"`. Check that its skip tests (a line that mixes rows) do not exclude staccatos with no legato neighbour.
  - Then `ROW_TRIM_DB["Oboe 1"] = {"Stac DblTng RRx9": (-5.0, 72)}` (from CC11 72 up), which is c00's relation to the flute.
  - After the render, run `tools/fit_accents.py 3 build/parts.json --family wind` to bring any head still outside +2..+4 dB into it (cap 5 dB).
  - Pass: Oboe 1's tutti staccatos within about 1 dB of Flute 1's, and the heads +2..+4 dB over their staccato.

## Also measured (not ranked)

- **Woodwind accents (BRIEF item 9), measured.** 2-5 kHz over the first 100 ms minus the body, median per track: Flute 1 -3.9, Flute 2 -6.8, Oboe 1 -5.4, cor anglais -7.7, Clarinet 1 -8.2, Clarinet 2 -4.1, bassoons and contrabassoon -2.7..-3.7 dB. No wind accent bites; the only exception is Flute 1 at the summit (1005, +8.6, a Leg Slur MAX head at v80).
- **Wind theme-head staccatos, measured.**
  - The same-pitch eighth pairs dip 5.0-7.2 dB at the median on the Flute 1/2, Oboe 1, cor anglais and Clarinet 2 stems (S1 met on the stems).
  - In the heads, Flute 1's eighths read 6-7 dB under its quarters. At the same pitch and velocity the gap is only 1-2 dB. The rest is register: the row's per-pitch residuals are Flute 1 D5 -8.9 and F sharp 5 -7.8, and the eighths sit a fourth under the quarters. This is a candidate for Stac-row pitch trims later.
- **No silent wind notes** (every note within 15 dB of its neighbours, except Clarinet 2's C sharp 4, finding 4). No chords on wind legato rows, and no slurred wind interval over an octave (manual p.112).

## Do not touch

- The wind "Stac DblTng RRx9" rows and their 0.02-0.03 s leads (pair dips 5-7 dB).
- `GENTLE_ACCENT` on the winds (no bite measured).
- The hemiola strokes 300-310 / 902-910 and Violins I's tutti "Stac RRx14".
- `PORT_TARGETS` 640, the c02 `ROW_REMAP` choices, the re-bow fills, and the CC70 and CC15 lanes.
- The Marc LITE heads stay a pair with their level steps. Change their velocity band and refit the steps; do not drop the row.

# Cycle 25, critic A: articulation and phrasing (on the c24 render)

Material:
- `cycles/c24/render` stems and `cycles/c24/build_render/parts.json` (the data as rendered).
- `cycles/c18/render` and its parts.json as the older comparison. c23's stems are deleted. c23's parts.json and `cycles/c24/before/build_reaper.py` were used for the data and envelope comparisons.
- `cycles/c24/records/`. The 1st Violins KS Master was read with `mockup-kit/opus/opus_state.py` `load_oib` (read only).

Method:
- Levels are the mean of the two channels' power in 5 or 10 ms frames, on the parts.json tempo map.
- The written envelope was read with `vol_points` from the source cut before `ENV_LUA`, as `stem_fix.py` does.
- New this cycle, a pitch-resolved separation measure for the bar 23 figure. Each pitch's band is harmonics 2-5, ±0.3 semitone, on a 2048-point STFT with a 5 ms hop. The measure is how far the previous note's band has fallen below its own peak at the crossover, the first frame after the next note-on where the next pitch's band reaches the previous pitch's band.

"Measured" means a number from the render, parts.json or a patch file. "Inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c25. I read group A2, PDF pages 95-99 of the May 2021 HO manual, in full (string effects and legato). I also read `MANUAL-GAPS.md`.

| page | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| 97 | Repetitions exist only for violas and basses. A dozen pulses per note, tempo-synced, CC11 crossfades, no velocity | the theme's repeated eighth pairs (S1) | correctly not used. The violins have no such row, and the theme's repeats are pairs, not runs |
| 96 | Spiccato Runs exist only in the 2nd Violins and need consecutive steps of a whole tone or less | none: the theme head leaps and repeats | not applicable |
| 96-97 | Slur Runs (1st and 2nd Violins) are for 16ths at quarter 125 or faster. Tremolos ignore velocity and use CC11 | no runs or string tremolo in this lens's passages | not applicable |
| 98 | A legato transition needs no gap between the notes, and the first note of a phrase has none. Legato patches are monophonic; CC22 64-127 makes them polyphonic (2025 p.91 corrects the polarity) | celli trio tune 169-184, the violins' tune 177-184 / 209-224, the solo 349-356 | followed. pcX finds 200 celli, 97 Violins I, 104 Violins II and 18 solo joins, and no chord on a legato row. Timing: finding 3 |
| 98 | Legato Slur Staccato adds a slur-staccato accent to non-legato phrase starts | the second idea's phrase starts after rests (45, 121, 277) | not used. Not proposed: entries are already handled by entry leads and CC11 heads |
| 98-99 | Bow-change legato: Opus picks bow change, slur or portamento from the MIDI | celli 512 / 524 (c24 critic C #2b) | "Leg BC MAX" not loaded (c24 CHANGES). Still open, not ranked here |
| 99 | KS Masters switch rows by keyswitch | Violins I's row changes inside the theme | followed. Keyswitches sit 0.03 qn or more before their notes. At 340.312 a Stac RRx14 keyswitch falls 0.01 qn after the 340.302 D sharp, which stays on Spiccato as intended |
| 2025 p.92 (`score_to_parts.py` note) | Opus counts round robins per note | bars 115 / 315 (finding 2) | confirmed by measurement, finding 2 |

## Findings, ranked by what a listener hears

### 1. The 62 Violins I staccatos moved to "Spiccato RRx9" now sound as unprinted accents: +3.3 dB median over their neighbours (c18 -1.2), and the tutti F sharps are louder than the accented C after them (measured)

Where: Violins I, every note `STAC_ROW_BY_PITCH` moved to Spiccato (D5, D sharp 5, F sharp 5). Most audible:

| passage | qn (dB over neighbouring short notes) |
|---|---|
| theme | 64 (+5.7) |
| counterstatement | 109.5 (+6.2), 127.5 (+6.5), 128 (+5.9) |
| tutti | 321 (+7.3), **342 (+8.1)**, 356 (+8.4), 921 (+6.3), **942 (+7.7)**, 956 (+7.7) |
| retransition | 747-753 (+5.3..+10.8) |
| reprise | 817.5-824 (+4.6..+8.1) |
| coda | 988 (+5.9) |

Evidence (measured):
- 70 ms peak of each moved note less the median of the unmoved short notes within ±3 qn:
  - c18: median -1.2 dB, 10 of 62 over +3;
  - c24: median **+3.3 dB**, **34 over +3, 21 over +5**.
- The same notes, c18 to c24, same data: from Staccatissimo +4.2 dB median, from Stac RRx14 +5.7. Notes that stayed on their rows moved -0.0..-0.3.
- At bar 115 (qn 342 to 345) the 70 ms peaks are:
  - F sharp (Spiccato) -23.6 dB;
  - G -34.0, A -32.0;
  - B -26.6, **accented C -26.5**.

  So the unaccented staccato quarter is the loudest note of the figure, 3 dB over the printed accent. Bar 315 is the same.
- Inside an all-Spiccato phrase these pitches are not hot (reprise 780-786: F sharp -41.0 / -35.7, D sharp -37.6 / -35.0 against G / E -33.7 / -35.3). So the step comes from the row change at the same velocity, not from the pitch.
- Velocities of the moved notes: v45-76 (24 notes, overlapping the original Spiccato notes' v57 / v67) and **v81-95 (38 notes, no original Spiccato note at 80 or above)**.
- Part of c24's separation gain (D5 0.7 -> 4.7, D sharp 5 2.2 -> 7.6 dB) is the Spiccato row's shape, which a pure gain change keeps (inferred: trough and peak scale together).

What a listener hears (inferred): the theme head's eighth pairs and quarters get an accent wherever the line touches D, D sharp or F sharp. The pattern follows pitch, not metre.

Fix: lower only the moved notes, on the instrument side.
- a) Tutti and loud notes, `build/mix.json` "Violins I" `region_gain_db`: append `{"rows": [], "row_dyn_db": {"Spiccato RRx9": {"vel>=80": -4.0}}}`. This is the form Violins II already uses. It touches only moved notes (all 38 at v81-95) and keeps their separation.
- b) The soft moved notes (v45-76): add an optional fourth value `vel_add` to `STAC_ROW_BY_PITCH` in `tools/score_to_parts.py` (default 0), applied to rerouted notes only. Scherzo value: `{"Violins I": [(74, 78, "Spiccato RRx9", -10)]}`, starting with the notes under velocity 80.
- Range test 96-132 and 326-358 against a same-start control. Acceptance:
  - moved notes -1..+1.5 dB against their neighbouring short notes;
  - separation at D5 / D sharp 5 / F sharp 5 still 4.5 dB or more;
  - the F sharp at 342 / 942 under the accented C at 345 / 945.

### 2. Bars 115 / 315 did not get worse: the 5.8 -> 3.3 dB reading is an artefact of the broadband trough measure. Do not apply CHANGES' proposed fix (F sharp back on Stac RRx14 or a reset), which would undo a 5 dB gain (measured)

Where: Violins I, qn 342-345 and 942-945 (the figure F sharp, slurred G-A, B, accented C), and qn 346-349 / 946-949.

Evidence:
- **Round robins are counted per note number, across all rows** (measured). I compared c18 and c24 at notes with identical data:
  - 13 Spiccato notes at 757-786 are identical to 0.00 dB in their first 80 ms;
  - their per-row counts differ by 43-46 between the renders;
  - for 782 / 784 / 784.5 / 786, the per-row-per-key counts differ too (0 vs 17, 0 vs 19, 1 vs 20, 1 vs 18).

  Only a counter per note number across rows predicts these identities. So moving the D sharp and F sharp to Spiccato changed no other key's position. The B5 at 344 / 944 has the same per-key position in c23 and c24 (344 is the 13th B5 in both), so it plays the same take.
- Between c23 and c24, nothing else changed at 342-345:
  - notes, velocities and CC11 / CC1 are identical (the C6 at 344.56 is the same in both);
  - the written envelope is flat at 10.33 dB from 313 to 359 in both (vol_points);
  - the only other change is the orphan group switched off on the Stac rows.
- Pitch-resolved crossover decay (previous note's band below its peak at the hand-off, dB), c18 -> c24:

  | occurrence | F sharp -> G | G -> A (slurred) | A -> B | B -> C |
  |---|---|---|---|---|
  | bar 115 | 16.5 -> **21.8** | 7.6 -> 5.3 | 2.1 -> **8.3** | 12.7 -> 9.5 |
  | bar 315 | 16.6 -> **22.1** | 6.4 -> 5.4 | 1.9 -> **7.4** | 12.9 -> 9.3 |
  | bar 23 (Dan's bar) | 20.7 -> 19.8 | 0.5 -> 4.7 | 3.1 -> **8.5** | 12.2 -> 9.2 |
  | bar 263 | 23.4 -> 16.6 | 5.0 -> 4.6 | 2.7 -> 4.8 | 18.6 -> 20.9 |

  - The other 14 occurrences are within ±1.5 dB except bar 38 (F sharp -> G 2.2 -> 7.8) and bar 116 / 316 (E -> B, 15.4 -> 10.8 / 11.6, cause not found; data identical to c18).
- Why the old measure fell: `fig24.py` takes each note's peak in the first 0.11 s after its moved note-on. The C6's moved note-on (79.67 s) comes 50 ms after the B5's peak, so the "C6 peak" is the B5's own tail in the C6's first frame, and the trough collapses (1.5 dB). In the bands, the B5 falls 7-8 dB before the C6 rises, and the C6 reaches its level at 79.77 s, on the beat.
- B -> C is 9.5 dB now against 12.7 in c18. That follows c23's 0.10 s lead on the C6 (c18 0.06 s). It equals bar 23's accepted 9.2.

Fix:
- Keep the F sharps of 342 / 346 / 942 / 946 on Spiccato and add no reset. Finding 1 deals with their level.
- Replace the first-check measure with the pitch-resolved crossover. My scratch script is deleted with the scratch folder; its logic, to write as `actor_scripts/fig25.py` beside the old columns:
  - mono stem, Hann-windowed 2048-point STFT, 240-sample (5 ms) hop at 48 kHz;
  - each pitch's band is the bins within ±0.3 semitone of harmonics 2-5;
  - for each pair of different pitches, the previous note's peak is the band's maximum from its moved note-on to 0.06 s after the next one;
  - the crossover is the first frame within 0.3 s after the next moved note-on where the next pitch's band is at or above the previous pitch's band;
  - the value is the previous note's peak minus its band level at that frame.
- Acceptance for "nothing worse than c23": per transition, no more than 2 dB under c24's values above.

### 3. The celli's trio tune still joins late: median +36 ms, 38% over 60 ms. Thirteen joins land 80-281 ms late, mostly at 1-2 semitone steps, while the violins' legato sits at +3..+10 ms (measured)

Where: Violoncellos "Leg Slur MAX", bars 169-192 (the trio tune T, arco espress., at quarter 228, eighth 0.13 s).

Evidence (`tools/pcx.py` on c24, read only):

| scope | c18 | c24 |
|---|---|---|
| all 198 celli joins | +36 ms, 35% over 60 | +31 ms, 31% over 60 |
| trio tune 504-552 (29 joins) | +49 ms, 41% | +36 ms, 38% |
| joins of 6 semitones or more | +79 ms | +75 ms (c24's v112 rule changed little) |
| Violins I (97) / Violins II (104) / solo (18) | | +9 / +6 / +6 ms |

Late joins in c24 (qn: interval, lead s, pcX ms):

| qn | interval | lead (s) | pcX (ms) |
|---|---|---|---|
| 510 | 64 -> 63 | 0.18 | +117 |
| 512 | 54 -> 57 | 0.127 | +105 |
| 514 | 57 -> 56 | 0.23 | +80 |
| 516 | 56 -> 57 | 0.205 | +150 |
| 519 | 59 -> 61 | 0.18 | +83 |
| 522 | 66 -> 64 | 0.145 | +104 |
| 526 | 58 -> 59 | 0.27 | +98 |
| 528 | 59 -> 61 | 0.20 | +166 |
| 540 | 56 -> 51 | 0.195 | +109 |
| 542 | 54 -> 59 | 0.245 | +159 |
| 544 | 59 -> 58 | 0.155 | +98 |
| 570 | 54 -> 56 | 0.275 | +281 |
| 576 | 54 -> 42 | 0.03 | +144 |

- The targets are at v80 on purpose: c10, `LEG_VEL_SPANS` celli (504.5, 552, 80), chosen for the slower, more vocal slide. c10 measured -19 ms median then. The fits have drifted since.
- What a listener hears (inferred): at +100-160 ms the cello tune lands about an eighth behind the harp's off-beat chords and Violins II's arpeggios (S2).

Fix (keep v80, refit the leads):
- In `build/leg_leads.json` "Violoncellos", add (pcX - 0.015 s), capped at +0.08 s, to every join above +40 ms, within `LEG_LEAD_CLAMP` (0.03, 0.35). For example 510 -> +0.08, 516 -> +0.08, 528 -> +0.08, 542 -> +0.08, 570 -> +0.075 (clamped at 0.35 s total), 512 -> +0.08, 522 -> +0.08.
- 576 (lead 0.03 s, a twelfth down to 42 at v112): set it apart in `LEG_LEAD_AT` / leg_leads to 0.15 s.
- Check with pcx on the render: trio tune median +15 ms or less, 15% or less over 60 ms. Also check the legato swell (crest at the join no more than +1 dB).

### 4. Violins I's isolated staccatos still ring 60-75 ms longer than the other sections'. The cause is that the V1 Stac samples peak at or after the note-off, which is why the earlier release caps cut the peaks (measured, fix inferred)

Where: Violins I staccato quarters before rests or before a leap: the theme-head quarters and the phrase ends at 81, 95, 165, 393, 801, 827, 861 and 957 (Dan's "lasting too long" family).

Evidence (measured, c24; notes with 0.4 s or more to the next note):

| track (row) | onset to -20 dB under the peak |
|---|---|
| Violins I (Stac RRx14 / Staccatissimo RRx9) | 283 / 285 ms |
| Violins II (Stac RRx9 / Spiccato) | 210 / 210 ms |
| violas | 225 ms |
| basses | 232 ms |
| Flute 1 / Oboe 1 Stac DblTng | 270 / 245 ms |

Peak time after the note-on, against a sounding length of 114 ms (an eighth):

| track (row) | peak after note-on |
|---|---|
| Violins I Staccatissimo | 95 ms |
| Violins I Stac RRx14 | 115 ms |
| Violins I Spiccato (moved eighths sound 57 ms) | 65 ms |
| Violins II Stac | 75 ms |
| violas | 90-100 ms |

- So on Violins I the release starts at or before the peak.
- c23's trial (`STAC_MIN_SOUND_S` 0.10 s plus a 150 ms cap) cut 5-20 dB from the peaks because 0.10 s is still before the 0.115 s peak (inferred from these numbers). Violins II's 150 ms cap works because its samples peak 40 ms before the note-off.

Fix (range test 84-132 and 950-960 against a same-start control):
- Set `STAC_MIN_SOUND_S` {"Violins I": 0.14} only for short-row notes with 0.2 s or more to the next note (the existing `STAC_MIN_SOUND_GAP_S` logic), so eighth pairs keep their length.
- Add a 220 ms `sus_release_cap_ms` with `any_dyn` on "Staccatissimo RRx9" and "Stac RRx14" for Violins I. Make it conditional on the minimum-length notes if `cap_release` can take a note filter; otherwise test it on the whole row.
- Acceptance:
  - 60 ms peaks within 0.5 dB of the control;
  - onset to -20 dB at 230 ms or less on isolated quarters;
  - eighth-pair separation unchanged.

### 5. Accents: no bite anywhere, but the cor anglais' accents arrive late (measured)

Where: the 321 printed accents. Accents per track: Violins I 47, Violins II 42, violas 35, celli 28, Flute 1 36, Oboe 1 28, cor anglais 29.

Evidence (c24):

| track | 2-5 kHz in the first 80 ms against the body | time to within 3 dB of the note's maximum, from the score onset |
|---|---|---|
| Violins I | -6.3 dB | +34 ms (p90 +120) |
| Violins II | -4.8 dB | +32 ms (p90 +216) |
| violas | -2.4 dB | +4 ms |
| celli | -2.8 dB | +2 ms |
| Flute 1 | -1.4 dB | +40 ms |
| Oboe 1 | -2.0 dB | -15 ms |
| **cor anglais** | -7.3 dB | **+89 ms** (p90 +115), all 29 on Sus MAX |

- No family has an attack brighter than its body, so Dan's "weight, not bite" holds.
- The cor anglais' accent weight comes about 0.4 of an eighth late. The actor's level measure (c24 `acc2.txt`) still has every track but the celli under Dan's +1..+2 dB median. The violins' shortfall is mostly the B staccato before the accented C, which finding 1 makes louder at D / F sharp.

Fix:
- Cor anglais accented notes: per-onset entries in `build/entry_leads.json` "Cor anglais", +0.05 s on the 29 accented onsets. Check pcx / attack centre at -10..+30 ms.
- Re-measure the violin accent medians after finding 1's cut before changing any accent setting.

### Not covered this cycle

Pizzicato and arco changes, the harp, the timpani rolls, con sordino and the re-bows: not re-measured. The c24 attack probe reports no late or hole notes, and c24 changed none of them.

Do not touch:
- the Spiccato route itself (keep the rows, change only the level of the moved notes);
- the orphan groups switched off on Violins I's short rows;
- bar 23's CC11 lift (66.72-67.12) and its 0.10 s lead;
- the bar 38 / 263 lifts;
- Violins II's and violas' 150 ms short-row caps;
- c10's v80 on the celli trio tune and c15's v112 pickups;
- the violins' legato leads (+3..+10 ms);
- Violins II's same-pitch pairs;
- the flute / Oboe 1 accent rows.

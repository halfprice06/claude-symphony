# Cycle 06, critic B (balance and levels), on the c05 render

Material: `cycles/c05/render/` (final stems after c05's Flute 1 and Violin I solo stem fix, and the master), `cycles/c05/metrics/`, `cycles/c05/build_render/parts.json` (the data that was rendered), `build/roles.json`, `build/mix.json`, `build/score_config.py`, `build/mockup-events.tsv`, score pages 2, 5, 7, 10 and 12, and `sections/sC.ily`, `coda.ily`, `retr.ily`, `link.ily`. The c04 stems are deleted, so every comparison here is within c05 or against c05's CHANGES.md.

Method:
- Levels are K-weighted power: the BS.1770 K filter applied to 2048-point spectra every 10 ms, both channels summed, averaged over qn windows on the parts.json tempo map. These are the same kind of numbers as the c03-c05 B reports, not the plain RMS of metrics.md.
- "Peak" is the highest 50 ms mean inside a note. "X over Y" is X's level minus Y's in the same window.
- A simulation scales a stem's frame powers by the proposed role and adds the difference to the master as power (role ramps ignored).
- Each judgement is marked **measured**, **read** (data, code, score or manual) or **inferred**.

## Manual notes (cycle 6, slot B: group B6, PDF pages 32-34, 43, 46, 191-192, read in full; pages 32, 34 and 191 also as images; MANUAL-GAPS.md read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 32-33 | Streaming: the preload size sets how much of each sample sits in RAM against what streams from disk (HDD most, SSD SATA less, PCIe least; "Never Preload" streams all). Multi-threaded reverb and voice renderer, voice-render threads; 1-16 plugin stereo busses. | The 31 Opus instances stream from the USB sample drive; one offline 1x render per cycle; DIGEST §3 reads PreloadSize 1 (SSD SATA), multithreading off, 9 busses. | **Yes (read).** c05 settled at 45 GB with 0 compressed and rendered without the memory gate (CHANGES.md). The render is offline, so streaming speed affects render time, not levels. Output busses are not used for balance (one stereo out per track). |
| 34 | MIDI preferences: the Round Robin "Reset Controller" CC (or a reset note) returns every round-robin cycle to its first rotation. | Every staccato and pizzicato row the scherzo leans on: Stac RRx14, Spiccato RRx9, Staccatissimo RRx16, Stac DblTng RRx9, the timpani rows. | **Partly (read).** This machine's preference is CC16 (DIGEST §3); the pipeline sends CC36 in the pre-roll, which the KS Masters map to the Repetition script's "Reset RR", not to the sample round robins (DIGEST line 43; M1 c14: CC36 did not reset a Stac RRx9 cycle). CC16 is never sent (MANUAL-GAPS #12). Finding 4. |
| 43 | Purge removes samples from memory; purged instruments reload samples as notes play (red / yellow / green states); the rack's volume slider is the same control as the Play page fader and the Mix fader. | Every instance; the instrument volume is one more gain stage besides mix.json gain_db. | **Yes (read).** No purge is used (an offline render from USB needs the samples loaded). Levels are set in parts.json / mix.json and the REAPER envelope, not by the rack slider. |
| 46 | System usage: voices, CPU, RAM, disk; menu commands. | The memory record each actor writes. | **Partly (read).** CHANGES.md records RAM (45 GB settled, 45 / 27-28 GB compressed after) but not voice counts. No balance consequence measured. |
| 191-192 | All Instances window: purge per instrument, articulation selector, **voice limit per instrument** ("a single note can have multiple microphone positions and/or articulations ... raise the Voice Limit" if voices drop), octave transposition, key range. | Patches ship 250 (woodwinds, brass, timpani) and 350 (strings) voices (DIGEST §2.3). The densest voice loads here are the harp's ringing pp chords (346 notes, 73-88, 153-240, 341-361) and the non div. string chords at bars 72, 300 and 339 with 150-350 ms release caps. | **No evidence of dropped voices (inferred).** Octave and key range are untouched (no transposed or split tracks). Nothing in the stems shows a chord note cut short, but this was not measured note by note. |

## Standing checks (Dan's ears), measured on c05

- **Loop pulsing (item 8): none.** Autocorrelation at 3.95 s of the detrended level / 100-300 Hz band / spectral centroid: Violins I 0-23: -0.36 / -0.41 / -0.02; Violins I 1089-1128: -0.05 / -0.17 / -0.06; Violins I 420-445: -0.69 / -0.35 / -0.11; celli 605-624: -0.35 / -0.32 / +0.19; celli 1070-1091: -0.77 / -0.79 / -0.42; Horn 1 1110-1128: -0.48 / -0.31 / -0.07; Horn 4 drone 456-504: -0.12 / -0.01 / -0.02; master 1089-1128: -0.25 / +0.17 / -0.19.
- **S3 (measured).** Master in 50 ms frames from 0.2 s before the bar line: qn 360 -30.3, -30.3, -33.4, -33.4, -32.5, -30.1 ...; qn 828 -31.6, -36.0, -38.1, -38.2, -35.9, -34.6 ...; sfp qn 900 -13.6, -17.3, -18.1, -16.2, -19.0, -20.6, -20.0, -21.8, -24.4, -26.9. No step to silence at any of them.
- **Timpani rolls (priority 5, measured).** Roll level against the loudest other stem, 1.5 qn windows: bar 101 4-8 dB under; 129 6-10 under; 205-208 (pp < f printed) grows from 0.3-5 under to 0.6 under at the f arrival; 237 8-14 under; 285 6-10 under; 303 8-9 under; 332 10-11 under; 336 9 under. The rule holds everywhere.
- **c05 B fixes (from c05 CHANGES.md, consistent with these numbers).** Flute 1 G6 -2.4 / -1.5 dB under Violins I; coda build Violins I +9.4..-2.5 over Violins II; Oboe 1 at 828-840 0.7-5.7 under Flute 1, 345-348 3.4-6.2 over Clarinet 1; bass clarinet under Violins I at 744-753; celli -4.9..+0.6 against Violins I at 132-156.

## Findings, ranked by what a listener would hear

### 1. Coda theme in three octaves, bars 333-338 (qn 996-1014): Violins II's middle octave is louder than Violins I's top line, and the violas' bottom octave is buried under the held horns (measured)

**Score (read, page 12 and coda.ily).** In 333-335 the theme head is ff in three octaves of strings: Violins I E6, Violins II E5, violas E4 (with the woodwinds), over a held ff horn chord. coda.ily's own note on this passage: in a ff melody in octaves over held brass the lowest octave carries the violas, and "the violas' E4 sat alone under four ff horns" (c084). 336-338 is the fff summit, with the same three octaves.

**Measured (1.5 qn windows):**

| qn | 996 | 997.5 | 999 | 1000.5 | 1002 | 1003.5 | 1008 | 1009.5 |
|---|---|---|---|---|---|---|---|---|
| Violins I | -23.5 | -22.6 | -22.0 | -24.1 | -21.3 | -19.2 | -18.2 | -18.5 |
| Violins II | -22.2 | -20.1 | -19.5 | -22.4 | -19.0 | -17.0 | -15.4 | -18.4 |
| violas | -34.2 | -33.1 | -29.0 | -28.3 | -29.9 | -29.5 | -23.6 | -22.0 |
| Horn 1 | -25.0 | -25.2 | -26.4 | -27.0 | -26.9 | -27.2 | -24.8 | -24.2 |
| Horn 4 | -26.9 | -28.4 | -42.0 | -57.8 | -66.6 | -44.2 | -28.9 | -30.8 |

- Violins II sit 1.3-2.8 dB over Violins I in every window of 333-335 and at 1008. Per bar, Violins I minus Violins II: 333 -2.0, 334 -2.3, 335 -2.3, 336 +3.3, 337 -1.7, 338 +1.8. In the espress. octave passages the same two sections measure Violins I +5.8 (bars 45-56), +5.9 (121-131) and +5.5 (209-224).
- The violas are 7-12 dB under Violins II and 2-9 dB under Horn 1 alone. Horn 1, holding a chord tone, is the third loudest stem in bars 333-334, 5-6 dB over Horn 2 on the same chord (Horn 2 -30.8..-33.4).
- Per note, the cause is the row: Violins II's "Spiccato RRx9" plays over Violins I's "Stac RRx14" an octave higher at the same velocity and CC11 (997: -21.7 against -29.1; 997.5: -21.2 against -23.0; 998: -16.9 against -21.3). On the shared Sus MAX note at 999 Violins II is still 2.9 dB over. The violas' "Staccatissimo RRx16" peaks at -32..-35.

**Read.**
- parts.json `row_trimmed` is empty for Violins I, Violins II and violas over 900-1017: `ROW_TRIM_DB`'s string branch needs a Leg-row note within 3 qn, so the tables' -3 / -3 / -4 never apply here (the c05 lesson, which c05 fixed only for the build at 984-995.5).
- roles.json carries c01's summit stem-fix cuts: Violins II [996, 1016, -2], violas [996, 1016, -3]. The violas' -3 was a limiter fix when the summit overshot; it now costs the bottom octave.

**Judgement (inferred).** The listener hears the theme's middle octave as the tune, the top line duller than in every other octave doubling of the movement, and the four horns where the score asks for the violas.

**Fix.** `build/roles.json`, all adding to the existing rows:
- "Violins II": `[996, 1004.75, -3]`, `[1008, 1011, -3]`.
- "Violas": `[996, 1016, 3]` (cancels c01's -3) and `[996, 1004.75, 1]`.
- "Horn 1": `[996, 1014, -3]`.

**Target (simulated).**
- Violins I over Violins II +1.7..+3.0 dB in 996-1004.75, about +0.2..+2.9 at 1008-1011.
- Violas -24.3..-30.2 in 333-335: 3-5 dB under Violins II and level with or over each horn.
- Horn 1 -27.8..-30.2, level with Horns 3-4.
- Master -0.3..-1.1 dB over 996-1004.75 and within ±0.3 dB at 1005-1012, so the summit's margin over bars 333-335 grows a little. The fff downbeat (1005) is untouched.
- Re-measure the Violins II and violas pair dips at 997 / 1003 (a flat role should leave them unchanged).

### 2. In the ff tutti theme and the ff arrivals, Violins II sit level with or over Violins I (bars 113-120, qn 336-357; bar 72, qn 213; bar 300, qn 897), and Clarinet 1 reaches the violins' level on the held ff chords (measured)

**Score (read, page 5 and sC.ily).** From bar 113 to 120 Violins II play the theme an octave under Violins I (bars 105-112 are unison, as is the whole reprise statement 305-320). Bars 72 and 300 are one-bar ff tutti chords before a sudden drop (bar 72 into the pp F major episode, bar 300 into the sfp).

**Measured.**
- Violins I minus Violins II per bar, 113-120: +1.6, -1.5, +1.4, 0.0, +1.2, +2.1, -1.1, -2.1 dB (mean +0.2). In the espress. octave passages the same pair reads +5.5..+5.9 (finding 1).
- Per note at 336-342, Violins II's "Spiccato RRx9" (G4-D sharp 4) peaks at -19.0..-22.2, Violins I's "Stac RRx14" an octave up at -19.1..-22.7. `row_trimmed` holds only 357 in 312-360.
- Bar 300 (qn 897-899, 1 qn windows): Violins II -18.3 / -15.7 / -22.5, Violins I -21.3 / -18.8 / -21.7, Clarinet 1 -18.9 / -18.6. Clarinet 1 is the second loudest stem of the ff arrival.
- Bar 72 (qn 213-216): Violins II -19.6 (a non div. double stop), Violins I -22.5, Clarinet 1 -22.7 (its held C sharp 6, Leg Slur Rep, CC1 108, envelope +3.5), Flute 1 -24.1, Oboe 1 -25.8.

**Judgement (inferred).** Where the score doubles the tune at the octave, the lower octave carries it and the top line loses its edge; the same row imbalance as finding 1. At bars 72 and 300 a single clarinet stands out of the tutti chord at the level of a full violin section (the problem c01 B #3 fixed at 104/304, not at these two bars).

**Fix.** `build/roles.json`:
- "Violins II": `[336, 357, -3]`, `[213, 216, -2.5]`, `[897, 900, -2.5]`.
- "Clarinet 1": `[213, 216, -3]`, `[897, 900, -3]`.
- Leave 312-336 and 912-960 alone: there the sections play in unison.
- A generic alternative is to let `ROW_TRIM_DB`'s string branch also trim staccato rows inside `ART_SPANS` that have no Leg neighbour. That would drop all four tutti string sections by 3-4 dB at once (and the violas are already the weakest), so the roles are the safer change.

**Target (simulated).** Violins I over Violins II +1.5..+5.1 dB in 113-119 (mean about +3.5); bar 300 Violins I level with or 0.6 dB over Violins II and 0-2 dB over Clarinet 1; bar 72 Violins I level with Violins II and 3 dB over Clarinet 1. Master -0.4..-1.0 dB in 113-119 and -0.4..-0.5 at 72 / 300, which adds about 0.4 dB to the delivered summit's margin over bar 300 (2.0 dB in c05).

### 3. Two of the trio's p solo phrases are 4-7 dB softer than the solos around them: Oboe 1 in bars 185-188 and Bassoon 1 in bars 233-236 (measured)

**Score (read, page 7, events).** 185-188: Oboe 1 "1. espress." p over the harp's pp chords and pp pizz. basses; at 189 the celli take the phrase on, p dolce. 225-236 (codetta): Oboe 1, Clarinet 1 and Bassoon 1 pass the dolce line on every four bars, each p.

**Measured (whole phrase, and the next two stems):**

| phrase | printed | solo | master | next stems |
|---|---|---|---|---|
| Clarinet 1, 153-168 | p dolce | -37.4 | -35.7 | harp -43.7, Horn 4 -46.4 |
| **Oboe 1, 185-188** | **p espress.** | **-43.1** | **-41.3** | harp -47.0, basses -53.1 |
| celli, 189-192 | p dolce | -37.7 | -36.6 | harp -46.0 |
| Oboe 1, 225-228 | p dolce | -37.5 | -34.9 | Violins II -43.7 |
| Clarinet 1, 229-232 | p dolce | -37.3 | -35.5 | violas -42.9 |
| **Bassoon 1, 233-236** | **p dolce** | **-41.4** | **-39.1** | harp -46.1, Horn 4 -47.3 |
| Horn 3, 341-344 | p dolce | -38.2 | -36.2 | violas -43.5 |
| Oboe 1, 345-348 | p dolce | -35.9 | -33.2 | harp -41.0 |

- In 1.5 qn windows over 185-188 the oboe is only 0.4-2.2 dB over the pp harp in four of eight windows (553.5 +1.7, 556.5 +2.2, 558 +0.5, 562.5 +0.4).
- At 189 the celli enter 5.4 dB louder than the oboe phrase they continue.
- At 233 Bassoon 1 enters 5.2 dB under Clarinet 1's last bar (693: -36.2 -> 696: -41.4), although roles.json already gives it [696, 711, +2].

**Read.** c05 raised Oboe 1 at 672-676.5 and 1032-1041 (+4 each) but not at 552-564; Oboe 1 `gain_db` -5.3, p trim 5.

**Judgement (inferred).** The trio's middle part sounds like a drop in level rather than a new colour, and the oboe's espress. line sits on the harp instead of over it. In the codetta the line seems to fade when it reaches the bassoon.

**Fix.** `build/roles.json`: "Oboe 1" `[552, 564, 4]`; "Bassoon 1" `[696, 708, 3]` (adds to the existing +2).

**Target (simulated).** Oboe 1 -37..-43 per window, 4-9 dB over the harp and within 1-2 dB of the celli at 189; master in 185-188 about -37.5 (from -41.3), level with the clarinet's tune at 153. Bassoon 1 -36.8..-40.5, 1-3 dB under Clarinet 1's phrase and 6-9 dB over the harp and Horn 4.

### 4. The sample round robins are never reset by the controller Opus listens to, so fitted per-onset levels may not carry from one render to the next (read; effect inferred, low priority)

**Read.** Manual p.34: the Round Robin "Reset Controller" set in Opus's MIDI preferences returns every round-robin cycle to rotation 1. This machine's preference is CC16 (DIGEST §3). `build_reaper.py` sends CC36 in the pre-roll (`RR_RESET_QN`), which the KS Masters map to the Repetition script's reset, and M1 c14 measured that CC36 did not reset a Stac RRx9 cycle. CC16 appears in no patch map and is never sent (MANUAL-GAPS #12).

**Why it matters for balance (inferred).** The theme heads, the coda pairs and the ff tutti all play on RRx9-RRx16 rows, and several level tables are fitted per onset on one render (accent fits, the Marc LITE head steps, the stem-fix roles). If the restart does not return every cycle to rotation 1, the next render can play a different round-robin sample on the same note. c04's LEARNINGS records a 24 ms render-to-render change in the violas' legato spread with identical data.

**Fix.** In `tools/build_reaper.py`, send CC16 = 127 at the pre-roll point where CC36 is sent now, on every track, and keep CC36. Check: after the c06 render, compare per-note peaks of an unchanged passage (Violins I 36-84 if its data does not change this cycle) against c05; the round-robin order should match note for note.

## Do not touch

The timpani roll levels and `TIMP_DAMP_AT` (every roll stays under the texture except at printed crescendo arrivals); c05's flute ff staccato trim and G6 roles; the coda-build string roles at 984-995.5; Oboe 1's `LEVEL_SHAPES` at 827.5-840.5 and the +4 roles at 672 and 1032; the bass clarinet's [732, 756, -5]; the sfp roles at 900-906; the celli's [132, 156, -3]; the Violin I solo +8 role and the DIV shelves; the harp caps; the hall settings (fx 0.095, 160 Hz low cut, ir_setup 0.7 / 0.7).

# Critic B, cycle 5 (render c04): balance and levels

## Manual notes (MANUAL-READING row c5 B: May 2021 HO manual PDF pages 32-34, 43, 46, 191-192, read in full; MANUAL-GAPS.md read; Opus `Preferences.json` read)

| Page | What the manual says | Where it applies in this mockup | Does the render follow it? |
|---|---|---|---|
| p.32 | Streaming: the Default Preload Size (HDD / SSD SATA / SSD PCIe) sets how much of each sample sits in RAM. Never Preload streams everything and needs RAID-0 NVMe. | Every instance. Preferences.json: `PreloadSize` 1 (SSD SATA), `NeverPreload` false. KIT §11 kept 1 on purpose, because the late entries of earlier renders came from memory pressure, not the drive. | Yes. c04 settled at 45 GB with 0 GB compressed and rendered with 0 probe flags. A larger preload would need more RAM, and the project is already at the 45 GB limit (below). |
| p.33 | Multi-threading: threaded reverb, threaded voice renderer, number of render threads. Output configuration: 1-16 plugin stereo busses. | Preferences.json: `UseMultiThreadedReverb` false, `RenderMultiThreaded2` false, `NumVoiceRenderThreads` 1, `PluginStereoOuts` 9. Each track uses one stereo output. | Followed in effect. A 1x offline render does not need threading, and threading could change timing between renders (inferred). Leave it. |
| p.33-34 | Audio Drives: set each drive's type. Slower drives need more RAM. Several streaming drives avoid bottlenecks. | All samples stream from one external drive (`/Volumes/MAC DRIVE`). | Not a balance factor. Timing passed (probe 0 flags), so no bottleneck was measured. |
| p.34 | MIDI channel assignment (Auto Increment or Omni). Round Robin: a Reset Controller CC or a Reset Note returns every round-robin cycle to its first rotation. Program Change to Articulation. | Preferences.json: `RoundRobinResetCC` 16, `RoundRobinResetNote` -1, `ProgramChangeToArticulation` false, `AutoAssignMidiChannel` 0. One instrument per instance and keyswitches only. **The Finale's `tools/build_reaper.py` (lines 779-806) sends only CC36 in the pre-roll. Movement I c43 added `RR_RESET_CC` (CC16, read from the preference) next to CC36** (mvt1 `tools/build_reaper.py` lines 790-831). | **Partly.** CC16 is never sent. Measured effect: small (render-to-render check below). On unchanged data, c03 against c04 differs by a median of 0.00-0.14 dB per beat on 29 of 31 stems. The five instances that were not rebuilt (Contrabassoon, Timpani, crash, bass drum, harp) differ by 0.00-0.11 dB, with 0 % of beats over 1.5 dB. So the CC36 reset plus the strings' Repetition-off already makes these renders repeatable. Port CC16 when a cycle refits per-note tables anyway: MANUAL-GAPS #6 and mvt1 c43 say it reshuffles the takes once. |
| p.43 | Purge All Instruments / All Instances removes samples from RAM. Samples then load as notes play (yellow), and the instrument is green when fully loaded. | The pipeline never purges. `UNLOAD_UNUSED_ROWS` removes unused rows instead. | Yes. A purged instance in a 1x offline render would load samples during the render, which is the late-entry risk of KIT §11 (inferred). Do not use purge as a memory saver. |
| p.46 | System Usage: voices, CPU, RAM, disk in real time. | Not readable from scripts. The pipeline records REAPER's footprint in `metrics/memory.txt`. | Followed with the footprint. **Memory record:** settled 41 (c00) -> 43 -> 44 -> 44 -> **45 GB (c04)** with 0 GB compressed, and 46 GB after the render (26-28 GB compressed by macOS; a 6 GB CrashRestartHelper and 6.8 GB of Steam processes were also resident). c04 is at the brief's 45 GB limit, so every fix below is a level change (roles, no new rows). |
| p.191 | All Instances window: per-instrument purge state and the articulation selector for KS Masters. | Same as p.43. | Nothing to change. |
| p.192 | Voice Limit per instrument: notes with several mics or rows add voices, and at the limit voices are stolen. Octave transposition and Key Range. | Preferences.json `InstrumentVoiceLimitMax` 1024. The per-instance limits are inside the binary `.oib` / plugin state and were not read. Dense chords: div. a 3 tremolos and the final chord, harp chords. | Not measured directly. No level finding below depends on a dropped voice: the final-chord levels match c03 to within 0.2 dB on unchanged data. Critic A's row (p.160-162) covers voice limits. |

MANUAL-GAPS.md: #6 (round-robin reset on CC16) is covered by the p.34 note. No open gap is a better fix than roles for the findings below. Memory rules out new rows this cycle.

## Method

- **Data.** The c04 stems and master. `cycles/c04/rendered_build/parts.json` and `mix.json` are identical to `build/` (cmp). The tempo map comes from parts.json (`tools/pcx.py` TM).
- **Levels.** A 4096-point STFT with a 25 ms hop, stereo power, K-weighted by the BS.1770 curve applied as a power response, plus six bands. "re M" means stem (or group power sum) minus master over the same span.
- **Per-beat pairs.** A track is counted on a beat when its notes cover at least 0.9 qn of it. Offsets per printed dynamic come from least squares over every same-dynamic pair.
- **Pizzicato.** For each pluck, the peak K frame in -0.03..+0.15 s, minus the solo's mean K level over the surrounding 1 qn. Beats where the solo is silent are skipped.
- **Render variance.** Per track and beat, a beat is compared only when notes, keyswitches, CC1/11/7/15/70 lanes (qn-3..qn+1) and the volume envelope (within 0.05 dB) are identical in c03 and c04.
- **Simulations.** Each stem's frame power is scaled by the proposed dB over the span. The master is rescaled by the change in the stem sum.
- **Score pages read.** 3, 5, 7, 10, 13, 14, 15, 16.
- **Dan's checks through this lens:**
  - Items 5 and 7: the timpani rolls in every listed span rank 8-22 among the stems (-13.3..-20.4 re M), so none covers anything.
  - S3: a scan of all volume envelopes for falls of 3 dB or more within 0.12 s under a sounding note found only accent-swell tails, the timpani settle and the basses' detach dips (all by design).
  - Every fix below is a role row that starts on an onset or in silence, and none ends with a fall under a held note.
  - S1, S2: no timing or length change.
- **Cross-family consistency at each printed dynamic (measured, no finding).** At p, all winds fall within ±2.6 dB of the mean (Trumpet 3 -4.6). At f and ff, trumpets and trombones sit 2-4 dB over the woodwinds, and horns 1-3 dB over them. This matches the Rimsky norm, so p sounds like p across families on sustained notes. The exceptions are the pizzicato accompaniments (finding 2) and two local tuttis (findings 1 and 3).

## 1. Bars 255-258 (qn 1016-1032): the returning F2 phrase (Hn 3-4 a2, Vln II, Vla, Vc, "espress." ff) is level with or under its held accompaniment; the celli drop out of it (measured)

**Where.**
- Bars 255-256 (1016-1024): the phrase against the low brass (B.tbn and Tuba held ff whole notes) and the Violins I tremolo chord.
- Bars 257-258 (1024-1032): the phrase against the held woodwind chords (f < ff) and Trumpet 1's held a2 whole notes.

**Evidence (K, group power sums re M, c04).**

| qn | melody (Hn3+Hn4+VlnII+Vla+Vc) | B.tbn+Tuba | Vln I | Tpt 1 | woodwinds | Vc alone |
|---|---|---|---|---|---|---|
| 1016-1018 | -3.1 | -4.6 | -11.1 | -10.7 | -24.1 | -12.9 |
| 1018-1020 | -4.9 | -4.9 | -8.0 | -11.3 | — | -14.5 |
| 1020-1022 | **-6.4** | **-4.2** | -7.1 | -11.7 | — | -14.8 |
| 1022-1024 | -4.8 | -5.6 | -7.8 | -12.6 | — | -14.2 |
| 1024-1026 | -3.5 | -8.6 | -11.4 | -8.8 | -9.5 | -15.9 |
| 1026-1028 | -5.6 | -7.9 | -11.6 | -6.8 | -8.2 | -18.8 |
| 1028-1030 | **-6.8** | -9.6 | -13.3 | -6.8 | **-6.0** | -17.0 |
| 1030-1032 | **-7.2** | -11.4 | -15.8 | -8.8 | **-5.3** | -22.0 |

- The five melody stems together are under two low-brass stems in bar 256, and under the woodwind chord in bar 258. On its own, the Violins I tremolo chord (-7.1) is the loudest single stem at 1020-1022.
- Within the phrase, the notes after the head fall 5-11 dB under it:
  - Hn 3: head -21.3, then -29.4 / -32.4 dB on C3-E3;
  - Vc: -27.1, then -32.2..-38.4;
  - Vln II: -23.7, then -27.6..-33.4.

  The head carries the `<>` hairpin lift (vol +5.8 on the strings, +9 on Hn 3). After it the envelope is back to +1..+2.
- Cause in the tables:
  - The bass-octave rows `Bass trombone` / `Tuba` `[988, 1020, 3.0, 4]` (c01 C #1) still hold +2.9..+0.9 dB over 1016-1020, inside the phrase.
  - The melody roles are only +2 (Vla, Vc, Vln II) and +3 (Hn 3-4), and the celli need more because of their gain -4 / ff trim -2.5.
- c03 gives the same picture (melody -5.9 against low brass -4.6 at 1020-1024; -6.9 against winds -6.0 at 1028-1032), so this is not render variance.
- By the norm, an accompaniment at the same printed dynamic as the melody is cut 3-7 dB (KIT §13). Here it is level or louder.

**Fix (`build/roles.json`).**
- Bass trombone and Tuba:
  - `[988, 1020, 3.0, 4]` -> `[988, 1016, 3.0, 2]`;
  - new `[1016, 1032, -3.0]`.

  1016 and 1032 are onsets on both tracks. The step back up at 1032 is onto a new note.
- Violoncellos `[1016, 1032, 2]` -> `[1016, 1032, 6]`.
- Violas `[1016, 1032, 2]` -> `[1016, 1032, 4]`.
- Violins II `[1016, 1048, 2]` -> `[1016, 1032, 4]` and `[1032, 1048, 2]`.
- Horn 3 and Horn 4 `[1016, 1048, 3]` -> `[1016, 1032, 5]` and `[1032, 1048, 3]`.
- Violins I `[1016, 1048, -2]` -> `[1016, 1024, -4]` and `[1024, 1048, -2]` (1024 is a Vln I onset).
- Flute 1, Flute 2, Oboe 1, Oboe 2, Clarinet 1, Clarinet 2: new `[1024, 1032, -2, 2]`. The end ramp opens over the last 2 qn of their printed crescendo to ff at 259.

**Expected (simulation, same groups).**
- Melody -1.4 / -2.5 / -3.6 / -2.7 / -2.0 / -3.7 / -4.5 / -5.0 in the eight spans above.
- Low brass -9.2 / -8.5 / -6.8 / -8.7 / -12.2 / -11.0 / -12.6 / -14.3.
- Woodwinds -12.1..-7.2. Vc -8.6..-17.9.
- The melody leads every accompanying group by 2-7 dB.
- Master -0.4..+0.7 dB per 2 qn. Bars 223 and 278 stay the loudest.

## 2. The pp pizzicato accompaniments under the three soft solos: basses and celli pluck at or over the solo's level, violas 4-6 dB under their Violins II partner (measured)

**Where.**
- Bars 51-66 (qn 200-264) under Trumpet 1's p solo: Vln II and Vla pizz. div. off-beat chords; Vc and Cb pizz.
- Bars 117-122 (456-488) under the bassoon solo: the same layout.
- Bars 171-186 (680-744) under the cor anglais and muted Trumpet 1: Cb and Vc pizz quarters, violas' slurred eighths.

**Evidence (pluck peak minus the solo's level, median / p90 / max dB, c04).**

| span | Vln II | Violas | Violoncellos | Double basses |
|---|---|---|---|---|
| 200-264 vs Tpt 1 | -4.6 / -1.6 / +0.9 | -9.9 / -5.0 / -4.6 | -4.3 / **+0.8** / +2.6 | -3.3 / **+1.0** / +1.4 |
| 456-488 vs Bn 1 | -6.6 / -2.7 / -1.3 | -9.7 / -8.0 / -4.2 | -4.8 / **+3.8** / +4.4 | -5.4 / **+2.6** / +5.2 |
| 680-744 vs CA | — | -12.9 / -8.3 (arco eighths) | -6.0 / **+1.5** / +4.5 | -3.2 / **+1.0** / +1.6 |

- One pluck in ten of the bass line reaches or passes the solo's level, in all three passages.
- c03 gives the same numbers (Cb -3.3 / +1.0 at 200-264; Cb +4.9 p90 at 456-488 before c04's -3 row), so this is not render variance.
- Cause:
  - `build/mix.json` Double basses `soft_trim_db` pp +8.5 and Violoncellos pp +4. These were set so that held pp bass notes are audible, and they also lift every pp pluck.
  - Only Vln II (201-264, -3), Cb (464-488, -3) and Vc (-1 at 200-264 and 680-744) carry rows.
- In the same off-beat chords, the violas' pizz. pp (the lower half of the four-voice chord) sit 4-6 dB under Vln II (5-7 dB before Vln II's -3 row) despite their soft trim +6. The chord is top-heavy and the bass thumps.
- By the norm, a pp plucked accompaniment sits well under a p solo (KIT §13; c04 B #4).

**Fix (`build/roles.json`; all start in silence or on the first pizz onset, so a 0.5 qn ramp-in completes before the first pluck).**
- Double basses:
  - new `[200, 264, -4.0]` (first pizz 200.0, previous note ends 198.88; arco at 264);
  - new `[680, 744, -4.0]` (first pizz 680.0, previous note ends 678.86; arco at 744);
  - `[464, 488, -3.0]` -> `[456, 488, -5.0]` (first pizz 456.0).
- Violoncellos:
  - `[200, 264, -1.0]` -> `[200, 264, -3.0]`;
  - `[680, 744, -1.0]` -> `[680, 744, -3.0]`;
  - new `[456, 488, -3.0]`.
- Violas: new `[201, 264, 3.0]` and `[457, 488, 3.0]` (first pizz onsets; previous note ends 198.88 / 454.86).

**Expected.**
- Cb p90 +1.0 -> -3.0 under the trumpet, +2.6 -> -0.6 under the bassoon (with the -5 row), +1.0 -> -3.0 under the cor anglais.
- Vc p90 +0.8 -> -1.2, +3.8 -> +0.8, +1.5 -> -0.5.
- Violas -9.9 -> -6.9 (2.3 dB under Vln II instead of 5.3).
- Simulated spans: pizz group re M 200-232 -8.3 -> -9.5; Trumpet 1 -3.0 -> -2.8; CA 680-712 -2.6 -> -2.3. Master -0.1..-0.25 dB (the delivery ride lifts these spans anyway).

If the basses' pizz sounds too thin after this, the fallback is a lower pp soft trim on the "Pizz RRx4" row only (a row-specific trim in `score_to_parts.py`, inferred), not the whole pp trim, which the held pp notes need.

## 3. Codetta, bars 91-94 (qn 360-376): Tuba and bass trombone are the two loudest brass stems; the three trumpets ("codetta with trumpets") are 1-3 dB under them (measured)

**Where.** The ff tutti chords of bars 91-94. Trumpets 1-3 play the chord top in the hammered rhythm (notes 360-374). Tuba and B.tbn are on the bass.

**Evidence (re M).**

| qn | Tuba+B.tbn | Tpt 1-3 | Horns 1-4 | Tuba alone |
|---|---|---|---|---|
| 360-364 | -7.9 | -10.0 | -12.7 | -10.1 |
| 364-368 | -7.0 | -9.9 | -12.7 | -9.2 (loudest stem) |
| 368-372 | -8.0 | -10.8 | -12.6 | -11.0 |
| 372-376 | -7.4 | -8.4 | -12.0 | -10.1 (loudest stem) |

- In every other ff tutti, the trumpets lead the low brass:
  - 436-452: +1.4..+3.1;
  - 584-600: +2.3..+7.0;
  - 792-816: +1.0..+2.4;
  - 888-892: +4.2;
  - 1088-1113: +2.5..+6.3.
- The codetta is the exception because of the bass-octave rows Tuba / B.tbn / Cb / Cbn `[360, 380, 3.0, 4]` (c01 C #1).
- c03: -7.1..-8.2 against -7.8..-10.3, the same order. c04's Trumpet 2 ff trim (-2 dB) took about 0.5 dB more off the trumpet group here.
- Pair offsets at ff over the whole piece put Tuba and B.tbn level with the trumpets (+2.6 / +3.3 against +1.9..+3.1). Adding +3 dB on top makes this chord bottom-heavy.

**Fix (`build/roles.json`).**
- Tuba and Bass trombone `[360, 380, 3.0, 4]` -> `[360, 380, 1.0, 4]`. Keep the Cb and Cbn rows, which carry the low octave.
- Trumpet 1, Trumpet 2, Trumpet 3: new `[360, 376, 2.0]` (360 onset; last note ends 374; the next trumpet entry is later).

**Expected (simulation).**
- Tuba+B.tbn -9.9 / -8.9 / -10.0 / -9.5.
- Trumpets -8.0 / -7.8 / -8.7 / -6.5: level with or over the bass, the horns unchanged.
- Master within ±0.1 dB.

## 4. Bar 263 (qn 1048): the fff crash is the loudest stem by 3.3 dB and holds 55 % of the master's 2-6 kHz energy, more than at the main climax (measured; dominance inferred)

**Where.** Crash cymbals at 1048 (bar 263, fff, the climax of the Più allegro), compared with 888 (bar 223) and 1108 (bar 278). All three strokes are pitch 60 at velocity 124 with no volume rows.

**Evidence.**
- Crash re M over the first 2 qn: 888 -10.3 (equal with Trumpet 1 -10.6), **1048 -7.6 (next stem Tuba -10.9)**, 1108 -9.1.
- The crash's share of the master's 2-6 kHz band: -5.7 dB at 888, **-2.6 at 1048**, -4.8 at 1108. The 6-20 kHz share is -0.4..-1.1 at all three (a crash carries that band, as it should).
- At 1048 the orchestra is 1.6 dB quieter than at 888 (M -6.7 against -5.1). That is correct, since 223 and 278 are the climaxes. The crash at the same velocity therefore stands further out, over the brass's presence band, for about one beat.
- c03 measured the same (crash -8.6 at 1048-1050, -11.2 at 888-890).

**Fix (`build/roles.json`).** Crash cymbals new `[1046, 1060, -3.0]`. The track is silent before 1048, so the ramp is complete. The row holds through the ring, so the hall tail is not cut (S3).

**Expected.**
- Crash re M -11.5 / -10.9 over 1048-1050, level with Tuba, Trumpet 1 and Trumpet 3 (-10.2..-11.7); 2-6 kHz share about -5.
- Master -0.3 dB for one beat. Bar 263 stays below 223 and 278.

## 5. Render repeatability and the CC16 reset (measured; low priority for listeners)

**Where.** All tracks: `tools/build_reaper.py` `item_lua` pre-roll resets.

**Evidence.** c03 against c04, beats with identical data, stem minus stem (median / p10 / p90, share of beats over 1.5 dB):
- Instances not rebuilt in c04: Contrabassoon +0.05 / +0.02 / +0.17 (0 %), Timpani +0.11 / +0.06 / +0.21 (0 %), crash, bass drum and harp 0.00 (0 %).
- Rebuilt tracks: winds and horns -0.14..+0.01 median, 0-5 % over 1.5 dB. Strings -0.00..+0.36 median, 1-5 % over 1.5 dB.
- Trumpet 2's -0.82 median is its c04 ff trim change, which lives in mix.json and is not in parts.json, not variance.
- The isolated large beats are all on tracks rebuilt with a new state (string release caps, new staccato rows): Flute 1 qn 520 +7.8, Violins II 520 -7.6 and 1057 -7.1, Clarinet 2 1087 -10.2, Violoncellos 146 +6.3. They are state effects, not round robins.
- Opus resets round robins on CC16 (`RoundRobinResetCC` 16, manual p.34 with the 2025 correction). The Finale sends only CC36, which every KS Master maps to the Repetition script's "Reset RR".

**Fix.** Port Movement I's `_opus_rr_cc()` / `RR_RESET_CC` block (mvt1 `tools/build_reaper.py` lines 790-831; it reads Preferences.json and sends CC16 = 127 at `RR_RESET_QN` next to CC36). Do it in a cycle that refits per-note tables, and compare per note with the render before. Mvt1 c43 measured a one-time 1-14.5 dB change on some brass legato targets, and repeatability within 0.15 dB from the next render on (mvt1 c46 B). Not urgent: the current renders already repeat closely enough that no finding above is variance.

## Do not touch

- The cross-family balance at p, f and ff (pair offsets in Method).
- Solos over their accompaniment by span:
  - Trumpet 1 at 51-66: -2.5 re M;
  - Bassoon 1 at 115-122: -3.0;
  - harp solo at 123-134: -4.0;
  - cor anglais -3.2 with muted Trumpet 1 -6.5 at 171-186.
- F2 in E flat, 67-82: Vln I -5.4, Vln II -7.3, harp -10.2.
- M, 187-197: Vln I -4.6, Vln II -6.9.
- F1 in the bass at 27-34: Tuba -7.2, Hn 3 -7.6, Cb -9.0 over the countersubject -10.8.
- Theme B, 211-218: Trumpet 1 -6.7 over Trumpet 2 -7.6.
- The chorale:
  - 224-225: brass -1..-2 over the mf tremolo;
  - 226-230: the ff tune +2.6..+3.4 over the f brass;
  - 231-233: brass on top.
- The Più allegro's two theme groups at 247-254 (within 1-3 dB of each other, the bass 2-5 dB under).
- The arrival at 223: trumpets -6.2 over low brass -10.4, timpani -19.2, bass drum -19.5 at the stroke.
- The final chord: trumpets -6.5, low brass -10.4.
- The timpani roll trims (rank 8-22 in every roll).
- The bass-octave rows outside bars 91-94 and 255-256.
- The c04 final-chord, Vln II doubling and inner-voice rows.
- The hall, release caps and `UNLOAD_UNUSED_ROWS`. Memory is at 45 GB, so add no rows or instances in the main project.

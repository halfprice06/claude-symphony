# Cycle 11, critic B (balance and levels): report on the c10 render

## Manual notes (MANUAL-READING row c11 B = the c5 B row: May 2021 HO manual PDF pages 32-34, 43, 46, 191-192, read in full; second reading; c05 B's table checked; MANUAL-GAPS.md read; Opus `Preferences.json` read)

| Page | What the manual says | Where it applies here | Does the c10 render follow it? |
|---|---|---|---|
| p.32 | Streaming: Default Preload Size (HDD / SSD SATA / SSD PCIe) sets how much of each sample sits in RAM; Never Preload needs RAID-0 NVMe. | Every instance. Preferences.json unchanged since c05: `PreloadSize` 1, `NeverPreload` false. | Yes. c10 settled at 45 GB with 38 GB compressed before the render (34 GB after). The repeatability check below shows the render was not hurt by it. Keep 1 (KIT §11: more preload means more memory). |
| p.33 | Multi-threaded reverb and voice renderer, render threads; plugin stereo busses. | `UseMultiThreadedReverb` false, `RenderMultiThreaded2` false, `NumVoiceRenderThreads` 1, `PluginStereoOuts` 9. The Opus reverb is off on every track since c06, so the reverb thread setting no longer matters. | Followed in effect. A 1x offline render does not need threading. Leave it. |
| p.33-34 | Audio drives: drive type sets the RAM/stream ratio; several streaming drives avoid bottlenecks. | All samples stream from one external exFAT drive. | Not a level factor here. The probe flagged only the known Vc qn 24 artefact. |
| p.34 | Round Robin: a Reset Controller CC (or note) returns every round-robin cycle to its first rotation. | `RoundRobinResetCC` 16. Since c08 the basses get CC16 at five span starts (parts.json `cc16`). The pre-roll still sends CC36 only (`tools/build_reaper.py` lines 939-944), and CC36 is the Repetition script's "Reset RR", not Opus's reset (LEARNINGS c08). | Partly, and the gap costs nothing measurable. On the 122 bars whose notes, keyswitches, CC lanes and envelope points are identical in c09 and c10, the master matched c09 per bar with median 0.00 dB, p90 0.32 dB. Most moves over 0.3 dB come from level changes that are outside parts.json's lanes: the trumpets' ff trims (bars 94, 110-112, 216) and the role / trim rows (bar 44 = Vln I harmonic -8). The unexplained ones (bar 106 -1.34 dB, 154 -0.64, 195-196 ±0.35) are all bars where the fully rebuilt Bassoon 1 plays, which fits Movement I c47 (a rebuild changes an instance's state). A pre-roll CC16 is not needed for repeatability. |
| p.43 | Purge All Instruments / All Instances: samples then load as notes play (yellow), green when fully loaded. | The pipeline never purges. `UNLOAD_UNUSED_ROWS` unloads rows instead. | Yes. A purge before a 1x render would load samples during the render, the late-entry risk of KIT §11 (inferred). Do not use it to save memory. |
| p.46 | System Usage: voices, CPU, RAM, disk. | Not readable from scripts. `metrics/memory.txt` records REAPER's footprint. | Followed: 45 GB settled, 45 after, compressed 38 -> 34 GB. That is at the brief's limit, so every fix below is a level change with no new rows or instances. The one exception is the optional velocity in finding 5, which loads nothing. |
| p.191 | All Instances window: per-instrument purge state and the articulation selector. | Same as p.43. | Nothing to change. |
| p.192 | Voice Limit per instrument (mics and rows add voices; voices are stolen at the limit); Octave; Key Range. | `InstrumentVoiceLimitMax` 1024. The densest chords are the final div. a 3 chord with FINAL_RING and the harp chords. | No dropped voice is visible. Bar 279 is among the 122 unchanged bars and matches c09 within 0.3 dB, and the final chord's decay is identical in both renders (below). |

MANUAL-GAPS.md: #6 (CC16) is covered by the p.34 note. #5 (expressive rows) is finding 5. p.103 Sforzando Crescendo is discussed under finding 3. No open gap is a better fix than a level row for the findings below.

## Method

- **Data.** The c10 stems 01-35 and master (`cycles/c10/render/`), with `cycles/c10/rendered_build/parts.json` for the tempo map, notes and lanes. I compared against the c09 master for repeatability and the bassoon solo, and against `cycles/c10/mvt3-mockup-c10.mp3` (decoded; offset 5 ms) for delivery.
- **Levels.** A 4096-point STFT with a 25 ms hop, stereo power, K-weighted (BS.1770 curve applied as a power response). Values are on my own scale, so compare differences.
  - Per beat: the mean K power over each score quarter. A track counts on a beat when its notes cover at least 0.5 of it.
  - Per note: the body is the score onset + 0.04 s to the end - 0.03 s.
  - Band shares use the same frames.
- **Repeated notes (S1).** For each basses same-pitch eighth pair, I took 2048-point frames (window centred) at body = onset + 0.10 s and at five points across the gap (note-off to next note-on + 15 ms). I summed the band of harmonics 1 (and 1-2, 1-5) of the basses' pitch. The dip is body minus gap minimum. The per-stem gap share is each stem's band energy in the gap over the sum of stems.
- **Decays.** The master's 5 ms energy envelope.
  - Tutti stops are aligned where the level first falls 3 dB under the 0.35-0.05 s body.
  - The final chord is measured at fixed times after the written end (qn 1113), as LEARNINGS c08 asks.
- **Score pages read.** 4, 13, 14, 16. Event marks are from `build/mockup-events.tsv`.
- **Dan's checks through this lens.**
  - Item 5 (rolls): every roll ranks 7th-23rd among the dry stems at its median, at -9.8..-14.3 dB re master. One exception: the timpani are rank 1 on the single beat 920 (bar 231, f roll entering with the f brass while Vln I rests; -13.5 dB re master). They fall to 9-11 dB under the brass by 924. No change is proposed.
  - Item 4 (accents): every fix below is a level row, so no accent's 2-5 kHz front changes.
  - Item 7 (loops): no note length changes.
  - S3: every proposed row starts on a fresh onset or in a rest, or is a bump up. None is a fast fall under a sounding chord, and the returns are post-fader (LEARNINGS c09).
- **Cross-family consistency (measured, no finding).** Median K per beat at each printed dynamic (sustained beats, roles included):
  - At p, winds -13.5, horns -14.7, Tpt 1 -13.3, trombones -16.6, strings -10.4 (Vln I) to -16.9 (Vc). These are within about ±3.5 dB, so p sounds like p. The outliers are Flute 2 (-22.8) and Trumpets 2-3 (-22.1), but those are only the sub. p chord at qn 872-878 and four beats of bar 42, which is not enough to act on.
  - At ff, winds -1.1, horns +3.1, trumpets +6.1, trombones +4.9, strings +0.9..+3.2. That is Rimsky-Korsakov's order (string section +3 over a wind, a horn +3, a trumpet or trombone +6), now that c10 added +2 dB to the trumpets.

## 1. Bar 275 (qn 1096-1100): the last statement of the turn tune sits under the held horns; c10's horn crescendo shape made it worse (measured)

**Where.** Largamente, bar 275. The tune is the turn figure: C5, G4-G4 eighths, C5, then E5 into 276. It is played by Trumpets 1-2 a2 (one track after the unison drop), Flute 1, Clarinet 1 and Violins I "unis.". Under it, Horns 1-2 a2 (Horn 1 track, E4), Horns 3-4 (Horn 3 track) and Trombones 1-2 (Trombone 2 track) hold whole notes with the crescendo into the fff at 278. c10 (critic C #2) added `LEVEL_SHAPES` on Horns 1 and 3, +2.5 dB rising over 1096-1104 (`build/score_config.py` line 604), on top of horn levels that already sit high from the ff of 273-274.

**Evidence (measured, K, note bodies).**

| tune note (sq) | Trumpet 1 | Horn 1 | Horn 3 | Trombone 2 | Violins I | Flute 1 | Clarinet 1 |
|---|---|---|---|---|---|---|---|
| 1096 C5 | 7.4 | 5.7 | 5.8 | 5.1 | 7.6 | 4.4 | 5.8 |
| 1097 G4 | 0.9 | 9.2 | 8.7 | 5.5 | 9.7 | -1.8 | -1.9 |
| 1097.5 G4 | 0.7 | 10.2 | 8.6 | 6.7 | 8.4 | -2.7 | -3.2 |
| 1098 C5 | 5.3 | 9.3 | 7.9 | 7.3 | 9.2 | -1.6 | -0.3 |
| 1099 E5 | 11.4 | 9.3 | 6.1 | 7.8 | 6.0 | 7.6 | -0.6 |

- On the eighths and the C5 of beat 2, Horn 1's held E4 is 4-9.5 dB over Trumpet 1 and 9-13 dB over Flute 1 and Clarinet 1. It is level with or over the violins, which carry the tune.
- The trumpet's two G4 eighths sit on vol 0.2-0.3 dB while its accented quarters have +3..+5.5 dB swells (parts.json `vol_db`). They come out 4.6-6.7 dB under the trumpet's own neighbouring notes.
- The held chord should sit 3-6 dB under the tune (KIT §13). Here the tune is heard only from the violins, and the brass colour of the figure is lost for its first beat and a half.

**Fix.**
- `build/score_config.py` c10 block, line 604: replace the Horn 1 and Horn 3 shape `[(1096.0, 0.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)]` with:
  - Horn 1: `[(1095.78, -4.0), (1099.0, -4.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)]`
  - Horn 3: `[(1095.88, -3.0), (1099.0, -3.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)]`
  - Each first point is at the track's moved note-on, so the step lands on the new attack.
- Add `LEVEL_SHAPES["Trombone 2"] += [[(1095.88, -2.0), (1099.0, -2.0), (1104.0, 0.0)]]`.
- `build/note_trims.json` "Trumpet 1": `{"1097.0": 3.0, "1097.5": 3.0}`.
- Expected (simulated on the stems):
  - Horn 1 4.9 / 5.6 / 4.7 on the three beat-2 notes, and Horn 3 about 5.4 / 5.3 / 4.4.
  - Trumpet 1's eighths 3.9 / 3.7. Violins I are unchanged at 8.4-9.7, now 3.5-4.5 dB over the horns.
  - The horns still crescendo, now by about +6.5 dB from 1099 to 1104 instead of +2.5. That serves C's c10 aim (horns rising through 275-276) more strongly.
  - Bar 276: Horn 1 about 2.5 dB lower at 1101.5 (7.9 against Trumpet 1's 10.2).

## 2. Bars 236-238 (qn 937-952): Clarinet 1's p counter-line under the violins' "molto cantabile" is lower than the harp's p arpeggios and the basses (measured)

**Where.** Q, Poco più mosso. Movement I's second theme returns in C major in Violins I and II ("molto cantabile", mf, port.). Under it, Clarinet 1 has the "1." p counter-line with its own hairpins from 237. The harp plays p arpeggios, the violas p, the basses p. No role is on Clarinet 1 here. Harp has `[952, 968, -3]`, Violins II `[936, 968, 2.5]`.

**Evidence (measured, K, Clarinet 1 note bodies 937-950).**
- Clarinet 1: -9.3 to -16.3 dB, median -11.6.
- Harp: -8.3 to -10.0 (median -8.7).
- Double basses: -7.0 to -12.4. Violas: -6.2 to -12.4.
- Violins I: -2.5 to +3.5 (median -0.5).
- So the counter-line is 3 dB under the harp's accompaniment (as much as 7 dB on 946) and 11 dB under the tune.
- Norms: at p one wind equals one string section (Rimsky-Korsakov, KIT §13). A counter-melody belongs between the tune and the accompaniment, 3-7 dB under the tune.

**Fix.** `build/roles.json`:
- Clarinet 1 `[937.0, 952.0, 4.0, 1.0]` (it starts on the line's first note; the clarinet rests before).
- Harp `[936.0, 951.5, -2.0]`. It ends where the existing `[952, 968, -3]` starts its 0.5 qn ramp-in, so the two do not add.
- Expected: Clarinet 1 median about -7.6, harp about -10.7, Violins I -0.5. The counter-line then sits 3 dB over the harp and 7 dB under the tune.
- Clarinet 1 is a CC1 dynamics track with a CC1 floor of 36 here. The role is level only, so the p layer is kept.

## 3. The sf of the sfp at bar 149 (qn 592) in the winds and brass: the front is 3-4.5 dB under the ff before and the peak is 0.27 s late; the strings' c10 bump works and should be extended (measured; effect of the fix inferred)

**Where.** qn 592. Every wind, horn, trombone, tuba, timpani and string staff has the sfp. The trumpets do not: Trumpets 1-2 continue their ff accented half notes over it (mockup-events.tsv). The open item from c10 was that the brass peak +0.27 s late although led 0.05-0.12 s.

**Evidence (measured; 5 ms energy).** Columns: first 0.1 s minus the ff before (-0.6..-0.1 s); 0.1-0.25 s minus the ff before; peak time in the first 0.5 s.
- Horn 1: -2.9 / -1.9 dB, +0.27 s.
- Horn 3: -4.1 / -1.3, +0.27 s.
- Trombone 1: -4.4 / -3.6, +0.28 s.
- Clarinet 1: -3.0 / -4.4, +0.29 s.
- Bassoon 1: -4.5 / -1.8, +0.17 s.
- Master: -1.4 / -1.2, +0.24 s.
- For comparison, the strings with the c10 bump: Violins I -0.6, Violins II +1.6, peaks +0.00..+0.06 s.
- Horn 1's CC1 stays at 108 until 592.38 and only then falls into the p. So the attack already plays the ff layer, and a different CC1 shape cannot bring the peak earlier: the sample's rise sets it, as c10 found.
- The "Sfz Cres" row (p.103, Solo Horn and Solo Tuba) records an sf followed by a strong crescendo. It would fit "sfp <", but it costs a full rebuild of each track and memory at 45 GB, and its lengths are fixed.

**Fix (no memory cost).**
- `build/score_config.py`, next to the strings' bump (line 598): add the same post-fader shape `[(591.95, 0.0), (592.0, 3.0), (592.22, 3.0), (592.35, 0.0)]` to Horn 1, Horn 3, Trombone 1, Clarinet 1 and Bassoon 1 (the tracks whose front is 2.9 dB or more under).
- Leave out Flute 1 (+4.6), Bassoon 2 (-1.0), Tuba (-0.7), Trombone 2 (0.0) and Trumpet 3 (-1.5).
- Expected: those fronts move to about -1.5..+0.1 dB of the ff before, and the master's first 0.1 s from -1.4 to about -0.6 dB (simulated by scaling the stems' frame power).
- The perceived attack should move earlier because the front rises while the peak stays put (inferred; check with pcx).
- If a later cycle has memory to spare, the Sfz Cres row on Horn 1 alone is the A/B to try.

## 4. The basses' repeated eighths on the master: in the band the basses own, the dips are 2.8-4.6 dB. The rest of the gap is filled by printed held unisons, so matched gaps on the doublers would contradict the score (measured; fix effect simulated)

**Where.** Double basses' hammered eighths 792-840, 984-1088, 1088-1108 (296 same-pitch pairs). This is the coordinator's open item.

**Evidence (measured).**
- **The basses carry only their fundamental.** Each 1/6-octave band's share of the dry-stem sum:
  - Basses 73-86 % at 60-75 Hz, 16-51 % at 84-134 Hz, 5-7 % at 170-215 Hz, 0-1 % above 250 Hz.
  - Their bow attacks never reach the bands where a listener hears articulation in a tutti, so separation can only come from the fundamental.
- **Master dips by band** (median per span: 792-840 / 984-1088 / 1088-1108):
  - Harmonics 1-5: 1.7 / 2.1 / 1.6 dB (the measure behind c10's 2.2-3.0 dB).
  - Harmonics 1-2: 3.2 / 2.7 / 3.3 dB.
  - Harmonic 1: 3.8 / 2.8 / 4.6 dB, with 38 / 52 / 37 % of repeats under 3 dB.
  - The harmonics 1-5 band is mostly other instruments: the basses hold only 6-10 % of it, because celli, horns and violas play the same pitch class an octave or two up.
- **Who fills the gaps at the fundamental:**
  - 792-840: basses 52 %, tuba 23 %, timpani 16 %.
  - 1088-1108: basses 65 %, celli 19 %, tuba 18 %, timpani 9 %.
  - 984-1088: celli 47 %, basses 32 %. This is the celli's held melody (Movement I's theme, G2 at 98 Hz falls inside the 2048-point band). The fundamental-band dip there is partly a measurement limit.
- **The doublers hold the basses' pitch in the score.** Tuba and contrabassoon hold the same pitch as whole notes at 796 (D2, 3.75 qn) and 1092 (C2, 3.76 qn). At 984-1004 they hold C2/E2 under the basses' C2/E2 eighths. Gaps or per-stroke dips on those held notes would contradict the printed sustained notes.
- **The stem dip fell when the detach dip was cut.** At the fundamental the basses' stem dips are now 5.7 / 4.3 / 6.9 dB. c01's -5 dB detach dip gave 7.3-7.9 dB. c10 cut it to -3 dB on these spans while it added the 63 ms gaps.

**Fix.**
- `build/score_config.py`: return the basses' detach dip on 792-840.25 and 1088-1108.25 to -5 dB (keep -3 on 984-1088, where the celli fill the band anyway). Keep the REP_SPLIT gaps.
- Expected from the gap shares: the master fundamental-band dip rises by about +0.9 dB in 792-840 (to about 4.7) and +1.2 dB in 1088-1108 (to about 5.8). In 984-1088 it stays about 2.8-3.0, which is the most the printed celli line allows.
- Refit the metric tables after the render (LEARNINGS c10: gaps and dips move the per-position stroke levels).
- Judge S1 for the basses in the fundamental band, and drop the 4 dB master target in the harmonics 1-5 band for these spans. Record that in LEARNINGS.

## 5. Bassoon 1's "Leg Slur Exp" solo (bars 115-122): keep the row; its two phrase-start notes swell in 7 dB over 150 ms (measured; fix inferred)

**Where.** qn 455.9-488, "solo, espress." p < mp > p, on the BS KS Master's "Leg Slur Exp" row since c10 (stem fix -2 dB).

**Evidence (measured).**
- **Balance.** The solo is +4.6 dB over the sum of everything else (median per beat). Its nearest stem is Violins II's pizz. at 8.4 dB under (Vln I 7.8 on 9 beats). That is the same margin as Trumpet 1's open solo (+6.1 over its nearest). The level is right after the stem fix.
- **Evenness.** On the master, where the solo dominates, per-note body levels span 7.9 dB (SD 2.0) in c09 on Leg Slur MAX and 8.9 dB (SD 2.4) in c10 with the 2 dB stem fix added back. The Exp row is slightly less even, not more. The worst note is Eb4 at 475, 6.5 dB under the master and 9 dB under its neighbours on the stem. Its residual against the CC11 curve is about -18 dB, against -8..-12 for the notes around it.
- **Phrase starts.** The two velocity-53 phrase starts (456 D4, 472 C4) begin 7.4 and 7.3 dB under the rest of the note in their first 150 ms (stem). In c09 the same notes measured +0.9 and -0.1 dB on the master. The other long notes (v60-80) measure -5.2..+6.1. The printed mp peak (464 A4, -11.2) comes out 2.9 dB under the Bb3 at 462 (-8.3) that leads into it.

**Verdict and fix.**
- Keep the row: joins and level are fine (c10: joins +10 ms median), and the slow first-note bloom may be the "espress." colour. Dan's ear decides that.
- Two level-only corrections in `build/note_trims.json` "Bassoon 1":
  - `{"475.0": 4.0, "464.0": 2.0}` (Eb4 back to its neighbours; the printed mp crest over 462).
- If the entry bloom is judged late, `VEL_SET["Bassoon 1"] = {456.0: 72, 472.0: 72}`. Check the realised velocity in parts.json, because VEL_SET matches on the note's qn. A higher first-note velocity should speed the attack on this legato patch (inferred; measure early-minus-body again).

## 6. Bar 223's chorale and the ending: balance holds; one small adjustment in bars 230-233 (measured)

**Where.** P, bars 224-234: the brass chorale in whole notes, f (Trumpet 1 top), with the violins' mf tremolo in 224-225, the winds' and violins' ff line in 226-229, and Violins II's portato quarters in 231-233.

**Evidence (measured, per 4 qn).**
- **224-225.** Trumpet 1 -2.4 / +1.0, Trombone 1 -1.3 / +1.7, Violins I tremolo -3.8 / -3.8, Violins II -6.0 / -6.4. The chorale top is 1.4-4.8 dB over the tremolo, so the tremolo is under the chorale as the brief asks.
- **226-228.** The winds and violins have the printed ff line and lead (Violins I +5.7 over Trumpet 1). That is correct.
- **230-233 (916-932).** Trumpet 1 -2.1 / -2.8 / -3.8 / -7.3 against Violins II's portato -1.7 / -5.2 / -1.4 / -4.6 and Trombone 1 -2.0 / -2.1 / -2.1 / -5.8. The chorale's top voice is level with the accompanying portato pulse (Rimsky: a trumpet at f about 3 dB over a string section).
- **Arrival 888.** 30-150 Hz is basses 38 %, timpani 18 %, bass drum 17 %, tuba 11 %. In the next beat it is basses 61 %, tuba 17 %. The crash is the loudest stem for one beat (-8.8 dB re master) and is gone from the top six after it.
- **Ending 1104-1112.** Basses 46-57 %, tuba 11-19 %, timpani 8-13 %, bass drum 14 % for one beat. The crash is -10.2 dB re master at 1108, then out of the top six. Low brass, timpani and bass drum do not cover.
- **Timpani rolls in 273-278.** Rank 3-16, 30-150 Hz share up to 70 % only in the allargando strokes of 1084-1086 (bar 272, printed ff strokes).

**Fix.** `build/roles.json` Trumpet 1: split the existing `[892.0, 928.0, 1.0, 4.0]` into two rows, so they do not add:
- `[892.0, 914.0, 1.0, 1.0]` (224-228 unchanged; Trumpet 1 rests 912-916).
- `[916.0, 932.0, 3.0, 2.0]`, ending with the printed decrescendo of 233.

Expected: Trumpet 1 +2 dB in 230-233 (-0.1 / -0.8 / -1.8 on the first three bars), 1.5-4.4 dB over Violins II's pulse on two of three bars. This is the smallest finding; do it only if the cycle has room.

## Coordinator items

**Wetness (measured on the master, returns unchanged).**

| | to -20 dB | drop at +0.3 s |
|---|---|---|
| qn 5 | 0.41 s | 15.9 dB |
| qn 21 | 0.36 s | 15.7 dB |
| qn 101.75 | 0.29 s | 20.8 dB |
| qn 373.75 | 0.39 s | 13.2 dB |
| qn 450 | 0.29 s | 19.9 dB |
| qn 662 | 0.36 s | 15.8 dB |
| final chord, after qn 1113 | 0.41 s (-10 dB at 0.17 s) | 14.4 dB |

- c09's values are the same to within 0.03 s except qn 450 and 662, where c10 is longer by 0.05 and 0.13 s.
- Every stop is inside the ceiling (0.50 s). The final chord falls 20 dB in 0.41 s, as asked.
- The mix is on the dry side of the recordings (0.43-0.55 s) but not too dry. The drop at +0.3 s is 13-21 dB against 13-17 in the recordings, and c10 B's late slope of 1.5-1.7 s still holds (returns untouched). Do not dry it further. If Dan hears it as dry, raise the four return faders by +1 dB first.

**Delivery (mp3 against the master, plain RMS per bar).**
- **Bars 41-42.** Master 9.3 dB, mp3 6.7 dB. Bar 41 is a held V7 thinning out, falling to p, not a subito, so a 6.7 dB step still reads as the printed fall. Bars 42 -> 43 are -2.7 in the master and -0.3 in the mp3. No change needed.
- **Rise into 278.** mp3 bars 273-278: -18.0 / -18.5 / -18.1 / -17.6 / -15.8 / -14.3. Master: -20.1 / -20.1 / -19.6 / -19.2 / -17.5 / -15.4.
  - One 0.5 dB reversal at 273 -> 274 in the mp3, against a flat master.
  - 275 -> 278 rises 3.8 dB in the mp3 and 4.2 dB in the master.
  - 278 is the loudest mp3 bar, then 223.
  - Fine. Finding 1 does not change the ride, because it is a level change inside one bar of held chords.

**315 Hz hump in J (536-600), what else feeds it (measured).**
- The hump is 8.3 dB. Horn 3 holds 36 % of the master's 315 Hz third octave in J and 40 % of the excess over the 250/400 Hz mean.
- 92 % of Horn 3's 315 Hz energy in J is its D4 (294 Hz) at 584, 588 and 592-599 (the stop chord and the sfp crescendo). c10's cut on 552-564 touched 2 % of it, which is why the hump moved only 0.1 dB.
- The other feeders are the violas 15 %, bass clarinet 7 %, Trombone 2 7 % and R Brass 6 %, all on the written D4 / E flat 4.
- Horns 3-4 a2 at the stop chord sit about 2 dB under the trumpets and trombones, inside the norm. A -3 dB row on Horn 3 584-600 would take J's hump only to about 7.5 dB.
- Do not chase J. Use the whole-piece 4.4 dB as the measure.

**Brass peak at 592:** finding 3. **Bassoon 1's Exp row:** finding 5. **Basses' repeats:** finding 4. **Flute 2 at 650 and the violas' chord repeats:** critic A's area. Neither changes a level here.

**Render repeatability:** see the p.34 note. Before fitting anything on Bassoon 1 outside its solo, compare it note by note with c10. The full rebuild in c10 moved bars 106, 154 and 195-196 by up to 1.3 dB on the master with unchanged data.

**Do not touch:**
- Trumpet 1's open solo (bars 51-66: +6.1 dB over the nearest stem).
- The muted Trumpet 1 with the cor anglais (bars 171-186).
- Theme B in the trumpets (bars 211-218: the pair +8.1 over the nearest non-trumpet).
- The F2 violins over the viola / cello counter-lines (bars 67-82: Vln I+II +7.3 / +8.0).
- The counterstatement's bass theme over the violin countersubject (+6.5).
- The ff family order (trumpets +7 over winds, horns +4, strings +2..+4).
- The trumpets' c10 ff trims.
- The string sf bump at 592.
- The final ride row and FINAL_RING (final chord -20 dB at 0.41 s).
- The returns, faders and register sends.
- The arrival and ending low-end balance (basses lead 30-150 Hz; timpani, bass drum and tuba under; crash one beat on top).

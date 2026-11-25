# Cycle 45, critic A (articulation and phrasing), on the c44 render

Sources: the c44 render (`cycles/c44/render/`, stems 01-32 dry, 33-36 returns, `00_Master.wav` = dry + returns) and the data it was made from (`cycles/c44/rendered_build/parts.json`; `build/parts.json` now equals `delivered_build/parts.json`, which differs only by the removed Clarinet 1 role). The reference MIDIs are the originals in `/Users/gooby/sandbox/mockup-reference-cn1rc0/mockup-kit/reference/`. I measured them and our parts.json with one script that uses the same definitions for both (phrase = notes with gaps under 150 ms, as in FINDINGS `smf2.py`). My scripts were in `/private/tmp/claude-501/mockup-loop/mvt2-c45-A/`, deleted at the end. The methods are listed at the end.

The c44 mix change touched no MIDI, so the articulation data (keyswitches, rows, mutes, tremolos, pizz., harp rolls) is the c43 data. c44 A checked it and found it correct, and I did not re-check those parts. This report covers the ONE_TIME performance-data items in my area (finding 1 and the table after the findings), plus what the new mix changed in what can be heard.

## Manual notes (MANUAL-READING row c45 / A: group A5, May 2021 HO manual PDF pages 100 and 103-107, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| Brass instruments: Solo French Horn, Solo Trombone, Solo Tuba, 2 French Horns, 2 Trombones, 2 Tbn + 1 Bass Tbn, 6 Horns (p.100) | Horns 1-4 on 1FH KS Master, Horns 1-2 a2 on 2FH, trombones and bass trombone on 1TB, tuba on 1TU | Yes. The bass trombone's D2 at 218 still plays an E2 root two semitones down (MANUAL-GAPS #12, optional). |
| Repetitions patches: tempo-synced, not round robin, the mod wheel sets the level; Triple Performance; Sforzando Crescendo on Solo Horn and Tuba, where velocity sets the attack (p.103) | v600 has no fast brass repeats and no brass sf< | n/a, correctly not used |
| Effects: trills, rips, recorded crescendos ("Crescendo MOD SPEED": CC1 1-42 / 43-85 / 86-127 picks slow / medium / fast), flutter, clusters (p.104-105) | none printed | n/a |
| Legato: a slur sounds only with no gap and an interval of at most an octave; legato patches are monophonic unless CC22 is 0-63 (p.105) | every brass Leg Slur MAX note | Yes (measured in parts.json): no brass legato join wider than 12 semitones, no chord sent to a Leg row on any brass track, and every join overlaps (45 ms). |
| Legato Slur: the mod wheel sets the volume, and near CC1 127 it opens a filter for overblowing; **velocity sets the speed of the slur** (p.106) | brass on CC1 (`CC1_DYN_TRACKS`); every brass legato target | CC1: yes. Its maximum is 108 on every brass track (bars 61-64 and 79-82), so no overblow colour reaches the ff tutti, which suits "molto sostenuto". Velocity: **no**. Every horn legato target plays v124, the fastest slur, including Horn 1's dolce solos (bars 7-14, 65-70). EW's own HO template plays 1FH legato at v80 (IQR 77-87) and 2FH at v76. See finding 2. |
| Legato Slur Accent: accent strength set by velocity (p.106) | Trombone 1 213 and 218 (accents inside the slurred quotation) | Not used. It is not needed: the Sus MAX swell already gives weight without bite (do-not-touch below). |
| Legato Slur Repetitions: re-tongued samples for same-pitch notes inside a slur (p.106) | Horn 2 208 (ff tenuto repeat, own-band dip 2.7 dB in c43), Horns 1-2 bars 80-81, Horn 3 289 | Not used. Horn 2 208 is the only brass repeat that still runs together (c44 A #1c, deferred). This row is the library's answer if the re-tongue gap fails again. |
| Mutes: the 06 Mutes folder; stopped horn (p.106) | Horn 3 con sord. from 286 | The Solo French Horn folder has only stopped-horn patches (MANUAL-GAPS, checked), so the `mute_eq` emulation stays. This is correct for a straight mute. |
| KS Masters switch by keyswitch (p.107) | all brass tracks | Yes. No keyswitch arrives within 0.02 qn after a note it governs (c44 A). |

## Findings, ranked by what a listener would hear

### 1. Wind and horn phrases still start and end flat: +1.8 dB of swell by 0.8 s and 1.9 dB of taper, against about +3.5 dB and 4 dB. Here are the exact c45 values

**Where.** Every wind and horn phrase of 2.5 s or more: Horn 1 bars 7-14, 53-60, 65-70; Oboe 1 15-22 and 45-47; bass clarinet 31-36; Flute 1 37-44; cor anglais 41-50; Clarinet 1 85-89; the bassoons and clarinets under them. The string themes come second (23-30, 53-56, 71-77).

**What is wrong (measured).**
- Lanes in parts.json, phrases of 1.5 s or more, compared with the reference originals. Values are in CC units: peak position / start under peak / end under peak / range.
  - Ours:
    - winds 0.28 / 4 / 8 / 18;
    - strings 0.40 / 12 / 21 / 22;
    - brass 0.01 / 2 / 0 / 4.
  - Lyrical references:
    - Kung Fu Panda 3 strings 0.57 / 43 / 58 / 63;
    - Duc's Mahler Adagietto (strings, played in) 0.40 / 21 / 20 / 36;
    - Atonement strings 0.57 / 30 / 24 / 35 and winds 0.62 / 38 / 22 / 38;
    - Shape of Water winds 0.47 / 26 / 29 / 30.
- Swell after the first onset (lane, +0.4 s / +0.8 s).
  - Ours: 0 / +1 in all three families.
  - References: KFP3 strings +13 / +18, Shape winds +8 / +14, Atonement winds 0 / +8, Duc 1 / 3.
- Taper over the last second.
  - Ours: 3 / 4 / 0 (winds / strings / brass).
  - References: KFP3 18, The Crown winds 33, Atonement 3-5.
- Long notes held flat in the lane: ours strings 23 %, winds 28 %, brass 67 %; references 0-13 % (Duc 26 %).
- CC points per second inside phrases: ours 3.2 / 2.4 / 0.5; references 8-26 (Duc 25.6, KFP3 strings 17.7, The Crown 13.5-15.5, Atonement 8-13).
- What reaches the listener (dry stems, phrases of 4 s or more, 100 ms RMS):
  - Winds: start 7.7 dB and end 6.6 dB under the peak (range 13.3), so the arch depth is already there from the printed hairpins. But the peak lies inside 0.33-0.62 of the phrase on only 22 % of phrases (median 0.38). Swell +1.7 dB at 0.4 s and +1.8 at 0.8 s; taper 1.9 dB over the last second.
  - Brass: same picture. Peak in the middle third on 24 %; swell +2.7 / +1.6; taper 1.9.
  - Strings: the sample bloom already gives +7.0 / +8.2 dB by 0.4 / 0.8 s. Taper 2.6 dB.
  - Long notes of 2 s or more vary 3.3-4.7 dB in audio; only 11-14 % are flat (under 1.5 dB). The flat lane does not give flat long notes; the problem is only the timing of the motion, not its amount.
- Doublings (plan item "doublings share one curve"). Over every doubled run of 6 notes or more:
  - The CC lanes are already shared: r 0.91-1.00, because they come from the printed dynamics.
  - The `vol_db` lanes diverge: r -0.41 to 0.93, SD of the difference 1.5-6.0 dB. Examples: Flute 1 / Oboe 1 / Violins I-II at 188-204 r -0.16..-0.36; Oboe 1 / Bassoon 1 at 140-151 r -0.19; Bassoon 1 / celli at 196-204 r -0.41. A phrase shape computed separately per track would make this worse.

**Fix (`tools/score_to_parts.py`, new generic `PHRASE_SHAPE`; movement II values in `build/score_config.py`).** Apply it after the printed-dynamic curve. It is skipped on any phrase where a printed hairpin covers more than half the phrase.
- **Class "lyrical"** (slurred lines marked dolce, espr., cantabile, or unmarked melody). Write it in `vol_db`, relative to the phrase's onset level:
  - 0 dB at the onset;
  - +1.5 dB at +0.4 s and +2.0 dB at +0.8 s;
  - rising to +2.5 dB at 0.44 L;
  - +0.5 dB at L - 1.0 s, and -2.0 dB at the last note-off.
  - Scale by 0.6 at ppp-pp and 1.0 from mp; phrases of 2.5 s or more only.
  - Add a CC11 copy of +4 CC at the peak only where the note's CC11 stays inside one layer (read the layer tables; woodwind edges at CC 30-36, LEARNINGS section 4).
  - On horns use `vol_db` only. Horn CC1 must not go under 57 (c31: legato collapse).
  - Strings: no swell term (the bloom does it). Use only the taper (+0.5 at L - 1 s, -1.5 dB at the end), and only on phrases with no printed decrescendo at their end.
- **Class "build"** (a phrase under a printed crescendo to f or ff: bars 53-60, 75-78). No arch. The printed crescendo is already the shape; keep the existing hairpin rules.
- **Class "accented"** (Trombone 1's quotation). Leave it alone: 213 already peaks at +0.2-0.4 s and falls 5 dB over its 1.7 s, and 218 falls 27 dB through its printed decrescendo, which is the plan's start-high-and-fall shape.
- **Doublings.** Compute the shape once per doubling group, from the top voice's phrase boundaries, and add the same dB curve to every track in the group. Each track's trims and roles stay on top. Groups from parts.json:
  - Violins I + II at 65-90, 171-204, 237-262;
  - Flute 1 + Oboe 1 + Violins I/II at 188-204;
  - Oboe 1 + Bassoon 1 + celli at 139-151;
  - bass clarinet + Bassoon 2 + basses at 188-204;
  - Bassoon 1 + celli at 250-274;
  - Flute 1 / Oboe 1 / Clarinet 1 / Violins at 256-274.
- **Density.** In `sample()` (line 1697), change the grid from 0.125 qn to 0.0625 qn. That is 69 ms at 54 bpm, about 14 points per second wherever the shape moves, which falls inside the plan's 13-44.
- **Leave out** the in-slur lean-off: -2 CC is about 0.5 dB, and the legato fills already lean off by 0.5-1.1 dB (c44 A).
- **S3.** A `vol_db` taper is safe now. The sends are post-fader and the hall is on the returns, so a fall in the dry track leaves the hall tail ringing (inferred from the routing; check the fastest 50 ms master falls at 148 / 195 / 223 after the render).
- **Targets for the next render** (wind and brass phrases of 4 s or more): swell at +0.8 s of +3 to +4 dB; taper over the last second of 3.5-4.5 dB; peak inside 0.33-0.62 on half the lyrical phrases or more; delivered LRA and span unchanged within 0.3.

Judgement: the baseline and reference numbers are measured. The dB values are inferred: they convert the plan's +15 / +25 / 20-unit shape at our CC11 slope of 0.17-0.36 dB per CC (LEARNINGS section 4) and stop at the depth our winds already have.

### 2. Wind legato targets play v60 (v80 under 0.9 s), and horn targets play v124 even in the dolce solos. Oboe 1 arrives +63 ms by pcX with its crossovers on time

**Where.**
- Every wind legato target (202 joins; median v60, IQR 60-80). `score_to_parts.py` sets them by note length, not by dynamic.
- Every horn legato target (all v124, `LEG_VEL_STRONG`): Horn 1 bars 7-14 (dolce espr.), 53-60 and 65-70; Horns 1-2 a2.

**What is wrong (measured).**
- Joins on the c44 stems with `tools/pcx.py`. Values are the pcX median and robust SD:
  - Oboe 1 +63 ms (SD 76);
  - bass clarinet +40;
  - Bassoon 1 +14;
  - Flute 1 +9;
  - Clarinet 1 +6;
  - cor anglais -1;
  - Horn 1 -20 (early).
- On Oboe 1 the crossovers sit at a median of about +0.016 s (on time), but the pcX on the rising joins is late: 43.5 +0.115, 55 +0.112, 140 +0.178, 142.5 +0.171, 146 +0.144, 189 +0.174 s. The new note's level comes up slowly after the transition, which is the slow slur of a low-velocity target.
- Velocity sets the slur speed on HO legato (manual p.106 brass, p.144 strings). EW's own HO template plays its KS Master legato rows at:
  - Flute v95 (IQR 91-104), Oboe 92 (87-102), cor anglais 91 (82-97), Clarinet 90 (81-96);
  - 1FH 80 (77-87), 2FH 76;
  - basses 94.
- The expert files have legato velocity following the dynamic, with r about 0.3-0.35. In our winds it is r 0.19 (by length), in our strings and brass none (constant v124).

**Fix (`tools/score_to_parts.py`, the `leg_target` branch at about line 2741).**
- Winds: replace the length rule with `value_at([(22, 86), (46, 90), (72, 96), (114, 104)], base(q))`. Keep the cor anglais's c04 per-onset values where they are higher.
- Horns (1FH and 2FH): use the same map minus 6, which gives v80-98. Horn 1 is 20 ms early now, so a slower slur has room.
- Strings: keep v124 this cycle. On the string KS Masters v108 against v124 gave crossovers identical to the millisecond (LEARNINGS section 5, c11), so there is nothing to gain for the risk.
- After the render, re-measure pcX on the winds and Horn 1. Refit `LEG_LEAD_S` only where the median moves more than 30 ms. The expected moves are Oboe 1 and the bass clarinet earlier, and Horn 1 later by 25-80 ms (c03's measured velocity effect).
- Target: wind pcX medians within ±30 ms, Oboe 1's rising joins under +0.08 s, and Horn 1 between -10 and +40 ms.

Judgement: the velocities, the pcX values and the template values are measured. The effect of velocity on these joins is inferred from the manual and c03.

### 3. Violas' sotto voce portato eighths (bars 48-51): still two identical takes alternating, and every second A3 peaks 0.31 s after its beat

**Where.** Violas qn 152.5-167.5, Detache row, 15 notes, all at v37. This is c44 A #4, deferred by the brief to c45.

**What is wrong (measured, c44 stem).**
- The A3s at 152.5, 154.5, 157.5 and 161.5 all peak at -50.7 dB, +0.17 s, centroid 332-335 Hz.
- 153.5, 156.5 and 160.5 all peak at -50.6 dB, +0.31-0.32 s, centroid 359-363 Hz.
- The D sharp 4 pair repeats the pattern: 164.5 / 166.5 at +0.13 s, 660 Hz; 165.5 / 167.5 at +0.05 s, 675-708 Hz.
- The peaks agree within 0.1 dB. That is a mechanical repetition, and the late take puts the perceived attack an eighth's worth late (S2).
- Leads are already +220 ms on the late takes and +290 ms on the others.

**Fix (`build/score_config.py`).**
- `VEL_SET["Violas"]` on these 15 onsets: a seeded pattern within ±5-7 of 37 (plan item "±5-7 random"), for example 37, 32, 40, 34, 39, 31, 36, 41, 33, 38, 35, 42, 34, 39, 36. Detache crossfades its layers with velocity, so no two notes play the same sample at the same layer weight.
- `build/entry_leads.json` "Violas": +0.06 s on 153.5, 156.5 and 160.5 (total 0.28 s, under the 0.30 s cap).
- Re-measure after the render, because velocity changes can move the round-robin take order.
- Target: A3 peaks spread over 1-3 dB, every peak by +0.20 s.

Judgement: measured. The velocity response of Detache is inferred.

### 4. S1 judged in the master: only Violas 87 still runs together; Vln II 289 is already a 7.6 dB hole in the master, so do not widen it

**Where.** The three repeats ONE_TIME lists (Violins II 289 and 120, Violas 87), measured in the master as well as the stem (c44 `s1_c44.txt`, confirmed with my band envelopes).

**What (measured).**
- **Violins II 289.** Own-band dip 0.4 dB in the stem, but **master 7.6 dB**. At qn 289 (bar 88) every voice re-attacks together: Clarinet 1 tenuto (stem dip 8.5), Horn 3 tenuto (10.8), Violas div (5.7), Violas, celli and basses on new pitches. The master already drops more than the 3-6 dB aim (MANUAL-GAPS #2). The MIDI gap at Vln II 289 is only 35 ms (the 0.03 qn re-bow gap; 289 is not in `soft_gap_at`), but widening it would deepen the master hole further.
- **Violins II 120.** MIDI gap 80 ms; own-band 0.3 dB in the stem, master 3.3 dB. It passes in the master, because Vln II div 120 dips 5.8 dB at the same moment.
- **Violas 87.** Gap 80 ms, CC11 already falls 48 -> 38 into it; stem 2.6 dB, own-band 2.5, master 2.2. This one fails. The release (600 ms pp/p cap) and the slow pp attack fill the 80 ms. Violas 71, with the same gap and fall, dips 16.6 dB because the old note has fallen 0.07 s before the onset.

**Fix (`build/score_config.py`).**
- Violas 87: add it to `DOWNBOW_STROKE_AT["Violas"]` (line 995; the path that fixed Violas 69 / 248.5 in c42-c43, with its sus_fall). Target: master dip 3-6 dB.
- Violins II 289: no change. Drop it from the ONE_TIME list on this evidence.
- Horn 3 289: shorten its re-tongue gap so its stem dip falls from 10.8 to 5-7 dB (`REP_RETONGUE_AT["Horn 3"]` or `WIND_REP_PORTATO` gap 0.06 s). Target: master at 289 between 4 and 6 dB.
- Violins II 120: no change.

Judgement: measured. The DOWNBOW_STROKE_AT effect at 87 is inferred from 69 / 248.5.

### 5. Timpani strokes sound 58-60 ms after the beat (`TIMP_DELAY_S` 0.06). Pizz. velocity ignores the beat

**Timpani (measured).**
- Audible onsets (10 ms RMS reaching peak - 10 dB) on the dry stem: the coda answer at 277 / 278.5 / 279 at +58 / +60 / +58 ms, the bar 61 roll start at 204 at +58 ms. The attack probe reads 277 at +0.05 s (limit 0.06).
- The delay comes from Movement I c03. There, Allegro tutti strokes sounded 80 ms ahead of sections whose attacks were slow. Here every string and wind attack is now led onto the beat (pcX medians +1..+22 ms on the strings).
- The plan says percussion on the grid. Star Wars puts its timpani 38-43 ms earlier than its pitched tracks.
- Fix: `TIMP_DELAY_S = 0.0` in `build/score_config.py`. Target: 277 within ±20 ms in the probe. Check that the 203 and 209.5 strokes still sound with the strings' attacks.

**Pizzicato (measured).**
- The violas' pizz. triplets (bars 41-44, 42 notes) play v48-53 following the printed hairpin, the same at every triplet position.
- The audio peaks spread with SD 3-5 dB at each position, from the round robin, with no metric pattern: beat 1 / 2nd / 3rd triplet medians -49.4 / -51.4 / -49.5 dB.
- The basses' pizz. are v53 on every beat (v98 at the 212 sf).
- Plan: 15-25 steps between the strongest and weakest note, ±5-7 random. The pizz. row has a velocity-layer edge at 46/47 (5-8 dB, c29 A #3), so stay at 48 or more.
- Fix, as `VEL_SET["Violas"]` on 124-140: beats 1 and 3 hairpin value +10, beats 2 and 4 +6, 2nd triplet +0, 3rd triplet +3 (it leans into the next beat, as KFP3's 117 / 93 / 96 / 109); then ±4 seeded. The result is 48-63. Basses: beat 1 +6. Read the row's next velocity edge in the .oib first.
- Parking CC11 high for shorts (plan) changes the level by 10+ dB at pp. Test it only on a test stem.

Judgement: measured. The audible effect of the velocity pattern is inferred.

### 6. Held notes and re-bows after the mix change: no loop period in the long notes, two short spans to re-check, master dips small

**Measured.** For each held pitch of 8 s or more: the autocorrelation at 3.95 s of its own band (harmonics 1-4) and of the spectral centroid, 50 ms frames.
- Final chord (Violins I, Violins II, violas, celli, basses, Violas div, 18-26 s): band -0.17..+0.09, centroid -0.04..+0.09.
- Opening Violins I C5: -0.07 / -0.01.
- Basses' 4 soli pedals (304-322 s, 329-348 s): -0.02 / -0.12.
- Celli div coda: -0.00.
- Bass clarinet pedal: -0.23.

None shows the loop period.

Two short spans read positive, but they are only about two loop periods long, so the value is unreliable: violas A flat 3 qn 278.8-285.9 (band +0.44, centroid +0.15) and basses qn 164-172 (+0.35).

Re-bow dips:
- In the stems, 0.8-8.6 dB. Over 8 dB: opening Vln I at 2.8 and 8.5 s, final chord Vln I at qn 295.0, Vln II at 292.0, basses at 297.2 and 283.6.
- In the master the same points dip 0.5-3.5 dB, with steps of -2.5..+2.8 dB.
- The largest master step is -4.9 dB at qn 295.0 (bar 90, rit.).

**Fix.** No data change. Listen-check, and after the render re-measure the violas at 279-286 and the basses at 164-172 with spans of 3 or more periods (fold over 12 s). If the violas stay above +0.3, give them a REBOW_AT point at about 282.5. Re-bow fills were not refit for the dry + return master (c44). Refit them only if the master dips grow past 4 dB.

Judgement: measured. Whether the two spans pulse is unresolved.

## ONE_TIME items in my area: exact values

Ours = c44 parts.json and stems. Refs = the originals, measured with the same definitions (phrases of 1.5 s or more, values in lane units unless dB is stated). "EW" is EW's HO template demo (artic-report, KS Master rows).

| Item | Ours (c44) | Refs | Value for c45 |
|---|---|---|---|
| Legato overlap | 45 ms [40-46] in every family (`LEG_OVERLAP` 0.04 qn) | EW KS Masters: winds 24-41, horns 35-40, basses 41; The Crown 31; Atonement strings 94; Duc (CSS) 181 | Keep 0.04 qn. It is inside the plan's 45-80 (strings) and 33-58 (winds and brass), and string pcX medians are +1..+22 ms. |
| Legato velocity | winds 60 [60-80], r 0.19; strings and brass 124 | EW winds 90-95, 1FH 80, 2FH 76, basses 94; Duc strings 76 [53-93], r 0.28; Atonement 75-83, r 0.37 | Finding 2 (winds 86-104 by dynamic, horns 80-98, strings 124) |
| Repeat gap | strings 42 ms [35-60] (this includes the 0.03 qn loop re-bows, which are meant to be inaudible), winds 76, brass 100 | Duc 114, Atonement strings 132, KFP3 87, Shape 90 | Keep c44's 0.08 / 0.10 s; finding 4 |
| Phrase arch (peak / start / end / range) | strings 0.40 / 12 / 21 / 22; winds 0.28 / 4 / 8 / 18; brass 0.01 / 2 / 0 / 4. Audio dB: winds 0.38 / 7.7 / 6.6 / 13.3 | KFP3 strings 0.57 / 43 / 58 / 63; Duc 0.40 / 21 / 20 / 36; Atonement winds 0.62 / 38 / 22 / 38 | Finding 1 (lyrical vol_db arch, peak at 0.44 L) |
| Swell +0.4 / +0.8 s | lane 0 / +1; audio winds +1.7 / +1.8 dB, brass +2.7 / +1.6, strings +7.0 / +8.2 | KFP3 strings +13 / +18; Shape winds +8 / +14; Duc +1 / +3 | Winds and horns +1.5 / +2.0 dB added; strings none |
| Taper, last second | lane 3 / 4 / 0; audio 1.9 / 2.6 / 1.9 dB | KFP3 18; The Crown winds 33; Atonement 3-5 | -2.5 dB over the last second (strings -2.0) |
| Long notes flat | lane 23 / 28 / 67 % (strings / winds / brass); audio under 1.5 dB spread 11 / 11 / 14 % | 0-13 % (Duc 26 %) | Audio already meets it; the arch adds motion to the lane |
| CC density | 3.2 / 2.4 / 0.5 points/s | Duc 25.6, KFP3 9-18, The Crown 13.5-15.5, Atonement 8-13 | 0.0625 qn grid (about 14/s) |
| Before the onset | +1 / +2 (entry leads) | 0 | Keep (the leads hold the entry level from the moved onset) |
| Level lane follows timbre lane | brass and clarinets r(CC1, CC11) 0.97-1.00 | The Crown, 6 Underground, KFP3: 0.92-0.98 | Met; no change |
| Doublings share one curve | CC lanes r 0.91-1.00; vol_db r -0.41..0.93 | The Crown copies lanes point for point | Finding 1 (one dB shape per group) |
| Beat-position velocity | viola pizz. v48-53 flat across positions; basses pizz. v53 | The Crown 104 / 101 / 95 / 87; 6 Underground 95 / 72 / 83 / 72; KFP3 117 / 93 / 96 / 109 | Finding 5 |
| Spiccato length | v600 prints no spiccato, staccato or wind staccato | 50-62 % | Does not apply |
| Fixed early shift | winds 30-80 ms median per track (Fl1 30, Ob1 60, CA 80, Cl1 70, Cl2 30, BCl 40, Bn1 60, Bn2 40); brass 0-100; strings 120-240 (Vln I 170, Vln II 240, Va 144, Vc 220, Cb 120); harp 0; timpani -60 | Polar: Ob 27, Cl 38 / 46, BCl 17, Bn 40 / 85, Fl 75; strings and brass 20-120; percussion 0 | Winds and brass meet the plan. Strings: drop the 120 ms ceiling. Their leads compensate a measured legato lag of 200-275 ms (LEARNINGS section 5), and the probe is 0. Timpani to 0 (finding 5). |
| Repeated short-note groups fall 15-17 | none in v600 (no repeated short figures) | The Crown | Does not apply |

## Do not touch

- Trombone 1's two accents. 213 is +3.2 dB over the 212.5 pickup in its first 0.3 s and 218 is +4.5 over 217.5; their 2-5 kHz front lies 3.1 and 8.4 dB under the body, and each peaks early and then falls (weight, no bite). Keep their Sus MAX swells, v124 at 215 and the CC7 110/120.
- Brass CC1 at most 108 (no overblow).
- The 45 ms legato overlap.
- Clarinet 1's lead 0.07 (pcX +6 ms).
- The entry leads that hold the entry level.
- c44's soft_gap 0.08 / loud_gap 0.10.
- The basses' coda re-bow points and fills.
- The final-chord re-bows (no loop period measured).
- Flute 1 136 on LegRep RRx4.
- The CC15 mute placement.
- The harp at 0 shift.

## Methods

- **Lanes.** The dynamic lane is CC1 on `CC1_DYN_TRACKS` and CC11 elsewhere, read as steps and converted on parts.json's tempo map. References: CC1, tracks grouped into families by name; same phrase, swell, taper and long-note definitions (`perf.py`).
- **Audio.** 100 ms RMS on the dry stems. Swell is measured against [+0.05, +0.2] s; peak position over 41 points; a long note counts as flat when its 15/50/85 % levels lie within 1.5 dB.
- **Legato timing.** `tools/pcx.py` on `cycles/c44/render`.
- **Doublings.** Same score onsets, same pitch class, 6 notes or more within 4 qn; lanes sampled every 0.125 qn.
- **Loop check.** Own band (harmonics 1-4, ±3 %), 50 ms frames, slow trend removed, autocorrelation at 3.95 s. Re-bow dip = mean 30 ms RMS over [-0.5, -0.2] s minus the 30 ms minimum within ±0.15 s; step = [+0.3, +0.7] s minus [-0.5, -0.2] s.
- **Timpani onsets.** 10 ms RMS reaching peak - 10 dB.
- **Accents.** 2-5 kHz energy in [0, 80 ms] against [250, 600 ms].

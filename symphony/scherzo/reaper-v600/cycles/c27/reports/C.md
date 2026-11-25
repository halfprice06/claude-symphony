# Cycle 27, critic C: tempo, timing and transitions (lens C3), on the c26 render

Sources: `cycles/c26/render/` (master and 31 stems), `cycles/c26/scherzo-mockup-c26.mp3`, `cycles/c25/render/00_Master.wav` and `cycles/c25/scherzo-mockup-c25.mp3`, `cycles/c18/render/` stems, `cycles/c26/build_render/` (parts.json, score_config.py, roles.json), `cycles/c26/records/` (timing_c26.json, pcx.txt), the timing records of c19, c20, c24 and c25, `build/mockup-events.tsv`, `build/score_config.py`, `tools/pcx.py`, score pages 3, 4 and 12, and `cycles/c26/CHANGES.md`.

Methods:
- "S" is the c13 timing measure from `timing_cNN.json`: the earlier of `pcx.attack_pcx` (perceived attack on the note's harmonic bands) and the crossover of the old and new pitch bands, in ms from the score onset.
- For the trio and Meno mosso, I ran `cycles/c19/actor_scripts/timing19trio.py`, copied to scratch with only its root path and track list changed, on c26.
- For the celli joins, I ran `tools/pcx.py` on c26 and kept every join's pcx, crossover and rise.
- Soft entries: the harmonic-band envelope (`pcx.band_env`), with the time each note reaches -12, -6 and -3 dB of its own maximum in the 0.7 s after the beat.
- Downbeat weight: the 10 ms peak in the 90 ms after the downbeat, minus the mean of the same peak on beats 2 and 3. It is given broadband and in 2-5 kHz, per bar, then as a median.
- The mp3 is aligned to the master: it lags by 239 samples on both c25 and c26.
- "Measured" means a number from the render or the data. "Inferred" means reasoned, not tested.

## Manual notes

MANUAL-READING.md has no row for cycle 27 ("cycles after c20 pick their own pages"). I read group T1, May 2021 HO manual PDF p.143-146, in full, because it covers this lens, and I used MANUAL-GAPS.md.

| Reading (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.143: performance-script CCs. CC5 is the legato/portamento time of the emulated (script) legato only; CC36 resets the round robins; CC69 is repetitions; CC70 is finger position. | Every track. The legato rows are true legato, so CC5 does nothing on them. | Yes. CC36/CC16 resets are in use (`RR_RESET_AT`). CC70 rests at 127, with the "sul A" spans in `SUL_SPANS`. |
| p.144: Monophonic True Legato. Velocity sets the transition time (50-60 slower, 110-127 tighter) and "does not affect loudness". | The trio tune: celli v80 (v112 on wide leaps), Violins I v80 at 527.5-552 (`LEG_VEL_SPANS`). The soft legato heads are at v41-53. | Partly. The joins follow the page: the celli crossovers are on time (+8 ms median, check below). Velocity cannot speed up the soft heads' slow first note, because a head has no transition to speed up. That needs CC11 (finding 3). |
| p.144: CC22 mono/poly | none (one line per instance) | Not needed. |
| p.145: the Repetition script randomises each playback; RR Reset gives the same result on every playback. | the theme head's repeats, the pizz. bass of bars 89-100 | Correct: no repetition script (MANUAL-GAPS #2, #15). |
| p.145: RR Reset "to force a particular order of RR samples" at chosen positions | the resets at the heads of the three-bar groups, bars 89/92/95/98 (qn 264/273/282/291), celli and basses | Followed, but the order it forces puts the softest pizzicato sample on every group head (finding 4). The same page's tool, a reset placed elsewhere, can put a louder sample there. |
| p.145-146: finger-position tables (CC70) | Violins I sul A 528-538 and 1089-1125; Violins II 364-383.5, 839.5-851.5, 1044-1054 | Followed. The 528 entry is one of the late soft heads (finding 3); its string choice is not the cause. |
| MANUAL-GAPS #8 (slower legato velocities on the cantabile lines, tried c10) and #12 (RR resets) | trio, ritmo di tre battute | #8: no change needed for timing. #12: see finding 4. |

## Checks the cycle note and the lens asked for (measured)

**Tempo map against the print.**
- Per-bar average tempo on the c26 map:
  - bars 149-152: 253 / 241 / 233 / 228 (printed 252 / 240 / 232 / 228);
  - bars 237-240: 223 / 214 / 207 / 202 (printed 222 / 214 / 206 / 198);
  - bars 241-252: 199, 202, 206, 211, 217, 223, 229, 235, 241, 247, 252, 257 (printed 198 to 254 in two-bar steps), then 264 at bar 253;
  - bars 370-375: 213 / 196 / 179 / 161 / 147 / 140 (printed 210 / 196 / 180 / 160 / 140 / 140).
- The steps are exact:
  - bar 2 at 88 (2.05 s);
  - Più mosso 288 at qn 972 (233.72 s);
  - G.P. bar at 96 (1.875 s, from 243.10 s);
  - Meno mosso 228 at 1020;
  - bar 376 at 50 (3.60 s).
- Total 4:37.9.
- The master falls to -50 dB 0.3 s into the G.P. and to -69 dB by 0.8 s. The last G sharp (Horn 1 and Violins I) fades on CC11 in the last 0.45 s and is gone 1.2 s after the score's end.
- Nothing to change.

**sfp < at bar 301 (C #2 of c26): works.**
- Master per qn: sf 900 -20.9; p 902-905 -30.3 / -30.4 / -29.1 / -29.1; then -27.8, -27.5, -23.9, -22.5, -20.7 at 910. The p holds for 3 qn and the crescendo rises +6.6 dB from 904 to 909.
- On the mp3 the dip is 4.9 LU (900 -11.9 to 903 -16.8). c25 had 2.5.

**Summit arrival on the mp3.**
- The master's peak now comes 0.18 s after 1005 (c25 0.52 s).
- The first 0.5 qn after 1005 is +1.7 dB on the master and +0.8 dB on the mp3 over the 1004-1005 beat (c25 +1.1 / +0.8).
- The lift of the staccato quarter at 1004 (-20.1 dB at 1004.75) makes a +3.9 dB step on the master into 1005.25, but the delivery's compression leaves +0.8 dB on the mp3.
- Over 1006-1007.5 the summit bar is now 0.5-1.5 dB lower than c25 (net of the global -3 dB), because the bloom has gone.
- The timing is right now. The size of the step belongs to the dynamics and balance lenses.

**SLUR_END_BEFORE_STAC in the tutti woodwinds.**
- The slur covers the accented half note, two eighths and the staccato quarter (e.g. Fl1/Ob1/VlnI 315-318). So the 35 ms gap falls inside the slur, before its last, lifted note.
- Level dip between the slurred eighth and the staccato, median (largest): Flute 1 6.1 (9.8), Oboe 1 5.3 (7.6), Clarinet 2 5.7 (6.4), Flute 2 9.3 (17.7) dB. Violins I and II dip 2.0 and 2.2 dB at the same places.
- The staccatos still sit with the strings: 312-360 S medians Flute 1 +7, Flute 2 +13, Oboe 1 -7, Clarinet 2 -11, Violins I Stac +6, Violins II Spic -7 ms.
- Phrasing reads as a lift before the last note. The slur is not broken anywhere else, and the joins inside the slur are unchanged (c26 CHANGES).
- One exception: Flute 2 in the first tutti (318, 330, 348, 354) drops 13.5-17.7 dB, which is a silent hole. Fix: `SLUR_END_BEFORE_STAC["Flute 2"]["s"]` 0.035 -> 0.02 (inferred to close it to about 8 dB).

**Section alignment in the Allegro statements (S2).**
- S medians by passage:
  - theme A: strings short -7;
  - counterstatement: strings short 0, winds short 0;
  - tuttis: strings short -5 / -8, winds short -6 / -9, trumpets -9 / -7;
  - reprise: strings short -18 (Violins I Spiccato -20, violas pizz. +30 against Violins II pizz. -12).
- Staccato strings, staccato winds and trumpets agree within 20 ms everywhere. The exception is the accents (finding 1).

**Trio legato tune against the harp.**
- Clarinet 1's joins sit +18 ms (456-504) and the harp's chords -16 ms: 34 ms apart. That is a slight lag of the tune behind the off-beat chords, smaller than a quarter of an eighth at quarter 228.
- Not a priority. If wanted: Clarinet 1 `LEG_LEAD_S` +0.015 s in 456-720.

## Findings, ranked by what a listener would gain

### 1. Accented notes now start about 40 ms before the beat and peak 0.1-0.25 s after it. c21's extra accent lead and c26's CC11 bump moved the start forward together; the weight did not move. The second bar of every theme statement (the accented half note) now rushes against the staccatos (measured)

**Where.** All 47 Violins I accents; the eight accented half notes of the soft theme statements (qn 39, 51, 69, 75, 759, 771, 789, 795, "Sus Marc LITE"); the cor anglais' 28 accents.

**Evidence (measured, S in ms, median per class).**

| | c20 | c24 | c26 |
|---|---|---|---|
| Violins I, soft accents (n 20) | -3 (lead 120) | -33 (lead 160) | **-40** (lead 160) |
| Violins I, tutti accents (n 27) | -4 (lead 80) | -19 (lead 100) | **-39** (lead 100) |
| Violins I theme half notes 39 / 51 / 69 / 75 / 759 / 771 / 789 / 795 | -7 / -16 / -17 / -7 / -6 / -10 / 0 / -7 | -64 / -50 / -60 / -45 / -82 / -74 / -70 / -64 | same as c24 |
| Cor anglais accents (n 28) | -4 | | **-30** (9 earlier than -40) |

- The steps line up with the data changes:
  - c21's `ROW_CHANGE_ACC_ADD_S` 0.04 s on Violins I (and the strings, Flute 2, Clarinet 2);
  - c25's +0.05 s on the cor anglais' accented onsets (`entry_leads.json`);
  - c26's `ACCENT_CC` "lead_s" 0.06: the CC11 bump starts before the moved note-on, so the tutti S went from -19 to -39 at an unchanged lead.
- The staccatos around them sit at -7..+6 ms, so each accent is heard 35-80 ms ahead of the line. At quarter 264 that is a third to two thirds of an eighth.
- Meanwhile the accent's weight still comes late. The median envelope of the accented half notes peaks at +0.08 s (soft Violins I) and +0.14 / +0.16 s (tutti Violins I / II); Oboe 1 peaks at +0.26 s. The stress is spread from 40 ms before the beat to 150-250 ms after it.

**Fix.**
- `build/score_config.py`, c21 block item 7: drop "Violins I" from the `ROW_CHANGE_ACC_ADD_S` dict, which removes its 0.04 s. Its accents get the front from the c26 CC11 bump, which already starts 0.06 s before the note-on.
- `build/entry_leads.json`: undo c25's +0.05 s on the cor anglais' accented onsets (keep 900).
- Keep `ACCENT_CC` lead_s 0.06 and Violins II / violas as they are: their S is -9 / -18.
- Targets on the next render:
  - Violins I accent S median within ±15 ms, none earlier than -40;
  - theme half notes -20..+10 ms;
  - cor anglais median within ±15 ms;
  - the accent fronts that A measures (first 100 ms over neighbours) no worse than c26 by more than 0.5 dB, because the bump stays.

### 2. In the ff tutti statements (bars 105-120, 305-320) the bar has almost no downbeat. The accented half notes are as loud on beat 2 as on beat 1, the c26 body dip lands after beat 2, and the violas' off-beat double stops (+4 dB role) are louder than the basses' downbeat (measured; the effect of the fix is inferred)

**Where.** qn 312-360 and 912-960: Violins I/II, violas, Oboe 1, Clarinet 2, cor anglais, double basses.

**Evidence (measured).**
- Downbeat weight (broadband / 2-5 kHz), median per bar:

| passage | master c25 | master c26 | mp3 c26 |
|---|---|---|---|
| theme A 13-28 (p) | +2.8 / +4.0 | +2.8 / +3.9 | +2.6 / +3.6 |
| tutti 105-120 | -0.3 / +0.9 | +0.3 / +1.4 | **+0.4 / +1.0** |
| tutti 305-320 | +1.0 / +0.9 | +1.2 / +1.7 | **+0.8 / +1.0** |

  The one-in-a-bar scherzo has a clearer downbeat at p than at ff.
- Per stem in 105-120, downbeat peak against beats 2-3:
  - weight on the downbeat: trumpets +10.5 / +12.4, low brass +6.5..+13.1, timpani +7.9, basses +9.5;
  - no weight: Violins I +0.1, Violins II +0.8, celli +1.0, cor anglais +0.2, Clarinet 2 +0.6;
  - violas: silent on 1, -32.5 dB on beats 2-3. That is within 1 dB of Violins I's melody (-31.6) and 2.8 dB over the basses' downbeat (-35.3).
  - 305-320 is the same, without trumpets and low brass.
- The accented half notes in the tuttis: level at beat 2 minus level at beat 1 is Violins I -0.7, Violins II +0.3, cor anglais +0.2, Oboe 1 +1.8, Clarinet 2 +1.4 dB (Flute 1 -4.4, the one that decays).
- c26's body dip (`ACCENT_CC` "body_s" (0.22, 0.36) from the moved note-on) starts about 0.12 s after the beat and is full only at about +0.26 s, after beat 2 (+0.227 s).
- The violas' off-beat "non div." staccatissimo double stops (v95, CC11 104-106) carry the c22 role row [312.5, 359.45, +4] / [912.5, 960, +4], which was meant for their slurred pairs.

**Fix (instrument side).**
- `build/score_config.py`, c26 block item 5: `body_s` (0.22, 0.36) -> (0.14, 0.24) on Violins I / II and violas, and on cor anglais, Clarinet 2 and Oboe 1. The dip is then full before beat 2. Keep `body_cc` -8 / -6.
- Violas: `VEL_SET["Violas"]` on the off-beat staccatissimo double stops on beats 2 and 3 of 312-359 and 912-959 (onsets with qn % 3 in {1, 2} on "Staccatissimo"): v95 -> v82. Range-test first: velocity picks the layer on HS short rows (c07), so check that the step is 2-4 dB and not 10.
- Keep the +4 role, so the slurred pairs (Dan's inner line) are not touched.
- Targets:
  - accented half notes at beat 2 at least 2 dB under beat 1 on those six stems;
  - violas' beats 2-3 at or under the basses' downbeat;
  - tutti downbeat weight at least +2 dB on the master and +1.5 dB on the mp3;
  - Dan's bar 23 figure and the violas' pair (fig25 / inner23) no more than 1 dB worse.

### 3. Soft string legato entries in the trio, codetta and Meno mosso reach their level 150-330 ms after the beat, more than an eighth late at quarter 228. More lead has not helped since c19. The finale's technique 139 (a CC11 front on the head) has not been tried (measured; the effect of the fix is from the finale)

**Where (score qn, track, velocity, CC11 at the note-on; times are the -12 / -6 dB points of the note's own peak):**

| note | data | -12 / -6 dB points |
|---|---|---|
| Violins I 528 | v53, CC11 49, the dolce espress. doubling of the celli's tune, sul A | +106 / +208 ms |
| Violins I 576 | | +110 / +330 |
| Violins I 603 | | +76 / +180 |
| Violins II 708 | lead already 300 ms | +72 / +146 |
| Violins II 1068 | | +130 / +206 |
| violas 708 | | +30 / +256 |
| violas 1020 | lead 300 ms | -56 / +216 |
| celli 1071 | | +98 / +240 |
| celli 504 (head of the celli's tune) | | +38 / +90 |

- The same notes at CC11 86 (Violins I / II at 624) reach -6 dB at +52..+66 ms.
- `timing19trio` S on these heads: Violins I 528 +151, 576 +204, 603 +160; Violins II 672 +198, 708 +132, 1068 +133; violas 1020 +86; celli 504 +69, 1071 +100 ms.
- c19 gave the same values (528 +144, 576 +204, 672 +289, 1068 +172), so they have not changed.
- Raising the lead to 258-300 ms (Violins II 672 / 708, violas 1020) did not bring them in. The slow part is the first-note sample at low CC11, not the start.

**Fix.**
- `tools/score_to_parts.py`: a generic rule, default off, e.g. `SOFT_LEG_HEAD_CC = {"families": ("string",), "rows": ("Leg",), "max_cc": 70, "rest_qn": 0.5, "add": 10, "pre_s": 0.06, "hold_s": 0.25, "gone_s": 0.45}`.
  - It applies to a legato-row note that follows a rest of at least `rest_qn`, at a resting CC11 of `max_cc` or less.
  - CC11 goes up by `add` units from `pre_s` before the moved note-on, holds to `hold_s` after it, and is back by `gone_s`. This is finale c26-c27 technique 139: attacks -12..+115 ms, were +140..+220.
  - It is a shape on the instrument, applied to every soft head, not a level for one note.
- Scherzo values in `build/score_config.py`, spans 456-720 and 1020-1128.
- Keep each head's present lead, and take back any lead over 0.12 s (Violins II 672 / 708, violas 1020) only if the head then reads early.
- Targets:
  - every listed head reaches -6 dB of its peak by +100 ms;
  - S within -30..+60 ms;
  - no head louder than the line it joins by more than 1 dB over its first 0.5 s (check on the celli's 504 against the Clarinet 1 / Horn 3 texture).

### 4. "Ritmo di tre battute" (bars 89-98): the round-robin resets at the group heads put the softest pizzicato sample on every head, so the bass line does not mark the three-bar groups (measured)

**Where.** qn 264-294, celli and basses pizz. on B every downbeat; `RR_RESET_AT` [264, 273, 282, 291] on both.

**Evidence (measured, 10 ms peak at each downbeat, dB).**
- Celli, by position in the group: head -48.0 / -48.3 / -48.3 / -47.0, second bar -45.7, third bar -45.3. The head is the softest, although it has v56 against v52.
- Basses: head -50.6 / -48.9, second -48.7, third -52.3.
- Together: heads -45.6 / -44.8 / -44.8 / -43.6 against -43.7 and -45.3. The heads are never the heaviest bar, and the 0.3 s level is flat within 0.7 dB.
- So the three-bar groups are carried only by the head entries (violas 89, Oboe 1 92, Violins I 95) and the timpani's f motive on the third bar (91, 94).
- The bars repeat exactly per group position (c18 had the same pattern), which shows the reset decides it. Manual p.145: the reset forces "a particular order of RR samples".

**Fix (instrument side; range-test the order first).**
- `build/score_config.py` `RR_RESET_AT`: move the resets so that each head falls on the loud sample.
  - Celli: [264.0, 267.0, 276.0, 285.0]. A reset in the bar after each head puts the head on the third sample (-45.3), between -48.0 and -45.7. Bar 89, after its own reset, stays on the first.
  - Basses: [264.0, 270.0, 279.0, 288.0]. The heads land on the second sample (-48.7), against -52.3 and -50.6.
- Expected, from these measured levels: heads +1.5 dB (celli) and +2.8 dB (basses) over the mean of the next two bars, with the round robins still varying.
- If the range test shows the samples follow velocity rather than position, raise the head velocity instead (v56 -> v63 celli, v41 -> v49 basses) and re-measure.
- Target: the combined low strings' head at least 1.5 dB over the two bars after it at 92, 95 and 98.

### 5. The celli's trio joins (+30 ms median by pcx) are on time by pitch. The late readings are a swell after on-time joins, so stop refitting `leg_leads.json` for them (measured)

**Evidence (measured, `pcx.py` on the c26 celli, 200 joins).**
- The crossover of the old and new pitch bands (42 spurious readings under -150 ms left out):
  - median +9 ms over the whole movement;
  - +8 ms in the tune 504-552;
  - +9 ms in the trio.
- pcx median +30 (tune +25, middle part 553-720 +37).
- 39 joins have their crossover within ±30 ms and their pcx later than +60 ms: the pitch changes on the beat and the level keeps rising for 0.1-0.3 s. Examples:
  - 542 (crossover +7, pcx +162);
  - 570 (-1 / +281);
  - 645 (+1 / +295);
  - the tutti countermelody's head at 312 / 912 (+10 / +256 and +47 / +251, with leads of 310-315 ms already).
- 542 moved from -89 (c25) to +162 ms after a 0.07 s lead change: a lead cannot hit a level rise.

**Fix.**
- Freeze the celli's `leg_leads.json`, and judge joins by the crossover (pcx's `cross`) from now on.
- If the swells on 542 / 570 / 645 are heard, give them the c24 celli counter-shape (`CC11_ADD_SPANS`: a few units down at the join, easing back over 0.3 s, the 516 / 526 mechanism) rather than more lead.
- Target: crossover median within ±15 ms (met now), and the level 0.3 s after each listed join within 2 dB of the level at +0.1 s.

## Do not touch

- The tempo map (RAMP_SPANS, the bar-2, G.P. and final steps).
- The sfp < at 301 (`cresc_after_fp`, the 902 lift +12, the ride row ending at 900).
- The c26 summit stroke and its counter-shape (peak at +0.18 s).
- The woodwind figure state (slur ends, caps, trails, Oboe 1 v118), except Flute 2's gap in the first tutti.
- Staccato and pizzicato leads in the theme statements (strings, winds and trumpets within 20 ms).
- The G.P. hall and the final fade.
- The celli's trio leads as they are.
- Bar 23's state, the Spiccato split, stretch_cc7 and the delivery chain.

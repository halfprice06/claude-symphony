# Cycle 06, critic C: dynamics over time (lens C2), on the c05 render

Sources: `cycles/c05/render/` (master and stems), the delivered `scherzo-mockup-c05.mp3`, the c00, c02 and c04 masters and mp3s for comparison, `cycles/c05/build_render/parts.json`, `build/score_config.py`, `build/roles.json`, `tools/score_to_parts.py`, `tools/deliver_master.py`, score pages 4, 8, 10, 12 and 13, and `build/mockup-events.tsv`. Levels are plain RMS dB on the parts.json tempo map unless marked LUFS. The LUFS values are EBU momentary loudness (400 ms), taken as the median per bar or passage. Bar b starts at qn 3(b-1). I ran delivery simulations with `tools/deliver_master.py` on the c05 master, writing only to my scratch folder (since deleted).

## Manual notes (cycle 6, slot C: group D2, May 2021 HO manual PDF pages 101-102, read in full with p.100; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.101, Sustain | Brass sustains take their dynamics from the Mod Wheel (CC1). All 4 dynamic layers play at once and CC1 crossfades them, so a crescendo can be made inside a held note. | The brass crescendos into the tuttis: bars 101-104 (qn 300-309), Hn 1-4 at 301-304 (900-909), the coda's brass at bar 332 (993-996). | Yes for the horns, trombones and tuba. CC1 rises 64 -> 86-108 (horns) and 29 -> 86 (low brass), and the stems grow 12-15 dB: Horn 3 -47.2 -> -32.9, Tuba -47.2 -> -32.5 (300 -> 309); Horn 1 -61.5 -> -29.5 (992 -> 996). Not for the trumpets in bar 103: CC1 drops back to 28 after the bar-102 rest (finding 4). Measured. |
| p.101, Sustain Accent | Velocity sets the accent's loudness and CC1 sets the sustain. | The score has no brass accents (coda.ily c200: "weight, not bite"). | Not loaded, which is correct. |
| p.101, Sustain Marcato Long/Short | Velocity opens a low-pass filter on the marcato attack, so harder playing gives a harsher front. | Nothing printed needs it. | Not used, which is correct. |
| p.101, Portato; Legato Repetitions | Re-tongued repeats inside a legato phrase; the same samples serve Legato Slur Repetition. | Horn 1's tenuto repeats at 630/633/663 (dips still 9.6-11.4 dB in c05). | Not used (MANUAL-GAPS #10, memory cap). This belongs to the articulation lens. |
| p.102, Short | Short articulations have no release trail. Play staccato notes connected so the room is heard between them. | Trumpet 1 on "StacSs DblTng RRx9" (56 notes). | Yes: staccato quarters are written at 0.5 qn, eighths at 0.25 qn. |
| p.102, Staccato | At the highest velocity the brass staccato includes overblowing (rougher, more upper harmonics). | Trumpet 1's staccatos in the ff tuttis (bars 105-120, 305-320) and the coda. | Trumpet 1's highest velocity is 96, so nothing overblows. That matches Dan's "weight, not bite". Measured in parts.json. |
| p.102, Shorts MOD SPEED | CC1 moves between staccatissimo, staccato and marcato. | None. | Not used. It must stay unused, because CC1 carries the brass dynamics (`CC1_DYN_TRACKS`). |
| p.102, Marcato | Four round robins. | None. | Not used. |

## Findings, ranked by what a listener would gain

### 1. The tutti sfp at bar 301 (qn 900) has no sf: the ff of bar 300 falls straight to the p in two steps (measured)

**Where.** qn 899.7-900.5, every sfp track: Flutes 1-2, Oboes 1-2, cor anglais, Clarinets 1-2, Bassoons 1-2, contrabassoon, Violins I, Violins II, violas, celli, basses (score p.10).

**What a listener hears.** Master in 50 ms windows: bar 300's body is -14.0..-15.1 dB. It drops to -20.9..-22.7 at 899.85-900.0 and reaches the p trough, -29..-30.7, by +0.25..+0.45 s. Nothing at 900 is louder than the ff before it. c00, c02 and c04 show the same shape (c00: -14.6 -> -17.2 at 900 -> -24 by +0.25 s), so no render has had an sf here.

Stems, 0.25 qn windows:

| Track | Before 900 | At 900.0 | At 900.25 |
|---|---|---|---|
| Violins I | -26.8 (899.75) | -30.2 | -37.0 |
| Clarinet 1 | -23.7 (898.5, the ff) | -43.0 | |
| Oboe 1 | | -43.2 | -35.4 (the "sf" arrives as a late swell) |

**Cause (read in parts.json).**
- **Strings.** The 900 notes have velocity 53 and sit on "Leg Slur MAX" (keyswitch 899.94). They abut the 899 notes (v111, ending at 900.0), so Opus plays a legato transition: no new bow and no attack. The CC11 spike (900.02, 114, held to 900.375, at 46 by 900.5) only holds the level of the note before. The score has an unslurred half note with a fresh down-bow at 301.
- **Winds.** Entry leads move the note-ons early: Oboe 1, Clarinet 2 and Flute 2 to 899.758, Bassoon 1 to 899.736, Flute 1 to 899.824, Clarinet 1 to 899.846. CC11 (46-51) and, for the clarinets, CC1 (42-58) at the moved onset are at p. The sf spike points stay at the score onset, 900.02 (CC11 114-119, clarinet CC1 108). So every wind note starts at p and swells 35-60 ms later.
- In the fp/sfp branch of `tools/score_to_parts.py` (about line 1787), the spike is written at the mark's score qn. The lead code then adds a point at the moved onset that carries the old level.

**Fix.**
1. Strings: in `build/score_config.py`, add 900.0 to `DOWNBOW_STROKE_AT` for Violins I, Violins II, Violas and Violoncellos (the fresh Sus MAX stroke path the hemiola uses at 902-910). Add `VEL_SET` {900.0: 105} on the same tracks. c01 found that strokes at velocity 52 speak 13-15 dB late, and c02-c05 used v85-112 for loud strokes.
2. Winds, generic option in `score_to_parts.py`, for example `FP_SPIKE_FROM_ONSET = True`: when a note with an fp/sfp mark has been moved early, start the spike at its moved onset ((qn - 0.01, level), (qn, spike)). The hold and the fall to p stay timed from the score qn. Fallback with no tool change: `entry_leads.json` 0.0 at 900.0 for the ten wind tracks, plus `VEL_SET` {900.0: 100} on them.
3. Keep c05's trough roles (Flute 2 -6, Horns 1-2 -3 over 900-906) and the c02 chain fix.

**Targets.** Master over 900.0-900.15 level with bar 300 (-14..-15 dB). Trough -28..-30 by 900.5-901 (unchanged). An sf of weight, not bite: the 2-5 kHz front of the strings no more than +2 dB over the note body.

### 2. Bar 364 (qn 1089): Horn 1's held G sharp jumps 12 dB in the middle of the closing chord's printed fade (measured)

**Where.** Horn 1, qn 1088.75-1097. The held note sq 1077 lasts 20 qn (bars 360-366). Score p.13: the chord fades pp > over 361-363, Violins I enter ppp at 364, Hn 1 decrescendos over 365-366 and re-enters pp at 368.

**What is wrong.** `roles.json` Horn 1 `[1089, 1128, 10]` (c02, written for "Hn 1's last G sharp") starts inside this held note. In parts.json, vol_db goes +3.5 (1080.5) -> +8.5 (1088.75) -> +13.5 (1089).

Measured, 0.5 qn windows:

| qn | 1088.0 | 1088.5 | 1089.0 |
|---|---|---|---|
| Horn 1 | -53.3 | -45.9 | -40.9 |
| Master | -46.1 | -44.0 | -40.6 |

So the horn rises 12.4 dB in about 0.25 qn (66 ms at quarter 228). The master rises 5.5 dB exactly where the score asks for the softest moment yet: the end of a pp decrescendo into a ppp entry. Bar 364 (-42.9) is 2.5 dB over bar 363 (-45.4), and Horn 1 there (-42.7) is louder than its own p espress. at bar 358 (-40.8 to -37.5 with its role).

**Fix.** In `build/roles.json`, change Horn 1 `[1089, 1128, 10]` to `[1100.25, 1128, 10]`. The role then reaches full value at the new note's moved onset (1100.772, the pp G sharp of bar 368) and covers the same last G sharp c02 aimed at. No held note sounds between 1097.1 and 1100.77.

Simulated on the c05 stems (Horn 1 stem -10 dB from 1089 to 1100.3):

| qn | 1089 | 1090 | 1091 |
|---|---|---|---|
| Master now | -41.3 | -42.9 | -45.4 |
| Master after | -47.4 | -49.6 | -52.1 |

The chord then fades evenly from bar 361 into the Violins I's ppp, and Horn 1 sits at about -52..-55 dB, under Violins I by 1092.

### 3. In the delivered mp3 the trio's ff climax (bar 218, qn 651) is no louder than its f at bar 197 or its f/mf at 222 (measured; fix simulated)

**Where.** Bars 196-224 (qn 585-672), delivered file only.

**What is wrong.** In the master the arc is right. Bar 218 measures -20.5 LUFS against -25.3 at 197 (+4.8 LU) and -26.2..-27.8 over 209-216 (+6).

The delivery ride gives the climax 2.7 dB of lift and the bars around it 6.8-8.0 dB. That is the 3:1 ratio below the knee (`deliver_master.py` `RATIO, KNEE_BELOW = 3.0, 5.0`). Delivered (median per bar):

| Bar | 197 | 199 | 218 | 219 | 222 |
|---|---|---|---|---|---|
| LUFS | -17.3 | -17.2 | -17.8 | -17.5 | -17.5 |

Maximum momentary: 218-219 -15.6 against 197-200 -16.0. A listener hears the f, the build of 209-217 and the ff summit of the trio at one level. The same flattening is milder at 50-55 (master +3.8 LU from bar 50 to 53, delivered +2.2).

**Fix (simulated with `deliver_master.py` on the c05 master).**
- **a.** Delivery-only rows in `build/score_config.py` `RIDE_TRIMS`:
  ```
  [(587.0, 0.0), (588.0, -2.0), (601.0, -2.0), (602.0, 0.0)],
  [(624.0, 0.0), (625.0, -1.0), (648.0, -1.0), (649.0, 0.0)],
  [(659.0, 0.0), (660.0, -2.0), (671.0, -2.0), (672.0, 0.0)]
  ```
  Delivered 218-219 is then -17.4 against -19.6 (197-200) and -20.5 (222-223): +2.2 / +3.1 LU. Maxima: +2.4 / +3.5. LRA 13.9, span 19.1 dB, limiter 3.0 dB. The summit is unchanged (336-339 -9.3, bar 304 -12.9).
- **b. Optional, with a.** `DELIVER_RATIO 2.5`, `DELIVER_KNEE_BELOW 6` (or the same constants on line 48). This raises the delivered LRA from 13.9 to 14.7 LU, inside the 14-16 target the c05 render missed. Trio climax +2.8 / +3.8 LU over 197 / 222. Span 19.7 dB. Summit 3.4 LU over bar 304 and 3.6 over bar 104. Limiter 3.3 dB, slightly over the 3 dB guide.

Take a.; take b. only if the limiter figure is acceptable.

### 4. Bars 101-104: the trumpets' printed pp < f crescendo restarts at pp after the bar-102 rest, so the second group is 5-12 dB softer than the first and the f jumps 18-25 dB (measured; cause read)

**Where.** Trumpets 1-2, qn 300-309. Score p.4: Tpt 1-2 pp with one hairpin from bar 101 through the rest of bar 102 and the group of bar 103, to f at 104.

**What is wrong.** Stem levels per quarter:

| Track | 301 | 302 | 306 | 307 | 308 | 309 (f) |
|---|---|---|---|---|---|---|
| Trumpet 1 | -45.4 | -45.0 | -57.5 | -52.6 | -49.9 | -31.6 |
| Trumpet 2 | -50.8 | -45.4 | -54.6 | -54.7 | -47.2 | -35.0 |

**Cause.**
- `hairpins_and_marks` in `score_to_parts.py` closes a hairpin "at the next rest of 2 qn or more". Bar 102's 3.5 qn rest ends the hairpin at 302.5/303.
- CC1 (the trumpets' dynamic, p.101) climbs 29 -> 52, then falls 46 -> 28 at 303.125-303.5. The bar-103 group (306-308) plays at CC1 28.
- Trumpet 1's velocities fall back to 58. Trumpet 1 also carries c04's flat -6 dB step over 299.7-308.75 (`LEVEL_SHAPES["Trumpet 1"]`).
- A census of every printed hairpin that this rule cuts with notes still to come before its printed end found the trumpets the only sustained case. The others are pizzicato bass lines whose velocities still rise (basses 108-120 grow +4.8 dB).

**Fix.**
1. Generic option in `hairpins_and_marks`, for example `HP_KEEP_ACROSS_REST_QN = 9`: a hairpin stays open across a rest when its printed stop or next dynamic follows within that many qn of the hairpin's start and the staff has notes in between. Config-only alternative: `SHARED_HP = {"Trumpet 1": [(300.0, 309.0, "cresc")], "Trumpet 2": [(300.0, 309.0, "cresc")]}`. Check in parts.json that the cut 300-302.5 hairpin does not survive beside it.
2. Turn Trumpet 1's flat step into a ramp: `[(299.5, 0.0), (299.7, -6.0), (308.75, -2.0), (308.85, 0.0)]`.

**Targets.** The bar-103 group 3-5 dB over the bar-101 group. The f at 309 6-10 dB over the bar-103 group instead of 18-25.

### 5. The fff summit's timpani roll (bar 336) vanishes within one bar, and the bar-332 mf < f roll does not grow (measured)

**Where.** Timpani, qn 1005-1008 (ff roll under the fff) and 993-996 (mf < f into bar 333). Score p.12.

**What is wrong.**
- **The summit roll.** Stem per 0.75 qn: -24.9, -34.5, -37.6, -42.2 dB. Its share of the master's 40-160 Hz band falls from -7.0 to -15.9, -20.3 and -25.4 dB. In parts.json the loud-attack bump (+9.6 dB at 1005.05) decays to +0.4 by 1007 and then -9 at 1007.95 (role -4 from 1007.9). CC7 is 67. So the fff downbeat has a timpani hit and then no roll. The other f/ff rolls sit at -10..-12 dB in this band (bars 101-103: -10.4; 301-303: -10.3..-11.7). mockup-kit LEARNINGS section 10 brought f/ff rolls to -5..-6 dB in 50-250 Hz.
- **The bar-332 roll.** -37.6, -38.4, -37.4, -39.1 dB: flat, 8-11 dB under the celli. CC7 goes only 48 -> 50, because the roll table separates mf and f by 1 dB, and vol_db goes 9.5 -> 9.1. Only CC1 rises (73 -> 88).

**Fix.** In `build/score_config.py`, `LEVEL_SHAPES["Timpani"]` +=
- `[(1005.7, 0.0), (1006.0, 5.0), (1007.0, 8.0), (1007.85, 8.0), (1007.9, 0.0)]`, so the roll body holds at about -29..-34 dB, still 7-10 dB under the top stems (-21..-23);
- `[(993.0, 0.0), (995.9, 5.0), (995.95, 0.0)]`, for 5 dB of growth into bar 333.

Keep `TIMP_DAMP_AT` 1014.5 and the -4 role from 1007.9. Dan's rule 5 is kept, because both rolls have a printed ff or crescendo and stay well under the strings. The levels after the fix are inferred.

### 6. The reprise's sub. p (bar 277, qn 828): the p espress. swell of Flute 1 and Oboe 1 reaches the level of the f before it within a bar and a half (measured; fix simulated)

**Where.** Flute 1 and Oboe 1, qn 828-840 (score: Fl 1, Ob 1, Bn 2 and celli sub. p; the flute and oboe espress. with < > hairpins).

**What is wrong.** Master per 1.5 qn:

| qn | 822 (bar 275, f) | 828 | 829.5 | 831 | 832.5 | 834 |
|---|---|---|---|---|---|---|
| dB | -28.6 | -37.3 | -37.9 | -34.7 | -29.6 | -34.0 |

At 832.5 the hairpin peak is 1.0 dB under the f. There Oboe 1 measures -33.1 and Flute 1 -35.6, against their own f in bar 275 (-40.5 / -45.4). Delivered per bar: 274 -17.1, 275 -18.5, 277 -26.1, 278 -21.2 (max -18.5, against bar 275's max -17.6). So the subito lasts one bar. The exposition's version (bars 121-124) stays flat at -29.6..-30.2 after a -15.7 ff.

**Cause.** c05's `LEVEL_SHAPES["Oboe 1"]` (+7, +2 at the hairpin peak, +4 over 827.5-840.5) sits on top of the soft-hairpin gain on both instruments. That was critic B's balance fix: oboe level with the flute.

**Fix.** Lower the pair by 3.5 dB and keep their relation:
- Oboe 1 shape values -3.5: `[(827.5, 0.0), (828.0, 3.5), (831.5, 3.5), (832.3, -1.5), (833.5, 0.5), (840.0, 0.5), (840.5, 0.0)]`;
- Flute 1's role 834-836 -3 replaced by `[828, 840, -3.5]` in `roles.json`.

Simulated on the stems: master 828-830 -39.6, 832.5 -32.6 (4.0 dB under bar 275), 834 -36.6.

## Also measured (not ranked)

- **Loop pulsing (BRIEF 8).** Autocorrelation at 3.95 s, measured on the 100-300 Hz band / the spectral centroid / the level:

  | Held note | Band | Centroid | Level |
  |---|---|---|---|
  | Violins I 0.5-23 | -0.53 | 0.00 | -0.20 |
  | Violins I 1089-1127 | -0.31 | -0.02 | -0.01 |
  | Horn 1 1101-1127 | -0.09 | -0.20 | -0.32 |
  | Horns 3-4 456-503 | -0.16 / +0.02 | -0.03 | |
  | Violins I harmonic 420-445 | -0.23 | -0.10 | |

  No held note pulses. The basses' +0.48 at 672-719 is the pizzicato bar pattern.
- **S3 at bar 121.** No vol_db fall over 2.5 dB under any sounding note at 358.5-361. The master falls 14 dB from bar 119 to 121 through CC11. Clean.
- **Summit (lens).** Delivered 336-339 -9.3 LUFS against 333-335 -12.6, bar 304 -13.0 and bar 104 -13.2. It is the loudest moment, and the G.P. is unchanged from c05.
- **Hairpin census** (stem level over the hairpin's last window against its first, hairpins of 2 qn or more): flat or reversed crescendos are wind 24 of 123 (11 counting the arrival), strings 9 of 94, brass 4 of 44. Most of the wind cases are short espress. swells on Flute 1 and Oboe 1 (bars 45-54, 125-130, 281-286) and the sfp crescendos, whose first window holds the sf.
- **Timpani rolls (Dan 5).**
  - 101-103: grows 6 dB, 3-6 dB under the celli.
  - 205-208: grows 11.5 dB and ends 0.4 dB over the violas (-36.3 / -36.7) in its last 2 qn, at the limit of the rule.
  - 237-240: 7-11 dB under the top stem.
- **Bars 9-12 (qn 24-36).** Timpani motive x, p, alone: delivered median -36.7 LUFS, 8 dB under the ppp close (-28..-29) and under every printed pp. The ride is at its +10 dB cap. A Timpani role [24, 36, +4] (post-hall, strokes only) would bring it near the bars 1-2 pp (inferred).
- **Delivered LRA.** 13.9 LU, under the 14-16 target. Finding 3 b. is the measured way back into the range.

**Do not touch:**
- the sub. p at bar 121 as a CC11 fall (14 dB, no envelope cut);
- the summit as the loudest moment, with `ARRIVAL_WEIGHT_AT` 1005 and the summit `RIDE_TRIMS` at 300-312 / 897-912;
- `TIMP_DAMP_AT` 1014.5 and the G.P. hall;
- the bar-101 and bar-301 roll growth (`TIMP_ROLL_TRIM_HOLD_CRESC` 0.6);
- the brass CC1 crescendos at 300-309 and 993-996 (horns on the soft map);
- the re-bow fills (no loop pulsing on any held note);
- the bar-72 decrescendo (master -15.3 -> -22.0 across the bar);
- the trio's mix arc (ff 218 4.8 LU over 197 in the master).

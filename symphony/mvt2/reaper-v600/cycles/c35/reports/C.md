# Cycle 35, critic C: tempo, timing and transitions (on the c34 render)

Material: `cycles/c34/render` (master and 32 stems), `cycles/c34/rendered_build/parts.json` (every qn-to-seconds conversion uses its tempo map), `cycles/c34/metrics`, `cycles/c33` and `cycles/c30` renders for before/after comparison, `build/{early_fills,entry_leads,leg_leads}.json`, `build/score_config.py`, `tools/score_to_parts.py`, `build/global.ily`, `build/mockup-events.tsv`, score pages 4-6, the May 2021 HO manual PDF pp. 99 and 147-149 (row T2 of `loop/MANUAL-READING.md`, cycle 35), `loop/MANUAL-GAPS.md`, and the c31 critic C report (the last tempo-lens report).

Methods (all measured from the score onset `sq`, on the tempo map):
- **Entries.** Stereo-power envelope, 20 ms window, 5 ms hop. The body is the level at +0.4..+0.9 s. b-6 and b-3 are when the stem first reaches body - 6 dB and body - 3 dB. 117 entries: notes after at least 0.45 s of silence and at least 0.6 s long.
- **Joins and group arrivals.** STFT with a 5 ms hop, on each track's own pitch: harmonics 1-4 ±3% with 4096 points, or harmonics 2-8 with 8192 points below MIDI 55. Crossover (co) is when the new pitch overtakes the old one and stays ahead for 60 ms. b-6 and b-3 are taken on the new pitch's own band. This covered 667 joins and all 171 onsets where three or more tracks start together. Bass-line readings disagreed between crossover and rise (shared partials), so I make no bass-join claims.
- **Breaths.** Level 30 ms windows; the dip is the minimum in [onset - 0.45 s, onset + 0.05 s] against the level at -0.9..-0.45 s.

## Manual notes (T2: PDF pp. 99, 147-149)

| What the manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| A legato transition needs "no significant time gap" between two notes; the first note of a phrase has no legato effect (p.99) | Every slur break (the pipeline ends a slur 0.05 qn early), every row change (Sus/Detache/Tremolo to a legato row), wide leaps and the bar 25 tutti re-entry | Partly. These notes correctly play as first notes, but most of them get **no lead at all**, so they arrive 0.15-0.37 s late (finding 1). |
| Legato rows are monophonic by default; CC22 64-127 makes them polyphonic and risks unwanted glides (p.99) | All legato rows | Yes. CC22 is never sent, and divisi run on their own tracks. |
| Legato Slur Staccato puts a slight slur-staccato accent on the first note of each legato phrase (p.99) | Phrase-first and slur-break notes | Not used. An option if the lead in finding 1 still leaves soft re-attacks dull (inferred). First check with `dump_ks.py` whether the string and wind KS Masters carry the row. |
| Bow-change legato has its own bow-change sound; Opus picks the components from the MIDI (p.99) | Leg BC MAX on unslurred and slur-to-slur string joins | Yes (string Leg BC crossover median +0.015 s). At qn 204 the strings' printed new bow under the tutti breath plays as a connected bow-change transition (finding 3). |
| Keyswitches select rows (p.99) | 358 keyswitches | Yes (measured). All come before their note: minimum 19.6 ms, median 36 ms. No clashes. Leg Slur/Leg BC switches under a sounding note keep the legato. |
| Violin finger positions (p.147). Note names are one octave low (C3 = middle C). At FP4, D5-D#5 (74-75) lie on the D string, and the A string runs E5-G#5 (76-80). At FP4 the D string covers G4-D#5 (67-75); E♭4-F#4 (63-66) go to the G string. | "sul A" Vln I/II 171-187; "sul D" Vln I/II 65-78, Vln II 237-250 | "sul A": yes (CC70 20 for ≤74 and 127 for 77/78, all on A). "sul D": **no** for the E♭4-F4 pickups at 65, 77, 237 and 249, which sound on the G string (finding 5). |
| Viola finger positions (p.148): at FP4 the C string reaches B3 (59) | "sul C" Violas 218-223 (55, 56) | Yes. |
| Celli finger positions (p.149): at FP4 the D string covers G3-C#4 (55-61); E♭3-F#3 (51-54) need FP1-FP3 | "sul D" Vc 66-90, 139-151, 238-259 | Partly. 34 notes play on the D string. 8 notes (E♭3/F3 at 69, 78, 80, 82, 238, 241, 250, 252) go to the G string, and 142 (E♭4) to the A string (finding 5). |
| Round-robin reset (p.145; 2025 p.92) | Repeatability | Timing repeats. Across 117 entries, the c33 -> c34 b-6 has median and p90 \|Δ\| of 0.000 s. The max is 0.07 s, at Vc 286, where c34 changed a role. CC16 is still open (MANUAL-GAPS #10). |

## Where c34 stands (measured)

- **Tempo map.** Unchanged since c30. Every printed tempo, rit., animando and allargando lands within 1-3%:
  - Bars 35-36: 49.2 / 45.0.
  - Bar 47: 58.0.
  - Bars 48-52: 54.0, 52.5, 52.5, 52.3, 52.8.
  - Bars 53-59: 60.0 rising to 64.0.
  - Bar 60: 59.9 without the caesura (the printed 62/58 gives 59.9).
  - Bars 61-63: 53.2, 53.2, 54.0.
  - Bar 64: 45.0 (printed mean 44.8).
  - Bars 78-82: 50.3, 48.7, 45.5 (caesura), 45.9, 44.0.
  - Bars 89-92: 48.4, 44.0, 39.9, then 36 and 20 on the last beat.
- **Final bar.** The chord holds 6.33 s, and CC11 goes 22 -> 8 over the last beat. All seven tracks release together at 348.23 s. The master falls about 30 dB/s after the release. The mp3 ends 1.67 s after the release, with the tail at -104 dB. Nothing is cut.
- **The c31 timing fixes held** (c30 -> c34, b-6):
  - Vln I 171: +0.353 -> +0.063
  - Vc 139: +0.326 -> +0.056
  - Vc 124: +0.221 -> +0.041
  - Vln II 59: +0.273 -> +0.043
  - Vla 78: +0.277 -> +0.047
  - Cb 140: +0.274 -> -0.001
  - Vc div 62: +0.241 -> +0.066
- **qn 204.** Every arrival falls within -0.045..+0.095 s (Cb crossover +0.165 -> +0.085, Vln II +0.11 -> +0.05).
- **Bar 79 run (262).** Vln I/II arrive at +0.010 / -0.005 against the flute's +0.015.
- **Legato crossover medians.** Strings +0.003..+0.043 s, winds +0.038..+0.085, horns +0.013..+0.068.
- **The gap between strings and winds (S2).** String entries still reach body - 3 dB later than wind entries: median **+0.157 s** (Leg Slur MAX, n = 30) against winds +0.03..+0.06. Most of that is now in the few notes below.

## 1. Re-attacks that follow a note with no rest get no lead and arrive 0.15-0.37 s late; unisons split (S2; measured)

The lead code (`score_to_parts.py`, the `shift[id(n)]` chain around l. 2940-3010) leads legato targets, entries after rests and a few special joins. A note that re-attacks right after the previous note falls through every branch and keeps lead 0. That covers:
- a new slur after the 0.05 qn slur-break gap;
- a change of row (Sus/Detache/Tremolo to Leg Slur, or Sus to Sus);
- a string leap over an octave;
- the Vln I tutti re-entry at 72.

Such a note plays the slow first-note layer (manual p.99). The worst cases, with their unison or doubling partner in brackets:

| track, sq (bar) | what it is | lead now | b-6 / b-3 (co) | partner |
|---|---|---|---|---|
| Violins I 249 (74 b3, mp pickup into the second A' phrase) | slur break after a 16-semitone leap, Leg Slur MAX v63 | 0 | **+0.215 / +0.235** | Vln II, same E♭4, Leg BC lead 0.17: -0.010 / +0.050 |
| Violins I 72 (25, "tutti, con sord.") | tutti re-entry inside the slur, Leg Slur MAX v63 | 0.06 | **+0.245 / +0.535** (co +0.145) | Vln II, same C5: +0.045 / +0.070 |
| Violins II 218 (64 b3, "sul G", p) | after the tremolo, 25-semitone drop | 0 | **+0.325 / +0.380** | Vla 218 +0.150, Tbn1 218 on time |
| Violas 218 ("sul C") | after the tremolo | 0 | +0.150 / +0.175 (co +0.135) | |
| Horn 1 208 / 210, Horn 2 210, Horn 3 210 (62, molto sostenuto tenutos) | Sus re-attack, 0.033 s gap | 0 | +0.245 / +0.145 / +0.180 (b-3 +0.355) / +0.120 | strings at 210: Vln II +0.020, Vc 0.000, Vla +0.030 |
| Oboe 1 210 | sostenuto repeat (`SOST_REP_S` 0.04) | 0.04 | **+0.260 / +0.315** | Vln II, same E5: +0.020 |
| Flute 1 116 (40, solo "dolce cantabile") | slur break | 0 | +0.185 / **+0.390** (co +0.16) | pizz. basses on the beat |
| Bassoon 1 144 / 198 / 261 | slur break / Sus -> Leg Slur | 0 | +0.190 / +0.215 / +0.190 | Vc 144 +0.015, Vc 198 +0.025, Horns a2 261 +0.005 |
| Oboe 2 267, Horn 3 267 (80 b4) | Sus -> Sus abutting / Sus -> Leg Slur | 0 | +0.300 / +0.165 (b-3 +0.59) | Vla 267 +0.005 |
| Violas 168, 252.5, 266 | Detache -> Leg Slur / slur break / Sus -> Leg Slur | 0 | +0.370 / +0.315 / +0.215 | |
| Clarinet 2 256, Horn 1 196 (59, after the breath, f) | Leg Slur -> Sus / Leg Slur -> Sus after the breath | 0 | +0.185 / +0.160 | Cl1 256 0.000; Bn1 196 -0.035 |

Two table entries are already dead:
- `leg_leads.json` Bassoon 1 "198": 0.12 never applies, because 198 is not a legato target (parts.json lead 0).
- Violas 266 has a 6 dB early fill. It lifts the level but cannot move the late pitch change (co +0.19).

The audible cases:
- **Bar 74 b3 and the bar 25 downbeat.** The two violin sections play the same note 0.2 s apart in the theme, which sounds smeared.
- **Bar 62 b3.** The horn and oboe chord change trails the strings by 0.12-0.26 s inside the ff Largamente.
- **Bar 64 b3.** The p sul G/sul C entries arrive a fifth of a beat late.

**Fix**, a generic rule in `tools/score_to_parts.py` with movement II values in `build/score_config.py`:
- **Option.** `REATTACK_LEAD_S = {}` by default; movement II `{"string": 0.15, "wind": 0.08, "brass": 0.10}`.
- **Which notes.** It applies only when no other branch set a lead, and only to a note that:
  - has a previous note on the track whose written end lies within 0.10 qn of its onset;
  - differs in pitch from that note (same-pitch re-bows and repeats keep their own rules);
  - lasts at least 0.4 s.
- **Lead.** The lead is converted on the real tempo map (`lead_qn`) and capped at 0.45 × the previous note's slot. The previous note's end moves with it to the moved onset - 0.02 qn, which keeps the re-attack.
- **Overrides and table hygiene.**
  - Add `REATTACK_LEAD_AT = {track: {sq: s}}` for per-onset values.
  - Let `leg_leads.json` entries on such notes count as overrides.
  - Print a WARNING for any `leg_leads` key that matches no led note (Bassoon 1 198 today).
- **Start values** (b-6 minus about 0.05 s, capped at 0.30):
  - Violins I: 249 0.18, 72 0.20.
  - Violins II: 218 0.25, plus `early_fills` `{"db": 4, "pre_s": 0, "hold_s": 0.15}`.
  - Violas: 218 0.12, 252.5 0.25, 266 0.15. Leave 168 (sotto voce, end of the portato) at the family value.
  - Horn 1: 208 0.20, 210 0.10, 196 0.10.
  - Horn 2: 210 0.15.
  - Horn 3: 210 0.08, 267 0.12.
  - Oboe 1: 210 0.20.
  - Oboe 2: 267 0.25.
  - Flute 1: 116 0.15.
  - Bassoon 1: 144 0.12, 198 0.15, 261 0.12.
  - Clarinet 2: 256 0.12.

**Check after the render:**
- every listed b-6 within -0.03..+0.08 s of its partner;
- the 50 ms peak in the first 0.6 s under body + 2.5 dB (Bassoon 1 261 and Violas 266 keep 6 dB fills that may overshoot once led; lower them by the overshoot);
- no new holes at the same-pitch neighbours (Violas 169.5, Oboe 2 268, Horn 3 268);
- that the Vln I 249 E♭4 still sounds for at least 0.3 s (its slot is 0.405 qn).

Gain: the largest timing fault left. It is in the theme's two exposed unisons and both Largamente bars.

## 2. Legato targets still late where crossover and own-pitch rise agree (measured)

The pair and onset leads of c31 brought most joins to +0.03..+0.08 s. Following the LEARNINGS c19 rule (act only when crossover and rise agree), these remain:

| track sq | interval | lead now | co / b-6 | doubled by | proposed `build/leg_leads.json` extra |
|---|---|---|---|---|---|
| Flute 1 200 (bar 60, top line, octave over Vln I) | 82->84 | 0.13 (extra 0.10) | +0.135 / +0.175 | Vln I -0.025, Vln II -0.030 | "200": 0.10 -> 0.20 |
| Oboe 1 271 (bar 82) | 70->68 | 0.06 | +0.180 / +0.170 | Vln II, same pitch, -0.035 | "271": 0.12 |
| Bass clarinet 30 (bar 11 b1, solo line) | 43->44 | 0.05 | +0.235 / +0.205 | Horn 1 +0.090 | "30": 0.15 |
| Clarinet 2 244 (bar 73) | 70->68 | 0.03 | +0.375 / +0.160 (rise +0.163) | | "244": 0.12 |
| Violins II 80 (bar 27 b3) | 72->77, Leg BC | 0.25 | +0.178 / +0.193 | Vln I 80 +0.170 (both late; Vc +0.035) | Vln II "80": 0.10 (clamped at 0.35); Vln I "80": 0.10 |
| Violoncellos 240 (bar 71 b3, "cantabile, sul D") | 51->56 | 0.22 | +0.135 / +0.210 | | "240": 0.08 |
| Flute 1 118 (bar 40 b3, solo) | 77->75 | 0.15 | +0.115 / +0.135 | | "118": 0.08 (added to the `LEG_PAIR_EXTRA_S` (77, 75) 0.12, which stays so 111 keeps its timing) |
| Horn 1 176 (bar 54, counter-melody) | 58->61 | 0.10 | +0.100 / +0.210 | Vln I 176 -0.030 | "176": 0.08 |
| Oboe 1 145.5, 146 (bar 46, the oboe/cello duet) | 69->70, 70->73 | 0.06 | +0.070 / +0.220; +0.095 / +0.225 | Vc 146 +0.075 | "145.5": 0.05, "146": 0.05 |

Also measured but not proposed: Oboe 1 140 and 189, and Bassoon 2 261. Their crossovers are on time (-0.015..+0.06) while their levels rise late, so a lead would make them early.

Re-measure after the render. Check the reverse steps (75 -> 77 Flute, 68 -> 70 Oboe) for early arrivals. Gain: the bar 60 flute top note and the bar 82 oboe are heard over the strings that double them.

## 3. The tutti breath at qn 204 (before bar 61) is heard only as lost time; 196 and 268 are inaudible in the master (measured; the cause is inferred)

On the master the breaths dip **1.5 dB at 204** (at -0.29 s, before the caesura), **1.8 dB at 196** and **2.7 dB at 268**. In 40 ms frames the master is flat at -16/-17 dB through the caesura at 204 and then rises.
- **The winds.** Their stems dip 10-20 dB (Cl2 20.4, Bn1 14.7, Hn1 13.4).
- **The strings.** They play straight through the 0.22 s caesura as Leg BC transitions: Vln I -25 -> -20 dB across the caesura, basses -37 -> -29.

The score prints a new bow for the strings at 204: Vln I up-bow < in bar 60, then down-bow ff tenuto; Vln II and the celli also re-bow; the basses have "change bow at will". So the 0.22 s stretch sounds like a dragged bar 60 rather than a breath.

The brief puts the third breath "before bar 82". It is at qn 268, which is bar 81's downbeat. There the violins' slur runs across, so 268 is right as it is. c31 C #6 proposed the same test and it is still open.

**Test** (204 only), with the pass criterion fixed before the render:
- **Strings.** Vln I, Vln II and Vc 204 as fresh strokes. The previous note ends 0.10 qn before 204's moved onset. The 204 note takes the loud family entry lead (plus `entry_leads` 0.04 if needed). This needs a generic `FRESH_AT = {track: [sq]}`, or a `BC_SOFT_SKIP`-style list that stops the Leg BC join at listed onsets.
- **Winds.** `BREATH_GAP_AT` for the 12 wind and brass notes ending at 204: 0.3 qn, `BREATH_FALL_CC` 6.
- **Pass:**
  - master dip in [203.75, 204] of 4-6 dB;
  - every string arrival at 204 within b-6 +0.06 s;
  - 2-5 kHz over the first 80 ms of the string re-attacks no more than 2 dB over the c34 level;
  - limiter no higher than c34's 2.6 dB.
- **Fail.** Revert to the c34 legato.

Gain: the climax's downbeat gets its breath. Smaller than findings 1-2, because the hall partly fills the gap anyway.

## 4. Six soft string entries still reach their level 0.11-0.20 s after the beat (S2; measured, fills simulated on the c34 stems)

The c31 fills fixed the worst entries. These remain, with no fill at present. I simulated each proposed `build/early_fills.json` shape (0 at onset - 0.02 s, +db at the onset, held to hold_s, 0 by hold_s + 0.25) on the c34 envelope:

| track sq (bar) | now b-6 / b-3 | proposed fill | simulated b-6 / b-3 | 50 ms peak over body |
|---|---|---|---|---|
| Violins II div 108 (37, Poco più mosso downbeat, Flautando) | +0.157 / +0.247 | `{"db": 4, "pre_s": 0, "hold_s": 0.20}` | +0.067 / +0.152 | -0.3 |
| Violas div 81 (28) | +0.199 / +0.214 | `{"db": 5, "pre_s": 0, "hold_s": 0.15}` | +0.044 / +0.194 | +2.1 |
| Violas div 78 (27) | +0.122 / +0.237 | `{"db": 3, "pre_s": 0, "hold_s": 0.12}` | -0.013 / +0.122 | +1.9 |
| Violas div 84 (29) | +0.109 / +0.174 | `{"db": 3, "pre_s": 0, "hold_s": 0.12}` | +0.034 / +0.109 | +1.6 |
| Violoncellos 238 (71, A' "cantabile, sul D") | +0.112 / +0.227 | `{"db": 4, "pre_s": 0, "hold_s": 0.15}` | +0.037 / +0.092 | -0.2 |
| Violins I 292 (89, coda) | +0.097 / +0.172 | `{"db": 3, "pre_s": 0, "hold_s": 0.15}` | -0.013 / +0.097 | -0.6 |

Leave Violas 66 and 279 (+0.15/+0.16). Their attacks already peak 2.5-3 dB over the body, and a 2.5 dB fill would put them at +3. At 108 the harp, pizz. basses and Flute 1 are on the beat (-0.04..+0.03). The div. sul tasto pad is the one late voice of the new tempo's downbeat.

## 5. "sul D" finger positions put the phrase pickups on the G string (manual pp.147-149; measured in parts.json, sound inferred)

`score_to_parts.py` l. 4641-4659 sets CC70 = 127 (FP4) for every note under "sul d/g/c", and for "sul a" 20 up to MIDI 74 and 127 above. Read against the p.147 and p.149 tables:
- **Violins.** The E♭4-F4 pickups (63, 65) that start each "espr., sul D" phrase sound on the G string at FP4:
  - Vln I and Vln II: 65/65.5 and 77/77.5;
  - Vln II also: 237/237.5 and 249/249.5.
- **Celli.** E♭3/F3 (51, 53) at 69, 78, 80, 82, 238, 241, 250 and 252 sound on the G string. 142 (E♭4) goes to the A string, beyond the D string's range at every FP.

**Fix:** choose the highest finger position that keeps the note on the printed string.
- **Violins, "sul d":** 62-63 -> 20, 64 -> 57, 65-66 -> 95, ≥67 -> 127.
- **Violins, "sul a":** 75 -> 95. No 75 is in the current span.
- **Violins, "sul g":** 127 as now.
- **Celli, "sul d":** 50-51 -> 20, 52-53 -> 57, 54 -> 95, 55-61 -> 127. Use the same values +12 for the violas.

**Check:**
- Do this as one MIDI change. Then compare the joins at the new CC70 change points with c34. Vln I 178 already crosses at +0.203 at a CC70 change against Vln II's +0.068, so a finger-position switch inside a legato phrase may cost transition time.
- If the joins at 65.5, 77.5 and 237.5 get later by more than 0.05 s, move the CC70 point 0.1 qn earlier into the previous note's tail.

Gain: a consistent D-string colour on the four phrase openings of the A sections. It is small next to findings 1-4.

**Do not touch:**
- The tempo map: `RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH`, `CAESURA`.
- The final bar, its CC11 fade and the joint release.
- Keyswitch placement and the pre-roll CC36/CC69 (timing repeats render to render).
- The c31 entry fills and leads: Vln I 171, Vc 124/139/152, Vln II 42/59/140/286, Vla 78, Cb 140, Vc div 62.
- The qn 204 leads and `ABUT_LEAD` `force_at` 152/204.
- `GROUP_LEAD_AT` on the bar 79 run.
- The string legato leads (crossover medians +0.003..+0.043 s).
- The 268 breath with the violins' slur across it.

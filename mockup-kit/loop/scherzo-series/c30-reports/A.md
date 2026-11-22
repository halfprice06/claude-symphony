# Cycle 30, critic A: articulation and phrasing (on the c29 render)

Material: `cycles/c29/render` stems (main pass plus `32_Timpani soft`), `cycles/c29/build_render/` (parts.json, mix.json,
roles.json as rendered), `cycles/c29/records/`, and `cycles/c18/render` as the felt-timpani and pre-CC7 comparison
(c18 is 3 dB hotter). Scripts were mine, in my scratch folder. Lanes come from a copy of build_reaper's `vol_points` /
`cc7_lane`, cut before ENV_LUA, with my own jobs folder; `ENV_NO_GUARD=1` gives the lanes without `note_move_guard`.
"Measured" means a number from the stems or the data. "Inferred" means reasoned from those numbers or the manual.

## Manual notes

`MANUAL-READING.md` has no row for c30, so I did no group reading. I used `MANUAL-GAPS.md` and the pages behind this
cycle's items:

| PDF page | what it says | where it applies | does the render follow it |
|---|---|---|---|
| 123 | Timpani Felt Long: "Note Velocity also controls dynamics"; LH zone C1-A2, RH zone C3-A4; strokes within 65 ms play a damped double hit | the felt alias (soft sticks 435-672 and 1020-1128, medium 672-864); motive x alternates hands (+24) | yes, except the coda's ppp strokes (finding 5): they use the pp velocities less 2-4 |
| 123-124 | Felt Rolls with CC1 in 8 levels; Felt Cresc rows | rolls 612, 708, 852 in the alias | yes. Rolls 612 / 708 / 852 are within 1 dB of c28 (records/timp.txt) |
| 101 | Sustain Accent: "The MIDI Velocity parameter controls the loudness of the attack"; CC1 / CC11 the sustained note | Flute 1's sfp at 900, where the row is already loaded (Flute 1 uses "Sus Accent MAX" at 902) | not used for the sfp (finding 4) |
| 64, 151 (MANUAL-GAPS c25) | CC7 is the relative level; CC11 shapes inside it | the CC7 trim lane | yes. But three role edges on the summit and one hairpin end land after led note-ons (findings 1 and 6) |
| MANUAL-GAPS #6 / #7 (c29 entry) | hard sticks for the Allegro; felt for the soft and medium spans in pass 2 | Timpani, Timpani soft | yes: the alias plays every stroke at c18's felt level and colour within about 1 dB |

## First check: Dan's figure at every occurrence (c29)

- **Strings** (`records/fig25.txt`, pitch-resolved): every Violins I and II step at all 20 + 15 occurrences equals c28.
  For example, bar 23 reads 78->79 17.1, 79->81 5.6, 81->83 8.7, 83->84 12.4.
  - Low values that were already in c28: Violins I bar 42 0.9, bar 70 0.8, bar 316 0.4; Violins II bar 315 81->83 0.6
    and bar 328 0.4 / 0.6.
  - None of my fixes touches these bars, except the optional Violins II 197.5 end in finding 3. Re-measure bar 66
    (Violins II 83->82 17.5, 82->81 2.2) if that end is adopted.
- **Woodwinds** (`records/fig29w.txt`, the harmonics 1-3 gate), Flute 1 / Flute 2 / Oboe 1 / Clarinet 2:
  - medians +14.7 / +15.8 / +20.2 / +23.4;
  - 0 crossovers under +3 on every track;
  - worst +9.3 / +7.0 / +10.6 / +6.3.
- **Verdict:** solved, and stable over two renders (measured). c30 compares against c29.

## Findings, ranked by what a listener hears (top three safe in one render)

### 1. The fff summit stroke (bar 336, qn 1005) swells in the strings. Their role edges sit at 1004.75, after the strokes' moved note-on at 1004.592, so 2-6 dB of the summit level arrives 0-150 ms into the stroke (measured; fix inferred)

**Where:** Violins I, Violins II, Violas and Violoncellos at qn 1005. These are three of the 33 "CC7 change in the first
50 ms" notes, and the only three of the 33 whose change spans the attack.

**Evidence, data** (CC7 in dB at the moved note-on, then at the score beat 1005; the envelope is flat across the note):

| track | moved note-on | CC7 at note-on | CC7 at 1005 | rise inside the note |
|---|---|---|---|---|
| Violins I | 1004.592 (lead 85 ms) | -6.2 | -4.0 | +2.2 dB |
| Violins II | 1004.592 | -8.4 | -2.5 | **+5.9** |
| Violas | 1004.592 | -10.6 | -7.4 | +3.2 |

- The rises come from the roles.json rows:
  - Violins I [1004.75, 1008, 5.0];
  - Violins II [996, 1004.75, -5] -> [1004.75, 1016, 0.5];
  - Violas [996, 1004.75, 1] -> [1004.75, 1017, 4.0];
  - Violoncellos [1004.75, 1016, -0.5].
- 1004.75 is not the onset of any note. `ROLE_EDGE_MOVED` therefore does not pin these edges, and each one ramps over
  0.5 qn ending after the led stroke has begun. `stretch_cc7` then carries the ramp in CC7.
- The winds' summit rows start at 1005 (an onset), so they are pinned before their moved note-ons, and none of the
  winds is in the list.

**Evidence, stems** (front = 0-80 ms, body = 150-400 ms after the moved note-on):

| track | front - body | peak | -6 dB point |
|---|---|---|---|
| Violins II | **-14.5 dB** | 210 ms | 140 ms (55 ms after the beat) |
| Violas | -8.2 | 320 ms | 90 ms |
| Violins I | -3.8 | 160 ms | 70 ms |
| Oboe 1 (pinned row) | +7.3 | 40 ms | |

- On the master (20 ms bins) the level is -21 / -22 / -21 dB just before the beat, then climbs -20, -19, -19, -18,
  -17 over the first 100 ms. The summit plays as a swell into the chord, not a downbeat.
- The summit step has been the weak point for four cycles (+1.1 to +1.8 dB against a +3 target).

**Fix:** `build/roles.json`. Move every 1004.75 edge to the stroke's score onset 1005.0:
- Violins I [1005, 1008, 5.0];
- Violins II [996, 1005, -5], [1005, 1016, 0.5];
- Violas [996, 1005, 1], [1005, 1017, 4.0];
- Violoncellos [1005, 1016, -0.5].

`ROLE_EDGE_MOVED` (0.03 s) then draws each step in the 30 ms before the moved note-on. That falls inside the rest after
the 1004 eighth: Violins I ends 1004.284, Violas 1004.31, Violins II 1004.332, so the rest is 54-64 ms. This is not in
a note body, so the guard leaves it alone. This needs `--midi-only` (a role change).

**Acceptance:**
- Strings' 1005 front minus body -3 dB or better, and the -6 dB point within 60 ms of the moved note-on.
- 2-5 kHz front minus body at 0 dB or lower (weight, not bite).
- Spec item 2 (summit lead, now +0.60 LU) not lower, and the summit limiter at 6 dB or less (now 3.9).
- The bar 334 figure (Violins I 1001-1003) unchanged.

### 2. The celli's countermelody head (bars 105 / 305, qn 312 / 912) is 4.4 dB under its own line because note_move_guard spreads the +4.5 role step into a 10-qn ramp (measured; fix simulated on the data)

**Where:** Violoncellos 309.6-321 and 909.6-921. Bassoon 1, Horn 3 and Horn 4 double the same line, ff espress.

**Evidence:**
- The role [310.6, 360, 4.5] (and [910.6, 960, 4.5]) ramps in at 310.1-310.6. That is inside the accented ff B2 half
  note (moved 309.56-311.716).
- The head G3 follows after only 0.02 qn (4.5 ms). The guard needs a rest of `rest_min_s` 0.04 s to place a step, so
  it rejoins at `rejoin_db_per_s` 2.0. At that rate the 4.4 dB takes 2.2 s (about 10 qn).
- Net level (envelope + CC7, dB):

| qn | 311.8 (head) | 313 | 315 | 317 | 319.6 | 322 |
|---|---|---|---|---|---|---|
| celli, c29 | -2.9 | -2.4 | -1.4 | -0.5 | +0.6 | +1.5 |
| celli, without the guard | +1.5 | +1.5 | +1.5 | +1.5 | +1.5 | +1.5 |
| Bassoon 1 | -0.1 | +2.3 | +2.3 | +2.3 | +2.3 | +2.3 |
| Horn 3 | +0.5 | +0.5 | +0.5 | +0.5 | +0.5 | +0.5 |

  The doubling instruments are at their level from the head on. Only the celli fade in.
- Stems, head 312-315 minus bar 106-107 (318-321), full band:
  - celli -4.5 / -4.9 dB (312 / 912);
  - Bassoon 1 -0.1 / -0.1 on the same line;
  - c18 celli -1.8.

  In the 300 Hz-5 kHz band the gap is larger (-9.0 on my measure, 5.3 / 5.7 in `records/trio_heads.txt`), because
  that band also cuts the G3's 196 Hz fundamental.
- So c29's Sus MAX head was not the cause: the guard ramp sits under it.

**Fix** (`build/roles.json` and `build/score_config.py` c30 block):
- roles: Violoncellos [310.6, 360, 4.5] -> **[312, 360, 4.5]** and [910.6, 960, 4.5] -> **[912, 960, 4.5]**.
  `ROLE_EDGE_MOVED` pins the step at 0.03 s before the head's moved note-on (311.736 / 911.736).
- `NOTE_END_AT["Violoncellos"] = {**..., 310.0: 311.5, 910.0: 911.5}`. The ff half note then ends about 54 ms early
  (a bow lift before the leap). The step falls in a rest the guard accepts.

**Simulation** (my copy of parts.json with the step at 311.55-311.6 and the B2 ended at 311.5, run through
vol_points / cc7_lane with the guard on):
- net -3.0 to 311.4, then **+1.5 from 311.8 to 322**;
- envelope 4.0 -> 8.5 in the rest;
- no in-note move;
- the same at 912.

**Acceptance:**
- In parts.json the B2 ends at 311.55 or earlier, and the head's moved onset stays at 311.736.
- Head minus line full band -1.5 dB or better (now -4.5).
- Guard and first-0.35 s gate counts not higher.
- Bar 105 on the master not lower. Its crescendo arrival was -0.5 dB, reversed; this should raise it a little
  (inferred).

### 3. The same guard mechanism carries other role edges onto later fresh notes: 46 note-ons sit 1.5-5.8 dB off their intended level (measured; optional for c30)

**Evidence:** net level 60 ms after each moved note-on, with the guard against without it (`ENV_NO_GUARD`), all
non-timpani tracks: 46 notes differ by 1.5 dB or more. The ones that change a phrase:

| track | notes | difference | cause |
|---|---|---|---|
| Violins II | bar 67, 198-201 (fugato) | **+4.7, +3.7, +3.3, +2.9, +2.0** over intended | the [192, 198, 5.5] entry lift does not end at 198: the moved 197.5 eighth ends 197.83 and the 198 note starts 197.85 |
| Bass clarinet | 264 (ritmo di tre battute) | **-4.9** at the onset, still -1.6 at 267 | role [240, 264, -5] end; 261 ends 263.79, 264 starts 263.85 |
| Violoncellos | 648-651 (bar 217 crescendo after the trio climax role) | -3.2, -2.2, -1.6 | role [623.6, 648, -3.5] end |
| Violoncellos | 840-844 | -3.0..-1.5 | role [828, 840, -3] end |

Also listed:
- Contrabassoon 312 / 912 / 1002 (+2.8..+3.7);
- cor anglais 144-148 (+1.9..+2.4) and 1001 (-2.5..-3.5);
- Horn 1 138-141;
- Horn 3 350 / 932-933 / 999-1001;
- Violas 618;
- Double basses 96 (+5.8: here the guard is keeping out a -6 dB fall inside the held 93 note, so leave it).

**Fix pattern, per edge:**
- Put the role edge on the score onset of the next fresh note.
- Give that note a rest of 0.04 s or more before it with `NOTE_END_AT` on the note before (0.18 qn at quarter 264):
  - Violins II {197.5: 197.65} (the 197.5 eighth is Dan's bar 66 figure, so re-measure it);
  - Bass clarinet {261.0: 263.6}.
- Do the celli 648 / 840 edges only if both legato notes allow the gap.

If time is short, do finding 2 alone and keep this list for the record.

### 4. Flute 1's sfp at bar 301 (qn 900) is inverted: its p is 3.4 dB louder than its sf. A CC7 rise of 6.5 dB at 900.5-900.625 cancels the CC11 fall (measured; fix inferred)

**Where:** the tutti sfp < of bar 301. S3 and Dan's "sf and sfp larger as printed".

**Evidence:** stems, sf = 0-150 ms after the moved note-on, p = 900.95 to the note's end (before the 902 accent).

| track | sf - p (c29) | sf - p (c18) |
|---|---|---|
| **Flute 1** | **-3.4** | -3.0 |
| Flute 2 | +1.0 | |
| Double basses | +0.8 | |
| Cor anglais | +2.2 | |
| Bassoon 2 | +3.3 | |
| Clarinet 2 | +3.5 | |
| Oboe 1 | +5.5 | |
| Violas | +8.7 | |
| Violins I | +9.0 | |
| Clarinet 1 | +11.4 | |

- Flute 1's lanes:
  - CC11 holds 122 to 900.45, then falls to 46 by 900.9;
  - CC7 goes -6.8 at the note-on, -8.5 at 900.375, then -4.2 at 900.5 and -2.0 at 900.625;
  - the p trim lands as the CC11 fall begins.
- The 10 ms envelope peaks at -35 dB at 120-160 ms. It returns to -34 at 260 ms: the p is as loud as the sf.
- The attack on "Sus MAX" v118 (`VEL_SET["Flute 1"][900.0]`) is slow: peak 160 ms.
- The other 30 of the 33 snap notes are not heard as events:
  - 13 are single steps 1-12 ms after the moved note-on, before the attack has built: the 384 group, the 900 group,
    Flute 1 142, Clarinet 1 306, Violas 984;
  - 10 are hairpin-trim ramps of 0.2-0.6 dB per 10-14 ms;
  - the bassoons' 210 / 894 shapes leave no front bump on the stems (Bassoon 2 -38..-39 dB flat after the join).

  Do not spend c30 time snapping them. The exception is finding 6.

**Fix** (`build/score_config.py`):
- `ART_SPANS["Flute 1"]` and `["Flute 2"]`: `{"from": 899.5, "to": 900.1, "art": "Sus Accent MAX"}` for the 900 note.
  Manual p.101: velocity sets the attack loudness. Flute 1 already loads the row for 902, so no new row is needed. Keep
  v118 on Flute 1 and give Flute 2 v110.
- If the fp's p level is a per-track setting, set the flutes' fp p CC11 to 36 instead of 46.

**Acceptance:** Flute 1 and Flute 2 sf - p +4 dB or more; 2-5 kHz front not over the oboes'; the 902 accent and the
crescendo to 909 unchanged.

### 5. The coda's ppp strokes "near the rim" (bars 371 and 374, qn 1110-1112 and 1122) are only 1-3 dB under the pp strokes before them. Otherwise the felt alias is right (measured)

**Evidence:** Timpani soft stem, per stroke; peak and 1-5 kHz share of the first 50 ms. c18 felt is shown at -3 dB.

| span | c29 against c18 | 1-5 kHz share, c29 (c18) |
|---|---|---|
| trio pp 444-561 | -54.6..-58.5 (c18 -52.9..-56.3) | -35..-41 (-36..-41) |
| f 597 / 624 | -31.2 / -32.5 (same as c18) | |
| medium sticks 720-803 | every stroke equal to c18 within 0.1 dB | |
| coda pp 1086-1100 | -47.3..-51.5 (c18 -47.5..-51.5) | |
| **coda ppp 1110-1112** | **-50.7..-56.9** | |
| ppp 1122 | -60.9 | |

- The alias plays soft and medium sticks with c18's felt colour and level.
- The "+1.9 dB over c28" in CHANGES is the felt level itself (c28 played hard sticks there). It is not a fault.
- Fault: ppp 1110 / 1111.5 (B2, v62) sit at -52.2 / -50.7 against pp 1098 / 1099.5 (v64) at -47.9 / -50.5. That is a
  4.3 and a 0.2 dB difference. 1111 RH v52 sits at -51.8 against v56 at -47.3.
- v62 and v64 are in the same Flt Lng layer. p.123: velocity controls the felt dynamics.

**Fix:** `VEL_SET["Timpani"] = {**..., 1110.0: 50, 1111.5: 50, 1111.0: 44, 1112.0: 44, 1122.0: 44}`.
- The alias copies the source's notes. Check in parts.json that "Timpani soft" carries them after `lh_vel_add`: LH
  strokes 50 / 44, RH 44.
- Acceptance: ppp strokes 4-6 dB under the 1086-1100 pp strokes, 1-5 kHz share not above theirs, and still audible over
  the bed (the master there is about -45 dB).

### 6. Oboe 1, bar 347 (qn 1038, dolce): a 4 dB CC7 fall lands 17-60 ms after the moved note-on and gives the note a 2-3 dB front lean (measured; small)

**Evidence:**
- The CC7 lane goes -4.6 (1037.875) -> -6.7 (1038.0) -> -8.6 (1038.038). The note is moved to 1037.81 (50 ms lead).
- This is the decrescendo 1036-1038 handing over at its score end, not at the moved onset.
- Stem, 20 ms bins from 30 ms before: -41 -39 -41 -42 -43 -44. The front is 2-3 dB over the body.
- No accent is printed.

**Fix:** let the hairpin-end level reach its value 0.02 s before the moved note-on of the note on the hairpin's end. This
is the end-side twin of `HP_START_MOVED`. If that is a tool change too large for the last cycle, leave it: it is the
smallest item here.

## Not ranked

- Accents (`records/acc2.txt`):
  - Violins I -3.8 dB under the detached note before, Violins II -2.3 (Dan's +1..+2 not met);
  - violas +0.2, celli +0.8;
  - no data change since c28.
  
  I do not propose a last-cycle change. Every lever tried (leads, body CC11, rows) is in HISTORY.
- Not re-measured this cycle (no data change in c29): pizzicato / arco, harp, con sordino, sul A, re-bows, the solo
  violin, the trio's legato joins (pcx: celli +29 ms, unchanged).

**Do not touch:**
- the c26 woodwind figure state and every string figure occurrence (gate 0 under +3; c29 equal to c28);
- the felt alias windows (435-864, 1020-1128) with their rolls and stroke levels, and the hard-stick Allegro with its
  region gains;
- `TIMP_RH_ALT` and the rolls' stroke ends;
- the pair-only Spiccato reroute and its layer cuts;
- the soft-head eighths v62;
- the tutti tenuto ends at q + 0.85;
- the Sus MAX leads on the tutti tenutos;
- the winds' summit rows pinned at 1005;
- Oboe 1's two cc7_spans_db rows;
- `note_move_guard` itself: fix its inputs by edges in rests, not the guard's thresholds.

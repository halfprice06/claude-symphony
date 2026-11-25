# Cycle 19, critic A: articulation and phrasing (on the c18 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b - 1). Levels are mean-square dB on the stems of `cycles/c18/render/`, read against `cycles/c18/build_render/parts.json` (the data as rendered). Comparisons use `cycles/c17/render/` with `cycles/c17/build_render/parts.json`. Join timing is measure S (`cycles/c14/actor_scripts/s14.py`, run by me on both renders). Join excess is `cycles/c18/actor_scripts/legx18.py`'s reading. "Measured" means a number from these files. "Inferred" means reasoned but not tested. Nobody heard the audio. Every fix below is on the instrument side (row, region volume in the Opus state, CC11 or CC1, velocity, note lengths and leads). None of them moves the track volume envelope.

## Manual notes (May 2021 HO manual, cycle 19 slot A: PDF pages 68-71, Hollywood Harp)

| what the page says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.68: the harp's mic set is for a solo instrument: vintage Close and Mid in place of the surround pairs | Harp and Harp harmonics tracks (`mix.json`: Close 0, Mid 0, Main -9 dB) | Yes. The standard Close / Mid / Main are used and no vintage pair; nothing in the score asks for a different colour |
| p.69: "Sustain RR" alternates Pluck Long and Thumb Pick by round robin at velocity 1-123 (5 layers each); velocity 124-127 selects Nail Pick on every round robin | every harp note (Harp track, `Harp Sus RR.oib`) | Yes (measured): 346 notes at velocity 40-65, none at 124 or more, so no nail pick. The repeated off-beat "non arpegg." chords show no pluck/thumb alternation in level: chord peaks have a standard deviation of 1.4-1.9 dB and an even-minus-odd difference of -0.3 to -0.6 dB in bars 81-84, 153-167, 185-192, 225-236 and 341-348 |
| p.69: the Maestro and Angels patches (Double Hit, Gliss Technique, Bisbigliando by CC1) | none: the scherzo has no harp glissando, tremolo or grace note | Not needed |
| p.70: "Harmonics" (individual patch): upper partials only, 2 dynamic layers by velocity | bars 149 and 151 (qn 445, 451) and bar 375 (qn 1123) on the Harp harmonics track | Yes: the 9 harmonic notes play on `Harp Harmonics.oib` at velocity 58 (the p layer). Not on the plain pluck |
| p.70: "Pluck" (5 layers) and "Thumb Pick" (5 layers) as separate patches | the trio chords, if the round-robin alternation were uneven | Not needed: no alternation is measurable (row above) |
| p.71: "Repetition Rep" lets an earlier pluck of the same pitch ring when a key is struck again | the trio's chords repeat the same pitches every bar | Not needed, and the render is right without it. On a real harp a re-pluck of one string stops that string; `score_to_parts.py` ends a ringing note at the next same-pitch onset (measured in parts.json: 457 / 458 / 460 / 461, pitch 56), with the 200 ms release of `env_release_ms` |
| (p.68-71 do not cover damping; the "étouffez" marks are handled by `HARP_RING_S` / `HARP_DAMP_TEXT`) | qn 258 (bar 87), 575.5 (bar 192), 717 (bar 240) | Yes (measured): the harp stem falls from -47 / -51 / -66 dB to silence within 0.25 s of each mark. The arpeggiated chords at 708 (bar 237) and 1080 (bar 361) are rolled at 0.15 qn steps |

From MANUAL-GAPS.md: no open harp item. Manual p.144 (Monophonic True Legato, read for finding 2) says that legato velocity sets the transition time "and does not affect loudness".

## Findings, ranked by what a listener would hear

### 1. LEG_TRANS_CC cannot reach the string legato swell: CC11 does not act on the transition sample. Remove it, and lower the transition groups' region volume (cause measured; fix inferred)

Where: every string "Leg Slur MAX" join. The exposed cases are the trio tune in the celli (bars 169-184), the second idea (bars 45-56, 121-140, 277-288), the solo (349-356) and the soft legato in the codetta and coda. Join excess on c18: median +3.1 dB, 91 of 429 joins over 6 dB (c17 +3.2, 87 over 6).

Evidence (measured; c17 and c18 compared at the 258 joins that received the dip):
- The two renders are identical to 0.0 dB from 0.1 s before the moved note-on to 0.05 s after it, at every depth. The swell peaks there, at a median of 70 ms after the note-on (65-80 ms per depth group).
- The dip first shows at +0.08 s. Its median is -1.6 to -1.8 dB at +0.17 to +0.23 s for the 9- and 12-unit joins and -0.5 to -0.6 dB for the 3- and 6-unit joins. The beat lies at +0.18 to +0.20 s, so the dip lands on the arrival note and not on the swell.
- Per depth: the swell peak changed -0.1 / -0.1 / -0.2 / -0.8 dB for 3 / 6 / 9 / 12 units. The new note's body (beat + 0.12 to + 0.45 s) lost 0.1 / 0.2 / 0.3 / 0.5 dB. The dip therefore made the sag after the beat slightly deeper.
- Side effect on timing: on joins whose lead did not change, S moved by more than 30 ms on 25 of the 235 dipped joins (median |dS| 4 ms) but on only 5 of the 223 undipped joins (median 0). The dip changes the band envelope that S reads. It has no effect on the swell.
- Cause. The swell comes from the transition sample, which Opus keeps in its own groups inside the row: "TLeg <pitch>" (132 groups in the Celli KS Master's "Leg Slur MAX", next to the "1V <dyn>" sustain groups; loop LEARNINGS 2026-11-15). A CC11 change that starts after the note-on does not reach that sample while it plays. Up to about 80 ms the samples are identical, so whatever acts later comes through the sustain. This matches Movement II's c21 finding that velocity does not remove these spikes, and manual p.144: velocity sets the transition time, not the level.

Fix:
1. Delete `LEG_TRANS_CC` (`build/score_config.py` c18 block 4, and `build/leg_trans.json`).
2. Add a group selector to `tools/build_reaper.py` `region_gain`. The layer key `"group:TLeg"` in `row_dyn_db` would match every group whose name starts with "TLeg": in the inner loop, `or (l_.startswith("group:") and gn_.startswith(l_[6:]))`. Then in `build/mix.json` `region_gain_db`, `{"row_dyn_db": {"Leg Slur MAX": {"group:TLeg": X}}}` with X per track from the c18 medians, keeping the woodwinds' +0.1..+1.1 dB as the measuring floor:
   - Violins I -1.5;
   - Violins II -2.5;
   - Violas -2.5;
   - Violoncellos -2.0;
   - Violin I solo (DIV A) -2.0;
   - Violas div (DIV B) -2.0.

   The region volume acts before the hall, so the hall follows it, and it changes only the transition sample (loop LEARNINGS 2026-11-11: region volume works per pitch).

Range-test before the full build on the celli at 504-552 (13 joins) and violas 693 / 726 / 1035. Check on the stems that slurred eighths do not fall under their neighbours: they are mostly transition sound (LEARNINGS 2026-11-15 / c17 note on short legato notes). Target: median excess +1.5 dB or less, 30 or fewer joins over 6 dB, slurred eighths within 1.5 dB of their c18 level.

### 2. Horn 1's motto-tail hole is the A4 to G sharp 4 legato transition sample. It recurs at bars 148 and 200. Velocity cannot fix it; re-attack the G sharp on "Sus MAX" (measured; fix inferred)

Where: Horn 1 "Leg Slur MAX", A4 (69) to G sharp 4 (68), slurred, at qn 442 (bar 148), 598 (bar 200) and 1077 (bar 360, the motto tail, exposed over the fading chord); also Horn 3 1026 (bar 343).

Evidence (20 ms frames):
- At 1077 the c17 render (velocity 106) and the c18 render (velocity 72) differ by 1 dB or less in every frame from 1076.5 to 1080. The hole sits at 1077.75-1078.0 in both, -50.6 dB against -35.1 at the beat and -39 at 1079.
- It is not phase cancellation: the L/R correlation in the hole is 0.73-0.76 and L and R both fall 15 dB. So velocity 72 (c18) did nothing, as manual p.144 predicts.
- Every Horn 1 legato arrival, measured as the minimum in 0.12-0.40 s after the moved note-on against the body at 0.4-0.7 s:

  | qn | velocity | hole under the body (dB) | at (s) | under the peak before it (dB) |
  |---|---|---|---|---|
  | 442 | 100 | 11.1 | +0.34 | 20.8 |
  | 598 | 106 | 9.4 | +0.30 | 19.9 |
  | 1077 | 72 | 10.9 | +0.32 | 18.5 |

  Every other Horn 1 slur is 6.3 dB or less, except the upward ones (9, 729), which only rise into a louder note. Horn 3 1026 (the same interval) reads 6.2 dB at +0.38 s. The fault belongs to this one transition of the 1FH patch.
- At 598 the G sharp lasts only 2 qn, so the hole is most of the note.
- Horn 1 on "Sus MAX" at CC1 58-60 reaches body - 3 dB in 0.04-0.06 s from silence (708, 1101, 420) and 0.16-0.18 s at 120 / 816.

Fix:
- `ART_AT` Horn 1 {442.0, 598.0, 1077.0: "Sus MAX"} (the row is loaded).
- End the A4 exactly at the G sharp's moved note-on, with no overlap. KS Masters turn an overlapping note on another row into a legato transition (kit LEARNINGS, c23 `SOST_JOIN_LEAD_S`).
- Lead the G sharp by 0.05 s.
- Keep the CC1 / CC11 lanes as they are.

The slur becomes a soft re-tongue at pp. That is a small liberty, and it is better than a 10-11 dB hole on the exposed note.

Alternative if the re-tongue is audible: Horn 2 is silent at 442 and from 1060 to the end. It could take a `HELD_DOUBLE` copy of the G sharp on "Sus MAX" from the score onset, with its CC11 falling to 0 over 1 qn after the hole (a CC shape on the copy).

Target: no fall over 4 dB inside 0.6 s of the arrival at 442 / 598 / 1077.

### 3. Accents: most of the 36 "over +3 dB" are the measurement window. The real outliers are soft string accents with a full 12-unit bump and the Violins I "Sus Marc LITE" halves. Keep the build/ revert of bars 18 / 258 (measured; fix sizes inferred)

Evidence (isolated accents; acc17's 0.35 s window against the first 100 ms of each note):
- Of the 36 over +3 dB on the 0.35 s window, 24 read +3 dB or less on the first 100 ms. They have a staccato eighth neighbour (0.11 s), which the 0.35 s window counts as a quiet note.
- One is a printed ff arrival (Bassoon 1 213).
- 11 remain:
  - Violins II 123, 195, 372, 819, 840 (+3.1 to +5.3);
  - Violas 144 (+4.0);
  - Violins I 285 (+4.1);
  - Oboe 1 144 (+3.8);
  - Flute 2 327 (+3.5);
  - Clarinet 2 345 (+3.5);
  - Clarinet 1 999 (+4.0).
- All 144 isolated accents on the first 100 ms: median -0.9 dB, p90 +3.0, 15 over +3.
- By resting CC11, strings:
  - under 60: median +1.1, p90 +4.4, 6 over +3;
  - 60-90: +0.9 / +3.6 / 4;
  - 90 and over: -1.0 / +1.3 / 0.

  A string accent with the same 12-unit bump is +5 dB at CC11 46 (Violins II 372: CC 46 to 57, +5.1) and nothing at CC11 105.
- Violins I "Sus Marc LITE" (36 notes):
  - The accented halves at velocity 56-64 (39, 51, 69, 75, 285, 759, 771, 789, 795) read +4.1 to +6.9 dB over their neighbours on 0-0.3 s.
  - The row layers a marcato short sample ("V1 Marc Shrt rrx1/2", velocity regions 1-65 / 66-108 / 109-127) over the sustain groups (1-127), so the first 0.3 s holds two samples.
  - The 2-5 kHz share of the first 80 ms against the body is -1.1 dB (51) and -2.2 dB (771) in c17, and -5.3 (285). The Marc row does not bite on this measure.
- The c18 change of 51 / 771 to "Sus MAX" lost 10.7 / 11.6 dB over 0-0.3 s (-33.9 to -44.6, -33.6 to -45.2). That is bars 18 / 258 -6.9 / -4.8 on the master. **The build/ revert to the theme row is right.**
- Violins II 195 (the fugato entry, +4.4) carries the c18 +30 lift from its note-on.

Fix:
- `ACCENT_CC` strings: a softer add when the resting CC11 is low. New keys `"soft_cc": 60, "add_soft": 6` in the `ACCENT_CC` block of `tools/score_to_parts.py`: under `soft_cc`, `add_soft` replaces `add`. At the strings' slope there (0.4-0.5 dB per unit) that is +2.5-3 dB. Default off.
- Violins I `mix.json` `region_gain_db`: `{"row_dyn_db": {"Sus Marc LITE": {"vel<66": -4}}}`. This touches only the 1-65 marcato short regions, which only the accented halves use. Their velocity-66+ eighths and the sustain groups are unchanged.
- Target: soft string accents p90 under +3.5 on the first 100 ms; Marc halves +2 to +3 dB over the neighbours on 0-0.3 s.
- Change the accent measure to the first 100 ms when a neighbour is shorter than 0.35 s (critic A c18 #5). The +3 dB count on the 0.35 s window is mostly that artefact.

### 4. The 14 half-step lead changes: 6 now inside 60 ms, 1 never applied, and 3 row-change eighths whose S does not follow the lead (measured)

S on c18 (ms; lead in ms), against c17:

| track, qn | c17 S / lead | c18 S / lead | note |
|---|---|---|---|
| Violoncellos 933 | -69 / 180 | **+30** / 146 | in; slope about 3 (overshoot) |
| Violoncellos 948 | -70 / 155 | **+26** / 120 | in; overshoot |
| Violoncellos 333 | -60 / 210 | **-44** / 180 | in |
| Violas 594 | -71 / 265 | **+18** / 230 | in |
| Violas 1056 | +88 / 225 | **+43** / 269 | in |
| Violins I 361.5 | +62 / 80 | **+40** / 111 | in |
| Violoncellos 348 | -127 / 210 | -78 / 147 | better, still out |
| Violins II 133.5 | -107 / 200 | -63 / 147 | better, still out |
| Violins II 134 | -90 / 230 | -72 / 185 | better, still out |
| Violins I 145.5 / 373.5 | -67 / 235, -68 / 235 | -60 / 202, -69 / 201 | 33 ms less lead moved S by +7 / -1 |
| Violins II 373.5 | -99 / 245 | -118 / 196 | 49 ms less lead, S 19 ms earlier |
| Violins I 597 | +92 / 132 | +92 / 132 | `lead_set.json` asks 0.178 s; parts.json's `lead_set` has no 597 entry and the lead stayed 132 ms. In `score_to_parts.py` (LEAD_SET_AT) `want_` is capped by `_prev_room` (`PREV_MIN_SOUND_S` 0.06 s after the previous note's moved note-on) and skipped when it equals the old lead (inferred from the code) |

Totals on c18: Violins I 3 outside 60 ms, Violins II 5, violas 2, celli 4 (c17: 4 / 3 / 2 / 4).

Six of the new ones (Violins II 374 -79 and 681 +61, violas 858 -84 and 1032 +77, celli 588 +79 and 647 +75) kept their c17 lead. All six are LEG_TRANS_CC joins (finding 1), so their S moved with the dip. Celli 163 (+77, c17 -9) is the one undipped mover, a round-robin take (finale c21 #8).

Fix:
- Do not refit any lead in c19 except Violins I 597. For 597, either remove the cap for that note (a `PREV_MIN_SOUND_S` exception list) or accept +92.
- After finding 1 removes the dip, re-read S. Then change only joins outside 60 ms on two agreeing renders (HISTORY c15: refit on two agreeing passes).
- Stop moving the three row-change eighths (Violins I 145.5 / 373.5, Violins II 373.5): their S does not follow the lead (slope 0 to -0.4). The cause is the row change, not the lead. Inferred: S there may be reading the "Stac" to "Leg" row change, not the new pitch. Check by eye on a spectrogram before any more lead changes.

### 5. Wind and brass joins: the 0.04 s overlap worked on pitch changes; REP_GAP_FLOOR_LONG_S did nothing; the notches left are S1 separations (measured)

Notch = mean of beat - 0.40..-0.20 and + 0.15..+ 0.35 s against the lowest 20 ms in beat - 0.15..+ 0.05 s, on the wind-and-brass stem sum.

Evidence:
- Pitch-change joins (3 or more tracks at one onset, both notes 0.4 s or longer, 21 onsets):
  - played gap median 14 to 8 ms;
  - notch median 1.9 to 1.1 dB, over 5 dB 3 to 0;
  - master 2.0 to 1.7.
  - Biggest gains: 606 (5.2 to 1.5), 1008 (4.1 to 1.9).
- 108 pitch changes overlap on the ≥0.4 s tracks I could match: Bassoon 2 53, Bassoon 1 16, cor anglais 13, Flute 1 12, contrabassoon 7 and others.
- All joins with no rest (190 onsets): notches over 5 dB fell from 29 to 16.
- The 16 left are of two kinds, and both are the printed articulation:
  - Staccato eighths before a quarter, gaps 94-144 ms (345, 351, 333, 207, 120, 951).
  - Same-pitch repeated chords: the coda build at 999, 11 tracks, notch 6.1 dB, master 4.2.
- Same-pitch held repeats: gap median 65 ms in both renders (47 onsets). `REP_GAP_FLOOR_LONG_S` replaces only the floor, and the `WIND_DETACH` gap (0.05 s / 12 % winds, 0.09 s / 18 % brass) is larger. Its `min_s` 0.6 also excludes the coda's 0.53-0.56 s halves.
- S1 on the short repeats (dip before the second of each same-pitch eighth pair) is unchanged to 0.2 dB on every track:
  - Violins I 5.9, Violins II 4.6, violas 4.7, celli 5.7;
  - Flute 1 8.2, Oboe 1 8.9, cor anglais 6.4, Clarinet 2 9.1;
  - Trumpet 1 4.5, Trumpet 2 3.6.
- The weakest pairs (1.5-3.0 dB: Violins II "Spiccato RRx9" 331 / 931, Violins I 955, Trumpet 2 994) are single samples on short rows. They play 36-62 ms of sound and leave 52-74 ms of gap.
- Clicks and cut-offs at the louder delivery:
  - No click (sample-step spikes 8x the local level) on any stem.
  - No fall of 30 dB in 50 ms from -42 dB or more.
  - The 25-30 dB falls in 100 ms that exist (Clarinet 1 "Leg Slur Rep" note ends at 312.5 / 912.5, trumpets at 358, basses 334 / 916 / 925 / 958, Violas div 639-657) sit under tutti or string texture. The master moves 1-3 dB there, so the hall covers them.

Fix:
- Keep `WIND_DETACH` `overlap_s` 0.04.
- Delete `REP_GAP_FLOOR_LONG_S` from `score_config.py` (a no-op) rather than tune it. The same-pitch notches are the separation S1 asks for.
- Leave the short-row repeats as they are.

### 6. Violins II fugato lift +24 (build/) is right (measured inputs; result inferred)

The c18 +30 units over 194.9-197 put Violins II's held note at -36.5 dB, 4.4 dB over the violas' -40.9 (0.48 dB per unit, actor's c18 table). In build/parts.json the lane at 194.462 is 66 instead of 72.

Expected effect:
- At the strings' slope there (0.4-0.48 dB per unit at CC11 66-72) the six units give -2.4 to -2.9 dB, so Violins II should end about 1.5-2 dB over the violas. That is half the error, as Movement II c57 advises.
- It also takes the 195 accent (+4.4 on the first 100 ms, finding 3) to about +1.5.

No further change before the render shows it.

## Checked and fine (measured)

- Harp: every item in the manual table. No nail-pick velocities, harmonics on their own patch, damps at 258 / 575.5 / 717, rolled arpeggios at 708 / 1080, off-beat chords even within 1.4-1.9 dB.
- S1: the theme head's repeated staccato eighths are unchanged against c17 on every section (finding 5).
- Note ends: no clicks and no exposed cut-offs at the -14 LUFS delivery (finding 5).

**Do not touch:**
- the c17 / c18 leads that are now inside 60 ms: celli 933 / 948 / 333, violas 594 / 1056, Violins I 361.5;
- `WIND_DETACH` `overlap_s` 0.04 on held pitch changes;
- the WIND_DETACH gaps on same-pitch repeats and the staccato rows and lengths of the theme head (S1);
- the harp's ring, damp and velocity settings and its Harmonics track;
- the build/ revert of Violins I 51 / 771 to "Sus Marc LITE" and the Violins II fugato +24;
- the Horn 1 mic pair, CC1 and CC11 lanes of the motto tail (only its row and note ends change in finding 2).

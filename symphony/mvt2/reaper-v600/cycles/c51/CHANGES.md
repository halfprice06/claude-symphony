# Cycle 51 (actor): printed tempo only, note starts fitted on critic A's S measure, critic B's four level rows

Rendered 2026-11-10 08:54-09:04 (one full render; two whole-piece range renders r1 and r2 for the lead checks).
Critic reports: `reports/A.md`, `B.md`, `C.md`. The lead notes (`lead_c51.md`, `lead_c51_inbox.md`) and one addition
relayed during the cycle (scherzo c13 points) were followed; where they differ from a critic, the lead notes won.

## 1. Tempo: a change of musical character (lead decision 1; A #1, C #1-#2)
The mockup now plays the printed tempo with no rubato beyond the print. To reverse it, delete the first c51 block at
the end of `build/score_config.py` (the c46 tables above it are untouched; `before/` holds the c50 files; the old values
are also kept in `_C46_TEMPO`), then rebuild every track with `--midi-only --tempo`.
- `PHRASE_ARCS = []` (so `APEX_AGOGIC` does nothing), `TEMPO_PUSH = []`, `BEAT_STRETCH = {}`.
- `CAESURA`: all 24 keys kept. Value 0.0 at the 14 with no printed breath (42, 48, 54, 60, 65, 77, 90, 96, 116, 139, 148,
  171, 237, 249) and at the 5 printed breaths that notes move through (164, 188, 196, 204, 259). Kept with time: the
  printed breaths that every part holds through: 29 0.18 s, 124 0.18 s, 286 0.16 s (critic C's reduced values) and
  102 0.15 s, 268 0.15 s (unchanged; both lie at or inside printed ritardandi). C's optional `CAESURA_SPAN_QN` was not built.
- Untouched: `RAMP_SPANS` (every printed rit., the animando, the Largamente), the fermata, `CAESURA_BREATH_S`, `CAESURA_LIFT`.
- New generic option `CAESURA_BREATH_QN_AT` (`tools/score_to_parts.py`): the gap of one listed caesura breath. 204 is set
  to 0.163 qn, which is the 0.174 s it lasted inside c46's slowed quarter beat (C's do-not-touch: the breath gaps at 204).
- Tables tied in seconds to a moved onset (`actor_scripts/qnshift51.py` lists every qn-keyed point whose offset from its
  nearest onset moved 20 ms or more): the four `JOIN_NOTCH` windows c46 had recomputed are back at their pre-c46 values
  (the same seconds on this map), Oboe 1's attack shape at 148 and the basses' pitch-trim hold at 148 follow their
  moved onsets. Other listed points are mid-note points of long shapes and were left.
- Measured on the map (`tempo_c51.txt`): 233 a-tempo beats; outside 0.5 % of printed: 4 (c50: 157), the same 4 outside
  3 % (c50: 103): the beats before the kept breaths, +15.6 % (28), +13.0 % (101), +18.0 % (123), +13.9 % (285). Longest
  beat with no printed mark: +0.0 % (c50: +42 %). Triplets a tempo even within 0.0 % (c50: 27 % at beat 115); in the
  printed ramps within 2.7 % (bar 60 sextuplets 174, 173, 175, 177, 176, 178 ms; c50 174 ... 209, 245). Length 346.04 s
  (c50 353.30; printed steps 345.33).
- Parts diff in seconds against c50 (`pdiff_c50_r1.txt`, `actor_scripts/pdiff51.py`): no note added or dropped, no
  keyswitch or articulation change, re-bow points and curved hairpins unchanged, no WARNING. Note ends moved only where
  a gap is defined in qn. Side effects: the basses' note at 204 is now 4.28 s (was 4.49 s), so the abutting 208 takes
  the 0.16 s `ABUT_LEAD` like its neighbours; the last two viola sextuplets of bar 60 take velocity 100 like the others.

## 2. Note starts (lead decisions 2 and 3)
- Measure: `tools/pcx.py` `robust_cross` and `s_start` (critic A's code) and new `tools/s_onsets.py` (every legato join
  and A's 26 lines; `--report` compares files). On the c50 render it reproduces A's table (214 / 76 of 411 outside 25 / 60 ms).
- Winds and brass (A #2, applied with A's exact values): 43 per-onset rows deleted (`build/leg_leads.json`), stacked
  extras removed (`LEG_EXTRA_S` Horn 1, old pair extras, Flute 1's `LEG_SOFT_EXTRA_S`), one row lead per track in
  `LEG_LEAD_S`, A's `LEG_PAIR_EXTRA_S` table, `SLUR_JOIN_LEAD_AT` Horn 4 268 0.05. Result, 263 joins: outside 25 ms
  97 -> 26, outside 60 ms 23 -> 2 (range render r1; unchanged in the full render).
- Strings (A #3 / #4): A's 109 rows applied, `LEG_CAP_FRAC` (181.0, 182.01, 0.75) on both violins. Guard on r1 (keep if
  S within 25 ms or closer than c50; `guard_r1.txt`, `leads_guard.json`): **101 kept** (91 within 25 ms), **8 reverted**
  to their c50 value (Violins I 197.5; Violins II 73.5, 85, 193.5, 196; Violas 109, 111, 249.5). The reverts lay in more
  than one passage, so a second range render r2 was made; with it a second pass of A's rule on r1 (9 new rows on joins
  still over 60 ms off with both estimators agreeing; `leads_pass2.json`): all 9 read closer in r2 and were kept
  (Violins I 193.5 only from +102 to -96 ms: it overshoots).
- A #5: Trombone 1 row lead 0.075, `REATTACK_LEAD_AT` {214.5: 0.04, 216: 0.05, 217: 0.05, 218: 0.04, 219.5: 0.10}, the
  212.5 entry extra 0.06 -> 0 (lead 50 ms): starts -6, +9, -16, -10, +15, +3, +17, +35, +6, -4 ms (c50 -65 ... +82).
  The run into 262: A's 0.05 s left 262 at +204 ms in r1; set to 0.08 / 0.06 s on the run and 0.15 s on 262: Violins I
  -30, -36, +14, +3; Violins II -40, +40, -20, -7 (c50 -98, -106, -53, +2 and -118, -49, -112, +93).
- Early fills (`actor_scripts/fillshift51.py`): 77 dict fills on notes whose lead changed by 20 ms or more moved with
  the note-on (pre_s + d, hold_s - d), computed from the c50 table each time.
- Result on the full render, all 26 lines (`S_report_c51.txt`, table below): outside 25 ms 214 -> **112**, outside 60 ms
  76 -> **28** of 411; slur neighbours over 60 ms apart 77 -> 32. All 727 legato joins: within 25 ms 377 -> 522, within
  60 ms 606 -> 678. The lead's aim (slur neighbours within 25 ms by S) is met on the wind and brass lines to within a few notes and not on the string lines.
- Violins I against Violins II on common onsets (82 in bars 22-30, 53-60, 70-78): more than 60 ms apart 18 -> **14**
  (2 + 5 + 7; r2 had 6), max 217 -> 184 ms (68, +184). Target (none over 60) missed. String join timing is not repeatable
  between renders: r2 and the full render were made from identical data (parts.json equal), and 35 of the 439 joins on
  the four string tracks moved 25 ms or more (20 by 60 ms or more), against 5 (1) of 284 on the other tracks. So about
  one string join in twelve cannot be held within 25 ms by any lead table.
- Heard lengths (A #4; scherzo point 2), heard / printed ms: bar 55 triplet Violins I 322 / 330, 324 / 330, 363 / 329;
  Violins II 267, 292, 347 (the first is 63 ms short; r2 had 365, 295, 347). Violas 111: 256 / 333, 111.333: 276 / 333,
  116: 283 / 333, 189: 197 / 324 (unchanged: its row is held by the 0.75 cap). No line note under 0.75 or over 1.3 of its
  printed length (c50: 4).
- Legato-row notes after a note on another row (scherzo point 1; `rowchange_c51.txt`): 186, of which 7 have no lead.
  Their S: Flute 1 212 +36, Bass clarinet 21 -66, Bassoon 1 271 +18, Horn 1 198 +16, Violas 269 -96, Violoncellos 218
  +59, Horns 1-2 a2 271 -43 ms. None is late like the scherzo's (+30 to +186); no data change.

Per line by S (ms), c50 against c51:

| Line | c50 min / max / median | c50 outside 25 / 60 | c51 min / max / median | c51 outside 25 / 60 | of |
|---|---|---|---|---|---|
| Horn 3, intro C-Db-C, bars 3-6 | -47 / +10 / +5 | 1 / 0 | -3 / +5 / +0 | 0 / 0 | 3 |
| Horn 1, theme A, bars 6-14 | -86 / +64 / -26 | 14 / 6 | -41 / +87 / +0 | 5 / 2 | 24 |
| Oboe 1, answer, bars 15-22 | -59 / +48 / -14 | 6 / 0 | -24 / +21 / -2 | 0 / 0 | 11 |
| Violin I solo, solo, bars 17-22 | -28 / +165 / +9 | 4 / 2 | -26 / +109 / +8 | 4 / 2 | 11 |
| Violins I, theme A, bars 22-30 | -59 / +102 / +2 | 10 / 3 | -41 / +126 / -0 | 10 / 2 | 24 |
| Violins II, theme A, bars 22-30 | -76 / +92 / -3 | 11 / 5 | -58 / +92 / -7 | 8 / 1 | 24 |
| Violoncellos, counter-melody, bars 22-30 | -73 / +122 / -18 | 10 / 5 | -64 / +73 / +12 | 8 / 3 | 19 |
| Bass clarinet, solo, bars 31-36 | -45 / +35 / -9 | 3 / 0 | -28 / +68 / -5 | 4 / 1 | 12 |
| Flute 1, theme B, bars 36-40 | -57 / +62 / +10 | 3 / 1 | -14 / +44 / +1 | 2 / 0 | 19 |
| Cor anglais, theme B, bars 41-44 | -110 / +24 / -15 | 3 / 1 | -18 / +20 / -1 | 0 / 0 | 14 |
| Flute 1, theme B answer, bars 41-44 | -114 / +32 / -51 | 10 / 2 | -4 / +46 / +2 | 1 / 0 | 12 |
| Oboe 1, B flat minor head, bars 45-47 | -62 / +50 / +11 | 6 / 1 | -34 / +66 / +18 | 3 / 1 | 10 |
| Violoncellos, B flat minor head, bars 45-47 | -66 / +14 / -6 | 4 / 1 | -54 / +70 / +1 | 3 / 1 | 9 |
| Cor anglais, quotation, bars 47-52 | -36 / +42 / -12 | 3 / 0 | -20 / +42 / +1 | 2 / 0 | 13 |
| Violins I, theme B, bars 53-60 | -80 / +74 / -8 | 18 / 5 | -96 / +88 / -9 | 10 / 3 | 30 |
| Violins II, theme B, bars 53-60 | -125 / +102 / -0 | 20 / 9 | -77 / +85 / -2 | 11 / 2 | 30 |
| Horn 1, counter-melody, bars 53-60 | -164 / +32 / -24 | 10 / 3 | -60 / +43 / +0 | 4 / 1 | 19 |
| Violoncellos, bars 53-60 | -98 / +70 / -17 | 9 / 4 | -40 / +44 / -10 | 4 / 0 | 19 |
| Violins I, climax, bars 61-64 | +11 / +229 / +29 | 3 / 2 | +14 / +229 / +30 | 3 / 2 | 6 |
| Trombone 1, quotation, bars 63-64 | -73 / +82 / +12 | 8 / 3 | -16 / +35 / +5 | 1 / 0 | 10 |
| Horn 1, motto tail, bars 65-70 | -47 / -13 / -36 | 4 / 0 | -22 / +6 / -4 | 0 / 0 | 5 |
| Violins I, theme A', bars 70-78 | -106 / +112 / -18 | 18 / 9 | -57 / +101 / -4 | 7 / 3 | 28 |
| Violins II, theme A', bars 70-78 | -133 / +38 / -25 | 19 / 8 | -78 / +100 / -11 | 11 / 2 | 28 |
| Violoncellos, counter-melody, bars 71-78 | -101 / +80 / -31 | 12 / 5 | -88 / +26 / -20 | 8 / 1 | 18 |
| Violins I, cadence, bars 79-82 | -87 / +41 / +2 | 3 / 1 | -86 / +21 / +1 | 2 / 1 | 9 |
| Clarinet 1, motto tail, bars 85-88 | +11 / +34 / +22 | 2 / 0 | -9 / +27 / +12 | 1 / 0 | 4 |

## 3. Critic B (all four applied; values rewritten for this map and these leads)
- B1 Flute 1 F5 at 108: shape +3 dB from the beat, +8 dB over the hole. Hole under the head 8.6 -> 4.1 dB; K level
  108.0-108.25 -40.9 -> -37.9, 108.25-108.5 -43.3 -> -37.9 (pickup -41.0). B's fallback limit was 4 dB; no velocity test made.
- B2 Violoncellos bar 73 shape -2.5 / +0.5: celli over Violins I at 246.0 +7.9 -> +4.3 dB K; C's conditions +1.4 (>= -1) and +4.4 (>= 3).
- B3 Bass clarinet 108 -3.5 dB (moved 45 ms later with the lead): peak of the first 0.45 s -38.6 -> -42.2 (C3 before it -45.0).
- B4 Flute 1 fill at 111 `hold_s` 0.30 (then shifted with the lead): 111.0-111.5 minus 110.5-111.0 -2.4 -> +0.5 dB
  (need >= -1.5): pass; 111.5-112.0 minus 110.0-111.0 +2.3 -> +2.6 (need <= 2.5): missed by 0.1 dB.

## 4. Render, state, checks
- Lock: waited for the turn 06:36:31-07:44:39 (68 min; scherzo, then the finale). Held 07:44:39-09:06:10: **1 h 22 min**.
  Sessions: start, settle, `--midi-only --tempo` on all 32 tracks (326 tempo markers, no mismatch), save, restart,
  r1; 4 string tracks `--midi-only`, save, restart, r2; Trombone 1 full rebuild, save, restart, settle, 45 s,
  `Audio_Init`, full render into a new folder, save, quit, unlock. No audio setting changed (CoreAudio, Mac Studio
  Speakers, 48000 Hz, 512, no input at every reading).
- State guard: 0 stale before the work, 0 after the first build; **1 stale (Trombone 1, 12 attacks 20 against 1076)** in
  the save after r1 and again after r2 (so r2's Trombone 1 stem is not valid); rebuilt in full; 0 stale before the
  render, inside `render_cycle.py`, in the save after the render and in the project saved by `quit`.
- Master -22.8 LUFS (c50 -22.9), LRA 23.4, true peak -3.7 dBFS, sample peak 0.654, no clipping, 37 files.
  Delivered -19.7 LUFS, LRA 14.7, TP -1.4 dBTP, limiter about 1.0 dB (c50 2.1), p10-to-max span 18.5 dB, length 347.40 s.
  Attack probe: late or hole 0. Motion dS4 p90 7.02, 1 s / 20 s 4.29.
- REAPER memory: 43 GB / 0.8 GB compressed before the render (no `--force-memory`), **43 GB / 33 GB compressed after**.
  Disk 40 GB free before the render, 37 GB at the end (range-render audio deleted, measurements kept).
- Wetness t20: strings 0.539 s (c50 0.361; limit 0.55), winds 0.284, brass 0.272; final chord t20 **0.46 s** (c50 0.444;
  limit 0.45, missed by 0.01), t10 0.285.
- S1 (`s1_c51.txt`, 49 points): own-band median dip 7.1 dB (7.4); under 3 dB: 6 (c50 3): the c50 three plus Violins II
  120 (2.6; c50 3.3), Violins II div 120 (2.0; 3.8) and Double basses 144 (1.0; 11.3), whose notes, gaps, CC11 and
  envelope are the same in seconds as in c50. S2: section 2. S3 (`check46_c51.txt`): steepest 10 ms fall at the caesuras
  at most 1.1 dB (139); master dip at the kept breaths 5.6 (29), 9.5 (102), 8.4 (124), 4.5 (268), 2.4 dB (286).
- state_check against c50 and c49: only 73 / 71 notes count as unchanged data (leads in seconds move every led note in
  qn). Its three runs (Clarinet 2 261-263, Violas 194-203, Double basses 112-134) are artefacts of comparing on one
  map: on each render's own map those notes differ by a median 0.0 / -0.1 / 0.0 dB (largest +1.1 dB). No level run.
- Re-bows (`rebow_c51.txt`): basses' pedal 220-238 dips 1.5-4.5 dB (c50 1.4-5.7), after 235.659 5.7 -> 4.4;
  Violoncellos div 275.527 2.5 -> 6.2 dB and 277.599 2.1 -> 3.8 (worse), 284.141 8.4 -> 7.0. Final chord re-bows within
  1.5 dB of c50 (the bars are inside the unchanged rit.). Violoncellos `JOIN_NOTCH` at 77 is back on its pre-c46 window.
- Trombone 1 (item 9): 2-5 kHz front minus body per note within 3 dB of c50 except 217 (-10.2 -> -14.6) and 218; body of
  217 +2.1 dB against c50 with its new 50 ms lead. No level change made.

## Rejected, deferred, open
- A #6 (wind legato velocity): deferred (lead). C #3 (fermata): no change asked. No MANUAL-GAPS item tried (no room).
- Open: the doubled violin onsets (14 over 60 ms) and the string lines' remaining 20-odd notes over 60 ms: string
  join latency is not stable from render to render once neighbouring data moves; Violins I 193.5 overshoot (-96);
  Violas 189 (cap); Horn 1 37.5 +87 ms and Bassoon 1 143 +88 (pairs A left out); Violoncellos div re-bow fill at
  275.527; S1 at Violins II 120 and basses 144; final chord t20 0.46; B4's second test; strings t20 0.539.

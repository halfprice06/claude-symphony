# Cycle 15 changes (actor, 2026-11-10)

Reports: `reports/A.md` (articulation, timing), `B.md` (balance), `C.md` (tempo, timing, transitions), all on the c14 render,
and the coordinator's rulings (`scratchpad/c15_actor.txt`). Priority of the cycle: steady note timing in the fast themes.
Snapshot of the tools and data before the cycle: `before/`. Scripts: `actor_scripts/`. Logs: `logs/`.

## What changed (files, parameters)

### Tools (`tools/score_to_parts.py`; every option has a neutral default)
- `STEADY_LINE` ported from Movement I c54 (`actor_scripts/port_steady.py` is the patch): a span of a track plays one row,
  with one lead per class (slurred, new bow, entry after a rest, same-pitch repeat) and per-onset `at` rows; slurred notes
  end `overlap_s` after the next note-on, a new bow `gap_s` before it. parts.json `steady_line` rows
  `[score qn, row, lead s, end minus next note-on s, class]`. Added here: `level_db` steps with `level_default` {row: dB}
  and `level_all` (the steps also act on the span's staccato notes).
- `SHORT_SUS_LEG_SPANS` {track: [(from, to)]}: slurred eighths of 0.20-0.25 s stay on the legato row inside the spans.
- `RETONGUE_LEAD_SPANS` {track: [(from, to, s)]}: a re-tongue lead per span.
- `ROW_LEAD_KEEP_GAP` {track: {row: [(from, to)]}}: the note before a led stroke ends earlier by the lead, so the gap
  before the stroke keeps its length.
- `LEG_VEL_STRONG` takes a track key before the family key.
- Phrase-arc depth `"light"` (`PHRASE_SLOW_LIGHT` 0.99 / 0.975, no push).

### Item 1: the first theme on one row (`build/score_config.py` c15 block, `build/steady_leads.json`, `build/steady_levels.json`)
- `STEADY_LINE` "Sus MAX" on Violins I, Violins II, Violas over 40-104 and 600-680 (spans 40-72, 72-104, 600-632,
  632-664, 664-680) and on Violoncellos and Double basses over 104-136. Printed staccato quarters keep "Staccatissimo
  RRx9" / "Stac RRx9" / "Staccato RRx9". `overlap_s` 0.02, `gap_s` 0.03, `rep_gap_s` 0.05, chords included.
- Accented halves (40, 52, 56, 68, 72, 84, 88, 100, 600, 612, 616, 628, 632, 644, 648, 660; low strings 104, 116, 120,
  132): their own lead class ("acc", start 0.09 s) and a +3 dB front (`LEVEL_SHAPES_S`, +1 dB on 40 and 600).
- The c14 strokes, stroke leads, row-trim marks, the head shape at 40 and the lifts at 42 / 74 / 602 inside the spans are
  removed. `ROW_TRIM_DB` is skipped inside the spans (`ROW_TRIM_SKIP`); the levels are `level_default` per row plus the
  per-note steps fitted on the range renders (`actor_scripts/fit15.py`).

### Item 2: fixed-offset classes
- Violins I's countersubject 104-136: a `STEADY_LINE` span (already "Sus MAX"): slurred 0.07 s, heads 0.02 s, third eighths
  0.03 s (start values), no level steps.
- Violins I's octave theme 632-664 and the violas' leggiero eighths 72-104 are inside the item-1 spans with start leads
  of 0.08 / 0.09 s.
- `ROW_LEAD_S` "Sus MAX" (328, 392) on Violins II and Violas 0.11 -> 0.06 s. Violins I (969.5, 976.5) 0.10 s.
- Low strings' staccato quarters: `STAC_LEAD_S["Double basses"]` 0.04; Violoncellos "Stac RRx9" (104, 136) 0.05 s.

### Item 3: second theme
- `SHORT_SUS_LEG_SPANS` Violins II and Violoncellos (264, 328): the eighths at 283-284.5, 299-299.5, 309.5 are legato-row
  notes again; the c14 strokes at 310 are removed. Violins II 300 is "Leg Slur MAX" > "Leg BC MAX" as on Violins I.
- `leg_leads.json`: A's eleven corrections; Violins II 300 back to -0.046; start rows for the new legato eighths.
- `entry_leads.json`: Violins I 744 total 0.30 -> 0.17 s and no +5 dB front there; Violoncellos 264 0.30 -> 0.21 s. The
  +5 dB fronts at 264 (Violins I / II) end at +0.20 s instead of +0.40 s.

### Item 4: codetta and the basses' eighths
- `entry_leads.json`: Trombone 1 360-369 -0.05, Bass trombone -0.02, Horn 1 355-360 -0.06, Trumpet 2 360-365.5 -0.04;
  Violins II and Violas 360 / 364 / 369 +0.05, Double basses +0.04, Violins I 369 +0.06.
- Double basses 1056-1108: the on-beat 0.03 s leads of c12 are deleted; off-beat eighths lead 0.035 s (1056-1088) and
  0.03 s (1088-1108), with `ROW_LEAD_KEEP_END` and `ROW_LEAD_KEEP_GAP` over (1055.98, 1108).

### Item 5: winds and brass
- `LEG_ART_EXTRA_S["Clarinet 1"]` "Leg Slur" 0.02 s. `RETONGUE_LEAD_SPANS["Oboe 1"]` 0.03 s in 536-600, 792-816, 1088-1108.
- `LEG_PAIR_EXTRA_S`: Oboe 1 (79, 77) +0.06, (77, 76) +0.035, (74, 72) 0.10 -> 0.065; Horn 1 (59, 62) +0.05, (50, 53) -0.06,
  (65, 64) -0.13 (it cancels the F4 source extra on the falling semitone).
- Horn 1: entries 40, 64 -0.06, 614 -0.04, "Sus MAX" entries 72, 664 -0.06 (`entry_leads.json`); stopped note 668 0.12 s
  (`ROW_LEAD_S` "Stop Sus"). Trumpet 1 200, 984 -0.06; Trombone 1 984.5 -0.10.
- Cap test: `LEG_VEL_STRONG` "Horn 1" / "Trumpet 1" `[(52, 100), (65, 106), (127, 112)]` (switch `C15_BRASSCAP`).
- Horn 1 "Marc Shrt RRx4" velocities in 40-104 15 steps lower.

### Item 6: balance and dynamics
- Bars 222 / 245: celli counter-shapes on the two G2 whole notes and +4 dB fronts at 884 / 976; Violins I / II new bows
  0.08 s early (Violins I 976 0.10 s) with +3 dB fronts; Violins I "Sus MAX" through 884-888.
- `note_trims.json`: Double basses 264 +5, 268 +4, 270 +5, 288 +3; Flute 1 406 -5, 418.5 -3, 422 -4; Clarinet 1 406 -4;
  Oboe 1 406 +3, 72 / 600 / 632 +4; Trumpet 1 1084 -4; Oboe 2 888 / 1108 -4. `roles.json`: Flute 1 [404, 408, +1.5] removed.
- Bar 42: +2 dB on the five string tracks over 164-167, ramped out by 168.
- Head shapes: Violoncellos 1064 -3, Clarinet 2 1056 -4.
- Release fades after the stops of bars 2 and 6 (celli, basses): -6 / -5 -> -4 dB.

### Item 7: tempo
- `CAESURA` 72 and 632: 0.03 -> 0.02 s. `PHRASE_ARCS` (680, 696), (712, 728), (744, 760), (760, 776): "sub" -> "light".
  Total length 423.83 -> 423.76 s. No re-bow point or re-bow fill key moved (parts.json `rebows`, `rebow_fill_ends` equal).

### Added from the coordinator's relayed notes (Movement II c52 / c53, Scherzo c13)
- `KS_LEAD_SPANS` (tools) {track: [(from, to, s)]}: the keyswitch of each remaining row change on the first-theme spans
  (Violins I / II, Violas 40-104 and 600-680, Violins I 104-136, Violoncellos / Double basses 104-136) goes 0.15 s before
  its note. Tested on the second theme too in R1 and removed there (below).
- Start shapes: `build/steady_fronts.json` (fit15.py: notes of 0.6 s or longer whose first 0.5 s is more than 3 dB under
  the body get a level-only start shape from the note-on). The cello front at 264 now starts at its note-on.
- Each range pass is rendered twice after a build (R1a / R1, R2a / R2); the first is only compared, the second is fitted.
- `wait_lock.py`: on equal start times the folder whose root path sorts first goes first.

## Range tests under the lock (logs in `logs/`; S = the earlier of pcX and the band crossover, c14 = the c14 full render)

Ranges (qn): 37-138, 262-330, 326-374, 598-682, 742-794, 838-894, 934-990, 1054-1110; each starts 2 qn before a section
reset. R1 = the pre-lock build; R2 = after the fits on R1.

| segment (lines) | notes | c14 out 25 / 60 ms | R1 | R2 |
|---|---|---|---|---|
| bars 11-26 (Violins I, II, Violas, Horn 1) | 256 | 104 / 30 | 74 / 12 | 77 / 18 |
| bars 27-34 (Vc, Cb, Bn 1, Tuba, Violins I) | 175 | 77 / 12 | 64 / 15 | 60 / 11 |
| bars 67-82 (Violins I, II, Vc) | 140 | 64 / 20 | 87 / 37 | 53 / 7 |
| bar 90 | 15 | 1 / 1 | 2 / 1 | 1 / 1 |
| bars 151-170 (Violins I, II, Violas, Horn 1, Tpt 1) | 325 | 118 / 29 | 107 / 20 | 93 / 18 |
| bars 187-198 (Violins I, II) | 62 | 27 / 5 | 36 / 20 | 25 / 5 |
| coda 2 (Trumpet 1) | 16 | 8 / 4 | 8 / 4 | 8 / 4 |
| all range lines | 989 | 399 / 101 | 378 / 109 | 317 / 64 |

Decisions taken on the range renders:
- **Class leads** (`build/steady_leads.json`, fitted on R1: old lead + the class's median S): accented halves 0.05-0.12 s,
  slurred 0.05-0.10 s, entries 0.03-0.09 s per track and span. Violas bars 11-26: 46 / 19 -> 25 / 5; Violins II 20 / 1 ->
  12 / 1; Violins I 15 / 1 -> 18 / 4 (its notes over 60 ms in R2: the entries after rests at 40, 48 and 61, +71..+102 ms,
  and 88 at -74 ms).
- **Keyswitch 0.15 s early**: kept on the first theme (sustain and staccato rows: 0 of the listed moved notes between
  R1a and R1 lie on these lines). Removed on the second theme: with it the legato-row joins read +36..+45 ms later at
  the median (Violins I bars 187-198 12 / 3 -> 17 / 11 with no other change on most notes); without it (R2) the second
  theme reads 53 / 7 and 25 / 5.
- **Brass velocity cap 112** (`logs/captest_R1.log`): Horn 1 bars 11-26 robust SD 69 -> 48 ms with one note 2.7 dB down,
  bars 151-170 33 -> 23 ms, Trumpet 1 coda 2 31 -> 39 ms. The conditions (under 25 ms, no note down more than 2 dB) hold
  on one of three lines: cap off (`C15_BRASSCAP` default 0), the c14 ladder stays.
- **Basses' off-beat leads** (`logs/chk15_R1.log`, envelope half-rise): off-beat +50 / +68 ms with the leads (c14 +54 /
  +39), on-beat +4 / +1 (c14 +10 / -30). The off-beat rise did not follow its note-on: block off (`C15_CBLEADS`
  default 0), c14 leads kept. Open for c16.
- **Levels** (`build/steady_levels.json`): per-note steps fitted on R1 and refitted (level only) on R2. On R2 the head falls
  3-6 dB to its second note on every string line (c14: 6.6-8.7 dB at bars 11 and 19), the staccato-row median is within
  2.5 dB of the "Sus MAX" median on each span, and the spans' RMS is 0.0-1.9 dB under c14 before the last refit.
- **Long notes on "Sus MAX"** (R2): end minus start -4.0..+4.3 dB on the violins (two notes over 4 dB, both rising),
  two viola notes fall 5.8 / 6.5 dB, one cello note 7.0 dB, two bass notes 6.3 / 12.5 dB (open: body shapes on those five);
  start against body within 3 dB on all but Violas 676 (start shape added). No slurred join has a stretch
  12 dB under the notes' bodies (dip median 2.5-3.7 dB, largest 9.0 dB): the slurred pairs read as joined, no pair is
  kept on an overlap exception.
- **Codetta** (S at 360 / 364 / 369): spread 129 / 166 / 120 ms in c14 -> 93 / 30 / 68 ms in R1; four rows trimmed again.
- **Bars 222 / 245**: master step at 884 -2.8 dB (c14) -> -1.5 (R1) -> -1.2 (R2, fronts +5 / +6); at 976 -2.3 -> -0.4 / -1.6.
- State guard after the two range rounds: Double basses stale (8 attacks differ); rebuilt in full, then 0 stale.

## The c15 render (one full render, from a restarted REAPER at 44 GB, 0 compressed; `--force-memory` not needed)

- Master -20.6 LUFS, LRA 22.9 LU, true peak -1.3 dBFS (sample peak 0.864). Delivered mp3 -19.8 LUFS, LRA 14.8 LU,
  -1.5 dBTP, limiter about 2.1 dB, p10-to-max span 19.4 dB. Attack probe: 0 late or hole. All 35 stems present.
- REAPER memory after the render: 45 GB, 0 compressed. State guard before the render 0 stale; in the project saved at
  quit after the render: Violoncellos stale (52 attacks differ). **c16 must rebuild Violoncellos in full before its
  first range render.**
- Lock: taken 21:58 on 10 Nov, released 05:44 on 11 Nov. Working time under it 74 minutes (21:58-22:25 phase 1,
  04:57-05:44 the rest); between the two the actor was stopped by the usage limit for 6.5 hours with the lock held.

### Timing on S (`logs/render/S_table.log`; c14 / range R2 / c15, notes outside 25 / 60 ms)

| segment | notes | c14 | R2 | c15 |
|---|---|---|---|---|
| bars 11-26 | 256 | 104 / 30 | 77 / 18 | 79 / 18 |
| bars 27-34 | 175 | 77 / 12 | 60 / 11 | 61 / 12 |
| bars 51-66 | 41 | 10 / 1 | - | 10 / 0 |
| bars 67-82 | 140 | 64 / 20 | 53 / 7 | 54 / 9 |
| bar 90 | 15 | 1 / 1 | 1 / 1 | 1 / 1 |
| bars 151-170 | 325 | 118 / 29 | 93 / 18 | 90 / 16 |
| bars 171-186 | 65 | 20 / 5 | - | 21 / 5 |
| bars 187-198 | 62 | 27 / 5 | 25 / 5 | 26 / 3 |
| bars 199-210 | 151 | 53 / 9 | - | 51 / 9 |
| bars 211-222 | 16 | 8 / 4 | 8 / 4 | 7 / 4 |
| bars 235-246 | 33 | 17 / 6 | - | 15 / 3 |
| bars 247-270 | 120 | 56 / 23 | - | 54 / 19 |
| all lines | 1399 | 555 / 145 | - | 469 / 99 |

Targets: under 400 / 80 not met (469 / 99). First theme, outside 25 ms: Violins I 15 -> 21 (bars 11-26), 32 -> 29
(151-170); Violins II 20 -> 13, 34 -> 16; Violas 46 -> 22, 25 -> 22; outside 60 ms: Violins I 1 -> 4 and 10 -> 2,
Violins II 1 -> 1 and 6 -> 0, Violas 19 -> 4 and 4 -> 6. The target "under 10 each" is not met. Violins I's
countersubject 29 / 2 -> 15 / 1. Row changes left inside the first theme: Violins I 16 + 16, Violins II 16 + 8, Violas
8 + 16, Violoncellos 8, Double basses 8, every one between "Sus MAX" and the staccato row (none onto or off a legato
row; c14: 36, 36, 23, 19, 17 in bars 11-34 with 19, 19, 13, 11, 10 on the legato side).

### Items, measured on the render
- Item 3: A's corrections: Violins I 296 -100 -> -12, 312 -92 -> -16, 747 -75 -> -4, 779 -111 -> -15 ms; Violins II 296
  -81 -> -21; Violoncellos 264 -89 -> -7, 286 -178 -> -32, 298 -141 -> -16, 304 -167 -> -5. Violins I 744 -148 -> +72 ms
  (target within 40: not met, the 0.17 s lead without a front is too short; c16: about 0.22 s). Violins II 300 +86 ->
  -59 ms (row fix done; lead row needs +0.05). Bar 67 entries +63 / +46 ms.
- Item 4: codetta chords, S spread first to last: 360 129 -> 105 ms, 364 166 -> 30, 369 120 -> 41 (target under 60: met
  on two of three; at 360 Trombone 1 -49 and Double basses +56). Basses' eighths: c14 values kept (range test).
- Item 5: Horn 1 entries 40 -50 -> -16, 64 -77 -> -6, 72 -58 -> +7, 614 -62 -> +18, 664 -70 -> -10, stopped 668 +189
  -> +67; pair (65, 64) at 993.5 / 1009.5 -152 / -128 -> -37 / -22; Trumpet 1 200 -89 -> -30, 984 -88 -> -32; Trombone 1
  984.5 -124 -> -40. Clarinet 1 bar 90 median +12 -> -3. Horn 1 theme lines 23 / 9 and 27 / 9 -> 23 / 9 and 23 / 8.
- Item 2: Violins I 970 / 972 / 973 / 976 +108 / +156 / +96 / +102 -> +2 / +56 / -8 / +2 ms.
- Item 6: bar 222, master 0-0.3 s after 884 against 0.3 s before: -2.8 -> -0.8 dB (target 1: met); strings' lowest 40 ms
  window after the beat -10 / -12 / -14 -> -4.5 / -7.0 / -6.1 dB. Bar 245 (976): -2.3 -> -1.6 dB. Bar 42: master bars
  41-43 -38.3 / -42.6 / -44.9 (c14 -38.3 / -44.8 / -44.7): the p is 2.3 dB over the pp, steps 4.3 and 2.3 dB (bars
  39-42: 5.3 / 4.6 / 4.3); mp3 41 -> 42 2.9 dB. Bars 272 -> 273: master -21.8 -> -21.2 (+0.6 dB; c14 -0.1), mp3 +2.4 dB.
- Stops, master drop at +0.3 s (`logs/render/stops.log`): bar 2 17.7 -> 17.4, bar 6 17.9 -> 18.0 (limit 17 not met:
  the -4 dB fades changed little), bar 94 16.6 -> 15.6, bar 113 19.5 -> 20.5, bar 166 14.9 -> 18.1 dB (drier: the theme's
  last notes now end on "Sus MAX" with the 150 ms release cap), bar 204 14.4 -> 14.3; final chord unchanged (14.9 dB,
  RT60 1.27 s). **Open for c16: bar 166 (and bars 2 / 6) over the 17 dB limit.**
- Bars 75 / 90 / 150 re-measured: bar 75 Violins I G / A flat / F -34 / +13 / -8 ms (unchanged), Violins II -31 / +46 /
  -64 ms (c14 +11 / +50 / +83); bar 90 Flute 1 +17, Oboe 1 +14, Clarinet 1 +12 ms on the F at 358; bar 150 as c14
  (releases at 599 reach -20 dB in 76-214 ms on the winds, entries at 600 unchanged).

## Rejected or deferred
- A #2 brass velocity cap: rejected on the range test (numbers above). A #6 (C3 repeats 987.5 / 995.5): not worked on.
- C #4 basses' off-beat leads: rejected on the range test; c14 leads kept.
- C #2.4 / #2.5 (Piu allegro and introduction span leads), C's Violins II 264-328 one-row test, A's combination-row
  test, B's Trumpet 1 +3 dB at 844 / 851: not done (outside the ruling or no room in two range rounds).
- Item 8: the keyswitch test became part of items 1 and 3 (kept on the first theme, removed on the second);
  `REP_OFF_FAMILIES` on winds and brass not tested: c16.
- Not met: S totals, Violins I / II first theme under 10, Violins I 744, Violins II 300, codetta chord 360, stops at
  bars 2 / 6 / 166. Entries after rests on "Sus MAX" (Violins I 40, 48, 61, 600, 608: +62..+114 ms) are the largest
  remaining class in the theme.

# Cycle 11: changes (actor, on the c10 render)

Snapshot of the tables and tools before this cycle: `cycles/c11/before/`. Scripts: `cycles/c11/actor_scripts/`
(`apply11.py` table edits; `fit11.py` per-onset legato offsets, run once, do not rerun; `predict11.py` predicted attack
times from lead changes; `check11.py CYCLE [PARTS]` the per-finding measurements; `m11.py` helpers; `vdata11.py`,
`envd11.py`, `volenv11.py` data and volume-envelope checks without REAPER; `unchanged11.py` per-note comparison of two
renders; `stemdiff11.py` per-half-beat comparison of two renders; `splice11.py` the stem repair; `ride_ramps11.py`,
`ridechk11.py` delivery ride checks; `wait_mem.py`). Data as rendered: `cycles/c11/build_render/`. Measurements:
`cycles/c11/check_c10.txt` and `check_c11.txt` (the same script on both renders), `cycles/c11/records/` (note diff,
envelope diff, unchanged-track comparison, state guard results, ride levels, metrics before the stem repair).

STATUS: rendered 2026-11-09 17:02-17:10 (`render_cycle.py 11 --force-memory`), checked. No stem fix. After unlocking,
five horn spans and three brass-return spans (4.5 s of 286 s) were replaced from the c10 stems (section "Render").
Lock held 16:44:46-17:23:14 = 38.5 min (the 10 min waited behind Movement II before that are not counted).
mp3: `cycles/c11/scherzo-mockup-c11.mp3`.

## 1. Critics' findings

All levels are K-weighted dB unless noted. "pcX" is the perceived attack time in ms against the score onset, with the
previous note's pitch excluded.

| finding | status | change | measured c10 -> c11 |
|---|---|---|---|
| A #1 / C #1 note after a slurred eighth late in the strings | accepted, Violins II in part | `tools/score_to_parts.py`: new `LEG_CAP_FROM_MOVED` (the legato lead cap is measured from the previous note's moved onset). `score_config.py`: `{"Violins I": None, "Violas": None, "Violoncellos": None, "Violins II": 0.5}` (Violins II only after notes of an eighth or shorter: its runs of quarters were on time on c10 at the capped lead and the full lead would put them 45 ms early). `fit11.py` added 35 negative per-onset offsets to `build/leg_leads.json` (key `_c11_fit`) for joins that `predict11.py` put under -40 ms | Joins, median, count over +60 / over +100 / under -40 ms: Violins I +49, 49 / 19 / 1 -> +15, 19 / 5 / 9; Violins II +3, 15 / 9 / 17 -> -2, 8 / 3 / 20; Violas +6, 16 / 6 / 17 -> +3, 10 / 6 / 17; Violoncellos +27, 51 / 26 / 27 -> +7, 34 / 13 / 33. The worked example (Violins II 134) +179 -> under +60; Violins I 134 +135 -> under +73 |
| A #2 Horn 1's call, bars 3-5 | accepted; G#3 short of target | `leg_leads.json` Horn 1 `"9.0": 0.10`; `RETONGUE_LEAD_AT` Horn 1 `6.0: 0.13` (new option; the G#3 is a re-tongue after a 0.13 qn gap, where an `entry_leads.json` extra removes the lead); `LEVEL_SHAPES["Horn 1"]` over the E4 (9.6-14.7, down to -6.6 dB at 12.0, placed for the new note-on) | pcX E4 (9.0) +155 -> +53; G#3 (6.0) +84 -> +83 (target +40 not met: open). Rise after 9.5: 3.9 -> 0.8 dB; levels per 0.5 qn 9-15 now fall from -34.7 to -44.3 |
| A #3 / C #4 sfp hemiola, bars 301-302 | accepted, different means at 902 | 904: `REATTACK_LEAD_AT` Violins II 0.09, Violas 0.07, Violoncellos 0.09. 902: new `ACCENT_CC_AT` `{902.0: (22, 0.5)}` on Violins II, Violas, Violoncellos (CC11 +22 at the stroke, back to the curve 0.5 qn after the beat) with leads 0.09 / 0.07 / 0.09; basses `REATTACK_LEAD_AT` 902 0.08; `accent_bodies.json` 902 removed and `accent_fits.json` `"902.0": 3.0` on the three sections. 900: `ABUT_LEAD["Double basses"]` at 900.0 (lead 0.08) | pcX 900 / 902 / 904 and the 902 step: Violins II -67 / +64 / -132, -12.9 -> -72 / +50 / -45, +0.9; Violas -39 / +31 / -190, -18.1 -> -39 / -32 / -6, -2.5; Violoncellos -44 / +177 / -122, -15.2 -> -44 / -47 / +10, +0.4; Double basses +115 / +101 / -20 -> -17 / +54 / -21 (its 902 step -2.6 -> -11.2: it now plays a stroke of its own at 900 and the 902 measure reads against that; open). Master 901.5-901.9 -> 902.0-902.4: +4.1 -> +4.3 dB (target 3). Violins II 900 at -72 ms and Flute 1 904 at +146 ms are outside ±50: open |
| A #4 / C #3 Violins I joins behind the other strings | accepted | `LEG_ART_EXTRA_S["Violins I"]["Leg Slur MAX"] = 0.04`; the 36 Leg Slur MAX joins already fitted in `leg_leads.json` lose 0.04 s so their leads do not move; `LEG_VEL_EXTRA_S["Violoncellos"] = (85, 0.06)` (trio tune); `LEG_LEAD_CLAMP_TOTAL = True` (finale technique 20) | Violins I median +49 -> +15 ms (IQR +16..+73 -> -4..+46). Celli 506-552 +39 -> -8 ms (n 30). Probe after: Violins I median +15, robust SD 37, window 69 ms; Violins II -2, 38, 82; Violas +3, 53, 96; Violoncellos +7, 45, 66 |
| A #5 horns' slurred tenuto repeats on "Leg Slur Rep MAX" | rejected as written; other fix | `NOTE_END_AT` Horn 1 `{627.0: 629.58, 630.0: 632.58, 660.0: 662.58}`: the notes before Horn 1's repeats end 21 ms before the re-attack's moved onset instead of 63 ms | Hole against the note before (lowest 10 ms frame within ±0.15 s of the note-on), Horn 1 630 / 633 / 663: 12.6 / 12.7 / 12.9 -> 7.2 / 7.5 / 7.3 dB (limit 8). Horn 2 627 / 642 / 651 / 657 unchanged: 2.6 / 5.3 / 0.4 / 7.8 |
| A #6 Horn 3 + Horn 4 unison is one solo horn | rejected | none | the "2 French Horns" patch needs memory and the project settles at the 45 GB cap |
| B #1 clarinets raised by c10's wind phrase-shape scale | accepted | `score_to_parts.py`: PHRASE_SHAPE key `family_scale_skip_cc1`; `score_config.py` sets it True. `roles.json` Horn 1 `[138, 153, -3]`. Clarinet 1: `pitch_trims.json` `_skip_onsets` for 624-672, positive `note_trims.json` copies removed (also the stale `"494.0"` +2.5) | Bars 47-50: Clarinet 1 -33.3 -> -36.5, Clarinet 2 -35.6 -> -39.0, Horn 1 -34.2 -> -37.1 (Violins I -33.2, Oboe 1 -35.6); margins under Violins I 0.4 / 2.7 / 1.2 -> 3.3 / 5.9 / 3.9 dB, under Oboe 1 -2.3 / 0.0 / -1.5 -> +0.9 / +3.4 / +1.5. Reprise 624-645: beats with Clarinet 1 over Violins II or less than 2 dB under Violins I 7 -> 2 (640, 641: open). Trio solo Clarinet 1 unchanged (-37.99 -> -38.12) |
| B #2 basses' arco G#1 8-10 dB over the other bass notes | accepted | `note_trims.json` Double basses 142 -6, 507 / 531 -7, 651 -3, with `NOTE_TRIM_RAMP_S` 0.1 s on those onsets | Note bodies: 142 -32.9 -> -38.2 (next note -39.8), 507 -41.0 -> -47.9 (next -50.8), 531 -41.1 -> -48.1, 651 -34.0 -> -36.6 (next -38.5). 504-528 basses -47.4 -> -49.6 against celli -38.8; bar 48 basses -33.8 -> -38.8 (Violins I -36.9) |
| B #3 Horn 4's sub. p crescendo level with Violins I, bars 125-127 | accepted | `roles.json` Horn 4 `[372, 381.5, -4]` | Horn 4 372-381 -39.9 -> -43.9 (Violins I -37.7, Flute 1 -40.6); the mf at 382-384 unchanged (-35.3) |
| B #4 coda bar 332, brass at f a beat early | accepted, steeper rows than proposed | `roles.json` rows `[994, 995.5]`: Horn 2 -2, Horn 3 -3, Trumpet 1 -4, Trumpet 2 -5, Trombone 1 -5, Trombone 2 -6, Tuba -7; Horn 1 `[994, 995.45, -3]`. No Bass trombone row (it has no note before 996) | Each track at 995-996 against its own 996-999: Horn 1 -2.7 -> -4.7, Horn 2 -4.1 -> -5.7, Horn 3 -3.1 -> -5.5, Trumpet 1 -3.7 -> -6.8, Trumpet 2 -0.2 -> -4.6, Trombone 1 -2.2 -> -6.0, Trombone 2 +0.4 -> -3.8, Tuba +1.4 -> -4.0 (target -3 each: met). Brass sum under the string sum at 995: 2.3 -> 5.0 dB (target 5). Master per qn 993-997 -23.5 / -22.2 / -21.6 / -18.5, rising |
| B #5 violas' pizz. beat 2, Oboe 2's F5 | accepted | `note_trims.json` Violas +3.0 -> +5.5 on 14 beat-2 pizzicato onsets (757-799); Oboe 2 `"900.0": -2`, `"990.0": 3` with 0.1 s ramps; `LEVEL_SHAPES["Oboe 2"]` -5.5 dB over 902.95-904.2, -2 to 905.9 (B's -3 note trim left +2.4..+4.6 in the simulation) | Oboe 2 - Oboe 1 at 900-902.9 / 903-905.9: +2.1 / +4.1 -> +0.4 / +0.4. Oboe 2 987 / 990 / 993: -43.8 / -39.5 / -35.7 -> -43.8 / -39.0 / -35.7. Violas' beat 2 - beat 3 (0.2 s peaks) median +1.1 -> +3.3; first 0.1 s of beat 2 -52.3 -> -49.8 (beat 3 -48.8) |
| C #2 soft first notes at the section joints late | accepted; four entries still late | `entry_leads.json` extras (total lead): Violins II 672 / 708 0.18 (300 ms), 738 0.12 (240), 1044 0.10 (220), 360 0.08 (200); Oboe 1 672 0.08 (135); Violas 1020 0.18 (300); Flute 1 1044 0.20 (255); Violas div 1044 0.08 (200). Hand-set `early_fills.json` entries: Violins II 672 / 708 +4, 738 +2; Oboe 1 672 +2; Violas 1020 +4; Flute 1 1044 +4; Violas div 1044 +3; Violin I solo 1044 +3; Double basses 504 +4; Horn 1 1077 +5 (starting 0.09 s after the note-on). `roles.json` Violins II row `[336, 357]` now ends at 359.2 (see below) | pcX: Violins II 672 +281 -> +167, 708 +272 -> +138, 738 +159 -> +43, 1044 +137 -> +57, 360 +129 -> +98; Oboe 1 672 +220 -> +194; Violas 1020 +261 -> +109; Flute 1 1044 +324 -> +67; Violas div 1044 +167 -> +81; Violin I solo 1044 +228 -> +139; Double basses 504 +144 -> +112, 1071 +144 (no change made); Horn 1 1077 +3 -> +21. Violoncellos 504 reads +263 -> +339, but the stem is identical to c10's through qn 505.0: the reading changed because the next note's onset moved |
| C #5 pizzicato three-bar groups have no weight on the heads | accepted | `note_trims.json`: Violoncellos 264 +1.5 -> +2.5, 273 / 282 +1.5 -> +2.3, 270 / 279 / 288 -6.0 -> -5.5; Double basses (new) 264 +1.5, 273 / 282 +0.3, 270 / 279 / 288 +1.0 | Head bar against the other two bars (0.2 s peaks): celli +1.1 / +1.3 / +1.3 -> +1.9 / +1.9 / +1.8; basses +0.9 / +2.1 / +2.2 -> +1.9 / +1.9 / +2.0. The trims on these pizzicato notes are realised as requested (finale technique 22 checked) |
| C #6 final rit. overshoots the printed 140 | accepted | `score_to_parts.py`: `RAMP_LAST_STEP_HOLD_QN`; `score_config.py` 6.0 | Tempo over 1122.0-1124.75: c10 fell 139.4 -> 127.2; c11 holds 140.0; both 50.0 at 1125. Master per bar 1104-1128 within 0.7 dB of c10 |

Rejected or deferred, with reasons:

- A #5 as written ("Leg Slur Rep MAX", +0.25 GB): the patch file shows the row's re-tongue groups start on round robin
  only (`loop/MANUAL-GAPS.md` #2: read, not used). Measured against the note before, Horn 2's repeats on Sus MAX already
  dip 2.6-7.8 dB; only Horn 1's had holes over the 8 dB limit, and closing the gap before them fixed that.
- A #6: no memory room (REAPER settles at 45.0 GB, the cap).
- C #4's horn sub-item (horns' loud entry lead 0.05 -> 0.02 over 300-340 and 900-1017): the brass tenuto quarters on
  Sus MAX are on critic A's do-not-touch list, and -14..-41 ms is inside ±50 ms.
- The Sus Marc LITE row for the 902 strokes of Violins II, violas and celli (Violins I, on that row, was on time): the
  row is loaded on Violins I only and there is no memory room for three more. The CC11 lift at the stroke gave the time.
- B #4 Bass trombone row: it has no note before 996.
- Solo violin in `LEG_CAP_FROM_MOVED`: not flagged, and on critic A's do-not-touch list.
- `auto_fills.py`'s retimes of the celli fills at 576 / 600 / 768: the new ramp lay inside the legato transition; the
  c10 values are kept (`early_fills.json` `_auto` notes).
- Short of target and open: Horn 1 G#3 at 6 (+83 ms); Violins II 672 / 708 (+167 / +138), Oboe 1 672 (+194), Violin I
  solo 1044 (+139), Violas 1020 (+109), Double basses 504 / 1071 (+112 / +144); Flute 1 904 (+146); Violins II 900
  (-72); the basses' 902 stroke; Flute 2's joins (+46 ms median); reprise beats 640 / 641.

Other changes made while implementing the findings:

- Violins II at 360 (sub. p entry): with the lead at 200 ms the rest before it shrank from 0.514 s to 0.434 s, under the
  0.5 s tail-hold minimum, so the release of the role row `[336, 357, -3]` lifted the previous staccato note's hall
  tail by 3 dB. The row now ends at 359.2, inside the entry's lead. Violins II per 0.5 qn over 357-360 falls evenly.
- Violins I theme heads at 53 / 77: c10's +5.5 dB trims on the first eighth ended at the next note-on, which the new
  leads put before the eighth's own score onset (realised +3.5 dB). New `LEG_JOIN_TRIM_HOLD_TO_AT` (plateau to 0.025 s
  before the next score onset). First eighth against the next quarter: 53 -4.2 -> -1.3 dB, 77 -4.1 -> -0.8 dB.
- `rebow_fills.json`: keys renamed where the new leads moved the automatic re-bow points.
- `auto_fills.py 10` run on the c10 data with `--write --exclude "Clarinet 1:634" --exclude "Clarinet 1:662" --exclude
  "Horn 1:1077"` (26 entries), before the hand fills.
- Stale-state recheck on the c10 audio (c10 was the first render after a full rebuild of all legato tracks): the
  accent fits hold; the c05 legato-passage roles hold; Clarinet 1's `"494.0"` +2.5 trim was fitted on stale audio and is
  removed.
- CC11 against attack time, measured on the c10 stems: Sus MAX strokes speak 60-110 ms after the note-on at CC11 75 or
  more and 210-380 ms at CC11 60-74. A volume swell does not change the time.

Note diff against c10 (`records/note_diff_c10_c11.txt`): Flute 1 moved 1; Flute 2 moved 43; Oboe 1 moved 1; Horn 1 moved
2, duration 6; Harp duration 4; Violins I moved 61, duration 101; Violins II 18 / 29; Violas 18 / 28; Violoncellos 66 /
77; Double basses 2 / 3; Violas div moved 1. No velocity, articulation or note-count changes.

## 2. ONE_TIME (`loop/ONE_TIME_c11.done.md`, finale SHARED-TECHNIQUES 13-17)

| item | result |
|---|---|
| 1 (technique 13) strings' sf of the sfp at bar 301 | Measured first on c10: sf front (0.1 s peak against 900.9-901.9) Violins I +9.3, Violins II +11.0, Violas +12.5, Violoncellos +8.8 dB; Double basses had no stroke at 900 (pcX +115 ms, note-on at the p point before the spike). Applied where short: Violins II +4 dB bump (`LEVEL_SHAPES`, 899.65-900.1), the basses' stroke (`ABUT_LEAD` at 900.0, lead 0.08 s: pcX +115 -> -17 ms), Flute 1 +3 dB bump (899.69-900.5). Result: Violins II +11.0 -> +12.5, Flute 1 +2.3 -> +3.9 dB. Violas and celli pass without a bump. The +5 dB celli / basses bump of the item was not needed |
| 2 (technique 14) Flute 1 / Flute 2 unison joins | Flute 2's joins measured +40 ms median against Flute 1's +2 ms at the same 0.03 s lead: `LEG_LEAD_S["Flute 2"] = 0.07`. Result: median +53 -> +46 ms, over +60 22 -> 16, over +100 6 -> 3 (previous pitch excluded). 40 ms more lead moved the median 7 ms: open |
| 3 (technique 15) delivery ride | `ride_ramps11.py` found three ramps running against a printed hairpin. Rows changed: 300 (the 2 dB fall is now in the 0.4 qn before the subito f), 587 (the fall is spread over the crescendo 576-588), 659 (the return is spread over the diminuendo 666-672). Delivered step 300 -> 303: +1.7 -> +2.8 dB (master +2.9). Steps over 576-588: +2.1, +1.9, +2.1, -0.6 -> +1.1, +2.0, +1.8, +0.4. Falls 666 -> 669 -> 672: 4.3, -0.3 -> 3.7, 0.2 dB. `--fit-flat` trial rows (+1.5 dB) not adopted: at bar 121 the trial lowered the delivered f -> sub. p step from 8.8 to 7.1 dB against the master's 10.2; at bar 277 the ride is already flat within 0.4 dB |
| 4 (technique 16) texts on full-bar rests | Listener added to `build/mockup.ly`; the event list gains 15 text lines: timpani stick and tuning changes, Violins II "via sord." (bar 185), Clarinet "muta in B flat" (bar 376), harp "étouffez". Used: the harp damps (`HARP_RING_S = 2.0`, four harp note ends): harp level 0.3-0.6 s after 258 / 575.5 / 717 -47.5 / silent / -73.6 -> silent in all three. Timpani stick changes: found, pending (`loop/MANUAL-GAPS.md` #6) |
| 5 (technique 17) negative result | no action; no REP_SPLIT gaps added |

## 3. Coordinator notes during the cycle

Movement II c48 (two checks):

1. fp spike read as a printed f by `vol_points()`: the scherzo's `vol_points()` reads `dyn_curve`, and the p point at
   900.0 is a one-grid-point bump in the per-dynamic trim; no `fp_falls` port is needed (`volenv11.py`).
2. Tracks that move without a data change after `--midi-only` builds: every track was fully rebuilt before this render.
   `unchanged11.py 10 ... 11 ...` on all 31 tracks (`records/unchanged_tracks_c10_c11.txt`): median level difference
   0.00 dB and median lag 0 ms on every track (Bass trombone, same data, 23 notes: 0.00 dB / 0 ms; Trombone 1 max
   0.27 dB; Flute 2's p10 lag of -21 ms is its lead change). No track moved as a whole. Single notes differ: see
   "Render".

Finale techniques 18-23:

- 20 (negative per-onset legato lead clamped before it is added): adopted as `LEG_LEAD_CLAMP_TOTAL = True`.
- 22 (note trims ramp in over 0.6 s): the pizzicato head-bar trims of C #5 are realised as requested (pizzicato trims
  are steps); bowed and blown notes got `NOTE_TRIM_RAMP_S` 0.1 s, and Oboe 2's F5 a level shape.
- 23 (ride row after a subito): bar 277 checked, no row added (item 3 above).
- 19 in part (Flute 1's sf bump at 900). 18 and 21 not done.

Movement I c52 state guard: `tools/state_guard.py` copied from Movement I's tools (unchanged apart from its header) and run
three times. Before the build, on the project saved after the c10 render: 5 stale of 31 tracks (Bassoon 2 18 envelope attacks,
Contrabassoon 24, Horn 4 16, Violins I 58, Violas 52). After a full build of all tracks and a save: 0 stale, 0 missing.
On the project saved after the c11 render: 5 stale again (Bassoon 2 18, Horn 4 16, Violins I 58, Violas 52,
Violoncellos 52). **The c12 actor must start with a full build of all tracks.** `build_reaper.py` and `render_cycle.py`
do not enforce the guard yet (item 8 of `loop/ONE_TIME_c12.md`).

`loop/ONE_TIME_c12.md` items touched this cycle: 3 done; 7 done; 2, 5, 6, 8 in part (as above). Items 16 and 17 match
this cycle's findings on round robins and on horn notes that differ between two renders of the same data.

## Research items

| item | status |
|---|---|
| EW template mix (c06), returns and sends (c07-c09), c08 EQ set, brass track width (c10) | adopted, unchanged. Hall: G.P. 20.4 dB at +0.3 s, RT60 1.34 s (same as c10) |
| finale SHARED-TECHNIQUES 13-17 | 13 adopted where the sf was short (Violins II +11.0 -> +12.5, Flute 1 +2.3 -> +3.9 dB, basses' stroke +115 -> -17 ms); 14 adopted (Flute 2 +53 -> +46 ms); 15 adopted for three rows, `--fit-flat` rejected (step 8.8 -> 7.1 dB against 10.2); 16 adopted; 17 no action |
| finale SHARED-TECHNIQUES 18-23 | 20 adopted; 22, 23 checked; 19 in part; 18, 21 pending (`loop/ONE_TIME_c12.md`) |
| wind phrase-shape scale x1.4 (c10) | kept on CC11 tracks; rejected on CC1-dynamics tracks (clarinets +2.6..+4.5 dB) |
| Movement II c48: `fp_falls`, unchanged-track comparison | first not needed (checked); second adopted as a check each cycle |
| Movement I c52 state guard | adopted as a check (5 stale -> 0 -> 5); enforcement in the tools pending |
| Movement I c52 items 9-15, Movement II items 16-20 of `ONE_TIME_c12.md` | pending |
| batch 6 #3 shared curves, CC11 -> CC1 pass 2, separate legato tracks | pending (memory / pass 2) |

## MANUAL-GAPS

#2 (solo horn "Leg Slur Rep MAX"): read, not used. #6 (timpani stick changes on full-bar rests): found, pending. Both
recorded in `loop/MANUAL-GAPS.md`.

## Tool changes (generic, off by default)

- `tools/score_to_parts.py`: `LEG_CAP_FROM_MOVED`, `LEG_LEAD_CLAMP_TOTAL`, `ACCENT_CC_AT`, `LEG_JOIN_TRIM_HOLD_TO_AT`,
  PHRASE_SHAPE `family_scale_skip_cc1`, `RETONGUE_LEAD_AT`, `RAMP_LAST_STEP_HOLD_QN`.
- `build/mockup.ly`: multi-measure text listener.
- `tools/state_guard.py`: new (from Movement I).
- `build_reaper.py`, `stem_fix.py`, `render_cycle.py`, `deliver_master.py`, `build/mix.json`: unchanged.

## Render

Steps: waited 16:34-16:44 behind Movement II; lock 16:44:46; start, open (35 tracks; Opus log: 0 "Interrupted system
call"); state guard on the saved project (5 stale); full build of all 31 tracks plus returns (65 s); save; guard (0
stale); restart; memory settled at 45.0 GB by 17:00:25 (558 s); audio_init (48000 / 512); `render_cycle.py 11` refused
at the memory gate, rerun with `--force-memory` 17:02-17:10; checks; quit 17:22:06; unlock 17:23:14.

Memory: 45 GB settled (26 GB compressed) before the render, 46 GB (29 GB compressed) after
(`cycles/c11/top_after_render.txt`).

Stem repair after unlocking (no second render). `stemdiff11.py` and `unchanged11.py` against c10 showed horn notes on
data identical to c10's with slow or missing attacks in the c11 render: Horn 4's note-on at 251.78 (a 26 dB hole for
0.5 s), Horn 1's at 155.6 and 164.6 (2.5-12 dB under), Horn 2's at 158.78 and 626.81 (2-5.7 dB under). All are
re-tongued notes 7-14 ms after the end of the note before. `splice11.py --apply` replaced these spans with the c10
stem (30 ms crossfades at points where the two renders correlate): Horn 4 251.70-256.25; Horn 1 155.55-160.90 and
164.40-167.20; Horn 2 158.70-161.60 and 626.70-631.00; R Brass 251.70-256.60, 155.55-162.00, 164.40-167.60; and
rebuilt the master as the sum of the stems. Span levels c11 -> spliced (c10): Horn 4 -46.6 -> -43.8 (-43.8); Horn 1
-39.4 -> -37.4 (-37.5) and -46.4 -> -42.3 (-42.3); Horn 2 -37.3 -> -35.8 and -43.9 -> -43.4. 214323 of 13747323
samples changed; master sample peak unchanged (0.8251). Checks: master minus the sum of the 35 stems -137.9 dB;
`stemdiff11.py` at 2 dB on all brass shows the holes gone; `check11.py 11` changed in one line (Horn 2's 627 dip 5.2 ->
2.6, c10's value); `render_cycle.py 11 --measure-only` remade the metrics and the mp3. The first render's files are in
`cycles/c11/render_first/` (master, Horn 1, Horn 2, Horn 4, R Brass); log `cycles/c11/splice.log`. The spliced stems
and the master are 32-bit float; the other stems are 24-bit.

Two renders of the same data also differ on single staccato woodwind notes by 1-6 dB (round robins; 317-357 and
912-958), and the brass return differs by 2-3 dB on single sustained horn notes whose dry stems agree within 0.6 dB
(441-442.5, 902.5-904.5, 1028.5-1030.5). Neither was changed.

Master -21.0 LUFS, LRA 23.0 LU, true peak -1.7 dBFS, sample peak 0.825 (c10 -21.0 / 23.1 / -1.2, 0.874). Delivered
-19.8 LUFS, LRA 14.8 LU, TP -1.4 dBTP, limiter about 2.9 dB, span 19.6 dB (c10 -19.8 / 14.8 / -1.6 / 3.3 / 19.6); ride
+10.0 / -3.2 dB. Band shares 2-6 kHz -9.55, 6-20 kHz -28.77 dB (unchanged). Attack probe: no late or hole, every line
ok. Hall: G.P. drop at +0.3 / +0.6 / +1.0 s 20.4 / 31.3 / 46.7 dB, RT60 1.34 s; final chord 20.2 / 31.1 / 40.5 dB, RT60
1.32 s; tutti 20 dB fall 0.30-0.31 s; soft ends 0.14-0.29 s; returns -11.63 dB against dry. All inside Dan's limits and
equal to c10.

Disk: deleted cycles/c10's stems and return stems (kept its 00_Master.wav and mp3) and the four files in `Backups/`;
no deletion was refused. `cycles/c08/render` still holds its stems (2.8 GB; refused in c09, not part of this cycle's
instruction). 69 GB free after.

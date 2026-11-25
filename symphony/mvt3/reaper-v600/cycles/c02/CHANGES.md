# Cycle 2: changes (critics A, B, C on the c01 render)

Render: `cycles/c02/mvt3-mockup-c02.mp3` (Horn 3/4 stem fix applied; originals in `render_first/`). Before-state in `before/`.
Actor checks: `actor_scripts/m02.py 1 2` (broadband 10 ms repeat dips, the master's 35-180 Hz dips, sfp frames, arrivals, span levels).

## Accepted

### Tools (`tools/score_to_parts.py`, generic, defaults off)
- **`STR_REP_NEW_BOW`**: Movement I c44's rule, ported from `symphony/mvt1/reaper-v621/tools/score_to_parts.py` (I checked the hunks against Movement I's current code and they are identical, with the same settings as its c44 CHANGES item 3). A same-pitch string repeat that the legato merge would have joined into the note before is now a new bow stroke when it is not inside the same slur. Loud repeats become a Sus MAX stroke after a gap of min(0.06 s, 25% of the note). A slurred tenuto repeat becomes a "portato" stroke after min(0.05 s, 25%), with a 6 / 8 CC fall. Soft repeats become re-bow points.
- Two additions of my own:
  - `STR_REP_NEW_BOW["skip"]` {track: [(a, b)]}: these spans keep the merge.
  - A `DOWNBOW_STROKE_AT` stroke before a same-pitch slurred repeat is now a valid predecessor for the rule. Without this, Violas 893 after the 892 stroke would have been an unled Leg Slur MAX first note.
- **`SFP_SPIKE_S`** (hold_s, fall_s) and **`SFP_VEL`**: an sfp's attack level is held and released in seconds on the real tempo map, and the notes at the mark get a minimum velocity. Legato targets keep their own velocity.
- **IR envelope (`ir_setup`)**: not ported. Movement I had not kept or rendered a setting when I built, and critic C measured the decay as on target. See "Deferred to c03".

### Config (`build/score_config.py`, "mvt3 c02" block)
- **A #1 (S1):**
  - `STR_REP_NEW_BOW` uses Movement I's values. `skip` keeps the merge for Vc / Cb 892.5-940.5 ("change bow at will").
  - The slurred portato quarters (Violas 893-911, Violins II 921-931) are portato strokes. The critic had asked to keep them merged. I changed them because the violas' 892 head is a stroke, so a merge after it would have left unled Leg Slur notes, and because Dan asked for repeats to be heard.
  - The slur heads after those strokes go on `DOWNBOW_STROKE_AT`: Violas 892, 896, 900, 904, 906, 908, 912; Violins II 924, 928, 932; Violins I 431. Every unled legato note the change would have created is gone (I scanned parts.json against c01: no new ones, three fewer).
  - Result (parts.json): 51 strokes or portato strokes, 4 soft re-bow points and 13 Sus-repeat gaps (`sus_min_s`). Vc 602-608 is now four notes, not one note of 6.62 qn.
- **A #1, basses:** `STR_REP_DETACH` adds spans 64-104, 148-172 and 596-672 with `max_qn` 2.0 and `same_pitch_only`. Dips 320 -> 331.
- **A #1, bassoons:** `WIND_REP_RETONGUE_BY` "Bassoon" and "Contrabassoon" take the horns' gap 0.10 s, frac 0.3 and fall 12 CC over 0.15 s.
- **A #2:** `SHORT_SUS_LEAD_S` 0.1 -> 0.06, now on Violins I, Violins II and Violas (it was Violins II only).
- **A #3:** Horns 3/4 at 40-104 move from StacSs to "Marc Shrt RRx4". Horn 1 gets Marc Shrt for its staccatos at 40-104, 552-664, 816-828 and 1056-1076 (38 notes).
- **A #4:** `PORT_TARGETS` Violins I / II {941.0: 100}. The bar 236 portamento now plays on Leg Port MAX.
- **A #5:** `DOWNBOW_STROKE_AT` Violas 892.
- **C #3:** `SFP_SPIKE_S` (0.12, 0.30), `SFP_VEL` 96.
- **C #1b:** `ARRIVAL_WEIGHT_AT` 1108 (-1, +2, 0.5) and 1048 (-1, +1.5, 0.5).
- **C #1c:** `LEVEL_SHAPES` against the held-fff sag at 1108.5-1113.2: Horn 1 +4, Bass trombone +3.5, Trumpet 2 +3 dB.
- **C #2 / C #4 fallback:** `RIDE_TRIMS` (delivery only), refit on this render by rerunning `deliver_master.py`:
  - soft passages: 168-200 +1.3, 200-264 +2.55, 376-392 +1.3, 452-504 +2.1, 680-744 +2.55 dB (the critic's values x 0.85);
  - 1088-1104 +2.5 and 584-600 -1.5 dB.
  - Three variants were simulated on the c02 master; this one gives LRA 14.7, and 273-276 is 1.4 dB over 147-150 in the mp3.

### Data (`build/*.json`)
- **mix.json, B #1 `dyn_trim_db`:**
  - Violins I: f 0, ff -1.0, fff -1.5.
  - Violins II: f -1, ff -1.0, fff -1.5.
  - Violas: f 0, ff 0.
  - Horns 1-4: ff and fff each +1.5.
- **mix.json, B #4 `soft_trim_db`:** Clarinet 1 mf 2.5, mp 3.0; Clarinet 2 mf 3.0; Oboes mf 5.5; Violas mf 3.0.
- **roles.json:**
  - B #2 (255-262): Tpt 1/2 -3; Vln I -2; Vln II +2; Vla +2; Hn 3/4 +3.
  - B #3 (247-254): Tbn 1/2 984.5-1016 +4; Tpt 1/2 984-1000 +3.
  - B #5: the Tuba row is split into 1032-1088 +3 and 1088-1116 +1.
  - B #6: Vln I / II 892-900 -2.
  - C #1a: final chord 1107.9-1113.5, Vln I +5, Vln II +5, Vla +4, Vc +3.
  - Stem-fix refit: Horn 3 / Horn 4 at 40-104 go from +3 / +5 to -2.6 / -1.9. Marc Shrt came out 7-8 dB over the c01 StacSs level; they are now set to the c01 level +1.5 dB.
- **pitch_trims.json:** Trombone 2 D4 (62, on every articulation) -4.5. The only notes affected are qn 584, 588 and 592.
- **note_trims.json:** Clarinet 1 qn 544 and 548 +6.

## Rejected or deferred
- **A #4, `SUL_SPANS`:** deferred. On Movement I the string change did not happen under slurs (Results c38), so the gain is uncertain.
- **A #6, soft brass legato velocity:** deferred. It is the lowest-priority item and is still open from c01.
- **A, keep the portato quarters merged:** not followed, for the reasons given under Config (S1, and to avoid unled legato notes).
- **C #5, counter-shapes for Oboe 1 376-384 and Violins II 376-391:** deferred. They need a fit on 0.2 s frames from a render. Only the Clarinet 1 note trims were done.
- **C #6 (hall):** no change. Per the coordinator, fx_volume stays 0.095 and low_cut_hz 160, and sends were not raised.
- **Deferred to c03 (coordinator, 2026-11-07, received after the REAPER build had started):** Movement I c44's three measured changes.
  - `reverb.ir_setup` {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}, with the irSetup block copied into `tools/build_reaper.py`.
  - `sus_release_cap_ms` for the string sections (150 ms on Sus MAX / Sus Marc LITE, pp-ff) and the horns (237 ms on Sus MAX / LegRep).
  - Both change the Opus state, so c03 needs a full rebuild of every track. Item 3 (`STR_REP_NEW_BOW` from Movement I) is already in this cycle.
- **WARNINGs:** the 64 WARNING lines (fp / sfp "curve 48-49" at qn 592 and 832, and Clarinet 1 pp at 481 / 483) are identical to c01's. They were not fixed this cycle.

## Measured (c01 -> c02, same method on both renders)
- **Repeat dips, broadband 10 ms on the stem (dB):**
  - Double basses 604 / 606 / 608 / 658: 4.6 / 9.8 / 4.6 / 4.6 -> 7.1 / 9.2 / 7.2 / 7.1.
  - Bassoon 1: 4.0-4.1 -> 6.0-6.6.
  - Contrabassoon: 7.6-7.8 -> 9.3-9.4.
  - Violoncellos 70 / 98 / 156 / 604 / 606 / 608 / 630 / 658: 1.5 / 0.8 / 2.2 / 1.5 / 3.7 / 2.4 / 2.3 / 1.0 -> 2.4 / 5.2 / 2.1 / 2.1 / 2.5 / 13.5 / 1.6 / 6.1. Mixed: the cello strokes at 604, 606 and 630 still measure about 2 dB (release and hall fill a 0.06 s gap at G2). This is the open point for c03; Movement I's 150 ms string release cap addresses it.
  - Violas 38 (accented f): 4.0 -> 9.5. Violins I 444: 4.8 -> 9.7.
  - The louré at 796 / 988 measures 6.2-7.9 on the violins (it was 9.2-9.8 with the CC notch on this broadband measure; critic A's harmonic-band measure read -0.4 to 2.6 in c01). Not comparable across methods; re-measure on harmonic bands in c03.
- **Master 35-180 Hz dips** at 604 / 606 / 608 / 630 / 658: 13.8 / 9.5 / 9.5 / 4.9 / 3.3 -> 6.1 / 8.7 / 12.8 / 8.6 / 4.9.
- **Violins II minus Violins I timing** (pcX, unison short notes): median -39 ms (p10 -123, p90 +27) -> +0 ms (p10 -44, p90 +85).
- **sfp at qn 592**, master quarter-qn frames:
  - The sf is now -14.6 against -13.4..-14.0 before the gap (c01: no sf, -19.3 at that frame).
  - The fall reaches -22.3 by 593, 7.7 dB under the sf (target 10). Then it rises to -12.3 at 596.
- **Arrivals:**
  - Bar 278's first quarter is -9.5, against 277's accents at -11.5 (+2.0; c01 +0.2) and 223's head at -10.3.
  - 1048 is -11.3 against 1047 at -12.5 (+1.2; c01 +0.3).
  - Held-fff sag, last minus first quarter: Horn 1 -7.6 -> -5.5, Bass trombone -5.2 -> -3.6, Trumpet 2 -3.7 -> -2.4.
- **Balance, re master:**
  - 255-258: Horn 3 -13.7 -> -9.3, Violas -16.2 -> -10.8, Vln II -13.9 -> -13.3, against Tpt 1 -5.7 -> -8.5 and Vln I -9.0 -> -13.2.
  - 247-250: Trombone 1 -17.8 -> -14.5, Trumpet 1 -15.5 -> -12.9.
  - Recap 151-166: Vln I -8.5 -> -10.8, Horn 1 -11.4 -> -9.5, Violas -16.4 -> -13.3.
  - Tuba at 278-279: -9.4 -> -12.2.
- **Retransition:** Trombone 2 at 584-592 is -20.0 -> -24.4 dB. Bar 147 is -13.3, with Trombone 2 level with the cellos and Trumpet 2.
- **Levels:**
  - Horn 1 Marc Shrt spans: 40-104 -38.7 -> -38.2; 552-664 -32.9 -> -31.4.
  - Violas 892-912 (portato strokes): -37.2 -> -34.3.
  - Oboe 1 264-328: -48.8 -> -46.7. Clarinet 1 536-552: -45.7 -> -43.5.
- **Master:** -15.9 LUFS, LRA 22.1 LU, float-sum peak 1.655 (+4.4 dBTP; the 24-bit file is replaced by the float sum, as in c00-c01).
- **Delivered:** -19.8 LUFS, LRA 14.7 LU, TP -1.5 dBTP, limiter 2.3 dB, p10-to-max span 18.9 dB, ride max +12.6 dB. The pre-limiter peaks are at 223 (+0.83) and 278. Without the refit the first delivery read LRA 14.2, limiter 2.4 and span 18.6.
- **Attack probe:** 2 flags.
  - Violoncellos qn 24 +0.36 s. Its notes are unchanged from c01, which read +0.15 and c00 +0.42: render-to-render variation, as before.
  - Violins I joins robust SD 75 ms against a 75 ms limit (c01 74 ms, judged ok). Its window median is 82 ms (c01 84).
  - c01's Oboe 1 qn 36 flag is gone.
- **Pre-roll:** still not silent on the strings, the same as c00-c01.

## REAPER
- Lock held 12:52:00-13:27:32 (36 min). Fresh start; `--midi-only` on all 31 tracks, with Horn 1, Horn 3, Horn 4, Violins I and Violins II fully rebuilt (their Opus state changed); restart; settle; audio-device reopen (48000 Hz, 512, no input); render with `--force-memory`; `--mix-only` Horn 3 / Horn 4 for the stem fix; save, quit, unlock.
- Before locking I followed the coordinator's longest-waiter rule. I stopped my first wait and locked again after Movement I had taken REAPER.
- REAPER memory: 44 GB settled with 32 GB compressed before the render; 44 GB after, with 27 GB compressed (41 GB at quit). Other large processes: CrashRestartHelper 6 GB, Steam 6.8 GB. Disk: 68 GB free.

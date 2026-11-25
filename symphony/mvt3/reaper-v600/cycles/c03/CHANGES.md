# Cycle 3: changes (critics A, B, C on the c02 render)

Render: `cycles/c03/mvt3-mockup-c03.mp3`. Before-state in `before/`. Actor checks: `actor_scripts/m03.py tails|dips|bal|pcx 2 3`
(c02 on `before/parts.json`, c03 on `build/parts.json`). Every track was fully rebuilt (the IR envelope is in every Opus state).

## Accepted

### Required (Movement I c44's dry-hall changes, BRIEF end section; coordinator)
- **IR envelope:** `tools/build_reaper.py` apply_mix: the irSetup block copied from `mockup-kit/pipeline/build_reaper.py`.
  `build/mix.json` reverb `ir_setup` {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5} (checked in the generated
  state: `irSetup` envelopeMode 2, endPos 0.5, decayLength 0.5; lowCutFreq 160). fx_volume 0.095, low_cut_hz 160 and
  every send unchanged.
- **Release caps** (`build_reaper.cap_release` was already in tools/; mix.json per track):
  - Violins I, Violins II, Violas, Violoncellos, Double basses: `{"ms": 150, "dyn": ["pp","p","mf","f","ff"], "rows": ["Sus MAX","Sus Marc LITE"]}`
    (replaces the 250 ms mf-ff cap on Violas / Violoncellos / Double basses). Build log: groups shipped 323-931 ms.
  - Horns 1-4: `{"ms": 237, "dyn": ["pp","mf","f"], "rows": ["Sus MAX","LegRep RRx4"]}` (1FH pp 372/562, mf 394, f 316 ms).
- **Full rebuild** of all 31 tracks and the tempo map (`build_reaper.py build/parts.json jobs`, no flags).

### No WARNING (64 lines through c02 -> 0)
`tools/score_to_parts.py` (generic, defaults off; on in `build/score_config.py`):
- fp / sfp marks are checked where the attack has fallen to the printed p (`FP_CHECK_AT`, filled in base_points). The
  48 fp/sfp lines at qn 592 and 832 were the check reading the spike's 0.02 qn ramp (46 + 5% of the spike); the curves
  were already right.
- `HP_DIM_RESTATE`: a decrescendo whose printed target equals the current level still falls 6 CC (c06 rule), but when
  the track has a note onset at the mark the mark restates its level there. Fixes Vln I/II mf > mf at 296 and 776, Vla
  mp > mp at 776, Vla/Vc/Cb sf > p at 552 (the new notes started 6 CC under their printed dynamic).
- `HP_SWELL_AT_MARK`: a crescendo starting on a printed mark whose target equals it (ff < > ff at 1016-1019 on Vln II,
  Vla, Vc, Hn 3/4; Cl1 pp < > pp at 481-483) swells one untargeted step above the mark (short-hairpin cap 6 CC, ceiling
  120) instead of starting 12 CC under the printed mark ("niente <").
- Result: `score_to_parts.py` prints 0 WARNING lines (c02: 64).

### Critic findings accepted
Tools (`tools/score_to_parts.py`, generic, defaults off) and config (`build/score_config.py`, "mvt3 c03" block):
- **C #1a `ACC_HEAD_JOIN`:** an accented slur head on the Sus row is a SLUR_START_SUS head when the slur's next note
  abuts it at another pitch on a legato row: the head overlaps it and the second note takes the SOST join (0.12 s lead,
  v100). parts.json `acc_head_joins`.
- **C #1b `SHORT_SUS_DETACH_JOIN_LEG`:** a loud detached short_sus eighth whose next note is a legato-row note of the
  same slur joins it (SHORT_SUS_JOIN: legato target, lead capped at 0.75 of the eighth, v124) instead of ending 0.01 qn
  before it.
- **C #2:** `ENTRY_LEAD_ART_S["string"]["Leg Slur MAX"]` 0.06 s; `TREM_ENTRY_LEAD_S` 0.04 -> 0.08.
- **C #3:** `ABUT_LEAD["Double basses"]` {lead 0.07 s, cap_frac 0.45, rebow_ok, skip_next_same, new key `min_qn` 0.75}.
- **C #6a `RAMP_END_CLAMP`:** a slowing ramp that ends on a printed tempo at or under its last step does not go under it
  (880-888 ended at 106.4 qpm; now 112 to the arrival).
- **A #1:** `STR_REP_NEW_BOW["portato"]` gap 0.05 -> 0.08 s, fall 6/8 -> 10/12 CC over 0.06 s; new key `"tenuto"`
  {gap 0.07 s, frac 0.25, fall 8 CC / 0.05 s} (tools: an unslurred same-pitch tenuto repeat is a new bow at any dynamic
  and length); `STR_REP_DETACH` Double basses spans 322-328 and 976-984; `WIND_REP_RETONGUE_BY["Trombone 1"]` horn values.
- **A #2:** stopped horn on "Stop Sus" (`ART_SPANS`): Horn 1 191.9-199.9 and 667.9-675.9, Horn 2 667.9-675.9,
  Horns 3/4 547.9-551.9. Level refit after the render (stem fix, below).
- **A #3:** Trumpet 1 dolce solo: `LEG_VEL_SPANS` (200.5, 264, v96) and `build/leg_leads.json` -0.035 s on its 37
  legato targets (lead 0.10 -> 0.065 s).
- **A #6:** `PORT_TARGETS` velocity 100 -> 80 at 941 (glide not measured this cycle).
- **B #1:** `TIMP_ROLL_TRIM_DB` refit for hard sticks [(22, 7.7), (34, 9.2), (46, 10.7), (58, 9.8), (72, 9.4), (88, 7.3), (114, 5.9), (124, 2.6)].
- **B #2:** new `TIMP_SETTLE_SKIP` (tools; Finale [1108.0]): the final fff roll keeps its level.
- **B #3:** roles.json Trumpet 1 888-892 +2 -> +5; Tuba 888-896 +3 -> +1.5.
- **B #4:** mix.json dyn_trim_db fff Clarinet 1 -0.8 -> -4.0, Clarinet 2 -1.9 -> -6.0, Oboes 2.0 -> 4.0; roles.json Clarinet 1 [900, 920, -2.5].
- **B #5:** `PERC_MAP["Bass drum"]["bassdrum"]["vel"]` 114 (printed ff).
- **B #6:** roles.json Clarinet 2 [184, 200, +6].
- **Pipeline:** `space_rebows.py --write` had never been run in this folder (rebow_moves.json was `{}`): 7 automatic
  re-bow points moved (Cb 172.9, 568.0, 576.0; Vla 174.1; Vln I 189.6; Vc 191.6), then score_to_parts.py again.

### Stem fix (after the render, level only; originals in `render_first/`)
- roles.json Horn 1 [192, 200, +2.5], Horn 2 [668, 676, +8.5], Horn 3 [548, 552, +10.5], Horn 4 [548, 552, +7.5]:
  the stopped notes came out 2.2-12.8 dB (K-weighted, re master) under the open c02 notes; now 2.3-3.3 dB under.
  `tools/stem_fix.py 3 cycles/c03/rendered_build build --apply` (Horns 1-4), then `render_cycle.py 3 --measure-only`.
- **Not in REAPER yet:** I had already unlocked when I measured this, so the project's Horn 1-4 volume envelopes lack
  these four rows. c04 must write Horns 1-4 (`--midi-only` or a full build; build/parts.json has them).

## Rejected or deferred
- A #4 (overlap the slurred muted-trumpet notes, `SLUR_ON_SUS_OVERLAP`): deferred; needs a new tool option and a
  smear check; lower priority than the timing and S1 items.
- A #5 (REP_ROW LegRep on the whole-note brass pedals): conditional on the horn cap. Measured: Horn 3/4 repeats rose
  1.9-3.5 -> 4.1-5.2 dB broadband (the cap works at f), but Horn 2 810/812/442/896 and the bass trombone stay 2.1-3.3 dB
  (Horn 2 plays ff, whose release is already 237 ms; the trombone has no cap). Open for c04: REP_ROW on Horn 2 808-814
  and the bass trombone 828-840.
- C #4 (per-onset string legato leads from c02's pcX): deferred; c03 changed the predecessors of many joins (C #1b),
  refit on c03.
- C #6b/c (BEAT_STRETCH 887, PHRASE_ARCS): deferred; one tempo change (the clamp) this cycle.
- Re-bow fills refit after the string release cap (BRIEF dry-hall #2): `build/rebow_fills.json` is empty in this
  folder, so there is nothing to refit yet.

## Measured (c02 -> c03; `actor_scripts/m03.py`, c02 on its own parts.json)
- **Hall tail (master):** final fermata (qn 1112.9) drop at 0.15 / 0.3 / 0.6 / 1.0 s 11.6 / 18.0 / 28.3 / 35.1 ->
  12.1 / 18.5 / 31.3 / 36.7 dB; RT(-5..-25 dB) 1.58 -> 1.31 s; late RT(-20..-35 dB) 2.51 -> 1.98 s (recordings 1.1-1.6;
  Movement I c44 2.42 -> 1.29). Drop at 0.3 s at the tutti cut-offs qn 5 / 21 / 102 / 374 / 450 / 814: 16.8 / 17.0 /
  13.4 / 14.3 / 19.7 / 17.3 -> 17.8 / 18.9 / 14.7 / 14.8 / 18.7 / 17.4 dB (all >= 13). Slowest stems to -20 dB at
  qn 5 / 21 / 374 / 814: cellos 0.69 / 0.65 / 0.53 / 0.63 -> 0.64 / 0.62 / 0.61 / 0.61 s; horn 1 0.54 -> 0.50 s
  (critic C's 0.3 s target not met: these cello notes end on legato rows, which the Sus cap does not touch).
- **Repeat dips (harmonic band | broadband 10 ms, dB):**
  - Violas portato 893-911: harmonic median about 4.1 -> 9.9 (911 1.7 -> 8.3, 909 1.2 -> 5.4).
  - Violins II portato 921-931: 0.6-3.1 -> 3.6-6.8.
  - Louré, broadband: 796 Vln I 6.8 -> 11.3, Vln II 7.9 -> 5.7, Vla 3.4 -> 3.3; 988 Vln I 6.2 -> 9.8, Vln II 7.6 ->
    14.6, Vc 6.3 -> 10.6, Trombone 1 3.6 -> 5.0.
  - Vc tenutos 980-983: -1.0..2.7 -> 3.9-8.8 (harmonic); Vc 325 / 327 -1.9 / 1.5 -> 3.0 / 3.3.
  - Cb tenutos 978-983: broadband 2.8-5.2 -> 5.6-9.9; 327 3.5 -> 7.7.
  - Horn 3 384 / 836 1.9 / 2.5 -> 5.2 / 4.2; Horn 4 810 / 836 3.5 / 3.5 -> 5.1 / 4.2 (broadband). Horn 2 and the bass
    trombone unchanged (see Rejected).
  - Unchanged: Vc 604 / 606 / 630 strokes (2.1 / 3.0 / 1.6 broadband), Vc 828 / 832 (2.2 / 2.5).
- **Timing (pcX re score onset, ms):**
  - F1 head second notes: Horn 1 74 / 602 / 634 / 650 / 1058 / 970 +140 / +157 / +156 / +169 / +157 / +241 -> +80 /
    +33 / +87 / +53 / +87 / +121; Oboe 1 90 / 578 / 826 / 1074 +194 / +227 / +165 / +151 -> +105 / +120 / +15 / +65;
    Flute 1 578 +200 -> -67; Bassoon 1 106 / 122 +255 / +370 -> +133 / +252; Trumpet 1 970 +219 -> +54.
  - Long string notes after slurred eighths: Vln I 66 / 626 / 97.5 / 657.5 +260 / +259 / +226 / +234 -> +126 / +124 /
    +97 / +120; Vln II 66 / 626 +270 / +256 -> +139 / +134. Still late: these 16 (Vln I) and 15 (Vln II) new joins
    median +85 / +128 ms; the lead is capped at 0.75 of the eighth.
  - Entries: Vln I / II at 600 +123 / +107 -> +72 / +55; Vla 600 +82 -> +51; 1048 Vln I +220 -> +116, Vla +255 -> +255.
  - Double basses long pitch changes 848 / 856 / 884 / 908 / 90 +137 / +121 / +156 / +122 / +246 -> +65 / +50 / +88 /
    +52 / +131 (900 +125 -> +170).
  - Trumpet 1 solo joins 200-264: pcX median -47 -> -6 ms, window 74 -> 64 ms.
  - String legato joins: Vln I rSD 75 -> 84 ms on all joins (the 16 new joins included; on the 196 common joins
    75 -> 81 ms); Vln II 73 -> 73, Vla 67 -> 70, Vc 59 -> 64. The attack probe flags the Vln I spread (84 > 75 ms).
- **Balance (re master, dB):**
  - Timpani rolls: 156-159 -16.8 -> -21.2; 872-876 -10.7 -> -18.1; 876-880 -11.4 -> -16.3; 930-933 -14.6 -> -18.5;
    886-888 -14.3 -> -12.4; 888-889 -16.6 -> -14.0; 1048-1049 -14.5 -> -12.0; final 1108-1109 / 1109-1112 / 1112-1113
    -18.9 / -22.4 / -25.0 -> -16.0 / -16.0 / -17.3 (critic B simulated -18.8, -17.3, -13.3, -13.7, -17.0..-18.3).
  - 888-892: Trumpet 1 -13.4 -> -10.5, Trumpet 3 -10.2, Tuba -10.0 -> -11.4.
  - Canon 900-920: Clarinet 1 -8.7 -> -11.2, Oboe 1 -10.5 -> -9.8, Vln I -11.1 -> -10.8, Flute 1 -14.2 -> -13.7.
  - Clarinet 2 184-200: -20.3 -> -14.0. Oboe 1 1052-1080: -19.3 -> -18.2.
  - Bass drum first 0.3 s at 888 / 1108: -24.0 / -23.5 -> -26.2 / -25.7 dB stem level (ring after 0.3 s within 1 dB).
  - Master quarter-qn levels into the arrival unchanged within 0.5 dB; 223 (-10.0) and 278 (-10.5) are still the loudest bars.
- **Master:** -16.1 LUFS, LRA 22.2 LU, float-sum peak 1.512 (+3.6 dBTP; the 24-bit file replaced by the float sum).
- **Delivered:** -19.8 LUFS, LRA 14.7 LU, TP -1.4 dBTP, limiter about 1.3 dB (c02 2.3), p10-to-max span 19.0 dB, ride max +12.6 dB.
- **Attack probe:** 1 flag, Violins I legato-join spread 84 ms (limit 75). c02's Violoncellos qn 24 flag is gone (+0.09 s).
- **Pre-roll:** still not silent on the strings (as c00-c02).
- **Silent notes (metrics):** Oboe 2 qn 856 (as in c02; unchanged data).

## REAPER
- Turn rule: at 13:58 the scherzo actor's waiter (since about 13:32) was older than mine, so I waited for it; it left
  the queue at 14:04 without taking REAPER, and I locked when Movement II unlocked.
- Lock held 14:05:09-14:34:51 (30 min): fresh start and open; full build of all 31 tracks and the tempo map; restart;
  audio device reopened (48000 Hz, 512, no input); render with `--force-memory` (44 GB settled, 14 GB compressed after
  the fresh open); save, quit, unlock. The stem fix and remeasure ran after unlocking (no REAPER).
- REAPER memory: 44 GB settled before the render (14 GB compressed), 44 GB after it (25-28 GB compressed). Other large
  processes: CrashRestartHelper 6 GB, Steam 3.7 GB. Disk 64 GB free.

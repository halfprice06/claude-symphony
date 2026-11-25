# Cycle 9 changes (actor, 2026-11-08): sfp / fp / subito, 315 Hz hump, width, accents, repeats, balance

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c08 render). Snapshot: `before/`. Scripts in `actor_scripts/`:
- `m09.py`: the cycle's before/after checks (m08.py plus the 315 Hz hump, brass accent fronts, basses swing, image, new
  dips and balance rows). Results: `m_c08.json`, `m_c09.json`.
- `sub09.py`: per-track drops at the sfp 592, fp 832 and sub. p 872.
- `tail09.py`: which stems carry a tutti stop's tail.
- `wet09.py`: tutti cut-off -10 / -20 / -30 dB times at qn 5 / 21 / 661 / 1113 (the wetness ceiling).
- `sub09.py` results are in the stem-fix section below.

## Tool code (each option defaults to off)
- `tools/score_to_parts.py`:
  - `FP_SPIKE_AT_MARK` (A #1, B #4). An fp / sfp attack level starts at the mark (a step), not 0.02 qn after it. A
    hairpin printed on the same onset ("sfp <") now starts where the attack has fallen (`fp_hp`). Its (q, level) points
    had overwritten the step, so every led note's pull (CC held from the moved note-on) read the p. The timpani's first
    CC7 point and its hairpin gain now start from the sf as well.
  - `FP_SPIKE_S`, `FP_VEL`: the fp's hold / fall in seconds and its attack velocity (as `SFP_SPIKE_S` / `SFP_VEL`).
  - `HP_CURVE["skip_staves"]`: staves whose hairpins stay linear (timpani, Movement I c51).
  - `PHRASE_SHAPE["types"]["drop"]` (B #3): a driving phrase that enters on a subito-softer mark or on a printed drop of
    `cc` or more takes no positive offset. Inside any shaped phrase, the offset is also not positive from such a mark to
    the next hairpin.
  - `ACCENT_SWELL_FROM_MOVED` (A #3): the families whose gentle-accent swell starts at the moved note-on of a led,
    non-legato accent.
  - `STR_REP_NEW_BOW["plain"]` (A #2): an unslurred same-pitch string repeat on a sustained row whose played gap (after
    every lead) is under min(gap_s, frac x onset distance) gets that gap before the next note's moved note-on. Excluded:
    re-bow and other split pieces, STR_REP_DETACH spans, the "skip" spans. parts.json `plain_gaps`.
  - `HARP_VEL_MAX` (B #1): a cap on the harp's final velocity.
- `tools/build_reaper.py`: mix.json `track_width` (C #2), REAPER's D_WIDTH, written by the full build and by
  `--mix-only`.

## Data (build/, each entry carries a "_c09" note)
- `build/score_config.py`, c09 block: FP_SPIKE_AT_MARK on; SFP_SPIKE_S (0.10, 0.30) v110 and FP_SPIKE_S (0.10, 0.30)
  v96; the c08 string sfp row leads removed; HP_CURVE skip_staves ("Timp",) (Movement I c51); PHRASE_SHAPE "drop"
  (cc 6); brass GENTLE_ACCENT swell_s (0.02, 0.18, 0.45) from the moved note-on; STR_REP_NEW_BOW "plain" (0.09 s, 30 %,
  mp and up; skip 864-884 on Vln I/II, Vc, Cb); RR_RESET_AT basses at 792 / 816 / 984 / 1056 / 1088; HARP_VEL_MAX 123.
- `build/roles.json`: counter-melody 264-292 Vla +4, Vc +5 (B #2); chorale horns -1, Tpt 1 +1 at 892-928 and +2 at
  1032-1047.5 (B #5); fresh brass at 872 -4 (B #3); clarinets under Flute 1 -2.5 (B #6); sfp p rows 593-596 from the
  c08 stems (A #1 / B #4).
- `build/note_trims.json`: harp 524 -5 (B #1). `build/entry_leads.json`: the c08 violas / celli 592 leads removed.
- `build/mix.json` (C #1-#5, B #6): horn bell 315 Hz -5 + gain +1.0, violas bell 315 -3 + gain +0.8; the side bell
  180 Hz -5.5 dB plus a side low shelf 60 Hz -3 in place of the 400 Hz -8 side shelf on 12 tracks and the 4 returns;
  track_width trumpets 0.5, trombones 0.6 with new pans; basses HP 35 Hz; upper winds' R Winds send -7; flute /
  clarinet f trim -1.5.
- parts.json: 0 WARNING, no Opus state change, re-bows unchanged.

## Deferred / rejected
- A #1 brass "Sfz Cres" row A/B (one more row on 8 tracks; memory); A #5 keyswitch leads and C's 2.3 kHz return
  low-pass (rejected with numbers, LEARNINGS); MANUAL-GAPS #4 Mid mics on the solo winds (full rebuilds).

## REAPER
- Lock 1 (2026-11-09 08:37-08:46): start, open, `--midi-only` all 31 tracks (RC 0), `--mix-only`, restart; handed
  back while memory settled. Lock 2 (09:39:11-10:16:20, 37 min; mvt1 c51 held REAPER 08:46-09:39): restart, settle
  to 44 GB (17 GB compressed) in 10 min, Audio_Init (48000 / 512 / no input), `render_cycle.py 9 --force-memory`
  (render 09:56-10:07), stem fix, `--mix-only` on the 18 stem-fixed tracks, quit (saved), unlock.
- Interruptions: /Volumes/MAC DRIVE hung from 2026-11-08 20:36 (listings blocked, "Interrupted system call"); the
  actor held the lock 21:12-21:15 without starting REAPER and waited until about 23:00 with no lock. On 2026-11-09 the
  drive answered every 10-second test.
- REAPER memory after the render: 45 GB, 28-30 GB compressed.

## Stem fix (`stemfix.log`; originals in `render_first/`; REAPER `build3_stemfix.log`)
Measured on the render with `sub09.py` (before = ff/f window, p = the p window after the mark):
- sfp 592: the existing 593-596 rows deepened by (drop - 10) / 0.875 (the row's mean factor over the p window):
  Fl 1 -7 -> -12, Fl 2 -8 -> -12, Cl 1 -6 -> -7.5, Cl 2 -7.5 -> -9, Bn 1 -4.5 -> -5.5, Bn 2 -8 -> -8.5, CA -5.5 -> -6,
  Tuba -4 -> -4.5, Timpani new -1.
- fp 832: new rows 833.25-839 (opened over the crescendo) for the parts whose sf-to-p drop stayed under 9 dB:
  Fl 2 -10, Ob 1 -8.5, Cl 1 -7, Cl 2 -5.5, Bn 2 -7, Hn 1-4 -1.5 / -3.5 / -1.5 / -3.5, Tbn 2 -1.5, Tuba -5, Vla -5.
- sub. p 872: rows 872-880 held to 876, opened over the crescendo 876-880: CA -7, Fl 1 -8, celli -5.
- Basses metric tables (`score_config.py`, end): 792-816 down 0 / mid 0 / beat 0 / off -0.5 (the default table gave
  down - off +6.2), and a new 1088-1108 table down 1.5 / mid 1.0 / beat 0.5 / off -1.5 (METRIC_BOWED extended to 1108).
- stem_fix reported no other difference than the metric_db counter. Delivered again: `deliver_stemfix.log`.

## Measured, c08 -> c09 (after the stem fix; `actor_scripts/m_c08.json`, `m_c09.json`)
- **sfp 592, ff-to-p drop per part** (target 10 dB): every sfp part 10.0-17.3 dB (c08: Fl 2 0.7, Bn 2 1.6, Cl 2 2.3,
  Fl 1 2.6, Cl 1 4.2, CA 4.5, Bn 1 5.4, Tuba 6.0, timpani -1.3 i.e. rose). Strings 12.4-14.5 (c08 8.6-12.9), basses
  10.2. sf peak minus p: strings 10.4-14.8 dB (c08 3.8-9.8), but basses 4.5 and Fl 2 5.5 (their sf peak sits under the
  ff before). Master ff -19.2 -> p -29.7 dB (10.5 dB; c08 6.2). Trumpets 1-2 are printed ff and excluded.
- **fp 832, sf-to-p drop** (target 8-10): all fp parts 8.2-15.3 dB except Flute 2 8.3 after its fix (c08: Fl 2 -4.6,
  Ob 1 -8.1, Cl 1 3.3, Bn 2 -0.2, Tuba 0.2, Vla -3.1, Timp 1.0, Hn 2/4 4.2/4.5, Tbn 1 6.8, Bass Tbn 1.9).
- **sub. p 872**: master 869-871 -34.2 -> 872-874 -38.4 dB (4.2 dB; c08 1.7). Winds -48.0 -> -48.9, strings -40.5 ->
  -41.5 (c08 strings rose 2.4). CA drop 9.5 (c08 1.3), Fl 1 7.0 (c08 -1.2), celli -0.2 (c08 -6.6, rose).
- **Width** (L/R correlation, loudest 10 %): below 250 Hz 0.758 -> 0.539 (refs 0.54-0.62); 31-62 0.85 -> 0.54,
  62-125 0.88 -> 0.65, 125-250 0.71 -> 0.49; 250-5000 0.471 -> 0.564; 5-16 kHz 0.388 -> 0.555; side/mid 200 Hz-5 kHz
  -4.5 -> -5.6 dB. Image (Tpt 1 / CA position measure) Trumpet 1 -1.3 / +0.4 -> +2.6 / +3.1, CA +4.5 / +4.1.
- **315 Hz hump** (third octave over the mean of 250 and 400): whole piece 5.8 -> 4.3 dB; F 5.6 -> 4.7, J 10.6 -> 8.5,
  P 7.0 -> 4.9, R 7.0 -> 5.4, T 6.0 -> 3.5 (target within 3 dB: missed in J, P, R, close in T).
- **Wetness** (BRIEF ceiling): tutti cut-offs -20 dB in 0.39 / 0.41 / 0.30 / 0.39 s (qn 5 / 21 / 661 / 1113; c08 0.41 /
  0.41 / 0.30 / 0.29); final chord RT60 from -10..-30 dB 1.26 s (c08 1.17). Inside the ceiling (0.50 s, 1.5 s).
- **Basses metre**, down - off: 792-816 6.2 -> 3.2, 816-840 3.5, 984-1056 3.5, 1056-1088 3.8, 1088-1108 0.0 -> 3.0 dB
  (target +2..+4). Swing (on-beat minus off-beat attack): 1088-1108 -27 -> -68 ms, 816-840 -30 ms (target +-12): the
  CC16 resets at the span starts did not even out the lilt.
- **Brass accent fronts** (2-5 kHz front minus body, master): median -8.0 -> -6.9 dB; per stem the accented notes are
  still 3-8 dB duller than the unaccented ones on the horns, trumpets 1 and tuba (Horn 1 -14.0 vs -5.9), brighter on
  the trombones.
- **Repeat dips**: violas 820-830 8.7-10.8 dB (828 9.3 -> 10.8), Vla 868 4.9 -> 6.0, but Vla 832 9.9 -> 3.8, Vla 426
  1.1, Vln I 884 0.0, Vc 832 4.3 (targets 5 dB).
- **Balance**: harp 524 -23.6 -> -29.8 (1.8 dB over the celli, target 1-3), master at 524 -19.1 -> -22.8; counter-melody
  violas -49.5 -> -46.2, celli -49.8 -> -46.9; chorale 900-928 horns 0.6-4.1 dB under Trumpet 1 (c08 3.6 over to 1.8
  under). The horns' soft passages fell 3-5 dB in plain RMS (Horn 1 pp 264-300 -49.1 -> -53.6, 10.9 dB under Vln I;
  stubs Hn 1 118 / Hn 2 122 -5.4 / -3.0), from the 315 Hz bell: critics should check it A- or K-weighted.
- **Tone**: centroid 993 -> 998 Hz; 31-62 Hz share -30.5 -> -26.7, 125-250 -11.3 -> -10.2 dB.
- **Loudness**: master -20.4 LUFS, LRA 22.0 LU, TP -0.2 dBFS, sample peak 0.974 (no clipping). Delivered -19.8 LUFS,
  LRA 14.7 LU, TP -1.6 dBTP, limiter about 0.8 dB on the loudest sample peak, span 18.8 dB.
- **Attack probe**: 1 flag, Violoncellos qn 24 +0.43 s, the build-shape artefact of c00-c08.
- **Pre-roll**: strings sound in the pre-roll, as in c06-c08.

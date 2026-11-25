# Cycle 5: changes (critics A, B, C on the c04 render)

Render: `cycles/c05/mvt3-mockup-c05.mp3`. Before-state in `before/`; the rendered data in `rendered_build/` (parts.json
and mix.json as rendered, before the stem fix). Two earlier actors stopped before REAPER (`INTERRUPTED.md`); a third
finished the build, render, measurements and stem fix. Actor checks: `actor_scripts/softends.py`, `tutti.py` (c04
baselines `softends_c04.txt`, `tutti_c04.txt`; c05 results `softends_c05.txt`, `tutti_c05.txt`), `m05.py bal|timing`
(`m05_bal.txt`, `m05_timing.txt`). c04's stems were deleted for disk space, so c04 values come from the c04 baselines and
the critics' reports.

## Accepted

### Soft string endings (critic C #1; BRIEF soft-endings warning)
- `tools/build_reaper.py` `cap_release`: `"ms"` may be a dict keyed by the group's dynamic word (generic; a number keeps
  the old meaning). `build/mix.json` `sus_release_cap_ms` on all five string tracks: pp 500, p 500, mf 300, f 150, ff 150
  ms (rows unchanged: Sus MAX, Sus Marc LITE, Leg Slur / Leg BC / Leg Port MAX, Tremolo). Opus state change: the five
  string tracks fully rebuilt.

### Timing (S1, S2; critic A)
- A #1: `build/score_config.py` `STR_REP_NEW_BOW["sus_min_s"]` 0.4 -> 0.3 (the violas' ff repeated quarters at 176 qpm,
  0.34 s, now get the new-bow gap and the re-tongue lead).
- A #1.2: `RETONGUE_LEAD_ART_S` Violoncellos Sus MAX +0.07 s.
- A #5: `tools/score_to_parts.py` `PIZZ_LEAD_S` (generic, default none); Violoncellos 0.035 s, Violins II 0.015 s.
- A #4: `tools/score_to_parts.py` `ROW_LEAD_S` (generic, default none); Trumpet 1 "Mute Sus" 0.035 s.
- A #3: `tools/score_to_parts.py` `PERC_END_AT` (generic per-stroke end); crash and bass drum strokes at 1108 end at
  1113.2 instead of ringing 9 s / 6 s on `min_s` (the 888 and 1048 strokes keep `min_s`).

### Balance (critic B #1-#4, `build/roles.json`, exactly as proposed)
- B #1 bars 255-258 (Vc +6, Vla +4, Vln II +4 / +2, Horns 3-4 +5 / +3, Vln I -4 / -2, woodwinds -2 ramp 2).
- B #2 pizz accompaniments (Cb -4 / -5, Vc -3, Vla +3 under the three soft solos).
- B #3 codetta (Tuba, B.tbn +3 -> +1; Trumpets 1-3 +2 on 360-376).
- B #4 crash at 1048 -3 dB.

`score_to_parts.py`: 0 WARNING. parts.json diffed against c04 (`actor_scripts/parts_c04.json`); re-bow points did not
change.

### Stem fix (after the render; level only)
- **The crash ignored its note-off.** With the stroke ending at 1113.2 (A #3), the crash still rang on after the cut-off
  at about 7 dB/s (stem -42.5 dB at the note-off, -51.0 at +1 s, -57.9 at +2 s). It was still the whole master tail:
  crash -50.1 against master -49.3 dB at +1 s (critic A's target: crash at least 10 dB under the master).
- Fix: `build/score_config.py` `PERC_MAP["Crash cymbals"]["_damp"] = [(1113.2, -40.0, 1.0)]` and
  `PERC_MAP["Bass drum"]["_damp"] = [(1113.2, -30.0, 1.0)]`. This uses the existing generic printed-damp rule, a
  post-hall fall that is linear in dB from the note-off. 40 dB/s is about the hall's own decay rate. parts.json
  regenerated (0 WARNING; only the two tracks' `vol_db` / `vol_bp` differ). `tools/stem_fix.py 5 cycles/c05/rendered_build
  <new build> --apply` (originals in `render_first/`), the same data written to REAPER with `build_reaper.py --mix-only
  "Crash cymbals" "Bass drum"` (checked in the saved .rpp), then `render_cycle.py 5 --measure-only`.
- Master after the final cut-off (0.2 s RMS, L0 -10.9 dB): +0.3 s -30.9 -> -31.1, +0.6 s -41.0 -> -42.5, +1 s -49.3 ->
  -58.5, +2 s -56.9 -> -83.9 dBFS (c04: -47.9 at +1 s, -53.2 at +2 s). Crash 26.5 dB under the master at +1 s. The
  delivered mp3 now ends 2.2 s after the cut-off (424.0 s instead of 426.8 s).

## Rejected or deferred
- C #2 brass width: deferred (the brass tracks were not rebuilt this cycle).
- C #3 soli side shelf: deferred. `side_lua` drops a switched shelf when the track has no static `side_shelf`, so the
  code needs changing first.
- C #4 harp harmonics, A #2 felt-stick timpani (pass 2), A #6, B #5: deferred.
- Carried from c04 and still open: the re-bow refit on c04/c05, the celli legato ends, "Horns a2", the grace run into
  bar 35, Bassoon 1 solo v100 joins.

## Measured (c04 -> c05)
- **Soft string ends (C #1; time to fall 10 / 20 dB after the note-off, median of pp-mp ends):** Violins I (6) 0.08 /
  0.13 -> 0.23 / 0.36 s, Violins II (5) 0.09 / 0.18 -> 0.26 / 0.40 s, Violas (2) 0.06 / 0.15 -> 0.09 / 0.27 s.
  References: 0.20-0.40 s to -10 dB, 0.43-0.58 s to -20 dB. The violins are now inside the -10 dB range at every soft end
  except Violins I 198.88 (0.13 s) and 477 (0.15 s). Their -20 dB times sit 0.03-0.07 s under the -20 dB range. The violas
  are still fast: 454.86 falls 10 dB in 0.05 s, and 198.88 (CC11 7, L0 -62 dB) in 0.14 s. f-ff ends unchanged: Vln I
  0.10 / 0.23 -> 0.09 / 0.23, Vln II 0.14 / 0.23 -> 0.12 / 0.24, Vla 0.11 / 0.32 -> 0.12 / 0.32, Vc 0.25 / 0.45 -> 0.25 /
  0.45, Cb 0.13 / 0.35 -> 0.12 / 0.39 s. On the master the bar-50 soft end (qn 198.89, 71.21 s) used to fall 8.1 dB in
  the first 0.1 s; it now falls 1.4 dB in 0.1 s and 8.9 dB in 0.3 s.
- **Tutti cut-offs (master, `tutti.py`):** time to -20 dB 0.54 / 0.54 / 0.42 / 0.49 / 0.49 -> 0.47 / 0.50 / 0.41 / 0.47
  / 0.49 s (Movement I's measured range 0.45-0.55); time to -10 dB 0.24-0.34 -> 0.18-0.34 s. These stay in range.
- **Timing (A, pcX median):** violas 1033-1048 +111 -> +20 ms; celli Sus MAX repeats 604-658 +136..+184 -> +127 ms
  (n 4); cello pizz minus bass pizz on 59 shared onsets +39 -> +1 ms (Vc +7, Cb +3); Violins II pizz +25 -> +10 ms; muted
  Trumpet 1 minus cor anglais on 24 shared onsets +35 -> +4 ms.
- **String legato joins (probe, pcX median / robust SD):** Violins I +20 / 61 -> +24 / 63 ms, Violins II +1 / 50 -> +8 /
  54, Violas -5 / 47 -> -6 / 47, Violoncellos +21 / 43 -> +19 / 43. These are about unchanged.
- **Balance (re master, power mean over the span; my method reads about 3 dB lower than critic B's on the unchanged 888
  crash):**
  - B #4: crash at 1048 -13.5 dB, the same as its 888 level (-13.5) and under Tuba (-9.3) and Trumpet 1 (-11.3).
    Critic B's c04 reading was -7.6 against -10.3 at 888.
  - B #3: Trumpets 1-3 -13.2 / -13.7 / -12.5 against Tuba -11.3 and B.tbn -13.4 per stem. The three trumpets together
    (about -8.3) sit over Tuba plus B.tbn (about -9.2).
  - B #2: the solos are -2.9 / -1.2 / -3.5 (Tpt1 201-264, Bn1 456-488, CA 680-744). Under them the basses are -15.0 /
    -13.9 / -15.0 and the celli -14.6 / -14.9 / -14.2. Violas -16.6 against Violins II -15.8 at 201-264.
  - B #1: Horn 3 -4.8..-9.5, Violas -6.4..-11.7, celli -9.1..-13.9 on 1016-1032; flutes -15..-50 there.
  - Climaxes (master, 4 qn): 888 -10.0, 1108 -10.5, 1048 -11.4 dB. Bars 223 and 278 stay the loudest.
- **Master:** -16.1 LUFS, LRA 21.6 LU, float-sum peak 1.619 (+4.2 dBTP; the 24-bit file is replaced by the float sum).
- **Delivered** `cycles/c05/mvt3-mockup-c05.mp3` (after the stem fix): -19.8 LUFS, LRA 14.7 LU, TP -1.6 dBTP, limiter
  about 2.0 dB, p10-to-max span 18.9 dB.
- **Attack probe:** 0 late or holes. The string pre-roll lines are the same as c04's.

## REAPER
- Lock 10:18:05-12:06:16 (1 h 48 min). I waited behind scherzo c04 (held from 09:46:55), with no other waiter. The
  waits were foreground `reaper_ctl.py lock` runs.
- `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` on the five strings (all "Opus state changed,
  full rebuild", release caps printed per dynamic), save, `--midi-only` on Flute 1-2, Oboe 1-2, Clarinet 1-2, Horn 3-4,
  Trumpet 1-3, Bass trombone, Tuba, Crash cymbals, Bass drum (all 15 MIDI-only), `restart` (31 tracks), Audio_Init
  (48000 / 512, no input), `render_cycle.py 5`.
- **First render rejected (half-loaded samples).** `render_cycle.py`'s settle gate passed at 30 GB (c04: 45 GB with
  the same Opus states, state sizes within 0.02 %). That render had the attack probe at 5 flags: Violoncellos qn 9 +0.18
  s and qn 24 +0.54 s late, and string join spread on Violins II / Violas / celli. pcX median / SD rose to +62 / 119,
  +40 / 100, +65 / 105 ms. The joins were late at every dynamic and in every part of the piece, including f-ff, where
  nothing changed. Winds and brass were unflagged. Its probe, metrics and log are in `render1_rejected/`; its stems were
  deleted. Then `restart` again, and I waited about 44 min while memory grew from 17 GB to 44 GB at about 0.4 GB/min,
  then Audio_Init and `render_cycle.py 5` again. That render passed the probe (0 flags).
- After the stem fix: `build_reaper.py --mix-only "Crash cymbals" "Bass drum"`, `save`, `quit`, `unlock`.
- REAPER memory: 46 GB settled before the second render (27 GB compressed), 46 GB after it (29 GB compressed).

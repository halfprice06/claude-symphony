# Cycle 16: changes (actor)

One render from a freshly restarted REAPER (33 tracks, every track updated with `--midi-only`; no Opus state changed, checked offline against `jobs/*.b64` before the build), then two level-only stem fixes:
- `tools/stem_fix.py 16 cycles/c16/rendered_build build --apply` (string pickup level, brass pickup trims back)
- `tools/stem_fix.py 16 <the fix-1 build> build --apply` (accent refit)

Then `render_cycle.py 16 --measure-only`, `build_reaper.py --mix-only` (all tracks), save, quit (the quit job timed out after the save; REAPER had exited).

Where things are:
- First-render stems: `cycles/c16/render_first/`. The data and code the render was made from: `cycles/c16/rendered_build/`.
- Snapshot of the c15 tools and data: `cycles/c16/before/`.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c16-actor/` (`pk.py` / `pk2.py` pickup measures, `ssj.py`, `solo.py` K-weighted solo margins, `spans.py`, `trace.py`, `clim.py`, `envdiff.py`, `pdiff.py`, and the pre-render simulation in `sim/`).

All level changes were simulated on the c15 stems before the render (`stem_fix.py` into scratch, then `deliver_master.py`): delivered LRA 14.6 LU, span 19.2 dB, limiter 1.9 dB. The render measured 14.6 / 19.0 / 1.9.

## Accepted

### A #1 (test): pickups after a rest on the Sus row (`PICKUP_SUS`, generic)
- New generic rule in `tools/score_to_parts.py`; movement I values in `build/score_config.py`: families wind/brass/string, `max_qn` 0.62, `rest_qn` 0.2, `min_target_qn` 0.5, `level_db` strings -2.5 (stem fix: -3.5).
- A monophonic pickup (not accented or tenuto) with nothing of its track sounding 0.2 qn before it, whose next note starts at its written end at a new pitch in the same slur (or, on strings, both unslurred), plays the Sus row. The target is joined through the c15 `SLUR_START_SUS` path (overlap `LEG_OVERLAP`, target led min(0.12 s, 0.45 x pickup), velocity `SOST_VEL`). New parts.json key `pickup_sus`: 94 pickups on 21 tracks. No new articulation rows.
- The +3 dB note trims on the theme pickups (Trumpet 1 664.5/672.5, Horns a2 272.5/664.5/672.5) were removed for the render (Sus-row brass pickups sat -0.7 dB under their targets in c15). Without them the pickups sat -4..-6 dB under the targets, so the stem fix put them back.
- Result: **failed on its pass criteria.**
  - The four exposed cases A named are unchanged, on A's score-window measure: Violins I 136.5 -11.0 (c15 -8.5), Bass clarinet 304.5 -8.5 (-8.7), 432.5 -10.7 (-11.3), Oboe 1 312.5 -11.7 (-12.4). Pass was -6..-1.
  - Traces show why. The Sus pickup after a rest rises as slowly as the Leg pickup did. Violins I bar 35: -52.6 dB at the score onset (c15 -50.8), with the target's body at -30. Oboe 1 bar 79: -55 at the onset in both renders. The slow first sound is the mf attack of a note after a rest on either row, not the Leg row's sustain layer.
  - Family medians on the score-window measure (`pk.py`, all 94): winds -3.9 -> -1.7, brass -5.2 -> -6.0, strings -2.0 -> +1.6.
  - On the pickup's own sounding time (`pk2.py`, moved onset to the target's moved onset): winds -3.3 -> -4.6, brass -4.8 -> -7.7, strings -5.5 -> -6.2.
  - The tutti-motive pickups of bars 27-29 / 139 (flute, oboe, clarinet) gained +2.5..+4 dB on the score-window measure.
- Left in the render and the tools so the render matches parts.json. Revert next cycle (`PICKUP_SUS = None`; also restore the string pickups' -3.5 dB and the targets' fits by refit). The next thing to try for the exposed pickups is entry lead plus a fill from the moved onset, as for the c15 soft string entries.

### A #2: bar 51 tenuto (Horn 1 201)
- The critic's fill/trim change was simulated on the c15 stems. It overshot by 6 dB at -0.12 s and left the note 5-7 dB low at +0.12..+0.3 s, so it was not used.
- Instead, an exact `LEVEL_SHAPES` fill measured from the c15 hole, in seconds from the score onset: +6 at -0.04, +8 at 0, +6 at +0.04, +3 at +0.08, +2.5 at +0.30, 0 at +0.40.
- Celli 201 fill `pre_s` 0.081 -> 0.12 (0.16 simulated a 5 dB overshoot).
- Horn 1 at the change, c15 -> c16: lowest -47.0 -> -40.0 dB against the E-flat's -36 (dip 4 dB; pass < 4). At +0.04..+0.3 s: -35.3..-37.3 (pass -2..+1 of the E-flat).
- The -2.5 dB point at 200.877 that A asked about is the C5 pitch trim (-5) ramping in over 0.25 qn from the moved onset. It stays.

### A #3: two-note slur release on short notes (`SLUR_PAIR_RELEASE` "short_s", "full_short_s", "join_db")
- Settings: 0.35 s, 0.12 s, -3 dB.
- A second note written under 0.35 s starts its release at its moved onset, full at min(0.12 s, half its length). It takes -3 dB when it is a SLUR_START_SUS/PICKUP_SUS join. Such pairs count from 0.25 qn notes up.
- Pair releases: Violins II 4 -> 6; other tracks unchanged in count.
- `ssj.py` (second peak minus first body, all joins): winds +4.1 -> +4.8, brass +5.2 -> +5.4. This is not a pass: most joins are in slurs of three or more notes, where the pair release does not apply. Open.

### A #4: `auto_fills.py` retimed branch for led targets
- For a target led 0.10 s or more, the fill is full from 0.08 s after the moved onset (or 0.05 s before this render's minimum, if earlier), held to 0.35 s. Constants: `RETIME_LEAD_MIN_S`, `RETIME_AFTER_MOVED_S`, `RETIME_HOLD_S`.
- Run on c15 with `--write`. Excluded: the PICKUP_SUS targets (their join changes), Horn 1 201 and celli 201.
- Result: 39 entries: 9 new, 1 raised, 10 retimed (celli 82/122/270/654/687/694/712, Horn 1 614, Bn1 420, Cl1 507.5), and the rest lowered or removed by the overshoot rule.

### A #5
- **Oboe 1 314.5-316:** +3 dB exact shape from its moved onset.
- **Basses bar 72:** new generic `DETACH_LEAD_KEEP_QN` 0.15. A detached stroke after a detached stroke keeps 0.15 qn of its gap when a lead moves it. Cb 285 moved from 284.761 to 284.900, gap 0.011 -> 0.15 qn. Stem dip at the gap only about 2 dB (pass 4): partial.

### B #1: Horn 4 trims
- `mix.json` `dyn_trim_db` f/ff/fff 2.5/5.3/2.8 -> 1.0/1.5/0.5.
- `roles.json` [504,518,-4,2] -> [504,520,-4,0.5].
- Horn 4 against the sum of the other stems: letter G (464-480) -9.5 -> -13.3 dB; bar 41 -11.8 -> -15.6.

### B #2: bar 130 roles
- Bassoon 1 +4, Violins II +3, celli -3, Horn 4 -2 over 515.5-520.
- Bassoon 1 against the loudest other stem: -6.7/-5.5 -> -1.3/-0.1 dB (level with the pedal). Against the sum of the rest: -10.6/-9.4 -> -6.1/-4.5.

### B #3 / C #2 (combined): soft solos
- **Lento cor anglais, bars 5-8:**
  - The celli's re-bow fill at 26.516 had its two late bumps capped: +0.36..+0.52 s at +4.5 dB, +0.80..+1.08 s at +2. The +10 over the +0.14 s dip stays.
  - Roles: celli [24,29,-2.5,1], violas [24,29,-2,1].
  - Cor anglais `LEVEL_SHAPES`: +2 to 27, +1.5 to 31. C's +3 simulated +6 dB over the sum at 19-21 together with the basses' cut. B's +2.5 over 26.5-32 was halved, because C asks to leave bars 7-8 to the strings.
  - Result, cor anglais against the sum of the other stems (K-weighted): 19-21 / 21-23 / 23-25 / 27-28 / 28-31: c15 +1.2 / -0.5 / -0.1 / -8.7 / -7.6 -> c16 +5.1 / +2.1 / +3.3 / -4.8 / -5.8.
- **Horn 1, bars 13-14:** role +4.5 (C's +3 simulated -1..-3). Against the sum: -4.1 / -4.3 / -6.8 -> +0.4 / +0.5 / -1.7.
- **Oboe 1, bars 145-146:** role +4. Against the sum: -5.8 / +1.0 / -6.3 -> -1.5 / +5.4 / -2.5.
- **Cor anglais coda:** [683,694,+2]. Against the celli: -3.1..-3.9 dB (target within 3).
- **Basses:** -2 at 16-28, 48-56, 576-584 (C asked -3/-2.5/-3; B #4's pp trim takes another 1.5).

### B #4: basses
- `dyn_trim_db` f/ff 1/2 -> 2.5/4.
- `soft_trim_db` pp 10 -> 8.5, with an mf anchor 3.7 (mf unchanged). B wrote pp "2.0 to 0.5"; the file has 10, and B's -1.5 dB was applied.
- Master 100-300 Hz share in the loudest frames (-6..0 dB of the file max): -8.52 -> -7.94 dB, with C #3 below.

### B #5: string f trims
- Violins I f -1.5 -> 0 (mf anchor 1.0), Violins II -2.5 -> -1.0 (mf -0.8), celli -2 -> -1 (mf 0.7). The anchors keep mf where it was.
- The pitch-matched mf -> f step was not re-measured this cycle. Open for the critics.

### B #6: trumpets
- Trumpets 2/3 [104,124,-2,0.5] and [551.5,554,-2.5,0.25].
- Trumpet 1 [484,486.5,2,0.25].

### C #1: bar 121
- The c14 letter-G lift on the ten held ff parts is held and grows to +4 dB at 483.5, gone at 484.0.
- `ARRIVAL_WEIGHT_AT[484]` hold-back -1.5 -> -0.5.
- Master: bar 121 last beat over bar 120: +1.2 -> +3.1 dB (target 3.5-4.5). Step at 484: +5.1 -> +3.4 dB (target 2-3). Bar 122 beat 1: -10.40 -> -10.44 dB.

### C #3: violin loud EQ
- `loud_eq` high shelf 2.5 kHz -2.5 dB on Violins I/II over the celli's loud spans.
- Master 2-5 kHz share in the loudest frames: -9.57 -> -10.32 dB (C's target about -10.8; reference -11.1).

### C #4: second-theme head swell
- Front-loaded `LEVEL_SHAPES` on Horn 1 (to +5.5) and celli (to +5.0) at 184/584.
- Horn 1, 184.3-185 to 186.5-187.5: exposition +1.0 -> +2.7 dB; recapitulation -0.1 -> +1.6 dB (target +3).
- The eighth at 187.5 still stands over the 188 quarter (-34.1 against -40.5 dB).

### Accent refit
- `fit_accents.py 16 build/parts.json --family {brass,wind,string} --keep-long-qn 1.4 --pickup-over 2.5 --write` on the fix-1 stems, applied as stem fix 2.
- Predicted in 2-4 dB: brass 34/37, winds 125/141, strings 103/135.
- 2-5 kHz first 80 ms over body > 3 dB: brass 0, winds 0, strings 1.
- Several string theme targets lost large fitted steps. For example, Violins II 113 [5, 4.25] -> 0.86: the Sus pickup's join no longer sags.

## Rejected or deferred
- **C #5 (basses coda repeats), rejected.** On the c15 stem the on-beat and off-beat C2 eighths of 664-676 differ by -0.7 dB (RMS of the first 0.2 s; the off-beats are louder), and by +2.4 dB in 50-140 Hz only. That is not 5 dB, and a -2 dB on-beat step would reverse the metre.
- **A #2, critic's literal fix:** replaced by the measured shape (above).
- **A #5, Horns 3-4 a2 at bars 80-81:** deferred again (needs the Hn3 staff's events in the a2 track).
- **B #3, refit of the 26.516 re-bow with `fit_rebows.py`:** not done (c10 lesson: single-row refits next to old shapes were no better). Hand caps instead.

## Before / after (c15 -> c16 after both stem fixes)

| Measure | c15 | c16 |
|---|---|---|
| Master integrated (float stem sum) | -16.2 LUFS | -16.3 LUFS |
| Master LRA | 22.2 LU | 22.2 LU |
| Master sample peak | 1.461 | 1.541 |
| Master true peak (float) | +3.3 dBFS | +3.8 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.5 LU | 14.5 LU |
| p10-to-max span | 19.1 dB | 19.0 dB |
| Delivery limiter | 2.0 dB | 2.0 dB |
| Delivered true peak | -1.6 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.98 / 4.54 dB | 8.82 / 4.56 dB |

- First render, before the stem fixes: LRA 14.6, span 19.0, limiter 1.9.
- Climax order on delivered S max: 160 -10.10 > 122 -11.20 > 167-170 -12.89 (c15 -9.96 > -11.11 > -12.81).
- Master top peaks: 1.541 at qn 636.19 (the fff downbeat), 1.506 at 641.19, 1.348 at 484.53, 1.301 at 643.12.
- Attack probe: 0 flagged.
- REAPER memory (`metrics/memory.txt`): 25 GiB with 0 compressed when the render started, 45 GiB with 28 compressed after it. Other processes: VM 2.7 GB, Steam 2.2 GB, a python3.12 job of 2.1 GB.
- Delivered mp3: `cycles/c16/mvt1-mockup-c16.mp3`.

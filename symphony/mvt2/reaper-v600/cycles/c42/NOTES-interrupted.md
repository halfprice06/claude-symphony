# Cycle 42: interrupted before the build (actor, 2026-11-07)

## Why it stopped

Took the REAPER lock at 18:58:01 after the turn rule (the finale's c05 waiter left the queue at 18:54 without taking the lock; Movement I c46 released at about 18:57). Started REAPER. The disk check failed: `df -h /System/Volumes/Data` showed **24 GiB free**, and the rule is at least 30 GB. The actor may delete nothing outside its own cycle folder and scratch, so it could not free space. For scale: `cycles/c41` is 7.0 GB and `cycles/c40` 4.4 GB (render, render_first, stems). Movement I's scratch `/private/tmp/claude-501/mockup-loop/mvt1-c46-actor` holds 1.5 GB. A crashed process `CrashRestartHelper` held 6 GB of memory, mostly compressed.

REAPER had no project open (only `start` had run). `reaper_ctl.py quit` refused to save an empty project, so REAPER was terminated with `pkill -x REAPER`, which loses nothing with no project open. Then `reaper_ctl.py unlock` ran at 19:01:38. No bridge job ran, and the .rpp and jobs/ are unchanged.

**To resume:** free disk space to 30 GB or more (Dan or the coordinator: for example old cycles' `render_first/` folders), then rerun the actor for c42. `before/` exists, so step 2 resumes: every edit below is done and parts.json is regenerated. What remains is steps 5-6: build, restart, render, post-render refit, CHANGES and HISTORY.

## Done (steps 1-4)

Snapshot: `cycles/c42/before/` (tools/*.py, score_config.py, build/*.json).

- `tools/fit_rebows.py`: the plan now includes the CC7 lane, `+ 20*log10(cc7/127)`, from `step_at(cc7, q, 127)`. The docstring is updated.
- `build/rebow_fills.json`, refit on the c41 final stems with the CC7 plan (`fit_rebows.py 41 build/parts.json --hold-max-after 301:0 --tracks "Violins II,Violas,Violoncellos"`). Only these keys were taken from the refit; the rest are unchanged:
  - 223 holds: Violins II +6.94 -> +0.50, violas +8.56 -> +2.10, celli +1.17 -> -5.29 dB. c39's holds were +0.9 / 0.0 / -4.8.
  - Violins II 263.921: hold -4.6 -> -6.0 (clamped). The fit no longer fills back c41 B #2's -2 dB of CC7.
  - Violas 296.9: held at -3.0 from 1.12 s (A #4).
  - Violas div 298.3 and 301.25: back to the c39 lists (C #4).
- `build/mix.json`, release caps:
  - Violins I, Violins II, Violas, Violoncellos, Double basses: pp/p 400 -> 600 ms, mf-ff 300 kept.
  - Violin I solo, Violoncellos div, Violins II div, Violas div: 300 ms at all layers -> `[300 ms mf/f/ff, 600 ms pp/p]`.
  - Horns unchanged.
- `tools/score_to_parts.py`: `STR_REP_NEW_BOW["sus_fall"]` now also applies on the stroke and portato-stroke path. It replaces a smaller portato fall, at the repeat's base CC <= max_cc.
- `build/score_config.py`, c42 block at the end:
  - `sus_fall`: basses 12 CC; Violins II, Violas, Violoncellos 8 CC / 0.06 s at p or softer.
  - A #3: Violas 69 and 248.5 added to `DOWNBOW_STROKE_AT`. They take the Leg -> Sus entry path: velocity 105, lead 0.06 s / 0.115 s, the note before cut at the keyswitch with a 0.04 qn gap. Their c41 `LEVEL_SHAPES_S` are removed, as is basses 144's -5 shape.
  - B #1: Horn 1's 182 shape +5 -> +2, and +3 over 184.1-195.35.
  - C #5: Violins I/II +2 over 190-199.6 (ramp 190-194). Violins II +4 over 252.5-253.55, back to 0 under the 254 attack (C's 253.45 end moved so that no fall lands on the held note).
  - C #3: Oboe 1 LEVEL_SHAPES +4.2 at 148.0, back to 0 at 148.59. The swell came from the HP_SOFT_DEC gain ramp, not from the role C named. The step falls in the gap after the note that ends at 147.93. The role is unchanged.
- `build/roles.json`:
  - B #2: Horn 1 16.5-42 +2.5 -> +4.5; Bassoon 1, Bassoon 2 and Bass clarinet `[17.5, 41.9, -1.5, 0.5]`.
  - B #3: Flute 1 `[120.4, 123.95, 2, 0.4]`.
  - C #5: Violoncellos `[190.5, 204, -3, 4]` -> `[186.5, 204, -3, 4]` (in by 186.5; the end ramp is unchanged, so 200-204 does not change).
- `build/parts.json` is regenerated with no WARNING. Diff against c41 (`/private/tmp/.../parts_c41.json`, now deleted; `cycles/c42/before/parts.json` is the old one):
  - vol_db changes only on Flute 1, Oboe 1, Bass clarinet, Bassoons 1-2, Horn 1, Violins I/II, Violas, Violoncellos, Violas div, Double basses (144 +5 where the shape was removed).
  - Notes, keyswitches and CC11/CC1 change only on Violas (69 and 248.5 strokes) and on the sus_fall onsets: Violins II 49.875, Violoncellos 127.84, Double basses 143.84 / 155.86 / 167.87.

Opus states that change (caps): Violins I, Violins II, Violas, Violoncellos, Double basses, Violin I solo, Violoncellos div, Violins II div, Violas div. No articulation row changes.

## Still to do

1. Lock (turn rule), then `reaper_ctl.py start`, then `open`. Wait 2 min for memory to settle.
2. `tools/build_reaper.py build/parts.json jobs --midi-only "Flute 1" "Oboe 1" "Bass clarinet" "Bassoon 1" "Bassoon 2" "Horn 1" "Violins I" "Violins II" "Violas" "Violoncellos" "Double basses" "Violin I solo" "Violoncellos div" "Violins II div" "Violas div"`. The 9 tracks with cap changes rebuild fully.
3. `restart`, then the audio init job (`cycles/c42/_c42_audio_init.lua`), then `render_cycle.py 42`.
4. Measure with `cycles/c42/actor_scripts/check42.py cycles/c42/render build/parts.json`. c41 baseline: `actor_scripts/check42_c41.txt`. Also run `cycles/c41/actor_scripts/m41.py` for t10/t20. Targets:
   - niente: steady fall from 223;
   - final chord: -20 dB at 0.43-0.58 s;
   - soft repeat dips: master >= 3 dB (c41: 7 of 15 under 3, Violins II 45 at 1.8);
   - bar 91: no viola rise.
5. Refit the re-bows after the render, as c41 did: `fit_rebows.py 42 cycles/c42/rendered_build/parts.json --hold-max-after 298:0 --window "Double basses:2.6" --skip "Double basses:273.229"` on the string tracks, then `relevel41.py` for the basses pedal (c39 means +1.5) and the coda. Apply with stem_fix and `--mix-only` while holding the lock.

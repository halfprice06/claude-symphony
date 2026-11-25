# Cycle 43: interrupted before the build (disk)

On 2026-11-08 the actor waited for its turn from 08:48. The scherzo c03 actor held the lock, and the Movement I c48 actor was waiting ahead of this one. The lock came at 09:46:17. By then `/System/Volumes/Data` had **24 GiB free** (about 25.8 GB), under the 30 GB rule. It was 31 GiB at 08:30, and the other threads' renders used the rest.

REAPER was not started. The lock was released at 09:46:38, held 21 s.

## Done (steps 1-4 complete)

- Snapshot in `before/` (c42 final tools and data).
- Every change in `CHANGES.md` is implemented in tools/, build/score_config.py and build/*.json, and `build/parts.json` is regenerated with no WARNINGs.
- pdiff against c42 was checked.
- The stem_fix + deliver_master simulation on the c42 stems gives span 18.7 dB and limiter 2.3 dB (`actor_scripts/stemfix_sim.log`).

## Left to do (step 5 on; do not snapshot again)

1. Free disk to 30 GB or more. This needs Dan or the coordinator: old render folders of any thread, Movement I's render_first copies, and so on. Do not delete files outside this cycle's folder.
2. Follow the turn rule (`actor_scripts/turn_lock.sh`, writing to `lock.log`).
3. `reaper_ctl.py restart`, then wait about 2 min after memory settles.
4. Build, run from symphony/mvt2/reaper-v600/: `tools/build_reaper.py build/parts.json jobs --midi-only "Cor anglais" "Clarinet 1" "Bass clarinet" "Horn 1" "Horn 2" "Horn 3" "Horn 4" "Timpani" "Harp" "Violins II" "Violas" "Violoncellos" "Double basses" "Harp harmonics" "Violoncellos div" "Violas div"`. Double basses rebuilds fully, because its release cap changed.
5. `reaper_ctl.py restart`, then wait for memory to settle. Check disk (30 GB or more), memory, the mount and the 32 tracks.
6. Run `_c43_audio_init.lua`, then `render_cycle.py 43`.
7. Run `tools/state_check.py` against c42's stems (`cycles/c42/render`, `cycles/c43/before` vs `cycles/c43/render`, `cycles/c43/rendered_build`). Measure:
   - the basses' old pitch at 286 / 246 / 61 (target -15 dB or lower at +0.35 s);
   - the clarinet pcX medians (within ±25 / ±30 ms);
   - the bar 62 limiter;
   - Violoncellos 66 stem dip (6-9 dB);
   - Horn 1 196 and Violas 238 arrivals;
   - Horn 4 268.
8. Quit, unlock, finish CHANGES.md, HISTORY and LEARNINGS.

## Second attempt (2026-11-08, after the coordinator reported 34 GB free at about 11:07)

- Followed the turn rule from 11:08. The finale (mvt3 c05), then Movement I c49 and the scherzo c05 used REAPER first. The lock came at 12:34:25.
- Free disk was then **26 GiB** (about 27.9 GB), under 30 GB again: the three renders before mine used the 8 GB freed earlier.
- REAPER was not started. The lock was released at 12:34:46 (21 s). Nothing else changed; the "Left to do" list above still applies.
- Space a render needs: a render folder is about 3.8 GB, plus up to 1 GB for render_first and the mp3.
- Large deletable candidates, for Dan or the coordinator to decide (not deleted, since they are outside this cycle's folder): this thread's old `cycles/cNN/render_first` folders (c41 2.9 GB, c30 1.2 GB, c40 1.0 GB, c42 0.9 GB, c38 0.5 GB, ...) and old full render folders (about 3.8 GB each).

## Resolved

The third attempt (lock 13:09-13:47 on 2026-11-08, after Dan freed disk) completed the build and the render; see CHANGES.md.

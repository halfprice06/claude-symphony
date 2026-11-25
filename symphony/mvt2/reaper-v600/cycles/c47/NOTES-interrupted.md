# c47 actor: interrupted before the build and render (2026-11-09 10:20)

Resolved: resumed 10:59 the same day and completed (build, render 11:26, checks); see CHANGES.md.

Done: every data change (cycles/c47/CHANGES.md, "Changes"), simulated on the c46 stems; build/parts.json regenerated
(0 WARNINGs, equal to the simulated build); before/ snapshot taken. No change was written to REAPER.

Not done: the build, render, checks, HISTORY/LEARNINGS entries. The lock was taken at 10:16:30 with 25 GiB free on
/System/Volumes/Data (under the 30 GB rule; the other threads' renders and stem fixes since 08:53, 46 GiB then). REAPER
was started and the project opened (36 tracks), then quit without any build; the lock was released at 10:20 because the
run had to end.

Resume (step 2 of actor_prompt: before/ exists, do not snapshot again):
1. Check disk >= 30 GB and the turn rule; `cycles/c47/actor_scripts/turn_lock.sh > cycles/c47/lock_wait.log` (background).
2. reaper_ctl.py start, open; wait until memory is flat for 2 min.
3. tools/build_reaper.py build/parts.json jobs --midi-only "Flute 1" "Flute 2" "Oboe 1" "Oboe 2" "Cor anglais"
   "Clarinet 1" "Clarinet 2" "Bass clarinet" "Bassoon 1" "Bassoon 2" "Contrabassoon" "Horn 1" "Horn 4" "Timpani"
   "Violins I" "Violins II" "Violas" "Violoncellos" "Double basses" "Violoncellos div" "Violins II div" "Violas div"
   (no Opus state change expected; check build.log for any full rebuild).
4. reaper_ctl.py restart; wait for settled memory; python3 ~/.rpr-bridge/rpr.py run cycles/c47/actor_scripts/_c47_audio_init.lua;
   then at once render_cycle.py 47.
5. Checks: cycles/c47/actor_scripts/m47.py cycles/c47/rendered_build cycles/c47/rendered_build --render cycles/c47/render;
   entries47.py cycles/c47/render cycles/c47/rendered_build/parts.json (bar 79 and wind median; c46: -38 ms, 8 entries
   over 60 ms early); cycles/c45/actor_scripts/check44.py (wetness, final chord t20 target <= 0.45 s; simulated 0.430);
   s1check44.py (c46: n 49, own-band median 8.2, master 3.7, 7 under 3 dB); state_check.py c46 -> c47 (same tempo map);
   probe 0, span <= 19, limiter <= 3 (simulated 15.3 LU / 18.8 dB / 2.4 dB).
6. quit, unlock; fill RESULTS_PLACEHOLDER in CHANGES.md; HISTORY and LEARNINGS entries.

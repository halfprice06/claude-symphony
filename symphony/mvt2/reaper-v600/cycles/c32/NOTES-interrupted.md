# c32 actor: interrupted before the render (2026-11-07 01:22)

Done: snapshot in before/; every edit listed in the actor's handback (score_config.py c32 block, roles/note_trims/entry_leads/loop_fills/rebow_fills.json, mix.json loud_eq on Horns 1/2/4, score_to_parts.py: LOOP_FILLS warning and CC1_HOLD for vibrato families); parts.json regenerated with no WARNING; `--midi-only` build of 15 tracks written into the project (build.log, 0 errors) and saved by `reaper_ctl.py restart`. No Opus state changed.
Not done: render, measurement, stem fixes, CHANGES.md, HISTORY/LEARNINGS entries. REAPER was quit and the lock released.
To resume: lock, `reaper_ctl.py restart` (the project already holds the c32 data), wait for memory to settle, Audio_Init (`_c32_audio_init.lua`), `render_cycle.py 32`.

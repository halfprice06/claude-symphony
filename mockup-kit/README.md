# Mockup kit: orchestral mockups in REAPER with EastWest Hollywood Orchestra (Opus)

Tools, method and learnings for turning a LilyPond score from this repo into a REAPER mockup played by Hollywood Orchestra Opus Edition, built and improved by Claude without using the REAPER GUI. It grew out of the movement II mockup (`symphony/mvt2/reaper/`, not committed: the project, renders and generated plugin states stay local). The kit is updated after each batch of improvement cycles; `sync_from_mvt2.sh` copies the current pipeline in.

Read `LEARNINGS.md` before starting. It records what was measured about Opus, the HO patches, REAPER and the bridge, and where `guides/reaper-claude-scripting-guide.md` is wrong for this library (patch loading is scriptable; CC11 is dynamics and CC1 vibrato in HO).

## Contents

- `bridge/install_bridge.py`: installs the file bridge from the scripting guide (`~/.rpr-bridge`, the REAPER runner, `__startup.lua`).
- `opus/opus_state.py`: reads `.oib` patch files and builds Opus plugin states, so a script can load any HO patch into a track (`TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", state)`). `opus/dump_ks.py` reads a patch's keyswitch map and controllers; `opus/ks_maps.json` has the maps of the patches used so far.
- `pipeline/`: the reference pipeline from movement II. `mockup.ly` (one staff per player; dumps MIDI plus an event list of every articulation, text, dynamic, hairpin, slur and tremolo), `score_to_parts.py` (score data to notes, keyswitches and CC lanes per track), `build_reaper.py` (tracks, patches, mix, envelopes, tempo map into REAPER), `render_cycle.py` (save, wait for samples, render master + stems, measure, mp3), `measure.py` (per-bar stem levels against printed dynamics, loudness, spectrum against a reference recording), `probe_attacks.py`. `example-config/` holds the movement II mix, role and note-trim files.
- `loop/`: the actor-critic method: `BRIEF-mvt2-example.md` (the brief every agent read), `critic_prompt.md`, `actor_prompt.md`, and `workflow.js` (the Workflow script: three critics in parallel per cycle, then one actor who edits, rebuilds and renders).

## Mocking up another score

1. Install the bridge (`python3 mockup-kit/bridge/install_bridge.py`), start REAPER, check `python3 ~/.rpr-bridge/rpr.py status`. Copy `opus/*` to `~/.rpr-bridge/libs/ew_ho/`.
2. Make a work folder next to the score (keep it out of git). Copy `pipeline/mockup.ly` and point its includes and `\pl` staff list at the new score's part variables. Run LilyPond (convert-ly first if the score is older than your LilyPond).
3. Edit the track table at the top of `score_to_parts.py` (track name, source staves, `.oib` patch, family, pan) for the new instrumentation. Dump keyswitch maps for any new patches with `dump_ks.py` and add them to `ks_maps.json`. Check every track's pitch range against its patch's keyswitch keys.
4. Generate `parts.json`, then run `build_reaper.py` with REAPER open (each patch takes 20-60 s to load; render only after loading settles). Set the project to 1x offline rendering (see LEARNINGS).
5. Render and measure with `render_cycle.py 0`, listen, then run improvement cycles with the `loop/` prompts and `workflow.js`, adapting the brief to the new score.

The pipeline is tuned on one movement. Things still tied to movement II are listed in `LEARNINGS.md` and in the comments of `score_to_parts.py`; generalising them (the track table and per-score trims into config) is planned once the 30 cycles finish.

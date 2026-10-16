# Mockup kit: orchestral mockups in REAPER with EastWest Hollywood Orchestra (Opus)

Tools, method and learnings for turning a LilyPond score from this repo into a REAPER mockup played by Hollywood Orchestra Opus Edition, built and improved by Claude without using the REAPER GUI. It comes from the movement II mockup (`symphony/mvt2/reaper/`, 27 rendered cycles c00-c26) and the movement I mockup (`symphony/mvt1/reaper/`, in progress; this kit holds its tools as of c05). Neither work folder is committed: the projects, renders and generated plugin states stay local.

Read `LEARNINGS.md` before starting, beginning with "What a listener noticed that measurement missed". It records what was measured about Opus, the HO patches, REAPER and the bridge, and where `guides/reaper-claude-scripting-guide.md` is wrong for this library (patch loading is scriptable; in HO CC11 crossfades the dynamic layers, and CC1 crossfades a non-vibrato and a vibrato layer).

## Contents

- `bridge/install_bridge.py`: installs the file bridge from the scripting guide (`~/.rpr-bridge`, the REAPER runner, `__startup.lua`).
- `opus/opus_state.py`: reads `.oib` patch files and builds Opus plugin states, so a script can load any HO patch into a track (`TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", state)`). `opus/dump_ks.py` reads a patch's keyswitch map and controllers; `opus/ks_maps.json` and `ks_maps_extra.json` have the maps of the patches used.
- `pipeline/`: the reference pipeline (movement II's, generalised in movement I). Movement-specific tables live in a per-score `build/score_config.py` that `score_to_parts.py` runs after its generic defaults; `example-config/` (movement II) and `example-config-mvt1/` hold complete configs (`score_config.py`, `mix.json`, `probe.json`; mvt1 also its `mockup.ly`). New tools from movement I: `fit_rebows.py` (a level shape per re-bow, from a render), `space_rebows.py` (sections' re-bows at least 0.6 s apart), `fit_loops.py` (periodic loop profiles on long notes), `stem_fix.py` (exact level-only fixes on the stems), `rendermap.py` (file time of a score qn in renders made with a shifted tempo map). `mockup.ly` (one staff per player plus a DrumStaff, here with movement I's staves; dumps MIDI plus an event list of every articulation, text, dynamic, hairpin, slur and tremolo), `score_to_parts.py` (score data to notes, keyswitches, CC lanes and volume envelopes per track), `build_reaper.py` (tracks, patches with unused rows unloaded, mix, envelopes, tempo map into REAPER; `--midi-only` and `--mix-only` for cheaper updates), `render_cycle.py` (save, wait for samples, render master + stems at 1x, attack probe, measure, delivery mp3), `deliver_master.py` (the headphone delivery master), `measure.py`, `probe_attacks.py`, `motion.py` (loudness-motion figures), `auto_fills.py` (legato-sag fills from the previous render). `example-config/` holds the movement II mix, role, trim, lead, fill and loop-profile files.
- `loop/`: the actor-critic method: `BRIEF-mvt2-example.md` and `BRIEF-mvt1-example.md` (the briefs every agent read, with Dan's listening notes), `DYNAMICS-RESEARCH.md` (delivery targets), and movement I's `critic_prompt.md`, `actor_prompt.md` and `workflow.js` (three critics in parallel per cycle, then one actor who edits, rebuilds, restarts REAPER and renders; run one cycle per workflow call with args {start, end, prev}). Replace the work-folder paths in them for a new score.
- `sync_from_work.sh <work folder> [name]`: copies a work folder's tools (and with a name, its config) into the kit.

## Starting a new mockup

These are the lessons that cost the most cycles to learn. Do them from the first build.

1. **Unload unused articulation rows** (`UNLOAD_UNUSED_ROWS` in `build_reaper.py`). It cut a 32-track project from 61 GB to 43 GB with no change in sound; before that, renders ended with under 1 GB free on a 96 GB Mac.
2. **Render at 1x offline** (`RENDER_1X 1` in the `.rpp`; it cannot be set by API) with a silent pre-roll bar that carries each track's first keyswitch, first CC values and the CC36 round-robin reset (CC69 = 0 on strings). Full-speed renders start notes up to 0.6 s late.
3. **Restart REAPER before every render and quit it after.** Save, quit, start with `-new`, open the project with `Main_openProject("noprompt:...")`, wait until memory is flat, render once, save and quit. Fix level-only problems on the stems afterwards instead of rendering twice.
4. **Deliver through `deliver_master.py`.** An unprocessed orchestral master has a 20-24 LU loudness range, which is unusable on headphones; target 14-16 LU delivered, with soft levels also raised in the mix.
5. **CC11 for dynamics, CC1 only for the vibrato layer.** CC11 crossfades the dynamic layers; make balance corrections in the volume envelope so the printed dynamic keeps its timbre. Do not hold CC1 inside the non-vib/vib crossfade (about 55-76).
6. **Read keyswitch maps and CC11 layer tables from the `.oib` files** (`dump_ks.py`), never from screenshots or memory. A keyswitch to an unloaded row is ignored, and soft swells near a layer boundary jump 8-11 dB.
7. **Use the true-stereo hall** (HO's `S. Cal Hall Perc TS FR 3.3s` IR with `trueStereo: true`, one shared insert copied into every patch, depth set by send level), with a side-only low shelf (-2 dB at 200 Hz) on the bass tracks.
8. **Re-bow long held string notes.** Split any note over about 4.5 s into same-pitch Sus MAX pieces at staggered times per section, and fit a level shape for each re-bow. One sample held for 15-25 s pulses with its 3.95 s loop.
9. **Give the pre-roll bar its own meter** (3/4 for the 3 qn pre-roll; `build_reaper.py` does this and stops if any tempo marker lands off its qn). With the score's 4/4 there, everything played 1/6 qn early (LEARNINGS section 11).
10. **Keep accents gentle.** Plain Sus MAX at moderate velocity, CC11 at the printed dynamic, and a short volume swell (full at +0.07 s, gone by +0.6 s) of about +3-6 dB; check 2-5 kHz attack energy against the body as well as level. Accent samples and CC11 bumps into the top layer sound harsh.

Then, as in movement II:

1. Install the bridge (`python3 mockup-kit/bridge/install_bridge.py`), start REAPER, check `python3 ~/.rpr-bridge/rpr.py status`. Copy `opus/*` to `~/.rpr-bridge/libs/ew_ho/`.
2. Make a work folder next to the score (keep it out of git). Copy `pipeline/mockup.ly` and point its includes and `\pl` staff list at the new score's part variables. Run LilyPond (convert-ly first if the score is older than your LilyPond).
3. Write `build/score_config.py` from an example config: `TRACKS` (track name, source staves, `.oib` patch, family, seat), `SCORE_END`, `SCORE_TITLE`, `RAMP_SPANS` for the printed rit./accel. steps, `PERC_MAP` for unpitched percussion, and `build/probe.json` (attack-probe checks). Keep the per-onset tables empty. Dump keyswitch maps for new patches and check every track's pitch range against its patch's keyswitch keys and sample range.
4. Start the per-note config files empty (`note_trims`, `pitch_trims`, `leg_leads`, `entry_leads`, `early_fills`, `loop_profiles`, `rebow_fills`, `roles`): they are keyed to a score's onsets. Keep `mix.json` (mics, hall, seats, EQ) as a starting point.
5. Generate `parts.json`, build with `build_reaper.py`, restart REAPER, then `render_cycle.py 0`. Ask a person to listen early and often; then run improvement cycles with the `loop/` prompts and `workflow.js`, adapting the brief to the new score.

`LEARNINGS.md` section 19 lists what movement II left open; section 20 adds movement I's lessons.

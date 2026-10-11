# Mockup improvement loop: brief for every critic and actor

## Goal

Dan (2026-10-11), after hearing the first REAPER mockup of movement II: "It's ok. Use 30 actor subagent critic loops to make it better. Use all available resources."

The mockup is movement II (Adagio, A flat major) of the symphony, score `symphony/mvt2/v77`, played in REAPER by EastWest Hollywood Orchestra Opus Edition (Diamond) through the Opus plugin. Each cycle makes it sound more like a real orchestra playing this score well. The score is fixed. Only the rendering changes.

Dan's standing priorities for renders (from `symphony/render/BRIEF.md`, written for the earlier FluidSynth/VPO renders, and still his rules):
1. Articulations must be audible and correct: slurs/legato, tenuto, accents, tremolo, pizzicato, as printed.
2. Each track's level must match its printed dynamic and its role (melody above accompaniment) at every dynamic level.
3. Blend: one ensemble in one room (common reverb, seating, matched colours, nothing sticking out because of a sample set).
4. Accents: emphasis and weight, not a hard click (about 2-4 dB, no sharp transient).
5. Timpani rolls: start at the printed dynamic, then settle under the texture. Only a printed crescendo makes a roll grow. A long roll is never the loudest stem unless the timpani lead.

## Nobody can hear

You cannot hear audio. Judge by measurements and by reading the data: per-bar stem levels against the printed dynamics, spectra, loudness range, onset timing, note lengths and keyswitch placement in the MIDI, and comparison with a real orchestral recording (`symphony/render/assets/refs/dvorak9_i_columbia.mp3`). Say which judgements are measured and which are inferred.

## Where things are (all under `symphony/mvt2/reaper/`)

- `README.md`: how the mockup was built, including how Opus patches are loaded by script. Read it first.
- `mvt2-v77-mockup.rpp`: the REAPER project, open in the running REAPER.
- `build/mockup.ly`, `build/mockup-events.tsv`, `build/mockup.midi`: the per-player extraction of the score (MIDI plus every articulation, text, dynamic, hairpin, slur and tremolo with its position in quarter notes).
- `build/parts.json`: exactly what is written into REAPER: per track the patch, notes, keyswitches and CC lanes, all in quarter notes from the start.
- `tools/score_to_parts.py` (score -> parts.json), `tools/build_reaper.py` (parts.json -> REAPER tracks), `tools/render_cycle.py N` (save, render master + all stems, measure, mp3), `tools/measure.py`.
- `~/.rpr-bridge/`: the REAPER bridge (`python3 ~/.rpr-bridge/rpr.py run job.lua`), `libs/ew_ho/opus_state.py` (Opus state), `libs/ew_ho/ks_maps.json` (keyswitch maps read from the patch files), `libs/ew_ho/dump_ks.py` (dump another patch's map).
- The score: `symphony/mvt2/v77/score.pdf`, `sections/*.ily`, `global.ily`. Bar numbers: bars 1-36 in 3/4, 37-64 in 4/4, 65-92 in 3/4 (from `sections.txt`).
- Sample libraries: `/Volumes/MAC DRIVE/EW Hollywood {Strings,Brass,Harp,Orchestral Woodwinds,Orchestral Percussion} Diamond/*Opus Instruments/` (`.oib` patch files: individual articulation patches, KS Masters, divisi, ensembles, mutes). Any of them can be loaded with `opus_state.py`.
- Library knowledge: `guides/eastwest-hollywood-orchestra/` (HO and Opus manuals as text, reviews, tutorial transcripts) and `guides/reaper-claude-scripting-guide.md`. Orchestration books: `reference-books/` (see `INVENTORY.md`; text in `reference-books/text/`). Impulse responses with licences: `symphony/render/assets/ir/` and `assets/README.md`.
- Loop records: `loop/HISTORY.md` (one entry per cycle), `cycles/cNN/` (that cycle's reports, render, metrics, mp3, CHANGES.md). Cycle 0 is the first mockup.

## Facts already established

- Hollywood Orchestra: CC11 (expression) crossfades the dynamic layers; CC1 (mod wheel) controls vibrato (HO manual section 2.1.3). Velocity sets dynamics of short notes and legato transition speed in legato patches.
- Legato patches (Leg Slur MAX etc.) are monophonic: a chord in a legato articulation drops notes. A legato transition needs the notes to overlap.
- Opus loads samples in the background after a patch is set; render only after loading settles (`render_cycle.py` waits for REAPER's memory to stop growing).
- A patch is set by writing its full instrument JSON into an Opus state (never a locator-only zone: it crashes Opus).
- The Harp KS Master's keyswitches (21-35) overlap the harp's low notes. The Celli KS Master has keyswitches at 80-90.
- Mic positions in the KS Masters default to Close + Main loaded (`layerMatrix.columns`, with per-column volume).
- The REAPER master has no effects. Render settings 1 = master mix plus one stem per track, in one pass.

## Rules

- Only the actor drives REAPER. Critics never run `rpr.py`, never touch the bridge folder, never write into `mvt2-v77-mockup.rpp`, and never start renders. Critics may run their own analysis scripts on the rendered files (python in `~/.venvs/claude-composes-reaper/bin/python` has numpy, soundfile, mido; also ffmpeg, lilypond).
- Never edit the score or anything in `symphony/mvt2/v77/`, `symphony/mvt1/`, `symphony/render/`. Never commit or push. Never delete files outside your own cycle folder and your own scratch folder.
- Do not install software (no pip, brew or downloads). No GUI or computer use; REAPER is driven only through the bridge.
- Everything that changes the result lives in scripts or config files under `symphony/mvt2/reaper/` (tools, `build/*.json`), so the project can be rebuilt from scratch with the tools. A mix setting made only inside REAPER is lost when a track is rebuilt.
- The printed notes, dynamics, articulations and tempos are the reference. A rendering must not contradict them. Small musical liberties that real players take (shaping inside a hairpin, a slight swell on a long note, breath before a breath mark, a little rubato inside a printed rit.) are allowed if the score supports them.
- Keep scratch under 2 GB per agent, in `/private/tmp/claude-501/mockup-loop/<your label>/`.

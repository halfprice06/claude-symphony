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

Dan (2026-10-11, after cycle 7): "Right now, I have to turn my head phones to max volume to hear the soft parts well, which makes the loudest parts almost unbearable. pls improve in this respect." So:
6. The delivered mp3 must be comfortable at one volume setting: soft passages clearly audible, loud passages not painful. Research and targets: `loop/DYNAMICS-RESEARCH.md` (read it). `render_cycle.py` masters the mp3 with `tools/deliver_master.py` (a slow look-ahead gain ride that lifts only the quiet passages, up to +10 dB, then -19 LUFS and a -1.5 dBTP limiter; c08 test: LRA 23.6 -> 15.9 LU, limiter 4.6 dB). Targets for the delivered mp3: LRA 14-16 LU, 16-19 dB from the 10th-percentile short-term loudness to the loudest, no reversed crescendos or diminuendos, the climax still clearly the loudest, limiter at most about 3 dB. Do part of the work in the mix: raise ppp/pp by a further 2-4 dB and p by 1-2 dB with the soft_trim volume envelopes (not CC11, which sets timbre), give exposed soft solos +2-3 dB, and lower the loudest timpani and brass transients at the climax so the limiter does less. pp must still sound soft through timbre and texture. Critics report these numbers for both the unprocessed master and the mp3.

7. Memory (added by the thread before cycle 24): with 32 tracks, every render since c21 has pushed REAPER from about 21 GB to 63 GB with 44-51 GB compressed, leaving under 1 GB free on this 96 GB Mac. That is the condition that froze the Mac on 2026-10-11. Cut REAPER's sample memory so a full render ends below about 45 GB: load only the articulation rows and mic columns each track actually uses (measure each patch's cost), merge or drop tracks whose patch is barely used, and do not add new instances without removing others. Record REAPER memory after the render in CHANGES.md. When a cycle's render finishes, quit REAPER (save first) so the critics' analysis does not run against a full machine.

Dan (2026-10-12, after listening to cycle 24) — fix these first; they come from a person who heard the render:
8. "Sounds like there's some kind of weird bowing effect being applied on the last note; it doesn't sound right." The final chord (strings held from qn ~286-292 to 304 under the rit. and fermata, many seconds long) plays one note per string track with a slow CC11 fade. Candidates to check against the stems: the sample's sustain loop (strings loop every 3.95 s) and the periodic inverse loop profile on that note (`build/loop_profiles.json`), bow-change notches or merge notches, CC1 vibrato movement, the volume-envelope fade, and the reverb tail. Find which one makes an audible periodic or swelling movement on the last note and remove it; a real section holds the chord with staggered, inaudible bow changes and a smooth diminuendo.
9. "The accented notes the trombones play during the call back to movement 1 at the climax: the accents are too harsh." Trombone 1, bars 63-64 (qn 212.5-219.5: Sus Accent MAX and Marc Lng notes, velocities 94-110, accent dB in the envelope). Make them weighty but not harsh: lower velocity and attack boost, consider Sus MAX with a gentle envelope swell instead of the accent samples, and check the 2-5 kHz energy of the attacks against the surrounding strings. Dan's earlier rule applies: accents are emphasis and weight, about 2-4 dB, with no hard front edge.

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
- Library knowledge: `guides/eastwest-hollywood-orchestra/` (HO and Opus manuals as text, reviews, tutorial transcripts; the May 2021 edition `text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt` has the most per-instrument detail on velocity, CC11, CC1 and mic positions) and `guides/reaper-claude-scripting-guide.md`. Orchestration books: `reference-books/` (see `INVENTORY.md`; text in `reference-books/text/`). Impulse responses with licences: `symphony/render/assets/ir/` and `assets/README.md`.
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

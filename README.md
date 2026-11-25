# claude_composes

Files from the "Music" Claude project: a four-movement neo-Romantic symphony composed by Claude in LilyPond over about 2,500 critic-and-revise cycles, its REAPER/EastWest mockups, the score videos, and the reference material used along the way.

## Where to start

- The symphony has four movements: I (C minor, `symphony/mvt1/`), II Adagio (A flat, `symphony/mvt2/`), III Scherzo (E, `symphony/scherzo/`), IV Finale (`symphony/mvt3/`; the folder name predates the scherzo).
- Final scores: `symphony/mvt1/v621`, `symphony/mvt2/v600`, `symphony/scherzo/v600`, `symphony/mvt3/v600` (LilyPond source, MIDI, score and parts PDFs, rebuilt with LilyPond 2.24).
- How the music was written: `symphony/LOOP-METHOD.md` (the compose/critique loop), each movement's plan, `CHECKPOINT.md`, `critics/` and `tools/`, and `symphony/coherence/` (themes shared across movements).
- How the mockups were made: `mockup-kit/README.md` and `mockup-kit/LEARNINGS.md`, then `mockup-kit/loop/` (one folder of loop notes per movement series) and `mockup-kit/pipeline/` (score-to-REAPER tools and each movement's config). The full working record of every mockup cycle is in the REAPER work folders: `symphony/mvt1/reaper` and `symphony/mvt2/reaper` (first series), then `symphony/mvt1/reaper-v621`, `symphony/mvt2/reaper-v600`, `symphony/scherzo/reaper-v600` and `symphony/mvt3/reaper-v600`. Each has `loop/` (brief, history, learnings), `build/` (config), `tools/` and `cycles/cNN/` (that cycle's `CHANGES.md`, three critic reports and measurements).
- How the videos were made: `symphony/video/glow/README.md`.
- Final mockup renders: Movement I cycle 63, II cycle 57, scherzo cycle 30, finale cycle 30. The audio and video files are not in git (see "Not in the repository").

## Layout

- `symphony/` — the symphony.
  - `movement-1-plan.md`, `cyclic-notes.md`, `LOOP-METHOD.md`, `loop-kit/` — plans for the movements and the compose/critique loop method and scripts. `reading/` holds reading lists.
  - `mvt1/` — movement I. `v621` is the final version (LilyPond source, MIDI, score and parts PDFs); `v421` to `v620` are the versions of the last loop series. Versions before v421 are in the git history (all present at commit fdb1ffc) and can be rebuilt with `mvt1/tools/build.sh`. `mvt1/critics/` holds the critiques between versions and `mvt1/tools/` the build and analysis scripts.
  - `mvt2/` — movement II, organised the same way (`movement-2-plan.md`, `critics/`, `tools/`); final version v600, with v400 to v599 from the last series.
  - `scherzo/` — the scherzo, organised the same way; final version v600.
  - `coherence/` — notes and scripts checking theme quotations across the movements.
  - `mvt3/` — the finale, organised the same way (`movement-3-plan.md`, `critics/`, `tools/`); final version v600.
  - `video/glow/` — the glowing-score videos of all four movements: tools, per-movement annotations, title cards, tempo maps and stem loudness data. `video/mvt2/` is the first score video of movement II.
  - `mockup-research/` — measurements of expert mockup projects (EastWest templates, REAPER and Cubase projects, MIDI mockups).
  - `mvt2/reaper-export/` — the first export of movement II for REAPER.
  - `render/` — work on improving the MP3 rendering of movement I (`BRIEF.md`, `HISTORY.md`, one folder per cycle `rNN/`, `critics/`, `tools/`). Sources and licences for the third-party soundfont, sample library (VPO3), impulse responses and reference recordings are in `render/assets/README.md`. The soundfont, the VPO3, Iowa and Philharmonia sample files and the FLAC reference recordings are not committed (see `.gitignore`); download them from those sources. Only the newest render cycle keeps its MP3s, and render PDFs are not committed.
- `mockup-kit/` — tools, method and learnings for REAPER mockups of the scores with EastWest Hollywood Orchestra (Opus), scripted by Claude through a file bridge: loading Opus patches by script, score-to-REAPER pipeline, stem measurement, and the actor–critic improvement loop. See `mockup-kit/README.md` and `LEARNINGS.md`. `loop/mvt1-series2/`, `loop/scherzo-series/` and `loop/finale-series/` hold each movement's brief, history, learnings and last-cycle reports; `pipeline/example-config-*` hold each movement's build config; `reference/` holds other people's mockup projects for study; `listening-page/` is the source of the page with the mockups, scores and videos.
- `reference-corpus/` — orchestral scores by Mozart, Beethoven, Dvořák, Tchaikovsky and others (Mutopia LilyPond sources, MusicXML conversions, form and harmony annotations). See `reference-corpus/README.md` for sources and licences.
- `reference-books/` — the list of reference books used (`README.md`) and Claude's guide to them (`INVENTORY.md`). The books and their extracted text are not in the repository.
- `guides/` — working guides. `reaper-claude-scripting-guide.md` sets up a file bridge so Claude Code can script REAPER (tempo maps, tracks, MIDI notes, keyswitches, CC curves, stem renders) for orchestral and film-score work. `eastwest-hollywood-orchestra/` holds the EastWest Hollywood Orchestra Opus Edition manuals (2025, and the more detailed May 2021 edition) and the Opus engine manual, reviews, forum threads and YouTube tutorial transcripts (see its `README.md`).

## Not in the repository

- The reference books (PDFs and extracted page text). They are under copyright; `reference-books/README.md` lists them.
- Mockup audio (mp3, stems), the score video MP4s and the REAPER project files. The work folders on main hold text only: per-cycle actor and critic scripts, logs, plots, the `before/` snapshots and notes over 1 MB were left out. They are on the Mac that ran REAPER, under `symphony/<movement>/reaper-v6xx/cycles/cNN/` and `symphony/video/glow/`; the finished video is on YouTube.
- Sample libraries and soundfonts (EastWest Hollywood Orchestra, VPO3, Iowa, Philharmonia) and the FLAC reference recordings. Sources are in `symphony/render/assets/README.md`.

# claude_composes

Files from the "Music" Claude project: a neo-Romantic symphony and the reference material used to write it.

- `symphony/` — the symphony.
  - `movement-1-plan.md`, `cyclic-notes.md`, `LOOP-METHOD.md`, `loop-kit/` — plans for the movements and the compose/critique loop method and scripts. `reading/` holds reading lists.
  - `mvt1/v421` — the final version of movement I (LilyPond source, MIDI, score and parts PDFs); `mvt1/v221` keeps the most recent MP3. Earlier versions are in the git history (all versions are present at commit fdb1ffc) and can be rebuilt with `mvt1/tools/build.sh`. `mvt1/critics/` holds the critiques between versions and `mvt1/tools/` the build and analysis scripts.
  - `mvt2/` — movement II, organised the same way (`movement-2-plan.md`, `critics/`, `tools/`); only the final version (v400) is on main, plus v201 for its MP3.
  - `scherzo/` — the scherzo, organised the same way; final version v400.
  - `coherence/` — notes and scripts checking theme quotations across the movements.
  - `mvt3/` — the finale, organised the same way (`movement-3-plan.md`, `critics/`, `tools/`); final version v400, plus v391 for its MP3.
  - `render/` — work on improving the MP3 rendering of movement I (`BRIEF.md`, `HISTORY.md`, one folder per cycle `rNN/`, `critics/`, `tools/`). Sources and licences for the third-party soundfont, sample library (VPO3), impulse responses and reference recordings are in `render/assets/README.md`. The soundfont, the VPO3, Iowa and Philharmonia sample files and the FLAC reference recordings are not committed (see `.gitignore`); download them from those sources. Only the newest render cycle keeps its MP3s, and render PDFs are not committed.
- `mockup-kit/` — tools, method and learnings for REAPER mockups of the scores with EastWest Hollywood Orchestra (Opus), scripted by Claude through a file bridge: loading Opus patches by script, score-to-REAPER pipeline, stem measurement, and the actor–critic improvement loop. See `mockup-kit/README.md` and `LEARNINGS.md`.
- `reference-corpus/` — orchestral scores by Mozart, Beethoven, Dvořák, Tchaikovsky and others (Mutopia LilyPond sources, MusicXML conversions, form and harmony annotations). See `reference-corpus/README.md` for sources and licences.
- `reference-books/` — an inventory and extracted text of the reference books; the book PDFs themselves are in `pdfs/`.
- `guides/` — working guides. `reaper-claude-scripting-guide.md` sets up a file bridge so Claude Code can script REAPER (tempo maps, tracks, MIDI notes, keyswitches, CC curves, stem renders) for orchestral and film-score work. `eastwest-hollywood-orchestra/` holds the EastWest Hollywood Orchestra Opus Edition and Opus engine manuals, reviews, forum threads and YouTube tutorial transcripts (see its `README.md`).

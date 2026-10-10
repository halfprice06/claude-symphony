# claude_composes

Files from the "Music" Claude project: a neo-Romantic symphony and the reference material used to write it.

- `symphony/` — the symphony.
  - `movement-1-plan.md`, `cyclic-notes.md`, `LOOP-METHOD.md`, `loop-kit/` — plans for the movements and the compose/critique loop method and scripts. `reading/` holds reading lists.
  - `mvt1/v01` … — every version of movement I (LilyPond source and MIDI). Only the newest version has its PDF score and MP3 committed; the others can be rebuilt with `mvt1/tools/build.sh`. `mvt1/critics/` holds the critiques between versions and `mvt1/tools/` the build and analysis scripts.
  - `mvt2/` — movement II, organised the same way (`movement-2-plan.md`, versions `v01` …, `critics/`, `tools/`); again only the newest version has its PDF and MP3.
  - `render/` — work on improving the MP3 rendering of movement I (`BRIEF.md`, `HISTORY.md`, one folder per cycle `rNN/`, `critics/`, `tools/`). Sources and licences for the third-party soundfont, sample library (VPO3), impulse responses and reference recordings are in `render/assets/README.md`. The soundfont, the VPO3 and Iowa sample files and the FLAC reference recordings are not committed (see `.gitignore`); download them from those sources. Only the newest render cycle keeps its MP3s, and render PDFs are not committed.
- `reference-corpus/` — orchestral scores by Mozart, Beethoven, Dvořák, Tchaikovsky and others (Mutopia LilyPond sources, MusicXML conversions, form and harmony annotations). See `reference-corpus/README.md` for sources and licences.
- `reference-books/` — an inventory and extracted text of the reference books; the book PDFs themselves are in `pdfs/`.
- `guides/` — working guides. `reaper-claude-scripting-guide.md` sets up a file bridge so Claude Code can script REAPER (tempo maps, tracks, MIDI notes, keyswitches, CC curves, stem renders) for orchestral and film-score work.

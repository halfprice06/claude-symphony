# claude_composes

Files from the "Music" Claude project: a neo-Romantic symphony and the reference material used to write it.

- `symphony/` — the symphony.
  - `movement-1-plan.md`, `cyclic-notes.md` — plans for movement I and for movements II and III.
  - `mvt1/v01` … `mvt1/v120` — every version of movement I (LilyPond source and MIDI). `v120` is the finished version and the only one with its PDF score and MP3 committed; the others can be rebuilt with `mvt1/tools/build.sh`. `mvt1/critics/` holds the critiques between versions and `mvt1/tools/` the build and analysis scripts.
  - `render/` — work on improving the MP3 rendering of movement I (`BRIEF.md`, `HISTORY.md`, one folder per cycle `rNN/`, `critics/`, `tools/`). Sources and licences for the third-party soundfont, sample library (VPO3), impulse responses and reference recordings are in `render/assets/README.md`. The soundfont, the VPO3 sample files and the two Brahms FLAC recordings are not committed (see `.gitignore`); download them from those sources. Render PDFs are not committed either.
- `reference-corpus/` — orchestral scores by Mozart, Beethoven, Dvořák, Tchaikovsky and others (Mutopia LilyPond sources, MusicXML conversions, form and harmony annotations). See `reference-corpus/README.md` for sources and licences.

The `pdfs/` folder holds music reference books.

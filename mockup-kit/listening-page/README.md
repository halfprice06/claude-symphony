# Listening page (mockups artifact)

Source of https://claude.ai/artifact/7V3Gt4wRG5NKRXEFgYchCd ("Symphony No. 1 Mockups"). `index.html` is hand-written; there is no build step. Always publish to that URL (pass it as `url`; a new conversation reads the artifact once first), so Dan's bookmark keeps working.

## What the page holds

- Tab "REAPER mockups": the newest mockup mp3 of each movement. Published as `mvt1-cNN.mp3`, `mvt2-cNN.mp3`, `scherzo-cNN.mp3`, `mvt3-cNN.mp3` (mvt3 is the finale).
- Tab "Basic MIDI": plain General MIDI playback of each movement's current `score.midi` (Dan, 2026-11-09: no r07 renderer here, "super basic plain general midi samples"). Published as `basic/<movement>-<version>-gm.mp3`.
- Section "Volume shaping A/B (Movement I)" under the mockups list (added 2026-11-11 with mockup c56): four comparison clips from `symphony/mvt1/reaper-v621/cycles/c56/ab/`, published as `ab/mvt1-c56-<bars>-<mix|instrument>.mp3`. Each clip is c55 then c56. Its rows are `<li class="trk" data-set="ab" data-mvt="1" data-title="...">`; `data-title` is what the player shows instead of the movement title, and `data-mvt` picks the score shown. Rows of this set do not auto-advance. Remove or replace the section when a later comparison supersedes it.
- Section "Volume shaping, three states (Movement I)" after the A/B section (added 2026-11-11): eight clips from `symphony/mvt1/reaper-v621/cycles/c57/ab3/`, published as `ab3/<bars>-<mix|instrument>.mp3`. Each clip is c56, then per-note shapes off, then all per-note volume off, with 1 s of silence between; the start time of each state is in the row's meta line and `data-kind`. Rows use `data-set="ab3"`. The three caveats shown with it come from that folder's `README.txt`.
- Score viewer: the engraved score of each movement as page images, `scores/<movement>-<version>/01.webp ...`. One audio element plays everything, so the audio continues while the score is scrolled or the tab is switched.

## Updating

New mockup render: edit that movement's `<li class="trk" data-set="mockups">` row (`data-src`, `data-kind`, the cycle tag, Length from `ffprobe -show_entries format=duration`, Rendered from the file's mtime in CST). If it is Movement I, also edit the `<audio id="player" src>` and the player's first label, which start on that row. Publish with `files` = `{"<new>.mp3": {"from": "<absolute path>"}, "<old>.mp3": null}`.

New General MIDI render (when a score changes): `gm/render-gm.sh <score.midi> <out.mp3>` in a temporary folder, then edit the `data-set="basic"` row. It uses Apple's built-in GM set (DLSMusicDevice, gs_instruments.dls) through an offline Swift render; this Mac has no fluidsynth or soundfont. Nothing is added: no reverb, panning or balancing, one fixed gain to put the peak at -1 dBFS. Use a new published name when the audio changes (for example `basic/mvt2-v601-gm.mp3`) and remove the old one with `null`, so browsers do not play a cached copy.

Where the MIDI comes from: `score.midi` in `symphony/mvt2/v600`, `symphony/scherzo/v600` and `symphony/mvt3/v600` (finale). Movement I's `score.midi` is git-ignored and not on this Mac, so build it: copy `score.ly`, `global.ily`, `parts*.ily` and `sections/` from `symphony/mvt1/v621` to a temporary folder, run `convert-ly -e` on them (`--from=2.24.0` for the section files, which have no `\version`), then `lilypond -o score score.ly` (LilyPond 2.26, 8 seconds). `midi2events.py` gives each GM program its own channel, so the raw LilyPond file works.

New score engraving: `make-score-pages.sh <score.pdf> <dir>` in a temporary folder, publish the pages under a new folder name (`scores/mvt2-v600c/...`), set the old pages to `null`, and edit `dir`, `pages`, `version` and `note` in the `SCORES` table in the script at the bottom of `index.html`.

Files not named in a publish stay as they are. One publish takes at most 64 MB.

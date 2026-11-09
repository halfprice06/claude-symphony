# Listening page (mockups artifact)

Source of https://claude.ai/artifact/7V3Gt4wRG5NKRXEFgYchCd ("Symphony No. 1 Mockups"). `index.html` is hand-written; there is no build step. Always publish to that URL (pass it as `url`; a new conversation reads the artifact once first), so Dan's bookmark keeps working.

## What the page holds

- Tab "REAPER mockups": the newest mockup mp3 of each movement. Published as `mvt1-cNN.mp3`, `mvt2-cNN.mp3`, `scherzo-cNN.mp3`, `mvt3-cNN.mp3` (mvt3 is the finale).
- Tab "Basic renders": the r07 render of each movement's current score (`score-r07.mp3` in the version folder). Published as `basic/<movement>-<version>-r07.mp3`.
- Score viewer: the engraved score of each movement as page images, `scores/<movement>-<version>/01.webp ...`. One audio element plays everything, so the audio continues while the score is scrolled or the tab is switched.

## Updating

New mockup render: edit that movement's `<li class="trk" data-set="mockups">` row (`data-src`, `data-kind`, the cycle tag, Length from `ffprobe -show_entries format=duration`, Rendered from the file's mtime in CST). If it is Movement I, also edit the `<audio id="player" src>` and the player's first label, which start on that row. Publish with `files` = `{"<new>.mp3": {"from": "<absolute path>"}, "<old>.mp3": null}`.

New basic render: same, in the `data-set="basic"` row. Use a new published name when the audio changes (for example `basic/mvt2-v600b-r07.mp3`) and remove the old one with `null`, so browsers do not play a cached copy.

New score engraving: `make-score-pages.sh <score.pdf> <dir>` in a temporary folder, publish the pages under a new folder name (`scores/mvt2-v600b/...`), set the old pages to `null`, and edit `dir`, `pages`, `version` and `note` in the `SCORES` table in the script at the bottom of `index.html`.

Files not named in a publish stay as they are. One publish takes at most 64 MB.

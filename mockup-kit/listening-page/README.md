# Listening page (mockups artifact)

Source of https://claude.ai/artifact/7V3Gt4wRG5NKRXEFgYchCd ("Symphony No. 1 Mockups"). `index.html` is hand-written; there is no build step. Always publish to that URL (pass it as `url`; a new conversation reads the artifact once first), so Dan's bookmark keeps working.

## What the page holds

Dan, 2026-11-17: the page holds only the latest mockup of each of the four movements, the Basic MIDI tab and the scores. No A/B or comparison clips, no interim or alternate deliveries; when a new render arrives it replaces the old one and the old mp3 is removed with `null`.

- Tab "REAPER mockups": the newest mockup mp3 of each movement. Published as `mvt1-cNN.mp3`, `mvt2-cNN.mp3`, `scherzo-cNN.mp3`, `mvt3-cNN.mp3` (mvt3 is the finale).
- Tab "Basic MIDI": plain General MIDI playback of each movement's current `score.midi` (Dan, 2026-11-09: no r07 renderer here, "super basic plain general midi samples"). Published as `basic/<movement>-<version>-gm.mp3`.
- Tab "Score videos" (added 2026-11-23): the four glow score videos from `symphony/video/glow/<movement>-glow-video.mp4` (1080p, 195-303 MB each), set to the final mockups (I c63, II c57, III c30, IV c30). They play in the score column (the score pages hide while a video is open; the audio player pauses while a video plays, and the other way round). They ship as the page's own published files: 720p 60 fps HLS (Dan wanted 60 fps because text blurred in pans at 30), 20-second fMP4 pieces, 2-pass at 740 kbps video + 96 kbps AAC (about 160 MB for all four), under `videos/<movement>[-rN]/` with the playlist as `.../<movement>-playlist.txt` (artifacts do not serve `.m3u8`; hls.js 1.5.13 from cdnjs reads the playlist whatever its type). Posters: `videos/<movement>[-rN]-poster.jpg`, the frame at 12 s. When a video is replaced, publish it under the next folder name (`videos/mvt2-r2/`, then `-r3`), null the old folder and poster in the same publish, and update `data-hls`/`data-poster` on the row, so browsers never mix cached pieces of two renders. One movement per publish keeps the version under 256 MB. Encode with the script in this README's "Score videos" section below. Budget: a version may hold 256 MB in all and the page sits near 240 MB, so a higher video bitrate does not fit.
- Score viewer: the engraved score of each movement as page images, `scores/<movement>-<version>/01.webp ...`. One audio element plays everything, so the audio continues while the score is scrolled or the tab is switched.

## Updating

New mockup render: edit that movement's `<li class="trk" data-set="mockups">` row (`data-src`, `data-kind`, the cycle tag, Length from `ffprobe -show_entries format=duration`, Rendered from the file's mtime in CST). If it is Movement I, also edit the `<audio id="player" src>` and the player's first label, which start on that row. Publish with `files` = `{"<new>.mp3": {"from": "<absolute path>"}, "<old>.mp3": null}`.

New General MIDI render (when a score changes): `gm/render-gm.sh <score.midi> <out.mp3>` in a temporary folder, then edit the `data-set="basic"` row. It uses Apple's built-in GM set (DLSMusicDevice, gs_instruments.dls) through an offline Swift render; this Mac has no fluidsynth or soundfont. Nothing is added: no reverb, panning or balancing, one fixed gain to put the peak at -1 dBFS. Use a new published name when the audio changes (for example `basic/mvt2-v601-gm.mp3`) and remove the old one with `null`, so browsers do not play a cached copy.

Where the MIDI comes from: `score.midi` in `symphony/mvt2/v600`, `symphony/scherzo/v600` and `symphony/mvt3/v600` (finale). Movement I's `score.midi` is git-ignored and not on this Mac, so build it: copy `score.ly`, `global.ily`, `parts*.ily` and `sections/` from `symphony/mvt1/v621` to a temporary folder, run `convert-ly -e` on them (`--from=2.24.0` for the section files, which have no `\version`), then `lilypond -o score score.ly` (LilyPond 2.26, 8 seconds). `midi2events.py` gives each GM program its own channel, so the raw LilyPond file works.

New score engraving: `make-score-pages.sh <score.pdf> <dir>` in a temporary folder, publish the pages under a new folder name (`scores/mvt2-v600c/...`), set the old pages to `null`, and edit `dir`, `pages`, `version` and `note` in the `SCORES` table in the script at the bottom of `index.html`.

Files not named in a publish stay as they are. One publish takes at most 64 MB.


## Score videos

Encode (from the repo root; output folder is listed in `.git/info/exclude`):

```bash
V="-vf scale=1280:720 -c:v libx264 -preset slow -b:v 740k -maxrate 1150k -bufsize 2300k -profile:v high -pix_fmt yuv420p -g 120 -keyint_min 120 -sc_threshold 0"
ffmpeg -i in.mp4 $V -pass 1 -passlogfile /tmp/pM -an -f null /dev/null
ffmpeg -i in.mp4 $V -pass 2 -passlogfile /tmp/pM -c:a aac -b:a 96k -ac 2 -f hls -hls_time 20 -hls_playlist_type vod -hls_segment_type fmp4 \
  -hls_fmp4_init_filename M-init.mp4 -hls_segment_filename "out/M/M-%03d.mp4" out/M/M-playlist.txt
```

Keep a separate `-passlogfile` per movement when encoding several at once (all four in parallel take about 3 minutes on this Mac). Check that the four together stay under about 170 MB: the rest of the page is about 77 MB.

Publish each movement's folder as `videos/M/...` (one publish takes at most 64 MB). The artifact's asset store (1 GB, 20 MB per file) was tried first with full-quality pieces: the page got 404 for every `/_blob/` fetch and video load when viewed signed out, so those 82 assets (620 MB) are unused; they can be deleted.

#!/bin/bash
# Rebuild the movement II score video from the repo:
#   score  symphony/mvt2/v77                      (the version the REAPER mockup was built from)
#   audio  symphony/mvt2/reaper-export/mvt2-mockup-c26.mp3
#   tempo  symphony/mvt2/reaper-export/parts.json (the tempo map REAPER played)
# Output: symphony/video/mvt2/mvt2-score-video.mp4 (not committed; about 10 min on 4 cores)
# Needs: lilypond 2.24, ffmpeg, python3 with pillow, numpy, mido.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
SCORE="${SCORE:-$ROOT/symphony/mvt2/v77}"
EXPORT="${EXPORT:-$ROOT/symphony/mvt2/reaper-export}"
"$HERE/tools/build.sh" "$SCORE"
python3 "$HERE/tools/render_video.py" --build "$HERE/tools/build" \
  --tempo "$EXPORT/parts.json" --audio "$EXPORT/mvt2-mockup-c26.mp3" \
  --out "$HERE/mvt2-score-video.mp4" "$@"

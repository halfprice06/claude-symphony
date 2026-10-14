#!/bin/bash
# Rebuild the movement II glowing-score video from the repo:
#   score  symphony/mvt2/v77                      (the version the REAPER mockup was built from)
#   audio  symphony/mvt2/reaper-export/mvt2-mockup-c26.mp3
#   tempo  symphony/mvt2/reaper-export/parts.json (the tempo map REAPER played)
# Output: symphony/video/mvt2-glow/mvt2-glow-video.mp4 (not committed).
# Extra arguments go to glow_video.py, e.g. --bars 53 64 for an excerpt, --still 212 for test frames.
# Needs: lilypond 2.24, ffmpeg, python3 with numpy, pillow, opencv-python, cairosvg.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
SCORE="${SCORE:-$ROOT/symphony/mvt2/v77}"
EXPORT="${EXPORT:-$ROOT/symphony/mvt2/reaper-export}"
OUT="${OUT:-$HERE/mvt2-glow-video.mp4}"
[ -f "$HERE/build/strip2.png" ] || "$HERE/tools/build-strip.sh" "$SCORE" "$HERE/build"
python3 "$HERE/tools/glow_video.py" --strip "$HERE/build" \
  --tempo "$EXPORT/parts.json" --audio "$EXPORT/mvt2-mockup-c26.mp3" --out "$OUT" "$@"

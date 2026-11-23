#!/bin/bash
# make-glow-video.sh MOVEMENT AUDIO [glow_video.py arguments]
# Rebuild the glowing-score video of one movement from the repo:
#   MOVEMENT  mvt1 | mvt2 | scherzo | finale
#   AUDIO     the final mockup mp3 (mvt1-mockup-c63.mp3, mvt2-mockup-c57.mp3, scherzo-mockup-c30.mp3, mvt3-mockup-c30.mp3)
#   score     main's version folder (below); tempo map and stem loudness of that mockup in data/
# Output: symphony/video/glow/<MOVEMENT>-glow-video.mp4 (or OUT=; not committed). JOBS= parallel parts (default: all cores).
# Extra arguments go to glow_video.py, e.g. --bars 53 64 for an excerpt, --still 212 for test frames.
# Needs: lilypond 2.24, ffmpeg, python3 with numpy, pillow, opencv-python, cairosvg.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
M="$1"; AUDIO="$2"; shift 2
case "$M" in
  mvt1)    SCORE=symphony/mvt1/v621;    DATA=mvt1-c63 ;;
  mvt2)    SCORE=symphony/mvt2/v600;    DATA=mvt2-c57 ;;
  scherzo) SCORE=symphony/scherzo/v600; DATA=scherzo-c30 ;;
  finale)  SCORE=symphony/mvt3/v600;    DATA=finale-c30 ;;
  *) echo "usage: $0 mvt1|mvt2|scherzo|finale AUDIO.mp3 [glow_video.py args]"; exit 1 ;;
esac
BUILD="$HERE/build/$M"
OUT="${OUT:-$HERE/$M-glow-video.mp4}"
[ -f "$BUILD/strip2.png" ] || "$HERE/tools/build-strip.sh" "$ROOT/$SCORE" "$BUILD"
python3 "$HERE/tools/glow_video.py" --strip "$BUILD" --tempo "$HERE/data/$DATA-tempo.json" --stems "$HERE/data/$DATA-stems.npz" \
  --audio "$AUDIO" --out "$OUT" --jobs "${JOBS:-$(nproc)}" "$@"

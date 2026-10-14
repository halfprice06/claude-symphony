#!/bin/bash
# build-strip.sh SCORE_DIR OUT_DIR : engrave the whole movement on one long line as SVG,
# then render the PNG (14264 px wide) from that same SVG (cairosvg) so note positions and pixels match exactly.
set -e
TOOLS="$(cd "$(dirname "$0")" && pwd)"
SRC="$(cd "$1" && pwd)"; OUT="$2"
rm -rf "$OUT" && mkdir -p "$OUT"
cp -r "$SRC"/sections "$SRC"/parts.ily "$SRC"/sections.txt "$OUT"/
# v77's intro.ily tie callback fails when the notehead has no event cause; make it tolerate that
python3 - "$OUT/sections/intro.ily" <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
s = s.replace("(p (ly:event-property (event-cause nh) 'pitch))", "(ev (event-cause nh)) (p (if ev (ly:event-property ev 'pitch) #f))")
open(p, 'w').write(s)
PY
python3 "$TOOLS/make_strip_ly.py" "$SRC" "$OUT"
sed -i 's/\\RemoveEmptyStaves//' "$OUT/video.ly"
cd "$OUT"
lilypond -dbackend=svg -dno-point-and-click -o strip video.ly > svg.log 2>&1
python3 -c "import cairosvg; cairosvg.svg2png(url='strip.svg', write_to='strip2.png', output_width=14264, background_color='white')"

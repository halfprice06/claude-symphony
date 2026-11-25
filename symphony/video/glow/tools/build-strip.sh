#!/bin/bash
# build-strip.sh SCORE_DIR OUT_DIR : engrave the whole movement on one long line as SVG (tools/make_strip_ly.py),
# then render the PNG from that same SVG (cairosvg) so note positions and pixels match exactly.
set -e
TOOLS="$(cd "$(dirname "$0")" && pwd)"
SRC="$(cd "$1" && pwd)"; OUT="$2"
rm -rf "$OUT" && mkdir -p "$OUT"
# the score and everything it includes (sources only, no PDFs, audio or MIDI)
(cd "$SRC" && find . -maxdepth 2 \( -name '*.ly' -o -name '*.ily' -o -name 'sections.txt' \) -print0 | xargs -0 cp --parents -t "$OUT")
python3 "$TOOLS/make_strip_ly.py" "$OUT"
cd "$OUT"
lilypond -dbackend=svg -dno-point-and-click -o strip strip.ly > svg.log 2>&1 || { tail -30 svg.log; exit 1; }
python3 "$TOOLS/svg_to_png.py" strip.svg strip2.png

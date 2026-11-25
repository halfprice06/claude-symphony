#!/bin/sh
# Render a score PDF to the page images the listening page shows.
# Usage: make-score-pages.sh <score.pdf> <out-dir>
# Writes <out-dir>/01.webp, 02.webp, ... (200 dpi, grey, lossless; an A3 page is 2339 x 3308 px, about 100 KB).
# Needs pdftoppm (poppler) and cwebp.
set -e
pdf=$1
out=$2
[ -f "$pdf" ] && [ -n "$out" ] || { echo "usage: $0 <score.pdf> <out-dir>" >&2; exit 2; }
mkdir -p "$out"
tmp=$(mktemp -d)
pdftoppm -r 200 -gray -png "$pdf" "$tmp/p"
i=0
for f in $(ls "$tmp"/p-*.png | sort); do
  i=$((i + 1))
  cwebp -quiet -lossless -z 7 "$f" -o "$out/$(printf '%02d' $i).webp"
done
rm -r "$tmp"
echo "$i pages in $out"

#!/bin/bash
# c075: build the scherzo's instrumental parts (one PDF per player) next to score.ly, as movement I does (mvt1 build-parts.sh, c185).
# Run build.sh first (it regenerates parts.ily). Usage: bash build-parts.sh [version-dir] -> <version-dir>/partsout/parts-NN-<instrument>.pdf
# PARTS_AUDIT=1 adds a proofreading log in parts.log (entries after rests without a dynamic, entries after 8+ whole notes' rest, notes with 4+ ledger lines).
set -u
V="${1:-$(cd "$(dirname "$0")" && pwd)}"; cd "$V" || exit 1
python3 -I parts-gen.py parts.ly
mkdir -p partsout
lilypond -dno-point-and-click -o partsout/parts parts.ly > parts.log 2>&1; rc=$?
echo "parts: lilypond rc=$rc, warnings/errors: $(grep -cE 'warning|error' parts.log)"
for f in partsout/*.pdf; do echo "  $(basename "$f"): $(pdfinfo "$f" | awk '/Pages/{print $2}') p."; done

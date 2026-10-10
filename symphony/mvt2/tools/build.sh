#!/bin/bash
# Usage: build.sh <version-dir> [main.ly]
# Compiles the score to PDF + MIDI, renders audio with FluidSynth, runs analysis.
set -u
TOOLS="$(cd "$(dirname "$0")" && pwd)"; V="$1"; MAIN="${2:-mvt1.ly}"
cd "$V" || exit 1
base="${MAIN%.ly}"
[ -d sections ] && python3 -I "$TOOLS/assemble.py" . > /dev/null
lilypond -dno-point-and-click -o "$base" "$MAIN" > build.log 2>&1
rc=$?
grep -E "warning|error" build.log | grep -v "MIDI channel wrapped\|remapping modulo\|channels beyond" > build-warnings.txt
echo "lilypond rc=$rc, warnings/errors: $(wc -l < build-warnings.txt)"
MID=$(ls "$base".mid* 2>/dev/null | head -1)
if [ -n "$MID" ]; then
  python3 -I "$TOOLS/fixmidi.py" "$MID" > /dev/null || echo "fixmidi failed"
  fluidsynth -ni -g 0.6 -r 44100 -F "$base.wav" /usr/share/sounds/sf2/FluidR3_GM.sf2 "$MID" > /dev/null 2>&1
  ffmpeg -y -loglevel error -i "$base.wav" -af "loudnorm=I=-20:TP=-2" -b:a 192k "$base.mp3" && rm -f "$base.wav"
  echo "audio: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$base.mp3")s"
  python3 -I "$TOOLS/analyze.py" "$MID" > analysis.txt 2>&1; head -c 3000 analysis.txt
fi

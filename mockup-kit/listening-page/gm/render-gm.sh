#!/bin/sh
# Plain General MIDI render of a LilyPond score.midi: Apple's built-in GM sound set, no reverb, no panning,
# no balancing. The only processing is one fixed gain so the loudest peak sits at -1 dBFS.
# Usage: render-gm.sh <score.midi> <out.mp3> [work-dir]
# Needs swiftc, python3 and ffmpeg. Takes a few seconds per movement and plays nothing aloud.
set -e
here=$(cd "$(dirname "$0")" && pwd)
mid=$1; out=$2; work=${3:-$(mktemp -d)}
mkdir -p "$work"
[ -x "$work/gmrender" ] || swiftc -O "$here/gmrender.swift" -o "$work/gmrender"
python3 "$here/midi2events.py" "$mid" "$work/events.txt"
"$work/gmrender" "$work/events.txt" "$work/gm.wav" 2>/dev/null
peak=$(ffmpeg -hide_banner -nostats -i "$work/gm.wav" -af ebur128=peak=true -f null - 2>&1 | awk '/Peak:/ {p=$2} END {print p}')
gain=$(python3 -c "print(round(-1.0 - float('$peak'), 2))")
ffmpeg -y -loglevel error -i "$work/gm.wav" -af "volume=${gain}dB" -c:a libmp3lame -b:a 192k "$out"
rm "$work/gm.wav" "$work/events.txt"
echo "$out: peak was $peak dBFS, gain $gain dB, $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out") s"

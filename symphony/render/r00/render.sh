#!/bin/bash
# Baseline renderer (= mvt1/tools/build.sh audio step, v120)
# Usage: render.sh <in.midi> <out.mp3>
set -e
fluidsynth -ni -g 0.6 -r 44100 -F /tmp/r00.wav /usr/share/sounds/sf2/FluidR3_GM.sf2 "$1" > /dev/null 2>&1
ffmpeg -y -loglevel error -i /tmp/r00.wav -af "loudnorm=I=-20:TP=-2" -b:a 192k "$2"

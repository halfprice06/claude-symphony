#!/bin/bash
# build.sh SRC_VERSION_DIR : engrave the video score into build/ and parse its layout
set -e
cd "$(dirname "$0")"
rm -rf build && mkdir build
cp -r "$1"/sections "$1"/parts.ily build/; cp "$1"/sections.txt build/
python3 - <<'PY'
p='build/sections/intro.ily'; s=open(p).read()
s=s.replace("(p (ly:event-property (event-cause nh) 'pitch))","(ev (event-cause nh)) (p (if ev (ly:event-property ev 'pitch) #f))"); open(p,'w').write(s)
PY
python3 make_video_ly.py "$1" build
cd build
lilypond -dbackend=svg -dno-point-and-click -o video video.ly > svg.log 2>&1
lilypond --png -dresolution=305 -dno-point-and-click -o video video.ly > png.log 2>&1
cd .. && python3 parse_layout.py build

#!/bin/bash
# usage: meas.sh TAG MP3 MIDI   -> /tmp/render-02/meas/TAG
set -e
T=/mnt/project-files/symphony/render/tools; O=/tmp/render-02/meas/$1; mkdir -p $O
cd /tmp
python3 $T/score_events.py --midi $3 --events /tmp/render-02/build/ly_scratch/events.tsv --out $O/notes.csv --summary $O/articulation_midi.json > /dev/null
python3 $T/measure.py $2 --midi $3 --out $O/mix > $O/measure.log 2>&1
python3 $T/stems.py --midi $3 --notes $O/notes.csv --out $O/stems --work /tmp/render-02/stemwork --render "python3 /mnt/project-files/symphony/render/r02/stem.py {midi} {wav}" > $O/stems.log 2>&1
python3 /mnt/project-files/symphony/render/critics/c01/scripts/melody.py $O/stems/stem_bars.csv $O/notes.csv > $O/melody.md
echo done $1

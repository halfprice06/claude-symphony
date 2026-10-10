#!/bin/bash
# critic 3 copy of r03/meas/scripts/meas.sh (measures one r03 render): meas.sh WORK MP3 OUTDIR LABEL
# WORK = render.py --work folder (stems, notes.csv, render.midi, events), OUTDIR gets every table.
# Uses tools/ (critic 0) and critic 2's scripts (critics/c02/scripts), the same measures as critics/c02.md.
set -e
W=$1; MP3=$2; O=$3; L=$4
R=/mnt/project-files/symphony/render; S=$R/critics/c02/scripts
mkdir -p $O
[ -f $O/mix/metrics.json ] || python3 $R/tools/measure.py $MP3 --midi $W/render.midi --out $O/mix > $O/measure.log 2>&1
[ -f $O/stems/stems_summary.json ] || python3 $R/tools/stems.py --midi $W/render.midi --notes $W/notes.csv --out $O/stems --work $W/stems --reuse --keep-wav \
   --render "python3 $R/r03/stem.py {midi} {wav}" > $O/stems.log 2>&1
python3 $S/barlev.py $W/stems $O/mix/bars.csv $O/bar_levels_whole_bar.csv
python3 $S/bardyn.py $L $O/mix/bars.csv $W/notes.csv > $O/bardyn.txt
python3 $S/melody2.py $W/ly_scratch/events.tsv $W/notes.csv $O/stems/stem_bars.csv $W/render.midi $R/r03/config.json > $O/melody.md
python3 $S/rolls2.py $W/notes.csv $O/mix/bars.csv $O/bar_levels_whole_bar.csv $W/stems/Timpani.wav $L > $O/rolls.txt 2>&1 || true
python3 $S/stemcmp.py $L $O/stems/stems_summary.json $O/stems/stem_bars.csv > $O/stemcmp.md
python3 $S/lowstem.py $W/stems > $O/lowstem.txt
python3 $S/clicks2.py $W/mix_prem.wav > $O/clicks_premaster.txt
python3 $S/staccmp.py $W/notes.csv $W/stems $L > $O/staccmp.txt
python3 $S/tremmod2.py $W/notes.csv $W/stems $L > $O/tremmod.txt
cp $W/render_report.json $W/balance_report.json $W/articulate_report.json $O/ 2>/dev/null || true
echo done $L

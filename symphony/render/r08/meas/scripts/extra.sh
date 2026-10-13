#!/bin/bash
# r07: measures beyond meas.sh, on one render: extra.sh WORK OUTDIR LABEL (after meas.sh wrote OUTDIR)
W=$1; O=$2; L=$3; R=/mnt/project-files/symphony/render
python3 $R/critics/c06/scripts/accents2.py $W $L wet > $O/accents2-wet.txt 2>&1 || true
python3 $R/r08/meas/scripts/rollcheck.py $W > $O/rollcheck.txt 2>&1 || true
python3 $R/critics/c06/scripts/rollchains.py $W > $O/rollchains.txt 2>&1 || true
python3 $R/critics/c05/scripts/inv_by_stem.py $O/stems/stem_bars.csv $L > $O/inv_by_stem.txt 2>&1 || true
python3 $R/r05/meas/scripts/inv_nohp.py $O/stems/stem_bars.csv $W/notes.csv $L > $O/nohp.txt 2>&1 || true
for s in Horns_12 Horns_34 Trumpets_12 Trombones_12 Tuba Cor_anglais Contrabassoon; do
  [ -f $W/stems/${s}_syn.wav ] || [ ! -f $W/stems/$s.mid ] || python3 $R/r08/stem.py $W/stems/$s.mid /tmp/r08x_dry_$$.wav --dry --synth-out $W/stems/${s}_syn.wav > /dev/null 2>&1
done; rm -f /tmp/r08x_dry_$$.wav
python3 $R/critics/c05/scripts/pitchcheck.py $W Horns_12 Horns_34 Trumpets_12 Trombones_12 Tuba Cor_anglais Contrabassoon > $O/pitch.txt 2>&1 || true
bash $R/r08/meas/scripts/summ.sh $O $W $L > $O/summary.txt 2>&1 || true
echo extra done $L

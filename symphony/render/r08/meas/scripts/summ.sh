#!/bin/bash
# r07: key numbers of one measured render: summ.sh MEAS_DIR WORK LABEL (MEAS_DIR from meas.sh; WORK = render --work)
O=$1; W=$2; L=$3; R=/mnt/project-files/symphony/render
python3 - "$O" <<'PY'
import json, sys
m = json.load(open(sys.argv[1] + "/mix/metrics.json"))
e = m["ffmpeg_ebur128"]; s = m["loudness"]["S_percentiles_rel_I"]
print(f"I {e['I_LUFS']} LRA {e['LRA_LU']} TP {e['true_peak_dBTP']} | S p10 {s['p10']} p50 {s['p50']} p95 {s['p95']} max {m['loudness']['S_max_rel_I']}")
PY
sed -n 1,4p $O/bardyn.txt
grep "balance inversions" $O/stemcmp.md | cut -c1-60
python3 $R/r05/meas/scripts/inv_nohp.py $O/stems/stem_bars.csv $W/notes.csv $L 2>/dev/null | head -3
tail -1 $O/melody_nt.txt
python3 $R/r08/meas/scripts/rollcheck.py $W | tail -1

#!/bin/bash
# r05 (copy of critic 4 generality.sh): run r05's score stages (score_events, articulate, marks) on a score version without rendering audio.
# Usage: generality.sh SCOREDIR WORK
set -e
R=/mnt/project-files/symphony/render/r05; S=$1; W=$2; mkdir -p $W
cp $S/score.midi $W/score.midi
python3 $R/lib/score_events.py --midi $W/score.midi --out $W/notes.csv --ly-dir $S --scratch $W/ly_scratch --summary $W/am.json > /dev/null
python3 $R/articulate.py $W/score.midi $W/notes.csv $R/config.json $W/render.midi --report $W/ar.json --score $S | tail -1
python3 - $W <<'PY'
import sys, os, csv, json, re
sys.path.insert(0, "/mnt/project-files/symphony/render/r05/lib"); import marks, rtk, staffmap
W = sys.argv[1]; mi = rtk.midi_info(os.path.join(W, "score.midi"))
rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
mel = marks.melodies(os.path.join(W, "ly_scratch", "events.tsv"), rows, mi["bar_s"], tpb=mi["tpb"])
rl = marks.rolls(rows, mi["bar_s"])
cfg = json.load(open("/mnt/project-files/symphony/render/r05/config.json"))
staves = sorted(set(r["staff"] for r in rows))
print("bars", len(mi["bar_s"]) - 1, "notes", len(rows), "melodies", len(mel), "rolls", len(rl), [(b[0], b[-1], d) for _, _, b, d, _ in rl])
print("staves without own config entry:", [s for s in staves if re.sub(r"[^A-Za-z0-9 ]", "", s).strip() not in cfg["stems"]])
ar = json.load(open(os.path.join(W, "ar.json"))); print("unmatched", ar.get("stats", ar).get("unmatched"))
PY

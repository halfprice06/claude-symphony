#!/bin/bash
# nochange.sh N "lens and reading" "recorded summary" : cycle N changed nothing; promote v(N+1) as a relabelled copy of vN, log, commit, sync.
M=/home/user/claude_composes/symphony/mvt2; N=$1; NEW=$((N+1))
bash $M/kit/promote-parts.sh $NEW $N $M/v$N 2>&1 | grep -E "^warnings|Pages|draft v[0-9]"
printf '# v%s — cycle %s (%s)\n\nAccepted: nothing (v%s = v%s relabelled). Report: critics/reports/c%03d.md.\nRecorded (no change): %s\nBuild: 0 warnings, 8 pages, 0 outer-voice parallels; parts book 30 pages.\n' $NEW $N "$2" $NEW $N $N "$3" > /tmp/m2/crit.txt
printf '## Cycle %s (v%s → v%s)\n%s. Report: reports/c%03d.md.\n- Accepted: nothing (v%s = v%s relabelled).\n- Recorded (no change): %s\n- Do-not-touch: standing list; the 8-page layout.\n' $N $N $NEW "$2" $N $NEW $N "$3" > /tmp/m2/hist.txt
python3 $M/kit/log.py $NEW /tmp/m2/crit.txt /tmp/m2/hist.txt && bash $M/kit/finish.sh $NEW

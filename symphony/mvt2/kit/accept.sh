#!/bin/bash
# accept.sh N SRC CRIT_FILE HIST_FILE : cycle N accepted changes from SRC; prompt for N+1, promote v(N+1) with parts, log, commit, push.
M=/home/user/claude_composes/symphony/mvt2; N=$1; NEW=$((N+1))
bash $M/kit/genprompt.sh $NEW "" >/dev/null
bash $M/kit/promote-parts.sh $NEW $N $2 2>&1 | grep -E "^warnings|^Outer|Pages|parts:"
python3 $M/kit/log.py $NEW $3 $4 && bash $M/kit/finish.sh $NEW | tail -1
cd /home/user/claude_composes && git push -q origin claude/project-thread-sgcp3g 2>&1 | tail -1; git status --short | head -3

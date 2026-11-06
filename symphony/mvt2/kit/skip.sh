#!/bin/bash
# skip.sh N "lens and reading" "recorded summary" : genprompt N+1, nochange.sh, push.
M=/home/user/claude_composes/symphony/mvt2; N=$1
bash $M/kit/genprompt.sh $((N+1)) "" >/dev/null
bash $M/kit/nochange.sh "$@" 2>&1 | grep -E "^warnings|Pages|parts:|logged|Movement II cycle"
cd /home/user/claude_composes && git push -q origin claude/project-thread-sgcp3g 2>&1 | tail -1; git status --short | head -3

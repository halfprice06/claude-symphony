#!/bin/bash
# cycle-done.sh N SRC "applied" "open" "do-not-touch" "cross" : promote v(N+1) from SRC, log cycle N, write the next prompt, commit and push.
set -e
M=/home/user/claude_composes/symphony/mvt1; N=$1; SRC=$2; NEW=$((N+1))
if [ ! -d "$SRC" ]; then rm -rf /tmp/src$N && cp -r $M/v$N /tmp/src$N && rm -rf /tmp/src$N/partsout; SRC=/tmp/src$N; fi
bash $M/kit/promote.sh $NEW $N $SRC 2>&1 | grep -E "warnings|Pages|^[<>]|FAILED" || true
rm -f $M/v$N/score.mp3
bash $M/kit/log.sh $N "$3" "$4" "$5" "$6"
bash $M/kit/genprompt.sh $NEW
cd /home/user/claude_composes && git add -A symphony/mvt1 && git commit -qm "Movement I series 3: cycle $N (v$NEW)

Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_018HrEPSmMSqb3YkeMbTtpwH" && git push -q origin claude/project-thread-ytvxdy 2>&1 | tail -1
uptime

#!/bin/bash
# cyc.sh N "critique" "history" ["focus"] : next.sh with the fifth-run focus by default, short summary, commit (fifth run helper).
M=/home/user/claude_composes/symphony/scherzo; N=$1; F="${4:-$(cat $M/kit/focus-fifth.txt)}"
bash $M/kit/next.sh $N "$2" "$3" "$F" 2>&1 | grep -E "warnings|Pages|theme|C-major|part|Your|CHANGED|MOVED|THEMES"
cd /home/user/claude_composes && git add -A symphony && git commit -qm "Scherzo cycle $N (v$((N+1)))

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014b4HENepxQGh2bXjJ3GenA" && echo committed

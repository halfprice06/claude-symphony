#!/bin/bash
# finish.sh NEW : after promote and logging, commit vNEW to git (source, MIDI, latest PDFs only), and refresh the shared-folder copy
# (/mnt/project-files/symphony/mvt2/latest/ text files + CHECKPOINT.md). Third series, 2026-10-19.
set -e
R=/home/user/claude_composes; M=$R/symphony/mvt2; S=/mnt/project-files/symphony/mvt2
NEW=$1; PREV=$((NEW-1)); cd $R
rm -f $M/v$PREV/score.mp3
[ $PREV -gt 201 ] && git rm -q --cached --ignore-unmatch symphony/mvt2/v$PREV/score.pdf symphony/mvt2/v$PREV/parts-book.pdf || true
git add -- "symphony/mvt2/v$NEW" ':!symphony/mvt2/v'$NEW'/*.mp3' symphony/mvt2/critics symphony/mvt2/kit symphony/mvt2/README.md
git commit -q -m "Movement II cycle $PREV: v$PREV -> v$NEW" -m "Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01WWGdo2VND72g1pVzSE2829"
# shared-folder copy (best effort; the mount can fail)
if timeout 60 ls $S >/dev/null 2>&1; then
  mkdir -p $S/latest/sections
  for f in global.ily score.ly parts.ily score-defs.ily parts-book.ly genparts.py sections.txt critique.md analysis.txt; do cp $M/v$NEW/$f $S/latest/$f; done
  cp $M/v$NEW/sections/*.ily $S/latest/sections/
  cat > $S/CHECKPOINT.md <<EOT
# Movement II checkpoint (third series, cycles 201-400)

Updated $(date -u '+%Y-%m-%d %H:%M UTC'). Latest version: v$NEW (cycle $PREV done).
The versions live in the git checkout of the thread "Movement II, 200 more loops" and are pushed to branch claude/project-thread-wtf58k of halfprice06/claude_composes every 10 cycles.
latest/ holds the text files of v$NEW (build with symphony/mvt2/tools/build.sh after copying in the rest of a version folder).
Log: critics/HISTORY.md on that branch; critique.md in latest/.
EOT
  echo "shared copy ok"
else echo "SHARED FOLDER UNREACHABLE"; fi
git log --oneline -1

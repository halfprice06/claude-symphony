#!/bin/bash
# checkpoint.sh V : after promoting vV, copy its text sources to the shared folder (replacing the previous checkpoint), update CHECKPOINT.md, force-add score.pdf, commit, push.
set -e
M=/home/user/claude_composes/symphony/mvt1; V=$1; S=/mnt/project-files/symphony/mvt1
OLD=$(ls -d $S/v[34][0-9][0-9] 2>/dev/null | grep -v "/v$V$" || true)
rm -rf $S/v$V.new && mkdir $S/v$V.new && cp -r $M/v$V/{analysis.txt,build-parts.sh,critique.md,full.ly,global.ily,parts-gen.py,score.ly,sections,sections.txt,vl.txt} $M/v$V/parts*.ily $S/v$V.new/ && rm -rf $S/v$V && mv $S/v$V.new $S/v$V
[ -n "$OLD" ] && rm -rf $OLD
sed -i "s/^- Latest: v[0-9]*.*/- Latest: v$V (cycle $((V-1)) done, $(date -u +%Y-%m-%d\ %H:%M) UTC). Cycles 321–420 → v421 (Dan 2026-10-25: \"another 100 loops\"); release check at 420./" $M/CHECKPOINT.md
cp $M/CHECKPOINT.md $S/CHECKPOINT.md
cd /home/user/claude_composes && git add -f symphony/mvt1/v$V/score.pdf && git add -A symphony && git commit -qm "Movement I series 3: v$V checkpoint

Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_018HrEPSmMSqb3YkeMbTtpwH" && git push -q origin claude/project-thread-ytvxdy 2>&1 | tail -1
git log --oneline -1

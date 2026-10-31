#!/bin/bash
# finish.sh N "heading" FILE : cycle N done (vN -> vN+1). FILE holds the critique body (also appended to HISTORY under the heading).
# Writes v(N+1)/critique.md, appends to critics/HISTORY.md, deletes scratch, commits, mirrors the latest text files to /mnt/project-files.
set -e
M=/home/user/claude_composes/symphony/mvt3; N=$1; H="$2"; F=$3; NX=$((N+1)); NNN=$(printf %03d $N)
{ echo "# v$NX (cycle $N, $H)"; echo; echo "Report: critics/reports/c$NNN.md."; cat $F; echo; echo "Build: $(wc -c < $M/v$NX/build-warnings.txt) warnings, $(grep -o 'similar motion): [0-9]*' $M/v$NX/analysis.txt | grep -o '[0-9]*$') parallels, $(pdfinfo $M/v$NX/score.pdf | awk '/Pages/{print $2}') pages, $(python3 /home/user/claude_composes/symphony/coherence/themecheck.py /home/user/claude_composes/symphony/coherence/themes-finale-quotes.ly $M/v$NX --beats 4 | tail -1)."; } > $M/v$NX/critique.md
{ echo; echo "## Cycle $N (v$N → v$NX), $H"; grep '^- ' $F; } >> $M/critics/HISTORY.md
rm -rf /tmp/critic-$N /tmp/m3/v$N
cd /home/user/claude_composes && git add -A symphony/mvt3 symphony/coherence/finale.md symphony/coherence/themes-finale-quotes.ly && git commit -qm "Finale cycle $N: v$NX ($H)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014b4HEMpCkCv9WRxyrrFKba"
git push -q origin claude/project-thread-gvpxu4 2>&1 | tail -1 || true
P=/mnt/project-files/symphony/coherence
if timeout 60 ls /mnt/project-files/ >/dev/null 2>&1; then
  mkdir -p $P && cp /home/user/claude_composes/symphony/coherence/finale.md /home/user/claude_composes/symphony/coherence/themes-finale-quotes.ly $P/ && echo "mirrored finale.md"
else echo "MOUNT I/O PROBLEM"; fi
echo "uptime h: $(awk '{printf "%.1f", $1/3600}' /proc/uptime)"

#!/bin/bash
# log.sh N "applied" "not applied / open" "do-not-touch" "cross-movement" : writes v(N+1)/critique.md and appends to critics/HISTORY.md
M=/home/user/claude_composes/symphony/mvt1; N=$1; NEW=$((N+1)); K=$(( (N-1)%10 + 1 ))
LENS=$(sed -n "$((K+1))p" $M/critics/LENSES3.md | sed "s/^$K\. //" | cut -d: -f1)
RD=$(grep "^| $N |" $M/critics/READING3.md | awk -F' \\| ' '{print $3}' | sed 's/ |$//')
B="warnings $(wc -c < $M/v$NEW/build-warnings.txt), $(pdfinfo $M/v$NEW/score.pdf | awk '/Pages/{print $2}') PDF pages, parallels: $(grep -A1 '^Outer' $M/v$NEW/analysis.txt | tail -1 | sed 's/^ *//')"
cat > $M/v$NEW/critique.md <<EOT
# v$NEW — critic $N ($LENS)

Reading: $RD
Report: critics/reports/c$N.md

Applied: $2

Not applied / open: $3

Do not touch: $4

Cross-movement effects: $5

Build: $B
EOT
cat >> $M/critics/HISTORY.md <<EOT

## Cycle $N ($LENS; $RD) → v$NEW
- Accepted: $2
- Open / not applied: $3
- Do-not-touch: $4
- Cross-movement: $5
EOT
echo logged c$N

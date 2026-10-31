#!/bin/bash
# Fourth-series cycle helper (cycles 400-599, v400 -> v600).
#   go4.sh prompt N          writes pN.txt with the standard focus for cycle N and prints the agent instruction
#   go4.sh done N "heading" NOTES   promotes /tmp/critic-N/work (or an unchanged copy of vN if absent) to v(N+1),
#                            adds NOTES' "- " lines to coherence/finale.md's running list, then runs finish.sh
set -e
KIT=/home/user/claude_composes/symphony/mvt3/kit; M=/home/user/claude_composes/symphony/mvt3; CO=/home/user/claude_composes/symphony/coherence
cmd=$1; N=$2; K=$(( (N-1)%10 + 1 ))
if [ "$cmd" = prompt ]; then
  F=""
  [ $K -eq 9 ] && F="v$((N-10)) has no score.pdf; build it in your scratch area (copy v$((N-10)) to /tmp/critic-$N/v$((N-10)) and run the build there) if you need to view its pages."
  [ $K -eq 10 ] && F="Cyclic review. The sibling movements' current coherence files are in /home/user/claude_composes/symphony/coherence/ (movement II's records themes-mvt2.ly and themes-mvt2-b.ly are there too). Check every quotation at pitch against them and give corrected wording for any stale sentence in coherence/finale.md (list it in your report; do not edit the file)."
  [ $N -eq 599 ] && F="$F This is the last cycle of the series: v600 is the release version, so also do a release check (no leftover draft markings, title 'IV. Finale', subtitle with the version and date, parts consistent with the score)."
  bash $KIT/genprompt.sh $N "$F"
  echo "AGENT: Read your full task from $KIT/p$N.txt and carry it out exactly. Do not call any mcp__hearthbot tools and do not message anyone; write only your report file and your scratch copy under /tmp/critic-$N. Do not run git commands."
elif [ "$cmd" = done ]; then
  H="$3"; NOTES=$4; NX=$((N+1))
  SRC=/tmp/critic-$N/work; [ -d $SRC ] || { SRC=/tmp/critic-$N/unchanged; rm -rf $SRC; mkdir -p /tmp/critic-$N; cp -r $M/v$N $SRC; }
  bash $KIT/promote.sh $NX $N $SRC
  rm -rf $M/v$NX/parts
  python3 - "$CO/finale.md" "$NX" "$N" "$H" "$NOTES" <<'PY'
import sys,re,datetime
p,nx,n,h,notes=sys.argv[1:]
s=open(p).read()
lines=[l.rstrip() for l in open(notes) if l.startswith('- ')]
block=''.join(f'- v{nx} (cycle {n}, {h}): {l[2:]}\n' for l in lines) or f'- v{nx} (cycle {n}, {h}): no score change.\n'
hdr='## Changes in cycles 400– (v401–), running list\n\n'
i=s.index(hdr)+len(hdr)
j=s.index('\n## ',i)
s=s[:j].rstrip('\n')+'\n'+block+s[j:] if s[i:j].strip() else s[:i]+block+s[i:]
s=re.sub(r'Updated \d{4}-\d\d-\d\d for v\d+ \([^)]*\)', f'Updated {datetime.date.today()} for v{nx} (cycle {n}, {h})', s, count=1)
open(p,'w').write(s)
PY
  bash $KIT/finish.sh $N "$H" $NOTES
fi

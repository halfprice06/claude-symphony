#!/bin/bash
# siblings.sh N : before a lens-10 cycle N, copy the sibling movements' latest coherence files into the checkout (uncommitted)
# and extract their newest version folders to /tmp/siblings; appends the paths to pN.txt. Restore afterwards with siblings.sh restore.
R=/home/user/claude_composes; cd $R
if [ "$1" = restore ]; then git checkout symphony/coherence/scherzo.md symphony/coherence/themes-scherzo.md symphony/coherence/themes-scherzo.ly symphony/coherence/mvt1.md symphony/coherence/themes-mvt1.ly symphony/coherence/themes-mvt1.md symphony/coherence/mvt2.md symphony/coherence/themes-mvt2.ly symphony/coherence/themes-mvt2-b.ly; exit; fi
N=$1; git fetch -q origin
M1=origin/claude/project-thread-6v70nw; M2=origin/claude/project-thread-sgcp3g; SC=origin/claude/project-thread-kusasb
for f in mvt1.md themes-mvt1.ly themes-mvt1.md; do git show $M1:symphony/coherence/$f > symphony/coherence/$f; done
for f in mvt2.md themes-mvt2.ly themes-mvt2-b.ly; do git show $M2:symphony/coherence/$f > symphony/coherence/$f; done
for f in scherzo.md themes-scherzo.md themes-scherzo.ly; do git show $SC:symphony/coherence/$f > symphony/coherence/$f; done
rm -rf /tmp/siblings; mkdir -p /tmp/siblings; P=""
for spec in "$M1 symphony/mvt1" "$M2 symphony/mvt2" "$SC symphony/scherzo"; do set -- $spec
  v=$(git ls-tree -d --name-only $1 $2/ | grep -E '/v[0-9]+$' | sort -V | tail -1); git archive $1 $v | tar -x -C /tmp/siblings; P="$P /tmp/siblings/$v"; done
python3 - $R/symphony/mvt3/kit/p$N.txt "$P" <<'PY'
import sys
p,paths=sys.argv[1],sys.argv[2].split()
s=open(p).read()
s=s.replace("(list it in your report; do not edit the file).","(list it in your report; do not edit the file). The siblings' newest versions are extracted read-only at "+", ".join(paths)+"; run coherence/themecheck.py against those, not against the older versions in the checkout.",1)
open(p,'w').write(s)
PY
echo $P; git status --short | head

#!/bin/bash
# siblings.sh : fetch the other movements' fifth-run branches and archive their newest versions into /tmp/siblings/ (for lens-10 cyclic checks).
# Branches (2026-10-31): 6v70nw = movement I, sgcp3g = movement II, gvpxu4 = finale (symphony/mvt3).
cd /home/user/claude_composes
git fetch -q origin 'refs/heads/claude/project-thread-*:refs/remotes/origin/claude/project-thread-*'
rm -rf /tmp/siblings; mkdir -p /tmp/siblings/coherence
for pair in mvt1:6v70nw mvt2:sgcp3g mvt3:gvpxu4; do
  m=${pair%%:*}; b=origin/claude/project-thread-${pair##*:}
  v=$(git ls-tree --name-only $b symphony/$m/ | grep -E '/v[0-9]+$' | sed 's#.*/##' | sort -V | tail -1)
  mkdir -p /tmp/siblings/$m; git archive $b symphony/$m/$v | tar -x -C /tmp/siblings/$m --strip-components=2
  echo "$m $v ($b)"
done
for f in mvt1.md mvt2.md finale.md themes-mvt1.ly themes-mvt1.md themes-mvt2.ly themes-mvt2-b.ly themes-finale-quotes.ly; do
  for b in 6v70nw sgcp3g gvpxu4; do git show origin/claude/project-thread-$b:symphony/coherence/$f > /tmp/siblings/coherence/$f.$b 2>/dev/null || rm -f /tmp/siblings/coherence/$f.$b; done
done
ls /tmp/siblings/coherence | tr '\n' ' '

#!/bin/bash
# promote-parts.sh NEW PREV SRC : promote.sh, then regenerate the parts book in /tmp/m2/vNEW and copy it into vNEW.
M=/home/user/claude_composes/symphony/mvt2; NEW=$(printf %02d $1)
bash $M/kit/promote.sh "$@" && cd /tmp/m2/v$NEW && python3 genparts.py parts-book.ly > gp.log 2>&1 && lilypond -dno-point-and-click parts-book.ly > parts.log 2>&1
echo "parts: rc=$? warnings=$(grep -ci warning /tmp/m2/v$NEW/parts.log) $(pdfinfo /tmp/m2/v$NEW/parts-book.pdf | grep Pages)"
cp /tmp/m2/v$NEW/parts-book.ly /tmp/m2/v$NEW/parts-book.pdf $M/v$NEW/

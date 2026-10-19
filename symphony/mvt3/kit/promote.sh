#!/bin/bash
# promote.sh NEW PREV SRC : copy SRC (a critic scratch copy or the composer's edit) into mvt3/vNEW, bump the draft label, build in /tmp, copy back, summarise.
set -e
M=/home/user/claude_composes/symphony/mvt3
NEW=$(printf %02d $1); PREV=$(printf %02d $2); SRC=$3
W=/tmp/m3/v$NEW; rm -rf $W; mkdir -p $W
(cd $SRC && tar cf - --exclude='*.wav' --exclude='score-r0*.mp3' --exclude=build --exclude=probe --exclude=base --exclude='pg*' --exclude='*.png' .) | (cd $W && tar xf -)
sed -i -e "s/draft v$PREV\"/draft v$NEW\"/" $W/score.ly
bash $M/tools/build.sh $W score.ly >/dev/null 2>&1 || true
mkdir -p $M/v$NEW && (cd $W && tar cf - .) | (cd $M/v$NEW && tar xf -)
echo "warnings: $(wc -c < $M/v$NEW/build-warnings.txt)"; grep -A3 "^Outer" $M/v$NEW/analysis.txt; head -1 $M/v$NEW/analysis.txt; pdfinfo $M/v$NEW/score.pdf | grep Pages; grep -o "draft v[0-9]*" $M/v$NEW/score.ly
echo "scherzo quotations:"; python3 /home/user/claude_composes/symphony/coherence/themecheck.py /home/user/claude_composes/symphony/coherence/themes-finale-quotes.ly $M/v$NEW --beats 4 || echo "QUOTATION CHANGED: check against coherence/themes-scherzo.ly"

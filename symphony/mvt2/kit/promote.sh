#!/bin/bash
# promote.sh NEW PREV SRC : copy SRC (a critic scratch copy or the composer's edit) into mvt2/vNEW, bump the draft label, build in /tmp, copy back, summarise.
# Third series (2026-10-19): versions live in the git checkout; scratch logs and test files are left out.
set -e
M=/home/user/claude_composes/symphony/mvt2
NEW=$(printf %02d $1); PREV=$(printf %02d $2); SRC=$3
W=/tmp/m2/v$NEW; rm -rf $W; mkdir -p $W
(cd $SRC && tar cf - --exclude='*.wav' --exclude='*.mp3' --exclude=build --exclude=probe --exclude=base --exclude='pg*' --exclude='*.png' \
  --exclude='*_c[0-9]*.log' --exclude='ap_*.txt' --exclude='ap[0-9]*.txt' --exclude=gp.log --exclude=gp.txt --exclude=b.log --exclude='b[0-9]*.txt' --exclude='build_*.txt' \
  --exclude='o_*.txt' --exclude='tl.*' --exclude='ttest.*' --exclude='vtest.*' --exclude=score_tl.ly --exclude=midi_players.ly --exclude=mp --exclude=work .) | (cd $W && tar xf -)
sed -i -e "s/draft v$PREV\"/draft v$NEW\"/" -e "s/in C — v$PREV, [^\"]*\"/in C — draft v$NEW\"/" $W/score.ly
bash $M/tools/build.sh $W score.ly >/dev/null 2>&1 || true
mkdir -p $M/v$NEW && (cd $W && tar cf - .) | (cd $M/v$NEW && tar xf -)
echo "warnings: $(wc -c < $M/v$NEW/build-warnings.txt)"; grep -A3 "^Outer" $M/v$NEW/analysis.txt; head -1 $M/v$NEW/analysis.txt; pdfinfo $M/v$NEW/score.pdf | grep Pages; grep -o "draft v[0-9]*" $M/v$NEW/score.ly

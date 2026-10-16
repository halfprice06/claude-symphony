#!/bin/bash
# promote.sh NEW PREV SRC : copy SRC (a critic scratch copy or the composer's edit) into scherzo/vNEW, bump the draft label, build in /tmp, copy back, summarise.
set -e
M=/home/user/claude_composes/symphony/scherzo
NEW=$(printf %02d $1); PREV=$(printf %02d $2); SRC=$3
W=/tmp/sch/v$NEW; rm -rf $W; mkdir -p $W
(cd $SRC && tar cf - --exclude='*.wav' --exclude='score-r0*.mp3' --exclude=build --exclude=probe --exclude=base --exclude='pg*' --exclude='*.png' .) | (cd $W && tar xf -)
sed -i -e "s/draft v$PREV\"/draft v$NEW\"/" $W/score.ly
bash $M/tools/build.sh $W score.ly >/dev/null 2>&1 || true
# instrumental parts (since c075): rebuild so partsout always matches the score
[ -f $W/build-parts.sh ] && { rm -rf $W/partsout; bash $W/build-parts.sh $W > $W/parts-summary.txt 2>&1 || true; }
# theme record (Dan, 2026-10-12: themes are NOT locked; this only reports which themes changed so the finale can follow)
python3 /home/user/claude_composes/symphony/coherence/themecheck.py /home/user/claude_composes/symphony/coherence/themes-scherzo.ly $W > $W/themecheck.txt || true
mkdir -p $M/v$NEW && (cd $W && tar cf - .) | (cd $M/v$NEW && tar xf -)
echo "warnings: $(wc -c < $M/v$NEW/build-warnings.txt)"; grep -A3 "^Outer" $M/v$NEW/analysis.txt; head -1 $M/v$NEW/analysis.txt; pdfinfo $M/v$NEW/score.pdf | grep Pages; grep -o "draft v[0-9]*" $M/v$NEW/score.ly
grep -v '^ok' $M/v$NEW/themecheck.txt; grep -q '^CHANGED' $M/v$NEW/themecheck.txt && echo 'THEMES CHANGED: refresh coherence/themes-scherzo.ly, log under Theme changes in critics/HISTORY.md, send old and new notes to the finale thread'
python3 $M/kit/cmajor.py $M/v$NEW
python3 $M/kit/partlengths.py $M/v$NEW
[ -f $M/v$NEW/parts-summary.txt ] && head -1 $M/v$NEW/parts-summary.txt

#!/bin/bash
# promote.sh NEW PREV SRC : copy SRC (critic scratch copy or composer edit) into mvt1/vNEW, set the header label, build,
# rebuild full.midi and the all-pairs voice-leading list (vl.txt), diff it against vPREV, summarise.
set -e
M=/home/user/claude_composes/symphony/mvt1; NEW=$1; PREV=$2; SRC=$3
W=/tmp/m1/v$NEW; rm -rf $W; mkdir -p $W
(cd $SRC && tar cf - --exclude='*.wav' --exclude='score-r0*.mp3' --exclude=partsout --exclude='pg*' --exclude='*.png' --exclude='p-*' --exclude=probe --exclude=base .) | (cd $W && tar xf -)
sed -i -E "s/— (draft )?v$PREV[^\"]*\"/— draft v$NEW\"/" $W/score.ly
bash $M/tools/build.sh $W score.ly >/dev/null 2>&1 || true
(cd $W && lilypond -dno-point-and-click -o full full.ly >/dev/null 2>&1 && python3 -I $M/tools/critic-scripts/vl.py full.midi > vl.txt) || echo "full.midi FAILED"
PV=$M/v$PREV/vl.txt; [ -f $PV ] || PV=$M/kit/vl-v$PREV.txt
rm -rf $M/v$NEW; mkdir -p $M/v$NEW && (cd $W && tar cf - .) | (cd $M/v$NEW && tar xf -)
echo "warnings: $(wc -c < $M/v$NEW/build-warnings.txt)"; grep -A3 "^Outer" $M/v$NEW/analysis.txt | head -4; pdfinfo $M/v$NEW/score.pdf | grep Pages
echo "vl diff vs v$PREV (< old, > new):"; diff $PV $M/v$NEW/vl.txt | grep '^[<>]' | head -30
grep -o 'subtitle[^"]*"[^"]*"\|v[0-9][0-9][0-9][^"]*"' $M/v$NEW/score.ly | head -3

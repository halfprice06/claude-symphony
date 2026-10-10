#!/bin/bash
# promote.sh NEW PREV SRC : copy critic scratch SRC into mvt1/vNEW (no stale files), bump draft label, build, summarise
set -e
cd /mnt/project-files/symphony/mvt1
mkdir v$1
(cd $3 && tar cf - --exclude='all*.l*' --exclude='all*.midi' --exclude=dump --exclude='perinst*' --exclude=scripts --exclude=probe --exclude=base --exclude=parts .) | (cd v$1 && tar xf -)
sed -i -e "s/draft v$2/draft v$1/" -e "s/Full score in C — v$2/Full score in C — draft v$1/" v$1/score.ly
bash tools/build.sh v$1 score.ly >/dev/null 2>&1 || true
echo "warnings: $(wc -c < v$1/build-warnings.txt)"; grep -A1 "^Outer" v$1/analysis.txt; pdfinfo v$1/score.pdf | grep Pages; grep -o "draft v[0-9]*" v$1/score.ly

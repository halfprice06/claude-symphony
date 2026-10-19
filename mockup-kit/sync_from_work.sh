#!/bin/bash
# Copy a mockup work folder's current pipeline into the kit (scripts only; never the .rpp, renders, generated states or
# the per-note tables). Usage, from the repo root: mockup-kit/sync_from_work.sh symphony/mvt1/reaper
# The movement's own config (build/score_config.py, mix.json, probe.json, mockup.ly) goes to pipeline/example-config-<name>/
# only when asked: mockup-kit/sync_from_work.sh symphony/mvt1/reaper mvt1
set -eu
SRC=$1; K=mockup-kit
cp $SRC/tools/*.py $K/pipeline/
if [ $# -ge 2 ]; then
  mkdir -p $K/pipeline/example-config-$2
  cp $SRC/build/score_config.py $SRC/build/mix.json $SRC/build/probe.json $SRC/build/mockup.ly $K/pipeline/example-config-$2/
fi
cp ~/.rpr-bridge/libs/ew_ho/{opus_state.py,dump_ks.py,ks_maps.json} $K/opus/
echo "synced tools from $SRC (latest cycle $(ls -d $SRC/cycles/c* | tail -1 | sed 's/.*\/c//'))"

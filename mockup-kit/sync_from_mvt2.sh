#!/bin/bash
# Copy the current reference pipeline from the movement II mockup into the kit (scripts and small configs only;
# never the .rpp, renders or generated states). Run from the repo root before committing a kit update.
set -eu
SRC=symphony/mvt2/reaper; K=mockup-kit
cp $SRC/tools/*.py $K/pipeline/
cp $SRC/build/mockup.ly $K/pipeline/
for f in mix.json roles.json note_trims.json; do [ -f $SRC/build/$f ] && cp $SRC/build/$f $K/pipeline/example-config/; done
cp $SRC/loop/BRIEF.md $K/loop/BRIEF-mvt2-example.md
cp $SRC/loop/DYNAMICS-RESEARCH.md $K/loop/
cp $SRC/loop/critic_prompt.md $SRC/loop/actor_prompt.md $K/loop/
cp ~/.rpr-bridge/libs/ew_ho/{opus_state.py,dump_ks.py,ks_maps.json} $K/opus/
echo "synced pipeline from $SRC (cycle $(ls -d $SRC/cycles/c* | tail -1 | sed 's/.*c//'))"

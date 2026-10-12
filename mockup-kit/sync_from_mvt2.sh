#!/bin/bash
# Copy the current reference pipeline from the movement II mockup into the kit (scripts and small configs only;
# never the .rpp, renders or generated states). Run from the repo root before committing a kit update.
set -eu
SRC=symphony/mvt2/reaper; K=mockup-kit
cp $SRC/tools/*.py $K/pipeline/
cp $SRC/build/mockup.ly $K/pipeline/
for f in $SRC/build/*.json; do case $(basename $f) in parts.json|ks_maps_extra.json) ;; *) cp $f $K/pipeline/example-config/;; esac; done
cp $SRC/loop/BRIEF.md $K/loop/BRIEF-mvt2-example.md
cp $SRC/loop/DYNAMICS-RESEARCH.md $K/loop/
cp $SRC/loop/critic_prompt.md $SRC/loop/actor_prompt.md $K/loop/
cp ~/.rpr-bridge/libs/ew_ho/{opus_state.py,dump_ks.py,ks_maps.json} $K/opus/
echo "synced pipeline from $SRC (latest cycle folder $(ls -d $SRC/cycles/c* | tail -1 | sed "s/.*c//")))"
cp $SRC/build/ks_maps_extra.json $K/opus/ 2>/dev/null || true

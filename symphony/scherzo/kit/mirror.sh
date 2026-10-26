#!/bin/bash
# mirror.sh vNN : copy the scherzo's small shared files from the git checkout into /mnt/project-files (third series, 2026-10-19).
# The versions themselves live in git (branch claude/project-thread-y9u1tb); the shared folder keeps only text and the latest version without audio.
G=/home/user/claude_composes/symphony; P=/mnt/project-files/symphony; V=$1
cp $G/coherence/scherzo.md $G/coherence/themes-scherzo.ly $G/coherence/themes-scherzo.md $P/coherence/
mkdir -p $P/scherzo/critics $P/scherzo/kit
cp $G/scherzo/CHECKPOINT.md $G/scherzo/README.md $P/scherzo/
cp -r $G/scherzo/critics/. $P/scherzo/critics/
(cd $G/scherzo/kit && tar cf - --exclude='p[0-9]*.txt' .) | (cd $P/scherzo/kit && tar xf -)
rm -rf $P/scherzo/latest; mkdir -p $P/scherzo/latest
(cd $G/scherzo/$V && tar cf - --exclude='*.mp3' --exclude=partsout --exclude='*.midi' .) | (cd $P/scherzo/latest && tar xf -)
echo "$V" > $P/scherzo/latest/VERSION

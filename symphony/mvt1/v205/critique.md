# v205 — critic 185 (parts stage; MOLA second pass)

Report: critics/reports/c185.md

Applied (full score pixel-identical to v204):
- New parts build: `bash tools/build.sh <vdir> score.ly`, then `bash <vdir>/build-parts.sh <vdir>` → 30 parts in `<vdir>/partsout/parts-NN-<instrument>.pdf` (B4, 7.2 mm staves, page turns in rests, cues in long rests). Edit parts-gen.py, not the generated parts.ly. PARTS_AUDIT=1 adds a proofreading log.
- Transposed parts (Cl, B.cl, C.a.) now get transposed key signatures; horn, trumpet and timpani parts have none.
- Multi-bar rests joined correctly; tempo/rehearsal marks take horizontal space in parts.
- Hn 4 bass clef in modern notation at 11–12 and 23–25 (back to treble at 26).
- Harp pedal marks kept in the score, left out of the harp part (MOLA; c155/c165). Restorable in parts-gen.py.
- Page turns in rests (Fl 1, Hn 1 at 127–130; Ob 1 into 147); strings and harp have a cover page so their music fills two facing pages.
- Part-only markings: Hn 1 ossia 8vb at 106; "a2 with 3." in Hn 4 at 158; Bsn 1 "Solo" at 33; Hn 4 mp at 67.

Open: composer name on score and parts (needs Dan); B.cl bass clef at 91–106 kept (Adler prefers treble throughout).

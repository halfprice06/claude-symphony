# Brief for critics of Symphony No. 1, movement III

You are one critic in a series of 200 compose–critique–revise cycles on movement III, the finale. The composer (another Claude session) reads your report and revises the score. You do not edit the score itself; you may test fixes in a scratch copy (see your task).

## The goal (from Dan, who commissioned the work)
- A full orchestral score of a neo-Romantic symphony that would be indistinguishable from the work of a modern master composer.
- Equal weight on beauty: melodies that stick, and that might stay with a listener for a lifetime.
- Models: Brahms, Tchaikovsky, Dvořák, Rachmaninoff, Elgar, with late-Romantic orchestration. For this movement the main models are Brahms 1/iv (the C-major arrival and chorale), Tchaikovsky 5/iv (a motto turned to major) and Dvořák 9/iv (earlier themes recalled in a finale).
- Dan makes no musical choices. Do not leave anything "for the composer to decide" or "for Dan": decide every optional point yourself and say what you decided.

## The work
- Movement III: Allegro con fuoco, C minor ending in C major, sonata form with a long coda (arrival, chorale, second-theme head, final combination), all in 2/2. Plan: /mnt/project-files/symphony/mvt3/movement-3-plan.md.
- Movement I (C minor) is finished: /mnt/project-files/symphony/mvt1/v221/ (use it as the reference). Movement II (Adagio, A♭ major) is in progress in /mnt/project-files/symphony/mvt2/ (latest vNN); it ends on a soft A♭ chord, and movement III starts after a pause.
- Material shared between movements: /mnt/project-files/symphony/cyclic-notes.md. Read its section "Start here for movement III" first; where older notes disagree, that section wins. Rules from it that bind this movement:
  - Open loud from movement II's A♭ chord as a German sixth to V of C; no soft opening.
  - The first theme is new and does not open with a rising sixth.
  - No root-position V–I (or V–i) cadence in C before the last cadence (254–255), which is the symphony's first since movement I bar 135, trumpets B→C.
  - The owed items sound once each, in this movement only: the soft trumpet solo (trumpets' first entry, 51), the C-major arrival with string tremolo and the violins' C7 (219 only), the falling major motto G–E–D–C in full brass, the brass chorale and its last statement, the violins' C-major second-theme head over a C pedal, the brass combination of the theme heads, the hammered tutti in movement I's layout, the horn call in major in the trumpets, the E♭/E♮ thread closed in the violas.
  - The stop chord B–D–F–A♭ resolves to C only at the arrival (218→219).
  - No tam-tam. Hn 3·4 "senza sord." at their first entry. The timpani's first label gives the retuning made in the pause.
  - Every F♭ resolves to E♭. Length at least 6 minutes.
- Orchestra: 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon, 4 horns, 3 trumpets, 2 trombones, bass trombone, tuba, timpani, cymbals and bass drum (one DrumStaff, `\drummode`: `cymc` crash cymbal, `bd` bass drum), harp, strings.
- Page cap: the score is 16 A3 pages (v01). Check the page count of the version you review and of your scratch build. A change that adds a page must say why the page is worth it.

## Files (read-only for you)
Version under review: /mnt/project-files/symphony/mvt3/vNN/:
- `global.ily`: tempi, keys, time signatures, rehearsal marks, MIDI tempo steps (`\mt`, in quarter notes per minute: 2 = 84 is `\mt 168`).
- `sections.txt`: section name, length in bars, and quarter beats per bar (4 throughout: 2/2).
- `sections/*.ily`: one file per section, one variable per instrument (e.g. `pOneVlnOne`). Order: intro, pOne, pTwo, trans, sOne, sTwo, clos, dev, retr, recP, recS, codaOne, codaTwo, arrival, sHead, finale (check sections.txt; the composer may add sections).
  - LilyPond 2.24, Dutch note names (es = E♭, fis = F♯), absolute pitch (c' = middle C).
  - Everything is at concert pitch. Contrabass and contrabassoon are written at sounding pitch and displayed an octave up.
- `score.ly`: staff setup; pairs of instruments are part-combined.
- `score.pdf`: engraved score. `score.mp3`: FluidSynth rendering; nobody in this loop can hear it, do not pretend to.
- `analysis.txt`: automatic outer-voice parallel check, ranges, and a density profile. Trumpet C6 is flagged by the analyser (limit B♭5) and was accepted for C trumpet.
- `critique.md`: the composer's notes on that version.

To look at pages: `pdftoppm -r 70 -png -f N -l N score.pdf /tmp/critic-<cycle>/p` and read the PNG.

## History
- `/mnt/project-files/symphony/mvt3/critics/HISTORY.md` lists, cycle by cycle, what earlier critics raised, what the composer accepted or rejected and why, and the do-not-touch list.
- Do not repeat a point that was fixed. You may re-raise a rejected point only if you answer the composer's stated reason.

## Research: required, and the reason you exist

**The books come first** (Dan, 2026-10-09: "I want greater coverage and use of the books. the focus should be on the books content"). Each cycle has an assigned reading in critics/READING.md. Read it in full, view its example pages as images, list its principles in a "Reading notes" table, and base your findings on it.

Dan's reference books: /mnt/project-files/reference-books/. INVENTORY.md lists each book, its chapters with PDF page numbers, and which pages are mostly music examples. Text is in `text/<book>/pNNNN.txt` (one file per PDF page; scanned books were OCR'd, so check odd wording and all notation against the page image). Books: Adler, *The Study of Orchestration* (2 parts); Aldwell & Schachter, *Harmony and Voice Leading*; Rimsky-Korsakov, *Principles of Orchestration* (file "principles of form.pdf"); Gould, *Behind Bars* (ch. 1–2 excerpt); Sebesky, *The Contemporary Arranger*; Casanelles, *The Hyperorchestra*; MOLA guidelines. `oct_9_score.pdf` is a copy of movement I, not a reference.
- Every report cites at least three specific book passages (book, chapter, PDF page).
- View printed examples as images: `pdftoppm -f N -l N -r 110 -png "<book>.pdf" /tmp/critic-NNN/pg`, then Read the PNG.

Supporting sources:
1. Local corpus: /mnt/project-files/reference-corpus/ (README.md is the index). Finales there include Dvořák 9/iv and 7/iv, Tchaikovsky 6/iv, Beethoven 9/iv and the Eroica finale, Mozart 41/iv, Méhul 1/iv. Compare bar by bar and cite file and bar.
2. The web (WebSearch, WebFetch): IMSLP, analyses, instrument guides. Cite URLs.

## Your report
Plain direct prose without metaphors or flourish.
1. "Reading notes" table: principle, book and PDF page, bars of this score, verdict (follows / violates / not applicable).
2. A short paragraph on what else you studied.
3. Up to 8 findings ranked by how much each stands between this score and a master's work: bars; what is wrong; evidence; a concrete fix in LilyPond in this score's conventions.
4. One line naming what is already at a master's level and should not be touched.

If a finding would undo an earlier fix, say so. Keep the report under 2000 words, not counting the Reading notes table.

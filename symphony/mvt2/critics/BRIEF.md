# Brief for critics of Symphony No. 1, movement II

You are one critic in a series of 400 compose–critique–revise cycles on movement II. The composer (another Claude session) reads your report and revises the score. You do not edit the score itself; you may test fixes in a scratch copy (see your task).

## The goal (from Dan, who commissioned the work)
- A full orchestral score of a neo-Romantic symphony that would be indistinguishable from the work of a modern master composer.
- Equal weight on beauty: melodies that stick, and that might stay with a listener for a lifetime.
- Models: Brahms, Tchaikovsky, Dvořák, Rachmaninoff, Elgar, with late-Romantic orchestration. For this movement the main model is Dvořák 9/ii (Largo).

## The work
- Movement II: Adagio in A♭ major, ABA′ with a D♭-major middle section and a coda. Plan: /home/user/claude_composes/symphony/mvt2/movement-2-plan.md.
- Movement I (C minor, finished separately, latest version in /home/user/claude_composes/symphony/mvt1/) ends on a soft C-major chord with C5 on top; movement II opens from it by a common-tone modulation.
- Material shared between movements: /home/user/claude_composes/symphony/cyclic-notes.md. Read §3 "Plan for movements II and III" and the "Changes" sections. Rules from it that bind this movement: no tam-tam, no trombone chorale and no C-major material (reserved for the finale, now movement IV); new themes do not open with a rising sixth; the S-head rhythm `2.~ 8 8 | 4 2 4` is used only in the one quotation; melodic moments for horn, bass clarinet, harp and timpani; string-free passages; D♭ as a key; plagal D♭–A♭ close with D♭–C on top.
- Four movements since 2026-10-12: I C minor, II this Adagio in A♭, III Scherzo in E (symphony/scherzo/), IV finale in C (symphony/mvt3/). Each movement keeps a current-state file. Since 2026-10-30 mvt1.md, mvt2.md, scherzo.md and movement II's theme records (themes-mvt2*.ly, themecheck.py, lyparse.py) are in the checkout's /home/user/claude_composes/symphony/coherence/; the live finale.md is /mnt/project-files/symphony/coherence/finale.md (the checkout's finale.md is an older copy) (c450) (mvt1.md, mvt2.md, scherzo.md, finale.md, plus themes-*.ly). Movement II's last bars lead into the scherzo: its Hn 1 opens on G♯4 = movement II's last A♭, timpani retune to E, G, B, E. Themes in every movement may still develop (nothing is locked), but a change to movement II's ending, its exported themes or its quotations must be reported in your findings so the composer can tell the other threads. Never edit files outside your report.
- Orchestra (same as movement I): 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon, 4 horns, 3 trumpets, 2 trombones, bass trombone, tuba, timpani, harp, strings. No percussion in this movement.

## Files (read-only for you)
Version under review: /home/user/claude_composes/symphony/mvt2/vNN/:
- `global.ily`: tempi, keys, time signatures, rehearsal marks, MIDI tempo steps (`\mt`).
- `sections.txt`: section name, length in bars, and quarter beats per bar (the metre is mixed: 3/4 and 4/4).
- `sections/*.ily`: one file per section, one variable per instrument (e.g. `aOneVlnOne`). Order: intro, aOne, trans, bSec, retr, aTwo, coda (check sections.txt; the composer may add sections).
  - LilyPond 2.24, Dutch note names (es = E♭, fis = F♯), absolute pitch (c' = middle C).
  - Everything is at concert pitch. Contrabass and contrabassoon are written at sounding pitch and displayed an octave up.
- `score.ly`: staff setup; pairs of instruments are part-combined.
- `score.pdf`: engraved score. `score.mp3`: FluidSynth rendering; nobody in this loop can hear it, do not pretend to.
- `analysis.txt`: automatic outer-voice parallel check, ranges, and a density profile (bar numbers follow the real metre).
- `critique.md`: the composer's notes on that version.

To look at pages: `pdftoppm -r 70 -png -f N -l N score.pdf /tmp/critic-<cycle>/p` and read the PNG.

## History
- `/home/user/claude_composes/symphony/mvt2/critics/HISTORY.md` lists, cycle by cycle, what earlier critics raised, what the composer accepted or rejected and why, and the do-not-touch list.
- Do not repeat a point that was fixed. You may re-raise a rejected point only if you answer the composer's stated reason.

## Research: required, and the reason you exist

**The books come first** (Dan, 2026-10-09: "I want greater coverage and use of the books. the focus should be on the books content"). Each cycle has an assigned reading in critics/READING.md. Read it in full, view its example pages as images, list its principles in a "Reading notes" table, and base your findings on it.

Dan's reference books: text and INVENTORY.md in /home/user/claude_composes/reference-books/; the PDFs are in /home/user/claude_composes/pdfs/ (render example pages from there). INVENTORY.md lists each book, its chapters with PDF page numbers, and which pages are mostly music examples. Text is in `text/<book>/pNNNN.txt` (one file per PDF page; scanned books were OCR'd, so check odd wording and all notation against the page image). Books: Adler, *The Study of Orchestration* (2 parts); Aldwell & Schachter, *Harmony and Voice Leading*; Rimsky-Korsakov, *Principles of Orchestration* (file "principles of form.pdf"); Gould, *Behind Bars* (ch. 1–2 excerpt); Sebesky, *The Contemporary Arranger*; Casanelles, *The Hyperorchestra*; MOLA guidelines. `oct_9_score.pdf` is a copy of movement I, not a reference.
- Every report cites at least three specific book passages (book, chapter, PDF page).
- View printed examples as images: `pdftoppm -f N -l N -r 110 -png "/home/user/claude_composes/pdfs/<book>.pdf" /tmp/critic-NNN/pg`, then Read the PNG.

Supporting sources:
1. Local corpus: /home/user/claude_composes/reference-corpus/ (README.md is the index). Slow movements there include Dvořák 9/ii and 7/ii, Tchaikovsky 6/iv and the Violin Concerto's Canzonetta, Beethoven 9/iii, 3/ii and 7/ii, Mozart 41/ii. Compare bar by bar and cite file and bar.
2. The web (WebSearch, WebFetch): IMSLP, analyses, instrument guides. Cite URLs.

## Your report
Plain direct prose without metaphors or flourish.
1. "Reading notes" table: principle, book and PDF page, bars of this score, verdict (follows / violates / not applicable).
2. A short paragraph on what else you studied.
3. Up to 8 findings ranked by how much each stands between this score and a master's work: bars; what is wrong; evidence; a concrete fix in LilyPond in this score's conventions.
4. One line naming what is already at a master's level and should not be touched.

If a finding would undo an earlier fix, say so. Keep the report under 2000 words, not counting the Reading notes table.

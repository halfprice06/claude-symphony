# Brief for critics of Symphony No. 1, movement I

You are one critic in a long series of compose–critique–revise cycles. The composer (another Claude session) will read your report and revise the score. You do not edit the score.

## The goal (from Dan, who commissioned the work)
- A full orchestral score of the first movement of a neo-Romantic symphony that would be indistinguishable from the work of a modern master composer.
- Equal weight on beauty: melodies that stick, and that might stay with a listener for a lifetime.
- Models in the plan: Brahms, Tchaikovsky, Dvořák, Rachmaninoff, Elgar, with late-Romantic orchestration.

## The work
- C minor, sonata form with a slow introduction and a cyclic motto: G rising a minor sixth to E♭, then falling chromatically D–D♭–C.
- Orchestra: 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon, 4 horns, 3 trumpets, 2 trombones, bass trombone, tuba, timpani, percussion (cymbals, tam-tam), harp, strings.
- Plan: /mnt/project-files/symphony/movement-1-plan.md

## Files (read-only for you)
Latest version: the folder named in your task, e.g. /mnt/project-files/symphony/mvt1/vNN/. It contains:
- `global.ily`: tempi, keys, rehearsal marks.
- `sections.txt`: section lengths in bars.
- `sections/*.ily`: one file per section, one variable per instrument (e.g. `tOneVlnOne`). The order is intro, tOne, trans, tTwo, clos, dev, recOne, recTwo, coda.
  - LilyPond 2.24, Dutch note names (es = E♭, fis = F♯), absolute pitch (c' = middle C).
  - Everything is written at concert pitch. Contrabass and contrabassoon are written at sounding pitch and displayed an octave up.
- `score.ly`: staff setup. Pairs of instruments are part-combined.
- `score.pdf`: engraved score.
- `score.mp3`: FluidSynth rendering. Neither you nor the composer can hear it. Do not pretend to.
- `analysis.txt`: an automatic outer-voice parallel check and a density profile.
- `critique.md`: the composer's notes on that version.

Movement bar numbers are printed in the PDF. Note: since v100 the movement has 182 bars. HISTORY entries before cycle 70 use the oldest numbering (add 8 to old bar numbers ≥ 103); entries before cycle 80 use the 186-bar numbering (subtract 4 from bar numbers ≥ 160). Section start bars are in `sections.txt` (cumulative).

To look at pages, render them with `pdftoppm -r 70 -png -f N -l N score.pdf /tmp/critic-<yourcycle>/p` into a new directory of your own under /tmp, and read the PNG. Do not write anywhere under /mnt/project-files except your own report file.

## History
- `/mnt/project-files/symphony/mvt1/critics/HISTORY.md` lists, cycle by cycle, what earlier critics raised and what the composer did or rejected, and why.
- Do not repeat a point that was fixed.
- You may re-raise a point the composer rejected, but only if you answer the composer's stated reason.

## Research: required, and the reason you exist

**From cycle 107: the books come first.** Dan asked for greater coverage and use of his reference books, with the focus on their content. Each cycle has an assigned reading in critics/READING.md. Read it in full, view its example pages as images, list its principles in a "Reading notes" table, and base your findings on it. The corpus and the web below are supporting sources.
Ground your judgments in evidence, not taste alone.
1. **Local reference corpus:** /mnt/project-files/reference-corpus/ (README.md is the index). It holds LilyPond and MusicXML scores of Romantic symphonies (Brahms, Tchaikovsky, Dvořák, Beethoven and others) and compiled PDFs in `pdf/`. Find specific passages that do what this score attempts, and compare them bar by bar. Cite file and bar, e.g. "Tchaikovsky 6/i bars 89–100 voices the second theme in ...".
2. **The web:** use WebSearch and WebFetch for orchestration and engraving authorities and for score analyses. Examples:
   - Rimsky-Korsakov, *Principles of Orchestration* (public domain online);
   - Adler, *The Study of Orchestration*;
   - Gould, *Behind Bars* (engraving conventions);
   - IMSLP score pages;
   - analyses of the model works;
   - instrument range and technique guides.

   Cite what you used, with URLs.

3. **Dan's reference books (required from cycle 101 on):** /mnt/project-files/reference-books/. INVENTORY.md there lists each book, its chapters with PDF page numbers, and which pages are mostly music examples. Searchable text is in `text/<book>/pNNNN.txt` (one file per PDF page; the scanned books were OCR'd, so check odd wording against the page image). The books: Adler, *The Study of Orchestration* (2 parts); Aldwell & Schachter, *Harmony and Voice Leading* (3rd ed., OCR; Roman numerals in the text are unreliable, check the image); Rimsky-Korsakov, *Principles of Orchestration* (the file is misnamed "principles of form.pdf"; text PDF 13–170, examples PDF 173–504); Gould, *Behind Bars* (excerpt: chapters 1–2 only); Sebesky, *The Contemporary Arranger*; Casanelles, *The Hyperorchestra*; MOLA guidelines for music preparation. `oct_9_score.pdf` is a copy of this movement (v120), not a reference.
   - Every report must cite at least three specific book passages (book, chapter, PDF page) that bear on its findings.
   - Many examples in these books are printed scores. View them as images: `pdftoppm -f N -l N -r 110 -png "<book>.pdf" /tmp/critic-NNN/pg` and then Read the PNG. Compare the book's example with this score's passage.
   - The books may justify reopening a decision recorded as settled in HISTORY.md. If so, quote the book and answer the reason the decision was taken.

If a source is unreachable, say so and continue.

## Your report
Write it to the path given in your task, as plain direct prose without metaphors or flourish.
1. A short paragraph on what you studied: corpus files and web sources.
2. Up to 8 findings, ranked by how much each one stands between this score and a master's work. Each finding gives:
   - the bar numbers;
   - what is wrong;
   - the evidence (corpus comparison or cited source);
   - a concrete fix, written as LilyPond notes in this score's conventions where possible.
3. One line naming anything that is already at a master's level and should not be touched. This protects good material from churn.

If a finding would undo an earlier fix, say so explicitly.

Keep the report under 2000 words (the Reading notes table does not count). Return the report text as your final answer as well.

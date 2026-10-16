# Brief for critics of Symphony No. 1, movement III (Scherzo)

You are one critic in a series of 200 compose–critique–revise cycles on the scherzo. The composer (another Claude session) reads your report and revises the score. You do not edit the score itself; you may test fixes in a scratch copy (see your task).

## The goal (from Dan, who commissioned the work)
- A full orchestral score of a neo-Romantic symphony that would be indistinguishable from the work of a modern master composer.
- Equal weight on beauty: melodies that stick, and that might stay with a listener for a lifetime.
- Models: Brahms, Tchaikovsky, Dvořák, Rachmaninoff, Elgar, with late-Romantic orchestration. For this movement the main models are Dvořák 9/iii (E minor scherzo), Beethoven 9/ii (motivic timpani), the hemiola scherzi of Brahms and Bruckner, and the soft trios of the Eroica and Dvořák 8.
- Dan makes no musical choices. Do not leave anything "for the composer to decide" or "for Dan": decide every optional point yourself and say what you decided.

## The work
- The symphony now has four movements (Dan, 2026-10-12): I Allegro (C minor, finished: /home/user/claude_composes/symphony/mvt1/v221/), II Adagio (A♭ major, /home/user/claude_composes/symphony/mvt2/, latest vNN), III Scherzo (this movement, E minor with an E-major trio), IV Finale (C minor → C major, /home/user/claude_composes/symphony/mvt3/, paused at v26 and to be reworked once the scherzo's themes and ending are settled).
- Plan: /home/user/claude_composes/symphony/scherzo/movement-scherzo-plan.md. 3/4 throughout, one beat to the bar (Allegro vivace 2. = 88; Trio 2. = 76).
- Material shared between movements: /home/user/claude_composes/symphony/cyclic-notes.md. Read its section "Four movements (Dan, 2026-10-12): plan for the scherzo" first. Rules from it that bind this movement:
  - No C major anywhere (no C-major key, no C-major triad); C major belongs to the finale's arrival.
  - Trumpets only in tutti rhythm or fanfare figures; no trumpet melody.
  - Kept for the finale, not used here: string tremolo, the violins' C7, the trumpets' B→C, the stop chord B–D–F–A♭ (in any spelling, including B–D–F–G♯, and in any role: no common-tone or other use of this diminished seventh anywhere in the scherzo), the falling major motto in full brass, the brass chorale, the violins' C-major second theme, the combined heads, the hammered tutti in major, a tuba melody, a high horn unison, a full low-brass unison bass, cymbals.
  - Violin peak at most B6 (the finale reaches C7).
  - Quote the motto (its chromatic tail, the horn call), do not develop it. New themes do not open with a rising sixth.
  - Hn 3·4 "senza sord." at their first entry; the timpani's first label gives the retuning made in the pause after movement II.
  - The movement starts and ends on G♯ in the horn (movement II's A♭); the finale's link will start from the scherzo's last chord.
- Orchestra: 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon, 4 horns, 3 trumpets, 2 trombones, bass trombone, tuba, timpani (E, G, B, E; G→G♯ for the trio), harp, strings. No percussion staff.
- Page count: v01 is 13 A3 pages. Check the page count of the version you review and of your scratch build. A change that adds a page must say why the page is worth it.

## Files (read-only for you)
Version under review: /home/user/claude_composes/symphony/scherzo/vNN/:
- `global.ily`: tempi, keys, time signature, rehearsal marks, MIDI tempo steps (`\mt`, in quarter notes per minute: 2. = 88 is `\mt 264`).
- `sections.txt`: section name, length in bars, and quarter beats per bar (3 throughout).
- `sections/*.ily`: one file per section, one variable per instrument (e.g. `sAVlnOne`). Order: intro, sA, sB, sC, link, tA, tB, tC, retr, dA, dB, dC, coda (check sections.txt; the composer may add sections).
  - LilyPond 2.24, Dutch note names (es = E♭, fis = F♯), absolute pitch (c' = middle C).
  - Everything is at concert pitch. Contrabass and contrabassoon are written at sounding pitch and displayed an octave up.
- `score.ly`: staff setup; pairs of instruments are part-combined.
- `score.pdf`: engraved score. `score.mp3`: FluidSynth rendering; nobody in this loop can hear it, do not pretend to.
- `analysis.txt`: automatic outer-voice parallel check, ranges, and a density profile. Its bar numbers can drift by one or two bars late in the movement; check against the score.
- `critique.md`: the composer's notes on that version.

To look at pages: `pdftoppm -r 70 -png -f N -l N score.pdf /tmp/critic-<cycle>/p` and read the PNG.

## History
- `/home/user/claude_composes/symphony/scherzo/critics/HISTORY.md` lists, cycle by cycle, what earlier critics raised, what the composer accepted or rejected and why, and the do-not-touch list.
- Do not repeat a point that was fixed. You may re-raise a rejected point only if you answer the composer's stated reason.

## Research: required, and the reason you exist

**The books come first** (Dan, 2026-10-09: "I want greater coverage and use of the books. the focus should be on the books content"). Each cycle has an assigned reading in critics/READING.md. Read it in full, view its example pages as images, list its principles in a "Reading notes" table, and base your findings on it.

Dan's reference books: /home/user/claude_composes/reference-books/. INVENTORY.md lists each book, its chapters with PDF page numbers, and which pages are mostly music examples. Text is in `text/<book>/pNNNN.txt` (one file per PDF page; scanned books were OCR'd, so check odd wording and all notation against the page image). Books: Adler, *The Study of Orchestration* (2 parts); Aldwell & Schachter, *Harmony and Voice Leading*; Rimsky-Korsakov, *Principles of Orchestration* (file "principles of form.pdf"); Gould, *Behind Bars* (ch. 1–2 excerpt); Sebesky, *The Contemporary Arranger*; Casanelles, *The Hyperorchestra*; MOLA guidelines. `oct_9_score.pdf` is a copy of movement I, not a reference.
- Every report cites at least three specific book passages (book, chapter, PDF page).
- View printed examples as images: `pdftoppm -f N -l N -r 110 -png "<book>.pdf" /tmp/critic-NNN/pg`, then Read the PNG.

Supporting sources:
1. Local corpus: /home/user/claude_composes/reference-corpus/ (README.md is the index). Scherzi there: Dvořák 9/iii (E minor, Molto vivace) and 7/iii, Beethoven 9/ii, Eroica iii, Tchaikovsky 6/iii, Mozart 41/iii (menuetto), Méhul 1/iii. Compare bar by bar and cite file and bar.
2. The web (WebSearch, WebFetch): IMSLP, analyses, instrument guides. Cite URLs.

## Your report
Plain direct prose without metaphors or flourish.
1. "Reading notes" table: principle, book and PDF page, bars of this score, verdict (follows / violates / not applicable).
2. A short paragraph on what else you studied.
3. Up to 8 findings ranked by how much each stands between this score and a master's work: bars; what is wrong; evidence; a concrete fix in LilyPond in this score's conventions.
4. One line naming what is already at a master's level and should not be touched.

If a finding would undo an earlier fix, say so. Keep the report under 2000 words, not counting the Reading notes table.

## Coherence across movements (coordinator, 2026-10-12 22:24 UTC, at Dan's request)
The finale (movement IV, symphony/mvt3/) resumed its rework from the scherzo. Each movement keeps a current-state file in /home/user/claude_composes/symphony/coherence/ (scherzo.md, finale and movement II files by their threads). Cyclic-review cycles must read every file there and check the link from movement II's latest ending into bar 1 and from the scherzo's ending into the finale's latest opening. Report any mismatch as a finding; changes to the scherzo's opening, ending, exported themes, keys or timpani tunings must be named so the composer can notify the other threads.

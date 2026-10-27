# v316 (cycle 315, lens 5, MOLA guidelines, parts)

Report: critics/reports/c315.md.
- Parts: rehearsal letters and tempo words landed at different heights at D, F, K, N, O, P, Q, R, T (the problem movement II found in its parts; MOLA PDF 10 Ex. 4). A new `\lt` helper in global.ily draws the tempo text inside the letter's mark, active only with `isPartsBook = ##t` (set in parts-head.ily; keep that line if the file is regenerated). Percussion and timpani padding adjusted.
- Fl 2 part: fixed page turn in the rest at 198|199, back to 2 pages.
- Part titles: "Symphony No. 1 in C minor — IV. Finale" (MOLA PDF 6).
- Bar 10: part-only minimum hairpin length in Fl 1, Fl 2 and Ob 2, so the crescendo prints (MOLA PDF 8 Ex. 7). Parts now build with 0 warnings (were 5).
- Score pixel-identical and MIDI byte-identical to v315. mkparts.py is stale; parts-book.ly is the real parts source.

Build: 0 warnings, 0 parallels, 16 pages, theme record: 39/39 unchanged.

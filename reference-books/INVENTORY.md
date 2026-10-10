# Reference books: inventory

Nine PDFs added by Dan on 2026-10-09 (originals also in `/home/user/claude_composes/pdfs/`).
Text extracted 2026-10-09. All page numbers below are **PDF page numbers** (1-based) unless marked "p." (printed page).

## How to use

1. Search the combined text for a book. Each page starts with a marker line `=== p123 ===` (PDF page 123).
   To get the page number with each hit:

   ```sh
   cd /mnt/project-files/reference-books/text
   awk '/^=== p/{p=$2} tolower($0) ~ /doubling/ {print FILENAME": "p": "$0}' adler1.txt adler2.txt rimsky-principles.txt
   ```

   Plain `grep -n -i word book.txt` also works; scroll up to the nearest `=== pN ===` line.
2. Read one page as text: `text/<book>/p0123.txt` (4-digit, zero-padded PDF page).
3. Look at music examples as images, not as text. The text of notation is garbage in every book. Render a page with
   `pdftoppm -f 123 -l 123 -r 110 -png "<book>.pdf" /tmp/pg` and open `/tmp/pg-123.png` (or `-0123.png`, depending on the page count). Do not write images into this folder.
4. Each book folder has `pages.tsv` (pdf_page, prose_lines, chars, class). Class `EX` = few prose lines (mostly music examples, score excerpts, tables, or a title/TOC/index page), `mixed` = prose plus examples, `text` = mostly prose, `blank`. This is a heuristic count, so treat it as a hint.
5. Printed page to PDF page: use the offset given for each book (PDF = printed + offset). For the scanned Aldwell & Schachter the offset drifts. Use the unit table below and check ±2 pages.

Text folder: `/mnt/project-files/reference-books/text/` (per-page files in `<book>/`, combined file `<book>.txt`).

| Short name | PDF file | PDF pages | Text source | Quality |
|---|---|---|---|---|
| adler1 | adler - the study of orchestration (part 1 of 2).pdf | 329 | native layer (old Acrobat OCR) + 1 page re-OCR | prose very good (~98% words); notation garbage |
| adler2 | adler - the study of orchestration (part 2 of 2).pdf | 329 | native layer + 1 page re-OCR | as part 1; many landscape full-score pages |
| gould-behind-bars | behind bars.pdf | 68 | native (publisher text) | clean; special glyphs (fractions, symbols) sometimes odd |
| aldwell-schachter | harmony and voice leading.pdf | 626 | Tesseract OCR, 300 dpi | prose good (~95-97%); chord labels and figures unreliable (6/4 often read as "§", II6 as "Ilé"); stray fragments from the facing page at the top of many pages |
| sebesky | the contemporary arrange - sedesky.pdf | 242 | Tesseract OCR, 300 dpi | prose good (~95%); page-border rules OCR'd as junk lines ("wwvwv..."); chord symbols garbled |
| hyper-orchestra | hyper-orchestra.pdf | 336 | native (publisher text) | clean |
| rimsky-principles | principles of form.pdf | 516 | native layer (Internet Archive OCR) + 57 empty pages OCR'd by Tesseract | prose good (~95%) but with odd word spacing; example pages are scores (text useless) |
| mola | MOLA-Guidelines-for-Music-Preparation.pdf | 16 | native + 5 image pages OCR'd | clean prose; pp. 9-11 (PDF) are example images |
| oct9-score | oct_9_score.pdf | 17 | native (LilyPond) | only titles, instrument names, tempo and expression words are useful |

---

## 1. Adler, *The Study of Orchestration*, 2nd edition (W. W. Norton, 1989)

Samuel Adler (Eastman). Split into two PDFs of 329 pages each. This is the main orchestration reference in the set.

- **Part 1** (`adler1`): PDF 1-18 front matter (TOC PDF 6-11). Printed pp. 3-313. **PDF = printed + 16.**
- **Part 2** (`adler2`): printed pp. 314-642, index, publisher adverts. **PDF = printed − 313** (PDF 1 = p. 314).
- Text: old Acrobat OCR layer. Prose and example captions ("Example III-60. Harris, Symphony No. 3 ...") read well. Notation is garbage. PDF 273 (part 1) and 136 (part 2) had an empty layer and were re-OCR'd (both are score pages).
- Many full-score examples are printed sideways (landscape). Render them and rotate if needed.

Chapter map (printed p. → file and PDF page):

| Ch. | Title | Printed | PDF |
|---|---|---|---|
| — | Contents / Preface | v-xv | adler1 6-16 |
| 1 | The Orchestra, Yesterday and Today | 3 | adler1 19 |
| 2 | Bowed String Instruments (divisi p.14, bowing p.20, harmonics p.46) | 8 | adler1 24 (divisi 30, bowing 36) |
| 3 | Individual Bowed Strings: violin 55, viola 68, cello 80, bass 88 | 55 | adler1 71, 84, 96, 104 |
| 4 | Plucked Strings (harp 94) | 94 | adler1 110 |
| 5 | Scoring for Strings: foreground-middleground-background 116, homophonic writing 134, strings as accompaniment 142 | 109 | adler1 125 (132, 150, 158) |
| 6 | The Woodwind Choir | 152 | adler1 168 |
| 7 | Individual Woodwinds: flute 168, oboe 181, clarinet 192, bassoon 209, contrabassoon 214 | 168 | adler1 184 (197, 208, 225, 230) |
| 8 | Scoring for Woodwinds and Woodwind-String Combinations: winds in the symphony orchestra 218, variety of orchestral treatments 235 | 217 | adler1 233 (234, 251) |
| 9 | Introduction to Brass | 266 | adler1 282 |
| 10 | Individual Brass: horn 283, trumpet 296, trombone 311, tuba 319 | 283 | adler1 299, 312, 327; tuba adler2 6 |
| 11 | Scoring for Brass, and Brass with Strings and Winds: homophonic unit 332, melodic presentation 339, climactic uses 350, contrapuntal 354 | 327 | adler2 14 (19, 26, 37, 41) |
| 12 | The Percussion Ensemble (timpani 392) | 368 | adler2 55 (79) |
| 13 | Keyboard Instruments | 405 | adler2 92 |
| 14 | Scoring for Percussion with Keyboard | 419 | adler2 106 |
| 15 | **Scoring for Orchestra**: unison-octave tutti 460, foreground and background 467, homophonic texture 472, polyphonic texture 485, additional thoughts 500, special effects 502 | 459 | adler2 146 (147, 154, 159, 172, 187, 189) |
| 16 | The Orchestral Transcription | 510 | adler2 197 |
| 17 | The Orchestra as Accompanist | 569 | adler2 256 |
| 18 | **Preparation of Score and Parts**: score setup 605, preparing parts 611 | 604 | adler2 291 (292, 298) |
| App. A | Ranges of orchestral instruments; names in four languages; terms | 615 | adler2 302 |
| App. B | Bibliography | 626 | adler2 313 |
| — | Index | 633 | adler2 320 |

Pages mostly music examples (class EX): adler1 31, 34, 65, 68, 71, 77-78, 80, 88-104 (scattered), 120, 131, 137-165 (scattered), 187-320 (scattered); adler2 18-54 (most), 96-139 (most), 143-186 (scattered), 202-244 (most), 249-307 (most). See `pages.tsv`.

Most useful for our C-minor first movement:
- Ch. 15 (adler2 146-196): unison-octave tutti, foreground/background, homophonic and polyphonic orchestral texture, with full-score examples (Brahms, Beethoven, Tchaikovsky, Dvořák, etc.). This is the core reference for balance and doubling in tutti and transition passages.
- Ch. 5 and 8 (adler1 125-167, 233-281): string voicing and wind-string combinations, i.e. how to double a melody and keep the accompaniment from covering it.
- Ch. 11 (adler2 14-54): brass as a homophonic choir, brass melody, climactic brass (horn and trombone spacing at a climax).
- Ch. 10 horn section (adler1 299-311): horn ranges, stopped and muted horn, horns in pairs. Useful for C-minor horn writing.
- Ch. 18 (adler2 291-301): score order, part preparation. App. A (adler2 302-312): quick range charts with professional and amateur limits.

## 2. Gould, *Behind Bars: The Definitive Guide to Music Notation* (Faber Music, 2011): EXCERPT ONLY

Elaine Gould. The PDF has 68 pages: front matter, the full contents list, Introduction, **Chapter 1 "Ground Rules" (complete, pp. 3-43)** and **the first part of Chapter 2 "Chords – Dotted notes – Ties" (pp. 45-55 only)**. Everything from p. 56 on is missing, including dynamics and articulation, strings, **score layout (ch. 17)** and **part preparation (ch. 18)**.

- Native text, clean. Examples are engraved images. Their text is fragments.
- Offset: PDF 16 = Part i title, PDF 17 = ch. 1 title (p. 3). **PDF = printed + 14 for pp. 3-43** (PDF 17-57). **PDF = printed + 13 for pp. 45-55** (PDF 58-68).

| Section | Printed | PDF |
|---|---|---|
| Contents (whole book) | — | 7-8 |
| Introduction | xi-xv | 9-13 |
| Ch. 1 Ground Rules: stave, clefs 5-8 | 3 | 17 (19-22) |
| Noteheads, stems, tails | 9-16 | 23-30 |
| Beams | 17-27 | 31-41 |
| Ledger lines, octave signs | 27-34 | 41-48 |
| Rests | 34-38 | 48-52 |
| Rhythmic spacing; spacing of symbols | 39-43 | 53-57 |
| Ch. 2 Chords: chords, adjacent-note chords, unisons, double-stemmed writing | 47-54 | 60-67 |
| Dotted notes (start only) | 55 | 68 |

Useful for us: engraving checks on the LilyPond output. Stem direction and beaming in shared-staff wind parts (a2 and divisi on one staff, double-stemmed writing PDF 66-67), octave-sign rules (PDF 42-48), rest placement in two-part staves, horizontal spacing. Nothing on score layout or parts. For those use MOLA and Adler ch. 18.

## 3. Aldwell & Schachter, *Harmony and Voice Leading*, 3rd edition (Thomson Schirmer, 2003)

Edward Aldwell and Carl Schachter. A scan of the printed book (Epson flatbed, no text layer). OCR'd with Tesseract.

- **Scan problems:** pages are skewed, some are offset in the frame, and many PDF pages include a strip of the facing page. That strip appears as broken words at the start of the OCR text. At least one page is scanned twice (PDF 401 = 403). A few printed pages may be skipped; the printed→PDF offset drifts from +11 to −12. **The scan stops at p. 638 (PDF 626), partway through Appendix I.** Appendix II (score reduction), the index of examples and the subject index are missing.
- OCR: prose is good. Roman-numeral labels and figured-bass figures are often wrong. Check them on the image.
- Unit starts (PDF page, ±1):

| Unit | Title | Printed | PDF |
|---|---|---|---|
| — | Contents, Preface | iii-xiv | 2-12 |
| I | **The Primary Materials and Procedures** | 1 | 13 |
| 1 | Key, Scales, and Modes | 3 | 14 |
| 2 | Intervals | 22 | 33 |
| 3 | Rhythm and Meter | 36 | 47 |
| 4 | Triads and Seventh Chords | 47 | 58 |
| 5 | **Procedures of Four-Part Writing** (chord construction, voice leading) | 63 | 74 |
| II | I-V-I and its elaborations | 81 | (title page not in scan) |
| 6 | I, V, and V7 | 83 | 92 |
| 7 | I6, V6, VII6 | 97 | 106 |
| 8 | Inversions of V7 | 112 | 121 |
| 9 | Leading to V: IV, II, II6 (harmonic syntax) | 125 | 134 |
| 10 | The Cadential 6/4 | 146 | 152 |
| 11 | VI and IV6 | 158 | 163 |
| 12 | Supertonic and Subdominant Seventh Chords | 171 | 176 |
| 13 | Other Uses of IV, IV6, and VI | 191 | 195 |
| 14 | V as a Key Area (tonicization and modulation) | 207 | 211 |
| 15 | III and VII | 226 | 230 |
| III | 5/3, 6/3, 6/4 techniques | 245 | 248 |
| 16 | 5/3-Chord Techniques | 247 | 249 |
| 17 | **Diatonic Sequences** | 262 | 263 |
| 18 | 6/3-Chord Techniques | 290 | 289 |
| 19 | 6/4-Chord Techniques | 305 | 304 |
| IV | Elements of Figuration | 327 | 326 |
| 20 | Melodic Figuration | 329 | 327 |
| 21 | Rhythmic Figuration (suspensions, anticipations, pedal point) | 348 | 346 |
| V | Dissonance and Chromaticism I | 375 | 372 |
| 22 | Leading-Tone Seventh Chords (diminished 7th) | 377 | 373 |
| 23 | **Mixture** | 390 | 386 |
| 24 | Remaining Uses of Seventh Chords | 403 | 398 |
| 25 | Applied V and VII | 422 | 418 |
| 26 | **Diatonic Modulation** (incl. modulation, large-scale motion, form, p. 454) | 448 | 442 |
| VI | Dissonance and Chromaticism II | 469 | ~462 |
| 27 | Seventh Chords with Added Dissonance (9ths, 11ths, 13ths) | 471 | 463 |
| 28 | **The Phrygian II (Neapolitan)** | 490 | 482 |
| 29 | **Augmented Sixth Chords** | 512 | 503 |
| 30 | Other Chromatic Chords (advanced mixture, augmented triads, common-tone dim. 7ths) | 540 | 530 |
| 31 | **Chromatic Voice-Leading Techniques** (parallel/contrary chromaticism, equal divisions of the octave) | 561 | 551 |
| 32 | Chromaticism in Larger Contexts (new modulatory techniques, chromatic tonal areas) | 595 | 584 |
| App. I | Keyboard Progressions (incomplete) | 619 | 607-626 |

Pages mostly music examples: about 140 (see `pages.tsv`). They include most of Appendix I (PDF 608-626) and the first page of most units (each unit opens with a literature example).

Useful for us: the minor-mode chromatic vocabulary of a C-minor Romantic movement. Mixture (Unit 23), the Neapolitan (28), augmented sixths and their use in modulation (29), common-tone diminished sevenths and augmented triads (30), and chromatic sequences and equal division of the octave (31-32) are the tools for development sections and retransitions. Unit 5 and the "Points for Review" at the end of each unit give compact voice-leading rules a critic can apply bar by bar (parallels, doubling the leading tone, cross relations p. 424, PDF 420). Unit 26 covers modulation and its relation to form (second-group key choices).

## 4. Sebesky, *The Contemporary Arranger* (Alfred Publishing, 1974/1979)

Don Sebesky (the filename's "Sedesky" is a misspelling). A scan, OCR'd with Tesseract. Records were part of the original book and are not included.

- **PDF = printed + 9** throughout (PDF 11 = p. 2). Last PDF page is p. 233. It ends mid-sentence in ch. 9, so the final page or pages are probably missing.

| Ch. | Title | Printed | PDF |
|---|---|---|---|
| — | Contents | v | 4 |
| — | Recorded examples list, About the author, Preface | viii-xv | 5-10 |
| 1 | Basics: balance, economy, focus, variety | 2 | 11 |
| 2 | Wind Instruments: trumpet 12, trombone 18, horn 23, tuba 30, brass combinations 32, saxophones 46, clarinets 51, flutes 56, double reeds 61, combining woodwinds 69, brass with woodwinds 74 | 12 | 21 (27, 32, 39, 41, 55, 60, 65, 70, 78, 83) |
| 3 | Strings: violin 104, viola 114, cello 116, bass 117, harp 118, **voicing the strings 124**, combining strings with winds 155 | 102 | 111 (113, 123, 125, 126, 127, 133, 164) |
| 4 | The Rhythm Section (incl. synthesizer, p. 187) | 165 | 174 (196) |
| 5 | Voices | 188 | 197 |
| 6 | Melodic Considerations | 195 | 204 |
| 7 | The Importance of the Lyric | 210 | 219 |
| 8 | **The Recording Studio** (+ glossary p. 227) | 222 | 231 (236) |
| 9 | General Advice | 231 | 240 |

Pages mostly music examples: 1-6, 17-20, 26-27, 45, 48, 55, 84-110 (scattered), 128-172 (scattered), 177-215 (scattered), 227-229.

Useful for us: this is a commercial and studio arranging book, but ch. 1 (balance, economy, focus, variety: a good checklist for clutter) and ch. 3 "Voicing the Strings" and "Combining Strings with Winds" (PDF 133-173) apply to orchestral string writing. Ch. 2's brass and woodwind combination pages show unison and octave blends (flute+oboe, flute+clarinet, etc.). **MIDI/mock-up:** nothing on MIDI (1979). There is one paragraph on the synthesizer (PDF 196). Ch. 8 (PDF 231-239) covers multitrack session planning, microphone separation, overdubbing and remix. That is loosely relevant to how sections should be balanced and panned in a rendering.

## 5. Casanelles, *The Hyperorchestra: Screen Music and Virtual Musical Ensembles* (Palgrave Macmillan / Springer Nature, 2024)

Sergi Casanelles. ISBN 978-3-031-75192-9. Native text, clean.

- Blank versos were removed, so the offset drifts: **ch. 1 PDF = printed + 14; ch. 2 +13; ch. 3 +12; ch. 4 +11; ch. 5-6 +10; ch. 7 +9; references and index +8.**

| Ch. | Title | Printed | PDF |
|---|---|---|---|
| — | Contents | ix-xiii | 8-12 |
| 1 | Introduction (glossary of concepts p. 14) | 1 | 15 (28) |
| Part I | Theoretical and Practical Foundations | 23 | 37 |
| 2 | From Hyperreality to Digital Cinema | 25 | 38 |
| 3 | Conceptualizing the Hyperorchestra | 61 | 73 |
| 4 | **The Digital Tools: MIDI, Virtual Instruments, and Digital Music**. MIDI messages 112, the effect of the mockup 120, sampling techniques 128, layering 134, dynamics layering/crossfading 137, round robin and legato 139, recording locations and sound perspectives 146, classifying virtual instruments 151, reproducing the Western orchestra 167 | 107 | 118 (123, 131, 139, 145, 148, 150, 157, 162, 178) |
| Part II | The Hyperorchestra and Contemporary Screen-Music Aesthetics | 187 | 198 |
| 5 | Hyperorchestral Aesthetic Frameworks (film case studies) | 189 | 199 |
| 6 | **Hyperorchestration: Sonic Strategies**. Spectral orchestration 247, mixing as hyperorchestration 261, acoustic mixing in Mahler's First Symphony 261, combining microphones 271, EQ 275, harmonic density 277, volume and dynamics 280, virtual space design 281, expanding Western orchestration principles 291 | 245 | 255 (257, 271, 271, 281, 285, 287, 290, 291, 301) |
| 7 | Conclusion | 299 | 308 |
| — | References / Index | 303 / 317 | 311 / 325-336 |

Few music examples (mostly prose). EX-class pages are only title pages and the index.

Useful for us: mostly about the mock-up and audio rendering, not the score. Ch. 4 (PDF 131-161): what makes a sample-based orchestral mock-up sound real or fake (dynamic crossfading vs. velocity, round robins, legato transitions, mic positions). Ch. 6 (PDF 271-307): mixing as a part of orchestration, microphone perspective, EQ, reverb and "virtual space", with a short analysis of Mahler 1. It is a useful check when our rendered audio has balance problems that the score does not. It has nothing on traditional voice leading or form.

## 6. Rimsky-Korsakov, *Principles of Orchestration*, with examples drawn from his own works

Nikolay Rimsky-Korsakov, ed. Maximilian Steinberg, English translation Edward Agate. E. F. Kalmus reprint (of the 1912/1922 edition), Internet Archive scan of a UConn library copy. **The filename "principles of form.pdf" is wrong: this is Rimsky-Korsakov's orchestration treatise, not a book on form.** Both volumes are in one PDF: the text and the example scores.

- Text volume: PDF 13-170, **PDF = printed + 18** (p. 1 = PDF 19, p. 152 = PDF 170).
- Examples volume ("Part II, Examples"): PDF 171-504, examples No. 1-312 (full scores from his operas, Scheherazade, Capriccio espagnol, etc.). Example pages are numbered **PDF = printed + 170**. Appendix "Single tutti chords": PDF 505-510. PDF 511-516: blank or cover.
- Text layer: Internet Archive OCR, with odd spaces between words. 57 pages with an empty layer were OCR'd by Tesseract; almost all are score pages, so they contain little.

| Ch. | Title | Printed | PDF |
|---|---|---|---|
| — | Contents | iii-v | 9-11 |
| — | Editor's Preface; Author's prefaces | vii-5 | 13-23 |
| I | General review of orchestral groups (strings 6, woodwind 12, brass 21, plucked/percussion 26-32, **comparison of resonance and combination of tone qualities 33**) | 6 | 24 (30, 39, 44-50, 51) |
| II | **Melody**: strings 36 (unison 39, octaves 40, double/triple octaves 44-45), woodwind 46, brass 53, combined groups 56 | 36 | 54 (57, 58, 62, 64, 71, 74) |
| III | **Harmony**: number of parts and duplication 64, distribution of notes in chords 67, strings 69, woodwind 71, brass 82, combined groups 88 (overlaying, crossing, enclosure 90; strings and wind 94; three groups 95) | 63 | 81 (82, 85, 87, 89, 100, 106, 108, 112, 113) |
| IV | **Composition of the orchestra**: full tutti 101, limits of range 106, transfer of phrases 107, sf-p chords 111, crescendo/diminuendo 112 | 97 | 115 (119, 124, 125, 129, 130) |
| V | Voice with orchestra; stage band | 119 | 137 |
| VI | Voices (supplementary) | 132 | 150 |
| — | Examples No. 1-312 | 1-334 | 173-504 |
| — | Appendix: single tutti chords | — | 505-510 |

Example number to PDF page (first page of each example): 1→173, 10→185, 20→197, 30→207, 40→~218, 50→~224, 60→231, 70→242, 80→253, 90→265, 100→~278, 110→285, 120→292, 130→305, 140→315, 150→322, 160→332, 170→~340, 180→349, 190→357, 200→364, 210→377, 220→389, 230→401, 240→408, 250→416, 260→427, 270→437, 280→447, 290→467, 300→486, 310→500, 312→502. The text cites examples by number. To find example 123: `grep -nE "^ *N[?9°o0]? ?123\." rimsky-principles.txt` (the OCR writes "No." as "N?", "N9" and similar).

Useful for us: chapters II and III are the classic rules for **doubling and chord spacing**: which instruments double a melody well at the unison or octave, how to distribute and double chord tones across strings, woodwind and brass, and the "overlaying, crossing and enclosure" methods of interlocking winds and brass (PDF 106-114). Ch. IV on tutti, sf-p and crescendo (PDF 119-136) applies to exposition climaxes. The appendix of tutti chords (PDF 505-510) shows exact full-orchestra chord spacings to copy for big C-minor tutti chords. View the example pages as images.

## 7. MOLA, *Guidelines for Music Preparation* (2017 revision)

Major Orchestra Librarians' Association, Publications Committee (first edition 1993, revised 2001 and 2017). 16 pages. **PDF = printed + 2.**

| Section | PDF |
|---|---|
| Foreword | 3 |
| The Performance Material: full score (instrument names, tempo marks, bar numbers, rehearsal letters, percussion, score order) | 4 |
| Parts (transposition, cautionary clefs/keys, bar numbers, cues, tacet, doublings, horn/timpani accidentals) | 5 |
| Cover and front matter (title, duration, instrumentation page) | 6 |
| Formatting (double-sided, staff sizes: score ≥ 4 mm, parts 7-7.5 mm; page turns; margins; staves per page; one wind instrument per part) | 7 |
| Proofreading; paper and binding (sizes, weight) | 8 |
| Examples 1-7 (images: score first page, abbreviated names, cautionary signs, cues, doubling changes, barlines, collisions) | 9-11 (view as images) |
| Resources (bibliography) | 12 |
| MOLA publications; committee list | 13, 16 |

Useful for us: the checklist for making the score and parts usable by a real orchestra. Score order and naming, bar numbers and rehearsal marks, cues and multi-rests in parts, page-turn rules, staff sizes. Use it together with Adler ch. 18.

## 8. oct_9_score.pdf: our own score

**Byte-identical (same MD5) to `/mnt/project-files/symphony/mvt1/v120/score.pdf`**: "Symphony No. 1 in C minor, I. Lento — Allegro appassionato, Full score in C — v120", LilyPond 2.24.3, 17 pages, created 2026-10-09 06:43 UTC. Text in `text/oct9-score/` contains only titles, instrument names, tempo and expression words. Use the PDF images or the LilyPond source instead.

---

### Extraction notes

- Native-text pages: `pdftotext -layout`, one file per page. The combined files compress runs of spaces to two spaces for readable grep output. The per-page files keep the full layout.
- OCR: Tesseract 5.3.4, English, 300 dpi grayscale, `--psm 3`, 4 parallel processes. All 626 + 242 pages of the two scanned books were processed without errors.
- Pages with an empty native layer were re-OCR'd: adler1 p273, adler2 p136, mola p1, 9, 10, 11, 16, and 57 rimsky-principles pages (mostly scores). The remaining empty pages are genuinely blank.
- Accuracy figures are rough estimates from reading sample pages, not measured.

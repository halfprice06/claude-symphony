\version "2.24.0"
\language "nederlands"
#(set-global-staff-size 21)
\paper { #(set-paper-size "b4") top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm
  print-first-page-number = ##t bookpart-level-page-numbering = ##t
  % c165: letters and tempo words stacked over a system (e.g. G over Largamente, J over Tempo I, poco sostenuto over poco rit.) sat nearer
  % the system above than their own (B.cl. "poco sostenuto" of 48 under the solo at 32-33, Hn 1 under 13-14): MOLA PDF 8, Ex. 7 (PDF 12),
  % floating markings in extracted parts. The parts pages are half empty, so the systems get more room between them.
  system-system-spacing = #'((basic-distance . 12) (minimum-distance . 8) (padding . 4) (stretchability . 60)) oddHeaderMarkup = \markup \fill-line { "" \unless \on-first-page-of-part \fromproperty #'header:instrument \if \should-print-page-number \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \if \should-print-page-number \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
\include "score-defs.ily"
noBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
% c165: MOLA PDF 5, Ex. 3-4 (PDF 10): a run of rests is one multi-bar rest, split only where the player must see something (letter,
% tempo word, key or metre). LilyPond starts a new multi-bar rest at every skip or rest boundary, so the MIDI-only \mt steps, the
% score's line-break skips and the section joins split rests for no visible reason (Fl 1 53-56 "2 2", 71-76 "4 2", 89-92 "1 1 1 1").
% partMerge drops the MIDI tempo steps and bar checks (the score build checks the bars) and joins adjacent plain skips and plain whole-bar rests; anything printed still splits them.
% The c035 spacing section at 59-60 is kept (the viola part needs it to stay on one page), so rests still break at 59.
#(define (mt-step? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e) (eq? (ly:music-property e 'name) 'PropertySet)
               (eq? (ly:music-property e 'symbol) 'tempoWholesPerMinute)))))
% c225: the part-combiner switches (\partCombineSoloII etc.) mean nothing in a single part, but they split rests too (Cl 1 71-76 printed "4 2")
#(define (pc-switch? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e) (eq? (ly:music-property e 'name) 'PropertySet)
               (eq? (ly:music-property e 'symbol) 'partCombineForced)))))
% c225: MOLA Ex. 4 (PDF 10): the letter at the barline with the tempo word beside it, not stacked over it. A tempo word that follows a
% letter with no music between them is moved right, past the boxed letter, so both sit on one line (MOLA Ex. 7, PDF 12: floating markings).
#(define (beside-letter lst)
   (let loop ((l lst) (after-mark #f) (acc '()))
     (if (null? l) (reverse acc)
         (let* ((m (car l)) (n (ly:music-property m 'name)))
           (cond ((eq? n 'RehearsalMarkEvent) (loop (cdr l) #t (cons m acc)))
                 ((and after-mark (eq? n 'TempoChangeEvent))
                  (loop (cdr l) #f (cons m (cons #{ \once \override Score.MetronomeMark.X-offset = #3.6 \once \override Score.MetronomeMark.outside-staff-horizontal-padding = #0.2 #} acc))))
                 ((memq n '(SkipEvent MultiMeasureRestMusic NoteEvent EventChord RestEvent)) (loop (cdr l) #f (cons m acc)))
                 (else (loop (cdr l) after-mark (cons m acc))))))))
#(define (flat-seq lst)
   (append-map (lambda (m)
                 (cond ((or (mt-step? m) (pc-switch? m) (eq? (ly:music-property m 'name) 'BarCheck)) '())
                       ((eq? (ly:music-property m 'name) 'SequentialMusic)
                        (flat-seq (ly:music-property m 'elements)))
                       (else (list m))))
               lst))
#(define (plain? m kind)
   (and (eq? (ly:music-property m 'name) kind) (null? (ly:music-property m 'articulations))))
#(define (join a b)
   (let* ((len (ly:moment-main (ly:moment-add (ly:music-length a) (ly:music-length b))))
          (c (ly:music-deep-copy a)))
     (ly:music-set-property! c 'duration (ly:make-duration 0 0 (numerator len) (denominator len)))
     c))
#(define (merge-run lst)
   (if (null? lst) '()
       (let loop ((acc (list (car lst))) (rest (cdr lst)))
         (if (null? rest) (reverse acc)
             (let ((a (car acc)) (b (car rest)))
               (if (or (and (memq (ly:music-property a 'name) '(MultiMeasureRestMusic)) (plain? b 'MultiMeasureRestMusic))
                       (and (eq? (ly:music-property a 'name) 'SkipEvent) (plain? b 'SkipEvent)))
                   (loop (cons (join a b) (cdr acc)) (cdr rest))
                   (loop (cons b acc) (cdr rest))))))))
partMerge = #(define-music-function (m) (ly:music?)
  (if (eq? (ly:music-property m 'name) 'SequentialMusic)
      (make-sequential-music (beside-letter (merge-run (flat-seq (ly:music-property m 'elements)))))
      m))
partGlobalPlain = \partMerge \noBreaks \global
partGlobal = << \partGlobalPlain { <>_\markup \small \italic "attacca from movement I" } >>
% c235: harp only: in the short 1-6 multi-rest the attacca text ran across the barline of 7 and under the RH chord (Gould PDF 43: never cut through other symbols); here it takes its own width
partGlobalHarp = << \partGlobalPlain { \once \textLengthOn <>_\markup \small \italic "attacca from movement I" } >>
\addQuote "bassTbnQ" { \removeWithTag #'part \bassTbn }  % c145: without the tag filter the quote held both the score rests and the part-only Vc cue at 58-59 (c135), so it ran two bars late and trombone 1's cue at 61-62 showed B.tbn's A flat2 of 60 (Adler part 2 PDF 299 item 6)
\addQuote "corAnglaisQ" { \removeWithTag #'part \corAnglais }  % c285: without the filter the quote held both the score rest and the part-only B.cl. cue at 31, so it ran a bar late
\addQuote "bassClQ" { \removeWithTag #'score \bassCl }  % c285: unfiltered, bar 8 held both the score B flat1 and the part-only ossia chord (four beats), so every B.cl. cue after bar 8 (Fl 1 at 34-36) ran a quarter late
% c165: the instrument name was printed three times on each first page (running header, title block, piece label); it now appears once
% in the title block and as the running header from page 2 on (MOLA PDF 6: name on the front; PDF 7: name as a header on each subsequent page)
% c135: bookpart-level-page-numbering: every part starts at page 1 on a right-hand page (MOLA PDF 7: odd pages right, even left), so the book can be split into parts
% c135: cues before the entries at 52 and 59-61 (MOLA PDF 5); the quoted parts without their own score/part-only marks
\addQuote "hnOneQ" { \removeWithTag #'part \hnOne }
\addQuote "clOneQ" { \removeWithTag #'part \clOne }  % c285: cue for clarinet 2 at 55-56; the score-tagged rests at 51-52 keep the quote aligned
\addQuote "oboeOneQ" { \removeWithTag #'(score part) \oboeOne }
\addQuote "vcQ" { \removeWithTag #'(score part) \vc }
% c145: tempo words in adjacent rest bars (poco rit. 47, poco sostenuto 48) ran together on one line in Tbn 1 and other parts; they now stack (Adler part 2 PDF 291 item 1: clear and unproblematical)
\layout { indent = 12\mm \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver"
    \override Hairpin.minimum-length = #8 \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods }
  \context { \Score rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.self-alignment-X = #LEFT \override RehearsalMark.outside-staff-padding = #1 \override MetronomeMark.outside-staff-padding = #1
    \override RehearsalMark.outside-staff-horizontal-padding = #1 \override MetronomeMark.outside-staff-horizontal-padding = #1.5 } \context { \Score skipBars = ##t
  \override MultiMeasureRest.expand-limit = #1 } }
% c255: Gould, Behind Bars PDF 34: "Notes spaced very close together horizontally (closer than three spaces) take only a slight angle
% (1/4 or 1/2 space) regardless of the interval." The parts are spaced about two spaces per quaver, so LilyPond's default slopes of 0.6-1.0
% space for falling or rising quaver groups (Cl 1 77 and 81, Vln I/II 29, Vln II 77 and 81, Hn 1 13, Cl 2 72, Vla 42 and 71, harp 53-54,
% Vc 18) were the steep angles PDF 34 shows as wrong. A closely spaced beam steeper than 1/2 space is recomputed with more damping, so the
% quanting still attaches both ends to stave-lines (PDF 20) and keeps the direction of the outside interval (PDF 22). The score is unchanged.
#(define (gould-close-beam grob)
   (let* ((p (beam::place-broken-parts-individually grob))
          (n (length (ly:grob-array->list (ly:grob-object grob 'stems))))
          (xp (ly:grob-property grob 'X-positions)))
     (if (or (< n 2) (not (pair? xp)) (not (pair? p))) p
         (let ((sp (/ (- (cdr xp) (car xp)) (- n 1))))
           (let loop ((p p) (d (ly:grob-property grob 'damping 1)))
             (if (or (>= sp 3.0) (<= (abs (- (cdr p) (car p))) 0.55) (> d 40)) p
                 (begin (ly:grob-set-property! grob 'damping (* 2 d))
                        (loop (beam::place-broken-parts-individually grob) (* 2 d)))))))))
\layout { \context { \Voice \override Beam.positions = #gould-close-beam } }
% c260: MOLA PDF 5: "Numbering each measure should be avoided, except in the case of multi-measure rests, where measure number ranges
% are helpful (e.g., '27-117')". As movement I (v266): a rest of two or more bars prints its bar range, small, above the count.
% The range is read from the rest's bounding columns, so it follows the score's numbering (bar 1 = movement I's tied chord).
#(define (mmr-range-stencil grob)
   (let* ((base (ly:text-interface::print grob))
          (lc (ly:spanner-bound grob LEFT)) (rc (ly:spanner-bound grob RIGHT))
          (ll (ly:grob-property lc 'rhythmic-location #f)) (rl (ly:grob-property rc 'rhythmic-location #f)))
     (if (and (ly:stencil? base) (pair? ll) (pair? rl) (> (- (car rl) (car ll)) 1))
         (ly:stencil-combine-at-edge (ly:stencil-aligned-to base X CENTER) Y UP
           (ly:stencil-aligned-to (grob-interpret-markup grob
             (markup #:fontsize -4 #:normal-text (format #f "~a–~a" (car ll) (- (car rl) 1)))) X CENTER) 0.3)
         base)))
\layout { \context { \Staff \override MultiMeasureRestNumber.stencil = #mmr-range-stencil } }

\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Flute 1" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \fluteOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Flute 2" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \fluteTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Oboe 1" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \oboeOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Oboe 2" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \oboeTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Cor anglais in F" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \partMerge \removeWithTag #'score \corAnglais >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Clarinet 1 in B♭" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes c' << \partGlobal \partMerge \removeWithTag #'score \clOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Clarinet 2 in B♭" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes c' << \partGlobal \partMerge \removeWithTag #'score \clTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Bass clarinet in B♭ (low C)" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes, c' << \partGlobal \partMerge \removeWithTag #'score \bassCl >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Bassoon 1" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \bsnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Bassoon 2" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \bsnTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Contrabassoon" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests \transpose c c' << \partGlobal \partMerge \removeWithTag #'score \cbsn >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Horn 1 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \partMerge \removeWithTag #'score \hnOne >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Horn 2 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \partMerge \removeWithTag #'score \hnTwo >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Horn 3 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \partMerge \removeWithTag #'score \hnThree >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Horn 4 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \partMerge \removeWithTag #'score \hnFour >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trumpet 1 in C" tagline = ##f }
      \markup \vspace #4 \markup \fill-line { \fontsize #6 \bold "Tacet" } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trumpet 2 in C" tagline = ##f }
      \markup \vspace #4 \markup \fill-line { \fontsize #6 \bold "Tacet" } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trumpet 3 in C" tagline = ##f }
      \markup \vspace #4 \markup \fill-line { \fontsize #6 \bold "Tacet" } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trombone 1" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \tbnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trombone 2" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \tbnTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Bass trombone" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \bassTbn >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Tuba" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \tuba >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Timpani" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \timp >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Harp" tagline = ##f }
  \score { \new PianoStaff \with { connectArpeggios = ##t } << \new Staff { \compressMMRests << \partGlobalHarp \partMerge \removeWithTag #'score \harpR { s4*238 \pageBreak s4*21 \break } >> } \new Staff { \clef bass \compressMMRests << \partGlobalPlain \partMerge \removeWithTag #'score \harpL >> } >> \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Violin I" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \vlnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Violin II" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \vlnTwo >> } \layout { } } }
\bookpart { \paper { system-system-spacing.padding = #0.5 bookTitleMarkup = \markup \fill-line { \fontsize #3 \bold \fromproperty #'header:instrument \line { \bold \fromproperty #'header:title \hspace #1 \bold \fromproperty #'header:subtitle } \null } } \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Viola" tagline = ##f }
  \score { \new Staff  { \clef alto \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \vla >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Violoncello" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \vc >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Double bass" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests \transpose c c' << \partGlobal \partMerge \removeWithTag #'score \cb >> } \layout { } } }
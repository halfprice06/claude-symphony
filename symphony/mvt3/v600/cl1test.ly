\version "2.24.0"
% c075 (MOLA PDF 5, 7, 8): one A4 part per player, staff 21 pt (7.4 mm), transposed parts (horns, trumpets and timpani without key signature; trumpets since c226, Adler adler1 PDF 297-298), multi-measure rests,
% page turns only in rests of 2+ bars (strings use the normal breaker: the inside player turns; parts that cannot turn early start on page 2, MOLA PDF 6), part-only cues kept, score-only marks removed.
% Build from this directory: lilypond -o parts/ parts-book.ly
\include "parts-head.ily"
stripBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
% c345 (MOLA PDF 8: parts no smaller than A4, larger preferred, JIS B4 "the most common size"; PDF 7: 7.5 mm "the most readable staff size for all instruments",
% at most 8-10 staves a page for flute, violin and tuba, up to twelve for the others): JIS B4 257 x 364 mm, as the parts of movements I, II and III; staff 21.26 pt = 7.5 mm.
\paper { page-breaking = #ly:page-turn-breaking paper-width = 257\mm paper-height = 364\mm max-systems-per-page = 12 top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm indent = 8\mm
  % c525 (MOLA PDF 7: the instrument name is a header on each subsequent page; page 1 already names it under the title): no running header name on a part's first page.
  oddHeaderMarkup = \markup \fill-line { "" \unless \on-first-page \fromproperty #'header:instrument \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \fromproperty #'page:page-number-string \unless \on-first-page \fromproperty #'header:instrument "" } }
% c135 (MOLA PDF 5: in parts, multi-measure rests carry bar-number ranges, e.g. "27-117"; Example 3, PDF 10: "9 - 11" under the numbered rest): every rest of two or more bars prints its first and last bar below the staff.
#(define (mmr-with-range grob)
  (let* ((st (ly:multi-measure-rest::print grob))
         (n (ly:grob-property grob 'measure-count 1))
         (col (ly:spanner-bound grob LEFT))
         (loc (and (ly:grob? col) (ly:grob-property col 'rhythmic-location #f))))
    (if (and (ly:stencil? st) (> n 1) (pair? loc))
        (let* ((first (car loc))
               (txt (grob-interpret-markup grob (markup #:fontsize -2 (format #f "~a–~a" first (+ first n -1)))))
               (xc (interval-center (ly:stencil-extent st X)))
               (txt (ly:stencil-translate-axis txt (- xc (interval-center (ly:stencil-extent txt X))) X))
               (txt (ly:stencil-translate-axis txt (- -3.6 (cdr (ly:stencil-extent txt Y))) Y)))
          (ly:stencil-add st txt))
        st)))
% c165 (MOLA PDF 8 and Example 7, PDF 12: extracted parts must be proofread for colliding marks): the range under a numbered rest was drawn outside the rest's
% height, so the vertical spacing did not see it and the next system's rehearsal letters and tempo marks were set on top of it (Cor anglais 7-10 under E, 43-48 under G,
% 115-122 under Tempo I; Flute 1 135-142 under K). The rest's height now includes the range, so systems are spaced to clear it.
#(define (mmr-height-with-range grob)
  (let ((e (ly:multi-measure-rest::height grob)))
    (if (> (ly:grob-property grob 'measure-count 1) 1) (cons (min (car e) -5.0) (cdr e)) e)))
% c315 (MOLA PDF 5, Example 4 PDF 10: letter and tempo word on one line, see global.ily): layout follow-ups, parts only. The percussion part's combined letter + tempo marks take
% horizontal space like its tempo marks (c195), with two spaces after them, so "R Più allegro" stays inside the margin and "P Maestoso" clears the cymbals' fff at 223; its system padding is 0.5 (ten systems on its one page). Timpani padding 0.5 and cor anglais 0.2
% keep their page counts (2 and 1) without compression; Flute 2 keeps its two pages with a fixed turn in the rest 187-198, as in v315.
\layout { #(layout-set-staff-size 21.26) \context { \Staff \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Staff \consists "Page_turn_engraver" \override DynamicTextSpanner.before-line-breaking = #c405-broken-cresc } \context { \DrumStaff \consists "Page_turn_engraver" \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Score skipBars = ##t minimumPageTurnLength = #(ly:make-moment 2/1) \override MultiMeasureRest.expand-limit = #1 rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.font-size = #2 } }
% c315 (MOLA PDF 6: the front of each part carries the full title as printed in a concert programme): the parts' title gains "in C minor", as on the score.
\book { \bookOutputName "part-clOne"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Clarinet 1 in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes \transpose bes c' { \mergeRests \removeWithTag #'score \clOne } } >> \layout { } } }

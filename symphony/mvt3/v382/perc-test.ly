\version "2.24.0"
% c075 (MOLA PDF 5, 7, 8): one A4 part per player, staff 21 pt (7.4 mm), transposed parts (horns, trumpets and timpani without key signature; trumpets since c226, Adler adler1 PDF 297-298), multi-measure rests,
% page turns only in rests of 2+ bars (strings use the normal breaker: the inside player turns; parts that cannot turn early start on page 2, MOLA PDF 6), part-only cues kept, score-only marks removed.
% Build from this directory: lilypond -o parts/ parts-book.ly
\include "parts-head.ily"
stripBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
\paper { page-breaking = #ly:page-turn-breaking #(set-paper-size "a4") top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm indent = 8\mm
  oddHeaderMarkup = \markup \fill-line { "" \fromproperty #'header:instrument \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
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
\layout { #(layout-set-staff-size 21) \context { \Staff \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Staff \consists "Page_turn_engraver" } \context { \DrumStaff \consists "Page_turn_engraver" \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Score skipBars = ##t minimumPageTurnLength = #(ly:make-moment 2/1) \override MultiMeasureRest.expand-limit = #1 rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.font-size = #2 } }
% c195 (MOLA PDF 8: marks must not be set over one another or read as belonging to another bar): the cor anglais' single page was compressed by 10 staff-spaces (fixed by the joined rests 128-142 in global.ily);
% its 205 "poco a poco più animato" stood above "Tempo I" of 199 and hung under its solo at 183-184. A line break before 205 puts it over its own rest; still one page.
% c195 (MOLA PDF 6: a part that cannot be read from one page starts on page 2, so its two pages face each other and need no turn; Gould PDF 31-41 and MOLA PDF 8: no marks set over notes or other marks): since c187's doubling at 27-34 the
% bass clarinet's single page was over-full by 20.5 staff-spaces and LilyPond compressed it (letters D, E, J and N on the notes, tempo texts under the wrong system). Now two facing pages (2-3), break before K (151).
% c195: Tpt 1 and Tpt 3 system padding 0.5 (as Flute 2 and cor anglais): the joined rests 128-134 and 135-142 (global.ily) changed their page breaks and left page 1 over-full by 0.0-0.2 staff-spaces.
% c165 (MOLA PDF 7: a page turn is best at the end of a multi-measure rest, otherwise in rest or an unexposed passage): the free breaker turned Violin I's page at 78|79,
% inside F2's first violin statement (the dotted peak at 78-79), and at 213|214 inside theme B's recall. Pages 1 and 3 now end with the 16-bar rests 51-66 and
% 171-186 (pages 2-3 and 4-5 face each other, MOLA PDF 7: odd pages on the right), so neither turn costs a note. Five pages instead of four;
% page 4 ends at 234 (not a turn) so it is not over-full.
% c165 (MOLA PDF 7): the cellos' first turn fell at 72|73, inside their F2 counter-melody (67-82); it now falls after the pizzicato bar 66 (three beats of rest).
% c255 (MOLA PDF 7: a page turn falls in a rest or an unexposed passage, considering the playing technique; PDF 5: odd pages on the right): Violin II, viola, cello and double bass now turn
% where Violin I turns, in the rests at 66 (pizz. -> arco at 67) and after 186 (before M), instead of inside music: viola 191|192 (F2 tune, A flat), Violin II 213|214 (theme B episode, f),
% cello 227|228 (chorale bass), double bass 86|87 (closing group, f) and 249|250 (hammered eighths, ff). Violin II keeps its first turn at 61|62 (pizz. pp; 1-66 does not fit one page).
% c105: the percussion part takes the score's drum-staff settings (stems and ties up from the single line, score.ly), so the 279 cymbal quarter no longer hangs below the line
% c195 (MOLA PDF 8: marks must not be set over one another or read as belonging to another bar): in the percussion part the rests are short, so the tempo texts at 205 (poco a poco più animato) and 243/247 were stacked above
% the earlier tempo marks and hung under the previous system. Tempo marks now take horizontal space (as \markLengthOn), so each stands over its own bar; still one page.
% c255 (MOLA PDF 5: a notation key at the head of the percussion part; PDF 6: name the instruments and the number of players): the one-line stave carries two players,
% so the part says which mark is which and that the written length is the length of the sound (223 let ring a bar, 278 tied into 279 and damped on beat 2), as the score's staff name already says "(2 players)".
\book { \bookOutputName "part-perc" \header { title = "Symphony No. 1 — IV. Finale" instrument = "Cymbals, Bass drum (2 players)" tagline = ##f
    piece = \markup \normal-text \small \column { \line { "Notation key:" \musicglyph "noteheads.s2xcircle" "above the line = crash cymbals (pair);" \musicglyph "noteheads.s2" "below the line = bass drum." }
      \line { "Each stroke rings for its written length and is damped at its end." } } }
  \score { \new DrumStaff \with { \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override Tie.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 1) (bassdrum default #f -1))) } << \mergeRests \removeWithTag #'score \global { \mergeRests \removeWithTag #'score \perc } >> \layout { \context { \Score \override MetronomeMark.extra-spacing-width = #'(0 . 1.0) \override MetronomeMark.extra-spacing-height = #'(-inf.0 . +inf.0) } } } }

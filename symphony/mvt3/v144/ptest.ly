\version "2.24.0"
% c075 (MOLA PDF 5, 7, 8): one A4 part per player, staff 21 pt (7.4 mm), transposed parts (horns and timpani without key signature), multi-measure rests,
% page turns only in rests of 2+ bars (strings use the normal breaker: the inside player turns; parts that cannot turn early start on page 2, MOLA PDF 6), part-only cues kept, score-only marks removed.
% Build from this directory: lilypond -o parts/ parts-book.ly
\include "parts-head.ily"
stripBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
\paper { page-breaking = #ly:page-turn-breaking #(set-paper-size "a4") top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm indent = 8\mm
  oddHeaderMarkup = \markup \fill-line { "" \fromproperty #'header:instrument \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
\layout { #(layout-set-staff-size 21) \context { \Staff \consists "Page_turn_engraver" } \context { \DrumStaff \consists "Page_turn_engraver" } \context { \Score skipBars = ##t minimumPageTurnLength = #(ly:make-moment 2/1) \override MultiMeasureRest.expand-limit = #1 rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.font-size = #2 } }
\book { \bookOutputName "part-bsnTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Bassoon 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bsnTwo } >> \layout { } } }
\book { \bookOutputName "part-hnThree"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Horn 3 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnThree } } >> \layout { } } }
\book { \bookOutputName "part-tptOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trumpet 1 in C" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptOne } >> \layout { } } }
\book { \bookOutputName "part-tbnOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trombone 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tbnOne } >> \layout { } } }
\book { \bookOutputName "part-tuba"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Tuba" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tuba } >> \layout { } } }
\book { \bookOutputName "part-vlnOne" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Violin I" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \vlnOne } >> \layout { } } }
\book { \bookOutputName "part-vla" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Viola" tagline = ##f }
  \score { \new Staff \with {  } << { \clef alto \mergeRests \removeWithTag #'score \global } { \clef alto \mergeRests \removeWithTag #'score \vla } >> \layout { } } }
\book { \bookOutputName "part-vc" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Violoncello" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \vc } >> \layout { } } }
\book { \bookOutputName "part-cb" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Double bass" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \transpose c c' { \mergeRests \removeWithTag #'score \global } } { \clef bass \transposition c \transpose c c' { \mergeRests \removeWithTag #'score \cb } } >> \layout { } } }
% c105: the percussion part takes the score's drum-staff settings (stems and ties up from the single line, score.ly), so the 279 cymbal quarter no longer hangs below the line

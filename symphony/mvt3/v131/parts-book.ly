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
\book { \bookOutputName "part-fluteOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Flute 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \fluteOne } >> \layout { } } }
\book { \bookOutputName "part-fluteTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Flute 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \fluteTwo } >> \layout { } } }
\book { \bookOutputName "part-oboeOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Oboe 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \oboeOne } >> \layout { } } }
\book { \bookOutputName "part-oboeTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Oboe 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \oboeTwo } >> \layout { } } }
\book { \bookOutputName "part-corAnglais"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Cor anglais in F" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \corAnglais } } >> \layout { } } }
\book { \bookOutputName "part-clOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Clarinet 1 in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes \transpose bes c' { \mergeRests \removeWithTag #'score \clOne } } >> \layout { } } }
\book { \bookOutputName "part-clTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Clarinet 2 in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes \transpose bes c' { \mergeRests \removeWithTag #'score \clTwo } } >> \layout { } } }
\book { \bookOutputName "part-bassCl"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Bass clarinet in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c'' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes, \transpose bes c'' { \mergeRests \removeWithTag #'score \bassCl } } >> \layout { } } }
\book { \bookOutputName "part-bsnOne" \paper { first-page-number = 2 } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Bassoon 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bsnOne } >> \layout { } } }
\book { \bookOutputName "part-bsnTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Bassoon 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bsnTwo } >> \layout { } } }
\book { \bookOutputName "part-cbsn"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Contrabassoon" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \transpose c c' { \mergeRests \removeWithTag #'score \global } } { \clef bass \transposition c \transpose c c' { \mergeRests \removeWithTag #'score \cbsn } } >> \layout { } } }
\book { \bookOutputName "part-hnOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Horn 1 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnOne } } >> \layout { } } }
\book { \bookOutputName "part-hnTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Horn 2 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnTwo } } >> \layout { } } }
\book { \bookOutputName "part-hnThree"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Horn 3 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnThree } } >> \layout { } } }
\book { \bookOutputName "part-hnFour"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Horn 4 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnFour } } >> \layout { } } }
\book { \bookOutputName "part-tptOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trumpet 1 in C" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptOne } >> \layout { } } }
\book { \bookOutputName "part-tptTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trumpet 2 in C" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptTwo } >> \layout { } } }
\book { \bookOutputName "part-tptThree"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trumpet 3 in C" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptThree } >> \layout { } } }
\book { \bookOutputName "part-tbnOne"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trombone 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tbnOne } >> \layout { } } }
\book { \bookOutputName "part-tbnTwo"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Trombone 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tbnTwo } >> \layout { } } }
\book { \bookOutputName "part-bassTbn"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Bass trombone" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bassTbn } >> \layout { } } }
\book { \bookOutputName "part-tuba"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Tuba" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tuba } >> \layout { } } }
\book { \bookOutputName "part-timp"  \header { title = "Symphony No. 1 — IV. Finale" instrument = "Timpani" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \timp } >> \layout { } } }
\book { \bookOutputName "part-vlnOne" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Violin I" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \vlnOne } >> \layout { } } }
\book { \bookOutputName "part-vlnTwo" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Violin II" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \vlnTwo } >> \layout { } } }
\book { \bookOutputName "part-vla" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Viola" tagline = ##f }
  \score { \new Staff \with {  } << { \clef alto \mergeRests \removeWithTag #'score \global } { \clef alto \mergeRests \removeWithTag #'score \vla } >> \layout { } } }
\book { \bookOutputName "part-vc" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Violoncello" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \vc } >> \layout { } } }
\book { \bookOutputName "part-cb" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 — IV. Finale" instrument = "Double bass" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \transpose c c' { \mergeRests \removeWithTag #'score \global } } { \clef bass \transposition c \transpose c c' { \mergeRests \removeWithTag #'score \cb } } >> \layout { } } }
% c105: the percussion part takes the score's drum-staff settings (stems and ties up from the single line, score.ly), so the 279 cymbal quarter no longer hangs below the line
\book { \bookOutputName "part-perc" \header { title = "Symphony No. 1 — IV. Finale" instrument = "Cymbals, Bass drum" tagline = ##f }
  \score { \new DrumStaff \with { \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override Tie.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 1) (bassdrum default #f -1))) } << \mergeRests \removeWithTag #'score \global { \mergeRests \removeWithTag #'score \perc } >> \layout { } } }
\book { \bookOutputName "part-harp" \header { title = "Symphony No. 1 — IV. Finale" instrument = "Harp" tagline = ##f }
  \score { \new PianoStaff << \new Staff << \mergeRests \removeWithTag #'score \global { \mergeRests \removeWithTag #'score \harpR } >> \new Staff << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \harpL } >> >> \layout { } } }

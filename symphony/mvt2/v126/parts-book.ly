\version "2.24.0"
\language "nederlands"
#(set-global-staff-size 21)
\paper { #(set-paper-size "b4") top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm
  print-first-page-number = ##t oddHeaderMarkup = \markup \fill-line { "" \fromproperty #'header:instrument \if \should-print-page-number \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \if \should-print-page-number \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
\include "score-defs.ily"
noBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
partGlobalPlain = \noBreaks \global
partGlobal = << \partGlobalPlain { <>_\markup \small \italic "attacca from movement I" } >>
\addQuote "bassTbnQ" { \bassTbn }
\addQuote "corAnglaisQ" { \corAnglais }
\addQuote "bassClQ" { \bassCl }
\layout { indent = 12\mm \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver"
    \override Hairpin.minimum-length = #5 \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods }
  \context { \Score \override RehearsalMark.outside-staff-padding = #1 \override MetronomeMark.outside-staff-padding = #1
    \override RehearsalMark.outside-staff-horizontal-padding = #1 } \context { \Score skipBars = ##t
  \override MultiMeasureRest.expand-limit = #1 } }

\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Flute 1" piece = "Flute 1" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \fluteOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Flute 2" piece = "Flute 2" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \fluteTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Oboe 1" piece = "Oboe 1" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \oboeOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Oboe 2" piece = "Oboe 2" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \oboeTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Cor anglais in F" piece = "Cor anglais in F" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \removeWithTag #'score \corAnglais >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Clarinet 1 in B♭" piece = "Clarinet 1 in B♭" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes c' << \partGlobal \removeWithTag #'score \clOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Clarinet 2 in B♭" piece = "Clarinet 2 in B♭" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes c' << \partGlobal \removeWithTag #'score \clTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Bass clarinet in B♭" piece = "Bass clarinet in B♭" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests \transpose bes, c' << \partGlobal \removeWithTag #'score \bassCl >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Bassoon 1" piece = "Bassoon 1" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \bsnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Bassoon 2" piece = "Bassoon 2" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \bsnTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Contrabassoon" piece = "Contrabassoon" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests \transpose c c' << \partGlobal \removeWithTag #'score \cbsn >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Horn 1 in F" piece = "Horn 1 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \removeWithTag #'score \hnOne >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Horn 2 in F" piece = "Horn 2 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \removeWithTag #'score \hnTwo >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Horn 3 in F" piece = "Horn 3 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \removeWithTag #'score \hnThree >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Horn 4 in F" piece = "Horn 4 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef treble \compressMMRests \transpose f c' << { \transposition f } << \partGlobal \removeWithTag #'score \hnFour >> >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Trombone 1" piece = "Trombone 1" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \tbnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Trombone 2" piece = "Trombone 2" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \tbnTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Bass trombone" piece = "Bass trombone" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \bassTbn >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Tuba" piece = "Tuba" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \tuba >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Timpani" piece = "Timpani" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \timp >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Violin I" piece = "Violin I" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \vlnOne >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Violin II" piece = "Violin II" tagline = ##f }
  \score { \new Staff  { \clef treble \compressMMRests << \partGlobal \removeWithTag #'score \vlnTwo >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Viola" piece = "Viola" tagline = ##f }
  \score { \new Staff  { \clef alto \compressMMRests << \partGlobal \removeWithTag #'score \vla >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Violoncello" piece = "Violoncello" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests << \partGlobal \removeWithTag #'score \vc >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Double bass" piece = "Double bass" tagline = ##f }
  \score { \new Staff  { \clef bass \compressMMRests \transpose c c' << \partGlobal \removeWithTag #'score \cb >> } \layout { } } }
\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Harp" piece = "Harp" tagline = ##f }
  \score { \new PianoStaff \with { connectArpeggios = ##t } << \new Staff { \compressMMRests << \partGlobal \removeWithTag #'score \harpR { s4*238 \pageBreak } >> } \new Staff { \clef bass \compressMMRests << \partGlobalPlain \removeWithTag #'score \harpL >> } >> \layout { } } }
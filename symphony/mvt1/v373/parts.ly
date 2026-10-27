\version "2.24.0"
\language "nederlands"
% c185: instrumental parts, one PDF per player (MOLA Guidelines PDF 5-8). Build (after build.sh, which regenerates parts.ily):
%   cd <version-dir> && mkdir -p partsout && lilypond -dno-point-and-click -o partsout/parts parts.ly
% gives partsout/parts-NN-<instrument>.pdf. PARTS_AUDIT=1 in the environment adds a proofreading log (see parts-lib.ily). The full score is still score.ly; this file changes nothing in it.
% Generated from the same single-player variables as the score (parts.ily), so every player has his own dynamics.

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  tagline = ##f
}
#(set-global-staff-size 20.5) % 7.2 mm staff (MOLA PDF 7: 7.0-7.5 mm for parts)
\paper {
  % B4 (JIS), "the most common size" for parts (MOLA PDF 8; A4 is the minimum)
  paper-width = 257\mm
  paper-height = 364\mm
  top-margin = 20\mm % c265: MOLA PDF 7, a 20 mm margin all round the image area (was 15 mm)
  bottom-margin = 20\mm
  left-margin = 20\mm
  right-margin = 20\mm
  ragged-last-bottom = ##t
  max-systems-per-page = 12 % MOLA PDF 7: up to twelve staves per page
  % MOLA PDF 7: page turns in rests. Page breaks after odd pages (the turns) are allowed only where the
  % Page_turn_engraver found a rest of at least minimumPageTurnLength; breaks after even pages fall anywhere.
  page-breaking = #ly:page-turn-breaking
  print-first-page-number = ##t
  % default LilyPond headers: page number top right on odd pages, top left on even; instrument name from page 2 (MOLA PDF 7)
}

sec = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))
secDrum = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))

\include "global.ily"
% Parts-only redefinitions, read before the sections so the section variables pick them up:
soloStemsOn = {}   % stem-direction switches for the shared staff
soloStemsOff = {}
pedAflat = \markup \null   % harp pedal diagrams: score only (MOLA PDF 5)
pedNat = \markup \null
pedBflatAflat = \markup \null
\include "sections/intro.ily"
\include "sections/tOne.ily"
\include "sections/trans.ily"
\include "sections/tTwo.ily"
\include "sections/clos.ily"
\include "sections/dev.ily"
\include "sections/recOne.ily"
\include "sections/recTwo.ily"
\include "sections/coda.ily"
\include "parts.ily"
\include "parts-lib.ily"
\include "parts-clefs.ily"

% Cue sources (MOLA PDF 5: cues in long rests, in the reader's key; LilyPond transposes them by instrumentTransposition)
\addQuote "cueVla" { \vla }
\addQuote "cueVc" { \vc }
% c295: the cello an octave down, so that in the contrabassoon part (instrumentTransposition an octave below) the cue prints at the
% cellos' own written pitch: E-flat2-C4 at 67-68 instead of E-flat3-C5 with five ledger lines (MOLA PDF 5: cues "audible and obvious").
\addQuote "cueVcLow" { \transpose c c, \vc }
\addQuote "cueObOne" { \oboeOne }
\addQuote "cueClOne" { \clOne }
\addQuote "cueHnOne" { \hnOne }
\addQuote "cueVlnOne" { \vlnOne }
% c365: octave-shifted Vln I for the 94-95 cue before the entries at 96 (Cl 1, Hn 1-2, Tbn 1, B.tbn, Cbsn: 12 bars rest, no letter between E and F; Adler adler2 PDF 299 item 6, Ex. XVIII-7)
\addQuote "cueVlnOneLow" { \transpose c c, \vlnOne }
\addQuote "cueVlnOneLowII" { \transpose c c,, \vlnOne }
\addQuote "cueVlnOneLowIII" { \transpose c c,,, \vlnOne }
\addQuote "cueVlnTwo" { \vlnTwo } % c295
\addQuote "cueFlOne" { \fluteOne }
\addQuote "cueTimp" { \timp }
\addQuote "cueTimpHigh" { \transpose c c' \timp } % c295

% c200: "attacca" at the end of every part, not only Vln I: the five tied parts (Vln I, Vln II, Vla, Vc, Hn 3), Hn 4's relief of
% Hn 3 at movement II bar 1 and the timpani tuning all run straight into movement II (MOLA PDF 5: instructions that govern the
% performance go in all parts, even in rests; PDF 7: players need time to change parts). Vln I's own mark is tagged 'score in coda.ily.
partGlobalPlain = \partGlobalOf \global % harp LH: the RH staff already carries the end mark
partGlobal = << \partGlobalOf \global { \skip 1*182 \textEndMark \markup \italic "attacca" } >>

\layout {
  \context { \Score
    skipBars = ##t
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #2
    \override MultiMeasureRest.expand-limit = #1
    \override MultiMeasureRest.minimum-length = #14 % room for the tempo words and rehearsal letters that fall in rests
    \override MultiMeasureRest.stencil = #mmr-with-range % c265: bar range under the rest (MOLA PDF 5, Ex. 3 PDF 10)
    % c295: the rest's height comes from its own callback, which ignores the range printed under it, so the system below could
    % set a tempo word on top of it (percussion: "largamente" at 160 over "128-130"; MOLA PDF 8 and Ex. 7, PDF 12: collisions).
    % Taking the height from the stencil puts the range into the skyline that spaces the systems.
    \override MultiMeasureRest.Y-extent = #ly:grob::stencil-height
    \override SpacingSpanner.spacing-increment = #1.6 % looser than the score: parts are read at a distance (MOLA PDF 7: avoid over-crowding)
    \override MetronomeMark.padding = #1.5
    \override RehearsalMark.padding = #1.5
    \override Hairpin.minimum-length = #5
    \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods
    \override MultiMeasureRestNumber.font-size = #0
    % = \markLengthOn: tempo words and rehearsal letters take horizontal space, so a tempo word over a short rest
    % does not stack above the previous one or float away from its bar (MOLA PDF 8 and Ex. 7, PDF 12: collisions and floating markings)
    \override MetronomeMark.extra-spacing-width = #'(0 . 1.0)
    \override RehearsalMark.extra-spacing-width = #'(-0.5 . 0.5)
    \override MetronomeMark.extra-spacing-height = #'(4 . 4)
    \override RehearsalMark.extra-spacing-height = #'(4 . 4)
  }
  % one player per part: dynamics engraved per staff, as in score.ly (a hairpin begun inside a divisi \\\\ passage is ended by the next dynamic)
  \context { \Staff \consists "Page_turn_engraver" }
  \context { \Score minimumPageTurnLength = #(ly:make-moment 2/1) }
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" \consists #gould-middle-line-engraver \override Beam.positions = #gould-beam-positions \override Rest.after-line-breaking = #gould-rest-snap } % c225: Gould PDF 27-28; c235: beam angles, Gould PDF 33-36, as in score.ly
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" }
}

\book {
  \bookOutputSuffix "01-flute-1"
  \header { instrument = "Flute 1" }
  \score {
    \new Staff = "part" \with { \audit "01-flute-1" midiInstrument = "flute"  }
      << \partGlobal \partCues #`(("cueVlnOne" "Vln. I" ,DOWN 62 2) ("cueVlnTwo" "Vln. II" ,DOWN 92 2)) \partClean \fluteOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "02-flute-2"
  \header { instrument = "Flute 2" }
  \score {
    \new Staff = "part" \with { \audit "02-flute-2" midiInstrument = "flute"  }
      << \partGlobal \partCues #`(("cueVlnOne" "Vln. I" ,DOWN 66 2) ("cueVlnOne" "Vln. I" ,DOWN 113 2)) \partClean \fluteTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "03-oboe-1"
  \header { instrument = "Oboe 1" }
  \score {
    \new Staff = "part" \with { \audit "03-oboe-1" midiInstrument = "oboe"  }
      << \partGlobal \partCues #`(("cueClOne" "Cl. 1" ,UP 67 2) ("cueVlnOne" "Vln. I" ,DOWN 113 2)) \partClean \oboeOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "04-oboe-2"
  \header { instrument = "Oboe 2" }
  \score {
    \new Staff = "part" \with { \audit "04-oboe-2" midiInstrument = "oboe"  }
      << \partGlobal \partCues #`(("cueClOne" "Cl. 1" ,UP 67 2) ("cueVlnOne" "Vln. I" ,DOWN 101 2)) \partClean \oboeTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "05-cor-anglais"
  \header { instrument = "Cor anglais in F" }
  \score {
    \new Staff = "part" \with { \audit "05-cor-anglais" midiInstrument = "english horn" instrumentTransposition = #(ly:make-pitch -1 3 0) }
      << \transpose f c' \partGlobal \transpose f c' \partCues #`(("cueClOne" "Cl. 1" ,UP 67 2)) \partClean \corAnglais  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "06-clarinet-1"
  \header { instrument = "Clarinet 1 in B♭" }
  \score {
    \new Staff = "part" \with { \audit "06-clarinet-1" midiInstrument = "clarinet" instrumentTransposition = #(ly:make-pitch -1 6 -1/2) }
      << \transpose bes c' \partGlobal \transpose bes c' \partCues #`(("cueVlnOne" "Vln. I" ,DOWN 94 2)) \partClean \clOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "07-clarinet-2"
  \header { instrument = "Clarinet 2 in B♭" }
  \score {
    \new Staff = "part" \with { \audit "07-clarinet-2" midiInstrument = "clarinet" instrumentTransposition = #(ly:make-pitch -1 6 -1/2) }
      << \transpose bes c' \partGlobal \transpose bes c' \partCues #`(("cueClOne" "Cl. 1" ,UP 67 2) ("cueVlnOne" "Vln. I" ,DOWN 101 2)) \partClean \clTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "08-bass-clarinet"
  \header { instrument = "Bass clarinet in B♭ (with low C)" }
  \score {
    \new Staff = "part" \with { \audit "08-bass-clarinet" midiInstrument = "clarinet" instrumentTransposition = #(ly:make-pitch -2 6 -1/2) }
      << \transpose bes c'' \partGlobal << \bclClefs \transpose bes c'' \partCues #`(("cueVc" "Vc." ,UP 67 2)) \partCleanNoClefs \bassCl >>  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "09-bassoon-1"
  \header { instrument = "Bassoon 1" }
  \score {
    \new Staff = "part" \with { \audit "09-bassoon-1" midiInstrument = "bassoon"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,DOWN 67 2)) \partClean \bsnOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "10-bassoon-2"
  \header { instrument = "Bassoon 2" }
  \score {
    \new Staff = "part" \with { \audit "10-bassoon-2" midiInstrument = "bassoon"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 58 2)) \partClean \bsnTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "11-contrabassoon"
  \header { instrument = "Contrabassoon" }
  \score {
    \new Staff = "part" \with { \audit "11-contrabassoon" midiInstrument = "bassoon" instrumentTransposition = #(ly:make-pitch -1 0 0) }
      << \clef bass \transpose c c' \partGlobal \transpose c c' \partCues #`(("cueVcLow" "Vc." ,UP 67 2) ("cueVlnOneLowIII" "Vln. I" ,UP 94 2)) \partClean \cbsn  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "12-horn-1"
  \header { instrument = "Horn 1 in F" }
  \score {
    \new Staff = "part" \with { \audit "12-horn-1" midiInstrument = "french horn" instrumentTransposition = #(ly:make-pitch -1 3 0) }
      << \transpose f c' \partGlobal \transpose f c' \partCues #`(("cueVlnOneLow" "Vln. I" ,DOWN 94 2)) \partCleanNoClefs \hnOne  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "13-horn-2"
  \header { instrument = "Horn 2 in F" }
  \score {
    \new Staff = "part" \with { \audit "13-horn-2" midiInstrument = "french horn" instrumentTransposition = #(ly:make-pitch -1 3 0) }
      << \transpose f c' \partGlobal \transpose f c' \partCues #`(("cueVc" "Vc." ,DOWN 54 2) ("cueVlnOneLow" "Vln. I" ,DOWN 94 2) ("cueVla" "Vla." ,DOWN 154 2)) \partCleanNoClefs \hnTwo  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "14-horn-3"
  \header { instrument = "Horn 3 in F" }
  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "Horn 3 in F"
    } }
  }
  \pageBreak
  \score {
    \new Staff = "part" \with { \audit "14-horn-3" midiInstrument = "french horn" instrumentTransposition = #(ly:make-pitch -1 3 0) }
      << \transpose f c' \partGlobal \transpose f c' \partCues #`(("cueTimpHigh" "Timp." ,DOWN 179 2)) \partCleanNoClefs \hnThree  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "15-horn-4"
  \header { instrument = "Horn 4 in F" }
  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "Horn 4 in F"
    } }
  }
  \pageBreak
  \score {
    \new Staff = "part" \with { \audit "15-horn-4" midiInstrument = "french horn" instrumentTransposition = #(ly:make-pitch -1 3 0) }
      << \transpose f c' \partGlobal << \hnFourClefs \transpose f c' \partCues #`(("cueTimpHigh" "Timp." ,DOWN 179 2)) \partCleanNoClefs \hnFour >>  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "16-trumpet-1"
  \header { instrument = "Trumpet 1 in C" }
  \score {
    \new Staff = "part" \with { \audit "16-trumpet-1" midiInstrument = "trumpet"  }
      << \partGlobal \partCues #`(("cueVlnOne" "Vln. I" ,UP 67 2) ("cueVlnOne" "Vln. I" ,UP 111 2)) \partClean \tptOne  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "17-trumpet-2"
  \header { instrument = "Trumpet 2 in C" }
  \score {
    \new Staff = "part" \with { \audit "17-trumpet-2" midiInstrument = "trumpet"  }
      << \partGlobal \partCues #`(("cueVlnOne" "Vln. I" ,UP 67 2) ("cueVlnOne" "Vln. I" ,UP 111 2)) \partClean \tptTwo  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "18-trumpet-3"
  \header { instrument = "Trumpet 3 in C" }
  \score {
    \new Staff = "part" \with { \audit "18-trumpet-3" midiInstrument = "trumpet"  }
      << \partGlobal \partCues #`(("cueVlnOne" "Vln. I" ,UP 80 2) ("cueVlnOne" "Vln. I" ,UP 111 2)) \partClean \tptThree  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "19-trombone-1"
  \header { instrument = "Trombone 1" }
  \score {
    \new Staff = "part" \with { \audit "19-trombone-1" midiInstrument = "trombone"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 70 2) ("cueVlnOneLowII" "Vln. I" ,UP 94 2)) \partClean \tbnOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "20-trombone-2"
  \header { instrument = "Trombone 2" }
  \score {
    \new Staff = "part" \with { \audit "20-trombone-2" midiInstrument = "trombone"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 70 2) ("cueVc" "Vc." ,UP 111 2)) \partClean \tbnTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "21-bass-trombone"
  \header { instrument = "Bass trombone" }
  \score {
    \new Staff = "part" \with { \audit "21-bass-trombone" midiInstrument = "trombone"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 70 2) ("cueVlnOneLowII" "Vln. I" ,UP 94 2)) \partClean \bassTbn  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "22-tuba"
  \header { instrument = "Tuba" }
  \score {
    \new Staff = "part" \with { \audit "22-tuba" midiInstrument = "tuba"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 70 2) ("cueVc" "Vc." ,UP 109 2)) \partClean \tuba  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "23-timpani"
  \header { instrument = "Timpani" }
  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "Timpani"
    } }
  }
  \pageBreak
  \score {
    \new Staff = "part" \with { \audit "23-timpani" midiInstrument = "timpani"  }
      << \clef bass \partGlobal \partCues #`(("cueVc" "Vc." ,UP 60 2) ("cueVc" "Vc." ,UP 113 2)) \partClean \timp  >>
    \layout { \context { \Staff \remove "Key_engraver" }  }
  }
}
\book {
  \bookOutputSuffix "26-violin-1"
  \header { instrument = "Violin I" }
  \score {
    \new Staff = "part" \with { \audit "26-violin-1" midiInstrument = "string ensemble 1"  }
      << \partGlobal \partCues #`(("cueVc" "Vc." ,DOWN 53 2) ("cueVlnTwo" "Vln. II" ,DOWN 92 2) ("cueClOne" "Cl. 1" ,DOWN 175 2)) \partClean \vlnOne  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "27-violin-2"
  \header { instrument = "Violin II" }
  \score {
    \new Staff = "part" \with { \audit "27-violin-2" midiInstrument = "string ensemble 1"  }
      << \partGlobal \partClean \vlnTwo  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "28-viola"
  \header { instrument = "Viola" }
  \score {
    \new Staff = "part" \with { \audit "28-viola" midiInstrument = "viola"  }
      << \clef alto \partGlobal \partClean \vla { \skip 1*106 \pageTurn } >>
    \layout {  \context { \Score \override SpacingSpanner.spacing-increment = #1.42 } }
  }
}
\book {
  \bookOutputSuffix "29-violoncello"
  \header { instrument = "Violoncello" }
  \score {
    \new Staff = "part" \with { \audit "29-violoncello" midiInstrument = "cello"  }
      << \clef bass \partGlobal \partClean \vc  >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "30-double-bass"
  \header { instrument = "Double bass" }
  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "Double bass"
    } }
  }
  \pageBreak
  \score {
    \new Staff = "part" \with { \audit "30-double-bass" midiInstrument = "contrabass" instrumentTransposition = #(ly:make-pitch -1 0 0) }
      << \clef bass \transpose c c' \partGlobal \transpose c c' \partClean \cb { \skip 1*174 \pageTurn } >>
    \layout {   }
  }
}
\book {
  \bookOutputSuffix "24-percussion"
  \header { instrument = "Percussion: tam-tam, suspended cymbal" }
  \score {
    \new DrumStaff = "part" \with { \audit "24-percussion" \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 0) (ridecymbal cross #f 0) (tamtam default #f 0))) }
      << \partGlobal \partClean \perc >>
    \layout { }
  }
}
\book {
  \bookOutputSuffix "25-harp"
  \header { instrument = "Harp" }

  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "Harp"
    } }
  }
  \pageBreak
  \score {
    \new PianoStaff = "part" <<
      \new Staff = "Harp RH" \with { \audit "25-harp-rh" } << \partGlobal \partCues #`(("cueClOne" "Cl. 1" ,UP 45 2) ("cueVla" "Vla." ,UP 154 2) ("cueVlnOne" "Vln. I" ,UP 179 2)) \partCleanHarp \harpR >>
      \new Staff = "Harp LH" \with { \audit "25-harp-lh" \override MultiMeasureRest.stencil = #ly:multi-measure-rest::print \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \partGlobalPlain \partCleanHarp \harpL >>
    >>
    \layout { }
  }
}

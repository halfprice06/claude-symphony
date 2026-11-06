\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  % c200: release copy: "draft" dropped, revision number and date kept (MOLA PDF 6: "print date, or revision date")
  % c420: release v421: the cycle stamp "draft vNNN" (c355: to go at the release) becomes the c200 release form, version and date (MOLA PDF 6)
  subsubtitle = \markup \center-column { "Full score in C — draft v488" \small "Contrabassoon and double basses sound an octave lower than written" }
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  system-separator-markup = \slashSeparator
  % c265: MOLA PDF 7, right-hand pages odd. The front-matter page is a right-hand page 1 (number not printed), so the music
  % runs on pages 2-18 (was 1-17 with the front page as page 0, which put odd numbers on left-hand pages in a double-sided print)
  first-page-number = 1
}

% A section variable, or full-bar rests of the section's length if the instrument is silent there.
sec = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))
secDrum = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))

\include "global.ily"
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

\layout {
  \context { \Staff \RemoveEmptyStaves \consists "Merge_rests_engraver" soloText = "1." soloIIText = "2." }
  \context { \DrumStaff \RemoveEmptyStaves }
  % c165: keep the choir bracket when only one staff of a choir is left on a system (default collapse-height 5 hides it); Adler PDF 294: "heavy brackets set off the choirs"
  \context { \StaffGroup \override SystemStartBracket.collapse-height = #1 }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" \consists #gould-middle-line-engraver \override Beam.positions = #gould-beam-positions \override Rest.after-line-breaking = #gould-rest-snap } % c225: Gould PDF 27-28; c235: beam angles, Gould PDF 33-36
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" }
  \context { \Score \remove "Bar_number_engraver"
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #3
    \override BarNumber.break-visibility = ##(#f #t #t)
    \override BarNumber.font-size = #-1
    \override BarNumber.padding = #2
    barNumberVisibility = #(every-nth-bar-number-visible 1)
  }
}

pc = #(define-music-function (a b) (ly:music? ly:music?) #{ \partCombine #a #b #})
% c185: material tagged 'part (cues, part-only dynamics and labels, the Hn 1 ossia at 106) is for parts.ly only; every
% variable that carries such a tag is passed through \removeWithTag #'part here (C.a., Bsn 1, Hn 1, Hn 4, Tpt 2 (c308), Tbn 2).

% c155: front matter page (MOLA, Guidelines PDF 6: movement title, approximate duration, full instrumentation with keys of
% transposing instruments, percussion list and number of players, explanation of non-standard notation). Music pages stay 1-17.
\bookpart {
  \paper { page-count = 1 }
  \header { subsubtitle = ##f }
  \markup \vspace #6
  % c200: timpani retunings are on the A-flat drum since c176 (trans.ily 34-46, dev.ily 84-111); the C drum stays at C (MOLA PDF 6: percussion list with required notes)
  \markup \fill-line { \fontsize #4 \override #'(baseline-skip . 5) \column {
    % c420: MOLA PDF 6 asks for each movement's duration and the total: I 7:10, II 5:45, III 4:36, IV 7:02 (MIDI, coherence/*.md) = 24:33
    \line { \bold "Duration" " c. 7½ minutes (movement I); the symphony c. 25 minutes" }
    \vspace #1
    \bold "Instrumentation"
    \line { "2 Flutes" }
    \line { "2 Oboes" }
    \line { "Cor anglais in F" }
    \line { "2 Clarinets in B♭" }
    \line { "Bass clarinet in B♭ (with low C)" }
    \line { "2 Bassoons" }
    \line { "Contrabassoon" }
    \vspace #0.5
    \line { "4 Horns in F" }
    \line { "3 Trumpets in C" }
    \line { "2 Trombones" }
    \line { "Bass trombone" }
    \line { "Tuba" }
    \vspace #0.5
    \line { "Timpani (4 drums: G, A♭/B♭/B♮, C, E♭)" }
    \line { "Percussion, 1 player: tam-tam, suspended cymbal" }
    \line { "Harp" }
    \vspace #0.5
    \line { "Strings" }
    \vspace #1
    \bold "Notes"
    \line { "Full score in C: all instruments are written at sounding pitch," }
    \line { "except contrabassoon and double basses, which sound an octave lower than written." }
    \line { "Movement I ends attacca into movement II." }
  } }
}
\bookpart {
  \paper { page-count = 17 }
\score {
  <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl. 1·2" midiInstrument = "flute" }
        << \global \pc \fluteOne \fluteTwo >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob. 1·2" midiInstrument = "oboe" }
        << \global \pc \oboeOne \oboeTwo >>
      \new Staff = "Cor anglais" \with { instrumentName = \markup \center-column { "Cor anglais" "in F" } shortInstrumentName = \markup \center-column { "C.a." "(F)" } midiInstrument = "english horn" }
        << \global \removeWithTag #'part \corAnglais >>
      \new Staff = "Clarinets 1·2" \with { instrumentName = \markup \center-column { "Clarinets 1·2" "in B♭" } shortInstrumentName = \markup \center-column { "Cl. 1·2" "(B♭)" } midiInstrument = "clarinet" }
        << \global \pc \clOne \clTwo >>
      \new Staff = "Bass clarinet" \with { instrumentName = \markup \center-column { "Bass clarinet" "in B♭" \small "(low C)" } shortInstrumentName = \markup \center-column { "B.cl." "(B♭)" } midiInstrument = "clarinet" }
        << \clef bass \global \bassCl >>
      \new Staff = "Bassoons 1·2" \with { instrumentName = "Bassoons 1·2" shortInstrumentName = "Bn. 1·2" midiInstrument = "bassoon" }
        << \clef bass \global \pc \removeWithTag #'part \bsnOne \bsnTwo >>
      \new Staff = "Contrabassoon" \with { instrumentName = "Contrabassoon" shortInstrumentName = "Cbn." midiInstrument = "bassoon" }
        << \clef bass \global \transposition c \transpose c c' \cbsn >>
    >>
    \new StaffGroup <<
      \new Staff = "Horns 1·2" \with { instrumentName = \markup \center-column { "Horns 1·2" "in F" } shortInstrumentName = \markup \center-column { "Hn. 1·2" "in F" } midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnOne \hnTwo >>
      \new Staff = "Horns 3·4" \with { instrumentName = \markup \center-column { "Horns 3·4" "in F" } shortInstrumentName = \markup \center-column { "Hn. 3·4" "in F" } soloText = "3." soloIIText = "4." midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnThree \removeWithTag #'part \hnFour >>
      \new Staff = "Trumpets 1·2" \with { instrumentName = \markup \center-column { "Trumpets 1·2" "in C" } shortInstrumentName = \markup \center-column { "Tpt. 1·2" "in C" } midiInstrument = "trumpet" }
        << \global \pc \tptOne \removeWithTag #'part \tptTwo >>
      \new Staff = "Trumpet 3" \with { instrumentName = \markup \center-column { "Trumpet 3" "in C" } shortInstrumentName = \markup \center-column { "Tpt. 3" "in C" } midiInstrument = "trumpet" }
        << \global \tptThree >>
      \new Staff = "Trombones 1·2" \with { instrumentName = "Trombones 1·2" shortInstrumentName = "Tbn. 1·2" midiInstrument = "trombone" }
        << \clef bass \global \pc \tbnOne \removeWithTag #'part \tbnTwo >>
      \new Staff = "Bass trombone" \with { instrumentName = "Bass trombone" shortInstrumentName = "B.tbn." midiInstrument = "trombone" }
        << \clef bass \global \bassTbn >>
      \new Staff = "Tuba" \with { instrumentName = "Tuba" shortInstrumentName = "Tba." midiInstrument = "tuba" }
        << \clef bass \global \tuba >>
    >>
    % c165: timpani and percussion form one choir with its own bracket (Adler, Study of Orchestration ch. 18, PDF 293 Ex. XVIII-1 and PDF 294)
    % no span bars here: the percussion texts above the one-line stave (122, 159, 160, 175) run across the barline
    \new StaffGroup \with { \remove "Span_bar_engraver" } <<
    % c155: timpani without key signature, accidentals written in (MOLA PDF 5; Ex. 6 PDF 11, Beethoven 9: no key signature on the timpani staff)
    \new Staff = "Timpani" \with { \remove "Key_engraver" instrumentName = "Timpani" shortInstrumentName = "Timp." midiInstrument = "timpani" }
      << \clef bass \global \removeWithTag #'part \timp >>
    % c115: single-line stave for the two unpitched instruments; crossed heads for the cymbals (Gould PDF 19, 26)
    \new DrumStaff \with { \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 0) (ridecymbal cross #f 0) (tamtam default #f 0))) instrumentName = \markup \center-column { "Susp. cymbal" "Tam-tam" } shortInstrumentName = "Cym. T.-t." }
      << \global \removeWithTag #'part \perc >>
    >>
    \new PianoStaff \with { instrumentName = "Harp" shortInstrumentName = "Hp." } <<
      \new Staff = "Harp RH" \with { midiInstrument = "orchestral harp" } << \global \harpR >>
      \new Staff = "Harp LH" \with { midiInstrument = "orchestral harp" \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \global \harpL >>
    >>
    \new StaffGroup <<
      \new Staff = "Violins I" \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" instrumentName = "Violins I" shortInstrumentName = "Vln. I" midiInstrument = "string ensemble 1" }
        << \global \vlnOne >>
      \new Staff = "Violins II" \with { instrumentName = "Violins II" shortInstrumentName = "Vln. II" midiInstrument = "string ensemble 1" }
        << \global \vlnTwo >>
      \new Staff = "Violas" \with { instrumentName = "Violas" shortInstrumentName = "Vla." midiInstrument = "viola" }
        << \clef alto \global \vla >>
      \new Staff = "Violoncellos" \with { instrumentName = "Violoncellos" shortInstrumentName = "Vc." midiInstrument = "cello" }
        << \clef bass \global \vc >>
      \new Staff = "Double basses" \with { \consists "Bar_number_engraver" \override BarNumber.direction = #DOWN \override BarNumber.self-alignment-X = #CENTER \override BarNumber.break-align-symbols = #'(staff-bar) \override BarNumber.break-visibility = ##(#f #t #t) \override BarNumber.font-size = #-1 \override BarNumber.padding = #1 \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #7 \override BarNumber.outside-staff-horizontal-padding = #0.5 instrumentName = "Double basses" shortInstrumentName = "Cb." midiInstrument = "contrabass" }
        << \clef bass \global \transposition c \transpose c c' \cb >>
    >>
  >>
  \layout { }
  \midi { \context { \Score midiChannelMapping = #'instrument
    % Wider top of the dynamic range so the single fff (156) outweighs accented ff chords in the audio.
    % \subP is a markup dynamic ("sub. p"): give it the p volume. sf/fp were unmapped and fell back to the default (0.71, louder than ff).
    dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42)) #f)
      0.42)) }
    % Harp: one set of dynamics for both hands (printed under the LH); the RH staff has none, so its notes played at the default volume.
    \context { \PianoStaff \consists "Dynamic_performer" } }
}
}

\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "III. Scherzo: Allegro vivace"  % c100: the four titles name the movement and its tempo, as I ("Lento — Allegro appassionato"), II ("Adagio") and IV ("Finale: Allegro con fuoco") do
  % c200: release copy: "draft" dropped, version and date kept, as movement I (v221, 12 October 2026) and movement II (v201, 13 October 2026) (MOLA PDF 6: "print date, or revision date"); promote.sh's "draft vNN" sed no longer matches, so this line is final
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  % c155: the separator moved down 2 spaces: on page 3 it was printed over the bar number 59 of the system above (Gould PDF 55: no characters collide)
  system-separator-markup = \markup \translate #'(0 . -2) \slashSeparator
  % c250: page 1 numbered in its upper right corner, as movement I (v266) and movement II (v261) (MOLA PDF 7: right-hand pages odd-numbered in the upper right corner)
  print-first-page-number = ##t
}

% A section variable, or full-bar rests of the section's length if the instrument is silent there.
% mvt2: mixed metre, so the rest length is bars x quarter-beats per bar.
sec = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))
secDrum = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))

% c125: an articulation on the stem side (the second voice of a shared staff, and up-stem chords with scripts above) sat on the
% stem end, touching it (bars 61-62: tenutos in Fl, Ob, Cl, Bn 1-2). Gould, Behind Bars PDF 55: characters at least half a space apart, none colliding.
% Scripts on the notehead side are unchanged; on a stem end they move 0.4 space further out (about 0.6 space clear of the stem).
#(define (stem-side-y-offset grob)
  (let* ((y (ly:side-position-interface::y-aligned-side grob))
         (nc (ly:grob-parent grob X))
         (stem (if (ly:grob? nc) (ly:grob-object nc 'stem) '()))
         (dir (ly:grob-property grob 'direction)))
    (if (and (ly:grob? stem) (>= (ly:grob-property stem 'duration-log 0) 1)
             (eqv? dir (ly:grob-property stem 'direction)))
        (let* ((ref (ly:grob-parent grob Y))
               (se (ly:grob-extent stem ref Y))
               (st (ly:grob-property grob 'stencil))
               (ex (if (ly:stencil? st) (ly:stencil-extent st Y) '(0 . 0)))
               (gap (if (> dir 0) (- (+ y (car ex)) (cdr se)) (- (car se) (+ y (cdr ex))))))
          (if (< gap 0.5)
              (+ y (* dir (if (< (abs y) 2.4) 1.0 (- 0.6 gap))))  ; inside the stave a whole space, so a quantized tenuto stays in a space
              y))
        y)))

% c015/c105 beam callback (Gould PDF 31-37): see beams.ily (c195: shared with the parts)
\include "beams.ily"
\include "stems.ily"  % c095: middle-line stems follow the surrounding stems (Gould PDF 27-28, 60-61)

\include "global.ily"
\include "sections/intro.ily"
\include "sections/sA.ily"
\include "sections/sB.ily"
\include "sections/sC.ily"
\include "sections/link.ily"
\include "sections/tA.ily"
\include "sections/tB.ily"
\include "sections/tC.ily"
\include "sections/retr.ily"
\include "sections/dA.ily"
\include "sections/dB.ily"
\include "sections/dC.ily"
\include "sections/coda.ily"
\include "parts.ily"
\score { <<
 \new Staff \with {midiInstrument="flute"} << \global \removeWithTag #'part \fluteOne >>
 \new Staff \with {midiInstrument="flute"} << \global \removeWithTag #'part \fluteTwo >>
 \new Staff \with {midiInstrument="oboe"} << \global \removeWithTag #'part \oboeOne >>
 \new Staff \with {midiInstrument="oboe"} << \global \removeWithTag #'part \oboeTwo >>
 \new Staff \with {midiInstrument="english horn"} << \global \removeWithTag #'part \corAnglais >>
 \new Staff \with {midiInstrument="clarinet"} << \global \removeWithTag #'part \clOne >>
 \new Staff \with {midiInstrument="clarinet"} << \global \removeWithTag #'part \clTwo >>
 \new Staff \with {midiInstrument="clarinet"} << \global \removeWithTag #'part \bassCl >>
 \new Staff \with {midiInstrument="bassoon"} << \global \removeWithTag #'part \bsnOne >>
 \new Staff \with {midiInstrument="bassoon"} << \global \removeWithTag #'part \bsnTwo >>
 \new Staff \with {midiInstrument="bassoon"} << \global \removeWithTag #'part \cbsn >>
 >> \midi { \context { \Staff \consists "Dynamic_performer" } \context { \Voice \remove "Dynamic_performer" } } }

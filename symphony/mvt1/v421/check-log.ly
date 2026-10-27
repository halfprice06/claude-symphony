\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = \markup \center-column { "Full score in C — draft v165" \small "Contrabassoon and double basses sound an octave lower than written" }
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  system-separator-markup = \slashSeparator
  page-count = 17
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


#(define logport (open-output-file "/tmp/critic-288/notes.log"))
#(define (note-log ctx)
  (let ((evs '()) (dyns '()) (hp '()) (arts '()))
    (make-engraver
     (listeners
      ((note-event engraver ev) (set! evs (cons ev evs)))
      ((articulation-event engraver ev) (set! arts (cons (ly:event-property ev 'articulation-type) arts)))
      ((absolute-dynamic-event engraver ev) (set! dyns (cons (ly:event-property ev 'text) dyns)))
      ((span-dynamic-event engraver ev) (set! hp (cons (format #f "~a~a" (car (ly:event-property ev 'class)) (ly:event-property ev 'span-direction)) hp)))
      ((slur-event engraver ev) (set! hp (cons (if (= (ly:event-property ev 'span-direction) -1) "S(" "S)") hp))))
     ((stop-translation-timestep engraver)
      (let ((now (ly:context-current-moment ctx)))
        (for-each (lambda (ev)
          (let* ((p (ly:event-property ev 'pitch))
                 (arts arts)
                 (tie (any (lambda (a) (eq? (ly:music-property a 'name) 'TieEvent)) (ly:event-property ev 'articulations '()))))
            (format logport "~a\t~a\t~a\t~a\t~a\t~a\t~a\t~a\n" (ly:context-id ctx) (ly:context-property ctx 'currentBarNumber)
              (exact->inexact (ly:moment-main now)) (ly:pitch-semitones p) (exact->inexact (ly:moment-main (ly:duration-length (ly:event-property ev (quote duration)))))
              arts dyns hp)))
          evs)
        (if (and (null? evs) (or (pair? dyns) (pair? hp)))
            (format logport "~a\t~a\t~a\tNA\t0\t()\t~a\t~a\n" (ly:context-id ctx) (ly:context-property ctx 'currentBarNumber) (exact->inexact (ly:moment-main now)) dyns hp))
        (set! evs '()) (set! dyns '()) (set! hp '()) (set! arts '()))))))

#(define (entry-check ctx)
  (let ((last-end #f) (note-now #f) (dyn-now #f) (cresc-now #f) (maxend #f))
    (make-engraver
     (listeners
      ((note-event engraver ev)
       (let* ((now (ly:context-current-moment ctx))
              (len (ly:duration-length (ly:event-property ev 'duration)))
              (e (ly:moment-add now len)))
         (set! note-now #t)
         (if (or (not maxend) (ly:moment<? maxend e)) (set! maxend e))))
      ((absolute-dynamic-event engraver ev) (set! dyn-now #t))
      ((span-dynamic-event engraver ev) (set! cresc-now #t)))
     ((process-music engraver)
      (if note-now
          (let ((now (ly:context-current-moment ctx)))
            (if (and (or (not last-end) (not (ly:moment<? now (ly:moment-add last-end (ly:make-moment 1)))))
                     (not dyn-now))
                (ly:message "ENTRY ~a ~a bar ~a~a" (ly:context-id ctx) (if last-end "after-rest" "first")
                  (ly:context-property ctx 'currentBarNumber) (if cresc-now " (hairpin only)" ""))))))
     ((stop-translation-timestep engraver)
      (if note-now (set! last-end maxend))
      (set! note-now #f) (set! dyn-now #f) (set! cresc-now #f)))))


\score { << \new Staff = "fluteOne" << \global \removeWithTag #'part \fluteOne >>
\new Staff = "fluteTwo" << \global \removeWithTag #'part \fluteTwo >>
\new Staff = "oboeOne" << \global \removeWithTag #'part \oboeOne >>
\new Staff = "oboeTwo" << \global \removeWithTag #'part \oboeTwo >>
\new Staff = "corAnglais" << \global \removeWithTag #'part \corAnglais >>
\new Staff = "clOne" << \global \removeWithTag #'part \clOne >>
\new Staff = "clTwo" << \global \removeWithTag #'part \clTwo >>
\new Staff = "bassCl" << \global \removeWithTag #'part \bassCl >>
\new Staff = "bsnOne" << \global \removeWithTag #'part \bsnOne >>
\new Staff = "bsnTwo" << \global \removeWithTag #'part \bsnTwo >>
\new Staff = "cbsn" << \global \removeWithTag #'part \cbsn >>
\new Staff = "hnOne" << \global \removeWithTag #'part \hnOne >>
\new Staff = "hnTwo" << \global \removeWithTag #'part \hnTwo >>
\new Staff = "hnThree" << \global \removeWithTag #'part \hnThree >>
\new Staff = "hnFour" << \global \removeWithTag #'part \hnFour >>
\new Staff = "tptOne" << \global \removeWithTag #'part \tptOne >>
\new Staff = "tptTwo" << \global \removeWithTag #'part \tptTwo >>
\new Staff = "tptThree" << \global \removeWithTag #'part \tptThree >>
\new Staff = "tbnOne" << \global \removeWithTag #'part \tbnOne >>
\new Staff = "tbnTwo" << \global \removeWithTag #'part \tbnTwo >>
\new Staff = "bassTbn" << \global \removeWithTag #'part \bassTbn >>
\new Staff = "tuba" << \global \removeWithTag #'part \tuba >>
\new Staff = "timp" << \global \removeWithTag #'part \timp >>
\new Staff = "harpR" << \global \removeWithTag #'part \harpR >>
\new Staff = "harpL" << \global \removeWithTag #'part \harpL >>
\new Staff = "vlnOne" << \global \removeWithTag #'part \vlnOne >>
\new Staff = "vlnTwo" << \global \removeWithTag #'part \vlnTwo >>
\new Staff = "vla" << \global \removeWithTag #'part \vla >>
\new Staff = "vc" << \global \removeWithTag #'part \vc >>
\new Staff = "cb" << \global \removeWithTag #'part \cb >> >> \layout { \context { \Staff \consists #entry-check \consists #note-log } } }

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

#(define evport (open-output-file "ev595.txt"))
#(define (art-names ev)
   (let ((arts (ly:event-property ev 'articulations '())))
     (map (lambda (a)
            (let ((n (ly:event-property a 'name #f))
                  (t (ly:event-property a 'articulation-type #f))
                  (cls (car (ly:event-property a 'class '(x)))))
              (cond
               ((memq 'slur-event (ly:event-property a 'class)) (if (= (ly:event-property a 'span-direction) -1) "(" ")"))
               ((memq 'phrasing-slur-event (ly:event-property a 'class)) (if (= (ly:event-property a 'span-direction) -1) "\\(" "\\)"))
               ((memq 'tie-event (ly:event-property a 'class)) "~")
               ((memq 'tremolo-event (ly:event-property a 'class)) (format #f ":~a" (ly:event-property a 'tremolo-type)))
               ((memq 'absolute-dynamic-event (ly:event-property a 'class)) (format #f "\\~a" (ly:event-property a 'text)))
               ((memq 'crescendo-event (ly:event-property a 'class)) (if (= (ly:event-property a 'span-direction) -1) "\\<" "\\!"))
               ((memq 'decrescendo-event (ly:event-property a 'class)) (if (= (ly:event-property a 'span-direction) -1) "\\>" "\\!"))
               ((memq 'text-script-event (ly:event-property a 'class)) (format #f "T[~a]" (markup->string (ly:event-property a 'text ""))))
               ((memq 'text-span-event (ly:event-property a 'class)) (format #f "TS~a" (ly:event-property a 'span-direction)))
               ((memq 'articulation-event (ly:event-property a 'class)) (format #f "a:~a" (or t n)))
               (else (format #f "?~a" cls)))))
          arts)))
#(define (logger ctx)
  (make-engraver
   (listeners
    ((note-event engraver ev)
     (let ((p (ly:event-property ev 'pitch)) (d (ly:event-property ev 'duration)))
       (format evport "~a ~a ~a N ~a ~a ~a\n"
         (ly:context-id (ly:context-find ctx 'Staff))
         (ly:context-property ctx 'currentBarNumber)
         (ly:moment-main (ly:context-property ctx 'measurePosition))
         (ly:pitch-notename p) (+ 60 (ly:pitch-semitones p))
         (ly:moment-main (ly:duration-length d)))
       (for-each (lambda (s) (format evport "~a ~a ~a A ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) s)) (art-names ev))))
    ((rest-event engraver ev)
       (format evport "~a ~a ~a R ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (ly:moment-main (ly:duration-length (ly:event-property ev 'duration)))))
    ((slur-event engraver ev)
       (format evport "~a ~a ~a S ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (ly:event-property ev 'span-direction)))
    ((tremolo-event engraver ev)
       (format evport "~a ~a ~a TR ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (ly:event-property ev 'tremolo-type)))
    ((text-script-event engraver ev)
       (format evport "~a ~a ~a TX ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (markup->string (ly:event-property ev 'text ""))))
    ((articulation-event engraver ev)
       (format evport "~a ~a ~a AR ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (ly:event-property ev 'articulation-type)))
    ((absolute-dynamic-event engraver ev)
       (format evport "~a ~a ~a D ~a\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition)) (ly:event-property ev 'text)))
    ((tie-event engraver ev)
       (format evport "~a ~a ~a TIE\n" (ly:context-id (ly:context-find ctx 'Staff)) (ly:context-property ctx 'currentBarNumber) (ly:moment-main (ly:context-property ctx 'measurePosition))))
    )))
\score { <<
\new Staff = "vlnOne" << \global \removeWithTag #'part \vlnOne >>
\new Staff = "vlnTwo" << \global \removeWithTag #'part \vlnTwo >>
\new Staff = "vla" << \global \removeWithTag #'part \vla >>
\new Staff = "vc" << \global \removeWithTag #'part \vc >>
\new Staff = "cb" << \global \removeWithTag #'part \cb >> >>
\layout { \context { \Voice \consists #logger } } }

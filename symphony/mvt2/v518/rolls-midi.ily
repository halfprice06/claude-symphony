% rolls-midi.ily (critic 360): MIDI-only timpani rolls, for any movement of the symphony.
% LilyPond's Note_performer ignores stem tremolo, so a roll written b,2.:32 plays as ONE stroke held for the note's length,
% and a roll tied over bar lines (b,2.:32~ | b,2.:32~ | ...) as one stroke for the whole chain: the GM timpani sample dies away
% after about a second, so the scherzo's crescendo rolls at 101-103, 205-208 and 301-303 (and 129-130,
% 237-240, 285-286, 332, 336) sound as a single fading stroke in score.midi (articulate.ly is no help:
% it copies the tie onto every stroke, which merges them again).
% \rollStrokes #n music: every note or chord carrying a stem tremolo becomes repeated n-th notes (16 = semiquavers) of the same total length.
% The first stroke keeps the note's dynamics, hairpins and texts; the roll's tie is dropped, so a chain of tied rolls sounds as
% continuous strokes across the bar lines (keeping the tie on the last stroke silenced the stroke on the next downbeat), and a roll
% tied into a plain note (e,2.:32~ | e,4) ends with a stroke on that note, as a timpanist ends a tied roll.
% Use it on the music of a \midi-only \score; the printed score is untouched.
#(define (roll-stroke-copy note dur arts)
   (let ((c (ly:music-deep-copy note)))
     (set! (ly:music-property c 'duration) dur)
     (set! (ly:music-property c 'articulations) arts)
     c))

#(define (roll-plan len n)
   ;; number of strokes and the stroke duration for a roll of length len (a rational) in n-th notes
   (let* ((slen (/ 1 n))
          (count (max 1 (inexact->exact (floor (/ len slen)))))
          (r (/ len (* count slen)))
          (lg (1- (integer-length n))))
     (cons count (if (= r 1) (ly:make-duration lg 0 1) (ly:make-duration lg 0 (numerator r) (denominator r))))))

#(define (roll-name? a . names) (memq (ly:music-property a 'name) names))

rollStrokes = #(define-music-function (n music) (integer? ly:music?)
  (music-map
    (lambda (m)
      (cond
        ;; a single note: b,2.:32
        ((and (eq? (ly:music-property m 'name) 'NoteEvent)
              (any (lambda (a) (roll-name? a 'TremoloEvent)) (ly:music-property m 'articulations)))
         (let* ((arts (ly:music-property m 'articulations))
                (plan (roll-plan (ly:moment-main (ly:duration-length (ly:music-property m 'duration))) n))
                (keep (filter (lambda (a) (not (roll-name? a 'TremoloEvent 'TieEvent))) arts)))
           (make-sequential-music
             (list-tabulate (car plan)
               (lambda (i) (roll-stroke-copy m (cdr plan) (if (= i 0) keep '())))))))
        ;; a chord: <e, b,>2.:32 (the tremolo is one of the chord's elements)
        ((and (eq? (ly:music-property m 'name) 'EventChord)
              (any (lambda (e) (roll-name? e 'TremoloEvent)) (ly:music-property m 'elements)))
         (let* ((els (filter (lambda (e) (not (roll-name? e 'TremoloEvent 'TieEvent))) (ly:music-property m 'elements)))
                (notes (filter (lambda (e) (roll-name? e 'NoteEvent)) els))
                (others (filter (lambda (e) (not (roll-name? e 'NoteEvent))) els))
                (plan (roll-plan (ly:moment-main (ly:duration-length (ly:music-property (car notes) 'duration))) n)))
           (make-sequential-music
             (list-tabulate (car plan)
               (lambda (i)
                 (make-music 'EventChord 'elements
                   (append (map (lambda (nt)
                                  (roll-stroke-copy nt (cdr plan)
                                    (if (= i 0) (filter (lambda (a) (not (roll-name? a 'TieEvent))) (ly:music-property nt 'articulations)) '())))
                                notes)
                           (if (= i 0) others '()))))))))
        (else m)))
    music))

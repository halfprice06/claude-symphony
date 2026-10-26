\version "2.24.0"
% parts-lib.ily (scherzo, adapted from movement I v221, c185): helpers for parts.ly. The full score (score.ly) does not include this file.

% Remove from a single player's music what only makes sense on the shared score staff:
% system and page breaks (score layout), the part-combiner's player labels ("1.", "2.", "a2"),
% overrides that place rests, note columns, breath marks and combine labels around the other player,
% and staff positions of pitched rests (\rest), which were set to clear the other voice.
#(define (combine-label? m)
   (any (lambda (s) (or (equal? m (list bold-markup s))
                        (equal? m (list line-markup (list (list bold-markup s))))))
        '("1." "2." "a2")))
#(define (clean-markup m)
   (cond ((combine-label? m) #f)
         ((and (pair? m) (eq? (car m) line-markup) (pair? (cdr m)) (list? (cadr m)))
          (let ((rest (filter (lambda (x) (not (combine-label? x))) (cadr m))))
            (cond ((null? rest) #f)
                  ((null? (cdr rest)) (car rest))
                  (else (list line-markup rest)))))
         (else m)))
#(define (shared-staff-grob? sym) (memq sym '(Rest MultiMeasureRest NoteColumn CombineTextScript BreathingSign)))
#(define (drop-for-part? m)
   (let ((n (ly:music-property m 'name)))
     (or (memq 'score (ly:music-property m 'tags)) ; \tag #'score material (the \tag #'part alternative stays)
         (memq n '(LineBreakEvent PageBreakEvent PageTurnEvent))
         (and (memq n '(OverrideProperty RevertProperty))
              (shared-staff-grob? (ly:music-property m 'symbol))))))
#(define (part-clean! m extra-drop?)
   (cond ((drop-for-part? m) #f)
         ((extra-drop? m) #f)
         ((eq? (ly:music-property m 'name) 'TextScriptEvent)
          (let ((t (clean-markup (ly:music-property m 'text))))
            (if t (begin (ly:music-set-property! m 'text t) m) #f)))
         (else
          (if (eq? (ly:music-property m 'name) 'RestEvent)
              (ly:music-set-property! m 'pitch '()))
          (let ((es (ly:music-property m 'elements))
                (as (ly:music-property m 'articulations))
                (e (ly:music-property m 'element)))
            (if (pair? es)
                (begin
                  (ly:music-set-property! m 'elements (filter-map (lambda (x) (part-clean! x extra-drop?)) es))
                  (move-rest-dynamics! m)))
            (if (pair? as)
                (ly:music-set-property! m 'articulations (filter-map (lambda (x) (part-clean! x extra-drop?)) as)))
            (if (ly:music? e)
                (ly:music-set-property! m 'element
                  (or (part-clean! e extra-drop?) (make-music 'SequentialMusic 'elements '()))))
            m))))

% A dynamic that the score hangs on a rest (so it lines up with the other player's attack on the shared staff)
% moves to this player's first note after the rest (MOLA PDF 10 Ex. 3; Gould: dynamics belong to the note they affect).
#(define (dyn? a) (eq? (ly:music-property a 'name) 'AbsoluteDynamicEvent))
#(define (first-note m)
   (let ((n (ly:music-property m 'name)))
     (cond ((memq n '(NoteEvent EventChord)) m)
           ((memq n '(RestEvent MultiMeasureRestMusic SkipEvent)) 'stop)
           (else
            (let loop ((es (append (let ((e (ly:music-property m 'element))) (if (ly:music? e) (list e) '()))
                                   (let ((es (ly:music-property m 'elements))) (if (list? es) es '())))))
              (if (null? es) #f
                  (let ((r (first-note (car es))))
                    (if r r (loop (cdr es))))))))))
#(define (move-rest-dynamics! m)
   (let ((es (ly:music-property m 'elements)))
     (if (and (eq? (ly:music-property m 'name) 'SequentialMusic) (pair? es))
         (let loop ((l es) (pending '()))
           (if (pair? l)
               (let* ((x (car l)))
                 (if (pair? pending)
                     (let ((t (first-note x)))
                       (if (ly:music? t)
                           (begin
                             (if (eq? (ly:music-property t 'name) 'EventChord)
                                 (ly:music-set-property! t 'elements (append (ly:music-property t 'elements) pending))
                                 (ly:music-set-property! t 'articulations (append (ly:music-property t 'articulations) pending)))
                             (set! pending '())))))
                 (if (and (eq? (ly:music-property x 'name) 'RestEvent)
                          (any dyn? (ly:music-property x 'articulations)))
                     (begin
                       (set! pending (append pending (filter dyn? (ly:music-property x 'articulations))))
                       (ly:music-set-property! x 'articulations (remove dyn? (ly:music-property x 'articulations)))))
                 (loop (cdr l) pending))))))
   m)

% Neighbouring full-bar rests (R1 | R1, or a section ending in rests followed by one beginning with rests) are
% joined into one multi-measure rest, so the part shows one numbered rest (MOLA PDF 10 Ex. 3-4).
#(define (plain-seq? e)
   (and (eq? (ly:music-property e 'name) 'SequentialMusic) (null? (ly:music-property e 'tags))))
#(define (bare-mmr? e)
   (and (eq? (ly:music-property e 'name) 'MultiMeasureRestMusic)
        (null? (ly:music-property e 'articulations)) (null? (ly:music-property e 'tags))))
% A rest that only ends a hairpin (R1\\! after a diminuendo) may still be joined to the rests after it; the joined rest keeps the \\!.
#(define (hairpin-stop? a)
   (and (memq (ly:music-property a 'name) '(CrescendoEvent DecrescendoEvent))
        (eqv? (ly:music-property a 'span-direction) STOP)))
#(define (stop-only-mmr? e)
   (and (eq? (ly:music-property e 'name) 'MultiMeasureRestMusic) (null? (ly:music-property e 'tags))
        (every hairpin-stop? (ly:music-property e 'articulations))))
#(define (merge-mmrs! m)
   (let ((es (ly:music-property m 'elements)) (e (ly:music-property m 'element)))
     (if (ly:music? e) (merge-mmrs! e))
     (if (pair? es)
         (begin
           (for-each merge-mmrs! es)
           (if (eq? (ly:music-property m 'name) 'SequentialMusic)
               (let* ((flat (remove (lambda (x) (eq? (ly:music-property x 'name) 'BarCheck)) ; bar checks (| in the source) would keep R1 | R1 apart; the score build checks them
                                    (append-map (lambda (x) (if (plain-seq? x) (ly:music-property x 'elements) (list x))) es)))
                      (merged (fold-right
                                (lambda (x acc)
                                  (if (and (stop-only-mmr? x) (pair? acc) (bare-mmr? (car acc)))
                                      (let ((j (mmr-of (+ (ly:moment-main (ly:music-length x))
                                                          (ly:moment-main (ly:music-length (car acc)))))))
                                        (ly:music-set-property! j 'articulations (ly:music-property x 'articulations))
                                        (cons j (cdr acc)))
                                      (cons x acc)))
                                '() flat)))
                 (ly:music-set-property! m 'elements merged)))))
     m))
#(define (mmr-of len) (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 (numerator len) (denominator len))))

partClean = #(define-music-function (m) (ly:music?)
  (merge-mmrs! (part-clean! (ly:music-deep-copy m) (lambda (x) #f))))

% Score staff clef changes (\clef inside a player's variable) are dropped where a part gets its own clef plan.
#(define (clef-change? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e)
               (let ((es (ly:music-property e 'elements)))
                 (and (pair? es)
                      (any (lambda (x) (and (eq? (ly:music-property x 'name) 'PropertySet)
                                            (eq? (ly:music-property x 'symbol) 'clefGlyph))) es)))))))
partCleanNoClefs = #(define-music-function (m) (ly:music?)
  (merge-mmrs! (part-clean! (ly:music-deep-copy m) clef-change?)))

% MOLA (Guidelines PDF 5): "Harp pedaling should be left to the performer and not printed."
% The pedal letters in the score ("G♭", "F♮", "B♮ A♮") are \small markups of note names; drop them from the harp part.
#(define (pedal-letter-markup? m)
   (and (pair? m) (eq? (car m) small-markup) (pair? (cdr m)) (string? (cadr m))
        (or (string-prefix? "Ped." (cadr m))
        (let ((toks (filter (lambda (t) (not (string-null? t))) (string-split (cadr m) #\space))))
          (and (pair? toks)
               (every (lambda (t) (and (= (string-length t) 2)
                                       (memv (string-ref t 0) (string->list "ABCDEFG"))
                                       (memv (string-ref t 1) (string->list "♭♮♯"))))
                      toks))))))
% c135: the starting setting at bar 1 ("set pedals in the pause: ...", a \\small \\line markup) is pedalling too (MOLA PDF 5); the score keeps it (c116).
#(define (pedal-setting-markup? m)
   (and (pair? m) (eq? (car m) small-markup) (pair? (cdr m)) (pair? (cadr m)) (eq? (car (cadr m)) line-markup)
        (pair? (cdr (cadr m))) (list? (cadr (cadr m)))
        (any (lambda (x) (and (pair? x) (eq? (car x) italic-markup) (pair? (cdr x)) (string? (cadr x))
                              (string-prefix? "set pedals" (cadr x))))
             (cadr (cadr m)))))
partCleanHarp = #(define-music-function (m) (ly:music?)
  (merge-mmrs! (part-clean! (ly:music-deep-copy m)
    (lambda (x) (and (memq (ly:music-property x 'name) '(TextScriptEvent MultiMeasureTextEvent))
                     (or (pedal-letter-markup? (ly:music-property x 'text)) (pedal-setting-markup? (ly:music-property x 'text))))))))

% Proofreading aid (MOLA PDF 8: extracted parts are not error-free by themselves). With PARTS_AUDIT=1 in the
% environment, each part logs (a) entries after two or more whole notes' rest that carry no dynamic, and (b) notes
% with more than three ledger lines.
#(define parts-audit? (and (getenv "PARTS_AUDIT") #t))
#(define audit-ledger-limit (if (getenv "PARTS_AUDIT_POS") (string->number (getenv "PARTS_AUDIT_POS")) 11))
#(define (make-audit-engraver name)
   (lambda (context)
     (let ((last-end (ly:make-moment 0)) (step-end #f) (step-dyn #f) (step-note #f) (step-pos '()))
       (make-engraver
        (listeners
         ((note-event engraver ev)
          (let* ((now (ly:context-current-moment context))
                 (d (ly:event-property ev 'duration))
                 (p (ly:event-property ev 'pitch))
                 (mc (ly:context-property context 'middleCPosition 0)))
            (if (and (ly:duration? d) (equal? (ly:moment-grace now) 0))
                (let ((end (ly:moment-add now (ly:duration-length d))))
                  (set! step-note #t)
                  (if (or (not step-end) (ly:moment<? step-end end)) (set! step-end end))))
            (if (ly:pitch? p) (set! step-pos (cons (+ mc (ly:pitch-steps p)) step-pos)))))
         ((absolute-dynamic-event engraver ev) (set! step-dyn 'abs))
         ((span-dynamic-event engraver ev) (if (not step-dyn) (set! step-dyn 'hairpin))))
        ((stop-translation-timestep engraver)
         (let ((now (ly:context-current-moment context))
               (bar (ly:context-property context 'currentBarNumber)))
           (if step-note
               (begin
                 (if (and last-end
                          (not (ly:moment<? (ly:moment-sub now last-end) (ly:make-moment 2))))
                     (if (not (eq? step-dyn 'abs))
                         (ly:message "parts-audit ~a bar ~a: entry after ~a whole notes' rest without a dynamic~a"
                                     name bar (exact->inexact (ly:moment-main (ly:moment-sub now last-end)))
                                     (if step-dyn " (hairpin only)" ""))))
                 (if (and last-end (not (ly:moment<? (ly:moment-sub now last-end) (ly:make-moment 8))))
                     (ly:message "parts-audit ~a bar ~a: entry after a long rest (~a whole notes)" name bar
                                 (exact->inexact (ly:moment-main (ly:moment-sub now last-end)))))
                 (set! last-end step-end)))
           (for-each (lambda (pos)
                       (if (> (abs pos) audit-ledger-limit)
                           (ly:message "parts-audit ~a bar ~a: ~a ledger lines" name bar (quotient (- (abs pos) 4) 2))))
                     step-pos)
           (set! step-note #f) (set! step-end #f) (set! step-dyn #f) (set! step-pos '())))))))
audit = #(define-scheme-function (name) (string?)
  (if parts-audit?
      (ly:make-context-mod (list (list 'consists (make-audit-engraver name))))
      (ly:make-context-mod)))

% The score's \global is a chain of skips cut at its system breaks and MIDI tempo steps (\mt). In a part each cut
% would split a multi-measure rest, so the part's global drops the \mt steps and joins neighbouring skips.
#(define (mt-step? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e) (eq? (ly:music-property e 'name) 'PropertySet)
               (eq? (ly:music-property e 'symbol) 'tempoWholesPerMinute)))))
#(define (skip-len m) (ly:moment-main (ly:music-length m)))
#(define (merge-skips! m)
   (let ((es (ly:music-property m 'elements)))
     (if (pair? es)
         (let loop ((l (remove mt-step? es)) (acc '()))
           (cond ((null? l) (ly:music-set-property! m 'elements (reverse acc)))
                 ((and (eq? (ly:music-property (car l) 'name) 'SkipEvent)
                       (null? (ly:music-property (car l) 'articulations)) ; c075: a skip carrying a fermata (bars 2, 340, 376) stays apart
                       (pair? acc) (eq? (ly:music-property (car acc) 'name) 'SkipEvent)
                       (null? (ly:music-property (car acc) 'articulations)))
                  (let ((len (+ (skip-len (car acc)) (skip-len (car l)))))
                    (loop (cdr l) (cons (make-music 'SkipEvent 'duration
                                          (ly:make-duration 0 0 (numerator len) (denominator len))) (cdr acc)))))
                 (else (merge-skips! (car l)) (loop (cdr l) (cons (car l) acc))))))
     m))
partGlobalOf = #(define-music-function (m) (ly:music?)
  (merge-skips! (part-clean! (ly:music-deep-copy m) mt-step?)))

% Part-only cues in long rests (MOLA PDF 5: "Logical cues are expected during long periods of rest, the cues being
% transposed to the reading key of the instrument. Cues must be audible and obvious"). \partCues takes a list of
% (quote-name label direction first-bar bars) and replaces those bars of a multi-measure rest by a \cueDuring.
% Bars count from 1 in 3/4; the rest that contains the bars is split around them.
#(define (bar-moment b) (* 3/4 (- b 1))) % scherzo: 3/4 throughout
#(define (mmr-of len) (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 (numerator len) (denominator len))))
#(define (make-cue-music name label dir len)
   (make-music 'QuoteMusic
     'element (make-music 'SequentialMusic 'elements
                (list (make-music 'SkipEvent 'duration (ly:make-duration 2 0 0 1)
                        'articulations (list (make-music 'TextScriptEvent 'direction UP
                                               'text (markup #:fontsize -3 label))))
                      (mmr-of len)))
     'quoted-context-type 'CueVoice 'quoted-context-id "cue"
     'quoted-music-name name 'quoted-voice-direction dir))
#(define (insert-cue m t0 start len mk)
   ;; returns (cons new-music done?)
   (let* ((n (ly:music-property m 'name))
          (l (ly:moment-main (ly:music-length m))))
     (cond
      ((or (> t0 start) (< (+ t0 l) (+ start len))) (cons m #f))
      ; c075: a joined rest that only ends a hairpin (R\\! after a diminuendo, e.g. Ob 2 at 201) may take a cue after its first bar
      ((and (eq? n 'MultiMeasureRestMusic)
            (let ((as (ly:music-property m 'articulations)))
              (or (null? as) (and (> start t0) (every hairpin-stop? as)))))
       (cons (make-music 'SequentialMusic 'elements
               (append (if (> start t0)
                           (let ((r (mmr-of (- start t0))))
                             (ly:music-set-property! r 'articulations (ly:music-property m 'articulations))
                             (list r))
                           '())
                       (list (mk len))
                       (if (> (+ t0 l) (+ start len)) (list (mmr-of (- (+ t0 l) start len))) '())))
             #t))
      ((eq? n 'SequentialMusic)
       (let loop ((es (ly:music-property m 'elements)) (t t0) (acc '()))
         (if (null? es)
             (cons m #f)
             (let* ((e (car es)) (el (ly:moment-main (ly:music-length e))) (r (insert-cue e t start len mk)))
               (if (cdr r)
                   (begin (ly:music-set-property! m 'elements (append (reverse acc) (list (car r)) (cdr es)))
                          (cons m #t))
                   (loop (cdr es) (+ t el) (cons e acc)))))))
      ((and (ly:music? (ly:music-property m 'element)) (not (eq? n 'SimultaneousMusic)))
       (let ((r (insert-cue (ly:music-property m 'element) t0 start len mk)))
         (if (cdr r) (ly:music-set-property! m 'element (car r)))
         (cons m (cdr r))))
      (else (cons m #f)))))
partCues = #(define-music-function (cues m) (list? ly:music?)
  (for-each
    (lambda (c)
      (let* ((name (list-ref c 0)) (label (list-ref c 1)) (dir (list-ref c 2))
             (b (list-ref c 3)) (n (list-ref c 4))
             (r (insert-cue m 0 (bar-moment b) (* 3/4 n) (lambda (len) (make-cue-music name label dir len)))))
        (if (not (cdr r)) (ly:warning "partCues: no rest for cue ~a at bar ~a" name b))))
    cues)
  m)

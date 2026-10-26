\version "2.24.0"
% parts-lib.ily (c185): helpers for parts.ly. The full score (score.ly) does not include this file.

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

% c245: the score's octave signs (Vln I 31, 71-72, 121-123) save space between staves; they are not for a playing part:
% Gould, Behind Bars PDF 47: "These octave signs should not be transferred to a playing part, except where absolutely
% necessary"; "In performance material, always use ledger lines in preference to octave signs"; strings read up to five
% ledger lines (the Violin I part reaches A-flat6, four lines, as it already does at pitch at 41 and 160). The harp keeps its
% 8va at 56-59 (six ledger lines; PDF 47: harp may use octave signs more freely), so partCleanHarp does not drop them.
#(define (ottava-event? m) (eq? (ly:music-property m 'name) 'OttavaEvent))
partClean = #(define-music-function (m) (ly:music?)
  (merge-mmrs! (part-clean! (ly:music-deep-copy m) ottava-event?)))

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
  (merge-mmrs! (part-clean! (ly:music-deep-copy m) (lambda (x) (or (clef-change? x) (ottava-event? x))))))

% MOLA (Guidelines PDF 5): "Harp pedaling should be left to the performer and not printed."
% The pedal letters in the score ("G♭", "F♮", "B♮ A♮") are \small markups of note names; drop them from the harp part.
#(define (pedal-letter-markup? m)
   (and (pair? m) (eq? (car m) small-markup) (pair? (cdr m)) (string? (cadr m))
        (let ((toks (filter (lambda (t) (not (string-null? t))) (string-split (cadr m) #\space))))
          (and (pair? toks)
               (every (lambda (t) (and (= (string-length t) 2)
                                       (memv (string-ref t 0) (string->list "ABCDEFG"))
                                       (memv (string-ref t 1) (string->list "♭♮♯"))))
                      toks)))))
partCleanHarp = #(define-music-function (m) (ly:music?)
  (merge-mmrs! (part-clean! (ly:music-deep-copy m)
    (lambda (x) (and (memq (ly:music-property x 'name) '(TextScriptEvent MultiMeasureTextEvent))
                     (pedal-letter-markup? (ly:music-property x 'text)))))))

% Proofreading aid (MOLA PDF 8: extracted parts are not error-free by themselves). With PARTS_AUDIT=1 in the
% environment, each part logs (a) entries after two or more whole notes' rest that carry no dynamic, and (b) notes
% with more than three ledger lines.
#(define parts-audit? (and (getenv "PARTS_AUDIT") #t))
#(define audit-ledger-limit (if (getenv "PARTS_AUDIT_POS") (string->number (getenv "PARTS_AUDIT_POS")) 11))
#(define (make-audit-engraver name)
   (lambda (context)
     (let ((last-end #f) (step-end #f) (step-dyn #f) (step-note #f) (step-pos '()))
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
                       (pair? acc) (eq? (ly:music-property (car acc) 'name) 'SkipEvent))
                  (let ((len (+ (skip-len (car acc)) (skip-len (car l)))))
                    (loop (cdr l) (cons (make-music 'SkipEvent 'duration
                                          (ly:make-duration 0 0 (numerator len) (denominator len))) (cdr acc)))))
                 (else (merge-skips! (car l)) (loop (cdr l) (cons (car l) acc))))))
     m))
% c275: the score's spacing sections (73-76: \newSpacingSection and a SpacingSpanner override) also cut the skips and split
% a multi-measure rest at 73 in the C.a., Tpt 3, percussion and harp parts (69-72 | 73-76 with no mark at 73); a part has
% its own spacing, so they are dropped too (Adler, Study of Orchestration ch. 18, PDF 299 Ex. XVIII-5: rests are split only
% at rehearsal letters and changes of metre; MOLA PDF 10 Ex. 3-4).
#(define (spacing-section? m)
   (or (eq? (ly:music-property m 'name) 'SpacingSectionEvent)
       (and (eq? (ly:music-property m 'name) 'EventChord) ; \newSpacingSection is an EventChord around the event
            (let ((es (ly:music-property m 'elements)))
              (and (pair? es) (every (lambda (x) (eq? (ly:music-property x 'name) 'SpacingSectionEvent)) es))))
       (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
            (let ((e (ly:music-property m 'element)))
              (and (ly:music? e) (memq (ly:music-property e 'name) '(OverrideProperty RevertProperty))
                   (eq? (ly:music-property e 'symbol) 'SpacingSpanner))))))
#(define (part-global-drop? m) (or (mt-step? m) (spacing-section? m)))
partGlobalOf = #(define-music-function (m) (ly:music?)
  (merge-skips! (part-clean! (ly:music-deep-copy m) part-global-drop?)))

% Part-only cues in long rests (MOLA PDF 5: "Logical cues are expected during long periods of rest, the cues being
% transposed to the reading key of the instrument. Cues must be audible and obvious"). \partCues takes a list of
% (quote-name label direction first-bar bars) and replaces those bars of a multi-measure rest by a \cueDuring.
% Bars count from 1 in 4/4; the rest that contains the bars is split around them.
#(define (bar-moment b) (- b 1))
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
      ;; c265: a merged rest may carry a hairpin end or a dynamic (e.g. Hn 2 R1\\! at 45); the cue may still go in its later bars,
      ;; the leading part of the rest keeps the articulations
      ((and (eq? n 'MultiMeasureRestMusic)
            (or (null? (ly:music-property m 'articulations)) (> start t0)))
       (cons (make-music 'SequentialMusic 'elements
               (append (if (> start t0)
                           (let ((lead (mmr-of (- start t0))))
                             (ly:music-set-property! lead 'articulations (ly:music-property m 'articulations))
                             (list lead))
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
             (r (insert-cue m 0 (bar-moment b) n (lambda (len) (make-cue-music name label dir len)))))
        (if (not (cdr r)) (ly:warning "partCues: no rest for cue ~a at bar ~a" name b))))
    cues)
  m)

% c265: bar-number range under each multi-measure rest of two or more bars (MOLA PDF 5: "except in the case of multi-measure
% rests, where measure number ranges are helpful (e.g., '27-117')"; Ex. 3, PDF 10: the rest "3" with "9 - 11" below the staff).
% The range is read from the rest's left paper column, so it always matches the score's bar numbers.
#(define (mmr-with-range grob)
   (let* ((stil (ly:multi-measure-rest::print grob))
          (count (ly:grob-property grob 'measure-count 1))
          (col (ly:spanner-bound grob LEFT))
          (loc (and (ly:grob? col) (ly:grob-property col 'rhythmic-location #f))))
     (if (and (ly:stencil? stil) (pair? loc) (integer? count) (> count 1))
         (let* ((start (car loc))
                (end (+ start count -1))
                (txt (grob-interpret-markup grob (markup #:fontsize -2 (format #f "~a–~a" start end))))
                (cx (interval-center (ly:stencil-extent stil X)))
                (tx (ly:stencil-aligned-to txt X CENTER)))
           (ly:stencil-add stil (ly:stencil-translate tx (cons cx -4.2))))
         stil)))

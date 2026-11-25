\version "2.26.0"
\language "nederlands"
% REAPER mockup extraction: one staff per player, MIDI + an event dump (articulations, text, dynamics, hairpins, slurs, tremolos).
\include "score-defs.ily"

#(define mock-port (open-file "mockup-events.tsv" "w"))
#(define (mk->str x)
   (cond ((string? x) x)
         ((markup? x) (markup->string x))
         ((symbol? x) (symbol->string x))
         ((number? x) (number->string x))
         (else (format #f "~a" x))))
#(define (mock-line ctx kind . vals)
   (let* ((m (ly:context-current-moment ctx))
          (staff (ly:context-property ctx 'instrumentName)))
     (display (string-join
               (append (list (mk->str staff)
                             (number->string (exact->inexact (* 4 (ly:moment-main m))))
                             (number->string (exact->inexact (* 4 (ly:moment-grace m))))
                             kind)
                       (map mk->str vals)) "\t") mock-port)
     (newline mock-port)))
#(define mock-engraver
  (lambda (ctx)
   (make-engraver
    (listeners
     ((note-event eng e) (let ((p (ly:event-property e 'pitch)) (dt (ly:event-property e 'drum-type)))
                       (if (symbol? dt)
                           (mock-line ctx "drum" dt
                                      (exact->inexact (* 4 (ly:moment-main (ly:duration->moment (ly:event-property e 'duration)))))))
                       (if (ly:pitch? p)
                           (mock-line ctx "note" (+ 60 (ly:pitch-semitones p))
                                      (exact->inexact (* 4 (ly:moment-main (ly:duration->moment (ly:event-property e 'duration)))))))))
     ((articulation-event eng e) (mock-line ctx "script" (ly:event-property e 'articulation-type)))
     ((text-script-event eng e) (mock-line ctx "text" (ly:event-property e 'text)))
     ((slur-event eng e) (mock-line ctx "slur" (ly:event-property e 'span-direction)))
     ((phrasing-slur-event eng e) (mock-line ctx "slur" (ly:event-property e 'span-direction)))
     ((dynamic-event eng e) (mock-line ctx "dynamic" (ly:event-property e 'text)))
     ((absolute-dynamic-event eng e) (mock-line ctx "dynamic" (ly:event-property e 'text)))
     ((crescendo-event eng e) (mock-line ctx "cresc" (ly:event-property e 'span-direction)))
     ((decrescendo-event eng e) (mock-line ctx "decresc" (ly:event-property e 'span-direction)))
     ((tremolo-event eng e) (mock-line ctx "tremolo" (ly:event-property e 'tremolo-type)))
     ((tie-event eng e) (mock-line ctx "tie"))
     ((breathing-event eng e) (mock-line ctx "breathe"))
     ((arpeggio-event eng e) (mock-line ctx "arpeggio" 1))))))   % c04 (A #1): rolled chords

% c32 (critics A #2, B #2, C #5): the mockup owns the MIDI velocity table. A score may set Score.dynamicAbsoluteVolumeFunction
% itself (v621's global.ily sets expr-volume, LilyPond's default volumes, for its own MIDI); that \set overrode the \midi table
% below, and every velocity-dependent row (pizz., Stac, harp, timpani strokes) played 3-10 dB louder than the 30 cycles of
% series 1 had tuned. mockVol replaces the value of any such \set in the score music with mock-volume, which reads the
% dynamic word inside a markup ("pp espr.", "sub. p") with the mockup's table; a mark with no known word keeps p.
#(define mock-dyn-table '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66)
                          ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("sfz" . 0.66) ("fp" . 0.42)))
#(define (mock-volume d)
   (let* ((s (cond ((string? d) d) ((markup? d) (markup->string d)) (else "")))
          (w (find (lambda (x) (assoc x mock-dyn-table)) (string-split s #\space))))
     (if w (assoc-get w mock-dyn-table) 0.42)))
% mvt2 v600 port (c27): v600 carries 52 hidden dynamics (-\tweak stencil ##f \mp etc.), MIDI-only levels the composition
% loop added because LilyPond's MIDI velocity is one value per note-on (e.g. the crest of a crescendo put on a tied
% note). The mockup draws hairpins as continuous CC11 and reads the printed marks only, so mockVol replaces a dynamic
% whose stencil is tweaked to #f by a hairpin stop (\!): it still ends the hairpin it ended in the score (the events
% log "cresc 1"), but sets no level in the events or the MIDI. The score's MIDI-only volume settings go too (below). 'midi-tagged marks (Bsn 1, bars 76-77) stay: they repeat the
% part's marks on the shared bassoon staff.
#(define (mock-hidden-dyn? x)
   (and (ly:music? x)
        (memq (ly:music-property x 'name) '(AbsoluteDynamicEvent))
        (let ((tw (ly:music-property x 'tweaks '())))
          (any (lambda (t) (and (pair? t)
                                (or (eq? (car t) 'stencil) (and (pair? (car t)) (eq? (cdar t) 'stencil)))
                                (not (cdr t))))
               tw))))
#(define (mock-unhide a)
   (if (mock-hidden-dyn? a) (make-music 'CrescendoEvent 'span-direction 1) a))
mockVol = #(define-music-function (m) (ly:music?)
  (music-map (lambda (x)
               (if (pair? (ly:music-property x 'articulations))
                   (ly:music-set-property! x 'articulations (map mock-unhide (ly:music-property x 'articulations))))
               (if (and (eq? (ly:music-property x 'name) 'EventChord) (pair? (ly:music-property x 'elements)))
                   (ly:music-set-property! x 'elements (map mock-unhide (ly:music-property x 'elements))))
               (cond ((and (eq? (ly:music-property x 'name) 'PropertySet)
                           (eq? (ly:music-property x 'symbol) 'dynamicAbsoluteVolumeFunction))
                      (ly:music-set-property! x 'value mock-volume) x)
                     ;; mvt2 v600 port (c27): the score's own MIDI volume ranges and CC11 fades (midiMinimumVolume /
                     ;; midiMaximumVolume on the cor anglais and clarinet 1, midiExpression on the strings and the
                     ;; morendo) are dropped: velocities come from mock-volume alone, CC11 from score_to_parts.py
                     ((and (memq (ly:music-property x 'name) '(PropertySet PropertyUnset))
                           (memq (ly:music-property x 'symbol)
                                 '(midiMinimumVolume midiMaximumVolume instrumentEqualizer midiExpression)))
                      (make-music 'SequentialMusic 'elements '()))
                     (else x)))
             m))

pl = #(define-music-function (name m) (string? ly:music?)
  #{ \new Staff = #name \with { instrumentName = #name midiInstrument = "string ensemble 1" } << \global \removeWithTag #'part #m >> #})

\score {
  \mockVol <<
    \pl "Fl1" \fluteOne  \pl "Fl2" \fluteTwo  \pl "Ob1" \oboeOne  \pl "Ob2" \oboeTwo  \pl "CA" \corAnglais
    \pl "Cl1" \clOne  \pl "Cl2" \clTwo  \pl "BCl" \bassCl  \pl "Bn1" \bsnOne  \pl "Bn2" \bsnTwo  \pl "Cbn" \cbsn
    \pl "Hn1" \hnOne  \pl "Hn2" \hnTwo  \pl "Hn3" \hnThree  \pl "Hn4" \hnFour
    \pl "Tpt1" \tptOne  \pl "Tpt2" \tptTwo  \pl "Tpt3" \tptThree
    \pl "Tbn1" \tbnOne  \pl "Tbn2" \tbnTwo  \pl "BTbn" \bassTbn  \pl "Tuba" \tuba  \pl "Timp" \timp
    \new DrumStaff \with { instrumentName = "Perc" } << \global \removeWithTag #'part \perc >>
    \new PianoStaff \with { instrumentName = "Harp" } << \pl "HarpR" \harpR \pl "HarpL" \harpL >>
    \pl "VlnI" \vlnOne  \pl "VlnII" \vlnTwo  \pl "Vla" \vla  \pl "Vc" \vc  \pl "Cb" \cb
  >>
  \layout { \context { \Voice \consists #mock-engraver } \context { \DrumVoice \consists #mock-engraver } }
  \midi { \context { \Score midiChannelMapping = #'staff
    dynamicAbsoluteVolumeFunction = #mock-volume }
    \context { \PianoStaff \consists "Dynamic_performer" } }
}

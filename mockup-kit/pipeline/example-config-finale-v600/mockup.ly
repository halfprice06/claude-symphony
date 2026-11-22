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
     ;; mvt3 c10 (critic A #3): text on a multi-measure rest (stick changes, "muta", "togli sord.") was dropped
     ((multi-measure-text-event eng e) (mock-line ctx "text" (ly:event-property e 'text)))
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
mockVol = #(define-music-function (m) (ly:music?)
  (music-map (lambda (x)
               (if (and (eq? (ly:music-property x 'name) 'PropertySet)
                        (eq? (ly:music-property x 'symbol) 'dynamicAbsoluteVolumeFunction))
                   (begin (ly:music-set-property! x 'value mock-volume) x)
                   x))
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

\version "2.26.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing.
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinuteAsMoment = #(ly:make-moment bpm 4) #})
% c045: rehearsal letter (and tempo) repeated above the highest string staff when Violins I rest (MOLA PDF 4: tempo marks above the
% top staff and above the first violins, or the similarly positioned staff; rehearsal letters as landmarks). 
strMark = #(define-event-function (letter tempo) (string? markup?)
  #{ -\tag #'score -\tweak outside-staff-priority #1000 -\tweak X-offset #-1 ^\markup \column { \override #'(box-padding . 0.5) \box \bold \fontsize #3 #letter \bold #tempo } #})
% c335: Gould, Behind Bars PDF 63 (perfect unisons on one stem: one notehead each side of the stem). For a single pitch inside a
% divided string passage, both halves on the note. Draws the second head on the far side of the stem; adds no MIDI note (c325 open point).
unisHead = #(define-music-function (note) (ly:music?)
  #{ \tweak NoteHead.stencil
       #(lambda (grob)
          (let* ((s (ly:note-head::print grob))
                 (stem (ly:grob-object (ly:grob-parent grob X) 'stem))
                 (dir (if (ly:grob? stem) (ly:grob-property stem 'direction) UP))
                 (w (interval-length (ly:stencil-extent s X))))
            ;; the extent stays the original head's, so the stem still attaches to it; the copy sits on the far side of the stem
            (ly:make-stencil (ly:stencil-expr (ly:stencil-add s (ly:stencil-translate-axis s (* dir (- w 0.13)) X)))
                             (ly:stencil-extent s X) (ly:stencil-extent s Y))))
     \tweak NoteHead.extra-spacing-width #'(-1.6 . 1.6)
     #note #})
global = {
  \accidentalStyle Score.modern
  \numericTimeSignature
  \key aes \major \time 3/4
  \tempo "Adagio" 4 = 52
  % 1-6: common-tone link from movement I (C held on top, E natural falls to E flat)
  s2.*6 \break
  \mark \default % A 7: horn theme, no strings
  s2.*8 \break
  \mark \default % B 15: oboe and violins in dialogue
  s2.*8 \break
  \mark \default % C 23: theme in the violins, cello counter-melody
  s2.*8 \break
  % 31-36: bass clarinet over an A flat pedal, to D flat
  \mark \default % D 31 (c425: Adler part 2 PDF 299 item 4, Ex. XVIII-5: no 12-14-bar stretch without a landmark; later letters move up one)
  s2.*4 \tempo \markup \normal-weight \italic "poco rit." \mt 49 s2. \mt 45 s2. \break
  \bar "||" \key des \major \time 4/4 \mark \default % E 37 (D before c425)
  \tempo "Poco più mosso" 4 = 60
  s1*4 \break s1*4 \break
  \mark \default % F 45 (letters from 37 renamed by c425)
  s1*2
  \bar "||" \key fis \minor
  % c048: the 3-bar group 45-47 ends on the C sharp 7 goal; the quotation is held back as movement I holds back its S theme
  % (mvt I: poco rit. into Poco meno mosso) and as Dvorak 9/ii 53-54 does (poco ritard. - Poco meno mosso); A&S PDF 47 note, 53-54
  s2 \tempo \markup \normal-weight \italic "poco rit." \mt 57 s4 \mt 55 s4
  \tempo \markup \normal-weight \italic "poco sostenuto" \mt 54 s1 \break s1*2
  \bar "||" \key des \major
  s1*2 \break
  \mark \default % G 53
  \tempo \markup \normal-weight \italic "a tempo, poco a poco animando" \mt 60 s1*2 \mt 61 s1*2 \break \mt 62 s1*2
  % c035: 59-60 have viola sextuplets; a tighter spacing section keeps a quarter as wide here as in 57-58 (Gould, Behind Bars p. 40, PDF 54: equal durations take equal space across a system)
  \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.0
  \mt 64 s1 \once \override Staff.MetronomeMark.extra-offset = #'(3.0 . -0.7) \tempo \markup \normal-weight \italic "poco allargando" \mt 62 s2 \mt 58 s2 \break
  \newSpacingSection \revert Score.SpacingSpanner.shortest-duration-space
  \mark \default % H 61
  \tempo "Largamente" 4 = 54
  s1*2
  \bar "||" \key a \minor
  % c153: the quotation's head (63) stays in the Largamente tempo; the broadening starts at its tail (64), as Dvorak 9/ii states the trombone
  % quotation (96-98) in tempo and relaxes only after it (corpus percussion.notesL.ily: no rit. in 90-100); Adler part 2 PDF 279-281 (Bizet: the
  % rall. on the last notes of the phrase, then a tempo); PDF 267 (after a tutti the solo is set off by reducing the forces, not the motion). Was \mt 50 s1 \mt 46 s2 \mt 40 s2 with the word at 63
  s1 \once \override Staff.MetronomeMark.outside-staff-padding = #1.5 \tempo \markup \normal-weight \italic "allargando" \mt 48 % c585: clear of Vln I "unis." (64) so tempo word and string instruction read as two marks (Adler part 1 PDF 30, 53; Gould PDF 55)
  s2 \mt 42 s2 \break
  \bar "||" \key aes \major \time 3/4 \mark \default % J 65
  \tempo "Tempo I" 4 = 52
  s2.*6 \break
  \mark \default % K 71
  s2.*4 \break s2.*3 \tempo \markup \normal-weight \italic "poco allargando" \mt 50 s2. \break \mt 48 s2.*2 \mt 46 s2. \mt 44 s2. \break
  \mark \default % L 83: coda (v03's closing 83-90 cut)
  \tempo "a tempo" \mt 52
  s2.*4 \break s2.*2 \once \override Staff.MetronomeMark.outside-staff-padding = #1.5 \tempo \markup \normal-weight \italic "rit." \mt 48 s2. \mt 44 s2. \mt 40 \set Staff.midiExpression = #1.0 s8 \set Staff.midiExpression = #0.96 s8 \set Staff.midiExpression = #0.92 s8 \set Staff.midiExpression = #0.88 s8 \set Staff.midiExpression = #0.84 s8 \set Staff.midiExpression = #0.8 s8
  % c228: MIDI only. The morendo 91-92 is a diminuendo on tied notes, which velocity (one value per Note On) cannot render; Staff.midiExpression (CC11) fades every sounding staff together across 91 (Casanelles PDF 124, 142, Fig. 4.5: dynamics inside a sounding note need a continuous controller)
  \set Staff.midiExpression = #0.76 \mt 36 s4 s4 \mt 20 s4
  \bar "|."
}

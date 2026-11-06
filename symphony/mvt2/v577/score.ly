\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "II. Adagio"
  subsubtitle = \markup \center-column { "Full score in C — draft v577" \small "Contrabassoon and double basses sound an octave lower than written" \small "Trumpets and percussion tacet" \small "Follows movement I attacca: bar 1 continues its last chord" \small "Duration: about 6 minutes" }  % c060: trumpets tacet in movement II (staves removed; see bSec.ily)  % c340: percussion (movement I's tam-tam and suspended cymbal player) named as tacet and the approximate duration given, as the scherzo (c045, c225) and the finale print them (MOLA PDF 5-6: tacet stated for the whole movement; approximate duration for each movement); score.midi lasts 345 s
  % c200: release copy v201 read "v201, 13 October 2026"; the third series (from c201) prints "draft vNN" again until its own release check (MOLA PDF 6: "print date, or revision date")
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  print-first-page-number = ##t  % c260: page 1 numbered in its upper right corner, as movement I (v266) (MOLA PDF 7: right-hand pages odd-numbered in the upper right corner)
  system-separator-markup = \markup \translate #'(-4 . 0) \slashSeparator  % c285: page 2's systems are close, and the slashes, drawn at the left margin, overprinted the bar numbers 15, 23 and 31 below the systems (MOLA PDF 4: measure numbers below the system; PDF 8 and Ex. 7: no collisions); 4 staff spaces further left they clear the numbers
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
\include "global.ily"
\include "sections/intro.ily"
\include "sections/aOne.ily"
\include "sections/trans.ily"
\include "sections/bSec.ily"
\include "sections/retr.ily"
\include "sections/aTwo.ily"
\include "sections/coda.ily"
\include "parts.ily"

\layout {
  \context { \Staff \RemoveEmptyStaves \consists "Merge_rests_engraver" soloText = "1." soloIIText = "2." }
  \context { \DrumStaff \RemoveEmptyStaves }
  % c215: keep a choir bracket when only one staff of the choir is printed (default collapse-height 5 hid it: Hn. 7-14, 53-56, 75-78; Cbn. and Hn. 23-30; C.a. 49-52; Bn. and Hn. 65-70; Cl. 83-86),
  % as movement I (its c165) (Adler part 2 PDF 294: "heavy brackets set off the choirs"; Ex. XVIII-1, PDF 293)
  \context { \StaffGroup \override SystemStartBracket.collapse-height = #1 }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver"
 \override Script.Y-offset = #(ly:make-unpure-pure-container stem-side-y-offset ly:side-position-interface::pure-y-aligned-side) }  % c125, see stem-side-y-offset
  % c175: the callback is wrapped with the default pure estimate. As a bare procedure it also ran in the pure (pre-line-breaking) phase,
  % where the side-position call formatted the ties under an up-bow before the columns had positions; the ties 79-80 in Vln I, Vln II
  % and Vla came out as zero-length dots (Adler part 1 PDF 38, Ex. II-20: the tied long note with the bow change must be read as one note)
  % c315: as the scherzo's s305 (Gould PDF 55, "no characters should collide"): box skylines, so a dynamic clears stem ends, dots and tenutos
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" \override DynamicText.vertical-skylines = #ly:grob::simple-vertical-skylines-from-extents }
  \context { \Score \remove "Bar_number_engraver"
    % c435: stems thinner than the stave-lines, barlines conspicuously thicker than stems (Gould PDF 27, 52); LilyPond default 1.3
    \override Stem.thickness = #0.9
    % c435: one stave-space after end-of-system warning key and time signatures (Gould PDF 56-57; default 0.5)
    \override TimeSignature.space-alist.right-edge = #'(extra-space . 1.0)
    \override KeySignature.space-alist.right-edge = #'(extra-space . 1.0)
    \override KeyCancellation.space-alist.right-edge = #'(extra-space . 1.0)
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #3
    \override BarNumber.break-visibility = ##(#f #t #t)
    \override BarNumber.font-size = #-1
    \override BarNumber.padding = #2
    barNumberVisibility = #(every-nth-bar-number-visible 1)
  }
}

% c060: horns carry the concert key signatures again, as in movement I (trumpets tacet here; give them signatures too if they return) (one convention for both concert-pitch scores:
% Adler part 2 PDF 294, key signatures after the clef on every staff; parts for horns without signatures, MOLA PDF 5). Supersedes c046.
% c055: keys of horns and trumpets named at the start, as for the clarinets and as in movement I (Adler part 2 PDF 292: "Keys of the horns/trumpets must be given at the beginning of the score"); timpani without key signature, as in movement I (Adler PDF 301: proofreading for consistency).
% c045: the bar numbers are engraved on the double-bass staff, which is hidden when the basses rest, so systems 7-14 and 31-36 had
% no bar numbers at all (MOLA PDF 4: all full scores include measure numbers; if every bar is numbered, below the system).
% The lowest staff of those two systems carries them instead, for those bars only.
bnBelow = #(define-scheme-function (from to) (integer? integer?)
  #{ \with { \consists "Bar_number_engraver"
      barNumberVisibility = #(lambda (n pos) (and (>= n from) (<= n to)))
      \override BarNumber.direction = #DOWN \override BarNumber.self-alignment-X = #CENTER \override BarNumber.break-align-symbols = #'(staff-bar)
      \override BarNumber.break-visibility = ##(#f #t #t) \override BarNumber.font-size = #-1 \override BarNumber.padding = #1
      \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #7 \override BarNumber.outside-staff-horizontal-padding = #0.5 } #})

% c135: short names keep the instrument keys, as on the first page (MOLA PDF 9, Example 2: "Cl. 1, 2 (B♭)", "Hn. 1, 2 in F")
% c260: horns read "in F" under the short name, as Example 2 and movement I (v266); clarinets keep "(B♭)"
pc = #(define-music-function (a b) (ly:music? ly:music?) #{ \partCombine #a #b #})

% c215: tempo words (and the letter at 61) repeated above the brass on the four full-orchestra systems, where the top and string marks are
% about 15 staves apart (Adler part 2 PDF 294: "tempo markings be placed at the top of the score and repeated in the space separating each
% choir"; Ex. XVIII-1, PDF 293). Reduced systems keep the top and string marks only (their brass staff is at most four staves below the top).
% The scherzo (c055/c145) and the finale already print tempo marks over the brass.
brassMark = #(define-event-function (tempo) (markup?)
  #{ -\tweak outside-staff-priority #1000 ^\markup #tempo #})
brassLetter = #(define-event-function (letter tempo) (string? markup?)
  #{ -\tweak outside-staff-priority #1000 -\tweak X-offset #-1 ^\markup \column { \override #'(box-padding . 0.5) \box \bold \fontsize #3 #letter #tempo } #})
brassMarks = {
  \once \override TextScript.X-offset = #-5.2 s2.\brassMark \markup { \bold "Adagio" \concat { "(" \fontsize #-2 \general-align #Y #DOWN \note {4} #1 " = 52)" } } s2.*35 |
  s1*23 | s1\brassMark \markup \medium \italic "poco allargando" |
  s1\brassLetter "H" \markup { \bold "Largamente" \concat { "(" \fontsize #-2 \general-align #Y #DOWN \note {4} #1 " = 54)" } } | s1*2 |
  s1\brassMark \markup \medium \italic "allargando" |
}

% c388: the music is a function of the timpani part, so the MIDI-only \score below can turn the timpani rolls into strokes
% (rolls-midi.ily from the coherence folder). Note_performer ignores stem tremolo, so each roll played as one held stroke.
% The printed score passes the timpani unchanged.
\include "rolls-midi.ily"
scoreMusic = #(define-music-function (tp) (ly:music?) #{
  <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl. 1·2" midiInstrument = "flute" }
        << \global \pc \removeWithTag #'part \fluteOne \removeWithTag #'part \fluteTwo >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob. 1·2" midiInstrument = "oboe" }
        << \global \pc \removeWithTag #'part \oboeOne \removeWithTag #'part \oboeTwo >>  % c315: oboeOne carries a part-only cue (42-43)
      \new Staff = "Cor anglais" \with { instrumentName = "Cor anglais" shortInstrumentName = "C.a." midiInstrument = "english horn" }
        << \global \removeWithTag #'part \corAnglais >>
      \new Staff = "Clarinets 1·2" \with { instrumentName = \markup \center-column { "Clarinets 1·2" \small "in B♭" } shortInstrumentName = \markup \center-column { "Cl. 1·2" \small "(B♭)" } midiInstrument = "clarinet" }
        << \global \pc \removeWithTag #'part \clOne \removeWithTag #'part \clTwo >>  % c285: clOne now carries a part-only cue (51-52)
      \new Staff = "Bass clarinet" \with { instrumentName = \markup \center-column { "Bass clarinet" \small "in B♭ (low C)" } shortInstrumentName = \markup \center-column { "B.cl." \small "(B♭)" } midiInstrument = "clarinet" }
        << \clef bass \global \removeWithTag #'part \bassCl >>  % c156: part-only ossia at 8 (Adler App. A, adler2 PDF 304: the low C is parenthesised, not on every instrument)
      \new Staff = "Bassoons 1·2" \with { instrumentName = "Bassoons 1·2" shortInstrumentName = "Bn. 1·2" midiInstrument = "bassoon" }
        << \clef bass \global \pc \bsnOneX \bsnTwo >>
      \new Staff = "Contrabassoon" \with \bnBelow 31 36 \with { \override BarNumber.staff-padding = #4.5 % c485: the 31-36 numbers sat 7 spaces below the Cbn, on the line of the next system's "Poco più mosso" (Adler part 2 PDF 291 items 1-2)
        instrumentName = "Contrabassoon" shortInstrumentName = "Cbn." midiInstrument = "bassoon" }
        << \clef bass \global \transposition c \transpose c c' \removeWithTag #'part \cbsn >>
    >>
    \new StaffGroup <<
      % c215: horns 1-4 and the trombones each joined by a sub-bracket inside the brass bracket, as in the scherzo (c145) (Adler part 2 PDF 294:
      % "heavy brackets set off the choirs; and an additional brace clarifies instruments of a family"; Ex. XVIII-1, PDF 293)
      \new StaffGroup \with { systemStartDelimiter = #'SystemStartSquare \override InstrumentName.padding = #1.2 } <<
      \new Staff = "Horns 1·2" \with { instrumentName = \markup \center-column { "Horns 1·2" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 1·2" \small "in F" } midiInstrument = "french horn" }
        << \global \new Voice \brassMarks \pc \removeWithTag #'part \hnOne \removeWithTag #'part \hnTwo >>
      \new Staff = "Horns 3·4" \with { instrumentName = \markup \center-column { "Horns 3·4" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 3·4" \small "in F" } soloText = "3." soloIIText = "4." midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnThree \removeWithTag #'part \hnFour >>
      >>
      \new StaffGroup \with { systemStartDelimiter = #'SystemStartSquare \override InstrumentName.padding = #1.2 } <<
      \new Staff = "Trombones 1·2" \with { instrumentName = "Trombones 1·2" shortInstrumentName = "Tbn. 1·2" midiInstrument = "trombone" }
        << \clef bass \global \pc \removeWithTag #'part \tbnOne \removeWithTag #'part \tbnTwo >>
      \new Staff = "Bass trombone" \with { instrumentName = "Bass trombone" shortInstrumentName = "B.tbn." midiInstrument = "trombone" }
        << \clef bass \global \removeWithTag #'part \bassTbn >>
      >>
      \new Staff = "Tuba" \with { instrumentName = "Tuba" shortInstrumentName = "Tba." midiInstrument = "tuba" }
        << \clef bass \global \removeWithTag #'part \tuba >>
    >>
    % c215: timpani in its own bracket, the percussion choir of Ex. XVIII-1 (Adler part 2 PDF 293-294), as in movement I (c165) and the scherzo
    \new StaffGroup \with { \remove "Span_bar_engraver" } <<
    \new Staff = "Timpani" \with { \remove "Key_engraver" instrumentName = "Timpani" shortInstrumentName = "Timp." midiInstrument = "timpani" }
      << \clef bass \global #tp >>
    >>
    \new PianoStaff \with { connectArpeggios = ##t midiInstrument = "orchestral harp" instrumentName = "Harp" shortInstrumentName = "Hp." } <<
      \new Staff = "Harp RH" \with { midiInstrument = "orchestral harp"
        % c125: two-note rolls in the RH were drawn about two spaces tall, the size and shape of a quarter rest, right after the r4 in 7, 9-11, 13, 72-73 (Gould PDF 55-56: no symbol placed so it can be mistaken for another); lengthen each roll by one space at both ends
        \override Arpeggio.positions = #(lambda (grob) (let ((p (ly:arpeggio::calc-positions grob))) (cons (- (car p) 1) (+ (cdr p) 1)))) } << \global \removeWithTag #'part \harpR >>  % c315: harpR carries part-only cues (34-36, 68-70)
      \new Staff = "Harp LH" \with \bnBelow 7 14 \with { midiInstrument = "orchestral harp" \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \global \removeWithTag #'part \harpL >>
    >>
    \new StaffGroup <<
      \new Staff = "Violins I" \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" instrumentName = "Violins I" shortInstrumentName = "Vln. I" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnOne >>
      \new Staff = "Violins II" \with { instrumentName = "Violins II" shortInstrumentName = "Vln. II" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnTwo >>  % c485: filtered like Vln I and violas; the part-only "via sord." at 92 (c470) printed at the top of the score, over the cor anglais
      \new Staff = "Violas" \with { instrumentName = "Violas" shortInstrumentName = "Vla." midiInstrument = "viola" }
        << \clef alto \global \removeWithTag #'part \vla >>  % c235: without the filter the part-only texts printed in the score as well (div./unis. twice at 80-81 since c227, and the 87-89 texts)
      \new Staff = "Violoncellos" \with {  % c527: \bnBelow 53 56 removed; the bass staff is visible at 53-56 again
       instrumentName = "Violoncellos" shortInstrumentName = "Vc." midiInstrument = "cello" }
        << \clef bass \global \vc >>
      \new Staff = "Double basses" \with { \consists "Bar_number_engraver" \override BarNumber.direction = #DOWN \override BarNumber.self-alignment-X = #CENTER \override BarNumber.break-align-symbols = #'(staff-bar) \override BarNumber.break-visibility = ##(#f #t #t) \override BarNumber.font-size = #-1 \override BarNumber.padding = #1 \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #7 \override BarNumber.outside-staff-horizontal-padding = #0.5 instrumentName = "Double basses" shortInstrumentName = "Cb." midiInstrument = "contrabass" }
        << \clef bass \global \transposition c \transpose c c' \cb >>
    >>
  >>
#})

% c400: 'midi-tagged events (Bsn 1's hidden levels at 76-77) reach only the MIDI \score; in the printed score a hidden dynamic in Bsn 1 ended Bsn 2's shared-staff hairpin early
bsnOneX = \removeWithTag #'(part midi) \bsnOne
\score {
  \scoreMusic \removeWithTag #'part \timp
  \layout { }
}

% c388: MIDI only. 64th-note strokes: 13.9 per second at 52, 16 at 60, 11.7 at the 44 of bar 81 (rolls at 2-3, 52, 60-62, 67-70, 79-81).
bsnOneX = \removeWithTag #'part \bsnOne
\score {
  \scoreMusic \rollStrokes #64 \removeWithTag #'part \timp
  \midi { \context { \Score midiChannelMapping = #'instrument
    % c228: LilyPond's equalizer table (midi-init.ly) has no entry for english horn, trombone, tuba, orchestral harp, so these played over the full 0-1 range while
    % oboe, horns and the other winds are scaled to 0-0.7: at 79 the cor anglais (a doubling) was the loudest wind, at 61 the trombones f were 21 velocity steps over the horns f.
    % The FluidR3 patches are within about 4 dB of each other at equal velocity, so each gets its family neighbour's range (Casanelles PDF 133-134, 141-142).
    % c244: timpani take the horn range (0.1 . 0.7) instead of LilyPond's default (0.2 . 0.9), whose floor made the ppp roll at 67 (v47) louder than Hn 1's p tail (v44) and the pp answer at 84 (v54) level with the harp's p head (now v37 and v37); the timpani are a brass-choir instrument (Adler part 1 PDF 21) and a roll is a constant level that is heard as more present than a moving line (Casanelles PDF 290). Listed first, because the default alist has a timpani entry
    instrumentEqualizer = #(lambda (s) (or (assoc-get s '(("timpani" . (0.1 . 0.7)))) (assoc-get s instrument-equalizer-alist) (assoc-get s '(("english horn" . (0 . 0.7)) ("trombone" . (0.1 . 0.7)) ("tuba" . (0.1 . 0.7)) ("orchestral harp" . (0 . 0.7)) ("pizzicato strings" . (0.1 . 0.7)) ("tremolo strings" . (0.1 . 0.7))))))
    % c388: fp takes the f velocity; the three fp notes at 47 (Vln II, Vla, Cb) fall to p by a CC11 ramp in bSec.ily.
    % \subP is a markup dynamic ("sub. p"): give it the p volume. sf/fp were unmapped and fell back to the default (0.71, louder than ff).
    dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.66)) #f)
      0.42)) }
    % c244: the harp dynamics are performed in the PianoStaff, whose midiInstrument was unset, so c228's ("orchestral harp" . (0 . 0.7)) range was never applied (pp played at v41, mf at v73); midiInstrument is now set on the PianoStaff too
    % Harp: one set of dynamics for both hands (printed under the LH); the RH staff has none, so its notes played at the default volume.
    \context { \PianoStaff \consists "Dynamic_performer" } }
}

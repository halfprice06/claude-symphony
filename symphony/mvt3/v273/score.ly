\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "IV. Finale: Allegro con fuoco"
  subsubtitle = \markup \center-column { "Full score in C — draft v273" \small "Contrabassoon and double basses sound an octave lower than written (double basses: C extension at 166 and 174–183)" \small "After movement III (Scherzo): a pause" \small "Duration: about 7 minutes" }
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  % c245: 2 mm more page height (top 5 -> 4 mm, bottom 6 -> 5 mm, LilyPond defaults before); the up-stems from gould-mid-stems (bars 12, 20) left page 2
  % over-full by 1.2 staff-spaces. Page breaks and systems unchanged.
  top-margin = 4\mm
  bottom-margin = 5\mm
  system-separator-markup = \markup \translate #'(-3 . 0) \slashSeparator  % c135: moved 3 staff spaces left, clear of the first bar number below the system (page 2: bar 13 was printed under it; MOLA PDF 4)
  % c023: page-count = 16 removed: with it LilyPond reports "too few pages: 16 (should have at least 17)" after the 8 added bars (269-276); without it the free page breaker still lays the score out on 16 pages
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
\include "sections/pOne.ily"
\include "sections/pTwo.ily"
\include "sections/trans.ily"
\include "sections/sOne.ily"
\include "sections/sTwo.ily"
\include "sections/clos.ily"
\include "sections/dev.ily"
\include "sections/retr.ily"
\include "sections/recP.ily"
\include "sections/recS.ily"
\include "sections/codaOne.ily"
\include "sections/codaTwo.ily"
\include "sections/arrival.ily"
\include "sections/sHead.ily"
\include "sections/finale.ily"
\include "parts.ily"
% c075 (MOLA PDF 5: logical cues during long rests in the parts): sources of the part-only cues (tag 'part, see trans, sOne, recP, retr, arrival).
% Every staff below reads its player through \removeWithTag #'part, so the cues never reach the score or the MIDI.
\addQuote "oboeOne" { \removeWithTag #'part \oboeOne }
\addQuote "tptOne" { \removeWithTag #'part \tptOne }
\addQuote "vlnOne" { \removeWithTag #'part \vlnOne }
\addQuote "vlnTwo" { \removeWithTag #'part \vlnTwo }
\addQuote "bsnOne" { \removeWithTag #'part \bsnOne }
\addQuote "vc" { \removeWithTag #'part \vc }  % c105: cue source for the low brass and timpani at 197-198

% c245 (Gould, Behind Bars ch. 1, PDF 27-28, "Notes on the centre stave-line"; PDF 61 for chords): a note on the middle line (or a chord whose outer notes
% are equidistant from it) takes its stem direction from context: it continues the direction of the stems on both sides when they agree, and otherwise
% keeps the direction of the note in the same half-bar (one beat of 2/2); only with no clear case is it a down-stem. LilyPond always gives such a note a
% down-stem, so a B4 in treble (D3 in bass, C4 in alto) turned its stem down between up-stems inside a phrase. Only unbeamed notes whose direction is not
% fixed (no \voiceOne/\voiceTwo, part-combined chords and solos included), and only neighbours that join the note without a rest.
#(define (gould-mid-stems context)
  (let ((items '()))
    (define (heads stem) (let ((a (ly:grob-object stem 'note-heads))) (if (ly:grob-array? a) (ly:grob-array->list a) '())))
    (define (head-len h) (let ((ev (event-cause h))) (if (and ev (ly:duration? (ly:event-property ev 'duration))) (ly:moment-main (ly:duration-length (ly:event-property ev 'duration))) 0)))
    (make-engraver
     (acknowledgers
      ((stem-interface engraver grob source-engraver)
       (let ((now (ly:context-current-moment context)))
         (if (zero? (ly:moment-grace now))
             (set! items (cons (vector grob (ly:moment-main now) (ly:context-property context 'currentBarNumber)
                                       (ly:moment-main (ly:context-property context 'measurePosition))) items))))))
     ((finalize translator)
      (let* ((v (list->vector (reverse items))) (n (vector-length v))
             (info (make-vector n #f)))
        ;; info: #(stem start end bar half visible? candidate?)
        (do ((i 0 (1+ i))) ((= i n))
          (let* ((it (vector-ref v i)) (stem (vector-ref it 0)) (hs (heads stem))
                 (start (vector-ref it 1)) (len (if (null? hs) 0 (head-len (car hs))))
                 (dl (ly:grob-property stem 'duration-log 2))
                 (pos (map (lambda (h) (ly:grob-property h 'staff-position 0)) hs))
                 (visible (and (pair? hs) (>= dl 1)))
                 (cand (and visible (procedure? (ly:grob-property-data stem 'direction))
                            (not (ly:grob? (ly:grob-object stem 'beam)))
                            (= 0 (+ (apply min pos) (apply max pos))))))
            (vector-set! info i (vector stem start (+ start len) (vector-ref it 2)
                                        (if (< (vector-ref it 3) 1/2) 0 1) visible cand))))
        (let loop ((i 0))
          (if (< i n)
              (let ((x (vector-ref info i)))
                (if (not (vector-ref x 6)) (loop (1+ i))
                    (let run ((b i))
                      (if (and (< (1+ b) n) (vector-ref (vector-ref info (1+ b)) 6)
                               (= (vector-ref (vector-ref info b) 2) (vector-ref (vector-ref info (1+ b)) 1)))
                          (run (1+ b))
                          (let* ((l (and (> i 0) (let ((y (vector-ref info (1- i))))
                                                  (and (vector-ref y 5) (not (vector-ref y 6)) (= (vector-ref y 2) (vector-ref x 1)) y))))
                                 (r (and (< (1+ b) n) (let ((y (vector-ref info (1+ b))))
                                                  (and (vector-ref y 5) (not (vector-ref y 6)) (= (vector-ref (vector-ref info b) 2) (vector-ref y 1)) y))))
                                 (ld (and l (ly:grob-property (vector-ref l 0) 'direction)))
                                 (rd (and r (ly:grob-property (vector-ref r 0) 'direction))))
                            (do ((k i (1+ k))) ((> k b))
                              (let* ((c (vector-ref info k))
                                     (same (lambda (y) (and y (= (vector-ref y 3) (vector-ref c 3)) (= (vector-ref y 4) (vector-ref c 4)))))
                                     (d (cond ((and ld rd (= ld rd)) ld)
                                              ((and (same l) (not (same r))) ld)
                                              ((and (same r) (not (same l))) rd)
                                              (else #f))))
                                (if (and d (not (= d 0))) (ly:grob-set-property! (vector-ref c 0) 'direction d))))
                            (loop (1+ b))))))))))))))

\layout {
  \context { \Voice \consists #gould-mid-stems }  % c245, see gould-mid-stems
  \context { \Staff \RemoveEmptyStaves \consists "Merge_rests_engraver" soloText = "1." soloIIText = "2." }
  \context { \DrumStaff \RemoveEmptyStaves }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver"
 \override Script.Y-offset = #stem-side-y-offset }  % c125, see stem-side-y-offset
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" }
  \context { \Score \remove "Bar_number_engraver" \override SpacingSpanner.shortest-duration-space = #1.6
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #3
    \override BarNumber.break-visibility = ##(#f #t #t)
    \override BarNumber.font-size = #-1
    \override BarNumber.padding = #2
    barNumberVisibility = #(every-nth-bar-number-visible 1)
  }
}

% Movement II convention (its c060): horns and trumpets carry the concert key signatures, as in movement I (one convention for all concert-pitch scores:
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
      \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #5.5 \override BarNumber.outside-staff-horizontal-padding = #0.5 } #})

% c135: short names keep the instrument keys, as on the first page (MOLA PDF 9, Example 2: "Cl. 1, 2 (B♭)", "Hn. 1, 2 in F")
pc = #(define-music-function (a b) (ly:music? ly:music?) #{ \partCombine #a #b #})

\score {
  <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl. 1·2" midiInstrument = "flute" }
        << \global \pc \removeWithTag #'part \fluteOne \removeWithTag #'part \fluteTwo >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob. 1·2" midiInstrument = "oboe" }
        << \global \pc \removeWithTag #'part \oboeOne \removeWithTag #'part \oboeTwo >>
      % c135 (MOLA PDF 7: complicated divisions on separate staves, barline continuous): Ob 2's counter-line at 159-166 on its own staff, shown only in that system
      % (bars 1-158 and 167-279 are rests, so RemoveEmptyStaves hides it; remove-first hides it on page 1). Keep the rest lengths in step with sections.txt.
      \new Staff = "Oboe 2" \with { instrumentName = "Oboe 2" shortInstrumentName = "Ob. 2" midiInstrument = "oboe" \override VerticalAxisGroup.remove-first = ##t }
        << \global { R1*158 \recPOboeTwoDiv R1*113 } >>
      \new Staff = "Cor anglais" \with { instrumentName = "Cor anglais" shortInstrumentName = "C.a." midiInstrument = "english horn" }
        << \global \removeWithTag #'part \corAnglais >>
      \new Staff = "Clarinets 1·2" \with { instrumentName = \markup \center-column { "Clarinets 1·2" \small "in B♭" } shortInstrumentName = \markup \center-column { "Cl. 1·2" \small "(B♭)" } midiInstrument = "clarinet" }
        << \global \pc \removeWithTag #'part \clOne \removeWithTag #'part \clTwo >>
      \new Staff = "Bass clarinet" \with { instrumentName = \markup \center-column { "Bass clarinet" \small "in B♭" } shortInstrumentName = \markup \center-column { "B.cl." \small "(B♭)" } midiInstrument = "clarinet" }
        << \clef bass \global \removeWithTag #'part \bassCl >>
      \new Staff = "Bassoons 1·2" \with { instrumentName = "Bassoons 1·2" shortInstrumentName = "Bn. 1·2" midiInstrument = "bassoon" }
        << \clef bass \global \pc \removeWithTag #'part \bsnOne \removeWithTag #'part \bsnTwo >>
      \new Staff = "Contrabassoon" \with { instrumentName = "Contrabassoon" shortInstrumentName = "Cbn." midiInstrument = "bassoon" }
        << \clef bass \global \transposition c \transpose c c' \removeWithTag #'part \cbsn >>
    >>
    % c055 (Adler part 2 PDF 294: tempo markings at the top of the score and repeated in the space separating each choir; Example XVIII-1, PDF 293):
    % tempo and rehearsal marks also over the brass
    \new StaffGroup \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" } <<
      \new Staff = "Horns 1·2" \with { instrumentName = \markup \center-column { "Horns 1·2" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 1·2" \small "(F)" } midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnOne \removeWithTag #'part \hnTwo >>
      \new Staff = "Horns 3·4" \with { instrumentName = \markup \center-column { "Horns 3·4" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 3·4" \small "(F)" } soloText = "3." soloIIText = "4." midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnThree \removeWithTag #'part \hnFour >>
      \new Staff = "Trumpets 1·2" \with { instrumentName = \markup \center-column { "Trumpets 1·2" \small "in C" } shortInstrumentName = \markup \center-column { "Tpt. 1·2" \small "(C)" } midiInstrument = "trumpet" }
        << \global \pc \removeWithTag #'part \tptOne \removeWithTag #'part \tptTwo >>
      \new Staff = "Trumpet 3" \with { instrumentName = \markup \center-column { "Trumpet 3" \small "in C" } shortInstrumentName = \markup \center-column { "Tpt. 3" \small "(C)" } midiInstrument = "trumpet" }
        << \global \removeWithTag #'part \tptThree >>
      \new Staff = "Trombones 1·2" \with { instrumentName = "Trombones 1·2" shortInstrumentName = "Tbn. 1·2" midiInstrument = "trombone" }
        << \clef bass \global \pc \removeWithTag #'part \tbnOne \removeWithTag #'part \tbnTwo >>
      \new Staff = "Bass trombone" \with { instrumentName = "Bass trombone" shortInstrumentName = "B.tbn." midiInstrument = "trombone" }
        << \clef bass \global \removeWithTag #'part \bassTbn >>
      \new Staff = "Tuba" \with { instrumentName = "Tuba" shortInstrumentName = "Tba." midiInstrument = "tuba" }
        << \clef bass \global \removeWithTag #'part \tuba >>
    >>
    % Timpani and percussion form one choir with its own bracket, as in movement I (Adler part 2 PDF 293-294)
    % c235 (Adler part 2 PDF 294: "tempo markings ... repeated in the space separating each choir"; "measure lines ... through the individual complete choirs";
    % Example XVIII-1, PDF 293: the tempo stands over the timpani and the barlines run through timpani and percussion): tempo marks over this choir too, and its
    % barlines joined. Movement I removed the span bars because texts above its one-line stave crossed the barline; the finale's drum staff has no text in the score.
    % c245 (Gould PDF 29: a sign must never cut through other symbols; PDF 41: no characters should collide): the engraver moves from this StaffGroup
    % to the timpani staff. When both drum staves are hidden (37-127, 171-198) the group's tempo texts had no staff to stand on and fell onto the top
    % staff of the system, a second "poco rit." through Fl 1's notes at 197 and a second "animando" and "Tempo I" inside the flute staff at 81 and 83.
    \new StaffGroup <<
    \new Staff = "Timpani" \with { \consists "Metronome_mark_engraver" \remove "Key_engraver" instrumentName = "Timpani" shortInstrumentName = "Timp." midiInstrument = "timpani" }
      << \clef bass \global \removeWithTag #'part \timp >>
    % single-line stave for the unpitched instruments, crossed heads for the cymbals (Gould PDF 19, 26), as in movement I
    \new DrumStaff \with { \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override LaissezVibrerTie.direction = #UP \override Tie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 1) (ridecymbal cross #f 1) (bassdrum default #f -1))) instrumentName = \markup \center-column { "Cymbals" "Bass drum" "(2 players)" } shortInstrumentName = \markup \center-column { "Cym." "B.d." } }
      << \global \removeWithTag #'part \perc >>
    >>
    \new PianoStaff \with { connectArpeggios = ##t instrumentName = "Harp" shortInstrumentName = "Hp." } <<
      \new Staff = "Harp RH" \with { midiInstrument = "orchestral harp"
        % c125: two-note rolls in the RH were drawn about two spaces tall, the size and shape of a quarter rest, right after the r4 in 7, 9-11, 13, 72-73 (Gould PDF 55-56: no symbol placed so it can be mistaken for another); lengthen each roll by one space at both ends
        \override Arpeggio.positions = #(lambda (grob) (let ((p (ly:arpeggio::calc-positions grob))) (cons (- (car p) 1) (+ (cdr p) 1)))) } << \global \removeWithTag #'part \harpR >>
      \new Staff = "Harp LH" \with { midiInstrument = "orchestral harp" \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \global \removeWithTag #'part \harpL >>
    >>
    % c045 (MOLA PDF 4: tempo marks above the top staff and above the first violins, "or similarly positioned staff"): the marks are
    % engraved by the string group, so they stand over its top live staff (Vln II at 51-65 and 171-185, where Vln I is hidden)
    \new StaffGroup \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" } <<
      \new Staff = "Violins I" \with { instrumentName = "Violins I" shortInstrumentName = "Vln. I" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnOne >>
      \new Staff = "Violins II" \with { instrumentName = "Violins II" shortInstrumentName = "Vln. II" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnTwo >>
      \new Staff = "Violas" \with { instrumentName = "Violas" shortInstrumentName = "Vla." midiInstrument = "viola" }
        << \clef alto \global \removeWithTag #'part \vla >>
      \new Staff = "Violoncellos" \with { instrumentName = "Violoncellos" shortInstrumentName = "Vc." midiInstrument = "cello" }
        << \clef bass \global \removeWithTag #'part \vc >>
      \new Staff = "Double basses" \with { \consists "Bar_number_engraver" \override BarNumber.direction = #DOWN \override BarNumber.self-alignment-X = #CENTER \override BarNumber.break-align-symbols = #'(staff-bar) \override BarNumber.break-visibility = ##(#f #t #t) \override BarNumber.font-size = #-1 \override BarNumber.padding = #1 \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #5.5 \override BarNumber.outside-staff-horizontal-padding = #0.5 instrumentName = "Double basses" shortInstrumentName = "Cb." midiInstrument = "contrabass" }
        << \clef bass \global \transposition c \transpose c c' \removeWithTag #'part \cb >>
    >>
  >>
  \layout { }
  \midi { \context { \Score midiChannelMapping = #'instrument
    % \subP is a markup dynamic ("sub. p"): give it the p volume. sf/fp were unmapped and fell back to the default (0.71, louder than ff).
    dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42)) #f)
      0.42)) }
    % Harp: one set of dynamics for both hands (printed under the LH); the RH staff has none, so its notes played at the default volume.
    \context { \PianoStaff \consists "Dynamic_performer" } }
}

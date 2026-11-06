\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "III. Scherzo: Allegro vivace"  % c100: the four titles name the movement and its tempo, as I ("Lento — Allegro appassionato"), II ("Adagio") and IV ("Finale: Allegro con fuoco") do
  subsubtitle = \markup \center-column { "Full score in C — draft v532" \small "Contrabassoon and double basses sound an octave lower than written" \small "After movement II (Adagio): a pause" \small "Trumpet 3 and percussion tacet" \small "Duration: about 4½ minutes" }  % c045: approximate duration of the movement (MOLA PDF 6). c225: percussion (2 players in movement I) is tacet here too and is now named (MOLA PDF 5-6)
  % c200: release copy: "draft" dropped, version and date kept, as movement I (v221, 12 October 2026) and movement II (v201, 13 October 2026) (MOLA PDF 6: "print date, or revision date"); promote.sh's "draft vNN" sed no longer matches, so this line is final
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  % c155: the separator moved down 2 spaces: on page 3 it was printed over the bar number 59 of the system above (Gould PDF 55: no characters collide)
  system-separator-markup = \markup \translate #'(0 . -2) \slashSeparator
  % c250: page 1 numbered in its upper right corner, as movement I (v266) and movement II (v261) (MOLA PDF 7: right-hand pages odd-numbered in the upper right corner)
  print-first-page-number = ##t
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

% c015/c105 beam callback (Gould PDF 31-37): see beams.ily (c195: shared with the parts)
\include "beams.ily"
\include "stems.ily"  % c095: middle-line stems follow the surrounding stems (Gould PDF 27-28, 60-61)

\include "global.ily"
\include "sections/intro.ily"
\include "sections/sA.ily"
\include "sections/sB.ily"
\include "sections/sC.ily"
\include "sections/link.ily"
\include "sections/tA.ily"
\include "sections/tB.ily"
\include "sections/tC.ily"
\include "sections/retr.ily"
\include "sections/dA.ily"
\include "sections/dB.ily"
\include "sections/dC.ily"
\include "sections/coda.ily"
\include "parts.ily"

% c230: MIDI only (prints nothing). Casanelles PDF 216-217, Figs. 5.7-5.8: a dynamic change inside a held note is continuous controller data in the
%   mockup; velocity is one value per Note On, so a hairpin on a tied note does not sound (movement II renders its own closing morendo this way, its c228).
%   The two fades of the closing page now sound: the held chord 362-364 (Fl, Cl, Vln II, Vla, Vc, Cb; pp > to the release, c123) and Hn 1's last G sharp
%   372-375 (pp > ppp, the pivot into the finale; 0.76 = ppp/pp in the volume table below). One step per bar: steps inside a bar
%   add spacing columns and moved page 13; at the bar line they change nothing in the print. The chord's staves are back at 1.0 at 365,
%   before Vln I (same MIDI channel as Vln II) enters at 369 and Vc/Cb pizz. at 375. Hn 3 (same channel as Hn 1) stops at 369, before the horn fade.
chordFadeMidi = { s2.*361 \set Staff.midiExpression = #0.85 s2. \set Staff.midiExpression = #0.7 s2. \set Staff.midiExpression = #0.55 s2.
  \set Staff.midiExpression = #1.0 s2.*12 }
hornFadeMidi = { s2.*371 \set Staff.midiExpression = #0.94 s2. \set Staff.midiExpression = #0.88 s2. \set Staff.midiExpression = #0.82 s2.
  \set Staff.midiExpression = #0.76 s2.*2 }

\layout {
  \context { \Staff \RemoveEmptyStaves \consists "Merge_rests_engraver" soloText = "1." soloIIText = "2." }
  % c415: an empty line between choirs on every system, not only on full pages (Adler II PDF 292: "It is imperative to leave space between
  %   the choirs on the score page. Leave an empty line between the winds and the brass, between the brass and the percussion, between the
  %   percussion and the harp, between the (harp) piano and the strings"; PDF 291 item 2: the separation of choirs "must be immediately
  %   discernable"). With LilyPond's default (padding 1, as inside a choir) the gap on the compressed two-system pages was set by the
  %   notes and dynamics alone: Bn->Hn at 359 (8.8 spaces) narrower than Fl->Cl (9.7), Bn->Hn at 190 (9.2) narrower than Cl->Bn (10.6),
  %   Hn->Hp at 341 equal to Ob->Cl. Padding 3.5 (about one stave height clear of the lowest and highest symbols) applies at every group's
  %   last staff, so the brass sub-brackets (horns, trombones) keep the larger gap they already had on full pages (Ex. XVIII-1, PDF 293).
  \context { \StaffGroup \override StaffGrouper.staff-staff-spacing = #'((basic-distance . 9) (minimum-distance . 7) (padding . 0.5) (stretchability . 5)) \override StaffGrouper.staffgroup-staff-spacing = #'((basic-distance . 10.5) (minimum-distance . 8) (padding . 2.0) (stretchability . 9)) }
  \context { \PianoStaff \override StaffGrouper.staffgroup-staff-spacing = #'((basic-distance . 10.5) (minimum-distance . 8) (padding . 2.0) (stretchability . 9)) }
  % c368: playing words (espress., non div., non arpegg., senza sord., scherz., arco) on an inner staff of a group were struck through by the
  %   group's span bar where they overhang a bar line (45, 73, 81, 105, 121, 185, 225, 253, 269, 277, 300, 339). MOLA PDF 7: bar lines continuous
  %   within each family; PDF 8 and Ex. 7: anchored markings must not collide. The text now sits above the bar lines with a thin outline whiteout
  %   (a white box around the text only; outside-staff placement already keeps it clear of notes and slurs); spacing is unchanged. The muta text at 376 (c268) is a MultiMeasureRestText and keeps its own setting.
  \context { \Staff \override TextScript.whiteout = #1 \override TextScript.whiteout-style = #'box \override TextScript.layer = #3 }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  % c365: Gould, Behind Bars PDF 27, "Stems should be thinner than the stave-line, but not so thin as to reproduce too faintly".
  %   LilyPond's default stem is 1.3 times the stave-line (measured at 600 dpi on page 9: stave-line 3 px, stem 5 px, stave-space 29 px;
  %   Gould's own examples, PDF 27 at 600 dpi: stave-line 3-4 px, stem 3-4 px, stave-space 26.5 px). 0.9 makes the stem a shade thinner
  %   than the stave-line, as the book's engraving is, and still prints as solidly as the stave-lines themselves.
  \context { \Voice \override Stem.thickness = #0.9
  \override Stem.length = #c365-stem-length-container  % c365, see stems.ily (Gould PDF 28-29)
  \consists #middleLineStemEngraver \remove "Dynamic_engraver" \remove "Dynamic_align_engraver"
 \override Script.Y-offset = #stem-side-y-offset  % c125, see stem-side-y-offset
 \override Beam.positions = #gould-ledger-beam-positions }  % c015, see gould-ledger-beam-positions
  % c155: drawn hairpins at least about three stave-spaces long (minimum-length 5 between bounds, bound-padding 0.5 instead of 1.0); the bar widens to take them (springs-and-rods). One-beat swells at 79, 165-166, 181-182,
% 221-222 and the short diminuendos at 339, 355, 357 were drawn 0.9-2.4 spaces long and read as accents (Gould PDF 9: the operator refines the
% software's settings; PDF 55: symbols evenly spaced, none crowded; PDF 53-54: spacing may stretch a little where symbols need room).
% s215 (cycle 215): minimum-length 3.9 (was 5.0) still draws every hairpin at least 3 spaces long (c155's aim; shortest now 3.0, was 4.1), but no longer
%   stretches a one-beat swell's beat to 1.6-1.7 times its neighbours (111/311, 158, 166, 174, 182, 214, 222, 346, 355: Gould PDF 54, notes of equal
%   duration take equal space across a system).
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver"
    \override Hairpin.minimum-length = #3.9 \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods \override Hairpin.bound-padding = #0.5 
    % s305 (cycle 305): Gould PDF 55, "no characters should collide". Dynamics were placed against the glyph outline, so a down-stem
    %   could run into the hook of an f (Bn 69/297, Bn 197, Cl 209/273, Vc 133/321, Tbn 333/339) and Cb's staccato touched "mf" at 135/323.
    %   With box skylines each dynamic clears the stem end and the dot.
    \override DynamicText.vertical-skylines = #ly:grob::simple-vertical-skylines-from-extents }
  % s215 (cycle 215): Gould PDF 57, stems never closer than one space to a barline. Beamed up-stem quavers before a barline stood 0.5-0.8 space from it
%   (Fl/Ob/Cl/C.a. 334, Cl/C.a./Vln II 106, 110, 116, 118, 306, 310, 316, 318, C.a. 189, Vla 195, Cl 246), and down-stems after a barline 0.84-0.95.
%   The barline keeps 0.9 space clear on its left for spacing, and the first note after it sits 1.1 spaces away (default 0.9; PDF 56: a stave-space either side).
  \context { \Score \remove "Bar_number_engraver" \override BarLine.extra-spacing-width = #'(-0.9 . 0) \override BarLine.space-alist.next-note = #'(semi-fixed-space . 1.1) \override SpacingSpanner.shortest-duration-space = #1.6
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
      \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #7 \override BarNumber.outside-staff-horizontal-padding = #0.5 } #})

% c145: a choir-level tempo word or rehearsal letter is dropped when none of the choir's staves is printed in that system (c059's double
% letters above the flutes), and otherwise kept above the choir's top printed staff, so Hn 3·4 carry it when Hn 1·2 rest (87-89, 153, 169).
% Adler part 2 PDF 294: "tempo markings be placed at the top of the score and repeated in the space separating each choir"; Ex. XVIII-1, PDF 293.
#(define (c145-choir-mark grob)
  (let* ((sys (ly:grob-system grob))
         (sup (ly:grob-object grob 'side-support-elements))
         (els (if (ly:grob-array? sup) (ly:grob-array->list sup) '()))
         (live (any (lambda (e)
                 (let* ((orig (or (ly:grob-original e) e))
                        (pcs (if (ly:spanner? orig) (ly:spanner-broken-into orig) '()))
                        (pcs (if (null? pcs) (list e) pcs)))
                   (any (lambda (pc)
                          (and (eq? sys (ly:grob-system pc))
                               (let ((v (ly:grob-parent pc Y)))
                                 (and (ly:grob? v)
                                      (begin (ly:hara-kiri-group-spanner::force-hara-kiri-callback v) (grob::is-live? v))))))
                        pcs)))
                 els)))
    (if live
        (ly:side-position-interface::move-to-extremal-staff grob)
        (ly:grob-set-property! grob 'stencil #f))))
choirMarks = \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" \consists "Staff_collecting_engraver"
  \override RehearsalMark.after-line-breaking = #c145-choir-mark \override MetronomeMark.after-line-breaking = #c145-choir-mark }

% c135: short names keep the instrument keys, as on the first page (MOLA PDF 9, Example 2: "Cl. 1, 2 (B♭)", "Hn. 1, 2 in F")
pc = #(define-music-function (a b) (ly:music? ly:music?) #{ \partCombine #a #b #})

% c360: the music is a variable so that a second, MIDI-only \score can play the timpani rolls as strokes (rolls-midi.ily); the print is unchanged.
\include "rolls-midi.ily"
scherzoMusic = <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl. 1·2" midiInstrument = "flute" }
        << \global \pc \removeWithTag #'part \fluteOne \removeWithTag #'part \fluteTwo \chordFadeMidi >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob. 1·2" midiInstrument = "oboe" }
        << \global \pc \oboeOne \removeWithTag #'part \oboeTwo >>
      \new Staff = "Cor anglais" \with { instrumentName = "Cor anglais" shortInstrumentName = "C.a." midiInstrument = "english horn" }
        << \global \removeWithTag #'part \corAnglais >>
      \new Staff = "Clarinets 1·2" \with { instrumentName = \markup \center-column { "Clarinets 1·2" \small "in A" } shortInstrumentName = \markup \center-column { "Cl. 1·2" \small "(A)" } midiInstrument = "clarinet" }
        << \global \pc \removeWithTag #'part \clOne \removeWithTag #'part \clTwo \chordFadeMidi >>  % c255: Cl 1's part-only muta (376) stays out of the score
      % c036: "(low C)" dropped: the lowest note is now D2 (written E3), the standard low E; an extension to low C is not available in every orchestra (Adler PDF 216)
      \new Staff = "Bass clarinet" \with { instrumentName = \markup \center-column { "Bass clarinet" \small "in B♭" } shortInstrumentName = \markup \center-column { "B.cl." \small "(B♭)" } midiInstrument = "clarinet" }
        << \clef bass \global \bassCl >>
      \new Staff = "Bassoons 1·2" \with { instrumentName = "Bassoons 1·2" shortInstrumentName = "Bn. 1·2" midiInstrument = "bassoon" }
        << \clef bass \global \pc \removeWithTag #'part \bsnOne \bsnTwo >>
      \new Staff = "Contrabassoon" \with { instrumentName = "Contrabassoon" shortInstrumentName = "Cbn." midiInstrument = "bassoon" }
        << \clef bass \global \transposition c \transpose c c' \removeWithTag #'part \cbsn >>
    >>
    % c055: tempo words and rehearsal letters also above the brass, the middle choir of the page (Adler part 2 PDF 294: "tempo markings
    % be placed at the top of the score and repeated in the space separating each choir"; Example XVIII-1, PDF 293)
    % c059: the engravers sit in the Horns 1·2 staff, not the brass StaffGroup: on systems with no brass staff (29, 185, 253) the group's
    %   marks lost their staves and printed a second time above the flutes ("B" over "B", "Q" on top of "Tempo I"); now they vanish with the staff.
    % c145: back on the brass StaffGroup (as c055), with c145-choir-mark doing c059's job of dropping the marks where no brass staff is printed.
    \new StaffGroup \with \choirMarks <<
      % c145: horns 1-4 and the three trombones each joined by a sub-bracket inside the brass bracket (Adler part 2 PDF 294: "heavy brackets set off
      % the choirs; and an additional brace clarifies instruments of a family"; Ex. XVIII-1, PDF 293, joins I-II with III-IV and the three trombones)
      % c250: short names of the horns and trumpets "in F" / "in C", as movement I (v266) and movement II (v261) print them (MOLA PDF 9, Ex. 2: "Hn. 1,2 in F",
      %   "Tpt. 1, 2 in C"; the clarinets keep "(A)", as MOLA's "Cl. 1,2 (B♭)" and the other movements' clarinets do)
      \new StaffGroup \with { systemStartDelimiter = #'SystemStartSquare \override InstrumentName.padding = #1.2 } <<
      \new Staff = "Horns 1·2" \with { instrumentName = \markup \center-column { "Horns 1·2" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 1·2" \small "in F" } midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnOne \removeWithTag #'part \hnTwo \hornFadeMidi >>
      \new Staff = "Horns 3·4" \with { instrumentName = \markup \center-column { "Horns 3·4" \small "in F" } shortInstrumentName = \markup \center-column { "Hn. 3·4" \small "in F" } soloText = "3." soloIIText = "4." midiInstrument = "french horn" }
        << \global \pc \removeWithTag #'part \hnThree \removeWithTag #'part \hnFour >>
      >>
      \new Staff = "Trumpets 1·2" \with { instrumentName = \markup \center-column { "Trumpets 1·2" \small "in C" } shortInstrumentName = \markup \center-column { "Tpt. 1·2" \small "in C" } midiInstrument = "trumpet" }
        << \global \pc \removeWithTag #'part \tptOne \removeWithTag #'part \tptTwo >>
      % c020: Trumpet 3 is tacet in the scherzo (cyclic rule): its empty staff removed and the tacet stated under the title, as movement II states "Trumpets tacet"
      \new StaffGroup \with { systemStartDelimiter = #'SystemStartSquare \override InstrumentName.padding = #1.2 } <<
      \new Staff = "Trombones 1·2" \with { instrumentName = "Trombones 1·2" shortInstrumentName = "Tbn. 1·2" midiInstrument = "trombone" }
        << \clef bass \global \pc \removeWithTag #'part \tbnOne \removeWithTag #'part \tbnTwo >>
      \new Staff = "Bass trombone" \with { instrumentName = "Bass trombone" shortInstrumentName = "B.tbn." midiInstrument = "trombone" }
        << \clef bass \global \removeWithTag #'part \bassTbn >>
      >>
      \new Staff = "Tuba" \with { instrumentName = "Tuba" shortInstrumentName = "Tba." midiInstrument = "tuba" }
        << \clef bass \global \removeWithTag #'part \tuba >>
    >>
    % Timpani in its own bracket, as in movement I (Adler part 2 PDF 293-294)
    \new StaffGroup \with { \remove "Span_bar_engraver" } <<
    \new Staff = "Timpani" \with { \remove "Key_engraver" instrumentName = "Timpani" shortInstrumentName = "Timp." midiInstrument = "timpani" }
      << \clef bass \global \removeWithTag #'part \timp >>
    >>
    \new PianoStaff \with { connectArpeggios = ##t instrumentName = "Harp" shortInstrumentName = "Hp." } <<
      \new Staff = "Harp RH" \with { midiInstrument = "orchestral harp"
        % c125: two-note rolls in the RH were drawn about two spaces tall, the size and shape of a quarter rest, right after the r4 in 7, 9-11, 13, 72-73 (Gould PDF 55-56: no symbol placed so it can be mistaken for another); lengthen each roll by one space at both ends
        \override Arpeggio.positions = #(lambda (grob) (let ((p (ly:arpeggio::calc-positions grob))) (cons (- (car p) 1) (+ (cdr p) 1)))) } << \global \removeWithTag #'part \harpR >>
      \new Staff = "Harp LH" \with { midiInstrument = "orchestral harp" \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \global \removeWithTag #'part \harpL >>
    >>
    % c005: marks and tempo above the top visible string staff (MOLA PDF 4), not only above Vln I, which is hidden in some systems
    \new StaffGroup \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" \consists "Staff_collecting_engraver" } <<
      \new Staff = "Violins I" \with { instrumentName = "Violins I" shortInstrumentName = "Vln. I" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnOne >>
      \new Staff = "Violins II" \with { instrumentName = "Violins II" shortInstrumentName = "Vln. II" midiInstrument = "string ensemble 1" }
        << \global \removeWithTag #'part \vlnTwo \chordFadeMidi >>  % c426: Vln II's part-only 'via sord.' at 185 stays out of the score
      \new Staff = "Violas" \with { instrumentName = "Violas" shortInstrumentName = "Vla." midiInstrument = "viola" }
        << \clef alto \global \vla \chordFadeMidi >>
      \new Staff = "Violoncellos" \with { instrumentName = "Violoncellos" shortInstrumentName = "Vc." midiInstrument = "cello" }
        << \clef bass \global \vc \chordFadeMidi >>
      \new Staff = "Double basses" \with { \consists "Bar_number_engraver" \override BarNumber.direction = #DOWN \override BarNumber.self-alignment-X = #CENTER \override BarNumber.break-align-symbols = #'(staff-bar) \override BarNumber.break-visibility = ##(#f #t #t) \override BarNumber.font-size = #-1 \override BarNumber.padding = #1 \override BarNumber.outside-staff-priority = #1000 \override BarNumber.staff-padding = #7 \override BarNumber.outside-staff-horizontal-padding = #0.5 instrumentName = "Double basses" shortInstrumentName = "Cb." midiInstrument = "contrabass" }
        << \clef bass \global \transposition c \transpose c c' \cb \chordFadeMidi >>
    >>
  >>
\score { \scherzoMusic \layout { } }
\score {
  \rollStrokes #16 \scherzoMusic
  \midi { \context { \Score midiChannelMapping = #'instrument
    % \subP is a markup dynamic ("sub. p"): give it the p volume. sf/fp were unmapped and fell back to the default (0.71, louder than ff).
    dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42) ("sfp" . 0.42)) #f)
      0.42)) }
    % Harp: one set of dynamics for both hands (printed under the LH); the RH staff has none, so its notes played at the default volume.
    \context { \PianoStaff \consists "Dynamic_performer" }
    % c124: part-combined staves: one set of dynamics per staff. With the performer in each Voice, the partCombine "shared" voice did not
    %   receive the dynamics written in the parts and kept a stale or default level: Tbn 1·2 played 105-120 louder than any other track in the
    %   tutti where the print says f; Hn 3·4 played 77-80 and 85-88 at mf in the pp F-major episode. The shared staves carry equal simultaneous
    %   dynamics (score rule), so a staff-level performer plays what is printed. MIDI only; the print is unchanged.
    \context { \Staff \consists "Dynamic_performer" }
    \context { \Voice \remove "Dynamic_performer" } }
}

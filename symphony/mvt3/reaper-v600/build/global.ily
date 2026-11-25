\version "2.26.0"
% c018: down-bow then up-bow on one long note (Adler ch. 2, PDF 38, Beethoven Coriolanus) so the next attack is again a down-bow
dnup = ^\markup \concat { \musicglyph "scripts.udownbow" \hspace #1.2 \musicglyph "scripts.uupbow" }
% c035: "change bow at will" on two lines, so the text stays inside its bar (it ran across the next barline at 224, 226, 229, 235, 255: Gould PDF 55, no characters may collide)
cbaw = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "change bow" "at will" }
% c325 (Adler part 2 PDF 291 item 1 and PDF 301, proofreading; Gould PDF 41, 55: no characters may collide): "unis., change" was wider than the whole-note bars
% it stands in and ran across the next barline into the following note (Vc 224 into 225, Vln II 226 into 227); "unis." now on its own line, so the text is no wider than \cbaw
cbawU = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "unis.," "change bow" "at will" }
% c395 (Gould PDF 54: equal durations take equal space across a system; PDF 57: added symbols should distort the rhythmic spacing as little as possible):
% at 217 c265's \textLengthOn under "change bow at will" (Vln II, Vc, Cb) gave the violas' first minim 12.3 spaces and the second 5.4, against 3.6 for the minims of 218;
% the words now stand on three lines, no wider than "change", so the bar keeps the system's spacing and the text still ends before the 217|218 barline
cbawN = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "change" "bow" "at will" }
% c415 (Adler part 2 PDF 291 item 1 and PDF 301, proofreading; Gould PDF 41, 55, 57): in the whole-note bars at 2 = 56 and under the allargando the two-line texts still ran
% into the next barline (Vc and Cb 224 "change bo|w", Vln II 226 touching; Cb 139, Vc and Cb 149 in retr). Those places now use the three-line \cbawN or this four-line form.
cbawUN = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "unis.," "change" "bow" "at will" }
% c368 gave bar 243 score-only extra spacing so "mf cresc. molto" ended inside the bar; replaced in c395 by the two-line text below (see \crescMolto).
% c368 (MOLA PDF 12, Example 7: a long crescendo written as words, "cresc. molto"; PDF 10, Example 3: a crescendo ends on a printed level): text crescendo
% over two dynamic levels, used at 243-246 (strings mf to the ff of 247 under the stringendo); it plays in the MIDI like a hairpin
% c395 (Gould PDF 54: notes of equal duration take equal space for an entire system; PDF 55, 57: no collisions, and distort the rhythmic spacing as little as possible):
% c368 widened bar 243 alone (spacing-increment 5.0) so "mf cresc. molto" ended inside it; its minims took 6.8 and 11.5 spaces against 3.1 for the minim at 245 and
% 5.2 for the dotted minim at 244 on the same system. The words now stand on two lines, as \cbaw does (c035), and start at 244 (mf stays at 243; the push begins
% at 245, c348), so they fit that bar at the system's own spacing.
crescMolto = #(make-music 'CrescendoEvent 'span-direction START 'span-type 'text
  'span-text (markup #:override '(baseline-skip . 2.3) #:column ("cresc." "molto")))
% c405 (MOLA PDF 7: the page layout must let the player read on after a turn; PDF 8: proofread the horizontal lines of the score; Example 7, PDF 12: a long
% change written as words, "cresc. molto"): a crescendo or diminuendo written as words ("cresc." with dashes) that runs across a system or page break
% continued on the new line as bare dashes (141-145: Bn, Cbn, timpani, Vla, Vc, Cb from page 7 to page 8), so after the turn nothing said what the line meant.
% The continuation now restates the word in parentheses, "(cresc.)". Hairpins are unchanged; MIDI unchanged.
#(define (c405-broken-cresc grob)
   (dynamic-text-spanner::before-line-breaking grob)
   (let ((t (ly:grob-property grob 'text #f)))
     (if (markup? t)
         (ly:grob-set-nested-property! grob '(bound-details left-broken text)
           (make-concat-markup (list "(" t ")"))))))
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% c185 (MOLA PDF 4: placement of measure numbers the same throughout; Gould PDF 19: every symbol measured from the stave): on pages 12-16 a dynamic at the barline
% (212, 259, 263, 278) pushed that bar number about 1.2 spaces below the row of the others. From the page turn at 209 the whole row sits 1.3 spaces lower, clear of those dynamics.
bnLow = \tag #'score { \override Staff.BarNumber.staff-padding = #6.8 }
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing. Its unit is the quarter note (2 = 84 is \mt 168).
% c075: tagged 'score, so a part built with \removeWithTag #'score \global does not split its multi-measure rests at these silent steps (MOLA PDF 5: rests as numbered ranges)
mt = #(define-music-function (bpm) (integer?) #{ \tag #'score { \set Score.tempoWholesPerMinuteAsMoment = #(ly:make-moment bpm 4) } #})
% c075 (MOLA PDF 7: in the parts, page turns fall in rests): the score's line and page breaks are tagged 'score so the parts (parts-test.ly, \removeWithTag #'score \global) lay out their own pages
% c215 (Gould PDF 55, "Notes of bar-length duration": a bar holding one bar-length note in every part, with no other duration, puts the note just left of the centre of the bar, not against the barline):
% score-only extra space after the barline in such mid-system bars (96, 97, 136-138, 147, 221)
cen = \tag #'score { \once \override Score.BarLine.space-alist.next-note = #'(semi-fixed-space . 3.2) }
% c485 (Gould PDF 55: "when there are other durations in other parts, the single duration is placed at the beginning of the bar as normal"): 97 (Cl 1's half rest and half note) and 138 (Tpt 1-2's quaver) lost \cen; 5 (one bar-length note in every part, mid-system after a plain barline) gained it. 135 and 219 follow a key change, whose signature already sets the note near the bar's centre (an override there was tested and changed nothing)
% c315 (MOLA PDF 5: rehearsal letters and tempo changes in every part; Example 4, PDF 10: "[E] Tempo I", the boxed letter at the barline and the tempo word after it on one line):
% in the parts the letter and the tempo text were two grobs placed independently, so where both fall on one bar (D, F, K, N, O, P, Q, R, T) the letter sat above the tempo
% at some letters and beside or below it at others (Trumpet 1: D above, K below; percussion: D, K, N, R at stave height). Parts only: the tempo text is drawn inside the
% letter's stencil, on the letter's baseline, and the separate tempo grob is omitted; the letter, not the whole line, is centred on the barline.
% The score (letter above its tempo text, c185, c225) and the MIDI are unchanged.
#(define (c315-letter-centre grob)  ; self-alignment-X that puts the letter's centre (not the whole line's) on the barline
   (let* ((l (ly:stencil-extent (ly:text-interface::print grob) X))
          (c (ly:stencil-extent (ly:grob-property grob 'stencil) X))
          (w (- (cdr c) (car c))))
     (if (> w 0) (- (/ (* 2 (- (/ (+ (car l) (cdr l)) 2) (car c))) w) 1) 0)))
#(define ((c315-letter-with-tempo tm) grob)
   (ly:stencil-combine-at-edge (ly:text-interface::print grob) X RIGHT
     (grob-interpret-markup grob (markup #:fontsize -2 tm)) 0.8))
mmk = #(define-scheme-function (txt n) (markup? string?)
  #{ \markup \line { \bold #txt \normal-text \concat { "(" \fontsize #-1 \general-align #Y #DOWN \note {2} #UP #(string-append " = " n ")") } } #})
% The score keeps global's 'part tags (score.ly does not remove them), so \lt acts only when parts-head.ily has set isPartsBook before including this file.
% c525 (MOLA PDF 5 and Example 4, PDF 10: each letter and tempo word stands over its own bar or rest; PDF 8 and Example 7, PDF 12: no colliding marks in extracted parts):
% in the parts a multi-measure rest that starts at a lettered tempo change is made at least as long as the letter and its tempo text, so the text ends inside its own rest.
% Before, "D Poco meno mosso (half = 72)" ran past the 16-bar rest 51-66 and the next letter, E (67), was set on top of "meno mosso" in eight parts (Ob 1, Bn 2, Hn 1,
% Tpt 2, Tpt 3, Tbn 1, Tbn 2, tuba) and stacked over it in nine more; A (11) stood over "Allegro con fuoco" in the trumpets, the harp and other parts resting 1-10.
% With \partNoBreak before D, 51 never starts a line, where a rest's length counts from the clef. Page counts and page turns of all 30 parts unchanged.
#(define ((c525-rest-fits-mark tm) grob)
   (let* ((t (grob-interpret-markup grob tm))
          (w (interval-length (ly:stencil-extent t X))))
     (max 12 (+ w 10.0))))
% 10 staff spaces allow for the letter and for the clef, key and time signature, which a rest starting a line must also clear (its length is measured from the line start).
% The spanner rods that hairpins use (c045, c315) are added to the rest's own.
#(define (c525-rest-rods grob) (ly:multi-measure-rest::set-spacing-rods grob) (ly:spanner::set-spacing-rods grob))
% \ltRest (parts only, like \lt): a multi-measure rest starting here is long enough for the text tm.
ltRest = #(define-music-function (tm) (markup?)
  (if (not (eq? (ly:parser-lookup 'isPartsBook) #t)) (make-music 'SequentialMusic 'elements '())
  #{ \tag #'part { \once \override Staff.MultiMeasureRest.minimum-length = #(c525-rest-fits-mark tm)
                   \once \override Staff.MultiMeasureRest.springs-and-rods = #c525-rest-rods } #}))
% \partNoBreak: \noBreak in the parts book only (the score keeps global's 'part tags, so \tag #'part would also reach the score).
partNoBreak = #(if (eq? (ly:parser-lookup 'isPartsBook) #t) #{ \noBreak #} (make-music 'SequentialMusic 'elements '()))
lt = #(define-music-function (tm) (markup?)
  (if (not (eq? (ly:parser-lookup 'isPartsBook) #t)) (make-music 'SequentialMusic 'elements '())
  #{ \ltRest #tm
     \tag #'part { \once \override Score.RehearsalMark.stencil = #(c315-letter-with-tempo tm)
                   \once \override Score.RehearsalMark.self-alignment-X = #c315-letter-centre
                   \once \omit Score.MetronomeMark } #}))
global = {
  \accidentalStyle Score.modern
  % c395 (Gould PDF 56: allow a stave-space on either side of a barline; PDF 57: stems must never come closer to a barline than one space): in close spacing
  % LilyPond set the last stem of a bar 0.4 space from the barline (72 bars, mostly on pages 14-16). Score only: the barline counts 0.75 space wider on its left
  % in spacing, so every stem stays at least one space from it; on page 15 (253-265), the tightest system, 0.58 (at least 0.86 space), to keep 16 pages.
  \tag #'score \override Score.BarLine.extra-spacing-width = #'(-0.75 . 0)
  \key c \minor \time 2/2
  % c525: the rest that opens a part (Tpt 1-3, harp, B. cl., C.A., Bn 2, Cbsn, Tbn 1-2, tuba) is long enough for "Allegro con fuoco (half = 84)", so A (11) is not set above "fuoco"
  \ltRest \mmk "Allegro con fuoco" "84"
  \tempo "Allegro con fuoco" 2 = 84
  % 1-10: introduction. After the scherzo (movement III) and a pause: its last G sharp (Hn 1, Vln I) is taken as A flat, the root of the German sixth, ff, resolving to V of C
  s1*4 \cen s1 s1*5
  \mark \default % A 11: first theme
  % c251: score-only staff distances for the two systems of page 2 (14-26, 27-36), measured from a build with staff padding 0.5;
  % c585: each about 1% closer (as LilyPond compressed them), so the bar-number row at c585's uniform 6.8 spaces (score.ly, Double basses) still fits page 2;
  % the tuba's F1 at 27-32 adds a staff to the second system, and the default padding left page 2 over-full by 8.4 staff spaces. Other pages unchanged.
  s1*3 \tag #'score \pageBreak \tag #'score \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details #'((alignment-distances . (12.04 10.67 11.76 8.61 8.61 11.04 9.06 10.74 8.64 8.64 8.61 8.61))) s1*13 % c217: pages 1-3 fixed as in v217 (1-13, 14-36, 37-66), so Cl 1's countersubject 27-34 does not move the free breaker
  \tag #'score \break \tag #'score \noPageBreak \tag #'score \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details #'((alignment-distances . (9.81 13.00 8.88 14.58 8.61 13.00 12.38 11.11 8.78 8.61 11.28 14.99 10.53 9.57 10.74 9.98))) \mark \default % B 27: counterstatement, theme in the bass, modulating to V of E flat
  s1*10 \tag #'score \pageBreak s1*6
  \mark \default % C 43: transition over the B flat pedal
  s1*6 \tempo \markup \normal-weight \italic "poco rit." \mt 160 s1 \mt 150 s1
  \partNoBreak \bar "||" \tag #'score \break \key es \minor \lt \mmk "Poco meno mosso" "72" \mark \default % D 51: second theme, E flat minor, trumpet solo
  \tempo "Poco meno mosso" 2 = 72
  s1*16
  \bar "||" \tag #'score \pageBreak \key es \major \mark \default % E 67: second theme in E flat major, violins
  % c235 (Adler part 2 PDF 299, item 4, and PDF 301, proofreading; Gould PDF 55: characters at least half a space apart): in parts with the two-bar rest 81-82 (Tpt 2-3, B.cl., tuba, Ob 2),
  % "animando" ended against "Tempo I" at 83; parts only, the text keeps a space clear on each side, so it goes to its own tier instead of widening the bars
  % c298 (expression; A&S Unit 21, PDF 348 sec. 3: a suspension's resolution should sound like a relaxation, a decrease in intensity; PDF 359-360 sec. 21: delaying a resolution builds tension;
  %   PDF 353-354, Ex. 21-15e-f: the 7/6 over V7 is given its full length): 'animando' moves from 81 to 82, so the 7/6 suspension over V7 at 80.4-81.2 (c241) and its diminuendo resolve in tempo,
  %   and the push comes with the crescendo run of 82 into Tempo I (c113: 'animando now carried' by that run). MIDI 144 through 81, 152 and 160 on the halves of 82, 168 at 83.
  s1*15 \tag #'part \once \override Score.MetronomeMark.outside-staff-horizontal-padding = #1 \tempo \markup \normal-weight \italic "animando" \mt 152 s2 \mt 160 s2
  % c395 (Gould PDF 53: thin double barlines mark divisions between sections): F (83, closing group, Tempo I) and T (273, Largamente) were the only lettered
  % tempo changes without one; D, K, N, O, P, Q and R have it
  \bar "||" \lt \mmk "Tempo I" "84" \mark \default % F 83: closing group
  \tempo "Tempo I" 2 = 84
  s1*4 \tag #'score \pageBreak s1*9 \cen s1 s1 s1 % c055: page turn before the 6/3 bridge (87), not inside it
  \bar "||" \key f \minor \mark \default % G 99: development, F minor
  s1*16
  % c585: score-only staff distances for both systems of page 7 (115-127, 128-143), measured from the build with the bar-number row at 6.8 spaces (MOLA PDF 4), which left the free layout over-full by 1.7 spaces
  \bar "||" \tag #'score \pageBreak \tag #'score \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details #'((alignment-distances . (13.48 11.22 8.13 11.22 14.85 11.70 12.00 14.34 9.30))) \key g \minor \mark \default % H 115: G area (bassoon, then harp)
  s1*8
  \bar "||" \key g \major
  s1*5 \tag #'score \break \tag #'score \noPageBreak \tag #'score \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details #'((alignment-distances . (10.80 13.20 11.15 9.06 10.12 13.48 12.42 8.20 7.38 7.89 9.26 13.34 13.07 11.49 12.93 12.35 12.31))) s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak % c187: system break at 128 fixed, as in v187; c195: written out (an unfolded repeat split the parts' rests 128-134 into single bars)
  \bar "||" \key c \minor \mark \default % J 135: retransition, G with B natural in the bass
  % c187: page turns at 144 and 158 fixed, as in v187 (the free breaker otherwise spread 115-170 over four pages)
  s1 \tag #'score \noBreak \cen s1 \tag #'score \noBreak \cen s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \pageBreak s1*3 \cen s1 s1 \tempo \markup \normal-weight \italic "allargando" \mt 156 s1 \mt 140 s1
  % c065 (Gould PDF 53: thin double barlines mark divisions between sections): the recapitulation (151) and its second theme (171) get the double bar that 51 and 67 have
  % c235 (Adler part 2 PDF 299, item 4: chaos may result if a rehearsal letter is missing from a resting player's part; PDF 301: proofread the parts): the score-only paddings of K, N, O, R
  % (c185, c225) are tagged 'score; in the parts they pushed N and O into the system before (cor anglais: N under 181, O under 184) and R into the 239 system
  \bar "||" \tag #'score \once \override Score.RehearsalMark.outside-staff-horizontal-padding = #2 \lt \mmk "Tempo I" "84" \mark \default % K 151: recapitulation. c225 (MOLA PDF 4, as c185 at R): K, N and O stand above their tempo text, as D, F, P, Q, R, T do
  \tempo "Tempo I" 2 = 84
  % c073 (form): no poco rit. at 169-170 and no Poco meno mosso at 171. The recapitulated second theme keeps Tempo I, so it does not replay the exposition's
  % pacing (51 and 67 are Poco meno mosso); Dvorak 9/iv (corpus: no tempo change at its second theme, 68; its Poco meno mosso at 214-226 is the soft reprise of the first
  % theme, Tempo I from 227) and Dvorak 7/iv (no meno mosso for its second theme) keep their finales' second themes at the main tempo.
  s1*7 \tag #'score \pageBreak s1*13
  \bar "||" \tag #'score \pageBreak \mark \default % L 171: second theme in C minor, muted trumpet with cor anglais (at Tempo I since c073)
  s1*16
  % c055 (Adler part 2 PDF 299, item 4; PDF 291, item 3): a letter at the C-major second theme; L-M was 28 bars, the longest gap
  % c073 (form; A&S PDF 95: a tonic's meaning comes from its function): the major statement goes to A flat, the key the deceptive cadence of 186 opens, so C major,
  % its E natural (the violas' thread pitch) and the tonic as a goal are heard first at the arrival (223). The rit. steps are now relative to Tempo I.
  \bar "||" \tag #'score \break \key aes \major \mark \default % M 187: second theme in A flat major, violins (was C major until c073)
  % c255 (MOLA PDF 8 and Example 7, PDF 12: extracted parts must be proofread for colliding marks): in the Trumpet 1 part "poco rit." (197) ran into "Tempo I" (199) and in the harp part
  % "allargando" (221) touched "Maestoso" (223); parts only, as c235 did for "animando" at 81, the text keeps a space clear on each side and takes its own tier
  s1*10 \tag #'part \once \override Score.MetronomeMark.outside-staff-horizontal-padding = #1 \tempo \markup \normal-weight \italic "poco rit." \mt 160 s1 \mt 150 s1
  \bar "||" \tag #'score \pageBreak \key c \minor \tag #'score \once \override Score.RehearsalMark.outside-staff-horizontal-padding = #2 \lt \mmk "Tempo I" "84" \mark \default % N 199: coda, the last C-minor tutti
  % c111 (hypermetre: 199-204 is movement I's hammered tutti (its 27-32), 205-210 the F1-head build over A flat in 2-bar units): the MIDI steps were at 203 and 207, the first inside the six-bar quotation;
  % the quotation now stays at Tempo I and the acceleration starts with the build at 205 (printed there), 172 at 205, 176 at 207 (2 = 88, as before)
  % c179 (holistic; Adler part 2 ch. 16, adler2 PDF 201: a gradual change is written out step by step): MIDI 86 (205), 88 (206), 90 (207-208), 92 (209-210), one step per bar under the printed "poco a poco" instead of a 5% jump on 205; end tempo unchanged.
  % c173 (form): the MIDI acceleration was 84 -> 86 -> 88 (+5%, at the threshold of hearing); now 88 (205), 90 (207), 92 (209-210), so the build is heard to press on and Largamente 2 = 72 at 211 broadens by a fifth. Printed marks unchanged; R stays 2 = 88.
  \tempo "Tempo I" 2 = 84
  % c151 (page cap): 199-210 stay one system on one page; the accidental of the violins' G flat at 210 (c151) otherwise pushes 206-210 onto a page of its own
  s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak s1 \tag #'score \noBreak \tempo \markup \normal-weight \italic "poco a poco più animato" \mt 172 s1 \tag #'score \noBreak \mt 176 s1 \tag #'score \noBreak \mt 180 s1 \tag #'score \noBreak s1 \tag #'score \pageBreak \mt 184 s1 \tag #'score \noBreak s1
  \bar "||" \tag #'score \noBreak \key des \major \tag #'score \once \override Score.RehearsalMark.outside-staff-horizontal-padding = #9 \lt \mmk "Largamente" "72" \mark \default % O 211: D flat episode, trumpets (c013: theme B augmented, 211-218)
  \tempo "Largamente" 2 = 72
  s1*8
  \bar "||" \key c \major
  % c045 (MOLA PDF 5: avoid over-crowding within each measure; Example 7, PDF 10: no colliding markings): 219-222 are the narrowest bars of the score and the
  % mp < f hairpins at 220-222 were drawn about 1 mm long; give hairpins a minimum length here so the bars widen to hold them
  \override Staff.Hairpin.minimum-length = #8 \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods
  s1*2 \cen \tag #'part \once \override Score.MetronomeMark.outside-staff-horizontal-padding = #1 \tempo \markup \normal-weight \italic "allargando" \mt 124 s1 \mt 112 s1
  \revert Staff.Hairpin.minimum-length \revert Staff.Hairpin.springs-and-rods
  \bar "||" \tag #'score \pageBreak \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.3 \lt \mmk "Maestoso" "56" \mark \default % P 223 (was 219; O until c055): C major arrival and chorale
  \tempo "Maestoso" 2 = 56
  s1*12
  \bar "||" \lt \markup \column { \mmk "Poco più mosso" "66" \line { \normal-weight \italic "molto cantabile" } } \mark \default % Q 235 (was 231): movement I's second theme in C major, violins
  % c185 (Gould PDF 55-57 and MOLA PDF 8: no marks set over one another): the tempo text on two lines; on one line it ran over 235-246 in the parts with rests here
  % (Fl 2, Ob 2, B.cl., Cbsn, Tbn 1, Tuba, percussion) and forced "poco a poco stringendo" (243) and R/Più allegro (247) into a second and third tier above it
  \tempo \markup \override #'(baseline-skip . 2.4) \column { "Poco più mosso" \line { \normal-weight \italic "molto cantabile" } } 2 = 66
  % c023: page break before 239 (start of the second phrase of the second-theme head); with the 8 bars added at 269-276 the free page breaker otherwise turns the page after 239, inside that phrase
  % c225 (MOLA PDF 8 and Example 7, PDF 12: no colliding marks): "poco a poco stringendo" on two lines; on one line it ran from 243 into 245 and touched the violins' "unis."
  % c348 (tempo; A&S Unit 3, PDF 49: the impression of tempo comes from the pace of the beats, which goes with the rate of chord change and of the melody's main tones, not with the quickest notes):
  %   243-244.5 hold one harmony (III# then the cadential 6/4) under the horn call in augmentation, whose notes enter on weak beats (243.3, 244.2, 245.3) with no part marking the beat,
  %   so a stringendo there cannot be heard and only hurries the call; the push now starts at 245 with the violins' and violas' eighth-note run and the timpani crescendo, which carry a beat.
  %   243-244 stay at 2 = 66 (Poco più mosso); MIDI 68, 73 (245.3), 78 (246), 83 (246.3), 88 at R (247) as before. "stringendo" fits on one line (c225's two lines are no longer needed).
  s1*4 \tag #'score \pageBreak s1*4 s1 s1 \tempo \markup \normal-weight \italic "stringendo" \mt 136 s2 \mt 146 s2 \mt 156 s2 \mt 166 s2 % c076: the MIDI stringendo reaches 2 = 88 at R (247), not already at 246
  % c185 (MOLA PDF 4: rehearsal letters placed the same way at every landmark): R sat at stave height beside "Più allegro", where P, Q, S and T stand above their tempo text
  \bar "||" \tag #'score \once \override Score.RehearsalMark.outside-staff-horizontal-padding = #2 \lt \mmk "Più allegro" "88" \mark \default % R 247 (was 243): Più allegro (Allegro molto 2 = 100 until Dan's note 2026-10-13: too fast), both heads of movement I in C major
  \tempo "Più allegro" 2 = 88
  % c395: page 15 holds 253-265 as one system, as in v395, now fixed (the free breaker moved 253 onto page 14 once bar 243 lost its extra width,
  % and split 253-279 into four systems with the barline clearance below)
  s1*6 \tag #'score \pageBreak \tag #'score { \override Score.NonMusicalPaperColumn.line-break-permission = ##f \override Score.BarLine.extra-spacing-width = #'(-0.58 . 0) } s1*2
  % c013: the chorale's last statement (255-264) stays in the Più allegro, written in doubled values (Brahms 1/iv 407ff), instead of Maestoso 2 = 60
  % c038 (expression; Dvorak 7/iv "Molto maestoso" and 9/iv "Meno mosso e maestoso" over the closing tremolo/held chords): 273-279 Largamente, 2 = 72 (the tempo of 211), for the closing chain G-F sharp-F-E, the scherzo quotation and the last chord
  % c039 (Rimsky-Korsakov Ex. 209, PDF 375; Ex. 272, PDF 438): the broadening into 273 is written out over 271-272 (was 2 = 100 straight to 72)
  % c045 (MOLA PDF 4: rehearsal letters at the landmarks of the music): 33 bars of Q had one letter; R at the chorale's last statement (255), S at Largamente (273); since c055 (letter M added at 187) these are S and T
  \mark \default s1*10 s1 \tag #'score \pageBreak \tag #'score \override Score.BarLine.extra-spacing-width = #'(-0.75 . 0) s1*5 \tempo \markup \normal-weight \italic "allargando" \mt 164 s1 \mt 152 s1 \bar "||" \lt \mmk "Largamente" "72" \mark \default \tempo "Largamente" 2 = 72 s1*6 s1
  \bar "|."
}
% c095 (MOLA PDF 5: rests in the parts as one numbered range; Gould PDF 23: rests drawn so the next entry is easy to find): in a part, every new spacer in
% \global and every new R event started a new multi-measure rest, so the score-only \mt steps and page breaks, removed with their tags, still left
% splits (Tpt 1: 81 | 82, 83-86 | 87-90; percussion 247-262 drawn as sixteen single bars). For the parts only, adjacent plain skips and adjacent plain
% full-bar rests (no text, dynamic or fermata attached; bar checks between them dropped) are joined. Marks, tempo marks, key changes and double bars still divide rests.
#(define (c095-mergeable? x)
  (and (memq (ly:music-property x 'name) '(SkipEvent MultiMeasureRestMusic))
       (null? (ly:music-property x 'articulations))
       (null? (ly:music-property x 'tags))))
#(define (c095-join a b)
  (let ((r (+ (ly:moment-main (ly:music-length a)) (ly:moment-main (ly:music-length b)))))
    (make-music (ly:music-property a 'name) 'duration (ly:make-duration 0 0 r))))
mergeRests = #(define-music-function (m) (ly:music?)
  (music-map
    (lambda (x)
      (if (eq? (ly:music-property x 'name) 'SequentialMusic)
          (let loop ((es (ly:music-property x 'elements)) (acc '()) (bcs '()))
            (cond
              ((null? es) (ly:music-set-property! x 'elements (append (reverse acc) (reverse bcs))) x)
              ((and (eq? (ly:music-property (car es) 'name) 'BarCheckEvent) (pair? acc) (c095-mergeable? (car acc)))
               (loop (cdr es) acc (cons (car es) bcs)))
              ((and (c095-mergeable? (car es)) (pair? acc) (c095-mergeable? (car acc))
                    (eq? (ly:music-property (car es) 'name) (ly:music-property (car acc) 'name)))
               (loop (cdr es) (cons (c095-join (car acc) (car es)) (cdr acc)) '()))
              (else (loop (cdr es) (cons (car es) (append bcs acc)) '()))))
          x))
    m))

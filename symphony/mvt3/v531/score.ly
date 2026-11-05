\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "IV. Finale: Allegro con fuoco"
  % c399 release check (as movement I v421 and scherzo v400; MOLA PDF 6: "print date, or revision date"): the cycle stamp "draft vNNN" becomes the release form, version and date.
  subsubtitle = \markup \center-column { "Full score in C — draft v531" \small "Contrabassoon and double basses sound an octave lower than written (double basses: C extension at 75–76, 166, 174–183 and 189)" \small "After movement III (Scherzo): a pause" \small "Duration: about 7 minutes" \small "Instrumentation: 2 flutes, 2 oboes, cor anglais in F, 2 clarinets in B♭, bass clarinet in B♭, 2 bassoons, contrabassoon — 4 horns in F, 3 trumpets in C, 2 trombones, bass trombone, tuba —" \small "4 timpani (G, A♭, C, E♭), percussion (2 players: crash cymbals, bass drum), harp — strings" \small \line { "Percussion stave (one line):" \musicglyph "noteheads.s2xcircle" "above the line = crash cymbals (pair);" \musicglyph "noteheads.s2" "below the line = bass drum" } }  % c495 (MOLA PDF 6: an explanation of non-standard notation follows the instrumentation; PDF 5: a notation key for the percussion, as the part has had since c255): the one-line drum stave's key. c345: MOLA PDF 6, the score names the full instrumentation, the keys of the transposing instruments and the percussion with its number of players
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
\addQuote "clOne" { \removeWithTag #'part \clOne }  % c435: cue source for Fl 1, Hn 3, Hn 4 at 127-128 (MOLA PDF 5)
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

% c285 (Gould, Behind Bars ch. 1, PDF 36 (a) and (c), PDF 38 "chords"): a beamed group is horizontal when it begins and ends on the same note, or
% when an inner note lies closer to the beam than both outer notes (a concave group). LilyPond flattens a group only when an inner note
% passes the first note in the direction opposite to the beam's slope, and otherwise only damps the slope, so concave groups such as
% Vln I 27.3-4 F5-D5-B4-D5 (stems down) still sloped. For chords the note nearest the beam counts (PDF 38). Only groups of three or more
% notes with all stems in one direction (no kneed or cross-staff beams); manual Beam.positions overrides are unaffected. No sound change.
% c285 also (Gould PDF 35 'notes on ledger lines', PDF 36 'direction of beam angle'): groups wholly above the first ledger line whose beam LilyPond
% laid flat at the middle line get the slope of the outer interval, 1/2 space (1/4 for a second), as Vln I at 199-210 and 247-267 since c105/c195:
% 90 Fl 1 and Vln I, 101 Vln I, 104 Fl 1, 125 Vln I, 206 Vln II, 250 and 253 Fl 1, Vln I, Vln II, 265 and 267 Vln II (\offset on shared staves).
#(define (gould-concave-damping beam)
  (let* ((heads (lambda (s) (let ((h (ly:grob-object s 'note-heads))) (if (ly:grob-array? h) (ly:grob-array->list h) '()))))
         (stems (filter (lambda (s) (pair? (heads s)))
                        (let ((a (ly:grob-object beam 'stems))) (if (ly:grob-array? a) (ly:grob-array->list a) '()))))
         (dir (ly:grob-property beam 'direction 0))
         (close (map (lambda (s) (apply max (map (lambda (h) (* dir (ly:grob-property h 'staff-position 0))) (heads s)))) stems)))
    (if (and (> (length close) 2) (not (= dir 0))
             (every (lambda (s) (= (ly:grob-property s 'direction 0) dir)) stems)
             (or (= (car close) (last close))
                 (let ((lo (max (car close) (last close))))
                   (any (lambda (p) (> p lo)) (cdr (drop-right close 1))))))
        (begin
          (if (ly:get-option 'gould-concave-log)
              (let* ((ev (event-cause (car (heads (car stems))))) (o (and ev (ly:event-property ev 'origin #f))))
                (ly:message "gould-concave ~a ~a" (if o (ly:input-file-line-char-column o) "?") close)))
          100000)
        1)))

% c375 (Gould, Behind Bars ch. 1, PDF 33-34 "Degree of beam angle"): "Beam angles should not deviate far from the horizontal ... Usually, they
% cross no more than one stave-line"; "the beam of shorter groups should not cross more than one stave-space"; "avoid steep angles through
% stave-lines, as these create an uncomfortable visual lattice effect"; "the wider the interval, the more flattened the beam angle becomes".
% LilyPond gave 95 groups of two to four notes a slope of 1.65-2 spaces (harp 67-82, 123-130, 235-242; violins 17, 28, 157, 259-262;
% violas 17, 19, 35, 157; clarinet 257-262; bassoon 35). For a group of at most four notes in one stem direction whose slope exceeds 1.4
% spaces, the end with the shorter stem keeps its place (PDF 35: "the stem that is going to be the shorter determines the starting point of
% the beam") and the other end moves exactly one space from it, so it stays in the same sit/hang/straddle position against the stave-lines
% (PDF 31-32, 34) and only its stem lengthens. Longer groups, kneed, broken and manually positioned beams are unaffected. No sound change.
#(define (gould-max-slope beam)
  (let* ((pos (beam::place-broken-parts-individually beam))
         (orig (ly:grob-original beam))
         (heads (lambda (s) (let ((h (ly:grob-object s 'note-heads))) (if (ly:grob-array? h) (ly:grob-array->list h) '()))))
         (stems (filter (lambda (s) (pair? (heads s)))
                        (let ((a (ly:grob-object beam 'stems))) (if (ly:grob-array? a) (ly:grob-array->list a) '()))))
         (dir (ly:grob-property beam 'direction 0)))
    (if (and (pair? pos) (<= 2 (length stems) 4) (not (= dir 0))
             (or (not (ly:grob? orig)) (null? (ly:spanner-broken-into orig)))
             (every (lambda (s) (= (ly:grob-property s 'direction 0) dir)) stems)
             (> (abs (- (cdr pos) (car pos))) 1.4))
        (let* ((near (lambda (s) (/ (* dir (apply max (map (lambda (h) (* dir (ly:grob-property h 'staff-position 0))) (heads s)))) 2)))
               (ll (* dir (- (car pos) (near (car stems)))))
               (lr (* dir (- (cdr pos) (near (last stems)))))
               (keep-left (<= ll lr))
               (k (if keep-left (car pos) (cdr pos)))
               (o (if keep-left (cdr pos) (car pos)))
               (n (+ k (if (> o k) 1.0 -1.0))))
          (if (> (* dir (- n o)) 0)
              (if keep-left (cons k n) (cons n k))
              pos))
        pos)))

% c465 (Gould, Behind Bars ch. 1, PDF 34 "Degree of beam angle": "Notes spaced very close together horizontally (closer than three spaces) take
% only a slight angle (1/4 or 1/2 space) regardless of the interval"; PDF 31-32, 34: both ends attached to a stave-line). At staff size 14 on A3 the
% score's quavers stand 1.5-2.6 spaces apart (median 2), yet 211 groups of three or four notes kept slopes of 0.82-1.35 spaces after c375's
% one-space limit (violins 28-38, harp 67-82, 123-130, 235-242, development 101-112, coda 257-264). For a group of two to four notes in one stem
% direction whose stems average under 3 spaces apart and whose slope exceeds 0.7, the end with the shorter stem keeps its place (PDF 35) and the
% other end moves to the line-attached position nearest a 1/2-space slope (sit-to-hang 0.65 or 0.35), or 1/4 (0.18) when the outer interval is a
% second; only that end's stem lengthens. Runs after gould-max-slope; manual positions, kneed and broken beams unaffected. No sound change.
% Off (Beam.details.gould-close-off) for the harp LH's up-stem arpeggios at 123-130: their beams lie between the two harp staves and the
% longer stems overfill page 7 (115-143) by 0.1 space; c375's one-space limit still applies there.
#(define (gould-close-slope beam)
  (let* ((pos (gould-max-slope beam))
         (orig (ly:grob-original beam))
         (heads (lambda (s) (let ((h (ly:grob-object s 'note-heads))) (if (ly:grob-array? h) (ly:grob-array->list h) '()))))
         (stems (filter (lambda (s) (pair? (heads s)))
                        (let ((a (ly:grob-object beam 'stems))) (if (ly:grob-array? a) (ly:grob-array->list a) '()))))
         (dir (ly:grob-property beam 'direction 0))
         (sys (ly:grob-system beam)))
    (if (and (pair? pos) (<= 2 (length stems) 4) (not (= dir 0)) (ly:grob? sys)
             (not (assoc-get 'gould-close-off (ly:grob-property beam 'details '()) #f))
             (or (not (ly:grob? orig)) (null? (ly:spanner-broken-into orig)))
             (every (lambda (s) (= (ly:grob-property s 'direction 0) dir)) stems)
             (> (abs (- (cdr pos) (car pos))) 0.7)
             (< (/ (- (ly:grob-relative-coordinate (last stems) sys X) (ly:grob-relative-coordinate (car stems) sys X))
                   (1- (length stems)))
                3.0))
        (let* ((near (lambda (s) (/ (* dir (apply max (map (lambda (h) (* dir (ly:grob-property h 'staff-position 0))) (heads s)))) 2)))
               (ll (* dir (- (car pos) (near (car stems)))))
               (lr (* dir (- (cdr pos) (near (last stems)))))
               (keep-left (<= ll lr))
               (k (if keep-left (car pos) (cdr pos)))
               (o (if keep-left (cdr pos) (car pos)))
               (up (if (> o k) 1.0 -1.0))
               (second (<= (abs (- (near (car stems)) (near (last stems)))) 0.5))
               (q (/ (- (ly:grob-property beam 'beam-thickness 0.48) (ly:staff-symbol-line-thickness beam)) 2))
               ;; line-attached beam centres: n, n+q, n-q
               (cands (filter (lambda (n) (and (> (* up (- n k)) 0.1) (<= (* up (- n k)) (if second 0.36 0.66))))
                              (append-map (lambda (m) (list m (+ m q) (- m q)))
                                          (map (lambda (i) (+ (round k) i)) '(-2.0 -1.0 0.0 1.0 2.0)))))
               (n (if (null? cands) #f
                      (if second (car (sort cands (lambda (a b) (< (abs (- a k)) (abs (- b k))))))
                          (car (sort cands (lambda (a b) (> (abs (- a k)) (abs (- b k))))))))))
          (if (and n (> (* dir (- n o)) 0))
              (if keep-left (cons k n) (cons n k))
              pos))
        pos)))

% c295 (Gould, Behind Bars ch. 1, PDF 49: "From the centre of the stave, rests move an exact number of stave-spaces up or down, so that they
% remain correctly positioned in relation to the stave-lines"; PDF 51: a rest displaced by the other part moves further away). On shared staves
% LilyPond's rest-collision code moves a voiced crotchet or quaver rest by half-spaces, so Bn 1's off-beat rests at 11, 19 and 24 stood 3.5 and
% 4.5 spaces up among neighbours at 2, 3 and 4 (five heights for one pattern), and single rests at 62, 182, 201, 210, 222, 259, 268 and 276 sat
% half a space off the stave-line grid. After the collision is resolved, a crotchet or shorter rest that stands a half-space off the grid moves
% the remaining half-space further from the centre (never towards the other part). Minim and semibreve rests are left alone: LilyPond already
% hangs or sits them on a line or ledger line (PDF 48, 51). Score only in effect (the parts have one voice per stave); no sound change.
#(define (gould-rest-grid grob)
  (if (>= (ly:grob-property grob 'duration-log 2) 2)
      (let* ((par (ly:grob-parent grob Y))
             (y (ly:grob-relative-coordinate grob par Y))
             (ss (ly:grob-object grob 'staff-symbol))
             (y0 (if (ly:grob? ss)
                     (let ((c (ly:grob-common-refpoint grob ss Y)))
                       (- (ly:grob-relative-coordinate grob c Y) (ly:grob-relative-coordinate ss c Y)))
                     y))
             (frac (- (* 2 y0) (round (* 2 y0)))))
        (if (and (< (abs frac) 0.01) (odd? (inexact->exact (round (* 2 y0)))))
            (ly:grob-translate-axis! grob (if (> y0 0) 0.5 -0.5) Y)))))

\layout {
  \context { \Voice \consists #gould-mid-stems }  % c245, see gould-mid-stems
  \context { \Staff \override Rest.after-line-breaking = #gould-rest-grid }  % c295, see gould-rest-grid
  % c475 (Gould PDF 50: on a shared stave the lower part's rests sit below the centre line, the upper part's above it; PDF 51: a rest goes
  % outside the stave only when the other part's note displaces it, and "the space in which a rest centres, or its distance from the stave,
  % should be on the same level as surrounding pitches"). LilyPond hangs a lower part's semibreve rest from the bottom line, outside the stave,
  % and sits its minim rest on the bottom line, even when the other player holds a note at or above the centre line (Ob 2 at 217-218 under
  % Ob 1's D flat 5; Fl 2 at 217-218 under Fl 1's D flat 6). Semibreve and minim rests now start one space nearer the centre (voiced-position 2:
  % semibreve hanging from the second line, minim sitting on it), never across the centre line; rest-collision still pushes them out when a note
  % is in the way. Crotchet and shorter rests keep c295's placement. Score only in effect; no sound change.
  \context { \Staff \override Rest.voiced-position = #(lambda (g) (if (< (ly:grob-property g 'duration-log 2) 2) 2 4)) \override MultiMeasureRest.voiced-position = #2 }  % c475 (whole-bar rests R1 of a part-combined player too)
  \context { \Staff \override Beam.positions = #gould-close-slope }  % c375 gould-max-slope, then c465 gould-close-slope (it calls gould-max-slope first)
  \context { \Staff \override Beam.damping = #gould-concave-damping }  % c285, see gould-concave-damping (Staff level, so the c-cycle \override Staff.Beam.damping = #+inf.0 in pOne and recP still wins there)
  \context { \Staff \RemoveEmptyStaves \consists "Merge_rests_engraver" soloText = "1." soloIIText = "2." }
  \context { \DrumStaff \RemoveEmptyStaves }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver"
 \override Script.Y-offset = #stem-side-y-offset }  % c125, see stem-side-y-offset
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" \override DynamicTextSpanner.before-line-breaking = #c405-broken-cresc }  % c405, see c405-broken-cresc in global.ily
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

% c325 (MIDI focus, shared with the scherzo; symphony/coherence/rolls-midi.ily, copied here as rolls-midi.ily): LilyPond plays a stem-tremolo roll as ONE stroke held for
% the note's length, so every timpani roll in score.midi (5, 147-152, 209-210, 219-223, 231-238, 243-246, 261-263, 273-278) was a single fading stroke. The orchestra is now
% a music function of the timpani music: the printed \score takes the timpani as written, the MIDI-only \score takes them through \rollStrokesByBar, which turns each roll
% into repeated strokes at a rate chosen from its bar's tempo. Only the timpani staff differs between the two scores, so the string tremolo (223 on) still plays as held
% notes, and the printed pages are pixel-identical. arrivalPerc, codaTwoPerc and finalePerc keep their names (render helper).
\include "rolls-midi.ily"
% Stroke value by bar, (first bar . n), n = 16 (semiquavers) or 32 (demisemiquavers); rolls-midi.ily computes stroke lengths correctly only for powers of two.
%   1-210 at 2 = 84-92: semiquavers, 11.2-12.3 strokes a second (demisemiquavers would be 22-25)
%   211-260 at 2 = 72-56 (219-223, 231-234) and 66 (235-238): demisemiquavers, 15-19 a second, rising to 22 in the stringendo of 243-246 (a crescendo roll quickens)
%   261-270 at 2 = 88: semiquavers, 11.7 a second; 271-279 (Largamente 2 = 72 from 273): demisemiquavers, 19.2 a second
rollStrokeTable = #'((1 . 16) (211 . 32) (261 . 16) (271 . 32))
#(define (c325-roll? m)
   (or (and (eq? (ly:music-property m 'name) 'NoteEvent)
            (any (lambda (a) (eq? (ly:music-property a 'name) 'TremoloEvent)) (ly:music-property m 'articulations)))
       (and (eq? (ly:music-property m 'name) 'EventChord)
            (any (lambda (e) (eq? (ly:music-property e 'name) 'TremoloEvent)) (ly:music-property m 'elements)))))
#(define (c325-n-at bar table)
   (let loop ((t table) (n 16)) (if (and (pair? t) (>= bar (caar t))) (loop (cdr t) (cdar t)) n)))
% Walks the music keeping each element's start (2/2 throughout, so bar = whole notes elapsed + 1) and hands each roll to \rollStrokes with that bar's n.
rollStrokesByBar = #(define-music-function (table music) (list? ly:music?)
  (define (walk m t)
    (cond
      ((c325-roll? m) (rollStrokes (c325-n-at (1+ (inexact->exact (floor t))) table) m))
      ((eq? (ly:music-property m 'name) 'SequentialMusic)
       (let loop ((es (ly:music-property m 'elements)) (t t) (acc '()))
         (if (null? es)
             (begin (ly:music-set-property! m 'elements (reverse acc)) m)
             (loop (cdr es) (+ t (ly:moment-main (ly:music-length (car es)))) (cons (walk (car es) t) acc)))))
      ((ly:music? (ly:music-property m 'element))
       (ly:music-set-property! m 'element (walk (ly:music-property m 'element) t)) m)
      ((pair? (ly:music-property m 'elements))
       (ly:music-set-property! m 'elements (map (lambda (e) (walk e t)) (ly:music-property m 'elements))) m)
      (else m)))
  (walk music 0))

familyBracket = \with { systemStartDelimiter = #'SystemStartSquare \override InstrumentName.padding = #1.2
  \override StaffGrouper.staffgroup-staff-spacing = #'((basic-distance . 9) (minimum-distance . 7) (padding . 1) (stretchability . 5)) }
% c325: the whole orchestra, with the timpani music as the argument (see above)
fullScore = #(define-music-function (timpMusic) (ly:music?) #{
  <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl. 1·2" midiInstrument = "flute" }
        << \global \pc \removeWithTag #'part \fluteOne \removeWithTag #'part \fluteTwo >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob. 1·2" midiInstrument = "oboe" }
        << \global \pc \removeWithTag #'part \oboeOne \removeWithTag #'part \oboeTwo >>
      % c135 put Ob 2's line at 159-166 on its own 'Oboe 2' staff; c446 moved that line to the cor anglais (recP.ily), so the extra staff is gone.
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
    % c505 (Adler part 2 PDF 291: "the spacing on the page, indicating the separation of choirs, must be immediately discernable"; PDF 292: "It is
    % imperative to leave space between the choirs ... between the winds and the brass, between the brass and the percussion"): the family
    % sub-brackets were nested StaffGroups whose own StaffGrouper set the plain distance below them, so whenever the lowest live brass staff belonged
    % to a family, the brass-to-percussion or brass-to-harp gap shrank to the gap inside a family (150 dpi, staff space 7.3 px: B.tbn.-Timp. at 37-50
    % 47 px, the same as Fl.-Ob.; Hn. 1-2-Harp at 67-76 66 px and 77-86 71 px; Tpt. 1-2-Timp. at 171-178 41 px, less than Vc.-Cb. below it). The
    % same squares are now drawn by one brass StaffGroup through systemStartDelimiterHierarchy, so one StaffGrouper spaces the brass: plain
    % distance between its staves, the choir distance (minimum 8) below the lowest live one, whichever it is (now 65, 81, 82 and 55 px). Page 7
    % (128-143) stays at its minimum; a minimum of 9 was tested and compresses page 7. Brackets, barlines, names, marks and MIDI unchanged.
    % familyBracket (above) is no longer used.
    \new StaffGroup \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver"
      systemStartDelimiterHierarchy = #'(SystemStartBracket (SystemStartSquare hnA hnB) (SystemStartSquare tpA tpB) (SystemStartSquare tbA tbB) tba)
      \override InstrumentName.padding = #1.2 } <<
      % c325 (Adler part 2 PDF 294: "heavy brackets set off the choirs; and an additional brace clarifies instruments of a family"; Ex. XVIII-1, PDF 293:
      % 4 Horns, 3 Trumpets and 3 Trombones each joined inside the brass bracket): horns 1-4, trumpets 1-3 and the three trombones each get a
      % sub-bracket, as the scherzo has had since its c145 (SystemStartSquare, same padding). Tuba alone. No sound change.
      % The sub-group keeps the plain staff-to-staff distance below it (staffgroup-staff-spacing = the StaffGrouper's staff-staff-spacing default),
      % so only the brass/percussion and other choir gaps stay wider; without it each family got a choir-sized gap and every system grew taller.
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
      << \clef bass \global #timpMusic >>
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
#})

\score { \fullScore \removeWithTag #'part \timp
  \layout { }
}

% c325: MIDI only (see fullScore): the same orchestra, the timpani rolls as repeated strokes
\score { \fullScore \rollStrokesByBar #rollStrokeTable \removeWithTag #'part \timp
  \midi { \context { \Score midiChannelMapping = #'instrument
    % \subP is a markup dynamic ("sub. p"): give it the p volume. sf/fp were unmapped and fell back to the default (0.71, louder than ff).
    dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42)) #f)
      0.42)) }
    % Harp: one set of dynamics for both hands (printed under the LH); the RH staff has none, so its notes played at the default volume.
    \context { \PianoStaff \consists "Dynamic_performer" } }
}

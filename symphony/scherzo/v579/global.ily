\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./accel./fermatas in score.midi; prints nothing. Its unit is the quarter note (2. = 88 is \mt 264).
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
% c018: down-bow sign for accented strokes (Adler PDF 38: mark the bow only to counteract the players' habit). avoid-slur ignore:
% with the default, the stem-side Y-offset callback (score.ly, c125) failed on the high C under a short slur ("Nothing to minimise"), and 'inside made a cyclic slur dependency.
dnb = -\tweak avoid-slur #'ignore \downbow
% c445: the same for the up-bow. With the default avoid-slur, an up-bow on the first note of a slur that also starts a tie (45 Vln I, Vln II, Vla;
%   121 Vln I) collapsed the slur and the tie to a zero-width stencil (0.1-0.2 staff space): the score showed 45-46 and 121-122 as separate bows with
%   the tied B5/G5 restruck, while the parts (no stem-side callback) were right. Adler I PDF 37: a slur is one bow, no slur means a change of bow;
%   PDF 54: playing instructions must appear in both score and parts, and the two must agree. Found by logging every Slur/Tie stencil's X-extent in a test build (only these 4+4).
upb = -\tweak avoid-slur #'ignore \upbow
% c235: player label restated at the start of a system on a shared staff (Adler II PDF 295: "all the instruments must be clearly marked
% in all systems"). The part combiner prints "1.", "2." or "a2" only where the state changes, so a solo or a2 carried over a system break
% reached the new system unlabelled (Ob 1·2 at 93: one line, solo or a2?). The label prints only if its note is the first of its system;
% anywhere else (after a layout change) it is dropped. Score only: the tag keeps it out of the parts.
#(define (c235-first-in-system grob)
  (let* ((col (ly:item-get-column grob))
         (sys (ly:grob-system grob))
         (left (and (ly:grob? sys) (ly:spanner-bound sys LEFT))))
    ;; c335: test by musical moment. The old test read 'rank, which is not a grob property (always 0), so every label printed wherever
    ;; it stood; after the c334 breaks moved 214->213 and 234->233, three labels printed in a system's second bar (Gould PDF 13, 55).
    ;; A label prints only if its note falls in the first bar of its system.
    (if (not (and (ly:grob? col) (ly:grob? left)
                  (let ((wc (ly:grob-property col 'when #f)) (wl (ly:grob-property left 'when #f)))
                    (and (ly:moment? wc) (ly:moment? wl) (not (ly:moment<? wc wl))
                         (ly:moment<? (ly:moment-sub wc wl) (ly:make-moment 3/4))))))
        (ly:grob-set-property! grob 'stencil #f))))
% Its height counts for the final spacing (slurs and scripts are avoided) but not in the page-breaking estimate, so the line and page
% breaks stay as they were (with the full estimate the score grew to 15 pages).
#(define c235-label-extent (ly:make-unpure-pure-container ly:grob::stencil-height (lambda (grob start end) '(0 . 0))))
sysLabel = #(define-event-function (txt) (markup?)
  #{ -\tag #'score -\tweak Y-extent #c235-label-extent -\tweak after-line-breaking #c235-first-in-system ^\markup \bold #txt #})
% c575 (Gould PDF 54: notes of equal duration take equal space across the system): \beatq #w note widens the space before an off-beat quaver
%   that follows a dotted crotchet, so it does not crowd the beat-2 chord in another staff. The full-height extent lets the note reach the
%   dotted note's dot even after a leap (a finite height had no effect in the score); w is the left-edge change in staff spaces. Print only.
beatq = #(define-music-function (w m) (number? ly:music?) #{ \tweak extra-spacing-height #'(-inf.0 . +inf.0) \tweak extra-spacing-width #(cons w 0) #m #})
global = {
  \accidentalStyle Score.modern
  \key e \minor \time 3/4
  \tempo "Allegro vivace" 2. = 88
  % 1-12: introduction. Hn 1 G sharp (movement II's A flat) -> horn call in E major -> E minor; timpani motive x
  % c020: fermata on bar 2: the pivot G sharp 4 (movement II's last A flat 4) is held before the tempo starts at 3 (was 1.4 s, now about 2.7 s in the MIDI)
  s2. \mt 88 s2.\fermata \mt 264
  s2.*10
  \mark \default % A 13: theme A, strings
  s2.*6 \tag #'score \pageBreak s2.*10  % c415: page and system starts pinned at v415's (19, 38, 58, 93, 111, 131, 173, 190, 211, 232, 253, 289, 305, 321, 341)
  \mark \default % B 29: counterstatement, winds and strings in call and response
  s2.*9 \break s2.*7
  \mark \default % C 45: second idea, G major, hemiola
  s2.*12
  \bar "||" \mark \default % D 57: development, fugato on the theme head
  % c411: system break before 58 keeps v411's systems (19-36, 37-57 | 58-74, 75-92) after the second idea's new quavers at 45/49 widened 37-57; without it 58 joined page 2 and page 3 was over-full.
  s2. \tag #'score \pageBreak s2.*15
  \bar "||" \key f \major \mark \default % E 73: F major (the Neapolitan of E), winds and harp without strings
  % c412: breaks before 75, 93 and 111 keep v412's systems (58-74, 75-92, 93-110, 111-130); the applied A sharp dim7 at 128 widened that system and the automatic breaks moved by one bar, over-filling page 3.
  % c533 (A&S Unit 15, PDF 234-235, Ex. 15-5 and 15-6): no poco rit. at 87-88. V arrives at 89 in tempo, under the clarinet's E4 handed to the violas' E4
  %   and the bass clarinet's A-A sharp-B; the dominant needs no emphasis by duration (PDF 234), and the f hemiola at 101 is where it is brought to attention (Brahms Op. 119/3).
  s2.*2 \break s2.*14
  \bar "||" \key e \minor \mark \default % F 89: retransition over the B pedal
  \tempo \markup \medium \italic "ritmo di tre battute" \mt 264
  % c019: 89-100 in three-bar groups (head entries at 89, 92, 95; timpani at 89, 92, 95, 98-100; c327: timpani at 91, 94, 97-100, answering each head), as Beethoven 9/ii bars 177-233 "Ritmo di tre battute"
  s2.*4 \tag #'score \pageBreak s2.*8 \tempo \markup \medium \italic "ritmo di quattro battute" \mt 264 s2.*4
  \mark \default % G 105: theme A, tutti
  s2.*6 \tag #'score \pageBreak s2.*10
  \mark \default % H 121: second idea in E minor
  s2.*10 \tag #'score \pageBreak s2.*2
  s2.*8
  \bar "||" \mark \default % J 141: link to the trio, E minor -> E major
  s2.*8 \tempo \markup \medium \italic "poco rit." \mt 252 s2. \mt 240 s2. \mt 232 s2. \mt 228 s2.
  \bar "||" \break \key e \major \mark \default % K 153: Trio (c005: the trio starts a system, not the last bar of one)
  \tempo \markup { "Trio" \medium \italic "Un poco meno mosso" } 2. = 76
  s2.*16
  \mark \default % L 169 (c045): the trio tune in the cellos (c344; MOLA PDF 4: rehearsal letters at landmarks; letters from here on are one to four later than before c045)
  s2.*4 \tag #'score \pageBreak s2.*12
  \mark \default % M 185: trio, middle part (c003: 24 bars)
  s2.*5 \break s2.*19
  \mark \default % N 209: trio tune returns
  s2.*2 \tag #'score \pageBreak s2.*14
  \mark \default % O 225 (c045): trio codetta over the E pedal
  s2.*7 \break s2.*5 \tempo \markup \medium \italic "poco rit." \mt 222 s2. \mt 214 s2. \mt 206 s2. \mt 198 s2.  % c028: 240 the slowest bar of the printed poco rit. (was \mt 228, a MIDI-only a tempo that the score does not print)
  % c023: retransition 12 bars (was 16); the E-minor key signature now falls on 241, where Hn 1's G sharp turns to G natural
  \bar "||" \key e \minor \mark \default % P 241: retransition
  \tempo \markup \medium \italic "poco a poco accelerando" \mt 198  % c028: the accelerando starts from the rit.'s tempo
  % c113: one tempo curve through 237-253: the rit. ends at 198 (2. = 66, 13 per cent under the trio tempo, the same depth as the link's rit. at 149-152) and the accelerando starts there
  %   (it jumped from 188 at 240 to 204 at 241, a lurch on the falling inflection G sharp -> G that the print marks "poco a poco"; A-S PDF 585), then rises every two bars to Tempo I.
  s2.*2 \mt 208 s2.*2 \mt 220 s2.*2 \mt 232 s2.*2 \mt 244 s2.*2 \mt 254 s2.*2
  \bar "||" \tag #'score \pageBreak \mark \default % Q 253: scherzo returns (c025: the reprise starts a system, as the Trio does since c005)
  \tempo "Tempo I" 2. = 88
  % s395 (cycle 395): system breaks at 269, 289, 305, 321, 341 and 359 (was automatic: 253-270, 271-292, 293-311, 312-331, 332-353, 354-376).
  %   Gould PDF 53-54: durations spaced in relative proportion, each longer value with more space than its shorter neighbour, and on a denser
  %   system fewer bars. The automatic breaks crowded 253-353 (heterophony quavers, tutti): a mid-bar crotchet had only 1.15-1.28 times a
  %   quaver's space (1.5 elsewhere in the score), and Fl 1's crotchet at 254, 258, 306, 310, 318 had less space than the quaver after it.
  %   Seven systems instead of six (the last page now holds two), still 13 pages; every system now 1.35-1.9. Score only (the parts drop \break).
  s2.*16 \break
  s2.*8
  \mark \default % R 277 (c045): second idea in E minor (as C 45 and H 121)
  s2.*12
  \bar "||" \tag #'score \pageBreak \mark \default % S 289 (c035: double bar as at D 57, the same juncture; Gould PDF 53): development, shortened
  s2.*16
  \tag #'score \pageBreak \mark \default % T 305: theme A, tutti (c023: 20 bars, the close cut to 4)
  % c575 (Gould PDF 53-54, 55): the page starts at U 325 instead of 321, and 305-324 is two systems of ten bars (305, 315). With 321-340 on one system the coda's
  %   build and fff summit had a crotchet only 1.13 times a quaver (2.13 against 1.88 spaces; c395 set 1.35 as the floor and measured 1.35 here in v395).
  %   Now 325-339 has 3.38 against 2.12 (1.59); 305-314 and 315-324 have 3.0-3.2 spaces a quaver. One system for 305-324 was tested: crotchet = quaver (1.95), rejected.
  s2.*10 \tag #'score \break s2.*10
  \bar "||" \tag #'score \pageBreak \mark \default % U 325: coda (c030: bar numbers in these comments are v24-v30 numbers)
  \tempo "Più mosso" 2. = 96
  s2.*15 \mt 96 \tempo \markup "G.P." s2.\fermata  % c045: "G.P." printed above the top staff and the strings, where the tempo marks go (MOLA PDF 4)
   % c043: the G.P. with fermata lasts about two bars in the MIDI (it played as one plain bar, 0.6 s)
  \bar "||" \tag #'score \pageBreak \key e \major \mark \default % V 341: the trio tune recalled; G.P. at 340, rit. 370-376
  \tempo \markup { "Meno mosso" \medium \italic "(tempo del Trio)" } 2. = 76
  s2.*16
  \mark \default % W 357 (c045): the motto's chromatic tail and the close
  s2.*2 \break s2.*11 \once \override Score.MetronomeMark.outside-staff-padding = #1.2  % c035: the rit. touched "change bow freely" (Vln I, 369); Gould PDF 55: no characters collide
  \tempo \markup \medium \italic "rit." \mt 210 s2. \mt 196 s2. \mt 180 s2. \mt 160 s2. \mt 140 s2.*2 \mt 50 s2.-\tweak staff-padding #2 \fermata  % c035: the last fermata cleared the incoming ties of Vln I and Hn 1 (it touched them; Gould PDF 55)
  % c230: MIDI only: the final fermata bar at \mt 50 (3.6 s; was \mt 100, 1.8 s, shorter than a bar of the rit. it ends). The last G sharp, the pivot the finale
  %   takes as A flat, is held under the fermata after the 375 chord has died away (Casanelles PDF 210-212: the mockup is how the score is heard and judged;
  %   movement II's final fermata bar lasts 6.3 s in its MIDI). Print unchanged.
  \bar "|."
}

\version "2.24.0"
% c075 (MOLA PDF 5, 7, 8): one A4 part per player, staff 21 pt (7.4 mm), transposed parts (horns, trumpets and timpani without key signature; trumpets since c226, Adler adler1 PDF 297-298), multi-measure rests,
% page turns only in rests of 2+ bars (strings use the normal breaker: the inside player turns; parts that cannot turn early start on page 2, MOLA PDF 6), part-only cues kept, score-only marks removed.
% Build from this directory: lilypond -o parts/ parts-book.ly
\include "parts-head.ily"
stripBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
% c345 (MOLA PDF 8: parts no smaller than A4, larger preferred, JIS B4 "the most common size"; PDF 7: 7.5 mm "the most readable staff size for all instruments",
% at most 8-10 staves a page for flute, violin and tuba, up to twelve for the others): JIS B4 257 x 364 mm, as the parts of movements I, II and III; staff 21.26 pt = 7.5 mm.
\paper { page-breaking = #ly:page-turn-breaking paper-width = 257\mm paper-height = 364\mm max-systems-per-page = 12 top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm indent = 8\mm
  % c525 (MOLA PDF 7: the instrument name is a header on each subsequent page; page 1 already names it under the title): no running header name on a part's first page.
  oddHeaderMarkup = \markup \fill-line { "" \unless \on-first-page \fromproperty #'header:instrument \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \fromproperty #'page:page-number-string \unless \on-first-page \fromproperty #'header:instrument "" } }
% c135 (MOLA PDF 5: in parts, multi-measure rests carry bar-number ranges, e.g. "27-117"; Example 3, PDF 10: "9 - 11" under the numbered rest): every rest of two or more bars prints its first and last bar below the staff.
#(define (mmr-with-range grob)
  (let* ((st (ly:multi-measure-rest::print grob))
         (n (ly:grob-property grob 'measure-count 1))
         (col (ly:spanner-bound grob LEFT))
         (loc (and (ly:grob? col) (ly:grob-property col 'rhythmic-location #f))))
    (if (and (ly:stencil? st) (> n 1) (pair? loc))
        (let* ((first (car loc))
               (txt (grob-interpret-markup grob (markup #:fontsize -2 (format #f "~a–~a" first (+ first n -1)))))
               (xc (interval-center (ly:stencil-extent st X)))
               (txt (ly:stencil-translate-axis txt (- xc (interval-center (ly:stencil-extent txt X))) X))
               (txt (ly:stencil-translate-axis txt (- -3.6 (cdr (ly:stencil-extent txt Y))) Y)))
          (ly:stencil-add st txt))
        st)))
% c165 (MOLA PDF 8 and Example 7, PDF 12: extracted parts must be proofread for colliding marks): the range under a numbered rest was drawn outside the rest's
% height, so the vertical spacing did not see it and the next system's rehearsal letters and tempo marks were set on top of it (Cor anglais 7-10 under E, 43-48 under G,
% 115-122 under Tempo I; Flute 1 135-142 under K). The rest's height now includes the range, so systems are spaced to clear it.
#(define (mmr-height-with-range grob)
  (let ((e (ly:multi-measure-rest::height grob)))
    (if (> (ly:grob-property grob 'measure-count 1) 1) (cons (min (car e) -5.0) (cdr e)) e)))
% c315 (MOLA PDF 5, Example 4 PDF 10: letter and tempo word on one line, see global.ily): layout follow-ups, parts only. The percussion part's combined letter + tempo marks take
% horizontal space like its tempo marks (c195), with two spaces after them, so "R Più allegro" stays inside the margin and "P Maestoso" clears the cymbals' fff at 223; its system padding is 0.5 (ten systems on its one page). Timpani padding 0.5 and cor anglais 0.2
% keep their page counts (2 and 1) without compression; Flute 2 keeps its two pages with a fixed turn in the rest 187-198, as in v315.
\layout { #(layout-set-staff-size 21.26) \context { \Staff \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Staff \consists "Page_turn_engraver" \override DynamicTextSpanner.before-line-breaking = #c405-broken-cresc } \context { \DrumStaff \consists "Page_turn_engraver" \override MultiMeasureRest.stencil = #mmr-with-range \override MultiMeasureRest.Y-extent = #(ly:make-unpure-pure-container mmr-height-with-range) } \context { \Score skipBars = ##t minimumPageTurnLength = #(ly:make-moment 2/1) \override MultiMeasureRest.expand-limit = #1 rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.font-size = #2 } }
% c315 (MOLA PDF 6: the front of each part carries the full title as printed in a concert programme): the parts' title gains "in C minor", as on the score.
\book { \bookOutputName "part-fluteOne"   \paper { max-systems-per-page = 10 }\header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Flute 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \fluteOne } >> \layout { } } }
\book { \bookOutputName "part-fluteTwo" \paper { max-systems-per-page = 10 system-system-spacing.padding = #0.5 page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Flute 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \fluteTwo } { s1*198 \pageBreak } >> \layout { } } }
\book { \bookOutputName "part-oboeOne"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Oboe 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \oboeOne } >> \layout { } } }
\book { \bookOutputName "part-oboeTwo"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Oboe 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \oboeTwo } >> \layout { } } }
% c195 (MOLA PDF 8: marks must not be set over one another or read as belonging to another bar): the cor anglais' single page was compressed by 10 staff-spaces (fixed by the joined rests 128-142 in global.ily);
% its 205 "poco a poco più animato" stood above "Tempo I" of 199 and hung under its solo at 183-184. A line break before 205 puts it over its own rest; still one page.
% c435 (MOLA PDF 8 and Example 7, PDF 12: no colliding or floating marks; Example 4, PDF 10: each letter and tempo word over its own rest): in the cor anglais and bass clarinet parts the rest after P
% (223-234, 224-234) was narrower than "P Maestoso (half = 56)", so Q's tempo was stacked above it and Q's second line "molto cantabile" stood next to P's "= 56)", reading as part of Maestoso.
% A line break before Q (235) in these two parts (and before S, 255, in the cor anglais, so Q-R and S-T each have a line), as c195 did before 205 in the cor anglais. Tested and declined: marks taking horizontal space as in the percussion part (pushed the notes of 1, 223 and 273
% away from their barlines) and a wider rest at 223 (MultiMeasureRest.minimum-length was not honoured there).
\book { \bookOutputName "part-corAnglais" \paper { system-system-spacing.padding = #0.2 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Cor anglais in F" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \corAnglais } } { s1*204 \break s1*30 \break s1*20 \break } >> \layout { } } }
\book { \bookOutputName "part-clOne"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Clarinet 1 in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes \transpose bes c' { \mergeRests \removeWithTag #'score \clOne } } >> \layout { } } }
\book { \bookOutputName "part-clTwo" \paper { max-systems-per-page = 10 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Clarinet 2 in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes \transpose bes c' { \mergeRests \removeWithTag #'score \clTwo } } >> \layout { } } }
% c195 (MOLA PDF 6: a part that cannot be read from one page starts on page 2, so its two pages face each other and need no turn; Gould PDF 31-41 and MOLA PDF 8: no marks set over notes or other marks): since c187's doubling at 27-34 the
% bass clarinet's single page was over-full by 20.5 staff-spaces and LilyPond compressed it (letters D, E, J and N on the notes, tempo texts under the wrong system). Now two facing pages (2-3), break before K (151).
% c345: on B4 the whole part fits on one page, so the forced break before K (151) and the start on page 2 are no longer needed (MOLA PDF 6-7).
\book { \bookOutputName "part-bassCl" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Bass clarinet in B♭" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \transpose bes c'' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition bes, \transpose bes c'' { \mergeRests \removeWithTag #'score \bassCl } } { s1*234 \break } >> \layout { } } }
\book { \bookOutputName "part-bsnOne" \paper { first-page-number = 2 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Bassoon 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bsnOne } >> \layout { } } }
\book { \bookOutputName "part-bsnTwo"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Bassoon 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bsnTwo } >> \layout { } } }
\book { \bookOutputName "part-cbsn"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Contrabassoon" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \transpose c c' { \mergeRests \removeWithTag #'score \global } } { \clef bass \transposition c \transpose c c' { \mergeRests \removeWithTag #'score \cbsn } } >> \layout { } } }
\book { \bookOutputName "part-hnOne"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Horn 1 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnOne } } >> \layout { } } }
\book { \bookOutputName "part-hnTwo"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Horn 2 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnTwo } } >> \layout { } } }
\book { \bookOutputName "part-hnThree"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Horn 3 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnThree } } >> \layout { } } }
\book { \bookOutputName "part-hnFour"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Horn 4 in F" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \transpose f c' { \mergeRests \removeWithTag #'score \global } } { \clef treble \transposition f \transpose f c' { \mergeRests \removeWithTag #'score \hnFour } } >> \layout { } } }
% c195: Tpt 1 and Tpt 3 system padding 0.5 (as Flute 2 and cor anglais): the joined rests 128-134 and 135-142 (global.ily) changed their page breaks and left page 1 over-full by 0.0-0.2 staff-spaces.
\book { \bookOutputName "part-tptOne" \paper { system-system-spacing.padding = #0.5 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Trumpet 1 in C" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptOne } >> \layout { } } }
\book { \bookOutputName "part-tptTwo"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Trumpet 2 in C" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptTwo } >> \layout { } } }
\book { \bookOutputName "part-tptThree" \paper { system-system-spacing.padding = #0.5 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Trumpet 3 in C" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \tptThree } >> \layout { } } }
\book { \bookOutputName "part-tbnOne"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Trombone 1" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tbnOne } >> \layout { } } }
\book { \bookOutputName "part-tbnTwo"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Trombone 2" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tbnTwo } >> \layout { } } }
\book { \bookOutputName "part-bassTbn"  \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Bass trombone" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \bassTbn } >> \layout { } } }
\book { \bookOutputName "part-tuba"   \paper { max-systems-per-page = 10 }\header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Tuba" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \tuba } >> \layout { } } }
\book { \bookOutputName "part-timp" \paper { system-system-spacing.padding = #0.5 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Timpani" tagline = ##f }
  \score { \new Staff \with { \remove "Key_engraver" } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \timp } >> \layout { } } }
% c165 (MOLA PDF 7: a page turn is best at the end of a multi-measure rest, otherwise in rest or an unexposed passage): the free breaker turned Violin I's page at 78|79,
% inside F2's first violin statement (the dotted peak at 78-79), and at 213|214 inside theme B's recall. Pages 1 and 3 now end with the 16-bar rests 51-66 and
% 171-186 (pages 2-3 and 4-5 face each other, MOLA PDF 7: odd pages on the right), so neither turn costs a note. Five pages instead of four;
% page 4 ends at 234 (not a turn) so it is not over-full.
% c345: on B4, 67-186 fits one page, which put the turn at 234|235 inside the music; the break moves from 234 to 126 (between facing pages 2 and 3), so the turns stay at 66 and 186.
\book { \bookOutputName "part-vlnOne" \paper { max-systems-per-page = 10 page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Violin I" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \vlnOne } { s1*66 \pageBreak s1*60 \pageBreak s1*60 \pageBreak } >> \layout { } } }
\book { \bookOutputName "part-vlnTwo" \paper { max-systems-per-page = 10 page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Violin II" tagline = ##f }
  \score { \new Staff \with {  } << { \clef treble \mergeRests \removeWithTag #'score \global } { \clef treble \mergeRests \removeWithTag #'score \vlnTwo } { s1*66 \pageBreak s1*120 \pageBreak } >> \layout { } } }
\book { \bookOutputName "part-vla" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Viola" tagline = ##f }
  \score { \new Staff \with {  } << { \clef alto \mergeRests \removeWithTag #'score \global } { \clef alto \mergeRests \removeWithTag #'score \vla } { s1*66 \pageBreak s1*120 \pageBreak } >> \layout { } } }
% c165 (MOLA PDF 7): the cellos' first turn fell at 72|73, inside their F2 counter-melody (67-82); it now falls after the pizzicato bar 66 (three beats of rest).
\book { \bookOutputName "part-vc" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Violoncello" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \vc } { s1*66 \pageBreak s1*120 \pageBreak } >> \layout { } } }
\book { \bookOutputName "part-cb" \paper { page-breaking = #ly:optimal-breaking } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Double bass" tagline = ##f }
  \score { \new Staff \with {  } << { \clef bass \transpose c c' { \mergeRests \removeWithTag #'score \global } } { \clef bass \transposition c \transpose c c' { \mergeRests \removeWithTag #'score \cb } } { s1*66 \pageBreak s1*120 \pageBreak } >> \layout { } } }
% c255 (MOLA PDF 7: a page turn falls in a rest or an unexposed passage, considering the playing technique; PDF 5: odd pages on the right): Violin II, viola, cello and double bass now turn
% where Violin I turns, in the rests at 66 (pizz. -> arco at 67) and after 186 (before M), instead of inside music: viola 191|192 (F2 tune, A flat), Violin II 213|214 (theme B episode, f),
% cello 227|228 (chorale bass), double bass 86|87 (closing group, f) and 249|250 (hammered eighths, ff). Violin II keeps its first turn at 61|62 (pizz. pp; 1-66 does not fit one page).
% c105: the percussion part takes the score's drum-staff settings (stems and ties up from the single line, score.ly), so the 279 cymbal quarter no longer hangs below the line
% c195 (MOLA PDF 8: marks must not be set over one another or read as belonging to another bar): in the percussion part the rests are short, so the tempo texts at 205 (poco a poco più animato) and 243/247 were stacked above
% the earlier tempo marks and hung under the previous system. Tempo marks now take horizontal space (as \markLengthOn), so each stands over its own bar; still one page.
% c255 (MOLA PDF 5: a notation key at the head of the percussion part; PDF 6: name the instruments and the number of players): the one-line stave carries two players,
% so the part says which mark is which and that the written length is the length of the sound (223 let ring a bar, 278 tied into 279 and damped on beat 2), as the score's staff name already says "(2 players)".
\book { \bookOutputName "part-perc" \paper { system-system-spacing.padding = #0.5 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Cymbals, Bass drum (2 players)" tagline = ##f
    piece = \markup \normal-text \small \column { \line { "Notation key:" \musicglyph "noteheads.s2xcircle" "above the line = crash cymbals (pair);" \musicglyph "noteheads.s2" "below the line = bass drum." }
      \line { "Each stroke rings for its written length and is damped at its end." } } }
  \score { \new DrumStaff \with { \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override Tie.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 1) (bassdrum default #f -1))) } << \mergeRests \removeWithTag #'score \global { \mergeRests \removeWithTag #'score \perc } >> \layout { \context { \Score \override MetronomeMark.extra-spacing-width = #'(0 . 1.0) \override MetronomeMark.extra-spacing-height = #'(-inf.0 . +inf.0) \override RehearsalMark.extra-spacing-width = #'(0 . 2.0) \override RehearsalMark.extra-spacing-height = #'(-inf.0 . +inf.0) } } } }
% c525: system padding 0.5 (as Flute 2, Tpt 1, Tpt 3, timpani) keeps the harp on two pages, turn after 122, now that rests at lettered tempo changes are wider (global.ily, \lt).
\book { \bookOutputName "part-harp" \paper { system-system-spacing.padding = #0.5 } \header { title = "Symphony No. 1 in C minor — IV. Finale" instrument = "Harp" tagline = ##f }
  \score { \new PianoStaff << \new Staff << \mergeRests \removeWithTag #'score \global { \mergeRests \removeWithTag #'score \harpR } >> \new Staff << { \clef bass \mergeRests \removeWithTag #'score \global } { \clef bass \mergeRests \removeWithTag #'score \harpL } >> >> \layout { } } }

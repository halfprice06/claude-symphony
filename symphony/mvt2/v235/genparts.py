import sys
out = sys.argv[1]
# (var, title, clef, transpose-from (concert pitch that is written as c'), keyless)
P = [
 ("fluteOne","Flute 1","treble",None,False),("fluteTwo","Flute 2","treble",None,False),
 ("oboeOne","Oboe 1","treble",None,False),("oboeTwo","Oboe 2","treble",None,False),
 ("corAnglais","Cor anglais in F","treble","f",False),
 ("clOne","Clarinet 1 in B♭","treble","bes",False),("clTwo","Clarinet 2 in B♭","treble","bes",False),
 ("bassCl","Bass clarinet in B♭ (low C)","treble","bes,",False),
 ("bsnOne","Bassoon 1","bass",None,False),("bsnTwo","Bassoon 2","bass",None,False),
 ("cbsn","Contrabassoon","bass","c",False),
 ("hnOne","Horn 1 in F","treble","f",True),("hnTwo","Horn 2 in F","treble","f",True),
 ("hnThree","Horn 3 in F","treble","f",True),("hnFour","Horn 4 in F","treble","f",True),
 ("tbnOne","Trombone 1","bass",None,False),("tbnTwo","Trombone 2","bass",None,False),
 ("bassTbn","Bass trombone","bass",None,False),("tuba","Tuba","bass",None,False),
 ("timp","Timpani","bass",None,True),
 ("vlnOne","Violin I","treble",None,False),("vlnTwo","Violin II","treble",None,False),
 ("vla","Viola","alto",None,False),("vc","Violoncello","bass",None,False),("cb","Double bass","bass","c",False),
]
h = r'''\version "2.24.0"
\language "nederlands"
#(set-global-staff-size 21)
\paper { #(set-paper-size "b4") top-margin = 20\mm bottom-margin = 20\mm left-margin = 20\mm right-margin = 20\mm
  print-first-page-number = ##t bookpart-level-page-numbering = ##t
  % c165: letters and tempo words stacked over a system (e.g. G over Largamente, J over Tempo I, poco sostenuto over poco rit.) sat nearer
  % the system above than their own (B.cl. "poco sostenuto" of 48 under the solo at 32-33, Hn 1 under 13-14): MOLA PDF 8, Ex. 7 (PDF 12),
  % floating markings in extracted parts. The parts pages are half empty, so the systems get more room between them.
  system-system-spacing = #'((basic-distance . 12) (minimum-distance . 8) (padding . 4) (stretchability . 60)) oddHeaderMarkup = \markup \fill-line { "" \unless \on-first-page-of-part \fromproperty #'header:instrument \if \should-print-page-number \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \if \should-print-page-number \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
\include "score-defs.ily"
noBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
% c165: MOLA PDF 5, Ex. 3-4 (PDF 10): a run of rests is one multi-bar rest, split only where the player must see something (letter,
% tempo word, key or metre). LilyPond starts a new multi-bar rest at every skip or rest boundary, so the MIDI-only \mt steps, the
% score's line-break skips and the section joins split rests for no visible reason (Fl 1 53-56 "2 2", 71-76 "4 2", 89-92 "1 1 1 1").
% partMerge drops the MIDI tempo steps and bar checks (the score build checks the bars) and joins adjacent plain skips and plain whole-bar rests; anything printed still splits them.
% The c035 spacing section at 59-60 is kept (the viola part needs it to stay on one page), so rests still break at 59.
#(define (mt-step? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e) (eq? (ly:music-property e 'name) 'PropertySet)
               (eq? (ly:music-property e 'symbol) 'tempoWholesPerMinute)))))
% c225: the part-combiner switches (\partCombineSoloII etc.) mean nothing in a single part, but they split rests too (Cl 1 71-76 printed "4 2")
#(define (pc-switch? m)
   (and (eq? (ly:music-property m 'name) 'ContextSpeccedMusic)
        (let ((e (ly:music-property m 'element)))
          (and (ly:music? e) (eq? (ly:music-property e 'name) 'PropertySet)
               (eq? (ly:music-property e 'symbol) 'partCombineForced)))))
% c225: MOLA Ex. 4 (PDF 10): the letter at the barline with the tempo word beside it, not stacked over it. A tempo word that follows a
% letter with no music between them is moved right, past the boxed letter, so both sit on one line (MOLA Ex. 7, PDF 12: floating markings).
#(define (beside-letter lst)
   (let loop ((l lst) (after-mark #f) (acc '()))
     (if (null? l) (reverse acc)
         (let* ((m (car l)) (n (ly:music-property m 'name)))
           (cond ((eq? n 'RehearsalMarkEvent) (loop (cdr l) #t (cons m acc)))
                 ((and after-mark (eq? n 'TempoChangeEvent))
                  (loop (cdr l) #f (cons m (cons #{ \once \override Score.MetronomeMark.X-offset = #3.6 \once \override Score.MetronomeMark.outside-staff-horizontal-padding = #0.2 #} acc))))
                 ((memq n '(SkipEvent MultiMeasureRestMusic NoteEvent EventChord RestEvent)) (loop (cdr l) #f (cons m acc)))
                 (else (loop (cdr l) after-mark (cons m acc))))))))
#(define (flat-seq lst)
   (append-map (lambda (m)
                 (cond ((or (mt-step? m) (pc-switch? m) (eq? (ly:music-property m 'name) 'BarCheck)) '())
                       ((eq? (ly:music-property m 'name) 'SequentialMusic)
                        (flat-seq (ly:music-property m 'elements)))
                       (else (list m))))
               lst))
#(define (plain? m kind)
   (and (eq? (ly:music-property m 'name) kind) (null? (ly:music-property m 'articulations))))
#(define (join a b)
   (let* ((len (ly:moment-main (ly:moment-add (ly:music-length a) (ly:music-length b))))
          (c (ly:music-deep-copy a)))
     (ly:music-set-property! c 'duration (ly:make-duration 0 0 (numerator len) (denominator len)))
     c))
#(define (merge-run lst)
   (if (null? lst) '()
       (let loop ((acc (list (car lst))) (rest (cdr lst)))
         (if (null? rest) (reverse acc)
             (let ((a (car acc)) (b (car rest)))
               (if (or (and (memq (ly:music-property a 'name) '(MultiMeasureRestMusic)) (plain? b 'MultiMeasureRestMusic))
                       (and (eq? (ly:music-property a 'name) 'SkipEvent) (plain? b 'SkipEvent)))
                   (loop (cons (join a b) (cdr acc)) (cdr rest))
                   (loop (cons b acc) (cdr rest))))))))
partMerge = #(define-music-function (m) (ly:music?)
  (if (eq? (ly:music-property m 'name) 'SequentialMusic)
      (make-sequential-music (beside-letter (merge-run (flat-seq (ly:music-property m 'elements)))))
      m))
partGlobalPlain = \partMerge \noBreaks \global
partGlobal = << \partGlobalPlain { <>_\markup \small \italic "attacca from movement I" } >>
\addQuote "bassTbnQ" { \removeWithTag #'part \bassTbn }  % c145: without the tag filter the quote held both the score rests and the part-only Vc cue at 58-59 (c135), so it ran two bars late and trombone 1's cue at 61-62 showed B.tbn's A flat2 of 60 (Adler part 2 PDF 299 item 6)
\addQuote "corAnglaisQ" { \corAnglais }
\addQuote "bassClQ" { \bassCl }
% c165: the instrument name was printed three times on each first page (running header, title block, piece label); it now appears once
% in the title block and as the running header from page 2 on (MOLA PDF 6: name on the front; PDF 7: name as a header on each subsequent page)
% c135: bookpart-level-page-numbering: every part starts at page 1 on a right-hand page (MOLA PDF 7: odd pages right, even left), so the book can be split into parts
% c135: cues before the entries at 52 and 59-61 (MOLA PDF 5); the quoted parts without their own score/part-only marks
\addQuote "hnOneQ" { \removeWithTag #'part \hnOne }
\addQuote "oboeOneQ" { \removeWithTag #'(score part) \oboeOne }
\addQuote "vcQ" { \removeWithTag #'(score part) \vc }
% c145: tempo words in adjacent rest bars (poco rit. 47, poco sostenuto 48) ran together on one line in Tbn 1 and other parts; they now stack (Adler part 2 PDF 291 item 1: clear and unproblematical)
\layout { indent = 12\mm \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver"
    \override Hairpin.minimum-length = #8 \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods }
  \context { \Score rehearsalMarkFormatter = #format-mark-box-letters \override RehearsalMark.self-alignment-X = #LEFT \override RehearsalMark.outside-staff-padding = #1 \override MetronomeMark.outside-staff-padding = #1
    \override RehearsalMark.outside-staff-horizontal-padding = #1 \override MetronomeMark.outside-staff-horizontal-padding = #1.5 } \context { \Score skipBars = ##t
  \override MultiMeasureRest.expand-limit = #1 } }
'''
s = [h]
def tacet():
    for n in ("1","2","3"):  # c135: trumpets tacet in this movement; each trumpet book still needs the movement's page (MOLA PDF 5: tacet only for a whole movement)
        s.append(f'''\\bookpart {{ \\header {{ title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Trumpet {n} in C" tagline = ##f }}
      \\markup \\vspace #4 \\markup \\fill-line {{ \\fontsize #6 \\bold "Tacet" }} }}''')
def harp():
    # c165: harp page 2 breaks before 78 (as before rests were joined); without it 71-92 went on one crowded line with arpeggios on the rests at 76 and 78 (MOLA PDF 7: avoid over-crowding)
    s.append(r'''\bookpart { \header { title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "Harp" tagline = ##f }
  \score { \new PianoStaff \with { connectArpeggios = ##t } << \new Staff { \compressMMRests << \partGlobal \partMerge \removeWithTag #'score \harpR { s4*238 \pageBreak s4*21 \break } >> } \new Staff { \clef bass \compressMMRests << \partGlobalPlain \partMerge \removeWithTag #'score \harpL >> } >> \layout { } } }''')
for v,t,clef,tr,keyless in P:
    if v == 'tbnOne': tacet()
    if v == 'vlnOne': harp()  # c165: harp before the strings, in score order (MOLA PDF 4), so the set files in the same order as the score
    mus = f"\\partMerge \\removeWithTag #'score \\{v}"
    body = f"<< \\partGlobal {mus} >>"
    if tr: body = f"\\transpose {tr} c' << {{ \\transposition {tr} }} {body} >>" if tr=='f' else f"\\transpose {tr} c' {body}"
    w = "\\with { \\remove \"Key_engraver\" }" if keyless else ""
    pc = "\\paper { system-system-spacing.padding = #0.5 } " if v == 'vla' else ""  # c221: padding 0.5 (was 1) after the lower triplets at 43-44 pushed it to two pages; c165: the viola part fills its page and has no stacked marks; it keeps the default spacing so it stays on one page (no turn)
    s.append(f'''\\bookpart {{ {pc}\\header {{ title = "Symphony No. 1 in C minor" subtitle = "II. Adagio" instrument = "{t}" tagline = ##f }}
  \\score {{ \\new Staff {w} {{ \\clef {clef} \\compressMMRests {body} }} \\layout {{ }} }} }}''')
open(out,'w').write("\n".join(s))

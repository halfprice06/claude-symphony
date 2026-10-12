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
  print-first-page-number = ##t bookpart-level-page-numbering = ##t oddHeaderMarkup = \markup \fill-line { "" \fromproperty #'header:instrument \if \should-print-page-number \fromproperty #'page:page-number-string }
  evenHeaderMarkup = \markup \fill-line { \if \should-print-page-number \fromproperty #'page:page-number-string \fromproperty #'header:instrument "" } }
\include "score-defs.ily"
noBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))
partGlobalPlain = \noBreaks \global
partGlobal = << \partGlobalPlain { <>_\markup \small \italic "attacca from movement I" } >>
\addQuote "bassTbnQ" { \bassTbn }
\addQuote "corAnglaisQ" { \corAnglais }
\addQuote "bassClQ" { \bassCl }
% c135: bookpart-level-page-numbering: every part starts at page 1 on a right-hand page (MOLA PDF 7: odd pages right, even left), so the book can be split into parts
% c135: cues before the entries at 52 and 59-61 (MOLA PDF 5); the quoted parts without their own score/part-only marks
\addQuote "hnOneQ" { \removeWithTag #'part \hnOne }
\addQuote "oboeOneQ" { \removeWithTag #'(score part) \oboeOne }
\addQuote "vcQ" { \removeWithTag #'(score part) \vc }
\layout { indent = 12\mm \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver"
    \override Hairpin.minimum-length = #8 \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods }
  \context { \Score \override RehearsalMark.outside-staff-padding = #1 \override MetronomeMark.outside-staff-padding = #1
    \override RehearsalMark.outside-staff-horizontal-padding = #1 } \context { \Score skipBars = ##t
  \override MultiMeasureRest.expand-limit = #1 } }
'''
s = [h]
def tacet():
    for n in ("1","2","3"):  # c135: trumpets tacet in this movement; each trumpet book still needs the movement's page (MOLA PDF 5: tacet only for a whole movement)
        s.append(f'''\\bookpart {{ \\header {{ title = "Symphony No. 1 — II. Adagio" instrument = "Trumpet {n} in C" piece = "Trumpet {n} in C" tagline = ##f }}
      \\markup \\vspace #4 \\markup \\fill-line {{ \\fontsize #6 \\bold "Tacet" }} }}''')
for v,t,clef,tr,keyless in P:
    if v == 'tbnOne': tacet()
    mus = f"\\removeWithTag #'score \\{v}"
    body = f"<< \\partGlobal {mus} >>"
    if tr: body = f"\\transpose {tr} c' << {{ \\transposition {tr} }} {body} >>" if tr=='f' else f"\\transpose {tr} c' {body}"
    w = "\\with { \\remove \"Key_engraver\" }" if keyless else ""
    s.append(f'''\\bookpart {{ \\header {{ title = "Symphony No. 1 — II. Adagio" instrument = "{t}" piece = "{t}" tagline = ##f }}
  \\score {{ \\new Staff {w} {{ \\clef {clef} \\compressMMRests {body} }} \\layout {{ }} }} }}''')
s.append(r'''\bookpart { \header { title = "Symphony No. 1 — II. Adagio" instrument = "Harp" piece = "Harp" tagline = ##f }
  \score { \new PianoStaff \with { connectArpeggios = ##t } << \new Staff { \compressMMRests << \partGlobal \removeWithTag #'score \harpR { s4*238 \pageBreak } >> } \new Staff { \clef bass \compressMMRests << \partGlobalPlain \removeWithTag #'score \harpL >> } >> \layout { } } }''')
open(out,'w').write("\n".join(s))

# Writes parts-test.ly: one \book per player, A4 portrait, staff 21 pt (7.4 mm, MOLA PDF 7), compressed multi-measure rests.
import sys
work=sys.argv[1]; filt=sys.argv[2] if len(sys.argv)>2 else 'filter'
P=[('fluteOne','Flute 1',None,'treble',True),('fluteTwo','Flute 2',None,'treble',True),('oboeOne','Oboe 1',None,'treble',True),('oboeTwo','Oboe 2',None,'treble',True),
('corAnglais','Cor anglais in F',"\\transpose f c'",'treble',True),('clOne','Clarinet 1 in B♭',"\\transpose bes c'",'treble',True),('clTwo','Clarinet 2 in B♭',"\\transpose bes c'",'treble',True),
('bassCl','Bass clarinet in B♭',"\\transpose bes c''",'treble',True),('bsnOne','Bassoon 1',None,'bass',True),('bsnTwo','Bassoon 2',None,'bass',True),('cbsn','Contrabassoon',"\\transpose c c'",'bass',True),
('hnOne','Horn 1 in F',"\\transpose f c'",'treble',False),('hnTwo','Horn 2 in F',"\\transpose f c'",'treble',False),('hnThree','Horn 3 in F',"\\transpose f c'",'treble',False),('hnFour','Horn 4 in F',"\\transpose f c'",'treble',False),
('tptOne','Trumpet 1 in C',None,'treble',True),('tptTwo','Trumpet 2 in C',None,'treble',True),('tptThree','Trumpet 3 in C',None,'treble',True),
('tbnOne','Trombone 1',None,'bass',True),('tbnTwo','Trombone 2',None,'bass',True),('bassTbn','Bass trombone',None,'bass',True),('tuba','Tuba',None,'bass',True),
('timp','Timpani',None,'bass',False),('vlnOne','Violin I',None,'treble',True),('vlnTwo','Violin II',None,'treble',True),('vla','Viola',None,'alto',True),('vc','Violoncello',None,'bass',True),('cb','Double bass',"\\transpose c c'",'bass',True)]
out=['\\version "2.24.0"','% c075 (MOLA PDF 5, 7, 8): one A4 part per player, staff 21 pt (7.4 mm), transposed parts (horns and timpani without key signature), multi-measure rests,','% page turns only in rests of 2+ bars (strings use the normal breaker: the inside player turns; parts that cannot turn early start on page 2, MOLA PDF 6), part-only cues kept, score-only marks removed.','% Build from this directory: lilypond -o parts/ parts-book.ly','\\include "parts-head.ily"',
'''stripBreaks = #(define-music-function (m) (ly:music?)
  (music-filter (lambda (x) (not (memq (ly:music-property x 'name) '(LineBreakEvent PageBreakEvent)))) m))''',
'''\\paper { page-breaking = #ly:page-turn-breaking #(set-paper-size "a4") top-margin = 20\\mm bottom-margin = 20\\mm left-margin = 20\\mm right-margin = 20\\mm indent = 8\\mm
  oddHeaderMarkup = \\markup \\fill-line { "" \\fromproperty #'header:instrument \\fromproperty #'page:page-number-string }
  evenHeaderMarkup = \\markup \\fill-line { \\fromproperty #'page:page-number-string \\fromproperty #'header:instrument "" } }''',
'''\\layout { #(layout-set-staff-size 21) \\context { \\Staff \\consists "Page_turn_engraver" } \\context { \\DrumStaff \\consists "Page_turn_engraver" } \\context { \\Score skipBars = ##t minimumPageTurnLength = #(ly:make-moment 2/1) \\override MultiMeasureRest.expand-limit = #1 rehearsalMarkFormatter = #format-mark-box-letters \\override RehearsalMark.font-size = #2 } }''']
COVER = set(sys.argv[3].split(',')) if len(sys.argv)>3 else set()
G = "\\stripBreaks \\global" if filt=='filter' else "\\removeWithTag #'score \\global"
for v,name,tr,clef,key in P:
    music=f"\\removeWithTag #'score \\{v}"
    gl=G
    TP={"\\transpose f c'":"f","\\transpose bes c'":"bes","\\transpose bes c''":"bes,","\\transpose c c'":"c"}
    if tr: music=f"\\transposition {TP[tr]} {tr} {{ {music} }}"; gl=f"{tr} {{ {G} }}"
    keyrm = "" if key else "\\remove \"Key_engraver\""
    stafftype="Staff"
    pb = "\\paper { page-breaking = #ly:optimal-breaking }" if v in ('vlnOne','vlnTwo','vla','vc','cb') else ""
    if v in COVER: pb = "\\paper { first-page-number = 2 }"
    out.append(f'''\\book {{ \\bookOutputName "part-{v}" {pb} \\header {{ title = "Symphony No. 1 — IV. Finale" instrument = "{name}" tagline = ##f }}
  \\score {{ \\new {stafftype} \\with {{ {keyrm} }} << {{ \\clef {clef} {gl} }} {{ \\clef {clef} {music} }} >> \\layout {{ }} }} }}''')
out.append(f'''\\book {{ \\bookOutputName "part-perc" \\header {{ title = "Symphony No. 1 — IV. Finale" instrument = "Cymbals, Bass drum" tagline = ##f }}
  \\score {{ \\new DrumStaff \\with {{ \\override StaffSymbol.line-count = #1 drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 1) (bassdrum default #f -1))) }} << {G} {{ \\removeWithTag #'score \\perc }} >> \\layout {{ }} }} }}''')
out.append(f'''\\book {{ \\bookOutputName "part-harp" \\header {{ title = "Symphony No. 1 — IV. Finale" instrument = "Harp" tagline = ##f }}
  \\score {{ \\new PianoStaff << \\new Staff << {G} {{ \\removeWithTag #'score \\harpR }} >> \\new Staff << {{ \\clef bass {G} }} {{ \\clef bass \\removeWithTag #'score \\harpL }} >> >> \\layout {{ }} }} }}''')
open(work+'/parts-test.ly','w').write('\n'.join(out)+'\n')

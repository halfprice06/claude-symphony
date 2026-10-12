"""Build video.ly from a movement II version folder: 16:9-friendly systems, featured lines coloured,
SVG output attributes for notes, bar lines and staff lines (positions for the video)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import FEATURES, BREAKS, COLORS

src = sys.argv[1]          # folder with score.ly, global.ily, sections/, parts.ily, sections.txt
out = sys.argv[2]          # output folder (gets video.ly, global-video.ily, copies of includes)

score = open(f"{src}/score.ly").read()
glob = open(f"{src}/global.ily").read()
glob = re.sub(r"\\break\b", "", glob)
open(f"{out}/global-video.ily", "w").write(glob)

# bar lengths in quarter notes, from sections.txt (name bars beats)
bars = []
for line in open(f"{src}/sections.txt"):
    p = line.split()
    if len(p) >= 3:
        bars += [int(p[2])] * int(p[1])
nbars = len(bars)

staff_names = re.findall(r'\\new Staff = "([^"]+)"', score)
roles = {n: [None] * (nbars + 1) for n in staff_names}
for a, b, lines, _ in FEATURES:
    for st, r in lines:
        assert st in roles, st
        for k in range(a, b + 1):
            roles[st][k] = r

def var(i):
    return "hl" + "".join(chr(ord("A") + int(c)) for c in str(i))

defs = []
for i, n in enumerate(staff_names):
    seq, cur = [], None
    for k in range(1, nbars + 1):
        r = roles[n][k]
        if r != cur:
            seq.append(r"\hlOff" if r is None else rf"\hlOn #(rgb-color {COLORS[r][0]} {COLORS[r][1]} {COLORS[r][2]})")
            cur = r
        if i == 0:
            if k in BREAKS and k > 1: seq.append(r"\break")
        seq.append(f"s4*{bars[k-1]}")
    defs.append(f"{var(i)} = {{ {' '.join(seq)} }}")

grobs = "NoteHead Stem Beam Flag Dots Accidental Tie Slur PhrasingSlur TupletBracket TupletNumber Script Arpeggio StemTremolo RepeatTie LaissezVibrerTie Fingering StringNumber".split()
hl = ("hlOn = #(define-music-function (col) (color?) #{ "
      + " ".join(rf"\override Staff.{g}.color = #col" for g in grobs) + " #})\n"
      + "hlOff = { " + " ".join(rf"\revert Staff.{g}.color" for g in grobs) + " }\n")

# header and paper
score = re.sub(r"\\header \{.*?\n\}\n", "\\\\header { tagline = ##f }\n", score, count=1, flags=re.S)
score = re.sub(r"#\(set-global-staff-size 14\)", "#(set-global-staff-size 18)", score)
score = re.sub(r"\\paper \{.*?\n\}\n", r"""\\paper {
  paper-width = 280\\mm paper-height = 700\\mm
  top-margin = 8\\mm bottom-margin = 8\\mm left-margin = 6\\mm right-margin = 6\\mm
  indent = 26\\mm short-indent = 16\\mm
  ragged-bottom = ##t ragged-last-bottom = ##t ragged-last = ##f
  max-systems-per-page = 1
  print-page-number = ##f
  oddHeaderMarkup = ##f evenHeaderMarkup = ##f oddFooterMarkup = ##f evenFooterMarkup = ##f
  system-separator-markup = ##f
}
""", score, count=1, flags=re.S)
score = score.replace('\\include "global.ily"', '\\include "global-video.ily"')

# SVG attributes
attrs = r"""
    \override VerticalAxisGroup.remove-first = ##t
    \override NoteHead.output-attributes = #(lambda (g) `((class . "nh") (data-m . ,(vid-mom g))))
    \override BarLine.output-attributes = #(lambda (g) `((class . "bl") (data-m . ,(vid-mom g))))
    \override Rest.output-attributes = #(lambda (g) `((class . "rs") (data-m . ,(vid-mom g))))
    \override MultiMeasureRest.output-attributes = #(lambda (g) `((class . "mm") (data-m . ,(vid-mom g))))"""
score = score.replace('\\context { \\Score \\remove "Bar_number_engraver"', '\\context { \\Score \\remove "Bar_number_engraver"' + attrs, 1)

# per staff: staff-symbol name and the highlight voice
for i, n in enumerate(staff_names):
    key = f'\\new Staff = "{n}"'
    p = score.index(key)
    w = score.index("\\with {", p) + len("\\with {")
    score = score[:w] + f' \\override StaffSymbol.output-attributes = #\'((class . "st") (data-name . "{n}"))' + score[w:]
    q = score.index("<<", score.index(key))
    score = score[:q + 2] + f" \\{var(i)}" + score[q + 2:]

pre = ("#(define (vid-mom g) (let ((c (if (ly:spanner? g) (ly:item-get-column (ly:spanner-bound g LEFT)) (ly:item-get-column g)))) (number->string (if (ly:grob? c) "
       "(exact->inexact (* 4 (ly:moment-main (ly:grob-property c 'when)))) -1))))\n" + hl + "\n".join(defs) + "\n")
score = score.replace("\\score {", pre + "\\score {", 1)
# no MIDI needed
score = re.sub(r"\\midi \{.*?\n\}\n", "}\n", score, count=1, flags=re.S) if False else score
open(f"{out}/video.ly", "w").write(score)
print(len(staff_names), "staves,", nbars, "bars")

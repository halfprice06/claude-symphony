"""Turn a movement's score.ly into strip.ly: the whole movement engraved on one long line, every staff kept,
and SVG output attributes on noteheads (score moment data-m, duration data-d in quarter notes, data-t 1 when a tie
arrives at the head), bar lines
(data-m) and staff lines (data-name = the staff's name), so glow_video.py can find every note on the strip.

python3 make_strip_ly.py OUT_DIR      (OUT_DIR holds a copy of the version folder; writes OUT_DIR/strip.ly)

Works on the four movements' score.ly files (mvt1 v621, mvt2 v600, scherzo v600, finale v600) by editing them as text:
  - titles and the front-matter bookpart go; bookparts lose their page-count;
  - staff size 18 and a one-line paper (ly:one-line-breaking);
  - \\RemoveEmptyStaves is removed, so every staff stays on the strip;
  - MIDI-only \\score blocks and \\midi blocks go (the strip needs no MIDI);
  - the output attributes go into the score's own top-level \\layout block.
"""
import re, sys

out = sys.argv[1]
s = open(f"{out}/score.ly").read()


def skip(s, j):
    """index after the comment or string starting at j, or None"""
    if s.startswith("%{", j):
        return s.index("%}", j + 2) + 2
    if s[j] == "%":
        k = s.find("\n", j)
        return len(s) if k < 0 else k
    if s[j] == '"':
        j += 1
        while s[j] != '"':
            j += 2 if s[j] == "\\" else 1
        return j + 1
    return None


def block_end(s, i):
    """s[i] == '{': index just after its matching '}'"""
    depth, j = 0, i
    while j < len(s):
        k = skip(s, j)
        if k is not None:
            j = k
            continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    raise ValueError("unbalanced braces")


def blocks(s, cmd, top_only=True):
    """(start, brace, end) of each `\\cmd {` block, at brace depth 0 when top_only"""
    res, depth, j = [], 0, 0
    pat = re.compile(r"\\" + cmd + r"\s*\{")
    while j < len(s):
        k = skip(s, j)
        if k is not None:
            j = k
            continue
        if s[j] == "\\" and (depth == 0 or not top_only):
            m = pat.match(s, j)
            if m:   # `\score {` only: \scoreMusic and the like do not match
                b = m.end() - 1
                e = block_end(s, b)
                res.append((j, b, e))
                j = e
                continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
        j += 1
    return res


def remove(s, spans):
    for a, e in sorted(spans, reverse=True):
        s = s[:a] + s[e:]
    return s


# titles
hs = blocks(s, "header")
s = remove(s, [(a, e) for a, _, e in hs])
s = re.sub(r"#\(set-global-staff-size [\d.]+\)", "#(set-global-staff-size 18)", s)

# bookparts: drop the ones without music, take the page settings out of the others
for a, b, e in sorted(blocks(s, "bookpart"), reverse=True):
    body = s[b:e]
    if "\\score" not in body:
        s = s[:a] + s[e:]
        continue
    inner = blocks(body[1:-1], "paper") + blocks(body[1:-1], "header")
    body = "{" + remove(body[1:-1], [(x, y) for x, _, y in inner]) + "}"
    s = s[:b] + body + s[e:]

# scores: drop the MIDI-only ones, take \midi out of the others
for a, b, e in sorted(blocks(s, "score", top_only=False), reverse=True):
    body = s[b:e]
    if "\\midi" in body and "\\layout" not in body:
        s = s[:a] + s[e:]
        continue
    mids = blocks(body[1:-1], "midi", top_only=False)
    if mids:
        body = "{" + remove(body[1:-1], [(x, y) for x, _, y in mids]) + "}"
        s = s[:b] + body + s[e:]

s = s.replace("\\RemoveEmptyStaves", "")

PAPER = r"""\paper {
  paper-width = 280\mm paper-height = 700\mm
  page-breaking = #ly:one-line-breaking
  top-margin = 8\mm bottom-margin = 8\mm left-margin = 6\mm right-margin = 6\mm
  indent = 30\mm short-indent = 16\mm
  ragged-bottom = ##t ragged-last-bottom = ##t ragged-last = ##f
  print-page-number = ##f print-first-page-number = ##f
  oddHeaderMarkup = ##f evenHeaderMarkup = ##f oddFooterMarkup = ##f evenFooterMarkup = ##f
  system-separator-markup = ##f
}
"""
ps = blocks(s, "paper")
a, _, e = ps[0]
s = s[:a] + "\\header { tagline = ##f }\n" + PAPER + s[e:]
s = remove(s, [(x, y) for x, _, y in blocks(s, "paper")[1:]])

DEFS = r"""
#(define (vid-dur g) (let ((e (event-cause g))) (number->string (if (and e (ly:duration? (ly:event-property e 'duration #f))) (exact->inexact (* 4 (ly:moment-main (ly:duration-length (ly:event-property e 'duration))))) 0))))
#(define (vid-mom g) (let ((c (if (ly:spanner? g) (ly:item-get-column (ly:spanner-bound g LEFT)) (ly:item-get-column g)))) (number->string (if (ly:grob? c) (exact->inexact (* 4 (ly:moment-main (ly:grob-property c 'when)))) -1))))
#(define vid-tied (make-hash-table 4096))
#(define (vid-tie-end g) (let ((r (ly:spanner-bound g RIGHT))) (if (ly:grob? r) (hashq-set! vid-tied r #t))))
#(define (vid-staff-name context)
  (make-engraver
    (acknowledgers
      ((staff-symbol-interface engraver grob source-engraver)
        (let ((id (ly:context-id context)))
          (ly:grob-set-property! grob 'output-attributes
            `((class . "st") (data-name . ,(if (string-null? id) "Percussion" id)))))))))
"""
ATTRS = r"""
  \context { \Score
    \override Tie.after-line-breaking = #vid-tie-end
    \override NoteHead.output-attributes = #(lambda (g) `((class . "nh") (data-m . ,(vid-mom g)) (data-d . ,(vid-dur g)) (data-t . ,(if (hashq-ref vid-tied g #f) "1" "0"))))
    \override BarLine.output-attributes = #(lambda (g) `((class . "bl") (data-m . ,(vid-mom g))))
  }
  \context { \Staff \consists #vid-staff-name }
  \context { \DrumStaff \consists #vid-staff-name }
"""
ls = blocks(s, "layout")
a, b, e = ls[0]
s = s[:a] + DEFS + s[a:b + 1] + ATTRS + s[b + 1:]
open(f"{out}/strip.ly", "w").write(s)
print("strip.ly:", len(re.findall(r'\\new Staff = "', s)), "named staves")

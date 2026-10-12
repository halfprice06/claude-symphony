# Usage: python3 -I parts-gen.py parts.ly   (regenerates parts.ly; edit the table P below to change parts, cues or clefs)
# Writes parts.ly (c185). One \book per player; output parts-<nn>-<name>.pdf
import re, sys
out = sys.argv[1]
F = "#(ly:make-pitch -1 3 0)"      # F below middle C
BB = "#(ly:make-pitch -1 6 -1/2)"  # B-flat below middle C
BB2 = "#(ly:make-pitch -2 6 -1/2)" # B-flat a ninth below middle C
C8 = "#(ly:make-pitch -1 0 0)"     # an octave below
# suffix, header name, staff name/mid, music expression, clef, staff-with extras, layout extras
NOKEY = r'\context { \Staff \remove "Key_engraver" }'
VI = ("cueVlnOne", "Vln. I")
VC = ("cueVc", "Vc.")
VA = ("cueVla", "Vla.")
CL = ("cueClOne", "Cl. 1")
# suffix, header name, midi, music, clef, staff \with extras, layout extras, cues [(quote, label, dir, bar, bars)]
P = [
 ("01-flute-1", "Flute 1", "flute", r"\partClean \fluteOne", None, "", "", []),
 ("02-flute-2", "Flute 2", "flute", r"\partClean \fluteTwo", None, "", "", [VI+("DOWN",113,2)]),
 ("03-oboe-1", "Oboe 1", "oboe", r"\partClean \oboeOne", None, "", "", []),
 ("04-oboe-2", "Oboe 2", "oboe", r"\partClean \oboeTwo", None, "", "", [CL+("UP",67,2)]),
 ("05-cor-anglais", "Cor anglais in F", "english horn", r"\transpose f c' CUES \partClean \corAnglais", None, f"instrumentTransposition = {F}", "", []),
 ("06-clarinet-1", "Clarinet 1 in B♭", "clarinet", r"\transpose bes c' CUES \partClean \clOne", None, f"instrumentTransposition = {BB}", "", []),
 ("07-clarinet-2", "Clarinet 2 in B♭", "clarinet", r"\transpose bes c' CUES \partClean \clTwo", None, f"instrumentTransposition = {BB}", "", [CL+("UP",67,2)]),
 ("08-bass-clarinet", "Bass clarinet in B♭ (with low C)", "clarinet", r"<< \bclClefs \transpose bes c'' CUES \partCleanNoClefs \bassCl >>", None, f"instrumentTransposition = {BB2}", "", [VC+("UP",67,2)]),
 ("09-bassoon-1", "Bassoon 1", "bassoon", r"\partClean \bsnOne", "bass", "", "", [VC+("DOWN",67,2)]),
 ("10-bassoon-2", "Bassoon 2", "bassoon", r"\partClean \bsnTwo", "bass", "", "", []),
 ("11-contrabassoon", "Contrabassoon", "bassoon", r"\transpose c c' CUES \partClean \cbsn", "bass", f"instrumentTransposition = {C8}", "", [VC+("DOWN",67,2)]),
 ("12-horn-1", "Horn 1 in F", "french horn", r"\transpose f c' CUES \partCleanNoClefs \hnOne", None, f"instrumentTransposition = {F}", NOKEY, []),
 ("13-horn-2", "Horn 2 in F", "french horn", r"\transpose f c' CUES \partCleanNoClefs \hnTwo", None, f"instrumentTransposition = {F}", NOKEY, []),
 ("14-horn-3", "Horn 3 in F", "french horn", r"\transpose f c' CUES \partCleanNoClefs \hnThree", None, f"instrumentTransposition = {F}", NOKEY, []),
 ("15-horn-4", "Horn 4 in F", "french horn", r"<< \hnFourClefs \transpose f c' CUES \partCleanNoClefs \hnFour >>", None, f"instrumentTransposition = {F}", NOKEY, []),
 ("16-trumpet-1", "Trumpet 1 in C", "trumpet", r"\partClean \tptOne", None, "", NOKEY, [VI+("UP",67,2), VI+("UP",111,2)]),
 ("17-trumpet-2", "Trumpet 2 in C", "trumpet", r"\partClean \tptTwo", None, "", NOKEY, [VI+("UP",67,2), VI+("UP",111,2)]),
 ("18-trumpet-3", "Trumpet 3 in C", "trumpet", r"\partClean \tptThree", None, "", NOKEY, [VI+("UP",80,2), VI+("UP",111,2)]),
 ("19-trombone-1", "Trombone 1", "trombone", r"\partClean \tbnOne", "bass", "", "", [VC+("UP",70,2)]),
 ("20-trombone-2", "Trombone 2", "trombone", r"\partClean \tbnTwo", "bass", "", "", [VC+("UP",70,2), VC+("UP",111,2)]),
 ("21-bass-trombone", "Bass trombone", "trombone", r"\partClean \bassTbn", "bass", "", "", [VC+("UP",70,2)]),
 ("22-tuba", "Tuba", "tuba", r"\partClean \tuba", "bass", "", "", [VC+("UP",70,2), VC+("UP",109,2)]),
 ("23-timpani", "Timpani", "timpani", r"\partClean \timp", "bass", "", NOKEY, []),
 ("26-violin-1", "Violin I", "string ensemble 1", r"\partClean \vlnOne", None, "", "", []),
 ("27-violin-2", "Violin II", "string ensemble 1", r"\partClean \vlnTwo", None, "", "", []),
 ("28-viola", "Viola", "viola", r"\partClean \vla", "alto", "", "", []),
 ("29-violoncello", "Violoncello", "cello", r"\partClean \vc", "bass", "", "", []),
 ("30-double-bass", "Double bass", "contrabass", r"\transpose c c' CUES \partClean \cb", "bass", f"instrumentTransposition = {C8}", "", []),
]
L = []
w = L.append
w(r'''\version "2.24.0"
\language "nederlands"
% c185: instrumental parts, one PDF per player (MOLA Guidelines PDF 5-8). Build (after build.sh, which regenerates parts.ily):
%   cd <version-dir> && mkdir -p partsout && lilypond -dno-point-and-click -o partsout/parts parts.ly
% gives partsout/parts-NN-<instrument>.pdf. PARTS_AUDIT=1 in the environment adds a proofreading log (see parts-lib.ily). The full score is still score.ly; this file changes nothing in it.
% Generated from the same single-player variables as the score (parts.ily), so every player has his own dynamics.

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  tagline = ##f
}
#(set-global-staff-size 20.5) % 7.2 mm staff (MOLA PDF 7: 7.0-7.5 mm for parts)
\paper {
  % B4 (JIS), "the most common size" for parts (MOLA PDF 8; A4 is the minimum)
  paper-width = 257\mm
  paper-height = 364\mm
  top-margin = 15\mm
  bottom-margin = 20\mm
  left-margin = 20\mm
  right-margin = 20\mm
  ragged-last-bottom = ##t
  max-systems-per-page = 12 % MOLA PDF 7: up to twelve staves per page
  % MOLA PDF 7: page turns in rests. Page breaks after odd pages (the turns) are allowed only where the
  % Page_turn_engraver found a rest of at least minimumPageTurnLength; breaks after even pages fall anywhere.
  page-breaking = #ly:page-turn-breaking
  print-first-page-number = ##t
  % default LilyPond headers: page number top right on odd pages, top left on even; instrument name from page 2 (MOLA PDF 7)
}

sec = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))
secDrum = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))

\include "global.ily"
% Parts-only redefinitions, read before the sections so the section variables pick them up:
soloStemsOn = {}   % stem-direction switches for the shared staff
soloStemsOff = {}
pedAflat = \markup \null   % harp pedal diagrams: score only (MOLA PDF 5)
pedNat = \markup \null
pedBflatAflat = \markup \null
\include "sections/intro.ily"
\include "sections/tOne.ily"
\include "sections/trans.ily"
\include "sections/tTwo.ily"
\include "sections/clos.ily"
\include "sections/dev.ily"
\include "sections/recOne.ily"
\include "sections/recTwo.ily"
\include "sections/coda.ily"
\include "parts.ily"
\include "parts-lib.ily"
\include "parts-clefs.ily"

% Cue sources (MOLA PDF 5: cues in long rests, in the reader's key; LilyPond transposes them by instrumentTransposition)
\addQuote "cueVla" { \vla }
\addQuote "cueVc" { \vc }
\addQuote "cueObOne" { \oboeOne }
\addQuote "cueClOne" { \clOne }
\addQuote "cueHnOne" { \hnOne }
\addQuote "cueVlnOne" { \vlnOne }
\addQuote "cueFlOne" { \fluteOne }
\addQuote "cueTimp" { \timp }

% c200: "attacca" at the end of every part, not only Vln I: the five tied parts (Vln I, Vln II, Vla, Vc, Hn 3), Hn 4's relief of
% Hn 3 at movement II bar 1 and the timpani tuning all run straight into movement II (MOLA PDF 5: instructions that govern the
% performance go in all parts, even in rests; PDF 7: players need time to change parts). Vln I's own mark is tagged 'score in coda.ily.
partGlobalPlain = \partGlobalOf \global % harp LH: the RH staff already carries the end mark
partGlobal = << \partGlobalOf \global { \skip 1*182 \textEndMark \markup \italic "attacca" } >>

\layout {
  \context { \Score
    skipBars = ##t
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #2
    \override MultiMeasureRest.expand-limit = #1
    \override MultiMeasureRest.minimum-length = #14 % room for the tempo words and rehearsal letters that fall in rests
    \override SpacingSpanner.spacing-increment = #1.6 % looser than the score: parts are read at a distance (MOLA PDF 7: avoid over-crowding)
    \override MetronomeMark.padding = #1.5
    \override RehearsalMark.padding = #1.5
    \override Hairpin.minimum-length = #5
    \override Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods
    \override MultiMeasureRestNumber.font-size = #0
    % = \markLengthOn: tempo words and rehearsal letters take horizontal space, so a tempo word over a short rest
    % does not stack above the previous one or float away from its bar (MOLA PDF 8 and Ex. 7, PDF 12: collisions and floating markings)
    \override MetronomeMark.extra-spacing-width = #'(0 . 1.0)
    \override RehearsalMark.extra-spacing-width = #'(-0.5 . 0.5)
    \override MetronomeMark.extra-spacing-height = #'(4 . 4)
    \override RehearsalMark.extra-spacing-height = #'(4 . 4)
  }
  % one player per part: dynamics engraved per staff, as in score.ly (a hairpin begun inside a divisi \\\\ passage is ended by the next dynamic)
  \context { \Staff \consists "Page_turn_engraver" }
  \context { \Score minimumPageTurnLength = #(ly:make-moment 2/1) }
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" }
}
''')
# Strings and harp: a cover page (page 1, MOLA PDF 6: needed "when pagination requires the music to begin on page two
# in order to accommodate page turns"), so the music opens on a two-page spread and the first turn comes after page 3.
COVER = r'''
  \paper { bookTitleMarkup = ##f } % the cover page carries the title; no second title block above it
  \markup \column {
    \vspace #12
    \fill-line { \center-column {
      \fontsize #6 \bold "Symphony No. 1 in C minor"
      \vspace #1
      \fontsize #3 "I. Lento — Allegro appassionato"
      \vspace #4
      \fontsize #5 \bold "NAME"
    } }
  }
  \pageBreak'''
def cuelist(cues):
    if not cues: return ""
    return "\\partCues #`(" + " ".join('("%s" "%s" ,%s %d %d)' % c for c in cues) + ") "
for suf, name, mid, mus, clef, withx, lay, cues in P:
    clefs = f"\\clef {clef} " if clef else ""
    cl = cuelist(cues)
    # strings: few rests long enough for a turn; the inside player turns (MOLA PDF 7 asks to consider the instrument), so plain optimal breaking
    strpaper = ""
    mus = mus.replace("CUES ", cl) if "CUES " in mus else cl + mus
    cover = suf[:2] in ("26","27","28","29","30")
    cov = COVER.replace("NAME", name) if cover else ""
    bp_open = ""
    bp_close = ""
    # c185: the key signatures live in \partGlobal, so a transposed part transposes the global too (else a B-flat clarinet reads the concert key)
    mt = re.search(r"\\transpose (\S+) (\S+)", mus)
    glob = (r"\transpose %s %s \partGlobal" % mt.groups()) if mt else r"\partGlobal"
    w(rf'''\book {{
  \bookOutputSuffix "{suf}"
  \header {{ instrument = "{name}" }}{cov}{bp_open}
  \score {{
    \new Staff = "part" \with {{ \audit "{suf}" midiInstrument = "{mid}" {withx} }}
      << {clefs}{glob} {mus} >>
    \layout {{ {lay} }}
  }}{bp_close}
}}''')
# percussion
w(r'''\book {
  \bookOutputSuffix "24-percussion"
  \header { instrument = "Percussion (2 players): cymbals, tam-tam" }
  \score {
    \new DrumStaff = "part" \with { \audit "24-percussion" \override StaffSymbol.line-count = #1 \override Stem.direction = #UP \override LaissezVibrerTie.direction = #UP drumStyleTable = #(alist->hash-table '((crashcymbal cross #f 0) (ridecymbal cross #f 0) (tamtam default #f 0))) }
      << \partGlobal \partClean \perc >>
    \layout { }
  }
}
\book {
  \bookOutputSuffix "25-harp"
  \header { instrument = "Harp" }
COVERHARP
  \score {
    \new PianoStaff = "part" <<
      \new Staff = "Harp RH" \with { \audit "25-harp-rh" } << \partGlobal \partCues #`(("cueVla" "Vla." ,UP 154 2)) \partCleanHarp \harpR >>
      \new Staff = "Harp LH" \with { \audit "25-harp-lh" \override DynamicText.direction = #UP \override DynamicLineSpanner.direction = #UP } << \clef bass \partGlobalPlain \partCleanHarp \harpL >>
    >>
    \layout { }
  }
}''')
L = [x.replace('COVERHARP', COVER.replace('NAME', 'Harp')) for x in L]
open(out, 'w').write('\n'.join(L) + '\n')

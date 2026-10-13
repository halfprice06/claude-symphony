from h import *
PZ = '^\\markup \\italic "pizz."'
AR = '^\\markup \\italic "arco"'

# ---------------- INTRO 1-12 ----------------
write('intro', r"""% INTRODUCTION, bars 1-12 (Allegro vivace). After a pause following movement II.
% 1-3: Hn 1 holds G sharp 4 alone: movement II's last A flat heard again as G sharp, the third of E major (cyclic-notes "Four movements").
% 4-7: the horn call of movement I (E flat-C-B, 3-1-7) in E major: G sharp-E-D sharp-E. D sharp is spelled as E major's leading tone.
% 7-8: clarinets and bassoon turn the chord to E minor (G natural replaces G sharp).
% 9-12: timpani alone: motive x (quarter, two eighths, quarter), the rhythm of the scherzo theme (a melodic timpani figure, still unused in I and II).""", {
    'HnOne': J('gis\'2.~\\pp', "gis'2.~", "gis'2.\\<", "e'2.\\>", "dis'2.", "e'2.~\\!", "e'2 r4", R(5)),
    'HnTwo': J(R(2), "b2.~\\pp", "b2.~", "b2.~", "b2.~", "b2 r4", R(5)),
    'ClOne': J(R(6), "g'2.~\\pp", "g'2 r4", R(4)),
    'ClTwo': J(R(6), "e'2.~\\pp", "e'2 r4", R(4)),
    'BsnOne': J(R(6), "b2.~\\pp", "b2 r4", R(4)),
    'Timp': J('<< R2.*2 { s2.^\\markup \\small \\column { "Timpani: E, G, B, E" "(retuned during the pause)" } s2. } >>',
              "e,4\\pp r4 r4", R(5), "b,4\\p b,8 b,8 g,4", "e,4 r4 r4", "b,4 b,8 b,8 e4", "e,4 r4 r4"),
    'Vc': J(R(2), "e,4\\pp" + PZ + " r4 r4", "R2.", "b,4 r4 r4", "e,4 r4 r4", R(6)),
    'Cb': J(R(2), "e,,4\\pp" + PZ + " r4 r4", "R2.", "b,,4 r4 r4", "e,,4 r4 r4", R(6)),
})

# ---------------- sA 13-56 ----------------
# a 13-28 theme (strings); b 29-44 counterstatement, winds call / strings answer, to V of G; c 45-56 second idea in G major, hemiola.
themeA = ["e''4-.\\p^\\markup \\italic \"leggiero\" b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) b'8-. b'-. g'4-.", "fis'4-. dis'-. b-.",
          "e''4-. b'8-. b'-. e''4-.", "a''2->( gis''8 g''8", "fis''4-.) dis''8-. dis''-. b'4-.", "e''4-. r4 r4",
          "a''4-. g''-. fis''-.", "e''4-. dis''8-. dis''-. e''4-.", "fis''4-.( g''8 a''8) b''4-.", "b''4-. fis''-. dis''-.",
          "e''4-. b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) dis''8-. dis''-. fis''4-.", "e''4-. r4 r4"]
vln1b = ["R2.", "R2.", "e''4-. b'8-. b'-. g'4-.", "fis'4-. dis'-. b-.", "R2.", "R2.", "fis''4-. d''8-. d''-. a'4-.", "d''4-. a'8-. a'-. fis'4-.",
         "g''4-.\\< d''8-. d''-. g''4-.", "b''2->( ais''8 a''8", "g''4-.) d''8-. d''-. b'4-.", "a'4-. fis'-. d'-.",
         "a''4-.\\f d''8-. d''-. a''4-.", "c'''2->( b''8 bes''8", "a''4-.) fis''8-. fis''-. d''4-.", "a'4-. fis'-. d'-."]
second = ["d'''2->(\\f b''4~", "b''4 g'''2", "fis'''2 e'''4~", "e'''4 d'''2)", "e'''2->( cis'''4~", "cis'''4 a'''2", "g'''2 fis'''4~", "fis'''4 e'''2)",
          "d'''4( b''4 g''4", "a''2 fis''4", "g''2.)", "g''4-. r4 r4"]
oct_down = lambda bars: [b.replace("'''", "QQQ").replace("''", "QQ").replace("QQQ", "''").replace("QQ", "'") for b in bars]

vln2a = off(["g'", "g'", "g'", "a'", "g'", "a'", "a'", '-', "a'", "g'", "a'", "a'", "g'", "g'", "a'", '-'])
vln2a[0] = "r4 g'4-.\\pp g'4-."
vln2b = ["R2.", "R2."] + off(["g'", "a'"]) + ["R2.", "R2."] + off(["fis'", "fis'", "b'", "b'", "b'", "a'"])
vln2b[8] = "r4 b'4-.\\< b'4-."
vln2b += off(["c''", "c''", "a'", "c''"]); vln2b[12] = "r4 c''4-.\\f c''4-."
vln2c = ["b'2( d''4~", "d''4 b'2)", "a'2( g'4~", "g'4 g'2)", "a'2( e''4~", "e''4 e''2)", "cis''2( d''4~", "d''4 cis''2)",
         "b'4( d''4 b'4", "c''2 a'4", "b'2.)", "b'4-. r4 r4"]
vla_a = off(["b", "b", "b", "fis", "b", "c'", "dis'", '-', "c'", "b", "c'", "dis'", "b", "b", "dis'", '-'])
vla_a[0] = "r4 b4-.\\pp b4-."
vla_b = ["R2.", "R2."] + off(["b", "fis"]) + ["R2.", "R2."] + off(["d'", "d'", "d'", "d'", "d'", "d'"])
vla_b[8] = "r4 d'4-.\\< d'4-."
vla_b += off(["fis'", "fis'", "fis'", "fis'"]); vla_b[12] = "r4 fis'4-.\\f fis'4-."
vla_c = ["g'2( g'4~", "g'4 g'2)", "fis'2( e'4~", "e'4 d'2)", "e'2( a'4~", "a'4 a'2)", "e'2( fis'4~", "fis'4 a'2)",
         "g'4( g'4 g'4", "fis'2 fis'4", "g'2.)", "g'4-. r4 r4"]
bass_a = ["e,", "e,", "e,", "b,", "e,", "a,", "b,", "e,", "a,", "g,", "a,", "b,", "e,", "g,", "b,", "e,"]
vc_a = down(bass_a); vc_a[0] = "e,4\\p r4 r4"
vc_b = ["R2.", "R2."] + down(["e,", "b,"]) + ["R2.", "R2."] + down(["d", "d", "g,", "g,", "g,", "d", "d", "d", "d", "d"])
vc_b[8] = "g,4\\< r4 r4"; vc_b[12] = "d4\\f r4 r4"
vc_c = ["g,2(\\f" + AR + " b,4~", "b,4 g,2)", "d2( e4~", "e4 b,2)", "a,2( a,4~", "a,4 g,2)", "fis,2( fis,4~", "fis,4 cis2)",
        "d,2.~", "d,2.", "g,2.", "g,4-. r4 r4"]
lower = lambda bars: [b.replace(",", ",,") if "d," not in b else b for b in bars]
cb_a = down([n + "," for n in bass_a]); cb_a[0] = "e,,4\\p r4 r4"
cb_b = ["R2.", "R2."] + down(["e,,", "b,,"]) + ["R2.", "R2."] + down(["d,", "d,", "g,,", "g,,", "g,,", "d,", "d,", "d,", "d,", "d,"])
cb_b[8] = "g,,4\\< r4 r4"; cb_b[12] = "d,4\\f r4 r4"
cb_c = ["g,,2(\\f" + AR + " b,,4~", "b,,4 g,,2)", "d,2( e,4~", "e,4 b,,2)", "a,,2( a,,4~", "a,,4 g,,2)", "fis,,2( fis,,4~", "fis,,4 cis,2)",
        "d,2.~", "d,2.", "g,,2.", "g,,4-. r4 r4"]

fl1b = ["e'''4-.\\p b''8-. b''-. e'''4-.", "g'''2->( fis'''8 f'''8", "e'''4-.) r4 r4", "R2.",
        "e'''4-. b''8-. b''-. e'''4-.", "a'''2->( gis'''8 g'''8", "fis'''4-.) r4 r4", "R2."] + vln1b[8:]
ob1b = ["e''4-.\\p b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) r4 r4", "R2.",
        "e''4-. b'8-. b'-. e''4-.", "a''2->( gis''8 g''8", "fis''4-.) r4 r4", "R2.", "R2.", "R2.", "R2.", "R2."] + vln1b[12:]

write('sA', r"""% SCHERZO, first part, bars 13-56 (E minor).
% 13-28: theme A in Vln I, p leggiero, over pizzicato bass and off-beat crotchets in Vln II and violas. Motive x = crotchet, two quavers, crotchet.
%   The tail G-F sharp-F-E (14-15, 26-27) is the motto's chromatic tail (E flat-D-D flat-C in C) on E's own degrees; F natural is E's Neapolitan, as D flat is C's.
%   Timpani answer at 20 and 28. Cadences: half cadence 16, authentic 20 and 28 (E minor is the key; no C major chord anywhere in the scherzo).
% 29-44: counterstatement as call and response: winds alone (string-free) at 29-30, 33-34; strings answer 31-32, 35-36; together from 37 in G major, on V of G 41-44.
% 45-56: second idea in G major (III), forte, legato, in hemiola (three minims across two bars) against the horns' dotted minims; cadence in G 53-55.""", {
    'FluteOne': J(*(R(16).split('|') if False else ["R2.*16"]), *fl1b, *second),
    'FluteTwo': J("R2.*16", "R2.*8", "d''2.~\\<", "d''2.~", "d''2.~", "d''2.", "fis''2.~\\f", "fis''2.~", "fis''2.", "d''4 r4 r4", "R2.*12"),
    'OboeOne': J("R2.*16", *ob1b, *oct_down(second)),
    'OboeTwo': J("R2.*16", "R2.*12", "d''2.~\\f", "d''2.~", "d''2.", "a'4 r4 r4", "R2.*12"),
    'ClOne': J("R2.*16", "g'2.~\\p", "g'2.", "g'4 r4 r4", "R2.", "a'2.~", "a'2.", "fis'4 r4 r4", "R2.",
               "b'2.~\\<", "b'2.~", "b'2.", "a'2.", "c''2.~\\f", "c''2.", "a'2.", "fis'4 r4 r4", *vln2c),
    'ClTwo': J("R2.*16", "e'2.~\\p", "e'2.", "e'4 r4 r4", "R2.", "e'2.~", "e'2.", "d'4 r4 r4", "R2.",
               "g'2.~\\<", "g'2.~", "g'2.", "fis'2.", "fis'2.~\\f", "fis'2.~", "fis'2.", "d'4 r4 r4", *vla_c),
    'BsnOne': J("R2.*16", "b2.~\\p", "b2.", "b4 r4 r4", "R2.", "c'2.~", "c'2.", "a4 r4 r4", "R2.",
                "d'2.~\\<", "d'2.~", "d'2.", "d'2.", "a2.~\\f", "a2.", "c'2.", "a4 r4 r4", *vc_c),
    'BsnTwo': J("R2.*16", "e2.~\\p", "e2.", "e4 r4 r4", "R2.", "a,2.~", "a,2.", "d4 r4 r4", "R2.",
                "g,2.~\\<", "g,2.~", "g,2.", "d2.", "d2.~\\f", "d2.~", "d2.", "d4 r4 r4", "R2.*12"),
    'Cbsn': J("R2.*32", *[b.replace(AR, '') for b in cb_c]),
    'HnOne': J("R2.*28", "fis'2.~\\f", "fis'2.~", "fis'2.", "d'4 r4 r4",
               "d''2.\\f", "d''2.", "a'2.", "b'2.", "a'2.", "a'2.", "a'2.", "a'2.", "b'2.", "a'2.", "b'2.", "b'4-. r4 r4"),
    'HnTwo': J("R2.*28", "d'2.~\\f", "d'2.~", "d'2.", "a4 r4 r4",
               "g'2.\\f", "g'2.", "fis'2.", "g'2.", "e'2.", "e'2.", "e'2.", "e'2.", "g'2.", "fis'2.", "g'2.", "g'4-. r4 r4"),
    'Timp': J("R2.*7", "r4 b,8\\p b,8 e,4", "R2.*7", "r4 b,8 b,8 e,4", "R2.*27", "g,4-.\\f r4 r4"),
    'VlnOne': J(*themeA, *vln1b, *second),
    'VlnTwo': J(*vln2a, *vln2b, *vln2c),
    'Vla': J(*vla_a, *vla_b, *vla_c),
    'Vc': J(*vc_a, *vc_b, *vc_c),
    'Cb': J(*cb_a, *cb_b, *cb_c),
})

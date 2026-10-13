from h import *
PZ = '^\\markup \\italic "pizz."'
AR = '^\\markup \\italic "arco"'

T = ["gis'2(\\p^\\markup \\italic \"dolce\" a'4", "b'2 e''4)", "dis''4.( cis''8 b'4)", "gis'2.",
     "a'2( b'4", "cis''2 fis''4)", "e''4.( dis''8 cis''4)", "b'2.",
     "cis''2( dis''4", "e''2 gis''4)", "fis''4.( e''8 dis''4)", "cis''4( b'4 a'4)",
     "gis'4( b'4 e''4", "dis''2 fis''4)", "e''2.~", "e''2 r4"]
# harmony per bar: E E B7 E | A F#m F#7 B | C#m E/G# B7 A | E/B B7 E E
Tbass = ["e", "e", "b,", "e", "a,", "fis,", "fis,", "b,", "cis", "gis,", "b,", "a,", "b,", "b,", "e", "e"]
hp_ch = ["<gis b e'>", "<gis b e'>", "<a b dis'>", "<gis b e'>", "<a cis' e'>", "<a cis' fis'>", "<cis' e' fis'>", "<b dis' fis'>",
         "<gis cis' e'>", "<gis b e'>", "<a b dis'>", "<a cis' e'>", "<gis b e'>", "<a b dis'>", "<gis b e'>", "<gis b e'>"]
FlH = ["gis''4( fis''8 gis'' a''4)", "b''4( cis'''8 b'' e'''4)", "dis'''8( e''' dis''' cis''' b''4)", "gis''2.",
       "a''4( gis''8 a'' b''4)", "cis'''4( dis'''8 cis''' fis'''4)", "e'''8( fis''' e''' dis''' cis'''4)", "b''2.",
       "cis'''4( b''8 cis''' dis'''4)", "e'''4( fis'''8 e''' gis'''4)", "fis'''8( gis''' fis''' e''' dis'''4)", "cis'''4( b'' a'')",
       "gis''4( b'' e''')", "dis'''4( e'''8 dis''' fis'''4)", "e'''2.~", "e'''2 r4"]
VcC = ["b,2( cis4", "dis2 e4)", "fis2( a4", "gis2.)", "e2( dis4", "cis2 a,4)", "ais,2( b,4", "dis2.)",
       "e2( fis4", "gis2 e4)", "a2( fis4", "e2 cis4)", "b,2( cis4", "a,2 b,4)", "gis,2.~", "gis,2 r4"]
v2T = ["b'", "b'", "a'", "b'", "a'", "a'", "ais'", "b'", "gis'", "b'", "a'", "a'", "b'", "a'", "gis'", "gis'"]
vlaT = ["e'", "e'", "dis'", "e'", "e'", "fis'", "e'", "dis'", "e'", "e'", "dis'", "e'", "e'", "dis'", "e'", "e'"]
ten = lambda lst: [f"r4 {n}4-- {n}4--" for n in lst]
hpR = lambda: [f"r4 {c}4 {c}4" for c in hp_ch]
hpL = lambda: [f"{n},4 r4 r4" for n in Tbass]
pz = lambda lst: [f"{n}4 r4 r4" for n in lst]
up = lambda lst: [shift(b, 1) for b in lst]

# ---------------- tA 153-184 ----------------
vc1 = pz(Tbass); vc1[0] = "e4\\p" + PZ + " r4 r4"
cb1 = pz([n + "," if "," in n else n.replace("e", "e,").replace("cis", "cis,") for n in Tbass]); cb1[0] = "e,4\\p" + PZ + " r4 r4"
cb1 = [b.replace("b,,", "b,,") for b in cb1]
v1T = up(T); v1T[0] = "gis''2(\\mp^\\markup \\italic \"espressivo\" a''4"
v2a = ten(v2T); v2a[0] = "r4 b'4--\\pp b'4--"
vlaa = ten(vlaT); vlaa[0] = "r4 e'4--\\pp e'4--"
vcC = list(VcC); vcC[0] = "b,2(\\p" + AR + " cis4"
hr = hpR(); hl = hpL(); hl[0] = "e,4\\p r4 r4"
write('tA', r"""% TRIO, first part, bars 153-184 (E major, un poco meno mosso).
% 153-168: the trio tune T in Cl 1, dolce, over the harp's off-beat chords and a soft E-B drone in Hn 3-4 (a musette).
%   T is new material: it rises by step and a fourth (G sharp-A-B-E) and falls back through D sharp, the leading tone (cyclic-notes:
%   the scherzo prepares D sharp as a spelling for the finale's violas). Cadences: half 160, authentic 167.
% 169-184: T in Vln I, an octave higher; Fl 1 doubles it heterophonically (the same line with passing notes and turns: still unused in I and II);
%   the cellos have a countermelody of their own (a melodic bass line), the double basses pizzicato.""", {
    'FluteOne': J("R2.*16", *[FlH[0] + "\\pp"] + FlH[1:]),
    'ClOne': J(*T, "R2.*16"),
    'HnThree': J("b2.~\\pp", "b2.~", "b2.~", "b2", "r4", "b2.~", "b2.~", "b2.~", "b2", "r4", "b2.~", "b2.~", "b2.~", "b2", "r4", "b2.~", "b2.~", "b2.~", "b2", "r4", "R2.*16").replace("b2 | r4", "b2 r4"),
    'HnFour': J("e2.~\\pp", "e2.~", "e2.~", "e2", "r4", "e2.~", "e2.~", "e2.~", "e2", "r4", "e2.~", "e2.~", "e2.~", "e2", "r4", "e2.~", "e2.~", "e2.~", "e2", "r4", "R2.*16").replace("e2 | r4", "e2 r4"),
    'Timp': J("e,4\\pp^\\markup \\small \\italic \"soft sticks\" r4 r4", "R2.*3", "R2.*11", "e,4 r4 r4", "R2.*16"),
    'HarpR': J(*hr, *hr),
    'HarpL': J(*hl, *hpL()),
    'VlnOne': J("R2.*16", *v1T),
    'VlnTwo': J("R2.*16", *v2a),
    'Vla': J("R2.*16", *vlaa),
    'Vc': J(*vc1, *vcC),
    'Cb': J(*cb1, *[b.replace(PZ, '') for b in cb1]),
})

# ---------------- tB 185-216 ----------------
callA = ["e''2(\\p cis''4", "gis''2 fis''4)", "e''4.( dis''8 cis''4)", "bis'2."]
callA = ["e''2(\\p dis''4", "cis''2 gis'4)", "a'4.( b'8 cis''4)", "gis'2."]
ansA = ["e2(\\p dis4", "cis2 gis,4)", "a,4.( b,8 cis4)", "gis,2."]
callB = ["dis''2( cis''4", "b'2 fis'4)", "gis'4.( a'8 b'4)", "fis'2."]
ansB = ["dis2( cis4", "b,2 fis,4)", "gis,4.( a,8 b,4)", "fis,2."]
build = ["fis''2(\\< gis''4", "a''2 cis'''4)", "b''4.( a''8 gis''4)", "fis''2.",
         "e'''2(\\f dis'''4", "cis'''2 gis''4)", "a''4.( b''8 cis'''4)", "gis''2."]
# bass per bar 185-216
bB = ["cis", "cis", "fis,", "gis,", "cis", "cis", "fis,", "gis,", "b,", "b,", "e", "fis,", "b,", "b,", "e", "fis,",
      "fis,", "fis,", "e", "b,", "cis", "cis", "fis,", "gis,", "a,", "a,", "b,", "b,", "b,", "b,", "b,", "b,"]
hpB = ["<gis cis' e'>", "<gis cis' e'>", "<a cis' fis'>", "<gis bis dis'>", "<gis cis' e'>", "<gis cis' e'>", "<a cis' fis'>", "<gis bis dis'>",
       "<b dis' fis'>", "<b dis' fis'>", "<gis b e'>", "<ais cis' fis'>", "<b dis' fis'>", "<b dis' fis'>", "<gis b e'>", "<ais cis' fis'>"]
write('tB', r"""% TRIO, middle part, bars 185-216.
% 185-200: call and response between a woodwind and the cellos: Ob 1 in C sharp minor (185), the cellos answer (189);
%   Ob 1 and cor anglais in B major (193), the cellos answer (197).
% 201-208: the strings together, crescendo to the trio's forte: the oboe's call in C sharp minor in Vln I and II, ending on G sharp (V of C sharp).
% 209-216: A major, then A minor (mixture, iv), to the dominant pedal B; T's head in Cl 1 and Fl 1, diminuendo.""", {
    'FluteOne': J("R2.*24", "R2.*4", "gis''2(\\pp a''4", "b''2.~", "b''2.~", "b''2) r4"),
    'FluteTwo': J("R2.*20", "cis''2.\\f", "cis''2.", "cis''2.", "bis'2.", "R2.*8"),
    'OboeOne': J(*callA, "R2.*4", *callB, "R2.*4", "R2.*4", *[b.replace("'''", "QQ").replace("''", "'").replace("QQ", "''") for b in build[4:]], "R2.*8"),
    'OboeTwo': J("R2.*20", "gis'2.\\f", "gis'2.", "fis'2.", "gis'2.", "R2.*8"),
    'CorAnglais': J("R2.*8", *[shift(b, -1) for b in callB[:1]] + [shift(b, -1) for b in callB[1:]], "R2.*20"),
    'ClOne': J("R2.*16", "a'2.\\p\\<", "cis''2.", "b'2.", "a'2.", "e''2.\\f", "e''2.", "cis''2.", "dis''2.", "R2.*4", "gis'2(\\p a'4", "b'2.~", "b'2.~", "b'2) r4"),
    'ClTwo': J("R2.*16", "fis'2.\\p\\<", "fis'2.", "e'2.", "dis'2.", "gis'2.\\f", "gis'2.", "a'2.", "gis'2.", "e'2.\\p", "e'2.", "dis'2.\\>", "dis'2.", "dis'2.\\!", "dis'2.", "dis'2.", "dis'2."),
    'BsnOne': J("R2.*16", "a2.\\p\\<", "a2.", "gis2.", "fis2.", "gis2.\\f", "gis2.", "fis2.", "bis,2.", "cis'2.\\p", "c'2.", "b2.\\>", "a2.", "fis2.\\!", "fis2.", "fis2.", "fis2."),
    'BsnTwo': J("R2.*20", "cis2.\\f", "cis2.", "fis,2.", "gis,2.", "a,2.\\p", "a,2.", "b,2.", "b,2.", "R2.*4"),
    'HnOne': J("R2.*20", "gis'2.\\f", "gis'2.", "a'2.", "gis'2.", "R2.*8"),
    'HnTwo': J("R2.*20", "e'2.\\f", "e'2.", "fis'2.", "dis'2.", "R2.*8"),
    'HnThree': J("R2.*24", "e'2.\\p", "e'2.", "dis'2.\\>", "dis'2.", "dis'2.\\!", "dis'2.", "dis'2.", "dis'2."),
    'HnFour': J("R2.*24", "cis'2.\\p", "c'2.", "b2.\\>", "b2.", "b2.\\!", "b2.", "b2.", "b2."),
    'Timp': J("R2.*28", "b,2.:32\\pp", "b,2.:32", "b,2.:32", "b,4 r4 r4"),
    'HarpR': J(*[f"r4 {c}4 {c}4" for c in hpB], "R2.*16"),
    'HarpL': J(*[f"{n},4 r4 r4" for n in bB[:16]], "R2.*16"),
    'VlnOne': J("R2.*16", *build, "a'4--\\p r4 r4", "c''4-- r4 r4", "R2.*6"),
    'VlnTwo': J("R2.*16", *[shift(b, -1) for b in build], "cis'4--\\p r4 r4", "e'4-- r4 r4", "R2.*6"),
    'Vla': J("R2.*16", "a2.\\p\\<", "a2.", "gis2.", "a2.", "cis'2.\\f", "cis'2.", "cis'2.", "bis2.", "e'2.\\p", "e'2.", "fis'2.\\>", "fis'2.", "fis'2.\\!", "fis'2.", "fis'2.", "fis'2."),
    'Vc': J("R2.*4", *ansA, "R2.*4", *ansB, "fis,2.\\p\\<" + AR, "fis,2.", "gis,2.", "b,,2.".replace("b,,", "b,"), "cis2.\\f", "cis2.", "fis,2.", "gis,2.", "a,2.\\p", "a,2.", "b,2.", "b,2.", "b,2.", "b,2.", "b,2.", "b,2."),
    'Cb': J(*[f"{n},4 r4 r4".replace(",,,", ",,") if True else "" for n in bB[:16]], "fis,,2.\\p\\<" + AR, "fis,,2.", "gis,,2.", "b,,2.", "cis,2.\\f", "cis,2.", "fis,,2.", "gis,,2.",
            "a,,2.\\p", "a,,2.", "b,,2.", "b,,2.", "b,,4" + PZ + " r4 r4", "b,,4 r4 r4", "b,,4 r4 r4", "b,,4 r4 r4"),
})

# ---------------- tC 217-248 ----------------
v1C = up(T); v1C[0] = "gis''2(\\f^\\markup \\italic \"espressivo\" a''4"; v1C[-1] = "e'''2\\> r4\\!"
hnC1 = ["b'2.\\p", "b'2.", "a'2.", "b'2.", "a'2.", "a'2.", "ais'2.", "b'2.", "gis'2.", "b'2.", "a'2.", "a'2.", "b'2.", "a'2.", "gis'2.", "gis'2."]
hnC2 = ["e'2.\\p", "e'2.", "dis'2.", "e'2.", "e'2.", "fis'2.", "e'2.", "dis'2.", "e'2.", "e'2.", "dis'2.", "e'2.", "e'2.", "dis'2.", "e'2.", "e'2."]
code_bass = ["e", "e", "a,", "e", "e", "e", "a,", "e", "e", "e", "a,", "e", "e", "e", "e", "e"]
write('tC', r"""% TRIO, third part, bars 217-248.
% 217-232: T returns, forte espressivo: Vln I with Fl 1 at the octave above Cl 1; Vln II and violas off-beat; the cellos' countermelody;
%   harp; Hn 1-2 sustain the harmony (no unison horns: the high horn unison is kept for the finale).
% 233-248: codetta over the E pedal with plagal A-E: T's head falls through Ob 1 (233), Cl 1 (237), Hn 1 (241); poco rit. 245-248.""", {
    'FluteOne': J(*[b.replace("\\f^\\markup \\italic \"espressivo\"", "\\f") for b in v1C], "R2.*16"),
    'OboeOne': J("R2.*16", "gis''2(\\p a''4", "b''2.~", "b''2.~", "b''2) r4", "R2.*12"),
    'ClOne': J(*[T[0].replace("\\p^\\markup \\italic \"dolce\"", "\\f")] + T[1:], "R2.*4", "gis'2(\\p a'4", "b'2.~", "b'2.~", "b'2) r4", "R2.*8"),
    'ClTwo': J("R2.*16", "e'2.\\pp", "e'2.", "e'2.", "e'2.", "e'2.", "e'2.", "e'2.", "e'2.", "R2.*8"),
    'BsnOne': J(*[f"{n}2." for n in Tbass], "b2.\\pp", "cis'2.", "b2.", "b2.", "R2.*12"),
    'BsnTwo': J(*[f"{n}2." for n in Tbass], "e2.\\pp", "e2.", "e2.", "e2.", "R2.*12"),
    'HnOne': J(*hnC1, "R2.*8", "gis'2(\\pp a'4", "b'2.~", "b'2.~", "b'2) r4", "R2.*4"),
    'HnTwo': J(*hnC2, "R2.*16"),
    'HnThree': J("R2.*24", "b2.\\pp", "b2.", "b2.", "b2.", "b2.~", "b2.~", "b2.~", "b2 r4"),
    'HnFour': J("R2.*24", "e2.\\pp", "e2.", "e2.", "e2.", "e2.~", "e2.~", "e2.~", "e2 r4"),
    'Timp': J("e,4\\f r4 r4", "R2.*3", "R2.*11", "e,4 r4 r4", "R2.*12", "e,2.:32\\pp", "e,2.:32", "e,2.:32", "e,4 r4 r4"),
    'HarpR': J(*hpR(), *[f"r4 {c}4 {c}4" for c in ["<gis b e'>", "<gis b e'>", "<a cis' e'>", "<gis b e'>"] * 3], "<gis b e'>2.\\arpeggio", "R2.*3"),
    'HarpL': J(*hpL(), *[f"{n},4 r4 r4" for n in code_bass[:12]], "e,2.", "R2.*3"),
    'VlnOne': J(*v1C, "R2.*16"),
    'VlnTwo': J(*[b.replace("--\\pp", "--\\f") for b in v2a], "b'2.\\pp", "b'2.", "a'2.", "b'2.", "b'2.", "b'2.", "a'2.", "b'2.", "b'2.", "b'2.", "a'2.", "b'2.", "b'2.~", "b'2.~", "b'2.~", "b'2 r4"),
    'Vla': J(*[b.replace("--\\pp", "--\\f") for b in vlaa], "gis'2.\\pp", "gis'2.", "e'2.", "gis'2.", "gis'2.", "gis'2.", "e'2.", "gis'2.", "gis'2.", "gis'2.", "e'2.", "gis'2.", "gis'2.~", "gis'2.~", "gis'2.~", "gis'2 r4"),
    'Vc': J(*[VcC[0].replace("(", "(\\f")] + VcC[1:], *[f"{n}4 r4 r4" for n in code_bass], ).replace("e4 r4 r4 | e4 r4 r4 | a,4", "e4\\pp" + PZ + " r4 r4 | e4 r4 r4 | a,4", 1),
    'Cb': J(*[b.replace(PZ, '').replace("\\p", "\\f") for b in cb1], *[f"{n},4 r4 r4" if "," not in n else f"{n},4 r4 r4" for n in code_bass]),
})

# ---------------- retr 249-264 ----------------
write('retr', r"""% RETRANSITION, bars 249-264, poco a poco accelerando to Tempo I.
% The introduction again, compressed: timpani motive x on B; Hn 1 G sharp (249-252) falls to G natural (253): E major turns to E minor;
% the head of theme A in the violas (253), Vln II (257) and Vln I (261), pp, over the pizzicato B.""", {
    'HnOne': J("gis'2.~\\pp", "gis'2.~", "gis'2.~", "gis'2", "r4", "g'2.~", "g'2.~", "g'2", "r4", "R2.*9").replace("gis'2 | r4", "gis'2 r4").replace("g'2 | r4", "g'2 r4"),
    'ClOne': J("R2.*12", "b'2.\\pp", "b'2.", "b'2.", "b'4 r4 r4"),
    'ClTwo': J("R2.*12", "fis'2.\\pp", "fis'2.", "a'2.", "a'4 r4 r4"),
    'Timp': J("b,4\\pp b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "R2.", "R2.^\\markup \\small \\italic \"muta G♯ in G\"", "R2.*3",
              "b,4 b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "R2.", "b,4\\< b,8 b,8 b,4", "b,4 b,8 b,8 b,4", "b,4 b,8 b,8 b,4", "b,4\\p r4 r4"),
    'VlnOne': J("R2.*12", "b'4-.\\pp b'8-. b'-. b'4-.", "dis''4-. fis''-. a''-.", "b''4-. a''-. fis''-.", "dis''4-. b'-. r4"),
    'VlnTwo': J("R2.*8", "e''4-.\\pp b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) r4 r4", "R2.*5"),
    'Vla': J("R2.*4", "e'4-.\\pp" + AR + " b8-. b-. e'4-.", "g'2->( fis'8 f'8", "e'4-.) r4 r4", "R2.*9"),
    'Vc': J("e4\\pp" + PZ + " r4 r4", "R2.", "e4 r4 r4", "R2.", "e4 r4 r4", "R2.", "e4 r4 r4", "R2.", "b,4 r4 r4", "R2.", "b,4 r4 r4", "R2.", "b,4 r4 r4", "b,4 r4 r4", "b,4 r4 r4", "b,4 r4 r4"),
    'Cb': J("e,4\\pp" + PZ + " r4 r4", "R2.", "e,4 r4 r4", "R2.", "e,4 r4 r4", "R2.", "e,4 r4 r4", "R2.", "b,,4 r4 r4", "R2.", "b,,4 r4 r4", "R2.", "b,,4 r4 r4", "b,,4 r4 r4", "b,,4 r4 r4", "b,,4 r4 r4"),
})

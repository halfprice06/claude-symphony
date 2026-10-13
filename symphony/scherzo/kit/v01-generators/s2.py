from h import *
PZ = '^\\markup \\italic "pizz."'
AR = '^\\markup \\italic "arco"'

# ---------------- sB 57-104: development ----------------
# 57-72 fugato on the head of theme A (G minor Vc, D minor Vla, A minor Vln II), stretto 69-72 onto A major (V of D minor).
# 73-88 F major (the Neapolitan of E; A -> F is a falling major third): winds and harp, no strings. The harp has the melody 73-80, Cl 1 81-88.
# 89-104 retransition over the B pedal: timpani motive x, the head rising through Vla, Vln II, Vln I; hemiola build 101-104 to ff.
subj_g = ["g4-.\\p d8-. d-. g4-.", "bes2->( a8 aes8", "g4-.) d8-. d-. bes,4-.", "a,4-. fis,-. d,-."]
subj_d_vla = ["d''4-.\\p d''8-. d''-. d''4-.".replace("d''8-. d''-.", "a'8-. a'-."), "f''2->( e''8 es''8", "d''4-.) a'8-. a'-. f'4-.", "e'4-. cis'-. a-."]
subj_a_v2 = ["a''4-.\\p e''8-. e''-. a''4-.", "c'''2->( b''8 bes''8", "a''4-.) e''8-. e''-. c''4-.", "b'4-. gis'-. e'-."]
cs_g = ["d'4( c' bes", "a2 g4", "f4 e d", "cis2 e4)"]           # countersubject, Vc 61-64 (under the D minor subject)
cs_a_vla = ["a'4( g' f'", "e'2 d'4", "c'4 b a", "gis2 e'4)"]      # Vla 65-68 (under the A minor subject)
str69 = {
    'VlnOne': ["a''4-.\\f e''8-. e''-. a''4-.", "c'''2->( b''8 bes''8", "a''4-.) b''-. cis'''-.", "e'''2.->\\ff"],
    'VlnTwo': ["e''4-. b'8-. b'-. e''4-.", "a''2->( gis''8 g''8", "fis''4-.) gis''-. a''-.", "cis'''2.->\\ff"],
    'Vla': ["c''4-.\\f a'-. a'-.", "e''2-> d''4-.", "cis''4-. d''-. e''-.", "a'2.->\\ff"],
    'Vc': ["a,4-.\\f a-. a,-.", "a,4-. a-. a,-.", "a,4-. a-. a,-.", "a,2.->\\ff"],
}
# F major episode
hpR = ["a''4\\p f''4 a''4", "c'''2 bes''8 a''8", "g''4 d''4 g''4", "bes''2 a''8 g''8", "f''4 c''4 f''4", "a''2 g''8 f''8", "e''4 g''4 bes''4", "a''2.",
       "r4 <d' f' a'>4 <d' f' a'>4", "r4 <d' f' bes'>4 <d' f' bes'>4", "r4 <d' g' bes'>4 <d' g' bes'>4", "r4 <c' f' a'>4 <c' f' a'>4",
       "r4 <c' f' a'>4 <c' f' a'>4", "r4 <c' f' a'>4 <c' f' a'>4", "R2.", "R2."]
hpL = ["f,4 <c f a>2", "f,4 <c f a>2", "g,4 <d g bes>2", "g,4 <d g bes>2", "a,4 <c f a>2", "d,4 <d f a>2", "e,4 <e g bes>2", "f,4 <c f a>2",
       "d,2.", "bes,,2.", "g,,2.", "a,,2.", "a,,2.", "a,,2.", "R2.", "R2."]
cl_mel = ["d''4\\p^\\markup \\italic \"dolce\" a'8 a' d''4", "f''2( e''8 d''8", "bes'4) g'8 g' bes'4", "a'2.",
          "a'4 f'8 f' a'4", "c''2( b'8 bes'8", "a'4) fis'8 fis' dis'4", "fis'2."]
bcl_bass = ["f,2.\\pp", "f,2.", "g,2.", "g,2.", "a,2.", "d,2.", "e,2.", "f,2.", "d,2.", "bes,,2.", "g,2.", "a,2.", "a,2.~", "a,2.~", "a,2.~", "a,2."]
retr_vla = ["e'4-.\\pp b8-. b-. e'4-.", "g'2->( fis'8 f'8", "e'4-.) r4 r4", "R2."]
retr_v2 = ["e''4-.\\pp b'8-. b'-. e''4-.", "a''2->( gis''8 g''8", "fis''4-.) r4 r4", "R2."]
retr_v1 = ["e''4-.\\p\\< b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) b'8-. b'-. g''4-.", "fis''4-. dis''-. b'-."]
hem_v1 = ["b''2\\f a''4~", "a''4 fis''2", "dis'''2 b''4~", "b''4 a''2\\ff"]

write('sB', r"""% SCHERZO, development, bars 57-104.
% 57-72: fugato on the head of theme A: Vc and Bn 1 in G minor (57), violas in D minor over the cellos' countersubject (61),
%   Vln II in A minor over the violas' countersubject (65), stretto in all strings 69-72 onto A major, ff (V of D minor).
% 73-88: F major, the Neapolitan of E (A major -> F major is a falling major third, the symphony's key relation). No strings:
%   the harp has the theme head as a melody 73-80 (still unused colour: a melodic harp line); Cl 1 dolce 81-88, from D minor to the
%   Neapolitan sixth over A (85-86, chromatic tail C-B-B flat) and vii7 of V (87-88).
% 89-104: retransition over the B pedal (pizzicato basses, timpani motive x), the head rising Vla -> Vln II -> Vln I; hemiola build 101-104.""", {
    'FluteOne': J("R2.*12", "a''4-.\\f e''8-. e''-. a''4-.", "c'''2->( b''8 bes''8", "a''4-.) b''-. cis'''-.", "e'''2.->\\ff", "R2.*16",
                  "R2.*12", "b''2\\f a''4~", "a''4 fis''2", "dis'''2 b''4~", "b''4 a''2\\ff"),
    'FluteTwo': J("R2.*15", "a''2.->\\ff", "R2.*28", "fis''2.\\f", "fis''2.", "fis''2.", "dis''2.\\ff"),
    'OboeOne': J("R2.*8", *[b.replace("\\p", "\\pp") for b in subj_a_v2], "a''4-.\\f e''8-. e''-. a''4-.", "c'''2->( b''8 bes''8", "a''4-.) b''-. cis'''-.", "e'''2.->\\ff",
                 "R2.*28", "b'2\\f a'4~", "a'4 fis'2", "dis''2 b'4~", "b'4 a'2\\ff"),
    'OboeTwo': J("R2.*15", "cis'''2.->\\ff", "R2.*28", "dis''2.\\f", "dis''2.", "dis''2.", "b'2.\\ff"),
    'ClOne': J("R2.*4", *[b.replace("\\p", "\\pp") for b in subj_d_vla],
               "R2.*4", "e''4-.\\f b'8-. b'-. e''4-.", "a''2->( gis''8 g''8", "fis''4-.) gis''-. a''-.", "cis'''2.->\\ff",
               "a'2.\\pp", "a'2.", "bes'2.", "bes'2.", "a'2.", "a'2.", "bes'2.", "a'2.", *cl_mel,
               "R2.*12", "a'2\\f fis'4~", "fis'4 dis'2", "fis'2 dis'4~", "dis'4 fis'2\\ff"),
    'ClTwo': J("R2.*15", "a'2.->\\ff", "f'2.\\pp", "f'2.", "d'2.", "d'2.", "c'2.", "d'2.", "e'2.", "f'2.", "f'2.", "f'2.", "g'2.", "f'2.", "f'2.", "f'2.", "dis'2.", "dis'2.",
               "R2.*12", "dis'2.\\f", "dis'2.", "a'2.", "a'2.\\ff"),
    'BassCl': J("R2.*16", *bcl_bass, "R2.*16"),
    'BsnOne': J(*subj_g, "R2.*8", "a2.\\f", "a2.", "a2.", "a2.\\ff",
                "c'2.\\pp", "c'2.", "bes2.", "bes2.", "c'2.", "a2.", "bes2.", "c'2.", "a2.", "bes2.", "bes2.", "a2.", "a2.", "a2.", "a2.", "a2.",
                "R2.*12", "b2.\\f", "a2.", "b2.", "a2.\\ff"),
    'BsnTwo': J("R2.*12", "a,2.\\f", "a,2.", "a,2.", "a,2.\\ff", "R2.*16", "R2.*12", "b,2.\\f", "b,2.", "b,2.", "b,2.\\ff"),
    'Cbsn': J("R2.*12", "a,,2.\\f", "a,,2.", "a,,2.", "a,,2.\\ff", "R2.*28", "b,,2.\\f", "b,,2.", "b,,2.", "b,,2.\\ff"),
    'HnOne': J("R2.*14", "cis''2.\\f", "cis''2.\\ff", "R2.*28", "fis'2.\\f", "fis'2.", "fis'2.", "a'2.\\ff"),
    'HnTwo': J("R2.*14", "a'2.\\f", "a'2.\\ff", "R2.*28", "dis'2.\\f", "dis'2.", "dis'2.", "fis'2.\\ff"),
    'HnThree': J("R2.*16", "c'2.\\pp^\\markup \\italic \"senza sord.\"", "c'2.", "d'2.", "d'2.", "c'2.", "d'2.", "e'2.", "c'2.",
                 "d'2.", "d'2.", "d'2.", "c'2.", "c'2.", "c'2.", "c'2.", "c'2.", "R2.*12", "b2.\\f", "b2.", "b2.", "b2.\\ff"),
    'HnFour': J("R2.*16", "f2.\\pp^\\markup \\italic \"senza sord.\"", "f2.", "g2.", "g2.", "f2.", "f2.", "g2.", "f2.",
                "f2.", "f2.", "g2.", "f2.", "a2.", "a2.", "a2.", "a2.", "R2.*12", "fis2.\\f", "fis2.", "fis2.", "fis2.\\ff"),
    'TptOne': J("R2.*44", "b'4-.\\f b'8-. b'-. b'4-.", "R2.", "b'4-. b'8-. b'-. b'4-.", "dis''2.\\ff"),
    'TptTwo': J("R2.*44", "fis'4-.\\f fis'8-. fis'-. fis'4-.", "R2.", "fis'4-. fis'8-. fis'-. fis'4-.", "a'2.\\ff"),
    'TbnOne': J("R2.*44", "fis2.\\f", "fis2.", "a2.", "a2.\\ff"),
    'TbnTwo': J("R2.*44", "dis2.\\f", "dis2.", "fis2.", "fis2.\\ff"),
    'BassTbn': J("R2.*44", "b,2.\\f", "b,2.", "b,2.", "b,2.\\ff"),
    'Timp': J("R2.*32", "b,4\\pp b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "R2.",
              "b,4\\p b,8 b,8 b,4", "R2.", "b,4 b,8 b,8 b,4", "b,4 b,8 b,8 b,4", "b,2.:32\\<", "b,2.:32", "b,2.:32", "b,4 b,8 b,8 b,4\\ff"),
    'HarpR': J("R2.*16", *hpR, "R2.*16"),
    'HarpL': J("R2.*16", *hpL, "R2.*16"),
    'VlnOne': J("R2.*12", *str69['VlnOne'], "R2.*16", "R2.*8", *retr_v1, *hem_v1),
    'VlnTwo': J("R2.*8", *subj_a_v2, *str69['VlnTwo'], "R2.*16", "R2.*4", *retr_v2, "fis''4-.\\p\\< dis''-. b'-.", "a'4-. fis'-. dis'-.", "b'4-. fis'-. dis'-.", "a'4-. fis'-. dis'-.", "fis''2\\f dis''4~", "dis''4 b'2", "fis''2 dis''4~", "dis''4 fis''2\\ff"),
    'Vla': J("R2.*4", *subj_d_vla, *cs_a_vla, *str69['Vla'], "R2.*16", *retr_vla, "R2.*4", "b4-.\\pp b-. b-.", "b4-. b-. b-.", "b4-.\\< b-. b-.", "b4-. b-. b-.",
             "dis'2\\f fis'4~", "fis'4 a'2", "b'2 fis'4~", "fis'4 dis'2\\ff"),
    'Vc': J(*[subj_g[0].replace("\\p", "\\p" + AR)] + subj_g[1:], *cs_g, "a,2.", "g,2.", "d,2.", "e,2.", *str69['Vc'], "R2.*16",
            "b,,4\\pp".replace("b,,", "b,") + PZ + " r4 r4", *(["b,4 r4 r4"] * 11), "b,2\\f" + AR + " b,4~", "b,4 b,2", "b,2 b,4~", "b,4 b,2\\ff"),
    'Cb': J("R2.*8", "a,,2.\\p", "g,,2.", "d,2.", "e,,2.", "a,,4-.\\f r4 r4", "a,,4-. r4 r4", "a,,4-. r4 r4", "a,,2.->\\ff", "R2.*16",
            "b,,4\\pp" + PZ + " r4 r4", *(["b,,4 r4 r4"] * 11), "b,,2\\f" + AR + " b,,4~", "b,,4 b,,2", "b,,2 b,,4~", "b,,4 b,,2\\ff"),
})

# ---------------- sC 105-140: theme A ff, second idea in E minor, close ----------------
from s1 import themeA
ff_theme = [themeA[0].replace("\\p^\\markup \\italic \"leggiero\"", "\\ff")] + themeA[1:]
sec_e = ["b''2->(\\f g''4~", "g''4 e'''2", "dis'''2 cis'''4~", "cis'''4 b''2)", "c'''2->( a''4~", "a''4 fis'''2", "e'''2 dis'''4~", "dis'''4 b''2)",
         "b''4( g''4 e''4", "fis''2 dis''4", "e''2.)", "e''4-. r4 r4"]
sec_e_v2 = ["g'2( b'4~", "b'4 g'2)", "fis'2( a'4~", "a'4 g'2)", "a'2( c''4~", "c''4 a'2)", "g'2( fis'4~", "fis'4 fis'2)", "g'4( g' g'", "a'2 fis'4", "g'2.)", "g'4-. r4 r4"]
sec_e_vla = ["e'2( e'4~", "e'4 b2)", "b2( e'4~", "e'4 e'2)", "e'2( e'4~", "e'4 c'2)", "b2( b4~", "b4 dis'2)", "e'4( e' e'", "dis'2 b4", "b2.)", "b4-. r4 r4"]
sec_e_bass = ["e,2( g,4~", "g,4 e,2)", "b,2( a,4~", "a,4 g,2)", "a,2( c4~", "c4 dis2)", "e2( b,4~", "b,4 b,2)", "b,2.~", "b,2.", "e,2.", "e,4-. r4 r4"]
close_vc = ["e4-.\\f b,8-. b,-. e4-.", "R2.", "e4-.\\mf b,8-. b,-. e4-.", "R2.", "e4-.\\p b,8-. b,-. g,4-.", "fis,4-. dis,-. b,,-.".replace("b,,", "b,"), "e,4-.\\pp r4 r4", "R2."]
# chords for the ff theme (one per bar): vln2 / vla off-beats
v2ff = off(["g'", "g'", "g'", "a'", "g'", "a'", "a'", "g'", "a'", "g'", "a'", "a'", "g'", "g'", "a'", "g'"]); v2ff[0] = "r4 g'4-.\\ff g'4-."
vlaff = off(["b", "b", "b", "fis'", "b", "c'", "dis'", "b", "c'", "b", "c'", "dis'", "b", "b", "dis'", "b"]); vlaff[0] = "r4 b4-.\\ff b4-."
bassff = ["e,", "e,", "e,", "b,", "e,", "a,", "b,", "e,", "a,", "g,", "a,", "b,", "e,", "g,", "b,", "e,"]
vcff = [f"{n}4->\\ff r4 r4" if i == 0 else f"{n}4-> r4 r4" for i, n in enumerate(bassff)]
cbff = [f"{n},4->\\ff r4 r4" if i == 0 else f"{n},4-> r4 r4" for i, n in enumerate(bassff)]
tbaff = [f"{n},4->\\f r4 r4" if i == 0 else f"{n},4-> r4 r4" for i, n in enumerate(bassff)]
hn12 = ["<b' e''>", "<b' e''>", "<b' e''>", "<b' dis''>", "<b' e''>", "<a' c''>", "<b' dis''>", "<b' e''>", "<a' c''>", "<b' e''>", "<a' c''>", "<b' dis''>", "<b' e''>", "<b' e''>", "<b' dis''>", "<b' e''>"]
hn34 = ["<e' g'>", "<e' g'>", "<e' g'>", "<dis' fis'>", "<e' g'>", "<e' a'>", "<dis' fis'>", "<e' g'>", "<e' a'>", "<e' g'>", "<e' a'>", "<dis' fis'>", "<e' g'>", "<e' g'>", "<dis' fis'>", "<e' g'>"]
hpair = lambda lst, d: [f"{c}4->{d if i == 0 else ''} r4 {c}4-." for i, c in enumerate(lst)]
tpt_x = lambda p, d: [f"{p}4-.{d} {p}8-. {p}-. {p}4-.", "R2.", f"{p}4-. {p}8-. {p}-. {p}4-.", "R2."]
write('sC', r"""% SCHERZO, reprise of the first part, bars 105-140.
% 105-120: theme A ff, tutti: Vln I with Fl 1-2 and Ob 1 at pitch, Cl 1 and Vln II an octave lower; horns on beats 1 and 3,
%   trumpets in motive x (a fanfare figure only: the trumpets have no melody in the scherzo; cyclic-notes), timpani with the bass.
% 121-132: the second idea in E minor (it was in G major at 45), hemiola, f.
% 133-140: close: motive x in the cellos, dying away to E minor pp.""", {
    'FluteOne': J(*[shift(b, 1) if i == 3 else b for i, b in enumerate(ff_theme)], *sec_e, "R2.*8"),
    'FluteTwo': J(*[shift(b, 1) if i == 3 else b for i, b in enumerate(ff_theme)], "R2.*12", "R2.*8"),
    'OboeOne': J(*ff_theme, *[b.replace("'''", "QQ").replace("''", "'").replace("QQ", "''") for b in sec_e], "R2.*8"),
    'OboeTwo': J(*[b.replace("'", "", 1) if False else b for b in [x.replace("''", "'") for x in v2ff]], "R2.*12", "R2.*8"),
    'CorAnglais': J("R2.*28", "e'2.\\p", "e'2.", "e'2.\\>", "e'2.\\!", "R2.*4"),
    'ClOne': J(*[b if i == 3 else shift(b, -1) for i, b in enumerate(ff_theme)], *sec_e_v2, "g'2.\\p", "g'2.", "g'2.\\>", "g'2.\\!", "R2.*4"),
    'ClTwo': J(*[x for x in v2ff], *sec_e_vla, "b2.\\p", "b2.", "b2.\\>", "b2.\\!", "R2.*4"),
    'BsnOne': J(*[f"{n.replace(',', '')}4->\\ff r4 r4" if i == 0 else f"{n.replace(',', '')}4-> r4 r4" for i, n in enumerate(bassff)], *[b.replace(",", "") for b in sec_e_bass], "e2.\\p", "e2.", "e2.\\>", "e2.\\!", "R2.*4"),
    'BsnTwo': J(*vcff, *[b.replace('(', '').replace(')', '') for b in sec_e_bass], "R2.*8"),
    'Cbsn': J(*cbff, *[b.replace(",", ",,") if "c4" not in b and "c4~" not in b and "dis2" not in b else b.replace(",", ",,").replace("c4", "c,4").replace("dis2", "dis,2") for b in sec_e_bass], "R2.*8"),
    'HnOne': J(*hpair(hn12, "\\ff"), "b'2.\\f", "b'2.", "b'2.", "b'2.", "c''2.", "c''2.", "b'2.", "b'2.", "b'2.", "a'2.", "g'2.", "g'4-. r4 r4", "R2.*8"),
    'HnTwo': J(*hpair(hn12, "\\ff"), "g'2.\\f", "g'2.", "fis'2.", "e'2.", "e'2.", "e'2.", "e'2.", "fis'2.", "g'2.", "fis'2.", "e'2.", "e'4-. r4 r4", "R2.*8"),
    'HnThree': J(*hpair(hn34, "\\ff"), "R2.*12", "R2.*8"),
    'HnFour': J(*hpair(hn34, "\\ff"), "R2.*12", "R2.*8"),
    'TptOne': J(*tpt_x("b'", "\\f"), *tpt_x("b'", ""), *tpt_x("b'", ""), *tpt_x("b'", ""), "R2.*20"),
    'TptTwo': J(*tpt_x("e'", "\\f"), *tpt_x("dis'", ""), *tpt_x("e'", ""), *tpt_x("e'", ""), "R2.*20"),
    'TbnOne': J("g2.\\f", "g2.", "g2.", "fis2.", "g2.", "a2.", "fis2.", "g2.", "a2.", "g2.", "a2.", "fis2.", "g2.", "g2.", "fis2.", "g4 r4 r4", "R2.*20"),
    'TbnTwo': J("e2.\\f", "e2.", "e2.", "dis2.", "e2.", "e2.", "dis2.", "e2.", "e2.", "e2.", "e2.", "dis2.", "e2.", "e2.", "dis2.", "e4 r4 r4", "R2.*20"),
    'BassTbn': J("e,2.\\f", "e,2.", "e,2.", "b,2.", "e,2.", "a,2.", "b,2.", "e,2.", "a,2.", "g,2.", "a,2.", "b,2.", "e,2.", "g,2.", "b,2.", "e,4 r4 r4", "R2.*20"),
    'Tuba': J(*tbaff, "R2.*20"),
    'Timp': J("e,4->\\ff r4 r4", "e,4 r4 r4", "e,4 r4 r4", "b,4-> b,8 b,8 b,4", "e,4 r4 r4", "R2.", "b,4 b,8 b,8 b,4", "e,4 r4 r4",
              "R2.", "g,4 r4 r4", "R2.", "b,4 b,8 b,8 b,4", "e,4 r4 r4", "g,4 r4 r4", "b,4 b,8 b,8 b,4", "e,4 r4 r4",
              "R2.*8", "b,2.:32\\f", "b,2.:32", "e,4 r4 r4", "R2.", "R2.*2", "e,4\\p e,8 e,8 e,4", "R2.", "R2.", "e,4\\pp r4 r4", "R2.*2"),
    'VlnOne': J(*ff_theme, *sec_e, "R2.*4", "R2.*4"),
    'VlnTwo': J(*v2ff, *sec_e_v2, "R2.*8"),
    'Vla': J(*vlaff, *sec_e_vla, "R2.*8"),
    'Vc': J(*vcff, *sec_e_bass, *close_vc),
    'Cb': J(*cbff, *[b.replace(",", ",,") if "c4" not in b and "dis2" not in b else b.replace(",", ",,").replace("c4", "c,4").replace("dis2", "dis,2") for b in sec_e_bass],
            "e,,4-.\\f r4 r4", "R2.", "e,,4-.\\mf r4 r4", "R2.", "e,,4-.\\p r4 r4", "b,,4-. r4 r4", "e,,4-.\\pp r4 r4", "R2."),
})

# ---------------- link 141-152: E minor -> E major ----------------
write('link', r"""% LINK to the trio, bars 141-152. The intro in reverse: Hn 1 G natural (141-144) rises to G sharp (145), E major;
% the harp enters with E major (pedals set during 105-140); poco rit. 149-152.""", {
    'HnOne': J("g'2.~\\pp", "g'2.~", "g'2.~", "g'2", "r4", "gis'2.~\\<", "gis'2.~", "gis'2.\\>", "gis'2", "r4\\!", "R2.*4").replace("g'2 | r4 |", "g'2 r4 |").replace("gis'2 | r4\\! |", "gis'2 r4\\! |"),
    'ClOne': J("R2.*4", "e'2.\\pp", "e'2.", "e'2.", "e'2 r4", "R2.*4"),
    'ClTwo': J("R2.*4", "b2.\\pp", "b2.", "b2.", "b2 r4", "R2.*4"),
    'BsnOne': J("b,2.\\pp", "b,2.", "b,2.", "b,2 r4", "R2.*8"),
    'BsnTwo': J("e,2.\\pp", "e,2.", "e,2.", "e,2 r4", "R2.*8"),
    'Timp': J("R2.*4", "R2.^\\markup \\small \\italic \"muta G in G♯\"", "R2.*3", "e,4\\pp r4 r4", "R2.", "b,4 r4 r4", "R2."),
    'HarpR': J("R2.*8", "r4 <gis' b' e''>4\\arpeggio r4", "R2.", "r4 <gis' b' e''>4\\arpeggio r4", "R2."),
    'HarpL': J("R2.*8", "e,4\\pp r4 r4", "R2.", "e,4 r4 r4", "R2."),
    'Vc': J("R2.*8", "e,4\\pp" + PZ + " r4 r4", "R2.", "b,4 r4 r4", "R2."),
    'Cb': J("R2.*8", "e,,4\\pp" + PZ + " r4 r4", "R2.", "b,,4 r4 r4", "R2."),
})

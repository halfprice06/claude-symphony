from h import *
from s1 import oct_down
PZ = '^\\markup \\italic "pizz."'
AR = '^\\markup \\italic "arco"'


def xo(top, low, n, d=''):
    """motive x as an ostinato: top, low, low, top"""
    return [f"{top}4-.{d if i == 0 else ''} {low}8-. {low}-. {top}4-." for i in range(n)]


peak = ["e'''4-.\\ff b''8-. b''-. e'''4-.", "g'''2->( fis'''8 f'''8", "e'''4-.) b''8-. b''-. g'''4-.", "b'''2.->"]
cad = ["a'''2-> fis'''4~", "fis'''4 dis'''2", "e'''4-> r4 r4", "R2."]
Tend_v1 = ["cis'''2(\\pp dis'''4", "e'''2 gis'''4)", "fis'''4.( e'''8 dis'''4)", "cis'''4( b'' a'')", "gis''4( b'' e''')", "dis'''2( fis'''4)", "e'''2.~", "e'''2 r4"]
P = {}
P['VlnOne'] = J("R2.*3", *xo("b''", "fis''", 1, "\\pp\\<"), "e''4-.\\mf b'8-. b'-. e''4-.", "d''4-. a'8-. a'-. d''4-.", "cis''4-. g'8-. g'-. cis''4-.", "b'4-. fis'8-. fis'-. a'4-.\\f",
                *peak, *cad, "R2.*8", *Tend_v1, "R2.*12", "gis''2.~\\ppp", *["gis''2.~"] * 6, "gis''2.")
P['FluteOne'] = J("R2.*8", *peak, *cad, "R2.*8", *Tend_v1, "R2.*4", "gis''2.\\pp", "gis''2.~", "gis''2.~", "gis''2 r4", "R2.*12")
P['FluteTwo'] = J("R2.*8", "b''2.\\ff", "b''2.", "b''2.", "dis'''2.", "dis'''2.", "b''2.", "e''4-> r4 r4", "R2.", "R2.*36")
P['OboeOne'] = J("R2.*8", *oct_down(peak), *oct_down(cad), "R2.*36")
P['OboeTwo'] = J("R2.*8", "g''2.\\ff", "g''2.", "g''2.", "fis''2.", "fis''2.", "fis''2.", "g''4-> r4 r4", "R2.", "R2.*36")
P['ClOne'] = J("R2.*4", "g'2.\\mf\\<", "fis'2.", "e'2.", "dis'2.", "e''2.\\ff", "e''2.", "e''2.", "dis''2.", "dis''2.", "dis''2.", "e''4-> r4 r4", "R2.",
               "R2.*4", "a'2(\\p b'4", "cis''2 fis''4)", "e''4.( dis''8 cis''4)", "b'2.", "R2.*12", "e'2.\\pp", "e'2.~", "e'2.~", "e'2 r4", "R2.*12")
P['ClTwo'] = J("R2.*4", "e'2.\\mf\\<", "d'2.", "cis'2.", "b2.", "b'2.\\ff", "b'2.", "b'2.", "a'2.", "a'2.", "a'2.", "b'4-> r4 r4", "R2.", "R2.*20", "b2.\\pp", "b2.~", "b2.~", "b2 r4", "R2.*12")
P['BassCl'] = J("R2.*4", "e,2.\\mf\\<", "d,2.", "cis,2.", "b,,2.\\f", "R2.*8", "R2.*36")
P['BsnOne'] = J("R2.*4", "b2.\\mf\\<", "a2.", "g2.", "fis2.", "g2.\\ff", "g2.", "g2.", "fis2.", "fis2.", "fis2.", "e4-> r4 r4", "R2.", "R2.*16", "gis2.\\p", "g2.", "a2.", "gis2.", "R2.*16")
P['BsnTwo'] = J("R2.*4", "e2.\\mf\\<", "d2.", "cis2.", "b,2.", "e2.\\ff", "e2.", "e2.", "b,2.", "b,2.", "b,2.", "e,4-> r4 r4", "R2.", "R2.*16", "e2.\\p", "e2.", "e2.", "e2.", "R2.*16")
P['Cbsn'] = J("R2.*8", "e,,2.\\ff", "e,,2.", "e,,2.", "b,,2.", "b,,2.", "b,,2.", "e,,4-> r4 r4", "R2.", "R2.*36")
P['HnOne'] = J("R2.*8", "b'2.\\ff", "b'2.", "b'2.", "b'2.", "b'2.", "a'2.", "g'4-> r4 r4", "R2.",
               "gis'2(\\p^\\markup \\italic \"dolce\" a'4", "b'2 e''4)", "dis''4.( cis''8 b'4)", "gis'2.", "R2.*12",
               "b'2.(\\p", "ais'2.", "a'2.", "gis'2.)~", "gis'2.~\\pp", *["gis'2.~"] * 14, "gis'2.")
P['HnTwo'] = J("R2.*8", "g'2.\\ff", "g'2.", "g'2.", "fis'2.", "fis'2.", "fis'2.", "e'4-> r4 r4", "R2.", "R2.*16", "e'2.\\p", "e'2.", "e'2.", "e'2.", "e'2.\\pp", "e'2.~", "e'2.~", "e'2 r4", "R2.*12")
P['HnThree'] = J("R2.*8", "e'2.\\ff", "e'2.", "e'2.", "dis'2.", "dis'2.", "dis'2.", "e'4-> r4 r4", "R2.", "R2.*36")
P['HnFour'] = J("R2.*8", "b2.\\ff", "b2.", "b2.", "b2.", "b2.", "b2.", "b4-> r4 r4", "R2.", "R2.*36")
P['TptOne'] = J("R2.*8", "b'4-.\\f b'8-. b'-. b'4-.", "R2.", "b'4-. b'8-. b'-. b'4-.", "b'2.->\\ff", "a'2.", "a'2.", "g'4-> r4 r4", "R2.", "R2.*36")
P['TptTwo'] = J("R2.*8", "e'4-.\\f e'8-. e'-. e'4-.", "R2.", "e'4-. e'8-. e'-. e'4-.", "dis'2.->\\ff", "dis'2.", "dis'2.", "e'4-> r4 r4", "R2.", "R2.*36")
P['TbnOne'] = J("R2.*8", "g2.\\ff", "g2.", "g2.", "fis2.", "fis2.", "fis2.", "g4-> r4 r4", "R2.", "R2.*36")
P['TbnTwo'] = J("R2.*8", "e2.\\ff", "e2.", "e2.", "dis2.", "dis2.", "dis2.", "e4-> r4 r4", "R2.", "R2.*36")
P['BassTbn'] = J("R2.*8", "e,2.\\ff", "e,2.", "e,2.", "b,2.", "b,2.", "b,2.", "e,4-> r4 r4", "R2.", "R2.*36")
P['Tuba'] = J("R2.*8", "e,2.\\ff", "e,2.", "e,2.", "b,,2.", "b,,2.", "b,,2.", "e,4-> r4 r4", "R2.", "R2.*36")
P['Timp'] = J("R2.*4", "e,4\\mf r4 r4", "R2.", "R2.", "b,2.:32\\<", "e,4->\\ff e,8 e,8 e,4", "R2.", "e,4 e,8 e,8 e,4", "b,2.:32", "b,2.:32", "b,2.:32", "e,4-> r4 r4", "R2.",
              "R2.*16", "R2.*6", "b,4\\pp b,8 b,8 e,4", "R2.", "R2.*2", "b,4 b,8 b,8 e,4", "R2.", "R2.*3", "e,2.:32\\ppp", "e,2.:32", "e,2.:32", "e,4 r4 r4", "R2.")
hpc = ["<gis b e'>", "<gis b e'>", "<a b dis'>", "<gis b e'>", "<a cis' e'>", "<a cis' fis'>", "<cis' e' fis'>", "<b dis' fis'>"]
P['HarpR'] = J("R2.*16", *[f"r4 {c}4 {c}4" for c in hpc], "R2.*12", "<e' gis' b' e''>2.\\arpeggio", "R2.*13", "<e gis b>4\\arpeggio r4 r4", "R2.")
P['HarpL'] = J("R2.*16", *[f"{n},4\\pp r4 r4" if i == 0 else f"{n},4 r4 r4" for i, n in enumerate(["e", "e", "b,", "e", "a,", "fis,", "fis,", "b,"])],
               "R2.*12", "<e, b,>2.\\arpeggio", "R2.*13", "<e,, e,>4\\arpeggio r4 r4", "R2.")
P['VlnTwo'] = J("R2.*2", *xo("e''", "b'", 6, "\\pp\\<"), "g''2.\\ff", "g''2.", "g''2.", "fis''2.", "fis''2.", "fis''2.", "g''4-> r4 r4", "R2.",
                "R2.*8", "e''2.\\pp", "e''2.", "dis''2.", "e''2.", "e''2.", "a'2.", "gis'2.", "gis'2.", "gis'2.\\p", "cis''2.", "c''2.", "b'2.",
                "b'2.~\\pp", "b'2.~", "b'2.~", "b'2 r4", "R2.*12")
P['Vla'] = J("R2.", *xo("b", "fis", 7, "\\pp\\<"), "e'2.\\ff", "e'2.", "e'2.", "dis'2.", "dis'2.", "dis'2.", "e'4-> r4 r4", "R2.",
             "e'2.\\pp", "e'2.", "dis'2.", "e'2.", "e'2.", "fis'2.", "e'2.", "dis'2.", "gis'2.", "b'2.", "a'2.", "e'2.", "e'2.", "fis'2.", "e'2.", "e'2.",
             "e'2.\\p", "g'2.", "a'2.", "gis'2.", "gis'2.~\\pp", "gis'2.~", "gis'2.~", "gis'2 r4", "R2.*12")
Tb = ["e", "e", "b,", "e", "a,", "fis,", "fis,", "b,", "cis", "gis,", "b,", "a,", "b,", "b,", "e", "e"]
vcT = [f"{n}4 r4 r4" for n in Tb]; vcT[0] = "e4\\p" + PZ + " r4 r4"
cbT = [f"{n},4 r4 r4" for n in Tb]; cbT[0] = "e,4\\p" + PZ + " r4 r4"
P['Vc'] = J(*xo("e", "b,", 8, "\\pp\\<" + AR), "e,2.\\ff", "e,2.", "e,2.", "b,2.", "b,2.", "b,2.", "e,4-> r4 r4", "R2.",
            *vcT, "e2.\\p" + AR, "e2.", "e2.", "e2.", "e2.~\\pp", "e2.~", "e2.~", "e2 r4", "R2.*10", "e,4\\pp" + PZ + " r4 r4", "R2.")
P['Cb'] = J("R2.*4", "e,4-.\\p" + AR + " r4 r4", "d,4-. r4 r4", "cis,4-. r4 r4", "b,,4-.\\f r4 r4", "e,,2.\\ff", "e,,2.", "e,,2.", "b,,2.", "b,,2.", "b,,2.", "e,,4-> r4 r4", "R2.",
            *cbT, "e,2.\\p" + AR, "e,2.", "e,2.", "e,2.", "e,2.~\\pp", "e,2.~", "e,2.~", "e,2 r4", "R2.*10", "e,,4\\pp" + PZ + " r4 r4", "R2.")

write('coda', r"""% CODA, bars 341-392.
% 341-356 Più mosso: motive x as a stretto ostinato entering from the bottom (Vc 341, Vla 342, Vln II 343, Vln I 344), pp crescendo; the bass falls
%   E-D-C sharp-B (345-348); theme A's head ff (349); Vln I peaks on B6 at 352 (the scherzo's highest note, a semitone under the finale's C7);
%   hemiola cadence 353-354, E minor chord ff (355), general pause (356).
% 357-392 Meno mosso (tempo del Trio), E major: T returns p in Hn 1 (357), Cl 1 (361), Vln I and Fl 1 (365), cadence 371.
% 373-376: Hn 1 sings the motto's chromatic tail on the fifth degree, B-A sharp-A-G sharp (E flat-D-D flat-C transposed),
%   over E - A sharp dim7 - A minor (iv, mixture) - E: a plagal close that ends on G sharp.
% 377-392: E major held pp, then only Hn 1 and Vln I on G sharp (the pitch that opened the scherzo, movement II's A flat) over a timpani roll
%   and a last pizzicato E; the finale can take that G sharp as A flat.""", P)

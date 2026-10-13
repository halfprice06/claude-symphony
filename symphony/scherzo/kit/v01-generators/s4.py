from h import *
from s1 import themeA, vln1b, second, vln2a, vln2b, vln2c, vla_a, vla_b, vla_c, vc_a, vc_b, vc_c, cb_a, cb_b, cb_c, oct_down
import s2
PZ = '^\\markup \\italic "pizz."'
AR = '^\\markup \\italic "arco"'


def part(sec, k):
    """read a generated section variable back (for reuse), without braces"""
    import re
    txt = open(f"{OUT}/{sec}.ily").read()
    m = re.search(rf"^{sec}{k} = {{ (.*) }}$", txt, re.M)
    return m.group(1).rstrip(' |') if m else None


def bars(sec, k, a, b):
    """bars a..b (1-based, inclusive) of a generated section variable, as a list of bar strings (R2.*n expanded)"""
    s = part(sec, k)
    if s is None:
        return ['R2.'] * (b - a + 1)
    out = []
    for t in s.split(' | '):
        t = t.strip()
        if t.startswith('R2.*'):
            out += ['R2.'] * int(t[4:])
        else:
            out.append(t)
    return out[a - 1:b]


# ---------------- dA 265-300 ----------------
FlA = ["e'''4-.\\pp^\\markup \\italic \"leggiero\" b''8-. b''-. e'''4-.", "g'''8( a''' g''' fis''' f'''4)", "e'''8( dis''' e''' b'' g''4)", "fis''8( e'' dis'' cis'' b'4)",
       "e'''4-. b''8-. b''-. e'''4-.", "a'''8( b''' a''' gis''' g'''4)", "fis'''8( e''' dis''' cis''' b''4)", "e'''4-. r4 r4",
       "a'''8( b''' a''' g''' fis'''4)", "e'''8( fis''' e''' dis''' e'''4)", "fis'''8( g''' a''' g''' fis'''4)", "b''8( a'' fis'' a'' dis''4)",
       "e'''4-. b''8-. b''-. e'''4-.", "g'''8( a''' g''' fis''' f'''4)", "e'''8( dis''' e''' fis''' dis'''4)", "e'''4-. r4 r4"]
v2pz = [b.replace("-.", "") for b in vln2a]; v2pz[0] = "r4 g'4\\pp" + PZ + " g'4"
call = ["e''4-.\\p b'8-. b'-. e''4-.", "g''2->( fis''8 f''8", "e''4-.) r4 r4", "R2."]
s_ans = ["R2.", "R2.", "fis''4-.\\p d''8-. d''-. a'4-.", "d''4-. a'8-. a'-. fis'4-."]

def sec_part(k, a, b):
    return bars('sA', k, a, b)

dA = {}
for k in INSTR:
    th = sec_part(k, 1, 16)        # theme 13-28
    cs = sec_part(k, 29, 32)       # 41-44 (sA bars 29-32)
    sd = sec_part(k, 33, 44)       # second idea
    if th is None or len(th) == 0:
        th = ['R2.'] * 16
    dA[k] = [th, cs, sd]
# theme: Vln II pizzicato, Fl 1 heterophony; counterstatement compressed to 8 bars
dA['VlnTwo'][0] = v2pz
dA['FluteOne'][0] = FlA
mid = {k: ['R2.'] * 4 for k in INSTR}
mid['OboeOne'] = call
mid['ClOne'] = [shift(b, -1) if False else b for b in ["g'2.~\\p", "g'2.", "g'4 r4 r4", "R2."]]
mid['ClTwo'] = ["e'2.~\\p", "e'2.", "e'4 r4 r4", "R2."]
mid['BsnOne'] = ["b2.~\\p", "b2.", "b4 r4 r4", "R2."]
mid['VlnOne'] = s_ans
mid['VlnTwo'] = ["R2.", "R2."] + off(["fis'", "fis'"])
mid['Vla'] = ["R2.", "R2."] + off(["d'", "d'"])
mid['Vc'] = ["R2.", "R2.", "d4\\p" + PZ + " r4 r4", "d4 r4 r4"]
mid['Cb'] = ["R2.", "R2.", "d,4\\p" + PZ + " r4 r4", "d,4 r4 r4"]
parts = {}
for k in INSTR:
    th, cs, sd = dA[k]
    # the sA bars 41-44 (counterstatement end) begin f; keep them
    parts[k] = J(*th, *mid[k], *cs, *sd)
write('dA', r"""% SCHERZO RETURNS, bars 265-300 (Tempo I).
% 265-280: theme A as at 13, but Vln II pizzicato and Fl 1 doubling the violins heterophonically two octaves up (pp, with turns and passing notes).
% 281-288: the counterstatement compressed: Ob 1 calls (281), the violins answer on V of G (283), then 285-288 = 41-44.
% 289-300: the second idea in G major, as at 45-56.""", parts)

# ---------------- dB 301-316 ----------------
parts = {}
for k in INSTR:
    a = bars('sB', k, 1, 8)
    b = bars('sB', k, 13, 16)
    c = bars('sB', k, 45, 48)
    parts[k] = J(*a, *b, *c)
write('dB', r"""% DEVELOPMENT, shortened, bars 301-316: fugato entries in G minor (cellos, 301) and D minor (violas over the countersubject, 305),
% stretto onto A major ff (309-312 = 69-72), then straight to the hemiola on V7 (313-316 = 101-104). The F major episode is not repeated.""", parts)

# ---------------- dC 317-340 ----------------
parts = {}
for k in INSTR:
    a = bars('sC', k, 1, 16)
    b = bars('sC', k, 29, 36)
    parts[k] = J(*a, *b)
write('dC', r"""% THEME A, ff tutti, bars 317-332 (= 105-120), then the close 333-340 (= 133-140), dying away to pp before the coda.""", parts)


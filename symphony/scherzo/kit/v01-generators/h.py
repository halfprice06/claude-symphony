# Helpers for writing the scherzo's v01 sections (3/4 throughout). Later versions are edited by hand.
import os
OUT = os.environ.get('OUT', '/tmp/sch/v01/sections')
INSTR = ['FluteOne', 'FluteTwo', 'OboeOne', 'OboeTwo', 'CorAnglais', 'ClOne', 'ClTwo', 'BassCl', 'BsnOne', 'BsnTwo', 'Cbsn',
         'HnOne', 'HnTwo', 'HnThree', 'HnFour', 'TptOne', 'TptTwo', 'TptThree', 'TbnOne', 'TbnTwo', 'BassTbn', 'Tuba',
         'Timp', 'HarpR', 'HarpL', 'VlnOne', 'VlnTwo', 'Vla', 'Vc', 'Cb']


def R(n):
    return '' if n == 0 else ('R2.' if n == 1 else f'R2.*{n}')


def J(*bars):
    """join bar strings with bar checks; empty strings are skipped"""
    return ' | '.join(b for b in bars if b) + ' |'


def rep(bar, n):
    return [bar] * n


def dyn(seq, d):
    """attach a dynamic (or any postfix) to the first sounding note of a bar string"""
    import re
    m = re.search(r"(<[^>]*>|[a-g](?:isis|eses|is|es|s)?[',]*)(\d+\.*)?((?:-[.>\-^_!]|\([^\s]*)*)", seq)
    # find first note that is not a rest
    toks = seq.split(' ')
    for i, t in enumerate(toks):
        if t and (t[0] in 'abcdefg<') and not t.startswith('R'):
            # insert after duration/articulations, before slur/tie markers is fine for LilyPond
            toks[i] = t + d
            return ' '.join(toks)
    return seq


def off(notes, art='-.'):
    """one bar per entry: rest on beat 1, staccato quarters on beats 2 and 3; '-' = full-bar rest"""
    out = []
    for n in notes:
        out.append('R2.' if n == '-' else f'r4 {n}4{art} {n}4{art}')
    return out


def down(notes, art=''):
    """one bar per entry: quarter on beat 1, then rests"""
    return ['R2.' if n == '-' else f'{n}4{art} r4 r4' for n in notes]


def held(notes):
    """dotted halves; a trailing '~' in an entry ties to the next bar"""
    return ['R2.' if n == '-' else f'{n.rstrip("~")}2.' + ('~' if n.endswith('~') else '') for n in notes]


def write(name, header, parts):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name + '.ily'), 'w') as f:
        f.write(header.rstrip() + '\n\n')
        for k in INSTR:
            if k in parts and parts[k]:
                f.write(f'{name}{k} = {{ {parts[k]} }}\n')


import re as _re
def _octs(o):
    return "'" * o if o > 0 else "," * (-o)
def shift(ly, k):
    """shift every note in a LilyPond string by k octaves (k > 0 up); markups in double quotes are left alone"""
    parts = _re.split(r'("[^"]*")', ly)
    def rep(m):
        o = m.group(2)
        return m.group(1) + _octs(o.count("'") - o.count(",") + k)
    for i in range(0, len(parts), 2):
        parts[i] = _re.sub(r"(?<![A-Za-z\\])([a-g](?:isis|eses|is|es|s)?)([',]*)(?=[0-9<>\s\(\)~\-\\\^_|.:]|$)", rep, parts[i])
    return ''.join(parts)

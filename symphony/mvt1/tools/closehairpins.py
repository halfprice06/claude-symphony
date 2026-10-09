"""Terminate hairpins that run into rests.

A crescendo or diminuendo that is still open when a part reaches a rest is
closed on that rest with \\!, so the hairpin does not continue across empty bars.
Edits the given .ily files in place and reports how many hairpins it closed.
"""
import re
import sys

EV = re.compile(r'\\(<|>|!|ppp|pp|p|mp|mf|fff|ff|f|sfz|fp|sf)(?![A-Za-z])')
REST = re.compile(r'^(R\d|r(1|2)(?!\d))')

total = 0
for path in sys.argv[1:]:
    src = open(path).read()
    out, opened, n = [], False, 0
    # Process token by token, keeping whitespace; reset state at each variable definition.
    for tok in re.split(r'(\s+)', src):
        if re.match(r'^\w+$', tok) and False:
            pass
        if tok.endswith('=') or re.match(r'^[A-Za-z]+$', tok) and tok in ('',):
            pass
        if REST.match(tok) and opened and not EV.search(tok):
            tok = tok + '\\!'
            opened, n = False, n + 1
        evs = EV.findall(tok)
        if evs:
            opened = evs[-1] in ('<', '>')
        if tok.strip() == '}' or tok.startswith('%'):
            opened = False if tok.strip() == '}' else opened
        out.append(tok)
    open(path, 'w').write(''.join(out))
    total += n
print(f"closed {total} hairpins")

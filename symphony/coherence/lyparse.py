#!/usr/bin/env python3
"""Minimal reader for the symphony's section files (absolute-pitch LilyPond, one variable per instrument).

part_events(version_dir, suffix) -> list of (bar, beat_in_bar, midi_pitch_or_None, quarter_length) for one instrument
across the whole movement, in sections.txt order. A chord gives its top note; ties are merged; rests are dropped.
Bars are counted from sections.txt (beats column = quarter beats per bar). Used by themecheck.py.
"""
import re, os
from fractions import Fraction as F

STEP = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
NOTE = re.compile(r"([a-g])((?:is|es|s)*)([',]*)[!?]?")

def pitch(tok):
    m = NOTE.fullmatch(tok)
    if not m:
        return None
    l, acc, octs = m.groups()
    p = 48 + STEP[l] + 1 * acc.count('is') - acc.count('es') - (1 if acc == 's' else 0)
    p += 12 * octs.count("'") - 12 * octs.count(',')
    return p

def strip(text):
    text = re.sub(r'%\{.*?%\}', ' ', text, flags=re.S)
    text = re.sub(r'\\tag\s*#\'part\s*\\cueDuring\s*#"[^"]*"\s*#\w+\s*\{[^}]*\}', ' ', text)
    # score view: drop part-only braced blocks (\tag #'part { ... })
    while True:
        m = re.search(r"\\tag\s*#'part\s*\{", text)
        if not m:
            break
        i, depth = m.end(), 1
        while depth:
            depth += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        text = text[:m.start()] + ' ' + text[i:]
    text = re.sub(r'\\clef\s+"?\w+"?', ' ', text)
    text = re.sub(r'\\(override|revert|once|tweak)\s+[\w.-]+(\s*=\s*#\S+|\s+#\S+)?', ' ', text)
    text = re.sub(r"\\offset\s+[\w.-]+\s+#'?\([^)]*\)\s+[\w.]+", ' ', text)
    text = re.sub(r'\\(set|unset)\s+[\w.]+(\s*=\s*(#\S+|"[^"]*"))?', ' ', text)
    text = re.sub(r"#'\w+", ' ', text)
    text = re.sub(r'%[^\n]*', ' ', text)
    text = re.sub(r'"(?:\\.|[^"\\])*"', ' ', text)
    # markup with a braced argument: drop the braces' content
    while True:
        m = re.search(r'\\markup(?:\s*\\[a-zA-Z-]+)*\s*\{', text)
        if not m:
            break
        i, depth = m.end(), 1
        while depth:
            depth += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        text = text[:m.start()] + ' ' + text[i:]
    text = re.sub(r'\\markup(?:\s*\\[a-zA-Z-]+)*', ' ', text)
    return text

TOKEN = re.compile(r"<<|>>|\\transpose|\\[a-zA-Z]+|\\[<>!]|[{}|~()\[\]]|<[^<>]*>[0-9]*\.*|[a-gsrR](?:[a-z]*)[',]*[!?]?[0-9]*\.*(?:\*[0-9]+(?:/[0-9]+)?)?(?::[0-9]+)?")

def variables(path):
    text = strip(open(path).read())
    out = {}
    for m in re.finditer(r'([A-Za-z]+)\s*=\s*\{', text):
        i, depth = m.end(), 1
        while depth:
            depth += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        out[m.group(1)] = text[m.end():i - 1]
    return out

def dur(spec, prev):
    m = re.match(r'([0-9]+)?(\.*)(?:\*([0-9]+)(?:/([0-9]+))?)?', spec)
    base, dots, mul, div = m.groups()
    d = F(4, int(base)) if base else prev[0]
    if base:
        b = d
        for _ in dots:
            b /= 2; d += b
        prev[0] = d
    elif dots:
        pass
    mult = F(int(mul), int(div) if div else 1) if mul else 1
    return d, d * mult

def events(body):
    """-> list of (pitch or None, length in quarters, tied_to_next)"""
    toks = TOKEN.findall(body)
    out, prev, trans, i = [], [F(1)], [0], 0
    stack = []  # transpose stack, pushed at '{' after \transpose
    pending = None
    while i < len(toks):
        t = toks[i]; i += 1
        if t == '<<':
            # keep the first element only (the intro timpani label is a spacer branch)
            depth, j = 1, i
            while depth:
                depth += {'<<': 1, '>>': -1}.get(toks[j], 0); j += 1
            inner = toks[i:j - 1]
            first = inner[:1]
            out += events(' '.join(first))
            i = j
            continue
        if t == '\\transpose':
            a, b = pitch(toks[i]), pitch(toks[i + 1]); i += 2
            pending = b - a
            continue
        if t == '{':
            stack.append(pending or 0); trans[0] += pending or 0; pending = None
            continue
        if t == '}':
            if stack:
                trans[0] -= stack.pop()
            continue
        if t == '~':
            if out:
                p, l, _ = out[-1]; out[-1] = (p, l, True)
            continue
        if t.startswith('\\') or t in '|()[]':
            continue
        if t.startswith('<'):
            m = re.match(r'<([^<>]*)>(.*)', t)
            ps = [pitch(x) for x in m.group(1).split() if pitch(x) is not None]
            _, total = dur(m.group(2), prev)
            out.append((max(ps) + trans[0], total, False))
            continue
        m = re.match(r"([a-gsrR][a-z]*[',]*[!?]?)([0-9]*\.*(?:\*[0-9]+(?:/[0-9]+)?)?)", t)
        name, spec = m.groups()
        _, total = dur(spec, prev)
        if name[0] in 'rRs' and re.fullmatch(r'[rRs]', name):
            out.append((None, total, False))
        else:
            p = pitch(name.rstrip('!?'))
            out.append((None if p is None else p + trans[0], total, False))
    return out

def sections(vdir):
    rows = []
    for line in open(os.path.join(vdir, 'sections.txt')):
        f = line.split()
        if len(f) >= 2:
            rows.append((f[0], int(f[1]), int(f[2]) if len(f) > 2 else 4))
    return rows

def part_events(vdir, suffix):
    res, bar0 = [], 1
    for name, bars, beats in sections(vdir):
        path = os.path.join(vdir, 'sections', name + '.ily')
        body = variables(path).get(name + suffix) if os.path.exists(path) else None
        pos = F(0)
        if body is not None:
            merged = []
            for p, l, tie in events(body):
                if merged and merged[-1][3] and merged[-1][1] == p and p is not None:
                    q = merged[-1]; merged[-1] = (q[0], p, q[2] + l, tie)
                else:
                    merged.append((pos, p, l, tie))
                pos += l
            for start, p, l, _ in merged:
                if p is not None:
                    bar = bar0 + int(start // beats)
                    res.append((bar, start - (bar - bar0) * beats, p, l))
        bar0 += bars
    return res

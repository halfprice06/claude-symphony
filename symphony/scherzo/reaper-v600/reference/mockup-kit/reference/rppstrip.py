"""Strip large plugin state blobs from a REAPER .RPP for study copies.
Keeps every line except the base64 body of <VST ...> blocks whose header matches PATTERN
(default: Opus). Prints a size report to stderr. Usage: rppstrip.py in.RPP out.RPP [pattern]"""
import sys, re, collections
src, dst = sys.argv[1], sys.argv[2]
pat = re.compile(sys.argv[3] if len(sys.argv) > 3 else 'Opus', re.I)
sizes = collections.Counter(); out = []
stack = []  # (header, strip?)
with open(src, 'r', encoding='utf-8', errors='surrogateescape') as f:
    for line in f:
        s = line.strip()
        if s.startswith('<'):
            hdr = s
            strip = s.startswith('<VST') and bool(pat.search(s))
            stack.append((hdr, strip, 0))
            out.append(line)
            if strip:
                out.append(line[:len(line) - len(line.lstrip())] + '  ' + '(plugin state removed in this study copy)\n')
            continue
        if s == '>' and stack:
            hdr, strip, n = stack.pop()
            if hdr.startswith('<VST'):
                name = re.findall(r'"([^"]*)"', hdr)
                sizes[(name[0] if name else hdr[:40], strip)] += n
            out.append(line); continue
        if stack and stack[-1][1]:
            h, st, n = stack[-1]; stack[-1] = (h, st, n + len(line)); continue
        if stack and stack[-1][0].startswith('<VST'):
            h, st, n = stack[-1]; stack[-1] = (h, st, n + len(line))
        out.append(line)
with open(dst, 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.writelines(out)
tot = collections.Counter()
for (name, strip), n in sizes.items(): tot[(re.sub(r'\s*\(.*', '', name), strip)] += n
for (name, strip), n in tot.most_common(12):
    print(f'{n/1e6:8.2f} MB  {"STRIPPED " if strip else "kept     "}{name}', file=sys.stderr)

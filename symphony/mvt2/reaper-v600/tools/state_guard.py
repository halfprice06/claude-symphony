"""mvt2 c50 (ONE_TIME; from mvt1 c52's tools/state_guard.py, scherzo c09): find Opus instances whose saved state is
not the state build_reaper wrote.

After an Opus instance has played, REAPER's saved project can hold runtime values in its state: the AHDSR attacks of the
legato sustain groups at 20 ms instead of the written 267-1501 ms (scherzo c09; mvt1 c51). A --midi-only build keeps
that saved state, and the render then plays loud legato joins early and louder. This tool decodes every Opus block of a
saved .rpp and compares each group's AHDSR attack with the state build_reaper last wrote for the track
(jobs/NN_<patch>.b64). Movement II has one pass, so --pass2 selects nothing here.

Usage: python state_guard.py RPP PARTS JOBS [--json OUT] [--quiet]
  Prints one line per track; exit status 1 when any instance differs (its name is on a "STALE" line), 0 otherwise.
  build_reaper.py --midi-only calls stale_tracks() on the project it builds into and fully rebuilds those tracks;
  render_cycle.py refuses to render a project that still holds one (--force-stale overrides).
"""
import base64, json, os, re, sys, zlib
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import opus_state

GZ = b"\x1f\x8b\x08"


def rpp_opus_blocks(rpp):
    """{track name: [base64 lines of its first Opus VST block]} from a saved .rpp (streamed; 120 MB files)"""
    out, name, block, depth_vst = {}, None, None, None
    with open(rpp, encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if s.startswith("<TRACK"):
                name = None
            elif s.startswith("NAME ") and name is None and block is None:
                name = s[5:].strip().strip('"')
            elif s.startswith('<VST "VST3i: Opus') and name is not None and name not in out:
                block, depth_vst = [], len(line) - len(line.lstrip())
            elif block is not None:
                if s == ">" and len(line) - len(line.lstrip()) == depth_vst:
                    out[name] = block
                    block = None
                else:
                    block.append(s)
    return out


def decode_block(lines):
    """the Opus performance JSON of an .rpp VST3 block (several base64 segments; decoded line by line)"""
    b = b"".join(base64.b64decode(l) for l in lines if l)
    i = b.find(GZ)
    if i < 0:
        return None
    return json.loads(zlib.decompressobj(31).decompress(b[i:]))


def decode_b64(text):
    return opus_state.split(text)[1]


def _instrument_zones(js):
    for z in js.get("zones", []):
        inst = z.get("instrument")
        if isinstance(inst, dict):
            yield inst


def attacks(js):
    """[(group name, attack)] for every AHDSR processor of every group, in order"""
    out = []
    for inst in _instrument_zones(js):
        for g in inst.get("groups", []):
            for p in (g.get("processors") or {}).get("processors", []):
                if p.get("class") == "AHDSR":
                    out.append((g.get("name", "?"), p.get("attack")))
    return out


def compare(saved, written):
    """(number of differing attacks, examples) between two decoded states; None when the group lists differ in length"""
    a, b = attacks(saved), attacks(written)
    if len(a) != len(b):
        return None, [f"{len(a)} AHDSR groups saved, {len(b)} written"]
    bad = [(ga, va, vb) for (ga, va), (gb, vb) in zip(a, b) if va != vb]
    ex = [f"{g}: {va} (written {vb})" for g, va, vb in bad[:3]]
    return len(bad), ex


def b64_path(jobs, i, tr):
    return f"{jobs}/{i:02d}_{tr['stem'].replace(' ', '_')}.b64"


def check(rpp, parts, jobs, pass2=False):
    """[{track, status, n, examples}] for the parts.json tracks of the pass; status ok / STALE / missing / no-jobs"""
    d = json.load(open(parts)) if isinstance(parts, str) else parts
    blocks = rpp_opus_blocks(rpp)
    rows = []
    for i, tr in enumerate(d["tracks"]):
        if (tr.get("pass", 1) == 2) != pass2:
            continue
        name = tr["name"]
        bf = b64_path(jobs, i, tr)
        if name not in blocks:
            rows.append({"track": name, "status": "missing", "n": 0, "examples": []})
            continue
        if not os.path.exists(bf):
            rows.append({"track": name, "status": "no-jobs", "n": 0, "examples": [bf]})
            continue
        saved = decode_block(blocks[name])
        written = decode_b64(open(bf).read())
        if saved is None:
            rows.append({"track": name, "status": "STALE", "n": -1, "examples": ["state not decodable"]})
            continue
        n, ex = compare(saved, written)
        rows.append({"track": name, "status": "ok" if n == 0 else "STALE", "n": n if n is not None else -1,
                     "examples": ex})
    return rows


def stale_tracks(rpp, parts, jobs, pass2=False):
    """names of the tracks whose saved Opus state has AHDSR attacks other than the written ones"""
    if not os.path.exists(rpp):
        return set()
    return {r["track"] for r in check(rpp, parts, jobs, pass2) if r["status"] == "STALE"}


def main():
    a = sys.argv[1:]
    if len(a) < 3:
        sys.exit(__doc__)
    rpp, parts, jobs = a[:3]
    pass2 = "--pass2" in a
    rows = check(rpp, parts, jobs, pass2)
    quiet = "--quiet" in a
    for r in rows:
        if r["status"] != "ok" or not quiet:
            print(f"{r['status']:8s} {r['track']}: {r['n']} attacks differ" + (f"  ({'; '.join(r['examples'])})" if r["examples"] else ""))
    if "--json" in a:
        json.dump(rows, open(a[a.index("--json") + 1], "w"), indent=1)
    nst = sum(r["status"] == "STALE" for r in rows)
    print(f"state_guard: {len(rows)} tracks, {nst} stale, {sum(r['status'] == 'missing' for r in rows)} missing")
    sys.exit(1 if nst else 0)


if __name__ == "__main__":
    main()

"""mvt3 c07 (copied into Movement II c44; string values added): edit REAPER <FXCHAIN> text from the EW template chunks before build_reaper.py returns_job pastes it.

Ported from Movement I's tools/template_mix.py (its c50: header_info, set_header_size, vst_runs, _json_end,
spaces_split, spaces_set, the ReaEQ decode/encode), so that a mix.json "returns" entry can carry
  "set": {"irSetup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}}   values of the Spaces II processor JSON
  "hp_hz": 160                                                                 band 0 (high pass) of the return's ReaEQ
Chunk layout (template_mix.py docstring): a VST block's body is three base64 runs: REAPER's header (one line), the
plugin state (lines of 128 chars; what vst_chunk reads and writes), the program-name trailer (one line).
EW Spaces II state: u32 len - 16, u32 flag, the processor JSON, the editor JSON, JUCE data. spaces_set() changes values
inside the processor JSON text and keeps every other byte.
"""
import base64, json, re, struct

MAGICS = (0xFEED5EEE, 0xFEED5EEF)


def header_info(hdr):
    uid, magic, nin = struct.unpack_from("<III", hdr, 0)
    if magic not in MAGICS:
        raise ValueError(f"not a REAPER VST header (magic {magic:#x})")
    off = 12 + 8 * nin
    nout = struct.unpack_from("<I", hdr, off)[0]
    off += 4 + 8 * nout
    return {"size": struct.unpack_from("<I", hdr, off)[0], "size_at": off}


def set_header_size(hdr, n):
    at = header_info(hdr)["size_at"]
    return hdr[:at] + struct.pack("<I", n) + hdr[at + 4:]


def strip_reaper_header(data):
    """a state read back from REAPER, without REAPER's header if it carries one (template_mix.py)"""
    if len(data) >= 8 and struct.unpack_from("<I", data, 4)[0] in MAGICS:
        info = header_info(data)
        return data[info["size_at"] + 12:info["size_at"] + 12 + info["size"]]
    return data


def vst_runs(lines):
    raw = [base64.b64decode(l) for l in lines]
    if len(raw) < 3:
        raise ValueError("a VST block needs at least three base64 lines")
    hdr, data, trailer = raw[0], b"".join(raw[1:-1]), raw[-1]
    if header_info(hdr)["size"] != len(data):
        raise ValueError(f"header size {header_info(hdr)['size']} != state run {len(data)} bytes")
    return hdr, data, trailer


def b64_lines(data, width=128):
    s = base64.b64encode(data).decode()
    return [s[i:i + width] for i in range(0, len(s), width)] or [""]


def _json_end(b, start):
    depth, i, instr = 0, start, False
    while i < len(b):
        c = b[i:i + 1]
        if instr:
            if c == b"\\":
                i += 1
            elif c == b'"':
                instr = False
        elif c == b'"':
            instr = True
        elif c == b"{":
            depth += 1
        elif c == b"}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unterminated JSON object")


def spaces_split(data):
    n0, flag = struct.unpack_from("<II", data, 0)
    if n0 != len(data) - 16:
        raise ValueError(f"Spaces state: first u32 {n0} != len - 16 ({len(data) - 16})")
    if data[8:9] != b"{":
        raise ValueError("Spaces state: no JSON at byte 8")
    end = _json_end(data, 8)
    return flag, data[8:end].decode("utf-8"), data[end:]


def spaces_json(data):
    """the processor JSON of a Spaces II state (also of one read back from REAPER, which may lack the length prefix)"""
    try:
        return json.loads(spaces_split(data)[1])
    except ValueError:
        i = data.index(b"{")
        return json.loads(data[i:_json_end(data, i)])


def _fmt(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str):   # mvt2 c44: string values (e.g. impulseA / impulseB, presetName)
        return json.dumps(v)
    v = float(v)
    if v.is_integer():
        return f"{v:.1f}"
    r = repr(v)
    return r if "e" not in r else f"{v:.12f}".rstrip("0")


_SCALAR = r'(?:"(?:[^"\\]|\\.)*"|-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|true|false|null)'


def flat_set(changes):
    flat = {}
    for k, v in changes.items():
        if k.startswith("_"):
            continue
        if isinstance(v, dict):
            flat.update({k2: v2 for k2, v2 in v.items() if not k2.startswith("_")})
        else:
            flat[k] = v
    return flat


def spaces_set(data, changes):
    flat = flat_set(changes)
    flag, text, rest = spaces_split(data)
    for k, v in flat.items():
        pat = re.compile(r'("' + re.escape(k) + r'":)' + _SCALAR)
        if len(pat.findall(text)) != 1:
            raise ValueError(f"Spaces state: key {k!r} occurs {len(pat.findall(text))} times")
        text = pat.sub(lambda m_: m_.group(1) + _fmt(v), text)
    json.loads(text)
    body = struct.pack("<II", 0, flag) + text.encode("utf-8") + rest
    return struct.pack("<I", len(body) - 16) + body[4:]


def reaeq_set_band_hz(data, band, hz):
    ver, nb = struct.unpack_from("<II", data, 0)
    if band >= nb:
        raise ValueError(f"ReaEQ has {nb} bands, no band {band}")
    off = 8 + 33 * band + 8
    return data[:off] + struct.pack("<d", float(hz)) + data[off + 8:]


def reaeq_bands(data):
    ver, nb = struct.unpack_from("<II", data, 0)
    out = []
    for b in range(nb):
        off = 8 + 33 * b
        t, en = struct.unpack_from("<II", data, off)
        f, g, bw = struct.unpack_from("<ddd", data, off + 8)
        out.append((t, en, f, g, bw))
    return out


def edit_fxchain(text, spaces=None, reaeq_hp_hz=None):
    """the <FXCHAIN> text with every EW Spaces II block's processor JSON changed by `spaces` (spaces_set) and band 0 of
    the first ReaEQ block set to reaeq_hp_hz; returns (text, {"spaces": state bytes, "reaeq": state bytes})"""
    lines = text.split("\n")
    out, i, states, eq_done = [], 0, {}, False
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<VST "):
            out.append(lines[i])
            ind = lines[i + 1][:len(lines[i + 1]) - len(lines[i + 1].lstrip())]
            j, body = i + 1, []
            while lines[j].strip() != ">":
                body.append(lines[j].strip())
                j += 1
            hdr, data, trailer = vst_runs(body)
            changed = False
            if "EW Spaces II" in s and spaces:
                data = spaces_set(data, spaces)
                changed = True
                states["spaces"] = data
            elif "ReaEQ" in s and reaeq_hp_hz and not eq_done:
                if reaeq_bands(data)[0][0] != 4:
                    raise ValueError("the return ReaEQ's band 0 is not a high pass")
                data = reaeq_set_band_hz(data, 0, reaeq_hp_hz)
                changed, eq_done = True, True
                states["reaeq"] = data
            if changed:
                hdr = set_header_size(hdr, len(data))
                body = b64_lines(hdr) + b64_lines(data) + b64_lines(trailer)
            out += [ind + l for l in body]
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), states


if __name__ == "__main__":   # offline check: python3 tools/fxchunk.py CHUNK.txt
    import sys
    t = open(sys.argv[1]).read()
    t2, st = edit_fxchain(t, {"irSetup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}}, 160)
    print(spaces_json(st["spaces"])["irSetup"], reaeq_bands(st["reaeq"])[0])
    t3, _ = edit_fxchain(t2)
    assert t3 == t2
    print(len(t), len(t2))

"""mvt1 c50: EastWest's own HO REAPER template mix (loop/TEMPLATE-PLAN.md sections 1-3 and 8): chunk parsing, return
tracks, family EQ and sends for build_reaper.py. Keys and checks: tools/TEMPLATE-TOOLS.md.

build_reaper.py imports this module only when build/mix.json holds one of the c50 keys ("send_profile", "returns",
"family_eq", ...). Without them nothing here runs, and the Lua jobs and Opus states are byte-identical to c49
(tools/build_identity_check.py).

Chunk format, read from symphony/mockup-research/ew-template-2026-11-08/ho-mix-chunks/*.txt (verbatim <FXCHAIN> blocks):
  A plugin is a block `<VST "VST: ReaEQ (Cockos)" reaeq.vst.dylib 0 "" 1919247729<...> ""` whose lines are three base64
  runs, each padded on its own:
  1. one line: REAPER's header: u32 plugin id, u32 magic 0xFEED5EEE (or ...EF), u32 n_in, n_in x u64 input pin masks, u32 n_out,
     n_out x u64 output pin masks, u32 size of run 2, u32 1, u32 flags;
  2. the plugin state, in lines of 128 characters. This run is what TrackFX_Get/SetNamedConfigParm(fx, "vst_chunk")
     read and write: the Opus states build_reaper.py loads are the same kind of run (u32 len - 16, u32 1, data);
  3. one line: VST2 the program name ("\\0Program 1\\0\\x10\\0\\0\\0"), VST3 six zero bytes.
ReaEQ state: u32 0x21, u32 n_bands, per band u32 type (0 low shelf, 1 high shelf, 3 low pass, 4 high pass, 8 band),
  u32 enabled, f64 frequency (Hz), f64 gain (linear), f64 bandwidth (octaves), u8 1; then 32 bytes (u32 1, u32 1,
  f64 1.0, u32 0, u32 window width, u32 window height, u32 2), copied unchanged when a band list is written.
EW Spaces II state (VST3, a JUCE plugin): u32 len(state) - 16, u32 1, the processor JSON (one compact object), the
  editor JSON ({"bounds": ...}), u32 its length, "TSIU", JUCE's private data. spaces_set() edits values inside the
  processor JSON text, keeps every other byte, and fixes the first u32. In the processor JSON:
  - the IR: "impulseA" / "impulseB", the left / right halves of a true-stereo impulse; the template loads the
    rear-position impulses ("//ir/So. Cal. Orchestral Hall/S-S/S. Cal. Hall Strings L Rear N" and "... R Rear N"; the
    brass return pairs "S. Cal. Hall Horns L Rear N" with "S. Cal. Hall Brass R Rear N", San Francisco Hall "RL"/"RR").
    "selectedPreset" (presetName, fileName, path, folderImage) only labels the GUI. The impulse names of every installed
    preset are in /Library/Application Support/East West/EW Spaces II/Presets/**/*.preset (JSON).
  - "trueStereo": true (the four-channel impulse), "stereo": false, "width": 1.0.
  - pre-delay: "delay" in seconds (strings 0.0196, winds 0.018496, brass and perc 0.0100).
  - wet and dry: "wet" (linear: 1.0000002 strings, 1.0043690 brass and perc, 0.9827572 winds) and "dry" 1e-6, so the
    return is 100 % wet; "inGain" 1.0.
  - the IR envelope "irSetup" {class ConvolutionSetup, envelopeMode 0, startPos 0, endPos 1.0, ...}: the whole IR (the
    same object as Opus's ConvolutionReverb, LEARNINGS c44).
  - the input filter: "filterActive" false, "lowFilterFreq"/"lowCutFreq" 30, "highFilterFreq"/"highCutFreq" 18000.
ReaVerbate state (ALGO GLUE): 0xDEADBEEF, 0xDEADF00D, then 8 floats 0.500 1.000 0.951 0.500 1.000 0.000 0.240 0.001.
  Which float is which slider is not decoded here (check Wet / Dry in REAPER: if Dry is up, the glue return also adds
  the dry signal at its send level).

CLI (offline checks): python3 tools/template_mix.py check [CHUNK_DIR] [ho-mix-fx.json]
  decodes every chunk, compares the ReaEQ bands and the Spaces II JSON with ho-mix-fx.json, and round-trips the encoders.
"""
import base64, json, math, os, re, struct, sys

CHUNK_DIR = "/Users/gooby/sandbox/claude_composes/symphony/mockup-research/ew-template-2026-11-08/ho-mix-chunks"
MAGICS = (0xFEED5EEE, 0xFEED5EEF)   # REAPER writes EF for some Cockos plugins (ReaComp, ReaVerbate); same layout
BAND_TYPES = {"lowshelf": 0, "highshelf": 1, "lowpass": 3, "highpass": 4, "notch": 6, "bandpass": 7, "bell": 8}
TYPE_NAMES = {v: k for k, v in BAND_TYPES.items()}
DEFAULT_BW = {"highpass": 2.0, "lowpass": 2.0}   # ReaEQ's own defaults (as in every template chunk); 1.39 otherwise
SPACES_ADD = "VST3: EW Spaces II (East West)"


# ------------------------------------------------------------------------------------------------ chunk text
def parse_blocks(text):
    """The plugin blocks of an <FXCHAIN> / <MASTERFXLIST> text, in order: dicts with "kind" (VST, JS, ...), "name" (the
    quoted name, e.g. 'VST3: EW Spaces II (East West)'), "head" (the '<VST ...' line), "lines" (the body lines) and
    "bypass" (the BYPASS line before the block)."""
    out, lines, i, bypass = [], text.split("\n"), 0, "BYPASS 0 0 0"
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("BYPASS"):
            bypass = s
        if s.startswith("<") and not s.startswith(("<FXCHAIN", "<MASTERFXLIST")):
            kind = s[1:].split(" ", 1)[0]
            m = re.match(r'<\S+ "([^"]*)"', s)
            name = m.group(1) if m else s.split()[1]
            depth, body, i = 1, [], i + 1
            while i < len(lines) and depth:
                t = lines[i].strip()
                if t.startswith("<"):
                    depth += 1
                elif t == ">":
                    depth -= 1
                if depth and t:
                    body.append(t)
                i += 1
            out.append({"kind": kind, "name": name, "head": s, "lines": body, "bypass": bypass})
            continue
        i += 1
    return out


def header_info(hdr):
    """REAPER's header run of a VST block: plugin id, pins and the size of the state run (and where that size sits)."""
    uid, magic, nin = struct.unpack_from("<III", hdr, 0)
    if magic not in MAGICS:
        raise ValueError(f"not a REAPER VST header (magic {magic:#x})")
    off = 12 + 8 * nin
    nout = struct.unpack_from("<I", hdr, off)[0]
    off += 4 + 8 * nout
    return {"uid": uid, "n_in": nin, "n_out": nout, "size": struct.unpack_from("<I", hdr, off)[0], "size_at": off}


def set_header_size(hdr, n):
    at = header_info(hdr)["size_at"]
    return hdr[:at] + struct.pack("<I", n) + hdr[at + 4:]


def vst_runs(lines):
    """(header, state, trailer) bytes of a VST block's base64 lines; checks the header's size field."""
    raw = [base64.b64decode(l) for l in lines]
    if len(raw) < 3:
        raise ValueError("a VST block needs at least three base64 lines")
    hdr, data, trailer = raw[0], b"".join(raw[1:-1]), raw[-1]
    if header_info(hdr)["size"] != len(data):
        raise ValueError(f"header size {header_info(hdr)['size']} != state run {len(data)} bytes")
    return hdr, data, trailer


def strip_reaper_header(data):
    """a state read back from REAPER, without REAPER's header if it carries one"""
    if len(data) >= 8 and struct.unpack_from("<I", data, 4)[0] in MAGICS:
        info = header_info(data)
        return data[info["size_at"] + 12:info["size_at"] + 12 + info["size"]]
    return data


def find_fx(blocks, which):
    """a block by index or by a (case-insensitive) substring of its name; exactly one must match"""
    if isinstance(which, int):
        return blocks[which]
    hits = [b for b in blocks if which.lower() in b["name"].lower()]
    if len(hits) != 1:
        raise ValueError(f"fx {which!r}: {len(hits)} matches among {[b['name'] for b in blocks]}")
    return hits[0]


def b64_lines(data, width=128):
    s = base64.b64encode(data).decode()
    return [s[i:i + width] for i in range(0, len(s), width)] or [""]


# ------------------------------------------------------------------------------------------------ ReaEQ
def reaeq_decode(data):
    ver, nb = struct.unpack_from("<II", data, 0)
    off, bands = 8, []
    for _ in range(nb):
        t, en = struct.unpack_from("<II", data, off)
        f, g, bw = struct.unpack_from("<ddd", data, off + 8)
        bands.append({"type": t, "band": TYPE_NAMES.get(t, str(t)), "enabled": bool(en), "freq_hz": f,
                      "gain_db": 20 * math.log10(g) if g > 0 else -math.inf, "gain_lin": g, "bw_oct": bw,
                      "flag": data[off + 32]})
        off += 33
    return {"version": ver, "bands": bands, "tail": data[off:]}


def reaeq_encode(bands, tail, version=0x21):
    """ReaEQ state from a band list [{"band": "bell", "hz": 456, "db": -2.2, "bw_oct": 0.75, "enabled": true}, ...]
    (band names as BAND_TYPES; db 0 and bw_oct ReaEQ's default when absent); tail = the 32 bytes after the bands of a
    template ReaEQ state."""
    out = struct.pack("<II", version, len(bands))
    for b in bands:
        t = BAND_TYPES[b["band"]] if isinstance(b["band"], str) else int(b["band"])
        bw = float(b.get("bw_oct", DEFAULT_BW.get(b["band"], 1.39)))
        out += struct.pack("<IIddd", t, 1 if b.get("enabled", True) else 0, float(b["hz"]),
                           10 ** (float(b.get("db", 0.0)) / 20.0), bw) + b"\x01"
    return out + tail


# ------------------------------------------------------------------------------------------------ Spaces II
def _json_end(b, start):
    """index after the JSON object that starts at b[start] ('{'), strings respected"""
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
    """(flag, processor JSON text, rest) of an EW Spaces II state run"""
    n0, flag = struct.unpack_from("<II", data, 0)
    if n0 != len(data) - 16:
        raise ValueError(f"Spaces state: first u32 {n0} != len - 16 ({len(data) - 16})")
    if data[8:9] != b"{":
        raise ValueError("Spaces state: no JSON at byte 8")
    end = _json_end(data, 8)
    return flag, data[8:end].decode("utf-8"), data[end:]


def spaces_json(data):
    return json.loads(spaces_split(data)[1])


def _fmt(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str):
        return json.dumps(v)
    v = float(v)
    if v.is_integer():
        return f"{v:.1f}"
    r = repr(v)
    return r if "e" not in r else f"{v:.12f}".rstrip("0")


_SCALAR = r'(?:"(?:[^"\\]|\\.)*"|-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|true|false|null)'


def spaces_set(data, changes):
    """the Spaces II state with values of the processor JSON replaced: changes {key: value}, a key being any scalar
    key of the JSON other than "class" (every other key occurs once: presetName, fileName, path, folderImage, impulseA,
    impulseB, delay, wet, dry, trueStereo, width, filterActive, lowFilterFreq, highFilterFreq, lowCutFreq, highCutFreq,
    envelopeMode, endPos, ...); a nested dict (e.g. {"irSetup": {"endPos": 0.8}}) is flattened. The text of every
    other value, the editor JSON and JUCE's data stay byte for byte."""
    flat = {}
    for k, v in changes.items():
        if k.startswith("_"):
            continue
        if isinstance(v, dict):
            flat.update({k2: v2 for k2, v2 in v.items() if not k2.startswith("_")})
        else:
            flat[k] = v
    flag, text, rest = spaces_split(data)
    for k, v in flat.items():
        if k == "class":
            raise ValueError("Spaces state: 'class' cannot be set")
        pat = re.compile(r'("' + re.escape(k) + r'":)' + _SCALAR)
        if len(pat.findall(text)) != 1:
            raise ValueError(f"Spaces state: key {k!r} occurs {len(pat.findall(text))} times")
        # mvt1 c50: a value the plugin writes as an integer literal (e.g. "envelopeMode":0) stays an integer literal
        def _rep(m_, v=v):
            old_ = m_.group(0)[len(m_.group(1)):]
            if re.fullmatch(r"-?\d+", old_) and isinstance(v, (int, float)) and not isinstance(v, bool) \
                    and float(v).is_integer():
                return m_.group(1) + str(int(v))
            return m_.group(1) + _fmt(v)
        text = pat.sub(_rep, text)
    js = json.loads(text)

    def find(o, key):
        if isinstance(o, dict):
            if key in o:
                return o[key]
            for v_ in o.values():
                r_ = find(v_, key)
                if r_ is not None:
                    return r_
        return None
    for k, v in flat.items():
        got = find(js, k)
        if (isinstance(v, (int, float)) and not isinstance(v, bool) and abs(float(got) - float(v)) > 1e-9) or \
                (not isinstance(v, (int, float)) or isinstance(v, bool)) and got != v:
            raise ValueError(f"Spaces state: {k} reads back {got!r}, wanted {v!r}")
    body = struct.pack("<II", 0, flag) + text.encode("utf-8") + rest
    return struct.pack("<I", len(body) - 16) + body[4:]


# ------------------------------------------------------------------------------------------------ returns
def chunk_dir_of(mix, mix_dir):
    d = mix.get("return_chunks_dir") or CHUNK_DIR
    return d if os.path.isabs(d) else os.path.normpath(os.path.join(mix_dir, d))


_CACHE = {}


def _blocks(path):
    if path not in _CACHE:
        _CACHE[path] = parse_blocks(open(path, encoding="utf-8").read())
    return _CACHE[path]


def kind_of(name):
    n = name.lower()
    return "reaeq" if "reaeq" in n else "spaces" if "spaces ii" in n else "reaverbate" if "reaverbate" in n else "other"


def resolve_fx(entry, chunk_dir):
    """One "fx" entry of a mix.json return (or a family EQ given as a chunk) -> {"add": the name for
    TrackFX_AddByName, "data": state bytes, "hdr", "trailer", "head", "kind", "label"}.
      {"chunk": "STRING_VERB.txt", "fx": "ReaEQ"}            the block verbatim ("fx": a name substring or an index)
      {"chunk": "PERC_VERB.txt", "fx": "Spaces", "set": {...}} a Spaces II block with processor-JSON values changed
      {"reaeq": [bands], "chunk": "STRING_VERB.txt"}          a ReaEQ written from a band list (header and the 32-byte
                                                              tail from the chunk's ReaEQ; default STRING_VERB.txt)"""
    if "reaeq" in entry:
        base = find_fx(_blocks(os.path.join(chunk_dir, entry.get("chunk", "STRING_VERB.txt"))), "ReaEQ")
        hdr, bdata, trailer = vst_runs(base["lines"])
        data = reaeq_encode(entry["reaeq"], reaeq_decode(bdata)["tail"])
        hdr = set_header_size(hdr, len(data))
        label = "ReaEQ (bands)"
    else:
        base = find_fx(_blocks(os.path.join(chunk_dir, entry["chunk"])), entry.get("fx", 0))
        hdr, data, trailer = vst_runs(base["lines"])
        label = f"{base['name']} ({entry['chunk']})"
        if entry.get("set"):
            if kind_of(base["name"]) != "spaces":
                raise ValueError(f"'set' is for EW Spaces II only, not {base['name']}")
            data = spaces_set(data, entry["set"])
            hdr = set_header_size(hdr, len(data))
            label += " set " + ",".join(sorted(k for k in entry["set"] if not k.startswith("_")))
    return {"add": base["name"], "data": data, "hdr": hdr, "trailer": trailer, "head": base["head"],
            "kind": kind_of(base["name"]), "label": label}


def resolve_return(mix, mix_dir, base, name):
    """the return track `name` (a mix.json "returns" entry `base`; name = base or base + " test") as a spec for
    returns_lua()"""
    r = mix["returns"][base]
    cd = chunk_dir_of(mix, mix_dir)
    return {"name": name, "base": base, "fader_db": float(r.get("fader_db", 0.0)), "pan": float(r.get("pan", 0.0)),
            "bypass": bool(r.get("bypass", False)), "fx": [resolve_fx(e, cd) for e in r["fx"]]}


def fxchain_text(fxs):
    """an <FXCHAIN> block (REAPER's own format) holding these FX; FXIDs left out (REAPER assigns them)"""
    L = ["<FXCHAIN", "SHOW 0", "LASTSEL 0", "DOCKED 0"]
    for f in fxs:
        L += ["BYPASS 0 0 0", f["head"]]
        L += ["  " + l for l in b64_lines(f["hdr"])] + ["  " + l for l in b64_lines(f["data"])] + \
             ["  " + l for l in b64_lines(f["trailer"])]
        L += [">", "WAK 0 0"]
    return "\n".join(L + [">"])


RETURNS_LUA = r"""
-- mvt1 c50 (tools/template_mix.py): return tracks. A missing return is added at the end of the project; an existing one
-- keeps its place and its receives, and its FX chain is rebuilt from the mix.json chunks.
local function rebuild_return(spec, method)
  local tr = R.track_by_name(spec.name)
  local created = false
  if not tr then
    tr = R.add_track(spec.name, { idx = reaper.CountTracks(0), color = R.rgb(120, 120, 120), midi_in = false })
    created = true
  end
  reaper.SetMediaTrackInfo_Value(tr, "I_RECARM", 0)
  reaper.SetMediaTrackInfo_Value(tr, "I_RECMON", 0)
  reaper.SetMediaTrackInfo_Value(tr, "B_MAINSEND", 1)
  reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 10 ^ (spec.fader_db / 20))
  reaper.SetMediaTrackInfo_Value(tr, "D_PAN", spec.pan)
  for i = reaper.TrackFX_GetCount(tr) - 1, 0, -1 do reaper.TrackFX_Delete(tr, i) end
  local out = { name = spec.name, created = created, method = method, fx = {}, log = {} }
  if method == "fxchain" then
    local ok, ch = reaper.GetTrackStateChunk(tr, "", false)
    ch = ch:gsub("\n<FXCHAIN.-\n>", "", 1)
    ch = ch:gsub("\n>%s*$", "\n" .. spec.fxchain .. "\n>\n", 1)
    out.log[#out.log + 1] = "SetTrackStateChunk " .. tostring(reaper.SetTrackStateChunk(tr, ch, false))
  else
    for _, f in ipairs(spec.fx) do
      local fx = reaper.TrackFX_AddByName(tr, f.add, false, -1)
      local ok = false
      if fx >= 0 then ok = reaper.TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", f.chunk) end
      out.log[#out.log + 1] = f.add .. " fx " .. fx .. " vst_chunk " .. tostring(ok)
    end
  end
  for i = 0, reaper.TrackFX_GetCount(tr) - 1 do
    if spec.bypass then reaper.TrackFX_SetEnabled(tr, i, false) end
    local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
    local _, st = reaper.TrackFX_GetNamedConfigParm(tr, i, "vst_chunk")
    out.fx[#out.fx + 1] = { name = nm, chunk = st, enabled = reaper.TrackFX_GetEnabled(tr, i) }
  end
  local _, idx = R.track_by_name(spec.name)
  out.idx = idx
  out.vol_db = 20 * math.log(math.max(reaper.GetMediaTrackInfo_Value(tr, "D_VOL"), 1e-9), 10)
  return out
end
"""


def lua_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def returns_lua(specs, method="vst_chunk"):
    """the Lua job that creates or rebuilds the return tracks (method "vst_chunk": TrackFX_AddByName and
    TrackFX_SetNamedConfigParm(fx, "vst_chunk", state); "fxchain": the <FXCHAIN> written into the track chunk)"""
    if method not in ("vst_chunk", "fxchain"):
        raise ValueError(f"return_load {method!r}: use vst_chunk or fxchain")
    rows = []
    for s in specs:
        fx = ",".join("{add=%s, chunk=%s}" % (lua_str(f["add"]), lua_str(base64.b64encode(f["data"]).decode()))
                      for f in s["fx"])
        chain = "[==[" + fxchain_text(s["fx"]) + "]==]"
        rows.append("{name=%s, fader_db=%r, pan=%r, bypass=%s, fx={%s}, fxchain=%s}"
                    % (lua_str(s["name"]), s["fader_db"], s["pan"], "true" if s["bypass"] else "false", fx, chain))
    return RETURNS_LUA + "\nlocal res = {}\nfor _, s in ipairs({" + ",\n".join(rows) + "}) do\n" \
        f"  res[#res + 1] = rebuild_return(s, {lua_str(method)})\nend\nreturn {{ returns = res }}\n"


def _close(a, b, tol):
    return abs(a - b) <= tol


def verify_fx(kind, want, got_b64):
    """problems (list of strings) between the state we wrote and the state REAPER reads back"""
    if not got_b64:
        return ["no vst_chunk read back"]
    try:
        got = strip_reaper_header(base64.b64decode(got_b64))
    except ValueError as e:
        return [f"read-back is not base64 ({e})"]
    if got == want:
        return []
    if kind == "reaeq":
        a, b = reaeq_decode(want)["bands"], reaeq_decode(got)["bands"]
        if len(a) != len(b):
            return [f"ReaEQ has {len(b)} bands, wrote {len(a)}"]
        bad = [f"band {i}: {y} != {x}" for i, (x, y) in enumerate(zip(a, b))
               if x["type"] != y["type"] or x["enabled"] != y["enabled"] or not _close(x["freq_hz"], y["freq_hz"], 0.01)
               or not _close(x["gain_lin"], y["gain_lin"], 1e-4) or not _close(x["bw_oct"], y["bw_oct"], 1e-3)]
        return bad
    if kind == "spaces":
        try:
            a, b = spaces_json(want), spaces_json(got)
        except ValueError:
            try:
                b = json.loads(got[got.index(b"{"):_json_end(got, got.index(b"{"))])
                a = spaces_json(want)
            except ValueError as e:
                return [f"Spaces II read-back not parsed ({e})"]
        bad = []
        for k in ("impulseA", "impulseB", "trueStereo", "filterActive"):
            if a.get(k) != b.get(k):
                bad.append(f"{k} {b.get(k)!r} != {a.get(k)!r}")
        for k in ("delay", "wet", "dry", "width", "lowCutFreq", "highCutFreq", "lowFilterFreq", "highFilterFreq"):
            if k in a and not _close(float(a[k]), float(b.get(k, -1e9)), 1e-6):
                bad.append(f"{k} {b.get(k)!r} != {a[k]!r}")
        for k, v in (a.get("irSetup") or {}).items():
            if k != "class" and not _close(float(v), float((b.get("irSetup") or {}).get(k, -1e9)), 1e-6):
                bad.append(f"irSetup.{k} {(b.get('irSetup') or {}).get(k)!r} != {v!r}")
        if a.get("selectedPreset", {}).get("presetName") != b.get("selectedPreset", {}).get("presetName"):
            bad.append(f"presetName {b.get('selectedPreset', {}).get('presetName')!r}")
        return bad
    return [f"{kind} state differs ({len(got)} bytes read back, {len(want)} written)"]


def verify_returns(res, specs):
    """problems with a returns job's result (FX count, names and the read-back states)"""
    if not res or "returns" not in res:
        return [f"no result from the returns job ({res!r})"]
    bad = []
    for r, s in zip(res["returns"], specs):
        if r.get("name") != s["name"]:
            bad.append(f"result order: {r.get('name')} != {s['name']}")
            continue
        fx = r.get("fx") or []
        if len(fx) != len(s["fx"]):
            bad.append(f"{s['name']}: {len(fx)} FX loaded, wanted {len(s['fx'])} ({r.get('log')})")
            continue
        for f_got, f_want in zip(fx, s["fx"]):
            stem = f_want["add"].split(":", 1)[-1].split("(")[0].strip().lower()
            if stem not in f_got.get("name", "").lower():
                bad.append(f"{s['name']}: FX {f_got.get('name')!r} where {f_want['add']!r} was wanted")
                continue
            bad += [f"{s['name']} {f_want['label']}: {p}" for p in verify_fx(f_want["kind"], f_want["data"], f_got.get("chunk"))]
    return bad


def returns_summary(res):
    """the returns job's result without the state strings (for the build log)"""
    if not res or "returns" not in res:
        return res
    return {"returns": [{k: (v if k != "fx" else [{"name": f.get("name"), "enabled": f.get("enabled"),
                                                  "chunk_bytes": len(f.get("chunk") or "")} for f in v])
                         for k, v in r.items()} for r in res["returns"]]}


# ------------------------------------------------------------------------------------------------ family EQ, sends
FAMILY_LUA = r"""
-- mvt1 c50 (tools/template_mix.py): the family EQ (TEMPLATE-PLAN section 3), a ReaEQ after every other FX of the track.
-- set_eq deletes every ReaEQ on a re-run (--midi-only, --mix-only) and this adds it again, so re-runs agree.
local function set_family_eq(tr, spec, eq)
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local out = { fx = fx, kind = "family " .. spec.name }
  if spec.chunk then
    out[#out + 1] = "vst_chunk " .. tostring(reaper.TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", spec.chunk))
  else
    for b = 0, 4 do
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED" .. b, "0")
      set_by_fmt(tr, fx, 3 * b + 1, 0.0)
    end
    for i, bd in ipairs(spec.bands) do
      local b = i - 1
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE" .. b, tostring(bd.type))
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED" .. b, "1")
      local s = bd.band .. " " .. set_by_fmt(tr, fx, 3 * b, bd.hz) .. " Hz"
      if bd.db then s = s .. " " .. set_by_fmt(tr, fx, 3 * b + 1, bd.db) .. " dB" end
      if bd.bw then s = s .. " bw " .. set_by_fmt(tr, fx, 3 * b + 2, bd.bw) end
      local _, ty = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDTYPE" .. b)
      out[#out + 1] = s .. " type " .. tostring(ty)
    end
  end
  eq[#eq + 1] = out
end
"""

SENDS_LUA = r"""
-- mvt1 c50 (tools/template_mix.py): post-fader sends to the return tracks. Every send of the track is removed first, so
-- re-runs agree. A send with row offsets gets a volume envelope (square steps) and D_VOL 1.
local function set_sends(tr, S, eq)
  for i = reaper.GetTrackNumSends(tr, 0) - 1, 0, -1 do reaper.RemoveTrackSend(tr, 0, i) end
  local out = { kind = "sends" }
  for _, s in ipairs(S) do
    local dest = R.track_by_name(s.dest)
    if not dest then
      out[#out + 1] = "SEND ERROR: no return track " .. s.dest
    else
      local k = reaper.CreateTrackSend(tr, dest)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "I_SENDMODE", 0)   -- post-fader (post-pan)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "D_PAN", 0)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "B_MUTE", 0)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "I_SRCCHAN", 0)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "I_DSTCHAN", 0)
      local info = ""
      if s.env then
        reaper.SetTrackSendInfo_Value(tr, 0, k, "D_VOL", 1.0)
        local env = reaper.GetTrackSendInfo_Value(tr, 0, k, "P_ENV:<VOLENV")
        local okp, valid = pcall(reaper.ValidatePtr2, 0, env, "TrackEnvelope*")
        if not (okp and valid) then
          info = " SEND ERROR: no send volume envelope (" .. tostring(env) .. ")"
        else
          reaper.DeleteEnvelopePointRange(env, -1, 1e9)
          local mode = reaper.GetEnvelopeScalingMode(env)
          for _, p in ipairs(s.env) do
            reaper.InsertEnvelopePoint(env, reaper.TimeMap2_QNToTime(0, p.qn), reaper.ScaleToEnvelopeMode(mode, 10 ^ (p.db / 20)), 1, 0, false, true)
          end
          reaper.Envelope_SortPoints(env)
          -- scherzo c06: activate after the points are in (set before them, REAPER read back "ACT 0 -1" on a new send
          -- envelope and the build stopped)
          local ok, ch = reaper.GetEnvelopeStateChunk(env, "", false)
          if ok then
            ch = ch:gsub("\nACT 0", "\nACT 1"):gsub("\nVIS 0", "\nVIS 1")
            reaper.SetEnvelopeStateChunk(env, ch, false)
          end
          local _, ch2 = reaper.GetEnvelopeStateChunk(env, "", false)
          info = " envelope points " .. reaper.CountEnvelopePoints(env) .. (ch2:find("\nACT 1") and " active" or " SEND ERROR: envelope not active")
        end
      else
        reaper.SetTrackSendInfo_Value(tr, 0, k, "D_VOL", 10 ^ (s.db / 20))
      end
      local v = reaper.GetTrackSendInfo_Value(tr, 0, k, "D_VOL")
      out[#out + 1] = string.format("%s %.2f dB mode %d", s.dest, 20 * math.log(math.max(v, 1e-9), 10),
                                    reaper.GetTrackSendInfo_Value(tr, 0, k, "I_SENDMODE")) .. info
    end
  end
  eq[#eq + 1] = out
end
"""


def family_spec(name, entry, mix, mix_dir):
    """a mix.json "family_eqs" entry as a Lua table: a band list (set with build_reaper's set_by_fmt, as the per-track EQ)
    or {"chunk": file, "fx": "ReaEQ"} (the template's own ReaEQ state, loaded with vst_chunk)"""
    if isinstance(entry, dict):
        if "chunk" not in entry:
            entry = entry["bands"]
        else:
            f = resolve_fx(entry, chunk_dir_of(mix, mix_dir))
            if f["kind"] != "reaeq":
                raise ValueError(f"family EQ {name}: {f['add']} is not a ReaEQ")
            return "{name=%s, chunk=%s}" % (lua_str(name), lua_str(base64.b64encode(f["data"]).decode()))
    if len(entry) > 5:
        raise ValueError(f"family EQ {name}: {len(entry)} bands (ReaEQ's default instance has 5)")
    rows = []
    for b in entry:
        if b["band"] not in BAND_TYPES:
            raise ValueError(f"family EQ {name}: band type {b['band']!r} (use {sorted(BAND_TYPES)})")
        bw = b.get("bw_oct")
        rows.append("{band=%s, type=%d, hz=%r%s%s}" % (lua_str(b["band"]), BAND_TYPES[b["band"]], float(b["hz"]),
                                                     ", db=%r" % float(b["db"]) if "db" in b else "",
                                                     ", bw=%r" % float(bw) if bw is not None else ""))
    return "{name=%s, bands={%s}}" % (lua_str(name), ",".join(rows))


def sends_table(sends):
    rows = []
    for s in sends:
        env = ""
        if s.get("env"):
            env = ", env={" + ",".join("{qn=%r, db=%r}" % (p["qn"], p["db"]) for p in s["env"]) + "}"
        rows.append("{dest=%s, db=%r%s}" % (lua_str(s["dest"]), s["db"], env))
    return "{" + ",".join(rows) + "}"


# ------------------------------------------------------------------------------------------------ offline check
def check(chunk_dir=CHUNK_DIR, fx_json=None):
    fx_json = fx_json or os.path.join(os.path.dirname(chunk_dir), "ho-mix-fx.json")
    ref = json.load(open(fx_json))
    files = {"MASTER": "MASTER.txt", "STRINGS": "STRINGS.txt", "BRASS": "BRASS.txt", "WOODWINDS": "WOODWINDS.txt",
             "Harp KS Master": "Harp_KS_Master.txt", "ORCHESTRAL PERC": "ORCHESTRAL_PERC.txt",
             "Timpani Flt KS": "Timpani_Flt_KS.txt", "STRING VERB": "STRING_VERB.txt", "BRASS VERB": "BRASS_VERB.txt",
             "WW VERB": "WW_VERB.txt", "PERC VERB": "PERC_VERB.txt", "CHOIR VERB": "CHOIR_VERB.txt",
             "LONG VERB": "LONG_VERB.txt", "ALGO GLUE": "ALGO_GLUE.txt", "DELAY": "DELAY.txt"}
    n_ok = n_bad = 0
    for track, fn in files.items():
        blocks = [b for b in _blocks(os.path.join(chunk_dir, fn)) if "Opus" not in b["name"]]
        rfx = [f for f in ref[track]["fx"] if "Opus" not in f["fx"]]
        if [b["name"] for b in blocks] != [f["fx"] for f in rfx]:
            print(f"BAD {track}: FX {[b['name'] for b in blocks]} != {[f['fx'] for f in rfx]}")
            n_bad += 1
            continue
        for b, f in zip(blocks, rfx):
            if b["lines"] != f["chunk_base64_lines"]:
                print(f"BAD {track} {b['name']}: base64 lines differ from ho-mix-fx.json")
                n_bad += 1
                continue
            hdr, data, trailer = vst_runs(b["lines"])
            k = kind_of(b["name"])
            msg = []
            if k == "reaeq":
                dec = reaeq_decode(data)
                for x, y in zip(dec["bands"], f["decoded_bands"]):
                    if x["type"] != y["type"] or x["enabled"] != y["enabled"] or abs(x["freq_hz"] - y["freq_hz"]) > 0.01 \
                            or abs(x["gain_db"] - y["gain_db"]) > 0.051 or abs(x["bw_oct"] - y["bw_oct"]) > 0.0011:
                        msg.append(f"band {x} != {y}")
                if len(dec["bands"]) != len(f["decoded_bands"]):
                    msg.append("band count")
                again = reaeq_encode([{"band": x["type"], "hz": x["freq_hz"], "db": x["gain_db"] if x["gain_lin"] > 0 else 0,
                                       "bw_oct": x["bw_oct"], "enabled": x["enabled"]} for x in dec["bands"]], dec["tail"],
                                     dec["version"])
                re_dec = reaeq_decode(again)
                if any(abs(p["gain_lin"] - q["gain_lin"]) > 1e-12 or p["freq_hz"] != q["freq_hz"] or p["bw_oct"] != q["bw_oct"]
                       or p["type"] != q["type"] for p, q in zip(re_dec["bands"], dec["bands"])) or re_dec["tail"] != dec["tail"]:
                    msg.append("encode round trip")
                desc = "; ".join(f"{x['band']} {x['freq_hz']:g} Hz {x['gain_db']:+.2f} dB bw {x['bw_oct']:g}"
                                 + ("" if x["enabled"] else " (off)") for x in dec["bands"])
            elif k == "spaces":
                js = spaces_json(data)
                if js != f["decoded_state"]:
                    msg.append("Spaces JSON differs from decoded_state")
                if spaces_set(data, {}) != data:
                    msg.append("Spaces rebuild round trip")
                d2 = spaces_set(data, {"delay": 0.0123, "irSetup": {"endPos": 0.8}})
                if spaces_json(d2) != dict(js, delay=0.0123, irSetup=dict(js["irSetup"], endPos=0.8)) \
                        or spaces_split(d2)[2] != spaces_split(data)[2] or len(d2) - 16 != struct.unpack_from("<I", d2, 0)[0]:
                    msg.append("Spaces set: other values or the rest changed")
                d3 = spaces_set(d2, {"delay": js["delay"], "irSetup": {"endPos": js["irSetup"]["endPos"]}})
                if spaces_json(d3) != js or spaces_split(d3)[2] != spaces_split(data)[2]:
                    msg.append("Spaces set/unset round trip")
                desc = (f"{js['selectedPreset']['presetName']}: A {js['impulseA']} | B {js['impulseB']}; delay "
                        f"{js['delay'] * 1000:.2f} ms, wet {js['wet']:.6f}, dry {js['dry']:g}, trueStereo {js['trueStereo']}, "
                        f"irSetup endPos {js['irSetup']['endPos']} mode {js['irSetup']['envelopeMode']}, filter {js['filterActive']}")
            elif k == "reaverbate":
                desc = "floats " + " ".join(f"{v:.3f}" for v in struct.unpack_from("<8f", data, 8))
            else:
                desc = f"{len(data)} bytes"
            if msg:
                n_bad += 1
                print(f"BAD {track} {b['name']}: " + "; ".join(msg))
            else:
                n_ok += 1
                print(f"ok  {track:16s} {b['name']:32s} {desc}")
    print(f"{n_ok} FX states decoded and matched, {n_bad} problems")
    return n_bad


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        sys.exit(1 if check(*(sys.argv[2:4])) else 0)
    print(__doc__)

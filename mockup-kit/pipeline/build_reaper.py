"""Build the movement II mockup in a running REAPER through the file bridge (~/.rpr-bridge).

Usage: python build_reaper.py <parts.json> <jobs-dir> [--mix-only] [track names...]
  c02: each track also gets a volume envelope (mix.json gain_db + parts.json vol_db + mix.json
  dyn_trim_db/soft_trim_db; D_VOL stays at 0 dB, since REAPER ignores it under an envelope), and the patch
  state loads every articulation the track uses (KS Masters load only their first rows by default).
  With no track names: sets the tempo map and builds every track.
  Mix settings come from mix.json next to parts.json (track gain, stereo seat/width, Opus mics, reverb).
  --mix-only: only set track volume, pan, the volume envelope and the ReaEQ (c04) on the existing tracks (no patch reload).
  c05: seats and widths live in the Opus state (mic channel panLeft/panRight), so a seat, width, mic or reverb change
  needs a full rebuild of the track; --mix-only keeps REAPER's pan at centre / width 1.
Patches are loaded by writing Opus's own plugin state (the .oib instrument JSON inside a
Performance zone) with TrackFX_SetNamedConfigParm(..., "vst_chunk", ...).
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import opus_state

PARTS, JOBS = sys.argv[1], sys.argv[2]
MIX_ONLY = "--mix-only" in sys.argv[3:]
ONLY = set(a for a in sys.argv[3:] if a != "--mix-only")
os.makedirs(JOBS, exist_ok=True)
RPR = ["python3", os.path.expanduser("~/.rpr-bridge/rpr.py")]
d = json.load(open(PARTS))
MIX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")))


def mix_for(name):
    t = dict(MIX["tracks"][name])
    g = MIX["groups"][t["group"]]
    for k, v in g.items():
        t.setdefault(k, v)
    return t

COLORS = {"wind": (90, 160, 90), "brass": (210, 170, 60), "timp": (150, 110, 80), "harp": (170, 120, 200), "harm": (170, 120, 200), "string": (70, 110, 200)}


def run(path, timeout=300):
    out = subprocess.run(RPR + ["run", path, "--timeout", str(timeout)], capture_output=True, text=True)
    if out.returncode:
        sys.exit(f"job {path} failed:\n{out.stderr}\n{out.stdout}")
    return json.loads(out.stdout) if out.stdout.strip() else None


def lua_list(rows, keys):
    return "{" + ",".join("{" + ",".join(f"{k}={r[k] if isinstance(r, dict) else r[i]}" for i, k in enumerate(keys)) + "}" for r in rows) + "}"


def tempo_job():
    # absolute seconds for each tempo change (tempo is constant between changes)
    pts, t, last_q, last_bpm = [], 0.0, 0.0, None
    sig = {q: (n, dd) for q, n, dd in d["timesig"]}
    for q, bpm in d["tempo"]:
        if last_bpm is not None:
            t += (q - last_q) * 60.0 / last_bpm
        n, dd = sig.get(q, (0, 0))
        pts.append({"t": round(t, 6), "bpm": bpm, "num": n, "den": dd, "qn": q})
        last_q, last_bpm = q, bpm
    lua = f"""
reaper.SetCurrentBPM(0, {pts[0]['bpm']}, false)
for i = reaper.CountTempoTimeSigMarkers(0) - 1, 0, -1 do reaper.DeleteTempoTimeSigMarker(0, i) end
local P = {lua_list(pts, ['t', 'bpm', 'num', 'den', 'qn'])}
for _, p in ipairs(P) do
  reaper.SetTempoTimeSigMarker(0, -1, p.t, -1, -1, p.bpm, p.num, p.den, false)
end
reaper.UpdateTimeline()
local bad = {{}}
for _, p in ipairs(P) do
  local q = reaper.TimeMap2_timeToQN(0, p.t)
  if math.abs(q - p.qn) > 1e-3 then bad[#bad + 1] = {{want = p.qn, got = q}} end
end
reaper.GetSetProjectInfo(0, "PROJECT_SRATE", 48000, true)
reaper.GetSetProjectInfo(0, "PROJECT_SRATE_USE", 1, true)
return {{ markers = reaper.CountTempoTimeSigMarkers(0), mismatches = bad,
         end_sec = reaper.TimeMap2_QNToTime(0, {d['end_qn']}) }}
"""
    p = f"{JOBS}/00_tempo.lua"
    open(p, "w").write(lua)
    return run(p)


_REVERB = None


def shared_reverb():
    """The reverb channel (fx:0) of reverb.from_patch: one hall for every track (c01)."""
    global _REVERB
    if _REVERB is None:
        src = opus_state.load_oib(MIX["reverb"]["from_patch"])
        ch = next(c for c in src["mixer"]["channels"] if c["channelId"] == "fx:0")
        _REVERB = [i for i in ch["inserts"] if i["class"] == "ConvolutionReverb"][0]
    return json.loads(json.dumps(_REVERB))


def apply_mix(inst, m):
    chans = inst["mixer"]["channels"]
    subs = {c["label"]: c for c in chans if c["channelId"].startswith("sub:")}
    cols = {c["name"]: c for c in inst["layerMatrix"]["columns"]}
    if m.get("mics") is not None:
        for label, c in subs.items():
            on = label in m["mics"]
            c["loaded"] = on
            if label in cols:
                cols[label]["loaded"] = on
            if on:
                c["volume"] = m["mics"][label]
    # c05 (C #3): the seat and width are set inside Opus on every mic channel (panLeft/panRight), so the shared hall
    # (fx:0) returns centred at full width instead of being panned and narrowed with the dry sound by the REAPER pan
    # after the plugin. The REAPER track pan is centre, width 1.
    for c in subs.values():
        c["pan"] = 0.0
        c["panLeft"] = max(-1.0, m["seat"] - m["width"])
        c["panRight"] = min(1.0, m["seat"] + m["width"])
        for ins in c["inserts"]:
            if ins["class"] == "SendProcessor" and ins.get("output") == "fx:0":
                ins["level"] = m["send"]
    fx = next(c for c in chans if c["channelId"] == "fx:0")
    fx["volume"] = MIX["reverb"]["fx_volume"]
    fx["pan"], fx["panLeft"], fx["panRight"] = 0.0, -1.0, 1.0
    rv = shared_reverb()
    rv["wet"] = MIX["reverb"]["wet"]
    fx["inserts"] = [i for i in fx["inserts"] if i["class"] != "ConvolutionReverb"] + [rv]


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def load_articulations(inst, used):
    """c02: a KS Master loads only its first rows (six in the string patches); a keyswitch to an unloaded articulation
    is ignored. Load and enable every articulation the track uses, and give its trigger a key (as the loaded rows have)."""
    want = {a.lower() for a in used if a}
    for row in inst["layerMatrix"]["rows"]:
        if row["name"].lower() in want:
            row["loaded"] = True
            row["active"] = True
    for trig in inst.get("articulations", {}).get("trigger", []):
        if trig["name"].lower() in want and not trig.get("useKey"):
            trig["useKey"] = True
            trig["triggerName"] = NOTE_NAMES[trig["key"] % 12] + str(trig["key"] // 12 - 2)
    if any("leg" in a for a in want):
        # c02: as in the dedicated Leg Slur MAX patches: velocity sets the legato transition's start offset
        for f in inst.get("filters", []):
            if f.get("name") == "EWSO":
                f["legato_speed_active"] = True
            if f.get("name") == "RTKiller":
                f["active"] = True


def state_for(tr):
    inst = opus_state.load_oib(tr["patch"])
    if "articulations" in inst:
        load_articulations(inst, list(tr["art_counts"]) + [tr["first_art"]])
    if tr["first_ks"] is not None and "articulations" in inst:
        inst["articulations"]["currentKeySwitch"] = tr["first_ks"]
    for f in inst.get("filters", []):
        if f.get("name") == "ConSordino" and tr["cc15"]:
            f["conSordino"] = tr["cc15"][0][1] >= 64
    apply_mix(inst, mix_for(tr["name"]))
    _, perf, _ = opus_state.split(opus_state.TEMPLATE)
    perf["name"] = tr["name"]
    perf["zones"] = [{"class": "InstrumentZone", "keyMin": 0, "keyMax": 127, "velMin": 1, "velMax": 127,
                      "octave": 0, "groupIndex": 0, "instrument": inst}]
    return opus_state.build(perf)


def step_at(pts, q, default=0.0):
    v = default
    for pq, pv in pts:
        if pq <= q + 1e-6:
            v = pv
        else:
            break
    return v


def vol_points(tr):
    """c02: the track volume envelope in dB: parts.json vol_db (roles, note trims, timpani settle, final fade) plus the
    mix.json dynamic trims read from the printed dynamic curve. Both are step lanes on a 0.125 qn grid."""
    m = mix_for(tr["name"])
    dt = m.get("dyn_trim_db", {"f": 0, "ff": 0})
    st = MIX.get("soft_trim_db", {})
    soft = {} if tr["name"] in st.get("_except", []) else st
    soft = m.get("soft_trim_db", soft)   # c03: per-track override (Violas pp 0)
    tbl = [(22, soft.get("ppp", 0)), (34, soft.get("pp", 0)), (46, 0.0), (88, dt["f"]), (114, dt["ff"]), (127, dt["ff"])]

    def trim(cc):
        if cc <= tbl[0][0]:
            return tbl[0][1]
        for (c0, d0), (c1, d1) in zip(tbl, tbl[1:]):
            if c0 <= cc <= c1:
                return d0 + (d1 - d0) * (cc - c0) / (c1 - c0)
        return tbl[-1][1]
    dyn = tr.get("dyn_curve", [])
    vol = tr.get("vol_db", [])
    first = dyn[0][1] if dyn else 46
    grid = [i * 0.125 for i in range(int((d["end_qn"] + 6) / 0.125))]
    g = m["gain_db"]   # c02: with a volume envelope REAPER ignores D_VOL (measured: every gain was lost), so the gain goes in here
    vals = [round(g + step_at(vol, q) + (trim(step_at(dyn, q, first)) if dyn else 0.0), 2) for q in grid]
    out = []
    for k, (q, v) in enumerate(zip(grid, vals)):
        if k == 0 or k == len(vals) - 1 or v != vals[k - 1] or v != vals[k + 1]:
            out.append({"qn": q, "db": v})
    return out


ENV_LUA = """
local function set_vol_env(tr, V)
  reaper.SetOnlyTrackSelected(tr)
  local env = reaper.GetTrackEnvelopeByName(tr, "Volume")
  if not env then reaper.Main_OnCommand(40406, 0); env = reaper.GetTrackEnvelopeByName(tr, "Volume") end
  if not env then return false end
  local ok, ch = reaper.GetEnvelopeStateChunk(env, "", false)
  if ok and ch:find("ACT 0") then reaper.SetEnvelopeStateChunk(env, (ch:gsub("ACT 0", "ACT 1")), false) end
  reaper.DeleteEnvelopePointRange(env, -1, 1e9)
  local mode = reaper.GetEnvelopeScalingMode(env)
  for _, p in ipairs(V) do
    reaper.InsertEnvelopePoint(env, reaper.TimeMap2_QNToTime(0, p.qn), reaper.ScaleToEnvelopeMode(mode, 10 ^ (p.db / 20)), 0, 0, false, true)
  end
  reaper.Envelope_SortPoints(env)
  reaper.SetTrackSelected(tr, false)
  reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 1.0)
  return reaper.CountEnvelopePoints(env)
end

-- c04: ReaEQ after Opus from mix.json "eq" (B #2, C #4). Parameters are set by searching the normalized value whose
-- displayed value matches the target (ReaEQ's scales are not linear). Band 0 = low shelf, band 1 = bell.
local function set_by_fmt(tr, fx, p, target)
  local lo, hi = 0.0, 1.0
  for _ = 1, 40 do
    local mid = (lo + hi) / 2
    reaper.TrackFX_SetParamNormalized(tr, fx, p, mid)
    local _, s = reaper.TrackFX_GetFormattedParamValue(tr, fx, p, "")
    local v = tonumber((s or ""):match("[-%d%.]+")) or -1e9
    if v < target then lo = mid else hi = mid end
  end
  reaper.TrackFX_SetParamNormalized(tr, fx, p, (lo + hi) / 2)
  local _, s = reaper.TrackFX_GetFormattedParamValue(tr, fx, p, "")
  return s
end
local function set_eq(tr, bands)
  for i = reaper.TrackFX_GetCount(tr) - 1, 1, -1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
    if nm:find("ReaEQ") then reaper.TrackFX_Delete(tr, i) end
  end
  if #bands == 0 then return {} end
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local out = {fx = fx}
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE0", "0")
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE1", "8")
  for b = 0, 4 do set_by_fmt(tr, fx, 3 * b + 1, 0.0) end
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED4", "0")
  for _, bd in ipairs(bands) do
    if bd.band == "highpass" then   -- c05 (C #2): band 4 is ReaEQ's high pass (type 4)
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE4", "4")
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED4", "1")
      out[#out + 1] = "highpass " .. set_by_fmt(tr, fx, 12, bd.hz) .. " Hz"
    else
      local b = bd.band == "lowshelf" and 0 or 1
      out[#out + 1] = set_by_fmt(tr, fx, 3 * b, bd.hz) .. " Hz " .. set_by_fmt(tr, fx, 3 * b + 1, bd.db) .. " dB"
      if bd.bw then out[#out] = out[#out] .. " bw " .. set_by_fmt(tr, fx, 3 * b + 2, bd.bw) end
    end
  end
  for b = 0, 4 do
    local _, en = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDENABLED" .. b)
    local _, ty = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDTYPE" .. b)
    local _, g = reaper.TrackFX_GetFormattedParamValue(tr, fx, 3 * b + 1, "")
    out[#out + 1] = "band" .. b .. " type " .. tostring(ty) .. " on " .. tostring(en) .. " gain " .. g
  end
  return out
end
"""


def eq_lua(m):
    """c04: mix.json eq bands as a Lua table."""
    rows = []
    for b in m.get("eq", []):
        bw = f', bw={b["bw_oct"]}' if "bw_oct" in b else ""
        rows.append(f'{{band="{b["band"]}", hz={b["hz"]}, db={b.get("db", 0)}{bw}}}')
    return "{" + ",".join(rows) + "}"


def track_job(i, tr):
    b64file = f"{JOBS}/{i:02d}_{tr['stem'].replace(' ', '_')}.b64"
    m = mix_for(tr["name"])
    open(b64file, "w").write(state_for(tr))   # always regenerated: mix.json changes the state
    r, g, b = COLORS[tr["family"]]
    notes = lua_list(tr["notes"], ["qn", "dur", "pitch", "vel"])
    ks = lua_list(tr["ks"], ["qn", "pitch"])
    ccs = []
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, tr.get("cc7", [])), (70, tr.get("cc70", []))):
        ccs += [{"qn": q, "cc": num, "v": v} for q, v in lane]
    ccs = lua_list(ccs, ["qn", "cc", "v"])
    vpts = lua_list(vol_points(tr), ["qn", "db"])
    lua = ENV_LUA + f"""
local name = {json.dumps(tr['name'])}
local old = R.track_by_name(name)
if old then reaper.DeleteTrack(old) end
local tr = R.add_track(name, {{ idx = math.min({i}, reaper.CountTracks(0)), instrument = "VST3i: Opus (East West)", color = R.rgb({r}, {g}, {b}) }})
reaper.SetMediaTrackInfo_Value(tr, "I_PANMODE", 5)
reaper.SetMediaTrackInfo_Value(tr, "D_PAN", 0)     -- c05: the seat is set inside Opus (apply_mix)
reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", 1)
reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 1.0)   -- c02: the gain is in the volume envelope
reaper.SetMediaTrackInfo_Value(tr, "I_RECARM", 0); reaper.SetMediaTrackInfo_Value(tr, "I_RECMON", 0)
local f = assert(io.open({json.dumps(os.path.abspath(b64file))}, "rb")); local st = f:read("a"); f:close()
local okset = reaper.TrackFX_SetNamedConfigParm(tr, 0, "vst_chunk", st)
local endqn = {d['end_qn'] + 6}
local item = reaper.CreateNewMIDIItemInProj(tr, 0, endqn, true)
local take = reaper.GetActiveTake(item)
reaper.GetSetMediaItemTakeInfo_String(take, "P_NAME", name .. " (mvt II v77)", true)
local ppq = function(q) return reaper.MIDI_GetPPQPosFromProjQN(take, q) end
for _, n in ipairs({notes}) do
  reaper.MIDI_InsertNote(take, false, false, ppq(n.qn), ppq(n.qn + n.dur), 0, n.pitch, n.vel, true)
end
for _, k in ipairs({ks}) do
  reaper.MIDI_InsertNote(take, false, false, ppq(k.qn), ppq(k.qn + 0.03), 0, k.pitch, 1, true)
end
for _, c in ipairs({ccs}) do
  reaper.MIDI_InsertCC(take, false, false, ppq(c.qn), 0xB0, 0, c.cc, c.v)
end
reaper.MIDI_Sort(take)
local _, nn, nc = reaper.MIDI_CountEvts(take)
local okget, back = reaper.TrackFX_GetNamedConfigParm(tr, 0, "vst_chunk")
local envn = set_vol_env(tr, {vpts})
local eq = set_eq(tr, {eq_lua(m)})
return {{ track = name, okset = okset, notes = nn, ccs = nc, state_len = #back, env_points = envn, eq = eq }}
"""
    p = f"{JOBS}/{i:02d}_{tr['name'].replace(' ', '_')}.lua"
    open(p, "w").write(lua)
    return run(p, timeout=600)


def mix_job():
    rows = []
    for tr in d["tracks"]:
        if ONLY and tr["name"] not in ONLY:
            continue
        m = mix_for(tr["name"])
        rows.append(f'{{n={json.dumps(tr["name"])}, pan=0, w=1, vol={10 ** (m["gain_db"] / 20):.6f}, env={lua_list(vol_points(tr), ["qn", "db"])}, eq={eq_lua(m)}}}')
    lua = ENV_LUA + f"""
local done = {{}}
for _, r in ipairs({{{",".join(rows)}}}) do
  local tr = R.track_by_name(r.n)
  if tr then
    reaper.SetMediaTrackInfo_Value(tr, "I_PANMODE", 5)
    reaper.SetMediaTrackInfo_Value(tr, "D_PAN", r.pan)
    reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", r.w)
    set_vol_env(tr, r.env)
    local eq = set_eq(tr, r.eq)
    done[#done + 1] = r.n
    if #eq > 0 then done[#done + 1] = eq end
  end
end
return {{ set = done }}
"""
    p = f"{JOBS}/95_mix.lua"
    open(p, "w").write(lua)
    return run(p)


if MIX_ONLY:
    print(json.dumps(mix_job()))
    sys.exit(0)
if not ONLY:
    print(json.dumps(tempo_job()))
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY:
        continue
    res = track_job(i, tr)
    print(json.dumps(res), flush=True)

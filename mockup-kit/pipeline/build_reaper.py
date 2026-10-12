"""Build the movement II mockup in a running REAPER through the file bridge (~/.rpr-bridge).

Usage: python build_reaper.py <parts.json> <jobs-dir> [--mix-only] [track names...]
  c02: each track also gets a volume envelope (mix.json gain_db + parts.json vol_db + mix.json
  dyn_trim_db/soft_trim_db; D_VOL stays at 0 dB, since REAPER ignores it under an envelope), and the patch
  state loads every articulation the track uses (KS Masters load only their first rows by default).
  With no track names: sets the tempo map and builds every track.
  Mix settings come from mix.json next to parts.json (track gain, stereo seat/width, Opus mics, reverb).
  --midi-only (c07): replace each track's MIDI item, volume envelope and ReaEQ without reloading its Opus patch, when
  its Opus state is unchanged since the last full build (jobs/NN_*.b64); a track whose state changed is fully rebuilt.
  The tempo map is not rewritten (rebuild everything after a tempo-map change), unless --tempo is given (c08): then the
  tempo map is written first and every listed track's items are recreated on it.
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
MIDI_ONLY = "--midi-only" in sys.argv[3:]   # c07: see midi_job
TEMPO = "--tempo" in sys.argv[3:]   # c08: with --midi-only, rewrite the tempo map first
ONLY = set(a for a in sys.argv[3:] if a not in ("--mix-only", "--midi-only", "--tempo"))
os.makedirs(JOBS, exist_ok=True)
RPR = ["python3", os.path.expanduser("~/.rpr-bridge/rpr.py")]
d = json.load(open(PARTS))
# c06 (A #1): every event is written PRE qn later than its parts.json (score) position; the pre-roll bar is silent except
# for each track's first keyswitch and first controller values at qn 0.25. render_cycle.py cuts the pre-roll off.
PRE = d.get("preroll_qn", 0.0)
PRE_BPM = d.get("preroll_bpm", 60.0)
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
    if PRE:
        pts.append({"t": 0.0, "bpm": PRE_BPM, "num": sig.get(0.0, (3, 4))[0], "den": sig.get(0.0, (3, 4))[1], "qn": 0.0})
        t = PRE * 60.0 / PRE_BPM
    for q, bpm in d["tempo"]:
        if last_bpm is not None:
            t += (q - last_q) * 60.0 / last_bpm
        n, dd = sig.get(q, (0, 0))
        pts.append({"t": round(t, 6), "bpm": bpm, "num": n, "den": dd, "qn": q + PRE})
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
         end_sec = reaper.TimeMap2_QNToTime(0, {d['end_qn'] + PRE}), preroll_sec = reaper.TimeMap2_QNToTime(0, {PRE}) }}
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
                if MIX["reverb"].get("send_pre_fader"):
                    # c09 (C #2): the send was post-fader, so the hall got each mic channel's panned signal and returned
                    # it at the seat. Pre-fader (Opus manual pp. 106-107) it is taken before the channel fader and pan;
                    # the level is scaled by the channel volume so the reverb input stays as before
                    ins["post"] = False
                    ins["level"] = round(m["send"] * c["volume"], 4)
    # c13 (C #1): the main (Master) channel pans after the reverb return is mixed in; the DIV A patches ship it panned
    # (1st Violins DIV A -0.74, Celli DIV A +0.33), which put the solo violin and its hall at the left wall. Centre it.
    main = next((c for c in chans if c["channelId"] == "main"), None)
    if main is not None:
        main["pan"], main["panLeft"], main["panRight"] = 0.0, -1.0, 1.0
    fx = next(c for c in chans if c["channelId"] == "fx:0")
    fx["volume"] = MIX["reverb"]["fx_volume"]
    fx["pan"], fx["panLeft"], fx["panRight"] = 0.0, -1.0, 1.0
    rv = shared_reverb()
    rv["wet"] = MIX["reverb"]["wet"]
    if MIX["reverb"].get("impulse"):
        # c17 (C #1): a true-stereo hall IR (the one HO's own percussion patches ship, e.g. Timpani Flt KS): a stereo IR
        # convolves L with L and R with R, so each seat's hall tail stayed at its seat (Vln I tail R-L -8.1 dB)
        rv["impulseA"] = MIX["reverb"]["impulse"]
        rv["trueStereo"] = bool(MIX["reverb"].get("true_stereo"))
    if MIX["reverb"].get("high_cut_hz"):
        # c09 (C #4): Bandpass on, high cut on the hall only (manual p. 133; a hall's tail darkens). The state carries two
        # key pairs (highFilterFreq / highCutFreq); both are set
        rv["filterActive"] = True
        rv["highFilterFreq"] = rv["highCutFreq"] = float(MIX["reverb"]["high_cut_hz"])
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


TAIL_HOLD_MIN_S, TAIL_HOLD_LEAD_S, TAIL_HOLD_STOP_QN = 0.5, 0.35, 303.5   # c17 (C #2), see vol_points


def q2s(q):
    """score qn -> seconds from score qn 0 on the parts.json tempo map (steps; the 0.25 qn ramps are close enough here)"""
    t, lq, lb = 0.0, 0.0, d["tempo"][0][1]
    for tq, b in d["tempo"]:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb
        lq, lb = tq, b
    return t + (q - lq) * 60 / lb


def s2q(t):
    lo, hi = 0.0, d["end_qn"] + 8
    for _ in range(50):
        mid = (lo + hi) / 2
        if q2s(mid) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


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
    # c06 (B #2): a "p" anchor at CC 46 (0 when absent, as before)
    tbl = [(22, soft.get("ppp", 0)), (34, soft.get("pp", 0)), (46, soft.get("p", 0)), (88, dt["f"]), (114, dt["ff"]), (127, dt["ff"])]

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
    grid = [i * 0.125 for i in range(int((d["end_qn"] + 6) / 0.125))]   # score qn
    # c10: exact breakpoints of fast vol_db shapes (parts.json vol_bp), between the grid points
    grid = sorted(set(grid) | {q for q in tr.get("vol_bp", []) if 0 <= q < grid[-1]})
    g = m["gain_db"]   # c02: with a volume envelope REAPER ignores D_VOL (measured: every gain was lost), so the gain goes in here
    val_at = lambda q: round(g + step_at(vol, q) + (trim(step_at(dyn, q, first)) if dyn else 0.0), 2)
    vals = [val_at(q) for q in grid]
    # c17 (C #2): tail hold. The hall is inside Opus, before this envelope, so a level change while the track rests acts on
    # its last note's decaying tail (cuts of 6-8 dB, swells of 5-8 dB measured). In every rest of TAIL_HOLD_MIN_S or more
    # (from the end of the sounding notes e to the next moved onset n) the envelope holds its value just before e until
    # TAIL_HOLD_LEAD_S before n; the final fade (qn TAIL_HOLD_STOP_QN on) is left alone. Note bodies do not change.
    if tr.get("notes") and m.get("tail_hold", MIX.get("tail_hold", True)):
        segs = sorted((n["qn"], n["qn"] + n["dur"]) for n in tr["notes"])
        rests, ce = [], segs[0][1]
        for a_, b_ in segs[1:]:
            if a_ > ce + 1e-6:
                rests.append((ce, a_))
            ce = max(ce, b_)
        # c19 (C #5): the rest after the track's last note (to the end of the project) holds too, so roles and the final
        # fade that end later no longer move the last hall tail (Cb tail rose 5-6 dB after the final release; the tuba's
        # bar 63 tail fell 16 dB in 0.3 s)
        rests.append((ce, grid[-1] + 1.0 + TAIL_HOLD_LEAD_S * 4))
        last_rest = rests[-1]
        held = 0
        for e_, n_ in rests:
            if (e_, n_) == last_rest:
                ve_ = val_at(e_ - 0.002)
                for k, q in enumerate(grid):
                    if q >= e_ - 1e-6 and vals[k] != ve_:
                        vals[k] = ve_
                        held += 1
                continue
            if e_ >= TAIL_HOLD_STOP_QN or q2s(n_) - q2s(e_) < TAIL_HOLD_MIN_S:
                continue
            nh_ = s2q(q2s(n_) - TAIL_HOLD_LEAD_S)
            ve_ = val_at(e_ - 0.002)   # the level the last note ended at
            for k, q in enumerate(grid):
                if e_ - 1e-6 <= q < nh_ and vals[k] != ve_:
                    vals[k] = ve_
                    held += 1
    out = []
    for k, (q, v) in enumerate(zip(grid, vals)):
        if k == 0 or k == len(vals) - 1 or v != vals[k - 1] or v != vals[k + 1]:
            out.append({"qn": q + PRE, "db": v})
    if PRE:
        out.insert(0, {"qn": 0.0, "db": out[0]["db"]})
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
local function config_eq(tr, fx, bands, out)
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE0", "0")
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE1", "8")
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE3", "1")   -- c09 (C #1): band 3 = high shelf
  for b = 0, 4 do set_by_fmt(tr, fx, 3 * b + 1, 0.0) end
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED4", "0")
  for _, bd in ipairs(bands) do
    if bd.band == "highpass" then   -- c05 (C #2): band 4 is ReaEQ's high pass (type 4)
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE4", "4")
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED4", "1")
      out[#out + 1] = "highpass " .. set_by_fmt(tr, fx, 12, bd.hz) .. " Hz"
    else
      local b = (bd.band == "lowshelf" and 0) or (bd.band == "highshelf" and 3) or 1
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED" .. b, "1")
      out[#out + 1] = bd.band .. " " .. set_by_fmt(tr, fx, 3 * b, bd.hz) .. " Hz " .. set_by_fmt(tr, fx, 3 * b + 1, bd.db) .. " dB"
      if bd.bw then out[#out] = out[#out] .. " bw " .. set_by_fmt(tr, fx, 3 * b + 2, bd.bw) end
    end
  end
end
local function set_eq(tr, bands)
  for i = reaper.TrackFX_GetCount(tr) - 1, 1, -1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
    if nm:find("ReaEQ") then reaper.TrackFX_Delete(tr, i) end
  end
  if #bands == 0 then return {} end
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local out = {fx = fx}
  config_eq(tr, fx, bands, out)
  for b = 0, 4 do
    local _, en = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDENABLED" .. b)
    local _, ty = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDTYPE" .. b)
    local _, g = reaper.TrackFX_GetFormattedParamValue(tr, fx, 3 * b + 1, "")
    out[#out + 1] = "band" .. b .. " type " .. tostring(ty) .. " on " .. tostring(en) .. " gain " .. g
  end
  return out
end

-- c09 (A #4): a second ReaEQ (after set_eq, which deletes every ReaEQ) whose Wet parameter is automated: 0 before
-- from_qn, 1 from it (square). Emulates a mute on the horns (HO's ConSordino script is a strings EQ; inert on 1FH).
-- c16 (C #1): generalised: spec.points = {{qn, w}, ...} (project qn), spec.shape = envelope point shape (0 linear,
-- 1 square); mix.json "mute_eq" (square step at from_qn) and "loud_eq" (linear wet points) both use it.
local function set_mute_eq(tr, spec)
  if not spec then return nil end
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local out = {fx = fx}
  config_eq(tr, fx, spec.bands, out)
  local wet = -1
  for p = 0, reaper.TrackFX_GetNumParams(tr, fx) - 1 do
    local _, pn = reaper.TrackFX_GetParamName(tr, fx, p, "")
    if pn == "Wet" then wet = p end
  end
  if wet < 0 then out[#out + 1] = "no Wet parameter"; return out end
  local env = reaper.GetFXEnvelope(tr, fx, wet, true)
  reaper.DeleteEnvelopePointRange(env, -1, 1e9)
  reaper.InsertEnvelopePoint(env, 0.0, 0.0, spec.shape, 0, false, true)
  for _, p in ipairs(spec.points) do
    reaper.InsertEnvelopePoint(env, reaper.TimeMap2_QNToTime(0, p.qn), p.w, spec.shape, 0, false, true)
  end
  reaper.Envelope_SortPoints(env)
  reaper.TrackFX_SetParam(tr, fx, wet, 0.0)
  out[#out + 1] = (spec.kind or "wet") .. " eq wet param " .. wet .. " points " .. reaper.CountEnvelopePoints(env)
  return out
end
-- c20 (C #2): mix.json "side_shelf" {hz, db}: a low shelf on the side channel only, after every other FX:
-- JS Mid/Side Encoder (ch1 = (L+R)/2, ch2 = (L-R)/2) -> ReaEQ whose pins read and write channel 2 only (channel 1 has no
-- output pin, so it passes through) -> JS Mid/Side Decoder (0 dB). Re-run safe: set_eq deletes every ReaEQ and this
-- deletes the two JS FX first. With db = 0 the chain is an identity.
local function set_side_shelf(tr, spec, eq)
  for i = reaper.TrackFX_GetCount(tr) - 1, 1, -1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
    if nm:find("Mid/Side") or nm:find("KanakaMS") then reaper.TrackFX_Delete(tr, i) end
  end
  if not spec then return end
  local enc = reaper.TrackFX_AddByName(tr, "JS: utility/KanakaMSEncoder1", false, -1)
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local out = {fx = fx, kind = "side", enc = enc}
  -- c21 (C #4): spec is either {hz, db} (a low shelf, c20) or {bands = {...}} (any config_eq bands, e.g. a high shelf)
  config_eq(tr, fx, spec.bands or {{band = "lowshelf", hz = spec.hz, db = spec.db}}, out)
  reaper.TrackFX_SetPinMappings(tr, fx, 0, 0, 0, 0)
  reaper.TrackFX_SetPinMappings(tr, fx, 0, 1, 2, 0)
  reaper.TrackFX_SetPinMappings(tr, fx, 1, 0, 0, 0)
  reaper.TrackFX_SetPinMappings(tr, fx, 1, 1, 2, 0)
  local dec = reaper.TrackFX_AddByName(tr, "JS: utility/KanakaMS5", false, -1)
  out.dec = dec
  local pins = {}
  for io = 0, 1 do for p = 0, 1 do
    local lo = reaper.TrackFX_GetPinMappings(tr, fx, io, p)
    pins[#pins + 1] = tostring(lo)
  end end
  out[#out + 1] = "side pins in/out " .. table.concat(pins, ",")
  eq[#eq + 1] = out
end
local function set_wet_eqs(tr, specs, eq)
  for _, spec in ipairs(specs) do
    local r = set_mute_eq(tr, spec)
    if r then eq[#eq + 1] = r end
  end
end
"""


def eq_lua(m, bands=None):
    """c04: mix.json eq bands as a Lua table."""
    rows = []
    for b in (m.get("eq", []) if bands is None else bands):
        bw = f', bw={b["bw_oct"]}' if "bw_oct" in b else ""
        rows.append(f'{{band="{b["band"]}", hz={b["hz"]}, db={b.get("db", 0)}{bw}}}')
    return "{" + ",".join(rows) + "}"


def mute_lua(m):
    """c09 (A #4): mix.json mute_eq {from_qn, bands} as a list of Lua wet-EQ specs; from_qn is a score qn.
    c16 (C #1): plus mix.json loud_eq {points: [[score qn, wet], ...], bands}: a level-dependent EQ whose Wet follows the
    points linearly (0 elsewhere), so the soft passages keep their spectrum."""
    specs = []
    me = m.get("mute_eq")
    if me:
        specs.append(f'{{kind="mute", shape=1, points={{{{qn={me["from_qn"] + PRE}, w=1}}}}, bands={eq_lua(m, me["bands"])}}}')
    le = m.get("loud_eq")
    for le in (le if isinstance(le, list) else [le] if le else []):   # c21 (C #3): a list of specs, one ReaEQ each
        pts = ",".join(f'{{qn={q + PRE}, w={w}}}' for q, w in le["points"])
        specs.append(f'{{kind="loud", shape=0, points={{{pts}}}, bands={eq_lua(m, le["bands"])}}}')
    return "{" + ",".join(specs) + "}"


def side_lua(m):
    """c20 (C #2): mix.json side_shelf {hz, db} as a Lua table (nil when absent).
    c21 (C #4): or a list of eq bands ([{band, hz, db}, ...]; lowshelf = ReaEQ band 0, highshelf = band 3)."""
    ss = m.get("side_shelf")
    if isinstance(ss, list):
        return f'{{bands={eq_lua(m, ss)}}}' if ss else "nil"
    return f'{{hz={ss["hz"]}, db={ss["db"]}}}' if ss else "nil"


def b64_path(i, tr):
    return f"{JOBS}/{i:02d}_{tr['stem'].replace(' ', '_')}.b64"


def item_lua(tr):
    """The MIDI item (notes, keyswitches, CCs), volume envelope and ReaEQ for track variable `tr` (Lua)."""
    m = mix_for(tr["name"])
    notes = lua_list([dict(n, qn=round(n["qn"] + PRE, 4)) for n in tr["notes"]], ["qn", "dur", "pitch", "vel"])
    ks_rows = [{"qn": round(k["qn"] + PRE, 4), "pitch": k["pitch"]} for k in tr["ks"]]
    if PRE and tr["first_ks"] is not None:   # c06: the first articulation is also selected in the pre-roll
        ks_rows.insert(0, {"qn": 0.25, "pitch": tr["first_ks"]})
    ks = lua_list(ks_rows, ["qn", "pitch"])
    ccs = []
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, tr.get("cc7", [])), (70, tr.get("cc70", []))):
        ccs += [{"qn": round(q + PRE, 4), "cc": num, "v": v} for q, v in lane]
        if PRE and lane:   # c06: each lane's first value is sent in the pre-roll too
            ccs.append({"qn": 0.25, "cc": num, "v": lane[0][1]})
    ccs = lua_list(ccs, ["qn", "cc", "v"])
    vpts = lua_list(vol_points(tr), ["qn", "db"])
    return f"""
local endqn = {d['end_qn'] + 6 + PRE}
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
local envn = set_vol_env(tr, {vpts})
local eq = set_eq(tr, {eq_lua(m)})
set_wet_eqs(tr, {mute_lua(m)}, eq)
set_side_shelf(tr, {side_lua(m)}, eq)
"""


def track_job(i, tr):
    b64file = b64_path(i, tr)
    open(b64file, "w").write(state_for(tr))   # always regenerated: mix.json changes the state
    r, g, b = COLORS[tr["family"]]
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
""" + item_lua(tr) + f"""
local okget, back = reaper.TrackFX_GetNamedConfigParm(tr, 0, "vst_chunk")
return {{ track = name, okset = okset, notes = nn, ccs = nc, state_len = #back, env_points = envn, eq = eq }}
"""
    p = f"{JOBS}/{i:02d}_{tr['name'].replace(' ', '_')}.lua"
    open(p, "w").write(lua)
    return run(p, timeout=600)


def midi_job(i, tr):
    """c07: replace only the MIDI item, volume envelope and ReaEQ of an existing track; the Opus instance and its loaded
    samples stay (no patch reload, no memory growth). Allowed only when the Opus state build_reaper would write equals
    the state written at the last full build of the track (jobs/NN_<patch>.b64); otherwise the track is fully rebuilt."""
    lua = ENV_LUA + f"""
local name = {json.dumps(tr['name'])}
local tr = R.track_by_name(name)
if not tr then return {{ track = name, error = "no such track" }} end
for j = reaper.CountTrackMediaItems(tr) - 1, 0, -1 do
  local it = reaper.GetTrackMediaItem(tr, j)
  reaper.DeleteTrackMediaItem(tr, it)
end
""" + item_lua(tr) + """
return { track = name, midi_only = true, notes = nn, ccs = nc, env_points = envn, eq = eq, items = reaper.CountTrackMediaItems(tr) }
"""
    p = f"{JOBS}/{i:02d}_{tr['name'].replace(' ', '_')}_midi.lua"
    open(p, "w").write(lua)
    return run(p, timeout=600)


def mix_job():
    rows = []
    for tr in d["tracks"]:
        if ONLY and tr["name"] not in ONLY:
            continue
        m = mix_for(tr["name"])
        rows.append(f'{{n={json.dumps(tr["name"])}, pan=0, w=1, vol={10 ** (m["gain_db"] / 20):.6f}, env={lua_list(vol_points(tr), ["qn", "db"])}, eq={eq_lua(m)}, meq={mute_lua(m)}, ss={side_lua(m)}}}')
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
    set_wet_eqs(tr, r.meq, eq)
    set_side_shelf(tr, r.ss, eq)
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
if (not ONLY and not MIDI_ONLY) or TEMPO:
    print(json.dumps(tempo_job()))
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY:
        continue
    if MIDI_ONLY:
        bf = b64_path(i, tr)
        if os.path.exists(bf) and open(bf).read() == state_for(tr):
            res = midi_job(i, tr)
        else:
            print(f"{tr['name']}: Opus state changed, full rebuild", flush=True)
            res = track_job(i, tr)
    else:
        res = track_job(i, tr)
    print(json.dumps(res), flush=True)

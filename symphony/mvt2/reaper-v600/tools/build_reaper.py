"""Build a score mockup (parts.json from score_to_parts.py) in a running REAPER through the file bridge (~/.rpr-bridge).

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
  needs a full rebuild of the track; --mix-only keeps REAPER's pan at centre / width 1 (mvt3 c06 / mvt2 c48: at
  mix.json track_pan / track_width, which act after the plugin).
Patches are loaded by writing Opus's own plugin state (the .oib instrument JSON inside a
Performance zone) with TrackFX_SetNamedConfigParm(..., "vst_chunk", ...).
"""
import bisect, json, math, os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import opus_state

PARTS, JOBS = sys.argv[1], sys.argv[2]
MIX_ONLY = "--mix-only" in sys.argv[3:]
MIDI_ONLY = "--midi-only" in sys.argv[3:]   # c07: see midi_job
TEMPO = "--tempo" in sys.argv[3:]   # c08: with --midi-only, rewrite the tempo map first
ONLY = set(a for a in sys.argv[3:] if a not in ("--mix-only", "--midi-only", "--tempo", "--no-stale-guard"))
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

# mvt3 c06 (EastWest template mix, mockup-kit/EW-TEMPLATE-PLAN.md items 1-3; no kit code existed, written here):
# - mix.json "family_eq" (group or track key): a list of ReaEQ bands [{"type": "hp"|"lp"|"bell"|"hshelf"|"lshelf",
#   "hz", "db", "bw"}] loaded as a second ReaEQ named "FAMILY EQ" from a ReaEQ plugin chunk built on the template's own
#   chunk (symphony/mockup-research/ew-template-2026-11-08 ho-mix-fx.json STRINGS; vst_chunk). set_eq leaves it alone.
# - mix.json "returns": [{"name", "chunk", "fader_db"}]: REAPER return tracks after the instruments, their FX chain
#   pasted verbatim from the template's chunk file (ReaEQ + EW Spaces II); a group/track "return" {"to", "db"} sends the
#   track post-fader to it. render_cycle.py renders the returns as stems, so the master is the dry stems + the returns.
# - mix.json "track_pan" (group or track): REAPER track pan (I_PANMODE 5, width 1) after the plugin.
REAEQ_TYPES = {"lshelf": 0, "hshelf": 1, "lp": 3, "hp": 4, "bell": 8}
_EW_DIR = "/Users/gooby/sandbox/claude_composes/symphony/mockup-research/ew-template-2026-11-08"


def reaeq_b64(bands):
    """ReaEQ plugin state (what vst_chunk takes) for a band list, on the template's ReaEQ chunk layout:
    int 33, int nbands, per band (int type, int enabled, double Hz, double linear gain, double bw octaves, byte 1),
    then the template's trailer (output gain 1.0 and window data)."""
    import base64, struct
    tpl = json.load(open(f"{_EW_DIR}/ho-mix-fx.json"))["STRINGS"]["fx"][0]["chunk_base64_lines"]
    raw = b"".join(base64.b64decode(x) for x in tpl[1:-1])
    nb = struct.unpack("<i", raw[4:8])[0]
    trailer = raw[8 + 33 * nb:]
    out = struct.pack("<ii", 33, len(bands))
    for b in bands:
        out += struct.pack("<iiddd", REAEQ_TYPES[b["type"]], 1, float(b["hz"]), 10 ** (float(b.get("db", 0.0)) / 20),
                           float(b.get("bw", 2.0))) + b"\x01"
    return base64.b64encode(out + trailer).decode()


def fam_eq_lua(m):
    fe = [b for b in (m.get("family_eq") or []) if isinstance(b, dict)]
    if not fe:
        return "nil"
    want = ",".join(f'{{t={REAEQ_TYPES[b["type"]]}, hz={float(b["hz"])}, db={float(b.get("db", 0.0))}}}' for b in fe)
    return f'{{chunk="{reaeq_b64(fe)}", want={{{want}}}}}'


def sends_lua(m):
    # mvt2 c44: "return" may be one {to, db} or a list of them (e.g. the family return plus the Duc test return)
    r = m.get("return")
    if not r or not MIX.get("returns"):
        return "{}"
    rs = r if isinstance(r, list) else [r]
    return "{" + ", ".join(f'{{to={json.dumps(x["to"])}, vol={10 ** (float(x["db"]) / 20):.6f}}}' for x in rs) + "}"


def track_pan(m):
    return float(m.get("track_pan", 0.0))


def track_width(m):
    """mvt2 c48, from mvt3 c09 (critic C #2; mvt3/reaper-v600/tools/build_reaper.py, unedited there): mix.json
    "track_width" (group or track, default 1.0): REAPER's stereo-pan width (D_WIDTH, I_PANMODE 5) after the plugin, so a
    section sounds as a narrower source at its track_pan; the post-fader sends feed the halls from the narrowed signal.
    Set by the full build and by --mix-only (a --midi-only build leaves it as it is)."""
    return float(m.get("track_width", 1.0))


COLORS = {"perc":(160, 140, 100), "wind": (90, 160, 90), "brass": (210, 170, 60), "timp": (150, 110, 80), "harp": (170, 120, 200), "harm": (170, 120, 200), "string": (70, 110, 200)}


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
        # mvt1 c03 (critic C #4, ONE_TIME): the pre-roll marker gets its own meter (PRE quarter notes = one bar). It had
        # the score's 4/4, so the 3 qn pre-roll was an incomplete bar and REAPER moved the score's first marker from 3.0 s
        # to the next barline (4.0 s): every event from score qn 1 on sounded 1/6 qn early (c00-c02, the "envelope lead")
        pn = int(round(PRE)) if abs(PRE - round(PRE)) < 1e-9 and 1 <= round(PRE) <= 16 else 4
        pts.append({"t": 0.0, "bpm": PRE_BPM, "num": pn, "den": 4, "qn": 0.0})
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
  if math.abs(q - p.qn) > 2.5e-3 then bad[#bad + 1] = {{want = p.qn, got = q}} end
end
reaper.GetSetProjectInfo(0, "PROJECT_SRATE", 48000, true)
reaper.GetSetProjectInfo(0, "PROJECT_SRATE_USE", 1, true)
return {{ markers = reaper.CountTempoTimeSigMarkers(0), mismatches = bad,
         end_sec = reaper.TimeMap2_QNToTime(0, {d['end_qn'] + PRE}), preroll_sec = reaper.TimeMap2_QNToTime(0, {PRE}) }}
"""
    p = f"{JOBS}/00_tempo.lua"
    open(p, "w").write(lua)
    res = run(p)
    # mvt1 c03: any marker REAPER placed off its intended qn shifts every later event; stop the build
    # mvt2 c46: tolerance 1e-3 -> 2.5e-3 qn. Read back on the 353 s c46 map, markers on whole qn are exact and markers
    # between them are early by an amount that grows with absolute time (0.05e-3 qn at 174 s, 1.1e-3 qn = 1.4 ms at
    # score qn 268.25) and returns to 0 at the next whole qn, so nothing accumulates; c45's shorter map sat just under 1e-3
    if res and res.get("mismatches"):
        sys.exit(f"tempo map: {len(res['mismatches'])} markers off their qn, first {res['mismatches'][:3]}")
    return res


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
    # mvt1 c45 (critic C #1 step 2, Opus manual p.139: each mic sub-mix has its own panning; mvt2 c41 ONE_TIME #2, copied
    # from mockup-kit/pipeline/build_reaper.py): "width_by_mic" {mic label: width} widens the listed mics (never narrows:
    # the larger of the track width and the mic's); the Close mic keeps the track width and anchors the seat
    wbm_ = {k_: float(v_) for k_, v_ in (m.get("width_by_mic") or {}).items() if not k_.startswith("_")}
    # mvt3 c06 (EW template, plan item 1): mix.json "pan_by_mic" {"seat_mics": [...]}: the listed mics (Close) sit at the
    # seat with the track width; every other mic (Main, Surround, Mid) stays at full width, centred, as recorded.
    # Replaces width_by_mic and the seat-narrowed Main
    pbm_ = MIX.get("pan_by_mic")
    for c in subs.values():
        c["pan"] = 0.0
        if pbm_ and c["label"] not in pbm_.get("seat_mics", ["Close"]):
            c["panLeft"], c["panRight"] = -1.0, 1.0
            continue
        wd_ = m["width"] if pbm_ else max(m["width"], wbm_.get(c["label"], 0.0))
        c["panLeft"] = max(-1.0, m["seat"] - wd_)
        c["panRight"] = min(1.0, m["seat"] + wd_)
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
    if MIX["reverb"].get("opus_off"):
        # mvt3 c06 (EW template, plan item 2): Opus's own hall off on every track (the return tracks carry the hall):
        # sends to fx:0 at 0, the fx:0 channel at 0, and its ConvolutionReverb removed (no convolution CPU)
        for c in subs.values():
            for ins in c["inserts"]:
                if ins["class"] == "SendProcessor" and ins.get("output") == "fx:0":
                    ins["level"] = 0.0
        fx["volume"] = 0.0
        fx["inserts"] = [i for i in fx["inserts"] if i["class"] != "ConvolutionReverb"]
        return
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
    if MIX["reverb"].get("low_cut_hz"):
        # 2026-11-07 (Dan: too wet, mushy): low cut on the hall input only (same Bandpass, keys lowFilterFreq /
        # lowCutFreq; the factory value is 30 Hz), so the bass reaches the hall less and the low end stays dry
        rv["filterActive"] = True
        rv["lowFilterFreq"] = rv["lowCutFreq"] = float(MIX["reverb"]["low_cut_hz"])
    # mvt2 c40 (ONE_TIME, from the kit / mvt1 c44; Dan: too wet, mushy): the IR envelope ("IR Envelope Preprocessing", Opus manual pp. 133-134) is the
    # ConvolutionReverb's "irSetup" dict (class ConvolutionSetup: envelopeMode, simpleDecay, startPos, endPos,
    # attackLength, decayLength, attackCurve, decayCurve; every installed patch ships envelopeMode 0, simpleDecay 1.0,
    # endPos 1.0). simpleDecay changes nothing in any mode; endPos with decayLength shortens the tail in mode 1 or 2.
    # reverb.ir_setup {key: value} sets it on the shared hall; a track's own "reverb_ir_setup" (mix.json track or group)
    # overrides it (for A/B tests of the decay). Unknown keys stop the build
    irs_ = dict(MIX["reverb"].get("ir_setup") or {}, **(m.get("reverb_ir_setup") or {}))
    for k_, v_ in irs_.items():
        if k_.startswith("_"):
            continue
        if k_ not in rv.get("irSetup", {}):
            sys.exit(f"reverb ir_setup: the ConvolutionSetup has no key {k_!r} ({sorted(rv.get('irSetup', {}))})")
        rv["irSetup"][k_] = type(rv["irSetup"][k_])(v_)
    fx["inserts"] = [i for i in fx["inserts"] if i["class"] != "ConvolutionReverb"] + [rv]


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


UNLOAD_UNUSED_ROWS = True   # c24 (A #4)


def load_articulations(inst, used, row_vol=None):
    """c02: a KS Master loads only its first rows (six in the string patches); a keyswitch to an unloaded articulation
    is ignored. Load and enable every articulation the track uses, and give its trigger a key (as the loaded rows have).
    mvt2 c56 (the finale's c16 tool): row_vol {row name: dB} = mix.json "row_volume_db"[track]: the row's own volume
    knob in the patch (manual p.137; layerMatrix.rows[].volume, 1.0 = 0 dB). Names match without case."""
    want = {a.lower() for a in used if a}
    rows = inst["layerMatrix"]["rows"]
    row_vol = {k_.lower(): v_ for k_, v_ in (row_vol or {}).items()}
    for k_ in row_vol:
        if k_ not in [r["name"].lower() for r in rows]:
            print(f"WARNING row_volume_db: row {k_!r} is not in the patch", file=sys.stderr)
    # c24 (A #4, BRIEF rule 7): unload the default rows the track never plays (the RRx9/RRx16 shorts, Sus Accent, ...),
    # to cut REAPER's sample memory. Only when at least one wanted row exists (the harp patches keep their single row).
    unload = UNLOAD_UNUSED_ROWS and any(r["name"].lower() in want for r in rows)
    for row in rows:
        if row["name"].lower() in want:
            row["loaded"] = True
            row["active"] = True
            if row["name"].lower() in row_vol:
                row["volume"] = round(float(row.get("volume", 1.0)) * 10 ** (float(row_vol[row["name"].lower()]) / 20), 4)
        elif unload:
            row["loaded"] = False
            row["active"] = False
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


_CAP_PRINTED = set()


def cap_release(inst, spec, name):
    """mvt1 c21 (critic A #1): mix.json "sus_release_cap_ms" {"ms", "dyn": [...], "rows": [...]}: cap the AHDSR release
    of the sustain sample groups of the listed rows (default "Sus MAX") whose name ends in one of the listed dynamics
    (default mf/f/ff). A group belongs to a row when every region of its region map sits on that layerMatrix row.
    Release-trail groups ("... RT"), legato transitions ("TLeg") and the soft layers keep their release. The Hollywood
    Strings KS Masters ship 524-931 ms on the Sus MAX sustain groups (Celli mf/f/ff 524, Basses mf 700, Violas mf
    394-653) against 100-237 ms on the legato rows, so rests and cut-offs on Sus MAX did not stop.
    mvt1 c22 (critic A #4): optional "rt_ms" caps the release-trail ("RT") groups of the same rows and dynamics as well
    (the Violas KS Master's Sus MAX RT groups ship 1660 ms, 1st Violins 1245-1741, Celli/Basses 131-166)."""
    ms = float(spec["ms"])
    dyns = set(spec.get("dyn", ["mf", "f", "ff"]))
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if r in spec.get("rows", ["Sus MAX"])}
    hit = {}
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if g.get("type") == 3 or not regs or any(r_.get("row") not in want for r_ in regs):
            continue
        nm = g["name"].split(" rr")[0].split(" RR")[0].strip()
        words = nm.split()
        ms_ = ms
        if words[-1] == "RT" and spec.get("rt_ms") is not None and len(words) >= 2 and words[-2] in dyns:
            ms_ = float(spec["rt_ms"])   # mvt1 c22 (critic A #4): the release-trail groups of the listed dynamics too
        elif "TLeg" in nm or words[-1] == "RT" or words[-1] not in dyns:
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "AHDSR" and pr_.get("release", 0) > ms_:
                hit.setdefault(nm, set()).add(round(pr_["release"]))
                pr_["release"] = ms_
    if (name, ms) not in _CAP_PRINTED:
        _CAP_PRINTED.add((name, ms))
        print(f"{name}: release cap {ms:.0f} ms (RT {spec.get('rt_ms')}) on {sorted((k, sorted(v)) for k, v in hit.items())}", file=sys.stderr)


def region_gain(inst, spec, name):
    """mvt2 c56 (copied from the scherzo's tools/build_reaper.py, c16 version; scherzo c15 critic A #1a): mix.json "region_gain_db" (per track)
    {"rows": [row names], "pitch_db": {"71": 4.5, ...}}: multiply the per-region `volume` (linear; absent = 1) of every
    region on a listed row whose key range holds a listed pitch by 10^(dB/20), so a per-pitch level correction is made
    inside Opus (before its hall, moving with each note's own sample) instead of in the track volume envelope.
    scherzo c16: the value may be a list of such specs (one pitch table per set of rows); row names match without
    case (the cor anglais patch names its row "Sus Max": c15's -3.5 dB for A4 on "Sus MAX" never reached it); and
    "row_dyn_db" {row: {layer: dB}} changes one dynamic layer of a row: layer "pp" / "p" / "mf" / "f" / "ff" selects the
    groups whose name ends in that dynamic (their release-trail groups " RT" too), layer "vel>=N" the regions of a
    velocity-switched short row whose lowest velocity is N or more."""
    if isinstance(spec, list):
        for s_ in spec:
            region_gain(inst, s_, name)
        return
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    low_ = lambda x: (x or "").lower()
    for r_ in list(spec.get("rows") or []) + list(spec.get("row_db", {})) + list(spec.get("row_dyn_db", {})):
        if low_(r_) not in [low_(x) for x in rows]:
            print(f"WARNING {name}: region gain row {r_!r} is not in the patch", file=sys.stderr)
    want = {i for i, r in enumerate(rows) if spec.get("rows") is None or low_(r) in [low_(x) for x in spec["rows"]]}   # rows None: every row
    pd_ = {int(k): float(v) for k, v in spec.get("pitch_db", {}).items()}
    rd_ = {i: float(v_) for i, r in enumerate(rows) for k_, v_ in spec.get("row_db", {}).items() if low_(k_) == low_(r)}   # "row_db" {row: dB}: a whole row
    dd_ = {i: v_ for i, r in enumerate(rows) for k_, v_ in spec.get("row_dyn_db", {}).items() if low_(k_) == low_(r)}
    n_ = nd_ = 0
    for g in inst.get("groups", []):
        gn_ = (g.get("name") or "")
        gdyn_ = (gn_[:-3] if gn_.endswith(" RT") else gn_).rsplit(" ", 1)[-1]
        for r_ in (g.get("regionMap") or {}).get("regions", []):
            if r_.get("row") in rd_:
                r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (rd_[r_["row"]] / 20.0)
                n_ += 1
            for l_, d_ in dd_.get(r_.get("row"), {}).items():
                if (l_.startswith("vel>=") and r_.get("velMin", 0) >= int(l_[5:])) or l_ == gdyn_:
                    r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (float(d_) / 20.0)
                    nd_ += 1
            if r_.get("row") not in want:
                continue
            for p_, d_ in pd_.items():
                if r_.get("keyMin", -1) <= p_ <= r_.get("keyMax", -1):
                    r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (d_ / 20.0)
                    n_ += 1
                    break
    print(f"{name}: region gain on {n_} regions" + (f", dynamic-layer gain on {nd_}" if nd_ else ""), file=sys.stderr)


def state_for(tr):
    inst = opus_state.load_oib(tr["patch"])
    if "articulations" in inst:
        load_articulations(inst, list(tr["art_counts"]) + [tr["first_art"]], (MIX.get("row_volume_db") or {}).get(tr["name"]))
    if tr["first_ks"] is not None and "articulations" in inst:
        inst["articulations"]["currentKeySwitch"] = tr["first_ks"]
    for f in inst.get("filters", []):
        if f.get("name") == "ConSordino" and tr["cc15"]:
            f["conSordino"] = tr["cc15"][0][1] >= 64
    m_ = mix_for(tr["name"])
    apply_mix(inst, m_)
    if m_.get("env_release_ms") is not None:
        # mvt1 c11 (critic A #4): set the amplitude envelope's release of every sample group (Harp Sus RR ships 3019 ms,
        # so a note-off never damps a string); score_to_parts.py HARP_RING_S then sets each note's ring by its length
        rel_ = float(m_["env_release_ms"])
        for g_ in inst.get("groups", []):
            for pr_ in (g_.get("processors") or {}).get("processors", []):
                if pr_.get("class") == "AHDSR":
                    pr_["release"] = rel_
        if isinstance(inst.get("envelope"), dict) and "releaseTime" in inst["envelope"]:
            inst["envelope"]["releaseTime"] = rel_
    if m_.get("env_sustain") is not None or m_.get("env_decay_ms") is not None:
        # mvt1 c35 (critic A #2): Harp Sus RR (and Harp Pluck Long) ship every AHDSR, and the instrument EnvelopeProxy, with
        # decay 5990 ms to sustain 0.001, so each note fell to -60 dB in 6 s whatever its sample (the recorded plucks run
        # 6.6-10.6 s): the final ppp chord died 2 s into its fermata. env_sustain (0..1) sets the sustain level, so a note
        # decays as recorded until its note-off and env_release_ms; env_decay_ms sets the decay time
        for g_ in inst.get("groups", []):
            for pr_ in (g_.get("processors") or {}).get("processors", []):
                if pr_.get("class") == "AHDSR":
                    if m_.get("env_sustain") is not None:
                        pr_["sustain"] = float(m_["env_sustain"])
                    if m_.get("env_decay_ms") is not None:
                        pr_["decay"] = float(m_["env_decay_ms"])
        if isinstance(inst.get("envelope"), dict):
            if m_.get("env_sustain") is not None and "sustain" in inst["envelope"]:
                inst["envelope"]["sustain"] = float(m_["env_sustain"])
            if m_.get("env_decay_ms") is not None and "decayTime" in inst["envelope"]:
                inst["envelope"]["decayTime"] = float(m_["env_decay_ms"])
    if m_.get("sus_release_cap_ms") is not None:
        # mvt1 c46 / mvt2 c41 (coordinator, critics A #1 / C #1): a list of specs, applied in order (e.g. 300 ms at mf-ff
        # and 400 ms at pp / p); cap_release only lowers releases
        caps_ = m_["sus_release_cap_ms"]
        for spec_ in (caps_ if isinstance(caps_, list) else [caps_]):
            cap_release(inst, spec_, tr["name"])
    if m_.get("region_gain_db"):   # mvt2 c56: per-pitch / per-row sample levels inside Opus (see region_gain)
        region_gain(inst, m_["region_gain_db"], tr["name"])
    _, perf, _ = opus_state.split(opus_state.TEMPLATE)
    perf["name"] = tr["name"]
    perf["zones"] = [{"class": "InstrumentZone", "keyMin": 0, "keyMax": 127, "velMin": 1, "velMax": 127,
                      "octave": 0, "groupIndex": 0, "instrument": inst}]
    return opus_state.build(perf)


# c17 (C #2), see vol_points; the final fade starts 0.5 qn before the score's last release (parts.json score_end)
TAIL_HOLD_MIN_S, TAIL_HOLD_LEAD_S, TAIL_HOLD_STOP_QN = 0.5, 0.35, d.get("score_end", d["end_qn"]) - 0.5


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


# mvt1 c33 (critic B #3): 72 -> 127 (every decrescendo). From f/ff/fff the brass and bassoon soft trims climbed 7-17 dB
# inside the hairpin (Tuba bar 162 ff > mp fell 0.7 dB on its stem, envelope +6.6; bars 124-125 fff > pp held -12.5 re M
# while the master fell 16 dB); only decrescendos starting above mf change, each by a cut
SOFT_DECRESC_HOLD_MAX_CC = 127   # mvt1 c15 (critic B #2): 72; None = off
# the trim keeps this share of its rise inside the hairpin: with none kept (the c15 render) the 20 soft decrescendos
# with a rising trim fell a median 6.5 dB (others 4.4; before 1.7), Horn 1 at bar 106 11.9 dB from mf to mp
SOFT_DECRESC_KEEP = 0.5
# mvt1 c36 (critic C #1, Dan's listening note on bar 62): this envelope comes after the Opus hall, so a subito fall of
# 11-16 dB at the mark cut the forte's hall tail at once (master -14.5 dB in 0.2 s, flat after: "sounds like a glitch";
# a natural cut-off here falls about 7 dB by 0.1-0.2 s and 11 dB by 0.2-0.3 s). At each parts.json `subito_falls` entry
# [mark, fall qn] (score_to_parts SUBITO_FRESH: the fall qn is the moved onset of the track's note on the mark): the
# level before the fall is held to the fall qn; a track that sounded in the `sounded_s` before it then falls
# `at_once_db` at once and the rest linearly in dB over `ramp_s` (never under the level after the mark); a smaller fall
# (or a silent track) moves to the fall qn. None = off
SUBITO_TAIL = {"at_once_db": 4.0, "ramp_s": 0.35, "sounded_s": 0.5, "min_db": 0.5}


# mvt2 c55: REAPER's volume-envelope fader scale (VOLTYPE 1), up to a constant factor: amplitude ** 0.25 (the Scherzo's
# c15 bridge read of reaper.ScaleToEnvelopeMode(1, a); symphony/scherzo/reaper-v600/cycles/c15/records/env_scale.txt)
ENV_SCALE = lambda db: 10 ** (db / 80.0)
ENV_UNSCALE = lambda s: 80.0 * math.log10(max(1e-9, s))


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
    # mvt1 c02 (critic B #5): optional "mp" (CC 58) and "mf" (CC 72) anchors. The taper from the p anchor (+5) to a
    # negative f trim cancelled CC11's growth from p to mf (Flute 1 medians pp -44.8 / p -44.1 / mp -44.8 / mf -44.4 dB)
    tbl = sorted(tbl + [(c_, soft[k_]) for k_, c_ in (("mp", 58), ("mf", 72)) if k_ in soft])
    # mvt1 c09: an optional "fff" anchor (CC 124) in dyn_trim_db (the CC1-layered brass: fff on the ff layer alone)
    if "fff" in dt:
        tbl = [r for r in tbl if r[0] != 127] + [(124, dt["fff"]), (127, dt["fff"])]

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
    # mvt1 c15 (critic B #2): the soft trims are larger at pp than at p, so across a soft decrescendo the envelope rose
    # 2-9 dB and cancelled most of CC11's fall (median fall -1.7 dB where the trim rose 2 dB or more, -4.1 elsewhere).
    # Inside each decrescendo that starts at CC SOFT_DECRESC_HOLD_MAX_CC or lower, from its start to the first note-on
    # after its end, the trim may fall but rises only by SOFT_DECRESC_KEEP of its rise above its value at the hairpin's
    # start
    holds = []
    if dyn and SOFT_DECRESC_HOLD_MAX_CC is not None:
        ons_ = sorted((n.get("sq", n["qn"]), n["qn"]) for n in tr.get("notes", []))
        for h0, h1, k_ in tr.get("hairpins", []):
            if k_ != "decresc":
                continue
            # mvt2 c48: a decrescendo printed at an fp starts from the p after the attack (parts.json fp_falls), not from
            # the attack's f: with the attack a step at the mark (FP_SPIKE_AT_MARK) the cap read the f trim and held the p
            # after the fp 2-3 dB under its soft trim up to the next note
            fa_ = next((b_ for a_, b_ in tr.get("fp_falls", []) if abs(a_ - h0) < 0.02), None)
            c0 = step_at(dyn, fa_ if fa_ is not None else h0, first)
            if c0 > SOFT_DECRESC_HOLD_MAX_CC:
                continue
            # up to the moved onset of the first note whose score onset is at or after the hairpin's end
            e_ = next((mq_ for sq_, mq_ in ons_ if sq_ >= h1 - 1e-6), h1 + 1.0)
            holds.append((h0, e_, trim(c0), SOFT_DECRESC_KEEP))

    fpw_ = [(a_, b_) for a_, b_ in tr.get("fp_falls", [])]

    def trim_at(q):
        # mvt2 c48: under an fp attack (mark to the end of its fall, parts.json fp_falls) the trim reads the p it falls
        # to: the f spike is the attack's shape, not a printed f to balance. The f trim dipped the envelope 4-6 dB under
        # the attack (soft trim p against dyn trim f; Violins II +3.5 / -0.5, basses +8.5 / +2.5), on score time while
        # the led notes' CC11 step starts at their moved note-on
        c_ = next((step_at(dyn, b_, first) for a_, b_ in fpw_ if a_ - 1e-9 <= q < b_ - 1e-9), None)
        t_ = trim(step_at(dyn, q, first) if c_ is None else c_)
        for a_, b_, cap_, keep_ in holds:
            if a_ - 1e-9 <= q < b_ - 1e-9 and t_ > cap_:
                t_ = cap_ + keep_ * (t_ - cap_)
        return t_
    val_at = lambda q: round(g + step_at(vol, q) + (trim_at(q) if dyn else 0.0), 2)
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
        # mvt2 c47 (critic C #4): level shapes that start at or after the last release (parts.json post_end_shapes, e.g.
        # a fade over the final chord's release) are added on top of the last-rest hold. With the hall in post-fader
        # returns (c44) the envelope sits before the hall, so such a fade shortens the dry release and what it sends
        for ps_ in tr.get("post_end_shapes", []):
            for k, q in enumerate(grid):
                if q >= ps_[0][0] - 1e-9:
                    j_ = bisect.bisect_right([x_ for x_, _ in ps_], q) - 1
                    if j_ >= len(ps_) - 1:
                        d_ = ps_[-1][1]
                    else:
                        (x0_, d0_), (x1_, d1_) = ps_[j_], ps_[j_ + 1]
                        d_ = d0_ + (d1_ - d0_) * (q - x0_) / (x1_ - x0_)
                    vals[k] = round(vals[k] + d_, 2)
    # mvt1 c36: SUBITO_TAIL (see the default)
    if SUBITO_TAIL and tr.get("subito_falls"):
        segs_ = [(n["qn"], n["qn"] + n["dur"]) for n in tr.get("notes", [])]
        for s_, f_ in tr["subito_falls"]:
            def cur(q, G=list(grid), V=list(vals)):
                k = bisect.bisect_left(G, q)
                if k <= 0:
                    return V[0]
                if k >= len(G):
                    return V[-1]
                return V[k - 1] + (V[k] - V[k - 1]) * (q - G[k - 1]) / max(1e-9, G[k] - G[k - 1])
            fs_ = min(f_, s_ - 0.1)   # the hairpin and level-shape falls start up to 0.1 qn before the mark
            pre = cur(fs_ - 0.002)
            post = lambda q: cur(max(q, s_))
            drop = pre - post(f_)
            if drop < SUBITO_TAIL["min_db"]:
                continue
            T = s2q(q2s(f_) + SUBITO_TAIL["ramp_s"]) - f_
            A = SUBITO_TAIL["at_once_db"]
            q_snd = s2q(max(0.0, q2s(f_) - SUBITO_TAIL["sounded_s"]))
            split = drop > A and any(a_ < f_ - 1e-6 and b_ > q_snd for a_, b_ in segs_)
            pT = post(f_ + T)

            def new_v(q):
                if q < f_:
                    return pre
                if split and q <= f_ + T:
                    return max(post(q), (pre - A) + (pT - (pre - A)) * (q - f_) / T)
                return post(q)
            q_end = max(s_, f_ + T if split else f_)
            add = [fs_ - 0.002, fs_, f_ - 0.002, f_, s_, q_end] + ([f_ + T * k_ / 6 for k_ in range(1, 7)] if split else [])
            old_map = dict(zip(grid, vals))
            grid = sorted(set(grid) | {round(x_, 5) for x_ in add if fs_ - 0.01 <= x_ <= q_end + 1e-9})
            vals = [round(new_v(q), 2) if fs_ - 0.005 <= q <= q_end + 1e-9 else old_map[q] for q in grid]
    # mvt2 c56 (lead 1.1; critics B #4, C #6): mix.json "env_edge_slew" {"db_s": R, "tail_s", "mark_pad_qn", "skip_families"}
    # (top level; absent = off). Role, section-row and hairpin-gain-release edges are keyed to score onsets and bar lines,
    # so they stepped 2-5 dB inside notes that start earlier (leads) or are held across the edge. While the track sounds
    # (moved note-on to note end + tail_s) and no hairpin or dynamic mark is printed there, the envelope may move at most
    # R dB per second: the lane is slew-limited forward and backward and the two are averaged, so a step becomes a ramp
    # centred on its edge (slope R/2) and nothing faster than R remains; in rests the envelope moves as written, so an
    # edge before an entry is complete at the note-on. Printed sudden changes (a dyn_curve step of "mark_min_cc" CC or
    # more, default 24, +- mark_pad_qn; fp and subito falls), the final fade and the skipped families (the timpani roll
    # rules) keep their timing; "hairpins_free": true also leaves the inside of printed hairpins alone (off: a hairpin's
    # gain is itself slower than R, and role edges that fall inside hairpins were among the largest steps).
    es_ = MIX.get("env_edge_slew") if not os.environ.get("ENV_NO_SLEW") else None
    if es_ and tr.get("notes") and tr.get("family") not in es_.get("skip_families", ("timp",)) and len(grid) > 2:
        R_ = float(es_["db_s"]); tl_ = float(es_.get("tail_s", 0.25)); pad_ = float(es_.get("mark_pad_qn", 0.3))
        ts_ = [q2s(q) for q in grid]
        snd_ = sorted((q2s(n["qn"]), q2s(n["qn"] + n["dur"]) + tl_) for n in tr["notes"])
        mk_ = [(q2s(h0), q2s(h1)) for h0, h1, _ in tr.get("hairpins", [])] if es_.get("hairpins_free") else []
        dc_ = tr.get("dyn_curve", [])
        mk_ += [(q2s(q_ - pad_), q2s(q_ + pad_)) for (q0_, c0_), (q_, c_) in zip(dc_, dc_[1:]) if abs(c_ - c0_) >= es_.get("mark_min_cc", 24)]
        mk_ += [(q2s(a_ - pad_), q2s(b_ + pad_)) for a_, b_ in tr.get("fp_falls", [])] + [(q2s(s_ - pad_), q2s(f_ + 1.0)) for s_, f_ in tr.get("subito_falls", [])]
        mk_.append((q2s(TAIL_HOLD_STOP_QN - 2.0), 1e9))
        mk_.sort()
        def merge_(iv):
            out_ = []
            for a_, b_ in sorted(iv):
                if out_ and a_ <= out_[-1][1]:
                    out_[-1][1] = max(out_[-1][1], b_)
                else:
                    out_.append([a_, b_])
            return out_
        snd_, mk_ = merge_(snd_), merge_(mk_)

        def cover_(iv, t):
            k_ = bisect.bisect_right(iv, [t, 1e18]) - 1
            return k_ >= 0 and iv[k_][0] <= t < iv[k_][1]
        lim_ = [None] * len(grid)   # the largest move allowed over segment k-1 -> k (None = free)
        for k in range(1, len(grid)):
            tm_ = 0.5 * (ts_[k - 1] + ts_[k])
            if cover_(snd_, tm_) and not cover_(mk_, tm_):
                lim_[k] = R_ * (ts_[k] - ts_[k - 1])
        f_ = list(vals)
        for k in range(1, len(grid)):
            if lim_[k] is not None:
                f_[k] = min(max(vals[k], f_[k - 1] - lim_[k]), f_[k - 1] + lim_[k])
        b_ = list(vals)
        for k in range(len(grid) - 2, -1, -1):
            if lim_[k + 1] is not None:
                b_[k] = min(max(vals[k], b_[k + 1] - lim_[k + 1]), b_[k + 1] + lim_[k + 1])
        vals = [round(0.5 * (x_ + y_), 2) for x_, y_ in zip(f_, b_)]
        # a printed sudden change keeps its step, but the step is keyed to the note it belongs to: where a note of the
        # track has its score onset on the mark and its moved note-on before it, the envelope takes the value it has
        # 0.15 qn after the mark from 0.02 qn before the note-on (the step sat 50-300 ms inside the led note: Horn 1's
        # solo entry at 226 stepped +5.3 dB after its note-on, Horn 3 at 204 +4.6)
        for (q0_, c0_), (qm_, c_) in zip(dc_, dc_[1:]):
            if abs(c_ - c0_) < es_.get("mark_min_cc", 24) or qm_ >= TAIL_HOLD_STOP_QN - 2.0:
                continue
            on_ = min((n["qn"] for n in tr["notes"] if abs(n.get("sq", n["qn"]) - qm_) < 0.02), default=None)
            if on_ is None or on_ > qm_ - 0.01 or on_ < qm_ - 0.6:
                continue
            def cur_(q, G=list(grid), V=list(vals)):
                k = bisect.bisect_left(G, q)
                if k <= 0:
                    return V[0]
                if k >= len(G):
                    return V[-1]
                return V[k - 1] + (V[k] - V[k - 1]) * (q - G[k - 1]) / max(1e-9, G[k] - G[k - 1])
            qa_, qb_ = round(on_ - 0.04, 5), round(on_ - 0.02, 5)
            qe_ = round(qm_ + 0.15, 5)
            va_, ve_ = round(cur_(qa_), 2), round(cur_(qe_), 2)
            if abs(ve_ - va_) < 1.0 and max(abs(v - va_) for q, v in zip(grid, vals) if qa_ <= q <= qe_ or q == grid[0]) < 1.0:
                continue
            pts_ = [(q, v) for q, v in zip(grid, vals) if q < qa_ - 1e-9 or q > qe_ + 1e-9] + [(qa_, va_), (qb_, ve_), (qe_, ve_)]
            pts_.sort()
            grid, vals = [q for q, _ in pts_], [v for _, v in pts_]
    # mvt2 c55 (critics B #1, C #4; the Scherzo's c15 pass): simplification. Two thirds of the c54 points were slow layers
    # drawn as stairs or collinear grid samples. With mix.json "env_simplify_db" (top level; absent or 0 = off;
    # environment ENV_NO_SIMPLIFY=1 switches it off) a point stays only if the line between its kept neighbours misses it
    # by more than that many dB (Douglas-Peucker). REAPER draws the line between two points of a volume envelope in its
    # fader scale (VOLTYPE 1: amplitude ** 0.25, read with reaper.ScaleToEnvelopeMode in the Scherzo's c15) and in
    # seconds, not in qn: the error is taken on ENV_SCALE values over seconds and converted back to dB, and no kept
    # segment spans more than "env_simplify_max_seg_db" (default 4), so the result does not depend on the exact law
    keep = None
    tol_ = MIX.get("env_simplify_db", 0) if not os.environ.get("ENV_NO_SIMPLIFY") else 0
    if tol_ and len(grid) > 2:
        mseg_ = MIX.get("env_simplify_max_seg_db", 4.0)
        ts_ = [q2s(q) for q in grid]
        sc_ = [ENV_SCALE(v) for v in vals]
        keep = [False] * len(grid)
        keep[0] = keep[-1] = True
        stack = [(0, len(grid) - 1)]
        while stack:
            i, j = stack.pop()
            if j - i < 2:
                continue
            worst, wk = 0.0, None
            dt_ = max(1e-12, ts_[j] - ts_[i])
            for k in range(i + 1, j):
                e_ = abs(vals[k] - ENV_UNSCALE(sc_[i] + (sc_[j] - sc_[i]) * (ts_[k] - ts_[i]) / dt_))
                if e_ > worst:
                    worst, wk = e_, k
            if worst <= tol_ and abs(vals[j] - vals[i]) > mseg_:
                wk = (i + j) // 2
            elif worst <= tol_:
                continue
            keep[wk] = True
            stack += [(i, wk), (wk, j)]
    out = []
    for k, (q, v) in enumerate(zip(grid, vals)):
        if keep is not None:
            if keep[k]:
                out.append({"qn": q + PRE, "db": v})
        elif k == 0 or k == len(vals) - 1 or v != vals[k - 1] or v != vals[k + 1]:
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
      -- c25 (C #1): "bell2" = band 2, a second bell (ReaEQ type 8)
      local b = (bd.band == "lowshelf" and 0) or (bd.band == "highshelf" and 3) or (bd.band == "bell2" and 2) or 1
      if b == 2 then reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDTYPE2", "8") end
      reaper.TrackFX_SetNamedConfigParm(tr, fx, "BANDENABLED" .. b, "1")
      out[#out + 1] = bd.band .. " " .. set_by_fmt(tr, fx, 3 * b, bd.hz) .. " Hz " .. set_by_fmt(tr, fx, 3 * b + 1, bd.db) .. " dB"
      if bd.bw then out[#out] = out[#out] .. " bw " .. set_by_fmt(tr, fx, 3 * b + 2, bd.bw) end
    end
  end
end
local function is_family_eq(tr, i)
  local _, rn = reaper.TrackFX_GetNamedConfigParm(tr, i, "renamed_name")
  local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
  return rn == "FAMILY EQ" or nm == "FAMILY EQ"
end
local function set_eq(tr, bands)
  for i = reaper.TrackFX_GetCount(tr) - 1, 1, -1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, i, "")
    if nm:find("ReaEQ") and not is_family_eq(tr, i) then reaper.TrackFX_Delete(tr, i) end   -- mvt3 c06: keep FAMILY EQ
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

-- mvt3 c06 (EW template, plan item 3): the family EQ as its own ReaEQ named "FAMILY EQ", loaded from a ReaEQ plugin
-- chunk (vst_chunk) and read back (band type, frequency and gain as ReaEQ displays them). Re-run safe: an old FAMILY EQ
-- is deleted first; set_eq skips it. spec = nil removes it.
local function set_family_eq(tr, spec)
  for i = reaper.TrackFX_GetCount(tr) - 1, 1, -1 do
    if is_family_eq(tr, i) then reaper.TrackFX_Delete(tr, i) end
  end
  if not spec then return nil end
  local fx = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
  local ok = reaper.TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", spec.chunk)
  reaper.TrackFX_SetNamedConfigParm(tr, fx, "renamed_name", "FAMILY EQ")
  local out = {fx = fx, ok = ok, bad = {}}
  for b, w in ipairs(spec.want) do
    local _, ty = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDTYPE" .. (b - 1))
    local _, en = reaper.TrackFX_GetNamedConfigParm(tr, fx, "BANDENABLED" .. (b - 1))
    local _, fs = reaper.TrackFX_GetFormattedParamValue(tr, fx, 3 * (b - 1), "")
    local _, gs = reaper.TrackFX_GetFormattedParamValue(tr, fx, 3 * (b - 1) + 1, "")
    local hz = tonumber((fs or ""):match("[-%d%.]+")) or -1
    if (fs or ""):find("k") then hz = hz * 1000 end
    local g = tonumber((gs or ""):match("[-%d%.]+")) or 0
    if (gs or ""):find("inf") then g = -150 end
    out[#out + 1] = ty .. "/" .. en .. " " .. fs .. " " .. gs
    local gain_ok = (w.t == 4 or w.t == 3) or math.abs(g - w.db) < 0.15
    if tonumber(ty) ~= w.t or en ~= "1" or math.abs(hz - w.hz) > 0.03 * w.hz + 2 or not gain_ok then
      out.bad[#out.bad + 1] = b
    end
  end
  return out
end
-- mvt3 c06: post-fader sends from this track to the named return tracks (old sends to any of them are removed first)
local function set_sends(tr, S, all_returns)
  for i = reaper.GetTrackNumSends(tr, 0) - 1, 0, -1 do
    local dest = reaper.GetTrackSendInfo_Value(tr, 0, i, "P_DESTTRACK")
    local _, dn = reaper.GetTrackName(dest)
    for _, rn in ipairs(all_returns) do if dn == rn then reaper.RemoveTrackSend(tr, 0, i); break end end
  end
  local out = {}
  for _, s in ipairs(S) do
    local dest = R.track_by_name(s.to)
    if dest then
      local k = reaper.CreateTrackSend(tr, dest)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "I_SENDMODE", 0)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "D_VOL", s.vol)
      reaper.SetTrackSendInfo_Value(tr, 0, k, "D_PAN", 0)
      out[#out + 1] = s.to .. " " .. string.format("%.2f dB", 20 * math.log(s.vol, 10))
    else
      out[#out + 1] = "MISSING return " .. s.to
    end
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
  -- mvt1 c35 (critic C #2): spec.switched = {points = {{qn, w}, ...}, bands = {...}}: a second side-only ReaEQ inside the
  -- same encoder/decoder pair, same pins, its Wet automated (linear) like set_mute_eq: a side band that a passage switches off
  if spec.switched then
    local fx2 = reaper.TrackFX_AddByName(tr, "ReaEQ", false, -1)
    local o2 = {fx = fx2, kind = "side switched"}
    config_eq(tr, fx2, spec.switched.bands, o2)
    reaper.TrackFX_SetPinMappings(tr, fx2, 0, 0, 0, 0)
    reaper.TrackFX_SetPinMappings(tr, fx2, 0, 1, 2, 0)
    reaper.TrackFX_SetPinMappings(tr, fx2, 1, 0, 0, 0)
    reaper.TrackFX_SetPinMappings(tr, fx2, 1, 1, 2, 0)
    local wet = -1
    for p = 0, reaper.TrackFX_GetNumParams(tr, fx2) - 1 do
      local _, pn = reaper.TrackFX_GetParamName(tr, fx2, p, "")
      if pn == "Wet" then wet = p end
    end
    if wet >= 0 then
      local env = reaper.GetFXEnvelope(tr, fx2, wet, true)
      reaper.DeleteEnvelopePointRange(env, -1, 1e9)
      for _, p in ipairs(spec.switched.points) do
        reaper.InsertEnvelopePoint(env, reaper.TimeMap2_QNToTime(0, p.qn), p.w, 0, 0, false, true)
      end
      reaper.Envelope_SortPoints(env)
      local pins2 = {}
      for io = 0, 1 do for pp = 0, 1 do pins2[#pins2 + 1] = tostring(reaper.TrackFX_GetPinMappings(tr, fx2, io, pp)) end end
      o2[#o2 + 1] = "switched side wet param " .. wet .. " points " .. reaper.CountEnvelopePoints(env) .. " pins " .. table.concat(pins2, ",")
    else
      o2[#o2 + 1] = "no Wet parameter"
    end
    eq[#eq + 1] = o2
  end
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
    c21 (C #4): or a list of eq bands ([{band, hz, db}, ...]; lowshelf = ReaEQ band 0, highshelf = band 3).
    mvt1 c35 (C #2): plus mix.json side_shelf_switched {points, bands}: a second side EQ with an automated Wet."""
    ss = m.get("side_shelf")
    sw = m.get("side_shelf_switched")   # mvt1 c35 (critic C #2): {points: [[score qn, wet], ...], bands: [...]}
    swl = ""
    if sw:
        pts = ",".join(f'{{qn={q + PRE}, w={w}}}' for q, w in sw["points"])
        swl = f', switched={{points={{{pts}}}, bands={eq_lua(m, sw["bands"])}}}'
    if isinstance(ss, list):
        return f'{{bands={eq_lua(m, ss)}{swl}}}' if ss else "nil"
    return f'{{hz={ss["hz"]}, db={ss["db"]}{swl}}}' if ss else "nil"


def b64_path(i, tr):
    return f"{JOBS}/{i:02d}_{tr['stem'].replace(' ', '_')}.b64"


RR_RESET_QN = 0.1   # c24 (A #3): pre-roll position (REAPER qn) of the CC36 reset and the string CC69 off
# mvt2 c45 (critic B, HO manual p.34): the Opus engine's round-robin reset is the CC set in Opus's Preferences
# ("RoundRobinResetCC": 16 in /Library/Application Support/East West/Opus/Preferences.json); CC36 is only the KS Masters'
# Repetition script "Reset RR". No patch maps CC16 to anything else (ks_maps.json controls)
RR_RESET_CC = 16
RR_RESET_SKIP_FAMILIES = {"harp", "harm"}   # harp tracks were already bit-identical render to render
REP_OFF_FAMILIES = {"string"}


def item_lua(tr):
    """The MIDI item (notes, keyswitches, CCs), volume envelope and ReaEQ for track variable `tr` (Lua)."""
    m = mix_for(tr["name"])
    notes = lua_list([dict(n, qn=round(n["qn"] + PRE, 4)) for n in tr["notes"]], ["qn", "dur", "pitch", "vel"])
    ks_rows = [{"qn": round(k["qn"] + PRE, 4), "pitch": k["pitch"]} for k in tr["ks"]]
    if PRE and tr["first_ks"] is not None:   # c06: the first articulation is also selected in the pre-roll
        ks_rows.insert(0, {"qn": 0.25, "pitch": tr["first_ks"]})
    ks = lua_list(ks_rows, ["qn", "pitch"])
    ccs = []
    # mvt2 c49 (A #1): the parts.json lane "cc36" (round-robin resets inside the music: MEAS_TREM "rr_runs" and
    # RR_RESET_AT) is sent on RR_RESET_CC, the controller Opus resets on (CC36 inside the music did not reset a stroke
    # row in Movement I c14); the lane is not repeated in the pre-roll, which has its own reset at RR_RESET_QN
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, tr.get("cc7", [])), (70, tr.get("cc70", [])),
                     (RR_RESET_CC, tr.get("cc36", []))):
        ccs += [{"qn": round(q + PRE, 4), "cc": num, "v": v} for q, v in lane]
        if PRE and lane and num != RR_RESET_CC:   # c06: each lane's first value is sent in the pre-roll too
            ccs.append({"qn": 0.25, "cc": num, "v": lane[0][1]})
    if PRE and tr["family"] not in RR_RESET_SKIP_FAMILIES:
        # c24 (A #3): reset Opus's round-robin state (CC36, any value) at the start of every render, and on the strings
        # turn the Repetition script off (CC69 0-63 = OFF, HO manual CC table), so renders are reproducible
        ccs.append({"qn": RR_RESET_QN, "cc": RR_RESET_CC, "v": 127})
        if tr["family"] in REP_OFF_FAMILIES:
            ccs.append({"qn": RR_RESET_QN, "cc": 69, "v": 0})
    ccs = lua_list(ccs, ["qn", "cc", "v"])
    vpts = lua_list(vol_points(tr), ["qn", "db"])
    return f"""
local endqn = {d['end_qn'] + 6 + PRE}
local item = reaper.CreateNewMIDIItemInProj(tr, 0, endqn, true)
local take = reaper.GetActiveTake(item)
reaper.GetSetMediaItemTakeInfo_String(take, "P_NAME", name .. " ({d.get('title', 'mockup')})", true)
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
local feq = set_family_eq(tr, {fam_eq_lua(m)})   -- mvt3 c06
local sends = set_sends(tr, {sends_lua(m)}, {{{returns_names_lua()}}})
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
reaper.SetMediaTrackInfo_Value(tr, "D_PAN", {track_pan(mix_for(tr['name']))})     -- c05: the seat is set inside Opus (apply_mix); mvt3 c06: mix.json track_pan
reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", {track_width(mix_for(tr['name']))})   -- mvt2 c48 (mvt3 c09): mix.json track_width
reaper.SetMediaTrackInfo_Value(tr, "D_VOL", 1.0)   -- c02: the gain is in the volume envelope
reaper.SetMediaTrackInfo_Value(tr, "I_RECARM", 0); reaper.SetMediaTrackInfo_Value(tr, "I_RECMON", 0)
local f = assert(io.open({json.dumps(os.path.abspath(b64file))}, "rb")); local st = f:read("a"); f:close()
local okset = reaper.TrackFX_SetNamedConfigParm(tr, 0, "vst_chunk", st)
""" + item_lua(tr) + f"""
local okget, back = reaper.TrackFX_GetNamedConfigParm(tr, 0, "vst_chunk")
return {{ track = name, okset = okset, notes = nn, ccs = nc, state_len = #back, env_points = envn, eq = eq, family_eq = feq, sends = sends }}
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
return { track = name, midi_only = true, notes = nn, ccs = nc, env_points = envn, eq = eq, family_eq = feq, sends = sends, items = reaper.CountTrackMediaItems(tr) }
"""
    p = f"{JOBS}/{i:02d}_{tr['name'].replace(' ', '_')}_midi.lua"
    open(p, "w").write(lua)
    return run(p, timeout=600)


def returns_names_lua():
    return ",".join(json.dumps(r["name"]) for r in MIX.get("returns", []))


def returns_job():
    """mvt3 c06: create or refresh the return tracks (after every instrument track). The FX chain is pasted verbatim from
    the template's chunk file into the track's state chunk (an existing return keeps its receives: only its FXCHAIN block
    is replaced); volume from fader_db; master send on."""
    rets = MIX.get("returns") or []
    if not rets:
        return None
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import fxchunk   # mvt2 c44 (the finale's c07 tools/fxchunk.py): edits of the return chunks; imported here because
    # stem_fix.py / state_check.py exec this file's head without __file__
    rows, want = [], {}
    for r in rets:
        fxc = open(r["chunk"] if os.path.isabs(r["chunk"]) else f"{_EW_DIR}/ho-mix-chunks/{r['chunk']}").read().strip("\n")
        # mvt3 c07 (finale tools, ported mvt2 c44): "set" changes values of the Spaces II processor JSON (tools/fxchunk.py;
        # e.g. "impulseA" / "impulseB" / "delay" for another hall, or the IR envelope "irSetup"), "hp_hz" sets band 0 (the
        # high pass) of the return's ReaEQ. Both are read back from REAPER after the paste
        if r.get("set") or r.get("hp_hz"):
            fxc, want[r["name"]] = fxchunk.edit_fxchain(fxc, r.get("set"), r.get("hp_hz"))
        # mvt2 c44 (EW-TEMPLATE-PLAN section 9, darker hall tail): "post_eq" [bands] adds a ReaEQ after Spaces II, loaded
        # from a ReaEQ chunk like the family EQ (set_family_eq; read back), e.g. a 2.3 kHz low pass on the return's tail
        peq = fam_eq_lua({"family_eq": r.get("post_eq")}) if r.get("post_eq") else "nil"
        rows.append(f'{{n={json.dumps(r["name"])}, vol={10 ** (float(r.get("fader_db", 0.0)) / 20):.6f}, peq={peq}, fxc=[==[{fxc}]==]}}')
    lua = ENV_LUA + f"""
local out = {{}}
local function strip_fxchain(ch)
  local lines, keep, depth = {{}}, {{}}, 0
  for l in (ch .. "\\n"):gmatch("(.-)\\n") do lines[#lines + 1] = l end
  local skipping = false
  for _, l in ipairs(lines) do
    local t = l:match("^%s*(.-)%s*$")
    if not skipping and t:sub(1, 8) == "<FXCHAIN" then skipping = true; depth = 1
    elseif skipping then
      if t:sub(1, 1) == "<" then depth = depth + 1 elseif t == ">" then depth = depth - 1 end
      if depth == 0 then skipping = false end
    else keep[#keep + 1] = l end
  end
  return table.concat(keep, "\\n")
end
for _, r in ipairs({{{",".join(rows)}}}) do
  local tr = R.track_by_name(r.n)
  if not tr then
    reaper.InsertTrackAtIndex(reaper.CountTracks(0), false)
    tr = reaper.GetTrack(0, reaper.CountTracks(0) - 1)
    reaper.GetSetMediaTrackInfo_String(tr, "P_NAME", r.n, true)
  end
  local _, ch = reaper.GetTrackStateChunk(tr, "", false)
  ch = strip_fxchain(ch)
  local i = ch:find(">%s*$")
  ch = ch:sub(1, i - 1) .. r.fxc .. "\\n>\\n"
  local okc = reaper.SetTrackStateChunk(tr, ch, false)
  reaper.SetMediaTrackInfo_Value(tr, "D_VOL", r.vol)
  reaper.SetMediaTrackInfo_Value(tr, "D_PAN", 0)
  reaper.SetMediaTrackInfo_Value(tr, "B_MAINSEND", 1)
  local peq = set_family_eq(tr, r.peq)   -- mvt2 c44: post_eq (nil: none)
  local fxn = {{}}
  local fxs = {{}}
  for j = 0, reaper.TrackFX_GetCount(tr) - 1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, j, ""); fxn[#fxn + 1] = nm
    local _, st = reaper.TrackFX_GetNamedConfigParm(tr, j, "vst_chunk"); fxs[#fxs + 1] = st
  end
  out[#out + 1] = {{ name = r.n, ok = okc, idx = reaper.GetMediaTrackInfo_Value(tr, "IP_TRACKNUMBER"), fx = fxn,
                    receives = reaper.GetTrackNumSends(tr, -1), states = fxs, post_eq = peq }}
end
return out
"""
    p = f"{JOBS}/90_returns.lua"
    open(p, "w").write(lua)
    res = run(p)
    # mvt3 c07 (finale): read-back of the edited states (Spaces II "set" keys; ReaEQ band 0 Hz); mvt2 c44: string values
    # (impulses) compared as strings, and the post_eq read-back
    import base64
    for o in res or []:
        sts = o.pop("states", None) or []
        r = next(x for x in rets if x["name"] == o["name"])
        bad = []
        if r.get("post_eq"):
            pe = o.get("post_eq") or {}
            if not pe or pe.get("bad") or not pe.get("ok"):
                bad.append(f"post_eq {pe}")
        if want.get(o["name"]):
            for nm, st in zip(o["fx"], sts):
                raw = fxchunk.strip_reaper_header(base64.b64decode(st)) if st else b""
                if "Spaces" in nm and r.get("set"):
                    js = fxchunk.spaces_json(raw)
                    flat = fxchunk.flat_set(r["set"])
                    got = dict(js.get("irSetup", {}), **{k: v for k, v in js.items() if not isinstance(v, dict)})
                    for k, v in flat.items():
                        g_ = got.get(k)
                        if isinstance(v, str):
                            if g_ != v:
                                bad.append(f"{k} {g_!r} != {v!r}")
                        elif g_ is None or abs(float(g_) - float(v)) > 1e-6:
                            bad.append(f"{k} {g_!r} != {v!r}")
                    o["spaces_read"] = {k: got.get(k) for k in flat}
                if "ReaEQ" in nm and r.get("hp_hz") and "spaces_read" not in o and "eq_band0_read" not in o:
                    b0 = fxchunk.reaeq_bands(raw)[0]
                    o["eq_band0_read"] = [b0[0], round(b0[2], 2)]
                    if b0[0] != 4 or abs(b0[2] - float(r["hp_hz"])) > 0.01:
                        bad.append(f"ReaEQ band 0 {b0}")
        o["readback_bad"] = bad
        if bad:
            sys.exit(f"returns read-back mismatch {o['name']}: {bad}")
    return res


def mix_job():
    rows = []
    for tr in d["tracks"]:
        if ONLY and tr["name"] not in ONLY:
            continue
        m = mix_for(tr["name"])
        rows.append(f'{{n={json.dumps(tr["name"])}, pan={track_pan(m)}, w={track_width(m)}, vol={10 ** (m["gain_db"] / 20):.6f}, env={lua_list(vol_points(tr), ["qn", "db"])}, eq={eq_lua(m)}, meq={mute_lua(m)}, ss={side_lua(m)}, feq={fam_eq_lua(m)}, sends={sends_lua(m)}}}')
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
    local feq = set_family_eq(tr, r.feq)   -- mvt3 c06
    local sends = set_sends(tr, r.sends, {{{returns_names_lua()}}})
    done[#done + 1] = r.n
    if #eq > 0 then done[#done + 1] = eq end
    if feq then done[#done + 1] = feq end
    done[#done + 1] = sends
  end
end
return {{ set = done }}
"""
    p = f"{JOBS}/95_mix.lua"
    open(p, "w").write(lua)
    return run(p)


print(json.dumps({"returns": returns_job()}), flush=True)   # mvt3 c06: before any track sends to them
if MIX_ONLY:
    print(json.dumps(mix_job()))
    sys.exit(0)
if (not ONLY and not MIDI_ONLY) or TEMPO:
    print(json.dumps(tempo_job()))
# c50 (ONE_TIME; mvt1 c52, scherzo c09): a --midi-only build keeps the Opus state REAPER loaded from the saved project,
# and after an instance has played that state can hold runtime values (legato sustain-group AHDSR attacks at 20 ms
# instead of the written ones). --midi-only decodes the saved project (tools/state_guard.py) and fully rebuilds every
# track whose saved attacks differ from its jobs/NN_*.b64, also when it is not listed. render_cycle.py refuses to
# render a project that still holds one.
STALE = set()
if MIDI_ONLY and "--no-stale-guard" not in sys.argv[3:]:
    import glob as _glob
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import state_guard as _sg
    _root = os.path.dirname(os.path.dirname(os.path.abspath(PARTS)))
    _rpps = sorted(_glob.glob(f"{_root}/*.rpp"))
    if _rpps:
        STALE = _sg.stale_tracks(_rpps[0], d, JOBS)
        print(f"state_guard on {os.path.basename(_rpps[0])}: stale {sorted(STALE) or 'none'}", flush=True)
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY and tr["name"] not in STALE:
        continue
    if MIDI_ONLY:
        bf = b64_path(i, tr)
        if tr["name"] in STALE:
            print(f"{tr['name']}: saved Opus state is stale (state_guard: AHDSR attacks differ), full rebuild", flush=True)
            res = track_job(i, tr)
        elif os.path.exists(bf) and open(bf).read() == state_for(tr):
            res = midi_job(i, tr)
        else:
            print(f"{tr['name']}: Opus state changed, full rebuild", flush=True)
            res = track_job(i, tr)
    else:
        res = track_job(i, tr)
    print(json.dumps(res), flush=True)

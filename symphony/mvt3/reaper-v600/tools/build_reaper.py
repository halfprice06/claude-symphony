"""Build a score mockup (parts.json from score_to_parts.py) in a running REAPER through the file bridge (~/.rpr-bridge).

Usage: python build_reaper.py <parts.json> <jobs-dir> [--mix-only] [--midi-only [--tempo]] [--pass2] [track names...]
  mvt1 c39: --pass2 builds the "pass": 2 tracks (and, with no track names, the tempo map) into the open second project;
  without it those tracks are left out.
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
import bisect, json, math, os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import opus_state
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fxchunk   # mvt3 c07

PARTS, JOBS = sys.argv[1], sys.argv[2]
MIX_ONLY = "--mix-only" in sys.argv[3:]
MIDI_ONLY = "--midi-only" in sys.argv[3:]   # c07: see midi_job
TEMPO = "--tempo" in sys.argv[3:]   # c08: with --midi-only, rewrite the tempo map first
# mvt1 c39: --pass2 builds only the parts.json tracks marked "pass": 2 (score_to_parts.py PASS2_TRACKS) into the open
# project, which must be the second REAPER project (reaper_ctl.py --pass2); without it those tracks are skipped, so the
# main project never holds them. Everything else (tempo map, pre-roll, mix.json, shared hall) is the same code
PASS2 = "--pass2" in sys.argv[3:]
ONLY = set(a for a in sys.argv[3:] if a not in ("--mix-only", "--midi-only", "--tempo", "--pass2"))
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
    r = m.get("return")
    if not r or not MIX.get("returns"):
        return "{}"
    return f'{{{{to={json.dumps(r["to"])}, vol={10 ** (float(r["db"]) / 20):.6f}}}}}'


def track_pan(m):
    return float(m.get("track_pan", 0.0))


def track_width(m):
    """mvt3 c09 (critic C #2): mix.json "track_width" (group or track, default 1.0): REAPER's stereo-pan width (D_WIDTH,
    I_PANMODE 5) after the plugin, so a section sounds as a narrower source at its track_pan; the post-fader sends feed the
    halls from the narrowed signal."""
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
  if math.abs(q - p.qn) > 1e-3 then bad[#bad + 1] = {{want = p.qn, got = q}} end
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
    # mvt1 c45 (critic C #1 step 2, Opus manual p.139; ported mvt3 c04): "width_by_mic" {mic label: width} widens the
    # listed mics (never narrows: the larger of the track width and the mic's); the Close mic keeps the track width and
    # anchors the seat, the recorded Main pair spreads (after the drier hall the master's L/R correlation rose)
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
        # mvt3 c01 (from mockup-kit, 2026-11-07; Dan: too wet, mushy): low cut on the hall input only (same Bandpass,
        # keys lowFilterFreq / lowCutFreq; the factory value is 30 Hz), so the bass reaches the hall less
        rv["filterActive"] = True
        rv["lowFilterFreq"] = rv["lowCutFreq"] = float(MIX["reverb"]["low_cut_hz"])
    # mvt3 c03 (copied from mockup-kit/pipeline/build_reaper.py, Movement I c44; Dan: too wet, mushy): the IR envelope
    # ("IR Envelope Preprocessing", Opus manual pp. 133-134) is the ConvolutionReverb's "irSetup" dict (class
    # ConvolutionSetup: envelopeMode, simpleDecay, startPos, endPos, attackLength, decayLength, attackCurve, decayCurve;
    # every installed patch ships envelopeMode 0, simpleDecay 1.0, endPos 1.0). simpleDecay changes nothing in any mode;
    # endPos with decayLength shortens the tail in mode 1 or 2. reverb.ir_setup {key: value} sets it on the shared hall;
    # a track's own "reverb_ir_setup" (mix.json track or group) overrides it. Unknown keys stop the build
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
    is ignored. Load and enable every articulation the track uses, and give its trigger a key (as the loaded rows have)."""
    want = {a.lower() for a in used if a}
    rows = inst["layerMatrix"]["rows"]
    # c24 (A #4, BRIEF rule 7): unload the default rows the track never plays (the RRx9/RRx16 shorts, Sus Accent, ...),
    # to cut REAPER's sample memory. Only when at least one wanted row exists (the harp patches keep their single row).
    unload = UNLOAD_UNUSED_ROWS and any(r["name"].lower() in want for r in rows)
    for row in rows:
        if row["name"].lower() in want:
            row["loaded"] = True
            row["active"] = True
            # mvt3 c16: mix.json "row_volume_db" {track: {row: dB}}: the row's own volume knob in the patch (manual
            # p.137; layerMatrix.rows[].volume, 1.0 = 0 dB), for level differences between articulation rows
            if row_vol and row["name"] in row_vol:
                row["volume"] = round(10 ** (float(row_vol[row["name"]]) / 20), 4)
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
_rg_shared = set()


def region_gain(inst, spec, name):
    """mvt3 c17 (the scherzo's c15 tool, ported; coordinator's note on ruling 4a): mix.json "region_gain_db" (per track)
    {"rows": [row names or prefixes], "pitch_db": {"39": 6.0, ...}}: multiply the per-region `volume` (linear; absent
    = 1) of every region on a listed row whose key range holds a listed pitch by 10^(dB/20), so a per-pitch level
    correction is made inside Opus, at every dynamic (CC11 is flat above 114 on the string rows, so a weak pitch
    cannot be raised there at ff)."""
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    # mvt3 c19: row prefixes match without case (the EH KS Master names its row "Sus Max"); "all_db": every region of
    # the rows (a row level: the row's own volume knob did nothing in Movement II's test); "groups": only sample groups
    # whose name contains one of these strings (one round-robin take: "rrx2")
    pre = tuple(x_.lower() for x_ in (spec.get("rows") or ()))
    want = {i for i, r in enumerate(rows) if not pre or r.lower().startswith(pre)}
    pd_ = {int(k): float(v) for k, v in spec.get("pitch_db", {}).items()}
    n_ = 0
    for g in inst.get("groups", []):
        if spec.get("groups") and not any(x_ in str(g.get("name", "")) for x_ in spec["groups"]):
            continue
        for r_ in (g.get("regionMap") or {}).get("regions", []):
            if r_.get("row") not in want:
                continue
            if spec.get("all_db") is not None:
                r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (float(spec["all_db"]) / 20.0)
                n_ += 1
            # mvt3 c20 (critic A #4): a region whose key range holds several listed pitches (one sample shared by two
            # keys, e.g. the celli pizzicato take rrx2: 47 / 48, 43 / 44) takes the mean of their values; it took the
            # first listed pitch only, so 48's +5.8 never applied. Unequal values on one region are reported
            # (default "shared": "first", the old rule, so the tables fitted on it keep their values: the oboes' E5 / F5
            # and D5 / E flat 5 share regions; "shared": "mean" takes the mean; unequal values are reported either way)
            hit_ = [d_ for p_, d_ in pd_.items() if r_.get("keyMin", -1) <= p_ <= r_.get("keyMax", -1)]
            if hit_:
                d_ = sum(hit_) / len(hit_) if spec.get("shared") == "mean" else hit_[0]
                r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (d_ / 20.0)
                n_ += 1
                if max(hit_) - min(hit_) > 0.5:
                    _rg_shared.add((name, r_.get("keyMin"), r_.get("keyMax"), tuple(sorted(hit_))))
    for w_ in sorted(x_ for x_ in _rg_shared if x_[0] == name):
        print(f"WARNING {name}: region keys {w_[1]}-{w_[2]} shared by listed pitches with values {w_[3]}: {spec.get('shared', 'first')} applied",
              file=sys.stderr)
    print(f"{name}: region gain on {n_} regions", file=sys.stderr)


def cap_release(inst, spec, name):
    """mvt1 c21 (critic A #1): mix.json "sus_release_cap_ms" {"ms", "dyn": [...], "rows": [...]}: cap the AHDSR release
    of the sustain sample groups of the listed rows (default "Sus MAX") whose name ends in one of the listed dynamics
    (default mf/f/ff). A group belongs to a row when every region of its region map sits on that layerMatrix row.
    Release-trail groups ("... RT"), legato transitions ("TLeg") and the soft layers keep their release. The Hollywood
    Strings KS Masters ship 524-931 ms on the Sus MAX sustain groups (Celli mf/f/ff 524, Basses mf 700, Violas mf
    394-653) against 100-237 ms on the legato rows, so rests and cut-offs on Sus MAX did not stop.
    mvt1 c22 (critic A #4): optional "rt_ms" caps the release-trail ("RT") groups of the same rows and dynamics as well
    (the Violas KS Master's Sus MAX RT groups ship 1660 ms, 1st Violins 1245-1741, Celli/Basses 131-166)."""
    # mvt3 c05 (critic C #1, BRIEF soft-endings warning): "ms" may be a number or a dict keyed by the group's dynamic
    # word ({"pp": 500, "p": 500, "mf": 300, "f": 150, "ff": 150}); a dynamic missing from the dict keeps its release
    ms_map = spec["ms"] if isinstance(spec["ms"], dict) else None
    ms = None if ms_map is not None else float(spec["ms"])
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
        ms_ = ms if ms_map is None else ms_map.get(words[-1])
        if ms_ is not None:
            ms_ = float(ms_)
        if words[-1] == "RT" and spec.get("rt_ms") is not None and len(words) >= 2 and words[-2] in dyns:
            ms_ = float(spec["rt_ms"])   # mvt1 c22 (critic A #4): the release-trail groups of the listed dynamics too
        elif spec.get("any_dyn") and ms_map is None and "TLeg" not in nm and words[-1] != "RT":
            # mvt3 c20 (critic A #1): every non-RT, non-legato-transition group of the rows, whatever its name (the
            # basses' "Stac On Bow RRx9" groups are "Db Stac Hrd rrx1" and "release extension": no dynamic word)
            pass
        elif "TLeg" in nm or words[-1] == "RT" or words[-1] not in dyns or ms_ is None:
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            # mvt3 c21 (critic A c21 #3): "set": true also raises a shorter release to ms (the trumpets' f / ff sustain
            # groups ship 178 ms and stop dead between +0.15 and +0.20 s; trombones / horns keep 237 ms)
            if pr_.get("class") == "AHDSR" and (pr_.get("release", 0) > ms_ or (spec.get("set") and abs(pr_.get("release", 0) - ms_) > 0.5)):
                hit.setdefault(nm, set()).add(round(pr_["release"]))
                pr_["release"] = ms_
    if (name, json.dumps(spec, sort_keys=True)) not in _CAP_PRINTED:
        _CAP_PRINTED.add((name, json.dumps(spec, sort_keys=True)))
        ms_txt = json.dumps(ms_map) if ms_map is not None else f"{ms:.0f}"
        print(f"{name}: release cap {ms_txt} ms (RT {spec.get('rt_ms')}) on {sorted((k, sorted(v)) for k, v in hit.items())}", file=sys.stderr)


def cap_attack(inst, spec, name):
    """mvt3 c22 (critic A #3b): mix.json "attack_cap_ms" (a spec or a list) {"ms", "rows": [row names], "groups": [group name
    prefixes]}: cap the AHDSR attack of the sample groups of those rows whose name (round-robin suffix removed) starts
    with a listed prefix followed by a space. The woodwind KS Masters fade the legato target's sustain groups in over
    440-738 ms ("1Fls", "OBs", "EHs", "Cls" 553, "Bss" 438) under a transition sample of about 0.5 s, so the sum dips
    6-13 dB 0.1-0.4 s after a legato note-on."""
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if r in spec.get("rows", ["Leg Slur MAX"])}
    pre = tuple(g_ + " " for g_ in spec.get("groups", []))
    hit = {}
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if not regs or any(r_.get("row") not in want for r_ in regs):
            continue
        nm = g["name"].split(" rr")[0].split(" RR")[0].strip()
        if pre and not nm.startswith(pre):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "AHDSR" and pr_.get("attack", 0) > float(spec["ms"]):
                hit.setdefault(nm, set()).add(round(pr_["attack"]))
                pr_["attack"] = float(spec["ms"])
    print(f"{name}: attack cap {spec['ms']} ms on {sorted((k, sorted(v)) for k, v in hit.items())}", file=sys.stderr)


def tleg_env(inst, spec, name):
    """mvt3 c23 (critic C #4a): mix.json "tleg_env" {"rows": [row names], "hold_ms", "decay_ms"}: set the AHDSR hold and/or
    decay of the legato-transition sample groups ("TLeg" in the group name) of those rows. The woodwind KS Masters' TLeg
    groups hold 264-412 ms and decay 177-237 ms to sustain 0.001 (Flute 1: sustain 1.0, never faded), while the target's
    connected sustain group fades in over 440-738 ms: the transition is gone before the sustain is up (holes 0.1-0.45 s
    after a legato note-on)."""
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if r in spec.get("rows", ["Leg Slur MAX", "Leg Slur"])}
    hit = {}
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if "TLeg" not in str(g.get("name", "")) or not regs or any(r_.get("row") not in want for r_ in regs):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "AHDSR":
                hit.setdefault((round(pr_.get("hold", 0)), round(pr_.get("decay", 0)), pr_.get("sustain")), 0)
                hit[(round(pr_.get("hold", 0)), round(pr_.get("decay", 0)), pr_.get("sustain"))] += 1
                if spec.get("hold_ms") is not None:
                    pr_["hold"] = float(spec["hold_ms"])
                if spec.get("decay_ms") is not None:
                    pr_["decay"] = float(spec["decay_ms"])
    print(f"{name}: TLeg envelope hold {spec.get('hold_ms')} / decay {spec.get('decay_ms')} ms on "
          f"{sum(hit.values())} groups (shipped hold, decay, sustain: {sorted(hit)})", file=sys.stderr)


def vel_volume(inst, spec, name):
    """mvt3 c22 (critic B #1): mix.json "vel_volume" {"from": patch path}: copy the Global Group's MidiVelocity processor
    and its "Velocity -> Source/volume" connection (with its rescaler table) from another patch into this one. The Harp KS
    Master has no velocity-to-volume path (its Global Group modulates Source/volume from CC11 only), while Harp Sus RR has
    both connections on Source/volume (sensitivity 0, a square-law table): on the KS Master velocity picks only the
    layer, so p plucks came out 8-9 dB too loud and ff 3.5 dB too soft (c21)."""
    src = opus_state.load_oib(spec["from"])
    sg = next(g for g in src["groups"] if g.get("type") == 0 or g.get("name") == "Global Group")
    dg = next(g for g in inst["groups"] if g.get("type") == 0 or g.get("name") == "Global Group")
    sp, dp = sg["processors"], dg["processors"]
    proc = next(p for p in sp["processors"] if p.get("class") == "MidiVelocity")
    conn = [c for c in sp.get("connections", []) if c.get("source", "").startswith("Midi Velocity/")]
    if any(p.get("class") == "MidiVelocity" for p in dp["processors"]):
        print(f"{name}: vel_volume: the patch already has a MidiVelocity processor; left alone", file=sys.stderr)
        return
    dp["processors"].insert(1, json.loads(json.dumps(proc)))
    dp.setdefault("connections", []).extend(json.loads(json.dumps(c)) for c in conn)
    print(f"{name}: vel_volume: MidiVelocity and {len(conn)} connection(s) copied from {os.path.basename(spec['from'])}", file=sys.stderr)


def state_for(tr):
    inst = opus_state.load_oib(tr["patch"])
    if "articulations" in inst:
        load_articulations(inst, list(tr["art_counts"]) + [tr["first_art"]], (MIX.get("row_volume_db") or {}).get(tr["name"]))
    if "articulations" in inst and (MIX.get("tracks", {}).get(tr["name"]) or {}).get("ks_keys"):
        # mvt3 c21 (critic A c21 #4): mix.json "ks_keys" {articulation: key} moves a trigger to another key, and
        # "ks_unused_off": true takes the key off every trigger the track does not use. The Harp KS Master's triggers sit
        # on keys 21-35, where the harp itself plays (26-35 in the Finale): Harmonics (29) and Gliss Technique (27) move
        # above the harp's range; build/ks_maps_extra.json holds the same keys for score_to_parts.py
        mt_ = MIX["tracks"][tr["name"]]
        used_ = {a.lower() for a in list(tr["art_counts"]) + [tr["first_art"]] if a}
        for trig in inst["articulations"].get("trigger", []):
            if trig["name"] in mt_["ks_keys"]:
                trig["key"] = int(mt_["ks_keys"][trig["name"]])
                trig["triggerName"] = NOTE_NAMES[trig["key"] % 12] + str(trig["key"] // 12 - 2)
            if mt_.get("ks_unused_off") and trig["name"].lower() not in used_:
                trig["useKey"] = False
        print(f"{tr['name']}: keyswitch keys {[(t_['name'], t_['key'], t_.get('useKey')) for t_ in inst['articulations'].get('trigger', []) if t_.get('useKey')]}", file=sys.stderr)
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
        # mvt3 c20: a list of specs (different rows, different caps)
        for sp_ in (m_["sus_release_cap_ms"] if isinstance(m_["sus_release_cap_ms"], list) else [m_["sus_release_cap_ms"]]):
            cap_release(inst, sp_, tr["name"])
    if m_.get("channel_map") is not None:
        # mvt3 c19 (critic B #4): mix.json "channel_map" (track): Opus Channel Routing (manual p.141; the instrument's
        # "channelMap": 0 Stereo, then Mono, Mono From Left, Mono From Right, Swap in the manual's order)
        inst["channelMap"] = int(m_["channel_map"])
    if m_.get("region_gain_db"):   # mvt3 c17; c18: one spec or a list of specs (different rows, different tables)
        rg_ = m_["region_gain_db"]
        for spec_ in (rg_ if isinstance(rg_, list) else [rg_]):
            region_gain(inst, spec_, tr["name"])
    if m_.get("vel_volume"):
        vel_volume(inst, m_["vel_volume"], tr["name"])
    if m_.get("attack_cap_ms"):
        for sp_ in (m_["attack_cap_ms"] if isinstance(m_["attack_cap_ms"], list) else [m_["attack_cap_ms"]]):
            cap_attack(inst, sp_, tr["name"])
    if m_.get("tleg_env"):   # mvt3 c23
        tleg_env(inst, m_["tleg_env"], tr["name"])
    if m_.get("bandpass"):
        # mvt3 c01 (critic C #5): mix.json "bandpass" {"rows": [...], "low_hz", "high_hz"}: the "Bandpass Filter"
        # processors of the sample groups of the listed rows (every row when "rows" is absent). The 1TP KS Master's mute
        # rows ship a fixed 90 Hz-3 kHz bandpass on every layer (read from the .oib), so the con sordino trumpet came out
        # 18 dB darker above 5 kHz than the open trumpet
        bp_ = m_["bandpass"]
        rows_ = [r["name"] for r in inst["layerMatrix"]["rows"]]
        want_ = {i for i, r in enumerate(rows_) if "rows" not in bp_ or r in bp_["rows"]}
        nbp_ = 0
        for g in inst.get("groups", []):
            regs = (g.get("regionMap") or {}).get("regions", [])
            if not regs or any(r_.get("row") not in want_ for r_ in regs):
                continue
            for pr_ in (g.get("processors") or {}).get("processors", []):
                if pr_.get("class") == "Bandpass":
                    pr_["low"], pr_["high"] = float(bp_["low_hz"]), float(bp_["high_hz"])
                    nbp_ += 1
        print(f"{tr['name']}: bandpass {bp_['low_hz']}-{bp_['high_hz']} Hz on {nbp_} groups", file=sys.stderr)
    if m_.get("legato_speed"):
        # mvt1 c41 (critic C #1): mix.json "legato_speed" {PARAM: value}: parameters of the KS Master's "LegatoSpeed"
        # EventFilterScript (Hollywood Strings: velocity VELO_MIN..VELO_MAX -> transition sample start START_MIN..START_MAX
        # samples; RELEASE ms; BUMPRED; read from the .oib). Unknown parameter names stop the build
        ls_ = [f_ for f_ in inst.get("filters", []) if f_.get("name") == "LegatoSpeed"]
        if not ls_:
            sys.exit(f"{tr['name']}: legato_speed set but the patch has no LegatoSpeed script")
        for k_, v_ in m_["legato_speed"].items():
            if k_.startswith("_"):
                continue
            if k_ not in ls_[0]:
                sys.exit(f"{tr['name']}: LegatoSpeed has no parameter {k_!r}")
            ls_[0][k_] = type(ls_[0][k_])(v_)
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
# mvt3 c27 (critic A #2a, B #4, ruling 1): inside a held decrescendo the trim no longer rises at all (0.5 left the
# stopped horns at 548 / 668 flat or swelling through a printed decrescendo: Horn 4 +5.9 dB, Horn 1 -0.7 dB); the trim
# returns at the next note-on as before. env BUILD_DECRESC_KEEP overrides
SOFT_DECRESC_KEEP = float(os.environ.get("BUILD_DECRESC_KEEP", "0.0"))
# mvt3 c27 (critic B #5, ruling 1; Dan, 11 Nov: no per-note move in the track volume envelope): mix.json
# "dyn_trim_to_cc7" {"tracks": "all" or [names], "except": [names], "families_except": [families]} moves the dynamic
# trims (dyn_trim_db / soft_trim_db read from the printed dynamic curve, with every hold above) out of the volume
# envelope into CC7 (inside Opus; CC7 is 20 log10(CC7 / 127), manual p.64 / p.151, measured on the string patches in
# Finale c26): the envelope holds gain + vol_db + the track's largest trim, and CC7 = the lane's own CC7 x
# 10^((trim - largest) / 20), on the same grid, held in rests like the envelope's tail hold. A --mix-only build does not
# rewrite CC7: after a trim change use --midi-only. Off when the key is absent
TRIM_CC7 = {}
TRIM_CC7_ONSET_QN, TRIM_CC7_ONSET_PRE = 0.15, 0.003   # mvt3 c28: see the trim lane in vol_points (None = off)
TRIM_CC7_FAMILIES_EXCEPT = ("timp", "perc", "harp", "harm")
# mvt3 c29 (ruling 8, critic A c29 #6): a trim change point that lands up to TRIM_CC7_LEG_PRE_QN before a moved note-on
# while another note of the track still sounds across it (a legato overlap: celli 951.48 -4.7 dB, basses 951.78 -4.2,
# 25-40 ms before the led 952) changed the old note's last tens of ms: it moves to TRIM_CC7_LEG_POST qn after that
# note-on (the old note keeps its level to the join; the new note's first ms at the old level is inaudible). None = off
TRIM_CC7_LEG_PRE_QN, TRIM_CC7_LEG_POST, TRIM_CC7_LEG_MIN_DB = 0.1, 0.003, 1.0   # only steps of 1 dB or more (not ramps)
TRIM_CC7_LEG_MAX_OV = 0.12   # a held voice that rings on past the new note-on by more than this (a chord's other voice) keeps the step before it
# mvt3 c29 (ruling 7): the highest value the volume envelope may hold (see vol_points); None = off
ENV_MAX_DB = 23.5
ENV_SHIFTED = {}


def trim_cc7_on(tr):
    spec = MIX.get("dyn_trim_to_cc7")
    if not spec or tr.get("family") in spec.get("families_except", TRIM_CC7_FAMILIES_EXCEPT):
        return False
    if tr["name"] in spec.get("except", []):
        return False
    t = spec.get("tracks", "all")
    return t == "all" or tr["name"] in t
# mvt1 c36 (critic C #1, Dan's listening note on bar 62): this envelope comes after the Opus hall, so a subito fall of
# 11-16 dB at the mark cut the forte's hall tail at once (master -14.5 dB in 0.2 s, flat after: "sounds like a glitch";
# a natural cut-off here falls about 7 dB by 0.1-0.2 s and 11 dB by 0.2-0.3 s). At each parts.json `subito_falls` entry
# [mark, fall qn] (score_to_parts SUBITO_FRESH: the fall qn is the moved onset of the track's note on the mark): the
# level before the fall is held to the fall qn; a track that sounded in the `sounded_s` before it then falls
# `at_once_db` at once and the rest linearly in dB over `ramp_s` (never under the level after the mark); a smaller fall
# (or a silent track) moves to the fall qn. None = off
SUBITO_TAIL = {"at_once_db": 4.0, "ramp_s": 0.35, "sounded_s": 0.5, "min_db": 0.5}
SUBITO_SILENT_QN = 0.05   # mvt1 c42: a track with no note on the mark or across it holds its level instead (see the loop)
LEADIN_HOLD = "alias"     # mvt1 c42: see vol_points
# mvt3 c16 (B #6, C #6): the mirror of SOFT_DECRESC_HOLD for crescendos. Where the dynamic trims fall with a rising
# dynamic (Clarinet 2 fff -6 against ff 0), the envelope fell across a printed crescendo and the stem did not rise (18 of
# 393 crescendos). Inside each crescendo, from its start to the first note-on after its end, the trim may rise but falls
# only by CRESC_TRIM_KEEP of its fall under its value at the hairpin's start. None = off. Only on listed crescendos (see vol_points)
CRESC_TRIM_KEEP = 0.5
DYN_LIN_IN_HAIRPINS = True
# mvt3 c16 (Dan, 11 Nov: the volume lane showed peaks and valleys on every note): THIN_DB drops every envelope point
# that the line through its kept neighbours misses by less than this many dB (the line is checked in dB and in a
# fourth-root amplitude scale, the two shapes REAPER's volume envelope scalings can take, on the seconds axis REAPER
# interpolates on). 53.7k points -> about 34k with the same curve. None = off (env BUILD_THIN=0)
THIN_DB = 0.1 if os.environ.get("BUILD_THIN", "1") != "0" else None


def thin_points(pts, tol):
    """pts [(seconds, dB)] ascending -> indexes kept (Ramer-Douglas-Peucker on the vertical error)."""
    n = len(pts)
    if n < 3:
        return list(range(n))
    k4 = math.log(10) / 80.0
    keep = [False] * n
    keep[0] = keep[-1] = True
    stack = [(0, n - 1)]
    while stack:
        a, b = stack.pop()
        if b - a < 2:
            continue
        (xa, ya), (xb, yb) = pts[a], pts[b]
        fa, fb = math.exp(k4 * ya), math.exp(k4 * yb)
        worst, wi = 0.0, None
        for i in range(a + 1, b):
            x, y = pts[i]
            u = (x - xa) / (xb - xa) if xb > xa else 0.0
            e = max(abs(ya + (yb - ya) * u - y), abs(math.log(max(1e-12, fa + (fb - fa) * u)) / k4 - y))
            if e > worst:
                worst, wi = e, i
        if wi is not None and worst > tol:
            keep[wi] = True
            stack += [(a, wi), (wi, b)]
    return [i for i in range(n) if keep[i]]


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
    # mvt3 c16: parts.json "vol_lin": vol_db is piecewise linear between its points (ramps drawn as ramps, not as a
    # stair of grid steps); its points join the grid
    vlin = bool(tr.get("vol_lin"))
    if vlin:
        grid = sorted(set(grid) | {q for q, _ in vol if 0 <= q < grid[-1]})
        vq_, vv_ = [p_[0] for p_ in vol], [p_[1] for p_ in vol]

        def vol_at(q):
            k = bisect.bisect_right(vq_, q + 1e-9)
            if k <= 0:
                return vv_[0] if vv_ else 0.0
            if k >= len(vq_):
                return vv_[-1]
            return vv_[k - 1] + (vv_[k] - vv_[k - 1]) * (q - vq_[k - 1]) / max(1e-12, vq_[k] - vq_[k - 1])
    else:
        vol_at = lambda q: step_at(vol, q)
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
            c0 = step_at(dyn, h0, first)
            if c0 > SOFT_DECRESC_HOLD_MAX_CC:
                continue
            # up to the moved onset of the first note whose score onset is at or after the hairpin's end
            e_ = next((mq_ for sq_, mq_ in ons_ if sq_ >= h1 - 1e-6), h1 + 1.0)
            holds.append((h0, e_, trim(c0), SOFT_DECRESC_KEEP))
    choldS = []
    # (simulated on the c15 stems for every crescendo: 104 hairpins would change by 1.5-5.6 dB and in 63 the hairpin's
    # end would stand over the arrival, so the hold acts only on the crescendos listed in mix.json "cresc_trim_hold"
    # {track: [[from_qn, to_qn], ...]}: hairpins that start inside a listed span)
    csp_ = (MIX.get("cresc_trim_hold") or {}).get(tr["name"], [])
    if dyn and CRESC_TRIM_KEEP is not None and csp_:
        ons_ = sorted((n.get("sq", n["qn"]), n["qn"]) for n in tr.get("notes", []))
        for h0, h1, k_ in tr.get("hairpins", []):
            if k_ != "cresc" or not any(a_ - 1e-6 <= h0 < b_ for a_, b_ in csp_):
                continue
            e_ = next((mq_ for sq_, mq_ in ons_ if sq_ >= h1 - 1e-6), h1 + 1.0)
            choldS.append((h0, e_, trim(step_at(dyn, h0, first)), CRESC_TRIM_KEEP))

    # mvt3 c16: inside a printed hairpin the dynamic curve is read as a line between its points (DYN_LIN_IN_HAIRPINS),
    # so the trims move as a ramp and not as a stair of 0.2-0.4 dB steps that the thinning cannot join
    hp_sp_ = [(h0, h1) for h0, h1, _ in tr.get("hairpins", [])] if DYN_LIN_IN_HAIRPINS else []
    dq_ = [p_[0] for p_ in dyn]

    def dyn_at(q):
        if not any(a_ + 1e-6 < q < b_ - 1e-6 for a_, b_ in hp_sp_):
            return step_at(dyn, q, first)
        k = bisect.bisect_right(dq_, q + 1e-9)
        if k <= 0 or k >= len(dq_):
            return step_at(dyn, q, first)
        (q0_, c0_), (q1_, c1_) = dyn[k - 1][:2], dyn[k][:2]
        if q1_ - q0_ > 2.0 or abs(c1_ - c0_) > 6:   # a hold or a jump: not part of the ramp
            return c0_
        return c0_ + (c1_ - c0_) * (q - q0_) / max(1e-9, q1_ - q0_)

    def trim_at(q):
        t_ = trim(dyn_at(q))
        for a_, b_, cap_, keep_ in holds:
            if a_ - 1e-9 <= q < b_ - 1e-9 and t_ > cap_:
                t_ = cap_ + keep_ * (t_ - cap_)
        for a_, b_, flo_, keep_ in choldS:
            if a_ - 1e-9 <= q < b_ - 1e-9 and t_ < flo_:
                t_ = flo_ + keep_ * (t_ - flo_)
        return t_
    val_at = lambda q: round(g + vol_at(q) + (trim_at(q) if dyn else 0.0), 2)
    c7m = bool(dyn) and trim_cc7_on(tr)   # mvt3 c27: DYN_TRIM_TO_CC7 (see TRIM_CC7)
    tl = None
    if c7m:
        tv_ = [trim_at(q) for q in grid]
        tmax_ = max(tv_)
        val_at = lambda q: round(g + vol_at(q) + tmax_, 2)
        tl = [round(t_ - tmax_, 2) for t_ in tv_]
    vals = [val_at(q) for q in grid]
    # mvt1 c42: lead-in hold. Before a track's first note the envelope holds the value at that note's moved onset, so
    # the written envelope does not ramp across the onset from an unrelated earlier level. An alias track (parts.json
    # "alias_of") has its source's whole vol_db / dyn curve but only its windows' notes, and a soft-decrescendo trim hold
    # that ended at the source's next note ran on to the alias's first note (f62 aliases: 2.3 / 3.5 dB lower over the
    # first 0.09 qn). LEADIN_HOLD: "alias" (alias tracks only), "all", or None
    if tr.get("notes") and (LEADIN_HOLD == "all" or (LEADIN_HOLD == "alias" and tr.get("alias_of"))):
        q0_ = min(n["qn"] for n in tr["notes"])
        v0_ = val_at(q0_)
        vals = [v0_ if q < q0_ - 1e-6 else v for q, v in zip(grid, vals)]
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
        tl0_ = list(tl) if tl is not None else None

        def tl_at(q):   # the trim lane (CC7 mode) before the holds, as a step on the grid
            k_ = bisect.bisect_right(grid, q + 1e-9) - 1
            return tl0_[max(0, k_)]
        for e_, n_ in rests:
            if (e_, n_) == last_rest:
                ve_ = val_at(e_ - 0.002)
                te_ = tl_at(e_ - 0.002) if tl is not None else None
                for k, q in enumerate(grid):
                    if q >= e_ - 1e-6 and vals[k] != ve_:
                        vals[k] = ve_
                        held += 1
                    if tl is not None and q >= e_ - 1e-6:
                        tl[k] = te_
                continue
            if e_ >= TAIL_HOLD_STOP_QN or q2s(n_) - q2s(e_) < TAIL_HOLD_MIN_S:
                continue
            nh_ = s2q(q2s(n_) - TAIL_HOLD_LEAD_S)
            ve_ = val_at(e_ - 0.002)   # the level the last note ended at
            te_ = tl_at(e_ - 0.002) if tl is not None else None
            for k, q in enumerate(grid):
                if e_ - 1e-6 <= q < nh_ and vals[k] != ve_:
                    vals[k] = ve_
                    held += 1
                if tl is not None and e_ - 1e-6 <= q < nh_:
                    tl[k] = te_
    if tl is not None:   # mvt3 c27: the CC7 trim lane (score qn, dB <= 0), changes only
        chg_ = [(q, t_) for k, (q, t_) in enumerate(zip(grid, tl)) if k == 0 or t_ != tl[k - 1]]
        # mvt3 c28 (coordinator, scherzo c25): the lane changes on its grid (0.125 qn), so a trim step for a led note
        # landed 10-45 ms after the moved note-on (Horn 1 744 played its first 20 ms 12.5 dB low, Clarinet 1 720 40 ms
        # 8.3 dB low). A change point within TRIM_CC7_ONSET_QN after a moved note-on (with no other note-on between)
        # moves to TRIM_CC7_ONSET_PRE qn before that note-on: trims read on moved time
        if TRIM_CC7_ONSET_QN and tr.get("notes"):
            ons_ = sorted({round(n["qn"], 5) for n in tr["notes"]})
            out_ = []
            for k, (q, t_) in enumerate(chg_):
                j_ = bisect.bisect_left(ons_, q + 1e-9) - 1
                if k > 0 and j_ >= 0 and q - ons_[j_] <= TRIM_CC7_ONSET_QN and ons_[j_] - TRIM_CC7_ONSET_PRE > out_[-1][0] + 1e-4:
                    q = ons_[j_] - TRIM_CC7_ONSET_PRE
                elif k > 0 and TRIM_CC7_LEG_PRE_QN and j_ + 1 < len(ons_) and 0 < ons_[j_ + 1] - q <= TRIM_CC7_LEG_PRE_QN \
                        and any(n_["qn"] < q - 1e-6 and n_["qn"] + n_["dur"] > ons_[j_ + 1] - 1e-6 for n_ in tr["notes"]) \
                        and not any(n_["qn"] < q - 1e-6 and n_["qn"] + n_["dur"] > ons_[j_ + 1] + TRIM_CC7_LEG_MAX_OV for n_ in tr["notes"]) \
                        and abs(t_ - chg_[k - 1][1]) >= TRIM_CC7_LEG_MIN_DB \
                        and (k + 1 >= len(chg_) or chg_[k + 1][0] > ons_[j_ + 1] + TRIM_CC7_ONSET_QN):
                    q = ons_[j_ + 1] + TRIM_CC7_LEG_POST   # mvt3 c29: see TRIM_CC7_LEG_PRE_QN
                out_.append((round(q, 5), t_))
            chg_ = out_
        TRIM_CC7[tr["name"]] = chg_
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
            # mvt1 c42 (critic C #1): a track that is silent at the mark (no note starts within SUBITO_SILENT_QN of
            # it and none sounds across it; e.g. an alias that plays only the forte, its last note ending at the mark)
            # does not fall: the level before is held from fs_ until TAIL_HOLD_LEAD_S before its next moved onset (or
            # to the end), so its last note rings under the subito as a release would
            silent_ = (not any(abs(n.get("sq", n["qn"]) - s_) < SUBITO_SILENT_QN for n in tr.get("notes", []))
                       and not any(n["qn"] < s_ - SUBITO_SILENT_QN and n["qn"] + n["dur"] > s_ + SUBITO_SILENT_QN
                                   for n in tr.get("notes", [])))
            if silent_:
                nxt_ = [n["qn"] for n in tr.get("notes", []) if n["qn"] > s_ - 1e-6]
                h_end = s2q(q2s(min(nxt_)) - TAIL_HOLD_LEAD_S) if nxt_ else grid[-1] + 1.0
                if h_end > fs_:
                    vals = [pre if fs_ - 1e-6 <= q < h_end else v for q, v in zip(grid, vals)]
                    old_map = dict(zip(grid, vals))
                    grid = sorted(set(grid) | {round(fs_, 5), round(fs_ - 0.002, 5)})
                    vals = [old_map[q] if q in old_map else (pre if q >= fs_ - 1e-6 else cur(q)) for q in grid]
                continue
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
    # mvt1 c42: parts.json "vol_post" (score_to_parts POST_SHAPES_S): shapes added after the tail hold and SUBITO_TAIL
    def lin_(xs, ys, q):   # piecewise linear, xs ascending
        k = bisect.bisect_left(xs, q)
        if k <= 0:
            return ys[0]
        if k >= len(xs):
            return ys[-1]
        return ys[k - 1] + (ys[k] - ys[k - 1]) * (q - xs[k - 1]) / max(1e-12, xs[k] - xs[k - 1])
    for sh_ in tr.get("vol_post", []):
        xs_, ds_ = [p_[0] for p_ in sh_], [p_[1] for p_ in sh_]
        G0, V0 = list(grid), list(vals)   # the written envelope is linear between its points: new points keep that line
        grid = sorted(set(grid) | {round(x_, 5) for x_ in xs_ if 0 <= x_ < grid[-1]})
        vals = [round(lin_(G0, V0, q) + (lin_(xs_, ds_, q) if xs_[0] <= q <= xs_[-1] else 0.0), 2) for q in grid]
    # mvt3 c29 (coordinator's ruling 7; critics A / B / C c29): REAPER's volume envelope stops at +24 dB, and Horn 3 reached
    # exactly +24.0 (Trombone 1 23.6, Tuba 23.5) with no margin. ENV_MAX_DB: with the trims in CC7 (dyn_trim_to_cc7) the
    # excess x over it comes off the whole envelope and goes into the CC7 trim lane (+x, level-neutral, CC7 is
    # 20 log10 inside Opus); where the trim lane is within x of 0 dB (CC7 cannot exceed 127) the remainder stays in the
    # envelope at that point. Any envelope still over ENV_MAX_DB fails the build
    if ENV_MAX_DB is not None and vals and max(vals) > ENV_MAX_DB + 1e-6:
        x_ = round(max(vals) - ENV_MAX_DB, 2)
        chg7_ = TRIM_CC7.get(tr["name"]) if c7m else None
        if chg7_:
            cq_ = [c_[0] for c_ in chg7_]

            def t7_(q):
                k_ = bisect.bisect_right(cq_, q + 1e-9) - 1
                return chg7_[max(0, k_)][1]
            vals = [round(v - x_ + max(0.0, t7_(q) + x_), 2) for q, v in zip(grid, vals)]
            TRIM_CC7[tr["name"]] = [(q, round(min(0.0, t_ + x_), 2)) for q, t_ in chg7_]
            ENV_SHIFTED[tr["name"]] = x_
        if max(vals) > ENV_MAX_DB + 0.01:
            raise SystemExit(f"{tr['name']}: volume envelope {max(vals):.2f} dB over ENV_MAX_DB {ENV_MAX_DB} (REAPER stops at +24)")
    out = []
    for k, (q, v) in enumerate(zip(grid, vals)):
        if k == 0 or k == len(vals) - 1 or v != vals[k - 1] or v != vals[k + 1]:
            out.append({"qn": q + PRE, "db": v})
    if THIN_DB:
        kept_ = thin_points([(q2s(p_["qn"] - PRE), p_["db"]) for p_ in out], THIN_DB)
        out = [out[i_] for i_ in kept_]
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
RR_RESET_SKIP_FAMILIES = {"harp", "harm"}   # harp tracks were already bit-identical render to render
REP_OFF_FAMILIES = {"string"}
PRE_RR_RESET = True   # mvt3 c14: CC16 (rr_reset_cc) 127 at RR_RESET_QN on every track that gets the CC36 reset


def cc7_lane(tr):
    """mvt3 c27: parts.json cc7 (a step lane, 127 when empty) times the DYN_TRIM_TO_CC7 trim lane (vol_points first)"""
    base = sorted((float(q), int(v)) for q, v in tr.get("cc7", []))
    tl = TRIM_CC7.get(tr["name"])
    if not tl:
        return [tuple(c) for c in base]
    bq = [q for q, _ in base]

    def b_at(q):
        k = bisect.bisect_right(bq, q + 1e-9) - 1
        return base[k][1] if k >= 0 else 127
    tq = [q for q, _ in tl]

    def t_at(q):
        k = bisect.bisect_right(tq, q + 1e-9) - 1
        return tl[k][1] if k >= 0 else tl[0][1]
    out = []
    for q in sorted(set(bq) | set(tq)):
        v = int(round(max(1, min(127, b_at(q) * 10 ** (t_at(q) / 20)))))
        if not out or out[-1][1] != v:
            out.append((round(q, 4), v))
    return out


def item_lua(tr):
    """The MIDI item (notes, keyswitches, CCs), volume envelope and ReaEQ for track variable `tr` (Lua)."""
    m = mix_for(tr["name"])
    notes = lua_list([dict(n, qn=round(n["qn"] + PRE, 4)) for n in tr["notes"]], ["qn", "dur", "pitch", "vel"])
    ks_rows = [{"qn": round(k["qn"] + PRE, 4), "pitch": k["pitch"]} for k in tr["ks"]]
    if PRE and tr["first_ks"] is not None:   # c06: the first articulation is also selected in the pre-roll
        ks_rows.insert(0, {"qn": 0.25, "pitch": tr["first_ks"]})
    ks = lua_list(ks_rows, ["qn", "pitch"])
    vpts = lua_list(vol_points(tr), ["qn", "db"])   # mvt3 c27: first, so TRIM_CC7 is filled
    ccs = []
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, cc7_lane(tr)), (70, tr.get("cc70", [])),
                     (36, tr.get("cc36", []))):   # mvt1 c14 (A #2): round-robin resets inside the music
        ccs += [{"qn": round(q + PRE, 4), "cc": num, "v": v} for q, v in lane]
        if PRE and lane:   # c06: each lane's first value is sent in the pre-roll too
            ccs.append({"qn": 0.25, "cc": num, "v": lane[0][1]})
    # mvt3 c08 (MANUAL-GAPS #6): round-robin resets inside the music on Opus's reset controller (parts.json "cc16",
    # "rr_reset_cc"); not repeated in the pre-roll, so the rest of the track keeps its round-robin sequence
    ccs += [{"qn": round(q + PRE, 4), "cc": int(tr.get("rr_reset_cc", 16)), "v": v} for q, v in tr.get("cc16", [])]
    if PRE and tr["family"] not in RR_RESET_SKIP_FAMILIES:
        # c24 (A #3): reset Opus's round-robin state (CC36, any value) at the start of every render, and on the strings
        # turn the Repetition script off (CC69 0-63 = OFF, HO manual CC table), so renders are reproducible
        ccs.append({"qn": RR_RESET_QN, "cc": 36, "v": 127})
        # mvt3 c14 (critic A #4, manual p.145; Movement I c43, Movement II c45): the reset Opus itself listens to
        # (Preferences.json RoundRobinResetCC, parts.json "rr_reset_cc") in the pre-roll of every track, so a render
        # does not start from the round-robin position the last playback left
        if PRE_RR_RESET and int(tr.get("rr_reset_cc", 16)) != 36:
            ccs.append({"qn": RR_RESET_QN, "cc": int(tr.get("rr_reset_cc", 16)), "v": 127})
        if tr["family"] in REP_OFF_FAMILIES:
            ccs.append({"qn": RR_RESET_QN, "cc": 69, "v": 0})
    ccs = lua_list(ccs, ["qn", "cc", "v"])
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
reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", {track_width(mix_for(tr['name']))})   -- mvt3 c09: mix.json track_width
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


def return_ride_points(fader_db):
    """mvt3 c16 (A #5, B #5, C #5): mix.json "return_rides": tail-only rides of the return faders, so a tutti stop that
    falls too fast keeps more of its hall ring without any send or return level change elsewhere. Rows:
    {"stop": score qn of the cut-off, "db": lift} (0 dB until 0.05 s before the stop, the lift from 0.05 s after it, held
    "hold_s" (0.9), back to 0 dB "rel_s" (0.3) later or 0.05 s before the next note-on of any track, whichever is first)
    or {"pts": [[score qn, dB], ...]} (a drawn shape, 0 dB outside). Returns the envelope points (fader_db + ride), the
    same on every return, or None when no ride is listed."""
    rides = MIX.get("return_rides") or []
    if not rides:
        return None
    ons = sorted({n["qn"] for tr in d["tracks"] for n in tr.get("notes", [])})
    pts = []
    for r in rides:
        if "pts" in r:
            pts += [(float(q_), float(v_)) for q_, v_ in r["pts"]]
            continue
        t0 = q2s(float(r["stop"]))
        nx = next((q2s(q_) for q_ in ons if q_ > float(r["stop"]) + 0.02), 1e9)
        t3 = min(t0 + float(r.get("hold_s", 0.9)) + float(r.get("rel_s", 0.3)), nx - 0.05)
        t2 = min(t0 + float(r.get("hold_s", 0.9)), t3 - 0.1)
        if t2 <= t0 + 0.06:
            sys.exit(f"return_rides {r}: no room before the next note-on")
        pts += [(s2q(t0 - 0.05), 0.0), (s2q(t0 + 0.05), float(r["db"])), (s2q(t2), float(r["db"])), (s2q(t3), 0.0)]
    pts.sort()
    if any(b_[0] <= a_[0] for a_, b_ in zip(pts, pts[1:])):
        sys.exit(f"return_rides overlap: {pts}")
    out = [{"qn": 0.0, "db": fader_db}] + [{"qn": round(q_ + PRE, 4), "db": round(fader_db + v_, 2)} for q_, v_ in pts]
    return out + [{"qn": round(d["end_qn"] + PRE + 8, 4), "db": fader_db}]


def returns_job():
    """mvt3 c06: create or refresh the return tracks (after every instrument track). The FX chain is pasted verbatim from
    the template's chunk file into the track's state chunk (an existing return keeps its receives: only its FXCHAIN block
    is replaced); volume from fader_db; master send on."""
    rets = MIX.get("returns") or []
    if not rets:
        return None
    rows, want = [], {}
    for r in rets:
        fxc = open(r["chunk"] if os.path.isabs(r["chunk"]) else f"{_EW_DIR}/ho-mix-chunks/{r['chunk']}").read().strip("\n")
        # mvt3 c07 (critic C #1, B #1): "set" changes values of the Spaces II processor JSON (Movement I's
        # template_mix.spaces_set, ported in tools/fxchunk.py; e.g. the IR envelope "irSetup"), "hp_hz" sets band 0 (the
        # high pass) of the return's ReaEQ. Both are read back from REAPER after the paste
        if r.get("set") or r.get("hp_hz"):
            fxc, want[r["name"]] = fxchunk.edit_fxchain(fxc, r.get("set"), r.get("hp_hz"))
        # mvt3 c08 (critic C #2): a return may carry "side_shelf" (the track key's list form): the M/S side EQ after its FX
        rp_ = return_ride_points(float(r.get("fader_db", 0.0)))
        env_ = lua_list(rp_, ["qn", "db"]) if rp_ else "nil"
        rows.append(f'{{n={json.dumps(r["name"])}, vol={10 ** (float(r.get("fader_db", 0.0)) / 20):.6f}, env={env_}, ss={side_lua(r)}, fxc=[==[{fxc}]==]}}')
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
  local envn = nil
  if r.env then envn = set_vol_env(tr, r.env) end   -- mvt3 c16: return_rides (the envelope carries the fader level)
  reaper.SetMediaTrackInfo_Value(tr, "D_PAN", 0)
  reaper.SetMediaTrackInfo_Value(tr, "B_MAINSEND", 1)
  local sseq = {{}}
  set_side_shelf(tr, r.ss, sseq)   -- mvt3 c08 (C #2)
  local fxn = {{}}
  local fxs = {{}}
  for j = 0, reaper.TrackFX_GetCount(tr) - 1 do
    local _, nm = reaper.TrackFX_GetFXName(tr, j, ""); fxn[#fxn + 1] = nm
    local _, st = reaper.TrackFX_GetNamedConfigParm(tr, j, "vst_chunk"); fxs[#fxs + 1] = st
  end
  out[#out + 1] = {{ name = r.n, ok = okc, idx = reaper.GetMediaTrackInfo_Value(tr, "IP_TRACKNUMBER"), fx = fxn,
                    receives = reaper.GetTrackNumSends(tr, -1), states = fxs, side = sseq, env_points = envn }}
end
return out
"""
    p = f"{JOBS}/90_returns.lua"
    open(p, "w").write(lua)
    res = run(p)
    # mvt3 c07: read-back of the edited states (Spaces II irSetup and the other "set" keys; ReaEQ band 0 Hz)
    import base64
    for o in res or []:
        sts = o.pop("states", None) or []
        w = want.get(o["name"])
        if not w:
            continue
        r = next(x for x in rets if x["name"] == o["name"])
        bad = []
        seen_eq = False   # mvt3 c08: only the first ReaEQ is the return's own (a later one is the side-shelf EQ)
        for nm, st in zip(o["fx"], sts):
            raw = fxchunk.strip_reaper_header(base64.b64decode(st)) if st else b""
            if "Spaces" in nm and r.get("set"):
                js = fxchunk.spaces_json(raw)
                flat = fxchunk.flat_set(r["set"])
                got = dict(js.get("irSetup", {}), **{k: v for k, v in js.items() if not isinstance(v, dict)})
                bad += [f"{k} {got.get(k)!r} != {v!r}" for k, v in flat.items() if abs(float(got.get(k, -1e9)) - float(v)) > 1e-6]
                o["spaces_read"] = {k: got.get(k) for k in flat}
            if "ReaEQ" in nm and seen_eq:
                continue
            if "ReaEQ" in nm:
                seen_eq = True
            if "ReaEQ" in nm and r.get("hp_hz"):
                b0 = fxchunk.reaeq_bands(raw)[0]
                o["eq_band0_read"] = [b0[0], round(b0[2], 2)]
                if b0[0] != 4 or abs(b0[2] - float(r["hp_hz"])) > 0.01:
                    bad.append(f"ReaEQ band 0 {b0}")
        o["readback_bad"] = bad
        if bad:
            sys.exit(f"returns read-back mismatch {o['name']}: {bad}")
    return res


def in_pass(tr):
    """mvt1 c39: the track belongs to the pass being built (--pass2: only "pass": 2 tracks; else only the others)"""
    return (tr.get("pass", 1) == 2) == PASS2


def mix_job():
    rows = []
    for tr in d["tracks"]:
        if (ONLY and tr["name"] not in ONLY) or not in_pass(tr):
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


if not PASS2:
    print(json.dumps({"returns": returns_job()}), flush=True)   # mvt3 c06: before any track sends to them
if MIX_ONLY:
    print(json.dumps(mix_job()))
    sys.exit(0)
if (not ONLY and not MIDI_ONLY) or TEMPO:
    print(json.dumps(tempo_job()))
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY:
        continue
    if not in_pass(tr):
        if ONLY:
            print(f"{tr['name']}: skipped (pass {tr.get('pass', 1)}; {'without' if PASS2 else 'with'} --pass2)", flush=True)
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

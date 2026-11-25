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
mvt1 c50: EastWest's template mix (loop/TEMPLATE-PLAN.md; tools/TEMPLATE-TOOLS.md): per-mic levels and pans
("mic_db", "pan_by_mic"), REAPER track pan ("reaper_pan"), Opus reverb off ("opus_reverb_off"), REAPER return tracks
loaded from the template's chunks with post-fader sends ("returns", "send_profiles", "send_profile"), and a family EQ
("family_eqs", "family_eq"). Each is off unless its mix.json key is present (see the block above item_lua).
"""
import bisect, json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import opus_state

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

COLORS = {"perc": (160, 140, 100), "wind": (90, 160, 90), "brass": (210, 170, 60), "timp": (150, 110, 80), "harp": (170, 120, 200), "harm": (170, 120, 200), "string": (70, 110, 200)}


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


def mic_volumes(m, name=None):
    """The loaded mics and their Opus volumes (linear) for apply_mix: {label: volume}, or None for the patch's own mics.
    mvt1 c50 (TEMPLATE-PLAN section 1): mix.json "mic_db" {label: dB} (group or track) gives the levels in dB, as the
    EastWest template lists them (opus-mics.txt: Close 0 dB / Main -4.7 dB on the flute KS Master); the listed mics are
    loaded, the others unloaded, as with "mics". "mic_db" wins over "mics", except that a track's own "mics" (with no
    "mic_db" of its own) wins over its group's "mic_db" (Cello solo's DIV A patch has only a Close mic); a track's
    "mic_db": null falls back to "mics". Without "mic_db" anywhere this is the c49 rule: m["mics"]."""
    t_ = MIX["tracks"].get(name, {}) if name is not None else {}
    if "mics" in t_ and "mic_db" not in t_:
        return t_["mics"]
    if m.get("mic_db") is not None:
        return {k_: 10 ** (float(v_) / 20.0) for k_, v_ in m["mic_db"].items() if not k_.startswith("_")}
    return m.get("mics")


def opus_reverb_off(m):
    """mvt1 c50 (TEMPLATE-PLAN section 2): mix.json "opus_reverb_off" (top level, or a group / track overriding it):
    every Opus reverb send level 0, the fx:0 channel volume 0, and no ConvolutionReverb in fx:0 (the shared hall is not
    loaded). The hall then comes from the REAPER return tracks ("returns", "send_profile")."""
    return bool(m["opus_reverb_off"] if "opus_reverb_off" in m else MIX.get("opus_reverb_off", False))


def apply_mix(inst, m, name=None):
    chans = inst["mixer"]["channels"]
    subs = {c["label"]: c for c in chans if c["channelId"].startswith("sub:")}
    cols = {c["name"]: c for c in inst["layerMatrix"]["columns"]}
    mics_ = mic_volumes(m, name)   # mvt1 c50: "mic_db" (dB) or "mics" (linear)
    if mics_ is not None:
        for label, c in subs.items():
            on = label in mics_
            c["loaded"] = on
            if label in cols:
                cols[label]["loaded"] = on
            if on:
                c["volume"] = mics_[label]
        if m.get("mic_db") is not None and mics_ is not m.get("mics"):
            miss_ = [k_ for k_ in mics_ if k_ not in subs]
            if miss_:
                print(f"{name}: mic_db names mics the patch does not have: {miss_} (has {sorted(subs)})", file=sys.stderr)
    off_ = opus_reverb_off(m)   # mvt1 c50
    # mvt1 c50 (TEMPLATE-PLAN section 1): mix.json "pan_by_mic" {mic label: rule} (group or track). "seat": the c05
    # rule below (panLeft / panRight = seat -/+ width, pan 0; width_by_mic still widens); "full": pan 0, panLeft -1,
    # panRight +1 (the template's Main, Mid and Surround: full width, not re-panned); "factory": panLeft -1, panRight +1
    # and the patch's own pan knob (HO's Close pans: 1st Violins -0.31, Celli +0.33, horns -0.25, ... are the template's
    # seats); a number: that pan knob value with panLeft -1, panRight +1. A mic not listed (or no pan_by_mic) is "seat".
    pbm_ = {k_: v_ for k_, v_ in (m.get("pan_by_mic") or {}).items() if not k_.startswith("_")}
    # c05 (C #3): the seat and width are set inside Opus on every mic channel (panLeft/panRight), so the shared hall
    # (fx:0) returns centred at full width instead of being panned and narrowed with the dry sound by the REAPER pan
    # after the plugin. The REAPER track pan is centre, width 1.
    # mvt1 c45 (critic C #1 step 2, Opus manual p.139: each mic sub-mix has its own panning): "width_by_mic" {mic label:
    # width} widens the listed mics (never narrows: the larger of the track width and the mic's); the Close mic keeps the
    # track width and anchors the seat, the recorded Main pair spreads (after the c44 drier hall the master's L/R
    # correlation rose 0.57 -> 0.69, outside all five references)
    wbm_ = {k_: float(v_) for k_, v_ in (m.get("width_by_mic") or {}).items() if not k_.startswith("_")}
    for c in subs.values():
        rule_ = pbm_.get(c["label"], "seat")
        if rule_ == "seat":
            wd_ = max(m["width"], wbm_.get(c["label"], 0.0))
            c["pan"] = 0.0
            c["panLeft"] = max(-1.0, m["seat"] - wd_)
            c["panRight"] = min(1.0, m["seat"] + wd_)
        elif rule_ == "full":
            c["pan"], c["panLeft"], c["panRight"] = 0.0, -1.0, 1.0
        elif rule_ == "factory":
            c["panLeft"], c["panRight"] = -1.0, 1.0
        elif isinstance(rule_, (int, float)) and not isinstance(rule_, bool):
            c["pan"], c["panLeft"], c["panRight"] = float(rule_), -1.0, 1.0
        else:
            sys.exit(f"{name}: pan_by_mic {c['label']}: {rule_!r} (use seat, full, factory or a number)")
        for ins in c["inserts"]:
            if ins["class"] == "SendProcessor" and ins.get("output") == "fx:0":
                if off_:   # mvt1 c50: Opus reverb off
                    ins["level"] = 0.0
                    continue
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
    if off_:   # mvt1 c50: Opus reverb off (see opus_reverb_off)
        fx["volume"] = 0.0
        fx["pan"], fx["panLeft"], fx["panRight"] = 0.0, -1.0, 1.0
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
    # mvt1 c44 (ONE_TIME #3, BRIEF S4): the IR envelope ("IR Envelope Preprocessing", Opus manual pp. 133-134) is the
    # ConvolutionReverb's "irSetup" dict (class ConvolutionSetup: envelopeMode, simpleDecay, startPos, endPos,
    # attackLength, decayLength, attackCurve, decayCurve; factory envelopeMode 0, simpleDecay 1.0, endPos 1.0).
    # reverb.ir_setup {key: value} sets it on the shared hall; a track's own "reverb_ir_setup" (mix.json track or group)
    # overrides it (used for A/B tests of the decay). Unknown keys stop the build
    irs_ = dict(MIX["reverb"].get("ir_setup") or {}, **(m.get("reverb_ir_setup") or {}))
    for k_, v_ in irs_.items():
        if k_.startswith("_"):
            continue
        if k_ not in rv.get("irSetup", {}):
            sys.exit(f"reverb ir_setup: the ConvolutionSetup has no key {k_!r} ({sorted(rv.get('irSetup', {}))})")
        rv["irSetup"][k_] = type(rv["irSetup"][k_])(v_)
    # mvt1 c49 (critic C #1, Opus manual p.220: the reverb insert's Width 0-200 %, stored 0-2, factory 1.0): reverb.width
    # sets the shared hall's stereo width; a track's own "reverb_width" (mix.json track or group) overrides it (A/B tests).
    # Absent = the IR's factory 1.0 (the state is left as loaded)
    wv_ = m.get("reverb_width", MIX["reverb"].get("width"))
    if wv_ is not None:
        if "width" not in rv:
            sys.exit(f"reverb width: the ConvolutionReverb has no 'width' key ({sorted(rv)})")
        rv["width"] = float(wv_)
    fx["inserts"] = [i for i in fx["inserts"] if i["class"] != "ConvolutionReverb"] + [rv]


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


UNLOAD_UNUSED_ROWS = True   # c24 (A #4)


def load_articulations(inst, used):
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
    """mvt1 c21 (critic A #1): mix.json "sus_release_cap_ms" {"ms", "dyn": [...], "rows": [...]} (mvt1 c46: or a list of
    such specs, each applied in turn): cap the AHDSR release
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
    if (name, ms, tuple(sorted(dyns))) not in _CAP_PRINTED:   # mvt1 c46: one line per spec of a list
        _CAP_PRINTED.add((name, ms, tuple(sorted(dyns))))
        print(f"{name}: release cap {ms:.0f} ms (RT {spec.get('rt_ms')}) on {sorted((k, sorted(v)) for k, v in hit.items())}", file=sys.stderr)


def rt_gain(inst, spec, name):
    """mvt1 c45 (critic C #2, HO manual p.222: the room is heard in the release-trail samples): mix.json "rt_gain_db"
    {"db": D, "rows": [...] (default: every row)}: multiply the SourceProcessor volume of every release-trail group
    (`releaseTrail` true) whose regions all sit on the listed rows by 10^(D/20). The KS Masters ship trail gains from
    0.58 (Solo Trumpet) to 3.98 (+12 dB, 1st / 2nd Violins and Violas mf); capping a trail's AHDSR release does nothing,
    because a trail is a one-shot sample (c22 rt_ms)."""
    db_ = float(spec["db"])
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if spec.get("rows") is None or r in spec["rows"]}
    n_ = 0
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if not g.get("releaseTrail") or not regs or any(r_.get("row") not in want for r_ in regs):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "SourceProcessor" and "volume" in pr_:
                pr_["volume"] = float(pr_["volume"]) * 10 ** (db_ / 20.0)
                n_ += 1
    print(f"{name}: release-trail gain {db_:+.1f} dB on {n_} groups", file=sys.stderr)


def region_gain(inst, spec, name):
    """mvt1 c57 (port of scherzo c15; Dan: no per-note volume in the track envelope): mix.json "region_gain_db" (per
    track; one spec or a list) {"rows": [row names] or null (every row), "pitch_db": {"41": -1.5, ...}}: multiply the
    per-region `volume` (linear; absent = 1) of every region on a listed row whose key range holds a listed pitch by
    10^(dB/20): a per-pitch level correction inside Opus (it moves with the note's own sample) in place of the
    pitch trims of the track volume envelope."""
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    n_ = 0
    for sp_ in (spec if isinstance(spec, list) else [spec]):
        want = {i for i, r in enumerate(rows) if sp_.get("rows") is None or r in sp_["rows"]}
        pd_ = {int(k): float(v) for k, v in sp_.get("pitch_db", {}).items()}
        for g in inst.get("groups", []):
            if sp_.get("dyn"):
                # mvt1 c58 (critic B #5): "dyn": only the sample groups of these dynamic layers (the group name's
                # last word, or the word before "RT": "1FH pp", "1FH pp RT")
                w_ = g["name"].split(" rr")[0].split(" RR")[0].split()
                if not w_ or (w_[-2] if w_[-1] == "RT" and len(w_) > 1 else w_[-1]) not in sp_["dyn"]:
                    continue
            for r_ in (g.get("regionMap") or {}).get("regions", []):
                if r_.get("row") not in want:
                    continue
                if sp_.get("all_db") is not None:   # mvt1 c58: a row level (every region of the listed rows)
                    r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (float(sp_["all_db"]) / 20.0)
                    n_ += 1
                for p_, d_ in pd_.items():
                    if r_.get("keyMin", -1) <= p_ <= r_.get("keyMax", -1):
                        r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (d_ / 20.0)
                        n_ += 1
                        break
    print(f"{name}: region gain on {n_} regions", file=sys.stderr)


def state_for(tr):
    inst = opus_state.load_oib(tr["patch"])
    if "articulations" in inst:
        load_articulations(inst, list(tr["art_counts"]) + [tr["first_art"]])
    if tr["first_ks"] is not None and "articulations" in inst:
        inst["articulations"]["currentKeySwitch"] = tr["first_ks"]
    for f in inst.get("filters", []):
        if f.get("name") == "ConSordino" and tr["cc15"]:
            f["conSordino"] = tr["cc15"][0][1] >= 64
    m_ = mix_for(tr["name"])
    apply_mix(inst, m_, tr["name"])
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
        # mvt1 c46 (critic C #1): a list of specs, applied in order (e.g. 150 ms at mf-ff and 350 ms at pp / p)
        caps_ = m_["sus_release_cap_ms"]
        for spec_ in (caps_ if isinstance(caps_, list) else [caps_]):
            cap_release(inst, spec_, tr["name"])
    if m_.get("rt_gain_db"):
        rt_gain(inst, m_["rt_gain_db"], tr["name"])
    if m_.get("region_gain_db"):
        region_gain(inst, m_["region_gain_db"], tr["name"])
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
# mvt1 c56: see the end of vol_points; None = every grid point as before. Slow ramps reach vol_db as 0.25 qn stairs
# (score_to_parts samples them on its grid); within 0.1 dB the thinning turns the small ones back into lines
# (points of all tracks 54000 -> 32600 at 0.1 dB; 0.3 dB gives 22700 and was not taken: the limit agreed is 0.1 dB)
# mvt1 c58 (critic C #2): the dynamic trim, roles and hairpin gain are read at score time, so a level step for a note
# that enters after a rest ended at the score onset, 50-240 ms inside the led note (125 entries with 3 dB or more, 51
# with 6 dB or more; brass entries +9..+15 dB in their first 60 ms). ONSET_KEY = {"min_rest_s", "ramp_s"}: for every
# note whose moved note-on m lies before its score onset s and at least min_rest_s after the end of the notes before
# it, the envelope holds the level the last note ended at until ramp_s before m (or that note's end), reaches the
# value of s at m and holds it to s: the step lies wholly in the rest. Notes joined to the note before (legato
# targets) keep the step on the join. mix.json "onset_key" overrides; None = off
ONSET_KEY = None
DECRESC_RAMP = None    # mvt1 c60: see vol_points (mix.json "decresc_ramp"); None = the held trim steps at the arrival
DECRESC_RAMPS = []     # (track, hairpin start, arrival note-on, trim at the start, trim at the arrival) of the ramps written
ENV_THIN = {"tol_db": 0.75, "max_step_db": 3.0, "max_qn": 16.0}   # mvt1 c59 (critic B #6): 0.5 until c58;   # mvt1 c57: 0.1 / 2.0 / 4.0 until c56 (slow layers only now: points near the reference rate)


# mvt1 c62 (Dan, 2026-11-11: "nuke all the volume adjustments per note"; coordinator c62): a generic last pass on the
# written envelope. c61 had no per-note rule left, but the slow-balance rules (hairpin-gain releases, the
# held-decrescendo trim, role and phrase-row edges, chord cuts, the dynamic trims stepping at printed marks) still made
# 354 fast moves (over 3 dB/s, 1.5 dB or more) inside sounding notes. mix.json "note_slope_guard" (top level; absent =
# off; env ENV_NO_GUARD=1 turns it off for a measurement):
#   {"max_db_s": 2.8, "detect_db_s": 2.9, "min_db": 1.2, "sudden_db_s": 20.0, "sudden_pre_s": 0.03,
#    "sudden_marks": ["sf", "sfz", "fp", "sfp", "sub. p", "sub. pp"], "new_pre_s": 0.35, "new_post_s": 0.15,
#    "rest_lead_s": 0.35, "hairpin_tail_s": 0.3, "step_s": 0.01, "merge_gap_s": 0.25, "passes": 8, "mark_steps": true,
#    "join_max_s": 2.0}
# On the envelope sampled every step_s seconds, every run of samples steeper than detect_db_s whose part inside the
# track's sounding notes (moved note-on to note end) moves min_db or more is rewritten:
#   - at a new note (a moved note-on m from new_pre_s before the run's start to new_post_s after its end):
#       a printed sudden dynamic on that note (sudden_marks in build/mockup-events.tsv, parts.json subito_falls):
#       a sudden_db_s ramp that ends sudden_pre_s before m;
#       otherwise, after a rest: the move lies in the rest (from rest_lead_s before m, or the rest's start) and ends at m;
#       otherwise (the note before still sounds): a max_db_s ramp that ends at m, at most join_max_s long (a larger
#       move stays steeper and is listed in "left");
#       "mark_steps": a printed dynamic that changes the level on the note with no hairpin arriving there counts as
#       a printed sudden dynamic too;
#   - inside a held note: a move in the direction of a printed hairpin that covers it (from the hairpin's start to
#     hairpin_tail_s after its end) becomes one ramp from the hairpin's start (at least as long as max_db_s needs);
#     any other move (a release, a row edge) is held at its start level and goes back to the written course at
#     max_db_s, or in the next rest when the note ends sooner (from rest_lead_s before the next note-on); after the
#     track's last note-on a fall ramps at max_db_s into its written end instead (the final fade)
# A run longer than "ramp_min_s" (0.4 s) is a ramp, not a step: it is made a max_db_s ramp from the start of a printed
# hairpin of its direction that covers it, else one that ends where it ended. Repeated up to "passes" times. Points outside the rewritten stretches are kept as written. The track dict gets
# "_nsg" = {kind: count, "left": [(qn, dB inside), ...]} (left = runs still over min_db after the last pass).
_TA = None
_SUD_EV = None


def _tempo_arr():
    global _TA
    if _TA is None:
        import numpy as np
        qs = sorted({0.0} | {float(tq) for tq, _ in d["tempo"] if tq > 0} | {float(d["end_qn"]) + 1000.0})
        _TA = (np.array(qs), np.array([q2s(q) for q in qs]))
    return _TA


def _sudden_qn(tr, marks, mark_steps=False):
    global _SUD_EV
    if _SUD_EV is None:
        _SUD_EV = {}
        f_ = os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mockup-events.tsv")
        if os.path.exists(f_):
            for ln_ in open(f_):
                x_ = ln_.rstrip("\n").split("\t")
                if len(x_) > 4 and x_[3] == "dynamic":
                    _SUD_EV.setdefault(x_[0], []).append((round(float(x_[1]), 3), x_[4]))
    out = {q_ for st_ in tr.get("staves", []) for q_, v_ in _SUD_EV.get(st_, []) if v_ in marks}
    out |= {round(float(s_), 3) for s_, _f in tr.get("subito_falls", [])}
    if mark_steps:
        # a printed dynamic that changes the level on a note with no hairpin arriving there (ff ... pp, p ... f): the
        # score's own step, as sudden as a subito for the envelope (c62: a 2.4 dB/s ramp into the celli's pp at 286
        # lifted their ff marcato strokes 9 dB, and into the pp unis. at 504 a divisi chord through its decrescendo)
        lv_ = {"ppp": 0, "pp": 1, "p": 2, "mp": 3, "mf": 4, "f": 5, "ff": 6, "fff": 7}
        ends_ = [h1 for _h0, h1, _k in tr.get("hairpins", [])]
        for st_ in tr.get("staves", []):
            prev_ = None
            for q_, v_ in sorted(_SUD_EV.get(st_, [])):
                if v_ not in lv_:
                    continue
                if prev_ is not None and lv_[v_] != lv_[prev_] and not any(q_ - 1.0 <= e_ <= q_ + 0.01 for e_ in ends_):
                    out.add(q_)
                prev_ = v_
    return out


def note_slope_guard(tr, grid, vals, cfg):
    import numpy as np
    R, DET, MIN = cfg.get("max_db_s", 2.8), cfg.get("detect_db_s", 2.9), cfg.get("min_db", 1.2)
    SR, SP = cfg.get("sudden_db_s", 20.0), cfg.get("sudden_pre_s", 0.03)
    NPRE, NPOST = cfg.get("new_pre_s", 0.35), cfg.get("new_post_s", 0.15)
    RL, HT, dt = cfg.get("rest_lead_s", 0.35), cfg.get("hairpin_tail_s", 0.3), cfg.get("step_s", 0.01)
    QB, TB = _tempo_arr()
    G, V = np.asarray(grid, float), np.asarray(vals, float)
    TG = np.interp(G, QB, TB)
    t = np.arange(TG[0], TG[-1] + 1e-9, dt)
    N = len(t)
    v = np.interp(t, TG, V)
    ed = np.zeros(N, bool)
    notes = tr.get("notes", [])
    on = np.interp([n["qn"] for n in notes], QB, TB)
    off = np.interp([n["qn"] + n["dur"] for n in notes], QB, TB)
    tm = t[:-1] + dt / 2
    snd = (np.searchsorted(np.sort(on), tm, "left") - np.searchsorted(np.sort(off), tm, "right")) > 0
    sud_q = _sudden_qn(tr, set(cfg.get("sudden_marks", ["sf", "sfz", "fp", "sfp", "sub. p", "sub. pp"])), cfg.get("mark_steps", False))
    JMAX = cfg.get("join_max_s", 2.0)
    RAMP_S = cfg.get("ramp_min_s", 0.4)
    RHP = cfg.get("hairpin_db_s", R)   # the steepest ramp a printed hairpin's own move may keep
    ons = sorted(set(round(float(x), 4) for x in on))
    sud_on = sorted({round(float(o_), 4) for o_, n in zip(on, notes) if any(abs(n.get("sq", n["qn"]) - s_) < 0.02 for s_ in sud_q)})
    hps = [(float(np.interp(h0, QB, TB)), float(np.interp(h1, QB, TB)), k_) for h0, h1, k_ in tr.get("hairpins", [])]
    ix = lambda x: int(min(N - 1, max(0, round((x - t[0]) / dt))))
    stats = {"sudden": 0, "new_rest": 0, "new_join": 0, "hairpin": 0, "held_hold": 0, "held_rest": 0, "final": 0}
    accepted = set()
    joined_m = {}

    GAP = max(1, int(round(cfg.get("merge_gap_s", 0.25) / dt)))

    def runs():
        dv = np.diff(v)
        s_ = np.where(np.abs(dv) / dt >= DET, np.sign(dv), 0.0)
        br = np.flatnonzero(np.diff(s_) != 0) + 1
        starts, ends = np.r_[0, br], np.r_[br, len(s_)]
        rs_ = [[int(a_), int(b_), s_[a_]] for a_, b_ in zip(starts, ends) if s_[a_] != 0]
        # runs of one sign with a short still gap between them are one move: a ramp that the lanes write as 0.25 qn
        # stairs (a step every other grid point) is steep only in pieces, but ENV_THIN draws it as one steep line
        mg_ = []
        for r_ in rs_:
            if mg_ and r_[2] == mg_[-1][2] and r_[0] - mg_[-1][1] <= GAP and \
                    np.all(dv[mg_[-1][1]:r_[0]] * r_[2] >= -0.02) and \
                    abs(v[r_[1]] - v[mg_[-1][0]]) / max(dt, t[r_[1]] - t[mg_[-1][0]]) >= DET:
                mg_[-1][1] = r_[1]
            else:
                mg_.append(list(r_))
        out = []
        for a_, b_, _sg in mg_:
            ins = float(np.abs(dv[a_:b_][snd[a_:b_]]).sum())
            if ins >= MIN:
                out.append((a_, b_, ins))
        return out

    def put(i0, i1, f):
        i0, i1 = max(0, i0), min(N - 1, i1)
        if i1 < i0:
            return
        v[i0:i1 + 1] = [f(x) for x in t[i0:i1 + 1]]
        ed[max(0, i0 - 1):min(N, i1 + 2)] = True

    def ramp(s0, te, v0, v1, hold_from=None):
        """from s0 (level v0) linearly to te (level v1); hold_from: hold v0 from there to s0 first"""
        L = max(dt, te - s0)
        a0 = s0 if hold_from is None else min(hold_from, s0)
        return a0, (lambda x: v0 if x < s0 else (v0 + (v1 - v0) * min(1.0, (x - s0) / L)))

    for _pass in range(cfg.get("passes", 8)):
        # a run inside a written sudden ramp is that ramp (a later pass must not move it to another note)
        acc_in = lambda a_, b_: any(a_ >= x0 - 3 and b_ <= x1 + 3 for x0, x1 in accepted)
        rs = [r_ for r_ in runs() if not acc_in(r_[0], r_[1])]
        if not rs:
            break
        for k0, k1, ins in rs:
            a, b = t[k0], t[k1]
            va, vb = v[k0], v[k1]
            D = vb - va
            if abs(D) < 1e-6:
                continue
            hp = [h for h in hps if h[0] - 0.05 <= a <= h[1] + HT and ((h[2] == "cresc" and D > 0) or (h[2] != "cresc" and D < 0))]
            if b - a > RAMP_S:
                # a ramp, not a step (a steep stretch of a printed hairpin's rise, or runs merged across stairs): from the
                # hairpin's start when one covers it, else a max_db_s ramp that ends where it ended
                Rr = RHP if hp else R
                s0 = hp[0][0] if hp else b - abs(D) / Rr
                for _it in range(4):
                    v0 = v[ix(s0)]
                    if abs(vb - v0) / max(dt, b - s0) <= Rr:
                        break
                    s0 = b - abs(vb - v0) / Rr
                a0, f = ramp(s0, b, v0, vb)
                put(ix(a0), k1, f)
                stats["ramp"] = stats.get("ramp", 0) + 1
                continue
            cand = [m for m in ons if a - NPRE <= m <= b + NPOST]
            if cand:
                m = min(cand, key=lambda x: abs(x - 0.5 * (a + b)))
                if any(abs(m - s_) < 0.005 for s_ in sud_on):
                    te = m - SP
                    s0 = te - abs(D) / SR
                    v0 = v[ix(s0)] if s0 < a else va
                    a0, f = ramp(s0, te, v0, vb, hold_from=a)
                    put(ix(a0), ix(max(b, te)), f)
                    accepted.add((ix(s0), ix(te)))
                    stats["sudden"] += 1
                    continue
                prev_snd = snd[max(0, ix(m) - 3):max(1, ix(m) - 1)].any()
                if not prev_snd:
                    k_ = ix(m) - 2
                    while k_ > 0 and not snd[k_ - 1] and t[k_] > m - RL:
                        k_ -= 1
                    s0 = max(t[k_], m - RL)
                    te = m - 0.005
                    if te - s0 < dt:
                        s0 = te - dt
                    v0 = v[ix(s0)] if s0 < a else va
                    a0, f = ramp(s0, te, v0, vb, hold_from=a)
                    put(ix(a0), ix(max(b, m)), f)
                    stats["new_rest"] += 1
                else:
                    # the step only is spread: the written course under it is kept and the step's size is added as
                    # a ramp that ends at m (overwriting [s0, m] with a straight line lifted a rising trim course up to
                    # 5.7 dB above itself, Violins II 489-496); at most join_max_s
                    # at most three times per note-on: unbounded passes walked the ramps back across a printed
                    # decrescendo (Violins II f62 231-236 +4 dB)
                    if joined_m.get(round(m, 3), 0) >= 3:
                        continue
                    joined_m[round(m, 3)] = joined_m.get(round(m, 3), 0) + 1
                    L = min(abs(D) / R, JMAX)
                    s0 = m - L
                    vv = v.copy()

                    def f(x, s0=s0, L=L, a=a, b=b, D=D, vv=vv):
                        ox = float(np.interp(x, t, vv))
                        ex = ox if x < a else (float(np.interp(a, t, vv)) if x < b else ox - D)   # the course without the step
                        return ex + D * min(1.0, max(0.0, (x - s0) / L))
                    put(ix(min(s0, a)), ix(max(b, m)), f)
                    stats["new_join"] += 1
                continue
            if hp:
                s0 = hp[0][0]
                v0 = v[ix(s0)]
                if abs(vb - v0) / max(dt, b - s0) > R:
                    s0 = b - abs(vb - v0) / R
                    v0 = v[ix(s0)]
                a0, f = ramp(s0, b, v0, vb)
                put(ix(a0), k1, f)
                stats["hairpin"] += 1
                continue
            later = [m for m in ons if m > b + NPOST]
            if not later:
                s0 = b - abs(D) / R
                v0 = v[ix(s0)]
                a0, f = ramp(s0, b, v0, vb)
                put(ix(a0), k1, f)
                stats["final"] += 1
                continue
            L = abs(D) / R
            k_ = k1
            while k_ < N - 1 and snd[k_] and t[k_] < b + L:
                k_ += 1
            if k_ < N - 1 and not snd[k_] and t[k_] < b + L:
                rho = t[k_]
                nx = min(m for m in ons if m > rho - 1e-6) if any(m > rho - 1e-6 for m in ons) else rho + 1.0
                te = nx - 0.005
                s0 = max(rho, nx - RL)
                if te - s0 < dt:
                    s0 = te - dt
                v1 = v[ix(te)]
                put(k0, ix(te), lambda x, s0=s0, te=te, v1=v1, va=va: va if x < s0 else va + (v1 - va) * (x - s0) / max(dt, te - s0))
                stats["held_rest"] += 1
            else:
                e_ = ix(b + L)
                vv = v.copy()
                put(k0, e_, lambda x, b=b, L=L, va=va, vb=vb: va if x <= b else float(np.interp(x, t, vv)) + (va - vb) * max(0.0, 1 - (x - b) / L))
                stats["held_hold"] += 1
    acc_in = lambda a_, b_: any(a_ >= x0 - 3 and b_ <= x1 + 3 for x0, x1 in accepted)
    left = [(round(float(np.interp(t[a_], TB, QB)), 3), round(i_, 1)) for a_, b_, i_ in runs() if not acc_in(a_, b_)]
    stats["left"] = left
    tr["_nsg"] = stats
    if not ed.any():
        return grid, vals
    # keep the written points outside the rewritten stretches, the samples inside them
    TGq = np.interp(t, TB, QB)
    keep = [(float(q_), float(v_)) for q_, v_, tg_ in zip(G, V, TG) if not ed[ix(tg_)]]
    keep += [(round(float(TGq[k_]), 5), round(float(v[k_]), 2)) for k_ in np.flatnonzero(ed)]
    keep.sort()
    out_q, out_v = [], []
    for q_, v_ in keep:
        if out_q and q_ <= out_q[-1] + 1e-6:
            continue
        out_q.append(q_); out_v.append(v_)
    return out_q, out_v


# mvt1 c63 (coordinator c63, Dan approved 2026-11-18): note_slope_guard "mode": "relocate". c62's guard reached 0 fast
# moves inside held notes but shifted whole phrases by up to 15 dB against c61 (cycles/c62/NET-LEVEL-CHECK.md): its
# held moves returned at max_db_s or "in the next rest" far later, its join ramps ran up to 2 s back three times per
# note-on, and hairpin ramps were limited to hairpin_db_s. This mode takes each fast move out as a unit and puts the same
# size back elsewhere, so the written course outside the move's own note is unchanged (written course minus the move's
# own shape plus the same size at its new place; the moves superpose). One pass over the runs found as in the default
# mode (steeper than detect_db_s, moving min_db or more inside sounding notes); only the steep samples of a merged run
# move, and a move is split at the track's rests (gaps of rest_min_s or more): each part inside a sounding segment
# (from new_pre_s before its first note-on) is placed on its own, a part in a rest stays.
#   - a printed sudden dynamic at a new note (sudden_marks, subito_falls, and with "mark_steps" a printed dynamic that
#     changes the level with no hairpin arriving; moves up to ramp_min_s long): a step ending sudden_pre_s before the
#     moved note-on, sudden_db_s but at most sudden_max_s long;
#   - a move in the direction of a printed hairpin that covers it (hairpin_pre_s before its start to hairpin_tail_s
#     after its end): a ramp inside the printed hairpin and inside the note it lies in (from the hairpin's start or the
#     note-on before, to its note-on or the hairpin's end), however steep; at a note-on after a rest, in that rest;
#   - any other move, to the option that moves the least level (dB x seconds off the written course; level moved
#     outside the move's own note counts out_weight times): the rest before or after its note (crossing no note-on of
#     the track; a move at a joined note-on may go to the rest before the note it joins), placed in the last
#     rest_lead_s before the next note-on so the hall tail keeps the level the note ended at; a ramp across its note
#     (at a joined note-on: either note or both) or slowed about its centre inside them; a move ramp_min_s or longer
#     (a ramp already) slowed about its centre inside its sounding segment, or ("mix_ramp_rest") split between such a
#     ramp and a rest. Ramps count only when the written course with the ramp stays under max_db_s inside sounding
#     notes (slope_win_s windows; the other moves of the pass taken out, the ones placed before put in). With no such
#     option: the least steep ramp, listed in "steep_ramps". "ramp_cross": ramps may also run one note-on further.
# tr["_nsg"]["moves"] lists (qn from, qn to, dB, kind, placed from, placed to) for the net-level gate
# (cycles/c63/actor_scripts/gate63.py --guard).
def _nsg_relocate(tr, grid, vals, cfg):
    import numpy as np
    DET, MIN = cfg.get("detect_db_s", 2.6), cfg.get("min_db", 0.8)
    R = cfg.get("max_db_s", 3.0)
    SR, SP = cfg.get("sudden_db_s", 20.0), cfg.get("sudden_pre_s", 0.03)
    NPRE, NPOST = cfg.get("new_pre_s", 0.35), cfg.get("new_post_s", 0.15)
    RL, HT, HPRE, dt = cfg.get("rest_lead_s", 0.35), cfg.get("hairpin_tail_s", 0.3), cfg.get("hairpin_pre_s", 0.05), cfg.get("step_s", 0.01)
    RMIN = cfg.get("rest_min_s", 0.04)
    RAMP_ANY = cfg.get("ramp_any", True)       # a ramp across the note may be chosen over a rest when it moves less level
    RAMP_LONG = cfg.get("ramp_long_s", 4.0)
    OUTW = cfg.get("out_weight", 6.0)
    SUBMIN = cfg.get("sub_min_db", 0.3)
    SUDMAX = cfg.get("sudden_max_s", 0.06)
    MIX_RR = cfg.get("mix_ramp_rest", True)  # a ramp-long move may be split between a slow ramp and a rest
    RAMP_S = cfg.get("ramp_min_s", 0.4)     # a move this long is a ramp: it may be slowed across note-ons     # parts of a move under this per segment stay where they are
    CROSS = cfg.get("ramp_cross", False)   # ramps may run one note-on further either side (c63: off; the net-level gate)    # with ramp_any false: only notes this long ramp (else the nearest rest)
    GAP = max(1, int(round(cfg.get("merge_gap_s", 0.25) / dt)))
    QB, TB = _tempo_arr()
    G, V = np.asarray(grid, float), np.asarray(vals, float)
    TG = np.interp(G, QB, TB)
    t = np.arange(TG[0], TG[-1] + 1e-9, dt)
    N = len(t)
    v = np.interp(t, TG, V)
    v_in = v.copy()
    notes = tr.get("notes", [])
    on = np.interp([n["qn"] for n in notes], QB, TB)
    off = np.interp([n["qn"] + n["dur"] for n in notes], QB, TB)
    tm = t[:-1] + dt / 2
    snd = (np.searchsorted(np.sort(on), tm, "left") - np.searchsorted(np.sort(off), tm, "right")) > 0
    sud_q = _sudden_qn(tr, set(cfg.get("sudden_marks", ["sf", "sfz", "fp", "sfp", "sub. p", "sub. pp"])), cfg.get("mark_steps", False))
    ons = sorted(set(round(float(x), 4) for x in on))
    sud_on = sorted({round(float(o_), 4) for o_, n in zip(on, notes) if any(abs(n.get("sq", n["qn"]) - s_) < 0.02 for s_ in sud_q)})
    hps = [(float(np.interp(h0, QB, TB)), float(np.interp(h1, QB, TB)), k_) for h0, h1, k_ in tr.get("hairpins", [])]
    # sounding segments (gaps under rest_min_s are joins) and the note-ons inside each
    iv = sorted(zip([round(float(x_), 4) for x_ in on], off.tolist()))
    segs = []
    for a_, b_ in iv:
        if segs and a_ < segs[-1][1] + RMIN:
            segs[-1][1] = max(segs[-1][1], b_)
        else:
            segs.append([a_, b_])
    seg_on = [sorted({round(o_, 4) for o_ in ons if s0_ - 1e-6 <= o_ <= s1_ + 1e-6}) for s0_, s1_ in segs]
    ix = lambda x: int(min(N - 1, max(0, round((x - t[0]) / dt))))
    stats = {"sudden": 0, "hairpin": 0, "rest_before": 0, "rest_after": 0, "note_ramp": 0, "hairpin_ramps": [], "moves": []}
    accepted = []

    def runs():
        dv = np.diff(v)
        s_ = np.where(np.abs(dv) / dt >= DET, np.sign(dv), 0.0)
        br = np.flatnonzero(np.diff(s_) != 0) + 1
        starts, ends = np.r_[0, br], np.r_[br, len(s_)]
        rs_ = [[int(a_), int(b_), s_[a_]] for a_, b_ in zip(starts, ends) if s_[a_] != 0]
        mg_ = []
        for r_ in rs_:
            if mg_ and r_[2] == mg_[-1][2] and r_[0] - mg_[-1][1] <= GAP and \
                    np.all(dv[mg_[-1][1]:r_[0]] * r_[2] >= -0.02) and \
                    abs(v[r_[1]] - v[mg_[-1][0]]) / max(dt, t[r_[1]] - t[mg_[-1][0]]) >= DET:
                mg_[-1][1] = r_[1]
            else:
                mg_.append(list(r_))
        out = []
        for a_, b_, _sg in mg_:
            ins = float(np.abs(dv[a_:b_][snd[a_:b_]]).sum())
            if ins >= MIN:
                out.append((a_, b_, ins))
        return out

    def shape(x0, x1):
        L = max(dt, x1 - x0)
        return np.clip((t - x0) / L, 0.0, 1.0)

    W_ = max(1, int(round(cfg.get("slope_win_s", 0.25) / dt)))

    def slope_with(r0_, r1_):
        """the steepest slope (dB/s over slope_win_s) of the written course with this move placed over [r0_, r1_]"""
        i0_, i1_ = max(0, ix(r0_) - W_), min(N - 1, ix(r1_) + W_)
        if i1_ - i0_ <= W_:
            return abs(D_cur[0]) / max(dt, r1_ - r0_)
        w_ = base_[0][i0_:i1_ + 1] + D_cur[0] * shape(r0_, r1_)[i0_:i1_ + 1]
        sl_ = np.abs(w_[W_:] - w_[:-W_]) / (W_ * dt)
        sn_ = snd[i0_:i1_ + 1 - W_] if i1_ + 1 - W_ <= len(snd) else np.r_[snd[i0_:], np.zeros(i1_ + 1 - W_ - len(snd), bool)]
        sn_ = sn_[:len(sl_)]
        return float(sl_[sn_].max()) if sn_.any() else 0.0   # inside sounding notes only

    D_cur, old_cur, base_ = [0.0], [None], [None]

    def own(k0, k1):
        """the steep part of a run: (D, k0, k1, shape 0 before / 1 after) or None"""
        dv_ = np.diff(v[k0:k1 + 1])
        st_ = np.where(np.abs(dv_) / dt >= DET, dv_, 0.0)
        D = float(st_.sum())
        if abs(D) < 1e-6:
            return None
        nz_ = np.flatnonzero(st_)
        k0, k1 = k0 + int(nz_[0]), k0 + int(nz_[-1]) + 1
        st_ = st_[nz_[0]:nz_[-1] + 1]
        old = np.zeros(N)
        old[k1:] = 1.0
        old[k0 + 1:k1 + 1] = np.cumsum(st_) / D
        return D, k0, k1, old

    def seg_of(x):
        for k_, (s0_, s1_) in enumerate(segs):
            if s0_ - 1e-3 <= x <= s1_ + 1e-3:
                return k_
        return None

    for _pass in range(cfg.get("passes", 1)):
        acc_in = lambda a_, b_: any(t[a_] >= x0 - 0.03 and t[b_] <= x1 + 0.03 for x0, x1 in accepted)
        rs = [r_ for r_ in runs() if not acc_in(r_[0], r_[1])]
        if not rs:
            break
        add = np.zeros(N)
        # the written course with every move of this pass taken out (candidates are judged against it)
        base_[0] = v.copy()
        for k0, k1, ins in rs:
            o_ = own(k0, k1)
            if o_:
                base_[0] -= o_[0] * o_[3]
        # each move is the steep part of its run (merged runs keep their slow stretches in place), split at the
        # track's rests: the part in each sounding segment (from new_pre_s before its first note-on) is moved on its
        # own; a part that lies in a rest stays where it is
        subs = []
        for k0, k1, ins in rs:
            dv_ = np.diff(v[k0:k1 + 1])
            st_ = np.where(np.abs(dv_) / dt >= DET, dv_, 0.0)
            for zk_, (S0_, S1_) in enumerate(segs):
                z0_ = max(S0_ - NPRE, segs[zk_ - 1][1] if zk_ > 0 else -1e9)
                if S1_ < t[k0] or z0_ > t[k1]:
                    continue
                tz_ = t[k0:k1]
                pz_ = np.where((tz_ >= z0_ - 1e-9) & (tz_ < S1_), st_, 0.0)
                Dz_ = float(pz_.sum())
                if abs(Dz_) < SUBMIN:
                    continue
                nz_ = np.flatnonzero(pz_)
                j0_, j1_ = k0 + int(nz_[0]), k0 + int(nz_[-1]) + 1
                oz_ = np.zeros(N)
                oz_[j1_:] = 1.0
                oz_[j0_ + 1:j1_ + 1] = np.cumsum(pz_[nz_[0]:nz_[-1] + 1]) / Dz_
                subs.append((j0_, j1_, Dz_, oz_))
        for k0, k1, D, old in subs:
            a, b = t[k0], t[k1]
            D_cur[0], old_cur[0] = D, old
            c_ = float(t[k0] + (np.abs(old[k0:k1 + 1] - 0.5)).argmin() * dt)
            qq_ = lambda x_: round(float(np.interp(x_, TB, QB)), 3)
            hp = [h for h in hps if h[0] - HPRE <= a and b <= h[1] + HT and ((h[2] == "cresc" and D > 0) or (h[2] != "cresc" and D < 0))]
            cand = [m for m in ons if a - NPRE <= m <= b + NPOST]
            m = min(cand, key=lambda x: abs(x - c_)) if cand else None
            if m is not None and b - a <= RAMP_S and any(abs(m - s_) < 0.005 for s_ in sud_on):
                te = m - SP
                s0 = te - min(abs(D) / SR, SUDMAX)   # c63: at most sudden_max_s (a 0.44 s ramp lifted the celli's ff stroke before the pp at 286)
                add += D * (shape(s0, te) - old)
                base_[0] += D * shape(s0, te)
                accepted.append((s0, te))
                stats["sudden"] += 1
                stats["moves"].append((qq_(a), qq_(b), round(D, 2), "sudden", qq_(s0), qq_(te)))
                continue
            if hp:
                # the hairpin's move stays inside the printed hairpin and inside the note it lies in (from the
                # hairpin's start or the note-on before, to the move's note-on or the hairpin's end), however steep;
                # at a note-on after a rest it lies in that rest
                h0, h1 = hp[0][0], hp[0][1]
                x0 = m if m is not None else 0.5 * (a + b)
                k_ = seg_of(x0)
                if k_ is None:
                    k_ = seg_of(a) if seg_of(a) is not None else seg_of(b)
                if k_ is not None:
                    S0, S1 = segs[k_]; bo = seg_on[k_]
                    prv = max([o_ for o_ in bo if o_ < x0 - 1e-6] or [S0])
                    nxt = min([o_ for o_ in bo if o_ > x0 + 1e-6] or [S1])
                    if m is not None and m <= S0 + 1e-6:
                        pe = segs[k_ - 1][1] if k_ > 0 else t[0]
                        r0, r1 = max(pe, S0 - RL, h0 - HPRE), S0 - 0.005
                    elif m is not None:
                        r0, r1 = max(h0, prv), m - 0.005
                    else:
                        r0, r1 = max(h0, prv), min(h1 + HT, nxt)
                    if r1 - r0 < b - a:
                        r0, r1 = a, b
                else:
                    r0, r1 = a, b
                if os.environ.get("NSG_DEBUG") == tr["name"]:
                    print("hp", [round(float(np.interp(x_, TB, QB)), 3) for x_ in (a, b, r0, r1, h0, h1)], m and round(float(np.interp(m, TB, QB)), 3), k_ is not None and [round(float(np.interp(x_, TB, QB)), 3) for x_ in segs[k_]], round(float(D), 2))
                add += D * (shape(r0, r1) - old)
                base_[0] += D * shape(r0, r1)
                accepted.append((r0, r1))
                stats["hairpin"] += 1
                stats["moves"].append((qq_(a), qq_(b), round(D, 2), "hairpin", qq_(r0), qq_(r1)))
                stats["hairpin_ramps"].append((round(float(np.interp(r0, TB, QB)), 3), round(float(np.interp(r1, TB, QB)), 3), round(float(D), 2),
                                               round(float(np.interp(h0, TB, QB)), 3), round(float(np.interp(h1, TB, QB)), 3)))
                continue
            x0 = m if m is not None else 0.5 * (a + b)
            k_ = seg_of(x0)
            if k_ is None:
                k_ = seg_of(a) if seg_of(a) is not None else seg_of(b)
            if k_ is None:
                continue
            S0, S1 = segs[k_]
            bo = seg_on[k_]
            new = m is not None
            prv = max([o_ for o_ in bo if o_ < x0 - 1e-6] or [S0])
            nxt = min([o_ for o_ in bo if o_ > x0 + 1e-6] or [S1])
            # options, each with the level it moves (dB x seconds away from the written course)
            opts = []
            if (new and prv <= S0 + 1e-6) or (not new and prv <= S0 + 1e-6):
                pe = segs[k_ - 1][1] if k_ > 0 else t[0]
                opts.append((x0 - S0, "rest_before", max(pe, S0 - RL), S0 - 0.005))
            if nxt >= S1 - 1e-6:
                nx = segs[k_ + 1][0] if k_ + 1 < len(segs) else S1 + RL + 0.005
                opts.append((S1 - x0, "rest_after", max(S1, nx - RL), nx - 0.005))
            pp_ = max([o_ for o_ in bo if o_ < prv - 1e-6] or [S0])     # one note-on further either side
            nn_ = min([o_ for o_ in bo if o_ > nxt + 1e-6] or [S1])
            if not CROSS:
                pp_, nn_ = prv, nxt
            rmp = ([(prv, x0), (x0, nxt), (pp_, x0), (x0, nn_), (prv, nxt)] if new else [(prv, nxt), (pp_, nxt), (prv, nn_)])
            rmp += [(max(a, pp_), min(b, nn_))]
            # the move slowed to max_db_s about its own centre, kept inside one note-on either side
            Lc_ = abs(D) / (0.98 * R)
            c_ = float(t[k0] + (np.abs(old[k0:k1 + 1] - 0.5)).argmin() * dt)
            lo_, hi_ = (pp_, nn_)
            if hi_ - lo_ >= Lc_:
                r0_ = min(max(c_ - Lc_ / 2, lo_), hi_ - Lc_)
                rmp.append((r0_, r0_ + Lc_))
            # a ramp already (ramp_min_s or longer): slowed to max_db_s about its centre inside its sounding segment,
            # across note-ons as it was written (not a per-note step)
            if b - a >= RAMP_S:
                Lr_ = max(b - a, Lc_)
                if S1 - S0 >= Lr_:
                    r0_ = min(max(c_ - Lr_ / 2, S0), S1 - Lr_)
                    rmp.append((r0_, r0_ + Lr_))
            ramps = []
            for r0_, r1_ in rmp:
                L_ = max(dt, r1_ - r0_)
                cost_ = ((x0 - r0_) ** 2 + (r1_ - x0) ** 2) / (2 * L_)
                ramps.append((cost_, "note_ramp", r0_, r1_, slope_with(r0_, r1_)))
            ok_r = [r_[:4] for r_ in ramps if r_[4] <= R and (RAMP_ANY or r_[3] - r_[2] >= RAMP_LONG)]
            if os.environ.get("NSG_DEBUG") == tr["name"]:
                q_ = lambda x_: round(float(np.interp(x_, TB, QB)), 3)
                print("mv", q_(a), q_(b), round(D, 2), "m", m and q_(m), "seg", q_(S0), q_(S1), "opts", [(round(o_[0], 2), o_[1], q_(o_[2]), q_(o_[3])) for o_ in opts], "ramps", [(q_(r_[2]), q_(r_[3]), round(r_[4], 2)) for r_ in ramps])
            wt_ = np.where((t >= prv - 1e-3) & (t <= nxt + 1e-3), 1.0, OUTW)
            # candidates as new shapes: the rests, the ramps under max_db_s, and for a ramp-long move with a rest
            # option the largest part f of it (in tenths) that a ramp can carry under max_db_s with the rest of it
            # in the rest
            cands = [(kind_r, shape(r0_, r1_), r0_, r1_) for _c, kind_r, r0_, r1_ in opts + ok_r]
            if MIX_RR and opts and b - a >= RAMP_S:
                for _c, kind_o, o0_, o1_ in opts:
                    so_ = shape(o0_, o1_)
                    for _c2, _k2, q0_, q1_, sl2_ in ramps:
                        if sl2_ <= R:
                            continue
                        sr_ = shape(q0_, q1_)
                        i0_, i1_ = max(0, min(ix(q0_), ix(o0_)) - W_), min(N - 1, max(ix(q1_), ix(o1_)) + W_)
                        for f_ in (0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1):
                            sh_ = f_ * sr_ + (1 - f_) * so_
                            w_ = base_[0][i0_:i1_ + 1] + D * sh_[i0_:i1_ + 1]
                            sl_ = np.abs(w_[W_:] - w_[:-W_]) / (W_ * dt)
                            sn_ = snd[i0_:i0_ + len(sl_)]
                            sl_ = sl_[:len(sn_)]
                            if not sn_.any() or sl_[sn_].max() <= R:
                                cands.append(("mixed", sh_, min(q0_, o0_), max(q1_, o1_)))
                                break
            if cands:
                # the option that moves the least level (dB x seconds away from the written course); level moved
                # outside the move's own note (held: between its note-ons; at a note-on: the notes either side)
                # counts out_weight times
                kind_, nsh_, r0, r1 = min(cands, key=lambda c_: float((np.abs(c_[1] - old) * wt_).sum()))
            else:
                _c, kind_, r0, r1, sl_ = min(ramps, key=lambda r_: r_[4])
                nsh_ = shape(r0, r1)
                stats.setdefault("steep_ramps", []).append((round(float(np.interp(r0, TB, QB)), 3), round(float(np.interp(r1, TB, QB)), 3), round(float(D), 2)))
            add += D * (nsh_ - old)
            base_[0] += D * nsh_
            stats[kind_] = stats.get(kind_, 0) + 1
            stats["moves"].append((qq_(a), qq_(b), round(D, 2), kind_, qq_(r0), qq_(r1)))
        v = v + add
    acc_in = lambda a_, b_: any(t[a_] >= x0 - 0.03 and t[b_] <= x1 + 0.03 for x0, x1 in accepted)
    stats["left"] = [(round(float(np.interp(t[a_], TB, QB)), 3), round(i_, 1)) for a_, b_, i_ in runs() if not acc_in(a_, b_)]
    tr["_nsg"] = stats
    ed = np.abs(v - v_in) > 0.004
    if not ed.any():
        return grid, vals
    ed = ed | np.r_[ed[1:], False] | np.r_[False, ed[:-1]]
    TGq = np.interp(t, TB, QB)
    keep = [(float(q_), float(v_)) for q_, v_, tg_ in zip(G, V, TG) if not ed[ix(tg_)]]
    keep += [(round(float(TGq[k_]), 5), round(float(v[k_]), 2)) for k_ in np.flatnonzero(ed)]
    keep.sort()
    out_q, out_v = [], []
    for q_, v_ in keep:
        if out_q and q_ <= out_q[-1] + 1e-6:
            continue
        out_q.append(q_); out_v.append(v_)
    return out_q, out_v


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
    g = m["gain_db"] + tr.get("vol_shift_db", 0.0)   # mvt1 c62: score_to_parts VOL_TO_CC7's shift; c02: with a volume envelope REAPER ignores D_VOL (measured: every gain was lost), so the gain goes in here
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
            # mvt1 c56 (critic C #3): mix.json per-track "soft_decresc_keep" (Violas 612-616 rose 5.1 dB through a
            # printed diminuendo with half the trim's rise kept)
            # mvt1 c60 (critic A #3): where the hairpin runs into its arrival note with no rest and the held trim would
            # step up by "min_step_db" or more at that note-on, the trim ramps over the hairpin instead (hairpin gain,
            # a slow ramp): Violas 164-168 stepped +12.6 dB in 60 ms at the join into the pp. mix.json "decresc_ramp"
            # {"min_step_db", "rest_s", "max_db_s"}; a ramp steeper than max_db_s starts earlier in the hairpin's note
            dr_ = m.get("decresc_ramp", MIX.get("decresc_ramp", DECRESC_RAMP))
            tgt_ = None
            if dr_:
                keep_ = m.get("soft_decresc_keep", SOFT_DECRESC_KEEP)
                t1_ = trim(step_at(dyn, max(e_, h1) + 0.01, first))
                held_ = trim(c0) + keep_ * max(0.0, t1_ - trim(c0))
                ends_ = [n["qn"] + n["dur"] for n in tr.get("notes", []) if n["qn"] < e_ - 1e-6]
                joined_ = bool(ends_) and q2s(e_) - q2s(min(e_, max(ends_))) < dr_.get("rest_s", 0.1)
                if joined_ and t1_ - held_ >= dr_["min_step_db"] and q2s(e_) - q2s(h0) > 0.3:
                    tgt_ = min(t1_, trim(c0) + dr_.get("max_db_s", 3.0) * (q2s(e_) - q2s(h0)))   # the rest stays a step at the join
                    DECRESC_RAMPS.append((tr["name"], round(h0, 3), round(e_, 3), round(trim(c0), 2), round(tgt_, 2), round(t1_, 2)))
            holds.append((h0, e_, trim(c0), m.get("soft_decresc_keep", SOFT_DECRESC_KEEP), tgt_))

    def trim_at(q):
        t_ = trim(step_at(dyn, q, first))
        for a_, b_, cap_, keep_, tgt_ in holds:
            if a_ - 1e-9 <= q < b_ - 1e-9 and tgt_ is not None:
                t_ = max(min(t_, cap_), cap_ + (tgt_ - cap_) * (q - a_) / max(1e-9, b_ - a_))
            elif a_ - 1e-9 <= q < b_ - 1e-9 and t_ > cap_:
                t_ = cap_ + keep_ * (t_ - cap_)
        return t_
    val_at = lambda q: round(g + step_at(vol, q) + (trim_at(q) if dyn else 0.0), 2)
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
    # mvt1 c58 (critic C #2): ONSET_KEY (see the default)
    ok_ = MIX.get("onset_key", ONSET_KEY)
    if ok_ and tr.get("notes"):
        def cur0(q, G=list(grid), V=list(vals)):
            k = bisect.bisect_left(G, q)
            if k <= 0:
                return V[0]
            if k >= len(G):
                return V[-1]
            return V[k - 1] + (V[k] - V[k - 1]) * (q - G[k - 1]) / max(1e-9, G[k] - G[k - 1])
        sub_q_ = [s_ for s_, _f in tr.get("subito_falls", [])]
        edits_, done_, max_end_ = [], set(), None
        for n in sorted(tr["notes"], key=lambda n: (n["qn"], n.get("sq", n["qn"]))):
            m_, s_ = n["qn"], n.get("sq", n["qn"])
            pe_ = max_end_
            max_end_ = max(max_end_ if max_end_ is not None else -1e9, n["qn"] + n["dur"])
            if s_ - m_ < 0.004 or round(s_, 4) in done_ or s_ >= TAIL_HOLD_STOP_QN or m_ < 0:
                continue
            gap_ = q2s(m_) - q2s(pe_) if pe_ is not None else 1e9
            if gap_ < ok_["min_rest_s"] or any(abs(s_ - x_) < 0.2 for x_ in sub_q_):
                continue   # joined to the note before (a legato target: the step stays on the audible join)
            v_new_ = val_at(s_ + 0.001)
            r0_ = s2q(q2s(m_) - ok_["ramp_s"])
            if pe_ is not None:
                r0_ = max(r0_, pe_)
            lo_ = r0_ if pe_ is None else (s2q(q2s(m_) - TAIL_HOLD_LEAD_S) if gap_ >= TAIL_HOLD_MIN_S else pe_)
            lo_ = min(lo_, r0_)
            hold_ = cur0(lo_ - 0.002) if pe_ is not None else v_new_
            if abs(v_new_ - hold_) < 0.3 and abs(cur0(m_) - v_new_) < 0.3:
                continue
            edits_.append((lo_, r0_, m_, s_, hold_, v_new_))
            done_.add(round(s_, 4))
        if edits_:
            mp_ = dict(zip(grid, vals))
            for lo_, r0_, m_, s_, hold_, v_new_ in edits_:
                for q in [q for q in mp_ if lo_ - 1e-6 <= q < s_ - 1e-6]:
                    del mp_[q]
                mp_[round(r0_, 5)] = round(hold_, 2)
                mp_[round(m_, 5)] = round(v_new_, 2)
                if round(lo_, 5) < round(r0_, 5):
                    mp_[round(lo_, 5)] = round(hold_, 2)
            grid = sorted(mp_)
            vals = [mp_[q] for q in grid]
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
    # mvt1 c62: note_slope_guard (see the function)
    nsg_ = MIX.get("note_slope_guard")
    if nsg_ and tr.get("notes") and not os.environ.get("ENV_NO_GUARD"):
        grid, vals = (_nsg_relocate if nsg_.get("mode") == "relocate" else note_slope_guard)(tr, grid, vals, nsg_)   # c63: mode
    out = []
    for k, (q, v) in enumerate(zip(grid, vals)):
        if k == 0 or k == len(vals) - 1 or v != vals[k - 1] or v != vals[k + 1]:
            out.append({"qn": q + PRE, "db": v})
    # mvt1 c56 (Dan: the envelope's point density): ENV_THIN drops the points of a ramp that lie within tol_db of the
    # straight line (in dB over qn) between the points kept around them; two kept points are at most max_step_db apart
    # in level, so REAPER's own interpolation between them stays within about 0.06 dB of the dB line
    if ENV_THIN and len(out) > 2:
        tol_, ms_ = ENV_THIN["tol_db"], ENV_THIN["max_step_db"]
        kept, i = [out[0]], 0
        while i < len(out) - 1:
            j = i + 1
            while j + 1 < len(out):
                a_, b_ = out[i], out[j + 1]
                if abs(b_["db"] - a_["db"]) > ms_ or b_["qn"] - a_["qn"] > ENV_THIN.get("max_qn", 4.0):
                    break
                if any(abs(a_["db"] + (b_["db"] - a_["db"]) * (out[k]["qn"] - a_["qn"]) / (b_["qn"] - a_["qn"]) - out[k]["db"]) > tol_
                       for k in range(i + 1, j + 1)):
                    break
                j += 1
            kept.append(out[j])
            i = j
        out = kept
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


# ---- mvt1 c50: EastWest template mix (loop/TEMPLATE-PLAN.md sections 1-4 and 8; tools/TEMPLATE-TOOLS.md) ----
# Every key below is off when absent, and then no line of the generated Lua or Opus state changes (proof:
# tools/build_identity_check.py). Keys (mix.json):
#   "mic_db", "pan_by_mic" (group or track): see mic_volumes / apply_mix.   "opus_reverb_off": see opus_reverb_off.
#   "reaper_pan" (group or track): REAPER's track pan (D_PAN, stereo pan mode 5) after Opus; absent = centre, as before.
#   "family_eqs" (top level) {name: [bands] or {"chunk": file, "fx": "ReaEQ"}} and "family_eq" (group or track) = a name
#     (null = none): one more ReaEQ after every other FX of the track (set_family_eq in template_mix.FAMILY_LUA). Bands
#     are {"band": lowshelf|highshelf|lowpass|highpass|bell, "hz", "db", "bw_oct"}, at most 5, in ReaEQ band slots
#     0..4 in list order; set like the per-track "eq" (set_by_fmt). set_eq deletes every ReaEQ on a re-run and the
#     family EQ is added again after it, so --midi-only / --mix-only re-runs give the same chain.
#   "returns" (top level) {name: {"fx": [...], "fader_db", "pan", "enabled", "bypass"}}: REAPER return tracks (see
#     template_mix.resolve_fx for the "fx" entries: the template's chunks verbatim, Spaces II with "set" values, or a
#     ReaEQ from a band list). "return_chunks_dir": where the chunk files are (default: the research folder).
#     "return_load": "vst_chunk" (default; TrackFX_SetNamedConfigParm) or "fxchain" (the <FXCHAIN> in the track chunk).
#     The returns job (jobs/90_returns.lua) runs before the track jobs in every mode; a return is created at the end of
#     the project when missing, otherwise rebuilt in place (its receives stay). Its states are read back and compared.
#     A return renders as a stem; render_cycle.py renumbers it 91.. in "returns" order (tools/return_stems.py).
#   "send_profiles" (top level) {profile: {group: {return: dB}}}, "send_profile" (top level, or a group / track
#     overriding it; null = no sends): post-fader sends from each track to its family's returns. A disabled return
#     ("enabled": false) gets no sends. Per track or group: "sends" {return: dB} replaces the profile's group entry;
#     "send_offset_db" (a number, or {return: dB}) is added; "send_row_db" {return or "*": {KS row: dB}} adds the row's
#     offset while that articulation row plays (a send volume envelope stepping at the onset of the first note of each
#     row, D_VOL 1). A parts.json "test" track sends to "<return> test", a copy of the return made in the pass-2 project,
#     whose stem render_cycle.py keeps with the test stems (never in the master).
_TM = None


def tm():
    """mvt1 c50: tools/template_mix.py, imported on first use (only when mix.json holds a c50 key)"""
    global _TM
    if _TM is None:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import template_mix
        _TM = template_mix
    return _TM


def reaper_pan(m):
    v_ = m.get("reaper_pan")
    return None if v_ is None else float(v_)


def track_width(m):
    """mvt3 c09 (critic C #2), ported mvt1 c52 (critic B #4): mix.json "track_width" (group or track, default 1): REAPER's
    stereo-pan width (D_WIDTH, I_PANMODE 5) after the plugin, so a section sounds as a narrower source at its reaper_pan;
    the post-fader sends feed the returns from the narrowed signal. Returned as Lua text ("1" when absent, so the
    generated jobs of tracks without the key do not change)."""
    w_ = float(m.get("track_width", 1.0))
    return "1" if w_ == 1.0 else repr(w_)


def family_eq_lua(m):
    """mvt1 c50: the track's family EQ as a Lua table, or None"""
    k_ = m.get("family_eq")
    if not k_:
        return None
    tbl_ = MIX.get("family_eqs") or {}
    if k_ not in tbl_:
        sys.exit(f"family_eq {k_!r}: no such entry in mix.json family_eqs ({sorted(tbl_)})")
    return tm().family_spec(k_, tbl_[k_], MIX, os.path.dirname(os.path.abspath(PARTS)))


def send_row_env(tr, db_, rows):
    """mvt1 c50: send volume points [{qn, db}] (project qn) for "send_row_db": the row of each note is the last
    keyswitch row at or before its (moved) onset (first_art before the first keyswitch); the level steps at the onset of
    the first note of each row. None when no note plays a listed row."""
    ks_ = sorted((k["qn"], k.get("art")) for k in tr.get("ks", []))

    def row_at(q):
        r_ = tr.get("first_art")
        for kq_, art_ in ks_:
            if kq_ <= q + 1e-6:
                r_ = art_
            else:
                break
        return r_
    pts, cur = [], None
    for n in sorted(tr.get("notes", []), key=lambda n_: n_["qn"]):
        v_ = round(db_ + rows.get(row_at(n["qn"]), 0.0), 3)
        if v_ != cur:
            pts.append({"qn": round(n["qn"] + PRE, 4), "db": v_})
            cur = v_
    if not pts or all(p_["db"] == round(db_, 3) for p_ in pts):
        return None
    if pts[0]["qn"] > 0:
        pts.insert(0, {"qn": 0.0, "db": pts[0]["db"]})
    return pts


def send_list(tr):
    """mvt1 c50: the track's sends [{dest, base, db, env}] (empty without a send profile)"""
    m = mix_for(tr["name"])
    prof = m["send_profile"] if "send_profile" in m else MIX.get("send_profile")
    if not prof:
        return []
    profs = MIX.get("send_profiles") or {}
    if prof not in profs:
        sys.exit(f"{tr['name']}: send_profile {prof!r} is not in mix.json send_profiles ({sorted(profs)})")
    base = m["sends"] if m.get("sends") is not None else (profs[prof].get(m["group"]) or {})
    off = m.get("send_offset_db") or 0.0
    rows_all = m.get("send_row_db") or {}
    out = []
    for dest, db in base.items():
        if dest.startswith("_"):
            continue
        rdef = (MIX.get("returns") or {}).get(dest)
        if rdef is None:
            sys.exit(f"{tr['name']}: sends to {dest!r}, which is not in mix.json returns")
        if rdef.get("enabled", True) is False:
            continue
        db_ = float(db) + (float(off.get(dest, 0.0)) if isinstance(off, dict) else float(off))
        rows = {k_: float(v_) for k_, v_ in dict(rows_all.get("*") or {}, **(rows_all.get(dest) or {})).items()
                if not k_.startswith("_")}
        out.append({"dest": dest + (" test" if tr.get("test") else ""), "base": dest, "db": round(db_, 3),
                    "env": send_row_env(tr, db_, rows) if rows else None})
    return out


def template_lua(feq, snd):
    """mvt1 c50: the Lua that adds the family EQ and the sends to track variable `tr` (results into `eq`); "" when
    neither is set (the c49 jobs)"""
    if not feq and not snd:
        return ""
    T = tm()
    return ((T.FAMILY_LUA if feq else "") + (T.SENDS_LUA if snd else "")
            + (f"set_family_eq(tr, {feq}, eq)\n" if feq else "") + (f"set_sends(tr, {T.sends_table(snd)}, eq)\n" if snd else ""))


def pass_returns():
    """mvt1 c50: [(return track name, mix.json returns key)] that this pass's tracks send to, in "returns" order (a
    test copy right after its source)"""
    if not (MIX.get("send_profile") or any(isinstance(e_, dict) and e_.get("send_profile")
                                           for e_ in list(MIX["groups"].values()) + list(MIX["tracks"].values()))):
        return []   # no send profile anywhere (the c49 mix.json)
    want = set()
    for tr in d["tracks"]:
        if in_pass(tr) and tr["name"] in MIX["tracks"]:
            want.update(s["dest"] for s in send_list(tr))
    if not want:
        return []
    order = [(nm, k) for k in (MIX.get("returns") or {}) if not k.startswith("_") for nm in (k, k + " test") if nm in want]
    clash = sorted({nm for nm, _ in order} & {t["name"] for t in d["tracks"]})
    if clash:
        sys.exit(f"return track names equal track names: {clash}")
    if len([k for k in MIX["returns"] if not k.startswith("_")]) > 9:
        sys.exit("more than 9 returns: render_cycle.py numbers return stems 91..99")
    return order


def returns_job():
    """mvt1 c50: create or rebuild this pass's return tracks; stop the build when REAPER reads back other FX states"""
    rets = pass_returns()
    if not rets:
        return None
    T = tm()
    specs = [T.resolve_return(MIX, os.path.dirname(os.path.abspath(PARTS)), base, name) for name, base in rets]
    p = f"{JOBS}/90_returns.lua"
    open(p, "w").write(T.returns_lua(specs, MIX.get("return_load", "vst_chunk")))
    res = run(p, timeout=300)
    bad = T.verify_returns(res, specs)
    if bad:
        sys.exit("return tracks differ from mix.json:\n  " + "\n  ".join(bad))
    return T.returns_summary(res)


def check_sends(tr, res):
    """mvt1 c50: stop the build when a send could not be made (no return track, no send envelope)"""
    if send_list(tr) and "SEND ERROR" in json.dumps(res):
        print(json.dumps(res), flush=True)
        sys.exit(f"{tr['name']}: a send failed (SEND ERROR above); the returns job must run first (any build mode does it)")


RR_RESET_QN = 0.1   # c24 (A #3): pre-roll position (REAPER qn) of the CC36 reset and the string CC69 off


def _opus_rr_cc(default=16):
    """mvt1 c43 (MANUAL-GAPS #6): Opus resets its round robins on the "Reset Controller" CC entered in Preferences / MIDI /
    Round Robin (HO manual 2025 p.92, Opus manual p.29-30); the 2021 manual's CC36 is, in every installed KS Master's
    controller map, "Repetition: Reset RR", a control of the Repetition script. Read from Opus's Preferences.json
    (RoundRobinResetCC, 16 on this Mac; no patch maps CC16); None when the preference is off (-1)."""
    try:
        v = json.load(open("/Library/Application Support/East West/Opus/Preferences.json")).get("RoundRobinResetCC", default)
        return int(v) if v is not None and int(v) >= 0 else None
    except (OSError, ValueError, TypeError):
        return default


RR_RESET_CC = _opus_rr_cc()   # sent (value 127) at RR_RESET_QN next to CC36 on every track that gets the CC36 reset
RR_RESET_SKIP_FAMILIES = {"harp", "harm"}   # harp tracks were already bit-identical render to render
REP_OFF_FAMILIES = {"string"}


def item_lua(tr):
    """The MIDI item (notes, keyswitches, CCs), volume envelope and ReaEQ for track variable `tr` (Lua)."""
    m = mix_for(tr["name"])
    two_ch = any(n.get("ch") for n in tr["notes"])   # mvt1 c58: re-bow pieces on a second MIDI channel (REBOW_OVERLAP)
    notes = lua_list([dict(n, qn=round(n["qn"] + PRE, 4), **({"ch": n.get("ch", 0)} if two_ch else {})) for n in tr["notes"]],
                     ["qn", "dur", "pitch", "vel"] + (["ch"] if two_ch else []))
    ks_rows = [{"qn": round(k["qn"] + PRE, 4), "pitch": k["pitch"]} for k in tr["ks"]]
    if PRE and tr["first_ks"] is not None:   # c06: the first articulation is also selected in the pre-roll
        ks_rows.insert(0, {"qn": 0.25, "pitch": tr["first_ks"]})
    ks = lua_list(ks_rows, ["qn", "pitch"])
    ccs = []
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, tr.get("cc7", [])), (70, tr.get("cc70", [])),
                     (36, tr.get("cc36", []))):   # mvt1 c14 (A #2): round-robin resets inside the music
        ccs += [{"qn": round(q + PRE, 4), "cc": num, "v": v} for q, v in lane]
        if PRE and lane:   # c06: each lane's first value is sent in the pre-roll too
            ccs.append({"qn": 0.25, "cc": num, "v": lane[0][1]})
    if tr.get("cc16") and RR_RESET_CC is not None:
        # mvt1 c52 (critic A #3; finale mvt3 c08): round-robin resets inside the music (score_to_parts.py RR_RESET_AT) on
        # the controller Opus listens to (Preferences.json RoundRobinResetCC)
        ccs += [{"qn": round(q + PRE, 4), "cc": RR_RESET_CC, "v": v} for q, v in tr["cc16"]]
    if PRE and tr["family"] not in RR_RESET_SKIP_FAMILIES:
        # c24 (A #3): reset Opus's round-robin state (CC36, any value) at the start of every render, and on the strings
        # turn the Repetition script off (CC69 0-63 = OFF, HO manual CC table), so renders are reproducible
        ccs.append({"qn": RR_RESET_QN, "cc": 36, "v": 127})
        if RR_RESET_CC is not None and RR_RESET_CC != 36:   # mvt1 c43: the reset Opus itself listens to
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
  reaper.MIDI_InsertNote(take, false, false, ppq(n.qn), ppq(n.qn + n.dur), n.ch or 0, n.pitch, n.vel, true)
end
for _, k in ipairs({ks}) do
  reaper.MIDI_InsertNote(take, false, false, ppq(k.qn), ppq(k.qn + 0.03), 0, k.pitch, 1, true)
end
for _, c in ipairs({ccs}) do
  reaper.MIDI_InsertCC(take, false, false, ppq(c.qn), 0xB0, 0, c.cc, c.v)
  {"reaper.MIDI_InsertCC(take, false, false, ppq(c.qn), 0xB0, 1, c.cc, c.v)" if two_ch else ""}
end
reaper.MIDI_Sort(take)
local _, nn, nc = reaper.MIDI_CountEvts(take)
local envn = set_vol_env(tr, {vpts})
local eq = set_eq(tr, {eq_lua(m)})
set_wet_eqs(tr, {mute_lua(m)}, eq)
set_side_shelf(tr, {side_lua(m)}, eq)
""" + template_lua(family_eq_lua(m), send_list(tr))   # mvt1 c50: "" without the template keys


def track_job(i, tr):
    b64file = b64_path(i, tr)
    open(b64file, "w").write(state_for(tr))   # always regenerated: mix.json changes the state
    r, g, b = COLORS[tr["family"]]
    rp_ = reaper_pan(mix_for(tr["name"]))   # mvt1 c50: mix.json reaper_pan (absent: the c05 line, unchanged)
    pan_line = ('reaper.SetMediaTrackInfo_Value(tr, "D_PAN", 0)     -- c05: the seat is set inside Opus (apply_mix)' if rp_ is None
                else f'reaper.SetMediaTrackInfo_Value(tr, "D_PAN", {rp_!r})     -- mvt1 c50: mix.json reaper_pan, after Opus')
    lua = ENV_LUA + f"""
local name = {json.dumps(tr['name'])}
local old = R.track_by_name(name)
if old then reaper.DeleteTrack(old) end
local tr = R.add_track(name, {{ idx = math.min({i}, reaper.CountTracks(0)), instrument = "VST3i: Opus (East West)", color = R.rgb({r}, {g}, {b}) }})
reaper.SetMediaTrackInfo_Value(tr, "I_PANMODE", 5)
{pan_line}
reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", {track_width(mix_for(tr['name']))})
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


def in_pass(tr):
    """mvt1 c39: the track belongs to the pass being built (--pass2: only "pass": 2 tracks; else only the others)"""
    return (tr.get("pass", 1) == 2) == PASS2


def mix_job():
    rows = []
    ext_used = set()   # mvt1 c50: "feq" / "snd" when some row has a family EQ / sends
    for tr in d["tracks"]:
        if (ONLY and tr["name"] not in ONLY) or not in_pass(tr):
            continue
        m = mix_for(tr["name"])
        rp_ = reaper_pan(m)   # mvt1 c50
        # mvt1 c50: family EQ and sends per row (fields left out without the template keys, so the c49 text is unchanged)
        feq_, snd_ = family_eq_lua(m), send_list(tr)
        ext_ = (f", feq={feq_}" if feq_ else "") + (f", snd={tm().sends_table(snd_)}" if snd_ else "")
        if feq_ or snd_:
            ext_used.update(["feq"] if feq_ else [])
            ext_used.update(["snd"] if snd_ else [])
        rows.append(f'{{n={json.dumps(tr["name"])}, pan={rp_ if rp_ is not None else 0}, w={track_width(m)}, vol={10 ** (m["gain_db"] / 20):.6f}, env={lua_list(vol_points(tr), ["qn", "db"])}, eq={eq_lua(m)}, meq={mute_lua(m)}, ss={side_lua(m)}{ext_}}}')
    ext_lua = ""
    if ext_used:   # mvt1 c50
        ext_lua = ("    if r.feq then set_family_eq(tr, r.feq, eq) end\n" if "feq" in ext_used else "") + \
                  ("    if r.snd then set_sends(tr, r.snd, eq) end\n" if "snd" in ext_used else "")
    lua = ENV_LUA + (tm().FAMILY_LUA if "feq" in ext_used else "") + (tm().SENDS_LUA if "snd" in ext_used else "") + f"""
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
{ext_lua}    done[#done + 1] = r.n
    if #eq > 0 then done[#done + 1] = eq end
  end
end
return {{ set = done }}
"""
    p = f"{JOBS}/95_mix.lua"
    open(p, "w").write(lua)
    return run(p)


if MIX_ONLY:
    if pass_returns():   # mvt1 c50: the return tracks exist (and match mix.json) before any send is made
        print(json.dumps(returns_job()), flush=True)
    print(json.dumps(mix_job()))
    sys.exit(0)
if (not ONLY and not MIDI_ONLY) or TEMPO:
    print(json.dumps(tempo_job()))
if pass_returns():   # mvt1 c50: in every build mode, before the track jobs (their sends need the return tracks)
    print(json.dumps(returns_job()), flush=True)
# mvt1 c52 (critic A #1, scherzo c09): a --midi-only build keeps the Opus state REAPER loaded from the saved project, and
# after an instance has played that state can hold runtime values (legato sustain-group AHDSR attacks at 20 ms instead of
# 267-1501 ms; c51: Horn 1, Horn 3, Trumpet 1, Trumpet 2 and pass-2 Bassoon 1 stac played every loud legato join 45 ms
# early and 3-5 dB louder). With STALE_GUARD, --midi-only decodes the saved project (tools/state_guard.py) and fully
# rebuilds every track of the pass whose saved attacks differ from its jobs/NN_*.b64, also when it is not listed.
# render_cycle.py refuses to render a project that still holds one. The scherzo's alternative, rebuilding every legato
# track on each --midi-only build (MIDI_ONLY_REBUILD_LEGATO), costs a full patch reload of 29 tracks here.
STALE_GUARD = True
MIDI_ONLY_REBUILD_LEGATO = False   # scherzo c09's rule, kept as an option
STALE = set()
if MIDI_ONLY and STALE_GUARD:
    import glob as _glob
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import state_guard as _sg
    _root = os.path.dirname(os.path.dirname(os.path.abspath(PARTS)))
    _rpps = sorted(f for f in _glob.glob(f"{_root}/*.rpp") if f.endswith("-pass2.rpp") == PASS2)
    if _rpps:
        STALE = _sg.stale_tracks(_rpps[0], d, JOBS, PASS2)
        print(f"state_guard on {os.path.basename(_rpps[0])}: stale {sorted(STALE) or 'none'}", flush=True)
if MIDI_ONLY and MIDI_ONLY_REBUILD_LEGATO:
    STALE |= {t["name"] for t in d["tracks"] if any("Leg" in a_ for a_ in (t.get("art_counts") or {}))}
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY and tr["name"] not in STALE:
        continue
    if not in_pass(tr):
        if ONLY:
            print(f"{tr['name']}: skipped (pass {tr.get('pass', 1)}; {'without' if PASS2 else 'with'} --pass2)", flush=True)
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
    check_sends(tr, res)   # mvt1 c50: stops on a failed send (no-op without sends)
    print(json.dumps(res), flush=True)

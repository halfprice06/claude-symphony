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
  its Opus state is unchanged since the last full build (jobs/NN_*.b64); a track whose state changed is fully rebuilt,
  and so is every track that plays a legato row (MIDI_ONLY_REBUILD_LEGATO, scherzo c09) and every track whose saved
  Opus state is stale, listed or not (STALE_GUARD, scherzo c12; tools/state_guard.py).
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
import bisect, json, math, os, subprocess, sys
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
    if m.get("channel_map") is not None:
        # scherzo c17 (critic C #1; HO manual p.141, 4.2.6 Channel Routing): mix.json track key "channel_map": N sets the
        # instrument's `channelMap` (0 = Stereo in every patch file; the other values are the menu's order, to be
        # confirmed on a range render before use)
        inst["channelMap"] = int(m["channel_map"])
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
    (the Violas KS Master's Sus MAX RT groups ship 1660 ms, 1st Violins 1245-1741, Celli/Basses 131-166).
    scherzo c20 (critic A #4): "any_dyn": true caps every non-RT, non-TLeg group of the listed rows, whatever its name
    ends in (the short rows' groups, e.g. 2nd Violins "V2 Stac rrx1", carry no dynamic word: 372-749 ms releases)."""
    ms = float(spec["ms"])
    dyns = set(spec.get("dyn", ["mf", "f", "ff"]))
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if r in spec.get("rows", ["Sus MAX"])}
    hit = {}
    if spec.get("orphan_only"):
        # scherzo c24 (critic A #2): "orphan_only": true acts only on the groups of a listed row that have no start
        # modes while the row's other groups rotate by RoundRobin start modes (1st Violins KS Master: "V1 Stac rrx9" in
        # "Staccatissimo RRx9", "V1 Stac rrx16" in "Stac RRx14", "V1 stac rrx9" in "Stac On Bow RRx9": 721-733 ms
        # attack, 1000 ms release, read from the .oib). "deactivate": true switches such a group off instead of
        # capping its release
        for ri in sorted(want):
            gs = [g for g in inst.get("groups", []) if (g.get("regionMap") or {}).get("regions")
                  and all(r_.get("row") == ri for r_ in g["regionMap"]["regions"])]
            if not any((g.get("startModes") or {}).get("modes") for g in gs):
                continue
            for g in gs:
                if (g.get("startModes") or {}).get("modes"):
                    continue
                if spec.get("deactivate"):
                    g["active"] = False
                    hit.setdefault(g["name"], set()).add("off")
                    continue
                for pr_ in (g.get("processors") or {}).get("processors", []):
                    if pr_.get("class") == "AHDSR" and pr_.get("release", 0) > ms:
                        hit.setdefault(g["name"], set()).add(round(pr_["release"]))
                        pr_["release"] = ms
        print(f"{name}: orphan groups {'off' if spec.get('deactivate') else f'release cap {ms:.0f} ms'} on {sorted((k, sorted(map(str, v))) for k, v in hit.items())}", file=sys.stderr)
        return
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if g.get("type") == 3 or not regs or any(r_.get("row") not in want for r_ in regs):
            continue
        nm = g["name"].split(" rr")[0].split(" RR")[0].strip()
        words = nm.split()
        ms_ = ms
        if words[-1] == "RT" and spec.get("rt_ms") is not None and len(words) >= 2 and words[-2] in dyns:
            ms_ = float(spec["rt_ms"])   # mvt1 c22 (critic A #4): the release-trail groups of the listed dynamics too
        elif "TLeg" in nm and spec.get("tleg"):
            pass   # scherzo c26 (critic A #1): "tleg": true caps the legato transition groups too (no dynamic in their names)
        elif "TLeg" in nm or words[-1] == "RT" or (words[-1] not in dyns and not spec.get("any_dyn")):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "AHDSR" and pr_.get("release", 0) > ms_:
                hit.setdefault(nm, set()).add(round(pr_["release"]))
                pr_["release"] = ms_
    key_ = (name, ms, tuple(sorted(dyns)), tuple(spec.get("rows", ["Sus MAX"])), bool(spec.get("any_dyn")), bool(spec.get("tleg")))
    if key_ not in _CAP_PRINTED:   # mvt1 c46: one line per spec of a list (scherzo c20: rows and any_dyn in the key)
        _CAP_PRINTED.add(key_)
        print(f"{name}: release cap {ms:.0f} ms (RT {spec.get('rt_ms')}) on {sorted((k, sorted(v)) for k, v in hit.items())}", file=sys.stderr)


def leg_sus_attack(inst, spec, name):
    """scherzo c21 (critic A #4): mix.json "leg_sus_attack_ms" {"ms", "rows": [...] (default ["Leg Slur MAX"]),
    "prefix": [...] (default ["V1s", "V2s"])}: cap the AHDSR attack of the legato row's connected sustain groups (every
    region on the listed rows, name starting with a prefix) at ms. The Hollywood Strings KS Masters ship 841-1501 ms on
    these groups while the transition groups ("TLeg") reach full level in 116 ms, so a legato join crests on the
    transition and sags 2-3 dB at 0.2-0.45 s while the sustain fades in. The transition and detached groups keep theirs."""
    ms = float(spec["ms"])
    rows = [r["name"] for r in inst["layerMatrix"]["rows"]]
    want = {i for i, r in enumerate(rows) if r in spec.get("rows", ["Leg Slur MAX"])}
    pre = tuple(spec.get("prefix", ["V1s", "V2s"]))
    hit, n_ = set(), 0
    for g in inst.get("groups", []):
        regs = (g.get("regionMap") or {}).get("regions", [])
        if not regs or any(r_.get("row") not in want for r_ in regs) or not g["name"].startswith(pre):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "AHDSR" and pr_.get("attack", 0) > ms:
                hit.add(round(pr_["attack"]))
                pr_["attack"] = ms
                n_ += 1
    print(f"{name}: legato sustain attack cap {ms:.0f} ms on {n_} groups (were {sorted(hit)[:3]}..{sorted(hit)[-3:]})", file=sys.stderr)


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
        # scherzo c26 (critic A #1): optional "dyn": [...] limits the gain to trail groups whose name ends in "<dyn> RT"
        w_ = g["name"].split(" rr")[0].split(" RR")[0].split()
        if spec.get("dyn") and not (len(w_) >= 2 and w_[-1] == "RT" and w_[-2] in spec["dyn"]):
            continue
        for pr_ in (g.get("processors") or {}).get("processors", []):
            if pr_.get("class") == "SourceProcessor" and "volume" in pr_:
                pr_["volume"] = float(pr_["volume"]) * 10 ** (db_ / 20.0)
                n_ += 1
    print(f"{name}: release-trail gain {db_:+.1f} dB on {n_} groups", file=sys.stderr)


def region_gain(inst, spec, name):
    """scherzo c15 (critic A #1a; a range test, see cycles/c15/CHANGES.md): mix.json "region_gain_db" (per track)
    {"rows": [row names], "pitch_db": {"71": 4.5, ...}}: multiply the per-region `volume` (linear; absent = 1) of every
    region on a listed row whose key range holds a listed pitch by 10^(dB/20), so a per-pitch level correction is made
    inside Opus (before its hall, moving with each note's own sample) instead of in the track volume envelope.
    scherzo c16: the value may be a list of such specs (one pitch table per set of rows); row names match without
    case (the cor anglais patch names its row "Sus Max": c15's -3.5 dB for A4 on "Sus MAX" never reached it); and
    "row_dyn_db" {row: {layer: dB}} changes one dynamic layer of a row: layer "pp" / "p" / "mf" / "f" / "ff" selects the
    groups whose name ends in that dynamic (their release-trail groups " RT" too), layer "vel>=N" the regions of a
    velocity-switched short row whose lowest velocity is N or more.
    scherzo c17: layer "vel<N" (regions whose highest velocity is under N), and a spec key "dyn": ["f", ...] limits its
    "pitch_db" to the groups of those dynamic layers (a pitch that is hot in the loud layer only).
    scherzo c19 (critic A #1): layer "group:PREFIX" selects the regions of the row's groups whose name starts with PREFIX
    ("group:TLeg": the legato transition samples of a KS Master's "Leg Slur MAX" row, which CC11 cannot reach).
    scherzo c27 (critic A #4): spec key "vel_min": N limits "pitch_db" to regions whose lowest velocity is N or more."""
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
                if (l_.startswith("vel>=") and r_.get("velMin", 0) >= int(l_[5:])) or l_ == gdyn_ \
                        or (l_.startswith("vel<") and not l_.startswith("vel<=") and r_.get("velMax", 127) < int(l_[4:])) \
                        or (l_.startswith("group:") and gn_.startswith(l_[6:])):
                    r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (float(d_) / 20.0)
                    nd_ += 1
            if r_.get("row") not in want or (spec.get("dyn") and gdyn_ not in spec["dyn"]):
                continue
            if spec.get("vel_min") is not None and r_.get("velMin", 0) < int(spec["vel_min"]):
                continue   # scherzo c27 (critic A #4): "vel_min": the pitch gain only in regions whose lowest velocity is N+
            for p_, d_ in pd_.items():
                if r_.get("keyMin", -1) <= p_ <= r_.get("keyMax", -1):
                    r_["volume"] = float(r_.get("volume", 1.0)) * 10 ** (d_ / 20.0)
                    n_ += 1
                    break
    print(f"{name}: region gain on {n_} regions" + (f", dynamic-layer gain on {nd_}" if nd_ else ""), file=sys.stderr)


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
    if m_.get("leg_sus_attack_ms"):   # scherzo c21 (critic A #4)
        leg_sus_attack(inst, m_["leg_sus_attack_ms"], tr["name"])
    if m_.get("rt_gain_db"):
        rt_gain(inst, m_["rt_gain_db"], tr["name"])
    if m_.get("region_gain_db"):
        region_gain(inst, m_["region_gain_db"], tr["name"])
    if m_.get("stereo_double"):
        # scherzo c13 (critic C #2; HO manual p.141): mix.json "stereo_double" {"spread": 0..1, optional "direction",
        # "left", "right"} switches on the patch's own Stereo Double processor (class "StereoDouble", found in the
        # instrument's "Global Group", groups[0], not in the mixer) for a one-signal patch such as a DIV half section
        sd_n_ = 0
        for g_ in inst.get("groups", []):
            for pr_ in (g_.get("processors") or {}).get("processors", []):
                if pr_.get("class") == "StereoDouble":
                    pr_["active"] = True
                    for k_, v_ in m_["stereo_double"].items():
                        if not k_.startswith("_"):
                            pr_[k_] = v_
                    sd_n_ += 1
        print(f"{tr['name']}: stereo_double {m_['stereo_double']} on {sd_n_} processor(s)", file=sys.stderr)
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


_Q2S = None


def q2s_fast(q):
    """q2s with the tempo steps' start times computed once (the simplification pass calls it for every grid point)"""
    global _Q2S
    if _Q2S is None:
        qs_, t_, lq, lb, ts_ = [0.0], 0.0, 0.0, d["tempo"][0][1], [0.0]
        bp_ = [d["tempo"][0][1]]
        for tq, b in d["tempo"]:
            if tq <= 0:
                lb = b; bp_[0] = b
                continue
            t_ += (tq - lq) * 60 / lb
            lq, lb = tq, b
            qs_.append(tq); ts_.append(t_); bp_.append(b)
        _Q2S = (qs_, ts_, bp_)
    qs_, ts_, bp_ = _Q2S
    k = max(0, bisect.bisect_left(qs_, q) - 1)
    return ts_[k] + (q - qs_[k]) * 60 / bp_[k]


# scherzo c15: REAPER's volume-envelope fader scale (VOLTYPE 1). It is not a power law (716.2 at 0 dB, 483.9 at -12,
# 363.3 at -20, 171.0 at -40, 1000 at +12): the table was read with a bridge job (jobs/env_scale.lua)
_ES = json.load(open(next(p_ for p_ in (os.path.join(os.path.dirname(os.path.abspath(globals().get("__file__", "tools/x"))), "env_scale.json"),
                                          os.path.join(os.path.dirname(os.path.abspath(PARTS)), "..", "tools", "env_scale.json"),
                                          "tools/env_scale.json") if os.path.exists(p_))))


def ENV_SCALE(db):   # the table tools/env_scale.json (1 dB steps, read from REAPER), linear between its entries
    x = min(max((db - _ES["from_db"]) / _ES["step_db"], 0.0), len(_ES["scale"]) - 1.000001)
    i = int(x)
    return _ES["scale"][i] + (_ES["scale"][i + 1] - _ES["scale"][i]) * (x - i)


def ENV_UNSCALE(s):
    sc = _ES["scale"]
    i = min(max(bisect.bisect_right(sc, s) - 1, 0), len(sc) - 2)
    return _ES["from_db"] + _ES["step_db"] * (i + (s - sc[i]) / max(1e-12, sc[i + 1] - sc[i]))


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
# scherzo c25 (critic B #1, finale technique 135; Dan 2026-11-11: no per-note moves in the volume envelope). mix.json
# "dyn_trim_to_cc7" {"tracks": "all" or [names], "except": [names], "families_except": [families], "moved": true,
# "lead_s": 0.02} moves the dynamic trims (dyn_trim_db / soft_trim_db read from the printed dynamic curve, with the
# soft-decrescendo and crescendo holds) out of the post-hall volume envelope into CC7, which acts inside Opus before its
# hall (20 log10(CC7 / 127): mockup-kit LEARNINGS section 3; finale c26 / c27 range tests on HS strings and HO woodwind
# and brass KS Masters). The envelope holds gain + vol_db + the track's largest trim; CC7 = the lane's own CC7 x
# 10^((trim - largest) / 20), held in rests like the envelope's tail hold, ending on its last value. "moved": the trim is
# read on moved time: the dynamic curve's marks and hairpin starts / ends at a led note's score onset move to that
# note's moved onset (less lead_s), so a led note no longer plays its head at the previous dynamic's trim (c24: 163 led
# notes off by 1.5 dB or more; trombones / tuba at 993 by 12-15 dB). A --mix-only build does not rewrite CC7: after a
# trim change use --midi-only. Off when the key is absent
TRIM_CC7 = {}
TRIM_CC7_FAMILIES_EXCEPT = ("timp", "perc", "harp", "harm")


def trim_cc7_on(tr):
    spec = MIX.get("dyn_trim_to_cc7")
    if not spec or tr.get("family") in spec.get("families_except", TRIM_CC7_FAMILIES_EXCEPT):
        return False
    if tr["name"] in spec.get("except", []) or tr.get("cc7"):
        return False
    t = spec.get("tracks", "all")
    return t == "all" or tr["name"] in t


def dyn_warp(tr, dyn, lead_s=0.02, mark_cc=3):
    """scherzo c25: moved-time anchors of the printed dynamic curve, [(moved qn, score qn)] ascending in both. Anchors:
    every hairpin start and end and every mark (a step of mark_cc or more outside the hairpins). An anchor at the score
    onset of a led note (moved onset earlier) moves to that onset less lead_s; the others stay (identity)"""
    pts = {h0 for h0, _, _ in tr.get("hairpins", [])} | {h1 for _, h1, _ in tr.get("hairpins", [])}
    for (q0, c0), (q1, c1) in zip(dyn, dyn[1:]):
        if abs(c1 - c0) >= mark_cc and not any(h0 - 1e-6 <= q1 <= h1 + 1e-6 for h0, h1, _ in tr.get("hairpins", [])):
            pts.add(q1)
    by_sq = {}
    for n in tr.get("notes", []):
        sq = round(n.get("sq", n["qn"]), 3)
        by_sq[sq] = min(by_sq.get(sq, 9e9), n["qn"])
    out = []
    for a in sorted(pts):
        m_ = by_sq.get(round(a, 3))
        mv = a
        if m_ is not None and m_ < a - 1e-4:
            mv = s2q_fast(q2s_fast(m_) - lead_s)
        if out and mv <= out[-1][0] + 1e-3:
            mv = out[-1][0] + 1e-3
        out.append((round(mv, 5), a))
    return out


def warp_fn(anch):
    """moved qn -> score qn, piecewise linear through the anchors, identity outside"""
    if not anch:
        return lambda q: q
    ms = [m_ for m_, _ in anch]; ss = [s_ for _, s_ in anch]

    def W(q):
        k = bisect.bisect_right(ms, q + 1e-9)
        if k == 0:
            return min(q, ss[0] - 1e-4)   # before the first anchor: identity (the skipped score span holds one value)
        if k >= len(ms):
            return max(q, ss[-1])
        m0, m1, s0, s1 = ms[k - 1], ms[k], ss[k - 1], ss[k]
        return s0 + (s1 - s0) * (q - m0) / max(1e-9, m1 - m0)
    return W


def s2q_fast(t):
    """inverse of q2s_fast"""
    q2s_fast(0.0)
    qs_, ts_, bp_ = _Q2S
    k = max(0, bisect.bisect_right(ts_, t) - 1)
    return qs_[k] + (t - ts_[k]) * bp_[k] / 60.0


# scherzo c16 (critics A #4, B #2; Dan 2026-11-11: the volume envelope carries slow balance only). What was left of
# fast fader movement after c15 sat inside sounding notes: hairpin-gain and crescendo-trim releases on the arrival note
# (6-7.5 dB given back while the note is held), role edges that fall after a led note's start, roll-settle edges on
# the next stroke. mix.json "note_move_guard" (top level; absent = off):
#   {"max_db": 1.5, "skip_s": 0.04, "snap_s": 0.2, "rest_min_s": 0.04, "rest_ramp_s": 0.3, "rejoin_db_per_s": 2.5, "decay_s": 0.5, "decay_families": ["harp", "harm"], "decay_rows": ["Pizz"],
#    "free_rows": ["Rls", "Roll"], "mark_cc": 3}
# For every note, from skip_s after its score onset (or its moved onset if later) to its end, outside the printed
# zones (printed hairpins, printed dynamic marks, the subito tails, the final fade, notes on free_rows: timpani rolls
# keep their printed shape), the written envelope may move by at most max_db. A note that breaks this is changed:
#   - a move that is over within snap_s of the score onset (a role edge or a level step that belongs to the note's
#     start) is finished 10 ms before the onset, over 40 ms (on the join, or in the rest before the note);
#   - otherwise the level at the note's start is held to the note's end (or to the next printed zone) and the envelope
#     returns to its written course in the rest that follows (over at most rest_ramp_s, ending 30 ms before the next
#     note-on), across the printed zone, or, when the next note follows without a rest, at rejoin_db_per_s under the
#     following notes (never past the written course), each of which is checked in turn.
# Plucked and struck notes (decay_families, decay_rows) are checked over their first decay_s only.
# parts.json is not changed; the track dict gets "_nmg" = [notes changed by a snap, by a hold, notes still over 2 dB]
def note_move_guard(tr, grid, vals, cfg):
    mx_, skip_, snap_ = cfg.get("max_db", 1.5), cfg.get("skip_s", 0.04), cfg.get("snap_s", 0.2)
    rmin_, rramp_ = cfg.get("rest_min_s", 0.04), cfg.get("rest_ramp_s", 0.3)
    rate_ = cfg.get("rejoin_db_per_s", 2.5)
    T = q2s_fast
    G, V = list(grid), list(vals)

    def cur(q):
        k = bisect.bisect_left(G, q)
        if k <= 0:
            return V[0]
        if k >= len(G):
            return V[-1]
        return V[k - 1] + (V[k] - V[k - 1]) * (q - G[k - 1]) / max(1e-9, G[k] - G[k - 1])

    def splice(pts):
        """replace the curve between pts[0][0] and pts[-1][0] by the points pts (qn ascending)"""
        nonlocal G, V
        a_, b_ = pts[0][0], pts[-1][0]
        keep_l = [(q, v) for q, v in zip(G, V) if q < a_ - 1e-9]
        keep_r = [(q, v) for q, v in zip(G, V) if q > b_ + 1e-9]
        new = keep_l + [(round(q, 5), round(v, 2)) for q, v in pts] + keep_r
        G, V = [q for q, _ in new], [v for _, v in new]

    # rows per note (the last keyswitch at or before the note-on)
    ksq = sorted((k["qn"], k.get("art") or "") for k in tr.get("ks", []))
    def row_of(q):
        r = tr.get("first_art") or ""
        for kq, a in ksq:
            if kq <= q + 1e-6:
                r = a
            else:
                break
        return r
    fam = tr.get("family")
    decay_all = fam in cfg.get("decay_families", ["harp", "harm"])
    # printed zones (qn)
    zones = [(h0, h1) for h0, h1, _ in tr.get("hairpins", [])]
    mark_z = set()   # zones of printed dynamic marks
    dyn = tr.get("dyn_curve", [])
    for (q0, c0), (q1, c1) in zip(dyn, dyn[1:]):
        if abs(c1 - c0) >= cfg.get("mark_cc", 3) and not any(h0 - 1e-6 <= q1 <= h1 + 1e-6 for h0, h1, _ in tr.get("hairpins", [])):
            zones.append((q1 - 0.05, q1 + 0.3)); mark_z.add((q1 - 0.05, q1 + 0.3))
    for s_, f_ in tr.get("subito_falls", []):
        zones.append((min(f_, s_ - 0.1) - 0.01, s2q_fast(T(f_) + SUBITO_TAIL["ramp_s"]) + 0.01 if SUBITO_TAIL else s_ + 0.3))
    zones.append((TAIL_HOLD_STOP_QN - 5.5, grid[-1] + 10))
    notes = sorted(tr["notes"], key=lambda n: (n["qn"], n["qn"] + n["dur"]))
    for n in notes:
        if any(w in row_of(n["qn"]) for w in cfg.get("free_rows", ["Rls", "Roll"])):
            zones.append((n["qn"] - 0.05, n["qn"] + n["dur"] + 0.05))
    zones.sort()
    ons = sorted(n["qn"] for n in notes)
    ends = sorted((n["qn"] + n["dur"], n["qn"]) for n in notes)

    def sounding_after(q, skip=None):
        """is any note (other than skip) sounding at qn q"""
        return any(o["qn"] < q - 1e-6 and o["qn"] + o["dur"] > q + 1e-6 for o in notes if o is not skip)

    def unprot(a, b, entry_on=None):
        """the parts of [a, b] outside the printed zones. entry_on: the note enters after a rest at this qn; a printed
        mark that stands within 0.35 s after it is the entry's own dynamic (its step, keyed to the score onset, would
        land inside the led note): not a printed zone for this note, so the step is moved before the note-on"""
        out, x = [], a
        for z0, z1 in zones:
            if entry_on is not None and (z0, z1) in mark_z and entry_on - 0.06 <= z0 and T(z0) - T(entry_on) <= 0.35:
                continue
            if z1 <= x or z0 >= b:
                continue
            if z0 > x:
                out.append((x, min(z0, b)))
            x = max(x, z1)
            if x >= b:
                break
        if x < b:
            out.append((x, b))
        return [(u0, u1) for u0, u1 in out if u1 - u0 > 1e-4]

    def rng(u0, u1):
        vs = [cur(u0), cur(u1)] + [v for q, v in zip(G, V) if u0 < q < u1]
        return max(vs) - min(vs)
    def chk_span(n):
        """the checked stretch of a note: from skip_s after its score onset (or its note-on if later) to its end, or to
        10 ms before the next note-on of the track (the join belongs to the next note); None when too short"""
        sq = n.get("sq", n["qn"])
        # (Movement II c56 #4) a note that enters after a rest is checked from its moved note-on: an edge keyed to the
        # score onset lands 50-300 ms inside a led note; at a join the old note sounds up to the score onset
        on_ = n["qn"] if not sounding_after(s2q_fast(T(n["qn"]) - rmin_), n) else max(sq, n["qn"])
        a = s2q_fast(T(on_) + skip_)
        b = n["qn"] + n["dur"]
        k = bisect.bisect_right(ons, n["qn"] + 0.01)
        if k < len(ons):
            b = min(b, s2q_fast(T(ons[k]) - 0.01))
        if decay_all or any(w in row_of(n["qn"]) for w in cfg.get("decay_rows", ["Pizz"])):
            b = min(b, s2q_fast(T(a) + cfg.get("decay_s", 0.5)))
        return (sq, a, b, n["qn"] if on_ == n["qn"] and sq > n["qn"] + 1e-6 else None) if b - a >= 0.02 else None
    snaps = holds = 0
    for pass_ in range(cfg.get("passes", 3)):
        changed = 0
        for n in notes:
            cs = chk_span(n)
            if not cs:
                continue
            sq, a, b, ent_ = cs
            for u0, u1 in unprot(a, b, ent_):
                if rng(u0, u1) <= mx_:
                    continue
                # where the envelope moves inside the part
                qs_ = [u0] + [q for q in G if u0 < q < u1] + [u1]
                vs_ = [cur(q) for q in qs_]
                mv_ = [k for k in range(1, len(qs_)) if abs(vs_[k] - vs_[k - 1]) > 0.02]
                m1 = qs_[mv_[-1]]
                after_ = s2q_fast(T(m1) + 0.1)
                if u0 == a and T(m1) - T(max(sq, n["qn"])) <= snap_ and m1 < u1 - 1e-6 and abs(cur(after_) - cur(m1)) < 0.1:
                    # snap: a move that is over early in the note belongs to its start
                    on_ = min(sq, n["qn"])
                    if not sounding_after(s2q_fast(T(on_) - rmin_), n):   # after a rest: finished 10 ms before the note-on
                        x1 = s2q_fast(T(on_) - 0.01); x0 = s2q_fast(T(x1) - 0.04)
                    else:                                                 # a join: centred on the score onset
                        x0, x1 = s2q_fast(T(sq) - 0.02), s2q_fast(T(sq) + 0.02)
                    v1 = cur(m1)
                    splice([(x0, cur(x0)), (x1, v1), (m1, v1)])
                    snaps += 1; changed += 1
                    continue
                at_end = abs(u1 - b) < 1e-6
                if u0 == a and not at_end and T(u1) - T(a) <= snap_:
                    # a short stretch between the note's start and a printed zone: the level the zone starts on is
                    # reached before the note (a role or mark step followed at once by a printed hairpin)
                    on_ = min(sq, n["qn"])
                    if not sounding_after(s2q_fast(T(on_) - rmin_), n):
                        x1 = s2q_fast(T(on_) - 0.01); x0 = s2q_fast(T(x1) - 0.04)
                    else:
                        x0, x1 = s2q_fast(T(sq) - 0.02), s2q_fast(T(sq) + 0.02)
                    v1 = cur(u1)
                    splice([(x0, cur(x0)), (x1, v1), (u1, v1)])
                    snaps += 1; changed += 1
                    continue
                vh = cur(u0)
                if not at_end:   # the next printed zone: return across it (at most 1.5 s)
                    z1 = max([z_[1] for z_ in zones if z_[0] <= u1 + 1e-6 < z_[1]], default=u1 + 0.5)
                    c = min(z1, s2q_fast(T(u1) + 1.5))
                    splice([(u0, vh), (u1, vh), (c, cur(c))])
                else:
                    e_ = n["qn"] + n["dur"]
                    nxt = [o for o in ons if o > n["qn"] + 0.01]
                    gap_s = (T(nxt[0]) - T(e_)) if nxt else 9.0
                    if gap_s >= rmin_ and not sounding_after(e_ + 1e-4, n):
                        if nxt:
                            c1 = s2q_fast(T(nxt[0]) - 0.03) if gap_s > 0.06 else nxt[0]
                            c0 = max(e_, s2q_fast(T(c1) - rramp_))
                        else:
                            c0, c1 = e_, s2q_fast(T(e_) + rramp_)
                        splice([(u0, vh), (c0, vh), (c1, cur(c1))])
                    else:   # no rest: the level closes on the written course at rejoin_db_per_s under the next notes
                        pts_, t_, v_ = [(u0, vh), (b, vh)], T(b), vh
                        while True:
                            t_ += 0.05
                            q_ = s2q_fast(t_)
                            tg_ = cur(q_)
                            v_ += max(-rate_ * 0.05, min(rate_ * 0.05, tg_ - v_))
                            if abs(tg_ - v_) < 0.02 or t_ - T(b) > 15.0:
                                pts_.append((q_, tg_))
                                break
                            pts_.append((q_, v_))
                            zn_ = [z_ for z_ in zones if z_[0] <= q_ < z_[1]]
                            if zn_:      # a printed zone: return across it (at most 1.5 s)
                                c = min(max(z_[1] for z_ in zn_), s2q_fast(t_ + 1.5))
                                if c > q_ + 1e-4:
                                    pts_.append((c, cur(c)))
                                break
                            if not sounding_after(q_, None):   # a rest: return in it
                                nx_ = [o for o in ons if o > q_]
                                c1 = min(s2q_fast(t_ + rramp_), s2q_fast(T(nx_[0]) - 0.03)) if nx_ else s2q_fast(t_ + rramp_)
                                if c1 > q_ + 1e-4:
                                    pts_.append((c1, cur(c1)))
                                break
                        splice(pts_)
                holds += 1; changed += 1
        if not changed:
            break
    # what is left over 2 dB (reported, not changed)
    left = []
    for n in notes:
        cs = chk_span(n)
        if not cs:
            continue
        r_ = max([rng(u0, u1) for u0, u1 in unprot(cs[1], cs[2], cs[3])], default=0.0)
        if r_ > 2.0:
            left.append([round(cs[0], 3), round(r_, 1)])
    tr["_nmg"] = [snaps, holds, left]
    return G, V


# scherzo c24 (critic B #1, Dan 2026-11-11: no per-note volume moves). note_move_guard leaves printed zones (hairpins,
# the 0.35 qn after a printed mark, subito tails) alone, and a step drawn on the score onset of a led note (a legato
# target, an entry) lands 0.05-0.5 s inside the sounding note: 175 notes of c23 held a step of 1.5 dB or more at
# more than 6 dB/s (critic B's 2 dB / 20 dB/s: 59), most at printed marks inside led notes, at the sfp's spike shape
# in the dynamic trims, and at role edges. mix.json "note_slew" (top level; absent = off):
#   {"rate_db_s": 5.5, "rest_s": 0.005, "free_rows": ["Rls", "Roll"], "skip_tracks": ["Timpani"]}
# A note sounds from its moved note-on to its written end; notes less than rest_s apart (legato overlaps, joins) make
# one sounding stretch. Inside a stretch the envelope changes by at most rate_db_s: a backward pass makes every move
# complete at its written time and start earlier (a role or trim step on a led note's score onset becomes a ramp that
# ends there; a fast trim fall inside a short printed crescendo starts before it). A stretch that starts after a rest
# takes its first value in that rest (a step from 30 to 10 ms before the note-on, as note_move_guard's snap, or inside
# a shorter rest, between the previous note's end and the note-on: a re-attack after a gap starts at its own level). Rests and
# notes on free_rows keep the written values. The written course is reached again at the end of every stretch.
def note_slew(tr, grid, vals, cfg):
    R = cfg.get("rate_db_s", 5.5)
    rest_ = cfg.get("rest_s", 0.005)
    T, S = q2s_fast, s2q_fast
    ksq = sorted((k["qn"], k.get("art") or "") for k in tr.get("ks", []))

    def row_of(q):
        r = tr.get("first_art") or ""
        for kq, a in ksq:
            if kq <= q + 1e-6:
                r = a
            else:
                break
        return r
    notes = [n for n in tr["notes"] if not any(w in row_of(n["qn"]) for w in cfg.get("free_rows", ["Rls", "Roll"]))]
    if not notes:
        return grid, vals
    G, V = list(grid), list(vals)

    def cur(q):
        k = bisect.bisect_left(G, q)
        if k <= 0:
            return V[0]
        if k >= len(G):
            return V[-1]
        return V[k - 1] + (V[k] - V[k - 1]) * (q - G[k - 1]) / max(1e-9, G[k] - G[k - 1])
    segs = sorted((T(n["qn"]), T(n["qn"] + n["dur"])) for n in tr["notes"])
    mask = sorted((T(n["qn"]), T(n["qn"] + n["dur"])) for n in notes)
    if cfg.get("skip_hairpins"):
        # finale c27 (coordinator, 2026-11-17): printed hairpins are not rate-limited: their spans are free stretches
        hz = sorted((T(h0), T(h1)) for h0, h1, _ in tr.get("hairpins", []))
        cut = []
        for a_, b_ in mask:
            pcs = [(a_, b_)]
            for h0, h1 in hz:
                pcs = [x for x0, x1 in pcs for x in ((x0, min(x1, h0)), (max(x0, h1), x1)) if x[1] - x[0] > 1e-4]
            cut += pcs
        mask = sorted(cut)
    merged = []
    for a_, b_ in mask:
        if merged and a_ <= merged[-1][1] + rest_:
            merged[-1][1] = max(merged[-1][1], b_)
        else:
            merged.append([a_, b_])
    step = 0.01
    out_pts, spans = {}, []
    # scherzo c27 (critic B #3): optional "onset_step_s": at a re-attack join (a note-on whose previous note ends within
    # 0.03 s before it, with no note sounding across it) a written move within onset_step_s of the note-on stays a step
    # 0.02 s before the note-on and the backward pass does not carry it into the note before (role edges at joins were
    # ramped across the whole earlier note: Violins I 1012 -2.1 dB inside an accented note)
    os_ = cfg.get("onset_step_s")
    joins_ = []
    if os_:
        for n in notes:
            t_ = T(n["qn"])
            if any(x_ < t_ - 1e-6 and y_ > t_ + 0.005 for x_, y_ in segs):
                continue
            if any(x_ < t_ - 1e-6 and t_ - 0.03 <= y_ <= t_ + 0.005 for x_, y_ in segs):
                if abs(cur(S(t_ + os_)) - cur(S(t_ - 0.02))) >= 0.05:
                    joins_.append(t_)
        joins_ = sorted(set(round(x_, 5) for x_ in joins_))
    for a_, b_ in merged:
        if b_ - a_ < 0.01:
            continue
        # after a rest (no note of the track, free rows included, sounds within rest_s before): the start is free
        free0 = not any(x_ < a_ - 1e-6 and y_ > a_ - rest_ for x_, y_ in segs)
        ts = [a_ + k * step for k in range(int((b_ - a_) / step) + 1)] + [b_]
        jn_ = [j_ for j_ in joins_ if a_ + 0.03 < j_ < b_ - 1e-4]
        ts = sorted(set(round(x, 5) for x in ts) | {round(T(q), 5) for q in G if S(a_) < q < S(b_)}
                    | {round(j_ - 0.02, 5) for j_ in jn_} | {round(j_ - 0.021, 5) for j_ in jn_})
        e = [cur(S(x)) for x in ts]
        for j_ in jn_:   # the move's after-value from 0.02 s before the note-on
            v_ = cur(S(j_ + os_))
            e = [v_ if j_ - 0.02 - 1e-6 <= x <= j_ + os_ else ev for x, ev in zip(ts, e)]
        if max(e) - min(e) < 0.05:
            continue
        y = e[:]
        brk_ = {k for k in range(len(ts) - 1) for j_ in jn_ if ts[k] < j_ - 0.02 - 1e-6 <= ts[k + 1]}
        # scherzo c24 (coordinator, Movement I c62: a guard moved join ramps 19 qn back): optional "max_ramp_qn": a
        # written move of D dB may start at most this many qn before it ends, at max(rate, D / that time) (it then
        # breaks the rate; the guard lists it)
        rk = [R] * len(ts)
        mrq_ = cfg.get("max_ramp_qn")
        if mrq_:
            k = 0
            while k < len(ts) - 1:
                if abs(e[k + 1] - e[k]) > R * (ts[k + 1] - ts[k]) + 1e-9:
                    j = k
                    while j < len(ts) - 1 and abs(e[j + 1] - e[j]) > R * (ts[j + 1] - ts[j]) + 1e-9 and (e[j + 1] - e[j]) * (e[k + 1] - e[k]) > 0:
                        j += 1
                    lm_ = T(S(ts[j]) - 0.0) - T(S(ts[j]) - mrq_)
                    rr_ = max(R, abs(e[j] - e[k]) / max(1e-6, lm_))
                    for i in range(len(ts)):
                        if ts[j] - lm_ - 1e-9 <= ts[i] <= ts[j]:
                            rk[i] = max(rk[i], rr_)
                    k = j
                else:
                    k += 1
        for k in range(len(ts) - 2, -1, -1):
            if k in brk_:
                continue   # scherzo c27: a kept onset step
            dt = ts[k + 1] - ts[k]
            y[k] = max(y[k + 1] - rk[k] * dt, min(y[k + 1] + rk[k] * dt, y[k]))
        if not free0 and abs(y[0] - e[0]) > 0.05:
            # joined to a free-row note: the start keeps its value, the stretch climbs at the rate (forward)
            for k in range(1, len(ts)):
                dt = ts[k] - ts[k - 1]
                y[k] = max(y[k - 1] - rk[k] * dt, min(y[k - 1] + rk[k] * dt, y[k]))
            y[0] = e[0]
        if max(abs(p - q) for p, q in zip(y, e)) < 0.05:
            continue
        x0 = a_
        if free0 and abs(y[0] - e[0]) >= 0.05:
            pe_ = max([y_ for x_, y_ in segs if x_ < a_ - 1e-6 and y_ <= a_ + 1e-6], default=a_ - 1.0)
            j0, j1 = max(a_ - 0.03, pe_ + 0.001), max(a_ - 0.01, pe_ + 0.003)
            j1 = min(j1, a_ - 0.0005); j0 = min(j0, j1 - 0.0005)
            x0 = j0
            out_pts[S(j0)] = cur(S(j0))
            out_pts[S(j1)] = y[0]
        for x, v in zip(ts, y):
            out_pts[S(x)] = v
        spans.append((S(x0), S(b_)))
    if not spans:
        return G, V
    keep = [(q, v) for q, v in zip(G, V) if not any(s0 - 1e-6 <= q <= s1 + 1e-6 for s0, s1 in spans)]
    new = sorted(keep + list(out_pts.items()))
    tr["_nsl"] = len(spans)
    return [round(q, 5) for q, _ in new], [round(v, 2) for _, v in new]


def stretch_cc7(tr, grid, vals):
    """scherzo c26 (critic B #1, #3; finale technique 136; Dan's rule): mix.json dyn_trim_to_cc7 "stretch_cc7" {"max_qn": N,
    "floor_db": F, "except": [names]}. Applied to the finished envelope (after note_move_guard and note_slew): its moves
    inside sounding stretches (notes less than 5 ms apart) go into the CC7 lane, before the hall. A stretch of at most N
    qn keeps one envelope level, its highest, from the end of the tail hold in the rest before it to its end; CC7 carries
    the difference (ramps resampled every 10 ms), so the level heard is unchanged and every envelope step falls in a
    rest. In a longer stretch only the falls in its last N qn are held to its end (rises stay in the envelope). A stretch
    whose CC7 would go under F dB (with the trim lane) keeps its envelope. The final fade (TAIL_HOLD_STOP_QN on) is left
    alone. Returns grid, vals and the CC7 offsets [(qn, dB <= 0)] (steps), to be added to the trim lane."""
    cfg = (MIX.get("dyn_trim_to_cc7") or {}).get("stretch_cc7")
    if not cfg or not tr.get("notes") or tr["name"] in cfg.get("except", []) or not trim_cc7_on(tr):
        return grid, vals, []
    mx_q, fl = float(cfg.get("max_qn", 16.0)), float(cfg.get("floor_db", -30.0))
    tl = TRIM_CC7.get(tr["name"]) or [(grid[0], 0.0)]
    tq = [q for q, _ in tl]
    t_at = lambda q: tl[max(0, bisect.bisect_right(tq, q + 1e-9) - 1)][1]
    sg = sorted((n["qn"], n["qn"] + n["dur"]) for n in tr["notes"])
    strs, (a0, b0) = [], sg[0]
    for a_, b_ in sg[1:]:
        if q2s_fast(a_) - q2s_fast(b0) < 0.005:
            b0 = max(b0, b_)
        else:
            strs.append((a0, b0)); a0, b0 = a_, b_
    strs.append((a0, b0))
    G, V = list(grid), list(vals)
    off = {}            # grid index -> offset
    ins = []            # (q, env, offset) extra points
    ends = []           # (stretch end, env, offset, original value there)
    starts = []         # (h0, env, offset)
    holds = []          # (stretch end, last grid index inside)
    moved = kept = 0
    prev_end = -1e9
    for a_, b_ in strs:
        if b_ > TAIL_HOLD_STOP_QN:   # a stretch that reaches the final fade keeps its envelope
            prev_end = max(prev_end, b_); continue
        h0 = s2q(q2s(a_) - TAIL_HOLD_LEAD_S) if q2s(a_) - q2s(prev_end) >= TAIL_HOLD_MIN_S else prev_end + 0.002
        h0 = min(max(h0, prev_end + 0.002), a_)
        ks = [k for k, q in enumerate(G) if h0 - 1e-6 <= q < b_ - 1e-6]
        prev_end = b_
        kz_ = bisect.bisect_left(G, b_ - 1e-6) - 1   # the last grid point inside the stretch: its level is held to b_
        if kz_ >= 0 and G[kz_] >= a_ - 1e-6:
            holds.append((round(b_, 5), kz_))
        if len(ks) < 2:
            continue
        nv = {}
        if b_ - a_ <= mx_q:
            M = max(V[k] for k in ks)
            if any(t_at(G[k]) + V[k] - M < fl for k in ks):
                kept += 1; continue
            nv = {k: M for k in ks}
        else:
            H = None
            for k in ks:
                if H is None or V[k] >= H or b_ - G[k] > mx_q:
                    H = V[k]
                elif t_at(G[k]) + V[k] - H >= fl:
                    nv[k] = H
                else:
                    H = V[k]
        if not any(abs(nv[k] - V[k]) > 1e-6 for k in nv):
            continue
        moved += 1
        if b_ - a_ <= mx_q:   # the stretch level from h0 on (h0 may fall between grid points)
            k0_ = min(nv)
            if G[k0_] > h0 + 1e-6 and k0_ > 0:
                vh_ = V[k0_ - 1] + (V[k0_] - V[k0_ - 1]) * (h0 - G[k0_ - 1]) / max(1e-9, G[k0_] - G[k0_ - 1])
                starts.append((round(h0, 5), nv[k0_], vh_ - nv[k0_]))
                if abs(V[k0_] - vh_) > 0.3:   # resample the segment from h0 to the first moved point
                    n_ = max(1, int((q2s_fast(G[k0_]) - q2s_fast(h0)) / 0.01))
                    for j in range(1, n_):
                        q_ = h0 + (G[k0_] - h0) * j / n_
                        v_ = V[k0_ - 1] + (V[k0_] - V[k0_ - 1]) * (q_ - G[k0_ - 1]) / max(1e-9, G[k0_] - G[k0_ - 1])
                        ins.append((q_, nv[k0_], v_ - nv[k0_]))
        for k in sorted(nv):   # every envelope segment from a moved point (to the next point or the stretch end)
            if k + 1 < len(G) and abs(V[k + 1] - V[k]) > 0.3:
                qe_ = min(G[k + 1], b_)
                n_ = max(1, int((q2s_fast(qe_) - q2s_fast(G[k])) / 0.01))
                for j in range(1, n_ + (0 if qe_ == G[k + 1] else 1)):
                    q_ = G[k] + (qe_ - G[k]) * j / n_
                    if q_ >= b_ - 1e-6:
                        break
                    v_ = V[k] + (V[k + 1] - V[k]) * (q_ - G[k]) / max(1e-9, G[k + 1] - G[k])
                    ins.append((q_, nv.get(k + 1, nv[k]) if (k + 1) in nv and nv[k + 1] == nv[k] else nv[k], v_ - nv[k]))
        kl = max(nv)
        if kl + 1 < len(G) and G[kl] < b_ - 1e-6:
            vb_ = V[kl] + (V[kl + 1] - V[kl]) * (b_ - G[kl]) / max(1e-9, G[kl + 1] - G[kl])
            ends.append((round(b_, 5), nv[kl], vb_ - nv[kl], vb_))
        for k in nv:
            off[k] = V[k] - nv[k]
            vals[k] = round(nv[k], 2)
    if moved or kept:
        print(f"{tr['name']}: stretch_cc7 moved the envelope of {moved} stretches into CC7 ({kept} kept: floor)", file=sys.stderr)
    pts = {G[k]: (vals[k], round(off.get(k, 0.0), 2)) for k in range(len(G))}
    for q, e_, o_ in ins:
        pts.setdefault(round(q, 5), (round(e_, 2), round(o_, 2)))
    for q, k_ in holds:   # every stretch ends on its own level (the envelope's step after it falls in the rest)
        if q not in [e[0] for e in ends]:
            pts[q] = (vals[k_], round(off.get(k_, 0.0), 2))
    for q, e_, o_ in starts:
        pts[q] = (round(e_, 2), round(o_, 2))
    for q, e_, o_, vb_ in ends:   # the stretch level up to its end (also on a grid point there), then the step
        nx_ = round(q + 0.002, 5)
        if nx_ not in pts:
            k_ = bisect.bisect_right(G, nx_) 
            pts[nx_] = (round(vals[k_], 2), round(off.get(k_, 0.0), 2)) if k_ < len(G) and G[k_] - nx_ < 1e-3 else (round(vb_, 2), 0.0)
        pts[q] = (round(e_, 2), round(o_, 2))
    grid = sorted(pts)
    vals = [pts[q][0] for q in grid]
    offs, last = [], None
    for q in grid:
        o_ = pts[q][1]
        if o_ != last:
            offs.append((q, o_)); last = o_
    # merge into the trim lane (both steps)
    oq = [q for q, _ in offs]
    o_at = lambda q: offs[max(0, bisect.bisect_right(oq, q + 1e-9) - 1)][1] if offs and q >= oq[0] - 1e-9 else 0.0
    lane, lv = [], None
    for q in sorted(set(tq) | set(oq)):
        v_ = round(max(-60.0, t_at(q) + o_at(q)), 2)
        if v_ != lv:
            lane.append((q, v_)); lv = v_
    TRIM_CC7[tr["name"]] = lane
    return grid, vals, offs


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
    g = m["gain_db"] + MIX.get("global_gain_db", 0.0)   # scherzo c26 (critic B #6): mix.json "global_gain_db" on every track; c02: with a volume envelope REAPER ignores D_VOL (measured: every gain was lost), so the gain goes in here
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

    # scherzo c14 (critic C #2): CRESC_TRIM_HOLD, the crescendo counterpart of the soft-decrescendo hold. The trim tables
    # fall toward f (winds p +5, f -4), so across a crescendo the envelope took back 0.9-1.05 dB per 10 CC of the rise:
    # 40 of 215 printed crescendos did not rise on their own stem (c13). mix.json "cresc_trim_hold" (top level, or per
    # track; None / absent = off): {"keep": k, "release_s": r, "groups": [...] (optional: only these mix groups),
    # "max_hold_db": m (optional), "skip": [[q0, q1], ...] (optional: hairpins that start in a span are left alone)}. Inside each "cresc" hairpin whose table trim is lower at its end than at its start,
    # from the hairpin's start to the moved onset of the first note at or after its end, the trim falls only by `keep`
    # of its fall below the value at the start (the held amount is at most max_hold_db); from that onset the held
    # amount goes back to the table value linearly over release_s seconds (a crescendo rises, then settles)
    cholds = []
    cth_ = m.get("cresc_trim_hold", MIX.get("cresc_trim_hold"))
    if cth_ and "groups" in cth_ and m.get("group") not in cth_["groups"]:
        cth_ = None
    if dyn and cth_:
        ons_c = sorted((n.get("sq", n["qn"]), n["qn"]) for n in tr.get("notes", []))
        for h0, h1, k_ in tr.get("hairpins", []):
            if k_ != "cresc" or any(a_ - 1e-6 <= h0 < b_ for a_, b_ in cth_.get("skip", [])):
                continue
            e_ = next((mq_ for sq_, mq_ in ons_c if sq_ >= h1 - 1e-6), h1)
            t0_ = trim(step_at(dyn, h0, first))
            if trim(step_at(dyn, max(e_, h1), first)) < t0_ - 1e-6:
                if cth_.get("release_at") == "mark":
                    # scherzo c27 (critic B #1): the held amount stays until the next printed change after the
                    # arrival (a mark or a hairpin start: the first dyn_curve point after the arrival with another
                    # value), at most max_hold_qn after the arrival, then goes back over release_s (it went back over
                    # release_s from the arrival: a 1-3 dB fade inside f / ff arrival notes with nothing printed)
                    v0_ = step_at(dyn, max(e_, h1) + 1e-4, first)
                    cap_ = max(e_, h1) + cth_.get("max_hold_qn", 16.0)
                    mk_ = next((q_ for q_, v_ in dyn if q_ > max(e_, h1) + 1e-4 and v_ != v0_), cap_)
                    if cth_.get("hold_through_rise"):
                        # scherzo c28 (critic B #2): a new crescendo is not a release point (the held amount follows the
                        # table as the curve rises); the hold ends where the curve first falls under the arrival's value
                        mk_ = next((q_ for q_, v_ in dyn if q_ > max(e_, h1) + 1e-4 and v_ < v0_ - 1e-6), cap_ + 1e9)
                    e2_ = min(mk_, cap_)
                    if mk_ > cap_ and cth_.get("hold_to_dec_qn"):
                        # scherzo c28 (critic B #1): no printed change within the cap: the held amount stays to a printed
                        # decrescendo that starts within hold_to_dec_qn of the arrival, when the curve does not fall and
                        # the track has no rest of rest_min_qn or more before it; released across the decrescendo
                        ar_ = max(e_, h1)
                        d_ = sorted((a2_, b2_) for a2_, b2_, k2_ in tr.get("hairpins", [])
                                    if k2_ == "decresc" and ar_ + 1e-4 < a2_ <= ar_ + cth_["hold_to_dec_qn"])
                        if d_:
                            d0_, d1_ = d_[0]
                            sg_ = sorted((n.get("sq", n["qn"]), n.get("sq", n["qn"]) + n["dur"]) for n in tr.get("notes", []))
                            ce_, gap_ = None, False
                            for a2_, b2_ in sg_:
                                if a2_ >= d0_:
                                    break
                                if ce_ is not None and a2_ > ar_ and a2_ - ce_ >= cth_.get("rest_min_qn", 2.0) - 1e-6:
                                    gap_ = True
                                    break
                                ce_ = b2_ if ce_ is None else max(ce_, b2_)
                            fall_ = any(v_ < v0_ - 1e-6 for q_, v_ in dyn if ar_ + 1e-4 < q_ < d0_)
                            if not gap_ and not fall_:
                                cholds.append((h0, d0_, t0_, d1_, max(0.05, q2s(d1_) - q2s(d0_))))
                                continue
                    if mk_ > cap_ and cth_.get("rest_extra_qn"):
                        # at the cap: a gap of 0.25 qn or more between the track's notes starting within rest_extra_qn
                        # takes the release
                        sg_ = sorted((n["qn"], n["qn"] + n["dur"]) for n in tr.get("notes", []))
                        # the trim is read on moved time through the dyn_trim_to_cc7 warp (trim_at(W(q))): a position
                        # in the moved notes is W(position) in the trim's frame
                        Wc_ = lambda q: q
                        if trim_cc7_on(tr) and (MIX.get("dyn_trim_to_cc7") or {}).get("moved", True):
                            Wc_ = warp_fn(dyn_warp(tr, dyn, MIX["dyn_trim_to_cc7"].get("lead_s", 0.02)))
                        ce_, got_ = None, False
                        for a2_, b2_ in sg_:
                            if ce_ is not None and a2_ - ce_ >= 0.25 and ce_ >= cap_ - 1e-6:
                                if ce_ <= cap_ + cth_["rest_extra_qn"]:
                                    e2_, got_ = Wc_(ce_ + 0.005), True
                                    rl_ = max(0.02, min(cth_["release_s"], q2s(Wc_(a2_)) - q2s(e2_) - 0.025))
                                break
                            ce_ = b2_ if ce_ is None else max(ce_, b2_)
                        if not got_:
                            # no rest: a step at the next re-attack (no note sounding across its note-on) within
                            # rest_extra_qn, finished at that note-on (a passage level at a note-on)
                            ra_ = [a2_ for a2_, _ in sg_ if cap_ - 1e-6 <= a2_ <= cap_ + cth_["rest_extra_qn"]
                                   and not any(x_ < a2_ - 1e-6 and y_ > a2_ + 0.01 for x_, y_ in sg_)]
                            if ra_:
                                e2_ = s2q(q2s(Wc_(ra_[0])) - 0.03)
                                cholds.append((h0, e2_, t0_, s2q(q2s(e2_) + 0.025), 0.025))
                                continue
                        else:
                            cholds.append((h0, e2_, t0_, s2q(q2s(e2_) + rl_), rl_))
                            continue
                    cholds.append((h0, e2_, t0_, s2q(q2s(e2_) + cth_["release_s"])))
                else:
                    cholds.append((h0, e_, t0_, s2q(q2s(e_) + cth_["release_s"])))

    def trim_at(q):
        t_ = trim(step_at(dyn, q, first))
        for a_, b_, cap_, keep_ in holds:
            if a_ - 1e-9 <= q < b_ - 1e-9 and t_ > cap_:
                t_ = cap_ + keep_ * (t_ - cap_)
        hm_, tt_ = 0.0, t_
        for a_, b_, t0_, r_, *rs_ in cholds:   # overlapping hairpins (or one hairpin's release under the next) do not add up
            if a_ - 1e-9 <= q < r_ - 1e-9 and tt_ < t0_:
                h_ = min((1.0 - cth_["keep"]) * (t0_ - tt_), cth_.get("max_hold_db", 99.0))
                if q >= b_:
                    h_ *= max(0.0, 1.0 - (q2s(q) - q2s(b_)) / max(rs_[0] if rs_ else cth_["release_s"], 1e-6))
                hm_ = max(hm_, h_)
        return t_ + hm_
    # scherzo c15 (ONE_TIME_c15 item 1): the layer test. parts.json `vol_cls` holds vol_db split into the classes slow,
    # level and shape (score_to_parts.py vol_add). ENV_SHAPE=off writes the envelope without the shape class, ENV_SHAPE=capN
    # with the shape class limited to +-N dB (analysis and range tests only; unset = vol_db as written)
    es_ = os.environ.get("ENV_SHAPE", "")
    if es_ and tr.get("vol_cls"):
        cl_ = tr["vol_cls"]
        cap_ = 0.0 if es_ == "off" else float(es_[3:])
        vol_at = lambda q: step_at(cl_["slow"], q) + step_at(cl_["level"], q) + max(-cap_, min(cap_, step_at(cl_["shape"], q)))
    else:
        vol_at = lambda q: step_at(vol, q)
    val_at = lambda q: round(g + vol_at(q) + (trim_at(q) if dyn else 0.0), 2)
    c7m = bool(dyn) and trim_cc7_on(tr)   # scherzo c25: dyn_trim_to_cc7 (see TRIM_CC7)
    tl = None
    if c7m:
        spec_ = MIX["dyn_trim_to_cc7"]
        W_ = lambda q: q
        if spec_.get("moved", True):
            anch_ = dyn_warp(tr, dyn, spec_.get("lead_s", 0.02))
            W_ = warp_fn(anch_)
            grid = sorted(set(grid) | {m_ for m_, s_ in anch_ if abs(m_ - s_) > 1e-4 and 0 <= m_ < grid[-1]})
        tv_ = [trim_at(W_(q)) for q in grid]
        tmax_ = max(tv_)
        # the envelope may not pass env_max_db (REAPER's volume envelope range, +24 dB; env_scale.json ends there): on a
        # track whose gain + vol_db + largest trim would pass it, CC7 carries the trims up to tc and the envelope the rest
        # (the softest dynamics' share above tc stays a step in the envelope, on moved time too)
        vmax_ = max(g + vol_at(q) for q in grid)
        tc_ = min(tmax_, spec_.get("env_max_db", 23.0) - vmax_)
        grid_c7_ = list(grid)
        tv_at_ = lambda q: tv_[max(0, bisect.bisect_right(grid_c7_, q + 1e-9) - 1)]
        val_at = lambda q: round(g + vol_at(q) + tc_ + max(0.0, tv_at_(q) - tc_), 2)
        tl = [round(min(t_, tc_) - tc_, 2) for t_ in tv_]
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

        def tl_at(q):   # scherzo c25: the CC7 trim lane before the holds, as a step on the grid
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
    # scherzo c25 (critic B #4, #5; Dan's rule): mix.json per track "cc7_spans_db" [[q0, q1, dB, ramp_in_qn, ramp_out_qn],
    # ...] (project qn, moved time): passage levels before the hall, added to the CC7 trim lane (0 at q0, dB from
    # q0 + ramp_in to q1, 0 again at q1 + ramp_out; ramps sampled every 10 ms). The lane stays at or under 0 dB (CC7 127):
    # a lift is cut there, with a warning. Put the edges in rests or at moved note-ons
    sp7_ = m.get("cc7_spans_db") or []
    if sp7_ and tl is None and trim_cc7_on(tr):
        tl = [0.0] * len(grid)
    if tl is not None:   # scherzo c25: the CC7 trim lane (qn, dB <= 0), changes only
        lane_ = [(q, t_) for k, (q, t_) in enumerate(zip(grid, tl)) if k == 0 or t_ != tl[k - 1]]
        if sp7_:
            lq_ = [q for q, _ in lane_]
            l_at_ = lambda q: lane_[max(0, bisect.bisect_right(lq_, q + 1e-9) - 1)][1]

            def sp_at(q):
                v_ = 0.0
                for r_ in sp7_:
                    a_, b_, db_ = r_[0], r_[1], r_[2]
                    ri_, ro_ = (r_[3] if len(r_) > 3 else 0.0), (r_[4] if len(r_) > 4 else 0.0)
                    if a_ - 1e-9 <= q < b_ + ro_:
                        f_ = min(1.0, (q - a_) / ri_) if ri_ > 0 else 1.0
                        if q >= b_:
                            f_ = min(f_, 1.0 - (q - b_) / ro_) if ro_ > 0 else 0.0
                        v_ += db_ * max(0.0, f_)
                return v_
            xs_ = set(lq_)
            for r_ in sp7_:
                a_, b_ = r_[0], r_[1]
                ri_, ro_ = (r_[3] if len(r_) > 3 else 0.0), (r_[4] if len(r_) > 4 else 0.0)
                for x0_, x1_ in ((a_, a_ + ri_), (b_, b_ + ro_)):
                    k_ = max(1, int((q2s_fast(x1_) - q2s_fast(x0_)) / 0.01))
                    xs_ |= {x0_ + (x1_ - x0_) * j / k_ for j in range(k_ + 1)}
            out7_, cut_ = [], 0
            for q in sorted(xs_):
                v_ = round(l_at_(q) + sp_at(q), 2)
                if v_ > 0:
                    v_, cut_ = 0.0, cut_ + 1
                if not out7_ or out7_[-1][1] != v_:
                    out7_.append((round(q, 5), v_))
            if cut_:
                print(f"WARNING {tr['name']}: cc7_spans_db lift cut at CC7 127 on {cut_} points", file=sys.stderr)
            lane_ = out7_
        TRIM_CC7[tr["name"]] = lane_
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
    # scherzo c16: note_move_guard (see the function)
    nmg_ = MIX.get("note_move_guard")
    if nmg_ and tr.get("notes") and not os.environ.get("ENV_NO_GUARD"):
        grid, vals = note_move_guard(tr, grid, vals, nmg_)
    # scherzo c24: note_slew (see the function)
    nsl_ = MIX.get("note_slew")
    if nsl_ and tr.get("notes") and tr["name"] not in nsl_.get("skip_tracks", []) and not os.environ.get("ENV_NO_SLEW"):
        grid, vals = note_slew(tr, grid, vals, nsl_)
    # scherzo c26: stretch_cc7 (see the function)
    grid, vals, _ = stretch_cc7(tr, grid, vals)
    # scherzo c15 (critic B #2): simplification. 38 % of the c14 points were collinear grid samples of slow ramps. With
    # mix.json "env_simplify_db" (top level; absent or 0 = off) a point stays only if the line between its kept
    # neighbours misses it by more than that many dB (Douglas-Peucker). REAPER draws the line between two points of a
    # volume envelope in its fader scale (VOLTYPE 1: ScaleToEnvelopeMode), not in dB, and in seconds, not in qn: the
    # distance is taken on ENV_SCALE values over seconds and converted back to dB, and no kept segment spans more
    # than "env_simplify_max_seg_db" (default 4) so that the result does not depend on the exact scale law
    keep = None
    tol_ = MIX.get("env_simplify_db", 0) if not os.environ.get("ENV_NO_SIMPLIFY") else 0
    if tol_ and len(grid) > 2:
        mseg_ = MIX.get("env_simplify_max_seg_db", 4.0)
        ts_ = [q2s_fast(q) for q in grid]
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
    # scherzo c28 (finale c29 note): REAPER's volume envelope ends at +24 dB and clips silently above it. The trims' excess
    # already goes into CC7 (env_max_db above, 23.0); this check fails the build if any point still passes ENV_CEIL_DB
    # (mix.json "env_ceiling_db", default 23.5), e.g. a role or hairpin gain on a track without the CC7 trim lane
    ceil_ = MIX.get("env_ceiling_db", 23.5)
    over_ = [p_ for p_ in out if p_["db"] > ceil_ + 1e-9]
    if over_:
        sys.exit(f"ENVELOPE CEILING {tr['name']}: {len(over_)} points over +{ceil_} dB (max {max(p_['db'] for p_ in over_):+.2f} "
                 f"at qn {max(over_, key=lambda p_: p_['db'])['qn'] - PRE:.2f}); move the excess into CC7 (dyn_trim_to_cc7 env_max_db)")
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


def track_width(m):
    """scherzo c10, from the finale's c09 (SHARED-TECHNIQUES item 5): mix.json "track_width" (group or track, default
    1.0): REAPER's stereo-pan width (D_WIDTH, I_PANMODE 5) after the plugin, so a section sounds as a narrower source;
    the post-fader sends feed the halls from the narrowed signal. With the seat set inside Opus, width pulls the image
    toward the centre: raise reaper_pan to keep the seat."""
    return float(m.get("track_width", 1.0))


def reaper_pan(m):
    v_ = m.get("reaper_pan")
    return None if v_ is None else float(v_)


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
# scherzo c09 (orchestrator, critic A #3): CC22 is the true-legato mono/poly switch (HO manual 2021 p.105, p.112, p.144
# and 2025 p.91: 64-127 monophonic, the default; 2021 p.99 states the opposite for the strings). The pipeline never sent
# it, so every legato instance ran in whatever state it loaded. Send CC22 = 127 (mono) in the pre-roll on every track
# that plays a "Leg" row; the lane ends on its resting value. None = off
LEGATO_MONO_CC22 = 127
# scherzo c09 (critic B #1): Opus writes runtime values into the saved state of an instance that has played (envelope
# attacks of legato sustain groups, the EWSO filter's legato_speed_active, start-mode controller values), and a
# --midi-only build keeps that saved state. Every render whose Violas instance was MIDI-only (c04, c08) came out with
# its loud legato joins about 0.1 s early and 1.5-2 dB louder; every full build was normal. With True, --midi-only
# fully rebuilds every track that plays a "Leg" row (its state reloads from jobs/NN_*.b64)
MIDI_ONLY_REBUILD_LEGATO = True


def cc7_lane(tr):
    """scherzo c25: parts.json cc7 (a step lane, 127 when empty) times the dyn_trim_to_cc7 trim lane (vol_points first)"""
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
    vpts = lua_list(vol_points(tr), ["qn", "db"])   # scherzo c25: first, so TRIM_CC7 is filled
    notes = lua_list([dict(n, qn=round(n["qn"] + PRE, 4)) for n in tr["notes"]], ["qn", "dur", "pitch", "vel"])
    ks_rows = [{"qn": round(k["qn"] + PRE, 4), "pitch": k["pitch"]} for k in tr["ks"]]
    if PRE and tr["first_ks"] is not None:   # c06: the first articulation is also selected in the pre-roll
        ks_rows.insert(0, {"qn": 0.25, "pitch": tr["first_ks"]})
    ks = lua_list(ks_rows, ["qn", "pitch"])
    ccs = []
    for num, lane in ((1, tr["cc1"]), (11, tr["cc11"]), (15, tr["cc15"]), (7, cc7_lane(tr)), (70, tr.get("cc70", [])),
                     (36, tr.get("cc36", []))):   # mvt1 c14 (A #2): round-robin resets inside the music
        ccs += [{"qn": round(q + PRE, 4), "cc": num, "v": v} for q, v in lane]
        if PRE and lane:   # c06: each lane's first value is sent in the pre-roll too
            ccs.append({"qn": 0.25, "cc": num, "v": lane[0][1]})
    if PRE and LEGATO_MONO_CC22 is not None and any("Leg" in a_ for a_ in (tr.get("art_counts") or {})):
        ccs.append({"qn": 0.25, "cc": 22, "v": LEGATO_MONO_CC22})   # scherzo c09: legato mono pinned
    if tr.get("rr_reset") and RR_RESET_CC is not None:   # scherzo c07 (critic C #4): resets inside the music
        ccs += [{"qn": round(q + PRE, 4), "cc": RR_RESET_CC, "v": v} for q, v in tr["rr_reset"]]
    if PRE and tr["family"] not in RR_RESET_SKIP_FAMILIES:
        # c24 (A #3): reset Opus's round-robin state (CC36, any value) at the start of every render, and on the strings
        # turn the Repetition script off (CC69 0-63 = OFF, HO manual CC table), so renders are reproducible
        ccs.append({"qn": RR_RESET_QN, "cc": 36, "v": 127})
        if RR_RESET_CC is not None and RR_RESET_CC != 36:   # mvt1 c43: the reset Opus itself listens to
            ccs.append({"qn": RR_RESET_QN, "cc": RR_RESET_CC, "v": 127})
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
reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", {track_width(mix_for(tr['name']))})   -- scherzo c10 (finale c09): mix.json track_width
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
        rows.append(f'{{n={json.dumps(tr["name"])}, pan={rp_ if rp_ is not None else 0}, w={track_width(m)}, vol={10 ** ((m["gain_db"] + MIX.get("global_gain_db", 0.0)) / 20):.6f}, env={lua_list(vol_points(tr), ["qn", "db"])}, eq={eq_lua(m)}, meq={mute_lua(m)}, ss={side_lua(m)}{ext_}}}')
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
# scherzo c12 (ONE_TIME item 8; mvt1 c52): STALE_GUARD. A --midi-only build decodes the saved project
# (tools/state_guard.py) and fully rebuilds every track of the pass whose saved Opus state is not the written one
# (legato AHDSR attacks saved at 20 ms after playback), also when the track is not listed and plays no "Leg" row.
# tools/render_cycle.py refuses to render a project that still holds a stale track (--force-stale overrides).
STALE_GUARD = True
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
for i, tr in enumerate(d["tracks"]):
    if ONLY and tr["name"] not in ONLY and tr["name"] not in STALE:
        continue
    if not in_pass(tr):
        if ONLY:
            print(f"{tr['name']}: skipped (pass {tr.get('pass', 1)}; {'without' if PASS2 else 'with'} --pass2)", flush=True)
        continue
    if MIDI_ONLY:
        bf = b64_path(i, tr)
        leg_ = MIDI_ONLY_REBUILD_LEGATO and any("Leg" in a_ for a_ in (tr.get("art_counts") or {}))
        if tr["name"] in STALE:
            print(f"{tr['name']}: saved Opus state is stale (state_guard: AHDSR attacks differ), full rebuild", flush=True)
            res = track_job(i, tr)
        elif os.path.exists(bf) and open(bf).read() == state_for(tr) and not leg_:
            res = midi_job(i, tr)
        elif leg_:
            print(f"{tr['name']}: plays a legato row, full rebuild (MIDI_ONLY_REBUILD_LEGATO)", flush=True)
            res = track_job(i, tr)
        else:
            print(f"{tr['name']}: Opus state changed, full rebuild", flush=True)
            res = track_job(i, tr)
    else:
        res = track_job(i, tr)
    check_sends(tr, res)   # mvt1 c50: stops on a failed send (no-op without sends)
    print(json.dumps(res), flush=True)

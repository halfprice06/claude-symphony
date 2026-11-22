"""Offline tests of the mvt1 c50 template-mix tools (tools/TEMPLATE-TOOLS.md). Nothing is sent to REAPER.

Usage: python3 tools/test_template_tools.py [--work DIR] [--mix build/mix_template50.json] [--skip-render]
  1. chunks: template_mix.check() (every FX state of the template decoded and compared with ho-mix-fx.json).
  2. build: build_reaper.py run offline on parts.json + the template mix (main pass, --pass2, --mix-only, --midi-only,
     and the "duc" profile) with a fake bridge that answers the returns job the way REAPER would (the states it was
     given); then every Opus state, return spec, send, family EQ and pan line is checked against the mix, the Lua jobs
     are checked for balanced blocks, and a corrupted read-back must stop the build.
  3. stems: tools/return_stems.py rename / merge_pass2 / fit on synthetic stems.
  4. render (unless --skip-render): render_cycle.py end to end on a scratch copy of the work folder with synthetic stems
     and a fake REAPER (main render, then --pass2): stem names and order, return renumbering, test returns, the master as
     the sum of dry and return stems, measure.py's return section, deliver_master.py's master EQ.
Prints PASS / FAIL per check; exit status 1 on any failure.
"""
import base64, glob, json, math, os, re, shutil, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
args = sys.argv[1:]
WORK = os.path.abspath(args[args.index("--work") + 1]) if "--work" in args else tempfile.mkdtemp(prefix="template-tests-")
MIXT = os.path.abspath(args[args.index("--mix") + 1]) if "--mix" in args else os.path.join(ROOT, "build", "mix_template50.json")
PY = os.path.expanduser("~/.venvs/claude-composes-reaper/bin/python")
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
import template_mix as T
import opus_state

FAILS = []


def ok(cond, what):
    print(("PASS " if cond else "FAIL ") + what, flush=True)
    if not cond:
        FAILS.append(what)
    return cond


# ------------------------------------------------------------------------------------------------ 1. chunks
print("== 1. chunks")
ok(T.check() == 0, "every template FX state decodes and matches ho-mix-fx.json (ReaEQ bands, Spaces II JSON)")

# ------------------------------------------------------------------------------------------------ 2. build
print("== 2. build (offline)")
RUNNER = r"""
import json, re, runpy, subprocess, sys, os
_real = subprocess.run
MODE = os.environ.get("FAKE_REAPER", "echo")
class _Done:
    returncode = 0
    stderr = ""
    def __init__(self, out): self.stdout = out
def _fake(cmd, *a, **k):
    if isinstance(cmd, (list, tuple)) and len(cmd) > 1 and str(cmd[1]).endswith("rpr.py"):
        path = cmd[3]
        if os.path.basename(path) == "90_returns.lua":
            lua = open(path).read()
            res = []
            for m in re.finditer(r'\{name="([^"]+)", fader_db=([^,]+), pan=([^,]+), bypass=(\w+), fx=\{(.*?)\}, fxchain=', lua, re.S):
                fx = [{"name": a, "chunk": c, "enabled": m.group(4) != "true"} for a, c in re.findall(r'\{add="([^"]+)", chunk="([^"]+)"\}', m.group(5))]
                if MODE == "corrupt" and fx:
                    import base64, struct
                    b = bytearray(base64.b64decode(fx[0]["chunk"]))
                    b[8 + 8 + 8] ^= 0x40   # a band's frequency
                    fx[0]["chunk"] = base64.b64encode(bytes(b)).decode()
                res.append({"name": m.group(1), "created": True, "fx": fx, "log": []})
            return _Done(json.dumps({"returns": res}))
        return _Done("{}")
    return _real(cmd, *a, **k)
subprocess.run = _fake
sys.argv = json.loads(sys.argv[1])
runpy.run_path(sys.argv[0], run_name="__main__")
"""


def build(mix, tag, extra, env_mode="echo", jobs=None):
    d = os.path.join(WORK, "build-" + tag)
    os.makedirs(d, exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "build", "parts.json"), os.path.join(d, "parts.json"))
    json.dump(mix, open(os.path.join(d, "mix.json"), "w"), indent=1)
    jobs = jobs or os.path.join(d, "jobs")
    os.makedirs(jobs, exist_ok=True)
    argv = [os.path.join(TOOLS, "build_reaper.py"), os.path.join(d, "parts.json"), jobs] + extra
    p = subprocess.run([sys.executable, "-c", RUNNER, json.dumps(argv)], capture_output=True, text=True,
                       env=dict(os.environ, FAKE_REAPER=env_mode))
    return p, jobs


def lua_balanced(src):
    """a rough Lua block check: strings and comments removed, then function/if/for/while/do/repeat vs end/until,
    and brackets"""
    s = re.sub(r"--\[(=*)\[.*?\]\1\]", "", src, flags=re.S)
    s = re.sub(r"\[(=*)\[.*?\]\1\]", '""', s, flags=re.S)
    s = re.sub(r'"(?:[^"\\\n]|\\.)*"', '""', s)
    s = re.sub(r"'(?:[^'\\\n]|\\.)*'", "''", s)
    s = re.sub(r"--[^\n]*", "", s)
    toks = re.findall(r"\b(function|if|for|while|do|repeat|end|until|then)\b|([(){}\[\]])", s)
    stack, pend = [], 0
    pairs = {")": "(", "}": "{", "]": "["}
    for w, br in toks:
        if br:
            if br in "({[":
                stack.append(br)
            elif not stack or stack.pop() != pairs[br]:
                return False
        elif w in ("function", "if", "repeat"):
            stack.append(w)
        elif w in ("for", "while"):
            stack.append(w)
            pend += 1
        elif w == "do":
            if pend:
                pend -= 1
            else:
                stack.append("do")
        elif w == "end":
            if not stack or stack.pop() not in ("function", "if", "for", "while", "do"):
                return False
        elif w == "until":
            if not stack or stack.pop() != "repeat":
                return False
    return not stack


mix = json.load(open(MIXT))
parts = json.load(open(os.path.join(ROOT, "build", "parts.json")))
P = {t["name"]: t for t in parts["tracks"]}


def merged(name):
    t = dict(mix["tracks"][name])
    for k, v in mix["groups"][t["group"]].items():
        t.setdefault(k, v)
    return t


p, jobs = build(mix, "main", [])
ok(p.returncode == 0, f"template build, main pass, exits 0 ({p.stderr.strip()[-300:]})")
main_tracks = [t for t in parts["tracks"] if t.get("pass", 1) != 2]
rl = open(os.path.join(jobs, "90_returns.lua")).read() if os.path.exists(os.path.join(jobs, "90_returns.lua")) else ""
names = re.findall(r'\{name="([^"]+)", fader_db', rl)
ok(names == ["R Strings", "R Brass", "R Winds", "R Perc"], f"main returns job builds R Strings, R Brass, R Winds, R Perc ({names})")
ok(lua_balanced(rl), "returns job Lua blocks balanced")
mixdir = os.path.join(WORK, "build-main")
for nm in names:
    spec = T.resolve_return(mix, mixdir, nm, nm)
    chunks = re.search(r'\{name="%s".*?fx=\{(.*?)\}, fxchain=' % re.escape(nm), rl, re.S).group(1)
    got = re.findall(r'chunk="([^"]+)"', chunks)
    ok([base64.b64decode(g) for g in got] == [f["data"] for f in spec["fx"]], f"{nm}: the job loads the chunk states verbatim")
    js = T.spaces_json(spec["fx"][1]["data"])
    ref = json.load(open(os.path.join(os.path.dirname(T.CHUNK_DIR), "ho-mix-fx.json")))
    want = {"R Strings": "STRING VERB", "R Brass": "BRASS VERB", "R Winds": "WW VERB", "R Perc": "PERC VERB"}[nm]
    eqd = T.reaeq_decode(spec["fx"][0]["data"])["bands"]
    ok(js == ref[want]["fx"][1]["decoded_state"]
       and all(abs(a["freq_hz"] - b["freq_hz"]) < 0.01 and abs(a["gain_db"] - b["gain_db"]) < 0.051 and a["type"] == b["type"]
               for a, b in zip(eqd, ref[want]["fx"][0]["decoded_bands"])),
       f"{nm}: ReaEQ and Spaces II states = the template's {want} ({js['selectedPreset']['presetName']}, "
       f"pre-delay {js['delay'] * 1000:.1f} ms, endPos {js['irSetup']['endPos']}, EQ "
       + ", ".join(f"{b['band']} {b['freq_hz']:g}" + (f" {b['gain_db']:+.1f}" if b['band'] == 'bell' else '') for b in eqd) + ")")
    fx_line = re.search(r'\{name="%s", fader_db=([^,]+)' % re.escape(nm), rl).group(1)
    ok(abs(float(fx_line) - mix["returns"][nm]["fader_db"]) < 1e-9, f"{nm}: fader {fx_line} dB")
    ok(T.fxchain_text(spec["fx"]).count("<VST") == 2 and T.parse_blocks(T.fxchain_text(spec["fx"]))[1]["name"] == T.SPACES_ADD,
       f"{nm}: the fxchain alternative parses back to the same two FX")
    fb = T.parse_blocks(T.fxchain_text(spec["fx"]))
    ok([T.vst_runs(b["lines"])[1] for b in fb] == [f["data"] for f in spec["fx"]], f"{nm}: fxchain text round-trips the states")

bad_state, bad_send, bad_feq, bad_pan, nchk = [], [], [], [], 0
FAM = {"string": "strings", "horn": "brass", "trumpet": "brass", "lowbrass": "brass", "wind": "woodwinds", "harp": "harp", "timp": "timpani"}
for i, tr in enumerate(parts["tracks"]):
    if tr.get("pass", 1) == 2:
        continue
    m = merged(tr["name"])
    st = open(os.path.join(jobs, f"{i:02d}_{tr['stem'].replace(' ', '_')}.b64")).read()
    inst = opus_state.split(st)[1]["zones"][0]["instrument"]
    ch = inst["mixer"]["channels"]
    subs = {c["label"]: c for c in ch if c["channelId"].startswith("sub:")}
    own = mix["tracks"][tr["name"]]
    mics = own["mics"] if ("mics" in own and "mic_db" not in own) else (
        {k: 10 ** (v / 20) for k, v in m["mic_db"].items()} if m.get("mic_db") is not None else m.get("mics"))
    for lab, c in subs.items():
        if mics is not None:
            if c["loaded"] != (lab in mics) or (lab in mics and abs(c["volume"] - mics[lab]) > 1e-9):
                bad_state.append(f"{tr['name']} {lab} loaded {c['loaded']} vol {c['volume']}")
        rule = (m.get("pan_by_mic") or {}).get(lab, "seat")
        if rule == "full" and (c["pan"], c["panLeft"], c["panRight"]) != (0.0, -1.0, 1.0):
            bad_state.append(f"{tr['name']} {lab} pan {c['pan']} {c['panLeft']} {c['panRight']}")
        if rule == "seat":
            wd = max(m["width"], (m.get("width_by_mic") or {}).get(lab, 0.0))
            if (c["pan"], c["panLeft"], c["panRight"]) != (0.0, max(-1.0, m["seat"] - wd), min(1.0, m["seat"] + wd)):
                bad_state.append(f"{tr['name']} {lab} seat pan {c['panLeft']} {c['panRight']}")
        for ins in c["inserts"]:
            if ins["class"] == "SendProcessor" and ins.get("output") == "fx:0" and ins["level"] != 0.0:
                bad_state.append(f"{tr['name']} {lab} reverb send {ins['level']}")
    fx0 = next(c for c in ch if c["channelId"] == "fx:0")
    if fx0["volume"] != 0.0 or any(x["class"] == "ConvolutionReverb" for x in fx0["inserts"]):
        bad_state.append(f"{tr['name']} fx:0 volume {fx0['volume']} inserts {[x['class'] for x in fx0['inserts']]}")
    lua = open(os.path.join(jobs, f"{i:02d}_{tr['name'].replace(' ', '_')}.lua")).read()
    if not lua_balanced(lua):
        bad_state.append(f"{tr['name']}: Lua blocks unbalanced")
    rp = m.get("reaper_pan")
    if (rp is None and 'reaper.SetMediaTrackInfo_Value(tr, "D_PAN", 0)     -- c05' not in lua) or \
            (rp is not None and f'reaper.SetMediaTrackInfo_Value(tr, "D_PAN", {float(rp)!r})' not in lua):
        bad_pan.append(tr["name"])
    sends = re.search(r"set_sends\(tr, \{(.*)\}, eq\)", lua)
    want = [(k, v) for k, v in mix["send_profiles"]["ew"][m["group"]].items() if mix["returns"][k].get("enabled", True)]
    got = re.findall(r'\{dest="([^"]+)", db=([-\d.e]+)', sends.group(1)) if sends else []
    if [(a, float(b)) for a, b in got] != [(k, float(v)) for k, v in want]:
        bad_send.append(f"{tr['name']}: {got} != {want}")
    fam = FAM.get(m["group"])
    feq = re.search(r"set_family_eq\(tr, \{name=\"([^\"]+)\", bands=\{(.*?)\}\}, eq\)", lua)
    if fam is None:
        if feq:
            bad_feq.append(f"{tr['name']}: family EQ {feq.group(1)} where none is wanted")
    else:
        bands = re.findall(r'\{band="(\w+)", type=(\d+), hz=([\d.]+)(?:, db=([-\d.]+))?(?:, bw=([\d.]+))?\}', feq.group(2)) if feq else []
        wb = mix["family_eqs"][fam]
        if not feq or feq.group(1) != fam or len(bands) != len(wb) or any(
                b[0] != w["band"] or int(b[1]) != T.BAND_TYPES[w["band"]] or float(b[2]) != w["hz"]
                or (b[3] and float(b[3]) != w.get("db")) or (b[4] and float(b[4]) != w.get("bw_oct")) for b, w in zip(bands, wb)):
            bad_feq.append(f"{tr['name']}: {feq.group(0)[:120] if feq else None}")
        if feq and lua.index("set_family_eq(tr,") < lua.index("set_side_shelf(tr,"):
            bad_feq.append(f"{tr['name']}: family EQ before the side shelf")
    nchk += 1
ok(not bad_state, f"{nchk} main Opus states: mic_db levels and loading, pan_by_mic rules, Opus reverb off (fx:0 volume 0, no "
                  f"ConvolutionReverb, sends 0); Lua blocks balanced {bad_state[:4]}")
ok(not bad_send, f"sends: each main track sends to its family returns at the profile level, R Glue skipped {bad_send[:3]}")
ok(not bad_feq, f"family EQ: the right band list per family, after the per-track and side-shelf EQs {bad_feq[:3]}")
ok(not bad_pan, f"REAPER track pan line per reaper_pan (centre line unchanged without it) {bad_pan[:3]}")

# --midi-only on the same jobs: unchanged states -> MIDI jobs with the family EQ and sends again
p, _ = build(mix, "main", ["--midi-only"], jobs=jobs)
mj = sorted(glob.glob(os.path.join(jobs, "*_midi.lua")))
ok(p.returncode == 0 and len(mj) == len(main_tracks) and all("set_sends(tr," in open(f).read() for f in mj),
   f"--midi-only reuses the states and re-adds sends in every MIDI job ({len(mj)} jobs)")
ok("90_returns.lua" in os.listdir(jobs), "--midi-only runs the returns job first")
p, _ = build(mix, "main", ["--mix-only"], jobs=jobs)
mxl = open(os.path.join(jobs, "95_mix.lua")).read()
ok(p.returncode == 0 and "if r.feq then set_family_eq(tr, r.feq, eq) end" in mxl and "if r.snd then set_sends(tr, r.snd, eq) end" in mxl
   and "pan=-0.1," in mxl and lua_balanced(mxl), "--mix-only sets reaper_pan, family EQ and sends")

# pass 2: test tracks send to "<return> test"
p, jobs2 = build(mix, "p2", ["--pass2"])
rl2 = open(os.path.join(jobs2, "90_returns.lua")).read()
n2 = re.findall(r'\{name="([^"]+)", fader_db', rl2)
ok(p.returncode == 0 and n2 == ["R Strings", "R Strings test", "R Brass", "R Brass test", "R Winds"],
   f"pass-2 returns: sources plus test copies for the test tracks ({n2})")
bad = []
for i, tr in enumerate(parts["tracks"]):
    if tr.get("pass", 1) != 2:
        continue
    lua = open(os.path.join(jobs2, f"{i:02d}_{tr['name'].replace(' ', '_')}.lua")).read()
    dests = re.findall(r'\{dest="([^"]+)"', lua)
    if tr.get("test") and not all(x.endswith(" test") for x in dests) or not tr.get("test") and any(x.endswith(" test") for x in dests):
        bad.append(f"{tr['name']} {dests}")
ok(not bad, f"pass-2 test tracks send only to test returns, the others only to the real ones {bad[:3]}")

# the duc profile: R Duc with its ReaEQ and Spaces II set, celli / basses send envelopes
mduc = json.loads(json.dumps(mix))
mduc["send_profile"] = "duc"
p, jd = build(mduc, "duc", [])
rld = open(os.path.join(jd, "90_returns.lua")).read()
ok(p.returncode == 0 and re.findall(r'\{name="([^"]+)", fader_db', rld) == ["R Duc"], "profile 'duc': only R Duc is built")
sd = T.resolve_return(mduc, os.path.join(WORK, "build-duc"), "R Duc", "R Duc")
eqb = T.reaeq_decode(sd["fx"][0]["data"])["bands"]
jsd = T.spaces_json(sd["fx"][1]["data"])
ok([(b["band"], b["freq_hz"], b["enabled"]) for b in eqb] == [("highpass", 184.0, True), ("lowpass", 3000.0, True)],
   "R Duc ReaEQ: high pass 184 Hz, low pass 3 kHz")
ok(jsd["impulseA"].endswith("Hollywood Scoring Stage L Rear") and jsd["impulseB"].endswith("Hollywood Scoring Stage R Rear")
   and abs(jsd["delay"] - 0.012) < 1e-12 and jsd["trueStereo"] is True and jsd["irSetup"]["endPos"] == 1.0
   and T.spaces_split(sd["fx"][1]["data"])[2] == T.spaces_split(T.vst_runs(T.find_fx(T._blocks(os.path.join(T.CHUNK_DIR, "PERC_VERB.txt")), "Spaces")["lines"])[1])[2],
   f"R Duc Spaces II: {jsd['selectedPreset']['presetName']}, rear true-stereo impulses, 12 ms, editor/JUCE bytes kept")
vc = [i for i, t in enumerate(parts["tracks"]) if t["name"] == "Violoncellos"][0]
lv = open(os.path.join(jd, f"{vc:02d}_Violoncellos.lua")).read()
envs = re.findall(r'\{qn=([\d.]+), db=([-\d.]+)\}', re.search(r'set_sends\(tr, (.*), eq\)', lv).group(1))
lvl = sorted({float(b) for _, b in envs})
ok(lvl == [-7.0, -1.6], f"Violoncellos under 'duc': send envelope steps between -1.6 (longs) and -7.0 dB (short rows) ({lvl}, {len(envs)} points)")
# the envelope steps at the onset of the first note of each row
tr = P["Violoncellos"]
ks = sorted((k["qn"], k["art"]) for k in tr["ks"])
row_at = lambda q: ([a for kq, a in ks if kq <= q + 1e-6] or [tr["first_art"]])[-1]
shorts = {"Pizzicato RRx4", "Stac RRx9", "Stac On Bow RRx9"}
want_pts = []
cur = None
for n in sorted(tr["notes"], key=lambda n: n["qn"]):
    v = -7.0 if row_at(n["qn"]) in shorts else -1.6
    if v != cur:
        want_pts.append((round(n["qn"] + parts["preroll_qn"], 4), v))
        cur = v
got_pts = [(float(a), float(b)) for a, b in envs]
ok(got_pts[1:] == want_pts or got_pts == want_pts, "send envelope points = the first note of each row run (pre-roll point first)")

# a wrong read-back stops the build
p, _ = build(mix, "corrupt", [], env_mode="corrupt")
ok(p.returncode != 0 and "return tracks differ from mix.json" in p.stderr, "a REAPER read-back that differs from the chunk stops the build")
# the "fxchain" method writes the same chunks into a track chunk
mfx = json.loads(json.dumps(mix))
mfx["return_load"] = "fxchain"
p, jf = build(mfx, "fxchain", ["--mix-only"])
rlf = open(os.path.join(jf, "90_returns.lua")).read()
ok(p.returncode == 0 and 'rebuild_return(s, "fxchain")' in rlf and rlf.count("<FXCHAIN") == 4, "return_load fxchain: four FXCHAIN texts in the job")

# ------------------------------------------------------------------------------------------------ 3. return stems
print("== 3. return stems (synthetic)")
import numpy as np
import soundfile as sf
import return_stems as RS
sr, n = 48000, 48000 * 3
rng = np.random.default_rng(7)
C = os.path.join(WORK, "stems", "c90")
for sub in ("render", "render_pass2"):
    os.makedirs(os.path.join(C, sub), exist_ok=True)
rets = RS.returns_of(MIXT)
ok(list(rets.items())[:4] == [("R Strings", 91), ("R Brass", 92), ("R Winds", 93), ("R Perc", 94)], f"return stem numbers {rets}")
dry = {nm: rng.standard_normal((n, 2)) * 0.05 for nm in ("Violins I", "Violas", "Horn 1")}
for k, nm in enumerate(dry):
    sf.write(os.path.join(C, "render", f"{k + 1:02d}_{nm}.wav"), dry[nm].astype("float32"), sr, subtype="FLOAT")
g = {"Violins I": 10 ** (-5.56 / 20), "Violas": 10 ** (-5.56 / 20) * 10 ** (-2 / 20), "Horn 1": 10 ** (-8.77 / 20)}
rs_ = dry["Violins I"] * g["Violins I"] + dry["Violas"] * g["Violas"]
rb_ = dry["Horn 1"] * g["Horn 1"]
sf.write(os.path.join(C, "render", "04_R Strings.wav"), (rs_ * 10 ** (1.03 / 20)).astype("float32"), sr, subtype="FLOAT")
sf.write(os.path.join(C, "render", "05_R Brass.wav"), (rb_ * 10 ** (1.03 / 20)).astype("float32"), sr, subtype="FLOAT")
sf.write(os.path.join(C, "render", "06_R Strings test.wav"), np.zeros((n, 2), "float32"), sr, subtype="FLOAT")
RS.rename(os.path.join(C, "render"), rets, os.path.join(C, "test_stems"))
lst = sorted(os.listdir(os.path.join(C, "render")))
ok(lst == ["01_Violins I.wav", "02_Violas.wav", "03_Horn 1.wav", "91_R Strings.wav", "92_R Brass.wav"]
   and os.listdir(os.path.join(C, "test_stems")) == ["91_R Strings test.wav"], f"rename: {lst}, test copy to test_stems")
pfake = os.path.join(WORK, "stems", "parts.json")
json.dump({"tracks": [{"name": nm} for nm in dry]}, open(pfake, "w"))
fr = RS.fit(os.path.join(C, "render"), pfake, MIXT)
ok(abs(fr["R Strings"]["send_db"]["Violins I"] + 5.56) < 0.01 and abs(fr["R Strings"]["send_db"]["Violas"] + 7.56) < 0.01
   and abs(fr["R Brass"]["send_db"]["Horn 1"] + 8.77) < 0.01 and "Horn 1" not in fr["R Strings"]["send_db"],
   f"fit recovers the send levels from bypassed returns ({fr['R Strings']['send_db']}, {fr['R Brass']['send_db']})")
p2 = rng.standard_normal((n - 100, 2)) * 0.01
sf.write(os.path.join(C, "render_pass2", "02_R Strings.wav"), p2.astype("float32"), sr, subtype="FLOAT")
sf.write(os.path.join(C, "render_pass2", "03_R Brass test.wav"), p2.astype("float32"), sr, subtype="FLOAT")
main_rs = sf.read(os.path.join(C, "render", "91_R Strings.wav"), dtype="float64")[0]
RS.merge_pass2(C, os.path.join(C, "render_pass2"), rets, n)
RS.merge_pass2(C, os.path.join(C, "render_pass2"), rets, n)   # twice: the main copy keeps it idempotent
got = sf.read(os.path.join(C, "render", "91_R Strings.wav"), dtype="float64")[0]
want = main_rs + np.pad(p2, ((0, 100), (0, 0)))
ok(np.abs(got - want).max() < 1e-6 and os.path.exists(os.path.join(C, "render_pass2", "returns_main", "91_R Strings.wav"))
   and os.path.exists(os.path.join(C, "test_stems", "92_R Brass test.wav"))
   and sf.read(os.path.join(C, "render", "92_R Brass.wav"))[0].shape == (n, 2),
   "merge_pass2: return = main + pass 2 (padded to the main length; idempotent), test return to test_stems, others untouched")

# ------------------------------------------------------------------------------------------------ 4. render_cycle
if "--skip-render" not in args:
    print("== 4. render_cycle.py end to end (synthetic stems, fake REAPER)")
    R = os.path.join(WORK, "root")
    shutil.rmtree(R, ignore_errors=True)
    os.makedirs(os.path.join(R, "build"))
    shutil.copytree(TOOLS, os.path.join(R, "tools"), ignore=shutil.ignore_patterns("__pycache__"))
    pj = json.load(open(os.path.join(ROOT, "build", "parts.json")))
    # a short piece: the real tracks, a 40 s tempo map
    pj["end_qn"], pj["score_end"], pj["ride_trims"] = 30.0, 28.0, []
    pj["tempo"], pj["timesig"] = [[0.0, 90.0]], [[0.0, 4, 4]]
    for t in pj["tracks"]:
        t["notes"] = [nt for nt in t["notes"] if nt["qn"] < 26][:40]
        t["dyn_curve"] = [x for x in t.get("dyn_curve", []) if x[0] < 26]
    json.dump(pj, open(os.path.join(R, "build", "parts.json"), "w"))
    shutil.copy2(MIXT, os.path.join(R, "build", "mix.json"))
    open(os.path.join(R, "mvt1-fake.rpp"), "w").write("RENDER_1X 1\n")
    open(os.path.join(R, "mvt1-fake-pass2.rpp"), "w").write("RENDER_1X 1\n")
    N = 90
    Cc = os.path.join(R, "cycles", f"c{N:02d}")
    os.makedirs(os.path.join(Cc, "render"))
    pre = pj["preroll_qn"] * 60 / pj["preroll_bpm"]
    L = int((pre + 28 * 60 / 90 + 8) * sr)
    STAGE1, STAGE2 = os.path.join(WORK, "stage_main"), os.path.join(WORK, "stage_p2")
    for d_ in (STAGE1, STAGE2):
        shutil.rmtree(d_, ignore_errors=True)
        os.makedirs(d_)
    main = [t["name"] for t in pj["tracks"] if t.get("pass", 1) != 2]
    p2t = [t["name"] for t in pj["tracks"] if t.get("pass", 1) == 2]
    tone = lambda f, a: (a * np.sin(2 * np.pi * f * np.arange(L) / sr))[:, None] * np.array([[1.0, 0.8]])
    tot = np.zeros((L, 2))
    for k, nm in enumerate(main):
        x = tone(110 + 13 * k, 0.01) * (np.arange(L)[:, None] >= int(pre * sr))
        sf.write(os.path.join(STAGE1, f"{k + 1:02d}_{nm}.wav"), x.astype("float32"), sr, subtype="FLOAT")
        tot += x
    for k, nm in enumerate(["R Strings", "R Brass", "R Winds", "R Perc"]):   # REAPER numbers the returns after the tracks
        x = tone(1500 + 100 * k, 0.005) * (np.arange(L)[:, None] >= int(pre * sr))
        sf.write(os.path.join(STAGE1, f"{len(main) + k + 1:02d}_{nm}.wav"), x.astype("float32"), sr, subtype="FLOAT")
        tot += x
    sf.write(os.path.join(STAGE1, "00_Master.wav"), tot.astype("float32"), sr, subtype="FLOAT")
    HARNESS = r"""
import json, os, runpy, subprocess, sys, time
_real = subprocess.run
PRE = float(os.environ["FAKE_PRE"])
import re, shutil
class _Done:
    def __init__(self, out, rc=0): self.stdout, self.stderr, self.returncode = out, "", rc
def _fake(cmd, *a, **k):
    if isinstance(cmd, (list, tuple)) and cmd and len(cmd) > 1 and str(cmd[1]).endswith("rpr.py"):
        lua = open(cmd[3]).read()
        if "GetAudioDeviceInfo" in lua:
            return _Done(json.dumps({"IDENT_IN": "", "SRATE": "48000", "BSIZE": "512", "running": True}))
        if "Main_OnCommand(42230" in lua:   # the render: REAPER writes the stems into RENDER_FILE
            dst = re.search(r'local dir = "([^"]+)"', lua).group(1)
            os.makedirs(dst, exist_ok=True)
            for f in os.listdir(os.environ["FAKE_STAGE"]):
                shutil.copy2(os.path.join(os.environ["FAKE_STAGE"], f), dst)
        return _Done(json.dumps({"pre_sec": PRE}))
    if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "top":
        return _Done("PID COMMAND MEM CMPRS\n1 REAPER 40G 0B\n")
    if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "pgrep":
        return _Done("1\n")
    if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "ps":
        return _Done("1000\n")
    return _real(cmd, *a, **k)
subprocess.run = _fake
time.sleep = lambda s: None
sys.argv = json.loads(sys.argv[1])
runpy.run_path(sys.argv[0], run_name="__main__")
"""
    env = dict(os.environ, FAKE_PRE=repr(pre), FAKE_STAGE=STAGE1)
    pr = subprocess.run([PY, "-c", HARNESS, json.dumps([os.path.join(R, "tools", "render_cycle.py"), str(N)])],
                        capture_output=True, text=True, env=env)
    open(os.path.join(WORK, "render_main.log"), "w").write(pr.stdout + "\n--- stderr\n" + pr.stderr)
    lst = sorted(os.listdir(os.path.join(Cc, "render")))
    want_l = ["00_Master.wav"] + [f"{k + 1:02d}_{nm}.wav" for k, nm in enumerate(main)] + \
             ["91_R Strings.wav", "92_R Brass.wav", "93_R Winds.wav", "94_R Perc.wav"]
    ok(pr.returncode == 0, f"render_cycle.py (main) exits 0 ({pr.stderr.strip()[-300:]})")
    ok(lst == want_l, f"main render: instrument stems keep their names and numbers, returns renumbered 91-94 last ({lst[-5:]})")
    mt = json.load(open(os.path.join(Cc, "metrics", "metrics.json")))
    ok(set(mt.get("returns", {})) == {"R Strings", "R Brass", "R Winds", "R Perc"} and not set(mt["stems"]) & set(mt.get("returns", {}))
       and "returns_re_dry_db" in mt, f"measure.py: return stems in their own section ({mt.get('returns_re_dry_db')} dB re dry)")
    mdm = open(os.path.join(Cc, "metrics", "metrics.md")).read()
    ok("## Return stems (c50)" in mdm and "master EQ (mix.json master_eq)" in mdm,
       "metrics.md has the return section and the delivery used the master EQ")
    # pass 2: two non-test stems, one test stem, the pass-2 returns
    R2 = STAGE2
    p2stems = {}
    for k, nm in enumerate(p2t):
        x = tone(220 + 7 * k, 0.004) * (np.arange(L)[:, None] >= int(pre * sr))
        sf.write(os.path.join(R2, f"{k + 5:02d}_{nm}.wav"), x.astype("float32"), sr, subtype="FLOAT")
        p2stems[nm] = x
    for k, nm in enumerate(["R Strings", "R Strings test", "R Brass", "R Brass test", "R Winds"]):
        x = tone(2500 + 50 * k, 0.002) * (np.arange(L)[:, None] >= int(pre * sr))
        sf.write(os.path.join(R2, f"{k + 1:02d}_{nm}.wav"), x.astype("float32"), sr, subtype="FLOAT")
        p2stems[nm] = x
    sf.write(os.path.join(R2, "00_Master.wav"), np.zeros((L, 2), "float32"), sr, subtype="FLOAT")
    before = {f: sf.read(os.path.join(Cc, "render", f), dtype="float64")[0] for f in os.listdir(os.path.join(Cc, "render"))}
    pr = subprocess.run([PY, "-c", HARNESS, json.dumps([os.path.join(R, "tools", "render_cycle.py"), str(N), "--pass2"])],
                        capture_output=True, text=True, env=dict(env, FAKE_STAGE=STAGE2))
    open(os.path.join(WORK, "render_pass2.log"), "w").write(pr.stdout + "\n--- stderr\n" + pr.stderr)
    ok(pr.returncode == 0, f"render_cycle.py --pass2 exits 0 ({pr.stderr.strip()[-300:]})")
    tests = {t["name"] for t in pj["tracks"] if t.get("test")}
    lst2 = sorted(os.listdir(os.path.join(Cc, "render")))
    names_p2 = [t["name"] for t in pj["tracks"]]
    want2 = sorted(set(want_l) | {f"{names_p2.index(nm) + 1:02d}_{nm}.wav" for nm in p2t if nm not in tests})
    ok(lst2 == want2, f"pass 2: pass-2 stems at their parts.json numbers, returns still 91-94 last ({lst2[-6:]})")
    cut = int(round(pre * sr))
    m91 = sf.read(os.path.join(Cc, "render", "91_R Strings.wav"), dtype="float64")[0]
    ok(np.abs(m91 - (before["91_R Strings.wav"] + p2stems["R Strings"][cut:])).max() < 1e-6,
       "pass 2: R Strings = main return + pass-2 return (pre-roll cut)")
    ok(np.abs(sf.read(os.path.join(Cc, "render", "93_R Winds.wav"), dtype="float64")[0] - (before["93_R Winds.wav"] + p2stems["R Winds"][cut:])).max() < 1e-6
       and np.abs(sf.read(os.path.join(Cc, "render", "94_R Perc.wav"), dtype="float64")[0] - before["94_R Perc.wav"]).max() == 0,
       "pass 2: R Winds summed, R Perc (no pass-2 sender) untouched")
    ts = sorted(os.listdir(os.path.join(Cc, "test_stems")))
    ok("91_R Strings test.wav" in ts and "92_R Brass test.wav" in ts, f"pass 2: test returns in test_stems ({[f for f in ts if 'R ' in f]})")
    master = sf.read(os.path.join(Cc, "render", "00_Master.wav"), dtype="float64")[0]
    ssum = sum(sf.read(os.path.join(Cc, "render", f), dtype="float64")[0] for f in lst2 if f != "00_Master.wav")
    ok(np.abs(master - ssum).max() < 1e-6, "pass 2: 00_Master.wav = float sum of every dry and return stem in render/")
    ok(not any(np.abs(master - (ssum + p2stems[nm][cut:])).max() < 1e-6 for nm in ("R Strings test", "R Brass test")),
       "pass 2: test returns are not in the master")
    ok("master EQ (mix.json master_eq)" in pr.stdout + open(os.path.join(Cc, "metrics", "metrics.md")).read(), "pass 2: delivery with the master EQ")

    # deliver_master's master EQ against the band list: white noise through the same ffmpeg chain
    import importlib.util
    noise = os.path.join(WORK, "noise.wav")
    sf.write(noise, (rng.standard_normal((sr * 20, 2)) * 0.05).astype("float32"), sr, subtype="FLOAT")
    src = open(os.path.join(TOOLS, "deliver_master.py")).read()
    ns = {}
    exec(src[src.index("def eq_filter"):src.index("if MASTER_EQ:")], {"sys": sys}, ns)
    flt = ns["eq_filter"](mix["master_eq"])
    eqd = os.path.join(WORK, "noise_eq.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", noise, "-af", flt, "-c:a", "pcm_f32le", eqd], check=True)
    a_ = sf.read(noise)[0][:, 0]
    b_ = sf.read(eqd)[0][:, 0]
    nf = 1 << 15
    H = lambda x: np.mean([np.abs(np.fft.rfft(x[i:i + nf] * np.hanning(nf))) ** 2 for i in range(0, len(x) - nf, nf // 2)], axis=0)
    resp = 10 * np.log10(H(b_) / H(a_))
    fq = np.fft.rfftfreq(nf, 1 / sr)
    at = lambda f: float(np.median(resp[(fq > f / 2 ** (1 / 12)) & (fq < f * 2 ** (1 / 12))]))
    meas = {f: round(at(f), 2) for f in (30, 42, 167, 1180, 16000)}
    ok(meas[30] < -4 and -4.5 < meas[42] < -1.5 and -1.9 < meas[167] < -1.2 and -2.2 < meas[1180] < -1.5 and 0.5 < meas[16000] < 1.1,
       f"master EQ response on noise (dB): {meas} (template: HPF 42, -1.6 @ 167, -1.9 @ 1180, +0.8 shelf @ 8 k)")

print(f"\n{'ALL PASS' if not FAILS else str(len(FAILS)) + ' FAILED'}; work folder {WORK}")
sys.exit(1 if FAILS else 0)

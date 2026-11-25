"""mvt1 c01: apply a level-only change to rendered stems instead of rendering again (kit LEARNINGS 15).

Usage: stem_fix.py N OLD_BUILD_DIR NEW_BUILD_DIR [--apply] [--out DIR] [--old-src build_reaper.py] [track ...]
  OLD_BUILD_DIR / NEW_BUILD_DIR: folders holding a parts.json and a mix.json each: the data the cycle-N render was made
  from, and the changed data. Only volume-envelope differences are applied (vol_db, roles, trims, fills, mix gains,
  dyn/soft trims): each changed track's stem is multiplied by the new-minus-old envelope, computed with build_reaper's
  own vol_points(), interpolated between envelope points in REAPER's fader scale (c55) on the score tempo map. Anything else
  that differs (notes, CC lanes, EQ, mics) is reported and not simulated.
  The master is rebuilt as the float sum of all stems (no master FX, so the sum equals a render).
  Without --apply the stems and master go to --out (default: a scratch folder) for measurement; with --apply the
  original files are moved to cycles/cNN/render_first/ (once) and the fixed ones written to cycles/cNN/render/.
"""
import glob, json, os, shutil, sys
import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = int(sys.argv[1])
OLD, NEW = sys.argv[2], sys.argv[3]
rest = sys.argv[4:]
APPLY = "--apply" in rest
OUT = rest[rest.index("--out") + 1] if "--out" in rest else f"/private/tmp/claude-501/mockup-loop/mvt2-stemfix-c{N:02d}"
ONLY = [a for i, a in enumerate(rest) if not a.startswith("--") and (i == 0 or rest[i - 1] not in ("--out", "--old-src", "--return-gain"))]
SRC = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_reaper.py")).read()
SRC = SRC[:SRC.index("ENV_LUA = ")]
# mvt1 c15: --old-src FILE: the build_reaper.py the render was made with, when vol_points() changed since (the old
# envelope must be computed with the code that wrote it)
OLD_SRC = SRC
if "--old-src" in rest:
    OLD_SRC = open(rest[rest.index("--old-src") + 1]).read()
    OLD_SRC = OLD_SRC[:OLD_SRC.index("ENV_LUA = ")]


def load(build_dir, src=None):
    SRC_ = SRC if src is None else src
    ns = {"__name__": "build_reaper_partial"}
    argv = sys.argv
    sys.argv = ["build_reaper.py", os.path.join(build_dir, "parts.json"), "/private/tmp/claude-501/mockup-loop/mvt2-stemfix-jobs"]
    try:
        exec(compile(SRC_, "build_reaper.py", "exec"), ns)
    finally:
        sys.argv = argv
    return ns


A, B = load(OLD, OLD_SRC), load(NEW)
# mvt3 c06: --return-gain "R Winds=-2.9,R Brass=0.6"
RETURN_GAIN_DB = {k.strip(): float(v) for k, v in (kv.split("=") for kv in rest[rest.index("--return-gain") + 1].split(","))} \
    if "--return-gain" in rest else {}
C = f"{ROOT}/cycles/c{N:02d}/render"
stems = sorted(f for f in glob.glob(f"{C}/[0-9][0-9]_*.wav") if not f.endswith("00_Master.wav"))
PRE = A["PRE"]
q2s = A["q2s"]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rendermap   # mvt1 c03: renders c00-c02 sound 1/6 qn early on the parts.json map
q2s = rendermap.wrap(q2s, N)
ta = {t["name"]: t for t in A["d"]["tracks"]}
tb = {t["name"]: t for t in B["d"]["tracks"]}
os.makedirs(OUT, exist_ok=True)
total, sr0 = None, None
changed = []
for f in stems:
    name = os.path.basename(f)[3:-4]
    x, sr = sf.read(f, dtype="float64", always_2d=True)
    sr0 = sr
    if name not in ta:
        # mvt3 c06: a return stem (no parts.json track): scaled by RETURN_GAIN_DB {name: dB} when given (a send carries
        # its tracks' gain change; set it by hand from the family change), else summed unchanged
        rg_ = RETURN_GAIN_DB.get(name, 0.0)
        if rg_ and (not ONLY or name in ONLY):
            x = x * 10 ** (rg_ / 20)
            changed.append(name)
            print(f"{name:16s} return stem gain {rg_:+.2f} dB")
            sf.write(f"{OUT}/{os.path.basename(f)}", x.astype(np.float32), sr, subtype="FLOAT")
        total = x if total is None else total + x
        continue
    va = A["vol_points"](ta[name])
    vb = B["vol_points"](tb[name])
    other = [k for k in ta[name] if k not in ("vol_db", "vol_bp") and ta[name].get(k) != tb[name].get(k)]
    if (va != vb or A["mix_for"](name) != B["mix_for"](name)) and (not ONLY or name in ONLY):
        ma, mb = A["mix_for"](name), B["mix_for"](name)
        mdiff = sorted(k for k in set(ma) | set(mb) if k not in ("gain_db", "dyn_trim_db", "soft_trim_db")
                       and ma.get(k) != mb.get(k))
        t = np.arange(len(x)) / sr
        sa = np.array([q2s(p["qn"] - PRE) for p in va]); da = np.array([p["db"] for p in va])
        sb = np.array([q2s(p["qn"] - PRE) for p in vb]); db = np.array([p["db"] for p in vb])
        # mvt2 c55: REAPER draws the line between two envelope points in its fader scale (amplitude ** 0.25), not in dB
        # (build_reaper.py ENV_SCALE); with the simplified envelopes the points are far enough apart for that to matter
        g = 80 * np.log10(np.interp(t, sb, 10 ** (db / 80))) - 80 * np.log10(np.interp(t, sa, 10 ** (da / 80)))
        x = x * (10 ** (g / 20))[:, None]
        changed.append(name)
        print(f"{name:16s} gain change min {g.min():+.2f} max {g.max():+.2f} dB; also differs (not simulated): {other + mdiff}")
        sf.write(f"{OUT}/{os.path.basename(f)}", x.astype(np.float32), sr, subtype="FLOAT")
    elif other:
        print(f"{name:16s} no envelope change; differs (not simulated): {other}")
    total = x if total is None else total + x
sf.write(f"{OUT}/00_Master.wav", total.astype(np.float32), sr0, subtype="FLOAT")
print(f"master (float stem sum) peak {np.abs(total).max():.3f} -> {OUT}/00_Master.wav; changed stems: {len(changed)}")
if APPLY:
    first = f"{ROOT}/cycles/c{N:02d}/render_first"
    # mvt1 c22: keep only the originals this fix replaces (the master and the changed stems); copying every stem
    # (about 4 GB) filled the internal disk in c22. A second fix adds the stems it changes that are not there yet
    os.makedirs(first, exist_ok=True)
    for f in [f"{C}/00_Master.wav"] + [glob.glob(f"{C}/[0-9][0-9]_{n}.wav")[0] for n in changed]:
        if not os.path.exists(os.path.join(first, os.path.basename(f))):
            shutil.copy2(f, first)
    for name in changed:
        f = glob.glob(f"{C}/[0-9][0-9]_{name}.wav")[0]
        shutil.copy2(f"{OUT}/{os.path.basename(f)}", f)
    shutil.copy2(f"{OUT}/00_Master.wav", f"{C}/00_Master.wav")
    print(f"applied: originals in {first}")

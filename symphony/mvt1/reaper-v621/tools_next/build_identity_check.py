"""Prove that a change to build_reaper.py leaves the build unchanged for a given parts.json / mix.json (mvt1 c50).

Usage: python3 tools/build_identity_check.py OLD_BUILD_REAPER.py [--new tools/build_reaper.py] [--parts build/parts.json]
                                             [--work DIR] [--quick]
  Runs OLD and NEW offline on the same parts.json (and the mix.json next to it) in these modes, each in the same jobs
  folder: full build, --midi-only (on the full build's states), --mix-only, a two-track --midi-only --tempo build, then
  the same four with --pass2. Every call to the REAPER bridge (~/.rpr-bridge/rpr.py) is answered with "{}" (nothing is
  sent to REAPER and the lock is not touched). Then it compares, byte for byte, every file each mode wrote (the Lua jobs
  and the Opus .b64 states) and the printed output (stdout and stderr), and prints IDENTICAL or the differences.
  --quick: only the full build and --mix-only of the main pass.
  Exit status 0 when everything is identical.
"""
import filecmp, os, shutil, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
args = sys.argv[1:]


def opt(name, default):
    return args[args.index(name) + 1] if name in args else default


OLD = os.path.abspath(args[0])
NEW = os.path.abspath(opt("--new", os.path.join(TOOLS, "build_reaper.py")))
PARTS = os.path.abspath(opt("--parts", os.path.join(ROOT, "build", "parts.json")))
WORK = os.path.abspath(opt("--work", tempfile.mkdtemp(prefix="build-identity-")))
QUICK = "--quick" in args

RUNNER = r"""
import json, runpy, subprocess, sys
_real = subprocess.run
class _Done:
    returncode = 0
    stdout = "{}"
    stderr = ""
def _fake(cmd, *a, **k):
    if isinstance(cmd, (list, tuple)) and len(cmd) > 1 and str(cmd[1]).endswith("rpr.py"):
        return _Done()
    return _real(cmd, *a, **k)
subprocess.run = _fake
sys.argv = json.loads(sys.argv[1])
runpy.run_path(sys.argv[0], run_name="__main__")
"""


import json
_tracks = json.load(open(PARTS))["tracks"]
two_main = [t["name"] for t in _tracks if t.get("pass", 1) != 2][:2]
two_p2 = [t["name"] for t in _tracks if t.get("pass", 1) == 2][:2]
MODES = [("full", []), ("midi", ["--midi-only"]), ("mix", ["--mix-only"]), ("two", ["--midi-only", "--tempo"] + two_main)]
if two_p2:
    MODES += [("p2full", ["--pass2"]), ("p2midi", ["--midi-only", "--pass2"]), ("p2mix", ["--mix-only", "--pass2"]),
              ("p2two", ["--midi-only", "--tempo", "--pass2"] + two_p2)]
if QUICK:
    MODES = [m for m in MODES if m[0] in ("full", "mix")]


def run_version(tag, src):
    jobs = os.path.join(WORK, "jobs")   # the same path for both versions (the Lua jobs name their .b64 files)
    shutil.rmtree(jobs, ignore_errors=True)
    os.makedirs(jobs)
    for mode, extra in MODES:
        if mode.startswith("p2") and mode == "p2full":
            shutil.rmtree(jobs)
            os.makedirs(jobs)
        before = {f: os.path.getmtime(os.path.join(jobs, f)) for f in os.listdir(jobs)}
        argv = [src, PARTS, jobs] + extra
        p = subprocess.run([sys.executable, "-c", RUNNER, json.dumps(argv)], capture_output=True, text=True)
        out = os.path.join(WORK, tag, mode)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "_stdout.txt"), "w").write(p.stdout)
        open(os.path.join(out, "_stderr.txt"), "w").write(p.stderr)
        open(os.path.join(out, "_returncode.txt"), "w").write(str(p.returncode))
        for f in os.listdir(jobs):
            if f not in before or os.path.getmtime(os.path.join(jobs, f)) != before[f]:
                shutil.copy2(os.path.join(jobs, f), out)
        print(f"{tag:4s} {mode:7s} exit {p.returncode}, {len(os.listdir(out)) - 3} files written", flush=True)


run_version("old", OLD)
run_version("new", NEW)
bad = 0
for mode, _ in MODES:
    a, b = os.path.join(WORK, "old", mode), os.path.join(WORK, "new", mode)
    fa, fb = sorted(os.listdir(a)), sorted(os.listdir(b))
    if fa != fb:
        bad += 1
        print(f"DIFF {mode}: file lists differ: only old {sorted(set(fa) - set(fb))}, only new {sorted(set(fb) - set(fa))}")
    same = [f for f in sorted(set(fa) & set(fb)) if filecmp.cmp(os.path.join(a, f), os.path.join(b, f), shallow=False)]
    diff = sorted(set(fa) & set(fb) - set(same))
    if diff:
        bad += 1
        print(f"DIFF {mode}: {diff}")
    print(f"{mode:7s}: {len(same)} of {len(set(fa) | set(fb))} files byte-identical "
          f"({sum(os.path.getsize(os.path.join(a, f)) for f in same)} bytes)")
print(("IDENTICAL" if not bad else f"NOT IDENTICAL ({bad} modes differ)") + f"; outputs in {WORK}")
sys.exit(1 if bad else 0)

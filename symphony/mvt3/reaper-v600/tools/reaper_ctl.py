#!/usr/bin/env python3
"""REAPER session control for this work folder (series 2).

Usage: reaper_ctl.py [--pass2] lock | start | open | save | quit | restart | status | unlock | create
  --pass2  open / save / quit / restart act on the second-pass project (<main>-pass2.rpp, mvt1 c39); "create" writes it
           from the main project's header (no tracks) if it does not exist
  lock     take the shared REAPER lock for this folder (owner "mvt1"), waiting up to 6 h while another thread holds it
  unlock   release it (refuses while REAPER is running: quit first)
  start    start REAPER (-new) if it is not running and wait until the bridge answers, then 30 s more
  open     open this folder's .rpp (noprompt) and wait for the job (up to 30 min); prints project path and track count
  save     Main_SaveProject on the open project (refuses unless the open project is this folder's .rpp)
  quit     save, then quit (40004); kills REAPER if it is still running 60 s later (a save-changes dialog blocks the bridge)
  restart  quit (if running), start, open
  status   bridge status and REAPER memory

Never save with Main_SaveProjectEx and an explicit path: that writes a copy to the path given while the open project
stays where it was (series 2 c31 overwrote the series 1 project this way).
"""
import glob, json, os, subprocess, sys, time
sys.path.insert(0, os.path.expanduser("~/.rpr-bridge"))
import reaper_lock   # 2026-11-06: the Movement II thread shares this Mac's REAPER; hold the lock for all REAPER work
OWNER = "mvt3"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# mvt1 c39: the second render pass has its own project in this folder (PASS2_SUFFIX); --pass2 selects it
PASS2_SUFFIX = "-pass2.rpp"
MAIN_RPP = sorted(f for f in glob.glob(f"{ROOT}/*.rpp") if not f.endswith(PASS2_SUFFIX))[0]
PASS2_RPP = MAIN_RPP[:-len(".rpp")] + PASS2_SUFFIX
RPP = PASS2_RPP if "--pass2" in sys.argv else MAIN_RPP
RPR = os.path.expanduser("~/.rpr-bridge/rpr.py")
JOBS = f"{ROOT}/jobs"


def alive():
    r = subprocess.run(["python3", RPR, "status"], capture_output=True, text=True)
    return "alive" in r.stdout


def running():
    return subprocess.run(["pgrep", "-x", "REAPER"], capture_output=True).returncode == 0


def job(name, lua, timeout):
    p = f"{JOBS}/_ctl_{name}.lua"
    open(p, "w").write(lua)
    r = subprocess.run(["python3", RPR, "run", p, "--timeout", str(timeout)], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


PROJ = 'local _, fn = reaper.EnumProjects(-1, "")\nreturn { project = fn, tracks = reaper.CountTracks(0) }\n'


def need_lock():
    cur = reaper_lock.read()
    if not cur or cur["owner"] != OWNER or cur["root"] != os.path.realpath(ROOT):
        sys.exit(f"REAPER lock not held by {OWNER} for {ROOT}: {cur}. Run reaper_ctl.py lock first.")


def lock():
    got = reaper_lock.acquire(OWNER, ROOT, wait=6 * 3600, note=" ".join(sys.argv[2:]) or "mvt3 actor")
    if not got:
        sys.exit(f"lock not acquired within 6 h: {reaper_lock.read()}")
    print("locked:", got)


def unlock():
    if running():
        sys.exit("REAPER is still running: reaper_ctl.py quit first, then unlock")
    if not reaper_lock.release(OWNER):
        sys.exit(1)
    print("unlocked")


def start():
    need_lock()
    if not running():
        subprocess.run(["open", "-a", "REAPER", "--args", "-new"])
    for _ in range(120):
        if alive():
            break
        time.sleep(5)
    else:
        sys.exit("REAPER bridge did not come up")
    time.sleep(30)
    print("started")


def open_():
    need_lock()
    rc, out = job("open", f'reaper.Main_openProject("noprompt:{RPP}")\n' + PROJ, 1800)
    print(out)
    if rc or RPP not in out:
        sys.exit("open failed")


def save():
    rc, out = job("proj", PROJ, 60)
    if RPP not in out:
        sys.exit(f"refusing to save: open project is not {RPP}: {out}")
    rc, out = job("save", "reaper.Main_SaveProject(0, false)\n" + PROJ, 600)
    print(out)
    if rc:
        sys.exit("save failed")


def quit_():
    if not running():
        print("not running")
        return
    if alive():
        save()
        job("quit", "reaper.Main_OnCommand(40004, 0)\n", 60)
    for _ in range(12):
        if not running():
            print("quit")
            return
        time.sleep(5)
    subprocess.run(["pkill", "-x", "REAPER"])
    time.sleep(10)
    if running():
        subprocess.run(["pkill", "-9", "-x", "REAPER"])
        time.sleep(5)
    print("killed after save")


def create2():
    """mvt1 c39: write the second-pass project (PASS2_RPP) if it does not exist: the main project's header (project
    settings, render settings with RENDER_1X 1, 48 kHz, no master FX) without its tracks. build_reaper.py --pass2 then
    writes the tempo map and the pass-2 tracks into it, and reaper_ctl.py --pass2 save keeps it."""
    if os.path.exists(PASS2_RPP):
        print("exists:", PASS2_RPP)
        return
    head = []
    with open(MAIN_RPP, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith("  <TRACK"):
                break
            head.append(line)
    txt = "".join(head)
    if "RENDER_1X 1" not in txt or "<MASTERFXLIST" in txt:
        sys.exit("main project header lacks RENDER_1X 1 or has master FX; not copied")
    open(PASS2_RPP, "w").write(txt + ">\n")
    print("created:", PASS2_RPP, len(head), "header lines")


def status():
    print("bridge:", "alive" if alive() else "not answering", "| process:", "running" if running() else "none")
    print(subprocess.run("top -l 1 -o mem -stats pid,command,mem,cmprs | sed -n 12,17p", shell=True,
                         capture_output=True, text=True).stdout)


args_ = [a for a in sys.argv[1:] if a != "--pass2"]
cmd = args_[0] if args_ else "status"
if cmd == "lock":   # the note is everything after "lock"
    sys.argv = [sys.argv[0]] + args_
{"start": start, "open": open_, "save": save, "quit": quit_, "status": status, "lock": lock, "unlock": unlock,
 "create": create2, "restart": lambda: (quit_(), start(), open_())}[cmd]()

#!/usr/bin/env python3
"""One REAPER for several mockup threads: a lock file that says which work folder owns REAPER right now.

  reaper_lock.py acquire --owner mvt1 --root /path/to/work/folder [--wait 14400] [--note "c36 actor"]
  reaper_lock.py release --owner mvt1 [--force]
  reaper_lock.py status

Rules (2026-11-06, Dan: two movement threads share this Mac and must never overlap on REAPER):
- Acquire before starting or opening REAPER; hold it through build, render, stem fix and save; quit REAPER, then release.
- Only one REAPER project fits in memory (about 46 GB each). Never start REAPER while another owner holds the lock.
- rpr.py refuses `run`/`eval`/`snapshot` when there is no lock, and when the job file (or the working directory for
  eval/snapshot) is outside the lock's root folder (temp folders under /private/tmp and /tmp are allowed, and so is any
  caller whose environment has RPR_OWNER set to the lock's owner).
- Never break the other owner's lock. If it is older than STALE_H hours, message that thread first.
"""
import argparse, json, os, subprocess, sys, time
from pathlib import Path

BRIDGE = Path(os.environ.get("RPR_BRIDGE", Path.home() / ".rpr-bridge"))
LOCK = BRIDGE / "REAPER.lock"
STALE_H = 3
TEMP_ROOTS = ("/private/tmp/", "/tmp/", "/private/var/folders/")


def read():
    try:
        return json.loads(LOCK.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def reaper_running():
    return subprocess.run(["pgrep", "-x", "REAPER"], capture_output=True).returncode == 0


def _create(owner, root, note):
    data = {"owner": owner, "root": str(Path(root).resolve()), "since": time.strftime("%Y-%m-%d %H:%M:%S"),
            "since_epoch": time.time(), "note": note or ""}
    fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    with os.fdopen(fd, "w") as f:
        json.dump(data, f)
    return data


def acquire(owner, root, wait=0, note=""):
    deadline = time.time() + wait
    said = False
    while True:
        cur = read()
        if cur is None:
            try:
                return _create(owner, root, note)
            except FileExistsError:
                continue
        if cur["owner"] == owner and cur["root"] == str(Path(root).resolve()):
            cur["note"] = note or cur.get("note", "")
            LOCK.write_text(json.dumps(cur))
            return cur
        age_h = (time.time() - cur.get("since_epoch", time.time())) / 3600
        if age_h > STALE_H and not said:
            print(f"lock is {age_h:.1f} h old: message its owner ({cur['owner']}) before anything else; never break it", file=sys.stderr)
        if time.time() >= deadline:
            return None
        if not said:
            print(f"waiting: REAPER is held by {cur['owner']} ({cur.get('note', '')}) since {cur['since']}", file=sys.stderr)
            said = True
        time.sleep(30)


def release(owner, force=False):
    cur = read()
    if cur is None:
        return True
    if cur["owner"] != owner and not force:
        print(f"not released: the lock belongs to {cur['owner']}", file=sys.stderr)
        return False
    if reaper_running() and not force:
        print("not released: REAPER is still running; quit it first (reaper_ctl.py quit)", file=sys.stderr)
        return False
    LOCK.unlink(missing_ok=True)
    return True


def allowed(path):
    """rpr.py: may a job from this file path (or working directory) talk to REAPER now?"""
    cur = read()
    if cur is None:
        return False, "no REAPER lock is held; acquire it first (~/.rpr-bridge/reaper_lock.py acquire --owner ... --root ...)"
    p = str(Path(path).resolve())
    if (p + os.sep).startswith(cur["root"] + os.sep) or (p + os.sep).startswith(TEMP_ROOTS):
        return True, ""
    if os.environ.get("RPR_OWNER") == cur["owner"]:
        return True, ""
    return False, f"REAPER is held by {cur['owner']} for {cur['root']} (since {cur['since']}); {p} is outside it"


def main():
    ap = argparse.ArgumentParser(prog="reaper_lock")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("acquire"); p.add_argument("--owner", required=True); p.add_argument("--root", required=True)
    p.add_argument("--wait", type=float, default=0); p.add_argument("--note", default="")
    p = sub.add_parser("release"); p.add_argument("--owner", required=True); p.add_argument("--force", action="store_true")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "acquire":
        got = acquire(a.owner, a.root, a.wait, a.note)
        if not got:
            sys.exit(f"lock not acquired: {read()}")
        print(json.dumps(got))
    elif a.cmd == "release":
        sys.exit(0 if release(a.owner, a.force) else 1)
    else:
        cur = read()
        print(json.dumps(cur) if cur else "free", "| REAPER", "running" if reaper_running() else "not running")


if __name__ == "__main__":
    main()

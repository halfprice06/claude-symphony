#!/usr/bin/env python3
"""rpr — send Lua jobs to a running REAPER through the file bridge.

  rpr run script.lua [--timeout 20]     run a file
  rpr eval 'return R.tracks()'          run inline Lua
  rpr snapshot                           compact project state
  rpr status                             is the runner alive?
  rpr api <regex>                        grep the ReaScript reference (api.txt)
"""
import argparse, json, os, re, sys, time, uuid
from pathlib import Path

BRIDGE = Path(os.environ.get("RPR_BRIDGE", Path.home() / ".rpr-bridge"))
INBOX, OUTBOX = BRIDGE / "inbox", BRIDGE / "outbox"


def alive(max_age=3.0):
    hb = BRIDGE / "heartbeat"
    return hb.exists() and (time.time() - hb.stat().st_mtime) < max_age


def submit(code: str, timeout: float) -> dict:
    if not alive():
        sys.exit("bridge not running: no recent heartbeat. Is REAPER open with claude_bridge.lua loaded?")
    job = uuid.uuid4().hex[:12]
    tmp, final = INBOX / f"{job}.tmp", INBOX / f"{job}.lua"
    tmp.write_text(code, encoding="utf-8")
    os.replace(tmp, final)                      # atomic on all platforms
    out = OUTBOX / f"{job}.json"
    deadline = time.time() + timeout
    while time.time() < deadline:
        if out.exists():
            data = None
            for _ in range(50):                 # tolerate a half-written file
                try:
                    data = json.loads(out.read_text(encoding="utf-8"))
                    break
                except (json.JSONDecodeError, OSError):
                    time.sleep(0.01)
            out.unlink(missing_ok=True)
            if data is None:
                sys.exit(f"unreadable result for job {job}")
            return data
        time.sleep(0.02)
    sys.exit(f"timeout after {timeout}s (job {job}). REAPER may be busy, rendering, or the script may be stuck.")


def report(data: dict) -> int:
    if data.get("log"):
        print("\n".join(data["log"]), file=sys.stderr)
    if data.get("ok"):
        print(json.dumps(data.get("result"), indent=2, ensure_ascii=False))
        return 0
    print("ERROR:", data.get("error"), file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(prog="rpr")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("run");   p.add_argument("file"); p.add_argument("--timeout", type=float, default=20)
    p = sub.add_parser("eval");  p.add_argument("code"); p.add_argument("--timeout", type=float, default=20)
    sub.add_parser("snapshot")
    sub.add_parser("status")
    p = sub.add_parser("api");   p.add_argument("pattern"); p.add_argument("-C", type=int, default=2)
    a = ap.parse_args()

    if a.cmd == "status":
        print("alive" if alive() else "not running"); return
    if a.cmd in ("run", "eval", "snapshot") and os.environ.get("RPR_NO_LOCK") != "1":
        # 2026-11-06: two mockup threads share REAPER; see reaper_lock.py
        sys.path.insert(0, str(BRIDGE))
        import reaper_lock
        ok, why = reaper_lock.allowed(a.file if a.cmd == "run" else os.getcwd())
        if not ok:
            sys.exit("rpr: refused: " + why)
    if a.cmd == "run":
        sys.exit(report(submit(Path(a.file).read_text(encoding="utf-8"), a.timeout)))
    if a.cmd == "eval":
        sys.exit(report(submit(a.code, a.timeout)))
    if a.cmd == "snapshot":
        sys.exit(report(submit("return R.snapshot()", 20)))
    if a.cmd == "api":
        apif = BRIDGE / "api.txt"
        if not apif.exists():
            sys.exit("api.txt missing; see guide §3.1")
        lines = apif.read_text(encoding="utf-8", errors="replace").splitlines()
        rx = re.compile(a.pattern, re.I)
        hits = [i for i, l in enumerate(lines) if rx.search(l)]
        shown = set()
        for i in hits[:60]:
            for j in range(max(0, i - a.C), min(len(lines), i + a.C + 1)):
                if j not in shown:
                    print(lines[j]); shown.add(j)
            print("--")
        if len(hits) > 60:
            print(f"... {len(hits) - 60} more matches; narrow the pattern")


if __name__ == "__main__":
    main()

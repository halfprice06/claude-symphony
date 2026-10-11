"""Install the REAPER file bridge from guides/reaper-claude-scripting-guide.md (runner, CLI, helper library).

Usage: python3 install_bridge.py   (macOS; REAPER resource path ~/Library/Application Support/REAPER)
Extracts the three code blocks from the guide, writes them to ~/.rpr-bridge/ and REAPER's Scripts folder,
and adds an __startup.lua line so the runner starts with REAPER. Existing files are left alone unless --force.
"""
import pathlib, re, sys
GUIDE = pathlib.Path(__file__).resolve().parents[2] / "guides" / "reaper-claude-scripting-guide.md"
home = pathlib.Path.home()
res = home / "Library/Application Support/REAPER/Scripts"
bridge = home / ".rpr-bridge"
force = "--force" in sys.argv
for d in ("inbox", "outbox", "lib", "libs", "jobs"):
    (bridge / d).mkdir(parents=True, exist_ok=True)
targets = {"-- claude_bridge.lua": res / "claude_bridge.lua",
           '#!/usr/bin/env python3\n"""rpr': bridge / "rpr.py",
           "-- rpr.lua": bridge / "lib" / "rpr.lua"}
for _, body in re.findall(r"```(\w*)\n(.*?)```", GUIDE.read_text(), re.S):
    for head, path in targets.items():
        if body.startswith(head) and (force or not path.exists()):
            path.write_text(body); print("wrote", path)
start = res / "__startup.lua"
line = 'dofile(reaper.GetResourcePath() .. "/Scripts/claude_bridge.lua")\n'
if not start.exists() or "claude_bridge.lua" not in start.read_text():
    with open(start, "a") as f: f.write(line)
    print("added runner to", start)

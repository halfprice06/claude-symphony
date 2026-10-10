# REAPER + Claude: a scripting guide for film-score work

Written 10 October 2026 against REAPER 7.8x, Claude Code, and Claude Opus 5.5. Function signatures are from the ReaScript reference for 7.82; the guide tells you how to confirm any of them against your own build before you depend on it.

## 0. What this guide assumes

- You want Claude to do real work inside REAPER — set up cues against picture, build an orchestral template, write notes, keyswitches and CC curves, read state back, render stems — and you want to own the mechanism rather than depend on a single-maintainer MCP server.
- You can run Python and edit a Lua file. Nothing here needs a compiler.
- REAPER runs on Windows or macOS, because that is where Kontakt, Opus, Spitfire, SINE, Synchron Player and VE Pro run. REAPER itself is fine on Linux, and everything in this guide works there, but the sample-library ecosystem does not (and EastWest's iLok licensing has no confirmed working setup under Wine). A split setup — REAPER plus samples on Windows/macOS, Claude Code on Linux talking to a shared folder — is covered in §9.
- Claude cannot hear. Every design decision below follows from that: Claude edits symbolic data and reads back symbolic state; you audition.

## 1. The architecture

ReaScript runs inside REAPER. Claude runs outside. REAPER's embedded Lua cannot open sockets, and there is no verified command that injects a script into an already-running instance. So the connection is a folder: a Lua script running inside REAPER on a `defer()` loop watches an inbox, executes each `.lua` file that lands there inside an undo block, and writes a JSON result to an outbox. A Python CLI on the other side writes the job, waits for the result, and prints it. Claude Code calls the CLI through Bash.

```
Claude Code ──bash──▶ rpr.py ──writes──▶ ~/.rpr-bridge/inbox/<id>.lua
                                                   │
                                          claude_bridge.lua (inside REAPER, ~30 Hz poll)
                                          runs job in undo block, preloads helper lib R
                                                   │
Claude Code ◀──json─── rpr.py ◀──reads─── ~/.rpr-bridge/outbox/<id>.json
```

Round trip is roughly 40–150 ms. Each job is one undo step. The helper library (`R`) gives Claude tested primitives for the film-scoring operations so it composes from known-good functions instead of the raw 900-function API every time.

Why this and not a 180-tool MCP server: scripts cover the entire API, batch naturally (one script does fifty operations in one round trip), and depend on nothing but REAPER's own stable scripting surface. Typed MCP tools are worth adding later for exactly three things: compact read-back formats Claude asks for constantly, input validation, and narrowing the blast radius of mutations. §4 shows the minimal MCP wrapper for when you want Claude Desktop (which has no shell) to reach REAPER; it is twelve lines on top of the same bridge.

## 2. Install the bridge

### 2.1 Layout

```
~/.rpr-bridge/
  inbox/        jobs land here as <id>.lua (written as .tmp, renamed when complete)
  outbox/       results appear as <id>.json
  lib/rpr.lua   helper library, reloaded for every job
  libs/         your sample-library articulation maps (§6.6)
  api.txt       greppable ReaScript reference for your REAPER build (§3.1)
  rpr.py        the CLI
  heartbeat     touched once a second by the runner
```

On Windows, `~` is `%USERPROFILE%`. Keep this folder out of cloud-sync (Dropbox, iCloud, OneDrive): anything that can write to `inbox/` can drive REAPER.

### 2.2 The runner (inside REAPER)

Save as `<REAPER resource path>/Scripts/claude_bridge.lua`. Find the resource path with Options → Show REAPER resource path in explorer/finder.

```lua
-- claude_bridge.lua — executes Lua jobs from ~/.rpr-bridge/inbox inside REAPER.
-- Each job runs in one undo block with dialogs stubbed out and console output captured.

local sep    = package.config:sub(1, 1)
local home   = os.getenv("HOME") or os.getenv("USERPROFILE")
local BRIDGE = home .. sep .. ".rpr-bridge"
local INBOX  = BRIDGE .. sep .. "inbox"
local OUTBOX = BRIDGE .. sep .. "outbox"
local LIBF   = BRIDGE .. sep .. "lib" .. sep .. "rpr.lua"

reaper.RecursiveCreateDirectory(INBOX, 0)
reaper.RecursiveCreateDirectory(OUTBOX, 0)

-- ---------- JSON (encode only; jobs are Lua, results are JSON) ----------
local function json(v, depth)
  depth = depth or 0
  if depth > 40 then return '"<too deep>"' end
  local t = type(v)
  if v == nil then return "null"
  elseif t == "boolean" then return tostring(v)
  elseif t == "number" then
    if v ~= v or v == math.huge or v == -math.huge then return "null" end
    if math.type(v) == "integer" then return tostring(v) end
    return string.format("%.10g", v)
  elseif t == "string" then
    local s = v:gsub('[%c"\\]', function(c)
      local m = { ['"'] = '\\"', ['\\'] = '\\\\', ['\n'] = '\\n', ['\r'] = '\\r', ['\t'] = '\\t' }
      return m[c] or string.format("\\u%04x", c:byte())
    end)
    return '"' .. s .. '"'
  elseif t == "table" then
    local n = #v
    local is_array = (n > 0) or (next(v) == nil)
    if is_array then
      for k in pairs(v) do
        if math.type(k) ~= "integer" or k < 1 or k > n then is_array = false break end
      end
    end
    local out = {}
    if is_array then
      for i = 1, n do out[i] = json(v[i], depth + 1) end
      return "[" .. table.concat(out, ",") .. "]"
    end
    for k, val in pairs(v) do out[#out + 1] = json(tostring(k)) .. ":" .. json(val, depth + 1) end
    table.sort(out)
    return "{" .. table.concat(out, ",") .. "}"
  end
  return json(tostring(v))
end

local function write_atomic(path, text)
  local tmp = path .. ".tmp"
  local f = assert(io.open(tmp, "wb")); f:write(text); f:close()
  os.remove(path); os.rename(tmp, path)
end

-- ---------- dialog stubs: a job must never block REAPER on a modal ----------
local STUBS = {
  ShowMessageBox         = function() return 1 end,
  MB                     = function() return 1 end,
  GetUserInputs          = function() return false, "" end,
  GetUserFileNameForRead = function() return false, "" end,
}

local function run_job(path, id)
  local log, saved = {}, {}
  for k, f in pairs(STUBS) do saved[k] = reaper[k]; reaper[k] = f end
  saved.ShowConsoleMsg = reaper.ShowConsoleMsg
  reaper.ShowConsoleMsg = function(s) log[#log + 1] = tostring(s) end

  -- reload helper library so edits take effect without restarting REAPER
  local libok, lib = pcall(dofile, LIBF)
  R = libok and lib or nil
  BRIDGE_DIR = BRIDGE

  local t0 = reaper.time_precise()
  local ok, result
  local chunk, lerr = loadfile(path)
  if not chunk then
    ok, result = false, lerr
  else
    reaper.Undo_BeginBlock2(0)
    reaper.PreventUIRefresh(1)
    ok, result = xpcall(chunk, debug.traceback)
    reaper.PreventUIRefresh(-1)
    reaper.UpdateArrange()
    reaper.UpdateTimeline()
    reaper.TrackList_AdjustWindows(false)
    reaper.Undo_EndBlock2(0, "Claude job " .. id, -1)
  end

  for k, f in pairs(saved) do reaper[k] = f end
  if not libok then log[#log + 1] = "lib load failed: " .. tostring(lib) end

  write_atomic(OUTBOX .. sep .. id .. ".json", json({
    id = id, ok = ok,
    result = ok and result or nil,
    error = (not ok) and tostring(result) or nil,
    log = log,
    ms = math.floor((reaper.time_precise() - t0) * 1000),
  }))
end

local last_beat = 0
local function tick()
  if reaper.file_exists(BRIDGE .. sep .. "STOP") then
    os.remove(BRIDGE .. sep .. "STOP")
    return -- not re-deferred: runner exits
  end
  local now = reaper.time_precise()
  if now - last_beat > 1 then
    write_atomic(BRIDGE .. sep .. "heartbeat", tostring(os.time()))
    last_beat = now
  end
  reaper.EnumerateFiles(INBOX, -1) -- invalidate REAPER's directory cache
  local i = 0
  while true do
    local fn = reaper.EnumerateFiles(INBOX, i)
    if not fn or fn == "" then break end
    if fn:match("%.lua$") then
      local id = fn:sub(1, -5)
      local src, claimed = INBOX .. sep .. fn, INBOX .. sep .. id .. ".running"
      if os.rename(src, claimed) then
        run_job(claimed, id)
        os.remove(claimed)
      end
      reaper.EnumerateFiles(INBOX, -1)
      i = -1
    end
    i = i + 1
  end
  reaper.defer(tick)
end

tick()
```

Notes on the design:

- Jobs are claimed by renaming `<id>.lua` to `<id>.running`, so a second runner (if you ever start one by accident) cannot execute the same job.
- `R` is reloaded from `lib/rpr.lua` for every job, so you and Claude can edit the library without restarting REAPER.
- `PreventUIRefresh` keeps the arrange view from redrawing per operation; the explicit `UpdateArrange`/`UpdateTimeline` at the end repaints once.
- Scripts run on REAPER's main thread. While a job runs, REAPER's UI is frozen. Keep jobs under a couple of seconds; chunk long work (one job per cue, per section, per track).

### 2.3 Start it automatically

Create `<REAPER resource path>/Scripts/__startup.lua` (REAPER runs this file at launch) containing:

```lua
dofile(reaper.GetResourcePath() .. "/Scripts/claude_bridge.lua")
```

To start it by hand instead: Actions → Show action list → New action → Load ReaScript, pick `claude_bridge.lua`, then run it. To stop it: create an empty file `~/.rpr-bridge/STOP`, or use Actions → "ReaScript: Terminate all running ReaScripts".

### 2.4 The CLI (outside REAPER)

Save as `~/.rpr-bridge/rpr.py`. Python 3.8 or newer, standard library only.

```python
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
```

Make it easy to call: `alias rpr='python3 ~/.rpr-bridge/rpr.py'` (or a small `rpr.cmd` on Windows).

### 2.5 Smoke test

With REAPER open and the runner started:

```
rpr status
rpr eval 'return { v = reaper.GetAppVersion(), tracks = reaper.CountTracks(0), lib = R ~= nil }'
```

You should see the version, a track count, and `"lib": true` once `lib/rpr.lua` exists (§5). If `lib` is false, the result's `log` will say why. Then:

```
rpr eval 'return R.project_info()'
```

Confirm `start_tc` matches the project start timecode shown on REAPER's ruler. If it does, timecode parsing honors your project offset and frame rate, and the rest of the time helpers are trustworthy.

## 3. Teach Claude the API

### 3.1 Get the reference into a greppable file

Do not use the copy on reaper.fm; it is not always current and it omits extensions you have installed. Generate the reference from your own build: Actions → "ReaScript: Open ReaScript documentation (html)". REAPER writes `reascripthelp.html` into its resource path and opens it. Convert it to text:

```python
# make_api_txt.py  — run once; rerun after REAPER or extension updates
import html, re, sys
from pathlib import Path
src = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
txt = re.sub(r"<script.*?</script>|<style.*?</style>", "", src, flags=re.S)
txt = re.sub(r"<br\s*/?>|</p>|</div>|</h\d>", "\n", txt)
txt = html.unescape(re.sub(r"<[^>]+>", "", txt))
txt = re.sub(r"\n{3,}", "\n\n", txt)
Path.home().joinpath(".rpr-bridge", "api.txt").write_text(txt, encoding="utf-8")
```

The result includes the SWS and js_ReaScriptAPI functions if those are installed, which the web copy does not. `rpr api 'SetTempoTimeSigMarker'` then prints the exact Lua signature for your build. Claude should run this before using any function it has not used in the session; the reference is about a megabyte and does not belong in context whole.

### 3.2 CLAUDE.md

Put this in the project folder where you run Claude Code. Adjust paths.

```markdown
# REAPER bridge

REAPER is running with a file bridge. Run Lua inside it with:

    rpr run <file.lua>            # or: python3 ~/.rpr-bridge/rpr.py run <file.lua>
    rpr eval '<lua>'
    rpr snapshot                  # project info, tempo map, markers, tracks
    rpr api '<regex>'             # exact ReaScript signatures for THIS build

Every job runs in one undo block. `return` a table from the job to get JSON back.
`R` (lib/rpr.lua) is preloaded in every job: time/timecode, tempo map, markers,
tracks, MIDI notes/keyswitches/CC curves, FX params, render. Prefer R.* over raw
API calls for those; use raw reaper.* for anything else.

## Rules
1. Read before you write. Start with `rpr snapshot`. Never assume track names,
   tempo, or the project start timecode.
2. Batch. One job per musical operation (a cue, a section, a track), never one
   job per note. Build the data as a Lua table and pass it to R.write_cue.
3. Check signatures. Before using an unfamiliar function, `rpr api <name>`.
4. Verify after writing: read back counts or a sample and report them.
5. Never open dialogs. Dialog functions are stubbed and return defaults.
6. Keep jobs short (< ~2 s of work). REAPER's UI is frozen while a job runs.
   Renders block the CLI: use `--timeout 900` for `R.render_*`.
7. Times passed to R.* are absolute project seconds. Convert timecode strings
   with R.tc_to_sec("01:00:12:08"); never do frame math by hand.
8. Keyswitch pitches and CC assignments come from the library maps in
   ~/.rpr-bridge/libs/. Never invent a keyswitch.
9. You cannot hear the result. Say so when a judgment depends on sound, and
   ask for an audition instead of guessing.
10. On any error, stop and show the error and the job source; do not retry
    blindly. The failed job is already one undo step.
```

### 3.3 How Claude should work a task

The pattern that works: snapshot → plan in prose → one job per operation → read-back → report. Claude writes each job to a file in the project (`jobs/0012_vln1_phrase.lua`) rather than inline `eval`, so you can read, rerun and keep them. Long projects accumulate a library of cue scripts that are themselves documentation of how the project was built.

## 4. Optional: the MCP wrapper (Claude Desktop, or typed tools later)

Claude Code does not need this. Claude Desktop has no shell, so it does. The same bridge, exposed as two tools:

```python
# mcp_server.py — pip install mcp
import sys
sys.path.insert(0, str(__import__("pathlib").Path.home() / ".rpr-bridge"))
import json, rpr
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("reaper")

@mcp.tool()
def run_lua(code: str, timeout: float = 20) -> str:
    """Run Lua inside the live REAPER project. `return` a table for JSON. Helper lib R is preloaded."""
    return json.dumps(rpr.submit(code, timeout))

@mcp.tool()
def snapshot() -> str:
    """Project info, tempo map, markers, and track list."""
    return json.dumps(rpr.submit("return R.snapshot()", 20))

if __name__ == "__main__":
    mcp.run()
```

Register it:

- Claude Code (optional): `claude mcp add --transport stdio reaper -- python3 ~/.rpr-bridge/mcp_server.py` (`--scope project` writes it to `.mcp.json` for the project). Claude Code caps MCP tool output at 25,000 tokens by default (`MAX_MCP_OUTPUT_TOKENS` to raise it) and warns above 10,000, which is one more reason to paginate read-backs.
- Claude Desktop: add the same command to `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/`; Windows: `%APPDATA%\Claude\`) under `mcpServers`.

When you later want typed tools — `set_tempo_marker`, `add_hit_points`, `write_cue` with validated schemas — add them to this file as thin wrappers that build a Lua call to the matching `R.*` function. Keep the count under 30–50; Anthropic's own guidance is that tool selection degrades past that, and `run_lua` already covers everything else.

## 5. The helper library: `lib/rpr.lua`

This is the part worth maintaining. Every function takes and returns plain data (seconds, pitches, tables) so Claude can build inputs as literal tables. Save as `~/.rpr-bridge/lib/rpr.lua`.

```lua
-- rpr.lua — helper library preloaded as global R by claude_bridge.lua
local R = {}
local P = 0 -- current project

-- ===== time & timecode ================================================
function R.tc_to_sec(tc)  return reaper.parse_timestr_pos(tc, 5) end   -- "HH:MM:SS:FF" -> project seconds
function R.sec_to_tc(sec) return reaper.format_timestr_pos(sec, "", 5) end
function R.sec_to_bar(sec)                                               -- "bar.beat" string
  return reaper.format_timestr_pos(sec, "", 2)
end
function R.qn_at(sec) return reaper.TimeMap2_timeToQN(P, sec) end        -- quarter-note position
function R.sec_at_qn(qn) return reaper.TimeMap2_QNToTime(P, qn) end

function R.project_info()
  local fps, drop = reaper.TimeMap_curFrameRate(P)
  local off = reaper.GetProjectTimeOffset(P, false)
  return {
    name = reaper.GetProjectName(P, ""),
    fps = fps, drop_frame = drop,
    start_offset_sec = off, start_tc = R.sec_to_tc(0),
    length_sec = reaper.GetProjectLength(P),
    bpm_at_start = reaper.TimeMap_GetDividedBpmAtTime(0),
    tracks = reaper.CountTracks(P),
    sample_rate = reaper.GetSetProjectInfo(P, "PROJECT_SRATE", 0, false),
  }
end

-- ===== tempo map =========================================================
function R.tempo_markers()
  local out = {}
  for i = 0, reaper.CountTempoTimeSigMarkers(P) - 1 do
    local _, pos, meas, beat, bpm, num, den, lin = reaper.GetTempoTimeSigMarker(P, i)
    out[#out + 1] = { idx = i, time = pos, tc = R.sec_to_tc(pos), measure = meas, beat = beat,
                      bpm = bpm, num = num, den = den, linear = lin }
  end
  return out
end

-- Add (or update) a tempo/time-signature marker at an absolute time.
-- num/den = 0 keeps the current meter. linear=true ramps to the next marker.
function R.set_tempo_at(sec, bpm, num, den, linear)
  local idx = -1
  for i = 0, reaper.CountTempoTimeSigMarkers(P) - 1 do
    local _, pos = reaper.GetTempoTimeSigMarker(P, i)
    if math.abs(pos - sec) < 1e-4 then idx = i break end
  end
  local ok = reaper.SetTempoTimeSigMarker(P, idx, sec, -1, -1, bpm, num or 0, den or 0, linear or false)
  reaper.UpdateTimeline()
  return ok
end

function R.clear_tempo_map()  -- keeps marker 0 (project tempo)
  for i = reaper.CountTempoTimeSigMarkers(P) - 1, 1, -1 do reaper.DeleteTempoTimeSigMarker(P, i) end
  reaper.UpdateTimeline()
end

-- Candidate tempi that put hit t2 on a whole beat if the music starts at t1.
-- Returns { {bpm=, beats=}, ... } within [min_bpm, max_bpm]; Claude picks musically.
function R.tempi_for_hit(t1, t2, min_bpm, max_bpm)
  local out, span = {}, t2 - t1
  for beats = 1, 2000 do
    local bpm = beats * 60 / span
    if bpm > max_bpm then break end
    if bpm >= min_bpm then out[#out + 1] = { bpm = bpm, beats = beats } end
  end
  return out
end

-- ===== markers & regions ===============================================
function R.rgb(r, g, b) return reaper.ColorToNative(r, g, b) | 0x1000000 end

function R.markers()
  local out, i = {}, 0
  while true do
    local ret, isrgn, pos, rgnend, name, num, color = reaper.EnumProjectMarkers3(P, i)
    if ret == 0 then break end
    out[#out + 1] = { idx = i, region = isrgn, time = pos, tc = R.sec_to_tc(pos),
                      ["end"] = isrgn and rgnend or nil, name = name, number = num }
    i = i + 1
  end
  return out
end
function R.add_marker(sec, name, color) return reaper.AddProjectMarker2(P, false, sec, 0, name, -1, color or 0) end
function R.add_region(s, e, name, color) return reaper.AddProjectMarker2(P, true, s, e, name, -1, color or 0) end
function R.add_hit_points(hits)   -- { {tc="01:00:12:08", name="door slam"}, ... }
  local ids = {}
  for _, h in ipairs(hits) do ids[#ids + 1] = R.add_marker(R.tc_to_sec(h.tc), h.name, h.color) end
  return ids
end
function R.delete_markers(match)  -- match: Lua pattern on name, or nil for all
  local _, nm, nr = reaper.CountProjectMarkers(P)
  local n = 0
  for i = nm + nr - 1, 0, -1 do
    local _, _, _, _, name = reaper.EnumProjectMarkers3(P, i)
    if not match or name:match(match) then reaper.DeleteProjectMarkerByIndex(P, i); n = n + 1 end
  end
  return n
end

-- ===== tracks ============================================================
function R.tracks()
  local out = {}
  for i = 0, reaper.CountTracks(P) - 1 do
    local tr = reaper.GetTrack(P, i)
    local _, name = reaper.GetTrackName(tr)
    local fx = {}
    for f = 0, reaper.TrackFX_GetCount(tr) - 1 do
      local _, fxname = reaper.TrackFX_GetFXName(tr, f, "")
      fx[#fx + 1] = fxname
    end
    out[#out + 1] = {
      idx = i, name = name,
      folder = reaper.GetMediaTrackInfo_Value(tr, "I_FOLDERDEPTH"),
      items = reaper.CountTrackMediaItems(tr), fx = fx,
      mute = reaper.GetMediaTrackInfo_Value(tr, "B_MUTE") == 1,
      vol_db = 20 * math.log(math.max(reaper.GetMediaTrackInfo_Value(tr, "D_VOL"), 1e-9), 10),
    }
  end
  return out
end

function R.track_by_name(name)
  for i = 0, reaper.CountTracks(P) - 1 do
    local tr = reaper.GetTrack(P, i)
    local _, n = reaper.GetTrackName(tr)
    if n == name then return tr, i end
  end
  return nil
end

function R.installed_fx(filter)  -- names exactly as TrackFX_AddByName expects them
  local out, i = {}, 0
  while true do
    local ok, name = reaper.EnumInstalledFX(i)
    if not ok then break end
    if not filter or name:lower():find(filter:lower(), 1, true) then out[#out + 1] = name end
    i = i + 1
  end
  return out
end

-- opts: idx, color, folder (1 = starts a folder, -1 = last child), instrument (exact FX name), midi_in (default true)
function R.add_track(name, opts)
  opts = opts or {}
  local idx = opts.idx or reaper.CountTracks(P)
  reaper.InsertTrackAtIndex(idx, true)
  local tr = reaper.GetTrack(P, idx)
  reaper.GetSetMediaTrackInfo_String(tr, "P_NAME", name, true)
  if opts.color  then reaper.SetMediaTrackInfo_Value(tr, "I_CUSTOMCOLOR", opts.color) end
  if opts.folder then reaper.SetMediaTrackInfo_Value(tr, "I_FOLDERDEPTH", opts.folder) end
  if opts.instrument then
    local fx = reaper.TrackFX_AddByName(tr, opts.instrument, false, -1)
    if fx < 0 then error("instrument not found: " .. opts.instrument .. " (use R.installed_fx)") end
  end
  if opts.midi_in ~= false then
    reaper.SetMediaTrackInfo_Value(tr, "I_RECINPUT", 4096 + 63 * 32) -- all MIDI devices, all channels
    reaper.SetMediaTrackInfo_Value(tr, "I_RECMON", 1)
  end
  return tr, idx
end

-- ===== MIDI ==============================================================
function R.new_midi_item(tr, start_sec, end_sec)
  local item = reaper.CreateNewMIDIItemInProj(tr, start_sec, end_sec, false)
  return item, reaper.GetActiveTake(item)
end

function R.items(tr)
  local out = {}
  for i = 0, reaper.CountTrackMediaItems(tr) - 1 do
    local it = reaper.GetTrackMediaItem(tr, i)
    local take = reaper.GetActiveTake(it)
    local pos = reaper.GetMediaItemInfo_Value(it, "D_POSITION")
    local _, tname = reaper.GetSetMediaItemTakeInfo_String(take, "P_NAME", "", false)
    local _, nn, cc = reaper.MIDI_CountEvts(take)
    out[#out + 1] = { idx = i, name = tname, start = pos, tc = R.sec_to_tc(pos),
                      length = reaper.GetMediaItemInfo_Value(it, "D_LENGTH"), notes = nn, ccs = cc,
                      midi = reaper.TakeIsMIDI(take) }
  end
  return out
end

-- notes: { {t=sec, dur=sec, pitch=, vel=, chan=0}, ... }   absolute project time
function R.insert_notes(take, notes)
  for _, n in ipairs(notes) do
    local s = reaper.MIDI_GetPPQPosFromProjTime(take, n.t)
    local e = reaper.MIDI_GetPPQPosFromProjTime(take, n.t + n.dur)
    reaper.MIDI_InsertNote(take, false, false, s, e, n.chan or 0, n.pitch, n.vel or 96, true)
  end
  reaper.MIDI_Sort(take)
  return #notes
end

-- same, positioned in quarter notes from project start (follows the tempo map)
function R.insert_notes_qn(take, notes)  -- { {qn=, dur_qn=, pitch=, vel=, chan=} }
  for _, n in ipairs(notes) do
    local s = reaper.MIDI_GetPPQPosFromProjQN(take, n.qn)
    local e = reaper.MIDI_GetPPQPosFromProjQN(take, n.qn + n.dur_qn)
    reaper.MIDI_InsertNote(take, false, false, s, e, n.chan or 0, n.pitch, n.vel or 96, true)
  end
  reaper.MIDI_Sort(take)
  return #notes
end

-- A keyswitch is a short, quiet note just before the phrase it governs.
function R.insert_keyswitch(take, t, pitch, chan, lead)
  lead = lead or 0.05
  local s = reaper.MIDI_GetPPQPosFromProjTime(take, t - lead)
  local e = reaper.MIDI_GetPPQPosFromProjTime(take, t - lead + 0.02)
  reaper.MIDI_InsertNote(take, false, false, s, e, chan or 0, pitch, 1, true)
end

-- CC lane from breakpoints, linearly interpolated: points {{t=sec, v=0..127}, ...}
function R.insert_cc_curve(take, cc, points, step, chan)
  step, chan = step or 0.02, chan or 0
  table.sort(points, function(a, b) return a.t < b.t end)
  local n = 0
  for i = 1, #points - 1 do
    local a, b = points[i], points[i + 1]
    local t = a.t
    while t < b.t do
      local f = (t - a.t) / (b.t - a.t)
      local v = math.floor(a.v + (b.v - a.v) * f + 0.5)
      reaper.MIDI_InsertCC(take, false, false, reaper.MIDI_GetPPQPosFromProjTime(take, t), 0xB0, chan, cc, v)
      t, n = t + step, n + 1
    end
  end
  local last = points[#points]
  reaper.MIDI_InsertCC(take, false, false, reaper.MIDI_GetPPQPosFromProjTime(take, last.t), 0xB0, chan, cc, last.v)
  reaper.MIDI_Sort(take)
  return n + 1
end

function R.notes(take, limit, offset)   -- paginated read-back
  local _, total = reaper.MIDI_CountEvts(take)
  limit, offset = limit or 300, offset or 0
  local out = {}
  for i = offset, math.min(total - 1, offset + limit - 1) do
    local _, _, _, s, e, ch, pitch, vel = reaper.MIDI_GetNote(take, i)
    local ts = reaper.MIDI_GetProjTimeFromPPQPos(take, s)
    out[#out + 1] = { i = i, t = ts, dur = reaper.MIDI_GetProjTimeFromPPQPos(take, e) - ts,
                      pitch = pitch, vel = vel, chan = ch }
  end
  return { total = total, offset = offset, notes = out }
end

function R.ccs(take, cc, limit, offset)  -- cc=nil for all lanes
  local _, _, total = reaper.MIDI_CountEvts(take)
  limit, offset = limit or 300, offset or 0
  local out, seen = {}, 0
  for i = 0, total - 1 do
    local _, _, _, pos, msg, ch, num, val = reaper.MIDI_GetCC(take, i)
    if msg == 0xB0 and (cc == nil or num == cc) then
      if seen >= offset and #out < limit then
        out[#out + 1] = { t = reaper.MIDI_GetProjTimeFromPPQPos(take, pos), cc = num, v = val, chan = ch }
      end
      seen = seen + 1
    end
  end
  return { total = seen, offset = offset, events = out }
end

function R.clear_take(take)
  local _, nn, nc = reaper.MIDI_CountEvts(take)
  for i = nn - 1, 0, -1 do reaper.MIDI_DeleteNote(take, i) end
  for i = nc - 1, 0, -1 do reaper.MIDI_DeleteCC(take, i) end
  reaper.MIDI_Sort(take)
end

-- Write a whole cue in one job. Items start 0.5 s early so keyswitch leads fit.
-- cue = { start=sec, stop=sec, parts = {
--   { track="Vln I", name="M1 phrase A",
--     keyswitches = { {t=, pitch=} },
--     notes = { {t=, dur=, pitch=, vel=} },
--     cc = { {cc=1, points={{t=,v=},...}}, {cc=11, points={...}} } }, ... } }
function R.write_cue(cue)
  local report = {}
  for _, part in ipairs(cue.parts) do
    local tr = R.track_by_name(part.track)
    if not tr then error("no track named '" .. part.track .. "'") end
    local item, take = R.new_midi_item(tr, cue.start - 0.5, cue.stop)
    reaper.GetSetMediaItemTakeInfo_String(take, "P_NAME",
      part.name or (part.track .. " @ " .. R.sec_to_tc(cue.start)), true)
    for _, ks in ipairs(part.keyswitches or {}) do R.insert_keyswitch(take, ks.t, ks.pitch, ks.chan) end
    if part.notes then R.insert_notes(take, part.notes) end
    for _, lane in ipairs(part.cc or {}) do R.insert_cc_curve(take, lane.cc, lane.points, lane.step, lane.chan) end
    local _, nn, nc = reaper.MIDI_CountEvts(take)
    report[#report + 1] = { track = part.track, notes = nn, cc_events = nc }
  end
  return report
end

-- ===== FX ================================================================
function R.fx_params(tr, fxidx)
  local out = {}
  for p = 0, reaper.TrackFX_GetNumParams(tr, fxidx) - 1 do
    local _, name = reaper.TrackFX_GetParamName(tr, fxidx, p, "")
    out[#out + 1] = { p = p, name = name, val = reaper.TrackFX_GetParamNormalized(tr, fxidx, p) }
  end
  return out
end
function R.set_fx_param(tr, fxidx, p, v) return reaper.TrackFX_SetParamNormalized(tr, fxidx, p, v) end

-- ===== render ============================================================
-- bounds: 1 = entire project, 2 = time selection, 3 = all regions, 5 = selected regions
-- what:   0 = master mix, 3 = stems of selected tracks (verify once in File > Render)
function R.render(dir, pattern, bounds, what)
  reaper.GetSetProjectInfo_String(P, "RENDER_FILE", dir, true)
  reaper.GetSetProjectInfo_String(P, "RENDER_PATTERN", pattern or "$project_$region", true)
  reaper.GetSetProjectInfo(P, "RENDER_BOUNDSFLAG", bounds or 3, true)
  reaper.GetSetProjectInfo(P, "RENDER_SETTINGS", what or 0, true)
  reaper.Main_OnCommand(42230, 0) -- File: Render project, using the most recent render settings, auto-close render dialog
  return { dir = dir, pattern = pattern, bounds = bounds, what = what }
end

-- ===== snapshot ==========================================================
function R.snapshot()
  return { project = R.project_info(), tempo = R.tempo_markers(), markers = R.markers(), tracks = R.tracks() }
end

function R.save() reaper.Main_SaveProject(P, false) end

return R
```

Two things to verify once on your machine, then trust: that `R.render` with `what = 3` renders stems the way your render dialog is configured (open File → Render once and look), and that action 42230 exists in your Actions list (search "auto-close render dialog"; the ID has been stable, but confirm).

## 6. Film-scoring workflows

Each workflow is a prompt you give Claude Code plus the shape of the job it should write. Times are absolute project seconds throughout; timecode strings are converted with `R.tc_to_sec`.

### 6.1 Set up a cue from spotting notes

Before anything else, set the project's start timecode and frame rate in Project Settings (Alt+Enter) by hand or by computer use: these are settings dialogs, and there is no clean ReaScript setter for the start offset. Import the picture (Insert → Media file) the same way. Then:

**Prompt:** "Here are the spotting notes for 1M3 (start 01:00:12:08, end 01:01:40:00, 23.976 fps). Hits: 01:00:19:14 door slam, 01:00:33:02 she turns, 01:01:12:20 cut to exterior. Add a region for the cue, markers for the hits, and propose a tempo map that puts the first two hits on downbeats, staying between 72 and 96 bpm. Then show me the tempo markers."

**Job shape:**

```lua
local s, e = R.tc_to_sec("01:00:12:08"), R.tc_to_sec("01:01:40:00")
R.add_region(s, e, "1M3", R.rgb(90, 140, 220))
R.add_hit_points({
  { tc = "01:00:19:14", name = "HIT door slam" },
  { tc = "01:00:33:02", name = "HIT she turns" },
  { tc = "01:01:12:20", name = "HIT cut exterior" },
})
-- tempo so that bar 3 (8 beats in 4/4) lands on the door slam:
local hit1 = R.tc_to_sec("01:00:19:14")
local cands = R.tempi_for_hit(s, hit1, 72, 96)   -- Claude chooses from these
return { cue = { s, e }, candidates = cands }
```

Then a second job sets the chosen tempo: `R.set_tempo_at(s, 84.3, 4, 4)` and, if a second hit needs a different tempo from bar N, `R.set_tempo_at(R.sec_at_qn(qn_of_bar_N), new_bpm)`. Claude should read `R.tempo_markers()` back and report where each hit now falls in bars and beats (`R.sec_to_bar`). This is the "find tempo" arithmetic every scoring DAW does; here Claude does it and shows its work.

### 6.2 Build the orchestral template

**Prompt:** "List installed FX matching 'opus' and 'kontakt'. Then build a template: folders Strings, Brass, Woodwinds, Percussion; tracks Vln I, Vln II, Vla, Vc, Cb under Strings each with one Opus instance; color strings blue, brass gold. Confirm with the track list."

**Job shape:**

```lua
local inst = R.installed_fx("opus")[1] or error("no Opus")
local blue = R.rgb(70, 110, 200)
R.add_track("Strings", { folder = 1, color = blue })
for i, n in ipairs({ "Vln I", "Vln II", "Vla", "Vc", "Cb" }) do
  R.add_track(n, { instrument = inst, color = blue, folder = (i == 5) and -1 or 0 })
end
return R.tracks()
```

Patch loading inside Opus, Kontakt or SINE is not reachable from ReaScript: the plugin's own browser is not exposed as parameters. Load patches once by hand, then save the track as a track template (right-click track → Save tracks as track template), and from then on Claude can insert the finished template with the action "Track: Insert track from template" after writing the template path to the clipboard, or simply duplicate an existing configured track with `reaper.Main_OnCommand(40062, 0)` (Track: Duplicate tracks) after selecting it. One Kontakt or Opus instance per track is the arrangement REAPER handles best.

### 6.3 Write a cue: notes, keyswitches, dynamics

**Prompt:** "Write the first eight bars of 1M3 for Vln I and Vc: a sustained D minor pedal in the celli, violins entering at bar 3 with a rising line, pp swelling to mf by the door slam. Use the Hollywood Strings map in libs/. Put everything in one job and report counts."

**Job shape** (keyswitch pitches come from the library map, never from Claude's memory):

```lua
local M = dofile(BRIDGE_DIR .. "/libs/hollywood_strings.lua")   -- articulation map, see 6.6
local s = R.tc_to_sec("01:00:12:08")
local bar = function(b) return R.sec_at_qn(R.qn_at(s) + (b - 1) * 4) end  -- 4/4 after the tempo map
return R.write_cue({
  start = s, stop = bar(9),
  parts = {
    { track = "Vc", name = "1M3 pedal",
      keyswitches = { { t = bar(1), pitch = M.Vc.sustain } },
      notes = { { t = bar(1), dur = bar(9) - bar(1), pitch = 38, vel = 70 } },
      cc = { { cc = M.cc.dynamics, points = { { t = bar(1), v = 30 }, { t = bar(9), v = 60 } } },
             { cc = M.cc.expression, points = { { t = bar(1), v = 90 }, { t = bar(9), v = 110 } } } } },
    { track = "Vln I", name = "1M3 line",
      keyswitches = { { t = bar(3), pitch = M.VlnI.legato } },
      notes = {
        { t = bar(3), dur = 2.0, pitch = 69, vel = 80 }, { t = bar(3) + 2.0, dur = 2.0, pitch = 72, vel = 82 },
        { t = bar(4), dur = 4.0, pitch = 74, vel = 85 },
      },
      cc = { { cc = M.cc.dynamics, points = { { t = bar(3), v = 25 }, { t = bar(5), v = 55 }, { t = bar(9), v = 85 } } } } },
  },
})
```

Conventions that make this sound acceptable without hearing it: CC1 (dynamics) crossfades layers, CC11 (expression) shapes within a layer; start CC11 slightly after CC1 moves; leave 50 ms of keyswitch lead; velocity still matters for short articulations. Claude can apply those rules. It cannot tell whether the result breathes. You audition and tell it what to change, in bars and beats.

### 6.4 Read back and revise

**Prompt:** "Show me the notes and CC1 in the Vln I item for 1M3, bars 3–5, then raise the peak of the swell by 10 and move it one beat earlier."

Claude finds the take (`R.track_by_name("Vln I")`, `R.items(tr)`), reads `R.notes(take)` and `R.ccs(take, 1)`, clears the CC1 lane (delete by index, or `R.clear_take` and rewrite the part if the item is small), and rewrites the curve. Because items start 0.5 s early and all times are absolute, rewrites are idempotent: the same input produces the same result.

### 6.5 Render stems

**Prompt:** "Render all regions as stems of the selected tracks to ~/Cues/1M3/stems, named `$region_$track`."

```lua
return R.render(os.getenv("HOME") .. "/Cues/1M3/stems", "$region_$track", 3, 3)
```

Run with `rpr run job.lua --timeout 900`. The render blocks REAPER and the CLI until it finishes. If you want loudness numbers back, render, then analyze the files in Python (`pyloudnorm`, `soundfile`) — the measurement loop in §7.

### 6.6 Articulations: the library map

REAPER has no expression-map object. Keyswitches are MIDI notes and CCs are CCs, which is the easy case for scripting: everything is explicit in the item. What you need is a map per library so Claude uses the right pitches. Keep one Lua file per library in `~/.rpr-bridge/libs/`:

```lua
-- libs/hollywood_strings.lua — fill from the Opus patch's keyswitch list; do not let Claude guess these
return {
  instrument = "VST3: Opus (EastWest)",
  cc = { dynamics = 1, expression = 11, vibrato = 21 },
  VlnI = { sustain = 24, legato = 25, staccato = 26, spiccato = 27, tremolo = 28, pizzicato = 29 },
  Vc   = { sustain = 24, legato = 25, staccato = 26, spiccato = 27, tremolo = 28, pizzicato = 29 },
  notes = "KS patches: keyswitch range C0–B0; CC1 crossfades, CC11 is volume-shaping.",
}
```

The pitches above are placeholders. Open the patch in Opus, read its keyswitch assignments, and write them in. Claude can write the file for you from a screenshot of the patch's keyswitch panel (it can read images), and it can draft maps from a library's manual PDF, but you check them: a composer who had Claude generate expression maps reported it "worked very nicely for basic maps" and failed on a library whose dynamics ran on velocity instead of CC11.

If you prefer to switch articulations from the piano roll rather than bake keyswitch notes, Reaticulate (free, Lua, reaticulate.com) reads text `.reabank` files, which Claude can author from the same map. Its last release was February 2024, so treat it as stable-but-dormant; check the bank format on its site before generating files. The baked-keyswitch approach in `R.write_cue` has no such dependency and survives export to any other DAW.

### 6.7 The other path: compile MIDI outside, import inside

Everything above writes into REAPER live. The alternative is to have Claude generate a Standard MIDI File with Python (`mido` or `symusic`; a Type-1 file with a conductor track carrying tempo, meter and markers, and instrument tracks carrying notes, keyswitches and CC curves) and import it:

```lua
reaper.SetEditCurPos(R.tc_to_sec("01:00:12:08"), false, false)
reaper.InsertMedia("/path/to/1M3_vln1.mid", 1)   -- 1 = add on a new track
```

Set Preferences → Media → MIDI → "Import tempo/time signature from MIDI files" to your preference first, or the import raises a dialog (which the bridge will auto-answer, possibly not the way you want). This path is slower per iteration but portable: the same SMF plays in Cubase, Logic or Digital Performer, and it is the only way to carry a cue into a DAW with no scripting API. If you already have an LLM-to-MIDI tool, this is where it plugs in; the live bridge is for everything the SMF cannot express (track setup, FX, regions, render) and for fast revision.

## 7. What Claude cannot do here

- **Hear.** Claude's inputs are text and images; its output is text. No current Claude model accepts audio. The only evaluation loop is render → measure → adjust, where the measurement is LUFS, true peak, a spectrogram image, or note/CC statistics. That addresses balance and obvious errors (a keyswitch landing late, a CC lane that never moves), not phrasing. The practitioners who have run this loop in 2026 describe output that is rhythmically correct and musically flat until a human adjusts it by ear. Budget your time accordingly: Claude for setup, maps, tempo arithmetic, batch edits and first drafts; you for every bar that has to be musical.
- **See REAPER's screen** unless you turn on computer use, which is slow and coordinate-error-prone; reserve it for the settings dialogs in §6.1.
- **Load patches** inside Opus, Kontakt or SINE (§6.2).
- **Read the video.** Spotting is yours; Claude works from your timecodes.
- **Transcribe a scanned score** reliably. It reads images, but a 2026 attempt to convert a PDF part to MIDI got the rhythm and lost the pitches.

## 8. Safety

- **Undo.** Every job is one undo step, including failed ones. Ctrl+Z reverses a bad job completely.
- **Save first.** Have Claude call `R.save()` (or you press Ctrl+S) before any job that touches the tempo map or deletes markers; and turn on Preferences → Project → "Save project backups" so you have timestamped copies.
- **Injection surface.** The inbox executes whatever Lua it receives, and Opus 5.5's system card notes it is more likely than its predecessor to follow instructions hidden in pasted text. Keep `~/.rpr-bridge` on the local disk, not in a synced folder; do not point the CLI at a shared folder on an untrusted network; and when Claude reads files you did not write (a library manual, a downloaded template, a forum post), tell it those are data, not instructions.
- **Dry runs.** For destructive scripts, have Claude add a `DRY = true` flag that computes and returns what it would do without calling the write functions, then flip it.
- **Review the job.** The job file is small. Read it before running anything that loops over all tracks or all items.

## 9. Variants

- **Claude on Linux, REAPER on Windows/macOS.** Point `BRIDGE` in the Lua runner and `RPR_BRIDGE` for the CLI at the same SMB or NFS share. Round trips go to a few hundred milliseconds, which does not matter for scripted edits. The share must be writable by both sides and must not be cloud-synced.
- **Python instead of Lua for jobs.** Not recommended. REAPER's Python needs a matching interpreter configured in Preferences, has the same function set, and gains nothing here. Keep Python outside (the CLI, SMF generation, audio measurement) and Lua inside.
- **Multiple REAPER instances.** Give each its own bridge folder via the `BRIDGE` constant and `RPR_BRIDGE`.
- **Claude Code hooks.** A `PostToolUse` hook on Bash that greps for `rpr run` can automatically run `rpr snapshot` afterward and append it to the transcript, so Claude always sees the post-state without asking.

## 10. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `bridge not running: no recent heartbeat` | Runner not loaded, or REAPER busy | Check `__startup.lua`; run `claude_bridge.lua` from the Actions list; look for a modal dialog in REAPER |
| Timeout on a job that should be quick | A modal dialog not covered by the stubs, or a script stuck in a loop | Dismiss the dialog; add the function to `STUBS`; Ctrl+Z |
| `lib: false` in the smoke test | Syntax error in `rpr.lua` | The result's `log` has the Lua error |
| Notes land at the wrong time | Times given in seconds-from-cue instead of absolute project seconds; or item created after notes | Use `R.tc_to_sec` and absolute times; create the item before inserting |
| Keyswitches have no effect | Pitch wrong for the patch; keyswitch before item start; KS channel wrong | Check the library map; items start 0.5 s early in `R.write_cue`; check the patch's MIDI channel |
| `attempt to call a nil value (field 'X')` | Function name or signature differs in your build | `rpr api X`; fix the call |
| Tempo marker ignored | Marker already exists at that time with other values | `R.tempo_markers()`, then `R.set_tempo_at` updates the existing one (it matches within 0.1 ms) |
| UI freezes for seconds | Job too large | Split by track or section; keep CC `step` at 0.02 s or coarser |
| Render returns before files appear | Render ran asynchronously in your configuration | Raise `--timeout`; poll the output folder from Python |
| Result JSON truncated in Claude Code | Over the 25K-token MCP/output limit | Paginate with `limit`/`offset` in `R.notes`/`R.ccs`; use `rpr snapshot` rather than dumping items |

## 11. Appendix: ReaScript functions this guide uses

Confirm any of these with `rpr api <name>`; the list is the contract between the helper library and REAPER.

Time: `parse_timestr_pos(buf, mode)` and `format_timestr_pos(tpos, buf, mode)` (mode 2 = measures.beats, 5 = h:m:s:f), `TimeMap2_timeToQN`, `TimeMap2_QNToTime`, `TimeMap_curFrameRate`, `GetProjectTimeOffset`, `GetProjectLength`, `TimeMap_GetDividedBpmAtTime`.
Tempo: `CountTempoTimeSigMarkers`, `GetTempoTimeSigMarker`, `SetTempoTimeSigMarker(proj, ptidx(-1=new), timepos, measurepos(-1), beatpos(-1), bpm, num(0=keep), den(0=keep), linear)`, `DeleteTempoTimeSigMarker`, `UpdateTimeline`.
Markers: `AddProjectMarker2`, `EnumProjectMarkers3`, `CountProjectMarkers`, `DeleteProjectMarkerByIndex`, `ColorToNative`.
Tracks: `CountTracks`, `GetTrack`, `GetTrackName`, `InsertTrackAtIndex`, `GetSetMediaTrackInfo_String`, `Get/SetMediaTrackInfo_Value` (`I_FOLDERDEPTH`, `I_CUSTOMCOLOR`, `I_RECINPUT`, `I_RECMON`, `B_MUTE`, `D_VOL`), `TrackList_AdjustWindows`.
FX: `EnumInstalledFX`, `TrackFX_AddByName(track, name, recFX, instantiate(-1=new))`, `TrackFX_GetCount`, `TrackFX_GetFXName`, `TrackFX_GetNumParams`, `TrackFX_GetParamName`, `TrackFX_Get/SetParamNormalized`.
MIDI: `CreateNewMIDIItemInProj`, `GetActiveTake`, `TakeIsMIDI`, `MIDI_InsertNote(take, sel, muted, startppq, endppq, chan, pitch, vel, noSort)`, `MIDI_InsertCC(take, sel, muted, ppq, chanmsg(0xB0), chan, msg2, msg3)`, `MIDI_GetNote`, `MIDI_GetCC`, `MIDI_CountEvts`, `MIDI_DeleteNote`, `MIDI_DeleteCC`, `MIDI_Sort`, `MIDI_GetPPQPosFromProjTime`, `MIDI_GetPPQPosFromProjQN`, `MIDI_GetProjTimeFromPPQPos`, `GetSetMediaItemTakeInfo_String`, `GetMediaItemInfo_Value`, `CountTrackMediaItems`, `GetTrackMediaItem`.
Project/render: `GetSetProjectInfo` (`RENDER_BOUNDSFLAG`, `RENDER_SETTINGS`, `PROJECT_SRATE`), `GetSetProjectInfo_String` (`RENDER_FILE`, `RENDER_PATTERN`), `Main_OnCommand(42230)`, `Main_SaveProject`, `InsertMedia`, `SetEditCurPos`.
Runtime: `defer`, `time_precise`, `EnumerateFiles(path, -1 to refresh)`, `file_exists`, `RecursiveCreateDirectory`, `GetResourcePath`, `Undo_BeginBlock2`/`Undo_EndBlock2`, `PreventUIRefresh`, `UpdateArrange`, `ShowConsoleMsg`.

Sources behind the claims in this guide: the ReaScript API reference generated by REAPER 7.82; the REAPER 7.53–7.82 changelog for the 2026 video and timecode changes; the Claude Code MCP documentation for the output limit and `claude mcp add` syntax; the Claude Opus 5.5 model page and system card for modality and the injection note; the Reaticulate changelog for its release status; and the 2026 practitioner reports collected in the companion research report "Best DAW for Claude film scoring".

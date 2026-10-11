"""Save the open REAPER project, render master + every track stem for cycle N, measure it, and make an MP3.

Usage: python render_cycle.py <N>
Output: cycles/cNN/render/00_Master.wav + NN_<track>.wav, cycles/cNN/metrics/metrics.md (+ json, png),
        cycles/cNN/mvt2-mockup-cNN.mp3. Takes about 5-6 minutes; REAPER is blocked while it renders.
"""
import os, subprocess, sys
N = int(sys.argv[1])
ROOT = "/Users/gooby/sandbox/claude_composes/symphony/mvt2/reaper"
C = f"{ROOT}/cycles/c{N:02d}"
os.makedirs(f"{C}/render", exist_ok=True)
PY = os.path.expanduser("~/.venvs/claude-composes-reaper/bin/python")
RPR = ["python3", os.path.expanduser("~/.rpr-bridge/rpr.py")]
# Opus streams samples in after a patch loads; wait until REAPER's memory stops growing before rendering
import time
def rss():
    pid = subprocess.run(["pgrep", "-x", "REAPER"], capture_output=True, text=True).stdout.split()[0]
    return int(subprocess.run(["ps", "-o", "rss=", "-p", pid], capture_output=True, text=True).stdout)
# c02: one quiet 10 s reading was not enough after a full rebuild (the first c02 render still had 83 late entries,
# the same project rendered again later 26); require three quiet readings in a row
prev, t0, quiet = rss(), time.time(), 0
while time.time() - t0 < 1500 and quiet < 3:
    time.sleep(10)
    cur = rss()
    quiet = quiet + 1 if abs(cur - prev) < 50_000 else 0
    prev = cur
job = f"{C}/render.lua"
open(job, "w").write(f"""
reaper.Main_SaveProject(0, false)
local dir = "{C}/render"
local endt = reaper.TimeMap2_QNToTime(0, 304.0) + 8
for i = 0, reaper.CountTracks(0) - 1 do reaper.SetTrackSelected(reaper.GetTrack(0, i), true) end
reaper.GetSet_LoopTimeRange(true, false, 0, endt, false)
reaper.GetSetProjectInfo(0, "RENDER_SRATE", 48000, true)
reaper.GetSetProjectInfo(0, "RENDER_CHANNELS", 2, true)
reaper.GetSetProjectInfo_String(0, "RENDER_FILE", dir, true)
reaper.GetSetProjectInfo_String(0, "RENDER_PATTERN", "$tracknumber_$track", true)
reaper.GetSetProjectInfo(0, "RENDER_BOUNDSFLAG", 2, true)
reaper.GetSetProjectInfo(0, "RENDER_SETTINGS", 1, true)   -- master mix + stems of selected tracks
reaper.Main_OnCommand(42230, 0)
for i = 0, reaper.CountTracks(0) - 1 do reaper.SetTrackSelected(reaper.GetTrack(0, i), false) end
return {{ dir = dir, end_sec = endt }}
""")
r = subprocess.run(RPR + ["run", job, "--timeout", "1800"], capture_output=True, text=True)
if r.returncode:
    sys.exit("render failed: " + r.stderr + r.stdout)
# c01: full-speed offline renders start notes up to 0.6 s late (Opus cannot stream the samples in time from the
# external drive); the project must render at 1x offline (RPP line "RENDER_1X 1", set by editing the .rpp and reopening).
if "RENDER_1X 1" not in open(f"{ROOT}/mvt2-v77-mockup.rpp", encoding="utf-8", errors="replace").read():
    print("WARNING: project is not set to 1x offline render (RENDER_1X 1); expect late note starts", file=sys.stderr)
master = f"{C}/render/00_Master.wav"
if not os.path.exists(master):
    sys.exit("no 00_Master.wav rendered")
subprocess.run([PY, f"{ROOT}/tools/measure.py", f"{C}/render", f"{ROOT}/build/parts.json", f"{C}/metrics"], check=True)
# c05 (A #1): attack-timing gate. 10 isolated attacks and 4 tremolo arrivals; c03 passed all 14, c04 failed 11. If it
# fails, the render's string timing is not trustworthy (sample streaming fell behind): render again before judging.
pr = subprocess.run([PY, f"{ROOT}/tools/probe_attacks.py", f"{C}/render", f"{ROOT}/build/parts.json"], capture_output=True, text=True)
open(f"{C}/metrics/attacks.txt", "w").write(pr.stdout + pr.stderr)
print(pr.stdout.strip().splitlines()[-1] if pr.stdout.strip() else "probe: no output")
if pr.returncode:
    print("WARNING: attack probe failed (see metrics/attacks.txt)", file=sys.stderr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", master, "-af", "volume=5dB,alimiter=limit=0.89:level=false",
                "-b:a", "192k", f"{C}/mvt2-mockup-c{N:02d}.mp3"], check=True)
print(f"{C}/metrics/metrics.md")
print(f"{C}/mvt2-mockup-c{N:02d}.mp3")

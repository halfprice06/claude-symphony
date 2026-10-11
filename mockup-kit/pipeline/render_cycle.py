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
# c07 (critic C #1a): refuse to render while macOS holds much of REAPER's memory compressed (c06: 42 of 57 GB
# compressed -> every entry 0.2-0.3 s late). Restart REAPER (save, quit, reopen the project) to clear it.
import re, time
MAX_CMPRS_GB = 6.0
def cmprs_gb():
    out = subprocess.run(["top", "-l", "1", "-stats", "pid,command,mem,cmprs"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        f = line.split()
        if len(f) >= 4 and f[1] == "REAPER":
            m = re.match(r"([\d.]+)([KMGB])", f[3])
            if m:
                return float(m.group(1)) * {"K": 1e-6, "M": 1e-3, "G": 1.0, "B": 1e-9}[m.group(2)], f[2]
    return None, None
cg, mem = cmprs_gb()
print(f"REAPER memory {mem}, compressed {cg} GB", flush=True)
if cg is not None and cg > MAX_CMPRS_GB and "--force" not in sys.argv:
    sys.exit(f"REAPER has {cg:.1f} GB compressed (limit {MAX_CMPRS_GB}); restart REAPER before rendering, or pass --force")
# Opus streams samples in after a patch loads; wait until REAPER's memory stops growing before rendering
def rss():
    pid = subprocess.run(["pgrep", "-x", "REAPER"], capture_output=True, text=True).stdout.split()[0]
    return int(subprocess.run(["ps", "-o", "rss=", "-p", pid], capture_output=True, text=True).stdout)
# c02: one quiet 10 s reading was not enough after a full rebuild (the first c02 render still had 83 late entries,
# the same project rendered again later 26); require three quiet readings in a row
prev, t0, quiet = rss(), time.time(), 0
# c08: after the Mac's reset the first reload grew only about 1 GB per minute (cold drive cache), so the old 1500 s cap
# would have rendered half-loaded patches; wait up to 45 minutes and refuse to render if memory is still growing
WAIT_CAP_S = 2700
while time.time() - t0 < WAIT_CAP_S and quiet < 3:
    time.sleep(10)
    cur = rss()
    quiet = quiet + 1 if abs(cur - prev) < 50_000 else 0
    prev = cur
if quiet < 3 and "--force" not in sys.argv:
    sys.exit(f"REAPER memory still growing after {WAIT_CAP_S} s (samples still loading); rerun later, or pass --force")
import json, glob
PARTS = json.load(open(f"{ROOT}/build/parts.json"))
PRE = PARTS.get("preroll_qn", 0.0)   # c06 (A #1): silent pre-roll before score qn 0, cut off after the render
job = f"{C}/render.lua"
open(job, "w").write(f"""
reaper.Main_SaveProject(0, false)
local dir = "{C}/render"
local endt = reaper.TimeMap2_QNToTime(0, {304.0 + PRE}) + 8
local pre_sec = reaper.TimeMap2_QNToTime(0, {PRE})
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
return {{ dir = dir, end_sec = endt, pre_sec = pre_sec }}
""")
r = subprocess.run(RPR + ["run", job, "--timeout", "1800"], capture_output=True, text=True)
if r.returncode:
    sys.exit("render failed: " + r.stderr + r.stdout)
# c01: full-speed offline renders start notes up to 0.6 s late (Opus cannot stream the samples in time from the
# external drive); the project must render at 1x offline (RPP line "RENDER_1X 1", set by editing the .rpp and reopening).
if "RENDER_1X 1" not in open(f"{ROOT}/mvt2-v77-mockup.rpp", encoding="utf-8", errors="replace").read():
    print("WARNING: project is not set to 1x offline render (RENDER_1X 1); expect late note starts", file=sys.stderr)
master = f"{C}/render/00_Master.wav"
# Delivery master (Dan, 2026-10-11: soft passages too quiet at a volume where the loud ones are uncomfortable).
# Slow, gentle compression lifts the soft passages, then loudnorm brings the result to -18 LUFS with LRA about 11 LU
# and -1.5 dBTP. The stems and 00_Master.wav stay unprocessed; only the mp3 gets this chain.
MASTER_CHAIN = "acompressor=threshold=-36dB:ratio=2.5:attack=80:release=1200:makeup=1,loudnorm=I=-18:LRA=11:TP=-1.5"
if not os.path.exists(master):
    sys.exit("no 00_Master.wav rendered")
# c06: cut the pre-roll (sample-exact, from REAPER's own time of qn PRE) off the master and every stem
pre_sec = json.loads(r.stdout).get("pre_sec", 0.0) if r.stdout.strip() else 0.0
if PRE:
    trim = subprocess.run([PY, "-c", f"""
import glob, soundfile as sf
cut = None
for f in sorted(glob.glob({C + '/render/*.wav'!r})):
    info = sf.info(f); x, sr = sf.read(f, dtype='float32', always_2d=True)
    n = int(round({pre_sec} * sr)); cut = n
    tail = x[:n]
    sf.write(f, x[n:], sr, subtype=info.subtype)
    if abs(tail).max() > 10 ** (-40 / 20): print('pre-roll not silent:', f, float(abs(tail).max()))   # c07: qn-0 string leads start in the pre-roll (about -53 dBFS)
print('cut', cut, 'samples')
"""], capture_output=True, text=True)
    print(trim.stdout.strip(), trim.stderr.strip()[-500:])
    if trim.returncode:
        sys.exit("pre-roll trim failed")
subprocess.run([PY, f"{ROOT}/tools/measure.py", f"{C}/render", f"{ROOT}/build/parts.json", f"{C}/metrics"], check=True)
cg2, mem2 = cmprs_gb()
open(f"{C}/metrics/memory.txt", "w").write(f"before render: REAPER {mem}, compressed {cg} GB\nafter render: REAPER {mem2}, compressed {cg2} GB\n")
# c05 (A #1): attack-timing gate. 10 isolated attacks and 4 tremolo arrivals; c03 passed all 14, c04 failed 11. If it
# fails, the render's string timing is not trustworthy (sample streaming fell behind): render again before judging.
pr = subprocess.run([PY, f"{ROOT}/tools/probe_attacks.py", f"{C}/render", f"{ROOT}/build/parts.json"], capture_output=True, text=True)
open(f"{C}/metrics/attacks.txt", "w").write(pr.stdout + pr.stderr)
print(pr.stdout.strip().splitlines()[-1] if pr.stdout.strip() else "probe: no output")
if pr.returncode:
    print("WARNING: attack probe failed (see metrics/attacks.txt)", file=sys.stderr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", master, "-af", MASTER_CHAIN,
                "-b:a", "192k", f"{C}/mvt2-mockup-c{N:02d}.mp3"], check=True)
print(f"{C}/metrics/metrics.md")
mp3 = f"{C}/mvt2-mockup-c{N:02d}.mp3"
out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp3, "-af", "ebur128=peak=true", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
summary = " ".join(l.strip() for l in out.splitlines() if l.strip().startswith(("I:", "LRA:", "Peak:")))
open(f"{C}/metrics/metrics.md", "a").write(f"\n## Delivered mp3 (after the delivery master chain)\n\n{summary}\n")
print(mp3)

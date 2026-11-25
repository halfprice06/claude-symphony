"""Save the open REAPER project, render master + every track stem for cycle N, measure it, and make an MP3.

Usage: python render_cycle.py <N> [--measure-only] [--force-memory] [--force] [--force-stale]
Output: cycles/cNN/render/00_Master.wav + NN_<track>.wav, cycles/cNN/metrics/metrics.md (+ json, png),
        cycles/cNN/<title>-cNN.mp3 (title from parts.json, set in build/score_config.py). Takes about 5-6 minutes; REAPER is blocked while it renders.
"""
import os, subprocess, sys
N = int(sys.argv[1])
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the work folder (tools/ is inside it)
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
# mvt1 c01: --measure-only re-runs the measurements, the attack probe and the delivery on the files already in
# cycles/cNN/render (after a level-only stem fix, tools/stem_fix.py); no render, metrics/memory.txt is kept
MEASURE_ONLY = "--measure-only" in sys.argv
cg, mem = cmprs_gb() if not MEASURE_ONLY else (None, None)
print(f"REAPER memory {mem}, compressed {cg} GB", flush=True)
# mvt1 c36: --force-memory overrides only this gate (the audio-device check below still applies). A fresh open that
# streams about 45 GB of samples can leave REAPER's idle sample memory compressed by macOS (c36: 20 of 45 GB after a
# settled open; kit LEARNINGS 11: fresh sessions rendered on time with 31-37 GB compressed); the attack probe judges it
if cg is not None and cg > MAX_CMPRS_GB and "--force" not in sys.argv and "--force-memory" not in sys.argv:
    sys.exit(f"REAPER has {cg:.1f} GB compressed (limit {MAX_CMPRS_GB}); restart REAPER before rendering, or pass "
             "--force-memory (memory gate only) or --force")
# Opus streams samples in after a patch loads; wait until REAPER's memory stops growing before rendering
def rss():
    pid = subprocess.run(["pgrep", "-x", "REAPER"], capture_output=True, text=True).stdout.split()[0]
    return int(subprocess.run(["ps", "-o", "rss=", "-p", pid], capture_output=True, text=True).stdout)
# c02: one quiet 10 s reading was not enough after a full rebuild (the first c02 render still had 83 late entries,
# the same project rendered again later 26); require three quiet readings in a row
prev, t0, quiet = (rss(), time.time(), 0) if not MEASURE_ONLY else (0, time.time(), 3)
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
# mvt1 c34 (critic C #1): the audio device REAPER has open is part of the render conditions. c33 rendered after REAPER
# had opened a Bluetooth headset's microphone (HFP, 24 kHz only) as the default input; the 48 kHz request failed, the
# device dropped out ("Could not find default device", system log) and every Opus instance's output then differed from
# the c32 render of the same data by a component 256 samples (5.3 ms) later: comb-like changes below about 300 Hz (low
# instruments -2..-4 dB at 20-100 Hz, horns +3 dB at 100-250 Hz), with the saved project identical on those tracks.
# Record the device with every render and refuse to render unless it matches the series' renders (48000 Hz, 512-sample
# blocks, no input device); --force overrides.
AUDIO_EXPECT = {"SRATE": "48000", "BSIZE": "512"}
audio = {}
if not MEASURE_ONLY:
    aj = f"{C}/audio_device.lua"
    open(aj, "w").write('local r = {}\nfor _, k in ipairs({"IDENT_IN", "IDENT_OUT", "SRATE", "BSIZE", "MODE"}) do '
                        'local ok, v = reaper.GetAudioDeviceInfo(k, "") r[k] = ok and v or "" end\n'
                        'r.running = reaper.Audio_IsRunning()\nreturn r\n')
    ar = subprocess.run(RPR + ["run", aj, "--timeout", "60"], capture_output=True, text=True)
    try:
        audio = json.loads(ar.stdout)
    except ValueError:
        audio = {"error": (ar.stdout + ar.stderr).strip()[-300:]}
    print("audio device:", audio, flush=True)
    bad = [f"{k} {audio.get(k)!r} (expected {v})" for k, v in AUDIO_EXPECT.items() if str(audio.get(k)) != v]
    if str(audio.get("IDENT_IN", "")).replace("CoreAudio", "").strip():
        bad.append(f"input device {audio.get('IDENT_IN')!r} open (expected none; a Bluetooth headset's microphone "
                   "forces it into 24 kHz HFP mode)")
    if not audio.get("running"):
        bad.append("audio device not running")
    if bad and "--force" not in sys.argv:
        sys.exit("audio device differs from the series' renders: " + "; ".join(bad) +
                 ". Disconnect the headset or set REAPER's input device to none, restart REAPER (reaper_ctl.py restart), "
                 "then render; or pass --force")
PARTS = json.load(open(f"{ROOT}/build/parts.json"))
PRE = PARTS.get("preroll_qn", 0.0)   # c06 (A #1): silent pre-roll before score qn 0, cut off after the render
job = f"{C}/render.lua"
open(job, "w").write(f"""
reaper.Main_SaveProject(0, false)
local dir = "{C}/render"
local endt = reaper.TimeMap2_QNToTime(0, {PARTS.get("score_end", PARTS["end_qn"]) + PRE}) + 8
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
if not MEASURE_ONLY and "--force-stale" not in sys.argv:
    # c50 (ONE_TIME; mvt1 c52): refuse to render a saved project whose Opus states are not the written ones (legato
    # AHDSR attacks saved at 20 ms after playback; tools/state_guard.py). The project on disk is the one REAPER loaded
    # at the restart; fix with build_reaper.py --midi-only (it rebuilds stale tracks) or a full build of the track
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import state_guard as _sg
    _rpp = sorted(glob.glob(f"{ROOT}/*.rpp"))
    _st = _sg.stale_tracks(_rpp[0], PARTS, f"{ROOT}/jobs") if _rpp else set()
    print(f"state_guard: stale {sorted(_st) or 'none'}", flush=True)
    if _st:
        sys.exit(f"saved Opus state is stale on {sorted(_st)}: rebuild them fully (build_reaper.py build/parts.json jobs "
                 f"\"<track>\"), restart, then render; or pass --force-stale")
if not MEASURE_ONLY:
    r = subprocess.run(RPR + ["run", job, "--timeout", "1800"], capture_output=True, text=True)
    if r.returncode:
        sys.exit("render failed: " + r.stderr + r.stdout)
# c01: full-speed offline renders start notes up to 0.6 s late (Opus cannot stream the samples in time from the
# external drive); the project must render at 1x offline (RPP line "RENDER_1X 1", set by editing the .rpp and reopening).
RPP = sorted(glob.glob(f"{ROOT}/*.rpp"))
if not RPP or "RENDER_1X 1" not in open(RPP[0], encoding="utf-8", errors="replace").read():
    print("WARNING: project is not set to 1x offline render (RENDER_1X 1); expect late note starts", file=sys.stderr)
master = f"{C}/render/00_Master.wav"
# Delivery master (Dan, 2026-10-11: soft passages too quiet at a volume where the loud ones are uncomfortable):
# tools/deliver_master.py (look-ahead gain ride on quiet passages, -19 LUFS, -1.5 dBTP; loop/DYNAMICS-RESEARCH.md).
# The stems and 00_Master.wav stay unprocessed; only the mp3 is mastered.
if not os.path.exists(master):
    sys.exit("no 00_Master.wav rendered")
# c06: cut the pre-roll (sample-exact, from REAPER's own time of qn PRE) off the master and every stem
pre_sec = (json.loads(r.stdout).get("pre_sec", 0.0) if r.stdout.strip() else 0.0) if not MEASURE_ONLY else 0.0
if PRE and not MEASURE_ONLY:
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
# mvt2 c44 (EW template mix): returns listed in mix.json "test_returns" (e.g. "R Duc", the Duc-hall fallback fed in
# parallel) are rendered as stems but are not part of the mix: their stems go to cycles/cNN/test_stems/ and
# 00_Master.wav is rebuilt as the float sum of the remaining stems (REAPER's own master, which held the test return too,
# is kept there as 00_Master_reaper.wav)
_mixj = json.load(open(f"{ROOT}/build/mix.json"))
_tests = set(_mixj.get("test_returns") or [])
if _tests and not MEASURE_ONLY:
    tr_ = subprocess.run([PY, "-c", f"""
import glob, os, shutil, soundfile as sf, numpy as np
C = {C!r}; tests = {sorted(_tests)!r}
os.makedirs(C + '/test_stems', exist_ok=True)
moved = []
for f in sorted(glob.glob(C + '/render/[0-9][0-9]_*.wav')):
    if os.path.basename(f)[3:-4] in tests:
        shutil.move(f, C + '/test_stems/' + os.path.basename(f)); moved.append(os.path.basename(f))
if moved:
    shutil.move(C + '/render/00_Master.wav', C + '/test_stems/00_Master_reaper.wav')
    st = [f for f in sorted(glob.glob(C + '/render/[0-9][0-9]_*.wav')) if not f.endswith('00_Master.wav')]
    s, sr = None, None
    for f in st:
        x, sr = sf.read(f, dtype='float64'); s = x if s is None else s + x
    sf.write(C + '/render/00_Master.wav', s.astype('float32'), sr, subtype='FLOAT')
print('test returns moved to test_stems:', moved, '; master = float sum of', len(st) if moved else 0, 'stems')
"""], capture_output=True, text=True)
    print(tr_.stdout.strip(), tr_.stderr.strip()[-500:])
    if tr_.returncode:
        sys.exit("test-return split failed")
# mvt1 c00: the 24-bit master clipped (stem sum peak 1.11, 45 samples at full scale). The master has no FX, so it equals
# the stem sum (LEARNINGS section 15): when it reaches full scale, replace it with the stem sum written as 32-bit float
fix = subprocess.run([PY, "-c", f"""
import glob, soundfile as sf, numpy as np
m, sr = sf.read({master!r}, dtype='float64')
if np.abs(m).max() >= 0.9999:
    st = [f for f in sorted(glob.glob({C + '/render/[0-9][0-9]_*.wav'!r})) if not f.endswith('00_Master.wav')]
    s = sum(sf.read(f, dtype='float64')[0] for f in st)
    sf.write({master!r}, s.astype('float32'), sr, subtype='FLOAT')
    print('master clipped: replaced by the float stem sum, peak', round(float(np.abs(s).max()), 4))
"""], capture_output=True, text=True)
print(fix.stdout.strip(), fix.stderr.strip()[-300:])
subprocess.run([PY, f"{ROOT}/tools/measure.py", f"{C}/render", f"{ROOT}/build/parts.json", f"{C}/metrics"], check=True)
if not MEASURE_ONLY:
    cg2, mem2 = cmprs_gb()
    open(f"{C}/metrics/memory.txt", "w").write(f"before render: REAPER {mem}, compressed {cg} GB\nafter render: REAPER {mem2}, compressed {cg2} GB\n"
                                              f"audio device at render: {json.dumps(audio)}\n")
# c05 (A #1): attack-timing gate. 10 isolated attacks and 4 tremolo arrivals; c03 passed all 14, c04 failed 11. If it
# fails, the render's string timing is not trustworthy (sample streaming fell behind): render again before judging.
pr = subprocess.run([PY, f"{ROOT}/tools/probe_attacks.py", f"{C}/render", f"{ROOT}/build/parts.json"], capture_output=True, text=True)
open(f"{C}/metrics/attacks.txt", "w").write(pr.stdout + pr.stderr)
print(pr.stdout.strip().splitlines()[-1] if pr.stdout.strip() else "probe: no output")
if pr.returncode:
    print("WARNING: attack probe failed (see metrics/attacks.txt)", file=sys.stderr)
mp3 = f"{C}/{PARTS.get('title', 'mockup')}-c{N:02d}.mp3"
dm = subprocess.run([PY, f"{ROOT}/tools/deliver_master.py", master, mp3], capture_output=True, text=True)
if dm.returncode:
    sys.exit("delivery master failed: " + dm.stderr[-800:])
open(f"{C}/metrics/metrics.md", "a").write(f"\n## Delivered mp3 (tools/deliver_master.py)\n\n{dm.stdout.strip()}\n")
# c24 (C #3): phrase-scale loudness motion of the master and the mp3 (tools/motion.py)
mo = subprocess.run([PY, f"{ROOT}/tools/motion.py", master, mp3], capture_output=True, text=True)
open(f"{C}/metrics/metrics.md", "a").write(f"\n## Loudness motion (tools/motion.py)\n\n{mo.stdout.strip()}\n")
print(f"{C}/metrics/metrics.md")
print(mp3)

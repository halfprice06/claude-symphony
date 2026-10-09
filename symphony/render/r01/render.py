#!/usr/bin/env python3
"""r01: rebuild out.mp3 from the final score (mvt1/v120) with one command.

Usage: python3 render.py [--v120 DIR] [--work /tmp/render-01/build] [--jobs 4] [--events EVENTS.tsv]

Steps
 1. copy v120/score.midi (LilyPond output after fixmidi.py) to the work folder;
 2. lib/score_events.py: compile a scratch copy of the v120 LilyPond source with an event-logging engraver and
    list every printed note with its articulations, slur position, technique and dynamic (notes.csv);
 3. articulate.py: write r01.midi (articulation lengths and channels, CC11 dynamics, CC20 dynamic curve);
    a copy is kept next to this script for the critic;
 4. split r01.midi into one MIDI per staff (same grouping as tools/stems.py) and render each with stem.py
    (FluidSynth float, gain, brightness, pan, Detmold Konzerthaus room) in parallel;
 5. sum the stems, gain to the target integrated loudness (linear, no dynamic compression), true-peak
    limiter only if the true peak would exceed the ceiling, encode MP3.
"""
import argparse, json, os, re, shutil, subprocess, sys, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import soundfile as sf
import mido

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


def split_stems(midi, outdir):
    m = mido.MidiFile(midi)
    groups = defaultdict(list)
    for i, tr in enumerate(m.tracks[1:], 1):
        if any(not x.is_meta for x in tr) and any(x.type == "note_on" for x in tr):
            groups[key(tr.name)].append(i)
    paths = {}
    for g, idx in groups.items():
        n = mido.MidiFile(type=1, ticks_per_beat=m.ticks_per_beat)
        n.tracks.append(m.tracks[0])
        for i in idx:
            n.tracks.append(m.tracks[i])
        p = os.path.join(outdir, re.sub(r"\W+", "_", g) + ".mid")
        n.save(p); paths[g] = p
    return paths


def ebur128(path):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    s = r[r.rfind("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", s).group(1))
    LRA = float(re.search(r"LRA:\s+(-?[\d.]+) LU", s).group(1))
    TP = float(re.search(r"Peak:\s+(-?[\d.inf]+) dBFS", s).group(1))
    return I, LRA, TP


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v120", default=os.path.normpath(os.path.join(HERE, "..", "..", "mvt1", "v120")))
    ap.add_argument("--work", default="/tmp/render-01/build")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--events", help="reuse an events.tsv from an earlier run (skips the 30 s LilyPond compile)")
    ap.add_argument("--out", default=os.path.join(HERE, "out.mp3"))
    a = ap.parse_args()
    t_start = time.time()
    cfg = json.load(open(os.path.join(HERE, "config.json")))
    W = a.work; os.makedirs(W, exist_ok=True)
    stems_dir = os.path.join(W, "stems"); os.makedirs(stems_dir, exist_ok=True)
    src_midi = os.path.join(W, "v120.midi")
    shutil.copy(os.path.join(a.v120, "score.midi"), src_midi)
    # 2. printed events
    notes = os.path.join(W, "notes_v120.csv")
    cmd = [sys.executable, os.path.join(HERE, "lib", "score_events.py"), "--midi", src_midi, "--out", notes,
           "--ly-dir", a.v120, "--scratch", os.path.join(W, "ly_scratch"), "--summary", os.path.join(W, "articulation_midi_v120.json")]
    if a.events:
        cmd += ["--events", a.events]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    print(f"[{time.time()-t_start:5.1f}s] score events -> {notes}", flush=True)
    # 3. rendering MIDI
    r01_midi = os.path.join(W, "r01.midi")
    subprocess.run([sys.executable, os.path.join(HERE, "articulate.py"), src_midi, notes, os.path.join(HERE, "config.json"),
                    r01_midi, "--report", os.path.join(W, "articulate_report.json")], check=True)
    shutil.copy(r01_midi, os.path.join(HERE, "r01.midi"))
    print(f"[{time.time()-t_start:5.1f}s] articulated MIDI -> {r01_midi}", flush=True)
    # 4. stems
    mids = split_stems(r01_midi, stems_dir)
    def one(item):
        g, p = item
        w = p[:-4] + ".wav"
        subprocess.run([sys.executable, os.path.join(HERE, "stem.py"), p, w], check=True)
        return g, w
    with ThreadPoolExecutor(a.jobs) as ex:
        wavs = dict(ex.map(one, sorted(mids.items())))
    print(f"[{time.time()-t_start:5.1f}s] {len(wavs)} stems rendered", flush=True)
    # 5. mix and master
    sr = cfg["sample_rate"]
    mix = None
    for g, w in wavs.items():
        x, r = sf.read(w, dtype="float64", always_2d=True)
        if mix is None:
            mix = x
        else:
            if len(x) > len(mix):
                mix = np.vstack([mix, np.zeros((len(x) - len(mix), 2))])
            mix[:len(x)] += x
    # trim trailing near-silence (keep the room tail down to -90 dBFS)
    env = np.abs(mix).max(axis=1)
    last = np.nonzero(env > 10 ** (-90 / 20) * env.max())[0][-1]
    mix = mix[:last + int(0.2 * sr)]
    pre = os.path.join(W, "mix_prem.wav")
    sf.write(pre, mix.astype(np.float32), sr, subtype="FLOAT")
    I, LRA, TP = ebur128(pre)
    M = cfg["master"]
    g = M["target_LUFS"] - I
    print(f"premaster I {I:.1f} LUFS, LRA {LRA:.1f} LU, true peak {TP:.1f} dBTP; gain {g:+.2f} dB; peak after gain {TP+g:.1f} dBTP", flush=True)
    master = os.path.join(W, "master.wav")
    af = f"volume={g:.3f}dB"
    if TP + g > M["true_peak_dBTP"] - 0.3:
        # limiter on a 4x oversampled signal, ceiling 0.5 dB under the target true peak, slow release
        lim = 10 ** ((M["true_peak_dBTP"] - 0.5) / 20)
        af += f",aresample={4*sr},alimiter=limit={lim:.4f}:attack=5:release=200:level=false:asc=true,aresample={sr}"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", pre, "-af", af, "-c:a", "pcm_f32le", master], check=True)
    I2, LRA2, TP2 = ebur128(master)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", master, "-c:a", "libmp3lame", "-b:a", M["mp3_bitrate"], a.out], check=True)
    I3, LRA3, TP3 = ebur128(a.out)
    rep = {"premaster": {"I": I, "LRA": LRA, "TP": TP}, "gain_dB": g, "master_wav": {"I": I2, "LRA": LRA2, "TP": TP2},
           "mp3": {"I": I3, "LRA": LRA3, "TP": TP3}, "seconds": round(time.time() - t_start, 1)}
    json.dump(rep, open(os.path.join(W, "render_report.json"), "w"), indent=1)
    print(json.dumps(rep))


if __name__ == "__main__":
    main()

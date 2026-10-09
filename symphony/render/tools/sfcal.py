#!/usr/bin/env python3
"""Soundfont calibration: level and brightness of each General MIDI program at several velocities.

Usage:
  python3 sfcal.py --sf2 FILE.sf2 --out DIR [--programs 73,68,...] [--bank 0]
                   [--render 'fluidsynth -ni -g 0.6 -r 44100 -R 0 -C 0 -F {wav} {sf2} {midi}']

For each program a test MIDI plays one 2-second note at a mid-range pitch for velocities
32, 48, 64, 80, 96, 112, 127 (1 s apart). Writes DIR/sfcal.json and DIR/sfcal.csv with, per program and
velocity: loudness of the note (LUFS over the note), level change from velocity 64, spectral centroid,
and the centroid change from velocity 32 to 127 (does the sample get brighter when played louder?).
Default programs: the ones in v120's MIDI, plus 44 (tremolo strings), 45 (pizzicato strings), 49 (string ensemble 2).
"""
import argparse, csv, os, shlex, subprocess, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rtk

PITCH = {73: 74, 68: 69, 69: 62, 71: 62, 70: 48, 60: 55, 56: 67, 57: 53, 58: 41, 47: 48, 46: 60, 48: 67, 41: 60,
         42: 48, 43: 36, 44: 60, 45: 55, 49: 67, 40: 69, 72: 79, 61: 60, 59: 67}
VELS = [32, 48, 64, 80, 96, 112, 127]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sf2", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--programs", default="73,68,69,71,70,60,56,57,58,47,46,48,41,42,43,44,45,49")
    ap.add_argument("--bank", type=int, default=0)
    ap.add_argument("--render", default="fluidsynth -ni -g 0.6 -r 44100 -R 0 -C 0 -F {wav} {sf2} {midi}")
    a = ap.parse_args()
    import mido
    os.makedirs(a.out, exist_ok=True)
    wd = tempfile.mkdtemp(prefix="sfcal_")
    rows = []
    for prog in [int(p) for p in a.programs.split(",")]:
        m = mido.MidiFile(ticks_per_beat=480); t = mido.MidiTrack(); m.tracks.append(t)
        t.append(mido.MetaMessage("set_tempo", tempo=500000))
        t.append(mido.Message("control_change", channel=0, control=0, value=a.bank, time=0))
        t.append(mido.Message("program_change", channel=0, program=prog, time=0))
        p = PITCH.get(prog, 60)
        for i, v in enumerate(VELS):
            t.append(mido.Message("note_on", channel=0, note=p, velocity=v, time=0 if i == 0 else 480 * 2))
            t.append(mido.Message("note_off", channel=0, note=p, velocity=0, time=480 * 4))
        t.append(mido.MetaMessage("end_of_track", time=480 * 4))
        mid = os.path.join(wd, f"p{prog}.mid"); wav = os.path.join(wd, f"p{prog}.wav"); m.save(mid)
        subprocess.run(a.render.format(wav=shlex.quote(wav), sf2=shlex.quote(a.sf2), midi=shlex.quote(mid)), shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        x = rtk.decode(wav)
        res = {}
        for i, v in enumerate(VELS):
            s0 = int(i * 3.0 * rtk.SR); seg = x[s0 + int(0.05 * rtk.SR): s0 + int(2.0 * rtk.SR)]
            tM, M = rtk.loudness_series(seg, rtk.SR, 0.4, 0.1)
            f, P = rtk.psd(seg.mean(axis=1), nfft=4096)
            res[v] = (rtk.power_mean_lufs(M), float((f * P).sum() / (P.sum() + 1e-20)))
        for v in VELS:
            rows.append({"program": prog, "pitch": p, "velocity": v, "LUFS": round(res[v][0], 1),
                         "dB_rel_vel64": round(res[v][0] - res[64][0], 1), "centroid_Hz": round(res[v][1], 0)})
        print(f"prog {prog:3d}: vel64 {res[64][0]:6.1f} LUFS, 32->127 {res[127][0]-res[32][0]:5.1f} dB, centroid {res[32][1]:.0f}->{res[127][1]:.0f} Hz")
    with open(os.path.join(a.out, "sfcal.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    summ = {}
    for prog in sorted(set(r["program"] for r in rows)):
        rr = {r["velocity"]: r for r in rows if r["program"] == prog}
        summ[prog] = {"LUFS_vel64": rr[64]["LUFS"], "range_32_to_127_dB": round(rr[127]["LUFS"] - rr[32]["LUFS"], 1),
                      "centroid_vel32_Hz": rr[32]["centroid_Hz"], "centroid_vel127_Hz": rr[127]["centroid_Hz"],
                      "brightening_oct": round(float(np.log2((rr[127]["centroid_Hz"] + 1) / (rr[32]["centroid_Hz"] + 1))), 2)}
    rtk.save_json({"sf2": a.sf2, "render": a.render, "programs": summ}, os.path.join(a.out, "sfcal.json"))


if __name__ == "__main__":
    main()

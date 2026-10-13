#!/usr/bin/env python3
"""r07 (critic 6, plan 2 horns and plan 3): per-note samples and SFZ maps from the Philharmonia Orchestra sound samples
(one MP3 per pitch, length and dynamic, e.g. french-horn_C3_15_mezzo-forte_normal.mp3; https://philharmonia.co.uk/
audio-sound-samples/, free to use in any work, not to be resold as samples). Same output format as build_iowa.py
(key_dyn.wav + SFZ with -L/-R/-a2 player maps), so the stems play them through sfzplay like the Iowa sets.

Usage: build_phil.py NAME SRC_DIR OUT_DIR SFZ_PATH --prefix french-horn --dyns piano,mezzo-forte,fortissimo
       [--vel 41,60] [--pan-spread 35] [--release 0.15]

For every pitch and each of the three dynamic layers (pp, mf, ff slots of the SFZ), the longest plain note is used
(length code 15 = 1.5 s, else 1, else 05; 'normal' technique only). Each file is decoded with ffmpeg (mono 44.1 kHz),
its onset found on a 2 ms envelope (first frame within 20 dB of the note's sustain, sample starts 8 ms before), its
pitch measured (autocorrelation, build_iowa.pitch) and kept as SFZ tune when within 50 cents of the named pitch, the
note cut where it has decayed 45 dB under the sustain, levelled per layer (build_iowa.LAYER_DB), and given a sustain loop
on rising zero crossings between 0.35 s after the onset and 0.25 s before the release (if at least 0.35 s long).
"""
import argparse, glob, os, re, subprocess, sys
import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_iowa as BI

NN = {"C": 0, "Cs": 1, "D": 2, "Ds": 3, "E": 4, "F": 5, "Fs": 6, "G": 7, "Gs": 8, "A": 9, "As": 10, "B": 11}
SLOTS = ("pp", "mf", "ff")


def decode(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", "44100", "-f", "f32le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).astype(np.float64), 44100


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name"); ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("sfz")
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--dyns", required=True, help="three Philharmonia dynamic words for the pp, mf, ff layers")
    ap.add_argument("--vel", default="41,60")
    ap.add_argument("--pan-spread", type=float, default=0.0)
    ap.add_argument("--release", type=float, default=0.15)
    ap.add_argument("--tune", type=float, default=0.0, help="cents added to every region (calibration)")
    a = ap.parse_args()
    v1, v2 = (int(q) for q in a.vel.split(","))
    BI.VEL.update({"pp": (1, v1), "mf": (v1 + 1, v2), "ff": (v2 + 1, 127)})
    BI.XF = 0
    words = a.dyns.split(",")
    os.makedirs(a.out, exist_ok=True)
    notes, log = {}, []
    files = glob.glob(os.path.join(a.src, a.prefix + "_*_normal.mp3"))
    pat = re.compile(re.escape(a.prefix) + r"_([A-G]s?)(\d)_(15|1|05|025)_([a-z-]+)_normal\.mp3$")
    cand = {}
    for p in files:
        m = pat.search(os.path.basename(p))
        if not m or m.group(4) not in words:
            continue
        k = 12 * (int(m.group(2)) + 1) + NN[m.group(1)]
        dyn = SLOTS[words.index(m.group(4))]
        rank = ["15", "1", "05", "025"].index(m.group(3))
        if (k, dyn) not in cand or rank < cand[(k, dyn)][0]:
            cand[(k, dyn)] = (rank, p)
    for (k, dyn), (_, p) in sorted(cand.items()):
        x, sr = decode(p)
        e, h = BI.env_db(x, sr)
        hs = h / sr
        top = np.percentile(e, 95)
        on = np.nonzero(e > top - 25)[0]
        if not len(on):
            continue
        t0, t1 = on[0] * hs, (on[-1] + 1) * hs
        ee = e[on[0]:on[-1] + 1]
        sus = np.median(ee[int(0.2 / hs):max(int(0.2 / hs) + 1, len(ee) - int(0.15 / hs))]) if len(ee) > 0.5 / hs else np.median(ee)
        i0s = max(0, int((t0 - 0.2) * sr)); seg = x[i0s:int((t0 + 0.3) * sr)]
        hh2 = int(0.002 * sr); k2 = len(seg) // hh2
        e2 = 10 * np.log10((seg[:k2 * hh2].reshape(k2, hh2) ** 2).mean(1) + 1e-20)
        j2 = int(np.argmax(e2 > sus - 20)) if (e2 > sus - 20).any() else 0
        t0 = (i0s + j2 * hh2) / sr - 0.008
        i0 = int((t0 + min(0.4, (t1 - t0) * 0.3)) * sr); i1 = min(int(t1 * sr), i0 + int(0.4 * sr))
        cents = 0.0
        if i1 - i0 > int(0.1 * sr):
            try:
                midi = 69 + 12 * np.log2(BI.pitch(x[i0:i1], sr, lo=25.0) / 440.0)
            except IndexError:
                midi = float(k) + 6.0  # no clear period: no tune
            dev = (midi - k + 6) % 12 - 6
            if abs(dev) < 0.5:
                cents = float(np.clip(dev * 100, -40, 40))
            else:
                log.append(f"{os.path.basename(p)}: measured {midi:.2f} vs key {k}: tune not applied")
        a0 = max(0, int(t0 * sr))
        ee, hh = BI.env_db(x[a0:], sr)
        j = int((t1 - t0) / 0.01)
        while j < len(ee) and ee[j] > sus - 45:
            j += 1
        a1 = a0 + min(len(x) - a0, j * hh + int(0.02 * sr))
        y = x[a0:a1].copy()
        fo = min(len(y) // 4, int(0.02 * sr)); y[-fo:] *= np.linspace(1, 0, fo)
        fi = int(0.002 * sr); y[:fi] *= np.linspace(0, 1, fi)
        y *= 10 ** ((BI.LAYER_DB[dyn] - 18.0 - sus) / 20)
        ls = int(0.35 * sr); le = int((t1 - t0 - 0.25) * sr)
        loop = None
        if le - ls > int(0.35 * sr):
            zc = np.nonzero((y[:-1] < 0) & (y[1:] >= 0))[0]
            s1 = np.searchsorted(zc, ls); s2 = np.searchsorted(zc, le)
            if s1 < len(zc) and s2 > 0 and zc[s2 - 1] - zc[s1] > int(0.3 * sr):
                loop = (int(zc[s1]), int(zc[s2 - 1]))
        fn = os.path.join(a.out, f"{k:03d}_{dyn}.wav")
        sf.write(fn, y.astype(np.float32), sr, subtype="PCM_24")
        notes[(k, dyn)] = (fn, cents - a.tune, loop, t1 - t0)
        log.append(f"{os.path.basename(p)} key {k} {dyn} ({cents:+.0f} c) sus {sus:.1f} dB len {t1 - t0:.2f} s loop {loop}")
    # SFZ: same writer as build_iowa (group() closure there is local; rebuilt here with the same lines)
    sfz_dir = os.path.dirname(os.path.abspath(a.sfz))
    head = [f"// r07: {a.name} from the Philharmonia Orchestra sound samples (https://philharmonia.co.uk/audio-sound-samples/;",
            "// free to use in any work, not to be sold as samples). Built by r07/build_phil.py; one sample per key and",
            "// dynamic (pp/mf/ff slots), sustain loop, natural attack. Do not edit by hand: rerun build_phil.py."]

    def group(pan=0.0, detune=0.0, vol=0.0, delay=0.0):
        g = [f"<group> amp_veltrack=100 ampeg_attack=0.004 ampeg_release={a.release} loop_mode=loop_sustain loop_crossfade=0.1"
             + (f" pan={pan:g}" if pan else "") + (f" volume={vol:g}" if vol else "") + (f" delay={delay:g}" if delay else "")]
        for dyn in SLOTS:
            ks = sorted(k for k, d in notes if d == dyn)
            lo_v, hi_v = BI.VEL[dyn]
            for i, k in enumerate(ks):
                lok = 0 if i == 0 else (ks[i - 1] + k) // 2 + 1
                hik = 127 if i == len(ks) - 1 else (k + ks[i + 1]) // 2
                fn, cents, loop, dur = notes[(k, dyn)]
                rel = os.path.relpath(os.path.realpath(fn), os.path.realpath(sfz_dir))
                lp = f" loop_start={loop[0]} loop_end={loop[1]}" if loop else " loop_mode=no_loop"
                g.append(f"<region> sample={rel} lokey={lok} hikey={hik} pitch_keycenter={k} tune={-cents + detune:.0f}"
                         f" lovel={lo_v} hivel={hi_v}{lp}")
        return g
    base = a.sfz[:-4]
    open(a.sfz, "w").write("\n".join(head + ["// single player, centre"] + group()) + "\n")
    if a.pan_spread:
        P = a.pan_spread
        open(base + "-L.sfz", "w").write("\n".join(head + [f"// player 1 of a section, pan {-P:g}"] + group(pan=-P)) + "\n")
        open(base + "-R.sfz", "w").write("\n".join(head + [f"// player 2 of a section, pan {P:g}, 8 ms late"] + group(pan=P, delay=0.008)) + "\n")
        open(base + "-a2.sfz", "w").write("\n".join(head + ["// a2: both players in unison, -3 dB each, 8 cents apart, the second 12 ms late"]
                                              + group(pan=-P, detune=-4, vol=-3) + group(pan=P, detune=4, vol=-3, delay=0.012)) + "\n")
    open(os.path.join(a.out, "build_log.txt"), "w").write("\n".join(log) + "\n")
    print(f"{a.name}: {len(notes)} notes, per layer", {d: sum(1 for _, dd in notes if dd == d) for d in SLOTS},
          "loops", sum(1 for v in notes.values() if v[2]))


if __name__ == "__main__":
    main()

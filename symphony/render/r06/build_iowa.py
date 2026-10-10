#!/usr/bin/env python3
"""r05 (critic 4, plan 3): build per-note samples and an SFZ file from the University of Iowa MIS chromatic runs.

Usage: build_iowa.py NAME SRC_DIR OUT_DIR SFZ_PATH [--voices N] [--pan-spread P]

SRC_DIR holds the pre-2011 MIS files of one instrument (e.g. BbClar.pp.C4B4.aiff: one chromatic run per octave and
dynamic, single detached notes with natural attack and release, recorded dry, mono 44.1 kHz;
https://theremin.music.uiowa.edu/MIS.html, "may be downloaded and used for any projects, without restrictions").

For every file:
  1. note segmentation on a 10 ms RMS envelope: threshold = max(noise floor + 15 dB, file peak - 45 dB), runs above
     it longer than 0.3 s (gaps under 80 ms merged);
  2. pitch of each note by autocorrelation (parabolic peak) over its steadiest 0.4 s, rounded to the nearest MIDI key
     (cents deviation kept as SFZ tune);
  3. the note is cut from 15 ms before the onset to where the envelope falls 45 dB under the note's sustain level
     (its own release and room-free decay), with a 20 ms fade;
  4. a sustain loop between 0.45 s after the onset and 0.25 s before the release starts (when at least 0.6 s long),
     on rising zero crossings; sfzplay crossfades it.
Every note is written as 24-bit WAV (OUT_DIR/<key>_<dyn>.wav). Within a dynamic layer every note is normalised to the
same sustain RMS; the layers keep fixed offsets (LAYER_DB) so that the timbre changes with the dynamic while the
level per printed step is set by velocity and CC11, as for the other stems.

The SFZ maps each sample from its own key to halfway to the next sampled key (pitch_keycenter with tune), with three
velocity layers crossfaded (xfin/xfout) at the boundaries in VEL. loop_mode=loop_sustain: the note's sustain loops
while held; at note-off ampeg_release (short, as a wind player's tongue/breath stop) ends it.
--voices N writes N copies of the region list in N <group>s keyed to MIDI channels by the caller (one SFZ per channel
is how stem.py maps them); --pan-spread writes pan=+-P on the copies so that two players of one section are not one
mono point (critic 4: clarinet stems L/R correlation 0.91).
"""
import argparse, glob, os, re
import numpy as np
import soundfile as sf

LAYER_DB = {"pp": -4.0, "mf": 0.0, "ff": 2.5}
VEL = {"pp": (1, 58), "mf": (59, 88), "ff": (89, 127)}
XF = 8  # velocity crossfade half-width


def env_db(x, sr, h=0.01):
    n = int(h * sr); k = len(x) // n
    e = (x[:k * n].reshape(k, n) ** 2).mean(1)
    return 10 * np.log10(e + 1e-20), n


def segments(x, sr):
    e, h = env_db(x, sr)
    top = np.percentile(e[e > -150], 90) if (e > -150).any() else e.max()
    thr = top - 22  # the sustain of the file's notes is within a few dB of each other (one dynamic per file)
    on = e > thr
    runs = []; i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]:
                j += 1
            runs.append([i, j]); i = j
        else:
            i += 1
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < 8:
            merged[-1][1] = r[1]
        else:
            merged.append(r)
    hs = h / sr
    return [(a * hs, b * hs, e[a:b]) for a, b in merged if (b - a) * hs > 0.3], thr, hs


def pitch(x, sr, lo=40.0, hi=2200.0):
    x = x - x.mean()
    n = len(x)
    f = np.fft.rfft(x * np.hanning(n), 2 * n)
    ac = np.fft.irfft(np.abs(f) ** 2)[:n]
    ac /= ac[0] + 1e-20
    a, b = int(sr / hi), int(sr / lo)
    z = np.nonzero(ac[a:b] < 0.0)[0]
    a = a + (int(z[0]) if len(z) else 0)  # past the zero-lag lobe
    seg = ac[a:b]
    # first peak above 0.85 of the maximum (avoids octave errors from sub-harmonic peaks)
    mx = seg.max()
    idx = None
    for i in range(1, len(seg) - 1):
        if seg[i] > seg[i - 1] and seg[i] >= seg[i + 1] and seg[i] > 0.85 * mx:
            idx = i; break
    if idx is None:
        idx = int(np.argmax(seg))
    y0, y1, y2 = seg[idx - 1], seg[idx], seg[idx + 1]
    d = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2 + 1e-20)
    lag = a + idx + d
    return sr / lag


def yin_f0(x, sr, fmin, fmax, thr=0.3):
    """r06: YIN cumulative-mean-normalised difference (de Cheveigne & Kawahara 2002), FFT cross term; f0 or None."""
    x = x - x.mean(); n = len(x)
    lo, hi = max(2, int(sr / fmax)), int(sr / fmin)
    W = n - hi
    if W < 128:
        return None
    a = x[:W]
    N = 1 << int(np.ceil(np.log2(n + W)))
    cross = np.fft.irfft(np.fft.rfft(x, N) * np.conj(np.fft.rfft(a, N)), N)[:hi + 1]
    c2 = np.concatenate([[0.0], np.cumsum(x ** 2)])
    e_tau = c2[np.arange(hi + 1) + W] - c2[np.arange(hi + 1)]
    d = (a ** 2).sum() + e_tau - 2 * cross
    d[0] = 0
    cm = d[1:] * np.arange(1, hi + 1) / np.maximum(np.cumsum(d[1:]), 1e-12)
    cm = np.concatenate([[1.0], cm])
    seg = cm[lo:hi]
    if not len(seg):
        return None
    i = int(np.argmin(seg))
    if seg[i] > thr:
        return None
    j = lo + i
    if 1 <= j < hi:
        p, q, r = d[j - 1], d[j], d[j + 1]; den = p - 2 * q + r
        sh = 0.5 * (p - r) / den if den else 0.0
    else:
        sh = 0.0
    return sr / (j + sh)


def pitch_onset(x, sr, t_level, key, tol_c=30.0, look_back=0.1, look_ahead=0.6, hop=0.01, win=0.05, back_max=0.02):
    """r06 (critic 5, plan 1): the time where the note's own pitch is established. Some Iowa runs (bassoon, some oboe)
    are played without gaps, so the level onset lands in the previous note's tail (0.1-0.3 s a semitone low).
    f0 in 10 ms hops (50 ms windows) from look_back before the level onset; the first frame within tol_c of the key
    whose next two voiced frames are also within it; then back to the lowest 2 ms level within back_max before it
    (the articulation dip between the notes), never earlier than the level onset minus look_back."""
    ft = 440.0 * 2 ** ((key - 69) / 12)
    ds = 2 if sr > 40000 else 1
    xs = x[::ds]; srs = sr / ds
    t = max(0.0, t_level - look_back)
    cents = []
    times = []
    while t < t_level + look_ahead:
        seg = xs[int(t * srs):int((t + win) * srs)]
        if len(seg) < int(win * srs * 0.9):
            break
        f = yin_f0(seg, srs, ft / 1.6, ft * 1.6) if np.sqrt((seg ** 2).mean()) > 1e-6 else None
        cents.append(None if f is None else 1200 * np.log2(f / ft)); times.append(t)
        t += hop
    # tolerate the sample's own tuning: measure against the steady median of the last frames
    voiced = [c for c in cents[-15:] if c is not None]
    ref = float(np.median(voiced)) if voiced else 0.0
    ok = None
    for i, c in enumerate(cents):
        if c is None or abs(c - ref) > tol_c:
            continue
        nxt = [v for v in cents[i + 1:i + 4] if v is not None]
        if len(nxt) >= 2 and all(abs(v - ref) <= tol_c for v in nxt):
            ok = i; break
    if ok is None:
        return t_level, False
    # was any earlier frame clearly on another pitch (the previous note)? if not, keep the level onset
    # (a previous semitone of the ascending run, -60..-140 c, in at least 3 frames; a tongued attack's own pitch
    # scoop is shorter and is kept)
    prev = [c for c in cents[:ok] if c is not None and -140 <= c - ref <= -60]
    if len(prev) < 3:
        prev = []
    t_ok = times[ok] + 0.5 * win - hop  # the frame centre, less one hop (the frame is already on pitch)
    if not prev or t_ok <= t_level:
        return t_level, False
    a = max(0, int((t_ok - back_max) * sr)); b = int((t_ok + 0.004) * sr)
    h = int(0.002 * sr); k = (b - a) // h
    if k >= 2:
        e = (x[a:a + k * h].reshape(k, h) ** 2).mean(1)
        t_ok = (a + int(np.argmin(e)) * h) / sr
    return t_ok, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name"); ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("sfz")
    ap.add_argument("--pan-spread", type=float, default=0.0)
    ap.add_argument("--release", type=float, default=0.12)
    ap.add_argument("--vel", default="41,60", help="top velocity of the pp and mf layers (LilyPond's wind velocities: pp 29-36, p 37-40, mp 44-52, mf 51-56, f 58, ff 64)")
    ap.add_argument("--pitch-onset", action="store_true", help="r06: start each note where its own pitch is established (gapless runs: bassoon, oboe)")
    ap.add_argument("--fade-in", type=float, default=0.0, help="r06: fade-in (s) applied to samples whose start was moved by --pitch-onset")
    ap.add_argument("--xf", type=int, default=0, help="velocity crossfade half-width (0: hard layer switch; crossfading two takes of one pitch beats, measured 3.3 dB envelope ripple)")
    a = ap.parse_args()
    v1, v2 = (int(q) for q in a.vel.split(","))
    global XF
    XF = a.xf
    VEL.update({"pp": (1, v1), "mf": (v1 + 1, v2), "ff": (v2 + 1, 127)})
    os.makedirs(a.out, exist_ok=True)
    notes = {}  # (key, dyn) -> (path, tune_cents, loop)
    log = []
    for p in sorted(glob.glob(os.path.join(a.src, "*.aif*"))):
        m = re.search(r"\.(pp|mf|ff)\.", os.path.basename(p))
        if not m:
            continue
        dyn = m.group(1)
        x, sr = sf.read(p, dtype="float64", always_2d=True)
        x = x.mean(1)
        segs, thr, h = segments(x, sr)
        ef, _ = env_db(x, sr)
        # expected chromatic run from the file name (e.g. C4B4 = 60..71, concert pitch; 'Db2C2' = Db2..C3)
        rng = re.findall(r"([A-G]b?)(\d)", os.path.basename(p).split(".")[-2])
        expected = None
        if rng:
            nn = {"C": 0, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}
            lo = 12 * (int(rng[0][1]) + 1) + nn[rng[0][0]]
            hi = 12 * (int(rng[-1][1]) + 1) + nn[rng[-1][0]] if len(rng) > 1 else lo
            if hi < lo:
                hi += 12
            expected = list(range(lo, hi + 1))
        by_order = expected is not None and len(segs) == len(expected)
        for si, (t0, t1, e) in enumerate(segs):
            sus = np.median(e[int(0.3 / h):max(int(0.3 / h) + 1, len(e) - int(0.3 / h))]) if len(e) > 0.9 / h else np.median(e)
            # onset: first 2 ms frame (searched from 0.3 s before the threshold crossing) within 20 dB of the note's
            # sustain; the sample starts 8 ms before it. (A first version walked back through breath and key noise
            # and started notes up to 0.3 s early, i.e. sounding late: oboe median 0.27 s to -20 dB.)
            i0s = max(0, int((t0 - 0.3) * sr)); seg = x[i0s:int((t0 + 0.4) * sr)]
            hh2 = int(0.002 * sr); k2 = len(seg) // hh2
            e2 = 10 * np.log10((seg[:k2 * hh2].reshape(k2, hh2) ** 2).mean(1) + 1e-20)
            j2 = int(np.argmax(e2 > sus - 20)) if (e2 > sus - 20).any() else int(0.3 / 0.002)
            t1 = t1  # run end unchanged
            t0 = (i0s + j2 * hh2) / sr + 0.007
            # steadiest 0.4 s for the pitch
            i0 = int((t0 + min(0.5, (t1 - t0) * 0.3)) * sr); i1 = min(int(t1 * sr), i0 + int(0.4 * sr))
            if i1 - i0 < int(0.15 * sr):
                continue
            f0 = pitch(x[i0:i1], sr)
            midi = 69 + 12 * np.log2(f0 / 440.0)
            k = int(round(midi)); cents = (midi - k) * 100
            if by_order:
                k = expected[si]
                dev = (midi - k + 6) % 12 - 6
                cents = float(np.clip(dev * 100, -30, 30)) if abs(dev) < 0.5 else 0.0
            elif expected and not (expected[0] - 1 <= k <= expected[-1] + 1):
                log.append(f"{os.path.basename(p)} {t0:6.2f}s: pitch {midi:.2f} outside {expected[0]}-{expected[-1]}, skipped")
                continue
            moved = False
            if a.pitch_onset:
                t_new, moved = pitch_onset(x, sr, t0, k + cents / 100.0)
                if moved:
                    log.append(f"{os.path.basename(p)} key {k}: pitch onset {t_new - t0:+.3f} s after the level onset")
                    t0 = t_new
            # cut: from 15 ms before the onset to 45 dB under the sustain after the run ends
            a0 = max(0, int((t0 - (0.0 if moved else 0.015)) * sr))  # = 8 ms before the -20 dB point
            ee, hh = env_db(x[a0:], sr)
            end_i = int((t1 - t0) / 0.01)
            j = end_i
            while j < len(ee) and ee[j] > sus - 45:
                j += 1
            a1 = a0 + min(len(x) - a0, j * hh + int(0.02 * sr))
            y = x[a0:a1].copy()
            fo = int(0.02 * sr)
            y[-fo:] *= np.linspace(1, 0, fo)
            if moved and a.fade_in > 0:
                fi = int(a.fade_in * sr)
                y[:fi] *= np.linspace(0, 1, fi) ** 2
            # level: sustain RMS to the layer offset
            g = 10 ** ((LAYER_DB[dyn] - 18.0 - sus) / 20)
            y *= g
            # loop on rising zero crossings
            ls = int(0.45 * sr); le = int((t1 - t0 - 0.25) * sr)
            loop = None
            if le - ls > int(0.6 * sr):
                zc = np.nonzero((y[:-1] < 0) & (y[1:] >= 0))[0]
                ls2 = zc[np.searchsorted(zc, ls)] if np.searchsorted(zc, ls) < len(zc) else None
                le2 = zc[np.searchsorted(zc, le) - 1] if np.searchsorted(zc, le) > 0 else None
                if ls2 is not None and le2 is not None and le2 - ls2 > int(0.5 * sr):
                    loop = (int(ls2), int(le2))
            if (k, dyn) in notes:
                continue
            fn = os.path.join(a.out, f"{k:03d}_{dyn}.wav")
            sf.write(fn, y.astype(np.float32), sr, subtype="PCM_24")
            notes[(k, dyn)] = (fn, cents, loop, (t1 - t0))
            log.append(f"{os.path.basename(p)} {t0:6.2f}-{t1:6.2f}s key {k} ({cents:+.0f} c) sus {sus:.1f} dB loop {loop}")
    keys = sorted(set(k for k, _ in notes))
    sfz_dir = os.path.dirname(os.path.abspath(a.sfz))
    head = [f"// r05/r06: {a.name} from the University of Iowa MIS (pre-2011 chromatic runs, pp / mf / ff; free for any use,",
            "// https://theremin.music.uiowa.edu/MIS.html). Built by r05/build_iowa.py; one sample per key and dynamic,",
            "// velocity layers crossfaded, sustain loop, natural attack. Do not edit by hand: rerun build_iowa.py."]

    def group(pan=0.0, detune=0.0, vol=0.0, delay=0.0):
        g = [f"<group> amp_veltrack=100 ampeg_attack=0.004 ampeg_release={a.release} loop_mode=loop_sustain loop_crossfade=0.12"
             + (f" pan={pan:g}" if pan else "") + (f" volume={vol:g}" if vol else "") + (f" delay={delay:g}" if delay else "")]
        for dyn in ("pp", "mf", "ff"):
            ks = sorted(k for k, d in notes if d == dyn)
            lo_v, hi_v = VEL[dyn]
            for i, k in enumerate(ks):
                lok = 0 if i == 0 else (ks[i - 1] + k) // 2 + 1
                hik = 127 if i == len(ks) - 1 else (k + ks[i + 1]) // 2
                fn, cents, loop, dur = notes[(k, dyn)]
                rel = os.path.relpath(fn, sfz_dir)
                xf = ""
                if dyn != "pp" and XF:
                    xf += f" xfin_lovel={lo_v - XF} xfin_hivel={lo_v + XF}"
                if dyn != "ff" and XF:
                    xf += f" xfout_lovel={hi_v - XF} xfout_hivel={hi_v + XF}"
                lv = max(1, lo_v - XF) if dyn != "pp" else 1
                hv = min(127, hi_v + XF) if dyn != "ff" else 127
                lp = f" loop_start={loop[0]} loop_end={loop[1]}" if loop else " loop_mode=no_loop"
                g.append(f"<region> sample={rel} lokey={lok} hikey={hik} pitch_keycenter={k} tune={-cents + detune:.0f}"
                         f" lovel={lv} hivel={hv}{xf}{lp}")
        return g
    base = a.sfz[:-4]
    open(a.sfz, "w").write("\n".join(head + ["// single player, centre"] + group()) + "\n")
    if a.pan_spread:
        P = a.pan_spread
        open(base + "-L.sfz", "w").write("\n".join(head + [f"// player 1 of a section, pan {-P:g}"] + group(pan=-P)) + "\n")
        open(base + "-R.sfz", "w").write("\n".join(head + [f"// player 2 of a section, pan {P:g}"] + group(pan=P)) + "\n")
        open(base + "-a2.sfz", "w").write("\n".join(head + ["// a2: both players in unison, -3 dB each, 8 cents apart, the second 12 ms late"]
                                              + group(pan=-P, detune=-4, vol=-3) + group(pan=P, detune=4, vol=-3, delay=0.012)) + "\n")
    open(os.path.join(a.out, "build_log.txt"), "w").write("\n".join(log) + "\n")
    print(f"{a.name}: {len(notes)} notes, keys {keys[0]}-{keys[-1]}, per layer",
          {d: sum(1 for _, dd in notes if dd == d) for d in ("pp", "mf", "ff")})


if __name__ == "__main__":
    main()

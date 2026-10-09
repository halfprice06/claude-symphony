#!/usr/bin/env python3
"""Render one staff's MIDI (tempo track + that staff's tracks, as written by articulate.py) to a processed stem.

Usage: stem.py STEM.mid OUT.wav [--config config.json] [--dry]

Chain (same for the mix and for tools/stems.py, so that stem measurements are what the mix uses):
  1. FluidSynth, internal reverb and chorus off, fixed gain, 32-bit float WAV (no clipping possible);
  2. channel trim gain written by articulate.py (text meta "r01 stem trim +X dB") and the stem gain from config;
  3. brightness: zero-phase crossover at config.brightness.crossover_Hz; the band above it gets a gain that
     follows the printed dynamic (CC20 curve), 0 dB at ff, lower at softer dynamics;
  4. width and pan: mid/side narrowing, then constant-power pan;
  5. room: the stem (mono sum) convolved with the Detmold Konzerthaus impulse response of the loudspeaker
     position given in config (omni + figure-of-eight decoded as mid/side stereo, direct sound removed),
     at send_dB relative to the dry stem, added to the dry signal.
No loudness normalisation per stem.
"""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np
import soundfile as sf
import mido
from scipy.signal import butter, sosfiltfilt, oaconvolve

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


_IR = {}


def raw_ir(cfg, src, sr):
    d = os.path.join(ASSETS, "ir", "detmold_konzerthaus_setC_" + cfg["ir_receiver"])
    o, r1 = sf.read(os.path.join(d, f"Omni_{src}{cfg['ir_receiver']}.wav"))
    f, r2 = sf.read(os.path.join(d, f"Fig8_{src}{cfg['ir_receiver']}.wav"))
    assert r1 == r2 == sr, (r1, r2, sr)
    g = cfg["ir_fig8_gain"]
    ir = np.stack([o + g * f, o - g * f], axis=1)  # figure-of-eight positive lobe points left (checked on S1/S4)
    k = int(np.argmax(np.abs(o)))
    cut = k + int(cfg["ir_direct_cut_ms"] * 1e-3 * sr)
    fade = int(0.002 * sr)
    w = np.zeros(len(o)); w[cut:cut + fade] = np.linspace(0, 1, fade); w[cut + fade:] = 1
    ir = (ir * w[:, None])[k:]  # time zero = direct sound; the dry stem plays the direct sound
    tail = int(0.05 * sr); ir[-tail:] *= np.linspace(1, 0, tail)[:, None]
    return ir


def load_ir(cfg, src, sr):
    """Processed stereo IR; every source scaled by one factor so that source S3's IR has unit energy gain per
    channel in 250-2000 Hz (send 0 dB = reverberant energy equal to the dry energy there for S3); measured
    relative levels between sources kept."""
    if src not in _IR:
        ref = raw_ir(cfg, "S3", sr)
        # energy gain of the S3 response in 250-2000 Hz (where most orchestral energy is), mean of L and R
        H = np.abs(np.fft.rfft(ref, 2 ** 17, axis=0)) ** 2
        f = np.fft.rfftfreq(2 ** 17, 1 / sr)
        scale = 1.0 / np.sqrt(H[(f >= 250) & (f <= 2000)].mean())
        _IR[src] = (raw_ir(cfg, src, sr) * scale).astype(np.float32)
    return _IR[src]


def cc_curve(mid, control, sr, n, rate_dt=0.01):
    """Step curve of a controller on channel 0, sampled every rate_dt seconds: (times, values)."""
    tempo_ev, pts = [], []
    for tr in mid.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == "set_tempo":
                tempo_ev.append((t, m.tempo))
    tempo_ev.sort()
    if not tempo_ev or tempo_ev[0][0] > 0:
        tempo_ev.insert(0, (0, 500000))
    def t2s(tick):
        s, lt, lv = 0.0, 0, tempo_ev[0][1]
        for tk, tv in tempo_ev:
            if tk > tick:
                break
            s += (tk - lt) * lv / 1e6 / mid.ticks_per_beat; lt, lv = tk, tv
        return s + (tick - lt) * lv / 1e6 / mid.ticks_per_beat
    for tr in mid.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == "control_change" and m.control == control and m.channel == 0:
                pts.append((t, m.value))
    if not pts:
        return None
    pts.sort()
    secs = np.array([t2s(p[0]) for p in pts]); vals = np.array([p[1] for p in pts], float)
    tg = np.arange(0, n / sr + rate_dt, rate_dt)
    idx = np.searchsorted(secs, tg, side="right") - 1
    return tg, np.where(idx >= 0, vals[np.clip(idx, 0, None)], vals[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("midi"); ap.add_argument("wav")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    ap.add_argument("--dry", action="store_true", help="skip the room (for checks)")
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    sr = cfg["sample_rate"]
    mid = mido.MidiFile(a.midi)
    names = [tr.name for tr in mid.tracks[1:] if any(not m.is_meta for m in tr)]
    st = key(names[0]) if names else "drums"
    if any(m.type == "note_on" and m.channel == 9 for tr in mid.tracks for m in tr):
        st = "drums" if all(key(n) == "drums" for n in names) else st
    sc = cfg["stems"].get(st)
    if sc is None:
        sys.exit(f"stem.py: no config for staff {st!r}")
    trim = 0.0
    for tr in mid.tracks:
        for m in tr:
            if m.type == "text" and m.text.startswith("r01 stem trim"):
                trim = max(trim, float(m.text.split("+")[1].split()[0]))
    tmp = tempfile.mkdtemp(prefix="r01stem_")
    raw = os.path.join(tmp, "raw.wav")
    subprocess.run(["fluidsynth", "-ni", "-q", "-R", "0", "-C", "0", "-g", str(cfg["fluid_gain"]), "-r", str(sr),
                    "-o", "synth.polyphony=512", "-O", "float", "-T", "wav", "-F", raw, cfg["sf2"], a.midi],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    x, r = sf.read(raw, dtype="float32", always_2d=True)
    os.remove(raw); os.rmdir(tmp)
    assert r == sr
    x = x * np.float32(10 ** ((sc["gain_dB"] + trim) / 20))
    n = len(x)
    # brightness from the dynamic curve
    B = cfg["brightness"]
    cv = cc_curve(mid, 20, sr, n)
    if cv is not None and sc["family"] not in ("timp",):
        tg, v = cv
        gdb = np.clip((v - B["ref_velocity"]) * B["dB_per_velocity"], B["min_dB"], B["max_dB"])
        k = 5  # 50 ms moving average on the 10 ms grid, to avoid steps
        gdb = np.convolve(np.pad(gdb, (k // 2, k - k // 2 - 1), mode="edge"), np.ones(k) / k, mode="valid")
        g = (10 ** (np.interp(np.arange(n, dtype=np.float32) / sr, tg, gdb) / 20)).astype(np.float32)
        sos = butter(2, B["crossover_Hz"], "lowpass", fs=sr, output="sos")
        lo = sosfiltfilt(sos, x, axis=0).astype(np.float32)
        x = lo + (x - lo) * g[:, None]
    # width and pan
    mid_s = 0.5 * (x[:, 0] + x[:, 1]); side = 0.5 * (x[:, 0] - x[:, 1]) * sc["width"]
    th = (sc["pan"] + 1) * np.pi / 4
    mid_s, side = mid_s.astype(np.float32), side.astype(np.float32)
    # keep the stem's power: narrowing a decorrelated (wide-stereo) sample would otherwise lower its level by
    # up to 3 dB while a mono sample (e.g. the brass) keeps its level
    e_in = float((x.astype(np.float64) ** 2).sum()); e_out = float(2 * (mid_s.astype(np.float64) ** 2).sum() + 2 * (side.astype(np.float64) ** 2).sum())
    if e_out > 0:
        k = np.float32(np.sqrt(e_in / e_out)); mid_s *= k; side *= k
    gl, gr = np.cos(th) * np.sqrt(2), np.sin(th) * np.sqrt(2)
    y = np.stack([gl * mid_s + side, gr * mid_s - side], axis=1)
    if not a.dry:
        ir = load_ir(cfg, sc["src"], sr)
        send = 10 ** ((sc["send_dB"] + cfg["reverb_master_dB"]) / 20)
        wet = oaconvolve(mid_s[:, None] * send, ir, axes=0)
        y = np.vstack([y, np.zeros((len(wet) - n, 2), np.float32)]) + wet.astype(np.float32)
    sf.write(a.wav, y.astype(np.float32), sr, subtype="FLOAT")


if __name__ == "__main__":
    main()

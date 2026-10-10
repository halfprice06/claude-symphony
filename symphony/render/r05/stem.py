#!/usr/bin/env python3
"""Render one staff's MIDI (tempo track + that staff's tracks, as written by articulate.py) to a processed stem.

Usage: stem.py STEM.mid OUT.wav [--config config.json] [--dry] [--engine fluidsynth|sfz]

Chain (same for the mix and for tools/stems.py, so that stem measurements are what the mix uses):
  1. synthesis, 32-bit float, no clipping possible:
       engine "fluidsynth": FluidSynth + FluidR3_GM, internal reverb and chorus off, fixed gain (as r01);
       engine "sfz" (r02): sfzplay.py plays each MIDI channel from its own SFZ file (Virtual Playing Orchestra
       articulation sets for the strings, sfz/perc-r02.sfz for the percussion), with per-channel trims, per-note
       envelope rules (config stems.<staff>.sfz.channels.<ch>.env) and the channel's CC11 curve applied as gain
       (40*log10(cc/127) dB, the same law as FluidSynth and sfizz);
  2. channel trim gain written by articulate.py (fluidsynth engine), the stem gain from config, and the CC11
     headroom (config dynamics.headroom_dB) given back;
  3. brightness: zero-phase crossover at config.brightness.crossover_Hz; the band above it gets a gain that
     follows the printed dynamic (CC20 curve), 0 dB at ff, lower at softer dynamics. r02: with
     brightness.preserve_level the stem's broadband level is restored after the filter (0.4 s windows), so
     the filter changes tone colour only and does not lower bright stems more than dark ones;
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
from scipy.ndimage import uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
sys.path.insert(0, HERE)


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
    channel in 250-2000 Hz (send 0 dB = reverberant energy equal to the dry energy there for S3)."""
    if src not in _IR:
        ref = raw_ir(cfg, "S3", sr)
        H = np.abs(np.fft.rfft(ref, 2 ** 17, axis=0)) ** 2
        f = np.fft.rfftfreq(2 ** 17, 1 / sr)
        scale = 1.0 / np.sqrt(H[(f >= 250) & (f <= 2000)].mean())
        _IR[src] = (raw_ir(cfg, src, sr) * scale).astype(np.float32)
    return _IR[src]


class TMap:
    def __init__(self, mid):
        ev = []
        for tr in mid.tracks:
            t = 0
            for m in tr:
                t += m.time
                if m.type == "set_tempo":
                    ev.append((t, m.tempo))
        ev.sort()
        if not ev or ev[0][0] > 0:
            ev.insert(0, (0, 500000))
        self.ev = ev; self.tpb = mid.ticks_per_beat
        self.secs = [0.0]
        for i in range(1, len(ev)):
            self.secs.append(self.secs[-1] + (ev[i][0] - ev[i - 1][0]) * ev[i - 1][1] / 1e6 / self.tpb)
        self.ticks = np.array([e[0] for e in ev])

    def t2s(self, tick):
        i = int(np.searchsorted(self.ticks, tick, side="right") - 1)
        return self.secs[i] + (tick - self.ev[i][0]) * self.ev[i][1] / 1e6 / self.tpb


def cc_points(mid, tm, control):
    """{channel: [(seconds, value)]} for one controller."""
    pts = {}
    for tr in mid.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == "control_change" and m.control == control:
                pts.setdefault(m.channel, []).append((tm.t2s(t), m.value))
    for c in pts:
        pts[c].sort()
    return pts


def cc_curve(mid, control, sr, n, rate_dt=0.01):
    """Step curve of a controller, sampled every rate_dt seconds: (times, values); r02: the maximum over
    channels (wind staves carry one curve per voice channel)."""
    tm = TMap(mid)
    pts = cc_points(mid, tm, control)
    if not pts:
        return None
    tg = np.arange(0, n / sr + rate_dt, rate_dt)
    out = None
    for c, p in pts.items():
        secs = np.array([q[0] for q in p]); vals = np.array([q[1] for q in p], float)
        idx = np.searchsorted(secs, tg, side="right") - 1
        v = np.where(idx >= 0, vals[np.clip(idx, 0, None)], vals[0])
        out = v if out is None else np.maximum(out, v)
    return tg, out


def midi_notes(mid, tm):
    """[(channel, t_on, t_off, key, vel)]"""
    out = []
    for tr in mid.tracks:
        t = 0; act = {}
        for m in tr:
            t += m.time
            if m.type == "note_on" and m.velocity > 0:
                act.setdefault((m.channel, m.note), []).append((t, m.velocity))
            elif m.type in ("note_off", "note_on") and act.get((m.channel, m.note)):
                on, v = act[(m.channel, m.note)].pop(0)
                out.append((m.channel, tm.t2s(on), tm.t2s(t), m.note, v))
    return out


def env_for(rule, L):
    """Per-note envelope overrides from a channel rule: list of [max_len_s or null, {overrides}] (first match)."""
    if not rule:
        return None
    for lim, ov in rule:
        if lim is None or L < lim:
            return ov
    return None


def render_sfz(mid, sc, cfg, sr):
    import sfzplay
    S = sc["sfz"]
    tm = TMap(mid)
    notes = midi_notes(mid, tm)
    cc11 = cc_points(mid, tm, 11)
    end = max([n[2] for n in notes] + [1.0]) + S.get("tail_s", 8.0)
    n = int(end * sr) + 1
    out = np.zeros((n, 2), np.float32)
    by_ch = {}
    for c, t0, t1, k, v in notes:
        by_ch.setdefault(c, []).append((t0, t1, k, v))
    for c, lst in sorted(by_ch.items()):
        spec = S["channels"].get(str(c))
        if spec is None:
            raise SystemExit(f"stem.py: no SFZ for channel {c}")
        path = spec["file"] if os.path.isabs(spec["file"]) else os.path.normpath(os.path.join(HERE, spec["file"]))
        inst = sfzplay.Sfz(path)
        rule = spec.get("env")
        nl = [(t0, t1, k, v, env_for(rule, t1 - t0)) for t0, t1, k, v in lst]
        y = sfzplay.render(inst, nl, sr, end, seed=S.get("seed", 1) * 100 + c)
        y *= np.float32(10 ** (spec.get("trim_dB", 0.0) / 20))
        # CC11 of this channel as gain (40*log10 law). r03: a CC value holds until the next message (as in a MIDI
        # synth); r02 interpolated linearly between successive messages, so a value that stayed constant for 17 s
        # ramped towards the next one over all 17 s (e.g. the roll settle drifted back up). Ramps that articulate.py
        # writes as 20 ms steps stay ramps (linear over at most 20 ms).
        p = cc11.get(c)
        if p:
            ts0 = np.array([q[0] for q in p]); vs0 = np.array([q[1] for q in p], float)
            ts = [ts0[0]]; vs = [vs0[0]]
            for i in range(1, len(ts0)):
                if ts0[i] - ts0[i - 1] > 0.021:
                    ts.append(ts0[i] - 0.02); vs.append(vs0[i - 1])
                ts.append(ts0[i]); vs.append(vs0[i])
            ts = np.array(ts); vs = np.array(vs)
            tt = np.arange(n, dtype=np.float64) / sr
            g = np.interp(tt, ts, (vs / 127.0) ** 2).astype(np.float32)
            y *= g[:, None]
        out += y
    return out


def synth(mid, sc, cfg, st, engine):
    """Stage 1: synthesis, static gains, tone shelves and the brightness filter -> stereo float32 (n, 2)."""
    sr = cfg["sample_rate"]
    gain = sc["gain_dB"]
    if st != "drums":
        gain += cfg["dynamics"].get("headroom_dB", 0.0)
    if engine == "sfz":
        x = render_sfz(mid, sc, cfg, sr)
        gain += sc["sfz"].get("gain_dB", 0.0)
    else:
        trim = 0.0
        for tr in mid.tracks:
            for m in tr:
                if m.type == "text" and m.text.startswith("r01 stem trim"):
                    trim = max(trim, float(m.text.split("+")[1].split()[0]))
        tmp = tempfile.mkdtemp(prefix="r03stem_")
        raw = os.path.join(tmp, "raw.wav"); mp = os.path.join(tmp, "in.mid")
        ov = sc.get("sfz_overlay")
        x_ov = None
        if ov:
            # r04 (critic 3, plan 3): channels listed in sfz_overlay (e.g. the wind staccato channel) are played by
            # sfzplay from recorded samples; FluidSynth plays every other channel
            och = set(int(c) for c in ov["channels"])
            mf = mido.MidiFile(type=mid.type, ticks_per_beat=mid.ticks_per_beat)
            mo = mido.MidiFile(type=mid.type, ticks_per_beat=mid.ticks_per_beat)
            for tr in mid.tracks:
                a_, b_ = mido.MidiTrack(), mido.MidiTrack(); ta = tb = 0
                for m in tr:
                    ta += m.time; tb += m.time
                    if not m.is_meta and m.type in ("note_on", "note_off") and m.channel in och:
                        b_.append(m.copy(time=tb)); tb = 0
                    elif not m.is_meta and hasattr(m, "channel") and m.channel in och:
                        b_.append(m.copy(time=tb)); tb = 0
                        a_.append(m.copy(time=ta)); ta = 0
                    else:
                        a_.append(m.copy(time=ta)); ta = 0
                        if m.is_meta:
                            b_.append(m.copy(time=tb)); tb = 0
                mf.tracks.append(a_); mo.tracks.append(b_)
            if any(m.type == "note_on" for tr in mo.tracks for m in tr):
                x_ov = render_sfz(mo, {"sfz": ov}, cfg, sr) * np.float32(10 ** ((gain + ov.get("gain_dB", 0.0)) / 20))
            mid = mf
        mid.save(mp)
        subprocess.run(["fluidsynth", "-ni", "-q", "-R", "0", "-C", "0", "-g", str(cfg["fluid_gain"]), "-r", str(sr),
                        "-o", "synth.polyphony=512", "-O", "float", "-T", "wav", "-F", raw, cfg["sf2"], mp],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        x, r = sf.read(raw, dtype="float32", always_2d=True)
        os.remove(raw); os.remove(mp); os.rmdir(tmp)
        assert r == sr
        gain += trim
        x = x * np.float32(10 ** (gain / 20))
        if x_ov is not None:
            if len(x_ov) > len(x):
                x = np.vstack([x, np.zeros((len(x_ov) - len(x), 2), np.float32)])
            x[:len(x_ov)] += x_ov
        gain = 0.0
    x = x * np.float32(10 ** (gain / 20))
    n = len(x)
    # r02: static high shelf (tone), e.g. to take the close-microphone brightness off the VPO violin samples
    tone = sc.get("tone") or {}
    if tone.get("shelf_dB"):
        sos = butter(2, tone["shelf_Hz"], "lowpass", fs=sr, output="sos")
        lo = sosfiltfilt(sos, x, axis=0).astype(np.float32)
        x = lo + (x - lo) * np.float32(10 ** (tone["shelf_dB"] / 20))
    # r03 (critic 2, plan 5): low shelf (VPO section basses / cellos have weak fundamentals) and an 'air' shelf
    # (air absorption at about 20 m takes several dB above 8-10 kHz, https://sengpielaudio.com/calculator-air.htm)
    if tone.get("low_shelf_dB"):
        sos = butter(2, tone["low_shelf_Hz"], "lowpass", fs=sr, output="sos")
        lo = sosfiltfilt(sos, x, axis=0).astype(np.float32)
        x = x + lo * np.float32(10 ** (tone["low_shelf_dB"] / 20) - 1)
    air = sc.get("air", cfg.get("air"))
    if air and air.get("dB"):
        sos = butter(2, air["Hz"], "lowpass", fs=sr, output="sos")
        lo = sosfiltfilt(sos, x, axis=0).astype(np.float32)
        x = lo + (x - lo) * np.float32(10 ** (air["dB"] / 20))
    # brightness from the dynamic curve
    B = cfg["brightness"]
    cv = cc_curve(mid, 20, sr, n)
    if cv is not None and sc["family"] not in ("timp", "perc"):
        tg, v = cv
        gdb = np.clip((v - B["ref_velocity"]) * B["dB_per_velocity"], B["min_dB"], B["max_dB"])
        k = 5
        gdb = np.convolve(np.pad(gdb, (k // 2, k - k // 2 - 1), mode="edge"), np.ones(k) / k, mode="valid")
        g = (10 ** (np.interp(np.arange(n, dtype=np.float32) / sr, tg, gdb) / 20)).astype(np.float32)
        sos = butter(2, B["crossover_Hz"], "lowpass", fs=sr, output="sos")
        lo = sosfiltfilt(sos, x, axis=0).astype(np.float32)
        y = lo + (x - lo) * g[:, None]
        if B.get("preserve_level"):
            w = int(B.get("preserve_window_s", 0.4) * sr)
            e_in = uniform_filter1d((x.astype(np.float64) ** 2).sum(1), w)
            e_out = uniform_filter1d((y.astype(np.float64) ** 2).sum(1), w)
            floor = 1e-12 * max(e_in.max(), 1e-30)
            c = np.sqrt((e_in + floor) / (e_out + floor))
            c = np.clip(c, 1.0, 10 ** (B.get("preserve_max_dB", 3.0) / 20)).astype(np.float32)
            y *= c[:, None]
        x = y
    return x.astype(np.float32)


def place(x, sc, cfg, gain_curve=None, dry=False):
    """Stage 2: optional slow gain curve (r03 mix balance: (times_s, dB)), width and pan, room."""
    sr = cfg["sample_rate"]
    n = len(x)
    if gain_curve is not None:
        tg, gdb = gain_curve
        g = (10 ** (np.interp(np.arange(n) / sr, tg, gdb) / 20)).astype(np.float32)
        x = x * g[:, None]
    mid_s = 0.5 * (x[:, 0] + x[:, 1]); side = 0.5 * (x[:, 0] - x[:, 1]) * sc["width"]
    th = (sc["pan"] + 1) * np.pi / 4
    mid_s, side = mid_s.astype(np.float32), side.astype(np.float32)
    e_in = float((x.astype(np.float64) ** 2).sum()); e_out = float(2 * (mid_s.astype(np.float64) ** 2).sum() + 2 * (side.astype(np.float64) ** 2).sum())
    if e_out > 0:
        k = np.float32(np.sqrt(e_in / e_out)); mid_s *= k; side *= k
    gl, gr = np.cos(th) * np.sqrt(2), np.sin(th) * np.sqrt(2)
    y = np.stack([gl * mid_s + side, gr * mid_s - side], axis=1)
    if not dry:
        ir = load_ir(cfg, sc["src"], sr)
        send = 10 ** ((sc["send_dB"] + cfg["reverb_master_dB"]) / 20)
        wet = oaconvolve(mid_s[:, None] * send, ir, axes=0)
        y = np.vstack([y, np.zeros((len(wet) - n, 2), np.float32)]) + wet.astype(np.float32)
    return y.astype(np.float32)


def staff_of(mid, cfg):
    names = [tr.name for tr in mid.tracks[1:] if any(not m.is_meta for m in tr)]
    st = key(names[0]) if names else "drums"
    if any(m.type == "note_on" and m.channel == 9 for tr in mid.tracks for m in tr):
        st = "drums" if all(key(n) == "drums" for n in names) else st
    return st


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("midi"); ap.add_argument("wav")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    ap.add_argument("--dry", action="store_true", help="skip the room (for checks)")
    ap.add_argument("--engine", help="override the stem's engine (fluidsynth|sfz), for A/B tests")
    ap.add_argument("--synth-out", help="r03: also save the stage-1 signal (before gain curve, pan and room)")
    ap.add_argument("--from-synth", help="r03: skip synthesis, read this stage-1 signal")
    ap.add_argument("--gain-curve", help="r03: .npy array (2, k): times in s and gain in dB (mix balance)")
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    mid = mido.MidiFile(a.midi)
    st = staff_of(mid, cfg)
    sc = cfg["stems"].get(st)
    if sc is None:
        # r04: family fallback (lib/staffmap.py) instead of aborting
        sys.path.insert(0, os.path.join(HERE, "lib"))
        import staffmap
        k, sc = staffmap.resolve(cfg, st)
        if sc is None:
            sys.exit(f"stem.py: no config for staff {st!r} and no instrument word in its name")
        print(f"stem.py: staff {st!r} has no config entry; using {k!r}", file=sys.stderr)
    if a.from_synth:
        x, _ = sf.read(a.from_synth, dtype="float32", always_2d=True)
    else:
        x = synth(mid, sc, cfg, st, a.engine or sc.get("engine", "fluidsynth"))
        if a.synth_out:
            sf.write(a.synth_out, x, cfg["sample_rate"], subtype="FLOAT")
    gc = None
    if a.gain_curve:
        g = np.load(a.gain_curve); gc = (g[0], g[1])
    y = place(x, sc, cfg, gc, a.dry)
    sf.write(a.wav, y, cfg["sample_rate"], subtype="FLOAT")


if __name__ == "__main__":
    main()

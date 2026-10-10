#!/usr/bin/env python3
"""Minimal SFZ sample player in Python (numpy/scipy), written for r02 because no SFZ player may be installed.

It implements the subset of SFZ 1/2 opcodes used by the Virtual Playing Orchestra 3 files r02 plays
(checked with grep over those files):
  headers  <control> (default_path), <global>, <master>, <group>, <region>; #define, #include
  mapping  sample, key, lokey, hikey, lovel, hivel, seq_length, seq_position,
           xfin_lovel/xfin_hivel/xfout_lovel/xfout_hivel, xfin_lokey/.../xfout_hikey (power curve)
  pitch    pitch_keycenter, pitch_keytrack, transpose, tune, pitch_random
  amp      volume, amp_veltrack, amp_random, pan (balance on stereo samples)
  timing   delay, delay_random, offset
  env      ampeg_delay, ampeg_attack, ampeg_hold, ampeg_decay, ampeg_sustain, ampeg_release and the
           ampeg_vel2* modifiers (value added = modifier * velocity / 127)
  loops    loop_mode (no_loop, one_shot, loop_continuous, loop_sustain); loop points from loop_start /
           loop_end or from the WAV 'smpl' chunk (the default mode is loop_continuous when the file has a loop)
  filters  eq1..eq3 (peaking, freq / bw in octaves / gain), fil_type lpf_2p/lpf_1p with cutoff and fil_veltrack
  choke    group / off_by (fast release of the choked voices)
Not implemented (not used by the files r02 plays, or ignored on purpose): CC-modulated opcodes (gain_ccN,
delay_ccN ...), ampeg_dynamic, pitch envelopes, LFOs. r03: trigger=release regions play at note-off; every loop gets
a crossfade (loop_crossfade, default 0.1 s); optional random-segment looping (loop_random) for long rolls.

Semantics follow the SFZ format reference https://sfzformat.com/ (opcode pages, e.g.
https://sfzformat.com/opcodes/amp_veltrack , https://sfzformat.com/opcodes/loop_mode ,
https://sfzformat.com/opcodes/xfin_lovel , https://sfzformat.com/opcodes/seq_position ) and sfizz's behaviour
as measured by critic 1 (velocity gain 40*log10(vel/127) dB, i.e. amplitude (vel/127)^2 at amp_veltrack 100).
Envelope shapes: linear attack; decay and release exponential, reaching -60 dB at the given time (decay towards
the sustain level). Resampling: 4-point cubic Hermite interpolation.
"""
import os, re, struct
import numpy as np
import soundfile as sf
from scipy.signal import lfilter

NOTE = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}


def note_num(v):
    v = v.strip().lower()
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    m = re.fullmatch(r"([a-g])([#b]?)(-?\d+)", v)
    if not m:
        raise ValueError(f"bad note {v!r}")
    n = NOTE[m.group(1)] + (1 if m.group(2) == "#" else -1 if m.group(2) == "b" else 0)
    return 12 * (int(m.group(3)) + 1) + n


def _strip_comments(text):
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    return "\n".join(l.split("//")[0] if not l.lstrip().startswith("sample") else re.sub(r"\s//.*$", "", l)
                     for l in text.splitlines())


def _read_wav_loop(path):
    """Loop (start, end) frames from a RIFF smpl chunk, or None."""
    try:
        with open(path, "rb") as f:
            d = f.read()
    except OSError:
        return None
    if d[:4] != b"RIFF":
        return None
    i = 12
    while i + 8 <= len(d):
        cid = d[i:i + 4]; sz = struct.unpack("<I", d[i + 4:i + 8])[0]
        if cid == b"smpl" and sz >= 36:
            body = d[i + 8:i + 8 + sz]
            n = struct.unpack("<I", body[28:32])[0]
            if n >= 1 and len(body) >= 60:
                s, e = struct.unpack("<II", body[36 + 8:36 + 16])
                return int(s), int(e)
        i += 8 + sz + (sz & 1)
    return None


class Sample:
    def __init__(self, path):
        x, sr = sf.read(path, dtype="float32", always_2d=True)
        if x.shape[1] == 1:
            x = np.repeat(x, 2, axis=1)
        self.x = np.ascontiguousarray(x[:, :2].T)  # (2, frames)
        self.sr = sr
        self.loop = _read_wav_loop(path)
        self.n = self.x.shape[1]
        self._env = None

    def xfaded(self, ls, le, xf):
        """Copy of the sample whose last xf frames before the loop end are cross-faded (equal power) with the
        xf frames before the loop start, so the jump from loop end to loop start is seamless
        (SFZ opcode loop_crossfade, https://sfzformat.com/opcodes/loop_crossfade)."""
        k = ("xf", ls, le, xf)
        if k not in self.__dict__.setdefault("_xf", {}):
            x = self.x.copy()
            xf = min(xf, ls, le - ls)
            if xf > 8:
                t = np.linspace(0, 1, xf, dtype=np.float32)
                fin, fout = np.sqrt(t), np.sqrt(1 - t)
                x[:, le + 1 - xf:le + 1] = x[:, le + 1 - xf:le + 1] * fout + self.x[:, ls - xf:ls] * fin
            # r03: the 4-point interpolation reads up to two frames past the loop end; make them the frames after
            # the loop start, as played (r02 read the original frames after the loop end: one HF spike per cycle,
            # critic 2's bass clicks 1.857 s apart)
            k2 = min(3, self.n - 1 - le)
            if k2 > 0:
                x[:, le + 1:le + 1 + k2] = self.x[:, ls:ls + k2]
            self._xf[k] = x
        return self._xf[k]

    def time_to(self, db):
        """Seconds from the sample start until its 10 ms RMS envelope first reaches (steady level + db); the
        steady level is the median envelope from 0.6 s to 2.0 s (or of the second half for shorter samples).
        r02 uses it to start short sustain notes past the slow swell of the SSO string samples
        (the 'sample start' / offset technique, SFZ opcode offset)."""
        if self._env is None:
            h = int(0.01 * self.sr)
            m = self.x.mean(0); k = len(m) // h
            self._env = 10 * np.log10((m[:k * h].reshape(k, h) ** 2).mean(1) + 1e-20)
        e = self._env
        a, b = (60, 200) if len(e) > 220 else (len(e) // 2, len(e))
        steady = float(np.median(e[a:b]))
        idx = np.nonzero(e >= steady + db)[0]
        return 0.01 * float(idx[0]) if len(idx) else 0.0


class Sfz:
    _samples = {}

    def __init__(self, path, overrides=None):
        self.path = path
        self.regions = []
        self._parse(path, overrides or {})
        self.rr = {}

    # ---------------- parsing
    def _expand(self, path, defines):
        text = _strip_comments(open(path, encoding="utf-8", errors="replace").read())
        out = []
        for line in text.splitlines():
            m = re.match(r"\s*#define\s+(\$\w+)\s+(.*)$", line)
            if m:
                defines[m.group(1)] = m.group(2).strip(); continue
            m = re.match(r'\s*#include\s+"(.*)"', line)
            if m:
                out.append(self._expand(os.path.join(os.path.dirname(path), m.group(1).replace("\\", "/")), defines)); continue
            for k, v in sorted(defines.items(), key=lambda kv: -len(kv[0])):
                line = line.replace(k, v)
            out.append(line)
        return "\n".join(out)

    def _parse(self, path, overrides):
        text = self._expand(path, {})
        base = os.path.dirname(os.path.abspath(path))
        default_path = ""
        level = {"global": {}, "master": {}, "group": {}}
        cur, cur_hdr = None, None
        toks = re.split(r"(<\w+>)", text)
        for tk in toks:
            h = re.fullmatch(r"<(\w+)>", tk)
            if h:
                if cur_hdr == "region" and cur is not None:
                    self._add_region(cur, level, base, default_path, overrides)
                cur_hdr = h.group(1)
                if cur_hdr in ("global", "master", "group"):
                    level[cur_hdr] = {}
                    if cur_hdr == "global":
                        level["master"] = {}; level["group"] = {}
                    if cur_hdr == "master":
                        level["group"] = {}
                    cur = level[cur_hdr]
                elif cur_hdr == "region":
                    cur = {}
                else:
                    cur = {}  # control / curve / effect
                continue
            ops = _opcodes(tk)
            if cur_hdr == "control":
                if "default_path" in ops:
                    default_path = ops["default_path"].replace("\\", "/")
                continue
            if cur is not None:
                cur.update(ops)
        if cur_hdr == "region" and cur is not None:
            self._add_region(cur, level, base, default_path, overrides)

    def _add_region(self, reg, level, base, default_path, overrides):
        r = {}
        for k in ("global", "master", "group"):
            r.update(level[k])
        r.update(reg); r.update(overrides)
        if "sample" not in r:
            return
        sp = (default_path + r["sample"]).replace("\\", "/")
        r["_path"] = os.path.normpath(os.path.join(base, sp))
        if "key" in r:
            k = note_num(r["key"]); r.setdefault("lokey", str(k)); r.setdefault("hikey", str(k)); r.setdefault("pitch_keycenter", str(k))
        self.regions.append(r)

    # ---------------- helpers
    @classmethod
    def sample(cls, path):
        if path not in cls._samples:
            cls._samples[path] = Sample(path)
        return cls._samples[path]

    def sample_paths(self):
        return sorted(set(r["_path"] for r in self.regions))

    def select(self, key, vel, trigger="attack"):
        """Regions sounding for (key, velocity), with their crossfade gains; advances the round robin.
        r03: trigger 'attack' (note-on regions) or 'release' (regions with trigger=release, played at note-off;
        r02 played them at note-on)."""
        cand = []
        for r in self.regions:
            if (r.get("trigger", "attack") == "release") != (trigger == "release"):
                continue
            lo = note_num(r.get("lokey", "0")); hi = note_num(r.get("hikey", "127"))
            if not (lo <= key <= hi):
                continue
            if not (int(r.get("lovel", 0)) <= vel <= int(r.get("hivel", 127))):
                continue
            cand.append(r)
        if not cand:
            return []
        # round robin: one counter per key (and trigger) for this instrument
        c = self.rr.get((key, trigger), 0); self.rr[(key, trigger)] = c + 1
        out = []
        for r in cand:
            sl = int(r.get("seq_length", 1)); sp = int(r.get("seq_position", 1))
            if sl > 1 and (c % sl) + 1 != sp:
                continue
            g = 1.0
            g *= _xf(vel, r, "xfin_lovel", "xfin_hivel", True) * _xf(vel, r, "xfout_lovel", "xfout_hivel", False)
            g *= _xf(key, r, "xfin_lokey", "xfin_hikey", True, note=True) * _xf(key, r, "xfout_lokey", "xfout_hikey", False, note=True)
            if g > 0:
                out.append((r, g))
        return out


def _opcodes(text):
    """key=value pairs; values may contain spaces (sample paths): a value runs until the next 'name='."""
    out = {}
    ms = list(re.finditer(r"(?:(?<=\s)|^)([A-Za-z_][A-Za-z0-9_]*)=", text))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        val = text[m.end():end].strip()
        if m.group(1) != "sample":
            val = val.split()[0] if val.split() else ""
        else:
            val = val.splitlines()[0].strip() if val else ""
        out[m.group(1)] = val
    return out


def _xf(v, r, klo, khi, fade_in, note=False):
    if klo not in r and khi not in r:
        return 1.0
    conv = note_num if note else int
    lo = conv(r.get(klo, "0")); hi = conv(r.get(khi, "127"))
    if hi <= lo:
        x = 1.0 if v >= hi else 0.0
    else:
        x = min(1.0, max(0.0, (v - lo) / (hi - lo)))
    return float(np.sqrt(x if fade_in else 1 - x))  # power (equal-power) curve, the SFZ default


def _f(r, k, d=0.0):
    try:
        return float(r.get(k, d))
    except ValueError:
        return d


def peaking(f0, bw_oct, gain_db, sr):
    """RBJ audio-EQ-cookbook peaking filter (https://www.w3.org/TR/audio-eq-cookbook/)."""
    A = 10 ** (gain_db / 40); w0 = 2 * np.pi * f0 / sr
    alpha = np.sin(w0) * np.sinh(np.log(2) / 2 * bw_oct * w0 / np.sin(w0))
    b = np.array([1 + alpha * A, -2 * np.cos(w0), 1 - alpha * A]); a = np.array([1 + alpha / A, -2 * np.cos(w0), 1 - alpha / A])
    return b / a[0], a / a[0]


def lowpass2(fc, sr, q=0.7071):
    w0 = 2 * np.pi * min(fc, 0.45 * sr) / sr; alpha = np.sin(w0) / (2 * q)
    b = np.array([(1 - np.cos(w0)) / 2, 1 - np.cos(w0), (1 - np.cos(w0)) / 2]); a = np.array([1 + alpha, -2 * np.cos(w0), 1 - alpha])
    return b / a[0], a / a[0]


DEFAULT_LOOP_XF = 0.1


def random_loop(smp, lp, offset, n, ratio, lr, rng):
    """Source signal for a looped voice built from random segments of the loop region [ls, le]: the sample up to a
    random point in the loop, then segments of seg_s (min, max) seconds from random starts, each joined with an
    equal-power crossfade of xf_s seconds. Returns (source array (2, m), read positions for n output samples)."""
    ls, le = lp
    sr = smp.sr
    xf = int(lr.get("xf_s", 0.2) * sr)
    smin, smax = [int(v * sr) for v in lr.get("seg_s", (1.0, 2.0))]
    smax = min(smax, le - ls - 1); smin = min(smin, smax)
    need = offset + int(n * ratio) + 8
    first_end = int(rng.integers(min(ls + smin, le), le + 1)) if le > ls + smin else le
    parts = [smp.x[:, :first_end].copy()]
    total = first_end
    t = np.linspace(0, 1, xf, dtype=np.float32)
    fin, fout = np.sqrt(t), np.sqrt(1 - t)
    while total < need:
        L = int(rng.integers(smin, smax + 1))
        a = int(rng.integers(ls + xf, max(ls + xf + 1, le - L)))
        seg = smp.x[:, a - xf:a + L].copy()
        prev = parts[-1]
        if prev.shape[1] >= xf:
            prev[:, -xf:] = prev[:, -xf:] * fout + seg[:, :xf] * fin
            seg = seg[:, xf:]
        parts.append(seg); total += seg.shape[1]
    src = np.concatenate(parts, axis=1)
    pos = offset + np.arange(n, dtype=np.float64) * ratio
    return src, np.minimum(pos, src.shape[1] - 1)


def hermite(x, pos):
    """4-point cubic Hermite interpolation of x (channels, frames) at fractional positions pos."""
    i = np.floor(pos).astype(np.int64); f = (pos - i).astype(np.float32)
    n = x.shape[1]
    im1 = np.clip(i - 1, 0, n - 1); i0 = np.clip(i, 0, n - 1); i1 = np.clip(i + 1, 0, n - 1); i2 = np.clip(i + 2, 0, n - 1)
    y0, y1, y2, y3 = x[:, im1], x[:, i0], x[:, i1], x[:, i2]
    c1 = 0.5 * (y2 - y0); c2 = y0 - 2.5 * y1 + 2 * y2 - 0.5 * y3; c3 = 0.5 * (y3 - y0) + 1.5 * (y1 - y2)
    return ((c3 * f + c2) * f + c1) * f + y1


def render_voice(r, g_xf, key, vel, dur, sr, rng, env_over=None):
    """One voice: returns (start_delay_s, stereo float32 array (2, n)). dur = seconds until note-off (None = one-shot)."""
    env_over = env_over or {}
    smp = Sfz.sample(r["_path"])
    v = vel / 127.0
    # pitch
    kc = note_num(r.get("pitch_keycenter", str(key)))
    cents = (key - kc) * _f(r, "pitch_keytrack", 100) + 100 * _f(r, "transpose") + _f(r, "tune")
    pr = _f(r, "pitch_random")
    if pr:
        cents += rng.uniform(-pr, pr) / 2
    ratio = 2 ** (cents / 1200) * smp.sr / sr
    # amplitude
    vt = _f(r, "amp_veltrack", 100) / 100
    amp = (1 - vt) + vt * v * v if vt >= 0 else (1 + vt) - vt * (1 - v) ** 2
    vol = _f(r, "volume") + (rng.uniform(0, _f(r, "amp_random")) if _f(r, "amp_random") else 0)
    amp *= 10 ** (vol / 20) * g_xf
    pan = _f(r, "pan") / 100
    gl, gr = (1.0, 1.0)
    if pan:
        th = (pan + 1) * np.pi / 4
        gl, gr = np.cos(th) * np.sqrt(2), np.sin(th) * np.sqrt(2)
        m = max(gl, gr); gl, gr = gl / m, gr / m
    # timing
    delay = _f(r, "delay") + (rng.uniform(0, _f(r, "delay_random")) if _f(r, "delay_random") else 0)
    offset = int(_f(r, "offset")) + int(env_over.get("offset_s", 0) * smp.sr)
    if "skip_db" in env_over:
        offset += int(min(smp.time_to(env_over["skip_db"]), env_over.get("skip_max_s", 0.4)) * smp.sr)
    # envelope parameters
    def ep(name, d):
        return max(0.0, _f(r, "ampeg_" + name, d) + _f(r, "ampeg_vel2" + name) * v)
    e_delay, att, hold, dec = ep("delay", 0), ep("attack", 0), ep("hold", 0), ep("decay", 0)
    sus = min(1.0, ep("sustain", 100) / 100); rel = ep("release", 0.001)
    if "attack" in env_over:
        att = env_over["attack"]
    if "release" in env_over:
        rel = env_over["release"]
    if "release_scale" in env_over:
        rel *= env_over["release_scale"]
    rel = max(rel, 0.005)
    mode = r.get("loop_mode")
    lp = None
    if "loop_start" in r and "loop_end" in r:
        lp = (int(r["loop_start"]), int(r["loop_end"]))
    elif smp.loop:
        lp = smp.loop
    if mode is None:
        mode = "loop_continuous" if lp else "no_loop"
    if mode == "one_shot":
        dur = None
    looping = mode in ("loop_continuous", "loop_sustain") and lp is not None and lp[1] > lp[0] + 16
    # length of the voice in output samples
    rel_tail = rel  # -60 dB at 'rel' seconds
    if dur is None:
        t_end = (smp.n - offset) / (ratio * sr)
    else:
        t_end = dur + rel_tail
        if not looping:
            t_end = min(t_end, (smp.n - offset) / (ratio * sr))
    t_end = max(t_end, 0.002)
    n = int(t_end * sr) + 1
    pos = offset + np.arange(n, dtype=np.float64) * ratio
    if looping:
        ls, le = lp
        over = pos > le
        pos[over] = ls + np.mod(pos[over] - ls, le - ls + 1)
    pos = np.minimum(pos, smp.n - 1)
    # r03 (critic 2, plan 7): every looped sustain gets an equal-power loop crossfade (default 0.1 s), not only the
    # timpani roll; r02's bass loop seams clicked
    xfs = env_over.get("loop_crossfade", _f(r, "loop_crossfade", DEFAULT_LOOP_XF))
    lr = env_over.get("loop_random")
    if looping and lr:
        # r03 (critic 2, plan 2): long recorded rolls repeated their 3-5 s loop audibly; instead of cycling one loop,
        # chain random segments of the loop region with equal-power crossfades (a new segment start each time)
        src, pos = random_loop(smp, lp, offset, n, ratio, lr, rng)
    else:
        src = smp.xfaded(lp[0], lp[1], int(xfs * smp.sr)) if looping else smp.x
    y = hermite(src, pos)
    # envelope
    t = np.arange(n, dtype=np.float32) / sr
    env = np.ones(n, np.float32)
    ta = t - e_delay
    env[ta < 0] = 0
    if offset > 0:
        att = max(att, 0.003)  # r03: a sample started at an offset gets at least a 3 ms fade-in (no click)
    if att > 0:
        m = (ta >= 0) & (ta < att); env[m] = ta[m] / att
    t_dec0 = e_delay + att + hold
    if dec > 0 or sus < 1:
        m = t >= t_dec0
        if dec > 0:
            env[m] = sus + (1 - sus) * 10 ** (-3 * (t[m] - t_dec0) / dec)
        else:
            env[m] = sus
    if dur is not None:
        k = int(dur * sr)
        if k < n:
            lvl = env[k] if k < n else 0
            env[k:] = lvl * 10 ** (-3 * (t[k:] - dur) / rel)
    if looping and lr and lr.get("drift_dB"):
        # slow random level drift (a real roll is never perfectly even)
        k = max(2, int(t_end / lr.get("drift_s", 1.5)) + 2)
        pts = rng.uniform(-1, 1, k) * lr["drift_dB"]
        env *= (10 ** (np.interp(t, np.linspace(0, t_end, k), pts) / 20)).astype(np.float32)
    y *= env[None, :] * np.float32(amp)
    if gl != 1.0 or gr != 1.0:
        y[0] *= gl; y[1] *= gr
    # filters
    for q in (1, 2, 3):
        if f"eq{q}_gain" in r and _f(r, f"eq{q}_gain") != 0:
            b, a = peaking(_f(r, f"eq{q}_freq", 1000), _f(r, f"eq{q}_bw", 1), _f(r, f"eq{q}_gain"), sr)
            y = lfilter(b, a, y, axis=1).astype(np.float32)
    if "cutoff" in r:
        fc = _f(r, "cutoff") * 2 ** (_f(r, "fil_veltrack") * v / 1200)
        b, a = lowpass2(fc, sr)
        y = lfilter(b, a, y, axis=1).astype(np.float32)
    return delay, y


def render(sfz, notes, sr, length_s, seed=0, env_over=None):
    """notes: list of (t_on_s, t_off_s or None, key, velocity[, per-note env overrides dict]).
    Returns float32 array (n, 2)."""
    rng = np.random.default_rng(seed)
    n_out = int(length_s * sr) + 1
    out = np.zeros((2, n_out), np.float32)
    active_groups = []  # (group id, start sample, voice end) for off_by choke (applied as a fast fade)
    voices = []
    for nt in sorted(notes, key=lambda z: z[0]):
        t0, t1, key, vel = nt[:4]
        eo = dict(env_over or {})
        if len(nt) > 4 and nt[4]:
            eo.update(nt[4])
        for r, g in sfz.select(key, vel):
            dur = None if t1 is None else max(0.005, t1 - t0)
            d, y = render_voice(r, g, key, vel, dur, sr, rng, eo)
            a = int(round((t0 + d) * sr))
            voices.append((a, y, r.get("group"), r.get("off_by")))
        if t1 is not None and not eo.get("no_release_trigger"):
            # r03: release-triggered regions (e.g. the closing stroke of a VPO timpani roll) start at note-off
            ro = {k: v for k, v in eo.items() if k in ("release_trigger_gain_dB",)}
            for r, g in sfz.select(key, vel, "release"):
                g = g * 10 ** (ro.get("release_trigger_gain_dB", 0.0) / 20)
                d, y = render_voice(r, g, key, vel, None, sr, rng, {})
                a = int(round((t1 + d) * sr))
                voices.append((a, y, r.get("group"), r.get("off_by")))
    # choke: a voice whose off_by equals a later voice's group fades out over 10 ms at that voice's start
    starts_by_group = {}
    for a, y, grp, ob in voices:
        if grp is not None:
            starts_by_group.setdefault(grp, []).append(a)
    for a, y, grp, ob in voices:
        if ob is not None and ob in starts_by_group:
            later = [s for s in starts_by_group[ob] if s > a]
            if later:
                k = min(later) - a
                if k < y.shape[1]:
                    f = int(0.01 * sr)
                    y[:, k:k + f] *= np.linspace(1, 0, min(f, y.shape[1] - k), dtype=np.float32)[None, :]
                    y[:, k + f:] = 0
        b = min(n_out, a + y.shape[1])
        if b > a >= 0:
            out[:, a:b] += y[:, :b - a]
    return out.T

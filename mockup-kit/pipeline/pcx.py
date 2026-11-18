"""Perceived attack and legato-transition timing on harmonic bands with exclusion bands (mvt1 c42, critic A #1).

Usage: pcx.py RENDER_DIR PARTS [--tracks "Violins I" ...] [--synthetic] [--json FILE]
  RENDER_DIR  a render folder (stems named NN_<track>.wav as parts.json orders the tracks); PARTS the parts.json the render
              was made from (cycles/cNN/rendered_build/parts.json)
  --tracks    the tracks to scan (default: every string track with legato rows)
  --synthetic also measure a synthetic instant switch between the same two pitches for every join (the estimator's own error)
  --json      write every join's values to FILE

Why: the m37 estimator (cycles/c37/actor_scripts/m37.py, used for S2 and the per-onset leads of c27/c37) takes each
harmonic +-max(1.5 %, 1 FFT bin); under 220 Hz one bin of its 4096/8192-point FFT is wider than a semitone, and at any
FFT size harmonics in small-number ratios (9:8, 4:3, 3:2) fall inside each other's +-1.5 %, so each pitch's band holds the
other pitch's partials. On a synthetic instant switch it reads up to 0.6 s of "both pitches sounding" on violas and celli
and puts 24-32 % of perfect attacks more than 60 ms off. Here a pitch's band leaves out every bin within EXCL_BINS of any
harmonic of the other pitch, and the FFT is the shortest (2048, 4096, 8192) at which at least MIN_HARM harmonics of the
measured pitch keep a bin. Synthetic error: robust SD 3-4 ms.

Functions (any score; times in seconds of the stem, x = float32 stereo array at SR):
  attack_pcx(x, tm, ts, ln, pitch, prev_pitch=None)  perceived attack: floor = minimum in [tm - 0.12, ts + 0.06], reference =
      30 ms maximum in [tm, ts + min(ln, 0.45)], t50 = first crossing of half the amplitude between them, h10 = first
      crossing of reference - 10 dB, pc = mean of t50 and h10, seconds re ts (score onset); tm = moved onset, ln = played
      length (s). prev_pitch: the pitch sounding before (its harmonics are excluded); None = no exclusion.
  pair_window(x, tm, ts, te, p_old, p_new)  crossover (new band reaches old band, from tm - 0.1) re ts and the contiguous
      time around it during which the two exclusion bands are within 6 dB.
  legato_joins(track)  monophonic legato joins of a parts.json track: a note on a legato row ("Leg" or a LEG_ROWS_EXTRA row)
      whose moved onset falls inside exactly one other sounding note of another pitch.
  synth_switch(p_old, p_new, t_sw, t0, t1, seed)  the synthetic instant switch (harmonics 1-40 at k^-0.8, three chorus voices
      +-6 cents with 5.5-6.2 Hz +-12-cent vibrato, 5 ms crossfade at t_sw), stereo, covering [t0, t1].
"""
import bisect, json, os, sys
import numpy as np

SR = 48000
EXCL_BINS = 2
MIN_HARM = 2
NFFTS = (2048, 4096, 8192)
LEG_ROWS_EXTRA = ("Slur Runs",)


class TM:
    """seconds of a score qn on a parts.json tempo map ([[qn, bpm], ...], square steps; renders are on score time)."""

    def __init__(self, tempo):
        self.pts = sorted((float(q), float(b)) for q, b in tempo)
        self.q = [x for x, _ in self.pts]
        self.t = [0.0]
        for (q0, b0), (q1, _) in zip(self.pts, self.pts[1:]):
            self.t.append(self.t[-1] + (q1 - q0) * 60.0 / b0)

    def sec(self, q):
        i = max(0, bisect.bisect_right(self.q, q) - 1)
        return self.t[i] + (q - self.q[i]) * 60.0 / self.pts[i][1]


def f0(p):
    return 440.0 * 2 ** ((p - 69) / 12.0)


def harmonics(pitch):
    return range(2, 9) if f0(pitch) < 110 else range(1, 7)


def band_mask(pitch, nfft, other=None, excl=EXCL_BINS):
    """bins of pitch's harmonic bands (+-max(1.5 %, 1 bin)); with other, every bin within excl bins of any harmonic of
    other is left out. Returns (mask, number of harmonics that keep at least one bin)."""
    freqs = np.fft.rfftfreq(nfft, 1 / SR)
    fp = f0(pitch)
    m = np.zeros(len(freqs), bool)
    per = []
    for k in harmonics(pitch):
        mk = (freqs > k * fp * 0.985) & (freqs < k * fp * 1.015)
        j = int(round(k * fp * nfft / SR))
        mk[max(0, j - 1):j + 2] = True
        per.append(mk)
    if other is not None:
        fo = f0(other)
        hi = max(harmonics(pitch)) * fp * 1.1 + (excl + 2) * SR / nfft
        ex = np.zeros(len(freqs), bool)
        for j in range(1, int(hi / fo) + 2):
            b = int(round(j * fo * nfft / SR))
            ex[max(0, b - excl):b + excl + 1] = True
        per = [mk & ~ex for mk in per]
    for mk in per:
        m |= mk
    return m, sum(1 for mk in per if mk.any())


def choose_nfft(pitch, other=None):
    for n in NFFTS:
        if band_mask(pitch, n, other)[1] >= MIN_HARM:
            return n
    return NFFTS[-1]


def _spec_frames(x, t0, t1, nfft, hop, x0=0.0):
    a, b = int(round((t0 - x0) * SR)) - nfft // 2, int(round((t1 - x0) * SR)) + nfft // 2
    seg = np.zeros((b - a, 2), np.float32)
    s0, s1 = max(0, a), min(len(x), b)
    if s1 > s0:
        seg[s0 - a:s1 - a] = x[s0:s1]
    h = int(hop * SR)
    starts = np.arange(0, len(seg) - nfft, h)
    win = np.hanning(nfft)
    S = 0
    for ch in (0, 1):
        fr = np.lib.stride_tricks.sliding_window_view(seg[:, ch], nfft)[::h][:len(starts)]
        S = S + np.abs(np.fft.rfft(fr * win, axis=1)) ** 2
    t = x0 + a / SR + (starts + nfft / 2) / SR
    return t, S / 2


def band_env(x, t0, t1, pitch, other=None, nfft=None, hop=0.002, box=0.010, x0=0.0):
    """harmonic-band level (dB) of pitch over [t0, t1], other's harmonics excluded (x0: stem time of x[0])."""
    nfft = nfft or choose_nfft(pitch, other)
    m, _ = band_mask(pitch, nfft, other)
    t, S = _spec_frames(x, t0, t1, nfft, hop, x0)
    e = S[:, m].sum(axis=1)
    k = max(1, int(box / hop))
    e = np.convolve(e, np.ones(k) / k, mode="same")
    return t, 10 * np.log10(e + 1e-20), nfft


def _pc_from_env(t, e, tm, ts, ln):
    fl_m = (t >= tm - 0.12) & (t <= ts + 0.06)
    if not fl_m.any():
        return None
    i_fl = np.where(fl_m)[0][np.argmin(e[fl_m])]
    rf_m = (t >= tm) & (t <= ts + min(ln, 0.45))
    e30 = np.convolve(e, np.ones(15) / 15, mode="same")
    ref = e30[rf_m].max() if rf_m.any() else e.max()
    fl = e[i_fl]
    if ref - fl < 3:
        return {"t50": None, "h10": None, "pc": None, "rise": round(float(ref - fl), 1)}
    amp_half = 20 * np.log10((10 ** (fl / 20) + 10 ** (ref / 20)) / 2)
    after = np.arange(len(t)) >= i_fl
    c50 = np.where(after & (e >= amp_half))[0]
    c10 = np.where(after & (e >= ref - 10))[0]
    t50 = float(t[c50[0]] - ts) if len(c50) else None
    h10 = float(t[c10[0]] - ts) if len(c10) else None
    pc = (t50 + h10) / 2 if t50 is not None and h10 is not None else None
    return {"t50": t50, "h10": h10, "pc": pc, "rise": round(float(ref - fl), 1)}


def attack_pcx(x, tm, ts, ln, pitch, prev_pitch=None, x0=0.0):
    t, e, nfft = band_env(x, tm - 0.25, ts + 0.6, pitch, prev_pitch, x0=x0)
    r = _pc_from_env(t, e, tm, ts, ln)
    if r is not None:
        r["nfft"] = nfft
    return r


def attack_m37(x, tm, ts, ln, pitch, x0=0.0):
    """the c37 estimator, for comparison (no exclusion; nfft 8192 under 110 Hz, 4096 under 220 Hz, else 2048)."""
    fp = f0(pitch)
    nfft = 8192 if fp < 110 else (4096 if fp < 220 else 2048)
    t, e, _ = band_env(x, tm - 0.25, ts + 0.6, pitch, None, nfft=nfft, x0=x0)
    return _pc_from_env(t, e, tm, ts, ln)


def pair_window(x, tm, ts, te, p_old, p_new, exclude=True, x0=0.0):
    """crossover and both-within-6-dB window (s re ts). exclude=False: the c41 C method (each pitch's m37 band, no
    exclusion, the m37 FFT size of each pitch)."""
    t0, t1 = tm - 0.2, min(te, ts + 0.8)
    if exclude:
        n = max(choose_nfft(p_new, p_old), choose_nfft(p_old, p_new))
        to, eo, _ = band_env(x, t0, t1, p_old, p_new, nfft=n, x0=x0)
        tn_, en, _ = band_env(x, t0, t1, p_new, p_old, nfft=n, x0=x0)
    else:
        nf = lambda p: 8192 if f0(p) < 110 else (4096 if f0(p) < 220 else 2048)
        to, eo, _ = band_env(x, t0, t1, p_old, None, nfft=nf(p_old), x0=x0)
        tn_, en, _ = band_env(x, t0, t1, p_new, None, nfft=nf(p_new), x0=x0)
        if len(to) != len(tn_) or np.any(np.abs(to - tn_) > 1e-6):
            eo = np.interp(tn_, to, eo)
    t = tn_
    after = t >= tm - 0.1
    cross = np.where(after & (en >= eo))[0]
    if not len(cross):
        return None
    ic = cross[0]
    d = np.abs(en - eo) <= 6
    i0 = ic
    while i0 > 0 and d[i0 - 1]:
        i0 -= 1
    i1 = ic
    while i1 < len(t) - 1 and d[i1 + 1]:
        i1 += 1
    win = float(t[i1] - t[i0]) if d[ic] else 0.0
    return {"cross": float(t[ic] - ts), "win": win}


def is_leg(art):
    return "Leg" in (art or "") or any(r in (art or "") for r in LEG_ROWS_EXTRA)


def legato_joins(track):
    ks = sorted(track.get("ks", []), key=lambda k: k["qn"])

    def art_at(q):
        a = track.get("first_art")
        for k in ks:
            if k["qn"] <= q + 1e-6:
                a = k["art"]
            else:
                break
        return a or ""
    ns = sorted(track["notes"], key=lambda n: n["qn"])
    out = []
    for n in ns:
        if not is_leg(art_at(n["qn"])):
            continue
        sounding = [m for m in ns if m is not n and m["qn"] < n["qn"] - 1e-4 and m["qn"] + m["dur"] > n["qn"] + 1e-4]
        same = [m for m in ns if m is not n and abs(m["qn"] - n["qn"]) < 0.02]
        if len(sounding) != 1 or same or sounding[0]["pitch"] == n["pitch"]:
            continue
        out.append((sounding[0], n))
    return out


def synth_switch(p_old, p_new, t_sw, t0, t1, seed=0, xfade=0.005):
    rng = np.random.default_rng(seed)
    n = int(round((t1 - t0) * SR))
    tt = t0 + np.arange(n) / SR
    out = np.zeros((n, 2), np.float32)
    g = np.clip((tt - (t_sw - xfade / 2)) / xfade, 0, 1)
    for p, w in ((p_old, 1 - g), (p_new, g)):
        fp = f0(p)
        for ch in (0, 1):
            sig = np.zeros(n)
            for det in (-6, 0, 6):
                rate = rng.uniform(5.5, 6.2)
                ph = rng.uniform(0, 2 * np.pi)
                cents = det + 12 * np.sin(2 * np.pi * rate * tt + ph)
                inst = fp * 2 ** (cents / 1200)
                phase = 2 * np.pi * np.cumsum(inst) / SR + rng.uniform(0, 2 * np.pi)
                for k in range(1, 41):
                    if k * fp * 1.01 >= SR / 2:
                        break
                    sig += k ** -0.8 * np.sin(k * phase + rng.uniform(0, 2 * np.pi))
            out[:, ch] += (0.02 * w * sig).astype(np.float32)
    return out


def robust_sd(z):
    z = np.asarray([v for v in z if v is not None], float)
    return float(1.4826 * np.median(np.abs(z - np.median(z)))) if len(z) else float("nan")


def stem_path(render_dir, parts, name):
    names = [t["name"] for t in parts["tracks"]]
    i = names.index(name) + 1
    f = f"{render_dir}/{i:02d}_{name}.wav"
    if os.path.exists(f):
        return f
    import glob
    c = glob.glob(f"{render_dir}/*_{name}.wav")
    return c[0] if c else None


def scan(render_dir, parts, tn, synthetic=False):
    import soundfile as sf
    tm_ = TM(parts["tempo"])
    T = {t["name"]: t for t in parts["tracks"]}[tn]
    x, sr = sf.read(stem_path(render_dir, parts, tn), dtype="float32", always_2d=True)
    assert sr == SR
    rows = []
    for k, (p, n) in enumerate(legato_joins(T)):
        tm, ts = tm_.sec(n["qn"]), tm_.sec(n["sq"])
        te = tm_.sec(n["qn"] + n["dur"])
        ln = te - tm
        a = attack_pcx(x, tm, ts, ln, n["pitch"], p["pitch"]) or {}
        w = pair_window(x, tm, ts, te, p["pitch"], n["pitch"]) or {}
        row = {"sq": n["sq"], "pitch": n["pitch"], "prev": p["pitch"], "lead_s": round(ts - tm, 3), "pcx": a.get("pc"),
               "rise": a.get("rise"), "cross": w.get("cross"), "win": w.get("win")}
        if synthetic:
            t0 = tm - 0.6
            y = synth_switch(p["pitch"], n["pitch"], ts, t0, ts + 1.2, seed=k)
            sa = attack_pcx(y, tm, ts, ln, n["pitch"], p["pitch"], x0=t0) or {}
            sw = pair_window(y, tm, ts, min(te, ts + 1.1), p["pitch"], n["pitch"], x0=t0) or {}
            row["syn_pcx"] = sa.get("pc")
            row["syn_win"] = sw.get("win")
        rows.append(row)
    return rows


def summary(tn, rows):
    pcs = [r["pcx"] for r in rows if r["pcx"] is not None]
    med = float(np.median(pcs)) if pcs else float("nan")
    off = float(np.mean([abs(v - med) > 0.06 for v in pcs])) if pcs else float("nan")
    wins = [r["win"] for r in rows if r.get("win") is not None]
    s = (f"{tn:14s} joins {len(rows):3d}  pcX median {med * 1000:+5.0f} ms  robust SD {robust_sd(pcs) * 1000:4.0f} ms  "
         f">60 ms off {off * 100:3.0f}%  window median {np.median(wins) * 1000 if wins else float('nan'):4.0f} ms")
    if rows and "syn_pcx" in rows[0]:
        sp = [r["syn_pcx"] for r in rows if r.get("syn_pcx") is not None]
        sw = [r["syn_win"] for r in rows if r.get("syn_win") is not None]
        s += f"  | synthetic: pcX rSD {robust_sd(sp) * 1000:3.0f} ms, window median {np.median(sw) * 1000:3.0f} ms"
    return s, med, robust_sd(pcs), off


def main():
    a = sys.argv[1:]
    rd, pj = a[0], a[1]
    parts = json.load(open(pj))
    tracks = []
    if "--tracks" in a:
        i = a.index("--tracks") + 1
        while i < len(a) and not a[i].startswith("--"):
            tracks.append(a[i]); i += 1
    if not tracks:
        tracks = [t["name"] for t in parts["tracks"] if t.get("family") == "string" and not t.get("test")
                  and legato_joins(t)]
    out = {}
    for tn in tracks:
        rows = scan(rd, parts, tn, synthetic="--synthetic" in a)
        out[tn] = rows
        print(summary(tn, rows)[0])
    if "--json" in a:
        json.dump(out, open(a[a.index("--json") + 1], "w"), indent=0, default=float)


if __name__ == "__main__":
    main()

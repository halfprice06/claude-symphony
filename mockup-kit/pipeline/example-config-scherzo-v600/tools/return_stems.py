"""mvt1 c50: return-track stems in a cycle's render folders (tools/TEMPLATE-TOOLS.md).

REAPER renders every return track (build/mix.json "returns") as a stem named by its track number; in the main project
the returns come after the instrument tracks (e.g. "34_R Strings.wav", where parts.json track 34 is a pass-2 track).
Here each return stem gets a fixed number, 91.. in mix.json "returns" order, so every instrument stem keeps its
parts.json name and number and the return stems come last. A test copy ("<return> test", fed only by parts.json "test"
tracks in the pass-2 project) goes to cycles/cNN/test_stems/ and never into the master. Without "returns" in mix.json
nothing here does anything.

Where the master sum is computed:
  - main render: REAPER's own master mix (render/00_Master.wav) is the sum of every track routed to the master, i.e. the
    instrument tracks plus the returns (there are no master FX). render_cycle.py replaces it with the float sum of every
    stem in render/ (return stems included) when it reaches full scale.
  - --pass2: render_cycle.py rebuilds render/00_Master.wav as the float sum of every stem in render/: the main stems,
    the pass-2 stems, and each return stem, which merge_pass2() first makes the sum of the main project's return
    (kept in render_pass2/returns_main/) and the pass-2 project's return of the same name.
  - deliver_master.py reads render/00_Master.wav (then its optional master EQ, the ride and the limiter); measure.py
    measures it as the mix and lists the return stems in their own section.

Usage (the venv python: numpy, soundfile):
  return_stems.py rename RENDER_DIR MIX_JSON TEST_DIR
      the main render, after the pre-roll cut (render_cycle.py does this)
  return_stems.py fit RENDER_DIR PARTS_JSON MIX_JSON [--start S] [--dur D]
      send-level check: on a render made with "bypass": true on the returns (each return then outputs the plain sum of
      its sends), fit every return stem as a weighted sum of the instrument stems and print each weight in dB minus the
      return's fader: the send level each track actually had (post-fader sends make it exact)
"""
import glob, json, os, shutil, sys
import numpy as np
import soundfile as sf

FIRST = 91


def returns_of(mix_path):
    """{return name: stem number} in mix.json "returns" order (empty without returns)"""
    try:
        mix = json.load(open(mix_path))
    except (OSError, ValueError):
        return {}
    names = [k for k in (mix.get("returns") or {}) if not k.startswith("_")]
    return {k: FIRST + i for i, k in enumerate(names)}


def classify(name, rets):
    """(return, is_test) when a stem name is a return or a return's test copy, else None"""
    if name in rets:
        return name, False
    if name.endswith(" test") and name[:-5] in rets:
        return name[:-5], True
    return None


def _stems(d):
    return sorted(glob.glob(os.path.join(d, "[0-9][0-9]_*.wav")))


def rename(render_dir, rets, test_dir):
    n = 0
    for f in _stems(render_dir):
        name = os.path.basename(f)[3:-4]
        c = classify(name, rets)
        if not c:
            continue
        base, test = c
        dst = os.path.join(test_dir if test else render_dir, f"{rets[base]:02d}_{name}.wav")
        if os.path.abspath(f) == os.path.abspath(dst):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(f, dst)
        n += 1
        print(f"return stem {os.path.basename(f)} -> {os.path.relpath(dst, os.path.dirname(render_dir))}")
    return n


def _fit_len(x, n):
    if len(x) == n:
        return x
    print(f"length {len(x)} -> {n}")
    return np.pad(x, ((0, max(0, n - len(x))), (0, 0)))[:n]


def merge_pass2(C, R2, rets, n_main):
    """the pass-2 project's return stems (in R2) into cycles/cNN/render (summed with the main project's) or test_stems"""
    keep = os.path.join(R2, "returns_main")
    for f in _stems(R2):
        name = os.path.basename(f)[3:-4]
        c = classify(name, rets)
        if not c:
            continue
        base, test = c
        num = rets[base]
        x, sr = sf.read(f, dtype="float64", always_2d=True)
        x = _fit_len(x, n_main)
        if test:
            os.makedirs(os.path.join(C, "test_stems"), exist_ok=True)
            dst = os.path.join(C, "test_stems", f"{num:02d}_{name}.wav")
            sf.write(dst, x.astype("float32"), sr, subtype="FLOAT")
            print(f"pass-2 test return {os.path.basename(dst)} peak {float(np.abs(x).max()):.4f}")
            continue
        dst = os.path.join(C, "render", f"{num:02d}_{name}.wav")
        main_copy = os.path.join(keep, os.path.basename(dst))
        if not os.path.exists(main_copy) and os.path.exists(dst):
            os.makedirs(keep, exist_ok=True)
            shutil.copy2(dst, main_copy)
        how = "pass 2 only"
        if os.path.exists(main_copy):
            m, _ = sf.read(main_copy, dtype="float64", always_2d=True)
            x = x + _fit_len(m, n_main)
            how = "main + pass 2"
        sf.write(dst, x.astype("float32"), sr, subtype="FLOAT")
        print(f"pass-2 return {os.path.basename(dst)} ({how}) peak {float(np.abs(x).max()):.4f}")


def fit(render_dir, parts_path, mix_path, start=0.0, dur=None):
    rets = returns_of(mix_path)
    mix = json.load(open(mix_path))
    tracks = [t["name"] for t in json.load(open(parts_path))["tracks"]]
    dry = [(os.path.basename(f)[3:-4], f) for f in _stems(render_dir) if os.path.basename(f)[3:-4] in tracks]
    info = sf.info(dry[0][1])
    a = int(start * info.samplerate)
    b = info.frames if dur is None else min(info.frames, a + int(dur * info.samplerate))
    X = np.stack([sf.read(f, dtype="float64", always_2d=True, start=a, stop=b)[0] for _, f in dry])   # tracks x n x 2
    X = X.reshape(len(dry), -1)
    G = X @ X.T
    out = {}
    for f in _stems(render_dir):
        name = os.path.basename(f)[3:-4]
        if name not in rets:
            continue
        y = sf.read(f, dtype="float64", always_2d=True, start=a, stop=b)[0].reshape(-1)
        keep = np.flatnonzero(np.abs(X @ y) > 1e-12 * max(1.0, float(np.abs(X @ y).max())))
        w = np.zeros(len(dry))
        w[keep] = np.linalg.lstsq(G[np.ix_(keep, keep)], X[keep] @ y, rcond=None)[0]
        res = y - w @ X
        fader = float((mix["returns"][name] or {}).get("fader_db", 0.0))
        rows = {dry[i][0]: round(20 * np.log10(abs(w[i])) - fader, 2) for i in range(len(dry)) if abs(w[i]) > 1e-3}
        err = float(20 * np.log10(np.sqrt(np.mean(res ** 2)) / max(1e-12, np.sqrt(np.mean(y ** 2)))))
        out[name] = {"send_db": rows, "residual_db": round(err, 1)}
        print(f"{name} (fader {fader:+.2f} dB): residual {err:.1f} dB re the return; send levels:")
        for k, v in rows.items():
            print(f"   {k:20s} {v:+.2f} dB")
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "rename":
        n = rename(a[1], returns_of(a[2]), a[3])
        print(f"{n} return stems renumbered" if n else "no return stems to renumber")
    elif a and a[0] == "fit":
        fit(a[1], a[2], a[3], float(a[a.index("--start") + 1]) if "--start" in a else 0.0,
            float(a[a.index("--dur") + 1]) if "--dur" in a else None)
    else:
        print(__doc__)

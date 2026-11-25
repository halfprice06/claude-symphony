"""mvt2 c50 (ONE_TIME; copied from mvt1 c52, critic B #5): magnitude responses of mix.json EQ bands (RBJ cookbook biquads, ReaEQ-style bandwidth in
octaves; bells default 1 octave, shelves / filters 2), 48 kHz. Used by state_check.py to remove an EQ change from a
render-to-render level comparison. Critic B's simulator with these responses reproduced bal50 on the c51 stems to 0.0 dB
and predicted the c51 brass EQ change on 73 notes to a median -0.03 dB (cycles/c52/reports/B.md #5)."""
import numpy as np

SR = 48000


def _coef(band, hz, db=0.0, bw=None, sr=SR):
    w0 = 2 * np.pi * hz / sr
    A = 10 ** (db / 40)
    if bw is None:
        bw = 1.0 if band in ("bell", "bell2") else 2.0
    alpha = np.sin(w0) * np.sinh(np.log(2) / 2 * bw * w0 / np.sin(w0))
    c = np.cos(w0)
    if band in ("bell", "bell2"):
        b = [1 + alpha * A, -2 * c, 1 - alpha * A]
        a = [1 + alpha / A, -2 * c, 1 - alpha / A]
    elif band == "lowshelf":
        sA = 2 * np.sqrt(A) * alpha
        b = [A * ((A + 1) - (A - 1) * c + sA), 2 * A * ((A - 1) - (A + 1) * c), A * ((A + 1) - (A - 1) * c - sA)]
        a = [(A + 1) + (A - 1) * c + sA, -2 * ((A - 1) + (A + 1) * c), (A + 1) + (A - 1) * c - sA]
    elif band == "highshelf":
        sA = 2 * np.sqrt(A) * alpha
        b = [A * ((A + 1) + (A - 1) * c + sA), -2 * A * ((A - 1) + (A + 1) * c), A * ((A + 1) + (A - 1) * c - sA)]
        a = [(A + 1) - (A - 1) * c + sA, 2 * ((A - 1) - (A + 1) * c), (A + 1) - (A - 1) * c - sA]
    elif band == "highpass":
        b = [(1 + c) / 2, -(1 + c), (1 + c) / 2]
        a = [1 + alpha, -2 * c, 1 - alpha]
    elif band == "lowpass":
        b = [(1 - c) / 2, 1 - c, (1 - c) / 2]
        a = [1 + alpha, -2 * c, 1 - alpha]
    else:
        raise ValueError(band)
    return np.array(b), np.array(a)


def resp2(bands, f, sr=SR):
    """|H(f)|^2 of a list of mix.json bands (unknown band types are skipped)"""
    z = np.exp(-1j * 2 * np.pi * np.asarray(f, float) / sr)
    h = np.ones_like(z)
    for bd in bands or []:
        if not isinstance(bd, dict) or "band" not in bd:
            continue
        if bd.get("db", 0) == 0 and bd["band"] in ("bell", "bell2", "lowshelf", "highshelf"):
            continue
        try:
            b, a = _coef(bd["band"], float(bd["hz"]), float(bd.get("db", 0.0)), bd.get("bw_oct"), sr)
        except ValueError:
            continue
        h = h * (b[0] + b[1] * z + b[2] * z * z) / (a[0] + a[1] * z + a[2] * z * z)
    return np.abs(h) ** 2


_FAM_TYPES = {"hp": "highpass", "lp": "lowpass", "bell": "bell", "hshelf": "highshelf", "lshelf": "lowshelf"}


def track_bands(mix, m):
    """(bands on both channels, side-only bands) of a track's mix entry m (group defaults merged): the family EQ and
    "eq", and "side_shelf". mvt2 c50: in this folder "family_eq" is a list of bands in the entry itself, written
    {"type": hp|lp|bell|hshelf|lshelf, "hz", "db", "bw"} (build_reaper.py, mvt3 c06); they are converted here."""
    fe = m.get("family_eq") or []
    if isinstance(fe, str):
        fe = (mix.get("family_eqs") or {}).get(fe, [])
    fam = [{"band": _FAM_TYPES[b["type"]], "hz": b["hz"], "db": b.get("db", 0.0), "bw_oct": b.get("bw")}
           for b in fe if isinstance(b, dict) and b.get("type") in _FAM_TYPES]
    ss = m.get("side_shelf") or []
    if isinstance(ss, dict):
        ss = [dict(ss, band=ss.get("band", "lowshelf"))]
    return fam + list(m.get("eq") or []), list(ss)

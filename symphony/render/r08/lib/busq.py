"""r04: zero-phase mix-bus EQ (critic 3, plan item 4: spectral blend). RBJ audio-EQ-cookbook biquads
(https://www.w3.org/TR/audio-eq-cookbook/) designed at half the requested gain and run forward and backward
(scipy sosfiltfilt), so the net response is the requested gain with no phase shift.
eq: list of {"type": "bell" | "lowshelf" | "highshelf", "Hz": f0, "dB": gain, "Q": q (bell) / "S": slope (shelves)}."""
import numpy as np
from scipy.signal import sosfiltfilt, sosfreqz


def biquad(t, f0, db, sr, q=0.707, S=1.0):
    A = 10 ** (db / 40); w = 2 * np.pi * f0 / sr; cw, sw = np.cos(w), np.sin(w)
    if t == "bell":
        al = sw / (2 * q)
        b = [1 + al * A, -2 * cw, 1 - al * A]; a = [1 + al / A, -2 * cw, 1 - al / A]
    else:
        al = sw / 2 * np.sqrt((A + 1 / A) * (1 / S - 1) + 2); sA = 2 * np.sqrt(A) * al
        if t == "lowshelf":
            b = [A * ((A + 1) - (A - 1) * cw + sA), 2 * A * ((A - 1) - (A + 1) * cw), A * ((A + 1) - (A - 1) * cw - sA)]
            a = [(A + 1) + (A - 1) * cw + sA, -2 * ((A - 1) + (A + 1) * cw), (A + 1) + (A - 1) * cw - sA]
        else:
            b = [A * ((A + 1) + (A - 1) * cw + sA), -2 * A * ((A - 1) + (A + 1) * cw), A * ((A + 1) + (A - 1) * cw - sA)]
            a = [(A + 1) - (A - 1) * cw + sA, 2 * ((A - 1) - (A + 1) * cw), (A + 1) - (A - 1) * cw - sA]
    return np.array(b + a) / a[0]


def sos_of(eq, sr):
    return np.array([biquad(e["type"], e["Hz"], e["dB"] / 2, sr, e.get("Q", 0.707), e.get("S", 1.0)) for e in eq])


def apply(x, sr, eq):
    if not eq:
        return x
    return sosfiltfilt(sos_of(eq, sr), x, axis=0)


def power_response(eq, sr, f):
    """|H|^2 of the zero-phase chain at frequencies f (forward-backward = |H_half|^4)."""
    if not eq:
        return np.ones_like(f)
    w, h = sosfreqz(sos_of(eq, sr), worN=f, fs=sr)
    return np.abs(h) ** 4

"""c24 (critic C #3): phrase-scale loudness motion of a rendered file.

Usage: python motion.py <audio> [<audio> ...]
For each file, from ffmpeg's EBU R128 momentary (M, 400 ms) and short-term (S, 3 s) loudness at 10 Hz, over the frames
with S above -60 LUFS:
  - dS4 p90: the 90th percentile of |S(t + 4 s) - S(t)| (dB)
  - motion 1s/20s: the std of (power mean of M over 1 s) - (power mean of M over 20 s), 20 s trimmed at each end (dB)
c24 references (critic C, same method): Brahms 1/ii 8.55 / 4.56, Brahms 4/ii 6.29 / 3.92; c23 master 5.79 / 3.76,
c23 mp3 4.99 / 2.84. A fall of more than 0.2 dB from the previous cycle is a regression to justify in CHANGES.md.
"""
import re, subprocess, sys
import numpy as np


def series(path):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                          "ebur128=metadata=1,ametadata=print:file=-", "-f", "null", "-"],
                         capture_output=True, text=True).stdout.replace("-inf", "-70")
    M = [float(v) for v in re.findall(r"lavfi\.r128\.M=(-?[\d.]+|nan)", out)]
    S = [float(v) for v in re.findall(r"lavfi\.r128\.S=(-?[\d.]+|nan)", out)]
    n = min(len(M), len(S))
    return np.nan_to_num(np.array(M[:n]), nan=-70.0), np.nan_to_num(np.array(S[:n]), nan=-70.0)


def pmean(x, w):
    return 10 * np.log10(np.convolve(10 ** (x / 10), np.ones(w) / w, "same") + 1e-12)


def motion(path):
    M, S = series(path)
    act = S > -60
    M, S = M[act], S[act]
    dS = np.abs(S[40:] - S[:-40])
    d1 = pmean(M, 10) - pmean(M, 200)
    return float(np.percentile(dS, 90)), float(np.std(d1[200:-200]))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        a, b = motion(p)
        print(f"{p.split('/')[-1]}: dS4 p90 {a:.2f} dB, motion 1s/20s {b:.2f} dB")

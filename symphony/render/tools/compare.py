#!/usr/bin/env python3
"""Compare several measure.py result folders: markdown table to stdout and an LTAS/loudness overlay PNG.

Usage: python3 compare.py DIR1 DIR2 ... [--png out.png] [--md out.md]
Each DIR holds metrics.json (and loudness_series.csv) written by measure.py.
"""
import argparse, json, os, sys
import numpy as np


def row(d):
    L, P, S, St, B = d["loudness"], d["peaks"], d["spectrum"], d["stereo"], d.get("brightness", {})
    t = d.get("tails", {}).get("final") or {}
    sp = L["S_percentiles_rel_I"]
    return [d["label"], f'{d["duration_s"]:.0f}', f'{d["ffmpeg_ebur128"]["I_LUFS"]}', f'{d["ffmpeg_ebur128"]["LRA_LU"]}',
            f'{d["ffmpeg_ebur128"]["true_peak_dBTP"]}', f'{sp["p10"]} / {sp["p95"]}', f'{L["S_max_rel_I"]}',
            f'{P["crest_factor_dB"]}', f'{S["slope_dB_per_oct_100_10k"]}',
            f'{S["band_shares_dB"]["20-100Hz"]} / {S["band_shares_dB"]["2000-6000Hz"]} / {S["band_shares_dB"]["6000-20000Hz"]}',
            f'{B.get("centroid_median_Hz", "")}', f'{B.get("centroid_slope_oct_per_10LU", "")}',
            f'{St["corr_LR"]}', f'{St["side_to_mid_dB"]}', f'{St["pan_spread_std"]}',
            f'{d.get("cutoff_decays", {}).get("n")}: {d.get("cutoff_decays", {}).get("median_t_to_minus20dB_s")} s / {d.get("cutoff_decays", {}).get("median_RT60_est_s")} s',
            f'{t.get("RT60_from_T20_s")}', f'{t.get("EDT_s")}', f'{d["noise"]["quietest_5pct_100ms_dBFS"]}']


HDR = ["file", "dur s", "I LUFS", "LRA LU", "TP dBTP", "S p10/p95 rel I", "S max rel I", "crest dB", "slope dB/oct",
       "<100 / 2-6k / >6k Hz share dB", "centroid Hz", "brightening oct/10LU", "L/R corr", "S/M dB", "pan spread",
       "cut-offs n: t to -20 dB / RT60 est", "final RT60 s", "final EDT s", "5% quietest dBFS"]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dirs", nargs="+"); ap.add_argument("--png"); ap.add_argument("--md")
    a = ap.parse_args()
    ds = [json.load(open(os.path.join(p, "metrics.json"))) for p in a.dirs]
    lines = ["| " + " | ".join(HDR) + " |", "|" + "---|" * len(HDR)]
    lines += ["| " + " | ".join(row(d)) + " |" for d in ds]
    md = "\n".join(lines); print(md)
    if a.md:
        open(a.md, "w").write(md + "\n")
    if a.png:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(15, 5))
        for d, p in zip(ds, a.dirs):
            f = np.array(d["spectrum"]["third_octave_Hz"]); v = np.array(d["spectrum"]["third_octave_dB_rel_total"])
            ax[0].semilogx(f, v, marker=".", label=d["label"])
            s = np.loadtxt(open(os.path.join(p, "loudness_series.csv")), delimiter=",", ndmin=2)
            I = d["loudness"]["I_LUFS"]; st = s[:, 2] - I; st = st[st > -40]
            h, e = np.histogram(st, bins=np.arange(-40, 15, 1), density=True)
            ax[1].plot(e[:-1] + 0.5, h, label=d["label"])
        ax[0].set_xlabel("Hz"); ax[0].set_ylabel("1/3-octave share of total (dB)"); ax[0].grid(alpha=.3, which="both"); ax[0].legend(fontsize=7)
        ax[0].set_title("Long-term average spectrum"); ax[0].set_ylim(-50, 0)
        ax[1].set_xlabel("short-term loudness relative to integrated (LU)"); ax[1].set_ylabel("share of time"); ax[1].grid(alpha=.3)
        ax[1].set_title("Distribution of short-term loudness"); ax[1].legend(fontsize=7)
        fig.tight_layout(); fig.savefig(a.png, dpi=90)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Measure one audio file. Writes <out>/metrics.json, <out>/bars.csv (with --midi), and PNG plots.

Usage:
  python3 measure.py AUDIO --out DIR [--midi score.midi] [--label NAME]
                     [--start S --dur D] [--offset S] [--tail-start S] [--no-plots]

--midi        align to the MIDI: bar times from its tempo map, per-bar loudness against the printed
              dynamic (from note velocities), decay after the last note-off and after every
              general silence (fermata / caesura), onset lag.
--offset      seconds to add to MIDI times to get audio times (default 0; FluidSynth renders start at 0).
--tail-start  for recordings without MIDI: time (s) of the final cut-off; default: automatic estimate.
"""
import argparse, csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rtk


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("--out", required=True)
    ap.add_argument("--midi"); ap.add_argument("--label")
    ap.add_argument("--start", type=float); ap.add_argument("--dur", type=float)
    ap.add_argument("--offset", type=float, default=0.0)
    ap.add_argument("--tail-start", type=float)
    ap.add_argument("--no-plots", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sr = rtk.SR
    x = rtk.decode(a.audio, sr, a.start, a.dur)
    mono = x.mean(axis=1)
    dur = len(x) / sr
    R = {"file": os.path.abspath(a.audio), "label": a.label or os.path.basename(a.audio),
         "start": a.start, "duration_s": round(dur, 2)}

    # --- loudness
    R["ffmpeg_ebur128"] = rtk.ffmpeg_ebur128(a.audio, a.start, a.dur)
    tM, M = rtk.loudness_series(x, sr, 0.4, 0.1)
    tS, S = rtk.loudness_series(x, sr, 3.0, 0.1)
    I = rtk.integrated(M)
    lra, lo, hi = rtk.lra(S)
    act = S[S > I - 30]
    R["loudness"] = {"I_LUFS": round(I, 2), "LRA_LU": round(lra, 1), "LRA_low": round(lo, 1), "LRA_high": round(hi, 1),
                     "S_percentiles_rel_I": {f"p{p}": round(float(np.percentile(act, p) - I), 1) for p in (5, 10, 25, 50, 75, 90, 95, 99)},
                     "M_max_rel_I": round(float(M.max() - I), 1),
                     "S_max_rel_I": round(float(S.max() - I), 1),
                     "S_min_active_rel_I": round(float(act.min() - I), 1)}
    # --- peaks
    pk = float(np.abs(x).max())
    rms = float(np.sqrt((x.astype(np.float64) ** 2).mean()))
    R["peaks"] = {"sample_peak_dBFS": round(20 * np.log10(pk + 1e-12), 2),
                  "samples_abs_ge_0.999": int((np.abs(x) >= 0.999).sum()),
                  "samples_abs_gt_1.0": int((np.abs(x) > 1.0).sum()),
                  "crest_factor_dB": round(20 * np.log10(pk / (rms + 1e-12)), 1),
                  "rms_dBFS": round(20 * np.log10(rms + 1e-12), 1)}
    # --- noise floor: quietest 100 ms windows
    t10, e10 = rtk.env_db(x, sr, 0.1, 0.05)
    R["noise"] = {"quietest_1pct_100ms_dBFS": round(float(np.percentile(e10, 1)), 1),
                  "quietest_5pct_100ms_dBFS": round(float(np.percentile(e10, 5)), 1)}
    # --- spectrum
    f, P = rtk.psd(mono, sr)
    bands = rtk.third_octave(f, P)
    R["spectrum"] = {"third_octave_Hz": [round(float(v), 1) for v in rtk.THIRD_OCT],
                     "third_octave_dB_rel_total": [round(float(v), 2) for v in bands],
                     "band_shares_dB": rtk.band_shares(f, P),
                     "slope_dB_per_oct_100_10k": round(rtk.spectral_slope(f, P), 2)}
    # brightness against loudness (louder orchestras get brighter)
    tc, cen, fS, Sx = rtk.centroid_series(mono, sr)
    Mi = np.interp(tc, tM, M)
    act_m = Mi > I - 20
    if act_m.sum() > 20:
        sl = np.polyfit(Mi[act_m], np.log2(cen[act_m] + 1), 1)[0]
        loud = act_m & (Mi >= np.percentile(Mi[act_m], 90)); soft = act_m & (Mi <= np.percentile(Mi[act_m], 30))
        # LTAS of loud vs soft frames (difference in 1/3-octave shape)
        def ltas_of(mask):
            Pm = Sx[:, mask].mean(axis=1)
            return rtk.third_octave(fS, Pm)
        bl, bs = ltas_of(loud), ltas_of(soft)
        R["brightness"] = {"centroid_median_Hz": round(float(np.median(cen[act_m])), 0),
                           "centroid_loudest10pct_Hz": round(float(np.median(cen[loud])), 0),
                           "centroid_softest30pct_Hz": round(float(np.median(cen[soft])), 0),
                           "centroid_slope_oct_per_10LU": round(float(sl * 10), 3),
                           "loud_minus_soft_shape_dB_at_Hz": {str(int(round(fc))): round(float(d), 1) for fc, d in
                                                               zip(rtk.THIRD_OCT, bl - bs) if fc in rtk.THIRD_OCT[2::3]}}
    # --- stereo
    R["stereo"] = rtk.stereo_stats(x, sr)

    # --- MIDI-aligned measures
    te, ee = rtk.env_db(x, sr, 0.03, 0.01)
    bars_rows = []
    if a.midi:
        mi = rtk.midi_info(a.midi)
        off = a.offset - (a.start or 0)
        # per-bar loudness (power mean of momentary values whose centre lies in the bar)
        for b in mi["per_bar"]:
            t0, t1 = b["t_start"] + off, b["t_end"] + off
            m = (tM >= t0) & (tM < t1)
            Lb = rtk.power_mean_lufs(M[m]) if m.any() else float("nan")
            row = dict(b); row["loud_LUFS"] = round(Lb, 2); row["loud_rel_I"] = round(Lb - I, 2)
            row["dyn_from_vel_median"] = rtk.vel_to_dyn(b["vel_median"]); row["dyn_from_vel_max"] = rtk.vel_to_dyn(b["vel_max"])
            bars_rows.append(row)
        ok = [r for r in bars_rows if r["vel_median"] is not None and np.isfinite(r["loud_LUFS"])]
        from scipy.stats import spearmanr
        vm = np.array([r["vel_max"] for r in ok]); vmed = np.array([r["vel_median"] for r in ok]); lb = np.array([r["loud_LUFS"] for r in ok])
        ns = np.array([r["sounding"] for r in ok])
        bydyn = {}
        for r in ok:
            bydyn.setdefault(r["dyn_from_vel_max"], []).append(r["loud_LUFS"] - I)
        order = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff/acc"]
        R["score_alignment"] = {
            "n_bars": len(bars_rows),
            "spearman_bar_loudness_vs_vel_max": round(float(spearmanr(vm, lb)[0]), 3),
            "spearman_bar_loudness_vs_vel_median": round(float(spearmanr(vmed, lb)[0]), 3),
            "spearman_bar_loudness_vs_sounding_notes": round(float(spearmanr(ns, lb)[0]), 3),
            "linear_dB_per_velocity_step_of_10": round(float(np.polyfit(vm, lb, 1)[0] * 10), 2),
            "bar_loudness_by_loudest_marked_dynamic_rel_I": {d: {"n": len(bydyn[d]), "median": round(float(np.median(bydyn[d])), 1),
                                                                   "min": round(float(np.min(bydyn[d])), 1), "max": round(float(np.max(bydyn[d])), 1)}
                                                              for d in order if d in bydyn},
            "loudest_bars": sorted([(r["bar"], round(r["loud_rel_I"], 1), r["dyn_from_vel_max"]) for r in ok], key=lambda z: -z[1])[:8],
            "softest_bars": sorted([(r["bar"], round(r["loud_rel_I"], 1), r["dyn_from_vel_max"]) for r in ok], key=lambda z: z[1])[:8],
        }
        # tails: final note-off and every silence in the score
        tails = {"final": rtk.decay_fit(te, ee, mi["last_note_off_s"] + off, max_len=min(10.0, te[-1] - mi["last_note_off_s"] - off))}
        tails["final"]["audio_after_last_note_off_s"] = round(float(dur - mi["last_note_off_s"] - off), 2)
        g = []
        for (s0, s1) in mi["gaps"]:
            d = rtk.decay_fit(te, ee, s0 + off, floor_db=-100, max_len=s1 - s0)
            if d:
                k = (te >= s0 + off) & (te < s1 + off)
                d["gap_len_s"] = round(s1 - s0, 2); d["bar"] = int(np.searchsorted(mi["bar_s"], s0, side="right"))
                d["drop_at_gap_end_dB"] = round(float(d["level_at_t0_dB"] - ee[k][-1]), 1) if k.any() else None
                g.append(d)
        tails["silences_in_score"] = g
        R["tails"] = tails
        # onset lag: spectral flux vs MIDI onsets
        Z = Sx  # power spectrogram, hop 2048
        hop_s = 2048 / sr
        flux = np.maximum(np.diff(np.log(Z + 1e-10), axis=1), 0).sum(0)
        tf = tc[1:]
        grid = np.arange(0, dur, 0.01)
        fl = np.interp(grid, tf, flux); fl = (fl - fl.mean()) / (fl.std() + 1e-9)
        tr = np.zeros_like(grid)
        idx = np.clip(((np.asarray(mi["note_on_s"]) + off) / 0.01).astype(int), 0, len(grid) - 1)
        np.add.at(tr, idx, 1.0)
        from scipy.ndimage import gaussian_filter1d
        tr = gaussian_filter1d(tr, 3); tr = (tr - tr.mean()) / (tr.std() + 1e-9)
        lags = np.arange(-30, 31)
        cc = [float(np.mean(fl[max(0, L):len(fl) + min(0, L)] * tr[max(0, -L):len(tr) - max(0, L)])) for L in lags]
        R["onsets"] = {"best_lag_ms_audio_after_midi": int(lags[int(np.argmax(cc))] * 10), "peak_corr": round(max(cc), 3),
                       "note": "spectral-flux vs MIDI note-on train, 10 ms grid, +-300 ms"}
        with open(os.path.join(a.out, "bars.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(bars_rows[0].keys())); w.writeheader(); w.writerows(bars_rows)
    else:
        # recordings: final cut-off estimate = last time the 30 ms envelope is within 12 dB of the max of the final 20 s
        if a.tail_start is not None:
            t0 = a.tail_start
        else:
            m = te > te[-1] - 20
            thr = ee[m].max() - 12
            k = np.where(m & (ee >= thr))[0]
            t0 = float(te[k[-1]])
        R["tails"] = {"final": rtk.decay_fit(te, ee, t0, max_len=min(10.0, te[-1] - t0)),
                      "final_note": "t0 = automatic cut-off estimate (last frame within 12 dB of the max of the final 20 s)" if a.tail_start is None else "t0 given"}
        R["tails"]["final"]["audio_after_t0_s"] = round(float(dur - t0), 2)

    cd = rtk.cutoff_decays(te, ee)
    R["cutoff_decays"] = {"n": len(cd), "median_t_to_minus20dB_s": round(float(np.median([c["t_to_minus20dB_s"] for c in cd])), 3) if cd else None,
                          "median_RT60_est_s": round(float(np.median([c["RT60_est_s"] for c in cd])), 2) if cd else None,
                          "events": cd[:40],
                          "note": "sharp cut-offs found from the audio alone (0.4 s sustained, then >=15 dB fall within 0.4 s); RT60 from the -5..-20 dB slope"}
    rtk.save_json(R, os.path.join(a.out, "metrics.json"))
    with open(os.path.join(a.out, "loudness_series.csv"), "w") as fh:
        np.savetxt(fh, np.c_[tM, M, np.interp(tM, tS, S)], delimiter=",", header="t_s,momentary_LUFS,shortterm_LUFS", fmt="%.2f")
    if not a.no_plots:
        plots(a, R, x, sr, tM, M, tS, S, I, bars_rows, mi if a.midi else None, f, P, te, ee)
    print(f"{R['label']}: I {R['loudness']['I_LUFS']} LUFS, LRA {R['loudness']['LRA_LU']} LU, TP {R['ffmpeg_ebur128']['true_peak_dBTP']} dBTP -> {a.out}")


def plots(a, R, x, sr, tM, M, tS, S, I, bars_rows, mi, f, P, te, ee):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from scipy import signal
    mono = x.mean(axis=1)
    off = a.offset - (a.start or 0)
    # spectrogram (log frequency)
    nfft, hop = 8192, 4410
    ff, tt, Z = signal.stft(mono, sr, nperseg=nfft, noverlap=nfft - hop)
    D = 10 * np.log10(np.abs(Z) ** 2 + 1e-14)
    fig, ax = plt.subplots(figsize=(18, 6))
    keep = (ff >= 25) & (ff <= 18000)
    vmax = np.percentile(D[keep], 99.5)
    ax.pcolormesh(tt, ff[keep], D[keep], shading="auto", cmap="magma", vmin=vmax - 80, vmax=vmax)
    ax.set_yscale("log"); ax.set_ylim(25, 18000); ax.set_xlabel("time (s)"); ax.set_ylabel("Hz")
    ax.set_title(f"Spectrogram: {R['label']}")
    if mi:
        for t, txt, bar in mi["markers"]:
            ax.axvline(t + off, color="cyan", lw=0.6); ax.text(t + off, 20000, txt, color="cyan", fontsize=8, va="bottom")
    fig.tight_layout(); fig.savefig(os.path.join(a.out, "spectrogram.png"), dpi=90); plt.close(fig)
    # loudness over time
    fig, ax = plt.subplots(figsize=(18, 5))
    ax.plot(tM, M, lw=0.4, color="0.7", label="momentary (400 ms)")
    ax.plot(tS, S, lw=1.2, color="C0", label="short-term (3 s)")
    ax.axhline(I, color="k", ls="--", lw=0.7, label=f"integrated {I:.1f} LUFS")
    ax.set_ylim(I - 45, I + 15); ax.set_xlabel("time (s)"); ax.set_ylabel("LUFS")
    if bars_rows:
        ax2 = ax.twinx()
        ts = [r["t_start"] + off for r in bars_rows]; vm = [r["vel_max"] or 0 for r in bars_rows]
        ax2.step(ts, vm, where="post", color="C3", lw=0.8, label="max note velocity in bar (printed dynamic)")
        ax2.set_ylim(0, 160); ax2.set_ylabel("velocity", color="C3")
        lb = [r["loud_LUFS"] for r in bars_rows]
        ax.step(ts, lb, where="post", color="C2", lw=1.0, label="bar loudness")
        for t, txt, bar in mi["markers"]:
            ax.axvline(t + off, color="0.5", lw=0.5); ax.text(t + off, I + 13, txt, fontsize=8)
        ax2.legend(loc="upper right", fontsize=8)
    ax.legend(loc="upper left", fontsize=8); ax.set_title(f"Loudness: {R['label']}")
    fig.tight_layout(); fig.savefig(os.path.join(a.out, "loudness.png"), dpi=90); plt.close(fig)
    # LTAS
    fig, ax = plt.subplots(figsize=(8, 5))
    m = (f > 20) & (f < 20000)
    ax.semilogx(f[m], 10 * np.log10(P[m] / P[m].sum()), lw=0.6, color="0.6", label="PSD (normalised)")
    ax.semilogx(rtk.THIRD_OCT, R["spectrum"]["third_octave_dB_rel_total"], "o-", color="C0", label="1/3 octave share")
    ax.set_xlabel("Hz"); ax.set_ylabel("dB"); ax.grid(True, which="both", alpha=0.3); ax.legend(fontsize=8)
    ax.set_title(f"Long-term average spectrum: {R['label']}")
    fig.tight_layout(); fig.savefig(os.path.join(a.out, "ltas.png"), dpi=90); plt.close(fig)
    # final tail
    t0 = R["tails"]["final"]["t0_s"]
    k = (te > t0 - 3) & (te < t0 + 10)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(te[k] - t0, ee[k]); ax.axvline(0, color="r", lw=0.7)
    ax.set_xlabel("s after final cut-off / last note-off"); ax.set_ylabel("dBFS (30 ms RMS)")
    ax.set_title(f"Final decay: {R['label']}"); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(a.out, "tail.png"), dpi=90); plt.close(fig)


if __name__ == "__main__":
    main()

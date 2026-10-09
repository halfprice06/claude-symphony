#!/usr/bin/env python3
"""Render one stem per staff and measure per-instrument level, articulation and blend.

Usage:
  python3 stems.py --midi IN.midi --notes notes.csv --out DIR
                   [--render 'fluidsynth -ni -g 0.6 -r 44100 -F {wav} /usr/share/sounds/sf2/FluidR3_GM.sf2 {midi}']
                   [--jobs 4] [--work /tmp/stems_x] [--keep-wav] [--reuse]

Each stem is the MIDI with track 0 (tempo) plus only the tracks of one staff (track-name prefix before ':'),
rendered with the same command as the full mix. The command must not normalise loudness per stem
(use a fixed gain), or the stem levels mean nothing. notes.csv comes from score_events.py for the same MIDI.

Writes:
  DIR/stems_summary.json  per stem: loudness while sounding, level by printed dynamic (and dB per dynamic
                          step), pan, centroid, articulation audio metrics; blend measures across stems
  DIR/stem_bars.csv       per bar x stem loudness while sounding (LUFS) and the printed dynamic
  DIR/stem_levels.png     level by printed dynamic per stem
"""
import argparse, csv, json, os, re, shlex, subprocess, sys
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rtk

DYN = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]
FAMILY = {"Flutes 12": "woodwind", "Oboes 12": "woodwind", "Cor anglais": "woodwind", "Clarinets 12": "woodwind",
          "Bass clarinet": "woodwind", "Bassoons 12": "woodwind", "Contrabassoon": "woodwind",
          "Horns 12": "horn", "Horns 34": "horn", "Trumpets 12": "brass", "Trumpet 3": "brass",
          "Trombones 12": "brass", "Bass trombone": "brass", "Tuba": "brass", "Timpani": "percussion", "drums": "percussion",
          "Harp RH": "harp", "Harp LH": "harp", "Violins I": "strings", "Violins II": "strings", "Violas": "strings",
          "Violoncellos": "strings", "Double basses": "strings"}


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


def write_stem_midis(midi, outdir):
    import mido
    m = mido.MidiFile(midi)
    groups = defaultdict(list)
    for i, tr in enumerate(m.tracks[1:], 1):
        if any(not x.is_meta for x in tr):
            groups[key(tr.name)].append(i)
    paths = {}
    for g, idx in groups.items():
        n = mido.MidiFile(type=1, ticks_per_beat=m.ticks_per_beat)
        n.tracks.append(m.tracks[0])
        for i in idx:
            n.tracks.append(m.tracks[i])
        p = os.path.join(outdir, re.sub(r"\W+", "_", g) + ".mid")
        n.save(p); paths[g] = p
    return paths


def render(cmd, mid, wav):
    c = cmd.format(midi=shlex.quote(mid), wav=shlex.quote(wav))
    subprocess.run(c, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)


def art_class(r):
    a = r["arts"].split("|") if r["arts"] else []
    if r["tech"] == "pizz": return "pizz"
    for k in ("staccato", "marcato", "accent", "tenuto"):
        if k in a: return k
    if any(x.startswith("tremolo") for x in a): return "tremolo"
    if r["slur"] in ("start", "in"): return "legato"
    return "detached"  # no mark, not slurred to the next note (incl. slur ends)


def note_metrics(te, ee, rows):
    """Audio metrics per printed note from a stem envelope (10 ms hop)."""
    ons = np.array([r["t_on_s"] for r in rows])
    res = []
    def at(t):
        return float(np.interp(t, te, ee))
    for i, r in enumerate(rows):
        t0, L = r["t_on_s"], r["notated_s"]
        k0 = np.searchsorted(te, t0 - 0.01); k1 = np.searchsorted(te, t0 + min(0.2, max(0.06, L)))
        if k1 <= k0 + 1:
            continue
        seg = ee[k0:k1]; pk = float(seg.max())
        att = float(te[k0 + np.argmax(seg >= pk - 3)] - t0)
        others = ons[(ons > t0 + 0.03) & (ons < t0 + L + 0.3)]
        iso = len(others) == 0
        clean = at(t0 - 0.02) <= pk - 10  # onset not masked by an earlier note of the stem
        d = {"cls": art_class(r), "peak": pk, "attack_s": att if clean else None, "dyn": r["dyn"], "bar": r["bar"], "L": L, "iso": iso,
             "slur": r["slur"], "arts": r["arts"], "t_on": t0}
        if L >= 0.15 and not len(ons[(ons > t0 + 0.03) & (ons < t0 + 0.75 * L)]):
            d["sustain75_dB"] = at(t0 + 0.75 * L) - pk
        if iso:
            k = np.searchsorted(te, t0 + att); kk = np.searchsorted(te, t0 + L + 3.0)
            below = np.where(ee[k:kk] < pk - 20)[0]
            if len(below):
                d["audible_len_s"] = float(te[k + below[0]] - t0)
                d["audible_ratio"] = d["audible_len_s"] / L
        if d["cls"] == "tremolo" and L >= 0.4:
            m = (te > t0 + 0.05) & (te < t0 + L - 0.05)
            from scipy.signal import find_peaks
            p, _ = find_peaks(ee[m], prominence=3)
            d["trem_peaks_per_s"] = len(p) / (L - 0.1)
            d["trem_env_std_dB"] = float(np.std(ee[m]))
        res.append(d)
    # boundary dips between consecutive notes of one voice
    by_v = defaultdict(list)
    for r in rows:
        by_v[(r["voice"], r["midi_track"])].append(r)
    dips = []
    for v, rs in by_v.items():
        rs.sort(key=lambda r: r["t_on_s"])
        for a, b in zip(rs, rs[1:]):
            if abs(a["t_on_s"] + a["notated_s"] - b["t_on_s"]) > 0.02 or a["notated_s"] < 0.15 or "staccato" in a["arts"]:
                continue
            if len(ons[(ons > a["t_on_s"] + 0.03) & (ons < b["t_on_s"] - 0.03)]):
                continue
            mid = np.median(ee[(te > a["t_on_s"] + 0.3 * a["notated_s"]) & (te < a["t_on_s"] + 0.7 * a["notated_s"])])
            mn = ee[(te > b["t_on_s"] - 0.08) & (te < b["t_on_s"] + 0.03)]
            if len(mn) and np.isfinite(mid):
                dips.append({"slurred": a["slur"] in ("start", "in"), "dip_dB": float(mn.min() - mid)})
    return res, dips


def analyse_stem(name, wav, rows, bars, mix_I):
    x = rtk.decode(wav)
    tM, M = rtk.loudness_series(x, rtk.SR, 0.4, 0.1)
    te, ee = rtk.env_db(x, rtk.SR, 0.02, 0.01)
    sounding = np.zeros_like(tM, dtype=bool)
    for r in rows:
        sounding |= (tM >= r["t_on_s"] + 0.1) & (tM <= (r["t_off_s"] or r["t_on_s"] + r["notated_s"]))
    out = {"stem": name, "family": FAMILY.get(name, "?"), "notes": len(rows),
           "I_LUFS_whole_file": round(rtk.integrated(M), 2),
           "loud_while_sounding_LUFS": round(rtk.power_mean_lufs(M[sounding]), 2) if sounding.any() else None,
           "peak_dBFS": round(float(20 * np.log10(np.abs(x).max() + 1e-12)), 1)}
    L, R = x[:, 0].astype(float), x[:, 1].astype(float)
    eL, eR = (L ** 2).sum(), (R ** 2).sum()
    out["pan_R_minus_L_dB"] = round(float(10 * np.log10((eR + 1e-20) / (eL + 1e-20))), 2)
    out["corr_LR"] = round(float((L * R).sum() / np.sqrt(eL * eR + 1e-20)), 3)
    f, P = rtk.psd(x.mean(axis=1))
    out["centroid_Hz"] = round(float((f * P).sum() / P.sum()), 0)
    # per-bar loudness while sounding, and printed dynamic in the bar (most frequent among its notes)
    bar_rows = []
    nb = defaultdict(list)
    for r in rows:
        nb[r["bar"]].append(r)
    for b in bars:
        ns = nb.get(b["bar"])
        if not ns:
            continue
        m = sounding & (tM >= b["t_start"]) & (tM < b["t_end"])
        if m.sum() < 3:
            continue
        dyns = [r["dyn"] for r in ns if r["dyn"] in DYN]
        d = Counter(dyns).most_common(1)[0][0] if dyns else ""
        bar_rows.append({"bar": b["bar"], "stem": name, "dyn": d, "loud_LUFS": round(rtk.power_mean_lufs(M[m]), 2),
                         "vel_med": float(np.median([r["midi_vel"] for r in ns if r["midi_vel"] != ""] or [0]))})
    byd = defaultdict(list)
    for br in bar_rows:
        if br["dyn"]:
            byd[br["dyn"]].append(br["loud_LUFS"])
    out["level_by_dynamic_LUFS"] = {d: {"n": len(byd[d]), "median": round(float(np.median(byd[d])), 1)} for d in DYN if d in byd}
    xs = [DYN.index(br["dyn"]) for br in bar_rows if br["dyn"]]; ys = [br["loud_LUFS"] for br in bar_rows if br["dyn"]]
    out["dB_per_dynamic_step"] = round(float(np.polyfit(xs, ys, 1)[0]), 2) if len(set(xs)) >= 2 else None
    # articulations
    nm, dips = note_metrics(te, ee, rows)
    arts = {}
    for c in sorted(set(d["cls"] for d in nm)):
        ds = [d for d in nm if d["cls"] == c]
        av = [d["attack_s"] for d in ds if d["attack_s"] is not None]
        e = {"n": len(ds), "attack_ms_median_clean_onsets": round(1000 * float(np.median(av)), 0) if av else None, "clean_onsets_n": len(av)}
        for k in ("sustain75_dB", "audible_len_s", "audible_ratio", "trem_peaks_per_s", "trem_env_std_dB"):
            v = [d[k] for d in ds if k in d]
            if v:
                e[k + "_median"] = round(float(np.median(v)), 2); e[k + "_n"] = len(v)
        arts[c] = e
    # accent boost: accented peak minus median peak of unaccented notes, same dynamic, within 2 bars
    boosts = []
    for d in nm:
        if d["cls"] in ("accent", "marcato"):
            ref = [o["peak"] for o in nm if o["cls"] not in ("accent", "marcato", "staccato") and o["dyn"] == d["dyn"] and abs(o["bar"] - d["bar"]) <= 2]
            if ref:
                boosts.append(d["peak"] - np.median(ref))
    if boosts:
        arts["accent_peak_boost_dB_median"] = round(float(np.median(boosts)), 1); arts["accent_boost_n"] = len(boosts)
    for s in (True, False):
        v = [d["dip_dB"] for d in dips if d["slurred"] == s]
        if v:
            arts[("slurred" if s else "detached") + "_boundary_dip_dB_median"] = round(float(np.median(v)), 1)
            arts[("slurred" if s else "detached") + "_boundary_n"] = len(v)
    out["articulation_audio"] = arts
    return out, bar_rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--midi", required=True); ap.add_argument("--notes", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--render", default="fluidsynth -ni -g 0.6 -r 44100 -F {wav} /usr/share/sounds/sf2/FluidR3_GM.sf2 {midi}")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--keep-wav", action="store_true"); ap.add_argument("--reuse", action="store_true")
    ap.add_argument("--work", help="folder for stem MIDI/WAV files (default: a new folder under /tmp; keep it out of /mnt/project-files)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    import tempfile
    wd = a.work or tempfile.mkdtemp(prefix="stems_"); os.makedirs(wd, exist_ok=True)
    print("stem files in", wd)
    mids = write_stem_midis(a.midi, wd)
    rows = list(csv.DictReader(open(a.notes)))
    for r in rows:
        for k in ("t_on_s", "notated_s"):
            r[k] = float(r[k])
        r["t_off_s"] = float(r["t_off_s"]) if r["t_off_s"] else None
        r["bar"] = int(r["bar"]); r["midi_vel"] = int(r["midi_vel"]) if r["midi_vel"] else ""
    by_stem = defaultdict(list)
    for r in rows:
        by_stem[key(r["midi_track"]) if r["midi_track"] else r["staff"]].append(r)
    bars = rtk.midi_info(a.midi)["per_bar"]
    jobs = []
    for g, p in mids.items():
        w = p[:-4] + ".wav"
        if not (a.reuse and os.path.exists(w)):
            jobs.append((p, w))
    with ThreadPoolExecutor(a.jobs) as ex:
        list(ex.map(lambda j: render(a.render, *j), jobs))
    results, allbars = [], []
    def work(g):
        return analyse_stem(g, mids[g][:-4] + ".wav", by_stem.get(g, []), bars, None)
    with ThreadPoolExecutor(a.jobs) as ex:
        for res, br in ex.map(work, sorted(mids)):
            results.append(res); allbars += br
            print(f"{res['stem']:15s} sounding {res['loud_while_sounding_LUFS']} LUFS  dB/step {res['dB_per_dynamic_step']}  pan {res['pan_R_minus_L_dB']}", flush=True)
    # ---------------- blend measures across stems, per bar
    per_bar = defaultdict(list)
    for br in allbars:
        per_bar[br["bar"]].append(br)
    dominance, inversions, loudest = [], [], Counter()
    inv_pairs = Counter()
    for b, lst in per_bar.items():
        lst = sorted(lst, key=lambda z: -z["loud_LUFS"])
        if len(lst) >= 2:
            dominance.append(lst[0]["loud_LUFS"] - lst[1]["loud_LUFS"])
        loudest[lst[0]["stem"]] += 1
        for A in lst:
            for B in lst:
                if A["dyn"] in DYN and B["dyn"] in DYN and DYN.index(A["dyn"]) < DYN.index(B["dyn"]) and A["loud_LUFS"] > B["loud_LUFS"] + 3:
                    inversions.append((b, A["stem"], A["dyn"], B["stem"], B["dyn"], round(A["loud_LUFS"] - B["loud_LUFS"], 1)))
                    inv_pairs[(A["stem"], B["stem"])] += 1
    fam = defaultdict(lambda: defaultdict(list))
    for br in allbars:
        if br["dyn"]:
            fam[FAMILY.get(br["stem"], "?")][br["dyn"]].append(br["loud_LUFS"])
    blend = {"bars_with_2plus_stems": len(dominance),
             "loudest_minus_second_dB_median": round(float(np.median(dominance)), 1) if dominance else None,
             "bars_where_one_stem_leads_by_6dB_plus": int(sum(1 for d in dominance if d >= 6)),
             "loudest_stem_count": dict(loudest.most_common()),
             "balance_inversions_n": len(inversions),
             "balance_inversion_note": "bar where a stem with a softer printed dynamic is >3 dB louder (while sounding) than a stem with a louder printed dynamic",
             "balance_inversions_top_pairs": [[f"{a} louder than {b}", n] for (a, b), n in inv_pairs.most_common(15)],
             "balance_inversions_examples": inversions[:25],
             "family_level_by_dynamic_LUFS_median": {f: {d: round(float(np.median(v)), 1) for d, v in sorted(dd.items(), key=lambda z: DYN.index(z[0]))} for f, dd in fam.items()},
             "stem_pan_R_minus_L_dB": {r["stem"]: r["pan_R_minus_L_dB"] for r in results},
             "stem_centroid_Hz": {r["stem"]: r["centroid_Hz"] for r in results}}
    rtk.save_json({"render": a.render, "midi": os.path.abspath(a.midi), "stems": results, "blend": blend}, os.path.join(a.out, "stems_summary.json"))
    with open(os.path.join(a.out, "stem_bars.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(allbars[0].keys())); w.writeheader(); w.writerows(allbars)
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(12, 7))
        for i, r in enumerate(sorted(results, key=lambda r: list(FAMILY).index(r["stem"]) if r["stem"] in FAMILY else 99)):
            d = r["level_by_dynamic_LUFS"]
            xs = [DYN.index(k) for k in d]; ys = [d[k]["median"] for k in d]
            ls = {"woodwind": "-", "horn": "--", "brass": "-.", "strings": ":", "harp": "-", "percussion": "-"}.get(r["family"], "-")
            ax.plot(xs, ys, ls, marker="o", label=r["stem"], color=plt.cm.tab20(i % 20))
        ax.set_xticks(range(len(DYN))); ax.set_xticklabels(DYN); ax.set_ylabel("stem loudness while sounding (LUFS, median of bars)")
        ax.set_title("Per-stem level by printed dynamic"); ax.grid(alpha=0.3); ax.legend(fontsize=7, ncol=3)
        fig.tight_layout(); fig.savefig(os.path.join(a.out, "stem_levels.png"), dpi=90); plt.close(fig)
    except Exception as e:
        print("plot failed:", e)
    if not a.keep_wav:
        for g, p in mids.items():
            w = p[:-4] + ".wav"
            if os.path.exists(w) and not os.path.abspath(w).startswith("/mnt/project-files"):
                os.remove(w)
    print(json.dumps({k: v for k, v in blend.items() if k in ("loudest_minus_second_dB_median", "balance_inversions_n", "loudest_stem_count")}, indent=1))


if __name__ == "__main__":
    main()

"""Measure a mockup render: mix loudness, per-bar levels of the mix and of every stem, level per printed dynamic,
long-term spectrum against a reference recording, and spectrogram pictures.

Usage: python measure.py <render-dir> <parts.json> <out-dir>
  render-dir holds 00_Master.wav and NN_<track>.wav stems (REAPER render, RENDER_SETTINGS=1).
  mvt1 c50: return stems (the names in mix.json "returns", next to parts.json) are listed in their own section and
  res["returns"]; they are left out of the per-track tables. The mix is 00_Master.wav (dry stems + returns).
Writes <out-dir>/metrics.md (read this first), metrics.json, spectrogram.png, waveform.png.
"""
import glob, json, os, re, subprocess, sys
import numpy as np
import soundfile as sf

RENDER, PARTS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
REF = "/Users/gooby/sandbox/claude_composes/symphony/render/assets/refs/dvorak9_i_columbia.mp3"
os.makedirs(OUT, exist_ok=True)
d = json.load(open(PARTS))
DYN_NAMES = [(22, "ppp"), (34, "pp"), (46, "p"), (58, "mp"), (72, "mf"), (88, "f"), (114, "ff"), (124, "fff")]   # c02: ff 114, fff 124


def dyn_name(v):
    return min(DYN_NAMES, key=lambda x: abs(x[0] - v))[1]


# ---- tempo map: qn -> seconds, bar starts ----
tempo = sorted(d["tempo"])


def qn_to_sec(q):
    t, lq, lb = 0.0, 0.0, tempo[0][1]
    for tq, bpm in tempo[1:]:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb; lq, lb = tq, bpm
    return t + (q - lq) * 60 / lb


# mvt1 c03: renders c00-c02 sound 1/6 qn early on the parts.json map (tools/rendermap.py)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rendermap
qn_to_sec = rendermap.wrap(qn_to_sec, rendermap.cycle_of(RENDER))

bars, q, sig = [], 0.0, sorted(d["timesig"])
while q < d["end_qn"] - 1e-6:
    num, den = [(n, dd) for sq, n, dd in sig if sq <= q + 1e-6][-1]
    bars.append(q); q += num * 4 / den
bar_sec = [qn_to_sec(b) for b in bars] + [qn_to_sec(d["end_qn"])]


def db(x):
    return float(20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)) if len(x) else -120.0


def ebur(path):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    g = lambda k: float(re.findall(k + r":\s+(-?[\d.]+)", out)[-1])
    return {"I_LUFS": g("I"), "LRA_LU": g("LRA"), "true_peak_dBFS": g("Peak")}


def ltas(x, sr):
    """1/3-octave long-term average spectrum (dB, normalised to the 1 kHz band)."""
    mono = x.mean(1) if x.ndim > 1 else x
    n = 1 << 15
    frames = [mono[i:i + n] for i in range(0, len(mono) - n, n // 2)]
    spec = np.mean([np.abs(np.fft.rfft(f * np.hanning(n))) ** 2 for f in frames], axis=0)
    freqs = np.fft.rfftfreq(n, 1 / sr)
    centres = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    bands = {}
    for c in centres:
        lo, hi = c / 2 ** 0.5, c * 2 ** 0.5
        bands[c] = 10 * np.log10(spec[(freqs >= lo) & (freqs < hi)].mean() + 1e-20)
    ref = bands[1000]
    return {str(c): round(v - ref, 1) for c, v in bands.items()}


# c09 (critic C #1): band shares of total energy (dB), against the Dvorak MP3 and two lossless slow-movement references
# (Brahms 1/ii and 4/ii, Musopen; stored metrics, since their audio is not on disk). Tune the low end against all three.
SHARE_BANDS = [(20, 100), (100, 250), (250, 500), (500, 2000), (2000, 6000), (6000, 20000)]
BRAHMS = {k: f"/Users/gooby/sandbox/claude_composes/symphony/render/critics/c04/ref_{k}_musopen/metrics.json"
          for k in ("brahms1_ii", "brahms4_ii")}


def shares(x, sr):
    mono = (x.mean(1) if x.ndim > 1 else x).astype(np.float64)
    n = 1 << 15
    S = 0
    for k in range(0, len(mono) - n, n):
        S = S + np.abs(np.fft.rfft(mono[k:k + n] * np.hanning(n))) ** 2
    f = np.fft.rfftfreq(n, 1 / sr)
    tot = S[f > 15].sum()
    return {f"{a}-{b}Hz": round(float(10 * np.log10(S[(f >= a) & (f < b)].sum() / tot)), 2) for a, b in SHARE_BANDS}


mix_path = os.path.join(RENDER, "00_Master.wav")
mix, sr = sf.read(mix_path)
res = {"mix": ebur(mix_path), "bars": len(bars)}
res["mix"]["sample_peak"] = float(np.abs(mix).max())
res["mix"]["bar_db"] = [round(db(mix[int(a * sr):int(b * sr)]), 1) for a, b in zip(bar_sec, bar_sec[1:])]
res["mix"]["ltas"] = ltas(mix, sr)
if os.path.exists(REF):
    tmp = os.path.join(OUT, "_ref.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", REF, "-ac", "2", "-ar", "48000", tmp])
    r, rsr = sf.read(tmp); res["ref_ltas_dvorak9_i"] = ltas(r, rsr); res["ref_shares_dvorak9_i"] = shares(r, rsr); os.remove(tmp)
res["mix"]["shares"] = shares(mix, sr)
for k, pth in BRAHMS.items():
    if os.path.exists(pth):
        res[f"ref_shares_{k}"] = json.load(open(pth))["spectrum"]["band_shares_dB"]

# ---- stems ----
tracks = {t["name"]: t for t in d["tracks"]}
stems = {}
# mvt1 c50: return stems (mix.json "returns"; tools/return_stems.py numbers them 91..) are measured apart, in
# res["returns"], with the energy ratio of all return stems to all instrument stems (the master is their sum)
_mixp = os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")
RETS = [k for k in ((json.load(open(_mixp)).get("returns") or {}) if os.path.exists(_mixp) else {}) if not k.startswith("_")]
rets, e_dry, e_ret = {}, 0.0, 0.0
for p in sorted(glob.glob(os.path.join(RENDER, "[0-9][0-9]_*.wav"))):
    name = os.path.basename(p)[3:-4]
    if name == "Master":
        continue
    x, _ = sf.read(p)
    if name in RETS:   # mvt1 c50
        rets[name] = {"bar_db": [round(db(x[int(a * sr):int(b * sr)]), 1) for a, b in zip(bar_sec, bar_sec[1:])],
                      "peak": round(float(np.abs(x).max()), 3), "rms_db": round(db(x), 1)}
        e_ret += float(np.sum(np.asarray(x, dtype=np.float64) ** 2))
        continue
    if RETS:
        e_dry += float(np.sum(np.asarray(x, dtype=np.float64) ** 2))
    t = tracks.get(name)
    entry = {"bar_db": [round(db(x[int(a * sr):int(b * sr)]), 1) for a, b in zip(bar_sec, bar_sec[1:])],
             "peak": round(float(np.abs(x).max()), 3)}
    if t:
        active = [False] * len(bars)
        for n in t["notes"]:
            for bi, b in enumerate(bars):
                be = bars[bi + 1] if bi + 1 < len(bars) else d["end_qn"]
                if n["qn"] < be and n["qn"] + n["dur"] > b:
                    active[bi] = True
        curve = t.get("dyn_curve") or t["cc11"] or t.get("cc7") or []
        dyn = []
        for b in bars:
            v = [vv for qq, vv in curve if qq <= b + 1e-6]
            dyn.append(dyn_name(v[-1]) if v else None)
        entry["active"] = active
        entry["printed_dyn"] = dyn
        by = {}
        for a, lv, dn in zip(active, entry["bar_db"], dyn):
            if a and dn:
                by.setdefault(dn, []).append(lv)
        entry["median_db_by_dynamic"] = {k: round(float(np.median(v)), 1) for k, v in by.items()}
    stems[name] = entry
res["stems"] = stems
if rets:   # mvt1 c50
    res["returns"] = rets
    res["returns_re_dry_db"] = round(10 * np.log10(max(e_ret, 1e-20) / max(e_dry, 1e-20)), 2)


# mvt1 c40 (critic B #1): silent-note check. Clarinet 1's D5 at qn 654 (a 2.4 s note at the top of its phrase) never
# sounded in eight renders (a legato-row re-tongue 30 ms after the previous note-off) and no measure listed it. For every
# note of SILENT_MIN_QN or longer: the median A-weighted level (50 ms frames) from score onset + 0.35 qn to min(end - 0.1,
# onset + 2 qn), against the median of the same measure over the track's other such notes at the same printed dynamic
# (dyn_curve in the middle of that window, so a note inside a hairpin is compared at its own level); listed when it is more than SILENT_UNDER_DB under. A delayed unison copy (UNI_DELAY) or a chord note under another of
# the same stem, or a note under the final fade, can read as a false alarm; read the list, do not act on it blindly.
SILENT_MIN_QN, SILENT_UNDER_DB = 0.9, 18.0


def a_weight_db(f):
    f2 = np.maximum(f, 1.0) ** 2
    ra = (12194.0 ** 2 * f2 ** 2) / ((f2 + 20.6 ** 2) * np.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) * (f2 + 12194.0 ** 2))
    return 20 * np.log10(ra) + 2.0


def frames_a(x, sr, hop=0.05):
    mono = (x.mean(1) if x.ndim > 1 else x).astype(np.float64)
    n, h = 4096, int(hop * sr)
    w = np.hanning(n)
    aw = 10 ** (a_weight_db(np.fft.rfftfreq(n, 1 / sr)) / 10)
    out = []
    for k in range(0, max(1, len(mono) - n), h):
        seg = mono[k:k + n]
        if len(seg) < n:
            seg = np.pad(seg, (0, n - len(seg)))
        out.append(10 * np.log10((np.abs(np.fft.rfft(seg * w)) ** 2 * aw).sum() + 1e-20))
    return np.array(out), (n / 2) / sr, hop   # frame k centred at k * hop + n / 2 / sr


silent = []
for p in sorted(glob.glob(os.path.join(RENDER, "[0-9][0-9]_*.wav"))):
    name = os.path.basename(p)[3:-4]
    t = tracks.get(name)
    if name == "Master" or not t or t.get("family") == "perc":
        continue
    x, _ = sf.read(p)
    fa, off, hop = frames_a(x, sr)
    curve = t.get("dyn_curve") or t["cc11"] or []
    rows = []
    for nt in t["notes"]:
        sq = nt.get("sq", nt["qn"])
        end = nt["qn"] + nt["dur"]
        if end - sq < SILENT_MIN_QN:
            continue
        a_, b_ = qn_to_sec(sq + 0.35), qn_to_sec(min(end - 0.1, sq + 2.0))
        ia, ib = int(max(0, (a_ - off) / hop)), int(max(0, (b_ - off) / hop))
        if ib <= ia or ib > len(fa):
            continue
        qm = (sq + 0.35 + min(end - 0.1, sq + 2.0)) / 2   # the printed level in the middle of the window (hairpins)
        v = [vv for qq, vv in curve if qq <= qm + 1e-6]
        rows.append((sq, nt["pitch"], dyn_name(v[-1]) if v else "?", float(np.median(fa[ia:ib]))))
    for sq, pitch, dn, lv in rows:
        ref = [r[3] for r in rows if r[2] == dn and r[0] != sq]
        if len(ref) >= 3 and lv < np.median(ref) - SILENT_UNDER_DB:
            silent.append({"track": name, "sq": round(sq, 3), "pitch": pitch, "dyn": dn, "db_a": round(lv, 1),
                           "track_median_db_a": round(float(np.median(ref)), 1)})
res["silent_notes"] = silent
json.dump(res, open(os.path.join(OUT, "metrics.json"), "w"), indent=1)

# ---- pictures ----
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mix_path, "-lavfi",
                "showspectrumpic=s=1800x700:legend=1:scale=log:fscale=log", os.path.join(OUT, "spectrogram.png")])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mix_path, "-filter_complex",
                "showwavespic=s=1800x300:split_channels=1", "-frames:v", "1", os.path.join(OUT, "waveform.png")])

# ---- markdown summary ----
L = []
m = res["mix"]
L.append(f"# Render metrics\n\nMix: {m['I_LUFS']} LUFS integrated, LRA {m['LRA_LU']} LU, true peak {m['true_peak_dBFS']} dBFS, "
         f"sample peak {m['sample_peak']:.3f}. {len(bars)} bars. Levels are plain RMS dB per bar (not K-weighted).\n")
L.append("## Long-term spectrum, 1/3-octave bands relative to 1 kHz (mix vs Dvorak 9/i Columbia reference)\n")
L.append("| Hz | " + " | ".join(m["ltas"]) + " |\n|---|" + "---|" * len(m["ltas"]))
L.append("| mix | " + " | ".join(str(v) for v in m["ltas"].values()) + " |")
if "ref_ltas_dvorak9_i" in res:
    L.append("| ref | " + " | ".join(str(v) for v in res["ref_ltas_dvorak9_i"].values()) + " |")
L.append("\n## Band shares of total energy (dB): mix vs references (c09)\n")
L.append("| | " + " | ".join(m["shares"]) + " |\n|---|" + "---|" * len(m["shares"]))
L.append("| mix | " + " | ".join(str(v) for v in m["shares"].values()) + " |")
for k in ("dvorak9_i", "brahms1_ii", "brahms4_ii"):
    if f"ref_shares_{k}" in res:
        L.append(f"| {k} | " + " | ".join(str(res[f"ref_shares_{k}"].get(b, "")) for b in m["shares"]) + " |")
L.append("\n## Mix level per bar (dB)\n")
L.append(" ".join(f"{i + 1}:{v}" for i, v in enumerate(m["bar_db"])))
L.append("\n## Stems: median level (dB) of bars where the track plays, by printed dynamic\n")
L.append("| track | peak | " + " | ".join(n for _, n in DYN_NAMES) + " |\n|---|---|" + "---|" * len(DYN_NAMES))
for name, e in stems.items():
    md = e.get("median_db_by_dynamic", {})
    L.append(f"| {name} | {e['peak']} | " + " | ".join(str(md.get(n, "")) for _, n in DYN_NAMES) + " |")
if rets:   # mvt1 c50
    L.append("\n## Return stems (c50): peak, whole-file RMS (dB), median of the bars where the mix is above -60 dB\n")
    L.append(f"All return stems against all instrument stems (energy): {res['returns_re_dry_db']:+.2f} dB. The mix "
             "(00_Master.wav) is the sum of both.\n")
    L.append("| return | peak | RMS | median bar |\n|---|---|---|---|")
    for name, e in rets.items():
        bl = [v for v, mv in zip(e["bar_db"], m["bar_db"]) if mv > -60]
        L.append(f"| {name} | {e['peak']} | {e['rms_db']} | {round(float(np.median(bl)), 1) if bl else ''} |")
L.append(f"\n## Silent notes (c40): notes of {SILENT_MIN_QN} qn or longer more than {SILENT_UNDER_DB:g} dB (A) under the "
         "track's median at the same printed dynamic\n")
L.append("\n".join(f"- {r['track']} qn {r['sq']} pitch {r['pitch']} ({r['dyn']}): {r['db_a']} dB A, track median "
                    f"{r['track_median_db_a']}" for r in silent) if silent else "none")
L.append("\n## Loudest three stems per bar (dB), bars where anything plays\n")
for bi in range(len(bars)):
    lv = sorted(((e["bar_db"][bi], n) for n, e in stems.items() if e.get("active", [True] * len(bars))[bi]), reverse=True)[:3]
    if lv:
        L.append(f"- bar {bi + 1} (mix {m['bar_db'][bi]}): " + ", ".join(f"{n} {v}" for v, n in lv))
open(os.path.join(OUT, "metrics.md"), "w").write("\n".join(L) + "\n")
print(os.path.join(OUT, "metrics.md"))

"""Measure a mockup render: mix loudness, per-bar levels of the mix and of every stem, level per printed dynamic,
long-term spectrum against a reference recording, and spectrogram pictures.

Usage: python measure.py <render-dir> <parts.json> <out-dir>
  render-dir holds 00_Master.wav and NN_<track>.wav stems (REAPER render, RENDER_SETTINGS=1).
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
for p in sorted(glob.glob(os.path.join(RENDER, "[0-9][0-9]_*.wav"))):
    name = os.path.basename(p)[3:-4]
    if name == "Master":
        continue
    x, _ = sf.read(p)
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
L.append("\n## Loudest three stems per bar (dB), bars where anything plays\n")
for bi in range(len(bars)):
    lv = sorted(((e["bar_db"][bi], n) for n, e in stems.items() if e.get("active", [True] * len(bars))[bi]), reverse=True)[:3]
    if lv:
        L.append(f"- bar {bi + 1} (mix {m['bar_db'][bi]}): " + ", ".join(f"{n} {v}" for v, n in lv))
open(os.path.join(OUT, "metrics.md"), "w").write("\n".join(L) + "\n")
print(os.path.join(OUT, "metrics.md"))

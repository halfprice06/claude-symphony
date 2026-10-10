#!/usr/bin/env python3
"""r03/r04: render any version folder of either movement to MP3 with one command.

Usage: python3 render.py --score <symphony/mvtX/vNN> --out <file.mp3> [--work /tmp/render-03] [--jobs 4]
                         [--events EVENTS.tsv] [--midi-out <file.midi>] [--no-balance]
       (--v120 is kept as an alias of --score)

Steps
 1. copy <score>/score.midi (LilyPond output after fixmidi.py) to the work folder;
 2. lib/score_events.py: compile a scratch copy of the score's LilyPond source with an event-logging engraver and
    list every printed note with its articulations, slur position, technique and dynamic (notes.csv); r03: bar
    numbers from the MIDI's time-signature grid (mixed metre);
 3. articulate.py: write the rendering MIDI (articulation lengths and channels, CC11 dynamics, CC20 dynamic curve,
    percussion read from the score's DrumStaff if it has one) into the work folder (and --midi-out if given;
    never into the code folder or a score folder);
 4. split it into one MIDI per staff and render each with stem.py (stage 1: synthesis, gains, tone, brightness;
    stage 2: pan and room) in parallel;
 5. r03: mix-stage balance (lib/balance.py): marked melodies derived from the score's text marks (lib/marks.py) and
    timpani rolls longer than a bar, measured on the placed stems; slow gain curves; the affected stems are placed
    again from their stage-1 signal;
 r04: the balance obeys the printed dynamics (lib/balance.py docstring); --reuse-synth for tuning runs.
 6. sum the stems, r04: zero-phase mix-bus EQ (lib/busq.py, config master.eq), gain to the target integrated loudness (linear, no dynamic compression), true-peak
    limiter only if the true peak would exceed the ceiling, encode MP3.
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import soundfile as sf
import mido

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


def split_stems(midi, outdir):
    m = mido.MidiFile(midi)
    groups = defaultdict(list)
    for i, tr in enumerate(m.tracks[1:], 1):
        if any(not x.is_meta for x in tr) and any(x.type == "note_on" for x in tr):
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


def ebur128(path):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    s = r[r.rfind("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", s).group(1))
    LRA = float(re.search(r"LRA:\s+(-?[\d.]+) LU", s).group(1))
    TP = float(re.search(r"Peak:\s+(-?[\d.inf]+) dBFS", s).group(1))
    return I, LRA, TP


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--score", "--v120", dest="score", required=True, help="score version folder (score.midi + LilyPond source)")
    ap.add_argument("--work", default="/tmp/render-04")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--events", help="reuse an events.tsv from an earlier run of the same score (skips the LilyPond compile)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--midi-out", help="also copy the rendering MIDI here")
    ap.add_argument("--no-balance", action="store_true", help="skip the mix-stage balance (for A/B tests)")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    ap.add_argument("--keep-synth", action="store_true", help="keep the stage-1 stem signals (*_syn.wav)")
    ap.add_argument("--reuse-synth", action="store_true", help="r04 (tuning): reuse kept stage-1 signals whose stem MIDI, stem config and synth code are unchanged (implies --keep-synth)")
    a = ap.parse_args()
    t_start = time.time()
    score = os.path.abspath(a.score)
    cfg = json.load(open(a.config))
    W = os.path.abspath(a.work); os.makedirs(W, exist_ok=True)
    stems_dir = os.path.join(W, "stems"); os.makedirs(stems_dir, exist_ok=True)
    src_midi = os.path.join(W, "score.midi")
    shutil.copy(os.path.join(score, "score.midi"), src_midi)
    # 2. printed events
    notes = os.path.join(W, "notes.csv")
    events = a.events or os.path.join(W, "ly_scratch", "events.tsv")
    cmd = [sys.executable, os.path.join(HERE, "lib", "score_events.py"), "--midi", src_midi, "--out", notes,
           "--ly-dir", score, "--scratch", os.path.join(W, "ly_scratch"), "--summary", os.path.join(W, "articulation_midi.json")]
    if a.events:
        cmd += ["--events", a.events]
        os.makedirs(os.path.join(W, "ly_scratch"), exist_ok=True)
        if os.path.abspath(a.events) != os.path.abspath(events := os.path.join(W, "ly_scratch", "events.tsv")):
            shutil.copy(a.events, events)
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    print(f"[{time.time()-t_start:5.1f}s] score events -> {notes}", flush=True)
    # 3. rendering MIDI
    r_midi = os.path.join(W, "render.midi")
    subprocess.run([sys.executable, os.path.join(HERE, "articulate.py"), src_midi, notes, a.config,
                    r_midi, "--report", os.path.join(W, "articulate_report.json"), "--score", score], check=True)
    if a.midi_out:
        shutil.copy(r_midi, a.midi_out)
    print(f"[{time.time()-t_start:5.1f}s] articulated MIDI -> {r_midi}", flush=True)
    # 4. stems: synthesis (kept as *_syn.wav) and placement
    mids = split_stems(r_midi, stems_dir)
    import hashlib
    gl = {k: v for k, v in cfg.items() if k not in ("stems", "balance", "master", "melodies", "balance_targets_dB")}
    def one(item):
        g, p = item
        w = p[:-4] + ".wav"
        syn = p[:-4] + "_syn.wav"
        st = key(g)
        h = hashlib.sha1(open(p, "rb").read() + json.dumps([cfg["stems"].get(g), gl], sort_keys=True).encode()
                         + open(os.path.join(HERE, "stem.py"), "rb").read() + open(os.path.join(HERE, "sfzplay.py"), "rb").read()).hexdigest()
        hf = syn + ".sha1"
        if a.reuse_synth and os.path.exists(syn) and os.path.exists(hf) and open(hf).read() == h:
            # r04: stage-1 signal unchanged (same stem MIDI, stem config and synth code): place only
            subprocess.run([sys.executable, os.path.join(HERE, "stem.py"), p, w, "--config", a.config, "--from-synth", syn], check=True)
        else:
            subprocess.run([sys.executable, os.path.join(HERE, "stem.py"), p, w, "--config", a.config, "--synth-out", syn], check=True)
            open(hf, "w").write(h)
        return g, w
    with ThreadPoolExecutor(a.jobs) as ex:
        wavs = dict(ex.map(one, sorted(mids.items())))
    print(f"[{time.time()-t_start:5.1f}s] {len(wavs)} stems rendered", flush=True)
    sr = cfg["sample_rate"]
    # 5. mix-stage balance
    B = cfg.get("balance", {})
    if B.get("enabled", True) and not a.no_balance:
        import marks, balance, rtk
        mi = rtk.midi_info(src_midi)
        bars = [(b["bar"], b["t_start"], b["t_end"]) for b in mi["per_bar"]]
        rows = list(csv.DictReader(open(notes, encoding="utf-8")))
        M = cfg.get("melodies", {})
        mel = marks.melodies(events, rows, mi["bar_s"], tpb=mi["tpb"], pattern=M.get("pattern", r"espr|dolce|cantabile|solo"),
                             max_bars=M.get("max_bars", 8))
        rl = marks.rolls(rows, mi["bar_s"])
        by = defaultdict(list)
        for r in rows:
            by[key(r["midi_track"]) if r["midi_track"] else key(r["staff"])].append(r)
        def lv(g):
            x, _ = sf.read(wavs[g], dtype="float64", always_2d=True)
            return g, balance.bar_levels(x, sr, by.get(g, []), bars)
        with ThreadPoolExecutor(a.jobs) as ex:
            lvs = dict(ex.map(lv, sorted(wavs)))
        levels = {g: v[0] for g, v in lvs.items()}; whole = {g: v[1] for g, v in lvs.items()}
        gains, rep_bal, mels = balance.compute(levels, bars, mel, rl, B, whole=whole, pdyn=balance.printed_dyn(rows))
        rep_bal["derived_melodies"] = [(s, bs[0], bs[-1], txt) for s, bs, _, _, txt in mel]
        rep_bal["balanced_phrases"] = [(s, bs[0], bs[-1]) for s, bs in mels]
        end_s = max(e for _, _, e in bars) + 1.0
        todo = []
        for g, gb in gains.items():
            if gb:
                cp = mids[g][:-4] + "_gain.npy"
                np.save(cp, balance.curve(gb, bars, end_s, B.get("smooth_s", 0.4)))
                todo.append((g, cp))
        def again(item):
            g, cp = item
            p = mids[g]
            subprocess.run([sys.executable, os.path.join(HERE, "stem.py"), p, wavs[g], "--config", a.config,
                            "--from-synth", p[:-4] + "_syn.wav", "--gain-curve", cp], check=True)
        with ThreadPoolExecutor(a.jobs) as ex:
            list(ex.map(again, todo))
        json.dump(rep_bal, open(os.path.join(W, "balance_report.json"), "w"), indent=1)
        print(f"[{time.time()-t_start:5.1f}s] balance: {len(mel)} melodies, {len(rl)} rolls, {len(todo)} stems re-placed", flush=True)
    # 6. mix and master
    mix = None
    for g, w in wavs.items():
        x, r = sf.read(w, dtype="float64", always_2d=True)
        if mix is None:
            mix = x
        else:
            if len(x) > len(mix):
                mix = np.vstack([mix, np.zeros((len(x) - len(mix), 2))])
            mix[:len(x)] += x
    # trim trailing near-silence (keep the room tail down to -90 dBFS)
    env = np.abs(mix).max(axis=1)
    last = np.nonzero(env > 10 ** (-90 / 20) * env.max())[0][-1]
    mix = mix[:last + int(0.2 * sr)]
    if not (a.keep_synth or a.reuse_synth):
        for p in mids.values():
            if os.path.exists(p[:-4] + "_syn.wav"):
                os.remove(p[:-4] + "_syn.wav")
    # r04 (critic 3, plan 4): zero-phase mix-bus EQ against the low-mid build-up of stacked sample ambience and the
    # dull 5-8 kHz band (third-octave LTAS against Brahms 1 and 4, NOTES.md)
    import busq
    mix = busq.apply(mix, sr, cfg["master"].get("eq", []))
    pre = os.path.join(W, "mix_prem.wav")
    sf.write(pre, mix.astype(np.float32), sr, subtype="FLOAT")
    I, LRA, TP = ebur128(pre)
    Mst = cfg["master"]
    g = Mst["target_LUFS"] - I
    print(f"premaster I {I:.1f} LUFS, LRA {LRA:.1f} LU, true peak {TP:.1f} dBTP; gain {g:+.2f} dB; peak after gain {TP+g:.1f} dBTP", flush=True)
    master = os.path.join(W, "master.wav")
    af = f"volume={g:.3f}dB"
    if TP + g > Mst["true_peak_dBTP"] - 0.3:
        # limiter on a 4x oversampled signal, ceiling 0.5 dB under the target true peak, slow release
        lim = 10 ** ((Mst["true_peak_dBTP"] - 0.5) / 20)
        af += f",aresample={4*sr},alimiter=limit={lim:.4f}:attack=5:release=200:level=false:asc=true,aresample={sr}"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", pre, "-af", af, "-c:a", "pcm_f32le", master], check=True)
    I2, LRA2, TP2 = ebur128(master)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", master, "-c:a", "libmp3lame", "-b:a", Mst["mp3_bitrate"], a.out], check=True)
    I3, LRA3, TP3 = ebur128(a.out)
    rep = {"score": score, "premaster": {"I": I, "LRA": LRA, "TP": TP}, "gain_dB": g, "master_wav": {"I": I2, "LRA": LRA2, "TP": TP2},
           "mp3": {"I": I3, "LRA": LRA3, "TP": TP3}, "seconds": round(time.time() - t_start, 1)}
    json.dump(rep, open(os.path.join(W, "render_report.json"), "w"), indent=1)
    print(json.dumps(rep))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Printed articulations, slurs, dynamics and techniques for every note, matched to MIDI notes.

Compiles a scratch copy of the LilyPond score with tools/ly/eventlog.ily (an engraver that logs every
note and post-event), then matches each printed note to a note in a MIDI file by staff, onset and pitch.

Usage:
  python3 score_events.py --midi score.midi --out notes.csv [--ly-dir /mnt/project-files/symphony/mvt1/v120]
                          [--scratch DIR] [--events events.tsv] [--summary summary.json]

notes.csv columns: staff, voice, bar, beat, tick_on, notated_ticks (ties merged), pitch, dyn (printed dynamic
in force), hairpin (cresc/decresc running), arts (staccato|accent|tenuto|marcato|fermata|tremolo32|...),
slur (start|in|end|''), tech (pizz|arco|sul tasto|''), midi_track, midi_on, midi_off, midi_len, midi_vel,
t_on_s, t_off_s (seconds of the MIDI note), notated_s (seconds of the notated length).
The scratch compile never touches mvt1/. --events reuses an existing events.tsv instead of compiling.
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, tempfile
from collections import defaultdict
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rtk

HERE = os.path.dirname(os.path.abspath(__file__))
WHOLE = 4  # quarter notes per whole note


def key(name):
    return re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()


def compile_events(ly_dir, scratch):
    os.makedirs(scratch, exist_ok=True)
    for f in os.listdir(ly_dir):
        p = os.path.join(ly_dir, f)
        if f.endswith((".ly", ".ily")):
            shutil.copy(p, scratch)
        elif f == "sections":
            shutil.copytree(p, os.path.join(scratch, f), dirs_exist_ok=True)
    s = open(os.path.join(scratch, "score.ly"), encoding="utf-8").read()
    inc = '\\include "%s"' % os.path.join(HERE, "ly", "eventlog.ily")
    s = re.sub(r'(\\language\s+"[^"]+")', r"\1\n" + inc.replace("\\", "\\\\"), s, count=1) if "\\language" in s else inc + "\n" + s
    open(os.path.join(scratch, "logged.ly"), "w", encoding="utf-8").write(s)
    subprocess.run(["lilypond", "-dno-print-pages", "-o", "logged", "logged.ly"], cwd=scratch,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return os.path.join(scratch, "events.tsv")


def parse_events(path):
    notes, posts = [], defaultdict(list)
    for line in open(path, encoding="utf-8", errors="replace"):
        f = line.rstrip("\n").split("\t")
        if len(f) < 8 or float(f[4] or 0) != 0.0:  # skip grace notes
            continue
        kind, staff, voice, pos = f[0], key(f[1]), f[2], round(float(f[3]), 6)
        if kind == "note":
            notes.append({"staff": staff, "voice": voice, "pos": pos, "dur": float(f[5]), "pitch": int(f[6])})
        else:
            posts[(staff, voice, pos)].append(f[7])
    return notes, posts


def build(notes, posts):
    by_voice = defaultdict(list)
    for n in notes:
        by_voice[(n["staff"], n["voice"])].append(n)
    # staff-wide state from post events (dynamics, techniques) in score order
    staff_ev = defaultdict(list)
    for (st, vo, pos), evs in posts.items():
        for e in evs:
            staff_ev[st].append((pos, e))
    # r05: at one position, hairpin stops first, then dynamics, then hairpin starts (r04 sorted the strings, so
    # 'cresc-1' came before 'dyn:p' and the dynamic cleared the hairpin that starts with it: every note printed
    # '\p\<' lost its hairpin, among them the timpani rolls; critic 4, 5.2)
    def _ord(e):
        if e in ("cresc1", "decresc1"):
            return 0
        if e.startswith("dyn:"):
            return 1
        if e in ("cresc-1", "decresc-1"):
            return 2
        return 3
    for st in staff_ev:
        staff_ev[st].sort(key=lambda z: (z[0], _ord(z[1]), z[1]))
    out = []
    for (st, vo), ns in by_voice.items():
        ns.sort(key=lambda n: (n["pos"], n["pitch"]))
        slur_open = False; pend_tie = {}
        sev = staff_ev[st]; k = 0; dyn = None; hp = ""; tech = ""
        for n in ns:
            while k < len(sev) and sev[k][0] <= n["pos"] + 1e-9:
                e = sev[k][1]
                if e.startswith("dyn:"):
                    dyn = e[4:].replace("sub. ", ""); hp = ""
                elif e in ("cresc-1", "decresc-1"):
                    hp = e[:-2]
                elif e in ("cresc1", "decresc1"):
                    hp = ""
                elif e.startswith("text:"):
                    t = e[5:].strip().rstrip(".")
                    if t in ("pizz", "arco", "sul tasto", "ord"):
                        tech = "" if t in ("arco", "ord") else t
                k += 1
            evs = posts.get((st, vo, n["pos"]), [])
            arts = sorted({e[4:] for e in evs if e.startswith("art:")} | {e for e in evs if e.startswith("tremolo")})
            starts = "slur-1" in evs; ends = "slur1" in evs
            if starts:
                sl = "start"
            elif ends and slur_open:
                sl = "end"
            elif slur_open:
                sl = "in"
            else:
                sl = ""
            if starts:
                slur_open = True
            if ends:
                slur_open = False
            # ties: continuation of a previous note of the same pitch
            if n["pitch"] in pend_tie and abs(pend_tie[n["pitch"]]["pos"] + pend_tie[n["pitch"]]["dur_total"] - n["pos"]) < 1e-6:
                head = pend_tie.pop(n["pitch"])
                head["dur_total"] += n["dur"]
                head["arts"] = sorted(set(head["arts"]) | set(a for a in arts if a == "fermata"))
                if "tie" in evs:
                    pend_tie[n["pitch"]] = head
                continue
            rec = {"staff": st, "voice": vo, "pos": n["pos"], "dur_total": n["dur"], "pitch": n["pitch"],
                   "dyn": dyn, "hairpin": hp, "arts": arts, "slur": sl, "tech": tech, "_sev": sev}
            out.append(rec)
            if "tie" in evs:
                pend_tie[n["pitch"]] = rec
    # r05 (critic 4, plan 1): dynamics and hairpins printed INSIDE a note (ties merged), and the first printed
    # dynamic within a quarter note after its end, as 'relpos:event;...' (relpos in whole notes from the note's start;
    # relpos >= the notated length = after the end). articulate.py builds timpani roll curves from it.
    for rec in out:
        sev = rec.pop("_sev"); a, L = rec["pos"], rec["dur_total"]
        inner = []; after = None
        for pos, e in sev:
            if not (e.startswith("dyn:") or e in ("cresc-1", "decresc-1", "cresc1", "decresc1")):
                continue
            if a + 1e-9 < pos < a + L - 1e-9:
                inner.append(f"{pos - a:g}:{e}")
            elif a + L - 1e-9 <= pos <= a + L + 0.25 + 1e-9 and e.startswith("dyn:") and after is None:
                after = f"{pos - a:g}:{e}"
        if after:
            inner.append(after)
        rec["inner"] = ";".join(inner)
    return out


def match_midi(recs, midi_path):
    mi = rtk.midi_info(midi_path)
    tpb = mi["tpb"]; t2s = mi["t2s"]
    # r03: bars from the MIDI's own time-signature grid (rtk.midi_info), not tick // whole (4/4 only): mixed metre
    # (mvt2: 3/4 + 4/4) gets the printed bar numbers
    import bisect
    grid = list(mi["bar_ticks"])
    idx = defaultdict(list)
    for (on, off, ti, ch, p, v, name) in mi["notes"]:
        idx[(key(name), int(round(on)))].append((on, off, p, v, name))
    rows = []
    for r in recs:
        tick = int(round(r["pos"] * WHOLE * tpb))
        cands = []
        for dt in (0, -1, 1, -2, 2):
            cands += [c for c in idx.get((r["staff"], tick + dt), []) if c[2] % 12 == r["pitch"] % 12]
        cands.sort(key=lambda c: (abs(c[2] - r["pitch"]) % 12 != 0, abs(c[2] - r["pitch"])))
        c = cands[0] if cands else None
        ntk = r["dur_total"] * WHOLE * tpb
        bi = max(0, bisect.bisect_right(grid, tick) - 1)
        bar = bi + 1
        row = {"staff": r["staff"], "voice": r["voice"], "bar": bar, "beat": round((tick - grid[bi]) / tpb + 1, 3),
               "tick_on": tick, "notated_ticks": int(round(ntk)), "pitch": r["pitch"], "dyn": r["dyn"] or "",
               "hairpin": r["hairpin"], "arts": "|".join(r["arts"]), "slur": r["slur"], "tech": r["tech"],
               "midi_track": c[4] if c else "", "midi_on": int(c[0]) if c else "", "midi_off": int(c[1]) if c else "",
               "midi_len": int(c[1] - c[0]) if c else "", "midi_vel": c[3] if c else "",
               "t_on_s": round(float(t2s(c[0] if c else tick)), 4),
               "t_off_s": round(float(t2s(c[1])), 4) if c else "",
               "notated_s": round(float(t2s(tick + ntk) - t2s(tick)), 4), "inner": r.get("inner", "")}
        rows.append(row)
    return rows


def summary(rows):
    """MIDI-side articulation check: does the MIDI make marked notes shorter/longer/louder?"""
    def cls(r):
        a = r["arts"].split("|") if r["arts"] else []
        if r["tech"] == "pizz": return "pizz"
        for k in ("staccato", "marcato", "accent", "tenuto"):
            if k in a: return k
        if any(x.startswith("tremolo") for x in a): return "tremolo"
        if r["slur"] in ("start", "in"): return "legato (slurred, not last)"
        if r["slur"] == "end": return "slur end"
        return "plain"
    S = defaultdict(list)
    for r in rows:
        if r["midi_len"] != "":
            S[cls(r)].append(r)
    out = {"matched_notes": sum(1 for r in rows if r["midi_len"] != ""), "unmatched_notes": sum(1 for r in rows if r["midi_len"] == "")}
    # velocity reference: median velocity of plain notes per (staff, bar)
    ref = defaultdict(list)
    for r in S["plain"] + S["legato (slurred, not last)"]:
        ref[(r["staff"], r["bar"])].append(r["midi_vel"])
    for c, rs in sorted(S.items()):
        ratio = [r["midi_len"] / r["notated_ticks"] for r in rs if r["notated_ticks"] > 0]
        dv = [r["midi_vel"] - np.median(ref[(r["staff"], r["bar"])]) for r in rs if ref.get((r["staff"], r["bar"]))]
        out[c] = {"n": len(rs), "midi_len_over_notated_median": round(float(np.median(ratio)), 3),
                  "midi_len_over_notated_p10_p90": [round(float(np.percentile(ratio, 10)), 3), round(float(np.percentile(ratio, 90)), 3)],
                  "vel_minus_plain_same_bar_median": round(float(np.median(dv)), 1) if dv else None}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--midi", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--ly-dir", help="score folder (required unless --events is given)")
    ap.add_argument("--scratch"); ap.add_argument("--events"); ap.add_argument("--summary")
    a = ap.parse_args()
    ev = a.events or compile_events(a.ly_dir, a.scratch or tempfile.mkdtemp(prefix="evlog_"))
    notes, posts = parse_events(ev)
    rows = match_midi(build(notes, posts), a.midi)
    with open(a.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    sm = summary(rows)
    if a.summary:
        rtk.save_json(sm, a.summary)
    print(json.dumps(sm, indent=1))


if __name__ == "__main__":
    main()

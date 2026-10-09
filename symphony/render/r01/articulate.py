#!/usr/bin/env python3
"""Rendering MIDI for r01: articulations, continuous dynamics and per-stem channels.

Usage: articulate.py IN.midi notes.csv config.json OUT.midi [--report report.json]

Reads v120's MIDI (unchanged LilyPond output) and notes.csv (tools/score_events.py: every printed note with
its articulations, slur position, technique and printed dynamic, matched to the MIDI note). Writes a MIDI with
the same tracks, track names, tempo map and note onsets, where

  * note lengths follow the printed articulation (legato overlap, detached gap, slur-end gap, staccato,
    tenuto) per instrument family;
  * string tremolo (:32) moves to a tremolo-strings channel (GM 44), pizz. to a pizzicato channel (GM 45),
    string staccato to a channel whose envelope release is shortened by SoundFont NRPN; measured
    tremolo (:16) becomes repeated 16th notes; timpani rolls become repeated strokes;
  * dynamics become a continuous CC11 (expression) curve per staff: extra range per printed step, hairpins
    as ramps also on held notes, accent / sf / fp shapes (loud attack, sustain back at the base level);
  * CC20 (undefined in GM, ignored by FluidSynth) carries the velocity-equivalent dynamic curve for the
    stem renderer's brightness filter;
  * channels are numbered inside each staff (0 main, 1 tremolo, 2 pizz, 3 string staccato); the file is
    meant to be split into one MIDI per staff (render.py / tools/stems.py do that), not played as a whole.
"""
import argparse, csv, json, math, re, sys
from bisect import bisect_right
from collections import defaultdict
import numpy as np
import mido

CH_MAIN, CH_TREM, CH_PIZZ, CH_STAC = 0, 1, 2, 3


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


class TempoMap:
    def __init__(self, mid):
        self.tpb = mid.ticks_per_beat
        ev = []
        for tr in mid.tracks:
            t = 0
            for m in tr:
                t += m.time
                if m.type == "set_tempo":
                    ev.append((t, m.tempo))
        ev.sort()
        if not ev or ev[0][0] > 0:
            ev.insert(0, (0, 500000))
        self.ticks = [e[0] for e in ev]; self.tempi = [e[1] for e in ev]
        self.secs = [0.0]
        for i in range(1, len(ev)):
            self.secs.append(self.secs[-1] + (self.ticks[i] - self.ticks[i - 1]) * self.tempi[i - 1] / 1e6 / self.tpb)

    def t2s(self, tick):
        i = bisect_right(self.ticks, tick) - 1
        return self.secs[i] + (tick - self.ticks[i]) * self.tempi[i] / 1e6 / self.tpb

    def s2t(self, s):
        i = bisect_right(self.secs, s) - 1
        return int(round(self.ticks[i] + (s - self.secs[i]) * 1e6 * self.tpb / self.tempi[i]))


def vel_dB(v):
    return 40.0 * math.log10(max(v, 1) / 127.0)


def notes_of(track):
    """(on_tick, off_tick, pitch, velocity, channel) of each note in a track."""
    t, act, out = 0, {}, []
    for m in track:
        t += m.time
        if m.type == "note_on" and m.velocity > 0:
            act.setdefault((m.channel, m.note), []).append((t, m.velocity))
        elif m.type in ("note_off", "note_on"):
            lst = act.get((m.channel, m.note))
            if lst:
                on, v = lst.pop(0)
                out.append([on, t, m.note, v, m.channel])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("midi"); ap.add_argument("notes"); ap.add_argument("config"); ap.add_argument("out")
    ap.add_argument("--report")
    a = ap.parse_args()
    cfg = json.load(open(a.config)); A = cfg["articulation"]
    mid = mido.MidiFile(a.midi)
    tm = TempoMap(mid)
    rows = list(csv.DictReader(open(a.notes, encoding="utf-8")))
    by_on = defaultdict(list)
    for r in rows:
        if r["midi_on"] != "":
            by_on[(r["midi_track"], int(r["midi_on"]))].append(r)

    # ---- collect notes per track, attach printed info
    tracks = []  # (track index, name, staff key, [note dicts])
    for i, tr in enumerate(mid.tracks):
        if i == 0:
            continue
        ns = notes_of(tr)
        if not ns:
            tracks.append((i, tr.name, key(tr.name), []))
            continue
        lst = []
        # match MIDI notes to printed notes: same track and onset; the printed pitch can differ from the MIDI
        # pitch by the staff's transposition (e.g. double basses sound an octave lower), so use the most
        # common pitch offset of the track, then sorted order within a chord
        offs = defaultdict(int)
        for on, off, p, v, ch in ns:
            for r in by_on.get((tr.name, on), []):
                offs[p - int(r["pitch"])] += 1
        d = max(offs, key=offs.get) if offs else 0
        for on, off, p, v, ch in ns:
            cands = by_on.get((tr.name, on), [])
            r = None
            if cands:
                r = min(cands, key=lambda q: abs(int(q["pitch"]) + d - p))
                if abs(int(r["pitch"]) + d - p) > 0:
                    r = None
            lst.append({"on": on, "off": off, "pitch": p, "vel": v, "ch": ch, "row": r, "track": i})
        tracks.append((i, tr.name, key(tr.name), lst))

    staff_notes = defaultdict(list)
    for i, name, st, lst in tracks:
        staff_notes[st] += lst

    stats = defaultdict(int)
    new_notes = defaultdict(list)  # track index -> list of [on, off, pitch, vel, ch]
    staff_info = {}
    for st, lst in staff_notes.items():
        scfg = cfg["stems"].get(st, {"family": "wind"})
        fam = scfg["family"]
        is_string = fam == "string"
        if st == "drums":
            for n in lst:
                new_notes[n["track"]].append([n["on"], n["off"], n["pitch"], n["vel"], 9])
            continue
        # -------- velocity-equivalent dynamic curve V(t) (seconds), from plain notes
        plain = defaultdict(list); hp_at = {}
        for n in lst:
            r = n["row"]
            arts = (r["arts"].split("|") if r and r["arts"] else [])
            if r is None or any(x in arts for x in ("accent", "marcato")) or r["dyn"] in ("sf", "fp") and is_event(r, lst):
                continue
            plain[n["on"]].append(n["vel"])
            if r["hairpin"]:
                hp_at[n["on"]] = True
        on_ticks = sorted(plain)
        pts_t, pts_v = [], []
        for k, tk in enumerate(on_ticks):
            v = float(np.median(plain[tk])); ts = tm.t2s(tk)
            if pts_t and not hp_at.get(on_ticks[k - 1]):
                # hold the previous value until just before this onset (step)
                pts_t.append(ts - 0.02); pts_v.append(pts_v[-1])
            pts_t.append(ts); pts_v.append(v)
        if not pts_t:
            pts_t, pts_v = [0.0], [64.0]
        Vt = np.array(pts_t); Vv = np.array(pts_v)

        def V(s):
            return float(np.interp(s, Vt, Vv))

        # -------- voices: next onset per voice for legato / gap rules
        voice_on = defaultdict(list)
        for n in lst:
            r = n["row"]
            if r:
                voice_on[(r["staff"], r["voice"], n["track"])].append(n)
        nxt = {}
        for vk, vn in voice_on.items():
            ons = sorted(set(n["on"] for n in vn))
            pitches_at = defaultdict(set)
            for n in vn:
                pitches_at[n["on"]].add(n["pitch"])
            for n in vn:
                j = bisect_right(ons, n["on"])
                if j < len(ons):
                    nxt[id(n)] = (ons[j], pitches_at[ons[j]])
        all_onsets = sorted(set(n["on"] for n in lst))

        accents = []  # (t_on_s, t_end_s, dip_dB)
        for n in lst:
            r = n["row"]; on, off, p, v = n["on"], n["off"], n["pitch"], n["vel"]
            ch = CH_MAIN
            if r is None:
                new_notes[n["track"]].append([on, off, p, v, ch]); stats["unmatched"] += 1
                continue
            arts = r["arts"].split("|") if r["arts"] else []
            tech = r["tech"]
            t0 = tm.t2s(on); t1 = tm.t2s(off); L = t1 - t0
            # ---- dynamics events on this note
            vb = V(t0)
            if r["dyn"] == "fp" and is_event(r, lst):
                v = 84; dip = vel_dB(53) - vel_dB(84)
                accents.append((t0, None, dip, on)); stats["fp"] += 1
            elif r["dyn"] == "sf" and is_event(r, lst):
                v = int(min(127, max(v, vb + A["sf_velocity_boost"])))
                accents.append((t0, None, max(-A["accent_dip_max_dB"], vel_dB(vb) - vel_dB(v)), on)); stats["sf"] += 1
            elif ("accent" in arts or "marcato" in arts) and fam in ("string", "brass", "wind"):
                accents.append((t0, None, max(-A["accent_dip_max_dB"], min(0.0, vel_dB(vb) - vel_dB(v))), on)); stats["accent"] += 1
            if "tenuto" in arts:
                v = min(127, v + A["tenuto_velocity"])
            if tech == "sul tasto":
                v = max(1, v + A["sul_tasto_velocity"])
            # ---- technique channels
            if is_string and tech == "pizz":
                ch = CH_PIZZ  # plucked: the note-off only starts the release, so end it early
                off = min(off, tm.s2t(t0 + min(A["pizz_len_frac"] * L, A["pizz_len_max_s"])))
                new_notes[n["track"]].append([on, max(off, on + 1), p, v, ch]); stats["pizz"] += 1
                continue
            if fam == "timp" and any(x.startswith("tremolo") for x in arts):
                rate = A["timp_roll_rate_hz"]; k = 0; s = t0
                rng = np.random.default_rng(on)
                while s < t1 - 0.5 / rate:
                    vv = V(s) + A["timp_roll_vel_offset"] + rng.uniform(-1, 1) * A["timp_roll_vel_jitter"]
                    new_notes[n["track"]].append([tm.s2t(s), tm.s2t(min(t1, s + 1.0 / rate)), p, int(np.clip(vv, 1, 127)), ch])
                    k += 1; s = t0 + k / rate
                stats["timp_roll_strokes"] += k; stats["timp_rolls"] += 1
                continue
            if is_string and "tremolo16" in arts:
                # measured tremolo: repeated 16th notes (sixteenth = quarter / 4)
                step = mid.ticks_per_beat // 4; k = 0
                while on + k * step < off:
                    s_on = on + k * step
                    new_notes[n["track"]].append([s_on, min(off, s_on + int(step * 0.85)), p, v, ch]); k += 1
                stats["tremolo16_notes"] += 1
                continue
            if is_string and "tremolo32" in arts:
                ch = CH_TREM
                new_notes[n["track"]].append([on, off, p, v, ch]); stats["tremolo_prog44"] += 1
                continue
            if fam in ("timp", "harp"):
                new_notes[n["track"]].append([on, off, p, v, ch]); continue
            # ---- lengths
            nx = nxt.get(id(n))
            contiguous = nx is not None and tm.t2s(nx[0]) - t1 < 0.03
            if "staccato" in arts:
                if is_string:
                    newL = min(L * A["staccato_frac_string"], A["staccato_max_s_string"]); ch = CH_STAC
                else:
                    newL = min(L * A["staccato_frac_wind"], A["staccato_max_s_wind"])
                off = tm.s2t(t0 + newL); stats["staccato"] += 1
            elif "tenuto" in arts or "fermata" in arts:
                if contiguous and p in nx[1]:
                    off = tm.s2t(tm.t2s(nx[0]) - 0.02)
                stats["tenuto/fermata"] += 1
            elif r["slur"] in ("start", "in") and contiguous:
                if p in nx[1]:
                    off = tm.s2t(tm.t2s(nx[0]) - 0.03)
                else:
                    off = tm.s2t(tm.t2s(nx[0]) + A["legato_overlap_s"])
                stats["legato"] += 1
            elif r["slur"] == "end" or r["slur"] in ("start", "in"):
                gap = min(max(L * A["slur_end_gap_frac"], A["slur_end_gap_min_s"]), A["slur_end_gap_max_s"])
                off = tm.s2t(t1 - min(gap, 0.4 * L)); stats["slur_end"] += 1
            else:
                gap = min(max(L * A["detached_gap_frac"], A["detached_gap_min_s"]), A["detached_gap_max_s"])
                off = tm.s2t(t1 - min(gap, (1 - A["detached_min_frac"]) * L)); stats["detached"] += 1
            if "marcato" in arts:
                off = min(off, tm.s2t(t0 + 0.8 * L))
            new_notes[n["track"]].append([on, max(off, on + 1), p, int(v), ch])

        staff_info[st] = {"V": (Vt, Vv), "accents": accents, "onsets": [tm.t2s(x) for x in all_onsets], "fam": fam}

    # ---- resolve same-pitch overlaps per staff and channel
    for st, lst in staff_notes.items():
        tids = sorted(set(n["track"] for n in lst))
        allnotes = [(tid, nn) for tid in tids for nn in new_notes[tid]]
        byk = defaultdict(list)
        for tid, nn in allnotes:
            byk[(nn[4], nn[2])].append(nn)
        for k, ns in byk.items():
            ns.sort(key=lambda z: (z[0], -z[1]))
            for x, y in zip(ns, ns[1:]):
                if y[0] < x[1]:
                    if y[1] < x[1]:
                        y[1] = x[1]
                    x[1] = y[0]
                    stats["overlap_trimmed"] += 1
            for nn in ns:
                if nn[1] <= nn[0]:
                    nn[1] = nn[0] + 1

    # ---- controller curves per staff
    D = cfg["dynamics"]["extra_dB_points"]
    dx = np.array([p[0] for p in D], float); dy = np.array([p[1] for p in D], float)
    end_s = tm.t2s(max(n[1] for tid in new_notes for n in new_notes[tid]) + 1)
    grid = np.arange(0.0, end_s + 0.5, 0.02)
    cc_curves = {}
    for st, info in staff_info.items():
        Vt, Vv = info["V"]
        Vg = np.interp(grid, Vt, Vv)
        extra = np.interp(Vg, dx, dy) * cfg["stems"].get(st, {}).get("dyn_scale", 1.0)
        if info["fam"] not in ("timp", "harp"):
            # held notes under hairpins: follow V(t) relative to the value at the last onset in the staff
            ons = np.array(info["onsets"])
            idx = np.searchsorted(ons, grid, side="right") - 1
            v_last = np.where(idx >= 0, np.interp(ons[np.clip(idx, 0, None)], Vt, Vv), Vg)
            hold = 40 * np.log10(np.maximum(Vg, 1) / np.maximum(v_last, 1))
            extra = extra + hold
        acc = np.zeros_like(grid)
        ons = np.array(info["onsets"])
        for (t0, _, dip, on) in info["accents"]:
            j = np.searchsorted(ons, t0 + 1e-3)
            tn = ons[j] if j < len(ons) else t0 + 4.0
            tn = min(tn, t0 + 4.0)
            s0, s1 = t0 + A["accent_dip_start_s"], t0 + A["accent_dip_full_s"]
            if tn <= s0:
                continue
            m = (grid >= s0) & (grid < tn)
            ramp = np.clip((grid[m] - s0) / (s1 - s0), 0, 1)
            acc[m] = np.minimum(acc[m], dip * ramp)
        expr = extra + acc
        cc11 = np.clip(np.round(127 * 10 ** (expr / 40.0)), 1, 127).astype(int)
        cc20 = np.clip(np.round(Vg), 0, 127).astype(int)
        cc_curves[st] = (cc11, cc20)
        staff_info[st]["expr_dB_range"] = [float(expr.min()), float(expr.max())]

    # ---- channel trims (CC7) so that tremolo / pizz programs sit at the arco level
    cal = cfg["program_sfcal_LUFS_vel64"]
    out = mido.MidiFile(type=1, ticks_per_beat=mid.ticks_per_beat)
    out.tracks.append(mid.tracks[0])
    first_track_of = {}
    for i, name, st, lst in tracks:
        first_track_of.setdefault(st, i)
    for i, tr in enumerate(mid.tracks):
        if i == 0:
            continue
        st = key(tr.name)
        progs = [m.program for m in tr if m.type == "program_change"]
        prog = progs[0] if progs else 0
        ev = []  # (tick, order, msg)
        for m in tr:
            if m.is_meta and m.type in ("track_name", "instrument_name", "key_signature", "time_signature"):
                ev.append((0, 0, m.copy(time=0)))
        if st == "drums":
            for m in tr:
                if m.type == "program_change":
                    ev.append((0, 1, m.copy(time=0, channel=9)))
        else:
            fam = cfg["stems"].get(st, {}).get("family", "wind")
            chans = {CH_MAIN: prog}
            if fam == "string":
                chans.update({CH_TREM: A["tremolo_program"], CH_PIZZ: A["pizz_program"], CH_STAC: prog})
            arco = cal.get(str(prog), -31.5)
            trims = {}
            for c, pg in chans.items():
                t = arco - cal.get(str(pg), arco) if c in (CH_TREM, CH_PIZZ) else 0.0
                if c == CH_PIZZ:
                    t += A["pizz_rel_arco_dB"]
                trims[c] = t
            top = max(trims.values())
            for c, pg in chans.items():
                ev.append((0, 1, mido.Message("program_change", channel=c, program=pg)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=7, value=int(round(127 * 10 ** ((trims[c] - top) / 40))))))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=10, value=64)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=91, value=0)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=93, value=0)))
            if top > 0:
                # the renderer adds this gain back (CC7 can only attenuate)
                ev.append((0, 0, mido.MetaMessage("text", text=f"r01 stem trim +{top:.2f} dB")))
            if fam == "string" and i == first_track_of[st]:
                # SoundFont NRPN (MSB 120, LSB = generator 38 releaseVolEnv): shorter release on the staccato
                # channel, and optionally on the main channel (config stems.<staff>.main_release_timecents)
                rel = [(CH_STAC, A["string_staccato_release_timecents"])]
                if cfg["stems"][st].get("main_release_timecents"):
                    rel.append((CH_MAIN, cfg["stems"][st]["main_release_timecents"]))
                for c, tc in rel:
                    data = int(8192 + tc / 2)  # FluidSynth scales NRPN data for envelope times by 2 timecents
                    for cc, val in ((99, 120), (98, 38), (38, data & 0x7F), (6, data >> 7)):
                        ev.append((0, 3, mido.Message("control_change", channel=c, control=cc, value=val)))
            if i == first_track_of[st] and st in cc_curves:
                cc11, cc20 = cc_curves[st]
                last11 = last20 = None
                for g, s in enumerate(grid):
                    tk = tm.s2t(s)
                    if cc11[g] != last11:
                        for c in chans:
                            ev.append((tk, 4, mido.Message("control_change", channel=c, control=11, value=int(cc11[g]))))
                        last11 = cc11[g]
                    if cc20[g] != last20:
                        ev.append((tk, 4, mido.Message("control_change", channel=CH_MAIN, control=20, value=int(cc20[g]))))
                        last20 = cc20[g]
        for on, off, p, v, ch in new_notes.get(i, []):
            ev.append((on, 6, mido.Message("note_on", channel=ch, note=p, velocity=int(max(1, min(127, v))))))
            ev.append((off, 5, mido.Message("note_off", channel=ch, note=p, velocity=0)))
        ev.sort(key=lambda z: (z[0], z[1]))
        nt = mido.MidiTrack(); last = 0
        for tk, _, m in ev:
            nt.append(m.copy(time=tk - last)); last = tk
        nt.append(mido.MetaMessage("end_of_track", time=0))
        out.tracks.append(nt)
    out.save(a.out)
    rep = {"stats": dict(stats), "expr_dB_range": {s: i.get("expr_dB_range") for s, i in staff_info.items()}}
    if a.report:
        json.dump(rep, open(a.report, "w"), indent=1)
    print(json.dumps(rep["stats"]))


_event_cache = {}


def is_event(r, lst):
    """True if this note is the first note of its staff where the printed dynamic (sf / fp) appears."""
    k = (r["staff"], r["dyn"], r["tick_on"])
    if k in _event_cache:
        return _event_cache[k]
    st_rows = sorted({(int(n["row"]["tick_on"]), n["row"]["dyn"]) for n in lst if n["row"]})
    prev = None; first = set()
    for tk, d in st_rows:
        if d != prev and d in ("sf", "fp"):
            first.add((tk, d))
        prev = d
    for tk, d in st_rows:
        _event_cache[(r["staff"], d, str(tk))] = (tk, d) in first
    return _event_cache.get(k, False)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rendering MIDI for r02: articulations, continuous dynamics and per-stem channels.

Usage: articulate.py IN.midi notes.csv config.json OUT.midi [--report report.json]

Reads v120's MIDI (unchanged LilyPond output) and notes.csv (tools/score_events.py: every printed note with
its articulations, slur position, technique and printed dynamic, matched to the MIDI note). Writes a MIDI with
the same tracks, track names, tempo map and note onsets, where

  * note lengths follow the printed articulation (legato overlap, detached gap, slur-end gap, staccato,
    tenuto) per instrument family. r02: every rule starts from the NOTATED length (notes.csv notated_s); r01
    started from the MIDI length, which LilyPond had already halved for staccato notes (double shortening);
  * strings: tremolo (:32), pizz., staccato, accented and slurred notes each get their own channel
    (1 tremolo, 2 pizz, 3 staccato, 4 accent, 5 legato, 0 other); the stem renderer maps each channel to an
    articulation sample set (VPO through sfzplay.py) or to a GM program (FluidSynth fallback);
    measured tremolo (:16) becomes repeated 16th notes; timpani rolls become repeated strokes;
  * dynamics become a continuous CC11 (expression) curve: extra range per printed step, hairpins as ramps
    also on held notes, accent / sf / fp shapes (loud attack, sustain back at the base level).
    r02: woodwind and brass staves get one curve and one channel PER VOICE TRACK (one, two, shared, solo), so an
    accent or a new onset in one voice no longer moves the held note of another voice; strings, timpani and
    harp keep one curve per staff;
  * r02: a fixed headroom (config dynamics.headroom_dB) is taken off every CC11 curve and given back as stem gain
    by stem.py, so crescendos on held notes at f/ff can rise without hitting CC11 = 127;
  * printed fff notes are played 'fff_velocity_cut' velocity steps lower (LilyPond writes 127); r03: marked
    melodies are no longer lifted here (no bar lists): render.py balances them in the mix stage (lib/balance.py);
  * CC20 (undefined in GM, ignored by FluidSynth) carries the velocity-equivalent dynamic curve for the
    stem renderer's brightness filter;
  * r02: printed percussion that LilyPond's MIDI lacks (tam-tam) or reduces to one stroke (cymbal roll) is added
    as a separate track (perc.py);
  * channels are numbered inside each staff; the file is meant to be split into one MIDI per staff
    (render.py / tools/stems.py do that), not played as a whole.
"""
import argparse, csv, json, math, os, re, sys
from bisect import bisect_right
from collections import defaultdict
import numpy as np
import mido

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
sys.path.insert(0, HERE)

CH_MAIN, CH_TREM, CH_PIZZ, CH_STAC, CH_ACC, CH_LEG = 0, 1, 2, 3, 4, 5
# velocity-equivalent of each printed dynamic (v120 volume table x 127; fff after fff_velocity_cut)
DYN_VEL = {"ppp": 32, "pp": 42, "p": 53, "mp": 64, "mf": 74, "f": 84, "ff": 91, "fff": 110}


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
    ap.add_argument("--score", help="score folder being rendered (percussion is read from its LilyPond source)")
    a = ap.parse_args()
    cfg = json.load(open(a.config)); A = cfg["articulation"]
    mid = mido.MidiFile(a.midi)
    tm = TempoMap(mid)
    rows = list(csv.DictReader(open(a.notes, encoding="utf-8")))
    # r04: staves without a config entry borrow the entry of the instrument their name names (lib/staffmap.py)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
    import staffmap
    fb = staffmap.fill(cfg, set(key(tr.name) for tr in mid.tracks[1:]))
    if fb:
        print("articulate.py: config fallback for staves", fb, file=sys.stderr)
    by_on = defaultdict(list)
    for r in rows:
        if r["midi_on"] != "":
            by_on[(r["midi_track"], int(r["midi_on"]))].append(r)
    fff_cut = A.get("fff_velocity_cut", 0)
    # r03: velocity outliers against the printed dynamic. LilyPond scales velocities per instrument (so velocity is
    # not the printed dynamic), but some notes carry the dynamic state of another voice context (e.g. v156 Horns 1-2
    # 'shared' bars 132-137: printed mp, velocity 88-99, 12 dB above every other stem). A note outside a printed
    # hairpin whose velocity is more than vel_outlier_steps ABOVE the median of its staff, printed dynamic and accent
    # class (at least vel_outlier_min_n notes) gets that median (only upward outliers: a too-loud voice breaks the
    # balance; quieter entries can be deliberate).
    vo = A.get("vel_outlier_steps", 0)
    def vcls(r):
        a = r["arts"].split("|") if r["arts"] else []
        return (key(r["staff"]), r["dyn"], "acc" if ("accent" in a or "marcato" in a) else "")
    vgrp = defaultdict(list)
    for r in rows:
        if r["midi_vel"] != "" and r["dyn"] and not r["hairpin"]:
            vgrp[vcls(r)].append(int(r["midi_vel"]))
    vmed = {g: float(np.median(v)) for g, v in vgrp.items() if len(v) >= A.get("vel_outlier_min_n", 10)}

    # ---- collect notes per track, attach printed info
    tracks = []  # (track index, name, staff key, [note dicts])
    vel_fixed = [0]
    for i, tr in enumerate(mid.tracks):
        if i == 0:
            continue
        ns = notes_of(tr)
        if not ns:
            tracks.append((i, tr.name, key(tr.name), []))
            continue
        lst = []
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
            if r is not None and vo and r["dyn"] and not r["hairpin"] and vcls(r) in vmed and v - vmed[vcls(r)] > vo:
                v = int(round(vmed[vcls(r)])); vel_fixed[0] += 1
            is_roll = (r is not None and A.get("timp_roll_mode") == "sample" and key(r["staff"]).startswith("Timp")
                       and "tremolo" in (r["arts"] or ""))
            if r is not None and r["dyn"] == "fff" and fff_cut and not (is_roll and not A.get("timp_roll_fff_cut", True)):
                v = max(1, v - fff_cut)  # r02: LilyPond's fff = 127 stood 10 LU above the mix (critic 1, 3.6)
            lst.append({"on": on, "off": off, "pitch": p, "vel": v, "ch": ch, "row": r, "track": i})
        tracks.append((i, tr.name, key(tr.name), lst))

    staff_notes = defaultdict(list)
    for i, name, st, lst in tracks:
        staff_notes[st] += lst
    # r02: dynamics units: one per voice track for woodwinds and brass, one per staff otherwise
    per_track = set(cfg["dynamics"].get("per_track_families", ["wind", "brass"]))
    track_rank = {}
    ROLE = {"one": 0, "two": 1, "shared": 2, "solo": 3}
    for st in staff_notes:
        tids = sorted(set(n["track"] for n in staff_notes[st]))
        roles = [mid.tracks[t].name.split(":")[-1].strip() if ":" in mid.tracks[t].name else "" for t in tids]
        if cfg["stems"].get(st, {}).get("artic_channels") and all(r in ROLE or r == "" for r in roles) and len(set(roles)) == len(roles):
            # r03: sample-set staves: the voice role (one, two, shared = a2, solo) fixes the channel, so the config
            # can give single players solo samples and the shared (a2) voice section samples
            for tid, r in zip(tids, roles):
                track_rank[tid] = ROLE.get(r, 0)
        else:
            for k, tid in enumerate(tids):
                track_rank[tid] = k

    stats = defaultdict(int)
    new_notes = defaultdict(list)  # track index -> list of [on, off, pitch, vel, ch]
    unit_info = {}
    lst_by_unit = {}
    for st, lst_all in staff_notes.items():
        scfg = cfg["stems"].get(st, {"family": "wind"})
        fam = scfg["family"]
        is_string = fam == "string"
        if st == "drums":
            for n in lst_all:
                new_notes[n["track"]].append([n["on"], n["off"], n["pitch"], n["vel"], 9])
            continue
        if fam in per_track:
            units = defaultdict(list)
            for n in lst_all:
                units[(st, n["track"])].append(n)
            units = list(units.items())
        else:
            units = [((st, None), lst_all)]
        for ukey, lst in units:
            # -------- velocity-equivalent dynamic curve V(t) (seconds), from plain notes
            plain = defaultdict(list); hp_at = {}
            for n in lst:
                r = n["row"]
                arts = (r["arts"].split("|") if r and r["arts"] else [])
                if r is None or any(x in arts for x in ("accent", "marcato")) or r["dyn"] in ("sf", "fp") and is_event(r, lst_all):
                    continue
                plain[n["on"]].append(n["vel"])
                if r["hairpin"]:
                    hp_at[n["on"]] = True
            on_ticks = sorted(plain)
            pts_t, pts_v = [], []
            for k, tk in enumerate(on_ticks):
                v = float(np.median(plain[tk])); ts = tm.t2s(tk)
                if pts_t and not hp_at.get(on_ticks[k - 1]):
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

            accents = []; timp_rolls = []; timp_roll_dyn = []
            acc_extra = scfg.get("accent_extra_vel", 0)
            for n in lst:
                r = n["row"]; on, off, p, v = n["on"], n["off"], n["pitch"], n["vel"]
                ch = CH_MAIN
                if r is None:
                    new_notes[n["track"]].append([on, off, p, v, ch]); stats["unmatched"] += 1
                    continue
                arts = r["arts"].split("|") if r["arts"] else []
                tech = r["tech"]
                t0 = tm.t2s(on)
                # r02: lengths from the notated length (LilyPond halves staccato notes in its MIDI)
                L = float(r["notated_s"]) if r.get("notated_s") not in (None, "") else tm.t2s(off) - t0
                t1 = t0 + L
                off = max(on + 1, tm.s2t(t1))
                vb = V(t0)
                accented = False
                if r["dyn"] == "fp" and is_event(r, lst_all):
                    v = 84; dip = vel_dB(53) - vel_dB(84)
                    accents.append((t0, None, dip, on)); stats["fp"] += 1
                elif r["dyn"] == "sf" and is_event(r, lst_all):
                    v = int(min(127, max(v, vb + A["sf_velocity_boost"])))
                    accents.append((t0, None, max(-A["accent_dip_max_dB"], vel_dB(vb) - vel_dB(v)), on)); stats["sf"] += 1
                    accented = True
                elif ("accent" in arts or "marcato" in arts) and fam in ("string", "brass", "wind", "timp"):
                    v = min(127, v + acc_extra)
                    if fam != "timp":
                        accents.append((t0, None, max(-A["accent_dip_max_dB"], min(0.0, vel_dB(vb) - vel_dB(v))), on))
                    stats["accent"] += 1; accented = True
                if "tenuto" in arts:
                    v = min(127, v + A["tenuto_velocity"])
                if tech == "sul tasto":
                    v = max(1, v + A["sul_tasto_velocity"])
                # ---- technique channels
                if is_string and tech == "pizz":
                    ch = CH_PIZZ
                    off = min(off, tm.s2t(t0 + min(A["pizz_len_frac"] * L, A["pizz_len_max_s"])))
                    new_notes[n["track"]].append([on, max(off, on + 1), p, v, ch]); stats["pizz"] += 1
                    continue
                if fam == "timp" and any(x.startswith("tremolo") for x in arts) and A.get("timp_roll_mode") == "sample":
                    # r02: a recorded roll (VPO timpani-roll.sfz, looped with a crossfade) on channel 1, one
                    # note for the whole roll; an optional soft stroke on channel 0 marks the start. The fade
                    # (settle) and hairpins are written into the CC11 curve below (timp_rolls).
                    cresc = r["hairpin"] in ("cresc", "<", "crescendo")
                    new_notes[n["track"]].append([on, off, p, v, CH_TREM])
                    if A.get("timp_roll_start_stroke_vel") is not None:
                        new_notes[n["track"]].append([on, min(off, tm.s2t(t0 + 0.3)), p, int(np.clip(v + A["timp_roll_start_stroke_vel"], 1, 127)), CH_MAIN])
                    timp_rolls.append((t0, t1, cresc, L)); stats["timp_rolls"] += 1
                    timp_roll_dyn.append((t0, t1, cresc, L, r["dyn"], p))
                    continue
                if fam == "timp" and any(x.startswith("tremolo") for x in arts):
                    rate = A["timp_roll_rate_hz"]; k = 0; s = t0
                    rng = np.random.default_rng(on)
                    # r02 (Dan, 2026-10-09): a roll starts at its printed dynamic, then settles below the attack
                    # level; only a printed crescendo makes it grow (V(t) follows the hairpin); long rolls (longer
                    # than timp_roll_long_s) sink a further timp_roll_long_dB to sit under the texture
                    cresc = r["hairpin"] in ("cresc", "<", "crescendo")
                    while s < t1 - 0.5 / rate:
                        el = s - t0
                        vv = V(s) + (0 if k == 0 else A["timp_roll_vel_offset"]) + (0 if k == 0 else rng.uniform(-1, 1) * A["timp_roll_vel_jitter"])
                        if not cresc and k > 0:
                            settle = A["timp_roll_settle_dB"] * (1 - math.exp(-el / A["timp_roll_settle_tau_s"]))
                            if L > A["timp_roll_long_s"]:
                                settle += A["timp_roll_long_dB"] * min(1.0, el / A["timp_roll_long_s"])
                            vv = max(1.0, vv) * 10 ** (settle / 40)
                        new_notes[n["track"]].append([tm.s2t(s), tm.s2t(min(t1, s + 1.0 / rate)), p, int(np.clip(vv, 1, 127)), ch])
                        k += 1; s = t0 + k / rate
                    stats["timp_roll_strokes"] += k; stats["timp_rolls"] += 1
                    continue
                if is_string and "tremolo16" in arts:
                    step = mid.ticks_per_beat // 4; k = 0
                    while on + k * step < off:
                        s_on = on + k * step
                        new_notes[n["track"]].append([s_on, min(off, s_on + int(step * 0.85)), p, v, ch]); k += 1
                    stats["tremolo16_notes"] += 1
                    continue
                if is_string and "tremolo32" in arts:
                    ch = CH_TREM
                    new_notes[n["track"]].append([on, off, p, v, ch]); stats["tremolo32"] += 1
                    continue
                if fam in ("timp", "harp"):
                    new_notes[n["track"]].append([on, off, p, v, ch]); continue
                # ---- lengths
                nx = nxt.get(id(n))
                contiguous = nx is not None and tm.t2s(nx[0]) - t1 < 0.03
                if "staccato" in arts:
                    v = min(127, v + scfg.get("staccato_extra_vel", 0))
                    if is_string:
                        newL = min(max(L * A["staccato_frac_string"], A["staccato_min_s_string"]), A["staccato_max_s_string"]); ch = CH_STAC
                    else:
                        newL = min(max(L * A["staccato_frac_wind"], A["staccato_min_s_wind"]), A["staccato_max_s_wind"])
                    newL = min(newL, L)
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
                    if is_string:
                        ch = CH_LEG
                    stats["legato"] += 1
                elif r["slur"] == "end" or r["slur"] in ("start", "in"):
                    gap = min(max(L * A["slur_end_gap_frac"], A["slur_end_gap_min_s"]), A["slur_end_gap_max_s"])
                    off = tm.s2t(t1 - min(gap, 0.4 * L)); stats["slur_end"] += 1
                else:
                    gap = min(max(L * A["detached_gap_frac"], A["detached_gap_min_s"]), A["detached_gap_max_s"])
                    off = tm.s2t(t1 - min(gap, (1 - A["detached_min_frac"]) * L)); stats["detached"] += 1
                if "marcato" in arts:
                    off = min(off, tm.s2t(t0 + 0.8 * L))
                if is_string and accented and ch in (CH_MAIN, CH_LEG) and A.get("string_accent_channel", True):
                    ch = CH_ACC; stats["string_accent_channel"] += 1
                if fam in ("wind", "brass") and scfg.get("artic_channels"):
                    # r03: wind / brass sample sets: channel offset 4 = staccato samples, 8 = accent samples
                    ch = 4 if "staccato" in arts else (8 if accented and scfg.get("artic_accent_channel", True) else 0)
                    stats["wind_artic_" + str(ch)] += 1
                new_notes[n["track"]].append([on, max(off, on + 1), p, int(v), ch])

            lst_by_unit[ukey] = lst
            unit_info[ukey] = {"V": (Vt, Vv), "accents": accents, "onsets": [tm.t2s(x) for x in all_onsets], "fam": fam,
                               "staff": st, "timp_rolls": timp_rolls, "timp_roll_dyn": timp_roll_dyn}

    # ---- r04 (critic 3, plan 7): section timing. Each staff (a section) moves as one unit: a family offset (strings
    # a little late on soft entries, brass slightly late, winds, harp and timpani on time) plus a random offset held
    # for a phrase-length segment (config timing.phrase_s), the same for every note of the staff in that segment.
    # Sources: https://forum.vsl.co.at/post/232667 ; https://vi-control.net/community/threads/timing-of-brass-strings.121576/
    TM = cfg.get("timing") or {}
    if TM.get("enabled"):
        soft = set(TM.get("soft_dyns", ["ppp", "pp", "p", "mp"]))
        for st, lst in staff_notes.items():
            fam = cfg["stems"].get(st, {}).get("family", "wind")
            if st == "drums":
                continue
            fo = TM.get("family_ms", {}).get(fam, [0, 0])  # [soft, loud]
            dyn_at = {}
            for n in lst:
                if n["row"]:
                    dyn_at[(n["track"], n["on"])] = n["row"]["dyn"]
            seed = sum(ord(ch) for ch in st) * 7919 + TM.get("seed", 1)
            rng = np.random.default_rng(seed)
            jit = {}
            for tid in sorted(set(n["track"] for n in lst)):
                for nn in new_notes[tid]:
                    ts = tm.t2s(nn[0])
                    seg = int(ts // TM.get("phrase_s", 8.0))
                    if seg not in jit:
                        jit[seg] = None
            for seg in sorted(jit):
                jit[seg] = float(rng.uniform(-1, 1) * TM.get("random_ms", 0.0))
            for tid in sorted(set(n["track"] for n in lst)):
                for nn in new_notes[tid]:
                    ts = tm.t2s(nn[0])
                    d = dyn_at.get((tid, nn[0]), "mf")
                    ms = (fo[0] if d in soft else fo[1]) + jit[int(ts // TM.get("phrase_s", 8.0))]
                    if abs(ms) < 0.5:
                        continue
                    sh = ms / 1000.0
                    on2 = tm.s2t(max(0.0, ts + sh)); off2 = tm.s2t(max(0.0, tm.t2s(nn[1]) + sh))
                    nn[0], nn[1] = on2, max(on2 + 1, off2)
                    stats["timing_shifted"] += 1

    # ---- resolve same-pitch overlaps per staff and channel (before voice channels are assigned)
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

    # ---- controller curves per dynamics unit
    D = cfg["dynamics"]["extra_dB_points"]
    dx = np.array([p[0] for p in D], float); dy = np.array([p[1] for p in D], float)
    headroom = cfg["dynamics"].get("headroom_dB", 0.0)
    end_s = tm.t2s(max(n[1] for tid in new_notes for n in new_notes[tid]) + 1)
    grid = np.arange(0.0, end_s + 0.5, 0.02)
    # r03: no CC11 melody lift here; marked melodies (derived from the score's text marks, lib/marks.py) are balanced
    # in the mix stage by render.py (lib/balance.py: a small lift on the melody, the rest as a cut on the accompaniment)
    mel = []
    cc_curves = {}
    for ukey, info in unit_info.items():
        st = info["staff"]
        Vt, Vv = info["V"]
        Vg = np.interp(grid, Vt, Vv)
        extra = np.interp(Vg, dx, dy) * cfg["stems"].get(st, {}).get("dyn_scale", 1.0)
        corr = cfg["stems"].get(st, {}).get("dyn_corr_dB")
        if corr:
            # r02: per-stem correction by printed dynamic, fitted from stem measurements (NOTES.md section 3)
            cp = sorted((DYN_VEL[d], x) for d, x in corr.items() if d in DYN_VEL)
            extra = extra + np.interp(Vg, [p[0] for p in cp], [p[1] for p in cp])
        if info["fam"] not in ("timp", "harp"):
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
        ptrim = cfg["stems"].get(st, {}).get("printed_trim_dB")
        if ptrim:
            # r03: trim by PRINTED dynamic (step curve from the notes' printed dynamic at their onsets)
            pd = sorted((tm.t2s(n["on"]), n["row"]["dyn"]) for n in lst_by_unit[ukey] if n["row"] and n["row"]["dyn"])
            if pd:
                pt = np.array([x[0] for x in pd]); pv = np.array([ptrim.get(x[1], 0.0) for x in pd])
                j = np.clip(np.searchsorted(pt, grid, side="right") - 1, 0, None)
                extra = extra + pv[j]
        lift = np.zeros_like(grid)
        for mst, ta, tb, db in mel:
            if mst == st:
                ramp = np.clip(np.minimum(grid - (ta - 0.3), (tb + 0.3) - grid) / 0.3, 0, 1)
                lift = np.maximum(lift, db * ramp)
        settle = np.zeros_like(grid)
        for (t0, t1, cresc, L) in info.get("timp_rolls", []):
            # r02 (Dan): a roll starts at its printed dynamic and settles below it; long rolls sink further;
            # a printed crescendo (hairpin) is left to V(t)
            if cresc:
                continue
            m = (grid >= t0) & (grid < t1 + 0.5)
            el = grid[m] - t0
            sd = A["timp_roll_settle_dB"] * (1 - np.exp(-el / A["timp_roll_settle_tau_s"]))
            if L > A["timp_roll_long_s"]:
                sd += A["timp_roll_long_dB"] * np.minimum(1.0, el / A["timp_roll_long_s"])
            settle[m] = np.minimum(settle[m], sd)
        for (t0, t1, cresc, L, dyn, pitch) in info.get("timp_roll_dyn", []):
            # r04 (critic 3, plan 2): trim by the roll's PRINTED dynamic so that roll start levels rise with it
            # (the global velocity curve is flat between f and fff; printed fff rolls started below f rolls), and by
            # the roll sample's own level per pitch (calib_timp_roll.py), so rolls on different drums match
            tr = A.get("timp_roll_trim_dB", {}).get(dyn, 0.0)
            pt = A.get("timp_roll_pitch_trim_dB", {})
            if pt:
                tr += pt.get(str(pitch), pt[min(pt, key=lambda q: abs(int(q) - pitch))])
            if tr:
                m = (grid >= t0 - 0.02) & (grid < t1 + 0.5)
                settle[m] += tr
        expr = extra + acc + lift + settle - headroom
        cc11 = np.clip(np.round(127 * 10 ** (expr / 40.0)), 1, 127).astype(int)
        cc20 = np.clip(np.round(Vg), 0, 127).astype(int)
        cc_curves[ukey] = (cc11, cc20)
        info["expr_dB_range"] = [float(expr.min()), float(expr.max())]
        info["cc11_capped_s"] = float(0.02 * (expr > 0).sum())

    # ---- write the MIDI
    cal = cfg["program_sfcal_LUFS_vel64"]
    out = mido.MidiFile(type=1, ticks_per_beat=mid.ticks_per_beat)
    out.tracks.append(mid.tracks[0])
    first_track_of = {}
    for i, name, st, lst in tracks:
        if lst:
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
        notes_i = new_notes.get(i, [])
        if st == "drums":
            for m in tr:
                if m.type == "program_change":
                    ev.append((0, 1, m.copy(time=0, channel=9)))
        else:
            fam = cfg["stems"].get(st, {}).get("family", "wind")
            if fam in per_track:
                ukey = (st, i); base = track_rank.get(i, 0)
                notes_i = [[on, off, p, v, base + ch] for on, off, p, v, ch in notes_i]
                chans = {base: prog}
                if cfg["stems"].get(st, {}).get("artic_channels"):
                    chans.update({base + 4: prog})
                    if cfg["stems"][st].get("artic_accent_channel", True):
                        chans.update({base + 8: prog})
                write_curve = ukey in cc_curves
            else:
                ukey = (st, None); base = 0
                chans = {CH_MAIN: prog}
                if fam == "timp" and A.get("timp_roll_mode") == "sample":
                    # r03 (critic 2, 5.1): the recorded rolls play on CH_TREM; the CC11 curve (settle, hairpins,
                    # per-stem corrections) must reach that channel too
                    chans[CH_TREM] = prog
                if fam == "string":
                    chans.update({CH_TREM: A["tremolo_program"], CH_PIZZ: A["pizz_program"], CH_STAC: prog, CH_ACC: prog, CH_LEG: prog})
                write_curve = i == first_track_of.get(st) and ukey in cc_curves
            arco = cal.get(str(prog), -31.5)
            trims = {}
            for c, pg in chans.items():
                t = arco - cal.get(str(pg), arco) if c in (CH_TREM, CH_PIZZ) and fam == "string" else 0.0
                if c == CH_PIZZ and fam == "string":
                    t += A["pizz_rel_arco_dB"]
                trims[c] = t
            top = max(trims.values())
            for c, pg in chans.items():
                ev.append((0, 1, mido.Message("program_change", channel=c, program=pg)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=7, value=int(round(127 * 10 ** ((trims[c] - top) / 40))))))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=10, value=64)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=91, value=0)))
                ev.append((0, 2, mido.Message("control_change", channel=c, control=93, value=0)))
            if top > 0 and i == first_track_of.get(st):
                ev.append((0, 0, mido.MetaMessage("text", text=f"r01 stem trim +{top:.2f} dB")))
            if fam == "string" and i == first_track_of.get(st):
                rel = [(CH_STAC, A["string_staccato_release_timecents"])]
                if cfg["stems"][st].get("main_release_timecents"):
                    rel += [(c, cfg["stems"][st]["main_release_timecents"]) for c in (CH_MAIN, CH_ACC, CH_LEG)]
                for c, tc in rel:
                    data = int(8192 + tc / 2)
                    for cc, val in ((99, 120), (98, 38), (38, data & 0x7F), (6, data >> 7)):
                        ev.append((0, 3, mido.Message("control_change", channel=c, control=cc, value=val)))
            if write_curve:
                cc11, cc20 = cc_curves[ukey]
                last11 = last20 = None
                for g, s in enumerate(grid):
                    tk = tm.s2t(s)
                    if cc11[g] != last11:
                        for c in chans:
                            ev.append((tk, 4, mido.Message("control_change", channel=c, control=11, value=int(cc11[g]))))
                        last11 = cc11[g]
                    if cc20[g] != last20:
                        ev.append((tk, 4, mido.Message("control_change", channel=base, control=20, value=int(cc20[g]))))
                        last20 = cc20[g]
        for on, off, p, v, ch in notes_i:
            ev.append((on, 6, mido.Message("note_on", channel=ch, note=p, velocity=int(max(1, min(127, v))))))
            ev.append((off, 5, mido.Message("note_off", channel=ch, note=p, velocity=0)))
        ev.sort(key=lambda z: (z[0], z[1]))
        nt = mido.MidiTrack(); last = 0
        for tk, _, m in ev:
            nt.append(m.copy(time=tk - last)); last = tk
        nt.append(mido.MetaMessage("end_of_track", time=0))
        out.tracks.append(nt)
    # r02: printed percussion that LilyPond's MIDI drops (tam-tam) or plays as one stroke (cymbal roll)
    if cfg.get("percussion"):
        import perc
        added = perc.apply(out, cfg, a.midi, a.score) if a.score else 0
        stats["percussion_events"] = added
    stats["velocity_outliers_fixed"] = vel_fixed[0]
    out.save(a.out)
    rep = {"stats": dict(stats), "melody_spans": [(s, round(x, 2), round(y, 2), d) for s, x, y, d in mel],
           "units": {f"{k[0]}/{k[1]}": {"expr_dB_range": v.get("expr_dB_range"), "cc11_capped_s": v.get("cc11_capped_s")} for k, v in unit_info.items()}}
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

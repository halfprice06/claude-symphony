"""mvt3 c17: instrument-side post-pass of score_to_parts.py (called at the end of build_track, config INSTR_POST).

Dan, 11 Nov: the track volume envelope holds slow balance only; no per-note fader move. Every level correction of a
single note goes to the instrument: CC11 / CC1 / CC7, velocity, note lengths, gaps. This module holds the generic rules;
their values are in build/score_config.py INSTR_POST = {rule: {track or family: ...}}. A track name wins over a family.

Rules (all optional):
  row_onset   {track: [{"row", "from", "to", "lead_s", "rr_leads_s": [..], "rr_pitch": p}]}: notes of a row start
              lead_s before their score onset (the length is kept); rr_leads_s gives one lead per round-robin position
              counted from the track's last CC16 reset (only for pitch rr_pitch when given)
  note_end    {track: [{"end": qn, "early_s": s}]}: notes that end at this score position end early_s sooner
  rebow_join  {track: [{"from", "to"} or {"at": [qn]}, "gap_s", "swell", "pre_s", "hold_s", "back_s", "lane"]}: at a
              same-pitch join on a sustained row the old note ends gap_s before the new note-on and the lane swells
  gap_set     {track/family: [{"from", "to", "min_qn", "gap_s", "rows"}]}: joins of long notes in a span take this gap
  gap_floor   {track/family: {"floor_s", "rows", "prev_rows", "cap_frac", "min_len_s", "skip": [(a, b)]}}: a tongued
              (not slurred) join on a monophonic line gets at least floor_s of played gap (the earlier note is shortened,
              by at most cap_frac of the onset distance)
  rest_map    {track/family: {lane: [(in, out), ...]}}: the lane's values pass through this piecewise-linear map (the
              resting level of plain notes; mix.json dyn_trim_db carries the level back)
  accent      {track/family: [{"lane", "amt": [(printed dynamic, units)] or "amt_rel": x, "max", "pre_s", "hold_s",
              "end_s", "rows", "skip_rows" (c24), "min_units"}]}: a printed accent is a lane bump from pre_s before the moved note-on, held
              hold_s, back by end_s (held to the end on notes shorter than 0.3 s); overlapping accents do not stack
  note_cc     {track/family: [{"lane", "rows", "from", "to", "pitch": {midi: units}, "row_dyn": {row: [(dyn, units)]},
              "chord": {n: units}, "add": units}]}: an offset held from each note-on to the next note-on ("add": the
              same offset on every note of the span, c18)
  c18 keys:   accent "tutti_scale": [(staves, factor), ...] (the bump is scaled by the number of staves that print an
              accent on the same score onset), "max_step" (the bumped value stands at most this many units over the
              lane's value on the note before, when that note is on the same row and ended less than 1 s earlier; never
              under "min_units");
              cc_shape "from_note": True (seconds count from the moved note-on of the note printed at "at");
              gap_floor "skip_long": [(from, to, min_qn)] (long notes of a span are left to gap_set);
              vel_cap {track: [{"row", "max", "min", "from", "to"}]}: a velocity ceiling / floor on a row;
              vol_guard "hairpin_ok" (moves that overlap a printed hairpin are left alone), "max_iter"
  cc_shape    {track: [{"lane", "at": qn, "pts": [(seconds from at, units)]}]}: an additive shape (c25 "no_pre_cap": True:
              the accent's pre-note ceiling does not hold inside it)
  cc_cap      {track: [{"lane", "pts": [(qn, ceiling)]}]}: the lane stays under this line (a held p after an sfp);
              c25 "acc_free": True: the ceiling holds the resting lane only, accent bumps go on top of it
  vel_pitch   {track: [{"row", "pitch": {midi: steps}, "from", "to"}]}: velocity offset by pitch
  vel_db      {track: [{"row", "table": {score qn: dB}, "steps_per_db"}]}: a fitted per-note level as velocity
  cc_scale    {track: [{"lane", "pts": [(qn, dB)], "k"}]}: the lane times 10^(dB / k) (a passage level inside the patch)
  cc_scale_k  {track/family: k}: the k of cc_scale rows that give none (c24: 20 on brass and clarinets, where CC11 is
              linear volume; default 40)
  note_merge  {track: [score qn]}: the note printed there is tied to the same-pitch note before it
  onset_lead  {track: [{"at": [score qn], "lead_s", "gap_s"}]}: listed notes start lead_s before the score onset
  vol_to_cc7  {track: {"shift_db", "keep_after": qn}}: the volume envelope before keep_after is folded into CC7 (linear
              amplitude in Opus: 20 log10(CC7 / 127)), less shift_db (which goes into the track gain)
  vol_guard   {"min_db", "win_s", "rate_db_s", "pre_s", "lead_max_s", "skip_after": qn}: a volume move of min_db or
              more within win_s that lies strictly inside a sounding note is moved to just before that note's moved
              note-on (when the move sits in the note's first lead_max_s) or stretched to rate_db_s
  c19 keys:   gap_set "pitch" / "skip_at" / negative gap_s (overlap), onset_lead "set" / "rows", accent "rest_amt" /
              "lead_key_s", note_shape, rr_each, vol_step_at {track: [{"at", "win_qn", "pre_s"}]} (see the code comments)
  dyn_step_on {"min_cc", "pre_s"}: jumps of the printed dynamic curve (parts.json dyn_curve, read by build_reaper.py
              for the dynamic trims) move from the score onset to just before the moved note-on
Returns a report dict (parts.json "instr_post").
"""
import bisect
import math


def _interp(tab, x):
    tab = sorted(tab)
    if x <= tab[0][0]:
        return tab[0][1]
    for (a, va), (b, vb) in zip(tab, tab[1:]):
        if x <= b:
            return va + (vb - va) * (x - a) / (b - a) if b > a else vb
    return tab[-1][1]


def _step_fn(pts):
    qs = [p[0] for p in pts]
    vs = [p[1] for p in pts]

    def f(q):
        i = bisect.bisect_right(qs, q + 1e-9) - 1
        return vs[i] if i >= 0 else (vs[0] if vs else 0)
    return f


def _lin_fn(ts, vs):
    def f(t):
        if not ts:
            return 0.0
        if t <= ts[0]:
            return vs[0]
        if t >= ts[-1]:
            return vs[-1]
        i = bisect.bisect_right(ts, t) - 1
        d = ts[i + 1] - ts[i]
        return vs[i] if d <= 0 else vs[i] + (vs[i + 1] - vs[i]) * (t - ts[i]) / d
    return f


def _pick(sec, tname, family):
    if not sec:
        return None
    return sec.get(tname, sec.get(family))


def _row(a, first_art):
    return str(a.get("_art") or first_art or "")


def _starts(row, prefixes):
    return any(row.startswith(p) for p in prefixes)


SHORT_ROWS = ("Stac", "Staccat", "Marc Shrt", "Spic", "Pizz", "Col Legno", "Bartok", "Ricochet", "Shorts", "Timpani")


def find_fast(ts, vs, t_end, min_db, win_s, step=0.005):
    """fast moves of a piecewise-linear lane: [(t_a, t_b, v_a, v_b)] where the lane moves min_db or more within win_s"""
    import numpy as np
    if len(ts) < 2:
        return []
    grid = np.arange(ts[0], min(ts[-1], t_end) + step, step)
    v = np.interp(grid, ts, vs)
    k = int(round(win_s / step))
    if len(v) <= k:
        return []
    d = np.abs(v[k:] - v[:-k]) >= min_db - 1e-6
    out, i, n = [], 0, len(d)
    while i < n:
        if d[i]:
            j = i
            while j + 1 < n and d[j + 1]:
                j += 1
            a, b = i, j + k
            # trim the flat ends of the window
            while a < b and abs(v[a + 1] - v[a]) < 1e-4:
                a += 1
            while b > a and abs(v[b] - v[b - 1]) < 1e-4:
                b -= 1
            out.append((float(grid[a]), float(grid[b]), float(v[a]), float(v[b])))
            i = j + k + 1
        else:
            i += 1
    return out


def inside_note(spans, t_a, t_b, edge_s):
    """the latest-started note that sounds from before t_a - edge to after t_b + edge, or None"""
    best = None
    for on, off in spans:
        if on + edge_s < t_a and off - edge_s > t_b and (best is None or on > best[0]):
            best = (on, off)
    return best


def apply(ctx):
    cfg = ctx["cfg"] or {}
    tname, family = ctx["tname"], ctx["family"]
    notes = ctx["out_notes"]
    S, Q = ctx["qn_to_sec"], ctx["sec_to_qn"]
    base = ctx["base"]
    first_art = ctx.get("first_art")
    rep = {}
    if not notes:
        return rep
    src = {}
    for n in ctx["ns"]:
        src.setdefault((round(n["qn"], 3), n["pitch"]), n)

    def sq_of(a):
        return a.get("sq", a["qn"])

    # ---------- note timing ----------
    for q_ in (cfg.get("note_merge") or {}).get(tname, []):
        # c18: [score qn, ...]: the note printed there is tied to the same-pitch note before it (a pedal marked "change
        # bow at will": the bow changes are placed by this list, not by the printed bar lines)
        for b in [a for a in notes if abs(sq_of(a) - q_) < 0.02]:
            prev = [a for a in notes if a is not b and a["pitch"] == b["pitch"] and a["qn"] < b["qn"]
                    and S(b["qn"]) - S(a["qn"] + a["dur"]) < 0.3]
            if not prev:
                continue
            a = max(prev, key=lambda a: a["qn"])
            a["dur"] = round(b["qn"] + b["dur"] - a["qn"], 4)
            notes.remove(b)
            rep.setdefault("note_merge", []).append([q_, b["pitch"]])
    for r in (cfg.get("onset_lead") or {}).get(tname, []):
        # c18: {"at": [score qn], "lead_s", "gap_s"}: the notes printed there start lead_s before the score onset and keep
        # their end; a same-pitch note before them ends gap_s before the moved note-on
        for b in [a for a in notes if any(abs(sq_of(a) - x) < 0.02 for x in r["at"])]:
            nq = round(Q(S(sq_of(b)) - r["lead_s"]), 4)
            # c23: "no_fall": the re-tongue CC11 fall before b is removed (also when b does not move)
            stay_ = abs(nq - b["qn"]) < 1e-4 or (nq >= b["qn"] and not r.get("set"))   # c19 "set": the lead may also shrink
            if stay_ and not r.get("no_fall"):
                continue
            if r.get("rows") and not _starts(_row(b, first_art), tuple(r["rows"])):
                continue
            old_on = b["qn"]
            if stay_:
                nq = b["qn"]
            else:
                b["dur"] = round(b["qn"] + b["dur"] - nq, 4)
                b["qn"] = nq
            for a in notes:
                if a is not b and a["pitch"] == b["pitch"] and a["qn"] < nq and a["qn"] + a["dur"] > Q(S(nq) - r.get("gap_s", 0.05)):
                    a["dur"] = round(max(0.05, Q(S(nq) - r.get("gap_s", 0.05)) - a["qn"]), 4)
            if ((r.get("move_fall") and nq < old_on - 1e-4) or r.get("no_fall")) and ctx.get("cc11"):
                # c22 (critic A #2): the re-tongue CC11 fall of a same-pitch note before b was built for the old note-on
                # (its bottom at the old onset, back up 0.1 s later): moved earlier, b started 8-10 units low and swelled
                # (chorale dips 0.6-2.8 dB). The fall keeps its shape in seconds and moves so that the lane is back at
                # its value 0.01 qn before the moved note-on; "fall_cc" sets a new depth
                if any(a is not b and a["pitch"] == b["pitch"] and a["qn"] < nq and S(nq) - S(a["qn"] + a["dur"]) < 0.3 for a in notes):
                    ln_ = ctx["cc11"]
                    win_ = [p_ for p_ in ln_ if old_on - 0.6 <= p_[0] <= old_on + 0.5]
                    if len(win_) >= 3:
                        qb_, vb_ = min((p_ for p_ in win_ if p_[0] <= old_on + 0.1), key=lambda p_: (p_[1], -p_[0]), default=(None, None))
                        pre_ = sorted(p_ for p_ in ln_ if qb_ is not None and qb_ - 0.6 <= p_[0] < qb_)
                        before_ = [p_ for p_ in ln_ if pre_ and p_[0] < pre_[0][0]]
                        # the lane's held value before the fall (a step lane: the last point before the window)
                        v0_ = None
                        if pre_:
                            v0_ = max(before_, key=lambda p_: p_[0])[1] if before_ else pre_[0][1]
                        post_ = sorted(p_ for p_ in ln_ if qb_ is not None and qb_ < p_[0] <= old_on + 0.5)
                        v1_ = post_[-1][1] if post_ else None
                        if qb_ is not None and v0_ is not None and v1_ is not None and min(v0_, v1_) - vb_ >= 3:
                            fs_ = pre_[0][0]            # fall start: the first point of the descent
                            re_ = min((p_[0] for p_ in post_ if p_[1] >= v1_ - 1), default=old_on + 0.5)   # back up
                            fall_s_, ret_s_ = S(qb_) - S(fs_), S(re_) - S(qb_)
                            depth_ = 0.0 if r.get("no_fall") else float(r.get("fall_cc", v0_ - vb_))
                            t_re = S(nq - 0.01)
                            t_b, t_f = t_re - ret_s_, t_re - ret_s_ - fall_s_
                            keep_ = [p_ for p_ in ln_ if not (min(fs_, Q(t_f)) - 1e-6 < p_[0] <= re_ + 1e-6)]
                            new_ = [(round(Q(t_f), 4), v0_), (round(Q(t_b), 4), int(round(max(1, v0_ - depth_)))), (round(Q(t_re), 4), v1_)]
                            # the lane is a step lane: the fall and the return as a staircase of 6 steps each
                            pts_ = []
                            for (qa_, va_), (qb2_, vb2_) in zip(new_, new_[1:]):
                                for j_ in range(6):
                                    pts_.append((round(qa_ + (qb2_ - qa_) * j_ / 6, 4), int(round(va_ + (vb2_ - va_) * j_ / 6))))
                            pts_.append(new_[-1])
                            ln_[:] = sorted([tuple(p_) for p_ in keep_] + pts_)
                            rep.setdefault("fall_moved", []).append([round(sq_of(b), 3), b["pitch"], round(qb_, 3), new_[1][0], int(depth_)])
            for k_ in ctx.get("ks") or []:
                if nq - 0.06 < k_["qn"] <= max(old_on, nq) + 1e-6 and k_["qn"] > min(old_on, nq) - 0.5:
                    k_["qn"] = round(nq - 0.06, 4)
            rep.setdefault("onset_lead", []).append([round(sq_of(b), 3), b["pitch"], nq])
    for r in (cfg.get("row_onset") or {}).get(tname, []):
        resets = sorted(t for t, _ in ctx.get("cc16") or [])
        cnt, last_reset, done = 0, None, 0
        for a in sorted(notes, key=lambda a: a["qn"]):
            if not _row(a, first_art).startswith(r["row"]):
                continue
            i = bisect.bisect_right(resets, a["qn"] + 1e-6) - 1
            rs = resets[i] if i >= 0 else None
            if rs != last_reset:
                cnt, last_reset = 0, rs
            k, cnt = cnt, cnt + 1
            if not (r["from"] - 1e-6 <= sq_of(a) < r["to"] - 1e-6):
                continue
            lead = r["lead_s"]
            if r.get("rr_leads_s") and (r.get("rr_pitch") is None or a["pitch"] == r["rr_pitch"]):
                lead = r["rr_leads_s"][k % len(r["rr_leads_s"])]
            old_on = a["qn"]
            a["qn"] = round(Q(S(sq_of(a)) - lead), 4)
            # a keyswitch placed for the old note-on must still come before the moved one (the row's first note)
            for k_ in ctx.get("ks") or []:
                if a["qn"] - r.get("ks_lead_qn", 0.06) < k_["qn"] <= old_on + 1e-6:
                    k_["qn"] = round(a["qn"] - r.get("ks_lead_qn", 0.06), 4)
                    rep.setdefault("ks_moved", []).append(k_["qn"])
            # and so must a round-robin reset (CC16) placed just before the old note-on
            c16 = ctx.get("cc16") or []
            for j_, (t_, v_) in enumerate(c16):
                if a["qn"] - 0.04 < t_ <= old_on + 1e-6:
                    c16[j_] = (round(a["qn"] - 0.1, 4), v_)
                    rep.setdefault("cc16_moved", []).append(c16[j_][0])
            done += 1
        rep.setdefault("row_onset", []).append([r["row"], r["from"], r["to"], done])
    for r in (cfg.get("note_end") or {}).get(tname, []):
        for a in notes:
            if abs(a["qn"] + a["dur"] - r["end"]) < r.get("tol", 0.08) and a["qn"] < r["end"] - 0.2 \
                    and (r.get("pitch") is None or a["pitch"] in r["pitch"]):
                if r.get("gap_next_s") is not None:
                    # c23 (critic C #1, ruling 1): end gap_next_s before the track's first note-on after this note's
                    # start that lies within tol of r["end"] (a lift before an arrival: the gap counts from the moved
                    # note-on, whatever the lead); only shortens
                    nx_ = [b["qn"] for b in notes if b["qn"] > a["qn"] + 0.2 and abs(b["qn"] - r["end"]) < r.get("tol", 0.08) + 0.3]
                    if not nx_:
                        continue
                    e = Q(S(min(nx_)) - r["gap_next_s"])
                    if e >= a["qn"] + a["dur"] - 1e-4:
                        continue
                else:
                    e = Q(S(a["qn"] + a["dur"]) - r["early_s"])
                a["dur"] = round(max(0.05, e - a["qn"]), 4)
                rep.setdefault("note_end", []).append([round(sq_of(a), 3), a["pitch"], round(a["qn"] + a["dur"], 4)])

    for r in (cfg.get("rr_each") or {}).get(tname, []):
        # c19: {"row", "from", "to", "pre_s", "skip_repeat"}: a round-robin reset (CC16 127) pre_s before every note of
        # the row in the span, so each key always plays the take that follows a reset (a pizzicato key's takes differ by
        # 5-10 dB); "skip_repeat": not before a note that repeats the pitch of the note before it (it plays the
        # second take, the same one in every render)
        c16 = ctx.get("cc16")
        if c16 is None:
            continue
        prev_p, n_ = None, 0
        for a in sorted(notes, key=lambda a: a["qn"]):
            if not _row(a, first_art).startswith(r["row"]) or not (r["from"] - 1e-6 <= sq_of(a) < r["to"] - 1e-6):
                prev_p = None
                continue
            if not (r.get("skip_repeat") and prev_p == a["pitch"]):
                t_ = round(Q(S(a["qn"]) - r.get("pre_s", 0.05)), 4)
                if not any(abs(t_ - c_[0]) < 0.011 for c_ in c16):
                    c16.append((t_, 127)); n_ += 1
            prev_p = a["pitch"]
        c16.sort()
        rep["rr_each"] = rep.get("rr_each", 0) + n_
    shapes = {"cc11": [], "cc1": []}     # additive polylines in seconds: [(t, units), ...]
    pend_swell = []
    for r in (cfg.get("rebow_join") or {}).get(tname, []):
        rows = tuple(r.get("rows", ("Sus",)))
        byp = {}
        for a in sorted(notes, key=lambda a: a["qn"]):
            byp.setdefault(a["pitch"], []).append(a)
        for p, l in byp.items():
            for a, b in zip(l, l[1:]):
                hit = (r.get("from") is not None and r["from"] - 1e-6 <= b["qn"] + 0.3 and b["qn"] < r["to"] - 1e-6
                       and b["qn"] >= r["from"] - 0.5) or any(abs(b["qn"] - x) < r.get("tol", 0.35) for x in r.get("at", []))
                if not hit or not (_starts(_row(a, first_art), rows + ("Leg",)) and _starts(_row(b, first_art), rows)):
                    continue
                tb = S(b["qn"])
                if S(a["qn"] + a["dur"]) < tb - 0.3:
                    continue   # a rest, not a join
                a["dur"] = round(max(0.05, Q(tb - r.get("gap_s", 0.005)) - a["qn"]), 4)
                if r.get("swell", 0):
                    pend_swell.append((r, tb, b["qn"]))
                rep.setdefault("rebow_join", []).append([round(b["qn"], 3), p])
    for r in _pick(cfg.get("gap_set"), tname, family) or []:
        # {"from", "to", "min_qn", "gap_s", "rows"}: joins of long notes in a span take this played gap (a chorale's breath)
        grp = {}
        for a in notes:
            grp.setdefault(round(a["qn"], 3), []).append(a)
        ks_ = sorted(grp)
        for ka, kb in zip(ks_, ks_[1:]):
            if len(grp[ka]) != 1 or len(grp[kb]) != 1:
                continue
            a, b = grp[ka][0], grp[kb][0]
            if not (r["from"] - 1e-6 <= sq_of(b) < r["to"] - 1e-6) or a["dur"] < r.get("min_qn", 3.0):
                continue
            # c19: "pitch": "diff" / "same" (joins that change / repeat the pitch only), "skip_at": [score onsets] (printed
            # breaths keep their gap); a negative gap_s is an overlap (polyphonic sustain rows only: never on a same-pitch
            # join, where the overlap would stop the new note, and never on a legato row)
            if (r.get("pitch") == "diff" and a["pitch"] == b["pitch"]) or (r.get("pitch") == "same" and a["pitch"] != b["pitch"]):
                continue
            if any(abs(sq_of(b) - x_) < 0.02 for x_ in r.get("skip_at", ())):
                continue
            if r.get("only_at") is not None and not any(abs(sq_of(b) - x_) < 0.02 for x_ in r["only_at"]):
                continue
            if r["gap_s"] < 0 and (a["pitch"] == b["pitch"] or (("Leg" in _row(a, first_art) or "Leg" in _row(b, first_art))
                                                             and not r.get("allow_leg"))):
                continue   # c22: "allow_leg": a legato join's overlap set to -gap_s (Flute 2's 0.17-0.20 s overlaps)
            if not (_starts(_row(a, first_art), tuple(r.get("rows", ("Sus",)))) and _starts(_row(b, first_art), tuple(r.get("rows", ("Sus",))))):
                continue
            gap = S(b["qn"]) - S(a["qn"] + a["dur"])
            if -0.25 <= gap <= 0.3 and abs(gap - r["gap_s"]) > 0.004:
                a["dur"] = round(Q(S(b["qn"]) - r["gap_s"]) - a["qn"], 4)
                rep.setdefault("gap_set", []).append([round(sq_of(b), 3), round(1000 * gap)])
    gf = _pick(cfg.get("gap_floor"), tname, family)
    if gf:
        rows, prows = tuple(gf.get("rows", ("Sus",))), tuple(gf.get("prev_rows", ("Sus", "Leg")))
        groups = {}
        for a in notes:
            groups.setdefault(round(a["qn"], 3), []).append(a)
        keys = sorted(groups)
        for ka, kb in zip(keys, keys[1:]):
            if len(groups[ka]) != 1 or len(groups[kb]) != 1:
                continue
            a, b = groups[ka][0], groups[kb][0]
            if any(x - 1e-6 <= sq_of(b) < y - 1e-6 for x, y in gf.get("skip", [])):
                continue
            if any(x - 1e-6 <= sq_of(b) < y - 1e-6 and a["dur"] >= m_ for x, y, m_ in gf.get("skip_long", [])):
                continue
            if not (_starts(_row(a, first_art), prows) and _starts(_row(b, first_art), rows)):
                continue
            if gf.get("min_dyn") is not None and base(sq_of(b)) < gf["min_dyn"] - 1e-6:
                continue
            na, nb = src.get((round(sq_of(a), 3), a["pitch"])), src.get((round(sq_of(b), 3), b["pitch"]))
            if na is None or nb is None or na is nb or ctx["same_slur"](na, nb) or nb.get("leg_target"):
                continue
            ta, tb = S(a["qn"]), S(b["qn"])
            gap = tb - S(a["qn"] + a["dur"])
            if gap >= gf["floor_s"] - 0.004 or gap > 0.3 or gap < -0.12:
                continue
            want = min(gf["floor_s"], gf.get("cap_frac", 0.45) * (tb - ta))
            te = max(tb - want, ta + gf.get("min_len_s", 0.07))
            if te >= S(a["qn"] + a["dur"]) - 0.002:
                continue
            a["dur"] = round(max(0.03, Q(te) - a["qn"]), 4)
            rep.setdefault("gap_floor", []).append([round(sq_of(b), 3), round(1000 * gap), round(1000 * (tb - te))])

    # ---------- lanes ----------
    groups = {}
    for a in notes:
        groups.setdefault(round(a["qn"], 3), []).append(a)
    keys = sorted(groups)
    acc_q = {round(q, 3) for q in ctx["accent_q"]}
    lanes = {"cc11": ctx["cc11"], "cc1": ctx["cc1"]}
    rmap = _pick(cfg.get("rest_map"), tname, family) or {}
    acc_rules = _pick(cfg.get("accent"), tname, family) or []
    off_rules = _pick(cfg.get("note_cc"), tname, family) or []
    free_win = {}   # c25: cc_shape "no_pre_cap" windows (seconds)
    for r in (cfg.get("cc_shape") or {}).get(tname, []):
        t0 = S(r["at"])
        if r.get("from_note"):   # c18: from the moved note-on of the note printed at "at" (none there: no shape)
            on_ = [a["qn"] for a in notes if abs(sq_of(a) - r["at"]) < 0.02]
            if not on_:
                continue
            t0 = S(min(on_))
        if r.get("hold_to") is not None:
            # c20: {"units", "hold_to": score qn}: a step of "units" at t0 held to 0.03 s before "hold_to" (an fff
            # arrival's level step held through the fff bar, to the next printed dynamic or rest)
            te_ = S(r["hold_to"]) - 0.03
            if te_ <= t0 + 0.02:
                continue
            shapes[r.get("lane", "cc11")].append([(t0 - 0.004, 0.0), (t0, r["units"]), (te_ - 0.004, r["units"]), (te_, 0.0)])
            rep["cc_shape"] = rep.get("cc_shape", 0) + 1
            continue
        shapes[r.get("lane", "cc11")].append([(t0 + x, d) for x, d in r["pts"]])
        if r.get("no_pre_cap"):
            # c25: the accent's pre-note ceiling (rest + bump, from just before the moved note-on) does not hold inside this
            # shape (a dynamic step moved ahead of a led note-on: the ceiling was taken from the lane before the step)
            free_win.setdefault(r.get("lane", "cc11"), []).append((t0 + r["pts"][0][0], t0 + r["pts"][-1][0]))
        rep["cc_shape"] = rep.get("cc_shape", 0) + 1
    for r in (cfg.get("note_shape") or {}).get(tname, []):
        # c19: {"lane", "rows", "from", "to", "min_qn", "units", "in_s", "out_s"}: every note of the rows in the span that
        # lasts min_qn or more gets an additive shape: 0 at the note-on, "units" from in_s after it to out_s before the
        # note-off, 0 at the note-off (a held note that swells inside the sample at a flat controller)
        for a in notes:
            if not (r.get("from", -1e9) - 1e-6 <= sq_of(a) < r.get("to", 1e9) - 1e-6) or a["dur"] < r.get("min_qn", 1.5):
                continue
            if r.get("rows") and not _starts(_row(a, first_art), tuple(r["rows"])):
                continue
            ta_, tb_ = S(a["qn"]), S(a["qn"] + a["dur"])
            if tb_ - ta_ < r.get("in_s", 0.35) + r.get("out_s", 0.3) + 0.1:
                continue
            shapes[r.get("lane", "cc11")].append([(ta_, 0.0), (ta_ + r.get("in_s", 0.35), r["units"]),
                                                  (tb_ - r.get("out_s", 0.3), r["units"]), (tb_, 0.0)])
            rep["note_shape"] = rep.get("note_shape", 0) + 1
    caps = {}
    for r in (cfg.get("cc_cap") or {}).get(tname, []):   # {"lane", "pts": [(qn, ceiling)]}: the lane stays under a line
        if r.get("to_note") is not None:
            # c20: the ceiling ends just before the moved note-on of the note printed at "to_note" (score qn): the
            # crescendo into an fff arrival stays under the ff ceiling up to the arrival itself, which then steps up
            on_ = [a["qn"] for a in notes if abs(sq_of(a) - r["to_note"]) < 0.02]
            if not on_:
                continue
            e_ = Q(S(min(on_)) - r.get("pre_s", 0.005))
            pv_ = _lin_fn([p_[0] for p_ in r["pts"]], [p_[1] for p_ in r["pts"]])(min(e_, r["pts"][-1][0]))
            r = dict(r, pts=[p_ for p_ in r["pts"] if p_[0] < e_ - 1e-4] + [(e_, pv_)])
            if len(r["pts"]) < 2:
                continue
        # c25 (ruling 8): "acc_free": True caps the resting lane only; accent bumps stand on top of the ceiling (the
        # 1040-1048 crescendo ceiling of the 1048 arrival had removed Trumpet 3's printed accent at 1044)
        caps.setdefault(r.get("lane", "cc11"), []).append(([p_[0] for p_ in r["pts"]], [p_[1] for p_ in r["pts"]], bool(r.get("acc_free"))))
        shapes[r.get("lane", "cc11")].append([(S(p_[0]), 0.0) for p_ in r["pts"]])   # its corners join the grid
        # c20: and a point just after its end, so the lane's own value returns there (an uncapped lane that rose under
        # the ceiling had no grid point of its own after it: brass CC1 stayed at 108 through the fff bar)
        shapes[r.get("lane", "cc11")].append([(S(r["pts"][-1][0]) + 0.001, 0.0), (S(r["pts"][-1][0]) + 0.002, 0.0)])
        for j in range(int((r["pts"][-1][0] - r["pts"][0][0]) / 0.125)):
            shapes[r.get("lane", "cc11")].append([(S(r["pts"][0][0] + 0.125 * j), 0.0), (S(r["pts"][0][0] + 0.125 * j) + 0.001, 0.0)])
        rep["cc_cap"] = rep.get("cc_cap", 0) + 1
    scales = {}
    for r in (cfg.get("cc_scale") or {}).get(tname, []):
        # c18: {"lane", "pts": [(qn, dB)], "k": 40}: the lane is multiplied by 10^(dB / k) along this line (0 dB at both
        # ends). c24 (critic B c24 #2, patch read and measured): on the brass and clarinet KS Masters (1FH, 1TP, 1TB, 1TU,
        # CL) CC11 drives Source/volume through a linear connection, so the level is 20 log10(CC11 / 127): k = 20 is
        # exact there (c22 -> c23 Horn 3 CC11 46 -> 73 measured +4.0 dB, Horn 4 46 -> 39 -1.4 dB); the c18 comment's
        # 40 log10 was wrong and every row written at k 40 delivered half its dB. "cc_scale_k" {track/family: k} sets the
        # k of rows that give none (default 40, the old value)
        ln_ = r.get("lane", "cc11")
        k0_ = _pick(cfg.get("cc_scale_k"), tname, family)
        scales.setdefault(ln_, []).append(([p_[0] for p_ in r["pts"]], [p_[1] for p_ in r["pts"]], float(r.get("k", k0_ if k0_ is not None else 40.0))))
        a_, b_ = r["pts"][0][0], r["pts"][-1][0]
        for j in range(int((b_ - a_) / 0.125) + 2):
            x_ = min(b_, a_ + 0.125 * j)
            shapes[ln_].append([(S(x_), 0.0), (S(x_) + 0.001, 0.0)])
        shapes[ln_].append([(S(p_[0]), 0.0) for p_ in r["pts"]] + [(S(r["pts"][-1][0]) + 0.001, 0.0)])
        rep["cc_scale"] = rep.get("cc_scale", 0) + 1
    acc_shapes = {"cc11": [], "cc1": []}
    pre_caps = {"cc11": [], "cc1": []}
    rest_fn = {}
    for ln in ("cc11", "cc1"):
        f0 = _step_fn(lanes[ln]) if lanes[ln] else None
        m = rmap.get(ln)
        rest_fn[ln] = (lambda q, f0=f0, m=m: (_interp(m, f0(q)) if m else f0(q))) if f0 else None
    for r, tb, qb in pend_swell:   # bow-change swells ("swell_rel": at most this share of the lane's value)
        ln = r.get("lane", "cc11")
        if rest_fn[ln] is None:
            continue
        sw = r["swell"]
        if r.get("swell_rel"):
            sw = min(sw, r["swell_rel"] * rest_fn[ln](qb + 0.01))
        shapes[ln].append([(tb - r.get("pre_s", 0.10), 0.0), (tb, sw), (tb + r.get("hold_s", 0.15), sw),
                           (tb + r.get("hold_s", 0.15) + r.get("back_s", 0.3), 0.0)])
    prev_val = {}   # c18: lane -> (end time, resting value incl. note_cc offsets) of the note before
    cm_ = _pick(cfg.get("cresc_mono"), tname, family)   # c22: {"lanes", "tol"}
    cresc_hp = sorted((h_[0], h_[1]) for h_ in (ctx.get("hairpins") or []) if len(h_) > 2 and h_[2] == "cresc") if cm_ else []
    cm_last = {}
    for i, k in enumerate(keys):
        g = groups[k]
        a0 = g[0]
        row = _row(a0, first_art)
        sq = sq_of(a0)
        t0 = S(a0["qn"])
        t_end = max(S(a["qn"] + a["dur"]) for a in g)
        t_next = S(groups[keys[i + 1]][0]["qn"]) if i + 1 < len(keys) else t_end + 1.0
        d = base(sq)
        off_on = {}
        for r in off_rules:
            ln = r.get("lane", "cc11")
            if rest_fn[ln] is None or (r.get("rows") and not _starts(row, tuple(r["rows"]))):
                continue
            if not (r.get("from", -1e9) - 1e-6 <= sq < r.get("to", 1e9) - 1e-6):
                continue
            u = float(r.get("add", 0.0))
            if r.get("pitch"):
                u += sum(r["pitch"].get(a["pitch"], r["pitch"].get(str(a["pitch"]), 0)) for a in g) / len(g)
            for rw, tab in (r.get("row_dyn") or {}).items():
                if row.startswith(rw):
                    u += _interp(tab, d)
            if r.get("beat"):   # {"period": qn, "on": units, "off": units}: by position in the beat
                u += r["beat"]["on"] if abs(sq / r["beat"].get("period", 2.0) - round(sq / r["beat"].get("period", 2.0))) < 0.01 else r["beat"]["off"]
            if r.get("chord") and len({a["pitch"] for a in g}) >= 2:
                u += r["chord"].get(min(len({a["pitch"] for a in g}), max(r["chord"])), 0)
            if abs(u) < 0.5:
                continue
            pad = r.get("pad_s", 0.02)
            tb = t_next - pad if t_next - t_end < 0.5 else t_end + 0.3
            shapes[ln].append([(t0 - pad - 0.004, 0.0), (t0 - pad, u), (tb - 0.004, u), (tb, 0.0)])
            off_on[ln] = off_on.get(ln, 0.0) + u
            rep["note_cc_" + ln] = rep.get("note_cc_" + ln, 0) + 1
        if cm_ and cresc_hp:
            # c22 (critic C #3, ruling 2): inside a printed crescendo the resting level (lane + note_cc offsets) of a note
            # does not fall under that of the note before in the same hairpin (a row offset such as Oboe 1's "Leg" -8 at
            # ff, or a falling note_cc, read as a dip inside the crescendo); the shortfall is added as a note_cc offset
            # (same row only, sustained rows only, not the hairpin's arrival note, at most "max" units; a note on another
            # row, a short row or the arrival starts the comparison again)
            hp_ = next(((ha_, hb_) for ha_, hb_ in cresc_hp if ha_ - 1e-6 <= sq < hb_ - 0.01), None)
            if _starts(row, SHORT_ROWS) or any(x_ - 1e-6 <= sq < y_ for x_, y_ in cm_.get("skip", ())):
                hp_ = None
            for ln in cm_.get("lanes", ("cc11",)):
                if rest_fn[ln] is None:
                    continue
                # the resting value in the note's body (40 % in, at most 0.6 s): not its front (an fp / sfp spike)
                v_ = rest_fn[ln](Q(t0 + min(0.4 * (t_end - t0), 0.6))) + off_on.get(ln, 0.0)
                last_ = cm_last.get(ln)
                if hp_ is not None and last_ is not None and last_[0] == hp_ and last_[2] == row and v_ < last_[1] - cm_.get("tol", 1.0):
                    u = min(last_[1] - v_, cm_.get("max", 8.0))
                    pad = 0.02
                    tb = t_next - pad if t_next - t_end < 0.5 else t_end + 0.3
                    shapes[ln].append([(t0 - pad - 0.004, 0.0), (t0 - pad, u), (tb - 0.004, u), (tb, 0.0)])
                    off_on[ln] = off_on.get(ln, 0.0) + u
                    v_ = v_ + u
                    rep.setdefault("cresc_mono", []).append([round(sq, 3), ln, round(u, 1)])
                cm_last[ln] = (hp_, v_, row) if hp_ is not None else None
        if round(sq, 3) in acc_q and not _starts(row, SHORT_ROWS):
            for r in acc_rules:
                ln = r.get("lane", "cc11")
                if rest_fn[ln] is None or (r.get("rows") and not _starts(row, tuple(r["rows"]))):
                    continue
                if r.get("skip_rows") and _starts(row, tuple(r["skip_rows"])):
                    continue   # c24: no bump on these rows (a marcato row carries its own front: Movement I c55)
                if not (r.get("from", -1e9) - 1e-6 <= sq < r.get("to", 1e9) - 1e-6):
                    continue   # c22: an accent rule may hold for a span only ("from" / "to", score qn)
                if r.get("min_dyn") is not None and d < r["min_dyn"] - 1e-6:
                    continue
                rest = rest_fn[ln](a0["qn"] + 0.01) + off_on.get(ln, 0.0)
                u = _interp(r["amt"], d) if "amt" in r else r["amt_rel"] * rest
                # c19 "rest_amt": [(rest from, rest to, units, row prefixes)]: the bump by the resting value (the steep
                # part of a row: +8 units were worth up to 6.5 dB on "Sus MAX" resting at 82-89)
                for lo_, hi_, u_, rw_ in r.get("rest_amt", ()):
                    if lo_ <= rest <= hi_ and _starts(row, tuple(rw_)):
                        u = min(u, u_)
                nst_ = (ctx.get("accent_staves") or {}).get(round(sq, 3), 1)
                for lim_, f_ in sorted(r.get("tutti_scale") or []):   # c18: many staves accent the same onset
                    if nst_ >= lim_:
                        u = (_interp(r["amt"], d) if "amt" in r else r["amt_rel"] * rest) * f_
                if nst_ >= min([l_ for l_, _ in r.get("tutti_scale") or []] or [1e9]):
                    rep["accent_tutti_" + ln] = rep.get("accent_tutti_" + ln, 0) + 1
                if r.get("max_step") is not None and prev_val.get(ln) is not None and t0 - prev_val[ln][0] < 1.0 \
                        and prev_val[ln][2] == row[:3]:
                    lim_u = prev_val[ln][1] + r["max_step"] - rest
                    if lim_u < u:
                        u = max(lim_u, r.get("min_units", 2))
                        rep["accent_step_cap_" + ln] = rep.get("accent_step_cap_" + ln, 0) + 1
                u = min(u, r.get("max", 127) - rest)
                if u < r.get("min_units", 2):
                    rep["accent_no_room"] = rep.get("accent_no_room", 0) + 1
                    continue
                pre, hold, end = r.get("pre_s", 0.02), r.get("hold_s", 0.15), r.get("end_s", 0.45)
                if t_end - t0 < 0.3:
                    hold, end = t_end - t0, t_end - t0 + 0.06
                if t_end - t0 >= 0.3 and end > t_end - t0:   # the bump is back before the note ends
                    end = t_end - t0
                    hold = min(hold, 0.5 * end)
                # c19 "lead_key_s": on a note led by more than this the bump's hold and end count from the score onset
                # (a bump keyed to the moved note-on of a legato target is over before the beat)
                ld_ = S(sq) - t0
                if r.get("lead_key_s") is not None and ld_ > r["lead_key_s"] and t_end - t0 >= 0.3:
                    hold, end = min(hold + ld_, 0.8 * (t_end - t0)), min(end + ld_, t_end - t0)
                    rep["accent_lead_keyed_" + ln] = rep.get("accent_lead_keyed_" + ln, 0) + 1
                acc_shapes[ln].append([(t0 - pre - 0.012, 0.0), (t0 - pre, u), (t0 + hold, u), (t0 + end, 0.0)])
                pre_caps[ln].append((t0 - pre - 0.012, t0 + 0.005, rest + u))   # before the note-on the lane may still stand on the phrase before
                rep["accents_" + ln] = rep.get("accents_" + ln, 0) + 1
        for ln in ("cc11", "cc1"):
            if rest_fn[ln] is not None:
                prev_val[ln] = (t_end, rest_fn[ln](a0["qn"] + 0.01) + off_on.get(ln, 0.0), row[:3])
    out_lanes = {}
    for ln in ("cc11", "cc1"):
        if rest_fn[ln] is None or not (rmap.get(ln) or shapes[ln] or acc_shapes[ln]):
            out_lanes[ln] = lanes[ln]
            continue
        bucket = {}

        def reg(sh, kind):
            f = _lin_fn([p[0] for p in sh], [p[1] for p in sh])
            for s in range(int(math.floor(sh[0][0])), int(math.floor(sh[-1][0])) + 1):
                bucket.setdefault(s, []).append((sh[0][0], sh[-1][0], f, kind))
        for sh in shapes[ln]:
            reg(sorted(sh), 0)
        for sh in acc_shapes[ln]:
            reg(sorted(sh), 1)
        ts = set(S(p[0]) for p in lanes[ln])
        for sh in shapes[ln] + acc_shapes[ln]:
            sh = sorted(sh)
            for (ta, va), (tb, vb) in zip(sh, sh[1:]):
                ts.add(ta); ts.add(tb)
                if abs(vb - va) > 0.5 and tb - ta > 0.02:
                    nst = int((tb - ta) / 0.015)
                    for j in range(1, nst + 1):
                        ts.add(ta + (tb - ta) * j / (nst + 1))
        out, last = [], None
        f = rest_fn[ln]
        for t in sorted(ts):
            q = Q(t)
            add, am = 0.0, 0.0
            for a_, b_, fn, kind in bucket.get(int(math.floor(t)), []):
                if a_ <= t <= b_:
                    if kind:
                        am = max(am, fn(t))
                    else:
                        add += fn(t)
            v = f(q) + add + am
            vr = f(q) + add   # c25: the resting part (without the accent bump), for "acc_free" caps
            for sq_, sd_, sk_ in scales.get(ln, []):   # c18 cc_scale: a level in dB as a factor on the lane
                if sq_[0] <= q <= sq_[-1]:
                    fac_ = 10 ** (_lin_fn(sq_, sd_)(q) / sk_)
                    v, vr = v * fac_, vr * fac_
            for cq, cv, cfree in caps.get(ln, []):
                if cq[0] <= q <= cq[-1]:
                    c_ = _lin_fn(cq, cv)(q)
                    if cfree:
                        v = min(vr, c_) + (v - vr)
                    else:
                        v = min(v, c_)
                    vr = min(vr, c_)
            for pa, pb, pc in pre_caps[ln]:
                if pa <= t <= pb and not any(fa_ <= t <= fb_ for fa_, fb_ in free_win.get(ln, ())):
                    v = min(v, pc)
            v = int(round(max(1, min(127, v))))
            if v != last:
                out.append((round(q, 4), v))
                last = v
        # equal positions: keep the last value
        ded = []
        for q, v in out:
            if ded and abs(ded[-1][0] - q) < 1e-6:
                ded[-1] = (q, v)
            else:
                ded.append((q, v))
        out_lanes[ln] = ded
    ctx["cc11"], ctx["cc1"] = out_lanes["cc11"], out_lanes["cc1"]

    # ---------- short-row controller park (c21) ----------
    # mvt3 c21 (critic B c21 #3; manual p.53 / p.64: velocity sets the dynamic of short articulations, CC11 the level of
    # sustained ones; research FINDINGS section 7: shorts park the CC high and take the dynamic from velocity):
    # short_cc_park {track/family: [{"rows": [prefixes], "cc11": value, "cc1_min": value, "pre_s", "from", "to"}]}: from
    # pre_s before each moved note-on of a listed row to its note-off, CC11 is held at "cc11" and CC1 at "cc1_min" or
    # more; after the note the lane returns to its own value. A brass mf staccato at CC11 72 lost 40 log10(72 / 100) =
    # -5.7 dB on top of its mf velocity layer (Trumpets 1-3 in bars 159-166: 22 dB under Violins I)
    for r in _pick(cfg.get("short_cc_park"), tname, family) or []:
        iv = []
        for a in notes:
            if not (r.get("from", -1e9) - 1e-6 <= sq_of(a) < r.get("to", 1e9) - 1e-6):
                continue
            if not _starts(_row(a, first_art), tuple(r.get("rows", ("Stac", "Marc Shrt")))):
                continue
            iv.append([Q(S(a["qn"]) - r.get("pre_s", 0.05)), a["qn"] + a["dur"]])
        iv.sort()
        mer = []
        for x in iv:
            if mer and x[0] <= mer[-1][1] + 1e-4:
                mer[-1][1] = max(mer[-1][1], x[1])
            else:
                mer.append(list(x))
        for ln, val, mode in (("cc11", r.get("cc11"), "set"), ("cc1", r.get("cc1_min"), "min")):
            if val is None or not ctx[ln]:
                continue
            lane = list(ctx[ln])
            for qa, qe in mer:
                f_ = _step_fn(lane)
                v_end = f_(qe)
                inside = [(q, v) for q, v in lane if qa - 1e-6 <= q < qe - 1e-6]
                keep = [(q, v) for q, v in lane if not (qa - 1e-6 <= q < qe - 1e-6)]
                if mode == "set":
                    new_ = [(round(qa, 4), int(val))]
                else:
                    new_ = [(round(qa, 4), int(max(val, f_(qa))))] + [(q, int(max(val, v))) for q, v in inside]
                lane = sorted(keep + new_ + [(round(qe, 4), v_end)])
                rep["short_cc_park"] = rep.get("short_cc_park", 0) + (1 if ln == "cc11" else 0)
            ded = []
            for q, v in lane:
                if ded and abs(ded[-1][0] - q) < 1e-6:
                    ded[-1] = (q, v)
                elif not ded or ded[-1][1] != v:
                    ded.append((q, v))
            ctx[ln] = ded

    # ---------- velocity ----------
    for r in (cfg.get("vel_pitch") or {}).get(tname, []):
        n_ = 0
        for a in notes:
            if _row(a, first_art).startswith(r.get("row", "")) and r.get("from", -1e9) <= sq_of(a) < r.get("to", 1e9):
                dv = r["pitch"].get(a["pitch"], r["pitch"].get(str(a["pitch"]), 0))
                if dv:
                    a["vel"] = int(max(r.get("min", 1), min(r.get("max", 127), a["vel"] + dv)))
                    n_ += 1
        rep["vel_pitch"] = rep.get("vel_pitch", 0) + n_

    for r in (cfg.get("vel_db") or {}).get(tname, []):   # a per-note level table in dB turned into velocity
        n_ = 0
        tab = {round(float(k_), 3): v_ for k_, v_ in r["table"].items()}
        for a in notes:
            dbv = tab.get(round(sq_of(a), 3))
            if dbv and _row(a, first_art).startswith(r.get("row", "")):
                a["vel"] = int(max(r.get("min", 1), min(r.get("max", 127), round(a["vel"] + dbv * r["steps_per_db"]))))
                n_ += 1
        rep["vel_db"] = rep.get("vel_db", 0) + n_

    for r in (cfg.get("vel_add") or {}).get(tname, []):   # c20: {"from", "to", "add", "row"}: velocity offset in a span
        n_ = 0
        for a in notes:
            if _row(a, first_art).startswith(r.get("row", "")) and r.get("from", -1e9) <= sq_of(a) < r.get("to", 1e9):
                a["vel"] = int(max(r.get("min", 1), min(127, a["vel"] + r["add"])))
                n_ += 1
        rep["vel_add"] = rep.get("vel_add", 0) + n_

    for r in (cfg.get("vel_cap") or {}).get(tname, []):   # c18: a row's velocities stay inside one sample layer
        n_ = 0
        for a in notes:
            if _row(a, first_art).startswith(r.get("row", "")) and r.get("from", -1e9) <= sq_of(a) < r.get("to", 1e9):
                v_ = int(max(r.get("min", 1), min(r.get("max", 127), a["vel"])))
                n_ += v_ != a["vel"]
                a["vel"] = v_
        rep["vel_cap"] = rep.get("vel_cap", 0) + n_

    # ---------- volume envelope ----------
    vol = [list(p) for p in ctx["vol_db"]]
    v7 = (cfg.get("vol_to_cc7") or {}).get(tname)
    if v7 and ctx.get("cc7"):
        keep = v7.get("keep_after", 1e9)
        vt = [S(p[0]) for p in vol]
        vf = _lin_fn(vt, [p[1] for p in vol])
        c7 = _step_fn(ctx["cc7"])
        tk = S(keep)
        ts = set(S(p[0]) for p in ctx["cc7"]) | set(t for t in vt if t < tk)
        for (ta, va), (tb, vb) in zip(zip(vt, [p[1] for p in vol]), zip(vt[1:], [p[1] for p in vol][1:])):
            if abs(vb - va) > 0.3 and tb - ta > 0.03 and ta < tk:
                nst = int((tb - ta) / 0.03)
                for j in range(1, nst + 1):
                    ts.add(ta + (tb - ta) * j / (nst + 1))
        out, last, clip, top = [], None, 0, -99.0
        for t in sorted(ts):
            q = Q(t)
            c = 20 * math.log10(max(1, c7(q)) / 127.0) + (vf(t) if t < tk else vf(tk)) - v7.get("shift_db", 0.0)
            top = max(top, c)
            if c > 0.05:
                clip += 1
            v = int(round(max(1, min(127, 127 * 10 ** (c / 20)))))
            if v != last:
                out.append((round(q, 4), v))
                last = v
        ctx["cc7"] = out
        v_k = vf(tk)
        vol = [[0.0, 0.0]] + ([[keep, 0.0]] if any(p[0] > keep for p in vol) else []) \
            + [[p[0], round(p[1] - v_k, 2)] for p in vol if p[0] > keep]
        rep["vol_to_cc7"] = {"points": len(out), "clipped": clip, "top_db": round(top, 2), "vol_at_keep": round(v_k, 2)}
    for r in (cfg.get("vol_step_at") or {}).get(tname, []):
        # c19: {"at": score qn, "win_qn": q}: a level change that the envelope makes over [at, at + win_qn], inside the
        # note printed at "at", becomes one step in the played gap before that note's moved note-on (a printed dynamic
        # after a breath: the fff arrival's level fell 4-7 dB inside the first chorale note)
        on_ = [a["qn"] for a in notes if abs(sq_of(a) - r["at"]) < 0.02]
        if not on_ or len(vol) < 2:
            continue
        t_on = S(min(on_)) - r.get("pre_s", 0.02)
        ts_ = [S(p[0]) for p in vol]
        f_ = _lin_fn(ts_, [p[1] for p in vol])
        t_b = S(r["at"] + r.get("win_qn", 2.0))
        v_a, v_b = f_(t_on - 0.02), f_(t_b)
        if abs(v_b - v_a) < 0.3:
            continue
        keep_ = [p for p, t_ in zip(vol, ts_) if t_ < t_on - 0.02 - 1e-4 or t_ > t_b + 1e-4]
        vol = sorted(keep_ + [[round(Q(t_on - 0.02), 4), round(v_a, 2)], [round(Q(t_on), 4), round(v_b, 2)], [round(Q(t_b), 4), round(v_b, 2)]])
        rep.setdefault("vol_step_at", []).append([r["at"], round(v_a, 2), round(v_b, 2)])
    for r in (cfg.get("vol_set") or {}).get(tname, []):
        # c20: {"pts": [(score qn, dB | None | "at:QN")]}: over [first qn, last qn] the envelope follows this line (a
        # held phrase level or a hairpin gain kept through an fff arrival instead of released). None = the envelope's
        # own value at that qn; "at:QN" = its own value at QN (a hold). Slow balance only: the guard below still runs
        if len(vol) < 2:
            continue
        vq0, vv0 = [p[0] for p in vol], [p[1] for p in vol]
        f0 = _lin_fn(vq0, vv0)
        pts_ = []
        for q_, d_ in r["pts"]:
            if d_ is None:
                d_ = f0(q_)
            elif isinstance(d_, str) and d_.startswith("at:"):
                d_ = f0(float(d_[3:]))
            pts_.append([q_, round(float(d_), 2)])
        a_, b_ = pts_[0][0], pts_[-1][0]
        vol = sorted([p for p in vol if p[0] < a_ - 1e-6 or p[0] > b_ + 1e-6] + pts_)
        rep.setdefault("vol_set", []).append([a_, b_, [p[1] for p in pts_]])
    vg = cfg.get("vol_guard")
    if vg and len(vol) > 1 and not v7 and tname not in vg.get("skip_tracks", ()):
        spans = [(S(a["qn"]), S(a["qn"] + a["dur"])) for a in notes]
        t_end = S(vg.get("skip_after", 1e9))
        edge, pre, rate = vg.get("edge_s", 0.018), vg.get("pre_s", 0.03), vg.get("rate_db_s", 20.0)
        fixed = []
        hp_t = [(S(h_[0]), S(h_[1]) + 0.05) for h_ in (ctx.get("hairpins") or [])] if vg.get("hairpin_ok") else []

        skip_t = [(S(a_), S(b_)) for a_, b_ in vg.get("skip", [])]   # c18: listed spans (score qn) are left alone

        def printed(ta, tb):   # c18: a move under a printed hairpin is a printed move
            if any(a_ <= ta and tb <= b_ for a_, b_ in skip_t):
                return True
            return any(a_ < tb and b_ > ta and min(tb, b_) - max(ta, a_) >= 0.5 * (tb - ta) for a_, b_ in hp_t)
        def rate_at(t, me):
            # c18: a ramp that must cross sounding notes before a note-on runs at "rate_db_s" when a held note sounds
            # there, and at "rate_short_db_s" when only notes shorter than "short_s" do (running notes: the level
            # changes between notes, no held note is ridden)
            snd = [f2 - o2 for o2, f2 in spans if (o2, f2) != me and o2 < t and f2 > t - 0.25]
            if vg.get("rate_short_db_s") and snd and max(snd) < vg.get("short_s", 0.5):
                return vg["rate_short_db_s"]
            return rate

        for _ in range(vg.get("max_iter", 4)):
            ts = [S(p[0]) for p in vol]
            vs = [p[1] for p in vol]
            f = _lin_fn(ts, vs)
            todo = [(ta, tb, va, vb) for ta, tb, va, vb in find_fast(ts, vs, t_end, vg["min_db"], vg["win_s"])
                    if inside_note(spans, ta, tb, edge) and not printed(ta, tb)]
            if not todo:
                break
            edits = []
            for ta, tb, va, vb in todo:
                on, off = inside_note(spans, ta, tb, edge)
                dv = abs(vb - va)
                # a large fall after a note's start is the fall of an fp / sfp or a subito: it stays where it is
                if ta - on <= vg.get("lead_max_s", 0.45) and not (vb < va and dv >= vg.get("fall_keep_db", 6.0)):
                    n1 = on - pre
                    busy = any(o2 < n1 and f2 > n1 - (tb - ta) - 0.005 for o2, f2 in spans if (o2, f2) != (on, off))
                    D = max(dv / rate_at(n1, (on, off)), 0.09) if busy else min(tb - ta, 0.03)
                    n0 = n1 - D
                    edits.append((n0, tb, [(n0, f(n0)), (n1, vb), (tb, vb)], "on"))
                else:
                    D = max(dv / rate, tb - ta)
                    c = 0.5 * (ta + tb)
                    n0, n1 = c - D / 2, c + D / 2
                    if n1 > off - 0.02:
                        n0, n1 = n0 - (n1 - (off - 0.02)), off - 0.02
                    if n0 < on + 0.02:
                        n0, n1 = on + 0.02, min(off - 0.02, n1 + (on + 0.02 - n0))
                    if n1 - n0 < 0.9 * dv / rate:   # the note is too short for a slow ramp: start at its note-on
                        n1 = on - pre
                        n0 = n1 - max(dv / rate_at(n1, (on, off)), 0.09)
                        edits.append((n0, tb, [(n0, f(n0)), (n1, vb), (tb, vb)], "on-short"))
                    else:
                        edits.append((n0, n1, [(n0, f(n0)), (n1, f(n1))], "slow"))
            new = [(t, v) for t, v in zip(ts, vs)]
            for n0, n1, ins, kind in edits:
                new = [(t, v) for t, v in new if not (n0 - 1e-6 <= t <= n1 + 1e-6)] + ins
                fixed.append([round(Q(n0), 3), round(Q(n1), 3), kind, round(ins[-1][1] - ins[0][1], 1)])
            new.sort()
            vol = [[round(Q(t), 4), round(v, 2)] for t, v in new]
            # strictly increasing positions
            ded = []
            for q, v in vol:
                if ded and q <= ded[-1][0] + 1e-5:
                    q = round(ded[-1][0] + 0.0002, 4)
                ded.append([q, v])
            vol = ded
        ts = [S(p[0]) for p in vol]
        left = [m for m in find_fast(ts, [p[1] for p in vol], t_end, vg["min_db"], vg["win_s"])
                if inside_note(spans, m[0], m[1], edge) and not printed(m[0], m[1])]
        rep["vol_guard"] = {"fixed": len(fixed), "left": [[round(Q(m[0]), 3), round(m[3] - m[2], 1)] for m in left],
                            "edits": fixed}
    ctx["vol_db"] = [tuple(p) for p in vol]
    # ---------- printed dynamic curve (build_reaper.py reads the dynamic trims from it) ----------
    ds = cfg.get("dyn_step_on")
    if ds and ctx.get("dyn_curve"):
        # {"min_cc": units, "pre_s": s}: a jump of the printed dynamic at a score onset moves to pre_s before the moved
        # note-on of the notes printed there, so the trim's step lies before the led note and not in its first 50-240 ms
        dc = [list(p) for p in ctx["dyn_curve"]]
        ons = {}
        for a in notes:
            ons[round(sq_of(a), 3)] = min(ons.get(round(sq_of(a), 3), 1e9), a["qn"])
        moved = 0
        for i in range(1, len(dc)):
            if abs(dc[i][1] - dc[i - 1][1]) < ds.get("min_cc", 8):
                continue
            m = ons.get(round(dc[i][0], 3))
            if m is None or m >= dc[i][0] - 1e-4:
                continue
            nq = round(Q(S(m) - ds.get("pre_s", 0.03)), 4)
            if nq > dc[i - 1][0] + 0.02 and (i + 1 >= len(dc) or nq < dc[i + 1][0]):
                dc[i][0] = nq
                if ctx.get("vol_bp") is not None:
                    ctx["vol_bp"] += [round(nq - 0.02, 4), nq]
                moved += 1
        ctx["dyn_curve"] = [tuple(p) for p in dc]
        rep["dyn_steps_moved"] = moved
    return rep

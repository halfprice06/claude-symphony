"""r02: printed percussion events read from the v120 LilyPond source, added to the rendering MIDI.

LilyPond's MIDI has no note for the tam-tam (`tt`, no GM drum) and plays the suspended-cymbal roll (`cymr1:32`)
as one ride-cymbal stroke. This module reads the DrumStaff variables directly from the source (parts.ily lists
the section variables of `perc` with their bar counts; each section's `*Perc = \\drummode {...}` gives the
events), converts bar/position to MIDI ticks with the score's own bar grid (4/4 throughout, checked against the
MIDI time signature), and rewrites the drum track of the rendering MIDI:
  * every printed percussion note becomes one note on channel 10 with the key given in config percussion.keys
    (keys of r02's own SFZ file sfz/perc-r02.sfz), velocity from the printed dynamic (v120 volume table);
  * l.v. notes are held for config percussion.lv_s seconds (the sample decides the real decay);
  * the roll's crescendo is realised by the crescendo sample itself, its length by the note.
Nothing in mvt1/ is changed; the source is only read.
"""
import os, re
import mido

DYN_VEL = {"ppp": 32, "pp": 42, "p": 53, "mp": 64, "mf": 74, "f": 84, "ff": 91, "fff": 127}
DUR = {"1": 1.0, "2": 0.5, "4": 0.25, "8": 0.125, "16": 0.0625}


def _section_body(ly_dir, name):
    for fn in sorted(os.listdir(os.path.join(ly_dir, "sections"))):
        txt = open(os.path.join(ly_dir, "sections", fn), encoding="utf-8").read()
        m = re.search(r"^" + re.escape(name) + r"\s*=\s*\\drummode\s*\{", txt, flags=re.M)
        if m:
            i = m.end(); depth = 1; j = i
            while depth:
                depth += {"{": 1, "}": -1}.get(txt[j], 0); j += 1
            return txt[i:j - 1]
    return None  # score.ly's secDrum: an undefined section variable means full-bar rests


def score_events(ly_dir):
    """[(bar (1-based, may be fractional), drum name, dyn, length in wholes, has_crescendo)]"""
    parts = open(os.path.join(ly_dir, "parts.ily"), encoding="utf-8").read()
    m = re.search(r"^perc\s*=\s*\{(.*?)\}\s*$", parts, flags=re.M)
    secs = re.findall(r'\\secDrum\s+"(\w+)"\s+(\d+)', m.group(1))
    out = []; bar0 = 1
    for name, nbars in secs:
        body = _section_body(ly_dir, name)
        if body is None:
            bar0 += int(nbars); continue
        body = re.sub(r"\\markup\s*\{[^{}]*\}", " ", body)
        body = re.sub(r'"[^"]*"', " ", body)
        body = re.sub(r"%.*", " ", body)
        pos = 0.0; last = "4"
        for tok in body.split():
            if tok == "|":
                continue
            t = re.match(r"([a-zA-Z]+)(\d*)(\.?)(?::\d+)?(?:\*(\d+))?(.*)$", tok)
            if not t:
                continue
            nm, d, dot, mult, rest = t.groups()
            if nm.startswith("\\") or tok.startswith("\\"):
                continue
            d = d or last; last = d
            ln = DUR[d] * (1.5 if dot else 1) * (int(mult) if mult else 1)
            if nm not in ("R", "r", "s"):
                dyn = re.search(r"\\(ppp|pp|p|mp|mf|f|ff|fff)(?![a-z])", rest)
                out.append((bar0 + pos, nm, dyn.group(1) if dyn else None, ln, "\\<" in rest))
            pos += ln
        if abs(pos - int(nbars)) > 1e-6:
            raise ValueError(f"{name}: {pos} bars parsed, {nbars} expected")
        bar0 += int(nbars)
    return out


def apply(mid, cfg, src_midi):
    P = cfg["percussion"]
    ly_dir = P["ly_dir"] if os.path.isabs(P["ly_dir"]) else os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), P["ly_dir"]))
    ev = score_events(ly_dir)
    tpb = mid.ticks_per_beat
    bar_ticks = 4 * tpb  # 4/4 throughout (global.ily \time 4/4; the MIDI has no other time signature)
    for tr in mid.tracks:
        for m in tr:
            if m.type == "time_signature":
                assert (m.numerator, m.denominator) == (4, 4), "perc.py assumes 4/4"
    # tempo map for l.v. lengths
    from articulate import TempoMap
    tm = TempoMap(mid)
    drum = None
    for tr in mid.tracks:
        if any(getattr(m, "channel", None) == 9 for m in tr if not m.is_meta):
            drum = tr
    if drum is None:
        drum = mido.MidiTrack(); mid.tracks.append(drum)
    name = next((m.name for m in drum if m.type == "track_name"), "")
    newtr = [(0, mido.MetaMessage("track_name", name=name))]
    n = 0
    last_dyn = "pp"
    for bar, nm, dyn, ln, cresc in ev:
        dyn = dyn or last_dyn; last_dyn = dyn
        k = P["keys"].get(nm)
        if k is None:
            continue
        on = int(round((bar - 1) * bar_ticks))
        v = DYN_VEL[dyn]
        if nm in P.get("lv", []):
            off = tm.s2t(tm.t2s(on) + P["lv_s"])
        else:
            off = on + int(round(ln * bar_ticks))
        if cresc and nm in P.get("cresc_keys", {}):
            # crescendo roll: pick the crescendo sample whose peak is nearest to the printed roll length
            dur = tm.t2s(on + int(round(ln * bar_ticks))) - tm.t2s(on)
            k = min(P["cresc_keys"][nm], key=lambda kv: abs(kv[1] - dur))[0]
            v = P.get("cresc_velocity", 100)
        newtr.append((on, mido.Message("note_on", channel=9, note=k, velocity=v)))
        newtr.append((off, mido.Message("note_off", channel=9, note=k, velocity=0)))
        n += 1
    newtr.sort(key=lambda z: (z[0], 0 if z[1].is_meta else (1 if z[1].type == "note_off" else 2)))
    drum.clear(); last = 0
    for tk, m in newtr:
        drum.append(m.copy(time=tk - last)); last = tk
    drum.append(mido.MetaMessage("end_of_track", time=0))
    return n

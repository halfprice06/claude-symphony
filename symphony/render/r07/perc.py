"""r02/r03: printed percussion events read from the LilyPond source of the version being rendered (render.py
--score), added to the rendering MIDI. r03: section positions are placed on the MIDI's own bar grid (any metre); a
score without a DrumStaff (no `perc = {...}` in parts.ily) adds nothing.

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


def score_events(ly_dir, bar_wholes=None):
    """[(section start bar (1-based), position in wholes from the section start, drum name, dyn, length in wholes,
    has_crescendo)]. bar_wholes(b0, n): length in wholes of n bars from bar b0 (MIDI grid); None = 4/4."""
    pp = os.path.join(ly_dir, "parts.ily")
    if not os.path.exists(pp):
        return []
    parts = open(pp, encoding="utf-8").read()
    m = re.search(r"^perc\s*=\s*\{(.*?)\}\s*$", parts, flags=re.M)
    if not m:
        return []
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
                out.append((bar0, pos, nm, dyn.group(1) if dyn else None, ln, "\\<" in rest))
            pos += ln
        want = bar_wholes(bar0, int(nbars)) if bar_wholes else float(nbars)
        if abs(pos - want) > 1e-6:
            raise ValueError(f"{name}: {pos} wholes parsed, {want} expected")
        bar0 += int(nbars)
    return out


def apply(mid, cfg, src_midi, ly_dir):
    """ly_dir: the score folder being rendered (render.py --score)."""
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
    import rtk
    P = cfg["percussion"]
    tpb = mid.ticks_per_beat
    grid = list(rtk.midi_info(src_midi)["bar_ticks"])
    def tick_of_bar(b):
        return grid[b - 1] if b - 1 < len(grid) else grid[-1] + (b - len(grid)) * 4 * tpb
    ev = score_events(ly_dir, lambda b0, n: (tick_of_bar(b0 + n) - tick_of_bar(b0)) / (4 * tpb))
    if not ev:
        return 0
    bar_ticks = 4 * tpb  # one whole note in ticks (positions inside a section are in wholes)
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
    for b0, pos, nm, dyn, ln, cresc in ev:
        dyn = dyn or last_dyn; last_dyn = dyn
        k = P["keys"].get(nm)
        if k is None:
            continue
        on = tick_of_bar(b0) + int(round(pos * bar_ticks))
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

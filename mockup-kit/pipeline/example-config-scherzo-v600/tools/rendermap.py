"""mvt1 c03: the file time of a score qn in a rendered cycle.

Renders c00-c02 were made with the pre-roll tempo marker in the score's 4/4 instead of the pre-roll's own 3/4, so REAPER
moved the score's first tempo marker to the next barline and every event from score qn 1 on sounded 1/6 qn early
(build/render_shift.json). Notes, controllers and the volume envelope all moved together. Any tool that reads such a
render on the parts.json tempo map must use wrap(q2s, cycle), or every shape it fits lands 1/6 qn early.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_P = f"{ROOT}/build/render_shift.json"
SHIFTS = {k: v for k, v in json.load(open(_P)).items() if not k.startswith("_")} if os.path.exists(_P) else {}


def shift_for(cyc):
    try:
        return SHIFTS.get(str(int(cyc)))
    except (TypeError, ValueError):
        return None


def cycle_of(path):
    """the cycle number of a render dir like .../cycles/c02/render (None if not found)"""
    import re
    m = re.search(r"/cycles/c(\d+)/", os.path.abspath(path) + "/")
    return int(m.group(1)) if m else None


def wrap(q2s, cyc):
    """q2s on the parts.json tempo map -> the file time of that score qn in cycle cyc's render"""
    sh = shift_for(cyc)
    if not sh:
        return q2s
    s, f0, bpm = sh["shift_qn"], sh["from_qn"], sh["preroll_bpm"]

    def f(q):
        return q * 60.0 / bpm if q <= f0 else q2s(q - s)
    return f

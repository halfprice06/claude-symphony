# One-time task for the next actor (c03 resume): three shared changes from Movement I c44

Movement I measured these for Dan's "too wet, mushy" note. Apply all three in this cycle, alongside the critics' fixes. Each is an Opus state change, so do a full rebuild of every track (not --midi-only / --mix-only). When done, rename this file to ONE_TIME.c03.done.md and record the changes in cycles/c03/CHANGES.md and loop/LEARNINGS.md.

1. Shorter hall tail.
   - In build/mix.json `reverb`, next to fx_volume 0.095 and low_cut_hz 160, add `"ir_setup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}`. Sends stay as they are.
   - Code: copy the irSetup block (about 13 lines, right after the low-cut block in `apply_mix`) from /Users/gooby/sandbox/claude_composes/mockup-kit/pipeline/build_reaper.py (commit 86b70270) into this folder's tools/build_reaper.py. `simpleDecay` does nothing; set the irSetup dict explicitly.
   - Movement I result: late slope 2.61 s -> 1.54 s; fermata -5..-25 dB slope 2.42 s -> 1.29 s. Measure the scherzo's late decay before and after (our c01 T60 was 3.5-3.7 s) and report it.
2. Release caps (`sus_release_cap_ms` per track in mix.json, read by cap_release; port cap_release from symphony/mvt1/reaper-v621/tools if this folder lacks it).
   - Every section string track: `{"ms": 150, "dyn": ["pp","p","mf","f","ff"], "rows": ["Sus MAX","Sus Marc LITE"]}`.
   - Every horn track: `{"ms": 237, "dyn": ["pp","mf","f"], "rows": ["Sus MAX","LegRep RRx4"]}`.
   - Match the row names to this folder's actual patches. Refit re-bow fills afterwards if any exist (fit_rebows.py).
   - Check that no phrase ending drops more than 10 dB in its first 0.05 s (that would sound clipped).
3. Repeated string notes (Dan's S1): port Movement I's generic rule `STR_REP_NEW_BOW` from symphony/mvt1/reaper-v621/tools/score_to_parts.py. Settings and the list of code places are in symphony/mvt1/reaper-v621/cycles/c44/CHANGES.md item 3. Loud, accented, slur-head or slurred-tenuto same-pitch repeats become fresh Sus MAX strokes after a gap of min(0.06 s, 25%); soft repeats inside one slur stay merged. Movement I's stem dips went from 2.3-2.9 to 5.0-7.8 dB; measure ours.

Read mockup-kit/README.md items 7, 11, 12 and mockup-kit/LEARNINGS.md "Too wet and mushy" first. Never write into symphony/mvt1/ or mockup-kit/.

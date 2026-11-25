# c05 actor: interrupted before REAPER (2026-11-08)

Done (steps 1-4): snapshot in before/; edits in tools/build_reaper.py (cap_release "ms" may be a per-dynamic dict),
tools/score_to_parts.py (PERC_END_AT, PIZZ_LEAD_S, ROW_LEAD_S), build/mix.json (string caps pp/p 500, mf 300, f/ff 150 ms
on all 5 string tracks), build/score_config.py (c05 section: PERC_END_AT crash/bass drum 1108 -> 1113.2,
STR_REP_NEW_BOW sus_min_s 0.3, RETONGUE_LEAD_ART_S Violoncellos Sus MAX +0.07, PIZZ_LEAD_S Vc 0.035 / Vln II 0.015,
ROW_LEAD_S Trumpet 1 Mute Sus 0.035), build/roles.json (critic B #1-#4 exactly as proposed). parts.json regenerated,
0 WARNING, diffed against c04 (actor_scripts/parts_c04.json). Re-bow points did not change (space_rebows not needed).

Not done: lock, build, render, measure, CHANGES.md, HISTORY, LEARNINGS. REAPER was never touched; no lock held.
Build needed: full rebuild of the 5 string tracks (cap state); --midi-only for Flute 1-2, Oboe 1-2, Clarinet 1-2,
Horn 3-4, Trumpet 1-3, Bass trombone, Tuba, Crash cymbals, Bass drum.
Deferred: C #2 brass width (brass not rebuilt), C #3 soli side shelf (side_lua drops a switched shelf when the track
has no static side_shelf), C #4 harp harmonics, A #2 felt timpani pass 2, A #6, B #5.
Measure after the render: actor_scripts/softends.py RENDER PARTS (c04 baseline softends_c04.txt), tutti.py MASTER 421.77
71.21 (baseline tutti_c04.txt). c04 stems were deleted (disk); master kept.

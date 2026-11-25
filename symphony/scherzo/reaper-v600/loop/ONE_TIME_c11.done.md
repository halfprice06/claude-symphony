# One-time task for the c11 actor: finale SHARED-TECHNIQUES items 13-17 (arrived during the c10 render)

Source (read only): `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` items 13-17, code in its `tools/`. The c10
build was already in REAPER when the orchestrator passed them on, so none was adopted in c10. Adopt each unless measured
numbers say no, record the result in cycles/c11/CHANGES.md, then rename this file ONE_TIME_c11.done.md.

1. Item 13 (strings' sf of an sfp): a 0.35 qn post-fader bump (+3 dB violins and violas, +5 dB celli and basses) plus
   0.08 s lead on unled sections, at bar 301 (qn 900). Measure each string stem's first 0.1 s against bar 300's ff and
   the peak's time after the mark on the c10 stems first (c09 critic A #2 measured drops of 16-20 dB; check the sf level,
   not only the drop). Flute 1's 900 got v118 and +0.03 s entry lead in c10 (A #2): check it on the c10 stems.
2. Item 14 (two players on one line, per-track SOST_JOIN_LEAD_S): check Flute 1 / Flute 2 unison joins (pcX of each on
   the c10 stems; c09 critic A #5 noted Flute 2's row reaching its peak about 0.1 s late in the low unison).
3. Item 15 (delivery ride): check our RIDE_TRIMS for a step inside a printed crescendo; try `--fit-flat` rows +1.5 dB
   on soft passages after loud ones (bar 121 and 277 sub. p) if deliver_master.py has it (port it if not).
4. Item 16 (multi-measure-text-event listener in build/mockup.ly): check whether the scherzo prints text on full-bar
   rests (timpani "soft sticks" at bar 341, "muta", "senza sord." on rests) that the event list misses.
5. Item 17 (negative result): no action; do not add REP_SPLIT gaps to the doubled bass eighths for master dips.

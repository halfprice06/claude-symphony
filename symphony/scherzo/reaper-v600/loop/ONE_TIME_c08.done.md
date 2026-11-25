# One-time tasks for the c08 actor (from c07's CHANGES.md and Movement I's c50/c51)

1. Brightness first: c07's 6-20 kHz share is -24.8 dB against references of -28.8 to -32.2 (c06 -27.2). Port Movement I c50's fix (symphony/mvt1/reaper-v621/cycles/c50/CHANGES.md): strings family shelf off, brass shelf +1, Violins I 5 kHz -6, Violins II 5 kHz -4; measure, target -28 or lower.
2. Loud brass tone (Movement I c51 critics; finale c08 did the same): halve the brass bells (475 Hz -2.7, 821 Hz -3.9 dB), add a 3.2 kHz -3 dB bell, lower brass gains 1.8-4.0 dB to keep loudness. Check the 2-5 kHz jump at brass accents (p90 under +2 dB).
3. Soft timpani rolls: low shelf 160 Hz -3 dB on the soft-roll spans only, +1 dB level there, if our rolls mask (measure).
4. String shorts: beat weight (+1.5 / 0 / -1 dB) and the CC11 park put into the volume envelope, keeping each note's current velocity layer (HO string short rows switch layer by velocity, about 10 dB a step).
5. Wetness limits still open: the final chord's RT60 1.68 s (limit 1.5) and one soft string end at 0.31 s (limit 0.30). Fix without making the rest drier than needed.
6. c07's deferred critic items: C #2.2 (pickup long notes as fresh strokes), the flute lead in bars 349-356, Trumpet 2's staccato row (memory), the solo's CC1 lane, C #4.2 group-head trims.
7. make_template_mix.py does not write c07's mix settings: either fold wet_mix07.py, width07.py and mix07_more.py into it, or keep re-running them; record which.

When done, rename this file to ONE_TIME_c08.done.md and list in CHANGES.md what was adopted, deferred or rejected.

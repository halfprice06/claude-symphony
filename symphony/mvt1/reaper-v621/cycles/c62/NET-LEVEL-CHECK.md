# c62 against c61: fader level per quarter note where the track sounds (coordinator check, 2026-11-18)

Method: written volume envelope of cycles/c61/rendered_build and cycles/c62/rendered_build (lib61.load_br, build_reaper.py cut before ENV_LUA), mean over each 1-qn span where the track has a sounding note, c62 minus c61. Percussion (moved to CC7) excluded.

Spans over 1.5 dB: 600 or more across 30 tracks. Largest, unintended by the work order:
- Trombone 1 qn 447-457 down to -14.7 dB; Bass trombone 451-459 -10.1; Tuba 442-464 up to +8.9; bass clarinet, bassoon 2, contrabassoon 443-464 +2 to +5.4 (the crescendo into the bar-122 fff).
- Violins II 473-484 down to -12.9 (into bar 122) and 658-664 -9.9.
- Horn 2 619-624 -10.1, 542-545 -7.2, 659-663 -7.0; Horn 1 658-663 -7.2; Horn 3 83-90 -6.0, 619-622 -5.7.
- Violas 160-168 +3 to +6.3, 378-384 up to +5.9; celli 285-286 +5.5.
Likely cause: the new note_slope_guard moving ramps away from note-ons (the first turn's bug walked join ramps up to 19 qn back; the fix may not cover every case), and edge re-keying of role rows. This also explains the six inner lines that dropped 1.5-2.6 dB.
Conclusion: c62 is not a safe replacement for c61. A c63 would diff net level (envelope + CC7) against c61 per 1-qn span and allow no change over 1.5 dB that the work order did not ask for.

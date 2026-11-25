# Cycle 0: first build

First mockup of mvt1/v221, built from mockup-kit (movement II's c26 tools) with the kit's "Starting a new mockup" rules applied from the start: unused rows unloaded, 1x offline render with a 3 qn pre-roll (first keyswitch, CC values, CC36/CC69 resets), REAPER restarted before the render, delivery through deliver_master.py, CC11 dynamics / CC1 vibrato only, keyswitch maps from the .oib files, the true-stereo hall, automatic re-bows of string notes over 4.5 s, gentle brass accents.

Setup: see README.md ("What differs from the movement II pipeline"). 32 tracks: winds 11, horns 4, trumpets 3 (1TP KS Master), trombones 2 + bass trombone, tuba, timpani (Flt KS), tam-tam, suspended cymbal, crash cymbals, harp (Sus RR), 5 string sections. Mix from movement II's c26 mix.json; trumpet gain -3 dB, percussion -4/-6 dB (guesses).

Render (cycles/c00): master -17.6 LUFS, LRA 23.1 LU, true peak +0.9 dBFS as a float stem sum (the 24-bit master render clipped: stem-sum peak 1.109, 45 samples; render_cycle.py now replaces a clipped master by the float stem sum). Delivered mp3: -19.8 LUFS, LRA 17.3 LU (target 14-16), TP -1.7 dBTP, limiter 1.3 dB, p10-to-max span 21.7 dB (target 16-19).

Memory: REAPER 17 GB settled before the render, 44 GB after with 28 GB compressed (two other users' Python processes held 11 + 6 GB during the render).

Attack probe: 4 of 12 failed: Trombone 1 qn 100 +0.14 s (now plain Sus under GENTLE_ACCENT; Sus speaks slower than the accent sample, LEARNINGS 7), Violins I qn 56.5 +0.20 s, Violins II qn 20 +0.34 s and Violoncellos qn 20 +0.63 s (pp entries: soft string first notes arrive 0.3-1.0 s late on the sample itself, LEARNINGS 6). The probe limits were first guesses with no earlier render to compare; c01 should compare these onsets with the c00 render to separate sample attack from engine lateness, and set the probe limits accordingly.

Open for c01: master headroom (Trombone 1 stem peak -3.8 dBFS, Violins I -3.0), delivered LRA and span over target, trumpet and percussion levels unmeasured against the score, the suspended-cymbal roll's alignment with the crash at qn 636, re-bow level steps (no rebow_fills fitted yet).

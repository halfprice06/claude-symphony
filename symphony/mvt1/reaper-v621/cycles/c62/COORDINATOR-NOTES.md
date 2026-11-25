# Cycle 62: coordinator notes. A narrow fix cycle, no critics.

## Why
Dan's rule (2026-11-11): "yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem". c61 has 0 envelope items from per-note rules, but a slope check (finale c26 critics' method) finds fast fader moves inside sounding notes from the slow-balance rules. Measured on cycles/c61/rendered_build with cycles/c61/actor_scripts/env61.py's edges() (over 3 dB/s, 1.5 dB or more inside a sounding note): 354 edges.
- 137 inside a held note (no note-on of that track within 0.35 s before to 0.15 s after): winds/brass/harp 62 (12 of 6 dB+), strings 32 (3 of 6 dB+), percussion 33 (6 of 6 dB+). Examples (s): Horn 2 50.1, 86.2, 175.4, 307.2, 347.7, 370.9; Horn 3 49.2, 83.3, 258.5, 347.2; brass at 115.7-116.0, 262-264 and 359.8-360.3; all strings at 431.4; Violins I/II f62 159-161.
- 217 at a new note while the previous note still sounds (step near the moved note-on).
Causes are not tagged on the points; likely hairpin-gain releases, the held-decrescendo rule, role and section-row edges, player-count marks, timpani dynamics.

## Work order
1. Tag each fast edge with its rule (temporary debug tagging is fine) and write the table cycles/c62/edges_c61.md: track, time, bar, size, rule.
2. Fix at the source where the rule is wrong (hairpin-gain release over at most 2.8 dB/s or at the next printed dynamic or rest; held-decrescendo release not inside the next note; role and row edges in rests or as ramps of 2 s or more), then a generic post-pass guard in build_reaper.py after vol_points: no move of 1.5 dB or more steeper than 3 dB/s inside a sounding note of that track. A move at a new note while the previous one sounds goes to 0.03 s before the moved note-on as a 20 dB/s ramp only if it is a printed sudden dynamic (sf, fp, subito); otherwise it becomes a ramp that ends at the moved note-on. A move inside a held note that a printed hairpin calls for becomes a ramp over the hairpin's length. Port from symphony/scherzo/reaper-v600/tools/build_reaper.py note_move_guard (and the finale's tools/instr_post.py guard) where it fits. Timpani dynamics: fold into a CC7 lane (finale) if the guard cannot keep rolls right.
3. Target after the build: fast edges inside held notes 0; at new notes only printed sudden dynamics. Report counts by family and the master bars that move more than 1.5 dB against c61 with cause.
4. Delivery under the new shared spec (mockup-kit/README.md "Decision: climax margin before loudness range"): top ride from 6 dB under p95 (TOP_ABOVE -6), quiet-lift ratio about 2.1, ride rows as needed so the summit bar 160 leads bars 122, 26 and 170 by 0.5 LU or more on loudest 0.4 s, printed f -> ff steps 2 LU or more, LRA 10.5 or more, p10 -23 or higher, limiter no sustained climax over 6 dB. Test on the c61 master first (no REAPER needed), then apply to the c62 master.
5. Guards: Violins I theme 56-90 S robust SD at or under 12 ms (cycles/c54/coordinator_scripts/theme_S.py c62 "Violins I" 56 90 from ROOT), theme over celli lower quartile 3.9 or more, inner-line table (cycles/c61/actor_scripts/linetable61.py) not worse by more than 1 dB on any line.
6. Deliver cycles/c62/mvt1-mockup-c62.mp3, CHANGES.md, edges table before and after, envelope table, A/B clips c61 then c62 of bars 12-16 and 85-91 (master), rendered_build/parts.json.

## Actor constraints
- Shared REAPER lock: wait_lock.py with a running background waiter (confirm with pgrep, keep it alive); never take or break the lock by hand; tie rule: the folder path that sorts first goes first. Do not end your turn while a waiter or render runs.
- Restart REAPER and run the audio-init step immediately before the main render. Shell chains stop and keep the lock on any failure (c61's p5.sh pattern).
- First range render after a rebuild is unusable; state guard at the start, after range renders and before the full render.
- Disk: 10 GB floor after the render; delete WAVs only in cycles/c60-c62 rangetest / variants folders if needed.
- No score change, no commit, nothing published, no REAPER preference change, nothing in ~/.rpr-bridge modified, no subagents. Scripts under cycles/c62/actor_scripts/. Update HISTORY.md and LEARNINGS.md. Hand-back at most 40 lines with what failed, what is left audible and what is not verified.

## Addition 2026-11-18 01:40 UTC: Dan approved c62 and the room bed
Dan: "Sure.  The bed is fine." (answering whether to run c62, and on the room-noise bed audition).
7. Room bed in the delivery (do this in tools/deliver_master.py, generic, for all movements): after the limiter and before the mp3 encode, add a synthetic hall-air bed at -60 LUFS integrated (pink noise, extra fall above 2.5 kHz as a first-order low pass, low cut 84 Hz fourth order, partly correlated stereo: L = 0.8 a + 0.6 c, R = 0.8 b + 0.6 c, fixed seed so renders repeat). The audition was made exactly this way (scratch script reproduced in the c62 notes below); after the bed the loudness loop and true-peak check must still pass. Env DELIVER_ROOM_BED_LUFS (default -60; "off" disables). Keep it after the delivery ride so the quiet-passage lift does not raise it. Report the delivered figures with and without the bed (the bed changes integrated loudness by under 0.05 LU).

Audition code (numpy, x = limited float32 stereo at sr):
    f = rfftfreq(n, 1/sr); f[0] = 1
    g = 1/sqrt(f) * 1/sqrt(1+(f/2500)**2) * (f/84)**4/(1+(f/84)**4)
    shaped(seed) = irfft(rfft(standard_normal(n, seed)) * g, n)
    noise = stack([0.8*a+0.6*c, 0.8*b+0.6*c]); scale to -60 LUFS integrated; y = x + noise

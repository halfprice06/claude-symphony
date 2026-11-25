# Carry-over from c07 (written after unlocking, 2026-11-08 16:15)

REAPER holds build/parts.json and build/mix.json exactly as rendered in c07. No stem fix was applied; mix.json "deliver"
affects only the mp3. The project has 35 tracks (31 instruments plus 4 returns).

Before rendering, wait until REAPER reaches 44 GB (c07 settled at 44 GB about 9 min after the restart).

Open from c07 (cycles/c07/CHANGES.md):
- Brass accent 2-5 kHz jump on the master: p90 5.2 dB (target < 2). Try the brass family 821 Hz bell -7.8 -> -4, or a
  3.2 kHz -3 dB bell.
- Drop at +0.3 s is 12-13 dB at qn 373 and 661. It is dry-limited (16.7 / 18.7 with no returns).
- Repeats still merging (dry + return under 3 dB): Trumpet 3 in the Più allegro (12 of 48), Vc 828, Vln I 884, Vc 832.
- Batches 6-7, not yet done: ostinato / beat-position short-note velocity, spiccato length 50-62 %, one dynamics curve
  for doublings.
- Movement I c50 B #2: per-instrument / per-dynamic brass make-up.
- CC1-only and narrow-brass A/B tests (pass 2, memory).
- Measure on c08:
  - pcX of the F / P / T upper-string Sus MAX leads, the tremolo leads in T, and the slur-head leads;
  - per-track entry residuals;
  - phrase-shape stats (rise by 0.8 s, peak position, last-second fall) by type.
- The probe flag at Vc qn 24 is a build-shape artefact; consider a probe exception.

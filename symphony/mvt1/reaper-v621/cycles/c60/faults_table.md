# Faults at audible size, c59 render -> c60 render (cycles/c60/actor_scripts/faults60.py, same measures as faults59.py; lists in faults_c60.txt)
| fault | c59 | c60 |
|---|---|---|
| join holes (6 dB or more for 80 ms or more) | 25 | 24 |
| same-pitch repeats under 3 dB of separation | 49 of 260 | 114 of 336 |
| re-bow holes (6 dB for 80 ms) | 14 of 52 | 8 of 44 |
| long notes sagging 6 dB or more | 61 | 68 |
| pulse on a held note (6 dB) | 13 | 12 |
| pitches 4 dB or more out of their line | 6 | 9 |
Strings: holes 6 -> 7, repeats 28 of 139 -> 28 of 123, re-bow holes 14 -> 8, sags 24 -> 23, pulse 9 -> 8, pitches 2 -> 4.
Winds: holes 17 -> 14, repeats 19 of 111 -> 44 of 119, sags 16 -> 19. Brass: holes 2 -> 3, repeats 2 of 10 -> 42 of 94, sags 21 -> 26.
Cause of the repeat count: WIND_DETACH "long" gives same-pitch joins of long notes a 0.025 s gap (the finale's form); 84
brass and 8 wind joins that were not counted as repeats now are, and most separate by under 3 dB by design (no dip in
the sustained chord). Not judged by ear.
The 8 re-bow holes (dB): Violas 292 11.0, 36 9.9, 52 8.1; celli 40 13.7, 295 13.5, 180 9.5, 52 8.7, 12.7 8.5.

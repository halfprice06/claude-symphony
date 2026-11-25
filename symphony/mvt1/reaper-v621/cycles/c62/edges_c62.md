# Fast fader edges inside sounding notes, c62 build (note_slope_guard on)

Measure: cycles/c62/actor_scripts/lib62.py edges() = the c61 env61 edges() unchanged: runs of written envelope points steeper than 3 dB/s whose part inside a sounding note of the track (moved note-on to note end) moves 1.5 dB or more. Kind: 'new' when a moved note-on of the track lies from 0.15 s before the run's start to 0.35 s after its end, else 'held'. Times are seconds from score qn 0; bar = qn // 4 + 1.

Total 30 (c61: 354).

| family | inside a held note | at a new note | of which 6 dB or more inside |
|---|---|---|---|
| brass | 0 | 6 | 1 |
| harp | 0 | 1 | 0 |
| strings | 0 | 19 | 2 |
| winds | 0 | 4 | 1 |
| all | 0 | 30 | 4 |

By class: {'sudden mark': 9, 'printed dynamic step': 20, 'other': 1}. 'sudden mark' = printed sf / fp / sub. p (the coordinator's exception); 'printed dynamic step' = a printed dynamic that changes the level on the note with no hairpin arriving there (mix.json note_slope_guard mark_steps: an extension of the exception, see CHANGES.md); both are written as a 20 dB/s ramp that ends 0.03 s before the moved note-on, inside the note before when that note still sounds.

| track | time s | bar | qn | size dB (inside) | dB/s | kind | class |
|---|---|---|---|---|---|---|---|
| Bassoon 1 | 303.52-303.66 | 134 | 535.57 | -2.8 (2.4) | 20 | new | printed dynamic step |
| Bassoon 2 | 160.78-160.92 | 61 | 243.65 | -2.5 (2.5) | 18 | new | sudden mark |
| Clarinet 1 | 160.55-160.92 | 61 | 243.24 | -6.9 (6.9) | 19 | new | sudden mark |
| Double basses | 57.27-57.52 | 12 | 47.70 | +4.9 (4.9) | 20 | new | printed dynamic step |
| Double basses | 182.37-182.54 | 72 | 285.58 | +3.4 (3.4) | 20 | new | printed dynamic step |
| Double basses | 204.05-204.31 | 83 | 331.11 | +5.0 (3.2) | 19 | new | sudden mark |
| Double basses | 320.70-320.84 | 143 | 571.65 | +2.8 (2.8) | 20 | new | printed dynamic step |
| Harp | 164.94-165.07 | 63 | 251.69 | -2.5 (2.5) | 19 | new | printed dynamic step |
| Horn 3 | 57.02-57.62 | 12 | 47.51 | +12.0 (12.0) | 20 | new | printed dynamic step |
| Horn 3 | 160.79-160.89 | 61 | 243.66 | -2.1 (2.1) | 21 | new | sudden mark |
| Horn 4 | 160.67-160.89 | 61 | 243.45 | -4.2 (4.2) | 19 | new | sudden mark |
| Horn 4 | 303.37-303.64 | 134 | 535.25 | +5.3 (3.3) | 20 | new | printed dynamic step |
| Oboe 1 | 116.83-116.92 | 40 | 159.65 | +1.7 (1.7) | 19 | new | sudden mark |
| Trumpet 2 | 99.42-99.75 | 31 | 123.08 | +6.7 (5.3) | 20 | new | printed dynamic step |
| Trumpet 2 | 318.70-318.89 | 142 | 567.45 | +3.7 (2.5) | 19 | new | printed dynamic step |
| Violas | 57.10-57.40 | 12 | 47.57 | +5.8 (5.8) | 19 | new | printed dynamic step |
| Violas | 190.95-191.07 | 76 | 303.60 | -2.4 (2.4) | 20 | new | printed dynamic step |
| Violas | 321.97-322.56 | 144 | 574.31 | +1.9 (1.9) | 3 | new | other |
| Violins I | 116.70-116.91 | 40 | 159.37 | -4.1 (2.5) | 20 | new | sudden mark |
| Violins II | 116.87-117.01 | 40 | 159.73 | +2.0 (1.8) | 14 | new | sudden mark |
| Violins II | 183.36-184.33 | 72 | 287.66 | +3.0 (2.9) | 3 | new | printed dynamic step |
| Violins II | 190.74-191.01 | 76 | 303.16 | -5.4 (5.4) | 20 | new | printed dynamic step |
| Violins II | 358.86-359.02 | 161 | 643.31 | -2.9 (2.9) | 18 | new | printed dynamic step |
| Violoncellos | 57.06-57.42 | 12 | 47.54 | +6.9 (6.9) | 19 | new | printed dynamic step |
| Violoncellos | 127.60-127.82 | 46 | 182.01 | -3.9 (3.9) | 18 | new | printed dynamic step |
| Violoncellos | 182.01-182.42 | 72 | 284.83 | +8.6 (8.6) | 21 | new | printed dynamic step |
| Violoncellos | 203.81-204.33 | 83 | 330.61 | +10.2 (2.7) | 20 | new | sudden mark |
| Violoncellos | 211.73-211.90 | 87 | 347.24 | -2.8 (1.6) | 17 | new | printed dynamic step |
| Violoncellos | 303.44-303.58 | 134 | 535.40 | -1.6 (1.6) | 11 | new | printed dynamic step |
| Violoncellos | 320.44-320.69 | 143 | 571.10 | +5.0 (5.0) | 20 | new | printed dynamic step |

# Carry-over from c05 (written after unlocking)

REAPER holds exactly build/parts.json and build/mix.json: the c05 render (cycles/c05/rendered_build/) plus the stem-fix
damp on Crash cymbals and Bass drum, written with `build_reaper.py --mix-only` before the quit. No REAPER change is pending.

Before rendering: wait until REAPER's memory reaches about 45 GB (c05's first render passed the settle gate at 30 GB and
was half-loaded; cycles/c05/CHANGES.md "REAPER").

Open items measured on the c05 render (cycles/c05/CHANGES.md):
- Violas' soft ends still fall 10 dB in 0.05-0.14 s (454.86, 198.88); the violins reach -20 dB in 0.36-0.40 s, a little
  under the 0.43-0.58 s reference. Check which viola release groups ship under the 500 ms pp cap.
- Celli Sus MAX repeats 604-658 still +127 ms (n 4) after the +0.07 s re-tongue lead.
- Deferred from c05: C #2 brass width, C #3 soli side shelf (side_lua code first), C #4 harp harmonics, A #2 felt timpani,
  A #6, B #5; and c04's open items (re-bow refit, celli legato ends, Horns a2, grace run into bar 35, Bassoon 1 v100 joins).

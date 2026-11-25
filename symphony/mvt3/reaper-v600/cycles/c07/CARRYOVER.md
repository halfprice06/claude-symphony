# Carry-over from c06 (written after unlocking, 2026-11-08 13:15)

REAPER holds exactly build/parts.json and build/mix.json (the c06 render plus the stem-fix gains, written with --mix-only
before the quit). The project has 35 tracks: 31 instruments + "R Strings", "R Brass", "R Winds", "R Perc". Every build
mode refreshes the return tracks first (returns_job) and re-sets each written track's FAMILY EQ and sends.

Before rendering: wait until REAPER reaches 44 GB (c06 settled at 44 GB after a 13 min reload).

Open from c06 (cycles/c06/CHANGES.md):
- Master 6-20 kHz share -25.1 dB (c05 -29.0, Brahms -32.2): halve the family shelves (strings +2, brass +2, winds +2.5;
  critic B #4). The strings shelf is stored at 0.33 oct (resonant in the RBJ form): check its response.
- Decays: tutti -20 dB in 0.62-0.73 s, RT60 about 2.0 s, soft string ends 0.47-1.0 s to -10 dB (references 0.20-0.40).
  Return level hardly matters (wet06.py); test Spaces II's irSetup envelope (envelopeMode 2, endPos 0.5, decayLength 0.5)
  on the returns (edit the chunk JSON in returns_job, or a mix.json override), or the Duc hall.
- Bar 263 downbeat -0.2 dB against 1047 (target +1).
- Duc sends and basses 205-250 Hz cut (Movement I commit 96d05220), repeat gaps by family, legato velocity by dynamic,
  PHRASE_SHAPE, CC1-only test, critic C #4 (sfp spike follows the moved onset).
- R Brass / R Perc stems were scaled by hand in the c06 stem fix; the c07 render will reproduce the sends exactly.

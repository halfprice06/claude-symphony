# Carry-over from c04 (measured after unlocking; nothing here is missing from REAPER)

REAPER holds exactly build/parts.json and build/mix.json as rendered in c04 (cycles/c04/rendered_build/). No REAPER
change is pending.

Open items measured on the c04 render (cycles/c04/CHANGES.md):
- Re-bow fills: refit on c04 (`fit_rebows.py 4 cycles/c04/rendered_build/parts.json --write`, refit mode). Violins I
  178.99 (stem dip 14.6 dB) and Violins II 174.49 (12.4) got worse with the c03 fit; the celli 172-192 and basses still
  dip 8-11 dB on the stem (master under 6). 8 of 24 fits sat at the +9/+10 dB clamp: consider REBOW_VEL_BY_CC (critic
  C #5) for the soft pieces.
- Celli phrase ends on the legato rows did not shorten with the 150 ms cap (drop at 0.15 s 10.5 -> 9.6 dB, 0.5 s to
  -20 dB); the celli are the slowest stem at every tutti cut-off. Check which groups sound after the celli note-offs
  (RT trails, Leg BC sustain groups not hit by the cap).
- "Horns a2" (critics A #2 / C #2): deferred twice. Needs a pass-2 project (main settles at 45 GB) and Movement I's
  fix of the espr./dolce boost-span code for TRACK_WINDOWS / alias tracks (tools/score_to_parts.py line ~3155) before
  any alias is built; diff the alias's notes and CC lanes against its source track before rendering.
- Grace run into bar 35: the violin run is led 0.14-0.17 s ahead of the winds by its target's legato lead.
- Bassoon 1 solo (456-500): v100 targets still up to +144 ms (6 over +80 ms): per-onset leg_leads.
- `rt_gain_db`: do not adopt (Movement I's result was invalid).

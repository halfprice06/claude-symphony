# One-time task for the c07 actor: the rest of EastWest's template adoption (MIDI rules; c06 did the mix)

c06 adopted the template mix (plan items 1-3 and the section 8 mix defaults; `cycles/c06/CHANGES.md`, `loop/ONE_TIME.c06.done.md`).
It deferred the performance data (plan item 5 and sections 6-8's MIDI defaults) to c07, because c06 was already a full rebuild
of every track with a new reverb, mic layout and EQ, and the MIDI rules need a render of the new mix to measure against.

Read first (read only): `mockup-kit/EW-TEMPLATE-PLAN.md` (sections 5-8), `mockup-kit/EW-TEMPLATE-FINDINGS.md`,
`loop/RESEARCH-FINDINGS.md`, `loop/ONE_TIME.c06.done.md`, and Movement I's c51 tools if it has posted them
(`symphony/mvt1/reaper-v621/tools/`, `mockup-kit/pipeline/`; port them rather than writing your own).

Do in c07, alongside the critics' fixes (every item is a default; drop one only with measured numbers, recorded in LEARNINGS):
1. Repeated-note gaps 60-100 ms (medians: winds 63, strings 90, brass 98, short rows 116 ms). At the scherzo's quarter 264
   an eighth lasts 114 ms, so cap the gap at a share of the note (the STR_REP_NEW_BOW / WIND_REP rules' `frac`) and measure
   the repeat dips (S1) against c06.
2. Legato overlap 45-80 ms on strings, 33-58 ms on winds and brass (compare with our measured leg leads first).
3. Legato velocity follows the dynamic (r about 0.35, around a median of 90; check what velocity does on each legato
   patch in the 2021 manual: on the string Leg rows it sets the LegatoSpeed start offset).
4. CC1 drawn at 7-13 points per second on sustained and legato lines; the phrase rule: a swell after the first onset
   (about +15 by 0.4 s, +25 by 0.8 s, nothing before the onset), the peak in the middle third of the phrase, a taper of
   about 20 over the last second, scaled to the dynamic, printed hairpins take over; inside slurs a small per-note
   lean-off (about -2 by 0.4-0.8 s). Mind the woodwind Non Vib / Vib zone (CC1 55-76, both layers sound).
5. The CC11 -> CC1 ("Mod + Expression Combo") staged test on the strings, as a pass-2 copy, adopted if no worse.
6. String shorts: CC1/CC11 parked at 110-127 with dynamics by velocity (EW medians 24-52); brass and wind shorts v62-95.
7. A seeded tutti entry spread of 36-55 ms from first to last section at tutti entries (plan section 8); tune by clarity.
8. Separate string legato tracks ("Leg Slur + Port LITE") are a test only if memory allows (c06 settled at the figure in
   CHANGES.md; the cap is 45 GB).

Also open from c06 (see its CHANGES.md): the mic-layout level residuals and the return levels, if the c07 critics measure
them off; Duc's single hall is the fallback if the EW returns measure mushy. Room-noise bed: skipped (no recording we are
free to use); revisit only if one is supplied.

When done, rename this file to ONE_TIME.c07.done.md and list in CHANGES.md what was adopted, deferred or rejected.

Added by the orchestrator (from Movement I's c50 critic B, symphony/mvt1/reaper-v621/cycles/c50/reports/B.md, simulated on dry stems; check each against our c06 stems before adopting):
- Timpani: the template's timpani EQ (+8.6 dB at 84 Hz) plus its Surround mic at 0 dB break Dan's "timpani rolls must not drown parts" rule (the EQ alone took the timpani's 30-150 Hz share over a 14-bar roll from 13% to 31%). Movement I keeps its old timpani mics (no Surround, which also saves memory) and the finale's reduced timpani EQ (symphony/mvt3/reaper-v600/, read only). Measure our rolls (bars 91-100, 332, the coda) and do the same if they mask.
- Brass make-up: the family EQ takes 6-9 dB (K-weighted) off brass against 1.3-1.9 off strings; c06 applied 6-10 dB, so check soft trombones and trumpets (they lose more) against soft horns and tuba (they lose less).
- Winds 1.5-2 dB hot (doubled Close), tam-tam and cymbals about 3 dB hot (no family EQ), and the harp's 183 Hz high-pass cuts a third of its fundamentals (80 Hz suggested). c06's stem fix already took flutes -3/-3.5, clarinet 2 -2.5, bassoons -1.5/-2, harp -2: put those into the build and check the harp high-pass.

Also from Movement I's c50 critics (symphony/mvt1/reaper-v621/cycles/c50/reports/), on wetness and brightness. Dan's standing note is "too wet, mushy", so treat these as c07 targets:
- Decay limits: every tutti stop falls 20 dB in 0.58 s or less (median 0.55 s or less); drop at +0.3 s at least 15 dB (c06: 13.9); late slope 2.0 s or less; the 60-250 Hz share of each tail no more than 2 dB over the previous cycle. Fix order if missed:
  1. The plan's section-9 register sends: bassoons, contrabassoon, trombones, tuba and basses 10 dB under their family send; trumpets 6 dB under.
  2. The Spaces II IR envelope on the returns: irSetup envelopeMode 2, endPos 0.5, decayLength 0.5.
  3. Duc's 2.3 s profile.
  Lowering return levels barely shortens the tails (the finale's result), so do not rely on that alone.
- Brass brightness: the brass family EQ makes brass about 6.5 dB brighter against its body. Check the master's 2-5 kHz jump at brass accents, with p90 under +2 dB. If it is over, cut the 821 Hz bell to -4 dB or add a 3.2 kHz -3 dB bell. Drop any trumpet 4 kHz shelf that stacks on the family shelf.

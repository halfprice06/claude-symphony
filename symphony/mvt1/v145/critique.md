# v145 — cycle 125 (critic 125, lens: engraving; reading: Gould, Behind Bars ch. 1 beams, PDF 31–41)

Report: critics/reports/c125.md (25-row Reading notes table).

Applied (layout only; no notes, rhythms, dynamics, slurs or tempo words changed):
1. Solo lines on shared staves at 33–40 (Fl 1, Ob 1, Cl 1, Bn 1) and 77–78 (Bn 1) were printed with forced up-stems, because the part-combiner keeps a solo in the up-stem voice while a hairpin runs. New helpers `soloStemsOn` / `soloStemsOff` in global.ily restore normal stem direction for those solos (Gould PDF 33, 35, 38). global.ily, trans.ily, dev.ily.
2. False "2." label at 139 in Fl, Ob, Cl (both players sound): `\partCombineApart` for 139–142, automatic again at 143. recOne.ily.
3. Harp right-hand beams at 47–63: `\override Beam.damping = #3`, reverted after 63; slopes about one space (Gould PDF 33–34). tTwo.ily.

Open: flutes a2 at 158–162 and Bn 1 at 88–90 still print up-stems in the full score (overrides had no effect; same cause suspected; next steps in the report).

Build: no warnings, 17 pages; parallels: the known bar-96 doubling only.

# v216 — critic 196 (playability; Sebesky ch. 2 wind instruments) — 2 changes

Report: critics/reports/c196.md

Applied:
1. The bass clarinet part stays in French treble clef through 91–106 (parts-clefs.ily `bclClefs = { \clef treble }`; parts only). This replaces the German-notation bass clef chosen in c185, which was still an open item. Sources: Sebesky p64 Ex. 72; VSL bass clarinet page; Steinberg forum.
2. Cl 2 has a quarter rest on beat 4 of 120, a breath before the fff (sections/dev.ily). The violas keep the triplets. Sources: Sebesky p24, p42–44. c186 allows breaths in 117–122.

Not applied (composer's choice):
- Move the Ob 1 low F4–E♭4 link at 45–46 (p) to the cor anglais (Sebesky p71–72). This is accepted c161 material.
- Cor anglais 5–9 single slur of about 19 s: at most a part-only "breathe ad lib.".

Checked, no change needed: Hn 4 bass clef at 11–12; Bsn 1 in bass clef; oboe unisons; ranges; trombone slides; page turns.

Checks: 0 warnings; only the bar-96 parallel; 18 PDF pages; full.midi rebuilt; the all-pairs check shows no new parallels; parts rc=0, 30 PDFs. The v215 full.midi was stale: c195 did not rebuild it after changing Cb 102. The v216 full.midi is current.

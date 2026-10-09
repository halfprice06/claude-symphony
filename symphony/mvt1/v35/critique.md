# v35 — cycle 15 (critic 15, lens: engraving)

Report: critics/reports/c015.md

Applied (1–7 tested together by the critic in a scratch build; I reviewed the diff and copied it):
1. Dynamics and hairpins no longer print on top of the noteheads. Since v25 they had been created outside any DynamicLineSpanner; Dynamic_align_engraver now moves to Staff with Dynamic_engraver, and the DrumStaff line (the real cause of cycle 5's 280 errors) is removed.
2. Harp pedal changes marked below the bass staff throughout the second theme (51–66); the unplayable E♭/E♮ in bar 56 respelled as F♭.
3. Ottavas removed again from the shared flute staff at 41–43, 71–72 and 113–115 (flute 2 was printing an octave low under them).
4. Duplicate dynamics an eighth apart removed at 27, 69, 109, 131 and 163; the wrong "2." label at 69 fixed.
5. "1." labels on entries after long rests (oboe 148, horn 47).
6. Expressive words (espr., dolce, largamente, morendo) in italic; technical words stay roman.
7. System breaks before 15 and before 167 (page 1 now ends at 14; the Lento coda has a full system). The score is now 17 pages.
8. (Applied by me.) Rehearsal letters skip I; bar numbers smaller with more padding so they no longer collide with tempo words; fermata on the harp's last chord.

Build: no warnings; 17 pages; outer-voice parallels: the known bar-96 octave doubling only.

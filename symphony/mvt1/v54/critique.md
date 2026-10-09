# v54 — cycle 34 (critic 34, lens: orchestration and colour)

Report: critics/reports/c034.md

Critic's statistics: the oboe doubles moving Violins I in 73% of bars (Tchaikovsky 5/i ~2%, Dvořák 9/i ~3%); moving Violins I are undoubled in 21% of bars (69% and 95% in the models). Too much to fix in one cycle without touching protected passages; recorded as a rule for movements II and III.

Applied (tested by the critic in a scratch build; I reviewed the diff and copied it):
1. Ob 1 rests at 94–96; the flutes rest at 103–106 and re-enter f at 107, so the fff at 114 gets a fresh wind colour.
2. The ff tutti chords at 33 and 135 shortened to an accented eighth (`X8->\ff r8 r2.`) so the head's first G is heard after them.
3. "div." at 163 in both violin parts; "unis." at 167 (Vln II) and 173 (Vln I).
4. Contrabassoon holds C1 under 163–166.

Build: no warnings; outer-voice parallels: the known bar-96 octave doubling only.

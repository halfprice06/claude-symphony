# v32 — cycle 12 (critic 12, lens: harmony and voice leading)

Report: critics/reports/c012.md

Applied (findings 1–7 were tested together by the critic in a scratch build; I reviewed the diff and copied it):
1. Bar 96: five consecutive parallel fifths (Fl/Ob/Vln I against Cl 1/Vln II/Vla) removed; the lower line now runs a third below (des'' bes''4. a'' aes''4).
2. Bars 123–124: Tpt 1 g'1 | g'2. b'4 and Hn 3 c'2. b4, so the counterline's suspensions no longer sound against their own resolution notes.
3. Bar 156: Hn 1·2 and Cl 1 counterline es'4 c''4 so the dominant 7th F resolves to E♭ (fifth of ♭VI) at the climax.
4. Bar 42: Hn 1·2 c'4 bes2. (removes fourteen voice-pairs of parallel fifths created in cycle 2).
5. Inner fifths: Hn 4 rests at 66; Tpt 2 holds a♭' at 70; Tpt 3 holds f' at 132.
6. Bar 169: Vla c'2 des'2, so the cor anglais's C no longer rubs against the viola's D♭.
7. Bar 64: Cb and harp follow the cellos' D (f,2 d,2).
8. (Untested by the critic; applied by me.) Cadences 67 and 161: the cello arpeggio's held top note no longer doubles the melody's 2 an octave below; it ends on the 7th (D♭ at 67, F at 161), which falls by step.

Tooling: tools/analyze.py now reports runs of parallel fifths; only runs of octaves are treated as doublings.

Build: no warnings; outer-voice parallels: the known bar-96 octave doubling only.

# v25 (cycle 24, orchestration: tutti chords; critic report critics/reports/c024.md)

Reading: Rimsky-Korsakov appendix of tutti chords (PDF 505–507) and the tutti examples No. 204–215 (PDF 367–385), with ch. IV (PDF 115–136). All 3 findings accepted and applied:
1. ERROR FIX: Hn 4 had 24 bars in dC (20 expected) since the v24 cut, so it ran 4 bars late to the end (missing from the coda tutti, sounding through the G.P.). Now R2.*4. The old countbars.py missed it; it is replaced by kit/partlengths.py (lyparse-based, run in promote.sh).
2. Reprise tutti 305–320 rescored: Fl 1 plays the upper octave at 309–312 and 317–320 (top A6, below the coda's B6). Theme record: the Fl 1 line at 305 removed (no longer a plain doubling).
3. Final ff chord of the scherzo proper (339): string multiple stops (Vln II G3–E4–B4–G5, Vla B3–G4–E5, Vc E2–B2).
Build: 0 warnings, 13 pages, 7 analyser parallels, theme record 40/40, no C-major triad, part lengths all match.

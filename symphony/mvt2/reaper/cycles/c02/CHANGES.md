# Cycle 2 changes (actor)

Input: critic reports A (articulation), B (balance), C (dynamics over time) on the cycle 1 render. Snapshot of the tools and build JSON before any change: `before/`. Final render: `render/`, `metrics/metrics.md`, `mvt2-mockup-c02.mp3`. Two earlier renders are kept: `pass1/` (all track gains lost, see below, and patches still loading) and `pass2/` (gains fixed, before the last trim adjustments).

## What changed

### tools/build_reaper.py
- **Articulations are loaded (A1).** `load_articulations()` sets `loaded`/`active` on every `layerMatrix` row the track uses and gives its trigger `useKey` and a `triggerName` (C0 = key 24). The string KS Masters load only their first six rows, so pizz., tremolo and flautando keyswitches were ignored in c01. Now loaded: Pizz in Vla/Vc/Cb, Tremolo in Vln I/II, Vla, Vc, Flautando in Vln II, Leg BC MAX in Vln I/II, Vla, Vc.
- **Legato speed (A2a).** Patches that use a Leg articulation get `EWSO.legato_speed_active = true` and `RTKiller.active = true`, as in the dedicated `1st Violins Leg Slur MAX.oib` and `1FH Leg Slur Accent MAX.oib` (checked in the files).
- **Volume envelope (B2, B5, C1, B1 roles).** Each track gets a REAPER volume envelope: mix.json `gain_db` + parts.json `vol_db` + mix.json `dyn_trim_db`/`soft_trim_db` read from the printed dynamic curve. CC11 still selects the dynamic layer.
  - REAPER ignores `D_VOL` once a volume envelope exists. The first render (pass1) lost every track gain: Vln I -7 dB, Cb +8 dB. The gain is now inside the envelope and `D_VOL` is set to 1.0.
  - `--mix-only` now rewrites the envelopes, so level changes need no patch reload.
- CC70 lane written with the other CCs.

### tools/score_to_parts.py
- `DYN["ff"]` 104 → 114, `fff` 118 → 124 (C2c). `measure.py` `DYN_NAMES` updated.
- **sf with a decrescendo (B4, C2b):** spike to max(100, level+12) at q+0.02, then down to min(level, mf) at q+0.5, where the hairpin starts. sf notes get +15 velocity.
- **Untargeted hairpins** move 22 CC from mp or softer (C4); 14 above.
- **Leg BC (A3).** Monophonic string notes that are unslurred, or that start a new slur straight after another, are played with `Leg BC MAX` and overlap the previous note by 0.04 qn. Unslurred monophonic string notes use Leg Slur MAX instead of Sus MAX. Basses are unchanged (no Leg BC). Counts: Vln I 31, Vln II 42, Vla 48, Vc 57 BC joins.
- **Legato velocity (A2b):** strings and brass legato targets 120 (< 0.9 s) / 105. Winds keep the c01 table.
- **Solo boost (B1, C2a):** strings +8 only for "solo", +3 for espr./cantabile/dolce. Winds/brass keep +8 for solo/espr./cantabile and get +3 for "dolce" alone. The boost fades linearly to 0 between mp and f.
- **Phrase shaping (C5):** notes of 1.8 s or more with no hairpin, no inner onset and no repeated pitch get +4 CC at 40% → -2 at the end. Phrase-final notes (slur end, breath, rest ≥ 1 qn) get -6 CC over the last half. Not applied in the final bars.
- **Anti-bloom (B6):** soft (≤ p) re-struck Sus MAX string chords get +6 CC at the onset → -2 at 1 qn → 0 at the end.
- **Final bar (C1):** CC11 ramps to 8 over qn 302-304, and `vol_db` fades every track sounding at the end by -20 dB from 301.5 to 304.
- **Finger position CC70 (A4):** 127 under sul D/G/C; under sul A, 20 for pitch ≤ 74 and 127 above. Ends at "ord." or "unis." without a new "sul".
- **Horn 3 con sord. (A6):** CC15 127 from qn 271.5, using the 1FH ConSordino script.
- **Timpani (B3, C6):** roll table mf -17, f -16, ff -14 (ppp/pp unchanged). Strokes at pp get roll +20. The roll settle moved from CC7 to `vol_db`: -5 dB over 3 qn on rolls of 3 qn or more, none under a crescendo.
- New outputs: `cc70`, `vol_db`.

### build/ (config)
- `mix.json`: `dyn_trim_db {f, ff}` per track (B's table shifted by +1 dB at f and +2 at ff, corrected for the CC104 → 114 change; final values in the file), `soft_trim_db` ppp -4 / pp -2 (all but timpani and harp harmonics). Timpani `gain_db` -6 → -7. After pass2: Trombone 1 ff trim 7 → 4, Double basses f/ff 2/3 → 0/-1.
- `roles.json` (new): Violoncellos [66,90,-5], [188,204,-6], [238,274,-5]; Harp [124,140,-3].
- `note_trims.json` (new): Oboe 1 F5 -7, Cor anglais A4 -8, Flute 1 B♭6 -4, on notes of 1.5 s or more, ramped over 0.6 s.

### tools/render_cycle.py
- The wait for sample loading now requires three quiet 10 s memory readings, not one. The pass1 render, started right after a full rebuild, had 83 late entries; the same project rendered again 25 minutes later had 26.

## Measured, c01 → c02 (final render)

| | c01 | c02 |
|---|---|---|
| Integrated | -27.4 LUFS | -27.2 LUFS |
| LRA | 23.5 LU | 24.7 LU |
| True peak | -9.2 dBFS | -8.4 dBFS |
| Late entries (> 120 ms to -60 dBFS, after silence) | 51 | 23 |
| Pizz. median drop 400 ms after peak (Vla / Vc / Cb) | 6.0 / 0.7 / 2.3 dB | 9.9 / 16.2 / 10.8 dB |
| Bar 92 vs bar 91 (RMS) | -44.9 vs -43.7 | -54.9 vs -47.1; last 0.7 qn -67.3 |
| Bars 59 / 61 / 63 (RMS, 4 qn) | -27.0 / -23.4 / -26.9 | -28.2 / -23.1 / -26.4 |
| Bars 79 / 80 | -24.4 / -23.5 | -24.5 / -23.4 |
| Bar 63 beats 2-4: Tbn1 vs Vln I | -35.8..-38.5 vs -34.6..-43.3 | -29.2..-29.6 vs -39.3..-42.6 |
| Vc vs Vln I, qn 78-84 / 190-200 / 250-256 | +9.9 / +10.4 / +8.7 dB | -1.4 / +1.2 / -0.5 dB |
| Timp ppp roll bars 2-3 / 89-92 | -49.1 / -49.1 | -52.0 / -53.7 |
| Horn 1 over timp, bars 69-70 | +2.5 | +5.7 |
| Timp pp strokes qn 277 / 278.5 / 279 | silent / -63.4 / -60.5 | -52.6 / -61.0 / -58.7 |
| Cor anglais qn 152-156 / Oboe qn 45-47 | -37.1 / -39.5 | -44.3 / -46.5 |
| ff, qn 258-264: Fl1 / Ob1 / Vln I | -33.7 / -48.3 / -37.2 | -40.6 / -43.7 / -38.8 |
| 63 Hz band re 1 kHz (ref -6.2) | +4.7 | +5.1 |

## Rejected or deferred
- **A2c (move legato targets earlier):** deferred. The lag needs re-measuring with legato speed on and velocity 105-120.
- **A5 (divisi DIV A/B tracks):** deferred. It adds tracks and patch RAM, and Leg BC fixes the connected lines first.
- **C3 (per-patch CC11 curves from a sweep render):** deferred. It needs a scratch project. Partly covered by `soft_trim_db` (ppp -4, pp -2).
- **B2 trims as given:** shifted upward (+1 at f, +2 at ff) so the climax does not get quieter. Applied exactly, B's cuts to strings and flute would have undone C's f-to-ff growth.
- **B1 +3 for winds' espr.:** not applied. The +8 stays for wind and horn solos (do-not-touch horn lead in bars 7-14). The +3 applies to string sections and to "dolce" alone.

## Open (for the next critics)
- Bar 61 is only level with bars 79-80 (target 2 LU louder).
- Trombone 1 leads the diminishing strings by about 10-13 dB in bar 63 beats 2-4 (target 4-6).
- Timp pp strokes at 278.5 and 279 are still about -60.
- 23 late entries remain, mostly at qn 0 and at section entries (Vln II/Vla at 0 by 0.8-0.95 s).
- Legato lag, slur-boundary dips and Leg BC joins have not been re-measured.
- Low end: 63 Hz +5.1 against the reference's -6.2.

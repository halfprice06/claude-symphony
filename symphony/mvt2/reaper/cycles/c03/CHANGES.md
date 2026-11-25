# Cycle 3 changes (actor)

Input: critic reports A (articulation), B (balance), C (timing) on the cycle 2 render. Snapshot before any change: `before/` (tools + build JSON). Final render: `render/`, `metrics/metrics.md`, `mvt2-mockup-c03.mp3`. `pass1/` is the first render (full rebuild), before two envelope-only fixes (Vln II roles, Bn1 trim at qn 208).

Analysis scripts (critics' scripts adapted to report against the score onset, since note onsets now move): `/private/tmp/claude-501/mockup-loop/c03-actor/an/`. `parts.json` notes carry `sq` (score onset) for this.

## What changed

### tools/score_to_parts.py
- **Legato lead (A2, C1).** Every legato target starts early by `LEG_LEAD_S` at the local tempo: strings 0.17 s, brass 0.10 s, oboe/bassoon 0.06 s, bass clarinet 0.05 s, flute/clarinet/cor anglais 0. Capped at 0.45 x the previous note; the previous note ends `LEG_OVERLAP` after the new onset. CC11/CC1/vol_db stay on score time; keyswitches stay at least 0.03 qn before the moved note. Legato velocity: strings 124, brass 124 (< 0.9 s) / 112.
- **Soft-entry lead (C5).** Sustained notes after at least 0.5 qn of silence start early (`ENTRY_LEAD_S`): strings 0.12 s at CC11 <= 50 / 0.06 s above, brass 0.10 / 0.05, bassoons and contrabassoon 0.06. CC11 holds the entry's own level from the moved onset ("pulls"), so the attack never takes the previous dynamic.
- **Same-pitch merge (A1).** In legato string lines a repeated pitch (gap < 0.1 qn, no breath) is merged into one note with a CC11 notch at the second onset: 10 CC for portato (tenuto in one slur), 14 CC for a bow change; the tenuto bump stays. Vln II 11, Vla 8, Vc 5 notches.
- **Tenuto (A3).** Strings: tenuto notes join with Leg BC / the slur legato when the pitch changes. Basses: 0.02 qn gap. Winds/brass: `min(0.03, 0.1*dur)` gap at mf and louder or under "sostenuto", 0.06 qn otherwise.
- **First keyswitch (A4).** Tracks whose first note is at qn 0.5 or later also send their first keyswitch (at qn 0). Fixes Trombone 1's first two accents.
- **After-grace run (C2).** Grace notes (event rows with a negative grace offset) are re-placed to end on their main note, 0.09 s each, velocity 127, all on Leg Slur (no Leg BC/keyswitch inside the run); the main note is held into the first grace; the run moves with its target's legato lead.
- **Fast slurred string notes (C3).** Slurred monophonic string notes under 0.25 s (viola sextuplets, bars 59-60) use Sus MAX overlapping the next note by 0.03 qn instead of Leg Slur/Leg BC.
- **Tempo ramps (C4).** `RAMP_SPANS`: inside each rit./allargando/animando span the `\mt` step values sit at the midpoints of their steps, joined linearly and written as 0.25 qn steps. Span lengths change by under 0.05 s (printed to stderr). Final 36 -> 20 step unchanged. 303 tempo markers.
- **Timpani (B1).** Soft roll chains (whole chain p or softer: qn 3, 168, 226, 292) get a flat -6 dB in vol_db, held through the ring like the settle; p strokes roll + 12 (was + 16); `TIMP_VEL` raises qn 278.5 and 279 to velocity 60.
- **Divisi/double stops (B2).** vol_db per string track: where k >= 2 notes sound, -10 log10(k) dB under "div.", -1.5 dB otherwise; all-tremolo chords a further -3 dB; starts 0.1 qn before the chord.
- **Note trims by onset (B4).** `note_trims.json` is now `{track: {onset qn: dB}}`, matched within 0.02 qn, no length cutoff.

### tools/build_reaper.py
- A track's own `soft_trim_db` in mix.json replaces the global one.

### build/ (config)
- `mix.json`: Violas `dyn_trim_db` f -2 / ff -3, own `soft_trim_db` {ppp -4, pp 0}; Bassoon 1 f/ff 1.5/1.5; Bassoon 2 f/ff 2/3 (B3).
- `note_trims.json`: B4's onset table, plus Bassoon 1 {208: -4} (pass1: Bn1 -28.6 over Vln I -31.0 at the ff).
- `roles.json`: Harp [124,140,-7] (B5); Violins II [108,124,-3] (pass1: the div. sul tasto chords were only 1-2 dB under the flute solo).

## Measured, c02 -> c03

Lag figures are against the score onset (crossover method of C's `leg.py`; c02 numbers from the critic reports).

| | c02 | c03 |
|---|---|---|
| Integrated / LRA / true peak | -27.2 LUFS / 24.7 LU / -8.4 dBFS | -28.1 LUFS / 24.0 LU / -10.2 dBFS |
| Legato crossover median, Vln I / Vln II / Vla / Vc | 250 / 275 / 220 / 260 ms | 50 / 85 / 80 / 62 ms |
| Horn 1 / Horn 2 / Ob 1 / Bn 1 | 202 / 190 / 155 / 155 ms | 108 / 85 / 90 / 105 ms |
| Soft-entry arrival median, Vln I / Vln II / Vla / Vc | (C table: 400-1010 ms) | 310 / 488 / 230 / 100 ms |
| Tbn1 attack brightness qn 212.5 / 213 | -8.8 / -8.6 dB | +5.6 / +4.1 dB (218: +6.1) |
| Master dip, qn 44 / 50 / 223 / 289 | -3..-5 / -3..-5 / -6..-10 / -3..-5 | -3 / -5 / -6..-9 / -5..-6 |
| Vln II level, 0.5 qn blocks at qn 223 | -56 | -50 |
| String joins bars 61-62 (master, qn 206/208/210) | -1..-3 dB | within -2 dB |
| Grace run bar 78: all three graces heard; ff 94 wins at | 92 never heard; 262.03 | yes; about 262.03-262.09 |
| Timp ppp roll bar 2 onset / settled | -46.7 / -50.3 | -52.7 / -56.4 |
| Timp roll bar 52 (qn 168-171) vs CA | -42.6..-40.2 vs -46..-45 | -48.6..-45.4 vs -46.6..-44.4 |
| Timp roll qn 229-236 vs Horn 1 | -50 vs -47..-50 | -56 vs -39..-51 |
| Final roll vs Vln I (qn 296-301) | -50.5 vs -53.7 | -56.4 vs -46..-54 |
| Timp p stroke qn 271 | -39.4 | -42.8 |
| Fit at CC104: Vln II / Vla | (Vla 1.8 dB over Vln I at ff) | -33.2 / -35.4 (Vla 2.2 under Vln II) |
| Bn1 / Bn2 at ff vs woodwind median (~-35) | -30.5 / -32.0 at CC114 | -35.8 / -36.5 at CC104 |
| Bars 61-62 Vla vs Vln I | -25..-28 vs -28..-31 | -34..-36 vs -28..-32 |
| Bar 28 Vla vs Vln I | -40.4 vs -47..-42 | -43.4 vs -47..-41 |
| Bars 37-40 Vln II vs Fl 1 | level | Vln II 3-9 dB under |
| Bar 64 Vln II vs Vln I | +7..+10 | +2.7..+3 |
| Harp vs CA, bars 41-43 | +2..+4 over | 3-6 dB under |
| Oboe 1 ff qn 204/208 | trimmed out (-4.6/-5.0 residual) | -33.3 / -33.2, level with Vln I |
| Bn1 qn 208 vs Vln I | -26.2 vs -30.9 | -31.6 vs -31.0 |

No clipping (master peak -10.2 dBFS; every stem present, peaks -32 to -11 dBFS). Tempo-map span lengths are unchanged within 0.05 s.

## Rejected or deferred
- **A5 (DIV A/B tracks):** deferred; B2's divisi level cut covers the balance part. The Vc div. upper line in bars 18/22 is still Sus MAX.
- **A4 state fields (`currentTrigger`, `lastArticulationId`):** not done; the first keyswitch fixes the measured case. Tracks starting at qn 0 still rely on the state.
- **A1 Flautando chord common tones:** not done (master shows no dip).
- **C2 Slur Runs patch:** not used (it would need a keyswitch between the run and its target); the run is on Leg Slur at velocity 127.
- **C3 Leg Slur alternative:** not tried; Sus MAX chosen.
- **C4 caesuras before the breaths at 204/268:** not done (optional liberty).
- **C5 qn 0 pre-roll:** not done.

## Open (for the next critics)
- Master at qn 223 still dips -6 to -9 dB for about 0.2 s, then sits 5-8 dB lower: Vln II's merged 6 qn note decays in the sample under the printed decrescendo. The notch (14 CC at CC ~34) may be too deep at pp.
- Viola sextuplets (f0 trace, 8192-point window): about 90-120 ms behind and the repeated 58 is short; Sus MAX attack lag. A 0.05 s lead on short Sus notes is the next step.
- Soft string entries still bloom: Vln II arrival median 488 ms, Vln I 310 ms.
- Vln I legato now crosses over at 50 ms (others 62-85); slightly ahead of the other strings.
- Cor anglais legato crossover measured 160 ms (C reported 90 on c02, no change to CA); check.
- Bar 28: the violas are still level with the Vln I tune at beats 1 and 3.
- Low end: 63 Hz +5.4 against the reference's -6.2.

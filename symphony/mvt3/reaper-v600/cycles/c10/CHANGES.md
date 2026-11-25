# Cycle 10 changes (actor, 2026-11-09)

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c09 render after its stem fix). Snapshot: `before/`. Builds:
`rendered_build/` (the render data with the stem-fix tables applied; the pre-fix parts.json was overwritten), `final_build/` (final data). Scripts:
`actor_scripts/m10.py` (every before/after number below; `m_c09.json`, `m_c10.json`). Logs: `build1.log`, `render.log`,
`stemfix.log`, `build2_mixonly.log`, `deliver_final.log`.

## What changed

Tools:
- `tools/score_to_parts.py`: Movement I c51's `REP_SPLIT` gap keys ported (`gap_s`, `frac`, `gap_min_s`, `gap_min_cc`;
  also the basses' plain Sus MAX repeats on a patch without Leg BC; parts.json `rep_split_gaps`). `SOST_JOIN_LEAD_S` may
  be a per-track dict (`by_name`, "default"), and a `leg_leads.json` row now also applies to slur-start joins.
- `build/mockup.ly`: the event dump keeps text on multi-measure rests (`multi-measure-text-event`). mockup-events.tsv gained
  12 lines ("soft sticks" 680, "muta D♭ in C medium sticks" 856, "hard sticks" 1016, "metti sord." 664, "togli sord." 732,
  timpani "muta" changes, harp pedal texts); mockup.midi unchanged, parts.json unchanged by it.

Config (`build/score_config.py` c10 block, `roles.json` `_c10`, `note_trims.json` `_c10`, `leg_leads.json` `_c10`,
`mix.json` `_c10`):
1. A #1 (S1): `REP_SPLIT` gap_s 0.08, frac 0.35, gap_min_s 0.06, gap_min_cc mp; the basses' eighths now end 0.063 s
   early (0.47 -> 0.325 qn, 297 strokes); basses detach dip -5 -> -3 dB on 792-840.25 and 984-1108.25; their level shapes
   +1.5 -> +2.0 dB.
2. A #2 (S2): `SOST_JOIN_LEAD_S` Flute 1 0.085, Flute 2 0.16, default 0.12; Flute 2 `LEG_VEL_EXTRA_S` (100, 0.02);
   leg_leads rows +0.08 s for Bassoon 1 466/748/756/845, Oboe 1 188/749/758/1014, Horn 1 51/87/970, Cor anglais
   692/702/738, +0.06 s for Flute 2's bars 27-34 joins (Oboe 1 188 and Bassoon 1 748 were held by the lead caps).
3. A #3: timpani medium-stick EQ window 871.5-985 -> 871.5-1016 (mix.json loud_eq); the event-dump fix above.
4. A #4 (MANUAL-GAPS #5, first try in any movement): Bassoon 1's solo 455.9-496 on the BS KS Master's "Leg Slur Exp"
   (key 77); full rebuild of Bassoon 1.
5. B #1: Trumpet 1 roles [1016, 1032, -3] deleted; LEVEL_SHAPES +2 dB rising over the tied G4 1016-1023.5.
6. B #2: trumpets' ff trims +2 dB (Tpt 1 7.3 -> 9.3, Tpt 2 8.0 -> 10.0, Tpt 3 11.1 -> 13.1).
7. B #3: Violins I roles 168-200 -3 -> -8. B #4: harp note trims -6 on every half qn 488.0-511.5. B #5: Horn 4
   932/936/940/944 -6/-6/-8/-9 (932 -9 after the stem fix), Horn 3 +2/+4/+3/+2. B #6: Violas [892, 900, -3, 1.0].
8. C #2: final ride row [(1087,0),(1088,2.5),(1096,2.0),(1104,2.0),(1107.9,1.5),(1108,1.0),(1113,1.0),(1113.5,0)];
   Horns 1 and 3 LEVEL_SHAPES +2.5 dB rising over 1096-1104, held to 1107.85.
9. C #3 (S3): Violoncellos sfp lead 0.08 s (ROW_LEAD_S span 591.9-592.1); a post-fader bump at 592.0-592.35
   (+3 dB Vln I / Vln II / Vla, +5 dB Vc / Cb).
10. C #4: Horn 1 roles [264, 300, +4] (C asked +5; B measured the line one dynamic step under the p bassoons, so the
    smaller lift). C #5: motive x bars 3-4 (8.8-15.9, opening over the last 0.4 qn) Vln I +4, Vln II +2, Vla +3, Vc +6.
    C #6: Horn 3 [552, 564, -4].
11. C #1 (delivery only): the 167-264 and 451-504 ride steps replaced by `--fit-flat` rows fitted on the c10 master
    (164-200, 200-264, 452-504), +1.5 dB each; the 164-200 row starts 1 dB under its fitted value (164-167) and reaches
    +1.5 by 172 (C's version halved the f -> p drop at bar 41 -> 42: mp3 4.5 dB against the master's 9.1; this one 6.5).

Stem fix after the render (`stem_fix.py --apply`, originals in `render_first/`; also written to REAPER with `--mix-only`):
Bassoon 1 roles [456, 488, -2.0] (the Exp row came out +2.2 dB K); Horn 4 932 -6 -> -9; basses metric tables refit
(984-1056 {down 1.0, mid 1.5, beat 1.5, off -0.5}, 1088-1108 {down 2.5, mid 2.0, beat 1.0, off -2.5}).

Tracks written: `--midi-only` on Flute 1, Flute 2, Oboe 1, Cor anglais, Bassoon 1 (Opus state changed: full rebuild),
Horns 1/3/4, Trumpets 1-3, Timpani, Harp, Violins I/II, Violas, Violoncellos, Double basses.

## Rejected or deferred
- A #3 felt / medium-stick timpani alias (pass 2): deferred; REAPER is at 45 GB settled with 34-38 GB compressed. The EQ
  window now covers the whole medium-stick span.
- A #5 louré chord repeats (violas 842-866): deferred (tool change to the portato rule for chord repeats; next cycle).
- A #6 "div. a 3" at 1108 as thirds: rejected. On Hollywood Strings a div. voice is the same full-section sample at a lower
  level; A asks to give the -4.8 dB back in roles.json to keep the climax order, so the sum would be no change in sound.
- C #3 extra leads on the winds and brass at 592: rejected with numbers. They already start 0.05-0.12 s early (0.10-0.34 qn
  in parts.json) and still peak 0.22-0.27 s after the mark (Horn 1, Trombone 1 +0.27 s): the sample's rise sets the peak.
- C: Horn 1 qn 118 +5 dB: not done (B: an mf hold inside the ff counterstatement, inaudible either way).
- C #1's morendo 170 -> 171 inversion: kept as C advised (a refit made it worse in C's simulation); mp3 171 is 1.3 dB over
  170 while the master falls 2.0 dB.
- Brass "Sfz Cres" row for 592 (MANUAL-GAPS p.103): still untried (memory).

## Measured (c09 -> c10; m10.py, K-weighted on the stems' own scale unless named)
- **Basses repeats (A #1)**, harmonic band (pcx), median dip stem / master, master repeats under 3 dB:
  792-840 7.3 / 2.7 (45 of 81) -> 6.2 / 2.5 (49); 984-1088 5.7 / 3.2 (83 of 177) -> 6.4 / 3.0 (85); 1088-1108 5.5 / 2.2
  (26 of 38) -> 6.0 / 2.2 (28). Stem on-beat / off-beat dips 3.2 / 10.0 -> 4.0 / 7.7, 4.6 / 9.2 -> 3.0 / 9.2, 3.6 / 13.8 ->
  1.1 / 8.0. **Target missed**: the 63 ms gaps did not deepen the master dips (target median 4 dB); the f/ff Sus MAX
  release (150 ms cap) and the celli / timpani / returns fill them. Basses position levels (first 120 ms, down - off)
  before the refit: 792-816 +4.1, 816-840 +2.6, 984-1056 +3.8 (beat - off -0.1), 1056-1088 +4.0, 1088-1108 +1.1; the
  stem fix's tables aim at +2..+4 everywhere.
- **Flutes (A #2)**, pcx attack time re the score onset at 602 / 618 / 634 / 650 / 1007 / 1074: Flute 1 -70 / -22 / -70 /
  -65 / -63 / -70 -> -42 / +10 / -45 / -30 / -34 / -42 ms; Flute 2 +89 / +192 / +105 / +192 / +136 / +89 -> +48 / +152 /
  +49 / +275 / -38 / +49 ms. Bars 27-34 Flute 2 +100..+124 -> +13..+104 (median about +75). The flam on the F1 heads fell
  from 160-260 to 90-140 ms except 650 (305 ms, worse); more lead needed on Flute 2 (its 0.45 cap binds).
- **Bassoon 1 on Leg Slur Exp (A #4)**: joins (pcx, 18) median +14 -> +10 ms, IQR -2..+31 -> -42..+20, none over +80;
  attack to -6 dB of the body 20 -> 35 ms (median); amplitude modulation 4-7.5 Hz share 0.46 -> 0.18 (less, not more,
  vibrato in level; pitch vibrato not measured); level +2.2 dB (fixed by the stem fix). Kept for the critics to judge.
- **B #1** Trumpet 1 1016-1024 / 1024-1032: 28.7 / 34.2 -> 34.6 / 39.2 (Horn 3 35.0 / 37.3; Violins I 30.8 / 30.1); the
  tied G4's fall over its four half bars 4.5 -> 2.9 dB.
- **B #2** trumpets +2.0 dB at ff in every measured window (stop chord 584-592 Tpt 1-3 33.6 / 35.0 / 34.4 against Horn 3
  34.1, Trombone 1 36.8). Master band shares (render metrics) 2-6 kHz -10.68 -> -10.63, 6-20 kHz -26.06 -> -25.96 dB.
- **B #3** Violins I 168-200 15.2 -> 10.2 (Flute 1 / Clarinet 1 / Oboe 1 17.9 / 19.8 / 20.7). **B #4** harp 496-508 20.1 ->
  14.1 (violas 15.7, Bassoon 1 14.9). **B #5** Horn 4 - Horn 3 per onset +9.0 / +10.7 / +10.9 / +11.3 -> +6.2 / +2.9 /
  +2.0 / +2.2 dB (932 fixed further in the stem fix). **B #6** violas 892-900 26.3 -> 23.5 (Trumpet 1 28.0).
- **C #3 sfp 592**, first 0.1 s minus the ff before / peak time: Vln I -3.7 -> -0.8 dB, -0.02 -> 0.00 s; Vln II -0.9 -> +2.0,
  0.00 s; Vla -4.4 -> -1.6, +0.10 -> +0.09 s; Vc -7.4 -> +0.4, +0.27 -> +0.07 s; Cb -7.0 -> -2.2, +0.29 -> +0.08 s; master
  -2.7 -> -1.6 dB (peak still +0.26 s: the brass). The p after it unchanged (Vc -33.3 -> -32.9, others equal).
- **C #4** Horn 1 264-300 11.3 -> 15.3 (Violins I 24.7, celli 18.1). **C #5** bars 3-4 Vln I / Vln II / Vla / Vc 24.6 /
  23.0 / 22.9 / 24.4 -> 28.4 / 24.9 / 25.8 / 29.4; master half bars 9-16 +3.4..+3.9 dB. **C #6** Horn 3 560-564 18.7 ->
  14.7 (Oboe 1 19.1); 315 Hz hump (master third octave over the 250/400 mean, my measure) J 8.5 -> 8.4, P 5.3, R 5.5 ->
  5.2, whole 4.5: Horn 3's 552-564 was not the main source in J.
- **C #2** master bars 273-278 (K) 44.8 / 44.9 / 45.2 / 45.4 / 47.3 / 49.8 -> 45.1 / 45.2 / 45.5 / 45.9 / 47.6 / 49.8; Horns
  1 / 3 now rise 0.6 / 0.2 dB across 1096-1104 (were -0.5 / -1.2). mp3 bars 275-278 (plain RMS) -16.2 / -15.8 / -13.8 /
  -12.4 (c09 flat to 277); mp3 momentary max 278 -11.1 over 223 -11.6 (c09 278 -11.7 under 223 -11.5).
- **C #1** mp3 bar levels (plain RMS): bars 43 -> 48 now follow the master (+4.5 dB, master +4.1); bars
  42 -> 48 +4.4 dB (old rides +6.4, master +1.7); bar 42 sits 0.1 dB over 43 (master 2.4 dB over); the f -> p at 41 -> 42 6.5 dB (master 9.1, old
  rides 8.8); bassoon solo 114 -> 117 +6.4 -> +3.6 (master +2.9), no longer inverted.
- **Wetness** unchanged (returns untouched): final chord drop at +0.3 s 15.4 dB, -20 dB at 0.41 s (c09 the same).
- **Loudness**: master -20.3 LUFS, LRA 22.6 LU (render metrics 22.8 before the stem fix), true peak -0.2 dBFS, sample peak
  0.971; delivered -19.8 LUFS, LRA 15.0 LU, TP -1.7 dBTP, limiter about 1.5 dB, p10-to-max span 19.2 dB.
- **Attack probe**: 1 flag, Violoncellos qn 24 +0.43 s, the known build-shape artefact (c09 +0.42 s).

## REAPER
- Lock 11:36-12:13 (37 min), after Movement II's c47 (waited 11:13-11:36). Drive answered at every check.
- start, open (35 tracks), `--midi-only` of 18 tracks, restart, settle 11 min to 45 GB, audio device reopened (48 kHz, 512,
  no input), render with `--force-memory` (38 GB compressed) 11:52-12:03, stem fix written with `--mix-only`, save, quit.
- REAPER memory after the render: 45 GB, 34 GB compressed.
- Disk: c09 stem WAVs (render/, render_first/) deleted, c09 `render/00_Master.wav` kept; 53 GB free.

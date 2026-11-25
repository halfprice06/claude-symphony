# Cycle 23 changes (actor)

Snapshot of the c22 tools and data: `cycles/c23/before/`. All 32 tracks were updated with `build_reaper.py build/parts.json jobs --midi-only`; no Opus state changed, so no track was fully rebuilt. Then save, quit (the quit job timed out after 60 s, but REAPER exited), `-new` restart and `Main_openProject` (32 tracks, about 6 minutes). One render: 20 GB and 0 GB compressed at the start, 63 GB with 44 GB compressed during the render. Attack gate 19 of 21: Vln II and Vc at qn 212 dip 6.7 and 7.6 dB, the same values as c20-c22 (known threshold noise).

One post-render fix (gain only): the Violins I join at qn 73.5 played its transition spike 0.1 qn later than in c22 (73.48-73.53, +8 dB on the stem, about +4 dB on the master), outside the c21 notch, with the notes and envelope unchanged. `JOIN_NOTCH` Vln I (73.37, 73.45, -6.0) became (73.37, 73.55, -5.5). The envelope difference was applied to the Vln I stem and the master rebuilt as the stem sum (the sum matched the rendered master to 8e-7 before the change); REAPER got `--midi-only "Violins I"` and was saved. Metrics, attack probe and mp3 were regenerated. The first render's master, Vln I stem, metrics and mp3 are in `/private/tmp/claude-501/mockup-loop/c23-actor/render1/`.

## Accepted

### Critic A
- **A #1 violin unison joins** (`build/early_fills.json`, marked in `_auto` "c23 set by hand (critic A #1, unison sum)"): Vln I 65.5 3.5/0.26, 74 2.5/0.19, 84 3.0/0.35, 87 4.5/0.24, 240 4.0/0.30; Vln II 65.5 5.0/0.24, 74 5.0/0.23, 80 5.0/0.22, 84 4.0/0.23, 87 5.0/0.23, 240 4.5/0.13 (db/hold_s, pre_s 0). Vln I 80 stays at 2.0.
- **A #2 slow soft string entries**: entry fills (marked "c23 entry fill"): Violas 42 4.0/0.40, Double basses 140 4.0/0.40, Violins II 108 4.0/0.40, Violins II div 108 3.0/0.35, Violas div 277 4.0/0.30. Entry leads merged with C #1 (below).
- **A #3 `JOIN_NOTCH`**: Cor anglais (155.41, 155.57, -3.5), Violas (56.81, 56.93, -6.0), Oboe 1 (56.97, 57.04, -2.5), Violas div (83.82, 83.98, -4.5), Violin I solo (50.89, 50.93, -2.5).
- **A #4 `REP_RETONGUE_AT`** (new, `score_to_parts.py`): Horn 4 and Bass clarinet 9/12/15, Horn 3 292, Bassoon 2 23/235. The note before a listed untied repeat ends 0.06 qn early (was 0.03).
- **Routine `auto_fills.py 22`** on `cycles/c23/before/parts.json`: Flute 1 128 3.5 -> 2.3, Violoncellos 219 2.9 -> 1.6. Excluded (one `--exclude` per entry): the hand-set notes (Hn1 202, Ob1 143/145, Vc 256), the entries that flip on and off (Fl1 200, Vc 203/210, Cl1 178/266) and CA 132/134.

### Critic B
- **B #1 pp swells into the next layer** (`SWELL_CC_CAP`, new `"*"` key and `SWELL_CAP_MAX_CC` 40). I read the four patch files' CC11 rescaler tables: Bassoon "Bs f" 0.12 at CC 34, 0.37 at 36; Bass clarinet "BC mp" 0.09 at 30, 0.37 at 34; Contrabassoon "CB mp" 0.13 at 34, 0.35 at 36; Clarinet "Cl mp" 0.02 at 32, 0.32 at 36. All four have the crossfade at the printed pp/p, so Contrabassoon and Clarinet 2 got the rule too: `{"Bassoon 1": {"*": 0}, "Bassoon 2": {"*": 0, 46: 34}, "Bass clarinet": {"*": 0}, "Contrabassoon": {"*": 0}, "Clarinet 2": {"*": 0}}`. A swelling long note that starts at CC11 <= 40 keeps its starting CC; the volume-envelope swell (SWELL_DB) stays.
- **B #2 bar 78**: the ten `[258, 269, dB, 1]` low-octave rows in `roles.json` now start at 261.5.
- **B #3**: Violoncellos `[73.5, 78, -2]`, `[245.5, 250, -2]`.
- **B #4**: Clarinet 1 `[287.4, 289.0, 2.5]`.

### Critic C
- **C #1 + A #2 entry leads** (`build/entry_leads.json`): Violas 0 0.12, 42 0.15, 66 0.12, 238 0.08, 277 0.10; Double basses 140 0.15; Violins II 0 0.06, 108 0.12 -> 0.18; Violins II div 108 0.12 -> 0.18; Violas div 66 0.06, 277 0.12. The two critics disagreed on Vln II div 108 (A: body - 6 dB at +0.44 s; C: -0.05 s, proposing 0.06). The c22 stem trace (-60 dB at +0.5 s, body about -51 at +1 s) supports A, so I used A's value.
- **C #2**: Bassoon 1 entry leads 229 0.10, 196 0.06.
- **C #3 `SOST_JOIN_LEAD_S`** (new, 0.12 s): a wind note under the sostenuto that follows an overlapping re-tongued Sus note (sost_rep/sost_sus) is led and gets `SOST_VEL` 100. Only Oboe 1 210 matches (moved 0.108 qn; keyswitch at 209.862, before the moved note).
- **C #4 `build/leg_leads.json`**: Violins II 206 0.08, Violoncellos 255 0.08, Bassoon 1 100 0.08, Oboe 1 200 0.06.
- **C #5 `LEG_PAIR_EXTRA_S` Violas**: (60, 58) -0.10, (65, 64) -0.08, (52, 51) -0.08.

## Rejected or deferred
- None of the findings were rejected.
- B #5 (oboe entries at 42/54 with shorter trim ramps) not done: critic B left it to critic A, and A #2's viola entry fix changes the same onset.
- Open: Bassoon 2 B flat 2 at qn 140 still rises 7 dB at a flat CC 33 (the sample swells by itself); Bn2 146 rises 10 dB inside its printed crescendo. Try a role or a shaped pitch trim for Bn2 [140.5, 143] next.

## Measured (c22 -> c23)
- Master: -22.5 -> -22.5 LUFS, LRA 23.6 -> 23.7 LU, TP -3.9 -> -4.0 dBFS.
- mp3: -19.8 -> -19.8 LUFS, LRA 16.0 -> 16.0 LU, TP -1.6 -> -1.6 dBTP, span 18.5 -> 18.5 dB, limiter 1.8 -> 1.7 dB.
- A #1 (`vjoin23.py`, summed Vln I + II dip / master dip, dB): 65.5 6.4/6.1 -> 3.0/3.3; 74 5.1/1.2 -> 1.6/0.6; 80 7.1/4.0 -> 4.5/3.3; 84 5.3/2.7 -> 3.3/2.4; 87 7.2/3.8 -> 2.5/3.0; 240 4.9/3.9 -> 2.9/2.6. Joins with a sum dip of 5 dB or more: 8 -> 3.
- A #2 / C #1 / C #2 (`slowent.py`, body - 6 dB after the score onset, s): Violas 42 +0.65 -> +0.11; Cb 140 +0.61 -> +0.31; Vln II 108 +0.54 -> +0.27; Vln II div 108 +0.44 -> under +0.11; Violas div 277 +0.56 -> under +0.11; Violas 0 +0.39 -> +0.26; Violas 66 +0.29 -> +0.18; Violas 277 +0.27 -> +0.19; Bn1 229 +0.23 -> under +0.11. Median over 82 entries 0.07 -> 0.05. No entry overshoots its body in the first 1.8 s.
- A #3 (`pk23.py`, stem peak over reference): CA 155.5 +5.6 -> +2.2, Violas 57 +8.2 -> -0.2, Ob1 57 +4.6 -> +2.1, Vla div 84 +6.7 -> +2.8, solo violin 51 +4.7 -> +2.2. Master bumps +4.0..+4.7 -> +0.7..+2.3.
- A #4 (`rep23.py`, dip at the repeat): Bn2 23 1.4 -> 3.5, Bn2 235 -0.7 -> 5.8, BCl 9/12/15 -2.2 -> 2.2..2.4, Hn4 9/12/15 0.4-0.8 -> 1.5-2.3, Hn3 292 0.1 -> 1.1. The horns stay under the 2.5 dB target: their release tails fill a 70 ms gap.
- B #1 (pp long notes in Bn1/Bn2/BCl/Cbn/Cl2 starting at CC <= 40, peak over the 30-100% section minus the early body): median +3.3 -> +1.2 dB over 50 notes. Bn1 24 +3.7 -> +1.0, Bn2 90 +6.7 -> +2.1, Bn2 232 +6.3 -> +4.1, Cbn 87 +3.3 -> +0.3, BCl 24 +4.8 -> +2.6. Bn2 140 +9.6 -> +7.3 (3-4 dB lower against the oboe solo at qn 141.75; still open).
- B #2 (Bn2 minus Vln I, stereo power, bar 78): +1.9/-1.3/-2.4/-0.6 -> -2.1/-5.3/-6.4/-4.6 dB on beats 259-260.5; Cb minus Vln I 3-4 dB lower. Master bar 78 about 1 dB lower; bar 79 unchanged.
- B #3 (Vc minus Vln I + II): qn 74-77 -1.3/-0.7/-2.4/-2.5 -> -4.5/-2.7/-4.4/-4.4; qn 246-249 +0.3/-1.2/-2.0/-0.3 -> -1.7/-3.2/-4.1/-2.4.
- B #4 (Cl1 minus Horn 4 / Violas at qn 288, 288.5): -1.0/-0.7 -> +1.5/+1.8; +1.7/-1.1 -> +4.2/+1.4.
- C #3/C #4/C #5 (crossover / rise, s): Ob1 210 +0.123/+0.305 -> -0.057/+0.095; Vln II 206 +0.103/+0.29 -> +0.028/+0.21; Vc 255 +0.168/+0.185 -> -0.017/+0.05; Bn1 100 +0.133/+0.225 -> +0.053/+0.14; Ob1 200 +0.108/+0.17 -> +0.073/+0.15; Violas falling steps 47/59/70/75/56/292 -0.07..-0.14 -> -0.04..+0.03 (crossover). The rising C4 join at 58 is unchanged (-0.032).
- Spike scan (`spikescan.py 5`, after the post-render fix): 37 -> 35 joins; Violas 57/72, Vla div 84, Vln I 244 and Vln II 208 left the list. New: Vln I 74 (+5.5 stem, +3.4 master) and Vln I 240 (+5.6, +2.7), both on their new A #1 fills, and Violas 292 (+5). Lower those two fills or notch them next cycle.

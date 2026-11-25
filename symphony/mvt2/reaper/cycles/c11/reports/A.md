# Cycle 11, critic A: articulation and phrasing (on the cycle 10 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c11-A/` (the c10 set, which defaults to cycle 10, plus new ones):
- `holes.py`: every legato join at or above `TH` dB. It reports the articulation, velocity and CC11, the dip, the time of the minimum relative to the score onset, the span that is 3 dB or more under the reference, any existing early fill, and the lead. It uses 10 ms frames smoothed over 40 ms.
- `bump.py`: for soft string joins, the hole and the level after the transition minus the level before it.
- `shp.py`: 50 ms level shapes from -0.4 to +1.4 s around an onset.
- `slurart2.py`: slurred notes that are not on a legato articulation.
- `acc2.py`: Trombone 1 accent attacks against the note body and against the mix.

Run them with `~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c10 stems (`render/`, after the solo gain fix). Onsets are score onsets (`sq`). build/parts.json (14:38) is the data that made this render.

## Checked and working (measured)

- **Chords:** no chord goes to a monophonic legato patch (`chords_leg.py`).
- **Slurs:** every slurred single-line note plays a legato articulation (`slurart2.py`). The exceptions are intended:
  - Ob1 208 and CA 157: Largamente/portato Sus.
  - The Vla sextuplets at 196-201: short_sus.
  - The Vc div. at 51-52 and 63-65: Sus MAX.
- **Keyswitches:** `ks_clash` is empty on every track. One keyswitch lands under 20 ms before its note (Ob1 207.952, 13 ms, the portato Sus switch). Leave it.
- **Harp harmonics:** they sound at the written octave plus 8va. Spectral peaks: key 63 -> 311 Hz, 65 -> 347, 68 -> 414, 72 -> 521.
- **Violin I solo track:** 9 joins, median dip 2.0 dB, none of 6 dB or more. Bodies are even (-44 to -49 in 50 ms frames at 49.5, 51 and 61). The release at qn 54 falls 16 dB in 0.35 s.
- **Mutes:** the drive has no con sordino horn. Solo French Horn/05 Mutes and 2 French Horns/05 Mutes hold only Stop (stopped-horn) patches, which have a different sound, so `mute_eq` remains the right tool for Horns 3-4 from bar 87.
- **Bass trombone:** D2 (qn 218) sounds (third partial at 220 Hz) and follows the printed decrescendo to p.

## 1. Soft string bow-change joins: the `bcsoft` CC11 dip sits inside the transition sag and makes 7-10 dB holes about 0.5 s long (Vc, Vla and Vln II, bars 16-21 and 46-51)

**Where:** Leg BC MAX targets at pp (CC11 34-39), v124:
- Violoncellos 48, 50, 156, 157, 160, 162: the pp unslurred bass line under the cor anglais "solo, espr." in bars 48-51, and bars 16-17.
- Violas 56, 60, 146, 160.
- Violins II 63, 152, 164.

**Measured (`holes.py`, `shp.py`):**

| Track | qn | dip (dB) | minimum at |
|---|---|---|---|
| Vc | 157 | 10.0 | +0.33 s |
| Vc | 162 | 9.3 | +0.32 s |
| Vc | 156 | 8.9 | 0.00 s |
| Vc | 160 | 7.5 | +0.39 s |
| Vc | 48 | 7.5 | +0.25 s |
| Vla | 60 | 10.0 | +0.18 s |
| Vla | 160 | 10.0 | +0.02 s |
| Vla | 146 | 9.8 | +0.12 s |
| Vla | 56 | 8.6 | +0.02 s |
| Vln II | 164 | 9.7 | +0.31 s |
| Vln II | 63 | 7.5 | |
| Vln II | 152 | 7.4 | |

The 50 ms shape of Vc qn 157:

| Time from onset | Level (dB) |
|---|---|
| before the onset | -47 to -48 |
| 0 to +0.15 s | -52 to -56 |
| +0.15 to +0.5 s | -56 to -60 |
| +0.8 s | -50 |
| +0.9 to +1.0 s | -46/-47 |

Vc 162 has the same shape.

By articulation, for soft joins (CC11 at or under 40), median dip:

| Section | Leg BC MAX | Leg Slur MAX |
|---|---|---|
| Violas | 5.6 dB (n 13) | 3.4 dB (n 73) |
| Violins II | 5.8 dB (n 14) | 4.7 dB (n 4) |
| Violoncellos | 5.2 dB (n 18) | |

Ten of the worst twelve targets carry `bcsoft`, because they are longer than 1.4 s:
- CC11 34 -> 28 at +0.125 qn, held, then back to 34 at +0.625 qn and on to 37-38 at +0.75 qn (Vc 157, 160, 162; Vln II 152, 164; Vla 60, 160).
- Six CC11 steps at CC 28-34 is about 3.5 dB (LEARNINGS: 5.7 dB per 10 CC below CC 40).
- The dip spans +0.15 to +0.5 s, which is where the Leg BC transition already sags. The bump it was meant to remove comes later, at +0.45 to +0.9 s (Vc 156, which has no bcsoft: -56 at 0 s, then -44/-45 at +0.45..+0.6 s).

This explains the c07 learning that bcsoft "cut the bump by only about 1-1.5 dB" (inferred): its timing is wrong, and it deepens the hole instead.

**What a listener hears (inferred):** in bars 48-51 the cello bass line under the cor anglais solo drops out for half a second on every note and then swells back. That reads as a pulse in the accompaniment, not as quiet bow changes. The same happens in the violas and Violins II in bars 19-21, under the solo violin.

**Fix (`tools/score_to_parts.py`):**
1. Generalise the c08 `VLA_BC_SOFT` rule to all three sections, with no length limit:
   - `BC_SOFT = {"tracks": ("Violins II", "Violas", "Violoncellos"), "max_s": 99, "max_cc": 52, "notch": 6}`.
   - In the Leg BC block (around line 677), replace `tname == "Violas"` with `tname in BC_SOFT["tracks"]`, and test `max_s` against the new value.
   - Those joins then stay Leg Slur MAX (overlapped, `bc_from`) with a bow-change CC11 notch. c08 measured this on the violas: median join dip 10.2 -> 6.2 dB.
   - Use notch 6 rather than 8, because at CC 34 one CC step is about 0.57 dB.
2. Set `BCSOFT["depth"]` to 0. After step 1 there are no soft Leg BC targets left for it to act on, so this only guards against it coming back.
3. Do not add early fills to these notes before re-measuring. The existing fills (Vln II 59/60, Vc 77/86, Vla 244/254.5) stay.

**Check:**
- `TH=6 holes.py "Violoncellos,Violas,Violins II"`: these 12 joins are 5 dB or less, and no new join of 7 dB or more appears in the same bars.
- `bump.py`: the soft-join "after minus before" median for each section stays within +2.5 dB, with no join over +5.
- The bars 48-51 cello line (qn 152-166) has a p10-p90 spread in 50 ms frames under 6 dB. It is about 12 dB now.

## 2. Wind, horn and tune joins whose hole lasts longer than the early fill's 0.10 s hold

**Where and measured (`holes.py`; the dip is post-envelope, the "hole" is the span 3 dB or more under the reference):**

| Track | qn (bar) | step | dip | hole | existing fill |
|---|---|---|---|---|---|
| Bassoon 1 | 231 (68.7) | 58->56 v60 | 10.8 | 0.00..+0.49 s, min +0.35 | note trim +4 only |
| Violins I | 71 (24.7) | 74->73 v124 | 8.9 | +0.05..+0.46, min +0.09 | none |
| Cor anglais | 129.5 (42.4) | 70->68 v90 | 9.4 | -0.03..+0.12 | 5 |
| Violins II | 65 (22.7) | 58->63 v124, cc58 | 8.7 | -0.08..+0.14 | none |
| Oboe 1 | 142.5 (45.6) | 75->73 v80 | 8.3 | +0.02..+0.33 | none |
| Horn 1 | 203 (60.75) | 66->65 v124 | 8.2 | -0.03..+0.49, min +0.42 | {4, pre 0.10} |
| Clarinet 1 | 184 (56.0) | 65->60 v60 | 8.1 | +0.01..+0.21 | none |
| Violas | 251.5 (75.5) | 68->63 v124 | 8.1 | -0.02..+0.19 | none |
| Violins II | 66 (23.0) | 65->68 v124 | 8.0 | -0.04..+0.47 | none |
| Bassoon 1 | 262 / 269 | +1 / +3, v60 | 7.9 / 7.9 | -0.03..+0.04 / +0.20..+0.33 | none |
| Violins I | 80 (27.7) | 72->77 Leg BC | 7.7 | +0.13..+0.24 | none |
| Cor anglais | 168 (52.0) | 66->65 v80 | 7.7 | +0.03..+0.27 | none |
| Clarinet 1 | 186 (56.5) | 60->61 v60 | 7.2 | +0.05..+0.42 | none |
| Violins I | 86 (29.7) | 73->72 | 7.1 | +0.14..+0.39 | none |

**Shapes (`shp.py`, 50 ms frames):**
- Bn1 231: -49 before; -52..-61 from 0 to +0.45 s; -46 from +0.55 s. The +4 note trim (0.6 s ramp) lifts the body 3 dB over the preceding note, but it does not reach the hole.
- Hn1 203: -31 before; -37 at -0.05 s; -41 at +0.4 s; -32 at +0.55 s. The c10 fill is held only to +0.10 s, so most of the hole remains (c10 measured 7.3 dB; this metric gives 8.2).

**Excluded:** all Flute 1 and Flute 2 joins. On held flute notes the 50 ms frames swing 4-8 dB from vibrato AM (Fl1 192: -37 to -49 inside one note), so a join dip of 6-11 dB there is not a hole.

**Inferred:** Vln I qn 71 and 80-86 are inside the "tutti, espr., sul D" tune (bars 23-29). Bn1 231 is the bassoon's solo phrase in bar 68, and Hn1 203 is the horn line into the bar 61 climax. Each sounds like a note that speaks late.

**Fix:**

1. `score_to_parts.py`, early-fill block: accept an optional `hold_s` (default 0.10, the current value). The fill holds +db to `sq + hold_s` and is back to 0 by `sq + hold_s + 0.25`. Write all four breakpoints into `vol_bp`.

2. `build/early_fills.json` (dB = dip - 3, capped at 7; hold = end of the hole - 0.05 s):

   | Track | qn | value |
   |---|---|---|
   | Bassoon 1 | 231 | `{"db": 7, "pre_s": 0, "hold_s": 0.40}` |
   | Bassoon 1 | 262 | `5` |
   | Bassoon 1 | 269 | `{"db": 5, "pre_s": 0, "hold_s": 0.28}` |
   | Horn 1 | 203 | `{"db": 5, "pre_s": 0.10, "hold_s": 0.42}` |
   | Violins I | 71 | `{"db": 5, "pre_s": 0, "hold_s": 0.40}` |
   | Violins I | 80 | `{"db": 4, "pre_s": 0, "hold_s": 0.20}` |
   | Violins I | 86 | `{"db": 4, "pre_s": 0, "hold_s": 0.35}` |
   | Violins II | 65 | `{"db": 5, "pre_s": 0.06}` |
   | Violins II | 66 | `{"db": 5, "pre_s": 0.02, "hold_s": 0.40}` |
   | Cor anglais | 129.5 | `5` -> `{"db": 7, "pre_s": 0.03}` |
   | Cor anglais | 168 | `{"db": 4, "pre_s": 0, "hold_s": 0.22}` |
   | Oboe 1 | 142.5 | `{"db": 5, "pre_s": 0, "hold_s": 0.28}` |
   | Clarinet 1 | 184 | `{"db": 5, "pre_s": 0, "hold_s": 0.16}` |
   | Clarinet 1 | 186 | `{"db": 4, "pre_s": 0, "hold_s": 0.37}` |
   | Violas | 251.5 | `{"db": 5, "pre_s": 0.02, "hold_s": 0.14}` |

3. `build/note_trims.json`: Bassoon 1 `"231"` 4 -> 1.

These are level-only changes. Simulate them on the c10 stems with the actor's `sim.py` before rendering.

**Check:**
- `TH=6 holes.py "Bassoon 1,Violins I,Violins II,Cor anglais,Oboe 1,Horn 1,Clarinet 1,Violas"`: each listed join is 5 dB or less.
- `shp.py` shows no frame from -0.2 to +0.7 s more than 2 dB over the following body.

## 3. Trombone 1's marcato pickup has no weight, and the bar 63 accent barely registers (bars 62-63, qn 212.5-218)

**Score:** Tbn1 enters ff "marcato" on the qn 212.5 pickup with an accent. There are further accents on 213 and 218, and 218 starts a decrescendo to mf/p.

**Measured (`acc2.py`):**

| qn | 0-120 ms vs note body | Tbn1 minus master, 0-150 ms |
|---|---|---|
| 212.5 | -1.7 dB | -5.4 dB |
| 213 | -0.3 dB | -2.7 dB |
| 218 | +3.0 dB | -0.8 dB |
| unaccented 214.5-217.5 | | -0.5 to -2.0 dB |

- In 50 ms frames, 212.5 rises -38, -32, -29, -28 and then stays flat at -26/-27. Nothing in the attack is over the body.
- Against the previous note, 213 is +2 to +3 dB and 218 is +1 to +2 dB.
- The accented pickup is the note that sits furthest under the mix, because the strings' sf tremolo chord at 212 sounds through it.
- c10 lowered 212.5/213 from v121 to v108/105 to remove 19-21 dB peaks. That was right, but it took the emphasis with it. The ACCENT_DB envelope (+2 dB from 212.5 to 212.75) covers half of a 0.5 qn note, so attack and body rise together.

Dan's rule is 2-4 dB of weight with no hard transient.

**Fix (`score_to_parts.py`):**
- Add a per-onset accent override, `ACCENT_DB_AT = {"Trombone 1": {212.5: 4.0, 218.0: 3.0}}`, applied with the timpani loud-attack shape: a 10 ms rise, held 0.12 qn, back to the base by 0.3 qn, written into `vol_bp`.
- Keep v108/105/110 (no new peak from velocity).
- On 212.5 the shape decays before 213, so 213 keeps its own +2.

**Check:**
- At 212.5, Tbn1 minus master over 0-150 ms is -2 dB or higher, and the attack is 2-4 dB over the 0.15-0.4 s body.
- At 218, the attack is 3-4 dB over the 217.5 note.
- The master's peak over qn 212-219 does not rise more than 1 dB over c10's.

## 4. Still no portamento on the "sul D / sul A" leaps (deferred in c10)

**Measured (data):** no note in parts.json uses Leg Port MAX (1st Violins key 49, 2nd Violins 46, Celli 89). The candidate leaps are unchanged from c10 A #3:
- Vln I and Vln II qn 82: F5 -> B flat 5, at the top of the "espr., sul D" phrase.
- Vln I qn 172: C5 -> F5, the "senza sord., sul A" entry. In parts.json the C5 at 171 is v53 and the F5 at 172 is v124.
- Vc qn 83: A flat 3 -> D flat 4, in the cantabile.

HO's True Legato sets the transition speed from velocity: 110-127 is shortest, 50-60 longer (manual, Performance Scripts, "TRUE LEGATO"). Every string join is v124, so even the widest espressivo leaps change pitch in the shortest transition the library has.

**Inferred:** a one-string leap in a Romantic Adagio is played with an audible shift. Exactly these 3-4 notes are where the mockup sounds like a sampler rather than a section.

**Fix (cheaper than the c10 plan, one track first):**
1. Add `PORT_TARGETS = {"Violins I": [82.0, 172.0]}` in `score_to_parts.py`. Before each target, send the Leg Port MAX keyswitch at the place the Leg Slur/Leg BC switches go now (while the previous note is held). After the target's moved onset, switch back to the slur's articulation. Target velocity 100.
2. Rebuild only Violins I (one patch reload, so the Leg Port row loads), restart REAPER, and render. Also export a short range (qn 78-90 and 168-176) for the f0 check.
3. If the glide measures 0.08-0.25 s, add Vln II 82 and Vc 83 in the next cycle. If it is longer than 0.3 s, set the target velocity to 115 before reaching for CC5.

**Check:**
- An STFT peak track on the Vln I stem shows a continuous 698 -> 932 Hz glide at qn 82 and a 523 -> 698 Hz glide at 172, each lasting 0.08-0.25 s.
- Their `holes.py` dips are no worse than now (Vln I 82: under 6 dB now).

## 5. Violin I solo: every join is the fastest transition (v124), while the solo has the most headroom for a slower one (inferred, low cost)

**Measured:**
- The solo track's joins (qn 48.5-63) are all v124.
- Their median dip is 2.0 dB, the lowest of any legato track, and none is 6 dB or more.
- The section tracks need v124 because slower transitions dipped there (c03). The DIV A solo patch measures much smoother.

**Inferred:** a "solo" line over the oboe in bars 17-22 is where a real player connects notes most vocally. HO says v50-60 "allowing the melody to breathe", and v124 gives every step the same quick change.

**Fix:**
- `score_to_parts.py` `VEL_SET` (or a per-track legato velocity): Violin I solo legato targets v124 -> 96.
- Keep the leads. The transition is longer, so add 0.03 s to the solo's legato lead (`LEG_LEAD_S` key "Violin I solo": 0.20).

**Check:**
- Solo join dips stay at or under 4 dB.
- Each target's body arrives within 0.1 s of `sq`.
- The crossover (old note -10 dB, new note within 3 dB of its body) lasts 0.10-0.18 s, against about 0.05-0.08 s now.

## Do not touch

- The slur-scoped legato with overlaps, and no chords on legato patches.
- The keyswitch placement in the preceding note or rest.
- The Violin I solo track, its window, its gain and its smooth joins.
- The c08-c10 early fills (Vln II 59/60, Vc 77/86, Vla 244/245.5/254.5, Cl1 266, CA 132/133.5, Ob1 270/271).
- VLA_BC_SOFT's Leg Slur + notch idea, which finding 1 extends.
- The same-pitch merges with notches; the tie handling; the tremolo at bars 61-64.
- The harp harmonics octave and the harp rolls; the timpani roll table, the settle and `TIMP_LOUD_ATTACK_DB` 6.
- Tbn1 v108/105/110 and the sf cut on the sf.
- `mute_eq` for Horns 3-4 (no con sordino horn patch exists on the drive).

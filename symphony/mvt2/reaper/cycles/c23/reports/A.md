# Cycle 23, critic A: articulation and phrasing (on the cycle 22 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c23-A/`: the c22-A set, plus these new ones:
- `slowent.py`: soft sustained entries, measuring the time from the score onset until the stem reaches body -6 dB and body -3 dB. It also groups entries that start together.
- `simfill23.py`: simulates an extra entry lead plus an entry fill on a stem.
- `vjoin23.py`: legato-join dips in Violins I, Violins II, their sum and the master, for the theme spans.
- `vsim23.py`: simulates violin fills on the summed unison.
- `pk23.py`: join transients.
- `rep23.py`: dips at repeated-pitch re-articulations.
- `af/tools/af.py`: a copy of `auto_fills.py` with Violins I, Violins II and Violas added to `TRACKS`. It was run in plan mode only.

Run them with `CYC=22 ~/.venvs/claude-composes-reaper/bin/python`. Levels are stereo power on the c22 stems, and onsets are score onsets (`sq`).

Delivery numbers, from `metrics.md` (not re-measured):
- Master: -22.5 LUFS, LRA 23.6 LU, TP -3.9 dBFS.
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.5 dB, limiter 1.8 dB.

None of the fixes below changes these numbers by more than about 0.1 LU (inferred: short, local level changes).

## Checked and working (measured, c22)

- **Keyswitches, chords and ties.**
  - Every keyswitch is at least 20 ms ahead of its note, except the known Ob1 207.952 (13 ms).
  - No chord goes to a legato patch.
  - All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
- **c22 pull fix.**
  - `ccorder.py` lists only legato targets with overlap=True, which is by design.
  - No CC11 is out of order at a moved note-on.
- **Legato timing.** Crossover medians are -0.01..+0.06 s on every legato track (`leg.py`).
- **Phrase ends.** Tapers and releases are unchanged (`ends.py`).
- **Bar 63 strings.** The sf > to p in bar 63 has an sf peak 8-12 dB over the bar's end, then a steady fall.

## 1. The violin theme loses notes at legato joins: the summed Vln I + Vln II unison dips 5-7 dB at six joins. The pickup F at bar 22 drops the whole master 6 dB. Measured; the fix is simulated

**Where:** Violins I and Violins II in unison. This is the a' theme, bars 22.67-30 (qn 65-90, "tutti, espr., sul D"), and the reprise at bar 71.67 (qn 240).

**What is wrong.** `auto_fills.py` measures only Flute 1, Oboe 1, Cor anglais, Clarinet 1, Bass clarinet, Horn 1, the solo violin and the celli. The violins carry the main theme twice, and their joins were only hand-filled (Vln I 68/71/80/86, Vln II 65/66). Neither section fills the other's dips: at the worst joins, both sections sag together.

`vjoin23.py` measures the dip on a 30 ms window. The reference is the lower of the previous note's body and the target's body.

| join (qn, bar) | Vln I | Vln II | Vln I + II sum | master |
|---|---|---|---|---|
| 65.5 (22.83), the pickup F4 of the tutti entry | 5.5 | 7.3 | 6.4 | **6.1** |
| 74 (25.67) | 5.4 | 7.1 | 5.1 | 1.2 |
| 80 (27.67) | 5.7 | 10.5 | 7.1 | 4.0 |
| 84 (29.00) | 5.4 | 6.7 | 5.3 | 2.7 |
| 87 (30.00), the cadence | 7.5 | 6.3 | 7.2 | 3.8 |
| 240 (71.67) | 6.8 | 7.3 | 4.9 | 3.9 |

- Over these spans, the median sum dip is 3.6 dB across 52 joins.
- At qn 65.5, the master per 0.08 qn reads -34.4, -39.5, **-43.1**, -38.2, -34.0. The E flat-F-A flat pickup that opens the theme reads loud, then a hole, then loud.
- The af.py plan proposes fills for the same joins, from its single-section dips: Vln I 65.5 6.3, 87 7.8, 240 7.5; Vln II 65.5 8.4, 74 9.2, 80 10.3, 87 8.0.

**Fix.** Add these entries to `build/early_fills.json` (score-onset keys). In each track's `_auto`, list them as "c23 set by hand (unison sum); auto_fills does not scan violins".

- "Violins I":
  - "65.5": {"db": 3.5, "pre_s": 0, "hold_s": 0.26}
  - "74": {"db": 2.5, "pre_s": 0, "hold_s": 0.19}
  - "84": {"db": 3.0, "pre_s": 0, "hold_s": 0.35}
  - "87": {"db": 4.5, "pre_s": 0, "hold_s": 0.24}
  - "240": {"db": 4.0, "pre_s": 0, "hold_s": 0.30}
- "Violins II":
  - "65.5": {"db": 5.0, "pre_s": 0, "hold_s": 0.24}
  - "74": {"db": 5.0, "pre_s": 0, "hold_s": 0.23}
  - "80": {"db": 5.0, "pre_s": 0, "hold_s": 0.22}
  - "84": {"db": 4.0, "pre_s": 0, "hold_s": 0.23}
  - "87": {"db": 5.0, "pre_s": 0, "hold_s": 0.23}
  - "240": {"db": 4.5, "pre_s": 0, "hold_s": 0.13}

This is a level-only change (`--midi-only`). Leave Vln I 80 at its hand-set 2.0.

**Simulated on the c22 stems** (`vsim23.py`, the fill shape from `score_to_parts.py`):

| join | sum dip before | sum dip after | 200 ms overshoot over the louder body |
|---|---|---|---|
| 65.5 | 6.4 | 2.6 | unchanged, +2.1 |
| 74 | 5.1 | 1.8 | unchanged |
| 80 | 7.1 | 4.5 | unchanged |
| 84 | 5.3 | 3.5 | -0.7 -> 0.0 |
| 87 | 7.2 | 2.5 | unchanged |
| 240 | 4.9 | 2.4 | unchanged |

**Check:**
- `vjoin23.py` on c23: sum dips at most 4 dB at these joins, and master at most 3 dB at 65.5.
- `spikescan.py 5` adds no new Vln I or Vln II entries at these onsets.

## 2. Soft string entries in chords bloom 0.4-0.5 s after the instruments entering with them. Measured; the fix is simulated

**Where:** pp chord entries after rests. The Opus sustain layers at CC11 22-46 have slow bow onsets.

`slowent.py` gives the time after the score onset at which each stem reaches body -6 dB. The body is the median over +0.8..+1.6 s.

| qn (bar), printed | late voice | partners entering on the same beat |
|---|---|---|
| 42 (15), pp con sord. | Violas **+0.65** (body -3 dB at +0.84) | Vc +0.12, Ob1 +0.13, Vln II +0.15 |
| 108 (37), pp sul tasto, "D" | Vln II **+0.54**, Vln II div +0.44 | Bn1 +0.02, Fl1 +0.07 (the new theme) |
| 140 (45), pp arco, "E" | Double basses **+0.61** | Vla +0.12, Bn2 +0.19, Vln II +0.23 |
| 277 (84), ppp | Violas div **+0.56** | Violas +0.27 |

Of the 70 sustained entries, the median is +0.10 s.

- At qn 42, the viola stem rises 18 dB over the first second: -64.8 at the onset, -48 at +0.9 s. The score prints no hairpin.
- At qn 140, the basses rise 15 dB in 0.8 s under a pp chord that is already sounding.
- The listener hears the inner voice (or the bass) fade in half a beat after the chord starts. That is an unprinted crescendo, and it smears the entry. Inferred: at 52-60 bpm, 0.5 s is about half a beat.

**Fix.** The family entry lead is 0.12 s (`ENTRY_LEAD_S`), with `ENTRY_CAP_S` 0.30.

- `build/entry_leads.json`:
  - "Violas": add "42": 0.15.
  - "Double basses": add "140": 0.15.
  - "Violins II": "108" 0.12 -> 0.18.
  - "Violins II div": "108" 0.12 -> 0.18.
  - "Violas div": add "277": 0.12.
- `build/early_fills.json` (entry fills; the dict form works on any note at that onset). Mark them in `_auto` as "c23 entry fill (set by hand)".
  - "Violas" "42": {"db": 4.0, "pre_s": 0, "hold_s": 0.40}
  - "Double basses" "140": {"db": 4.0, "pre_s": 0, "hold_s": 0.40}
  - "Violins II" "108": {"db": 4.0, "pre_s": 0, "hold_s": 0.40}
  - "Violins II div" "108": {"db": 3.0, "pre_s": 0, "hold_s": 0.35}
  - "Violas div" "277": {"db": 4.0, "pre_s": 0, "hold_s": 0.30}

**Simulated** (`simfill23.py`, stem time-shifted by the extra lead, plus the fill):

| entry | t-6 before | t-6 after | 0.8 s peak over body after | -20 dB point after |
|---|---|---|---|---|
| Violas 42 | +0.65 | +0.10 | -1.8 dB | -0.23 s |
| Cb 140 | +0.61 | +0.28 | +0.5 dB | -0.29 s |
| Vln II 108 | +0.54 | +0.26 | +0.1 dB | |
| Vln II div 108 | +0.44 | +0.02 | 0 dB | |
| Violas div 277 | +0.57 | +0.03 | -0.9 dB | |

- No entry overshoots its body.
- The first audible sound (body -20 dB) moves 0.12-0.18 s earlier. It sits 25 dB or more under the mix, so it is not heard as early (inferred).

**Check:**
- `slowent.py` on c23: these five entries at t-6 of +0.30 s or less.
- No 0.8 s peak more than 1.5 dB over the body.
- `probe_attacks.py` Vln II 42 start is unchanged.

## 3. Unwritten accents at joins in exposed solo lines. Measured, repeated in c21 and c22

`pk23.py` measures the stem peak over the louder of pre (-0.45..-0.2 s) and post (+0.2..+0.6 s), and how long the stem stays more than 2 dB over that reference. `mbumps.py 2.5` gives the master rise.

| track, onset (bar) | stem peak | span over ref +2 (qn) | master | note |
|---|---|---|---|---|
| Cor anglais 155.5 (48.88), "solo, espr." p, mid-bar eighths, no hairpin | +5.6 | 155.416-155.569 (170 ms) | +4.7 | c21 +4.5 |
| Violas 57 (20.0), pp under the oboe | +8.2 | 56.819-56.927 | +4.6, shared with the oboe | BC_SOFT join |
| Oboe 1 57 (20.0) | +4.6 | 56.979-57.031 | +4.6 | coincides with the 6.9 dB auto fill's onset. The 200 ms overshoot rule cannot see a 50 ms peak (c21 note) |
| Violas div 84 (29.0) | +6.7 | 83.824-83.977 (170 ms) | +2.1 | |
| Violin I solo 51 (18.0) | +4.7 | 50.890-50.925 | +4.0 | c21 +4.2 |

**Fix:** `tools/score_to_parts.py` `JOIN_NOTCH`. The depth is the spike minus 2, as in c21/c22.
- "Cor anglais": add [(155.41, 155.57, -3.5)] (new key).
- "Violas": add (56.81, 56.93, -6.0).
- "Oboe 1": add (56.97, 57.04, -2.5). Keep the fill.
- "Violas div": add [(83.82, 83.98, -4.5)] (new key).
- "Violin I solo": add (50.89, 50.93, -2.5).

**Check:**
- `pk23.py` on c23: each at +3 dB or less.
- `mbumps.py 2.5`: CA 155.5, Ob1/Vla 57 and solo 51 drop off the list.
- `joins.py`: no new 6 dB dips there.

## 4. Untied repeated pp notes in horns and low reeds are not re-articulated. Dips measured; the fix effect is inferred

**Where:**
- Intro bars 4-6 (qn 9, 12, 15): Horn 4 and bass clarinet `aes2. | aes2. | aes2.`, untied, pp.
- Coda bar 89 (qn 292): Horn 3 con sord. `aes2.` repeated.
- Bassoon 2, qn 23 (bar 8.67) and 235 (bar 70).

**What is wrong.** Non-legato same-pitch notes end 0.03 qn (about 35 ms) early (`build_track`, the `elif same_pitch:` branch). Release tails and the hall fill that gap, so the repeat makes no audible break (`rep23.py`, dip under the louder neighbour):
- Hn4 9/12/15: 0.4/0.8/0.6 dB.
- BCl 9/12/15: none. The new note starts 2 dB under the old note's end.
- Hn3 292: 0.1 dB.
- Bn2 23/235: 1.4/-0.7 dB.

In the score these are separate notes, which wind players re-tongue. The listener hears one held pedal instead of the soft bar-line pulse the notation asks for (inferred).

For comparison, same-pitch legato-row repeats end 0.06 qn early and dip 3.8-5.4 dB: CA 96 5.4, Bn1 96 4.0, Ob1 148 3.8 (measured).

**Fix** (`tools/score_to_parts.py`).
- New table: `REP_RETONGUE_AT = {"Horn 4": [9.0, 12.0, 15.0], "Bass clarinet": [9.0, 12.0, 15.0], "Horn 3": [292.0], "Bassoon 2": [23.0, 235.0]}`.
- In the `elif same_pitch:` branch, when `nxt[0]["qn"]` is within 0.02 of a listed onset, use `n["end"] = e0 - min(0.06, 0.15 * dur)`, the legato-repeat value.
- It is a `--midi-only` change.
- Expected: 3-5 dB dips (inferred from the legato repeats above).

**Check:**
- `rep23.py` on c23: listed repeats dip 2.5-6 dB.
- Body levels within 1 dB of c22.

## Not findings, checked

- **The opening chord** (qn 0) blooms over 0.5 s: Vln I t-6 +0.55, Violas +0.39, Hn3 +0.04. It is the tie-over from movement I, but as the first sound of a separately played movement a short fade-in is acceptable. Not proposed.
- **Viola sextuplets, bars 59-60, slurred but on Sus MAX.** These stay as they are: Leg Slur, Detache and Stac Leg all failed in c14-c16.
- **Patches.** Nothing better is on the drive for this lens.
  - No muted horn: Solo/2 French Horns have only stopped-horn rows.
  - No solo violin library.
  - "2 Trombones and 1 Bass Trombone" is a three-player ensemble.
- **Legato velocity.** v124 against v50-60 does not move HO string crossovers (LEARNINGS), and timing is on target. Not proposed.

**Do not touch:** the c22 pull pad and its removed compensations; the c21/c22 `JOIN_NOTCH` entries and hand-lowered fills (including Vln I 80 at 2.0 and Ob1 57/145); `ENTRY_LEAD_S` family values and `ENTRY_CAP_S`; `LEG_CAP_FRAC`, leg_leads, pair leads, `ABUT_LEAD`, `slur_out`, `BC_SOFT`/`BC_SOFT_SKIP`; Vln II Flautando joins (`FLAUT_*`); tie handling, keyswitch placement, CC15/`mute_eq`, pizz. and harp steps, timpani tie strokes, caesura breaths, the Tbn1 marcato and accents.

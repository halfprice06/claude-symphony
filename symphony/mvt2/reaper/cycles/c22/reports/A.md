# Cycle 22, critic A: articulation and phrasing (on the cycle 21 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c22-A/`: the c21-A set, plus these new ones:
- `ccorder.py`: notes whose moved note-on comes before the controller value written for them.
- `flagged.py`: the stem and master effect of each of those notes.
- `entryspk.py`: attack transients on entries after rests.
- `mbumps.py`: master-level bumps at legato joins.
- `who.py`: which stems rise at a given moment.

Run them with `CYC=21 ~/.venvs/claude-composes-reaper/bin/python`. `dbg/` holds two patched copies of `score_to_parts.py` and the parts.json files they produce, written only to scratch. Levels are stereo power.

Delivery numbers for c21 come from `metrics.md` and were not re-measured: master -22.5 LUFS, LRA 23.6 LU, TP -3.9 dBFS; mp3 -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.5 dB, limiter 1.9 dB.

## Checked and working (measured, c21)

- **Keyswitches, chords and ties.** Every keyswitch is at least 20 ms ahead of its note, except the known Ob1 207.952 (13 ms). No chord goes to a legato patch. All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
- **Phrase ends and breaths.** Phrase-end tapers and releases are within 0.5 dB and 0.04 s of c20 on every track (`ends.py`). The breath gaps and depths are unchanged (`breath2.py`).
- **c21 notches.** At master level they worked (`mbumps.py`, joins that raise the master by 2.5 dB or more).
  - Vln I 68: +6.4 -> under 2.5. Vc 68.5: +6.0 -> under 2.5. Vln II 177.5: +4.1 -> under 2.5.
  - Vc 240.5: +4.5 -> +3.0. Horn 1 30: +3.4 -> under 2.5.
  - Stem spikes of 3.5 dB or more fell from 120 to 114 of 606 joins.

## 1. Moved entries start on the previous phrase's dynamic. A rounding error drops the CC11/CC1 "pull" in about half the cases. Measured.

**What happens.** `score_to_parts.py` moves an entry's note-on early: the entry lead, abut lead, div entry, or flautando join. For each such note it records a "pull" (moved onset, score onset), so that CC11 already holds the new note's level from the moved onset (`final2`). `sample()` evaluates the curve only at grid points rounded to 4 decimals. When the moved onset rounds down (for example 228.94722 -> 228.9472), the grid point falls just before the pull's start, because the test is `a_ - EPS <= q` with EPS = 1e-6. The pull is skipped, and the CC11 point is written at the score onset. The note then sounds from its moved onset on the CC11 value of whatever the track last played. CC1 follows `final2`, so it is wrong in the same notes.

**Where.** 26 CC points on 15 tracks are affected (`ccorder.py`, compared with the patched `dbg/parts2.json`). The audible ones (`flagged.py` on the c21 stems):

| track, score onset | printed | CC11 at note-on -> at score onset | lead | stem peak over body | master rise |
|---|---|---|---|---|---|
| Bassoon 1, 229 (bar 68) | pp, under the horn solo | 114 -> 34 | 0.06 s | +14.8 dB | +5.5 dB |
| Bassoon 2, 232 (bar 69) | pp | 114 -> 34 | 0.06 s | +13.8 | +4.1 |
| Horn 1, 226 (bar 67, "1. solo", p) | p | 102 -> 54 | 0.11 s | +4.2 | +3.7 |
| Horn 4, 286 (bar 87) | pp | 74 -> 34 | 0.10 s | +7.0 | +2.5 |
| Horn 3, 286 (bar 87, con sord.) | pp | 74 -> 34 | 0.10 s | +4.1 | +2.7 |
| Horn 2, 250 (bar 75) | | 88 -> 58 | 0.05 s | +3.4 | |
| Horn 3, 204 (bar 61, ff tenuto) | ff | 34 -> 93 | 0.15 s | soft start; reaches body -6 dB at +0.04 s | |
| Bassoon 1, 196 (bar 59) | f | 46 -> 88 | 0.06 s | soft start, then +9.2 dB at +0.23 s | |
| Violas, 262 (bar 79) | ff | 83 -> 114 | 0.06 s | late f layer | |

- **Bassoon 1, qn 229.** The stem's 20 ms trace is -31.4 dB at the attack and -45..-48 dB for the body. The attack is as loud as the horn solo (-31.5) at the same instant, and it is the largest single bump on the master at any join or entry in the movement (`mbumps.py`, `entryspk.py`). A listener hears an unprinted ff bassoon accent under a p horn solo.
- **The pp entries** (Bn1/Bn2 229/232, Hn3/Hn4 286, Hn1 226) start for 50-110 ms on the ff or mf dynamic layer. That breaks Dan's rule 4 (no hard transients) and rule 1 (dynamics as printed).
- **The f/ff entries** (Hn3 204, Bn1 196, Vla 262) start on a p layer and swell into the f layer. That is a late, soft attack on a printed ff tenuto.
- **The bug is old.** It has been present since c05 (Bn1 196, Hn3/Hn4 286); Bn1/Bn2 229/232 since c15, Hn1 226 since c18. Earlier cycles compensated for its symptoms by hand:
  - Bn1 196 note trim -9 (c05).
  - Horn 4 286 note trim -5 (c07).
  - Horn 3 204 entry lead +0.10 plus an 8 dB fill (c11, which reported the attack as late).

**Fix:**

(a) `tools/score_to_parts.py`, `build_track`. Replace the line `pulls = sorted(set(pulls))` (just before `def final2`) with:
```python
    PULL_PAD_QN = 0.01   # c22 (A #1): the pull starts on a 4-decimal grid point just before the moved note-on
    pulls = sorted(set((round(a_ - PULL_PAD_QN, 4), b_) for a_, b_ in pulls))
```
- The 0.01 qn pad puts the controller change in the rest before the entry, as `early_time` does for other controllers. This also avoids any same-tick ordering of CC and note-on in REAPER.
- The pulls are already added to `breaks`, so the new start lands on the grid exactly.
- I ran this patched copy into scratch (`dbg/sp2.py` -> `dbg/parts2.json`). All CC11 mismatches are gone. Bn1 229 now has CC11 34 at 228.9372 (note-on 228.9472). Hn1 226 has 54 at 225.8994, Hn3 204 has 93 at 203.9129, and Hn4 286 has 34 at 285.9295.
- Nothing else in parts.json changed except the CC1/CC11 points listed by the diff: Ob1, Cl1, Bn1, Bn2, Hn1-4, Vln II, Vla, Vc, Cb, Vla div and Horns 1-2 a2.
- It is a `--midi-only` change.

(b) Remove the compensations in the same cycle, or they will overshoot:
- `build/note_trims.json`: Bassoon 1 "196" -9 -> 0. Horn 4 "286" -5 -> -1.
- `build/early_fills.json`: Horn 3 "204" {8, hold 0.10} -> {2, hold 0.10}.
- `build/entry_leads.json`: Horn 3 "204" 0.10 -> 0. The family lead of 0.05 s stays.
- List these under `_auto` as "c22 set by hand (pull fix)", so that `auto_fills.py` does not restore them from the c21 render, which still has the bug.

(c) Lower priority. Vibrato on entries still uses the score onset, because `sounding()` and the delayed-vibrato ramp in `cc1_fn0` take `n["qn"]`. Examples: Vc 274 starts with CC1 95 for 0.12 s, then 40; Ob1 208 starts at 110, then 75. In `cc1_fn`, evaluate `cc1_fn0` at the pull's end (`b_`) when `q` is inside a pull, as `final2` does.

**Check:**
- `ccorder.py` on the new parts.json: no CC11 row with overlap=False.
- `flagged.py` on c22:
  - Bn1 229 and Bn2 232: peak over body at most +4 dB, and master rise at most +1.5 dB.
  - Hn1 226 and Hn3/Hn4 286: at most +3 dB.
  - Hn3 204: reaches body -6 dB by +0.02 s, with the 30 ms peak at most +3 dB over the body.
  - Bn1 196: no +9 dB bulge at +0.23 s.

## 2. Remaining unwritten accents at legato joins in exposed lines. Measured: the spikes repeat in c20 and c21 within 0.5 dB, except Vln I 72.

`spikescan.py 5` finds 46 joins. These are the ones that raise the master or sit in an exposed line:

| track, onset | bar | spike over the louder body | where (qn) | stem rise at the spike | note |
|---|---|---|---|---|---|
| Oboe 1 145 | 46.25, dolce espr. solo | +5.8 (c20 +5.9) | 144.82-144.91 | +7.0; master +4.3 | the spike is before the 2 dB fill, so it comes from the transition sample |
| Violins II 73.5 | 25.5, theme a' | +5.3 (c20 +5.3) | 73.35-73.41 | +6.8 | Vln II peaks at -33.0, over Vln I at -37.8 after the c21 Vln I notch. The unison partner now carries the accent that the notch removed from Vln I |
| Violins I 72 | 25.0 | +5.9 (c20 +7.9) | 71.92-71.96 | +3.5; master +4.1 | the c21 notch (72.01-72.08) sits after the c21 spike; the spike moved 0.1 s earlier (round robin) |
| Violins I 249.5 | 74.83 | +5.2 | 249.39-249.43 | +5.8; master +3.4 | new in c21 |
| Violins II 83 | 28.67 | +5.2 | 82.85-82.90 | +3.3 | |
| Horn 1 180 / 202 | 55 / 60.5 | +5.0 / +5.4 | | | caused by the fills, 4.2 + the B #4 lift, and 8.0 from the auto_fills raise |

**Fix** (`tools/score_to_parts.py` `JOIN_NOTCH`; depth = spike - 2, as in c21):
- "Violins I":
  - Replace `(72.01, 72.08, -6.0)` with `(71.90, 72.08, -4.5)`. This covers both positions the spike has taken; the depth is lower because the span is wider.
  - Add `(249.37, 249.44, -3.5)`.
- "Violins II": add `(73.33, 73.42, -4.0)` and `(82.84, 82.91, -3.5)`.
- "Oboe 1": add `(144.81, 144.92, -4.0)`.
- `build/early_fills.json` Horn 1: "180" 4.2 -> 2.5 and "202" 8.0 -> 6.5. Mark both as lowered by hand in `_auto`.

**Check:**
- `spikescan.py 5` on c22: these joins at +3.5 or less.
- `mbumps.py 2.5`: Ob1 145 and Vln I 249.5 drop off the list.
- `joins.py 22 70 84 6`: no new dips of 6 dB or more.

## Not findings, checked

- **Patch choices.** I checked the Brass folder for a better patch:
  - The Solo and 2 French Horns folders have only stopped-horn mutes (Stop Sus, Stop Stac), no con sordino. Horn 3's bar 87 con sord. stays on the open KS Master, with the CC15 handling decided in c03.
  - "2 Trombones and 1 Bass Trombone" is an ensemble of three players, so it is no solo bass trombone.
  - Nothing better than the current patches is available for this lens.
- **Bow marks** at 265 (Vln I/II/Vla upbow on a tied note) and in the coda (292-301, "change bow at will"). These are bow changes on held notes. Rendering them as one continuous note is correct.
- **Flute 1 at 266** (+10.6 dB spike) and 254/212 (+9). Here the flute's vibrato swings 6-8 dB on a 20 ms window, and the master rises only 1.3-1.6 dB. Not proposed, as in c21.

**Do not touch:**
- **Notches and fills.** The c21 `JOIN_NOTCH` entries other than Vln I 72, and the c21 hand-lowered fills (Ob1 145, Vln I 68/80, Vc 156/256, Fl1 129.5/193/194).
- **Leads.** `ABUT_LEAD` (Bn1 and Cb), `LEG_CAP_FRAC`, the leg_leads and pair leads, and `slur_out`. The entry-lead amounts themselves stay. Only the CC pull changes.
- **Mechanics.** Tie handling, keyswitch placement, CC15/`mute_eq`, pizz. steps, the plucked note-trim step, the harp rolls, the timpani tie strokes, the caesura breaths, and the Tbn1 accents (218 now +3.2 over the eighths).

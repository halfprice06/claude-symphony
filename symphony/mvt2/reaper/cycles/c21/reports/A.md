# Cycle 21, critic A: articulation and phrasing (on the cycle 20 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c21-A/`: the c20-A set, plus `spikes.py`, `spikescan.py`, `notchplan.py`, `bumps21.py`, `bumps21b.py`, `expo.py` and `trace.py`. Run them with `CYC=20 ~/.venvs/claude-composes-reaper/bin/python`. `lib.py` now takes `PARTS=<parts.json>`, so an older render can be measured with the parts.json that made it (c19: `cycles/c20/before/build/parts.json`). Levels are stereo power. Times are relative to the score onset (`sq`).

Delivery numbers for c20 (from `metrics.md`, not re-measured): master -22.6 LUFS, LRA 23.6 LU, TP -3.8 dBFS. mp3 -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.5 dB, limiter 2.2 dB.

## Checked and working (measured, c20)

- **Keyswitches, chords and ties.**
  - Every keyswitch is at least 20 ms ahead of its note, except the known Ob1 207.952 (13 ms).
  - No chord goes to a legato patch.
  - All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
  - The one leap of more than an octave into a legato row (Vln II 218, C6 to D4) does not overlap the tremolo note before it, so no transition is played.
- **Phrase ends.** Median taper 1-7 dB and release 0.17-0.63 s on every track (`ends.py`).
- **Pizzicato.** The Vc/Cb/Vla pizz. notes decay 15-30 dB before their note-off, so the note-off does not cut the ring.
- **Harp.** Rolls are spaced 0.035 qn (about 40 ms at the tempo). Ring after the last chord of a phrase falls 5-15 dB in 1 s.
- **Portato.** Vln II bars 15-21 (tenuto under slurs, repeated A flat 4): the pulses dip 0.7-5.9 dB.
- **Bassoon 1 abut lead.** Unchanged since c19.

## 1. In the main melodic lines, about one legato join in ten produces an unwritten accent: a transition spike 5-12 dB over both the old and the new note, lasting 0.05-0.2 s. Measured. The effect on the listener is inferred.

**Where:** 61 of 606 legato joins (`spikescan.py 5`; spike at least 5 dB and at least 30 ms wide). The joins that matter most are in exposed melody, where the spike also raises the master:

| Track, onset | bar | spike over the louder body | width over +2 dB | master rise (est.) | c19 |
|---|---|---|---|---|---|
| Violoncellos 68.5 | 23.83 | +11.7 dB | -0.15..-0.01 s | +4.0 | +11.8 |
| Violins I 68 | 23.67 | +10.7 | -0.09..+0.02 | +6.7 | +5.6 (at -0.15..-0.09 s) |
| Violins I 72 | 25.00 | +7.9 | +0.01..+0.09 | Vln I is over the master here | +8.1 |
| Violins I 73.5 | 25.50 | +8.2 | -0.15..-0.06 | Vln I is over the master here | +8.1 |
| Violins I 80 | 27.67 | +6.7 | -0.15..+0.03 | +5.5 | +6.9 |
| Violins I 75 | 26.00 | +5.0 | -0.12..-0.03 | +3.9 | +5.0 |
| Violins II 177.5 | 54.38 | +6.7 | -0.15..+0.02 | +5.6 | +6.3 |
| Violin I solo 53 | 18.67 | +6.2 | -0.01..+0.19 | +5.2 | +6.2 |
| Horn 1 30 | 11.00 | +4.6 | -0.15..+0.01 | +4.1 | +4.6 |
| Violoncellos 240.5 | 71.83 | +7.5 | -0.15..-0.06 | +2.8 | +6.9 |
| Violins II 243 / 245.5 | 72.67 / 73.5 | +5.5 / +6.1 | short | +2.6 / +2.2 | +5.4 / +5.9 |
| Violins II 270.5 | 81.83 | +7.0 | -0.12..0.00 | +2.0 | +7.2 |
| Violas 162 | 50.50 | +5.9 | -0.15..-0.04 | +2.3 | +5.9 |
| Violoncellos 182 | 55.50 | +5.5 | -0.15..-0.01 | +2.1 | +5.5 |

- **Location.** The worst cluster is theme a', bars 23-27. That is the theme in both violin sections over the cello counter-melody, at p < mf. There, 5 of the 22 Vln I joins and the cellos' first slurred eighth (68.5) carry spikes of 5-12 dB.
- **Shape.** The 20 ms trace of Vln I at 68 shows -36 dB body, -26 dB peak and -37 dB body again within 0.12 s (`trace.py "Violins I" 67 69.5`). That reads as a hard bow accent on beat 3 of bar 23, the start of the printed crescendo.
- **Repeatability.** The spikes come from the transition samples:
  - With the volume envelope removed, they are the same size (`bumps21b.py`: Vln I 68 11.1, Vc 68.5 12.9, Vln I 72 7.2).
  - They repeat in c19 and c20 within 0.5 dB at the same time, except Vln I 68, whose spike moved and grew. That suggests a round-robin or bow-direction variant on that one join.
  - They occur at v124 (strings, horn) and at v60/80 (oboe), so the legato velocity does not cause them.
- **Why it matters.** Dan's rules 1 and 4: slurs should sound connected, and accents only where printed, at 2-4 dB with no sharp transient. These are unprinted accents of 5-12 dB.

**Fix:**

(a) This cycle, in `tools/score_to_parts.py`: add these `JOIN_NOTCH` entries (from qn, to qn, dB). They use the existing 0.04 qn ramps. Depth is 2 dB less than the smaller spike of c19 and c20, capped at 6, except Vc 68.5. Keep the existing Vln I 207.80 entry.

```python
JOIN_NOTCH = {"Violins I": [(67.86, 68.02, -3.0), (72.01, 72.08, -6.0), (73.37, 73.45, -6.0), (74.90, 74.98, -3.0),
                            (79.86, 80.03, -3.0), (207.80, 207.97, -4.0)],
              "Violoncellos": [(68.37, 68.49, -8.0), (181.85, 181.99, -3.5), (240.37, 240.45, -5.0)],
              "Violins II": [(177.35, 177.52, -4.3), (242.99, 243.05, -3.3), (245.39, 245.47, -3.9), (270.41, 270.50, -5.0)],
              "Violin I solo": [(52.99, 53.15, -4.0)],
              "Horn 1": [(29.88, 30.01, -2.5)],
              "Violas": [(161.86, 161.96, -3.9)]}
```

- Vln I 68: the spike is not repeatable, so its notch is broad and shallow.
- Vc 68.5 gets -8: it measured +11.7/+11.8 in both renders, and -6 would leave 6 dB.

(b) For later cycles: add a measured pass, the inverse of `auto_fills.py`. Either a `--peaks` mode or a new `tools/auto_notches.py PREV PARTS --write`. It would write `build/join_notches.json` ({track: {onset: [t0_s, t1_s, dB]}}, seconds after the score onset), and `score_to_parts.py` would append those entries to `JOIN_NOTCH`. The rule:
- Tracks: the string sections, Violin I solo, the div tracks, Horn 1, Ob1, CA, Cl1 and BCl. Not the flute: its high-register vibrato reaches +5 dB on a 30 ms window.
- Measurement: 30 ms envelope, 5 ms hop. The reference is the louder of the two bodies, as in `auto_fills`. The window runs from the moved start - 0.03 s to the score onset + 0.15 s.
- Write a notch when the spike is at least 5 dB and the region over reference + 2 dB is at least 0.03 s wide. Depth = -(spike - 2), capped at -6. The region is the notch span.
- Skip any join that has an early fill. Finding 2 handles those.

**Check:**
- Rerun `spikescan.py 5` on c21. Every listed join should be at +3.5 dB or less.
- `joins.py 21 0 304 6`: no new join dip of 6 dB or more at these onsets.
- If Vln I 68 shows a dip of more than 4 dB, halve its notch.

## 2. Several early fills sit on a transition peak and make it larger. Measured.

Each fill adds its dB to the 30 ms peak. The overshoot rule in `auto_fills.py` cannot see this: for Fl/Ob/CA it uses a 200 ms window, and the other tracks only get a check on the 200 ms body.

| Track, onset | fill (dB, hold) | 30 ms peak over body: with envelope / samples only | master rise |
|---|---|---|---|
| Oboe 1 145 (bar 46, dolce espr.) | 6.8, 0.1 s | +4.8 / -0.5 | +4.6 |
| Violins I 80 (bar 27.67) | 4, 0.2 s | +6.9 / +4.8 | +5.5 |
| Violoncellos 256 (bar 77) | 3.4, 0.1 s | +5.0 / +2.1 | +1.0 |
| Violoncellos 156 (bar 49) | 4.0, 0.1 s | +5.7 / +4.3 | +1.1 |
| Flute 1 193 (bar 58) | 6.0, 0.1 s | +8.2 / +4.7 | +2.5 |
| Flute 1 194 | 4.6, 0.29 s | +6.1 / +2.2 | +1.4 |
| Flute 1 129.5 (bar 42) | 4.8, 0.1 s | +5.6 / +2.3 | +1.6 |

The Vln I 68 fill (3 dB, 0.35 s) also sits on the finding 1 spike.

**Fix:**

1. Lower these entries in `build/early_fills.json`, and list them under `_auto` as "lowered" so the next rerun does not raise them:
   - Ob1 145: 6.8 -> 2.0.
   - Vln I 80: 4 -> 2. The notch in finding 1 covers the rest.
   - Vln I 68: 3 -> 1.5.
   - Vc 256: 3.4 -> 1.0. Vc 156: 4.0 -> 1.5.
   - Fl1 193: 6.0 -> 3.0. Fl1 194: 4.6 -> 2.0. Fl1 129.5: 4.8 -> 2.5.

   For the flute values, the 30 ms reading includes vibrato. They are set so the peak without vibrato is no more than 2-3 dB over the body, and they keep half of each fill.
2. In `auto_fills.py`, add a second overshoot test (b2), every track. Remove the vol_db fill shape from the stem (as `bumps21b.py` does). Then if the 30 ms peak in [moved onset - 0.05 s, score onset + 0.3 s] is more than 3 dB over the louder body, and the fill adds at least 2 dB to that peak, lower the fill by (peak - 2) dB. Lowering is limited to the fill's own dB.

**Check:**
- `bumps21b.py "Oboe 1,Flute 1,Violins I,Violoncellos" 4`: raw bump at most +3 on these onsets.
- `auto_fills.py 21` reports no new dips of 5 dB or more there.

## 3. Trombone 1's last printed accent (qn 218, bar 64, f4.-> starting the >) is only 1.5 dB over the unaccented marcato eighths before it. The two accents at 212.5 and 213 are 4.1 and 4.7 dB over. Measured.

**Evidence** (`Trombone 1` stem, 20 ms peaks):
- Accents: 212.5 -20.0, 213 -19.4, 218 -22.6 dB.
- Unaccented eighths 214.5-217.5: -23.0 to -25.1, mean -24.1.
- Trombone 1 is within 0.1-1.5 dB of the master at every one of these peaks, so the line is fully exposed.
- Cause, in parts.json `vol_db`:
  - Each unaccented `MARCATO_SPANS` eighth gets +5.0 dB on its attack (`MARC_BODY_DB` 2 + `MARC_ATTACK_DB` 3, at 217.03 and 217.53).
  - The accent at 218 gets only its `ACCENT_DB_AT` +3.0 (at 218.007). The accent is therefore boosted less than the notes it should stand out from.

The printed line is r8 e8-> c'4.-> b8 bes8 a8 | a4 gis8 a8 f4.-> \> e8\mf. Its last accent marks the peak before the dim., so it should stand 2-4 dB over the eighths (Dan's rule 4).

**Fix:** `tools/score_to_parts.py` `ACCENT_DB_AT = {"Trombone 1": {212.5: 4.0, 213.0: 3.0, 218.0: 4.5}}` (was 3.0).

Expected (inferred): 218 at about -21.1, which is +3 over the eighths and still 1.7 dB under the 213 accent, as the ff-to-mf line implies. Its attack rise is 0.115 s, so a higher level does not make a click.

**Check:** per-note 20 ms peaks. 218 should be 2.5-3.5 dB over the 214.5-217.5 mean and under 213.

## 4. After the portamento at qn 172 (bar 53, "sul A"), Violins II lose 7 dB for about a second. Their unison partner, Violins I, does not. Measured; mostly masked in the master (inferred), so low priority.

**Evidence** (20 ms trace):
- Vln II: -43 dB before the join, a 9.6 dB dip at +0.18 s, then -50..-53 dB for 1 s.
- Vln I, in unison: -45..-48 dB over the same span.
- The master holds -34..-38 dB.
- Vln I's own port join dips 2.9 dB, and Vln II's at 82 dips 3.9 dB.

**Fix:** `build/early_fills.json` "Violins II": `"172.0": {"db": 4, "pre_s": 0.0, "hold_s": 0.35}`.

**Check:** `joins.py 21 170 173 0`. Vln II 172 dip at most 5 dB, with no spike over +3 (spikescan).

## Not findings, checked

- **Legato velocity.** The spikes in finding 1 occur at v124 and at v60-80 alike, so lowering the string legato velocity (HO manual: 50-60 slower, 110-127 tighter) would not remove them. It would also undo the lead tables. Not proposed.
- **Intro timpani roll (bars 2-3).** The printed > on the bar 3 roll (qn 6-8) is not rendered: the stem stays at -58..-63 dB, because the CC7 curve has nothing under ppp. The roll is about 20 dB under the master there, so the missing dim. is inaudible. The tied strokes at qn 8 and 237 stay as rolls (c14 decision); not reopened.
- **Repeat-pitch tenuto in Vln II bars 15-21.** Pulses are present. No change.

**Do not touch:**
- **Leads and joins.** `ABUT_LEAD` (Bn1 and Cb), `LEG_CAP_FRAC`, the c19 leg_leads and pair leads, `slur_out`, `BC_SOFT`/`BC_SOFT_SKIP`, `SOST_HOLD_THROUGH`, the existing `JOIN_NOTCH` entry.
- **Loop seams.** The loop profiles and the c20 loop_fills.
- **Ties, keyswitches, mutes.** Tie handling and keyswitch placement, CC15/`mute_eq`.
- **Pizzicato, harp, timpani.** Pizz. timing and steps, the harp rolls, the timpani tie strokes.
- **Breaths and marcato.** The caesura breaths. The Tbn1 marcato eighths (only the 218 accent changes).

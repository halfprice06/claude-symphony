# Cycle 17, critic A: articulation and phrasing (on the cycle 16 render)

Scripts and data are in `/private/tmp/claude-501/mockup-loop/c17-A/`. They are the c16-A set plus:
- `lfchk.py` and `lfalign.py`: where the c16 loop fills landed, and the dip depth at each one in c15 and c16.
- `stp_dbg.py`: a copy of `score_to_parts.py` with debug prints. It writes only to the scratch folder, and its output is identical to `build/parts.json`.
- `refit.py` and `loopdipsc.py`: seam dips with the volume envelope removed.
- `simfill.py`: simulates the bump fills.
- `fold.py` and `foldx.py`: folded loop profiles, fitted in-sample and out-of-sample. The output is `loop_profiles_c16.json`.
- `overs.py` and `fljoin.py`: wind fill overshoot at 30 ms and 200 ms.
- `slurnonleg.py`, `startmodes.py` and `krange.py`: patch and slur checks.

Run them with `CYC=16 ~/.venvs/claude-composes-reaper/bin/python`. `build/parts.json` (21:16) is the data behind the c16 render (21:17). The only difference is the post-render Violas fix.

## Checked and working (measured)

- **Chords and slurs.** No chord goes to a legato patch. Every slurred pitch change plays on a Leg articulation except the intended ones: the viola sextuplets on bars 59-60 and the Cor anglais portato at 157 (`slurnonleg.py`). Inside slurs, only the six intended re-attacks remain.
- **Ties.** All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
- **Keyswitches.** Every keyswitch is at least 20 ms before its note, except the known Ob1 207.952 (13 ms).
- **Legato joins** (`wjoin2.py`):
  - The median dip is 1.5-3.1 dB on every legato track.
  - Only four joins reach 8 dB: Vln I 67.5 (10.5), Vln II 63 (9.0), Vln II 172 (8.2), and the Vc 124 arco entry, which is not a join.
- **Printed breaths** dip 9-38 dB.
- **Accents.** The Tbn1 accents at 212.5, 213 and 218 are +1.8, +2.2 and +3.2 dB over the body, inside Dan's 2-4 dB.
- **c16 A #2 (Flautando, bars 37-40).** Only qn 112 still has a trough of 6 dB or more: 7.0 dB for 0.10 s (`rebow.py`). The troughs at 114 and 120 are gone. Fix B (divisi tracks) is not needed.
- **c16 A #4 (bar 80 bow change).**
  - Vln I measures -30.0 dB at 264.3-264.95 and -31.4 dB at 265.1-265.8, which passes.
  - Vln II's slurred A flat at 266 now dips 7.7 dB, and Vln I's dips 3 dB.
  - The master rises at 266 (-20.8 to -19.9 dB), so the tutti does not show it.

## 1. Loop-seam pulse in the long string notes: c16 removed only a little of it. 14 of the 43 fills never reached the envelope, and the bump method cannot remove the pulse even when the fills land. Replace it with a folded inverse profile. Measured, and simulated out of sample.

**Where:**
- Vln I qn 0 and 292.
- Vc 164, 274 and 292.
- Cb 220, 271 and 292.
- Vla 292 and Vln II 286: bars 1-4, 53-55, 65-70, 82-87 and 89-92 (the final chord).

**What is wrong.** `loops.py` on c16 still finds the 3.95 s pulse:

| Note | Pulse p-p | Autocorrelation |
|---|---|---|
| Cb 271 | 11.7 dB | 0.64 |
| Vln I 292 | 10.2 dB | 0.62 |
| Cb 292 | 9.7 dB | 0.59 |
| Vc 292 | 7.7 dB | 0.60 |
| Cb 220 | 5.8 dB | 0.74 |

c15 measured 12.4, 10.5, 11.8, 9.9 and 5.8 dB on the same notes.

**Evidence, part 1: a bug in `tools/score_to_parts.py`** (line 2117, the c16 loop-fill block):

```
ts_ = [t_ for i_, t_ in enumerate(ts_) if i_ == 0 or t_ - ts_[i_ - 1] >= 0.02 or i_ == len(ts_) - 1]
```

- Each bump is sampled at width/20. For any width under 0.4 s the step is under 0.02 s, so the filter removes every inner point. A bump of that width puts one 0 dB point into the envelope and nothing else.
- With `stp_dbg.py`, Cb 220's four bumps produce 5 points, all at 0.0 dB, and `vol_db` is flat at +4.0 from 220.25 to 238.
- The fills lost this way:
  - Cb 220: all four.
  - Cb 271: 2.45, 6.45 and 14.4.
  - Vc 274: 3.35 and 7.3.
  - Vc 292: 17.5.
  - Vln I 292: 4.45 and 8.4.
  - Vln I 0: 4.85 and 8.8.
- At those seams the c16 dip equals c15 within 0.5 dB (`lfchk.py`). For example, Cb 220 at 7.95 s is 5.3 -> 5.5 dB.

**Evidence, part 2: the bumps cannot work even when they land.**
- The fills that did land made the 10 ms dips 1.5-3.5 dB shallower: Cb 292 at 8.05 s went 12.0 -> 8.9, Vln I 292 at 2.75 s went 10.5 -> 7.1.
- The pulse is not a row of narrow notches. It is a whole-cycle swell and sag.
- Folded over its period, with the volume envelope removed, the cycle shape has these peak-to-peak depths:

  | Note | Cycle p-p |
  |---|---|
  | Cb 271 | 15.3 dB |
  | Cb 292 | 15.4 dB |
  | Vln I 0 | 14.3 dB |
  | Vln I 292 | 11.6 dB |
  | Vc 292 | 10.6 dB |

- Re-fitting the bumps at 10 ms and applying them (`simfill.py`) leaves the pulse as large, or larger: Vln I 292 10.3 -> 11.9, Vc 292 7.6 -> 9.7.
- The pulse is a fixed function of the time since note-on:
  - The period is 3.97 s for all of these notes (Vln II 286: 3.40 s; Vla 292: 3.93 s).
  - With the envelope removed, the c15 and c16 stems give the same profile, although their tempo maps differ.

**Fix: replace the bump table with a periodic inverse profile.**

1. Copy `/private/tmp/claude-501/mockup-loop/c17-A/loop_profiles_c16.json` to `build/loop_profiles.json`.
   - It has one entry per note: `{track: {sq: {period_s, corr_db[]}}}`, with `corr_db` in 20 ms phase bins.
   - `corr_db` is the folded median profile, inverted, clamped to -3..+8 dB and smoothed over 0.1 s. It is then shifted so the note's mean power is unchanged (shifts of 0.2-1.6 dB). The final range is -4.6..+6.6 dB.
2. In `score_to_parts.py`, next to the loop-fill block, add a `LOOP_PROFILES` pass for each listed note:
   - Let t0 = max(0, `qn_to_sec(new_on(n))`), the same convention as the fills.
   - Every 0.04 s from t0 + 0.8 s to the note's end minus 0.3 s, add `corr_db[int(((t - t0) % period_s) / 0.02)]`.
   - Fade in over the first 0.3 s and out over the last 0.3 s. Write the points as exact `vol_bp` points through `sec_to_qn`.
   - That is about 25 points per second over 10 notes, roughly 4,000 breakpoints.
3. Delete these notes' entries from `build/loop_fills.json`; otherwise they would stack with the profile.
4. Fix the dedupe in line 2117 anyway, for any fills that remain: compare each point with the last kept point, not with the previous point in the list.

**Simulated, out of sample.** The profile was fitted on the c15 stems and applied to the c16 stems with the envelope removed (`foldx.py`, 50 ms `loops.py` metric):

| Note | Pulse p-p, c16 | Pulse p-p, simulated | Autocorrelation, c16 | Autocorrelation, simulated |
|---|---|---|---|---|
| Cb 220 | 6.0 | 1.5 | 0.75 | 0.30 |
| Cb 271 | 11.8 | 5.1 | 0.63 | 0.35 |
| Cb 292 | 9.4 | 5.7 | 0.57 | 0.29 |
| Vc 274 | 7.6 | 4.2 | 0.51 | 0.19 |
| Vc 292 | 8.0 | 4.2 | 0.56 | 0.24 |
| Vc 164 | 9.6 | 4.6 | | |
| Vln I 0 | 11.5 | 6.0 | 0.47 | 0.19 |
| Vln I 292 | 10.3 | 5.5 | 0.61 | 0.43 |
| Vln II 286 | 7.6 | 5.0 | 0.47 | 0.14 |
| Vla 292 | 8.8 | 7.5 | 0.37 | 0.23 |

**What a listener hears (inferred):** the "change bow at will" pp-ppp held notes, the bass pedal of bars 82-87 and the final chord stop swelling and sagging every 4 s.

**Caveats:**
- The profiles are valid only while these tracks' patch, mics and reverb are unchanged.
- The Vln I coda's printed bow notches (4.0, 8.1 and 12.6 s after 292) stay in CC11, and the profile does not touch them.

**Check:**
- `loops.py`: p-p 6 dB or less and autocorrelation 0.45 or less on every listed note.
- `bandloop.py Master 292.5 303.5 30 200`: under 8 dB (c15: 13.9).
- Bar RMS of bars 82-92 within ±0.7 dB of c16.

## 2. Wind legato fills: 14 now overshoot their joins by 2.5-8 dB, and this cycle's `auto_fills.py` plan would raise several of them. The flute's high-register "dips" are vibrato troughs. Measured.

**Where:**
- Flute 1 at 190, 200, 252, 255, 256 and 266 (bars 57-60 and 75-80).
- Cor anglais at 97, 99, 132, 134 and 152.
- Clarinet 1 at 178 and 266.
- Oboe 1 at 143.

**Evidence, part 1: the flute's envelope.**
- The flute's sustained notes at pitch 88 and above carry 10.5 dB p95-p5 of amplitude modulation at 3.9-4.7 Hz (`fljoin.py`; the vibrato rate).
- For comparison, the body roughness is 6.0 dB at pitch 72-84, 1.9 dB on the horn and 0.9-1.2 dB on the clarinet.
- `auto_fills.py` measures dips with a 30 ms window, so it reads a vibrato trough next to a join as a hole.

**Evidence, part 2: the same joins at two window lengths.** The table compares a 30 ms window with a 200 ms window, which spans one vibrato cycle. The reference is the louder of the two note bodies.

| Join | Fill | 30 ms dip / over | 200 ms dip / over | Sample dip, envelope removed, 200 ms |
|---|---|---|---|---|
| Fl1 190 | 8.0 | 11.2 / +10.7 | 1.7 / **+5.4** | 2.8 |
| Fl1 252 | 8.0 | 11.8 / +12.0 | -1.5 / **+6.1** | 4.0 |
| Fl1 255 | 5.0 | 7.1 / +9.7 | 2.4 / **+7.5** | 1.7 |
| Fl1 256 | 8.0 | 9.3 / +7.6 | 3.4 / **+3.8** | 8.1 |
| Fl1 200 | 5.1 | 7.5 / +11.0 | 4.4 / **+5.4** | 7.1 |
| Fl1 266 | 2.8 | 15.0 / +10.9 | 4.2 / **+7.9** | 4.5 |
| CA 152 | 6.0 | 5.9 / +8.0 | 1.1 / **+6.7** | 13.6 |
| CA 134 | 5.9 | 3.5 / +6.2 | 2.8 / +3.7 | 8.3 |
| CA 97 | 5.0 | 2.8 / +5.6 | 1.6 / +3.6 | 4.4 |
| CA 99 | 7.6 | 4.1 / +4.7 | 0.4 / +3.0 | 7.0 |
| CA 132 | 7.0 | 6.8 / +6.2 | 4.5 / +2.5 | 8.8 |
| Cl1 266 | 8.0 | 4.2 / +8.4 | -0.2 / **+7.1** | 2.7 |
| Cl1 178 | 5.0 | 3.2 / +4.4 | -0.2 / +3.8 | 2.9 |
| Ob1 143 | 8.0 | 5.2 / +6.0 | 1.8 / +3.5 | 6.3 |

The dry run `tools/auto_fills.py 16 build/parts.json` still raises some of these:
- Fl1 190 (hold 0.35 s).
- Fl1 252 (it stays at the cap of 8).
- Fl1 256 (hold 0.32 s).
- Fl1 200 (5.1 -> 7.2).
- CA 152 (6 -> 8).

**What a listener hears (inferred):** in the flute's climactic lines (bars 57-60, 75-80) and in the cor anglais solo, many slurred notes now begin with a 0.2-0.4 s swell 4-8 dB over the line. In effect these are accents on notes the score slurs. Dan wants accents only where printed, and soft.

**Fix:**

1. `build/early_fills.json`: set new = max(0, fill - (over_200 - 1)) on the entries over 2.5 dB.

   | Track | Entry | New value |
   |---|---|---|
   | Flute 1 | 190 | 3.6 |
   | Flute 1 | 252 | 2.9 |
   | Flute 1 | 256 | 5.2 |
   | Flute 1 | 200 | remove |
   | Flute 1 | 255 | remove |
   | Flute 1 | 266 | remove |
   | Cor anglais | 152 | remove |
   | Cor anglais | 134 | 3.2 |
   | Cor anglais | 97 | 2.4 |
   | Cor anglais | 99 | 5.6 |
   | Cor anglais | 132 | 5.5 |
   | Clarinet 1 | 266 | 1.9 |
   | Clarinet 1 | 178 | 2.2 |
   | Oboe 1 | 143 | 5.5 |

   Keep `pre_s` and `hold_s`. Leave Ob1 140/189: they are both a hole and a peak (dip 10-11 dB at 200 ms).
2. `tools/auto_fills.py`:
   - (a) For "Flute 1", "Oboe 1" and "Cor anglais", measure the dip and the bodies on a 200 ms window (`WIN` per track). Raise or add a fill only if that dip is 4 dB or more.
   - (b) Add an overshoot rule for every track. Take the peak of the 200 ms envelope in [moved onset - 0.1 s, score onset + 0.4 s] minus the louder of the two bodies. If it is over 2 dB, lower the entry by (over - 1). If that takes it to zero or below, delete it. Never raise such an entry in the same pass.
   - (c) Print the lowered entries as "lowered" in `_auto`.
3. Rerun the dry run on c16 after (a)-(b), before `--write`.

**Check (`fljoin.py` on c17):** no listed join over +2.5 dB at 200 ms, and no join's 200 ms dip deeper than in c16.

## 3. The flute's vibrato swings the tutti's presence band at bars 61-62. The amplitude modulation is measured; whether it should be reduced is inferred. Test CC1 on that held note.

**Where:** Flute 1, qn 204-212. It holds Ab6 (pitch 92) ff, Sus MAX, at the top of the Largamente tutti. Flute 1 at 262-268 is similar.

**Evidence:**
- The patch file `FL Sus MAX.oib` holds both "Sus Vib" and "Sus Non Vib" groups. Its release-trail groups switch at CC1 64/65 (`startmodes.py`), so CC1 chooses the vibrato samples.
- CC1 is 99-100 through 204-212 (the rule "CC1 follows the level, ff about 98").
- In the 1.5-4 kHz band:
  - The flute stem has 10.5 dB p95-p5 of amplitude modulation, with a peak at 4.39 Hz. 49% of its modulation energy lies in 3-7 Hz.
  - The master has 5.9 dB, with a peak at the same 4.39 Hz (33% in 3-7 Hz). Oboe 1: 7.6 dB at 4.69 Hz. Vln I: 9.4 dB, but with only 13% of its modulation energy in 3-7 Hz.
- So the tutti's presence band pulses at the flute's vibrato rate.

**What a listener hears (inferred):** a wobbling top on the climax chord. A real flute at ff vibrates too, but in a 60-player tutti it does not modulate the whole band.

**Fix (test, `score_to_parts.py`, the `cc1_fn` block):** for woodwind Sus MAX notes of 3 s or longer at CC11 100 or more, cap CC1 at 80. That is still on the vibrato side of 64. It is about the c16 C #5 "wind vibrato shaping" that was deferred.

**Check:**
- Flute 1 at 204-212: 1.5-4 kHz modulation 6 dB or less, and stem RMS within 1 dB of c16.
- If the modulation does not fall, CC1 is a switch rather than a depth control. Then try 66.

## 4. Viola "div." dyads, bars 23-28 and 87-88: a better patch exists. The cost is measured; the benefit is inferred.

**Where:** Violas, qn 66-90. There are 13 dyads at p-mf, such as (60,63), (58,68) and (61,65), plus the coda dyads (60,63) at 277 and (60,65) at 283. The score marks "div." and "(div.) change bow at will".

**What is wrong.**
- Each voice plays a full-section Sus MAX sample, and the chord is cut 3 dB (`chord_segs`, -10 log10 2).
- So the inner harmony under the bar 23 tune sounds like two full sections, about 24 players, played softer, instead of two half sections.
- The c13 cello answers had the same problem, and the "Violoncellos div" track (Celli KS Master DIV A) fixed it.
- HO has `Violas Divisi/06 Keyswitch/Violas KS Master DIV A.oib` and `DIV B.oib`, and `Violas Divisi/01 Long/Violas Sus MAX DIV A/B.oib`.

**Fix:**
- Add a "Violas div" track: Violas KS Master DIV B, with the same main-channel centring and seat as the Vc div track (`apply_mix`).
- Extend `TRACK_SPLITS` with a rank mode, `("Violas", [(66, 90), (277, 289)], "low")`, which takes the lower note of each two-note chord.
  - A pitch threshold cannot split these chords: the voices cross at 61 and 63.
  - Single notes stay on the main track.
- For the windows, drop the -3 dB `chord_segs` cut on both tracks, because each half section now plays one voice.
- Start the div track's gain at +3 dB, as the Vc div track needed. Load only Sus MAX on it.

**Check:**
- Vla plus Vla div RMS over 66-90 within ±1 dB of the c16 Violas stem.
- No new rearticulation hole at 69-72 (`rebow.py`).
- If REAPER's memory after the load is over 56 GB, drop the coda window.

**Do not touch:**
- **Ties, slurs, keyswitches.** Tie handling and the timpani tie strokes. Keyswitch placement. Slur-scoped legato overlap. The Leg Slur/Leg BC split and its v124 velocity.
- **Leads.** The legato lead tables, `LEG_ART_EXTRA_S`, `LEG_SOFT_EXTRA_S` and `leg_leads.json`.
- **Notches and sostenuto.** `BC_SOFT`/`BC_SOFT_SKIP`, the halved notches, and the soft bow-mark notch of 6 CC.
- **Joins.** `SOST_HOLD_THROUGH`. `slur_out`. `FLAUT_LEAD_S` 0.45 and `FLAUT_OVERLAP_QN` 0.7.
- **Tbn1 marcato and accents.** `MARCATO_SPANS`, `MARC_ATTACK_S` and `ACCENT_DB_AT`. The accents now measure 1.8-3.2 dB.
- **Pizzicato, harp, tremolo.** Pizzicato step trims. Harp rolls and the harmonics track. Tremolo in bars 61-64.
- **Mutes, breaths, phrase ends.** CC15 placement. Breath gaps and phrase-end releases.
- **Planned reverts.** Empty `STACLEG_SPANS` and `METRIC_VEL` as already planned. Nothing here depends on either.

# Cycle 16, critic A: articulation and phrasing (on the cycle 15 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c16-A/`. They are the c15-A set plus `loops.py`, `loop2.py`, `loopc.py`, `loopdet.py` and `loopdips.py` (periodic level pulsing in long notes; `loopdips.json` holds every dip found), `bandloop.py` (the same on a frequency band of the master), `tieslur.py` (slurs that start on a tied note), `sostcause.py` (CC11 and volume steps at the Largamente onsets), `reps.py`, `vibam.py`/`wob.py` (amplitude modulation) and `f0.py`. `lib.py` gained `art_at()`, `events()` and `slurs()`. Run them with `CYC=15 ~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c15 stems. `build/parts.json` (19:27) is the data that made the c15 render (20:05).

Delivery numbers for reference (c15, from the actor's measurements; not under this lens): master -23.6 LUFS, LRA 23.2 LU, true peak -4.5 dBFS; mp3 -19.8 LUFS, LRA 15.9 LU, true peak -1.6 dBTP, span 18.7 dB, limiter 1.9 dB.

## Checked and working (measured)

- No chord goes to a legato patch (`chords_leg.py`).
- All 104 ties are held. The only re-attacks are the intended timpani tie strokes at 203 and 211 (`ties.py`).
- Keyswitches: every one lands at least 20 ms before its note, except the known Ob1 207.952 (13 ms) (`kscheck.py`).
- Inside slurs, only the six intended non-overlapping legato notes remain (`slurov.py`).
- Legato joins: the median dip is 2.2-3.7 dB on every legato track (`wjoin2.py`). Only four joins reach 8 dB after the envelope:
  - Vln I 67.5: 10.3 dB.
  - Vln II 63: 9.4 dB.
  - Vln II 172: 8.1 dB.
  - BCl 92.5: 9.4 dB.

  The Vc 124 "join" (17.9 dB) is the arco entry after the pizz. note, not a legato join.
- Phrase-final tapers are 1-5.5 dB, and releases reach -15 dB in 0.12-0.8 s (`ends.py`).
- Printed breaths dip 12-38 dB, except Hn1 196 at 7.2 dB (`breath2.py`).
- The Tbn1 marcato line now has separation and small attacks: 214.5, 215, 215.5, 217 and 217.5 rise 1-3 dB over their bodies.
- The harp harmonics sound at the written pitch plus an octave: 311 Hz at qn 273 and 413 Hz at 274 (`f0` check).
- The timpani rolls at 226 (13.5 s) and 292 (18.7 s) sustain without gaps.

## 1. Long string notes pulse every 3.95 s: the samples' loop seams make 4-9 dB dips. In bars 89-92 the sections dip together, so the final chord throbs. Measured.

**Where:** every arco string note longer than about 6 s:
- the opening (Vln I qn 0);
- bars 53-55 (Vc 164);
- bars 65-70 (Cb 220);
- bars 82-87 (Cb 271, Vc 274);
- the coda, bars 89-92 (Vln I, Vla, Vc and Cb at 292).

**Measured:** in each note's 0.05 s envelope, I removed the 3 s trend and took the autocorrelation (`loops.py`):

| Note | Patch | Pulse p-p | Period | Autocorrelation |
|---|---|---|---|---|
| Cb 220 | Sus MAX | 5.8 dB | 3.95 s | 0.75 |
| Cb 271 | Sus MAX | 12.4 dB | 3.95 s | 0.71 |
| Cb 292 | Sus MAX | 11.8 dB | 4.00 s | 0.65 |
| Vc 274 | Sus MAX | 7.2 dB | 3.95 s | 0.51 |
| Vc 292 | Leg Slur MAX | 9.9 dB | 3.95 s | 0.71 |
| Vln I 292 | Leg Slur MAX | 10.5 dB | 3.95 s | 0.65 |
| Vla 292 | Leg Slur MAX | 8.5 dB | 3.95 s | 0.39 |
| Vln I 0 | Leg Slur MAX | 12.0 dB | 3.95 s | 0.45 |

- The period is sample time, not musical time:
  - It is 3.95 s in every note.
  - The bars there last 3.4-6.3 s.
  - It was already 3.95 s in the c00 render (`loopc.py`), on a different tempo map, mic set and reverb.
- CC11, CC1 and the volume envelope are flat during these notes. For example, Cb 220 holds CC11 32-34 and vol +4..+2. So the pulse comes from the samples.
- The dips recur at fixed times after each note starts (`loopdips.py`). Cb 220 dips at 4.0, 7.95, 11.9, 15.9 and 19.85 s. Folded over one period, the cycles correlate 0.65-0.90 with each other.
- The pattern repeats from render to render. On the same notes, the detrended c08 and c15 envelopes correlate 0.97 (Cb 292), 1.00 (Vln I 292), 0.91 (Vc 292), 0.78 (Cb 220) and 0.71 (Vla 292) (`loopdet.py`).
- **The master** (`bandloop.py`, 3 s detrend):

  | Bars | Band | Pulse p-p | Period | Autocorrelation |
  |---|---|---|---|---|
  | 89-92 | full band | 5.8 dB | 3.95 s | 0.60 |
  | 89-92 | 30-200 Hz | 13.9 dB | 3.95 s | 0.70 |
  | 82-87 | 30-200 Hz | 10.4 dB | 4.00 s | 0.40 |
  | 65-70 | 30-200 Hz | 7.1 dB | 3.95 s | 0.61 |

  In the coda, the Vln I and Vc dips both fall at 2.75 s and 6.7 s after qn 292.

**What a listener hears (inferred):** the score marks these notes "change bow at will", ppp/pp, which asks for a seamless held sound. The render plays them with a regular swell and sag every 4 s. It is most exposed on the final chord and in the bass pedal of bars 82-87.

**Fix: new `build/loop_fills.json`, applied by `score_to_parts.py` through `vol_bp`** (the same envelope path as `early_fills`):
- Format: `{track: {sq: [[t_s, dB, width_s], ...]}}`. `t_s` is measured from the moved note start (`n["qn"]`).
- Each entry is a raised-cosine bump: 0 at t - width, the full dB from t - width/2 to t + width/2, and 0 at t + width.
- Use 80% of the measured depth, capped at +6 dB. Apply it only on string tracks, on notes of 6 s or more.
- Starting values (dips of 3.5 dB or more from `loopdips.json`, already at 80%):
  - Double basses:
    - 220: [7.95, 3.0, 0.3], [11.9, 2.9, 0.35], [15.9, 3.1, 0.35], [19.85, 3.0, 0.3]
    - 271: [2.45, 3.6, 0.35], [3.75, 4.5, 0.85], [6.45, 5.0, 0.35], [7.75, 3.8, 0.4], [10.4, 5.0, 0.4], [11.7, 3.7, 0.45], [14.4, 4.9, 0.35], [15.65, 4.2, 0.8]
    - 292: [4.1, 6.0, 0.55], [8.05, 6.0, 0.45], [11.45, 5.7, 0.4], [12.1, 6.0, 0.6], [15.4, 5.5, 0.4], [16.1, 5.0, 0.5]
  - Violoncellos:
    - 274: [3.35, 3.5, 0.35], [5.1, 3.0, 0.6], [7.3, 3.1, 0.3], [9.05, 3.0, 0.6]
    - 292: [2.75, 3.0, 0.45], [3.95, 3.8, 0.5], [6.7, 3.3, 0.55], [7.9, 3.7, 0.5], [10.65, 3.2, 0.4], [11.9, 3.8, 0.5], [13.55, 5.3, 0.55], [15.85, 3.2, 0.4], [17.5, 3.4, 0.35]
    - 164: [2.05, 5.4, 0.75], [4.75, 4.6, 0.45], [6.05, 5.5, 0.7]
  - Violins I:
    - 292: [2.75, 4.7, 0.5], [4.45, 3.2, 0.35], [6.7, 4.8, 0.45], [8.4, 3.7, 0.35], [10.7, 3.4, 0.55]
    - 0: [3.2, 3.3, 0.65], [4.85, 4.6, 0.35], [8.8, 3.5, 0.3]
  - Violas: 292: [12.6, 2.9, 0.65]

Some Vln I coda dips (3.6, 8.35 and 12.35 s) are the printed bow-change notches at 295, 298 and 301, not loop seams. The fill shortens them as well. That is acceptable at ppp.

**Caveats:**
- The table is valid only while these tracks' Opus states (patch, mics, reverb) are unchanged. After a full rebuild of a track, re-measure it with `loopdips.py`.
- The fill acts on the whole track. That is safe here, because each of these notes sounds alone on its track.

**Check:**
- `loops.py`: residual p-p 5 dB or less and autocorrelation under 0.3 for every listed note.
- `bandloop.py Master 292.5 303.5 30 200`: p-p from 13.9 to 7 dB or less.
- Bar RMS of bars 82-92 within ±0.7 dB of c15.

## 2. Violins II "div., sul tasto" dyads, bars 37-40: the pad still drops 9-11 dB for about 1 s after three of the six chord changes. Measured. The divisi patch option is inferred.

**Score:** qn 108-124. Vln II "senza sord., div., sul tasto", pp, half-note dyads under the flute solo.

**Data (c15 `FLAUT_JOIN_TRACKS`):**
- Flautando, v41, CC11 constant.
- Moving voices start 0.15 s early (`FLAUT_LEAD_S`).
- The old moving notes end at the new onset + 0.35 qn (`FLAUT_OVERLAP_QN`).
- Common tones are merged.

**Measured (10 ms frames, 60 ms smoothing; the level before each change against the trough after it):**

| Change (qn) | Trough | Back within 2 dB |
|---|---|---|
| 112 | -8.9 dB at +0.20 s | +1.28 s |
| 114 | -10.4 dB at +1.41 s | +1.71 s |
| 120 | -10.6 dB at +0.90 s | +1.31 s |
| 116 | -5.2 dB | |
| 118 | -3.4 dB | |
| 122 | -2.8 dB | |

Each chord lasts 2.0 s, so after 112, 114 and 120 the pad spends most of the chord in the trough.

**Per voice** (`pitchtrack.py`, energy at the fundamental and second harmonic):
- qn 114: the new Bb3 (58) needs about 0.6 s to rise, and then sits 12-15 dB under the C#4 (61) it replaces. Flautando Bb3 is a weak note in this patch.
- qn 120: the old C#4 has faded by +0.9 s, but the new Eb4 (63) reaches its body level only at +1.1-1.3 s. Flautando blooms in about 1.2 s, as c14 measured, and the 0.15 s lead covers only a small part of that.

**What a listener hears (inferred):** the pad under the flute solo swells and fades with every half note. A real section's sul tasto dyads change without a gap.

**Fix A (data only, `score_to_parts.py`):**
- `FLAUT_LEAD_S` 0.15 -> 0.45 s.
- `FLAUT_OVERLAP_QN` 0.35 -> 0.7.
  - Flautando is not a legato patch, so the overlap is safe.
  - The new note is still in its slow attack, so the extra overlap should not sound early (inferred).
- `build/roles.json` Violins II [114, 116, 3]. The volume is track-wide, so this lifts the Bb3/Db5 dyad as a whole.

**Fix B (patch, if A leaves a trough of more than 5 dB):**
- "div." is printed, and the render plays each voice with the full 2nd Violins section. HO has `2nd Violins Divisi/01 Long/2nd Violins Flautando DIV A.oib` and `... DIV B.oib`. The DIV A patch has only the Close mic, like the c10 solo violin and c13 Vc div tracks.
- Route the upper voice of qn 108-124 to a new "Violins II div A" track and the lower voice to "Violins II div B" (stems 30 and 31), with `TRACK_SPLITS` by pitch rank.
- Each half-section voice then gets its own CC11 and volume, so the Bb3 can be lifted by itself (start at +6 dB).
- Only one articulation is loaded per track, so the memory cost is small.

**Check (`rebow.py 3`):** no Vln II trough of 5 dB or more at 112-122, and the Vln II RMS over 108-124 within ±1 dB of c15 (-49.2).

## 3. Viola sextuplets, bars 59-60: the Detache revert needs a full Violas rebuild. Use that rebuild to test the KS Master's "Stac Leg BC + Slur + Port MAX" row, the one viola patch not tried yet. The baseline is measured; the benefit is inferred.

**Status:**
- Bar 59 on Detache: own-pitch share 0.32, the same as the bar 60 Sus MAX control (c15 CHANGES).
- c14 Leg Slur MAX: 0.03.
- HO has no viola runs patch.

**Patch:**
- The Violas KS Master has a row "Stac Leg BC + Slur + Port MAX" (key 44, in `ks_maps.json`). It is the KS version of `Violas/04 Legato Slur + Port/Violas Stac Leg Slur + Port MAX.oib`.
- That patch contains separate short-attack groups ("1V pp..ff" with release-trigger groups) next to the true-legato transition groups ("TLeg"). It is built for short connected notes.
- It is the remaining candidate between Leg Slur (too slow at 0.157 s per note) and one-bow-per-note sustains (Sus MAX, Detache).

**Fix (`score_to_parts.py`):**
- Set `DETACHE_SPANS = {}` as planned.
- Add a `STACLEG_SPANS = {"Violas": [(196, 200)]}`:
  - Notes in it play `ks_lookup(stem, "Stac Leg BC + Slur + Port MAX")`.
  - Each note overlaps the next by 0.02 qn, inside each printed slur (6 notes).
  - v110 at f. No lead.
- Bar 60 stays on Sus MAX as the control.
- The rebuild that unloads Detache loads this row, so the test costs no extra rebuild.

**Check (`dom.py Violas 196 200 15` against `200 204`):**
- Pass: own share 0.5 or more in bar 59, first dominance no later than +0.06 s, and bar RMS within 1.5 dB of bar 60.
- Fail: close the item for good.

## 4. Bar 80 (qn 265-266), Violins I and II: the up-bow on the tied B flat and the slur that follows are rendered as two bow changes, with a vibrato restart on the slurred note. Measured, small. The effect is inferred.

**Score (aTwo.ily):**
- `bes'''2.)~\ff | bes'''4(\upbow aes'''2)` in Vln I, and the same an octave lower in Vln II.
- There is one new bow at 265, on the tied note. The A flat at 266 is slurred to it.

**Data:**
- The tie is merged into one note from 262 to 266, with a 15 CC notch at 265 (CC11 115 -> 100 -> 114 over 0.25 qn).
- The slur starts inside the merged note. `tieslur.py` finds that the join to 266 is treated as slur-to-slur, so it plays Leg BC MAX on Vln I and Vln II.
- The violas, with the same marks, get Leg Slur MAX at 266.
- Vln I's CC1 also drops from 105 to 85 at 266 and ramps back over 0.8 qn, a delayed-vibrato restart on a slurred note.

**Measured (RMS):**

| Window (qn) | Vln I | Vln II | Violas | Master |
|---|---|---|---|---|
| 264.3-264.95 | -29.0 | -28.4 | | -20.8 |
| 265.1-265.8 | -30.7 | -32.6 | | -22.0 |
| 266.05-266.45 | -27.9 | -30.1 | -33.4 | |

- So the notch costs 1.7 dB (Vln I) and 4.2 dB (Vln II) for about 0.7 s, and the master 1.2 dB.
- Vln I gets a Leg BC bump at 266 that the violas do not have.

**What a listener hears (inferred):** in the second bar of the climax, the top note sags just after the bar line, then the A flat is re-bowed and loses its vibrato for a moment. Two small breaks where the score asks for one bow change.

**Fix (`score_to_parts.py`):**
- In the slur assignment, a slur that starts on a tied continuation belongs to the merged note. The join from that note to the next one is then inside the slur, so 266 plays Leg Slur MAX, as on the violas.
- The notch for a printed bow mark inside a held note at f or louder: 14 -> 6 CC. The mark asks for a bow change on a held ff note, which a section makes nearly inaudible.
- No CC1 drop on a legato target that is inside the same slur as the previous note at f or louder.

**Check:** Vln I/II 265.1-265.8 within 1.5 dB of 264.3-264.95, and no rise of more than 2 dB at 266.

## 5. Largamente joins (bars 61-62): the remaining per-track falls come from the samples, not from the data, and the tutti no longer falls. Stop tuning them, except Flute 2's notch. Measured.

**Data at qn 206/208/210 (`sostcause.py`):**
- Every swell_sost track changes CC11 by 3 CC or less at the onset (122 -> 119; brass 96 -> 93).
- The volume step is at most 1.5 dB.
- The one exception is Flute 2. Its Leg Slur targets carry `SOST_NOTCH` 10 on top of the swell contour, so CC11 goes 122 -> 109 at every onset.

**Measured (0.55 s before against 0.55 s after each onset):**

| Track | 206 | 208 | 210 |
|---|---|---|---|
| Fl2 | -0.8 | -3.8 | -6.7 |
| Ob1 | | -5.1 | +4.9 |
| Bn2 | | +3.4 | -5.4 |
| Cb | | -5.2 | +0.8 |
| Vln II | | -5.6 | +2.6 |

- The same track rises at one onset and falls at the next, with the same data shape. That is sample-to-sample variation.
- The master steps at 206/208/210 are +0.5/-0.4/-0.4 dB (c15 CHANGES), so the tutti holds its weight.

**Fix:**
- Exempt Flute 2 from `SOST_NOTCH`, or set the notch to 0 for wind Leg Slur targets that are inside `SOST_HOLD_THROUGH`.
- Then close the item. Per-onset fills here would chase round robins.

## 6. Bassoon repeats at qn 21, 22 and 32 still open with holes from the failed `ABUT_LEAD` test. Measured; the revert is already planned.

`rebow.py` on c15:
- Bn1 22: 10.3 dB for 0.10 s.
- Bn1 32: 15.1 dB for 0.10 s.
- Bn2 21: 8.9 dB for 0.13 s.

These sit under the horn solo of bars 8-11. `ABUT_LEAD = {}` removes them.

Check: c14 had 3 dB at these onsets.

**Do not touch:**
- Tie handling and the timpani tie strokes.
- Keyswitch placement.
- The legato lead tables, `LEG_ART_EXTRA_S`, `LEG_SOFT_EXTRA_S` and `leg_leads.json`.
- `BC_SOFT` / `BC_SOFT_SKIP` and the halved notches.
- `SOST_HOLD_THROUGH`.
- The Vc fills 74-249.
- The Tbn1 marcato settings (`MARCATO_SPANS`, `MARC_ACC_CUT_AT`, `MARC_ATTACK_S`, `ACCENT_DB_AT`).
- Pizzicato velocities and step trims.
- Harp rolls, ringing and the harmonics track.
- Tremolo handling in bars 61-64.
- CC15 mute placement.
- The phrase-end releases and breath gaps.

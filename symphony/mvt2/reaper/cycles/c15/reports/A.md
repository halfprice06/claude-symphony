# Cycle 15, critic A: articulation and phrasing (on the cycle 14 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c15-A/`. They are the c14-A set plus `sost.py` (the level step at each note change in bars 61-62), `rebow.py` (troughs after non-legato re-attacks) and `breath2.py` (gaps at printed breaths). `ends.py` now reads `$CYC`. Run them with `CYC=14 ~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c14 stems, measured from score onsets (`sq`). `build/parts.json` (19:00) is the data that made the c14 render.

## Checked and working (measured)

- No chord goes to a legato patch (`chords_leg.py`).
- All 104 ties are held. The only two "re-attacks" are the intended `TIMP_TIE_STROKES` at 203 and 211 (`ties.py`).
- Keyswitches: every one lands at least 20 ms before its note, except the known Ob1 207.952 (13 ms) (`kscheck.py`).
- Slur overlaps: the only re-attacks inside slurs are the six intended ones listed in c14 (`slurov.py`).
- Mutes: CC15 changes all fall in rests, and match every con sord./senza sord. text, including Vln I "gli altri con sord." from 65 to 171 and the Vc div track.
- Phrase-final releases: the median taper is 1-6 dB per track, and releases reach -15 dB in 0.12-0.6 s. No phrase end is cut off or faded to nothing unless a hairpin is printed (`ends.py`).
- The bar 78 grace runs sound: own-pitch share 0.24-1.0 per 90 ms grace, and 0.97 on the target (`dom.py`, Vln I/II and Fl1 261-262.5).
- Tremolo, bars 61-64: no holes beyond the known Vc 212 probe.
- The timpani roll at 203 now ends in a stroke, +6.4 dB.
- Legato joins: the median dip is 1.9-3.7 dB on every legato track (`wjoin2.py`). The 6-8 dB joins vary from render to render with the round robins. The joins in finding 2 do not.

## 1. Bars 61-62 (Largamente, molto sostenuto, tenuto half notes): the c14 sostenuto ramp puts the weight at the end of each note, and every new chord falls back. Measured.

**Score:**
- qn 204-212. Winds, brass and strings play tenuto half notes ff (Fl2, Cl1, Vln II and Vc at 206; nearly all of them at 208 and 210).
- Tenuto asks for full value and even weight. The new note should arrive with at least the weight of the old one.

**Data:**
- `score_to_parts.py`, c14 C #4 block (about line 1767): each `swell_sost` note gets the volume points (a, 0), (x40, 0), (next onset - 0.25 qn, +2.5), (next onset, 0). The +2.5 dB is removed exactly as the next note starts.
- Some tracks fall further at the same instant:
  - Clarinet 1, qn 206: vol_db goes from +14.5 to +5.9 dB. The Ab4 `_all_arts` pitch trim (+6) and the hpgain release both end at that onset.
  - Horn 3, qn 208: vol_db goes from +6.5 to +1.0.

**Measured (`sost.py`: median level 0.1-0.35 s before each onset, against 0.1-0.5 s after it, 50 joins):**

| | c13 | c14 |
|---|---|---|
| Median step at the onset | +1.1 dB | -1.6 dB |
| Joins that fall 4 dB or more | 2 | 13 |

- The c14 joins that fall:

  | Track | Onset (qn) | Step (dB) |
  |---|---|---|
  | Fl2 | 206 / 208 / 210 | -8.2 / -5.1 / -5.7 |
  | Cl1 | 206 | -7.5 |
  | Cb | 208 | -7.6 |
  | Vln II | 208 | -6.9 |
  | Bn2 | 210 | -6.8 |
  | Hn3 | 208 / 210 | -6.2 / -5.4 |
  | BCl | 208 | -6.2 |
  | Tuba | 208 | -5.9 |
  | Ob1 | 208 | -4.8 |
  | Vc | 206 | -4.3 |

- Master, 50 ms frames: in c14 the tutti reaches -17.0 dB 0.25 s before the bar 62 downbeat (qn 208) and sits at -19.9..-20.5 for 0.5 s after it, about 3 dB lower. In c13 the downbeat was as loud as the end of bar 61 or louder (-20.0 before, -19.7..-20.7 after).

**What a listener hears (inferred):** each Largamente chord swells into the bar line and the new chord drops away. That is a pumping, the reverse of tenuto weight. It is most exposed at the bar 62 downbeat.

**Fix (`tools/score_to_parts.py`, the swell_sost block):**
- When a `swell_sost` note is followed by another `swell_sost` note on the same track with no rest:
  - Hold the ramp at +SOST_SUSTAIN_DB through the next onset: (next onset - 0.25 qn, +2.5), (next onset + 0.25 qn, +2.5).
  - Release it to 0 at 40% of the next note, where that note's own ramp starts.
- Keep the current drop to 0 only before the last note of the span, or before a rest.
- Clarinet 1 at 204: give the Ab4 +6 a `{"early", "body"}` shape, or list 204 in `_skip_onsets`, so 206 does not fall 8.6 dB in vol_db.

**Check (`sost.py`):**
- The median step at the onset is 0 dB or more, and no join falls 3 dB or more.
- In the master, the 0.5 s after qn 206, 208 and 210 is no lower than the 0.35 s before each onset.
- Bar 61 RMS rises no more than 0.5 dB (it is -17.7 now), and the mp3 limiter stays at 3 dB or less.

## 2. The cello cantabile countermelody (bars 25-28 and the reprise in bars 73-76): five legato targets start 5-8 dB under both neighbours for half a second. c14's note trims made two of them deeper. Measured.

**Score:** Vc "unis., cantabile", p/mp, slurred half and quarter notes. qn 74 (Ab3 to C4), 75 (C4 to Bb3), 246, 247, 249 (Bb3 to G3).

**Data:** `note_trims.json` Violoncellos 74 +4 / 246 +4 (c14 B #2). Note trims ramp in over 0.6 s (a do-not-touch rule), so the trims lift the bodies but not the joins. There are no early fills at these onsets (the fills are at 68, 77, 78 and 86).

**Measured (10 ms frames; mean of the first 0.5 s after the onset, against the previous note's end and the new note's body):**

| qn | Previous end | First 0.5 s | Minimum | Body |
|---|---|---|---|---|
| 74 | -43.7 | -49.4 | -55.5 at +0.06 s | -41.6 |
| 75 | -42.7 | -51.3 | -55.5 at +0.11 s | -43.1 |
| 246 | -43.4 | -47.1 | -55.0 at +0.00 s | -41.3 |
| 247 | -42.2 | -49.1 | -53.3 at +0.05 s | -42.0 |
| 249 | -43.4 | -49.4 | -54.4 at +0.12 s | -43.1 |

- `wjoin2.py`, Vc joins of 8 dB or more: c13 2, c14 6.
- 74 went from under 5 to 8.3 dB, 246 from under 5 to 8.8, 75 from 8.0 to 10.0, and 247 from 5.7 to 9.4.
- These are not the envelope: the pre-fader dips are the same size.

**What a listener hears (inferred):** in the line that answers the violin tune, the first beat of each slurred note sags and then blooms, like a swell on every note.

**Fix (`build/early_fills.json`, Violoncellos):**
- 74 {db 5, pre_s 0.05, hold_s 0.35}
- 75 {db 6, pre_s 0.05, hold_s 0.40}
- 246 {db 4, pre_s 0.05, hold_s 0.35}
- 247 {db 5, pre_s 0.05, hold_s 0.40}
- 249 {db 5, pre_s 0.05, hold_s 0.35}

These are about 80% of the measured hole. The 74/246 note trims stay.

**Check (`wjoin2.py Violoncellos -v`):**
- Joins of 8 dB or more: back to 2 or fewer.
- No first 0.5 s more than 2 dB over its body (c11 showed that plain fills can overshoot).

## 3. Violins II sul tasto chords, bars 37-40 (qn 108-124): every half-note chord change leaves a 10 dB trough 0.4-0.55 s after the beat. Measured, the same in c13.

**Score:** Vln II "senza sord., div., sul tasto", pp, unslurred half-note dyads under the flute solo. Common tones: Db5 (66) through 112-118, C#4/Db4 (61) at 116-118.

**Data:**
- Flautando, v41, CC11 33-38.
- Each dyad ends 0.03 qn before, or exactly at, the next score onset.
- No lead (`ENTRY_LEAD_S` applies only after a rest).
- Same-pitch common tones are re-attacked.

**Measured (`rebow.py`, 10 ms frames):**

| qn | Trough | Time below -6 dB |
|---|---|---|
| 112 | -11.0 dB at +0.44 s | 0.47 s |
| 118 | -10.0 at +0.54 | 0.25 s |
| 120 | -10.1 at +0.55 | 0.36 s |
| 114 | -7.2 | |

- In 50 ms frames, each chord falls from about -50 to -60 dB and needs about 1.4 s of its 2 s to get back to -48. The Flautando sample blooms slowly: after the rest at 108 it took 1.2 s to reach -48.
- c13 shows the same troughs (10.2, 7.5, 7.9, 8.5 and 9.4 dB).
- No other non-legato pad in the movement has a trough later than 0.25 s.
- At -50.4 dB, Vln II is the fourth loudest stem in these bars (master -40.9).

**What a listener hears (inferred):** the pad that should hold still under the flute breathes in a slow "wah" on every half note.

**Fix (`tools/score_to_parts.py`, the DIV_JOIN branch, about line 1316):** extend it to `tname == "Violins II" and n["art"] == "Flautando"` after a Flautando chord with no rest.
- Merge same-pitch common tones into one held note. A pp sul tasto bow change is barely audible; at most, add a 4 CC notch.
- The moving voices start 0.15 s early. The old chord's moving notes end at the new score onset + 0.35 qn (new constant `FLAUT_OVERLAP_QN`). Flautando is not a legato patch, so the overlap is safe.

**Check (`rebow.py 4`):**
- No Vln II trough of 4 dB or more at 112-122, and no time more than 6 dB under.
- The Vln II RMS over 108-124 is within ±1 dB of c14 (-50.4).

## 4. Trombone 1's marcato line (bars 63-64): the accented top note has almost no accent, and the Marc Lng notes still have no attack. Measured.

**Measured (`tbn.py`; peak in the first 0.12 s against the median body, 0.15-0.6 s):**

| Note | Patch | Peak over body |
|---|---|---|
| 212.5 | Sus Accent | +3.0 |
| 213 (C4, `c'4.->`, the line's peak) | Sus Accent | +1.2 |
| 218 | Sus Accent | +3.8 |
| 214.5 | Marc Lng | +0.1 |
| 215 | Marc Lng | +2.4 |
| 215.5 | Marc Lng | +0.9 |
| 216 | Marc Lng | -2.0 |
| 217 | Marc Lng | -1.3 |
| 217.5 | Marc Lng | +3.9 |

- The 213 accent is under Dan's 2-4 dB.
- The Marc Lng samples reach their level at +0.08 to +0.11 s.
- The c14 attack bump (10 ms rise, held 0.08 qn, about 0.09 s) is mostly over before the sample speaks.
- 214.5 has no separation: the stem is -26.9 dB just before it and -27.0 in its body, because 213 ends only 0.1 qn (0.11 s) early and its release fills the gap.

**What a listener hears (inferred):** the climax of the quotation (the dotted C4) and the B3 after it run together, and the marcato reads as a slightly detached legato.

**Fix (`tools/score_to_parts.py`):**
- `ACCENT_DB_AT` Trombone 1 213: +3 dB, with the same shape as 218.
- End 213 at 214.25 (0.25 qn early), so the break before 214.5 is about 0.27 s.
- Move `MARC_ATTACK_DB` to where the sample peaks, and make it +3 dB: 0 at the onset, +3 at onset + 0.04 s, held to + 0.16 s, 0 by + 0.30 s.

**Alternative, if Marc Lng still has no peak:** test the 1TB KS Master row "Marc Sus LITE" (key 31) for the six notes. It is a marcato attack on a sustain. Loading the row changes the Opus state, so Trombone 1 needs a full rebuild.

**Check (`tbn.py`):**
- 213 and every Marc note peak 2-4 dB over their body within 0.15 s.
- The level just before 214.5 is at least 6 dB under the 214.5 body.
- No peak exceeds the 212.5 accent.

## 5. The viola sextuplets of bars 59-60 are still a smear. A Detache test is proposed (the remaining patch option). Measured, with an inferred benefit.

**Measured (`dom.py`, median own-pitch share of each note's slot):**

| Passage | Articulation | Own share |
|---|---|---|
| Bar 60 sextuplets | Sus MAX | 0.29 |
| Bar 59 (the c13 splice) | Sus MAX | 0.33 |
| Bars 57-58 triplets | Leg Slur MAX | 0.78 |

Leg Slur MAX failed on the sextuplets in c14 (0.03).

**Proposed patch:**
- The Violas KS Master has a "Detache" row (key 30, not loaded by default; HO manual p. 54 lists it with the long articulations).
- At 0.157 s per note, a one-note-per-bow sustain with a defined attack is the closest playable stand-in for a slurred f figure, short of a runs patch. HO has slur runs only for violins.

**Fix (an A/B inside the next render):**
- In `score_to_parts.py`, put Violas notes with `sq` in [196, 200) on `ks_lookup(stem, "Detache")`: v100, written length + 0.01 qn, no lead.
- Bar 60 stays on Sus MAX as the control.
- Loading the row needs a full rebuild of Violas only.

**Check (`dom.py Violas 196 200 14` against `200 204`):**
- Bar 59 has an own share of 0.5 or more, and no first-dominance later than +0.06 s.
- Bar 59 RMS is within 1.5 dB of bar 60.
- If it passes, extend to bar 60. If not, close the item.

## 6. Horn 1's breath before bar 59 (qn 196) is not heard. Measured, and open since c13.

**Data and measurement (`breath2.py`):**
- 195 ends at 195.7, so the gap is 0.284 s.
- The stem's minimum in the gap is -43.6 dB against a body of -41.7: a 1.9 dB dip. The horn release fills it.
- The other 27 printed breaths dip 12-38 dB.

**Fix:**
- `score_to_parts.py`: end Horn 1's 195 at 195.5.
- Add a 10 CC fall over its last 0.2 qn.
- No caesura: the breath is the horn's own, and the strings carry on.

**Check:** a dip of 8 dB or more before 196, and the 196 attack gate stays ok.

Delivery numbers for reference (c14, not under this lens):
- Master: -23.8 LUFS, LRA 23.5, true peak -4.5.
- mp3: -19.8 LUFS, LRA 16.0, limiter 2.0 dB.

**Do not touch:**
- Tie handling and the timpani tie strokes (+6.4 dB at 203).
- Keyswitch placement.
- The legato lead tables, `leg_leads.json`, BC_SOFT / `BC_SOFT_SKIP` and the halved notches.
- The grace-run timing (`GRACE_S`).
- Viola triplets on Leg Slur MAX.
- Pizzicato velocities and step trims.
- Harp rolls and ringing.
- Tremolo handling in bars 61-64.
- Mute (CC15) placement.
- The phrase-end releases.
- The Tbn1 accent shapes at 212.5 and 218.
- `mute_eq` for Horns 3-4.

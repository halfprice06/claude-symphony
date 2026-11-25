# Cycle 11, critic A: articulation and phrasing (render c10, score v600)

Method. All numbers come from the c10 render after its stem fix (`cycles/c10/render/`: dry stems 01-31, returns 32-35, `00_Master.wav`), the delivered `mvt3-mockup-c10.mp3`, and the data that made it (`cycles/c10/rendered_build/parts.json`, `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py`, `tools/build_reaper.py`). Times use the parts.json tempo map (`tools/pcx.py` TM). My scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c11-A/` and were deleted after the report. "Measured" means a number from the render, the data or a patch map. "Inferred" means reasoned but not tested. Measures used:
- **Repeat dip (S1).** The c10 method: in a band around the onset, min(peak in the 0.2 s before the moved onset, peak in +0.03..+0.25 s) minus the minimum in ±0.06 s. The band is either the note's harmonic band (`pcx.band_env`) or, for the basses, 30-120 Hz (2048-point FFT, 2 ms hop).
- **Join time (S2).** `pcx.attack_pcx` / `pcx.scan` relative to the score onset.
- **Brass accent tilt jump.** On the master: 2-5 kHz over the first 80 ms minus the 200 ms before, minus the same jump at 0.25-1.5 kHz (LEARNINGS c08).

## Manual notes (cycle 11, slot A: second reading of 2021 manual PDF pages 160-162 and 188-190, read in full)

The first reading is `cycles/c05/reports/A.md`. These pages describe the Opus articulation window and the Zones window. They are UI pages, so the text was enough; I did not render the screenshots. Each c05 note is checked against c10 below. I also read p.101-103 (brass long and short articulations) for finding 2.

| Manual (PDF page) | Where it applies | c05 status | c10 status |
|---|---|---|---|
| p.160: each articulation cell has a load switch; KS Masters trigger rows by keyswitch | `build_reaper.py` loads only the rows a track uses | yes | **Yes (measured).** Every keyswitch goes to a row in the track's `art_counts`. c10 loaded one more row (Bassoon 1 "Leg Slur Exp", key 77), and REAPER stayed at 45 GB settled. |
| p.161: keyswitch notes lie outside the playable range | KS Masters whose keys are inside the range (basses, celli, 1TB, contrabassoon) | yes | **Yes (measured).** No played note on any of the 31 tracks lands on a key of a row its track uses. One side note: the EH KS Master names its sustain row "Sus Max" (lower-case "ax"), and the tools send key 24 correctly. A rule that matches the name "Sus MAX" exactly, such as mix.json `sus_release_cap_ms` "rows", would miss it. No wind track has a cap today, so this has no effect now. |
| p.161, p.189: Keyswitch Range, Program Change | | not used | Not used. Not needed. |
| p.162, p.190: Controller trigger (a CC value range selects a row) | CC1 lanes | yes, plain key triggers only | **Yes.** No CC switches a row. CC1 is the layer or vibrato crossfade only. |
| p.162, p.189-190: velocity-range trigger; a short accent at v110-127 layered over a sustain | the sfp at qn 592 (finding 2); brass accents | not used, not needed | **Not usable for the sfp (inferred from MIDI rules), not needed for accents (measured).** Inside one instance, the layer's note-off for the same key also ends the sustain, and a v110-127 layer would also fire under the v110-111 legato targets and sfp attacks the tools already write. The manual's single-note answer for an sfp is the Sustain Accent row (p.101: velocity sets the accent, the Mod Wheel sets the sustain); see finding 2. Accents elsewhere do not need a layer: the tilt jump on 98 brass accents has median -0.5 dB, p90 +2.8 and maximum +8.0; on the brass heads of 247-262 (16 accents) the median is -1.1 and p90 +2.2. Front minus body is median -7.1 dB. Nothing bites. |
| Exclusive keyswitch behaviour (via p.160) | row changes while the old row's note still sounds | yes; shortest lead 7.1 ms | **Yes (measured).** 2205 keyswitches. The shortest lead is 7.1 ms (violas' re-bows at qn 176, 181, 426, 556, 559) and the median is 12.5 ms. No wrong-row note was found. The 40-800 ms default stays rejected (c09). |
| p.188: Voice Limit | the harp glissando with the final chord; div. a 3 at 1108 | inferred OK | Unchanged data at 1106-1112. No missing chord tones found (inferred). |
| p.188: Octave, Key Range | Bass trombone B♭1 (MIDI 34) at qn 416 | effectively silent | **Still open (measured in the data):** the note is still MIDI 34, below the 1TB samples (MANUAL-GAPS #13). Not ranked: one note in the stringendo. |
| p.188-190: Zones and Group (several instruments in one instance) | the timpani stick changes (soft 680-712, medium 856-1016) | not used | Not used. A felt zone would load the felt samples in the timpani instance. That costs the same memory as c10's deferred felt alias, so it is no cheaper. |

MANUAL-GAPS items in this lens:
- #5 (expressive rows): first tried in c10. Judged in finding 3: keep, and extend.
- #13 (bass trombone low note): open.
- #12 (crescendo rolls) and #9 (horn portato): open, not ranked.
- New (p.101): Sus Accent MAX for the brass sfp (finding 2). It is not in MANUAL-GAPS yet.

## Standing checks and the coordinator's items

- **Wetness (measured): inside the ceiling, and not too dry.**
  - The final chord falls 6.3 / 11.0 / 14.4 / 18.9 / 22.8 dB at +0.1 / 0.2 / 0.3 / 0.41 / 0.5 s after the written end. So it reaches -20 dB at about 0.43 s (c10 claimed 0.41 s; the recordings give 13-17 dB at +0.3 s).
  - Tutti cut-offs at qn 5 / 21 / 661 / 1113 reach -20 dB 0.39 / 0.38 / 0.38 / 0.36 s after the last point within 3 dB of the held level. Measured from the written cut-off: 0.48 / 0.45 / (661 is held past the beat) / 0.42 s.
  - That is the dry end of the recordings (0.43-0.58 s from the written end) but inside them. Do not shorten further.
- **Loops (item 7, measured).** Master 100-300 Hz band and spectral centroid folded at 3.95 s:
  - chorale 888-936: +0.01 / -0.03;
  - final bars 1088-1112: -0.12 / +0.17.
  - No pulsing.
- **String re-bows in the chorale and the last bars (measured).** One hole: Violoncellos at qn 919.963 dip 10.1 dB for about 60 ms (+0.04..+0.12 s). The fitted fill (`build/rebow_fills.json` "Violoncellos" "919.963") is still at -4.4..-2.4 dB there and peaks +6.5 dB at +0.2 qn, after the hole. Refit this one entry with `fit_rebows.py` on c10, or move its rise about 0.1 qn earlier. The other three celli re-bows dip 3.2-3.3 dB.
- **Pizzicato 51-66 (measured):** attack medians Vln II +11, Vla +15, Vc +12, Cb +3 ms. Good.
- **Muted Trumpet 1, 171-198 (measured):** 22 note changes on Mute Sus dip a median 3.0 dB (p90 6.3). The open solo's Leg Slur joins in 51-66 dip 2.9 dB (p90 5.2). The non-legato mute row joins as smoothly as the legato row.
- **Delivery (measured on the mp3, plain RMS per bar; C's lens, reported because the coordinator asked):**
  - Bar 41 to 42: the f -> p drop is 6.6 dB (master 9.1).
  - Bar 42 to 43: flat (master -2.4).
  - Bars 273-278: -18.9 / -19.4 / -19.1 / -18.8 / -16.8 / -15.4 dB. The mp3 rises from 275 on (+3.7 dB over 275-278, master +4.2).
  - Bar 278 is 0.5 dB over 223.
- **315 Hz hump:** not my lens; not measured.

## 1. The basses' downbeats in the hammered eighths have no gap: each up-bow off-beat stroke swells straight into the next downbeat (S1, S2; measured, fix simulated)

**Where.** Double basses, Sus MAX eighths:
- coda bars 199-210 (qn 792-840);
- Più allegro bars 247-270 (984-1088);
- Largamente bars 273-277 (1088-1108).

297 same-pitch repeats. Only the basses play repeated eighths in these spans; every other track has longer notes there (parts.json).

**First, the c10 target was measured in the wrong band (measured; reject with these numbers in LEARNINGS).**
- c10 concluded that celli, timpani, tuba and the returns fill the basses' 63 ms gaps in the master. That conclusion rests on the harmonic-band dip: harmonics 2-8 of MIDI 29-41, which is 90-580 Hz.
- I subtracted stems from the master and re-measured. Removing celli, tuba, contrabassoon, timpani and bass trombone, and then also the R Strings / R Brass / R Perc returns, leaves the master's harmonic-band dip at 2.3 / 3.1 / 2.2 dB in the three spans, against 2.5 / 3.1 / 2.2 with them. So none of these parts fills the gap. That band in the master is dominated by the horns, trombones, violas and winds.
- In 30-120 Hz, where the basses are heard as the bass line, they carry 3.2-5.9 dB of the band's energy, and the master already dips a median 8.9 / 8.4 / 8.5 dB at the repeats. The stem dips 11.5 / 11.5 / 5.1 dB in the same band.
- So the "master harmonic-band median 4 dB" target cannot be met, because other instruments fill that band, and it does not need to be. Use 30-120 Hz for low string repeats.

**What is still wrong: the downbeats (measured).** The weak repeats are the on-beat ones:

| span | stem 30-120 Hz, on-beat / off-beat | master 30-120 Hz, on-beat / off-beat | stem harmonic band, on-beat / off-beat |
|---|---|---|---|
| 792-816 | 7.1 / 9.4 | 7.1 / 9.3 | 3.9 / 6.3 |
| 816-840 | 6.3 / 13.2 | 8.7 / 9.3 | 4.1 / 9.6 |
| 984-1056 | 10.3 / 11.1 | 6.9 / 7.9 | 4.1 / 9.2 |
| 1056-1088 | **2.3 / 12.0** | **4.7 / 12.0** | **0.7 / 11.3** |
| 1088-1108 | 5.1 / 8.1 | 8.5 / 9.1 | 1.5 / 10.0 |

**Cause (measured on the stem at qn 1000, 1060, 1072 and 1092).**
- The down-bow stroke peaks at about +0.08 qn and decays about 10 dB before its note-off, so the gap before an off-beat is a real hole (for example 24 -> 13 dB band level at 1060.0-1060.5).
- The up-bow off-beat stroke does the opposite. It rises from its onset (13 -> 19 dB by 1060.70) and keeps rising after its note-off at 1060.824 (21 dB at 1060.85-1060.96). The downbeat then adds only 3 dB (24 at 1061.10).
- The 63 ms MIDI gap and the 150 ms release cap do not stop that swell. On top of it, the METRIC_BOWED step for the downbeat (+2.5..+5 dB) starts ramping 0.03 s before the onset. Across the gap before a downbeat the envelope rises a median +1.0 dB; before an off-beat it falls 2.3 dB.
- The envelope's change across the gap correlates with the stem dip at r = -0.64 (297 repeats).
- This is also the "long-short lilt" c09 measured as an attack-time swing (-68 ms in 1088-1108).

**Fix (simulated on the c10 stems).**
1. `tools/score_to_parts.py`, STR_REP_DETACH block (about line 5268-5296): add a per-span option `beat_gap_db`. For a pair whose next onset `q1_` is a beat (`metric_kind(q1_)` in "down", "mid", "beat"), add one more exact env item that sits only in the gap. It starts at the moved note-off of the stroke before (its parts.json qn + dur), with points (off, 0), (off + 0.006 s, beat_gap_db), (tb - 0.009 s, beat_gap_db), (tb - 0.003 s, 0), where tb is the next moved onset.
   - It is a volume-envelope dip, so it acts on the release. The basses have no hall send, so no hall tail is cut.
   - It leaves both note bodies alone.
2. `build/score_config.py`: give the spans (792.0, 840.25) and (984.0, 1108.25) in `STR_REP_DETACH["at"]["Double basses"]` the option `{"beat_gap_db": -9.0}`. Keep the existing -3 dB dip.
3. Same file, METRIC_BOWED block (about line 4870): for REP_SPLIT strokes inside a STR_REP_DETACH span, start the step at the moved onset, (q0, 0) -> (q0 + 0.010 s, v_), instead of (q0 - 0.03 s, 0) -> (q0 - 0.01 s, v_). Otherwise the downbeat's step lifts the previous stroke's tail.

**Simulation.** I multiplied the basses stem by the gap dip in every gap before a beat (6 ms ramps) and rebuilt the master as master - stem + new stem.

| span | master 30-120 Hz on-beat dip, now -> -9 dB | stem 30-120 Hz on-beat dip, now -> -9 dB |
|---|---|---|
| 792-816 | 7.1 -> 9.7 | 7.1 -> 14.7 |
| 816-840 | 8.7 -> 9.2 | 6.3 -> 10.2 |
| 984-1056 | 6.9 -> 7.9 | 10.3 -> 18.8 |
| 1056-1088 | 4.7 -> 11.3 | 2.3 -> 7.3 |
| 1088-1108 | 8.5 -> 9.0 | 5.1 -> 10.5 |

- Off-beat dips are unchanged.
- The basses' span level falls 0.3 dB, because only the gaps change.
- At -6 dB the 1056-1088 master on-beat dip is 9.4. At -12 dB it is 12.0.

**Targets.**
- 30-120 Hz on-beat master dips of 8 dB or more in every span, and on-beat within 3 dB of off-beat.
- On-beat minus off-beat attack time within ±12 ms (pcx).
- Down minus off level (first 120 ms) unchanged at +2..+4 dB. The stroke bodies do not change, so no metric-table refit is expected.
- Record the band lesson in LEARNINGS.

## 2. The brass "sf" of the sfp at qn 592 (bar 149) is a slow swell that peaks after the fall has begun; the library's Sustain Accent row is the printed articulation (measured problem; inferred fix; manual p.101)

**Where.** The sfp chord at qn 592: Horns 1-4, Trumpets 1-3, Trombones 1-2, Bass trombone, Tuba. Tempo there is 167 qpm (0.364 s per qn).

**What is wrong (measured).**
- Every brass note at 592 is a fresh Sus MAX note (Sus Non Vib MAX on the trumpets), led 0.05-0.09 s, at velocity 110-111.
- CC1 is held at 108, the same value as the ff before, until 592.375 (+0.136 s). It then falls to 42 by 592.83 (+0.30 s).
- On the stems, the new note sits under the ff chord before it for the first 0.1 s, and peaks only when CC1 is already falling:

| track | at +0.05 s re ff before | at +0.10 s | peak time |
|---|---|---|---|
| Horn 1 | -3.4 | -1.9 | +0.266 s |
| Horn 3 | -3.9 | -2.5 | +0.274 s |
| Trumpet 1 | -4.8 | -3.3 | +0.237 s |
| Trombone 1 | -5.9 | -3.5 | +0.279 s |
| Tuba | -1.4 | +1.9 | +0.223 s |

- So the brass play "ff, a dip, a swell, then p" instead of a hard attack that drops. The strings at the same mark peak at -0.01..+0.09 s since the c10 bump (Violins I -0.011 s).
- The sample's rise sets the brass peak. c10 already showed that more lead does not move it (0.05-0.12 s leads still peaked +0.22-0.27 s).
- A CC1 shape cannot fix it either. On these KS Masters CC1 crossfades the dynamic layers with a fade of about 120 ms (Movement I c12: a CC1 front lift gave only +1..+2 dB). The sf already starts at the ff layer, and raising CC1 above 108 would only reach the brighter fff layer, again at the sample's rise.

**Manual.**
- p.101: Sustain Accent is "sustained but with an accent at the beginning of the note. The MIDI Velocity parameter controls the loudness of the attack. The Mod Wheel controls the loudness of the sustained note." That is an sfp in one note: velocity gives the sf and CC1 gives the p.
- kit LEARNINGS c19 calls the Sus Accent samples fast.
- p.103's "Sfz Cres" (1FH, 1TB, 1TU) is a sforzando followed by a strong crescendo. That is the wrong shape for sfp, so drop it from the MANUAL-GAPS c09 plan.
- The velocity-layer route (p.162/190) does not work for a same-pitch layer (Manual notes).

**Fix (A/B on one onset).**
1. `build/score_config.py` `ART_SPANS`: add `{"from": 591.9, "to": 592.1, "art": "Sus Accent MAX"}` to Horns 1-4 (1FH key 25), Trumpets 1-3 (1TP key 25), Trombones 1-2 and the Bass trombone (1TB key 25) and the Tuba (1TU key 61). Check in parts.json that the window catches each 592 note by its score onset (the moved onsets are 591.75-591.86) and no other note.
2. Velocity 100-105 on these notes, not 110 (kit LEARNINGS c10: a high accent velocity adds a transient, not weight). Keep FP_SPIKE_AT_MARK's CC1 path (hold 0.10 s, fall by 0.30 s). The accent is in the sample, so CC1 does not need to rise.
3. Lead: use the brass staccato lead (`STAC_LEAD_S` brass value, about 0.03 s) instead of the sustain lead, because the accent sample speaks fast. Then re-measure.
4. This adds one row on 11 tracks, so check REAPER's settled memory. If it goes over about 45 GB, do Horns 1 and 3, Trumpets 1-2, Trombone 1 and the Tuba first (inferred: they cover the chord's outer voices and its loudest stems).

**Targets.**
- Brass stems peak within +0.10 s of the mark.
- First 0.1 s at least as loud as the ff before (now -1.4..-5.9 dB).
- Drop to the p at least 10 dB by +0.35 s.
- Master tilt jump at 592 under +3 dB (no bite).
- If the stems overshoot, lower the velocity before adding any level row.

## 3. Bassoon 1's "Leg Slur Exp" row: keep it, and give the other two espressivo solos the same row (measured for the bassoon; inferred for the others; manual p.109, MANUAL-GAPS #5)

**Judgement on c10's first try (measured).** I tracked pitch on the Bassoon 1 stem (harmonics 2-4, 64 ms window): vibrato depth in cents, and the share of the cents signal at 4-7.5 Hz, over the first 0.5 s against the rest of each held note.
- On the Exp row, the longest held note grows a periodic vibrato:
  - 456.0 (D4): 3.3 -> 8.3 cents, 4-7.5 Hz share 0.33 -> 0.73.
  - 472.0: 4.1 -> 6.0 cents.
  - 484.0: 4.9 -> 3.4 cents, share 0.69.
- The soft Sus MAX notes in 208-292 change by 1-6 cents with shares of 0.02-0.48: drift, not vibrato.
- The Leg Slur MAX notes right after the solo (503, 514) move 8-14 cents with shares of only 0.2-0.37: drift plus transitions, not periodic vibrato.
- c10 measured the joins on time (median +10 ms, none over +80 ms), so the slower attack costs nothing in timing. The level was refit (-2 dB stem fix) and memory did not change.
- So the row does what p.109 describes (slower attack, gently increasing vibrato), with small depths. Keep it.

**Where next.** The two other exposed solos that the score marks expressively, both on Leg Slur MAX now:
- Cor anglais "dolce cantabile", bars 171-186 (qn 680-744, 62 joins, the duet with the muted Trumpet 1);
- Oboe 1 "solo, espress." bar 95 (qn 376-392, over the last desks' sul tasto) and "1. dolce" bar 187 (744-760).

**Fix.** `build/score_config.py` `ART_SPANS`:
- `"Cor anglais": [{"from": 679.9, "to": 744.0, "art": "Leg Slur Exp"}]` (EH key 35);
- `"Oboe 1"`: `{"from": 375.9, "to": 392.0, "art": "Leg Slur Exp"}` and `{"from": 743.9, "to": 760.0, "art": "Leg Slur Exp"}` (OB key 35).

Two full rebuilds. Keep CC1/CC11 as they are. After the render:
- refit the level with a roles row, as for the bassoon (+2.2 dB K there);
- check the cor anglais against the muted trumpet it doubles (c05: -12 ms median), adding leg_leads rows where a join moves past +80 ms.

**Measure.** Joins within ±40 ms, level within ±1 dB of c10, the pitch-vibrato share and growth as above. Revert a track if its joins move.

## 4. In the Largamente violas (bars 211-218), the new slurs re-bow less clearly than the louré notes inside each slur: the generic tenuto rule takes the chord repeats before the new-bow rule (S1; measured in the data and on the stem)

**Where.** Violas, div. two-note chords, qn 842-870. Each slur holds two tenuto half notes (louré). The chord repeats at the start of the next slur (846, 850, 854, 858, 862, 866), and the second note inside a slur repeats the first (844, 856, 860, 864, 868).

**What is wrong (measured).**

| repeat | count | gap in parts.json | stem dip median | stem under 3 dB |
|---|---|---|---|---|
| at a new slur | 16 | 0.06 qn (25 ms at 144 qpm) | 3.6 dB | 3 |
| inside a slur | 9 | 0.20-0.22 qn (83-92 ms, the STR_REP_NEW_BOW portato gap) | 10.1 dB | 0 |

- This is the reverse of the printing. The new slur is a new bow and should be the clearer break; the louré pulse inside the slur is the gentler one.
- c10's A #5 had the diagnosis the wrong way round.
- On the master both groups dip a median 2.7-2.8 dB in the violas' harmonic band, because the trumpets' ff theme fills that register. The audible gain is in the violas' own onsets, and its size on the master is inferred.

**Cause (read).** In `tools/score_to_parts.py`, the note-end chain (about lines 2834-2950) checks the generic tenuto branch (`elif near(n["qn"], ten_q) and ...`, strings: `e0 - min(0.06, 0.15 * dur)`) before the `STR_REP_NEW_BOW["chord"]` branch. Every one of these chords carries a tenuto, so the chord rule (gap 0.09 s, which needs a different slur and stroke_cc or louder, both true here) is never reached. The `STR_REP_NEW_BOW["tenuto"]` branch would also apply, but it excludes chords (`len(nxt) == 1 and not polyphonic`).

**Fix.** In that chain, test the `STR_REP_NEW_BOW["chord"]` condition before the generic tenuto branch. Or add `and not (same_pitch and family == "string" and (polyphonic(n) or len(nxt) > 1) and not same_slur(n, o0))` to the generic tenuto branch. Keep the "change bow at will" skip spans as they are (the violas have none at 842-870).
- Check: parts.json gaps at the six slur starts become 0.09 s (0.216 qn).
- Then scan the whole piece for other tenuto chord repeats the change catches. Expect Violins II / Violas at 362-366 and the chorale div. chords.

**Target.** Slur-start repeats dip 8 dB or more on the stem (now 3.6). Louré repeats stay at about 10 dB.

## 5. Flute 2 still lands 150-275 ms late on the F1 heads that leave D♯6; its lead is not capped (S2; measured)

**Where.** Flute 2's slur-start joins at qn 618 (D♯6 -> A♯5, bar 155) and 650 (D♯6 -> C♯6, bar 163), in unison with Flute 1 on the ff F1 recap.

**Evidence (measured).**
- Flute 2 lands +48 / +152 / +49 / **+275** / -38 / +49 ms at 602 / 618 / 634 / 650 / 1007 / 1074. Flute 1 lands -42 / +10 / -45 / -30 / -34 / -42 ms on the same notes.
- Every Flute 2 join gets the same lead: 0.448 qn (0.16 s, `SOST_JOIN_LEAD_S`).
- The 0.45 x first-note cap is 0.918 qn there (the first notes are 2.04 qn), so **the cap does not bind**. c10's explanation does not hold.
- The two late joins are the two that leave D♯6 (MIDI 87); the joins from C6 to G5 land +48/+49. Flute 1 is also 40-55 ms later from D♯6 (+10 against -30..-45). This is a source-pitch effect, as kit LEARNINGS section 5 describes for the Solo Horn's F4.
- Across the piece Flute 2's joins have median +28 ms, robust SD 47 ms, and 17 % more than 60 ms off (Flute 1: +8 / 12 ms / 4 %).

**Fix.** `build/leg_leads.json` "Flute 2": add "618.0": 0.12 and "650.0": 0.17. That is 0.8 x the error, which exceeds c10's ±0.08 s clamp; it is allowed because the cap leaves room to 0.33 s at 0.16 + 0.17. Also add Flute 1 "618.0": 0.03. Check the realised moved onsets in parts.json (Flute 2 650 at about 649.07).

**Target.** Flute 2 minus Flute 1 at the four ff heads within ±40 ms (now 90 / 142 / 94 / 305 ms).

## 6. (Small) Celli re-bow hole at qn 919.963 in the chorale (S1-type tone hole; measured)

- One re-bow piece of the celli's held C3 (bar 230) dips 10.1 dB for about 60 ms after its onset.
- Its fitted fill is still at -4.4..-2.4 dB there and peaks after the hole (+6.5 dB at +0.2 qn).
- Fix: refit `build/rebow_fills.json` "Violoncellos" "919.963" with `tools/fit_rebows.py` on the c10 stems. Failing that, start its rise at +0.0 qn instead of +0.08 qn.
- Target: under 3 dB, like the other celli re-bows (3.2-3.3).

**Do not touch:**
- The legato rules: mono, no joins wider than an octave, no CC22, overlap floors, velocity by dynamic with floor 100. String join medians are -6..+19 ms; winds and brass +1..+33.
- The wind and brass staccato rows.
- The wind and brass re-tongue repeats (stem medians 4.9-16.9 dB).
- The c09 "plain" new-bow gaps.
- The REP_SPLIT 63 ms gaps and the -3 dB detach dip on the basses (keep both, and add finding 1's gap dip on top).
- The muted Trumpet 1 on Mute Sus and the open solo on Leg Slur.
- The stopped horns.
- Pizzicato leads (attacks +3..+15 ms).
- The gentle brass accent swell (tilt jump median -0.5, p90 +2.8; heads 247-262 p90 +2.2).
- The re-bow layout and the tremolo rows (no loop fold over 0.2 on the master).
- FP_SPIKE_AT_MARK and the string sf bump at 592.
- Bassoon 1's Leg Slur Exp row.
- The returns and envelope: final chord -20 dB in about 0.43 s, tutti stops 0.36-0.39 s from the last held level.

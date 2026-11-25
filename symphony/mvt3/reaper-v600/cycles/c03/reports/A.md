# Cycle 3, critic A: articulation and phrasing (render c02, score v600)

Method. All numbers come from the c02 stems (`cycles/c02/render`, after the Horn 3/4 stem fix), placed on the tempo map in `build/parts.json` (`tools/pcx.py` TM; the stems are on score time, checked on the timpani strokes at qn 792-796: attack rise +10..+17 ms). Rows come from each track's keyswitch lane; marks, slurs and ties from `build/mockup-events.tsv`. Measures:
- **Repeat dip (S1), harmonic band.** `pcx.band_env` on the repeated pitch (exclusion bands, 10 ms box): min(peak in -0.15..-0.03 s, peak in +0.03..+0.25 s) minus the minimum in -0.10..+0.06 s around the score onset. Used for the louré and portato notes.
- **Repeat dip, broadband.** The same window on a 10 ms RMS envelope of the stem. Used for the all-track repeat scan. Repeats whose notes the unison rule moved to another track are excluded.
- **2-5 kHz front.** Band energy over the first 80 ms minus the band energy over +0.15 s to +0.6 s (notes of 0.3 s or longer).
- **Timing (S2).** `pcx.attack_pcx` (perceived attack re the score onset) and `pcx.pair_window` (crossover, and the time both pitches sit within 6 dB) on legato joins.
- **Staccato length.** Envelope peak to -10 dB.

"Measured" means a number from the render, parts.json or a patch file. "Inferred" means reasoned, not tested.

## Manual notes (cycle 3, slot A: 2021 manual PDF pages 100, 103-107, read in full; Movement I's c38 A table checked against the Finale)

| Manual (PDF page) | Where it applies in the Finale | Does the render follow it? |
|---|---|---|
| p.100: brass instruments (solo horn, trumpet, trombone, tuba; 2/6 Horns, 2 Trombones, 2 Trombones + Bass Trombone, 2/3 Trumpets). | 1FH on Horns 1-4, 1TP on Trumpets 1-3, 1TB on Trombones 1-2 and the bass trombone, 1TU on the tuba. | Yes. There is no solo bass trombone. The Finale has 11 bass trombone notes below the 1TB sample roots (E2, MIDI 40): MIDI 39 at qn 360-372 and 660, 37-34 at 414-416, 38 at 611 and 643. MANUAL-GAPS #13 counts 3 for Movement I. They are transposed samples (patch, measured); the audible effect is inferred to be small. |
| p.103: Repetitions Fast 170 / Med 145 / Slow 120 bpm (tempo-synced, CC1 sets loudness, release trails). Triple Performance (3 Trumpets). Double tonguing. | The Finale's brass repeats are whole and half notes (horns: 56 of 108 repeats are whole notes). The only eighth repeats are single ones: Tpt 1/2 at 1097.5, Tbn 1/2 at 996. The hammered eighths are in the basses and timpani. | n/a for the repetition rows. The brass staccatos are on "Stac DblTng RRx9" (Trumpets 1-3, 15 notes each): -10 dB length 0.27 s, against 0.22-0.27 s for the string staccato rows. Follows. |
| p.103: Sforzando Crescendo (horn, tuba). | Horns 3/4 at qn 548 are sf with a diminuendo, not a crescendo. | n/a. |
| p.104-105: effects (trills, rips, shakes, flutter, clusters). Crescendo patches Fast/Med/Slow, "often more realistic" than CC crescendos, no release trails. | No brass effects are printed. Brass hairpins are done with CC1. | n/a. The crescendo rows are not used; not ranked this cycle. |
| p.105: brass legato only with no gap and within an octave. Legato patches are monophonic (CC22 64-127). Slide legato on trombones. | Every brass legato row. | **Yes** (measured in parts.json on 11 brass tracks): no legato join wider than 12 semitones, no chord on a legato row, no same-pitch overlap, no CC22. No trombone glissando is printed, so Leg Slide is not needed. |
| p.106: Legato Slur. CC1 is the volume and opens an overblow filter near 127. **Velocity sets the transition speed.** | All brass Leg Slur MAX notes. Trumpet 1's open "solo, dolce cantabile" at bars 51-66 (qn 200-264). | CC1: yes, the brass maximum is 120 on every track. Velocity: 70 of Trumpet 1's 87 legato notes play v124, the fastest slur, including the p dolce solo, where the arrivals are 47 ms early (finding 3). |
| p.106: Legato Slur Accent (velocity = accent strength). | Accents inside brass slurs, e.g. Trombone 1 at 985, 993 and 1001 (Più allegro heads). | Not used: Leg Slur plus the GENTLE_ACCENT swell. 2-5 kHz fronts on those accents are -2.2 to -9.0 dB, and the 99 brass accents in 984-1116 have a median of -12.6 dB. That is weight, not bite, as Dan asked. Keep. |
| p.106: Legato Slur Repetitions (same-pitch notes "without space" get a re-tongued sample). | Slurred brass repeats into a tenuto: Trombone 1 987.5 -> 988 (bar 248, with Vc and the violins' louré). | Not used. The repeat is re-tongued on Sus MAX after a 77 ms gap, but dips only **0.9 dB** (finding 1). The 1TB KS Master has no Leg Slur Rep row (ks_maps), so the fix stays on the emulation. |
| p.106: Slur Runs (steps of a second). | No brass runs are printed. | n/a. |
| p.106-107: mutes. **"Stop" (hand in the bell), most characteristic of the French horn.** | Trumpet 1 con sordino, qn 680-792. **Stopped-horn marks ("+")**: Horn 1 qn 192-199 (p, tied); Horns 3 and 4 qn 548 (sf, dim.); Horns 1 and 2 qn 668-675 (tied, dim. to p). "Open" marks follow at 264, 552, 560 and 744. | **Mute: yes, but the slurred line is re-tongued on every note** (finding 4). The 1TP mute rows are Mute Sus, Mute Sus Accent and Mute StacSs; the Solo Trumpet Mutes folder has no legato patch (patch). **Stopped horn: no.** All five notes play open on Sus MAX, although the 1FH KS Master holds "Stop Sus" (key 80), "Stop Sus Accent" (81) and "Stop Stac RRx4" (82) (finding 2). |
| p.107: keyswitch masters. | Every row change. | Yes: `ks_clash` is empty on every brass track. The shortest keyswitch-to-note lead is 10.2 ms (measured). |
| MANUAL-GAPS #2 (repetition rows LegRep RRx4 / Leg Slur Rep, p.101, p.106) | Brass whole-note pedals in the coda (808-813, 824-836) and the chorale (896). | Not used: no `REP_ROW` entry in the Finale (Movement I kept it on 7 tracks). See finding 5. |
| MANUAL-GAPS #9 (horn portato row, p.101) | Horn tenutos, e.g. Horn 1 at 989 (Più allegro head). | Not used. Not ranked this cycle. |

Standing checks:
- **Item 4 (accents), measured: passes.** Brass 2-5 kHz front medians are -12.7 dB (984-1048, 20 accents) and -12.5 dB (1048-1116, 79 accents). The highest is Trombone 1 990 at -2.2 dB.
- **Staccato rows, measured: consistent.** Envelope peak to -10 dB:

| row | median | p90 |
|---|---|---|
| Horn 1 Marc Shrt | 0.23 s | |
| Horns 3/4 Marc Shrt | 0.30-0.32 s | |
| Trumpet 1 Stac DblTng | 0.27 s | |
| Bassoon 1 Stac DblTng | 0.23 s | |
| Violins I Staccatissimo | 0.22 s | |
| Vln II / Vla / Vc Stac | 0.23 / 0.27 / 0.24 s | |
| Double basses Staccato | 0.22 s | |
| all rows | | at most 0.34 s |

- **S1 scan (broadband, separate notes only):**
  - Most tracks are clear: Double basses median 9.5 dB over 339 repeats, timpani 9.0, wind and brass medians 5.7-10.3.
  - The weak points are findings 1 and 5.
- **Items 7 and S3:** not re-measured. c02 changed no held-note data in my lens.

## 1. Tenuto and portato repeats still run together in strings and trombone: harmonic-band dips of 0.4-2.9 dB on 46 notes (S1; measured)

**Where.**
- **Slurred portato quarters:**
  - Violas qn 892-911 (bars 224-228, the f portato under the chorale, 15 notes);
  - Violins II qn 921-931 (bars 231-233, 9 notes).
- **The louré (eighth slurred into a tenuto on the same pitch):**
  - qn 796 (bar 200): Vln I, Vln II and Vla;
  - qn 988 (bar 248): Vln I, Vln II, Vc and Trombone 1;
  - Vln I 430.
- **Unslurred tenuto repeats:**
  - Vc and Cb qn 976-983 (bars 245-246, the stringendo's repeated D quarters driving into the Più allegro);
  - Vc and Cb qn 324-327 (bar 82, animando, mp).
- **The whole-note pedal into the run:** Vc qn 824 -> 828 -> 832 (bars 207-209).

**What is wrong (measured, harmonic-band dip, dB).**

| passage | onsets | dips | median |
|---|---|---|---|
| Violas portato | 893-911 | 1.2-4.8 | 2.2 |
| Violins II portato | 921-931 | 1.4-2.4 | 2.1 |
| louré, Vln I / Vln II / Vla | 796 | 2.0 / 1.9 / 1.0 | |
| louré, Vln I / Vln II / Vc / Trombone 1 | 988 | 1.6 / 2.7 / 2.4 / 0.9 | |
| Vc tenutos | 978-983 | 0.5-1.9 | |
| Cb tenutos | 978-983 | 0.4-1.8 | |
| Vc / Cb, bar 82 | 325 / 327 | 1.1 / 1.4 and 2.1 / 0.6 | |
| Vc pedal | 828 / 832 | 0.7 / 0.6 (broadband) | |

- **In the same bars the winds separate.** At 796 and 988 the clarinet measures 8.7 dB, Flute 2 7.9 and Bassoon 1 4.3. The winds play the figure as two notes and the strings as one.
- The c02 actor's broadband figure for the louré (6.2-7.9 dB) does not hold on harmonic bands or on a 10 ms broadband envelope here. The Vln I stem around 796 stays within -33..-37 dB with no dip at the onset.

**Why (measured in parts.json).** The gaps are too short to survive the string release at these tempi (0.36-0.45 s per quarter):

| notes | gap (old note-off to new moved onset) | why |
|---|---|---|
| louré tenutos, 796 / 988 | 43-45 ms | `portato` gap 0.05 s, and the stroke then starts 51-54 ms early on the short-Sus lead |
| Vla / Vln II portato strokes | 50 ms | led by 100 ms |
| Vc 980-983 | 22-24 ms | they fall under `STR_REP_NEW_BOW["sus_min_s"]` 0.4 s (each quarter lasts 0.36-0.44 s at 136-166 qpm), so they keep the old short gap |
| Cb 978-983 and 325-327 | 7-9 ms | the basses get only the 0.03 qn same-pitch gap |
| Vc / Cb 325-327 | short | at mp they are under `stroke_cc` (mf), so the rule does not apply |
| Vc 832 | 10 ms | |
| Trombone 1 988 | 77 ms (Sus MAX, after a Leg Slur note at v124) | dips 0.9 dB anyway; the 1TB release trails fill it (inferred from the patch's release-trail groups) |

**Fix.**
1. **`build/score_config.py` `STR_REP_NEW_BOW["portato"]`:** `gap_s` 0.05 -> 0.08, `fall_cc` 6 -> 10, `fall_cc_loud` 8 -> 12, `fall_s` 0.04 -> 0.06. Measure the gap from the stroke's moved onset, not the score onset, so the stroke's lead cannot eat it. In `tools/score_to_parts.py`, where the "portato" class sets `n["end"]`, use `qn_before(moved onset, gap_s)` when the stroke is led. Generic, default unchanged.
2. **New key `STR_REP_NEW_BOW["tenuto"]`** (generic, default None): an unslurred same-pitch repeat carrying a tenuto is a portato stroke at any dynamic and any length. Finale value: `{"gap_s": 0.07, "frac": 0.25, "fall_cc": 8, "fall_s": 0.05}`. This covers Vc 324-327 and 976-983.
3. **Double basses:** add `STR_REP_DETACH["at"]["Double basses"]` spans (322.0, 328.0) and (976.0, 984.0) with `{"max_qn": 2.0, "same_pitch_only": True}`. That is the -5 dB / 0.08 s dip that took the bass line to 7 dB in c02.
4. **Vc 828 -> 832:** the 828 note (moved onset 827.70, length 4.27 qn) ends at 831.97. Let `sus_min_s` gaps apply when the next note is the head of a slur (832 is the first eighth of a slurred run). Or add Vc 832.0 to `DOWNBOW_STROKE_AT` so it takes the stroke path with its gap.
5. **Trombone 1 988 (and any brass repeat into a tenuto inside a slur):** `WIND_REP_RETONGUE_BY["Trombone 1"]` with the horn values (gap 0.10 s, frac 0.3, `fall_cc` 12, `fall_s` 0.15), which raised the bassoons from 4 to 6 dB in c02.
6. **The c03 string release cap** (150 ms on Sus MAX / Sus Marc LITE, Movement I c44, already planned) acts on exactly these notes. Measure these onsets again after it before changing more.

**Targets.**
- Harmonic-band dip at least 4 dB on the slurred portato quarters and at least 6 dB on the louré tenutos and unslurred tenuto repeats.
- Each stroke within ±2 dB of the note before (no stroke spike; the Vla CC11 already jumps 82 -> 93 at each stroke).
- Stroke pcX within ±0.04 s of the beat.

## 2. The five stopped-horn notes play open (measured in the data; audible effect inferred)

**Where.**
- Horn 1 qn 192-199 (bars 49-50, p, tied; "open" at 264).
- Horns 3 and 4 qn 548 (bar 138, sf with a diminuendo; "open" at 560 and 552).
- Horns 1 and 2 qn 668-675 (bars 168-169, tied, dim. to p; "open" at 744 and 776).
- The marks are the `stopped` script in mockup-events.tsv.

**What is wrong.**
- All five notes play the open "Sus MAX" row (parts.json): Horn 1 192 v53, Horns 3/4 548 v98, Horns 1/2 668 v83.
- `tools/score_to_parts.py` and `build/score_config.py` never read the `stopped` script.
- Stopped horn is a distinct, nasal, brassy sound. The score asks for it at the end of the transition into the second theme (bars 49-50, under the poco rit.), on the sf chord of the retransition (bar 138), and in the recapitulation's lead-in (168-169). Played open, these notes sound like ordinary held horn notes (inferred).

**Library (read).**
- Manual p.106: the stop is "most characteristic of the French Horn".
- The 1FH KS Master has "Stop Sus" (key 80), "Stop Sus Accent" (81) and "Stop Stac RRx4" (82), unloaded.
- The patch `Solo French Horn/05 Mutes/1FH Stop Sus.oib` has pp/mf/f groups with CC1 on the source volume, the same layer scheme as the 1FH Sus MAX. CC1_DYN_MAP therefore carries over unchanged.

**Fix (`build/score_config.py` `ART_SPANS`):**
- Horn 1: `{"from": 191.9, "to": 199.9, "art": "Stop Sus"}` and `{"from": 667.9, "to": 675.9, "art": "Stop Sus"}`.
- Horn 2: `{"from": 667.9, "to": 675.9, "art": "Stop Sus"}`.
- Horns 3 and 4: `{"from": 547.9, "to": 551.9, "art": "Stop Sus"}`, keeping the existing sf shaping (CC1 attack and fall).
- A/B option for 548: "Stop Sus Accent" at velocity 80-85 (p.101: velocity is the attack loudness). Dan rejected bright accents, so stay under v90.
- The new row is loaded on four horn tracks, so they need a full rebuild (row set changes, kit rule). Memory is about 0.1-0.3 GB per row (inferred, MANUAL-GAPS memory plan).

**Measure.**
- The span level against the c02 notes. Stopped samples are usually quieter and brighter; refit with a `roles.json` row if they move more than 2 dB.
- 2-5 kHz minus 0.5-1 kHz against the open notes. Expect the stopped notes clearly brighter.
- The 548 front: 2-5 kHz first 80 ms minus body under +3 dB.

## 3. Trumpet 1's open dolce solo (bars 51-66) arrives 47 ms early on every slur and uses the fastest legato velocity (S2 measured; colour inferred)

**Where.** Trumpet 1, qn 200-264: "solo, dolce cantabile", p, 37 legato joins on Leg Slur MAX.

**Evidence (measured, pcX on the stem).**
- Perceived attack median -0.047 s. 33 of 37 joins are earlier than -0.02 s; the range is -0.077 to +0.021 s. The crossover median is about -0.02 s, and the both-pitches window is 74 ms.
- Elsewhere the same track and the other brass are on time:
  - Trumpet 1 at 836-892 (ff): -0.010 s; at 984-1116: +0.010 s;
  - Trumpet 2 at 836-892: +0.002 s;
  - Horn 1: +0.006 / +0.028 s;
  - Trombone 1: +0.009 s.
- The lead is the brass `LEG_LEAD_S` 0.1 s on every join, and every target is v124.
- At p (CC1 42) the 1TP transition samples reach the new pitch sooner than at f, so the same lead lands early only in the soft solo (inferred from the contrast).
- In bars 51-66 the line is accompanied only by pizzicato strings, so a 47 ms anticipation of each melody note is exposed. The brief's S2 limit is 40 ms.

**Manual.** p.106: velocity sets the transition speed. v124 is the fastest, most clipped slur, the opposite of dolce cantabile (inferred). This is c01/c02 A #6, deferred twice; the timing number now gives it a measured basis.

**Fix.**
- **`tools/score_to_parts.py`:** a generic `BRASS_SOFT_LEG` option, default None, beside the soft-string rule. For brass legato targets whose CC1 is at or under a threshold:
  - velocity = "vel";
  - lead = "lead_s" in place of LEG_LEAD_S.
  - Finale value in `build/score_config.py`: `BRASS_SOFT_LEG = {"tracks": ("Trumpet 1",), "max_cc1": DYN["mp"], "vel": 96, "lead_s": 0.05}`.
- Or, without a tool change, per-onset entries in `build/leg_leads.json` for Trumpet 1 203-260 (lead 0.05 s), plus a velocity table if the tool takes one.
- **Option (A/B, inferred):** "Vib Leg Slur MAX" (1TP KS key 40) for 200-264. It is a vibrato legato, closer to a "dolce cantabile" solo than the non-vibrato Leg Slur. The row must be loaded (full rebuild of Trumpet 1, which already rebuilds for the c03 caps if they touch it).

**Targets.**
- pcX median within ±0.02 s.
- Transition peak minus body 0-2 dB (now a median +1.8 dB broadband).
- Both-pitches window under 0.12 s.

## 4. Trumpet 1's slurred con sordino solo is tongued on every note (measured; fix inferred)

**Where.** Trumpet 1 qn 680-731 (bars 171-183): two slurred phrases (680-696 and 712-731, "con sord., dolce cantabile"), doubled by the cor anglais on Leg Slur MAX.

**What is wrong.** "Mute Sus" is a sustain row (patch: 5 CC1 layers pp-ff, envelope attack 12-20 ms, release-trail groups), and HO has no muted legato for the solo trumpet (Solo Trumpet/05 Mutes holds only Mute Sus, Mute Sus Accent and StacSs Mute). The 22 slurred joins are butted fresh notes (gap 0.0 qn, parts.json), so every note of the slur starts with a new attack.

**Evidence (measured; 2-5 kHz front minus body on each join).**

| line | median | p90 | max | joins at or over +0 dB |
|---|---|---|---|---|
| muted solo | -4.9 | +1.4 | +6.2 (691) | 6 of 23 (687 +3.4, 691 +6.2, 694 +1.4, 719 +1.4, 723 +0.3, 726 +0.1) |
| same trumpet's open legato solo | | -1.8 | +0.9 | 2 of 40 |
| cor anglais on the same notes | -7.8 | -1.5 | | |

- Broadband dips at the joins reach 11.7 dB (690) and 6.8 dB (688), with fronts +4.4 / +4.5 dB.
- The perceived attacks run +0.044 s late (cor anglais +0.036).
- The muted trumpet articulates where the cor anglais it doubles slurs, so the doubling sounds tongued.

**Fix (inferred; there is no sample-based legato for this mute).**
- `tools/score_to_parts.py`: a generic option `SLUR_ON_SUS_OVERLAP = {track: (row, overlap_s)}`. Inside a printed slur, a note on that row is held `overlap_s` past the next note's onset, and the CC11 lane stays flat across the join. The old note's sustain then covers the new note's 12-20 ms attack ramp, and its release starts after the attack.
- Finale value: `{"Trumpet 1": ("Mute Sus", 0.06)}`.
- Only the slurred phrases; 792 (senza sord.) is not affected.

**Measure.**
- Join front (target p90 under -1 dB, no join over +2 dB).
- Both-pitches window under 0.15 s, so the overlap does not smear.
- pcX within ±0.04 s.
- If the overlap smears (window over 0.15 s), drop to 0.03 s.

## 5. Whole-note brass pedals in the coda and chorale re-attack only 1.8-3.5 dB (S1; measured)

**Where.**
- Horn 2: qn 808, 810, 812, 813 (bars 203-204, ff, repeated F4).
- Horn 2 qn 442 (bar 111) and Horn 3 qn 384 (bar 97).
- Horn 3 / Horn 4: 836 (bar 210).
- Bass trombone: 828, 836 (bars 208-210, the A♭ pedal, with the cellos of finding 1).
- Horn 2: 896 (bar 225, the chorale's repeated E4 whole notes).
- Trombone 2: 588.

**Evidence (measured, broadband dip, dB).**
- Horn 2: 810 2.0, 812 2.0, 442 1.9, 896 1.8.
- Horn 3: 384 1.9, 836 2.5.
- Horn 4: 810 3.5, 836 3.5.
- Bass trombone: 828 3.2, 836 2.4.
- The brass median elsewhere is 6.2-7.1 dB.
- These repeats have a 0.1 s gap and a 12 CC fall. Horn 2 810 ends at 809.468 against a moved onset at 809.748, a 0.28 qn gap at 168 qpm. The horn's 562 ms envelope release and its release-trail samples fill the gap.
- This pedal is the coda's driving pulse (S1 names brass repeated notes in the chorale and coda).

**Fix.**
- First, the c03 horn release cap (`sus_release_cap_ms` horns 237 ms on Sus MAX / LegRep, layers pp, mf, f, which covers every horn dynamic). Re-measure these onsets.
- If they stay under 4 dB, apply MANUAL-GAPS #2 (manual p.101: Legato Repetitions, re-tongued samples) with Movement I's c38 settings: `REP_ROW = {"Horn 2": [(808.0, 814.0, "LegRep RRx4")], "Horn 3": [(836.0, 840.0, "LegRep RRx4")], "Horn 4": [(836.0, 840.0, "LegRep RRx4")], "Bass trombone": [(828.0, 840.0, "LegRep RRx4")]}`. `REP_ROW_GAP_S` (0.06, 0.15) and `REP_ROW_REPEATS_ONLY` ("brass",) are already set.
- Movement I measured Horn 4 on this row at 7.2 dB with a real tongued front (Results c38). Horn 1's re-attack came in 2-5 dB louder (Results c41), so trim the body past 0.1 s if it does.
- The chorale's Horn 2 896 can stay on the cap alone: 3-4 dB is enough under a maestoso chorale (inferred).

**Target.** Dip at least 4 dB, each repeat within ±1.5 dB of the note before, 2-5 kHz front under +3 dB.

## 6. The bar-236 portamento is not yet heard as a slide, and Violins II arrives late (measured; small)

**Where.** Vln I and Vln II, qn 940 -> 941, C5 -> A5 "port." on Leg Port MAX at v100 (c02 A #4).

**Evidence (measured, c01 Leg Slur -> c02 Leg Port, band level over -0.4..+0.05 s around the join, dB).**

| | D5 (74) | E5 (76) | F#5 (78) | G#5 (80) |
|---|---|---|---|---|
| Vln I | 12.5 -> 9.7 | 13.6 -> 13.6 | 9.3 -> 9.7 | 1.2 -> 6.6 |
| Vln II | 10.5 -> 6.9 | 7.9 -> 7.9 | 1.0 -> 0.2 | -5.7 -> 4.1 |

- Only the semitone just under the target rose, by +5.4 / +9.8 dB, against critic A's c02 target of +10 dB across 73-80. The glide is a short scoop into the A, not a slide through the sixth.
- The A5 arrival pcX is +0.038 s on Vln I and **+0.114 s on Vln II** (c01: +0.048 / +0.019).

**Fix.**
- `PORT_TARGETS` velocity 100 -> 80 for a slower, longer slide. The manual says velocity sets transition speed for legato (p.98-99 strings, p.106 brass), and Movement I used 100 for a fourth, while this is a major sixth (inferred).
- Add a Vln II per-onset lead of +0.07 s at 941 (`LEG_LEADS` / `build/leg_leads.json`) so the two sections land together.
- Targets: the 76-78 bands up at least 6 dB over c01; |Vln II - Vln I| arrival under 0.03 s.
- Lowest priority of the six.

**Do not touch.**
- **Brass accents** on GENTLE_ACCENT: 2-5 kHz fronts median -12.6 dB in 984-1116, highest -2.2.
- **Staccato rows and lengths** (0.22-0.32 s across sections), including Horn 1 and Horns 3/4 on Marc Shrt.
- **Bass detach spans and repeat dips:** Double basses median 9.5 dB over 339 repeats.
- **Timpani repeated strokes:** median 9.0 dB.
- **Wind re-tongues:** medians 5.8-10.3 dB.
- **Brass legato hygiene:** no join wider than an octave, no chords on legato rows, CC1 at most 120, no keyswitch clash.
- **The tremolo rows and the CC11 subito at 892; the mute bandpass (250-8000 Hz).**
- **The Vc/Cb "change bow at will" merges 892-940; harp harmonics and the bar-277 glissando; the pizzicato rows.**

# Cycle 11, critic A: articulation and phrasing (render c10)

All measurements use `cycles/c10/render/` (dry stems 01-31 and `00_Master.wav`) with `cycles/c10/build_render/parts.json` and its tempo map. pcX is `tools/pcx.py` `attack_pcx`, run with the previous pitch excluded, as the tool's own `scan` runs it. Values are perceived attack minus score beat, in ms. "Cross" is `pair_window`'s crossover. Envelopes are RMS over 10 or 30 ms windows. I ran the same scripts on c08's stems with `cycles/c09/before/parts.json`. For every string note the c08 and c10 values are identical to the millisecond. The render is deterministic, so per-onset fits made on c10 will carry over. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c11-A/` and have been deleted.

## Manual notes (cycle 11 slot A: group A5, May 2021 HO manual PDF pp. 100, 103-107, Hollywood Brass; plus MANUAL-GAPS.md)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| The library has solo instruments and 2-player sections: 2 French Horns, 2 Trumpets, 2 Trombones (p.100) | Hn 3 + Hn 4 in unison on the tenor countermelody (105-120, 305-320) | No. Horn 4's 28 unison notes are dropped (`unison_dropped`) and Horn 3 plays them alone on the solo 1FH patch with `UNI_BOOST` +3 dB. The trumpets play in thirds, so two solo patches are right there. See finding 6. |
| Repetitions patches loop at fixed speeds of 120, 145 and 170 bpm (p.103) | none | n/a. The figures are the theme head (quarter, two eighths, quarter), not repeated quarters, and the eighths run at 528 per minute (MANUAL-GAPS #15). |
| Double tongue for fast repeated notes (p.103) | Trumpets 1-2: theme head in 101-120, 301-303 and the coda 993-1004 | Yes. Both trumpets play "StacSs DblTng RRx9" (56 notes each, v96 at ff). Stem pair dips are 2.5-4.4 dB median, because the Main mic carries the room. On the master the 1-4 kHz pair dips are 6.0 dB median (2.4-8.4). Measured, adequate. |
| Sforzando Crescendo on Solo Horn and Tuba (p.103) | the sfp < at bar 301 | n/a. The sfp is printed only in the woodwinds and strings (events read). The horns enter at 897/900 without sfp. |
| Legato slurs only with no gap and within an octave (p.105) | Hn 1's horn call, 56 -> 68 -> 56 -> 64 (bars 3-4) | Yes. The octave G sharp 4 -> G sharp 3 at qn 6 is exactly 12 semitones. No brass legato join exceeds an octave (parts.json). |
| Legato is monophonic by default; CC22 64-127 keeps it monophonic (p.105) | brass Leg rows | Yes (`LEGATO_MONO_CC22` 127 in the pre-roll). |
| Legato volume follows the Mod Wheel, with overblow near CC1 127; velocity sets the transition speed (p.106) | every horn legato note: CC1 dynamics (`CC1_DYN_TRACKS`, the horns' soft map) | Partly. CC1 tracks the dynamic, but the slow transitions are not given more lead. Hn 1's call at qn 9 (v100) arrives at +159 ms, Hn 3's dolce recall in 1020-1044 (v100) at +40 ms, while the v124 tutti countermelody lands at +7 ms. The CC1 hairpins are only 2-4 CC deep, so the sample's own swell wins: the horn call's decrescendo plays as a +9 dB crescendo (finding 2). |
| Legato Slur Accent: velocity sets the accent (p.106) | none (the score keeps accents off the brass, c200) | n/a. |
| Legato Slur Repetitions: repeated notes inside a slur, with no space between them, use re-tongued samples (p.106) | Horn 1 / 2 slurred tenuto repeats in 209-222 (the c10 open item) | Not used. 1FH has "Leg Slur Rep MAX" (17,245 regions read from the .oib, against Leg Slur MAX 13,990). Finding 5. |
| Slur Runs give their strong slur only on steps of a second (p.106) | none | n/a. |
| Mutes and stopped horn (p.106-107) | none (no horn mute passage) | n/a. |
| KS Masters switch rows by key (p.107) | all brass | Yes. Horn 1 plays Sus MAX / Leg Slur MAX / StacSs RRx9 / Port Lng, the trumpets StacSs DblTng / Sus Non Vib. |

## Findings, ranked by what a listener would hear

### 1. Strings: the note after a slurred eighth lands 0.1-0.27 s late, so the eighth sounds dotted (measured)

**Where.** The slurred quarter-eighth-next-note figure in the espress. lines:
- the second idea: 134, 146 (bars 45-49), 374 (bar 125), 842 (bar 281);
- the trio: Violins I 536 (bar 179), 584, 597 (bars 195-200), 632, 644, 656 (bars 211-219);
- celli 194, 512, 524, 536.
The tracks are Violins I, Violins II and Violoncellos (Leg Slur MAX targets, v100-124).

**What is wrong.** The target after a slurred eighth gets a lead of only 0.085 s at quarter 264 (0.099 s at 228). The cap is `LEG_CAP_FRAC` 0.75 × the written eighth (0.375 qn), and `score_to_parts.py` measures it from the eighth's *score* onset (`cf_ * (q - pv["qn"])`). The eighth itself starts with the full lead: 0.09-0.24 s in Violins I and II, 0.16-0.28 s in the celli. The eighth is therefore held 0.2-0.3 s in MIDI, and the next pitch arrives well after its beat.

**Evidence** (pcX of the note after the eighth, with cross in brackets, ms):

| track | onset: pcX (cross) |
|---|---|
| Violins I | 134: +135; 146: +139 (161); 374: +150 (153); 536: +97 (113); 584: +145 (99); 597: +141; 632: +150 (133); 644: +185 (113); 656: +128 (137) |
| Violins II | 134: +179; 374: +185 (173); 632: +100 (87); 644: +88 (75); 842: +118 (95) |
| celli | 194: +231; 512: +165 (191); 524: +271 (201); 536: +101 (117) |

- The eighths themselves read -57..+58 ms.
- Perceived eighth length (pc of the next note minus pc of the eighth) is longer than written by a median of +36 ms in Violins I (IQR +12..+143), +126 ms in Violins II (+93..+179) and +91 ms in the celli (+72..+194). The written eighth is 114 ms at quarter 264 and 132 ms at 228.
- Two estimators agree (pcX and the band crossover), and so do two renders.
- The c03 leg-lead fit left these onsets out on purpose ("C #1 changes their cause"). No later cycle has dealt with them.

**Fix.**
1. In `tools/score_to_parts.py`, add a generic option `LEG_CAP_FROM_MOVED` (a set of track names, empty by default). For those tracks, measure the cap from the previous note's *moved* onset: `cf_ * (q - (pv["qn"] - shift.get(id(pv), 0.0)))`. `LEG_MIN_GAP_S` still keeps the moved onsets apart (Violins I 0.06 s, Violins II and celli 0.10 s), so the eighth keeps at least that much sounding time, and the pair moves as one unit.
2. In `build/score_config.py`, set `LEG_CAP_FROM_MOVED = {"Violins I", "Violins II", "Violoncellos", "Violas"}`.
3. Worked example (Violins II at 133.5 / 134): the cap becomes 0.75 × 0.354 s = 0.265 s, so 134 gets its full 0.24 s instead of 0.085 s. Expected pcX about +179 - 0.9 × 0.155 ≈ +40 ms.

**Pass:**
- median pcX of the listed onsets +50 ms or less, and none over +100;
- eighths no earlier than -50 ms;
- the attack probe's legato windows and robust SD no worse than c10 (Violins I 64 / 44, Violins II 80 / 45, celli 65 / 49 ms);
- the theme-head pairs (41.5, 53.5, 77.5 ...) re-checked with the same pass.

### 2. Hn 1's horn call (bars 3-5, qn 6-15): the rising sixth arrives late, and its decrescendo plays as a +9 dB crescendo (measured)

**Where.** Horn 1, qn 6-15. G sharp 3 `<` to E4 **p** at 9, then `>` to the D sharp 4 at 14-15 (`introHnOne`, espress.). It is solo over pizz. celli and basses: the horn is 0.5-1 dB under the master there, so it *is* the master.

**What is wrong.**
- **The arrival is late.** The E4 at 9 is a Leg Slur MAX target at v100 with only the horn's 0.06 s legato lead (`LEG_LEAD_S["Horn"]`). Its pcX is +159 ms. The G sharp 3 band holds until +140 ms, and the E4 band reaches full level at +180 ms (cross +62 ms). The octave drop at 6 (v41, the slowest transition) reads +81 ms. Manual p.106: velocity sets the transition speed. The tutti countermelody at v124 lands at +7 ms, so the slower velocities need more lead than the 0.06 s set for fast ones.
- **The hairpin is reversed.** Horn 1 stem per half beat:

| qn | 9.0 | 9.5 | 10.0 | 11.0 | 12.0 | 12.5 | 13.0 | 14.0 | 14.5 |
|---|---|---|---|---|---|---|---|---|---|
| dB | -42.4 | -39.3 | -35.3 | -36.3 | **-33.5** | -34.1 | -38.1 | -40.3 | -45.5 |

  The note peaks at 12, 9 dB over its p arrival, in the middle of the printed decrescendo. The master follows it (-40.9 at 9, -32.6 at 12). The controllers barely move: CC1 64 -> 62 and CC11 53 -> 47 over 9-15, and vol_db 6.5 -> 4.0. So the E4 sample's own swell sets the shape. This is the same cause as c10's Horn 1 last-G-sharp fix (LEVEL_SHAPES for "the sample's own swell").

**Fix.**
1. `build/leg_leads.json`: `"Horn 1": {"6.0": 0.04, "9.0": 0.10}`. These add to the 0.06 s base, for totals of 0.10 / 0.16 s, inside `LEG_LEAD_CLAMP` and the 0.45 × 3 qn cap. That is the c07 rule (0.7 × (pc - 0.02)).
2. `build/score_config.py`, `LEVEL_SHAPES["Horn 1"]`: append `[(9.25, 0.0), (10.0, -4.5), (11.0, -5.5), (12.0, -8.5), (12.75, -7.0), (13.75, -3.0), (14.75, 0.0)]`. A decrescendo may sit in the volume envelope: S3 forbids only fast falls there. The alternative is a 6-8 CC deeper CC1 hairpin on this note.

**Pass:**
- E4 pcX +50 ms or less, and the G sharp 3 at 6 +40 ms or less;
- Horn 1 per half beat falling from 9.5 to 15 with no rise over 1 dB;
- the E4's maximum within 1 dB of its 9.5 level;
- the call's cresc into 9 still rising (6.0 -> 9.0 at +6 dB or more).

### 3. The sfp hemiola, bars 301-302 (qn 902 / 904): the accent at 902 is missing in three string sections, and the 904 strokes come 0.12-0.19 s early (measured)

**Where.** qn 902 (bar 301 beat 3, accented, tied) and 904 (bar 302 beat 2, accented), inside the sfp < at 900. The tracks are Violins II, violas, celli and basses. Violins I is on time (902: -5, 904: +2 ms).

**What is wrong (moved onsets read from parts.json).** `REATTACK_LEAD_AT` gives 902 and 904 leads of 0.18-0.25 s. They were set in c05 against late swells and re-set in c07. The CC11 crescendo steps are tied to the moved onsets:
- at 903.11 the celli and Violins II step from 78 to 94;
- at 902.89 the violas do the same.

So the "accent" of 904 sounds on the second beat of the tied 902 note.

At 902 the strings are still in the p trough (CC11 63-65) and carry a -3 dB body cut (`accent_bodies.json`), so no accent sounds:
- the violas stay at -19..-20 dB re their sf from -0.05 to +0.2 s;
- the celli at -15..-12;
- Violins II at -20..-12.
- On the master, 902 is -13 dB at -0.05 s and -8 dB at +0.05 s, against 0 dB at the sf (30 ms window). Bar 101's equivalent beat (302) rises from -9 to 0 dB.

**Evidence** (lead, pcX in ms; identical on c08 and c10):

| track | 902 | 904 |
|---|---|---|
| Violins II | 200, +64 | 200, **-132** |
| violas | 180, +31 | 250, **-190** |
| celli (same pitch; broadband confirms it is early: -9 dB re peak at -0.15 s, -6 at -0.10) | 200, +177 | 200, -122 |
| basses (no lead) | 0, +101 | |

At 900 the basses read 0, +115.

**Fix** (`build/score_config.py` and the JSON tables):
- `REATTACK_LEAD_AT`:
  - Violins II 904: 0.20 -> 0.09, and 902: 0.20 -> 0.24;
  - violas 904: 0.25 -> 0.10;
  - celli 904: 0.20 -> 0.10;
  - basses `{902.0: 0.08}`. ONE_TIME_c11 item 13 already adds 0.08 s at 900 for unled sections.
- `accent_bodies.json`: remove 902 for Violins II, violas and celli.
- `accent_fits.json`: add `"902.0": 3.0` for Violins II, violas and celli. These are pre-hall swells; the c05 doc removed the hemiola onsets only because of the body cuts.
- Apply this together with ONE_TIME item 13 (the 900 sf bump) and measure both.

**Pass:**
- every string stroke at 902 / 904 within ±50 ms pcX;
- each of Violins II, violas and celli 2-4 dB over its 901.5 level at 902 + 0.1 s;
- the master rising 3 dB or more from 901.75 to 902.15;
- 906-910 unchanged.

### 4. Violins I's legato joins run 45 ms behind Violins II's, because Violins I alone has no Leg Slur lead extra (measured)

**Where.** Violins I, every Leg Slur MAX target: 118 joins. The doubled lines show it most:
- the trio return (209-224), with Violins II an octave below: Violins I +36 against Violins II +12 ms;
- the second idea.

**Evidence.**
- Median pcX: Violins I +49 ms, Violins II +3, violas +6, celli +27 (pcx.py summaries on c10).
- 32 of Violins I's 100 joins common to c08 and c10 read over +60 ms in both renders (62-185 ms). Only 1 reads under -20 ms.
- Configuration: `LEG_ART_EXTRA_S` gives Leg Slur MAX +0.04 s on Violins II, +0.05 on celli and +0.025 on violas, but nothing on Violins I (only Leg BC MAX +0.05). Violins I's total is 0.17 s, against 0.24 s on Violins II.
- Correction to `loop/LEARNINGS.md` (c10 line). The c10 check (`check10.py`) called `attack_pcx` without the previous pitch, so the bands overlapped: celli trio tune -19 ms, IQR -139..+46. With the exclusion, as pcx.py runs it, the same 30 joins read **+51 ms on c08 and +39 ms on c10** (windows 76 -> 61 ms). The v80 change helped by about 12 ms. It did not bring the joins to the beat.

**Fix.**
1. `build/score_config.py`: `LEG_ART_EXTRA_S["Violins I"]["Leg Slur MAX"] = 0.04`.
2. Subtract 0.04 from every Violins I offset already in `build/leg_leads.json` (59 onsets fitted on the old base), so the listed totals stay as fitted. The extra adds to them through `tot = clamp(ls_ + ex)`.
3. Correct the c10 LEARNINGS line.

**Pass:**
- Violins I median pcX +20 ms or less;
- joins over +60 ms reduced from 32 to 12 or fewer;
- no new joins under -40 ms;
- the probe's Violins I legato window still 70 ms or less.

### 5. Horns 1-2 slurred tenuto repeats (209-222): use "Leg Slur Rep MAX" instead of gaps (manual p.106; current dips measured, gain inferred)

**Where.** Horn 1 at 630, 633 and 663, and Horn 2 at 627, 642 and 651. These are the c10 open item: dips 1.6 / 1.7 / 1.7 and 2.6 / 3.6 / 1.9 dB, against a target of 3-6 dB. Two cycles of gap and Port Lng tuning have not reached it.

**What the manual offers.** p.106 describes Legato Slur Repetitions: consecutive same-pitch notes "without space between the notes" play a re-tongued sample inside the legato phrase. That is exactly a slurred tenuto repeat. 1FH KS Master has the row "Leg Slur Rep MAX" (`ks_maps.json`). The clarinets' whole-piece "Leg Slur Rep" (c03) took their slurred repeats from 0.0 to 3.6 dB.

**Fix** (`build/score_config.py`):
- `REP_ROW["Horn 1"] = REP_ROW["Horn 2"] = [(0.0, SCORE_END, "Leg Slur Rep MAX")]`. This is the clarinets' keyswitch-only form, so Leg Slur MAX unloads.
- Set `REP_ROW_REPEATS_ONLY = ()`. No brass track uses `REP_ROW` today, so nothing else changes.
- Remove Horn 1's Port Lng `ART_SPANS` (626.5-664) and the c10 `NOTE_END_AT` gaps: Horn 1 627 / 630 / 660, Horn 2 624 / 639 / 648.
- First render the repeats with `REP_ROW_GAP_S` (the woodwind timer values). If the row's script wants contiguous notes, as p.106 says, set the gap for these tracks to 0.

Memory, read from the .oib: Leg Slur Rep MAX 17,245 regions against Leg Slur MAX 13,990, minus Port Lng's 775. That is about +5.7 thousand regions for both horns, about 0.25 GB at c02's 4 GB per 92 thousand.

**Pass:** 3-6 dB dips at all six repeats, no hole over 8 dB, and the other horn legato joins unchanged within 20 ms pcX.

### 6. Hn 3 + Hn 4's unison countermelody is one solo horn (inferred; manual p.100)

**Where.** The tenor countermelody, espress. ff, at 105-120 and 305-320 (qn 312-357, 912-957). Horn 4's 28 notes are dropped as unisons, and Horn 3 plays them on 1FH with +3 dB (`UNI_BOOST`).

**What is wrong.** The score asks for two horns (Adler, cited in sC.ily c097: two horns in unison equal one trumpet). A boosted solo horn has one player's vibrato-free tone and one attack. The library records "2 French Horns" (p.100). 2FH KS Master has the same rows (Leg Slur MAX, Leg Slur Rep MAX, Sus MAX, Portato).

**Fix**, if memory allows after finding 5:
- give these two spans to Horn 4 on a `TRACK_WINDOWS` alias on `2 French Horns/06 Keyswitch/2FH KS Master.oib`, as a pass-2 track (MANUAL-GAPS memory plan);
- or move Horn 4's whole track to 2FH and keep its solo passages, which already are the low voice.

Measure the ensemble spread of the attacks and the level against the celli and Bassoon 1 doubling. The gain is inferred, so rank this below 1-5.

## Checked and fine, or not worth chasing (measured)

- **Accents (Dan: weight, not bite).** 2-5 kHz energy in the first 80 ms over the body (100-300 ms) of accented notes is *lower* than on unaccented notes in every section, by medians:

  | section | accented | unaccented |
  |---|---|---|
  | Violins I | -4.5 | +4.7 |
  | Violins II | -0.7 | +5.0 |
  | violas | -0.1 | +2.7 |
  | celli | -2.3 | +4.1 |
  | basses | -3.1 | +5.9 |
  | Oboe 1 | -2.7 | +2.8 |
  | cor anglais | -2.6 | +2.6 |
  | Flute 1 | +0.4 | +2.8 |

  The outliers are the hemiola onsets of finding 3 (celli 902 +16.6, violas 902 +14.1, measured at the early moved onset) and Flute 1 at 310 / 910 / 1010 (+9..+11, the ff tutti, where they are masked).
- **Brass tenuto quarters in the tutti** (Trombone 1, bass trombone, tuba, 312-357, Sus MAX). pcX -9..+9 ms median, and they reach -3 dB re peak by +40 ms. They are no longer the c04 swells.
- **Horn 1/2 StacSs quarters** pcX -16 / -21 ms. **Trumpets** pcX -12..-14 ms on the quarters.
- **Flute 1's staccato note-off step** (the c10 open item, 5.1 dB median on the stem in 84-132). The master step at the same moments is 1.6 dB (p75 2.2), with Flute 1 10 dB under the master. Not audible enough to justify taking lead from the following notes.
- **Pizz. -> arco entries.**
  - Celli 90 / 300 / 756 / 828: -13 / +62 / +5 / +5 ms.
  - Violins II / violas 816: +19 / +9.
  - Basses 300 / 576: +12 / -33.
  - Celli 504 (+248) and basses 504 / 1071 (+147) are the entries c10 reverted on the orchestrator's decision. I leave them alone.
- **Wind and string staccato pair dips (S1), stem medians by section.** Flute 1 4.8-10.2, Oboe 1 7.7-13.4, cor anglais 4.1-6.8, Clarinet 2 9.0-9.2, Violins I 3.4-7.4, Violins II 3.9-8.0 dB.
- **Clarinet 1's trio tune** (pcX +16..+21 ms, rSD 7-12). **The Violin I solo** (+16 ms). **Flute 1 col Vl. solo** (+5 ms, rSD 3).

Do not touch: the woodwind and string short-row leads and eighth lengths; the trumpets' StacSs DblTng rows and the Trumpet 1 pp step; the brass tenuto quarters on Sus MAX; Clarinet 1/2 "Leg Slur Rep"; the c10 celli `LEG_VEL_SPANS` v80 (keep it; finding 4 only corrects how it was measured); `LEGATO_MONO_CC22`; the Violin I solo's v82 / 0.15 s legato; the harp's chords and arpeggios; the timpani roll ends, `TIMP_DAMP_AT` and `TIMP_STAC_ROW`; the Violins I re-bow fills; Violins I's 902 / 904 leads (on time); and every item in HISTORY's c10 do-not-touch list.

# Cycle 31, critic A: articulation and phrasing (on the c30 render)

Sources: `cycles/c30/render` stems and master, `cycles/c29/render` for comparison, `cycles/c30/CHANGES.md`, `build/parts.json` (the c30 state after the stem fix), `cycles/c30/before/parts.json` (the c29 state), `build/score_config.py`, `build/roles.json`, `build/early_fills.json`, `build/mix.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py` (`cc1_fn0`, `CC1_DYN_MAP`, `WIND_REP_RETONGUE`), the woodwind KS Master maps in `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, the May 2021 HO manual PDF pp.108-113 (row A4 of `loop/MANUAL-READING.md`, cycle 31), `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md`, the c30 critic A report.

Times are score qn unless marked s. Levels are plain RMS of the stem or master in 20-30 ms windows (joins, attacks, repeats) or 0.25 qn windows (phrase traces). Scratch scripts were deleted after use.

## Manual notes (A4, PDF pp.108-113: Hollywood Orchestral Woodwinds)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Flute 2 is a different player, seated differently; no samples are shared with Flute (p.108) | Flute 2 (FL2 KS Master), the unisons with Flute 1 at 204-212 and 262-271 | Yes. Flute 2 has its own patch. |
| Sustain dynamics "controlled with the Mod Wheel", 3 layers always playing (p.109) | every wind sustain | Play-era text. In the Opus patches, CC11 sets the dynamic on the flute, oboe, cor anglais, bassoon, bass clarinet and contrabassoon KS Masters, and CC1 crossfades non-vibrato and vibrato. CC1 sets the dynamic on the Clarinet KS Master (read in c30). The render follows the patches. |
| Sus Expressive: "a slower attack and a gently increasing vibrato" (p.109). The KS Masters also have Leg Slur Exp (FL key 35, OB 35, EH 35, BS 77; not CL or BC) | the espr./dolce solo entries (Oboe 1 at 42 and 139, bass clarinet at 91, cor anglais at 93, 124, 151 and 286, Flute 1 at 108, Clarinet 1 at 280) | Not used. These entries reach full body in 30-50 ms, ahead of the beat (finding 4). |
| Legato Repetitions RRx4: a non-vibrato sustain plus a re-tongued attack with 4 round robins, "for repeated notes within an otherwise legato phrase" (p.109-110). Every wind KS Master has the row (key 31) | the same-pitch repeats inside wind slurs: Bassoon 2 at 253 (a tenuto repeat), 144 and 21; Bassoon 1 at 148 and 235; Oboe 1 at 148; cor anglais at 160; Clarinet 1 at 289 | Not used. The repeats are re-tongued with a gap and a CC11 fall (`WIND_REP_RETONGUE`). Bassoon 2's 253 repeat does not separate (finding 3). |
| Shorts have no release trails. Hold the MIDI note long enough for the room to ring (p.110) | none: v600's winds have no staccato or marcato shorts | Not applicable. |
| Repetitions, trills, flutter, FX, Sing (p.111-112) | none in v600 | Not applicable. |
| Legato: a slur only with no gap and within an octave (D3 to D4 yes, D3 to D sharp 4 no); monophonic by default, CC22 0-63 polyphonic (p.112) | every Leg row | Followed (measured on parts.json): no slurred interval over 12 semitones on any Leg row, no chords on a Leg row, and no gap inside a slur except at deliberate slur boundaries (13 cases of 0.03-0.06 qn, all where a new slur starts). |
| Legato Slur Repetitions: same-pitch notes without space use a re-tongued sample (p.112). Present as Leg Slur Rep in FL (36), OB (36), EH (36) and CL (35); not in BS or BC | Flute 1 at 136 and cor anglais at 271 (slurred repeats merged with a notch); Clarinet 1 at 289 | Not used. Fl1 136 dips 8.7 dB on the stem (2.0 dB on the master); CA 271 dips 3.7 dB on the stem. The cor anglais repeat would be the first place to try Leg Slur Rep. |
| Slur Runs: strong portamento slur, only for steps of a minor or major second (p.112) | Flute 1 and Violins I's run into bar 79 (261.5-262: 89-91-92-94, steps of 2, 1 and 2 semitones, about 0.22 s each in the allargando) | Not used. At this speed Leg Slur MAX is the right row. Slur Runs would add a glissando the score does not ask for. |
| MANUAL-GAPS #2 (repetition rows), #5 (expressive rows) | as above | Both still "never". Findings 3 and 4 give the passages to test them on. |

## Findings, ranked by what a listener would hear

### 1. Horn 1's dolce espr. theme: since c30, each legato note swells at its start and then drops 7-10 dB under the bassoons and bass clarinet

- **Where.** Horn 1, bars 7-14 (qn 17-42, "dolce espr.", p to mp), bars 55-58 (176-188), and bars 65-70 (226-238, "dolce" alone over the basses' pedal). Every legato target with CC1 between about 30 and 54.
- **What is wrong (measured).** The note reaches its level within about 0.35 s of the moved onset, then falls and stays down. CC1, CC11 and the volume envelope are flat inside these notes.

  | note (qn) | CC1 c29 -> c30 | c29: head minus body | c30: head minus body (worst) |
  |---|---|---|---|
  | 18.0 A flat 3 | 66 -> 42 | 2.5 dB | 9.9 (11.6) dB |
  | 22.0 | 66 -> 50 | 2.9 | 9.4 (19.0) |
  | 23.0 | 65 -> 46 | -1.5 | 10.3 (14.4) |
  | 24.0 | 64 -> 42 | 4.8 | 8.2 |
  | 26.0 | 64 -> 42 | 0.4 | 7.2 |
  | 30.0 A flat 3 | 64 -> 42 | 0.9 | 9.8 (11.4) |
  | 35.0, 36.0 | 67 -> 52, 66 -> 49 | 3.2, 1.2 | 8.3, 7.7 |
  | 182.0, 184.0, 186.0 | 70 -> 54 | 4.1, 3.9, 2.5 | 13.4, 8.2, 8.3 |
  | 230.0, 231.0 | 67 -> 50, 66 -> 46 | -0.5, 2.6 | 7.1, 7.8 |

  - Head = the loudest 30 ms frame in 0.03-0.35 s. Body = the median from 0.45 s to the note's end. Median over Horn 1's 33 notes of 0.9 s or longer: c29 -1.5 dB, c30 +1.7 dB.
  - Example trace, qn 30 (30 ms frames). c30: -44/-45 dB until +0.41 s, then -48, -51, -53, and -54/-55 from +0.7 s to the next note. c29: -46/-47 dB throughout.
  - Against the accompaniment, A flat 3 at 18.75-19.4: Horn 1 -52 dB, bass clarinet -46, Bassoon 2 -50, Bassoon 1 -51. At 30.6-31.4: Horn 1 -52, Bassoon 2 -48, bass clarinet -49. The tune goes under its own accompaniment in the middle of every long note. The master swings 3-6 dB with it (bars 7-8: -40 -> -43 dB, c29 flat at -41/-40).
  - Bars 68-70 (232-235, a tied B flat 3 under a printed decrescendo mp -> pp): c30 -43 -> -49 -> -53 -> -56 dB at 234, then back up to -47 at 236-237 once CC1 reaches 28. c29 fell evenly, -42 -> -47. The horn plays a dip and then a swell where the score prints one diminuendo.
- **Cause (inferred from measurements, not isolated).** Body level (stem minus vol_db) against CC1 on Horn 1: CC1 24-29 -49.1 dB (CC11 37); 30-35 -56.5 (CC11 42); 36-41 -50.4; 42-47 -51.0 (CC11 48); 48-53 -44.0 (CC11 56). The sustain layers of the 1FH KS Master sum low where CC1 crossfades the pp and mf groups (about 30-47; table in c30 CHANGES.md: pp 0.59 at 30 and 0 at 50, mf 0.45 at 30 and 1.0 at 50). The legato transition samples are not lowered the same way. c30's p trim (+9.6 dB, `mix.json` Horn 1 `soft_trim_db`) was fitted on note medians, so it raised the transitions as well. The early fills at 22, 24, 26, 27, 36 and 37.5 (+2.1 to +3.8 dB, fitted on c16-c28 middle-layer sags) now sit on top of the transition. The p generic map value is `CC1_DYN_MAP` (46, 42), the middle of that band. mp (58, 54) sits at its edge. The clarinets and trombones do not show the effect: their median head-minus-body is -1.1 to +0.6 dB. Horn 3 shows it once (87, CC1 28, +6.5 dB).
- **Fix.**
  - (a) New option `CC1_DYN_MAP_BY = {"Horn": [(22, 18), (34, 24), (46, 26), (52, 50), (58, 54), (72, 68), (88, 86), (114, 108), (124, 120)]}` in `tools/score_to_parts.py` (default `{}`, used in `cc1_fn0` in place of `CC1_DYN_MAP` when the track name starts with a key). pp and p then play the pp group alone, mp and up the mf group, and a hairpin crosses 27-49 in one step. Also add a rule that a held note never rests in 28-48: move CC1 across that band within 0.15 s at the crossing point.
  - (b) Delete Horn 1's pre-c30 early fills (`build/early_fills.json` "Horn 1" 22, 24, 26, 27, 36, 37.5, 231). Run `tools/auto_fills.py` on the next render, not on this one.
  - (c) After the render, refit Horn 1's ppp/pp/p/mp `soft_trim_db` (and Horns 2-4 and the a2 track the same way) by stem fix on note bodies (+0.45 s to the end), not on whole-note medians. The current p trim of +9.6 is in effect fitted on the transitions.
  - Fallback if (a) gives a pp group too dark for "dolce espr.": a Horn map that keeps soft notes at CC1 50 (the mf group alone; c29 had 64 and measured flat bodies), with the level from the trims.
- **Check after the render.** On Horn 1's notes of 0.7 s or longer in bars 7-14, 55-58 and 65-70: head minus body at most 3 dB on every note. Horn 1 body 2-4 dB over the louder of Bassoons 1-2 and the bass clarinet at 18.75-19.4, 23.5-23.95 and 30.6-31.4. The 229-235 decrescendo falling monotonically. Horn 1's 1-5 kHz share at p still at least 4 dB under its f.

### 2. Bar 63 (qn 212), strings sf trem.: the climax is cut in the post-hall volume envelope. A role boundary drops Violins II 4.5 dB in one sample at the sf, and the decrescendo falls 10-13 dB in vol_db (S3). This is also the cause of the probe's "Violins II 212 tremolo dip" (flagged every cycle since c27)

- **Where.** Violins I, Violins II, violas and celli at 211.99-213.0: sf + trem. + decrescendo, under Trombone 1's ff entry at 212.5.
- **What happens (measured, parts.json and stems).**
  - `roles.json` Violins II [204,212,+2] is followed by [212,216,-6]. With the [211.75,213.0,+1.5] ramp, vol_db goes +4.88 dB at 211.999 -> +0.41 at 212.000. That is a 4.5 dB step down in one sample on the downbeat of the climax's tremolo.
  - Violins I: -0.63 -> -3.60 at 212.000 (the [204,208,-1.5] role and the sostenuto shapes).
  - The Violins II stem shows it as a hole on the downbeat: -29 dB at -0.04 s, -35 at +0.01 s, then -24/-21 at +0.11..+0.16 s (the sf). The attack probe reads this as the 6.5 dB "tremolo dip"; it is the envelope step, not the tremolo sample.
  - The rest of the fall is also post-hall (c30 report A #3, unchanged in c30): Violins II vol_db -6.2 at 212.25, -11.9 at 212.75, -13.0 at 213.0. Violins I falls to -9 and the violas to -6.5. The master goes from -15 dB at +0.06..+0.21 s to -21/-24 dB by +0.5..+0.8 s, while the trombone's first note is still rising.
- **Why it matters (inferred, S3: Movement I c36, this series' c29 violas and c30 niente CC7 fixes).** A downward step or fast fall in vol_db removes the hall tail of the ff with the dry sound. The listener hears the climax's room switched off at the sf, then the trombone entering into a dry hall. Because S3's mechanism is measured, but this case's hall/dry split was not, the audible size is inferred.
- **Fix (`build/score_config.py`, c31 block).**
  - Move the 212 role boundary into the sf ramp. Change Violins II [204,212,2] to end at 211.75, so the +2 -> -6 change happens inside the [211.75,213.0,1.5,0.5] ramp, not as a step.
  - Put the post-sf fall of all four tracks into CC7. For each of Violins I/II, violas and celli: take vol_db(q) - vol_db(212.06) over 212.06-213.0 and write it as `CC7_POINTS[track]` every 0.06 qn (CC7 = 127·10^(dB/20)). Hold vol_db at its 212.06 value over that span. Return CC7 to 127 over 213.0-214.5 while vol_db falls by the same dB (equal slow ramps on both sides of the hall are inaudible; inferred).
  - Generic version for later cycles: a `ROLE_STEP_TO_CC7` rule in `tools/score_to_parts.py` that sends any downward role/trim step of 3 dB or more under a sounding note into CC7.
- **Check after the render.** No vol_db change over 1 dB per 0.06 qn on these four tracks over 211.9-213.0. The Violins II stem has no frame under its 211.8 level before the sf peak (probe 212 not flagged). Stem and master at 213.0 within ±1.5 dB of c30. The trombone 212.5-213 level unchanged (roles [212.6,213.6,-2] stay).

### 3. Repeated notes inside wind slurs: Bassoon 2's tenuto repeat at 253 is not heard as a second note (0.5 dB), and the bassoon/horn repeats in bars 48 and 80 are marginal (S1)

- **Where (measured: dip = the level of 0.15-0.35 s before the onset minus the minimum within -0.2..+0.15 s).**

  | track, qn | score | stem dip | master dip |
  |---|---|---|---|
  | Bassoon 2, 253 (D flat 3, bar 78) | `des4 des2--` inside a slur, p crescendo | **0.5 dB** | 1.3 dB |
  | Bassoon 2, 144 | same-pitch repeat | 4.2 | 4.3 |
  | Bassoon 2, 265 | ff, bar 80 | 3.6 | 2.6 |
  | Contrabassoon, 265 | ff, bar 80 | 4.7 | 2.6 |
  | Horn 3 / Horn 4, 265 | ff, bar 80 | 4.4 / 4.7 | 2.6 |
  | Bassoon 1, 148 / 235 | repeats | 10.7 / 8.8 | 4.3 / 4.6 |
  | Oboe 1 148, cor anglais 160, Clarinet 1 289 | repeats | 6.8, 10.6, 8.9 | 4.3, 8.2, 3.7 |

  - At 253 the gap is 0.07 qn (0.08 s), and CC11 falls 59 -> 54 before the repeat. Bassoon 2's D flat 3 body carries a level wobble of about ±3 dB at about 4 Hz (amplitude modulation in the Sus MAX sample: peaks of -42.7/-43.5/-42.4 dB at -0.61/-0.37/-0.13 s, troughs of -49.4/-49.0 dB between them). The re-tongue's dip (-46.0 at -0.01 s) is shallower than the wobble's troughs. A listener hears one long note with a tremor, not a tenuto repeat.
  - Bar 80 is the ff cadence with the strings sustaining, so its master dips of 2.6 dB are covered in part. The stems are still weak against the 3-6 dB target used since c27 (MANUAL-GAPS #2).
- **Fix.**
  - (a) Bassoons and contrabassoon: `WIND_REP_RETONGUE_BY = {"Bassoon": {"gap_s": 0.09, "frac": 0.25, "fall_cc": 12, "fall_s": 0.15}, "Contrabassoon": {"gap_s": 0.09, "frac": 0.25, "fall_cc": 10, "fall_s": 0.15}}` in `build/score_config.py`. The horns need a deeper fall as well (Movement I c06: the horn release fills a 0.06 s gap): `"Horn": {"gap_s": 0.08, "frac": 0.25, "fall_cc": 10, "fall_s": 0.15}`. Note that on the horns CC11 now only scales volume, since CC1 carries the layer.
  - (b) Manual route (p.109-110, MANUAL-GAPS #2), one passage as a test: put Bassoon 2's 252-255 on the BS KS Master's LegRep RRx4 row (key 31) with `ART_SPANS["Bassoon 2"] = [{"from": 251.9, "to": 254.95, "art": "LegRep RRx4"}]`. Every note then gets the row's non-vibrato sustain plus a re-tongued attack. This also removes the wobble that hides the repeat. The row adds one loaded row to one track.
- **Check after the render.** Bassoon 2 253 stem dip at least 6 dB with the second note's body within 2 dB of the first. Every repeat in the table at least 5 dB on its stem. Master at 144, 148 and 253 at least 3 dB. No new gap at the start of the 255 slur.

### 4. The espr./dolce wind solo entries are tongued, not breathed in: full body in 30-50 ms, reached before the beat

- **Where.** The first notes of the wind solos.

  | entry | mark | moved onset | body - 12 dB | body - 3 dB |
  |---|---|---|---|---|
  | Oboe 1, 42 | dolce | -0.07 qn | -0.10 s | +0.04 s |
  | Oboe 1, 139 | dolce espr. | -0.11 qn | -0.09 s | -0.07 s |
  | bass clarinet, 91 | solo, espr. | -0.10 qn | -0.09 s | -0.04 s |
  | cor anglais, 93 | dolce | -0.10 qn | -0.09 s | +0.01 s |
  | Flute 1, 108 | dolce cantabile | -0.08 qn | -0.09 s | -0.05 s |
  | cor anglais, 124 | solo, dolce cantabile | -0.07 qn | -0.09 s | -0.03 s |
  | cor anglais, 151 | solo, espr. | -0.10 qn | -0.06 s | -0.04 s |
  | Clarinet 1, 280 | dolce | -0.15 qn | -0.13 s | +0.06 s |

  All have velocity 53. The cor anglais at 286 is the exception: +0.24 s to body - 3 dB.
- **What is wrong (measured rise; musical judgement inferred).**
  - Seven of eight entries go from 12 dB under to 3 dB under the body in 20-130 ms, and six reach body - 3 dB before the beat. The perceived attack centre is about 0.05 s early, and the shape is a tongued attack.
  - A dolce or espr. solo entry at p in an Adagio is normally a soft, breathed start that grows over 0.15-0.3 s with the vibrato coming in after it. That is what the manual's Sus Expressive is: "a slower attack and a gently increasing vibrato" (p.109).
  - The current entries are the Leg Slur MAX first-note sustain with an entry lead fitted for a fast attack (S2).
- **Fix (MANUAL-GAPS #5).**
  - Load the KS Masters' Leg Slur Exp row for these phrases on the tracks that have it: Oboe 1 (key 35), cor anglais (35), Flute 1 (35). Use `ART_SPANS` covering each slur from its first note to the slur end. The whole slur must stay on one legato row, because a Sus Exp first note followed by a Leg Slur MAX keyswitch would lose the first transition (p.112).
  - Re-measure the entry lead on the first render and set it so that body - 3 dB lands at +0.05..+0.15 s after the beat. That probably means a lead of 0, not the current 0.07-0.11 qn.
  - Clarinet 1 and the bass clarinet have no Leg Slur Exp; their KS Masters have Sus Exp (key 30). For their solo entries, a CC11 fade-in over the first 0.2 s (+0 -> body) with the entry lead removed is the substitute.
  - Do this on Oboe 1 at 42 and 139 and Flute 1 at 108 first. Their phrases are slurred throughout, so the row change is clean.
- **Check after the render.** Body - 12 dB to body - 3 dB takes 0.12-0.3 s on these entries. Body - 3 dB within -0.02..+0.15 s of the beat. Legato joins inside the phrases still under 3 dB (Leg Slur Exp transitions are slower; check that no target arrives late against the strings, S2). Phrase level within ±1 dB of c30 relative to the accompaniment (the Exp row may sit at a different level; correct it with the role, not CC11).

### 5. The bars 17-22 violin solo still has almost no vibrato on its long notes (c30 A #1, deferred; the data is unchanged)

- **Where.** Violin I solo (DIV A half section), qn 48-65, "solo, senza sord., dolce". Worst on the two long E flat 5s at 51-53 and 63-65.
- **State (read).** The solo's CC1 lane is identical in c29 and c30 (parts.json): 95 on most notes, which is the overlap of the Sus Vib (0.67) and Molto Vib (0.85) layers; 75 rising to 95 on the long notes. c30 A measured 2.6-3.2 c of vibrato on those notes against 30-60 c for a solo player (that range is inferred), so it sounds like a muted small section.
- **Fix (as c30 A #1).** `VIB_TGT = {"Violin I solo": 112}` and `VIB_DIP_FLOOR = {"Violin I solo": 106}` in `cc1_fn0`, so the track stays on the Molto Vib layer alone. Correct the level with the track's role [48,65,2], not CC11.
  - The better patch is Hollywood Solo Violin LegSus (p.81), which is not installed (MANUAL-GAPS #3).
  - The orchestral strings have no solo violin, so DIV A with molto vibrato is the closest installed option to "solo, dolce". The full section would be further off.
- **Check after the render.** At least 12-15 c peak to peak, with one spectral peak at 5-7 Hz, on 49, 51, 61 and 63 (46 ms autocorrelation pitch track, band-passed 4-8 Hz). Solo phrase level within ±1 dB of c30 relative to Oboe 1.

### 6. Clarinet 1 still slurs over the breath before bar 81 (qn 268): same 0.12 qn gap as the others, but a 6.5 dB dip against their 16-24 dB

- **Where.** The breath printed for all winds at 268, after the ff of bars 79-80.
- **Measured (c30).** Every wind ends its 267 note at 267.88 (gap 0.12 qn; c30's A #5 fix took the lead off). Dips: Flute 1 21.9 dB, Flute 2 23.7, Oboe 1 16.0, Oboe 2 18.8, cor anglais 22.3, bass clarinet 10.6, contrabassoon 8.5, **Clarinet 1 6.5**. The Leg Slur release trail of the CL KS Master fills the gap. The breath is in the score for the whole wind section, and the melody-carrying clarinet is the one that does not take it.
- **Fix (`build/score_config.py`).** For Clarinet 1, end the 267 note at 267.80 and fall CC11 by 14 over its last 0.15 s, returning at 268. The existing breath machinery (`breath_splits`) may already take a per-track gap; if it does, use `{"Clarinet 1": {268.0: 0.2}}`. Leave the other winds as they are.
- **Check after the render.** Clarinet 1 dip at 268 of 10-15 dB. The 268 entry within ±0.03 qn of Oboe 1's.

## Smaller observations (not ranked)

- **Legato data (measured, parts.json).** No chord, no overlap problem and no interval over an octave on any Leg row. The 13 gaps of 0.03-0.06 qn inside my slur windows are all at slur boundaries where a new slur starts on the same beat, which is correct.
- **Re-bows (measured; c30 changed no string re-bow, so all 87 re-bows read the same as c29).** Median dip 3.4 dB. Still over 6 dB: Violins I opening C5 2.4/4.6 (8.0/6.3 dB on the stem; the master dips 2-3 dB), Double basses 221.8 (7.9) and 283.6 (9.2), Violoncellos 147.8 (7.1), Violins II div 113.7 (7.3), Violas div 302.95 (6.7). The coda basses' fitted fills still swing ±5 dB within 0.1 qn (`rebow_fills.json`; see vol_db at 228.0-228.7: +1.0 -> +8.3 -> +2.6 dB). c30 A #6's refit with `FILL_SMOOTH_S` 0.25 is still the right fix. No loop pulse was reported on the c30 master.
- **Violas' portato eighths, bars 48-51; Violins II portato pairs, bars 15-21; pizz. 37-44; sul tasto Flautando 37-40; mutes (CC15 changes all in rests, the solo senza sord., Horns 3/4 con sord. from 271.5); tremolos 204-218 not re-bowed.** The data is unchanged since c30's checks, which passed them. Not re-measured.
- **Trombone 1, bars 63-64 (BRIEF item 9).** c30's ff-layer accents measured 2-5 kHz minus body at -17.1 (213) and -4.4 dB (218), weight with no bite. Keep.
- **Wind vibrato (measured, autocorrelation pitch track on the stems, with the reverb in).** Oboe 1, Flute 1 and the cor anglais show a coherent 4.2-4.8 Hz pitch modulation on long notes: the peak stands 8-50x the median of the spectrum. The 3-9 c depths read on wet stems understate the dry vibrato, so I make no claim about depth. Bassoon 1 at CC1 40-47 has none (1-3 c, no peak), which suits the bassoons' accompanying role in bars 7-14.
- **Better patches considered.** Basses/Celli DIV A for the 4 soli passages (MANUAL-GAPS #8), memory permitting. Leg Slur Rep on the cor anglais 271 slurred repeat (3.7 dB on the stem). Horn portato rows for the 61-62 tenutos are not needed (c29: master dips at most 2.2 dB). No 2-player horn patch is needed beyond the existing a2 track, but it shares finding 1's CC1 band (2FH KS Master), so apply the horn map to it too.

## Do not touch

Trombone 1's legato quotation, its shapes and its ff-layer accents (213, 218). The Violas Detache row with its entry leads and CC7 level (bars 48-51). The Violins II portato notches and the 45/51 re-bows. CC15 mute placement. The c30 niente CC7 lanes in bar 66. The final-chord, opening-chord and bar 66 re-bow times. The harp damp at bar 83. The Violin I solo's legato leads. The CC1 layer map on the trombones, tuba and clarinets (bodies flat, no finding-1 effect). Keyswitch placement and monophonic Leg rows (no chords, no octave-plus slurs).

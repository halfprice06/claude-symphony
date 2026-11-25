# Cycle 22, critic A: articulation and phrasing (on the c21 render)

The numbers below come from `cycles/c21/render/` (stems and master), the c20 and c19 stems, `build/parts.json` (the c21 data), `cycles/c21/before/parts.json` (the c20 data), `build/mockup-events.tsv`, and the installed `.oib` patch files, which I read as gzip JSON and did not change. "Measured" means a number taken from these files. "Inferred" means a conclusion that a render has to confirm. Nobody heard the audio. No fix below moves the track volume envelope per note. Every fix is in CC11 / CC1, velocities, note lengths, rows, release times or an Opus state setting.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 22 (its third round ends at c20), so I skipped the fixed reading and read the pages behind my findings, plus `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) / patch file | Where it applies | Does the render follow it |
|---|---|---|
| p.144, Monophonic True Legato: velocity sets transition timing; "around a Note Velocity range of 50-60" gives a longer transition, 110-127 a shorter one; velocity does not change loudness | Wind legato targets (finding 3): they play at velocity 60-100, and none plays above 100 | Partly. The strings and brass have a velocity floor (`LEG_VEL_STRONG`, 100-124). The winds have none, and 46 % of their targets at velocity 71-90 have a hole of 6 dB or more |
| p.105, brass Legato Slur: "MIDI Velocity is used to control the speed of the legato transitions"; the volume is on the Mod Wheel | Horn 1 legato targets (finding 3) | Followed (velocity 100-118) |
| p.112, woodwind Legato Slur: joins without a gap, within an octave; "3 sustain samples plus slur samples per note" | Finding 3 | The patch files show how the transition and the sustain are combined. In `FL KS Master` "Leg Slur MAX", the "TLeg" groups have a 54 ms attack and a 175 ms hold, then a 260 ms decay. The "1Fls" sustain groups under the target fade in over 250 / 625 / **738 ms**. In `OB KS Master`, "TLeg" has a 54 ms attack, a 264 ms hold and a 177 ms decay to 0, and "OBs" has a **440 ms** attack. The c21 critic read 465 ms on `EH KS Master` "EHs". A first note uses the 8 ms groups ("1Fl", "OB"). This explains the hole between the transition and the sustain |
| p.101, brass sustain; `1TP KS Master` sustain groups (c21: release set to 300 ms on Sus Non Vib MAX, Leg Slur MAX, Mute Sus) | Trumpet re-tongued repeats (finding 1) | The longer release worked for the note ends, but it now fills the re-tongue gap (finding 1) |
| p.101 / p.106 / p.109-110, Legato Repetitions and Legato Slur Repetitions (re-tongued repeat samples). MANUAL-GAPS #2 | The chorale's repeated brass whole notes (finding 2) | Not used for brass (`rep_row` is empty on every brass track; memory). The emulation in finding 2 is the cheaper fix |
| DIGEST p.99 / p.144: string "Leg BC" and "Leg Slur" rows, velocity as transition speed | Scherzo c19 note: the string Leg Slur MAX swell peaks about 70 ms after the note-on | Does not apply here (measured). The median target shape peaks +1.0 dB at +20..+60 ms on Violins I (16 targets) and +1.6 dB at +60 ms on the violas (31) |

## Findings, ranked by what a listener would gain

### 1. The trumpets' repeated notes no longer re-tongue: c21's 300 ms release fills the gap (measured; fix values partly inferred)

Where: Trumpets 1-3, every repeat in `rep_retongued`. These are the Più allegro's hammered half notes on Trumpet 3 (qn 986-1086, bars 247-272), the coda's dotted figures (793.5-813, bars 199-204), the codetta (361.5-372) and the retransition (588-596).

Evidence. I measured each repeat's dip (150-6000 Hz band, 20 ms windows): the new note's peak in its first 0.12 s minus the floor from 0.15 s before to 0.03 s after its moved note-on. The note data is identical in c20 and c21. Only the release changed (178 -> 300 ms at f / ff).

| track | n | median dip c20 -> c21 | under 3 dB c20 -> c21 |
|---|---|---|---|
| Trumpet 1 | 11 | 9.2 -> 4.1 | 0 -> 4 |
| Trumpet 2 | 11 | 9.0 -> 4.7 | 0 -> 1 |
| Trumpet 3 | 29 | 8.9 -> 4.5 | 0 -> 3 |
| Horn 3 / Horn 4 (237 ms release, gap 0.10-0.14 s, fall 12-14) | 25 / 25 | 8.0 / 10.0 | 3 / 2 |
| Trombone 2 (237 ms, gap 0.08 s, fall 10) | 24 | 8.5 | 1 |

Worst c21 cases:
- Trumpet 1 372 (1.4 dB), 813 (2.5), 794 (2.8), 588 (2.3).
- Trumpet 2 813 (1.1).
- Trumpet 3 1018 (1.3), 1046 (2.4), 813 (2.3).
- Trumpet 3's repeated half notes in 1018-1046 fell from 7-10 dB to 1.3-4.8 dB.
- The staccato row (not capped) still separates: Trumpet 1 361.5 is 10.8 dB.

The trumpets use the generic `WIND_REP_RETONGUE`: a 0.06 s gap and a 6-unit fall. Every other brass track has its own wider gap and deeper fall (`WIND_REP_RETONGUE_BY`). The trumpets did not need one while their release was 178 ms.

c21's target for note ends was -15 to -22 dB at +0.2 s. With 300 ms the trumpets read -14.2 / -15.9 / -15.4 dB, at or past the loud end of that range. Trombones 1-2 at 237 ms read -15 / -17 dB.

Fix (`build/score_config.py`; the release step is an Opus state change, so rebuild Trumpets 1-3 fully):
- Add `"Trumpet": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}` to `WIND_REP_RETONGUE_BY` (the horns' values).
- `build/mix.json`, Trumpets 1-3 `sus_release_cap_ms` (`"set": true`): change f and ff from 300 to 240 ms. Keep p / mf at 300 ms. Those are the soft phrase ends and the muted solo, where few repeats occur.
- Expected (inferred from the horns and trombones at 237 ms): dips 7-9 dB, and note ends at +0.2 s about -15..-17 dB.
- Pass: median dip 7 dB or more on each trumpet, none under 3 dB, and at least 5 dB on the 1018-1046 half notes. Note ends at +0.2 s between -14 and -20 dB.

### 2. The chorale's repeated brass whole notes (bars 224-234) swell instead of re-tonguing: the new note-on lands inside the CC11 fall (measured; fix inferred)

Where: qn 894-936.
- Horn 1 896 / 900 / 908 (G4 G4 G4, F4 F4).
- Horn 4 900; Horn 2 896.
- Trombone 1 and Bass trombone 920 / 924 / 928 (repeated C4 / C3, f, decresc. from 928).
- Oboe 1 928 / 932.

There are no slurs in the score. These are separate whole notes at Maestoso 2 = 56.

Evidence:
- Dips on the finding-1 measure: Horn 1 896 1.1, 900 0.7, 908 2.8 dB; Horn 4 900 0.6; Trombone 1 920 / 924 / 928 1.6 / 1.5 / 1.6; Bass trombone 1.6 / 1.7 / 1.4; Oboe 1 928 1.7, 932 0.7.
- The envelope at Trombone 1 920 falls 5.5 dB over 0.1 s, then rises back over 0.25 s. At Horn 1 896 it falls 4.8 dB and rises over 0.2 s. That is a soft swell, not a tongued re-attack.
- Cause (parts.json). c19's chorale block (`_C19_LEAD`, INSTR_POST `onset_lead` with `"set": True`) moves these note-ons 0.12-0.15 s earlier (Trombone 1 0.15, Bass trombone 0.13, Horn 1 0.12). The `WIND_REP_RETONGUE` CC11 fall stays on the old timing:
  - Trombone 1: CC11 86 at 919.50, falling to 78 at 919.72. That is the moved note-on. The lane is back at 88 only at 919.90.
  - Horn 1: CC11 91 -> 80 at 895.64. The lane is back at 92 at 895.82, and the note-on is at 895.773.
  - So the new note starts 8-10 units low and swells up.
- Across all 430 wind / brass re-tongued repeats:

  | CC11 rise in the 0.15 s after the new note-on | n | median dip | under 3 dB |
  |---|---|---|---|
  | 1 unit or less | 340 | 8.2 dB | 28 |
  | 8 units or more | 10 | 1.7 dB | 7 |

  Eight of those ten are the chorale notes above.
- In the master, the bar lines 896-932 show only a 0-5 dB articulation in 60-500 Hz.

Fix:
- `tools/instr_post.py`, `onset_lead` handler: when a `"set"` row moves a note-on earlier by Δ, move the CC11 fall-and-return points of the preceding same-pitch note's re-tongue fall by the same Δ. The rule is generic: the lane must be back at its value at least 0.01 qn before the moved note-on.
- `build/score_config.py`, c19 chorale block: for the same-pitch `gap_set` rows (`"pitch": "same"`, gap 0.025 s), give the old note a deeper fall of 18 units over its last 0.12 s on horns, trombones, bass trombone and tuba (for example a new key `"fall_cc": 18` on that row). Keep the 0.025 s gap and the pitch-change overlaps, which fixed c18's ensemble holes.
- Expected (inferred: the measured 0.45-0.7 dB per unit, from Horn 1's 11 units -> 4.8 dB and Trombone 1's 8 units -> 5.5 dB): dips of 7-10 dB with a fresh attack.
- Pass: each listed repeat 6 dB or more. In the master's 60-500 Hz band, no bar-line hole over 6 dB (c18 had 4-12 dB on 20 tracks at once and was ruled a fault).

### 3. A third of the wind legato targets have a 6-13 dB hole 0.1-0.4 s after the note-on; it is the same hole in c20 and c21 (measured; fix inferred)

Measure. Legato targets of 0.6 s or more, after a note of 0.4 s or more, 150-5000 Hz, 30 ms windows. The hole is the lower of (the previous note's last 0.25 s, the target's body at 0.45-0.8 s) minus the minimum in the first 0.45 s after the moved note-on.

| track | targets | 6 dB or more c20 / c21 (same notes in both) |
|---|---|---|
| Flute 1 | 20 | 6 / 5 (5) |
| Flute 2 | 9 | 7 / 6 (5) |
| Oboe 1 | 21 | 6 / 5 (5) |
| Cor anglais | 11 | 5 / 5 (4) |
| Clarinet 1 | 23 | 5 / 5 (5) |
| Clarinet 2 | 9 | 4 / 3 (3) |
| Bassoon 1 | 16 | 8 / 7 (7) |
| Horn 1 | 21 | 4 / 4 (4) |
| Trumpet 1 | 20 | 4 / 1 |

Worst cases:
- Oboe 1: 384 (73 -> 72, v60) 13.0 dB; 1014 (71 -> 72, v88) 12.0; 844 (v68) 11.0; 848 (v88) 9.0.
- Flute 1: 330 (87 -> 82, v80) 12.4; 848 (v88) 12.4; 964 (v60) 11.4.
- Flute 2: 842 (v100) 13.8; 602 / 634 / 1074 (84 -> 79, v100) 9.5-9.6. These four have 174-204 ms overlaps on the legato row, which the Movement II note says to check against the row each note plays.
- Cor anglais: 738 9.8, 650 8.7. Clarinet 1: 940 9.0, 606 8.4.
- Horn 1: 868 (61 -> 65) 7.8 dB at +0.31 s; 90 (63 -> 62) 7.8 at +0.27; 286 6.1 at +0.35. This is the scherzo's Horn 1 fault (a hole at +0.30 s in the transition sample), so that finding applies here.

The holes follow velocity, across all 109 wind targets:

| velocity | n | median hole | 6 dB or more |
|---|---|---|---|
| 60-70 | 23 | 4.0 dB | 8 |
| 71-90 | 48 | 5.2 dB | 22 |
| 91-110 | 38 | 3.7 dB | 6 |

Cause, from the patch tables (Manual notes): the transition sample lasts about 0.5 s, and the target's sustain fades in over 440-738 ms. The sum dips between them. A higher velocity plays a shorter transition (p.144).

This is the c21 cor anglais bloom in another form. c21's TLeg region gain of +4 dB changed nothing, so the lever is the timing, not the transition's level. The strings, by contrast, have 7-26 such holes, mostly on "Leg BC MAX" at +0.2-0.35 s (Violoncellos 26 of 103). They are less exposed, and I do not propose a change there this cycle.

Fix. One range test on Flute 1, Flute 2, Oboe 1, Clarinet 1 and Bassoon 1 over qn 320-392 and 836-1016:
- (a) `build/score_config.py`: a wind velocity floor like the strings' and brass': `LEG_VEL_STRONG["wind"] = [(52, 96), (65, 100), (80, 104), (100, 110), (127, 116)]`. Refit the wind entries of `LEG_VEL_EXTRA_S` with `tools/pcx.py`: a faster transition needs less of the 0.04-0.10 s extra lead.
- (b) Only if (a) leaves holes of 6 dB or more: a new mix.json key `attack_set_ms` in `tools/build_reaper.py`, modelled on `cap_release()` with `"set": true`. It sets the AHDSR attack of the legato-target sustain groups to 200 ms: "1Fls" on Flutes 1-2, "OBs" on Oboes, "EHs" on the cor anglais, and the matching groups on Clarinet / Bassoon (read their names from the patches). This is an Opus state change, so rebuild those tracks fully.
- Horn 1: per the scherzo c19 note, play 90, 286 and 868 on "Sus MAX" without an overlap, using `ART_SPANS` rows of 0.1 qn around each onset.
- Flute 2: cap its legato overlap at the wind floor (0.035 s) where it is 0.17-0.20 s.
- Pass: the number of 6 dB holes halves on each test track. The join timing (pcx median) stays within ±25 ms of c21, and the 2-5 kHz energy in the first 80 ms of the target rises no more than 3 dB (no new click).

### 4. The celli's re-bows already separate; the c21 measure looked in the wrong window (measured)

c21 reported 4 of 17 celli stroke-fall re-bows dipping 3 dB or more (`dips21.py`).

That script takes the floor from 30 ms before to 20 ms after the moved note-on. These re-bows lead by 100 ms, and the new "Sus MAX" note speaks slowly, so the true minimum falls 70-120 ms after the moved note-on, around the beat. On the same notes, the body-to-minimum depth is 6.5-16 dB.

Anchored on the score beat (the lower of the old body at -0.4..-0.15 s and the new peak at 0..+0.25 s, minus the minimum at -0.12..+0.08 s):

| track | n | c20 median (3 dB or more) | c21 median (3 dB or more, 6 dB or more) |
|---|---|---|---|
| Violoncellos | 17 | 6.6 dB (15) | 7.0 dB (17, 11) |
| Violas | 21 | 7.5 dB (21) | 7.8 dB (21, 15) |
| Double basses | 12 | 7.3 dB (11) | 8.4 dB (12, 10) |

The c21 stroke fall did its job: 70 went 3.7 -> 11.4 dB, 98 2.2 -> 9.8, 932 0.8 -> 4.9.

Fix:
- Do not deepen `STR_REP_NEW_BOW["stroke_fall"]`.
- Change the measuring window in the actor's check (the c21 `dips21.py` method) to the score beat as above, so the next cycle does not chase a fault that is not there.
- The remaining weak ones are celli 156 (4.2), 608 (4.3) and 896 (4.6). They are on the scherzo pattern of a slow new "Sus MAX" bow, and I would leave them.

### 5. Trumpet 3's printed accents in the Più allegro heads carry no weight (measured; fix inferred)

Where: Trumpet 3, accented half notes at 1024, 1032, 1040 and 1044 (bars 257-262, accent plus cresc., ff from 1032). The plain half notes alternate with them.

Evidence. The peak (100-2000 Hz, first 0.22 s) minus the body (0.3-0.6 s):
- Trumpet 3 accented notes: +0.4 dB. Their peak is 1.2 dB **under** the plain notes (-36.0 against -34.8 dB).
- Trombone 1's accents in the same span: +2.5 dB against -0.3 on its plain notes. That is the 2-4 dB of weight Dan asked for.
- The velocities differ (103-127 accented, 83-100 plain), but on "Sus Non Vib MAX" velocity hardly reaches the level (CC1 is the dynamic, p.101; inferred from these numbers).
- The rising cresc. CC1 (85 -> 108 over 1022-1032) lifts the plain notes as much as the accents.
- 2-5 kHz in the first 80 ms is -1.7 dB against the body (no bite), so the accents are not harsh; they are missing.

Fix:
- In the c17 accent table (`_C17_ACC` in `build/score_config.py`), give Trumpet 3 the same CC11 accent shape and `amt_rel` as the trombones over 1016-1048.
- Or, if that table is off on this track, an `accent_fits.json` swell of +2.5 dB on those four onsets.
- Do not raise accents elsewhere (Dan, c17: accents a little overdone). Other accents measured in place: the 1088-1108 brass accents read +0.2 to +1.5 dB peak-over-body, which I leave.
- Pass: Trumpet 3's accented peaks 2-3 dB over its neighbouring plain notes, with 2-5 kHz in the first 80 ms still under the body.

### 6. The basses' accelerando eighths (bars 205-210) are short of level because the extra CC11 sits on the top-layer plateau (measured; fix inferred)

Where: Double basses, "Stac On Bow RRx9", qn 816-840.

Evidence:

| span | c19 (dur 0.35 qn) | c20 (0.30 qn) | c21 (0.30 qn, all_db +4, CC11 +24 units) |
|---|---|---|---|
| stroke p90, 816-840 | -31.7 dB | -41.0 | -34.7 |
| stroke p90, 792-816 | -29.7 | -33.8 | -30.5 |
| dip between strokes, 816-840 | 7.7 dB | 10.3 | 10.3 |

- The CC11 median rose 88 -> 112 there.
- The +4 dB region gain alone lifted 792-816 by 3.3 dB, so the 24 CC11 units gave only about 2.7 dB (0.11 dB per unit). There is no room left above 112.
- The separation (10.3 dB) has 2.6 dB to spare over c19's 7.7.

Fix:
- `build/score_config.py`: note length 0.33 qn (instead of 0.30) for the basses' "Stac On Bow" notes at 816-840 only. Use the same mechanism that set 0.30 in c20, with a span limit.
- Keep the CC11 lift; it is harmless.
- Expected (inferred): +1.5-2.5 dB of stroke level, from c19 -> c20 where 0.05 qn cost about 9 dB here.
- Pass: p90 within 1.5 dB of c19 (-31.7) and dips 7 dB or more.

## The coordinator's c21 list, through this lens

- **Climax order.** The score prints fff on every staff at 888 (crash fff, bass drum ff), 1048 (crash fff) and 1108 (every staff fff and accented, strings div. a 3, crash and bass drum). Nothing in the print ranks 263 under 223 or the final.
  - The orchestration does: the final is the fullest (accents everywhere, div. a 3, both percussion), and 223 is the arrival after the allargando.
  - A 0.3 dB spread is not a contradiction of the print (inferred). If anything is changed, only keep the final chord at or above 223 and 263. Do not push 263 down: it is printed fff.
- **Master WAV clipping (+0.6 dBFS true peak, sample peak 1.073).** Add -2.0 dB of master gain before the render. Either add a `master_gain_db` key to `build/mix.json`, applied by `apply_mix()` as the master track's D_VOL, or put an output gain on the `master_eq` ReaEQ.
  - Expected: sample peak -1.4 dBFS (inferred).
  - The delivery's loudness loop normalises, so the mp3 is unchanged.
- **Trumpet note ends.** Fixed as targeted (-14.2 / -15.9 / -15.4 dB at +0.2 s). The new fault is finding 1. Fast staccato (the "Stac DblTng" row) is not smeared: 361.5 still dips 10.8 dB.
- **Celli re-bows.** See finding 4: met on a beat-anchored measure (17 of 17).
- **Basses' eighths.** See finding 6.
- **Scherzo c19 notes.**
  - Horn 1 legato hole: applies (finding 3, Horn 1 90 / 286 / 868).
  - String Leg Slur MAX swell at about 70 ms: does not apply (+1.0 / +1.6 dB). Leave the string TLeg region volumes alone.
  - "Test wind overlap rules against the row each note plays": Flute 2's 0.17-0.20 s overlaps on Leg Slur MAX sit on 9.5-13.8 dB holes (finding 3).
- **Movement II c57 notes.** Exposed undoubled bow pieces dipping 6-10 dB: the measured holes are on the celli's "Leg BC MAX" (finding 3's table), which is doubled by the basses most of the time. Not proposed this cycle.
- **Tremolo.** Every printed tremolo onset on all five string tracks (888-896, 1016-1044, 1088-1112) plays the "Tremolo" row (measured). No string note is longer than 4 s (the tremolo splits and re-bows hold), so there are no long single samples to pulse.

Do not touch:
- the c21 `STR_REP_NEW_BOW["stroke_fall"]` values;
- the trumpets' note-end treatment at p / mf;
- the c19 chorale pitch-change overlaps and the 0.025 s same-pitch gap;
- the harp's Harmonics / Gliss Technique rows on keys 112 / 113;
- the Tremolo rows from bar 223;
- the basses' 0.30 qn strokes outside 816-840 and their dips of 14-16 dB;
- the cor anglais "Sus MAX" spans (their level is a balance question, not an articulation one).

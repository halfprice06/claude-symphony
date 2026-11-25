# Cycle 4, critic A: articulation and phrasing (render c03, score v600)

Method. Every number comes from the c03 stems and master (`cycles/c03/render`, after the c03 horn stem fix), placed on the tempo map in `build/parts.json` with `tools/pcx.py` (TM). Rows come from each track's keyswitch lane. Marks, slurs and grace offsets come from `build/mockup-events.tsv`. Measures:
- **pc (S2).** `pcx.attack_pcx`: the perceived attack on the note's harmonic band, re the score onset. The previous pitch is excluded.
- **Band peak / length.** Time of the harmonic-band peak after the score onset, and the time from the peak until the band is 10 dB down.
- **Repeat and join dips.** 10 ms broadband RMS on the stem: min(peak before, peak after) minus the minimum around the onset.
- **2-5 kHz front.** Band energy over the first 80 ms minus the body over +0.15 to +0.6 s, per second.
- **Loop fold (item 7).** 100-300 Hz band and spectral centroid, autocorrelation at 3.95 s after a 2 s detrend.

"Measured" means a number from the render, parts.json, ks_maps.json or a patch. "Inferred" means reasoned, not tested. As instructed, the stopped-horn level is not reported.

## Manual notes (cycle 4, slot A: 2021 manual PDF pages 108-113, read in full; Movement I's c39 A table checked against the Finale)

The pages are text only, so the row facts below come from `~/.rpr-bridge/libs/ew_ho/ks_maps.json`. The "three tables" p.108 refers to are not in this edition.

| Manual (PDF page) | Where it applies in the Finale | Does the render follow it? |
|---|---|---|
| p.108: Flute 2 is a different player in another seat. There is one oboe, clarinet and bassoon player. 3 Flutes / 3 Clarinets / 3 Bassoons are new ensembles. | Flute 2 is on FL2. Oboe 2, Clarinet 2 and Bassoon 2 share their first players' KS Masters. | **Flutes: yes.** **Others: no** (measured, `find_unisons`). Same-patch unisons drop one copy, and the kept copy gets +3 dB (`UNI_BOOST`). Dropped: Oboe 2 50 notes, Clarinet 2 52, Bassoon 2 76. The same happens to the brass: Horn 2 189 notes in unison with Horn 1, Horn 4 81 with Horn 3, Trombone 2 47, Trumpet 2 35. Finding 2. |
| p.109: sustain dynamics "with the Mod Wheel". | Every wind sustain. | This is Play-era text. The render follows the patches (DIGEST 7.2): CC11 sets the dynamic and CC1 crossfades Non Vib / Vib on FL, OB, EH, BS and CB; CC1 is the dynamic on CL and BC (`CC1_DYN_TRACKS`). Yes. |
| p.109: Sus Expressive (slower attack, growing vibrato). | Bassoon 1 "solo, espress." bars 115-121 (qn 456-484). Cor anglais con sord. duet bars 171-183. | Not used. Bassoon 1 ramps CC1 65 -> 100 over the first beat of each phrase (456, 472), a vibrato fade-in that does the same job. The rows exist: "Sus Exp Vib" BS key 30, "Leg Slur Exp" BS 77 / EH 35. No finding: the solo's problem is timing (finding 1), not colour. |
| p.109-110: Legato Repetitions (LegRep RRx4) for repeats inside a sustained phrase. | Wind repeats: 341 re-tongued notes in parts.json. | Not used (`REP_ROW` is empty in the Finale). The emulation passes S1 (measured, standing checks). No change needed. |
| p.110: shorts (Staccato, StacSs, Double Tongue, Marcato) have no release trails. Hold the note so the room rings. | 170 printed wind staccatos, in the F1 head motive (bars 20, 24, 36, 84, 142-164, 208, 270-276), the hammered eighths of bars 202 and 250, and bar 275. | **Mostly not.** Only Bassoon 1 bars 11-33 plays "Stac DblTng RRx9" (36 notes). Every other wind staccato is a Sus or Leg slice that swells to its note-off (finding 3). The rows are present: Stac DblTng RRx9 is key 28 on FL, FL2, OB, EH, CL and BS; BC and CB have RRx5 (ks_maps). |
| p.110: Shorts MOD SPEED; p.111: runs, trills, flutter, repetitions, FX. | None printed. The only fast wind notes are the three-note grace runs into bar 35 (qn 135.2-136, Fl1 and Cl1). | n/a. The grace runs play on the Leg row at 0.09 s per note (`GRACE_S`). Complete on the winds, but **two of the doubled violin runs lose notes** (finding 5). |
| p.112: legato only with no gap and within an octave; monophonic unless CC22 < 64. | Every wind legato row. | Yes (measured in parts.json): no chord on a wind legato row, no join over 12 semitones (`WIND_WIDE_LEG`), no CC22, legato overlap 0.04 qn. |
| p.112: Legato Slur Repetitions. | Slurred same-pitch wind repeats. | Not used. The repeats separate anyway (S1 medians 7.4-11.3 dB). No change needed. |
| p.112-113: Slur Runs (seconds only, 40+ voices); KS Masters. | No wind runs. | n/a; yes. |
| Not on these pages, but it decides how the slurs sound: velocity sets the legato transition speed (p.106 brass, p.144 strings; the wind KS Masters carry the same LegatoSpeed script, and `build_reaper.py` turns `legato_speed_active` on). | `score_to_parts.py`: wind legato targets get v100 under 0.45 s, v80 under 0.9 s, v60 above (Cor anglais 100/90/80). | The slower velocities are kept for musical reasons, but their extra lead (`LEG_VEL_EXTRA_S`) covers only v70 and under. The v80 and v90 targets arrive late (finding 1). |

## Standing checks

- **Item 7, loops (measured): passes.**
  - The only non-string note held 6 s or longer is Horn 4 qn 168 (6.5 s). The strings are re-bowed.
  - Master fold at 3.95 s (band / centroid): chorale 888-936 is 0.09 / -0.04, final bars 1088-1116 are -0.03 / 0.03. No pulse.
- **Item 4, accents (measured): passes.** Wind and brass 2-5 kHz front minus body:

| track | median | p90 | highest |
|---|---|---|---|
| Flute 1 | -4.6 | +0.7 | +5.4 (qn 328) |
| Clarinet 1 | -4.7 | +1.1 | +4.1 (808) |
| Contrabassoon | -3.8 | | |
| Bassoon 2 | -9.1 | | |
| Horn 1 | -12.1 | | |
| Trombone 1 | -2.7 | | |
| Bass trombone | | | +4.7 (448) |

No accent is a burst.
- **S1, wind and brass repeats (broadband dip; measured): passes.**
  - Medians: Clarinet 1 10.6 dB, Bassoon 1 8.3, Contrabassoon 10.2, Oboe 1 11.3, Horn 2 6.1, Horn 4 7.1, Bass trombone 6.2, trumpets 8.1-9.1, Tuba 9.6.
  - Under 3 dB: Clarinet 2 932 (2.8), Horn 2 564 (2.9) and 896 (2.6), Bass trombone 836 (2.7).
  - The c03 horn cap holds. c03's open REP_ROW item (Horn 2 808-814, bass trombone 828-840) no longer measures under 3 dB with this method, so it stays low priority.
- **S2, staccato eighths of bars 202 and 250 (measured): on time.**
  - pc: Oboe 1 / Flute 1 / Clarinet 1 at 804-805.5: -14..+44 ms.
  - Flute 2 / Bassoon 1 at 996-997.5: +1..+29 ms.
  - The doubling Violins I / II staccato rows: -18..+56 ms.
- **Transition motive x, bars 43-48 (measured).**
  - Clarinet 1 (177-182) pc +12..+33 ms.
  - Flute 1 169.5-171.5 lands -37..-45 ms early. `LEG_SOFT_EXTRA_S["Flute 1"]` (50, 0.06) adds 0.05 s under CC11 50, and the lead drops back to 0.03 s once the crescendo starts (172.5-174: +8..+40 ms).
  - Oboe 1 is on time except its v80 targets (finding 1).

## 1. Wind legato targets at velocity 80 and 90 arrive 100-190 ms late, worst in the bassoon solo and the cor anglais duet (S2; measured)

**Where.** 61 wind legato targets at v60, v80 or v90 have pc over +80 ms. The exposed ones:

- **Bassoon 1 "solo, espress.", bars 117-121, pp strings only:**

| qn | 466 | 468 | 470 | 482 |
|---|---|---|---|---|
| pc | +145 ms | +187 ms | +184 ms | +144 ms |

  - 468 / 470 are the E♭3 and D3 half notes before the breath.
  - Also Bassoon 1 bars 127-129 (503, 508, 510, 514: +102..+267 ms), bars 187-193 (748, 750, 770: +153..+176 ms) and bars 213-214 (848-854: +149..+256 ms).
- **Cor anglais "espr." duet with the muted Trumpet 1, bars 172-185:**

| qn | 688 | 692 | 704 | 720 | 738 |
|---|---|---|---|---|---|
| pc | +118 ms | +185 ms | +174 ms | +103 ms | +172 ms |

  - The duet's v100 notes sit at -15..+50 ms.
- **Oboe 1:**

| qn | 97.5 | 188 | 308 | 1014 |
|---|---|---|---|---|
| pc | +184 ms | +159 ms | +200 ms | +177 ms |

- **Oboe 2 and Flute 2 in the Più allegro (992-1065):** Oboe 2 +128..+255 ms, Flute 2 +91..+211 ms.

**Evidence (measured, `velscan`).** Median pc per track and velocity:

| track | v100 | v80 | v60 | v90 |
|---|---|---|---|---|
| Bassoon 1 | +20 (n 138) | +105 (n 24) | +141 (n 5) | |
| Oboe 1 | 0 | +72 | +55 | |
| Oboe 2 | +32 | +147 | | |
| Flute 2 | +30 | +91 | +86 | |
| Cor anglais | +10 | +62 | | +92 |
| Flute 1 | +11 | +38 | +49 | |
| Clarinet 1 | +23 | +30 | -8 | |
| Clarinet 2 | +21 | +42 | | |

- In `tools/score_to_parts.py` (leg_target branch, about line 3003), a wind target gets v80 for notes of 0.45-0.9 s and v60 above; the cor anglais gets 90 / 80.
- `LEG_VEL_EXTRA_S` (Finale `{"Bass clarinet": (70, 0.09), "Oboe": (70, 0.05), "wind": (70, 0.04)}`) adds lead only at v70 and under. Every v80 / v90 target therefore keeps the v100 lead (Bassoon 1 60 ms, Cor anglais 50 ms) and plays a slower transition (LegatoSpeed: lower velocity = later sample start).
- At 168 qpm a quarter is 0.36 s, so +150..+190 ms is half a beat. In a solo over pp pizzicato that is heard as dragging. The brief's S2 limit is 40 ms.
- The lead cap does not bind on these notes: 0.45 × the previous quarter = 0.16 s.

**Fix.**
1. **`tools/score_to_parts.py`, `LEG_VEL_EXTRA_S` (generic, back-compatible):** accept a list of `(velocity at or below, extra s)` pairs per key, checked from the lowest velocity up. A plain tuple keeps today's meaning.
2. **`build/score_config.py`, values from the measured excess over each track's v100 median.** The current v60 extras are folded in:

```python
LEG_VEL_EXTRA_S = {"Bass clarinet": (70, 0.09),
                   "Bassoon": [(60, 0.16), (80, 0.09)],
                   "Oboe 1": [(60, 0.10), (80, 0.07)], "Oboe 2": [(60, 0.12), (80, 0.11)],
                   "Cor anglais": [(80, 0.05), (90, 0.08)],
                   "Flute 2": [(60, 0.10), (80, 0.06)], "Flute 1": [(60, 0.07), (80, 0.03)],
                   "Clarinet 2": [(80, 0.02)], "Clarinet 1": [(60, 0.0)], "wind": (70, 0.04)}
```

   - The table keeps the slower, singing transitions into long notes (p.106 / p.144) and moves their start instead.
   - Clarinet 1 v60 is already early (-8 ms), so its extra goes to 0.
3. **Flute 1 soft extra:** `LEG_SOFT_EXTRA_S["Flute 1"]` (50, 0.06) -> (50, 0.03). Its five joins at 169.5-171.5 land -37..-45 ms.
4. **Check after the render.** Run `pcx` on every wind target at v<100. Targets: track medians within ±30 ms; nothing over +80 ms in the bassoon solo (456-500) or the cor anglais duet (680-740). Per-onset outliers (Bassoon 1 466 at v100 +145, Cor anglais 702 / 735 at v100 +136..+140) go into `build/leg_leads.json` after this pass, not before.

## 2. The a2 passages are one solo sample + 3 dB: Horns 1-2 (199 unison onsets) and Horns 3-4 (94), plus the woodwind a2 (measured; better patches read; gain inferred from Movement I)

**Where.** Unison windows of 4 qn or longer, from the Hn1/Hn2 and Hn3/Hn4 note events:

| pair | windows (qn) | bars |
|---|---|---|
| Horns 1-2 | 40-102 | F1 theme, bars 11-26 |
| | 568-576, 588-662 | recapitulation, bars 148-166 |
| | 796-823 | coda |
| | 864-880 | |
| | 984-1016, 1024-1104 | Più allegro heads and chorale, bars 247-276 |
| Horns 3-4 | 104-135, 144-152, 408-416, 576-599, 816-823, 840-848, 892-896, 952-956, 1016-1032, 1073-1085 | |

`find_unisons` keeps one copy and adds `UNI_BOOST` +3 dB. parts.json: Horn 2 lost 189 notes to Horn 1, Horn 4 81 to Horn 3.

**Evidence (measured).**
- Horn 1 stem re master: -11.4 dB in bars 10-27, -10.9 in 148-166, **-8.3 in 244-254** and -8.2 in 273-276.
- In 244-254 Horn 1 is louder than every string section (Violins I -13.9, celli -11.7), Flute 1 (-11.3) and Trumpet 1 (-14.3). One solo French horn sample leads the "full brass" heads of the Più allegro.
- Its L/R correlation in the a2 spans is 0.83-0.87, against 0.95 in the solo span 51-66: no second player's spread.

**Movement I.** The same problem was fixed there by a "Horns a2" track on the 2FH KS Master. It is `symphony/mvt1/reaper-v621/build/score_config.py` lines 621-633 (TRACKS append, `TRACK_WINDOWS`, copied LEVEL_SHAPES / NOTE_TRIM_RAMP_S / ABUT_LEAD / BREATH tables). Results: levels refitted within -1.1..+0.2 dB, brass 2-5 kHz front max 8.3 -> 3.8 dB (M1 HISTORY c13), and a per-window gain of Horn 1 + 4.6 dB matched only at mf (KIT §20). The Finale port dropped that track: 31 tracks, no 2FH.

**Library (read, ks_maps).** 2FH KS Master rows: Sus MAX, Leg Slur MAX, StacSs DblTng RRx9, **Marc Shrt DblTng RRx4** (not "Marc Shrt RRx4": the Horn 1 staccato `ART_SPANS` need this row name in the a2 track), LegRep RRx4, Stop Sus. For the winds: 3CL and 3BS KS Masters (p.108 "new" ensembles; M1 c39 A #5); 2TP for Trumpets 1-2.

**Fix.**
1. Port Movement I's "Horns a2" block into `build/score_config.py`: `TRACKS.append(("Horns a2", ["Hn1"], B + "2 French Horns/06 Keyswitch/2FH KS Master.oib", "brass", -0.42))`, with `_A2W` = the Horns 1-2 windows above.
   - Horns 1 and 2 rest inside the windows (`TRACK_WINDOWS`).
   - Copy Horn 1's per-onset rules inside the windows, as M1 did.
   - Rename the Horn 1 staccato `ART_SPANS` entries (40-104, 552-664, 816-828, 1056-1076) for the a2 track to "Marc Shrt DblTng RRx4".
2. **Memory.** The main project settles at 44 GB with 31 instances. Render the a2 track in the second pass: `ALIAS_TRACKS` / `PASS2_TRACKS`, `build_reaper.py --pass2`, `render_cycle.py N --pass2` are in tools/. Do not add a 32nd main instance.
3. **Level.** Start at Horn 1's gain + 4.6 dB and fit per window on the first render (`roles.json`), against Horn 1's c03 level in the same windows.
4. **Measure.** Level per window within ±1 dB of c03, the 2-5 kHz front of accented notes (under +3 dB), L/R correlation, and pc on the F1 head joins.
5. **Next, same route.** Horns 3-4 a2 on a second 2FH alias in the second pass (windows above). Then Clarinets / Bassoons a2 on 3CL / 3BS where the dropped notes are exposed: Clarinet 2 bars 220 and 251-254 (-8.4 / -10.0 dB re master), Oboe 2 bars 214-226.

## 3. Wind staccatos on Sus and Leg slices swell into the note-off instead of being struck; only Bassoon 1 bars 11-33 uses the staccato row (measured; manual p.110)

**Where.** 170 printed wind staccatos, outside Bassoon 1's `ART_SPANS` window 40-132:
- the F1 head motive (two slur-end staccato quarters and a detached one): bars 20, 24, 36, 84, 142, 146, 152, 156, 160, 164, 208, 270, 276;
- the hammered staccato eighths: bar 202 (qn 804-805.5, Fl1 / Ob1 / Cl1, doubling the violins' staccato rows) and bar 250 (996-997.5, Fl1 / Fl2 / Bn1);
- Clarinet 1 1097, bar 275.

**Evidence (measured, harmonic band per note).**

| track, row | n | band peak after score onset (median) | peak to -10 dB |
|---|---|---|---|
| Flute 1, Sus MAX | 22 | +145 ms | 89 ms |
| Flute 1, Leg Slur MAX | 23 | +114 ms | |
| Oboe 1, Sus MAX | | +170 ms | |
| Oboe 1, Leg Slur MAX | | +152 ms | |
| Clarinet 1, Sus Non Vib | | +139 ms | |
| Clarinet 1, Leg Slur | | +166 ms | |
| Flute 2, Leg Slur MAX | | +182 ms | |
| **Bassoon 1, Stac DblTng RRx9 (bars 11-33)** | 36 | **+74 ms** | 140 ms, natural decay, pc -16..+19 ms |

- At 168 qpm the played slices last 0.21-0.23 s (quarters) and 85-89 ms (eighths). The sustain samples are still rising when the note-off arrives, so each staccato is a small swell cut by the 177 ms KS release, not an attack followed by a decay.
- The strings play the same figures on their staccato rows (`stacc_q` -> Stac RRx9 / Staccatissimo RRx9). Winds and strings articulate the doubled F1 motive differently (inferred from the shapes).
- In bar 202 the Flute 1 eighths peak 11.6 dB under the body of its next note (806). Oboe 1 is -2.2 dB, Clarinet 1 +2.1.
- Movement I kept the same rows for Bassoon 1, Cor anglais and Flute 1 (MANUAL-GAPS Results c39: peaks 0.06-0.16 s, natural decay, pc within 0.03 s of the strings).

**Fix.**
1. **`build/score_config.py` `ART_SPANS`**, whole-piece spans with `"mark": "staccato"` and Bassoon 1's velocity map (FL / OB layers are 1-74 / 75-114 / 115-127, M1 c39):

```python
_ww_stac_vel = [(58, 72), (72, 82), (88, 96), (114, 104)]
for _w in ("Flute 1", "Flute 2", "Oboe 1", "Clarinet 1"):
    ART_SPANS[_w] = ART_SPANS.get(_w, []) + [{"from": 0.0, "to": SCORE_END, "art": "Stac DblTng RRx9",
                                              "mark": "staccato", "vel_by_cc": _ww_stac_vel}]
ART_SPANS["Bassoon 1"] = [dict(ART_SPANS["Bassoon 1"][0], to=SCORE_END)]
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Flute 1": 0.03, "Flute 2": 0.03, "Oboe 1": 0.03, "Clarinet 1": 0.03})
```

   - Note-off at about 0.7 of the written value, so the room rings (p.110).
   - Bassoon 1 already has the row loaded, so extending its span costs nothing.
   - Each of the four other tracks loads one row. That is about 0.1-0.3 GB per row (MANUAL-GAPS memory plan) and needs a full rebuild of those tracks. Read `footprint` after the settle. Oboe 2, Clarinet 2, Bassoon 2 and the cor anglais follow if the first four pass.
2. **Then refit by stem fix.** Check `accent_fits` for accented staccatos, and the level of each staccato against the c03 note (the c01 lesson: short rows came in 3.6-8.6 dB under the Sus notes).
3. **Targets.** Band peak within +40..+90 ms; pc within ±40 ms of the doubled strings; level within ±2 dB of the c03 notes.

## 4. The ff three-note grace run into bar 35 is incomplete in the violins (measured in the data; audible effect inferred, small)

**Where.** qn 135.2-136 (the slurred grace run E♭5-F5-G5 into the accented A♭5 at bar 35). It is printed identically in Fl1 (an octave up), Cl1, Vln I and Vln II (mockup-events.tsv grace offsets -0.75 / -0.5 / -0.25), and all four staves carry it in `build/mockup.midi` (note-ons at 135.831, 135.885 and 135.943).

**What is wrong (parts.json).**
- Flute 1 and Clarinet 1 play all three grace notes (sq 135.244 / 135.496 / 135.748).
- **Violins I plays only F5 and G5** (75 missing).
- **Violins II plays only G5** (75 and 77 missing).
- At bar 109 (qn 436) both violin sections play all three, so the loss is specific to bar 35.
- The run starts on a different note and beat-fraction in each section, so the doubling is ragged at the head of the ff counterstatement (inferred).

**Fix.** In `tools/score_to_parts.py` `build_track`, the after-grace placement (about lines 1959-1987) takes each grace pitch from `cand = [n for n in ns if n["pitch"] == pitch and gq - 1 < n["qn"] < tgt["qn"] and n["end"] - n["qn"] < 0.2 ...]`.
- Print `ns` for Violins I / II between 135 and 136 before this block to find which earlier string step removed or merged the E♭5 / F5. Candidates are the top-note filter for flagged onsets just above it (line 1956) and the same-pitch repeat merge with the G5 quarter at 134.
- Exempt notes that sit on a grace row.
- Target: three grace notes on each of Vln I and Vln II at 135.244 / 135.496 / 135.748 sq, as on the winds.

## 5. Clarinet 1's "sub. p" at bar 138 is a 6 dB post-hall volume step under a ringing note (S3; measured)

**Where.** Clarinet 1 qn 547.85-547.93. Clarinets and bassoons play p < ... "sub. p" at 548 (bars 136-138) under the horns' stopped sf.

**What is wrong (measured, parts.json `vol_db`).**
- The crescendo's hairpin gain on Clarinet 1 rises to +8.45 dB (Bassoon 1 on the same hairpin: +2.5).
- It falls to +2.48 dB between 547.852 and 547.932, and to 0 at 548.0. The 544 note ends at 547.762 and its 177 ms release is still sounding.
- The stem's 20 ms envelope falls -41 -> -56 dB at the join, then sits at -47..-49. The hall tail of the louder note is cut, which is the S3 pattern (a fast fall in the REAPER envelope after the hall).
- The CC1 drop 64 -> 42 at 547.892 is right and stays.

**Fix.**
- Hold the hairpin gain past the old note's release: end the ramp at 548.0 + 0.2 s, falling over 0.15 s. The new note's CC1 42 already gives the sub. p.
- Or put the step on CC7 (pre-hall, MANUAL-GAPS Results c36), with the volume envelope flat across 547.8-548.3.
- Also check why the clarinet's hairpin gain is 3.4× the bassoon's on the same p < hairpin. `hpgain` for Clarinet 1 at 540-548 looks like the CC1-dynamic track getting the volume ramp on top of its CC1 crescendo (inferred).
- Target: no step of 3 dB or more within 0.2 s of a note-off in the volume envelope at 547-549, and the stem dip at the join under 8 dB.

## 6. Smaller items

- **Motive x, Flute 1 bars 43-44 (measured):** -37..-45 ms early on five joins (finding 1, fix 3).
- **4 soli (Violins I bars 120-128, measured in parts).** Played by the full 1st Violins section with the soli level cut (`SOLI_AS_META`). A DIV A half-section in the second pass (MANUAL-GAPS #7) is the closer patch for four players. Inferred; not ranked.
- **Muted Trumpet 1 slurs (c03 A #4, deferred).** Still butted fresh notes on "Mute Sus" (gap 0 ms on every join in parts.json). The cor anglais it doubles plays legato with 14 ms overlaps. `SLUR_ON_SUS_OVERLAP` remains the open fix.

**Do not touch:**
- Bassoon 1's Stac DblTng span and its velocity map (peak +74 ms, pc -16..+19 ms, natural decay).
- `WIND_REP_RETONGUE_BY` / `WIND_REP_PORTATO` and the c03 horn release cap: wind and brass repeat dips have medians 6.1-11.3 dB.
- GENTLE_ACCENT and the wind accent shaping: fronts have medians -3.8..-12.9 dB, highest +5.4.
- `WIND_WIDE_LEG`, the 0.04 qn legato overlap and the absence of CC22.
- The wind v100 legato leads: medians 0..+30 ms.
- `GRACE_S` on the winds.
- The re-bow layout (no loop fold in the master).
- The c03 dry hall, release caps and stopped-horn rows.

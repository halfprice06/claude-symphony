# Cycle 29, critic A: articulation and phrasing (on the c28 render)

Sources: the c28 stems and master (`cycles/c28/render/`), `cycles/c28/parts_rendered.json` (what was rendered; `build/parts.json` has changed since), the c27 and c26 stems and parts for comparison, `cycles/c28/CHANGES.md` and `logs/guard28_net.txt`, `build/mockup-events.tsv`, `build/score_config.py`, `build/mix.json`, the May 2021 HO manual (text) and `loop/MANUAL-GAPS.md`. All numbers come from my own scripts on the stems. Unless stated otherwise, levels are 200-6000 Hz band power in 40 ms frames, and "dip" is the drop at a join measured with 100 ms smoothing. "Measured" means a number from these files. "Inferred" means a cause, or a fix that a render still has to confirm. Every fix is on the instrument side (rows, onsets, crossfades, CC1 / CC11, velocity). None is a per-note move in the volume envelope or in CC7.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 29, so there was no assigned reading. I read the pages behind my findings and `loop/MANUAL-GAPS.md` (its c22, c23, c27 and c28 results).

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.104-105, brass Legato / Legato Slur | A slur joins two notes only when there is no gap between them and they are at most an octave apart. Legato patches are monophonic. | Every brass slur. Trumpets 1-2, 968-983 (bar 243, "molto espr."); Horn 1 / Horn 3 F1 head slurs | Partly. When an accented head plays the Sus row (`ACC_HEAD_JOIN`), the legato row has no sounding note to slur from. The second note then starts as that row's first note (finding 3). |
| p.106, Legato Slur | The patches always start 4 sustain samples and use separate samples for the slurs. Velocity sets the transition speed. | Trumpet legato targets at v118-124 | The fastest transitions still leave 10-13 dB holes on Trumpets 1-2 (finding 1). The hole is in the transition-to-sustain crossfade, not in the speed. MANUAL-GAPS c22 found the same on woodwinds: a velocity floor made no difference. |
| p.106, Legato Slur Accent | Like Legato Slur with an accent at the attack. The Mod Wheel sets the volume and velocity sets the accent strength. | Accented slur heads (MANUAL-GAPS #1) | Not used. I do not recommend first testing it in the last cycle that can still change the render. The Sus-row crossfade (MANUAL-GAPS c22 / c23, c27 variant b) has measured behaviour (findings 1-3). |
| p.123-126, timpani felt / hard | Separate felt-stick and hard-stick patches. | Score: hard sticks at 0, 711 and 1016; soft sticks at 680; medium sticks at 856 | The hard-stick patch ("Timpani Hrd KS": 160 Hrd Lng, 19 Hrd Rls) plays the whole piece. That is right for every passage marked hard. The soft (680-711) and medium (856-1016) passages also play on hard sticks (coordinator's list). |
| p.69 (harp), MANUAL-GAPS c22 | CC11 and note velocity set the harp's loudness. The KS Master has the copied Velocity->Volume path. | Harp at 952 | Can be used (coordinator's list). |

## Findings, ranked by what a listener on earbuds would notice

### 1. Bar 243 ("molto espr.", f): the trumpets' melody has a 10-13 dB hole at every slurred note change, and its first change is 0.18-0.25 s late (measured; cause inferred)

**Where.** Trumpets 1-2, qn 968-983. The slur is 968 (accented head, on "Sus Non Vib MAX"), then 970, 973 and 978 on "Leg Slur MAX". Trumpet 2 and Horn 1 play the line an octave under Trumpet 1. The 970 change is E5 to C6 (Trumpet 1).

**Evidence (measured on the c28 stems; c26 is the same within 1 dB):**

| join | Trumpet 1 dip / time under -6 dB | Trumpet 2 dip / time | new pitch at -6 dB vs beat (T1 / T2) |
|---|---|---|---|
| 970 | 10.6 dB / 330 ms | 10.9 / 140 | **+249 / +184 ms** |
| 973 | 11.2 / 290 | 12.4 / 270 | (semitone: not resolved) |
| 978 | 12.5 / 240 | 9.8 / 170 | (semitone: not resolved) |

- Trumpet 1 at 978 falls from 27 to 9 dB at +120 ms and stays at 10-16 for about 0.4 s.
- Horn 1, which plays the same line on "Leg Slur MAX", does not dip (973: 6.5 dB for 50 ms). Its 970 is +114 ms.
- In the master the joins dip 2.6-4.2 dB. The holes are in the melody's top octave.
- Other trumpet legato joins in the piece dip 5.5-6.4 dB for 0-30 ms (208, 256, 258). So 968-983 is an exception, not the row's normal sound.
- On the same row the velocity is already at the fastest transition (118), so velocity is not the lever. MANUAL-GAPS c22 found the same for woodwinds.
- The 970 lateness is the accented-head case of finding 3: the head is on the Sus row, so 970 is the legato row's first note.

**Fix (`build/score_config.py`, new c29 block).** Play the whole slur on the sustain row with crossfades. This is the c27 cor anglais variant b, which is kept: master join dips of 3 dB or more went from 3 of 22 to 2 of 22, and that span's joins now dip 1.1-3.9 dB (below).
- `ART_SPANS["Trumpet 1"]` and `["Trumpet 2"]`: `{"from": 969.4, "to": 983.5, "art": "Sus Non Vib MAX"}` (the head 968 is already on it).
- `ART_SPANS["Horn 1"]`: `{"from": 969.4, "to": 983.5, "art": "Sus MAX"}` (the same line; Horn 1's 970 is +114 ms).
- `INSTR_POST["onset_lead"]` for each of the three tracks: `{"at": [970.0, 973.0, 978.0], "lead_s": 0.10, "set": True}`. Each note keeps its end, so it overlaps the next note-on by 0.10 s (the c27 CA form).
- Velocity: 970 / 973 / 978 to 95, so a slurred note does not get a tongued attack (inferred). The join notes are now v100 (970) and v118 (973, 978). CC1 / CC11 lanes unchanged.
- Remove these onsets from `leg_leads` / `LEG_LEADS` if they are listed (973 is, from c27).

**Pass:**
- Join dips 5 dB or less at 970 / 973 / 978 on each trumpet stem and on Horn 1.
- New pitch at 970 within ±50 ms of the beat.
- 2-5 kHz first 80 ms minus body at most +2 dB on the three targets.
- Each target's body within ±2 dB of its c28 body (the head on the same row measured 26-31 against 24-33 for the legato notes, so no level change is expected).

### 2. Cor anglais solo phrases 696-706 and 731-740: the two legato joins left between the crossfaded spans dip 8 dB (measured)

**Where.** Cor anglais, bars 175-177 and 183-186 (the recapitulated F2 in C minor). The unison spans with the muted trumpet (683-694, 715-728) and 708 / 738 already play "Sus MAX" with crossfades. 696-706 and 731-740 are still on "Leg Slur MAX".

**Evidence (measured):**
- Joins on the Sus spans dip 1.1-3.9 dB (688, 692, 694, 708, 720, 728, 738).
- On the legato row:
  - **706: 8.3 dB for 220 ms.** The stem is +0.6 dB over the master there and the master dips 6.3 dB.
  - **740: 8.1 dB for 130 ms.** Master dip 5.2 dB.
- 740 directly follows 738, which c23 put on the Sus row. The legato row therefore has no note to slur from, so 740 is that row's first note. This is the same chain effect as finding 3.

**Fix (`build/score_config.py`, extend c27 ruling 2 variant b):**
- `ART_SPANS["Cor anglais"]` += `{"from": 698.9, "to": 707.0, "art": "Sus MAX"}` and `{"from": 730.9, "to": 741.0, "art": "Sus MAX"}`.
- Add 699, 700, 701, 702, 703, 704, 706, 732, 733, 734, 735, 736, 740 to the variant-b `onset_lead` list (`lead_s` 0.10, `set`).
- Keep 696 and 731 as phrase heads.

**Pass:** every join in 696-741 dips 4 dB or less, and the cor anglais level per note is within ±1.5 dB of c28.

### 3. Accented brass slurs: the second note is 0.14-0.28 s late (Horn 1 at 818 and 74, Horn 3 at 578 and 146). Trombone 1 plays the same figure on time (measured; cause inferred)

**Where.** The F1 head motive, "ben marc.", f: an accented half-note head on "Sus MAX", then a slurred dotted quarter, an eighth and a staccato quarter on "Leg Slur MAX".

**Evidence (measured; the time at which the new pitch reaches -6 dB of its later level, relative to the beat):**
- Horn 1: 818 **+229 ms**, 74 +144, 634 +89.
- Horn 3: 578 **+179**, 146 **+279**, 106 +9.
- Trombone 1 at 818, the same figure and the same rows: **-65 ms**.
- The c27 leads (0.18 qn at Horn 1 818) did not move it. c27 gave +130 ms, c28 +229.
- Cause (inferred): see finding 1. The second note is the legato row's first note, on its slow sustain start, so a lead cannot fix it.
- This is quieter than findings 1-2: the horn sits inside a tutti with the trombone on time. The coordinator asked for it, and "Leg Slur Accent MAX" is the open alternative.

**Fix (config only, the finding-1 form).** For each listed head, play the slur's later notes on "Sus MAX" with `onset_lead` 0.10 s `set`: the second note, the eighth, and the slur-ending staccato note.
- Horn 1: 818, 819.5, 820 and 74 plus its slur.
- Horn 3: 578, 579.5, 580 and 146 plus its slur.
- Velocity 90 (inferred, as finding 1).
- Leave Trombone 1 alone.
- Do not range-test "Leg Slur Accent MAX" in c29. It needs an Opus state change and a full rebuild of four brass tracks, its accent strength is set by velocity (p.106) with no measurement on this pipeline, and there is no cycle after c30 to correct it.

**Pass:** second note within +50 ms of the beat at 818 / 578 / 146 / 74, no join dip over 5 dB, and the head's 2-5 kHz front at most +2 dB over its body.

### 4. Bars 91-92, the trumpets' ff codetta (and 1104-1106): the pickup eighth runs into the accented quarter with no gap (measured)

**Where.** Trumpets 1-3, qn 361.5 -> 362 and 365.5 -> 366. The figure is an accented quarter, an eighth rest, an eighth, then an accented quarter, all three trumpets, ff. The same figure comes at 1105.5 -> 1106 (Trumpets 2-3). Trumpet 3 also has 1077.5 -> 1078 and 1085.5 -> 1086 on "Sus Non Vib MAX".

**Evidence (measured):**
- Same-pitch separation at the quarter: Trumpet 1 at 362 / 366 **0.7 dB**; Trumpet 2 at 1106 0.8; Trumpet 3 at 1078 / 1086 2.6-2.7.
- Of 568 same-pitch repeats in the piece, 25 are under 3 dB. These are the only brass ones apart from Trombone 1 at 988 / 992.5 (2.0-2.5).
- The curve at 362 (Trumpet 1): the 360 quarter at 26 decays to 14 at -205 ms. The eighth (a 48 ms note on "Stac DblTng RRx9") rises to 24 at -145 ms and runs straight into the 362 quarter, which is led by 0.14 qn (50 ms).
- Cause: the staccato sample's own tail fills the 100 ms between its note-off and the quarter's led note-on. The eighth and the quarter sound as one note.

**Fix (`build/score_config.py`):**
- `INSTR_POST["onset_lead"]` for Trumpets 1-3 at 362, 366, 1106 (and Trumpet 3 at 1078, 1082, 1086): `{"lead_s": 0.02, "set": True}`. The gap after the eighth grows from about 100 to 130 ms; research default for brass 60-100 ms.
- Lower the pickup eighths 95 -> 82 (Trumpet 3's Sus-row eighths 89-91 -> 80), so their tail is lower when the quarter enters (inferred: the velocity layers of Stac DblTng RRx9 are not measured on trumpet).
- The quarters stay accented. Their -6 dB point is now median -15 ms (Trumpet 1), so a 0.02 s lead keeps them within about +30 ms.

**Pass:** separation 4 dB or more at each listed quarter on its stem, and the quarter at -6 dB within +40 ms of the beat.

### 5. Più allegro, bar 248: Trumpet 1's tenuto at 989 overshot to 2 dB under its neighbours. Trumpet 2 is right (measured)

**Evidence** (per-note p90, 200-6000 Hz, c28):
- Trumpet 1: 988 18.2, **989 17.7**, 991 21.2. 989 minus mean(988, 991) = **-2.0 dB**. CHANGES gives -3.5 by another window.
- Trumpet 2: 988 19.1, 989 20.6, 991 17.6: **+2.2 dB**, inside the 0..+3 target.
- c28 moved Trumpet 1's 989 by -11.8 dB with CC1 -12 and the CC11 bump removed together.

**Fix (`build/score_config.py`, c28 block, "tpt" part):** Trumpet 1's `note_cc` cc1 on 988.9-989.1: `add` -12 -> **-7**. This is about +3 dB at about 0.65 dB per unit (c27 / c28 measures). Trumpet 2 stays at -6.

**Pass:** Trumpet 1 989 between 0 and +3 dB over the mean of 988 / 991, and its per-note range over 984-998 under 8 dB.

### 6. Smaller items, with the fix for each (measured unless marked)

- **Net-level in-note items (14 / 6 / 8).**
  - **Timpani roll CC7 shapes (10):** printed roll shapes or the settle under the texture that BRIEF item 5 requires. Exempt; leave them. The 920 roll (CC7 42 -> 24 over 920-922.9) settles evenly, with no loop pulsing (60-400 Hz within ±3 dB over 5.5 s).
  - **Steps that land a few ms before a legato note-on:** celli 951.48 (-4.7) and basses 951.78 (-4.2); violas 823.55 (+1.7, 0.01 qn); entries Violins I 487.5 / 488 / 892, violas 15 / 16 / 823.5 / 1088, Flute 1 136 / Clarinet 1 135.75. Fix in `tools/build_reaper.py` `TRIM_CC7_ONSET_*` (generic): when the old note overlaps the new one (legato), snap the CC7 step to 0.003 qn *after* the new note-on, not before. The old note's tail then keeps its level. The new note's first 1-2 ms at the old level is inaudible (inferred).
  - **Rate-limited carries inside short notes:** Violins I 896.08-899.32 (three notes at +1.5-1.6 dB each) and Horn 3 564.87-566.27 (+1.6). Fix in `ROLE_EDGE_IN_REST`: when a note is shorter than the carry at 2.5 dB/s needs, put each note's share of the carry as a step at its own note-on (±0.003 qn) instead of a ramp inside it. For Violins I: +1.5 dB at each of 896.0, 897.2 and 898.4, then the last +1.5 at 899.9. Same total, no move inside a note.
  - **Bassoon 1, 320.04-320.52 (+2.4):** the c26 variant C swell is a per-note level move. Remove it; there is no instrument-side equivalent worth the risk in the last cycle.
- **Harp at 952.** The envelope steps (vol_db -2.0 -> -3.0 over 951.9-952.15; CHANGES gives 2.9 dB net) under notes ringing since 950-951.5, at the printed mf.
  - Hold the envelope at its p value through 952-960 (no step).
  - Take the trim through velocity instead: the mf notes 952-957 are already v82-95 against v52-70 at p. Lower them by 8 steps (inferred slope; the harp's Velocity->Volume curve has not been measured).
  - Exempt the harp's `vol_set` row from vol_guard (`hairpin_ok`-style flag) or add no row at all.
- **Envelope at +24 dB.** gain + vol_db + the largest trim used reaches exactly 24.0 on Horn 3 (1017.2-1019.5, vol_db 9.2-10.0; ten points), 23.6 on Trombone 1 and 23.5 on Tuba. If ppp 14.0 is counted as the largest trim, Horn 3 reaches 25.0.
  - No clipping is proven at 24.0, but there is no margin.
  - Fix (generic, `build_reaper.py` `dyn_trim_to_cc7`): cap gain + max(vol_db) + largest at 23.0 by lowering the "largest" reference. Report any trim above it: here only pp / ppp notes, which never fall where vol_db is 9-10.
- **fff under ff.** Horn 1 fff 1.9 < ff 2.6, Trumpet 3 fff 12.6 < ff 14.1 (`build/mix.json` `dyn_trim_db`). Set fff = ff (2.6 / 14.1). Otherwise both drop 0.7 / 1.5 dB as a crescendo passes into fff at 888 and 1108. This is the scherzo c27 fault, and it is the same rule already applied to the woodwinds in c28.
- **Timpani sticks.** Hard sticks play everywhere. Correct for 0-680, 711-856 and 1016-1116. The printed soft sticks (680-711, four pp strokes "near the rim") and medium sticks (856-1016: the Largamente, the 888 arrival roll and the chorale rolls) are on the hard patch. A felt instance costs memory, and medium sticks lie between the two samples. Leave it in c29 (inferred: no audible gain worth a new instance at 45-46 GB).
- **Tenuto / loud downbeats peaking late (scherzo c28).** This does not apply in general here. Time to -3 dB of the note peak on loud notes (104-136, 600-640, 984-1048): Tuba median 46 ms (no note over 120), bass trombone 39, Trombone 1 19, celli 44, basses -5.
  - Outliers over 120 ms: basses 115 / 116 / 122 / 131 / 602-630 (154-334 ms), celli 116 / 122 / 600 / 632 / 1016 (179-439 ms). Most sit in the F1 bass line on "Sus MAX".
  - Not ranked: the celli's Detache re-attacks carry those downbeats (c25 / c26).

## The coordinator's list, through this lens

- **Net gate:** finding 6.
- **Trumpet 1 at 989:** finding 5 (CC1 -12 -> -7).
- **Harp 952, envelope +24, fff < ff:** finding 6.
- **Bars 271-273 against 255, and the bar-113 stop:** dynamics, not this lens. Through this lens, the held chords and tremolos of 271-279 have no note over 4.4 s on strings, and the timpani roll at 1088 (5.8 s) is level within ±3 dB.
- **Accented slur second notes:** findings 1 (Trumpets 1-2 at 970) and 3 (horns). Use the Sus-row crossfade, not "Leg Slur Accent MAX", in the last cycle.
- **Timpani hard sticks:** finding 6. The hard-stick patch is playing.
- **Tenuto downbeats:** finding 6. Does not apply in general.
- **Holistic: what a listener still notices in c28, through this lens.**
  - Most noticeable: the holes at slurred note changes in exposed melodies.
    - Of 194 measured wind and brass legato joins, 63 dip 6 dB or more and 25 dip 9 dB or more.
    - Most are in tutti: flutes at 330 / 618 / 842-848 sit 10-20 dB under the master, and the master moves 1-3 dB there.
    - The ones a listener hears are where the line leads: the trumpets at bar 243 (finding 1), the cor anglais solo (finding 2), Trumpet 1 at 844 (bar 212, theme B, ff: 9.9 dB for 140 ms while the stem is 3.2 dB under the master), and Bassoon 1's solo at 482 (10.1 dB; 1.8 dB under the master).
    - I have not ranked 844 and 482. The slur at 844 runs past 860, and a single Sus target there would make 847 the legato row's first note (the chain effect of finding 2). It needs the whole phrase on the Sus row, which is a larger change than one cycle should carry.
  - Next: the merged trumpet pickups of bars 91-92 (finding 4).
  - Repeated notes are otherwise clean: 543 of 568 same-pitch repeats separate by 3 dB or more.
  - Brass accents are on time: 321 accents, median -20 ms to -6 dB of the body, 4 % later than +60 ms. They have no bite: the 2-5 kHz front is under the body on every brass track (median -4 to -17 dB).
  - Accent weight: Trumpets 1-2 and Horn 3 accents in 960-1108 sit at -0.5 to -0.8 dB against unaccented neighbours. Do not raise them generally: Dan, c17, "a little overdone".

## Other movements' findings

- **Scherzo c24 note_slew / c25-c27 trims on moved time, hold-to-next-mark:** the c28 trim snap applies and works here. Its legato-overlap case is in finding 6.
- **Scherzo c26: slurred eighths on Leg Slur MAX ringing into the next staccato:** the brass form of it is finding 4 (staccato tail into the next note).
- **Scherzo c27: soft accented heads on Violins I Sus Marc LITE with a 7-13 dB hole:** checked. The Violins I accents in 960-1108 measure 2-5 kHz front minus body median -2.6 dB, accent minus neighbours +1.3 dB. No hole found.
- **Scherzo c28 timpani felt / hard:** checked (finding 6); hard sticks are correct here.
- **Scherzo c28 tenuto downbeats:** checked (finding 6). Does not apply in general.
- **Scherzo c28 round-robin resets replaying identical takes in a repeated ff tutti:** not measured this cycle.

Do not touch: the cor anglais variant-b crossfades over 683-694 and 715-728 (joins 1.1-3.9 dB); the c22 Horn 1 Sus-row targets (90 / 286 / 868); Trumpet 1 on "Mute Sus" with its overlaps; the basses' "Stac On Bow" hammered eighths with metric velocities; the chorale's re-tongue gaps; Trombone 1's 0.05 s gaps in the Più allegro; the trumpet solo's CC1 cap and targets (51-66); the pizzicato rows; the harp Harmonics / Gliss Technique rows and étouffez cuts; the tied crash / bass drum at 1108-1112; the timpani roll shapes; Trumpet 2's 989 (CC1 -6).

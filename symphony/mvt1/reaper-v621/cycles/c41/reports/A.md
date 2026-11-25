# Cycle 41, critic A: articulation and phrasing (render c40, score v621)

Method. All levels are stereo power in dB, measured on the final c40 stems (38 stems; the master is their float sum) and placed with `cycles/c40/rendered_build/parts.json`.

- Attack centres (pc), dips and harmonic envelopes come from `cycles/c37/actor_scripts/m37.py`:
  - pc = the mean of t50 and h10 on the note's harmonics, in seconds relative to the score onset;
  - dip = the lower note body minus the 30 ms minimum at the join.
- burst = the 30 ms maximum between a legato target's moved onset and its score onset + 0.15 s, minus the louder of the two note bodies.
- "rel" = the stem minus the master over the target's first 0.3-0.4 s.
- Pitch tracks use YIN (46 ms window, 5 ms hop).
- Simulations scale the c40 stem by a dB envelope and add the difference to the master. The volume envelope sits after Opus's hall, so the simulation is exact for level-only changes.
- Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c41-A/py/`:
  - `kscheck.py`, `states.py`: keyswitches and Opus states;
  - `joins.py`, `notchsim.py`, `notchsim2.py`, `notchpc.py`: joins;
  - `solo.py`: the cello solo;
  - `reps2.py`: S1 repeats;
  - `rebows.py`, `rbdetail.py`: re-bows;
  - `s2.py`: attack centres;
  - `acc.py`: accent fronts.

## Manual notes (2021 manual PDF pp. 160-162 and 188-190, read in full, pages rendered as images; also Opus p.86-88, MANUAL-GAPS.md, DIGEST.md 2.3)

The audit behind this table:
- I read every generated Opus state in `jobs/*.b64` (39 states).
- I checked every keyswitch and note in parts.json against the patch keyswitch maps (`ks_maps.json`, `build/ks_maps_extra.json`).

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.160: each articulation cell has a load switch (in RAM or out); KS Masters trigger rows by keyswitch | `build_reaper.py` loads only the rows parts.json uses | **Yes (read).** In every state, each row a track switches to is loaded and keyed. Example: Violins I loads 8 rows, all keyed at 24-49. No keyswitch goes to an unloaded row |
| p.161: keyswitch notes (C-2..G8) lie outside the playable range | Some KS Masters put their keys inside an instrument's range: Contrabassoon and Tuba 60-67, Basses 72-82, Celli 80-89, 1TB 73-115 | **Yes (measured).** No note on any of the 38 tracks sits on a keyswitch key of its patch |
| p.161: Keyswitch Range (pass thru, offset) and Program Change triggers | | Not set in any state (read) |
| p.162, p.190: Controller trigger (a CC value range selects a row; the example is CC1 0-42 / 43-87 / 88-127) | The pipeline's CC1 lanes: brass dynamics 18-120, string and woodwind vibrato about 40-110, timpani layers 56-122 | **Yes (read).** Every trigger entry in every state is a plain key trigger (only `useKey`/`key`; no velocity, controller or program fields), so no CC lane can switch a row |
| p.162, p.189-190, Opus p.87: velocity-range layering (sustain at 1-127 plus staccato at 110-127 gives an accent on hard notes) | Accents (663 marks); MANUAL-GAPS #1 is still open | **Not used, and it should stay that way in the same instance (inferred).** Velocity sets legato transition speed here (string and brass targets at v100-124), so a 110-127 accent layer would fire under every fast legato target. If a layer is wanted, it has to be its own pass-2 alias track. No accent problem needs two rows: at f and louder, accented notes put +0.9..+1.7 dB more 2-5 kHz into the master at their onset than plain notes, with weight by level (measured). String accents: see finding 4 |
| Opus p.86: Exclusive / Toggle / Temporary behaviour | Keyswitch notes at v1, 0.03 qn | **Yes (read).** Every trigger is Exclusive (behaviour 0), so keyswitch note-offs do nothing. There are 480 row changes while a note of the old row still sounds: SLUR_START_SUS heads, Leg Slur / BC / Port switches 33-160 ms before the old note ends, and timpani Lng after rolls. They do not cut the old note: those heads join at a median -0.1 dB since c15, and the c40 solo joins dip 3.8 dB or less (measured) |
| p.188: Group | All zones are in group 0, one instrument per instance (read) | n/a |
| p.188: Voice Limit (one note uses a voice per mic and per crossfaded layer; too low a limit drops voices) | Dense chords, harp arpeggios, timpani | **Yes.** Limits are 350 for strings and 250 for the rest (read). Most notes sounding at once, release included: strings 6-10, harp 22, timpani 11 (measured, parts.json). Estimate: strings 10 x 2 vibrato sets x 2 dynamic layers x up to 5 mics = 200; harp 22 x 2 mics x 2 = 88 (inferred). The c40 silent-note list has no chord notes |
| p.188-189: Octave and Key Range | | Every zone is 0-127 with octave 0 (read). The bass trombone's three lowest notes are transposed samples (MANUAL-GAPS #13, open) |
| Keyswitch timing (this row's task) | parts.json, all tracks | **Yes (measured).** The shortest lead on a row change is 9.5-10.7 ms (Violins II 189.62 / 196, Violas 294.215 / 300, celli 152.461 / 160 / 163.877 / 289.145). No keyswitch falls on or after its note. No chord goes to a legato row. All 77 legato-row overlaps longer than 0.12 s are SLUR_START_SUS heads overlapping their targets by 0.124-0.144 s, as designed |

MANUAL-GAPS items in this lens that are still open:
- #1 brass marcato row;
- #5 expressive wind rows;
- #9 horn portato rows.

None of them is the top problem on this render. Finding 4 is the level-only alternative to #1 for the strings.

## Standing checks

- **S2 (measured, 1,127 exposed notes).** Median pc by family and class is within ±0.025 s everywhere:
  - brass: accent +0.006, legato -0.004;
  - strings: accent -0.004, legato -0.022, staccato +0.001;
  - winds: accent +0.015, legato +0.012.

  The early tail is the string legato targets, p10 -0.172 s. Its worst notes are the transition spikes of finding 1.
- **Item 7, re-bows (measured).** The 92 automatic re-bows dip a median 2.1-3.6 dB per section. The level step after a re-bow has a median within ±0.6 dB. The larger residuals I checked (Violins I 48, celli 12.163, basses 38.003) follow the planned envelope (subito p, hairpins).
- **S1 (measured).** There are 706 score repeats.
  - Wind, brass, cello, viola and Violins II medians are 3.0-7.8 dB.
  - Violins I's 12 repeats have a median of 1.3 dB; most are long notes, and the exposed ones are 268 (-2.7), 575.5 (-0.4) and 627.5 (2.6).
  - The basses' f eighth pedal at 664-676 still merges each off-beat into its downbeat: the C2 harmonics rise straight through 664.5 / 665.5. This is the known c13-c22 compromise (Detache and Marc Shrt failed there), so I leave it.
- **Accents, item 8 (measured).** No bite. 2-5 kHz in the first 80 ms minus the body, median (p90): brass -13.9 (-7.1), winds -11.1 (-3.2), strings -8.6 (-2.7). Only celli 526 is over +3 dB and exposed (+4.5).

## 1. Twelve exposed legato joins still carry a 4.5-8.8 dB transition spike; four of them also pull the note's perceived attack 0.15-0.30 s ahead of the beat (measured; notches simulated)

**Where.** I scanned all 1,167 monophonic legato joins in c40 for unmarked Leg Slur targets with rel -10 dB or more and a burst of 4.5 dB or more. c40 notched the 11 largest from c40 A #4; these are the next tier. Leg BC targets are left alone (their bump is the bow-change accent, p.99). The spikes repeat to 0.1 dB between renders since c38, so notches land.

**Evidence and fix.** Add these `JOIN_NOTCH` rows in `build/score_config.py` as (from qn, to qn, dB). The tool adds 0.04 qn ramps. Each row was simulated on the c40 stem:

| join (bar) | span and depth | stem burst | stem dip | master burst | pc (s) |
|---|---|---|---|---|---|
| Bassoon 1 131 (33, espr. solo) | (130.75, 131.18, -6.2) | +8.2 -> +2.0 | -2.4 -> 3.7 | **+8.5 -> +3.9** | -0.105 -> -0.058 |
| Violoncellos 575 (144, held D3 under mp > pp) | (574.58, 575.02, -5.0) | +11.4 -> +6.9 (the rest is the printed decrescendo) | | **+8.2 -> about +5.5** | **-0.246 -> +0.016** |
| Violoncellos 191 (48, dolce tune) | (190.55, 190.72, -4.0) | +6.6 -> +4.0 | 4.5 unchanged | **+6.7 -> +4.9** | **-0.222 -> -0.077** |
| Clarinet 1 507 (127, Leg Slur Rep) | (506.80, 507.13, -2.5) | +4.5 -> +2.0 | | +4.9 -> +3.2 | |
| Violas 436 (110, tenuto) | (435.59, 435.97, -5.0) | +7.0 -> +2.0 | 2.9 unchanged | +4.6 -> +2.0 | unchanged |
| Oboe 1 315.5 (79) | (315.45, 315.58, -2.6) | +4.6 -> +2.0 | | +3.9 -> +3.1 | |
| Bassoon 1 138 (35) | (137.72, 138.34, -3.9) | +5.9 -> +2.0 | | +3.7 -> +2.9 | |
| Violas 182 (46) | (181.34, 181.77, -2.7) | +4.7 -> +2.0 | 3.4 unchanged | +3.7 -> +2.9 | **-0.297 -> -0.081** |
| Horns a2 164 (42) | (164.05, 164.34, -2.8) | +4.8 -> +2.0 | 0.5 unchanged | +3.6 -> +2.3 | |
| Violas 28 (8, Lento) | (27.80, 28.13, -5.7) | +7.7 -> +2.0 | -2.0 -> 3.8 | +3.6 -> +3.3 | -0.249 -> -0.176 |
| Violins II 259 (65) | (258.50, 258.87, -4.1) | +6.1 -> +2.0 | 2.0 unchanged | +3.3 -> +1.6 | |
| Violas 613 (154) | (612.68, 613.17, -6.8) | +8.8 -> +2.0 | -1.2 -> 4.4 | +1.9 -> +1.0 | **-0.151 -> +0.010** |

- The burst is heard on the master in the first nine rows.
- The early pc values belong to the S2 tail above: the spike inside the lead makes the new pitch speak before the beat.
- The rows are level only, so they can go in by stem fix.
- Re-run the join scan after the render. Targets: burst at most 2.5 dB, and no new dip over 4 dB.

## 2. Three printed breaths are played through, two of them on the breath into the fff at bar 160 (measured)

Every breath mark in v621 was measured: the gap after the note that ends at the breath, and the stem dip.

- Most breaths dip 4-13 dB.
- At the breath into 636, the other brass dip 5.6-11.0 dB: Trumpet 1 5.7, Trombone 1 5.6, Bass trombone 11.0.

These do not:

| breath (bar) | gap now | dip now | rel | why |
|---|---|---|---|---|
| Horns a2, note 634 -> breath 636 (160, into the fff) | 102 ms | **1.6 dB** | -8.9 | no `BREATH_GAP_AT` row; Horn 1's table holds no 634 |
| Trombone 2, note 628 -> breath 632 (159) | 150 ms | **1.8 dB** | -14.8 | no row; Trombone 1's row moved to 634 in c32 |
| Horn 4, note 532 -> breath 536 (134) | 90 ms | **-0.5 dB** | -17.0 | Horn 3 has (532: 0.4 qn, fall 8) and dips 3.8; Horn 4 has nothing |
| Oboe 2 and Flute 2, note 634 -> breath 636 | **22 ms** | 3.2 / 6.9 dB | -15.5 / -13.6 | the 0.12 qn row is eaten by the 636 entry lead |

**Fix** (`build/score_config.py`; keys are the onset of the note that ends at the breath):

```
BREATH_GAP_AT["Horns a2"] = {..., 634.0: 0.22}
BREATH_FALL_CC["Horns a2"] = {..., 634.0: 10}          # Trombone 1's values for this breath
BREATH_GAP_AT["Trombone 2"] = {628.0: 0.22}
BREATH_FALL_CC["Trombone 2"] = {628.0: 10}
BREATH_GAP_AT["Horn 4"] = {..., 532.0: 0.4}
BREATH_FALL_CC["Horn 4"] = {..., 532.0: 8}              # Horn 3's values at this breath
BREATH_GAP_AT["Oboe 2"][634.0] = 0.22
BREATH_GAP_AT["Flute 2"] = {634.0: 0.22}
```

Write the Horns a2 row after the `_in_a2` copy at about line 632, or the copy overwrites it.

Target: each of these dips 4 dB or more, like the other parts at the same mark. This is a MIDI change, so it needs the render (inferred effect from Trombone 1's 5.6 dB with the same values).

## 3. The coda cello solo (Cello solo, Celli KS Master DIV A, stem 38) is now a connected solo line. The 685 shift arrives on the beat; what is left is a 7 dB swing just after it (measured; shape simulated)

Judged as a solo line on the final c40 stem.

**Connection (measured).**
- 11 transitions: dips 0.2-3.8 dB, bursts 3.8 dB or less (687 the largest).
- pc -0.10..+0.05 s on every note.
- First note (680, upbow mp, after the 679 fermata): pc -0.09 s. Fine after a fermata.

**685 portamento (measured).**
- The f0 track reaches A-flat4 within 15 cents at **-0.03 s** relative to the beat.
- The harmonics of the C4 and the A-flat4 cross at -0.09 s; the glide runs from about -0.21 s.
- The "+0.28 s" in `cycles/c40/solo_b.txt` was measured before the contour stem fix, on the DIV A's own bloom (body +16.6 dB). In the delivered stem the shift is on time. It should stay a Leg Port at v100 with its 0.27 s lead.
- What remains (100 ms windows, relative to the 685 note body): -0.5 dB at +0.05 s, -3.8 at +0.25, **+3.1 at +0.35**. That is a 7 dB swing in 0.1 s; the master goes -2.5 -> +2.0 dB.
- Cause: the alias contour falls 11 dB between -0.15 and +0.26 s, but the Leg Port sample's crossfade into its sustain lands at +0.30 s. Heard as a small sag and then a push right after the shift (inferred).

**Fix.** Add this row to the Cello solo alias tables (`ALIAS_TRACKS["Cello solo"]["tables"]`, `LEVEL_SHAPES_S`):

```
(685.0, [(0.10, 0.0), (0.14, 3.0), (0.25, 3.0), (0.30, -2.0), (0.45, -2.0), (0.55, 0.0)])
```

Simulated on the c40 stem:
- stem range over 0..0.6 s: -4.4..+3.2 -> -3.6..+1.2 dB;
- master: -3.3..+2.1 -> -3.4..+0.4;
- pc -0.046 -> -0.093 s (the pitch still arrives at -0.03).

It is level only, so it can be applied by stem fix. It also has to be written to the pass-2 .rpp with the c40 contour rows, which c40 left for the next `--midi-only --pass2` build.

**Vibrato (measured and read; no change possible in this patch).**
- Note bodies vibrate 8-14 cents (half peak-to-peak) at 4.6-6.3 Hz: 680 7.8 at 4.6 Hz, 685 14.1, 692 10.6, 694 13.8.
- The same notes on the section patch ("Cello solo sec", c40 pass 2) give 5.7-6.9 cents.
- The lane already sits on the Molto Vib set. Read in `Celli KS Master DIV A.oib`: Molto Vib comes in from CC1 66 and is 0.85 at 95, full at 98; Sus Vib is 0.83 at 95 and 0.58 at 105. The lane runs 70 -> 105 over the first 1.4 qn, then 95-105.
- A soloist's espressivo vibrato is wider (inferred). Only Hollywood Solo Cello would give that (MANUAL-GAPS #3, not installed).

Keep everything else as fitted.

## 4. String accents carry their weight after the attack: at f and louder their front sits 2.8 dB further under the body than on plain notes (measured; fix inferred, level only)

**Evidence.** The quantity is 2-5 kHz over the first 80 ms minus the body (+0.15..+0.45 s), on notes of 0.35 s or more, at matched printed dynamics:

| family | dynamic | accented notes | plain notes |
|---|---|---|---|
| strings | f and louder | -8.6 (n 140) | -5.8 (n 254) |
| strings | mf | -7.8 | -6.2 |
| brass | f and louder | -14.4 | -13.6 |
| winds | f and louder | -11.1 | -10.5 |

- Brass and wind accents match their plain notes within 0.6-0.9 dB, so those accents are weight with an ordinary front, which is what Dan asked for.
- String accents still use the default swell `GENTLE_ACCENT["string"]["swell_s"] = (0.07, 0.25, 0.6)`: full from +0.07 to +0.25 s, gone by +0.6.
- Brass uses (0.03, 0.15, 0.40), set in c25 at `build/score_config.py` line 1387.
- So the string accent's extra level arrives in the note body. Heard as a push after the attack rather than an accent (inferred).

**Fix (`build/score_config.py`).**
- `GENTLE_ACCENT = dict(GENTLE_ACCENT, string=dict(GENTLE_ACCENT["string"], swell_s=(0.03, 0.15, 0.40)))`.
- Refit `build/accent_fits.json` with `tools/fit_accents.py PREV PARTS --family string --front-s 0.15 --write`.
- Check `accent_bodies.json` with `fit_accent_bodies.py`; the c18 body cuts already work toward the same goal.
- It is level only: simulate on the c40 stems and apply by stem fix.
- Targets:
  - string accent front minus body within 1 dB of plain f notes (about -6);
  - accents 2-4 dB over their neighbours on the front;
  - no 2-5 kHz front over +3 dB.

## 5. S1 leftovers on brass: five whole-note and half-note repeats on Horn 1 and Trumpet 2 barely separate (measured)

These are exposed repeats (rel -12 dB or more) with an onset gap of 0.13-0.22 qn and a dip under 3 dB:

| repeat (bar) | dip |
|---|---|
| Horn 1 448 -> 452, C5 (113) | 1.8 |
| Horn 1 526 -> 528, F4 (132) | 2.8 |
| Horn 1 620 -> 624, F4 (156) | -1.3 |
| Trumpet 2 122 -> 124, F4 accented (31) | 1.1 |
| Trumpet 2 453 -> 456, F4 (114) | -0.1 |

- The Solo French Horn's release and the hall fill the re-tongue gap (KIT §7).
- Horn 4's pedals moved from 3.2 to 7.2 dB on the repetition row (c38).

**Fix.** Add `REP_ROW` rows on "LegRep RRx4" (1FH key 34; 1TP key 35 in `build/ks_maps_extra.json`):
- Horn 1: (451.9, 452.1), (527.9, 528.1), (623.9, 624.1);
- Trumpet 2: (123.9, 124.1), (455.9, 456.1).

`REP_ROW_REPEATS_ONLY` keeps brass rows on the repeats, and `REP_ROW_GAP_S` (0.06, 0.15) keeps the re-tongue gap and fall.

Cost: one more row on each of two main-project tracks. That is about 0.1-0.3 GB each (inferred); the c38 Bass clarinet row left the project at 45.92 GiB. Read `footprint` after the settle.

Target: dips of 4 dB or more, and the repeat's 2-5 kHz front at -6..-2 dB.

**Do not touch:**
- the Opus trigger setup (key triggers only, Exclusive), the keyswitch placement and leads, and the SLUR_START_SUS overlaps;
- the Cello solo alias as fitted (DIV A, v70 targets, per-onset leads, the 685 Leg Port at v100 with its lead, contour and join rows) with Violoncellos resting over 679.5-696;
- the c40 JOIN_NOTCH rows and every Leg BC bow-change bump;
- GENTLE_ACCENT brass and winds with their accent fits;
- REP_ROW spans, gaps and the horn gap dips;
- the basses' STR_REP_DETACH spans and `_cb24` shapes (known compromise);
- the re-bow points and fits;
- STAC_ROW and the second-pass stac windows;
- SUBITO_FRESH / SUBITO_TAIL;
- SUL_DEFAULT_CC70 127 (and the Violins I full rebuild c40 asked for).

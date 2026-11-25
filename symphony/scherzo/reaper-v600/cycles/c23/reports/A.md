# Cycle 23, critic A: articulation and phrasing (on the c22 render)

Material: `cycles/c22/render` stems and `cycles/c22/build_render/parts.json` (the data as rendered). I also read the five Hollywood Strings section KS Masters and the 2nd Violins "Marc Lng" files with `opus_state.load_oib` (read only: group envelopes, controller connections, start modes, velocity maps).

Method:
- Levels are the mean of the two channels' powers in 5 ms frames, on the c16 `meas16.py` tempo map.
- I ran the actor's c22 measures as they are: `rt22.py` (kinds sep, acc, pairs) and `fig22.py`.
- My own scripts (deleted) measured three more things: ring (time from a note's peak until the stem is 10 or 20 dB under it, on notes followed by at least 1.2 qn of silence on the track), separation by pitch, and the context of each accent.

"Measured" means a number from the render, from parts.json or from a patch file. "Inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c23, so I did no page-range reading. I used `MANUAL-GAPS.md` and checked the pages behind each finding.

| source (PDF page) | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| HO 2021 p.91-92 (A1) | The sustain rows crossfade non-vibrato, vibrato and molto vibrato with CC1. CC11 is expression and the dynamic crossfade | the bar 23 soft pair (finding 1) | CC1 follows the CC11 lane (61-66 at the pair), so it cannot add level without raising CC11, and CC11 raises the staccato tail before the pair. Patch read: the short rows have no CC1 processor at all |
| HO 2021 p.94 | Staccatissimo is shorter than Staccato, and the shorts' samples end by themselves | Violins I theme staccatos (finding 2) | partly. Violins I "Staccatissimo RRx9" ("V1 Stac" samples) ships a 524 ms release and peaks 81-98 ms after the note-on, against 50-76 ms on Violins II "Stac RRx9" |
| HO 2021 p.97-98 | Legato Slur Staccato puts a "slightly stronger attack" on a slur's first note | the "Stac Slur" row (V1 StacSl samples, 3 velocity layers, 10 ms attack, 221 ms release, 5.6 thousand regions) | not used. It is a fallback for finding 1 |
| HO 2021 p.93 | Marcato Long exists only in the 2nd Violins and Basses | Violins II and basses accents (finding 4) | not used. Read: 2nd Violins "Marc Lng RRx4" has a 6 ms attack, two velocity layers (1-89, 90-127), 372 ms release and 3,760 regions |
| `MANUAL-GAPS.md` #16 | accent rows costed against memory | finding 4 | Violins II "Sus Marc LITE" ships a 368 ms sustain attack (Violins I: 260) and a Marc Shrt overlay with no velocity range above 99. c22's negative range test is explained by this (inferred) |
| `MANUAL-GAPS.md` #1, #3 | woodwind Stac DblTng in use; Spiccato for the leggiero theme | | #1 is in use and works. #3 is superseded by finding 2's measurements |

## Findings, ranked by what a listener would hear

### 1. Bar 23's soft pair: raise it with CC1, not CC11, and shorten its p-layer release. CC1 does not reach the staccato quarter before it.

Where: Violins I, bar 23. F sharp 5 staccato quarter at qn 66, the slurred pair G-A at 67 / 67.5 on "Sus MAX", B landing at 68, C accented at 69. The same treatment then applies to the four loud pairs at 125, 209, 821 and 893.

Evidence (measured, c22 full render):
- Peaks (`rt22.py pairs`): F sharp -40.6 dB, G -49.2, A -48.9, B -30.9. The pair is -13.5 / -13.2 dB against its neighbours.
- Decay before the next note-on (`fig22.py`): F sharp to G 7.0 dB, G to A 3.9, A to B **1.8**, B to C -1.6. A is still sounding when B starts. That is Dan's "overlap / lasting too long".
- Lanes at the pair: CC11 56-63, CC1 61-66. CC1 tracks CC11 in this pipeline, so c22's CC11 lift also raised CC1. The F sharp's tail rose because CC11 is Opus's Global Group volume, which acts on every sounding voice.
- Patch (1st Violins KS Master):
  - "Staccatissimo RRx9", "Stac RRx14" and "Spiccato RRx9" groups carry **no MidiController at all**. Their level is velocity plus the global CC11 table.
  - The "Sus MAX" sustain groups carry a second CC1 crossfade: Non Vib full to CC1 20 and gone by 55; Sus Vib full 55-85; Molto Vib from 70, full from 105.
  - Movement I c32 measured that raising CC1 from 42 to 85-105 makes a soft 1st Violins line 3-16 dB louder, because the Molto Vib samples are recorded louder.
  - So a CC1 lift raises only the Sus MAX pair, not the Staccatissimo F sharp or B. (Inferred from the patch and Movement I's number.)
- Ring:
  - The p-layer sustain groups ("1V p", which dominate at CC11 36-68) are capped at 350 ms in `mix.json`; the mf-ff groups are capped at 150 ms.
  - Release trails are picked by CC11 at the note-off: p RT at CC11 36-68 (source volume 2.82), mf RT at 69-93 (3.98). Their AHDSR does not set their length (Movement I c22).
  - Only 7 of Violins I's 83 "Sus MAX" notes end with CC11 between 36 and 68: 67, 67.5, 113.5, 371.5, 372, 597, 900.
  - So a 150 ms cap on the p groups touches almost nothing else. The ppp G sharps (CC11 under 36, pp groups) and their re-bows are untouched.

Fix (instrument side only; nothing in the volume envelope):
- a) New generic `CC1_FLOOR_SPANS` in `tools/score_to_parts.py`, next to `CC1_SET_SPANS`:
  - Form: `{track: [(q0, q1, CC1)]}` means CC1 at least this value over [q0, q1). In `cc1_fn`, take `max` where `CC1_SET_SPANS` takes `min`, and add the span edges to `vbr` as c20 did. Default empty.
  - Scherzo value: `{"Violins I": [(66.35, 67.70, 108)]}`.
  - The ramp starts after the F sharp's note-on (65.802). The F sharp's row has no CC1, so the ramp may run under its tail. With Opus's 120 ms fade (0.53 qn), the floor is reached by G's note-on at 66.736. It is back down before the C's "Sus Marc LITE" note at 68.296.
  - Leave CC11 exactly as in c22. `C22_SKIP` "66" stays.
- b) `build/mix.json`, Violins I `sus_release_cap_ms`: add `{"dyn": ["p"], "ms": 150, "rows": ["Sus MAX"]}`. Keep pp at 350.
- Checks, on a range test from qn 54 (before the 66.076 keyswitch), control and variant from the same start:
  - pair within 3 dB of the F sharp or above it, and B no more than 2 dB over c22;
  - F sharp to G decay at least 7.0 dB (unchanged: this is the check that killed c22's lift);
  - A to B decay at least 4 dB;
  - the C's first 100 ms within 1 dB of c22.
- If the pair comes out short of its target, add a CC11 rise that starts only at 66.62. That is after the F sharp's tail has fallen: decay 7 dB at G's note-on.
- Then extend: the loud pairs at 125 / 209 / 821 / 893 are still -7.2 / -8.8, -7.1 / -8.4 dB under (measured; CC11 92, CC1 91). c22 rejected their +8 CC11 because the second note grew into the landing note.
  - Try a CC1 floor of 112 over (q - 0.65, q + 0.70) on them.
  - Same checks: the second pair note's decay before the landing note must not fall below c22's 1.8-2.7 dB.
- Fallback for the soft pair if CC1 changes the colour too much: "Stac Slur" (V1 StacSl, 5,640 regions).
  - Velocity 50 (its lowest layer, 1-60), then `region_gain_db` `row_db` {"Stac Slur": x}, fitted on the range test.
  - Its level is velocity plus global CC11, so the F sharp is again untouched. c20's negative test was on the legato-scripted "StacSl Leg BC" row, not this one.

### 2. Violins I staccatos peak late and ring long, so repeated and stepwise eighths run together

This is what the other string sections no longer do since their c20 / c21 release caps.

Where: every Violins I theme statement. Worst at the counterstatement 84-132 (bars 29-44), the tutti pairs on D5 / D sharp 5 (331, 340, 931, 940) and the coda 982-988. The landing staccato of the bar 23 figure is among them.

Evidence (measured):
- Same-pitch eighth pairs, whole movement:

  | track | pairs | separation median | first eighth's peak after its note-on | decay of the first eighth at the second's note-on |
  |---|---|---|---|---|
  | Violins I | 54 | 4.0 dB | 0.081-0.098 s | 0.0-1.1 dB |
  | Violins II | 32 | 6.6 | 0.036-0.076 | 2.0-8.9 (median about 4) |
  | Violas | 21 | 6.8 | 0.046-0.096 | 1.0-5.7 (median about 3.8) |

- By pitch on Violins I:

  | pitch | pairs | separation median | second note's window maximum after its note-on |
  |---|---|---|---|
  | B4 (71) | 20 | 5.3 | 70 ms |
  | D5 (74) | 5 | 0.7 | 34 ms |
  | D sharp 5 (75) | 12 | 2.2 | 32 ms |
  | F sharp 5 (78) | 3 | 0.0 | 22 ms |

  A maximum 22-34 ms after the note-on means the first eighth's tail is louder than the second eighth's attack.
- Counterstatement pairs (103, 109, 115, 121, 127): 0.7, 0.7, 1.8, -0.3, -0.4 dB. Velocity 57-87 on "Staccatissimo RRx9".
- Ring, on staccatos followed by silence (time from the peak to 20 dB under it):
  - Violins I: "Staccatissimo RRx9" 0.208 s (p90 0.254), "Stac RRx14" 0.190 s;
  - Violins II "Stac RRx9": 0.140 s;
  - violas "Stac RRx9": 0.120 s, "Staccatissimo RRx16": 0.130 s.
- Patch: "Staccatissimo RRx9" ("V1 Stac") ships a 524 ms release, "Stac RRx14" 333 ms. The Violins II / violas rows carry the c20 / c21 caps (150 ms, `any_dyn`).
- Why c21 rejected the cap: a 150 ms cap cut the peaks of 40-80 ms notes. Violins I's eighths are written 0.25 qn (57 ms), with their note-off before their 81-98 ms peak. The quarters (0.5 qn, 114 ms) end after it.
- c22's 0.07 s first-eighth lead moved nothing (4.5 -> 3.8, 4.6 -> 5.1 dB), consistent with the cause being the sample's late peak and long tail rather than the spacing. (Inferred.)

Fix (`tools/score_to_parts.py` plus `build/mix.json`; note lengths and release, no levels):
- a) New generic `STAC_MIN_SOUND_S` `{track: seconds}`, default empty: on short rows, a note's sounding length is at least this, but never past the next same-track note-on minus 0.02 s. Scherzo value: `{"Violins I": 0.10}`.
  - The note-off then falls after the attack peak.
  - Alternative: make `STAC_LEN_NEXT_GAP_QN` accept a per-track dict. The global 0.5 qn gap stops `STAC_LEN_SPANS` from lengthening any eighth that is followed by another note 0.5 qn later.
- b) `mix.json` Violins I `sus_release_cap_ms`: add `{"any_dyn": true, "ms": 150, "rows": ["Staccatissimo RRx9", "Stac RRx14", "Spiccato RRx9"]}`.
- Both together, never b) alone: c21's peak loss comes back without a).
- Checks, on range tests of 84-132 and 312-360 against a control:
  - eighth peaks (60 ms) within 1 dB of c22, p10 within 2 dB;
  - ring to -20 dB at 0.15 s or less;
  - separation median 5.5 dB or more, counterstatement p10 2 dB or more;
  - bar 23 figure (`fig22.py`) no occurrence below c22.
- Expected size (inferred): with a 150 ms release starting at 0.10 s, the first eighth is about 10 dB down by the second eighth's peak (0.20 s), against about 3 dB now. This is the state Violins II and violas reached with the same cap.
- If the peaks still drop: test "Stac On Bow RRx9" ("V1 Stac Hrd", 3 velocity layers 1-59 / 60-114 / 115-127, 16 ms attack, 319 ms release, about 6.3 thousand regions) on the D5 / D sharp 5 / F sharp 5 pairs. Not loaded now.

### 3. Flute 1 accents: the p90 of +6.7 dB is half real and half the measure

Where: Flute 1 "Sus Accent MAX" (35 notes), Flute 2 (10).

Evidence (measured; first 100 ms of the accented note, then against the note before it, which is the comparison a listener makes after staccatos):

| note | velocity | CC11 | reading (`rt22 acc`) | against the note before |
|---|---|---|---|---|
| 123 | 90 | 90-91 | +6.7 | +5.0 |
| 819 | 90 | 91 | +8.4 | +6.0 |
| 945 | 90 | 105 | +6.7 | +4.6 |
| 789 | 70 | 68 | +8.6 | +3.6 |
| 207 | 90 | 83 | +5.2 | +3.4 |
| 99 | 70 | 46 | +5.5 | +0.3 |

- Real: the velocity-90 accents, middle StacSs layer 75-114, sit 3.4-6.0 dB over the staccato before them at f, against Dan's target of +1..+2 and no more than +3. At p (velocity 70) they are in range.
- Measure artefacts:
  - The note after most of these is a slurred "Leg Slur MAX" eighth whose first 100 ms is 2-3 dB under its own body (for example 125: -40.9 against -38.8 at 0.3 s). That deflates the neighbour mean.
  - 1014 (+18.1) is compared with the pp entry after the G.P.
  - Flute 2 213 (+9.0) and 897 (+8.1) have neighbours 84 and 72 qn away. Without them Flute 2's p90 is about +3.
- Peaks 0.04-0.07 s after the beat: the row fixed the timing, so keep it.

Fix:
- `mix.json` Flute 1 `region_gain_db` row_dyn_db `{"Sus Accent MAX": {"vel>=75": -3.0}}` (the form used on Violins I "Stac RRx14"). This lowers only the middle and top accent overlays.
- Velocity 70 stays where CC11 is under 80.
- Target: against the previous note +1.5..+3 on 123 / 207 / 819 / 945.
- Measure change for the actor: compare with the previous note when it is detached and within 2 qn, and drop neighbours over 2 qn away. Otherwise the next cycles chase 1014 and Flute 2's isolated notes.
- Flute 2: no change.

### 4. Violins II and basses accents: no front, peak 0.21-0.26 s late. c22's failed Marc LITE test had a patch cause, and Marcato Long is the unused route.

Where:
- Violins II: 42 accents, 32 of them half notes or longer and 8 quarters, all on "Sus MAX" (two on Leg Slur).
- Double basses: 18 accents (14 half, 4 quarter).
- Both include the hemiola 300-304, the tutti 897-910 and the summit 1008-1014.

Evidence (measured, `rt22.py acc` on c22):

| track | median against neighbours | front minus body | peak after the beat |
|---|---|---|---|
| Violins II | -2.7 dB | -0.1 | 0.26 s |
| Double basses | -0.3 dB | -3.2 | 0.21 s |

For comparison: violas -0.6 / +1.9 / 0.14 s; Violins I -0.7 / -2.0 / 0.14 s; celli +0.1 / -0.7 / 0.04 s.

Patch, read:
- Violins II "Sus Marc LITE":
  - sustain groups have a 368 ms attack (Violins I's: 260 ms, the row that works);
  - its Marc Shrt overlay's velocity map reads (1-60), (1-99), (61-99), with nothing above 99.
  - Inferred: a loud accent above velocity 99, or the body fading in over 368 ms under a decaying overlay, gives the -47 / +49 dB outliers c22 measured at the hemiola.
- "Marc Lng RRx4" (Violins II and Basses only, manual p.93):
  - a recorded long marcato stroke: 6 ms attack, layers 1-89 / 90-127, 372 ms release, release trails;
  - 3,760 regions on Violins II, under half of Marc LITE's 8,500;
  - its samples are about twice the size of the Stac files (397 against 205 KB median), so the stroke should cover a half note at quarter 264 (0.455 s). That is inferred and must be checked.

Fix (one track first, range test on 296-312 and 891-912, control from the same start):
- Violins II: `ART_SPANS` "Marc Lng RRx4" on printed accents written 2 quarters or shorter, plus the following tied or slurred note's re-attack rules unchanged. Velocity 80 at f, 100 at ff (layer edge 89 / 90). Keep the CC11 accent bump off on that row (`ACCENT_CC` `skip_rows`).
- Accents longer than 2 quarters stay on "Sus MAX". Do not route held chords: the finale's c24 found Marc LITE negative there.
- Targets:
  - median against neighbours +1..+2, no note over +3;
  - peak within 0.13 s of the beat;
  - front minus body 0..+3;
  - 2-5 kHz first-80 ms share no more than 3 dB over the body;
  - no level hole in the second half of the half notes, and none in the slurred eighths after them.
- Then basses with the same values.
- If Marc Lng decays too early on half notes: "Sus Marc LITE" with the sustain-group attack capped. Generalise `leg_sus_attack_ms` to take `{"ms": 120, "rows": ["Sus Marc LITE"], "prefix": ["V2 "]}`; the overlay's 16 ms attack stays under the cap. Velocities 61-99 only.

### 5. Checked and in order (no change)

All measured on c22:
- **Pizzicato and arco changes**: every pizz.-to-arco and arco-to-pizz. change on celli, basses, Violins II and violas has its keyswitch 0.20-21.9 s ahead of the note, with gaps of 0.31 s or more.
  - The one exception is the celli's pizz. at 1122: keyswitch 21 ms ahead (two audio blocks), and the note sounds (-54.6 dB).
  - Arco entries after pizz. at pp (basses 504 and 1071, celli 828 sub. p) open 9-10 dB under their body in the first 150 ms. These are soft slow-bow entries, as expected.
- **Flute 1 / 2 and oboe staccatos**: Stac DblTng rows, peaks 30-55 ms. No change.
- **Violins II, violas, celli repeated eighths**: 6.6 / 6.8 dB median separation with the c20 / c21 caps.
- **Bar 23 figure, every other occurrence**: c22's `fig23.txt` values hold (bars 38 and 263 improved in c22; the other 30 occurrences are unchanged data).

Not measured this cycle (no claims): timpani rolls and restrikes, harp, tenutos, the trio legato (the string legato swell remains open after five failed controls).

Do not touch:
- Violins I Sus MAX pairs on Sus MAX (no Detache), and the c22 CC11 spans on bars 38 / 263;
- the woodwind Stac DblTng rows and Flute 1 / 2 / Oboe 1 "Sus Accent MAX" (only the overlay level of finding 3 changes);
- the c20 / c21 short-row caps on Violins II, violas, celli and basses;
- the nine theme-head pairs on "Sus Marc LITE";
- the 0.060 s string legato overlap;
- the bar 301 sfp chain in CC11;
- con sordino and sul A lanes;
- the pp-layer 350 ms cap on Violins I (it protects the ppp G sharp re-bows).

# Cycle 22, critic A: articulation and phrasing (on the c21 render)

Material: `cycles/c21/render` stems, `cycles/c21/build_render/parts.json` (the data as rendered; identical to `build/parts.json`), c18 stems for comparison, and the 1st / 2nd Violins and Violas KS Master patch files read with `opus_state.load_oib` (read only). Levels are the mean of the two channels' powers on 5 ms frames. "Own-pitch band" means harmonics 1-3 of a note's pitch, plus or minus 30 cents, from a 4096-point STFT with a 5 ms hop. I used it only where the neighbouring notes are a whole tone or more away, because semitone neighbours leak into the band. My scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c22-A/` (deleted). "Measured" means a number from the render, parts.json or a patch file. "Inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c22. I read A1 (PDF p.89-94, string sections and shorts) in full, because the first check this cycle is the string short figure at bar 23.

| manual (PDF page) | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| p.91 | Detache samples "come to a well defined end"; for notes short enough to count as staccato, use a staccato articulation | the bar 23 slurred eighth pairs (0.114 s each) | yes since c21 (Sus MAX). The Detache test in c20 failed because of the shipped 5286 ms releases, not because of this page |
| p.91-92 | Marcato Sustain plays a marcato sample over the looped sustain, "extra power at the start of the note"; one in each section | the 321 printed accents | only on Violins I (38 notes on "Sus Marc LITE"). Violins II, violas and celli have the row ("Sus Marc LITE", 8.1-8.5 thousand regions) but play their accents on Sus MAX (finding 2) |
| p.92 | the Sustain rows cycle up and down bows by round robin and loop | the Violins I pairs on Sus MAX | yes |
| p.93 | Marcato Long exists only in 2nd Violins and Basses | a possible accent row for Violins II | not used (finding 2 suggests Marc LITE first) |
| p.94 | Staccato On Bow stops the bow on the string; Staccatissimo is shorter than Staccato | the theme's staccato quarters and eighths | partly. Violins I uses Staccatissimo / Stac RRx14 / Spiccato; "Stac On Bow RRx9" is not loaded. Not proposed: memory, and nothing measured points to it |
| p.94 | Repetitions: a dozen repeats in a sample, with release trails | the theme's two repeated eighths | correctly not used (two notes, not a run) |
| p.89-90 | DIV patches are close mics only, and a divisi half is "not much less" loud than the section | the Violin I solo, Violas div | not re-measured this cycle |

From `MANUAL-GAPS.md`: #1 (woodwind Stac DblTng rows) is in use and separates well (Flute 1 / Oboe 1 / Clarinet 2 repeated eighths 7.5-9.9 dB median). #2 (repetition rows) is still not applicable. #3 (spiccato) is in use. #16 (accent rows against memory) is the background to finding 2.

## Findings, ranked by what a listener would hear

### 1. Bar 23 figure (Dan's first check): the soft slurred pairs ring about twice as long as the loud ones and sit 7-13 dB under their neighbours. The cause is the dynamic layer that their CC11 selects, not velocity. A CC11 lift fixes both.

Where: Violins I, the three soft pairs among the 18 `_c20_pairs`: bar 23 (qn 67), bar 38 (113) and bar 263 (787), all on "Sus MAX".

Evidence (measured):
- **Separation, c21 = c18.** The Sus MAX pairs are back in the c19 state, and every number below is the same on the c18 stems.
- **Ring time.** Ring is the time from the note-off until the own-pitch band is 20 dB under its peak. The figure G-A-B moves in whole tones, so these bands are clean.

  | pairs | CC11 | first note | second note |
  |---|---|---|---|
  | bar 23 | 54-61 | 0.28 s | 0.19 s |
  | bar 38 | 55-56 | 0.29 s | did not fall 20 dB within 0.9 s |
  | bar 263 | 66-73 | 0.17 s | 0.13 s |
  | loud pairs | 82-107 | 0.12-0.16 s | 0.12-0.16 s |

  At bar 23 the A is still only 1.8 dB under its own peak 80 ms after the B starts. This is the "lasting too long / overlap" Dan described, and it is still in c21.
- **Level** (peak within 0.11 s of the moved note-on, Violins I stem):

  | bar | F sharp (preceding staccato quarter) | G | A | B (landing staccato) | C (accented half note) |
  |---|---|---|---|---|---|
  | 23 | -42.1 | -50.0 | -50.6 | -32.9 | -29.8 |
  | 38 | | -41.6 | -47.6 | -35.2 | |
  | 263 | -37.3 | -50.0 | -45.5 | -29.1 | |

  By contrast, the nine soft theme-head pairs on "Sus Marc LITE" (bars 18, 258: 53, 773) read within 1-4 dB of their neighbours (-41.7 / -38.7 against -37.3 / -36.9).
- **Patch** (1st Violins KS Master, "Sus MAX"):
  - no group has a MidiVelocity processor, and every region spans velocity 1-127. So velocity cannot raise these notes: the pair velocities 62-72 are irrelevant to level.
  - mix.json caps the release at 350 ms on the pp / p sustain groups and 150 ms on mf-ff, and the p and pp groups ship 524 / 931 ms.
  - The release-trail groups (" RT", p: volume 2.82, release 1245 ms) are not capped.
- The ring tracks CC11. At CC11 of about 80 or more, ring is 0.12-0.16 s; at 54-61 it is 0.19-0.29 s. That matches the 150 ms against 350 ms caps on the mf and p groups. The cause is inferred from this correlation and the patch values; the correlation itself is measured.

Fix: `build/score_config.py`, the c21 `CC11_ADD_SPANS` form, instrument side only.
- Change: `CC11_ADD_SPANS["Violins I"] += [(66.30, 67.70, 20, 20), (112.30, 113.70, 20, 20), (786.30, 787.70, 16, 16)]`.
  - The lift starts at the preceding note's note-off. Opus smooths CC11 over 120 ms (`fadeTime` 120 in the global group), which is 0.53 qn here, so the lift is full by the first pair note's attack.
  - It ends inside the second pair note, so it has mostly faded before the landing B peaks (+97 ms after its note-on).
- Expected result:
  - the pairs reach CC11 of about 74-93, inside the mf groups with their 150 ms cap;
  - at the Staccatissimo slope I read from bar 23 (F sharp to B, same velocity layer, +18 CC11 units = +9.2 dB, about 0.5 dB per unit) the pairs rise 8-10 dB, between the F sharp and the B, as the printed crescendo asks;
  - c18 measured 0.48 dB per unit for 2nd Violins Sus MAX at p.
- Checks, by range test (one start for control and variant, starting before the 66.076 Sus MAX keyswitch):
  - ring 0.16 s or less on bars 23 / 38 / 263;
  - each pair note within 3 dB of the F sharp or the note before it;
  - the B no more than 2 dB above c21;
  - decay before the next note-on (c21's `fig21.py`) 5 dB or more.
- Alternative if the lift changes the colour too much: give these three pairs the nine theme-head pairs' treatment.
  - `ART_SPANS` "Sus Marc LITE" with `vel_by_cc` [(34, 70), (46, 78), (58, 86), (72, 94)] and a 0.09 s `REATTACK_LEAD_AT`; the row is already loaded.
  - Measure ring there first. On the theme-head pairs I could not read ring cleanly, because the steps are semitones.
- Do not raise velocity: it has no path to level on this row.

### 2. String accents on "Sus MAX" have no front: they peak 0.22-0.26 s after the beat, and the body is louder than the front. The section's own Marcato Sustain row is unused outside Violins I.

Where: Violins II (35 accents on Sus MAX), violas (29), basses (18), celli (21). This includes the tutti chord accents of bars 72 (213), 101-102 (300-304), 300 (897) and the summit 337-339 (1008-1014). The finale's c24 found the same 212 ms swell.

Evidence (measured on the c21 stems; for each accented note, first 100 ms against the unaccented neighbours, time of the peak within 0.45 s after the beat, front 30-180 ms minus body 250-400 ms):

| track, row | n | against neighbours | peak after beat | front minus body |
|---|---|---|---|---|
| Violins I, Sus Marc LITE | 20 | +3.8 dB | 130 ms | -2.9 |
| Violins I, Sus MAX | 24 | -2.4 | 224 | -3.4 |
| Violins II, Sus MAX | 35 | -3.9 | 262 | -4.5 |
| Violas, Sus MAX | 29 | -1.4 | 225 | -0.7 |
| Double basses, Sus MAX | 18 | -2.4 | 246 | -5.3 |
| Violoncellos, Sus MAX | 21 | +0.1 | 115 | -2.7 |

- Tutti 300-304: Violins II / violas / celli / basses peak 260-360 ms after the beat.
- 2-5 kHz share, first 80 ms minus body: -1.2..+1.2 dB median. There is no bite anywhere, so a firmer front stays within "weight, not bite".
- Violins I is the one section whose accents arrive on time, and it is the one with the marcato overlay. Its "Sus Marc LITE" regions are "V1 Marc Shrt" overlays (velocity layers 1-65 / 66-108 / 109-127, 43 ms attack, decaying) over sustains with 260 ms attacks: the manual's p.91-92 design.

Fix (memory: about 8.1-8.5 thousand regions per row, about 0.37 GB each at c02's 4 GB per 92 thousand; REAPER settled at 43 GB):
- Violins II first, then violas: route printed accents on Sus MAX to "Sus Marc LITE" with Violins I's settings (`ART_SPANS` with `vel_by_cc` [(58, 74), (72, 80), (88, 84), (100, 88)]).
- mix.json `region_gain_db` `row_db` {"Sus Marc LITE": -9.0} plus `row_dyn_db` {"vel<66": -4.0}. This is Violins I's -8 / -4, one dB lower, because Violins I's accents read +3.8, over Dan's +3 limit.
- Add "Sus Marc LITE" to the Violins II and violas entries of the 120 ms release cap, as on Violins I (c07).
- Keep the CC11 accent bump off on that row (`ACCENT_CC` `skip_rows`, as for Oboe 1's "Sus Accent MAX").
- Targets:
  - median against neighbours +1 to +2 dB, no track over +3;
  - peak within 0.13 s of the beat;
  - front minus body 0 to +3;
  - 2-5 kHz first-80 ms share no more than 3 dB over the body.
- Basses: try the same row in a later cycle (they also have "Marc Lng"; p.93).

Also on Violins I itself: lower the Marc LITE accents, because the bar 18 / 24 / 26 heads read +7.6..+10.6 over neighbours. `row_db` -8 -> -10 on velocity 66 and up, measured against the target above.

### 3. Woodwind accents: Flute 1 and Flute 2 still play them on "Sus MAX" and swell late. The Oboe 1 test shows the KS Master's own accent row works.

Where: Flute 1 (36 accents, 35 on Sus MAX), Flute 2 (10). These include the counterstatement accents 87-123 and the second idea.

Evidence (measured):
- Flute 1: -3.4 dB against neighbours, peak 242 ms after the beat, front minus body -2.5.
- Flute 2: -1.8, 275 ms, -1.8.
- Oboe 1's four "Sus Accent MAX" notes: front minus body +0.6 (Oboe 1's Sus MAX accents -1.4), peak 154 ms within my 0.45 s window. The c21 range test read 0.03 s for the first peak.
- The FL and FL2 KS Masters both have "Sus Accent MAX" (`ks_maps.json`; about 7.1 thousand regions, from c21's count).
- Flute 1's 2-5 kHz first-80 ms share is +5.8 dB over the body (median). That is the sustain sample's breath attack, so check bite on the new row.

Fix: `build/score_config.py` c21 item 7 form (`_sacc` block). Add "Flute 1" and "Flute 2" with `ART_AT` "Sus Accent MAX", `VEL_SET` 70 at p-mf and 90 at f, and `ACCENT_CC` `skip_rows` ("Sus Accent MAX",).
- Range test Flute 1 87-132 against a control from the same start.
- Targets as in finding 2, plus 2-5 kHz no higher than now.
- Cor anglais stays off this row (c21: 300 -7.0 dB).
- Measured: the symptoms. Inferred: that the flute row behaves like the oboe's.

### 4. Violins I repeated staccato eighths: in 8 of 49 same-pitch pairs the second eighth is not heard over the first's tail

Where: Violins I at:
- bar 41 (121) and 43 (127): counterstatement, f;
- 114 / 314 (340 / 940): tuttis, "Stac RRx14";
- 309 (925);
- 253 (757);
- 328 / 330 (982 / 988): coda.

Evidence (measured; peak within 0.11 s of each moved note-on, trough between the peaks):
- Median separation by passage:

  | passage | separation | p10 |
  |---|---|---|
  | 13-28 | 6.0 dB | |
  | counterstatement 29-44 | 3.4 | 0.0 |
  | tutti 105-120 | 6.7 | |
  | tutti 305-320 | 6.6 | 0.6 |
  | coda | 6.2 | 0.8 |

- In the failures the first eighth peaks late (81-103 ms after its note-on; Staccatissimo / Stac RRx14 median 81-99 ms, against 56-75 ms for Violins II "Stac RRx9" and 30-55 ms for the woodwind Stac DblTng rows). The second note's window maximum then sits at its own note-on (-3..+22 ms), which means the first note's tail is louder than the second's attack.
- Both eighths take the same 0.045 s lead (`STAC_LEAD_S`), so they are 0.114 s apart.
- The perceived attack (peak) lands +34..+49 ms after the beat; the other strings land +22..+51 and the woodwinds +9..+47. S2 holds, but Violins I is the latest of the strings in the tuttis.
- c21 rejected release caps on these rows (they cut the 40-80 ms notes' peaks). This fix leaves the samples alone.

Fix: give the first eighth of each Violins I same-pitch staccato pair 0.07 s of lead and keep 0.045 s on the second.
- Mechanism: `LEAD_SET_AT["Violins I"]`, keys `str(sq)` of each first eighth (37, 43, 49, 55, 64, 73, 79, 91, 103, 106, 109, 115, 121, 127, 205, 283, 292, 313, 319, 325, 331, 340, 349, 355, 757, 763, 769, 775, 784, 793, 799, 811, 817, 823, 889, 913, 919, 925, 931, 940, 949, 955, 982, 985, 988, 991, 994, 997), or a generic `STAC_PAIR_FIRST_LEAD_S` in `score_to_parts.py`.
- This gives 0.139 s between the eighths and moves the first eighth's peak to about +10..+30 ms after the beat (closer to S2).
- Check on a range test of the counterstatement and the tutti:
  - p10 separation 3 dB or more;
  - the second eighth's peak no longer at its note-on;
  - the first eighth's peak 0..+40 ms from its beat.
- Inferred: the gain. The Staccatissimo tail falls about 6 dB in the 20 ms after its peak on the two clean cases I could read, so 25 ms more time should be worth several dB where the first note peaks late.

### 5. The loud Sus MAX pairs sit 6-11 dB under the landing staccato

Where: Violins I pairs at CC11 82-92: bars 42 (125), 70 (209), 274 (821), 298 (893).

Evidence (measured, same peak measure as finding 1):

| bar | pair | landing B |
|---|---|---|
| 42 | -34.7 / -35.8 | -28.6 |
| 70 | -35.0 / -35.7 | -28.9 |
| 274 | -34.6 / -41.7 | -30.5 |
| 298 | -38.3 / -41.2 | -29.8 |

- Ring is short here (0.12-0.16 s), so these pairs do not blur. They are faint, and the slur's two notes read as a dip before the quarter.
- In the tuttis (CC11 103-107) the first pair note is level with the B, and the second is 3-5 dB under.

Fix: `CC11_ADD_SPANS["Violins I"]` +8 units over (q - 0.70, q + 0.70) for q in (125, 209, 821, 893), the same form as finding 1. Target: each pair note within 3 dB of the B; ring 0.16 s or less. Inferred size (about 0.5 dB per unit).

### 6. Checked and in order (no change)

All measured:
- **Tutti sfp, bar 301 (qn 900).** The master falls from the sf (-16.4 dB) to -27 at 0.35-0.45 s, then rises with the crescendo. Every string stem falls 10-15 dB inside 0.4 s. This is the printed sfp; the drop is in CC11, before the hall (S3).
- **Woodwind repeated staccato eighths** on Stac DblTng: separation 7.5-9.9 dB median (Flute 1 coda single pair 3.0).
- **String short-row caps** (c21): Violins II, violas and celli repeated eighths 6.0-10.8 dB median.

Not measured this cycle (no claims): timpani rolls and restrikes, harp, pizzicato edges, tenutos, the trio legato.

Do not touch:
- Violins I pairs on Sus MAX, with no Detache (fix the soft ones by CC11, finding 1);
- no release cap on the Violins I short rows;
- the c21 caps on Violins II / violas / celli / basses;
- woodwind Stac DblTng rows;
- the nine theme-head pairs on Sus Marc LITE;
- Oboe 1 "Sus Accent MAX";
- the 0.060 s string legato overlap;
- the bar 301 sfp chain;
- con sordino and sul A lanes.

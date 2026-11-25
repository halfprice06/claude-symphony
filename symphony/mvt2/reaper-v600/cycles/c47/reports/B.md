# Cycle 47, critic B: balance and levels (on the c46 render)

c47 is the last cycle before Dan listens, so the findings are ranked by what a listener will hear.

## Method

- I measured the 32 dry stems and the master of `cycles/c46/render/` against `cycles/c45/render/`. For a few questions I also used the stems of c37, c43 and c44, and the Dvořák 9/i reference.
- Analysis frames: 4096-point Hann windows, hop 1024 (21 ms), power of both channels summed.
- Weightings: K-weighted (BS.1770 response) and A-weighted. Band levels use 1/3-octave bands.
- "Own-band margin": the lead's level over the sum of every other dry stem, in the 1/3-octave bands from 100 Hz to 10 kHz, weighted by the lead's own energy per band. It answers "is the lead masked", where K-weighted margins answer "is it louder".
- Positions come from each render's own `rendered_build/parts.json` tempo map, so qn bins match across c45 and c46 despite the c46 rubato.
- Labels: **measured** is a number from a render or the data; **predicted** is arithmetic on measured levels; **inferred** is a judgement about what a listener hears.
- I changed no audio settings and touched no REAPER, build or tool file. Scratch files were in `/private/tmp/claude-501/mockup-loop/mvt2-c47-B/` and are deleted.

## Manual notes (row c47/B: group B2, May 2021 HO manual PDF pp. 194-200, read in full with the page images; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.194, 196: the Mix page has one channel strip per instrument, with sub-mixer channels per mic (volume, pan, load/unload). | Mic levels and pans are written into each Opus state from `mix.json` (`mics`, `pan_by_mic`): Close at the seat, Main full width (c44 template). Track level comes from REAPER gain and the volume envelope. | **Followed.** The Opus master fader is not used, so the c46 brass re-levelling (`gain_db`) leaves the mic mix untouched. |
| p.196, 198: an FX Bus with a Reverb insert is fed by "Reverb Send" inserts on the sub-mixer channels. The send has a level slider and a Post switch; post-fader is "typically used to have the same level of signal present in the main mix as being sent to the FX Bus". | Since c44 the Opus FX bus reverb is off on every track (`reverb.opus_off`). The hall comes from REAPER Spaces II returns fed by post-fader sends (`return` in `mix.json`). | **Followed, by another route.** Because the sends are post-fader, every role, trim and volume-envelope shape also moves the hall. CC7 and CC11 act inside Opus, so they move it too. The low instruments' sends are off (c44), so the c46 basses trims added dry level only. |
| p.195: Store Mix / Restore Mix. | Not used. Every mix setting is rebuilt from `mix.json` (project rule). | **Not applicable.** No change needed. |
| p.199-200: EQ inserts inside Opus: Bass Comp (32-256 Hz "Fat" boost), Channel Equalizer (3 bands), Equalizer (6 bands, HP/LP/peak/shelf), Tone Enhancer. | All EQ is ReaEQ after Opus: `family_eq`, `loud_eq` (wet-automated), side EQs, and the c46 brass bells. | **Followed, by another route.** ReaEQ sits in the same place in the chain (after the mic mix, before the send) and can follow the score, which the Opus EQ cannot. Bass Comp is not needed: loud-frame 60-100 Hz is already above the reference ("Also measured"). |

MANUAL-GAPS bearing on this lens:
- **#8 (4 soli on half-section patches):** the levels are on target. Basses 4 soli at 220-226 sit -3.2 dB K under the celli; coda celli 4 soli (Vc div) are level with the basses (+0.0). Only timbre is open.
- **#4 (Mid mics):** superseded by the c44 layout.

## Did c46's changes make a solo lose to its accompaniment? (measured)

**No solo window got worse overall.** The table gives each lead's K-weighted margin over the sum of all other dry stems (median over the frames where the lead sounds). The last column is the own-band margin in c46.

| Solo | c45 | c46 | Own-band (c46) |
|---|---|---|---|
| Horn 1, bars 7-14 | +4.8 | +5.1 | +13.8 |
| Oboe 1, bars 15-16 | +1.9 | +1.7 | +14.4 |
| Solo violin, bars 17-18 | +5.4 | +6.5 | +19.6 |
| Oboe 1, bars 19-20 | +2.9 | +3.3 | +15.1 |
| Solo violin, bars 21-22 | +2.4 | +3.2 | +16.2 |
| Bass clarinet, bars 31-36 | +4.2 | +5.5 | +12.3 |
| Flute 1, bars 37-40 | +2.7 | +3.0 | +12.4 |
| Cor anglais, bars 41-44 | -0.9 | -0.8 | +12.8 |
| Oboe 1, bars 45-47 | +1.4 | +1.8 | +9.3 |
| Cor anglais, bars 48-50 | +0.6 | +1.6 | +14.1 |
| Trombone 1, bars 63-64 | +6.7 | +7.5 | +14.8 |
| Horn 1, bars 67-70 | +5.0 | +5.3 | +13.2 |
| Clarinet 1, bars 85-89 | +1.0 | +1.3 | +12.1 |

What the c46 changes did:
- **Solo roles:** Bassoon 1 -4.5, the cor anglais rows, celli -3 at 152-164 and basses -3 at 139.9-146 did what they were meant to.
  - Horn 1 over Bassoon 1 at qn 232: +7.2 -> +9.6.
  - Bass clarinet over the cor anglais at 93-94: +4.0..+4.4 -> +7.0..+7.2.
  - Cor anglais over its strongest accompanying stem at 152-154: +1.1 / -0.8 / -1.4 -> +5.2 / +4.0 / +2.7.
  - Oboe 1 over the basses at 140-141: +4.7 / +1.8 -> +7.9 / +4.7.
- **Brass bells and gains:** each stem's K level held within about 0.5 dB at the climaxes.
  - Horn 1 bars 7-14: lead +0.0 to +1.6 dB, margin +0.3.
  - Bars 61-62: brass levels relative to Violins I unchanged since c43 (Trombone 2 -3.6, Horn 1 -5.1).
- **Basses and bass clarinet trims:** they changed no solo window ("Also measured" covers the bass weight).
- **Hairpin curves:** the only measurable losses, all local. Each is a curved accompaniment hairpin rising faster than the lead's (finding 3):
  - Oboe 1 over Violins II at qn 46: +6.1 -> +3.7.
  - Cor anglais over Flute 1 at qn 133/134: +3.4/+3.4 -> +2.4/+1.7.
  - Clarinet 1 over the basses at qn 284/285: +7.8/+3.7 -> +6.6/+2.2.
- **Other new rows (S3):** the c46 role rows ramp over 0.5-1.5 qn, so none of them puts a step under a sounding chord.

## Findings, ranked by what a listener will hear

### 1. Bar 80 downbeat (qn 266-267.75): one oboe note is the loudest sound in the ff cadence (measured)

**Where:** Oboe 1 A flat 5 (score onset 266, moved onset 265.952, legato target v104, 1.93 qn). Bar 80 of the ff cadential bars 79-82. Oboe 1 doubles Violins II and Clarinet 1 an octave under Flute 1 and Violins I.

**Evidence (measured, c46, K-weighted):**
- The note body is 9.8 dB over its neighbours: Oboe 1 reads -4.0 at 265, +6.0 / +5.5 at 266 / 267, and -1.9 at 268.
- Against the ensemble at 266 / 267 it is the loudest stem:
  - Violins I +3.2 / +1.8;
  - Violins II (same note) +1.8 / +1.0;
  - Clarinet 1 (same note) -1.5 / -1.8;
  - celli +3.3 / +3.7.
- A-weighted it is +3.6 / +4.3 over Violins I.
- At 266.5-267.5 this one oboe carries 21-22 % of the whole orchestra's dry energy and **38-43 % of the 1-4 kHz band**.
- History:
  - c43 (legato velocity 60): +4.7 against neighbours +0.9 / -2.0.
  - c44 (template mics): the neighbours fell about 6 dB and this note did not.
  - c45 (`LEG_VEL_BY_CC`, v104): +6.0.
  - The A flat 5 sample is hot at this CC11 (114-118, the same as its neighbours, with the same volume envelope of +3 to +4 dB).
- No critic flagged it because the solo checks do not cover tuttis. The cor anglais's A flat at the same downbeat was already tamed in c38 (`CC7_POINTS["Cor anglais"]` 90 at 266).

**Inferred:** a bright oboe "honk" on the downbeat of bar 80, 1.5 beats long, louder than the melody. It is the single most obvious level fault left in the loud music.

**Fix:**
- `build/note_trims.json` "Oboe 1": add **"266": -8**.
- `build/score_config.py`: make it a step, `NOTE_TRIM_RAMP_S["Oboe 1"][266.0] = 0.1`, as for 190.0. Check that the key matches the note `score_to_parts.py` compares (the moved onset is 265.952; the tolerance is 0.02).
- Level only, so a stem fix is equivalent.

**Predicted:**
- Oboe 1 at 266 / 267: about -2.0 / -2.5. That is between its neighbours, about level with Clarinet 1, and 5 dB under Violins I.
- Dry sum -0.5 to -0.9 dB over 266-267.5.
- Bar 80 stays well under bar 61 (master K 13.9 against 20.2), so the climax order and the limiter are safe.

### 2. End of bar 82 (qn 272.5-274): the bass clarinet's held A flat 2 swells 6 dB against its printed p > pp and stalls the close into the coda (measured)

**Where:** Bass clarinet A flat 2, score onset 271, 3 qn. Printed p with a decrescendo to pp over the full close in A flat. Every other part is dying away under the harp's p > pp arpeggio.

**Evidence (measured, c46, K per 0.25 qn from 272.5 to 274.0):**

| | 272.5 | 272.75 | 273.0 | 273.25 | 273.5 | 273.75 | 274.0 |
|---|---|---|---|---|---|---|---|
| Bass clarinet | -16.7 | -15.0 | -15.6 | -14.7 | -12.4 | **-10.7** | -12.1 |
| Master | -4.1 | -6.4 | -3.6 | -6.8 | -7.1 | -7.1 | -5.8 |
| Every other stem (sum) | -3.7 | -6.2 | -5.7 | -9.2 | -8.8 | -9.1 | -8.7 |

- At 273.75 the bass clarinet is 22-41 % of the dry sum. It is louder than the harp (-18.0) and the basses (-19.0).
- The master stops falling for about one second (-6.8, -7.1, -7.1) before the coda's harp harmonics.
- c45 is identical (-16.1 -> -10.7), so this is not a c46 change.
- Two causes:
  - The decrescendo's dB ramp releases inside the note: `vol_db` -2.5 at 273.0 -> -1.5 at 273.75 -> -0.5 at 274.0. That is +2 dB. Kit LEARNINGS §4 records the same problem on a fermata chord.
  - The rest is the bass clarinet's A flat 2 sample swelling at CC11 34-36. That is the layer edge of the BC KS Master (kit §4), on the pitch whose swell c28/c35 had to shape in bars 3-6.
- The same pitch is uneven at pp in the chorale under Horn 1 (bars 7-14).
  - The A flat 2s at 18, 24 and 39 have bodies of -15.1 / -15.5 / -15.8. The bass clarinet's other pp notes there read -18 to -26 (B flat 1, C sharp 2, E flat 2 at -25 to -26).
  - The horn stays 9 dB over it, so this is a lumpy accompaniment, not a covered solo.

**Inferred:** in a quiet thinning chord, a low reed swelling up as the last sound of the A' section is audible. It undoes the printed morendo into the coda.

**Fix (pre-hall, so the room rings on; S3):** `build/score_config.py`:
```
CC7_POINTS["Bass clarinet"] = CC7_POINTS.get("Bass clarinet", []) + [
    (272.75, 127), (273.0, 101), (273.25, 82), (273.5, 57), (273.75, 40), (275.5, 40), (276.0, 127)]
```
- These values are -2, -3.8, -7 and -10 dB (CC7 is linear amplitude on the KS Masters, c29). No bass clarinet note follows, so the return to 127 is silent.
- The depth includes the +2 dB ramp release. If the actor prefers, hold the ramp at -2.5 to the note end instead and use 3 dB less CC7.
- Optional, same pitch: `build/note_trims.json` "Bass clarinet" **"18": -4, "24": -4, "39": -4**. This leaves the shaped 6/10/13.5 pedal and the solo trims at 91-92.5 untouched.

**Predicted:**
- Bass clarinet -17.6 / -18.5 / -19.4 / -20.7 / -22.1 at 273.0-274.0.
- Its share at 273.75 falls 41 % -> about 5 %.
- The master keeps falling about 2 dB more through the last beat.
- Optional trims: the three A flat 2s at about -19, level with its notes at 21 and 29-30 (-18 to -19).

### 3. The c46 hairpin curves lift three accompaniments under solos; keep them linear there (measured; audibility inferred small to medium)

**Mechanism (measured):** the curve adds the most dB on low CC11 values, where a CC step is worth 0.35-0.57 dB. When a soft accompaniment shares a hairpin with a lead playing higher on the lane, the accompaniment gains more than the lead.

**(a) Oboe 1, bars 15-16 (qn 42-47).**
- Violins II rose +1.8 / +2.7 / +1.3 / +0.8 / +2.3 dB at 42-46 over c45. Oboe 1 rose +0.8 / +1.1 / +0.2 / +0.3 / 0.0.
- Oboe over Violins II at 46: +6.1 -> +3.7.
- Oboe over the whole accompaniment in bars 15-16: +1.9 -> +1.7 dB median, 22 % of frames under it.

**(b) Cor anglais solo, bars 41-44 (qn 124-140; "solo, dolce cantabile", p -> mp).**
- Flute 1 is printed one level under it (pp -> p, decrescendo from 131 to pp at 136) an octave above. Under the curve it rose +1.4 / +2.2 at 133 / 134.
- The celli, the strongest accompanying stem, rose +0.3 to +1.1 at 125-131. That includes their 129 legato target, already 7 dB over its neighbours and only 2.7 dB under the cor anglais.
- The cor anglais over Flute 1 at 133 / 134: +3.4 / +3.4 -> +2.4 / +1.7. Over the whole bar 41-44 span the flute is at -2.8 dB median (c37's target was -3). At 127 and 130 the flute is level or over: flute minus cor anglais 0.0 / +0.7 dB K, and 1.2 / 1.8 dB over A-weighted.
- Inferred: where the flute is level, the ear takes the higher line as the tune, so this solo is the one most likely to sound like a flute melody with cor anglais below.

**(c) Clarinet 1 coda solo, bar 85 (qn 283-286).** The ppp pedal's crescendo on Violoncellos div rose +1.1 / +2.2 / +3.0 / +1.2 dB at 283-286, and the basses +0.6 / +1.1 / +0.8. This is the place where c24 set `HP_SOFT_ACC_SKIP` 283 so that the accompaniment would not swell under the clarinet. The own-band margin is unchanged (+18.6), so this is level, not masking.

**Fix (`build/score_config.py`, the c46 HP_CURVE block):** add to `HP_CURVE["linear"]`:
- `"Violins II": [(42.0, 47.0)]` (keep its existing 146-152.5 and 212-216);
- `"Violins II div": [(42.0, 47.0)]`;
- `"Flute 1": [(131.0, 136.0)]`;
- `"Violoncellos": [(124.0, 132.0)]` (plus its existing entries);
- `"Violoncellos div": [(283.0, 286.0)]`, `"Double basses": [(283.0, 286.0)]`, `"Violas div": [(283.0, 286.0)]`.

The generic version (critic B c46 #3) is cleaner if the actor has time: no curve on a non-lead track whose hairpin overlaps a `LEAD_SPANS` or solo window.

If the flute is still level with the cor anglais at 127/130 after this, change Flute 1's c37 role [125.75, 131.5, 3, 0.5] to 1.5 dB. That still leaves the flute at least 1 dB over the pizzicato accompaniment, as c37 required.

**Predicted:** the c45 margins come back:
- Oboe 1 over Violins II at 46: about +6;
- cor anglais over Flute 1 at 133-134: about +3.4;
- Clarinet 1 over the pedal at 284-285: about 1-1.5 dB more.

Nothing else moves (CC11 lanes only).

### 4. Horn 1's counter-melody in bars 59-60 (qn 196-204) is masked by the violins (measured; fix predicted)

**Where:** Horn 1 (f at 196, crescendo from 200 into the ff at 204) against Violins I/II, Flute 1 and Oboe 1 in unison on the theme (f), with the celli espr. BRIEF names "Horn 1's counter-melody" as part of this section.

**Evidence (measured, c46):**
- Own-band margin: +2.6 dB median in bars 57-58 (qn 182-196), with 24 % of frames under 0. In bars 59-60 (196-204) it is **-0.9 dB median, 59 % of frames under 0**.
- Every solo in the movement has an own-band median of at least +9 dB, and the celli counter-melody of bars 71-74 has +4.2.
- K-weighted, Horn 1 minus Violins I per beat at 196-203: +0.2, -2.1, -6.0, -1.2, -5.1, (-4.9 against the celli at 201), -5.2, -7.4. A-weighted: -0.8 to -9.7.
- Earlier cycles raised the counter-melody up to bar 58 (c41-c42: +2 / +3 over 184-195.35). Bars 59-60 only carry the old [188, 204, 2, 4] row.
- Horn and violins are printed at the same f. A single horn at f is about one string section (kit §13, Rimsky-Korsakov's resonance table), and here it is set against two sections plus flute and oboe in unison. So about -2 to -3 dB under Violins I is the norm, against -5 to -7 measured.

**Fix:** `build/roles.json` "Horn 1": add **[198.0, 203.9, 2.5]**.
- It ends before the 204 front, so the c36 bar 61 shape (front kept off the lift) and the limiter margin are untouched.
- If 198 is a legato target, the role ramps in after its onset (role code), which is what is wanted.

**Predicted:**
- Horn 1 minus Violins I at 198-203: about -3.5, +1.3, -2.6, -2.4 (celli), -2.7, -4.9.
- Own-band median about +1.5 dB.
- Master +0.1 to +0.2 dB in bar 60; bar 61 unchanged.
- Check after the render: bar 61 is still the loudest bar, and the limiter is at or under 2.6 dB.

### 5. Coda, bars 84-85: the timpani's E flat-C-A flat answer loses its first note (measured)

**Where:** Timpani pp strokes at 277 (E flat 3, v56), 278.5 (C3, v60) and 279 (A flat 2, v60). They answer the harp harmonics over the ppp A flat pedal.

**Evidence (measured, c46):**

| Stroke | Peak (K, first 200 ms) | Over the rest of the orchestra | Master jump at the stroke |
|---|---|---|---|
| 277 | -11.4 | +4.0 | **+1.7** |
| 278.5 | -8.2 | +5.7 | +11.7 |
| 279 | -9.5 | +3.5 | +4.8 |

- The first stroke is 3.2 dB under the second, and it lands while the bar 83 harmonics still ring.
- c45: +2.5 / +7.8 / +6.4 master jumps. The first stroke's jump fell 0.8 dB in c46 (its peak 0.5 dB, the pedal slightly up).
- All three are printed pp.

**Inferred:** the motto is heard as two notes, C-A flat, with only a faint thud before them.

**Fix:** `build/score_config.py`: `LEVEL_SHAPES["Timpani"] += [[(276.96, 0.0), (276.99, 2.5), (278.3, 2.5), (278.45, 0.0)]]`.
- This is a step on the stroke, the kit §13 rule for struck notes, the same form as the c35 shape at 172.
- It holds until just before the 278.5 stroke, so the second stroke is unchanged.

**Predicted:** 277 peak about -8.9, between the other two; master jump about +3.5 dB. The roll rule does not apply (single strokes), and nothing changes between the strokes.

## Also measured, no change

- **Bass weight after the c46 basses trims (f +2.5, ff +4.0):** solid, not boomy, with one place to listen. The basses are about back to c43 levels and still under the celli. The low band is heavier than c43 mainly because the c44 template EQ thinned the mids.

  | Measure | c46 | c45 | c43 |
  |---|---|---|---|
  | Basses minus celli, bar 61 | -5.1 | -8.1 | -6.2 |
  | Basses minus celli, bar 62 | -2.0 | -5.0 | -4.6 |
  | Basses minus celli, bars 79-80 | -3.4 | -6.4 | -4.8 |
  | Loudest 10 % of frames, 60-100 Hz re 250 Hz-2 kHz | -15.1 | -16.3 | -16.9 |
  | Same, 100-250 Hz | -6.4 | | |
  | Master 50-100 Hz re 250 Hz-2 kHz at qn 198-199 | -8.5 | -11.1 / -10.7 | -11.4 / -12.2 |

  - Reference: Dvořák (lossy) reads -17.8 for 60-100 Hz and -4.5 for 100-250 Hz. c37 read -17.6 for 60-100 Hz.
  - The listening spot is bar 59 beats 3-4. There the basses' G1 puts nearly all of its energy at 98 Hz, and the master's low band is 3-4 dB heavier than in c43 and 6-9 dB heavier than the surrounding beats.
  - With Dan listening next, I would not move the trims. If Dan hears the bass as thick there, take the basses' f trim from 2.5 to 1.5 (bars 57-60 only move).
- **Climaxes (bars 61-64, 79-82):**
  - Family sums re strings (K, bar 61 / 62): winds -3.4 / -2.8, horns -6.0 / -5.2, low brass -3.3 / -4.7, timpani -15.5 / -22.5. At bars 79-80: winds 0.0, horns -5.3, timpani -15.5.
  - The timpani rolls are never the loudest stem anywhere: -11 to -23 dB under the rest per beat. Their share of 30-150 Hz is 2-19 %, except at the ends of the printed crescendos into 172 (52 %) and 203 (31 %).
  - The low brass (printed f) sit 4-9 dB over each single ff woodwind and 1-4 dB over Horns 1-2 (ff) at bars 61-62. That relation has been the same since c43 and is protected (c37 brass +3). I leave it.
  - Neither the timpani nor the low brass covers the strings or the melody.
- **Dynamic mapping:**
  - pp accompaniment reads -14 to -19 dB K in every family (winds -14.4 to -19.4, Horns 3-4 -18.1 to -19.6, strings -14.5 to -18.1, timpani -17.7).
  - p solos sit together: Flute 1 -6.9, Oboe 1 -8.4, cor anglais -8.6, bass clarinet -6.6, Horn 1 -7.9, solo violin -7.3.
  - The violas run 2-6 dB under Violins I/II and the celli at mf-ff, as a real section does.
- **Divisi against full sections (K):**
  - Violins II div -1.4 against Violins II (bars 37-40).
  - Violas div against Violas: -1.1 (bars 23-26), +3.4 (bars 27-29), -0.2 / -0.5 (coda); bar 81 -3.3 since the c46 -2.5 gain.
  - Vc div (4 soli) 0.0 against the basses (bars 83-86).
  - Basses 4 soli -3.2 against the celli (bars 65-66).
  - Horns 1-2 a2 +0.4 against Horn 3 (bars 79-81).
  - All plausible for inner voices.
- **Harp:** the f arpeggio at 261 (bar 78) is briefly the loudest stem (+10.1 against Violins I +6.7). It is a pluck on the printed f before the bar 79 ff, so I leave it.

**Do not touch:**
- the c46 solo roles (Bassoon 1 [231.5, 237, -4.5, 1.5], the cor anglais rows, Violoncellos [152, 164, -3, 0.5], Double basses [139.9, 146, -3]) and the Violas div gain 2.98;
- the c46 brass bells and gains;
- the basses' f/ff trims 2.5/4.0 and the bass clarinet's f/ff -1/-3 (see above);
- the c37 bars 61-62 brass +3 and the c36 Horn 1 bar 61 front shape;
- the timpani roll shapes and linear timpani lanes;
- Trombone 1's c46 213 rows and CC7 127;
- the return levels and IR envelope (fx faders, hp 160);
- the solo violin CC1 72 with gain +0.4;
- the velocity sensitivity at 0 (manual p.150).

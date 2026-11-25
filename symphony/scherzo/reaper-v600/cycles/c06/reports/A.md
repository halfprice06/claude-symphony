# Cycle 06, critic A: articulation and phrasing (render c05)

Render under review: `cycles/c05/render/` (stems and master), made from `cycles/c05/build_render/parts.json`. Times are seconds of score time on that parts.json's tempo map. Unless noted, levels are plain RMS (10 ms windows for dips, 50 ms for note levels). Perceived attacks are `tools/pcx.py attack_pcx` values (pc, seconds after the score onset). Bar b starts at qn 3(b-1).

## Manual notes (A7: PDF pages 160-162 and 188-190 of the May 2021 HO manual, read in full; pages 162 and 188 viewed as images; Opus Software manual p.85-87 for the trigger behaviour; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| KS Masters load with the Keyswitch trigger option; a keyswitch note outside the playable range selects the row (p.160-161). Behaviour is Exclusive by default: the last trigger received deactivates every other row (Opus p.86-87) | Every track's `ks` lane in parts.json | Yes (read). `ks_clash` is empty on all 31 tracks. The closest keyswitches sit 0.02 qn before their note (4.5-5.3 ms): 3 on Violins I, 2 on Violins II, 9 on the violas, 5 on the celli. Every other keyswitch is earlier. Keyswitches often change while the previous note still sounds (Violins I 89 times, celli 83). The new row applies only to later note-ons (inferred from p.161 and Opus p.86). No cut notes were found at the points I checked. |
| Trigger by controller range (p.162) or program change (p.161) | Not used | n/a. Keyswitches cover every row change. |
| Velocity-range trigger: a short row limited to velocity 110-127 layered on a sustain gives an accent on hard notes (p.162, p.189-190) | The 321 accents | Not followed, by design. A KS Master plays one row at a time (Exclusive), so a layered short would need a second instance, which the 45 GB cap rules out. Dan's rule (weight, not bite) also argues against a staccato front. The mockup uses `GENTLE_ACCENT` swells and the "Sus Marc LITE" row instead. Finding 3 uses the Marc LITE row, which is already loaded, for the hemiola. |
| Voice limit per instrument; a note with several mics or articulations uses several voices; raise the limit if voices drop (p.188) | The "non div." double stops (bars 72, 105-120, 300, 305-320, 339) | Yes (read). `voiceLimit` is 350 in the Violas KS Master and the 1st Violins KS Master `.oib` (decompressed JSON). A two-note chord with its release trails is far below that, so no voices drop. |
| Group, Octave and Key Range zone options (p.188-189) | Not used | n/a. Key Range could split one instance into two ranges (a divisi without a second instance), but no passage needs it now. |

MANUAL-GAPS items that bear on the findings: #10 / #17 (horn "Port Lng", 775 regions) for finding 5; #3 (spiccato) as an alternative in finding 1.

## Findings, ranked by what a listener would gain

### 1. Theme A's second and fourth phrases blur the repeated eighths: the "Stac RRx14" row added in c04 for sample variety rings through the second eighth (measured)

**Where.** Violins I, theme A, p/mp leggiero. The c04 C #1 spans put phrases 2 and 4 of each statement on "Stac RRx14": bars 17-20 and 25-28 (qn 48-60, 72-84), and in the reprise bars 257-260 and 265-268 (768-780, 792-804). The repeated-eighth pairs in those spans are at 49, 55, 73, 79, 769, 775, 793 and 799.

**What is wrong.** This is Dan's S1 in the most exposed statement of the theme. On Staccatissimo RRx9 the first eighth has decayed about 6-9 dB by the time the second starts, 0.114 s later. On Stac RRx14 it stays within 1-3 dB of its peak through the second onset. Note lengths and leads are the same on both rows (0.057 s played, 57 ms gap, 45 ms lead). The difference is the sample, not the release: the row's AHDSR release is 333 ms against 524 ms on Staccatissimo RRx9 (read from the `.oib`).

**Evidence (measured; dip = peak in 0-80 ms after the second onset minus the minimum in -60..+30 ms).**

| statement | Staccatissimo RRx9 pairs: stem / master | Stac RRx14 pairs: stem / master |
|---|---|---|
| bars 13-28 | 37: 8.0 / 4.0; 43: 7.8 / 4.1; 64: 6.7 / 3.1 | 49: 4.7 / 2.9; 55: 2.0 / 1.5; 73: 4.8 / 1.8; 79: 2.3 / 1.8 |
| bars 253-268 | 757: 8.5 / 5.7; 763: 8.0 / 5.8; 784: 6.7 / 4.8 | 769: 4.5 / 3.7; 775: 2.3 / 2.9; 793: 5.1 / 3.1; 799: 2.3 / 1.8 |

- Same pitch, different row: D sharp 5 dips 6.7 dB on Staccatissimo (64) and 2.0-2.3 dB on Stac RRx14 (55, 79, 775, 799).
- Over the whole first statement the master's pair dips have a median of 2.9 dB, with 4 of 7 under 3 dB. Every later statement has a median of 3.7-5.0 dB.

**Fix.** In `build/score_config.py`, in the C #1 block (the `ART_SPANS["Violins I"]` line with spans (48, 60), (72, 84), (768, 780), (792, 804)), split each span so the two repeated eighths keep "Staccatissimo RRx9": (48, 49), (50, 55), (56, 60), (72, 73), (74, 79), (80, 84), (768, 769), (770, 775), (776, 780), (792, 793), (794, 799), (800, 804). The other notes of those phrases keep the alternate samples. Check in parts.json that only the 16 eighths change row.
- **Targets:** stem dips at least 6 dB and master dips at least 3.5 dB at the eight pairs. The heads' cross-correlation (C #1's measure) should stay under 0.98.
- **If the round robin repeats audibly on the pairs:** try MANUAL-GAPS #3 ("Spiccato RRx9") on those eighths, but count its regions first.

### 2. The violas' slurred tenuto pairs in bars 210-224 are played weak-strong: the first note sits on Leg Slur MAX's quiet first-note layer and the second is a Sus MAX stroke (measured)

**Where.** Violas and Violas div, the `_PORT_PAIRS` pairs at 628/629, 637/638, 640/641 ... 670/671 (bars 210-224, quarter 228). Since c05, `STR_REP_NEW_BOW["portato"]` puts the second note on a fresh Sus MAX stroke. The first note starts after a gap (no legato predecessor; for example Violas div at 630.548, 0.548 qn after the previous note-off) on Leg Slur MAX at v73.

**What is wrong.** The c05 actor read this as a missing dip ("div portato flat", 0.7 dB). Measured note by note, the real problem is a step: the second note comes in 4-12 dB louder than the first. A louré pair should lean on the first note, or at least keep both equal. Here the pair sounds like a pickup into an accent, thirteen times in the trio's climax.

**Evidence (measured; body = level 0.05 s after the onset to the note-off, or 0.05-0.25 s for the second note).**
- **Violas.** Second minus first: +5.6, +5.8, +8.4, +5.5, +4.5, +5.4, +7.7, +2.6, +1.6, (-6.3 at 659, a pitch change), +5.5, +8.3, -0.6, +0.6 dB. Median +5.4 over 14 pairs.
- **Violas div.** Every E4 pair steps up +4.4..+11.7 dB: 625, 628, 649, 652, 655, 658 and 661 (dips 1.2-4.0). The other pairs (631, 640, 643, 646, 664; D sharp 4 and F sharp 4) are level within 0..+0.9 dB and dip 6.7-7.0 dB, which is the intended result.
- **Cause (read).** At one CC11 the string Sus rows sit over the Leg rows (score_to_parts.py PICKUP_SUS comment, Movement I c16). A disconnected Leg Slur note plays the row's quiet first-note plateau.

**Fix.** Play the first note of each pair on Sus MAX as well, so both notes use the same row and layer and are separated only by the existing gap and notch.
- **How.** `ART_SPANS["Violas"]` and `ART_SPANS["Violas div"]`, one tight span per first note, {"from": q - 0.05, "to": q + 0.05, "art": "Sus MAX"}, at q = 625 (div only), 628, 631 (div), 637, 640, 643, 646, 649, 652, 655, 658, 661, 664, 667, 670. Sus MAX is loaded on both tracks. Skip any first note that is a legato target (joined from the note before); check the `ks` lane in parts.json.
- **Fallback (level only):** `build/note_trims.json` Violas +5 dB and Violas div +6 dB on the E4 first notes. `LEG_JOIN_TRIM_HOLD["string"]` is already set.
- **Target:** second minus first within ±2 dB, and a dip of 3-6 dB at each second note, on both tracks.

### 3. The hemiola still swells after each beat on Violins I: use the loaded "Sus Marc LITE" row for its strokes (measured; c05 partial)

**Where.** Bars 101-104 (qn 300-310) and 301-304 (902-910), the accented half notes of "ritmo di quattro battute". Violins I plays them as fresh Sus MAX strokes (`DOWNBOW_STROKE_AT`), with c05's -3 dB body cuts and leads.

**What is wrong.** After c05, the master's front (0-0.1 s) minus body (0.2-0.4 s) is -2.6, -5.0, -1.1, -1.6, +1.2, -0.7 dB at 300-310 and -2.0, -1.1, -2.0, -1.5, -0.4 dB at 902-910. The master peak falls 135-415 ms after the beat. Violins I, the top line, is the weakest stem: front minus body -10.0 / -3.2 / -1.1 / -0.5 / -1.5 / -1.3 dB at 300-310 and -0.5 / -5.4 / -3.9 / -3.8 / -2.9 dB at 902-910, with peaks 110-375 ms late. At f the Sus MAX sample is still rising when the next half note arrives, so a body cut can only flatten the swell. It cannot make a front. The pattern is the same one c01-c02 measured on the theme heads, which the Marc LITE row fixed (+2.0..+3.7 dB front over the following note, with a per-note level step).

**Fix.** `ART_SPANS["Violins I"]` += {"from": 299.5, "to": 311.0, "art": "Sus Marc LITE"} and {"from": 901.5, "to": 911.0, "art": "Sus Marc LITE"}, ahead of the `_HEM` `DOWNBOW_STROKE_AT` entries so they take the row.
- **Velocity:** about v80 (`VEL_SET`). c02 measured +4..+15 dB over neighbours at v70-86 before the level steps.
- **Level:** one level step per note from the moved onset (start at -6 dB and refit with `stem_fix.py`, as for the heads in c02). Keep the c05 body cuts in `accent_bodies.json` only if the step leaves the body above the next front.
- **Memory:** the row is already loaded on Violins I, and the release cap list already covers "Sus Marc LITE". The other sections do not have it loaded (8.5 thousand regions each), so they stay as they are this cycle.
- **Target:** Violins I front minus body at least +1 dB at 9 of 11 onsets; the master peak within +0.15 s of the beat at least at 300-310; 2-5 kHz front no more than about +3 dB over the body (Dan: weight, not bite).

### 4. Phrase heads on a legato row after a rest start 5-9 dB under the notes that follow, at flat CC11 (measured; cause inferred)

**Where and evidence.** Body of the first note of a slur after a rest against the median of the next joined notes. CC11 is flat and no hairpin is printed at these points; the c05 render has no vol_db step at any head.
- **Clarinet 2, 834 (bar 279), v41, Leg Slur Rep.** Head -8.7 dB against its next notes, and -9.5 dB under the median of its line 834-846.
- **Violas, 828 (bar 277, the reprise's second idea at p).** Head -7.0 dB.
- **Violoncellos, 828, E2.** Head -7.7 dB under the median of 828-840 (CC11 42-49; the -3 dB role from 828 applies to the whole line).
- **Violas, 159 (bar 54), v91.** Head -5.8 dB.
- **Celli trio tune, 504 (bar 169, mp, "arco, espress."), v63.** The head rises for 0.27 s from its note-on (0.22 s early) before reaching its body at about +0.05 s. That rise is why pcx reads it at +0.155 s. c05's extra 0.10 s lead moved the note-on earlier but not the body (pc +0.112 -> +0.155 s). The next transition, into A3 at 506, peaks 8-9 dB over the head.
- **Context.** Over 146 legato phrase heads in the piece, the heads where the score asks for a crescendo (Horn 1 582, Oboe 1 372 / 558 / 840, Violins I 576) are expected to be soft and are not counted here.
- **Cause (inferred).** The Leg rows play a slow first-note sustain layer after a rest (Movement I c16-c17: 4-18 dB under the target). The string LegatoSpeed script maps velocity 30-127 to a start offset of 0-100 ms (DIGEST §legato, from the patch; manual p.144). At v41-63 the head starts at almost the beginning of its slow attack.

**Fix.** Level, as Movement I c17 found (a lead cannot raise the plateau).
- **`build/note_trims.json`:** Clarinet 2 {834: +6}, Violas {828: +4.5, 159: +4}, Violoncellos {828: +5, 504: +5}. That is about two thirds of each deficit. `LEG_JOIN_TRIM_HOLD` (string, wind) already carries a positive trim into the join.
- **`build/entry_leads.json`:** remove the celli 504 extra (0.10 s), since it made the perceived attack later.
- **Optional test on the celli 504 head only:** `VEL_SET` v95, so that LegatoSpeed skips more of the slow attack. Measure whether its pc moves before using velocity anywhere else.
- **Targets:** head body within -2..+1 dB of the next notes; celli 504 pc within ±0.05 s.

### 5. Horn 1's repeated tenuto dotted halves in the trio's return still have holes 115-170 ms long (measured; c05 open item)

**Where.** Horn 1, bars 210-222 (qn 627-666). Repeated tenuto dotted halves: B4 627-630-633, C sharp 5 636-639, 648-651 and 660-663. All play on Sus MAX, re-tongued with c05's Horn 1 values (gap 0.035 s, 4 CC fall, 0.09 s lead).

**Evidence (measured on the stem; dip = level 0.12-0.35 s before the onset minus the minimum around the re-attack).**

| onset | 630 | 633 | 639 | 651 | 663 |
|---|---|---|---|---|---|
| dip | 10.2 dB | 8.9 dB | 2.9 dB | 4.8 dB | 8.0 dB |
| time more than 3 dB under the body | 145 ms | 170 ms | 0 ms | 115 ms | 120 ms |

The minima fall at -15..+10 ms around the beat at 630 / 633 / 663. A shorter gap cannot close the hole further: the Sus MAX sample decays through the dotted half and the new attack rises slowly (c04 LEARNINGS). At quarter 228, 0.15 s is more than half a beat of near-silence in a sustained horn line.

**Fix (MANUAL-GAPS #10 / #17).** `ART_SPANS["Horn 1"]` += {"from": 626.5, "to": 666.0, "art": "Port Lng", "mark": "tenuto"}. The 1FH KS Master row "Port Lng" has 775 regions, about 0.03 GB, within the memory cap. The row is recorded for exactly this tongued, connected repeat.
- Let the re-tongue rule keep only its lead on these notes (`WIND_REP_RETONGUE_BY["Horn 1"]` gap 0.02 s, no CC fall), because the row has its own articulation.
- Set the Port Lng velocity by layer, as the `_TSTAC` table does, about v70-80 at f.
- **Target:** dips 3-6 dB, under 80 ms below -3 dB, and the level within ±2 dB of the Sus MAX notes around them.

### 6. Clarinet 1's B4 pitch trim (+7.5 dB) now overshoots: the B4 bumps 5-7 dB out of the line wherever it falls between lower notes (measured; shared with lens B)

**Where.** Clarinet 1, every B4 on Leg Slur / Leg Slur Rep (`pitch_trims.json` "71": 7.5 since c04 C #4). Worst at 142 and 159 (bars 48 and 54, the second idea), 362 (bar 121, the sub. p second idea), 459 (bar 154, the trio tune's second bar), 591 (bar 198) and 830 (bar 277).

**Evidence (measured).** B4 body minus the mean of its two neighbours, over 21 B4s in joined lines: median +2.0 dB, with +7.0 / +5.3 / +5.3 / +5.7 / +5.5 / +5.7 dB at 142 / 159 / 362 / 459 / 591 / 830. In the sub. p phrase at 360-366 (CC11 flat at 46) the B4 sits 8 dB over the G4 before it. Every printed shape there is flat (p, espress.), so the sub. p line starts with a bump on its second note. Critic B noted the same B4 at 459 in c05 (4-7 dB hot).

**Fix.** `build/pitch_trims.json`, Clarinet 1 "71": 7.5 -> 4.5. That moves the median to about -1 dB and the worst cases to about +2.5 dB. Re-measure B4 minus neighbours on the next render; target -1..+2 dB.

## Also measured (not ranked)

- **S2 staccato alignment.** Section pc medians of the staccato and pizzicato theme heads all sit within ±25 ms of the beat:
  - counterstatement (84-132): -5..+17 ms, basses pizz. +24;
  - fugato (168-216): -8..+11;
  - reprise (756-828): -10..+20;
  - development (864-900): -9..+11;
  - coda (972-1008): Trumpet 1 -23, violas -21, Violins II -15, cor anglais -29, basses +20.
  - No action.
- **S1 master pair dips by statement** (median): counterstatement 3.9 dB, fugato 5.0, tutti 105-120 4.4, reprise 4.8, development 3.9, tutti 305-320 3.7, coda 4.1. Only the first statement (2.9) fails, which is finding 1.
- **Portamento at 640 (`PORT_TARGETS`, unmeasured since c01).** On the Leg Port MAX row the F sharp 6 band reaches its level +0.03 s after the score onset. The F 6 band rises from -0.12 s, so the glide is audible mainly over its last semitone, about 0.1-0.15 s long. Acceptable for "port."; no change.
- **Horn 1 re-tongue timing** (c05 side effect: every Horn 1 re-tongue now 0.04 s earlier). Against the other horns at the same onsets, over 31 pairs, Horn 1's pc runs a median 22 ms earlier. Same-pitch pc readings scatter ±150 ms, so this is not actionable on its own.
- **A7, rows and voices.** No chord is sent to a legato row on any track (no two simultaneous notes on a Leg row). The voice limit is 350.

## Do not touch

- The "Staccatissimo RRx9" theme rows and the Marc LITE heads with their level steps.
- The wind "Stac DblTng RRx9" rows and their leads; Trumpet 1's StacSs row.
- The pizzicato leads, which are on the beat.
- Violins II's con sord. `GROUP_LEAD_AT` (heads -0.003 / followers +0.025 s).
- The celli 756 and basses 840 entry leads (on time).
- `PORT_TARGETS` 640; the harp setup; the CC70 / CC15 lanes; the re-bow fills; subitos in CC11.
- The tutti and coda staccatissimo rows (their pair dips are 3.7-5.0 dB on the master).
- `ir_setup` 0.7 and the release caps.

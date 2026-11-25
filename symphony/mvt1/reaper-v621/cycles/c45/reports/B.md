# Critic B, cycle 45 (render c44): balance and levels

## Manual notes (second reading of the c39 B row: May 2021 HO manual PDF pages 49-52, 202-204 and 208, read again in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items that touch these pages come first, then the c39 B notes checked against the c44 render, then what the first reading missed.

| Source | What it says | Where it applies here | Followed in c44? |
|---|---|---|---|
| MANUAL-GAPS #4 (with p.50-51) | Each mic position can go to its own output and its own reverb send. Mid mics give "definition without the sound of close proximity". | Winds, horns and trumpets on Close + Main, with depth set by per-mic sends. | **Still open.** It is planned for this Blend cycle (lens C). None of the findings below comes from a mic choice: all four are envelope or EQ data (measured). |
| MANUAL-GAPS #7 (p.89-90) | Half-section divisi patches. | Soft div. passages. | **Still open** (c44 A #4 was deferred to c45). Not a balance finding this cycle. |
| MANUAL-GAPS #13 | The bass trombone's three lowest notes are transposed tenor samples. | Bars 113-115. | **Still open**, low priority. |
| p.49 | "Load with Effects off" so the reverb can be replaced in the DAW. | One shared hall replaces every patch's own reverb. | **Followed.** c44 halved the return (fx_volume 0.095) and added the low cut and the IR envelope, all in the same shared insert. One room is kept (measured: every family's level against the strings moved by 0.8 dB or less, see Checks). |
| p.50-51 | Route each mic to its own channel and send "varying amounts" of each mic to one reverb bus. | Per-mic pre-fader sends inside each instance (KIT §12). | **Equivalent, as in c39.** New note: the high-send tracks (trumpets 0.65, horns 0.5, low brass, timpani and percussion 0.45) lost only 0.2-0.8 dB against the strings in loud passages (measured), so no send needs to change (S4 forbids raising them in any case). |
| p.52 | Multi-timbral instances. | Not used. | Not applicable (unchanged). |
| p.202 | De-Esser (3-12 kHz) and Level Amp. | c39's only candidate was Trumpet 1's 5-12 kHz at 636-644. | **Not needed.** Trumpet 1's 5-12 kHz is now -8.2 / -7.9 dB re master at 636-640 / 640-644 (c39: -4.5 / -4.1), thanks to the c39-c40 shelves (measured). |
| p.203 | Limiter and Limiting Amp. | Delivery limiting happens outside Opus. | **Followed.** `deliver_master.py` limits about 0.4 dB in c44 (c38: 0.7). |
| p.204 | SSL Bus Compressor and Channel Strip. | Not used; EQ is done in REAPER. | Consistent (unchanged). A compressor would make the balance depend on level. |
| p.208 | Transient Shaper, whose Invert control softens attacks ("good for getting body"). | Felt timpani strokes, now that the hall is drier. | **Not needed by level.** Stroke peak minus the stroke's own ring at 0.25-0.45 s went from +11.0 to +13.1 dB, because the ring has less hall. The stroke peak re master did not change (-5.8 -> -5.5 dB median over 54 strokes at f or louder), so the strokes are drier, not louder (measured). If Dan hears the strokes as hard, Invert is the in-Opus tool for it (inferred). |

DIGEST 4.4 already records the p.208 correction from c39. No MANUAL-GAPS item changes state this cycle.

## Method

- **Data.**
  - Final c44 stems (40, after the stem fixes and the second pass), against the final c43 stems.
  - Build data: `build/` at the end of c44, `cycles/c44/before/` (c43 final), `cycles/c44/rendered_build_pass2/parts.json`.
- **Frames.**
  - 2048-point FFT, 10 ms hop, stereo power, K and A weighting, 1/3-octave bands.
  - "re M" means stem minus master over the same window.
  - The f62 aliases are summed into Violins I / II, Cello solo into Violoncellos, and the stac aliases into their source tracks.
- **Reference.** The Dvořák MP3, decoded and measured the same way (loudest 10% / 25% of 0.4 s windows).
- **Simulations.** Level shapes are applied to the frame powers and the master is rebuilt from them. The EQ in finding 2 is approximated with log-frequency bell curves on the 1/3-octave band powers.
- **Scratch.** Scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c45-B/` and are deleted at the end.

## Findings, ranked by what a listener would gain

### 1. Two new re-bow fill lists hold their last value for 26-29 bars: Violas +4.1 dB over bars 145-172, Violins II -2.0 dB over bars 145-175 (measured; fix simulated)

**Cause (read and measured).**
- c44's soft re-bows (`STR_REP_NEW_BOW`) added re-bow points at Violas / Violins II qn 576. `fit_rebows.py` fitted a list for each, in `build/rebow_fills.json` key "576".
- The lists end at +1.48 s on +4.1 dB (Violas) and -2.0 dB (Violins II).
- `score_to_parts.py` (REBOW_FILLS loop, about line 4561) holds a list's last value "until the next list starts". The next lists are at 688 (Violas) and 699.26 (Violins II). The note these lists belong to ends at 581.90 (parts.json `rebows` row `[576.0, 581.9031, ...]`).
- A third list, Violoncellos "172" (-0.5 dB), holds from its note end at 177.59 to 289.1. It is small, but it is the same fault.
- `close_fills44.py` closed only the lists that preceded removed points. No other list in `rebow_fills.json` holds past the end of its note (scanned all string tracks).

**Evidence (measured).**
- *Envelope.* c44 build minus c43 final `vol_db`: Violas +4.1 dB from 576.25 to 686.5; Violins II -2.0 dB from 578.5 to 699.0.
- *Render.* Violas +2.7..+4.4 dB in every bar from 145 to 172. Violins II -1.6..-3.6 dB (mostly -2.0..-2.5) in every bar from 145 to 175.
- *Bars 147-155 (J).* The tune is played in octaves by Horn 1, violas and celli, against Violins II sul tasto pp and basses pizz.
  - Violas minus celli over bars 147-150: +0.5 dB (c43) -> +4.3 dB A.
  - The violas are the loudest stem of the passage (-2.3 dB A re M at 147-150).
  - Horn 1 re M: -7.6 -> -9.7 dB A.
- *Bars 156-170 (climax and coda).* Violas +3.7..+4.2 dB re M against c43.
  - Violins I minus Violins II at 156-166: +0.9..+1.8 -> +4.7..+5.3 dB A.
  - The melody's middle octave at 636-640 (Trumpet 1 + Violins II): -7.3 -> -8.8 dB A re M.

**Fix (level only; `stem_fix.py`, then `--midi-only`).**
- *Generic, in `score_to_parts.py`.* In the REBOW_FILLS loop, end each list at the end of the note it belongs to: the `rebows` row's second element. When the next list starts later than that, hold the last value to the note end, then reach 0 dB 0.12 s later.
- *Data alternative.* Append two points to each of the three lists in `build/rebow_fills.json`:
  - Violas "576" and Violins II "576": `[2.88, last value], [3.0, 0.0]` (the note ends 2.93 s after qn 576);
  - Violoncellos "172": `[2.62, -0.5], [2.74, 0.0]` (2.67 s).

**Simulated (holds removed).**
- Violas minus celli 147-150: +4.3 -> +0.2 dB A.
- Horn 1 re M 147-150: -9.7 -> -7.8.
- Violins I minus Violins II 156-166: +4.7..+5.3 -> +2.7..+3.3.
- Middle octave 636-640: -8.8 -> -7.9.
- Master -0.2 dB at 160-161 and 167-170. The climax order is unchanged.

**Smaller fill effect nearby.** The soft re-bows at Violas 292 / 296 (bars 74-75, under the Flute 1 espr. solo) carry fitted fills that peak at +9.2 / +10.0 dB, the fitter's clamp.
- The violas there are +3..+6 dB A against c43, and now 1-4 dB over Violins II.
- The flute still leads by 9.3 dB (c43: 10.6).
- If the actor refits the fills, cap these two lists at +5 dB (inferred to be enough; re-measure).

### 2. The f tutti passages outside the climax spans lost the celli and basses' low-mid bells: the bass line fell 1.3-3.6 dB and the master's 100-250 Hz 2-4.3 dB there (measured; EQ fix approximated)

**Cause (read).**
- c44 C #4 moved the celli's static bells (170 Hz +3 / 1.5 oct and 125 Hz +3 / 1 oct) and the basses' 180 Hz +4 bell into `loud_eq` specs with the old climax points: bars 24-32, 82-83, 115-124, 130-134, 138-142, 157-162 and 167-170.
- C aimed at the soft passages. The printed f / ff tutti bars that fall outside those spans lost the bells too, and nothing gave the level back: the soft trims reach 0 at f.

**Evidence: f / ff bars with the celli playing (measured).**
- **Inside the spans** (33 bars, medians): celli -0.3 dB, basses -1.5, master 100-250 Hz -1.4, master K -0.5.
- **Outside the spans** (39 bars, medians): celli -1.3 dB, basses -2.3, master 100-250 Hz -2.4, master K -0.6.

Per passage, c43 -> c44:

| Passage | Celli + basses re M (K) | Master 100-250 re 250-2k Hz (dB) |
|---|---|---|
| Bars 69-72 (D, f tutti; descending half-note bass in celli, basses, Bn 2, Cbn) | -9.8 -> -13.4 | -6.8 -> -11.1 |
| Bars 136-137 | -8.7 -> -10.9 | -8.6 -> -12.2 |
| Letter F (98-102) | -11.9 -> -13.5 | -13.6 -> -15.6 |
| Bars 33, 41, 143 | celli -3.1..-4.2 dB per bar | master 100-250 Hz -1.9..-4.2 dB per bar |
| *Dvořák, loudest 25% of windows* | | *-5.1* |

- In bars 69-72 the celli lost 3.8 / 3.7 / 6.4 / 7.0 dB per bar.

**Is the tutti bass thin? (measured)** In the loudest 10% of windows:
- 100-200 Hz share: -9.9 -> -10.5 dB; the Dvořák has -6.7.
- 125 Hz third-octave: -6.0 -> -7.3 dB re 1 kHz; the Dvořák has -3.0.
- 40-100 Hz share: -16.0 -> -18.1 dB, still 1.9 dB over the Dvořák (-20.0).

So the loud passages are short of low-mid, not of sub-bass. The largest new loss is in the f passages outside the spans. The KIT warns against tuning the low end to the lossy Dvořák alone, but in these passages c43 itself had 2-4 dB more than c44 now has.

**Fix (`build/mix.json`; EQ, so a `--mix-only` build and the next render; not a stem fix).** Add these spans to Violoncellos `loud_eq[2].points` (the 170 / 125 Hz bells) and Double basses `loud_eq[3].points` (the 180 Hz bell). Leave the 150 / 160 Hz climax bells (`loud_eq[0]`) as they are.
- **Bar 33:** replace `[127, 1], [128, 0]` with `[131.75, 1], [132, 0]`.
- **Bar 41:** add `[159.5, 0], [160, 1], [163.75, 1], [164, 0]`. It starts at 160 so that bar 40 (finding 4) gains nothing.
- **Bars 69-72:** add `[271, 0], [272, 1], [287.75, 1], [288, 0]`.
- **Letter F to bar 104:** add `[387, 0], [388, 1], [415.75, 1], [416, 0]`.
- **Bars 136-137 and 143:** replace `[535, 1], [536, 0], [548, 0], [550, 1], [567, 1], [568, 0]` with `[535, 1], [536, 0], [539, 0], [540, 1], [571.75, 1], [572, 0]`.
- **Leave out** bars 80-81 and 91-97. The approximation puts them past c43 (-2.8 against -3.5 at 80-81, and -4.8 against -5.7 at 91-97).

**Approximated** (master 100-250 Hz re 250-2k Hz):
- 69-72: -11.1 -> -8.9;
- 136-137: -12.2 -> -8.2;
- letter F: -15.6 -> -13.8;
- 33 / 143: back to c43.

**Optional, to be agreed with lens C.** The climax spans themselves lost 0.7-1.7 dB of low-mid to the hall's low cut. +1.5 dB on the celli's 150 Hz climax bell (`loud_eq[0]`, 6 -> 7.5) would recover that without adding sub-bass (inferred; measure first).

### 3. Bars 127-128: the pp timpani roll now covers the celli's repeated pp quarters, which sit on the same pitch (G2) (measured; fix simulated; Dan's priority)

**Score (p.12).** Under the Clarinet 1 solo, the celli play repeated pp G2 quarters, then eighths, with a crescendo to mf at bar 129. The timpani hold a pp G2 roll with the same crescendo, and the basses and Horn 4 hold pp notes.

**Evidence (measured).**
- *The celli lost their bodies.* Note bodies at 504-512 are 2.6-10.4 dB under c43. The bar-127 quarters lost -6.3 / -2.9 / -10.4 / -4.9 dB and the bar-128 eighths -10.2..-2.6 dB. These soft strokes lost their overlapping release tails to the 150 ms cap.
- *K re M, c43 -> c44, per qn at 506-511.*
  - Celli: -6.2 / -8.9 / -10.0 / -12.2 / -15.6 / -14.6 -> -13.2 / -11.3 / -18.4 / -15.4 / -18.0 / -16.9.
  - Timpani: -18.5 / -12.8 / -16.4 / -13.1 / -15.6 / -12.9 -> -16.2 / -10.9 / -16.6 / -13.9 / -16.1 / -12.8.
- *Rank.* The roll is now the loudest accompanying part at the same printed pp, second only to the solo.
- *In the 79-125 Hz band* (the shared pitch), celli minus timpani: +18.5 / +9.2 / +13.6 / +7.4 / +4.3 / +4.9 -> +8.0 / +4.1 / +2.6 / +3.4 / +2.7 / +1.1 dB.
- *Separation.* The master's pulse depth at the celli's note rate in that band fell from 4.0-4.3 to 2.6-2.9 dB at 506-508.
- *Rule 5.* The roll's growth is printed, but it no longer sits under the texture.

**Fix (level only, `build/score_config.py`; stem fix).**
```
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(503.75, 0.0), (503.95, 3.5), (511.75, 3.5), (512.25, 0.0)]]
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES.get("Timpani", []) + [[(503.5, 0.0), (504.0, -2.0), (512.0, -2.0), (514.0, 0.0)]]
```

**Simulated.**
- Celli minus timpani in 79-125 Hz at 506-511: +13.5 / +9.6 / +8.1 / +8.9 / +8.2 / +6.5 dB, back near c43.
- Celli K re M: -9.9 / -8.0 / -14.9 / -12.0 / -14.5 / -13.5.
- The clarinet's margin is unchanged (Clarinet 1 re M -0.3..-2.1).
- The roll still grows by its printed crescendo from bar 129 on.

**Other long rolls: no cover (measured, c44 K re M, rank among stems).**
- G pedal 464-500: -10.6..-18.5, rank 4-23 (rank 4 only in the bars 124-125 decrescendo). In 63-250 Hz it stays under the loudest bass part, except during that decrescendo (+0.3..+3.0 dB at 494-498).
- 628-642: -12.5..-17.0, rank 5-15.
- 662-679: -13.1..-16.3, rank 7-17.
- 156-172: -13.8..-18.6, rank 5-14.
- 316-324 (p <): -8.2..-17.4, rank 4-9.
- Final ppp roll: -12.8..-16.6, rank 7-9.
- Bar 144 (mp > pp): rank 2 at 572-574 only (-8.6, 1.3 dB over the celli's mp), then -11..-21. It settles, so no change.

### 4. Bars 39-40: the c44 stroke trims on celli 152 (+5.0) and 156 (+5.5) make the celli's held note the loudest stem by up to 5.8 dB and take 2.7 dB off the step into the bar-41 sf (measured; fix simulated)

**Score (p.5).** The celli repeat a held whole note each bar, f with a crescendo. Violins I and the high winds have the run up to the sf tutti at bar 41, and Horns 3-4 a2 play f.

**Evidence (A, per qn, 152-160).**
- *Celli re M, 153-159:* -9.4 / -11.5 / -11.0 / -9.0 / -8.4 / -9.6 / -13.3 (c43) -> -6.6 / -6.6 / -6.2 / -8.6 / -4.2 / -3.6 / -4.9 (c44).
- *Celli minus the loudest other stem:* -0.9 / -0.4 / +4.9 / +5.8 / +3.0 dB at 155-159 (c43: -6.5 / -1.2 / -0.3 / -2.0 / -7.2).
- *Violins I run:* 5-7 dB under the celli at 157-159.
- *Master:* +2.7 dB over c43 at 158-160. The step from bar 40 into the sf of bar 41 fell from +6.2 to +3.5 dB.
- *The strokes themselves are not loud at their fronts.* 156's front is 12 dB under the end of the note before. The excess is the fresh Sus MAX bloom over the rest of the bar, lifted by the trim.

**Fix (level only, keeping the strokes' fronts).**
```
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(152.75, 0.0), (153.5, -2.0), (155.75, -2.0), (156.25, 0.0), (156.5, 0.0), (157.0, -3.0), (157.5, -5.0), (159.75, -5.0), (160.0, 0.0)]]
```
Alternatively, lower `note_trims.json` Violoncellos 152 to +3.0 and 156 to +1.0. That also lowers the fronts.

**Simulated.**
- Celli minus the loudest other stem at 155-159: -2.9 / -1.6 / +0.4 / +0.8 / -1.3 dB.
- Step into bar 41: +4.9 dB.
- Master bar 40 within -1.8..+0.9 dB of c43.

**The other STR_REP_NEW_BOW strokes (the coordinator's question; measured).** Front = 0.03-0.20 s and body = 0.20-0.60 s after the moved onset, each against the last 0.25 s of the note before.
- **None sits over its neighbours,** except two cases:
  - the Violins I portato tenutos 60 / 140 / 572: bodies +4.2..+6.3 dB over the end of the 0.11 s eighth before. This is lens A's open item, and A's 2 dB target is not met.
  - Violas 500, a new p after a decrescendo: front +5.8, body +2.5. In context it is a smooth continuation: -11.6 / -10.4 / -9.8 dB A re M per half qn, level with c43 after its first half beat. No change.
- **The loud cello strokes enter low.** Strokes 47, 84, 156, 374, 448, 456 and 668 enter 6-12 dB under the end of the note before, and their bodies stay 1.4-5 dB under it. This is the slow Sus MAX attack: an articulation and timing matter. The largest level shortfalls without a trim are celli 374 (-5.1) and 668 (-3.9). +2.5 dB trims would even them, but the gain is small (inferred).

## Checks with no change proposed (measured on the final c44 stems)

**Family levels after the drier hall.** Change c43 -> c44 relative to the strings, on loud beats (master top quarter):

| Family | Change (dB) |
|---|---|
| Horns | -0.2 |
| Trumpets | -0.6 |
| Trombones and tuba | -0.3 |
| Timpani | -0.8 |
| Woodwinds | 0.0 |
| Violoncellos | -0.3 |
| Double basses | -1.4 |

- **The brass is not further forward by level.** The c44 cut-off measure still shows more tail on the brass than on the strings (drop at 0.15 s after 679: brass -10.1, strings -8.8 dB), so the depth order holds. How dry the brass sounds is a blend question for lens C.
- **The timpani strokes are no louder.** Peak re master: -5.8 -> -5.5 dB median.

**Dynamic mapping.** Method: on beats where at least four tracks share one flat printed dynamic, each track's A level minus the beat median.
- Every family is within ±3 dB at every printed dynamic from pp to ff: winds -0.4..+2.9, horns -1.1..+1.7, trumpets +0.9..+1.8, low brass -2.2..+1.1, strings -0.3..+1.4.
- **Trumpets.** Trumpet 1 +2.6 / +4.0 / +3.1 at f / ff / fff (it leads), Trumpet 2 +0.5..+1.3, Trumpet 3 0.0..+1.3, Trumpets a2 +5.0 / +5.1 (the tune).
- **Percussion.** Tam-tam fff +8.5 (the printed heavy-beater stroke is the loudest stem for two bars) and pp -9.9. Timpani rolls pp -7.6, ppp -8.8.
- **The one shift since c43:** the basses, -0.7..-2.7 dB against the median at every dynamic. In the soft passages C chose this on purpose; at f it is finding 2.

**The coordinator's balance points.**
- *Letter F*, tune minus brass: +6.0 dB median, inside B's 5-6 window after the +1 dB brass lift.
- *Bar 158*, Horns a2 minus (Violins I + flutes) per 1/2 qn: -2.9 / -2.4 / -3.2 / -3.2 / -0.7 / +1.1 (c43: up to +3.6). With the cut undone and the violin lift halved, the horn swells 5 dB and ends only 1.1 dB over the top group, so leave it.
- *Bar 170*, Trumpets a2 minus Trombone 1 per 1/4 qn: -2.4..+5.9. Leave it.
- *Coda*, Trumpets a2 over Horns a2 per bar: +2.2 / +2.9 / +4.0.

**Solo margins** (A, over the loudest other stem, c43 -> c44). All hold within 1.3 dB, except the bars 147-150 tune trio (finding 1).

| Solo | Bars | c43 -> c44 (dB) |
|---|---|---|
| Cor anglais | 5-7 | +8.7 -> +7.8 |
| Horn 1 | 13-14 | +8.9 -> +8.7 |
| Celli dolce | 47-52 | +9.2 -> +9.3 |
| Flute 1 | 73-75 | +10.6 -> +9.3 |
| Clarinet 1 | 127-129 | +12.5 -> +12.9 |
| Coda cello solo | 171-174 | +8.5 -> +9.1 |
| Clarinet 1 | 175-177 | +4.4 -> +4.5 |

**Climax order (CHANGES c44).** 160 > 122 > 167-170 > 26, unchanged. Findings 1-4 move the master by at most -0.2 dB at 160 and 167-170.

**Do not touch:**
- the hall values (fx_volume 0.095, low cut 160 Hz, ir_setup endPos 0.5 / decayLength 0.5) and every send;
- the 150 / 237 ms release caps;
- the soft-passage bell removal on celli and basses, and the climax-span bells;
- the bar-170 and bar-158 shapes as they are now, and the letter-F +1 dB brass;
- the climax set (Violins II cuts with Trumpet 1 fff 8.1);
- the timpani roll levels, `TIMP_CC1_MAP` and `TIMP_RH_ALT` everywhere outside 504-514;
- the tam-tam fff and pp, the suspended-cymbal peak and the K Crash ring;
- the Trumpets a2 coda fit, every solo margin listed above, and the STR_REP_NEW_BOW classification with its other trims;
- plus every c44 and earlier do-not-touch item.

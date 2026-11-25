# Cycle 29, critic B (balance and levels), on the c28 render

All levels below are K-weighted (BS.1770 filter, energy mean over the span) from the c28 stems and master, unless I say RMS or momentary. "Relative to c18" means c28 minus c18 plus 3 dB (the c26 global -3 dB). Delivery figures come from re-running `tools/deliver_master.py` on `cycles/c28/render/00_Master.wav` into my scratch folder. The baseline run reproduces the delivered c28 mp3 exactly: -14.0 LUFS, LRA 10.9, lead +0.67, f -> ff 1.88, p10 -20.6, limiter 3.7. For the spec I used `cycles/c23/actor_scripts/spec23.py`, and for inner lines `cycles/c23/actor_scripts/inner23.py`.

## Manual notes

`loop/MANUAL-READING.md` has no row for c29. Cycles after c20 choose their own pages. The last four B critics read B1 (pp.137, 140, 150-151), so I read the mic and mix pages instead: May 2021 manual PDF pp.138-139 (mic positions and the mics used) and pp.194-200 (Mix page, sub-mixer mic channels, FX bus sends, EQ inserts). I also used `loop/MANUAL-GAPS.md`.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Close mics catch the section's presence. Main (Decca tree, about row 5) catches more room than direct sound, "a big, unified sound" (p.138) | `mix.json` `mic_db` on the winds: Clarinet 1 Main -3.4, Bassoon 1 Main -8.6. The strings use the patch defaults | Yes. The inner-line faults below are level and articulation faults, not mic choice. The countermelody head (finding 2) does not need a closer mic: its body two beats later leads with the same mics |
| Each instrument has sub-mixer mic channels with their own volume and load state (pp.139, 196) | per-track mic levels in `mix.json` | Yes. Mic levels are set per track and unused mics are unloaded (memory cap) |
| An FX send can be pre- or post-fader. "For reverb, post fader is typically used" (p.198) | the shared hall. The Opus reverb is off (`opus_reverb_off`). The REAPER sends are post-fader (`tools/template_mix.py` I_SENDMODE 0) | Yes. So a role row in the volume envelope moves dry and wet together. The role changes in finding 1 change level without changing depth |
| Opus EQ inserts: Channel Equalizer, 6-band Equalizer, Bass Comp (pp.199-200) | `family_eqs`, track `eq` and `master_eq` in REAPER (ReaEQ) | Equivalent. Nothing here needs the Opus EQ |
| MANUAL-GAPS #9 (half-section patch for "la metà") | Violins II from bar 349 | Not needed. Solo plus Flute 1 lead by +15.0 / +12.7 dB in their band (inner23) |

## Findings, ranked by what a listener would hear

### 1. Trio climax, bars 209-216 (qn 624-648): the f tune leads its mf accompaniment by only 1-2 dB. The celli hold is the right shape at too high a level, and the violas rose 8 dB (measured; verdict on the celli +5.4 dB)

**Print** (`sections/tC.ily`, events tsv). The tune is in Violins I and Violins II at f espress., with Clarinet 1 at mf "a level under Vln II" and Flute 1 from 217. The celli have a slurred mf countermelody, doubled by Bassoon 2 ("the strings predominate", tC.ily c087). The violas play mf off-beat slurred tenuto pairs in div. thirds. Nothing new is printed until the crescendo at 648 into the f of 653.

**Per bar (dB).**

| bar | 209 | 210 | 211 | 212 | 213 | 214 | 215 | 216 |
|---|---|---|---|---|---|---|---|---|
| tune group (Vln I + Vln II + Cl 1 + Fl 1), c28 | -29.7 | -33.0 | -32.4 | -30.7 | -32.4 | -32.2 | -33.9 | -31.4 |
| countermelody (Vc + Bsn 2), c28 | -36.3 | -33.1 | -33.8 | -34.1 | -34.6 | -34.4 | -35.0 | -33.0 |
| tune over countermelody, c28 | +6.6 | +0.1 | +1.4 | +3.3 | +2.1 | +2.2 | +1.1 | +1.6 |
| tune over countermelody, c18 | +5.0 | -0.2 | +3.4 | +6.7 | +6.3 | +8.0 | +6.4 | +7.3 |
| Violins I over celli alone, c28 | +2.2 | -3.0 | +2.9 | +1.7 | +0.1 | -1.3 | -1.4 | -0.7 |

- The violas (both tracks) are -36.6 to -40.3 dB, only 3.3-4.5 dB under the tune group. In c18 they were 10-14 dB under.
- Relative to c18, the violas are +8.3 dB over 209-216 and the Violas div +4.0. The celli are +2.0 over the passage and +4.1 to +5.4 in bars 212-215. The tune group is unchanged.
- The tune still wins its own band: inner23 gives +11.4 / +12.8 dB at 624-636, because the tune sits two octaves above. But in loudness, the mf celli are now louder than Violins I's f tune in bars 214-216, and the off-beat violas are nearly level with it.

**Verdict on the +5.4 dB hold (c28 CHANGES asks).**
- Keep the hold. The master sag into bar 215 is 2.6 dB (was 4.3), and the countermelody no longer falls away (Dan, 11-17).
- But the held level is about 2 dB too high on the celli and about 3 dB too high on the violas for mf under an f tune. By the print and by orchestration practice, the tune leads by about one dynamic step. Taking c18 as the upper bound, the target margin is about 3.5-4.5 dB over the countermelody and 6-8 dB over the violas.
- The countermelody also takes the crescendo's room: the celli rise only 4.4 dB from bars 213-216 to the f at 219 (-35.4 -> -31.0).

**Fix (passage levels in the post-fader envelope, edges in gaps or inside the printed crescendo).**
- `build/roles.json` Violoncellos: change [623.6, 648, -1.5] to [623.6, 648, -3.5]. Keep the end ramp where it is now, from the 647.3 legato note across the printed crescendo 648-653.
- `build/roles.json` Violas and Violas div: add [624.4, 648.5, -3.0] to each.
  - Start edge: before the first moved note-on 624.54.
  - End edge: in the gap 648.0-648.54 before the crescendo's first pair.
- Leave the `cresc_trim_hold` keys as they are, so the plateau stays flat.

**Expected (inferred).** Tune over countermelody +3.1 to +4.2 dB in bars 213-216. Tune over violas +6 to +7.5. Master bars 212-216 about -0.5 dB. The 648-653 crescendo gains about 2 dB of rise on the celli.

**Check after the build.** Violins I alone at or over the celli in every bar 212-216. The master plateau before 648 is still flat within 1.5 dB.

### 2. The tenor countermelody's head at the two ff tuttis (celli espress., qn 312 and 912) is 6 dB under the line's second bar. The G3 plays as a legato transition from the accented, unslurred B2, led 0.31 s (measured)

**Print.** The celli play B2 half, accent, ff (310 / 910), then a new slur with espress. from G3 at 312 / 912 (Bassoon 1 and Horn 3 in unison). Nothing slurs the B2 into the G3.

**Stems, per 3 qn (dB).**

| | head 912-915 | body 918-921 | gap | head 312-315 | body 318-321 | gap |
|---|---|---|---|---|---|---|
| celli c28 | -33.8 | -27.6 | 6.2 | -34.2 | -27.9 | 6.3 |
| celli c18 | -26.3 | -24.3 | 2.0 | -26.8 | -24.7 | 2.1 |

- So the head lost 4.5 dB against c18, relative to the global cut. The body did not change.
- inner23 has the line at -0.6 dB (312) and -3.8 dB (912) in its first 6 qn, the lowest of the 37 marked entries I ran. Part of the 912 figure is an artefact: Horn 3's G3 at 912 is dropped as a unison with Horn 4's held G3 (`unison_dropped`), and the measure counts Horn 4 (-28.0 dB there) against the line.

**Mechanism (parts.json c28).**
- The G3 note-on is at 910.614 / 310.636, 1.39 qn before its beat. The cause is `build/lead_set.json` Violoncellos "312": 0.31, "912": 0.315 (c16 refit). Both notes are on "Leg Slur MAX", so by the LEAD_SET_AT rule the B2's end moves with the new note-on.
- The head is therefore a slur transition out of the accented B2 while CC11 is still falling from 124 to 103 after the accent.
- In c18 an envelope ramp to +7.4 dB at 912.12 covered this. Dan's rule removed it, and the soft transition head is what is left.
- The 1.3 dB net in-note moves the actor lists for celli 312 / 912 are inside this same note.

**Fix (instrument side).** The head starts a new bow, as printed.
- `build/score_config.py`: add `ART_SPANS["Violoncellos"] += [{"from": 311.99, "to": 312.01, "art": "Sus MAX"}, {"from": 911.99, "to": 912.01, "art": "Sus MAX"}]`. Check that "Sus MAX" is in the list of rows that take leads (score_to_parts.py near line 305).
- `build/lead_set.json` Violoncellos: delete "312" and "912". The note then takes the string entry lead of about 0.06 s, not 0.31.
- The B2 keeps its printed length, so the two notes do not overlap.
- The next notes of the slur (914 A3, 915 B3) join from the Sus head, as the slur-start Sus heads already do elsewhere.

**Expected (i).** Head within 2-3 dB of the body (the c18 shape, without the envelope ramp). Perceived onset on the beat.

**Check.** Celli 912-915 at -30 dB or higher. The pcx onset of 312 / 912 within ±30 ms. No new hole at 914.

### 3. f -> ff reads 1.88 LU on the mp3 against 5.8 LU on the master. The delivery's top ride takes the step, not the mix (measured, simulated)

**Which passages** (spec23's sets, energy mean of momentary loudness, dB).

| set | passage | c28 mp3 | c27 mp3 | c28 master |
|---|---|---|---|---|
| f | 41-44 | -11.47 | -11.64 | -26.1 |
| f | 129-131 | -10.11 | -10.37 | -23.7 |
| f | 197-200 | -12.14 | -12.11 | -25.6 |
| f | 273-276 | -11.62 | -11.65 | -26.4 |
| f | 285-288 | -11.23 | -11.32 | -25.0 |
| ff | 72 | -9.35 | -9.45 | -18.9 |
| ff | 104 | -8.81 | -8.64 | -18.4 |
| ff | 105-120 | -9.81 | -9.82 | -21.0 |
| ff | 300 | -9.05 | -9.06 | -17.7 |
| ff | 304 | -9.54 | -8.87 | -20.4 |
| ff | 305-320 | -10.05 | -10.06 | -20.8 |

- The weakest pair: the f of 129-131 (-10.11) is level with the ff tutti 305-320 (-10.05) on the mp3. On the master they are 2.9 dB apart.
- c28 dropped the crescendo gains at 309 / 909. That cost the master 1.3 LU of step (7.2 -> 5.8) but the mp3 only 0.2 LU (bars 104 / 304: master -1.6 / -2.4, mp3 -0.2 / -0.7).

**Where the 3.9 LU goes** (the delivery's gain on the EQ'd master).
- Top ride (threshold p95 - 6 = -27.6 LUFS short-term, 2:1): it takes 1.1-2.0 dB from every ff passage and 0.0-0.15 dB from the f passages, because those sit just under its threshold.
- Ride rows: 72 -2.7, 300 -2.5, 305-320 -0.9. Against those, the f row at 197-200 is -2.0.
- Quiet lift: +0.1 to +0.8 dB on the f passages.
- Peak compressor and limiter: about 1.5 LU more on the ff set.

**Simulated fixes** (deliver_master.py env overrides on the same master).

| variant | f -> ff | lead | LRA | p10 | limiter | theme A mean |
|---|---|---|---|---|---|---|
| c28 (top -6) | 1.88 | 0.67 | 10.9 | -20.6 | 3.7 | -17.3 |
| top -4 | 2.15 | 0.61 | 11.3 | -20.9 | 3.8 | -17.6 |
| top -3 | 2.26 | 0.58 | 11.4 | -21.0 | 3.8 | -17.7 |
| top -2 | 2.36 | 0.57 | 11.6 | -21.0 | 3.9 | — |
| top -4, top ratio 1.6 | 2.24 | 0.60 | 11.4 | — | 3.8 | — |
| top -3 + 335 row deeper | 2.26 | 0.74 | 11.4 | -21.0 | 3.8 | -17.7 |
| top -3 + 335 row + Violins I theme A +1.5 dB | **2.29** | **0.76** | **11.5** | **-21.0** | **3.8** | **-17.0** |

I is -14.1 in each, and the climax order holds. 105 stays the one reversed arrival (-0.4).

**Fix.**
- (a) `tools/deliver_master.py`: TOP_ABOVE -6.0 -> -3.0 (the c22 line). The top ride then starts over the f passages and still holds the ff tuttis and the summit.
- (b) `score_config.py` RIDE_TRIMS: the coda row [(990, 0), (993, -2), (996, -4), (1004.6, -4.5), (1005.1, 0)] becomes [(990, 0), (993, -2), (996, -4), (1002, -5), (1004.6, -5.5), (1005.1, 0)]. These are bars before the fff, which the shared spec allows, and the arrival itself is untouched. This gives the summit lead back: 0.58 -> 0.74.
- (c) (a) costs the quiet passages 0.3-0.4 LU, against Dan's 11-17 note. Pay it back where c28 B #6 found the loss (theme A is -2.0 dB against c18): `cc7_spans_db` Violins I [35.6, 84, +1.5].
  - The reprise span [755.6, 804] is already at CC7 127 on 41 points, so leave it.
  - If the build warns of a CC7 cap on [35.6, 84], use a `roles.json` passage row with the same span, edges in the rests before 36 and after the last note before 84.
  - My simulation added 1.5 dB of the Violins I stem to the master in 36-84 and 756-804 (dry only, so slightly optimistic). The reprise half is not in (c).
- All six spec items stay met: -14.1, -1.4 dBTP, lead 0.76, f -> ff 2.29, p10 -21.0, limiter 3.8, LRA 11.5.

### 4. The violas' ff off-beat double stops in the tuttis (312-359, 912-959) play at the violas' own f level, 9 dB under Violins I. The c27 velocity cut did not buy the downbeat it was for (measured)

**Shorts at the onset (first 150 ms, median, dB).**

| | f | ff | f -> ff |
|---|---|---|---|
| violas | -40.2 | -37.8 | +2.4 |
| Violins I | -34.2 | -28.4 | +5.8 |
| Violins II | -40.6 | -30.6 | +10.0 |
| celli | -40.8 | -32.7 | +8.1 |

- Over the passage the violas are -37.6 dB against Violins I -28.5, Violins II -31.6 and celli -31.2. That is -4.5 dB relative to c18 at both tuttis.
- The violas' mf trio accompaniment (-39.1 in 209-216, finding 1) is as loud as their ff tutti.
- Cause: c27's v95 -> v82, a -5.2 dB layer step meant to clear the downbeat. The downbeat over beats 2-3 is still -0.1 / +0.7 dB on the mp3. The cut moved the violas but not the downbeat, which depends on the basses' and violins' fronts (C / A's lens).
- The violas here are an off-beat accompaniment, not a line, so this is a mapping inconsistency rather than a hidden line (i).

**Fix (velocity).**
- `score_config.py` (the c27 rule that sets v82 on the violas' off-beat staccatissimo double stops in 312-359 / 912-959): range-test v88 and v92 against v82 on Violas alone, 312-360.
- Accept the lowest velocity that gives violas ff shorts at least +5 dB over their f shorts, while the violas' beats 2-3 stay at or under the basses' downbeat (-34.5 dB in c27's measure).
- Not a role row: the step is a velocity layer.

### 5. The 34 net in-note moves left, and the per-bar master against c27 (measured from the actor's lists and the stems)

**In-note moves.** From the c28 actor's `records/netmoves_c28.txt`:
- 3 final fermata fades (allowed).
- Harp 238, counted 3 times (3.9 dB on let-ring chords; c28 B #4's role move was tried and rejected).
- Celli 312 / 912 1.3 dB: inside the countermelody head of finding 2. The fix there removes the reason for them.
- Clarinet 1, Clarinet 2 and Bassoon 2 at 1005, 1.1-1.2 dB. The source is still untraced. The summit's passage row [1005, 1017, +2.5] starts at the moved onset on 15 tracks, and these three are the woodwinds whose hold (`cresc_trim_hold` skip [1002, 1005]) ends there. Check whether the row and the skip end together.
- About 24 slow 1.0-1.5 dB ramps on held tutti notes (Horns 3 / 4, brass 309, violas / celli 897, Violins II 360 / 999). These are below what a listener separates inside an f / ff tutti (i).

No action beyond findings 2 and the 1005 check.

**Per bar.**
- Master against c27: median 0.0. Under -1.5 dB: bars 104 / 304 / 305 / 12. Over +1.5 dB: hard-stick bars 9 / 91 / 94, holds 42-43 / 136, trio 214-217 (finding 1), summit 337-340, 58.
- On the mp3 every f / ff passage is within 0.3 dB of c27 except 304 (-0.7).

### 6. Balances checked that are right (measured)

| check | c28 |
|---|---|
| theme A (inner23, best band) | +14.8 / +16.0 dB |
| counterstatement Fl 1 / Ob 1 | +12.2 / +8.6 |
| second idea, bar 45 | +18.5 / +12.1 |
| after the sub. p of 121 | +18.7 / +10.1 |
| trio Clarinet 1 | +14.3 / +11.9 |
| trio celli | +14.0 / +9.3 |
| Oboe 1 at 185 | +10.4 / +13.8 |
| Hn 1 motto, 357 | +12.4 / +14.0 |
| solo violin with Flute 1 | +15.0 / +12.7 |
| codetta Oboe 1, K-weighted | 7-9 dB over the next stem (inner23's +1.1 counts the hall returns) |
| Hn 1's last G sharp, 1125-1128 | -50.8 against Violins I -54.2 and the solo track -51.1 (ppp, both printed to the end) |
| trumpets' quarters, 105-120 | 7.5 dB under Violins I |
| timpani and low brass, 105-120 | -36.6 / -37.5 against the theme's -28.5 |
| summit brass (f / ff) | 4-15 dB under the fff strings and woodwinds, as the score asks |
| Flute 1 / Oboe 1 at 277 | +2.7 / +3.2 (weakest of these; reported before) |

## Do not touch

- The trio hold itself (`hold_to_dec_qn` 32, rest 2 qn, short arrivals held); finding 1 changes only the level it holds.
- The c28 summit passage level [1005, 1017, +2.5] and the coda ride rows' shape.
- The -14 delivery chain, room bed, peak compressor and quiet lift 2.1. Finding 3 changes only TOP_ABOVE and one ride row.
- The Violins I theme lead and the reprise CC7 span.
- Horn 3 / Horn 4 countermelody roles from 311.5 / 911.5.
- The solo violin, Flute 1 and Violins II balance at 349-356.
- Hn 1's motto and final G sharp.
- The trumpets and low brass under the tutti theme.
- The -3 dB global gain and the post-fader hall sends.

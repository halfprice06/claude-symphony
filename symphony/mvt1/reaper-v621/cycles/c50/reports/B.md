# Critic B, cycle 50 (render c49): balance and levels through the EastWest template switch

c50 adopts `build/mix_template50.json`. A family EQ is linear, so I applied each family EQ to every c49 dry stem and recomputed the balance. That part of the prediction is exact, apart from how ReaEQ shapes its shelves. Two parts of the switch cannot be simulated from audio: the new mic levels and the removal of the Opus hall. For those I used the finale's c06 render, which made the same switch from the same c05-era mics (`symphony/mvt3/reaper-v600/cycles/c06/CHANGES.md`, `c07/reports/B.md`). Every number from that source is marked inferred.

## Manual notes (second round, c48-51: pages chosen for this lens's top open problem, the template switch; MANUAL-GAPS.md and DIGEST.md sections 2, 4, 10 read)

| Manual (May 2021 HO, PDF page) | Where it applies | Followed? |
|---|---|---|
| p.138: Close mics capture presence; Main (about the fifth row) picks up more room than direct sound; Surround mics (high at the back) give a lush sound without definition. | The template puts Close 6-10 dB under a full-width Main on strings and brass, makes the winds Close-led, and adds the timpani's Surround mic at 0 dB. | Strings, brass and winds follow it. The timpani Surround does not suit this score (finding 2): a mic that "lacks definition", on a felt roll, is what made the c01 rolls cover the orchestra. |
| p.139: each mic sub-mix has its own volume, pan and load state. Loading a mic loads its samples. | `mic_db` and `pan_by_mic` in template50. | Yes. Loading the timpani Surround mic and the harp Mid mic adds sample memory, and the main pass already settles at 44 GB of the 45 GB limit (c49). |
| p.140: the master Gain changes the instrument's output level and leaves the mic sub-mix as it is. | The template's Opus master gains (string KS Masters +3.5..+5.1 dB, 1FH +8.0, timpani +3.3; `opus-mics.txt`). Template50 does not copy them; our `gain_db` does that job. | Yes. EastWest's own +8 dB on the solo horn under this EQ supports the horn make-up in finding 1. |
| p.198: an FX-bus send can be pre- or post-fader; the manual recommends post-fader for reverb. | The template's REAPER sends are post-fader. | Yes. Each send now carries the volume envelope, so every gain change in finding 1 also changes that track's reverb. A stem fix does not (finding 1, last paragraph). |
| p.199-200: Opus has its own EQ inserts (Channel EQ, 6-band Equalizer). | The family EQs are REAPER ReaEQs after Opus. | No conflict. No Opus EQ insert is in use. |
| p.123-125: Timpani Felt KS rolls (D#0) have 8 dynamic layers on CC1. CC11 and velocity set loudness. Felt Cresc (E0) holds recorded crescendos. | Timpani rolls: CC1 lane, CC7 level, volume-envelope settles. | Yes. Nothing in the template changes the roll programming. Only its mics and EQ threaten the roll balance (finding 2). MANUAL-GAPS #12 (Felt Cresc) stays open and low priority. |
| MANUAL-GAPS #4 (Mid instead of Close on the winds) | Template50 goes the opposite way: Close 0 dB with Main 3.4-20.6 dB under it. | Not followed. The winds become the closest and driest family (finding 3). Keep #4 open as a later pass-2 test. |

EW-TEMPLATE-PLAN items that template50 does not yet apply: section 8 basses -2.4..-3.6 dB at 205-250 Hz; section 9 register sends and the 2.3 kHz low-pass after Spaces II; section 8 Duc sends (template50 has them only as the inactive `duc` profile); section 4's pass-2 copy of the old layout (it needs test aliases in score_config.py); section 1's harp and timpani template mics are in the file, and I recommend against them (findings 2 and 5). Section 5 onwards is c51 work.

## Method

- Stems: `cycles/c49/render/01-40` (dry). Frames: 8192-point Hann FFT, 4096 hop, stereo power L²+R². Weighting is K, the convention of this loop's balance critics; A-weighting is given where it differs. Bars come from the parts.json tempo map.
- EQ: RBJ biquads with ReaEQ's bandwidth in octaves. Shelves were modelled as gentle, non-resonant shelves (the finale's c07 critic B showed that ReaEQ's 0.33-octave strings shelf is not resonant).
- Scenarios:
  - c49: as rendered.
  - P1: template50 exactly as written. Template family EQs (harp HPF 183 Hz, full timpani EQ), inferred mic offsets, no gain changes.
  - P2: my recommendations. Reduced timpani EQ, harp HPF 80 Hz, the trumpets' +2.5 dB and bass clarinet's -4 dB shelves removed, basses 230 Hz -3 dB with a 35 Hz HPF, plus the make-up and trims in findings 1, 3 and 6.
- Inferred mic and hall offsets (dB, absolute), calibrated on the finale's c06 residuals:
  - Violins I -2.2, Violins II -1.9, violas -1.6, celli -1.5, basses +0.4 (their Close rises from 0.6 to 0.68).
  - Flutes and clarinets +3.7..+4.0, oboes +2.4, cor anglais +2.7, bass clarinet +2.8, bassoons and contrabassoon +3.0.
  - Horns -0.4, Horns a2 -0.7, trumpets -2.1, trombones and tuba -1.8.
  - Timpani -0.3 and harp -0.2 (both kept on c49 mics), tam-tam and cymbals -0.7.
  - The uncertainty is about ±1 dB on strings and brass, and ±1.5 dB on the winds.
- Checks: "over loudest other" is the lead minus the loudest single other dry stem, per 1 qn, taking the median over the windows where the lead is within 15 dB of its loudest. "Minus" rows compare summed groups over the span. Return stems (91+) are excluded throughout.

## Findings, ranked by what a listener would hear

### 1. The brass family EQ takes 6-9 dB off the brass and 1.3-1.9 dB off the strings. Template50 has no make-up, so every brass lead loses 4-6 dB (EQ measured, mics inferred)

**Where.** Every brass passage. The worst places are the tuttis at bars 25-32, 115-126 and 158-161, the Horns a2 at bars 41-42, the trumpet tune at 167-170, the horn solo at 13-14 and the trombone chorale at 175-178.

**Evidence.** The BRASS EQ (-5.4 dB at 475 Hz and -7.8 dB at 821 Hz, both 1.92 octaves wide) overlaps into about -10 dB across 450-1000 Hz. Per-bar medians of the EQ alone (K):

| Track | EQ change (K) |
|---|---|
| Horns | -7.2 to -8.3 |
| Horns a2 | -8.7 |
| Trumpets | -6.3 to -6.7 |
| Trombones | -6.8 to -7.4 |
| Tuba | -5.5 (A-weighted -7.9) |
| Winds | -4.5 |
| Violins I | -1.4 |
| Violins II, violas, celli | -1.3 to -1.9 |
| Harp (HPF 80) | -4.3 |
| Timpani (reduced EQ) | -3.1 |

With the inferred mic offsets added, template50 as written gives these results (K, dry stems):

| Check | c49 | P1 (template50 as written) |
|---|---|---|
| Brass minus strings, bars 25-32 | -0.1 | -5.5 |
| Brass minus strings, bars 115-122 | +0.9 | -4.1 |
| Brass minus strings, bars 123-126 | +1.9 | -3.5 |
| Brass minus strings, bars 158-161 | -0.1 | -5.1 |
| Horns a2 over the loudest other, bars 41-42 | +0.8 | -4.9 |
| Trumpets a2 minus Violins I, bars 167-170 | +1.4 | -2.3 |
| Trumpet 1 minus Violins I, ff motif bars 82-83 | -0.7 | -5.7 |
| Horn 1 solo over the loudest other, bars 13-14 | +10.7 | +6.7 |
| pp trombone chorale minus strings, bars 175-178 | -2.4 | -8.8 |

At f in the same-dynamic scan (1 qn windows with a flat printed dynamic, against the upper strings' median), template50 as written moves:

| Family at f | c49 | P1 |
|---|---|---|
| Horns | -2.0 | -7.0 |
| Trumpets | -0.1 | -5.8 |
| Trombones and tuba | 0.0 | -5.7 |
| Winds | -4.1 | -2.3 |

That inverts Rimsky-Korsakov's forte ratios: a horn about two woodwinds, a trombone about two horns (Principles, "Comparison of resonance"; KIT §13). The finale measured the same on the same patches: brass needed +4-6 dB after the family EQ. EastWest itself runs the solo horn's Opus master at +8.0 dB under this EQ (`opus-mics.txt`).

**Fix.** Edit `build/mix.json` after copying template50. These are `gain_db` changes from the c49 values, chosen to put each family back at its c49 level against the strings.

| Track | gain_db, c49 -> c50 | Change |
|---|---|---|
| Horn 1 | -4 -> +1.5 | +5.5 |
| Horn 2 | -4 -> +0.5 | +4.5 |
| Horn 3 | -4 -> +1.0 | +5.0 |
| Horn 4 | -4 -> +1.5 | +5.5 |
| Horns a2 | 0.6 -> 7.1 | +6.5 |
| Trumpet 1 | -3 -> +2.0 | +5.0 |
| Trumpet 2 | -3 -> +2.0 | +5.0 |
| Trumpet 3 | -3 -> +2.5 | +5.5 |
| Trumpets a2 | -1.5 -> +3.0 | +4.5 |
| Trombone 1 | 0 -> +6.0 | +6.0 |
| Trombone 2 | 0 -> +5.5 | +5.5 |
| Bass trombone | 0 -> +5.5 | +5.5 |
| Tuba | 2 -> 7.0 | +5.0 (between the K value, +4.1, and the A value, +5.9) |

Simulated with findings 3 and 6 (P2, K), the checks come back:

| Check | c49 | P2 (recommended) |
|---|---|---|
| Brass minus strings, bars 25-32 | -0.1 | -0.4 |
| Brass minus strings, bars 115-122 | +0.9 | +0.7 |
| Brass minus strings, bars 123-126 | +1.9 | +1.4 |
| Brass minus strings, bars 158-161 | -0.1 | -0.6 |
| Horns minus heavy brass, bars 123-126 | -3.5 | -4.2 |
| Horns a2 over the loudest other, bars 41-42 | +0.8 | -0.8 |
| Trumpets a2 minus Violins I, bars 167-170 | +1.4 | +0.8 |
| Trumpets a2 minus Horns a2, bars 167-170 | +1.3 | +1.4 |
| Trumpet 1 minus Violins I, bars 82-83 | -0.7 | -1.9 |
| Horn 1 solo over the loudest other, bars 13-14 | +10.7 | +12.1 |
| pp chorale minus strings, bars 175-178 | -2.4 | -1.8 |

Only the Horns a2 at bars 41-42 stays short. If the render confirms it, add +1 dB there.

**Measure the make-up instead of guessing it.** The mic part of these numbers is inferred. Build plan section 4's pass-2 copy of the old layout as test aliases of one track per family:
- Violins I, Violoncellos, Double basses;
- Flute 1, Oboe 1, Clarinet 1, Bassoon 1;
- Horn 1, Trumpet 1, Trombone 1, Tuba;
- Harp.

Give each alias `"mic_db": null, "pan_by_mic": null, "family_eq": null, "send_profile": null, "reaper_pan": null, "opus_reverb_off": false` (TEMPLATE-TOOLS.md) and the c49 `gain_db`. Then the per-bar K difference between the c50 main stem and its old-layout test stem, minus the gain change, is the measured switch loss per family. That is 12 instances, and c49's pass 2 held 19 at 41 GB.

Correct the gains by that measurement. Write the corrected values into mix.json for c51, as well as applying them by stem fix: `stem_fix.py` leaves each return at the old send level ("return stems are summed unchanged"). So a correction of 2 dB or more on a track also shifts that track's wet/dry ratio by the same amount until the next build.

### 2. Template50 gives the timpani the template's +8.6 dB 84 Hz bell and a Surround mic at 0 dB. The long rolls would take two to three times their c49 share of the low end, against Dan's standing rule (EQ measured, mics inferred)

**Where.** Timpani, every long roll. Dan's rule is that long rolls must not drown other parts. The long rolls are:
- bars 1-4 (ppp) and 11-14;
- bars 40-43 (pp<>), 62-63 and 80-81 (p<ff);
- bars 117-130 (f-ff, 14 bars under the development climax, the sostenuto and the tam-tam);
- bars 144-146, 158-160 (ff) and 166-169;
- bars 174 and 181-182 (ppp).

**Evidence (measured, EQ only, c49 mics kept).** The template timpani EQ changes the timpani stem by:
- 30-150 Hz: +3.6 dB;
- 60-120 Hz: +4.6 dB;
- 20-100 Hz: +6.0 dB;
- 250-500 Hz: -10.2 dB;
- K-weighted level: -1.6 dB.

So the drum loses its body and stroke while its boom rises. The timpani's share of the dry sum's 30-150 Hz:

| Roll | c49 | P1 (template EQ) | P2 (reduced EQ) |
|---|---|---|---|
| 11 | 18 % | 40 % | 20 % |
| 13-14 | 24 % | 53 % | 27 % |
| 62-63 | 29 % | 43 % | 29 % |
| 117-130 | 13 % | 31 % | 12 % |
| 144-146 | 29 % | 61 % | 34 % |
| 158-160 | 22 % | 42 % | 23 % |

At 158-160 the roll comes out +0.8 dB over every other stem on one beat (c49: -1.8 at most).

**Evidence (inferred, the mics).** P1 does not yet include the mic change, which goes the same way:
- Template50 sets Close -8.4, Main -6.9 and Surround 0 dB. c49 has Close 0.2 / Main 0.5 and no Surround.
- KIT §10: with the factory Surround (0.46) and a 3.3 s hall, the timpani took 85-100 % of the master's 100-300 Hz (c01).
- Taking Surround off (Close 0.2 / Main 0.5) removed 7 dB from the timpani's 125-180 Hz (c05). The template's Surround (1.0) is 6.7 dB above the factory level (0.46).
- The R Perc return (high-pass at only 100 Hz, 2.6 s) then adds low-mid reverb that c49's hall, with its 160 Hz low cut, did not.

The finale rejected the same EQ for the same reason, and kept its old timpani mics to save memory (`mvt3/.../c06/reports/B.md` finding 2).

**Fix (`build/mix.json`).**
1. `groups.timp.mic_db` = `{"Close": -14.0, "Main": -6.0}`. That is c49's 0.2 / 0.5, and it leaves Surround unloaded, which also saves memory.
2. `family_eqs.timpani` = `[{"band": "highpass", "hz": 44.0, "bw_oct": 1.142}, {"band": "bell", "hz": 385.0, "db": -6.0, "bw_oct": 2.54}, {"band": "highshelf", "hz": 6960.0, "db": 4.5, "bw_oct": 1.39}]`. This is the finale's reduced form: -3.1 dB K, -1.0 dB at 30-150 Hz.
3. Remove the Timpani `loud_eq` (140 Hz +3 dB bell). R Perc now supplies the roll's low-mid reverb in the loud spans (inferred).
4. Keep `gain_db` -7. Do not copy the template's timpani Opus master gain (+3.3 dB).

With these changes, P2 holds every roll within 1.5 dB of c49 (table under "Checks").

### 3. The Close-led winds and the unequalised percussion come out 2-3 dB hot against the strings, and the cor anglais answers would cover the horn tune (EQ measured, mics inferred)

**Where.**
- Winds: everywhere, and most clearly in the soft solos and answers. At bars 147-152, Cor anglais minus Horn 1 goes from -4.9 dB to +1.5 in P1. Those answers were put under the tune on purpose (c41 B #1, c49 B #5).
- Percussion: the tam-tam fff at 484-491, the cymbal stroke at 636 and the tam-tam pp at 175.
- Within the strings: Violins I against the celli.

**Evidence.**
- Winds:
  - The WOODWINDS EQ removes 4.5 dB (measured, flat across dynamics within 0.5 dB).
  - Template50 doubles every wind's Close (0.5 -> 1.0) with Main at the template's -3.4..-20.6 dB. The finale's power-matched version of this layout still came out 2.9 dB hot (inferred: +2.4..+4.0 dB here).
  - P1 results: winds minus strings at bars 25-32 goes -1.5 -> +0.2, at 115-122 -0.2 -> +1.6, at 158-161 -2.1 -> -0.3. At p, the same-dynamic scan puts the winds 2.6 dB over the upper strings (c49 -0.2).
- Percussion: the tam-tam and cymbals get no family EQ and lose only their Close mic, while everything around them drops 3-9 dB. Tam-tam fff minus all others goes -6.6 -> -3.3, the bar-160 cymbal pair -15.9 -> -13.2, the bar-175 tam-tam pp -9.8 -> -6.8 (measured EQ, inferred mic).
- Within the strings: Violins I loses more Close (-9.0 dB under Main) than the celli (-6.6); the EQ costs both about the same (K -1.4 / -1.3). So the Violins I theme over the celli at bars 15-22 drops from +4.2 to +3.3 (inferred mic share 0.7 dB). The basses rise against the upper strings under the template (finding 4).

**Fix (`gain_db`, c49 -> c50).**
- Winds:

  | Track | gain_db, c49 -> c50 | Change |
  |---|---|---|
  | Flute 1 | -1.3 -> -3.8 | -2.5 |
  | Flute 2 | -1.5 -> -4.5 | -3.0 |
  | Oboe 1 | -5.3 -> -6.8 | -1.5 |
  | Oboe 2 | -5.3 -> -6.8 | -1.5 |
  | Cor anglais | -1 -> -2.5 | -1.5 |
  | Clarinet 1 | -1 -> -4.0 | -3.0 |
  | Clarinet 2 | -1 -> -4.5 | -3.5 |
  | Bass clarinet | 1 -> -2.0 | -3.0 (with its shelf removed, finding 5) |
  | Bassoon 1 | -2 -> -4.0 | -2.0 |
  | Bassoon 2 | -2 -> -4.0 | -2.0 |
  | Contrabassoon | 2 -> -1.0 | -3.0 |

  The stac aliases follow their sources: Flute 1 stac -3.8, Cor anglais stac -2.5, Bassoon 1 stac -4.0.
- Percussion: Tam-tam 1 -> -2.0, Suspended cymbal -8 -> -11.0, Crash cymbals -1 -> -4.0.
- Strings:
  - Violins I 5 -> 6.0, and Violins I f62 5 -> 6.0.
  - Double basses -8 -> -9.0 (with finding 4's 230 Hz cut; -10.5 without it).
  - Cello solo 6.0 -> 5.0. It keeps its Close-only `mics` and loses only the EQ.
  - Violins II, violas and celli unchanged.
- Harp: -4 -> -3.0 (finding 5).

P2 results:

| Check | c49 | P2 |
|---|---|---|
| Winds minus strings, bars 25-32 | -1.5 | -2.1 |
| Winds minus strings, bars 115-122 | -0.2 | -0.9 |
| Winds minus strings, bars 158-161 | -2.1 | -2.9 |
| Cor anglais minus Horn 1, bars 147-152 | -4.9 | -5.5 |
| Tam-tam fff minus all others | -6.6 | -7.2 |
| Bar-160 cymbals minus all others | -15.9 | -16.5 |
| Violins I theme over the loudest other, bars 15-22 | +4.2 | +4.3 |
| Violins f62 over the loudest other, bars 56-61 | +7.4 | +8.5 |
| CA solo over the loudest other, bars 5-8 | +4.8 | +4.6 |
| Cello solo over the loudest other, 680-696 | +7.6 | +8.8 |
| Clarinet 1 over the loudest other, coda (minimum) | +1.2 | +0.7 |

The wind numbers carry the largest uncertainty, -1 to -3.5 dB depending on the Close mic's raw level. Correct them from the Flute 1 / Oboe 1 / Clarinet 1 / Bassoon 1 test stems (finding 1).

### 4. Template50 is missing three of the coordinator's items, and without them the returns will make the low end heavy (file read, shares measured, return effect inferred)

**Where.** The low end of every tutti, and the bass line under soft passages.

**Evidence.** Template50 is missing:
- the register sends: its send profile is by group only, and no track has a `send_offset_db` except the inactive R Duc entries;
- the basses' 205-250 Hz cut;
- the 2.3 kHz low-pass after Spaces II: each return has only its chunk ReaEQ and Spaces II.

The dry stems after the EQ already carry more low mids. The 100-250 Hz share of the dry sum goes -9.05 -> -7.0 dB over the whole piece and -9.64 -> -7.5 in the loudest 10 % of frames (measured). The references are -6.6 / -8.75 / -7.55.

The returns then add low mids that c49's hall did not have: c49's hall had a 160 Hz low cut (c44, Dan's "mushy" note), while the template's string return high-passes at 87 Hz. In the finale, R Strings carried 2.4-2.9 dB more 80-320 Hz energy than the dry strings, and the master's 100-250 Hz share went to -5.6 (`mvt3/.../c07/reports/B.md` finding 1; inferred to apply here).

The register sends are a large part of the cure, by these shares (measured):
- The basses carry 42-46 % of the strings' 100-250 Hz, so -10 dB on their send takes 2.0-2.3 dB off R Strings there.
- Trombones and tuba carry 86-91 % of the brass's 100-250 Hz: R Brass -6.5..-7.5 dB.
- Bassoons and contrabassoon carry 65-82 % of the winds': R Winds -3.8..-5.8 dB.

Under the template's 53 Hz HPF and with no 230 Hz cut, the EQ costs the basses only 1.0 dB A, and their Close rises (0.6 -> 0.68): about -0.6 dB in all, against -3.6..-4.0 dB for the upper strings (EQ measured, mics inferred). They would rise about 3 dB in the string balance. The 53 Hz HPF also takes 3.6 dB off their 25-60 Hz: 101 of their 366 notes are at or below A1 (lowest F1, 44 Hz).

**Fix (`build/mix.json`).**
- Register sends:
  - `groups.lowbrass.send_offset_db` = `{"R Brass": -10.0}`;
  - `groups.trumpet.send_offset_db` = `{"R Brass": -6.0}`;
  - `send_offset_db` `{"R Winds": -10.0}` on the tracks Bassoon 1, Bassoon 2, Contrabassoon and Bassoon 1 stac;
  - Double basses `send_offset_db` = `{"R Strings": -10.0, "R Duc": -1.6}`. A track key replaces the group's, so keep the R Duc entry.
- Basses EQ:
  - Add `{"band": "bell", "hz": 230, "db": -3.0, "bw_oct": 1.39}` to the basses' track `eq`. Band slot 1 is free; they use the high-pass and bell2.
  - Give them `"family_eq": "strings_cb"`, a copy of `family_eqs.strings` with the high-pass at 35 Hz. This costs 1.4 dB in 25-60 Hz instead of 3.6, and 2.3 dB K in total with the cut.
- Returns:
  - Append `{"reaeq": [{"band": "lowpass", "hz": 2300, "bw_oct": 2.0}]}` to each return's `fx` list, after Spaces.
  - Replace R Strings' first FX with `{"reaeq": [{"band": "highpass", "hz": 160, "bw_oct": 2.639}, {"band": "bell", "hz": 2670, "db": -6.7, "bw_oct": 1.39}, {"band": "lowpass", "hz": 8490, "bw_oct": 2.0}]}`: the template's bands with c44's 160 Hz cut. The finale's c07 critic B simulated this on its render: with Duc's sends, the master's 100-250 Hz share went -5.6 -> -7.4.
- Optional (plan section 8): celli `send_offset_db` `{"R Strings": -1.6, "R Duc": -1.6}`.
- Check on the render: the master's 100-250 Hz share in the loudest 10 % of frames should be -7 to -8.5 dB. If it comes out above -6.5, halve the low `loud_eq` bells in c51: celli and basses +6 -> +3; contrabassoon, bass trombone and tuba +4 -> +2; Bassoon 2 +3 -> +1.5.

### 5. Old EQs that duplicate the family EQ, and the harp's 183 Hz high-pass (measured)

**Where.** The per-track `eq` and `loud_eq` entries in mix.json, and the harp in the second theme and the recapitulation.

**Evidence.**
- Trumpets: the +2.5 dB 4 kHz shelf stacks on the brass +4 dB shelf at 7.49 kHz. With it removed, Trumpet 1 holds 4.7 % of the 6-20 kHz band after the switch (c49: 9.0 %). c49 already left the Trumpets a2 8-16 kHz share open because of this shelf.
- Bass clarinet: its -4 dB 2.5 kHz shelf stacks with the woodwinds' -4.7 dB 2.2 kHz bell, which puts about -8.5 dB on its 2-4 kHz.
- The family high-passes (53 Hz strings, 41 Hz brass, 44 Hz timpani) replace the 40-45 Hz high-passes.
- Brightness: the dry sum's 6-20 kHz share goes -30.4 -> -24.6 dB. The references are -28.8 to -32.3, and the finale measured -25.1. Violins I would hold 51 % of that band (c49: 40.5 %). Its own 5 kHz -4 dB shelf is the one counterweight on the brightest track.
- Harp: the template EQ's 183 Hz high-pass removes the fundamentals of 61 of its 184 notes (at or below F#3), in bars 47-68, 156-166 and 182. In bars 47-68 it costs -24.7 dB at 25-60 Hz and -11.6 dB at 60-120 Hz, against -11.3 / -3.1 dB with an 80 Hz high-pass.
- Harp mics: template50 also sets the harp to Close 0 / Mid 0 / Main -9 dB, which loads the Mid mic.

**Fix.**
- Drop:
  - `highshelf 4000 +2.5` on Trumpets 1-3 and Trumpets a2;
  - `highshelf 2500 -4` on Bass clarinet;
  - `highpass 40` on Violins I/II, violas, the f62 aliases, Horns 1-4, Horns a2, Trumpets 1-3, Trumpets a2, Trombones 1-2 and Bass trombone;
  - `highpass 45` on Timpani;
  - `highpass 30` on Harp and Violoncellos.
- Keep:
  - Violins I `highshelf 5000 -4`;
  - the Violins I/II `loud_eq` 2.5 kHz -2.5 and Violins II's 584-619 sul tasto EQ;
  - the trombones' `highshelf 4000 -4`;
  - Horns a2 `highshelf 1250 -3` and its 1.6 kHz `loud_eq` (2FH samples are 5-15 dB brighter than 1FH; the family EQ hits both alike);
  - Trumpet 1's 633.8-644.6 shelves and the Trumpets a2 3.2 kHz bell;
  - the tuba 70 Hz shelf, 84 Hz bell2 and 25 Hz HPF; the contrabassoon 70 Hz shelf; the basses' 87.3 Hz bell2;
  - the Cello solo body bells; the tam-tam 86 Hz bell2 and the cymbals' 60 Hz HPF (percussion has no family EQ);
  - the woodwind 30/40 Hz HPFs (the woodwind EQ has none);
  - every `side_shelf` for c50. Whether full-width Mains make the wind/brass +1.5 dB side shelves redundant is a blend question.
- Harp: `family_eqs.harp[0].hz` 183 -> 80. Set `groups.harp.mic_db` = `{"Close": -4.4, "Main": 0.0}` (c49's 0.6 / 1.0, no Mid: memory, and its c49 balance), and gain -4 -> -3.0. P2: harp minus celli at bars 47-55 is -7.4 (c49) -> -7.7 (P1: -9.9).

### 6. The brass EQ changes the spacing between dynamics on the brass. Without trims, p no longer sounds like p across the families (measured)

**Where.** Trombones and trumpets, which lose more when soft; horns and tuba, which lose less when soft. Strings, winds, harp and timpani are flat within 0.5-1 dB.

**Evidence (EQ change by printed dynamic, K, per-bar medians).**

| Track | Soft | Loud |
|---|---|---|
| Trombone 1 | pp -8.2 | f -7.6, ff -5.5 |
| Trombone 2 | pp -9.2 | ff -5.1 |
| Trumpet 3 | p -7.9 | fff -4.6 |
| Horn 3 | pp -6.1, p -5.9 | f -7.7 |
| Horn 4 | pp -5.9 | f -8.3 |
| Tuba | pp -3.9 | ff -6.4 |

So the same CC11 layer table gives a trombone pp-to-ff spread about 3-4 dB wider than in c49, and a tuba spread 2.5 dB narrower.

Same-dynamic scan (family median minus the upper strings' median):

| Dynamic and family | c49 | P1 | P2 |
|---|---|---|---|
| pp, trombones and tuba | -2.4 | -8.2 | -1.2 |
| pp, horns | -2.3 | -4.8 | -1.4 |
| p, winds | -0.2 | +2.6 | -0.4 |
| p, horns | -0.7 | -4.8 | -0.9 |
| p, harp | -4.3 | -9.1 | -5.4 |
| f, trumpets | -0.1 | -5.8 | -0.9 |
| ff, trumpets | +1.5 | -3.5 | +1.2 |
| ff, trombones and tuba | +1.0 | -3.5 | +1.1 |

With P2 every family sits within about 1 dB of c49 at every dynamic. The harp at p is 1.1 dB under.

**Fix (`build/mix.json`, on top of finding 1's gains).**
- Trombone 1, Trombone 2, Bass trombone: `soft_trim_db` ppp/pp/p +1.5 (Trombone 1: 14.6 / 14.6 / 10.6 -> 16.1 / 16.1 / 12.1); `dyn_trim_db` ff and fff -2.0 (Trombone 1: 0.8 / -0.6 -> -1.2 / -2.6; Trombone 2: 3.3 / 1.9 -> 1.3 / -0.1; Bass trombone: 3.3 / 2.2 -> 1.3 / 0.2).
- Trumpets 1-3: `soft_trim_db` p and mp +1.0; `dyn_trim_db` fff -1.0.
- Horns 3 and 4: `soft_trim_db` ppp/pp -2.0 and p -1.0. Horns 1 and 2: p -1.0.
- Tuba: `soft_trim_db` pp/p -1.5; `dyn_trim_db` ff/fff +1.5.

The trombone pp lift costs the coda clarinet some margin (its minimum over the loudest other, Trombone 1, goes +1.2 -> +0.7 in P2). If the render confirms that, use +0.5 at pp instead of +1.5. These are level-only changes, so they can be stem-fixed if the render disagrees. Leave CC11 alone: the layer timbre per printed dynamic is right, only the level spacing moved.

## Checks for the c50 render (dry stems, K, the windows above; return stems 91+ excluded)

| Check | c49 | Template50 as written (P1) | Expected with findings 1-6 (P2) | Pass |
|---|---|---|---|---|
| Brass minus strings, bars 25-32 / 115-122 / 123-126 / 158-161 | -0.1 / +0.9 / +1.9 / -0.1 | -5.5 / -4.1 / -3.5 / -5.1 | -0.4 / +0.7 / +1.4 / -0.6 | each within 1 dB of c49 |
| Horns minus trumpets+trombones+tuba, bars 123-126 | -3.5 | -4.8 | -4.2 | -3 to -5 |
| Horns a2 over loudest other, bars 41-42 (median) | +0.8 | -4.9 | -0.8 | 0 or more |
| Trumpets a2 minus Violins I / minus Horns a2, bars 167-170 | +1.4 / +1.3 | -2.3 / +3.8 | +0.8 / +1.4 | +0.5 to +2.5 each |
| Trumpet 1 minus Violins I, bars 82-83 | -0.7 | -5.7 | -1.9 | -2 to 0 |
| Horn 1 solo over loudest other, bars 13-14 | +10.7 | +6.7 | +12.1 | +8 or more |
| Violins I theme over loudest other, bars 15-22 | +4.2 | +3.3 | +4.3 | +3.5 or more |
| Celli tune over loudest other, bars 47-55 | +3.8 | +6.4 | +3.7 | +3 or more |
| Harp minus celli, bars 47-55 | -7.4 | -9.9 | -7.7 | -6.5 to -8.5 |
| Winds minus strings, bars 25-32 / 158-161 | -1.5 / -2.1 | +0.2 / -0.3 | -2.1 / -2.9 | -1 to -3 |
| Cor anglais minus Horn 1, bars 147-152 | -4.9 | +1.5 | -5.5 | -4 to -6 |
| Tam-tam fff minus all others, 484-491 | -6.6 | -3.3 | -7.2 | -6 to -7.5 |
| Sus. cymbal + crash minus all others, 636-640 | -15.9 | -13.2 | -16.5 | -15 to -17 |
| pp chorale (trombones + tuba) minus strings, bars 175-178 | -2.4 | -8.8 | -1.8 | -1.5 to -3.5 |
| Clarinet 1 over loudest other, 699-706 (minimum / median) | +1.2 / +4.3 | +2.6 / +5.4 | +0.7 / +4.0 | minimum +1 or more |
| Cello solo over loudest other, 680-696 | +7.6 | +8.3 | +8.8 | +6 or more |
| Timpani ppp minus violas, bars 181-182 | -8.2 | -7.7 | -8.5 | -6 to -10 |

Timpani rolls. Each cell gives the roll minus the loudest other stem per 1 qn (median / maximum), then the timpani's share of the 30-150 Hz energy. Pass: the median within 1.5 dB of c49, no maximum over 0 except on printed strokes or the ends of printed crescendos, and the share no higher than c49 + 5 points.

| Roll | c49 | P1 | P2 |
|---|---|---|---|
| 11 pp< | -7.0 / -5.3, 18 % | -5.2 / -4.8, 40 % | -8.0 / -6.8, 20 % |
| 13-14 | -17.9 / -10.1, 24 % | -9.8 / -6.2, 53 % | -19.0 / -9.9, 27 % |
| 40-43 pp<> | -10.9 / -4.8, 38 % | -10.8 / -3.7, 48 % | -12.2 / -6.1, 38 % |
| 62-63 | -7.7 / -5.3, 29 % | -8.8 / -6.5, 43 % | -8.0 / -5.3, 29 % |
| 80-81 p<ff | -6.5 / -2.2, 31 % | -7.4 / -3.5, 36 % | -7.9 / -3.9, 31 % |
| 117-130 f-ff | -9.4 / -2.0, 13 % | -8.9 / -2.1, 31 % | -10.4 / -1.9, 12 % |
| 144-146 | -7.8 / -4.3, 29 % | -5.9 / -1.0, 61 % | -7.9 / -4.4, 34 % |
| 158-160 ff | -5.6 / -1.8, 22 % | -6.0 / +0.8, 42 % | -7.2 / -2.3, 23 % |
| 166-169 < | -5.4 / -0.9, 33 % | -4.7 / -2.4, 38 % | -5.8 / -0.2, 24 % |
| 181-182 ppp | -9.0 / -5.4, 13 % | -8.3 / -6.4, 20 % | -9.2 / -5.5, 14 % |

For the master, where the returns count, also check:
- the timpani dry stem plus R Perc as a share of the master's 30-150 Hz, per roll, against the c49 shares above;
- the master's 100-250 Hz share in the loudest 10 % of frames, at -7 to -8.5 dB (c49 -9.6);
- the 6-20 kHz share. The dry sum is predicted at -24.6, and the references are -28.8 to -32.3. If it reads 3 dB or more over -28.8, the c07 finale fixes apply (halve the family shelves, master EQ 6 kHz -3 dB).
- Same-dynamic scan:

  | Dynamic | Family (median minus upper strings) | c49 |
  |---|---|---|
  | f | horns | -2.0 |
  | f | trumpets | -0.1 |
  | f | trombones and tuba | 0.0 |
  | f | winds | -4.1 |
  | p | winds | -0.2 |
  | p | horns | -0.7 |
  | pp | trombones and tuba | -2.4 |

  Each family should land within 1.5 dB of its c49 value.

Do not touch: every c49 balance row (roles, note trims, LEVEL_SHAPES, the c49 B #1-#5 and A #3 rows, the bar-81 timpani row from 322); CC11 and the dynamic table; the 600 ms basses pp cap and the string and horn release caps; the Violins I 5 kHz and trombone 4 kHz cuts; the sample notches (basses 87.3 Hz, tuba 84 Hz, contrabassoon and tuba 70 Hz shelves, tam-tam 86 Hz); the Horns a2 1.25 kHz shelf and 1.6 kHz loud EQ; the Trumpet 1 bar-161 shelves and the Trumpets a2 3.2 kHz bell and coda lift; the Cello solo's Close-only mics; the template's string, brass and wind send levels and return chunks; c49's timpani mics (keep Close 0.2 / Main 0.5, no Surround) and gain -7.

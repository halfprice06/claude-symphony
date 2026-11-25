# Cycle 11, critic C: tempo, timing and transitions (lens C3), on the c10 render

Material: `cycles/c10/render/` (31 stems and `00_Master.wav`), `cycles/c10/build_render/parts.json`, `build/score_config.py`, `build/leg_leads.json`, `build/entry_leads.json`, `build/early_fills.json`, `build/note_trims.json`, `build/global.ily`, `build/mockup-events.tsv`, `tools/score_to_parts.py` (legato lead code around line 3697-3732, `smooth_tempo` at 1345), the c08 stems with `cycles/c09/before/parts.json` for comparison, the c05-c10 `metrics/attacks.txt`, and the c07 C report (this lens on c06).

Methods. "pc" is the perceived attack from `tools/pcx.py attack_pcx`, with the previous sounding pitch's harmonics excluded, in ms from the score onset on the render's tempo map. "Crossover" is `pcx.pair_window`: the time from the score onset at which the new pitch's band passes the old one, on legato joins only. pc misreads a same-pitch repeat (it finds the previous note's attack and reads about -115 ms) and a soft note that swells for 0.5 s (it reads the swell as lateness). I dropped those cases, and checked the large values with the crossover or with the time the note takes to reach 6 dB under its body (body = median level at +0.8..+1.6 s). The harp was measured on its 1-6 kHz onset, because pc on its low notes reads the previous note.

## Manual notes (T1: May 2021 HO manual, PDF pages 143-146 read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.143 controller table: CC5 legato/portamento time (Legato and Portamento scripts only), CC15 con sordino, CC22 true legato mono/poly, CC36 round-robin reset, CC57 / CC65 script on/off, CC69 Repetition, CC70 finger position | every track | Yes. CC15 on Violins II goes on at qn 445.3 and off at 552.5, so the bar 168-196 con sordino starts 56 qn after the switch, with plenty of time. CC22 127 is in the pre-roll (`LEGATO_MONO_CC22`). The round-robin reset is sent on CC16, the CC set in Opus's preferences (2025 p.92 says the reset follows that preference; p.143's CC36 is the factory default). CC70 follows `SUL_SPANS`. CC5, CC57, CC65 and CC69 are not sent; that is right, because the strings and winds play true-legato rows and not the scripts. |
| p.144 Monophonic True Legato: velocity sets the transition time (50-60 looser, 110-127 tighter) and does not change loudness | every legato row; the celli trio tune at v80 (c10 A #4); Violins I's theme-head tails at v88 / v85 | Partly, and here velocity costs timing. Measured on c10: the celli at v80 (bars 169-184) cross at +41 ms median, even with 0.03 s more lead, against +22 ms at v112-118 (bars 209-224). So the slower transition is real, as the manual says. Clarinet 1's tune crosses at +24 ms below v90 and +20 ms at v90 or above, almost no difference. Kit LEARNINGS section 5: on the Violins I KS Master, v108 and v124 gave identical crossovers. Use leads, not velocity, to fix timing (findings 1 and 3). |
| p.144 Legato: monophonic, no significant silence between notes | all slurred lines | Yes: the joins overlap. But the overlap rule caps the lead of a note that follows a short note, and that cap makes the trio tune limp (finding 1). |
| p.145 Repetition script: random detune or a neighbouring sample on each repeat, so a render cannot be repeated exactly. Round-robin reset: the same samples every time | the theme head's repeated eighths, the trumpets' repeated quarters, the timpani motive x, the pizzicato bass of bars 89-100 | Yes, by choice: the render uses RR rows plus `RR_RESET_AT`, which the manual recommends when the result must repeat. The resets at 264 / 273 / 282 / 291 work: the celli's pizz. peaks now repeat once per printed group (finding 5 has the level detail). |
| p.145-146 finger position on CC70 (FP4 = 115-127, warmer, nearer the bridge) | Violins I "sul A" 0-23, 528-538, 1089-1125; Violins II 364-383.5, 839.5-851.5, 1044-1054 | Yes (the c07 C report checked the tables; nothing has changed since). |
| MANUAL-GAPS #12 (reset CC), #2 (repetition rows), #11 (portamento) | see above | #12 is in use. #2 and #11 are not timing items. |

## Findings, ranked by what a listener would gain

### 1. The trio tune's dotted rhythm, the second idea's pickups and the theme head's slurred eighths limp: a legato note after a short legato note arrives 0.1-0.2 s late, because its lead is capped on the unmoved slot (measured; cause read in the code)

Where: the celli's trio tune, bars 169-184 (qn 512, 524, 536, 542, 567, 572); Violins I and II at the return, bars 209-224 (632, 644, 656); the second idea (V1 / V2 134, 146, 362, 372, 374, 840, 842; violas 596, 726); the solo 1052 and 1061.5; Violins I's theme-head tails after the accented half note (41 / 41.5, 53 / 53.5, 71 / 71.5, 77 / 77.5, 287 / 287.5, 761 / 761.5, 773 / 773.5, 791 / 791.5, 797 / 797.5, the `SHORT_SUS_LEG_AT` notes).

What: when a slurred eighth leads into a longer note, the eighth gets its full legato lead (0.17-0.28 s), but the next note's lead is capped at `LEG_CAP_FRAC` (0.75) times the eighth's *score* slot. That is 0.099 s at quarter 228 and 0.085 s at 264. So in MIDI the eighth lasts 0.23-0.33 s and the note after it only 0.03-0.1 s more than written. The cap ignores that the eighth itself was moved early. The eighth lands on time, and the long note after it lands an eighth late, so the tune's dotted rhythm (eighth pickup, long downbeat) comes out even, and the theme head's two slurred eighths come out as a late pair.

Evidence (measured on c10):
- Over all string tracks, 49 legato notes follow a led legato note of 0.5 qn or less. Their pc median is +55..+107 ms per section, against +2..+40 ms for every other legato note. On the crossover the trustworthy ones (window-edge readings dropped) pass at +75..+201 ms, median about +115.
- Trio tune pairs (eighth / long, crossover in brackets where the band check is clean): celli 511.5 -63 / 512 +165 (+191); 523.5 +15 / 524 +271 (+201); 535.5 +10 / 536 +101 (+117); 542 +108. Violins I 631.5 -2 / 632 +150 (+133); 643.5 +23 / 644 +185 (+113); 655.5 +1 / 656 +128 (+137). Violins II 632 +100 (+87), 644 +88 (+75). In the same bars, Clarinet 1 plays the same rhythm at +11..+26 ms (632 +20, 644 +26, 656 +11) and the harp's off-beat chords at +1..+3 ms.
- An eighth at 228 lasts 132 ms, so at 644 the Violins I's pickup lasts about 0.29 s instead of 0.13. The c07 C report measured the same pairs (512 +258, 524 +266, 632 +167, 644 +174). They were deferred in c07 and c08 and are unchanged on c10 (c08 stems: 512 +168, 524 +304, 632 +152, 644 +186). All of them have lead 0.099 s.
- Theme-head tails: the second eighth has lead 0.085 s, the first 0.17 s, so the first eighth sounds for 29 ms in MIDI before the second starts. Measured: first eighth +41..+72, second eighth +63..+89, the staccato quarter after them -2..-67 ms. So at 41.5 -> 42 the second eighth is followed by the quarter 15 ms later instead of 114. On c08 (Sus MAX) the first eighth was on time (+7..+39); the c09 move to legato targets cost about 40 ms on it.

Fix (generic, `tools/score_to_parts.py`, the legato branch at about line 3724): add `LEG_CAP_MOVED = False` to the defaults. When it is on, compute the cap from the previous note's *moved* onset: `pq_ = pv["qn"] - shift.get(id(pv), 0.0); L = min(lead_qn(q, tot), cf_ * (q - pq_))`. Keep `LEG_MIN_GAP_S` (V1 0.06 s, the other sections 0.1 s) as the guard on spacing, as it already is. In `build/score_config.py` set `LEG_CAP_MOVED = True`. Expected (inferred; the kit says the response is not 1:1): celli 512's lead 0.099 -> 0.25 s, 524 -> 0.247, Violins I 632 / 644 / 656 and 41.5 -> 0.17. Then each pickup and its long note are spaced by the written value in MIDI. Re-measure with pcx and the crossover. Targets: every listed long note within +50 ms of Clarinet 1 / Flute 1 where they double, and the second tail eighth at most +30 ms, with the quarter after it 90 ms or more after it. If a few pairs are still over +60 ms after the render, add per-onset `build/leg_leads.json` offsets of +0.04..+0.06. Separately, Violins I and II 144 (the Leg BC MAX note after the Sus MAX pickup 143.5) play with lead 0.000 and reach pc +204 / +200 ms. Give them the string legato lead, or an `ABUT_LEAD` entry at 144.0.

### 2. The soft first notes at the section joints arrive 0.15-0.4 s after the bass and harp that mark the downbeat (measured)

Where and evidence (pc; "body - 6 dB" = time to reach 6 dB under the body; the bass, harp and horn entering on the same beat in brackets):
- Bar 225, the codetta, qn 672 (bass pizz. +17, harp 1-6 kHz onset 0 ms): Oboe 1 dolce +220 (body - 6 dB at +178 ms, lead 0.055 s, v53); Violins II +281 (body - 6 dB at +342 ms, 20 dB under body at +0.05 s, lead 0.12, v41). Violins II at 708 and 738 (bar 237 into the rit.): +272 and +159.
- Bar 341, Meno mosso after the G.P., qn 1020 (Horn 3 -38, basses +6, harp 0): violas +261 (body - 6 dB at +406 ms, 18.7 dB under body at +0.05 s).
- Bar 349, "dolce, solo", qn 1044 (basses +9): Violin I solo +228 (lead already 0.27 s; the c07 extra lead did not move it: c02 +259), Flute 1 "col Vl. solo" +324 (body - 6 dB at +388 ms, 16.6 dB under body at +0.05 s), Violins II "la metà" +137, Violas div +167.
- Bar 121, sub. p, qn 360 (clarinets -11 / -7, Bassoon 2 -8, Horn 2 -1, celli +1): Violins II +129.
- Bar 169, the celli's trio entry, qn 504: celli +263, basses +144 (body - 6 dB at +342 ms). c09's lead increase made these worse and was reverted.
- Bar 3, the horn call (Horn 1 espress.) after the fermata: qn 6 +111, the legato E4 at 9 +155 ms (body - 6 dB at +152 ms; horn legato lead 0.06 s at v100). The celli and basses pizz. and the timpani on the same downbeat sit at +22..+31 ms.

Across the piece, 35 of 418 long, non-short entries after a rest of 0.75 qn or more reach over +100 ms, and these joints hold most of them. At quarter 228 a quarter lasts 0.26 s, so the new section's melody starts most of a beat after its bass. Kit LEARNINGS section 6 explains why: a soft first-note sample starts quiet and grows over 0.3-0.4 s, and lead alone only moves the quiet part earlier. What worked there was an extra lead of 0.06-0.15 s (total under 0.30 s) plus a 3-4 dB fill held 0.3-0.4 s.

Fix (`build/entry_leads.json` extras and `build/early_fills.json` {"db", "pre_s", "hold_s"}):
- Violins II 672, 708, 738: entry +0.12 s; fill 4 dB, hold 0.35 s.
- Oboe 1 672: entry +0.08; fill 3 dB, hold 0.2.
- Violas 1020: entry +0.12; fill 4 dB, hold 0.35.
- Flute 1 1044: entry +0.10; fill 4 dB, hold 0.3.
- Violins II 1044: entry +0.10; fill 3 dB, hold 0.3.
- Violas div 1044: entry +0.08; fill 3 dB, hold 0.25.
- Violin I solo 1044: no more lead; fill 4 dB, hold 0.35.
- Violins II 360: entry +0.08; fill 3 dB, hold 0.3.
- Double basses 504: no lead change (c09); fill 4 dB, hold 0.35.
- Horn 1: `build/leg_leads.json` "Horn 1" 9.0 +0.10 (kit: brass legato 0.10 s worked) and an entry extra 6.0 +0.05.

Apply the auto_fills overshoot rule to every new fill: the 200 ms peak to +0.4 s may not exceed the body by more than 2 dB. Target: each listed note within +80 ms (pc) and reaching body - 6 dB by +0.2 s. The hand-set fills must be excluded from `auto_fills.py`'s next pass (`--exclude`).

### 3. Violins I's legato runs 30-40 ms behind the other string sections, and the probe's median has drifted later every cycle (measured)

Evidence: crossover medians by row on c10, window-edge readings dropped: Violins I Leg Slur MAX +51 ms (n 65; pc +47) and Leg BC MAX +51 (n 28); Violins II Leg Slur +24 (pc +4); violas +19 (pc -3); celli Leg Slur +9, Leg BC +31.

The probe's Violins I legato pc median, c05 -> c10: +22, +18, +34, +37, +43, +49 ms. The probe passes it because it checks the window (64 ms), not the median. Part of the rise is the 18 theme-head tails added in c09 (median +68; finding 1). On the 100 joins common to c08 and c10 the median is unchanged, so the base offset was already there.

In bars 209-224, where all three play the tune, Violins I runs at +30..+60 ms on non-pickup notes, Violins II at 0..+25 and Clarinet 1 at +11..+28. Cause (read): Violins I's Leg Slur MAX gets 0.17 s, while Violins II gets 0.20 + 0.04 (`LEG_ART_EXTRA_S`). Kit section 5 found Leg Slur MAX crossing 0.05-0.08 s later than Leg BC at equal lead and used Leg Slur +0.025..+0.05. Violins I has the extra on Leg BC (+0.05) and none on Leg Slur.

Also on the celli: at v80 (bars 169-184) they cross at +41 ms against +22 at v112-118 (bars 209-224), even with `LEG_VEL_EXTRA_S` celli (85, 0.03). Note for the record: c10's check of this change read "-19 ms" because it called `attack_pcx` without `prev_pitch`, so the previous note's harmonics were counted. With exclusion (`pcx.scan`) the same notes read +39 ms.

Fix (`build/score_config.py`):
- `LEG_ART_EXTRA_S["Violins I"]["Leg Slur MAX"] = 0.035` (Leg BC stays at 0.05).
- `LEG_VEL_EXTRA_S["Violoncellos"]` (85, 0.03) -> (85, 0.06). Keep v80, which is the c10 cantabile choice.

Targets: Violins I Leg Slur crossover median within 15 ms of Violins II's, and the probe's Violins I pc median at +25 ms or less. Celli 506-552 crossover median at +25 ms or less, measured with `pcx.scan`, not bare `attack_pcx`. Apply after finding 1's cap change and re-measure both together, because the tails and pickups are in Violins I's joins.

### 4. "Ritmo di quattro battute" in the reprise: the hemiola's cross-accent at qn 904 comes 0.13-0.19 s early in Violins II and violas (measured)

Where: bar 302 beat 2 (qn 904), the second stroke of the reprise's four-bar hemiola after the sfp, Violins II and violas (`REATTACK_LEAD_AT`).

Evidence (pc; t50 / h10 agree, rise 40-44 dB, so not an estimator artefact):
- 904: Violins II -132 ms (lead 0.20 s; t50 -124, h10 -140), violas -190 (lead 0.25, set by c07 C #3 from +91 at 0.18; t50 -178, h10 -202). Violins I +2 (lead 0.13), Clarinet 1 +4, cor anglais +36.
- A quarter at 264 lasts 227 ms, so the violas' stroke lands nearer the previous eighth than its own beat.
- The neighbouring strokes with the 0.08 s abut lead are within ±50 ms: 906-910 Violins II +31..+47, violas -23..+45.
- The first statement (bars 101-104) has no stroke more than 52 ms off (strings -36..+52 at 302 / 304 / 306).

Smaller, same passage: Horns 1-2 play their tutti quarters on Sus MAX with the 0.05 s brass entry lead and land early at f/ff: Horn 2 -31..-41 ms on most quarters over 306-339, Horn 1 median -14 (down to -46), against the trumpets at -10 and the timpani at 0..+15. That is about a third of an eighth.

Fix (`build/score_config.py`, the c07 `REATTACK_LEAD_AT` lines at about 538-540):
- Violins II 904.0 0.20 -> 0.08; violas 904.0 0.25 -> 0.08 (the abut value of the other strokes).
- Horns: `ENTRY_LEAD_S["brass"]` second value (the loud entry, 0.05) -> 0.02 for "Horn" tracks over 300-340 and 900-1017, as a per-track override.

Target: every hemiola stroke at 902-910 within ±30 ms of Clarinet 1 / Flute 1, and the horns' tutti quarters within ±20 ms of the trumpets.

### 5. "Ritmo di tre battute" (bars 89-100): the pizzicato bass has no weight on the group heads, so the three-bar groups are marked only by the timpani's third bar (measured)

Where: celli and basses pizz. B on every downbeat, qn 264-291; head entries at 89 (violas pp), 92 (Oboe 1 pp) and 95 (cor anglais pp, Violins I p); timpani motive x f at 91 and 94, then every bar from 97.

Evidence: 200 ms peak per bar on the stems.
- Celli 89-98: -50.0 -50.8 -49.2 | -49.4 -50.8 -49.2 | -49.4 -50.8 -49.2 | -49.0. The c07 reset plus the current trims (heads +1.5, second bars -3, third bars -9 against the RR peak) left the three bars within 1.6 dB, and the third bar is the loudest.
- Basses: -46.6 -45.3 -48.8 | -45.3 -45.3 -48.8 | -45.3 -45.3 -48.8. The head is level with or under the second bar.
- Master: head bars -38.6 / -37.1 / -34.2, second bars -41.4 / -43.2 / -34.8, third bars -26.0 / -26.0 / -36.8. The timpani's printed f in the third bar is 10-12 dB over everything, as printed, so the group is audible.
- Nothing marks the printed head bar under the pp entries. The lens asks for downbeat weight every three bars; c07 C #4.2 (head trims) was deferred.

Fix (`build/note_trims.json`, step trims):
- Celli 264.0 / 273.0 / 282.0: +1.5 -> +3.0; the third-bar pizz. 270.0 / 279.0 / 288.0: one more -1.5.
- Double basses 264.0 / 273.0 / 282.0: +2.0 (none now).
- Leave 291 (inside the crescendo into 101) and the timpani as they are.

Target: on each stem the head bar is 1.5-2 dB over both other bars of its group (measured 200 ms peaks).

### 6. The final rit. overshoots the printed 140 in bar 375 (measured; small)

Where: `RAMP_SPANS` (1107, 1125, 228), bars 370-375; `smooth_tempo` in `tools/score_to_parts.py`.

Evidence: printed \mt 210 / 196 / 180 / 160 / 140 for two bars (374-375), then 50. Rendered bar averages: 212.5, 195.7, 179.3, 160.7, 146.6, 133.2, 50. Bars 370-373 are within 1.5 %. Bar 374 runs 4.7 % fast and bar 375 5 % slow (1.351 s against 1.286), because `smooth_tempo` places the two-bar 140 step's anchor at its midpoint (1122) and extrapolates the slope to 127 at 1125. The c07 C report read the same (133). Every other tempo checks against the print:
- bar 2 at quarter 88 (2.045 s);
- the 149-152 rit. 253.4 / 240.5 / 232.5 / 228 into the Trio at 228;
- 237-252 as one curve, 222.5 / 214 / 206.5 / 202, then 199 at 241 rising to 256.5 at 252, Tempo I 264 at 253;
- Più mosso 288;
- G.P. at 96 (1.875 s);
- Meno mosso 228;
- the last bar at 50 (3.6 s).
The 25 `BEAT_STRETCH` breaths are where the c07 list put them.

Fix (generic, `smooth_tempo`): in a non-increasing span whose last printed step lasts two bars or more, end the ramp on that step's value (`anchors.append((e, vb))`) instead of extrapolating. Expected: bar 374 about 148 and bar 375 140. This adds about 0.07 s and keeps the rit.'s last bar at its printed floor before the fermata.

Do not touch:
- The staccato timing of every theme statement and tutti (pc medians: Violins I -9..+3, Violins II -15..-3, violas -3..+9, Flute 1 +2..+12, Oboe 1 -8..-5, cor anglais -11..+3, clarinets -10..+5, trumpets' quarters -16..-10, timpani 0..+15, celli and bass pizz. +2..+7): that is `STAC_LEAD_S`, `PIZZ_LEAD_S`, `STAC_LEAD_SPIC` as set.
- Clarinet 1's trio tune (+16 / +17 ms, IQR ±7) and the harp's off-beat chords with no lead (1-6 kHz onset +1..+3 ms).
- Keyswitch placement (1,261 keyswitches; 5th percentile 6.8 ms before their note, none under 3 ms).
- `RR_RESET_AT`; CC15 timing on Violins II.
- The tempo map's printed steps and the 149-152 and 237-252 ramps.
- The tutti attack spread as it is (p10-p90 48-74 ms at 300, 306, 900, 1005-1014; do not add a seeded spread).
- `TIMP_DAMP_AT` and the G.P. cut-offs: the last chord (qn 1014) falls 20 dB at +157..+212 ms in the winds, +252..+512 in the strings and +94..+224 after their printed end in the brass.

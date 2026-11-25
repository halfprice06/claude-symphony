# Critic C, cycle 7 (tempo, timing and transitions), on the c06 render

Lens: the tempo map against the printed tempos and steps, attack timing (S2), keyswitch leads, note starts between sections, phrase ends and tutti cut-offs, breaths, the final fermata. The coordinator added three tasks: measure the c06 tails on the master (Dan: too wet and mushy), choose a fix (the Spaces II IR envelope or other Spaces II parameters vs Duc's single hall), and evaluate the tutti entry spread and the per-track early shifts against our lead tables. Two later notes were folded in: the Duc hall details (Movement I's `tools/make_template_mix.py` "R Duc" return and "duc" send profile; it is there, not in its `build_reaper.py`, which only reads `send_profiles`), and research batch 5 (BRIEF end; FINDINGS Part 5, commit c1cc028d).

Data: `cycles/c06/render/` (stems after the stem fix, return stems 32-35), `cycles/c06/rendered_build/parts.json`, the c05 master. Scratch scripts are in `/private/tmp/claude-501/mockup-loop/mvt3-c07-C/` and are deleted when this report is done.

## Manual notes (MANUAL-READING: c7 C re-reads the c3 C row, May 2021 HO manual p.143-149; c03 report's table checked against c06)

| Manual (PDF page) | What it says | Where in this mockup | Followed now? |
|---|---|---|---|
| p.143 | The CC table: CC5 legato/portamento time (emulated scripts only), CC15 con sordino, CC22 mono/poly, CC36 RR reset, CC57/65 legato/portamento scripts, CC69 repetition, CC70 finger position. | parts.json: cc15 has only a 0 at qn 0 on 5 string tracks; cc70 and cc36 lanes are empty (0 points); cc7 is used on the timpani (242 points). No CC5/22/57/65. | Yes, unchanged since c03. CC5 does nothing for true-legato patches (p.144 note). Read. |
| p.144 | True legato: velocity sets the transition time (50-60 slower, 110-127 tighter), not loudness. | Legato notes at v124 on strings (85-86 % of notes at 110 or more) and horns/trombones; woodwinds v100; Trumpet 1 v96. | Yes for now. **New risk:** the c07 plan item "legato velocity follows the dynamic" lowers these velocities, which lengthens transitions and makes joins late (finding 6). Read + measured. |
| p.145 | The Repetition script randomises; RR Reset (CC36) makes playback repeat identically. | Opus `Preferences.json` still reads `"RoundRobinResetCC": 16`, and nothing sends CC16. | Not fully (MANUAL-GAPS #6, still open). Movement I measured timing as repeatable, so it is not ranked. Send CC16 127 in the pre-roll next to CC36 the next time every track is rebuilt anyway. Measured. |
| p.145-146 | Finger position on CC70; FP4 is the warmest; a rebuilt track defaults to FP4. | cc70 empty, so every string section plays FP4 after the c06 full rebuild. | This affects colour, not timing. Nothing to apply. Read. |

MANUAL-GAPS items that touch timing: #2 (repetition rows) would move repeat attacks, so re-measure S2 if it is tried; #8 (slower legato velocity on cantabile lines) adds to finding 6.

## State through this lens (measured)
- **Tempo map.** It equals the printed tempos and the eight `RAMP_SPANS`. PHRASE_ARCS, TEMPO_PUSH, CAESURA and BEAT_STRETCH are all empty. 46 of 558 half-note beats (8 %) carry a tempo change, all inside the printed ramps. No beat is more than 15 % slower than its local (9-beat) median except one ramp beat.
- **Hammered tutti.** These still sound together. Perceived attack (pcx) minus the brass at the same onset: Più allegro R, strings -5 / -15 ms and timpani +3; coda N, strings +4 / -5 and timpani +18.
- **Keyswitches.** No change since c03; all precede their notes.

## Findings, ranked by what a listener would hear

### 1. The template returns make every cut-off and soft end ring 0.2-0.3 s longer. Fix: the IR envelope on the returns, batch 5's register sends and returns 3 dB lower (measured + simulated)
Where: the whole piece. Clean tutti cut-offs at 1.76 s (bar 2), 7.42 s (bar 6), 36.16 s (bar 26, end of A), 373 qn (bar 94), 661 qn (bar 166) and the final chord's cut-off at 421.55 s (bar 279). Soft string ends at qn 198.88, 454.86, 455.86, 477, 679.86.

Evidence. Times are measured on the master (30 ms RMS, 10 ms hop), for the six cut-offs in the order above. "−20 dB" is the time to fall 20 dB below the level of the last 0.25 s before the cut-off.

| file | −10 dB (s) | −20 dB (s) | median −20 | drop at +0.3 s (dB) |
|---|---|---|---|---|
| c05 master | 0.19 0.24 0.25 0.35 0.36 0.31 | 0.47 0.52 0.43 0.61 0.54 0.49 | 0.51 | 14 13 14 7 7 9 |
| **c06 master** | 0.37 0.42 0.43 0.54 0.44 0.37 | 0.74 0.79 >4 0.87 >4 0.76 | **0.78** | 7 6 5 2 3 6 |
| c06 dry stems only (01-31) | 0.18 0.23 0.28 0.34 0.35 0.30 | 0.39 0.43 0.41 0.57 0.52 0.42 | 0.42 | 16 14 11 7 7 11 |

- c05 and the references fall 20 dB in 0.41-0.55 s. c06 needs 0.74-0.87 s, and at two cut-offs it never falls 20 dB before the next entry. The 0.3 s drop fell from 13-14 dB to 5-7 dB (target at least 13).
- The dry stems alone (the Main mics already carry the hall) fall 20 dB in 0.39-0.57 s. So everything past that comes from the returns.
- Soft ends, measured on each string stem plus the R Strings stem as in c06's wetsum06: Violins I pp-mp fall 10 dB in 0.47 s, Violins II in 0.65 s, Violas in 0.81 s. The references take 0.20-0.40 s; the dry stems take 0.09-0.24 s. qn 454.86 never falls 10 dB on the c06 master. On the master, the other soft ends are covered by parts that are still playing, so the per-section stem plus return is the usable measure there.
- Mush: the master's 100-250 Hz share is −5.6 dB in c06, against −8.9 in c05 and −8.7 for the c06 dry stems. The returns alone add 3 dB to the low-mid band, because they take full-range low instruments and their ReaEQs only high-pass at 87-100 Hz. Whole-piece return energy is only 2.9 dB under the dry sum.

Simulation (measured on the c06 stems; inferred for REAPER). I estimated each return's true-stereo 2x2 impulse response by Wiener deconvolution of the return stem against the sum of its senders' stems. Each send is a fixed post-fader gain, so this is exact up to noise: re-convolving reproduces the four return stems to −24..−28 dB error. The estimated IRs fall 10 dB in 0.34-0.37 s and 20 dB in 0.69-0.76 s, with EDT-range T(−5..−25) = 2.1-2.5 s. I then rebuilt the master with changed sends and IRs.

The IR envelope was modelled as a linear fade from the IR start to endPos x IR length ("model B"). This is the model that reproduces Movement I's measured Opus result: T(−5..−25) ratio 0.74 against Movement I's 1.71/2.25 = 0.76. Fading only the last half of the kept part (ratio 0.90) does not reproduce it.

| variant (all on the c06 data) | return − dry energy | −20 dB median (s) | −10 dB (s) | drop at 0.3 s, clean cuts | soft ends −10 dB, Vln I / II / Vla | 100-250 Hz share |
|---|---|---|---|---|---|---|
| V0 c06 as rendered (reconstruction) | −2.9 dB | 0.74 | 0.35-0.53 | 7 6 5 6 | 0.43 / 0.55 / 0.53 | (−5.6) |
| V1 IR envelope only (envelopeMode 2, endPos 0.5, decayLength 0.5) | −3.7 | 0.64 | 0.34-0.49 | 8 7 6 7 | 0.38 / 0.38 / 0.38 | |
| V2 batch-5 sends only | −7.9 | 0.65 | 0.32-0.44 | 9 7 8 9 | | |
| V3 batch-5 sends + envelope | −8.7 | 0.56 | 0.31-0.42 | 10 8 8 10 | 0.30 / 0.33 / 0.37 | |
| **V3 with every return fader −3 dB** | −11.7 | **0.51** | 0.29-0.39 | 12 10 9 10 | (shorter still) | −8.1 |
| V4 = V3 −3 dB + 2 kHz low-pass on the returns + 25 ms pre-delay | −11.9 | 0.53 | 0.27-0.41 | 12 10 10 10 | 0.30 / 0.33 / 0.34 (at V3 level) | −8.2 |
| V5 batch-5 sends + low-pass + pre-delay, no envelope | −8.1 | 0.66 | 0.31-0.46 | 9 8 8 9 | | |
| V6 Duc-style single hall (approximation, see below) at V3's level | −8.7 | 0.51 | 0.29-0.37 | 11 9 10 8 | 0.27 / 0.32 / 0.33 | −7.9 |
| V6 −3 dB | −11.7 | 0.48 | 0.26-0.36 | 13 10 10 9 | | |

Here "batch-5 sends" means: violins, violas, celli, horns, trumpets and the upper woodwinds at −10 dB; basses, trombones, bass trombone, tuba, bassoons and contrabassoon with no send; percussion and harp unchanged.

Reading:
- No single change is enough. The envelope alone gives 0.64 s and the register sends alone 0.65 s. Together, with the returns 3 dB lower, the master reaches c05's 0.51 s and the 0.3 s drop rises to 9-12 dB. That is not quite the 13 dB target, but the dry stems themselves only reach 11 dB at two of the cuts.
- The register sends also fix the low-mid build-up (100-250 Hz −5.6 → −8.1 dB, inside the references' −6.6..−8.8).
- The 1.8-2.3 kHz low-pass and the 25 ms pre-delay do nothing for the length (0.51 → 0.53 s): the return's energy is low-frequency and the low-pass removes 0.2 dB of it. They are a colour choice, not a fix for mush. Keep them as the A/B batch 5 asks for, not as the clarity fix.
- Duc's single hall reaches the same decay at a 3 dB higher wet level, so more audible room for the same clarity. But V6 is only an approximation. The Hollywood Scoring Stage IR is encrypted (`.eird`), so I reshaped the estimated strings IR to RT 1.6 s (the 2.3 s preset scaled by our IRs' measured 2.3/3.3 ratio) and applied the 184 Hz HP and 3 kHz LP before the hall. The approximation does not justify replacing the template returns before the measured template-based fix is tried.

Fix (actor, c07):
1. Port Movement I's `template_mix.spaces_set` and the `"set"` field of its `resolve_fx` (`symphony/mvt1/reaper-v621/tools/template_mix.py` lines 181-273) into `tools/build_reaper.py returns_job`. Then give every `build/mix.json` "returns" entry `"set": {"irSetup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}}`.
   - The Spaces II chunk's `irSetup` is the same class `ConvolutionSetup` with the same keys as the Opus reverb Movement I measured (decoded from all six template VERB chunks: envelopeMode 0, endPos 1.0, decayLength 0).
   - Read the state back after the build, as Movement I's verify step does (template_mix.py lines 422-424).
2. Sends by register (batch 5 item 1), as track-level `"return"` keys in mix.json (`mix_for` lets a track key override its group):
   - Violins I, Violins II, Violas, Violoncellos: {"to": "R Strings", "db": −10}.
   - Double basses: "return": null.
   - Horns 1-4 and Trumpets 1-3: {"to": "R Brass", "db": −10}.
   - Trombone 1, Trombone 2, Bass trombone, Tuba: null.
   - Flutes, oboes, cor anglais, clarinets, bass clarinet: {"to": "R Winds", "db": −10}.
   - Bassoon 1, Bassoon 2, Contrabassoon: null.
   - Timpani, crash, bass drum and harp unchanged.
   - `sends_lua` already turns a null "return" into an empty send list. Check that the track job then removes the send that the c06 build left in REAPER: read the send count back. If it does not, use db −60.
3. Return faders 1.03 / 1.03 / 1.03 / 0.66 → −1.97 / −1.97 / −1.97 / −2.34 dB.
4. Checks on the c07 master:
   - cut-offs at 1.76, 7.42, 36.16 and 421.55 s fall 20 dB in 0.45-0.55 s, with the 0.3 s drop at least 11 dB;
   - string stem + R Strings soft ends fall 10 dB in 0.20-0.40 s;
   - 100-250 Hz share −7..−9 dB;
   - whole-piece return minus dry energy about −12 dB.
   If the −20 dB median is still over 0.6 s, switch to the Duc fallback: Movement I's "R Duc" return and "duc" send profile from make_template_mix.py (Spaces II "Hollywood Scoring Stage TS RR 2.3s", HP 184 / LP 3000 before it, 12 ms pre-delay, fader −5.5 dB), with batch 5's register sends in place of Duc's −1.6 dB celli/basses. Match its wet level by measurement to about −9..−12 dB return/dry energy: the preset's own wet value (0.051) is far below the template chunks' 1.0, so −5.5 dB is not a transferable number.
5. The A/B for the 2 kHz low-pass + 25 ms pre-delay can go in the same build as a ReaEQ band on the return (it does not change timing). Judge it on brightness, not on the decay.

### 2. Upper strings attack 40-85 ms late in the closing group, the Maestoso chorale and the final Largamente (measured)
Where: F (qn 328-392), P (888-936), T (1088-1116). Violins I, Violins II, Violas.

Evidence. Perceived attack from tools/pcx.py attack_pcx, harmonic bands, rise at least 6 dB, at tutti onsets (8 or more tracks), relative to the score beat. The estimator's zero for instant attacks is about +5..+11 ms (harp +6, timpani +14 here).
- Upper strings minus brass at the same onsets: F +39 ms, P +49, T +41. Every other section is −18..+11 (A-B −8, K −18, N +4, O +7, R −5). The same three sections were late at c03 (+51 / +44 / +37), so the c03 and c04 lead changes did not reach them.
- By row:
  - Sus MAX with no lead at all in P and T: Violas P 7 notes +75 ms (lead 0), Violas T 6 notes +67 ms (lead 0), Violins II P 3 notes +85 ms (lead 0).
  - Sus MAX with a 0.06 s lead that is too small: Violins II F 20 notes +62 ms, Violas F 35 notes +56 ms.
  - Tremolo: Violins II T 10 notes +84 ms (lead 0.03 s), Violins I T 7 notes +46 ms (lead 0.06 s).
- At 2 = 56-72 a 60-85 ms lag is under a sixth of a beat, but it falls on the chorale's and the final chords' downbeats, against brass and timpani that are on the beat. Dan's S2 rule calls 40 ms audible.

Fix:
- In `build/score_config.py`, add a Sus MAX lead for the slow sections (the generic short-Sus lead 0.06 s applies only to short notes). Use `ROW_LEAD_S` per track and row: Violins I, Violins II and Violas "Sus MAX" 0.07 s within qn 888-936 and 1088-1116. If ROW_LEAD_S has no span form, add one (a list of (from_qn, to_qn, s)), a generic tool change with a default of none.
- In F (328-392), raise the Violins II / Violas Sus MAX lead from 0.06 to 0.11 s.
- Raise the tremolo entry lead (c03's 0.08 s tremolo entry rule) to 0.12 s on Violins II and 0.10 s on Violins I in T.
- Check with pcx on c07: upper strings minus brass within ±20 ms in F, P and T.

### 3. Do not add the seeded 36-55 ms tutti entry spread: our perceived spread is already 117-183 ms first-to-last (measured)
Where: every tutti onset (434 onsets where 8 or more tracks attack; 430 measured).

Evidence:
- Perceived attack spread across tracks per onset: median first-to-last 142 ms (IQR 98-190), p10-p90 85 ms. By section, first-to-last / p10-p90:

  | section | first-to-last (ms) | p10-p90 (ms) |
  |---|---|---|
  | R | 117 | 83 |
  | N | 128 | 75 |
  | F | 133 | 70 |
  | K | 136 | 76 |
  | A-B | 141 | 87 |
  | J | 142 | 72 |
  | P | 168 | 104 |
  | O | 181 | 113 |
  | Q | 181 | 119 |
  | T | 183 | 93 |

- Our MIDI note-ons are spread 170 ms (IQR 120-240) by the per-track leads, which exist to bring the slow sample attacks onto the beat.
- The expert files' 36-55 ms is a note-on spread for played-in tracks (Howl's 32 ms median, Mulan 8 ms). Their perceived spread cannot be smaller than that.
- Some of our 85 ms p10-p90 is estimator scatter. But the family medians differ by up to 49 ms in the slow sections (finding 2) and by 12-24 ms for the woodwinds everywhere (woodwinds minus brass −12..−24 ms in A-B, K, N, O, R, T). The ensemble is already looser than the research target.
- Adding a seeded ±18-28 ms per section would push the p10-p90 toward 100-120 ms in the fast sections, and Dan's standing complaint is smear.

Fix: record the item as measured and not adopted in loop/LEARNINGS.md, with these numbers ("dropped only with measured evidence"). Spend the effort on bringing the spread down instead: finding 2, finding 4, and the woodwinds' −12..−24 ms early bias (reduce the woodwind ENTRY_LEAD_S / LEG_LEAD_S by 0.015 s on Oboe 1, Clarinet 2, Bassoon 2 and Contrabassoon, below). Revisit a spread only when the measured p10-p90 is under 50 ms.

### 4. Per-track early shifts: our leads already sit inside the research ranges; correct the per-track residuals instead (measured)
Evidence. Median MIDI lead per track (all notes) against the research shifts, and the median perceived attack at tutti onsets (zero is about +8 ms):

| track | our median lead (ms) | research shift (ms) | perceived attack at tutti (ms) |
|---|---|---|---|
| Flute 1 / 2 | −30 / −50 | −75 | +7 / +9 |
| Oboe 1 / 2 | −50 / −120 | −27 | −8 / **−31** |
| Clarinet 1 / 2 | −50 / −35 | −38 / −46 | **+19** / +9 |
| Bass clarinet | −35 | −17 | −6 |
| Bassoon 1 / 2 | −35 / −35 | −40 / −85 | −4 / −14 |
| Contrabassoon | −35 | | **−29** |
| Horns 1-4 | −50..−90 | | +14 / **−15** / +15 / +12 |
| Trumpets 1 / 2 / 3 | −50 / −80 / −70 | | **+25** / +14 / +14 |
| Trombone 1 / 2 | −50 / −50 | | **+21** / **+22** |
| Bass trombone / Tuba | −50 / −70 | | −3 / +2 |
| Violins I / II, Violas | −60 | | +9 / +10 / +12 |
| Violoncellos | −120 | | **+20** |
| Double basses | 0 | | +5 |
| Timpani | +20 (TIMP_DELAY_S) | 0 | +14 (zero) |

- Strings and brass research range: −20..−120 ms; percussion on the grid.
- Every lead is inside the research range. The research shifts are fixed per track in libraries with other latencies, so ours, fitted per note on measured attacks, should stay.
- What the data does show is per-track residuals of 15-40 ms against the zero: Oboe 2 and the contrabassoon early by about 37 ms; Trumpet 1, Trombones 1-2, celli and Clarinet 1 late by 11-17 ms.

Fix (score_config.py; small, measured on 89-374 notes each):
- Oboe 2 ENTRY_LEAD_S (0.0, 0.14, 0.0) → (0.0, 0.11, 0.0).
- Contrabassoon: 0.03 s less lead. Its lead is the wind default, so add "Contrabassoon": 0.005 to ENTRY_LEAD_S / LEG_LEAD_S, or a −0.03 s offset.
- Horn 2 ENTRY_LEAD_S middle value 0.08 → 0.06.
- Trumpet 1 +0.015 s (ROW_LEAD_S "Sus" rows outside the mute span).
- Trombone 1 (0.06, 0.07, 0.05) → (0.06, 0.09, 0.05) and the same for Trombone 2.
- Clarinet 1 entry +0.01 s.
- Keep the timpani, crash and bass drum as they are.
- Re-measure with the same spread script logic (pcx at tutti onsets); the target is every track within ±15 ms of the timpani's value.

### 5. The tempo map has no breaths: 8 % of beats change against the research's 19-20 %, and no phrase-end beat is over 15 % slower (measured; the shapes are inferred from the score)
Evidence:
- 46 of 558 half-note beats change tempo, all in printed ramps, and 1 beat is more than 15 % slower than its local median. Mulan and Howl's (FINDINGS Part 5, section 16) change tempo on 20 % / 19 % of beats, with 20 / 26 beats more than 15 % slower than the local median (the breaths). Duc's Adagietto does the same.
- The Finale has seven large entries straight after a rest in every part (parts.json: 10 or more tracks enter, at most 3 sounding in the 0.4 qn before): qn 72 (bar 19), 104 (27, the ff counterstatement), 392 (99, development), 632 (159), 664 (167), 816 (205, start of the accelerando), 1108 (278, the final crash chord). Each lands exactly on the metronome now.
- The lyrical sections have regular 4-bar phrases with no shaping: the second theme D/E (qn 200-324), its recapitulation L-M (680-784), Q molto cantabile (936-976), and the Largamente O (840-880).

Fix (build/score_config.py; the tools exist from Movement I: CAESURA, PHRASE_ARCS, TEMPO_PUSH):
- `CAESURA = {72.0: 0.06, 104.0: 0.08, 392.0: 0.08, 632.0: 0.06, 664.0: 0.06, 816.0: 0.05, 1108.0: 0.10}`. At 0.25 qn before each entry, 0.06-0.10 s extra makes that quarter 40-110 % longer; it is the breath. The hammered passages themselves stay metronomic.
- `PHRASE_ARCS`:
  - (200, 216, "sub"), (216, 232), (232, 248, "sub"), (248, 264, "main"), (264, 280, "sub"), (280, 296), (296, 312, "sub"), (312, 324, "open");
  - (680, 696, "sub"), (696, 712), (712, 728, "sub"), (728, 744, "main"), (744, 760, "sub"), (760, 776), (776, 784, "open");
  - (840, 856), (856, 872, "main");
  - (936, 952, "sub"), (952, 968, "main"), (968, 976, "open").
- No arc may overlap a RAMP_SPAN: the tool skips them, and (312, 324) and (776, 784) end where ramps start, so they are "open".
- Leave the Allegro sections without arcs (S2, Dan's beat rule).
- Expected effect: about 60 more changed half-beats, which puts the share near 19 %. Each "main" arc's last quarter is 12 % slower (PHRASE_SLOW_MAIN 0.88).
- Check after the build:
  - tempo shaping total +1..+3 s (the tool prints it);
  - re-run `space_rebows.py` for any held string note inside a changed arc (the rebow loop spacing is in seconds);
  - no arc may end where a ramp starts with a rising tempo (the tool warns).

### 6. The c07 "legato velocity by dynamic" change will make legato joins late unless the leads are refitted (inferred from the manual, measured baseline)
Where: every legato row, mostly the strings (259-331 legato notes per section at v124) and horns/trombones (v124).

Evidence: the HO manual p.144 says velocity 50-60 gives a longer legato transition and 110-127 a shorter one. The per-onset `leg_leads` and string per-onset leads were fitted at v124 (c04 C #4). The c06 celli joins are on time (pcx median +10 ms, SD 40 ms). Research batch 4 says legato velocity follows the dynamic (r about 0.35, median 90 or more).

Fix:
- Map the dynamic into 96-124 (pp 96, p 102, mf 112, f-ff 124), not lower, on the string and brass legato rows.
- Add the matching lead from `LEG_VEL_EXTRA_S` (the list form exists): about +0.03 s at v96-105 and +0.015 s at v106-115 on strings. This is the same mechanism c04 used for the woodwinds.
- Run `tools/pcx.py` on the c07 render: string join median within ±20 ms and SD no worse than c06's 40 ms. If a section's join median moves late by more than 25 ms, raise that section's extra before c08.

Do not touch: the printed tempo map and the eight RAMP_SPANS (exact); the hammered tutti alignment (R, N); percussion on the grid (crash / bass drum delay 0, TIMP_DELAY_S 0.02); keyswitch timing; the per-dynamic string release caps (the dry stems' cut-offs, −20 dB in 0.39-0.57 s, are already at the reference); the per-note string leads outside F/P/T; the template returns' IRs, pre-delays and EQ chunks (only the envelope, sends and faders change).

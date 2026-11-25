# Cycle 8, critic B (balance and levels): the c07 render

Under review: `cycles/c07/render/` (31 dry stems, the four return stems 32-35, `00_Master.wav` = their sum) with `cycles/c07/rendered_build/parts.json` and `mix.json` (identical to `build/`). Method: every stem was transformed (4096-point STFT, 25 ms hop, stereo power) into A-weighted and K-weighted (BS.1770) frame levels and the bands 30-150, 60-250, 100-300 Hz, 0.3-1, 1-2, 2-5 and 5-12 kHz. Each return's frame power was split between the tracks that send to it, in proportion to their smoothed dry power times their send gain (the c07 `bal07.py` idea, done per frame). "Sounding level" means the mean over frames inside the track's notes, from the score onset + 50 ms to the note end, so rests do not lower it. The c07 balance checks averaged whole passages including rests (for example "harp minus Vln I 123-134" compared the harp with a section that rests most of that span). Simulations are level-only arithmetic on these frames. That is exact for an envelope change, because the REAPER envelope sits before the post-fader send, so dry and return move together. A-weighting and K-weighting disagree by up to 9 dB on low instruments (celli at p: 8.7 dB A, 17.4 dB K), so I rank only problems that show in both and give both numbers. Score pages read: 7 (bars 115-143) and 13 (bars 223-238). Scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c08-B/` (deleted).

## Manual notes (second reading of row c2 B: May 2021 HO manual, PDF pages 194-200, Chapter 6 "Mix"; cycles/c02/reports/B.md re-checked; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies now | Followed? |
|---|---|---|
| p.194, p.196: each instrument has a master channel and one sub-mixer channel per mic. Each channel has volume, pan and a load button, and loading a mic loads its samples. | Since c06 the mics follow the EW template: strings Close 0.5 / Main 1.0; brass Close 0.31-0.48 / Main 1.0; winds Close-led (Close 0.78-0.94, Main 0.09-0.53); timpani Close 0.2 / Main 0.5 with no Surround. Harp: Close 0.6 / Main 1.0. | Yes, except the harp (read). The plan's item 1 gives the harp Close 0 dB, Main -9 dB and Mid 0 dB. Ours has Main 4.4 dB **over** Close and no Mid. This bears on finding 2, where the harp covers the cello melody. In c02, nothing needed a mic change for balance; now the harp does, at least as a test. |
| p.195: Store / Restore Mix. | Not used. The pipeline writes the whole state. | Not applicable. |
| p.196: FX Bus channels, fed by Reverb Send inserts on the sub-mixer channels. | Opus's FX bus is off (`opus_off`). The hall is on the REAPER Spaces II returns. | Yes, per the plan (read). c02's note that "the strings are the driest family" no longer holds. Strings, horns, trumpets and upper winds all send at -10 dB, and low strings, low brass and bassoons send nothing. |
| p.198: an Effects Send has a level and a Post switch, and post-fader is typical for reverb, "to have the same level of signal present in the main mix as being sent". | The REAPER sends are post-fader, after the track's volume envelope (roles, trims, soft trims). | Yes (read, measured). A role scales a track's dry sound and its hall feed together, so every fix below is level-only and keeps the depth. Since the hall rings on the return track, an envelope drop no longer cuts the tail (c07 B, p.151 row). S3 still applies to the dry sound. |
| p.199-200: Opus insert EQs. Bass Comp boosts 32-256 Hz; the 3-band Channel Equalizer and the 6-band Equalizer cover 30 Hz-18 kHz with gains of +24/-60 dB. | The mockup uses ReaEQ (family EQ, track EQ, loud_eq) before the REAPER send, which is the same position in the signal chain as an Opus insert on the mic channel. | Equivalent (read). Nothing here needs a low boost: the master's 100-250 Hz share is -8.5 dB (references -6.6..-8.8). If the tuba cut in finding 5 is adopted, ReaEQ can make it. Opus's EQ adds nothing ReaEQ lacks. |
| MANUAL-GAPS #4 (Mid mics) | The EW layout made the winds Close-led, which settles most of this item. The harp is the one place where the template itself uses a Mid mic. | Open for the harp only (finding 2, second option). |

## 1. Chorale bars 224-225 (qn 892-900): the Violins I mf tremolo is as loud as the f brass chorale, and the horns sit 4-7 dB under the trumpets and trombones (measured)

Where: qn 892-932, Violins I and Horns 1-4 against Trumpets 1-2 and Trombones 1-2. Page 13: the brass chorale is printed f; Violins I play a mf tremolo on C6, and violas, celli and basses are f.

Evidence. Sounding levels per bar, K-weighted (A-weighted in brackets):
- qn 892: Trumpet 1 32.8 (31.4), Trombone 1 32.7 (30.1), Violins I 33.2 (31.1), Horn 1 28.6 (26.0).
- qn 896: Trumpet 1 35.5 (34.0), Trombone 1 35.6 (34.1), Violins I 33.1 (31.0), Horns 1-4 28.2-30.2 (25.2-25.7).
- qn 900-928: the horns stay 2-7 dB under Trumpet 1 and Trombone 1. Horn 3 drops to 25-27 K at qn 904-924.

The printed balance puts the mf accompaniment under the f chorale. Instead, the Violins I tremolo matches the chorale's top voice and sits 4-5 dB over every horn. By Rimsky-Korsakov's resonance table, one horn is half a trumpet at f (-3 dB). Here the horns are 4.5-7 dB under. Over the whole piece at f, horn minus trumpet is -5.1 dB A and -3.2 dB K, so the chorale is the worst place. The c07 check (brass minus strings +5.3 dB) passed only because it summed eleven brass tracks against all five string sections.

Fix (`build/roles.json`, level only, no CC change):
- Violins I: `[892.0, 899.9, -4.0, 0.25]`. The tremolo chord changes to the ff "unis., change bow" line at 899.94, and the row's built-in ramp-in from 891.5 falls on the decaying end of the fff chord. Result: Violins I 29.1-29.2 K, 3.6-6.4 dB under Trumpet 1.
- Horns 1-4: `[892.0, 928.0, +2.0, 4.0]`. The 4 qn end ramp runs over the printed decrescendo of bars 232-234, so no step falls under the held chord (S3). Result: horn minus trumpet about -3 dB, the norm. Leave Horn 4 (+3.5 dB fff/ff trims) at +1.0 if its 896-928 level goes over Horn 1's.

Check on the render: per bar, Violins I 4-6 dB under Trumpet 1 at 892-899, and Horns 1-3 within 2-4 dB under Trumpet 1 at 892-928, in both weightings.

## 2. Bars 123-124 (qn 488-496): the celli's "espress." melody is covered by the harp's p arpeggios (measured)

Where: Violoncellos (arco, espress., sul D, p), Harp (p, low G-major arpeggios G2-G3), Double basses (pp). Page 7. The BRIEF's "harp solo in G major" is this accompaniment figure; the tune is in the celli.

Evidence. Sounding levels at qn 488-495: celli 11.2 A / 14.7 K, harp 12.6 A / 20.7 K. The accompaniment is 1.4 dB (A) to 6.0 dB (K) over the melody. Over bars 123-128, the celli sit 13-14 dB under the sum of the other tracks in both weightings, under the rest in 92-100 % of 2-qn windows. The harp is not too soft anywhere else: in bars 67-82 it sits 6-9 dB under the violins' F2 tune, which is right for an accompaniment. At p the harp's median is 14.6 dB A / 22.0 dB K, level with the p winds (17-20 A). The celli at p are at 8.7 A / 17.4 K.

Fix:
- `build/roles.json` Harp `[488.0, 496.0, -4.0, 0.25]`, as a step on the attack per the kit's plucked-note rule (start 0.03 s before the 488 onset). Or put the same -4 dB in `build/note_trims.json` on the harp onsets 488-495.5.
- `build/roles.json` Violoncellos `[488.0, 495.9, +3.0, 1.0]`. The 1 qn release runs into the dolce pp at 496.
- Arithmetic result: melody minus harp -1.4 -> +5.6 dB A and -6.0 -> +1.0 dB K.
- Second option, if the harp still reads as close: set the harp's mics to the template's (`build/mix.json` Harp `"mics": {"Close": 1.0, "Main": 0.35, "Mid": 1.0}`). This is an Opus state change (full rebuild, Mid adds memory), so try it only in a pass-2 test.

## 3. Brass accent brightness: the 2-5 kHz "jump" p90 of 5.2 dB measures accents after rests, not bright accents. Do not add a brass EQ cut (measured; a rejection with numbers)

Where: the 98 brass accent and marcato onsets in `mockup-events.tsv` (`cycles/c07/actor_scripts/accjump07.py`). Coordinator item: "propose exact EQ values".

Evidence:
- Reproduced: on the master, median -3.4 dB and p90 5.1 dB (c07 CHANGES: 5.2).
- The metric compares the first 80 ms after the onset with the 200 ms before it. 37 of the 98 accents follow a rest or a CAESURA: the 200 ms before them is more than 6 dB under the note body. The ten largest jumps include qn 104, 632 and 816 (caesura points, +11.4 / +12.7 / +14.2 dB) and 524. At five of the jumps over 2 dB, the stem that rose most was Violins I or the harp, not a brass track.
- On the 61 accents that follow sounding music, the same metric gives median -3.9 dB and p90 **-1.9 dB**. The target (under +2) is met.
- Against the body, which is the BRIEF item 4 measure (2-5 kHz over 0-80 ms minus 100-350 ms), the master gives median -8.2 dB and p90 -3.7 dB. Per brass stem over 329 accented notes: median -12.1 dB, p90 -4.6 dB, with every instrument's median between -7.3 (Trombone 1) and -16.5 dB (Horn 3). Horn 4's p90 of +15.8 dB comes from short notes, whose body window falls past the note end. No brass stem has a front brighter than its body.
- EQ simulated on the c07 stems (brass tracks plus R Brass, applied as the RBJ response to each window's spectrum), on the old metric:
  - 3.2 kHz -3 dB (1 octave): p90 5.1 -> 4.4.
  - 3.2 kHz -4.5 dB: 4.0.
  - 2.8 kHz -4 dB (1.5 octaves): 3.8.
  - 3.2 kHz -6 dB (1.2 octaves): 3.5.
  - 821 Hz bell -7.8 -> -4 dB: 5.5 (worse).
  - No static EQ reaches +2, because the jump comes from entries after silence. Any of these cuts would dull every brass note to fix a number that does not describe the accents.

Fix:
- Keep the brass family EQ (821 Hz -7.8, 475 Hz -5.4, shelf +2).
- Change the check in the next actor's copy of `accjump07.py`: measure 0-80 ms against the body (100-350 ms after the onset), or skip accents whose 200 ms pre-window is more than 6 dB under the body.
- Record the rejection in `loop/LEARNINGS.md` with the numbers above.

## 4. Bars 119-122 (qn 472-486): the bassoon solo's pp companions are as loud as the p solo (measured)

Where: Bassoon 1 (solo, espress., p), Violins I "4 soli" pp (qn 473-476, 485-487), Clarinet 1 "1. pp < >" (qn 481-485, D6 / C♯6). Page 7.

Evidence. Sounding levels per quarter:
- Violins I soli at 473-476: 16.0-17.7 A against the bassoon's 14.8-18.0 A (K: 18.1-19.8 against 17.7-21.2).
- Clarinet 1 at 481-485: 19.5-20.6 A against the bassoon's 16.2-20.1 A (K: 18.1-21.9 against 20.8-24.0). In 2-qn windows the clarinet is 1.6 dB over the solo at 482 and 2.1 dB over at 484.

The clarinet notes play CC11 34-40 (pp) with a -1.5..-4 dB hairpin envelope, so the cause is the high register itself: the kit records the Clarinet KS Master's upper notes running up to +10 dB hot (LEARNINGS 13). The soli are the full Violins I patch at -6 dB. A pp line should sit about one dynamic level (3-5 dB) under a p solo.

Fix:
- `build/note_trims.json` "Clarinet 1": `{"481.0": -4.0, "483.0": -4.0, "484.0": -4.0}`, ramped by NOTE_TRIM_RAMP_S. Result: clarinet minus bassoon about -3 dB A.
- `build/roles.json` Violins I `[472.9, 477.0, -4.0, 0.25]` and `[484.9, 488.0, -4.0, 0.25]`. These stack on the soli's existing -6 dB; check that the two ramps do not add where the rows meet the c07 soli envelope. Result: soli 3-5 dB under the solo.

## 5. The tuba is the largest single source of 100-300 Hz in the tuttis; Duc's tuba cut was never adopted (measured; small gain)

Where: Tuba throughout the tuttis (bars 223-234, 255-279, 27-34). `build/mix.json` Tuba: gain +7.0 dB (the highest in the brass), one EQ band (bell2 84 Hz -5 dB, 0.2 octaves).

Evidence. Share of the master's 100-300 Hz:
- Bars 223-234: tuba 25 %, basses 20 %, celli 13 %.
- Bars 255-279: tuba 21 %, celli 19 %, basses 15 %.
- Bars 27-34: tuba 23 %, basses 35 %.
- Whole piece: tuba 15 %, behind only the celli (26 %) and basses (16 %).

The tuba is one player against 14 cellists and basses. Research batch 4 (FINDINGS section 14: Duc's brass group, "tuba -4.3 dB at 143 Hz") is listed among the defaults but is not in `mix.json`. Simulated (RBJ bell 143 Hz, -4.3 dB, 1.39 octaves, applied to the tuba's 100-300 Hz band, average -2.7 dB): the master's 100-300 Hz falls 0.44-0.52 dB in the three tutti spans and 0.31 dB over the piece, and the 300 Hz-1 kHz band falls only 0.33 dB on the tuba. The master's 100-250 Hz share is already in the reference range (-8.5 dB), so this cleans up the low end; it fixes no boom.

Fix: add a `family_eq` to `build/mix.json` "Tuba": the lowbrass bands plus `{"type": "bell", "hz": 143, "db": -4.3, "bw": 1.39}`. Keep the 84 Hz bell2. Check the 5-band read-back. No make-up gain: on the K-weighted f median, tuba equals the trombones (+0.1 dB), the Rimsky norm.

## Coordinator checks (verified on the c07 master and stems)

**Wetness ceiling: met; the mix is not wetter than c05, and is now as dry as it (measured).**
- Re-running `decay07.py` and `wetsim07.py` reproduced c07's numbers exactly: aligned tutti -20 dB median 0.41 s (0.39 / 0.36 / 0.42 / 0.48 / 0.43 / 0.25), drop at +0.3 s 16.0 / 17.2 / 18.5 / 12.2 / 13.3 / 22.9 dB, RT60 at the final cut-off 1.22 s, late slope 0.95 s, returns 12.6 dB under the dry sum.
- One automatic stop detector, run the same way on every file (30 ms RMS, aligned to the steepest fall, the level must stay 15 dB down 1 s later): c05 -20 dB median 0.34 s, c06 0.52, c07 0.36. Dvořák 9/i (2 stops, lossy MP3) 0.79 s; Movement I's reference figures were 0.43-0.58.
- With the returns removed (simulated -60 dB), c07 still gives 0.34 s and a 16.7-25.7 dB drop: the dry stems set the stops, not the hall.
- Dry or boxy risk: the stops are at the dry end, under every recording, and equal to c05. They do not break Dan's ceiling.
- Room to add hall: raising the three family returns by +3 dB simulates -20 dB at 0.43 s with drops of 11.0-21.1 dB, which is within the 0.50 s ceiling. I would leave the faders alone this cycle (Dan's last word was "too wet"). Use this headroom only if Dan calls c08 dry.
- One ceiling breach remains: the violas' soft end at qn 455.86 takes 1.01 s to fall 10 dB with R Strings against 0.28 s dry, and Violins I at 454.86 takes 0.75 s (0.54 s dry). This belongs to lens C (the R Strings return at that pp chord).

**EW template corrections from Movement I c50:**
- Timpani: followed (read, measured). No 84 Hz bell, -6 dB at 385 Hz, no Surround mic (Close 0.2 / Main 0.5). Timpani share of 30-150 Hz:
  - roll 224-234: 8 %;
  - roll 273-277: 21 %, under the basses' 28 % and the low brass's 31 %; the roll settles under the basses and tuba by bar 274;
  - strokes in 271-272: 39 % (accented strokes with +6 dB swells, 2 dB over the tuba, printed allargando, acceptable).
  
  K-weighted, the timpani are 1-3 % of the master in every span, never the loudest stem. No loop pulsing on the 7 s roll at sq 920: 100-300 Hz autocorrelation at 3.95 s is -0.18 on the stem and -0.51 on the master, level SD 1.5 dB.
- Brass make-up per instrument and dynamic: measured, no change needed. Co-sounding medians at the same printed dynamic, A / K:
  - at f: horn minus trumpet -5.1 / -3.2 dB (norm -3), trumpet minus trombone +1.9 / +1.6 (norm 0), tuba minus trombone at f +0.1 dB K;
  - at mf: horn minus trumpet -3.5 / +0.7, horn minus trombone -0.8 / -0.1.
  
  Too few soft co-sounding beats (8-24) to fit soft make-ups. The one place where the horns are clearly low is the chorale (finding 1).
- Winds hot: not now (measured). At f, a string section over a single wind is +2.6 dB A / +6.2 dB K (norm +3); horn over wind is +2.3 / +4.3 (norm +3). The c06 stem fix (-2.9 dB) took the heat out.
- Cymbals hot: no (measured). The crash strokes at 888, 1048 and 1108 sit 9.4-10.8 dB under the rest of the orchestra K-weighted in their first 1.2 s and level with it at 5-12 kHz (43-53 % of the band): heard, not dominant. The bass drum's ff strokes are 15.5 % of 30-150 Hz in their first 0.35 s and do not cover anything.
- Harp high-pass 80 Hz: followed (read).
- Brass accents: finding 3.

**The BRIEF's balance checks that pass.** Margins of lead minus everything else, sounding frames, A / K:
- Trumpet 1 solo 51-66: +5.9 / +2.7 dB. Trumpet 1 is the top stem in every bar.
- F2 violins 67-82: Violins I is the top stem in every bar, 3 dB over Violins II and 6-9 dB over the harp and celli.
- Bassoon solo 115-118: 10-16 dB over the accompaniment.
- Muted Trumpet 1 with the cor anglais 171-186: the pair is the top two stems, 6 dB over the bass clarinet. Muted trumpet minus cor anglais +0.4 dB median, a blended doubling.
- Bass theme 27-34 against Violins I+II: +4.3 / +7.4 dB.
- Theme B 211-218: Trumpets 1-2 are the top two stems, 6-7 dB over the oboe and violins.
- Chorale 255-264: brass over strings +5.2 dB A.
- Climaxes: loudest bars 278 and 223.

The "silent notes" in metrics.md (Oboe 2 at 844 and 856) are the unison rule dropping Oboe 2 under Oboe 1 (`unison_dropped` 50, `uni_fades` 846.75 / 858.75); they are not missing notes.

Do not touch: the return faders, register sends and irSetup envelope (stops at c05's dryness, inside the ceiling); the brass family EQ, including the 821 Hz -7.8 dB bell (accent fronts are 12 dB under their bodies; finding 3); the timpani's reduced EQ with no Surround mic, and the harp HPF 80; the c06 make-ups and stem-fix gains (family ratios within 2 dB of Rimsky at f); the Trumpet 1 solo role; the crash and bass-drum levels; the Oboe 2 unison handling; the climax order (278, 223).

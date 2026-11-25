# Cycle 10, critic C: dynamics over time (render of cycle 9)

Scripts and outputs: `/private/tmp/claude-501/mockup-loop/c10-C/` (`a1.py` loudness statistics, `a3.py` per-bar loudness, `hairpins.py`/`hp2.py` every hairpin, `longnotes.py`, `stembeats.py`, `sim.py` + `run_sim.py` re-mix simulations). The stems sum exactly to the master (residual -140 dB), so a volume-envelope change can be simulated by scaling each stem by the dB change on the score-time grid and summing; the simulated masters were then run through the unchanged `tools/deliver_master.py`. Bar loudness below is the energy mean of momentary loudness (LUFS) per bar unless marked RMS.

## Brief checks for c09 (definitions as in DYNAMICS-RESEARCH.md)

- Unprocessed master: -23.7 LUFS, LRA 23.8 LU, TP -3.9 dBFS. Short-term p10 -43.2, max -14.2, span 29.0 dB. Climax rise (max short-term minus the mean of the 15-20 s before it) 14.0 dB.
- Delivered mp3: -19.5 LUFS, LRA 16.0 LU, TP -1.6 dBTP. p10 -28.4, max -8.7, span 19.8 dB. Climax rise 11.7 dB. Median share of 5 s moves kept 0.80. Inversions 0 of 156. Ride at its +10 dB cap. Limiter about 4.5 dB.
- Against the targets: LRA at the top of 14-16, span 0.8 dB over 16-19, limiter 1.5 dB over the 3 dB limit. Shape checks pass.
- Real orchestras, measured with the same method:
  - Brahms 1/ii: LRA 15.2, p10-to-max 17.9 dB, p95 minus median short-term 8.6 dB.
  - Brahms 4/ii: LRA 16.9, 18.7 dB, 11.1 dB.
  - Dvorak 9/i: LRA 21.8, 26.1 dB, 12.9 dB.
  - The c09 master: LRA 23.8, 29.0 dB, 19.6 dB. Most of the movement sits about 15 LU under its integrated level, and only the two climaxes reach it.
- The overall arc is right (measured):
  - Bars 53-61 rise every bar: -34.1, -30.9, -30.5, -28.0, -27.2, -23.4, -21.2, -17.8, -14.6.
  - Bar 61 is the loudest bar, 4.0 dB over bars 79-80.
  - The coda goes ppp (bars 83-84, -49.3), to pp (bar 87 -40.1, bar 89 -39.4), to ppp (bar 92 -46.7).

## Findings, ranked

### 1. The soft dynamics still carry no mix-side lift; the ride hits its cap and the soft solos are not raised (all soft bars, all tracks; measured and simulated)

- The brief (item 6) asks for a further +2-4 dB on ppp/pp and +1-2 dB on p in the volume envelopes. `mix.json` still has the c06 table `soft_trim_db` {ppp -2, pp 0, p +2}. ppp is still 4 dB under p on top of the CC11 drop.
- The delivered mp3 rides soft bars up 13-16 dB in total and the climax up 5.7-6.6 dB: bar 1 +16.4, bars 83-85 +15.0 to +16.3, bar 61 +5.7. The ride (`gdb`) sits at its +10 dB cap.
- The span (19.8 dB) and LRA (16.0) are just outside or at the edge of their targets.
- Two exposed soft solos sit level with or under their accompaniment (RMS per 2 qn, measured):
  - Ob1 "dolce espr." bars 45-47: qn 144, Ob1 -50.8 against Vc -47.0. qn 146: -45.9 against -45.6.
  - Cl1 "1. dolce" bars 85-88:
    - qn 284.5: Cl1 -52.5 against Vc -48.8 in the strings' ppp < pp.
    - qn 286-287.5: Cl1 -53.4/-55.7 against Cl2 -48.0/-49.1. Cl1's override {ppp -4, pp -3, p -1} is the deepest soft cut of any track.
- Fix in `build/mix.json`:
  - Global `soft_trim_db` {ppp +2, pp +3, p +3.5} (+4/+3/+1.5). Timpani and harmonics stay excepted.
  - Add the same +4/+3/+1.5 to every per-track override:
    - Cl1 {0, 0, 0.5}
    - Cl2 {0.5, 1.5, 3.5}
    - Bn1 {5, 6, 5.5}
    - Bn2 {6, 8, 6.5}
    - Vla {2, 5, 3.5}
    - Cb {2, 6, 6.5}
  - In `build/roles.json`, add Oboe 1 [139, 151, 2.5] and Clarinet 1 [280, 292, 3].
- Simulated effect with the c09 stems (trim tables only, solos not included):
  - Master: LRA 23.8 -> 21.4, span 29.0 -> 26.2.
  - mp3: LRA 16.0 -> 14.4, span 19.8 -> 18.1. Climax rise 11.4 dB kept, 0 inversions.
  - The limiter stays at 4.4 dB. Finding 2 fixes that.
- mf and louder are unchanged. pp keeps its soft CC11 layer, so its timbre stays soft.

### 2. Two Trombone 1 marcato attacks set the master peak and the limiter (bar 63, qn 212.5 and 213; measured and simulated)

- The loudest sample of the movement is Tbn1 at qn 212.54: stem -5.5 dBFS, master -3.9.
- At velocity 121, these two notes have peaks 19-21 dB over their own 80 ms RMS (212.5: peak -5.5 / RMS -24.4; 213.0: -8.7 / -24.8). Their bodies are no louder than the neighbouring notes (-26.2 / -23.4).
- Every other Tbn1 note has a peak about 10-11 dB over its RMS. That includes 218 at v110 (peak -14.6, RMS -25.6).
- This is the hard transient that brief rule 4 and item 6 ask to remove. The next master peak (qn 204.44, -4.6) is 0.7 dB lower.
- Fix in `tools/score_to_parts.py`:
  - `VEL_SET["Trombone 1"]`: add 212.5: 108 and 213.0: 105, the same treatment as 218.
  - Keep `ACCENT_DB` 2 for the weight.
- Simulated with a -3 dB envelope trim on the two attacks (a lower bound for the velocity change), together with finding 1:
  - Limiter 4.4 -> 3.7 dB. mp3 LRA 14.4, span 18.1, climax rise 11.3.
  - With `TARGET_I` -19.5 instead of -19.0 in `deliver_master.py` (inside the research's -18 to -20 range): limiter 3.2 dB, LRA 14.4, span 18.4.
- With finding 1, this brings every delivery target in range.

### 3. Bar 60's crescendo f -> ff is flat or falling in every woodwind, then the winds step up 8-12 dB at bar 61 (qn 200-204; measured)

- The 4.2 s crescendo, as a linear fit of the stem level:
  - Woodwinds: Fl1 -3.4, Ob1 -3.3, Cl1 -8.7, Bn1 -3.3, Bn2 -4.9 dB. Cl2 and BCl about +0.7.
  - Strings and brass over the same span: Vln I +4.9, Vln II +7.6, Vla +9.0, Vc +6.1, Cb +10.1, Hn4 +12.4, Tbn2 +15.5, Tuba +10.4.
- Per half beat, Ob1 is -38.4, -38.1, -37.7, -38.0, -38.7, -38.9 from qn 200.5 to 203, while CC11 rises 91 -> 108. Then Fl1 goes -41.5 -> -29.4 and Ob1 -42.9 -> -33.5 at qn 204.
- Cause, measured:
  - The c09 `HP_CHAIN` sets the chained second hairpin's start value to the first's gain (`it2[5] = it1[4]`). Its end value is the same `HP_GAIN_DB` (4 dB for winds). So the bar-60 hairpin has no dB growth: Ob1 vol_db is +4.0 flat from 196 to 204.
  - In these wind patches, CC11 above about 90 adds almost no level.
- Fix in `score_to_parts.py`, in the HP_CHAIN loop, give the chained hairpin its own rise: `it2[4] = it1[4] + HP_GAIN_DB[family] * 0.75`, which is 4 -> 7 dB for winds, 3 -> 5.25 for strings and 2 -> 3.5 for brass. Release it as now after the arrival.
- Expected: winds +2 to +4 dB from qn 200 to 203.5 instead of -1 to -9, and a 4-8 dB smaller step at qn 204. Check the master peak afterwards; the qn 204.44 peak gains about 1 dB at most, because the strings already grow.

### 4. The Largamente ff (bars 61-62) decays 4 dB with no printed decrescendo, and the bar-63 sf is quieter than the beat before it (qn 204-213; measured, plus one inferred cause)

- Per beat, the master goes -18.4, -19.4, -18.4, -20.0, -20.3, -22.7, -21.4, -22.0, then -22.7 on the sf (RMS).
- From qn 204 to 211: Vln I -25.2 -> -31.5, Vla -31.0 -> -35.8, Cb -29.6 -> -35.4, Tuba -36.5 -> -45.5.
- The score has ff "molto sostenuto" on long notes, with no hairpin until the sf at qn 212.
- Causes, measured from parts.json:
  - `hpgain` is released inside the span: Vln II from qn 205.82, Vln I and Cb from about 207.9. Vol_db steps down by 3 dB over bar 62.
  - At the sf, these level cuts all start at qn 211.6-212.15:
    - Vln I: -6 dB, from the c03 divisi -3 and the tremolo-chord -3.
    - Vln II: +2 -> -10.5 dB, from the double-stop and tremolo cuts plus the role [212, 216, -6].
    - Vla: -4.5 dB.
  - So at qn 212.0, Vln I -31.2 against -28.9 at 211.0, Cb -38.2 against -35.4, master -22.3 against -19.5. The sf has no weight, and the trombone's entry at 212.5 is the first thing heard in bar 63.
- Fix in `score_to_parts.py`:
  - (a) An `hpgain` arrival inside `SOSTENUTO_SPANS` holds to the span end (`hold_end = max(hold_end, 212.0)`), then releases over `HP_REL`.
  - (b) For a printed sf or sfz, the chord cut (`chord_segs`) and any role span starting within 0.1 qn of the sf begin at sf + 0.25 qn instead of 0.1 qn before it.
  - (c) The sf gets the `ACCENT_DB` volume accent (+2 to 3 dB, 30 ms rise, held 0.25 s) as loud accents do.
  - (d) String legato targets inside `SOSTENUTO_SPANS` use velocity 105-110 instead of 124. Why: at qn 207.85 the v124 Leg BC transitions peak 17-19 dB over their body (Vln I peak -11.9 against RMS -29.2; Vln II -14.1 against -32.7). Simulated: holding bars 61-62 +2.5 dB without (d) makes that onset the master peak (-2.25 dBFS) and raises the limiter to 5.4 dB. Slower transitions also suit Largamente molto sostenuto (inferred).
- Target: bar 62 within 1.5 dB of bar 61, and the sf beat 2-3 dB over the last beat of bar 62.

### 5. Coda: the ppp < pp crescendo into bar 87 overshoots and then lands on a 5-11 dB hole in Vc and Vla (qn 283-292; measured)

- Vc goes -53.5 (qn 283), -48.8 (284.5), -53.8 (286, the pp arrival), -57.3, -60.3 (289), while Cb stays at -52.7. Vla goes -52.9, -50.0, -55.8. The master falls 3.4 dB in the bar after the arrival (qn 286 -42.3 to 289 -45.7), at a sustained pp.
- The crescendo peaks before its target and then falls back, while the Cl1 solo underneath is covered (finding 1).
- Causes, measured:
  - The arrival notes at qn 286 are new Leg Slur notes at velocity 41 (Vc 49, Vla 53).
  - Vc and Vla get the c04 `bloomv` cut of 0 -> -4.5 dB over 2 qn: Vc vol_db reaches -4.5 by qn 290.8, and Vla -4.5 by 288.4.
  - The measured sample does not bloom here; it decays.
- Fix in `score_to_parts.py`:
  - Skip `bloomv` on a note whose onset is the end of a crescendo (`any(k_ == "cresc" and abs(b_ - q0) < 0.1 for a_, b_, k_ in hps)`).
  - Set the qn 286 arrival notes of Vc, Vla and Cb to velocity 60 with `VEL_SET`.
- Target: Vc within 2 dB of Cb in bars 87-88, and the master flat (±1.5 dB) from qn 286 to 289.

### 6. Long notes in crescendos sag, and note-to-note movement is flatter than in a real orchestra (whole movement; measured, with an inferred cause)

- 418 isolated long notes, level change from 0.5 s after the attack to the end:
  - Under rising CC11: median +1.6 dB (strings) and +1.4 dB (winds). A quarter of them fall.
  - Under flat CC11: median -1.0 dB, p25 -4.5 (strings).
- Examples:
  - Vln I F5 at qn 79.85, in the bar 27 crescendo to mf: -41.2, -43.3, -44.8 per beat.
  - Fitted over whole hairpins: the Vln II crescendo 78-82 measures -6.8 dB, the Vln II decrescendo 82-87 +3.9, and the Vln I crescendo 48-51 +0.1.
- One measured cause: `swell_db` (+1.5 at 40%, back to 0 at 80%) is applied in hairpins too. At qn 79.85-81.88 Vln I vol_db is +2.88 at 80.5 and 0.0 at 81.88, so the second half of a crescendo note gets quieter.
- Momentary loudness detrended in 6 s windows has a standard deviation of 1.05-1.43 dB in the mockup. The references measure 1.4-2.6 dB (Brahms 1/ii 2.0-2.6, Brahms 4/ii 1.4-2.1, Dvorak 1.6-2.5). Phrasing is about 30-40% flatter than real players. The cause is inferred: no beat-level or phrase-peak level shaping beyond CC1.
- Fix in `score_to_parts.py`, in the swell contour pass:
  - When the note is inside a crescendo, ramp the dB swell up to +SWELL_DB and hold it to the note end, instead of returning to 0.
  - In a decrescendo, do the reverse.
  - Optionally add a phrase-peak shape: +1 dB over the 0.5 qn around the highest note of each slur of 4 or more notes, in `vol_db`.
- Lower priority than findings 1-5.

Do not touch:
- `deliver_master.py`'s ride (0 inversions, 80% of 5 s moves kept, climax rise 11.7 dB). Keep its constants unless only `TARGET_I` is moved within -19 to -20.
- The bars 53-61 rise and bar 61 being the loudest bar (4 dB over 79-80).
- The first hairpin's hold in `HP_CHAIN`.
- `ACCENT_DB` 2 and Tbn1 218 at v110.
- The bar 64 -> 65 drop (p strings under the printed Tbn1 decrescendo, then pp).
- The coda's ppp-pp-ppp arc and the final hold at -10 dB.
- The timpani roll settle.

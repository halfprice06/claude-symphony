# Cycle 20, critic C (holistic): the c19 render

Lens: the whole movement as a listener hears it, against c00, c14, Movement I c59 and the Dvořák 9/i recording. Dan's note of 2026-11-17 ("too soft ... inner lines hidden behind the melody") is finding 1 and finding 3, as the coordinator asked. The shared delivery target (mockup-kit/README.md, "Shared delivery loudness target": -16 LUFS, -1.0 dBTP, LRA 12-13 LU, p10 short-term -25 LUFS or higher, climax order on the delivered file) is taken as given; finding 1 says what it costs this movement and what must be protected.

Scripts (scratch, deleted): K-weighted momentary/short-term loudness per bar on the mp3 and master, per-family stem curves per quarter note, inner-line level against the master and the melody (0.4 s windows), section envelope SD and 3-12 Hz modulation of the 500-4000 Hz envelope, and a copy of `tools/deliver_master.py` run with Movement I's new settings on the c19 master (`K1`: TARGET_I -16, KNEE_BELOW 7, TOP_ABOVE -10, TOP_RATIO 3, limit 0.891; the ride ratio stayed at this score's 2.0 from mix.json). That copy reproduced the c19 mp3 exactly with the old settings (I -19.8, LRA 15.0, limiter 0.6 dB).

## Manual notes (third round: pages behind the top open problems)

| Manual (May 2021 HO, PDF page) | Where it applies here | Followed? |
|---|---|---|
| p.53: velocity for shorts, CCs for held notes "because they can affect overall loudness and/or dynamics in the middle of a note or phrase" | every crescendo into an arrival (bars 221-223, 261-263, 275-278) | Partly. The CC lanes do the crescendo, but they reach the top of their range before the arrival (finding 2). |
| p.64: CC11 shapes dynamics and timbre (strings and woodwinds); CC1 does dynamics and vibrato on LITE rows; "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the ... dynamics" | inner-line balance (finding 3); passage balance in general | Not used. Passage balance sits in envelope role rows. MANUAL-GAPS "Results (c36)" measured CC7 as a pre-hall, voice-stage control. It is the instrument-side way to lower a masking track without changing its timbre. |
| p.101: brass Sustain has four dynamic layers crossfaded by CC1; "all 4 dynamic layers start to play simultaneously" | brass at 223 / 263: CC1 is already 120 at qn 887.9 and 1047.9, so the arrival chord plays the same layer as the crescendo's last beat | No. The arrival gets no change of layer (finding 2). |
| p.101: Sustain Accent (velocity = attack, CC1 = body) | the brass fff arrivals | Not proposed. Dan heard the accent rows as harsh (MANUAL-GAPS #1). The arrival step should come from CC1 headroom instead. |
| p.102: shorts have no release trails; "play the MIDI notes in a connected fashion" so the room is heard between them | the hammered eighths of N and R | Followed (gap floors, short-row lengths since c16-c19). |

MANUAL-GAPS.md: nothing open there covers findings 1-3. #7 (half-section divisi) and #8 (slower legato velocity on cantabile lines) would help the inner lines of finding 3 by timbre, but they cost memory and are not ranked here.

## 1. Too soft on earbuds: the shared target fixes the level, but it costs the climaxes and the chorale's diminuendo, and the costs need guards (measured)

Where: the whole movement, especially C (bars 43-50), D (51-66), L (171-186) and the soft half of G-H.

What a listener hears now (c19 mp3, K-weighted, measured): integrated -19.8 LUFS, p10 short-term -30.3. Section medians of short-term loudness: L -31.2, D -29.3, C -28.8, G-H -26.8, against T -14.6 and R -18.7. At a volume set for ordinary streamed music (-14 to -16 LUFS), L, D and C play 13-17 LU under it. On earbuds outdoors that is too far down to follow the muted Trumpet 1 / cor anglais duet (L), the pizzicato second theme under Trumpet 1 (D) or the motive x solos (C). Another 46 s (11 % of the piece) sits under -30 LUFS short-term.

The shared target on this master (simulation K1, measured): I -16.4, LRA 12.4, p10 -24.5, TP -0.9, p10-to-max span 16.4 dB. Section means rise L +6.0, D +5.8, C +5.7 dB, against R and T +2.3. The soft passages then sit at -23 to -25 LUFS, which is followable. The subito contrasts survive within 1 dB: ff 94 -> p 95 -16.2 -> -15.3 dB; bars 110-112 -> bassoon solo 115 -15.7 -> -14.6; L -> M +9.1 -> +8.8. The build of bars 219-223 stays large (+20.4 -> +17.8 dB).

What it costs (measured on K1):
- **Climax order breaks.** On the momentary maximum per bar, c19 runs 278, 277, 223, 222, 279, 262, 276, 150, 263. K1 runs 278, 279, 277, 223, 222, then **bar 1 (-8.8), bar 5, bar 131, bar 94, bar 113**. Bar 263 (fff, crash) drops out of the top ten, and bar 1 (ff) comes within 0.8 dB of bar 223 (fff); c19 had +3.4. The top ride reads 3 s short-term loudness, so it presses the long fff passages and lets the short ff stabs through (bars 1-2 and 5-6, 94, 113, 131-132).
- **The limiter takes 4.8 dB on the two climaxes.** The highest pre-limiter peaks are at 420.5 s (bar 278) and 329.2 s (bar 223). The punch of the two arrivals is what gets limited.
- **The chorale's diminuendo flattens.** Bars 225-228 -> 233 fell 3.4 dB in c19 and fall 1.4 dB in K1, because the top ride lifts the quieter end of the brass chorale.
- **The pp -> fff span shrinks.** C (pp, bars 43-48) to T (273-276): +13.9 -> +10.3 dB.

The contrasts that must survive (the checks to add to `deliver_master.py`'s printout for this movement):
1. Bars 223 and 278 over bars 1 and 5 by at least 2.5 dB on the momentary maximum (c19 +3.4).
2. Bar 263 over every ff bar that is not a climax (94, 113, 131, 150) by at least 1 dB.
3. The chorale's diminuendo, bars 225-228 -> 233, at least 3 dB.
4. The subito drops at 94/95 and 112/115 at least 13 dB.

Fix (values; delivery side, so it is not a track-volume move):
- Adopt the shared settings, but guard the stabs with score-timed `RIDE_TRIMS` rows in `build/score_config.py` (read by deliver_master through parts.json "ride_trims"): -2.5 dB over qn 0-8 (bars 1-2) and 16-24 (bars 5-6); -2 dB over qn 372-376 (bar 94), 448-452 (bar 113) and 520-528 (bars 131-132); each ramped over 0.25 qn. Bar 150 is handled by finding 2. Then re-check 1-4 on the delivered file.
- Chorale: a `RIDE_TRIMS` ramp from 0 at qn 912 to -2 dB at qn 932, back to 0 by qn 936. This restores about 2 dB of the printed diminuendo against the top ride's lift.
- The limiter: finding 2 moves the arrival weight into the instrument (a CC step), not the master peak. Even so, expect 3.5-4.5 dB of limiting at 223 / 278 on the new target. That is the price of -16 LUFS at -1 dBTP.

## 2. The two fff arrivals at 223 and 263 have no step in the orchestra: only the crash marks them (measured)

Where: bars 221-223 (qn 880-892) and 261-263 (qn 1040-1052); all wind, brass and string tracks.

Score: bar 221 mp cresc., bar 222 f cresc., bar 223 fff on every staff with crash and bass drum. Bars 261-262: brass f cresc. into fff on every staff at 263 (qn 1048), with crash.

Evidence (stems, per family, 0.5 s before against 0.5 s after the downbeat):
- **223:** strings -0.6 dB, winds +0.6, timpani -1.3, horns +5.4, trumpets +2.4, low brass +4.3. Per quarter note, the strings reach their loudest at the end of the **mp -> f** crescendo (qn 883: -17.2 dB). The f -> fff bar adds nothing: -20.9 at qn 884, -17.0 at 887, -17.7 at the fff downbeat. On the mp3, bar 222 (-10.2 momentary max) equals bar 223 (-10.1).
- **263:** every family falls at the fff downbeat: winds -1.5, horns -2.3, trumpets -3.7, strings -1.9 against qn 1046. The master is 1.4 dB lower at qn 1048 than at qn 1046, crash included.

Causes, read in build/parts.json (measured):
- The hairpin gains on strings and winds peak at the end of the first crescendo and fall during the second. Violins I / Violoncellos / Double basses: vol_db +2.5 at 880 -> +5.5 at 884 -> +3.0 by 886. Flute 1 / oboes / clarinets / bassoons: +2.5 -> +6.5 -> +4.0. So the f -> fff crescendo runs against a falling envelope of 2.5 dB.
- The CC lanes are at the top before the arrival. Strings CC11 116 at 887.9 -> 117-118 at 888 (0.14 dB/unit there: about +0.2 dB). Brass CC1 120 / CC11 106-114 at 887.9 and the same at 888. Winds 112-113 -> 114-115. Every arrival note is velocity 127 after the same.
- At 263, the arrival steps down. Violoncellos CC11 120 at 1047.5 -> 113 at 1048 (the resting fff value is below the crescendo's end). Horns 3 / 4 vol_db +5.0 -> +3.5 at 1048 -> +2.0 by 1049. Violins II +2.5 -> +1.5 -> +0.5 (hairpin gains released from the arrival).

Fix (instrument side; files `build/score_config.py` and `tools/instr_post.py` / the `HP_CURVE` / hairpin-gain code in `tools/score_to_parts.py`):
1. **Headroom for the arrival.** For a crescendo that ends on a printed fff downbeat, cap the lane at the ff resting value until 0.10 s before the moved note-on of the arrival: strings CC11 105, woodwinds 104, brass and clarinets CC11 100 with CC1 108. Then step to the fff values at the arrival's moved note-on: strings 118, woodwinds 115, brass CC1 120 / CC11 112. Brass CC1 108 -> 120 crosses into the top layer (p.101). Size the step from each track's own curve, not a family slope. Target: strings +2 dB and brass +3 dB or more at the downbeat over the beat before.
2. **Chained crescendos keep their gain.** When a crescendo is followed at its end by another crescendo on the same staff (`hp_chained` already lists 884 and 1032), the hairpin gain must not release at the first one's end. Hold +5.5 / +6.5 from 884 and let it ramp no further. Better: drop the bar-221 gain to +3.0 / +4.0 at 884, so the mp -> f crescendo arrives at f and not above it.
3. **No release on a fff arrival.** The c18 release (2.8 dB/s) must start at the next printed dynamic or rest, not at the arrival: 892 at 223 (f / mf), and the rest at 1052.5 at 263. The celli's 1048 resting value must be at least the crescendo's end (CC11 120, or cap the crescendo at 113 by rule 1).
4. Check after the build: mp3 momentary max of 223 at least 2 dB over 222, and 263 at least 1.5 dB over 262. Climax order then 278 / 223 > 263 > 150 / 262 > bar 1. Bar 1 (ff) is fine where it is once 263 is over it.

What it does not need: no envelope step at the downbeat (Dan's rule), and no accent row.

## 3. Inner lines that deserve to be heard, and how far under they are (measured; the fixes are inferred values)

From the score sources' own comments and the score pages, these lines carry the movement's counterpoint. Each was measured as the line's K-weighted level against the master and against the melody, in 0.4 s windows where the line plays:

| line | bars (qn) | printed | line minus master | line minus melody | target |
|---|---|---|---|---|---|
| Clarinets 1-2, leggiero broken chords under the first theme | 11-26 (40-104) | mf against strings f | **-18.6 dB** (p25 -21.3) | **-11.1** against Violins I | -6 under Violins I |
| Violoncellos + violas, counter-melody under the violins' F2 | 67-79 (264-316) | mp / mf against Violins I mf | Vc -11.2, Vla -11.0 | Vc -5.4, Vla -6.0 against Violins I | -2.5 (a counter-melody at one dynamic under the tune) |
| Violins I / II, running countersubject over F1 in the bass | 27-38 (104-152) | f against F1 ff | Vln I -10.5, Vln II -11.4 | -6.0 / -7.2 against the F1 group (Vc, Cb, Hn 3-4 summed) | -4 |
| Clarinet 2, chromatic inner voice under Trumpet 1's solo (G flat -> G at bar 66, the turn to E flat major) | 58-66 (228-264) | pp against the solo p | -10.3 | -6.6 against Trumpet 1 | already right (keep) |

The chorale's inner brass are not hidden. Trombones 1-2 sit +1.2 dB and Horns 2-4 -0.2 dB against Trumpet 1 + Horn 1 over qn 892-916. The harp in E is -6.1 dB under Violins I, which is right for its accompanying role.

Fixes:
- **Clarinets 40-104:** delete the -2.5 dB role rows `[40, 104, -2.5, 2.0]` on Clarinet 1 and Clarinet 2 in `build/roles.json`. Then lift the broken chords on the instrument: +6 CC1 units (Clarinet KS Master: CC1 crossfades the layers, `CC1_DYN_TRACKS`) at mf over the span, range-tested on the track's own curve. Goal: about +5 to +6 dB in all, which leaves the line 5-6 dB under Violins I, as mf under f should be.
- **Celli / violas 264-316:** they already carry +5 / +4 dB role rows over 264-292. Do not add envelope gain. Raise CC11 over 264-304 by the units that give +3 dB on each track's own curve (Hollywood Strings in the mp range measured 0.3-0.85 dB/unit on Movement I; range-test before trusting it). Then remove the role rows by the same amount once the CC11 carries it. The brighter mp layer helps them through, too.
- **Violins' countersubject 104-152:** lower the F1 group, not the violins. Set CC7 -2 dB (CC7 = 127 x 10^(-2/20) = 101) on Horns 3-4 and Bass trombone / Tuba over qn 104-136, returning at 136. CC7 is the pre-hall level control (manual p.64; MANUAL-GAPS Results c36), so the brass keep their ff timbre and the hall keeps its tail. Flutes 1-2 already double the countersubject at 27-34. Leave them.
- Measure each line again on the c20 stems with the same method. The new delivery (finding 1) raises everything but does not change these internal margins.

Cost: the first theme's tune loses about 1 dB of margin over the clarinets. In bars 27-34 the bass F1 sits about 2 dB less on top of the texture, which the score's comment (c097: "the voices around the subject drop to p") partly argues against. If Dan prefers F1 dominant, skip the CC7 part and leave the countersubject at -6.

## 4. Horn 1's chorale loss comes from "Mono From Left", not from the bar-224 step (measured)

Where: Horn 1, qn 888-936.

The c19 change is not the bar-224 step. That step moved only the 3 -> -1 dB fall from the first beat of the 892 note into the breath before it (c18: +3.0 at 892, -0.5 at 893; c19: -1.0 from 891.8). Over 48 qn that accounts for about 0.1 dB. The per-note mid levels of c18 against c19 (1 qn after each onset) show where the loss is:
- 888 (C5, fff): -25.1 -> **-32.5** (-7.4 dB).
- 906, 908, 920, 928: -42.1 / -42.2 / -41.6 / -41.1 -> -44.7 / -44.8 / -43.8 / -43.9 (-2.3 to -2.7). These are pitches whose right channel was the stronger one in c18 (R over L by 1.3-1.8 dB).
- 892-900: +0.7 to +1.1, the pitches whose left channel was stronger.

Left-only routing keeps the left mic's per-pitch level, so every pitch moves by its old L-R balance. The C5 loss is larger than its L-R difference, and part of it may be render variance (Movement I c43 measured Horn 1 states flipping 1-14.5 dB between renders).

Fix: Horn 1 per-pitch region gains (`region_gain_db` in `build/mix.json`): +2.5 dB on the pitches of 906 / 908 / 920 / 928. For C5, range-render it first: if C5 still reads 5 dB or more under c18 on a range render, give it +4 dB there, otherwise leave it. Horns 2 and 4: keep stereo. Their worst notes lose up to 2.8 dB in mono (medians 0.3-2.3 dB per pitch). Switching them to "Mono From Left" would move each pitch by its L-R balance, up to 7.9 dB on Horn 2 (L-R +7.9 at G4). That is a larger level fault than the mono loss it removes.

## 5. The loud passages became more static since c00 (measured on the master; cause inferred)

In loud frames (top 40 % of 3 s windows), the master's level SD is 2.50 dB in c19 against c00 2.85, c14 2.63, Movement I c59 2.80 and Dvořák 2.90. The envelope modulation at 4-8 Hz and 8-16 Hz (the rate of articulation) is 1.0 / 1.4 dB under c00 and 3.2 / 3.2 dB under Dvořák. By section, against c00, the losses are in the ending: P (chorale) SD 1.58 -> 1.31 dB and 3-12 Hz modulation 27.7 -> 25.5; Q -0.22; R -0.19; T 3.06 -> 2.50. Intro, A and N gained. Inferred: the per-note envelope layers removed in c16, the halved accents of c18 and the c19 chorale overlaps all smooth the late tuttis. The chorale overlaps are right for the bar-line holes, but nothing gives the long chorale notes life inside.

Fix (instrument side, small): the research's "long notes keep moving" (FINDINGS batch 4, phrase arch) on the chorale's whole notes in the brass (qn 892-932). Use a CC1 arch of +6 units peaking at 40-50 % of each two-bar phrase (brass CC1 near 86-92 at f, the steep part of the layer crossfade), with the printed diminuendo of 928-932 taking over. R (qn 984-1080): keep the ostinato velocity pattern (it is in: basses 81 / 97 / 87 before 1048). Check that the brass heads in R carry a falling 15-25 unit CC1 shape over their long notes (Balfe "fanfare" type, BRIEF research batch 6/7). Target: section SD within 0.15 dB of c00 in P-T. Low priority against 1-3.

## 6. Coordinator items checked through this lens (measured)

- **Climax order.** The printed order is final / 223 (fff) > 263 (fff) > bar 1 (ff) > 99. On the c19 mp3, 263 (-13.0) is only 0.5 dB over bar 1 (-13.5), and under bar 150 (ff, -12.9) and bar 222 (f cresc., -10.2). Bar 1's 1.1 dB fall on the master is not a fault: bar 1 is ff, and it needs to sit under the fff bars, which it does by 3.4 dB against 223. The fault is that 263 and 223 do not rise (finding 2). Bar 150 is ff: CC11 106-109 plus hairpin gains of +3 to +5 dB from the sfp crescendo (qn 592-596). The crescendo ends at the printed ff of qn 596, but the gains are still held at 597-598 (vol_db Flute 1 +4.0, Horn 1 / Horn 3 +5.0, Violoncellos +4.5). Ramp them to 0 between 596 and 598, so the ff of 596 is CC11's own ff and bar 150 drops about 2 dB under 223 (inferred size).
- **Basses' eighths, isolated accents, celli pizzicato, cor anglais row, trombones 199-204, the 89 plateaus.** Critics A and B cover these. Plateaus that touch this lens: celli / basses +3.0 over 885.8-892 and basses +3.0 over 1032-1052 are the arrival plateaus of finding 2. Keep them through the fff bar, then release them at the next printed dynamic (892 / 1052.5), per finding 2 item 3.
- **Movement I c60 (1):** "ff tutti louder than both fff climaxes" applies here in reduced form: bar 222 (f cresc.) equals 223, and 150 (ff) is within 1 dB of 263. The cause is the same (CC lanes at the top, hairpin gains). Finding 2 is the fix.
- **Movement I c60 (4):** the trim steps against crescendos apply: the bar-222 envelope falls 2.5 dB during a printed crescendo.

Do not touch: the c19 chorale overlaps and staggered same-pitch gaps (master bar-line dips 8 of 10 within 3 dB); the entry lead cuts; the stop decays (15.4-16.8 dB at +0.3 s, final chord RT60 1.39 s); the subito contrasts of bars 94/95, 112/115 and 42/43 (keep them on the new delivery); the chorale's inner brass balance (trombones +1.2, horns -0.2 against the lead); Clarinet 2's inner voice under the trumpet solo (-6.6 dB); the basses' ostinato velocities; the accent sizes (do not raise accents to restore liveliness).

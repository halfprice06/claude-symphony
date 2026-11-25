# Cycle 25, critic C: blend and space (render of cycle 24)

Material: `cycles/c24/render/` (31 dry stems, 4 returns, `00_Master.wav`), `cycles/c24/mvt3-mockup-c24.mp3`, `cycles/c23/render/` (Oboe 1 / Clarinet 1 comparison), `cycles/c24/parts_rendered.json`, `cycles/c24/before/parts.json` (c23 data), `cycles/c24/T1/parts.json`, `build/mix.json`, `build/score_config.py`, `build/roles.json`, `build/mockup-events.tsv`, the score pages 4, 7, 9 and 12, and the Dvořák 9/i reference (lossy MP3; used only above 100 Hz and for band shares). Times come from the rendered tempo map. Scripts were in the scratch folder, which is now deleted. "Measured" means a number taken from these files. "Inferred" means reasoning that no render has tested. Nobody in the loop can hear, so every claim about what a listener hears is inferred.

Masking measure used in finding 1. For each bar and each playing track I compared the track's power with the rest of the master (master minus the track) in 1/3-octave bands from 160 Hz to 6.4 kHz. I report the best band (the band where the track stands highest over the rest). A best band at -10 dB or lower is called hidden: the track is at least 10 dB under the rest of the orchestra in every band. Basses and contrabassoon are not judged this way, because their fundamentals lie under 160 Hz.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 25 (the plan ends at c20). I read the pages behind this lens's open problems in full, plus the MANUAL-GAPS items that apply.

| Manual (May 2021 HO, PDF page) / gap | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.122, 36in and 40in Ludwig Bass Drum | 36in: "deep, rumbling quality with a strong woody hit". 40in: "strong low frequency rumble and a firm attack". Both use the same key map (D1 = felt long), and velocity sets up to 12 dynamic layers. The 40in patch is installed. | Bass drum ff at qn 888 (bar 223) and 1108 (bar 278), on the 36in patch. | No. The 36in stroke peaks at 106 Hz, and its 30-90 Hz band is 10.4 dB under the basses at 888 and 8.3 dB under at 1108. The rumble does not reach the mix (finding 3). |
| p.125-126, Timpani Hard Rolls | CC1 selects among 8 dynamic levels; CC11 and velocity set loudness. | The fff roll at qn 888 with its printed decrescendo to f at 892. | Only in part. CC1 reaches 120 (the top layer) at 888.1, but the CC7 fold drops the level 8 dB by 888.25 (finding 2). |
| p.141, 4.2.6 Channel Routing | Mono From Left sends the left channel to both outputs and discards the right. | Horns 1 and 3 (`channel_map` 2 since c19). Horns 2 and 4 are stereo. | Not consistently. The horn section has two kinds of image (finding 4). |
| p.89-90, divisi patches; MANUAL-GAPS #7 | DIV A and DIV B record one chair of each stand, Close mics only; "the loudness of a divisi part is not much less than" the whole section. | Violins I "dolce, 4 soli" at qn 473-476 and 485-488 (bars 119-122). | No. The 4 soli play on the full-section "Sus MAX" row (finding 5). Kit LEARNINGS §1: the DIV A KS Masters ship with the main channel panned, so a DIV patch needs pan 0. |
| p.138, mic positions | Close sits in front of each section, Mid at the stage edge, and Main in the fifth row with "more room reflections than direct sound". | The winds are Close-heavy. The oboes run Close 0.939 / Main 0.088, and their stem correlation is 0.99 (other winds 0.84-0.93). | Yes. This is the EW template (FINDINGS §1: oboe Main 20.6 dB under Close). The wind return supplies the room (winds 6-10 dB dry over wet, strings 13-16). No change. MANUAL-GAPS #4 (Mid mics) is still untested and is not this lens's top problem. |
| p.118, 22in Zildjian K Crash | Pairs with three lengths (C3 long). Velocity sets 7 dynamic layers. "grandiose". | Crash fff at 888, 1048 and 1108. | Yes. In the first 0.4 s the crash's 10-16 kHz band equals the master's (-1.0 / -0.3 / -1.1 dB), and it decays about 10 dB per second. The cut after 1113 follows the printed quarter and rest. |

## Findings, ranked

### 1. Inner lines hidden: the second violins' f espress. countersubject in bars 159-165 sits 15-17 dB under the first violins; the horn's dolce counter-line in bars 67-70 is also hidden

Measured. This is Dan's "inner lines hidden" (17 Nov). I scanned every staff carrying a printed espress. / cantabile / dolce / solo / marc. text over the 4 bars after the text (method above). Lines whose best band is under -8 dB:

| track, bars | printed | best-band dB per bar | level against the line it is meant to be heard with |
|---|---|---|---|
| Violins II, 159-165 (qn 632-660) | f, espress., slurs of 4 eighths: the countersubject against the ff tune (Fl, Ob, Vln I, Vla, Hn 1-2) | -17 -16 -14 -16 -17 -15 -15 | Violins II -45.5..-48.6 dB per bar, Violins I -29.0..-32.5. Violins II is 15-17 dB under. |
| Clarinet 1, 159-165 | mf espress., the same figure in thirds | -11 -10 -11 -11 -9 -9 -13 | |
| Horn 1, 67-70 (qn 264-280) | pp, "1. dolce", counter-line under the violins' cantabile mf | -13 -12 -11 -10 | Horn 1 -52.9..-56.7 dB, harp -43.8..-46.6, strings -37.5..-44.8 |

Every other marked line passes (Trumpet 1 solos +5..+16, Bassoon 1 solo +9..+11, muted trumpet +5..+12, celli espress. mostly over 0).

Cause of the Violins II gap (measured from `parts_rendered.json`):
- CC11 is 75 at 631.87, rising to 82 by 646.5. Violins II's median CC11 at printed f over the movement is 82; Violins I is at 107 (ff).
- Strings "Sus MAX" runs about 0.7 dB per CC11 unit under its knee near 100 (MANUAL-GAPS c18). So the CC11 gap alone is about 15 dB.
- On top of that: the role row -2.9 dB (600-680) and velocity 83 (v100 in the same figure at 104-120).
- At 104-120 (the exposition's countersubject, ff) the same figure plays at -37.3 dB. Here it plays at -47.8 dB.

Simulated by adding gain to the Violins II band powers:

| Violins II gain | Violins II best band, bars 159-165 | Violins I best band |
|---|---|---|
| +6 dB | -8..-11 | |
| +8 dB | -6..-9 | |
| +10 dB | -4..-7 | +2..+5 (stays on top) |

Fix (instrument side plus one held passage level, so within Dan's rule):
- `build/score_config.py` `INSTR_POST` `cc_scale` on Violins II: `{"lane": "cc11", "pts": [(631.8, 0), (631.9, +6), (659.7, +6), (659.8, 0)], "k": 40}`. That is about 75 -> 89 at the start. The aim is CC11 88-92 over 632-659.7, still under the ff 103 of 660. If `cc_scale` does not reach it, use `note_cc` `"add": 12` on the span 632-660.
- `ROW_VEL_SPANS` (or `vel_cap` min) for Violins II at 632-660: velocity 100, as in the same figure at 104-120.
- `build/roles.json` Violins II: split `[600, 680, -2.9]` into `[600, 632, -2.9]`, `[632, 660, 0.0]` and `[660, 680, -2.9]`. These are held phrase levels; the edges sit on the f at 632 and the ff at 660.
- Target: Violins II 5-7 dB under Violins I over 159-165 (now 15-17), best band -7 or higher. The clarinets ride on the same figure; check that they reach -8 or higher once Violins II is up, and add Clarinet 1 +2 dB (`cc_scale` k 20) only if they do not.
- Horn 1, 264-280: a held role row +4 dB inside the existing `[200, 392, -2.5]` (net +1.5 over 264-280; ramp 0.5 qn at each end). Keep CC1 as it is, so the pp timbre stays. Target: best band -6..-8 (now -10..-13), still under the violins.
- Re-run the masking scan after the render. Both lines were masked without anyone noticing, because the level tables judge each track against its own printed dynamic, not against the line it plays under.

### 2. The timpani's fff roll at the C-major arrival (bar 223, qn 888) drops out within a quarter of a beat; at all three fff arrivals the timpani sit 15-26 dB under the master

Measured levels; audibility inferred. Score: Timp roll f cresc. 884-888, fff roll on C at 888 with a decresc. to f at 892 ("Trumpet 1 B to C with the timpani roll", BRIEF).

Timpani minus master per 0.25 s window:

| qn | 884 | 886 | 887 | 888 | 888.5 | 889 | 890 | 892 |
|---|---|---|---|---|---|---|---|---|
| dB | -12.6 | -15.4 | -15.2 | -17.2 | -20.8 | -25.7 | -27.5 | -15.8 |

- Timpani CC7 (`vol_to_cc7`, linear amplitude): 110 at 887.0, 96 at 887.98, then 38 at 888.25 (-8 dB). CC1 is 120 at 888.1, so the right layer plays at the wrong level.
- In bar 223 the timpani rank 26th of 31 stems (bars 219-222 7th). Its share of the master's 30-150 and 150-400 Hz bands is -19.8 and -19.7 dB.
- At 1048 (fff, bar 263) it is -15..-17 dB under the master; at 1108 (fff) -19..-22 dB.
- The roll is a fff that becomes a background for the rest of the bar, while the printed decrescendo lasts the whole bar.
- Kit LEARNINGS ("rolls too loud", c25 of Movement I): "The rule can overshoot: ... the ppp rolls sat 14-23 dB under the orchestra and needed +3-4 dB back". The settle rule is right for long rolls. At the arrivals it overshoots.

Fix: in the timpani block of `tools/score_to_parts.py`, add a generic rule `TIMP_ARRIVAL_RAMP` (default empty) with Finale values `[(888.0, 892.0), (1048.0, 1050.0)]`.
- For a roll at a printed arrival louder than the previous mark, with a printed decrescendo, the folded volume parts become one linear ramp. It starts at the level of the crescendo's top (CC7 about 100-105 at the moved note-on) and ends at the printed target's roll-trim level at the hairpin end (f at 892).
- This replaces the 0.25 qn attack bump and the hairpin-gain release at 888 (`timp_hp` [888, 0, -3.39] in parts.json).
- 1108 already skips the settle (`TIMP_SETTLE_SKIP`). For it, only the bump's release needs the same hold over 1108-1110.
- Targets: timpani minus master -10..-12 dB over 888.0-889.0 (now -17 / -26), -15..-18 at 891 (now -28), and never over -10 (so never the loudest stem).

Cost, simulated on the stems: +8 dB of timpani over 888-889 raises the master +0.25 dB, with peak +0.04 dB. Refit the bar-223 summit ride row (now -7.4) by -0.3 dB so the final keeps its 0.5 LU lead.

### 3. The loud tutti is thin at 100-250 Hz and bright above 6 kHz, and the bass drum adds no low end at the arrivals (open since c21)

Measured. Band shares (dB of total) over the loudest 10 % of 0.68 s frames, and over the 40th-70th percentile frames:

| frames | 20-100 | 100-250 | 250-500 | 500-2k | 2-6k | 6-20k |
|---|---|---|---|---|---|---|
| c24 master, loud | -12.6 | -10.9 | -7.8 | -2.3 | -9.6 | -23.7 |
| Dvořák 9/i, loud | (-23.9, lossy, not used) | -6.0 | -6.4 | -3.6 | -11.2 | -28.5 |
| c24 master, mid | -12.1 | -8.6 | -6.2 | -3.3 | -10.6 | -30.7 |
| Dvořák 9/i, mid | | -7.9 | -6.0 | -3.3 | -10.0 | -31.0 |

- Mid-level frames match the reference within 0.7 dB from 100 Hz to 20 kHz.
- Loud frames are 4.9 dB short at 100-250 Hz and 4.8 dB over above 6 kHz. This is the same picture as c20 (-11.7 / -23.4). The c21 `loud_eq` proposal was deferred in c22-c24.
- Who makes the bands in the loud frames:
  - 6-16 kHz: crash 23 %, Trumpets 1-2 33 %, Trombones 1-2 17 %, Violins I 8 %.
  - 100-250 Hz: basses 24 %, celli 22 %, tuba 12 %, timpani 10 %.

Low end at the arrivals:

| | master 30-90 Hz, f bar before -> after the stroke | full band | basses | bass drum 30-90 Hz |
|---|---|---|---|---|
| qn 888 | -30.9 -> -30.0 (+0.9) | +6.4 | -30.5 -> -30.8 | -41.2 |
| qn 1108 | +1.6 | +4.6 | | -39.6 (basses -31.3) |

- The bass drum's spectrum peaks at 106 Hz: 90-125 Hz holds -3 dB of its energy, 30-60 Hz only -12.

Fix:
- (a) `build/mix.json` `loud_eq`, reusing the existing ff-span point list (the one on Violins I and Tuba):
  - Violoncellos: bell 160 Hz +3 dB, 1.5 oct.
  - Trombone 1, Trombone 2: bell 180 Hz +2 dB, 1 oct.
  - Violas: bell 200 Hz +2 dB, 1 oct.
  - Trumpets 1-3: high shelf 5 kHz -4 dB.
  - Simulated on the c24 loud frames: 100-250 Hz -10.9 -> -10.1, 6-20 kHz -23.7 -> -24.7, K-weighted loudness +0.06 dB.
  - The stronger set (celli +4, low brass +3 at 180 Hz, violas +3, basses 130 Hz +3, horns 200 Hz +2, trumpets shelf 4 kHz -5, crash shelf 6 kHz -3) gives -9.3 / -25.7, +0.15 dB.
  - Start with the moderate set. Check that the delivered f -> ff step stays at 2 LU or more, since the loud frames get slightly louder.
- (b) Bass drum: switch the patch in `build/score_config.py` TRACKS from `36in Ludwig Bass Drum.oib` to `40in Ludwig Bass Drum.oib` (p.122; same D1 felt long key 38, same velocities 114 / 112; check its key map with `dump_ks.py`). Match its level on a range render.
  - Fallback without a patch change: Bass drum `eq` low shelf 70 Hz +8 dB.
  - Target: bass drum 30-90 Hz within 5 dB of the basses' band at both strokes (now 10.4 / 8.3 dB under), and the master's 30-90 Hz at 888 at least 2 dB over the f bar before (now +0.9).
  - Check the final-chord limiter stays at 6 dB or less: c21 simulated +6 dB of bass drum gain as +0.17 / +0.34 dB of peak.

### 4. The horn section has two kinds of image: Horns 1 and 3 are mono, while Horns 2 and 4 are wide and lose over 2 dB in mono on 21 notes

Measured. Stem correlation over the whole movement and in the chorale (892-928):

| | Horn 1 | Horn 2 | Horn 3 | Horn 4 |
|---|---|---|---|---|
| whole movement | 0.98 | 0.54 | 0.98 | 0.65 |
| chorale | 0.98 | 0.72 | 0.98 | 0.56 |

- Mono loss (stereo power over (L+R)/2 power, held notes of 1 qn or more):

| | median | notes over 2 dB |
|---|---|---|
| Horn 2 | 0.91 dB | 12 of 101 (E flat 4 at qn 0, 16, 357, 372, 417, 422, 664, 792; A flat 3 at 306 / 310; G4 at 560) |
| Horn 4 | 1.09 dB | 9 of 84 (F sharp 3 / G sharp 3 at 0, 16, 136, 364, 800, 824-832) |
| Horns 1 / 3 | 0.18-0.19 dB | none |
| Trumpets, trombones, tuba (stereo) | 0.61-1.08 dB | none |

- This is the per-pitch phase of the 1FH Main pair that c19 removed from Horns 1 and 3 only. On a mono or near-mono playback those notes drop 2-3 dB. In stereo the four horns that play one chord come from a point and from a spread (inferred). The scherzo's c21 note (Mono From Left horn stems at correlation 0.94-0.97) applies here: ours read 0.98.

Fix: `build/mix.json` Horn 2 and Horn 4 `"channel_map": 2` (Opus Channel Routing, p.141; full rebuild of both tracks), `gain_db` 2.0 -> 1.0 on both. c20 measured Horn 3 +1 to +2.5 dB after the same switch.
- Targets: mono loss under 1 dB on every Horn 2 / 4 note. Horn 3 minus Horn 4 in 936-948 within -1..-3 dB (now -4.1 by my window, -3.4 in CHANGES). Horn 2 / 4 levels at 888 and in the chorale within 1 dB of c24.

### 5. The "4 soli" of Violins I (bars 119-122) play on the full section

Measured (data and image); benefit inferred. Score p.7: "dolce, 4 soli", pp, a falling octave run (qn 473-476 and 485-488), "gli altri" rest.
- Rendered on "Sus MAX" of the full 1st Violins KS Master at CC11 37-43.
- Stem correlation in the run is 0.22: the full section's width. Four players from one desk give a narrow, thin image.
- Level -53.4 / -55.2 dB in bars 119-120, 5.6 dB under the bassoon solo, which is a sensible balance.

Fix (pass 2, so the main project's memory is unchanged):
- Add a pass-2 track "Violins I soli" on `1st Violins Divisi/01 Long/1st Violins Sus MAX DIV A.oib` (Close only, p.89-90), with the main channel pan set to 0 (kit LEARNINGS §1).
- It plays only qn 472.6-489.5, with the notes, CC11 and leads of the Violins I part there. Seat -0.31, width 0.15, return R Strings -10 dB. The main Violins I track drops those notes.
- Match the level so the run stays 4-7 dB under the bassoon solo.
- Target: correlation 0.6 or more during the run, level within 1 dB of c24.
- Lowest priority here: the passage is two bars of pp.

## Coordinator items checked through this lens

- **Oboe 1 568-576, why the range result did not transfer.** Measured: the oboe's level does not respond to CC11 above about 80 in this passage.
  - c23 played CC11 91-96 and c24 82-87; the stem read -43.2 and -42.9 dB over 568-571.7 (the c23 and c24 waveforms differ by -41 dB, so the sound changed, but its level did not).
  - T1's 74-78 read 7.8 dB under the clarinet.
  - So the level drop sits between 78 and 82, under the "Sus MAX" layer change. The full render's +3.5 dB (k 33) landed above the change, where CC11 does nothing.
  - Next step: CC11 79-80 on 567.5-575.75 (that is, `cc_scale` -1.5 dB at k 33 from the c24 lane, not +3.5). Or hold the c24 lane and add a held role row of -4 dB over 567.5-576 (a passage level).
  - Target: -4..-5 dB under Clarinet 1 (now -0.4 / -1.0).
- **Horn 3 under Horn 4, bars 235-237:** -4.1 dB (my window 935.6-947.75). Met within 1 dB; finding 4 will move it, so re-measure.
- **Muted Trumpet 1 against the cor anglais (171-197):** level -2.8 / -0.7 dB in the two unison phrases. The mute's colour holds: 5-10 kHz minus 0.5-2 kHz -51.0 dB (open p solo -43.8, cor anglais -38.3), and 2-5 kHz minus 0.5-2 kHz -17.9 (cor anglais -23.2). It is nasal over the cor anglais, as a straight mute should be. Both images sit right of centre (R-L 2.5-4.4 dB). Nothing to change.
- **Hall and stops (master):**
  - Bars 2 / 6 / 94 / 113 / 166 / final fall 20 dB in 0.33 / 0.34 / 0.41 / 0.38 / 0.33 / 0.37 s, inside the wetness ceiling (0.50).
  - Master side/mid -5.4 dB (references -4.7..-5.4; muted solo and F2 -7.0 / -7.1).
  - Stereo balance R-L +0.5 dB over the movement, within ±1.4 dB in every section.
  - Bar 113's 14.4 dB on the mp3 comes from the delivery stage, not the hall: its master drop is about 16.7 dB.
- **Timpani rolls against Dan's rule:** in 5, 147-152, 209-210, 231-238, 243-246, 261-263 and 273-278 the timpani rank 14th-20th of 31 stems, with a 30-150 Hz share of -10.6..-16.3 dB. No roll drowns anything. The problem is the opposite one, at the arrivals (finding 2).
- **Findings from the other movements:**
  - Mono From Left horn correlation (scherzo c21): applies (finding 4).
  - The violins' Detache 5286 ms release (scherzo c21): does not apply. No violin or viola row here is "Detache"; only the celli range test used it, with capped releases.
  - The other scherzo c21 / c22 items (staccato release caps, wind Sus Accent MAX, crescendo targets, ride rows) belong to the articulation, balance and delivery lenses and were not measured here.

Do not touch: the four Spaces returns, their send levels and the irSetup envelope (every tutti stop at -20 dB in 0.33-0.41 s, under the 0.50 ceiling; side/mid -5.4); the muted Trumpet 1 bandpass 250-8000 Hz with its level under the cor anglais; the oboes' and cor anglais's Close-heavy template mics; Horns 1 / 3 on Mono From Left; the crash patch, its length and its cut after 1113; the settle and soft-roll rules on the long rolls (keep them, and change only the arrival ramp of finding 2); the harp's colour and level (best band median -2.1 dB, hidden in no passage that matters).

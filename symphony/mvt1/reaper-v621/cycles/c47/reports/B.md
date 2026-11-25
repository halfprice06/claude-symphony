# Critic B, cycle 47 (render c46): balance and levels

## Manual notes (second reading of the c41 B row: May 2021 HO manual PDF pages 32-34, 43, 46, 191-192, read again in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items that touch these pages come first, then the c41 B notes checked against c46, then what the first reading missed.

| Source | What it says | Where it applies here | Followed in c46? |
|---|---|---|---|
| MANUAL-GAPS #6 (p.34, p.143, p.145; 2025 p.92) | Round robins reset on the CC set in Preferences > MIDI > Round Robin. | Every track; render-to-render repeatability. | c41: not followed. **Now followed** (since c43): `tools/build_reaper.py` reads `RoundRobinResetCC` (16) from Preferences.json and sends it at 127 in the pre-roll (read). Repeatability c45 -> c46 on spans whose data did not change (frames within 1.25 s of an envelope change left out): 25 of 35 compared stems have 96-100% of 50 ms frames within 0.5 dB (measured). Below that: violas, Violins II and celli (stems swapped or re-fitted in c46), Oboe 1 (93.9%), the pass-2 aliases (70-88%, no note over 3 dB) and Trumpet 1 (85.5%). The reset does not hold the Solo Trumpet's Leg Slur MAX state: finding 1. |
| MANUAL-GAPS #7 (p.89-90) | Half-section divisi for soft div. passages. | Violas div. bars 47-60. | Open, not needed for balance: the cello and horn tune of bars 47-54 sits +6.8 dB K (median per beat) over the loudest other stem (measured). |
| Memory plan, p.32-33 | Preload by drive type; a hard drive needs the most RAM; Never Preload needs RAID 0 PCIe. | Samples on one USB hard drive. | Unchanged: `PreloadSize` 1, `NeverPreload` false (read 2026-11-07). The c46 attack probe flagged 0 late notes (metrics.md). Followed in effect. |
| p.33 | Multi-threaded reverb and voice renderer, voice-render threads, plugin outputs. | Offline 1x render. | Unchanged: both off, 1 thread (read). The Opus worker-thread crash in the first c46 pass-2 render (CHANGES.md) happened with multi-threading off, so this setting is not its cause (inferred). |
| p.34 (picture) | Reset Controller and Reset Note; program change to articulation. | | `RoundRobinResetNote` -1, program change off: consistent (read). |
| p.43 | Purge states (red / yellow / green); the instrument volume slider is the mixer fader. | Render start; levels. | c41: memory.txt wrote the pre-settle reading. **Now followed**: 23 GB at start, 44 GB settled, 45 GB (24 GB compressed) after the main render; pass 2 14 / 34 / 37 GB (read). Levels live in REAPER's volume envelope, not in Opus's volume, as p.64 / p.151 ask (read). |
| p.46, p.191 | System usage; All Instances window. | GUI only. | Not applicable; unused rows are unloaded by `UNLOAD_UNUSED_ROWS`. |
| p.192 | Voice limit: too low a limit drops voices (one note uses a voice per mic and layer). | Dense chords. | Followed: patch limits 250 / 350, maximum 1024 (read); the silent-note check lists only its two known false alarms (Trombone 1 552, Timpani 727). |
| p.192 | Octave and key range. | | Not used; consistent. |
| New (p.34) | Drives dedicated only to streaming avoid bottlenecks. | One USB drive holds every library. | Hardware, outside the loop; no late notes measured. |

## Method

- Render: `cycles/c46/render/` (40 stems as delivered, after the swaps and stem fix), against `cycles/c45/render/`. Data: `build/parts.json` (describes the delivered stems), `cycles/c46/before/parts.json` (c45), `build/roles.json`, `build/score_config.py`, `build/mix.json`.
- Frames: 4096-point FFT, 50 ms hop, stereo power, A- and K-weighted (BS.1770 filters) and 1/3-octave bands. "re M" = stem minus master. Delivered: ffmpeg ebur128 short-term loudness of the mp3, centred as `deliver_master.py` does.
- Simulations scale a stem's frame powers by the proposed shape and add the change to the master as power.
- Score pages read: 2-6, 8-18.

## Findings, ranked by what a listener would gain

### 1. Trumpet 1 rendered 3.5-14.5 dB louder than c45 on 16 Leg Slur MAX notes with identical data: it now tops the tune in bars 69-71 and the pp crescendo of bars 113-114 (measured; cause known from c42 / c43)

**Where.** Trumpet 1, three phrases: qn 275.3-284.1 (bars 69-71), 451.3-456.0 (bars 113-114), 642.9-644.0 (bar 161).

**Evidence (measured).**
- Per note, c46 minus c45 (K, over min(length, 1 qn)): 275.5 +3.5, 276 +5.5, 277 +8.9, 279 +5.1, 280 +7.0, 281.5 +7.5, 282 +6.1, 283 +6.9, 283.5 +14.5; 451.5 +4.4, 452 +6.6, 453.5 +3.8, 454 +6.3, 455 +4.9, 455.5 +7.8; 643 +4.2.
- Notes, keyswitches, CC1 / CC11 lanes and the volume envelope are identical in these spans (envelope difference 0.0 dB), and the main pass was MIDI-only with no Opus state change (c46 CHANGES "Run"). Every other Trumpet 1 note is within 3 dB; Horn 1, Horns a2 and Trumpets a2 have no such note.
- These are the same three phrases that flipped in c42 (`cycles/c42/actor_scripts/splice42.py`, loop/LEARNINGS c42) and c43 (`_C43_STATEFIX_ROWS`): the per-note excess matches the c43 rows within 1.5 dB (e.g. 283.5 +14.5 against a -14.5 row).
- Balance, bars 69-71 (score p.7: Trumpet 1 doubles the f tune with flutes, oboe and Violins I). Trumpet 1 minus Violins I per qn 275-283 (K): c45 -7.1 / -4.8 / -5.4 / -6.3 / -8.5 / -11.2 / -6.9 / -6.7 / -3.2, c46 -4.5 / +1.2 / +3.4 / -2.2 / -1.6 / -3.9 / -0.2 / +0.2 / +7.2. Over Flute 1 +11.6 at 277 and 283. Trumpet 1 re M -11.0..-16.3 -> -3.8..-9.7; on the same-dynamic scan its f level is +7.1 / +6.5 over the f median in bars 70 / 71 (+0.3..+4.4 in its other f bars).
- Bars 113-114 (p.11, Trumpets 1-2 pp cresc.): Trumpet 1 rank among 39 stems 13-19 -> 2-7, re M -15.5..-18.8 -> -9.5..-13.1 at qn 451-455.
- Bar 161: re M at 643 / 643.5 -7.1 / -6.3 -> -4.1 / -5.5; over Violins I +3.5 / +4.4 -> +7.4 / +5.5.

**Fix.**
- Now: take c45's Trumpet 1 audio back over the three spans, as c42 did. Copy `cycles/c42/actor_scripts/splice42.py` with source `cycles/c45/render/16_Trumpet 1.wav`, target `cycles/c46/render/16_Trumpet 1.wav`, the same spans (275.29-284.1, 451.28-456.0, 642.88-644.0) and crossfades (0.03 s before each phrase's first changed onset, 0.05 s after its Sus note's onset; the two renders agree within 0.4 dB at 274.5-275.0, 284.5, 450 and 644). Rebuild the master and re-deliver (`render_cycle.py 46 --measure-only`).
- Simulated: Trumpet 1 minus Violins I back to the c45 values above (-3.2..-11.2); bar 114 Trumpet 1 re M -15.3..-19.0; master 272-284 -0.5 dB K.
- Keep it from returning: c47 builds Trumpet 1 MIDI-only again, so the state can flip either way. Before any stem fix, compare every note of every track whose notes, keyswitches and lanes did not change with the previous render, with the envelope difference removed, and list notes that moved more than 3 dB (loop/LEARNINGS c42 asks for this; no tool does it yet). A small `tools/state_check.py PREV_RENDER PREV_PARTS RENDER PARTS` run by `render_cycle.py` after measuring would do it. My per-note version (level over min(length, 1 qn), envelope difference at the onset removed), run on nine tracks of c46, flags exactly these 16 Trumpet 1 notes and 9 single notes of 3-6 dB elsewhere (Clarinet 1 116, Oboe 1 555, Violins II 192 / 290 from the second-instance swap, celli 156 / 328 / 355 / 388 / 670, partly the c46 stroke-trim change).

### 2. Bar 145: Clarinet 1's pp F4 is the loudest part of the pp chord and covers the first beat of the oboe's p dolce (measured)

**Where.** Clarinet 1, qn 575.9-582.07 (F4, pp, held into bar 146), under Oboe 1's p dolce from 578 (the coordinator's check point).

**Score (p.14).** Bar 145 is a pp chord: Clarinets 1-2 (F4 / D4), bassoons, Horns 3-4, strings, the timpani roll. Oboe 1 enters p dolce on beat 3 (G4 pickup into F5).

**Evidence (measured).**
- K re M over 576-578: Clarinet 1 -3.8, Bassoon 1 -8.9, Violins I -9.9, celli -10.3, Clarinet 2 -11.0, violas -13.6. Clarinet 1 is 5-7 dB over every other pp part and 7.2 dB over Clarinet 2 at the same pp.
- Oboe 1 minus the loudest other stem per half qn 578.0-582.0 (K): -4.0, +1.7, +4.7, +4.0, +4.0, +7.3, +5.6, +1.8, +4.9; the nearest voice is Clarinet 1 in 7 of the 9.
- On the same-dynamic scan (beats where four or more tracks share one flat printed dynamic), Clarinet 1 at pp sits +9.5 dB (median of 14 beats) over the median of the others. The other pp beats are its bars 175-177 "espr." solo, where a margin is wanted (+6.1 over the loudest other).
- Data (read): CC1 28 (pp), CC11 34-38, volume +1.1..+1.5 dB (the soft hairpin), soft trim pp 7.7 like the other winds. So the hot level comes from the patch's pp layer on this note, not from a mix setting (inferred).
- The violas are right here: Oboe 1 over violas +9.2..+18.6 dB K.

**Fix.** `build/roles.json` add `["Clarinet 1", [575.75, 582.0, -5, 0.25]]` (its next note at 582.5 is outside). Level only, so it can be a stem fix.
- Simulated: oboe minus the loudest other at 578.0 -4.0 -> +0.4, then +5.2 / +8.0 / +8.2 / +6.0 / +10.1 / +5.6 / +2.5 / +7.4 (Violins I now the nearest voice). The pp chord's parts at 576-578 within 2.2 dB of each other (Clarinet 1 -7.3, Bassoon 1 -7.5, Violins I -8.4, celli -8.8, Clarinet 2 -9.5).
- Master 576-578 -1.4 dB K; the delivery ride takes about two thirds of that back (ratio 3, inferred), and finding 5's ride trim covers this span.

### 3. Bars 35-38: the violins' mf motif is level with the bassoon's held notes and the clarinets' p chord (measured)

**Where.** Violins I qn 136.5-152 against Bassoon 1, Clarinets 1-2.

**Score (p.4).** After the bassoon solo (bars 33-34, f espr. > mf), Violins I enter mf with the first-theme motif in bar 35 and keep it to bar 38. Bassoon 1 holds mf long notes (breath at the end of bar 36; bars 37-38 a Bn 1-2 mf chord), Clarinets 1-2 hold a p chord with a < in bars 35-36, violas mp, celli and basses p.

**Evidence (measured).**
- Violins I minus the loudest other stem per qn 136.5-151.5 (K): +7.2, -0.7, +0.7, -5.8 (Bassoon 1), -2.0 (Clarinet 2), +1.7, +3.1, +0.9, +3.3, +1.6, +0.7, +0.7, +4.1, +3.9, +1.2, +0.6. Median +1.1; 3 of 16 beats under 0, 11 under +3. c45 had the same pattern (Violins I -10.2 dB re M at 139.5).
- At 140.5-141.5 the clarinets' p (Clarinet 2 -7.3 / -5.3 re M) is louder than the violins' mf (-7.4 / -8.2).
- Causes (read):
  - `roles.json` Bassoon 1 `[128.5, 140, 3]`, the solo lift, runs on into the violins' entry.
  - Clarinet 1's volume reaches +3.2..+3.4 dB at 140.0-140.25 (the soft-hairpin ramp on its p <).
  - Violins I carry row-trim and accent-body dips of -2.6..-4.0 dB at 138.0-138.3 and 140.25-140.8.
- RK (Principles, "Comparison of resonance"): in piano one string section equals one wind. An mf line should sit a dynamic level (3-5 dB) over p winds and over a held mf accompaniment.

**Fix (level only, `build/roles.json`).**
- Bassoon 1 `[128.5, 140, 3]` -> `[128.5, 137.0, 3, 0.5]`, and add `[140.0, 152.0, -3, 0.5]`.
- Clarinet 1 and Clarinet 2: add `[136.75, 144.0, -3, 0.5]`.
- Violins I `[144, 160, 2, 2]` -> `[136.25, 160, 2, 2]` (the existing lift starts at the motif's entry instead of bar 37).
- Simulated: Violins I minus the loudest other median +1.1 -> +3.7. Beats under 0: 3 -> 1 (139.5, -0.8: the motif's short eighths). Beats under +3: 11 -> 7.
- Bassoon 1 re M at 137-152 -5.2..-9.4 -> -7.0..-12.1, still clearly heard as the held line. The bar-34 solo is unchanged (Bassoon 1 minus violas +5.4). Master 136-152 -0.3 dB.

### 4. Bar 40: the celli's held A-flat3 is the loudest stem by 6-7 dB K over the violins' and woodwinds' run into the bar-41 sf (measured; K and A disagree on the size)

**Where.** Violoncellos qn 157.5-159.7 (A-flat3, f, crescendo to the sf at 160).

**Score (p.5).** Bar 40: celli and basses f whole notes with < to the bar-41 sf. Violins I, Flute 1 and Oboe 1 play a rising run (mf <). Violins II and violas hold f tremolo chords, Horns 3-4 a2 f, trombones p <, timpani pp <.

**Evidence (measured).**
- Celli minus the loudest other stem at 157.5 / 158.0 / 158.5 / 159.0 / 159.5: K +1.9 / +6.4 / +6.9 / +2.3 / +4.8. A, celli minus Violins I: +1.9 / +0.9 / +1.5 / +2.0 / +4.3. Celli re M -3.8..-6.5 K; Violins I -11.1..-13.5.
- On the same-dynamic scan the celli's f in bar 40 is +5.9 over the f median (-4.0..+3.7 in their other f bars).
- Data (read): note trim 156 +5.5 dB (c44 stroke trim, held to the note end), the c45 body cut -5 dB over 157.5-159.75 and the 144-156 crescendo gain +3 give +2.0 dB at 157.5-159.7, with CC11 at 88.
- A takes about 11 dB off the 208 Hz fundamental, K almost nothing. At f the ear's weighting of 200 Hz against 1 kHz lies between the two, nearer K (inferred). The c45 B #4 check that passed this bar used A.

**Fix.** In `build/score_config.py`, change the end of the c45 B #4 celli row (`[(152.75, 0.0), (153.5, -2.0), ...]`): replace `(157.0, -3.0), (157.5, -5.0), (159.75, -5.0), (160.0, 0.0)` with `(157.0, -3.0), (157.5, -8.0), (159.6, -8.0), (159.75, -5.0), (160.0, 0.0)`. Level only.
- Simulated: celli minus the loudest other (K) -1.1 / +3.4 / +3.9 / -0.7 / +4.2. Celli minus Violins I (A) -1.1 / -2.1 / -1.5 / -1.0 / +3.6.
- The step into the bar-41 sf grows +6.1 -> +6.5 dB K; master 156-160 -0.45 dB.

### 5. The delivered span is 19.35 dB against 16-19: the c46 fff lift raised the top while the soft floor stayed (measured; fix simulated)

**Evidence (measured, mp3 short-term loudness).**
- p10 -30.62 LUFS (c45 -30.60). Maximum -11.26 at 356.4 s, qn 638.6 (c45 -11.51). Span 19.08 -> 19.35.
- The +0.25 dB on the maximum comes from the `_all` +1.0 dB row at 636-637.25.
- The frames at or under p10 lie in bars 1-5, 14, 34, 43-44, 76, 144-145, 154-155, 165-166 and 175-182.
- Climax order (S max): 160 -11.26 > 122 -12.08 > 167-170 -13.58 > 26 -14.24. Keep it.

**Fix (delivery only; render and balance unchanged).**
- `RIDE_TRIMS` in `build/score_config.py` (read by `deliver_master.py`): +0.5 dB over qn 0-24, 52-56, 129-136, 168-176, 300-304, 572-584, 612-620, 656-664 and 696-728. Each row is `[(a, 0.0), (a + 0.5, 0.5), (b - 0.5, 0.5), (b, 0.0)]`; the opening row starts at `(0.0, 0.5)`. The coda row begins after the existing 679.95-695.9 row.
- Simulated on the c46 S curve: p10 -30.62 -> -30.23, span 19.35 -> 18.96. The climax is untouched.
- Not enough on its own: `DELIVER_RATIO=3.3` (run with the c46 master) gives 19.1 dB and LRA 14.8.
- Confirm with the span line that `deliver_master.py` prints.

## The coordinator's checks (no change proposed; measured on the final c46 stems)

**Violas (the c45 fault).** Right everywhere the coordinator named:

| Check | c45 | c46 |
|---|---|---|
| Bar 34: Bassoon 1 minus violas, per qn 132-135 (K) | -2.9 / +4.0 / +2.4 / -5.0 | +4.2 / +2.4 / +7.3 / +7.6 |
| Bar 35: Violins I minus violas at 136 / 137 (K) | -1.9 / +0.7 | +7.8 / +8.7 |
| Bar 129: violas re M at 514-516 (A) | -10.2 / -12.9 / -8.5 | -14.7 / -13.7 / -9.6 |
| Bar 129: clarinet solo over violas (A) | | +13.8 / +13.5 / +4.5 |
| Bars 135-136: melody (Flute 1 + Oboe 1 + Violins I) minus violas (K) | +5.2..+11.2 | +8.4..+14.4 |
| Bar 145: oboe over violas (K) | | +9.2..+18.6 |

In bars 135-136 the violas sit level with Violins II (-3.8..+0.6), which is right for two inner mf accompaniment parts.

**Timpani rolls (Dan's priority): no long roll drowns a part (measured).** Per 1 qn window, the roll's rank among 39 stems (K), and the roll minus the loudest other stem (K):

| Roll (bars) | Rank | Minus loudest other: median / max |
|---|---|---|
| 1-4, ppp (solo opening) | 1, then 3-4 | |
| 13-14 | 6-11 | -17.9 / -11.2 |
| 40-44 | 4-15 | -10.8 / -5.6 |
| 62-63 | 4-9 | -7.6 / -5.2 |
| 80-82 | 4-10 | -6.9 / -2.7 |
| 115-116 | 13-24 | -8.4 / -6.6 |
| 117-131 | 2-22 | -9.1 / -0.6 |
| 140-141 | 7-20 | -7.0 / -4.6 |
| 144-146 | 2-10 | -11.2 / -4.3 |
| 158-161 | 4-18 | -5.7 / -1.5 |
| 166-170 | 1-17 | -6.2 / +0.2 |
| 174 | 3-6 | -18.6 / -17.4 |
| 181-182 | 7-9 | -9.0 / -5.4 |

- The rank-1 and rank-2 beats are strokes or arrivals at the printed dynamic, not held rolls: the bar-167 f arrival (664.0-664.5, before the tune enters at 664.5; then -15..-18 re M), the bar-124 decrescendo (492), the mp start of bar 144 (572; it settles to rank 7-8 by 576), the bar-141 ff arrival stroke (560.0).
- The c46 changes did what they planned:
  - bar 174: roll -21.0..-18.1 re M (c45 -17.2..-13.7), the solo +17.4..+20.6 over it;
  - bars 13-14: the horn solo is +11.9..+21.5 over the roll, and the roll is +2.9..+6.5 over the celli and basses in 78-196 Hz (c45 +5.2..+9.5);
  - the crescendo rolls grow toward their arrivals: bar 62 roll -10.9 re M at 246-247 (c45 -13.1 / -14.3), bar 115 -14.6 at 459 (c45 -18.2), bar 140 -12.6 at 559 (c45 -15.9).

**Letter F.**
- Downbeat tune minus brass (K): +2.1 / +1.7 / +2.6 / +4.8 / +2.2 -> +4.9 / +4.2 / +5.1 / +6.9 / +4.1. Right channel +2.4..+5.1. Beats 3-4 +6.1 / +7.5 / +2.2 / +3.0 / +7.7.
- The half notes still sit over the Horns 3-4 chords (+0.7..+4.9 K), so the f answer is heard.

**fff arrivals.**
- Master K per beat into 636: 52.1 / 53.0 / 53.9 / 55.7 -> 59.1. The crescendo grows on every beat; the c41 stall is gone.
- Into 484: 52.5 / 53.9 / 54.2 / 54.2 -> 57.6. The last beat of bar 121 is flat (the low brass's eighth rest).
- Delivered beat RMS steps +3.7 / +4.0 dB.

**Opening swell.** Celli + basses K per qn, 3 -> 6 -> 10: 24.5 -> 30.8 -> 35.8 (c45 24.5 -> 27.8 -> 34.1). The ppp roll stays at 18.7-20.9 and is under the strings from qn 3.

**Dynamic mapping (K, same-dynamic scan).** Does p sound like p in every family?
- **Soft dynamics.** At pp, p and mf the families lie within ±3 dB of each beat's median, with these exceptions:
  - Clarinet 1 pp: finding 2.
  - Basses p -3.5 / pp -2.5. This is pitch-dependent: in bars 6-7 G2 / F2 sit 10-11 dB under the celli, while C2 in bar 5 sits level.
  - Horn 4 p -3.4, Bassoon 2 p -3.3.
- **Loud dynamics.** At f and ff:
  - Second winds sit 3-6 dB under the median: Clarinet 2 f -5.8 (the bars 117-120 triplets, under every ff part anyway), Contrabassoon f -5.1, Flute 2 -3.6 / -3.1, Oboe 2 -3.4. These are inner voices.
  - Trumpet 1 is +2.5 / +3.7 / +3.3 at f / ff / fff as the lead; finding 1 raises bars 70-71.
  - Trombone 1 f is +2.7, and +4.8..+6.4 in bars 131-134, where it carries the recap theme with clarinets, bassoons and celli.
- **RK's forte ratios.** Over the woodwind median at f: horns +0.8, trumpets +1.6, trombones +1.5 (RK: +3 / +6). The brass are light, as c46 B found. No general change: most f brass beats accompany ff tunes.

**New trumpet and percussion tracks.**
- Trumpets a2 and Horns a2 show no state change (finding 1 is Trumpet 1 only).
- Tam-tam fff is the loudest stem at 484-491 (-5.7..-10.7 re M), as printed (heavy beater).
- The pp tam-tam at 696-703 ranks 4-10 (-8.9..-19.3 re M).
- The suspended cymbal peaks at -18.0 re M at 635; the K Crash ring sits at -16..-29.

**Dan's standing checks.**
- **Loop pulsing.** 53 held spans of 6 s or more, scanned with the c25 loopscan method; 12 are too short to judge. One span is over 0.6: Bass clarinet G2 at 492 (bars 124-125), 100-300 Hz 0.68 and centroid 0.68 at 3.95 s, but 13.1 dB under the master.
- **Brass accents.** 2-5 kHz energy over the first 80 ms minus the body, on 177 accents: medians -8..-27 dB. Only Trumpet 1 284 (+4.4) is over +3, and it directly follows the flipped 283.5 note; re-measure after the finding 1 splice.
- **S1.** Same-pitch repeats, stem dip median: strings 4.3 dB (34% under 3 dB, mostly re-bows of held notes and merged legato repeats), winds 7.4, brass 9.5. Lens A's measures take precedence.
- **S2.** Not re-measured for this lens.
- **S3.** At bar 62 the master falls from -32 to -37 dB over 0.3 s, with no cut in the hall.

**Do not touch:**
- the violas' c46 stem and lanes (Violas `rt_gain_db` -6);
- the bar-174 timpani role 2, the bars 13-14 timpani shape and the crescendo-roll ramps;
- the letter F half-note cuts with the eighth-figure lifts;
- the `_all` fff arrival rows at 636 / 484, the opening swell shapes and the c45 B #2-#4 data (except the finding 4 tail);
- the oboe's bar-145 trim and role;
- the tam-tam, suspended-cymbal and K Crash levels;
- the hall, every send and the release caps;
- the climax order 160 > 122 > 167-170 > 26.

# Critic B, cycle 9 (render c08): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 116-117 and 121-126; second reading of the c03 B row)

c03's B report read these pages on the c02 render. Each of its notes is checked again on c08 (`cycles/c08/rendered_build/parts.json`, the c08 stems).

| Page | What the manual says | Where it applies | Does c08 follow it? |
|---|---|---|---|
| p.116-117 | Crash pairs: three lengths on white keys, 3 round robins; CC11 and velocity set loudness, velocity selects 7 layers. The 22in K appears only in the Combo list. | Crash cymbals: `22in Zildjian K Crash.oib`, key 60 (long), v124 at qn 888, 1048, 1108 (all fff). | Yes. Measured K-weighted: at 888-890 the crash is the 4th-loudest stem (-23.8 dB, the master -12.6). Bar means are -28.1 dB at 263 and -26.0 dB at 278, and the crash is never the loudest stem. It is heard but does not dominate. No change. |
| p.121-122 | Bass drums: C1 felt short, D1 felt long, felt and hard rolls and crescendos; velocity selects up to 12 layers, 4 round robins. 36in Ludwig: "deep, rumbling ... woody hit". | Bass drum: key 38 (D1, felt long), qn 888 and 1108, printed ff. | Yes. Since c03 it plays v114, not the fff layer. Measured: its 20-100 Hz share re the master is -7.6 dB in bar 223 and -6.7 dB in bar 278, which is weight without covering. |
| p.123, 125-126 | Timpani Long: two strokes within 65 ms play a damped double hit; left hand C1-A2, right hand C3-A4; up to 16 velocity layers. | 179 notes on Hrd Lng / Hrd Rls; `TIMP_RH_ALT`. | Yes. The closest pair of onsets is 0.17 s apart, and none is under 65 ms (measured). |
| p.124-126 | Timpani rolls: CC1 crossfades 8 layers; hard sticks give "clear individual hits". | 21 roll notes. | Mostly. All 21 rolls sit 14-26 dB under the master and rank 11th or lower among the stems (measured; Dan's rule holds). The exception is the sfp roll at qn 592: its CC1/CC7 fall to the p layer (CC1 71, CC7 43-48), but a +13.3 dB volume step at 592 cancels the fall (finding 4). |
| p.124, 126 | Short hits (C#0) for stops within a beat or two; hard-stick shorts are "more pronounced". | Not used. The quarter strokes followed by rests in bars 265-272 ring on Lng. | Open. This is an articulation question, not balance. |
| p.123, 125 | Recorded crescendo rolls (E0, Hard Cresc), 2 velocity layers. | Not used (MANUAL-GAPS #12). | Open. The 876-888 crescendo roll (sub. p to fff) rises to rank 11 and does not cover, so no balance finding needs it. |

MANUAL-GAPS.md read: #10 is done and #12 is open (above). #6 (CC16 reset) works (c08). No other gap is a balance item.

## Method

- Data: the c08 stems 01-35 and the master, framed by a 4096-point STFT with a 25 ms hop and stereo power. K-weighting is applied as the BS.1770 power response. I also kept band powers (20-100, 100-250, 125-250, 250-500, 500-2k, 2-5k, 5-12k, 4-8k Hz) and the side power below 250 Hz. Times come from the rendered parts.json tempo map, with no render shift for c08.
- Printed dynamics come from `build/mockup-events.tsv` per staff. "Sounding" means a note of that track overlaps the window (parts.json `sq` and `dur`).
- Balance targets: Rimsky-Korsakov's resonance ratios as earlier B reports used them. At p one wind equals one string section. At f a string section is about +3 dB over one wind, a horn equals two winds, and a trumpet or trombone equals two horns. Accompaniment sits 3-7 dB under a melody at the same printed level.
- Dan's checks through this lens:
  - Item 5 (rolls): table above. No roll covers.
  - S3: finding 3 uses CC on sounding notes and volume steps only at fresh entries.
  - Item 4: no proposed change touches an accent front.
  - Item 7 (loop pulsing): no new held-note change is proposed.
- Coordinator items: see the last section (wetness, width, the open items).

## 1. The harp's ff chord at bar 132 plays the Nail Pick zone and stands 10 dB over the whole orchestra (measured)

**Where.** Harp, qn 524.0 (bar 132, beat 1, "non arpegg.", accent, ff), six notes G2-B4. The orchestra is marked f.

**Evidence (measured).**
- Velocity 126-127 on all six notes. The harp map tops out at 118 for ff (`score_to_parts.py`, harp branch), and the accent pushes the chord above that.
- In Harp Sus RR, velocity 124-127 plays the Nail Pick instead of the pluck (manual p.69; DIGEST §10). It is the only harp chord at 120 or higher. The final ff chord at 1108 plays v116.
- K-weighted over 524-524.5, the harp is -19.6 dB and the master -17.7 dB. Without the harp the master would be -22.2 dB, so this one chord raises the master 4.5 dB.
- Over 524-525 the harp is -21.6 dB. The next stems are the celli and Horn 3 at -32.1 dB, so the harp leads by 10.5 dB. Over the bar before (523-524) the harp was -42.4 dB.
- A harp in an f tutti is a colour. Even at ff it should sit near the loudest single stems, not 10 dB over them (Adler on the harp in tutti: it carries only in thin scoring).

**Fix.**
- `tools/score_to_parts.py`, harp velocity block (around line 3117): clamp the final harp velocity to 123 after the accent, arp-top and `HARP_PITCH_VEL` additions. Use a new option `HARP_VEL_MAX = 123` (default None), set in `build/score_config.py`. This keeps every harp note out of the Nail Pick zone.
- `build/note_trims.json`, Harp: `"524.0": -5`, using the plucked-note step shape (full value at onset - 0.01 s).
- Target: the harp 1-3 dB over the loudest other stem over 524-525 (about -29..-31 dB K). Refit the trim by stem fix if the pluck layer lands elsewhere.

## 2. The F2 counter-melody (violas + celli, bars 67-73) is 8.5 dB under the tune and level with the harp's accompaniment (measured)

**Where.** qn 264-292 (bars 67-73): Violas and Violoncellos, "arco, unis., espress." / "arco espress.", mp, in unison (MIDI 53-67). The tune is in Violins I and II (mf, octaves). Harp broken chords mf; Horn 1 pp.

**Evidence (measured, K-weighted).**

| qn | tune (Vln I+II) | counter (Vla+Vc) | harp | Vla | Vc |
|---|---|---|---|---|---|
| 264-292 | -36.0 | -44.5 | -44.0 | -46.7 | -48.6 |
| 292-304 | -37.3 | -39.8 | -41.8 | -41.8 | -44.2 |

- In bars 67-73 the counter-melody is 8.5 dB under the tune and 0.5 dB under the harp's broken chords, which already carry a -6 dB role. Per bar the violas run -45.7 to -48.5 dB and the celli -45.4 to -51.0, against the harp's -43.6 to -44.6.
- The score prints one dynamic step between the lines (mf against mp). The composer's own note in `sections/sTwo.ily` (c094, Rimsky-Korsakov p.51) says the counter-melody should be heard: "in soft passages one string section = one wind; the counter-melody in unison (Vla + Vc) outweighs the tune spread in octaves". Bars 74-76 are already right (2.5 dB under the tune).
- Current roles: Vc +2 and Vln II +3 over 264-328; violas have none there.

**Fix.** `build/roles.json`:
- Violas `[264, 292, 4.0, 2.0]` (+4 dB, released over 292-294).
- Violoncellos: split the existing `[264, 328, 2.0]` into `[264, 292, 5.0, 2.0]` and `[292, 328, 2.0]`.

Simulated: the counter goes to -40.9 dB, which is 4.9 dB under the tune and 3.1 dB over the harp. No change after bar 74.

## 3. The sub. p at bar 219 drops the master only 1.7 dB: the strings enter about 11 CC above p, and the fresh brass entries sit at +10..+12 dB soft trims (measured; cause in PHRASE_SHAPE inferred)

**Where.** qn 872 (bar 219, "sub. p" in winds, horns 1-2 and trumpets; p in the other parts). Bar 218 is f > mf (winds, Hn 1-2 espress. f) and mp/mf (strings).

**Evidence (measured).**
- Master 869-871.8 -31.6 dB, then 872.3-874.5 -33.3 dB K: a 1.7 dB drop.
- Strings: `dyn_curve` is 46 (p) at 872 on every string track, but the written CC11 at the onset is above it:
  - Violins I 57-58, Violins II 61, violas 60, falling to 50-52 only by qn 875.6;
  - celli 51 rising to 54, basses 55.
  - The fall from mid-mp to p over the first bar matches PHRASE_SHAPE's "drive" type (tempo 144 qpm: starts high and falls), applied at a subito-softer onset. This cause is inferred.
  - K-levels over 872.2-876: Vln I -42.5, violas -43.9, celli -44.1, basses -44.5 dB. That is 6 dB over the celli's own p median (-49.9) and 3 dB over the basses' (-47.3), from the note table over the whole piece.
- Brass: the trombones, Horns 3-4 and Trumpets 1-3 enter fresh after rests. They have CC1 36 but soft trims of p +11.8..+12.6 (mix.json). Horn 3 is -43.5 dB, the loudest stem of the p chord. Horn 1, also at CC1 36, is -54.2 dB.
- Simulation: strings -3 dB plus the fresh brass entries -4 dB gives a drop of 1.7 -> 3.9 dB.

**Fix.**
- `tools/score_to_parts.py` PHRASE_SHAPE: a phrase whose first onset carries a subito-softer mark (`sub_soft_q`, the set SUBITO_FRESH already builds) takes no positive start offset. Clamp the shaped CC at the printed value until the next hairpin starts, or type it "build". Check that Vln I/II, violas, celli and basses write CC11/CC1 ≤ 46 at 872.0-876.0. This is the S3-safe route: a CC fall acts before the hall.
- `build/roles.json`: Horn 3, Horn 4, Trombone 1, Trombone 2, Bass trombone and Trumpets 1-3 get `[871.7, 876.0, -4.0, 4.0]`. All of them rest in bars 217-218, so the step falls on fresh entries, not under a sounding chord. Do not apply it to Horns 1-2, which tie in from bar 218.

## 4. sfp at bar 149 (qn 592): the winds' led notes start on CC 46 before the sf, and the timpani roll jumps +13 dB at the sf, so its p is louder than the ff roll before it (measured)

**Where.** qn 591.8-596 (bar 149). sfp < ff on Fl 2, Cl 1, Bn, Hn 3, Tpt 3, Tbn, strings and timpani. Trumpets 1-2 are printed ff with accented half notes straight through (no sfp).

**Evidence (measured).**
- The sfp lead moved the notes' onsets to 591.79-591.89, but the CC at the moved note-on is the p value. Flute 2, Clarinet 1, Bassoon 2 and Horn 3 all have CC11 46 there (CC1 42-55), then jump to 114 at 592.02.
- So each sf starts on the p layer for 0.13-0.23 qn and swells into the spike. This explains c08's "sf peak 0.27 s late" (the master's sf frame falls at 592.5 instead of 592.0).
- Timpani, roll at 592:
  - The volume envelope steps from +0.2 dB at 591.5 to +13.3 dB at 592.0 and stays at +12.6..+13.8 through 596. This is the roll-crescendo gain, applied from the sf instead of rising from the p.
  - CC1 71 / CC7 43 select the p layer, but the timpani measures -36.2 dB at 593.0 against -37.4..-38.6 dB in the ff roll before (588-591.5): the p is louder than the ff.
  - It then reaches -28.7 dB by 598.5, 9 dB over the ff roll.
- Drops from ff (590-591.5) to the p (593.0-593.75): violas 12.2, Vln I 11.4, Tbn 1 10.8, Hn 1 10.1, Hn 3 6.3, Cl 1 4.6, Bn 2 1.9, Fl 2 0.8 dB. The timpani rises 0.9 dB, Trumpet 1 falls 3.7 dB and Trumpet 2 rises 0.5 dB (both printed ff). Master -16.1 -> -22.4 dB (6.3 dB).
- c08's 10 dB target for the master is not reachable as scored, because Trumpets 1-2 keep playing ff. The right check is the sfp parts' own drop: target 10 dB or more on each, measured on the stems.

**Fix.**
- `tools/score_to_parts.py`, sfp spike (SFP_SPIKE_S / the c08 sfp leads): write the spike's CC value at the note's moved onset (`qn`), not at the score onset. Equivalently, when a led note starts on an sfp mark, move the spike's first point to the lead.
- Timpani roll crescendo gain (the `roll_db` / hairpin-gain code for timp chains): when a roll's crescendo starts from an fp/sfp mark, start the dB ramp at 0 at the p point (592.0 + SFP_SPIKE_S[1] in qn) and reach +13 dB at the crescendo's end (596), not at 592. Target for the timpani at 592.5-593.5: 10 dB or more under the 588-591.5 roll (about -48 dB K).
- Expected for the winds: drops of 8 dB or more on Fl 2 and Bn 2, and the sf on time (pcX).

## 5. Chorale: c08's +2 dB horn role overshot on K-weighting; the chorale's top line (Trumpet 1) is under the horns (measured)

**Where.** qn 892-928 (bars 224-232) and 1032-1047 (bars 259-262).
- At 224-228 the chorale tune is Trumpet 1 (G4-E5-D5-C5-D♭5-C5) doubled an octave below by Trombones 1-2 a2. Horns 1-4 and Trumpet 2 hold the harmony.
- At 259-262 the top line is Trumpets 1-2 a2. UNI_BOOST already gives the kept Trumpet 1 copy +3.0 dB.

**Evidence (measured, K-weighted, each stem minus Trumpet 1 over the span).**

| qn | Tpt1 | Hn1 | Hn2 | Hn3 | Hn4 | Tbn1 (a2) |
|---|---|---|---|---|---|---|
| 892-900 | -34.1 | -3.5 | -1.4 | +0.3 | -5.8 | +0.2 |
| 900-916 | -37.2 | +0.4 | +1.8 | -5.8 | -0.4 | +3.0 |
| 916-928 | -36.8 | +1.6 | -1.4 | -2.1 | -1.1 | -0.1 |
| 1032-1044 | -28.2 | +1.7 | | -0.2 | | +2.1 |

- c08 B #1 added +2 dB to Horns 1-4 at 892-928. CHANGES.md measured it on plain RMS (+3.7/+3.6/-1.8/+1.5 dB) and asked for a K-weighted re-check against the 2-4 dB-under target. On K-weighting the harmony horns are now 0.4-1.8 dB over the tune in 900-928, and Horn 3 is level with it in 224-225.
- Trombone 1 carries the a2 octave doubling of the tune, so its +3 dB in 900-916 is the tune and not a fault.
- In 259-262 the a2 trumpet top line is 1.7-2.1 dB under Horn 1 (Hn 1-2 a2, the octave below) and Trombone 1.

**Fix.** `build/roles.json`:
- Horns 1-4: `[892.0, 928.0, 2.0, 4.0]` -> `[892.0, 928.0, -1.0, 4.0]`. That is -3 dB from now: K-weighted Hn1 -2.6..-1.4, Hn2 -4.4..-1.2, Hn3 -2.7 dB re Trumpet 1.
- Trumpet 1: add `[892.0, 928.0, 1.0, 4.0]` after the existing 888-892 +5 arrival row, and `[1032.0, 1047.5, 2.0, 1.0]`.

## 6. Flutes and clarinets are no louder at f than at mf: their f trims (-4 dB) undo the CC step (levels measured; cause inferred from mix.json)

**Where.** Flute 1, Flute 2, Clarinet 1, Clarinet 2, every f passage. f onsets include qn 72-116 (bars 19-30), 136-156, 328-340, 520, 576-672.

**Evidence (measured).** Median K-level of note bodies (notes of 1.5 qn or more, from +0.25 s to the end), by printed dynamic:

| track | mf | f | f - mf |
|---|---|---|---|
| Flute 1 | -39.0 (12) | -40.6 (29) | -1.6 |
| Flute 2 | -39.8 (7) | -45.8 (12) | -6.0 |
| Clarinet 1 | -43.7 (21) | -43.5 (27) | +0.2 |
| Clarinet 2 | -42.7 (19) | -43.4 (14) | -0.7 |

- Every other family rises from mf to f: Oboe 1 +2.4, Bassoon 1 +1.7, Horn 1 +6.5, Trombone 1 +3.9, Violins I +3.0, violas +5.1, celli +3.8 dB.
- `build/mix.json`: Flutes have soft_trim mf +2.5 and dyn_trim f -4. Clarinet 1 has +2.5 / -4.2, Clarinet 2 +3.0 / -3.8. That is 6.3-6.8 dB of envelope against the 16 CC step from mf (72) to f (88), which is about 3 dB on these patches (kit LEARNINGS §4: woodwinds 1.8 dB per 10 CC).
- In bars where both the wind and Violins I are marked f, the winds sit 5-8 dB under Violins I: Fl1 -6.3 dB (23 bars), Cl1 -8.2 (19), Ob1 -5.0 (25). Rimsky-Korsakov's forte ratio puts one string section about 3 dB over one wind.

**Fix.**
- `build/mix.json`: Flute 1, Flute 2, Clarinet 1 and Clarinet 2 `dyn_trim_db.f` -4 / -4 / -4.2 / -3.8 -> -1.5. Leave ff and fff unchanged.
- Where an accompaniment then comes within 3 dB of the tune, cut it in `roles.json` rather than through the dynamic trim. The clarinets' broken chords under the F1 tune at qn 40-104 are the likely place: Clarinet 1/2 `[40, 104, -2.5, 2.0]`.
- Check the mf→f step on these four tracks after the render (target +2..+4 dB, as in the other families).

## Coordinator items

- **Wetness (verified, measured on the master).**
  - Genuine tutti stops at qn 101.75, 373.75, 450, 662 and 1112.75 fall 20 dB in 0.30-0.40 s (median 0.35 s). The drop at +0.3 s is 15.9-20.2 dB.
  - RT60 from the -5..-25 dB slope is 1.12-1.58 s (median 1.28 s).
  - c08's claims (0.39 s, 1.26 s) hold, inside Dan's ceiling (0.50 s, 1.5 s).
  - The detector also flags bars 1, 5 and 204 (0.80-0.85 s), but those are chords decaying under the bar's own notes, not stops.
- **Width below 250 Hz (measured; simulated proposal).**
  - Master, 20-250 Hz: correlation 0.735 and side/mid -8.2 dB on the loudest 10 % of frames; 0.70 on active frames. This confirms c08's 0.72 as too mono.
  - The stems with the -8 dB side shelf read 0.80-0.85 (trombones, bass trombone, timpani, contrabassoon) and 0.64-0.73 (celli, basses, tuba).
  - Model: an incoherent sum of the stems' side and mid powers reproduces the master (0.727 against 0.735). Raising the side shelf on those tracks and returns gives:
    - -8 -> -6 dB: 0.61 loud / 0.58 active;
    - -5 dB: 0.54 / 0.51;
    - -4 dB: 0.45 / 0.42.
  - Propose -6 dB, not the -4 dB c08 suggested, which would overshoot the references (0.54-0.62). This is a mix-only change: `side_shelf` on celli, basses, tuba, trombones, contrabassoon, timpani and the four returns. Movement I's Main-at-seat layout is needed only if -6 misses.
- **Open items outside this lens:** the Vc 832 / Vln I 884 repeats (articulation) and 4-8 kHz (blend). Not measured here.

**Do not touch:**
- the timpani roll levels (all rolls 14-26 dB under the master, rank 11 or lower);
- the crash (v124, heard and never the loudest stem) and the bass drum (v114);
- Trumpet 1's open solo (bars 51-66, 6.4 dB K over Clarinet 2; the pizz peaks -52.5..-55.5 match the clarinets' pp bodies -51..-53, so pp reads as pp across families);
- the muted Trumpet 1 with the cor anglais (bars 171-186, within 1 dB in unison);
- theme B in the trumpets (bars 211-218, 6 dB over every other stem);
- the bassoon solo at bar 115 (10.5 dB over the next stem);
- the wetness numbers above, and the climax order (223 and 278 loudest);
- c08's basses metric tables and FINAL_RING.

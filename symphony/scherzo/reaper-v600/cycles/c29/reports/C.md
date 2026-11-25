# Cycle 29, critic C: blend and space (lens C1), on the c28 render and its delivered mp3

Sources: the c28 stems, returns 91-94 and master (`cycles/c28/render/`); the delivered `cycles/c28/scherzo-mockup-c28.mp3`, decoded at 48 kHz and aligned to the master at +239 samples; `cycles/c28/build_render/` (parts.json, mix.json, roles.json); and the c18 stems and data for comparison. The c18 levels are lowered by 3 dB to allow for `global_gain_db`. Times come from the parts.json tempo map. Bar b starts at qn 3(b-1).

Terms used below:
- Levels are mean-square dB.
- "corr" is the L/R correlation at 300 Hz-8 kHz.
- "L-R" is the left level minus the right level at 300 Hz-8 kHz.
- "Band share" is a band's energy against the whole signal.

My scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c29-C/` and have been deleted.

## Manual notes

MANUAL-READING.md has no row for c29, so I did no scheduled reading. I used MANUAL-GAPS.md (#6, #7, #10, #13), and I read the pages behind the routing and mic findings: May 2021 HO manual PDF pp. 138-141.

| reading (PDF page) | where it applies | does the render follow it |
|---|---|---|
| p.138: Close mics take the direct sound. Main (Decca tree, fifth row) takes mostly room reflections. | The oboes play with Main 20.6 dB under Close and the cor anglais with Main 11.6 dB under (finding 4). Horn 1 is Close-led (Close -1.4 / Main -5.2). Horns 2-4 take the template mix (Close -6.3 / Main 0). | Partly. The oboes carry almost no recorded room, and Horn 3's mix differs from Horn 1's, the horn it relays with (finding 1). |
| p.140: Master Channel Pan keeps the relative panning of the mics. | `seat`, `reaper_pan` | Yes. All four horns share seat -0.25, with REAPER pans -0.18..-0.13. |
| p.141, 4.2.6 Channel Routing: "Mono From Left" outputs the left channel to both sides and discards the right channel. It is set per instrument (build_reaper `apply_mix` writes `channelMap` for the whole instance). | Horn 3 `channel_map` 2 since c18, set for one held note (G sharp 4 at qn 1092) | It applies to every Horn 3 note: the bar 105-120 countermelody, the trio drone, the 341 recall and the relay at 1092-1101 (finding 1). |
| p.141, 4.2.7 Stereo Double: works only with Stereo routing. | Violas div 0.6 and Violin I solo 0.4 (Stereo, working). Horn 3 cannot take it while on Mono From Left. | Yes, where it is used. |
| MANUAL-GAPS #6 (hard sticks, adopted in c28) and #7 (recorded crescendo rolls) | Timpani, one instance. The score prints "soft sticks" from bar 341. | #6 holds to bar 340. After 341 the strokes are still hard sticks (finding 3). |
| MANUAL-GAPS #13 (Mid or Main instead of Close on the winds) | oboes, cor anglais | Not tried on any wind. The c25 C #2 test is still pending (finding 4). |

## What passes on c28 (measured; keep)

- **Hall, master and mp3.** G.P. after the fff: I placed the cut-off at the last 10 ms frame within 6 dB of the bar's peak. That is a stricter reference than the actor's measure, so my drops are smaller than the 18.7 dB in CHANGES.md.

  | | drop at +0.3 s | 20 dB fall | 40 dB fall |
  |---|---|---|---|
  | c18 master | 16.7 dB | 0.40 s | 0.91 s |
  | c28 master | 14.9 dB | 0.42 s | 0.90 s |
  | c28 mp3 | 13.0 dB | 0.45 s | 1.0 s |

  All three are inside Dan's limit (at least 13 dB, a 20 dB fall within 0.50 s). The mp3 is at the edge on the drop, so the hall must not get any wetter.
- **Wet/dry is unchanged since c18, so the louder strings and the CC7 moves did not change the room.** Return against dry, c18 -> c28:

  | return | change in every section | exception |
  |---|---|---|
  | R Strings | within 0.4 dB (-12.9..-11.2) | trio 209-224: -11.7 -> -10.5, from the louder celli and violas (finding 2) |
  | R Brass | within 0.2 dB | |
  | R Winds | within 0.5 dB | |

  CC7 acts before the sends, so the level changes carried their own hall with them.
- **Hard-stick timpani in the room.**
  - Wet/dry in the tuttis: -12.6..-12.8 dB (felt -13.0).
  - Correlation 0.32-0.36 against felt 0.32-0.34. L-R -1.5..-1.7 against -1.6.
  - The template's Surround-led mics keep the brighter stick at the back of the hall. Only the timbre changed: level-matched, 1.5-4 kHz is +15..+20 dB in the soft strokes, +3..+10 dB in the loud ones.
  - Rolls are 1.5-3 s long, too short to show the 3.95 s loop.
- **Trumpets and horns are in one hall.**
  - In 312-360, Trumpet 1 reads corr 0.87 / L-R -3.6 and Horn 1 reads 0.91 / +4.1, both on R Brass with Main-led mics.
  - The trombones read 0.80-0.83, L-R -4.2..-5.5.
- **Low end in the tuttis (master band shares, 100-250 / 250-500 Hz).**

  | passage | 100-250 Hz | 250-500 Hz |
  |---|---|---|
  | 101-120 | -8.7 | -5.3 |
  | 301-320 | -9.2 | -6.1 |
  | 329-339 | -10.5 | -6.1 |
  | basses' div. pizz. 253-268 | -9.4 | -8.5 |
  | references: Dvořák | -6.6 | -6.3 |
  | references: Brahms | -7.6..-8.8 | -5.95..-6.3 |

  There is no build-up, and every value is within 0.6 dB of c18. The only passage that got thicker is the trio climax (finding 2).
- **Tone matches between sample sets.**
  - Violins II con sord. against open (2-8 kHz against 0.2-1 kHz): -12.0 against -8.1 dB. The mute is audible.
  - Violas div against Violas in 624-672: -15.5 against -15.3, the same colour. The Stereo Double gives corr 0.77.
  - Violin I solo: corr 0.94, L-R +5.5, a point source at the Violins I seat.
  - Handover from the borrowed harmonic E6 to the harp harmonics: -52.4 -> -51.9 dB, L-R +4.9 -> +4.4.
- **Flute 1 "col Vl. solo" (1044-1068)** is 6.6 dB under the solo (-49.2 against -42.6; c24 was 8.4 dB under). That is close to c25's 5 dB target. Leave it.
- **S3 on the mp3.** At the sub. p of 360, the level 0.3 s after the cut-off is 13.7 dB down on the mp3 against 15.2 on the master. At 828 it is 5.0 against 8.2, and the hall of the louder level keeps ringing under the p.

## Findings, ranked by what a listener hears

### 1. Horn 3 plays "Mono From Left" for the whole movement. The closing G sharp relay jumps in place and colour, and in bars 105-120 the two-horn countermelody is one mono point (measured; audibility inferred)

Where:
- Horn 3, all notes. Most exposed: the relay of the held G sharp 4 at the close. Horn 1 plays 1077-1097 and again from 1101. Horn 3 enters at 1092, pp, alone from 1097 to 1101, under the Violins I's ppp G sharp 5.
- The tenor countermelody of bars 105-120 (qn 312-360). There Horns 3-4 play a2: Horn 4's 28 unison notes are dropped (`unison_dropped`), so Horn 3 plays the line alone.
- The trio drone (153-168) and the recall at 341 (Hn 3 dolce).

What is wrong (measured):
- c18 set `channel_map` 2 to cure one note: Horn 3's G sharp 4 cancelled in mono under the template mix (corr -0.70, mono loss 8.3 dB). Channel routing applies to the whole instrument (p.141), so every Horn 3 note is now a dual-mono copy of the left channel.
- Horn 1 cured the same problem in c17 with a Close-led mix instead. The two horns that relay one held note now sound like two different instruments in two places:

  | stem, span | corr | L-R | harmonics 3-8 against 1-2 | centroid |
  |---|---|---|---|---|
  | Horn 1, 1083-1092 | 0.69 | +1.0 | -8.5 dB | 740 Hz |
  | Horn 3, 1094-1097 | 1.00 | +4.1 | -14.9 dB | 498 Hz |
  | Horn 3, 1097.5-1100.5 | 1.00 | +4.1 | -12.9 dB | 551 Hz |
  | Horn 1, 1103-1110 | 0.80 | +1.1 | -10.0 dB | 675 Hz |

- So the G sharp moves 3 dB to the left, shrinks to a point and darkens by 4-6 dB, then comes back when Horn 1 re-enters. Inferred: in a pp texture with almost nothing else playing, a listener hears the note change place and colour.
- In 312-360 Horn 3 is the loudest horn (-34.2 dB against Horn 1 -42.3 and Horn 2 -44.6) at corr 0.99. That is why the section reads 0.96 (CHANGES "0.961"). In 912-960, where Horn 4 has its own line, the section reads 0.82. Spreading the REAPER pans would not widen a mono source. The image has to come from the routing.

Fix (instrument side; mix.json only, no data change):
1. In `build/mix.json` tracks "Horn 3":
   - delete `"channel_map": 2`, or set it to 0 (Stereo);
   - set `"mic_db": {"Close": -1.4, "Main": -5.2}` (Horn 1's pair);
   - set `"reaper_pan": -0.18` (Horn 1's).

   c21's range test of exactly this mix on Horn 3 measured:
   - the G sharp at 1092: band corr +0.59, so it no longer cancels;
   - stem corr 0.94 / 0.97 in the drone / recall.

   c21 rejected it only against a 0.70-0.88 width target. The current state is 1.00 and fails both the relay and the countermelody.
2. Optional, if the range test still reads over 0.92: add `"stereo_double": {"spread": 0.6}` (Stereo routing makes it available again). On Violas div it took corr 1.00 -> 0.78 for 0.5 dB of mono loss.
3. Re-fit `gain_db` on Horn 3 so its K-weighted stem level matches c28 in the drone (456-504, -55.6 dB) and in 312-360 (-34.2 dB). Keep every Horn 3 role, CC11 lane and the HELD_DOUBLE set (times, lift, solo role) as they are.

Range test before the render: Horn 3 over 312-360, 456-504, 1020-1032 and 1089-1106, with one start before the last keyswitch and the settle time after the rebuild. It passes when:
- the G sharp 4 at 1026 and 1092 has 300-1000 Hz corr +0.4 or more and mono loss under 1.5 dB;
- the stem corr is 0.80-0.95;
- in the relay, Horn 3's L-R is within 1.5 dB of Horn 1's, and its harmonics 3-8 against 1-2 are within 2 dB of Horn 1's;
- the relay sum (1092-1101) has no level step over 1 dB at 1097 and 1101.

If the G sharp cancels again, keep Mono From Left and report it. No other change can fix the relay.

### 2. Trio climax (bars 210-216): the celli's held arrival gain puts their mf accompaniment level with the violins' f tune and thickens the master. c27's objection stands; this is my verdict on the "+5.4 dB for 14 qn" (measured)

Where: qn 624-651, Violoncellos (mf from 624, after the crescendo of 618-624), against Violins I / II (f espress., the tune T) and Clarinet 1 (mf espress.).

What is wrong (measured): per bar, 300 Hz-5 kHz, so that the celli's low register does not inflate their reading:

| bar | Violins I c18 / c28 | celli c18 / c28 | celli minus Violins I, c18 / c28 |
|---|---|---|---|
| 212 | -37.8 / -37.9 | -44.2 / -41.4 | -6.4 / -3.5 |
| 213 | -39.7 / -39.9 | -45.7 / -41.4 | -6.0 / -1.5 |
| 214 | -42.2 / -42.0 | -46.1 / -40.8 | -3.9 / **+1.2** |
| 215 | -42.1 / -42.2 | -47.2 / -42.2 | -5.1 / **0.0** |
| 216 | -39.7 / -39.8 | -47.2 / -41.7 | -7.5 / -1.9 |

- The tune is unchanged. The celli rose 3-5 dB and now equal or pass the melody in 214-215.
- On the master (624-651), 100-250 Hz rose -7.8 -> -6.8 dB and 2-6 kHz fell -9.9 -> -11.0 dB. This is the only passage in the movement whose low-mid share moved by more than 0.6 dB since c18. Inferred: the f climax is thicker and duller, which is Dan's "mushy".
- The source is the c28 hold rules. parts.json `vol_db` on the celli stays at +0.4 dB from 623.8 to 647, where c18 fell to -1.3 by 627.5. The CC11 holds at 75-79 where c18 dipped to 73. B's figure is a net +2.6 dB held for 14 qn.
- The violas also rose 5 dB at 300-5 kHz, because their [624, 672, -3.7] role is gone. They still sit 5-6 dB under the tune, so the inner line now reads without covering it. Keep that.

Fix (instrument side, one arrival):
- `build/score_config.py`, after the c28 block: `HP_GAIN_TO_CC11 = {**HP_GAIN_TO_CC11, "Violoncellos": {**HP_GAIN_TO_CC11.get("Violoncellos", HP_GAIN_TO_CC11["string"]), "drop_always": sorted(set(HP_GAIN_TO_CC11.get("Violoncellos", HP_GAIN_TO_CC11["string"]).get("drop_always", [])) | {624.0})}}`.
- `build/mix.json` tracks "Violoncellos": a track `cresc_trim_hold` that copies the global one with `skip` plus `[618.0, 625.0]`, so the held trim releases as well. Then run `--midi-only`.

Pass on the render:
- celli 300-5 kHz at least 3 dB under Violins I in each of bars 212-216;
- master 624-651: 100-250 Hz share -7.5 dB or lower, 2-6 kHz -10.5 or higher;
- no sag over 1.5 dB into bar 215 on the master (B's measure: c28 2.6 dB, c27 4.3). If the sag returns, it comes from the violins' own 632-640 hairpins and needs a separate fix.

### 3. The coda's "soft sticks" (bars 341-376) still sound with hard sticks, 9 dB brighter in the attack than the felt patch. A passage EQ on the Timpani track can supply the printed stick change, which the single instance cannot switch (measured; EQ result simulated)

Where: Timpani, the 13 strokes of 1086-1110 (bars 363-371, including the ppp "near the rim" strokes of bar 371). The score prints "soft sticks" at bar 341. The timpani are silent from the G.P. to 1086.

What is wrong (measured): in the first 50 ms of each stroke, against the c18 felt strokes at the same notes:
- 1-5 kHz share: median -18.9 dB against felt -27.6.
- Level-matched spectrum, hard minus felt: 1 kHz +8.8, 1.5 kHz +14.4, 2.5 kHz +19.4, 4 kHz +14.9, 6 kHz +6.7 dB.
- These are the most exposed strokes of the movement, ppp under the held G sharp. CHANGES.md "Faults" says nothing can change them on the instrument side, because a second instance breaks the memory cap.
- Inferred: a clear stick click where the composer asked for a soft, distant thud.

Fix: a level-independent tone change with no volume move. The mechanism exists (`loud_eq`, wet-automated ReaEQ, build_reaper `mute_lua`).
- `build/mix.json` tracks "Timpani", add: `"loud_eq": {"points": [[1060, 0], [1061, 1], [1128, 1]], "bands": [{"band": "highshelf", "hz": 1000, "db": -10}, {"band": "bell", "hz": 2500, "db": -8, "bw_oct": 1.2}], "_c29": "critic C #3: printed soft sticks from bar 341; one instance cannot switch to Timpani Flt KS"}`.
- The switch at 1060 falls in the timpani's 69 qn rest, so no sounding note or hall tail crosses it.
- Track FX run before the post-fader sends, so R Perc gets the softened stroke too, and the hall's colour matches.

Simulated on the c28 stem (an FFT-domain approximation of those two bands):
- 1-5 kHz share -18.9 -> -28.6 dB (felt -27.6);
- stroke level -0.06 dB.

Pass on the render:
- 1-5 kHz share of the first 50 ms at -30..-25 dB on the 1086-1110 strokes;
- stroke peaks within 0.5 dB of c28;
- the Allegro strokes unchanged.

### 4. The oboes and cor anglais are still dry mono points among a wide string stage. c25's Main-mic test (C #2) is still pending (measured; benefit inferred)

Where:
- the counterstatement, bars 29-44 (calls 84-90 and 96-102, string answers 90.4-96 and 102.4-108);
- Oboe 1's trio middle part, 185-196 (552-588);
- the cor anglais' pp arpeggio, 95-100.

What is wrong (measured on c28, the same as c24):

| stem or span | level | corr | side/mid |
|---|---|---|---|
| Oboe 1 stem, 552-588 | | 0.99 | -17.1 dB |
| Oboe 1 stem, 84-132 | | 0.99 | -18.1 dB |
| cor anglais, 282-300 | | 0.94 | -11.3 dB |
| Violins I / violas beside Oboe 1, 552-588 | | 0.43 / 0.40 | |
| master, winds' calls | -44.2 / -42.5 dB | 0.85 / 0.88 | |
| master, strings' answers | -44.1 / -43.4 dB | 0.39 / 0.39 | |

- At equal level, the stage narrows each time the winds call.
- The R Winds wet/dry is unchanged (-12.2 dB), and Dan's limit rules out more send.
- The only room the oboes can gain is their own recorded room, the Main mic (p.138). The CHANGES.md research table lists "oboe Main lower than -9 dB" as pending, not run.

Fix: c25 C #2 as written, still valid.
1. Range-render Oboe 1, Oboe 2 and the cor anglais over qn 81-110 and 549-590, once Close-only and once Main-only.
2. Mix offline at Main -9 and -6 dB under Close.
3. Adopt the lowest Main level that meets all of these:
   - Oboe 1 stem corr 0.92 or less in 552-588;
   - 250-500 Hz share up by less than 1.5 dB;
   - note-end drop at +0.15 s between -18 and -24 dB;
   - master corr in the winds' calls 0.80 or less.
4. Set `build/mix.json` `mic_db` Main on Oboe 1 / Oboe 2 together (expected -9 or -6) and on the cor anglais (expected -9). Re-fit `gain_db` to c28's K-weighted level.

Leave the flutes (corr 0.89), the clarinets (0.76) and the R Winds send alone. Pass: G.P. drop on the mp3 not under 13 dB on my measure (c28: 13.0).

## Do not touch

- The returns, their faders, filters, pans and IR envelopes, and every send. Wet/dry -12.7 dB has been stable since c18, and the mp3's G.P. drop sits at the edge of Dan's limit.
- The delivery chain with its bed and ride rows.
- The timpani's template mics and Hrd KS for bars 1-340.
- The trumpets', trombones' and Horns 1 / 2 / 4's mics and seats.
- The Violas div Stereo Double 0.6, the Violin I solo's mic, EQ and Stereo Double, and Flute 1 "col Vl. solo" at -6.6 dB under the solo.
- The borrowed harmonic and the harp harmonics, the Violins II con sordino lane, the violas' level in the trio climax (role removed: the inner line reads 5-6 dB under the tune), and the low end of every tutti.
- HELD_DOUBLE's times, lift and solo role (finding 1 changes only Horn 3's routing and mic mix).

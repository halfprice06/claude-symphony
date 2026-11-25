# Cycle 04, critic B (balance and levels), on the c03 render

Material: `cycles/c03/render/` (stems after c03's stem fix, and the master) and `cycles/c03/metrics/`; `build/parts.json`, `build/mix.json`, `build/roles.json`, `build/score_config.py`, `build/mockup-events.tsv`; the score comments in `symphony/scherzo/v600/sections/*.ily`; the Dvořák 9/i reference for band shares.

Method. Unless a line says otherwise, levels are dB of power through an approximate K-weighting: a 4th-order high-pass at 38 Hz and a +4 dB shelf above 1.5 kHz. They are computed from 2048-point spectra every 10 ms, with both channels summed, and averaged over qn windows on the parts.json tempo map (qn 0 = 0 s of the rendered files). They are the same kind of numbers as c03 B's report, but not the plain RMS that metrics.md prints. "X over Y" means X's level minus Y's in the same window. Judgements are marked **measured** (numbers from the stems), **read** (data, code, score or manual) or **inferred**.

## Manual notes (cycle 4, slot B: group B4, PDF pages 49-52, 202-204, 208, read in full; MANUAL-GAPS.md read)

| page | what it says | where it applies here | does the render follow it? |
|---|---|---|---|
| 49 (2.5.2-2.5.3) | Output configurations (stereo up to 16 stereo pairs); "Load with Effects off" lets you replace the reverb in each instrument with one reverb in the DAW | All 31 tracks: one stereo output per Opus instance; the hall is Opus's own convolution reverb, with the same IR, wet and IR envelope written into every instance (`reverb` in mix.json) | **Yes, by design (read).** Effects are kept on, but every instance gets an identical hall, so the result is one room without a DAW reverb bus. |
| 50-51 (2.5.5) | Multi-outputs: route each mic to its own output and send each mic to the reverb bus at its own level | The mockup does the same thing inside Opus: per-mic volume and a pre-fader send per mic (`groups.*.mics`, `send`) | **Yes (read).** Per-mic balance is the lever for how far back a section sits. The harp patch is a Maestro patch, which loads only the Close mic (DIGEST §10, patch; manual p.68 lists the harp's mic set). The harp therefore has no Main mic to move it back, only velocity and level (finding 2). |
| 52 (2.5.6) | Multi-timbral instances, up to 16 instruments per instance | Not used: one instrument per instance, 31 instances | Not applicable. Memory is governed by rows, not instances (c02 LEARNINGS). |
| 202-203 | Level Amp, Limiter, Limiting Amp inserts | No Opus dynamics insert on any track; the only limiting is `deliver_master.py` on the mp3 (c03: 2.5 dB) | **Yes (read).** Balance is done with level and CC11, as Dan's rule 6 asks, not with compression. |
| 204 | SSL Bus Compressor, SSL Channel Strip | The patches' SSL strips ship inactive (DIGEST §4.2) and stay inactive | **Yes.** A bus compressor would flatten the printed dynamics. |
| 208 | SSL Transient Shaper; "Invert" subtracts the added attack and leaves more body | Not used | Not used. This is an option for lens A (the Marc LITE heads' 2-5 kHz front) rather than a balance tool. |

The question B4 asks, "a mic or row change instead of envelope trims":
- **Harp (finding 2).** No other mic is available, so the fix is velocity: the Harp Sus RR layers follow velocity (manual p.69; layer splits measured in Movement I c33: Pluck p 1-57 / mp 58-85, Thumb p 1-42 / mp 43-70 / mf 71-97). A lower velocity cap gives a p timbre as well as a lower level.
- **Bassoons (finding 1).** The woodwind group already plays further back than the factory mix (Close 0.5 / Main 0.8, against the factory Close 1.0 / Main 0.01-0.28, DIGEST §4.1). The excess is level, not distance, so a gain and role change is the right tool.
- **Celli in the tuttis (finding 3).** The cause is an EQ boost, so it is fixed in the EQ.

## Standing checks (Dan's ears), measured on c03

- **Loop pulsing (item 8): none found.** Autocorrelation at 3.95 s of the detrended level, the 100-300 Hz band and the spectral centroid:

  | span | level | band | centroid |
  |---|---|---|---|
  | Violins I 0-23 | +0.05 | -0.20 | +0.02 |
  | Violins I 1089-1128 | -0.02 | -0.22 | 0.00 |
  | Horn 1 1110-1128 | -0.32 | -0.29 | -0.12 |
  | celli 1070-1091 | -0.55 | -0.49 | -0.46 |
  | celli 605-624 | -0.04 | -0.06 | +0.20 |
  | Horn 4 drone 456-504 | -0.05 | +0.10 | -0.04 |
  | master 1089-1128 | -0.21 | +0.19 | -0.23 |

  The Violins I harmonic E6 at 420-445 reads band +0.44. That band (100-300 Hz) holds the bassoon and bass clarinet pad, not the violins: level and centroid are +0.05 and -0.06.
- **S3 at the sub. p's (measured).** Master in 50 ms frames from 0.2 s before the bar line, no step to silence at either:
  - qn 360: -30.4, -29.9, -33.0, -33.8, -33.2, -31.2, -29.5, -28.3.
  - qn 828: -31.8, -36.4, -38.0, -38.9, -37.0, -34.1, -34.0, -32.1.
- **Low end against the reference (measured).** Band shares in the master's loudest 10% of frames are within 1-2 dB of Dvořák 9/i in every band. The exceptions are two windows (finding 3):
  - The coda build (qn 984-1005): 20-100 Hz is -18.8 dB against -24.8 dB.
  - Bars 101-104: 100-250 Hz is -4.4 dB against -6.3 dB.

  The master has no general 200-500 Hz build-up (250-500 Hz: -7.5 against -6.7 dB).

## Findings, ranked by what a listener would hear

### 1. The bassoons and the bass clarinet sit over the lines they accompany or double, at every dynamic (bars 69-71, 141-148, 193-200, 209-224, 345-348, 81-88; also 297-299)

**Measured (K-weighted, 3 qn windows unless noted).**

- **Bars 69-71 (qn 204-213; 297-299 is the same music).** The score wants the woodwind A pedal to grow in under the strings' f stretto ("p< (were f) ... grows in under the strings f", sB.ily c508). Bassoon 2's p< A2 reads -30.6 / -30.2 at qn 207 / 208.5 (1.5 qn windows). Against it:
  - Violins I's f subject: -30.0 / -31.3.
  - Violins II: -37.6.
  - celli: -33.1.

  The p pedal is level with the f tune and 7 dB over Violins II.
- **Bars 141-148 (link).** Bassoon 2's pp B3/C sharp 4, part of the pad under Hn 1's line (link.ily header), reads -42.7, -43.2, -43.3, -40.2 at bars 143-146. Hn 1 reads -43.1, -46.8, -43.7, -41.4. The pad is level with the line or over it, even with Hn 1's +3 role.
- **Bars 193-196 (qn 576-588).** Bassoon 1 holds an inner A3/G sharp 3 under Violins I's p< call (tB.ily: the oboe's call in the violins).

  | qn | 576 | 579 | 582 | 585 |
  |---|---|---|---|---|
  | Bassoon 1 | -39.3 | -35.6 | -36.0 | -30.4 |
  | Violins I | -42.1 | -38.6 | -37.2 | -34.8 |

  Bassoon 1 is the loudest stem in bars 194-196.
- **Bars 197-200 (qn 588-600).** Bassoon 1's f held E3 / G sharp 3 / F sharp 3 (harmony) reads -31.6, -36.8, -31.5, -32.6. The trio tune T reads:
  - violas: -33.1, -36.4, -34.5, -32.0.
  - Violins II: -35.2, -38.5, -37.6, -36.8.
  - Clarinet 1: -36.4, -39.2, -35.4, -35.8.

  The bassoon is the loudest stem in bars 197 and 199, 2-5 dB over T.
- **Bars 209-224 (qn 624-672).** Bassoon 2 doubles the celli's countermelody in unison. The score asks for "a degree under the cellos' f" and quotes Rimsky-Korsakov: "the strings predominate" (tC.ily c087).

  | qn | 630 | 633 | 636 | 639 | 645 |
  |---|---|---|---|---|---|
  | Bassoon 2 | -30.0 | -33.9 | -36.2 | -34.8 | -31.5 |
  | celli | -39.0 | -37.9 | -38.0 | -37.6 | -35.6 |

  - Bassoon 2 is 2-9 dB over the section it doubles.
  - The bass clarinet's mp bass is also over the celli: -36.5 / -35.6 at 630 / 636.
  - Bassoon 1's inner part (the soft horn-bassoon choir, c014) reads -25.7 / -27.0 at qn 654 / 657, over Violins I's tune (-26.5 / -31.6). It is the loudest stem in bars 219-220.
- **Bars 345-348 (qn 1032-1044).** Oboe 1 has T on top, Clarinet 1 and Bassoon 1 are under it, all p dolce. Bassoon 1 reads -35.6 / -35.0 at 1033.5 / 1035 (1.5 qn windows), against Oboe 1's -39.4 / -38.5: the bass line is 3-4 dB over the tune.
- **Bars 81-88 (qn 240-264).** Clarinet 1 has the dolce tune (sB.ily header: "Cl 1 dolce 81-88"); the pp bass clarinet bass reads:

  | qn | 249 | 255 | 258 | 261 |
  |---|---|---|---|---|
  | bass clarinet (pp) | -38.6 | -40.2 | -39.9 | -39.5 |
  | Clarinet 1 (p) | -41.8 | -40.8 | -44.4 | -44.9 |

- **The trio, bars 169-184.** Bassoon 2's pp pad reads -42..-46 against Violins II's pp con sord. arpeggios at -51 (finding 5).

**Cause (read).**
- Both bassoons have the largest soft trims in the mix: Bassoon 1 pp 8 / p 7 / mf 3.6, Bassoon 2 pp 9 / p 8 / mf 4.3. That is against flute and oboe p 5, Violins I p 3, Violins II p 0, violas and celli p 5.
- The hairpins add +4..+7 dB in `vol_db` on top of the CC11 rise (Bassoon 2 204-213: vol 0 -> +7.0).
- The trims made each track's p equally loud. A single bassoon is weaker than a string section at the same marking, so equal levels put it on top wherever it doubles or accompanies.

**Judgement (inferred).** Through the trio's build, its forte return and the link, a listener hears a bassoon in the middle of the texture instead of the tune. This is the most widespread balance error left in the render.

**Fix.**
- `build/mix.json`: `tracks."Bassoon 1".gain_db` -2 -> -5 and `tracks."Bassoon 2".gain_db` -2 -> -5.
- `build/roles.json` (score qn):
  - "Bassoon 1": `[576, 600, -3]` and `[624, 672, -3]` (inner parts under the tune); `[1032, 1044, -3]` (under Oboe 1's T); `[696, 711, 2]` (the codetta tune, bars 233-236). After the -3 gain its margin over the harp would be 3.2 dB (-42.6 against -45.8); this role keeps it about 5 dB.
  - "Bassoon 2": `[624, 672, -4]` (the unison doubling of the celli).
  - "Bass clarinet": `[240, 264, -5]` and `[624, 672, -4]`.
  - "Violoncellos": change c03's `[624, 672, -3]` to `[624, 672, -1]`. c03 measured the celli 6.2 dB under Violins I there and proposed about -1. With Bassoon 2 down by 7 dB, the countermelody needs the celli to carry it.

**Target, simulated by subtracting the changes from the c03 stems.**

| passage | after the change |
|---|---|
| 207-210 | Bassoon 2 at -33.2..-33.6, 2-3.6 dB under Violins I's f |
| 193-200 | Bassoon 1 2-4 dB under T and under Violins I's call |
| 630-645 | Bassoon 2 2-7 dB under the celli (celli at -33..-37) |
| 654-660 | Bassoon 1 at -31.7 / -33.0, under Violins I |
| 1033-1035 | Bassoon 1 about 3 dB under Oboe 1 |
| 249-261 | bass clarinet 1-3 dB under Clarinet 1 |

**Check after rendering:**
- the tenor countermelody of 105-120 and 305-320 (Bassoon 1 shares it with Horns 3-4 and celli, -35.5 against -30.3 / -26.0 now);
- the counterstatement's wind answers at bars 37-40.

### 2. The harp's p espress. melody in the F major episode is the loudest soft passage in the movement (bars 73-88, qn 216-264)

**Measured.**
- The harp's p espress. tune at 216-240 averages -30.3 dB K (50 ms peak -25.8), and the master -28.9. The other soft melodies, by comparison:

  | melody | level |
  |---|---|
  | Violins I's mp leggiero theme A (36-84) | -35.4 |
  | Clarinet 1's p dolce trio tune (456-504) | -36.9 |
  | the Violin I solo, pp-p dolce (1044-1068) | -36.7 |
  | Horn 3's p dolce T (1020-1032) | -37.7 |
  | Oboe 1's p espress. (552-564) | -42.2 |

  The harp's p is 5-12 dB louder than every other soft tune.
- The master at 216-240 is only 6.4 dB under the f stretto before it (204-213: -22.5) and 5.5 dB over the mp theme.
- Plain RMS (metrics.md) shows the same thing: the harp's median p bar is -34.8 dB, the loudest p of any track (Violins I -42.5, Flute 1 -46.3).
- In bars 81-88 the harp's pp chords are over Clarinet 1's p dolce tune: harp -36.5 against Clarinet 1 -40.2 at qn 240, and -37.9 against -35.9 at qn 252.

**Read.**
- c02's `VEL_CAP_SPANS` caps the harp at v78 over qn 216-240; the notes play v59-78.
- On Harp Sus RR that is the mp pluck layer (58-85) and the mp-mf thumb layers (43-97) (manual p.69; layer splits from Movement I c33, DIGEST §10).
- `mix.json` gives the harp `soft_trim_db` p +5.
- The patch loads only the Close mic (Maestro patch, DIGEST §10). It is all direct sound and sits in front of the woodwinds (Close 0.5 / Main 0.8).

**Judgement (inferred).** The F major episode sounds like a loud harp solo. The score's soft, strings-tacet colour change after the ff A major chord (bar 72) loses half its contrast.

**Fix.**
- `build/score_config.py`: `VEL_CAP_SPANS["Harp"]` = `[(216.0, 240.0, 56), (240.0, 264.0, 50)]`, the p pluck layer and the pp chords. This changes timbre as well as level.
- `build/roles.json` "Harp": add `[216, 240, -3]` and `[240, 264, -4]`.
- If only one change is possible, the role alone at -6 / -4.

**Target.**
- The harp tune at about -36..-37, level with Clarinet 1's and the solo violin's soft tunes.
- Still 4-8 dB over the pp horns and Bassoon 1 at 216-240 (now -40..-45; Bassoon 1 a further 3 dB lower after finding 1).
- The harp chords at least 3 dB under Clarinet 1 in 240-264.
- The master in bars 73-80 at least 10 dB under the stretto.

### 3. In the tuttis the celli are the loudest stem and carry the bass octave instead of the basses (bars 101-104, 301-304, coda build 329-339, summit 1005-1012)

**Measured.**
- **The celli over Violins I:**
  - qn 300-312 (101-104): celli -22.6 against Violins I -24.3. c03 B measured +4.4 dB at bar 101 and +2.7 at 103, and the celli are still on top.
  - At the summit, 1 qn windows:

    | qn | 1005 | 1010 |
    |---|---|---|
    | celli | -16.9 | -14.3 |
    | Violins I's fff B6 / F sharp 6 | -19.0 | -19.4 |
    | Flute 1 | -15.8 | |

    At 1005 Flute 1, doubling the tune at the octave above, is the loudest stem.
- **The celli over the basses:**
  - At 900-960, celli -25.1 against basses -31.7; at 972-1017, -24.0 against -28.3.
  - In the coda build (984-1005) the celli carry the master's 20-100 Hz band (-0.6 dB from the master's energy in that band); the double basses are 10.8 dB lower.
  - At 300-312 the celli carry the 100-250 Hz band (-1.3 dB from the master).
  - These are the two windows where the master's band shares exceed the reference (Standing checks: 20-100 Hz +6 dB, 100-250 Hz +1.9 dB).
- **Simulated.** Removing 4 dB of a 1-octave bell at 150 Hz from the celli stem lowers its K-weighted level by:

  | window | change |
  |---|---|
  | 300-312 | -3.2 dB |
  | 984-1005 | -3.0 dB |
  | 1005-1012 | -3.4 dB |
  | 312-360 | -2.2 dB |

  Most of the celli's tutti level sits in this band.

**Read.** `mix.json` "Violoncellos" has three boosts in this region:
- a permanent bell +3 dB at 170 Hz (1.5 oct);
- a permanent bell +3 dB at 125 Hz (1 oct);
- `loud_eq` +6 dB at 150 Hz over 298-360, 898-960 and 984-1017.

Together that is up to +12 dB around 150 Hz in every tutti. The basses' `loud_eq` (+6 at 160 Hz, -4 at 98 Hz) adds tone, not bottom octave.

**Judgement (inferred).** The tuttis sound low-mid heavy, with the tune second. The coda's falling bass line (score coda.ily: "the bass falls") is heard an octave too high, in the celli's motive, rather than in the basses.

**Fix.** `build/mix.json` "Violoncellos" `loud_eq.bands[0].db` 6 -> 2 (keep the points).

**Target.**
- The celli 1-2 dB under Violins I at 1005 (simulated -20.3 against -19.0) and at 101-104 (simulated level with Violins I).
- At 1010 still about 1.7 dB over; if needed, add the c03 B optional roles "Violoncellos" `[300, 312, -2]` and `[900, 912, -2]`.

**Side effects.**
- The master loses about 0.5 dB at the summit (inferred: the celli are about 20% of the K-weighted power at 1005). The same cut applies at 1004 and at 304, so the summit-to-304 relation stays about where it is (1.0 dB over in c03).
- The coda build's 20-100 Hz share falls toward the reference.
- Leave the basses' EQ alone. Their B1, the most frequent bass note (85 notes), keeps a fundamental share of -9.6 dB of the note's energy in the first 0.25 s, against -16.9 for A1 and -23.6 for E1 (measured): B1 is not thin despite the 61.7 Hz `mute_eq` cut.

### 4. The last timpani strokes (qn 1008-1014) are the loudest stem in bar 339 and fill the G.P. (bar 340, qn 1017-1020)

**Measured.**
- Bar 339: the timpani is the loudest stem, -22.2 dB against Violins II -25.0 and Violins I -25.5. At the 1014 stroke: timpani -18.3 against Violins I -20.2 / Violins II -23.8 / celli -24.6.
- 100 ms windows from qn 1014:

  | | 0.0 s | 0.6 s | 1.0 s |
  |---|---|---|---|
  | timpani | -18.3 | -35.2 | -40.0 |
  | Violins I | -20.2 | -47.7 | -63.5 |
  | master | -13.9 | -32.4 | -39.7 |

  From 0.6 s the master is the drum alone, 12-23 dB over the strings' hall. c03's "Timpani Flt Sht" row on the 1014 stroke did not change this. The Lng strokes at 1008, 1010 and 1012 (2 qn notes, v121) still ring, and the Sht stroke itself decays about 17 dB in 0.6 s.

**Read.**
- `vol_db` gives each of the four strokes +6.0 dB at the onset, then +3.0 at +0.5 qn: [1008.5, 3.0], [1010.048, 6.0], [1012.048, 6.0], [1014.048, 6.0].
- The score marks the drum ff against the strings' and woodwinds' fff (events: Timp 1005 ff).
- CC7 on the drum is 127 from 1007.98.

**Judgement (inferred).** The final chord ends on a drum hit louder than the orchestra, and the hall after the fff is a timpani ring. The rule "a roll/stroke is never the loudest stem unless the timpani lead" is broken at the movement's climax. This is the c03 open item seen through balance.

**Fix.**
- `build/roles.json` "Timpani": add `[1007.9, 1020, -5]`. This is one level from before the 1008 stroke through the G.P.; it lowers the drum and its hall together, with no fall under a sounding note, so S3 holds.
- In `build/score_config.py`, as c03's actor planned, a pre-hall CC7 fall on the timpani from qn 1014.6 to 1016.0 (127 -> 40) through the existing CC7 lane, so the drum is damped before the hall.

**Target.**
- The 1014 stroke 2-3 dB under Violins I.
- From qn 1016 the timpani at least 6 dB under the strings' hall (c03 B's target).

### 5. Violins II are too low where they carry the line or the texture (fugato entry bars 65-66; trio con sord. arpeggios bars 168-196)

**Measured.**
- **Fugato, bars 65-66 (qn 192-198).** Violins II have the p subject entry, over the violas' pp countersubject and the celli's pp espress. line (sB.ily: "Vln II in A minor over the violas' countersubject (65)").
  - Over 192-198: Violins II -45.3, violas -44.9, celli -42.5.
  - At qn 195: Violins II -47.7 against violas -44.4 and celli -42.6.
  - The subject is 3-5 dB under the two pp lines. The violas' subject at 61 was over the celli by 0 to +3.9 dB (qn 180-186).
- **Trio, qn 504-552.** Violins II's pp "con sord., dolce" quaver arpeggios average -51.3:
  - 14.5 dB under the celli's mp tune (-36.8);
  - 6-9 dB under the other pp accompaniment: Bassoon 2 -42..-46, Horn 3's p doubling -40..-42, basses -45..-51.

  They are the quietest stem in the texture, though they are its only motion.

**Read.** `mix.json` "Violins II" `soft_trim_db` pp 3 / p 0 / mf -0.8, the lowest string trims (Violins I 4 / 3 / 1, violas 6 / 5, celli 6 / 5). The con sord. CC15 lowers the samples further.

**Fix.** `build/roles.json` "Violins II": add `[192, 198, 4]` and `[501.5, 588, 4]`. The second span is from the "con sord." at 501.5 to the "senza sord." at 588.

**Target.**
- The subject 1-3 dB over the countersubjects at 192-198.
- The arpeggios about 10 dB under the celli's tune and level with the pp pad, which falls 3 dB in finding 1.

### 6. Single woodwinds that the score marks a level under the violins they double sit level with them or over them (bars 45-50, qn 132-150; bars 125-127, qn 372-381)

**Measured.**
- **Bars 45-50.** Violins I and II f espress.; Flute 1, Oboe 1 and cor anglais mf espress.

  | qn | 132 | 135 | 138 | 147 |
  |---|---|---|---|---|
  | Flute 1 | -30.4 | -30.5 | -32.6 | -25.9 |
  | cor anglais | | | | -27.5 |
  | Violins I | -30.4 | -30.0 | -32.7 | -31.2 |

  Flute 1 is level with Violins I at 132-138 and the flute and cor anglais are over it at 147.
- **Bars 125-127.** The score: "Fl 1 and Ob 1 join the violins' second idea pp<, a level under the strings they double" (sC.ily c167).

  | qn | 375 | 378 |
  |---|---|---|
  | Flute 1 | -30.6 | -29.1 |
  | Oboe 1 | -37.4 | -30.9 |
  | Violins I | -36.4 | -33.7 |

  Flute 1 is 4.6-5.8 dB over the violins it doubles.

**Read.** The winds' soft and mf trims (flute p 5 / mf 2.5, oboe p 5 / mf 3.1, cor anglais p 5 / mf 2.5) are 2-5 dB over the violins' trims. This is the same mechanism as finding 1.

**Fix.** `build/roles.json`:
- "Flute 1": `[132, 150, -3]`, `[372, 384, -5]`.
- "Oboe 1": `[372, 384, -3]`.
- "Cor anglais": `[144, 150, -3]`.

**Target.** The doubling winds 2-4 dB under Violins I. Their colour stays on the line, as the score's "a level under" asks.

## Other observations (not ranked)

- **Trumpets in the tutti theme (312-360).** Trumpet 1 averages -33.4, Trumpet 2 about 3 dB lower, against Violins I's -23.6: f trumpets 10 dB under ff violins. They are present, not on top, which is the lens's aim. If Dan hears them as missing, Trumpet 2 `dyn_trim_db.f` +2 is the first step.
- **At the summit some second woodwinds read over the firsts:** Oboe 2 -25.8 against Oboe 1 -32.2, Clarinet 2 -21.6 against Clarinet 1 -25.3 at 1005. Oboe 1 has c02's -3 role there and holds a long B5. Inner detail at fff; leave it unless lens A finds the top line missing.
- **The sub. p at 121 (master -29.7..-30.5 at 360-369) is louder than the mp theme of bars 13-28 (-34.4).** More players are involved, so this is acceptable, but no further rise should be added there.

## Do not touch

- Clarinet 1's trio tune over the harp and horn drone (153-168: Clarinet 1 -36.9 against harp -43.3).
- The celli's trio tune over Horn 3 (504-552), and Violins I over the celli at 528-552.
- The Violin I solo over Flute 1 at 349-356; Hn 1's motto tail at 357-360 and its last G sharp with the Violins I at 372-376.
- Theme A's Violins I over the pizz. bass (13-28).
- The roll levels at 300-309, 384, 612-624 (c03's -3 role), 708, 852, 906 and 993.
- The sub. p transitions at 360 and 828 (no step to silence).
- No loop pulsing on any held note.
- c03's celli roles at 362-396, 576-612 and 828-864 (finding 1 changes only 624-672).
- The Marc LITE heads with their level steps; the horn soft trims.
- The hall settings (fx_volume 0.095, low cut 160, ir_setup); the basses' EQ (finding 3).

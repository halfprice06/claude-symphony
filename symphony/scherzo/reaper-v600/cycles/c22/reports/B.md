# Cycle 22, critic B (balance and levels), on the c21 render

Measured on `cycles/c21/render` (stems and master), `cycles/c21/scherzo-mockup-c21.mp3` and the data in `cycles/c21/build_render/`. Stems are compared with `cycles/c18/render`, the mp3 with `cycles/c20/scherzo-mockup-c20.mp3`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

Terms:
- "L" is the A-weighted power of a stem over a window (1/6-octave bands, 21 ms frames, mean of the two channels), in dB on an arbitrary common scale. "RMS" is the plain power of a stem over a window in dBFS.
- "Best band" is the c20/c21 measure: over 1/6-octave bands 40 Hz-16 kHz, the line's power against every other stem plus the four returns, averaged over the frames in which the line's notes sound; only bands within 10 dB of the line's strongest band. Above 0 the line leads in its own register; under -6 it is masked.
- "Peak" is a note's highest 10 ms power within 0.12 s of its moved note-on.
- "M" is ffmpeg ebur128 momentary loudness on the mp3; a bar's value is its median M.

Each judgement is marked (m) measured or (i) inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for c22. I read PDF pages 101 (D2), 108-110 (A4, the woodwind sustain and short sections) and 150-151 (B1) of the May 2021 HO manual, because findings 1, 3 and 4 turn on volume against expression and on the accent row's velocity, and used `loop/MANUAL-GAPS.md`.

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Sustain Accent: velocity sets the loudness of the attack, the mod wheel the sustained note; "strike the keys harder ... whenever you want a louder accent" (p.101, brass chapter; the woodwind pages 108-110 do not describe the row) | Oboe 1's four p accented halves on "Sus Accent MAX" (qn 87, 99, 111, 123) | Partly. They play at velocity 70 / 70 / 70 / 90 and still sit 1.3-8.8 dB under the staccato before them (finding 4). |
| Woodwind sustains: dynamics on the mod wheel (CC1 in the Clarinet KS Master), all dynamic layers sound at once (p.108-109) | Clarinet 1-2's held chord under the counterstatement tune, bars 37-43 | The layers follow CC1 29 -> 88 as printed (p < f), but the level is set by stacked trims (finding 1). |
| Volume can raise or lower a section without changing its timbre; CC7 sets each track's ceiling, CC11 shapes the line (p.151) | Role rows in `build/roles.json` | Yes in method. Two rows now act on causes that later cycles removed (findings 2 and 3). |
| MANUAL-GAPS #9 (half-section patch for Violins II "la metà", bars 349-356) | Solo against Violins II and Flute 1 | Not needed: the solo leads with best band +4.5 to +9.8 dB; Violins II -7.2..+3.4, Flute 1 -4.9..-19.3 (m). |
| MANUAL-GAPS #10 (horn portato rows for tenutos) | The trio return's horn tenutos, bars 209-224 | Not used. Finding 3 is a level problem, not an articulation one, so it does not need the row. |
| MANUAL-GAPS #13 (Mid mics on woodwinds and horns) | | Tested on Horn 3 in c21 and rejected (correlation 0.97). Not repeated. |

## Answers to the cycle 22 questions (m unless marked)

- **Hidden inner lines (Dan, 2026-11-17).** I scanned every track bar by bar for moving lines (at least 3 onsets and 2 pitches in two bars) whose best band was under -5 dB and that were not doubled (same pitch class, onset and length) by another track. I also measured, by hand, every line the score marks espress., dolce or solo, and every independent counter-line I found on the score pages.
  - Most of the movement passes:
    - theme A's Violins I +9.5..+15 over the pizzicato bass (bars 13-28);
    - the fugato entries +1.9..+25.9 (57-72);
    - the tenor countermelody summed (Bassoon 1, Horns 3-4, celli) -0.8..+5.9 at 105-120 and -3.3..+6.4 at 305-320;
    - the celli's arco espress. counter-line under the reprise theme +2..+10 (253-260), -0.2..-3.6 where Flute 1 and Horn 3 join (261-266);
    - the F major episode's harp, Horn 3 and Clarinet 1 0..+18;
    - the trio's Oboe 1 +11..+14 with the celli's dolce counter-line +3..+10 (185-196);
    - the codetta's Oboe 1, Clarinet 1 and Bassoon 1 -1.3..+18.8, with the violas' unison line +3..+8;
    - Horn 1's link line +10..+19 (141-149), its motto tail +13 and its last G sharp +15..+23;
    - the Meno mosso's Horn 3, woodwinds and violas -0.2..+10.
  - The faults are in four places:
    - the counterstatement climax, where an accompaniment chord covers the tune (finding 1);
    - the coda build, where the inner string voices are cut by a stale role (finding 2);
    - the trio return, where the bass clarinet and Horn 4 lines are masked (finding 3);
    - Oboe 1's accents (finding 4).
  - Lesser, not ranked: Clarinets 1-2's syncopated thirds in the second idea (bars 45-56) read -7..-8.5 dB (L 12-18.5, against 19-28 for Flute 1 and Oboe 1 at the same printed mf). That is an acceptable accompaniment margin under an espress. tune.
- **Coda stretto after +4 dB.** On the mp3, bars 325 / 326 / 327 read -30.1 / -29.7 / -26.3 M (c20 -32.9 / -34.5 / -30.1). Every entry leads its own band by +6..+21 dB. The printed p fugatos read -23.5..-24.3 (bars 57-61) and -24.5..-25.8 (289-292). That puts the pp stretto 4.5-6 dB under the p fugatos, about one dynamic step, which is consistent with the print. Do not lift it further. Bar 324 (-30.6) is the end of the printed diminuendo.
- **Clarinet 1 at beat 640.** Over one-quarter windows Clarinet 1 reads L 19.1 against Violins I 17.1 and Violins II 18.8: +2.0 / +0.3 dB (c20 +3.3 / +2.3). The F sharp 5 trim worked. What remains is Violins I's own dip at its portamento arrival: 17.1 against 20.3 / 19.6 on the beats either side. That belongs to critic A.
- **Per-bar mp3, c21 against c20.** Median +0.2 dB; the p10 bar is -23.5 (was -23.7). Every change over 1.5 dB has a known cause:
  - Over +1.5 dB:
    - bar 148 +4.3 (Horn 1's CC1 cap removed; its p link line is back to +17 best band over a ppp harmonic, as printed);
    - bars 325-327 +3.2 / +3.6 / +3.1 (stretto rows);
    - bars 363-364 +2.2 / +1.9 (Horn 1).
  - Under -1.5 dB:
    - bar 23 -2.9 (Sus MAX pairs);
    - bar 184 -4.8 (Bassoon 2's swell gone);
    - bars 339-340 -3.0 / -4.6 (G.P. ride row; the row starts at 1015.3, after the last chord's quarter, so the chord is untouched).
- **Role rows by cause.** Stale rows:
  - Violins II [985, 995.5, -7] (finding 2);
  - Bass clarinet [624, 672, -4] (finding 3).
  - Missing: Clarinets 1-2 after 108 (finding 1). The c02 counterstatement rows end at qn 108, where the clarinets' crescendo starts.
  - Still inert (c21 critic B): Horn 1 [756, 864, -1.5] and [1020, 1068, -2.5].
  - The scan for fast steps (3 dB or more within 0.2 qn under a sounding note) finds no role edges, only the timpani roll ends (308.9, 623.9, 908.9, 995.9).
- **Sub. p at 121 and 277 (S3).** The master falls from -28..-31 to -34..-36 dB (360) and from -33..-36 to -39..-41 (828) over 0.25 s, with no hole: the hall's ring continues under the new entries.

## Findings, ranked by what a listener would hear

### 1. Counterstatement climax, bars 37-43 (qn 108-129): the clarinets' held chord is the loudest sound, 6-10 dB over the p tune it accompanies (m)

**Print.** Flute 1 and Oboe 1 carry the theme at p, with accented halves at 111 and 123. Violins I and II answer at p, with the crescendo to f at 41 (qn 120). Clarinets 1-2 hold chord tones (B4 / G4 for 3 bars from 108, then A4 / F sharp 4, C5 / A4 ...) p < f.

**Measured.**
- RMS per 3 qn window (c21; c18 within 0.3-2.4 dB, so this is old):

  | window (qn) | 108 | 111 | 114 | 117 | 120 | 123 | 126 |
  |---|---|---|---|---|---|---|---|
  | Clarinet 1 | -45.4 | -35.7 | -35.8 | -39.6 | -32.6 | -34.0 | -32.8 |
  | Clarinet 2 | -51.0 | -39.9 | -37.9 | -41.2 | -34.2 | -33.5 | -33.2 |
  | Flute 1 | -41.0 | -41.9 | -34.9 | -35.4 | -36.2 | -37.6 | -38.6 |
  | Oboe 1 | -42.7 | -46.4 | -43.2 | -42.6 | -35.9 | -40.0 | -40.6 |
  | Violins I | -43.1 | -45.7 | -38.9 | -36.1 | -32.6 | -34.9 | -34.7 |

- In bar 38 (qn 111-114) Clarinet 1's held B4 is 6.2 dB over Flute 1, 10.0 over Violins I and 10.7 over Oboe 1. `metrics.md` lists it as the loudest stem in bars 38 and 43, and level with Violins I in 41.
- Best band of the tune (Flute 1 and Oboe 1 summed): -5.2 / -4.1 / -10.0 / -4.2 dB in bars 37 / 39 / 41 / 43. The clarinet pair reads +6.8..+16.6.
- Mp3 bars 37-43: -16.4 -12.6 -11.6 -13.0 -10.5 -9.8 -11.4 M. So the bar-38 rise is mostly the clarinet chord, two bars before the printed f.

**Cause** (m, data): four boosts stack on this one held note, and no role row covers it:
- Clarinet 1's `region_gain_db` pitch 71 is +4.5 dB. It was fitted for the legato tune, and the whole track plays "Leg Slur Rep" (263 notes), so the held B4 gets it too.
- soft_trim p +5.0;
- gain_db +3.6;
- the hairpin volume ramp to +3.9.

The c02 rows that hold the counterstatement chord under the tune (Clarinet 1 [84, 96, -4], [96, 102, -9], [102, 108, -4]; Clarinet 2 [84, 108, -6]) stop at 108, exactly where this held chord starts.

**Fix** (`build/roles.json`, slow class, phrase-length, by role: an accompanying chord under the tune; CC1 keeps the printed p < f layers):
- Clarinet 1 [108, 129, -6];
- Clarinet 2 [108, 129, -4];
- the 0.5 qn edge ramps fall in the clarinets' breaths at 108 and 129.

Do not touch the pitch-71 trim, which the trio needs.

**Expected** (i):
- Clarinet 1 at qn 111-117 about -41.7 / -41.8: level with Flute 1, 4 dB over Violins I;
- at 120-126 about -38.6 / -40.0 / -38.8: 4-6 dB under Violins I's f;
- the tune's best band about 0 to +2 in bars 37-40;
- Oboe 1's accented B5 at 111 freed from the B4 an octave below it.
- Mp3 bars 38-40 about 1-1.5 dB lower. The crescendo arrival at 41 then grows (it is +1.2 now). Check it in the arrival list.

### 2. Coda build, bars 329-332 (qn 984-996): Violins II and the violas, which harmonize the theme head at the same mf < f as Violins I, sit 6-11 dB under it; the c05 role that caused this lost its reason in c20-c21 (m)

**Print.** From 329 all four string parts play the head together in thirds and sixths, mf, crescendo to f at 332 and ff at 333. Woodwinds hold p chords; timpani mf.

**Measured.**
- RMS per bar, c18 -> c21:

  | bar | 329 | 330 | 331 | 332 |
  |---|---|---|---|---|
  | Violins I | -34.0 -> -32.8 | -35.2 -> -35.1 | -32.5 -> -32.5 | -32.3 -> -32.3 |
  | Violins II | -41.7 -> -43.6 | -40.5 -> -42.6 | -37.4 -> -40.4 | -36.4 -> -39.9 |
  | Violas | -40.6 -> -40.8 | -39.9 -> -41.1 | -38.3 -> -41.6 | -32.1 -> -34.1 |

  Violins II fell 1.9-3.5 dB and the violas 0.2-3.3. Violins I's lead over Violins II grew from 4.1-7.7 to 7.5-10.8 dB.
- A-weighted: Violins I L 23-25, Violins II 16-19, violas 14-21. Best band: Violins II -5.6..-9.7, violas -1.0..-12.2.
- In the ff tutti of 105-120, where the same parts play the same head, Violins II read 1-5 dB under Violins I (L 22-28 against 27-32).
- Per note: Violins II's slurred eighth pairs peak 11-15 dB under Violins I's (985: -46.8 against -34.3; 991: -47.7 against -29.3).

**Cause** (m: roles.json `_doc` and the c20/c21 CHANGES):
- Violins II [985, 995.5, -7] was set in c05 "for the untrimmed Spiccato RRx9 row" (its releases ran 1718 ms).
- c20 capped Violins II "Stac RRx9" at 150 ms, and c21 capped "Spiccato RRx9" at 150 ms (`sus_release_cap_ms`, any_dyn). Those caps took the ring out, which is the 2-3.5 dB drop measured above.
- The -7 dB now cuts the notes themselves. With Violins I's +2 (987-995.5), the role gap is 9 dB between two sections at the same printed dynamic.
- The violas' c21 caps cost them up to 3.3 dB against their +3 role.

**Fix** (`build/roles.json`, slow rows, no new edges):
- Violins II [985, 995.5, -7] -> -3;
- Violas [984, 995.5, +3] -> +5.

Leave the 996+ rows (Violins II -5 / -2, violas +1 / +1.5) alone: the summit leads bar 318 by only 0.4 LU on the mp3, and bars 333-335 must not rise.

**Expected** (i):
- Violins II 3.5-6.8 dB under Violins I in 329-332 (the c18 gap, and close to the tutti's 1-5);
- violas 4-7 dB under;
- mp3 bars 329-332 (-12.9 / -13.4 / -12.3 / -10.5 M) about +0.3-0.6;
- the arrival at 329 is unchanged.
- Check: summit lead over bar 318 at least 0.4 LU, and the arrival at 336 not smaller.

### 3. Trio return, bars 209-224 (qn 624-672): the bass clarinet's mp line and Horn 4's mp-mf bass-clef line are masked, 8-15 dB under the tune and under every other sound in their band (m)

**Print.**
- The tune is in Violins I and II and Clarinet 1, f / ff.
- Celli, Bassoons 1-2 and basses play mf.
- Horns 1-2 play tenuto chords, mp.
- The bass clarinet has its own mp line in dotted halves (630-666; mf at 654).
- Horn 4 has a bass-clef counter-line at 217-224 (648 mp, 654 mf, 660 mp: E-G sharp-E-A-F sharp-B-C sharp-A-B).

**Measured** (L per 6 qn, 624-672):
- bass clarinet -15.6 / 9.2 / 10.0 / 7.6 / 12.2 / 7.5 / -11.2 / -3.0;
- Horn 4 at 648-666: 9.3 / 13.0 / 5.2;
- against Violins I 19.0-24.7, Bassoon 2 7.1-16.5, celli 5.3-18.6.

Best band:
- bass clarinet -0.9 / -2.3 / -5.1 / -5.0 / -9.8 / -5.1 in bars 211-224;
- Horn 4 -11.2 / -7.2 / -10.1 / -10.1 in 217-224;
- Horn 2's tenutos -3.1..-16.9 (they double Horn 1's chords, so less matters there).

**Cause** (m, roles.json `_doc`):
- Bass clarinet [624, 672, -4] is from c04 ("bassoons / bass clarinet over the lines they accompany"). Since then the bassoons' role in this span and their -5 gain were taken back (Bassoon 1 has no row here; bassoon gains are now -1.7 / -2.2). The bass clarinet is now the quietest of the low winds, not the loudest.
- Horn 4 has no row. Its CC1 (soft map) leaves it at L 5-13 against Horn 1's 12-19.

**Fix** (`build/roles.json`, slow, phrase-length):
- delete Bass clarinet [624, 672, -4];
- add Horn 4 [648, 669, +3] (its phrase; its edges are in rests);
- keep Bassoon 2 [624, 672, -4] (L 7-16, level with the celli).

**Expected** (i):
- bass clarinet L 11.5-16, best band about +3..-6, still 5-9 dB under the tune;
- Horn 4 L 8-16, best band about -4..-8. That is audible as a moving line under the mf celli, and still under Horn 1.

### 4. Counterstatement and retransition: Oboe 1's p accented halves still peak 1-9 dB under the staccato before them, and Flute 1's unison accents 2-7 dB under (m)

**Measured** (peak dB, c21). Accent against the staccato before it:

| accent (qn, pitch) | velocity | Oboe 1 | Flute 1 (unison) |
|---|---|---|---|
| 87 (G5) | 70 | -45.4 against -44.1 (-1.3) | -4.4 |
| 99 (A5) | 70 | -49.9 against -44.4 (-5.5) | -6.8 |
| 111 (B5) | 70 | -45.1 against -36.3 (-8.8), CC11 64 | -2.0 |
| 123 (C6) | 90 | -35.7 against -31.5 (-4.2) | -3.6 |

The target (Dan, 2026-11-11) is +1 to +2 dB.

**Cause** (m, data, and p.101):
- Each accent plays "Sus Accent MAX". On that row velocity sets the attack's loudness. The three p accents play at 70 and the f one (123) at 90; c21's range test used only 70 / 90.
- The staccato row itself carries c20's +3 dB (`row_dyn_db` "Stac DblTng RRx9" vel<75 +3), so the reference rose by 3 dB.
- At 111, Clarinet 1's held B4 (finding 1) sits an octave below.

**Fix** (instrument side):
- In `build/score_config.py` (the c21 Oboe 1 accent block, `VEL_SET` or its equivalent), set Oboe 1's velocity on 87 / 99 / 111 to 96 and on 123 to 105. First read the oboe KS Master's "Sus Accent MAX" velocity curve and layer table from the .oib, as c21 did for the release times.
- If the row's velocity range tops out under that, add `region_gain_db` {"rows": ["Sus Accent MAX"], "row_db": +3} to Oboe 1 in `build/mix.json`. Only these four notes use the row.
- Flute 1: test the same row ("Sus Accent MAX" is in the Flute KS Master, DIGEST row 240) on its four unison accents, with the same velocities.
- Finding 1 removes the masking at 111. Measure 111 again after it before you raise 111's velocity further.

**Target:** each accent +1..+2 dB over its staccato; 2-5 kHz attack minus body no higher than c21's -3.4..+1.0 dB (weight, not bite).

## Do not touch

- The coda stretto rows (pp now 4.5-6 dB under the p fugatos, consistent with the print).
- The G.P. ride row (it starts after the last chord).
- Clarinet 1's F sharp 5 -2.5 and its pitch-71 +4.5 trims (use the role in finding 1 instead).
- The fugato entry rows.
- The tenor countermelody rows (105-120, 305-320).
- Theme A's margins.
- Horn 1's link, motto and last G sharp levels.
- The solo's margins in 349-356.
- Violins II's trio con sord. lift.
- The violas' and celli's string caps.
- Violins II's and the violas' 996+ summit rows.
- The -14 LUFS delivery chain.

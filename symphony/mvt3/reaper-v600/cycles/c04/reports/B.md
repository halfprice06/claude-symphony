# Critic B, cycle 4 (render c03): balance and levels

## Manual notes (MANUAL-READING row c4 B: May 2021 HO manual PDF pages 49-52, 202-204, 208, read in full; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies in this mockup | Does the render follow it? |
|---|---|---|---|
| p.49 | "Load with Effects off" (Preferences > Other) loads instruments without the onboard convolution reverb, so the reverb can be replaced in the DAW. | Every track. The pipeline keeps Opus's reverb but replaces each patch's reverb with one shared hall (`build/mix.json` reverb: one IR, fx_volume 0.095, low cut 160 Hz, ir_setup). DIGEST p.35/p.49: the switch is off. | Yes, in effect: one room for all 31 tracks. No balance finding needs a different reverb route. |
| p.49-51 | Output configurations (stereo, 16x stereo multi-out). With multi-outs each mic position can go to its own DAW channel, and each mic can send a different amount to a reverb bus. | Each instance outputs one stereo pair; mic gains are set inside Opus (`mix.json` groups: wind Close 0.5 / Main 0.8, horn and trumpet Close 0.5 / Main 1.0, strings and trombones factory). | Not used, and not needed for these findings. The brief asks whether a level problem would be better solved by a mic or row change. All six findings below are offsets of 1.5-10 dB on one dynamic, one span, or one voice of a chord. A mic swap changes a whole track's depth and colour at every dynamic (MANUAL-GAPS #4), so it cannot fix them. Trims and roles are the right tool here (inferred). |
| p.52 | Multi-timbral use: up to 16 instruments in one Opus instance, with MIDI channels auto-incremented. | One instance per track (31). | Not used. It would not reduce sample memory (MANUAL-GAPS memory plan, inferred) and would not change any level. |
| p.202-203 | Dynamics inserts: De-Esser (3-12 kHz), Level Amp (fixed-ratio compressor with make-up gain), Limiter (ceiling -24..0 dB, release 1-400 ms), Limiting Amp (threshold, 0.1-10 ms attack, soft clip). | No insert dynamics on any track. The delivered mp3 is limited by `tools/deliver_master.py` (c03: about 1.3 dB on the loudest peak). | Yes. A per-track limiter would flatten the printed dynamics that the CC1/CC11 layers produce (BRIEF item 2). Leave these off. |
| p.204 | SSL Bus Compressor: threshold -20..+20 dB, ratio 2/4/20:1, attack 0.1-30 ms, release 0.1-1.2 s or Auto, make-up gain. | Not used. Loudness range is set by the delivery ride (`RIDE_TRIMS`, lift ratio 3.0). | Yes. Bus compression would raise the soft accompaniments that findings 4-5 already measure as too close to their solos. Not recommended. |
| p.208 | SSL Transient Shaper: Gain, Amount, Speed; **Invert** subtracts the detected attack, which softens the attack and leaves more body. Usable on the instrument or a mic channel. | Not used. The relevant case is the pp pizzicato under the soft solos (finding 4), whose attack peaks reach the solo's level. | Not applied. As an insert it acts on every row of the track at all times, and Violins II and the basses play arco and loud music on the same instance. A score-timed role (finding 4) is safer. Keep Invert as the fallback if a level cut thins the pizzicato chords too much (inferred). |

MANUAL-GAPS.md: no open item is a balance fix for these findings. #4 (Mid mics) is a colour and depth change, not a level change. #7 (divisi patches) would not change the Violins II level gap in finding 2 (the gap is the 2nd Violins patch at the same CC, Movement I c06).

## Method

- Data: the c03 stems and master as rendered (the stopped-horn level rows are missing from this render and are not counted; Horns 1-4 are not used below except bars 75-77 and 277-279, where no stopped note sounds), with `build/parts.json` and its tempo map (`tools/pcx.py` TM).
- Levels: a 4096-point STFT with a 25 ms hop and stereo power, K-weighted (BS.1770 curve applied as a power response), plus six unweighted bands. "re M" is a stem minus the master over the same span.
- Per-note table: K level over each note's body (0.1 s after the onset to 0.05 s before the end, notes of 0.25 s or longer), grouped by the printed dynamic on the note's staff (`mockup-events.tsv`).
- Pairs: per beat (1 qn), two tracks that each sound for at least 0.75 qn at the same printed dynamic; the median difference over beats. "Doubling" means the two tracks share a pitch class and each plays at most two notes.
- Render variance: I checked findings 1-3 on the c02 render with the same method. c02 gives Trumpet 2 minus Trumpet 1 +1.3 dB at 840-864, Violins II -9.2 / Horn 1 -9.9 re M in the final chord, and Violins II -10.0 re M in F2. These are the same results as c03, so the findings are not render variance.
- Dan's checks through this lens:
  - Items 4, 5, 7: every fix below is a level change in the volume envelope (roles) or in trims. None of them touches an accent's front, a timpani roll, or a note length. The held chords touched by finding 1 last 2.1 s (qn 1108-1113 at 144 qpm), less than one 3.95 s loop.
  - S1, S2: no timing or note-length change.
  - S3: every role starts on an onset of its own track. Each one ends on an onset, or after the track's last note of the phrase, or with a linear end ramp under a printed crescendo. None of them makes a fast fall under a sounding subito (the Trumpet 1 row in finding 3 ends at 866, before the sub. p at 872).
- Cross-family consistency (measured, no finding): pairs at the same printed dynamic follow Rimsky-Korsakov's norm (at p all winds roughly equal, at f a trumpet about two horns and a horn about two woodwinds).
  - Flute 1 minus Trumpet 1: +0.3 at p, -5.9 at f, -4.6 at ff.
  - Oboe 1 minus Horn 1: -3.1 at p, -0.6 at f.
  - Horn 1 minus Trumpet 1: -1.4 at f, -1.5 at ff.
  - Trombone 1 minus Trumpet 1: +1.7 at f.

  The woodwinds' p-to-f span is 3-4 dB against 9-12 dB for brass and strings, but that is what the norm asks for, so "p sounds like p" holds across families. The exceptions are single voices inside sections (findings 2, 3, 5) and soft accompaniments (finding 4).

## 1. The final chord (bars 277-279, qn 1104-1113) is led by Horn 1 and Violins II; Trumpet 1, on the chord's brass top, is the quietest trumpet (measured)

**Where.** Horn 1, Violins II, Trumpets 1-3 and Trombones 1-2, from the short ff chords of bar 277 through the fff chord at 278 to the cut at 279.2. All are printed fff at 278. The score (finale.ily) has the strings div. a 3 tremolo and the brass chord with Tpt 1 and Hn 1 on C5.

**Evidence (K, re M).**

| span (qn) | Horn 1 | Horn 2 | Tpt 1 | Tpt 2 | Tpt 3 | Tbn 1 | Vln I | Vln II | Fl 1 |
|---|---|---|---|---|---|---|---|---|---|
| 1104-1105.5 | **-7.9** | -13.8 | -14.4 | -12.0 | -11.5 | -11.8 | -12.7 | -10.6 | -20.1 |
| 1108-1109 | -9.5 | -15.4 | -15.3 | -13.9 | -13.4 | -13.8 | -13.6 | **-8.5** | -10.5 |
| 1109-1112 | -10.0 | -13.8 | -14.4 | -13.4 | -11.7 | -13.0 | -12.3 | **-9.5** | -11.7 |
| 1112-1113 | **-10.2** | -14.6 | -14.0 | -13.3 | -10.4 | -13.8 | -11.9 | -10.5 | -11.4 |

- Over the held chord Horn 1's C5 is 4.4-5.8 dB over Trumpet 1's C5 at the same pitch and velocity (127). In 0.5 qn frames the gap is 3.3 dB at the last quarter (-17.8 against -21.1). Trumpet 1 is the weakest of the three trumpets. By the Rimsky norm (trumpet = 2 horns in forte; c184 in finale.ily cites it), the trumpets should lead the brass.
- Violins II (C5-E5-G5 tremolo) is the loudest stem in the chord, 3.9-5.1 dB over Violins I (C6-E6-G6). The cause is the final-chord role +5 on both sections (`roles.json` [1107.9, 1113.5, 5]) on top of Violins II's +1 dB gain and its fff pair offset (Vln II minus Vln I at fff: +1.4 dB, against -1.9 at ff and -4.0 at f).
- Horn 1 rises through the chord because of c03's counter-shape (`LEVEL_SHAPES` Horn 1 +4 dB over 1108.5-1112.5), which is needed against the sample's sag (the stem still falls 4 dB from 1108 to 1112.5). Its vol_db runs from +7.4 to +8.8, against Trumpet 1's +4.5 falling to +2.3. The excess is the C5 sample's level, not the envelope.
- Bars 273-276 (1088-1104), where Horn 1 carries the a2 chain G-F sharp-F-E (UNI_BOOST +3 dB), are intended as the strongest moving line (finale.ily c034). Horn 1 at -8.3 / -9.6 re M is right there, and this finding starts at 1104.
- The c02 render gives the same order (Vln II -9.2, Horn 1 -9.9, Tpt 1 -14.8 re M at 1108-1112).

**Fix (`build/roles.json`).**
- Violins II `[1107.9, 1113.5, 5]` -> `[1107.9, 1113.5, 2]`.
- Horn 1: new row `[1104, 1113.5, -3.5]`. Keep the LEVEL_SHAPES counter-shape.
- Trumpet 1: new row `[1104, 1113.5, 3.0]`.
- Trumpet 2, Trumpet 3, Trombone 1, Trombone 2: new rows `[1104, 1113.5, 1.5]`.

1104 is an onset on all six tracks. The default 0.5 qn ramp-in falls on the last half beat of the crescendo into 277.

**Expected (arithmetic, incoherent sum).**
- At 1109-1112: Horn 1 -13.5, Violins II -12.5, Trumpet 1 -11.4, Trumpet 2 -11.9, Trumpet 3 -10.2, Trombones -11.5 / -12.0, Violins I -12.3. The trumpets now lead, and the two violin sections are level.
- The master changes by about +0.05 dB (Horn 1 and Violins II remove 0.111 of the master's energy, and the brass rows add 0.122). Bar 278 stays the loudest bar after 223, and the limiter load does not change.

## 2. Violins II plays 3-6 dB under Violins I wherever it doubles the tune at mf and f; in F2 (bars 67-82) the harp sits level with the tune (measured)

**Where.** Violins II with Violins I in unison or octaves:
- F1, bars 13-24 (qn 51-94, f);
- F2 in E flat, bars 67-82 (264-328, mf, "arco, unis., cantabile", the octave below Vln I);
- M, bars 187-197 (744-788, mf, printed "cantabile unis. with Vln I");
- Q, bars 234-242 (935-968, mf-f).

Harp, F2 (mf arpeggios).

**Evidence.**
- Violins II minus Violins I on doubling beats: mf -5.1 dB (123 beats), f -4.0 (116), ff -1.9 (170). By span:

  | span (qn) | dynamic | Vln II minus Vln I |
  |---|---|---|
  | 51-62 | f | -5.3 |
  | 64-78 | f | -3.0 |
  | 83-94 | f | -3.3 |
  | 264-283 | mf | -4.8 |
  | 285-298 | mf | -5.4 |
  | 300-308 | mf | -6.0 |
  | 308-324 | f | -5.0 |
  | 744-763 | mf | -5.5 |
  | 766-788 | mf | -5.4 |
  | 935-952 | mf | -3.6 |
  | 952-968 | f | -3.2 |

- With 14 players against 16, the acoustic difference would be about 0.6 dB. Movement I c06 measured 3.7-4.6 dB of this gap as the 2nd Violins patch's own level at the same CC. The Finale's trims make it slightly worse: Violins II gain +6 against +5, but mf trim -0.8 against +1.0 and f trim -1.0 against 0.0.
- F2, bars 67-82 (re M): Violins I -5.4, harp -8.2, cellos -9.7, Violins II -10.2, violas -11.3. In 2 qn frames over 270-302 the harp is within 1-3 dB of Violins I, and at 292-295 it is over it (-4.1 / -3.7 against -6.1 / -8.8). This is despite the role `[264, 328, -4.0]`, because the octave below the tune, which should carry it, is missing. The same holds on c02 (harp -5.2 against Vln I -5.7 at 288-304).

**Fix (`build/roles.json`, Violins II; all boundaries are Vln II onsets).**
- `[48, 96, 3.0]`
- `[264, 328, 3.0]`
- `[744, 788, 3.0]`
- `[936, 968, 2.5]`
- Harp `[264, 328, -4.0]` -> `[264, 328, -6.0]`.

Roles rather than the mf/f trims: a +3 dB mf trim would also turn Violins II's mf-to-sub. p at qn 872 into a 2.2 dB fall of the post-hall envelope (S3). The roles avoid that.

**Expected.**
- Doubling gap mf -5.1 -> about -2.1 and f -4.0 -> about -1.0 (Violins I level with or 1-2 dB over its lower octave).
- F2: Violins II -7.2 re M, harp about -10.6 (2-3 dB under the tune at bars 73-74 instead of over it).
- Master +0.3 to +0.4 dB in these spans (delivery ride unchanged; LRA effect under 0.2 LU).

## 3. At ff, Trumpet 2 plays over Trumpet 1; in theme B (bars 211-218) the harmony third is louder than the tune (measured)

**Where.** Trumpets 1-2, every ff passage where they play together:
- theme B, bars 211-218 (qn 840-864): Tpt 1 has the tune "cantabile", Tpt 2 a third or sixth below on the same staff;
- the codetta, bars 91-94 (360-374);
- the stop chord, bars 147-150 (584-599);
- the coda, bars 199-204 (792-814).

Table: `build/mix.json` `dyn_trim_db` ff for Trumpet 2 (10.0) against Trumpet 1 (7.3).

**Evidence.**
- Trumpet 2 minus Trumpet 1 on ff beats: +1.5 (840-864, 24 beats), +1.9 (360-374), +3.1 (584-599), +1.7 (792-814). Over all 76 ff beats the median is +1.4. On c02 it is +1.3 at 840-864.
- In 2 qn frames over 840-862, Trumpet 2 is over Trumpet 1 in 10 of 12 frames (by up to 3.1 dB at 844).
- Over the theme the spans read Trumpet 2 -6.3, Trumpet 1 -7.9 re M. The theme is also doubled by Ob 1 (-11.1), Fl 1 (-12.4) and Vln I (-12.6), but the brass statement is what the brief names as the theme's carrier.
- Trumpet 3 minus Trumpet 1 at ff is -0.4, so only Trumpet 2's trim is out of line. A second player normally balances to the first.

**Fix.**
- `build/mix.json` Trumpet 2 `dyn_trim_db` ff 10.0 -> 8.0.
- `build/roles.json` Trumpet 1 new row `[840, 866, 1.0]` (840 onset; Tpt 1's last note of the phrase ends at 864.14; 866 is before the sub. p entry at 872).
- The ff-to-p trim fall at 872 on Trumpet 2 shrinks from 3.7 to 1.7 dB, which is better for S3.

**Expected.**
- Theme B: Trumpet 1 about 1.5 dB over Trumpet 2.
- Codetta about -0.1, stop chord about +1.1, coda about -0.3 (Tpt 2 minus Tpt 1).
- Master -0.2 dB at 840-864. The arrival at 888 is not touched (Trumpet 2 is fff there).

## 4. The pp accompaniments of the soft solos reach the solo's level at their attacks (measured)

**Where.**
- Violins II pizz. div. pp under Trumpet 1's p solo, bars 51-66 (qn 201-264).
- Double basses pizz. pp under the bassoon solo, bars 117-122 (464-488).
- Clarinet 1's pp D6 with < >, bars 121-122 (481-486), against the bassoon's p line.

**Evidence.**
- Attack peak (best 150 ms window) of each accompaniment note minus the solo's peak in the same window. The solo's own peak is 1.8-1.9 dB over its 2 qn average.
  - Bars 51-66: Violins II median -2.7 dB, p90 +0.6. Double basses -4.9 / -0.5. Cellos -6.4 / -2.2 (their pizz has had roles since c01 B #5).
  - Bars 115-122: Double basses median -6.9, p90 +3.6.
  - Bars 171-186: Double basses -4.6 / -1.5. Cellos -9.2 / +1.1.
- In 1 qn windows at 468, 470 and 472 the basses' pizz reads -4.3 / -2.4 / -3.0 re M against the bassoon's -2.3 / -6.0 / -5.8.
- Clarinet 1 at 481-485: -3.7 / -2.2 / -2.7 / -2.8 / -3.5 re M, level with or over the solo bassoon (-3.5 / -4.6 / -3.7 / -3.9 / -3.2). Clarinet 1's pp notes there measure -37.2 dB K, against its other pp notes at -48.
- By the norm a plucked pp chord and a pp echo sit well under a p solo. The c03 report listed only span averages (Trumpet 1 -2.5 against Clarinet 1 -9.4), which hide these attacks.

**Fix (`build/roles.json`).**
- Violins II `[201, 264, -3.0]` (201 = first pizz onset, 264 = the arco F2 onset).
- Double basses `[464, 488, -3.0]` (both are onsets).
- Clarinet 1 `[481, 486, -4.0]` (481 onset; the last note ends 485.64).

These are 3-element rows. The basses' existing 4-element bass-octave rows lie outside these spans.

**Expected.**
- Violins II pizz peaks about -5.7 under the trumpet (p90 -2.4).
- The basses' pizz p90 about +0.6 under the bassoon.
- Clarinet 1 about -6..-7.7 re M, 3 dB under the bassoon.
- Master changes are under 0.2 dB (the delivery ride already lifts these spans).

## 5. Inner pp voices drop out of their chords: Clarinet 2 is 5-8 dB under the other held pp woodwinds, and Horn 2 is 10 dB under Horn 1 in their pp duet (measured)

**Where.**
- Clarinet 2, the held pp chord under Trumpet 1's solo, bars 51-66 (qn 200-266; with Cl 1 and Bn 1), and under the cor anglais and muted trumpet, bars 170-186 (676-744; with Bass clarinet and Cl 1).
- Horn 2, the pp thirds and sixths with Horn 1 in F2, bars 75-77 (296-308), before the crescendo to mp at 308.

**Evidence.**
- Clarinet 2's pp notes: median -54.9 dB K (25 notes, 184-262) and -55.4 (29 notes, 676-772). Clarinet 1's pp notes measure -48.0 / -48.4, Bassoon 1's -50.8, the bass clarinet's -46.8.
- Re M: at 200-264, Clarinet 2 -17.6 against Clarinet 1 -9.1 and Bassoon 1 -12.0. At 676-744, Clarinet 2 -16.9 against the bass clarinet -10.2 and Clarinet 1 -14.4.
- Clarinet 1 and the bass clarinet already carry -4 dB roles in these spans (c01 B #4). Clarinet 2 is the middle of a three-voice pp chord and sits 5.6-8.5 dB under its neighbours. At pp the norm puts all winds level.
- Horn 2 at 296-306 is -22.5..-23.9 re M against Horn 1 -11.9..-13.4. Both are at CC1 28, the same vol_db, and the Sus MAX row. The gap is the samples at Horn 2's lower pitches (G3-B flat 3: horn pp Sus MAX at median pitch 56 measures -49.5 dB, at pitch 64 -39.9). The lower voice of the duet is effectively missing.

**Fix (`build/roles.json`).**
- Clarinet 2 `[200, 266, 5.0]` (200 onset; its last note ends 265.2; the next onset is 676) and `[676, 744, 3.0]` (both are onsets). Keep c03's `[184, 200, 6.0]`: Clarinet 2 is -14.3 re M there now, which is right for that passage.
- Horn 2 `[296, 310, 6.0, 6]`: full +6 to 304, then the end ramp (4th element) fades it to 0 by 310, under the printed crescendo 304-308.

**Expected.**
- Clarinet 2 about -12.6 re M at 200-264 (level with Bassoon 1, 10 dB under the solo) and about -13.9 at 676-744.
- Horn 2 about -16.5..-18 at 296-304, 4-5 dB under Horn 1.
- Master changes are under 0.3 dB.

## Do not touch

- The cross-family balance at p, f and ff (the pairs in Method follow the Rimsky norm).
- Solos over their accompaniment by span average:
  - Trumpet 1 at bars 51-66: -2.4 re M;
  - the bassoon at 115: -2.2;
  - the harp solo at 123-134: -4.0;
  - the cor anglais -3.2 with muted Trumpet 1 -6.4 at 171-186.
- F1 in the bass at 27-34 (Tuba -7.2, Horn 3 -7.5, basses -9.1 over the violins' countersubject -10.8).
- The chorale:
  - 224-225: brass families -6.8..-7.2 over violins -9.3;
  - 230-233: brass -6..-9 over violins -12..-17;
  - 255-264.
- The fff family order at 223, with crash -13.2 re M (carrying 5-12 kHz, not dominant) and timpani -19.2.
- Bar 223 Trumpet 1 at -10.1, level with Trumpet 3.
- The timpani roll trims and settle skip.
- The bass drum's velocity 114.
- The bass-octave roles and `loud_eq`.
- The Horn 1 a2 chain at 273-276.
- The hall settings.

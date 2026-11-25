# Cycle 32, critic C (holistic): the c31 render of v600

Lens: listen through the data as a conductor would. Compared: c31 (stems, master, delivered mp3), the c27 port baseline, series 1's c26 render of v77 (this is also the render five cycles back; it is the only earlier render with full stems before c27) on unchanged passages, and the stored reference metrics. Levels are stereo-power RMS unless marked K (BS.1770 K-weighting applied in the spectrum). Bar/qn mapping as in BRIEF "The music". "Measured" means a number from these files; "inferred" means reasoned from them, the manual or the patch files.

## Manual notes (H2: May 2021 HO Opus manual PDF pp. 44-45, 134-136; MANUAL-GAPS.md read)

| Page | What it says | Where it applies here | Render follows it? |
|---|---|---|---|
| 44 | MIDI channel modes (Multi, MPE, Omni, 1-16): CC1, CC11 and pitch bend apply per channel | One Opus instance per track, one channel each | Yes; nothing here depends on per-note control. |
| 45 | CC1 "is commonly used to cross-fade between dynamic layers and / or vibrato layers"; CC11 controls volume, "or used to independently control dynamics when Modulation (CC 1) is being used to control vibrato depth" | Every string and woodwind KS Master (CC11 = dynamics, CC1 = vibrato) versus the brass and clarinet KS Masters (CC1 = dynamics) | Yes for the families as configured. Read in the patch for this report (finding 6): in `1st Violins KS Master.oib` and `... DIV A.oib`, the dynamic-layer tables (pp/p/mf/f/ff) are driven by the cc 11 controller and the Non Vib / Sus Vib / Molto Vib tables by cc 1. `cycles/c31/oib5.py` labels both "cc=1" because every connection is named "Amount Controller 1->Volume"; its source field ("Midi Controller" = cc 11, "Midi Controller 1" = cc 1) tells them apart. So c31's deferral of A #5 ("DIV A layer groups on cc 1") rested on a misread; CC1 on the strings is the vibrato control, as the kit says. |
| 134-135 | Play page; Moods, Performance, Sensitivity, Envelope; Stereo Double, Reverb | General | Not used: everything is set in the state and in REAPER. |
| 136 | Moods: Classic = Main mics + 3.4 s Southern California hall; Soft = Mid + Surround (or Vintage) through Abravanel Hall, for "slower, more emotional passages"; Epic = Close + Main + Surround, 2.8 s cathedral | The whole movement is an Adagio; the muted strings bars 15-30 and the coda | Partly. The mockup uses Close + Main and one shared true-stereo S. Cal Hall (3.3 s), close to Classic. The Soft mood's Mid-mic choice is MANUAL-GAPS #4 (winds and horns), still untried. The p.136 text does not mention con sordino or a compressor for Soft (the MANUAL-READING row says it does). |

## Where c31 stands overall (measured)

- Per-bar master against c27: within ±1 dB in 70 of 92 bars. Larger moves are the intended ones: bars 4-5 -2.3/-1.7 (bass clarinet swell fixed), 35 -3.0, 56 -1.9 (c30 C #2), 79-80 -2.7/-2.6 (climax order), and the coda clarinet (+2.1/+2.2 in bars 85-86, finding 5).
- Delivered maximum short-term loudness per section: climax 61-64 -10.4 LUFS, cadence 79-82 -11.3, bars 53-60 -12.0, A' 71-78 -13.8, strings 23-30 -16.9; soft sections -18.3 to -23.5. The climax is the loudest section, but by 0.9 LU (c26: 1.7).
- Loop pulsing (BRIEF 8): of the 33 notes held 8 s or longer (re-bow pieces merged), none shows a period at 3.95 s in both band level and centroid. The strongest are the bars 67-70 ppp timpani roll (0.46/0.56, but no peak at 3.95 s in a 1-6 s lag scan, and it sits 12-15 dB under Horn 1) and Contrabassoon 87 (0.44 level only). All final-chord string pieces read -0.38 to +0.29. No action.
- Against recordings: master motion 6.37 / 4.30 dB (Brahms 1/ii 8.55/4.56, 4/ii 6.29/3.92; c27 6.65/4.34); band shares inside the reference spread except 100-250 Hz (-8.4 against -6.6 to -8.8). No action.

## Findings, ranked by what a listener would hear

### 1. Bar 63 downbeat (qn 212, sf, the moment before the trombone quotation): Flute 1 shrieks 11 dB over its own ff and sets the delivery limiter, while the strings' sf is heard in Violins II only (measured)

- Where: Flute 1 qn 212.0-213.0 (A6, sf, slurred from the tied A flat 6 ff); Violins I/II, violas, celli at 212 (sf, trem.).
- Evidence. Flute 1 in 50 ms frames: -28/-29 dB on the held ff A flat 6, then -17, -18, -18, -19, -22, -20 dB from 212.0. That is +11 dB over its own body, the loudest stem at 212.0-212.5 (-20.0 against Violins I -24.6, Violins II -23.2). 2-5 kHz in the first 80 ms is +7 dB over the flute's body. The master rises 3.5 dB at the join. The highest pre-limiter peak of the delivery is at qn 212.20 (234.53 s, -0.08 dBFS; metrics.md), so this one flute note sets the 1.4 dB limiter. It has grown each series: c26 +7 dB, c27 +10, c31 +11. Cause (read in parts.json): the sf CC11 spike 114 -> 122, the sf vol_db weight (+6.18 dB at 212.063), CC1 75 -> 110, on top of a Leg Slur MAX transition into the top of the range.
- The strings' sf is uneven. Half-beat levels from 211.5 to 212.0: Violins I -23.5 -> -24.6 (-1.1 dB), Violins II -30.1 -> -23.2 (+6.9), violas -27.9 -> -27.0 (+0.9), celli -24.6 -> -25.3 (-0.7). The sf is audible as an accent only in the inner voice. BRIEF item 4 asks for 2-4 dB of weight with no hard front. Here the top voice has none and the flute and Violins II have 7-11 dB.
- Fix.
  - Flute 1. `build/roles.json` "Flute 1": add `[211.95, 213.05, -7, 0.03]`. Better, put the cut in CC7 before the hall (S3), in the same way as the c31 bar 63 lanes: a Flute 1 CC7 lane of 127·10^(-7/20) = 57 from 211.95 to 213.0, back to 127 at 213.0. Target: the A6's first 0.4 s at -24 to -25 dB, 3-4 dB over its own A flat 6 and not over Violins I.
  - Strings. Violins II -3 dB over 212.0-212.5, and Violins I and violas +2.5 dB sf weight over 212.0-212.4. Target: each section 2-4 dB over its own 211.5 level.
  - These roles touch 211-215, so recompute the bar 63 CC7 lanes with `cycles/c31/a2cc7.py`, as the c31 do-not-touch line requires. Level only: a stem fix can check it.
  - Expected: the delivery limiter falls from 1.4 dB toward the next peak (qn 210.6, -0.28 dBFS).

### 2. Bars 79-81 (qn 262-271, ff cadence): one flute leads the unison with sixteen first violins, and in bar 80 no voice leads (measured)

- Where: Flute 1 and Violins I, in unison on B flat 6-A flat 6-G6 and the descent (mockup-events: both play the same pitches 259-271), with Violins II, Oboe 1 and Clarinet 1 an octave lower.
- Evidence (K-weighted bar levels, loudest stems):

  | Render | Bar 79 | Bar 80 | Bar 81 |
  |---|---|---|---|
  | c31 | Flute 1 -25.2, Violins I -25.7 | Flute 1 -27.6, celli -28.3, a2 horns -28.6, Violins I -28.9 | Flute 1 -30.9, Violins I -32.9 |
  | c26 | Violins I -25.7, flute -26.1 | Violins I -26.3, flute -29.7 | Flute 1 -31.3, Violins I -31.7 |

  In bar 80 the five loudest stems lie within 1.3 dB of each other, and the tune is fourth. A full first-violin section at ff in unison with one flute is heard as violins with added brightness, not as a flute solo. The +7 dB flute lift was removed in c28, but the remaining Flute 1 rows (`[262.6, 263.5, -3]`, `[263.5, 265.9, 1]`) and the celli/a2 horns still leave the tune with no lead.
- Fix: `build/roles.json` "Flute 1": change `[262.6, 263.5, -3]` to `-6`, change `[263.5, 265.9, 1]` to `-2`, and add `[265.9, 271.0, -3]`. If bar 80 still has Violins I under the celli after that, add Violoncellos `[265, 268, -1.5]`.
  - Target, K-weighted: Violins I at least 1.5 dB over Flute 1 and over every other stem in bars 79-80.
  - This also takes 0.3-0.5 dB off the cadence (inferred from the flute's share). That moves the climax margin (delivered 0.9 LU) toward c26's 1.7.
  - Level only: stem fix.

### 3. Bar 29 (qn 85.9 and 86.9): two legato joins bump the master 4-6 dB inside the f -> p diminuendo into the A section's full close (measured)

- Where: Violins I and II, the quaver descent 85-87 (both sections in unison, decrescendo from f at 82 to p at 87).
- Evidence (frames of 0.04 qn):
  - At 85.84-85.96, Violins I -39 dB against a -47 body and Violins II -38 against -44. The master reads -34 against -40 on both sides.
  - At 86.80-86.96, Violins II -39/-40 against -47 before and -51 after. The master reads -35 against -39/-41.
  - The Violins I notch at 86.38-86.51 (JOIN_NOTCH) works; these two joins have none.
  - Series 1 had the same bumps (c26 master -34 at 85.875), so this is an old fault on notes v600 kept.
  - Two other joins reach the master at +3 dB or more: Violoncellos 77.0 (+3.3, bar 26) and Violins I 184.0 (+2.5, bar 54).
  - Across all legato joins of the melodic tracks, the stem's 30 ms peak over the louder body has a median of +2.2 dB on Violins I, +3.2 on violas and +0.7 on celli, unchanged since c27. Most are masked; the ones listed here are not.
- Fix: `build/score_config.py` `JOIN_NOTCH` (moved-qn windows, like the existing rows):
  - "Violins I": add `(85.84, 85.98, -6.0)`.
  - "Violins II": add `(85.79, 85.95, -5.0)` and `(86.78, 86.98, -5.5)`.
  - "Violoncellos": add a notch at the 77.0 join, about `(76.85, 77.00, -4.0)`. Check its moved onset in parts.json first.
  - Target: the master at both bar 29 joins within 1.5 dB of its neighbours, with the diminuendo falling monotonically from 85 to 87.

### 4. The p and pp horn solos still have the mf colour turned down; c30's darker soft colour went with the legato-collapse fix (measured gap, fix inferred)

- Where: Horn 1, the dolce theme bars 7-14 (qn 18-42), the retransition bars 67-70 (226-238) and bar 81 p (271-274). The same applies to Horns 2-4 and the a2 track in their soft entries.
- Evidence (Horn 1 stem, 1-5 kHz share of the 60 Hz+ energy):

  | Render | bars 7-10 (p) | bars 11-14 | bars 67-68 | bars 55-56 (mp-mf) | bars 61-62 (ff) |
  |---|---|---|---|---|---|
  | c26 / c27 / c29 / c31 | -15.7 | -13.1 | -16.0 | -10.8 | -8.6 |
  | c30 | -19.4 | -17.6 | -19.9 | -12.8 | -9.0 |

  The horn's colour spans only 7 dB from p to ff. c31 had to return the soft horns to CC1 57-72 because the 1FH transition table collapses legato targets under about CC1 54, so the soft layers cannot be used for this line (c31 CHANGES). The solo horn is the first melody a listener hears (bars 7-14) and the one that closes the climax section (bars 67-70). A bright, close p horn reads as a sampled mf.
- Fix: use the existing `loud_eq` mechanism (a ReaEQ after Opus whose Wet follows score-qn points linearly) as a soft-dynamic shelf in `build/mix.json` "Horn 1": `"loud_eq": {"points": [[0,1],[186,1],[194,0],[220,0],[221,1],[258,1],[261,0],[270,0],[271,1],[304,1]], "bands": [{"band": "highshelf", "hz": 1200, "db": -4}]}`.
  - If `loud_eq` is already a list on a track, append to it.
  - Same points and shelf on Horns 2 and 4 and the a2 track for their p/mp entries. Horns 3-4's `mute_eq` from 278 already darkens the coda.
  - This is FX only (`--mix-only` plus a stem check, no new row, no CC change), so it cannot bring the collapse back.
  - Target: 1-5 kHz share -19 to -20 dB in bars 7-10 and 67-68 (c30's values), level within ±0.5 dB of c31 per bar, and f/ff unchanged (wet 0 from 194 to 220 and from 261 to 270).

### 5. The coda's pp clarinet solo (bars 85-86) rose 2-3 dB with no change aimed at it, and is now as loud as the p horn theme (measured)

- Where: Clarinet 1, qn 280-286 (first phrase, "dolce", printed pp with a < > hairpin). The second phrase (286 on) was raised on purpose by c31 B #2 and is not part of this finding.
- Evidence (K-weighted per bar, bars 85-89):

  | Render | 85 | 86 | 87 | 88 | 89 |
  |---|---|---|---|---|---|
  | c26 | -44.0 | -41.2 | -41.7 | -44.2 | -44.3 |
  | c27 | -44.0 | -41.2 | -42.5 | -44.4 | -44.3 |
  | c31 | -41.4 | -39.4 | -41.2 | -43.6 | -43.2 |

  - Horn 1's p theme in bars 7-14 measures -45.3 to -37.8 K (mean about -41.6). The pp coda solo is therefore at the level of the p theme.
  - The delivered coda maximum is -22.2 LUFS (c26 -24.7, c27 -24.2). That is the loudest of all the soft sections bar the bass clarinet's mf, in a passage marked ppp/pp and morendo.
  - The likely cause is c30's CC1 dynamics refit on the clarinets (the soft trims were refitted per printed dynamic, and three stacked series 1 roles at 280-297 sum to +7.5 dB at 284-286). It is not a deliberate change.
- Fix: `build/roles.json` "Clarinet 1": add `[280, 286, -2.5, 0.5]`. Target: bars 85-86 at -43.5 / -41.5 K, back to c27, still 6-8 dB over the ppp/pp celli (now +8.8/+11.0 in plain RMS). Level only: stem fix.

### 6. The bars 17-22 violin solo sits in the middle of the Sus Vib / Molto Vib crossfade (patch read; audible effect inferred)

- Where: Violin I solo (1st Violins KS Master DIV A, Leg Slur MAX), qn 48-65. CC1 is 95 on the held notes, with peaks of 105 at 48.5 and 60.5, and 75-95 in between (parts.json).
- Evidence. Read in `1st Violins KS Master DIV A.oib` with the source field resolved (see the manual table). For the Leg Slur MAX row (row 2), CC1 values below are listed as tables over CC1 50/64/80/90/100/110:
  - Sus Vib: 0.98, 1.0, 1.0, 0.83, 0.29, 0.
  - Molto Vib: 0, 0, 0.43, 0.74, 0.94, 1.0.
  - The Molto Vib legato groups exist only as one soft group, whose CC11 table is 0.15-0.31 (V1s mf).
  - So at CC1 95-105 and the solo's p CC11 (about 46-60), the solo plays two vibrato layers at once, each at a reduced weight.
  - The kit (section 3) measured that holding CC1 inside a vibrato crossfade on a flute made the two layers beat: 1.5-4 kHz modulation 10.5 -> 16.9 dB. That matches what critic A heard in the data twice (c30 A #1, c31 A #5: no clear vibrato on the held notes).
  - c31 deferred A #5 because `oib5.py` showed the DIV A dynamic tables "on cc 1". They are on cc 11; that reading was wrong.
- Fix (test on this one track): in `build/score_config.py`, give the Violin I solo a fixed CC1 of 72 over 47.8-65 (Sus Vib only, Non Vib and Molto Vib at 0), in place of the vibrato rule's 75-105. The existing generic option does this: `CC1_HOLD = {"Contrabassoon": 40, "Violin I solo": 72}` (`tools/score_to_parts.py` line 3308; the solo track plays only qn 48-65). If that still sounds plain, test 115 (Molto Vib only).
  - Re-fit the level with a stem fix: Sus Vib alone at CC1 72 is louder than the 95-105 mix. Inferred about +3-5 dB from the tables; measure it.
  - Measure on the held notes 49, 51, 61 and 63: 4-7 Hz amplitude modulation depth at 1-4 kHz and the f0 wobble, against c31.
  - This is DIV A only (Close mic, small section). Hollywood Solo Violin is still not installed (MANUAL-GAPS #3).

## Smaller observations (not ranked)

- Bars 69-70 (qn 232-238): Horn 1's motto tail ends level with Bassoon 1 (K: Hn1 -47.1/-46.7, Bn1 -47.0/-47.2 at 236-237; c26 kept the horn 4-5 dB over). The bassoons' printed cresc at 235 makes some crossing legitimate. Watch it after finding 4, which leaves its level unchanged.
- Bar 36 (qn 105-108): the bass clarinet's pp end of the solo falls only 1.6 dB from bar 35 (master -40.2 -> -41.8; c26 -41.6 -> -45.4). The register differs from v77, so this is not a direct comparison. Small.
- Final chord: the master falls from -54 dB at qn 304 to below -83 dB within 1.5 s, close to the hall's own decay. The delivered file keeps about 1 s of audible tail. Fine.

Do not touch: AUTO_REBOW, `space_rebows.py` and every fitted re-bow (no loop period anywhere in the render); the c31 horn CC1 map (57-72 soft, CC1 dynamics from f up); the bar 63 CC7 lanes (recompute them, do not remove them, when finding 1 changes roles at 211-215); Trombone 1's quotation shapes and trims; the climax order of c28; GENTLE_ACCENT; the delivery chain (LRA 15.6, span 17.4); the timpani CC1 layers and roll trims.

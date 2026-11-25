# Cycle 56, critic C: whole-piece check of the first render without per-note volume moves, references, CC lanes, mix; dynamics over time (on the c55 render)

Material: `cycles/c55/render/` (the delivered stems and master, after the five-row stem fix), `cycles/c55/build_fix/parts.json` and `mix.json` (the data of the delivered stems), `cycles/c55/mvt2-mockup-c55.mp3`; for comparison `cycles/c54/render/`, `cycles/c54/build_fix/parts.json`, `cycles/c54/mvt2-mockup-c54.mp3`. The written envelope comes from `tools/build_reaper.py` `vol_points` with the source cut before `ENV_LUA` (nothing sent to REAPER). References: `/Users/gooby/sandbox/mockup-reference-cn1rc0/mockup-kit/reference/` (my own count of `<VOLENV` points), `mockup-kit/EW-TEMPLATE-FINDINGS.md`. Scratch, left in place, 216 MB, no simulated audio: `/private/tmp/claude-501/mockup-loop/mvt2-c56-C/` (`arc.py`, `attrib.py`, `line.py`, `hp.py`, `regions.py`, `envfast.py`, `cc.py`, `timbre.py`, `loop.py`, `fine.py`).

Method. 10 ms power frames and third-octave frames (50 ms hop) of every stem and the master for both cycles; note body = 20-80 % of the note; ffmpeg `ebur128` on masters and mp3s. No MIDI note changed between c54 and c55 except the timpani and viola pizzicato velocities, so a stem difference c55 minus c54 is the removed envelope (plus the section rows). Every figure is measured unless marked inferred. No fix below is a track volume move on one or two notes; where I name the envelope it is a section row of two bars or more or a role over three or more onsets.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 56, so no page range was read. Used from `MANUAL-GAPS.md`, the kit and the peers:

| Source | Where it applies | Render follows it? |
|---|---|---|
| Kit LEARNINGS line 54: CC7 is linear amplitude inside Opus | the bar 63 CC7 lanes (finding 2); a CC7 change can be simulated offline like a gain | The lanes are still in the MIDI; their envelope half is gone |
| Kit LEARNINGS line 66: CC11 5.7 / 3.5 / 2.5 / 1.2 dB per 10 steps at CC 0-40 / 30-60 / 50-80 / 88-128 | every CC11 fix below | My in-note slopes on c55 agree (table in "CC lanes") |
| Scherzo `tools/build_reaper.py` `region_gain` (lines 355-398): `mix.json` `region_gain_db` with `pitch_db`, `row_db`, `row_dyn_db`; Finale technique 64 | per-pitch and per-row level inside Opus | Movement II's `build_reaper.py` has no such function (grep: no `region_gain`, no `row_volume`) |
| BRIEF "Facts": in the Clarinet KS Master CC1 crossfades the dynamic layers | Clarinet 1 coda: CC11 is level only there | CC11 not used for the level |
| HO manual p.99 / p.144 (MANUAL-GAPS): legato velocity sets transition time, not level | soft legato starts cannot be fixed by velocity | n/a |

## Slot C part

### 1. Whole piece, c55 against c54 (master and mp3)

Delivered mp3: -19.8 LUFS both; LRA 15.1 -> 15.4 LU; short-term 10th percentile -28.4 -> -28.8, maximum -10.3 -> -9.7 LUFS, span 18.1 -> 19.1 dB (limit 19). The maximum moved because bar 61 rose 0.6 dB (basses +1.8, Horn 1 +2.0, Bassoon 2 +2.7); the 10th percentile because bar 86 fell 2.3 dB (Clarinet 1 -3.2, basses -4.6) and now lies under it. 60 of 92 bars are within 1.0 dB of c54 on the master; 23 bars moved 1.5 dB or more, 11 of them 2 dB or more.

| passage | better | worse (stem that carries it) |
|---|---|---|
| bars 1-6 | level unchanged (within 0.5 dB) | re-bows of Violins I 2.4 / 4.6: stem dip 4.8 -> 12.9 dB, master 2.2 -> 4.2; Clarinet 2 at qn 6 (6 s held): 3.95 s autocorrelation of the level -0.05 -> +0.76, but only 1.4 dB peak to peak |
| 7-14 Horn 1 theme | S unchanged (median -2 ms) | bar 11 +2.9, bars 9-10 and 12 -1.3 to -1.7 dB; the crescendo 30-34 now peaks one note early (finding 1) |
| 15-22 | Violin I solo margin -5.0 -> -2.4 dB | Oboe 1 bar 16 +2.3, bar 20 -3.2; Oboe 1's decrescendo 45-47 flat (+0.3 dB, was -3.4); Violins II 47 is 9-12 dB under its neighbours (was 3.2) |
| 23-30 violins' theme | basses' decrescendo 82-87 now falls (-0.9, was +2.5) | bars 23-24 -0.8 / -1.5, 25-26 +1.5; the crescendo 78-82 of both violin sections reversed on the long F5 (-2.4 / -1.0 dB, was +2.8 / +3.5); bar 30 +3.2 (basses' A flat 1 +6.9) |
| 31-36 | | Bass clarinet margin 4.5 -> 2.6 dB; bar 31 -1.9, bar 35 +3.9 (the 4-beat note after the breath, inside a printed decrescendo) |
| 37-44 | | bar 44 +3.3: Flute 1's last note of the phrase (pp) is 9.6 dB over c54 and 13 dB over the note before it; Violins II div 119 re-bow master dip 4.1 -> 8.0 dB |
| 45-52 | Oboe 1 margin 4.2 -> 5.8 dB | bar 48 +3.0 (Cor anglais A4 +4.9); the fp of bar 47 reaches its peak 0.1-0.2 s after the beat (c54: on the beat), same height |
| 53-60 | celli crescendos 180-184 and 188-196 now rise (+1.0 / +2.5, were -1.4 / +0.5); bar-to-bar rise unchanged | bar 59 -0.9 |
| 61-64 | | bar 62 first half -1.3 / -1.5 (the ff sags 3 dB and comes back); the sf of bar 63 is 3.6 dB lower and under the bar before it; Violins II's tremolo rises 10 dB inside the printed diminuendo; Trombone 1 margin over the strings 11.2 -> 6.8 dB (finding 2) |
| 65-70 | Horn 1 margin 7.6 -> 8.6 dB | the printed down-bow at 223 is a 6 dB drop (master dip 0.9 -> 6.4 dB); basses' re-bow 225.2 master dip 4.4 -> 7.3 |
| 71-78 | Violins I crescendo 261-262 +1.0 -> +4.0 | bars 71 and 73 +3.2 / +2.7: basses' A flat 1 +7.7 dB, celli +5.4; 56-112 Hz share of bars 71-74 -11.6 -> -7.4 dB; the basses (-38.0) are louder than each violin section (-42.3 / -42.8) under a pp theme |
| 79-82 | within 0.3 dB per bar | Violins II's crescendo 250-254 reversed (-1.2) |
| 83-92 | | timpani answer: three strokes at -34.9 / -45.0 / -46.0 (c54 -38.9 / -38.5 / -39.7); Clarinet 1 bars 86-88 -3.2 to -5.0, margin over the cor anglais 6.4 -> 2.2 dB; master hole at 289 5.6 -> 7.5 dB; bar 92 +3.1; re-bow dips (finding 3) |

Printed hairpins on the stems (114 crescendos, 115 diminuendos that sound at both ends): median change +4.4 -> +4.8 dB and -5.4 -> -5.1 dB; reversed 4 -> 8 and 5 -> 8; crescendos whose arrival note is under their start 8 -> 15. Thirteen hairpins on a track within 12 dB of the master got worse by 2 dB or more and now move under 1.5 dB the right way (Horn 1 32-34, Oboe 1 45-47, Violins I 69-72 and 78-82, Violins II 78-82, 87-89, 250-254, 254-255, Violoncellos 74-77, Cor anglais 124-128 and 131-136, Clarinet 1 256-259, Flute 1 261-262); four got better.

References. The delivered LRA (15.4 LU) is inside the 14-16 LU target of `loop/DYNAMICS-RESEARCH.md`; the climax is 5.8 dB over the ff cadence (bar 61 -12.9, bar 79 -18.7), unchanged. I did not re-measure a recording: only the Dvořák mp3 is on disk and the Brahms figures are stored shares.

### 2. Dan's standing notes on c55

- Themes in time and not choppy: S within 25 / 60 ms 613 / 709 of 727 (640 / 711). The 27 lost readings are level steps at the beat that the envelope no longer makes, not moved notes (no note-on changed). Choppiness now comes from level, not timing: note-to-note steps of 5-13 dB on Horn 1 bars 9-13, Flute 1 bars 43-44, Bass clarinet bar 35.
- S1: 49 repeats, median stem dip 8.6 dB (7.4), six under 3 dB in their own band (five): Contrabassoon 265 (0.0), Double basses 168 (0.0) and 144 (1.6), Bass clarinet 265 (1.9), Violins II 289 (2.4), Violins II div 120 (2.6).
- S2: the fp of bar 47 peaks at qn 148.1-148.2 on the master (c54 147.9-148.0).
- S3: no cut tail found. The hall is a post-fader return since c44, so neither the envelope nor CC7 cuts it. Fastest fall left in the envelope under a sounding note: 5.9 dB in 0.25 s (timpani roll settle at 262).
- Wet and mushy: the mix did not change. Strings' drop 0.3 s after a stop 15.9 -> 16.4 dB (minimum 10.0 -> 12.8), side/mid -5.7 -> -5.9 dB, correlation under 250 Hz 0.69 -> 0.72, 315-500 Hz against 1 kHz in bars 7-30 +6.6 -> +5.8 dB. The 2-4 kHz share of bars 7-30 fell 2.2 dB (-8.9 -> -11.1); the likely cause is that the removed fills sat on note starts (inferred).
- Per-note automation: none is written. 2,572 points; 28 notes still carry an unmarked move of 2 dB or more inside 0.25 s (finding 6).

### 3. The envelope against the reference projects

| project | tracks with a volume envelope | points per second per track | median gap between points | median step |
|---|---|---|---|---|
| EW Hollywood Orchestra template, EW ComposerCloud+ template | 0 of 59, 0 of 86 | | | |
| Duc, Mahler Adagietto (572 s) | 11 of 39 | 0.01-0.21 (strings 0.07-0.21) | 0.8-5.9 s | 0.5-1.9 dB |
| Duc, LOTR (152 s) | 15 of 222 | 0.02-0.12 | 1.3-64 s | 0-2.5 dB |
| movement II c55 | 32 of 32 | 0.06-0.66 (strings 0.44-0.66, winds 0.06-0.34, brass 0.06-0.25) | 0.33-1.15 s | 0.3-0.9 dB (timpani 1.7) |
| movement II c54 | 32 of 32 | strings 4.8-7.1 | | |

The strings are now 2-3 times Duc's densest track instead of 23-700 times. Duc's rides span -13 to +7 dB on one track, so a slow ride of that size is reference practice. What remains here is roles over three or more notes (383 items), hairpin gains (207), slow rows (226, of them 111 section rows), the final fade and the timpani roll rules. The gap to Duc is mostly ramps written as several points: our median step is 0.3-0.9 dB at 0.35-0.6 s. In the references the note-level shape is in the controllers: 7-13 CC1 points per second on every sustained line in EastWest's own MIDI, full 0-127 range, through the "Mod + Expression Combo" macro that moves CC11 and CC1 together (EW-TEMPLATE-FINDINGS lines 51, 81).

### 4. CC11 / CC1 lanes: resting level, headroom, slope, and lowering the resting CC

CC11 while sounding (5th percentile / median / 95th / maximum) and at the two ff passages (qn 204-212, 262-268):

| family | CC11 | at ff | share of sounding time at 106 or more | CC1 (5th / median / 95th) |
|---|---|---|---|---|
| Violins I | 22 / 61 / 120 / 126 | 118 | 13 % | 38 / 90 / 105 |
| Violins II, violas, celli, basses | 21-25 / 37-46 / 114-116 / 122 | 116-119 | 8-9 % | 20-38 / 45-54 / 98-105 |
| Flute 1, Oboe 1 | 34-44 / 68-71 / 122 / 122 | 118-119 | 26-28 % | 70-83 / 100 / 110 |
| clarinets, bass clarinet, bassoons, cor anglais | 22-36 / 34-56 / 115-122 / 118-122 | 115-118 | 10-24 % | by instrument |
| Horns 1-2 | 39-47 / 56-58 / 122 / 122 | 120-121 | 13 % / 46 % | 60-64 / 66-68 / 108 |
| Horns 3-4, Trombone 2, Bass trombone, Tuba, Horns a2 | 22-42 / 35-93 / 91-96 / 96-102 | 88-95 | 0 % | to 86 |
| Trombone 1 | 46 / 114 / 116 / 119 | (quotation 114) | 72 % | 42 / 108 / 108 |

Slope inside single notes on the c55 stems (stem minus the written envelope against the CC11 lane; notes of 1.3 s or more whose CC11 moves 6 or more; CC1 moves with it):

| CC11 centre | strings | winds | brass |
|---|---|---|---|
| 20-40 | 0.61 dB per unit (n 13) | 0.35 (10) | 0.37 (5) |
| 40-60 | 0.62 (10) | 0.30 (10) | 0.34 (4) |
| 60-80 | 0.47 (8) | 0.25 (12) | 0.42 (9) |
| 80-100 | 0.24 (2) | 0.21 (3) | 0.21 (6) |
| 100-128 | 0.33 (1) | 0.15 (11) | 0.41 (1) |

The 2-5 kHz share moves with CC11 inside a note by -0.1 to +0.1 dB per unit on strings and winds at every range (brass +0.40 at CC 60-80), so a CC11 move of 6-10 units inside a note is a level change of 2-6 dB at soft dynamics with a brightness change under 1 dB (measured; within-note, so the layer crossfade is included).

Lowering the resting CC with a slow trim making up the level:
- It is not needed movement-wide here. Movement II prints two accents (Trombone 1 213, 218) and one sf chord (212, seven parts); the finale's case (accents at ff on every page) does not exist. At ff the strings and upper winds rest at 115-121: 6-12 units of headroom at 0.15-0.33 dB per unit, 1-3 dB.
- It is safe locally: lowering 118 -> 108 costs 1.5-3.3 dB of level and under 1 dB of 2-5 kHz share by the slopes above. Use it only on the bar before a printed accent or sf (finding 2 uses a row volume and a CC11 fall instead, which leaves bars 61-62 as they are).
- The useful end is the soft one: strings rest at CC11 22-37 in the coda, the niente and the introduction, where one unit is 0.6 dB. A lift of 6-8 units over the first 0.3-0.5 s of a new bow is +3.6 to +4.8 dB with no fader move; that is the size of the re-bow fills that were removed (median stem dip 2.9 -> 7.8 dB).
- Brass that carry the theme (Horn 1, Trombone 1) sit at CC1 108 / CC11 114-121 in the loud bars with no headroom; Horns 3-4 and the low brass have 25-35 units.

### 5. Wetness and bass after the `loud_eq` change

56-112 Hz share of the master (third-octave bands 63-100 Hz), c54 -> c55: whole -12.1 -> -10.7; bars 53-60 -11.0 -> -9.8; 61-62 -12.9 -> -11.4; 79-81 -11.5 -> -9.4; coda -7.3 -> -7.6; bars 37-52 -9.0 both. These are the intended gain of the shelf. Bars 71-74 are different: -11.6 -> -7.4 dB, 4.2 dB in a pp passage where the shelf row (from qn 254) does not act. The cause is the basses' A flat 1 (pitch 32, fundamental 52 Hz, second harmonic 104 Hz) without its -5 dB pitch trim: body +7.7 / +7.8 / +7.8 dB at 238, 244, 250 and +6.9 at 87. With those notes 5 dB lower (dry-stem estimate) bars 71-74 read -10.5 and bars 71-78 -11.2. So keep the `loud_eq`; the A flat 1 belongs in the patch (finding 1). The 80 Hz bell from bar 71 then needs a second look: with the pitch level corrected the passage is at -10.5, inside 1 dB of the tutti figure.

### 6. Still open from c54

- **Clarinet 1 289**: master hole 5.6 -> 7.5 dB (0.25 s wide, -41.5 to -49.0). Six parts re-articulate on that barline: Clarinet 1 (gap 48 ms, stem -47 to -52), Horn 3 (84 ms), Violins II (printed repeat, 125 ms, stem dip 9.8 dB), Violas div (83 ms, 12.7 dB), and the celli and basses change note. The clarinet alone would be a 3 dB hole. Fix on the note side: start Violins II's and Violas div's new bows 0.08 qn before the barline (`STR_REP_NEW_BOW` lead for 289, or `REATTACK_LEAD_AT` 289: 0.10 s) and cut their gap to 0.05 s, so the strings have spoken when the clarinet re-tongues; then the clarinet's "Leg Slur Rep" row test (c54 A #1) is worth its rebuild. Range pass bars 87-89.
- **Violins II 154**: crossover +242 ms, unchanged (the c54 lead is at its clamp). Level is fine (-48.8 against -49.8 / -48.7). No change proposed; left audible.
- **Violins II 47** (G4, pp, between two A flats): -56.9 against -44.4 and -47.5, 9.4-12.5 dB under (c54 3.2). The other four G4 notes of the track are within 1.7 dB of c54, so this is the join, not the pitch. CC11 35 -> 45 over 46.95-48.0 (slope 0.6 dB per unit: +5 to +6 dB), range pass bars 15-17; if it stays more than 5 dB under, `Leg BC MAX` for this one target.
- **Bassoon 1 262**: body +4.4 dB over c54 (-28.0 against -35.9 before and -37.2 after); pitch 61 on Sus MAX is +3.6 dB on all three notes (148, 206, 269). `region_gain_db` Bassoon 1 `pitch_db` {"61": -3.5} (finding 1; `pitch_trims.json` has -5 for it). Its S reading (+48 ms in c54) is A's.

## Findings

### 1. Lead-line phrase shapes: single notes 4-13 dB off because of their row or pitch; move the level into the Opus state (measured; offline for level, range pass to confirm)

Where and size (c55 stem bodies; c54 in brackets):
- Flute 1 136, bar 44, the pp last note of theme B (3 qn): -38.7 (-48.4), after -51.8 at 135 and -55.1 at 133.5. It is the only note of the track on "LegRep RRx4". Master bar 44 +3.3 dB; the bar no longer falls from bar 43 (-38.0 -> -38.5; c54 -38.4 -> -41.7).
- Horn 1 bars 9-13: 26 -43.7, 27 -41.4, 30 -42.5, 31.5 -37.0, 32 **-32.4**, 34 (mp, the printed top) -35.0, 35 **-42.6**, 36 -41.7, 37 -36.9, 37.5 -43.1, 38 -39.5. The crescendo 30-34 arrives 2.6 dB under the note before it; the diminuendo zigzags by 5-7 dB. All at CC11 46-57, CC1 64-68: sample level by pitch (`pitch_trims.json` Horn 1 has -5 for 65, +5 for 68, +3 for 56).
- Cor anglais 152, the first long note of the movement I quotation (A4, 3.5 qn, p): -37.9 (-42.8) after -45.7; 163 (A4) +3.4. Master bar 48 +3.0.
- Bass clarinet 102, bar 35 (4 qn after the breath, start of a decrescendo to pp): -37.6 (-41.4), the loudest note of bars 33-36. Its CC11 is 55 where the printed-dynamic curve is 42.
- Double basses A flat 1 at 87, 238, 244, 250: +6.9 to +7.8 dB; master bars 30, 71, 73 +3.2 / +3.2 / +2.7.
- Clarinet 1 coda: 283 / 286 / 289 at -47.7 / -46.7 / -46.6 (-44.5 / -41.7 / -42.6), 292 at -40.5 (-44.4); the three notes before the swell lost 3-5 dB, the swell's top gained 3.9.
- Horn 1 208 (F sharp 4, Sus MAX, ff): -33.1 between -25.1 and -27.6 (part of finding 2); Bassoon 1 pitch 51 -4.0 on six notes, pitch 61 +3.6 on three.

Control and data:
1. Port `region_gain` from `symphony/scherzo/reaper-v600/tools/build_reaper.py` (lines 355-398 and the call in `state_for`) into `tools/build_reaper.py`, with the scherzo's `PITCH_TRIM_IN_OPUS` switch in `tools/score_to_parts.py`. Row names must match without case (the scherzo's cor anglais A4 miss).
2. `build/mix.json` `region_gain_db`:
   - Flute 1: `{"row_db": {"LegRep RRx4": -9.5}}` (one note uses the row; expected body -48.2, master bar 44 about -41.5).
   - Every track in `build/pitch_trims.json` (14 tracks): its table as `pitch_db` on the rows it names (`_arts`, or all rows where `_all_arts` is set): Horn 1 {53: +2.5, 55: +2.5, 56: +3, 60: -2, 61: -2.5, 62: -3, 65: -5, 66: +4, 67: +2, 68: +5}, Cor anglais {61: +4, 65: +3, 66: +3, 69: -5}, Double basses "Sus MAX" {32: -5, 37: -2, 39: +4}, Clarinet 1 {68: +6, 70: -3, 79: -6, 80: +5}, Flute 1 as listed there, and so on. The `_skip_onsets` lists cannot be kept (a region volume acts on every note of the pitch): for Horn 1 that is 23, 32, 37.5, 39, 177.5, 182, 210, 230. Check those eight notes on the range pass; 32 is the note that now stands 3.4 dB over c54, so the -5 on pitch 65 is wanted there.
   - Bassoon 1 is covered by its own table there ({51: +6, 55: +4, 56: +5, 61: -5}); on c55 the two pitches read 4.0 dB low and 3.6 dB high, so start from +4 and -3.5 and fit on the pass.
3. `build/cell_rows_c55.json` must be refitted after this. The section rows were computed with the trims off and hold each section at its c54 mean; with the pitch levels back in the patch they would count twice (Horn 1 [172, 204, +2.4], Double basses, Flute 1 [108, 140, +2.2], Cor anglais [108, 140, +2.9] among them).
4. Not a pitch or row matter, so CC11 or a role of three notes:
   - Bass clarinet 102-105: bring the CC11 lane from 55 down to 45 at 102 (it sits 13 over the dynamic curve on this note only; slope 0.30 dB per unit: -3 dB). Find the rule that lifts it in `score_to_parts.py` (the lane reads 54 / 75 / 74 / 70 / 69 / 66 on the notes before, 8-12 over the curve, so it is the solo lift carried through the breath).
   - Clarinet 1 283-292: `roles.json` Clarinet 1 `[283, 292, 3.5]` (three onsets: 283, 286, 289), and the CC11 lane at 292-295 from 34 to 28 (the Clarinet KS Master takes its layer from CC1, so CC11 is level only: -2 dB). Expected margin over the cor anglais in bars 87-88 about 5.5 dB (inferred; 2.2 now, 6.4 in c54).

Expected: master bars 11, 30, 35, 44, 48, 71, 73 within 1 dB of c54; Horn 1 32 -> 34 rising again; bass share of bars 71-74 about -10.5 dB.

Verification. Offline: a region or row volume is a gain on that note before the hall return, so simulate it as c55 stem times the per-note gain (the same arithmetic as `tools/stem_fix.py`), then rerun `hp.py`-style hairpin figures and the per-bar master. Range pass: bars 7-14 (Horn 1: the scherzo found legato-joined horn notes 2-5 dB under the region target), bars 41-48 (flute, cor anglais), bars 71-75 (basses). If the horn's joined notes miss, the remaining step is CC1 on the horn (its dynamic control), fitted on that pass.

### 2. Bars 62-64: the ff sags, the sf is a hole, and the tremolo swells inside the printed diminuendo because the c31 CC7 lanes lost their envelope half (measured; CC7 and rows offline, the sf by range pass)

Evidence, master per quarter 204-213, c54 / c55: -13.8 / -12.8, -13.5 / -12.9, -13.7 / -12.9, -13.3 / -13.1, **-14.5 / -15.8, -14.9 / -16.4**, -14.2 / -13.8, -14.8 / -14.5, **-17.5 / -19.9**. "ff molto sostenuto" spans 1.6 dB in c54 and 3.6 dB in c55.
- The sag at 208-210: Violins I play the F6 at 208 on "Leg Slur MAX" at -28.0 between Sus MAX notes at -20.6 and -23.5; Horn 1's F sharp 4 at -33.1 / -31.4 between -25.1 and -27.6 (pitch 66 on Sus MAX, -4.9 dB on both of its notes); celli -3.1, Bassoon 2 -3.2.
- The sf at 212.0-212.3: master -14.3 -> -17.9. Violins I -20.7 -> -27.6 (their tremolo chord E6 / A6 at CC11 122 is 3-5 dB under their Sus MAX at CC11 120-126; Violins II, violas and celli rise 1-4 dB into their tremolo, so only Violins I's row is weak), basses' pizzicato -22.1 -> -25.9, Flute 1 -27.3 -> -32.1, Bass trombone -25.4 -> -30.3. In c54 the bar 63 downbeat was level with bar 62 (+0.5 dB); now it is 3.5 dB under it.
- After the sf, with CC7 at 19-56 on Violins I, Violins II and violas returning to 127 over 213-214.5 (`score_config.py`, the c31 block that reads `cycles/c31/a2cc7.py`, comment "recompute if roles or shapes here change"): Violins II -35.7 at 212.75, -39.7 at 213.25, then **-31.8, -29.2** at 214.25 and 214.75 (c54 -39.0 / -39.0): a 10 dB rise inside sf > p, 3 dB under Trombone 1 (-26.0). Violins I -41.1 -> -36.1 (c54 flat at -36.8 / -37.2), violas -43.4 -> -39.3. Trombone 1's margin over strings and bass trombone 11.2 -> 6.8 dB.

Fix:
1. Remove the bar 63 CC7 points on Violins I, Violins II, Violas and Violoncellos (the `_d['cc7']` block near line 590 of `build/score_config.py` and the Violins I edit at line 704). The hall is post-fader since c44, so the reason for the lanes (S3) is gone.
2. Split the [204, 220] section rows at 212 in `build/cell_rows_c55.json` so the two tremolo bars have their own level (four onsets on Violins II: 212, 216, 218, 219). With the CC7 lanes divided out, c54 minus c55 over 212.5-218 is -1.1 dB (Violins I), **-11.1** (Violins II), -1.4 (violas), -3.3 (celli) relative to the present envelope. Three of these equal the present [204, 220] rows (+1.1, +1.4, +3.3), so the tremolo bars need no section row on those tracks: Violins I `[204, 212, 1.1]`, Violas `[204, 212, 1.4]`, Violoncellos `[204, 212, 3.3]`, nothing over 212-220; Violins II `[204, 212, 3.6]`, `[212, 220, -7.5]`. Offline check (CC7 is linear amplitude: stem times 127 / CC7, times the row change): no string stem rises more than 1 dB between 212.5 and 216; Trombone 1 margin 10 dB or more.
3. The sf, on the instrument: Violins I `region_gain_db` `{"row_db": {"Tremolo": 5}}` (on Violins I the row is used by this passage only). Take the 5 dB back after the spike in the CC11 lane, not in the envelope: the lane reaches 96 at 212.5 and 70 at 213.75 instead of 111 and 86 (0.24-0.33 dB per unit at this range, fit on the pass). Double basses' pizzicato at 212: velocity 98 -> 118 (about +3 dB at 0.15 dB per step). Bass trombone CC11 94 -> 106 over 212.0-212.5 (brass 0.2-0.4 dB per unit: about +3 dB; stay under 108 for BRIEF item 9). Expected master at 212.0-212.3 about -15 dB, level with bar 62 (inferred). Range pass bars 61-64.
4. The sag: Horn 1 `pitch_db` {66: +4} from finding 1 covers 208; for Violins I either keep 208 on Sus MAX (drop the keyswitch pair at 207.676 / 209.916: a bow per note is what "molto sostenuto" at ff asks for) or `row_dyn_db` {"Leg Slur MAX": {"ff": 5}}, which also changes bars 59-60 and 79-81 and needs their check. I prefer the first; range pass.

### 3. Re-bows of held soft notes: master dips of 6 dB or more at 11 re-bows (c54: 1); the niente and the morendo lose their shape (measured; range pass)

All 85 re-bows, stem dip median 2.9 -> 7.8 dB; master dip of 3 dB or more 24 -> 37, of 6 dB or more 1 -> 11. Worst on the master: Violins II div 119 (bar 39) 8.0; 289 (bar 88) 7.5; basses 225.2 (bar 66) 7.3; Violins II 295.8 (bar 90) 7.1; basses 278.35 6.9; violas 283 6.7; Violins II 144 6.6; the three sections at 223 6.4; Violins II 303.4 (inside the final chord) 5.9.
- Bar 66. The printed down-bow at 223 on the tied note starts the diminuendo to niente. Strings together per half beat from 221.5: -43.7, -41.9, -42.0, then **-48.0** at 223, -46.9, -47.4, -48.1, -53.4, -59.9 (c54 -45.5, -43.9, -43.6, -42.5, -44.6, -47.2, -48.8, -54.7). The down-bow is a 6 dB drop and the next beat and a half is flat. Violins II also rise 4.4 dB through bar 65 on a held pp note (-48.4 to -44.0) before dropping 7.6 dB.
- Bars 91-92. The master across the morendo and the final chord every half second from qn 298: -43.2, -43.6, -44.6, -46.1, **-44.6**, -46.2, -48.2, **-46.3**, -48.5, -49.3, **-47.4**, -47.8, -46.9, -48.6, -48.0, -47.8, -48.6, -50.0, -51.6, -53.3. Three bumps of 1.5-2 dB (basses' new bows at 299.8 and 302.0: stem +4 to +6 dB at the start) and a final chord that is flat for 4 s, 3 dB over c54. The fall from bar 90 to the chord is 5.3 dB (c54 7.5).

Fix, all CC11 or note timing (A decides the bow option per place; these are the dynamics-side values):
- New bows at CC11 22-37 start slowly and 5-8 dB under the old bow. Give each soft re-bow piece a CC11 lift of +7 at its note-on, back to the lane over 0.45 s (+4.2 dB at 0.6 dB per unit), and let the old piece's lane fall 4 units over its last 0.15 s. In `score_to_parts.py` this is a new option beside `STR_REP_NEW_BOW["soft_fall"]`, e.g. `REBOW_CC_LIFT = {"cc": 7, "s": 0.45, "max_cc": DYN["p"]}`. Expected stem dip median about 4 dB; master dips of 6 dB or more 11 -> 3 or fewer (inferred from the slope).
- 223: the down-bow should start the diminuendo from above: CC11 36 -> 43 at 223.0, falling through 36 at 223.75 to the existing lane (33 at 223.19 becomes 41). Violins II bar 65: CC11 36 -> 30 linearly over 220.5-222.9 to cancel the 4.4 dB bloom.
- Basses 299.8 / 302.0 / 303.3: no lift on these three (they bump); instead start each at CC11 3 under the lane for 0.3 s.
- Morendo: let CC11 do the fall on all five string sections: the lane now reads 33 at 298.3 and 22 at 301; make it 33 -> 18 by 301 and hold 18 to 303.5 (9 dB instead of 6.6 by the slope), which also brings the chord back to its c54 level without a row.
- Do not put the re-bows of two sections on the same point where the master is thin: 289 (finding "open items") and 223 are printed and stay; 295.8 (Violins II) and 295.3 (Violas div) are 0.5 qn apart and both dip 7-12 dB: move Violas div's to 294.6 in `REBOW_AT`.
Verify on a range pass of bars 65-66 and 88-92 with `rebow_c55_fix.txt`'s measure and the half-second master table above.

### 4. Timpani answer, bars 84-85: one stroke 10 dB over the other two (measured; range pass, timpani only)

E flat - C - A flat at pp (277, 278.5, 279). Stem peaks -34.9, -45.0, -46.0 dB (c54 -38.9, -38.5, -39.7). Velocities 88, 60, 60 (c54 56, 60, 60 with a fader lift on the first), and the coda section row of -6.4 dB lowers all three. The second and third strokes are at the level of the strings (-46) and the timpani's share of 30-150 Hz in bars 84-85 fell 16.2 -> 4.4 %; margin over the soft strings -11.1 -> -15.9 dB.

Fix: `score_config.py` timpani velocities 277: 88 -> 72, 278.5 and 279: 60 -> 72 (0.2-0.3 dB per step, and all three on the same stick layer; the top layer starts between 96 and 111); delete the Timpani `[274, 304, -6.4]` row in `cell_rows_c55.json` and refit it on the pass. If E flat 3 still reads under the others at equal velocity, correct it as a region volume on pitch 51 of "Timpani Flt Lng", not by velocity. Pass: three peaks within 2 dB, 6-9 dB over the strings' sum.

### 5. Hairpin tops and soft notes: use the CC11 lane, which has the slope for it (measured; range pass)

- Violins I and II, bars 23 and 27: the long notes at the top of the two crescendos sit 4-5 dB under the notes around them. 78-82: -35.2, -33.7, **-38.4** (F5, 2 qn, CC11 77-85), -32.2 (the f). 68: -38.9 between -39.7 and -39.2 where c54 had -34.2. Other F5 and E flat 5 notes of both sections are within 0.7 dB of c54, so it is not the pitch: c54 lifted these notes with the phrase-top layer. At CC11 60-80 the strings give 0.47 dB per unit. Fix: express the phrase top in the lane, `score_to_parts.py` phrase-top rule writing CC11 instead of dB (`PT_CC_PER_ST`, 9 units for these two notes: 80 -> 86-94 across the F5 instead of 77-85, 68 the same), and remove the CC11 drop to 72 at 81.0 inside the note.
- The same lane move answers Violins II 47 (open items) and the soft starts A counts: at CC11 under 60 a lift of 6-8 units over the first 0.3 s is 3.6-5 dB.
- No movement-wide lowering of the ff resting CC (slot C part 4).
Verify on a range pass of bars 23-28: crescendo 78-82 at least +3 dB to the F5 and +5 to the f.

### 6. Leftover edges inside notes, section rows, delivery span (measured; offline)

- 28 notes carry an unmarked envelope move of 2 dB or more within 0.25 s while sounding. They are role and section-row edges keyed to the score onset under a note that starts earlier, or a row edge on a bar line under a held note: Horn 3 204 (+4.5 dB at 204.01, note-on 203.95), Violas and Violas div at 291.9 (+4.3, section edge at 292 under notes from 291.7 / 291.83), Violins II 292.4 (+3.8), Violins II 107.8 (-4.0), Double basses 220.05 (+3.6), Oboe 2 210.15 (-3.6), Violoncellos 292.04 (-3.5), Clarinet 1 262.05 (-3.4), Horn 1 204.05 (-3.2), and five brass parts at 211.67 (-2.3 to -3.5 inside the last ff chord: the end of the `_all` climax row). Fix in `score_to_parts.py`: key a role or section-row edge to the led note-on of the first note it covers, and where a note sounds across the edge, ramp over the whole note or move the edge to the next rest (Scherzo c16 item 3). End the `_all` climax row at 212.0 with its ramp inside 212.0-212.5, after the chord.
- Delivery span 19.06 dB (limit 19). The fixes of findings 1 (Clarinet 1 bars 86-88) and 3 raise the 10th percentile; bar 61 is +0.6 dB over c54. After the section rows are refitted, set `LEVEL_SHAPES["_all"]` climax row from -0.4 to -1.0 if the span is still over 18.8.
- Simulate all of this on the c55 stems before the lock (stem times new minus old envelope).

## Do not touch

The removal itself (2,572 points, no per-note layer). The basses' `loud_eq` shelf (the tutti shares are where c55-C5 wanted them). Bars 53-61 (the crescendo rises every bar: -35.2, -29.7, -29.1, -25.6, -27.3, -22.9, -21.6, -16.8, -12.9, with the printed restart at bar 57). The climax over the cadence by 5.8 dB. The fp spike of bar 47 on CC11 (height unchanged). The hall settings and the post-fader return. The viola pizzicato velocity fit of bars 41-44. The printed re-articulations at 223 and 289 (shape them, do not remove them). The timpani roll rules.

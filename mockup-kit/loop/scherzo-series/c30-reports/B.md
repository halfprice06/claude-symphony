# Cycle 30, critic B (balance and levels), on the c29 render

How I measured. Levels are K-weighted (the BS.1770 shelf and high-pass applied with ffmpeg, energy mean over the span, channels averaged), taken from the c29 stems (`cycles/c29/render`), the c29 master and the delivered c29 mp3. "Against c18" means the c29 value minus the c18 value plus 3 dB, to allow for the c26 global -3 dB. Inner lines come from `cycles/c23/actor_scripts/inner23.py` (best band, line against all other stems plus the returns), run on 50 marked passages. Per-bar comparisons on the mp3 are c29 against c28; c28's stems are deleted, so stem comparisons go back to c18. Scratch scripts are in my scratch folder, deleted after this report.

## Manual notes

`loop/MANUAL-READING.md` has no row for c30, so I did not do the page reading. I used `loop/MANUAL-GAPS.md`, plus the page that explains finding 1.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Channel Routing: STEREO outputs the channels as recorded; MONO FROM LEFT discards the right channel (May 2021 manual, PDF p.141, printed p.140) | Horn 3 changed from Mono From Left (c18-c28) to Stereo in c29 | Yes, but the per-pitch region gains were fitted on the left channel alone. The E4 regions now play 4-5 dB hot against Horn 3's other pitches (finding 1). Horn 1, the same patch on the default routing and unchanged since c18, shows no such step: E4 -0.4 dB against c18, other pitches within 0.2 dB |
| Stereo Double needs STEREO as the master channel source (p.141) | Horn 3 is on Stereo now, so `stereo_double` is open to it. Countermelody correlation is 0.97 | Not used. Width is not a level fault, so I do not rank it |
| MANUAL-GAPS #10: horn and trombone portato rows for the tutti tenutos | Hn 3-4 and trombones, 312-360 | Not used. c28 and c29 rejected Portato, Marc Lng and Sus Accent by range test. No new data from me |
| MANUAL-GAPS #13: Mid instead of Close on the winds and horns | the trio's horns, the countermelody | Not used. Not needed for balance: the trio tune and the countermelody's level faults are region and envelope faults (findings 1-2) |

## Findings, ranked by what a listener would hear

### 1. Horn 3's E4 is 4-8 dB hot since the Stereo routing. In the ff tuttis the countermelody's top note rises over Violins I's theme, and the line's head sounds weak beside it (measured)

**Where.** Horn 3, every E4 (pitch 64): the tutti countermelody at 317, 350, 917, 950 (bars 106-107, 117-118, 306-307, 317-318); the trio at 509, 522, 600, 603; bar 300 at 897; the coda build at 992 and 996.

**Evidence: per note against c18** (first 1 qn of each note, after the onset).
- E4, 14 notes: median **+4.1 dB**, and 317 +4.7, 600 +4.6, 917 +4.7, 950 +6.1, 897 +7.7, 992 +8.4.
- Every other pitch, 1-35 notes each: median between -1.9 and +0.3 dB.
- The B3 at 320 / 920, which follows the E4 by legato, is +6.1 dB. It plays the E4's transition sample.
- Controls are identical in c28 and c29 at 313-322: CC1 108, CC11 114, no CC7, vol_db 7.01. The step comes from the samples, through the routing.

**Evidence: in the tutti** (K-weighted, per note or per bar).
- Horn 3's E4 at 317 is -29.6 dB against Violins I -32.7. The B3 at 320 is -26.2 against -27.5.
- In bar 107, Horn 3 is -25.0 dB: 4.7 dB over Violins I (-29.7) and 5.6 dB over the celli (-30.6), which carry the same line.
- The countermelody group (celli, Bsn 1, Hn 3, Hn 4) runs -30.0 in bar 105 and -23.7 in bar 107. That is the 6 dB head-to-body gap the c29 actor measured on the celli alone ("celli heads 5.3-5.7 dB under the body"). Most of the body's level is Horn 3's hot E4, not a weak celli head.
- inner23 has the theme's lead in its band at only +3.4 to +5.6 dB in bars 107 and 117. In the other bars it is +8 to +12.

**Mechanism.**
- `mix.json` Horn 3 `region_gain_db.pitch_db` has "64": -1.0, fitted under Mono From Left.
- c29's range test measured Stereo at +3.4 dB over 312-360 on average and set gain_db to -3.4. For E4 the routing change is about +8 dB, so after the -3.4 dB the E4 is still 4-5 dB hot. The other pitches ended about 1 dB under c18.

**Fix (Opus state, region volume; allowed by Dan's rule).**
- `build/mix.json` Horn 3: `region_gain_db.pitch_db["64"]` -1.0 -> **-5.0**. Horn 3 needs a full rebuild, as in c29.
- Optional, after the range test: if the countermelody's other notes stay about 1 dB under c18, raise gain_db -3.09 -> -2.4.
- The relay G sharp 4 at 1092 is unaffected (pitch 68 has its own region gain).

**Expected (simulated on the stems, E4 -5 dB).**

| | c29 | after the fix |
|---|---|---|
| Horn 3 in bar 107 | -25.0 | -29.7 |
| line body (bar 107) | -23.7 | -26.5 |
| line head-body gap, 312 | 6.3 dB | 3.5 dB |
| line head-body gap, 912 | 2.6 dB | 1.1 dB |

This closes most of the celli-head item without touching the celli.

**Range test.** Horn 3 alone, 312-360 and 1016-1106. Pass when:
- every E4 is within 1.5 dB of the B3 and A3 around it, as on c18;
- the line's head-body gap is 4 dB or less;
- the G sharp at 1092 is within 0.5 dB of c29.

### 2. Horn 3's notes at 350 and 353 get +4.8 dB envelope swells at their attacks. These are per-note volume moves, against Dan's rule (measured in parts.json; audibility inferred)

**Where.** Horn 3, score qn 349.25-350.5 and 352.25-353.5 (bar 117), and similar steps at 932.3-932.7 and 949.3-949.7.

**Evidence (`cycles/c29/build_render/parts.json`, Horn 3 `vol_db` / `vol_cls["slow"]`).**
- The envelope holds 5.01 dB from 331 to 349.25. It then rises to **9.78 at 349.716**: the E4's moved note-on is 349.736, so the rise falls in the last 0.1 s of the G3 before it.
- It falls to 6.77 by 350.5, which is 3 dB inside the E4's first 0.18 s.
- It rises again from 352.25 to 9.78 at 352.716, inside the E4's tail. It falls to 5.01 by 353.5, inside the A3's first 0.17 s.
- No hairpin is printed there (events tsv: Hn 3 has only the slur at 347 and the breath at 348). The class is "slow". My inference, which I have not traced through the build: these are `slow:uni_role` (Horn 3 has 6 uni_role items in `vol_tags`). The unison-boost role runs (`score_to_parts.py` about lines 6857-6890) split at the breath at 348, and the runs' edges land in note bodies.
- The actor's list counts only the net change ("Horn 3 350.0 1.2", "353.0 1.0", "933.0 1.2": 3 of the 32 net in-note moves). The swing inside the notes is 3-4.8 dB.
- Together with finding 1 it lands on the hot E4: Horn 3's E4 at 350 measures -28.5 dB against the line's other notes at -34 to -38.

**Fix (no new per-note move: make the a2 boost one span per tutti).**
- `tools/score_to_parts.py`: in the run merge (`n["qn"] - ub_runs_[-1][1] < 1.0`, line 6859), make the 1.0 a generic parameter `UNI_RUN_GAP_QN` (default 1.0).
- `build/score_config.py`: set it to 3.0 for the scherzo, so the breath at 348 / 948 does not split the Hn 3 / Hn 4 unison run.
- If the 348 G3 is not in `UNI_BOOST` (it is v73, and probably not a matched unison), the merged run must still cover it. The simplest form is a roles.json passage row for Horn 3, [311.5, 360, +5.0] and [911.5, 960, +5.0], with UNI_BOOST off for Horn 3 inside those windows.
- Check (a parts.json-only run, no REAPER): Horn 3's `vol_cls["slow"]` changes by less than 1 dB inside every note body in 312-360 and 912-960, outside the printed hairpins 329-331 and 929-931. The guard's net-move count drops by 3.

### 3. The reprise fugato's subject (celli, bars 289-292) plays 3 dB under the same printed p subject at bars 57-60. Its slurred held notes have CC11 9 lower, and these are the softest bars of the mp3 outside the G.P. and the bars before the coda (measured)

**Where.** Violoncellos qn 866.4-870 (the accented slurred B flat 3-A3-G sharp 3 of the subject), against 170.4-174.

**Evidence.**
- The notes, velocities, rows, leads and roles ([168, 180, +5] / [864, 876, +5]) are identical at the two places.
- The staccato notes match within 0.3 dB, except 864-866 (-1.3 to +2.1).
- The three slurred notes are **-5.1, -9.8 and -4.5 dB** under their exposition twins. CC11 is 49 -> 44 at 866.4-868 against 58 -> 52 at 170.4-172, so 9 CC lower. CC1, CC7 and vol_db are the same.
- The subject over 289-292: celli -44.5 dB against -41.6 at 57-60. On the mp3, -27.1 against -23.9.
- Bars 289-293 are among the ten softest bars of the mp3: -27.2 to -28.0 dB K-weighted per bar. Softer than every printed pp passage except bars 90 / 93 and 139-140.
- In the exposition, c17 lifted each entry's held note with CC11_ADD_SPANS (the violas at both 182.9 and 878.9). The celli entry never had a span, and the reprise CC11 baseline under it is lower. I could not trace where the 9 CC comes from in score_to_parts.
- This is the passage Dan's 11-17 note describes: a quiet contrapuntal line he has to turn the AirPods up to hear.

**Fix (CC11, instrument side; one phrase matched to its twin, not a per-note shape).**
- `build/score_config.py`: `CC11_ADD_SPANS["Violoncellos"] += [(866.3, 870.0, 9, 9)]`.
- If the actor finds the source of the lower baseline, fix it there instead.
- Check: celli 289-292 within 1 dB of 57-60, and the three held notes within 1.5 dB of 171 / 173 / 173.5.
- The violas' answer at 293-296 (-40.7 dB against -42.6 at 61-64) and Bsn 1 / Cl 1's pp downbeat marks are unchanged.

### 4. At the f / ff arrival of the 101-104 build, the brass as a family match the strings, through a held hairpin gain (measured; whether a listener notices is inferred)

**Print.** Trumpets, trombones and tuba crescendo pp -> f over 300-309. Strings f -> ff at 310, woodwinds p -> ff. The brass are printed a step under the strings at the arrival.

**Evidence, bar 104** (K-weighted sums).

| | level |
|---|---|
| trumpets + trombones + tuba | -24.9 |
| strings | -25.1 |
| Violins I | -32.4 |
| Trumpet 1 alone (its f B4) | -29.8 |

- In bar 101, the pp brass are already only 6.8 dB under the f strings (-35.0 against -28.2).
- c28 dropped the 309 / 310 crescendo gains on winds and strings (`drop_always`) but kept them on brass ("brass unchanged").
- Trombone 1, Bass trombone and Tuba hold +2 dB from the hairpin gain into bar 105 (vol_db 4.0 at 312, 2.1 at 315). Three of the 32 net in-note moves ("Trombone 1 309.0 1.2", "Bass trombone 309.0 1.4", "Tuba 309.0 1.3") come from this.

**Fix.**
- `build/score_config.py` (the c28 block, item 2): extend `drop_always` {309, 310} to the "brass" group for Trumpet 1-2, Trombone 1-2, Bass trombone and Tuba (not the horns). The brass crescendo is then made by CC1 / CC11 alone. Keep the low brass role [312, 360, +2].

**Expected (simulated).**
- Master bar 104 -0.3 dB; low brass -2 dB at the arrival; the three net moves gone.
- f -> ff loses about 0.05 LU (bar 104 is one of six ff passages). The 2.23 LU stays over 2.0.
- Arrival 105 (reversed, -0.5) moves by at most +0.2 dB, so this does not fix it.
- If the actor has time for only three items, skip this one.

### 5. The trio climax after c29's roles works. One bar left (measured)

**Per bar, 209-224 (dB).**

| bar | 209 | 210 | 211 | 212 | 213 | 214 | 215 | 216 |
|---|---|---|---|---|---|---|---|---|
| tune group over the celli | +8.3 | **+1.7** | +7.0 | +6.4 | +4.9 | +5.8 | +4.6 | +4.4 |
| tune group over the violas | +9.3 | +6.2 | +7.4 | +8.5 | +10.1 | +8.5 | +6.8 | +9.8 |

- inner23 on the tune: +12.4 to +16.2 dB in every window 624-672.
- At the f of 219 the violas are only 4.3-5.3 dB under the ff tune, which is one printed step, as written.
- Bar 210: the celli at -36.5 dB are louder than Violins I (-38.5). It is one bar of the slurred countermelody. Not worth a change in the last cycle.
- The 205-208 roll is now on felt (Timpani soft -43.6 dB, under the violas, celli and Horn 1). On the mp3, bar 208 is 1.1 dB under c28. The crescendo into 209 still rises 18.9 dB on the master.

### 6. Per bar and per passage on the mp3 against c28: the quiet passages lost 0.3 dB, theme A gained 0.4 (measured)

**Per bar.**
- mp3 c29 minus c28: median -0.30 dB.
- Over 1 dB: bar 365 -1.8 and bar 342 +1.5 (Horn 3's routing), bar 239 -1.1, 174 -1.1, 208 -1.1, 366 -1.0, 151 -1.0.

**Per passage (mp3, c29 against c28).**

| passage | change |
|---|---|
| intro, counterstatement, F major 73-88, link, trio (three sections), codetta, retransition, reprise, sub. p 277, solo, close | -0.3 to -0.6 dB |
| fugato 57-68 / 289-296 | -0.2 / -0.1 |
| Meno 341-348 | -0.2 |
| theme A 13-28 | **+0.4** (the passage row) |

- This is the cost of TOP_ABOVE -3. It runs against Dan's 11-17 AirPods note, though the spec's p10 (-21.0) still passes.
- No balance action from me beyond finding 3, which lifts the softest contrapuntal bars on the instrument side. The level of the quiet passages as a whole is C's call (the quiet lift in `deliver_master.py`).

## Balances checked that are right (measured)

| check | c29 |
|---|---|
| theme A, Violins I (inner23, bars 13-28) | +9.9 to +16.8 dB; reprise 253-268 +7.9 to +16.0 |
| counterstatement calls, Fl 1 + Ob 1 (29-36) | +12.2 / +8.6 / +4.7 / +4.2. From 37 the winds join the violins in unison, so "under" there is unison, not masking |
| second idea, 45-56 | the tune in three octaves +6.6 to +12.0 dB; the violas + cor anglais lower octave +1.2 to +4.3 (-3.6 / -3.8 in bars 48 / 50) |
| after the sub. p of 121 | Violins I -37.9 against the accompaniment -48 to -50 (+10 dB); inner23 +18.7 |
| after the sub. p of 277 | Fl 1 / Ob 1 -38.9 / -42.3 against every accompanying stem -49 to -57 (+7 to +10 dB) |
| trio Clarinet 1 (153-168) | +8.9 to +16.5 dB; harp -49 to -58, horns' drone -51 to -55 |
| trio celli (169-184) | +6.2 to +13.6 dB; bar 183 +3.3 (phrase end) |
| Violins I an octave above (177-184) | +10.1 to +14.5 dB |
| Oboe 1 at 185 | +10.4 / +14.2 dB |
| codetta Oboe 1 (225-228) | 6.3-9.5 dB over the next stem |
| solo violin with Flute 1 (349-356) | +12.8 to +15.0 dB over Violins II "la metà" and the violas div. |
| Hn 1 motto tail (357-360) | +12.4 / +13.9 dB |
| Hn 1's last G sharp (371-376) | +16.8 to +22.8 dB |
| trumpets' repeated quarters (105-120) | Trumpet 1 2-5 dB under Violins I on its bars; present, not on top |
| timpani (105-120) | -32 to -55 dB per bar against Violins I -29.5 to -31.6 |
| low brass (105-120) | tuba -38.3 to -42.8 dB against Violins I -29.5 to -31.6 |
| summit (333-338) | strings -15.7 to -24.3 dB, woodwinds -17.1 to -23.6, horns -25.3 to -27.8, trumpets / trombones -25.0 to -27.8. Brass 8-10 dB under the fff at 336-338, as printed |
| coda timpani roll (336) | -33.3 dB, under every family |
| fugato 57-72 / 289-296 internal balance | each entry leads its band by +4.1 to +26 dB |

## Do not touch

- Horn 3's Stereo routing, mics and pan, and the G sharp 4 region gain (the relay at 1092 matches Horn 1). Finding 1 changes only the E4 region.
- The trio climax roles (celli -3.5, violas / Violas div -3.0) and the trio hold.
- The Violins I theme A passage row, the reprise CC7 span, and the delivery chain (TOP_ABOVE -3, ride rows, room bed).
- The solo violin / Flute 1 / Violins II balance at 349-356; Hn 1's motto and last G sharp.
- The trumpets, low brass and timpani under the tutti theme. The summit's brass at 8-10 dB under the fff.
- The felt timpani alias and its windows.
- The -3 dB global gain and the post-fader hall sends.
- The c26 woodwind figure state and Dan's bar-23 figure. None of the fixes above touches the figure's tracks or windows.

For a safe last render, do findings 1 and 2 together (Horn 3: one rebuild plus a parts.json change), then finding 3 (one CC11 span, `--midi-only` on the celli). Finding 4 is optional.

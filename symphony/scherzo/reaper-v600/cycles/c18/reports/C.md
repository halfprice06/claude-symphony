# Cycle 18, critic C: dynamics over time (lens C2), on the c17 render

Sources: `cycles/c17/render/` (master, 31 stems, 4 returns), `cycles/c17/scherzo-mockup-c17.mp3`, `cycles/c17/build_render/parts.json` (the data as rendered; `build/` equals it after the Horn 1 stem fix), `build/score_config.py`, `build/mix.json`, `build/mockup-events.tsv`, `cycles/c17/CHANGES.md` and `records/`, the c16 / c15 / c13 renders for comparison. Levels are K-weighted mean-square dB over the stated span (master), or plain mean-square dB of the channel powers (stems), on each cycle's own tempo map. "Momentary" = 0.4 s window, "short-term" = 3 s window, both K-weighted. Bar b starts at qn 3(b-1). "Measured" = a number from the render or the data; "inferred" = reasoned, not tested.

## Manual notes (cycle 18, slot C: group D2, May 2021 HO manual PDF pp. 101-102, read in full; MANUAL-GAPS.md read)

| PDF page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.101, "Sustain" | Brass sustain dynamics are on the Mod Wheel (CC1); all 4 layers play at once and CC1 crossfades them, so a crescendo inside a held note is a CC1 move, not velocity. | The brass crescendos into the tuttis: 300-309 (bars 101-103), 990/993-996 (the coda build), 618-621. | Yes (measured). `CC1_DYN_TRACKS` on: CC1 28 -> 86 (trumpets, trombones, tuba) and 64 -> 86 / 108 (horns) across 300-309; stems rise +7.7 (Horn 1) to +22.6 dB (Trumpet 1). At 993-996 the same: +8.3 to +15.6 dB. |
| p.101, "Sustain Accent" | Velocity sets the loudness of a separate accent attack; CC1 the sustain. | Brass accents. | Not used, correctly: the score prints no brass accents (the summit keeps them off the brass, BRIEF item 9). |
| p.101, "Sustain Marcato" | Velocity sets a low-pass cut-off on the marcato attack (harder = brighter). | Would apply to a brass marcato. | Not used; none printed. |
| p.101, "Legato Repetitions" | Retongued repeats inside a legato phrase (also used by the Leg Slur Rep patches). | Horn repeats (A's lens). | Not used (MANUAL-GAPS #2, c11 note). No dynamics consequence found. |
| p.102, brass staccato | At the highest velocity Hollywood Brass staccatos add overblown, rougher harmonics. | Trumpets' repeated quarters, bars 101-120 ("StacSs DblTng RRx9"). | Yes (measured): trumpet staccato velocities 58-96, never the top, so no overblow (Dan's "weight, not bite"). |
| p.102, shorts | Short articulations have no release trails; play staccato phrases with connected MIDI notes so the room sounds in the gaps, and hold the last note of a phrase long enough to ring. | The theme head's quarters and eighths before rests; the hall's ring at the subitos and the G.P. | Yes (measured in parts.json): theme-head staccato quarters are written 0.5 qn and eighths 0.25 qn (full slot); the G.P. after bar 339 rings (master -23.8 at the bar line, -37.9 at +0.3 s, -48.2 at +0.6 s). |
| p.102, Shorts MOD SPEED | CC1 moves through Staccatissimo / Staccato / Marcato Short / Marcato Long / Marcato Long + Sus. | Could shape a brass short crescendo. | Not used; no need found. |

MANUAL-GAPS #7 (recorded crescendo rolls): still not needed. The three printed roll crescendos grow as printed (below).

## Checks the cycle note asked for (measured)

- **Delivered LRA 14.9 -> 14.3 and master -1.1 LUFS: flatter or quieter?** Neither, mostly. The delivered loudness-range low point rose (-29.6 -> -29.0 LUFS) while the high point stayed (-14.8 -> -14.6): the master's loud passages fell about 1 dB, so the constant delivery gain rose about 1 dB and the limiter did less (2.4 -> 1.6 dB). Delivered per section against c16: 27 of 33 sections +0.0 to +1.2 dB (soft passages a little easier to hear); the summit -0.2 (short-term max -12.6, unchanged); the two crescendos into bars 72 and 300 -1.1 and -2.1. Delivered span p10-to-max 20.2 -> 19.4 dB (target 16-19). What a listener loses is not loudness but distinction at the top: the climaxes stand less far above what precedes them (findings 1 and 2).
- **Hairpins with 59 gains in CC11.** Stem audit of every hairpin of 2 qn or more (first note's body against the arrival note's): 245 crescendos, median rise 7.2 dB in c16, 6.5 in c17; 29 do not rise (c16 35). 64 decrescendos, median -5.6; 10 do not fall (c16 10). The loss sits on the winds' and low strings' f / ff arrivals (finding 1). Fast falls of the volume envelope (2 dB or more within 0.12 s): 23 -> 63; at crescendo ends 8 -> 22; under a sounding note 20 -> 25 (the new ones: Bassoons 1-2 and Contrabassoon at 210 and 894, -3.9 dB each; Violins II 983.7, Violas 197, celli 196.75). Most of the other new ones are role edges moved into rests (harmless).
- **Dynamic order per track** (held notes of 0.9 qn or more outside hairpins, median per printed dynamic): 8 adjacent steps reversed by more than 1 dB, the same count as c16 (finding 5).
- **S3.** Both sub. p's keep the hall: R Strings at 360 falls -39.8 / -44.6 / -46.3 / -47.6 / -48.0 dB in 0.1 s steps from the bar line with no step (c16 the same within 1.4 dB); at 828 -47.1 / -50.1 / -52.9 / -54.6 / -55.3. The master falls 10.5 dB from the tutti (105-120, -20.4) to the sub. p (121-128, -30.9). The subito fall itself is in CC11 (e.g. Violas CC11 106 -> 51 at 359.46).
- **sfp of bar 301.** Master 20-200 ms after each beat: 897 -19.2, 898 -18.7, 900 (sf) -19.8, 901 -24.6, 901.5 -26.2, then up to -16.7 at 911 (ff 304). The sf is now level with the chords of bar 300 (c16 1.5 dB under, because bar 300 fell 5 dB, not because the sf rose); the fall to p is 6.4 dB (c16 6.4, c13 9.2); p to ff +9.5 dB. Per stem the sf is at or over its upbeat on 7 of 10 tracks (c16 on 0). Acceptable; a larger fall would read more clearly as sfp (inferred), not ranked.
- **Timpani rolls** (stem per quarter, unchanged from c16 except the summit strokes): 101-103 -41.5 / -49.9 ... -28.8 (+12.7 to the top); 205-208 flat at -50 to -51 for six quarters, then -43.5 ... -36.0 under the printed cresc from 618 (+15.4); 301-303 from the roll's start at 906 -40.9 -> -33.4 into 909. The unprinted rolls do not grow: 129-130 and 285-286 start -38.0, settle to -44 to -45, then the stroke; 237-240 -48 to -55. Roll 332 grows +3.0 under its printed cresc (993-996). Every roll stays 9-19 dB under the master. In order.
- **Loop pulsing** (level and centroid autocorrelation at 3.95 s, detrended). Horn 1's last G sharp (10.9 s, 380-450 Hz band): -0.00 / +0.15 (c16 +0.12 / -0.15); Violin I solo copy +0.05 / +0.08; the master over the last note +0.09 / -0.09. Violins I alone reads +0.39 / +0.45 over its 8.9 s piece, but the doubled sum and the master do not carry it. No held note pulses audibly. The p5-p95 level range of the last note (13-16 dB) is the printed fade and the rit., not a loop.
- **Arc against the print.** In order everywhere except the items below: ppp opening -40.9; theme A p -37.4; counterstatement -30.2 (cresc to f at 41); hemiola -24.3; F major pp -36.6; ritmo di tre battute +18.1 dB from bar 89 to 101; ff tutti -20.4; sub. p -30.9; link ppp -41.0; trio dolce -35.9, f (197) -29.3, ff (209-224) -27.0 with the A6 at 218 the trio's loudest (short-term -23.4); codetta fades to -46.5 at 240; accelerando +8.2 dB; reprise sub. p -36.5; coda pp -37.5 -> build +11.9 dB -> summit -15.8; G.P. rings; Meno mosso -36.7; held-chord fade 361-364 -37.0 / -39.3 / -43.5 / -44.1; close -44.4.

## Findings, ranked by what a listener would gain

### 1. The crescendo gains moved into CC11 do not reach the f and ff arrivals: the winds' crescendos into 41, 129, 197, 285 and into bars 72 and 300 lose 3.5-6.5 dB on their own stems, and the master's f arrivals are 2-2.5 dB lower than c16 (bars 72 and 300: 5 dB) (measured)

**Where.** Hairpins 108-120 (bars 37-40 into f at 41), 204-213 (bars 68-71 into ff at 72), 372-384 (125-128 into 129), 576-588 (193-196 into 197), 840-852 (281-284 into 285), 888-897 (296-299 into 300). Tracks: Bassoon 1, Bassoon 2, Contrabassoon, Clarinet 1, Clarinet 2, Flute 1, Oboe 1; less on Double basses, celli, violas.

**What is wrong.**
- Master rise across the crescendo (bar before the hairpin start to the arrival bar), c15 / c16 / c17: into 129 +9.2 / +9.8 / +7.9; into 197 +11.4 / +12.2 / +9.2; into 285 +10.0 / +9.8 / +7.8; into bar 72 +17.8 / +21.0 / +14.0; into bar 300 +27.2 / +29.9 / +24.5. The starts are unchanged (within 0.6 dB); the arrivals fell (129: -22.5 -> -24.4; 197: -24.5 -> -27.0; 285: -22.9 -> -25.1; bar 72: -15.8 -> -20.7; bar 300: -14.7 -> -19.5).
- Own-stem rise across the hairpin, c16 -> c17: Bassoon 1 372-384 +18.6 -> +12.5, 576-588 +17.0 -> +11.1, 840-852 +19.0 -> +12.4, 108-120 +12.1 -> +5.3; Bassoon 2 372-384 +12.3 -> +4.8, 840-852 +12.4 -> +4.9; Contrabassoon 372-384 +7.9 -> +3.1; Clarinet 2 108-120 +28.3 -> +17.8; Clarinet 1 576-588 +11.6 -> +6.5, 840-852 +4.6 -> +1.0; Double basses 372-384 +10.8 -> +6.6. 54 crescendos lost more than 2 dB of rise against c16.
- Cause 1, the slope. `HP_GAIN_TO_CC11` converts dB to units at 0.22 dB per unit for every family. Measured on the c17 arrivals (arrival change minus envelope change, over the CC11 change, all 59 conversions): winds 0.045 dB per unit (n 32), strings 0.14 (n 19), brass 0.14 (n 7). Movement I c59 measured winds at 0.07 dB per unit at CC11 88-104. So the winds' 10 units bring about 0.5 dB where the envelope gave +3.9; the strings' 10-14 units bring 1.4-2 dB where it gave +3.
- Cause 2, the cap. `cap_add` 10 clips every 18-unit request on the f arrivals (resting CC11 88), `records/hp_to_cc11_clipped.txt`.
- Cause 3, the chained gains at 210 and 894. Bassoon 1, Bassoon 2 and Contrabassoon have p < f (204-210, 888-894), then f < ff (210-213, 894-897). The second gain is dropped (`drop_ends` [213, 897]); the first gain, which c16 carried into the second hairpin, is now released in 28 ms at 210.0 / 894.0 while the f arrival note sounds (vol_db 3.92 -> 0.0). Bassoon 1's stem per half quarter: 209.5 -35.8, 210.0 -40.6, 210.5 -42.5 ... 212.5 -45.3 (bar 72's ff). So the bassoons fall 9.8 dB through a printed f < ff (c16: -34.7 -> -34.4). The same happens at 894-897.
- Flute 1's ff arrival at 213 (E6, "Sus MAX") plays 4.1 dB under its own f eighth before it (-35.6 against -31.5). The c17 region gain E6 -5 on the f layer, the dropped gain and no accent bump together (CC11 104 at 212.81; c16 114).

**Fix (instrument side; the envelope keeps only slow section levels).**
- `build/score_config.py` `HP_GAIN_TO_CC11`: per family, `"string": {"db_per_unit": 0.14, "cap_add": 16, ...}`, `"brass": {"db_per_unit": 0.14, "cap_add": 16, ...}` (88 + 16 = 104, still under the strings' flat top). Keep `max_arrival_cc` 100.
- Winds: take `"wind"` out of `HP_GAIN_TO_CC11`. Clarinet 1 and 2 are on `CC1_DYN_TRACKS`: send their crescendo gain into CC1 instead (new key `"lane": "cc1"`; c14 measured Clarinet 1 at +11 dB from CC1 80 to 105, about 0.44 dB per unit, so 9 units for +4 dB). For the flutes, oboes, cor anglais and bassoons, CC11 cannot carry it. Keep the gain as the section's f level: hold it from the hairpin end to the next rest of 0.5 qn or more (or the next printed dynamic) and release it inside that rest. That is a section dynamic with the hairpin as its ramp, and it moves nothing inside a sounding note. The rule goes in `tools/score_to_parts.py` next to `HP_GAIN_TO_CC11` (`hold_to_rest`, family list).
- Chains: in the `drop_ends` branch, when the dropped gain's predecessor ends at the dropped gain's start (210, 894), hold the predecessor to the dropped hairpin's end and release it in the rest after the ff chord (216) or, for 897, 0.22 s after the sf of 900 (inside the printed sf -> p fall, as finale technique 78 times it). Do not release it at 210 / 894.
- Flute 1 at 213: `ACCENT_CC` `add_at` 213 is +8 but the lane shows none at 212.81-213.4. Check that the accent is written on "Sus MAX" there, or lift the E6 f-layer region gain from -5 to -2.
- Targets: master f arrivals within 1 dB of c15 (129 about -23, 197 about -25.5, 285 about -23.5); bassoons' stems rise at least +3 dB from 209 to 213 and from 893 to 897; no envelope fall of 2 dB within 0.12 s under a sounding note at a crescendo end.

### 2. The summit is no longer clearly the loudest moment: one hot flute note in the ff tutti comes within 0.2 dB of it in the master (1.4 dB in the mp3), and the summit itself lost 1.0 dB (measured)

**Where.** Flute 2, qn 327 (bar 110, the accented A6 half note, "Sus MAX"). The summit, bars 336-339 (qn 1005-1017): Violins II, violas, cor anglais, Clarinet 2, Oboe 1.

**What is wrong.**
- Momentary maxima, master, c16 -> c17: summit (1005-1017) -13.6 -> -14.7; ff tutti 105-120 -15.9 -> -14.9; ff 304 -16.4 -> -16.1; bars 102-104 -16.2 -> -15.9. The summit's margin over the first tutti fell from 2.3 dB to 0.2 dB (mp3: 3.2 -> 1.4). Short-term margin: master 3.7 -> 2.8, mp3 4.7 -> 4.2.
- The tutti's peak is at qn 327.96, and Flute 2 is the loudest stem of the orchestra there: -18.2 dB, 4.6 dB over Violins I (-22.8) and 13 dB over Flute 1 playing the same A6 (-31.4). Flute 2's own A6 elsewhere, all on "Leg Slur MAX", reads -27.4 to -30.8 (927 -28.2, 936 -28.8, 943 -29.3). This is the only A6 on "Sus MAX", in its f layer, which c17 raised +3 (`region_gain_db` "Sus MAX" f +3). c16 read -21.2 there; c17 adds the +3. The master's bar 110 reads -17.6 against -20.6 for the bars around it.
- The summit lost 1.0 dB (master 1005-1017 -14.8 -> -15.8). Stems c16 -> c17: Violins II -23.7 -> -25.8, violas -23.2 -> -24.8, Violins I -23.6 -> -24.2, cor anglais -2.0, Clarinet 2 -2.8, Oboe 1 -1.5, Trombone 1 -1.7. The strings' part comes from `CHORD_CC11` (-7 / -11 units on the summit's double and triple stops, span (1005, 1017)). The build (984-1005) lost 0.8 dB the same way (Violins II -2.6, Contrabassoon -3.0, Bassoon 1 -2.0). At fff a section playing double and triple stops is louder than one line, and the print asks the summit to be the loudest moment, so a per-doubling correction does not belong there.

**Fix.**
- Flute 2, qn 327: `build/mix.json` Flute 2 `region_gain_db`, a "Sus MAX" entry for pitch 93 of about -9 dB (it then sits near the legato row's A6). Alternatively `ART_AT` Flute 2 {327.0: "Leg Slur MAX"}, as at 927. Target: Flute 2 at qn 327 about -27 dB, under Violins I.
- `CHORD_CC11` spans: remove (1005.0, 1017.0) from `_ch17` for all five string tracks (keep 213-216 and 897-900).
- Targets: master momentary summit at least 2 dB over any other moment (c16 2.3); short-term margin over the tuttis 3.5 dB or more; mp3 limiter still under 3 dB (inferred: +0.6-0.8 dB at the summit adds up to 0.8 dB of limiting).

### 3. The fugato does not grow: each p entry of the subject is softer than the one before, and the third entry's held note nearly vanishes (bars 57-66, qn 168-198, and bars 289-294, qn 864-882) (measured; open since c14 #1)

**Where.** Celli p at 168 (bar 57), violas p at 180 (bar 61, celli pp), Violins II p at 192 (bar 65, violas pp). The reprise: celli 864, violas 876.

**What is wrong.**
- Master per bar 57-66: -43.2 -42.9 -43.4 -42.4 | -44.2 -42.4 -40.9 -41.2 | -40.4 -41.7. Ten bars of a three-voice exposition sit within 3.8 dB with no step at either entry. The growth starts only at bar 67 (-34.6) under the printed crescendo. Reprise bars 289-294: -43.9 -41.3 -43.6 -42.4 -44.7 -40.7.
- The subject's held note (the third note, 2.3 qn), body over 0.6 s: celli 171 -43.2 ("Leg Slur MAX", velocity 73, CC11 50); violas 183 -44.4 ("Sus MAX", velocity 52, CC11 41); Violins II 195 -50.7 ("Sus MAX", velocity 52, CC11 42). In c16 the violas and Violins II had CC11 48 / 52 (-43.4 / -48.2). The staccato head: celli -40.6 to -44.6, violas -45.0 to -46.7, Violins II -42.0 to -47.0. All three entries are printed p, so the Violins II entry's long note is 7.5 dB under the celli's. Reprise: violas 879 -45.4 against celli 867 -41.2.

**Fix (CC11, row and velocity only).**
- `CC11_ADD_SPANS`: Violas (182.9, 185.0, +9) and (878.9, 881.0, +9); Violins II (194.9, 197.0, +8). This brings each held note to the celli's CC11 50 (the "Sus MAX" strings lose about 0.7 dB per unit under 100, finale technique 80: +5-6 dB inferred).
- If Violins II 195 stays more than 3 dB under the violas' 183 after that, play it on the celli's row and velocity: `ART_AT` Violins II {195.0: "Leg Slur MAX"}, velocity 73 (`VEL_SET`), and the same for Violas 183 / 879, so the three entries match in row as well as in print.
- Targets: master bars 61-64 1-1.5 dB over 57-60 and bars 65-66 1-1.5 dB over 61-64; each entry's held note within 1.5 dB of the celli's (-43 dB).

### 4. The bassoons, Violins I and the celli do not step up from one printed dynamic to the next (measured)

**Where.** Whole movement. Held notes of 0.9 qn or more outside hairpins, stem median per printed dynamic (c17).

**What is wrong.**
- Bassoon 1: pp -52.8, p -44.4, mf -41.5, f -41.6, ff -41.2 (three steps in 0.4 dB); fff -32.7. Bassoon 2: mf -44.8, f -44.5. Metrics' per-bar table says the same (Bassoon 1 mf -41.4, f -41.5, ff -41.8, fff -42.2).
- Violins I: p -37.9, mp -36.8, mf -38.6, f -37.3, then ff -28.0. Four printed levels in 1.8 dB, then a 9 dB jump to ff.
- Violoncellos: mp -38.9, mf -39.7, f -43.0 (f 3.3 dB under mf), ff -34.4. Violas f -39.4, ff -41.6. Horn 2 mf -40.6, f -42.8.
- The adjacent-step reversals over 1 dB number 8 in c16 and 8 in c17. The bassoons' flat f / ff follows from finding 1 (no crescendo gain left) and from the trims: Bassoon 1 `soft_trim_db` mf +3.6 against `dyn_trim_db` f 0.0 and ff +1.2, while the bassoon CC11 is nearly flat from 72 to 104 (0.045 dB per unit measured above).

**Fix.**
- `build/mix.json` Bassoon 1 `dyn_trim_db` f 0.0 -> +2.0, ff 1.2 -> +4.0; Bassoon 2 f 0.5 -> +2.5, ff 1.7 -> +4.5 (fff unchanged). These are section levels per dynamic, not per note; they ramp across hairpins as the trims already do.
- Violins I and the celli: rows and notes differ by dynamic (staccato theme at p, legato espress. lines at mf / f), so the reversal is partly a mix of rows (inferred). Look first at the f notes: celli f held notes (16) at -43.0. If they are the second idea's "Leg Slur MAX" notes at 360-420 / 828-864, the role rows there (`roles.json`, 22 put back after the first render) are the place to check before any trim change.
- Target: each adjacent printed step on held notes at least +1 dB on every track (+2 to +3 dB on the solo winds and the strings).

### 5. Two small crescendo faults at the start of the coda build (qn 983.7-984 and 995.75-996) (measured; cause inferred from the envelope data)

**Where.** Violins II at 984 (bar 329, the mf start of the coda build after their pp < from 981); celli, Clarinet 2 and Bassoon 1 at 996.

**What is wrong.** Violins II's envelope falls from +1.79 to -5.11 dB between 983.69 and 983.83 (6.9 dB in 30 ms) at the arrival of their own pp < mf, while the note of 983.5 sounds. The stem reads -43.7 at 982.5-983.0 and -47.9 at 983.0-983.5: the crescendo turns down at its end. At 995.75 the celli fall 5.2 dB and Clarinet 2 and Bassoon 1 4.6-4.8 dB in 0.1 qn, at the f arrival of the 993-996 crescendo; there the note has ended (a rest), so this is not heard as a step, but the arrival level is 4.6-5.2 dB lower than the hairpin's top.

**Fix.** Violins II: the fall is a slow row (the 325-340 section row, -2.3 in B's balance) plus the pp trim's end, both starting at the hairpin end. With `ROLE_EDGE_MOVED` the row edge should sit in the rest before 983.5 or ramp over 2 s (Movement I c58's rule for role edges). Move that row's start to 984.5, after the note of 983.5, and ramp the trim across the hairpin (`cresc_trim_hold` skip span [981, 984]). Target: Violins II stem rising monotonically from 981 to 984.5.

## Do not touch

The S3 handling of both sub. p's (subito falls in CC11, the hall decaying under them); the timpani rolls and their passage roles (they grow only under printed crescendos and stay 9-19 dB under the master); the brass crescendos on CC1 (`CC1_DYN_TRACKS`, the horns' soft map); `HELD_DOUBLE` and the last note's lift as a set (no audible loop period at the close); the delivery chain and its ride (LRA 14.3, span 19.4, limiter 1.6 dB); the sfp's CC11 shape at 900 (sf now level with or over its upbeat on 7 of 10 tracks); the trio's dynamic arc (dolce, f at 197, ff A6 at 218 as its loudest) and the codetta's fade.

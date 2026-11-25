# Cycle 28, critic B: balance and levels (on the c27 render)

Levels in this report are K-weighted, ungated, summed over both channels (so about 3 dB above the per-channel RMS in `metrics.md`), from 4096-point frames every 50 ms on the stems in `cycles/c27/render/`. Bar and qn times come from `build/parts.json` `tempo`. The sum of the stems matched the master within 0.03 dB at bars 61-62. "Measured" means a number from the render or from parts.json. "Inferred" means a judgement about what a listener hears, or about a cause I did not isolate.

## Manual notes (B1: May 2021 HO manual pp. 137, 140, 150-151; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.137: each row in the Articulations view has its own Load button and a Volume knob that sets that articulation's loudness. | Every KS Master track. Unused rows are unloaded (`UNLOAD_UNUSED_ROWS`). Row-to-row level differences are corrected in the REAPER volume envelope (note and pitch trims). | Yes for loading. The row Volume knob is not used. It is not needed while row offsets stay in the volume envelope. |
| p.140: the Master channel's Gain sets the instrument's output without changing its mic mix, and Pan places it while keeping the mics' relative panning. | `mix.json`: `gain_db` is REAPER track volume, seats are on the mic channels, the main channel is centred. | Yes. |
| p.150: velocity sensitivity is linear by default. Velocity selects sample layers (the example gives p at 1-25 and mp at 26-45) and cannot change mid-note, so it is mainly for shorts. | Harp and timpani dynamics by velocity, pizz. | Yes. Sensitivity is left at linear, and harp and timpani velocities set their layers. |
| p.150: the MIDI Control list shows CC1, CC5, CC11, CC15, CC22, CC36 and CC64 per instrument, and each instrument's own description decides what they do. | All tracks: CC1, CC11, CC15, CC36, CC69 and CC70 are sent. | Yes, but see finding 4: the brass and clarinet patches use CC1 for something else. |
| p.151: send CC1 and CC11 before the first note. | The 3 qn pre-roll carries every first CC value. | Yes. |
| p.151: CC7 sets each track's upper limit in the mix, and CC11 shapes notes and phrases. | Track gain is REAPER volume. CC7 is used only on the timpani, which has no CC11. | Yes in intent. The timpani shape their hairpins with CC7, which is linear amplitude (KIT §3), and that matters for finding 2. |
| p.151: in Hollywood Strings and Woodwinds Opus Edition, CC11 controls loudness and dynamics and CC1 controls vibrato. In other instruments CC1 controls dynamics. | Strings and most woodwinds follow this. The brass KS Masters and the Clarinet KS Master crossfade their dynamic layers on CC1 (MANUAL-GAPS #1, p.101; layer groups read in M1 c09). | No for horns, trombones, tuba and clarinets. Their CC1 follows the vibrato rule (53-87), so every printed dynamic plays the middle layers (finding 4). |

## 1. Bars 79-80 are louder than the climax (bars 61-62), and Flute 1's B♭6 is the loudest stem in the movement (measured)

**Where.** qn 261.5-268, Flute 1 (stem 01), Violins I and II, Violas, Violas div, Double basses. Compared against bars 61-62 (qn 204-212).

**What.** Master per bar: 61 -13.2, 62 -13.1, 79 -11.7, 80 -12.7. The BRIEF (item 6) requires the climax to stay clearly the loudest. In bar 79 Flute 1 measures -16.7, 2.4 dB over Violins I (-19.1). Per half beat at qn 262-265.5, the flute is -15.8 to -19.1 against Violins I at -15.4 to -21.2. The same flute at the bar 61-62 ff measures -31.1 and -26.1, so one printed ff sounds 10-15 dB apart in two places. Flute 1 carries about 32% of the master's power in bar 79. The delivery master's five highest pre-limiter peaks are at 293.07, 293.78, 294.88 and 296.82 s, which is qn 262.1-265.1: this held flute note. The fifth peak is at 234.03 s (qn 211.8).

**Cause (measured in parts.json and roles.json).** Flute 1's `vol_db` reaches +11.4 dB at qn 263.65. That is three things added together:
- the roles [262.6,263.5,3] and [263.5,265.9,7], which series 1 c17 B #3 added to hold up a B♭6 sample that decays 10 dB when the note was printed f;
- v600's new one-beat crescendo into the note, which gets hpgain [261,262,7];
- the ff dynamic trim.

The strings also still carry the c12 lift [262,268,2.5] (Violins I, Violins II, Violas, Double basses; Violas div [266,268,2.5]). That lift was for v77's f arrival. The port dropped the Violoncellos' rows of the same purpose ("bar 79 lifts for the printed f; v600 prints ff") but kept these. Meanwhile the climax carries `_all` [204,212,-1.4,3.5].

**Fix** (`build/roles.json`).
- Flute 1: replace [262.6,263.5,3] and [263.5,265.9,7] with [261.5,262.6,-6], [262.6,263.5,-3] and [263.5,265.9,1]. This keeps c17's decay compensation and moves the whole note down 6 dB.
- Remove [262,268,2.5] from Violins I, Violins II, Violas and Double basses, and remove [266,268,2.5] from Violas div.
- `_all`: change [204,212,-1.4,3.5] to [204,212,-0.4,3.5].

**Predicted** (stem-sum simulation with -5 dB on the flute, so slightly conservative): bars 79/80 at -13.7/-14.0, and bars 61/62 at -12.4/-12.0. The climax would be 1.3-2.0 dB over bars 79-80, close to c26's 2 dB. The flute would be about level with Violins I or 1 dB under, and the loudest peaks would move to the climax. Afterwards, check the delivered span (16-19 dB) and the limiter (no more than about 3 dB).

## 2. The timpani roll in bar 81 does not decrescendo; at qn 270 it is the loudest stem and most of the bass (measured)

**Where.** Timpani (stem 20), the roll at qn 268-271 (bar 81). The score prints a decrescendo hairpin, and the whole tutti falls to p at 271.

**What.**

| qn | Timpani | Master | Loudest other stem |
|---|---|---|---|
| 268 | -30.6 | -16.8 | |
| 269 | -31.6 | -22.0 | Violoncellos -30.2 |
| 270 | -32.4 | -26.2 | Violins I/II -36.0 |

The roll falls 1.8 dB from 268 to 270.5 while the master falls 9.4 dB. At qn 270 it is the loudest stem by 3.6 dB. In 50-250 Hz it is -34.1 against the master's -33.4, so about 85% of the master's bass energy at that moment (69% at qn 269). This breaks Dan's rule 5: a long roll is never the loudest stem unless the timpani lead.

**Cause (read in parts.json).** The hairpin [268,271,"decresc"] has no printed target, so `dyn_curve` falls only one level (88 to 74). CC7 moves 51 to 48, about 0.5 dB because CC7 is linear amplitude, and `vol_db` moves +1.7 to -0.4.

**Fix.** In `build/score_config.py`, add `HP_TARGET_AT["Timp"] = {268.0: "p"}`, the tutti's arrival dynamic, as already done for Hn3 and Hn4 at 268. `TIMP_HP_DB_FACTOR` 1.0 then puts the CC7 shortfall into the volume envelope. Inferred from c13: a decrescendo roll fell 8.4 dB this way. Target: the roll is under -38 by qn 270 and falls with the strings. Do not use a role for this: a role is a 0.5 qn step in the envelope, which would cut the hall tail (S3).

## 3. The bass clarinet's tied pp pedal in bars 3-6 swells over the wind chord and covers Horn 3's moving voice (measured)

**Where.** Bass clarinet (stem 08), one A♭2 tied from qn 6 to 17 (Sus Non Vib, CC11 34 falling to 28). The pp chord of Clarinet 2, Horns 3-4 and the bass clarinet, under Horn 3's C-D♭-C.

**What (per qn).**

| | Bass clarinet | Clarinet 2 | Horn 3 | Horn 4 |
|---|---|---|---|---|
| qn 6-8 | -48.2, -47.0, -43.9 | | | |
| qn 9-12 | -38.1, -39.0, -38.5, -37.1 | -42.6 to -45.5 | -45.5 to -48.2; at qn 12 (its D♭): -41.5 | -43.0 to -48.9 |
| qn 13-16 | -39.9, -42.4, -42.7, -44.2 | | | |

The pedal is the loudest stem in bars 4-5, 4-7 dB over the other chord members. At qn 12 it is 4.4 dB over Horn 3's D♭, which is the only moving voice.

**Cause.** `vol_db` adds only +3 dB from qn 9 (`_all` [9,17,2] plus the soft trim). The other 6-8 dB of rise is in the held sample at a flat or falling CC11 (measured). Inferred: CC11 34 sits on this patch's layer edge (KIT §4: the next layer fades in at CC11 30-36), and a 12 s held sample blooms. Loop pulsing is not the cause: autocorrelation at 3.95 s is 0.22 at 80-300 Hz and 0.17 at 300-2000 Hz.

**Fix** (`build/roles.json`, Bass clarinet): [8,9,-1], [9,13,-7], [13,14,-5], [14,16.75,-3]. These chain under `ROLE_CHAIN`. They shape the held note slowly and are not a subito.

**Predicted:** about -45 through qn 9-16, level with Clarinet 2 and Horn 4 and 3-4 dB under Horn 3's D♭. Keep `_all` [9,17,2].

## 4. Brass and clarinets play the same middle dynamic layer at every printed dynamic, so pp and ff differ only in volume (measured on the render; patch mapping read in movement I)

**Where.** Horns 1-4, Horns 1-2 a2, Trombones, Bass trombone, Tuba, Clarinets 1-2: Horn 1's solos in bars 7-14 and 65-70, the climaxes in bars 61-64 and 79-82, and Clarinet 1's coda.

**What.** CC1 on these tracks is 53-87 from the vibrato rule (parts.json; for example, Horn 1 CC1 64 at p and 86 at ff, Clarinet 1 58 at ppp and 84 at ff). On Horn 1's F4, p and ff have the same tone colour:

| Horn 1 F4 | Spectral centroid | 1.5-5 kHz share |
|---|---|---|
| p (qn 32) | 493 Hz | -25.0 dB |
| ff (qn 204) | 486 Hz | -21.5 dB |

On its E♭4 the f note is darker than the p note (-31.7 against -29.6 dB). Compare Bassoon 1, whose layers follow CC11:

| Bassoon 1 | Centroid, pp to f/ff | 1.5-5 kHz share, pp to f/ff |
|---|---|---|
| E♭3 | 395 to 520 Hz | -36 to -26 dB |
| F3 | 519 to 663 Hz | -38.6 to -22.6 dB |

Horn 1's 12 dB span from p (-39.3) to ff (-27.0) comes from CC11 volume alone. Inferred: the pp horn solo sounds like a turned-down mf horn, and the ff tuttis lack brass edge. This is the "does p sound like p in every family" question, and the answer is no for brass and clarinets.

**Fix** (`MANUAL-GAPS.md` #1). In `build/score_config.py`, set `CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba", "Clarinet ")`. The trailing space keeps the bass clarinet out. Keep the generic `CC1_DYN_MAP`.

This changes the level of every note on 13 tracks, so first simulate the expected per-dynamic change. After the render, re-check:
- the Horn 1 solo margins (now +2.3 to +5.8 dB over the accompaniment sum, 5-9 dB over each single stem);
- the climax balance from finding 1;
- Trombone 1's two accents (BRIEF item 9; 2-5 kHz attack against body);
- every pitch and note trim fitted on these tracks.

Movement I needed two cycles to settle this. If that is too much at once, do the horns first (Horn 1's solos are the most exposed).

## 5. Coda: the Violas div voice is 4-8.5 dB over the other half of the violas from bar 87, and the final chord's fifth is buried (measured)

**Where.** Violas div (stem 31) against Violas (stem 24), qn 286-304 (bars 87-92). From qn 286 the div voice plays A♭3 and the section plays F3, E3 and E♭3.

**What.** Violas div minus Violas per bar, 86 to 92: +3.3, +3.7, +7.4, +7.9, +8.5, +4.7, +5.4 dB. Violas div is the loudest stem in bar 90 and second in bars 88-89 (`metrics.md`). In the ppp final chord (qn 301-304) the div A♭3 is -54.1 and -55.2. The section's E♭3, the only fifth in the strings, is -61.1 and -59.7.

**Cause (read in roles.json and PORT.md).** The port shortened series 1's [276.5,304,-5] cut to [278.5,286,-5] because "from 286 the div voice is the chord's A flat 3". So the div track enters at 286 with its +4 dB higher `gain_db` (6 against 2) and no cut. KIT §8 already found a DIV patch's soft layers relatively louder (+7.6 dB at ppp, c18).

**Fix** (`build/roles.json`, Violas div): add [286,304,-6]. It starts on the div voice's new note at 286, so there is no step inside a sounding note. Keep the copied section rows ([292,298,4], [298,304,7], [289,304,-2], [292.5,304,-3.5]).

**Predicted:** div minus section from -1 to +2.5 dB in bars 87-92, and the E♭3 about level with the A♭3 in the final chord.

## 6. The double basses vanish in the last four beats; the final chord has no audible 16-foot root (measured)

**Where.** Double basses (stem 26), A♭1 "4 soli", ppp, notes re-bowed at qn 299.8, 302.0 and 303.3. Compared against the Violoncellos (A♭2).

**What.** Per qn from 299 to 303:

| qn | 299 | 300 | 301 | 302 | 303 |
|---|---|---|---|---|---|
| Double basses | -57.9 | -64.7 | -64.8 | -67.0 | -67.7 |
| Violoncellos | -53.2 | -54.9 | -53.7 | -48.2 | -55.7 |

So the basses are 10-19 dB under the celli. Over the last 8 s the basses were 7.6 dB under the celli in c26 and are 13.8 dB under in c27. The master's 40-63 Hz band in the final chord is -81 dB, 32 dB under its 250-1000 Hz band. The basses' `vol_db` there is -15 to -22 dB (the 4 soli -3, `_all` -2 and morendo -1/-2/-3, the re-bow fits) and their CC11 falls to 24-18. The celli's `vol_db` is -5 to -14.

Inferred: the last chord sounds like it rests on the celli. The bass line drops out at the fermata although all strings hold the chord, a real 4-soli A♭1 ppp would still be felt, and KIT §4 already measured the Basses KS Master 5-12 dB under the Celli at the same soft CC11.

**Fix** (`build/roles.json`, Double basses): [299.75,304,5]. It starts at the re-bow at 299.8. Target: the basses 6-8 dB under the celli, as in c26. Check that the 303.3 note (-71 dB in c27) sounds.

## Checks for Dan's items 8 and S1-S3

- **Loop pulsing (measured).** Autocorrelation at 3.95 s is low on every held note this lens touches: the bass clarinet pedal 0.22, the Double basses' bars 65-70 pedal -0.07, the timpani ppp roll at 226-237 -0.02, and the master's final chord at 100-300 Hz -0.08.
- **S3.** All six fixes keep the sudden-drop rule. The timpani decrescendo goes through CC7 inside Opus, and the role rows either begin at a note onset or change slowly over held notes. None is a fast fall in the volume envelope under a sounding chord.
- **Not ranked (measured, minor).**
  - Violoncellos div's upper moving voice in bars 21-22 (qn 62-65) is 2-4 dB under the section's held E♭3.
  - Horn 3 (Horns 3-4 a2 at f, role +5) is the loudest stem in bar 62 (-23.6), 2-3 dB over Horns 1 and 2 at ff. Ease that role to +3 if finding 1 is applied.
  - Violoncellos are 1-3 dB over the Violins I tune through the bar 60 crescendo, because the role [190.5,204,-3,4] opens there.

**Do not touch:**
- The solo balances: Horn 1 in bars 7-14 and 67-68; Oboe 1 in bars 15-20 and 45-47, 5-8 dB over every single accompanying stem; the Violin I solo in bars 17-21 (+3.4 to +5 dB over the whole accompaniment); the bass clarinet in bars 31-36; Flute 1 in bars 37-40 (+2.8 to +4.7); the cor anglais in bars 41-51; Clarinet 1 in bars 85-89, 6-8 dB over every single stem.
- Trombone 1's quotation in bar 63, the loudest stem by 4.4 dB over Violins I.
- The bar 61-62 timpani roll settling under the strings (-29.6 falling to -37).
- The coda's Double basses and Violoncellos balance in bars 83-86 (their shared 63-125 Hz band within 0 dB).
- The low-end EQ (Double basses bell2 80 Hz, 160 Hz +4.5, climax loud_eq).

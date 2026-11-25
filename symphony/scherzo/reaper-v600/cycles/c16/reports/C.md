# Cycle 16, critic C: holistic comparison (lens C4), on the c15 render

Material: `cycles/c15/render/` (master, 31 stems), `cycles/c15/build_render/parts.json`, the delivered mp3, the same for c14, c12, c08 (stems) and c00 (master only; its stems are gone), `cycles/c15/records/timing13_c15.json`, `tools/pcx.py`, `cycles/c13/actor_scripts/timing13.py` (`robust_cross`), `build/mockup-events.tsv`, `build/score_config.py`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB. "pc" is `pcx.attack_pcx`, "xr" the robust crossover of the old and new pitch bands, both in ms after the score onset.

Not done: no comparison with a recorded scherzo (the reference folder holds only the Dvořák 9/i mp3; no Beethoven or Bruckner scherzo is in the repository), and no new measurement of the Movement I or II stems (only their headline numbers: Movement I c56 master -20.8 LUFS, LRA 23.0, against -21.0 and 22.7 here).

## Manual notes (H1: May 2021 HO manual, PDF pages 10-11 and 61-63, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.10: the new 18 Violins are "an alternate to the first 16 violins", with different players and vibrato, and "the legato is the best we have ever recorded" | Violins I's legato lines: second idea (bars 45-56, 121-140, 277-288), trio tune (177-184, 209-224) | Not used and never discussed in this loop. `18V KS Master.oib` and `18V Leg Slur MAX.oib` are installed (`Hollywood Strings Opus Instruments/18 Violins/`). Movement I's MANUAL-GAPS rejects it there (no bow-change row, every fit redone). Here Violins I has used one legato row since c14, so the first objection is gone. A range pass on bars 209-224 would show whether its joins are shorter than the 169-236 ms measured below (inferred; see finding 2) |
| p.11: the new 2 Trumpets' legato "is blazing at high velocities"; new 2 tenor trombones | trumpets play only bars 101-120 and the coda, on Solo Trumpet "StacSs DblTng RRx9" (56 notes) and "Sus Non Vib MAX" (7) | No legato line for trumpets in this score. Nothing to change |
| p.61: seven libraries; Solo Violin and Solo Cello belong to the product | bars 349-356 solo | Not installed (MANUAL-GAPS #5); the DIV A half section stays |
| p.62-63: LITE instruments hold about half the dynamic and vibrato layers of MAX | Violins I "Sus Marc LITE" (39 notes: the theme head's slurred pairs, the hemiola, and the sf note of the tutti sfp at qn 900) | The row is in use and carries c15's -8 dB row volume; that volume also lowers the sfp's sf (finding 3) |
| p.63: every instrument fades to silence on CC11 (niente) | the held G sharp's last fade (Violins I CC11 22 down to 8 at qn 1128), the chord of bars 361-364 | Yes |
| p.63: finger position on CC70 | `SUL_SPANS` | Yes (checked by the c15 C report against p.147) |

## c15 against c14, c12, c08 and c00 as a whole (measured)

- Master per section (29 sections): c15 is within 0.5 dB of c14 everywhere except bars 1-12 (+0.9). Against c12 and c08 it is within 2.0 dB everywhere. Against c00 the loud tuttis are unchanged (bars 105-120 -0.2, 305-324 -0.3) and the soft sections are 4-6.5 dB lower (F major episode -6.5, trio opening -5.2, codetta -4.9), the summit bars 336-339 5.0 dB lower.
- Spectrum shares, c12 to c15: 20-100 Hz -18.1 to -15.5 dB (c14's bass EQ change), 100-250 Hz -8.1 to -9.5, 2-6 kHz -9.6 to -10.1. c14 and c15 are equal to 0.2 dB.
- Lead over everything else, c08 / c12 / c14 / c15: theme A Violins I bars 13-28 +5.1 / +4.9 / +5.3 / +5.3; trio Clarinet 1 153-168 +4.9 / +4.3 / +5.6 / +5.5; celli 169-184 -1.7 / -1.5 / -0.8 / -0.9; solo violin 349-356 +0.7 / +1.2 / +1.8 / +1.7. Changed by more than 2 dB since c08: trumpets in the tutti +2.3 (c14), harp in the trio -2.8 (c14), pizzicato basses in bars 253-268 +3.9 (c15: -47.9 to -44.7 dB, see finding 5).
- Per note, c15 against c14 on the same stem (level over the first 0.35 s, the running median of 17 notes removed): notes that moved by more than 3 dB: Oboe 1 23 %, Flute 2 22 %, Clarinet 1 14 %, violas 13 %, celli 12 %, Flute 1 11 %, Violins I 6 %, Violins II 7 %, basses 7 %, timpani 8 %, horns, trumpets, low brass and harp 0-1 %.
- Timing: measure S outside 25 / 60 ms is 26 % / 5 % in both.

Verdict. As a whole c15 is equal to c14 in balance, tone, hall and timing, with the fader moving 0.8 times per note instead of 7.1. Two things are better on the stems: Flute 1's single ff notes at qn 348 and 354 no longer stand 7-10 dB over their neighbours (c14 -23 against -30; c15 -33 / -31), and the theme-head spikes are gone. The removal costs a listener four things, in this order: the re-bows of the held G sharp (finding 1), the sf of the sfp and 1 dB of the summit (finding 3), the octave doubling at bar 277 and a few single notes (finding 5), and 1-2.5 dB on accents that were barely marked before (finding 4). The largest fault now is not a removal cost: legato notes that follow a row change are late and are not stable from render to render (finding 2).

## Findings, ranked

### 1. The held G sharp of Violins I dips 6-9 dB at every re-bow, in the two most exposed places of the movement (measured)

Where: Violins I, bars 1-8 (re-bow at qn 6.446) and bars 364-376 (re-bows at 1103.814, 1116.299, 1125.156). Track "Sus MAX", velocity 38, CC11 22-24, CC1 38.

Evidence (stem, 0.2 s windows, seconds after the re-bow): c15 at 1103.8: -47.7 before, -55.3 at +0.2 s, -52.2 at +0.7, -51.2 at +1.0, -48.4 at +1.5. At 1116.3: -48.7, -58.8, -51.6, -48.5 at +1.0. At 1125.2: -48.5, -60.3, -54.4, -53.8, -50.8 at +1.5. At 6.4: -48.3, -56.3, -53.9, -53.3, -50.7. c14 with its re-bow fills held all four within 2 dB (for example -49.2 / -49.4 / -49.3 / -48.3 at 1103.8). In the master the last one is plainly audible: -45.1 dB before, -50.9 at +0.2 s, -48.6 at +1.0 (c14: -44.7, -46.2, -46.7); only Horn 1 plays with the violins there. This is Dan's note 8 ("some kind of weird bowing effect being applied on the last note") in a new form: three swells of 6-9 dB in the last twelve bars.

Cause: a new ppp sustain note needs 1.0-1.5 s to reach its level, and the old note stops when the new one starts.

Fix (instrument side; the Sus row is polyphonic):
- `tools/score_to_parts.py` `AUTO_REBOW` (and `tools/space_rebows.py`): let the old note overlap the new one by 1.5 s at soft dynamics (a new generic option, for example `REBOW_OVERLAP_S = {"pp_or_softer": 1.5}`), instead of ending at the new note-on. Two uncorrelated voices at full level give at most +3 dB at the end of the overlap, so take CC11 down over the overlap by the units worth 3 dB and step it back at the old note-off (range-test the slope at CC11 22; 4-6 units is the expected size) (inferred; the rise times are measured).
- Drop the re-bow at 1125.156. It starts a note of 2.84 qn; without it the note from 1116.3 lasts about 7 s, one loop seam, against a certain 7 dB dip under the final fermata.
- The celli's re-bows show the same, smaller: 1074.0 dip 6.2 dB (c14 none), 1080.0 7.2 dB with a +7.9 dB bump (c14 6.5 / 2.8), 618.0 11.5 dB in both cycles. Use the same overlap there.

### 2. Legato notes after a row change are late by 66-180 ms, and the same MIDI gives different results in different renders (measured; the cause of the instability is inferred)

Where: Violins I, Violins II, violas, celli: every note on "Leg Slur MAX" whose predecessor plays on "Sus MAX" or a staccato row. This is the whole open timing list.

Evidence:
- Time from note-on to the crossover of the two pitches (c15, `timing13_c15.json`, lead + xr, medians): inside the legato row Violins I 169 ms, Violins II 232, violas 234, celli 194; after a row change Violins I 236, Violins II 246, violas 202, celli 186 (from Sus MAX) and 233 (from Stac). On "Sus MAX" joins 68-90 ms; on staccato rows 25-56 ms.
- The leads of the row-change joins are 74-170 ms, so they read late: xr median Violins I +68 (3 of 5 over 60 ms), Violins II +88 (5 of 7), violas +35 (2 of 7), celli +66 and +113 (13 of 21). Together 23 of 40 row-change joins are over 60 ms late, against 22 of 208 joins inside one row.
- The open list, pc / xr on the c15 stems (lead in brackets): Violins I 372 +145 / +136 (114: the note-on is at the pickup eighth's onset), 855 +82 / +77 (159; c14 +12 / -61 with 209), 144 +97 / +70 (78, Sus MAX), 159 +114 / +57, 597 +92 / +92; Violins II 372 +210 / +180 (74), 374 +159 / +98, 387 +163 / +88, 134 +100 / +77, 146 +98 / +72, 840 +95 / +66, 855 +163 / +88; celli 524 +191 / +108 (142, after an eighth), 536 +42 / +65; Violas 855 +2 / +76. Fixed and holding: celli 510 -11 / -10, 512 +17 / +51, 648 +65 / +26, 840 +130 / -4, Violins I 624 entry -3.
- Violins I 855 is not an overshoot to be halved. With the keyswitch 0.3 qn ahead (c15) the note is a first note on the row and crosses 236 ms after its note-on; with the keyswitch 7 ms ahead (c14) the same note crossed 148 ms after it. The lead it needs now is 0.236 s.
- Same data, different result: Violins II 855 has identical notes, keyswitch (854.22, 7 ms before the note-on at 854.25) and CC11 in c14 and c15. In c14 the new pitch's band is at +8 dB 30 ms before the beat and crosses at -2 ms; in c15 it is at -11 dB there and crosses at +88 ms. Violas qn 585 (B3, a 3-qn note that re-attacks the pitch of 584.5 on the legato row, keyswitch 7 ms ahead; identical notes, CC11, CC1 and envelope within 0.2 dB): -42 / -39 / -38 dB at 585.5 / 586 / 586.5 in c14 and -63 / -54 / -50 in c15. Violas qn 579 (A3 after A3, same pattern): -54 / -48 at 580 / 580.5 in c14, -68 / -59 in c15. Across renders the two viola notes read: c08 present, c12 soft (-62 to -69), c14 present, c15 soft. `metrics.md` lists 579 as a silent note. So a legato-row note whose keyswitch stands 7 ms before it starts in one of two ways, and which one is not controlled.
- Not late: Flute 1 qn 132. The stem is within 3 dB of the note's level at the beat (-49.1 dB at 0 ms, -46.3 at +30, -46.5 at +90); pc reads +143 because its reference window reaches the next note. Drop it from the list. Violas 828 (pc +185) is a velocity-41 first note that rises 13 dB over 400 ms at -51 to -57 dB in the stem, 13 dB under the mix; S is not valid there (entry after a 154 ms gap), and it is a slow soft start, not a late one.

Fix (`build/score_config.py`, `tools/score_to_parts.py`, `build/leg_leads.json`):
1. `KS_MIN_LEAD_S`: add Violins II 0.15 and Violas 0.15 (line 1198 sets Violins II to 0.0). Every legato-row first note then starts the same way in every render. This is the refit the c15 actor deferred; the two viola notes and Violins II 855 are the measured reason.
2. Row-change joins take the first-note time as their lead, not a capped transition lead: 0.235 s Violins I, 0.245 s Violins II, 0.20 s violas, 0.21 s celli (the medians above). The predecessor is on another row and keeps sounding, so the lead may run under it. Violins I 855: 0.236 s (`REATTACK_LEAD_AT` or its `leg_leads.json` row).
3. Where the predecessor is an eighth (shorter than the lead: Violins I and II 372, celli 524, Violins II 385.5, celli 171 / 180 / 867 / 876 after staccato), play the downbeat on "Sus MAX" with a lead of 0.08 s (measured 68-90 ms) and return to the legato row on the next note, which is a half note or longer in each of these places and has room for item 2's lead.
4. Same-pitch slur heads on the legato row (violas 579 and 585; the brief already records that such a note plays the slow first-note layer): "Sus MAX" as well.
Target: 5 or fewer of the 40 row-change joins over 60 ms; Violins I against Violins II within 40 ms at 372, 374, 387 and 855; violas 579 and 585 within 3 dB of their c14 levels in two successive passes.

### 3. The summit has lost most of its margin, and the sf of the tutti sfp is 9 dB softer (measured)

Where: bars 336-338 (qn 1005-1014) against bars 300 and 104; bar 301 (qn 900).

Evidence:
- Delivered mp3, level per bar: c08 bars 337 / 338 -13.2 / -12.6 against bar 300 -17.2 and bar 104 -16.8 (4.0-4.6 dB clear); c14 -12.6 / -12.5 against -15.0 (2.4-2.5 dB); c15 -13.6 / -13.6 against -14.6 (1.0 dB; bar 336 at -13.3 is 1.3 dB clear). Master: c14 337 / 338 -14.7 / -14.9 against bar 300 -17.0; c15 -15.7 / -15.7 against -16.9.
- Why: in c15 the summit's strings fell with their per-note levels (Violins I bar 337 -24.0 to -26.1, bar 338 -22.6 to -24.5; violas -23.8 to -25.0; Violins II -25.5 to -26.7), the timpani strokes at 1005-1014 are 4 dB softer, the delivery got a new -1 dB `RIDE_TRIMS` row over 1004-1017, and bar 300's strings rose 0.4-0.7 dB. The delivery limiter works 2.4 dB, under the 3 dB limit.
- sfp: Violins I qn 900 plays on "Sus Marc LITE" (keyswitch at 899.01), the row that c15 set to -8 dB for the theme head. Stem at 900 / 900.25 / 900.5: c14 -24 / -19 / -20, c15 -33 / -28 / -29. Master, 0.4 s from qn 900: c14 -17.9, c15 -20.1, after a bar-300 chord at -16.3. The sf now arrives 3.8 dB under the chord before it.

Fix:
- `build/roles.json`: summit section level for Violins I, Violins II and violas over 1005-1017, +1.5 dB (one row per track, a section balance, not a note level); timpani as critic B decides for the strokes.
- `build/score_config.py` `RIDE_TRIMS`: remove c15's -1 dB row over 1004-1017, and start the 897-912 row three quarters earlier, (894.0, 0.0), (897.0, -2.0), so that bar 300 is held back in the delivery like bars 301-304. Expected: the summit 2.5-3 dB clear of every other bar, limiter near 3 dB.
- Violins I qn 900: move the sf note to "Sus MAX" (its `FP_SPIKE` CC11 shape carries the sf), or use a second marcato row entry without the -8 dB. Check that the stem returns to -24 to -19 dB there.

### 4. Printed accents have nothing on the instrument side, and half of them sit where CC11 has no headroom (measured)

Where: all 321 accents; strings 158, Flute 1 36, cor anglais 29, Oboe 1 28, Clarinet 2 18.

Evidence:
- Accented note against the note before it (stem level, first 0.35 s, median), c14 to c15: Violins I +0.6 to -0.2 dB, Violins II +0.8 to -0.2, violas +0.9 to -1.6, celli +0.3 to -0.4, Oboe 1 +0.1 to -2.3, cor anglais +4.4 to +1.8, Flute 1 +0.5 to +1.0, Clarinet 2 +0.5 to +1.9. The fader swells gave the strings under 1 dB by this measure, so the accents were weak before the removal too.
- In `parts.json` the accented notes' CC11 is +0 to +2 units over the previous note's (basses and Clarinet 2 +4) and their velocity is equal (strings 88-96 against 88-95). CC11 at the accent, median: Violins I 101, Violins II 112, violas 100, celli 107, basses 110, Oboe 1 112, cor anglais 113, Clarinet 2 114; 130 of 269 accents on these nine tracks stand at CC11 110 or more.

Fix (`tools/score_to_parts.py` `GENTLE_ACCENT`, as finale c17 item 1 in ONE_TIME_c16 #7): rest the f / ff passages at CC11 104-106 on strings, 98 on woodwinds, 100 on clarinets (the slow dynamic trim makes up the 1-2 dB), and give each accent a CC11 rise to 121-124 held 0.15 s and released over 0.15 s; on notes of an eighth or less hold it for the note. On short string rows use velocity instead (+16 to +22 steps, 3.4-11 dB by the finale's measurement). Target: accented note 2-4 dB over the note before it, with the 2-5 kHz share of the first 80 ms no more than 3 dB over the body (Dan: weight, not bite). Critic A has the per-line numbers.

### 5. Three lines lost a balance that a per-note level used to carry (measured)

- Oboe 1, bars 277-279 (qn 828-831.5), the second idea an octave under Flute 1, both "sub. p espress." with an accent: Oboe 1 stem -61 / -58 / -60 / -57 dB at 828 / 828.5 / 829 / 829.5 (c14 -51 / -47 / -49 / -48), Flute 1 -49 / -45 / -44 / -41. The oboe is 12-16 dB under the flute (c14 3-7 dB), so the octave is gone. Its envelope holds a -4 dB role at 828 where c14 had +3 to +7.5. Fix: remove or reduce the role row at 828 in `build/roles.json` (to 0 dB) and raise Oboe 1's CC11 for 828-840 from 37-40 by the units worth 5 dB (its `soft_trim_db` in mix.json is the alternative if the whole p level of the oboe is low).
- Double basses, pizzicato, bars 253-268 (qn 756-804): the stem rose 3.2 dB as a section (-47.9 to -44.7), single notes +5 to +8 dB (771, 780, 783, 786); Violins I's theme lead over everything else fell from -0.9 to -1.7 dB. In bars 32-33 (qn 93.5-97) the basses are 5-14 dB softer than in c14 (qn 96: -41 to -55). Fix: pizzicato velocity by pitch (the row takes level from velocity), per critic B's table with the printed dynamic removed.
- Horn 1 qn 598 (G sharp 4, slurred from the tied A4 under a diminuendo): -42 dB against -34 on the A before it; c14's +11 dB row made it -30. An 8 dB fall inside one slur at CC11 71 to 44. Fix: CC1 / CC11 of the diminuendo starting 6-8 units higher at 598 (the horns' joined notes are 2-5 dB low in general: the legato row offset of ONE_TIME_c16 #7 item 2).

### 6. The celli's trio tune starts with an 18 dB swell on its first note (measured; not a removal cost)

Where: celli qn 504 (bar 169, "arco, espress."), "Leg Slur MAX", velocity 63, CC11 49 rising to 59 over the note.

Evidence: stem at 0 / +90 / +200 / +260 / +400 ms after the beat: -53.6 / -45.1 / -43.6 / -40.8 / -35.7 dB in c15, -53.7 / -44.6 / -41.9 / -38.7 / -40.8 in c14. The note-on is 180 ms before the beat; pc reads +243 (c14 +140). The c14 early fill changed the reading, not the sound of the first 200 ms. The rest of the tune is even (31 notes, step median 2.2 dB, range 6.8 dB), Violins I's doubling from 528 has a step median of 1.0 dB.

Fix: the phrase head on "Sus MAX" at the same CC11 with a lead of 0.08 s, the legato row from qn 506 with finding 2's row-change lead of 0.21 s; or keep the row and start CC11 at 59 for the first note (flat instead of 49 to 59). Range-test both and keep the one whose level at the beat is within 6 dB of the level at +300 ms (inferred).

Do not touch: `VOL_CLASSES = ("slow",)` and the rule behind it; the hall (G.P. drop 20.8 dB, RT60 1.30 s); the per-region volumes in the Opus state; the theme head's row volume for the slurred pairs (apart from the sf note at 900); the celli's trio-tune leads at 510, 512, 567, 572 and the entries at 624 (Violins I, -3 ms), 648 and 840; Trombone 2's level in bars 105-120; the trio's harp level (11 dB under the clarinet); Flute 1 at 348 and 354 without their spikes; the master's section levels, which are within 0.5 dB of c14.

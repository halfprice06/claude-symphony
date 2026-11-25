# Cycle 28, critic C (holistic): the c27 render

Lens: the whole movement as a conductor hears it. I compared c27 with the c00 port baseline, with c22 (five cycles back), with c16 (the first render after the per-note volume removal), with Movement I's latest render (c62) and with the Dvořák 9/i recording. Material: `cycles/c27/render/` (31 dry stems, 4 returns, master), `cycles/c26/render/` (the same stems from c26, used as the control for c27's data changes), the masters and mp3s of c00 / c16 / c22, `cycles/c27/parts_rendered.json`, `cycles/c27/before/parts.json` (c26 data), `build/parts.json` (c27 rides as refit), `build/roles.json`, `tools/score_to_parts.py`, `build/mockup-events.tsv`. All mp3 bar figures are momentary-loudness maxima per bar (400 ms windows, 0.30 s head). For the delivery simulations I ran an unmodified copy of `tools/deliver_master.py` on the c27 master with the c27 head, editing only `ride_trims` in a copy of parts.json. The unedited run reproduces the delivered c27 file exactly (-14.0 LUFS, LRA 11.0, -1.1 dBTP, limiter 4.4 dB, final -8.0 / 223 -8.5 / 263 -8.6). The scratch scripts have been deleted.

## Manual notes

MANUAL-READING.md has no row for cycle 28 (third round), so I read the pages behind my top problems in full (May 2021 HO manual, PDF pages), and also MANUAL-GAPS.md.

| Manual (page) | What it says | Where it applies here | Followed? |
|---|---|---|---|
| p.150-151, "Volume, Velocity, and Expression" | CC7 is "best used to set the overall upper limit on the volume of each track ... relative to each of the other tracks". CC11 shapes the line. Volume "can be adjusted mid-note". | Since c27, CC7 holds the dynamic trims, the passage levels and the role-edge carries on every pitched track. | The use matches the manual. But the role-edge carries land at the wrong note (finding 1), so several track levels moved to the wrong place. A mid-note CC7 ramp at the original edge is legitimate by this page. |
| p.101, Brass "Sustain" | The Mod Wheel controls the dynamics of the brass sustains, and all 4 layers play at once. | Trumpets 1-2 in the Più allegro slur, qn 984-999 (c27 CC1 +12). | Partly. The CC1 lift moved the whole line up 5-9 dB, and the tenuto at 989 up most of all (finding 3). |
| p.91, Strings "Sustain" | Looped samples. Bow direction is a round-robin cycle of up and down strokes. The basses have no finger-position control. | Basses' pp B-flat pedal, bars 43-50 (re-bows at 170.86 / 181.68 / 190.53). | Followed. The round robin cannot remove the hole, because the hole is the slow pp attack of the new stroke (finding 5). |
| p.101-102, brass "Sustain Marcato" and the shorts | A marcato attack whose velocity sets a low-pass cutoff. Shorts have no release trails. | No new use this cycle. | MANUAL-GAPS #1 is still open. No finding depends on it. |

MANUAL-GAPS.md: the c27 CC7 entry ("CC7 is 20 log10 ... adopted on every pitched track") is confirmed. The level law is right. The fault is in the time at which `ROLE_EDGE_IN_REST` writes its CC7 carries. "StacSl Leg BC" is still untried and is not needed for any finding below.

## Where the movement stands (measured)

- **Arc on the master** (section mean minus integrated) matches c00 within about 1 dB everywhere except T (+0.6 -> -2.1 LU). So far the cycles have changed detail, not the shape of the movement.
- **Dynamic scale on the mp3** (bar medians by prevailing printed dynamic, relative to integrated):

  | | p | f | ff | fff |
  |---|---|---|---|---|
  | c27 | -6.5 | -1.0 | +2.2 | +4.4 |
  | c16 | -9.1 | -3.1 | +1.4 | +6.5 |
  | c00 | -9.9 | -3.1 | +1.0 | +7.1 |

  f to ff has improved (c24 / c25 work). ff to fff has shrunk from 6.1 (c00) to 5.1 (c16), 3.9 (c22) and 2.2 dB (c27).
- **Top of the loudness distribution.** p75 to maximum of short-term loudness is 3.4 dB on c27, against c22 4.3, c16 8.3, Movement I c62 5.4 and the Dvořák record 4.8. The twelve loudest bars on the mp3 lie within 0.9 dB of each other: the ff opening chord of bar 5 is 0.1 dB under bar 223, and bars 147 / 150 / 158 are within 0.4 dB of it.
- **What got better since c16 / c22.**
  - Chord fronts. In bar 5, the first 50 ms after the beat is -2.5 dB re the chord's maximum (c22 -4.8, c16 -4.1), and the peak comes at +200 ms (c22 +550, c16 +450). At bar 277 (qn 1104) the peak comes at +200 ms (c22 +350).
  - The soft heads, the muted second theme and the chorale gaps, as listed in c27 CHANGES.
  - Soft music is audible on earbuds: p10 short-term -21.7 LUFS (c16 -30.3 at -19.8 LUFS).
- **What got worse.**
  - The fff moments, through finding 1 (a c27 data bug).
  - How far the arrival stands out on the mp3: bar 223 minus bar 228 is 0.7 dB (c22 2.0, c16 7.8).
  - The closing Largamente. Bars 271-274 sit 3-4 dB under the ff of bar 255 on the mp3. In c16 and c00 they were level with it or above it.
- **What no longer limits it (measured).**
  - Loop pulsing: no pulse. Master 100-300 Hz band and spectral centroid, autocorrelation at 3.95 s: chorale 888-936 -0.02 / +0.00; T 1088-1112 +0.02 / +0.15 (no peak against the 3.0 s and 5.0 s lags).
  - Spectrum, mid-loudness 2 s windows on the mp3: 100-250 / 250-500 / 500-2k / 2-6k / 6-20k Hz bands at -8.4 / -6.2 / -3.3 / -10.2 / -31.7 dB, against Dvořák -8.1 / -5.8 / -3.3 / -10.3 / -31.2. Every band is within 0.5 dB; the c24 brightness gap is closed.
- **Weakest passages now, in order.**
  1. The three printed fff moments (223, 263, the final chord), where c27 lowered single string and brass parts 2-5.5 dB by mistake.
  2. The arrival-to-chorale span 223-228, which is flat on the mp3.
  3. The Largamente close 271-276, which sits under the Più allegro.
  4. The trumpet line of the Più allegro slur (984-999), which bumps on 989 / 991.
  5. The Allegro sections, still played on a click.

## 1. ROLE_EDGE_IN_REST puts its CC7 carries at the wrong note: the fff moments lost 2-5.5 dB on single parts, and other lines moved (measured)

**Where.**
- Bar 223 (qn 888-892): Violins I.
- Bar 263 (qn 1048-1053): Trumpet 1, Horns 3-4, Violins II.
- The final chord (qn 1108-1113.5): Violins I, Violas, Violoncellos, Trumpets 1-3, Trombones 1-2.
- Bar 167 (qn 664-668): Horn 2.
- Bars 40-41 (qn 156-162): Flute 1.
- Bar 225 (qn 896-900): Violins I.

**What is wrong.** When `_edge_fix` in `tools/score_to_parts.py` (about line 4918) cannot put a role edge in a rest, it moves the envelope edge up to 16 qn away. It then writes a CC7 shape that should carry the difference up to the edge. The CC7 ramp is centred on `on_`, the onset of the note picked from `hit_`, not on the edge:
- `hit_` keeps only notes with `o_ < x1_ - 1e-4`. A note that starts exactly at the edge is therefore left out, and the note before it (sounding across the edge because of its lead) is chosen.
- For end edges inside a note (899.9, 1054, 1113.5), `on_` is that note's onset, up to 5.5 qn before the edge.

So the level change lands at the start of the wrong note. Examples:
- Violins I role [892, 899.9, -6]: the -6 dB ramp sits at 887.7-888.1, on the fff arrival, and the restore sits at 896.0-896.2, 4 qn before the printed ff at 900.
- The 1113.5 final-fade edges put their CC7 cut on the final chord's own onset.
- Horn 2's +8.5 dB stopped-note role (668) starts at the note-on of 664.

**Evidence.** Stem levels, c26 / c27. The notes and the other data in these spans did not change in c27.

| span | part | c26 dB | c27 dB | change |
|---|---|---|---|---|
| 888-892 (fff arrival) | Violins I | -26.6 | -32.1 | -5.5 |
| 896-900 (mf) | Violins I | -39.1 | -37.2 | +1.9 |
| 1108-1112 | Violins I | | | -4.7 |
| 1108-1112 | Violas | | | -3.6 |
| 1108-1112 | Violoncellos | | | -2.8 |
| 1108-1112 | Trumpet 1 | | | -2.8 |
| 1108-1112 | Trumpets 2 / 3 | | | -1.4 / -1.5 |
| 1108-1112 | Trombones 1 / 2 | | | -1.5 each |
| 1108-1112 | master (the final chord) | | | -1.1 |
| 1112-1113.5 | master | | | -1.2 |
| 1048-1050 (263 fff) | Trumpet 1 | | | -1.7 |
| 1048-1050 (263 fff) | Violins II | | | -2.0 |
| 664-668 (f) | Horn 2 | -42.5 | -34.9 | +7.6 |
| 156-158 (decrescendo to p) | Flute 1 | -45.1 | -41.3 | +3.8 |
| 840-844 | Violoncellos | | | -4.0 |
| 788-792 | Violins II | | | -3.4 |
| 982-984 | Violins II | | | -3.3 |

- At bar 167, Horn 2 is now 4 dB over Horn 1 (c26: 3.4 under).
- Flute 1 holds up through its printed decrescendo in bars 40-41.
- A data-only check agrees with the stems. Net level (vol_db + 20 log10(CC7 / 127)) of the c27 parts minus the c26 parts, on sounding notes, gives the same spans, and every one sits on a `role_edge_moved` entry with "cc7".
- Separately, ruling 3 (Horns 3-4 [1032, 1048] 3 -> 0 dB) also took Horns 3-4 down 3.0 / 2.9 dB at 1048-1056. In c26 the +3 carried into the held note of the fff. Together with Trumpet 1 and Violins II, bar 263 lost 0.6 dB on the master, which is the whole of its step over bar 262.
- The final chord's 1.1 dB loss is why c27 needed a deeper ride on 223 to keep the final ahead.

**Fix (tools/score_to_parts.py, `_edge_fix`, generic).**
1. Include a note that starts at the edge: `hit_ = [... if o_ < x1_ + 0.05 and en_ > x0_ + 1e-4]`.
2. In the CC7 branch, write the carry on the original edge ramp, not on `on_`:
   - rising edge: `role_cc7.append([(a_, 0.0), (b_, -d_), (x0_, -d_), (x1_, 0.0)])`;
   - falling edge: `role_cc7.append([(x0_, 0.0), (x1_, -d_), (a_, -d_), (b_, 0.0)])`.

   The level then changes exactly where roles.json says. The change is in CC7, inside Opus, so it is not a fader move.
3. Leave the 1113.5 final-fade edges in place (`role_edge_join`), as CHANGES c27 intended.
4. `build/roles.json`: Horns 3 and 4, add [1048, 1056, 3.0], which restores the c26 level in the fff.

**Check before the lock.** Diff the net level of the new parts.json against `cycles/c27/before/parts.json`, per track, on sounding notes. No span of 1 qn or more may differ by more than 1.5 dB except the c27 rulings 3 / 4 passage levels, which are 264-320, 632-660, 935-952 and 1032-1048.

**Expected (inferred from the stem deltas).** The final chord +1.1 dB on the master. Bar 263's step over 262 back from +0.6 to about +1.2 dB. Violins I back on top of the arrival chord. Several of the gate's entry-window items should go into CC7 the same way: Oboe 1 851 and celli 496 are role steps at entries.

## 2. On the mp3 the C-major arrival barely stands over the chorale, and the Largamente close sits under the Più allegro; two ride changes fix both with no change to the spec (measured, simulated)

**Where.**
- Bars 223-228 (qn 888-912).
- Bars 271-274 (qn 1080-1096) against bar 255.

**Evidence (mp3, momentary maxima).**
- Bar 223 is -8.5. The chorale's bars 227 / 228 (winds and violins ff with hairpins at 906-912, over f brass) are -9.6 / -9.2. The arrival leads by 0.7 dB (c22 2.0, c16 7.8). On the master the lead is 9-10.7 dB.
- The rides cause this: -8.8 dB on 888-891.5 (needed so that the final leads) and +3.0 dB on 893-899.5 (c24 ruling 3), with nothing on 900-912.
- Bars 271-274 (ff, allargando to the Largamente) are -12.5 / -11.8 / -12.0 / -11.6. Bar 255 (ff) is -8.7. The 1079.5 row (-3.5 dB over 1080-1088, -2.5 at 1092) makes the difference. In c16 bars 271-274 were 0.9-3.0 dB over bar 255.
- Raising 223's own row does not help: the limiter takes it. With 888 at -7.8 the bar's maximum rose only 0.1 dB and the limiter went to 5.1 dB. The top of the scale is limiter-bound at -14 LUFS (Introduction: twelve bars within 0.9 dB). Only the passages around a climax can move.

**Fix (`build/score_config.py` RIDE_TRIMS, delivery only; my variant v6).**
- Add the row [(899.5, 0.0), (900.0, -2.0), (911.9, -2.0), (912.5, 0.0)].
- Replace the 1079.5 row with [(1079.5, 0.0), (1080.0, -2.0), (1088.0, -2.0), (1092.0, -2.0), (1096.0, -2.0), (1104.0, -3.0), (1107.8, -3.5), (1107.95, 0.0)].
- Leave every other row as it is.

**Simulated on the c27 master.**

| measure | c27 | v6 |
|---|---|---|
| integrated / LRA / true peak | -14.0 / 11.0 / -1.1 | -14.0 / 11.0 / -1.1 |
| p10 short-term | -21.7 | -21.7 |
| limiter | 4.4 dB | 4.4 dB |
| final / 223 / 263 | -8.0 / -8.5 / -8.6 | -8.0 / -8.5 / -8.6 |
| bars 226-228 | -12.1 / -9.6 / -9.2 | -14.1 / -11.5 / -10.7 |
| 223 over 228 | 0.7 dB | 2.2 dB |
| bars 271-273 | -12.5 / -11.8 / -12.0 | -11.0 / -10.3 / -10.8 |
| 274-277 | | within 0.2 dB of c27 |
| chorale 224 / 225 minus bar 62 | +3.9 / +2.7 | +3.9 / +2.7 (c24 ruling 3 kept) |

Variants:
- Removing the 1079.5 row entirely lifts T 2-3.4 dB, but bar 276 then reaches -8.2 and the limiter 7.4 dB. Rejected.
- TOP_RATIO 1.5 or 3.0 with v6: final lead 0.4 / 0.6, nothing gained.

Finding 1 raises the master's final chord about 1.1 dB, so refit the 888 and 1107.95 rows on the c28 master after the render (the final ride can then be less deep). Keep two targets: 223 at least 2 dB over bars 227-228, and bars 271-273 within 1.5 dB of bar 255.

## 3. Trumpets 1-2 in the Più allegro slur: the CC1 lift raised the whole line 5-9 dB and 989 stands 6-9 dB over its neighbours (measured)

**Where.** Trumpets 1 and 2, qn 984-999, bars 247-250: the f slur with the tenuto at 989.

**Evidence.**
- Stem level per note (first 1 qn, c27, change against c26):

  | note (qn) | 987.5 | 988 | 989 (tenuto) | 991 | 992 | 993.5 | 996 | 998 |
  |---|---|---|---|---|---|---|---|---|
  | dB | -39.3 | -37.4 | -28.8 | -34.8 | -38.2 | -35.1 | -38.3 | -34.1 |
  | change | +4.6 | +7.5 | +8.7 | +6.4 | +4.7 | +8.6 | +4.8 | +5.6 |

- 989 is 8.6 / 6.0 dB over 988 / 991. A tenuto asks for 2-3 dB of weight.
- Trumpet 2 rose by +5.8..+8.1 dB across the same notes.
- The CC1 +12 (ceiling 110) crossed a layer boundary (p.101: CC1 crossfades the layers), and the CC11 bump on 989 (+12) stacks on it.

**Fix (`build/score_config.py`, the c27 ruling 6 block).**
- Trumpets 1-2 CC1 lift over 984.5-999.9: +12 -> +6 (range test: the line +2..+3 dB over c26).
- 989's CC11 bump: +12 -> 0 on both trumpets.
- Targets: 989 2-3 dB over 988 / 991, per-note range of the slur 6 dB or less.

The late legato targets (Trumpet 1 970 +152 ms, Horn 1 818 +130 ms) did not move with leads in c27. Leave them; at this tempo they are less audible than the 8 dB bumps.

## 4. Remaining small faults of c27, with instrument-side fixes (measured)

**Stops at bars 6 / 113 / 166 / 204: 17.3-17.7 dB at +0.3 s on the mp3.**
- On the master the change against c26 is +1.8 / +0.5 / +1.8 / +2.5 dB. Bars 6 and 204 are the celli CC11 ceilings of ruling 8: the celli stem rings 14.4 / 18.8 dB down, against 10 dB before.
- Real tutti stops fall 20 dB in 0.43-0.58 s (LEARNINGS), so the movement is at the dry end, not wrong.
- To meet the 14.5-17 band, halve the celli ceilings' depth at bars 6 and 204: target a celli stem drop of 12-13 dB at +0.3 s.

**Horn 3's stopped decrescendo falls 14.2 dB (target 7-10).** Horn 3 CC11 ceiling over 548.25-551.6: 127 -> 50 becomes 127 -> 70. Horn 4 is at 7.4 and stays.

**The nine gate items.**
- With finding 1's carry at the edge, the role steps at entries (Oboe 1 851 +3.0, celli 496 -1.8) go into CC7.
- Harp 951.5 / 951.9 (-3.5 dB; the harp is outside `dyn_trim_to_cc7`): lower the two notes' velocity by about 10 instead. The KS Master has the Velocity -> Volume path since c22 (MANUAL-GAPS c22).
- Celli 15.0: put the role window (15.640, 15.660) after the quarter's played note-off. The quarter ends 0.13 s early since c27, so the window must move with it.
- Bassoons / contrabassoon 600 (-1.7) and violas 775.4 (+1.9) are dynamic changes inside slurs. Send them through the CC7 trim lane: check why `dyn_trim_to_cc7` leaves them on the envelope.

**c27 role moves listed in `role_moves_over_1qn.txt`.** Finding 1 covers every one that moved a level audibly. The remaining moves (Trumpet 1 932 -> 967, which sits in a 32-qn rest; the into-the-rest moves before entries) stay under 1.5 dB in the net-level diff against c26. One span shows on the stems that the diff does not explain: Horns 1-2 at qn 156-162 are 3-4 dB under c26. It is small at that level; check it in the same diff after the fix.

## 5. The basses' pp pedal re-bows, bars 43-50: drop the worst re-bow (measured; fix inferred)

**Where.** Double basses, B-flat 1, re-bows at qn 170.86 / 181.68 / 190.53 (AUTO_REBOW, vel 45, CC11 25-33).

**Evidence.**
- At 170.86 the old stroke stops at -53 dB, and the new pp stroke starts at -67 dB and takes about 0.5 s to reach -54. This is the slow pp attack of the Sus MAX stroke, not a release.
- The holes are 16.2 / 6.5 / 5.3 dB. Neither c27 variant (a 0.10 s lead, a CC7 counter-shape) changed them.
- A same-key overlap is not possible on one track: REAPER trims the earlier note.
- Audibility on earbuds is limited (58 Hz fundamental, -55 dB stem), so this ranks below 1-4.

**Fix.**
- Remove the 170.86 re-bow, so that the first stroke runs 164-181.68 (17.7 qn, about 6.3 s; about 1.6 loop periods): `rebow_moves.json`, or an AUTO_REBOW skip for Double basses at 170.859.
- Keep 181.68 and 190.53.
- Check the held note for loop pulsing (100-300 Hz band and centroid autocorrelation at 3.95 s under 0.3). If it pulses, put the re-bow back at 172.82, where the CC11 ramp is lowest (its fill window already ends there).

## 6. What still sounds like a machine: the Allegro on a click (measured; listener effect inferred; only if the cycle has room)

**Evidence.**
- Half-note beats: p90 deviation from the local median tempo is 1.5 % (c22 1.5 %, c00 0.0 %).
- Only 19 of 556 beats deviate more than 5 %, and 2 beats are more than 15 % slower (the printed rits).
- The research gives 5-8 % and 20-26 breaths (FINDINGS Part 5); Movement I is the same as here.
- c24 ruling 10 added only the three BEAT_STRETCH breaths.

**Fix (`build/score_config.py` PHRASE_ARCS, the tools already have the key).**
- "light" arcs (0.99 / 0.975 on the last two beats, no push) on the 16-qn F1 phrases: (40, 56), (56, 72), (104, 120), (120, 136), (600, 616), (616, 632).
- Run `--midi-only --tempo` and recheck the caesura gaps and entry leads in those spans on the range pass.
- Do not land it in the same build as finding 1 if the lock time is short. Finding 1 and finding 2 come first.

## Findings from the other movements

- Movement I c62 room bed: applies, and it is already unified in c27 (same -60 LUFS implementation).
- Limit on how far a guard may move a ramp: applies in a new form. Our uncompensated moves are capped at 1 qn, but the CC7 carries reach 16 qn and their CC7 step lands at the wrong note (finding 1). The net-level diff check in finding 1 is the guard that would have caught it.
- f to ff only +1.2 LU on their mp3: does not apply here (+3.5 LU on the c27 mp3; my bar medians give +3.2 dB).

**Do not touch:**
- the -14 LUFS loudness loop, `top_above` -6, ratio 2.1 and TOP_RATIO 2.0;
- the room bed;
- the Violins II "Sus Marc LITE" chord fronts at 0 / 16 / 584 / 1104 and the viola / celli leads there;
- the soft-head CC11 fronts;
- cor anglais variant b;
- the chorale's same-pitch gaps;
- the re-bow layout of the chorale and the final chord (no loop pulse);
- the string and wind spectrum (within 0.5 dB of Dvořák from 100 Hz to 20 kHz);
- the c24 chorale ride (+3 dB on 893-899.5);
- the CC7 level law (`dyn_trim_to_cc7`), which is right; only the carry timing is wrong;
- the mp3 head of 0.30 s.

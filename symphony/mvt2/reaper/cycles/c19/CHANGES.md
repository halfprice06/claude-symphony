# Cycle 19 changes (actor)

Snapshot of the c18 tools and data: `cycles/c19/before/`. All changes are data or tool rules; no Opus state changed, so all 32 tracks were updated with `build_reaper.py build/parts.json jobs --midi-only`. Then save, quit (40004 stopped at a modal dialog again; REAPER was killed after the save), `-new` restart, `Main_openProject`, one render.

## Accepted

### Critic A
- **A #1 Horn 4 bar 80 (tools/score_to_parts.py `find_unisons`).** Notes that `TRACK_WINDOWS` moves to another track are left out of the unison grouping (`_owned`). Horn 4's Ab3 now plays 265-268 from the start (was 266.9, dur 1.1). The other unisons (Ob 210, Cl 259, Bn 196) are unchanged.
- **A #2 fills (build/early_fills.json).** `auto_fills.py 18 build/parts.json --write`: 21 entries (3 new: Cl1 178, Hn1 36, Vc 203; 3 raised; lowered/removed as listed in each `_auto`). CA 132 and CA 134 then set by hand to the critic's lower, longer shapes: 132 `{"db": 4.0, "pre_s": 0, "hold_s": 0.30}`, 134 `{"db": 3.0, "pre_s": 0, "hold_s": 0.32}` (`_auto`: "c19 shape").

### Critic B (build/roles.json, build/mix.json)
- **B #1 bars 31-33:** Bass clarinet `[93.5, 99, -6, 2.5]`, Cor anglais `[93, 98.5, 2]`.
- **B #2 p<mp crests:** Horn 1 crest row `[33.5, 38.5, 1.5, 1.0]` -> `[33.5, 38.5, -1.0, 1.0]` (-2.5 dB, not the proposed -3: the c18 bar 8 swell peaks at -33.1 dB RMS at qn 21, and -3 would bring the printed mp crest to within about 1 dB of it; c14/c15 work put the crest on top). Cor anglais `[127.5, 133.5, -3.5, 2.5]`.
- **B #3 bar 37:** Bass clarinet `[105, 110.5, -4]`, Flute 1 `[108, 112, 2]`.
- **B #4 bars 81-82:** Horns 1-2 a2 `[269, 278, -5]`.
- **B #5 bars 61-62:** Violas `[204, 212, 2.5]`.
- **B #6:** Horn 3 `[86, 90, -3]`; mix.json Double basses `soft_trim_db.ppp` 1 -> 4.

### Critic C
- **C #1 solo timing.** `LEG_PAIR_EXTRA_S` Horn 1 (F4 -> Bb4) -0.12 s; Oboe 1 (Db5 -> C5) and (F5 -> Eb5) +0.10 s. `build/leg_leads.json`: Horn 1 201 +0.10, Bass clarinet 92.5 +0.07 / 106 +0.08.
- **C #2 caesura breaths.** New `CAESURA_BREATH_QN = 0.12`: a loud wind/brass note ending at a breath that also has a `CAESURA` (204, 268) ends 0.12 qn early instead of 0.3. The listed `entry_leads.json` extras at 268 (Ob1, Cl1, Cl2, Bn2) still apply after the shorter rest (new `cb_` condition; without it they were lost).
- **C #3 viola triplets.** New `LEG_CAP_FRAC = {"Violas": [(108, 124, 0.75), (186, 192, 0.75)]}` (legato lead cap as a fraction of the previous note, default 0.45), plus `LEG_PAIR_EXTRA_S` Violas (58, 61) and (57, 60) +0.10 s. Leads went from 0.15 qn to 0.25 qn; the smallest note-on spacing in bars 37-40 is 0.228 s.
- **C #4 violin and cello joins (leg_leads.json).** Vln II 68 +0.10, 80 +0.08, 254 +0.08, 71 -0.10, 243 -0.10; Vln I 192 +0.04, 196 +0.04, 200 +0.08, 247 +0.08; Vc 54 +0.08, 180 +0.08.
- **C #5 final tail hold (tools/build_reaper.py `vol_points`).** The rest after each track's last note holds the envelope at its value at that note's end until the end of the project. The c09 final fade itself is unchanged (it already holds -10 from 304); the rise came from roles ending at 304, which the hold now overrides.
- **C #6 Bassoon 1 chord changes.** `ABUT_LEAD = {"Bassoon 1": {"lead_s": 0.10, "max_cc": 50, "overlap_qn": 0.0, "at": [27, 35, 36, 38]}}`, with a new `"at"` condition. The same-pitch repeats at 22/32/33 are unchanged in parts.json.

## Rejected or deferred
- **A #3 double-bass loud lead (test): deferred.** The critic's own spread (p25 -0.10, p75 +0.34 s) is wider than the 0.08 s shift, and the same mechanism failed in c15. With one render per cycle, a test on the climax bass line that could open holes is not worth it until the measurement is tighter (for example per-change rise times on the Cb stem alone).
- Oboe 1 qn 210 (C #1, Largamente portato path): left, as the critic suggested, since no lead applies on that path.

## Render
One render after a fresh open (62 GB, 0 GB compressed at the start; 15 GB compressed by the end). Attack gate 19 of 20: Vln I 171 "+0.34 s", the known probe artefact (c17, c18). No clipping: master sample peak 0.643.

## Measured (c18 -> c19)

| | c18 | c19 |
|---|---|---|
| Master integrated / LRA / TP | -22.5 LUFS / 23.6 LU / -4.1 dBFS | -22.4 LUFS / 23.7 LU / -3.8 dBFS |
| mp3 integrated / LRA / TP | -19.8 LUFS / 16.0 LU / -1.6 dBTP | -19.8 LUFS / 16.1 LU / -1.6 dBTP |
| mp3 span / limiter | 18.6 dB / 1.7 dB | 18.5 dB / 2.0 dB |

Stem RMS (stereo power, dB) unless noted:
- A #1 Horn 4 265.25-266.75: -51.6..-86.4 (hole) -> -31.8..-33.7, within 1.5 dB of its body; no attack at 266.9. Horn sum (Hn3 + Hn4 + a2) 265-267 +1.2 dB.
- A #2 CA 132 200 ms dip 7.2 -> 3.3 dB; CA 134 5.9 -> 4.7 dB (target 4.5).
- B #1 qn 93-96: BCl -34.0..-29.0 -> -36.9..-34.8, CA -46.1..-46.9 -> -44.1..-44.9; gap 12-17 -> 7-10 dB (BCl still on top).
- B #2 Horn 1 crest qn 34: -30.9 -> -33.9 (bar 8 swell -35.4, so the mp crest stays 1.5 dB on top). CA 128-129: -32.2 -> -35.7 (now 8 dB over the flute, was 11.5).
- B #3 qn 108.5-109: BCl -35.5/-35.8 -> -39.5/-39.8, Fl1 -42.3/-41.3 -> -40.3/-39.3; BCl over flute 6.8 -> 0.5 dB (RMS; the flute's A-weighted lead is larger).
- B #4 a2 horns 270/271: -37.7/-37.0 -> -42.7/-42.0, under Vln I at 270 (-39.4) and level at 271 (-43.2).
- B #5 Violas 204-212 +2.5 dB (-33.2..-32.1 -> -30.7..-29.6), 1.5-3 dB under Vln II.
- B #6 Horn 3 87-89 -3 dB (now 1.6-2.3 dB under Vln I at 87, was over); Cb at 301 -57.0 -> -54.0 (Vc -53.6).
- C #1/#4 crossover (stereo-power legato crossover / rise, s): Hn1 34 -0.157 -> -0.027, 178 -0.127 -> -0.037, 201 +0.178 -> +0.063; Ob1 47/55.5/143/270 +0.13..+0.16 -> +0.04..+0.06; BCl 92.5 +0.143 -> +0.078, 106 +0.123 -> +0.028; Vln II 68 +0.168 -> -0.002, 71 -0.152 -> -0.052, 243 -0.132 -> -0.037, 254 +0.118 -> +0.038, 80 +0.268 -> +0.193 (cap); Vln I 192 +0.123 -> +0.083, 196 +0.133 -> -0.002, 200 +0.123 -> -0.062 (rise -0.02), 247 +0.143 -> +0.058; Vc 54 +0.123 -> +0.023, 180 +0.153 -> +0.068.
- C #2 master before 204: lowest 0.1 s frame -20.2 -> -18.7 dB against -17.0/-16.7 on the beat (dip 3.2 -> 2.0 dB). 268 dip 1.8 -> about 0.9 dB.
- C #3 Violas 108-124 crossover median +0.053 -> -0.017 s, max +0.223 -> +0.138; the 58 -> 61 rises +0.13 -> +0.02..+0.04.
- C #5 Cb tail after 304: c18 rose -68.4 -> -65.5 dB at +0.25 s; c19 -64.2, -64.1, -64.9, -68.7 (no rise). Tuba after 212: -47.4/-57.7 -> -46.7/-54.0 at +0.2/+0.5 s (slower fall).
- C #6 Bn1 body - 3 dB: 27 +0.25 -> +0.20 s, 35 +0.30 -> +0.19 s. The 22/32/33 repeats are unchanged. But the hole before 36 deepened 8.1 -> 11.5 dB and before 38 4.7 -> 6.1 (the led notes end at the next moved start with no overlap).
- Master top peaks: 207.65 -4.06 -> -3.84, 206.52 -4.16 -> -3.95 dBFS (violas +2.5 in the tutti); limiter 1.7 -> 2.0 dB.

## Open
- mp3 LRA 16.1 (0.1 over the target band).
- Bn1 36/38 holes after the abut lead: try `overlap_qn` 0.03 on those two, or drop them from `at`.
- `auto_fills.py 19` (dry run) proposes 17 changes, among them new Vc 54/180/210/256 fills, Hn1 202 +3, Cl1 266 +2.6, Ob1 143 +1.8; the c19 CA 132 fill now lowers to 1.7.
- REAPER quit (40004) stopped at the modal dialog again, right after a successful save job.

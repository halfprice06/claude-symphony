# Critic B, cycle 10: balance and levels (render c09)

Method. K-weighted levels (BS.1770 filter as a zero-phase FIR) in 10 ms frames from the c09 stems, on the c09 parts.json tempo map (parts.json has not changed since the c09 render). Per-note levels run from the score onset `sq` + 80 ms. Where low instruments are compared with higher ones in soft passages I also use A-weighting, because K-weighting barely discounts 40-100 Hz and overstates the basses at low listening levels. Delivery numbers come from re-running the `deliver_master.py` ride offline on the c09 master and from ffmpeg ebur128 on the delivered mp3. A level simulation (`sim.py`) applies new mix.json soft trims to the stem frames through each track's `dyn_curve` and the `vol_points` table. On the unchanged c09 data it gives I -23.6 / LRA 23.9 (measured -23.7 / 23.8). Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c10-B/`: `prep.py`, `lib.py`, `sim*.py`, `lim.py`, `deliv.py`, `peaks.py`, `dyn.py`, `inv.py`, `melA.py`, `pair.py`, `aw*.py`, `coda.py`, `barlev.py`.

Delivery numbers for c09 (measured):
- Master: -23.7 LUFS, LRA 23.8 LU, TP -3.9 dBFS. Short-term p10 -43.2, max -14.2, span 29.0 dB.
- mp3: -19.5 LUFS, LRA 16.0 LU, TP -1.6 dBTP. Span 19.8 dB (target 16-19). Limiter 4.5 dB (target about 3).
- Climax rise over the 15-20 s before it: 14.2 dB in the master, 11.9 dB in the mp3. 0 inversions. 83% of each 5 s move is kept.
- The ride is at its +10 dB cap for 20 s, and above +7 dB for most of bars 1-21, 34-51, 65-70 and 83-92.

What holds (measured):
- The same printed dynamic gives the same level in every family. Per-note medians at pp: winds -49.9, brass -49.8, strings -50.5. At p: -42.2, -42.4, -43.5.
- Horns and trombones at the bar 61 climax follow Rimsky (rimsky-principles p41: in forte, horns are half as strong as trombones, so they are marked one degree higher). Hn2-4 at f measure -30.5 to -32.9; Tbn2, BTbn and Tuba at mf measure -31.4 to -32.6.
- Melody margins, A-weighted, melody minus the loudest other stem, per beat medians:
  - Violins I+II: +8.4 in theme A (bars 23-30), +6.2 in theme B (53-58), +8.2 in bars 71-74, +5.5 in 75-78.
  - Horn 1 solo, bars 7-14: +6.8.
  - Flute, bars 37-40: +6.3.

## 1. The soft passages are still too quiet in the mix; the c08 brief's soft-trim lift was never applied (measured; simulated fix)

Where: all ppp/pp/p passages (bars 1-22, 31-52, 65-70, 82-92), every track except timpani and harp harmonics. Config: `build/mix.json` `soft_trim_db`.

What:
- The brief (item 6, after c07) asks for ppp/pp +2-4 dB and p +1-2 dB through `soft_trim_db`. c08 and c09 changed neither the global table nor the overrides. The global is still `{ppp -2, pp 0, p +2}`, so ppp is still trimmed down.
- As a result the delivery ride does all the work. It sits at +7 to +10 dB through most of the piece and hits its +10 dB cap for 20 s (bars 1, 84-85, 92). The mp3 span is 19.8 dB, over the 16-19 target.
- The trims also make the dynamic ladder uneven. Per-note medians step about 7-8 dB from pp to p in every family, but only 2-4 dB from p to mp:
  - winds: pp -49.9, p -42.2, mp -39.6
  - brass: pp -49.8, p -42.4, mp -40.5
  - strings: pp -50.5, p -43.5, mp -39.6, mf -38.3, f -33.0, ff -29.2

  The CC11 steps are even (pp 34, p 46, mp 58). The soft-trim table adds 2 dB to both the ppp→pp and the pp→p steps.
- The quietest bars of the master are bars 83-85 (ppp coda), -50 to -51 RMS, and bar 66, -50.6. The climax is -17.9.

Evidence (simulated with `sim3.py`, c09 stems plus the trim change, then the `deliver_master` algorithm). The simulation reads the mp3 about 0.7 LU and 1.4 dB of span high against the measured c09, so the corrected values are in brackets:

| | master LRA | mp3 LRA | mp3 span | seconds at the +10 ride cap | bar 1 / 66 / 84 / 92 | bars 61 / 79 |
|---|---|---|---|---|---|---|
| c09 | 23.9 | 16.7 [16.0] | 21.2 [19.8] | 20 | -44.1 / -48.3 / -49.2 / -46.4 | -14.4 / -18.5 |
| delta ppp +3, pp +3, p +1.5 | 21.4 | 15.0 [about 14.3] | 19.5 [about 18.1] | 10 | -41.1 / -45.3 / -46.4 / -43.5 | unchanged |

The delivery gain (lift) stays at 6.5 dB, so the limiter at the climax is unaffected.

Fix in `build/mix.json`:
- Global `soft_trim_db` becomes `{ppp: +1, pp: +3, p: +3.5}`, with `_except` unchanged (Timpani, Harp harmonics).
- Add the same delta (+3 / +3 / +1.5) to every per-track override:
  - Clarinet 1: {-1, 0, 0.5}
  - Clarinet 2: {-0.5, 1.5, 3.5}
  - Bassoon 1: {4, 6, 5.5}
  - Bassoon 2: {5, 8, 6.5}
  - Violas: {1, 5, 3.5}
  - Double basses: {1, 6, 6.5}

CC11 does not change, so pp keeps its soft layer and timbre. This needs only `build_reaper.py --midi-only` (envelopes).

Check after the render:
- master LRA 21-22 LU
- mp3 LRA 14-15.5 LU and span 17-19 dB
- ride at its cap for no more than 10 s
- no printed-dynamic inversion within a track (`inv.py`)

## 2. The timpani are inaudible at both climaxes: the ff/f strokes sit 8-13 dB under the rest of the orchestra even in the timpani's own band (measured; audibility inferred)

Where: Timpani, qn 204 and 208 (bars 61-62, ff), and qn 262, 265 and 268 (bars 79-81, f). Code: `tools/score_to_parts.py`, timp block, `roll_db` / `timp_db`.

What: compare the loudest 50 ms frame of the timpani stem in 50-250 Hz with the master in the same band and frame:

| qn | 204 | 208 | 262 | 265 | 268 |
|---|---|---|---|---|---|
| timp minus mix (dB) | -10.6 | -8.2 | -9.0 | -13.1 | -11.0 |

- In the whole spectrum, the bar 61 ff roll is 17 dB under the mix at its attack. Its per-note level is -33.4, against Vln I -25 and the mix -14.2.
- Dan's rule 5 asks for a roll to start at its printed dynamic and then settle. These rolls start already settled, because `roll_db` puts ff at -11 dB and f at -16 dB of CC7. The roll then falls another 5 dB.
- At bar 61 the movement's only ff timpani stroke is masked. Inferred: a listener hears no timpani at either climax.

Fix: in `score_to_parts.py`, timp block, add a loud-attack bump to `vol_parts` for rolls and strokes printed f or louder (`base(q) >= DYN["f"]`):
- +6 dB from the onset (10 ms rise), held 0.25 qn, back to 0 by 0.75 qn.
- It ends before the settle has fallen by 1 dB.
- Name it `TIMP_LOUD_ATTACK_DB = 6`.
- Leave `roll_db` and the settle unchanged, so the roll body stays under the texture and is never the loudest stem (Dan's rule 5).

Peak cost: the timpani band peak at 204 goes from -35 to about -29 dBFS, far under the -4.6 dBFS tutti peak there, so the limiter is unaffected.

Target: the same band-frame difference between -3 and -5 dB at qn 204, 208 and 262, with the roll body at +1 qn within 1 dB of c09.

## 3. The limiter does 4.5 dB, and the largest single cause is Trombone 1's two marcato attacks at bar 63 (measured)

Where: Trombone 1, qn 212.5 and 213.0 (bar 63, ff marcato quotation). Second cause: the bar 61 tutti, qn 204.4-208.

What: the master's loudest sample, -3.85 dBFS at qn 212.54, is Tbn1 alone (-5.5 dBFS). A 0.1 s window analysis of the delivery chain gives this gain reduction:

| where | gain reduction (dB) |
|---|---|
| qn 212.5 (Tbn1) | 4.5 |
| qn 213.0 (Tbn1) | 2.7 |
| qn 204.4, 206.4, 207.8 (bar 61 tutti) | 3.3-3.7 |
| elsewhere in bars 60-62 and 79 | 1.0-2.9 |

The two Tbn1 attacks:
- Peaks: -5.5 and -7.6 dBFS. Their bodies, 0.1-0.4 s after the onset, are only -25.2 and -23.1, a 20 dB crest.
- The rest of the phrase (qn 213.5-218) peaks at -14.6 to -17.9. The two accented attacks are 9-11 dB hotter than the other notes, while their bodies are only 1-3 dB louder.
- Data: vel 121, CC11 122 (an sf-style spike over ff 114), `ACCENT_DB` +2 in the volume envelope, dyn_trim ff +4.
- This is the hard click that rule 4 forbids, and it is the master's peak.

Fix:
- `score_to_parts.py` `VEL_SET`: Tbn1 212.5 and 213.0 at 108 (c09 measured v110 at qn 218 as +2.2 dB over its neighbours).
- Skip `ACCENT_DB` on notes with velocity 115 or more, because the attack layer already carries the accent.
- Cap the CC11 spike at 118 for Tbn1 at these onsets.
- Target: Tbn1 peaks at or below -10 dBFS, with the body 0.1-0.4 s after the onset within 1 dB of c09 (-25 / -23). Tbn1 stays the loudest stem in bar 63.

Then re-measure the limiter. If bar 61 still needs more than 3.3 dB, lower the climax body by 0.7 dB rather than limit harder. Use roles.json spans of -0.7 on every track over [203.5, 212], or `deliver_master.py` TARGET_I -19.5, which is inside the research range of -18 to -20. Bar 61 stays 3.6 dB over bar 79.

## 4. The timpani's pp melodic figure in bar 84 sits 6-11 dB under the ppp string pedal (measured)

Where: Timpani qn 277 (E flat 3), 278.5 (C3) and 279 (A flat 2, held into bar 85), printed pp. Under it, violas, cellos and basses hold ppp. It is the only moving voice in the bar (score p7; the plan calls it the timpani's melodic moment).

What (K-weighted per 1.5 qn, then A-weighted):

| | Timpani | Violoncellos | Double basses | Violas |
|---|---|---|---|---|
| K-weighted | -61.2 / -58.0 | -53.2 | -54.4 | -57.6 |
| A-weighted (qn 277-280.5) | -74.4 / -71.2 / -74.8 | -65.4 / -68.6 / -67.1 | | -63.8 / -62.5 / -61.4 |

- The pp solo lies under the ppp accompaniment by 6-11 dB, the reverse of both the printed dynamics and the roles.
- The earlier +3 note trims (c05/c06) and `TIMP_VEL` 60 were not enough. Strokes at pp already get +20 dB of CC7 in `timp_db`.

Fix: `build/note_trims.json` Timpani `277`, `278.5` and `279` from 3 to 11. Keep velocities 56/60/60, so the pp timbre stays.

Target:
- Timpani A-weighted 1-3 dB over the violas and cellos in qn 277-280.
- The qn 279 ring under Cl1's entry at qn 280 at least 3 dB under Cl1.

If the trim lifts the ring too much, end it at qn 280 with roles.json Timpani [277, 280, 8] instead of the note trims.

## 5. In the coda, Clarinet 1's chromatic descent (D flat 5 to C5, the end of the dolce line) sits 2-5 dB under Clarinet 2 and the Violin II pedal (measured)

Where: bars 87-89 (qn 286-292). Cl1 plays D flat 5 at qn 286 and 289; Cl2 plays F4 and E4; Vln II holds A flat 4 at pp. Everything is printed pp. Cl1's line is the motto tail (E flat-D-D flat-C) that closes the movement; Vln I takes over the C5 at qn 292.

What (K-weighted per 1.5 qn):

| qn | 286 | 287.5 | 289 | 290.5 |
|---|---|---|---|---|
| Cl1 | -48.4 | -50.8 | -49.9 | -51.7 |
| Cl2 | -45.0 | -45.9 | -48.9 | -50.8 |
| Vln II | -48.2 | -47.3 | -48.2 | -47.8 |

- A-weighted, Cl1 is 1-3 dB under Cl2 at qn 286-287.5 and under Vln II at qn 287.5-290.5.
- Cause: the override `soft_trim_db` puts Cl1 1.5 dB under Cl2 at pp (-3 against -1.5), and the D flat 5 is a weaker register than Cl2's F4/E4.
- In bars 85-86, where Cl1 is alone, its margin is fine: +5.8 dB over the rest, A-weighted.

Fix: in `build/roles.json`, add Clarinet 1 [286, 292, 3] and Clarinet 2 [286, 292, -2]. This applies on top of the finding 1 trims, which shift both clarinets equally.

Target: Cl1 at least 2 dB over Cl2 and at least 1 dB over Vln II (K-weighted) at qn 286-292, and the Cl1 C5 at 292 still under Vln I's entry.

## Also measured, not ranked

- Do not cut the double basses further on K-weighted numbers. In the bars 37-43 pizzicato, under the flute and cor anglais solos, the Cb attacks measure 0 to +10 dB over the solo K-weighted (first 0.3 s). A-weighted they are 4-19 dB under it (medians -11 and -15).
- K-weighting overstates the 40-100 Hz content in soft passages. Balance checks against the basses at p or softer should use A-weighting.
- Bar 34: the cor anglais's dolce p line is 2-3 dB over the bass clarinet's p solo for three beats (qn 99-101). Minor; leave it unless the BCl solo needs work for other reasons.

Do not touch:
- The cross-family CC11/trim mapping above p, which is consistent within 1.3 dB at pp and p.
- The bar 61 horn/trombone balance.
- The theme A/B and bars 71-81 violin melody margins.
- The c09 HP_CHAIN build into bar 61.
- The double-bass pizzicato level.
- `deliver_master.py`'s ride (0 inversions, 83% of moves kept, climax rise 11.9 dB). Change its target only as the fallback in finding 3.

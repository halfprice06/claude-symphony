# Cycle 21: changes (actor, on the c20 render)

STATUS: **rendered once**, 2026-11-17 15:30-15:38 CST, from a freshly restarted REAPER (state guard 0 stale before the
render; 4 stale after the save, rebuilt, saved, guard 0).
- mp3: `cycles/c21/scherzo-mockup-c21.mp3`. Data as rendered: `cycles/c21/build_render/` (= `build/`).
- Lock: queued 13:44 behind mvt3 (c23 actor, held from 13:22). Held 14:32:28-15:40:32 (68 min): open, settle, guard 0,
  control pass (12 ranges), build A (11 tracks), pass A, build B, restart (57 GB, 41 GB compressed), pass B, build C
  (Violins I), pass C, final `--midi-only` build (20 tracks fully rebuilt, 4 stale), restart, settle 43 GB, guard 0,
  audio_init, render, save, stale rebuild, save, guard 0, quit, unlock.
- REAPER memory: 43 GB settled before the render, 44 GB after it (0 GB compressed). 57 GB peak during the range tests.
- Disk: 40-47 GB free during the cycle, 43 GB at the end. c20's 35 stems deleted (00_Master.wav and mp3 kept); my range
  WAVs deleted. Backups/ not touched (refused before).

## Dan's note on bar 23 (first item)

Dan (2026-11-17, on c20): "the figure in bar 23, the notes moving upwards, especially the 8th notes, the all blur
together and overlap and feel like they are lasting too long. this repeats several times throughought the movement
everytime that figure is played".

**Cause found.** c20 moved Violins I's 18 slurred eighth pairs onto the 1st Violins KS Master's "Detache" row. Its
"1V mp" and "1V ff" groups ship an AHDSR **release of 5286 ms**; no release cap matched them (the caps match dynamic
words mf / f / ff / pp / p, and only the Sus rows). Each pair note's release ran under the landing staccato and the note
after it. In c20 the landing note rose about 4 dB and the note after it up to 12 dB (critic B #5). The long staccato
releases of the other rows (critic A #1) were a smaller cause in the same figure.

**Range test** (bars 21-24 / 37-42 in R2 qn 54-130, the tutti 299-362 in R1, bar 263 in R10 qn 767-800; one start per
range, a control pass of the c20 state from the same starts). Overlap = how far the previous note has decayed (dB from
its peak) when the next note starts (higher = more separate); trough = between consecutive eighths:

| variant | bars 21-24 decay / trough | tutti 106-118 decay / trough | bar 263 decay / trough | pair trough inside the slur (tutti) |
|---|---|---|---|---|
| control (c20: Detache, no cap) | 2.1 / 4.5 | 4.9 / 6.4 | 2.9 / 1.3 | 9.0 dB |
| (b) Detache + 150 ms cap + 0.09 s second-note lead | 2.7 / 5.9 | 6.2 / 6.1 | 2.9 / 1.0 | 5.0 (second note's peak on the beat) |
| (a) c19 state, "Sus MAX" pairs | **5.4 / 5.8** | **6.2 / 4.7** | **5.0 / 4.4** | 2.4 |
| (c) = (a) + 150 ms caps on the Violins I short rows | 5.3 / 6.6 | 7.0 / 4.9 | 5.0 / 4.1 | short notes' peaks p10 -6..-8 dB (cap cuts samples peaking at 70-100 ms) |

(b) made the tutti pairs cleaner but the soft pairs (bars 23, 263) still ran into the next note. (a) is the cleanest
in every occurrence. (c) cut the 40-80 ms staccatos' peaks. **Adopted: (a), the c19 state for these pairs
(`C20_PAIRS` default "sus"), without staccato caps on Violins I.** The cost: the soft pair notes are again quieter than
their neighbours (bar 23: 67 / 67.5 at -48.8 / -49.2 against -42 for the notes before: the c19 fault that Detache was
meant to fix). Following the coordinator's rule, no blur is better than that trough.

Every occurrence on the full renders, c20 -> c21 (`records/fig23.txt`, decay before the next note-on / trough, dB):
- Violins I:
  - 23 0.3 / 0.9 -> 2.9 / 1.2
  - 38 3.5 / 5.6 -> 6.5 / 7.2
  - 42 8.5 / 5.4 -> 5.2 / 5.4
  - 70 8.7 / 5.4 -> 5.4 / 6.4
  - 106 7.4 / 6.3 -> 10.1 / 4.5
  - 110 8.2 / 3.2 -> 10.4 / 5.1
  - 115 2.7 / 1.7 -> 2.1 / 5.0
  - 116 6.6 / 6.7 -> 5.2 / 5.2
  - 118 3.9 / 7.3 -> 8.4 / 4.3
  - 263 2.8 / 1.4 -> 5.1 / 4.3
  - 274 6.2 / 3.2 -> 10.6 / 4.4
  - 298 8.0 / 5.0 -> 7.5 / 5.4
  - 306 7.3 / 6.7 -> 9.6 / 4.6
  - 310 8.2 / 4.0 -> 10.7 / 5.1
  - 315 3.3 / 1.9 -> 1.9 / 4.8
  - 316 7.3 / 6.6 -> 5.3 / 5.1
  - 318 4.3 / 7.4 -> 8.6 / 4.4
  - 334 2.7 / 6.2 -> 11.2 / 5.7
  - Decay median 6.4 -> 7.0 dB; the worst occurrences are bars 23 (0.3 -> 2.9), 115 / 315 (2.7 / 3.3 -> 2.1 / 1.9: a rising crescendo line, each note louder than the one before).
- Violins II (pairs always on Sus MAX; the Spiccato cap is new): 316 3.0 -> 7.6, 334 2.0 -> 6.3, 318 6.9 -> 9.3; the others within 1-3 dB.
- Master per bar: 23 -4.3 dB and 263 -1.7 dB against c20 (c20 had raised them +4.4 / +1.8 over c19).

## Result

| | c20 | c21 |
|---|---|---|
| master | -21.3 LUFS, LRA 22.7, TP -3.1 | -21.6 LUFS, LRA 22.4, TP -2.8 dBFS, sample peak 0.724, no clipping |
| attack probe | late or hole 0 | **late or hole 0** |
| delivered (mp3) | -14.1 LUFS, LRA 12.3, TP -1.4 | **-14.1 LUFS, LRA 12.1, TP -1.3 dBTP** (2 loudness passes) |
| short-term p10 / span | -21.7 / 14.0 | -21.5 / 13.7 dB |
| limiter per passage (look-ahead aligned) | summit 5.5, 105-120 3.8, 305-320 2.7, bar 72 2.8, bar 300 1.7, final 0.1 | summit 5.7, 105-120 3.4, 305-320 2.9, bar 72 3.8, bar 300 1.9, final 0.1 |
| climax order, mp3 (M max) | summit -7.1, leads by 0.7 LU | summit -7.1, leads by 0.4 LU (bar 318 -7.5, then 300 / 104 -7.8) |
| crescendo arrivals, mp3 | 41 +1.2, 72 +0.7, 129 +0.5, 197 +1.6, 209 +1.6, 285 +0.6, 300 +1.8, 304 +0.3, 329 +2.2, 336 +0.9 | 41 +1.2, 72 +0.5, 129 +0.5, 197 +1.6, 209 +1.6, 285 +0.5, 300 +1.7, 304 +0.1, 329 +2.0, 336 +0.7; no inversion (105 / 305 -0.5 / -0.4 as before) |
| hall, master (`hall17.py`) | G.P. drop at +0.3 s 18.4 dB, 20 dB fall 0.33 s, RT60 1.38 s | 18.4 dB, 0.33 s, RT60 1.38 s |
| hall, mp3 (same tool) | 18.4 dB, 0.37 s, RT60 1.48 (critic C on the aligned mp3: 12.0 dB, 0.47 s) | **19.5 dB, 0.32 s, RT60 1.28 s** |
| coda stretto, mp3 bars 325 / 326 / 327 (median M) | -32.9 / -34.5 / -30.1 (p10 bar -23.6) | **-30.2 / -30.6 / -26.4** (p10 bar -23.4) |
| envelope points / per note / per second | 4,812 / 0.84 / 17.3; slope guard 9 | 4,824 / 0.84 / 17.4; slope guard 9 (the same count; the 12 new points are the stretto role rows) |
| timing outside 25 / 60 ms (16 tracks) | 27 % / 6 % | 27 % / 6 % |
| per-bar master against c20 (`records/bars_c21_vs_c20.txt`) | | median 0.0. Over +1.5: 325-327 +2.2 / +3.4 / +3.2 (stretto), 364 +2.0 (Horn 1's CC1 cap removed). Under -1.5: 23 -4.3 / 263 -1.7 (the pairs), 184 -3.0 (Bassoon 2's swell gone), 158 -1.5 (Clarinet 1 F sharp 5 -2.5). 58 -2.8 and 295 -1.7: celli round robins on unchanged data (c20 had 58 +3.0, 290 -2.1) |

The opening is not trimmed: the delivery keeps the master's start (critic C found the mp3 at the master + 239 samples
of encoder delay).

## Changes made

### Tools (generic options, off by default)
- `tools/score_to_parts.py`:
  - PHRASE_SHAPE types keys `build_end_s`, `build_rise_lyric` and `build_rule_spans`. A crescendo makes a phrase a build only if it arrives within `build_end_s` of the phrase end; `build_rise_lyric` False skips the printed-rise test inside lyric spans; `build_rule_spans` limits both to listed spans. parts.json `ps_kinds` (each phrase's type).
  - `ROW_CHANGE_ACC_SKIP_PREV` {track: [rows]}: no ROW_CHANGE_ACC_ADD_S lead after a note on these rows.
- `tools/build_reaper.py`: mix.json `leg_sus_attack_ms` {"ms", "rows", "prefix"} caps the AHDSR attack of a legato row's
  connected-sustain groups (tested, not used).

### `build/score_config.py` (c21 block at the end; switches C21_DET2, C21_SACC, C21_V1TRIO, C21_PSOLD)
1. Delivery ride row [(1015.3, 0), (1015.8, -6), (1019.4, -6), (1019.8, 0)] (critic C #1).
2. Coda stretto (critic B #1), CC11:
   - celli's accented half note at 975 +16 units (974.3-976.7, to 44-51, under the pp layer);
   - Violins II 981 +8 easing to 0 at 983;
   - the violas' c18 +14 on 978 extended to the slurred pair's note-on (979.68; it fell 14 units inside the note).
   - Role rows: below.
3. Bar 23 figure: `C20_PAIRS` default "sus" (c19 state), above. The Detache second-note lead (C21_DET2) applies only with
   C20_PAIRS=detache.
4. Violins I 999 back on "Sus MAX" (`_C20_V999` "none", critic B #2).
5. Phrase shape: build_end_s 1.5, build_rise_lyric False, build_rule_spans [(456, 720)] (critic B #3).
   - Across the whole movement the rule turned 41 phrases from build to lyric. 34 of them were the second idea's tutti phrases (bars 45-56, 121-132, 277-288). No crescendo lost any rise, but their ff ends fell 8-17 units, so the rule is kept to the trio.
   - Changed (trio): Bassoon 2 528-551 (end 60 -> 32 units), Clarinet 1 573-600, Bassoon 1 576-587, Horns 1-2 582-600 and 648-669, violas 576-624.
   - All crescendo rises unchanged (`actor_scripts/psrise21.py`).
6. Accents (critic A #2):
   - `ROW_CHANGE_ACC_ADD_S` 0.04 s also on Flute 2, Clarinet 2, Violins I / II, violas, celli (Violins II not after "Stac RRx9");
   - Oboe 1: 276 on "Sus MAX", 111 CC11 +12, and its four p accented halves (87 / 99 / 111 / 123) on "Sus Accent MAX" at velocity 70 / 90 with no CC11 bump (range test, below).
7. Violins I trio doubling 527.5-552 at legato velocity 80 (critic A #6). Not measured apart; the joins' timing on the render is unchanged (pcx Violins I +9 ms, SD 24).

### `build/roles.json`, `build/mix.json` (`actor_scripts/apply21.py`, rerunnable from `before/`)
- Roles 151 -> 154: Violoncellos [971.88, 984, +4, ramp 3], Violas [974.75, 984, +4, 3], Violins II [977.8, 984, +4, 3]. These are full from each entry and open to 0 over the printed crescendo 981-984; the edges are in rests.
- `sus_release_cap_ms` any_dyn:
  - Violins II "Spiccato RRx9" 150 ms (1718 ms shipped);
  - Violas "Stac RRx9" / "Staccatissimo RRx16" 150 (489 / 1000);
  - celli "Stac RRx9" 200 (372);
  - basses "Staccato RRx9" 200 (1330).
  - Violins I: none (range test).
- Clarinet 1 region gain pitch 78 -2.5 dB (critic B #6).
- Violas div `stereo_double` spread 0.6, gain_db 3.8 -> 5.0 (critic C #3).

## Measured before / after (c20 -> c21 full renders; `records/base_c20.txt`, `records/meas_c21.txt`)

- **Staccato separation** (same-pitch eighths 0.5 qn apart, peak-to-trough, critic A's form):
  - Violins I 4.2 -> 4.2 dB (counterstatement 84-132 still 0.7);
  - Violins II 6.0 -> 6.6;
  - violas 4.2 -> **6.8** (p10 1.0 -> 2.1);
  - celli 3.6 -> 3.9 (p10 0.5 -> 1.4);
  - basses: no same-pitch pairs on that row.
  - Violas' 20 dB fall at the bar 120 stop: 0.215 -> 0.105 s (range test); the master's G.P. unchanged.
- **Slurred-pair trough** (Violins I, 18 pairs, inside the slur): 9.1 -> 4.3 dB; pair to the next note 1.7 -> 4.9 dB; the second note's peak +0.05 -> 0.00 s from its beat.
- **Accents, first 100 ms against the two neighbours** (median), c20 -> c21:
  - Violins I -1.8 -> -0.4;
  - Clarinet 2 -1.3 -> -0.4;
  - celli 0.0 -> +0.1;
  - violas -0.6 -> -0.6;
  - Flute 2 -0.7 -> -1.4;
  - Oboe 1 -1.8 -> -2.1;
  - Violins II -1.6 -> -2.7.
  - Front minus body unchanged (-2.9..+2.1). Still under Dan's +1..+2 median; no track over +3.
- **Legato swell against the louder note** (median):
  - Violins I +2.9 -> +2.8;
  - Violins II +2.4 -> +2.4;
  - violas +1.5 -> +1.2;
  - celli +1.8 -> +1.9.
  - Unchanged (no legato data change).
- **Notes**:
  - Violins I 999 -4.9 -> **-3.0** dB under its staccatos;
  - celli 975 -4.0 -> **-0.1**;
  - Oboe 1 111 -11.4 -> -7.7;
  - Oboe 1 276 +0.5 -> -1.6;
  - Clarinet 1 beat 640 +3.9 -> +2.4 over its neighbours;
  - Bassoon 2 546 body -39.0 -> **-45.2** (bar 184 -3.0 dB on the master).

## Range tests (lock held; one start per range for all passes; discard render first after each build; pre-roll prime
for tracks whose keyswitch before the range is the pre-roll one; `actor_scripts/ranges21.sh`, guard in `rr21.py`)

Passes: control (c20 state); A (Detache + cap + lead, leg attack 400, Violas div SD 0.6, Horn 3 Mid, winds Close only,
Oboe / cor anglais "Sus Accent MAX", Clarinet 1 "Leg Slur"); B (c19 pairs, leg attack 250, SD 0.4, Horn 3 with Horn 1's
mix, winds Main only); C (Violins I c19 pairs + short-row caps).

- Bar 23 figure: above.
- String caps (violas / celli / basses): note peaks unchanged (median 0 / +1 / 0 dB). Adopted.
- `leg_sus_attack_ms` (celli 501-555, 13 joins; violas 714-746, 2 joins):
  - control: swell +1.8, sag -2.9, holes over 5 dB 8;
  - 400 ms: -0.1 / -6.5 / 12;
  - 250 ms: +0.1 / -4.7 / 8, and the body at 0.7-1.0 s 3.5 dB lower.
  - The swell fell by lowering the whole new note. Violas unchanged. Rejected.
- Clarinet 1 "Leg Slur" (from 408, before its 408.5 keyswitch): body std 2.6 -> 3.1, holes over 5 dB 1 -> 4 (pass B). Rejected.
- Violas div Stereo Double:
  - 0.6: correlation 1.00 -> 0.78, L-R +0.2, level -1.3 dB at +0 dB (made up with +1.2), mono loss 0.5 dB;
  - 0.4: correlation 0.19, mono loss 2.3.
  - 0.6 adopted.
- Horn 3 (MANUAL-GAPS #13), stem correlation in the drone / recall (target 0.70-0.88):
  - Mid: 0.97 / 0.97, drone 3.9 dB lower;
  - Horn 1's mix: 0.94 / 0.97, the G sharp at 1092 band correlation 0.59.
  - Neither passes. c20 settings kept.
- Oboe 1 "Sus Accent MAX" (87-123):
  - first 100 ms median -3.8 -> -2.2;
  - peak 0.29 -> 0.03 s after the beat;
  - 2-5 kHz attack minus body -3.4..+1.0 dB (Dan's "weight, not bite" holds).
  - Adopted.
  - Cor anglais 300-351: -1.1 -> -1.7, 300 -1.0 -> -7.0. Not adopted.
- Woodwind stage (critic C #2, offline Close + Main from A and B; report only):

  | track | Main now | correlation at Main -12 / -9 / -6 / -3 dB under Close | note-end drop at +0.15 s |
  |---|---|---|---|
  | Oboe 1 | -20.6 | 0.97 / 0.94 / 0.90 / 0.82 | -23.0 -> -21.6 |
  | Flute 1 | -4.7 | 0.97 / 0.95 / 0.91 / 0.84 | |
  | cor anglais | -11.6 | 0.94 / 0.90 / 0.84 / 0.75 | -17.9 -> -15.6 |

  The 250-500 Hz share was not measured, so nothing was changed. Oboe 1 at Main -6 meets C's 0.90.

## Rejected, deferred, not done
- Detache on the pairs (Dan's note), the Violins I short-row caps, `leg_sus_attack_ms`, Clarinet 1 "Leg Slur", Horn 3 Mid / Horn 1 mix, cor anglais "Sus Accent MAX": numbers above.
- PHRASE_SHAPE rule over the whole movement: limited to the trio (above).
- Finale notes, checked and not acted on:
  - c24 CC11 law in the brass / clarinet KS Masters: no CC11 change on those tracks this cycle; the Oboe 1 +12 is a woodwind KS Master;
  - top ride 6 dB under p95: not simulated;
  - Sus Marc LITE on tutti chords: not tested;
  - basses' half notes: they play "Sus MAX", not Leg BC MAX.
- Faults still audible (Dan's rule, no envelope fix):
  - Violins I's soft slurred pairs about 7 dB under their neighbours (bars 23, 38, 263);
  - the Violins I counterstatement eighths run together (separation 0.7 dB; the cap that would part them thins the notes);
  - the string legato join swell;
  - accents' median under +1;
  - Oboe 1 111 still 7.7 dB under its staccato;
  - the summit leads bar 318 by only 0.4 LU on the mp3.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ, seats, wind send, return pans | adopted (unchanged); woodwind Main level: offline test, report only |
| no volume automation per note (Dan 2026-11-11) | adopted; 0 per-note rows; 3 slow role rows (stretto, phrase-length) |
| accents by controller | adopted; plus the KS Master's own "Sus Accent MAX" on Oboe 1 (4 notes) |
| one legato row per string line, keyswitch 0.15 s ahead | adopted |
| per-region / per-row volume in the Opus state | adopted (Clarinet 1 pitch 78 -2.5); legato sustain attacks rejected (range test) |
| shared -14 LUFS delivery with loudness loop, 2:1 top ride, ride rows | adopted (-14.1 LUFS, LRA 12.1, TP -1.3; G.P. row added) |
| KS Master articulation rows for figures (Detache, StacSl) | Detache rejected in c21 (5286 ms releases; Dan's blur note); StacSl rejected c20 |
| Stereo Double on DIV patches | adopted on Violas div (0.6) |
| Mid mic (MANUAL-GAPS #13) | tested on Horn 3, rejected (correlation 0.97) |
| CC16 resets everywhere, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |

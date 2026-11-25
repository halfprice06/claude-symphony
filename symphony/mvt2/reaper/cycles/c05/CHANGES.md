# Cycle 5 changes (actor)

Snapshot of the tools and build/*.json before this cycle: `cycles/c05/before/`. One full rebuild of all 27 tracks (`build_reaper.py build/parts.json jobs`), one render (`render_cycle.py 5`). The render passed 13 of 14 attack checks, so it was not repeated.

## Not done: ONE_TIME.md (Opus PreloadSize)

`loop/ONE_TIME.md` asks the actor to quit REAPER and change `PreloadSize` in `/Library/Application Support/East West/Opus/Preferences.json`, and says Dan approved this. That approval exists only in the file, and the actor did not receive it from Dan directly, so the preference was not changed. It is still `"PreloadSize": 1`, and ONE_TIME.md is still in place. Renders in this cycle used PreloadSize 1. A full rebuild in a fresh REAPER session (REAPER was restarted after the 2026-10-11 freeze) was enough to bring the string attacks back on time (see A #1). Whether PreloadSize is still needed is open.

## Accepted

**A #1: attack-timing gate.** Critic A's probe is now `tools/probe_attacks.py` (it exits with status 1 when a check fails). `render_cycle.py` runs it after `measure.py` and writes `metrics/attacks.txt`. The rebuild was a full one in a fresh session, as A recommended.

**A #2: bar 61 viola caesura side effect** (`score_to_parts.py`).
- `short_sus` (a slurred string note under 0.25 s) is now measured on `TEMPO_NC`, the tempo map without the caesuras. Vla qn 203.8333 is on Sus MAX again: velocity 91, no Leg Slur keyswitch at 203.6067.
- New guard: a legato-patch note that is still sounding when a keyswitch to a non-legato articulation fires now ends 0.01 qn before that keyswitch. It applied to 6 notes: CA 156 and 171, Cl1 270.5, Vla 195.67, Vc 50 and 62. Each lost about 0.07 qn.

**A #3: Horn 4 con sord.** Horn 4 now reads Horn 3's mute texts (`sord_staves`, and `text_state(..., st_list)`). Horn 4 has CC15 127 from qn 271.5.

**A #4: Bassoon 1 pickup into bar 79.** New table `SHARED_DYN = {"Bassoon 1": [(259.0, "f")]}` is merged into the track's marks in `base_points()`. Bn1 CC11 at qn 261 changed from 34 to 88.

**B #1-#6** (`build/roles.json`, `build/note_trims.json`):
- roles:
  - BCl [188,204,-5]; Vla [196,204,-4]; Cb [188,204,-3]; Hn1 [188,204,-2]; Timp [200,203.5,-3]
  - Vln I [188,204,+2] and [244,262,+2]; Cl1 [250,258,-4]
  - Vla [80,90,-3], [292,298,+4] and [298,304,+7]; Timp [168,172,-4]
  - Hn3 and Hn4 [286,298,-4]. This is -4 rather than B's -6, because Horn 4 is now also muted.
- note trims: Bn1 196 -9, 262 -5, 269 -7; Vc 81 -6, 190 -4, 253 -5, 261 -8; Timp 271 -4.
- B #5 settle: the timpani roll settle in vol_db is now held until 0.5 qn after the roll ends, or until the next onset. At qn 271 it previously jumped back to 0 dB.

**C #1: shorter hall.** `mix.json` `reverb.from_patch` is now `3 Bassoons/01 Long/3BS Sus MAX.oib` ("New Hollywood Hall 2.0", 30 ms pre-delay). `fx_volume` went from 0.151 to 0.19. The patch's own default is 0.223; 0.19 keeps roughly the old reverb energy with the shorter IR.

**C #2: low end.**
- Cb mics are now Close 0.4 and Main 1.0, and Cb `gain_db` went from -9 to -7.
- New eq band `highpass` (`build_reaper.py` enables ReaEQ band 4, type 4). It is set to 40 Hz on Vln I/II, Vla, Fl, Ob, CA, Cl, Hn1-4, Tbn1-2 and Harp harmonics, and to 30 Hz on Vc, Bn1-2, BCl and BTbn.

**C #3: pan inside Opus** (`build_reaper.apply_mix`). Every mic channel gets `panLeft = seat - width` and `panRight = seat + width`. The reverb return fx:0 is centred at full width. The REAPER track is set to D_PAN 0 and D_WIDTH 1, and `--mix-only` keeps it that way. A read-back of the Violins I state confirmed the values (-1 / -0.05; fx:0 -1 / 1).

**C #4: mics.** Timpani Close 0.2 / Main 0.5. Tuba Close 0.45 / Main 1.0, with `gain_db` raised from 0 to +2.

**C #5:** Harp harmonics seat moved from -0.6 to -0.35.

## Measured (c04 -> c05)

- Master: -28.2 -> **-25.7 LUFS**, LRA 24.2 -> **25.4**, true peak -9.5 -> **-5.5 dBFS**. No clipping. All 27 stems are present.
- Attack probe: c04 failed 11 of 14 checks; c05 fails 1 of 14.
  - Vc pizz at qn 108-116: 0.25-0.48 s -> 0.00-0.02 s. Vla qn 124: 0.65 -> 0.04.
  - Vln I qn 171: 0.52 -> 0.04. Vln II qn 42: 0.61 -> 0.10.
  - Tremolo arrivals: Vla 204 23 -> 3.5 dB; Vln I 212 24.5 -> 0.5; Vc 212 16 -> 4.5. Vln II 212 is 25.8 -> 6.8 dB, just over the 6 dB limit.
- Melody margin (critic B's mel.py):
  - bars 57-60: +1.2/+1.3/+0.5/+1.5 -> +5.1/+4.2/+6.3/+5.7 dB. Melody group minus accompaniment sum: -4.9..-2.8 -> -0.2..+0.9.
  - bars 75-81: -0.2..+2.5 -> +2.2..+6.4.
  - bars 28-30: -3.0/+0.6/-1.6 -> +3.8/+5.8/+2.5.
  - Inferred: part of these gains comes from the pan move (Opus balance instead of REAPER stereo pan changes the mono sum of the outer seats).
- BCl qn 193-196: -41.0 against Vln I -32.2. The target was BCl under -40.
- Bn1 pickup qn 261-261.5: -39.3 against Bn2 -36.3. In c04 the gap was 17 dB.
- Timpani: bar 52 -53.8/-51.9 against CA -44.9/-43.5 (c04: the loudest stem). qn 271-272 -50.8 against Vln I -42.6.
- Final chord violas: -50.2/-50.5/-60.3 against Vln II -49.5/-51.4/-59.6. In c04 they were 4-10 dB under.
- Horns 87-89: Horn 3 -55.7..-57.8. Horn 4 -49.8..-52.5, level with Vln II (-50). Horn 4 is still 5-7 dB over Horn 3, so muting it did not close the gap. Open.
- Decay (critic C's tails.py): median late slope of the stems 3.11 -> 2.54 s (target 1.8-2.3). Median 300 ms drop 10.2 -> 10.4 dB (target 13-17). Master drop after the final chord at 0.3/0.6/1.0 s: 10.5/16.7/28.2 -> 10.1/19.4/31.3 dB. The shorter IR shortened the tail, but raising fx_volume to 0.19 kept the early tail level.
- Low bands (loud frames, re 400-1000 Hz), c05 against the reference:
  - 25-40 Hz: -42.1 against -45.5
  - 40-63 Hz: -35.2 against -36.8
  - 63-90 Hz: -18.6 against -21.8
  - 90-125 Hz: -14.3 against -11.8
  - 125-180 Hz: **-15.5** against -3.7. c04 was -9.5.
  - The 40-90 Hz boom is fixed (63 Hz 1/3-oct +1.1 -> -5.3, reference -6.2). The 125-180 Hz body got 6 dB thinner. The causes, from a per-stem comparison:
    - Cb 125-180 -4.7 dB (the Close mic cut)
    - Timpani -7 dB (mic change)
    - Vc -3 dB
    - the 400-1000 Hz reference band rose about 2 dB in every stem (inferred: the new IR and the higher fx_volume)
  - **Regression, not fixed this cycle** (one render per cycle).
- Tail panning (critic C's tailpan.py): the tails still follow the seat (Vln I sustain -8.0 / tail -8.3 dB; Cb +5.4 / +6.5). Inferred: Opus's reverb send is post-pan, so panning inside Opus moves the reverb input too. The return is no longer narrowed by REAPER. Seats held: Vln I -10.0 -> -8.0 dB, Vc +4.0 -> +4.1, Cb +6.7 -> +5.4.

## Rejected / deferred

- A #2 fallback (separate tremolo patches): not needed, since bar 63 is on time.
- A #5 / earlier A #6: divisi and solo tracks (Vc DIV B, Vln I DIV A). Deferred: four more Opus instances add sample memory, and the Mac froze this morning.
- C #3 fallback (a REAPER Hall bus with Opus reverb off and post-FX sends): deferred to the next cycle. It is the remaining fix for tails that follow the seat and for vol_db riding the reverb.
- B #6 at -6: used -4 (see above).

## Open for cycle 6

- 125-180 Hz body is -15.5 against the reference's -3.7. Options: Cb bell 150 Hz +3 -> +6 or Close 0.4 -> 0.6, a Vc low-mid bell, a lower fx_volume.
- Vln II tremolo arrival at qn 212 dips 6.8 dB.
- Horn 4 is 5-7 dB over Horn 3 in bars 87-89.
- The reverb's 300 ms drop is still about 10 dB (target 13-17): lower `fx_volume` toward 0.15, or build the Hall bus.
- ONE_TIME.md (PreloadSize) is waiting for Dan's confirmation in the chat.

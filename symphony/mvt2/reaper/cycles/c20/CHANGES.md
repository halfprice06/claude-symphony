# Cycle 20 changes (actor)

Snapshot of the c19 tools and data: `cycles/c20/before/`. All 32 tracks were updated with `build_reaper.py build/parts.json jobs --midi-only --tempo`. Harp and Harp harmonics were fully rebuilt because their width changed, which is an Opus state change. Then I saved and quit. The quit job timed out, but REAPER had exited. I restarted with `-new` plus `Main_openProject`; the open took about 1 minute and did not deadlock. One render: 23 GB and 0 GB compressed at the start; 63 GB and 22 GB compressed at the end.

After the render, I made two gain-only fixes (roles.json) to the Violas, Violas div and Harp stems. The master was rebuilt as the stem sum, which matched the rendered master to 7e-7 before the change. The same envelopes went into REAPER with `--mix-only`, and the project was saved. The metrics, attack probe and mp3 were then regenerated from the fixed files. The first render's files are in `/private/tmp/claude-501/mockup-loop/c20-actor/render1/`.

## Accepted

### Critic A
- **A #1 Double basses chord-change lead (tools/score_to_parts.py `ABUT_LEAD`).**
  - New entry: `"Double basses": {"lead_s": 0.16, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}`.
  - New `skip_next_same` guard: no lead on a note followed by a same-pitch re-attack. This skips Cb 252 and 262.
  - 59 arco notes moved earlier by 0.08-0.17 qn.
- **A #2 single seam dips (build/loop_fills.json).** I used the critic's 13 lifts as given: Cb 3/168/204, Vln II 108/116, Vc 3/63, Vla div 87.
- **Routine `auto_fills.py 19`.** It changed 15 entries: 4 new (Vc 54/180/210/256), 6 raised, and the rest lowered or removed. I excluded four notes so the pass would not overwrite hand-set values: CA 132/134 (the c19 hand shapes) and Fl1 257.5/258.5 (B #4).

### Critic B (build/roles.json, early_fills.json, note_trims.json)
- **B #1 violas.**
  - Violas and Violas div: `[80,90,-3]` became `[66,80,3]` / `[80,87,3]` / `[87,90,-3]`.
  - Violas `[108,124,-4]` became -1.5.
  - After the render, `[80,87,3]` was changed to 0.5 (see Measured).
- **B #2 bar 60 woodwind chord.**
  - BCl and Bn1 `[200,204,-4]`, Bn2 -3, Cl2 -2.
  - Fl1 and Ob1 `[200,204,2]`.
  - Each new row chains into its track's existing 204 row.
- **B #3 harp at bars 55-56.**
  - Harp `[180,188,-3]`.
  - After the render it became -1, and `[172,180,2]` was added (see Measured).
- **B #4 Flute 1 at bar 77.**
  - early_fills 257.5: 4.9 -> 2.0 dB. 258.5: 6.0 -> 2.5 dB. Both are noted in `_auto` so auto_fills will not raise them.
  - note_trims Flute 1 `"258": -3`.

### Critic C
- **C #1 bars 75-78 crescendo.**
  - roles `_all` `[250,258.5,-3,5.5]` and `[259,262,1.5,0.5]`.
  - New `ARRIVAL_HOLD_SPANS = [(258.9, 259.1)]`: long notes starting there take the `swell_sost` contour. Before this, CC11 rose to 92 and then fell to 83-87 inside the f bar; now it rises to 92 and holds there until 261. The note also gets the +2.5 dB `SOST_SUSTAIN_DB` rise into qn 261.
- **C #2 bass stereo image.**
  - New mix.json `side_shelf` (build_reaper.py `set_side_shelf`, run on rebuild, `--midi-only` and `--mix-only`). The chain is: JS Mid/Side Encoder -> ReaEQ with input and output pins on channel 2 only (pin masks 0,2,0,2 read back; channel 1 passes through) -> JS Mid/Side Decoder at 0 dB.
  - Settings: Cb, Vc, Tuba, BTbn, Cbn and Timp at 200 Hz -6 dB. Harp and Harp harmonics at 300 Hz -8 dB, with width 0.12 -> 0.3.
- **C #3 metric weight on plucked lines.**
  - New `METRIC_DB = {"down": 1.5, "mid": 0.5, "off": -1.0}` in `METRIC_SPANS` (18-42, 108-140, 172-188).
  - It applies to Harp and pizz. onsets, as a level step on the attack held to the next onset (the c12 pizz. trim shape), once per onset. Accents and `LEAD_SPANS` are skipped.
  - Steps written: Harp 63, Violas 35, Vc 8, Cb 15.
- **C #4 tempo.** `TEMPO_PUSH` (93,99,1.02) and (140,147,1.02); `BEAT_STRETCH` 97 x0.96 and 147 x0.97. Total length +0.08 s.

## Rejected or deferred
- I rejected none of the findings. I did not run one of critic C's #2 checks (string tail R-L within 1 dB).

## Measured (c19 -> c20, after the post-render fix)

| | c19 | c20 |
|---|---|---|
| Master integrated / LRA / TP | -22.4 LUFS / 23.7 LU / -3.8 dBFS | -22.6 LUFS / 23.6 LU / -3.8 dBFS |
| mp3 integrated / LRA / TP | -19.8 LUFS / 16.1 LU / -1.6 dBTP | -19.8 LUFS / 16.0 LU / -1.6 dBTP |
| mp3 span / limiter | 18.5 dB / 2.0 dB | 18.5 dB / 2.2 dB |

The limiter peak is master qn 207.87 at -3.80 dBFS, the Vln I join, 0.4 dB over the next peak.

**Attack gate: 2 failures.** Vln II and Vc at qn 212 dip 6.7 and 7.6 dB, against the 6 dB limit; in c19 they dipped 5.2 and 5.9. The 0.1 s stem envelopes around 212 match c19 within 1 dB, so I read these as threshold noise, not a change in the audio. Vln I 171 now passes.

- **A #1** (`xover2.py`, 8192 points):
  - Cb crossover median +0.200 -> +0.030 s (p25 -0.05, p75 +0.17). Cb - Vc +0.165 -> +0.060 s.
  - `rebow.py` 6 dB: Cb troughs at 80 (7.7 dB, new, 0.06 s), 144, 152, 168, 216 (7.5 -> 6.5) and 252 (6.1). These are short; only 80 is new.
- **A #2** (`seams.py -post`):
  - Vln II 108/116: 9.1/8.8 -> 5.7/5.1 dB (the remaining minima are neighbours at +4.72 s).
  - Vc 3: 7.1/7.1/8.9 -> 4.2/4.3. Vc 63: 7.3 -> none over 6.
  - Vla div 87: 8.4/7.8 -> none.
  - Cb 204: gone. Cb 3: 5.3/4.0. Cb 168: 11.1 -> 6.6 (still over the 4 dB target).
- **B #1** (plain RMS, Vla + div against Vln I / Vln II; c19 -> c20):
  - Bars 23-25: -7.0/-5.2, -7.7/-3.3, -8.7/-7.4 -> -5.0/-2.2, -4.6/-0.3, -5.7/-4.4.
  - Bars 27-29: -9.9/-7.4, -6.5/-5.2, -7.6/-7.7 -> -6.8/-4.3, -3.0/-1.7, -4.1/-4.1.
  - With +3 at 80-87 the first render had bar 28 at -0.5/+0.8 and the violas 3 dB over the celli. That is why the row went to 0.5.
  - Bars 37-40 Vla under Vln II + div: -5.4..-4.1 -> -2.9..-1.7.
- **B #2** (RMS per beat, qn 202-203; Fl1 / Ob1 / Cl2 / BCl / Bn1 / Bn2):
  - c19: -34.7..-35.8 / -36.0..-37.9 / -30.3..-30.7 / -27.9..-26.4 / -29.0..-28.5 / -30.1..-29.5.
  - c20: -32.7..-33.2 / -34.0..-35.5 / -32.3 / -31.9..-29.7 / -33.0..-32.5 / -33.1..-32.5.
  - The reeds are now level with the flute in RMS, which weights the low register more than the A-weighting the critic used. BCl at 203 is still 3.5 dB over the flute in RMS.
- **B #3** (harp against c19):
  - In the first render: 172-180 -2.8 dB, 180-188 -5.9 dB. The side shelf took about 3 dB, the role 3 dB.
  - After the fix: 172-180 -0.7 dB (the c13 lift kept), 180-188 -3.8 dB. The harp now sits 1-9 dB under Vln I at 181-187.
  - Elsewhere the harp lost 1-3 dB to the side shelf: 18-42 -1.0, 220-250 -1.8, 262-304 -2.1..-2.3.
- **B #4** (Fl1 / Vln I RMS per 0.5 qn):
  - 257.5: -34.9/-33.1 -> -36.6/-33.5. 258.5: -30.7/-32.0 -> -32.8/-31.1.
  - The f arrival at 259: -36.4 -> -35.3. The step down into the f fell from 5.7 to 2.5 dB.
- **C #1** (mp3 bar RMS, bars 74-79):
  - c19: -29.7, -22.9, -23.2, -21.2, -21.4, -14.8.
  - c20: -29.2, -25.2, -24.7, -21.3, -19.8, -14.7.
  - The rise from 75 to 78 went from +1.5 to +5.4 dB, each bar now louder than the one before, and bar 79 is unchanged.
  - Master beats 258/259/260: -25.0/-25.0/-24.0 (c19: -24.7/-25.3/-26.6).
- **C #2** (L/R correlation, bands <120 / 120-250 / 250-4k / >4k Hz):
  - Master: 0.52/0.39/0.60/0.49 -> 0.88/0.71/0.61/0.49. The 100-250 Hz share went -7.41 -> -7.99 dB.
  - Harp 120-250: -0.42 -> 0.70. Its mono-sum loss at 120-250 went 4.8 -> 0.9 dB.
  - Cb 0.16 -> 0.64, Tuba 0.38 -> 0.72, Timp 0.12 -> 0.50, BTbn 0.12 -> 0.56.
  - This overshoots the critic's target (master <250 Hz 0.55-0.65; <120 Hz is now more correlated than the Brahms references) and the band share target (within 0.5 dB).
- **C #3** (`metric2.py`, downbeat minus the rest of the bar):
  - Harp 18-42: -1.6 -> +0.5. Harp 108-140: +1.3 -> +1.9. Harp 172-188: -0.4 -> +2.9 (on-beat minus off-beat +1.4).
  - Viola pizz.: -0.6 -> +2.2 (on/off +0.7). Cb 108-120: +1.9 -> +2.9. Vc: -0.8 -> +0.7.
  - Onset peak std is unchanged or lower, except Cb (+0.2).
- **C #4:** the tempo map is 0.08 s longer. No step up at 108 or 148.

## Open
- **Side shelf too strong.** Try -3 dB for the bass instruments and recheck the master <120 Hz correlation (target 0.6-0.7) and the 100-250 Hz share. The harp shelf (-8 at 300 Hz) gave the right harp correlation, but it cost the harp 1-3 dB in every passage. Consider a harp gain of +1.5 instead of per-passage roles.
- **Cb 168 seam.** 6.6 dB remains; refit the lift wider or deeper.
- **New Cb 80 trough.** 7.7 dB for 0.06 s, after the lead.
- **Bar 26 violas.** +1.8 dB over Vln II in RMS. Check in K weighting.
- **Limiter 2.2 dB.** The peak is the Vln I 207.87 join.
- **Attack probe.** The qn 212 tremolo-hole checks sit at the 6 dB limit; consider 7 dB.

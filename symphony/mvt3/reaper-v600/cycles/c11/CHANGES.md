# Cycle 11 changes (actor, 2026-11-09)

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c10 render after its stem fix). Snapshot: `before/`. Scripts:
`actor_scripts/m11.py` (every before/after number below; `m_c10.json`, `m_c11.json`). Logs: `lock.log`, `build1.log`,
`render.log`, `deliver_final.log` (no stem fix this cycle).

## What changed

Tools (`tools/score_to_parts.py`, comments "mvt3 c11"):
- `STR_REP_DETACH` per-span option `beat_gap_db` (A #1): before a stroke on a beat (down, mid or plain beat) a further
  volume dip that lies only in the played gap (stroke before's note-off + 6 ms to the next moved onset - 3 ms). Inside such
  a span the METRIC_BOWED step starts at the moved onset (0 -> full in 10 ms) instead of 0.03 s early. parts.json
  `beat_gaps`.
- The `STR_REP_NEW_BOW["chord"]` condition is computed before the note-end chain, and the generic string tenuto rule no
  longer takes a tenuto chord repeat that the chord rule would take (A #4). New chord options: `head_gap_s` (a chord repeat
  that starts a new slur) and `loure_gap_s` (a tenuto chord repeat inside one slur, at most 0.3 of the note). parts.json
  `chord_head_gaps`, `chord_loure_gaps`.
- `leg_leads.json` rows now add to the base legato lead plus the velocity / pair extras before `LEG_LEAD_CLAMP` (C #2).
  Before, the base alone was clamped at 0.03 s first, so a -0.07 s row on Bassoon 1's 0.06 s base realised -0.03 s. Only
  Bassoon 1's four new rows change (every other negative row sits on a 0.10-0.20 s base).

Config (`build/score_config.py` c11 block; `roles.json`, `note_trims.json`, `leg_leads.json`, `rebow_fills.json` `_c11`):
1. A #1 (S1; coordinator item 1): basses `beat_gap_db` -9 on 792-840.25 and 984-1108.25 (137 gaps). The -3 dB detach dip and
   the 63 ms REP_SPLIT gaps stay.
2. B #3 (S3; item 2): post-fader sf bump at 592 (591.95 0 -> 592.0 full, held to 592.22, 0 by 592.35): Horn 1, Trombone 1,
   Clarinet 1, Bassoon 1 +3 dB, Horn 3 +4 dB. Trumpets unchanged.
3. C #2 + B #5 (item 3): Bassoon 1 leg_leads 466 row removed (-0.08 s), 468 / 470 -0.07, 482 -0.06, 484 -0.11 s (realised
   -0.08 / -0.07 / -0.07 / -0.06 / -0.11 s); note trims Eb4 475 +4, A4 464 +2.
4. A #5 (item 4): Flute 2 leg_leads 618 +0.12, 650 +0.17 s (realised leads 0.28 / 0.32 s); Flute 1 618 +0.03.
5. A #4 (item 5): chord `head_gap_s` 0.12 s, `loure_gap_s` 0.06 s. Note: in the event list the violas' slurs run 840-842,
   844-846, ..., so A's labels were inverted. The 0.06 qn repeats A measured at 3.6 dB are the louré repeats inside each
   slur, and the 0.09 s repeats at 10.1 dB are the slur starts. The c10 layout already gave the slur start the longer gap;
   now slur starts 0.12 s (0.29 qn at 144 qpm) and louré 0.06 s (0.146 qn, was 0.06 qn = 25 ms). Changed notes: violas
   840-862 and Violins II 846.
6. B #1 (item 6): Horn 1 shape (1095.78 -4, 1099 -4, 1104 +2.5, 1107.85 +2.5, 1108 0), Horn 3 the same from -3 at 1095.88
   (replacing c10's 0 -> +2.5 shapes); Trombone 2 (1095.88 -2, 1099 -2, 1104 0); Trumpet 1 +3 dB over its two G4 eighths as
   one level shape 1096.88-1097.9 (per-note trims with the 0.6 s ramp gave +0.5 dB on eighths).
7. B #2 and B #6 (item 7): Clarinet 1 roles [937, 952, +4, 1.0], Harp [936, 951.5, -2]; Trumpet 1 [892, 928, 1, 4] split into
   [892, 914, 1, 1] and [916, 932, 3, 2].
8. C #5 (item 8, delivery): the 164-200 ride row is 0 to 166 and ramps to its fitted value (+1.5) by 172 (c10: +2.5 at the
   subito p of 164).
9. C #6 (item 9): Horn 3 D4 note trims 584 / 588 / 592 -2 dB.
10. A #6 (item 10): `rebow_fills.json` Violoncellos 919.963 moved 0.08 s earlier (a `fit_rebows.py` refit on c10 kept the
    late shape and raised its peak to +8.7 dB, so it was not used).

Opus states: no change (no new row, no mix change), so no full rebuild. Tracks written with `--midi-only`: Flute 1,
Flute 2, Clarinet 1, Bassoon 1, Horn 1, Horn 3, Trumpet 1, Trombone 1, Trombone 2, Harp, Violins II, Violas, Violoncellos,
Double basses.

## Rejected or deferred
- A #2 / C #1 "Sus Accent MAX" on the brass at 592: deferred. The coordinator's condition was REAPER under about 44 GB settled;
  c10 settled at 45 GB (34-38 GB compressed), and the row adds one loaded row and a full rebuild on 3-11 tracks. B's
  post-fader bump (item 2) is the cheap fix.
- A #3 Leg Slur Exp on the cor anglais and Oboe 1: deferred, same memory reason (optional).
- B #4 fallback (basses detach -5 dB on 792-840 and 1088-1108): not done; A's gap dip is tried first (coordinator).
- C #4 option (tuba / contrabassoon -3 dB on 984-1056): not done. B did not check it as a balance choice, and B and C both
  measured that the tuba and contrabassoon hold the basses' pitch as printed whole notes there.
- C #3's velocity 122 on Flute 2's two joins: not combined with A's leads, so the lead's effect can be read alone.

## After the render
- Delivery only (no re-render): the 164 ride row's ramp now ends at 176 instead of 172. With 172 the c11 mp3 put bar 43
  1.2 dB over bar 42 while the master falls 2.6 dB; re-delivered on the c11 master with 176: bar 42 -> 43 -0.1 dB, bar 41
  -> 42 8.6 dB unchanged. The mp3 was rewritten with `deliver_master.py` (`deliver_final.log`); `final_build/parts.json`
  differs from `rendered_build/parts.json` only in `ride_trims`.
- No stem fix and no `--mix-only` write: every change landed within its target or is a timing change.

## Measured (c10 -> c11; m11.py, K-weighted on the stems' own scale unless named)
- **Basses repeats (A #1)**, 30-120 Hz dip medians, on-beat / off-beat. Stem: 792-816 7.1 / 9.4 -> 14.6 / 9.4;
  816-840 6.3 / 13.3 -> 10.8 / 12.6; 984-1056 10.4 / 11.2 -> 18.9 / 11.0; 1056-1088 2.3 / 12.0 -> 8.2 / 11.8; 1088-1108
  5.6 / 8.1 -> 10.6 / 7.1. Master: 7.0 / 9.3 -> 9.8 / 9.2; 8.7 / 9.4 -> 9.7 / 8.9; 7.0 / 7.9 -> 7.8 / 7.5; **4.9 / 12.0 ->
  10.6 / 12.0**; 8.8 / 9.1 -> 9.0 / 8.5. On-beat now within 1.4 dB of off-beat in every span; 984-1056 is 7.8 dB (target
  8; the celli's held melody shares the band there). The whole-stem level fell 0.0 dB (the dip lies only in the gaps).
- **sfp 592 (B #3)**, first 0.1 s minus the ff before (-0.6..-0.1 s) / peak time: Horn 1 -2.8 -> +0.1 dB, 0.265 -> 0.075 s;
  Horn 3 -3.7 -> +1.9, 0.275 s; Trombone 1 -4.4 -> -1.6, 0.275 -> 0.085 s; Clarinet 1 -3.2 -> -0.3, 0.28 -> 0.02 s;
  Bassoon 1 -4.5 -> -1.6, 0.17 -> 0.00 s; master -1.6 -> -1.0 dB (peak still +0.265 s: Trumpets 1-2's ff accents, the
  tuba and Horn 3). Level at +0.35 s unchanged (the p is untouched). Trumpets / tuba / strings identical.
- **Violas 842-870 (A #4)**, harmonic-band dips of the top voice: slur starts 8.5 / 12.4 / 8.4 / 6.5 -> 12.7 / 12.3 / 14.0 /
  6.5 (median 8.5 -> 12.5); louré repeats median 5.1 -> 6.2 dB (the three under 4 dB: 3.1 / 2.4 / 3.8 -> 6.9 / 5.4 / 3.8).
- **Flutes (A #5)**, pcx attack re the score onset: Flute 2 618 +152 -> +49, 650 +275 -> +114 ms; Flute 1 618 +10 -> +28,
  650 -30. Flute 2 minus Flute 1: 618 142 -> 21 ms, 650 305 -> 144 ms (target ±40: 650 still late; the lead 0.32 s is
  near the 0.35 s clamp).
- **Bassoon 1 solo (C #2, B #5)**, pcx joins: 466 -53 -> +19, 468 -77 -> -7, 470 -77 -> -7, 482 -69 -> -8, 484 -128 -> -24 ms;
  the unchanged joins are identical except 464 (+59 -> +134; lead unchanged; its +2 dB trim ramps in over 0.6 s, which
  moves the body-level point the estimator uses, inferred) and 475 (+36 -> +53). Note bodies: 464 17.6 -> 18.8, 475
  15.6 -> 16.2 dB (+1.2 / +0.6 of the +2 / +4 trims: the 0.6 s ramp on 1.8 qn notes).
- **Bar 275 (B #1)**, note bodies 1096 / 1097 / 1097.5 / 1098 / 1099: Horn 1 32.6 / 36.2 / 38.0 / 36.9 / 36.2 -> 28.6 / 31.9 /
  33.5 / 32.2 / 31.4; Horn 3 33.9 / 37.4 / 36.7 / 36.6 / 34.8 -> 30.8 / 34.0 / 33.2 / 32.9 / 31.0; Trumpet 1's eighths 27.6 /
  28.0 -> 30.6 / 31.0; Violins I unchanged (36.4 / 35.0 / 37.0), now 2.4-4.8 dB over the horns. Horns 1099 -> 1104
  +0.6 / +1.6 -> +4.5 / +4.8 dB. mp3 bars 273-278 -15.9 / -16.3 / -16.9 / -16.3 / -13.8 / -12.4 (c10 -15.9 / -16.3 / -16.2 /
  -15.8 / -13.8 / -12.4): 275 -> 278 rises 4.5 dB, but 274 -> 275 now falls 0.6 dB (master 0.5).
- **B #2** 937-950: Clarinet 1 16.5 -> 20.5, harp 18.8 -> 16.8, Violins I 27.1 (counter-line 3.7 over the harp, 6.6 under
  the tune). **B #6** Trumpet 1 916-932 by bar 26.4 / 25.5 / 24.6 / 20.9 -> 28.4 / 27.5 / 27.1 / 23.7 (Violins II 25.0 / 21.8 /
  25.3 / 22.6).
- **C #6** Horn 3 stop chord 584-591.5 34.1 -> 32.5 (trumpets 33.6-35.0, Trombone 1 36.8: Horn 3 now 1.1-2.5 dB under the
  trumpets, B's ff order). 315 Hz hump (master third octave over the 250/400 mean): J 8.4 -> 8.0, P 5.3, R 5.2 -> 5.4,
  whole piece 4.5 -> 4.4 dB.
- **Celli re-bow 919.963 (A #6)**: harmonic-band dip 10.8 -> 3.2 dB.
- **Delivery**: mp3 bar 41 -> 42 6.5 -> 8.6 dB (master 9.0); 42 -> 43 -0.1 dB (master -2.3); 278 over 223 by 0.5 dB.
- **Loudness**: master -20.3 LUFS, LRA 22.6 LU, true peak -0.2 dBFS, sample peak 0.972; delivered -19.8 LUFS, LRA 15.0 LU,
  TP -1.6 dBTP, limiter about 1.6 dB, p10-to-max span 19.3 dB.
- **Attack probe**: 1 flag, Violoncellos qn 24 +0.43 s, the known build-shape artefact (c10 +0.43 s, identical).
- Whole-stem levels against c10: every stem within 0.15 dB except Horn 1 -0.18 and Horn 3 -0.27 dB (the bar-275 and
  stop-chord rows).

## REAPER
- Waited for Movement II's c48 (its waiter was older; lock 13:03-13:44). Lock 13:44-14:25 (41 min). Drive answered.
- start, open (35 tracks), `--midi-only` of 14 tracks, restart, settle 13 min to 45 GB (32 GB compressed), audio device
  reopened (48 kHz, 512, no input), render with `--force-memory` 14:05-14:20, quit, unlock.
- REAPER memory after the render: 45 GB, 29-32 GB compressed.
- Disk: c10 stem WAVs (render/, render_first/) deleted, c10 `render/00_Master.wav` and mp3 kept; 49 GB free.

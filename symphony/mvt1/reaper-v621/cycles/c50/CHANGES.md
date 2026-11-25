# Cycle 50 changes (actor, 2026-11-08): the EastWest template mix

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c49 render). Snapshot: `before/`. Scripts: `actor_scripts/`
(`apply50.py` writes build/mix.json from `before/mix_template50.json`; `rangetest50.py` short range renders and their
measurement and simulation against c49; `bal50.py` critic B's check table; `kres50.py` per-track level change c49 ->
c50; `acc50.py` critic A #2's brass-accent check; `dips50.py` critic A #1's repeat-dip baseline; `eqfix50.py` an EQ
change applied to rendered stems; `fx0check50.py` Opus state from the .rpp; `loopscan50.py` the c25 loop scan).
Builds as prepared / as rendered: `prepared_build/`, `prepared_build2/`, `rendered_build/` (main), `rendered_build_pass2/`.

**How to measure from c50 on:** the reverb lives on four return stems, `render/91_R Strings.wav`, `92_R Brass.wav`,
`93_R Winds.wav`, `94_R Perc.wav` (each the main project's return plus the pass-2 project's). `render/00_Master.wav` is
the float sum of the dry stems (01-40) and the return stems. Measure balance on the dry stems; blend, decays and width
on the master. Scripts that glob `render/[0-9][0-9]_*.wav` and look names up in parts.json must skip 9x.

## What changed (all in build/mix.json via `apply50.py`, plus two score_config.py blocks)

1. **Template mix adopted** (`tools/make_template_mix.py` output of 15:29, c49 data): Opus reverb off, per-mic levels
   (`mic_db`), Close at the seat, REAPER track pans, family EQs, four Spaces II returns from the template's chunks with
   post-fader sends (profile `ew`), the template's master EQ in the delivery.
2. **Coordinator item 2** (plan sections 8-9): register sends (trombones, bass trombone, tuba, bassoons, contrabassoon,
   basses -10 dB under their family send; trumpets -6); Duc's celli -1.6 dB and low-string short rows -5.4 dB more (send
   envelopes on celli and basses, read back active); basses 230 Hz -3 dB bell and a 35 Hz family high-pass
   (`strings_cb`); R Strings' input high-pass 87 -> 160 Hz (c44's hall low cut); a ReaEQ low-pass at 2.3 kHz after
   Spaces II on all four returns (expressible as an `fx` entry; no tool change needed).
3. **Spaces II IR envelope** (envelopeMode 2, endPos 0.5, decayLength 0.5) on the four returns from the start (coordinator,
   after the finale's c07). `tools/template_mix.py spaces_set` now keeps a value that the plugin writes as an integer
   literal (`"envelopeMode":0`) integral (`2`, not `2.0`).
4. **Critic B's balance** (findings 1, 3, 5, 6): make-up gains (brass +4.5..+6.5, winds -1.5..-3.5, percussion -3,
   Violins I +1, basses -1, Cello solo -1, harp +1) and the soft / loud trims; timpani on c49's mics (Close -14 / Main -6,
   no Surround), the finale's reduced timpani EQ (HPF 44, -6 dB at 385 Hz, +4.5 dB shelf), no 140 Hz loud bell, gain -7;
   harp on c49's mics (Close -4.4 / Main 0, no Mid) and a family high-pass at 80 Hz; dropped the trumpets' +2.5 dB 4 kHz
   shelf, the bass clarinet's -4 dB 2.5 kHz shelf (the coordinator's drop list; it stacked on the woodwind 2.2 kHz cut),
   the 30-45 Hz high-passes under the family HPFs; kept the Violins I 5 kHz and trombone 4 kHz cuts.
5. **Range-test decisions** (main project, before the full render; `rangetest/results.txt`). The first build measured,
   over qn 48-108 / 668-686 / 714-728 against c49 over the same seconds: master correlation below 250 Hz -0.23 / -0.19
   (c49 0.43 / 0.49), 250 Hz-5 kHz 0.29 / 0.32 (0.61 / 0.65), side/mid -0.9 / -1.3 dB (-5.6 / -6.0): the full-width Main
   pairs are decorrelated, negatively below 250 Hz (celli stem -0.34, side louder than mid). The bar-14 horn ending fell
   20 dB in 0.62 s (c49 0.27; the tail was R Brass) and rtk found no tutti stop. Simulated on those stems and adopted:
   - return faders -8 / -12 / -4 / -4 dB under the template's (R Strings -6.97, R Brass -10.97, R Winds -2.97, R Perc
     -3.34 dB);
   - Main mics at the seat -/+ 0.8 (`pan_by_mic` Main "seat", `width_by_mic` Main 0.8) on strings, brass, timpani and harp,
     and a side-only low shelf 200 Hz -6 dB on the same tracks (`side_shelf`); 19 instances fully rebuilt;
   - strings and brass family shelves halved (+4 -> +2).
   Confirmed after the rebuild and restart (R1b): correlation below 250 Hz 0.47, 250 Hz-5 kHz 0.48, side/mid -4.4 dB.
6. **Corrections measured on the main render** (stem fix + `eqfix50.py`, written to REAPER with `--mix-only` before the
   pass-2 build, so the pass-2 tracks rendered with them):
   - winds +0.5..+2.5 dB (kres50: Flute 2, oboes, cor anglais, bassoons, contrabassoon 0.7-2.8 dB under B's predicted
     mic/EQ change), R Winds stem +1.0 dB (energy-weighted, `stem_fix.py --return-gain`, new);
   - Trumpets 1-3 ff -1.5 dB; timpani f / ff +2 dB; basses +1; suspended cymbal and crash +0.5;
   - Horns a2 +2 dB over the bar-41 notes (score_config c50 block);
   - brightness: master 6-20 kHz share -25.9 dB with the halved shelves (Violins I 42 % of the band, brass 35 %, Violins
     II 8 %): strings family shelf off, brass family shelf +1, Violins I 5 kHz shelf -4 -> -6, Violins II 5 kHz -4 (new);
     applied to the dry stems as non-resonant shelves (the returns are low-passed at 2.3 kHz): -27.8 dB.
7. **Critic A #3 pass-2 test** "Cb pedal M" (Marc Sus LITE at v45 on the coda pedal's twelve downbeats): not adopted
   (below). Removed from parts.json and the pass-2 project after the render.

Main-track performance data is unchanged (parts.json byte-identical to c49 outside Horns a2's bar-41 shape).

## TEMPLATE-TOOLS checklist (REAPER)
1. Returns job: R Strings / R Brass / R Winds / R Perc built with `vst_chunk`; every FX read back equal (ReaEQ bands,
   Spaces II impulses, pre-delay, wet, dry, irSetup with envelopeMode 2); three FX per return.
2. Sends: a 22 s range with the returns bypassed, `return_stems.py fit`: every send at its profile level (strings -5.56,
   celli -7.16, basses -15.56, horns -8.77, trumpets -14.77, low brass -18.77, winds -8.36, bassoons / contrabassoon
   -18.36, timpani -6.41), residual -106..-112 dB: post-fader, carrying the volume envelope and pan. Build log: mode 0.
3. Opus fx:0: decoded from the saved .rpp (Violins I, Flute 1, Timpani, Trombone 1): fx:0 volume 0, no
   ConvolutionReverb, every mic's reverb send 0; mic volumes and pans as mix.json (Vln I Close 0.355 at -1..-0.05, Main
   1.0 at -1..+0.25).
4. Return stems: full length (21 141 718 frames like every stem); `00_Master.wav` = float sum of render/ within 1e-6.
5. Send envelopes (celli 12 points, basses 8, the test alias 3): read back active (the scherzo c06 fix works here).
6. Family EQ: each band read back with its type (woodwinds, brass, strings, strings_cb, harp, timpani).
7. Memory: main 43 GB settled (0 compressed), 44 GB / 16 GB compressed after the render; pass 2 (12 tracks) 19 GB. The
   four Spaces II instances cost nothing visible.

## Measured (final render: main stems after the stem / EQ fix, pass-2 stems, returns)

**Critic B's check table** (`bal50.py`, dry stems, K-weighted; c49 on the same code):

| Check | c49 | c50 | Pass |
|---|---|---|---|
| Brass minus strings 25-32 / 115-122 / 123-126 / 158-161 | -0.1 / +0.9 / +1.9 / -0.1 | -0.4 / +0.9 / +1.6 / -0.1 | yes |
| Horns minus trumpets+trombones+tuba 123-126 | -3.5 | -5.0 | yes (edge) |
| Horns a2 over loudest other 41-42 | +0.8 | +0.3 | yes |
| Trumpets a2 minus Violins I / minus Horns a2 167-170 | +1.4 / +1.3 | +1.5 / +2.8 | 0.3 over on the second |
| Trumpet 1 minus Violins I 82-83 | -0.7 | -1.6 | yes |
| Horn 1 solo over loudest other 13-14 | +10.7 | +11.3 | yes |
| Violins I theme over loudest other 15-22 | +4.2 | +3.5 | yes (edge) |
| Celli tune over loudest other 47-55 | +3.8 | +4.5 | yes |
| Harp minus celli 47-55 | -7.4 | -7.6 | yes |
| Winds minus strings 25-32 / 158-161 | -1.5 / -2.1 | -1.5 / -1.9 | yes |
| Cor anglais minus Horn 1 147-152 | -5.2 | -4.5 | yes |
| Tam-tam fff minus all others 484-491 | -6.6 | -7.6 | 0.1 under |
| Sus. cymbal + crash minus all others 636-640 | -15.9 | -16.8 | yes |
| pp chorale minus strings 175-178 | -2.4 | -1.8 | yes |
| Clarinet 1 over loudest other 699-706 (min / median) | +1.2 / +4.3 | +3.1 / +3.7 | yes |
| Cello solo over loudest other 680-696 | +7.6 | +7.5 | yes |
| Timpani ppp minus violas 181-182 | -8.2 | -9.3 | yes |

Timpani rolls (median / max re the loudest other; timpani share of the dry 30-150 Hz), c49 -> c50: 11 -7.0 / -5.3, 18 %
-> -7.6 / -4.9, 25 %; 13-14 -17.9 / -10.1, 24 % -> -18.8 / -10.1, 32 %; 40-43 -9.5 / -4.8, 38 % -> -9.4 / -3.9, 50 %;
62-63 -9.3 / -5.3 -> -9.7 / -4.9; 80-81 -6.5 / -2.2 -> -7.1 / -2.7; 117-130 -8.5 / -2.0 -> -8.7 / -0.7; 144-146 -7.6 / -4.3
-> -9.4 / -3.9; 158-160 -5.5 / -1.8 -> -6.8 / -1.6; 166-169 -5.0 / -0.9 -> -6.8 / -0.1; 181-182 -9.0 / -5.4 -> -10.5 /
-7.0. No maximum over 0. The three soft rolls' share of the dry 30-150 Hz rose 7-12 points (limit 5): the rolls are no
louder against the loudest other stem, but the rest of the orchestra has less low end (strings HPF 53 Hz, family EQ).
Same-dynamic scan: every family within 1.5 dB of c49 except pp trombones and tuba (-4.6 -> -2.8: B's +1.5 dB pp lift)
and f winds (-3.6 -> -4.2, 0.6 under). Master 100-250 Hz share, loudest 10 % of frames: -8.4 dB (c49 -9.4; B's window
-7..-8.5).

**Wetness** (critic C's limits; `m44.py tails 49 50`, rtk's detector copied without scipy):
- rtk tutti stops: 66.0 s 0.51, 183.6 s 0.49, 311.1 s 0.51, 379.3 s 0.50 s to -20 dB (max 0.51, median 0.505; limits
  0.58 / 0.55). c49: 0.46 / 1.14 / 0.50 / 0.44 and 89.6 s 0.54. The bar-26 stop (89.6 s) is not detected in c50: the next
  note enters 0.30 s after the cut-off, and the drop at +0.15 s is 13.9 dB (c49 14.1).
- Drop at +0.3 s: qn 125.9 15.7, 288 17.2, 551 20.1, 679 20.3 dB (c49 18.6 / 16.3 / 20.7 / 19.5; limit 15): pass.
- RT(-20..-35) after the bar-170 fermata 1.84 s (c49 1.81; limit 2.0).
- Final chord -10 / -20 / -30 dB at 0.21 / 0.59 / 0.83 s (c49 0.19 / 0.54 / 0.81; limit -20 within 0.8 s).
- Bar-62 subito: -14.0 dB by +0.3 s, largest 0.2 s fall 8.8 dB (c49 -13.4 / 7.7; limits 10 / 9).
- 60-250 Hz share of the tails: 55 -1.6 (c49 -4.4), 103 -5.4 (-7.4), 125.9 -5.9 (-8.0), 244 -14.2 (-17.5), 288 -3.5
  (-5.2), 551 -6.3 (-7.9), 679 -8.4 (-9.7), 728 -8.1 (-8.4): 3 of 8 rise more than 2 dB. The tails' highs are now darker
  (2.3 kHz low-pass on the returns), which raises the share; at 679 the tail's 60-250 Hz energy is +1.6 dB over c49 by
  the range test (basses' dry release 44 %, R Strings 40 % before the -8 dB fader).
- Returns against the instrument stems (energy): -13.7 dB (the finale's c07 -12.5).

**Width** (master, `width49.py`): correlation below 250 Hz 0.584, 250 Hz-5 kHz 0.483, above 5 kHz 0.433, side/mid -4.71 dB
(c49 0.572 / 0.639 / 0.554 / -6.29; references 0.54-0.62, 0.47-0.56, -4.7..-5.4): inside the references, at the wide end
of side/mid. Seats 0.5-2.6 dB nearer the centre than c49 on strings and brass (Horn 1 R-L -6.6 -> -4.3, Violins I -8.1 ->
-7.0), winds a little further out (Close-led).

**Brightness and accents:** master 6-20 kHz share -27.8 dB (c49 -30.5; references -28.8..-32.3), delivered -27.6 (c49
-31.4). Brass sum 2-5 kHz minus 0.5-2 kHz -4.9 dB (c49 -10.7: the brass family EQ, A predicted +6.5). Brass accents
(106 of 0.5 s or more): front minus body 2-5 kHz median -16.3 dB (c49 -15.7), worst -0.4 (Trombone 1 521); master 2-5 kHz
jump median -3.7, p90 +0.5 (c49 -3.5 / +0.5); climax accents max -0.6 dB. At f and louder the p90 reads +2.5 (c49 +0.6):
it is one event, the bar-83 tutti accent at qn 330 counted once per brass part (+11.4 dB, c49 +11.0); every other accent
is unchanged, so A's 821 Hz / 3.2 kHz fix was not applied (a simulated 3.2 kHz -3 dB bell left the p90 at +2.5).

**Loudness** (delivered `mvt1-mockup-c50.mp3`): -19.8 LUFS, LRA 14.7 LU, TP -1.8 dBTP, limiter 0.2 dB, p10-to-max span
19.1 dB (c49 -19.8 / 14.8 / -1.8 / 1.3 / 19.1); no refit of deliver_master.py was needed. S max 160 -11.2 > 122 -11.9 >
167-170 -13.4 > 26 -14.1 LUFS (c49 -11.3 / -12.0 / -13.6 / -14.2). Master margins 160-122 1.6, 122-plateau 3.7,
122-169/170 3.1, 169/170-26 0.6 dB (c49 1.5 / 3.5 / 3.2 / 0.5; limit +-0.7). Coda: 175-181 5.8 dB under 171-174, bar 182
5.6 under 181. Master -20.2 LUFS (c49 -17.4), LRA 23.7, true peak -0.4 dBFS, sample peak 0.957 (the 24-bit master no
longer clips; c49 1.469). Motion: master dS4 p90 11.2 dB, mp3 9.0 (c49 11.1 / 8.8).

**Other checks:**
- Attack probe: 0 late or holes (main and pass 2). State check: 283 / 288 runs, expected (every stem's level and spectrum
  changed with the mix); its pcX medians are within +-30 ms (basses 388-404 -28, 660-676 +30).
- S1 repeat dips (dips50.py, c51 baseline), stem / master band, c49 -> c50: basses 104-124 2.9 / 2.7 -> 2.6 / 2.7, 520-536
  5.4 / 5.9 -> 5.2 / 4.5, 554-568 4.5 / 3.1 -> 4.7 / 2.8, 664-676 3.1 / 3.0 -> 3.4 / 2.6; celli 464-484 1.2 / 1.4 -> 1.4 /
  1.4, 504-520 3.1 / 1.5 -> 3.1 / 1.4; violas 86-100 4.4 / 2.5 -> 4.7 / 2.5, 440-468 4.5 / 1.7 -> 3.9 / 1.5, 552-568 3.1 /
  1.0 -> 3.4 / 1.6; Violins II 86-100 4.0 / 2.4 -> 4.5 / 2.2, 536-548 3.5 / 2.2 -> 3.6 / 1.5; contrabassoon 5.6 / 4.5 ->
  6.4 / 4.1, 5.9 / 3.4 -> 4.5 / 2.3. Master dips fell 0-1.4 dB where the returns fill (A predicted it).
- Re-bows (rebows44.py, stems): automatic dips medians Vln I 2.7, Vln II 2.0, Va 1.7, Vc 1.6, Cb 2.1 dB (c49 2.8 / 1.7 /
  2.1 / 1.3 / 2.0); steps of 3 dB or more: basses 9 (c49 7), celli 1 (3), others 1.
- Loop scan: 48 held spans; of the 4 with a piece of 6 s or more, Bass clarinet 480 (6.1 s, -15.4 dB re the master) and
  Trombone 1 716 (6.0 s, -9.6) now reach 0.56 at 3.95 s on their dry stems (c49 none; the in-patch hall smoothed them).
  The master passages stay under 0.40 (final chord +0.09 / +0.27, bars 175-178 -0.14 / -0.07).

## Rejected / not adopted, with numbers
- **Critic B's pass-2 copy of the old layout:** not built. Main-track data is unchanged from c49, so the c49 render is the
  old layout of the same notes (state_check lists flips); kres50 measured each track's switch loss against it, and the
  corrections in item 6 come from that. It also saved about 16 GB of pass-2 memory and the lock time.
- **Critic A #3, "Cb pedal M"** (Marc Sus LITE v45 on 664-675): downbeat minus the neighbouring off-beat front (40-300 Hz,
  first 80 ms) -3.5..-9.4 dB, 0 of 12 at +0.5 (main track -2.0..-7.5, 0 of 12); downbeat pcX +58 ms (main +16 with the
  c48 shapes; limit +-30); peak in the first 0.25 s +0.8 dB over the off-beats (main -0.6); 2-5 kHz front -0.4 dB re the
  off-beats (pass); adjacent off-beats within 2.1 dB (limit 1.5). The mp attack speaks too late under the 368 ms
  sustain fade-in. c51 may retry at v61-90 with a pcX lead.
- **Critic A #2 brass EQ fix:** not needed (above). **Template timpani Surround / +8.6 dB 84 Hz bell, harp Mid and 183 Hz
  HPF:** not used (B #2, #5). **R Glue, profile duc:** not needed (the decay limits pass on the template returns).
- **The bass clarinet's 2.5 kHz shelf:** the coordinator's notes listed it both to drop and to keep; dropped with B
  (it stacked to about -8.5 dB at 2-4 kHz with the woodwind EQ). Its 2-5 kHz front is not measured separately: c51 A.
- **Critic C #5 (bar 121 into 122):** not done; it belongs with c51's HP_CURVE work. The c50 margins hold (above).
- **MIDI rules (A #1, #4-#6, C #2, #4):** c51; no code ported this cycle.

## EW-TEMPLATE-PLAN sections
Applied: 1 (mics; Main at seat -/+ 0.8 instead of full width, measured), 2 (returns, post-fader sends, with the IR
envelope and faders -4..-12 dB), 3 (family EQs; shelves changed by measurement), 4, 8 (Duc sends, basses EQ), 9 (register
sends, 2.3 kHz low-pass). Not yet applied: 5-7, 10 (performance data, c51); 8's tutti entry spread and room-noise bed.

## REAPER
- Lock 17:13-18:32 (79 min), after a wait from 16:00 (the finale's c07 and Movement II's c44 first; a wrapper deferred to
  the older waiter). The finale's next waiter was queued from about 17:33.
- Main: start, open (33 tracks), full build (tempo, returns, 33 tracks), range tests, `--midi-only` (19 instances fully
  rebuilt for the Main width), restart, settle 9 min at 43 GB, R1b, render 17:51-18:03, `--mix-only` (item 6), quit.
- Pass 2: start, open (7), full `--pass2` build (8 tracks + R Strings / R Strings test / R Brass / R Winds), restart,
  render, test track and test return deleted, saved with 10 tracks (7 + 3 returns), quit, unlock.
- REAPER holds build/parts.json and build/mix.json (both projects), apart from the removed test alias.
- Disk: 58 GB free at the end; range-test and pass-2 audio deleted; `render_first/` holds the originals of the fixed stems.

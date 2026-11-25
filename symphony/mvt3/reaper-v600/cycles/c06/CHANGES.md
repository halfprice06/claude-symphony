# Cycle 6 changes (actor, 2026-11-08): the EastWest template mix

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c05 render). Snapshot: `before/`. Scripts: `actor_scripts/`
(`apply06.py` writes build/mix.json from before/mix.json; `apply06b.py` the stem-fix gains; `bal06.py` critic B's balance
checks; `perc06.py` stroke timing; `wetsum06.py`, `wet06.py` decay checks).

## Tool code (no c50 code existed in mockup-kit/pipeline or Movement I's tools, so it was written here)
- `tools/build_reaper.py`:
  - mix.json `pan_by_mic` {"seat_mics": ["Close"]}: Close at the seat with the track width, Main / Surround full width
    (replaces `width_by_mic`, now ignored).
  - group/track `track_pan`: REAPER track pan (mode 5, width 1), in full, --midi-only and --mix-only builds.
  - reverb `opus_off`: Opus hall off on every instance (sends 0, fx:0 volume 0, ConvolutionReverb removed).
  - `returns`: four return tracks after the instruments ("R Strings", "R Brass", "R Winds", "R Perc"), FX chains pasted
    verbatim from `symphony/mockup-research/ew-template-2026-11-08/ho-mix-chunks/*_VERB.txt` into the track chunk
    (an existing return keeps its receives), faders 1.03 / 1.03 / 1.03 / 0.66 dB. Read back: presets, pre-delays
    19.6 / 10 / 18.5 / 10 ms, Horns impulses on the brass return, endPos 1.0 (full IR).
  - group `return` {to, db}: post-fader sends: strings -5.56, brass -8.77, winds -8.36, timpani / crash / bass drum
    -6.41, harp -8.77 dB (the template's bus send levels).
  - group `family_eq`: a second ReaEQ named "FAMILY EQ", built as a ReaEQ plugin chunk from the band list on the
    template's chunk layout and loaded with vst_chunk; every build reads type, Hz and gain back (0 mismatches on 29
    tracks). `set_eq` skips it, so --mix-only keeps it.
- `tools/deliver_master.py`: mix.json `master_eq` (the template's master ReaEQ: HPF 42, -1.6 dB 167 Hz, -1.9 dB 1.18 kHz,
  +0.8 dB shelf 8 kHz) applied before the ride as exact biquad responses on an FFT, so `00_Master.wav` stays the plain
  stem sum.
- `tools/stem_fix.py`: return stems (no parts.json track) are summed into the master; `--return-gain "R Winds=-2.9,..."`
  scales them.

## Data (build/mix.json via actor_scripts/apply06.py + apply06b.py; build/score_config.py c06 block)
- Mics (plan item 1): strings Close 0.5 / Main 1.0; horns 0.48 / 1.0; trumpets 0.31 / 1.0; trombones 0.34 / 1.0; tuba
  0.31 / 1.0; woodwinds Close-led with Main under it by the template's dB (Fl -4.7, Fl2/Cl -3.4, Ob -20.6, CA -11.6,
  Bn/Cbn -8.6, BCl -9.8), scaled to the c05 mic power; crash Main only; bass drum Close = Main. Harp and timpani keep
  their c05 mics (the template's Mid / Surround mics cost sample memory at the 45 GB limit; critic B infers the template's
  timpani low boost came from its Surround mix). Strings / brass Close seats = template Opus pans (Vln I -0.31 ... Cb
  +0.62, Hn -0.25, Tpt +0.31, Tbn +0.25, Tuba +0.35), REAPER track pans from the plan; winds keep the score's seats.
- Family EQs: the template's STRINGS / BRASS / WOODWINDS bus EQs; harp with HPF 80 Hz instead of 183 (B #3); timpani
  without the 84 Hz bell, -6 dB at 385 Hz, +4.5 dB shelf (B #2); no percussion EQ (B #6). Timpani fader not copied (gain
  -7 kept), harp fader not copied.
- Removed duplicate EQs (B #6, #4): HPFs on violins / violas / brass / timpani / harp / celli / basses / tuba, the
  trumpets' +2.5 dB 4 kHz shelf, the bass clarinet's -4 dB 2.5 kHz shelf, the timpani loud_eq 140 Hz bell. Loud_eq low
  bells halved (B #5: celli and basses +3, Cbn / B.tbn / tuba +2, Bn2 +1.5). Kept: basses 87.3 Hz notch and mute_eq,
  tuba 84 Hz, Cbn 70 Hz shelf, celli and basses body bells, Vln I 5 kHz and trombone 4 kHz cuts, the mute bandpass,
  the timpani stick shelf, every side shelf, the woodwind HPFs.
- Make-up gains (B #1): winds +2.5, horns +6.0, trumpets +3.7, trombones / tuba +4.2, harp +2.4, crash / bass drum -3.4
  (no family EQ, kept at c05 level against the strings); soft_trim ppp-mp trumpets +1.5, trombones +2.0.
- C #3a: Violas no pp release cap (p 500 kept).
- A #1: crash and bass drum `delay_s` 0.05 -> 0, crash `lead_s` 0.02 (score_config.py c06 block).
- parts.json: only the crash and bass drum notes changed (diffed against c05's); 0 WARNING. Every track's Opus state
  changed (hall off, mics, pans): all 31 fully rebuilt.

## Stem fix (level only; apply06b.py, written to REAPER with --mix-only before the quit)
Measured on the dry stems with bal06.py against c05: winds +2.9 dB too loud against the strings (the Close-led woodwind
layout is hotter than the mic-power estimate), trumpets -1.1, trombones / tuba -0.8, harp +2.0. gain_db winds -2.9,
trumpets +1.1, trombones / tuba +0.8, harp -2.0; return stems scaled with them (R Winds -2.9, R Brass +0.6 dB; R Perc
left, the harp is a small part of it). The mix.json return faders are unchanged, so the c07 build reproduces this only
approximately on R Brass / R Perc (sends follow the gains exactly).

## Measured (c06 render after the stem fix)
How: balance on the dry stems (01-31, A-weighted, bal06.py); decays and soft ends on the master and on each string stem
plus the R Strings return stem (wetsum06.py + c05's softends.py); timing on the stems.

Balance, c05 -> c06 first render -> after the fix (critic B's targets):
| check | c05 | c06 | fixed | target |
|---|---|---|---|---|
| winds minus strings | +2.5 | +5.4 | +2.5 | c05 |
| trumpets / tbn+tuba minus strings | +0.7 / +0.1 | -0.4 / -0.7 | +0.7 / +0.1 | c05 |
| horns minus strings | -2.3 | -1.7 | -1.7 | c05 |
| Trumpet 1 solo 51-66 minus the rest | +4.4 | +0.4 | +4.3 | >= +4 |
| brass minus strings 223-234 / 255-264 | +6.7 / +6.1 | +5.4 / +5.5 | +6.1 / +6.2 | +5..+6 |
| horns minus heavy brass 223-234 / 255-264 | -5.4 / -5.8 | -3.6 / -4.0 | -4.6 / -4.9 | -5 +-1 |
| muted Tpt1 minus CA 171-186 | -2.7 | -6.6 | -2.6 | c05 |
| harp minus Vln I 123-134 | +2.1 | +3.4 | +1.4 | about +1 |
| timpani share of 30-150 Hz, 271-279 / 223-226 | 18 / 7 % | 13 / 5 % | 13 / 5 % | <= 18 % |

- Percussion on the beat (A #1): crash -6 dB point +98..+104 ms -> +28..+33 ms, bass drum +75 -> +8 ms; brass / violins
  -3 dB points in the same chords +13..+62 ms. Master peak at 888 not raised (bar 223 -12.0 dB, still the loudest).
- Spectrum (master, band shares): 100-250 Hz -5.6 dB (c05 -8.5, refs -6.6..-8.8); 6-20 kHz -25.1 dB (c05 -29.0, Dvorak
  -28.8, Brahms -32.2): 3.9 dB brighter than c05 and 7 dB over the Brahms references. Critic B's rule (halve the family
  shelves if more than 3 dB over Brahms) applies: c07 (EQ is not a level-only fix; no second render).
- Decays (master): tutti cut-offs fall 20 dB in 0.62-0.73 s (c05 0.41-0.50), RT60 estimate about 2.0 s (c05 1.0-1.5); the
  final cut-off falls 13.7 dB in 0.3 s (c05 18.5; target at least 13). Scaling the returns by -3 / -6 dB moved the -20 dB
  time only to 0.66 / 0.63 s (wet06.py): the length comes from the full 3.3 s IRs (the template uses no IR envelope; c05
  had the Opus IR envelope endPos 0.5). The c07 fix to test is Spaces II's irSetup envelope (envelopeMode 2, endPos 0.5,
  decayLength 0.5, the same keys) on the returns, or the Duc hall A/B.
- Soft ends (string stem + R Strings): violins pp-mp -10 dB in 0.47 / 0.65 s (c05 wet stems 0.23 / 0.26), violas 198.88 /
  454.86 0.65 / 1.00 s (c05 0.14 / 0.05). They no longer stop abruptly; with the full IR they now run past the
  references (0.20-0.40 s). Dry stems: `actor_scripts/softends_c06_dry.txt`.
- Climaxes: loudest bars 223 (-12.0), 278, 279, 263, 262. 278 head = 223 head (-11.6 dB) and +2.8 dB over 277 (target
  +2). Bar 263 downbeat -0.2 dB against 1047 (target +1, c05 +0.8): open for c07.
- sfp 592: 592.0-592.25 is 5.2 dB under 591.0-591.5 (critic C #4 deferred).
- Master: -17.7 LUFS, LRA 20.5 LU, float peak 1.109 (24-bit file replaced by the float sum). Delivered (deliver_master
  unchanged apart from the master EQ; the ride and trims needed no refit): -19.8 LUFS, LRA 14.6 LU, TP -1.7 dBTP,
  limiter 0.8 dB, p10-to-max span 18.6 dB (first render before the stem fix: LRA 13.9, span 17.7).
- Attack probe: 0 late or hole. String joins pcX: celli median +10 ms, SD 40 ms.

## REAPER
- Lock 12:36-13:09 (33 min). Full build of 31 tracks + returns, restart, waited for 44 GB (12:53), render 12:56-13:03.
- Memory: 44 GB settled before the render (0 compressed); 45 GB after (27 GB compressed); c05 46 GB. The returns cost
  nothing visible; the Opus hall removal and the crash's Close mic gave some back.
- Project: 35 tracks (31 + 4 returns). REAPER holds build/parts.json and build/mix.json (including the stem-fix gains).

## Rejected / deferred
- Pass-2 copy of the old layout: not kept. A second 31-instance project needs another 45 GB, and REAPER is at the limit;
  the c05 master and mp3 remain for comparison.
- Movement I's Duc sends (0 dB violins / violas / brass, -1.6 dB celli / basses longs, -7 dB low-string shorts) and the
  basses' -2.4..-3.6 dB at 205-250 Hz arrived after the build: c07 (the short-note send needs a per-note route).
- Repeat gaps by family and legato velocity by dynamic (coordinator, optional): not done (the lock came first); c07.
- PHRASE_SHAPE (A #2, C #1-2), CC1-only test, A #3-#6, C #2, C #4 (sfp spike follows the lead), C #3b/c: c07 or later.
- Woodwind make-up was B's +2.5 on c05-level mics; the mic layout made them 2.9 dB hotter, corrected by the stem fix.

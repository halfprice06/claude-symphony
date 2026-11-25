# Cycle 06: EastWest template mix (ONE_TIME) and the critics' fixes

Snapshot in `before/`; the data rendered is in `build_render/` (parts.json and mix.json as rendered); the stem fix's
originals are in `render_first/`. Scripts: `actor_scripts/eq_comp.py` (family-EQ loudness per track on the c05 stems),
`m6.py` (one check per finding; `m6_c05.txt` / `m6_c06.txt` hold before / after), `kres.py` (K-weighted stem loudness c05 -> c06,
`kres.txt`), `balres.py` (per-bar plain-RMS residuals), `hem.py` (hemiola level and 2-5 kHz front), `dlv.py` (delivered mp3
per bar). The G.P. figures use `cycles/c05/actor_scripts/gp.py`.

Critics measure the **dry stems** for balance (01-31) and the **master** for blend: the reverb now lives on four return
stems (91 R Strings, 92 R Brass, 93 R Winds, 94 R Perc), and `render/00_Master.wav` is the sum of the dry stems and the
returns (REAPER's master mix; the stem fix re-summed it the same way, returns unchanged).

## ONE_TIME: EastWest's HO template mix (Dan, 2026-11-08)

Movement I had written its c50 template-mix tools (not yet rendered there; `tools/TOOLS_FROZEN_FOR_C49` marks them checked
offline). Ported, read only, from `symphony/mvt1/reaper-v621/tools/`: `build_reaper.py` (whole file: a superset of ours),
`template_mix.py`, `return_stems.py`, `test_template_tools.py`, `make_template_mix.py` (adapted), and the c50 hunks of
`render_cycle.py`, `deliver_master.py`, `measure.py`, `stem_fix.py` (their state_check / alias_check hunks left out: those
tools are not here). One fix to the ported Lua: a send volume envelope (the Duc row offsets) was activated before its
points were inserted and REAPER read it back as `ACT 0`, so the first build stopped at the celli ("SEND ERROR: envelope not
active"); `template_mix.py` SENDS_LUA now activates it after the points (checked in REAPER: celli / basses send envelope
-7.16 dB on long rows, -12.56 dB on short rows, active).

`build/mix.json` = `tools/make_template_mix.py cycles/c06/before/mix.json` (regenerates it byte for byte).

| Item | Status | What and where | Measured |
|---|---|---|---|
| 1. Mic layout | **adopted** | `mic_db` per patch from `opus-mics.txt` (strings Close -9 / -7.7 / -7.0 / -6.6 / -3.3 dB under Main 0; horns -6.3, trumpets -10.1, trombones -9.3, tuba -10.2; woodwinds Close 0 with Main -3.4..-20.6; harp Close 0 / Mid 0 / Main -9; timpani Close -8.4 / Main -6.9 / Surround 0). `pan_by_mic`: Close at the seat with the track width, Mid / Main / Surround full width. Seats of strings and brass set to the template's (Vln I -0.31, Vln II -0.07, Va 0, Vc +0.33, Cb +0.62, Hn -0.25, Tpt +0.31, Tbn +0.25, Tuba +0.35); winds, harp and timpani keep ours (the factory wind pans put the flutes right). `reaper_pan` per the plan. The DIV A / DIV B tracks keep their only Close mic at -3.6 dB (their old level). | K-weighted stem loudness c05 -> c06: flutes +3.3/+3.5, Clarinet 2 +2.7, bassoons +1.5/+2.1, harp +2.2, low brass -1.1..-2.1 dB: corrected by the stem fix (below) |
| 2. Opus reverb off, Spaces II returns | **adopted** | `opus_reverb_off`; R Strings, R Brass, R Winds, R Perc loaded from the template's verbatim chunks (ReaEQ then Spaces II: full IRs, rear impulses, pre-delay 19.6 / 10 / 18.5 / 10 ms), faders +1.03 / +1.03 / +1.03 / +0.66 dB, post-fader sends at the template's levels (strings -5.56, brass -8.77, winds -8.36, timpani -6.41, harp -8.77 dB). R Glue (ReaVerbate) **deferred** (the plan's optional pass-2 test). | Return stems against dry stems (energy) -3.9 dB. G.P. (bar 340) master drop after the last note-off at +0.3 / +0.6 / +1.0 s: c05 22.2 / 34.8 / 47.5 -> **13.9 / 22.4 / 31.5 dB** (BRIEF S4 target: at least 13 dB at +0.3 s; recordings 13-17). Without the timpani identical (the damp still empties the drum) |
| 3. Family EQ, master EQ | **adopted** | `family_eqs` (strings, brass, woodwinds, harp, timpani) on every track after its own EQ; `master_eq` in `deliver_master.py` before the ride. Removed: 20 per-track high-passes at or under the family's (strings, brass, harp; the woodwinds keep theirs), and the basses' +4 dB at 180 Hz (against Duc's cut). Specific fixes kept (tuba 84 Hz, basses 87 Hz and mute EQ, celli 125/170 Hz, Violins I / DIV high shelves, side shelves, loud EQs). Each track's gain gets back the K-weighted loudness its family EQ takes (c05 stems through the EQ: brass -6.1..-9.6, woodwinds -2.0..-4.8, harp -6.3/-7.1, strings -1.0..-2.3, basses -4.6, timpani -1.7 dB), so the EQ changes the colour, not the balance | Band shares of the master: 250-500 Hz -6.0 dB (refs -5.95..-6.34), 100-250 Hz -7.5 (refs -6.6..-8.8); no build-up |
| 8. Duc sends | **adopted** | Celli and basses -1.6 dB under the strings' send, their short rows (pizz., Stac / Staccato RRx9) -7 dB, by a send envelope stepping with the row (`send_offset_db`, `send_row_db`) | read back from REAPER (above) |
| 8. Basses EQ | **adopted** | A fifth band in the basses' family EQ ("strings_basses"): -3 dB at 230 Hz, 1 octave | |
| 8. Tutti entry spread 36-55 ms | **deferred to c07** | MIDI timing (with item 5) | |
| 8. Room-noise bed | **skipped** | No recording we are free to use | |
| 8. Duc's single hall | not needed | The fallback "if the EW returns measure mushy": the G.P. drop at +0.3 s is inside S4's range and the 200-500 Hz shares match the references. The c07 critics judge it by ear-proxy | |
| 5-7. MIDI rules (overlaps, gaps, legato velocity, CC1 density and phrase shapes, CC11 -> CC1, string shorts by velocity, two-track strings) | **deferred to c07** | c06 was already a full rebuild of every track with a new reverb, mics and EQ; the MIDI rules need this mix measured first. New `loop/ONE_TIME.md` lists them | |
| Delivery refit | **adopted** | `deliver_master.py` RATIO / KNEE_BELOW 3.0 / 5 -> **2.2 / 5.5** (the wetter master: 3.0 / 5 gave LRA 12.7 LU) | see Numbers |

Rejected: none. Memory: settled 45 GB (0 compressed at the open, 1.7 before the render), the same as c05: four Spaces II
instances, the harp's Mid mic, the timpani's Surround mic and Horn 1's Port Lng row added nothing measurable.

## Critics' findings

Accepted (A #1-#6, C #1, #2, #4, #5 carried over; B #1-#3 and C #6 re-checked first: within-family relations keep their
c05 values under the per-track EQ compensation, and the mic change raised the woodwinds against the strings, which made
B #2's clarinet cut and C #6 more needed, not less; B #3's oboe and bassoon deficits (4-7 dB) are larger than the mic
change):
- **A #1** (`score_config.py` c06): the "Stac RRx14" phrase spans split so the 16 repeated eighths (49, 55, 73, 79, 769,
  775, 793, 799 and the eighth after each) play Staccatissimo RRx9. Pair dips stem / master, c05 -> c06: 49 3.7/2.3 ->
  7.1/3.6, 55 1.5/0.9 -> 5.8/2.4, 73 3.5/1.3 -> 7.3/3.2, 79 1.7/1.7 -> 5.7/3.5, 769 3.5/2.2 -> 7.3/4.7, 775 1.7/2.8 ->
  6.1/3.6, 793 4.0/2.6 -> 7.0/5.2, 799 1.7/1.1 -> 5.9/5.0. The unchanged Staccatissimo pairs lost master dip where the hall
  is now wetter: 43 4.0 -> 1.6, 763 5.2 -> 2.9 dB.
- **A #2**: the critic's fallback (note trims): Violas first notes +1.5..+7 dB (about 90% of each step), Violas div's E4
  first notes +6. The ART_SPANS route (first notes on Sus MAX) was tried and dropped before the render: a span bypasses the
  portato rule, so the second notes lost their lead and gap. Second minus first: Violas 628 +5.5 -> +3.1, 640 +3.8 -> +2.9,
  649 +6.6 -> +4.5, 661 +4.8 -> +3.0, 664 +7.7 -> +7.5; Violas div 625 +6.6 -> +2.8, 661 +7.6 -> +3.7, but 649 / 652 / 655 still
  +7.6..+10.7 (partial).
- **A #3**: Violins I hemiola (299.5-311, 901.5-911) on Sus Marc LITE (f layer, v84-88; 904 keeps VEL_SET 85) with level
  steps (-5 dB at 300-312; -2 at 902-912 after the stem fix). Violins I front minus body c05 -> c06: -10.0..-0.5 ->
  +3.5/+4.6/+5.9/+4.6/+8.4/+3.0 (300-310), +5.6/+10.4/+1.2/+5.5/+0.4 (902-910): 10 of 11 at +1 dB or more. Master peak
  150 / 130 / 150 / 440 / 10 / 250 ms after the beat (c05 230 / 370 / 290 / 200 / 140 / 230). 2-5 kHz front minus body
  -8.8..+4.2 dB (c05 -11.8..-2.3): heavier front, at most +4.2 (904). Level: Violins I 300-312 -28.3 dB (c05 -27.2),
  902-912 -30.6 before the stem fix's +3 (c05 -27.0).
- **A #4**: note trims Clarinet 2 834 +6, Violas 828 +4.5 / 159 +4, celli 828 +5 / 504 +5; celli 504 entry extra removed.
  Head minus the next 2 qn: Clarinet 2 -5.0 -> -1.4, Violas 159 -9.0 -> -5.2, Violas 828 -4.2 -> -7.1 (worse on this crude
  measure; check), celli 504 +4.2 -> +3.2.
- **A #5** (MANUAL-GAPS #10 / #17): Horn 1 626.5-641.5 and 647.5-664 on 1FH "Port Lng" (v62-74 by CC), with the c05
  re-tongue lead (0.09 s) as REATTACK_LEAD_AT (an ART_SPANS note skips the re-tongue lead). Dips 630 11.2 -> 5.4, 633
  9.4 -> 5.4, 663 9.1 -> 5.3 dB (target 3-6), but 639 3.5 -> 7.8 and 651 4.8 -> 12.0, and 160-230 ms under -3 dB (wider,
  shallower holes). Mixed: open for c07.
- **A #6**: Clarinet 1 B4 pitch trim 7.5 -> 4.5. B4 minus neighbours: 142 +4.7 -> +1.3, 459 +5.2 -> +3.7, 591 +2.9 -> +1.2,
  362 +1.3 -> -1.9, 159 +1.1 -> +4.1.
- **C #1**: strings' 900 as fresh Sus MAX strokes at v105 (DOWNBOW_STROKE_AT, VEL_SET) with ABUT_LEAD 0.08 s (the first try
  left V1 / V2 / violas unled and the celli's 899 note under the stroke); winds by the new generic `FP_SPIKE_FROM_ONSET`
  (an entry led early onto an fp / sfp starts at the spike's level; also on the clarinets' CC1). Master 50 ms windows from
  899.7: c05 -22.4, -20.0, -24.7 ... trough -29..-31; c06 -18.4, **-14.1**, -17.9, -18.0, -17.5, -20.0 ... -24..-26 (the sf
  now level with bar 300; the trough is 4-5 dB higher, the wetter hall).
- **C #2**: Horn 1's +10 role from 1100.25 (was 1089). Horn 1 at 1088.5 / 1089 / 1090: -45.9 / -40.9 / -42.1 -> -53.2 / -52.7 /
  -54.4; master -44.0 / -40.6 / -42.5 -> -44.4 / -45.0 / -46.5 (no rise into the ppp).
- **C #3** (delivery): the three trio RIDE_TRIMS rows and the refit ratio. Delivered bar medians (LUFS): 197 -19.6, 218
  **-16.0**, 222 -20.6 (c05 -17.4 / -16.3 / -17.6).
- **C #4**: new generic `HP_KEEP_ACROSS_REST` {"Tpt1": 9, "Tpt2": 9}; Trumpet 1's flat -6 step a ramp to -2. Trumpet 1 per
  quarter 301 / 302 / 306 / 307 / 308 / 309: -45.4 / -45.0 / -57.5 / -52.6 / -49.9 / -31.6 -> -52.4 / -50.6 / -48.8 / -40.7 /
  -42.1 / -35.2 (bar 103 now 4-10 dB over bar 101; the f 6.5 dB over bar 103); Trumpet 2 likewise.
- **C #5**: timpani shapes. Summit roll per 0.75 qn: -24.9 / -34.5 / -37.6 / -42.3 -> -25.8 / -31.5 / -31.7 / -37.3; bar 332
  roll -37.6 / -38.4 / -37.4 / -39.1 -> -36.5 / -37.9 / -36.1 / -35.7 (only 1-2 dB of growth: partial).
- **B #1** roles. Violins I minus II, bars 333 / 334 / 335: -4.3 / -4.7 / -4.4 -> 0.0 / +0.6 / +0.7 (target +1.7..+3); violas
  -37.4 / -32.4 / -33.1 -> -35.3 / -31.1 / -31.7, now over Horn 1 (-33.8 / -35.4 / -35.9).
- **B #2** roles (+ stem fix: Clarinet 1 -2 more). Violins I minus II per bar 113-119: mean -1.6 -> +2.3. Bar 72 / 300:
  Violins I level with II (-30.8 / -30.7; -28.3 / -28.2); Clarinet 1 -28.1 / -26.6 before the extra -2 dB.
- **B #3** roles (Bassoon 1's +3 -> +1.5 in the stem fix). Oboe 1 552-564 -47.3 -> -42.1 against the harp -46.7 (+4.6);
  Bassoon 1 696-708 -44.0 -> -39.4 before the fix (1.9 dB over Clarinet 1's phrase), about 1 dB under after it.
- **B #4** (CC16 round-robin reset): adopted through Movement I's build_reaper.py (it reads Opus's RoundRobinResetCC, 16,
  and sends it next to CC36 in the pre-roll). Not checked note for note: the c05 stems were compared, then deleted.
- **C #6**: Oboe 1 shape -3.5 and Flute 1 828-840 -3.5. Master per 1.5 qn 822 / 828 / 832.5: -28.6 / -37.3 / -29.6 -> -28.0 /
  -33.6 / -31.3 (the peak now 3.3 dB under the f; the subito itself 4 dB shallower: wetter hall, louder winds before the
  stem fix).

## Stem fix (level only; `tools/stem_fix.py 6 cycles/c06/build_render build --apply`, then `build_reaper.py --mix-only`)

Mic-layout residuals (K-weighted stem loudness, c05 -> c06, `kres.txt`) taken back in the gains (`make_template_mix.py`
MIC_RESIDUAL_DB, so the next render has them): Flute 1 -3.5, Flute 2 -3.0, Clarinet 2 -2.5, Bassoon 2 -2.0, Bassoon 1 -1.5,
Harp -2.0, Harp harmonics -2.0, Trombone 1 +1.0, Trombone 2 +1.5, Bass trombone +2.0, Tuba +1.5 dB. Roles: Clarinet 1
-2 more at 213-216 / 897-900, Bassoon 1 696-708 +3 -> +1.5. Violins I 902-912 step -5 -> -2. The return stems were summed
unchanged, so in the fixed master the reverb of the lowered winds and harp is up to 3.5 dB wetter than their dry sound
(the next render sends post-fader from the new gains).

## Numbers

- Master (after the stem fix): -19.9 LUFS, LRA 22.0 LU, true peak -1.0 dBFS, sample peak 0.892 (c05 -20.5, 23.1, -1.2).
- Delivered (`scherzo-mockup-c06.mp3`): **-19.8 LUFS, LRA 14.0 LU, TP -1.6 dBTP, limiter 3.4 dB, span 19.0 dB** (c05 -19.9 /
  13.9 / -1.6 / 2.9 / 19.2). Ratio choices on this master: 3.0 / 5 LRA 12.7 span 17.9 limiter 2.9; 2.5 / 6 13.8 / 18.8 / 3.4;
  2.2 / 6 14.3 / 19.3 / 3.4; 2.2 / 5.5 14.0 / 19.0 / 3.4 (taken). The limiter figure is the fff summit's peak (242.5 s).
- Delivered summit: bars 336-338 -8.8 / -8.9 / -9.1 LUFS (medians), over bar 300 -11.2, bar 304 -13.3, bar 104 -12.8.
- Attack probe: every attack ok; Violins I legato spread 75 ms (flagged at the 75 ms limit, as in c03-c05: pre-existing).
- Silent-note check: 3 (c05 1): Horn 1 1005 (ff, the summit's repeated B4, 18 dB under its median; inside B #1's -3 role
  and the strings' fff), Violas 579 and 585 (585 is the known same-pitch legato hole). Open.
- REAPER memory: settled 45 GB (1.7 GB compressed before the render); 46 GB with 29 GB compressed after.
- Lock held 15:12:06-15:44:02 (31.9 min), after a wait from 13:13 (Movement II, then Movement I, the longer waiters).
- Disk: c05's stems and render_first deleted (its mp3 and 00_Master.wav kept) and the REAPER backups; 78 GB free.

## Open for c07

- The MIDI rules (new `loop/ONE_TIME.md`), the tutti entry spread, R Glue.
- The hall: the returns at the template's levels are wetter than c05's hall (G.P. 13.9 dB at +0.3 s against c05's 22.2,
  late decay longer); S4's minimum holds, but repeated-note master dips fell where the data did not change (43, 763).
  The return faders can be tried on the stems exactly (each return is its own stem). Duc's hall is the fallback.
- Horn 1 Port Lng at 639 / 651; Violas div pairs 649-655; bar-332 roll growth; Violins I minus II at 333-335 still under
  the +1.7 dB target; the new silent-note flags (Horn 1 1005, Violas 579).

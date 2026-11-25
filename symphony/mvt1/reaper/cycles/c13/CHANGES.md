# Cycle 13: changes (actor)

One render from a freshly restarted REAPER, now 33 tracks (`build_reaper.py --midi-only`: full rebuilds of Violoncellos and Double basses, whose loaded rows changed, and of the new "Horns a2" track; every other track kept its Opus instance). Three level-only stem fixes followed (`tools/stem_fix.py 13 ... --apply`; first-render stems in `cycles/c13/render_first/`, first metrics in `cycles/c13/metrics_first/`; the data the render was made from is in `cycles/c13/rendered_build/`). REAPER was updated with `--mix-only` (all tracks, then Bass trombone), saved and quit; the last quit job hung on a stale bridge heartbeat after the save, so REAPER was killed. Snapshot of the c12 tools and data: `cycles/c13/before/`. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c13-actor/` (`m13.py`, `peaks.py`, `climax.py`, `pdiff.py`, `A/` = critic A's scripts pointed at c12/c13, `A/hsplit.py`, `A/detw2b.py`).

## Accepted

### Horns a2 on the two-horn patch (A #3, C #2)
- New track "Horns a2" (`2 French Horns/06 Keyswitch/2FH KS Master.oib`, appended as stem 33; rows Sus MAX and Leg Slur MAX; its layer groups use CC1 like 1FH, read from the .oib, so `CC1_DYN_TRACKS` "Horn" covers it). Windows where every Horn 1 and Horn 2 onset is the same pitch: 163-165.5, 272.5-314.5, 381.5-404.5, 464-480.5, 628-643.75, 664.5-676.5 (81 notes). The single unison onsets 108 and 528 stay on the solo horns.
- `tools/score_to_parts.py`: `TRACK_WINDOWS` values may be `([(q0, q1), ...], keep_inside)` (helpers `tw_spans`, `tw_keep`, `tw_end`, used by the note filter, lead-line notes, solo boost, CC15 and `find_unisons`).
- Horn 1's per-onset rules inside the windows were copied to the new track (roles, note trims and their step ramps, early fill 311, accent fits as a start, entry lead 636, ABUT_LEAD, breath gap/fall 468, LEVEL_SHAPES 165.3 and 631.9). Pitch trims and legato pitch/pair extras (1FH samples) were not.
- Mix: Horn 1's settings, gain -4 + 4.6 = 0.6 dB (kit c18), seat -0.42.
- With Horn 1/2 off the windows, notes that `find_unisons` had grouped with Horn 1 now play on their own tracks: Horn 3 at 163-165 and 284/286, Horn 4 at 401.9/403.9/464/670 (real parts that were one boosted sample before). Horn 2 dropped unisons 84 -> 5.
- Measured (power, c12 Horn 1+2 against c13 a2+Horn 1+2 per window): first render +3.0 / +1.3 / +0.8 / +2.4 / +3.1 / +3.9 dB; stem-fix roles -3.0 / -1.3 / -0.8 / -2.4 / -3.0 / -2.5 put them at +0.2 / +0.1 / 0.0 / 0.0 / +0.1 / -1.1 dB (the last left 1 dB up for B #3).
- Item 8 on the brass after the change (critic A's `acchf.py`): 2-5 kHz first 80 ms minus body median -7.8 -> -8.2 dB, max +8.3 (Horn 1 273, the pickup's tail) -> +3.8 (Trumpet 1 676). Brass accents refit on c13 including the new track (predicted 33/37 in 2-4 dB).

### Measured tremolo (A #1)
- New generic `MEAS_TREM` (on: `max_value` 16, `min_s` 0.1): a string note with a tremolo value of 16 or 8 whose subdivision lasts 0.1 s or more is expanded at the input stage into abutting same-pitch notes that take the `REP_SPLIT` stroke path (parts.json `meas_trem`). Only the celli's g,1:16 of bars 117-121 qualifies: 80 Stac RRx9 sixteenths (v96 -> v116 through the crescendo). Celli `TREM_JOIN` (464, 484) removed.
- Celli 1-8 kHz folded on the sixteenth grid over 464-480 (A's `fold.py`): 0.5 -> 4.0 dB (pass 3; bar 130's written sixteenths 4.1).
- The strokes played 1.8-3.7 dB over c12 per bar with a -3 dB role; the role went to -6 by stem fix: per bar -1.2 / +0.3 / +1.1 / +0.9 / +1.0 dB against c12 (pass ±1.5), master 464-484 +0.3 dB (pass ±0.5); climax order kept.

### Accents against their pickups (A #2)
- `GENTLE_ACCENT[family]["swell_s_leg"]` = (0.04, 0.35, 0.7) on brass, wind and string: an accent played as a legato target holds its swell through the transition sag.
- `tools/fit_accents.py --pickup-over 2.5` (new; `--pickup-max-qn` 0.5, `--pickup-cap-over` 5.0): an accent must also stand 2.5 dB over a short unaccented pickup that ends at it; the swell is raised for that, but never to more than 5 dB over the same-dynamic neighbours. It also skips tracks the measured render does not have. Fits on c12 (all families), refit on c13 (all families).
- Pickup level cuts as exact LEVEL_SHAPES from the pickup's moved onset to the target's: Bassoon 1 520.5 -5, celli 520.5 -5 / 316.5 -4 / 320.5 -2 / 310.5 -3, Clarinet 1 408.5 -2. (Note trims keyed to these pickups started at the score onset, 0.13-0.26 qn after the moved legato first note, and reached only its last 0.07 qn: replaced.)
- Accent minus pickup (A's `pick.py`), c12 -> c13: Horn 1/a2 273 -1.2 -> +2.9, Bassoon 1 521 -6.3 -> -3.3, Clarinet 1 409 -1.9 -> +1.5, Violins I 118 -1.0 -> +1.5, celli 321 -2.4 -> +0.2, 311 -2.1 -> -1.4, Violas 665 -2.6 -> -1.7, celli 521 -5.6 -> -4.7, celli 317 -4.9 -> -4.6; Violins I 558 -1.5, Flute 1 110 -3.1 -> -2.7. Accents under their pickup 15 of 171 -> 15 of 177. Partial: see Open.

### Balance (B #1-#3, #5)
- B #1 fff anchors Trumpet 2 7.4 -> 10.4, Trumpet 3 9.6 -> 11.6, Horn 3 -2.7 -> -0.2, Horn 4 -0.7 -> 2.8, Horn 4 ff 3.8 -> 5.3; celli [484,492,-3,1]. Re master at 484-492: Tpt2 -15.1 -> -12.3, Tpt3 -15.1 -> -13.3, Hn3 -17.0 -> -14.6, Hn4 -17.2 -> -13.9, celli -9.4 -> -11.7 (no longer the loudest stem); 636-644 Tpt2 -16.5 -> -14.1, Hn3 -13.4 -> -11.5.
- B #2 final chord Violins I [720,729,-2.5,0.5], violas +2: Violins I -4.4/-4.7 -> -6.6/-6.7, violas -8.0/-9.0 -> -5.7/-6.6 dB re master; master -0.3/-0.5 dB.
- B #3 coda 672-676 rows: theme margin per half beat at 674.5/675/675.5 -0.1/0.0/-1.2 -> +3.9/+2.2/+2.7 dB; the 672.5 pickup -6.4 -> -2.6 (celli).
- B #5 opening roll: the proposed [0,12,12] + [12,16,9,1] pair added at qn 12 (+2.3 dB) and released the roll in bar 4 (stem: kit section 4); replaced by [0,16,12] with a -3 dB shape over bar 4: timpani minus quietest string at qn 12/13/14 +3.2/+3.5/+3.0 -> +2.3/+0.4/-0.2 dB.

### Low end (B #4, C #1, C #5)
- C #1 bass-octave rows Double basses, Tuba, Contrabassoon [637.25,646,2,0.25] (Bass trombone 0.5) and [664,680,1.5,0.5]. A row with an end ramp ramps in over [q0 - 0.5, q0], so C's [636.75, ...] lifted the tuba at the master's 636.66 peak (0.501 -> 0.580): moved to 637.25 by stem fix. Bass trombone 2 -> 0.5 dB (Violins I had fallen to its level at 636-644).
- B #4 Double basses loud_eq 160 Hz +4 -> +6, 98 Hz -2 -> -4; dyn trims f 0 -> 1, ff 1 -> 2.
- 63-250 Hz re 500-2000 Hz on the master: bars 160-162 -8.8 -> -7.5 (target -7.6), 167-170 -8.6 -> -7.1 (target -8.1), 117-120 -5.5 -> -5.4, 131-134 -3.3 -> -3.1. Basses re master 636-644 -15.2 -> -13.0.
- C #5 side-only low shelf removed from Vc and Cb: master L/R correlation 20-60 / 60-120 / 120-250 Hz 0.82/0.78/0.55 -> 0.71/0.69/0.48 (targets 0.65-0.75 / 0.60-0.72 / >= 0.48); seats Vc/Cb +4.5/+4.6 -> +4.8/+5.1 dB R-L.

### Smaller items
- c12 brass `cc1_front` test reverted (A #6).
- Final-chord horn breath splits (A #6): Horn 3's 724.6 split -> 725.0, -6/-4/-6 dB shapes at the re-entries (stem fix after -4 on the first render). Horn 3 re-entry bump at +0.1 s +8.3/+8.3/+4.7 -> +2.8/+2.4/+3.2 dB, max 0.5 s step 5.8 -> 2.0, 100-300 Hz autocorrelation 0.28 -> 0.21. Horn 4's re-entries are dips, not bumps (-1..-5 dB); its -4 dB shapes made them -8 and were removed.
- Tenuto 201 (A #6): Horn 1 trim -4 -> -1, celli shape starts at +2: group body minus the quarter before -3.0 -> -2.2 dB (pass 0..+3: not met).
- Clarinet 1 414/422 (C #4): trims -3 -> -6.5 / -2 -> -4. On C's measure (body against the notes each side) 414 +3.1..+6.1, 422 +3.8..+5.5 dB (c12 +5.3..+5.5 / +3.4..+5.4): not met; the accent refit (same-dynamic neighbours) put 422's swell back up to +3.0 over its neighbours. The two measures disagree on this note.

## Tests that failed (left in the render and the tools; revert in c14)
- A #4 Double basses `ART_SPANS` Detache 104-124: 1-8 kHz fold on the eighth grid 1.1 -> 1.3 dB (pass 4; control 520-536 2.0 -> 2.0), level -1.7/-1.2/-0.5 dB. Revert = full rebuild of the Double basses.
- C #3 suspended cymbal key 65, lead_s 1.50: the peak met the crash (+0.02 s, as key 64; the lead estimated from the .ews lengths was exact), but 6-16 kHz relative to the peak at -2.0 / -1.5 / -1.0 / -0.5 s was -71 / -65 / -38 / -14 dB (key 64 -76 / -72 / -46 / -12; pass within 30 dB at -1.5 s and 15 dB at -1.0 s); share of the master's 8-16 kHz at -1.0 s 0%. Every take of this patch swells only in its last second: back to key 64, lead_s 0.25.
- A #5 `WIND_DETACH` brass frac 0.18 -> 0.30: brass changes with a 0.06-0.075 s gap (30) holed -3.1 dB, those under 0.06 s (44) -3.2, slurred -3.5 (pass -4.8). A 0.07 s gap does not separate brass eighths; a CC11 fall at the change is the next thing to try.

## Rejected or deferred
- A #3's tam-tam + crash merge (to free a slot): not needed; the 33rd instance fit (memory below).
- A #6 basses pizz. 408: A asked to listen first; nothing measured to act on.
- C #3's alternatives (another cymbal patch) not tried this cycle.

## Open
- Pickups still louder than their accents: celli 521 -4.7, 317 -4.6, Bassoon 1 521 -3.3, Flute 1 110 -2.7 dB (A's measure). `fit_accents.py`'s pickup window (moved onsets) reads celli 317 at +2.9, A's (score onsets, so it includes the start of the early legato target) at -4.6; the fit's neighbour term then wanted -6 dB steps on 317/321, restored to the c12 values by hand.
- Brass tongued notes 1.2 dB under slurred (target 1.5): needs a CC11 fall.
- Tenuto 201 group -2.2 dB; Clarinet 1 414/422 on C's measure.
- Master sample peak 1.413 -> 1.600 (low brass and celli at 636.66 and 641.72, the C #1 rows and the a2 horns); delivery limiter 1.3 -> 2.3 dB.

## Before / after (c12 -> c13, after the stem fixes)
- Master (float stem sum): -16.3 -> -16.1 LUFS, LRA 21.9 -> 21.8 LU, sample peak 1.413 -> 1.600 (true peak +3.0 -> +4.1 dBFS on the float sum). First render before the fixes: -15.9 LUFS, peak 1.672.
- Delivered mp3 `cycles/c13/mvt1-mockup-c13.mp3`: -19.8 -> -19.8 LUFS, LRA 14.1 -> 14.2 LU, p10-to-max span 18.2 -> 18.5 dB, limiter 1.3 -> 2.3 dB (first render 2.6), -1.6 dBTP. Climax (delivered short-term max): bar 160 -10.27 -> -10.15 > bar 122 -10.76 -> -10.83 > bars 167-170 -12.57 -> -12.87. Motion (mp3) 8.78/4.53 -> 8.74/4.53 dB.
- Simulation before the render (level changes only, c12 stems): limiter 2.0 dB, LRA 14.2; the render measured 2.6 (kit section 16 margin of about 0.5 dB held).
- Attack probe: 0 flagged.
- REAPER memory: 19 GB (0 compressed) when the render started, 45 GB (32 GB compressed) after it, with 33 instances; at the 45 GB guide. Other processes: VM 2.8 GB, Steam 2.2 GB, two other users' Python processes 2.2 and 1.5 GB.

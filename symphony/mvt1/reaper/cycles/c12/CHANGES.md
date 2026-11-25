# Cycle 12: changes (actor)

Two renders this cycle, each from a freshly restarted REAPER (32 tracks, `build_reaper.py --midi-only`, no Opus state changed, no full rebuild). The first render (`cycles/c12/metrics_try1/`, `try1-mvt1-mockup-c12.mp3`, `parts_try1.json`; stems deleted) was broken on the timpani: with CC1 on the layer centres (critic A #1 as proposed) every soft roll played its own recorded-level layer, 20-41 dB under c11, and the opening ppp roll was silent (-83.7 dB, the attack probe's only failure). The second render (`cycles/c12/rendered_build/` is its data) carries the corrected timpani map, a longer brass detach gap and a second step of the brass CC1 test; then two level-only stem fixes (`tools/stem_fix.py 12 ... --apply`; first-render files in `cycles/c12/render_first/`), and REAPER was updated with `--mix-only` for the 17 stem-fixed tracks, saved and quit. Snapshot of the c11 tools and data: `cycles/c12/before/`. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c12-actor/` (`pdiff.py`, `gaps.py`, `timproll.py`, `span.py`, `front.py`, `climax.py`, `A/` and `C/` = the critics' scripts pointed at c11/c12).

## Accepted

### Timpani rolls on their dynamic layers (A #1)
- Checked in `Timpani Flt KS.oib`: the Rls row has groups V1-V8, each Source volume driven by a cc 1 MidiController (fadeTime 120 ms; full at CC1 0-9, 23-26, 38-41, 54-58, 71-73, 86-90, 102-105, 118-127); the stroke rows have no CC1. c11 sent no CC1 and played V8 (fff) everywhere.
- New generic `TIMP_CC1_MAP` / `TIMP_CC1_PAD_QN` / `TIMP_ROLL_TRIM_DB` in `tools/score_to_parts.py` (CC1 lane from the printed curve 0.02 qn ahead; per-dynamic roll level trims in the volume envelope, held through the ring).
- First render with A's map (ppp V1 ... fff V8): roll level against c11 by printed dynamic ppp -40.7, pp -22, p -23, mf -8.3, f -7.3, ff -3.7, fff 0 dB. The layers are recorded at their own level.
- Final map (`build/score_config.py`): ppp/pp CC1 56 (V4), p 60, mp 66, mf 72 (V5), f 88 (V6), ff 104 (V7), fff 122 (V8); `TIMP_ROLL_TRIM_DB` ppp 17.6, pp 19.0, p 18.6, mp 12.7, mf 9.5, f 7.3, ff 3.7, fff 0 dB (estimated, then refit by stem fix).
- Measured (roll body 1-8 kHz share, c11 -> c12): ppp -14.1 -> -37.9, p -12.3 -> -25.8, f -13.4 -> -22.4, ff -11.4 -> -15.9, fff -12.2 -> -12.2 dB (spread 3 -> 26 dB, ordered by dynamic). Crescendo 40-44: -26.3 -> -20.3; 156 pp < ff starts at -28.7. Roll body levels per starting dynamic within -1.0..+1.5 dB of c11 (median 0.0). Roll centroid/100-300 Hz autocorrelation at 3.3/3.95 s: all |r| <= 0.22 (c11 <= 0.22).

### Tongued wind/brass notes (A #2)
- New generic `WIND_DETACH` (`gap_s`, `frac`, per-family `by`): an unslurred wind/brass note into a new pitch ends min(gap, frac x length) early; an ABUT_LEAD on the next note keeps the gap before the moved onset (`wind_detach_qn`). Winds 0.05 s / 0.12; brass 0.09 s / 0.18 (the first render's 0.05 s gave brass only -3.0 -> -4.0 dB).
- Holes at the change (A's `detw2.py`), c11 -> c12: winds tongued -3.6 -> -5.7 dB against slurred -4.2 -> -4.1 (pass); brass -3.0 -> -4.8 against slurred -3.3 -> -3.7 (1.1 dB deeper than slurred; pass asked 1.5).

### Second theme (B #1, C #1)
- B #1: `HP_TARGET_AT` for Vc/Hn1 at 184-204 and +400, violas in the recap; `DYN` mf- 68, mf+ 78, f- 84. Celli now 72-84 (crest 84) instead of up to 100, Horn 1 58-70 (CC1 54-64). Levels moved less than predicted (Horn 1 +0.4, celli -0.8..-1.1, violas 0..-0.7 dB over 183-216/583-616; master -0.3): the per-dynamic trims follow the curve. No restoring roles were needed; Horn 1 minus the strings per qn median -2.1 / -1.3 dB (mf over mp).
- C #1: Horn 1 / celli swell shapes on 184/584, quarter fills cut (Hn1 188/588 6.5 -> 3.0, then 588 -> 5.5 in the stem fix; celli 588 5 -> 1, 188 2.5 -> 1 -> 2.5; Hn1 598 5.5 -> 2.0, 198 2.7 -> 1.0), celli 589 fill 2.5 (stem fix), Horn 1 596/196 decrescendo shapes. Measured: hairpins the right way by 1 dB 22 -> 27 of 39 (29 before the 588/188 refill); Horn 1 184 / 584 end minus start +2.8 / +6.2 dB (c11 +0.1 / +3.1); quarters under the eighth: Hn1 188 -4.4, 588 -4.7, Vc 188 -4.3, 588 -2.9 (c11 Vc 588 +4.2); tenutos after the quarter: Hn1 +2.3 / +0.8, Vc -1.7 / -3.8.
- `tools/auto_fills.py`: decrescendo guard (`DECRESC_UNDER_DB` 1.5): new and raised fills on a note inside or at the end of its own printed decrescendo are capped; existing fills are only reported (`--guard-existing` lowers them: on c11 that would have cut 25 fills, several fitted in c10/c11). auto_fills was not run this cycle.

### Tenutos (A #3) and repeats (A #5)
- Note trims as steps: Horn 1 413 +5, Violas 436 +5 / 589 +4 / 429 3 -> 5, Flute 1 436 +3, Bassoon 1 413 +2. Body minus the note before (c11 -> c12): Hn1 413 -5.1 -> -0.1, Vla 436 -5.6 -> -0.2, Vla 589 -4.4 -> -0.1, Fl1 436 -3.2 -> -0.2, Bn1 413 -1.9 -> +0.1, Vla 429 -2.4 -> +3.5.
- `WIND_REP_RETONGUE_BY["Trombone"]` gap 0.08 s, fall 10 CC. The Horns 3/4 final-chord "repeats" (721.6, 722.3) are the c05/c10 breath splits of a tied note, not printed repeats: left.

### Balance (B #2-#6)
- B #2 roles bars 23-25 / 135-137 (Vln I/Fl1/Ob1 up, Vln II/Va/Vc down). Tune minus loudest accompaniment per qn (my measure, Bn1 included): bars 23-25 -3.5 -> -0.3 dB (covered 10 -> 7 of 12), 135-137 -0.9 -> +1.9 (8 -> 1); master within 0.1 dB.
- B #3 final chord shapes: bar 180 -> 182 celli -8.9 -> -4.9, basses -6.0 -> -4.5 (violins -5.3/-3.8, master -4.4 -> -4.2); celli minus Vln I in bar 182 -9.7 -> -5.7.
- B #4 violas -3 at 680-695.5: cor anglais minus violas median +0.8 -> +4.4 dB (covered 5 -> 3 of 12).
- B #5 Horn 3/4 f anchors +1.8. B #6 timpani strokes 125 -2 / 284 -2.5 (steps): master over the first 0.6 s -0.3 / -1.0 dB.

### Bar-41 decrescendo (C #3)
- Level shapes Horn 1 (-8, after a first render at -6 gave -2.5 dB), Flute 2, Oboes, Clarinet 2; Horn 1 165 fill removed. Master 167-168 against 164-165: -1.0 -> -4.1 dB; Horn 1 +2.2 -> -4.1; Flute 2 never over its 160.5 level (max -41.8 against -39.8); bar 43 3.2 dB under 167-168.

### Accents
- `fit_accents.py 12 cycles/c12/rendered_build/parts.json --family brass|wind --keep-long-qn 1.4 --write` (79 rows); predicted brass 37/37, winds 123/140 in 2-4 dB, 2-5 kHz first 80 ms over 3 dB: none. Strings not refit (no string articulation changed).

## Test that failed (leave in, revert next cycle)
- C #2 brass CC1 front: +8 CC1 from the moved onset (first render), then +14 from 0.05 s before, held to +0.10 s, back over 0.15 s, plus the swell full at +0.04 s. Brass stems' 2-5 kHz first 80 ms minus body (146 accents): median -14.5 -> -13.5 dB; master brass accents -9.2 -> -9.6 (pass asked -5..-3); strong-onset median -6.2 -> -6.1. The CC1 MidiController's 120 ms fade and the Sus attack keep the front dark. Revert `cc1_front` next cycle (or try the next layer's attack another way); the swell timing can stay.

## Rejected or deferred
- A #4 a2 horns / tam-tam + crash merge: deferred again (needs a cycle with no other build change).
- C #4 220 Hz loud EQ on Tbn1/2, Hn3/4, violas: rejected by arithmetic. Those stems give -15.5..-22.4 dB of the loud 100-250 Hz band; +2.5 dB on all of them raises the band about 0.3 dB, the pass asked +0.9.
- C #5: a constraint, kept (no ff lift).
- A #5 Horns 3/4 final-chord part: see above.

## Open
- Brass tongued holes 1.1 dB deeper than slurred (target 1.5); a longer gap or a CC11 fall at the change next.
- C #2 failed (above).
- Bars 23-25 tune still covered in 7 of 12 beats on my measure.
- Hairpins in the second theme 27 of 39 (target 30); the 588/188 refills cost two.
- Violas 429 tenuto now +3.5 dB over the note before (target 0..+3).

## Before / after (c11 -> c12, after the stem fixes)
- Master (float stem sum): -16.3 -> -16.3 LUFS, LRA 21.8 -> 21.9 LU, sample peak 1.489 -> 1.413 (true peak +3.5 -> +3.0 dBFS on the float sum).
- Delivered mp3: -19.8 -> -19.8 LUFS, LRA 14.2 -> 14.1 LU, p10-to-max span 18.1 -> 18.2 dB, limiter 1.7 -> 1.3 dB, -1.6 dBTP. Climax (delivered S max): bar 160 -10.3 > bar 122 -10.8 > bars 167-170 -12.6 (c11 -10.3 / -10.8 / -12.7). Motion (mp3) 8.74/4.52 -> 8.78/4.53 dB.
- Attack probe: first render 1 flagged (the silent timpani opening, a real fault); second render and stem fixes 0 flagged.
- REAPER memory: 43 GB (0 compressed) before each render; after the first render 43 GB (13 GB compressed), after the second 43 GB (1.5 GB compressed; 28 GB compressed by the save and quit after the analysis). Other processes: VM 2.8 GB, Steam 2.1 GB, two other users' Python processes 1.5 and 1.2 GB.

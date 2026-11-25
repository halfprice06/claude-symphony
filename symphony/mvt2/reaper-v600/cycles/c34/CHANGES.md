# Cycle 34 changes (actor, on the critics' reports on the c33 render)

Snapshot of the previous tools and data: `before/`. Data as rendered: `rendered_build/`. Build log `build.log`, render log `render_cycle.log`.

## Accepted

Config (`build/score_config.py`, block "c34"):
- C #1 climax: Violins I/II +3 dB and celli +3.5 dB held 204.2-211.6 (`LEVEL_SHAPES`, slow ramps), `_all` -1.5 dB over 262.25-267.75 (cadence).
- C #6: strings +2.5 dB held 180.5-183.1 (the 172-178 hairpin gain was released at the start of the next crescendo).
- A #3 / C #2: Violins II 220-223 bloom: C's shape (-4 .. -7.5 dB, 220.75-222.95); `rebow_fills.json` Violins II 223 -4 dB over -0.04..1.48 s.
- C #5: `FP_SPIKE = ("f", 0.2, 0.4)` (was the default 0.12/0.25).
- C #3: bass clarinet pedal 6-17 split into three breaths on its own row: `REBOW_AT["Bass clarinet"] = [10.0, 13.5]`, new generic `REBOW_ART_BY = {"Bass clarinet": "Sus Non Vib"}`; the dead `REP_RETONGUE_AT` 9/12/15 removed.
- A #4: Trombone 1 215 lift +4.5 -> +1.5 dB; 214.5/217 slur heads +2 -> +4 dB held to 0.40 s; tenuto repeat 216 re-tongued by `WIND_REP_RETONGUE_BY["Trombone 1"]` (gap 0.14 s, CC11 fall 16).
- A #6: `MERGE_NOTCH_AT` Cor anglais 271: 20, Violins II 50: 14 -> 18; `WIND_REP_RETONGUE_BY["Horn 3"]` gap 0.12 s, fall 10 (265, 289).
- A #2: basses' 273.229 piece: -5 dB shape at 274.24-274.67 (its +5 dB bump; the piece keeps no fill, c29).

Tables:
- B #1 violas: `mix.json` Violas and Violas div `dyn_trim_db` f -2 -> 0, ff -3 -> -1.5; `roles.json` Violas [196,204,-4,4] -> -2; new [249.9,258.5,4,5.5].
- B #2: `roles.json` Violoncellos [286.9,288.9,-5,0.5] (bar 87 bloom).
- B #3: `roles.json` Double basses [285.9,299.75,2,0.5] (coda 4 soli).
- A #1: Violoncellos div pedal (274-286) re-bows fitted by `fit_rebows.py 33` (five keys); `early_fills.json` Violoncellos div 274 {db 4, hold 0.6 s}. Pieces not lengthened (REBOW_SEG_S_BY not added: it moves the points and voids the fit).
- A #2: Double basses pedal re-bows 221.8-235.659 and 276.05-283.605 refitted with the new `--window "Double basses:2.6"`, 273.229 skipped. The raw fit chained the pieces +2..+6 dB up (holds up to +9), so each refitted piece was shifted to keep its c33 mean (shape fixed, level kept); other basses keys (final chord, 6.25, 166, 170) kept.
- A #5: `auto_fills.py 33 --write` (86 entries: 19 new, 6 raised, 22 retimed, others lowered/removed), `--exclude "Violoncellos div:63.0"`. Simulated on the c33 stems: 14 fills whose 200 ms front rose more than 2 dB over the louder body (and 0.5 dB over c33) were lowered by (over - 2) dB; Violas 56 and Violins I 75 removed. The violas' listed joins (46.5, 109, 111, 120, 189, 249, 253.5 ...) are notes of 0.35-0.54 qn, under auto_fills' 0.45 s target length, so they were not filled.

Tools:
- `tools/fit_rebows.py`: `--window "Track:S"` (per-track fit window; hold window extends to W + 0.3 s).
- `tools/score_to_parts.py`: `REBOW_ART_BY = {}` (row for a track's listed re-bows).
- `tools/deliver_master.py`: `MOM_CAP_ABOVE` 6.0 -> 3.0 (C #4).

parts.json: no WARNING; MIDI changes on Cor anglais, Bass clarinet (2 new pieces, v45), Horn 3, Trombone 1, Violins II (50, fp), Violas/Double basses/div tracks (fp); vol_db on all tracks (`_all`). No Opus state changed (no full rebuild); `build_reaper.py --midi-only` for all 32 tracks in 24 s.

## Rejected / deferred
- A #1 step 2 (`REBOW_SEG_S_BY` longer pieces) and entry lead +0.15 s: both move the re-bow points of a pedal just fitted; the fill alone brought the swing under the 4 dB pass in simulation and render.
- A #5 viola short-note joins: need a fill rule for notes under 0.45 s (the critic's 50 ms dips; master dips 1-4 dB).
- A #6 Violins II 45 piece shortening (re-bow; small).
- C #2 `SWELL_CC_CAP` for the strings (changes the layer mix everywhere; the two exposed blooms got shapes instead).
- MANUAL-GAPS: no gap tried this cycle (the findings were level and shape work).

## Measured (c33 -> c34 render; the render matched the stem_fix simulation within 0.3 dB)
- Violoncellos div pedal 274.5-285.5 swing (p10-p90, 200 ms) 8.0 -> 4.3 dB.
- Double basses piece swings (100 ms): 225.2 9.4 -> 5.3, 230.4 9.1 -> 2.9, 235.7 9.2 -> 1.7, 278.4 9.5 -> 6.3, 273.2 11.4 -> 10.4 (shape too small; open).
- Violins II 221.5-222.9 -41.9 -> -48.2 dB (220-221.5 -45.2 -> -47.2): the bloom is gone.
- Violas minus Violins II: bars 57-58 -6.6 -> -5.4, 59 -3.7 -> +0.3, 60 -5.0 -> -2.9, 61-62 -1.9 -> -3.6, 75 -9.7 -> -5.3, 76-77 -3.0 -> -0.3, 78 -6.2 -> -4.1, 79-80 -4.7 -> -3.3.
- Celli 287-289 -44.6 -> -49.1 (3.6 dB over Violins II); basses 286-298 -56.7 -> -54.7.
- Master: 202.75-204 -16.5 -> -16.3, 204-206 -15.6 -> -14.5, 262-266 -18.2 -> -19.6; 181-182 -31.5 -> -30.0 (now level with 179).
- Trombone 1 bodies 214.5/215/215.5/216/217/217.5: -23.9/-25.5/-24.2/-25.1/-25.1/-24.0 (c33 -26.6/-22.5/-24.2/-24.8/-28.0/-24.0); 213 accent -21.5; 216 repeat dip 1.2 -> 4.6 dB.
- Repeats (30 ms): Horn 3 265 -0.4 -> 1.9, 289 0.5 -> 2.2 dB (still under 3); Cor anglais 271 now has a 10-15 dB hole 0.1-0.35 s after the onset (notch 20 is too deep: try 12-14 next cycle).
- bar 47 fp: master peak 148-148.6 -31.6 -> -31.5 (no measurable change).
- Bass clarinet 6.5-16.8 500-1000 Hz detrended level autocorrelation at 3.5-4.5 s: 0.32 -> 0.44 by my method (2 s detrend, 50 ms frames), which does not reproduce critic C's 0.94; the critics should re-measure with their method.
- Master -20.5 LUFS (c33 -21.0), LRA 23.4, true peak -0.3 dBFS (c33 -2.3; sample peak 0.961, no clipping; from the climax hold). Delivered: -19.7 LUFS, LRA 15.1, TP -1.6, span 18.2 dB, limiter 2.6 dB (c33 1.4).
- Attack probe: 0 flagged (Violins I 212 dip 5.9, celli 212 5.8 against limit 6: close).
- No stem fix needed.

## REAPER
- Lock held 04:07:20-04:31:19 (24 min). Fresh open settled at 44 GB with 11 GB compressed; rendered with `--force-memory`. 44 GB (27 GB compressed) after the render.

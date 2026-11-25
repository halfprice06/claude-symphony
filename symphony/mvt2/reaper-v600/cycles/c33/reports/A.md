# Cycle 33, critic A: articulation and phrasing (on the c32 render)

Sources: `cycles/c32/render` (stems and master), `cycles/c30/render`, `c30/render_first`, `c31/render`, `c31/render_first` for comparison, `cycles/c32/rendered_build/parts.json` and `mix.json`, `cycles/c30/rendered_build/parts.json`, `cycles/c31/before` and `c32/before`, `cycles/c32/CHANGES.md`, `build/score_config.py`, `build/mockup-events.tsv`, `build/sections/coda.ily` and `aTwo.ily`, the `.oib` envelopes of `Harp Sus RR.oib` and `Harp Harmonics.oib` (read with `opus_state.load_oib`), `tools/build_reaper.py` and `tools/score_to_parts.py`, the May 2021 HO manual PDF pp.68-71 (row A6 of `loop/MANUAL-READING.md`, cycle 33), `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md` (the listener section and section 9), movement I `loop/LEARNINGS.md` (Harp c11, c28, c35), the c32 critic A report.

Times are score qn unless marked s. Levels are RMS of the power sum of both channels, (L² + R²)/2, in the window stated. A plain L+R mean showed false 10 dB flutter on the final chord through hall phase cancellation, so I did not use it. Band levels are FFT energy in a band. They compare across renders, not as absolute values.

## Manual notes (A6, PDF pp.68-71: Hollywood Harp)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| The harp library has vintage close and mid mics instead of surround (p.68) | Harp and Harp harmonics, `mix.json` Close + Main | Yes. The mics are a blend question, not an articulation one. |
| Maestro patches: velocity selects the articulation; Maestro = Double Hit 1-60, Gliss Technique 61-102, Nail Picks 103-127 (p.69) | none | Correctly not used. With Maestro, a pp chord at v52 would play Double Hits, and the patch has no samples below MIDI 48 (KIT §9). |
| Sustain RR: Pluck Long (RRx1) and Thumb Pick (RRx2) alternate at v1-123, 5 dynamic layers each; Nail Pick at v124-127 (p.69) | the Harp track, all 158 notes | Followed. Velocities run 44-104, none reaches 124. Rolled two-note chords put Pluck on the bottom note and Thumb on the top until an odd note count flips the order (bars 7-14: flipped at 31-33). The level cost is small here. In the bars 53-56 triplets the even and odd notes have the same median peak (-42.8 / -42.6 dB, measured). |
| Bisbigliando variants (CC1) (p.69-70) | none printed | Not applicable. |
| Individual articulation patches: Pluck (5 layers), Thumb Pick (5), Double Hit, Gliss Technique, Nail Pick, Près de la table, Repetition Rep (p.70-71) | the triplet figure bars 53-56 has same-pitch repeats a third of a beat apart (B flat 3 at 180-183) | Not needed. The repeats are not fast enough for the Repetition patch, and each note rings until the next plucks (HARP_RING_S). |
| Harmonics: hollow sound with no fundamental, sounds at the written pitch, 2 dynamic layers by velocity (p.70) | Harp harmonics, qn 274-277 ("dolce, harm., L.H. (sound 8va)", p) | Followed. The track plays the hidden sounding voice (A flat 4, C5, E flat 5). Velocities 58/58/66 sit in one layer. |
| Glissando key maps (p.71) | none: v600 has no glissandi | Not applicable. |
| Not in the manual, but in the patches these pages describe: every group's AHDSR and the instrument envelope decay 5990 ms to sustain 0.001 (read in `Harp Sus RR.oib` and `Harp Harmonics.oib`) | every harp note | **No.** Movement I c35 fixed this with `mix.json` `env_sustain`; movement II never got that fix. See finding 1. |

## Findings, ranked by what a listener would hear

### 1. Every harp note is choked by the patch envelope: the chords fall 6-11 dB per second, and the let-ring A flat 1 under the bar 83 harmonics is gone by the downbeat

- **Where.** Harp (stem 21), every passage: bars 7-14 (chords under the Horn 1 theme), 37-44, the bars 53-56 triplets, 71-78, and the coda pickup. Harp harmonics (stem 27), qn 274-277.
- **Patch (read).** Both patches ship the same envelope on every group AHDSR and on the instrument EnvelopeProxy: decay 5989.6 ms to sustain 0.001. That is a fall of about 60 dB in 6 s, applied to plucks that were recorded at 6.6-10.6 s (movement I LEARNINGS c35).
  - `tools/build_reaper.py` already has the switch: `mix.json` `env_sustain` (lines 259-275).
  - `build/mix.json` "Harp" sets only `env_release_ms` 200. "Harp harmonics" sets neither.
- **Measured (c32 Harp stem, 100 ms frames; slope fitted from 0.3 s to the next onset).**

  | onset | 19 | 28 | 108 | 114 | 120 | 247 |
  |---|---|---|---|---|---|---|
  | slope dB/s | -9.3 | -8.9 | -11.4 | -6.4 | -5.7 | -6.2 |
  | drop before the next pluck, dB | -19.7 | -15.8 | -19.1 | -11.8 | -10.8 | -22.2 |

  - The 108 octave D flat (p, under Flute 1's theme B) loses 19 dB before the next pluck 2 s later.
  - In bars 7-14 the level 0.15 s before each chord is 55-72 dB, against chord peaks of -43 to -51 dB.
  - A harp chord in an Adagio at q=52 should still be ringing when the next one comes. Here it sounds damped. That is inferred: a real harp's low strings ring well past 2 s, and the patch's own samples run 6.6-10.6 s.
- **Coda (measured).** The score ties the A flat 1 of bar 82 into bar 83 ("let ring", `aTwo.ily` c214) so that the harmonics have a bass under them.
  - The harp stem reads -64 dB at the 274 downbeat, -84 at +1 s, -96 at +1.5 s and -110 at +2.5 s. The tie lasts to 277, 3.4 s after the downbeat.
  - The harmonics enter at -49 dB. The parts.json note is still held (271, 7.76 qn), so the decay comes from the envelope, not from the R.H. étouffez damp.
  - The harmonics fall on the same envelope. The 276 arrival goes -51 -> -69 dB within 2 s.
- **Fix.**
  - `build/mix.json` "Harp": add `"env_sustain": 1.0` and keep `env_release_ms` 200, so HARP_RING_S and the damps still work.
  - "Harp harmonics": add `"env_sustain": 1.0`. Its release stays the patch's 3019 ms, which suits ringing harmonics.
  - Both tracks need a full rebuild, because the Opus state changes.
  - Movement I c35 measured the cost: arpeggio tails between onsets rose a median 1.1 dB (p90 2.5), and an onset level does not move.
  - After the render, re-check the harp's level per printed dynamic with `stem_fix.py`. The sustained tails add energy in the bars 53-56 triplets, so expect -0.5 to -1.5 dB of trim there.
- **Check.** Drop before the next pluck 3-8 dB at 19/28/108/247. The coda harp stem no lower than -60 dB until 277. The harmonics' 276 arrival still within 6 dB of its peak 1.5 s later. The étouffez damp at 274 still 15 dB or more on the R.H. pickup notes (A flat 3, C4, E flat 4, F4).
- **Evidence.** Envelope read in both patches; decay measured; audibility inferred.

### 2. Trombone 1, bars 63-64: c32's revert did not bring back c30's softer legato heads. 213 and 215 still bite, and the cause is not the 212.5 lead

- **Where.** Trombone 1, qn 213 (slurred accent) and 215 (unaccented eighth, slurred target), ff marcato quotation.
- **Data (read).** c32's rendered parts.json for Trombone 1 is identical to c30's rendered parts.json in notes, velocities, keyswitches, CC1, CC11, CC7, CC36, tempo map and Opus state.
  - Only `vol_db` differs, after 215.9: the new 216 tenuto shape and the 217.5 shape that was removed.
  - The 212.5 pickup is back at 212.401 with v106. 213 is at 212.91, v112.
- **Render (measured).** 2-5 kHz energy in the first 80 ms of the note, and 30 ms peak:

  | note | c30 first render | c30 (after stem fix, -2.8 dB track) | c31 | c32 |
  |---|---|---|---|---|
  | 212.5 | 27.0 / -24.1 | 24.2 / -26.9 | 25.6 / -26.9 | 24.2 / -26.9 |
  | **213** | 27.4 / -18.6 | 24.6 / -21.4 | 35.0 / -17.8 | **35.5 / -17.4** |
  | 214.5 | 28.4 / -22.6 | 25.6 / -25.4 | 25.5 / -25.4 | 25.7 / -25.4 |
  | **215** | 28.7 / -19.5 | 25.9 / -22.3 | 36.6 / -20.3 | **36.7 / -20.1** |
  | 215.5 | 24.0 / -22.0 | 21.2 / -24.8 | 27.8 / -23.2 | 27.8 / -23.2 |

  - Notes with no legato transition (212.5, 214.5, 217) render the same in every cycle to 0.1 dB.
  - The legato targets 213, 215 and 215.5 changed in c31 and stayed changed in c32. That is +11 dB of 2-5 kHz front and +4 / +2.2 dB of peak against c30 at the same mix gain.
  - On the master, the 2-5 kHz jump (first 150 ms against 0.3-0.15 s before) is +6.1 dB at 213 and +6.3 at 215 in c32. In c30 it was +2.1 and +3.4. Series 1 c26 answered Dan's item 9 by taking that jump to +2.
  - 215 is not accented, yet it now has the brightest front of the phrase.
- **Cause (inferred).** The legato transition sample changed between renders while the MIDI stayed the same. The likely cause is a round-robin position that the pipeline never resets: the pre-roll sends CC36, while Opus's round-robin reset controller is CC16 (`Preferences.json` `RoundRobinResetCC: 16`; MANUAL-GAPS #10; 2025 manual p.92). c31's change of the pickup lead did not cause it: c32 undid that change and the sound stayed.
- **Fix.**
  - (a) Make takes repeatable first. Add a generic `RR_RESET_CC = 16` in `tools/score_to_parts.py`: send CC16 127 in the pre-roll on every track, next to the CC36 that is already sent, in the lane of the existing `cc36` mechanism. `build_reaper.py` must write it.
    - This changes the takes on every track once. Schedule the level check with the next stem fix.
  - (b) Whatever take (a) lands, give the two heads c30's weight with pre-hall CC7, so no tail is cut (S3):
    - `CC7_POINTS["Trombone 1"] = [(212.86, 127), (212.9, 85), (213.35, 85), (213.6, 127), (214.86, 127), (214.9, 95), (215.3, 95), (215.38, 127)]`. CC7 85 is -3.5 dB, 95 is -2.5 dB, linear amplitude.
  - (c) If the master jump is still over +3 dB, add a timed EQ in `mix.json` "Trombone 1": `loud_eq` `{"points": [[0,0],[212.85,0],[212.9,1],[213.4,1],[213.55,0],[214.85,0],[214.9,1],[215.3,1],[215.4,0],[304,0]], "bands": [{"band": "highshelf", "hz": 2000, "db": -6}]}`. It uses the same mechanism as the soft-horn shelf from c32 C #4.
- **Check.** Master 2-5 kHz jump at 213 at most +3 dB, and at 215 at most +2 dB and under 213's. Trombone 1's 213 peak -20 ±1 dB, 215's -22 ±1. 216, 217.5 and 218 unchanged: 218 now peaks 2.2 dB over 217.5 with a 2-5 kHz front 19 dB under its body (measured, c32 target met).
- **Evidence.** Measured (three renders, parts.json diffs); cause inferred.

### 3. Double basses "4 soli" and coda pedals: every second re-bow piece still swings 8-11 dB (c32 A #2, deferred, unchanged)

- **Where.** Double basses, E flat 2 pedal qn 220-238 ("4 soli, sul A, change bow at will") and A flat 1 pedal 271-286.
- **Measured (c32, p90-p10 of 100 ms levels with vol_db removed, from 0.4 s after each piece's start).**

  | piece | 220 | 221.8 | 225.22 | 227.78 | 230.39 | 233.04 | 235.66 | 271 | 273.23 | 276.05 | 278.35 | 282.2 | 283.61 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | spread dB | 6.9 | 5.4 | **8.8** | 4.4 | **10.5** | 4.8 | **8.4** | 3.9 | **9.9** | 5.0 | **10.6** | 2.9 | **9.1** |

  - The alternation is as strict as c32 critic A found on c31: the bow-direction round robin of Sus MAX, per the digest's note on manual p.91.
  - Re-bow dips are small (stem median 1.6 dB). The problem is the slow wobble inside every other piece.
  - The basses are the lowest voice under the Horn 1 solo of bars 65-70, and under the harp harmonics in the coda.
- **Fix.** The tool from finding 2(a) covers this: a generic `RR_RESET_AT = {track: [score qn]}` sends CC16 0.05 qn before each listed note.
  - Movement II: `{"Double basses": [220, 221.8, 225.215, 227.775, 230.393, 233.038, 235.659, 271, 273.229, 276.05, 278.351, 282.203, 283.605]}`. Every piece then starts on the same bow.
  - If that bow is the unsteady one, reset before every second piece instead, so the steady direction plays twice in a row.
  - Refit these pieces' `rebow_fills.json` entries with `fit_rebows.py --stems` after the render.
- **Check.** Every piece's spread at most 7 dB. Stem re-bow dips at most 4 dB.
- **Evidence.** Measured; cause read in the digest and inferred from the strict alternation.

### 4. Celli "4 soli", bars 83-86: play them on the free Violoncellos div track (Celli KS Master DIV A) instead of the full section at -3 dB

- **Where.** Violoncellos, A flat 2 pedal qn 274-286 ("4 soli"), ppp, under the harp harmonics and the timpani answer.
- **What is wrong (read; sound inferred).** `SOLI_AS_META` plays four players as the full section 3 dB lower. That is a soft full section, with a section's width and chorus, under a passage the score thins to harmonics and four solo players.
  - The "Violoncellos div" track already loads `Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib` (half section, Close only; manual pp.89-90).
  - The track plays only qn 51-54 and 62-66, so it costs no memory.
  - This is the same proposal as c32 A #6, which was deferred. The half-section patch is the best installed choice for "4 soli". The basses' equivalent (`Basses Divisi DIV A`) needs a 33rd instance, so it waits for a second pass (MANUAL-GAPS #8).
- **Fix.**
  - `TRACK_WINDOWS` in `build/score_config.py`: "Violoncellos div" (274.0, 286.0, True) and "Violoncellos" (274.0, 286.0, False). Extend `TRACK_WINDOWS` to a list per track in `score_to_parts.py` if it holds only one window.
  - Skip the META -3 dB inside the window.
  - Move the `rebow_fills.json` Violoncellos keys 275.494-284.151 to the div track and refit them.
  - Set the level by stem fix to c32's celli level over 274-286 (-55 dB, power sum).
  - The div track gains the Sus MAX row, so it is fully rebuilt.
- **Check.** Level within 1 dB of c32. Re-bow dips at most 4 dB. No alternating piece spreads like finding 3.
- **Evidence.** Patch and windows read; realism gain inferred.

### 5. Violin I solo, bars 17-22 ("solo, senza sord., dolce"): every legato target plays v124, the fastest transition

- **Where.** Violin I solo (DIV A), qn 48.5-53 and 60.5-63, 9 legato targets.
- **What is wrong.** parts.json gives every target v124 (`LEG_VEL_STRONG` string 124). In the string KS Masters, legato velocity sets the transition's sample start: v124 starts about 4650 samples in, v60 about 1480 (MANUAL-GAPS #6, script read in movement I). The manual says 50-60 gives a longer transition, "allowing the melody to breathe" (p.144).
  - The joins dip 0.1-4.2 dB (measured), so they connect. They are, however, the tight joins of a fast section passage, inside a dolce solo line of half and quarter notes at q=52. The audible effect is inferred.
  - This is the one passage where a slower transition costs nothing in timing: the solo leads its own line.
- **Fix.**
  - `VEL_SET["Violin I solo"] = {48.5: 80, 49.0: 76, 50.0: 76, 51.0: 72, 53.0: 72, 60.5: 80, 61.0: 76, 62.0: 76, 63.0: 72}`. Check in parts.json that VEL_SET wins over LEG_VEL_STRONG.
  - Add +0.04 s to the solo's `leg_leads.json` entries for these onsets (the slower transition arrives later).
- **Check.** Energy centroid of the first 150 ms of each target within ±0.04 s of c32's. Join dips 1-4 dB. Level per bar within 1 dB.
- **Evidence.** Velocities read; effect inferred.

### 6. Small harp details: the D flat 4 is weak in the bars 53-56 triplets, and the harmonics' passing C5 is still the loudest of the three

- **Triplets 172-188 (measured, 20 ms peaks against a 7-note running median).** D flat 4 (MIDI 61) sits a median 3.2 dB under its neighbours (six notes: -2.3, -0.3, -4.0, -4.3, +1.3, -4.2). Every other pitch is within ±1.7 dB except G flat 3 (+4.1, two notes) and A flat 4 (-2.8, two notes). The figure's p10-p90 is 5.2 dB.
  - Fix: `tools/score_to_parts.py` `HARP_PITCH_VEL` add `61: 6` and `68: 4`, and set `54: -5` in `build/score_config.py` if the dict can be overridden there. At 0.6-1.0 dB per step across a layer (movement I c28), that is about +3 to +5 dB.
- **Harmonics 274-276 (measured).** Peaks -46.0 / -44.7 / -46.8 dB. The passing eighth (275.5) is 1.3 dB over the first note and 2.1 dB over the slur's arrival, even after the c30 -5 dB shape.
  - Fix: deepen the `LEVEL_SHAPES_S["Harp harmonics"]` 275.5 shape from -5 to -7 dB. Raise 276 to v70. After finding 1, re-measure 276 1 s after its onset, not at its peak.
- **Evidence.** Measured; small audible gain.

## Smaller observations (measured unless marked)

- **c32 changes in my lens, verified.**
  - Violas' portato bars 48-51: all 15 peaks within -45.7..-47.6 dB (±1 dB). They sit 2.7-10.4 dB under the cor anglais (bar 48 -2.7..-4.0 dB, the c28 aim was 7-9). The energy centroid of the first 0.45 s is +0.15..+0.25 s on every note, now consistent.
  - Violins II 45: the stem dip rose from 2.7 to 4.5 dB, master 2.9 dB. Violins II 50: unchanged on the stem (5.9 dB), master 2.3 -> 2.9.
  - Trombone 1 216 tenuto: body -26.1 dB, between 215.5 (-25.0) and 217 (-29.1). 218 accent: 2.2 dB over 217.5, 2-5 kHz front 19 dB under its body.
- **Re-bows (stem dip = level -0.4..-0.05 s minus the minimum of 50 ms frames within -0.05..+0.3 s).** Stem medians: Violins I 3.4, Violins II 3.2, violas 3.5, celli 2.0, basses 1.6, Violas div 2.8, Violins II div 3.0 dB.
  - Largest on the master: Violins II 45 (4.4, the printed new bow), Violas 5.7 (3.4), Violas 270.94 (3.2), Violins II 293 (3.3).
  - Final chord, Violins I 295: stem 7.5, master 1.4 dB.
  - No 3.95 s loop pulse on the timpani rolls (autocorrelation -0.72..+0.22). c32's critic found none on the strings.
- **Timpani.** The ppp roll of bars 67-70 (226-237.5, 13.5 s) sits 13-17 dB under the master and falls 7 dB with the printed decrescendo. Horn 1, both bassoons and the basses are over it. The f rolls of bars 61-62 and 79-81 sit 15-22 dB under the master. Rule 5 holds.
- **Harp rolls.** Two-note chords are rolled at 35 ms and three/four-note chords at 30-40 ms per note, from the bottom. The Pluck/Thumb order inside a chord flips at 31-33 when an odd note count comes in; I measured no level step from it.
- **Not re-measured this cycle,** because c32 left them unchanged and c32 critic A measured them: pizzicato 37-44, Violins II sul tasto (Flautando) 37-40, tremolos 61-64, CC15 mute placement in the coda, breath marks, the tenutos of bars 61-62.

## Do not touch

The violas' Detache row with its per-note CC7, from c32. Trombone 1's bar 64 shapes (216 +3.5, 218 held up) and its slurred legato line. The timpani roll shapes and CC1 layers. The harp roll order and timing, the bar 83 R.H. damp, `env_release_ms` 200 and HARP_RING_S 2.0 (finding 1 adds sustain and keeps these). The re-bow times on the opening chord, bar 66 and the final chord. CC15 mute placement. Monophonic Leg rows and keyswitch placement.

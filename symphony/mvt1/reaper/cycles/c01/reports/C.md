# Cycle 1, critic C: blend and space (review of the c00 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new), low-end build-up against several references. Scripts and scratch output: /private/tmp/claude-501/mockup-loop/mvt1-c01-C/ (perc.py, brass.py, same.py, depth.py, stereo.py, tails.py, low.py, third.py, lowstems.py, barlow.py, fund.py, loop.py, acc.py). Times are score seconds from the parts.json tempo map; bar b starts at qn 4(b-1).

## 1. The trumpets sit 8-15 dB under the trombones in every loud tutti (Trumpet 1-3, bars 116-124, 130-134, 139-143, 158-161, 167-170)

What is wrong: the three trumpets are on a new sample set (1TP KS Master) and come out far below the rest of the brass. You cannot hear them as the top of the brass choir. Trombone 1 is the loudest stem of the whole orchestra in bars 117-121 and 159-161 (metrics.md, loudest three per bar), and the trumpets are buried under it.

Evidence (measured, A-weighted stem levels over the span, brass.py):
- Bars 158-161 (ff into the fff climax): Tpt1 38.0, Tpt2 35.1, Tpt3 31.6 against Tbn1 46.4, Tbn2 44.4, BTbn 43.9, Hn1 41.0, Vln I 43.5. Tpt1 is 8.4 dB under Tbn1 and Tpt3 is 14.8 dB under it.
- Bars 116-124: Tpt1 34.0 / Tbn1 45.1 (-11.1). Bars 130-134: 28.5 / 40.4 (-11.9). Bars 139-143: 33.7 / 39.1 (-5.4). Bars 167-170: 38.8 / 43.5 (-4.7).
- Same note, same controllers (same.py): at qn 628.3-631.8 Trumpet 3 and Trombone 1 both play C4 at CC11 117 with the same volume envelope (+1.12 dB). Trumpet 3 is 16.0 dB under Trombone 1 (A-weighted), 12 dB under in 2-5 kHz. Track gains differ by only 3 dB (trumpet -3, trombone 0), so the 1TP patch with Close 0.5 / Main 1.0 is about 13 dB quieter than the 1TB patch at the same pitch and CC11. CC11 on the trumpets is already 124-127 at the climax, so CC11 cannot close the gap.
- Spectral shape is not the problem: at that C4 the trumpet's 2-5 kHz sits 6 dB under its 0.2-1 kHz band, the trombone's 12 dB under. The trumpet is the brighter instrument, as it should be; it is only too quiet.
- The factory 1TP patch loads Close 0.25 / Main 0.47 / Surround 1.0 (read from the .oib); the mix uses Close 0.5 / Main 1.0, Surround off, which keeps it at the same depth as horns and trombones (tail drop 18.3-19.2 dB at 0.3-0.5 s after a release, against 16.6-18.1 for the trombones, depth.py). Depth is consistent; level is not.
- Rimsky-Korsakov's resonance comparison (used as the balance target in mockup-kit LEARNINGS section 13) puts a trumpet and a trombone at about equal power in forte (inferred target).

Fix: in build/mix.json raise Trumpet 1 gain_db from -3 to +5, Trumpet 2 from -3 to +6, Trumpet 3 from -3 to +7. Target, measured over bars 158-161: Tpt1 within 2-3 dB of Tbn1 (A-weighted), Tpt3 within 5 dB. At the same time give Trombone 1 and Trombone 2 dyn_trim_db {"f": -1, "ff": -1.5} so the first trombone stops being the loudest stem in bars 117-121 and 159-161. Check master headroom: the c00 24-bit master already clipped (stem-sum peak 1.109). The accents stay soft after the raise: trumpet accent attacks measured 2-5 kHz first 80 ms minus body median -1.2 / -2.0 / -3.9 dB, max +3.1 (acc.py), and a gain change does not alter that ratio.

## 2. The suspended-cymbal crescendo peaks 1.2 s before the crash and is fading when the crash arrives (Suspended cymbal, bar 159, qn 632-636)

What is wrong: the score has a pp roll with a crescendo across bar 159 into the fff crash at qn 636 (bar 160). In the render the roll swells, peaks on beat 2 and then decays for the last second of the bar. The gesture is reversed: the crash comes in after a diminuendo.

Evidence (measured, perc.py, 0.1 s RMS frames): the cymbal note starts at qn 632 (352.51 s). The stem reaches its peak, -27.9 dB, at 353.3-353.5 s, about 0.9 s after the start. At the crash (qn 636 = 354.49 s) the cymbal is already at -44.3 dB, 16 dB under its own peak. Its 4-12 kHz band falls from 37.2 to 20.5 over the same second. parts.json: key 60, velocity 105, no lead. score_config.py PERC_MAP has no lead_s for the cymbal, although the brief requires the crescendo peak to meet the crash.

The patch (18in Zildjian Sus Cymbal Cres.oib, read by script) maps four recorded crescendos to keys 60/62/64/65 (f layer from velocity 90, p layer below, two round robins). The sample lengths grow with the key: f1 8.3-9.3 s, f2 9.8-10.1 s, f3 10.2-10.9 s, f4 11.5-12.1 s (frame counts from the .ews headers). Key 60 (f1) is the shortest. Bar 159 lasts 1.98 s at the tempo in force.

Fix: in build/score_config.py PERC_MAP["Suspended cymbal"]["ridecymbal"] use "key": 64 and "lead_s": 0.5. This is inferred: if every sample rings out about the same 8.4 s after its peak, the f3 crescendo peaks about 2.4 s after its start, so a 0.5 s lead puts the peak on qn 636. The roll then starts about 0.25 qn before the printed bar, which is not audible at pp. In the c01 render, measure the cymbal stem's peak time and set lead_s = (peak time - start time) - 1.98 s so the peak falls within 0.1 s of 354.49 s. Keep velocity 105.

## 3. Low end: a narrow peak at 90-110 Hz and too little 125-250 Hz in the loud tutti (Double basses, Violoncellos; worst on the G and A-flat pedals)

What is wrong: the low end is not too heavy overall. Its shape is wrong: one band booms and the body above it is thin. Third-octave levels relative to 500 Hz-2 kHz (third.py; the mvt II c26 final master uses the same library and hall, and the Dvorak 9/i master is a second reference):

| frames | 63 Hz | 80 | 100 | 125 | 160 | 200 | 250 |
|---|---|---|---|---|---|---|---|
| loudest 10%, mvt1 c00 | -27.9 | -26.8 | **-11.7** | -17.3 | -16.0 | -11.0 | -14.3 |
| loudest 10%, mvt2 c26 | -19.0 | -23.9 | -15.0 | -14.2 | -12.8 | -8.6 | -10.4 |
| loudest 10%, Dvorak 9/i | -36.3 | -24.2 | -16.6 | -8.7 | -6.2 | -9.1 | -10.6 |
| middle 60%, mvt1 c00 | -21.2 | -19.9 | **-10.1** | -14.2 | -11.7 | -9.6 | -10.4 |
| middle 60%, mvt2 c26 | -21.0 | -19.3 | -12.0 | -13.8 | -8.8 | -10.2 | -9.0 |

In the loud tutti the 100 Hz band is 3.3-4.9 dB over both references, and 125-250 Hz is 2.5-4 dB under mvt II and 4-10 dB under Dvorak (measured). The 60-100 Hz band share of total energy is -14.7 dB against -19.1 (mvt II c26) and -21.8 (Dvorak) (low.py). The Brahms 1/ii and 4/ii shares in metrics.md (-8.5/-7.9 dB at 20-100 Hz) come from slow movements with a strong 62.5 Hz band and are not a target for this.

Where it comes from (measured, lowstems2.py, fund.py, barlow.py):
- In the loudest frames, the basses supply about 60% of the 89-112 Hz band. They supply little of 112-180 Hz; timpani, tuba and celli supply that.
- The basses' fundamentals are uneven, as LEARNINGS section 14 records. Fundamental relative to harmonics 2-4: F2 +5.8, G2 +3.3, Ab2 +4.6, B1 +0.6, D2 -2.6 dB, while C2 is -10.0, G1 -18.9 and Ab1 -19.2. The movement's most frequent bass notes are C2 (28), G1 (21) and Eb2 (15). G1 and Ab1 put their strong second harmonic at 98 and 104 Hz, which is the hot band.
- The bars where 89-112 Hz equals or exceeds the whole 250 Hz-2 kHz band: 84 (+8.2 dB, basses G1 + celli G2 at CC11 114), 130 (+2.7), 127-129, 73-76 (basses Ab1 alone, +0.2 to +2.6), 175 and bar 1 (celli G2). Across all bars the median is -27.9 dB.
- The existing body bell (160 Hz +4.5 dB, 1.4 oct) reaches down to about 100 Hz, so it lifts the hot band too (inferred from the bell width). The 80 Hz -6 dB cut sits below the problem; the 63 and 80 Hz loud bands are already 4-9 dB under mvt II.
- mvt II used `loud_eq` (wet-automated 150 Hz bells on celli and basses at the ff tutti, LEARNINGS section 14, c16) to get the loud 125-160 Hz body. The c00 mix dropped it because its points were keyed to mvt II onsets.

Fix in build/mix.json:
- Double basses `eq`: change `bell2` from 80 Hz -6 dB bw 1.0 to 100 Hz -5 dB bw 0.8. Move `bell` from 160 Hz +4.5 dB bw 1.4 to 180 Hz +4 dB bw 1.0.
- Add `loud_eq` to Violoncellos and Double basses: `{"points": [...], "bands": [{"band": "bell", "hz": 160, "db": 4, "bw_oct": 1.0}]}`, with Wet at 1 over the loud tutti and ramps of 2 qn. The spans are the bars where the c00 master is above about -18.5 dB: qn 94-104, 110-128, 318-332, 458-496, 518-536, 550-568, 626-646, 662-680. The points are `[[94,0],[96,1],[104,1],[106,0],...]` and so on.
- Targets for c01: in the loudest 10% of frames, 100 Hz within 1.5 dB of mvt II c26 (-15.0), and 125-200 Hz raised by 2-3 dB. In bars 73-76, 84 and 127-130, 89-112 Hz should be at least 3 dB under the 250 Hz-2 kHz band. Check that 63 Hz does not fall further.

## 4. Tam-tam and crash cymbals are too small for their printed fff (Tam-tam qn 484, bar 122; Crash cymbals qn 636, bar 160)

What is wrong: both strokes mark the two climaxes, and both pass quickly in the render.

Evidence (measured, perc.py):
- Tam-tam fff heavy beater, qn 484 (276.9 s): the stem peaks at -25.1 dB at +0.5 s, while the master is at -12.3 dB at that moment. That puts the tam-tam 13 dB under the orchestra. In 4-12 kHz it is 10 dB under the master (31.6 against 41.7). The sample is long (17-19 s; Lng V11/V12 headers) and the stem decays smoothly. The problem is level, not length.
- Crash cymbals fff, qn 636 (354.49 s): the stem peak is -24.7 dB, and at the hit it makes up most of the master's 4-12 kHz (42.3 against 43.0). Then it falls 21 dB in 1.5 s, and one second after the hit the master's 4-12 kHz is back to 34.5, below its level just before the hit (36.6). The 19in Zildjian A Crash "Long" samples at velocity 120-127 are only 6.2-8.8 s. The other HO pairs are longer: 22in Zildjian K Crash (Crash Cymbal 01) 9.4 s, 20in Constantinople Crash 9.7 s, 20in Zildjian Crash 8.8 s (header frame counts).

Fix: in mix.json raise the Tam-tam gain_db from -4 to +1. The target, inferred, is the tam-tam's 4-12 kHz within about 4 dB of the master's for the first 2 s after qn 484. In score_config.py TRACKS, replace the crash patch with `Cymbals/Cymbal Pairs/22in Zildjian K Crash.oib` (or 20in Constantinople Crash), key 60 (Long), keeping velocity 124 and min_s 9. Whether the longer pair rings audibly into bar 161 under the largamente tutti is inferred; measure the stem's 4-12 kHz 2 s after the hit in c01 and compare with the c00 figure (12.8 at +2.0 s).

## 5. Small seating points (inferred, low priority)

The seats measured as set (depth.py, sustain R-L): Vln I -8.1, Vln II -1.7, Vla +2.3, Vc +6.5, Cb +5.1, horns -1.9 to -5.3, trumpets +0.2 to +4.5, trombones +4.1 to +6.4, tuba +4.6 dB. The three percussion tracks sit apart (tam-tam -0.15, crash +0.10, suspended cymbal +0.25), and the timpani are at -0.05 with width 0.6. In most stage layouts the percussion stands together at the back on one side of the timpani. Moving the three cymbal and tam-tam seats to one area (for example +0.25 to +0.35, width 0.4) would place them as one section. This is a matter of placement only; nothing measured is wrong. Do it only if it is free while making the percussion changes above.

## Do not touch

Measured and right, keep: the shared true-stereo hall (`S. Cal Hall Perc TS FR 3.3s`, fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends). Master cutoff decay at bar 170: 14.4 / 21.3 / 32.1 dB at 0.3 / 0.6 / 1.0 s (references 13-17 dB at 0.3 s). Release tails centred within ±3 dB R-L on every stem. Master stereo image: correlation 0.512, side/mid -4.9 dB, below 250 Hz 0.61, 250 Hz-4 kHz 0.51, above 4 kHz 0.48 (Brahms 1/ii 0.512 / -4.9 / 0.60 / 0.48 / 0.38; Brahms 4/ii 0.554 / -5.4). This includes the side-only shelves and the Vc/Cb widths of 0.28. The per-family mic and send settings: tail drops of 15-22 dB at 0.3-0.5 s across all families, with no family drier or wetter than the rest. The 2-6 kHz and 6-20 kHz shares in the loudest frames (-11.5 / -29.0 dB, against mvt II c26 -11.5 / -30.6 and Dvorak -10.9 / -28.2). No loop pulsing at 3.95 s on the final chord, the G pedal at bars 127-130 or the opening timpani roll: 100-300 Hz and centroid autocorrelation at the loop lag -0.28 to +0.12. GENTLE_ACCENT on the brass: trumpet, trombone and horn accent attacks are 1-4 dB under the note body in 2-5 kHz.

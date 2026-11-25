# Cycle 4 changes (actor)

Input: critic reports A (articulation), B (balance), C (holistic) on the cycle 3 render. Snapshot: `before/` (tools + build JSON, taken 01:18 by the first attempt).

## How this cycle ran

- The first attempt (2026-10-11, 01:18-01:52) made the tool and config changes below, rendered once (`pass1/`, metrics only), adjusted mix.json, roles.json and note_trims.json from pass1 (01:39), applied them with `--mix-only`, and started a second render. The Mac froze during that render and was reset; the partial stems were deleted.
- The resumed attempt found REAPER reopened with the project. A state query (notes, keyswitches, tempo markers, envelope points, widths, ReaEQ per track) matched `build/parts.json` and `mix.json` exactly, and a regenerated parts.json was byte-identical, so nothing was rebuilt before rendering.
- Renders in the resumed attempt:
  - `pass2/`: first render, cold disk cache after the reboot. The timpani strokes at qn 277 and 278.5 were missing (-94 and -117 dB), and the bar 63 strings had a hole.
  - `pass3/`: after the fixes listed under "After pass2".
  - final `render/`: with the A #3 timing turned off (see below).
- Each pass directory holds `metrics/`, the mp3, and `check.txt` (actor checks). `pass2/parts.json` is the data pass2 was rendered from.
- Analysis scripts: `/private/tmp/claude-501/mockup-loop/c04-actor/`.
  - `check.py <cycle> [parts]`: A-weighted climax balance, same-patch correlations, low bands, stereo correlation, bar 63 and bars 64-66 string levels, cello countermelody.
  - `late6.py`: late attacks.
  - `state.lua` + `cmp.py`: REAPER state against parts.json and mix.json.

## What changed

### tools/score_to_parts.py
- **Harp arpeggios (A #1).** `build/mockup.ly` now logs `arpeggio-event`. Each rolled chord is sorted across the marked staves and played lowest first, with note k sounding k x 0.040 s late (0.030 s above mp). The delay is stored as a negative lead, so `sq` stays the score onset. The top note gets +4 velocity. This gives 33 rolled chords.
- **Same-patch unisons (A #2, simpler alternative).** `find_unisons()` works on wind and brass tracks that share a patch file. Where two of them play the same pitch, within 0.01 qn and overlapping more than 0.25 qn:
  - The note kept is a slurred note first, then the longer note, then the earlier track. The copies are dropped and the kept note gets +10 log10(n) dB in vol_db.
  - The pair is left alone when a copy holds more than 1 qn longer than the kept note (Cl qn 250).
  - Result: Hn1 keeps 261-271 (Hn2 x8 and Hn4 x1 dropped), Cl1 259, Ob1 210, Bn1 196.
  - No separate a2 horn track was added.
- **Portato in wind slurs (A #4).** A tenuto note inside a slur uses Sus MAX / Sus Max / Sus Non Vib instead of Leg Slur.
- **Woodwind legato lead (A #5).** `LEG_LEAD_S`: cor anglais 0.08 s, flute 0.03 s, clarinet 0.03 s. Cor anglais legato velocity is now 100/90/80.
- **sf shape (A #3).** From f or louder the spike is level+8 (ff 114 -> 122), held to q+0.25 at spike-6, and reaches the post level at q+0.75.
- **A #3 timing, implemented and then turned off.** `TREM_TIMING_C04 = False` disables two changes: the tenuto crossfade into another articulation, and the 0.05 s tremolo lead.
  - Both are still in the code behind that flag.
  - With them on (pass2, pass3), Vln I/II and Vc on the bar 63 downbeat had a 0.4-0.5 qn hole (-15 to -25 dB).
  - With them off (final), the hole is still there, so the timing was not its cause. See Open.
- **Vibrato (C #3).** CC1 now follows the musical role:
  - Flutes, oboes, cor anglais, bassoons and strings in melody spans: target 100 (strings 95). Every slurred note of a flute, oboe or cor anglais counts as melody.
  - Delayed vibrato on phrase starts of 0.8 s or more: target - 35 at the onset, reaching the target at 40% of the note. Long legato notes (1.8 s or more) dip by 20 instead.
  - +10 on the highest note of each slur.
  - Elsewhere CC1 follows the level: pp 42, p 55, f 90, ff 98. Flautando uses 20.
  - Horns, trombones, tuba, clarinets, bass clarinet and contrabassoon keep the c01 formula.
- **Soft re-attack bloom (C #5).** A soft string note (p or softer) on Leg Slur MAX that re-attacks after a short gap and lasts 2 qn or more gets vol_db from 0 to -4.5 dB over 2 qn (`bloomv`, 4 Vc notes and others). The bow-change notch at CC11 <= 40 is 8 instead of 14.
- **Caesuras (C #6).** `CAESURA = {204: 0.22 s, 268: 0.15 s}`. The 0.25 qn before each breath is slowed, 56.25 -> 30.8 bpm and 46.7 -> 31.8 bpm (+0.220 s and +0.150 s exactly).
- **Note-end guard (actor, after pass2).** A note ends 0.005 qn before a later note on the same track when that note has the same pitch, or is a tremolo onset within 0.1 qn of the note's end. pass2 had Vln I E6 / Vln II E5 overlapping their own tremolo re-attack (end 212.02, new onset 211.955). The guard trims 4 notes while the timing flag was on; with it off it trims none.

### tools/build_reaper.py
- mix.json `eq` per track inserts a ReaEQ after Opus: band 0 low shelf, band 1 bell; unused bands at 0 dB and band 4 disabled. Values are set by searching the normalized parameter against ReaEQ's displayed value. The EQ is applied on rebuild and by `--mix-only`.

### build/ (config)
- **`mix.json`**
  - Widths (C #2): wind 0.5, horn 0.6, lowbrass 0.5, timp 0.6, harp 0.55, Double basses 0.6. C asked for 0.7-0.8; the first attempt set these from pass1.
  - ff trims (B #1, C #1): Fl1/Fl2 -6 -> -1, Ob1/Ob2 +3 -> 0, Cl1/Cl2 -1 -> -3, Cbn +4 -> +1, Vln I -1.5 -> +1.5, Vln II -3 -> -1.5.
  - EQ (B #2, C #4): Double basses low shelf 90 Hz -7 dB plus bell 150 Hz +3 dB (bw 1.4 oct); Contrabassoon and Tuba low shelf 70 Hz -4 dB.
- **`roles.json`**
  - Vc (B #1, B #3): [66,78,-1] [78,90,-6] [204,212,-3] [238,250,-3] [250,274,-5].
  - Cb (B #2): [66,90,-4] [172,188,-2] [262,276,-2].
  - Vln II (B #4, C #5): [212,216,-6] [216,218,-8] [218,220,-2] [220,227,-3].
  - Vla [108,124,-4] and Harp [108,124,-4] [172,188,-4] (B #5).
  - Flute 1 [262,270,-2].
  - Vln II 216-220 was split and Vc 238-250 changed from -1 to -3 after pass2: pass2 had Vln II beats 3-4 of bar 64 9-13 dB under Vla/Vc, and Vc only 2 dB under Vln I at qn 240.
- **`note_trims.json`**: Vc {3: -5, 238: -10}, Fl1 {262: -6}, Fl2 {262: -2, 266: -3}, Ob2 {262: -4}, Bn1 {262: -3}, Vla {220: +4}.

## Rejected or deferred
- A #2 full version (a "Horns 1-2 a2" track on the 2FH KS Master): deferred. The drop-and-boost alternative removes the doubled sample.
- A #3 timing (crossfade, tremolo lead): implemented, measured no better, and turned off. Kept in the code behind `TREM_TIMING_C04`.
- A #6 divisi/solo tracks (Vc DIV B, Vln I DIV A for the solo): deferred again, as lower priority than 1-5.
- B #4 Vc {3: -5}: done. C #4's optional string high shelf: deferred.
- C #2 widths: applied at 0.5-0.6 instead of 0.7-0.8. The master correlation target (0.60-0.68) was met at these values.

## Measured, c03 -> c04 (final render)

| | c03 | c04 |
|---|---|---|
| Integrated / LRA / true peak | -28.1 LUFS / 24.0 LU / -10.2 dBFS | -28.2 LUFS / 24.2 LU / -9.5 dBFS |
| 63 Hz / 125 Hz third-octave re 1 kHz (ref -6.2 / +7.0) | +5.4 / +3.3 | +1.1 / +3.8 |
| 40-90 Hz re 200-1000 Hz, bars 61-62 / 23-28 | -9.3 / -7.3 | -12.9 / -15.7 |
| Vln I minus loudest single wind, A-weighted, bars 61 / 62 / 79 / 80 | -0.9 / -1.8 / -3.3 / -3.9 dB | +3.6 / +0.8 / -0.5 / -0.8 dB (the loudest wind is now a flute doubling the tune; oboes, clarinets and bassoons are 2-6 dB under Vln I) |
| Hn1/Hn2 correlation, qn 261-270 | 0.999 | no Hn2 copy (Hn1 -38.1 dB alone, was -41.7 per horn) |
| Cl1/Cl2 qn 259 and Ob1/Ob2 qn 210 correlation | -0.59 / 0.996 | single note on each |
| Stereo correlation, master / Ob1 / Hn1 / Harp / Timp | 0.76 / 0.91 / 0.94 / 0.95 / 0.78 | 0.64 / 0.74 / 0.74 / 0.85 / 0.55 |
| Vc countermelody qn 68-77: Vc / Vln I / Cb | -54.2 / -43.0 / -48.2 | -49.1 / -43.6 / -53.2 |
| Vc countermelody qn 240-249: Vc / Vln I / Cb | -54.1 / -46.1 / -54.8 | -49.7 / -45.6 / -55.2 |
| Vln II / Vla / Vc qn 216-217 | -45 / -54 / -48 | -54 / -53 / -48 |
| Harp rolled chords | 0 | 33 (35-40 ms steps in the data) |

## Open
- **Bar 63 downbeat (qn 212).** Vln I, Vln II and Vc have a 0.4-0.5 qn hole (-15 to -25 dB) and the tremolo sounds at about 212.45. This held in all three resumed renders, with and without the A #3 timing.
  - c03 had the same timing and a shorter hole (A: 9-13 dB, peak at +0.14 s).
  - What differs from c03 at that spot is CC11 (c04 holds 122/119/116 until 212.25 where c03 fell to 113/99) and CC1 (100 against 84-87).
  - The Vln I KS Master's Tremolo groups (pp/mf/f/ff, `groups[833-841]`) have no CC1 conditions. CC1 is therefore unlikely to be the cause.
  - Inferred: the violin tremolo does not sound while CC11 is high (above about 110), which would also explain c03's shorter hole.
  - Next step: a short range render of bars 62-63 (Vln I/II only) with the tremolo CC11 capped at 108, taking the sf weight from vol_db.
- **Late attacks.** Attacks more than 0.3 s late (`late6.py`): 29 in c03, 46 in c04.
  - The new ones are mostly soft string and viola entries: Vla qn 124-134 and 199-210; Vc 66 and 108-116; Vln I 48, 60 and 237.
  - Inferred cause: the delayed-vibrato CC1 dip at the onset, plus the vol_db ramps of the new roles. Check whether to drop the dip for strings.
- Timpani pp strokes at qn 277 and 278.5 were missing in pass2 (cold cache) and are present in the final render.
- 63 Hz is +1.1 dB, against targets of 0 to +1. 125 Hz is +3.8, against a target of +5.

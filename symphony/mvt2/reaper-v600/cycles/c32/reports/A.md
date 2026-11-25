# Cycle 32, critic A: articulation and phrasing (on the c31 render)

Sources: `cycles/c31/render` stems and master (after the stem fix), `cycles/c31/render_first`, `cycles/c29` and `c30` renders for comparison, `cycles/c31/CHANGES.md`, `cycles/c31/before/parts.json` (the c30 state), `build/parts.json` (the c31 state as rendered and stem-fixed), `build/score_config.py`, `build/note_trims.json`, `build/entry_leads.json`, `build/rebow_fills.json`, `build/mockup-events.tsv`, the score (`v600/score.pdf` pages 3 and 5), `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, the installed Basses Divisi and Celli Divisi folders, the May 2021 HO manual PDF pp.100 and 103-107 (row A5 of `loop/MANUAL-READING.md`, cycle 32), `guides/eastwest-hollywood-orchestra/DIGEST.md`, `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md`, `loop/LEARNINGS.md`, the c31 critic A report.

Times are score qn unless marked s. Levels are plain RMS of a stem or the master in 30-150 ms windows (the window is given where it matters). Band levels are FFT energy in 2-5 kHz over the stated window; they are comparable across renders, not absolute. Scratch scripts were deleted after use.

## Manual notes (A5, PDF pp.100, 103-107: Hollywood Brass)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Instruments: Solo French Horn, Solo Trombone, Solo Tuba, 2 French Horns, "2 Trombones [new]", 2 Trombones and 1 Bass Trombone (p.100) | Horns 1-4 on 1FH, Horns 1-2 a2 on 2FH, Trombones 1-2 and bass trombone on 1TB, tuba on 1TU | Yes, except the bass trombone, which plays the tenor Solo Trombone (its D2 at 218 lies under the patch's sample range; MANUAL-GAPS #12). No unison in v600 calls for "2 Trombones". |
| Repetitions patches (3 tempos), Triple Performance, Double Tongue (p.103) | none: v600's brass has no fast repeated notes | Not applicable. |
| Sforzando Crescendo, Solo Horn and Solo Tuba: accented attack plus strong crescendo, velocity sets both (p.103) | none printed (no brass sfz <) | Not applicable. |
| Effects: trills, rips, shakes, recorded crescendos (Fast/Medium/Slow; "Crescendo MOD SPEED" picks the speed by CC1 1-42/43-85/86-127), flutter, clusters (p.104-105) | the brass crescendos into bars 61 and 79 run over several notes | Not used, correctly: the recorded crescendos are one-note gestures. The KS Masters load them (1FH keys 91-93, 1TB 80-82). |
| Legato: a slur only with no gap and within an octave; trombone slide legato; monophonic by default, CC22 0-63 polyphonic (p.105) | Horn 1's solos, Horns 1-4 and a2 legato rows, Trombone 1's quotation | Followed (measured on parts.json): no chord on any Leg row, no slurred join over 12 semitones on any brass track, overlaps inside every slur, gaps of 0.03-0.07 qn where a slur ends. "Leg Slide" (1TB key 97) is loaded in the map but not needed: the quotation has no glissando. |
| Legato Slur: volume on the Mod Wheel (CC1); low-pass opens toward overblow near CC1 127; velocity = transition speed (p.106) | every brass Leg row (CC1 dynamics since c30, horns on the soft map since c31) | Followed. Brass legato targets play v124 (horns) and v100-112 (Trombone 1), i.e. fast transitions; brass CC1 tops out at 103 (Trombone 1 at 218), so no overblow filter is reached. |
| Legato Slur Accent: accent at the attack, strength by velocity (p.106); 1TB key 73, 1FH 83, 2FH 82 | Trombone 1's slurred accent at 213 | Not used (Leg Slur MAX plus a swell). Not recommended: the accent samples were the source of Dan's "harsh" note (S1 c24-c26). Finding 1 restores the c30 attack instead. |
| Legato Slur Repetitions: re-tongued sample for same-pitch notes inside a phrase (p.106) | Trombone 1 215.5 -> 216 (A3 repeated), not slurred | Not needed: the repeat dips 5.6 dB on the stem, 5.2 on the master (S1 passes). |
| Slur Runs: portamento slur for seconds (p.106) | none in the brass | Not applicable. |
| Mutes: 06 Mutes folder; the stop is the horn's hand mute (p.106-107) | Horn 3 con sord. from 286 | The Solo French Horn has only stopped-horn patches (MANUAL-GAPS "not applicable"), so the `mute_eq` emulation stays. CC15 placement correct (271.5, in rests, before 286). |
| Keyswitch Masters: blue keys select rows (p.107) | every KS track | Followed (measured): every keyswitch precedes its note (none less than 0.005 qn ahead), no keyswitch changes a row under a sounding note on the brass. |
| MANUAL-GAPS #9 (Port Lng / Portato rows for tenutos) | bars 61-62 tutti tenutos, Horns 1-2 bars 80-81 | Not needed now: the tutti tenutos re-articulate 1.3-2.0 dB on the master with no hole (measured, table under "Smaller observations"). |

## Findings, ranked by what a listener would hear

### 1. Trombone 1, bars 63-64: since c31 the slurred accent at 213 has a bright, loud head again (Dan's item 9), and in bar 64 the tenuto and the second accent are weaker than the unaccented eighths around them

- **Where.** Trombone 1, qn 212.5-219.5 (ff marcato quotation; accents at 213 and 218, tenuto at 216; slurs 212.5-213, 214.5-216, 217-217.5; decrescendo from 218 to p at 219.5).
- **213: what changed (measured).**

  | 213 (C4, slurred target of the 212.5 pickup) | c29 | c30 | c31 |
  |---|---|---|---|
  | Trombone 1 2-5 kHz, first 80 ms | -16.2 | -11.2 | **-0.8** |
  | Trombone 1 2-5 kHz, 0.08-0.3 s | -8.7 | -2.9 | **+2.6** |
  | Trombone 1 peak (30 ms) in 0.05-0.3 s | -22.7 dB | -21.3 dB | **-17.8 dB** |
  | master 2-5 kHz at 0.08-0.3 s minus the 0.3 s before | | -0.3 dB | **+3.9 dB** |

  - The note then falls 13 dB inside the ff dotted quarter: 50 ms frames -20, -18, -19, -20, -22, -25 ... -31 dB by 214.2. c30: -22 to -29. c29: flat at -24..-27.
  - The only MIDI difference at 212.5-213 between c30 and c31 is the pickup: it now starts at 212.455 instead of 212.401 (c31 C #5 removed the brass entry lead; velocity, CC and the 213 note itself are unchanged). The legato transition into 213 plays a brighter, louder sample.
  - The c31 stem fix (note trims 213 -3.5, 215 -2.2) did not reach the head: note trims ramp in over 0.6 s. `render_first` has the 213 peak at -17.4 dB, the stem-fixed render at -17.8. The trim only deepened the fall after the head.
  - Series 1 c26 fixed Dan's harsh-accent note by taking the master's 2-5 kHz jump from +10 to +2 dB. It is now +3.9 dB over the bar's ff tutti, with a peak 3.5 dB over c30's. That is the same kind of bite he objected to (inferred from his note and these numbers; not heard).
- **Bar 64 (measured, 30 ms frames).**
  - The tenuto A3 at 216 (Sus MAX, v100): body -29.4 dB. The unslurred eighth before it (215.0) is at -21.5 and the slur's last note (215.5) at -25.6.
  - The accent at 218 (Sus MAX, v92, swell +6.5 dB) peaks at -23.3. The unaccented 217.5 eighth before it peaks at -21.6, inflated by the c29 +2.5 dB shape at 217.5.
  - CC11 starts the decrescendo at 218.125 (114 -> 108 -> 103 ...) and CC1 falls with it (103 -> 42). On the allargando's tempo map that is 0.17 s after the onset, so the accent is 1.4-1.7 dB under the note it should stand out from, and it is already falling by +0.25 s.
  - c29 intended the opposite: "the 218 accent ... sits 2-4 dB over the raised 217.5" (`score_config.py` c29 block). The c31 numbers do not meet it.
- **Fix.**
  - (a) Restore the c30 pickup timing: `build/entry_leads.json` `"Trombone 1": {"212.5": 0.11}`. That is 0.11 s, which puts the note-on back at 212.401 on the local tempo. Remove `note_trims.json` `"Trombone 1"` 213 -3.5 and 215 -2.2: they compensated the c31 change. Pass: 213's 2-5 kHz first 80 ms within 2 dB of c30 (-11), peak -21 ±1 dB, and no fall of more than 8 dB before 214.4. The S2 cost is small: c30's start read -0.13 s on the probe against -0.02 now, and the pickup is an upbeat eighth into a slur.
  - (b) 216 tenuto: add `(216.0, [(-0.02, 0.0), (0.05, 3.5), (1.0, 3.5), (1.1, 0.0)])` to `LEVEL_SHAPES_S["Trombone 1"]`. Target body -26 ±1 dB, about level with 215.5 and 217.
  - (c) 217.5: delete the `(217.5, [(0.0, 0.0), (0.08, 2.5), (0.45, 2.5), (0.55, 0.0)])` shape from the c29 block (keep `SLUR_PAIR_RELEASE_DB_AT` 0).
  - (d) 218: let the accent speak before the decrescendo. Add a generic option in `tools/score_to_parts.py`, `HP_AFTER_ACCENT_S = {}` (default off): a decrescendo printed on an accented note starts its CC11/CC1 fall that many seconds after the onset. Movement II value `{"Trombone 1": 0.3}`. This is mockup-kit LEARNINGS §7, "start the hairpin after the spike". If the actor prefers no tool change, hold the level in vol_db instead: `(218.0, [(0.15, 0.0), (0.25, 1.5), (0.34, 3.0), (0.5, 2.0), (0.7, 0.0)])`. Rising post-hall changes do not cut a tail.
  - Pass for (b)-(d): 218 peak 2-3 dB over 217.5's peak; 2-5 kHz first 80 ms of 218 still at least 6 dB under its 0.08-0.3 s level (now -14 dB); the line 219.5 still arrives at p.
- **Evidence.** Measured (stems, three renders, parts.json diff); harshness to the ear inferred.

### 2. Double basses: every second re-bow piece of the long pedals plays a bow-direction sample that swings 11-14 dB, a slow wobble in the "4 soli" pedal of bars 65-70 and the coda pedal

- **Where.** Double basses, E flat 2 pedal qn 220-238 (bars 65-70, "4 soli, sul A, change bow at will", under Horn 1's solo and the ppp roll) and A flat 1 pedal qn 271-286 (bars 81-86, coda).
- **What is wrong (measured).** The spread is p90-p10 of 100 ms levels with vol_db subtracted, from 0.4 s after each piece's start:

  | piece (qn) | 220 | 221.8 | 225.215 | 227.775 | 230.393 | 233.038 | 235.659 | 273.229 | 276.05 | 278.351 | 282.203 | 283.605 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | spread dB | 11.1 | 5.3 | 12.3 | 5.9 | 13.6 | 5.7 | 12.1 | 11.4 | 5.2 | 11.7 | 2.3 | 10.3 |

  - The pieces alternate strictly within each pitch. The unsteady ones swing about once every 1-1.5 s. At 226.8-227.7: -54, -60, -60, -55, -57, -51 dB, against a steady -50..-53 in the next piece.
  - DIGEST (manual p.91): "Bow direction alternates by round robin (up/down)" on Sus MAX. So the up/down alternation of the re-bows lands one bow's sample, which beats strongly at these two pitches, on every other piece.
  - No other string section shows the alternation. Their pieces read 3-10 dB with no pattern (Violins I-II, violas, celli, both div tracks; niente pieces excluded).
  - No 3.95 s loop pulse anywhere: level and centroid autocorrelation at 3.95 s is at most 0.28 on every stem and at most 0.13 on the master, over bars 1-3, 65-70, 83-86 and 87-92. The c26-c29 re-bow work holds.
  - On the master the wobble is partly masked by the horn solo, the timpani roll and the coda harp. The master's 100 ms spread does not alternate. But the basses are the loudest stem at 225-226 (bar 66, the upper strings' niente) and at 276-279, and the master steps -47 -> -53 dB at the 225.215 piece. Audibility is inferred: a slow "wah" in the exposed pedal, the kind of periodic movement BRIEF item 8 says measurement tends to miss.
- **Fix.**
  - (a) MANUAL-GAPS #10, applied where it matters. A generic `RR_RESET_AT = {track: [qn, ...]}` in `tools/score_to_parts.py` writes Opus's round-robin reset controller, CC16 (`Preferences.json` `RoundRobinResetCC: 16`, DIGEST CC36 row; the CC36 the pipeline sends is a Repetition-script reset), 0.05 qn before each listed note.
    - Movement II value: `{"Double basses": [221.8, 225.215, 227.775, 230.393, 233.038, 235.659, 273.229, 276.05, 278.351, 282.203, 283.605]}`, plus 220 and 271. Every piece then starts the cycle on the same bow.
    - Render and re-measure the per-piece spread. If every piece is now steady, refit these fills with `fit_rebows.py`.
  - (b) If (a) makes every piece unsteady (the reset lands on the bad bow), remove it. Re-time the re-bows instead (`rebow_moves.json`) so that the unsteady-parity pieces last 1.5-2.0 s and the steady ones 4.0-4.4 s, then refit. That cuts the wobbling share of the pedal from about 55% to about 30%.
  - (c) The idiomatic patch for "4 soli" is `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` (installed; MANUAL-GAPS #8). It has different samples, and four players change bow at will. It costs one Close-only instance (about 0.7 GB, at the 45 GB cap), so it is a second-pass option, not this cycle's.
- **Check.** Per-piece spread at most 7 dB on all pieces of both pedals. Re-bow dips at most 4 dB on the stem. Master 220-238 with no step over 3 dB at a re-bow.
- **Evidence.** Measured on the stem; cause read in the digest (p.91) and inferred from the strict alternation; master audibility inferred.

### 3. Violas' sotto voce portato, bars 48-51: as loud as the cor anglais solo at the start, and uneven by pitch (A3 3-7 dB over the other notes)

- **Where.** Violas, Detache row, qn 152.5-167.5 (15 offbeat portato eighths, pp, "sotto voce"), under the cor anglais "solo, espr." (p).
- **What is wrong (measured, 30 ms peaks within -0.1..+0.6 s of the beat).**
  - The seven A3s (152.5, 153.5, 154.5, 156.5, 157.5, 160.5, 161.5) peak at -43.4..-43.8 dB. The other pitches peak lower: B3 158.5 -47.4, A flat 3 159.5 -45.6, D4 162.5 -50.7, B3 163.5 -48.1, E flat 4 164.5-167.5 -46.4..-47.2.
  - In bar 48 (152.5-155) the portato peaks equal the cor anglais's held note: peak minus CA +0.2, +0.1, +1.1 dB. The c28 pass criterion (MANUAL-GAPS #2) was 7-9 dB under. From 158.5 on it is 6-12 dB under.
  - Separation is good: 26-36 dB drop in each rest.
  - Attack timing (S2): the energy centroid of the first 0.45 s sits at +0.10 s on the A3s (entry lead 0.22 s) and +0.12..+0.17 s on 158.5-163.5 and 165.5/167.5 (lead 0.12 s). It is +0.044 s on 164.5/166.5 (lead 0.27 s), early against the others by about 0.07 s.
- **Fix.**
  - The Detache level lives in CC7 since c29 (Do-not-touch: keep it there). Lower the CC7 for the A3 notes by 3 dB (CC7 x 0.71, written in the rest before each note). Raise D4 162.5 by +3 dB and the B3s 158.5/163.5 by +1.5 dB. CC7 changes in the rests cut no tail.
  - `entry_leads.json` Violas 164.5 and 166.5: 0.15 -> 0.08 s.
- **Check.** All 15 peaks within ±2 dB of each other. Bar 48 peaks at least 4 dB under the cor anglais, with no change after 158 relative to it. Centroids within +0.08..+0.16 s.
- **Evidence.** Measured.

### 4. Violins II div. sul tasto, bars 37-40: the divisi pad's top voice is 5-8 dB under its bottom voice

- **Where.** qn 108-124. The lower voice is on Violins II (full-section KS Master, Flautando, with the divisi cut). The upper voice is on Violins II div (DIV B half section, Close mic, highshelf -6 dB at 1.5 kHz since c29).
- **What is wrong (measured, 200 ms windows).**
  - Lower/upper: 110.3 -45/-54, 112.6 -50/-53, 114.6 -47/-50, 116.4 -51/-55, 118.4 -47/-53, 120.4 -51/-55, 121.4 -52/-58 dB.
  - The sum is steady at -45..-51 with no trough over 3 dB, so the c15-c16 overlap work holds.
  - "div." means two equal halves of the section. Here the top voice of the harmony (A flat 4 / B flat 4 / G flat 4) sits under the bottom. Judgement on the music inferred.
- **Fix (levels only, so stem_fix can apply it).**
  - Roles over [107.9, 124.0]: Violins II div +3 dB, Violins II -2 dB. Put the Violins II cut in CC7 (its notes are tied across the window ends, so a vol_db step would cut a tail). Ramps 0.25 qn at both ends.
  - The DIV B track's highshelf stays: the issue is level, not colour.
- **Check.** Upper minus lower within ±1.5 dB in each half bar. Sum within 0.5 dB of c31. No new trough at the re-bows 110.053/113.7 (now 2.2/6.4 dB on the stem).
- **Evidence.** Measured. The better patch (a 2nd Violins DIV A for the lower voice) would be another instance; not proposed.

### 5. Violins II portato pairs, bars 15-21 (S1): the new-bow tenuto repeat at 45 and the merged tenuto at 50 are not heard as separate notes

- **Where.** Violins II, "aes'2--( aes'4--)" pairs under the oboe and the solo violin.
- **What is wrong (measured; dip = level -0.4..-0.1 s minus the minimum within -0.1..+0.25 s).**

  | qn | what it is | stem dip | master dip |
  |---|---|---|---|
  | 44 | merged repeat, CC11 notch 48 -> 44 | 7.0 | 4.4 |
  | **45** | new slur, same pitch, Sus MAX re-bow with fitted fill | **2.0** | **1.5** |
  | **50** | merged repeat, notch 39 -> 33 | **3.7** | **1.6** |
  | 51 | new slur, same pitch, re-bow | 6.6 | 2.6 |

  - At 45 the fitted re-bow fill (`rebow_fills.json` "Violins II" "45") lifts the new piece by +0.5..+3.8 dB over 0.08-0.32 s. That fills the very re-articulation the tenuto asks for.
  - The notch at 50 is 6 CC. KIT §6 uses 8 CC at CC11 40 or less, 10 for portato.
- **Fix.**
  - In `rebow_fills.json` "Violins II" "45", set the points from -0.12 to +0.08 to -3.0 dB and from +0.12 to +0.36 to 0 dB; keep the rest of the shape.
  - `MERGE_NOTCH_AT = {"Violins II": {50.0: 10}}` in `build/score_config.py`.
- **Check.** Stem dips 4-6 dB at 45 and 50, master at least 2.5 dB. No change to the levels of the pieces after +0.5 s.
- **Evidence.** Measured.

### 6. Celli "4 soli", bars 83-86: play them on the existing Violoncellos div track (Celli KS Master DIV A), at no memory cost

- **Where.** Violoncellos, qn 274-286, "4 soli, change bow at will". The A flat 2 pedal is now played by the full section -3 dB (`SOLI_AS_META`) and re-bowed six times (275.494-284.151).
- **What is wrong (read; sound inferred).**
  - A full-section sample at -3 dB sounds like a soft full section, not four players.
  - The "Violoncellos div" track already loads `Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib` (half section, Close only; manual p.89-90, A1 group). It plays only qn 51-54 and 62-66, so the window is free.
  - Unlike the basses (finding 2), this needs no new instance.
- **Fix.**
  - Route Vc 274-286 to "Violoncellos div" with `TRACK_WINDOWS` (`"Violoncellos div": (274.0, 286.0, True)`, `"Violoncellos": (274.0, 286.0, False)`). `TRACK_SPLITS`' pitch threshold (55) cannot take the A flat 2. If `TRACK_WINDOWS` holds one window per track, extend it to a list in `score_to_parts.py`.
  - Skip the META cut in that window: the patch is already a half section.
  - The div track gains the Sus MAX row (re-bows), so it is fully rebuilt.
  - Gain: c13 measured DIV A celli 10-12 dB under target at section gain -2, so start at the div track's existing +4 and set the level by stem fix to the c31 celli level over 274-286 (-55 dB).
  - `rebow_fills.json` Violoncellos 275.494-284.151 must be moved to the new track and refitted.
- **Check.** Level over 274-286 within 1 dB of c31. Re-bow dips at most 4 dB. Per-piece spread as in finding 2's table (no alternation).
- **Evidence.** Patch and track read; gain in realism inferred.

## Smaller observations (measured unless marked)

- **Legato data.** No chord on any Leg row (32 tracks), no same-pitch overlap, every keyswitch ahead of its note, no slurred join over an octave. Legato join dips (80 ms windows, targets of 0.6 s or more): median 0.7-3.0 dB per track. The remaining 6 dB joins are all 4 dB or more under the master (Violins I 67.5/251.5, Violins II 86.5, celli 240, Flute 1 111, cor anglais 132).
- **Tenutos, bars 61-62 (molto sostenuto).** Master dips at 206/208/210: 1.7/1.3/2.0 dB. Strings 1-6 dB on the stems, re-bow at 205.949 2.3 dB, so connected with a light re-articulation, as printed. Flute 2's Sus MAX tenutos dip 8-14 dB on its stem, under the tutti. Bass trombone and tuba 13-14 dB at 208 are their printed breath. Trombone 2 and bass trombone take only 5.5/4.2 dB at the 204 breath (others 11-21); the 204 caesura covers it on the master.
- **Tremolos 61-64.** The bar 63 CC7 fall and the trem entries pass the probe (Violas 204 4.0, Violins I/II/celli 212 5.1/2.7/5.0 dB). Not re-bowed, as intended.
- **Pizzicato 37-44.** Basses on time (peak +0.03..+0.21 s; the later ones are low-pitch bloom). Violas' triplets vary ±3.4 dB (p10-p90 around a 7-note running median), round robin rather than pitch. Not worth changing.
- **Mutes.** CC15 changes all fall in rests and before the printed con sord.: Violas 273.5 (first muted note 278.8), Violas div 268.5, Violins II 273.5 (285.8), Violins I 274.5 (291.7), Horn 3 271.5 (285.9); senza at 90.5 for the bar 37 entries. The bar 17-22 solo track has no mute. Correct.
- **Breaths.** Wind and brass breath dips 7-30 dB, except the two above.
- **Harp.** Arpeggios rolled bottom-up at 40 ms per note (30 ms at the f of 261), across both hands at 33 and 253. Correct. A slower roll (50-60 ms at pp in an Adagio) would be a matter of taste.
- **Timpani.** The roll-to-stroke ties at 203 and 209.5 are deliberate (`TIMP_TIE_STROKES`; 209.5 sits 15 dB under the master). Ties at 8 and 237 merge into the roll.
- **Opening chord re-bows.** Violins I C5 2.4 and 7.35: stem dips 5.5/7.5 dB on 150 ms windows, master 2.0/3.8. Smaller than the bass issue. The 50 ms trace shows the ppp sample's own ±4 dB tremor before any re-bow, so I propose no change.
- **Solo violin, bars 17-22.** The DIV A track remains the best installed option (Solo Violin not installed, MANUAL-GAPS #3). c31's deferred CC1 question stands. Running c31's `oib5.py` on the string KS Masters labels the dynamic groups "cc=1" for the full Violins I KS Master too, which contradicts the CC11 dynamics measured since series 1. That script's controller attribution is not reliable for the string patches. Test CC1 on the solo track by ear-equivalent measurement (vibrato depth, level) rather than reading.

## Do not touch

The c31 horn CC1 map and Horn 1 bodies. The bar 63 CC7 lanes. Trombone 1's slurred legato line and its velocities (only the 212.5 start, the 213/215 trims and the bar 64 shapes change in finding 1). The Violas Detache row with its level in CC7. The final-chord, opening-chord and bar 66 re-bow times (no loop pulse anywhere at 3.95 s). CC15 mute placement. The Violins II div Flautando overlaps. The harp roll order and the bar 83 damp. Keyswitch placement and monophonic Leg rows.

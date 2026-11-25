# Cycle 30, critic A: articulation and phrasing (on the c29 render)

Sources:
- `cycles/c29/render` stems and master (c27 stems for comparison), `cycles/c29/metrics`.
- `build/parts.json` (the data c29 rendered), `build/score_config.py`, `build/rebow_fills.json`, `build/mockup-events.tsv`.
- `v600/sections/aOne.ily` (bars 15-22) and score page 2.
- `tools/score_to_parts.py` (`cc1_fn0`, lines 3283-3330).
- The 1st Violins KS Master DIV A patch file, read with `opus_state.load_oib`.
- May 2021 HO manual PDF pp. 75-81 (row A3 of `loop/MANUAL-READING.md`, cycle 30); `loop/MANUAL-GAPS.md`; `mockup-kit/LEARNINGS.md` sections 3 and 5-9.

Times are score qn unless marked s. Levels are stem or master RMS: 30 ms windows for joins and attacks, 0.12 s for re-bows, 0.25 qn for phrase traces.

## Manual notes (A3, PDF pp. 75-81: Hollywood Solo Violin, licensed, not installed)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Solo Violin links dynamics and vibrato depth on CC1; the orchestral strings keep them separate (p.75) | Violin I solo, qn 48-65 ("solo, senza sord., dolce"), on `1st Violins KS Master DIV A` | Partly. The DIV A track carries vibrato on CC1 and dynamics on CC11. Its CC1 sits where two vibrato layers overlap (finding 1). |
| Solo mic set: Close, Mid, Main, plus vintage Close and Mid instead of surround (p.75) | The solo track | The DIV A patch has only a Close mic. The hall send is 0.8 (c29). A Solo Violin track would take Close + Mid. |
| Long Solo patches: a legato script that blends overlapping notes and removes strong attacks. It is not true legato (p.75-77) | none | Not applicable. True legato is the better choice for a slurred dolce line (next row). |
| Legato (true legato, transitions recorded at several dynamics). Velocity sets transition timing. Joins up to an octave. Leg Slur crossfades into a sustain vibrato layer, with CC1 dynamics (up to 3 levels). Leg Exp Vib is "best suited for slower tempos". Leg Lyr Vib is "reminiscent of singing", for slow to moderate tempos (p.79-80) | The two slurs of the solo, 48-54 and 60-65, Adagio q=52 | The DIV A Leg Slur MAX joins measure well: pitch crossovers at -0.07..+0.08 s, join dips 0.5-5.1 dB (measured). Legato targets are at v124 (fast transitions). See finding 1 for the Solo Violin patch choice. |
| LegSus: legato and sustain in one sample layer, "less cross-fading to preserve the feeling of a live performance". CC1 picks one of 2 dynamic layers at the note start and does not crossfade; CC1 and CC11 change loudness mid-note (p.81) | The same solo | Not available. With Solo Violin installed, LegSus is the closest match to the printed slurred dolce phrases with a hairpin inside each note. |
| Short patches (marcato, martelé, pizz., sforzando, spiccato) (p.78-79) | The solo has no short notes | Not applicable. |
| Sustain variants (Sus Vib, Lyrical Vib, Sus Exp molto vib, NV/VB combinations; CC1 picks 2-3 dynamic layers) (p.76-78) | The two long E flat 5s (qn 51 and 63) | The DIV A long notes have almost no audible vibrato (finding 1). |
| MANUAL-GAPS #3 (install Solo Violin, render it in a second pass) | as above | Still open; Dan has to install it. Finding 1 lists the settings a Solo Violin track would need, and what the DIV A track can change now. |

## Findings, ranked by what a listener would hear

### 1. The bars 17-22 violin solo has no audible vibrato on its held notes: it sounds like a muted small section, not one player

- **Where.** Violin I solo, qn 47.83-65 (bars 17-18 and 21-22). The longest and most exposed notes are the slur ends: E flat 5 at 51-53 and 63-65.
- **What is wrong (measured).** I tracked pitch in 46 ms autocorrelation frames and band-passed the cents trace to 4.5-7.5 Hz. The solo's coherent pitch vibrato:

  | qn | note | vibrato, peak to peak |
  |---|---|---|
  | 49 | G5 | 6.5 c |
  | 50 | F5 | 4.4 c |
  | 51.2-52.9 | E flat 5 | 3.2 c |
  | 53 | D flat 5 | 8.0 c |
  | 61 | E flat 5 | 9.7 c |
  | 63.2-64.9 | E flat 5 | 2.6 c |

  - The detrended trace has 5.7-7.4 c p95-p5 over the long notes, with no peak in the vibrato band (zero-crossing rate about 10 Hz, which is noise).
  - A solo violinist playing dolce uses a vibrato of roughly 30-60 c peak to peak at 5-6.5 Hz (inferred: the usual performance range, not measured here). The half section's players average each other out, so the solo comes out as a smooth chorus.
  - The two long E flats are where a soloist's vibrato is most audible, and they are the flattest notes in the phrase.
- **Why (read).** The DIV A patch's CC1 tables (`Amount Controller 1->Volume` on the second MidiController, cc 1):
  - Non Vib: 1.0 at CC1 0, 0.39 at 40, 0 by 64.
  - Sus Vib: 0.86 at 40, 1.0 at 64-85, 0.67 at 95, 0 at 105.
  - Molto Vib: 0 up to 64, 0.6 at 85, 0.85 at 95, 1.0 from 105.

  `cc1_fn0` gives the solo CC1 95 (string boost target), 105 on slur tops (48.5, 60.5), and a "long legato note" dip of 20 (75 rising to 95 over the first 40%) on 51 and 63. So:
  - Most of the solo sits at CC1 95, where Sus Vib (0.67) and Molto Vib (0.85) sound together. Kit LEARNINGS §3 found that two vibrato layers summed this way beat and blur the vibrato (flute, c17).
  - The two long E flats start at 75, where Sus Vib is mostly alone, and climb back into the overlap. That matches the measured minimum.

- **Fix now, without Solo Violin (`tools/score_to_parts.py` `cc1_fn0`, `build/score_config.py`).** Add a generic per-track CC1 target for vibrato families: `VIB_TGT = {"Violin I solo": 112}` (default: none, keeps 95), used in place of `tgt = 95`. Slur tops add +10, capped at 120.
  - Also add `VIB_DIP_FLOOR = {"Violin I solo": 106}`: the delayed-vibrato and long-note dips never take CC1 below it. The track then stays on the Molto Vib layer alone (1.0 from 105).
  - CC1 changes the Molto Vib set's level (it is recorded louder, BRIEF "Facts"). Measure the solo's level after the render and correct it with its role (`roles.json` "Violin I solo" [48,65,2]), not with CC11.
  - Check after the render: vibrato-band pitch modulation of at least 12-15 c peak to peak on 49, 51, 61 and 63, a single peak at 5-7 Hz, and the solo's phrase level within ±1 dB of c29 relative to Oboe 1.
  - If that is still under 10 c, the remaining option is a coherent pitch vibrato from MIDI pitch bend on this track only: about ±10 c at 5.5 Hz, entering over 0.3 s on notes of 0.8 s or more. That needs a pitch-bend lane in `build_reaper.py` (not supported now). Untested, and I have not measured what the patch's pitch-bend range of 0.318 means.
- **With Solo Violin installed (MANUAL-GAPS #3; inferred from pp.75-81).**
  - Patch: Legato `LegSus` (p.81). The alternative is `Leg Exp Vib` (p.80, "best suited for slower tempos").
  - CC1 from the printed dynamic (p about 50, rising to about 62 at the hidden mp tops 49.5 and 62; LegSus picks its layer from CC1 at each note start) and CC11 fixed at about 100 for balance. Do not put CC11 hairpin curves on it, because CC1 already carries the dynamic.
  - Legato target velocity 60-80 (p.79-80: slower transitions for a dolce Adagio line). Re-measure the leads; DIV A needed 0.12 s.
  - Mics Close + Mid (p.75).
  - Render in a second REAPER session with the same tempo map, pre-roll, hall IR and send (memory plan in MANUAL-GAPS).

### 2. The solo's first phrase ends louder than it fades: the slur's last note, D flat 5 at 53, comes in 5 dB over the end of the diminuendo

- **Where.** Violin I solo, qn 51-54: `es''2 (hidden mp) > des''4)\!`. The hairpin ends on the D flat, the close of the dolce two-bar answer to the oboe.
- **What is wrong (measured, 0.25 qn windows).**

  | qn | level |
  |---|---|
  | 51.25 | -38.6 dB |
  | 52.25 | -44.0 dB |
  | 52.75 | -47.4 dB |
  | 53.00 | -43.7 dB |
  | 53.25 | -42.1 dB |
  | 53.5-53.75 | -44.3 dB |

  - The diminuendo falls 9 dB across the E flat and then rises 4-5 dB on the D flat. The listener hears the phrase's last note pushed, a small accent on the resolution, which the score does not print.
  - Cause: the E flat's fall comes from both CC11 (73 to 54) and vol_db (+8.6 to +2.1). The D flat, a Leg Slur target at CC11 54 and vol_db +0.5..+2.0 after the `JOIN_NOTCH` (52.99-53.15, -4 dB), plays a louder sustain than the E flat's tail.
  - The second phrase (63-65) fades evenly (-40.5 to -51.3 dB), so it does not need a change.
- **Fix (`build/note_trims.json`, "Violin I solo").** `"53.0": -4.5` with the default 0.6 s ramp-in, so the trim does not deepen the transition sag (kit LEARNINGS 6, c09). Keep the join notch.
- **Check after the render.** D flat body at 53.25-53.75 within -1..+1 dB of the E flat's level at 52.5-52.9, and the join dip still at most 3 dB.

### 3. Bar 63 (qn 212), strings sf with trem. and >: the fall after the sf is in the post-hall volume envelope, so the climax's ring is cut just as Trombone 1's quotation enters (S3)

- **Where.** Violins I, Violins II, violas and celli, qn 212.0-213.0, all printed `sf` + trem. + decrescendo. Trombone 1 enters ff marcato at 212.5.
- **What happens (measured).**
  - vol_db on Violins II falls +4.9 dB (211.999) -> +0.4 (212.000) -> -6.2 (212.25) -> -11.9 (212.75) -> -13.0 (213). On Violins I it falls -0.6 -> -9.0 over the same span, and on the violas +3.6 -> -6.5.
  - CC11 moves only 122 -> 100 over the same beat (the sf spike and the start of the hairpin).
  - The Violins II stem falls from -21 to -31 dB in about 0.35 s, and the master from -15 to -23 dB in about 0.4 s. The trombone's first note is still rising then (-45 to -28 dB over 212.5-212.75).
  - Inferred: per S3 (Movement I c36, and this series' c29 Violas CC7 fix), a fall of 10-13 dB in 0.8 qn in the volume envelope removes the hall tail of the ff sf with the dry signal. The trombone then enters into a room that has stopped ringing, not under the decaying climax. I did not separate hall from dry signal, so the audible size of the effect is inferred.
- **Fix.** Move the post-sf part of the fall into CC7, as c29 did for the violas (`CC7_POINTS`, linear: CC7 = 127·10^(dB/20)). For each of the four string tracks, take the vol_db difference between 212.06 and 213.0 relative to the value at 212.06, write it as CC7 points (about every 0.06 qn), and flatten vol_db over that span to its 212.06 value.
  - Example for Violins II: CC7 127 at 212.06, 70 at 212.25, 43 at 212.5, 37 at 212.75, 32 at 213.0, back to 127 by a slow ramp ending under the next role step. The level the trombone needs (roles [212.6,213.6,-2] and the hairpin) is unchanged.
  - Keep the vol_db step at the sf onset itself (212.000) as it is.
- **Check after the render.** Stem and master level traces over 212-213 within ±1.5 dB of c29 at 213.0. The master's 2.5-5 s decay character after the strings' later cut-offs unchanged. The probe's Violins II 212 dip (6.5 dB, known) not worse.

### 4. Harp harmonics, bar 83 (qn 274-277): c29's velocity cut on the passing C5 did not lower it, so the arrival is still the softest note

- **Where.** Harp harmonics, `aes4.( c'8 es'4)`, p dolce.
- **What is wrong (measured, 30 ms peaks).**

  | qn | note | velocity | c28 peak | c29 peak |
  |---|---|---|---|---|
  | 274.0 | A flat 4 | v58 | -51.7 dB | -47.4 dB (the +4 role) |
  | 275.5 | C5 (passing eighth) | v58 -> v48 | -46.2 dB | -43.9 dB |
  | 276.0 | E flat 5 (arrival) | v64 | -55.2 dB (at v58) | -48.9 dB |

  - With the +4 role the C5 would have been at -42.2 dB at v58, so ten velocity steps bought only 1.7 dB. The 0.55 dB per step of kit LEARNINGS 9 holds around v58-76, not under v50.
  - The short passing note still stands 3.5-5 dB over the other two notes of a three-note dolce slur.
  - c29's damp works: the plucked harp is -66.5 dB at 274.05-274.3, 16 dB under the harmonic.
- **Fix.** Put velocity 275.5 back to 58 and lower the note in level: `LEVEL_SHAPES_S["Harp harmonics"] = [(275.5, [(-0.02, 0.0), (0.0, -5.0), (0.9, -5.0), (1.0, 0.0)])]`, starting at the onset because the note is plucked. Optionally take the arrival 276.0 to v66.
- **Check after the render.** Three peaks within 2 dB, the arrival not under the first note.

### 5. Breath at qn 268, bar 81: Oboe 1 and Clarinet 1 still do not breathe with the other winds (third time reported)

- **Where.** The printed breath before 268 (all winds, the decrescendo out of the ff of bars 79-80).
- **What is wrong (measured).**
  - Oboe 1's gap is 0.024 qn (dip 9.6 dB) and Clarinet 1's 0.020 qn (dip 5.1 dB). Flute 1 and the cor anglais leave 0.12 qn (23 dB) and the bass clarinet 0.12 qn (11 dB).
  - The legato lead of the 268 note (0.096 qn on Oboe 1, 0.10 on Clarinet 1) uses up the breath.
  - The strings play through, so the master dips by at most 2-3 dB (measured). This is a phrasing detail inside the wind choir, which a listener hears as the two tune-carrying reeds slurring over the breath the others take.
- **Fix (`build/score_config.py`).** Skip the legato/entry lead at 268.0 on Oboe 1 and Clarinet 1, for example with a per-onset 0 in `leg_leads.json` / `entry_leads.json` (keys "268.0"), or `BREATH_GAP_AT = {"Oboe 1": {268.0: 0.12}, "Clarinet 1": {268.0: 0.12}}` if the gap rule runs after the lead. Diff the note ends in parts.json before rendering.
- **Check after the render.** Both gaps at least 0.1 qn, dips of 8-15 dB, matching Flute 1 within 0.03 qn.

### 6. Re-bow fills on the coda 4 soli / ppp pedals jitter 4-9 dB within 0.1-0.2 s, and the opening Violins I C5 still dips 7 dB at two re-bows

- **Where and what (measured).**
  - **Double basses 276.05-286 (bar 84, ppp tonic pedal under the harp harmonics).** The fitted shapes in `rebow_fills.json` swing inside a fraction of a second:
    - 276.05: +3.9 dB at -0.12 s, then -1 by +0.04 s, then +3.8 at +0.6 s.
    - 278.351: -5.0 to +5.1 dB between +0.32 and +0.56 s.
    - 283.605: +3.2 to +9.1 dB over +0.04..+0.24 s.

    On the stem this reads as a -47 dB bulge at 275.5-275.8 before the 276.05 re-bow, against -52..-53 dB on both sides (the RMS of the whole pieces is level, -52.0 / -53.0). Per piece, the re-bow dips are 5.7-6.1 dB on the stem and up to 4.3-5.3 dB on the master at 276.05 and 278.351. A four-player ppp pedal does not lurch like that. This is the "smooth the 4 soli shapes" item of c29's report, which was left.
  - **Violins I, opening C5 (bars 1-3, ppp, the link from movement I).** The re-bows at 2.4 and 7.35 dip 7.0 and 7.1 dB on the stem (2.3 and 3.3 dB on the master) at +0.24..+0.28 s. The c29 wobble measure was still 6.1 dB.
  - The final chord and the other pedals are clean: band-level and centroid autocorrelation at 3.95 s is between -0.27 and +0.20 on every string stem and between -0.04 and +0.05 on the master, over 0-9, 220-238, 274-286 and 286-304. There is no loop pulse.
- **Fix.**
  - Refit the coda basses and the opening Violins I re-bows with `tools/fit_rebows.py 29 build/parts.json --tracks "Double basses,Violins I" --hold-max-after 301:0`, with `FILL_SMOOTH_S` 0.10 -> 0.25 for this run. Keep `--skip "Double basses:273.229"` and c29's per-key offsets (re-apply them as constant offsets after the refit).
  - The longer smoothing removes the sub-0.2 s swings that the fit takes from round-robin noise, and keeps the 1.5 s level matching.
  - Then simulate with `stem_fix.py` before rendering: the median 1 s range on Cb 273-286 should be under 5 dB (c29: 6.5), and Violins I 2.4/7.35 should dip at most 4 dB on the stem.

## Smaller observations (not ranked)

- **Violas' portato eighths, bars 48-51 (measured; c29's leads worked).** All 15 eighths reach body - 3 dB by +0.12 s, at -0.03..+0.12 s (c28: 6 of 15); one of the +0.12 s notes falls just over the line on rounding, so the scripted count is 14 of 15. The rests between eighths drop 26-38 dB. Sotto voce detached strokes, as printed.
- **Violins II slurred tenuto pairs (portato), bars 15-21 (S1, measured).** The notch re-articulations dip 7.6 dB at 44 and 4.3 dB at 50. The re-bows at 45 and 51 dip 2.7 and 4.3 dB with steps of -1..-2 dB. c29's refit fixed the c28 bulges.
- **Violas' pizz. bars 41-44 (measured).** pp beats peak at -47..-55 dB against p beats at -38..-45 dB. The low D flat 3/F3 notes are at -53..-55, still about 7 dB under the A flat 3s. That is acceptable for pp < p.
- **Trombone 1, bars 63-64 (BRIEF item 9, measured).** 2-5 kHz energy over the first 80 ms is 4.4-12.4 dB under each note's body on all nine notes. The accent at 213 is +3.4 dB in level over the 0.3 s before it, and the accent at 218 +2.0 dB. Weight, no bite.
- **Legato rows (measured on parts.json).** No chord, no simultaneous onset and no overlap over 0.15 qn on any Leg row (0 cases).
- **Mutes (read).** Every CC15 change falls in a rest: Vln I 274.5 (next note 292), Vln II and violas 273.5 (next notes 286 and 279), Violas div 268.5. The solo plays senza sord. (CC15 0) and the celli div con sord.
- **Violins II div., sul tasto, bars 37-40.** Both Violins II tracks play Flautando from 90.5/108 (CC1 20). No change needed.
- **Bar 61-62 tenutos, tremolos 204-218, pizz. 37-44, timpani 172 and the harp roll spacing:** see c29 (A). The probe's Violins II 212 tremolo dip (6.5 dB) is unchanged.
- **Better patches considered.**
  - Solo Violin for bars 17-22: finding 1.
  - Basses/Celli DIV A for the 4 soli passages (MANUAL-GAPS #8): still the better sound for four players against a section at -3 dB, memory permitting (second pass).
  - Horn portato rows for the bar 61-62 tenutos: not needed (master dips at most 2.2 dB, c29).
  - Leg Port MAX on one solo interval (G5 -> E flat 5 at 61): possible after finding 1, untested.

## Do not touch

- The Violas Detache row with c29's entry leads (bars 48-51).
- The Violins II portato notches and the refitted 45/51 re-bows.
- Trombone 1's legato line, its shapes, and the 218 Sus MAX accent.
- The CC15 mute placement.
- The final-chord, opening-chord and bar 66 re-bow times (no loop pulse anywhere).
- The harp damp at bar 83 (HARP_RING_S 2, release 200 ms, "R.H." staff).
- The Violin I solo's legato leads and entry (crossovers -0.07..+0.08 s; entries at body - 3 dB by +0.09..+0.11 s).
- Keyswitch placement and no chords on legato rows.

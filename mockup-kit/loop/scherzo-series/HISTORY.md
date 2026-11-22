# Movement III (Scherzo) mockup loop: history

One entry per cycle: Accepted, Rejected/Open, Do-not-touch. Work folder `symphony/scherzo/reaper-v600/` (score `symphony/scherzo/v600`, 376 bars of 3/4). Cycle c00 is the port of the Movement I / Movement II pipeline and its baseline render; cycles c01-c20 (at least 20) are Dan's improvement loops (2026-11-07), three critic subagents per cycle (`loop/LENSES.md`) and one actor.

### Cycle 00 (port and baseline render, no critics)

Port (offline, 2026-11-07; `cycles/c00/PORT.md`): Movement II's tools three-way merged with Movement I's later tools, using Movement I's `cycles/c37/before/` as the fork point. Owner "scherzo", mp3 `scherzo-mockup-cNN.mp3`. New generic options: "sfp", `HARM_ALL_PITCHES` and text-spanner events. `SUL_DEFAULT_CC70` 127. Movement II's delivery ratio 2.2/6 is commented out (Movement I's 3.0/5 kept). `mockup.ly` reads part-only marks (`\removeWithTag #'score`), drops the 62 hidden dynamics (hairpin stops), the closing-page midiExpression fades and the roll strokes, and reads the `\mt` tempo steps and the harmonics' octave transposition. 31 tracks: Movement I's minus percussion and Trumpet 3, plus Harp harmonics, Violin I solo (DIV A, 349-356) and Violas div (DIV B, 209-224, 349-356). RAMP_SPANS cover 149-152, 237-252 (one curve) and 370-375. SUL_SPANS hold the six "sul A" spans. The generic-rule settings are Movement I's plus Movement II's horn CC1 map. Per-note tables are empty. mix.json is Movement I's with Movement II's later fixes. parts.json has no WARNING; all ranges and every mark were checked.
Baseline render (2026-11-07, `cycles/c00/CHANGES.md`): full 31-track build in 68 s; lock held 07:10:41-07:36:10 after a 24 min wait for the finale thread; settled 45 GB with 21 compressed, so the render ran with `--force-memory`. Master -19.7 LUFS, LRA 20.8, true peak +2.7 dBFS (float stem sum, peak 1.367, at the fff summit bars 336-338). mp3 -20.0 LUFS, LRA 13.9, TP -1.6, limiter 4.9 dB, span 20.5. The summit is the loudest (bar 337 -9.5 dB). Probe: 17 of 20 attacks ok; Violins I 756 was a probe artefact (reference moved to 90); string legato spread Violins I 80 / Violins II 96 ms over the 75 ms limit. 46 GB after the render. No stem fix.
Accepted: none (baseline).
Rejected/Open: summit overshoot and limiter 4.9 dB, LRA 13.9 (lower the fff strings and woodwinds at 333-339); S2 legato spread on the violins; seconds-based leads set for quarter 126 (111 Violins I notes led more than 0.1 s); Violas 585 same-pitch legato hole; Violoncellos 816; MANUAL-GAPS #1 wind staccato rows, #6 timpani hard sticks, #9 basses div., #14 Violins I harmonic; Movement I's mix gains not yet checked on this score.
Do-not-touch: `mockup.ly`'s part-tag choice and hidden-dynamics handling (re-read the score's marks before changing them); CC70 lanes resting and ending at 127; the RAMP_SPANS decision (bar-2 fermata, G.P. and last bar as steps).

### Cycle 01

Accepted: Dan's S4 (coordinator): shared hall return `reverb.fx_volume` 0.19 -> 0.095 and new hall low cut `low_cut_hz` 160 (build_reaper.py block from mockup-kit/pipeline); full rebuild of all 31 tracks; tutti cut-off drop at 0.3 s 10.3-11.7 -> 13.9-16.2 dB (G.P. 15.5 -> 15.9), late decay T60 unchanged 3.5-3.7 s. A #1 DOWNBOW_STROKE_AT on the theme-head accents and the summit (+1008/1010/1012): **no gain** (Violins I p accents still -14 dB under the staccato before; strokes at v52). A #2 rebow fills (Violins I dips -7.5..-10.4 -> -1.1..-2.3 dB; celli 612.591 skipped, hold capped +3 after 1120). A #3 tutti staccatissimo rows (StacSs folders read per row): master pair dips 105-120 / 305-320 a little deeper, still some under 3.5 dB. A #4 / C #5 wind "Stac DblTng RRx9" on 8 woodwind tracks for every printed staccato (stem pair dips +0.8..+2.3 dB; level Oboe 1 +4.9, cor anglais -4.5 dB vs c00). A #5 basses pizz. pitch trims (lower note only: trims of simultaneous notes add). A #6 port. 640 on Leg Port MAX (unmeasured). B #1 horn pitch / soft trims and roles (+ Horn 4 -2 in the trio): Cl1 over the drone +0.8..+8.7 dB. B #2 + C #1 solo +7 / flute -6 / celli -2 (solo over flute +1.4..+5.8). B #3 summit and 104/304 wind roles. B #4 bassoon / CA f-ff trims. B #5 timpani [300, 300.5, -12]. C #2 loud_eq. C #3 Violas div gain 2 / width 0.45 (-2.9..+2.4 dB vs section). C #4 side shelves -4. C #6 widths. HP_TARGET_AT Hn1 618 (an old WARNING). Stem fix: summit Violoncellos -6, Violas -3, Violins II -2 (master peak 1.49 -> 1.03, limiter 5.9 -> 3.1). Delivered -19.9 LUFS, LRA 13.6, TP -1.6, limiter 3.1, span 19.0; probe 20/20 attacks ok, legato spread Violins I 89 / II 93 ms (pre-existing); REAPER 49 GB settled (16 compressed), 50 / 32 after; lock 28.5 min.
Rejected/Open: A #1 needs louder strokes (accent velocity ~90-105) or a marcato row; wind stac velocity per track (Oboe 1 down, CA up; Oboe 1 pairs p10 0 dB); summit only 1.2 dB over bar 304; memory over the 45 GB cap (+4 GB from 13 rows); late decay over 2 s (shorter IR via Opus IR envelope, manual p.133-134, Movement I testing); string unslurred same-pitch repeats as Sus MAX re-attacks after min(0.06 s, 25%) instead of CC notches (Movement I testing; scherzo notches: Violins II 7, violas 53, celli 37, Violas div 15); critics: 200-500 Hz build-up in the master vs references, cut there rather than boost treble; A #6 Violins II harmonic, trumpet stac rows deferred; legato spread on the violins.
Do-not-touch: fx_volume 0.095 and low cut 160 (Dan S4; no sends raised); the re-bow fills as fitted; the solo/flute/celli roles at 349-356; the Violas div gain/width; the trio horn roles and pitch trims; plus c00's items.

### Cycle 02

Accepted: ONE_TIME memory (new generic `ROW_REMAP`: brass, Oboe 2 and bass clarinet legato rows to Sus, Oboe 2 / Bassoon 1 / Clarinet 1 wind stac off, Violas / Violins II / Violas div Leg BC to Leg Slur + notch; loaded regions 701k -> 577k; settled 49 -> 45 GB, 25 compressed). A #1 Violins I p/mp theme heads on Sus Marc LITE plus a per-head level step (stem fix): accent minus staccato -14..-8.5 -> +2.0..+2.6 dB. A #2 hemiola strokes (master weight at 302-308 +2.0..+3.2 dB; celli merge gone). A #6 portato notch 18. B #1 harp pp trim 2 + C #5 `VEL_CAP_SPANS` (harp 1-5 dB under the trio clarinet). C #1 horn soft trims to Movement II's soft-map values, c01 horn roles removed, solo roles (Hn1 end level with Violins I). C #2 + B #2 summit (arrival weight, strokes v112, roles from 996: 1005 now +1.0 dB over 1004, bar 337 2.1 dB over 304). B #3 timpani loud attack once per onset. C #3 sfp chain fix (master p at 901-903 -3.6 dB). C #4 `TIMP_ROLL_TRIM_HOLD_CRESC` 0.6 (bar-101 roll grows 5.4 dB), codetta roll +4. B #5 counterstatement chord roles, B #6 celli pizz. trims. Delivered -19.9 LUFS, LRA 15.0, TP -1.6, limiter 3.2, span 20.2; probe attacks ok (legato spread V1 88 / V2 90 ms, pre-existing); lock 27.4 min.
Rejected/Open: Legato Slur Staccato / Slur Runs rows (memory); A #3 wind stac velocity tables had no effect (use level); A #4 Violins II Spiccato did not separate the tutti pairs (try Stac RRx9 -3 dB or shorter notes); Marc LITE heads' 2-5 kHz front +2..+7 dB over the body (check by ear); counterstatement master pair dips 1.3/2.5 dB; Horn 3 under the trio celli 5-8 dB; span 20.2 dB; memory at the cap (Leg Port MAX 1 note = 22k regions is the next candidate); legato spread; shorter hall still pending from Movement I.
Do-not-touch: ROW_REMAP choices (each moved row plays few notes; re-check memory before loading any row back); the Marc LITE heads with their level steps as a pair; the horn soft trims (Movement II's soft-map values); the sfp chain fix; plus c01's items (hall 0.095 / 160 Hz, re-bow fills, solo roles 349-356, Violas div gain/width, port. 640).

### Cycle 03

Resumed after the first attempt stalled 18 h on the lock (edits kept, clarinet ROW_REMAP replaced). ONE_TIME (Movement I c44): `reverb.ir_setup` envelopeMode 2 / endPos 0.5 / decayLength 0.5 (build_reaper irSetup block); release caps, strings 150 ms mf-ff + 350 ms pp/p (kit c46 list form, not ONE_TIME's 150 at all dynamics), horns 237 ms; `STR_REP_NEW_BOW` ported with Movement I's c45 lead fix and `REBOW_FILL_END_S`. Full rebuild of 31 tracks. Late decay at the G.P. without the timpani T60 1.76 -> 1.12 s (master 3.43 -> 3.27, the drum still rings); master RT(-5..-25) 2.46 -> 1.31 s. String repeat stem dips: strokes 0.9 -> 6.7, sus gaps 2.9 -> 7.5, portato -0.5 -> 1.5, soft 3.7 -> 4.2 dB; no phrase end over 10 dB in 0.05 s.
Accepted: A #1 Marc heads in the mp band (+2.4..+3.7 dB, front no longer bright; 51 / 771 -3 by stem fix); A #2 clarinets on "Leg Slur Rep" by whole-piece REP_ROW (dips 0.0 -> 3.6 dB); A #3 `WIND_REP_PORTATO_TENUTO`; A #4a clarinet pitch trims; A #5 `ROW_TRIM_WINDS`, Oboe 1 stac -5; B #1 celli roles (193-200 +9.5 -> +0.2 dB over the upper line), B #3-#6; B #2 / C #4 `TIMP_STAC_ROW` Sht; C #1 `SHORT_SUS_TO_LONG_ANY`; C #2 `ABUT_LEAD` 0.08; C #3 leg / entry leads; C #5 `PIZZ_LEAD_S`, `STAC_LEAD_SPIC`; C #6 `ENTRY_LEAD_LOUD_ART_S` (few notes moved). Stem fix: re-bow refit, two head trims. Delivered -19.9 LUFS, LRA 14.6, TP -1.6, limiter 2.5, span 19.5; master -20.0, LRA 23.4, TP -0.9; probe attacks ok, legato spread V1 75 ms (flagged at the limit), V2 80 ok; REAPER 45 GB settled (14 compressed), 45 / 29 after; lock 28.8 min.
Rejected/Open: the G.P. still filled by the timpani's Lng strokes of bars 337-338 (tail hold undoes a volume cut: needs a pre-hall CC7 fall); celli 209-224 now 6 dB under Violins I (role -3 -> about -1); summit 1005 0.9 dB under 1004, bar 337 only 1.0 over 304; string portato repeats 1.5 dB; celli 1074 re-bow dip 8 dB; A #3b LegRep rows, A #4b join fills; C #1-#3/#5 not measured with pcx; Trio ramp end 226.17 vs 228.
Do-not-touch: ir_setup and the release caps (shared values; 350 ms at pp/p); STR_REP_NEW_BOW settings; the clarinets' whole-piece REP_ROW (not ROW_REMAP); plus c02's items.

### Cycle 04

Accepted:
- B #4 / C #3: a pre-hall timpani damp (new generic `TIMP_DAMP_AT`, CC7 127 -> 1 over 1014.5-1015.25) and Timpani role -4 from 1007.9. Timpani at G.P. +0.3 s: -43.8 -> -71.0 dB; the G.P. is now the strings' hall.
- B #2 / C #5: harp `VEL_CAP_SPANS` 56 / 50 and roles -3 / -2. Harp over 216-240 -7.7 dB; delivered episode now 1.0 dB under theme A.
- C #2: delivery `RIDE_TRIMS` -2 dB at 300-312 and 897-912, -1.5 dB at bar 72. Delivered bar 337 is 3.4-3.9 dB over bars 72 / 104 / 304 (was 1.3-3.0) and 2.3 over bar 300.
- B #1: bassoon gains -5 plus roles, bass clarinet roles, celli 624-672 -1.
- B #3: celli loud_eq +2 (was +6).
- B #5, B #6; C #4 clarinet pitch trims.
- A #3: coda tutti staccatissimo rows (not celli). Violins II / violas coda pair dips 3.1 / 3.5 -> 5.5 / 4.9 dB.
- C #1: alternating Stac RRx14 phrases in theme A.
- A #1 partial: Trumpet 1 on "StacSs DblTng RRx9", plus `STAC_LEAD_S` for brass. Quarters now on the beat, eighths re-attack; pp bars -6 dB by stem fix.
- A #2 fallback: horn re-tongue 0.07 s / 8 CC. Horn 3 4.9-6.4 dB, Horn 4 3.7-3.8, Horn 1 8.4-10.9.
- A #4: auto_fills (Clarinet 2 and Bassoon 1 added; celli fills not kept). A #5: celli re-bow fills 1074 / 1077.
- Delivered -19.8 LUFS, LRA 14.3, TP -1.4, limiter 2.5, span 19.3. Master -20.1, LRA 23.4, TP -1.1.
- Probe: attacks ok; legato spread V1 76 ms (as c03) and violas 116 ms (render-to-render artefact, data unchanged).
- REAPER 45 GB settled (5 compressed), 46 / 28 after. Lock 30.7 min.

Rejected/Open:
- A #2 brass portato rows and Trumpet 2's staccato row (memory cap).
- C #6 staccato lead alignment (needs a pcx pass).
- Horn 1 tenuto repeats still 8-11 dB.
- Master coda pairs 985 / 1003 at 1-2 dB.
- Bassoon 1 at 1032 level with Oboe 1.
- Not yet measured: C #1, C #4, A #4, A #5.
- Disk was under 30 GB during the render (other threads).

Do-not-touch:
- `TIMP_DAMP_AT` at 1014.5 (pre-hall; do not move the damp into vol_db).
- The harp's episode caps and roles; the summit `RIDE_TRIMS`.
- The bassoon gains -5.
- Trumpet 1's StacSs row with its pp -6 dB step.
- Plus c03's items.

### Cycle 05

Accepted:
- C #1 (coordinator): `ir_setup` endPos / decayLength 0.5 -> 0.7 (Movement II c40 value), full rebuild of 31 tracks. G.P. drop after the last note-off at +0.3 / +0.6 / +1.0 s: 21.9 / 36.8 / 50.1 -> 22.2 / 34.8 / 47.5 dB; master late T60 (-12..-40) 1.25 -> 1.47 s.
- B #2 (regression): Violins II -7 / violas +3 / Violins I +2 over the coda build 984-995.5. The Spiccato row is untrimmed there, because ROW_TRIM_DB needs a Leg neighbour.
- A #1: hemiola body cuts, leads and v85 at 904. Master front minus body better at 9 of 11 onsets, still under +1 dB.
- A #2: Violins II GROUP_LEAD 0.05 s; heads -0.003 / followers +0.025 s.
- A #3: Horn 1 re-tongue 0.035 s / 4 CC, lead 0.09 s. Dips 3.1-11.4 dB, 2 of 5 in target.
- A #4: entry leads. Celli 756 and basses 840 on time; celli 504 later (+0.155 s).
- A #5: fit_accents for the string and wind families (29 fits removed by hand).
- A #6: portato 0.08 s / 12-14 CC. Violas dip 1.8 -> 3.6 dB, div 0.7 dB.
- B #1: flute ff staccatos +6, G6 roles. The stem fix took the cuts to -4 / -3 (cut and fitted swell had counted twice); G6 now 1.5-2.4 dB under Violins I.
- B #3-#6: oboe shape and roles; bass clarinet 732-756 -5; sfp Flute 2 -6 and Horns 1-2 -3; celli 132-156 -3.
- C #2: DIV shelves (tilt within 0.4-1.6 dB of the sections), Violas div 648-672 -3, solo +8 (stem fix).
- Numbers:
  - Delivered -19.9 LUFS, LRA 13.9, TP -1.6, limiter 2.9, span 19.2.
  - Master -20.5 LUFS, LRA 23.1, TP -1.2.
  - Probe: attacks ok; Violins I legato spread 77 ms (pre-existing).
  - REAPER 45 GB settled, 45 / 28 compressed after. Lock 25.1 min. 33 GB free at the end.

Rejected/Open:
- C #3 blanket flute cut (B #1 covers it).
- C #4 reverb.width, C #5 hard sticks (deferred).
- G.P. still short of C's +0.6 / +1.0 s targets; a longer envelope is a shared value.
- Horn 1 repeats 630 / 633 / 663: try 1FH Port Lng.
- Celli 504 entry late.
- Violas div portato flat.
- LRA 13.9.
- Horn 1 re-tongues all 0.04 s earlier.

Do-not-touch:
- ir_setup 0.7 / 0.7 with fx 0.095 and 160 Hz.
- The coda-build string roles (until ROW_TRIM covers staccato-only spans).
- The DIV shelves.
- Plus c04's items.

### Cycle 06

Accepted:
- ONE_TIME (Dan, EastWest's template mix), Movement I's c50 tools ported (send-envelope activation fixed): template mic levels (Close at the seat, Main/Mid/Surround full width, template seats for strings and brass, REAPER pans); Opus reverb off and four Spaces II returns from the template's chunks with post-fader sends at its levels; family EQ on every track (gains given back the K-weighted loudness it takes: brass 6-10 dB, winds 2-5, harp 6-7, strings 1-2) and the master EQ in delivery; Duc's celli/basses send offsets (-1.6 longs, -7 shorts) and basses -3 dB at 230 Hz; 20 redundant high-passes and the basses' +4 dB at 180 Hz removed. Full rebuild of 31 tracks plus 4 returns. G.P. drop at +0.3/0.6/1.0 s 22.2/34.8/47.5 -> 13.9/22.4/31.5 dB; returns -3.9 dB under the dry stems (energy); memory 45 GB settled (unchanged).
- Delivery refit 2.2 / 5.5 (3.0 / 5 gave LRA 12.7 on the wetter master).
- A #1 Stac RRx14 spans split (V1 pair dips 1.5-4.0 -> 5.7-7.3 dB stem); A #2 note-trim fallback (partial); A #3 V1 hemiola on Sus Marc LITE (front minus body +0.4..+10.4); A #4 head trims; A #5 Horn 1 Port Lng (mixed: 3 dips to 5.4 dB, 2 deeper); A #6 Cl1 B4 4.5; C #1 sfp strokes and new generic FP_SPIKE_FROM_ONSET (sf now level with bar 300); C #2; C #3 trio ride trims (delivered 218 3.6 / 4.6 LU over 197 / 222); C #4 new generic HP_KEEP_ACROSS_REST; C #5 summit roll held; B #1-#3, C #6 roles (re-checked against the mic change first); B #4 CC16 reset via the ported build_reaper.
- Stem fix: mic-layout residuals in the gains (flutes -3/-3.5, Cl2 -2.5, bassoons -1.5/-2, harp -2, low brass +1..+2), Cl1 -2 at bars 72/300, Bn1 role +1.5, V1 902-912 step -2.
- Delivered -19.8 LUFS, LRA 14.0, TP -1.6, limiter 3.4, span 19.0; master -19.9, LRA 22.0, TP -1.0; probe attacks ok, V1 legato spread 75 ms (pre-existing); REAPER 45 GB settled, 46 / 29 after; lock 31.9 min.

Rejected/Open:
- Deferred to c07 (new ONE_TIME.md): the MIDI rules (plan item 5, sections 6-8), the tutti entry spread, R Glue; room-noise bed skipped (no free recording).
- The hall is wetter than c05 (master pair dips fell at unchanged pairs 43, 763); Duc's hall is the fallback; return faders can be tried on the stems.
- Horn 1 Port Lng at 639 / 651; Violas div pairs 649-655; bar-332 roll; V1 over V2 at 333-335 +0.7 (target +1.7); silent-note flags Horn 1 1005, Violas 579; limiter 3.4 dB.

Do-not-touch:
- The template mix as built by `make_template_mix.py` (mics, returns and sends, family EQ with its gain compensation); change a value only with measured numbers (Dan: every item is a default).
- `FP_SPIKE_FROM_ONSET`, `HP_KEEP_ACROSS_REST`, the V1 hemiola Marc LITE spans with their steps, the split Stac RRx14 spans.
- Plus c05's items, except the old hall settings (fx 0.095, 160 Hz, ir_setup 0.7), which the template returns replace.

### Cycle 07

Accepted:
- Wetness (Dan; A #1 / B #1 / C #1; fitted on the c06 stems with a return-transfer simulator): return faders -6 dB, return high-pass 180 Hz, Spaces II IR envelope (mode 2, endPos / decayLength 0.5), no hall send from bassoons, contrabassoon, low brass and basses, trumpets -6. G.P. +0.3 s drop 12.9 -> 20.9 dB, t20 0.65 -> 0.27 s, RT60 2.46 -> 1.38 s; returns -4.8 -> -13.4 dB of the dry energy.
- Width (Movement I c50): Main mics at the seat ±0.8 and side-only 200 Hz -6 dB shelves on strings, brass, timpani and harp. Correlation <250 Hz 0.17 -> 0.68, 250 Hz-5 kHz 0.32 -> 0.57, side/mid -2.4 -> -5.6 dB.
- C #1.3: string Close mics -4.5 dB under Main.
- ONE_TIME items 1-4: repeat gaps 0.09 / 0.065 s at 30 %; legato overlap floors 60 / 45 ms; legato velocity by dynamic; PHRASE_SHAPE with types (ported from the finale's c07).
- Batch 5: HP_CURVE (timpani linear), register sends, tempo breaths (BEAT_STRETCH, 22 beats).
- Timpani 84 Hz bell halved; harp high-pass 80 Hz.
- Critics: A #2-#5, B #2-#6, C #2.1 / #2.3 / #3 / #4 (new generic RR_RESET_AT) / #5 (trio ramp end 228).
- Delivered -19.8 LUFS, LRA 14.7, TP -1.5, limiter 2.5, span 19.6. Master -20.8, LRA 22.6, TP -2.3. Probe all ok. REAPER 45 GB settled, 45 / 26 GB compressed after. Lock 40.7 min.

Rejected/Open:
- Brightness worse: 6-20 kHz share -27.2 -> -24.8 dB (Movement I c50's shelf fix for c08).
- SHORT_BEAT_VEL written but off (HO string short rows switch layer by velocity, about 10 dB: Movement I c51). Envelope beat weight for c08.
- The 2.3 kHz return low-pass (no gain in simulation).
- Tutti spread in the Allegro (C: already 40-66 ms perceived).
- Deferred: CC11 -> CC1 pass-2 test, separate legato tracks and Trumpet 2 StacSs (memory); pickup longs (C #2.2); the flute lead in 349-356; the solo CC1 lane; C #4.2 group-head trims; the loud brass tone and the soft-roll timpani shelf (Movement I c51).

Do-not-touch:
- The returns as built (fader -6, high-pass 180, IR envelope 0.5 / 0.5, low sends off); change them only with a measured decay.
- Main mics at the seat ±0.8 and the side shelves.
- RR_RESET_AT group resets.
- The string Close mics at -4.5.
- Plus c06's items, except its template return levels.

### Cycle 08

Accepted:
- ONE_TIME_c08: brightness (strings shelf off, brass shelf +1, V1 5 kHz -6, V2 -4, 3 kHz -2 bells on both violins, gains back): 6-20 kHz -24.8 -> -28.9 dB, 2-6 kHz -8.9 -> -9.5. Brass bells halved plus 3.2 kHz -3, gains -2..-4.5 (loudness held). SHORT_CC11_PARK and the 3/4 downbeat weight (+1.5 / 0 / -0.5). Horn release trails -6 dB: final-chord RT60 1.68 -> 1.28 s.
- Critics: A #1-#6, B #1-#4 and #6, C #1-#3 and #6, c07 C #2.4 (solo / flute). Timpani 84 Hz bell off (40-100 Hz share 70 -> 49 %); reprise on Spiccato / Staccatissimo (identical attacks 29 -> 2 of 38); V1 harmonic on V2 Harmonics (stem fix +5.4 dB); V1 Leg Port MAX unloaded.
- Delivered -19.8 LUFS, LRA 14.9, TP -1.6, limiter 2.6, span 19.6. Master -20.7, LRA 23.2, TP -1.6. REAPER 45 GB settled (21 GB compressed, rendered with --force-memory), 46 / 28 GB after. Lock 54.6 min.

Rejected/Open:
- Violas legato probe SPREAD (window 115 ms, limit 90) in 133-162, 390, 582-609, 858 with Violas data identical to c07 there; reproduced on a re-render; cause open.
- 2-6 kHz share 0.5 dB above the -10 target; one soft string end 0.31 s (limit 0.30).
- Deferred: C #5 hard timpani sticks, c07 C #2.2 pickup longs, the solo CC1 lane, research batch 6 #3 / CC11 -> CC1 pass 2 / separate legato tracks.

Do-not-touch:
- The c08 EQ set (no strings family shelf, brass bells halved, violin 5 kHz and 3 kHz cuts) and the timpani 84 Hz bell off; change only with measured band shares.
- Horn rt_gain_db -6, SHORT_CC11_PARK, the reprise row split, BORROW_NOTES for the harmonic.
- Plus c07's items.

### Cycle 09

Accepted:
- Violas legato state (orchestrator; A #3, B #1): cause found. Opus saves the AHDSR attack its legato script last set (20 ms instead of 841-1501 ms on 52 legato sustain groups) into a played instance's state; a `--midi-only` build kept it. A one-track test with only those 52 attacks set to 20 ms reproduced the c08 flip exactly (v112+ joins -83 ms, window 114 ms, stem +1.6 dB). Full rebuild of all 31 tracks: Violas window 91 / rSD 78 ms (ok), v112+ joins -3 ms, stem -36.7 / -39.9 dB. New generic `MIDI_ONLY_REBUILD_LEGATO` (on) and `LEGATO_MONO_CC22` (CC22 127 in the pre-roll).
- A #1 head tails as legato targets (new generic `SHORT_SUS_LEG_AT`, joined from the Marc LITE head): all 18 tails within 8 dB of the half note (were -13..-17 at 69 / 789). A #2 auto_fills incl. 17 celli fills (542 / 576 dips 11 -> 5 dB). A #5 celli join notches (master pair dips 763.5 / 799.5 2.5 / 1.6 -> 4.7 / 4.4). A #6 Horn 1 breath (dip 2.5 -> 7.5 dB).
- B #2 flutes f staccato (+5 / +5 / CA +4; Ob1 - Fl1 6.2 -> 1.2 dB), B #3 violas tutti +4, B #4 Clarinet 2 (588 -9 step), B #5 celli 111 / 114 as step trims, B #6 Flute 2 high-note trims (halved by stem fix: Fl2 - Fl1 -1.6 dB).
- C #1a wind send +3, C #2 trumpets 0 / trombones-tuba -11.77 / bassoons back in the hall, C #3 DIV sends +3.6 / +4, C #4 harp harmonics in R Strings; simulated first (`retsim09.py`) and rendered: G.P. 20.5 / 31.4 / 46.6 dB, RT60 1.34 s, final chord RT60 1.42 s, returns -11.64 dB re dry. Soft end at 1128 0.31 -> 0.14 s (V1 last 0.25 qn -6 dB).
- Delivered -19.8 LUFS, LRA 14.7, TP -1.5, limiter 2.7, span 19.6. Master -20.8, LRA 23.2, TP -1.6. Probe all ok. REAPER 45 GB settled (28 compressed, --force-memory), 46 / 28 after. Lock 38.9 min.

Rejected/Open:
- A #4 soft entries failed: celli 504 +285 -> +367 ms, basses 504 / 1071 +146 -> +166 ms with more lead, a fill and v53: revert in c10.
- A #1: heads 51 / 75 first tail still 10-11 dB under the next quarter. C #1b wind Main mics deferred (inferred).
- The 444.5 handover reads 0.71 s on the soft-end check because the harp harmonics ring in R Strings (strings alone 0.29 s).
- `loop/ONE_TIME.md` for c10: finale SHARED-TECHNIQUES items and Movement I c51 lessons not adopted in c09; MANUAL-GAPS none tried.
- c08 stems not deleted (permission refused in the session).

Do-not-touch:
- Full rebuild of legato tracks before every render (`MIDI_ONLY_REBUILD_LEGATO`); never render a legato instance from a state saved after a render.
- The c09 sends as rendered (simulated and measured within Dan's limits).
- SHORT_SUS_LEG_AT tails, the celli JOIN_NOTCH pair, the Horn 1 breath end.
- Plus c08's items.

### Cycle 10

Accepted:
- Orchestrator: c09 A #4 reverted (celli 504 +367 -> +263 ms, basses +166 -> +144); harp harmonics back in R Perc (soft end at 444.5 0.71 -> 0.29 s; G.P. 20.4 dB at +0.3 s, RT60 1.34 s).
- B #1 coda build: HP_CURVE `cresc_long` (min 10.5 qn) plus horn roles (bar 331 Oboe 2 -27.0 -> -39.2 K, V1 -30.4; master 329-333 rising). C #1 one-beat swells: HP_SHORT_KINDS with cresc plus stem-fix level shapes (Horn 1 +9.3 -> +4.8, Clarinet 1 +9.3 -> +5.2, Horn 3 +8.9 -> +5.0 dB). C #2 (arrivals over accents, +1.6 / +3.3 dB), C #3 (HP_DEC_HOLD_HELD; close +4.6 -> +2.1 dB), C #4 harp hairpins, C #5 timpani roll (+5.2 dB under the crescendo, flat before).
- B #2 pitch trims, B #3 Trio horn / flute roles, B #4 celli 506, B #5 violas pizz.; A #4 celli v80 (MANUAL-GAPS #8: pcX -63 -> -19 ms), A #5 Flute 2 trims (pair dips >= 4.1 dB), A #6 V1 heads (vs quarter -6.0 / -6.5 dB).
- ONE_TIME: brass track_width (ported, pans kept balance), wind phrase-shape x1.4; items 1, 3, 7, 8 rejected with band measurements, 4 / 5 skipped.
- Delivered -19.8 LUFS, LRA 14.8, TP -1.6, limiter 3.3, span 19.6. Master -21.0, LRA 23.1, TP -1.2. Probe all ok. REAPER 45 GB settled (38 compressed, --force-memory), 45 / 32 after. Lock 48.9 min.

Rejected/Open:
- Short of target: A #1 flute note-off step 7.6 -> 5.8 dB (only quarters before rests lengthen), A #2 Flute 1 sfp drop 7.1 dB (no change), A #3 horn repeat dips 1.6-3.6 dB, C #4 harp crests 1-2 dB, Oboe 1 A5 over Flute 1 (+6.5 K), Oboe 2 903 4 dB over Oboe 1.
- Limiter 3.3 dB (master peak 0.828 -> 0.874 at the same summit sample).
- Finale items 13-17 in `loop/ONE_TIME_c11.md`. cycles/c08 stems not deleted.

Do-not-touch:
- `cresc_long` at min 10.5 qn (min 9 changed the 300 / 900 hemiola legato data); HP_SHORT_KINDS with cresc; HP_DEC_HOLD_HELD.
- Harp harmonics in R Perc (the soft-end check reads R Strings).
- Flute STAC_LEN lengthening only before rests (a 0.02 qn margin cut the following notes' leads by 0.09 qn).
- Plus c09's items.

### Cycle 11

Accepted:
- A #1 / C #1 `LEG_CAP_FROM_MOVED` (cap measured from the moved onset; Violins II only after notes of an eighth or shorter) plus 35 fitted negative offsets: joins over +60 ms Violins I 49 -> 19, Violins II 15 -> 8, Violas 16 -> 10, Violoncellos 51 -> 34. A #4 / C #3 Violins I Leg Slur MAX +0.04 s (median +49 -> +15 ms), celli trio tune +0.06 s at v85 or less (+39 -> -8 ms), `LEG_LEAD_CLAMP_TOTAL`.
- A #3 / C #4 hemiola 902 / 904: `ACCENT_CC_AT` (CC11 +22 at the stroke) with re-attack leads; pcX at 902 / 904 Violins II +64 / -132 -> +50 / -45, Violas +31 / -190 -> -32 / -6, Violoncellos +177 / -122 -> -47 / +10; 902 steps -12.9 / -18.1 / -15.2 -> +0.9 / -2.5 / +0.4 dB; basses' stroke at 900 +115 -> -17 ms.
- A #2 Horn 1 E4 +155 -> +53 ms, rise after it 3.9 -> 0.8 dB. A #5 by other means: `NOTE_END_AT` before Horn 1's repeats (holes 12.7 -> 7.3 dB).
- B #1 `family_scale_skip_cc1` (clarinets -3.2 / -3.4 dB at 47-50; reprise beats over the strings 7 -> 2), B #2 basses' G#1 trims (-5.3 / -6.9 / -7.0 / -2.6 dB), B #3 Horn 4 role (-4.0), B #4 brass rows at 994-995.5 (each track 3.8-6.8 dB under its own 996; brass 5.0 dB under strings), B #5 violas' beat 2 (+1.1 -> +3.3) and Oboe 2 (+4.1 -> +0.4 over Oboe 1).
- C #2 entry leads and fills (Flute 1 1044 +324 -> +67, Violins II 738 +159 -> +43, Violas 1020 +261 -> +109), C #5 pizzicato head bars (+1.8..+2.0 dB), C #6 `RAMP_LAST_STEP_HOLD_QN` (rit. holds 140).
- ONE_TIME 13-16: sf bumps where short, Flute 2 lead 0.07, three delivery rows moved off printed hairpins (step at 300 +1.7 -> +2.8 dB), rest-bar text listener (harp damps used).
- State guard from Movement I: 5 stale tracks before the build, 0 after a full build. Horn splice from c10 after unlocking (five horn spans, three brass-return spans, 4.5 s), no second render.
- Delivered -19.8 LUFS, LRA 14.8, TP -1.4, limiter 2.9, span 19.6. Master -21.0, LRA 23.0, TP -1.7. Probe all ok. Hall as c10 (G.P. 20.4 dB at +0.3 s, RT60 1.34 s). REAPER 45 GB settled (26 compressed, --force-memory), 46 / 29 after. Lock 38.5 min.

Rejected/Open:
- Rejected: A #5 as written (the Rep row's re-tongue groups start on round robin only), A #6 (memory), C #4 horn leads (do-not-touch, inside ±50 ms), Sus Marc LITE on three more sections (memory), `--fit-flat` rows (delivered sub. p step 8.8 -> 7.1 dB).
- Short of target: Horn 1 G#3 at 6 (+83 ms), Violins II 672 / 708 (+167 / +138), Oboe 1 672 (+194), Violin I solo 1044 (+139), Violas 1020 (+109), basses 504 / 1071 (+112 / +144), Flute 1 904 (+146), Violins II 900 (-72), basses' 902 step (-11.2 dB against their new stroke at 900), Flute 2 joins (+46 ms), reprise beats 640 / 641, joins under -40 ms (Violoncellos 33, Violins II 20, Violas 17).
- The project saved after the c11 render is stale again on 5 tracks: c12 starts with a full build of all tracks and a guard run. The guard is not enforced in `build_reaper.py` / `render_cycle.py` yet.
- Horn notes re-tongued 7-21 ms after the note before can lose their attack in one render and not the next: compare the horn stems with c11's in every render (`stemdiff11.py`).
- Timpani stick changes (MANUAL-GAPS #6); `loop/ONE_TIME_c12.md` items 1, 4, 9-20 and the rest of 2, 5, 6, 8. cycles/c08 stems not deleted.

Do-not-touch:
- `family_scale_skip_cc1` True (the family scale moved the clarinets' whole dynamic layer).
- `LEG_CAP_FROM_MOVED` as set, Violins II at 0.5 (its quarter runs were on time at the capped lead); `LEG_LEAD_CLAMP_TOTAL`; `fit11.py` is not rerun.
- The 902 strokes: `ACCENT_CC_AT` with the 0.09 / 0.07 / 0.09 leads and the +3 accent fits (a volume swell did not move the time).
- `NOTE_END_AT` before Horn 1's repeats; `RAMP_LAST_STEP_HOLD_QN` 6.0; delivery rows at 300 / 587 / 659.
- Violins II role row ending at 359.2 (ending at 357 lifted a hall tail by 3 dB).
- Full build of every track before each render.
- Plus c10's items.

### Cycle 12

Accepted:
- Score change from Dan (commit 0a79d901): Horn 1's solo link in bar 56 removed in the build copy; beats 2-3 hold only the hall's decay (Horn 1 stem -44.2 -> -63.5 dB). Horn 1's staccato at 165 is 4.0 dB over Horn 2's.
- A #1 `TIMP_RH_ALT["lh_vel_add"]` (first-stroke deficit of the soft statements 9-13 -> 3-8 dB), A #2 harp `VEL_SET` by (qn, pitch) after the caps (same-pitch spread 10.8 -> 4.4 dB at worst), A #3 roll and stroke rows (roll end -39.1 -> -33.7, stroke 1008 -29.8 -> -25.3), A #4 45 join offsets (medians -77..-105 -> -13..-19 ms, none outside +-50).
- B #1 brass gains +2 trumpets, +3 trombones (against Violins I -9.9 / -11.1 / -12.4 / -9.8 / -12.2), B #2 pickup shapes (master -2.2 / -5.0 dB under the downbeat), B #3 C6 -4.5 / -4.0, B #4 Horn 1's last note falls evenly, B #5 Flute 1 -3.5, B #6 Horn 3 +2 and F#3 +3 with `PITCH_TRIM_MIRROR` (joins +3..+15 ms).
- C #1 join notches (celli 506 +11.6 -> +4.6, Clarinet 1 459 +7.1 -> +3.3), C #2 Violins II fill at 432.5 (dip 13.0 -> 4.2), C #3 Oboe 1 552 +5 (5.1 -> 1.6 under the eighths), C #4 entry leads with a front-weighted swell (stem fronts +1.3..+3.4 dB), C #5 Harp 216 +5.
- `LEG_HEAD_MIN_GAP_S` 32 ms wind and brass (Bassoon 2 holes 8.5 / 7.7 -> -1.3 / 1.7 dB); sf bumps at 900; `RR_RESET_AT` 312 / 912; basses' E2 +3 on 11 onsets.
- State guard: 5 stale before the build, 0 after the full build, 7 after the render; those 7 rebuilt without playback and saved: 0 stale. The guard is now enforced in `build_reaper.py` and `render_cycle.py`.
- One render, no splice, no stem fix. Master -20.8 LUFS, LRA 23.4, TP -1.5. Delivered -19.8 LUFS, LRA 14.8, TP -1.5, limiter 2.8. Probe all ok. Hall: G.P. 20.5 dB at +0.3 s, RT60 1.32-1.40 s. Tracks with identical data reproduce c11 at 0.00 dB. REAPER 45 GB settled (42 compressed, --force-memory), 45 / 32 after. Lock 47.8 min.

Rejected/Open:
- Rejected with numbers: `END_LEG_KS` (trailing legato keyswitch: treated tracks stale again; remove its three rows in c13), C #5's cap shift, A #5, C #4's body cuts, ONE_TIME 4 / 21 / 22 on strings (see CHANGES).
- Short of target: timpani first strokes at 291, 294, 744 (-6.7..-7.6 dB); trumpets against Violins I (B wants 6.5-8.5; stopped because the first tutti's brass is 1.2 dB over the woodwinds); pickup at 851.5 (2 dB too far: Violins I row -6 -> -4); Flute 1 under the solo after 1052 (+0.3..+2.8); Violins I re-bows 1116.3 / 1125.2 (4.1 / 4.3 dB steps); celli join 506 (+4.6); master front under body at 315 / 327 / 915 / 927 (-0.7..-2.5); Violins I 597 (+109 ms); Horn 1 re-tongue 998.57 (9.7 dB).
- Still open from c11, not worked on: Oboe 1 672 (+194), Violins II 672 / 708 (+248 / +138), Flute 1 904 (+146), basses 1071 / 504 (+149 / +120), solo 1044 (+139), Violas 1020 (+109), Horn 1 at 6 (+97), Violins II 900 (-59), basses' 902 step (-10.0 dB), Flute 2 joins (median +30), Bassoon 2 654 (+145), Violas 579 quiet note (metrics). Per-note refits: `loop/ONE_TIME_c13.md` item 2.
- Timpani hard sticks (MANUAL-GAPS #6) not tried (memory). cycles/c08 stems not deleted.
- Pending from Movement I c53: range-render fitting limits, delivery EQ variants on one master, staccato per-pitch shapes on the alias track, return-stem substitution.

Do-not-touch:
- The join offsets fitted this cycle (all inside +-50 ms); `LEG_HEAD_MIN_GAP_S` 0.032; the harp's `VEL_SET` rows and the 216 trim; the brass gains (the family order at the summit and the first tutti depend on them); the timpani roll and 1008 rows; Horn 1's closing contour rows; the C6 rows; `PITCH_TRIM_MIRROR` on Horn 3.
- After a render: guard, full rebuild of the stale tracks without playback, save, guard.
- Wait for memory to settle after an open before a full build.
- Plus c11's items.

### Cycle 13

Accepted:
- A #4: `BEAT_STRETCH` empty (22 unprinted beats, +0.53 s); full build on the new map.
- A #1: Violins I's nine soft theme-head pairs on Sus Marc LITE (the head's row), chosen on one-track range renders against Leg Slur MAX and Slur Runs: second eighth heard 0 -> 164 ms, its start +62 -> -2 ms, two renders identical. Slur Runs failed (late, weak, not repeatable). Celli fugato pairs as legato target + led stroke (now 30-76 ms early); tutti pairs' lead 0.06 -> 0.03 / 0.045 s (median -36 / -33 -> -6 / -17 ms).
- A #2: new generic `LEG_HEAD_AFTER_ROW_LEAD_S` (75 notes): wind heads +36..+69 -> 0..-19 ms (Oboe 1 -43); Violas 382 / 850 +181 / +186 -> +72 / -18.
- A #3: negative `leg_leads.json` rows (12 joins from 60-98 ms off to within 28, Violins I 146 to -46); Flute 2 +0.03 s.
- B #1-#6: hemiola steps (Violins I over Violins II 4-9.5 -> 0.4-3.9 dB, master peak at 908.5 -12.6 -> -15.4), pickup / head shapes, timpani p solo +7 and first-stroke steps (deficits 3-6.5 -> 0-1.4 dB), Oboe 1 rows, trumpets +2 / +2 / A4 +3 (bar 337: 14.7 -> 7.9 dB under Violins I), woodwind chord rows; delivery rows at 300 / 897 -2 -> -1.5 / -0.5.
- C #1a seats (Flute 1 / Oboe 1 L-R +4.6 / -5.2 -> +2.2 / -2.1), C #2 Stereo Double on the solo (correlation 1.00 -> 0.93, gain +2.5), C #3 wind send +3 -> +1.5 (R Winds re dry -9.9..-13.0), C #4 return pans (offsets within 0.51 dB) and harp seat -0.45.
- Two renders (the first had the Marc LITE eighths ringing over the staccato after them). Master -21.0 LUFS, LRA 23.4, TP -1.6. Delivered -19.8 LUFS, LRA 15.0, TP -1.6, limiter 2.8. Probe all ok. Hall: G.P. 20.7 dB at +0.3 s, RT60 1.30-1.32 s. S outside 25 / 60 ms: 31 % / 7 % -> 28 % / 6 % (my measure; critic A's c12 figure 27 % / 6 %). REAPER 45 GB settled, 0 compressed at both renders, 50 / 27 after. Lock 88 min after a 9 h wait.

Rejected/Open:
- Rejected with numbers: Slur Runs; keyswitch 0.15 s early (celli trio tune: no gain, 16 of 30 joins outside 25 ms against 14); A #5 shorter staccatos (pair dips unchanged: remove the rows or try another row).
- No effect: positive `leg_leads.json` rows held by the cap or the 100 ms gap (Violins II 134, 159, 374, 387, 819, 840, 855, 372; celli 171, 180, 207, 891); Flute 2's joins in 912-960 (median +37 ms).
- Too early now: Oboe 1's loud heads (-43 ms: lead 0.055 -> 0.02), celli 173 / 173.5 / 869 / 869.5 (-30..-76: halve), Violins I 146 (-46).
- Bar 49 beat 1 strings still +105..+139 ms (finale technique 49: a Sus MAX stroke 0.06 s early); Violins I 385.5 +80; pickup 383.5 now 5.9 dB over its downbeat on the stem (master +1.6).
- Theme head: the staccato quarter after the pair is the dominant pitch only 40-62 ms after its beat; second eighths at 53.5 / 287.5 / 773.5 7-11 dB over the half note's body.
- One legato row per string line needs a refit of every lead on the line (celli test: all joins 120-260 ms early); first item for c14 with finale 46 (resets) and Movement II c52's method.
- Soft ends 0.31 s (Violins II 444.5) and 0.33 s (solo, with Stereo Double) against the 0.30 s limit. C #1b oboe Main mics, Stereo Double on Violas div and spread 0.6: untested.
- c12's stems and `Backups/` not deleted (refused by the session's safety check). cycles/c08 stems as before.

Do-not-touch:
- `BEAT_STRETCH` empty: no unprinted tempo.
- The theme-head eighths on Sus Marc LITE with their leads, ends and level steps as a set (repeatable between renders); change levels only by the measured residue.
- `LEG_HEAD_AFTER_ROW_LEAD_S` cap 0.3 (0.5 cut the pickup eighth to 85 ms); the winds' 32 ms gap.
- The hemiola steps -8 / -6.5 with the delivery rows -1.5 / -0.5 as a pair; the timpani rows of bars 9-12 and the first-stroke steps; the woodwind seats, return pans, wind send 1.5.
- Discard the first range render after any rebuild; judge a variant on the second and third.
- Plus c12's items.

### Cycle 14

Accepted:
- A #4: one legato row on Violins I, Violoncellos and the solo (Leg BC MAX unloaded, keyswitch 0.15 s early) with a two-step refit of every legato lead on whole-piece passes: joins outside 25 ms Violins I 48 -> 9 of 100, celli 101 -> 24 of 200, solo 10 -> 3 of 18; 1-2 joins per track move between renders. Row-level steps on 19 former Leg BC notes. `JOIN_NOTCH_S` (seconds from the note-on) ported from Movement II.
- A #1 / B #1: theme head levels, one row per figure fitted on the c13 stem with steps on the score onsets: pair 2.5-3.7 dB under the half note's start, landing staccato within 1.4 dB of the pair, half note's tail 4.7-7.8 dB under its start. Velocity cure tested and rejected (Sus Marc LITE ignores velocity for level).
- A #3: 16 late legato heads as Sus MAX strokes with `REATTACK_KEEP_END` (bar 49 beat 1: +116 / +105 / +139 -> +76 / +34 / +28 ms). A #5: Flute 2's slow pitch pairs with a listed cap (over 60 ms 14 -> 7 of 65), Oboe 1 heads -43 -> -10 ms. Soft-end check from the note-off (`hall14.py`).
- B #2: bass, tuba and cello note bells removed (98 Hz halved, not removed): 70-112 Hz share of the tuttis -16.3 / -16.9 -> -14.7 / -15.0 dB; cello themes given back by roles. B #3 harp left hand (low bands against melody bands +6.5 -> -0.1 dB), B #4 clarinet rows, B #5 flute staccato pitch trims, B #6 solo send.
- C #1 fugato entries (master +2..+4 dB, two delivery rows), C #2 `cresc_trim_hold` with higher f anchors on flutes and clarinets (four named crescendos +4 to +5 dB), C #3 last re-bow (dip 5.5 -> 0.8 dB), C #4 / #5 note rows.
- One render, one stem fix (celli and harp roles), second delivery. Master -20.8 LUFS, LRA 22.7, TP -1.5. Delivered -19.8 LUFS, LRA 14.9, TP -1.5, limiter 3.0. Probe all ok. Hall: G.P. 20.7 dB at +0.3 s, RT60 1.30-1.32 s. S outside 25 / 60 ms 28 % / 6 % -> 26 % / 5 %. REAPER 43 GB settled, 43 / 0 after. Lock 92.5 min.

Rejected/Open:
- REAPER lacks the stem-fix roles (celli 312-360 / 912-960 / 624-672, harp 216-240): `--mix-only` first thing in c15.
- Worse: Violas 828 (+187 -> +261 ms with 0.13 s more entry lead: take it back). Short of target: Violins I 144 (+76), 372 (+105, cap), 855 (-61), Violins II 123 (+62), Violas 855 (+68), celli 840 (+56); Flute 2 912-960 still 34 of 65 over 25 ms; trio 169-184 low-mid share -5.3 (B: -6.3); delivered span 19.8 dB; G1 arco still 3 dB over E1.
- The landing staccatos at 42 / 288 / 774 / 798 read S -61..-130 ms since their level step sits on the beat: a reading effect, same MIDI as c13; check by ear or with a dominant-pitch measure.
- Volume envelope (Dan 2026-11-11): 7.1 points per note, 22 % of notes with over 3 dB of swing (c13: 6.9, 21 %): not reduced. The slow / per-note split of `vol_points` and the layer test are c15's (`loop/ONE_TIME_c15.md`).
- Not tried: Sus MAX for the theme head (finale 53), CC16 resets everywhere, delivery rise delay, oboe Main mics, trumpet / cello same-pitch pair dips, first eighths' lead 0.07 s, any MANUAL-GAPS item.
- My hairpin count did not confirm C's 40 of 215; the crescendo rule is verified on C's named cases only.

Do-not-touch:
- The one-row data of Violins I, Violoncellos and the solo as a set: `ROW_REMAP`, `KS_MIN_LEAD_S`, `build/leg_leads.json`, the moved early fills, `build/c14_row_levels.json`. A lead change on these tracks needs two whole-piece passes to judge (`wholepass14.py`, `scmp14.py`); do not add a row for the join at 18 (it moves the opening re-bow off its fill).
- The theme-head rows (`_c14_lv`) with c13's rows, leads, velocities and note ends; do not lower the eighths' velocity.
- The basses' 98 Hz -2 and 73.4 Hz -5 bands with the E1 / B1 note trims; the cello roles that replace the bells.
- `cresc_trim_hold` skip spans 297-312 / 897-912 (the sfp and the summit margin); max hold 3.5 dB.
- Do not rerun `cycles/c14/actor_scripts/apply14.py` alone (it resets the refitted tables).
- Plus c13's items.

### Cycle 15

Accepted:
- Dan's decision (2026-11-11): no per-note track volume moves. `VOL_CLASSES = ("slow",)`: the envelope holds roles, hairpin gains, roll shapes, fades and one-level rows of a bar or more. Points 40,724 -> 4,545 (7.1 -> 0.8 per note, 146.6 -> 16.4 per second over 31 tracks); notes with over 3 dB inside 22 % -> 6 % (strictly inside 598 -> 156). Master sections within 0.3 dB of c14, stems within 1.0 dB except the items below.
- Instrument side: pitch trims as per-region volume in the Opus state on 14 tracks (`region_gain_db`); Violins I "Sus Marc LITE" row -8 dB for the theme head (landing pitch leads at +20 ms in 7 of 9 figures, c14 2); string short rows back on printed CC11 (park off); timpani loud strokes velocity +22; passage constants in roles.json.
- Tools kept from the first half: every envelope item tagged by class and layer, `ONE_LEVEL`, `TRIM_STEP_S`, `ROW_TRIM_HOLD_QN`, `VOL_GRID_QN` 0.125, `env_simplify_db` 0.1 on REAPER's real fader scale (`tools/env_scale.json`), `ENV_SHAPE` test switch; `sim15.py` (an envelope simulated on rendered stems).
- C #2 celli trio tune: 510 / 512 / 567 / 572 +96..+117 -> -11..+17 ms; C #1 fallback rows: Violins II 148-154 +58..+114 -> -7..+18; C #4 Violas 855 +68 -> +2, celli 840 +56 -> -4, Violins II 123 / 897 -> +34 / +18. B #4 brass roles (Trombone 2 -2.0 in 105-120). B #6 delivery row: span 19.8 -> 19.1 dB, limiter 3.0 -> 2.4.
- One render, no stem fix. Master -21.0 LUFS, LRA 22.7, TP -1.4. Delivered -19.8 LUFS, LRA 14.8, TP -1.6, limiter 2.4. Probe all ok. Hall: G.P. 20.8 dB at +0.3 s, RT60 1.30-1.32 s. S outside 25 / 60 ms 26 % / 5 % (same with the envelope divided out: 26 % / 6 %). REAPER 43-44 GB settled, 50 / 32 after. Lock 69.5 min.

Rejected/Open:
- Faults left audible by the decision (CHANGES.md table): printed accents without level, 133 note trims (basses 138 / 140 / 642, G1), row jumps of 3-6 dB, late soft phrase heads (early fills), re-bow dips, join bumps at five joins, detach dips, timpani metric weight. Fix on the instrument side only.
- Timpani velocity +22: 2-5 kHz front +5 dB (harder): try +14 and a role. Cor anglais A4 +2.6..+3.0 dB (region gain does not reach it); horns: 10-18 % of notes 2-5 dB under target; Clarinet 1's 12 skip onsets +3.5.
- Violins I 855 overshot (-61 -> +77 ms); celli 524 still +108; Violins II 146 / 134 / 374 / 840 held by the cap; Violas 828 +185; Flute 1 132 +143 (real); Violins I 372 +136.
- Not done: Violins II / violas refit with the early keyswitch, Sus MAX for the theme pair, A #6 accent leads, MANUAL-GAPS items.
- The saved project holds 4 stale states (Flute 2, Horn 2, Horn 4, Violins I): state_guard and rebuild first. c14 stems, c15 rangetest WAVs and Backups not deleted (refused).

Do-not-touch:
- No per-note volume envelope items (`VOL_CLASSES`); a new level correction goes into the patch (region / row volume), velocity, CC11, note length or a role of a bar or more.
- Compare stem levels as the mean of the channels' powers (a mono sum reads the strings 1.2-1.8 dB low).
- `env_simplify_db` uses `tools/env_scale.json`; do not replace it by a power law.
- Plus c14's items (the one-row data; `apply14.py`), except the theme-head rows and `c14_row_levels.json`, which are no longer played.

### Cycle 16

Accepted:
- Re-bows (A #1, C #1): the two short held notes in one bow; the last G sharp doubled on the idle DIV A instance with interleaved bow changes and CC11 lifts (`HELD_DOUBLE`): dips 12.4-13.5 -> 4.1-6.5 dB, sum level as c15.
- Envelope guard (`note_move_guard` in build_reaper): no unprinted move over 1.9 dB inside a sounding note (101 snaps, 130 holds); 55 role rows over single notes or figures removed. Notes with over 3 dB strictly inside 156 -> 97 (unmarked 57 -> 9); B's count 89 -> 8.
- Accents in CC11 (`CC11_REST_MAP` ff 114 -> 104, `ACCENT_CC`): median over neighbours +0.7 -> +1.4 dB; woodwind bump halved after Dan's note on the finale.
- sfp: Violins I's sf on Sus MAX with CC11 122-127 (+1.1 dB over its upbeat, c15 -2.3); summit margin in the delivery 1.0 -> 1.4-1.8 dB.
- Timpani: velocity +8 capped at 104 with passage roles; roll 336 holds (-30..-34 dB, c15 fell to -45).
- Timing: keyswitch 0.15 s ahead on Violins II / violas, row-change leads, one refit step (`LEAD_SET_AT`): joins over 60 ms Violins II 11 -> 4, celli 7 -> 4.
- Row and region gains by dynamic layer; cor anglais A4 (the row is named "Sus Max"); Oboe 1 at 828 +7-11 dB; brass repeats: gap floor 0.09 s (trumpets 1.5-2.0 -> 6.4-9.3 dB of separation).
- One render, one stem fix (strings, two development sections). Master -20.6 LUFS, LRA 22.9, TP -2.1. Delivered -19.8 LUFS, LRA 14.9, TP -1.6, limiter 2.4. Probe all ok. Hall: G.P. 21.3 dB at +0.3 s, RT60 1.24-1.36 s. S outside 25 / 60 ms 25 % / 5 %. REAPER 43 GB (27 compressed, other processes), 44 / 25 after.

Rejected/Open:
- Accents over +3 dB on Flute 1, Clarinet 1, Bassoon 1; none at ff on strings, violas, basses, Flute 2.
- Celli joins outside 25 ms 28 -> 43 (refit on one pass); sf still 2 dB under its upbeat in the master; roll 332 grows 2.3 dB; celli 504 swell; Horn 1 598; cor anglais sections -2.7..-3.9; Clarinet 1 +3.1 / +3.6 in two sections; held arrivals +1-2 dB on basses, violas, bassoons.
- Not done: 18 Violins test, two-pass refit, pitch refits after the gains, sorting the remaining slow rows by cause, the "drive" phrase-shape check on held horn notes.
- The saved project holds 6 stale states (Contrabassoon, Horn 4, Violins I, Violas, Violoncellos, Violin I solo). c15 stems and `cycles/c16/render_first` not deleted (refused). The lock was held four days across a usage-limit stop.

Do-not-touch:
- `note_move_guard` and the rule behind it; no role row over one or two notes under two bars.
- `HELD_DOUBLE` on the last note with both roles (Violins I -0.5, solo +5.5) as a pair; the two short held notes in one bow.
- `CC11_REST_MAP` with the ff make-up in `dyn_trim_db` as a pair; change accents through `ACCENT_CC` only.
- Timpani velocity cap 104 with its five passage roles; `TIMP_CC1_AT` 1005.
- `build/lead_set.json` rows are absolute leads: refit them only on two agreeing passes.
- Plus c15's items.

### Cycle 17

Accepted:
- Horn 1 Close-led (Close -1.4 / Main -5.2 dB): G sharp 4 fundamental L/R correlation -0.69 / -0.81 -> +0.65 / +0.45, mono loss 8-10 -> 0.9-1.5 dB; soft notes made up in CC11 (0.22 dB per unit at CC11 35), levels by role (stem fix).
- Last G sharp: three bow changes 3.0 s apart, lift complete on the change, copy on "Sus MAX": dips 3.5 / 2.3 / 1.6 dB (c16 4.3-8.2), copy's colour as the section's, sum level as c16.
- Accents per track, 0.08 + 0.20 s from the beat on led notes, none on "Sus Marc LITE", baselines as region gains: isolated accents median +3.1 -> +1.4 dB, over +3 dB 75 -> 33 of 144; every track median at +3 or under except Clarinet 1 (+3.2).
- Lead cap from the previous note's moved note-on (`PREV_MIN_SOUND_S`): the eight late joins 94 -> 174-245 ms of lead; keyswitch rounding fault fixed.
- `HP_GAIN_TO_CC11` (59 gains in CC11, 28 dropped, 25 loud arrivals kept), `CHORD_CC11`, `ROLE_EDGE_MOVED`, guard 1.4 dB: slope guard 42 -> 8 notes. sf of bar 301 3.0 dB over its upbeat.
- Timpani summit strokes at velocity 104 without the cut; celli pp pizzicato velocity 52 (+9.2 dB, at the basses' level); cor anglais, basses G sharp 1, Clarinet 1 C sharp 6 gains; the two c14 celli lines unwritten.
- Two renders, one stem fix (Horn 1). Master -21.7 LUFS, LRA 22.5, TP -3.0. Delivered -19.8 LUFS, LRA 14.3, TP -1.6, limiter 1.6. Probe all ok. Hall: G.P. 20.1 dB at +0.3 s, RT60 1.36 s (late slope 1.53 s). S outside 25 / 60 ms 25 % / 5 %. REAPER 43 GB, 43 / 18 after. Lock 100 min.

Rejected/Open:
- Bars 72 / 300 are 4.6-4.7 dB under c16 (overdone); Violas bar 326 -4.3; 20 master bars over 1.5 dB down, 10 up (`cycles/c17/records/bars_c17_vs_c16.txt`); celli 333-341 2.2 dB under their line.
- Roles 172 -> 177: B's sorting removed 17, the first render's section drops put 22 section rows back. Mapping rows not moved into trims.
- Horn 1 is drier and narrower (call correlation 0.98); Horn 3's G sharp 4 untreated; `channel_map` untested; B flat 4 unchecked.
- Not done: Violas div spread, woodwind Main mics, join holes, Horn 1 598, per-join S readings.
- The saved project holds 4 stale states (Horn 2, Horn 4, Violins I, Violoncellos).

Do-not-touch:
- Horn 1's mic pair with its gain, CC11 offsets and roles as a set.
- `HELD_DOUBLE` times, lift and the solo role +4.5 as a set; a range test of the last note must start before qn 1003.99.
- `HP_GAIN_TO_CC11` `max_arrival_cc` 100 (gains into ff arrivals are lost in CC11).
- `apply17.py` rewrites roles.json and mix.json from `cycles/c17/before/` with `records/horn1_mix.json` and `records/fix_roles.json`.

## c18 (2026-11-16 / 17; rendered 06:40 on 17 Nov; `cycles/c18/CHANGES.md`)
Accepted:
- Crescendo gains:
  - they stay in the envelope on every track except Flute 1, cor anglais and Violins I and II (CC11 slope under 0.15 dB per unit), released slowly, across printed decrescendos or in rests;
  - chained bassoon gains are held;
  - the sfp gain is held through the sf.
- Bar 72 / 300 accents at +8 on every woodwind.
- Flute 2 matched to Flute 1 in the tuttis.
- Summit chords keep their CC11; timpani summit strokes at velocity 114.
- c17 low-group rows deleted.
- Wind and brass pitch-change overlap 0.04 s.
- Half-step lead corrections.
- Fugato CC11 lifts.
- Inner-line phrase rows (tutti countermelody, celli from 840).
- Horn 3 "Mono From Left".
- Delivery at -14 LUFS (shared target) with ride rows on the trio ff, bars 72 / 300 and the second tutti. Summit +0.7 LU on the mp3, +1.6 LU on the master. LRA 12.0, p10 short-term -21.7, limiter 5.5 dB on the summit.

Rejected / Open:
- LEG_TRANS_CC (CC11 dips over string legato transitions) changed nothing (join excess median 3.2 -> 3.1); remove it or test it on a range first.
- Horn 1 velocity 72 left the 1078 hole (-16 dB).
- f arrivals are still 1.8-2.2 dB under c16.
- Not rendered yet, in `build/`: bars 18 / 258 (Violins I "Sus MAX" -7 dB) reverted; Violins II fugato +30 -> +24.
- Horn 3 +3.7 dB and mono: re-level it per pitch.
- Bar 300 is level with the tuttis on the master.
- 5 stale states in the saved project.

Do-not-touch:
- The delivery chain:
  - -14 LUFS, ceiling 0.85, top ride 2.5:1 from 10 dB under p95, lift 1.6, knee 7, peak compressor;
  - the c18 ride rows;
  - the climax margin is set there, not by mix trims.
- `HP_GAIN_TO_CC11` per track as set in c18; the tutti countermelody rows.

## c19 (2026-11-17, actor on the c18 render; `cycles/c19/CHANGES.md`)
Rendered once; mp3 -14.0 LUFS, LRA 12.2, TP -1.4 dBTP, limiter 5.6 dB on the summit, summit +0.6 LU on the mp3 (+1.3 master); probe 0.
Accepted:
- LEG_TRANS_CC removed.
- Wind overlap only on the played non-legato row (clarinets off "Leg Slur Rep"), woodwinds 0.6 s or longer: the hemiola notes are back within 30 ms (cor anglais 306 / 906 still +68 / +58).
- Horn 1 G sharps 442 / 598 / 1077 on "Sus MAX" 0.05 s early: hole 10-12 -> 1.6-3.4 dB.
- Violins II trio +9 units: 8.6-9.8 -> 4.2-5.7 dB under the celli.
- Celli fugato +8 units.
- Leads:
  - celli 933 / 948 at their c17 values;
  - Violins I 597 a Sus MAX stroke (xr 92 -> 19, pc unchanged);
  - Horn 3 510 / 519 re-tongue cap 0.46 (+63 / +73 -> +33 / +31).
- Clarinet 1 CC1 f-fff lower: -0.9 dB only.
- Violins I Marc halves vel<66 -4 dB: -3 dB.
- Bar 328 hold back: +1.9 dB.
- Roles 164 -> 153; no per-note rows left on trumpets, Horns 3-4 or timpani.
- Delivery: loudness loop and 2:1 top ride; the trio ride row ramps over bar 209 (arrival +1.2 on the mp3, was 0).

Rejected / open:
- TLeg region gain -2 dB on the celli (range test: no change, one hole). The string legato swell stays (median +3.2 dB).
- Not rendered, in build/: Clarinet 1 ff trim -1.0.
- Open:
  - Clarinet 1 still +3 dB over Violins I at 214 / 302 / 334;
  - Violins II's stroke accents;
  - the Horn 1 / 3 hand-off at 1092;
  - tutti downbeat weight;
  - no summit step over bar 335 on the mp3 (the limiter).
- 6 stale states in the saved project.

Do-not-touch:
- Horn 1 "Sus MAX" G sharps;
- the clarinets off the overlap;
- the woodwind overlap at 0.6 s;
- the Violins II trio +9;
- REP_GAP_FLOOR_LONG_S (it does act on 40 held repeats);
- delivery: 2:1 top ride and the loudness loop.

## c20 (2026-11-17, actor on the c19 render; `cycles/c20/CHANGES.md`)
Rendered once; mp3 -14.1 LUFS, LRA 12.3, TP -1.4 dBTP, limiter 5.5 dB on the summit, summit +0.7 LU on the mp3 and +0.9 LU over bar 335 (was 0.0); probe 0.
Accepted:
- Inner lines:
  - violas' stale trio rows deleted (best band +0.7..+3.7 dB);
  - Violins II trio add rising to +17 (+1.7..+2.9 dB);
  - Oboe 1 p staccato layer +6 dB in the Opus state (9.0 -> 4.3 dB under Flute 1).
- Violins I slurred eighth pairs on "Detache" (range test: holes 4 -> 1 of 12; bar 23 -13 -> -3..-8 dB).
- Violins II "Stac RRx9" release 749 -> 150 ms (`any_dyn`): repeated-eighth dips 1.7 -> 2.8 dB.
- Cor anglais / Flute 1 accent bumps and 0.04 s earlier accented Sus after staccato: accent medians -4.8 / -1.7 -> -2.4 / +0.1.
- Summit ride row 990-1005.
- Cor anglais CC1 45 on the hemiola notes (swing 8.5-13.4 -> 1.7-6.9 dB).
- Clarinet 1 trio-return hairpin gains dropped.
- Timpani bar 335 velocities.
- Three hot or cold staccato notes moved into the next velocity layer.
Rejected / Open:
- Violas TLeg -6, celli LegatoSpeed RELEASE 200, "Sus MAX" on legato arrivals (a 14 dB hole): the string legato swell stays.
- StacSl pairs (-10..-14 / +6..+14 dB, 54 thousand regions); Detache on Violins II (no better).
- Horn 1 CC1 cap 51: brightness only -4 dB, body -6 dB; removed in build/ and REAPER (not rendered).
- Violins I 999 on Marc LITE: no gain (-4.9 dB).
- Clarinet 1 "Leg Slur" test void (keyswitch before the range start).
- Open: Clarinet 1 beat 640 +5.1 over Violins I; Violins II bars 181-183 -4..-7; accents' median -0.8.
Do-not-touch:
- Detache pairs on Violins I;
- Violins II Stac cap;
- the violas' trio without role rows;
- Oboe 1 stac vel<75 +3;
- summit ride row;
- delivery chain (2:1 top ride, loudness loop).

## c21 (2026-11-17, actor on the c20 render; `cycles/c21/CHANGES.md`)
Rendered once; mp3 -14.1 LUFS, LRA 12.1, TP -1.3 dBTP, limiter 5.7 dB on the summit, summit +0.4 LU over bar 318; probe 0; G.P. drop on the mp3 19.5 dB, 20 dB fall 0.32 s.
Accepted:
- Dan's bar 23 note: Violins I's slurred pairs back on "Sus MAX" (c19 state). Detache's 5286 ms releases blurred the figure; the range test's decay before the next note was 5.0-6.2 dB against 2.1-4.9.
- Coda stretto: role rows +4 dB on three entries plus CC11 on the celli's half note; mp3 bars 325-327 +2.7..+4.0 LU, and 975 -4.0 -> -0.1 dB.
- G.P. delivery ride row.
- Short-row release caps on Violins II spiccato, violas, celli and basses (violas separation 4.2 -> 6.8 dB).
- Violins I 999 on Sus MAX (-4.9 -> -3.0).
- Bassoon 2's trio swell gone (phrase-shape build rule, trio only; 546 -6 dB).
- Oboe 1 "Sus Accent MAX" on four p accents (peak 0.29 -> 0.03 s).
- Accent leads on more tracks; Clarinet 1 F sharp 5 -2.5 dB; Violas div Stereo Double 0.6.
Rejected / Open:
- Detache with cap and lead; the Violins I short-row caps (short-note peaks -6..-8 dB).
- Legato sustain attack 400 / 250 ms (it lowered the whole note, with more holes); Clarinet 1 Leg Slur (holes 1 -> 4).
- Horn 3 Mid or Horn 1's mix (correlation 0.94-0.97); cor anglais Sus Accent.
- Open: soft Violins I pairs about 7 dB under their neighbours; Violins I counterstatement eighths 0.7 dB apart; legato swell; accent median under +1; summit margin 0.4 LU over bar 318; woodwind Main -6 dB (offline: Oboe 1 correlation 0.90).
Do-not-touch:
- Sus MAX pairs on Violins I (Dan's blur note);
- no release cap on the Violins I short rows;
- the string caps on Violins II, violas, celli and basses;
- the stretto rows;
- the G.P. ride row;
- PHRASE_SHAPE rule kept to the trio.

## c22 (2026-11-17, actor on the c21 render; `cycles/c22/CHANGES.md`)
Rendered once; mp3 -14.0 LUFS, LRA 10.6, TP -1.4 dBTP, limiter 2.7 dB on the summit, summit +0.6 LU over bar 335 (+0.7 over every rival tutti), f -> ff 2.2 LU, p10 -20.2; probe 0; G.P. drop on the mp3 18.9 dB, 20 dB fall 0.33 s.
Accepted:
- Bar 23 figure: CC11 lift ending just after the second pair note's note-on on bars 38 and 263 (pairs -7.0 / -13.2 -> -3.9 / -8.7 and -17.4 / -11.9 -> -7.9 / -5.8 dB; decay before the landing note 6.5 -> 7.3, 5.1 -> 5.7); bar 23 unchanged.
- Inner lines: Clarinets 1-2 rows over bars 37-43, Violins II -3 / violas +5 in the coda build, bass clarinet row deleted, Horn 4 +3 (each line +2..+4 dB best band).
- Summit cuts from 1004.75, halved (celli ff -38.4 -> -32.4, fff over ff).
- `HP_TARGET_LOOKAHEAD_QN` 2.5 (Flute 1 into 105 / 305); Clarinet 1 row from 900.5.
- Flute 1 / 2 "Sus Accent MAX" (accents -2.2 / -1.4 -> +1.4 / +0.4, peak 0.07 s); Oboe 1 accent velocity 96 / 105.
- Delivery: peak comp -9 dB 3:1, top ride 6 dB under p95, lift 2.1, ride rows bar 53 / 218 / counterstatement (spec items 1-6 met).
- Violas fugato CC11 +8; cor anglais / Horn 2 dynamic trims.
Rejected / Open:
- The lift on all seven pairs (second note grew into the landing note), "Sus Marc LITE" pairs, the lift at bar 23 (raised the quarter before it).
- Violins II / violas accents on "Sus Marc LITE" (range test -47 / +49 dB at the hemiola).
- 0.07 s first-eighth lead (no gain); Sus MAX release-trail cap not tested.
- No peak compressor (summit limiter 9.7 dB).
- Open: bar 23 pair 13 dB under; Flute 1 crescendos flat with a 9-10 dB step; summit 2.4 dB over the coda ff; string accent fronts.
Do-not-touch:
- Sus MAX pairs (bar 23 state);
- the delivery chain and its ride rows;
- the c22 inner-line rows;
- the summit cuts from 1004.75.

## c23 (2026-11-17, actor on the c22 render; `cycles/c23/CHANGES.md`)
Rendered once; mp3 (with the new -60 LUFS room-noise bed) -14.0 LUFS, LRA 10.5, TP -1.4 dBTP, limiter 2.8 dB on the summit, summit +0.64 LU over bar 318, f -> ff 2.2 LU, p10 -20.2; probe 0; G.P. drop on the mp3 18.9 dB, 20 dB fall 0.33 s. Horn 2 / Horn 4 stale in the saved project (not rebuilt after the save).
Accepted:
- Bar 23: lead 0.10 s on G / A, each ending 0.03 s before the next note-on (A -> B decay 1.8 -> 5.8 dB, figure median 2.9 -> 3.4, pair -13.5 / -13.2 -> -7.6 / -10.7).
- Woodwind summit rows from 996 again (winds over strings +2.4..+3.2 -> +0.4..+1.3 dB; step into the summit 1.3 -> 2.1 dB on the master).
- Flute 1 [648, 660, -4] (trio climax +4.8..+5.4 -> +0.8..+1.4 dB over Violins I).
- Flute accent overlay -1.5 dB, G6 -2 dB (999 over Violins I +6.4 -> +2.3).
- Oboe 1 tutti accents on "Sus Accent MAX".
- Room-noise bed in deliver_master.py.
Rejected / Open:
- CC1 floor (the A grew into the B), Sus MAX p cap 150 ms (no change), lead route on the loud pairs (decay 2.0 -> 0.4).
- Violins I STAC_MIN_SOUND_S + short-row cap (peaks -5..-20 dB).
- Cor anglais / Clarinet 2 accent rows; dropping the violins' 0.04 s accent add; Violins II Marc Lng (broke notes).
- Flute 1 crescendo CC11 ramp kept but inert (CC11_REST_MAP 108).
- Open: bar 23 pair 8-11 dB under, F sharp -> G 1.4 dB; string accent fronts; Violins I staccato separation; 9 slope-guard notes (named in CHANGES); Horn 2 / 4 stale.
Do-not-touch:
- bar 38 / 263 CC11 lifts and the c22 pair states;
- no release cap on the Violins I short rows (twice negative);
- the delivery chain plus bed;
- the woodwind summit rows from 996 with celli / Horn 1 at 1004.75.

## c24 (2026-11-18, actor on the c23 render; `cycles/c24/CHANGES.md`)
Rendered once (after a disk wait); mp3 -14.0 LUFS, LRA 10.5, TP -1.3 dBTP, limiter 3.8 dB on the summit, summit +0.55 LU over bar 335, f -> ff 2.24 LU, p10 -20.1; probe 0; G.P. drop on the mp3 18.9 dB, RT60 1.38-1.50 s. Master -21.2 LUFS, TP -0.4.
Accepted:
- Fixed fader guard on the envelope REAPER gets (`guard24.py`) and generic `note_slew` (4 dB/s, ramps at most 2 qn): steps 175 -> 25, first-0.35 s changes 205 -> 64, critic B's measure 59 -> 0 (target 0 not met: the 2 qn cap keeps passage levels; 16 track-bars still change by more than 1.5 dB).
- Role edges at moved note-ons / rests (celli 310.6 / 910.6 / 623.3, violas 359.45, harp 1019); celli 362 and violas 197 rows as CC11; `ARRIVAL_WEIGHT_MOVED`.
- PHRASE_SHAPE start -4 / peak 6 / end -8, no wind scale, builds at -6 (entries 7 dB+ under 6 -> 3).
- Theme A basses [36, 90, -3], celli row removed (basses over celli +7.4 -> +2.4 dB).
- Violins I: D5 / D sharp 5 / F sharp 5 staccatos on Spiccato RRx9, short rows' no-start-mode group switched off (separation 4.2 -> 5.2 dB overall, those pitches 0.0-2.2 -> 4.7-7.6; isolated tails -50 -> -93 dB at +0.5 s).
- Bar 23 CC11 lift after the trough (figure 3.4 / 4.5 -> 4.4 / 7.7 dB).
- Flute 1 hemiola: no held gain, velocity 70 -> 100 (312 over 314 +8.2 -> +5.1, 912 +4.8 -> +1.8).
- Celli velocity 112 on wide legato targets, CC16 reset at 167, CC11 counter-shape 516 / 526 (trio tune steps over 4 dB 7 -> 3); ride row [645-659] removed; harp cap 45 at 1040-1068; room bed identical to Movement I's.
Rejected / Open:
- Range tests made right after a rebuild lose notes (void); orphan cap variant not re-run.
- A #5 mechanism wrong (Sus Marc LITE / config, no cap); leg_leads refit, Leg BC, hard sticks, CC7 trims (finale 135 / 136) not done.
- Open: bars 115 / 315 figure 5.8 / 5.4 -> 3.3 dB (round robins after the Spiccato F sharp); celli forte before the sub. p of 277 and the 349 entry +4.7 / +5.4 dB (slew anticipation); Flute 1 312 +5 dB; violas' 576 entry 8 dB under the celli; 25 + 64 guard notes.
Do-not-touch:
- bar 23 state (leads, ends, lift); bar 38 / 263 lifts;
- the Spiccato pitches and the switched-off orphan groups (unless the 115 / 315 fix needs the tutti F sharp back on Stac RRx14);
- the delivery chain plus bed; the woodwind summit rows from 996.

## c25 (2026-11-18, actor on the c24 render; `cycles/c25/CHANGES.md`)
Rendered once (mp3 delivered twice from the same master: a ride-trim change for LRA); mp3 -14.0 LUFS, LRA 10.5, TP -1.3 dBTP, limiter 3.7 dB on the summit, summit +0.56 LU over 335, f -> ff 2.31 LU, p10 -20.3; probe 0; G.P. drop on the mp3 17.2 dB, RT60 1.44-1.50 s. Master -21.1 LUFS. Lock 56 min, REAPER 44 GB after the render.
Accepted:
- Dynamic trims in CC7 on moved time (`dyn_trim_to_cc7`; law range-tested on HO woodwind / brass and HS strings: 0.00-0.01 dB median); `cc7_spans_db` passage levels; `HP_START_MOVED`, `HP_HOLD_TO_NOTE_END` (only with a rest after). Guard 25 / 64 -> 9 / 9 notes; envelope 16.3 -> 9.7 points per second.
- Violins I rerouted Spiccato notes: velocity -13 under 90 (1-54 layer, cut 2 dB) and the 90+ layers -4 dB: +3.8 -> +1.4 dB over neighbours, F sharp 342 / 942 now under the accented C; separation 4.8-6.1 dB; bar 23 within 1.3 dB of c24.
- Summit: arrival weight only with a printed rise (`ARRIVAL_WEIGHT_RISE_ONLY`), hold cap 1.5 qn, +3.0 (Trumpet 1 -2.4 dB).
- Inner lines: Flute 1 reprise row deleted (line -0.4 -> +2.4 dB), col Vl. solo -9.5 -> -6.5 (-48.9 -> -45.9 dB), CC7 accompaniment cuts (828-840, 672-684) and viola div. lifts (pair -4.6 -> -2.6 worst); Oboe 1 / Clarinet 2 role falls as CC7; Horn 1 1068 edge in the rest; trombone / tuba 993 head kept soft with CC7.
- Celli leg_leads +0.08 s (trio +36 -> +30 ms; 576 +144 -> +2 ms); cor anglais accents +0.05 s; delivery fugato lifts +2 -> +1.5 (LRA 10.4 -> 10.5).
Rejected / Open:
- A's "vel>=80" alone misses v81-87 (the layer starts at 90); velocity -10 alone left soft notes +2.5..+2.9; C's whole-row -2.5 not needed.
- Open: celli trio 510 / 512 / 528 still +80..+100 ms (leads capped), 542 now -89; viola div. bar 221 -2.6; Trumpet 1 3 dB over Horn 1 at the summit; E -> B at 117 / 317 11-12 dB (c18 15.4, cause not found); 9 + 9 guard notes (short printed hairpins on held notes, positive role ends without CC7 headroom); item 6 (Violins I stac length, oboe Main mic test) not done.
Do-not-touch:
- the CC7 trim lane and its moved-time warp (the law holds; a trim change needs `--midi-only`);
- the Spiccato layer cuts (v<55 -2, v>=90 -4) with velocity -13;
- bar 23 state; the delivery chain plus bed; RIDE_TRIMS fugato +1.5 (LRA).

## c26 (2026-11-18, actor on the c25 render; `cycles/c26/CHANGES.md`)
Rendered once (mp3 delivered twice from the same master: fugato ride lifts +1.5 -> +0.5 for LRA); mp3 -14.0 LUFS, LRA 10.5, TP -1.4 dBTP, limiter 3.6 dB on the summit, summit +0.68 LU over 335, f -> ff 2.23 LU, p10 -20.3; probe 0; G.P. drop on the mp3 19.0 dB, RT60 1.42-1.50 s. Master -24.4 LUFS (every track -3 dB from c26), peak -2.8 dBFS. Lock 68 min, REAPER 44 GB after the render.
Accepted:
- Woodwind figure (A #1): slur end 35 ms before the staccato in the tuttis (`SLUR_END_BEFORE_STAC`), 120 ms cap on f sustain + TLeg groups (`tleg`), f trails -6 dB (`rt_gain_db` `dyn`), Oboe 1 tutti staccatos v118: +70 ms medians Flute 1 -5.3 -> +8.5, Flute 2 +0.2 -> +12.5, Oboe 1 +8.1 -> +17.6, Clarinet 2 +3.8 -> +18.9 dB; joins unchanged.
- `HP_HOLD_TO_NOTE_END` skips holds under printed decrescendos (C #3: the six of bar 72 / 549).
- `stretch_cc7` (build_reaper): the envelope's moves inside stretches of 16 qn or less go into CC7, net level p99 0.1-0.3 dB; guard 9 / 9 -> 0 / 0.
- Summit: trumpet / Horn 1 role rows deleted; 1005 stroke on "Sus Marc LITE" (Violins I / II, violas, v92, 0.085 s) + CC11 counter-shape: master peak +0.52 -> +0.18 s, step +1.0 -> +1.8 dB.
- Accent `lead_s` 0.06 + CC11 `body_cc` (A #2): peaks 0.25-0.27 -> 0.21-0.23 s on the violins; medians still under target.
- sfp `cresc_after_fp`, 902 lift +12, ride row lets the sf through; Spiccato three-row split (median +1.4 -> -0.7); celli trio leads; Flute 2 213 v110; viola lifts removed; global gain -3 dB, render_cycle -1 dBFS warning.
Rejected / Open:
- C #4 ppp ride cuts (Dan's -14 note). Not done: Violins I staccato length (A #4), bar 200 re-attack, timpani roll 237-240.
- Open: accents -2.3..-5.4 dB under neighbours (strings, cor anglais, Clarinet 2, Oboe 1); summit step +1.8 (target +3); Flute 1 / cor anglais 156 / 384 fade (now in CC7); 152 CC7 moves of 1 dB+ inside notes outside hairpins (the old envelope edges, same net level); Violins II bar 315 B -> C 14.3 (17.3).
Do-not-touch:
- stretch_cc7 and the CC7 trim lane (a trim, span or role change needs `--midi-only`); the woodwind figure state (slur ends, caps, trails, Oboe v118);
- bar 23 state; the Spiccato split; the delivery chain plus bed and the fugato ride +0.5 (LRA 10.5).

## c27 (2026-11-18, actor on the c26 render; `cycles/c27/CHANGES.md`)
Rendered once; mp3 -14.0 LUFS, LRA 10.6, TP -1.4 dBTP, limiter 3.3 dB, summit +0.57 LU over 335, f -> ff 2.10 LU, p10 -20.4; probe 0; G.P. drop on the mp3 17.2 dB, RT60 1.42-1.49 s. Master -24.2 LUFS, sample peak 0.627. Lock 65 min, REAPER 44 GB after the render.
Accepted:
- Arrival holds (B #1): kept crescendo gains and held trims stay to the next printed change, cap 8 qn, then a release in a rest or a step at the next re-attack (`hold_until_mark_qn`, `cresc_trim_hold` release_at mark, positions through the CC7 warp); `note_slew` onset_step_s, skip_hairpins; unison-boost edges in rests / at note-ons. Net in-note moves outside hairpins 70 -> 48; coda woodwinds no longer fall at bar 333 (fff = ff on Clarinet 2 / Bassoon 1, summit rows from 984).
- Violins I soft heads: Sus Marc LITE vel<66 -6 (front +2.1 -> -0.9, 2-5 kHz +6.3 -> +3.3) + CC11 marc_lift (hole -7.2 -> -5.8).
- Accent leads removed (Violins I row-change add, cor anglais +0.05 s); Clarinet 2 bump 8; violas add_loud 14; body dip (0.14, 0.24); violas' off-beat double stops v82 (-5.2 dB).
- SOFT_LEG_HEAD_CC (finale 139): soft legato heads -6 dB point median 213 -> 131 ms. Celli RR resets one bar before the ritmo di tre battute heads (+3.3 dB). Spiccato F sharp v90+ -3 dB.
Rejected / Open:
- Flute 2 slur end 20 ms (figure worse); basses' RR resets (no gain); B's 16 qn hold (celli +5.4 dB for 13 qn).
- Open: tutti downbeat weight 0.0 / +0.9 dB on the master; accent fronts -0.6..-1.8 dB on A's measure; summit step +1.4 dB; soft heads' hole -10.7 dB lowest; accented C 345 / 945 0.8 dB under the F sharp before it; trio climax 632 cap steps 2-3 dB; Violins I eighths v62 and staccato ring test not run.
Do-not-touch:
- the c26 woodwind figure state (+70 ms medians +9..+22 dB) and bar 23 state (83->84 9.1 -> 12.4);
- stretch_cc7 and the CC7 trim lane (a trim, span, role or hold change needs `--midi-only`); the new hold caps (8 qn, rest / re-attack release);
- the Spiccato split; the delivery chain plus bed and the fugato ride +0.5 (LRA 10.6).

## c28 (2026-11-18, actor on the c27 render; `cycles/c28/CHANGES.md`)
Rendered once (mp3 delivered twice from the same master: ride rows moved off the 104 / 304 / 305 ff arrivals); mp3 -14.0 LUFS, LRA 10.9, TP -1.4 dBTP, limiter 3.7 dB, summit +0.67 LU over 335, f -> ff 1.88 LU, p10 -20.6; probe 0; G.P. drop on the mp3 17.9 dB, RT60 1.40-1.51 s. Master -23.8 LUFS, sample peak 0.702. Lock 57 min, REAPER 44 GB after the render.
Accepted:
- Spiccato reroute only for same-pitch pairs (`STAC_ROW_BY_PITCH_REP_ONLY`): bars 110 / 310 79->78 2.8 / 2.5 -> 3.7 / 4.3, F sharp 342 now 3.2 dB under the accented C.
- Arrival holds to the printed decrescendo (`hold_to_dec_qn` 32, rest 2 qn, short arrivals held; trim hold the same); tutti crescendo gains at 309-310 / 909-910 dropped on winds / strings: sags of 1.5 dB+ 35 -> 7; trio climax master sag 4.3 -> 2.6 dB; net in-note moves outside hairpins 48 -> 34.
- Summit arrival weight -> passage level [1005, 1017, +2.5] (lead +0.57 -> +0.67 LU; step +1.4 -> +1.1).
- Timpani Hrd KS (whole movement) with a velocity-layer refit: 1-5 kHz share +2..+10 dB, rolls within 1 dB.
- Violins I / II accent body (0.22, 0.36), add_loud 14 / 10; soft-head eighths v62 (2-5 kHz +5.6 -> -0.1 dB); Violins I reprise CC7 +1.9 dB; Horn 3 / 4 roles from 311.5 / 911.5; build stops above +23.5 dB envelope.
Rejected / Open:
- Tenuto quarters on Marc Lng / Portato (range test: later, trombones 6 dB softer); hold_through_rise; harp role move; cor anglais dip change.
- Open: tutti downbeats -0.1 / +0.7 dB on the mp3; f -> ff 1.88 (bars 104 / 304 without crescendo gain); summit step +1.1; accents -0.9..-1.5 dB; soft-stick coda strokes on hard sticks (one instance cannot switch); Oboe 1 387 / 855 4.6 dB step; trio celli +5.4 dB for 14 qn (judge); bars 115 / 315 first step margin 22 -> 13 dB.
Do-not-touch:
- the c26 woodwind figure state; bar 23 state; the pair-only Spiccato reroute and its layer cuts;
- stretch_cc7, the CC7 trim lane and the hold rules (a trim, span, role or hold change needs `--midi-only`);
- the delivery chain plus bed and the moved ride rows (LRA 10.9).

## c29 (2026-11-18, actor on the c28 render; `cycles/c29/CHANGES.md`)
Rendered once in two passes (main 31 tracks + pass-2 felt timpani alias); mp3 -14.1 LUFS, LRA 11.4, TP -1.2 dBTP, limiter 3.9 dB, summit +0.60 LU over bar 318, f -> ff 2.23 LU, p10 -21.0 (all six spec items met); probe 0; G.P. drop on the mp3 17.8 dB, RT60 1.40-1.50 s. Master -23.9 LUFS, sample peak 0.702. Lock 82 min, REAPER 44 GB after the main render, pass-2 project 1.2 GB.
Accepted:
- Delivery TOP_ABOVE -3, coda ride row deeper, Violins I theme A +1.5 dB passage row (f -> ff 1.88 -> 2.23).
- Trio climax roles: celli -3.5, violas / Violas div -3.0 (tune over celli 6.2-9.4 dB in 213-216; Violins I over celli every bar).
- Timpani soft / medium sticks on a felt alias in pass 2 (1-5 kHz share -35 / -28 / -29 dB against hard -21 / -18 / -19).
- Horn 3 Stereo with Horn 1's mics (relay corr 0.74 / L-R +1.9 / tilt -9.0 against Horn 1 0.68 / +1.0 / -8.3; G sharp corr +0.58).
- Tutti tenutos end at q + 0.85 (tenuto group downbeat +2.3 -> +4.4 dB); celli heads 312 / 912 on Sus MAX with a 0.06 s lead.
Rejected / Open:
- Brass Sus Accent MAX v70, basses Marc Sus LITE v80, violas v88 / v92 (range test).
- Open: mp3 downbeat +0.3 dB; celli heads 5.3-5.7 dB under the body; coda soft strokes +1.9 dB over c28; Horn 3 countermelody corr 0.97; 33 notes with 1.5 dB+ CC7 changes in their first 50 ms (pre-existing); 1005 woodwind moves; oboe Main mic.
Do-not-touch:
- the c26 woodwind figure state (gate 0 under +3) and the figure at every occurrence (within 1 dB of c28);
- the felt alias windows (435-864, 1020-1128, start and end in rests) and the hard-stick Allegro; Horn 3's routing and G sharp region gain;
- the delivery chain plus bed, TOP_ABOVE -3 and the ride rows (LRA 11.4).

## c30 (2026-11-18, actor on the c29 render; last cycle of the run; `cycles/c30/CHANGES.md`)
Rendered once in two passes; mp3 delivered twice from one master (coda ride row deepened); mp3 -13.8 LUFS, LRA 11.8, TP -1.4 dBTP, limiter 4.2 dB, summit +0.56 LU over bar 335, f -> ff 2.07 LU, p10 -21.1 (all six spec items met); probe 0; G.P. drop on the mp3 17.2 dB, RT60 1.40-1.50 s. Master -23.9 LUFS, sample peak 0.702. Lock 81 min, REAPER 45 GB after the main render.
Accepted:
- Dan's 0:39 note (bars 53-55, reprise 285-287): legato targets after a quarter led 0.22 s swallowed the quarter (crossover -316 ms); 7 notes as fresh Sus MAX heads (leads 0.06-0.18 s), lead_set entries dropped: crossover -52..+8 ms, attacks +20..+32 ms at 159, celli 154 +252 -> +62, violas 162 +105 -> -3.
- Horn 3 E4 region gain -5 (E4 -3.5 dB); unison-boost runs merged across boost values (Horn 3 in-note swells gone); celli head roles from 312 / 912 (head gap 3.9 -> 1.2 dB); summit string edges at 1005 with chained edges pinned.
- Horn 1's one-note +6 dB row deleted, CC11 +20 (close no longer rises: mp3 364 -> 372 +4.2 -> -0.3 LU); MOM_CAP_ABOVE 0 + solo ride rows (horn call -10.4 -> -13.0 LUFS momentary).
- Celli fugato CC11 +9 (gap 6.8 -> 2.4 dB); brass 309 / 310 gains dropped (-2 dB); roll 205-208 slower release; coda ppp velocities.
Rejected / Open:
- UNI_RUN_GAP_QN 3.0 (merged other tracks' runs across rests); C #5 stretto ride; A #3, A #4, A #6 not done.
- Open: summit stroke still swells (Violins II front -12.9 dB: the sample, not CC7); roll 205-208 only 2.8 dB under the master at its f; coda ppp strokes 9-12 dB under pp (overshoot); reprise violas joins +116 / +222 ms; Horn 3 B3 transition hot; arrival 105 -0.5, 305 -0.3.
Do-not-touch:
- the c26 woodwind figure state and the figure at every occurrence (within 1 dB of c29); the new heads at 154 / 159 / 162 / 850 / 855;
- Horn 3's Stereo routing, mics, G sharp gain; the felt alias; the trio roles; both sub. p's and the sfp at 301;
- the delivery chain: TOP_ABOVE -3, MOM_CAP_ABOVE 0, the ride rows (coda row to -6.5).

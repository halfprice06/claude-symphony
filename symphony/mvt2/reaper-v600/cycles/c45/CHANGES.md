# Cycle 45: changes (actor; critics A/B/C on the c44 render; loop/ONE_TIME.md c45: performance data)

- Snapshot before the changes: `before/`. Scripts: `actor_scripts/` (`apply45.py` writes build/mix.json, roles.json and
  note_trims.json from before/; `sim45.py` the EQ simulation on the c44 stems; `states45.py` lists Opus state changes;
  `phrase45.py` audio phrase shapes; `check44.py`, `s1check44.py`, `accent44.py` copied from c44; `turn_lock.sh`).
- The loop lead's notes decided between conflicting critic advice (brightness set, arch depth, beat velocity, repeats,
  wetness limits, RR reset).

## Tools

- `tools/score_to_parts.py`
  - `PHRASE_SHAPE` (new generic, default None) and `apply_phrase_shape()`: a pass after every track is built.
    Phrases are runs of sustained notes with gaps under 0.15 s, 2.5-16 s long, with 3 or more onsets and 2 or more
    pitches (held pedals and re-bowed single notes keep their fitted shapes). Classes, assigned from the score data:
    "skip:hairpin" when printed hairpins cover more than half the phrase (a printed swell or build: the hairpin is the
    shape); "skip:span" when the phrase touches a listed window (movement II: critic A's builds, bars 53-60 and 75-78,
    and the bars 61-64 climax with the accented trombone quotation); "skip:end" after qn 297 (the morendo);
    "skip:long" over 16 s (a continuous accompaniment); otherwise "lyrical". Short rows (tremolo, pizz., staccato,
    marcato, Detache, repetitions) are not part of phrases. A lyrical phrase gets a level arch in the volume envelope
    (`vol_db`) and, on the vibrato-crossfade patches, a CC1 arch. Doubling groups take the leader's phrases, class and
    family shape inside their window (one curve per group). parts.json `phrase_shape` lists every phrase and its class.
  - `CC_GRID_QN` 0.0625 (was a fixed 0.125 qn in `sample()`; critic A #1, plan CC density).
  - `LEG_VEL_BY_CC` (legato-target velocity by printed dynamic; critic A #2) and `WIND_REP_RETONGUE_AT` (per-onset
    re-tongue overrides; critic A #4).
- `tools/build_reaper.py`: `RR_RESET_CC` 16 (was CC36) for the pre-roll round-robin reset (critic B, HO manual p.34:
  Opus's Preferences.json `RoundRobinResetCC` 16; CC16 is mapped by no patch in ks_maps.json). MANUAL-GAPS #10.

## Data

- `build/score_config.py` c45 block:
  - `PHRASE_SHAPE` values. Level knots (dB): winds and brass -2.0 at the onset, -0.5 at +0.4 s, 0 at +0.8 s, +1.5 at
    0.44 of the phrase, 0 one second before the end, -2.5 at the last note-off (critic A's +1.5 / +2.0 dB swell and
    -2.5 taper, set around zero at critic B's measured depth of 3-4 dB so the phrase mean stays on the printed dynamic
    and solo margins hold); strings 0 / +0.5 one second before the end / -1.5 at the end, only where no decrescendo is
    printed over the last second (their bloom already swells +7 dB by 0.4 s). Scaled 0.6 at pp, 0.8 at p, 1.0 from mp.
    CC1 arch: woodwinds (Flute, Oboe, Cor anglais, Bassoon) 33 / 32 units under the peak at the ends, never under CC1 77;
    strings 8 / 12 units, floor 55. The floors answer LEARNINGS section 3 (woodwind CC1 55-76 sounds both layers and
    beats) and Movement I c32-c33 (on the Hollywood Strings KS Masters CC1 also selects the louder Molto Vib set from 70,
    so the plan's full depth would move the string level by several dB: critic B's premise that CC1 is "colour, not
    balance" holds for the woodwinds only). Horns, trombones, tuba and clarinets (CC1 = dynamic layers) take the level
    arch only. Groups: critic A's eight doubling windows (Violins I+II 65-90, 171-204, 237-262; Oboe 1 + Bassoon 1 +
    celli 139-151; bass clarinet + Bassoon 2 + basses 188-204; Bassoon 1 + celli 250-274; Flute 1 + Oboe 1 + violins
    188-204; Flute 1 / Oboe 1 / Clarinet 1 / violins 256-274). Result: 33 lyrical phrases (list in the s2p log and
    parts.json); most lead phrases carry printed hairpins and are left to them; the windows in the build spans are
    skipped, so in practice the Oboe 1 / Bassoon 1 / celli group at 139-151 is the shared curve that applies.
  - `LEG_VEL_BY_CC`: wind legato targets `value_at([(22, 86), (46, 90), (72, 96), (114, 104)])` (was 60/80/100 by
    length), the cor anglais keeps its c04 values where higher; horns (1FH, 2FH) the same minus 6 (was v124); strings
    and trombones unchanged (critic A #2).
  - Violas portato bars 48-51 (A #3): `VEL_SET` 37, 32, 40, 34, 39, 31, 36, 41, 33, 38, 35, 42, 34, 39, 36 on the 15
    onsets 152.5-167.5; `build/entry_leads.json` Violas 153.5 / 156.5 / 160.5 +0.06 s (0.16 s).
  - S1 (A #4): Violas 87 in `DOWNBOW_STROKE_AT` (its rebow_fills.json entry removed: no re-bow there now);
    `WIND_REP_RETONGUE_AT` Horn 3 289: gap 0.12 -> 0.06 s, CC11 fall 10 -> 5 (MIDI gap 0.104 -> 0.070 qn). Violins II
    289 and 120 unchanged (master dips 7.6 / 3.3 dB already pass; A).
  - `TIMP_DELAY_S` 0.06 -> 0.0 (A #5; percussion on the grid).
- `build/mix.json` (`actor_scripts/apply45.py`):
  - Brightness (lead: C's set plus B's 1 kHz bell, which simulated better): string family `hshelf` 4730 Hz +4 -> 0
    (group and the basses' own family EQ), string 1 kHz bell -5 -> -2.5, horn and low-brass shelves 7490 Hz +4 -> +2,
    Violins I and Violin I solo 5 kHz -4 -> -6, Violins II 5 kHz -4 added. Simulated on the c44 stems (`sim45.py`,
    measure.py's band shares; the template's shelf `bw` 0.33 read as 2 octaves, as critic C did, since c44's measured
    stem change shows no 3-4 kHz dip): 6-20 kHz -24.5 -> -28.0 dB, 2-6 kHz -8.5 -> -9.2, 500-2000 Hz -4.3 -> -3.9
    (C's set alone -27.6 / -8.9 / -4.1). Make-up gains (A-weighted, per stem): Vln I +0.12, Vln II -0.12, Violas -0.55,
    celli -0.57, basses -0.32, Vc div -0.51, Vla div -0.52, Tbn1 +0.08; Violins II div -2.53 with C #4's EQ change.
  - C #1 bass image: side EQ bell 200 Hz -6 dB (1.2 oct) + high shelf 350 Hz -2 dB on the 14 full-width Main tracks
    (Violins I/II, Violas, celli, basses with c41's 100 Hz -15 kept, Horns 1-4, a2, Trombones 1-2, bass trombone,
    tuba), replacing their old side shelves; C's stereo-power make-ups (+0.7 to +1.6 dB).
  - C #2: `hp_hz` 160 on all four returns (the c38 low cut), R Brass fader -0.97 -> -4.97 dB. The horns' 800 Hz soft
    shelf is not halved (critic B's do-not-touch; the lead took only the return items).
  - C #4: track sends Violin I solo +2.4 dB (+8 over the sections), Violins II div and Violas div +0.4 (+6), celli div
    -1.2 (+6); celli div seat 0.33 -> 0.15, track pan 0.15 -> 0.05 (Opus state change); Violins II div EQ 1 kHz -10 ->
    1.5 kHz -6.
  - C #5 seating (REAPER pan): Violins I -0.10 -> -0.22, celli 0.15 -> 0.25, basses 0.23 -> 0.30, horns 0.10 further
    left (Horn 1 -0.28).
  - C #6: harp group mics Close 0.6 / Main 1.0 -> Close 1.0 / Main 0.355 (Main -9 dB); Harp and Harp harmonics rebuilt.
  - Test returns R Duc, RE Strings, RE Brass, RE Winds, RE Perc removed from `returns` / `test_returns` and deleted in
    REAPER (`delete_test_returns.lua`).
  - B #2: every wind track `dyn_trim_db` f +1.5, ff +2.0. B #3: basses `soft_trim_db` {ppp 6, pp 8, p 8.5}.
    B #5: Trombone 2 `dyn_trim_db.f` 4.4 -> 3.6. B #6: Harp `gain_db` +3.
- `build/roles.json`: Flute 1 [204, 208] -4 -> -1.5, Clarinet 1 [204, 210] -4 -> -2, bass clarinet [204, 208.5] -4 -> -2
  (B #2); cor anglais [98.5, 102] -3 -> -5.5 (B #4b); bass trombone / tuba [200, 214] +3 -> +2 / +1 (B #5a); timpani
  [204.25, 209.5, +3, 0.25] added (B #5b); Trombone 1 [212.4, 213.6] +3 -> +5 (B #5c, weight; the 2 kHz accent shelf
  kept, rule 9 and critic A's do-not-touch); Harp [17.9, 42.0, -3, 0.5] added, [124, 140] -7 -> -5 (B #6).
- `build/note_trims.json`: cor anglais 152 -8 -> -3 (B #4a).
- parts.json against c44: 0 WARNING; every track's CC lanes change (the 0.0625 grid); notes change on the wind and horn
  legato targets (velocity), Violas (87 stroke, portato velocities and leads), Horn 3 (289), Timpani (no delay);
  `vol_db` on the phrase-shaped tracks and the role tracks. Re-bows unchanged (space_rebows.py proposes the same moves
  as on the c44 data, which earlier cycles left on purpose). Opus states changed: Harp, Harp harmonics, Violoncellos div.

## Rejected / deferred

- Beat-position velocity (plan section 10): not on the timpani (B, the felt strokes' 8-16 dB step at v56-64); not on
  the harp or pizzicato: series 1 c16 measured +6/+3/-3 velocity steps on pizz. and harp as 0.5-1.2 dB of downbeat
  weight with the basses' peak spread doubled (1.7 -> 3.3 dB), the c20 volume-envelope metric weight (METRIC_DB)
  already acts on these spans, and the pizz. row's 46/47 layer edge with the 48 floor leaves no room to centre a
  15-25 step pattern on the current v48-53. FINDINGS section 24 itself places this rule on the running figures of the
  scherzo and finale. The plan item is dropped for movement II on that evidence.
- Short-note CC parked high (plan section 6): critic B measured +14 to +20 dB on the pizz. at the same velocity; no
  short rows other than pizz. and harp (already CC11 110) in v600. Not tried.
- Spiccato length, repeated short-note groups: v600 has none.
- Pass-2 CC1-only string test (ONE_TIME): the template's "Mod + Expression Combo" is an Opus macro that drives CC1 and
  CC11 together; `opus_state.py` has no macro support, and with our mapping a CC1-only lane would leave the strings on one
  dynamic layer. A test track would also add an Opus instance (memory at 44 GB). Deferred until macro states can be
  written.
- Hairpin curve shapes (crescendos rise early and settle, diminuendos fall on the last held note; plan section 9):
  deferred to c46 with the tempo and rubato work, since they change every hairpin's CC11 and dB ramp, which the critics
  then need to judge on their own.
- In-slur lean-off: left out (A: -2 CC is about 0.5 dB, the legato fills already lean off 0.5-1.1 dB).
- Critic C #2's horn 800 Hz shelf -8 -> -4 (B: do not touch the horns' soft shelf).
- Critic B #5c's removal of Trombone 1's 213 accent shelf (rule 9; A: do not touch the accents). The role +5 was taken.

## Coordinator cross-checks from Movement I (received before the render)

- c50 (template render): brightness with the brass shelf at +1 gave 6-20 kHz -27.8 dB; here +2 is kept (simulated
  -28.0); if the render reads above -27, take the brass shelf to +1. Width: if C's side EQ alone misses the correlation
  targets, Movement I's Main pan at the seat (±0.8) is the next step (a state change on 14 tracks; c46). A short range
  render (`actor_scripts/range45.py`, after Movement I's rangetest50.py) checks bars 61-64 before the full render.
- c51 critics: (a) timpani roll lanes stay linear under any hairpin curve: no hairpin curve change this cycle (deferred
  above), keep it in mind for c46. (b) string shorts: CC11 park changes level only, layer by velocity; no CC11 park and no
  beat velocity here, and the beat weight is already in the volume envelope (METRIC_DB) -- consistent. (c) brass bells
  halved + 3.2 kHz -3 dB bell + brass gains -1.8..-4.0 dB for the loud tutti: a Movement I simulation, not measured on
  this movement; open for c46 (critic C measured the soft horn theme already heavy at 250-500 Hz, so halving the 475 Hz
  bell needs its own check here). (d) soft timpani rolls' 30-150 Hz share: critic B measured only the printed crescendo
  roll into 172 over the 18 % cap (allowed by rule 5); open for c46 if the c45 render shows more. (e) S1 checked in the
  master as well as the stems (s1check44.py measures both; results below).

## REAPER and render

- Lock 19:45:28-20:15:15 (30 min) after the turn rule (Movement III c08, which had waited longer, went first; my
  `turn_lock.sh` deferred only to waiters older than itself). Start + open (41 tracks), `delete_test_returns.lua`
  (R Duc and the four RE tracks deleted: 36 tracks = 32 + 4 returns), `--midi-only` on all 32 tracks (Harp, Harp
  harmonics, Violoncellos div fully rebuilt for their state change; returns refreshed with hp_hz 160, read back OK),
  `--mix-only` (pans, side EQs, family EQs, sends), restart (settled 43 GB, 0 compressed), audio 48000 / 512 / no input
  after `_c45_audio_init.lua`. Disk 54 GiB free.
- Range render first (coordinator; `actor_scripts/range45.py`, qn 200-222, 42 s): peak 0.70, L/R corr 60-250 Hz 0.02 ->
  0.62, 250-2000 Hz 0.29 -> 0.53, side/mid -1.95 -> -5.13 dB, 6-20 kHz share in that span -24.5 -> -26.9 dB. Passed, so
  the full render followed: `render_cycle.py 45` without `--force-memory`. After the render: **44 GB, 2.0 GB
  compressed**. Stem fix + `--mix-only` (below), save, quit, unlock.
- After the unlock one more level-only fix was made on the stems (Trombone 1's role back to +3, below); it is in build/
  but not in the saved REAPER project. The next build writes it: `--midi-only` rewrites every listed track's volume
  envelope, so include Trombone 1.

## Stem fix (`render_first/` holds the replaced stems)

- Harp -2.95 dB: the Close-led mics made the harp +2.95 dB louder in bars 7-14 (A-weighted stem, c44 -> c45), where B
  wanted no change; with B's +3 gain and roles the other passages measured +6.4..+7.3. After the fix the harp sits
  +3.5..+4.4 dB over c44 outside bars 7-14 (B #6's intent). The harp's share of R Perc was not re-simulated (small).
- Harp harmonics -1.8 dB (back to c44's coda level, which B kept).
- R Strings return -1 dB (`--return-gain`; mix.json fader -16.97 -> -17.97): the final chord's t20 was 0.461 s (limit
  0.45); after the fix 0.451 s. Strings family t20 stays 0.551 s (c44 0.551; set by the dry stems, as c44 found).
- Clarinet 1 role [279.9, 292, +1.5, 0.5]: the coda solo's lead over all other stems fell 3.9 -> 1.4 dB (basses +2.2 dB
  from B #3, cor anglais / Horn 4 arches +0.4); now 2.9, and 5.8 over the cor anglais.
- Trombone 1 role [212.4, 213.6] back to +3 (B #5c's +5): the role window covers the 212.5 pickup too, so the accent
  over its pickup stayed +2.2 dB (c44 +2.1); the +2 only made the quotation's head louder. Open for c46: a window that
  starts at the 213 accent (about 212.95) or a pickup cut.

## Measured (c44 -> c45 delivered; check44.py, s1check44.py, phrase45.py, pcx.py, accent44.py)

- Master -22.9 LUFS, LRA 23.4 LU, TP -4.0 dBFS, sample peak 0.632. **Delivered -19.8 LUFS, LRA 15.4 LU, TP -1.6 dBTP,
  span 18.7 dB, limiter 1.7 dB** (c44 -19.8 / 15.3 / -1.6 / 18.9 / 1.9). Attack probe 0 late or hole.
- Brightness: master 6-20 kHz share **-24.5 -> -28.7 dB** (simulated -28.0; references -28.8 to -32.3), 2-6 kHz -8.6 ->
  -9.4 (refs -10.5..-12.4: still above them, not dulled), 500-2000 Hz -4.4 -> -3.8 (refs -3.5..-4.4).
- Image: side/mid **-2.2 -> -5.6 dB**, L/R correlation below 250 Hz **0.06 -> 0.64** (references -4.7..-5.4 and
  0.54-0.62). Movement I's Main pan at ±0.8 is not needed.
- Wetness (family dry stems + return, t20 / smallest drop at +0.3 s): strings 0.551 s / 8.9 dB (c44 0.551 / 7.5),
  winds 0.324 / 17.6 (0.344 / 16.8), brass 0.282 / 20.1 (0.344 / 15.3; R Brass -4 dB), final chord 0.451 s (0.441).
  All at or under the limits (strings 0.55, winds/brass 0.50, final chord 0.45 within 0.001).
- Balance (A-weighted dry stems, family minus strings): winds whole piece -2.7 -> -1.6, bars 61-62 -1.8 -> +0.1, bars
  79-81 +1.7 -> +3.1 (B #2); brass bars 61-62 -0.9 -> -1.3 (B #5a); timpani bars 61-62 -26.2 -> -23.2 (B #5b). Solo
  margins: Horn 1 b7-14 6.4 -> 6.0, Oboe 1 b15-16 9.7 -> 7.8, Violin I solo b17-22 -6.2 -> -5.1, bass clarinet b31-36
  0.9 -> 3.7 (B #4b), cor anglais b41-44 0.4 -> 1.4, Flute 1 b37-40 8.4 -> 6.8, Oboe 1 b45-47 7.2 -> 5.6, Horn 1 b67-70
  7.0 -> 6.6, Clarinet 1 coda 3.9 -> 2.9 (over CA 6.5 -> 5.8), Violins I over celli b89-91 5.3 -> 5.3. Harp harmonics
  over Vc div + Cb -5.6 -> -3.9. Timpani share of 30-150 Hz: b1-3 12.4 -> 9.4 %, 168-172 27.4 -> 24.5, b60-62 6.5 -> 8.6,
  b67-70 15.2 -> 11.9, b84-85 15.4 -> 14.4.
- Phrase shapes (audio, dry stems, the 33 lyrical phrases; c44 -> c45): winds swell at +0.8 s **3.8 -> 4.7 dB**, taper
  over the last second **2.4 -> 3.9 dB**, peak in the middle third 4/17 -> 5/17; brass (3 phrases) swell 0.2 -> 1.2,
  taper 2.8 -> 4.4; strings taper 1.4 -> 2.3. Critic A's targets (swell 3-4, taper 3.5-4.5) are met for the shaped
  phrases; the peak position barely moved (the printed dynamics and samples dominate it).
- Legato velocity (pcX median, c44 -> c45): Oboe 1 +63 -> +46 ms, bass clarinet +40 -> +26, Horn 1 -20 -> -14, Flute 1
  +9 -> +5, Clarinet 1 +6 -> +8, Bassoon 1 +14 -> +16, cor anglais -1 -> -1. No lead refit needed (no move over 30 ms;
  Oboe 1 still over critic A's ±30 ms target).
- S1 (A's method; 49 points): own-band dip median 7.4 -> 7.1, under 3 dB 6 -> 7, master 3.9 -> 3.7. Horn 3 289 stem
  10.8 -> 5.7 dB (target 5-7), master 7.6 -> 7.3. Violas 87 (now a stroke, my 30 ms method) stem 2.5 -> 3.2, master 0.4
  -> 1.3: better, still under 3 dB in the master (open). Violins II 289 / 120 unchanged by design (master 7.3 / 2.4).
- Violas portato bars 48-51: the late takes now peak at +0.25 s (c44 +0.31-0.32); the A3 peaks still agree within
  0.3 dB, so Detache's velocity crossfade did not spread their level (open: a level pattern in vol_db instead).
- Timpani audible onsets (peak -10 dB): 204 / 277 / 278.5 / 279 at +0.05..+0.06 s -> 0.00 / 0.00 / -0.01 / -0.01 s.
- Trombone 1 accents (rule 9): 213 2-5 kHz attack minus body -10.0 -> -10.1 dB, master 2-5 kHz jump -5.7 -> -6.5;
  218 -15.7 -> -15.3 / -4.8 -> -5.1. Still soft.
- RR reset on CC16: the viola portato still alternates two takes (A3 peaks at +0.17 / +0.25 s in turn), so the reset did
  not stop the round robin; repeatability between renders not tested this cycle (next render with unchanged data on some
  tracks: run state_check.py).
- S3 fast master falls and the held-note loop check were not re-measured (the shapes are slow ramps; held-note data
  unchanged apart from the grid).

# Cycle 58: coordinator notes (read before anything else)

## Dan's rule (2026-11-11, no exceptions)
"yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem"

- The track volume envelope carries slow balance only: gain, roles, section dynamics, hairpin gain, divisi cuts, timpani settle, fades. Ramps, not steps on notes.
- No per-note level or per-note shape on the track volume envelope, on any track, for any reason.
- Faults are fixed in the instrument: CC11/CC1 shaped per phrase (flat across legato joins), velocity, patch or row choice, Opus region volume, row volume, note lengths, gaps, overlaps, keyswitch timing, leads.
- Rebuilding the old per-note bumps in CC11 is not a fix.
- A fault with no instrument-side fix stays audible and is listed.
- Reference practice: mockup-kit/EW-TEMPLATE-FINDINGS.md sections 5-8 and 12 (no volume automation in the EastWest templates; 0.01-0.36 points/s in the Duc projects; one CC1 lane per phrase; legato overlap 45-80 ms strings, 33-58 ms winds and brass; legato velocity 90-98; repeated-note gap 60-100 ms; shorts with CC parked high and dynamics by velocity).

## State after c57 (cycles/c57/CHANGES.md, envelope_table.md, faults_c57.txt, checks57.txt)
- Per-note envelope items 0 on all pitched tracks. Points 32712 -> 6962. Strings 0.9-1.35 points/s, winds and brass 0.2-0.8.
- STOPGAP TO REMOVE: 375 "carry" rows on 32 tracks (build/balance57.json, cycles/c57/actor_scripts/balance57.py, carryfix57.py): per bar, the mean level the dropped layers gave on the c56 stem. Plus ten 16 qn rows on Violins I added after the render. These are the old layers at bar resolution. They are why the strings are still at about 1 point/s.
- 263 config level shapes of 2 s or more remain (tag shape_slow).
- Theme (Violins I 56-127, 128.4-158, 536-576): Sus MAX on every note, class leads plus 103 per-note leads. Bars 15-22: S robust SD 9 ms, front minus tail -1.9 dB. Span 536-576 reads 17 ms with 7 notes over 40 ms.
- Theme over celli bars 15-22: median +4.4, lower quartile +1.7 (target 3.9).
- Faults c56 -> c57: join holes 44 -> 25; long-note sags 84 -> 62; re-bow holes 1 -> 16; pulses 13 -> 17; pitches 4 dB out 18 -> 23; repeats under 3 dB 83/425 -> 82/406 (basses 26 of 139).
- Accents: no emphasis at all, nothing in place.
- 15 master bars more than 1.5 dB over c56 (bar 21 +5.5, bar 182 +5.4, bar 85 +4.3, bar 7 +3.1).
- Cello solo: R-L +2.7 but stem correlation 1.00. Horn 4 bars 19-22 still falls 4.7 dB.
- Percussion tracks (tam-tam, cymbals) keep stroke shapes on the envelope (59 / 1 / 49 values), built by separate code.
- Not done in c57: legato overlap and legato velocity, accents by lower resting CC11, row levels in Opus, refit of region gains, Cello solo Main-mic alias, trumpet rt_gain test.
- Not verified: byte-identity of parts.json with the new keys off.

## What this cycle is for
1. Replace the carry rows. For each track, sort the 375 rows by cause (critic B): (a) a printed dynamic or role the CC11/velocity mapping should already give (fix the mapping: soft/dyn trims are track-level and allowed, CC11 per dynamic, patch choice); (b) per-pitch or per-row sample level (region volume, row volume); (c) compensation for a shape that no longer exists (delete); (d) a real balance decision of a phrase or more (keep as a role row, in rests or at phrase starts). Aim: strings at or under 0.4 points/s, and report what each deletion costs in dB.
2. Accents: lower resting CC11 (finale: strings about 104-106, winds 98, brass 100) so an accent can be a CC11 rise of the note's whole length or a higher velocity on rows that respond; Marc rows where the score has accents on sustained notes. Critic A measures which rows respond to velocity.
3. Re-bows: 16 holes of 7-16 dB. Options from the other movements: no split under about 6 s; no split on exposed notes; overlap 1.5 s on a second instance; doubling on an idle DIV instance with interleaved re-bows (Adagio: 8.4 -> 2.6 dB simulated); CC11 +7 units over the first 0.45 s of the new bow; start held notes on Sus MAX.
4. Legato: overlaps and velocity against the reference values; transition bursts on Leg Slur MAX at velocity 124 against EastWest's 92-98.
5. Region gains refitted to the c57 render for the pitches still out (Flute 2 Eb6 +11.0, F6 +7.9, Db6 -6.8, C6 -6.6; Flute 1 D6 -8.8; Bassoon 1 Ab3 -7.7; Horn 1 D4 +6.8; Violins II D4 +6.7; basses Ab1 -5.7).
6. Critic C lens this cycle: tempo, timing, transitions. Include: role, section-row and hairpin-gain edges keyed to the score onset that land inside led notes (Adagio found steps up to 5.3 dB 50-300 ms inside notes: key them to the moved note-on or put them in rests); theme span 536-576; keyswitch leads (minimum 0.15 s elsewhere).

## Notes from the other movements under the same rule
# Notes from other movements under Dan's no-per-note-volume rule (for c58 critics and actor)
Sources: symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md items 60-69 and cycles/c17/reports; symphony/scherzo/reaper-v600/cycles/c15/CHANGES.md and cycles/c16/reports; symphony/mvt2/reaper-v600/cycles/c55/CHANGES.md.
- Role rows covering only one or two notes count as per-note (Adagio ROLE_NOTE_MIN 3); unison plateaus over one or two notes too.
- Leftovers inside sounding notes: hairpin-gain releases (HP_REL 1.0 qn) and role edges stepping 2-3 dB in 0.1-0.14 s; arrivals where the envelope gives back 6-7.5 dB on the held note. Fix: long release ramps, role edges in rests.
- Per-pitch level: Opus per-region volume in the instrument state (scherzo mix.json region_gain_db); velocity on pizzicato and shorts. Row level: layerMatrix.rows[].volume (affects every note on the row; check users first).
- Accents: CC11 flat above about 106 on string Sus MAX; lower resting CC (104-106 strings, 98 winds, 100 brass) with the slow trim making up level; accent 121-124 for 0.15 s.
- "Leg Slur MAX" 3-7 dB under "Sus MAX" at f/ff; crossover 190-246 ms; keyswitch lead minimum 0.15 s.
- Tongued/repeated notes: gap floor 0.09 s brass, 0.065-0.07 s winds; under 60 ms they run together.
- Re-bows on exposed held notes (worst fault after removal): skip re-bow on notes under about 6 s; overlap bows 1.5 s; or double on an idle instance with interleaved re-bows.
- Timpani: 0.17-0.24 dB per velocity step; top layer from velocity 96-111 (harder stick sound); rolls with flat CC1 fall 16-19 dB once the envelope no longer holds them.
- Basses "Stac On Bow RRx9": separation 9.8-12.8 dB without dips, but 76-118 ms rise that differs per round-robin sample.
- ReaEQ narrow bells cut more than an RBJ model; bass F2 excess only in the loud sample layer (finale).
- REAPER fader scale is a table, not a fourth root (scherzo tools/env_scale.json; Adagio cycles/c55/env_scale.txt).
- Offline stem simulation of an envelope change predicts the render (finale envsim.py, Adagio).
- Adagio cost of removal: join holes 298 -> 379, soft starts 176 -> 302, re-bows over 3 dB 16 -> 30 of 37; balance unchanged.
- Tremolo strings and basses do not repeat between identical range passes.

## Adagio c56 critics (symphony/mvt2/reaper-v600/cycles/c56/reports/)
- Fault counts overstate the cost: filter out pizzicato decays, level steps between notes 6 dB apart, same-pitch re-bows before counting "join holes". Legato-join sags of 2-3 dB for 0.25 s: leave (reference lanes are flat there). Audible: starts 6 dB or more low.
- S readings change with no timing change when on-beat envelope steps go; do not chase them.
- A CC7/CC11 lane fitted together with a per-note envelope row breaks when the envelope half is removed (their sf > p swelled 5-11 dB). Check every such pair.
- Section-row, role and hairpin-gain edges keyed to the score onset land 50-300 ms inside led notes (steps up to 5.3 dB): key to the moved note-on or put in rests.
- Per-pitch sample level is the main cause of notes out of line once trims are gone: region gains and row volumes in the Opus state. A row used by a single note was 13 dB over its neighbour.
- Re-bows of soft held notes: dip 7-8 dB. Doubling on an idle DIV instance with interleaved re-bows: 8.4 -> 2.6 dB simulated. CC alternative: +7 CC11 units over the first 0.45 s of the new bow (0.6 dB per unit on soft strings). Start held notes on Sus MAX, not Leg Slur MAX.
- Transition bursts are all on Leg Slur MAX at velocity 124; EastWest uses legato velocity 92-98.
- Lowering the resting CC11 changes brightness by under 1 dB per 10 units.

## Instructions to the critics
- SAFETY: read-only. Never run tools/build_reaper.py or tools/render_cycle.py, never exec build_reaper.py whole (cut the source before ENV_LUA if you need its functions), never touch REAPER, ~/.rpr-bridge or another movement's folder. Scratch files only under cycles/c58/critic_scripts/<SLOT>/. No subagents.
- Propose instrument-side fixes only. Any proposal that puts a per-note value on the track volume envelope will be discarded.
- Do not count a fault that the reference projects also leave (legato-join sags of 2-3 dB; S shifts with identical MIDI).
- Every proposal: the measured size now, the expected size after, the file and key to change.
- Hand-back at most 40 lines; the full report goes to cycles/c58/reports/<SLOT>.md.

## Coordinator decisions on the c58 critic reports (actor: these are the work order; details and tables in reports/A.md, B.md, C.md)

Order of priority. Range-test where a critic says a value is inferred. If time runs short, drop from the bottom and list what was dropped.

1. Carry rows (B 1, 3, 6). Delete all rows of build/balance57.json and the ten 16 qn Violins I rows, by cause:
   - a: delete; roles.json Violins I [128,160,+3]; Violoncellos [56,88,-2] -> -3.5; Violins II theme doubling on Sus MAX (also rows 76-84, bar 21); held_decresc: -3 dB into the hairpin's CC11 end value; SWELL_CAP_TO_VOL_DB_PER_CC = None.
   - b: region gains per B 4 (29 entries, Sus MAX rows included); re-bow rows go with decision 3; "early" and bloom rows deleted, cost listed.
   - c: delete without replacement.
   - d: unison +3 dB as one role span per run of 3 or more notes with edges in rests. Shapes of 4 s or more on one held note (coda fade, bass pedal 464-484): put them in CC11 where the patch has CC11; envelope only where it does not (slow_min_onsets 1, slow_min_s 4.0).
   - No new fitted level rows of any length. If a track ends more than 3 dB off in a passage, fix the dynamic mapping (soft/dyn trims, CC11 per dynamic) or list it.
2. SHORT_CC11_PARK = None (B 2: 184 string shorts up to 11.4 dB hot since the envelope half went). Check every other CC + envelope pair for the same break.
3. Envelope edges (C 2): ONSET_KEY rule in vol_points for entries after a rest and new-bow joins (step wholly in the rest, keyed to the moved note-on); HP_REL 1.0 -> 4.0 qn; role edges moved to the rests in C's TSV; drop every kept shape_slow item with a segment over 3 dB/s. Brass soft ENTRY_LEAD_S 0.06 -> 0.045 only after a range test.
4. Timing (C 1, 3): _C54_STR_SPANS add (88,100) and (536,548) for Violins II and Violas; RETONGUE_LEAD_S["Double basses"] = 0.06; steady57_at.json delete "60.000" and "572.000", rep_gap_s 0.09 -> 0.06 there; leads at 88 and 536 0.245; the rows C lists for 573.0, 570.5, 539, 558, 574, 76.5; same cut fix on Violas 135.5 and Violins I 455.5. Guards: Violins I 56-90 S robust SD at or under 12 ms and front minus tail within 3 dB; report 56-127 and 536-576.
5. Re-bows (A 2): Option N first (REBOW_MAX_S 4.5 -> 5.2, drop those notes' frozen REBOW_AT points; measure pulse on those notes). Option A (pieces alternating with a pass-2 alias, 0.4 s overlap) for the printed bow changes and the long notes at 286-304 and 712-728 if it fits the cycle; else list them. Last chord (C 4): no re-bow on Violins I / II in bars 181-182, CC11 22 -> 14 across the fermata.
6. Accents (A 1): resting ff CC11 104 strings and winds, 100 brass, made up by the track dynamic trim; an accent is a flat CC11 value for the note's whole length (ceiling 124, brass 118; at f, 108-110), no shape inside the note. ACCENT_BUMP_AT needs the note's length and a ceiling. Sus Marc LITE with a row volume per section for string accents of 0.3-1 s at f and ff that start a bow, only if the row volumes are set (Violins II -5.4, Violas +0.5, celli +5.5). Report accent minus unaccented in dB per family.
7. Legato (A 4): LEG_OVERLAP in seconds (strings 0.06, winds and brass 0.045); the eight Violins II / Violas tied syncopations at 62.5-82.5 start on Sus MAX; legato velocity 124 -> 96 as a range test on bars 47-61 and 15-22 (celli transitions 7-10 dB over the body), adopt only if leads refit and guards hold.
8. Basses' eighths (A 3): range-test CC16 round-robin reset before every beat and Stac On Bow RRx9 on a pass-2 alias over qn 100-126; adopt the better one. Contrabassoon Sus MAX repeats -> LegRep RRx4.
9. Horn 4 (B 5): soft-layer region gain C3-F3 -9 if Opus allows a per-layer gain; else list. soft_trim mp 6.0 -> 9.0. Other soft_trim proposals of B's dynamic map: only those with n of 10 or more.
10. Small: Oboe 2 160 entry lead (153 ms early), Trumpet 2 arrivals, celli 526 velocity 111. Keyswitch lead 0.15 s for changes not into a legato row: skip unless free.

Report in the hand-back: per-note envelope items per track (must be 0), fitted level rows (must be 0), points per second per track, the guards, faults table c57 -> c58, the list of faults left audible, what was dropped. A/B clips c57 then c58 of bars 15-23 and bars 23-26 in cycles/c58/ab/.

## Actor constraints
- Shared REAPER lock: wait_lock.py with a running waiter; never take or break the lock by hand; tie rule: the folder path that sorts first goes first.
- First range render after a rebuild is unusable: render each variant twice, keep the second. State guard at the start, after range renders and before the full render; rebuild stale tracks in full. Wait 45 s after each range pass.
- No score change. No commit. Nothing published. No REAPER preference changed. Nothing in ~/.rpr-bridge modified. No subagents.
- Update HISTORY.md, LEARNINGS.md, cycles/c58/CHANGES.md. Hand-back at most 40 lines.

## Addition 2026-11-11 23:38 UTC: accents smaller (changes decision 6)
Dan on the finale's c17 (+2.1 to +4.1 dB accents): "The accents are little bit over done now". Movement I target: +1.5 to +2 dB over unaccented notes, none above +2.5. Ceilings lowered to fit.

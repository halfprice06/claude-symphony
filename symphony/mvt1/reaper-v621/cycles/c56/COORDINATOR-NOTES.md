# Coordinator notes for cycle 56 (read first)

## Dan's standing complaints, in order
1. (2026-11-11) The track volume envelope has large peaks and valleys on individual notes, also on fast notes; it looks unnatural to him. See "PRIORITY for c56" below: this is the first concern of this cycle for critics and actor.
2. (2026-11-10) The string theme at rehearsal A (bars 15-23) felt choppy and not in steady time. c54 fixed timing, c55 fixed the sag on long notes. Do not lose either: Violins I 56-90 S robust SD 9 ms (2 over 40), long notes front minus tail 0.6 dB median (coordinator check, 13 notes of 1.4 qn or more).
3. Earlier: articulations, per-track balance and blend, timpani rolls must not cover other parts, "mushy" low-mids.

## c55 facts (cycles/c55/CHANGES.md has the full record)
- Delivery -19.8 LUFS, LRA 14.4, TP -1.7 dBTP, 433.45 s.
- Theme over celli 56-88 lower quartile +4.95 dB; bar 138 Violins I within 0.3 dB of Violins II.
- Open: celli 520-536 S robust SD 24 (5 over 40); melody over celli at quarter 159 +2.8 (target 4); Horn 1 415; lyrical lines (celli 184-270, violas/celli 584-636, Violins I 636-664) untreated, range test found no good variant; one-row treatment of bars 113-120 and the development left out (hairpins); bow-change hole on long theme notes about 8 dB against the lifted body; winds row-lead/pitch-pair table; delivery rise delay; three stem-fix rows (celli 159, celli 526, cor anglais 24) in build/ but not in REAPER; 61 fixed-quarter level breakpoints near moved wind note-ons unchecked; re-bow pieces Violins II 188, 208 not refitted.
- Not measured on c55: tutti-entry rows, Violas 438, bars 131-134 per-onset spread, tutti-stop decays, basses' final chord.

## Critic instructions for this cycle
- Critic A (articulation): besides your lens, judge by ear-proxy measurements whether per-note envelope movement is audible as pumping or unevenness in: Violins I 56-90, celli 184-244, Oboe 1 88-104, Clarinet 1 520-536, Horn 1. Name the envelope layers responsible where you can (parts.json track keys such as accent_db, acc_fitted, accent_body, notches, early_fills, loop_fills, rebows, pitch_trimmed, cresc_fronts, phrase_shapes).
- Critic B (balance): measure Movement I's 56-112 Hz and 140-355 Hz shares against a Brahms reference if one is on disk (see symphony/mvt2/reaper-v600/cycles/c54/reports/B.md for the method and reference paths); simulate on the stems what removing the Double basses / tuba / celli note-cut EQ bells does before recommending a mix.json change.
- Critic C (dynamics over time): include a count of crescendos that do not rise on their own stem (scherzo found 40 of 215, caused by soft_trim_db / dyn_trim_db in vol_points) and winds against strings in crescendos into f.

## Actor constraints
- Shared REAPER lock: use wait_lock.py with a running waiter process; never take the lock by hand; if two waiters started in the same second, restart yours a few seconds later.
- First range render after a rebuild is unusable: render each variant twice, discard the first. State guard before the full render. Wait 45 s after each range pass.
- No score change. No commit. Nothing published. No REAPER preference changed.

## Notes collected from the other movements
# For the c56 actor: finale c14 techniques 46-52 (symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md; scripts in symphony/mvt3/reaper-v600/cycles/c14/actor_scripts/)
- 46 Repeatable takes: CC16 127 in every track's pre-roll plus a CC16 before the first note of each section on every pitched track (RR_RESET_ALL_AT; restate the keyswitch when the reset lies in a rest). Finale: 2036 of 2123 long/pizzicato notes equal within 0.5 dB between two range renders. Candidate for Movement I as a whole-movement rule; it changes every sample choice, so fills and trims fitted on the old takes need a refit pass (do it in one cycle with a full check).
- 47 After resets the only non-repeatable notes are row-change legato joins (42 of 300). Confirms one row per line.
- 48 With a reset before each section a range render matches the full render within 0.5 dB on 991 of 1030 notes: range renders become a valid fitting base. pluckfit.py for pizzicato trims (basses 184-216, 584-616).
- 49 A slurred string note after a Sus MAX eighth played as a Sus MAX stroke 0.06 s early: S +85..+144 → -38..+26 ms. Not for soft entries.
- 50 Long diminuendos: HP_CURVE keys decresc_last_max_qn 6, decresc_last_min_s 0.35.
- 51 Delivery ride hold after a diminuendo (ridefit.py).
- 52 After a restart gate the render on REAPER's memory footprint of the previous cycle, not on quiet readings.

# Movement II c52-c53 findings to check in Movement I (c56 critics and actor)
- After moving string lines to one row, a printed new bow starts like the middle of a slur: long notes 3.4-7.4 dB softer over the first half second. S does not show it. Fix: a start shape per note, level only. (Movement I has the opposite fault on the Marc row: check both directions after c55.)
- Join notches/fills keyed in absolute qn do not follow lead changes; key them in seconds from the note-on. Level rows on a legato target start after the transition.
- fit_rebows.py refits made fills worse on stems that already carry fills; fit residual corrections.
- Low-mid weight: Movement II master +3.2-3.7 dB at 140-355 Hz against Brahms slow movements, -5 to -7 dB at 70-110 Hz; celli supply 51-75 % of that band in string themes. Check Movement I against Dan's "mushy" note (blend-and-space lens, c57).
- Divisi tracks there are mono with no room at the wide section's level; check "Violins I f62", "Violins II f62", "Cello solo" and any divisi path here.
- Delivery rise delay 0.6 s ported there: 0.8-0.9 dB lower after loud stops, loudness unchanged.
- REAPER deadlocked in a MIDI job 35 s after a range pass: wait longer after a render.

# Scherzo c13 findings (2026-11-10)
- First range render after a rebuild is unusable even 50 s later (joins up to 400 ms off): render each variant 2-3 times, discard the first.
- Range renders leave tracks stale: state guard before the full render.
- Two slurred eighths of a theme head on the following half note's sustain row (Sus Marc LITE) with level steps: second eighth sounds 164 ms instead of 0-44 ms, reproducible; Slur Runs late, weak, non-repeatable.
- Removing 22 unprinted BEAT_STRETCH beats: no side effect.
- Positive leg_leads rows do nothing where the lead cap or the 100 ms gap binds.
- Keyswitch 0.15 s early alone: no gain on celli trio tune; one legato row needs the full lead refit (joins 120-260 ms early without it).
- Always keep a waiter process running while waiting for the lock. Two waiters started in the same second deadlock (each lists the other as ahead): start a few seconds apart.

# Scherzo c14 critic findings (2026-11-10), check in Movement I c56
- DYNAMICS LENS (c56 critic C): soft_trim_db / dyn_trim_db (build_reaper.py vol_points, from the printed dynamic curve) take back single-instrument crescendos: in the scherzo 40 of 215 crescendos do not rise on their own stem; winds fall 4-7 dB against strings in crescendos into f. Measure the same in Movement I. Proposed generic CRESC_TRIM_HOLD (counterpart of SOFT_DECRESC_HOLD).
- "Mushy": low-mid excess +3-6 dB at 140-355 Hz in soft passages only, 70-112 Hz 5-7 dB short. Movement I's note-cut EQ bells (Double basses 87.3, 61.7, 73.4 Hz; tuba 84 Hz; celli) sum to -9..-10 dB on some notes. Check in Movement I whether these bells cost the 70-112 Hz band on its own tonic/dominant (C minor: C2 65.4, G1 49, G2 98).
- Sus Marc LITE for slurred pair + half note: half note decays 11-16 dB over its second beat; note after it 4-14 dB over. Needs a held tail and landing-note steps. (Same fault as Movement I c54.)
- Row-change joins moved about 100 ms between identical renders in 10 of 138 against 4 of 340 same-row joins.
- Soft-end check: time from the note-off on the dry stem.
- Post-render stale state has no audible effect on the render itself.

# Adagio c53 results (2026-11-10)
- JOIN_NOTCH_S (seconds from the moved note-on) in symphony/mvt2/reaper-v600/tools/score_to_parts.py: join peaks over 5 dB 21 -> 3 of 460.
- Level shapes move S: a lift after the attack reads 34-135 ms late; start shapes begin on the note-on.
- leg_leads.json row = offset added to the row lead, then clamped.
- Retimed joins can still move 25-30 ms between range pass and full render.
- Divisi on the section's Close + Main patch: width (corr 1.00 -> 0.51) but per-note level +1..+12 dB; needs per-note trims; reverted there.
- Low-mid weight is mostly in the stems, not the EQ (removing a +3 dB cello bell at 170 Hz cost the theme 2.8 dB for a 0.3 dB share change).

# Adagio c54 critic findings (2026-11-10), check in Movement I c56/c57
- BALANCE (critic B, c56): "mushy" there is a missing bottom octave more than excess low-mid: 56-112 Hz share -15.6 dB against Brahms -7.9/-7.3. Double basses' 80 Hz -6 dB bell, 140 Hz +4.5 bell and the loud_eq 100 Hz shelf move tonic fundamentals to their octaves. Measure Movement I's 56-112 Hz share against a Brahms reference and simulate removing the bass bells/shelf on the stems before changing mix.json.
- soft_trim/dyn_trim did NOT take back crescendos in the Adagio (109 of 115 rise); scherzo did. Measure Movement I.
- A level lift fully up on the beat with at most 2 dB change up to +0.45 s does not move S; a 3 dB rise inside that window shifts S by about +70 ms.
- S (pcX) invalid on octave joins and unreliable where the new note's band is level around t50; use the crossover there.
- After join notches, check the note body (bodies 5-8 dB under the transition in a cello line).
- Horn 1 EW patch: A flat 3 and G3 4-7 dB weaker than C4 at the same CC11; pitch trims.

# PRIORITY for c56 (Dan, 2026-11-11): per-note track-volume envelope looks unnatural
Dan opened REAPER and saw large peaks and valleys on individual notes, also on fast notes. Measured on build/parts.json vol_db + c55 stems:
- 2250-4200 envelope points on each string track (4-11 per note); within-note swing median 2-3 dB, p90 6-9 dB, max 21-24 dB; 94 of 367 Violins I notes swing 6 dB or more. Bars 15-16 Violins I: -1 to -10.7 dB inside two bars.
- Net effect on note-to-note level step (first 0.35 s; stem minus envelope = level without it): Violins I 56-90 1.4 with / 1.3 without (no gain); Violins I 104-128 2.4 / 3.8 (helps); Violins I 304-384 2.9 / 3.9 (helps); celli 184-244 2.7 / 2.5 (hurts, SD 5.5 / 4.5); Oboe 1 88-104 3.4 / 2.4 (hurts); Clarinet 1 520-536 3.1 / 1.9 (hurts); Horn 1 all 2.8 / 3.0.
- Task: classify the vol_db layers (slow: roles, dynamic trims, balance steps, final fade; per-note: accent shapes/fits/bodies, join notches, re-bow/loop/early fills, pitch trims, level steps, cresc fronts, swells). Range-test theme 56-90, celli 184-244, Oboe 1 88-104, Clarinet 1 520-536 with per-note layers off, and with per-note layers capped at +-3 dB and none inside notes of 0.5 qn or less. Keep a layer only where it lowers the measured note-to-note step or cures a named fault. Prefer CC11/CC1/velocity for musical shape. Deliver A/B clips for Dan.

# Coordinator decisions on the c56 critic reports (actor: these are your orders of priority)

Facts agreed by the three critics: 74 % of the fader's travel is inside single notes; 2353 of 5282 notes swing 3 dB or more inside the note, 45 % of those with no printed marking; reference projects (EastWest templates: no volume envelope; Duc's Mahler and LOTR: 0.01-0.36 points per second) against 5.2-9.7 points per second on our strings. Balance does not depend on the per-note layers (track level changes 0.3 dB or less without them). Needed per-note layers: steady_body/tail lifts on the theme, re-bow fills, basses' trims, plucked trims, the accent layer as such.

## 1 Reduce the per-note volume envelope (Dan). Report before/after for every track: points per second, notes with 3 dB / 6 dB or more inside the note, share with no marking. Aim: at least halve the 3 dB count overall; no measured line's note-to-note step (body 0.05-0.35 s AND front, both measures) worse by more than 0.3 dB; theme targets of c55 kept (S robust SD, front minus tail, theme over celli).
a. Short notes (0.5 qn or less): one level per note (C #1: NOTE_FLAT pass in build_reaper.vol_points or at the source in score_to_parts.py, your choice; the source is better). Drop steady_levels54 / PICKUP_LIFT rows on eighths in Violins I 56-90 and celli 520-536; keep them on Violins I 104-128 (simulation fails there). Range-test with and without str_rep_dips / detach_dips on two passages; keep those dips only if the repeated notes stay separated (A says keep).
b. Theme level steps and the end of body/tail lifts: key to the next note's score onset with a 40 ms crossfade instead of the moved note-on (A #1: join holes 9.0 dB with the envelope, 4.7 without; holes over 6 dB 15 of 36). Refit steady_levels54 as residuals; check S on a range render (twice, discard the first).
c. Accents (A #2, B): refit accent_fits to +3 dB over neighbours, swell cap +3, total per-note shape cap 6 dB. Remove fitted accents and accent bodies where the line is less even with them: Oboe 1 88-104, Clarinet 1 520-536 (521/526/529 to about 1.5/1.0/0.5), Horn 1 400-430, Trumpet 1 456-496. Front steps on Violins II 104-128, celli 520-536, Violins I 304-384: remove if the range test confirms B.
d. Winds and brass: delete or flatten LEVEL_SHAPES / early_fills rows that put a front 3 dB or more over the body with no accent printed (C #2 list: Horn 3 256, Horn 1 206 and 201, Horns 1-2 108/112/528/532/556, bassoons 558-560, Horn 2 484; 56 notes in all). Horn 1 crescendo notes at 40, 94, 620, 662: the dynamic trim moves 7.5-12 dB inside the note; limit it.
e. Oboe 1 88-100 fills and trims (A #3); final-chord re-bow fills capped at +4 dB with residual fit (A #5); harp bars 47-59 level to velocity (A #6) if cheap.
f. Deliver two A/B clips for Dan as mp3 in cycles/c56/ab/: bars 15-23 and bars 23-26 (oboe) or 131-134, c55 then c56, same loudness treatment; plus a text table of the envelope points of Violins I bars 15-16 before and after.

## 2 Bottom octave (B #1, B #3; Dan's "mushy")
Double basses in mix.json: delete mute_eq, 87.3 Hz bell to -4 dB, keep loud_eq. Confirm on a range render of bars 1-14 (70-112 Hz share, bar 84 level, peak). Then test a 120 Hz +3 dB / 0.8 oct bell on celli and basses; adopt if the 125 Hz band rises about 1.5 dB for under 1 dB of celli level and no bar rises more than 1.5 dB. Timpani bell: no. Tuba: leave.

## 3 Dynamics rows (C #3, C #4)
Per-row fixes from C's report for crescendos that fall on their own stem (Violas 72-76, Horn 1 408-415, celli 601-603, Flute 2 480-484), Violas 612-616 diminuendo, clarinet trims in bars 9-12. Bar 160 over bar 122 margin: note it, change only if a row above causes it.

## 4 Carried over, if time
Three stem-fix rows into REAPER (celli 159, celli 526, cor anglais 24); celli 520-536 S; Horns 3-4 p +2 dB (B #4) only after checking the 21 notes.

Not this cycle: lyrical-line rows, winds row-lead table, delivery rise delay, blend and space (c57).

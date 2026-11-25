# One-time task for the cycle 30 actor (rename to ONE_TIME.done.md when done)

MANUAL-GAPS #1 (brass and clarinet dynamics on CC1) has been deferred three times (c28, c29). Every horn, trombone, tuba and clarinet plays CC1 53-87, the middle layers, at every printed dynamic, so p and ff have the same tone colour (c28 critics B #4, C #3: Horn 1 F4 centroid 493 Hz at p vs 486 at ff). Do it this cycle, as Movement I did in its c09 (`CC1_DYN_TRACKS`, `CC1_DYN_MAP`, `CC1_HOLD` in score_to_parts.py; check each patch's CC1 layer table with dump_ks.py / the .oib first). Keep the other changes of this cycle few, so its effect can be measured: per track and printed dynamic, level and 1-5 kHz brightness before and after, and refit the level tables on those tracks (roles, accent fits) where the layer change moved them. Record the result in MANUAL-GAPS.md and LEARNINGS.md.
# One-time task for cycle 38: less hall (Dan, 2026-11-07)

Dan listened and said the mockups sound too wet, and that everything still sounds a bit mushy. He wants every movement to dial the reverb back from now on. The shared values are in mockup-kit/README.md item 7 and mockup-kit/LEARNINGS.md ("What a listener noticed" and section 12). Apply them here:

1. Before changing anything, measure on the c37 render: the master's drop 0.3 s after each tutti cutoff (about 9-10 dB expected at the current hall), the late decay time, and the repeated-note dips and legato join notches.
2. build/mix.json `reverb.fx_volume` 0.19 -> 0.095 (-6 dB on the hall return; Opus mixer volumes are linear amplitude). Keep the sends, the IR, wet 2.0, the 5.5 kHz high cut and true stereo unchanged. Do not raise sends to get the depth back.
3. This is an Opus state change: fully rebuild every track (not --midi-only).
4. After the render check: the drop 0.3 s after each tutti cutoff should be at least 13 dB (real recordings 13-17 dB); the late decay (1.5-2 s in recordings); repeated-note dips and join notches against c37. Refit only the fills and notches the drier tail moved, and fix levels by stem fix. Check that the niente of bar 66 and the coda morendo still decay naturally (S3).
5. If the late decay still runs over 2 s, note it in HISTORY.md as a later-cycle task (a shorter hall IR).
6. Record the before/after values in CHANGES.md and a short dated bullet in loop/LEARNINGS.md, then append this file's text to ONE_TIME.done.md and delete this file.

7. Added later on 2026-11-07 (shared guide, same goal): a 160 Hz low cut on the hall input. Copy the `low_cut_hz` block from mockup-kit/pipeline/build_reaper.py (right after the high-cut block: filterActive true, lowFilterFreq = lowCutFreq = value) into tools/build_reaper.py, and set "low_cut_hz": 160 in build/mix.json reverb. Keep high_cut_hz 5500. It is a state change: fold it into the same full rebuild as fx_volume 0.095. Not adopted: separate lower sends for shorts or low strings.
# One-time task (from c40): Movement I's measured fixes for Dan's "too wet, mushy" note

Movement I measured these in its c44 (symphony/mvt1/reaper-v621/cycles/c44/CHANGES.md; mockup-kit README items 7, 11, 12; mockup-kit/LEARNINGS.md "Too wet and mushy"). Each is an Opus state change, so fully rebuild every track, all in one rebuild together with this cycle's critic fixes.

1. **Shorter hall tail.**
   - Add `"ir_setup": {"envelopeMode": 2, "endPos": 0.7, "decayLength": 0.7}` (coordinator's decision: Movement I used 0.5, but this movement's late decay is already 1.17 s and c40 critic C estimates 0.5 would bring it to about 0.7 s) to build/mix.json `reverb`, next to fx_volume 0.095 and low_cut_hz 160. Leave the sends, IR, wet, high cut and true stereo as they are.
   - Copy the irSetup code (about 13 lines, the ConvolutionReverb insert's `irSetup` dict) from mockup-kit/pipeline/build_reaper.py `apply_mix`, right after the low-cut block, into tools/build_reaper.py.
   - `simpleDecay` does nothing; every patch ships factory values, so the setting must be explicit.
   - Check: c38 measured a 1.19 s late decay after the final chord, already shorter than Movement I's before value. Measure again the same way (cycles/c38/actor_scripts/hall38.py). Recordings give 1.1-1.6 s. Aim for 1.1-1.6 s. If it comes out under 1.0 s or the coda morendo sounds cut, note 0.85 for the next cycle; if over 1.6 s, note 0.5.
2. **Release caps** (`sus_release_cap_ms` per track in build/mix.json, read by cap_release; check that tools/ has cap_release and copy it from mockup-kit/pipeline if not).
   - Every section string track: `{"ms": 150, "dyn": ["pp","p","mf","f","ff"], "rows": ["Sus MAX","Sus Marc LITE"]}`.
   - Every horn track: `{"ms": 237, "dyn": ["pp","mf","f"], "rows": ["Sus MAX","LegRep RRx4"]}`.
   - Check row names against this movement's patches (dump_ks.py) before relying on them.
   - c40 critic C measured that about 85% of string notes and 47 of Horn 1's 51 notes play legato rows, which these caps miss. Also cap the strings' legato rows (Leg Slur MAX, Leg BC MAX, Leg Port MAX, Flautando, as named in the patches) and add Leg Slur MAX to the horn cap; name the divisi and solo tracks explicitly. If legato-join dips deepen by more than 1 dB, use 237 ms on the string legato rows instead.
   - Then refit the re-bow fills with fit_rebows.py (Movement I's dips deepened to 5.4-7.7 dB and returned to 3.1-5.4 dB after the refit). Check that no phrase end falls more than 10 dB in its first 0.05 s.
3. **Repeated string notes (Dan's S1).** Port the generic rule `STR_REP_NEW_BOW` from symphony/mvt1/reaper-v621/tools/score_to_parts.py (read only; settings and code places in its cycles/c44/CHANGES.md item 3).
   - Loud, accented, slur-head or slurred-tenuto same-pitch repeats become fresh Sus MAX strokes after a gap of min(0.06 s, 25%). Soft repeats inside one slur stay merged.
   - Reconcile it with this movement's existing MERGE_NOTCH_AT, REBOW and REP_RETONGUE rules so no onset is handled twice.
   - Check S1 at the critic-flagged repeats (c39 A #3: Violins II 289/292, violas 62, violas div 70/79, basses 144/156/168/253/265).
4. After the render, record the measured before/after in CHANGES.md and LEARNINGS, append this file to ONE_TIME.done.md and delete it.
(c40: done; see cycles/c40/CHANGES.md)

## Done in c41 (2026-11-07)
# One-time task for c41

Movement I's c45 measured these (symphony/mvt1/reaper-v621/cycles/c45/CHANGES.md, "Values for the other movements"; code in mockup-kit/pipeline/build_reaper.py `apply_mix`, commit 409ab8de).

1. **Keep the hall** as c40 left it. Movement I's tutti stops fall 20 dB in 0.45-0.55 s, against 0.43-0.58 s in Brahms 1 and the Dvořák. Measure this movement's final chord and the breath at 268 the same way and record it.
2. **Stereo width.** The drier hall narrows the image. Movement I's master side/mid fell from -5.6 to -7.3 dB, below every reference (-4.7..-5.4). Measure this movement's master side/mid and correlation below 250 Hz first; act only if it is below the references.
   - Mix only: set any side-only low cuts to 0 dB (c37 added a timpani side shelf at 300 Hz and c33 centred the sub-bass with side shelves: check each before changing).
   - Opus state change (full rebuild of those tracks): add build/mix.json `width_by_mic`: `{"Main": 0.35}` on the wind, horn, trumpet and low brass groups; `{"Main": 0.45}` on celli and basses; try `{"Main": 0.2}` on Clarinet 1, Horn 1 and Trumpet 1, whose image spread across pitches rose on Movement I. Close keeps the track width and seat. Copy the code from the kit's `apply_mix`.
   - Movement I's result: correlation below 250 Hz 0.78 -> 0.57, side/mid -7.3 -> -6.3 dB, stem levels unchanged.
3. **Release-trail gain** `rt_gain_db`: do not adopt yet. Movement I withdrew its c45 result (its test stems had mismatched controller data); its c46 reruns the test. Wait for those values. For any test stem of your own, diff its parts.json notes and CCs against the source track before comparing.
4. Record the results in CHANGES.md and LEARNINGS, append this file to ONE_TIME.done.md and delete it.
# One-time task for cycle 44: adopt the EastWest template and expert-mockup defaults (Dan, 2026-11-08)

Dan: "yes to anything you can do ... don't wait." Every item in `mockup-kit/EW-TEMPLATE-PLAN.md` sections 1-9 is a default
for all four movements from each movement's next cycle. That is this cycle for Movement II. The plan's cycle numbers (c50/c51)
are Movement I's. Critics tune the values and may drop an item only with measured evidence. Where sources disagree, the plan
names the default, and Duc's shorter single hall is the fallback. Sources: `symphony/mockup-research/ew-template-2026-11-08/`
(FINDINGS.md parts 1-5, ho-mix-chunks/, ho-mix-fx.json, opus-mics.txt, duc-mix.txt, cubase-mix.txt, and the reports).

Reuse existing code; do not rewrite it. Start from the finale's REAPER-verified version in
`symphony/mvt3/reaper-v600/tools/build_reaper.py`: pan_by_mic, track_pan, Opus hall off, returns pasted from the template
chunks, post-fader sends, "FAMILY EQ" ReaEQ and master EQ. Movement I has a second version, tested offline only, behind
mix.json keys: `symphony/mvt1/reaper-v621/tools/template_mix.py` and `return_stems.py`, documented in
`tools_next/TEMPLATE-TOOLS.md`. Copy into this folder's tools/ and adapt there. Never edit symphony/mvt1/ or mvt3/.
The finale's first template render measured three things (mockup-kit README, commit a76a7b6e). Fix them up front:
- brass needs +4-6 dB make-up after the family EQ;
- the mix came out bright (6-20 kHz share -25 dB against -29 to -32 in the references): use the 2.3 kHz low-pass after
  each Spaces II return;
- tutti stops took 0.62-0.73 s to fall 20 dB: use the register sends (low brass, bassoons, contrabassoon and basses 10 dB
  below their family, trumpets 6 dB below), with Duc's 2.3 s hall as the fallback.

## This cycle (c44): the mix (plan sections 1-4, the mix parts of 8-9)
- Mic layout inside Opus: pan_by_mic, replacing width_by_mic and the seat-narrowed Main.
- Opus reverb off on every track, with per-family Spaces II returns using the plan's IRs, pre-delay, sends and return EQ.
  Batch 5 register sends: none, or -16 dB or lower, on low brass, bassoons, contrabassoon and basses. Percussion is
  unchanged. Use the plan's stated default where batch 4 or 5 conflicts with section 2.
- The section EQ and master EQ from section 3. Remove older per-track EQs that only did what the family EQ now does.
- Return stems are rendered and the master is dry plus returns, as section 2 says. Then re-fit deliver_master.py to the
  delivered targets.
- Keep one pass-2 copy of the old c43 layout (Opus hall, mics) for comparison: either a short A/B excerpt render or the c43
  stems themselves. Say in CHANGES.md which you used.
- The pass-2 A/B items named in the plan (the 1.8-2.3 kHz return low-pass, narrow brass, the ALGO GLUE return): do each
  one if there is room, otherwise leave it for c45.
- Re-check balance after the EQ, since it removes 2-8 dB in the body bands.
- Opus state changes on every track, so all 32 tracks need a full rebuild. Allow for long patch loads, and check memory.

## Next cycle (c45): the performance data (sections 5-9)
Overlaps and repeat gaps (60-100 ms), legato velocity, dense CC1 with the phrase swell after the onset, the taper over the
last second, the in-slur lean-off, the symmetric arch, per-track early shifts, and hairpin shapes. Also the CC1-only
pass-2 strings test. Research batch 6 (FINDINGS.md Part 6, commit 23a6225a on claude/project-thread-cn1rc0, Balfe sketches):
phrase shape by context (builds enter near zero and peak at the end; accented brass/fanfares enter at the top and fall 15-25
over a long note; lyrical lines keep the centred arch), repeated short-note groups fall 15-17 velocity first to last with
±5-7 random and strong beats +20-25, doubled lines share one dynamics curve, A/B brass timbre 25-35 under level and strings
about 15 over, spiccato length about 60% of the slot. Leave tempo/rubato (sections 8-9, Duc and batch 5) for c46 unless it fits.

When done, move this file to loop/ONE_TIME.done.md (append), and send the c44 mic/hall numbers in CHANGES.md so the
coordinator can pass them to Movement I.
# One-time task for cycle 45: performance data (EW-TEMPLATE-PLAN sections 5-9, research batches 3-7)

Dan, 2026-11-08: "yes to anything you can do ... don't wait." Every item in `mockup-kit/EW-TEMPLATE-PLAN.md` is a default.
Critics tune the values. An item can be dropped only with measured evidence. Sources: FINDINGS.md Parts 3-6 on
origin/claude/project-thread-cn1rc0, and the originals in /Users/gooby/sandbox/mockup-reference-cn1rc0/mockup-kit/reference/
(Balfe sketches, Duc projects, expert MIDIs). Measure our MIDI against them. Critic A's c44 report
(cycles/c44/reports/A.md) has the c43 baseline for phrase shapes and CC density.

## The MIDI (score_to_parts.py / build_reaper.py --midi-only)
- Phrase shape by context (batch 7):
  - Lyrical lines: an arch peaking at about 0.44 of the phrase, starting and ending about 33 CC under the peak. Long notes
    keep moving and are never flat.
  - Builds enter low and peak at the end.
  - Driving or accented music (brass fanfares, accents) starts at the top and falls 15-25 over a long note.
  - Ride the level lane in the same shape as the timbre lane. Do NOT add the brass/strings timbre offset (batch 6 item 4
    was withdrawn).
- Phrase swell after the first onset: CC1 +15 by 0.4 s and +25 by 0.8 s. Taper about 20 over the last second. In-slur
  lean-off about -2 per note.
- Crescendos rise early, then settle. Diminuendos fall on the last held note. Winds and brass may fade nearly out before
  rests.
- Dense CC: 13-44 points per second while a note sounds.
- Short notes:
  - Velocity by beat position, with 15-25 steps between the strongest and weakest beat, and ±5-7 random.
  - Repeated short-note groups fall 15-17 velocity from first to last.
  - CC parked high for shorts.
- Spiccato length 50-62 % of the slot.
- Doubled lines share one dynamics curve (one CC1/CC11 lane for all tracks of a doubling).
- Legato: overlaps per patch, 46-230 ms; legato velocity by the plan.
- Per-track fixed early shift: winds 17-85 ms, strings and brass 20-120 ms, percussion on the grid. Check against the
  attack probe and S2 (attacks on the beat). The probe must stay 0.
- Repeat gaps: keep c44's soft_gap 0.08 / loud_gap 0.10 (60-100 ms). Fix the three that are left: Violins II 289 and
  120, Violas 87.
- Pass-2 test: CC1-only dynamics on the strings (CC11 flat) as a test stem, against the main version.

## Carried from c44 (mix)
- Too bright: 6-20 kHz share -24.6 dB, against -30.1 in c43 and -29 to -32 in the references. Halve the strings and
  brass family shelves (critic B). Re-check the brass 2-5 kHz accent jump (p90 under +2 dB).
- Bass image too wide: L/R correlation below 250 Hz 0.06 (c43 0.66, references 0.54-0.62), side/mid -2.2 dB
  (references about -5). Try side low shelves or a narrower bass on the Main pairs.
- Timpani +1 dB stem fix: revert it if the rolls are heavy (Dan's rule 5).
- Trombone 1 at qn 213 is only 2.1 dB over its pickup (c43 6.7).
- Delete R Duc and the four RE test tracks from the project.
- Wetness limits stay: no family wetter than c43. Strings 0.55 s or less, winds and brass 0.50 s or less, final chord
  0.45 s or less to fall 20 dB.

Tempo and rubato (sections 8-9, critic C's c44 plan) are left for c46.

When done, append this file to loop/ONE_TIME.done.md and remove it.
# One-time task for cycle 46: rubato (EW-TEMPLATE-PLAN sections 8-9, research batches 4-5)

Research (FINDINGS.md Parts 4-5, Duc's Mahler Adagietto, Mulan/Howl's) found that our tempo moves far less than an expert
mockup:
- median beat deviation 8 % in the references against 3.0 % in ours;
- phrase-end breaths 15-30 % slower;
- tempo changes on about 20 % of beats.
Critic C's c44 report (cycles/c44/reports/C.md, finding 1) has a complete plan:
- PHRASE_ARCS ends moved to the real phrase ends, before the pickups;
- a new CAESURA table (both definitions replaced);
- a BEAT_STRETCH table.
Start from it. The c46 critic for tempo re-measures it against the references
(symphony/mockup-research/ew-template-2026-11-08/scripts/rubato.py) and tunes it.
- Keep S2 (attacks on the beat): the attack probe must stay 0 after the tempo map changes, and early shifts and lead
  times must follow the new map.
- No caesura may cut a hall tail into silence (S3). Check every breath for a smooth tail.
- Length will grow; report the new length.
- Hairpin curve shapes (plan section 8): port them, but keep timpani roll lanes linear (Movement I measured a curve
  lifting a fff→pp roll 8 dB over a horn solo).

## Carried from c45
- Trombone 1: the c45 stems and build/ have its role at +3, but the saved REAPER project does not. Include Trombone 1 in
  `--midi-only`. Its qn 213 accent is still only 2.2 dB over the pickup: give it a window that starts at 213, not 212.5.
- Movement I c51 findings (symphony/mvt1/reaper-v621/cycles/c51/reports/):
  - loud tutti brighter and thinner than the references: halve the brass bells (475 Hz to -2.7, 821 Hz to -3.9 dB),
    add a 3.2 kHz -3 dB bell, and lower brass gains 1.8-4.0 dB to keep each stem's loudness. Measure our loud frames'
    centroid first.
  - soft timpani rolls: a 160 Hz -3 dB low shelf on the soft-roll spans only, +1 dB level there, if the rolls take more
    of 30-150 Hz than in c43.
- Violas qn 87 master dip 1.3 dB (still under 3). The violas' alternating portato takes peak at the same level.
- Oboe 1 join timing +46 ms (target ±30).
- Check whether two renders of unchanged data now match after the CC16 round-robin reset.

When done, append this file to loop/ONE_TIME.done.md and remove it.
# One-time task for cycle 48: the finale's shared techniques

Dan asked that each movement's techniques reach the others. The finale's list, with exact settings and measured results,
is symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md. Its code is in symphony/mvt3/reaper-v600/tools/: copy into this
folder's tools/ and adapt, and never edit mvt3. Many items are already in place here: the dry hall from c44-c45, the
side-EQ width from c45, the brass bells from c46, and the string 1 kHz bell. Critics check the remaining items against
Movement II's own measurements. Adopt an item where it improves the measured result; drop it only with measured
evidence.
- Item 2, sfp/fp: our bar 47 fp at qn 148. Check whether a crescendo or hairpin on the same onset overwrites the spike,
  apply FP_SPIKE_AT_MARK / FP velocity, and judge each part's own drop (10 dB or more).
- Item 3, sub. p: our subitos (qn 195-196 and any other). PHRASE_SHAPE "drop" with no positive offset, and
  HELD_DECRESC_CARRY. S3 must hold.
- Item 5, brass seating: track_width on the brass, if Movement II's brass image measures wider than the references.
- Item 6, "mushy" low mids: the horn family bell at 315 Hz -5 dB and violas 315 Hz -3 dB, with make-up. Measure our
  315 Hz excess over the recordings first.
- Item 7, FINAL_RING: our final chord now falls 20 dB in 0.40 s, under the recordings' 0.43-0.55 s, because of c47's
  -4 dB fade. Decide between FINAL_RING and the fade by measurement, within the 0.45 s limit or the recordings' range.
- Item 9, harp: cap velocity at 123 (Nail Pick layer at 124 and up).
- Item 10: measure brass accents with the tilt jump (2-5 kHz minus 0.5-2 kHz).
- Item 11: winds family 1 kHz -1.55 dB with make-up, if our wind tone measures off the references.
- Item 12: the basses' template high-pass from 53 to 35 Hz, checked against "bass solid but not boomy".

## Carried from c47
- Oboe 1's eighths at 142 / 142.5 are 2.5-3 dB softer under the shorter fills.
- Horn 4 at qn 84: swing 9.3 dB (rule: under 5 dB); the rest is the sample's own loop dip.
- The bass clarinet repeat at 265 lost its own-band dip (12.8 to 1.5 dB).
- Movement I c51 lessons (mockup-kit/README.md): winds need phrase-shape offsets ×1.4 compared with brass; check inner
  held notes under a tune after held-note dynamic changes.

When done, append this file to loop/ONE_TIME.done.md and remove it.

(c48 actor, 2026-11-09: done; decisions in cycles/c48/CHANGES.md)

# One-time task for cycle 49: the finale's techniques 18-23 and c48's open items

The finale thread sent six more measured techniques after its cycle 11. Full text with settings and results:
symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md items 18-23. Its code is in symphony/mvt3/reaper-v600/tools/: copy
into this folder's tools/ and adapt, and never edit mvt3. Adopt an item where it improves Movement II's own measured
result; drop it only with measured evidence, and say which in CHANGES.md.
- Item 18, repeated low-string eighths: measure our low-string repeats at the fundamental (30-120 Hz), not the harmonic
  band. Where on-beat strokes are weak, a volume dip only in the played gap before each beat (-9 dB, note-off + 6 ms to
  next onset - 3 ms), with the downbeat's metric step starting at the onset.
- Item 19, sf on winds and brass: the post-fader bump (+3 dB over 0.35 qn) on our sf at bar 63 (qn 212: flute 1, bass
  trombone) and any other wind or brass sf / fp whose first 0.1 s is more than 2 dB under the f it should match. Try it
  before any new Opus row.
- Item 20, legato lead tables: check that a negative per-onset row is added to the total lead (base + velocity extras)
  before the clamp in our score_to_parts.py.
- Item 21, string repeats: a tenuto repeat inside one slur and a repeat that starts a new slur need different gaps
  (0.06 s and 0.12 s in the finale). Apply to the Violas' repeat at qn 271, whose own-band dip fell from 8.9 to 3.2 dB
  in c48, and to the other S1 points under 3 dB.
- Item 22: note trims ramp in over 0.6 s and barely act on eighths; use a level shape over the run (as c48 did for
  Oboe 1 at 142 / 142.5; that shape should end after the 142.5 note does).
- Item 23, delivery ride after a subito: hold the row at 0 through the subito bar and ramp in over about 10 qn; check
  our f to p steps in the mp3 against the master.

## Carried from c48
- Trombone 1 came out +2.6..+3.6 dB louder and 27-49 ms early at qn 213-215.5 on unchanged data; c48's delivered stem is
  c47's. Fully rebuild Trombone 1 in this cycle's build and compare with c47's stem.
- Stale legato state (scherzo c09, mockup-kit/README.md): our legato tracks have been built `--midi-only` since c45, so
  their leads were fitted on the saved post-playback state. Decide with the critics' evidence whether to fully rebuild
  the legato tracks and refit the leads in this cycle (S2 must hold after it).
- The fp at qn 148: master tilt jump +3.3 dB against the 3.0 ceiling; Violins II peak +115 ms after the beat.

When done, append this file to loop/ONE_TIME.done.md and remove it.

(c49 actor, 2026-11-09: done; decisions in cycles/c49/CHANGES.md. The stale legato state item is deferred to c50 by the loop lead: loop/ONE_TIME.next.md)


## c50

(c50 actor, 2026-11-10: done. State guard copied and run (0 stale before the work); every legato track rebuilt in full and measured alone; leads refitted under the lead guard; decisions in cycles/c50/CHANGES.md.)

# One-time task for cycle 50: full rebuild of stale legato state, measured alone

Movement II's legato tracks have been built `--midi-only` since c45, so the saved Opus state holds post-playback
envelope attacks (scherzo c09) and the legato leads were fitted on it. This cycle's main change is that rebuild; keep
other changes small so its effect on S2 (attacks on the beat) can be read.
- Copy symphony/mvt1/reaper-v621/tools/state_guard.py into this folder's tools/ and adapt (never edit mvt1). It decodes
  every Opus block of a saved .rpp and compares each legato group's envelope attack with the written state. Run it on
  the current project first and list the stale tracks in CHANGES.md.
- As in Movement I c52: `build_reaper.py --midi-only` fully rebuilds stale tracks, and `render_cycle.py` refuses a
  stale project.
- After the rebuild, re-measure the legato joins and refit the leads (Movement I: joins went from 18-45 ms early to
  within -8..+1 ms). Level trims that were fitted on stale audio may have to be reverted: check every trim fitted in
  c45-c49 on a legato track against the new stems.
- Movement I c52's other findings (mockup-kit/README.md, symphony/mvt1/reaper-v621/cycles/c52/CHANGES.md):
  - state_check.py must remove EQ changes before comparing two renders (mvt1 tools/eqresp.py); it does not model
    track-width level loss.
  - Track width costs level (trumpets at 0.5 lose 2.2-2.8 dB, trombones at 0.6 lose 1.0-1.9 dB); check our horns at
    0.8 keep their make-up within ±0.3 dB.
  - Side EQ and brass widths must be simulated together: each was inside the references alone and just outside
    together.
  - A "drop" phrase type by the 6-CC rule made 283 spans in Movement I; restrict it to printed subito marks if we use
    it.
  - Low winds with a clamped swell: put the clamped part into the volume envelope (0.20-0.32 dB per CC unit).
  - Inside a crescendo shorter than 4 qn, the phrase offset must not fall below its value at the hairpin start; count
    our reversed crescendos.
  - Corrected by Movement I (2026-11-09): the template's CC1 vibrato macro on celli is not the cause of deep legato
    joins (6 of 261 joins dipped 2 dB or more with it, against 2.9 % and 3.2 % on two tracks without it). Keep the
    macro; do not remove it.
  - A render refused because REAPER closed its audio device is fixed by reaper.Audio_Init() from a script.

## Evidence and rules from c49
- Trombone 1, fully rebuilt in c49: its loud legato join at qn 217.5 came out 35 ms later and 1.9 dB lower than in c47
  (master -1.7 dB for about 0.75 s) and was not compensated. Expect the same kind of shift on every legato track after
  the rebuild, so measure each join against c49 before refitting anything.
- c48 had state drift on unchanged data that neither c47 nor c49 shows (Double basses qn 60-80, Violoncellos div 63,
  Horn 1 198). From this cycle on, run `tools/state_check.py` against the two renders before (c49 and c48) after every
  render and report any flagged run in CHANGES.md.
- Order of work: (1) state_guard on the current project, (2) full rebuild of the stale tracks, (3) range renders to
  measure the joins, (4) refit leads, (5) check trims fitted in c45-c49 on those tracks, (6) one full render. Do not mix
  in new mix or image changes; the critics' other findings wait unless they are data-only and small.
- Disk: 67 GB free on 2026-11-09 17:20 after Dan removed the stems of c36-c45 (a cycle adds about 4 GB; the 30 GB
  rule still holds). Do not delete other cycles' stems; c46-c49 are the comparison renders.

When done, append this file to loop/ONE_TIME.done.md and remove it.

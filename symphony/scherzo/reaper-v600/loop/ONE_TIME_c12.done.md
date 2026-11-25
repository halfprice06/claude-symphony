# One-time task for the c12 actor: finale SHARED-TECHNIQUES items 18-23 (arrived during the c11 cycle)

Source (read only): `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` items 18-23, code in its `tools/`. The c11
actor was told of items 20, 22 and 23 while working; read cycles/c11/CHANGES.md first and skip what it already did.
Adopt each unless measured numbers say no, record the result in cycles/c12/CHANGES.md, then rename this file
ONE_TIME_c12.done.md.

1. Item 18 (repeated low-string eighths): measure the celli's and basses' repeated arco eighths at the fundamental
   (30-120 Hz) on the c11 stems and master. If on-beat strokes are weak, add a volume dip only in the played gap before
   each beat (-9 dB, note-off + 6 ms to next onset - 3 ms) and start the downbeat's metric step at the onset.
2. Item 19 (sf of an sfp on winds and brass): the post-fader bump of item 13, +3 dB over 0.35 qn (+4 on the weakest
   front). Check every wind and brass track that plays the sfp at bar 301 (qn 900), Flute 1 first (no sf there since
   c10). Target: first 0.1 s within 2 dB of bar 300's ff. Try it before any Sus Accent row.
3. Item 20 (legato lead tables): in tools/score_to_parts.py, check that a negative per-onset row in leg_leads.json is
   added to the total lead (base + velocity extras) before the clamp. Test with one negative row and compare the
   requested and realised lead.
4. Item 21 (string chord repeats): a tenuto repeat inside one slur and one that starts a new slur need different gaps
   (0.06 s and 0.12 s in the finale). List the scherzo's string chord repeats by slur state (`slur -1` = start) and
   measure their dips on the c11 stems; the same test applies to the horns' slurred tenuto repeats in bars 209-222.
5. Item 22 (note trims on short notes): note trims ramp in over 0.6 s. List every note trim on a note shorter than
   about 0.6 s (the pizzicato trims of c11 critic C #5 among them), measure requested against realised, and move the
   ones that fall short into a level shape over the run.
6. Item 23 (delivery ride after a subito): the ride row must stay at 0 through a subito bar and ramp in over about
   10 qn. Check the rows at the sub. p of bars 277 and 281 and after the G.P. at bar 340; compare the f to p step on the
   master and in the mp3. When simulating, keep the parts.json copy next to mix.json or the ratio falls back to 3.0.
7. From Movement II's c48: a non-legato stem (Trombone 1) changed level (+2.6 to +3.6 dB) and timing (27 to 49 ms
   early) on unchanged data after --midi-only builds; a full rebuild of the track fixed it. If c11 did not check the
   brass for this, compare unchanged tracks between two renders and fully rebuild any that moved.

## Movement I c52 findings (arrived 2026-11-09 22:01Z)

Full text (read only): `mockup-kit/README.md` and `symphony/mvt1/reaper-v621/cycles/c52/CHANGES.md`. Check each
against the scherzo and record the result.

8. Stale legato state guard: `symphony/mvt1/reaper-v621/tools/state_guard.py` decodes every Opus block of a saved .rpp
   and compares each legato group's envelope attack with the written state (five stale tracks found in Movement I's
   c51 project; joins went from 18-45 ms early to within -8..+1 ms). Port it to tools/, run it on
   scherzo-v600-mockup.rpp, make `build_reaper.py --midi-only` fully rebuild stale tracks and make render_cycle.py
   refuse a stale project. Revert level trims that were fitted on stale audio.
9. A check that compares two renders must remove EQ changes first (Movement I's tools/eqresp.py); it does not model
   the level lost to track width.
10. If the scherzo uses the "drop" phrase type with the 6-CC rule, count its spans; restrict it to printed subito
    marks (Movement I had 283 spans, many 16-64 qn, against 16 printed).
11. Track width costs level (trumpets at 0.5 lose 2.2-2.8 dB, trombones at 0.6 lose 1.0-1.9 dB). Measure each narrowed
    track's stem against its width-1.0 level and add make-up gain.
12. Side EQ and brass widths were each inside the references alone and just outside together (250 Hz-5 kHz
    correlation 0.566, side/mid -5.53 dB). Simulate width and side EQ changes together.
13. Low winds with a clamped swell: put the clamped part into the volume envelope (0.20-0.32 dB per CC unit).
14. Inside a crescendo shorter than 4 qn, do not let the phrase offset fall below its value at the hairpin start.
    Count reversed crescendos on the stems before and after.
15. Withdrawn by Movement I (2026-11-09 23:13Z): the template's CC1 vibrato macro on the celli is not the cause of
    deep legato joins (6 of 261 joins dipped 2 dB or more, 2.3 %, against 2.9 % and 3.2 % on two tracks without it).
    Keep the macro; no action.

## Movement II c49 findings (arrived 2026-11-09 22:56Z)

Full results (read only): `symphony/mvt2/reaper-v600/cycles/c49/CHANGES.md`.

16. A CC16 round-robin reset in the middle of the score works and is repeatable (two range renders identical after
    it; Movement II's table RR_RESET_AT in its tools/score_to_parts.py). Where a repeated-note passage's take order
    changed between two scherzo renders (uneven staccato or pizzicato repeats), try a reset before the passage.
17. State drift is wider than one comparison shows: Movement II's c48 had basses, divided celli and Horn 1 notes 2-6 dB
    off on unchanged data, and c49 returned to c47's state. Compare each render's unchanged tracks with the two renders
    before it (N-1 and N-2), not one. Do not fit a level trim to a difference that only one render shows.
18. Finale items 18, 19, 21 and 22 also worked in Movement II (gap dip on bass repeats: 30-120 Hz dip 2.7 to 7.7 dB;
    sf bump on bass trombone: +3 dB in the first 0.1 s; 0.12 s gaps on six soft string repeats: dips 1.5-3.2 to
    3.3-9.0 dB). This supports items 1, 2, 4 and 5 above.
19. Dropped in Movement II, do not try: a short "R Stage" return to widen a solo took 0.55-0.61 s to fall 20 dB,
    against Dan's "too wet" note.
20. Movement II's tools/pitch_check.py gives per-pitch level change against the track after a mic or width change.

## Finale c12 findings (techniques 24-33; full text in symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md, read-only)

21. (Finale 24) Same-pitch string repeats that must take a new bow: a "force" onset list in the new-bow rule gives a 74-90 ms data gap, but at p / pp the release tail still fills it. Add a volume notch inside the gap, in seconds before the note-on: ((-0.085, 0), (-0.060, g), (-0.015, g), (0, 0)); g = -8 dB gave a 10.1 dB dip. Where the repeat is softer than the note before, add that difference. Level-only, so it can go in by stem fix after the render.
22. (Finale 25) Detached f-ff cello repeats: detach dip -10 dB over 0.10 s (was -5 over 0.08) gave dips of 6.2-15.0 dB. A repeat after a legato-row note at velocity 124 also needs +4 dB over its first 0.8 qn.
23. (Finale 26) Late sfp peak in a tutti: a volume notch 0.11-0.40 s after the mark on the stems that keep rising (horns, trombones, tuba: -3 to -5 dB) plus a +3 dB front on the low brass. Applies to the sfp at bars 301-302 (qn 900-904) if the master peak there is late.
24. (Finale 27) Measure slurred joins on a sustain row per pitch (envelopes of harmonics 2-7 of the old and new pitch; finale cycles/c12/actor_scripts/joins6b.py), not by wide-band RMS. Keep overlaps on muted sustain rows at 0-10 ms.
25. (Finale 28) Pre-render simulation: stem_fix.py --out on the last render's stems, then deliver_master.py. Per bar within -0.30 / +0.21 dB of the real render; limiter 2.2 dB simulated against 2.6 real. Use it to test level-only changes before the render.
26. (Finale 29) Drift check on unchanged data (finale cycles/c12/actor_scripts/drift12.py). With a clean state guard: medians 0.00 dB on every track, single notes moved 2-6.7 dB on 12 of 31 tracks. A single-note difference under 7 dB between two renders is not evidence of a change.
27. (Finale 30) After adding a phrase arc: rebuild every track with --midi-only --tempo and rename the keys of seconds-spaced fits (re-bow fills moved 0.003-0.016 qn).
28. (Finale 31) Delivery ride over a soft passage: let the gain rise linearly across the passage instead of reaching its value in the first bar; a printed morendo then keeps falling in the mp3.
29. (Finale 32) HO Basses pitch trims: E2 +6, F2 / E flat 2 / F1 +3 dB raised those note bodies by 5.6 and 2.8-3.0 dB. Check the scherzo's basses on the same pitches before copying.
30. (Finale 33, results) A 0.03 s lead on the basses' on-beat sustain eighths moved the low-band rise by only 18 ms. Removing a 167 Hz -1.6 dB delivery bell raised the limiter figure from 1.6 to 2.6 dB and the longest stop decay from 0.47 to 0.50 s.
31. Rule from a finale mistake: never run tools/build_reaper.py (or anything that sends a job to the bridge) without holding the REAPER lock, even for an offline check.


Results (c12 actor, 2026-11-10): each item is recorded in cycles/c12/CHANGES.md, section 2.

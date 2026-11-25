# One-time task for the c06 actor: adopt EastWest's HO template mix (Dan, 2026-11-08)

(Done in c06: see cycles/c06/CHANGES.md. This file was restored by the c06 actor from the text it had read, after an
accidental overwrite when renaming; the content is the original.)

Dan has adopted EastWest's own Hollywood Orchestra REAPER template mix and MIDI rules as the default for all four movements: "take every bit of this and use it to improve our own scoring". The default is to adopt each item; reject one only with measured numbers, and record why in LEARNINGS.

Read first (read only, never write there):
- /Users/gooby/sandbox/claude_composes/mockup-kit/EW-TEMPLATE-FINDINGS.md
- /Users/gooby/sandbox/claude_composes/mockup-kit/EW-TEMPLATE-PLAN.md (commit 2e47a9c5)

The template's exact FX states (commit 1e9808d9) are in /Users/gooby/sandbox/claude_composes/symphony/mockup-research/ew-template-2026-11-08/:
- ho-mix-chunks/*.txt holds the verbatim FXCHAINs of each section bus, reverb return, harp, timpani and the master. Load them with TrackFX_SetNamedConfigParm(fx, "vst_chunk", ...).
- ho-mix-fx.json holds the decoded ReaEQ bands and the Spaces II JSON.
- opus-mics.txt, midi-report.txt, artic-report.txt and ccshape-report.txt cover the mics and the MIDI statistics.

With these chunks, item 3 below (the Spaces II returns) does not have to wait for Movement I's tools.

Corrections to the plan:
- Pre-delay differs by family: strings 19.6 ms, winds 18.5, brass 10, perc 10.
- Every return uses the full IR (endPos 1.0) with the rear-position impulses; the brass return loads the Horns impulses.
- On CC1: every template KS Master uses the Opus macro "Mod + Expression Combo", one CC1 lane driving vibrato and dynamic layers together, with no CC11.

Movement I is building the shared tools in its c50 (mix) and c51 (MIDI). Check symphony/mvt1/reaper-v621/tools/ and mockup-kit/pipeline/ for them before writing your own, and port them if they exist.

In c06, alongside the critics' fixes:
1. Plan item 1 (mic layout): strings and brass get Close panned to the seat, 4-10 dB under a full-width Main that is never re-panned. Woodwinds use Close as the main mic, with Main 3-21 dB under it. Harp and timpani as the plan says. Add the small REAPER track pans. This replaces width_by_mic and the seat-narrowed Main.
2. Plan item 3 (family EQ): put the family ReaEQ on every track, and the master EQ before delivery. Remove older per-track EQs that only did what the family EQ now does. Re-check balance afterwards.
3. Plan item 2 (Opus reverb off, Spaces II returns per family with ReaEQ before each, post-fader sends):
   - Do it if Movement I's tools for it are in the kit or in mvt1's tools by then.
   - If they are not, keep the current Opus hall for c06, and say so in CHANGES.md.
   - Note: the template's percussion and timpani return is "Northwest Hall TS RR 2.6s", shorter than ours. Re-check the bar-340 G.P. and the TIMP_DAMP_AT setting after the change.
4. Plan item 5 (MIDI):
   - Legato overlap 45-80 ms on strings and 33-58 ms on winds and brass.
   - Repeated-note gap 20-60 ms.
   - Legato velocity 90 or more where a clear change of note is wanted; check the manual first.
   - CC1 at 7-13 points per second.
   - The move from CC11 to CC1 is staged as the plan says. If c06 is already large, leave item 5 to c07 and say so.

All of these are Opus state or mix changes: full rebuild of every track. Measure before and after: balance, the G.P. drop at +0.3/+0.6/+1.0 s, the attack probe, LRA, and memory (keep it at or under 45 GB). When done, rename this file to ONE_TIME.c06.done.md, and list in CHANGES.md which items were adopted, deferred or rejected, with numbers.

Research batch 2 (plan section 6, commit f5077a89) for item 4:
- (a) CC1 at 57-79 sits in the 55-76 zone where both the Non Vib and Vib woodwind layers sound, which doubles the amplitude modulation. Measure mp-mf sustains, or cross 55-76 quickly.
- (b) String shorts: CC1/CC11 parked at 118-127, dynamics by velocity alone (medians 24-52). Brass and wind shorts use velocity 62-95. Shorts are 60-90 ms long and exactly on the grid. This suits the scherzo's staccato writing directly.
- (c) CC1 is shaped per phrase: flat across legato changes, a swell after the phrase start, and a taper of 13-37 units over the last 0.25-1 s.
- (d) Strings use a separate legato track ("Leg Slur + Port LITE", LegatoSpeed and RTKiller on) plus a KS Master for shorts, sustains and tremolo. Keyswitches go 40-800 ms early.
- (e) Keep our measured release caps.

Research batch 3 (plan section 7, commit 773b0244; from a hand-played professional mockup on other libraries, so the shapes and timing carry over but the absolute values do not):
- Phrase rule, adopt by default: CC swell after the first onset of about +15 by 0.4 s and +25 by 0.8 s, nothing before the onset; a taper of about 20 over the last second; scaled to the dynamic; printed hairpins take over.
- Inside slurs, a small per-note lean-off (about -2 by 0.4-0.8 s).
- Timing: winds early by a fixed amount per track (oboe -27, clarinets -38/-46, bass clarinet -17, bassoons -40/-85, flute -75 ms); strings and brass -20 to -120 ms. Percussion stays on the grid. Compare with our lead tables and measure with the attack probe before changing them.
- CC density 13-44 points/s.

Research batch 4 (plan section 8, commit 25bbfbf2; 20 expert MIDI mockups). It supersedes earlier values where they differ:
- Repeated-note gaps: 60-100 ms (medians: winds 63, strings 90, brass 98, short rows 116 ms), replacing the 20-45/20-60 ms above.
- Phrase arch: the peak at 33-62% of the phrase, with start and end well below it (30-60 units of range on long phrases). The rise begins after the onset, the last second tapers, and long notes keep moving.
- Legato velocity follows the dynamic, replacing "90 or more".
- Optional A/B tests for later cycles (not required in c06): Duc's single hall (2.1-2.45 s, low cut about 184 Hz, high cut about 3 kHz, return -5.5/-6.6 dB, low-string shorts sent 7 dB lower) against the EW returns; a string EQ variant; a tutti entry spread of 36-55 ms.

Dan (2026-11-08): "yes to anything you can do". Apply the research findings now, without waiting for Movement I's tools. The research thread's full FINDINGS.md (batches 1-4) is copied to loop/RESEARCH-FINDINGS.md; read it as well as the plan. Where the two differ, follow the newer batch.

Update (commit 96d05220, plan sections 1-8): everything in the plan is now a default, including what was listed above as optional A/B. Drop an item only with measured evidence, recorded in LEARNINGS.
- Sends: 0 dB for violins, violas and brass; -1.6 dB for cello and bass longs; -7 dB for low-string shorts.
- Basses EQ: -2.4 to -3.6 dB at 205-250 Hz.
- A seeded tutti entry spread of 36-55 ms.
- A room-noise bed only if a recording we are free to use exists (otherwise skip it and say so).
- Duc's single shorter hall is the fallback if the EW returns measure mushy.
- Movement I will post its c50 template-mix tools to mockup-kit once they are verified. Use them if they are there; otherwise build from the chunks in symphony/mockup-research/ew-template-2026-11-08/.

# Cycle 61: coordinator notes (read before anything else). Last cycle of this run; a report follows it.

## Dan's rules and requests (no exceptions)
- 2026-11-11: "yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem". Track volume envelope: slow balance only (gain, roles of a phrase or more, section dynamics, hairpin gain, divisi cuts, timpani dynamics, fades), as ramps. No per-note level or shape, no rows fitted to earlier renders. Faults are fixed in the instrument (CC11/CC1 per phrase, velocity, patch or row, region volume, note lengths, gaps, overlaps, leads, keyswitch timing) or left audible and listed. Per-note bumps as CC11 shapes inside notes are not a fix.
- 2026-11-11 (finale): "The accents are little bit over done now". Isolated accents +1.5 to +2 dB, no track over +3.
- 2026-11-17: "we have a problem across all movements in that i have to turn the volume on my airpods to almost max to really hear all the detail and instruments especially in quiet parts, basically overall the tracks are too soft and in some places there are still instruments with interesting internal lines that are hidden behind the melody or other instruments." Then: "-14 goal please". Delivery is now -14 LUFS (tools/deliver_master.py, loudness loop; guide section "Shared delivery loudness target"). THE INNER LINES ARE THIS CYCLE'S MAIN BALANCE JOB.

## State after c60 (cycles/c60/CHANGES.md, envelope_table.md, faults_table.md, accent_table.md)
- Per-note envelope items 0. Points 3437; strings 0.37-0.61 points/s, winds and brass 0.19-0.38, timpani 0.40.
- Delivered -14.0 LUFS, LRA 11.2, TP -1.2; master -21.1 LUFS, LRA 22.1. Limiter over 6 dB only at 202.7 s (bar 83, 6.7 dB).
- Climax order: master and delivered bar levels hold (160 > 122 > 26 > 170). Delivered loudest 0.4 s: 170 = 160 (-12.2), 26 -12.5, 122 -12.8: the delivery lift raises bar 170's first chord.
- Guards: Violins I 56-90 S robust SD 9 ms, front minus tail -1.5 dB. Theme over celli lower quartile +7.4 (c59 +4.3): the celli are now buried further (-3.9 dB under the theme in bars 15-22; Leg BC notes in the second theme -4.5 dB).
- Faults c59 -> c60: join holes 25 -> 24; re-bow holes 14 -> 8; sags 61 -> 68; pulses 13 -> 12; pitches out 6 -> 9; same-pitch repeats under 3 dB 49 -> 114 (from the new 0.025 s gap at same-pitch long-note joins: judge whether audible).
- Isolated accents: median +1.8, quartiles +1.2 / +2.6, max +9.6; 32 over +3, 22 under +1.
- Left audible: fugato bar 87 5.4 dB under bar 86; timpani f/ff strokes 0.4-4.8 dB under c59 (velocity 117-127 already); Violas step into 168 +4.4 dB; chord-change dips 3.2-6.3 dB at 484, 496, 664, 668, 676; 8 re-bow holes of 8-14 dB; join holes Flute 2 560, Oboe 1 166, celli 286 (16.5 dB), basses 310.
- Not done: final-chord alias Sus MAX copies; basses' 70 % / 0.075 s variant.
- Not verified: doubled attacks at long joins; tam-tam delay; Cello solo 685; Oboe 1 166-169 (+8-10 dB over c59 from a CC11 floor).
- WAV stems exist for c0 and c56-c60.

## What this cycle is for
1. Critic B (main): hidden inner lines. Go through the score bar by bar for every line with independent musical interest that is not the tune: countermelodies, imitative entries, moving inner voices, bass lines with motion, solo wind figures inside the texture, harp and pizzicato figures. For each, measure its level against the tune and its audibility in its best band against everything else (best-band masking, as the finale and scherzo did: they found counter-lines 6-15 dB under the tune). List every line more than about 8 dB under the tune or masked in its best band, ranked by musical importance, with the fix: role span of a phrase or more (edges in rests), CC11 phrase lane on the track's own curve, region volume, or a cut on the part masking it. The tune must stay on top. Include the celli under the theme in bars 15-22 and the second theme (now buried further).
2. Critic C (holistic): compare c60 with c56 (last render with per-note volume), c53 and c0 and with recordings, at the delivered -14 level. Weakest passages now; what still sounds like a machine; three to six changes. Include the delivered momentary climax order (bar 170) and the fix there: a delivery ride row (finale: -2 to -3 dB on ff stabs kept the order) or a mix change; check every crescendo on the delivered mp3 for inversions by the delivery stage.
3. Critic A: the same-pitch repeats count (49 -> 114: audible or not); the sags (61 -> 68); doubled attacks at the new long-chord joins; the remaining join holes and re-bow holes; timpani stroke weight; the fugato bar 87; Oboe 1 166-169; horn slurs onto G#4 / A-flat 4 (scherzo: 9-11 dB hole in the transition sample); wind legato target velocities under 96 (finale: 6-13 dB dips).

## Notes from the other movements
## Scherzo c17 render (symphony/scherzo/reaper-v600/cycles/c17/CHANGES.md)
- Horn 1 anti-phase pitch: Close-led mics (Close -1.4 / Main -5.2 dB) fixed it (mono loss 8-10 -> 0.9-1.5 dB); cost: Horn 1 drier and narrower than Horns 2-4.
- Last held string note: three bow changes 3 s apart, DIV copy on Sus MAX, other part's CC11 lift complete on the change: dips 3.5 / 2.3 / 1.6 dB.
- Accents per track with a short shape: isolated median +1.4; the rest is sample level.
- Crescendo gains to CC11: 59 moved, 25 had to stay (CC11 flat above 104 at ff arrivals). Removing held arrival gains and 17 role rows dropped low winds, basses, celli 3.9-5.6 dB in two sections; 22 section rows went back.
- Slope guard: role edges keyed to the moved note-on, chord rule in CC11: 42 notes -> 8.
- Lock: it sat free 9 minutes while two waiters each listed the other as ahead.

## Scherzo c18 critics (symphony/scherzo/reaper-v600/cycles/c18/reports/)
- Hairpin gain to CC11 with one assumed slope left 66 of 271 arrivals 3-7 dB short. Measured slopes: winds 0.045 dB/unit, strings 0.14, brass 0.14, bassoons about 0 near the top. Convert only where the track's slope there is 0.15 or more; else keep a ramp under the printed hairpin, released at the next printed dynamic or in a rest.
- An accent rule min(8, add_loud) gave 0 on five winds at ff: accented ff arrivals softer than the f bar before. Check accents at ff arrivals.
- One loud sample plus role and accent brought a tutti within 0.2 dB of the summit: check climax order after every level change.
- Leg Slur MAX string joins peak 98-128 ms before the beat at +3.3 to +3.7 dB over the new note's body. (Their proposal, a CC11 dip per join, is a per-note shape: not usable under Dan's rule; look for a velocity, lead or row fix instead.)
- Horn legato at velocity 106-112 sags 8-20 dB after each slur; proposed velocity about 72 (manual p.106).
- Wind/brass detached joins with 50+ ms gaps dip the sum 4.4 dB against 2.5 at 20 ms or less.
- Accent windows of 0.35 s count staccato neighbours as quiet notes.
- Celli pp pizzicato round-robin: reset so the weakest stroke is not on the first bar of each group.

## Finale c19 techniques (SHARED-TECHNIQUES.md items 81-86)
- Chorale whole-note joins: pitch-changing joins overlap 0.04-0.05 s on polyphonic sustain rows (never legato rows); same-pitch 0.025 s gap, staggered by per-track leads sized to rise time: bar-line dips 2.4-5.0 -> 0.2-4.0 dB.
- Horn anti-phase: Opus Channel Routing "Mono From Left" (channelMap 2): mono loss 7.7 -> 0.2 dB, level +0.8; re-balance after (sections +1 to +3 dB).
- Opus row volume knob does not act.
- Per-track entry-lead cuts: tutti spread 134-166 -> 76-121 ms.
- CC16 round-robin reset before each pizzicato pluck: same level per key, then a per-key table.
- Basses' short eighths 70 % of slot, lead 0.075 s: peak +74 -> +39 ms.
- wait_lock.py fix in symphony/mvt3/reaper-v600/cycles/c19/actor_scripts/: compare waiter process start times.

## Dan 2026-11-17 03:12 UTC (main c61 balance job)
"we have a problem across all movements in that i have to turn the volume on my airpods to almost max to really hear all the detail and instruments especially in quiet parts, basically overall the tracks are too soft and in some places there are still instruments with interesting internal lines that are hidden behind the melody or other instruments."
- Loudness: handled in delivery (deliver_master.py -16 LUFS, LRA 12-13, p10 -25 or higher; guide section "Shared delivery loudness target").
- Inner lines: critic B to list every interesting inner line (countermelodies, imitations, moving inner voices, bass lines with motion) that sits more than about 6-8 dB under the melody or is masked in its band, with role spans of a phrase or more, CC11 phrase lanes or region volumes to bring each forward without burying the melody.

## Finale c20 critics (symphony/mvt3/reaper-v600/cycles/c20/reports/)
- fff arrivals had no step: hairpin gains dipped 2.5 dB during the crescendo and released at the arrival while CC was already at the top. Fix: cap crescendos at the ff resting CC, step to the fff CC at the arrival note-on, no hairpin-gain release on fff arrivals.
- Horns "Mono From Left" shifted single pitches up to 7 dB; re-level per pitch; route only horns with negative L/R correlation.
- Stac On Bow basses: hidden release-extension group (+3.3 dB, 1.33 s) and 749 ms main releases.
- Region-gain tool only hits the first key where two keys share a sample.
- Trumpet note ends fall 44-47 dB in 0.2 s (no release trail) against 15-21 dB for horns and trombones.
- Hidden inner lines found by level and best-band masking against the score: accompaniment up to 18.6 dB under the master, counter-lines 6-15 dB under the tune.

## Scherzo c18 render at -14 (symphony/scherzo/reaper-v600/cycles/c18/CHANGES.md)
- At -14 the summit lost its lead (level with the first tutti; led by 1.4 LU at -19.8); limiter 4.9 dB on the summit. Fix climax order in the mix.
- Measured CC11 slopes: only Flute 1, cor anglais, Violins I/II reach crescendo arrivals by CC11 (0.16-0.23 dB/unit); others keep crescendo gain as an envelope ramp released at most 2.8 dB/s.
- Held wind/brass pitch changes overlap 0.04 s; same-pitch repeats keep a 25 ms gap.

## Finale c20 techniques (SHARED-TECHNIQUES.md items 87-92)
- -14 delivery on a master with LRA 22.8: -14.8 LUFS, LRA 12.0; limiter 6-8 dB on fff climaxes; re-measure true peak after the mp3 encode (0.87 once gave -0.8 dBTP).
- fff arrival step: cap crescendo CC lanes at ff resting values up to the arrival's moved note-on, step CC11 +2 (strings, woodwinds) / +6 (brass) with brass CC1 to the top layer, held to the next dynamic; hold hairpin gains through the arrival.
- Basses Stac On Bow RRx9: silence the release-extension group (region gain -60 dB), cap stroke releases at 90 ms: eighths separate 3.7 -> 13.0 dB, peaks on the beat; give back about 2.5 dB by region gain.
- Trumpet release trails sound about 45 dB under the note; raising them does nothing useful.
- Pizzicato per-key region gains after a CC16 reset per pluck: range 7.2-9.3 -> 2.3-5.5 dB; keys sharing a region need equal values.
- A role row holding a track down cancels a CC1 rise; remove the row first.

## Finale c21 critics (symphony/mvt3/reaper-v600/cycles/c21/reports/)
- At -14: delivery ride rows on climaxes (-2 to -4.5 dB), lift ratio 2.0 -> 1.8, loudness loop to land at -14 (-13.9, LRA 11.5, limiter 6.0/3.5/3.1). Mix trims mostly undone by the top ride.
- CC1 lifts often land on a dynamic-layer plateau (+0.4 dB or less): use CC11 or role rows.
- Brass staccato at mf cut twice (low CC11 + low velocity): hold CC11 high on brass short rows, velocity carries dynamics.
- Trumpet f/ff sustain release 178 ms: set 300 ms.
- Cor anglais legato swell is in the patch (465 ms attack).
- Harp harmonics / glissandi: Harp KS Master has Harmonics and Gliss rows (check ours).
- ff/fff bass loses 4 dB below 90 Hz on a Tremolo row without region gain.
- 1-2 dB render-to-render changes on unchanged data can be a different round-robin take.

## Movement II c57 render (symphony/mvt2/reaper-v600/cycles/c57/CHANGES.md)
- Top ride 3:1 gave LRA 10.6 and lifted a pre-climax bar level with the climax; 2:1 gave 12.0. Climax margin 1.7 -> 0.6 dB, limiter 6.0-6.6 dB on climax bars.
- Bow pieces on undoubled exposed sections dip 6-10 dB: double them.
- Change leads by half the measured error.
- Hidden inner lines 9-27 dB under the melody (violas pizz, harp, bassoons/bass clarinet, basses pizz).

## Scherzo c19 critics (symphony/scherzo/reaper-v600/cycles/c19/reports/)
- Horn 1 legato A4 -> G#4 leaves a 9-11 dB hole at +0.30 s in the transition sample at any velocity: play the G# on Sus MAX without overlap. Check our horn slurs onto G#4 / Ab4.
- String Leg Slur MAX swell peaks about 70 ms after note-on, out of CC11 reach: lower the TLeg region volume 1.5-2.5 dB.
- Best-band masking found hidden inner lines 7-10 dB under the tune.

## Finale c21 techniques (SHARED-TECHNIQUES.md items 93-99)
- Top ride 2:1 instead of 3:1: LRA 11.5 -> 12.4 at the same limiter load.
- Climax order at -14: delivery ride rows (final chord -3.5, fff arrival -3 / -5.5, ff stabs -2 to -3): final-chord limiting 7.8 -> 5.7 dB, printed order kept. Cutting single instruments does not help.
- Brass short rows: hold CC11 at the ff resting value on Stac / Marc Shrt, velocity carries the dynamic: mf staccato +5.7 dB. Check per track (horns: one note group +13.5).
- Trumpet KS Master f/ff sustain releases 178 ms -> set to 300 ms.
- KS Master trigger keys can be moved in the Opus state (harp Harmonics / Gliss on keys 112/113). KS Master Sus RR plays 5-7 dB over Harp Sus RR.
- Cor anglais legato bloom: Sus MAX on held notes fixes it; TLeg +4 dB does not.
- CC11 fall before string re-bows: weak.

## Finale c22 critics (symphony/mvt3/reaper-v600/cycles/c22/reports/)
- Delivery ride rows can invert crescendos and ff arrivals: check every crescendo on the delivered mp3.
- CC caps below the running level flatten crescendos.
- Trumpet 300 ms release fills re-tongue gaps (240 ms proposed).
- Move CC11 re-tongue falls with any note-on leads.
- Wind legato targets at velocity 71-90 dip 6-13 dB: floor about 96.
- Harp KS Master lacks the velocity-to-volume processor.
- Compare band power, not summed energy over unequal windows.

## Instructions to the critics
- SAFETY: read-only. Never run tools/build_reaper.py, tools/render_cycle.py or tools/deliver_master.py into ROOT paths (a copy into your scratch folder is fine), never exec build_reaper.py whole (cut the source before ENV_LUA if you need its functions), never touch REAPER, ~/.rpr-bridge or another movement's folder. Scratch files and scripts only under cycles/c61/critic_scripts/<SLOT>/. No subagents. No cache over 1 GB.
- Propose instrument-side fixes only. Any proposal that puts a per-note value or a fitted row on the track volume envelope will be discarded.
- Every proposal: measured size now, expected size after, file and key to change. Size CC11 changes from the track's own curve.
- Hand-back at most 40 lines; full report to cycles/c61/reports/<SLOT>.md.

## Coordinator decisions on the c61 critic reports (actor: this is the work order; values in reports/A.md, B.md, C.md)

Priority order. Range-test what a critic marks as inferred. Drop from the bottom if time runs short and list what was dropped. Do not touch: the 0 per-note envelope state, the theme leads on Violins I, the celli Leg BC MAX -4 region gain, the ff trims, the WIND_DETACH long form, the c60 re-bow list, the fugato velocities with the flat lane at 72, the accent values, brass legato velocities, timpani beat/off-beat velocities, the loudness and true-peak loops, the cello-solo and coda ride trims.

1. Inner lines (B, all of findings 1-4), as role rows of a phrase or more with edges in rests: celli [56,88] -2.0 -> +1.0 and new Bassoon 1 [76,88,+2]; celli [104,128] -3 -> +2.5; delete celli [360,372,-2,0.5]; celli [360,408] -3 -> -1; new celli [552,568,+2]; new celli and Bassoon 1 [664,675.5,+3]; violas [384,408.1,+5], [552,568,+2], [645,664.2,+3], [680,695.5] -3 -> +2; Clarinet 2 [464,479.07,+3]; delete Clarinet 1 [628,644,-3]; delete Cor anglais [682.75,689,-2.5,0.5]; new Clarinet 1 [606.5,612.1,+3]; Violins II CC11_ADD +5 units at 107-110 (qn per B). Range-render bars 15-32, 88-102 and 156-174 first. Guards: theme over celli lower quartile 3.9 or more in bars 15-22 (if the celli role costs it, stop the celli at the value that holds 3.9); the tune stays on top in every passage (report tune minus loudest other line per changed span). Report each line's K-dB under the tune and best-band figure before and after.
2. Delivery (C 1-2): tools/deliver_master.py TOP_RATIO 3.0 -> 2.0 (TOP_ABOVE stays -10); build/score_config.py RIDE_TRIMS append [(675.8,0),(676.0,-2.5),(679.0,-2.5),(679.9,0)], [(436,0),(440,-3),(448,-2),(456,0)], [(616,0),(620,-2),(624,-1),(627,0)]. Check on the delivered mp3: loudest 0.4 s order 160 > 122 > 26 > 170, no crescendo inverted, LRA, limiter per passage over 6 dB, p10. Re-check after item 1 (B's changes add about +0.17 dB at bar 160).
3. Oboe 1 (C 3, A 5): region gain Leg Slur MAX pitch 76 -8 on the layer that actually sounds at CC11 54 (check which; a dyn filter did not act on Horn 4 in c59); CC11_LANE["Oboe 1"] [(164,58),(165.85,58),(167.9,38),(168.9,36)]. Bar 146 within 1.5 dB of c56.
4. CC11 steps keyed to the moved note-on (A 2), generic in the score_to_parts lane writer: the rise at the moved note-on, the phrase-end taper ending at the next phrase's moved note-on. Report the count of notes starting 8 units or more under their own level (now 55) and celli 620.
5. Cor anglais qn 26 G4 -> G#4 dip (A 1): range-test ART_SPANS Sus MAX 25.8-26.95 against VEL_SET 26.0: 115; adopt the smaller dip. Celli qn 286: SUS_ENTRY_AT += [286.0].
6. Fugato drop into bar 88 (A): the two +3 celli roles ending at 348 / 348.5 and the CC11 step 78 -> 64 take the mp twice; keep one (the CC11 step) and end the role in the rest after 348.5 with a 2 s ramp, or end it later. Bar 88 should fall by the printed amount only.
7. Timpani stick (A 4): range-test mic_db Close -14 -> -8 on the timpani for the ff passages; adopt if the 0.7-3 kHz attack rises with no boom. The Hrd KS alias only if cheap.
8. Optional, only if time: PHRASE_SHAPE["end"] -12 -> -8; faults tool: count long-join same-pitch gaps separately and widen the legato-dip window to +0.26 s.
Not adopted: C 4 (raising the second-theme celli and Horn 1 lanes): B measured the second-theme tune +3.3 / +4.2 dB over the rest and not buried; B's measure governs. C 6 (EQ shelf): not this cycle.

Report in the hand-back: per-note envelope items (0), fitted rows (0), points per second, guards, the inner-line table before and after, delivered I / LRA / TP / p10 / limiter per passage over 6 dB / loudest-0.4 s climax order / crescendo inversions, faults table c60 -> c61, master bars more than 1.5 dB off c60 with cause, faults left audible, what was dropped, what is not verified. A/B clips c60 then c61 in cycles/c61/ab/: bars 15-23, 97-102, 156-162, 167-174, master and the inner-line stem each.

## Actor constraints
- Shared REAPER lock: wait_lock.py with a running background waiter (check it with pgrep after starting; keep it alive); never take or break the lock by hand; tie rule: the folder path that sorts first goes first.
- Restart REAPER immediately before the main render. Shell chains stop and keep the lock on any failure (as c60's p5.sh).
- First range render after a rebuild is unusable: render each variant twice, keep the second. State guard at the start, after range renders and before the full render; rebuild stale tracks in full. Restart REAPER between batches of rebuilds.
- Disk: keep a 10 GB floor after the render; delete WAVs only inside cycles/c60 and c61 rangetest / variants folders if needed.
- Scripts under cycles/c61/actor_scripts/. Write cycles/c61/rendered_build/parts.json as rendered.
- No score change. No commit. Nothing published. No REAPER preference changed. Nothing in ~/.rpr-bridge modified. No subagents.
- Update HISTORY.md, LEARNINGS.md, cycles/c61/CHANGES.md. Hand-back at most 40 lines. Do not end your turn while the waiter or a render is running: wait for it.

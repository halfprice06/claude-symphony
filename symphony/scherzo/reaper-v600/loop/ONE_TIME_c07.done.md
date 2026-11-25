# One-time task for the c07 actor: research batch 5 (Dan's standing OK to adopt research findings, 2026-11-08)

First, finish anything c06 left in loop/ONE_TIME.md, if that file still exists.

Then apply research batch 5: FINDINGS.md Part 5, from the Goldsmith Mulan and Hisaishi Howl's Moving Castle Cubase projects with VSL Synchron. The full text is in loop/RESEARCH-FINDINGS-c07.md, from line 191. The default is to adopt; drop an item only with measured evidence, recorded in LEARNINGS.
1. Hall sends: none, or -16 dB or lower, on low brass (trombones, bass trombone, tuba), bassoons, contrabassoon and basses. About -10 dB relative on everything else. Percussion unchanged. Reconcile this with c06's EW/Duc send values and record the choice.
2. A/B test: a 1.8-2.3 kHz low-pass on the hall return(s), with 25 ms pre-delay.
3. Dynamics shapes: crescendos rise early and then settle; diminuendos fall on the last held note; winds and brass may fade nearly out before rests.
4. A/B test: narrow brass, with horns left at 15-47% width and trumpets right at about 43%.
5. A detailed tempo map: changes on about 20% of beats, and phrase breaths more than 15% slower. The scherzo is fast and rhythmic, so keep it subtle in the main sections. Use it at phrase ends, the trio's breaths and the printed rit./fermata. Measure with the attack probe.
Keep the 60-100 ms repeated-note gaps.

For each A/B: render the test variant as stems if possible, or decide on a simulation, and record the numbers. When done, rename this file to ONE_TIME_c07.done.md.

Research batch 6 (FINDINGS.md Part 6, from Lorne Balfe's MIDI sketches; same file, see "# Part 6"). Item 2 matters most for the scherzo:
1. Phrase shape depends on the music. Builds to a climax enter near zero and peak at the phrase end. Accented brass and fanfares enter at the top and fall 15-25 by the end of a long note. Lyrical lines keep the centred arch.
2. Ostinato velocity: in repeated short-note figures, each beat or half-beat group falls 15-17 velocity steps from first note to last (e.g. 104, 101, 95, 87), with ±5-7 random variation (seeded) and strong beats accented by 20-25 steps. Two layers of one figure can alternate accents (1 and 3 against 2 and 4). Apply this to the scherzo's staccato theme, the repeated eighths and the accompaniment figures. Scale it to the printed dynamic, and measure the dips and accents before and after.
3. Instruments doubling a line share one dynamics curve.
4. A/B test: brass timbre (the CC that drives the dynamic layers) 25-35 under its level CC, and strings timbre about 15 over.
5. Spiccato note length about 60% of the slot.

Batch 7 (Part 6 rewritten, commit b01434e6; the copy in loop/RESEARCH-FINDINGS-c07.md is refreshed). It supersedes batch 6 where they differ:
- DROP batch 6 item 4 (the brass/strings timbre offset). Ride the level lane in the same shape as the timbre lane.
- Driving music at 105-150 bpm starts high and falls, or peaks early (0.05-0.30 of the phrase). The scherzo's main sections are this kind of music. Builds peak at the end; lyrical lines (the trio) keep the centred arch.
- Short-note velocity by position in the beat, 15-25 steps between the strongest and weakest note. In running 16ths, either the pattern beat > "and" (about -10) > the two 16ths in between (-20 to -25), e.g. 95, 72, 83, 72, or a fall of 15-17 across each group. In the scherzo's 3/4 at dotted half = 88, apply the same idea to the eighths within each beat and to beat 1 against beats 2-3. Add ±5-7 seeded random variation.
- Spiccato length 50-62% of the slot.
- Doublings share one dynamics curve.

# One-time notes for the cycle 17 actor

The cycle 16 actor received all of these as messages. Read `cycles/c16/CHANGES.md` first and skip what it already did. `loop/ONE_TIME_c16.md` items 5-7 (Dan's rule, finale techniques) still apply.

## 1. Dan on accents (2026-11-11 23:37Z, after the finale's c17): "The accents are little bit over done now"

Target here: median accent over neighbours +1.0 to +2.0 dB, no track over +3 dB (sf / sfp larger as printed). Finale c18 shape: about half the bump, hold 0.05-0.08 s, back by 0.20-0.25 s (a 0.15 s hold with 0.45 s return makes a bulge 60-450 ms after the front), scaled 0.75 / 0.6 when 9+ / 16+ staves are accented together. Report median and 90th percentile per track. c16 left Flute 1 +3.6, Clarinet 1 +5.0, Bassoon 1 +3.1 over the limit, and strings at ff (+0.8), violas, basses, Flute 2 with almost none.

## 2. Movement I c57 / c58 (`symphony/mvt1/reaper-v621/cycles/c57/CHANGES.md`, `cycles/c58/reports/`, read only)

- Bar-length level rows fitted to the old per-note layers are a stopgap. Sort ours by cause (mapping, sample level, bar means of removed shapes, real phrase decisions): sample level goes to region gains, bar means are deleted, phrase decisions stay.
- Dynamic trims step on [score onset - 0.125 qn, score onset] but the note-on is one lead earlier: key the step to the moved note-on, wholly in the rest.
- Slow shapes: drop any with a segment over 3 dB/s that is not a printed dynamic change or fade.
- Velocity does nothing on sustain rows (0.0 dB per 10 units); Leg Slur MAX fronts gain 0.45-0.85 dB per 10 on upper strings only. Woodwinds: CC11 88-98 is a plateau.
- Re-bow holes come from the slow Sus MAX bloom, not the gap; raising the no-split limit removes re-bows.
- Theme timing: Sus MAX with per-note leads gave 9 ms spread and no sag; Sus Marc LITE without lifts sags 7.5 dB.
- Repeated quarters on Sus MAX under 0.4 s got no lead and speak 67-130 ms late. Legato overlap should be set in seconds.
- A "drive" phrase shape on held notes made horns sink 7-12 dB over held pedals; cap it to phrases with mean note length under 2 qn.

## 3. Movement II c55 / c56 (`symphony/mvt2/reaper-v600/cycles/c55/CHANGES.md`, `cycles/c56/reports/`, read only)

- A CC7 / CC11 lane fitted together with a removed envelope row breaks; check every such lane.
- Median legato join sags 2-3 dB for 0.25 s and reference lanes are flat there: leave those; fix soft starts of 6 dB or more.
- S readings moved with no timing change because on-beat envelope steps had set the level onset.
- Transition bursts were all on Leg Slur MAX at velocity 124; EastWest's demo uses legato velocity 92-98.
- A held note whose first piece is on Leg Slur MAX leaves the next piece 2.2 dB lower.
- Tremolo strings and basses do not repeat between identical range passes.

## 4. Finale c17 / c18 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` items 70-75; `cycles/c18/reports/`, read only)

- Guard by slope: no unprinted move steeper than 3 dB/s and 1.5 dB or more inside a sounding note.
- Tongued-join gap floors: 0.09 s trumpets / tuba, 0.12 s horns / trombones, 0.068 s woodwinds, 0.085 s oboes, capped at 40-50 % of onset distance.
- Timpani: right-hand keys (+24) are 4-5 dB louder than left at equal velocity; envelope can be folded into CC7.
- Basses "Stac On Bow RRx9": no velocity response at 80-100; beat weight by CC11 offset on off-beats (-22 units = 2.0-2.7 dB); half amplitude at 95 ms, peak at 140 ms.
- Pizzicato velocity crosses a sample layer near 47 (then an 8-13 dB step).
- Bar-line dips in sustained tutti writing come from many tracks ending together 20-50 ms before the bar line: stagger note ends.
- When a note-on moves earlier, move its keyswitch and CC16 reset too.

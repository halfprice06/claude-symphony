# One-time notes for the cycle 24 actor

The cycle 23 actor received item 1 as a message while it worked. Read `cycles/c23/CHANGES.md` first and skip what it already did. Items of `ONE_TIME_c22.md` not done by c22 / c23 carry over.

## 1. Finale c25 techniques 117-124 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only)

117. Celli "Detache": velocity picks no layer; CC11 crossfades its mp and ff groups. An f bass line inside the crossfade swelled; played at the ff group's CC11 with a -6 dB passage level: back-minus-front +2.8 to -0.5 dB, repeats separated 1.5-6.6 dB.
118. Negative: Violins I "Sus Marc LITE" CC11 is not 20 log10 (-5 dB asked took fronts 8.5 dB, bodies 14 dB down); removing a +4 dB region gain lowered the body 4 dB, the marcato front only 0.6.
119. Timpani fff roll after a crescendo: a dB-linear CC7 ramp from the pre-arrival level to the target over the printed decrescendo kept the roll 4-7 dB louder after the arrival.
120. Crescendo gains held into an ff downbeat cover an entering tune: ending them at the printed mark (at most 2.8 dB/s) with +2-3 dB on the tune took tune-minus-rest -6.8 to -3.8 dB.
121. Basses' pp pedal re-bow blooms: a CC11 counter-shape per bow (-14 units from 0.35 to 1.6 s, back by 2.6 s) took the bloom +5..+9 to +1.6..+4.1 dB.
122. Accent bumps under a crescendo ceiling (cc_cap toward an arrival) are removed by the cap; capping only the resting lane brought a missing accent back (+3.8 dB).
123. Mono From Left on all four horns: Horns 2 / 4 stem correlation 0.54 / 0.65 to 0.98, notes losing over 2 dB in mono 21 to 0.
124. 40in Ludwig Bass Drum: +6.7 dB in 30-90 Hz over the 36in at the same velocity.

## 2. Finale c26 critic findings (`symphony/mvt3/reaper-v600/cycles/c26/reports/`, read only; 1, 3, 6 sent to the c23 actor)

1. Dan's rule was still broken in the finale: 30 fader steps inside sounding notes, mostly a "held decrescendo" rule releasing -3 dB at the hairpin end inside the next note. Check by slope after every build (over 3 dB/s, 1.5 dB or more, inside a sounding note), including role edges, player-count marks, crescendo-gain releases. Our 9 slope-guard notes must be named and removed where possible.
2. A 160 Hz loud_eq bell on celli lifted release ring 2.5 dB and shrank stops.
3. Delivery 5 s lift smoothing plus ride rows on ff bars flattened ff arrival steps on the mp3; ramp ride rows over the crescendo instead.
4. A timpani fff roll entering with CC7 from a previous decrescendo started 9 dB soft.
5. Celli "Detache" after a CC16 reset: first round-robin take rises 1.4-1.8 dB, second 8.9-10.3; place resets so repeats land on the second take.
6. Soft woodwind runs: notes after a soft (v53) first note drop 6-11 dB.

## 3. Room-noise bed in the delivery (coordinator relay: approved by Dan for all movements; sent to the c23 actor)

Spec `mockup-kit/README.md` "Room-noise bed in the delivery": synthetic hall-air noise at -60 LUFS integrated, after the limiter and before the mp3 encode; pink with extra fall above 2.5 kHz, low cut 84 Hz, partly correlated stereo, fixed seed. Reference: Movement I's `tools/deliver_master.py` (env DELIVER_ROOM_BED_LUFS). Keep it in every delivery from c23 on.

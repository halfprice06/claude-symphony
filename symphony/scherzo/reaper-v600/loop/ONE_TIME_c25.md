# One-time notes for the cycle 25 actor

The cycle 24 actor received item 1 as a message while it worked. Read `cycles/c24/CHANGES.md` first and skip what it already did.

## 1. Finale c27 critic findings (`symphony/mvt3/reaper-v600/cycles/c27/reports/`, read only)

1. Gate should FAIL any fader change of 1.5 dB or more in a note's first 0.35 s; role edges crossing moved note-ons caused 67 such notes there; place role ramps in the rest before the moved note-on.
2. Consider moving dynamic trims into CC7 (range-test first); do not rate-limit printed hairpins.
3. U-shaped trim tables move against printed hairpins on held notes.
4. Horn "Stop Sus" ignores CC1.
5. CC11 at 18-32 barely responds; use CC7 for soft passages.
6. Unison doubling on a non-legato row halves legato joins.
7. Check CC11 headroom before lifting.

## 2. Movement I c62 notes (sent to the c24 actor)

Movement I's `tools/deliver_master.py` now has the room bed (DELIVER_ROOM_BED_LUFS, default -60, "off"); our bed should match it. A guard moved join ramps up to 19 qn back in a first build there (celli ff +9 dB): limit how far a guard may move a ramp.

## 3. Finale c26-c27 techniques 125-143 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only; main ones sent to the c24 actor)

135. Dynamic trims out of the envelope: envelope at gain + the largest trim, CC7 = 127 x 10^((trim - largest)/20); CC7 is 20 log10 on HO woodwind and brass KS Masters.
136. Role / passage-level edges: ramp in the rest before the note nearest the edge (within 1 qn); with no rest, envelope edge to the nearest rest and CC7 holds the difference (cap 16 qn). A first-0.35 s gate found 187 moves older gates missed.
137. Stopped horns ignore CC1: a CC11 ceiling over the decrescendo (127 to 50) made them fall 7-14 dB.
138. Held soft crescendo on CC1-layered brass / clarinet: start CC11 4 dB low, ramp back by the hairpin end: +3..+4.5 dB rise.
139. Late soft legato string heads: CC11 +10 from 0.06 s before the note-on to +0.25 s, gone by +0.45 s: attacks -12..+115 ms (were +140..+220).
140. Violins II "Sus Marc LITE" (v92, lead 0.085 s) works once the CC11 ff step is 0.06 s before the moved note-on.
141. A woodwind doubling a muted trumpet: "Sus MAX" with each note led 0.10 s and crossfaded beats "Leg Slur MAX".
142. Negative: basses' pp re-bow holes do not respond to a 0.10 s lead or a CC7 counter-shape.
c26: held-decrescendo levels released at the led note's moved onset removed 22 in-note steps; a 160 Hz loud_eq bell on celli cost stops until the EQ span ended before the cut-off.

## 4. Finale c29 critic findings (`symphony/mvt3/reaper-v600/cycles/c29/reports/`, read only; sent to the c28 actor)

1. Exposed brass legato on "Leg Slur MAX" leaves 10-12.5 dB holes for 140-330 ms at each slurred note change, second note 180-250 ms late; the sustain row with each note led 0.10 s and overlapping the next (finale 141) has no holes.
2. A printed string harmonic played as a full-section vibrato note masked a p flute solo: CC1 0 (manual p.92) plus a role cut.
3. A delivery ride row stepping down exactly at a crescendo's ff arrival turned +2.3 dB on the master into +0.3 on the mp3: start such rows after the arrival bar.
4. "Mono From Left" on all horns with near-identical pans makes the section one mono point: spread pans.
5. The hard-stick timpani patch plays through printed soft / medium-stick passages too.
6. Envelope at exactly +24.0 dB (REAPER's ceiling): build check at +23.5, excess into CC7.

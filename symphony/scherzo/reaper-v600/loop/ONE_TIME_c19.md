# One-time notes for the cycle 19 actor

The cycle 18 actor received item 1 as a message while it worked. Read `cycles/c18/CHANGES.md` first and skip what it already did.

## 1. Finale c19 techniques 81-86 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, its `cycles/c19/CHANGES.md`; read only)

81. Chorale whole-note joins: pitch-changing joins overlap 0.04-0.05 s on polyphonic sustain rows (never legato rows); same-pitch joins keep a 0.025 s gap, staggered by per-track leads sized to each track's rise: master bar-line dips 2.4-5.0 to 0.2-4.0 dB (8 of 10 within 3).
82. Horn L/R anti-phase in the 1FH Main pair: Channel Routing "Mono From Left" (channelMap 2): mono loss 7.7 to 0.2 dB, level +0.8 dB, keeps the Main mics (our Close-led fix made Horn 1 drier); notes that used to cancel return at full level (sections +1 to +3 dB): re-balance after.
83. Negative: the Opus row volume knob does not act; use region volumes.
84. Tutti entries: per-track entry-lead cuts for the tracks that always speak first (Oboe 2, Flute 2, trombones, bassoons, Horns 3-4): spread at 5 tutti chords 134-166 to 76-121 ms.
85. CC16 round-robin reset before each pizzicato pluck: a key plays the same level every time, leaving a per-key table to fit.
86. Basses' short-row eighths: 70 % of the slot, lead 0.075 s: peak +74 to +39 ms after the beat; separation unchanged (dip 3.7 dB).
Lock waiter fix: `symphony/mvt3/reaper-v600/cycles/c19/actor_scripts/wait_lock.py` compares waiter process start times; the old logic caused the 15-16 Nov deadlock.

## 2. Dan (2026-11-17 03:12Z, all four movements): too soft, inner lines hidden

"we have a problem across all movements in that i have to turn the volume on my airpods to almost max to really hear all the detail and instruments especially in quiet parts, basically overall the tracks are too soft and in some places there are still instruments with interesting internal lines that are hidden behind the melody or other instruments."

Sent to the c18 actor as a priority: raise delivered loudness (Movement I's shared target in mockup-kit if present; else provisional -16 LUFS integrated, LRA 10-12 LU, -1.0 dBTP, quiet passages lifted most, limiter at most 3 dB, climax order kept) and bring up hidden inner lines by roles, region gains, CC11 or mic mix. Check what c18 did in `cycles/c18/CHANGES.md` and continue.
Shared target (Movement I, `mockup-kit/README.md` "Shared delivery loudness target"; sent to the c18 actor, replaces the provisional one): delivered mp3 -16 LUFS integrated (±0.5), -1.0 dBTP, LRA 12-13 LU, p10 short-term -25 LUFS or higher; check climax order on the delivered file (momentary max per bar). Reference `symphony/mvt1/reaper-v621/tools/deliver_master.py` (knee 7 dB under p95, top ride 10 dB under p95 at 3:1, limiter -1.0 dBFS). Fix climax order in the mix with per-dynamic trims. Hidden inner lines: a balance job for the c19 critics.

## 3. Finale c20 critic findings (`symphony/mvt3/reaper-v600/cycles/c20/reports/`, read only; items 1, 2, 3, 5, 7 sent to the c18 actor)

1. Shared delivery: limiter ceiling 0.891 missed -1.0 dBTP by 0.1 dB (use 0.87); top-ride ratio 3.0 dropped LRA to 11.3; short ff bars rose above an fff; the limiter took 4-5 dB on the final chord.
2. fff arrivals had no step: hairpin gains dipped during the crescendo and released at the arrival while CC was at the top. Cap crescendos at the ff resting CC, step to the fff CC at the arrival note-on, no hairpin-gain release on fff arrivals.
3. "Mono From Left" on horns shifted single pitches up to 7 dB; re-level per pitch; do not route horns with merely low (not negative) L/R correlation.
4. "Stac On Bow" basses row has a hidden release-extension group (+3.3 dB, 1.33 s) and 749 ms releases a cap may miss.
5. The region-gain tool only hits the first key where two keys share a sample (celli pizzicato 47/48, 43/44).
6. Trumpet note ends fall 44-47 dB in 0.2 s (release trails missing).
7. Hidden inner lines found by level and best-band masking against the score (counter-lines 6-15 dB under the tune).

## 4. Dan (2026-11-17 03:27Z): "-14 goal please"

Shared delivery target is now -14 LUFS integrated (±0.5); the rest of the shared spec stays. Sent to the c18 actor.
Final spec (README updated 03:30Z): -14 LUFS ±0.5, -1.0 dBTP (ceiling 0.87), LRA about 12, p10 short-term -23 or higher, climax order on the delivered file; report limiter gain reduction passage by passage (Movement I c59: 4-6 dB on its five highest peaks).
Limiter gain reduction: align for the 5 ms look-ahead (240 samples at 48 kHz); unaligned the finale over-read single peaks by 5+ dB.

## 5. Finale c20 techniques 87-92 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only; delivery, fff step and item 92 sent to the c18 actor)

87. Shared -14 LUFS delivery on a master with LRA 22.8: -14.8 LUFS, LRA 12.0, p10 -23.1 at ceiling 0.87; limiter 6-8 dB on fff climaxes; -14.0 would need about 0.6 dB more. Re-measure true peak after the mp3 encode (0.87 gave -0.8 dBTP once).
88. fff arrival step: cap the crescendo's CC lanes at ff resting values up to the arrival's moved note-on, step CC11 +2 (strings, woodwinds) / +6 (brass) with brass CC1 to the top layer, held to the next dynamic, hold hairpin gains through the arrival: strings -1.4 to +0.1 dB, brass +2.4..+5.2 to +4.7..+8.4 at the downbeat.
89. Basses "Stac On Bow RRx9": silence the release-extension group (region gain -60 dB), cap stroke releases at 90 ms: hammered eighths separate 3.7 to 13.0 dB, peaks on the beat; costs about 2.5 dB (give back by region gain).
90. Negative: trumpet release trails +6 dB change the drop after a stop by exactly 6 dB; the trails sound about 45 dB under the note.
91. Pizzicato per-key region gains after a CC16 reset before each pluck: range 7.2-9.3 to 2.3-5.5 dB; keys sharing a region need equal values.
92. Negative: clarinet CC1 +6 did nothing where a role row still held them down; without the -2.5 dB row they rose 3 dB.

## 6. Finale c21 critic findings (`symphony/mvt3/reaper-v600/cycles/c21/reports/`, read only; 1, 2, 4, 8 sent to the c18 actor)

1. At -14 climax peaks are tutti sums: cutting one family 3-4 dB moved the limiter 0.1-0.7 dB; the delivery top ride undoes about 2/3 of mix trims. Worked: delivery ride rows on climaxes and ff stabs (-2 to -4.5 dB), quiet-lift ratio 2.0 to 1.8, a loudness loop setting the pre-limiter target so the mp3 lands at -14. Climax margins of 1 dB or more were not reachable at -14 with 6 dB of limiting or less.
2. CC1 lifts often land on a dynamic-layer plateau (+0.4 dB or less); lift with CC11 or role rows.
3. Brass staccato at mf can be cut twice (low CC11 + low velocity): hold CC11 high on brass short rows, let velocity carry dynamics.
4. Trumpet f / ff sustain release 178 ms cuts note ends; set 300 ms.
5. The cor anglais legato swell is in the patch (465 ms attack).
6. Harp harmonics / glissandi were plain plucks on "Harp Sus RR"; "Harp KS Master" has Harmonics and Gliss Technique rows. Check our harp.
7. ff / fff basses lose 4 dB under 90 Hz moving to a Tremolo row without region gain.
8. 1-2 dB render-to-render changes on unchanged data can be a different round-robin take; do not fit levels to one render.

## 7. Movement II c57 results (`symphony/mvt2/reaper-v600/cycles/c57/CHANGES.md`, read only)

Delivery top ride 3:1 gave LRA 10.6 and lifted a pre-climax bar level with the climax; 2:1 gave 12.0. Limiter 6.0-6.6 dB on climax bars; climax margin 1.7 to 0.6 dB. render_cycle's memory gate refused at 29 GB compressed; a REAPER restart fixed it. Bow pieces on undoubled exposed sections dip 6-10 dB: double them. Change leads by half the measured error (one-measurement sizing overshoots).

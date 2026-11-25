# One-time notes for the cycle 21 actor

The cycle 20 actor received item 1 as a message while it worked. Read `cycles/c20/CHANGES.md` first and skip what it already did.

## 1. Finale c22 techniques 100-105 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only)

100. Harp KS Master has no Velocity->Volume path (Harp Sus RR does): copying the MidiVelocity processor and its connection into the state restores velocity dynamics. Check any KS Master swap.
101. Negative: woodwind legato velocity floor 96-116 left post-transition holes unchanged; a 200 ms attack cap on legato-target sustain groups made them worse.
102. Negative: moving a brass re-tongue CC11 fall to just before a led note-on did not deepen repeat dips; Opus smooths CC11 over 120 ms (fadeTime) in these patches.
103. Delivery: ride a crescendo's earlier bars down (-1.5 dB easing to 0 at the arrival), not its last bar: +1.5 dB of crescendo on the mp3, limiter unchanged.
104. Horn legato targets with a +0.3 s hole on "Sus MAX" 0.06 s early with no overlap: holes of 6 dB or more 2 to 0, front not brighter.
105. Trumpet sustain release 240 ms at f / ff with a 0.1 s gap and a 12-unit fall: repeat dips 4 to 5-6 dB; trumpet staccato velocity is steep (4 steps about 6.6 dB).

## 2. Finale c23 critic findings (`symphony/mvt3/reaper-v600/cycles/c23/reports/`, read only; sent to the c20 actor)

Brass KS Masters smooth CC1 / CC11 over 120 ms, so repeated-note separation comes only from note-off gaps (0.08-0.12 s about 7 dB, 0.12-0.20 s about 9 dB). Read velocity layer tables before velocity changes (7 dB jumps at layer boundaries). The LegatoSpeed script's SUS_GROUP_SUBSTRING "Obs" / "CLs" do not match group names "OBs" / "Cls"; SSOFFSET untried. fff arrivals step up more on the -14 mp3 with a 0.05 s caesura and no speeding into them. Audit section-wide negative role rows. Render from before qn 0; trim only for metrics.

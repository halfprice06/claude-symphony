# One-time notes for the cycle 22 actor

The cycle 21 actor received item 1 as a message while it worked. Read `cycles/c21/CHANGES.md` first and skip what it already did.

## 1. Finale c23 techniques 106-111 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only)

106. Brass same-pitch whole-note repeats in a slow chorale: 0.12 s gap (winds 0.08 s) and no CC11 fall: dips median 2.8 to 5.5 dB. Brass KS Masters smooth CC11 over 120 ms, so a fall ending near the note-on starts the new note low.
107. Woodwind / brass legato targets with an early hole (0.1-0.25 s) on the sustain row 0.06 s early with no overlap: all 8 treated targets under 6 dB.
108. Negative: woodwind LegatoSpeed SSOFFSET 11025 made legato holes worse; a celli release-trail cap of 80 ms did not shorten the linger at tutti stops.
109. Brass staccato velocity layers (1TP "Stac DblTng RRx9": 1-54 / 55-75 / 76-94 / 95-127): place velocities by layer; v95 instead of v92 is about +6.5 dB.
110. Delivery at -14: ride rows lowering the bars before each fff gave arrival steps +3.4 / +1.2 / +1.1 dB with the limiter at 5.9; final chord drop at +0.3 s 7.8 dB on the mp3 (16.1 master), a -8 dB tail ride restored 15.6.
111. Negative: a 0.05-0.06 s caesura and a 0.06 s string lift before an fff did not dip the master. Keeping 0.30 s of pre-roll before qn 0 in the delivered mp3 kept the opening chord's attacks (Horn 1 +131 to +26 ms).

## 2. Finale c24 critic findings (`symphony/mvt3/reaper-v600/cycles/c24/reports/`, read only; sent to the c21 actor)

1. In brass and clarinet KS Masters (1FH, 1TP, 1TB, 1TU, CL) CC11 scales volume as 20 log10(CC/ref), not 40 log10; offsets sized with 40 deliver half the planned dB (Horn 3 46 to 73 measured +4.0 dB).
2. Accented ff tutti chords on "Sus MAX" swell, peaking about 212 ms after the beat; test "Sus Marc LITE" on chord notes (mind its region gain).
3. The -14 delivery top ride (10 dB under p95, 3 s) squeezes f against ff to about 1.4 dB; simulated fix: 6 dB under p95, quiet-lift 2.1.
4. Brass re-attack gaps of 88-122 ms give a clear fresh attack.
5. Unslurred basses on "Leg BC MAX" swell late on half notes; "Sus MAX" is flat.

## 3. Shared delivery spec updated (Movement I, `mockup-kit/README.md`, "Decision: climax margin before loudness range"; sent to the c22 actor)

Priority on the delivered file: (1) -14 LUFS ±0.5, -1.0 dBTP; (2) printed summit leads every rival ff / fff by 0.5 LU or more (loudest 0.4 s per bar), other climaxes in printed order; (3) printed f to ff steps 2 LU or more; (4) p10 short-term -23 LUFS or higher; (5) no sustained climax or final chord over 6 dB limiting; (6) LRA 10.5 LU or more (10.5-12 accepted when it buys 2-3). Allowed: top ride from 6 dB under p95, quiet lift about 2.1, peak compressor before the limiter (-9 dB, 3:1), ride rows lowering rival ff passages or the bars before an fff.

## 4. Finale c24 techniques 112-116 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only; sent to the c22 actor)

112. Brass and clarinet KS Masters: CC11 is linear volume, dB = 20 log10 (Horn 3 46 to 73 = +4.0 dB). Woodwind / string CC11 also switches layers: fit per passage.
113. Mixed: celli half-note bass from "Leg BC MAX" to "Sus MAX" still swelled late (+2.6 to +2.9 dB) though the 100-400 Hz pulse fell; celli "Detache" (releases capped) flat at ff / v91, swelled 9-23 dB on f / v83 notes: check velocity layers first.
114. 1st Violins "Sus Marc LITE" v92 (middle marcato layer) on accented ff chords, 0.085 s lead, no CC11 bump: peak +475 to +225 ms, front no brighter. Negative on 2nd Violins / violas / celli held chords (started 13-25 dB under peak).
115. Slurred brass accent bite (2-5 kHz +5 to +11 dB on Leg Slur MAX v118) gone when tongued on "Sus MAX" v103 with the pickup ending 0.02 s before.
116. A soft upper horn voice in the weak CC1 layer: CC1 +12 at the same CC11 took it from 8.0 to 3.4 dB under the lower horn.
Delivery under the new spec: top ride 6 dB under p95, quiet lift 2.1 and ride rows met all six criteria (summit +0.6 LU, f to ff +3.7, LRA 11.8, limiter 5.8).

## 5. Finale c25 critic findings (`symphony/mvt3/reaper-v600/cycles/c25/reports/`, read only; sent to the c22 actor)

1. Check countersubjects by frequency band, not only stem level (a 2nd-violin countersubject 15-17 dB under from low CC11 + a role row + low velocity together).
2. End hairpin gains at the printed target dynamic; releasing after the ff downbeat buried a theme entry 6.9 dB.
3. Oboe stem jumps 6.4 dB between CC11 79 and 82 (layer step); check the full build writes the lane the range test used.
4. On LITE strings CC11 is loudness only; "Sus Marc LITE" plus +4 dB region gain made opening chords 7-10 dB too loud.
5. Ramp timpani CC7 over a printed decrescendo; a sudden drop made an fff roll vanish.
6. A harp ff chord at v123 peaked 13 dB over every other stem.
7. Loud tutti thin at 100-250 Hz (-4.9 dB) and bright above 6 kHz (+4.8) against the Dvořák reference.

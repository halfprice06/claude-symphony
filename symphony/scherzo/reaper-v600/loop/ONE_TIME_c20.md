# One-time notes for the cycle 20 actor

The cycle 19 actor received item 1 as a message while it worked. Read `cycles/c19/CHANGES.md` first and skip what it already did.

## 1. Finale c21 techniques 93-99 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`, read only)

93. Delivery loudness loop: after limiter and mp3 encode, measure the mp3's integrated loudness; add the shortfall (+0.05 dB) to the pre-limiter gain and limit again (2 passes landed -14.0 where 1 landed -14.5). Top ride 2:1 instead of 3:1: LRA 11.5 to 12.4 at the same limiter load.
94. Climax order at -14: delivery ride rows (final chord -3.5 dB, fff arrival -3 / -5.5, ff stabs -2 to -3) took final-chord limiting 7.8 to 5.7 dB with the order kept; cutting single instruments does not help.
95. Brass short rows: hold CC11 at the ff resting value on Stac / Marc Shrt notes and let velocity carry the dynamic (manual p.53 / p.64): mf staccato gained 5.7 dB. Check per track (on horns it raised one note group 13.5 dB).
96. Trumpet KS Master f / ff sustain releases ship at 178 ms; setting them to 300 ms gave -14..-16 dB at +0.2 s.
97. Moving a KS Master trigger to another key in the Opus state (trigger "key" + "triggerName"; "useKey" false on unused triggers) works; KS Master Sus RR plays 5-7 dB over the Harp Sus RR patch.
98. Negative: +4 dB on the cor anglais' "TLeg" groups did not reduce the legato bloom; "Sus MAX" on held notes did (+4.5..+7.6 to +0.7..+3.9 dB).
99. Weak: a CC11 fall of 10-12 units over 0.06 s before string re-bow repeats helped only 2 to 4 of 17 celli re-bows.

## 2. Finale c22 critic findings (`symphony/mvt3/reaper-v600/cycles/c22/reports/`, read only; delivery, CC and wind velocity items sent to the c19 actor)

Harp KS Master lacks the velocity-to-volume processor. Delivery ride rows can invert crescendos and ff arrivals: check every crescendo on the delivered mp3. CC caps below the running level flatten crescendos. Trumpet 300 ms release fills re-tongue gaps (240 ms proposed). Move CC11 re-tongue falls with any note-on lead. Wind legato targets at velocity 71-90 dip 6-13 dB (floor about 96 proposed). Compare band power, not summed energy over unequal windows.

## 3. Movement I c60 results (sent to the c19 actor)

The delivery quiet-lift can raise a loud chord after a quiet bar above the climax on momentary loudness even with bar levels in order: check per-bar momentary maxima on the delivered file. Removing the timpani per-stroke +6 dB shape left f / ff strokes 0.4-4.8 dB soft. render_cycle's memory gate needs a fresh REAPER restart right before rendering.

## 4. Movement I c61 critic findings (`symphony/mvt1/reaper-v621/cycles/c61/reports/`, read only; sent to the c19 actor)

Inner lines were mostly buried by old negative region / role rows from early cycles and row-wide cuts: search roles for stale negative rows; fix with phrase-length role rows +2 to +5 dB, edges in rests. Top ride 2:1 plus -2.5 to -3 dB ride rows keeps the printed order; 3:1 inverted a crescendo. Move CC11 rises and tapers with moved note-ons. Check which velocity layer sounds before per-layer region gains. Wind legato velocity floor 96 did not help there.

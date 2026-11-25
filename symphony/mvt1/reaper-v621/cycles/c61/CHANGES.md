# Cycle 61 (Movement I): CHANGES

Render: cycles/c61/mvt1-mockup-c61.mp3 (main render to 11:45, pass 2 to 12:11, 17 Nov; delivery re-run at 12:32 after one
ride row was moved, see item 2). Built from build/ as listed; rendered_build/ holds parts.json, mix.json, roles.json,
score_config.py and the variant choice files (ca61.txt, fug61.txt) as rendered (parts.json there is the re-delivery
build: its tracks are identical to the rendered build, only ride_trims differ). Scripts: cycles/c61/actor_scripts/.
Rules kept: no per-note level or shape on any track envelope, no row fitted to a render (envelope items from a per-note
rule: 0 on all 39 tracks; points 3437 -> 3449; strings 0.37-0.62 points/s, winds and brass 0.19-0.46, timpani 0.40).

## What changed, in the coordinator's order

1. **Inner lines (critic B findings 1-4), role rows of a phrase or more** (`build/roles.json` through `apply61.py`; key
   `_c61` documents them). All of B's proposals 1a-4c, with three departures:
   - celli [56,88] -2.0 -> **-0.8** (B: +1.0). The theme guard (Violins I over celli 56-88, lower quartile, 3.9 or more)
     held only up to +1.2 dB: same-start range renders c60 thB +5.20, c61 thB at -0.6 +3.80. Full render: +4.03 (c60 +5.32).
     Bassoon 1 [76,88,+2] carries the rest, as B proposed (ROLE_EDGE made its start a 2 s ramp: no rest at 76).
   - celli and Bassoon 1 [664,675.5,+3] -> **[664,679.1,+3]**: both lines are legato into the bar-170 chord with no rest;
     B's end ramp fell 3 dB across the chord's front (note-on 675.62, ff + accent at 676). The row runs to the fermata rest.
   - B's viola items 2c (464-484 2.5 -> 4.5), 2e ([272,288,3.5]) and 2f ([236.5,243.3,3], [620.5,627.3,3]) are in
     ("all of findings 1-4"), though the coordinator's list did not name them.
   - Violins II bars 107-110: `CC11_ADD` +5 units 423.9-439.9 (34 -> 39, under the p value 46).
   Result (full renders, B's measure; table in inner_line_table.md): every changed line came within 0.3-1.3 dB of B's
   expected K figure; tune on top in every changed span (tune minus line +2.0 to +13.5 dB K).
2. **Delivery.** `tools/deliver_master.py` TOP_RATIO 3.0 -> 2.0. `RIDE_TRIMS` += bar-170 chord [(675.8,0),(676,-2.5),
   (679,-2.5),(679.9,0)], [(616,0),(620,-2),(624,-1),(627,0)], and the 436 row in a changed form: C's
   [(436,0),(440,-3),...] inverted the 436-440 crescendo on the first c61 mp3 (master +2.4, delivered -0.3), so it is
   [(435.5,0),(436,-3),(440,-3),(448,-2),(456,0)] (in at the printed p). Delivery re-run on the same master; 0 inversions.
3. **Oboe 1.** `mix.json` region gain Leg Slur MAX key 76 -8 dB on the "OBs pp" and "OBs mf" sustain groups (the layers
   crossfaded at CC11 54; the f layer keeps its -5). The mf group's key-76 region spans 76-77, so F5 on that group takes
   the cut too. `CC11_LANE["Oboe 1"]` [(164,58),(165.85,58),(167.9,38),(168.9,36)].
   Measured (range, second pass): E5 bar 146 -32.9 -> -40.8 dB (4 dB over the G4 before it); master bar 146 -40.0 (c56)
   / -34.6 (c60) / -39.0 (c61): within 1.5 dB of c56. Bars 42-43: the tied G5 no longer sags (165.5: -50.3 -> -42.0) and
   there is no bounce at the F5, but the diminuendo 166 -> 168 is only 0.7 dB (F5 is 1.5-3.7 dB lower: the shared region).
4. **CC11 rise at the moved note-on** (generic, `tools/score_to_parts.py` `CC11_RISE_AT_MOVED`, default off; movement I
   `{"min_units": 8, "probe_qn": 0.15}`): a led note with no pull whose lane at score onset + 0.15 qn is 8 units or more
   over the lane at its moved note-on holds that value from the moved note-on. 20 notes on 8 tracks. Critic A's count of
   notes starting 8+ units under their own level: 55 -> 37 (the rest are leads applied later in the pipeline than this
   rule sees, mostly Violins I accents). Celli 620: fixed (join hole 7.8 dB gone).
5. **Cor anglais qn 26 / celli 286.** Range-tested (a) Sus MAX 25.8-26.95 against (b) velocity 115, same start: dip
   below the neighbours a 7.3 dB, b 10 dB (c60 about 9); 2-5 kHz share of the G#4 a -16.7, b -12.8, neighbours -15.6 /
   -20.3 (a is not brighter). Shipped a (`build/ca61.txt`). It re-attacks the following G4 (+2 dB) and leaves a 4 dB dip
   at 26.62 inside the Sus MAX note. Celli `SUS_ENTRY_AT` += 286.0: the subito pp now reaches -45 dB at 286.75 (c60
   -54.7); the marcato's last 0.12 s falls with the entry's CC11 (lead 0.25 qn). Hole 286 (16.5 dB) gone.
6. **Fugato into bar 88.** `ROLES_HOOK` (new generic hook in `score_to_parts.py`; config `C61_FUG`). Range-tested from the
   same start: both +3 rows run on to the rest at 359.9 (celli countersubject over the violas' subject, K +0.6: tune
   not on top) against one row ([338,348.5,3] runs on): celli 1-7 dB under the violas. Shipped one row
   (`build/fug61.txt`). Celli fall into bar 88: c60 10.1 dB, c61 8.4 (range).
7. **Timpani Close mic -14 -> -8** (range, same start): stick band 0.7-3 kHz +3.7 dB, boom band 50-250 Hz +5.5 dB:
   the boom rose more than the stick. Not adopted. Hrd KS alias: not done.
8. Optional: `faults61.py` counts long-join same-pitch repeats apart and widens the wind/brass join window to +0.26 s
   (faults_table.md). `PHRASE_SHAPE["end"]` -12 -> -8: not done.

## REAPER turn (lock 10:02-12:26)
State guard at the start 0 stale; main build --midi-only (Oboe 1 rebuilt in full: Opus state); restart; range renders,
each twice, second kept (bars 15-32, 85-102, 156-170 with all 34 main tracks; Cor anglais, celli 286, Oboe 1 twice;
variants CA b, fugato 1, timpani -8, each built into its track and built back). The first main render was refused by
render_cycle (audio device not running after the restart): p5.sh now runs audio_init.lua before the render; it stopped
and kept the lock as intended. Pre-render guard: Horn 4 stale, rebuilt in full, restart. Post-render saves: pass 2
Bassoon 1 stac / Cor anglais stac / Flute 1 stac and main Horn 1 / Trumpet 1 stale, rebuilt in full; 0 stale at quit.
Memory: main 43 GB before (0 compressed), 44 GB after (14 GB compressed); pass 2 20 GB. Disk 24 GB free.

## Measured, c61 against c60
- Delivered: I -14.0 LUFS, LRA 11.9 (c60 11.2), TP -1.1 dBTP, short-term p10 -22.2 (c60 -21.5), limiter 6.3 dB at bar 83
  (the only passage over 6 dB; bar 161 5.6, 41 5.2, 160 4.2, 122 4.1). Master -21.0 LUFS, LRA 22.2, TP -1.9.
- Climax order, loudest 0.4 s EBU momentary on the mp3: 160 -7.3 > 122 -7.5 > 26 -7.8 > 170 -8.3 (c60: 160 -7.1, 170
  -7.7, 26 / 122 -7.9). By mean-square 0.4 s windows the order is 160/161 > 26 -12.4 > 170 / 122 -12.5 (122 ties last).
  Master bar levels and loudest 0.4 s: 160/161 > 122 > 26 > 170.
- Crescendos on the mp3 (54 spans): 0 inverted, 1 halved (bars 40-41, +4.6 -> +2.2), median rise 4.5 master / 3.8 mp3.
- Guards: theme over celli lower quartile +4.03 (full); Violins I 56-87.9 robust SD 9 ms, front minus tail -1.5 dB.
- Master bars more than 1.5 dB off c60: 146 -4.6 and 145 -3.5 (Oboe 1 E5 region cut). Median +0.01.
- Faults (faults_table.md): holes 24 -> 25, re-bow holes 8 -> 7, sags 68, pulses 12, pitches 9.
- Isolated accents (accent_table.md): median +1.8, quartiles +1.2 / +2.6, max +9.6; 31 over +3, 23 under +1.
- Attack probe: late or hole 0.
- A/B clips c60 then c61 (ab/): bars 15-23 (celli stem), 97-102 (violas), 156-162 (Clarinet 1), 167-174 (celli).

## Left audible / not done / not verified
- Left audible: Oboe 1 bars 42-43 diminuendo 0.7 dB (F5 shares the E5 region); Cor anglais 26.62 4 dB dip inside the
  Sus MAX G#4; fugato bar 88 celli fall 8.4 dB; re-bow holes celli 40 (13.7), 52, 180, 12.7, violas 292, 36, 52; join
  holes Flute 2 560 (11.9) and 271.25 (13.2, new), basses 310, Violas 353 / 168; timpani stick still 14 dB under its
  boom; bars 40-41 crescendo halved by the delivery; limiter 6.3 dB on bar 83.
- Not done: Hrd timpani alias; PHRASE_SHAPE end -8; final-chord alias Sus MAX copies; basses' 70 % / 0.075 s form.
- Not verified (nobody listened): every inner-line change by ear; the Flute 2 271.25 hole's cause (the CC11 rise rule
  moved 44 -> 63 there); the marcato tail at celli 285.75; doubled attacks at long joins; the 0.2 / 0.3 LU climax margins
  under other measures.

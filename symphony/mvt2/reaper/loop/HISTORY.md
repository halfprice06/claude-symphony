# Mockup loop history

One entry per cycle: Accepted, Rejected/Open, Do-not-touch, and the measured effect.

## Cycle 0 (first mockup, 2026-10-10)
Built from v77 by `tools/score_to_parts.py` + `tools/build_reaper.py`. KS Master patches (solo winds and brass, string sections), Harp Maestro, Timpani Flt KS. Leg Slur for slurred single lines, Sus otherwise; pizz., tremolo, accent, sul tasto (Vln II Flautando) keyswitches; CC11 dynamics from printed dynamics and hairpins, CC1 vibrato following CC11, CC15 con sordino for strings, CC7 for timpani. No reverb, no track volume changes, default mics (Close + Main), simple pans. Dan's verdict: "It's ok."

## Cycle 1 (2026-10-11)
Accepted:
- Hairpin parser rewrite: every printed mark applied, with level holds between marks (B1).
- Slur ends legato; overlap only within one slur; re-attack between slurs and on repeated pitches (A2, A3).
- Legato velocity from note length (A4); breaths, tenuto, accents (A6).
- Keyswitches and CC15 placed in the preceding rest; first keyswitch skipped (A5, B6); solo/cantabile/espr. +8 CC11 (B6).
- Timpani CC7 per articulation with a roll settle (B2).
- Harp Sus RR with velocity dynamics; new Harp harmonics track (A1, B5).
- build/mix.json for track gains, mics, one shared hall reverb and stereo-pan seats (B3, B4, C1-C5).
- 1x offline render (RENDER_1X 1), which removed most late entries.
- Measured: -27.4 LUFS, LRA 23.5, TP -9.2; 63 Hz +14.1 → +4.7; p medians within about 2 dB across winds and strings; ppp timp rolls -48.
Rejected/Open:
- Leg BC and celli divisi deferred; earlier legato targets deferred.
- Shifting notes to hide start delays rejected (delays not deterministic). Some remain (Hn1 17/261, Hn3-4 84, Vln II/Vla 108); the remaining fix is Opus PreloadSize, a global preference left to Dan.
- Open: celli loudest in 26 bars (climax 57-63, bar 80); basses 8 dB under celli at f; timp pp strokes about -58.
Do-not-touch:
- Hairpin parser and level holds; slur-scoped legato overlap; mix.json reverb/mic scheme (one hall, sends for depth); 1x render; harp patch; timpani roll dB table, unless measured otherwise.

## Cycle 2 (2026-10-11)
Accepted:
- Used KS-Master articulations loaded (pizz., tremolo, flautando now play); EWSO legato speed and RTKiller on (A1, A2a).
- Leg BC MAX for connected string lines and slur-to-slur joins; legato velocity 120/105 for strings and horns (A3, A2b).
- CC70 sul D/G/C/A; Horn 3 con sord. via CC15 (A4, A6).
- Track volume envelope: gain + dyn_trim_db (f/ff) + soft_trim_db (ppp -4, pp -2) + roles.json + note_trims.json + final fade + timp roll settle (B1, B2, B5, C1, C3 partial). REAPER ignores D_VOL under an envelope, so the gain lives in the envelope.
- ff 114 / fff 124; sf spike then drop into the hairpin; +22 CC untargeted soft hairpins; boost +3 for string espr./cantabile, faded out at f; long-note swell and phrase taper; anti-bloom on soft string chords (C2, C4, C5, B4, B6).
- Timpani: gain -7, roll table +4 at mf-ff, pp strokes +20 (B3, C6).
- render_cycle waits for three quiet memory readings.
- Measured: -27.2 LUFS, LRA 24.7, TP -8.4; late entries 51 → 23; pizz. decay 10-16 dB; bar 92 8 dB under bar 91; celli level with the violin tune (were +9 to +10).
Rejected/Open:
- Deferred: A2c (legato target shift), A5 (divisi tracks), C3 (sweep-measured CC curves).
- Open: bar 61 not louder than 79-80; Tbn1 about 10 dB over the strings in bar 63; timp pp strokes at 278.5-279 about -60; legato lag not re-measured.
Do-not-touch:
- Articulation row loading; the volume-envelope scheme (gain in the envelope, D_VOL 1); Leg BC rule; roles.json celli cuts; final-bar fade; the timp settle in vol_db; the 1x render.

## Cycle 3 (2026-10-11)
Accepted:
- Legato targets start early (strings 0.17 s, brass 0.10, Ob/Bn 0.06, BCl 0.05) with velocity 124 (A2, C1); soft sustained entries start early (strings 0.12/0.06 s, brass 0.10/0.05, bassoons 0.06) with CC11 held at the entry level (C5). parts.json notes carry `sq` (score onset).
- Same-pitch string repeats merged with a CC11 notch (portato 10, bow change 14) (A1); tenuto joins legato in strings, lighter gaps in winds at mf+ (A3); first keyswitch sent for late-entering tracks (A4).
- After-grace run re-placed onto its target (C2); slurred string notes < 0.25 s on overlapping Sus MAX (C3); tempo steps smoothed into 0.25 qn ramps inside each rit./allargando/animando span (C4).
- Timp soft rolls -6 dB, p strokes +12, two pp strokes v60 (B1); divisi/double-stop level cut in vol_db (B2); Vla/Bn trims, per-track soft_trim_db (B3); note_trims by onset (B4); Harp roles -7, Vln II roles [108,124,-3] (B5).
- Measured: -28.1 LUFS, LRA 24.0, TP -10.2; string legato crossover 250-275 → 50-85 ms, horns 190-200 → 85-108; Tbn1 first accents -8.8 → +5.6 dB attack; soft rolls 6 dB under c02 and under the solos; Vla 2.2 dB under Vln II at ff; harp 3-6 dB under the CA solo.
Rejected/Open:
- Deferred: DIV A/B tracks (A5), Opus state trigger fields (A4), Slur Runs patch (C2), caesuras (C4), qn 0 pre-roll (C5).
- Open: master dip at qn 223 (-6..-9 dB, Vln II sample decay under the notch); viola sextuplets ~100 ms late; soft string entries still 300-500 ms (Vln I/II); Vln I legato slightly ahead (50 ms); CA legato 160 ms; bar 28 violas level with the tune; 63 Hz high.
Do-not-touch:
- Legato and entry lead tables (re-tune by measurement only, against `sq`); same-pitch merge; grace placement; tempo ramp spans (lengths match the steps); timp soft-roll -6 and settle; divisi cut; onset-keyed note trims.

## Cycle 4 (2026-10-11)
The first attempt was interrupted when the Mac froze during its second render. The resumed run checked the REAPER state against parts.json (all matched) and rendered pass2, pass3 and the final render.
Accepted:
- Harp arpeggios rolled from the bottom: 40/30 ms per note, top note +4 velocity, 33 chords (A1).
- Same-patch unisons: the copy is dropped and the kept note gets +3 dB. This applies to Hn1/2 at the climax, Cl 259, Ob 210 and Bn 196 (A2, simple version).
- Portato in wind slurs plays Sus (A4). Legato lead CA 0.08 s, Fl/Cl 0.03 s; CA legato velocity 100/90/80 (A5).
- sf from f or louder is +8 and held 0.25 qn (A3, CC shape only).
- Vibrato: CC1 by role (melody 100 / strings 95, delayed onset, +10 on the top note of each slur; accompaniment from level; flautando 20) (C3).
- Caesuras: +0.22 s before qn 204 and +0.15 s before qn 268 (C6).
- Soft re-attack bloom vol_db (-4.5 dB over 2 qn); pp notch 8 (C5).
- ReaEQ from mix.json `eq`: Cb low shelf 90 Hz -7 plus bell 150 Hz +3; Cbn and Tuba low shelf 70 Hz -4 (B2, C4). Wider widths, 0.5-0.6 (C2).
- ff trims: strings up, oboes/clarinets/Cbn down, flutes -6 -> -1 (B1, C1). roles and note_trims for Vc, Cb, Vln II, Vla, Harp, Fl1 (B1, B3-B5).
- Note-end guard before same-pitch and tremolo onsets.
- Measured: -28.2 LUFS, LRA 24.2, TP -9.5. 63 Hz +5.4 -> +1.1. Master correlation 0.76 -> 0.64. Vln I over oboes/clarinets/bassoons at both climaxes (flutes doubling the tune within 1 dB). Hn1/Hn2 correlation 0.999 -> no copy. Vc countermelody 4-6 dB under Vln I and 4-6 dB over Cb.
Rejected/Open:
- A3 timing (tenuto crossfade, 0.05 s tremolo lead) did not help and is off (`TREM_TIMING_C04`).
- Open: bar 63 downbeat, a 0.4-0.5 qn hole in Vln I/II/Vc. Inferred cause: the violin tremolo does not sound at high CC11. Test with a short range render and a CC11 cap of 108.
- Open: soft string attacks more than 0.3 s late rose from 29 to 46. Suspect the delayed-vibrato dip.
- Deferred: a2 horn track (A2 full), divisi/solo tracks (A6), string high shelf (C4).
Do-not-touch:
- Unison drop pass; harp roll timing; caesuras; the ReaEQ scheme in mix.json; climax ff trims; Vc countermelody roles; the stereo widths (master correlation is now at target).

## Cycle 5 (2026-10-11)
One full rebuild in a fresh REAPER session and one render. Opus PreloadSize was not changed: ONE_TIME.md's approval came only through the file, so the setting is still 1 and the file is left in place.
Accepted:
- Attack gate `tools/probe_attacks.py`, run by render_cycle into `metrics/attacks.txt` (A1).
- `short_sus` measured without caesuras; legato notes end before a non-legato keyswitch (A2). Horn 4 reads Horn 3's con sord. (A3). `SHARED_DYN` Bn1 f at 259 (A4).
- roles/note_trims for bars 28-30, 57-60, 75-81, the final chord, timp bar 52/82 and Hn3-4 -4 at the close; timp settle held 0.5 qn past the roll (B1-B6).
- Hall: New Hollywood Hall 2.0 (3BS Sus MAX) at fx_volume 0.19 (C1). Cb Close 0.4, gain -7; ReaEQ `highpass` band at 30/40 Hz (C2). Seat/width set inside Opus with panLeft/panRight, REAPER pan centre and width 1 (C3). Timp mics Close 0.2 / Main 0.5; Tuba Close 0.45, +2 (C4). Harp harmonics seat -0.35 (C5).
- Measured: -25.7 LUFS, LRA 25.4, TP -5.5. Probe 11 -> 1 failure (Vln II 212 dip 6.8 dB). String entries back on time (pizz 0.00-0.04 s). Melody margins +4 to +6 dB at bars 57-60 and 75-81. 63 Hz +1.1 -> -5.3 (ref -6.2). Stem late decay slope 3.1 -> 2.5 s.
Rejected/Open:
- Regression: 125-180 Hz -9.5 -> -15.5 (ref -3.7), from the Cb Close cut, timp mics and the new IR.
- Tails still follow the seat: the Opus send is post-pan (inferred). Next: a REAPER Hall bus (C3 fallback).
- Open: 300 ms drop still 10 dB; Horn 4 5-7 dB over Horn 3 at 87-89; PreloadSize waits for Dan.
- Deferred: divisi/solo tracks (memory), separate tremolo patches (not needed).
Do-not-touch:
- The full rebuild before a render; the attack gate; the short_sus/keyswitch guard; the B #1-#4 roles (margins now +4 to +6); the Cb 40-90 Hz cut (fix the body at 125-180 Hz instead); the seats.


## Cycle 6 (2026-10-11)
The project was rebuilt in full and rendered once. ONE_TIME.md was not done: Dan's approval is confirmed in the thread, but the permission system blocked the edit to Opus's Preferences.json. PreloadSize is still 1, and Dan needs to change it himself. The render's attack gate failed 10 of 19 checks: entries were 0.2-0.3 s late, including on unchanged tracks, because macOS had compressed 42 of REAPER's 57 GB under memory pressure. The render was not repeated, to avoid another freeze. Its levels can be trusted; its onset timing cannot.
Accepted:
- Silent 3 qn pre-roll in REAPER, cut off after the render; opening-chord checks in the probe (A #1, B #4). Hn3's opening went from -75 to -56 dB max.
- `build/pitch_trims.json`: per-pitch trims on legato notes for Hn1, Cl1, CA and Fl1. Removed Cl1 266 -3 (A #2). The Hn1 bar 55-60 spread went from 13 to 6.6 dB.
- Leg -> Sus string notes with no rest get the entry lead and velocity 105 (A #3, cheap version). Viola legato from C4 starts +0.10 s earlier (A #4). Printed bow marks inside held notes add notches (A #5).
- Soft trims: a p anchor, global {ppp -2, pp 0, p +2}, per-track overrides for Cl1/Cl2/Bn1/Bn2/Cb/Vla, and Cb roles eased with +5 on the pizz. (B #1-#3). Cb-Vc in soft bars went from -8.1 to -2.6 dB median. LRA went from 25.4 to 23.9.
- Roles: Hn3 under the bar 79-81 tune, Hn1 in bars 54-56, Vln II/Vla under the bar 46-47 oboe. Timp bar 84 +3 (B #5, #6).
- `hpgain`: crescendos to f+ get +4 dB (winds), +3 (strings), +2 (brass), released over 1 qn. A role can take a fourth value, end_ramp; the bar 57-60 cuts open over 4 qn (C #1). Wind growth in bar 60 went from -1..+0.7 to +1.7..+3.6 dB.
- sf from f+ falls 10 CC (C #2). Vln I bar 63 went from -8.1 dB in beat 1 to -2.8, then -2 to -3 per beat.
- Hairpin parser: no overshoot of the next mark; a decrescendo whose target is not below the current level falls 6; "niente <" (C #3). Cl2 bar 91 now falls 3.4 dB.
- roll_db ff -11 / fff -9; Tbn2/BTbn/Tuba +2 at the climax (C #4). The bar 61/62 vs 79/80 margin went from 1.4 to 2.4 dB.
- dB swell on long notes (C #5); Tbn1 bars 63-64 fall and the qn 218 accent at velocity 105 (C #6).
- Measured: -25.1 LUFS, LRA 23.9, TP -4.2.
Rejected/Open:
- Re-render c06 (or render c07) only when REAPER's compressed memory is low; then re-check the attack gate, the Vc div dips at 51/63 (51 measured worse, 17.6 dB, but confounded), the timp ff roll (+0.3 dB instead of +3), and bar 84 timp.
- Deferred: viola triplets on short_sus (A #4b), Celli DIV B and other divisi tracks (memory), the flute CC1 top-note alternative.
- Open: Fl1 still jumps +6.9 dB into qn 204; Bn1 still 1-8 dB under BCl in bars 7 and 10; the Cb crescendo in bars 75-77.
Do-not-touch:
- The pre-roll (and the rule that parts.json stays on score time); pitch_trims; the soft-trim table and its overrides; the B #5 horn roles; the hpgain release of 1 qn (not 0.25); the C #3 parser rules.

## Cycle 7 (2026-10-11)
ONE_TIME.md (PreloadSize 0) was deferred and goes back to Dan. The Opus manual says the HDD preload uses more RAM, and the c06 lateness came from memory compression, not from the preload. New `--midi-only` rebuild (no patch reload); REAPER was restarted before the render (49 GB, 0 GB compressed); one render; the attack gate passed 19 of 19.
Accepted:
- A #1: Largamente wind portato joined (Leg Slur targets, notches, 0.03 qn Sus crossfades, 0.04 s re-tongue). Dips Ob1 8.0 -> 4.9, Cl2 6.8 -> 5.2, Bn2 5.7 -> 4.1, Fl2 8.7/12.2 -> 6.1/10.5.
- A #2: viola/celli div. joins get the entry lead (viola joins of 6 dB or more 8 -> 2). A #3: bcsoft CC11 dip (Vln II qn 48 +7.9 -> +6.4).
- B #1-#6: pitch trims on all articulations (`_all_arts`: horns F4/Gb4/Ab4, Cb Ab1, Bn2 Db3); climax bass trims moved from the reeds to Cb/Vc; flute, bar 47, Hn3/Hn4 trims. Cb now 1-2 dB over Cbn at bar 79; bar 69 margin -2.1 -> +2.8.
- C #2: leads from qn 0 for strings; `build/entry_leads.json` per-onset extras (cap 0.30 s). C #3: Vln II/Vla legato lead 0.20, brass velocity 124 (Vln II median +0.053 -> +0.023). C #4: leads measured on the real tempo map (`qn_before`). C #5: the fermata holds (-47..-48 dB for 4 s, was -55..-68).
- C #1a: render_cycle refuses to render when REAPER has more than 6 GB compressed.
- Measured: -25.3 LUFS, LRA 23.7, TP -5.4. Entry median 0.060 s (c06 0.102).
Rejected/Open:
- Deferred: A #4 solo violin track, A #5 Leg Port, C #1b/c, C #2c, C #3c.
- Open: Fl2 Leg Slur dip at 208 (10.5 dB); Vln II soft BC bump 5-6 dB; Vln I 0 / Vln II 42 / Vla 54 entries later with the extra lead; Fl1 within 1 dB of Vln I at qn 262; bar 30 Cb over Vc; 63 Hz -4.7 -> -2.7.
Do-not-touch:
- The midi-only update and the restart before rendering; the compression gate; `qn_before` leads; the fermata hold; `_all_arts` pitch trims; the moved bass trims (Cb level with Cbn at the climaxes).

## Cycle 8 (2026-10-11)
ONE_TIME.md skipped (no answer from Dan since c07 sent it back; PreloadSize still 1). All changes were data: `build_reaper.py --midi-only --tempo` (new flag) rewrote the tempo map and every item without patch reloads; REAPER was restarted. Other work on the Mac compressed REAPER's samples (36 of 49 GB); the render ran with `--force` and still passed the attack gate 19 of 19. `render_cycle.py` now waits up to 2700 s for loading and refuses to render while memory is growing.
Accepted:
- A #1 `build/early_fills.json` (first 0.35 s of 30 sagging legato targets); `{"early","body"}` pitch-trim shape, Horn F4 +1/-5. A #2 Violas' soft short slur-to-slur joins stay Leg Slur MAX with an 8 CC notch (`VLA_BC_SOFT`). A #3 pizz.-only pitch trims (`"_arts"`).
- B #1 Fl1 G6-Bb6 trims on all articulations (`"_all_arts_pitches"`); B #2 Vc bars 71-74; B #3 Cl1 266 -5; B #4 harmonics read both harp staves, -6 velocity; B #5 pitch trims stop at onset + 3 qn on notes over 4 qn; B #6 viola roles under the oboe.
- C #1 hpgain held to the first onset after the arrival note; ff tenuto holds under "molto sostenuto". C #2 goal-note trims and Ob1 148 v100 (fallback). C #3 10 new `CAESURA` breaths (+1 s). C #4 coda soft string legato v90, roles. C #5 interim: Vln I solo without SOLO_BOOST, CC1 +10, role -3. C #6 Vc f/ff trims eased.
- Measured: -23.9 LUFS, LRA 23.6, TP -4.0. Wind/horn sag 7-10 -> 2-4 dB; moved viola joins 10.2 -> 6.2 dB median; arrival falls 4-6 -> 1-3.6 dB; Vc countermelody -5 -> -1.5 dB against Vln II; Fl1 now 0-2 dB under Vln I at the peaks; Vln I solo 5.6 dB over the oboe -> 1.9 under.
Rejected/Open:
- Deferred: DIV A solo violin track (memory), flute v80 legato test, C #2 general rules, cadence-bar slowing.
- Overshot: harmonics -47.7 -> -57.7 (use about v72); Cb 4.5 dB over Vc in bars 89-92. Not met: Horn F4 sag 6.6-7.7 (raise early to +4); bar 89 over bar 88; C #6 had no effect on the loud-frame 125/250 Hz bands.
Do-not-touch:
- early_fills and the F4 body -5; VLA_BC_SOFT; the hpgain hold to the next onset; the sostenuto tenuto hold; the new caesuras (gate passed); the Vc bars 71-74 balance; the Fl1 top-octave trims.

## Cycle 9 (2026-10-11)
Full rebuild: every Opus state changed (pre-fader sends, reverb high cut, widths). REAPER was restarted before each render. There were three renders. Pass 1 had regressions I caused (fast note-trim starts, accent too strong). Pass 2 fixed them, but my `fresh` cut had shortened the Vln I qn 65 note to 0.02 qn. Pass 3, with only Vln I changed, is the delivered render. Its first try stalled on a non-empty render folder (inferred: an overwrite prompt), so I emptied the folder and rendered again. All renders passed the attack gate. Someone else changed render_cycle.py in this cycle: the mp3 is now mastered by `tools/deliver_master.py`.
Accepted:
- A #1 early fills (Ob1 55.5/57/271, CA 99/129.5/133.5, Fl1 190/252, Fl1 256 3 -> 5).
- A #2: role spans that meet crossfade (`ROLE_CHAIN`), and spans on a legato target ramp in after the join. Trims end at the next moved onset. Pitch trims on joined notes start at the moved onset. bcsoft is skipped at a crescendo start.
- A #3: no Leg BC over an octave (Sus MAX entry) or at solo/tutti texts (`fresh` entry lead; Vln I 65 extra 0.10 s).
- A #4: Horns 3-4 mute emulated by `mute_eq` (a second ReaEQ with automated Wet from qn 278).
- A #5: `ACCENT_DB` 2 on loud accents; Tbn1 218 v110. A #6: `HARP_PITCH_VEL`.
- B #1: `HP_CHAIN` hpgain chaining. B #2: no trim cut on long notes, Cb [274,286,2]. B #3: messa di voce returns to its start level. B #4: Vln I [204,208,-1.5], Vln II [204,212,2]. B #5: harmonics gain +3. B #6: Bn2 259 -5.
- C #1 EQ: Vc bell 170 +3, Cb shelf -5 / bell 160 +6, Vln I high shelf 5 kHz -4 (new `highshelf`); measure.py band shares vs Brahms. C #3: widths 0.3 / 0.35. C #4: reverb high cut 5.5 kHz. C #5: fade holds -10 after the release. C #6: high-passes on harp, tuba, BTbn, timp.
- C #2 (pre-fader sends) is in place, but it had no measured effect.
- Measured (pass 2): -23.7 LUFS, LRA 23.8, TP -3.9.
  - Join dips: Ob1 55.5/57/271 10-12 -> 4-6 dB, CA 99 9.4 -> 4.2, Fl1 252 9.3 -> 3.7.
  - Vc 274 at body level by +0.2 s (was -76 dB for 0.8 s). Horn 3 muted 2-8 kHz ratio -17.7 -> -25.8 dB.
  - Bar 59 wind sag 6.5 -> 3.5 dB. Cb-Vc in bars 83-92 within -2.5..+0.3 dB. Vln I share of bar 61 37 -> 26%.
  - 100-250 Hz share -11.2 -> -9.6. 8-16 Hz -38.5 -> -50.2.
Rejected/Open:
- C #2: the tails still follow the seat (Vln I tail R-L -7.6 dB). Next: a REAPER Hall bus (ReaVerb, post-fader sends, Opus reverb off). C #4: tails are only 1 dB darker than the sustain.
- Open: CA 129.5/133.5, Fl1 190/256/270.5 joins 6-9 dB; Vla 146 still falls about 9 dB; Vln I 244-249 3 dB over bar 72 (target 1.5); 100-250 Hz 0.8-2 dB short; final tail -10 to -40 dB in 1.05 s.
Do-not-touch:
- The role chaining and the trim end rule (note trims keep their 0.6 s ramp in).
- The Leg BC octave/solo-tutti skip; `mute_eq`; `ACCENT_DB` 2 and Tbn1 v110; `HP_CHAIN`.
- The Cb [274,286,2] role and no long-note trim cut.
- The C #1 EQ: melody margins held within 0.7 dB.

## Cycle 10 (2026-10-11)
Only data changes plus one new track. The project was restarted and rendered once; the attack gate passed 19 of 19. The new solo track's gain was set from its measured level after the render. The delivered master is the stem sum with that stem at -7 dB, which is exact: the stems sum to the master to -122 dBFS.
Accepted:
- A #1: "Violin I solo" (track 28) on the 1st Violins KS Master DIV A (only a Close mic), from `TRACK_WINDOWS` 48-65. The qn 65 hole went from 6-7 dB to 1.3 dB. The solo is 5 dB over Vln II.
- A #2/#4: `{"db","pre_s"}` early fills with exact envelope breakpoints (`vol_bp`) and 15 new fills. Cl1 266 went from 10.5 to 4.4 dB, Vla 245.5 from 7.5 to 4.1, Vln I 67.5 from 8.5 to 4.8.
- B #1/C #1: soft trims +3/+3/+1.5 (global {ppp +1, pp +3, p +3.5}); Ob1/Cl1/Cl2 solo roles.
- B #2: `TIMP_LOUD_ATTACK_DB` 6. Timpani minus mix at qn 204 went from -11.1 to -6.4. B #4: Timp [277,280,10].
- B #3/C #2: Tbn1 212.5/213 at v108/105 (peaks -7.5 -> -15.6). `deliver_master.py` TARGET_I -19.5.
- C #3: `HP_CHAIN_RISE` for winds 0.75. C #4: a half hold to qn 212, the sf cut on the sf, an sf accent once per chord, and Largamente string legato at v108. C #5: no bloomv on a crescendo's arrival, v60 at qn 286.
- Measured: master -23.6 LUFS, LRA 21.6, TP -3.6. mp3 -20.0 LUFS, LRA 14.6, TP -1.5, span 19.5, limiter 3.6 (was 4.5).
Rejected/Open:
- Deferred: A #3 portamento (patch reload plus an f0 range test), C #6 swell shaping.
- Rejected in simulation: sf cuts after the attack (+2 dBFS peak), a full sostenuto hold (4.9 dB limiter), a string chain rise.
- Open: span 0.5 over; bar 62 still 2.4 dB under bar 61; Fl1/Ob1 +6..+9 dB step into bar 61; Hn1 203 join 7.3; Cl1 under Cl2 at 287.5; Timp 279 5.7 dB under the violas.
Do-not-touch:
- The solo track and window, and its gain -1.
- The sf cut timing (on the sf, not after it); `SOST_HOLD_SHARE` 0.5 unless re-simulated.
- `TIMP_LOUD_ATTACK_DB` 6; the soft-trim table.
- Tbn1 v108/105.

## Cycle 11 (2026-10-11)
The project was updated with `--midi-only`; Violins I got a full rebuild for the Leg Port row. The REAPER restart hung at startup on a "faulty project" alert. I started REAPER with `open -a REAPER --args -new` and opened the project with a bridge job. One render; the attack gate passed 19 of 19. After the render, the Horn 2/3 fills were reshaped and applied to their stems (a level-only envelope fix), and the master was rebuilt as the stem sum.
Accepted:
- A #1 `BC_SOFT` (soft Leg BC joins stay Leg Slur with a notch, Vln II/Vla/Vc, any length; BCSOFT depth 0). A #2 early fills with `hold_s` (15 joins). A #3 `ACCENT_DB_AT` Tbn1 212.5 +4 / 218 +3. A #4 `PORT_TARGETS` Vln I 82/172 (trial).
- B #1/#2 bar 61-62 roles (winds evened; BCl down, Tuba/BTbn/Cbn up). B #3 swell look-ahead cap and `HP_GAIN_MF_DB`. B #4 ppp soft trim 1 -> 3. B #5 timp p strokes +16. B #6 Tbn1 +3 over the strings' -2 at bar 63.
- C #1 Hn1 F4 extra lead 0.15. C #2 Hn3 204 lead plus a fill. C #3 `build/leg_leads.json`. C #4 solo lead 0.12. C #5 `LEG_PAIR_EXTRA_S`. C #6 `SHORT_SUS_DETACH`.
- Measured: master -23.7 LUFS, LRA 21.5, TP -3.6. mp3 -19.9 LUFS, LRA 14.4, TP -1.6, span 18.9, limiter 3.5.
  - Wind spread at bar 61 13.3 -> 5.1 dB; bar 61 -> 62 fall 2.2 -> 1.2 dB.
  - 15 filled joins 7-11 -> 3-5 dB.
  - Tbn1 212.5 attack -1.7 -> +2.0 dB over its body.
  - Crossovers: Hn1 184 +0.19 -> +0.05 s, Vln I 204 +0.14 -> +0.07, Vc 74/246 +0.23 -> -0.05, solo median -0.03 -> +0.02.
  - Timp 172 within 1.6-3.4 dB of the p violins.
Rejected/Open:
- A #5 rejected (it conflicts with the measured C #4).
- A #1 helped the violas (median dip 5.6 -> 3.1) but not Violins II (4.8 -> 6.2) or the celli (5.1 -> 5.3). Next: limit it to the long soft targets on Vln II/Vc.
- No effect: C #6 (dominance 0.27 -> 0.26), C #5 for the violas (lead cap), B #3 (+1 dB, target +2.5). A #4 glide not measurable yet.
- Open: Hn1 203 hole 7.2 dB; Hn1 193/202 still +0.18 s late.
Do-not-touch:
- The `hold_s` fills, including the reshaped Hn2 210 / Hn3 204 (the plain shape overshot 4-10 dB).
- BC_SOFT for the violas; BCSOFT depth 0.
- The bar 61-62 wind and low-brass roles; the mf arrivals do not chain.
- Tbn1 accent overrides; `leg_leads.json`; the solo lead 0.12; the Vc (56,60) pair lead.

## Cycle 12 (2026-10-11)
`--midi-only --tempo` update (Violins II and Violoncellos fully rebuilt for the Leg Port row), restart, one render. Other work compressed 31 GB of REAPER's memory during the render; the attack gate passed 18 of 19 (Vc 212 dip 6.6 dB against a limit of 6; its 25 ms envelope matches c11 within 1 dB).
Accepted:
- A #1 pizz. pitch trims as a step at full value on the attack. A #2 `BC_SOFT_SKIP` (16 joins back to Leg BC MAX). A #3 Leg Port on Vln II 82/172 and Vc 83. A #4 pickup roles into bar 53 (end_ramp, off the port target). A #6 Vln I 262 lead +0.05.
- B #1 theme A note trims; B #2 Vln I [0,9.2,-5], [292,304,-6]; B #4 coda horns +5/+3; B #5 CA under the bar 34 BCl solo.
- C #1 + B #3: bars 79-81 lift (strings +2-2.5, Ob1 +6/+4, Cl2/Bn2 +4, BCl/Cbn +2, Fl1 -2 role removed, three wind note trims eased) and a new roles.json `"_all"` row [204,212,-1]. C #5 horns +2 at both climaxes. C #2 alternative: Hn3/Hn4 [0,17,-2]. C #3 `PHRASE_ARCS` (14 phrases, +1.06 s). C #4 BCl pp -2 dB and a 2.5 kHz -4 dB shelf.
- Measured: master -23.6 LUFS, LRA 23.9, TP -3.9. mp3 -19.8 LUFS, LRA 15.7, TP -1.6, span 18.4, limiter 3.0.
  - Climax gap 4.8 -> 1.6 LU; bar 79 now 1.7 dB over bar 60.
  - Viola pizz. spread 8 -> 5.7 dB, largest jump 14.5 -> 6.7.
  - All 16 BC_SOFT_SKIP joins 2.5-5 dB shallower; Vc joins of 7 dB+ 22 -> 11.
  - Vln II 82 glide energy +17..+21 dB. Theme A swell top 4.4-6 -> 1.1-2.3 dB under the phrase start; mf at qn 82 3.7 dB over it.
Rejected/Open:
- Deferred: A #5 viola sextuplet articulation test (needs range renders). C #6 not needed (Vln I rests in bars 87-88). Global ppp 3 -> 1 not used (simulated -0.3 dB on the intro).
- Not met: intro and coda only 1.0 LU under the horn solo (targets 1.5-2.5 and 2); bar 53 pickup still 2-3 dB over its downbeat; BCl 2-6 kHz level with Hn1 (target +2); one pizz. F4 round robin now 6.6 dB under.
Do-not-touch:
- The pizz. step shape; `BC_SOFT_SKIP`; the bars 79-81 lift and the `_all` [204,212,-1] (climax gap now at target); `PHRASE_ARCS` amounts unless timing measures say otherwise; the coda horn roles; the Vln I opening/coda roles.

## Cycle 13 (2026-10-11)
`--midi-only` update. Five tracks were fully built: BCl, Cb, Harp harmonics, Violin I solo, and the new Violoncellos div. Then a restart and one render. The attack gate passed 18 of 19 (Vc 212 6.6 dB, identical to c12). After the render, the Vc div gain was raised by 6 dB (mix.json + `--mix-only`) and the master was rebuilt as the stem sum (exact).
Accepted:
- A #1 "Violoncellos div" (stem 29, Celli KS Master DIV A, `TRACK_SPLITS`) for the bar 18/22 answers. A #2 bow-change notches halved, `joined_next` (no taper or bloomv into a join), Vc fills 68/78. A #3 timp roll hairpins: the missing half of the CC7 dB goes in the volume envelope (`TIMP_HP_DB_FACTOR`); Timp [200,203.5,-3] removed. A #4 wind fills. A #5 loud breaths 0.3 qn.
- B #1-#4, #6 pitch trims (Cl1/Cl2 Ab4 +6, Bn Eb3 +6 / G3 +4, Cb Sus-only {32 -5, 37 -2, 39 +4}, CA Db4 +4). B #2 Ob1 42/54 +5, Vla 54 -7 / 48 -4. B #5 Harp [172,188,-4] removed.
- C #1 Opus main channel centred (DIV A patches), solo seat -0.4. C #3 Cb shelf removed, bell +3, Close 0.6, gain -8, 25 Hz HP. C #4 BCl seat -0.05. C #5 harmonics seat -0.65.
- Measured: master -23.3 LUFS, LRA 23.9, TP -3.6. mp3 -19.8 LUFS, LRA 15.8, TP -1.6, span 18.2, limiter 3.2.
  - Cello answer 6.2/3.9 dB under the solo violin. Entry dip 10 -> 6.6 (qn 51) / 4.6 (qn 63).
  - Timp qn 200 roll +5.3 -> +9.9 dB; qn 268 falls 8.4 dB.
  - Cl2 Ab4 +5.5 dB (bar 75-77 step 10 -> 4 dB). Bn Eb3 +5. Cb Eb2 +5..+6.
  - Solo violin R-L -21 -> -5 dB; BCl -5.3 -> -2.5.
Rejected/Open:
- Deferred: C #2 true-stereo hall IR (needs a full rebuild and a test render on its own cycle).
- Open: qn 200 roll 4.7 dB under Vln I (target 6-9); qn 51 cello entry 6.6 dB dip; Cb 20-100 Hz share -15.1 (target -14.5..-12.5); Hn1 196 breath only 1 dB deeper.
Do-not-touch:
- `TRACK_SPLITS` and the div track's gain +4.
- Main channel centring in apply_mix.
- `TIMP_HP_DB_FACTOR` 1.0 (adjust the roll with a role, not the factor, unless re-measured).
- The halved notches and `joined_next`.
- The new pitch trims; Cb trims on Sus MAX only.

## Cycle 14 (2026-10-11)
`--midi-only` update of all 29 tracks (no state changes), restart, one render. Attack gate 18 of 19: Vc 212 at 7.0 dB, the known marginal probe; the new sostenuto ramp into qn 212 raised the frame before it. After the render, two stem fixes, then the master was rebuilt as the stem sum:
- Tbn1 Marc Lng +2 dB body / +2 dB attack. This is level only, so the fix is exact.
- Violas qn 195.4-202.08 taken from the c13 stem, because the A #3 test was reverted. This splice is not sample-identical.
Accepted:
- A #1 `MARCATO_SPANS`: the Tbn1 line plays Marc Lng RRx4 at 0.75 length, v106-94. The c06 note-trim falls are removed.
- A #2 `TIMP_TIE_STROKES` 203/211: the roll ends in a stroke at roll + 4 dB CC7, with half the loud-attack bump.
- B #1/C #3 soft solo roles (horn +2.5/+2 with a crest row; Ob1, solo violin, BCl, CA +2) and `_all` [283.5,304,-2].
- B #2 Vc note trims. B #3 Ob1 42 +6, Vln II [42,44.5,-2]. B #4 Cl B flat 4 -3. B #5 Vln I [292,304,-4].
- C #1 `LEAD_SPANS` soft hairpin gain: +3 dB on crescendos (messa di voce released across the decrescendo), -2 dB on a lone decrescendo.
- C #2 trims and fills: Hn1 32 +2.5, C4 -2; BCl 93; Vln I 67.5/68 and C5 -2 with `_skip_onsets`; solo violin 48.5/53.
- C #4 `swell_sost` + `SOST_SUSTAIN_DB` 2.5.
- Measured: master -23.8 LUFS, LRA 23.5, TP -4.5. mp3 -19.8 LUFS, LRA 16.0, TP -1.7, span 18.2, limiter 2.0 (was 3.2).
  - Lead crescendos median +1.7 -> +5.3 dB.
  - Horn over accompaniment +0.2 -> +3.8 dB.
  - Intro 2.8 LU and pp coda 2.5 LU under the horn solo.
  - Vc step 8.2 -> 1.9 dB. Oboe +1.9..+6.3 over Vln II.
  - Timp 203 stroke +6.4 dB over the roll.
  - Bars 61-62 dip at 207.5 -21.8 -> -18.7.
Rejected/Open:
- A #3 (viola sextuplets on Leg Slur MAX): failed (own share 0.33 -> 0.03) and closed.
- Deferred: A #4 a2 horns, C #5 pitch-following shaping, the true-stereo IR.
- Open:
  - Tbn1 Marc Lng attacks have no peak (separation only).
  - Horn crest qn 34-35 still 2.4 dB under the bar 8 swell, per beat.
  - Vln I 68-70 crescendo still falls; Ob1 148-151 decrescendo flat.
Do-not-touch:
- `LEAD_SPANS` soft gain 3/-2.
- The soft solo roles and coda `_all` -2: the mp3 section gaps are now at target.
- `TIMP_TIE_STROKES` levels.
- `swell_sost`.
- B #2-#5 trims.
- The Tbn1 Marc Lng velocities and +2/+2 shape: retune only the attack.

## Cycle 15 (2026-10-11)
`--midi-only --tempo` update of 28 tracks. Violas were fully rebuilt (Detache row). Restart, one render, no stem fixes. The first reopen deadlocked inside Opus `VST3_LoadState`; a kill and a second `-new` start worked. Attack gate 17 of 19: Vc 212 6.8 (known), Vln II 212 7.8. The c14/c15 envelopes at 212 match within 1 dB, so this is probe noise.
Accepted:
- A #1 sostenuto hold-through (`SOST_HOLD_THROUGH`); Cl1 204 Ab4 trim skipped, note trim +2.
- A #2 Vc fills 74/75/246/247/249.
- A #3 Vln II Flautando joins (common tones held, 0.15 s lead, 0.35 qn overlap).
- A #4 Tbn1 213 accent +3 and end 214.25; Marc attack +3 at +0.04..+0.16 s.
- A #6 Hn1 195 breath 0.5 qn + 10 CC fall.
- B #1 `SWELL_NO_SOFT_GAIN`. B #2 Cb pizz. role 5 -> 2. B #3 Fl1 Bb4/C5/Db5 +4/+3/+3. B #4 Vc/Cb bar 30 cadence roles. B #5 Vc [262,265,2,0.25].
- C #1 `LEG_SOFT_EXTRA_S` flute. C #2 `LEG_ART_EXTRA_S`. C #3 per-note leads. C #5 phrase-arc depth (sub/main, x0.97 return beat).
- Measured: master -23.6 LUFS, LRA 23.2, TP -4.5. mp3 -19.8 LUFS, LRA 15.9, TP -1.6, span 18.7, limiter 1.9.
  - Sost median step -1.6 -> -0.8 dB; falls of 4 dB+ 13 -> 8.
  - Vc join holes 4-7 dB shallower. Vln II pad troughs median 10.0 -> 5.4.
  - Tbn1 213 accent +3.2; break before 214.5 13 dB. Hn1 196 breath dip 1.9 -> 7.2.
  - Swells now under the printed peaks (horn 2-3 dB, theme A 4.7 dB). Cb-Vc pizz. +6.7 -> +3.2.
  - Leg Slur crossovers: Vln II/Vla/Vc +0.058/+0.038/+0.068 -> +0.013/+0.015/+0.013 s. Flute solo +0.078 -> +0.038. Listed late notes 0.15-0.27 -> -0.05..+0.17.
Rejected/Open:
- Failed tests, in the render and the tools, to be reverted next cycle:
  - A #5 Detache bar 59: own share 0.32 vs 0.32 control, first dominance later. Set `DETACHE_SPANS = {}` (full Violas rebuild).
  - C #4 `ABUT_LEAD` bassoons: mixed arrivals, and new 11/21.6 dB holes on the same-pitch repeats that follow a led note (qn 22, 32). Set `ABUT_LEAD = {}`.
- Deferred: B #6 low-end bell test, C #6 viola cap exception.
- Open:
  - Fl2/Bn2/Hn3 sost falls of 5.5-6.7 dB.
  - Vln II 114/120 troughs of about 10 dB.
  - Marc Lng attacks are mixed.
  - Vln II 252 is now -0.05 s early.
Do-not-touch:
- `SOST_HOLD_THROUGH`.
- `LEG_ART_EXTRA_S` and `LEG_SOFT_EXTRA_S`.
- The c15 Horn 1 leads.
- `SWELL_NO_SOFT_GAIN`.
- The Cb pizz. role 2.
- The Vc fills 74-249.
- Phrase-arc depths, unless a bar-tempo table says otherwise.

## Cycle 16 (2026-10-11)
`--midi-only --tempo` update of 28 tracks. Violas were fully rebuilt (the Detache row was unloaded and the Stac Leg row loaded). Then a restart and one render. Attack gate 19 of 19.

After the render, the tied-slur rule had made the violas' qn 262 entry a first Leg Slur note, 6-9 dB low. I fixed the tool (`slur_out` only) and updated Violas with `--midi-only`. Viola stem qn 261.6-267.85 was spliced from c15 (with the new envelope), and the master was rebuilt as the stem sum.

Accepted:
- Reverts: `DETACHE_SPANS`, `ABUT_LEAD`.
- A #1 `build/loop_fills.json` (seam lifts, 43). A #2 `FLAUT_LEAD_S` 0.45 / `FLAUT_OVERLAP_QN` 0.7, Vln II [114,116,3]. A #3 test `STACLEG_SPANS` (bar 59).
- A #4 `slur_out` / `same_slur` (a slur starting on a tied continuation), loud bow notch 6 CC, no CC1 dip on loud in-slur targets. A #5 no `SOST_NOTCH` under `SOST_HOLD_THROUGH`.
- B #1-#5 roles and trims (Ob1 271 fill 3 / [271,274,-4], Fl1 271 +3; Ob1 144 +7 / 145.5 +3; bar 79 tenor line; reprise -2.5; Bn2 `_skip_onsets` 268).
- C #1 climax low octave: roles [200,214] / [258,269] with end ramp 1, and mix.json `loud_eq` (wet-automated ReaEQ; Vc/Cb 150 Hz +4, Cb 80 Hz -3, which absorbs B #6).
- C #2 `tools/auto_fills.py` (110 fills, `_auto`).
- C #3 `TEMPO_PUSH`, `APEX_AGOGIC`, `BEAT_STRETCH`, and two sub arcs removed.
- C #4 `METRIC_VEL`.
- Measured: master -23.0 LUFS, LRA 23.6, TP -2.9. mp3 -19.8 LUFS, LRA 16.1, TP -1.6, span 18.9, limiter 3.2 (one Vln II peak at 207.94, 1.5 dB over the other peaks).
  - Loud centroid 1010 -> 853 Hz; 125 Hz +3.9 dB.
  - Wind/horn joins of 5 dB or more 73 -> 22; Vc 45 -> 25.
  - Bar 82 oboe +4.3 -> -3.5 dB under the tune. Ob1 144 hole gone. Reprise 1.4 dB under theme A. Bn2 269 5.5 dB lower.
  - Bn1 22/32 holes 10-15 -> 3 dB. Vln II troughs at 114/120 gone. Bar 80 sag 4.2 -> 1.3 dB.
Rejected/Open:
- Failed, still on in this render and the tools; to empty next cycle:
  - A #3 Stac Leg: share 0.39 against 0.5, bar RMS 3.3 dB under the control. Set `STACLEG_SPANS = {}` (full Violas rebuild) and close the viola-sextuplet item.
  - C #4: beat-1 lean 0.5-1.2 dB, Cb pizz. std 1.7 -> 3.3. Set `METRIC_VEL = {}`.
- A #1 partial: the deepest seam dips are 6 dB shallower, but the p-p pulse is about the same (master 30-200 Hz bars 89-92 14.1 dB). Refit wider lifts from the c16 stems.
- Open:
  - 9 auto fills overshoot 2-5 dB (Fl1 135/194/200, Ob1 190, CA 152/163, Vc 71/140/263).
  - Vln II 112 trough 7 dB. Bn1/Bn2 21 holes 8-10 dB.
  - Limiter 3.2: the Vln II 207.94 join peak.
  - Bar 79 tenor line now 2-6 dB over the held voices (target about 0).
- Deferred: A #2 fix B (Vln II divisi tracks), C #5 vibrato.
Do-not-touch:
- The tempo shaping (pushes, apexes, the 204/208 stretches).
- `loud_eq` and the C #1 roles (centroid at target).
- `slur_out` (only the outgoing join).
- The B #1/#2/#4/#5 changes.
- `auto_fills.py` rules (rerun it each cycle on the previous render; fix overshoots by hand).

## Cycle 17 (2026-10-11)
`--midi-only` update; every Opus state changed (new hall IR), so all 29 tracks were fully rebuilt. Then save, quit and a `-new` restart. The first open deadlocked in Opus `VST3_LoadState`; I killed it and the second start worked. One render, at 40 GB compressed (file cache from the sample drive). Attack gate 18 of 19: Vln I 171 "+0.34 s" is a probe-threshold artefact, since the stem matches c16 within 1-2 dB from the first sound.
Accepted:
- Reverts: `STACLEG_SPANS`, `METRIC_VEL`.
- A #1 `loop_profiles.json` (periodic inverse profiles; loop_fills emptied; dedupe fixed).
- A #2 `auto_fills.py`: 200 ms windows for Fl/Ob/CA, an overshoot rule, centred windows. 33 entries changed.
- A #3 test: `WIND_VIB_CAP` 67. The patch files show CC1 crossfades Non Vib/Vib layers over 55-76, so 80 would do nothing.
- B #1 horns +3 at both climaxes (`_all` [204,212] -1.4). B #2 Bn2 skip 256/261. B #3 Fl1 262-266 hold lift. B #4 coda Cl1 +2.5, Vln II -2, Vla -1. B #5 Ob1 [55.5,58.5,-3]. B #6 `UNI_DELAY` (Hn4 Ab3 266.9) and Hn4 [86,90,-3].
- C #1 true-stereo hall (`S. Cal Hall Perc TS FR 3.3s`). C #2 tail hold in `vol_points`. C #3 harp seat -0.72/0.12. C #5 Vln II 3 kHz -5 dB `loud_eq` at 139-170.
- Measured: master -22.5 LUFS, LRA 24.3, TP -2.3. mp3 -19.9 LUFS, LRA 16.3, TP -1.6, span 18.9, limiter 3.4.
  - Tail R-L: Vln I -3.9 -> +0.3, Vln II -3.6 -> +0.2, Bn2 +4.8 -> -0.6. Pan centre share 68 -> 76%.
  - Loop pulse 1-6 dB smaller on all 10 notes (Cb 271 11.7 -> 5.3); 5 of 10 at 6 dB or less.
  - Wind joins over +2.5 dB at 200 ms: 13 -> 8.
  - Hn4 bar 80 Ab3 back (+14 dB). Horns at 208-212 +1.3..+3.1. Bn2 bars 77-78 under the tune. Fl1 266 step 8.5 -> 3.0. Coda Cl1 +5.6 over Vln II.
Rejected/Open:
- Failed, still on in this render and the tools: A #3. Flute 1.5-4 kHz modulation 10.5 -> 16.9 dB, stem +2.2 dB. Set `WIND_VIB_CAP = None` next cycle (`--midi-only`).
- Deferred: A #4 Violas div track; C #4. Its condition now holds: low corr 0.50 -> 0.37, so narrow Vc/Cb to 0.28.
- Open:
  - mp3 LRA 16.3 (0.3 over); limiter 3.4.
  - Loop pulse still 7.5-9 dB on Vln I 0/292 and Vc 164: refit the profiles on c17 (new hall).
  - Hn2/Hn3 at 204-208 did not rise.
  - Vln II 2-6 kHz still 4.6 dB over the CA at bars 45-51; try a 2 kHz shelf.
  - Cl1 256 (new auto fill) over +4.9 and Fl1 252 over +4.9.
  - Mid corr 0.61 (target 0.55).
Do-not-touch:
- The true-stereo hall and its fx volume (tails within 1.5 dB of c16).
- The tail hold.
- `UNI_DELAY`.
- The B #2-#6 roles.
- The auto_fills overshoot rule, including its fill-start limit.

## Cycle 18 (2026-10-11)
`--midi-only` update. Five tracks were fully rebuilt: Vc and Cb (width) and three new tracks (stems 30-32). The quit stopped at a modal dialog, so I killed REAPER and did a `-new` restart (open 8 min, no deadlock). One render: 56 GB loaded, 0 GB compressed at the start. Attack gate 19 of 20 (Vln I 171, the known artefact).

After the render, four gain-only fixes were applied to the stems, and the master was rebuilt as the stem sum (exact to 8e-7 before the change):
- a2 horns +4.6 dB.
- Vln II div -1.5 dB.
- Vla div -5 dB from 276.
- Horn 1 qn 34 fill replaced.

Accepted:
- A #1 `WIND_VIB_CAP = None`.
- A #2 "Violins II div" (Flautando, pitch split 64) and "Violas div" (`TRACK_SPLITS` "rank" mode), both on DIV B KS Masters.
- A #3 loop-profile refit (Vc 164 capped at +7). A #4 "Horns 1-2 a2" on 2FH KS Master (`TRACK_WINDOWS` 261-272). A #5 auto_fills rerun plus the critic's lower values.
- C #1 `SWELL_SOFT_GAIN_AT` (+2.5 messa di voce), decrescendos after an mf hpgain shaped, `HP_SOFT_DEC_AT` Ob1 148 4 dB.
- C #2 changed: the "collapse" was L/R anti-phase read on a mono fold (corr -0.7..-0.86). There is one 7 dB stereo-power frame, so one +4 dB lift at moved+0.825 s, and the probe uses stereo power.
- C #3 `JOIN_NOTCH` Vln I 208, `_all` end_ramp 3.5, string sf roles. C #4 phrase tops (`PT_*`). C #5 `_all` pp lifts.
- c17 C #4: Vc/Cb width 0.28.
- Measured: master -22.5 LUFS, LRA 23.6, TP -4.1. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.6, limiter 1.7 (was 3.4).
  - Flute AM 15.5 -> 8.1 dB.
  - Theme A < > now the printed way (+1.1/-2.3 and +3.4/-2.1 dB). Oboe 148 > falls 3.9 dB.
  - Phrase tops median +1.3 -> +3.7, loudest in 13 of 23.
  - Bar 62 sag 1.6 -> 0.2 dB; sf +1.2 dB.
  - Loop pulse Vln I 0/292 5.7/5.8, Cb 220 1.9, Vc 164 7.2.
  - Divisi sums within +0.8 / -0.8 dB of c17; a2 horns within 0.0.
Rejected/Open:
- Not added: the C #5 extras (LRA already 16.0).
- Open:
  - No tail hold after a track's last note (roles ending later move the tail).
  - Ob1 143 / CA 132 / CA 134 200 ms dips 6.4-7.2 dB after the lowered fills (rerun auto_fills on c18).
  - Vc 164 pulse 7.2.
  - REAPER quit (40004) can stop at a modal dialog.
Do-not-touch:
- The three new tracks, their gains (a2 +0.6, Vln II div 8.5, Vla div 6 with [276.5,304,-5]) and the rank split.
- `WIND_VIB_CAP = None`.
- `JOIN_NOTCH` and the climax roles (limiter 1.7).
- `SWELL_SOFT_GAIN_AT`.
- The phrase-top rule (`PT_*`).
- The Horn 1 34 lift (stereo-power probe 3.3 dB).

## Cycle 19 (2026-10-12)
`--midi-only` update of all 32 tracks (no state changes). Save, then quit stopped at the modal dialog, so REAPER was killed and reopened with `-new` plus `Main_openProject`. One render: 62 GB, 0 GB compressed at the start. Attack gate 19 of 20 (Vln I 171, the known artefact). No post-render fixes.
Accepted:
- A #1 `find_unisons` skips notes that `TRACK_WINDOWS` moves away (Hn4 Ab3 265-268 whole). A #2 auto_fills rerun; CA 132/134 lower, longer shapes.
- B #1-#6 roles: BCl/CA bars 31-33, Hn1 crest -2.5 (not -3), CA bar 42 -3.5, BCl/Fl1 bar 37, a2 horns [269,278,-5], Violas [204,212,2.5], Hn3 [86,90,-3]; Cb ppp soft trim 1 -> 4.
- C #1 Hn1/Ob1 pair leads, leg_leads Hn1 201, BCl 92.5/106. C #2 `CAESURA_BREATH_QN` 0.12 (entry extras at 268 kept). C #3 `LEG_CAP_FRAC` violas 0.75 + pair leads. C #4 violin/cello leg_leads. C #5 tail hold after each track's last note. C #6 `ABUT_LEAD` with an `at` list (Bn1 27/35/36/38).
- Measured: master -22.4 LUFS, LRA 23.7, TP -3.8. mp3 -19.8 LUFS, LRA 16.1, TP -1.6, span 18.5, limiter 2.0.
  - Hn4 bar 80 hole (to -86 dB) gone. CA 132 dip 7.2 -> 3.3.
  - BCl over CA bars 31-33 12-17 -> 7-10 dB; Hn1 crest -30.9 -> -33.9 (1.5 over the bar 8 swell); a2 horns at 270-271 under Vln I.
  - 20 listed legato notes from 0.12-0.18 s off to within 0.08 s (Vln II 80 +0.19, at its cap). Viola triplets median +0.053 -> -0.017 s.
  - Wind breath dip before 204 3.2 -> 2.0 dB. Final Cb tail no longer rises.
Rejected/Open:
- A #3 Cb loud lead deferred (critic's spread wider than the shift; c15 failure).
- Open: Bn1 36/38 holes deeper (8.1 -> 11.5, 4.7 -> 6.1 dB) after the abut lead; mp3 LRA 16.1; limiter 1.7 -> 2.0 (violas in the 207.65 peak); rerun auto_fills on c19 (17 proposals).
Do-not-touch:
- The `find_unisons` window rule; `CAESURA_BREATH_QN`; `LEG_CAP_FRAC`; the final tail hold.
- The c19 leg_leads and pair leads (both metrics agree now).
- The B #1-#4 roles; the Hn1 crest at -1.0 (keeps it over the bar 8 swell).

## Cycle 20 (2026-10-12)
`--midi-only --tempo` update of all 32 tracks. Harp and Harp harmonics were fully rebuilt (width change). Save, quit, `-new` restart, open. One render: 23 GB and 0 GB compressed at the start. Attack gate 18 of 20: Vln II and Vc 212 dip 6.7/7.6 dB against the 6 dB limit, but the stems match c19 within 1 dB, so these are threshold noise. After the render, gain-only fixes went to the Violas, Violas div and Harp stems, and the master was rebuilt as the stem sum.
Accepted:
- A #1 `ABUT_LEAD` Double basses (lead 0.16 s, `skip_next_same`). A #2 13 single seam lifts (loop_fills). auto_fills rerun on c19 (15 entries; CA 132/134 and Fl1 257.5/258.5 excluded).
- B #1 Violas/Vla div [66,80,3] / [80,87,0.5] (after the render; 3 was too much) / [87,90,-3]; Violas [108,124,-1.5].
- B #2 bar 60 reeds -2..-4, Fl1/Ob1 +2.
- B #3 Harp [172,180,2] / [180,188,-1] (after the render; the side shelf had taken 3 dB).
- B #4 Fl1 fills 257.5 2.0 / 258.5 2.5, note trim 258 -3.
- C #1 `_all` [250,258.5,-3,5.5] / [259,262,1.5,0.5] and `ARRIVAL_HOLD_SPANS` (259).
- C #2 mix.json `side_shelf` (M/S encoder, side-only ReaEQ, decoder): bass tracks 200 Hz -6, harp 300 Hz -8 with width 0.3.
- C #3 `METRIC_DB` level steps on plucked onsets.
- C #4 pushes 93-99 and 140-147, beat stretches 97 and 147.
- Measured: master -22.6 LUFS, LRA 23.6, TP -3.8. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.5, limiter 2.2.
  - Cb crossover +0.20 -> +0.03 s (Cb - Vc +0.165 -> +0.06).
  - mp3 bars 75 -> 78 +1.5 -> +5.4 dB, rising every bar; bar 79 unchanged.
  - Master corr <120/120-250 Hz 0.52/0.39 -> 0.88/0.71; harp 120-250 -0.42 -> 0.70.
  - Plucked downbeats +0.5..+2.9 dB (were -1.6..+1.3).
  - Violas 3-5 dB under Vln I in bars 23-29 (were 6.5-10). Seam dips 8-11 -> 4-6 dB, except Cb 168 at 6.6.
Rejected/Open:
- The side shelf overshoots: <120 Hz corr 0.88, 100-250 Hz share -0.6 dB. Try -3 dB on the bass tracks next cycle.
- The harp lost 1-3 dB in every passage to its shelf; consider a harp gain of +1.5.
- Open: Cb 168 seam 6.6 dB; new Cb 80 trough of 7.7 dB for 0.06 s; limiter 2.2 (Vln I 207.87 join); bar 26 violas +1.8 over Vln II in RMS.
Do-not-touch:
- The Cb `ABUT_LEAD` entry and `skip_next_same`.
- `ARRIVAL_HOLD_SPANS` and the C #1 `_all` rows.
- `METRIC_DB` values.
- The B #2 bar 60 rows; the B #4 Fl1 values.
- The side-shelf chain itself (only its dB values are open).

## Cycle 21 (2026-10-12)
`--midi-only` update of all 32 tracks (no state changes). Save, quit, `-new` restart, open. One render: 21 GB at the start; it ended at 63 GB with 51 GB compressed. Attack gate 18 of 20 (Vln II/Vc 212, the same values as c20). No post-render fixes.
Accepted:
- A #1 16 `JOIN_NOTCH` entries. A #2 fills lowered by hand (Ob1 145, Vln I 68/80, Vc 156/256, Fl1 129.5/193/194). A #3 Tbn1 218 accent 4.5. A #4 Vln II 172 fill. auto_fills rerun on c20 (8 entries; Vc 203 and Fl1 200 excluded because they flip on and off).
- B #1 Vc/Cb [188,204] -3/-1, Vc trims 190 -1.5 / 193 -3, Bn2 skip 193/198. B #2 Fl1 [191.5,196,-3]. B #3 Fl1 [112,124,2] and short-note trims +4. B #4 Hn1 [176,188,0.5], 180 -2. B #5 Harp 26 -5, with plucked note trims now a step on the attack.
- C #1 bass side shelf -2. C #2 Cb `loud_eq` 100 Hz -6 with wider ramps. C #3 `loud_eq` lists, Cb pizz. 90 Hz -5 at 108-140. C #4 `side_shelf` band lists: winds/brass high shelf 250 Hz +1.5, div tracks +3.
- Measured: master -22.5 LUFS, LRA 23.6, TP -3.9. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.5, limiter 1.9.
  - Spiking joins 62 -> 47; all listed joins under 5 dB except Vln I 72 (5.9) and Ob1 145 (5.8).
  - Tbn1 218 +3.2 over the eighths. Harp 26 -5 dB. Horn over the harp at 176-188. Fl1 median -1.4 under Vln I in bar 58.
  - Master corr 25-60/60-120/120-250 0.90/0.88/0.71 -> 0.71/0.75/0.56; 250 Hz-2 kHz 0.62 -> 0.56. Loudest 10% 60-100 Hz -13.4 -> -15.9.
Rejected/Open:
- Deferred: A #1b `auto_notches.py`, A #2b the 30 ms overshoot test in auto_fills.
- Open:
  - New spikes Hn1 180 (+5.0) and 202 (+5.4, the auto_fills raise to 8.0), Vln I 249.5. Ob1 145 needs a notch.
  - Bar 56 -> 57 still -1.7 dB in RMS.
  - Vc bars 57-58 now level with Vln I in RMS (check K-weighted).
Do-not-touch:
- The c21 `JOIN_NOTCH` entries and the hand-lowered fills (noted in `_auto`).
- The bass side shelf at -2 and the wind/brass/div side high shelves.
- The Cb `loud_eq` specs.
- The plucked note-trim step.

## Cycle 22 (2026-10-12)
`--midi-only` update of all 32 tracks (no state changes). Save, quit, `-new` restart, open. One render: 21 GB at the start, 42 GB compressed during the render. Attack gate 19 of 21 (Vln II/Vc 212, the same values as c20/c21). No post-render fixes.
Accepted:
- A #1 CC pull fix (`PULL_PAD_QN` 0.01, on the 4-decimal grid; CC1 at the pull's end); compensations removed (Bn1 196 trim, Hn4 286 -5 -> -1, Hn3 204 fill 8 -> 2 and lead 0.10 -> 0). A #2 five `JOIN_NOTCH` entries; Hn1 fills 180 2.5 / 202 6.5. auto_fills rerun on c21 (3 entries; flip-flop and hand-set notes excluded).
- B #1 `SWELL_CC_CAP` Bn2 B flat 2 at CC 36 (patch table: the f layer fades in over CC 33-38). B #2 Cb E flat 2 notches. B #3 Vc bar 60 notches. B #4 Harp [238,262,4].
- C #1 `HP_SOFT_GAIN_AT`, `HP_SOFT_EXTRA_SPANS` (Hn1 174-184), Ob1 57 dec 5, Hn1 32 F4 trim skipped / note -2, no phrase tops inside soft lead hairpins. C #2 `HP_MF_BRIDGE_REL` (mf gain held into the next crescendo, qn 188), Vc role split. C #3 coda notches at 286; no CC bloom on a crescendo's arrival. C #4 `HP_GAIN_SOFT_ACC_DB` 2.5 on accompaniment soft hairpins (`HP_SOFT_ACC_SKIP` 298). C #5 `_all` morendo -1/-2/-3.
- Measured: master -22.5 LUFS, LRA 23.6, TP -3.9. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.5, limiter 1.8.
  - Bn1 229 attack +14.8 -> -3.1 dB over body (master +5.5 -> -0.7); Hn3/Hn4 286 +4.1/+7.0 -> -3.4/-3.7; Bn1 196 bulge gone.
  - Spiking joins 46 -> 37; all listed joins under 5 dB.
  - Cb E flat 2 swells 4-6 dB lower; Vc bar 60 peak -17.0 -> -22.0; harp bars 71-78 +4.0.
  - Solo hairpins: Hn1 176 +4.5, solo violin 60 +3.8; coda fall after 286 5.2 -> 2.9; morendo 3.6 -> 6.0 dB.
Rejected/Open:
- Not met: solo violin 48 (+1.8), Hn1 32 (+1.3), Fl1 126 (+0.7; F5 sustain sag) against +3; bar 56 sag 4.8 (sim 3.8); Bn2 swells only 2 dB lower (still 5 dB under the horn; cap 34 or a role next); phrase-scale movement 1.253 -> 1.229.
- New: Vln I 244 join spike +5.1; Cb 140 pp entry 3-5 dB softer for 0.4 s (CC1 now the entry's own).
- Not done: B #5 items; C #2(c).
Do-not-touch:
- The pull pad and the removed compensations (re-measure before re-adding any).
- The c22 notches (Cb E flat 2 positions follow the c21 tempo map and abut lead).
- `HP_GAIN_SOFT_ACC_DB` and `HP_SOFT_ACC_SKIP`; the morendo rows; the 286 bloom skip.

## Cycle 23 (2026-10-12)
`--midi-only` update of all 32 tracks (no state changes). Save, quit, `-new` restart, open. One render: 20 GB at the start, 44 GB compressed during the render. Attack gate 19 of 21 (Vln II/Vc 212, as in c20-c22). One post-render gain fix: the Vln I 73.5 join spike moved 0.1 qn out of its notch (+4 dB on the master); notch widened to (73.37, 73.55, -5.5), applied to the stem, master rebuilt as the stem sum.
Accepted:
- A #1 unison fills Vln I/Vln II 65.5/74/80/84/87/240. A #2 + C #1 + C #2 entry leads and fills (Violas 0/42/66/238/277, Cb 140, Vln II 0/108, Vln II div 108, Vla div 66/277, Bn1 196/229). A #3 five `JOIN_NOTCH` entries. A #4 `REP_RETONGUE_AT`. auto_fills rerun on c22 (2 lowered; hand-set and flip-flop entries excluded).
- B #1 `SWELL_CC_CAP` "*" (start CC, at CC <= 40) on Bn1/Bn2/BCl/Cbn/Cl2, checked against all four patch tables. B #2 low-octave rows from 261.5. B #3 Vc [73.5,78,-2] / [245.5,250,-2]. B #4 Cl1 [287.4,289,2.5].
- C #3 `SOST_JOIN_LEAD_S` (Ob1 210). C #4 leg_leads Vln II 206, Vc 255, Bn1 100, Ob1 200. C #5 viola falling-step pair extras.
- Measured: master -22.5 LUFS, LRA 23.7, TP -4.0. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.5, limiter 1.7.
  - Unison sum dips 4.9-7.2 -> 1.6-4.5 dB; master at 65.5 6.1 -> 3.3.
  - Slow entries Vla 42 +0.65 -> +0.11 s, Cb 140 +0.61 -> +0.31, Vln II 108 +0.54 -> +0.27; entry median 0.07 -> 0.05.
  - Join bumps 4.6-8.2 -> -0.2..+2.8 dB. pp swell median +3.3 -> +1.2 dB. Bar 78 Bn2 now 2-6 dB under Vln I.
  - Ob1 210 rise +0.305 -> +0.095; C #4 joins +0.05..+0.15; viola falling steps within -0.04..+0.03.
Rejected/Open:
- Open: Bn2 140 B flat 2 still +7 dB (sample swell at flat CC 33); horn repeats dip only 1.1-2.3 dB (target 2.5); new spikes Vln I 74/240 on their A #1 fills and Violas 292.
Do-not-touch:
- The c23 unison fills except Vln I 74/240 (sum dips now under 4.5 dB).
- The entry leads and entry fills (no overshoot).
- `SWELL_CC_CAP` "*"; the 261.5 low-octave start; `SOST_JOIN_LEAD_S`.

## Cycle 24 (2026-10-12)
Full rebuild of all 32 tracks (every Opus state changed: unused rows unloaded). Save, quit, `-new` restart, open. Memory: the c23 project settled at 61 GB after a fresh open; the c24 project settles at 43 GB and the render peaked at 44 GB with 0 GB compressed (c23: 63 GB, 44 compressed). One render; no post-render fixes. Attack gate 18 of 21: Vln II/Vc 212 as before; Vln I 171 reads +0.34 s on audio identical to c23 (threshold noise).
Accepted:
- A #4 `UNLOAD_UNUSED_ROWS` in `build_reaper.py` (rows a track never plays are unloaded; harp single rows kept). No sound change: every stem without data changes is bit-identical to c23 before qn 151.5.
- A #3 pre-roll CC36 = 127 (round-robin reset) on every non-harp track and CC69 = 0 (Repetition script off) on the strings (`RR_RESET_QN` 0.1). Bn1/BCl now play other RR samples (same level). Reproducibility is checked by c25 vs c24.
- A #1 `JOIN_NOTCH` Vln I/II 86.5 and 259, Fl1 259/266. A #2 Horn 1 leg_leads 18/26/27/30/39/199.
- B #1 Hn1 [179.25,180.75,-6.5]. B #2 `HP_SOFT_ACC_SKIP` 283, Cl1 [284.25,285.75,3]. B #3 Harp harmonics 276 +5 (plucked-step trims now cover "harm"). B #4 Vc notch (274.70,275.30,-3). B #5 `NOTE_TRIM_RAMP_S` Ob1 42/54 0.1 s.
- C #1 Hn1 [20.5,23.5,-2.5,1], `SWELL_SOFT_GAIN_AT` 68 removed, Vln I/II trims 83 +2.5 / 84 +1. C #2 Ob1 [140,143,-2,0.5]/[148,151,3.5,2], Vc [148,151,3,2], `MERGE_NOTCH_AT` Vc 148 3 CC. C #3 `tools/motion.py` in `render_cycle.py`. C #4 coda accompaniment [283,291.5,-2,0.5] (Hn3/Hn4/Vla/Vla div/Vc/Cb), Cl1 [283,292,1.5,1]. C #5 `PHRASE_ARCS` (152,160,"sub"), (160,168).
- Loop rule (C #3): when a solo crest covers another voice, lower the covering voice or the accompaniment first; lower a crest only if it then stays 3 dB or more over the earlier swells of its own phrase. A fall of more than 0.2 dB in the motion figures is a regression to justify.
- Measured: master -22.5 LUFS, LRA 23.7, TP -3.9. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.4, limiter 1.9. Motion mp3 dS4 p90 5.00 -> 5.12, 1 s/20 s 2.84 -> 2.86.
  - Master bumps 86.5 +6.0 -> +2.1, 259 +5.0 -> +1.8, 266 +3.9 -> +3.1. Spike scan 35 -> 33.
  - Hn1 opening joins crossover +0.14..+0.20 -> +0.02..+0.10 s (27 rise-6 still +0.14).
  - Hn1 over the violins at bar 55 +6.7 -> +1.1 dB (plain power). Horn crest over bar 8 swell +0.9 -> +3.4; Vln I crest over bar 24 swell +0.8 -> +2.9.
  - Bar 47 mf over bar 45: oboe -1.0 -> +4.5, master +1.7 -> +4.9. Coda Cl1 over all others -3.7 -> -0.5 (median); Vc ppp<pp rise 8.5 -> 6.4.
Rejected/Open:
- Deferred: drop `PORT_TARGETS` and B #6 track merges (memory target met); C #4 Cl1 taper cap (role used instead).
- Open: run `det3.py` c24 vs c25 on the strings; if they still decorrelate, try `Repetition3` `active: False` in `state_for()`. Then notch Vln I 72/74/240 and recheck the variable-span notches. Hn1 27 rise-6 +0.14. Fl1 266 stem still +5.5. Vln I 252 new spike (+5.1, master +1.6).
Do-not-touch:
- `UNLOAD_UNUSED_ROWS` (memory; proven sound-neutral). The pre-roll CC36/CC69 until c25 shows its effect.
- The c24 notches, Horn 1 leads and C #1/C #2 roles.
- The coda balance (B #2 + C #4 together); `HP_SOFT_ACC_SKIP` 283.

## Cycle 25 (2026-10-12)
`--midi-only` update of 9 tracks (no state or tempo changes). Fresh `-new` open, one render. Memory 44 GB settled and at the render peak, 0 GB compressed; REAPER saved and quit afterwards. Attack gate 18 of 21 (the same three as c24). No post-render fixes.
Accepted:
- A #1 Cl1 coda lifts held to 297 (2 qn release), Cl1 292 +3 (3 s ramp), Cl2 [286,295,-2]. A #2 BCl 93 `JOIN_NOTCH` (cut, fill, step). A #3 Ob1 190 -4, Cl1 256 -2 (steps), Vc 180 -2 (1.8 s), Ob1 45 2.1 s ramp.
- B #1 Vc 204 -3, 265 -4. B #2 Timpani ppp rolls +4/+3/+4. B #3 Horns a2 261 -3 (0.1 s; key is the score onset). B #4 BCl 108 -3.
- C #1 Cb static bell2 80 Hz -6 (new `bell2` = ReaEQ band 2), 160 Hz +4.5, pizz loud_eq removed, climax shelf -3.
- auto_fills on c24 (Ob1 143 raised, Hn1 26 new; hand-set and flip-flop entries excluded).
- Measured: master -22.6 LUFS, LRA 23.6, TP -4.2. mp3 -19.8 LUFS, LRA 16.0, TP -1.6, span 18.5, limiter 1.6. Motion mp3 5.06/2.87 (c24 5.12/2.86).
  - Cl1 at 292-295 now 2.7-4.2 dB over Vln I (was 7 under); BCl 93 master attack-to-trough 7.9 -> 2.4 dB; trim holes at Ob1 190/Cl1 256/Vc 180 gone, Ob1 45 now falls across the bar.
  - Vc A flat 3 -2.6/-3.6 dB; timpani ppp rolls +3..+4; horn pickup peak -1.6 dB (0.7 under its f arrival); Fl1 over BCl at 108.5-109.5 +3..+4.
  - Cb low end as simulated: loud 30-100 median -17.0 -> -20.4, p90 -9.0 -> -13.3; bars 23-29/65-66 -16.9/-15.2; Db2/Eb2 f0 -5.1/-11.0; Cb 120-400 Hz +0.3..+0.5.
  - det3 c24 vs c25: strings 1-4% decorrelated (reset works), Fl1 12%, Bn1 20% with no data change.
Rejected/Open:
- Cl1 292 is 2 dB hotter than simulated (1.7 over its bar 88); +3 -> +1 if judged too prominent. Horn pickup fell 1.6 not 3 dB. Loud 100-250 -6.9 (C asked -6.6 or higher).
- Open: Cb F2 +3.9 (pitch trim 41 -2 next); Fl1/Bn1 still not reproducible (Repetition script on winds?); then Vln I 72/74/240/252 spikes and Hn1 27 can be notched against a stable render.
Do-not-touch:
- The Cb EQ set (bell2 80, 160 +4.5, climax shelf -3, no pizz shelf). The pre-roll CC36/CC69 (strings now reproducible).
- The c25 coda roles, the BCl 93 notch, the reshaped trims (re-measure with `trimsim.py` before adding trims back).
- The timpani ppp roll rows; the Vc 204/265 trims.

## Cycle 26 (2026-10-12)
Fresh `-new` open; `--midi-only` update of 13 tracks, with Tbn1, Vln I and Vln II fully rebuilt (row changes). Save, quit, fresh open, one render. Memory 44 GB settled and at the render, 0 compressed; saved and quit at the end. Attack gate 18 of 21 (same three as c24/c25). Post-render gain-only fixes (re-bow level shapes, chord balance rows, Tbn1 swell values) applied to six stems, master rebuilt as the stem sum; first render in `c26-actor/render1/`.
Accepted:
- Item 8 (A #1, C #1): `REBOW_AT` staggered Sus MAX re-bows of the held final chord, split at the output (CC/vol of the held note kept); `NOTCH_SKIP` Vln I 295/298/301, Vln II 289/292; final-chord loop profiles removed; `JOIN_NOTCH` 292 fills Vla/Vc/Cb at half of C's dB; `build/rebow_fills.json` (per-re-bow level shapes fitted on render 1); roles [292.5,304] Vla -3.5, Cb -4, Vln II +2.5.
- Item 9 (A #2, B #3, C #2): Tbn1 212.5/213/218 on Sus MAX (`ACCENT_ART_AT`), no CC11 bump (`ACCENT_BUMP_AT`), v96/96/92, swell +4.5/+3.0/+6.0 dB in seconds (`ACCENT_SWELL_S_AT`).
- B #1 Cl1 292 trim and ramp removed. B #2 `HP_TARGET_AT` Hn3/Hn4 268 -> p, Ob1 [268,271,4] removed. B #4 Hn3/Hn4 [86,90,-5.5]. C #3 coda rows from 282.25, Cb [274,282.5,2]. A #3 Timpani loop profiles 226/292. vol_db held after the last release.
- Measured: master -22.6 LUFS, LRA 23.6, TP -4.1. mp3 -19.8 LUFS, LRA 16.0, TP -1.7, span 18.5, limiter 1.7. Motion mp3 5.19/2.87.
  - Final chord master 100-300 Hz: loop autocorrelation 0.58 at 3.94 s -> best 0.24 at 1.68 s; centroid 0.39 -> 0.19. Re-bow dips after the fill: master median -2.3 dB (c25 control -1.9). Section means within 0.8 dB of c25.
  - Tbn1 2-5 kHz attack minus body +6.9/-0.9/+12.7 -> -0.8/-3.2/-9.4; master 2-5 kHz jump at 218 +10.1 -> +2.1; bodies +2.6/+3.9/+0.9 over the eighths' mean.
  - Cl1 292-296 now falls (-46.6/-50.9/-54.8); bar 81 horns -1..-5 dB, Ob1 -4; bar 30 horns -2.5; timpani loop pulse 4.2 -> 1.0 and 2.6 -> 1.1 dB.
Rejected/Open:
- C #3 had no effect on the Vla/Vc ppp<pp rise (only Cb, +1.0 -> +1.6); find which item flattens 283-286.
- 100-300 Hz residual p2p in the chord rose 4.8 -> 7.1 dB (irregular, no period); Tbn1 Sus MAX attacks start 2-10 dB under their body in the first 60 ms (check that they do not read as late).
- Deferred: CC1 56 on the final chord; `_all` morendo -4.5; c25 opens (Cb F2, Fl1/Bn1 reproducibility, Vln I spikes, Hn1 27).
Do-not-touch:
- `REBOW_AT` points and `rebow_fills.json` (fitted to these re-bows: refit both together if either changes, or if a string patch, mic or hall changes).
- The Tbn1 Sus MAX accents and the no-bump CC11; the marcato eighths.
- `HP_TARGET_AT`; the bar 30 horn rows; the timpani loop profiles.

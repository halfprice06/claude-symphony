# Cycle 07: changes (actor, on the c06 render)

Snapshot in `before/`; the data rendered is in `build_render/` (parts.json, mix.json, score_config.py, roles.json,
leg_leads.json, entry_leads.json as rendered). Scripts in `actor_scripts/`: `wet_mix07.py` (returns and sends),
`mix07_more.py` (string Close mics, timpani and harp EQ), `width07.py` (Main mics at the seat, side shelves) write
`build/mix.json`; `check07.py N` measures a render (`check_c06.txt`, `check_c07.txt`). The return simulator lived in the
scratch folder (deleted); its method is below and in LEARNINGS.

## 1. Wetness (priority 1: Dan's "too wet, mushy"; critics A #1, B #1, C #1; ONE_TIME decay limits; the orchestrator's hard limit)

Method. The c06 master is the dry stems plus the four return stems. For each return I estimated its 2 x 2 transfer
(send input -> return stem) by averaged cross-spectra. The send input is the sum of the original dry stems
(`render_first/` where the stem fix had replaced them) times their send gains. I used rectangular 10.9 s windows with
the lag weight corrected. Re-convolving reproduced each return stem to -19..-24 dB residual. The simulated c06 master
matched the real one: G.P. drop at +0.3 / +0.6 / +1.0 s 13.0 / 18.9 / 27.4 dB (real 12.9 / 19.0 / 28.8); time to -20 dB
0.67 s (real 0.65). The model is exact for return faders and return EQ and near-exact for per-track sends. For the IR
envelope it is approximate (modelled as a linear fade over the first half of the IR).

Simulated on the c06 stems (master; "cuts" = median of the detected tutti cut-offs; G.P. = bar 340):

| variant | cuts +0.1 / +0.3 / +0.6 dB | cuts t20 | G.P. +0.3 / +0.6 / +1.0 dB | G.P. t20 | tail 60-250 Hz share |
|---|---|---|---|---|---|
| c05 (real) | 12.0 / 18.9 / 24.7 | 0.25 s | 21.5 / 30.1 / 41.9 | 0.25 s | -7.9 dB |
| c06 (real) | 7.4 / 12.2 / 19.0 | 0.59 | 12.9 / 19.0 / 28.8 | 0.65 | -6.9 |
| A: S/W -5, B/P -3 | 8.5 / 14.8 / 20.8 | 0.45 | 14.8 / 20.8 / 29.2 | 0.48 | |
| B: all -6 + HPF 180 | 10.2 / 16.1 / 22.0 | 0.43 | 16.1 / 22.0 / 30.7 | 0.47 | |
| C: S -4.5, others -2 | 8.2 / 13.9 / 20.4 | 0.45 | 14.4 / 20.4 / 28.8 | 0.56 | |
| register sends -16 dB alone | 6.8 / 12.7 / 19.0 | 0.57 | 12.1 / 19.0 / 25.9 | 0.66 | |
| IR envelope 0.5 / 0.5 alone | 7.5 / 12.8 / 22.0 | 0.50 | 13.7 / 22.0 / 37.1 | 0.53 | |
| reg -16 + env + HPF 180 + all -3 | 9.3 / 14.8 / 23.7 | 0.49 | 14.8 / 23.7 / 37.9 | 0.50 | |
| same + 2.3 kHz return low-pass | 9.5 / 14.8 / 23.9 | 0.45 | 15.1 / 23.9 / 38.1 | 0.49 | |
| **chosen: low sends off, trumpets -6, env, HPF 180, all -6** | 10.5 / 16.1 / 25.6 | 0.40 | 16.6 / 25.6 / 39.4 | 0.47 | -8.7 |

Chosen (it is also the finale's c07 recipe):
- all four return faders -6 dB (R Strings / R Brass / R Winds 1.03 -> -4.97, R Perc 0.66 -> -5.34);
- each return's ReaEQ keeps the template's bands, with the high-pass moved from 87 / 100 to 180 Hz (critic B; S4's
  low-cut rule);
- Spaces II IR envelope on every return: irSetup envelopeMode 2, endPos 0.5, decayLength 0.5 (ONE_TIME fix order 2);
- register sends (research batch 5 item 1, ONE_TIME fix order 1, the orchestrator's note): no hall send from
  Bassoons 1-2, contrabassoon, trombones, bass trombone, tuba and basses (`"sends": {dest: -150}`; an empty list would
  leave the old send in REAPER); trumpets 6 dB under their family (`send_offset_db`).
- Not adopted: the 2.3 kHz return low-pass (batch 5 item 2). It moved the simulated drops by 0.0-0.3 dB, so it does
  nothing for wetness. The master's top end is now too bright (below), but the returns carry little of that.

Measured on the c07 render (`check07.py`; c06 in brackets):
- G.P. drop at +0.1 / +0.3 / +0.6 / +1.0 s: 11.3 / 20.9 / 31.2 / 46.1 dB (7.4 / 12.9 / 19.0 / 28.8). Target at +0.3 s
  was 15, better 18-20: met. Time to -20 dB 0.27 s (0.65), RT60 (2 x T-5..-35) 1.38 s (2.46).
- Final chord: +0.3 s 19.5 dB (11.4), t20 0.32 s (0.59), RT60 1.68 s (2.02).
- Soft string ends (Violins I + R Strings, -10 dB): 0.16 / 0.31 / 0.25 s (0.13 / 0.44 / 0.33).
- Returns against the dry stems: -13.4 dB of energy (-4.8). The finale measured -12.5.
- Master band shares: 100-300 Hz -7.2 dB (c06 -5.7, c05 -6.7); 200-500 Hz -5.5 (-5.1).
- Hard limit (no wetter than c05: tutti 20 dB fall 0.50 s or less, RT60 1.5 s or less, soft ends 0.30 s or less): met
  at the G.P. (0.27 s, 1.38 s). The final chord's RT60 is 1.68 s: the harp, timpani and Hn 1 close the movement there,
  and its t20 is 0.32 s. One soft end measures 0.31 s, 0.01 s over the limit.
- Brightness got worse. The master's 6-20 kHz share went from -27.2 to -24.8 dB (references -28.8..-32.2) and 2-5 kHz
  from -10.4 to -8.7. The dark returns now carry less, and the string Close mics are up. Fix for c08: Movement I's c50
  measured fix (strings family shelf off, brass shelf +1, Violins I 5 kHz -6, Violins II 5 kHz -4).

## 1b. Width (orchestrator note from Movement I c50, checked on our stems first)

c06 had the same anti-phase bass: master correlation below 250 Hz 0.17 and at 250 Hz-5 kHz 0.32, side/mid -2.4 dB.
c05 had 0.84 / 0.65 / -6.7, and the references are 0.54-0.62 / 0.47-0.56 / about -5. I ported Movement I's fix
(`width07.py`): on strings, brass, timpani and harp, the Main mics sit at the seat ±0.8 (`pan_by_mic` Main "seat",
`width_by_mic` Main 0.8), and a side-only low shelf (200 Hz, -6 dB) replaces the older side shelves on those tracks.
c07: 0.675 / 0.566 / -5.61 dB, inside or just over the references.

## 2. ONE_TIME (EastWest template MIDI rules) and research batches 5-7

Tool changes. Ported from the finale's c07 `score_to_parts.py` (hand-ported hunks; a three-way merge conflicted in 6
places because the two forks differ): `PHRASE_SHAPE` (with the batch 6-7 shape types), `HP_CURVE`, the list form of
`LEG_VEL_STRONG`, and `LEG_OVERLAP_MIN_S` (new here: `LEG_OVERLAP_MAX_FRAC`). New generic options:
- `HP_CURVE["skip_families"]` (`base_points(curve=)`);
- `SHORT_BEAT_VEL` (written, then switched off, below);
- `RR_RESET_AT` (parts.json lane `rr_reset`; build_reaper sends it on Opus's reset CC 16);
- a fix in `smooth_tempo`: a ramp's end tempo is written at the span's end.

| item | status | values / evidence |
|---|---|---|
| 1 repeat gaps 60-100 ms | adopted | `STR_REP_NEW_BOW` gap 0.06 -> 0.09 s, frac 0.25 -> 0.3; `WIND_REP_RETONGUE` 0.06 -> 0.065 s, frac 0.3; the horns keep their fitted gaps (c04-c06). Violins I tutti pair dips 2.5-9.2 -> 4.8-9.3 dB (stem). Violins II 1.9-2.9 -> 4.7-10.4 dB (with A #3) |
| 2 legato overlap | adopted | floors 60 ms strings, 45 ms winds and brass, at most 35 % of the target's length (critic A); 1,242 joins raised (they were 9-11 ms). Probe legato spread Violins I 74 / Violins II 84 / violas 88 / celli 68 ms, all within limits |
| 3 legato velocity follows the dynamic | adopted | strings and brass `LEG_VEL_STRONG` [(52,100),(65,106),(80,112),(100,118),(127,124)] (the finale's table); the solo at v82 (A #4) |
| 4 CC1 / CC11 phrase shape | adopted | `PHRASE_SHAPE` (the finale's c07 values). Lyrical spans 132-168, 360-420, 456-720, 828-864 and 1020-1128 keep the arch. Driving phrases in the Allegro enter +4, peak +6 at 0.15 of the phrase and fall to -6 (milder than the finale's 6 / 10 / -10). Builds peak at the end. Classes come from the score: a 10 CC printed rise or a crescendo into the last quarter makes a build; otherwise the lyrical spans; the rest is drive. 310 phrases shaped |
| 5 CC11 -> CC1 combo test (pass 2) | deferred | needs pass-2 aliases and memory (45 GB at the cap) |
| 6 string shorts parked high, dynamics by velocity | not adopted | Movement I c51 measured that one velocity table moves HO string short notes between layers by about 10 dB. Their fix (park and compensate in the volume envelope) is for c08 |
| 7 tutti entry spread | not adopted in the Allegro | critic C measured the perceived spread at 40-66 ms already (p10-p90; first to last 50-170 ms); trio at most 15 ms deferred |
| 8 separate string legato tracks | deferred | memory (45 GB settled, the cap) |
| Movement I notes: timpani EQ / Surround | partly | the rolls' timpani share of the master's 30-150 Hz was 12-24 % (33 % in the coda build), against the 31 % Movement I flagged. 84 Hz bell +8.58 -> +4.3 dB, Surround kept |
| brass make-up / brightness | open | the scherzo has no brass accents (score), so the 2-5 kHz accent check does not apply; the c51 loud-tutti brass tone note is for c08 |
| winds hot / harp HP | done / adopted | the c06 stem-fix gains were already in `build/mix.json`. Harp high-pass 183 -> 80 Hz |
| batch 5 #1 register sends | adopted | above (none on low brass, bassoons, contrabassoon and basses; trumpets -6) |
| batch 5 #2 return low-pass A/B | rejected (simulated) | 0.0-0.3 dB on the drops |
| batch 5 #3 hairpin shapes | adopted | `HP_CURVE` cresc (0.4, 0.7), decresc_last 0.35; timpani rolls stay linear (`skip_families`, Movement I c51 critic: a fff -> pp roll rose 8 dB) |
| batch 5 #4 narrow brass | partly | the Main mics now sit at the seat ±0.8 (the width fix); the 15-47 % Close width is not tested |
| batch 5 #5 tempo breaths | adopted | `BEAT_STRETCH` on 22 beats (critic C's list: Allegro joints x0.88-0.94 at 35, 167, 359, 827, 863, 971; trio and Meno mosso four-bar ends x0.92, x0.85 at 671 and 1067); +0.53 s in all. Probe: every attack ok |
| batch 6 #2 / batch 7 beat velocity | written, off | `SHORT_BEAT_VEL` (downbeat +8, beats 2-3 -4, off-beats -6, ±4 seeded) switched off before the render, because of the layer jumps above (Movement I c51). The beat weight goes into the volume envelope in c08 (+1.5 / 0 / -1 dB) |
| batch 6 #3 doublings share one curve | deferred | |
| batch 6/7 spiccato length 50-62 % | already met | string staccato eighths at 0.50 of the slot (p90 0.50-0.65) |

## 3. Critics' findings

| finding | status | change and measured result (c06 -> c07) |
|---|---|---|
| A #1 / B #1 / C #1.1-2 wetness | done | section 1 |
| C #1.3 string Close mics | adopted | Close -9 / -7.7 / -7 / -6.6 -> -4.5 dB under Main on Violins I, II, violas and celli; gains -0.8 / -0.64 / -0.53 / -0.46 dB (power sum). Violins I soft-head dips 43 / 757 / 763: 6.5 / 3.7 / 6.4 -> 5.1 / 5.3 / 5.6 dB |
| A #2 eighths after the accented half note | adopted | `SHORT_SUS_LEAD_TRACKS` Violins I / II / violas 0.06 s, keep-overlap 0.02 qn, cap 45 %; first eighths of the soft statements v53 -> 88; Violins I Sus Marc LITE release 120 ms. Not yet measured with own-pitch dominance (for the c08 critics) |
| A #3 tutti repeated pairs | adopted | Violins I pairs 325 / 331 / 355 / 925 / 931 / 955 on Staccatissimo RRx9, Violins II 313 / 319 / 913 / 919 on Stac RRx9 (-4 dB trim); see item 1. Trumpet 2 StacSs deferred (memory) |
| A #4 solo legato | adopted | v82 throughout, lead 0.15 s, C's per-onset offsets; the solo CC1 lane is deferred. Solo 4.6 dB over Flute 1 (3.9) |
| A #5 Horn 1 Port Lng holes | adopted | 635.5-641.5 and 650.5-656 back on Sus MAX re-tongues; Port Lng kept on 626.5-635.5, 647.5-650.5 and 656-664 |
| B #2 harp pp layer | adopted | `VEL_CAP_SPANS` 42 over 456-504, 552-576, 672-711 and 1020-1044. Harp minus Clarinet 1 at 456-504: -6.4 -> -7.8 dB (RMS) |
| B #3 subito inner voices | adopted | roles Cl1 / Cl2 [360,384] -3 / -4, Ob1 [828,840] -4, Cl2 [828,840] -3. Violins I over the clarinets 0.7 / 0 -> 6.9 / 6.7 dB; Flute 1 over Oboe 1 -3.5 -> +1.5 dB |
| B #4 trio horns | adopted | Hn1 [624,653] -4: Hn1 under Clarinet 1 -2.6 -> +2.8 dB (now under it). Hn3 [504,528] -1: 8.4 dB under the celli (3.7) |
| B #5 counterstatement celli | adopted | roles [90,96] -4, [102,108] -3: the celli now 0.5 / 1.3 dB under Violins I (+3.8 / +0.9 over before) |
| B #6 codetta bassoon | adopted | role +1.5 -> +4.5 (the rows add): Bassoon 1 -42.2 -> -38.9, against Ob1 -40.5 and Cl1 -40.6 |
| C #2.1 leg_leads refit | adopted | C's values into `build/leg_leads.json` (5 tracks; the file now holds 177 onsets); probe spread within limits |
| C #2.2 pickup longs as fresh strokes | deferred | |
| C #2.3 entry leads | adopted | solo 1044 +0.15, celli 368 / 836 +0.15, 504 +0.06 |
| C #2.4 flute "col Vl. solo" lead | deferred | |
| C #3 hemiola / summit stroke leads | adopted | `REATTACK_LEAD_AT` V1 902 0.11, 904 0.13; violas 904 0.25; V2 906 0.15, 910 / 1008 / 1010 / 1012 0.13 (not re-measured with pcx) |
| C #4 pizz round robins | adopted | new `RR_RESET_AT` (celli / basses at 264 / 273 / 282 / 291, violas / Violins II at 756). The celli now repeat one 3-note pattern per printed group (-49 / -48 / -41 dB, before an 8 dB 4-cycle); the basses -43.5 / -43.5 / -46. The group-head trims (C #4.2) are for c08: the loud note now falls on each group's third bar |
| C #5 tempo items | adopted | the breaths above; the trio ramp end now writes 228 at qn 456 (was 226.17) |
| C #6 probe harp references | open | still read "early" (probe artefact, unchanged) |

## 4. Render and numbers

- Build: `--midi-only --tempo` on all 31 tracks (19 with changed Opus states were fully rebuilt: brass, timpani, harp
  and strings for the mic, width and release changes) plus the returns. Restart. A second `--midi-only` on 7 tracks
  (SHORT_BEAT_VEL off, linear timpani hairpins), then a second restart.
- REAPER settled at 45 GB with 1.3 GB compressed; after the render 45 GB with 26 GB compressed.
- Master: -20.8 LUFS, LRA 22.6 LU, true peak -2.3 dBFS (c06 -19.9 / 22.0 / -1.0).
- Delivered mp3: -19.8 LUFS, LRA 14.7 LU, TP -1.5 dBTP, limiter about 2.5 dB, p10-to-max span 19.6 dB (c06 -19.8 / 14.0
  / -1.6 / 3.4 / 19.0).
- Attack probe: every attack ok; legato spread Violins I 74, Violins II 84, violas 88, celli 68 ms (all ok); harp
  references "early" as before (probe artefact).
- Every stem present. No stem fix was needed.
- Lock: I polled from 16:10 (behind mvt2 c44, mvt1 c50 and mvt3 c08, whose waiters started first), then held it
  19:04:40-19:45:20 (40.7 min, including two restarts).
- Disk: cycles/c06's stems, its render_first and Backups/ deleted (c06's mp3 and 00_Master.wav kept); 58 GB free.

## Open for c08

- Brightness (6-20 kHz -24.8 dB): Movement I c50's shelf fix.
- Loud brass tone (Movement I c51 critic).
- Soft-roll timpani low shelf (Movement I c51): check our soft rolls first.
- String shorts parked with an envelope compensation and the beat weight (+1.5 / 0 / -1 dB) in the volume envelope.
- Group-head trims in 89-98 (C #4.2).
- Pickup longs (C #2.2), the flute lead in 349-356, Trumpet 2 StacSs (memory), the solo CC1 lane, the CC11 -> CC1
  pass-2 test, the trio entry spread.

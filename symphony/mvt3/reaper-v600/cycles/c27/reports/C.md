# Critic C, cycle 27 (tempo, timing and transitions), on the c26 render

Data: `cycles/c26/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `cycles/c26/mvt3-mockup-c26.mp3` (decoded to 48 kHz; mp3 times are 0.30 s later than score time), `build/parts.json` (identical to `cycles/c26/parts_rendered.json`), `build/roles.json`, `build/score_config.py`, `build/mockup-events.tsv`, score pages 13, 15 and 16, `cycles/c26/logs/guard26_final.txt`, and the Violins I / Violoncellos KS Master `.oib` files (decompressed myself; I did not use the bridge library, and I did not import or run `build_reaper.py` or `guard26.py`).

My measures (scratch scripts, deleted after this report):
- **Entries (S2).** `tools/pcx.py attack_pcx` on every note that starts after at least 0.15 s of silence on its track: 1,521 notes on 29 tracks. pc = perceived attack, in ms against the score onset.
- **Legato joins.** `tools/pcx.py` on Violins I / II, Violas, Violoncellos, Flute 1, Oboe 1, Clarinet 1, Bassoon 1, Horn 1, Trumpet 1, Trombone 1 (1,790 joins).
- **Fold.** 150-3000 Hz band envelope (30-150 Hz on the master), averaged on the eighth-note grid in score time. I read the half-rise and the peak against the beat.
- **Frames.** 10, 20 and 50 ms RMS frames and quarter-note RMS on the stems, the master and the mp3.
- **Fader lane.** From parts.json `vol_db`: the change between each note's moved note-on and 0.35 s later, and the largest change in any 0.5 s window inside a held note. This leaves out build_reaper's dynamic trims, which I was not allowed to compute.

I cannot hear. "Measured" means a number from the files. "Inferred" means a conclusion from those numbers or from the data.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 27 (the third round ends at c20), so I did not do the page reading. I used `loop/MANUAL-GAPS.md`, `DIGEST.md` and the installed patches. Page numbers are PDF pages of the May 2021 HO manual, as `DIGEST.md` gives them.

| Manual / patch (page) | What it says | Where it applies here | Does the c26 render follow it? |
|---|---|---|---|
| p.98-99, legato | The first note of a phrase has no legato transition; it plays a plain first-note sample | String slur heads after rests: bars 67 (qn 264), 107 (424), 123 (488), 187 (744), 235 (937) | Yes. Patch read: in the Violins I KS Master, a "Leg Slur MAX" note after silence plays the "1V" sustain groups (VoiceTimer start=false, AHDSR attack 12-23 ms). The rise of 0.4-0.5 s is in the recorded soft sample, not in the envelope. Finding 2. |
| p.99 "Legato Slur Staccato" (KS row "StacSl Leg BC + Slur + Port MAX") | Adds a slur-staccato accent to notes with no legato connection: the first note of each phrase gets a slightly stronger attack | The same slur heads | Not used, and not listed in MANUAL-GAPS.md. It is a candidate for finding 2. |
| p.91-92 Sus Marc LITE | A marcato sample plus the sustain: extra power at the start of the note | The accented ff "espress." swell heads at qn 1016 (Violins II, Violas, celli) | Violins I uses it on its chords (v92). c24 rejected it on the lower sections at other chords (late starts). Not tried at 1016. |
| Patch read (c23): Global Group CC11 `fadeTime` 120 ms in the KS Masters | A CC11 move shorter than about 0.12 s is smoothed | Any CC11 front or cut-off ceiling suggested below | Taken into account: every CC change I propose lasts 0.2 s or more. |
| p.151: send CC1 / CC11 before the first note | | Pre-roll | Followed (3 qn pre-roll, mp3 head 0.30 s). |
| MANUAL-GAPS #2 (Rep rows), #8 (slower legato transitions) | | Chorale repeats; cantabile joins | Joins are centred (string medians -14..+17 ms), so #8 brings no timing gain. #2 has been in use since c23. |

## State through this lens (measured)

- **Tempo map.** Unchanged since c24. 441 points; every printed tempo word and step is realised. Caesuras 72 / 104 / 392 / 632 / 664 / 816 / 888 / 1048 / 1108. Beat stretches at 375 / 451 / 167. The allargando still reaches 112 one beat early (886) by `RAMP_END_CLAMP`, then the 0.06 s caesura at 887.75.
- **Entries.** Medians per track -21..+16 ms (cor anglais +25), timpani +14, harp +4. The family medians per section are inside ±20 ms nearly everywhere. Tutti chord spread (first to last pc) is 50-155 ms (median about 100, as in c23).
- **Legato joins.**
  - Strings: medians -14..+17 ms, robust SD 44-46 ms.
  - Winds: -6..+13 ms, SD 9-22 ms.
  - Brass: -13..+5 ms, SD 24-33 ms.
- **Hammered eighths** (fold, eighth grid; basses / timpani):
  - 792-816: half-rise -30 / +20 ms, peak +45 / +35.
  - 816-840: -15 / +20, peak +55 / +40.
  - 984-1016: -27 / +23, peak +28 / +33.
  - 1056-1080: -17 / +28, peak +43 / +33.
  - 1088-1104: -19 / +21, peak +61 / +26.
  - The c23 lead change holds: the peaks are within 10-35 ms of each other.
- **Breaths before big entries** (master, 20 ms frames, minimum in the 150 ms before minus the level 0.3-0.6 s before):
  - 104: 15.1 dB; 392: 10.0; 600: 24.3; 632: 19.3; 664: 20.3; 816: 17.4; 840: 11.0; 1108: 20.8.
  - 888: 4.2 dB (+4.7 dB step); 1048: 6.4 dB (+0.5 dB step); 984: 3.2.
- **Tutti stops** (master, time to -20 dB): 240-380 ms at every stop.

## Findings

### 1. Role edges cross moved note-ons, so 67 notes start with a fader swell or fall inside their first 0.35 s; the worst sit on entries (measured)

**Where.** The `roles.json` rows, written by the role block of `tools/score_to_parts.py` (around line 4877). An unchained row start ramps over [a - 0.5, a] qn. A chained edge ramps over [a - 0.1, a + 0.15]. When the track's note is led, its moved note-on falls inside that ramp, so the ramp plays during the attack.

**Evidence (parts.json `vol_db`, change from the moved note-on to +0.35 s):**
- 67 notes change 2 dB or more: 29 entries after a rest and 38 legato joins.
- Celli, qn 264 (bar 67, "arco, espress.", the start of the E-flat theme): -2.9 -> +3.8 dB. The ramp runs 263.5-264.5 and the note starts at 263.498, so the whole 6.7 dB rise lies in the first 0.42 s of the note. The celli then had 1.1 s of rest before the note.
- Celli, qn 1016 (bar 255, ff accented "espress."): +0.9 -> +6.9 dB. The ramp runs 1015.5-1016.0 and the note starts at 1015.56, after 0.24 s of rest.
- Violins II / Violins I, qn 1088 (bar 273, Largamente, ff div. tremolo): -3.7 -> -8.5 and -4.0 -> -7.5 dB. The rows `[1088, 1116, -8.5]` / `[1088, 1116, -7.5]` ramp over 1087.5-1088.0, and the notes start at 1087.707 / 1087.756. So the first 0.1 s of the ff chord plays 5 dB louder, then the level falls. Each part has a 16 ms rest just before its moved onset.
- Further entries: Oboe 1 192 -3.9 dB, Violas 1032 -3.9, Bassoon 1 844 +3.5, Trumpet 2 892 -3.2, Violas 678 / 680 +3.0 / +2.9, Oboe 1 932 +2.9, Violas 384 +2.9, Bassoon 2 384 +2.9.
- On the stems, the celli 264 entry rises from -73 to -42 dB over 0.7 s, and pc is +197 ms. The celli at 1016 have pc +183 ms.

**Why the gate misses them.** Under Dan's standing rule each of these is a per-note fader move. stepcheck and guard26 put every move that touches a note edge in the "edge" class. guard26 lists 550 edge moves and gates none of them. These ramps start at or just before the moved onset, so they land in that class.

**Fix** (`tools/score_to_parts.py`, generic, default on):
- Add a rule `ROLE_EDGE_IN_REST = {"min_gap_s": 0.012, "max_ramp_qn": 0.5}`. For every role start, chained edge or end whose ramp contains a moved note-on of the track:
  - when the previous note ends at least 0.012 s before that note-on, run the ramp from max(previous end + 0.002 qn, note-on - 0.5 qn) to note-on - 0.005 qn;
  - when there is no gap (a legato join), keep the c26 placement and list the edge in the parts.json key `role_edge_join`.
- Celli 264: the ramp then becomes 263.0-263.49, in the rest. Celli 1016: 1015.06-1015.55.
- Violins I / II 1088: 1087.719-1087.751 and 1087.669-1087.702. This is the same kind of window the c26 `ROLE_EDGE_XF` entries used.
- If the actor does not want a step of 8 dB in a 16 ms rest, put the Largamente string level in CC7 from 1087.70 instead (the c26 `CC7_POINTS` method, manual p.64 / p.151). The CC7 value must be measured, because c26 measured CC7 90 = -3.0 dB and 80 = -4.0 dB, which follow no standard curve.
- Gate: add a stepcheck test "entry window". A fader change of 1.5 dB or more between the moved note-on and +0.35 s fails unless a printed sf / fp / sfp or a printed hairpin starts on that note.

**Targets.**
- Entry-window changes of 1.5 dB or more: 29 entries -> 0. Legato joins stay listed.
- Celli 264 pc +197 -> under +120 ms (what is left is the sample's own rise; inferred).
- Violins II 1088: the 0-0.35 s stem level flat within 1.5 dB after the attack.
- Body levels in 264.5-266 and 1088.5-1090 within 0.5 dB of c26.

### 2. The soft and mf cantabile string themes start 150-250 ms after the harp and basses (S2; measured; fix inferred)

**Where and evidence** (pc, ms):
- **qn 264, bar 67** (F2 in E-flat major, mf cantabile):
  - Violins I +189 (lead 0.30 s, already at the cap), Violins II +146, Violas +202, celli +197.
  - Harp +7, basses -4.
  - At this tempo (144) a quarter is 0.42 s, so the theme sounds nearly half a beat behind its accompaniment.
- **qn 744, bar 187** (the C major statement, mf cantabile): Violins II +161, Violas +168, basses +184 (Violins I +31, celli +51).
- **qn 424, bar 107** (p cresc.): Violins I +138, Violins II +206, Violas +158, celli +214.
- **Single sections:** celli 488 (p espress.) +219, Violas 937 (Poco più mosso, p) +240, Violins I 576 (f accent) +147.
- **qn 1016** (ff accented "espress." with a <> swell): Violins II +172 (Sus MAX, lead 22 ms), celli +183.
- **What the stems show.** Violins I at 264 climbs from -60 dB at 0.2 s before the beat to -39 dB at +0.3 s. That is a 0.5 s rise.
- **Cause.** The patch read (Manual notes) puts this rise in the recorded first-note sample. A 12-23 ms AHDSR attack does not explain it. Soft dynamics (CC11 62, CC1 70 at the note-on) select the slowest layer. Mockup-kit LEARNINGS (c07, c23) already found that extra lead only moves the quiet part earlier.

**Fix** (range test 262-270, 742-750, 1014-1018 against a control range, from starts that carry a keyswitch for every string track):
- **Variant A: the manual's row for this case** (p.99). Put the slur head after a rest of 0.5 s or more, at mp-f, on "StacSl Leg BC + Slur + Port MAX" (Violins I / II, Violas, celli; DIGEST p.99), with the slur's later notes joined as now. Use `ART_SPANS` per onset: 263.2-264.1, 743.2-744.1, 423.2-424.1, 487.2-488.1, 936.8-937.1. A new row means a full rebuild of these four tracks. Check memory (about 0.1-0.3 GB per row, MANUAL-GAPS memory plan).
- **Variant B: an instrument-side front.** CC11 +10 units from 0.06 s before the moved onset to +0.25 s, back to the lane value by +0.45 s (`INSTR_POST["cc_shape"]`, longer than the 120 ms fadeTime), on the same onsets. No fader move is involved.
- **At 1016:** if the row is accepted at 264, test the Violins II / Violas / celli heads on "Sus Marc LITE" at v80. Keep the printed <> in CC11.

**Targets:** the pc of every listed head under +90 ms, and within 60 ms of the harp or basses at 264 / 744. Body level 0.5-1.5 s after the onset within 1 dB of c26. 2-5 kHz first 80 ms minus body under -4 dB, so the head is not heard as an accent.

### 3. The fff arrival at bar 263 (qn 1048) is weaker than the end of its own crescendo on eight stems (measured; fix partly inferred)

**Where:** bars 261-263. The score (page 15) gives f (257) -> ff (259) -> fff (263) with crash fff, timpani fff, every wind and brass re-tonguing at 263 under a printed diminuendo, and celli "non div.". The printed breaths are staggered (1032, 1040, 1044), so no common silence is printed before 263.

**Evidence (quarter-note RMS: the first quarter of 263 minus the loudest quarter of bar 262):**
- **Fall at the arrival:** Bassoon 1 -6.3 dB, Flute 2 -4.6, Bass clarinet -3.8, celli -3.0 (their peak is 1046 at -21.1 dB), Bassoon 2 -2.0, Trumpet 1 -1.8, Violins I -1.8, Horn 3 -1.8.
- **Step at the arrival:** Horn 1 +4.4, Flute 1 +4.2, Contrabassoon +3.8, Violins II +3.4, Tuba +2.8, crash +27.
- **Master:** 1044-1047 -15.4 / -14.4 / -14.1 / -15.2 dB against 1048 -14.0, so +0.4 dB over the loudest beat. mp3: -13.1 / -12.2 / -12.4 / -13.7 against -12.0.
- **The same measure at 223:** brass +3.3..+8.4, strings +2.7..+4.3, master +4.6.
- **The cause is in the stems, not in the limiter.** Bassoon 1 plays two fresh Sus MAX notes (B3 at 1044, v118, CC11 109-110; C4 at 1048, v127, CC11 113-117), and the fff note sounds 6 dB softer. So the sample or a dynamic trim under the printed diminuendo outweighs a +4..+7 CC11 step. Which one I could not separate, because the trims are written by build_reaper.
- **Celli:** the "Leg BC MAX" crescendo note (1043.56, CC11 111-112, fader +2.2 -> +3.0 dB) peaks before the fff Sus MAX pair, whose CC11 falls back to 115 after the c26 front.

**On 223 against 263 (coordinator's question):** both are printed fff.
- 223 is the movement's tonal arrival: crash fff, bass drum ff, timpani fff with a diminuendo, all brass on whole notes, and a drop to f / mf in bar 224.
- 263 ends an 8-bar crescendo and carries a printed diminuendo through the bar.
- A tie is acceptable. If one must lead, 223 should lead by 0.3-0.5 dB, not 263. The real fault at 263 is the missing step, not the level.

**Fix:**
1. **Find which stems fall** (actor): read the written volume lane (vol_db plus the dynamic trims plus gain, guard26's reader) for Bassoon 1, Flute 2, Bass clarinet, celli, Trumpet 1, Violins I and Horn 3 over 1044-1050.
   - If a trim or a `HP_CURVE` diminuendo point acts in 1048-1049, start the printed diminuendo's fall after 1049.0, on CC11 (instrument side). Do not use the fader.
   - If the lane is flat, the fff sample is softer. Then add CC11 +8 on the 1048 note from 0 to +0.5 s, falling into the diminuendo (`INSTR_POST["note_cc"]`, CC1 on Trumpet 1, `CC1_DYN_TRACKS`).
2. **Shape the crescendo** (`build/score_config.py`, `HP_CURVE` per hairpin). For the 1032-1048 crescendos on the wind, brass and celli tracks, use (0.6, 0.45) instead of (0.4, 0.7), so the last two beats still rise. Keep `cresc_mono`.
3. **Fallback, delivery only:** the 1032-1047.8 ride row -1.0 dB over 1046.0-1047.9, back to its value at 1047.95.

**Targets:** each listed stem's first quarter of 263 at least +1 dB over its loudest quarter of bar 262; the master +2 dB or more (now +0.4); the mp3 +1.5 dB (now +0.8); final over 263 still 0.5 LU or more.

### 4. Brass legato joins in theme B, the stringendo and the Più allegro speak 60-160 ms late (S2; measured)

**Where and evidence** (pc / lead, `tools/pcx.py` joins):
- **Trumpet 1:**
  - 850 / 851 / 852 (bar 213, theme B, Largamente): +61 / +130 / +76 ms, lead 0.12 s.
  - 970 / 973 (bars 243-244, Poco più mosso): +110 / +128.
  - 989 (bar 248, the tenuto made a "Leg Slur MAX" target in c26): +158, lead 0.10 s.
  - 995.5 / 996: +70 / +97.
- **Horn 1:**
  - 818 / 819.5 / 821.5 (bars 205-206, accelerando): +151 / +106 / +120.
  - 970 / 978 / 992 / 994 / 1008 / 1010 / 1014: +62..+133.
- **Trumpet 1 elsewhere:** the medians are on time (-3 ms overall, theme B 842-848 +1..+31). So the late joins are particular intervals and dynamics, not a general offset.
- **989.** The tenuto is now late as well as the softest note of its slur (the coordinator's item). A tenuto in a slur is a separated, weighted note.

**Fix** (`build/leg_leads.json`, per-onset legato leads):
- +0.06 s on Trumpet 1 851 / 973, +0.04 s on 850 / 852 / 970 / 996, +0.06 s on Horn 1 818 / 821.5 / 1014, +0.04 s on Horn 1 819.5 / 994 / 1010.
- For Trumpet 1 989: return it to a fresh "Sus Non Vib MAX" attack (the row the slur already uses from 1000.5) with a 0.04 qn gap after 988, v110 and CC1 matched to its neighbours (about 90). Leave the CC11 bump out, which removes the c26 +24 unit swell. That is a tenuto as printed: on time, separated, level with the slur.
- Range test 836-856 and 966-1000 against a control.

**Targets:** listed joins under +50 ms; Trumpet 1 per-note level range 984-998 under 6 dB, with 989 within 2 dB of 991.

### 5. The celli still ring 0.5 s past the tutti stops of bars 2, 6 and 204 (measured)

**Where:** celli note-offs at qn 5.0, 21.0 and 813.916 (G2, v111). These stops did not get the c26 bar-94 / 113 treatment.

**Evidence** (time to -20 dB below each stem's level before the stop):
- Celli 540 ms at all three stops. The median of the loud stems is 160 ms (basses 120-130 ms).
- At +0.3 s the celli are at -39 dB against the master's -34 / -33, so they are the loudest dry stem in the tail.
- Their CC11 stays at 98 (bars 2, 6) and 94-90 (204) through the release.
- The mp3 drops are 15.3 / 15.0 / 15.1 dB: inside the band, but at its low end, and 1-1.5 dB under bars 94 / 113 (16.3 / 16.8) since their fix.

**Fix** (`build/score_config.py`, the c26 ruling-2 block, the same `cc_cap` form): add Violoncellos ceilings
- `{"lane": "cc11", "pts": [(4.944, 98), (5.224, 72), (5.80, 72), (5.84, 105)]}`
- `{"lane": "cc11", "pts": [(20.944, 98), (21.224, 72), (21.80, 72), (21.84, 105)]}`
- `{"lane": "cc11", "pts": [(813.86, 97), (814.14, 70), (814.70, 70), (814.756, 93)]}`

These run from 0.02 s before each note-off to 0.08 s after it, about -6 dB, and are held until the next entry's own value. They are instrument side, and each ramp is longer than the 120 ms fadeTime.

**Targets:** celli to -20 dB within 300 ms; mp3 drops at bars 2 / 6 / 204 of 16-17 dB.

## Coordinator's items

- **guard26's 73 printed-hairpin ramps; audible as per-note moves?** I could not recompute the dynamic trims (build_reaper). On the parts.json lane alone:
  - 185 held notes change 1.5 dB or more in some 0.5 s window, leaving out the final ring. 89 of them carry a hairpin that starts and ends on that one note (<> or >), and 41 are steeper than 6 dB/s.
  - Those I infer are heard as per-note moves, not as phrase dynamics: celli 1016 (5.9 dB in 0.5 s, on top of the finding-1 edge), Violins I / II 884-888 (5.0-5.3), Bassoons 1-2 at 318 (3.9-4.3), the chorale winds at 906-914 (3.2-3.9 per <>), Violins II 936 (4.1), Flute 1 156 (4.2: the late part of a 12-qn diminuendo).
  - Next step: rate-limit hairpin gains and dynamic trims to 3 dB/s inside one note. Spread the excess over the note, and carry what remains to the next note-on. Put the single-note <> and > shapes in CC11 (±10-14 units, longer than 0.12 s) instead of dB.
- **The 5 printed dynamic steps on legato overlaps:**
  - Clarinet 1 135.75, Violas 823.5 and Bassoon 1 320.1 are small steps at a note change. They are acceptable: a player changes level with the new note.
  - Celli 951.5 (-4.7 dB in 0.01 s, molto cantabile) and Harp 951.9 (-3.5) are steps after the hall in a quiet passage. Put the celli step in CC11 (about -12 units over 0.2 s from the moved onset).
- **Celli 870.4 +4.6 dB over 0.56 s** (8 dB/s inside a held note, bar 218): audible as a swell (inferred). Release that hairpin gain over 1.5 s or more.
- **223 against 263:** finding 3. A tie is acceptable by the score. The fault is the +0.4 dB step at 263 on the mix itself, because eight stems fall at the fff downbeat.
- **Violins I marcato fronts over Violins II:** not measured here. Only Violins II at 584 passes my entry filter (pc +17 ms); the other chord fronts follow a note with no rest, so my measure does not cover them.
- **Basses' pp re-bow swells, Bassoon 1 514, Flute 1 runs, muted Trumpet 1 joins, violas over Trumpet 1 at 840-842, celli 235-237:** level and articulation items, not measured here. Trumpet 1's 840-848 joins are on time (+1..+31 ms). Trumpet 1 989 is in finding 4: +158 ms late as well as soft.
- **Room-noise bed:** it does not move any timing figure. The stops' time to -20 dB on the mp3 is set by the music, not the bed (the c26 actor's simulation agrees).
- **Scherzo c24 items checked:**
  - Celli legato leaps of 6 or more semitones landing about 76 ms late: not reproduced here. The celli join median is +1 ms, and the >60 ms joins are spread over all intervals.
  - Slope guard skipping windows: confirmed in a new form (finding 1, the "edge" class).
- **Listening through the movement (earbuds, normal volume; inferred from the numbers):**
  - In order of what I expect a listener to notice: the second theme in the violins (bar 67) and its C major return (bar 187) entering late and swelling against a punctual harp and basses (findings 1-2); the 5 dB fall right after the Largamente chord of bar 273 (finding 1); bar 263 arriving without a step (finding 3); the late trumpet notes in theme B and at bars 243-248 (finding 4); a low cello ring after the opening stops (finding 5).
  - The tempo shape itself (rits., the 888 and 1048 caesuras, the stringendo) and the hammered sections hold together.

**Do not touch:**
- The tempo map with its ramps, `RAMP_END_CLAMP`, caesuras (72, 104, 392, 632, 664, 816, 888, 1048, 1108), beat stretches and lyrical arcs.
- The basses' 0.06 s stroke lead (peaks within 10-35 ms of the timpani) and `TIMP_DELAY_S` 0.02.
- The entry-lead tables (track medians -21..+16 ms) and the legato lead tables (join medians within ±17 ms).
- The chorale same-pitch gaps; the c26 stop ceilings at 373.9 / 449.9; `FINAL_RING`; CC16 resets; the 0.30 s mp3 head.
- No per-note move in the track volume envelope.

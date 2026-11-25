# Cycle 8, critic A: articulation and phrasing (render c07, score v600)

Method. All numbers come from the c07 render (`cycles/c07/render`: dry stems 01-31, return stems 32-35, `00_Master.wav`; no stem fix was applied) and the data that produced it (`cycles/c07/rendered_build/parts.json`, identical to `build/parts.json`). Times use the parts.json tempo map (`tools/pcx.py` TM). "Measured" means a number from the render, parts.json, the events file or a patch file. "Inferred" means reasoned but not tested. Measures used:
- **Repeat dip (S1).** Broadband 10 ms RMS: min(peak before, peak after) minus the minimum around the moved onset. Measured on the dry stem, on the dry stem plus its family return, and in the master's harmonic band of the repeated pitch (`pcx.band_env`).
- **Accent front (item 4).** 2-5 kHz over the first 80 ms against the 200 ms before the onset (the actor's "jump") and against the body (+0.15..+0.6 s). I also took the same jump in 0.25-1.5 kHz, so that a level jump can be told apart from a brightness jump.
- **Decays.** 30 ms RMS, 10 ms hop. The cut-off is aligned to the steepest fall within -0.2..+0.3 s of the nominal time. Values are -10 / -20 dB times and the drop at +0.3 s.

## Manual notes (cycle 8, slot A: second reading of 2021 manual PDF pages 95-99, strings effects and legato, read in full)

The first reading is `cycles/c02/reports/A.md`. Each of its notes is checked here against c07. The "Combinations" section that p.99 refers to is outside this range.

| Manual (PDF page) | Where it applies | c02 status | c07 status |
|---|---|---|---|
| p.95-96: pre-recorded one-octave runs (Vln I, Vla, Vc; KS / MOD / SPLIT direction) | None printed. The turn figures at bars 3-4, 199-203 and 263-264 are slurred eighths. | n/a | n/a |
| p.96: Repetitions Runs script; velocity ignored, CC11 sets the level | none | n/a | n/a |
| p.96-97: Slur Runs (Vln I/II); minimum speed is sixteenths at about 125 bpm (0.12 s per note) | Turn figures of eighths at 168-176 qpm (0.17-0.18 s per note) | Not used; slower than the stated minimum | **Unchanged, still not needed (measured).** The string legato joins sit within ±20 ms (c07 pcX). |
| p.97: Spiccato Runs (Vln II) | none | n/a | n/a |
| p.97: unmeasured Tremolo and Meas Trem TS. Neither responds to velocity; CC11 changes level and timbre during the note. | Every `:32` mark from qn 888 to 1112 | Yes | **Followed (measured).** 57 of 57 tremolo notes (Vln I 17, Vln II 16, Vla 14, Vc 8, Cb 2) play the Tremolo row. Their velocities (73-127) do nothing, as the page says. No tremolo note lasts over 6 s, so none needs a loop check. |
| p.98: trills | none | n/a | n/a |
| p.98: Repetitions (Violas, Basses). About a dozen pulses in a little over one second, tempo-synced, CC11 crossfades 3 dynamics, velocity ignored. The page stresses "the bow reversal, within the sample". | The basses' hammered eighths, 792-840 and 984-1108 | Not used (`STR_REP_DETACH`) | **Not used.** Bars 265-271 show the cost of the alternative: the Sus MAX bow-direction round robin puts the strong stroke on the off-beats (finding 2). The internal rate is still unmeasured (MANUAL-GAPS Results c42), so no row change is proposed. |
| p.98: sul ponticello (Violas) | none | n/a | n/a |
| p.98-99: legato. The patches are monophonic (CC22 64-127 makes them polyphonic). A slur or portamento needs no gap. Portamento "slides all the way ... passing very quickly over all the intervening notes". | All legato rows; "port." at bar 236 (Vln I/II C5 to A5, qn 941) | Mono rule followed; portamento not played | **Mono rule followed (measured).** On every legato row: 0 chords at one onset, 0 same-pitch overlaps, 0 overlaps over 0.2 s. Overlaps are 45 ms on strings and 35 ms on winds and brass (c02: 14 ms). **Portamento: on Leg Port MAX at v80 since c03, but no glide can be measured** (finding 5). |
| p.99: Legato Slur Staccato (a stronger attack on phrase-first notes) | KS rows exist | Not used | **Unchanged.** Not needed: slur heads already join the beat (c07 slur-head leads). |
| p.99: keyswitch rows | All tracks | Yes | **Followed (measured).** No keyswitch falls within 0.01 qn before the note it serves, and `ks_clash` is empty. |

MANUAL-GAPS items open in this lens: #2 (repetition rows: `REP_ROW` is empty in the Finale; the brass repeats work by gap, below), #7 (divisi and "4 soli", still deferred for memory) and #8 (slower legato: finding 5 is its one printed case).

## Standing checks on c07

- **Item 4, accent weight (measured, pass).** Brass accents in the Più allegro heads 984-1048, first 0.3 s minus the unaccented neighbours within 4 qn:
  - Horn 3 +1.2 dB, Trumpet 3 +2.2 dB, Trombone 1 +3.2 dB.
  - Violins I +2.7 dB, celli +3.8 dB.

  Accent brightness: finding 4.
- **Item 7, loop pulsing (measured, pass).** No wind or brass note runs over 6 s. Every string chain over 6 s from 880 on has a 3.95 s autocorrelation under 0.25, both for its harmonic band and for its spectral centroid:
  - Vln II 888: -0.19 / 0.02 and 0.09 / -0.14.
  - Vc 912: 0.13 / -0.01. Vc 1084: -0.21 / -0.05.
  - Cb 1048 (20.7 s): -0.11 / -0.16.

  The worst in the piece is Vc 563, bar 141, mp, 7 s: band 0.35.
- **Short notes (batch 7 items 2-3; measured).**
  - Every short-row note lasts 0.50 of its slot: wind Stac DblTng, Horn 1 Marc Shrt, string Stac / Staccatissimo, 0.179 s. That is inside the 50-62 % target.
  - Velocity is flat by position: string staccatos 105-118, winds 97-104.
  - There are almost no running short figures to shape, though. The short notes are single off-beat quarters and eighths, one to three per bar. So beat-position velocity has few targets on this score. Its real target is the bass ostinato (finding 2).
- **S1, Trumpet 3 in the Più allegro: close the item (measured).**
  - The dry stem's repeats dip 10.4 dB (median of 33).
  - The "dry+return" figure of 0.5-2.4 dB at 1018-1038 comes from the shared R Brass return.
  - In the master's own harmonic band of each pitch, the repeats dip a median 4.4 dB. Where they do not (1018, 1026, 1028), another part holds the same pitch class through the repeat: Horn 2's C4 whole note at 1016, Oboe 2's C5 and Trombone 2's C3 at 1024. A real orchestra would mask those repeats the same way.
- **Wetness ceiling (coordinator; measured).** The c07 claims hold:
  - Tutti cut-offs fall 20 dB in 0.36 / 0.37 / 0.39 / 0.49 / 0.27 s (qn 101 / 21 / 5 / 661 / 1112; c07 claimed a 0.41 s median).
  - RT60 at the final cut-off is 1.29 s from the -10..-30 dB slope (claimed 1.22).
  - Return energy is 13.8 dB under the dry sum (claimed 12.5; I mixed to mono, the actor did not).

  The ceiling is met, and the opposite risk is now real at the cut-offs. Three of the five fall faster than any reference (0.43-0.55 s). The returns add only 1-2 dB to the drop at +0.3 s (master 16.0 / 16.6 / 18.7 / 21.4 dB against dry-only 17.2 / 18.3 / 19.5 / 23.2). See finding 1 for the final chord.
- **Movement I c50 template corrections (read from mix.json):**
  - Timpani: Close 0.2 / Main 0.5, no Surround mic, no 84 Hz bell. Followed.
  - Harp: high pass at 80 Hz. Followed.
  - Winds and crash: the c06 stem fix took -2.9 / -3.4 dB. Followed.
  - Brass make-up per instrument and dynamic: **still one value per group** (horns 2.0, trumpets 1.8, trombones 5.0, tuba 7.0). That is critic B's lens.
  - No trumpet 4 kHz boost stacks on the family shelf. The trombones' 4 kHz -4 dB shelf is a cut, so the rule does not apply to it.

## 1. The final fff chord stops dead: 20 dB down in 0.27 s, with trumpets and violas 46-47 dB down by +0.3 s (releases; measured, fix inferred)

**Where.** qn 1112-1113 (bar 279, Largamente, fff), followed by the rest with a fermata at 1114. Every pitched track.

**Evidence.**
- The master falls 10 / 20 / 30 / 40 dB in 0.09 / 0.27 / 0.52 / 0.77 s. Its drop at +0.3 s is 21.4 dB.
  - Recordings: tutti stops fall 20 dB in 0.43-0.55 s (Brahms 1/i), with 13-17 dB at +0.3 s.
  - Movement I c50's floor is "at least 15 dB" at +0.3 s.
  - This is the last sound of the movement, and it falls faster than every other cut-off in the piece.
- Per stem, level at +0.25..+0.35 s against the master's level just before the cut:

  | stem | relative level |
  |---|---|
  | Trumpets 1-3 | -57 / -57 / -61 dB |
  | Violas | -62 dB |
  | Clarinets | -52 / -53 dB |
  | Tuba | -44 dB |
  | Horns | -38 dB |
  | Double basses | -39 dB |
  | R Perc | -24 dB |
  | R Brass | -27 dB |
  | R Strings | -27 dB |

  The return stems are the loudest thing left. The dry stems fall 30-47 dB in 0.3 s because of three things together:
  - the release caps (strings 150 ms at ff, horns 237 ms);
  - `CUTOFF_EARLY_S` (brass notes end at 1112.904, strings at 1112.88);
  - no hall send on the low brass, and -10 dB on the trumpets (batch 5).
- **Raising the returns does not fix it (simulated on the c07 stems):**
  - At +3 dB on all four returns, the final cut-off's -20 dB time goes 0.27 -> 0.32 s, and qn 101 to 0.56 s, past the 0.50 s ceiling.
  - At +6 dB the final cut-off reaches only 0.37 s, and the median runs over the ceiling (0.51 s).

  The fix belongs on the dry side: the notes' own release.

**Fix.**
- `tools/score_to_parts.py`: add a generic `FINAL_RING = {"at": 1112.0, "ring_s": 0.45, "fall_db": -24.0, "tracks": "pitched"}`. On the notes that sound at `at`:
  - skip `CUTOFF_EARLY_S`;
  - extend the note-off by `ring_s`;
  - write a volume-envelope fall from 0 dB at the written end (1113.0) to `fall_db` at end + `ring_s`, in a curved (exponential-like) shape: -8 dB at 0.15 s, -16 at 0.3 s.

  The sends are post-fader, so the returns follow the fall and keep their own tails. This fall is a release, not a subito, so S3 does not apply.
- Leave the release caps alone (they serve every other cut-off), and leave the returns at c07 levels.
- Targets on the c08 master:
  - final cut-off -20 dB in 0.40-0.50 s;
  - drop at +0.3 s 14-17 dB;
  - no stem level step at 1113.0;
  - the 1113.2 crash and bass-drum damp unchanged.

## 2. The basses' f ostinato in bars 265-271 accents the off-beats: every off-beat eighth is 1-2 dB over the beat, in every bar (S1 / batch 7 item 2; measured)

**Where.** Double basses qn 1056-1088 (bars 265-272, f, after the fff crash at 263). Plain eighths, all on Sus MAX at v83, 0.47 qn each.

**Evidence.**
- Level in the first 120 ms of each eighth on the dry stem, bars 266-270, identical in every bar: beat 1 -41, "and" -40, beat 2 -42, "and" -40, beat 3 -42, "and" -40, beat 4 -42, "and" -40 dB. In bar 271 the off-beats are up to 4 dB over the beats.
- The same rules in the coda (792-816) give downbeat 0, beats -2.5, off-beats -4.5 dB, which is right. In 984-1048 the off-beats sit -3.5 dB under the downbeat.
- `METRIC_BOWED_DB` (down +1.0, mid +0.5, beat 0, off -0.5) covers 984-1080, but its 1.5 dB range loses to the bow-direction round robin. Here the strong stroke lands on the off-beats. Movement I's c49 lesson: which note gets the strong sample does not follow the count of earlier notes.
- Research batch 7: strong beats 15-25 velocity steps over the weakest, about 3-5 dB on short rows.

**Fix.**
- `tools/score_to_parts.py` METRIC_BOWED: allow a per-span table, `METRIC_BOWED_DB_SPANS = {"Double basses": [(1056.0, 1088.0, {"down": 1.5, "mid": 1.0, "beat": 0.0, "off": -2.5})]}` in `build/score_config.py`. That is 4 dB from downbeat to off-beat, the coda's measured shape.
- Extend `METRIC_BOWED["Double basses"]` to (984.0, 1088.0) so that bar 271 is covered.
- Target on the c08 stem, 1056-1088: downbeat minus off-beat +3..+4.5 dB, beat minus off-beat at least +1.5 dB in every bar.
- If the round robin still wins, add a CC36 reset 0.25 qn before 1056 (`cc36` lane). That is the "mid-music reset" Movement I c49 left untested; it may flip which stroke is strong (inferred).

## 3. Four printed notes play as silent or near-silent stubs: the unison "outlast" rule turns a held note into a late 0.25-0.84 qn tail (measured)

**Where.**
- Oboe 2 F5, sq 844 (bar 212, ff, 4 qn): played 846.75-847.59. Oboe 1 has F5 for 3 qn and then moves to F♯5, so the printed F5 against F♯5 rub is lost.
- Oboe 2 E♭5, sq 856 (bar 215, ff, 4 qn): played 858.75-859.59 against Oboe 1's F5.
- Horn 1 E♭4, sq 118 (bar 30, mf, 2 qn): played 118.75-119.5.
- Horn 2 B♭3, sq 122 (bar 31, mf, 2 qn): played 123.25-123.5.

**Evidence.** These are the only four notes in parts.json whose moved onset is more than 0.3 qn after the score onset. All four are in the render's own silent-note list (`metrics.md`): -200.0 / -22.8 dB A for Oboe 2 856 / 844 against a track median of 24.9, Horn 1 118 at -2.5 against 17.7, Horn 2 122 at -27.7 against 15.5.

The rule is `find_unisons()` in `tools/score_to_parts.py`, the c17 branch: "a copy that outlasts the kept note ... starts where the kept note leaves". A wind or brass sustain that starts mid-phrase at ff for under one beat, behind a -12 dB / 0.2 s fade and a re-tongue lead, barely speaks.

**Fix.** In that branch, when a copy outlasts the kept note by more than `UNI_OUTLAST_QN`:
- play the copy from its own onset as one note;
- put a volume shape on it: -6 dB from its onset to the kept note's end, then a 0.25 qn ramp to 0 dB.

That keeps the dissonance, and the unison is at most +1.8 dB louder. Alternatively, make the outlasting copy the kept note, but not when the other copy is slurred: Oboe 1 is slurred at 844 / 856, and dropping its notes would break its line.

Target: none of the four in the c08 silent-note list, and each within 6 dB of its track's median at its printed dynamic.

## 4. The brass-accent "2-5 kHz jump" (p90 5.2 dB) measures level, not bite; no brass EQ brings it under 2 dB (item 4; measured)

**Evidence (98 brass accents, c07 master).**

| measure | median | p90 |
|---|---|---|
| 2-5 kHz jump (the actor's measure) | -3.1 | 5.2 |
| 0.25-1.5 kHz jump | -2.7 | 3.6 |
| broadband jump | -2.4 | 3.3 |
| 2-5 kHz jump minus 0.25-1.5 kHz jump (tilt jump) | +0.1 | 3.6 |
| 2-5 kHz front minus body (the brief's own measure) | -10.5 | -6.2 |

- The largest jumps are entries after a rest or a step up in level. The 2-5 kHz and mid jumps there are about equal:
  - 816 (bar 205): 13.1 vs 14.7 dB.
  - 104: 11.5 vs 14.7 dB.
  - 632: 11.3 vs 10.8 dB.
  - 1108: 10.4 vs 9.9 dB.
- On the brass stems themselves, the accent fronts sit under their bodies: Horn 1 -14.6, Trombone 1 -11.8, Tuba -17.3 dB at 360.
- **EQ simulations on the c07 stems** (brass stems plus R Brass replaced by their EQ'd versions):

  | variant | jump p90 | tilt-jump p90 |
  |---|---|---|
  | 821 Hz bell -7.8 -> -4 dB, with -3.8 dB make-up | 4.4 | 3.5 |
  | 3.2 kHz -3 dB, 1 oct | 4.6 | 3.5 |
  | 3.2 kHz -3 dB, 1.5 oct | 4.5 | 3.5 |
  | 3.2 kHz -6 dB, 1.5 oct | 3.9 | 3.4 |

  None reaches 2, because a static EQ moves the "before" and "after" windows together.
- Accents whose tilt does jump:
  - qn 360 (bar 91, the codetta trumpets, ff): Trumpet 1 / Trumpet 2 tilt front minus body +5.4 / +6.4 dB on Sus Non Vib MAX at v111.
  - 1058 / 1066 (bars 265-267): Horn 1 on Leg Slur MAX v100, +4.1 / +5.2 dB 2-5 kHz front over body.

**Fix.**
- Leave the brass family EQ as it is. If the actor wants a small, safe brightness cut anyway, use a 3.2 kHz -3 dB bell, 1.5 oct (brass group `family_eq`), and expect the jump p90 to fall only 0.7 dB.
- Replace the check in `cycles/*/actor_scripts/accjump*.py` with the tilt jump (2-5 kHz jump minus 0.25-1.5 kHz jump). Target p90 under +3 dB, plus the per-stem front minus body under +3 dB on every accent.
- Treat the few bright accents one by one, in `build/score_config.py`:
  - Trumpets 1-2 at 360 ff: accent velocity 111 -> 95 (`ACC_VEL` or an `accent_fits.json` row; the brass Sus rows take dynamics on CC1, so velocity mostly shapes the attack, inferred). Target: tilt front minus body under +2 dB.
  - Horn 1 at 1058 / 1066 (accented notes inside the slur): `GENTLE_ACCENT` swell instead of the Leg Slur target's attack, or legato velocity 100 -> 90 on those two targets, with the +1.1 ms per step lead compensation.
- Record the rejected target in LEARNINGS with these numbers.

## 5. The bar-236 portamento has no audible glide (manual p.98; measured)

**Where.** Violins I and II, C5 -> A5 at qn 941 (bar 236, Q, molto cantabile, "port."), on Leg Port MAX at v80 (`PORT_TARGETS`, c03).

**Evidence.**
- Share of the 480-950 Hz energy that falls between semitones 73.5 and 79.5 (the passing pitches), in 30 ms frames every 5 ms from the moved onset: maximum -10.4 dB on Violins I (+10 ms) and -8.9 dB on Violins II (+205 ms). It is under -11 dB almost everywhere else.
- A spectral-peak track (85 ms window) jumps straight from 72 to 81, with no frame in between.
- Manual p.98: the pitch "slides all the way". On these KS Masters, velocity sets the LegatoSpeed start offset (v30-127 -> 0-4800 samples; kit section 5). At v80 about 2500 samples, roughly 50 ms of the recorded slide, are skipped (inferred from the map).

**Fix.**
- `build/score_config.py` `PORT_TARGETS = {"Violins I": {941.0: 45}, "Violins II": {941.0: 45}}`. That is about 900 samples skipped (inferred).
- A slower slide arrives later, so add 0.04 s to both targets in `leg_leads.json`, then refit on c08 pcX. Movement I c15 saw one join move 0.29 s for 0.10 s of lead.
- Target: passing-pitch share at -3 dB or above for 60-120 ms, and the A5 arrival (pcX) within ±40 ms of the beat.

## 6. Three string repeats still merge (S1; measured): Vc 828 and 832, Vln I 884

**Where and evidence (dry stem, dry+R Strings, master band).**
- Violoncellos 824 -> 828, G♯2 whole note to G♯2 whole note, unslurred (bar 208, f <): gap 90 ms, but the dips are only 1.5 / 4.1 / 2.5 dB. The 824 note is on Leg Slur MAX and 828 on Sus MAX. The legato note's release fills the gap, and the Sus MAX attack is slow.
- Violoncellos 828 -> 832, the held G♯2 to the same pitch at the head of the slurred run: gap 10 ms, dips 3.7 / 2.6 dB.
- Violins I 880 (div. chord F5 + B5) -> 884 B5 "unis.": gap 10 ms (0.03 qn), dips 3.9 / 2.5 / 2.5 dB.

c07 A #5 named these three. The actor restricted the chord rule to non-legato rows, so they are untouched.

**Fix (`build/score_config.py`):**
- Add the celli span (824.0, 836.0) to `STR_REP_DETACH["at"]["Violoncellos"]`: the post-hall -5 dB / 0.08 s dip that gives the basses 10 dB.
- Let `STR_REP_NEW_BOW` treat a slur head that repeats the held pitch as a new bow, gap 0.09 s / frac 0.3, for Vc 832.
- Do the same for a same-pitch note that follows a div. chord voice (Vln I 884), whatever row the next note uses.

Target: dry dips of 5 dB or more at all three, with the hidden pp re-bows unchanged (11 ms).

**Do not touch:**
- The release caps per dynamic, and the c07 return levels and envelope. The wetness ceiling holds; fix the final chord on the dry side.
- The legato overlap floors (45 / 35 ms) with velocity by dynamic, floor 100, and the 1.1 ms-per-step lead compensation. The mono-legato data are clean.
- All 57 tremolo assignments from 888.
- Short notes at 0.50 of the slot on the Stac / Staccatissimo / Stac DblTng / Marc Shrt rows, and the string staccato velocity by level.
- The basses' coda metric shape (792-816: downbeat 0, off-beat -4.5 dB) and their 10 ms gap plus detach dip.
- The brass re-tongue at 0.10 s (Trumpet 3 dry repeats 10.4 dB).
- The muted Trumpet 1 solo: joins dip 2.1 dB with front minus body -8.2 dB median, against 2.2 / -5.9 on the cor anglais it doubles.
- The re-bow stagger (no loop autocorrelation over 0.25 from 880 on).
- The harp glissando at 277.
- Percussion on the grid: crash -6 dB at +28..+34 ms, bass drum at +8 ms.
